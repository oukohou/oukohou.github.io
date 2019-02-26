---
layout: post
title:  "Ubuntu上配置atom+latex编辑环境"
date:   2019-02-26 14:30:28 +0800--
categories: [部署]
tags: [Ubuntu, aton, latex,]  
---

写论文受够了word的排版？  
想要解放自己专注于内容生产？  
那么LaTeX就是你的首选！  

按说这篇其实没啥必要写的，然而在安装过程中还是经历了一些波折，颇费了些工夫，故此记录一下，以飨后来者。  

### 1. Latex  
安装TexLive：  
- 在这里： [Installing TeX Live over the Internet](https://tug.org/texlive/acquire-netinstall.html) 下载安装包，
解压；  
- 运行:  
 `sudo ./install-tl.sh`  
 会有一个提示，选择 `i` 即可在线安装。  
值得一提的是，安装过程较为漫长，我的安装了一天。  
- 安装结束后，测试一下是否成功：  
`tex -version`  
  出现类似下面的结果，即为成功：
  
```bash
    TeX 3.14159265 (TeX Live 2015/Debian)
    kpathsea version 6.2.1
    Copyright 2015 D.E. Knuth.
    There is NO warranty.  Redistribution of this software is
    covered by the terms of both the TeX copyright and
    the Lesser GNU General Public License.
    For more information about these matters, see the file
    named COPYING and the TeX source.
    Primary author of TeX: D.E. Knuth. 
  ```
    
### 2. atom

安装atom：
- 在这里：[atom.io](https://atom.io/) 下载安装包；  
- 运行：  
`sudo dpkg -i atom-amd64.deb`  
安装较快；
- 测试是否安装成功：  
`atom --version`  
出现类似下面的结果，即为成功：  

```python  
    Atom    : 1.34.0
    Electron: 2.0.16
    Chrome  : 61.0.3163.100
    Node    : 8.9.3
```


### 3. Latex+atom

打开atom，安装编译LaTeX所需的几个packages：
- 在atom界面按快捷键 `ctrl+shift+p`；
- 在弹出的搜索框内输入 `setting`，点击第一个选项，进入到这个界面：  
    ![settings](https://s1.ax2x.com/2019/02/26/5jqeoN.png)  
- 选则 `Packages` 栏，搜索安装以下三个package：  
    - Language Latex  
    - Latex  
    - pdf-view  
    
- 点击 `Latex` 这个package的 `Settings` ，其第一行需要配置 `Tex Path`，为你的latexmk的路径。  
这里需要手动在这里：[latexmk–Fully automated LATEX document generation](https://ctan.org/pkg/latexmk/) 下载latexmk，
解压后，按照文件 `INSTALL` 里的指示，将 `latexmk.pl` 拷贝到路径 `/usr/local/bin` 并重命名为 `latexmk`：  
`sudo cp latexmk.pl /usr/local/bin/latexmk`.    
然后测试一下latexmk是否安装成功：  
`latexmk -version`  
出现类似下面的结果，即为成功：

```text
    Latexmk, John Collins, 25 October 2018. Version 4.61
```

 



<br>
微信公众号：璇珠杂俎(也可搜索[oukohou](https://mp.weixin.qq.com/s/dCxGcuv5ngyR6U-uBYVI9Q))，提供本站优质非技术博文～～
[![wechat_official_account](https://www.oukohou.wang/assets/imgs/wechat_official_account.png)](https://mp.weixin.qq.com/s/dCxGcuv5ngyR6U-uBYVI9Q "点击图像直达微信公众号～～")  




<br>
<p  align="right">regards.</p>
<h4 align="right">
    <a href="https://www.oukohou.wang/">
        oukohou.
    </a>
</h4>

