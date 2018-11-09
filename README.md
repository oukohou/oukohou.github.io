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


## A note:
Note that several html,txt files in root dir:  
-  60e2c4178f1d12527f7e5b00a80d0f2f.txt  
- baidu_verify_mDTcGWbBLX.html  
- google23b03f783980f31a.html  
- sogousiteverification.txt  
These files are for verifications of 360, google, baidu and sougou.
Such that these search engine will index my blog site.  
These files vary from one to one. Remember to change accordingly for your own site.  
**See my [this blog](https://www.oukohou.wang/2018/11/01/sereral_search_engines_urls/) for details.**

**Any star, fork or [donation](https://www.oukohou.wang/donate/) is highly appreciated!!!**
------
oukohou(<oukohou@outlook.com>)<br>
2018-09-17
