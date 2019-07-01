---
layout: post
title:  "使用我的jekyll博客主题的注意事项"
date:   2018-12-18 20:13:53 +0800--
categories: [部署]
tags: [notices, help]  
---

**首先要感谢你使用我的博客主题！**  
[我的独立博客](http://www.oukohou.wang/) 主题基于 [maupassant-jekyll](https://github.com/alafighting/maupassant-jekyll.git) 
重新修改和优化，同时很大程度上参考了 [kuanghy](https://github.com/kuanghy) 的博客主题 [luring](https://github.com/kuanghy/luring)，感谢。  
希望你在介绍自己的博客主题时，也能像上面一样，援引一下我的博客主题～～  

我的博客主题里加了一些自己定制化的内容，其中涉及到一些信息获取的事宜(比如百度统计的代码，你不改的话，
我可以直接获取到你的网站的各种访问信息呦🙈)，所以在这里单独成文，提醒一下：  

### 1. 百度统计
百度统计的代码在
```text
./assets/js/tongji.baidu.js
```
引用代码在
```text
./_layouts/base.html:
    <script type="text/javascript" src="/assets/js/tongji.baidu.js"></script>
```
关于百度统计，你可以在这个页面： [百度统计-管理](https://tongji.baidu.com/sc-web/26979727/home/site/index?from=3)
添加自己的网站，然后就会得到类似如下的统计代码段：  
![baidu-tongji-codes](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/notices_for_fork_theme/baidu%E7%BB%9F%E8%AE%A1%E4%BB%A3%E7%A0%81.png)  
copy这一段代码，去除首尾的$script$标签，即可部署完成你自己的百度统计。  
等待20分钟左右，再点击 [百度统计](https://tongji.baidu.com/web/26979727/homepage/index) 页面，你应该可以看到网站分析数据。  

### 2. google统计
google analytics的代码在
```text
./_layouts/base.html:  
```
的  
```html
    <!-- Global site tag (gtag.js) - Google Analytics -->
    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-130856615-1"></script>
    <script>
        window.dataLayer = window.dataLayer || [];

        function gtag() {
            dataLayer.push(arguments);
        }

        gtag('js', new Date());

        gtag('config', 'UA-130856615-1');
    </script>
```
跟百度统计的流程类似，添加网站之后获得统计代码，覆盖掉即可。  
具体可以访问： [google analytics](https://analytics.google.com/)，google自身的引导做得很好，你可以自己操作的。  

### 3. live2D看板娘
>啥是live2D看板娘？就是右下角这个萌萌萌萌哒而且可以跟你的鼠标互动的卡通啦～～  
萌不萌？是不是超萌え？  

我的部署代码在：
```text
./_layouts/base.html:  
```
的  
```html
    <!--live2d function-->
    <script src="/assets/live2dw/lib/L2Dwidget.min.js"></script>
    <script>L2Dwidget.init({
        "pluginRootPath": "live2dw/",
        "pluginJsPath": "lib/",
        "pluginModelPath": "assets/",
        "tagMode": false,
        "debug": false,
        "model": {"jsonPath": "/assets/live2dw/assets/unitychan.model.json"},
        "display": {"position": "right", "width": 100, "height": 180, "hOffset": 60, "vOffset": -30,},
        "mobile": {"show": true, "scale": 0.1,},
        "log": false
    });</script>
```
关于这个看板娘的配置，以及更多的角色选择，我专门写了一篇博文：  
[给自己的jekyll安装一个萌萌哒二次元看板娘](https://www.oukohou.wang/2018/11/29/live2D_installation/)  
点击进去尽情的撒个野吧～～  


### 4. Valine评论系统
> [Valine](https://valine.js.org/) 诞生于2017年8月7日，是一款基于Leancloud的快速、简洁且高效的无后端评论系统。  
理论上支持但不限于静态博客，目前已有Hexo、Jekyll、Typecho、Hugo 等博客程序在使用Valine。  

具体如何配置访问 [Valine的官网](https://valine.js.org/) 即可，官方介绍还是很详细的。  
我的部署代码在
```text
./_layouts/post.html:  
```
的  
```text
    <!--valine comment function-->
    <script src="https://cdnjs.loli.net/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
    <script src="//cdn1.lncld.net/static/js/3.0.4/av-min.js"></script>
    <script src="//unpkg.com/valine/dist/Valine.min.js"></script>

    <p><br/>既已览卷至此，何不品评一二：</p>
    <div id="valine_comment" class="fb_comments_container"></div>
    <script>
        var notify = '{{site.valine.notify}}' === true;
        var verify = '{{site.valine.verify}}.>' === true;
        var visitor = '{{site.valine.visitor}}.>' === true;

        new Valine({
            av: AV,
            el: '#valine_comment',
            notify: notify,
            verify: verify,
            // smiles_url: '/smiles',
            visitor: true,
            app_id: '{{site.valine.app_id}}',
            app_key: '{{site.valine.app_key}}',
            placeholder: '{{site.valine.placeholder}}',
            avatar: '{{site.valine.avatar}}',
        });
    </script>
```


对应更改
```text
./_config.yml
```
中的valine配置即可。    

### 5. sidebar(侧边栏)
sidebar（侧边栏）的部署代码在
```txt
./_layouts/base.html  
```
的*id="sidebar"*标识，所引用的代码文件在
```text
./_includes/widgets/
```
目录下，对应更改这些文件即可。 

### 6. 搜索引擎验证文件
所谓引擎验证文件，主要是repo根目录的一些html、txt文件，是用来提交站点收录时验证用的。  
套用我的 [一篇博客](https://www.oukohou.wang/2018/11/01/sereral_search_engines_urls/) 的几句话：
>有了自己的域名，搭建好了自己的个人博客站点，就万事俱备了么？  
剩下的只是勤恳更新自己的内容，就自然会有人看到并来给你32个赞了么？  
The answer is no！  
小伙子，你还需要把自己的网站地址提交到各个搜索引擎，求他们收录你的站点。   
这样别人在百度搜索的时候，你的站点内容才有可能被呈现在搜索结果中哦~~  
而且很有可能即使这么做了，人家还不情不愿不想收录哦～～  
更而且，即使收录了，也可能排在不知道几十页之后哦～～  

具体如何提交站点收录，可以参看我的 [这一篇博客](https://www.oukohou.wang/2018/11/01/sereral_search_engines_urls/)。

### 7. fork and star
赠人玫瑰，手有余香。  
看在我这么辛苦写readme的份上，不如支持我一下？   
<div style="float:left;border:solid 1px 000;margin:2px;">
<a href="https://github.com/oukohou/oukohou.github.io/stargazers" target="_blank">
<img src="https://img.shields.io/github/stars/oukohou/oukohou.github.io.svg?logo=github">
</a>
</div>


<div style="float:left;border:solid 1px 000;margin:2px;">
<a href="https://github.com/oukohou/oukohou.github.io/fork" target="_blank">
<img src="https://img.shields.io/github/forks/oukohou/oukohou.github.io.svg?logo=github">
</a>
</div><br>  
  
欢迎fork、star我的repo～～  
当然，如果你想要 [赏个铜板](https://www.oukohou.wang/donate/ "donate") 的话，那自然是更加欢迎的哈哈～～  
![yasashii](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/anime/%E6%B8%A9%E6%9F%94%E7%9A%84%E7%94%B7%E5%AD%A9%E5%AD%90.jpg "当然，女孩子会更温柔的啦～～")  


如有疑问，欢迎留言。


<p  align="right">regards.</p>
<h4 align="right">
    <a href="https:www.oukohou.wang">
        oukohou.
    </a>
</h4>

