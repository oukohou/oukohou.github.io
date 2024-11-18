---
layout: post
title:  "Simulink与Modelsim联合仿真方法"
date:   2022-01-15 8:00:00 +0800--
categories: [硬件]
tags:   [FPGA]
---

- [将Verilog代码导入Simulink](#将verilog代码导入simulink)
- [Simulink仿真](#simulink仿真)
- [总结](#总结)


背景：在传感器系统仿真中，分为表头和数字电路部分。若在FPGA中单独仿真数字电路，无法有效的验证数字算法的正确性。同时，表头难以写在testbench中。而Simulink可以导入Veilog代码，有效的验证数字算法对表头的作用。

本文以谐振器为例，将谐振器输出信号传送到数字电路中，并处理输出回Simulink系统。

环境：Matlab R2016A；Modelsim SE 10.4

## 将Verilog代码导入Simulink

本文主要介绍系统流程，代码中仅将谐振器输出信号相乘，并输出。代码如下：

```verilog

module mul(clk,rst_n,PLL_CLK,in_a,in_b,out);

input clk;
input rst_n;
input PLL_CLK;
input  signed [15:0] in_a;
input  signed [15:0] in_b;
output reg signed [31:0]  out;


always @(posedge PLL_CLK or negedge rst_n) begin
	if (!rst_n) begin
		out<=1'd0;
	end
	else out<=in_a*in_b;
	
end

endmodule

```

首先，打开Matlab并将路径设置为verilog代码所在位置。

运行 cosimWizard；

![image-20220108155610439](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-040956.png)

这步要确保系统正确识别到了modelsim的安装路径，否则会报错。

![image-20220108155658350](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041008.png)

添加要仿真的代码，如果有很多.v文件。可同时添加。

![image-20220108155744062](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041010.png)

这步是编译，若报错，需要修改代码。

![image-20220108155844125](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041012.png)

这步中定义一个cosimulate的名字，无所谓写成什么。在options中，-t 1ns代表timescale 1ns。-novopt代表不对代码进行优化，不建议去掉，去掉后可能会将原始代码中的有效部分优化掉。

![image-20220108160115080](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041015.png)

这步中，一定要设置clk和rst。若不设置会报错。而陀螺系统中，由于我们还需要一个陀螺谐振频率

16倍频的时钟，所以单独加一个PLL_clk。

![image-20220108161159010](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041017.png)

设置out端的sample time。这里设置成和simulation option中相同即可。

![image-20220108161301646](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041020.png)

设置时钟上升沿有效，设置rest初始值和启动时间。

![image-20220108161343987](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041023.png)

设置HDL仿真时间。建议设置为0，可以看见完整的信号流。

![image-20220108161418134](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041026.png)

最后Finish即可。

会生成一个新的simulink文件。在此文件中，Compile HDL design按钮可以重新编译.v文件；每次更改代码后均需重新编译（调用的均是Modelsim）。Launch HDL Simulator是启动Mdelsim仿真器，每次进行simulink仿真前一定要保证Modelsim是启动状态。

至此，就将verilog代码导入了Simulink。

## Simulink仿真

将生成的模块拷贝到待仿真的simulink系统中。 

![image-20220108164820306](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041028.png)

该系统包括了谐振器的16倍频时钟和陀螺的信号输出。

其中要通过Data Type conversion转换数据类型。否则会报错。同时每个端口前也需要用零阶保持器将数据离散化。

设置完成后，首先双击Launch HDL Simulator等待Modelsim启动。再启动simulink仿真。

![image-20220108170118568](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041030.png)

![image-20220108170217923](https://raw.githubusercontent.com/wamogu/Images/refs/heads/main/2022-01-15-matlab与modelsim联合仿真/matlab%E4%B8%8Emodelsim%E8%81%94%E5%90%88%E4%BB%BF%E7%9C%9F-20220206-041032.png)

仿真结束后可以在Modelsim和Simulink中分别查看数字电路内部信号和系统外部信号。

## 总结

通过Matlab和Modelsim的联合仿真，可以有效的分析数字电路中控制系统的部分。解决了testbench难以模拟传感器系统表头信号的问题。
