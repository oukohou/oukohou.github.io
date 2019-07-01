---
layout: post
title:  "ubuntu下挂载机械硬盘方法命令"
date:   2019-01-29 16:31:26 +0800--
categories: [部署]
tags: [ubuntu, 挂载硬盘, 命令]  
---



用的台式机虽然本身已经是256G固态+2T机械硬盘了，然而每天与海量数据打交道的我，还是迅速用的只剩下了100G不到：  
![not_many_space](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/ubuntu_mount_dick/%E9%83%BD%E5%81%9A%E4%BA%86%E4%BB%80%E4%B9%88%E5%95%8A.jpg)    

然后申请了个新的2T机械硬盘，麻溜装到机箱里，然后挂载(mount)的时候犯了难：  
`两个同样属性的机械硬盘，到底哪个是我新加的？这要是万一格式化格错了，岂不是万劫不复？`  
![same_disk](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/ubuntu_mount_dick/same_disk.png)  
  

不敢妄动。  
所幸搜索到了这篇[博客](https://blog.csdn.net/wshixinshouaaa/article/details/81275608), 才发现原来有个图形化工具Disks，
而我的Ubuntu 16.04 LTS也果然争气的自带了：
![disks](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/ubuntu_mount_dick/disks.png)  

可以看到，点选一个硬盘之后，具体内容里最后一行的 `Contents` 最后会显示是否已经挂载～  


那就方便多了对不对，更而且的是，点选未挂载的硬盘，然后选中具体内容里 `Volumes` 图案左下方的齿轮图标，
即会弹出格式化选项！  
选中之后即可进行格式化选项，这里在 `Name` 一栏选填一个名字，后面会有奇用～  
![format_disk](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/ubuntu_mount_dick/format_disk.png)   

让子弹飞一会儿，格式化完成。  
这时候我们再查看一下硬盘的UUID：  
```bash
sudo blkid
```
即可看到刚刚格式化的时候填的 `Name` ：
![disk——label](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/ubuntu_mount_dick/disk_label.png)     

惊不惊喜！意不意外！  
这下我们知道了要挂载的硬盘的UUID了，比如我的就是图中的 `d8df29bb-52ab-47c6-beba-a6f06fb576fe` ，然后编辑配置文件：  
```bash
sudo vim /etc/fstab
```

将下面这一行添加到最后一行：  
```bash
UUID=d8df29bb-52ab-47c6-beba-a6f06fb576fe home/CVAR-B    ext4    defaults        0       0
```  

然后重启电脑，查看，即可在目录 `/home`下看到刚刚挂载的硬盘对应的文件夹：  
![generated_dir](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/ubuntu_mount_dick/generatd_dir.png)  

当然目录放在 `/home`下入口可能有点深，需要从 `Computer` 下来找，不太方便。  
可以选择创建一个快捷链接，把它放到你希望的位置。
比如我是放在左侧导航栏第二行那个 `Home`下的。    
![short_cut](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/ubuntu_mount_dick/shortcut.png)  


以上，致礼！



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

