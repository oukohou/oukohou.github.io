#! /usr/bin/env python
# -*- coding: utf-8 -*-

# *************************************************************
#  Copyright (c) Huoty - All rights reserved
#
#      Author: Huoty <sudohuoty@gmail.com>
#  CreateTime: 2016-12-03 22:07:39
# *************************************************************

import os
import signal
import logging

import tornado.web
import tornado.gen
import tornado.template
import tornado.ioloop
import tornado.httpserver
from tornado.log import enable_pretty_logging, app_log as log


class IndexHandler(tornado.web.RequestHandler):
    """处理目录形式的请求"""

    def initialize(self, root=None, autoindex=False):
        self.root = root if root else '.'  # 站点根目录
        self.autoindex = autoindex  # 是否自动显示目录
        self.path = None            # 当前请求的路径
        self.local_path = None      # 请求路径对应的本地路径

    def get(self, path):
        """处理 GET 请求

        如果目录下有 index.html 则响应该页面
        当目录下没有 index.html 文件时：
            如果 autoindex 为 True, 则显示目录下的内容, 否则返回 404.
        """
        if os.path.sep != "/":
            path = path.replace("/", os.path.sep)
        self.path = path
        del path  # 确保能用 self.path 代替请求的路径
        self.local_path = os.path.abspath(os.path.join(self.root, self.path[1:]))
        if not os.path.exists(self.local_path):
            self.write_404()
        else:
            index = self.find_index()
            if index:
                with open(index, 'rb') as f:
                    self.write(f.read())
            elif self.autoindex:
                self.write(self.generate_index())
            else:
                self.write_404()
        self.finish()

    def find_index(self):
        """查找请求的目录下是否有 index 文件"""
        for index in ('index.html', 'index.htm'):
            index = os.path.join(self.local_path, index)
            if os.path.exists(index):
                return index
        return None

    def generate_index(self):
        """生成 index 文件, 并列出目录下的所有文件和目录"""
        files = [filename + '/' if os.path.isdir(os.path.join(self.local_path, filename)) \
            else filename for filename in os.listdir(self.local_path)]
        html_template = """
        <!DOCTYPE html><html>
        <title>Directory listing for /{{ path }}</title>
        <body>
        <h2>Directory listing for /{{ path }}</h2>
        <hr>
        <ul>
        {% for filename in files %}
        <li><a href="{{ filename }}">{{ filename }}</a>
        {% end %}
        </ul>
        <hr>
        </body>
        </html>
        """
        t = tornado.template.Template(html_template)
        return t.generate(files=files, path=self.path[1:])

    def write_404(self):
        """生成 404 页面"""
        # 首先查找根目录下下是否有 404 文件, 有就直接响应它
        html_404 = os.path.join(self.root, "404.html")
        if os.path.exists(html_404):
            with open(html_404, 'rb') as f:
                html = f.read()
        else:
            html = """
            <!DOCTYPE html><html>
            <title>404 Not Found</title>
            <body>
            <div style="padding: 40px 15px;text-align: center;">
            <h2>404 Not Found</h2>
            <div>Sorry, an error has occured, Requested page not found!</div>
            </div>
            </body>
            </html>
            """
        self.set_status(404)
        self.write(html)


class StaticFileHandler(tornado.web.StaticFileHandler):
    """处理静态文件请求"""

    @tornado.gen.coroutine
    def get(self, path, include_body=True):
        """处理 GET 请求

        当请求的路径为目录时，重定向给 IndexHandler 处理
        """
        self.path = self.parse_url_path(path)
        local_path = self.get_absolute_path(self.root, self.path)
        if not os.path.exists(local_path):
            raise tornado.web.HTTPError(404)
        elif os.path.isdir(local_path):
            self.redirect("/{path}/".format(path=self.path), permanent=True)
        else:
            super(StaticFileHandler, self).get(path, include_body)

    def write_error(self, status_code, **kwargs):
        """自定义错误页面"""
        html_404 = os.path.join(self.root, "404.html")
        if status_code == 404 and os.path.exists(html_404):
            with open(html_404, 'rb') as f:
                html = f.read()
            self.finish(html)
        else:
            self.finish("""
            <!DOCTYPE html><html>
            <title>{code} {message}</title>
            <body>
            <div style="padding: 40px 15px;text-align: center;">
            <h2>{code} {message}</h2>
            <div>Sorry, an error has occured, Requested page {message}!</div>
            </div>
            </body>
            </html>
            """.format(code=status_code, message=self._reason)
        )


def stop_server(signum, frame):
    tornado.ioloop.IOLoop.instance().stop()
    log.info('Server stopped!')

def main():
    from argparse import ArgumentParser
    parser = ArgumentParser(prog="SimpleTornadoServer",
                            description="A simple HTTP server based on tornado")
    parser.add_argument("-H", "--host", default="127.0.0.1",
                        help="Host to bind to")
    parser.add_argument("-p", "--port", type=int, default=8000,
                        help="Port to listen on")
    parser.add_argument("-r", "--root", default=".",
                        help="Root directory of the server")
    parser.add_argument("-l", "--autoindex", action="store_true",
                        help="List all files and dirs")
    parser.add_argument("-d", "--debug", action="store_true",
                        help="Debug mode")

    options = parser.parse_args()

    if options.debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
    enable_pretty_logging()
    log.info('Serving site from local directory: %s' % os.path.abspath(options.root))

    handlers = [
        (r'(.*)/$', IndexHandler, dict(root=options.root, autoindex=options.autoindex)),
        (r'/(.*)$', StaticFileHandler, dict(path=options.root)),
    ]
    settings = dict(
        debug=options.debug,
        compress_response=True,
    )

    app = tornado.web.Application(handlers, **settings)
    http_server = tornado.httpserver.HTTPServer(app, xheaders=True)
    http_server.listen(options.port, options.host)
    log.info("The server is running at: http://{host}:{port}/".format(**vars(options)))
    signal.signal(signal.SIGINT, stop_server)
    tornado.ioloop.IOLoop.instance().start()


# Script starts from here

if __name__ == "__main__":
    main()
