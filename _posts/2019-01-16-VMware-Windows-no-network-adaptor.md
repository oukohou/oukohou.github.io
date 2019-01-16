---
layout: post
title:  "VMware安装的Windows显示没有网络适配器的解决方法"
date:   2019-01-16 20:10:18 +0800--
categories: [备忘]
tags: [VMware, 网络, Windows]  
---

## 0. 概要
这篇主要讲讲当你在Windows虚拟机上误删除了网络适配器(network adaptor)之后，
宿主机虽然能上网，但Windows虚拟机死活上不了网的问题：
```text
Install a driver for your network adaptor

windows could not detect a properly installed network adaptor.
if you have a network adaptor, you will need to re-install the driver.
```

## 1. 环境
- 宿主机为Ubuntu 16.04 LTS；  
- VMware 版本为：  
    - Product : VMware® Workstation 15 Pro  
    - Version : 15.0.0 build-10134415
- 所安装的虚拟机版本为：  
    - Edition : Windows 10 Pro N  
    - Version : 1803  

## 2. 复现
在虚拟机上弹出U盘，手欠的错点了那个像极了U盘标志的符号的最后一栏：  
![logo](https://s1.ax2x.com/2019/01/16/5dqnSq.png "就是这个最后一栏！！！" )
  
 `Eject Intel(R) 82574L Gigabit Network Connection`，其实就是虚拟机的网络适配器(network adaptor)，
然后虚拟机就上不了网了。。。  
这时候点击虚拟机Windows的右下角网络标志，界面是这样的：  
![network_status](https://s1.ax2x.com/2019/01/16/5dqKLn.png)  
哦吼哦吼，`you aren't connected to any networks!`  
意不意外？惊不惊喜？  
这时候无助的我想要寄希望于那个 `Troubleshoot` 按键，于是点击之后，是这样的：  
![install_a_driver](https://s1.ax2x.com/2019/01/16/5dqISa.png)   
更加意外，更加惊喜了这下……  
怎么办呢？  

不用怕！且看下文如何分解～～  

## 3. 冲阵
在VMware的左侧虚拟机列表里选中你的虚拟机，比如我的就是 `Windows 10x64`，然后
右键单击，选择最下一栏的 `设置`，点开就看到了你的虚拟机设置界面：  
![settings](https://s1.ax2x.com/2019/01/16/5dq86h.png)   
可以看到，这时候你的 `Hardware` 栏里是没有网络适配器(Network Adaptor)的～～  
这可如何是好？  
不怕，既然没有，我们把它加上就是了：
- 选择下面的 `Add` 选项，你就会看到希望：  
![network_adaptor](https://s1.ax2x.com/2019/01/16/5dqf5H.png)  

咦～第四栏就是我们日思夜想梦寐以求的网络适配器(network adaptor)！  
意不意外！惊不惊喜！  

好了，平复一下心情，我们选中，保存。  
然后再启动我们的Windows虚拟机，看一看结果怎样？  

## 4. 收兵
开不开心？  
是不是激动地想要[赏我两个铜板](https://www.oukohou.wang/donate/ "那就赏吧，点击直达打赏页面～～ ")？    
[![yasashii](https://s1.ax2x.com/2018/12/19/5Qxfd6.jpg "当然，女孩子会更温柔的啦～～")](https://www.oukohou.wang/donate/)  






<p  align="right">regards.</p>
<h4 align="right">
    <a href="https:www.oukohou.wang">
        oukohou.
    </a>
</h4>


<br>
微信公众号：璇珠杂俎(也可搜索oukohou)，提供本站优质非技术博文～～
![wechat_official_account](https://www.oukohou.wang/assets/imgs/wechat_official_account.png)  
