---
layout: post
title:  "软件部署错误志"
date:   2019-04-21 18:26:49 +0800--
categories: [部署]
tags: [error, torch]  
---

> 前言:   
这篇主要记载各种软件、包之类的安装过程中的各种问题。    
这些问题确实有点困扰，但又不值得单独成文，所以一并放在这里。  
考虑到后续可能会有很多，这篇可能会冗长至极，所以在开头先放个目录，看官按需自取～～ 

Update log:
```text
2019-02-25： add section3:caffe.set_mode_gpu()    
2019-04-22： add section4:ConnectionResetError:[Errno 104]Connection reset by peer
 
```


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
![from_terminal](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/records_of_installation/section3_terminal.png)  

but if I do from the Pycharm IDE, errors occur:  
![from_pycharm](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/records_of_installation/section3_from_Pycharm_IDE.png)

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
![pycharm_IDE_success](https://raw.githubusercontent.com/oukohou/image_gallery/master/blogs/records_of_installation/section3_Pycharm_IDE_2.png)  

See the `caffe.__file__`'s result, now returns the expected path.   



## 4. ConnectionResetError: [Errno 104] Connection reset by peer

这个是今天在服务器上用`pip` 安装 `pytorch`的时候出现的问题，应该是`curse of speed`。    
什么意思呢，听我慢慢道来～    

### 4.1. error：  

当安装pytorch的时候，按照[官网](https://pytorch.org/)的指示，用的命令是：  
```bash
pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cu100/torch_nightly.html
```

然后就出错了：
```bash
Looking in links: https://download.pytorch.org/whl/nightly/cu100/torch_nightly.html
Collecting torch_nightly
  Downloading https://download.pytorch.org/whl/nightly/cu100/torch_nightly-1.1.0.dev20190421-cp35-cp35m-linux_x86_64.whl (702.6MB)
    8% |##                              | 56.7MB 73.8MB/s eta 0:00:09Exception:
Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/pip/_vendor/urllib3/response.py", line 360, in _error_catcher
  …… ……
ConnectionResetError: [Errno 104] Connection reset by peer

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/usr/local/lib/python3.5/dist-packages/pip/_internal/cli/base_command.py", line 179, in main
  …… ……
  File "/usr/local/lib/python3.5/dist-packages/pip/_vendor/urllib3/response.py", line 378, in _error_catcher
    raise ProtocolError('Connection broken: %r' % e, e)
pip._vendor.urllib3.exceptions.ProtocolError: ("Connection broken: ConnectionResetError(104, 'Connection reset by peer')", ConnectionResetError(104, 'Connection reset by peer'))
```

### 4.2. curse of speed  
啥叫`curse of speed`？  
先从`curse of knowledge`说起。  

- 知识的诅咒  
可以参考知乎这一个提问：[什么是知识的诅咒？](https://www.zhihu.com/question/37635606)  
其中一个回答说： [什么是知识的诅咒？-王文的回答](https://www.zhihu.com/question/37635606/answer/94053569)  
   
```text
知识的诅咒在奇普·希思与丹·希思合著的《粘住》一书中有介绍，它反映了一个现象：
如果我们很熟悉某个对象的话，那么我们会很难想象，在不了解的人的眼中，这个对象是什么样子的。
我们的知识水平会对我们产生影响，使我们不能从别人的角度看世界，不能准确评估别人有多少信心。
我们被我们所掌握的知识“诅咒”了。
```
简单说，因为掌握的知识太多，结果反而产生了不利影响。  

- curse of speed  
那么现在说回我们的这个错误。  
之所以我叫它`curse of speed`，是因为原因也在于我们的网速太快了。  
注意看上面的错误信息：  

```text
8% |##                              | 56.7MB 73.8MB/s eta 0:00:09Exception:
```
我的下载速度达到了73.8M/s，这么高的速度，我们知道这肯定是同时进行了大量的并发链接的。  
那么我们再看下报错信息：  

```text
ConnectionResetError: [Errno 104] Connection reset by peer
```
是个连接错误，errno 104？我们不妨搜一搜：  
看到了这个博客：[errno 104:connetction reset by peer的错误分析](https://blog.csdn.net/alibo2008/article/details/45694845)
```text
errno=104错误表明你在对一个对端socket已经关闭的的连接调用write或send方法.
在这种情况下，调用write或send方法后，对端socket便会向本端socket发送一个RESET信号，
在此之后如果继续执行write或send操作，就会得到errno为104，
错误描述为connection reset by peer。
```
那么真相就要浮出水面了：  
因为我们的网速太快，导致同时并发链接数太高，服务器主动断开了与我们的连接，然后我们再继续发包的时候，就会收到这个错误。  

### 4.3. solutions
那么怎么解决的呢？  
解铃还须系铃人。注意到我最开始的目的：用`pip` 安装 `pytorch`。我用的命令是：  
```bash
pip install torch_nightly -f https://download.pytorch.org/whl/nightly/cu100/torch_nightly.html
```

既然直接用pip会引起`curse of speed`，那么何不先把这个package下载下来然后本地安装？  
机智如我，就先用wget来下载了：  
```bash
wget https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl
```
显示：  
```bash
…… ……
Connecting to download.pytorch.org (download.pytorch.org)|99.84.239.94|:443... connected.
…… ……
Saving to: 'torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl'

torch-1.0.1.post2-cp35-cp35m-linux_x86_6  20%[===============>                                                                  ] 122.86M  31.0MB/s    in 4.0s    

2019-04-22 02:54:09 (31.0 MB/s) - Read error at byte 128829303/636801773 (Connection reset by peer). Retrying.

--2019-04-22 02:54:10--  (try: 2)  https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl
…… ……
Saving to: 'torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl'

torch-1.0.1.post2-cp35-cp35m-linux_x86_6  37%[++++++++++++++++=============>                                                    ] 229.42M  25.7MB/s    in 4.1s    

2019-04-22 02:54:14 (25.7 MB/s) - Read error at byte 240565495/636801773 (Connection reset by peer). Retrying.

--2019-04-22 02:54:16--  (try: 3)  https://download.pytorch.org/whl/cu100/torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl
…… ……
Saving to: 'torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl'

torch-1.0.1.post2-cp35-cp35m-linux_x86_6 100%[++++++++++++++++++++++++++++++===================================================>] 607.30M  29.7MB/s    in 11s     

2019-04-22 02:54:28 (34.2 MB/s) - 'torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl' saved [636801773/636801773]
```

注意到中间还是会时不时地`Connection reset by peer`，不过wget显然对此十分鲁棒，经过2次断点续传之后完成了使命。  
那么接下来直接本地安装：  
```bash
pip install torch-1.0.1.post2-cp35-cp35m-linux_x86_64.whl
```
即可。美滋滋～～  


## 5. TODO




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

