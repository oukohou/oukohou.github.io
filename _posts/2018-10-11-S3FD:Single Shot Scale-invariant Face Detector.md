---
layout: post
title:  "论文阅读_人脸检测-S3FD-Single Shot Scale-invariant Face Detector"
date:   2018-10-11 16:14:28 +0800--
categories: [论文]
tags:   [machine learning, face detection, S3FD, papers]
---

> 写在前面：记录一下论文阅读的收获，不然怕久远之后，就不记得了～

----------
### 1. Sum up
S3FD是2017年发表在[arXiv上的一篇文章](https://arxiv.org/abs/1708.05237)，文如其名，讲的是一个端到端的具有尺度不变性的人脸检测框架，论文主要创新点在于：  

 - 提出了一个适用于不同尺度大小的人脸的检测框架；
 - 通过锚框匹配策略改进了小尺度人脸的召回率；
 - 通过“最大者胜(max-out)”的背景标签降低了假阳性率(FPR)；
 
网络架构如图所示：  
![S3FD‘s architecture](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/S3FD/architecture_S3FD.png)  

---

### 2. What's up？
论文首先针对三个创新点抛出了基于锚框检测算法的几个弊病：
![drawbacks of anchor-based methods](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/S3FD/drawbacks%20of%20anchor-based%20methods.png)

 - 如图(a)所示，对于检测层网络来说，步长对应的感受野较大，小尺度人脸能够表达出的特征少之又少；
 - 如图(b)所示，锚框与感受野的大小不能很好的匹配，同时锚框、感受野都不能很好的匹配到小尺度人脸区域；
 - 如图(c)所示，由于锚框大小实际上都是固定的，所以落在这些固定大小之外的人脸就不能很好的检测到；
 - 如图(d)所示，如果想要检测到小尺度人脸，相对于大尺度人脸，那么就注定会有更多的小尺度、不包含人脸的背景锚框。  
 
 以上几点是论文所提出的问题，也就是论文创新点所重点关注和改善的几个地方，下面一一道来。
 
---
### 3. S3FD
#### 3.1 怎么能让网络适用于不同尺度的人脸？
答案很简单：既然不同尺度的人脸在同一层上的特征区域不同，那么又何必强求呢？道不同，不相为谋，在不同层上分别进行检测就是了。  
当然，理想很丰满。为了实现这一理想，就要做些骨感的工作：
 
首先要建立一个很骨感的网络，也就是开头那张图。以防大家一下就忘了，再放一次：  
	![S3FD](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/S3FD/architecture_S3FD.png)

这张图有什么玄机呢？
使劲瞅，用力看：

 - Base Convolutional Layers 这个方框内用的是[VGG16](https://arxiv.org/abs/1409.1556)的框架，不过只取到了Pool5层；
 - Extra Convolutioal Layers 原本应该是VGG16的全连接层fc6、fc7被换成了卷积层，当然我们知道，通过设计卷积层卷积核大小与前一层特征图相等，也能实现全连接的功能；同时后面也额外加上了4层卷积层，看来这是要搞大事情呀；
 - 左下角的Detection Layers就是一个抽象的概念了，其实就是Base、Extra方框内的一些卷积层被指派为检测层了，不知道其他没被指派的卷积层会不会感到失落呢；
 -  Normalization Layers：这个图上没标，其实就是对Base方框里被选中的几个检测层进行了L2 normalization；
 - Predicted Convolutional Layers 也是人如其名，就是预测层了，其中每个卷积层分别承担着不同尺度的人脸的检测任务，分别预测锚框的偏移量和所属类别的置信率；论文所声称的适用于不同尺度人脸的功能就是这样实现的了；
 - Max-out BG label：为了雨露均沾，还是提一下这个框框，这个就是专门为了Con3_3而设计的了，目的是筛选出大部分的背景锚框；
 - Multi-task Loss Layers：就是损失层咯，分类用softmax loss，回归用smooth L1 loss。 

以上，终于把这个十分骨感的网络讲完了，下面就是一点一点地实现我们丰满的理想了。

####  **How about anchors' scales?**
那么问题来了，前面说了不同层上检测不同尺度的人脸，这个“不同尺度”，也就是不同层的锚框大小该怎么定义呢？
首先的直觉是：因为人脸区域的标定框一般都是正方形，所以锚框也定义成正方形，长宽比1:1。
OK，那么关键的，这个长、宽到底应该是多少呢？取决于两个因素：

 - 有效感受野
	 啥叫有效感受野？看图说话：  
	 ![effective receptive field](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/S3FD/effective%20receptive%20field.png)  
  只看图(a)，对于整个黑色方框来说，其整体是一个理论上的能够对最终输出产生影响的感受野，也就是大家通常意义上所理解的感受野，真~感受野，那么有效感受野就是图中心的白色点点，这些是实际上能够对最终输出产生影响的区域，也就是所谓的有效感受野，真～真～感受野。因此，在图(b)中，黑色虚线框是正常的感受野，蓝色虚线圆就是我们的有效感受野，而红色实线框就应该是我们的锚框的大小；
 - 等比例间距原则(Equal-proportion interval principle)
这又是啥？不要着急，君且安坐，听我一言：   
看图(c)，对于锚框是n×n的，固定锚框之间的间隔是n/4，而n/4也正式对应的这一layer的stride size。于是这就成了我们的等比例间距原则:
不同尺度的锚框在图像上都有相等的密度，从而使得不同尺度的脸能够大体上匹配到相等数量的锚框。为便于理解及不让各位因为我的差劲转述而困惑，
这里贴上原论文的描述：

```text
The stride size of a detection layer determines the interval of its anchor on the input image. For example, the stride size of conv3_3 is 4 pixels and its anchor is 16×16, indicating that there is a 16 × 16 anchor for every 4 pixels on the input image....the scales of our anchors are 4 times its interval. Assuming n is the anchor scale, so n/4 is the interval of this scale anchor. n/4 also corresponds to the strid size of the layer associated with this anchor.
```  
为了能够实现我们的丰满理想，还真是操碎了心啊。

#### 3.2 尺度补偿锚框匹配策略(Scale compensation anchor matching strategy)
所谓锚框匹配，也就是在训练过程中如何确定哪些锚框是匹配到人脸了的，而哪些没有。
一般来说，锚框匹配首先匹配那些与标记好的人脸有最好IOU交并比的锚框，然后匹配那些与任意人脸的IOU交并比大于某个临界值的锚框。有点绕，但确实如此。就是先按照预先标记好的人脸区域匹配最好的锚框，然后从众多生成的锚框区域中来匹配次好的锚框。
但是陈独秀同志又有话说了，看图：  
![scale compensation](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/S3FD/scale%20compensation.png)  
我们知道，众多图像中的人脸区域大小应该是连续分布的，但我们的锚框大小却是一些固定的值。图(a)中蓝虚线，当锚框是固定值(16, 32, 64, 128, 256, 512)的时候，可以看到，与这些值都不接近的人脸区域不能够很好的被匹配到，尤其是小人脸部分，效果微乎其微。
据此，文章提出了尺度补偿锚框匹配策略：

 - 降低锚框匹配的临界值，一般是0.5， 这里改为0.35，以提高每个人脸框所匹配到的锚框数量；
 - 针对依然没有被匹配到的人脸区域， 将阈值改为0.1，然后选择匹配比最高的N个锚框进行匹配；
经过这一该进，效果显著，就是图(a)中的红实线了。
#### 3.3 “最大者胜”的背景标签(Max-out background label)  
首先，啥是背景标签？很简单，对于人脸检测，锚框区域如果包含人脸，那么就是正例，如果不包含人脸，那么就是负例，也即背景标签。  
对于基于锚框的检测方法来说，有一个问题：  
![anchors numbers](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/S3FD/anchors%20numbers.png)  
比如本文中所述的方法，对于一张640*640的图像，其总共产生了34,125个锚框！仅conv3_3就贡献了超过75%的尺度大小为16×16的锚框！  
这可如何是好呀？  
于是就到了3.2中图(b)的做法了：对于每个匹配到的锚框，同时预测其一系列背景锚框，然后选择其中置信率最高(max)的一个作为负例，也即Max-out。其实这就是一种局部优化方法，以此来减少假正率。  

### 4. The end, and flowers！
以上，就是S3FD如何提出了一个丰满的理想，并一步一步骨感地实现它的过程。  
论文在提出之时在各大人脸检测榜上刷出了较好的成绩，wider face、FDDB、AFW等，当然，截止到现在(2018-09-13 10:09:06)是又被其他方法给顶了下去。果然是打江山容易，守江山难啊～～
最后放上一张大家都爱放的检测效果图，也是S3FD论文中的检测效果图：  
![finding 853 faces](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/S3FD/finding%20853%20faces.png)    
这张图据说共有1000张脸，S3FD方法检测出了853张。  
不要惊奇，不要讶异，百度的Pyramidbox检测出了880张～～当然，这是后话，不在本文讨论。  

### 5. The real end，and FLOWERS！
完结撒花。  
你的赞是我最大的动力！  


----------
### 6. 个人私货时间：  
- github 	:[oukohou](https://github.com/oukohou)  
- my site:[oukohou.wang](http://www.oukohou.wang/)  
- e - mail:[oukohou@outlook.com](oukohou@outlook.com)  
- wechat official account: oukohou  
[![wechat_official_account](https://www.oukohou.wang/assets/imgs/wechat_official_account.png)](https://mp.weixin.qq.com/s/dCxGcuv5ngyR6U-uBYVI9Q "点击图像直达微信公众号～～")  
    Scan and we'll see.


regards.  
<h4 align = "right">oukohou.</h4>

