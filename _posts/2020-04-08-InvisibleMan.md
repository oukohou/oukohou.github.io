---
layout: post
title:  "量子纠缠：invisible man"
date:   2020-04-07 20:07:21 +0800--
categories: [技术]
tags: [paddlepaddle, 实例分割]  
---


源代码：
- 百度aistudio notebook：[量子纠缠：invisible man](https://aistudio.baidu.com/aistudio/projectdetail/383779)  
- 知乎链接：[量子纠缠：invisible man](https://zhuanlan.zhihu.com/p/126713763)  

废话不多说，效果视频如下：  
<iframe src="//player.bilibili.com/player.html?aid=882716475&bvid=BV12K4y1r7op&cid=175226086&page=1" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>





然后是一一剖析：以上是在装逼[捂脸]

哈哈，客官勿怪哈，其实是闲来无聊，下班回来体验了下百度paddlepaddle新出的人体抠图功能模块。。。。

说是人体抠图，据我朴素的推测，应该就是deeplabv3+的实例分割功能，在其基础上进行了一些针对人体的定制化抠图功能吧~~

当然，个人推测而已哈~~



下面上代码哈：

首先是一些环境配置：
```python
!pip install paddlehub==1.6.0 -i https://pypi.tuna.tsinghua.edu.cn/simple
import os
import cv2
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg 
```  
然后导入paddlepaddle预训练好的实例分割模块：
```python
import paddlehub as hub
module = hub.Module(name="deeplabv3p_xception65_humanseg")
```  
将预先下载好的视频提取成图片并保存：（这里我本来想直接从视频流读图喂到模型里的，省去中间的保存环节，无奈官方示例给的是TensorFlow类似的input_dict形式，只好先保存了~~）
```python

# video 2 images
def extract_images(src_video_, dst_dir_): 
    video_ = cv2.VideoCapture(src_video_) 
    count = 0 
 while True: 
        flag, frame = video_.read() 
 if not flag: 
 break 
        cv2.imwrite(os.path.join(dst_dir_, str(count) + '.png'), frame) 
        count = count + 1 
 print('extracted {} frames in total.'.format(count))

src_video = 'work/humanSeg/gameForPeace/Cap2cap.mp4'
dst_dir_ = 'work/humanSeg/Marvel'
extract_images(src_video, dst_dir_)
```
ok，模型有了，输入有了，现在我们开始进行“人体抠图”：
```python

# test images
test_image_list = [os.path.join('work/humanSeg/Marvel', "{}.png".format(image_index)) for image_index in range(500)]

# segment images!
input_dict = {"image": test_image_list}
module.segmentation(data=input_dict)
```
好了，抠出了人体图，现在我们仿照官方代码，找张背景图进行混合，我就随便找了张大海的背景图了：
```python

from PIL import Image
import numpy as np

def blend_images(fore_image_path, base_image, save_dir_):
    """
    将抠出的人物图像换背景
    fore_image: 前景图片，抠出的人物图片
    base_image: 背景图片
    save_dir_: 保存路径
    """
    # 读入图片
    base_image = Image.open(base_image).convert('RGB')
    fore_image = Image.open(fore_image_path).resize(base_image.size)

    # 图片加权合成
    scope_map = np.array(fore_image)[:,:,-1] / 255
    scope_map = scope_map[:,:,np.newaxis]
    scope_map = np.repeat(scope_map, repeats=3, axis=2)
    res_image = np.multiply(scope_map, np.array(fore_image)[:,:,:3]) + np.multiply((1-scope_map), np.array(base_image))
    
    #保存图片
    res_image = Image.fromarray(np.uint8(res_image))
    save_path = os.path.join(save_dir_, os.path.basename(fore_image_path))
    res_image.save(save_path)

# blend images
save_dir = 'work/humanSeg/MarvelBlended'
base_image = 'work/humanSeg/resized_1000.png'
for index_ in range(500):
    fore_image = 'humanseg_output/{}.png'.format(index_)
    blend_images(fore_image, base_image, save_dir)
```
ok，抠出的人体图和背景融合后，我们再用opencv把这些图片写成视频并保存：
```python

# image2video
dst_video_ = 'work/humanSeg/marvel_ocean500.avi'
dst_video_ = cv2.VideoWriter(dst_video_, cv2.VideoWriter_fourcc(*'XVID'), 25, (1920, 1080), True)
def image2video():
    for index_ in range(500):
        frame = cv2.imread('work/humanSeg/MarvelBlended/{}.png'.format(index_))
        dst_video_.write(frame)

image2video()
```
好啦，这样我们就完成了开头的那个视频啦~~

然后所谓量子纠缠时隐时现的效果是怎么做到的呢？

哈哈哈，其实是这个分割模型是在真人数据集上训练的，然后Avengers们穿着盔甲就不容易识别出来啦，所以会出现边界不清时隐时现的问题~~~

哈哈哈（逃）

最后，你的赞是我最大的动力！



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

