---
layout: post
title:  "ubuntu 16.04 python2安装caffe无痛流程(hope so)"
date:   2018-10-26 20:29:05 +0800--
categories: [installation]
tags:   [ubuntu, caffe, installation, python]
---

每次装caffe都是一次痛苦的经历。  
这种连安装都如此不友好的库，弃之如敝屣都来不及，然而还总是有人用，
我又不得不历经千辛万苦把它装好，这里记录一下，希望我永远都不会再用得到～～

### 1. Dependencies
```bash
sudo apt-get install libprotobuf-dev libleveldb-dev libsnappy-dev libopencv-dev libhdf5-serial-dev protobuf-compiler
sudo apt-get install --no-install-recommends libboost-all-dev
sudo apt-get install libopenblas-dev liblapack-dev libatlas-base-dev
sudo apt-get install libgflags-dev libgoogle-glog-dev liblmdb-dev
```
具体啥是啥我也搞不清楚，反正照着copy就是～～

### 2. CUDA and cuDnn
网上也有很多关于CUDA和cuDnn的安装教程，感觉都太繁琐。
强烈建议各位按照下面这两个链接操作，轻松愉快。
- CUDA  
根据[这个页面](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=debnetwork)
进行操作，我用的配置是：  
> linux, x86_64, Ubuntu, 16.04, deb[network]
然后根据这个[installation instructions](https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&target_distro=Ubuntu&target_version=1604&target_type=debnetwork)操作就行。

- cuDnn  
根据[这个页面](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)
进行操作，我用的是[这个页面](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html)中的[2.3.2](https://docs.nvidia.com/deeplearning/sdk/cudnn-install/index.html#installlinux-deb)的命令操作。

### 3. OpenCV
这个没啥难度，自助随便[百度一下](https://www.google.com/?hl=zh_cn)跟着安装就行了。

### 4. Caffe
终于，过关斩将之后，我们来到了最终的大boss面前。  
恶龙固然可怕，但勇士也必将战胜胆怯奋然前行！  

#### 4.1 Python dependencies
找一个你要下载caffe代码的路径，cd到该路径下，然后：
```bash
git clone https://github.com/BVLC/caffe
cd caffe/python

# 安装python依赖。
for req in $(cat requirements.txt); do sudo pip install $req; done
```
注意到这些python依赖有点蛋疼，有版本要求，但太高也不行～～  
为了方便各位看官，我把自己的依赖版本列一下：

|package | version|
|:---------:|:----------------:|
|Cython| 0.29|
|numpy|	1.15.3
|scipy|1.1.0
|scikit-image|	0.14.1
|matplotlib|	2.2.3
|ipython|  5.8.0
|h5py|2.8.0
|leveldb|   0.194
|networkx|	2.2
|nose|	1.3.7
|pandas|	0.23.4
|python-dateutil|	2.7.3
|protobuf|	3.6.1
|python-gflags|	3.1.2
|pyyaml|	3.13
|Pillow| 5.3.0
|six|1.11.0


#### 4.2 The Caffe！
安装完了python依赖项，然后是caffe了：
```bash
# 由于我们还在caffe/python路径下，所以切换回上一目录：
cd ..
cp Makefile.config.example Makefile.config
```
然后打开Makefile.config，将下面这些行改成：
```text
1. line4:   USE_CUDNN := 1
2. line12:  USE_LEVELDB := 1
3. line13:  USE_LMDB := 1
4. line23:  OPENCV_VERSION := 3 # 如果你装的是opencv2.x版本的话，当我没说
5. line35:  仔细阅读这一段的说明，注释掉对应的某几行
6. line94:  WITH_PYTHON_LAYER := 1
7. line97:  INCLUDE_DIRS := $(PYTHON_INCLUDE) /usr/local/include /usr/include/hdf5/serial
8. line98:  LIBRARY_DIRS := $(PYTHON_LIB) /usr/local/lib /usr/lib /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu/hdf5/serial 
"""
 看这篇文章的标题，注意到我用的是python2.7，这是为了减少不必要的麻烦。
 我也衷心劝各位，如果没有特殊的必要，还是用python2装caffe吧。
 虽然python核心团队计划在2020年就要停止支持Python2了。
 但是，你都决定装caffe了，还谈这些支持不支持有啥意义呢？
 所以，为免不必要的麻烦，奉劝看官还是用python2装caffe吧。
 当然，如果你用python3的话，记得修改Makefile.config里对应的行数，具体百度。
"""
```
现在我们的命令行还是在刚刚下载的caffe目录下，然后：
```bash
mkdir build
cd build
cmake ..
sudo make all -j8
sudo make install -j8
sudo make runtest -j8 # 这一步可能会报错，不用管，反正这里只是测试而已，前一步已经安装好了。至少我是没管的。
sudo make pycaffe -j8
```
到了这里，如果幸运的话，你运行：
```bash
python -c "import caffe;print(caffe.__path__)"
```
应该会出现类似下面这样的输出：
```text
['/usr/local/lib/python2.7/dist-packages/caffe']
```
那么恭喜你，你成功了！


### 5. A vast expanse of ocean
如果你没那么幸运，那么恭喜你，和我一样掉入了安装caffe的汪洋大海里。

这片海，浮浮沉沉着无数和我们一样苦逼兮兮的人～～

但你比我又幸运一点，我这里恰好有几个解决错误的小手段，你可能用得上！

#### Error 1：
```text
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/data/Downloads/caffe/python/caffe/__init__.py", line 1, in <module>
    from .pycaffe import Net, SGDSolver, NesterovSolver, AdaGradSolver, RMSPropSolver, AdaDeltaSolver, AdamSolver, NCCL, Timer
  File "/home/data/Downloads/caffe/python/caffe/pycaffe.py", line 13, in <module>
    from ._caffe import Net, SGDSolver, NesterovSolver, AdaGradSolver, \
ImportError: libcaffe.so.1.0.0: cannot open shared object file: No such file or directory
```
solution：  
   找到你的刚刚下载的caffe根目录，libcaffe.so.1.0.0应该在”/build/install/lib/“文件夹下，
   把这个路径添加到系统路径下：
```bash
sudo vim ~/.bashrc

# 然后找到下面这一行：
export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

# 然后把刚刚找到的libcaffe.so.1.0.0添加进去，比如我的变成：
export LD_LIBRARY_PATH=/home/data/Downloads/softwares/caffe/build/install/lib/:/usr/local/cuda-9.0/lib64${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}

# 然后使该改变生效：
source ldconfig
```


#### Error 2:
```text
ImportError: xxx/caffe/_caffe.so: undefined symbol: _ZN5caffe3NetIfE21CopyTrainedLayersFromENSt7__cxx1112basic_stringIcSt11
```

solution:  
    这个错误也是非常蛋疼的。  
    我百度了超级多，一看就是互相复制粘贴的，都说要把Makefile.config里的     
```text
# Uncomment to support layers written in Python (will link against Python libs)
# WITH_PYTHON_LAYER := 1
```
这行给取消注释掉。
但其实我在[4.2](#4.2-the-caffe！)中已经设置了，却依然出现这个错误！    
那我是怎么解决的呢？  
说实话我不清楚。。。  
应该是因为我重复安装了一遍？  
或者，是幸运女神的眷顾？  
反正这个问题我不知道如何解决掉的。。。    
想起了那张经典图：    
![but why?](https://s1.ax2x.com/2018/10/26/5Xp4rR.jpg)  
这里就有点对不起各位看官了，为做补偿，贴出一个官方[issue](https://github.com/BVLC/caffe/issues/3834)。    
有心的看官应该注意到了，这几行的奇数行都押韵！(卖个小萌)  
    
### 6. The end
综上，就是我如何与caffe斗智斗勇的过程。  
完结，撒花！  
![justice!](https://s1.ax2x.com/2018/11/06/5m4gIN.jpg)  


regards.
<h4 align = "right">oukohou.</h4>

