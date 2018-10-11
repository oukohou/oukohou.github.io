[我的独立博客](http://www.oukohou.wang/)
=================================

一个简洁的、多设备支持的 Jekyll 博客模板，用于搭建[我的独立博客](http://www.oukohou.wang/)。主题基于 [maupassant-jekyll](https://github.com/alafighting/maupassant-jekyll.git) 重新修改和优化，同时很大程度上参考了[kuanghy](https://github.com/kuanghy)的博客主题[luring](https://github.com/kuanghy/luring)，感谢。  
模板预览：

![template preview](https://camo.githubusercontent.com/74fd2ccea00a682742515ce1d3725283c3385721/687474703a2f2f6f6f6f2e306f302e6f6f6f2f323031352f31302f32342f353632623562653132313737652e6a7067)

## 主题安装

安装 Jekyll 本地环境，以便于调试：

```bash
gem install jekyll
jekyll new my-awesome-site
cd my-awesome-site
bundle install
bundle exec jekyll serve
# => 打开浏览器 http://localhost:4000
```

下载原作者主题安装调试：

```bash
git clone https://github.com/alafighting/maupassant-jekyll.git maupassant
cd maupassant
# 当然你也可以选择clone我的这个更改后的博客主题，只需改一下地址即可：
# git clone https://github.com/oukohou/oukohou.github.io oukohou
# cd oukohou
gem install jekyll-paginate
jekyll build
jekyll server
```

## Maupassant 在不同框架下的支持

Maupassant 最初是由 [Cho](https://github.com/pagecho/) 大神为 [Typecho](http://typecho.org/) 平台设计开发的一套响应式模板，体积只有20KB，在各种尺寸的设备上表现出色。由于其简洁大气的风格受到许多用户喜爱，目前也已经被移植到了多个平台上，例如：

+ Typecho：https://github.com/pagecho/maupassant/
+ Octopress：https://github.com/pagecho/mewpassant/
+ Farbox：https://github.com/pagecho/Maupassant-farbox/
+ Wordpress：https://github.com/iMuFeng/maupassant/
+ Hexo: https://github.com/icylogic/maupassant-hexo/
+ Ghost: https://github.com/LjxPrime/maupassant/
+ Jekyll: https://github.com/alafighting/maupassant-jekyll/

------
oukohou(<oukohou@outlook.com>)<br>
2018-09-17
