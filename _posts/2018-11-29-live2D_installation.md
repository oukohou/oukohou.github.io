---
layout: post
title:  "给自己的jekyll安装一个萌萌哒二次元看板娘"
date:   2018-11-29 12:20:06 +0800--
categories: [部署]
tags: [moe, live2D, ]  
---

啥是live2D看板娘？就是右下角这个萌萌萌萌哒而且可以跟你的鼠标互动的卡通啦～～  
萌不萌？是不是超萌え？  
想不想在自己的jekyll博客上也安装一个哦？  
如果你是 hexo + github pages 的组合博客，你有福了，作者就是在hexo上开发的，具体参见作者的这个github repo:
[hexo-helper-live2d](https://github.com/EYHN/hexo-helper-live2d)，按照说明安装即可。  
那么像我这样 jekyll + github pages 组合的朋友们可如何是好？  
不要担心，这篇博客就是教你如何一步一步一步一步地给自己的博客添加一个萌萌萌萌哒看板娘。  
 
首先饮水思源，这篇博客的步骤大体上是参照[这篇博客](https://done.moe/tutorial/2018/08/11/how-to-add-cute-live2d-in-jekyll-blog/#fnref:1)，
但当然不是全盘照抄，这种事我还是不屑为之的，如果完全一样，我会像我的另一篇博客[爱因斯坦求和约定](https://www.oukohou.wang/2018/10/25/Einstein-summation-convention/)
那样直接给出原文链接即可。  
主要是参照安装的过程中，遇到了很多意外，这里一一记录下来，以备后事之鉴。虽然应该不会有资于治道了，但至少应该有资于安装live2d吧？  
  
以下是安装步骤： 

### 1. 安装hexo：  

```bash
sudo npm install hexo-cli -g # 不加sudo的话会出现权限问题  
hexo init blog_demo  
cd blog_demo/  
npm install hexo --save  #同理，只使用npm install的话下一步hexo server会报错  

```

遇见警告：
```text
WARN engine hexo@3.8.0: wanted: {"node":">=6.9.0"} (current: {"node":"4.2.6","npm":"3.5.2"})
WARN engine hexo@3.8.0: wanted: {"node":">=6.9.0"} (current: {"node":"4.2.6","nploadDep:warehouse → 304   ▄ ╢██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╟
WARN engine nunjucks@3.1.4: wanted: {"node":">= 6.9.0 <= 11.1.0"} (current: {"noloadDep:warehouse → cache ▀ ╢██████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╟
WARN engine hexo-fs@0.2.3: wanted: {"node":">=6.9.0"} (current: {"node":"4.2.6",npm WARN deprecated titlecase@1.1.2: no longer maintained
loadDep:readable-stream → ▄ ╢███████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╟
WARN engine readable-stream@3.0.6: wanted: {"node":">= 6"} (current: {"node":"4.loadDeloadDep:set-valuloloadDep:static-extend → a ▄ ╢███loadDep:urix → addNameRan ▐ ╢█████████████████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░╟
```

更新node：
```bash
# 先在系统上安装好nodejs和npm
sudo apt-get install nodejs-legacy
sudo apt-get install npm

# 升级npm为最新版本
sudo npm install npm@latest -g

# 安装用于安装nodejs的模块n
sudo npm install -g n

# 通过n模块安装指定的nodejs（3选一）
sudo n latest
sudo n stable
sudo n lts

# 查看版本
sudo node -v
```


继续hexo调试：
```bash
hexo server
```
出现：
```text
INFO  Start processing
INFO  Hexo is running at http://localhost:4000 . Press Ctrl+C to stop.
```

至此成功安装了hexo.

### 2. 安装live2D：
```bash
yarn add hexo-helper-live2d
: <<!
提示：
The program 'yarn' is currently not installed. You can install it by typing:
sudo apt install cmdtest
!
# 照做：
sudo apt install cmdtest
# 再来：
yarn add hexo-helper-live2d
```
报错：
```text
ERROR: [Errno 2] No such file or directory: 'add'
```
百度一下，发现：
> [stackoverflow 上的一个解决方案](https://stackoverflow.com/questions/46013544/yarn-install-command-error-no-such-file-or-directory-install)

照做：
```bash
sudo apt remove cmdtest
sudo apt remove yarn
curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | sudo apt-key add -
echo "deb https://dl.yarnpkg.com/debian/ stable main" | sudo tee /etc/apt/sources.list.d/yarn.list
sudo apt-get update && sudo apt-get install yarn
```
然后再试一次：
```bash
yarn add hexo-helper-live2d
```
这次成功了，下一步。  
将下面的代码添加到Hexo博客的配置文件_config.xml中：  
```yaml
live2d:
  enable: true
  scriptFrom: local
  pluginRootPath: live2dw/
  pluginJsPath: lib/
  pluginModelPath: assets/
  tagMode: false
  debug: false
  model:
    use: unitychan
  display:
    position: right
    width: 150
    height: 300
  mobile:
    show: true
```

到[live2d-widget-models](https://github.com/xiazeyu/live2d-widget-models)直接把整个项目clone下来。  
解压即可看到package里众多可选的形象，这里随机选一个unitychan。  
找到项目里的live2d-widget-model-unitychan文件夹，把里面assets里面的内容(不含assets文件夹)，
拷贝到Hexo的blog文件夹下新建一个live2d_models\unitychan文件夹中。  
一切就绪，再次启动：  
```bash
hexo server
```
点击打开[http://localhost:4000/](http://localhost:4000/)即可发现萌萌哒看板娘了。  
然后运行：
```bash
hexo generate
```
生成静态文件，会在博客根目录下生成一个public文件夹。  
在public文件夹中找到live2dw文件夹，就是你部署到jekyll博客上所需要的资源了。  
而引用这些资源的代码就在public/index.html最底下的一行：
```html
<script src="/live2dw/lib/L2Dwidget.min.js?0c58a1486de42ac6cc1c59c7d98ae887"></script><script>L2Dwidget.init({"pluginRootPath":"live2dw/","pluginJsPath":"lib/","pluginModelPath":"assets/","tagMode":false,"debug":false,"model":{"jsonPath":"/live2dw/assets/unitychan.model.json"},"display":{"position":"right","width":150,"height":300},"mobile":{"show":true},"log":false});</script></body>
```
将live2dw拷贝到jekyll博客目录下，然后将这段引用代码写到你的jekyll博客布局html里，把对应路径改了。  
然后你的博客上就会出现一个可以跟随你的鼠标互动的萌萌哒二次元啦～～  

### 3. bonus！  
经过以上这些步骤，是不是觉得有点繁琐？  
不用担心，好心的我已经把这些全部都编译一遍并且分享出来啦！   
剩下的你只需要照着[2](###2.安装live2D：)中最后两步，下载我分享的静态文件，然后拷贝到jekyll目录，并把
引用代码对应路径修改一下，就可以用到你的jekyll博客上了!    
开不开心！惊不惊喜！  

- 百度网盘:    
  链接：[https://pan.baidu.com/s/1NrRkNR70X1jNN6aB3GS8EA](https://pan.baidu.com/s/1NrRkNR70X1jNN6aB3GS8EA)     
  提取码：8dy2   

- google driver:  
  ~~这会儿网不好，先不往google driver上传了，等网好了传。~~  
  [https://drive.google.com/drive/folders/1jG5T6GBzmDT1y5xhLV15H_YrzKUpn-S6?usp=sharing](https://drive.google.com/drive/folders/1jG5T6GBzmDT1y5xhLV15H_YrzKUpn-S6?usp=sharing)      

怎么样，是不是喜出望外？  
激动地想要[打赏](https://www.oukohou.wang/donate/)我却不知如何打赏?  
不用担心，体贴的我也早已料到了这一痛点，特地写了个页面:  
- [打赏传送门](https://www.oukohou.wang/donate/)  

点击上面的传送门然后在里面痛快地撒个野吧!   

![kitai](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/anime/gakki_kitai.jpg)  



  
<p  align="right">regards.</p>
<h4 align="right">
    <a href="https:www.oukohou.wang">
        oukohou.
    </a>
</h4>

