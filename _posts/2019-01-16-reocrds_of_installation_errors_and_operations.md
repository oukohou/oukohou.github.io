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


## 2. matlab datanum and python datetime convert
see :
- [Converting MATLAB's datenum to Python's datetime](http://sociograph.blogspot.com/2011/04/how-to-avoid-gotcha-when-converting.html)
- [python-datetime-to-matlab-datenum](https://stackoverflow.com/questions/8776414/python-datetime-to-matlab-datenum)



## 3. **caffe.set_mode_gpu()**: AttributeError: 'module' object has no attribute 'set_mode_gpu'
`as this section may be read by people not speaking Chinese, so I will write in English.`  

### 3.1 error:  

```bash
Traceback (most recent call last):
  File "/home/.../xxx.py", line 7, in <module>
    import rsa
  File "../src/rsa/__init__.py", line 1, in <module>
    from . import model 
  File "../src/rsa/model.py", line 18, in <module>
    caffe.set_mode_gpu()
AttributeError: 'module' object has no attribute 'set_mode_gpu'
```

### 3.2 solution:

    sys.path.insert(0, '/path/to/caffe/python')
    import caffe
    caffe.set_mode_gpu()

namely, add the `caffe/pathon` path to you `sys.path` before `import caffe`.  

### 3.3 analysis:  
This problem may be the results of package `caffe`'s path.  

For me, if I do the following from the Ubuntu Terminal, everything goes fine:
![from_terminal](https://s1.ax2x.com/2019/02/25/5jqWrX.png)  

but if I do from the Pycharm IDE, errors occur:

![from_pycharm](https://s1.ax2x.com/2019/02/25/5jqsp3.png)  

note that I tested the package `caffe`'s path in both ways, and got different results:  
- in the Ubuntu terminal, namely the way which goes fine, I got 
```text
'/home/CVAR-B/softwares/caffe/caffe/python/caffe/__init__.pyc'
```
which is the expected result;
- in the Pycharm IDE way, namely the way error occurs, I got 
```text
'/usr/local/lib/python2.7/dist-packages/caffe/__init__.pyc'
```
which is not the expected result.  

In view of this discovery, I did this one more thing to handle the error:

    sys.path.insert(0, '/path/to/caffe/python')
    import caffe
    caffe.set_mode_gpu()

namely, add the `caffe/pathon` path to you `sys.path` before `import caffe`.  

and the result shows this can be a workaround:
![pycharm_IDE_success](https://s1.ax2x.com/2019/02/25/5jquKK.png)  

See the `caffe.__file__`'s result, now returns the expected path.   



## 4. TODO




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

