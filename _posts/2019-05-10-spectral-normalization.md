---
layout: post
title:  "论文阅读-谱归一化_SN-GANs"
date:   2019-05-10 14:51:46 +0800--
categories: [论文]
tags: [paper, GAN, spectral normalization, image synthesis]  
---

明人不说暗话，这篇论文是即将出炉的下一篇的博文：[论文阅读-自注意力GAN_SAGAN](https://www.oukohou.wang/)的前导篇。  
何出此言？因为即将到来的下一篇SA-GAN里面用到了这个谱归一化（Spectral Normalization），所以我也就仔细看了看，这里写出来分享一下。  

- paper:[Spectral Normalization for Generative Adversarial Networks](https://arxiv.org/pdf/1802.05957.pdf)  
- codes:[https://github.com/pfnet-research/sngan_projection](https://github.com/pfnet-research/sngan_projection)  

谱归一化约束，通过约束 GAN 的 Discriminator 的每一层网络的权重矩阵(weight matrix)的谱范数来约束 Discriminator 的 Lipschitz 常数，
从而增强 GAN 在训练过程中的稳定性。  

好了，嘚瑟了一段看起来很屌的名词，下面听我慢慢道来～～  

### 1. 前情提要
开玩笑，说是前情提要，其实就是描述一下背景知识～～😏  

我们假设一个简单的多层神经网络作为 Discriminator，那么有：  
  
$$f(x,\theta )=W^{L+1}a_L(W^L(a_{L-1}(W^{L-1}(...a_1(W^1x)...))))$$    

式中，$\theta = \lbrace W^1,...,W^L,W^{L+1}\rbrace$，为了简化，略去了 bias。那么 discriminator
的输出为：  

$$D(x, \theta)= A(f(x,\theta))$$  

式中，$A$是激活函数。那么标准的 GAN 的公式就是：  

$$\underset{G}{min}\ \underset{G}{max}\ V(G,D)$$  

然后作者就说，机器学习社区认为 Discriminator 的函数空间对 GAN 的性能影响十分关键，很多针对 Lipschitz 一致性的工作在开展，
从而来确保数据的边界性。  
啥是 Lipschitz？  
我的理解是一个类似凹函数、凸函数定义的东西： 

>对于在实数集的子集的函数${ f\colon D\subseteq \mathbb {R} \to \mathbb {R} }$，若存在常数$K$，  
使得$|f(a)-f(b)|\leq K|a-b|\quad \forall a,b\in D$，则称$f$符合利普希茨条件，  
对于$f$最小的常数$K$称为$f$的利普希茨常数。

Lipschitz连续比一致连续要强。*它限制了函数的局部变动幅度不能超过某常量*。  

ok，说完了背景知识，下面步入正题～～  

### 2. 谱归一化（SPECTRAL NORMALIZATION）  

开篇说了，这篇论文提出的谱归一化，是实施在 Discriminator 的每一层的权重矩阵上的，其实也就是权重矩阵的*谱范数*。  
啥又是*谱范数*？咋又来个专有名词？  
不要怕，不要有畏难情绪，其实理解了的话，都不是啥难事儿：  
我们知道向量的`1-范数`、`2-范数`等等，`1-范数`表示向量元素绝对值之和，`2-范数`表示向量元素绝对值的平方和再开方。
扩展开来，向量的`p-范数`表示的意思是向量所有元素绝对值的`p`次方和的`1/p`次幂。  
了解了向量的范数的概念，其实矩阵的范数就是在向量的基础上推广开来而已，不过因为矩阵多了一维，所以定义看起来复杂了一些。  
矩阵的`1-范数`，则是列和范数，即矩阵的所有列向量绝对值之和的最大值，矩阵的`2-范数`，是`A*A`矩阵的最大特征值的开平方，即：  

$$\left \| A \right \|_2=\sqrt{\lambda _{max}(A^TA)}$$  

式中，$\lambda _{max}(A^TA)$为$A^TA$的特征值的绝对值的最大值。  
其实，矩阵的诱导`p-范数`也可以类似向量的`p-范数`推广开来：

$${\displaystyle \left\|A\right\|_{p}=\max \limits _{x\neq 0}{\frac {\left\|Ax\right\|_{p}}
{\left \| x \right \|_{p}}}=\max \limits _{x\neq 0}{\frac {\left(\sum _{i=1}^{m}|\sum _{j=1}^{n}a_{ij}x_{j}|^{p}\right)^{1/p}}{\left(\sum _{j=1}^{n}|x_{j}|^{p}\right)^{1/p}}}}
$$

那么，啥又是矩阵的谱范数？  
就是矩阵的`2-范数`！。其值为矩阵`A`的最大的奇异值或者半正定矩阵`A*A`的最大特征值的平方根。  

好了，解释完了矩阵的谱范数的概念，我们继续说谱归一化。  

对于网络的一个layer：$g:h_{in} \to h_{out}$，从定义上来说，其`Lipscchitz norm` $$\left \|g  \right \|_{Lip}$$
的值等于$$sup_h\sigma(\bigtriangledown g(h))$$，其中$\sigma(A)$即指矩阵`A`的谱范数。  
那么，$\left\| g \right\|_{Lip}=sup_h\sigma(\bigtriangledown g(h))=sup_h\sigma(W)=\sigma(W)$，
则根据Lipschitz 定义的不等式，有：  

$$\left \|f  \right \|_{Lip} ≤\left \| (h_L → W^{L+1}h_L)\right \|_{Lip}· \left \|a_L\right \|_{Lip}
 · \left \| (h_{L-1} → W^{L}h_{L-1})\right \|_{Lip}... \left \|a_1\right \|_{Lip}·
 \left \| (h_{0} → W^{1}h_{0})\right \|_{Lip}$$
 
 $$
 =\prod_{l=1}^{L+1}\left \|(h_{l−1}→ W^lh_{l−1}) \right \|_{Lip} 
=\prod_{l=1}^{L+1}\sigma (W^l)$$

于是，当约束权重矩阵 `W`使其`LIpschitz constraint` $\sigma(W)=1$，则有：  

$$\bar{W}_{SN}(W):=W/\sigma(W)$$  

那么，当我们这样约束的时候，带入上一个不等式，便可得到$\left \|f  \right \|_{Lip}$ `is bounded from above by 1`。  

好了，现在我们说完了谱归一化的原理，回过头来重新看看开头的那句总结：  
　　谱归一化约束，通过约束 GAN 的 Discriminator 的每一层网络的权重矩阵(weight matrix)的谱范数来约束 Discriminator 的 Lipschitz 常数，从而增强 GAN 在训练过程中的稳定性。  
是不是有种豁然开朗的感觉？  

### 3. Trivials  
论文里剩下的部分就是一些实现时的 tricks 了，这里就不赘述了，感兴趣的话可以阅读原文自行探索～～  

那么，说完了这一篇[Spectral Normalization for Generative Adversarial Networks](https://arxiv.org/pdf/1802.05957.pdf)前导篇，
敬请期待我的下一篇[论文阅读-自注意力GAN_SAGAN](https://www.oukohou.wang/)～～  



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

