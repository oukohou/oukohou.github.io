---
layout: post
title:  "软件部署错误志"
date:   2019-01-16 18:26:49 +0800--
categories: [部署]
tags: [error, torch]  
---

> 前言:   
这篇主要记载各种软件、包之类的安装过程中的各种问题。    
这些问题确实有点困扰，但又不值得单独成文，所以一并放在这里。  
考虑到后续可能会有很多，这篇可能会冗长至极，所以在开头先放个目录，看官按需自取～～ 


- TOC
{:toc} 


## 1. torch安装

安装torch是参考的其官网：[Torch](http://torch.ch/docs/getting-started.html#_)  
但是在步骤 `./install.sh` 时一直出现问题：  
```text
torch/extra/cutorch/lib/THC/generic/THCTensorMath.cu(393): error: more than one operator "==" matches these operands:
            function "operator==(const __half &, const __half &)"
            function "operator==(half, half)"
            operand types are: half == half
```

问题没有好好记录，不方便复现了，具体参考这个issue：[Failed installation when running './install.sh'](https://github.com/torch/distro/issues/239)  
解决方法也在这个issue里：  
```bash
./clean.sh
export TORCH_NVCC_FLAGS="-D__CUDA_NO_HALF_OPERATORS__"
./install.sh
```
这里为了方便，所以粘贴的代码，感谢提供这个方法的 [pkuwwt](https://github.com/pkuwwt).   

## 2. TODO




<br>
<br>
<br>

<p  align="right">regards.</p>
<h4 align="right">
    <a href="https:www.oukohou.wang">
        oukohou.
    </a>
</h4>



<br>
微信公众号：璇珠杂俎(也可搜索oukohou)，提供本站优质非技术博文～～
![wechat_official_account](https://www.oukohou.wang/assets/imgs/wechat_official_account.png)  

