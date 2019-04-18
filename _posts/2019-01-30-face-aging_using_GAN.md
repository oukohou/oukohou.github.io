---
layout: post
title:  "论文阅读-人脸老化-Generative_Adversarial_Style_Transfer_Networks_for_Face_Aging"
date:   2019-01-30 11:09:07 +0800--
categories: [论文]
tags: [face aging, GAN, style transfer]  
---

一个人10后会长什么样？  
10年前他又是什么样？  
这就是人脸老化(face aging)问题：给定一张人脸图像，给出其x年后的人脸图像，x可以为负数，此时即表示年轻化。    

关于这个问题，这篇论文提供了一个新的视角：  
```text
对于一张包含人脸的图像，将其所对应的年龄看作是其潜在的风格(underlying style),把人脸老化看成是一个风格迁移问题。
```  
是不是有点耳目一新的感觉？感觉风格迁移的做法啥任务都用来做了。    
先来张图一睹为快：    
![results_1](https://s1.ax2x.com/2019/01/30/5j8GCp.png)  

掌握上面那一句，其实已经掌握了这篇论文的大半了，且看下文一一分解。  

## 1. methods
网络架构主要用的[CycleGAN](https://arxiv.org/abs/1703.10593 '这里占个坑，下次把CycleGAN的博文补上～')，在其基础上进行了loss函数的魔改。    
而且提出了两个网络Group-GAN、FA-GAN，从最终的实验效果来看，其中Group-GAN对年龄跨度大的转换效果较好，FA-GAN则相反，偏向于年龄跨度小的转换。  

### 1.1. Group-GAN(Group based CycleGAN method)
论文中用CycleGAN来训练两组年龄组之间的年龄迁移。  
首先，按下面四个年龄组来分类数据集：  
```text
A) ages 00-20    B) ages 20-40  
C) ages 40-60    D) ages 60+   
```

对于每两个年龄组，作者都训练了一个CycleGAN进行迁移，一共要训练$$C_4^2=6$$个模型。
所用loss为：  
![loss_Group-GAN](https://s1.ax2x.com/2019/01/30/5j84BE.png)  

式中， λ 值为10.每个模型的训练时间24h左右，值得一提的是，虽然训练过程较稳定，但毕竟是GAN，
训练过程很容易陷入mode collapse，作者还是有几次要重新训练的。  
以及，当两个年龄组相差较大，即数据特征理论上来说分开的更好的时候，比如训练A组和D组年龄组的数据，
模型又有把背景颜色翻转的趋势……为此作者又额外加了个weak L1 loss：  
![weak_L1_loss](https://s1.ax2x.com/2019/01/30/5j8JsQ.png)  

这个模型的人脸老化效果图如下：  
![Group-GAN face aging results](https://s1.ax2x.com/2019/01/31/5j8CvN.png)  

可以看到，第一列的输入和最后一列的输出都有较为明显的年龄特征，第二列就有点不辩牛马了～～  
其实这里还有一个问题，论文中没提到，可能是作者有意略过的：  
``` markdown
从年轻的人脸老化到年老的人脸，如果20岁左右人脸大小定型了之后的话，那么效果还好。  
但对于第三行，是从一个几岁的儿童的人脸进行老化，但是儿童在长大的过程中，
不光是面部纹理的变化，其脸也会变大……如果只是增加面部纹理的话，
那么看起来就像是第三行最后一列一样，怎么看怎么像侏儒了……  
（TODO）
```

而同时，得益于CycleGAN的 `Cycle`，这个模型还能实现人脸年轻化(rejuvenation)，效果如下：  
![Group-GAN rejuvenation results](https://s1.ax2x.com/2019/01/31/5j8Elu.png)  

仔细观察的话，会感觉这两张效果图的前两列怎么好像没啥区别一样？  
带着这个疑问，作者又设计了更细粒度的年龄组进行训练，来测试Group-GAN在小年龄段之间的效果到底如何。
小年龄段的年龄分组信息如下：  
```text
A) ages 30-40    B) ages 40-50  
C) ages 50-60    D) ages 60-70     
```

同样操作训练之后，效果图如下图所示：  
![Group-GAN_results_with_smaller_age_groups](https://s1.ax2x.com/2019/01/31/5j8eF9.png)  

可以看到，效果是不尽如人意的。  
作者为此argue：  
`模型本身是要学习两个年龄组的图像的不同之处，而年龄相近的年龄组，其不同之处本就较难检测。`

### 1.2. FA-GAN(Face Aging GAN)
当然了，如果只是Group-GAN的话，大家可能会觉得有点被耍猴：  
`不是年龄老化吗？咋不能指定年龄？只能指定年龄组？`  
这就是作者提出的FA-GAN了：  
`给定一张人脸图像$x_0$和一个数字k，输出经过k年变化的同一张人脸`  
其中数字k可以为负，即年轻化(rejuvenation)。  
而为了让模型能够考虑年龄k，作者先假设能够有个可导的年龄估算器$age(x)$，
然后加上了平均绝对误差作为年龄的loss：   
![Loss_age](https://s1.ax2x.com/2019/01/31/5j8UsA.png)  

那么问题来了： `怎么保证人脸是同一个人呢？`   
没错，又是CycleGAN。一个老化k年后的人脸，再年轻化k年，所得到的应该和输入的人脸是相同的，也就引入了loss：  
![Loss_cycleGAN](https://s1.ax2x.com/2019/01/31/5j8KAO.png)  

最后，整体的loss为：  
![total_loss_FA-GAN](https://s1.ax2x.com/2019/01/31/5j81qq.png)  

值得一提的是，作者考虑到老化一张年轻人的人脸和老化一张老人的人脸，显然这两者的操作是不同的。  
比如同样過了10年，20岁的人到了30岁，和50岁的人到了60岁，显然20岁的人要变化更大。  
因此，在输入图像的同时，还同时输入了该图像的估算后的年龄。流程图如下：  
![diagram_of_FA-GAN](https://s1.ax2x.com/2019/01/31/5j8I2R.png)  

关于patchGAN，我在之前的[pix2pix](https://www.oukohou.wang/2019/01/07/Image-to-Image-Translation-with-Conditional-Adversarial-Networks/#222-markovian-discriminatorpatchgan)
博文里提到过，就是discriminator关注的不是整张图像，而是$N×N$的patches，具体可以参考我的这一篇博文：[pix2pix](https://www.oukohou.wang/2019/01/07/Image-to-Image-Translation-with-Conditional-Adversarial-Networks/#222-markovian-discriminatorpatchgan)。  

同时，作者预实验过程中，发现年龄老化、年轻化分开训练的话效果更好，即$$G_{+}(x_0,k)={\hat{x}}_k$$做老化,
$G_{-}(x_0,k)={\hat{x}}_{-k}$做年轻化。  
注意到k是从集合{0, 10, 20, 30, 40}中抽取的，其实这也不可苛责，毕竟不说生成年龄人脸了，
现在的年龄预测模型都有个几年的误差呢。还要啥自行车，对不对～  
最后的效果图如下：  
![FA-GAN_results](https://s1.ax2x.com/2019/01/31/5j8iuX.png)  

每一行的绿框框住的一张图像是输入图像，往左是年轻化的输出，往右是老化的输出。  
效果嘛，只能说还算凑合吧～～（~~说实话，就这么几组图像，我个人也怀疑是cherry-pick的……~~）  

### 1.3. F-GAN
根据前面的效果图，作者认为FA-GAN在年龄跨度小的时候效果较好，而Group-GAN在年龄跨度更大的时候效果较好。  
于是乎搞了个融合模型F-GAN，当年龄跨度小于20的时候，就用FA-GAN，大于20的时候就用Group-GAN。  


## 2. results
这个结果，因为目前也并没有稳定可靠的关于图像年龄的评测标准，所以论文里采用了一个朴素的方法：  
`人工评测～`  
示意图如下：  
![survey_sample](https://s1.ax2x.com/2019/01/31/5j8xAl.png)    

用调查问卷的方式，让被测者来给生成图像的可信度打分，然后用得分的平均值来衡量模型的好坏～～  
和别的模型的一个对比图示意如下：  
![comparison_results](https://s1.ax2x.com/2019/01/31/5j8RGB.png)  

然后据此认为效果更好，说：  
```text
We quantitatively evaluate our proposed method through a user study and show that it outperforms prior state-of-the-art techniques for face aging.
```

emmmm...,你说怎样就怎样啦～～  

## 3. ends

以上，致礼～  



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

