---
layout: post
title:  "博客搭建历程"
date:   2018-11-20 19:43:30 +0800--
categories: [部署]
tags: [installation, blog, setting up]  
---
前几天给博客加了[Valine](https://valine.js.org/)评论系统，至此博客也算是像模像样地正式搭建好可以见人了。  
想了想，麻雀虽小，但也要有个人样（啥玩意儿？），还是写一下这篇博客的搭建历程吧。  

搭建博客只需要解决两个问题：
 - 域名  
 - 载体   
 
且看下文如何分解。

## 1. 域名申请    
 
首先说域名。  
域名要买，有很多人卖。    
我就只有一个原则：便宜。      
找了半天，最后是在[腾讯云](https://cloud.tencent.com/)上买了这个域名[oukohou.wang](https://www.oukohou.wang/),后缀于我也算是应景。  
注册时犹豫了半天是要 kohou.wang 还是 oukohou.wang。  
最终还是因为已经在众多平台上注册了账号ID为oukohou，为了保证一致性，
选择了[oukohou.wang](https://www.oukohou.wang/)。  
还算便宜，一年只要29元。  
送了几张有效期一个月的券，当时没有用掉。现在想要续费几年，就有点可惜当初没有用了。  
那就这样吧，先用着看看。等明年快到期了再续费吧。  

## 2. 博客主题  
然后说载体。  
载体也**可以**买，也有很多人卖。  
注意，“可以”买，只有一个原则的我，自然是不想花这个钱了。  
恰好全球最大的同性交友网站[github](https://github.com/oukohou)免费提供了一个可以用作载体的工具：[github pages](https://pages.github.com/).  

![start_from_0](https://s1.ax2x.com/2018/11/20/5z798A.jpg)  

于是，这个博客是采用jekyll在github pages上搭建的。  
至于搭建步骤，这个就不需要我来班门弄斧了，网上随便一搜“jekyll github pages”，你就知道答案了。  
当然，如果你想要我的这个特定的博客主题的话，请参考[我的github repo](https://github.com/oukohou/oukohou.github.io)的步骤介绍。    


## 3. 站点收录
这个也是不容忽视的一点。  
套用我的[一篇博客](https://www.oukohou.wang/2018/11/01/sereral_search_engines_urls/)的几句话：
>有了自己的域名，搭建好了自己的个人博客站点，就万事俱备了么？  
剩下的只是勤恳更新自己的内容，就自然会有人看到并来给你32个赞了么？  
The answer is no！  
小伙子，你还需要把自己的网站地址提交到各个搜索引擎，求他们收录你的站点。   
这样别人在百度搜索的时候，你的站点内容才有可能被呈现在搜索结果中哦~~  
而且很有可能即使这么做了，人家还不情不愿不想收录哦～～  
更而且，即使收录了，也可能排在不知道几十页之后哦～～  

具体如何提交站点收录，可以参看我的[这一篇博客](https://www.oukohou.wang/2018/11/01/sereral_search_engines_urls/)。

## 4. 评论功能
评论功能难了我挺久一段时间。  
首先，作为一个博客，没有评论功能的话，感觉就只有自娱自乐，完全背离了分享交流的初衷。  
虽然现在我这个博客几乎没人来看～～  
但是，借用老舍那句话：  

> 万一将来我不得已而作了皇上呢，这篇东西也许成为史料，等着瞧吧。  

万一将来我火了呢？  
所以，等着瞧吧。  

那么问题来了，咋实现呢？
### 4.1. 首先是想要用[gitalk](https://github.com/gitalk/gitalk)  
但是gitalk首先需要申请github的App Oauth授权，而这个授权的权限又很大，具体参考[这个issue#95](https://github.com/gitalk/gitalk/issues/95)。  
为此也有一个权宜之计是可以用一个github小号来申请这个授权，我也确实不辞辛劳地这么干了，然而总是有问题，具体参考[这个issue#186](https://github.com/gitalk/gitalk/issues/186)。  
等了N久最终还是没解决，不得已，我只有寻找别的替代品。  

### 4.2. 于是尝试了[disqus](https://disqus.com/)
Disqus应该是比较出名的了，类似的还有[livere](https://www.livere.com/)。  
但是这两个好像都是国外的插件，考虑到科学上网还是有一定的
壁垒，并不是每个人都能轻而易举地科学上网，中间做了一段替代品，但同时也在寻找新的目标。

### 4.3. 最终遇到了[Valine](https://valine.js.org/)  
[Valine](https://valine.js.org/)应该是我目前情况下的最优选择了。  
不需要科学上网，无后端，极简风格，可以定制，而且免费、开源。  
还要啥自行车？  
[Valine](https://valine.js.org/)的配置，我用的是原作者的[这个配置](https://github.com/litten/hexo-theme-yilia/pull/646/files#diff-2)。  
想要折腾的同学可以参考另外一个人在Valine基础上魔改的版本：[Valine: 独立博客评论系统](https://panjunwen.com/diy-a-comment-system/)。

## 5. 完结撒花
总之，最后我总算实现了博客的评论功能，算是像模像样地搭建好了博客，可以见人了。  
说点啥来当做总结好呢？  
就把我的博客的slogan的全文贴出来吧！  

**满江红·思家**  
【作者】郑燮 【朝代】清  
我梦扬州，便想到扬州梦我。第一是隋堤绿柳，不堪烟锁。潮打三更瓜步月，雨荒十里红桥火。更红鲜冷淡不成圆，樱桃颗。  
何日向，江村躲；何日上，江楼卧。有诗人某某，酒人个个。花径不无新点缀，沙鸥颇有闲功课。将白头供作折腰人，将毋左。  

虽然我的老家不在扬州。  
![just smile~~](https://s1.ax2x.com/2018/11/20/5z70Yi.jpg)  



regards.
<h4 align = "right">oukohou.</h4>

