[TOC]

# 概率论的基本概念

## 随机事件与样本空间

### 基本历史

- 概率论起源于17世纪

- 1654年，Pascal和Fermat对”分赌本“问题的讨论

- 使概率论成为数学的一个分支的奠基人是瑞士数学家--伯努利

- 概率论的飞速发展是在17世纪微积分学说建立以后

### 研究对象

- 事件发生的现象可分为确定性现象和不确定现象，而《概率论与数理统计》是研究统随机现象的统计规律性的一门数学学科。例如：抛硬币、测量物理量(如长度、时间)的误差、某批产品的使用寿命

### 随机试验

#### 随机试验发生的条件

- 可以在相同的条件下重复进行

- 试验的全部结果(不止一个)之前是知道

- 不能预测试验出现的结果

#### 事件

> 随机试验中各种可能出现结果成为事件，通常用A,B,C等来表示
> 必然事件: 在随机试验中必然发生的事件，用 $\Omega$ 表示
> 不可能事件: 在随机试验中不可能发生的事件，用 $\emptyset$ 表示
> 基本事件: 不能再进行划分的最小事件，基本事件可能由于研究的目的和方法不同会有差异
> 复合事件:

#### 样本空间

由所有的随机试验的结果组成的集合，即由全体的基本事件所对应的元素，组成的集合称为样本空间。样本空间的中每一个元素实际上是每一个基本事件，称为样本点，每个样本点对应的是一个基本事件，通常情况用基本事件构成样本空间。

样本空间用 $\Omega$ 表示，是一个必然事件; 样本点用 $\omega$ 表示

ex1: 将一枚硬币连续抛两次，H: 正面; T: 反面那么 $\Omega = \{HH, HT, TH, TT\}$

ex2: 连续向一个目标射击，直到命中。 $\omega_i$ 表示前i-1次未命中，而第i 次命中，i=1,2,3,..., 那么 $\Omega = \{\omega_1, \omega_2, \omega_3, \ldots \}$

#### 集合论的方式表示随机事件

- 随机事件之间的关系和运算和集合论之间的关系和运算是一一对应的，这样就可以用集合论的方式来处理随机事件的关系和运算。虽然是按着集合论的方式去表达，但需要按着概率的方式去理解。

- ex1: 投掷一个骰子， $\Omega = \{1,2,3,4,5,6\}$. A事件表示奇数点, 那么A事件的样本点可以表示为A={1,3,5}; 同理 B: 偶数点 B={2,4,6}.  如果某个事件的其中一个样本点发生了，就说明这个事件发生了，这样就很好解释了事件和样本点之间的关系。

- ex2: 样本空间成为必然事件，即其中的一个样本点发生了，那么该事件就发生了。

- 用事件是否发生这样一种方式来表达和理解集合之间的符号。

- Venn图表示事件之间的关系

- > 包含关系(包含事件):  $A \subset B$
  > 
  > 和关系(和事件): $A \bigcup B = C$  或者 $\overbrace{\bigcup_{k=1}}^n A_k$
  > 交关系(积事件): $A \bigcap B = AB $ 或者 $\overbrace{\bigcap_{k=1}}^n A_k$
  > $A_1, A_2, \ldots A_n$ 称为完备事件组: 满足条件
  > 
  > $\left\{
  > \begin{array}{lr}
  >   A_1 \bigcup A_2 \bigcup \ldots \bigcup A_n = \Omega\\
  >   A_i \bigcap A_j = \emptyset & i \neq j
  > \end{array}
  > \right.$
  > 
  > 对立事件: $AB = \emptyset$  且 $A \bigcup B = \Omega$， 那么A，B称为对立事件
  > 差关系:  

- 运算规律: 交换律、结合律、分配律、对偶法则

## 概率的概念和性质

### 概念

- 概率分为主观概率和客观概率

- 陈希孺《概率论与数理统计》

- 1933年，科尔莫哥洛夫，做了系统的整理工作，提出了概率的公理化定义，用几条很少的公理，就建立起来了宏大的概率论的学科。概率的公理化定义主要有以下三条, 对于事件 A

- > (1) 非负性公理: 任何一个事件发生的概率一定是非负的. 即 $0 \leq P(A) \leq 1$
  > 
  > (2) 正则性公理: $p(\Omega) = 1$
  > 
  > (3) 互不相容的事件 $A_1, A_2, A_3, \ldots$ 满足 $P(\bigcup A_j) = \sum A_j$

- <font color=red> 注意: 概率为0的事件是不可能发生的，这种论述是错误的。</font>原因：不可能事件的概率一定为0，但概率为0的事件并不一定是不可能事件；必然事件的概率一定为1，但概率为1的事件并不一定是必然事件。但对于古典型来说概率为0的事件一定是不可能发生的；概率为1的事件一定是必然事件。 

- > (1) 对于连续型随机变量X服从[0,1]上的均匀分布,那么X取每个值的概率都为0,但是并非不可能
  > 
  > (2) 圆上任意取三点构成锐角三角形、钝角三角形、直角三角形的概率分别为1/4,3/4,0. 因为圆上任意三角形能够构成直角三角形，这事件明明会发生，也就是这是可能事件，这就是说可能事件的概率为0，概率为0的事件也是可以发生的。因为概率只反映了一件事情发生的可能性大小，概率为0的事件并不意味着不发生；同样概率为1的事件也不意味着一定发生。
  > 
  > (3) 还比如一个点在圆内及其边界移动，但落在边界和圆内某一点的概率为0，但这样的事件是可能发生的; 落在圆内的概率为1，但这样的时间不一定会发生。
  > 
  > (4) 从山顶悬挂一条线到山下，它刚好穿过山下某个针的针眼是有可能发生的，但这个事件发生的概率为0 

### 性质

- $P(\emptyset) = 0$

- 若 $A_1, A_2, \ldots, A_n$ 互不相容， 则 $P( \bigcup_{k=1}^n A_k) = \sum_{k=1}^n A_k$

- 对于任意事件 A, $P(A) + P(\overline{A}) = 1$

- 对于事件A， B $A \subset B$ 则 $P(A) \leq P(B); P(B-A) =  P(B) - P(A)$

- 对于任意两个事件A，B，$P(A \bigcup B) = P(A) + P(B) - P(AB)$

## 古典概型

### 要求

- 设E是一个实验，满足(1) 只有有限多个样本点  (2) 每个样本点发生的可能性相同(等可能事件)

### 排列、组合

- 加法原理

- 乘法原理

- 通过加法和乘法原理实现古典概型的计算

- 公式

$C_n^m = \frac {A_n^m} {m!} = \frac {n!} {m! (n-m)!}$

$C_n^m = C_n^{n-m}$

$C_n^m + C_n^{m-1} = C_{n+1}^m$

$C_n^0 + C_n^1 + C_n^2 + \ldots + C_n^n = 2^n$ 左边可以看成是$(1+1)^n$ 的牛顿二次展开

### 计算古典概型

#### 步骤

- 找出的样本空间，保证样本点的等可能性。不同的解法思路会导致样本空间不一样，比如，用排列的方式考虑了顺序问题；用组合的方式不考虑顺序问题

- 模型化：提炼出公共的、通用的模型

#### ex1

- 盒子中有10个球，分别编号为1，2，3，... ， 10，从中任取3个，求P(A)，A表示三个球中第二大的号码为4.

- > （1）求出样本空间，并且样本点的等可能性。即 $C_{10}^3$
  > 
  > （2）抽出最小号码为 $C_3^1$
  > 
  > （3）第二大号码为4，即$C_1^1$
  > 
  > （4）第三个球为$C_6^1$
  > 
  > （5）$P(A) = \frac {C_3^1 C_1^1 C_6^1} {C_{10}^3}$_

#### ex 2

- 袋子中有a只黑球，b只白球，现一个一个取出，不放回抽样，求第k次取到的是黑球的概率 $1 \leq k \leq a+b$ 
- 解法1：排列方式
- > （1）对a+b个球进行编号，那么排列的方式有 (a+b)!，这部分就是样本空间
  > 
  > （2）有利场合: 第k个球是黑球的逻辑是，从a个黑球中拿出来一个黑球的方法有a种，将其放到第k个位置；然后剩下的(a+b-1)个球进行全排列。
  > 
  > （3）$P = \frac {a (a+b-1)!} {(a+b)!} = \frac {a} {a+b}$
- 解法2：组合方式
- > （1）a+b个球没有顺序，那么我们对[1, a+b]个位置选出来a个位置放黑球，此部分就是样本空间 $C_{a+b}^a$
  > 
  > （2）有利场合:  第k位置放置黑球，剩下的a-1个位置放剩下的黑球，因此$C_{a+b-1} ^{a-1}$
  > 
  > （3）$P= \frac {C_{a+b-1}^{a-1}} {C_{a+b}^a} = \frac {a} {a+b}$

#### ex 3

- 设有n个球，每个球都可以以同样的概率 1/N 落到N个格子(N >= n)中的每个格子，求（1）某指定的n 个格子中各有一个球的概率P(A) （2）任何n 个格子各有一个球的概率P(B)
- > （1）样本空间 $N^n$
  > 
  > （2）n个格子各有一个球的相当于组合 n!, 因此 $P(A) = \frac {n!} {N^n}$
  > 
  > （3）任何n个格子，因此首先从N个格子选择出n个格子，然后再做全排列 $P(B) = \frac {C_N^n n!} {N^n}$

### 几何概型

- 古典概型的延展,使用测度的概念解决几何概型等可能事件概率的计算

- 长度、面积、体积和古典概型共性的东西是，这种也是等可能事件。这是有限样本空间的古典概型的推广，推广到无限样本空间。

- ex 会面问题: 两个人相约在5-6点在某地会面，先到者等待另外一个人20分钟，过时即可离去，求这两个人见面的概率。
  
  > 另x,y 分别表示两个人到达的时刻，满足见面的条件是 $|x-y| \leq 20$
  > 
  > $P = \frac {|x-y| \leq 20 的面积} {60^2}$

## 条件概率、乘法公式、全概率公式、贝叶斯公式

### 条件概率

- 引例
  
  > (1)连续生三个小孩，A事件表示三个都是女孩，那么P(A) = 1/8.
  > 
  > 分析：男: $\bigotimes$  女：$\bigoplus $ 那么样本空间为 $\Omega = \{\bigotimes\bigotimes\bigotimes, \bigotimes\bigotimes\nabla,\bigotimes\nabla\bigotimes,\nabla\bigotimes\bigotimes,\bigotimes\nabla\nabla,\nabla\bigotimes\nabla,\nabla\nabla\bigotimes,\nabla\nabla\nabla\}$
  > 
  > (2) 若已知B事件表示三个孩子中有一个是女孩，那么P(A|B) = 1/7
  > 
  > 样本空间为 $\Omega = \{\bigotimes\bigotimes\nabla,\bigotimes\nabla\bigotimes,\nabla\bigotimes\bigotimes,\bigotimes\nabla\nabla,\nabla\bigotimes\nabla,\nabla\nabla\bigotimes,\nabla\nabla\nabla\}$

- 定义
  
  > 假设有两个事件A，B，$P(B) \neq 0$ , 在给定B发生的条件下A发生的概率$P(A|B) = \frac {P(AB)} {P(B)}$
  
  - 使用古典概型定义(条件概率在本质上和古典概型是一致的)
    
    > 实验有N个结果(等可能是的)，其中A事件有M1 个，B事件有M2个， AB同时发生的有M12个，那么若B发生，那么现在新的样本空间为$\Omega = M2$ ，那么 $P= \frac {\frac {M12} {N}} {\frac {M2} {N}} (此部分为古典概型，样本空间仍然为N) = \frac {M12} {M2} (此部分为条件概率，样本空间变为M2)= \frac {P(AB)} {P(B)}$
  
  - 在几何概型中
    
    > 以$m(A), m(B), m(AB), m(\Omega) $ 表示 $A,B,AB,\Omega $ 所对应的点的测度，且 $P(B) \gt 0 $ 则 $P(A|B) = \frac {AB} {B} = \frac {\frac {m(AB)} {m(\Omega)}} {\frac {m(B)} {m(\Omega)}} = \frac {m(AB)} {m(B)}$

- 性质

- 例子
  
  > 令盒子中有1-10个编号的小球，从中抽取两次，一次一个球(有放回)，X1表示第一个号码，X2表示第二个号码，令A事件X1=4，B事件为X1+X2 = 7，求P(A|B) 和P(B|A)
  > 
  > 解：$P(A|B) = \frac {P(AB)} {P(B)} = \frac {P(X_1=4,X_1 + X_2 = 7)} {P(X_1+X_2=7)} = \frac {P(X_1=3,X_2=4)} {P(X_1+X_2=7)} = \frac {\frac {1} {100}} {\frac {6} {100}} = \frac {1} {6}$
  > 
  > $P(B|A) = \frac {P(AB)} {P(A)} = \frac {X_1=4,X_1+X_2=7} {X_1=4} = \frac {\frac {1} {100}} {\frac {1} {10}} = \frac {1} {10}$

### 乘法公式

- 公式
  
  > $P(B) > 0, P(A|B) = \frac {P(AB)} {P(B)}$ 
  > 
  > ==> $P(AB) = P(B) P(A|B)$
  > 
  > 令A，B，C是实验E的三个事件，且P(ABC) > 0,那么
  > 
  > $P(ABC) = P(A) \frac {P(AB)} {P(A)} \frac {P(ABC)} {P(AB)} = P(A)P(B|A)P(C|AB)$

- ex
  
  > 对某产品进行三次破坏性实验，产品没有通过第一种实验的概率为0.3；产品通过第一种实验，但是没有通过第二种实验的概率为0.2；产品通过第一二两种实验，但是没有通过第三种实验的概率为0.1，事件A表示没有通过三种实验，求P(A)
  > 
  > 分析: $A=  A_1 \bigcup A_2 \bigcup A_3$ <=> $\overline A = \overline A_1 \overline A_2 \overline A_3$
  > 
  > $P(A) = 1 - P(\overline A) = 1 - P(\overline A_1 \overline A_2 \overline A_3) = 1- P(\overline A_1) P(\overline A_2 |\overline A_1) P(\overline A_3| \overline A_1 \overline A_2) = 1 - 0.7 * 0.8 * 0.9$

### 全概率公式

- 引例: 将一个事件分解要成若干个互不相容的事件，即将一个复杂的概率分解成互不相容的若干个简单概率
  
  > 甲盒中有1-15编号的卡片，乙盒中有1-10编号的卡片，从甲乙两个盒中任意抽取一个盒子，然后在从中抽取一张卡片，求抽取的卡片是偶数的概率
  > 
  > 分析: A: 抽取到的是偶数的卡片；B1：抽到的是甲盒； B2： 抽到的是乙盒，
  > 
  > 那么 $\Omega = B_1 \bigcup B_2, B_1 \bigcap B_2 = \emptyset$
  > 
  > $A = AB_1 \bigcup AB_2$
  > 
  > $P(A) = P(AB_1 \bigcup AB_2) = P(AB_1) + P(AB_2) = P(B_1)P(A|B_1) + P(B_2)P(A|B_2) = 0.5 * 7/15 + 0.5 * 5/10$

- 定义
  
  > $B_1,B_2,\ldots, B_n$,   是一个样本空间完备事件组，并且 $(B_1\bigcup B_2,\dots,\bigcup B_n = \Omega, i \neq j, P(B_i) > 0, i = 1,2,3,\ldots,n)$
  > 
  > 那么$P(A) = P(A \bigcap \Omega) = P(A \bigcap (B_1 \bigcup B_2,\bigcup \ldots,\bigcup B_n)) = P(AB_1 \bigcup AB_2 \bigcup \ldots \bigcup AB_n) = \sum_{i=1}^nP(AB_i) = \sum_{i=1}^n P(B_i) P(A|B_i)$

- ex 1
  
  > 一批零件分别从甲乙丙三个厂家运来的概率分别为0.5，0.25，0.25，发生次品的概率分别为2%，2%，4%，求所有产品的次品率是多少？
  > 
  > 分析：另B1 = {甲厂}，B2 = {乙厂}，B3 = {丙厂}，那么
  > 
  > $P(A) = P(AB_1) + P(AB_2) + P(AB_3) $
  > 
  > $= P(B_1)P(A|B_1) + B(B_2) P(A|B_2) + P(B_3)P(A|B_3) $
  > 
  > $= 0.5 * 0.02 + 0.25*0.02 + 0.25*0.04$

### 贝叶斯公式

- 定义
  
  > 全概率公式: $B_1,B_2,\ldots,B_n 是 \Omega 的一个划分，那么 P(A) = \sum_{i=1} ^n P(A|B_i) 。$B1-Bn可以看做n个导致A事件发生的原因
  > 
  > $P(B_j|A) = \frac {P(B_jA)} {P(A)} = \frac {P(B_j) P(A|B_j)} {P(A)} $
  > 
  > $= \frac {P(B_j) P(A|B_j)} {\sum_{i=1}^n P(A|B_j)}$ 分子是分母中的一项

- 思想
  
  > 先验概率 $P(B_j), j=1,2,\ldots,n$ 是诸多的原因，反应的是各种途径或者各种原因占到的各种可能性的大小，在生活中通常是一些经验的总结，信息的归纳等;
  > 
  > 后验概率$P(B_j|A)$表示做完实验后，事件A发生的各种可能的原因有一个从新的认识
  > 
  > 从结果探求各种可能的原因，他们各占的可能性有多大。比如一个次品发生了，那么这个次品分别在甲乙丙三个厂出来的可能性分别有多大

- ex
  
  > 用某检验方法诊断肺癌，A事件表示被检验者患有肺癌; B事件表示阳性，求P(A|B), 表示诊断为阳性，且患肺癌的概率有多大？
  > 
  > 已知P(A) = 0.0004, 表示人群中有0.0004患肺癌，是统计的结果
  > 
  > P(B|A)= 0.95, 表示，在患肺癌的人群中，诊断为阳性的概率为0.95
  > 
  > $P(\overline B| \overline A) = 0.90$， 表示在正常人中，诊断为阴性的概率为0.90
  > 
  > $P(A|B) = \frac {P(AB)} {P(B)}$
  > 
  > $=\frac {P(A) P(B|A)} {P(A)P(B|A) + P(\overline A) P(B| \overline A)} = \frac {0.0004 * 0.95} {0.0004*0.95 + 0.0096*0.1} = 0.0038$

- 统计、分析、推断的基础

## 独立性、系统的可靠性

### 独立性

- 定义
  
  > 设A，B是随机试验E的两个事件，若满足 P(AB)= P(A)P(B)，称A，B是相互独立的事件

- 性质
  
  > 若A，B事件独立，则 $\overline A 与 B, A 与 \overline B, \overline A 与 \overline B$ 都是独立的

- 相互独立、两两独立区别

## Monty Hall Problem

- 问题描述
  
  > 参赛者会看到三扇关闭的门，其中一扇后面有汽车，另外两扇门后有羊；当参赛者选定一个门后，但未开启它的时候，知道门后情形的节目主持人开起剩下两个门中的一个，漏出一只山羊；主持人会问参赛者会不会换另一个关上的门。求最终换和不换的情况下，赢得汽车最大的概率
  > 
  > 分析:（1）直觉。任打开一扇门，选中的概率为1/3，没选中的概率为2/3; 如果坚持不换，则一开始选中就中奖，概率为1/3；如果坚持换，则一开始没选中就中奖，概率为2/3
  > 
  > (2) 贝叶斯分析: 若选择换，那么
  > 
  > P(选中汽车的概率) = P(第一次选择山羊) P(第二次选择汽车| 第一次选山羊) + P(第一次选择汽车) P(第二次选择汽车|第一次选择汽车) = 2/3 *1 + 1/3 * 0 = 2/3
  > 
  > 如果选择不换，那么
  > 
  > P(选中汽车) = 2/3 * 0 + 1/3 * 1 = 1/3

## 随机测试

TODO

# 随机变量及其分布

## 随机变量的含义

- 随机事件是随着不同的机会而发生的结果, 随机变量随着机会的不同而不同；取值随机会而定，随机试验可能会发生各种各样的结果，某个结果可以对应某个值，比如可以用变量x来表示某随机试验发生的结果，这个x随着不同的结果而取不同的值。==> 这个x就是这个随机试验结果的函数，在试验之前x的取值是不同的，只有在试验发生之后，才能获得x的结果取值。

- 随机变量的定义域是基本事件的全体，值域是[0,1]

- 随机事件和随机变量的区别
  
  > 随机变量和确定性变量的区别：（1）确定性变量: 当条件给定或者自变量给定，这个函数取得的结果是确定的；（2）随机变量: 只有在试验结果发生后，结果才能确定
  > 
  > 概率论的中心内容：就是对随机变量的研究，因为对于某个随机试验，往往更关心的是某个特定的结果或者某个特定发生的问题，而这个就是对应我们随机变量取得某些值
  > 
  > 随机事件: 从静态或者点态的角度解决；随机变量是一个动态的角度，从整体上把握和讨论随机试验的所有结果。这就是好比常量和变量的区别。概率论从计算一个单个或者孤立的事件概念发展到一个更高的理论体系，基础就是对随机变量的讨论。在随机变量这个基本前提下对可能性展开完整性的讨论。

- ex
  
  > （1）投掷一枚硬币， Z=1 (正面)； Z = 0 (反面)
  > 
  > （2）检测m件产品，Z=0,1,2,3,...,m
  > 
  > （3）测量误差：$\varepsilon \in (-\infty, +\infty)$

- <font color=red> 对随机变量而言，不仅要关心取到哪些值，更要关心取到这些值得概率，那么随机变量取到的值及其发生的概率，就构成了随机变量的分布。</font>

### 离散型随机变量

#### 含义

- 随机变量取到的值是有限个，就是离散型；若取到的值是一个区间，就是连续型

- 可以通过表格或者直方图来描述离散型随机变量；不仅给定了随机变量的取值，也给出了发生的概率，即一个完整的分布列

- 设Z为离散型随机变量，$P(Z=a_i) = p_i, i=1,2,\ldots$

| Z   | a1  | a2  | ... | an  | ... |
| --- | --- | --- | --- | --- | --- |
| P   | p1  | p2  | ... | pn  | ... |

$(1) p_i > 0, i=1,2,...$

$(2) \sum p_i = 1$

- 随机变量可以分为离散型随机变量、连续型随机变量、既不是离散型也不是连续型随机变量

#### 伯努利模型

- 重复独立试验：（1）随机事件彼此相互独立 （2）事件发生的概率p不变

- 伯努利模型：随机事件只有两个结果. $P(A) = p, P(\overline A) = 1-p=q, p >0, q>0, p+q =1 $

- 两点分布(伯努利分布)

| Z   | 1   | 0     |
| --- | --- | ----- |
| P   | p   | q=1-p |

#### 二项分布(n重伯努利试验)

- 做n次试验，每次试验发生的概率为p，那么A出现k次的概率记为 B(k;n, p). $P(B_k) = C_n^k p^k (1-p)^{n-k}, k=1,2,...,n$

| Z   | 0             | 1                 | ... | k                 | ... | n             |
| --- | ------------- | ----------------- | --- | ----------------- | --- | ------------- |
| P   | $C_n^0p^0q^n$ | $C_n^1p^1q^{n-1}$ | ... | $C_n^kp^kq^{n-k}$ | ... | $C_n^np^nq^0$ |

实质是满足二项展开: $1 = (p+q)^n = \sum_{k=1}^n C_n^kp^kq^{n-k}$

- 中心项: 使B(k;n,p)取最大值的项b(m;n,p)叫做中心项，m叫做最可能成功的次数

- 问题：（1）计算困难 （2）解决方法：中心极限定理； 泊松分布

#### Poisson 分布

- 历史
  
  > 1837年法国Poisson，主要目的是做为二项分布的近似
  > 
  > 二项分布和两个参数有关，而poisson只和一个参数 $\lambda$ 有关
  > 
  > 服从Poisson分布的现象: 电信台的呼叫、公交车站等待乘客的数量、物理学中释放的粒子落在某个区域的数目

- 用于构造其他分布的基本的分布，派生出更多的分布

- 定义

| Z   | 0   | 1   | ... | k                                       | ... |
| --- | --- | --- | --- | --------------------------------------- | --- |
| P   |     |     |     | $\frac {\lambda ^k} {k!} e^{- \lambda}$ |     |

$\sum _{k=0}^{\infty} \frac {\lambda ^k} {k!} e^{- \lambda} = 1, \lambda > 0$

$e^x = \sum_{k=0}^{\infty} \frac {x ^k} {k!} = 1$

- 定理
  
  > 在伯努利试验中，以$P_n$ 表示事件A出现的概率(Pn可能和n有关系)，若 $nP_n = \lambda, n -> \infty ==> b(k;n,p) = \frac {\lambda ^k} {k!} e^{- \lambda}$. (n很大，p很小，$\lambda = np$ 大小适中)

#### 分布函数

- 含义
  
  > 离散型随机变量可以通过二维的表格来表达分布律
  > 
  > 非离散型随机随机变量：（1）不能一个点一个点把分布罗列出来 （2）连续型的随机变量在一个点处的概率为0 （3）讨论一个区间范围内的概率(分布函数可实现)
  > 
  > 分布函数：设Z是一个随机变量，x是任意实数，$F(x)= P(Z \leq x) $ 称为Z的分布函数，这是一种累积的概率。
  > 
  > $P\{x_1 < Z \leq x_2\} = P(Z \leq x_2) - P( Z \leq x_1)$
  > 
  > 分布函数的间断点至多可数
  > 
  > 任何随机变量都有分布函数
  > 
  > 分布函数是一个右连续函数

- 优点
  
  > （1）分布函数完整的描述了区间的统计规律性。用数学的方式抽象的从整体上一般性的进行讨论
  > 
  > （2）可以把数学分析的方法用于概率和数理统计上来(<font color=red>微积分</font>)

- 性质
  
  > （1）F(x)单调递增，即对x1 < x2, F(x1) < F(x2)
  > 
  > （2）$0 \leq F(x) \leq 1$
  >  $F(- \infty) = \lim_{x->- \infty} F(x) = 0$
  >  $F(+ \infty) = \lim_{x->+ \infty} F(x) = 1$
  > （3）$F(x+0) = F(x)$ 右连续
  > $F(x-0) = F(x) 左连续$

- ex 1
  
  > 将一枚硬币连续抛两次，Z表示正面出现的次数，求Z的分布函数以及 $P \lbrace 0 < z \leq 1 \rbrace, P\{ 1 \leq z \leq 2\}$
  > 分析：（1）分布列
  > 
  > | Z   | 0   | 1   | 2   |
  > | --- | --- | --- | --- |
  > | P   | 1/4 | 1/2 | 1/4 |
  > 
  > （2）分布函数
  > 
  > $F(x) = \left \{ \begin{array}{l}
  > 0 & x < 0\\
  > 1/4 & 0 \leq x < 1 \\
  > 3/4 & 1 \leq x < 2\\
  > 1 & x \geq 2
  > \end{array} \right.$
  > 
  > （3）$\begin{array}{l}
  > P\{ 0 < z \le 1\}  = F(1) - F(0) = 3/4 - 1/4 = 1/2\\
  > P\{ 1 \le z \le 2\}  = P\{ z = 1\}  + P\{ 1 < z \le 2\} \\
  >  = 1/2 + F(2) - F(1)\\
  >  = 1/2 + 1 - 3/4 = 3/4
  > \end{array}$

- ex 2
  
  > 某脉冲信号在时间区间(0,T)内随机出现，出现的时刻记为t，事件$\{t_1 < t \le t_2 \}$ 的概率为 $P\{t_1 < t \le t_2\} = \frac {t_2-t_1} {T} , t_1,t_2 \subset (0,T)$, 求Z(t)=t的分布函数
  > 
  > 分析: $F(x) = \left \{ \begin{array}{l}
  > 0 & t < 0 \\
  > \frac {t} {T} & 0 \le t < t \\
  > 1 & t \ge T
  > \end{array} \right.$

### 连续型随机变量

#### 定义

> 设随机变量Z的分布函数为F(x),如果存在<font color=red>非负函数</font>f(x), 使得$F(x) = \int_{-\infty}^x f(t)dt$ ,则称Z为连续型随机变量, f(x)成为Z的概率密度函数
> 
> 约定：提到概率分布时，离散型<->分布律; 连续型 <->概率密度
> 
> <font color=red>概率密度的含义：描述了随机变量取不同值可能性的大小</font>

#### 性质

- $f(x) \ge 0, -\infty < x < +\infty$

- $\int_{-\infty}^{+\infty}f(x) dx = 1$

- 对$\forall x_1 \le x_2, P\{x_1 < z \le x_2\} = F(x_2) - F(x_1) = \int_{x_1}^{x_2}f(x)dx$

- 改变f(x)个别点处的函数值不影响F(x) ==> 连续型随机变量的分布函数是连续的

- 对 $\forall x, P\{Z=x\} = \int_{x}^{x}f(x)dx = 0$

- 若f(x)在x点连续，则 $F'(X) = f(x)$

#### 均匀分布

- 概率密度函数

$p(x) = \left \{ \begin{array}{l}
\frac {1} {b-a} &\text {if } a < x< b \\
0 &\text {if } others
\end{array} \right.$

记 $Z \sim \bigcup(a,b)$

- 分布函数

$F(x) = \int_{-\infty}^x = \left \{ \begin{array}{l}
\int_{-\infty}^xf(t)dt = 0 & \text {if } x < a \\
\int_{-\infty}^{a} f(t)dt + \int_{a}^{x} \frac {1} {b-a} dt = \frac {x-a} {b-a} & \text {if } a \le x < b \\
\int_{-\infty}^{a} f(t)dt + \int_{a}^{b} \frac {1} {b-1}dt + \int_{b}^{x}f(t)dt = 0 + 1 + 0 = 1 & \text {if } x \ge b
\end{array} \right.$

#### 指数分布

- 概率密度函数

$p(x) = \left\{ \begin{array}{l}
\lambda {e^{ - \lambda x}}dx &\text {if } x > 0 \\
0 & \text {if } x <  = 0
\end{array} \right.$

记Z服从参数$\lambda (\lambda > 0)$ 的指数分布

- 分布函数

$F(x) = \left\{ \begin{array}{l}
\int_{-\infty}^a f(t)dt = 0 & \text {if } x < 0 \\
\int_{-\infty}^0 f(t)dt + \int_{0}^{x} \lambda e^{-\lambda t}dt =0 + -e^{-\lambda t} |_{0}^{x} = 1-e^{\lambda x} & \text {if } x \ge 0
\end{array} \right.$

- 性质(无记忆性)

对$\begin{array}{l}
\forall s,t > 0\\
P\{ Z > s + t|Z > s\} \\
 = \frac{{P\{ Z > s + t \cap Z > s\} }}{{P\{ Z > s\} }}\\
 = \frac{{P\{ Z > s + t\} }}{{P\{ Z > s\} }}\\
 = \frac{{1 - P\{ Z \le s + t\} }}{{1 - P\{ Z \le s\} }}\\
 = \frac{{1 - F(s + t)}}{{1 - F(s)}}\\
 = \frac{{1 - (1 - {e^{ - \lambda (s + t)}})}}{{1 - (1 - {e^{ - \lambda (s)}})}}\\
 = {e^{ - \lambda t}} = P\{ Z > t\} 
\end{array}$

（1）s+t发生的概率和s发生的概率没有关系

（2）<font color=red>指数分布式是唯一一个连续型无记忆分布的概率分布</font>

- 使用
  
  > 寿命分布
  > 
  > 可靠性理论

#### 正太分布

- 概率密度

$p(x) = \frac{1}{{\sqrt {2\pi } \sigma }}{e^{ - \frac{{{{(x - u)}^2}}}{{2{\sigma ^2}}}}} , -\infty < x < +\infty$

其中 $\sigma >0$，称为Z服从参数为 $u, \sigma$ 的正太分布，又称为高斯分布，记为 $Z \sim N(u, \sigma^2)$

- 性质
  
  > （1）关于x=u对称，并且取到最大值$f(u)=\frac {1} {\sqrt{2\pi} \sigma}$，即为x=u附近可能会取到概率只最大
  > 
  > （2）拐点 $x= u\pm \sigma$
  > 
  > （3）分布函数 $F(x) = \int_{-\infty}^x \frac {1} {2\pi\sigma} e^{- \frac {(t-u)^2} {2 \sigma^2}} dt$
  > 
  > （4）标准正太分布：$u=0, \sigma=1$
  > 
  > 概率密度：$\varphi (x) = \frac{1}{{\sqrt {2\pi } }}{e^{ - \frac{{{x^2}}}{2}}}$
  > 
  > 分布函数：$\Phi(x) = \int_{-\infty}^x \frac {1} {\sqrt{2\pi}} e^{- \frac {x^2} {2}}dx$
  > 
  > 对称性：$\Phi(-x) = 1- \Phi(x)$
  > 
  > $\sigma$ 法则：$P\{u-\sigma < Z < u+ \sigma\} = P\{-1 < \frac {Z-u} {\sigma} < 1\} = \Phi(1) - \Phi(-1)=2\Phi(1) -1=68.26\%$
  > 
  > $P{u-2\sigma < Z < u+ 2\sigma} = P{-1 < \frac {Z-u} {2\sigma} < 1} = \Phi(2) - \Phi(-2)=2\Phi(2) -1=95.94\%$
  > $P{u-3\sigma < Z < u+ 3\sigma} = P{-1 < \frac {Z-u} {3\sigma} < 1} = \Phi(3) - \Phi(-3)=2\Phi(3) -1=99.74\%$
  > 
  > （5）正太分布和标准正太分布转换
  > 
  > $\begin{array}{l}
  > let \quad X \sim N(u,{\sigma ^2}),Z = \frac{{X - u}}{\sigma }\\
  > P\{ Z \le x\}  = P\{ \frac{{X - u}}{\sigma } \le x\} \\
  >  = P\{ X \le \sigma x + u\} \\
  >  = \frac{1}{{\sqrt {2\pi } \sigma }}\int_{ - \infty }^{\sigma x + u} {{e^{ - \frac{{{{(t - u)}^2}}}{{2{\sigma ^2}}}}}} dt\\
  > let \quad \frac{{t - u}}{\sigma } = s,dt = \sigma ds\\
  >  = \frac{1}{{\sqrt {2\pi } }}\int_{ - \infty }^x {{e^{ - \frac{{{{(s)}^2}}}{2}}}} ds = \Phi(x)
  > \end{array}$

## 随机变量的函数的分布

- 概率密度变换公式

设Z的概率密度为$p(x), x \in (a,b), y=f(x)$ 在(a,b)严格单调连续，且存在唯一的反函数x=h(y), $y\in (\alpha, \beta), h'(y)$ 连续，则y=f(z)也是连续型随机变量，其密度函数为：

$p(y) = p(h(y))|h'(y)|, y\in(\alpha, \beta)$

- ex1 离散型
  
  > | Z   | -2  | 0   | 1   | 2   |
  > | --- | --- | --- | --- | --- |
  > | P   | 0.1 | 0.2 | 0.3 | 0.4 |
  > 
  > 求Y=f(Z)=z^2+1的分布
  > 
  > | Y   | 5   | 0   | 2   | 5   |
  > | --- | --- | --- | --- | --- |
  > | P   | 0.1 | 0.2 | 0.3 | 0.4 |
  > 
  > 因此，
  > 
  > | Y   | 0   | 2   | 5   |
  > | --- | --- | --- | --- |
  > | P   | 0.2 | 0.3 | 0.5 |

- ex2 连续型
  
  > 设$\xi$ 的的概率密度为 $f(x) = \left \{\begin{array}{l} 2x & \text {if 0 < x < 1} \\
  > 0 & \text {if } others \end{array} \right.$
  > 
  > 求 $\eta = f(\xi) = 3\xi +1$的分布函数和概率密度
  > 
  > 分析：（1）求 $\eta$ 的分布函数 G(y)
  > 
  > $\begin{array}{l}
  > G(y) = P\{ \eta  \le y\}  = P\{ 3\xi  + 1 \le y\}  = P\{ \xi  \le \frac{{y - 1}}{3}\} \\
  >  = \left\{ \begin{array}{l}
  > 0 & \text {if } x \le 0\\
  > \int_0^{\frac{{y - 1}}{3}} {2xdx = \frac{{{{(y - 1)}^2}}}{3}  \quad\quad \text {if }1 < y < 4(0 < \frac{{y - 1}}{3} < 1)} \\
  > 1 & {if } y \ge 4(\frac{{y - 1}}{3} \ge 1)
  > \end{array} \right.
  > \end{array}$
  > 
  > （2）求密度函数
  > 
  > $g(y) = G'(y) = \left \{ \begin{array}{l} \frac {2} {9} (y-1) & {if } \quad 1 < y <4 \\
  > 0 & {if } \quad others
  >  \end{array} \right.$

# 二维随机变量及其分布

## 二维随机变量的概念

### 研究的主要问题

- 整体的分布和性质

- 分量之间的关系

- 分量和整体之间的关系

### 二维随机变量的分布函数

- 含义

设(x,y)是二维平面上的点，对 $\forall x,y$, 称二元函数 $F(x) = P \{X \le x, Y \le y \}$ (逗号表示交集)为(X,Y)的联合分布函数

- 性质

（1）单调性(多个变量不存在单调性，只是对单个变量而言)：F(x,y)对x(或者y)是单调非递减的

（2）概率

$0 \le F(x,y) \le 1$

$F(-\infty, y) = 0$

$F(x, -\infty) = 0$

$F(-\infty, \infty) = 0$

$F(+\infty, +\infty) = 1$

（3）连续型: 对x或者y都是右连续的

$F(x+0, y) = F(x,y)$

$F(X, y+0) = F(x,y)$

（4）矩形区域概率

$\begin{array}{l}
P\{x_1 < X \le x_2, y_1 < Y \le y_2 \} \\
= F(x_2, y_2) - F(x_1, y_2) - F(x_2, y_1) + F(x_1, y_1)
\end{array}$

### 二维离散型

- 含义

(X,Y)的取值为$(x_i,y_j), i,j=1,2,3,\ldots$ 若为有限多对或者可列无限多对(自然数范围内)

- 联合分布律--> 二维的表格表示

（1）$P \{X=x_i, Y=y_i \} = P_{ij} > 0$

（2）$\sum_{i=1}^n\sum_{j=1}^n p(x_i,y_j) = 1$

### 二维连续型

- 含义

设(X,Y)的联合分布函数为F(x,y), 如果存在非负函数f(x,y), 对

 $\forall x,y 有 F(x,y) = \sum_{-\infty}^x\sum_{-\infty}^y f(x,y)dxdy$

则称(X,Y)为二维连续型随机变量，f(x,y)成为二维联合概率密度函数

- 性质

（1）$p(x,y) \ge 0$ 

（2）$\int_{-\infty}^{+\infty} \int_{-\infty}^{+\infty}f(x,y)dxdy = 1$

（3）点(X,Y)落在某平面区域D上的概率为

$P\{(X,Y) \in D\} = \iint_Df(x,y)dxdy$

（4）若f(x,y)在点(x,y)连续，则

$\frac {\partial^2F(x,y)} {\partial x\partial y} = f(x,y)$

## 边缘分布

### 边缘分布函数

令(X,Y)的联合分布函数为F(x,y), 那么X的边缘分布函数为

$F_X(x) = F(x, +\infty) = P\{X \le x \} = P\{X \le x, Y < +\infty \}$

$F_Y(y) = F(+\infty, y) = P \{ Y \le y\} = P \{X < +\infty, Y < y\}$

<font color=red>超几何分布的边缘分布未必是超几何分布</font>

<font color=red>二项分布的边缘分布是二项分布</font>

<font color=red>正态分布的边缘分布仍是正态分布</font>

<font color=red>注意：联合概率分布决定了边缘分布，但反之不一定 </font>   例如

> 袋子中有2只白球，3只黑球，现在一只一只摸出
> 
> $X= \left \{ \begin{array}{l} 0 & 第一次黑球 \\
> 1 & 第一次白球 \end{array} \right.$
> 
> $Y= \left \{ \begin{array}{l} 0 & 第二次黑球 \\
> 1 & 第二次白球 \end{array} \right.$
> 
> （1）有放回
> 
> | Y\X           | 0          | 1        | $p_{\cdot j}$ |
> | ------------- | ---------- | -------- | ------------- |
> | 0             | $3/5* 3/5$ | 2/5 *3/5 | 3/5           |
> | 1             | $3/5*2/5$  | 2/5*2/5  | 2/5           |
> | $p_{i \cdot}$ | 3/5        | 2/5      | 1             |
> 
> （2）无放回
> 
> | Y\X           | 0          | 1        | $p_{\cdot j}$ |
> | ------------- | ---------- | -------- | ------------- |
> | 0             | $3/5* 2/4$ | 3/5 *2/4 | 3/5           |
> | 1             | $3/5*2/4$  | 2/5*1/4  | 2/5           |
> | $p_{i \cdot}$ | 3/5        | 2/5      | 1             |

### 离散型边缘分布

|              | $a_1$       | ... | $a_i$      | ... | $p_{\cdot j}$ |
| ------------ | ----------- | --- | ---------- | --- | ------------- |
| $b_1$        | $p_{11}$    |     | $p_{i1}$   |     | $p \cdot 1$   |
| ...          |             |     |            |     |               |
| $b_j$        | $p_{1j}$    |     | $p_{ij}$   |     | $p \cdot j$   |
| ...          |             |     |            |     |               |
| $p_{i\cdot}$ | $p_1 \cdot$ |     | $p_i\cdot$ |     | 1             |

### 连续型边缘分布

设(X,Y)的联合概率密度函数为 f(x,y),那么X的边缘分布函数为

$F_X(x)= F(x, +\infty) = P(X \le x) = \int_{-\infty}^x(\int_{-\infty} ^{+\infty} f(x,y)dy)dx$

X 的边缘概率密度函数为

$f_x(x) = F_X'(x) = \int_{-\infty}^{+\infty}f(x,y)dy$

同理：

$F_Y(y)= F(+\infty, y) = P(Y \le y) = \int_{-\infty}^y(\int_{-\infty} ^{+\infty} f(x,y)dx)dy$

$f_y(y) = F_Y'(y) = \int_{-\infty}^{+\infty}f(x,y)dx$

## 三种常见的二维分布

### 二维两点分布

| Y\X | 0   | 1   |     |
| --- | --- | --- | --- |
| 0   | 1-p | 0   | 1-p |
| 1   | 0   | p   | p   |
|     | 1-p | p   |     |

(X,Y)的联合分布函数为

（1）当 $ x< 0 || y <0, F(x,y) = P\{ X \le x, Y \le y \} = 0 $

（2）当$0 \le x < 1, y \ge 0$ 时，F(x,y) = 1-p

（3）当$x \ge0, 0 \le y < 1$ 时， F(x,y) = 1-p

（4）当$x \ge 1, y \ge 1$时， F(x,y) = 1

### 二维均匀分布

- 定义

密度函数为(区域面积分之一)

$f(x,y) = \left\{ \begin{array}{l}
\frac{1}{{{S_D}}} & (x,y) \in D\\
0 & others
\end{array} \right. $

- ex1

在[-1, 2]上任取两点，坐标分别为(X,Y)，求$P\{X+Y>1, XY < 1\}$

分析：（1）画出二维坐标图和X,Y代表的区域

（2）$P = \frac {3 * 1/2 + 2 \int_1^2 \frac {1} {x} dx} {9}$

### 二维正态分布

- 密度函数

$\begin{array}{l}
\varphi (x,y) = \frac{1}{{2\pi {\sigma _1}{\sigma _2}\sqrt {1 - {\rho ^2}} }}\exp \left\{ { - \frac{1}{{2(1 - {\rho ^2})}}(\frac{{{{(x - {u_1})}^2}}}{{{\sigma _1}^2}} - 2\rho \frac{{(x - {u_1})(y - {u_2})}}{{{\sigma _1}{\sigma _2}}} + \frac{{{{(y - {u_2})}^2}}}{{{\sigma _2}^2}})} \right\}\\
{\sigma _1} > 0,{\sigma _2} > 0, - 1 < \rho  < 1\\
(X,Y) \sim ({u_1},{\sigma _1};{u_2},{\sigma _2};\rho )
\end{array}$

- 二维正态分布可以推出边缘分布概率密度函数符合正态分布，反之不能确定

## 条件分布

在某个分量发生的情况下，另外一个分量发生的情况

- 二维离散型条件分布
  
  > 设(X,Y)是二维离散型的分布列： $P\{X=a_i,Y=b_j\} = p_{ij}, \quad i,j=1,2,...$
  > 
  > 对$P\{Y=b_j\} > 0$， X的条件概率分布为
  > 
  > $P\{X=a_i | Y=b_j\} = \frac {P\{X=a_i,Y=b_j\}} {P\{Y=b_j\}} = \frac {p_{ij}} {p_{\cdot j}}, i,j=1,2,...$

- 二维连续型条件分布
  
  > 设(X,Y)是二维连续型，联合概率密度函数为p(x,y) 注意: $P\{X=x\}=0， P\{Y=y\} = 0$
  > 
  > 对固定的y，若$P_Y(y) > 0$
  > 
  > $P_{X|Y}(x|y) = \frac {p(x,y)} {p(y)}$ 为在Y=y的条件下的条件密度函数

- ex
  
  > 设(X,Y)的联合密度函数为 $p(x,y) = \left\{ \begin{array}{l}
  > \frac{1}{y}{e^{ - \frac{x}{y}}}{e^{ - y}} & 0 < x,y <  + \infty \\
  > 0 & others
  > \end{array} \right.$ 
  > 求 $P\{X >1 | Y=y \}$
  > 
  > 分析：在$Y=y >0$ 时，X的条件密度函数为
  
  > $\begin{array}{l}
  > p(x|y) = \frac{{p(x,y)}}{{p(y)}}\\
  >  = \frac{{\frac{1}{y}{e^{ - \frac{x}{3}}}{e^{ - y}}}}{{\frac{1}{y}{e^{ - y}}\int_0^{ + \infty } {{e^{ - \frac{x}{y}}}} }} = \frac{{{e^{ - \frac{x}{y}}}}}{y} \quad x > 0\\
  > \therefore y > 0\\
  > P\{ X > 1|Y = y\}  = \int_1^{ + \infty } {\frac{1}{y}{e^{ - \frac{x}{y}}}dx = {e^{ - \frac{1}{y}}}} 
  > \end{array}$

## 独立性(分量之间的独立性)

- 定义
  
  > 设有(X,Y)，其中F(x,y) 是其联合分布函数，$F_X(x), F_Y(y)$是边际分布函数，对所有的X,Y 有 $F(x,y) = F_X(x) *F_Y(y)$
  > 
  > 即$P\{X \le x, Y \le y \} = P\{X \le x \} P\{Y \le y \}$
  > 
  > 则X与Y相互独立

- 离散型
  
  > $P \{X=a_i,Y=b_j \} = P\{X=a_i\} P\{Y=b_j\}$
  > 
  > 即 $p_{ij} = p_{i\cdot} p_{\cdot j}$

- 连续型
  
  > 独立性 <==> $P(x,y) = P_X(x)P_Y(y)$

- ex
  
  > 设X,Y独立同分布，$p(x) = \left \{ \begin{array}{l} 2x & 0 \le x \le 1 \\
  > 0 & others \end{array} \right.$
  > 
  > 求$P\{ X + Y \le 1\} $
  > 
  > 分析：（1）因为独立，所以联合密度函数为
  > 
  > $p(x,y) = p(x)p(y) = \left \{ \begin{array}{l} 4xy & 0 \le, x,y \le 1 \\
  > 0 & others \end{array} \right.$
  > 
  > （2）$\begin{array}{l} P\{X+Y \le 1\} =  \iint_{x+y \le 1}p(x,y)dxdy \\
  > = \int_0^1\int_0^{1-x}4xydxdy \\ 
  > = 1/6 \end{array}$

- 性质
  
  > （1）X与Y独立，那么f(x)与g(y)也相互独立
  > 
  > （2）常数C与任一随机变量独立
  > 
  > （3）若联合密度函数p(x,y)可以分离成$p(x,y) = g_1(x) g_2(y)$
  > 
  > 且g1(x) 的非零区域与y无关；g2(y)的非零区域与x无关，则X与Y相互独立
  > 
  > （4）可推导到多维 

## 两个随机变量的函数分布

- ex1--离散型
  
  > 设X，Y独立，且$X \sim P(\lambda_1), Y \sim P(\lambda_2)$ 的泊松分布，求X+Y的分布律
  > 
  > 分析：$\begin{array}{l} P\{X+Y=m\} = P\{X=0,Y=m\} + P\{X=1 ,Y=m-1\} + \ldots + P\{X=m, Y=0 \} \\
  > \sum_{k=0}^mP\{X=k, Y=m-k\} \\
  > \sum_{k=0}^mP\{X=k\}P\{Y=m-k\} \\
  > \sum_{k=0}^m \frac {\lambda_1^k} {k!} e^{-\lambda_1} \frac {\lambda_2^{m-k}} {(m-k)!} e^{-\lambda_2} \\
  > \frac {e^{-\lambda_1 - \lambda_2}} {m!} \sum_{k=0}^m \frac {m!} {k!(m-k)!} \lambda_1^k \lambda_2^{m-k} \\
  > \frac {(\lambda_1 + \lambda_2)^m} {m!} e^{-\lambda_1 - \lambda_2} , m=1,2,3,\ldots
  > \end{array}$
  > 即 $(X+Y) \sim P(\lambda_1 + \lambda_2)$
  > 
  > ==> 分布的可加性，（1）两个独立的泊松分布的和，依然是一个柏松分布，而且参数对应相加, （2） <font color=red>正太分布也具有可加性</font>
  > 
  > 若X，Y独立，$X \sim N(u_1, \sigma_1^2), Y \sim N(u_2, \sigma_2^2)$ 
  > 
  > 那么， $(X+Y) \sim N(u_1+u_2, \sigma_1^2+\sigma_2^2)$
  > 
  > （3）二项分布：若X，Y独立，$X \sim B(n_1, p), Y \sim B(n_2, p)$ 那么 (X+Y) \sim B(n_1+n_2, p)

- ex2 -- 最大值、最小值分布
  
  > 设X，Y独立，分布函数分为为 $F_X(x), F_Y(y)$ 求 $Z_1 = max(X,Y), Z_x=min(X,Y)$的分布函数
  > 
  > 分析：$\begin{array}{l} F_{Z_1}(z) = P\{Z_1 \le z \} = P \{ max(X,Y) \le z \} \\
  > = P\{X \le z\} P\{ Y \le z\} = F_X(x) F_Y(y) \\
  > P\{Z_2 \le z \} = P \{ min(X,Y) \le z \} \\
  > = 1 - P\{ min(X,Y) > z \} = 1 - P \{ X > z, Y > z \} \\
  > = 1 - P \{ X > z \} P \{ Y > z \} \\
  > = 1 - [1 - P \{ X \le z \}] [1 - P \{ Y \le z \}] \\
  > = 1 - [1 - F_X(x)][1 - F_Y(y)]
  > \end{array}$

- ex3 -- 连续型
  
  > 设X，Y的联合密度函数为p(x,y),求Z= X+Y的分布函数
  > 
  > 分析：$\begin{array}{l}
  > {F_Z}(z) = P\{ Z \le z\}  = P\{ X + Y \le z\} \\
  >  = \int_{ - \infty }^{ + \infty } {(\int_{ - \infty }^{z - y} {p(x,y} )dx)dy} 
  > \end{array}$

# 随机变量的数字特征

研究目的：即使给出某个随机变量的完整分布，由于分布的复杂性，通常不能很快的看出这个分布的形态，此时需要一个更加简单、明了的方法来方便的判断、解决这个分布的相关问题，而随机变量的数字特征就是为来解决这个问题。

## 数学期望

反应数据的集中程度

### 定义

- 离散型
  
  > | X   | $a_1$ | ... | $a_2$ | ... |
  > | --- | ----- | --- | ----- | --- |
  > | P   | $p_1$ | ... | $p_2$ | ... |
  > 
  > $\frac {p_1a_1+p_2a_2+...+p_na_n} {p_1+p_2+...+p_n} = \sum_{i=1}^np_ia_i$
  > 
  > $E(X) = \sum_{i=1}^{+\infty} a_ip_i$ 为X的数学期望(加权平均数)，其中 $\sum_{i=1}^{+\infty}$ 为绝对收敛。 

- 连续型
  
  > 设随机变量X的概率密度函数为p(x),那么期望为 $E(X) = \sum_{-\infty} ^ {+ \infty} xp(x)dx$
  > 
  > 其中，$\sum_{-\infty}^{+\infty}|xp(x)|dx$  收敛

- 绝对收敛
  
  > 设有级数$\sum u_n$
  > 
  > 若$\sum|u_n|$ 收敛，则称 $\sum u_n$ 绝对收敛。（无限次数加法满足交换律）
  > 
  > 若$\sum u_n$ 收敛，$\sum |u_n|$发散，则称 $\sum u_n$ 条件收敛。（无限次数加法不满足交换律）
  > 
  > Riemann TH: 无限级数的加法，绝对收敛的级数可以任意交换次序。
  > 
  > 随机实验要求绝对收敛的原因：随机实验的结果是任意次序的，理论上任意次序的相加，其结果也是一样的。

### 三种常见的离散型随机变量的期望

- 两点分布
  
  > | X   | 1   | 0   |
  > | --- | --- | --- |
  > | P   | p   | 1-p |
  > 
  > E(X) = 1*p + 0 *(1-p) = p

- 二项分布
  （1）利用定义推导
  
  > $\begin{array}{l}
  > X \sim B(n,p) \\
  > E(X) = \sum_{k=0}^n k C_n^k p^k (1-p)^{n-k} \\
  > = \sum_{k=1}^n k C_n^k p^k (1-p)^{n-k} \\
  > = \sum_{k=1}^n k \frac {n!} {k! (n-k)!} p^k (1-p)^{n-k} \\
  > = \sum_{k=1}^n \frac {n!} {(k-1)! (n-k)!} p^k (1-p)^{n-k} \\
  > = np \sum_{k=1}^n \frac {(n-1)!} {(k-1)! (n-1-(k-1))!} p^{k-1} (1-p)^{n-k} \\
  > = np \sum_{i=0}^{n-1} \frac {(n-1)!} {i! (n-1-i!} p^{i} (1-p)^{n-1-i} \\
  > = np(p+1-p)^{n-1} = np
  > \end{array}$
  
  （2）利用性质推导
  
  > $\begin{array}{l}
  > {X_i} = \left\{ \begin{array}{l}
  > 1 & 第i次A事件发生 \\
  > 0 & 第i次A事件发生
  > \end{array} \right.\\
  > X = {X_1} + {X_2} +  \cdots  + {X_n}\\
  > E({X_i}) = p\\
  > \therefore E(X) = E({X_1} + {X_2} +  \cdots  + {X_n})\\
  >  = E({X_1}) + E({X_2}) +  \cdots  + E({X_n})\\
  >  = np
  > \end{array}$ 

- 柏松分布
  
  > $\begin{array}{l}
  > X \sim P(\lambda) \\
  > E(X) = \sum_{k=0}^{+\infty} k \frac {\lambda ^k} {k!} e^{-\lambda} \\
  > = \sum_{k=1}^{+\infty} \frac {\lambda ^k} {(k-1)!} e^{-\lambda} \\
  > = \lambda \sum_{k=1}^{+\infty} \frac {\lambda ^{k-1}} {(k-1)!} e^{-\lambda} \\
  > = \lambda (e^{\lambda}) e^{-\lambda} \\
  > = \lambda
  > \end{array}$

### 三种常见的连续型随机变量的期望

- 均匀分布
  
  > $\begin{array}{l}
  > X \sim \bigcup [a, b] \\
  > E(X) = \int_{-\infty}^{+\infty} xp(x)dx  \\
  > = \int_a^b \frac {x} {b-a} dx \\
  > = \frac {1} {b-a} \frac {1} {2} x^2 \mid_a^b \\
  > = \frac {a+b} {2}  
  > \end{array}$

- 指数分布
  
  > $\begin{array}{l}
  > X \sim Exp(\lambda), \lambda > 0 \\
  > E(X) = \int_0^{+\infty} x \lambda e^{- \lambda x} \\
  > = - \int_0^{+\infty} x de^{-\lambda x} \\
  > = -xe^{-\lambda x} \mid_0^{+\infty} + \int_0^{+\infty} e^{-\lambda x}dx \\
  > = 0 - \frac {1} {\lambda} e^{-\lambda x} \mid_0^{+\infty} \\
  > = \frac {1} {\lambda}
  > \end{array}$

- 正太分布
  
  > $\begin{array}{l}
  > X \sim N(u, \sigma^2) \\
  > E(X) = \int_{-\infty} ^{+\infty} x \frac {1} {\sqrt{2\pi} \sigma} e^{-\frac {(x-u)^2} {2\sigma^2}} dx \\
  > let \quad t = \frac {x-u} {\sigma}, x = t\sigma +u, t \in (-\infty, +\infty) \\
  > = \int_{-\infty}^{+\infty} (t \sigma + u) \frac {1} {\sqrt {2 \pi} \sigma} e^{- \frac {t^2} {2}} d(\sigma t + u) \\
  > = \frac {1} {\sqrt{2\pi} \sigma} \int_{-\infty}^{+\infty} (t \sigma + u) e^{- \frac {t^2} {2}} * \sigma dt \\
  > = \frac {u} {\sqrt{2\pi}}  \int_{-\infty}^{+\infty} e^{- \frac {t^2} {2}} dt \\
  > = u
  > \end{array}$

### 随机变量函数的期望

设X的分布已知，Y=g(x)， g是连续函数，求 E(Y)

（1）离散

$\begin{array}{l} P \{X=a_i \} = p_i, i=1,2,... \\
则E(Y) = E(g(x)) = \sum_{i=1}^{\infty} g(a_i) p_i (绝对收敛)
\end{array}$

（2）连续
$\begin{array}{l} X, p(x)是其密度函数 \\
则E(Y) = E(g(x)) = \sum_{-\infty}^{+\infty} g(x) p(x)dx (绝对收敛)
\end{array}$

### 性质

- $E(C) = C$

- E(CX) = CE(X)

- 设两个随机变量X,Y $E(X \pm Y) = E(X) \pm E(Y)$

- 若X,Y 相互独立 E(XY) = E(X) E(Y)

## 方差

### 定义

- $D(X) = VAR(X) = E(X-E(X))^2$

- 考虑数据变异或者离散程度

- $\sigma(X) = \sqrt{D(X)}$ 标准差（均方差）<font color=red>为了和X保持相同的量纲</font>

- （1）离散型
  
  > | X   | $a_1$ | ... | $a_i$ | ... |
  > | --- | ----- | --- | ----- | --- |
  > | P   | $p_1$ | ... | $p_i$ | ... |
  > 
  > $D(X) = \sum_{k=1}^n (a_k - E(X))^2 p_k$
  
  （2）连续型
  
  > $D(X) = \int_{-\infty}^{+\infty} (x - E(x))^2 p(x) dx$

### 性质

- D(C) = 0

- $\begin{array}{l}
  D(X) = E{(X - E(X))^2}\\
   = E({X^2} - 2XE(X) + {(E(X))^2})\\
   = E({X^2}) - 2E(X)E(X) + {(E(X))^2}\\
   = E({X^2}) - {(E(X))^2}
  \end{array}$

- 对任意的常数a,b $D(aX+b) = a^2D(X)$

- $\begin{array}{l}
  D(X + Y) = E{(X + Y - E(X + Y))^2}\\
   = E{[(X + Y - E(X) - E(Y))]^2}\\
   = E{[(X - E(X)) + (Y - E(Y))]^2}\\
   = E[{(X - E(X))^2} + {(Y - E(Y))^2} - 2(X - E(X))(Y - E(Y))]\\
   = E{[X - E(X)]^2} + E{[Y - E(Y)]^2} - 2E[(X - E(X))(Y - E(Y))]\\
   = D(X) + D(Y) - 2E[(X - E(X))(Y - E(Y))]
  \end{array}$

- X,Y 相互独立时 $D(X \pm Y) = D(X) \pm D(Y)$  

### 三种常见的离散型的方差

- 两点分布
  
  > | $X^2$ | 1   | 0   |
  > | ----- | --- | --- |
  > | P     | p   | 1-p |
  
  > $\begin{array}{l}
  > E({X^2}) = 1 \times p + 0 \times (1 - p) = p\\
  > \therefore D(X) = E({X^2}) - {(E(X))^2}\\
  > = p - {p^2} = p(1 - p)
  > = \end{array}$

- 二项分布
  
  > $\begin{array}{l}
  > X \sim B(n,p) \end{array}$
  > 
  > ${X_i} = \left\{ \begin{array}{l}
  > 1 & 第i次A事件发生 \\
  > 0 & 第i次A事件发生
  > \end{array} \right. $
  > 
  > $\begin{array}{l}
  > X = {X_1} + {X_2} +  \cdots  + {X_n}\\
  > \therefore D(X) = D({X_1} + {X_2} +  \cdots  + {X_n})\\
  >  = D{X_1} + D{X_2} +  \cdots  + D{X_n}\\
  >  = npq
  > \end{array}$

- 柏松分布
  
  > $\begin{array}{l}
  > X \sim P(\lambda )\\
  > E({X^2}) = \sum\limits_{k = 0}^{ + \infty } {{k^2}\frac{{{\lambda ^k}}}{{k!}}{e^{ - \lambda }}} \\
  >  = \sum\limits_{k = 1}^{ + \infty } {\frac{{k{\lambda ^k}}}{{(k - 1)!}}{e^{ - \lambda }}} \\
  >  = \sum\limits_{k = 1}^{ + \infty } {\frac{{(k - 1 + 1){\lambda ^k}}}{{(k - 1)!}}{e^{ - \lambda }}} \\
  >  = {\lambda ^2}\sum\limits_{k = 2}^{ + \infty } {\frac{{{\lambda ^{k - 2}}}}{{(k - 2)!}}{e^{ - \lambda }}}  + \lambda \sum\limits_{k = 1}^{ + \infty } {\frac{{{\lambda ^{k - 1}}}}{{(k - 1)!}}{e^{ - \lambda }}} \\
  >  = {\lambda ^2}({e^\lambda }{e^{ - \lambda }}) + \lambda ({e^\lambda }{e^{ - \lambda }})\\
  >  = {\lambda ^2} + \lambda \\
  > \therefore D(X) = E({X^2}) - {[E(X)]^2}\\
  >  = {\lambda ^2} + \lambda  - {\lambda ^2}\\
  >  = \lambda  = E(X)
  > \end{array}$

### 三种常见的连续型的方差

- 均匀分布
  
  > $\begin{array}{l}
  > X \sim U[a,b] \\
  > E(X^2) = \int_a^b x^2 \frac {1} {b-a}dx \\
  > = \frac {1} {3(b-a)} x^3 \mid_a^b \\
  > = \frac {1} {3(a^2+ab+b^2)} \\
  > \therefore D(X) = E(X^2) - (E(X))^2 \\
  > = \frac {1} {3(a^2+ab+b^2)} - (\frac {a+b} {2})^2 \\
  > = \frac {(b-a)^2} {12}
  > \end{array}$

- 指数分布
  
  > $\begin{array}{l}
  > X \sim Exp(\lambda )\\
  > E({X^2}) = \int_0^{ + \infty } {{x^2}\lambda {e^{ - \lambda x}}} dx\\
  >  =  - \int_0^{ + \infty } {{x^2}} d{e^{ - \lambda x}}\\
  >  =  - {x^2}{e^{ - \lambda x}}{|_0}^{ + \infty } + 2\int_0^{ + \infty } x {e^{ - \lambda x}}dx\\
  >  = 0 + \frac{2}{\lambda }\int_0^{ + \infty } {\lambda x} {e^{ - \lambda x}}dx\\
  >  = \frac{2}{\lambda }*\frac{1}{\lambda } = \frac{2}{{{\lambda ^2}}}\\
  > \therefore D(X) = E({X^2}) - {[E(X)]^2}\\
  >  = \frac{2}{{{\lambda ^2}}} - \frac{1}{{{\lambda ^2}}} = \frac{1}{{{\lambda ^2}}}
  > \end{array}$

- 正太分布
  
  > $\begin{array}{l}
  > 设X的 E(X) = u, D(X)=\sigma^2 \ne 0 \\
  > let \quad Y=\frac {X-u} {\sigma} \\
  > E(Y) = E(\frac {X-u} {\sigma}) = \frac {1} {\sigma} [E(X) - E(u)] \\
  > \frac {1} {\sigma} (u - u) = 0 \\
  > D(Y) = D(\frac {X-u} {\sigma}) = \frac {1} {\sigma^2} D(X) = 1
  > \end{array}$
  
  > $\begin{array}{l}
  > X \sim N(0,1)\\
  > E({X^2}) = \int_{ - \infty }^{ + \infty } {{x^2}\frac{1}{{\sqrt {2\pi } }}} {e^{ - \frac{{{x^2}}}{2}}}dx\\
  >  = \frac{1}{{\sqrt {2\pi } }}\int_{ - \infty }^{ + \infty } {( - x)} d{e^{ - \frac{{{x^2}}}{2}}}\\
  >  = \frac{1}{{\sqrt {2\pi } }}[ - x{e^{ - \frac{{{x^2}}}{2}}}{|_{ - \infty }}^{ + \infty } + \int_{ - \infty }^{ + \infty } {} {e^{ - \frac{{{x^2}}}{2}}}dx]\\
  >  = \frac{1}{{\sqrt {2\pi } }}[0 + \int_{ - \infty }^{ + \infty } {} {e^{ - \frac{{{x^2}}}{2}}}dx] = 1\\
  > \therefore D(X) = E({X^2}) - {[E(X)]^2}\\
  >  = 1 - 0 = 1\\
  > \therefore Y \sim N(u,{\sigma ^2})\\
  > X = \frac{{Y - u}}{\sigma } \sim N(0,1)\\
  > Y = X\sigma  + u\\
  > E(Y) = E(X\sigma  + u) = \sigma E(X) + E(u)\\
  >  = 0 + u = u\\
  > D(Y) = D(X\sigma  + u) = {\sigma ^2}D(X) = {\sigma ^2}
  > \end{array}$

## 协方差、相关系数

对于X，Y两个随机变量，需要考虑三个方面：（1）除了可以单独考虑D(X),D(Y) （2）作为整体来考虑 （3）D(X),D(Y) 之间的关系

### 协方差

- 反应多维随机变量分散或者离异的程度。定义就是X与期望的偏差与Y与期望的偏差相乘，然后求一个平均的差，即$Cov(X,Y) = E[(X-E(X)) (Y-E(Y))]$

- 性质
  
  > （1）$Cov(X,Y) = Cov(Y,X)$
  > 
  > （2）$Cov(X,X) = D(X)$
  > 
  > （3）$Cov(X,Y) = E(XY) - E(X)E(Y)$
  > 
  > （4）X,Y相互独立，则$Cov(X,Y) = 0$ , 反之不一定成立
  > 
  > （5）$Cov(X_1+X_2, Y) = Cov(X_1,Y) + Cov(X_2, Y)$
  > 
  > （6）$Cov(aX,bY) = abCov(X,Y)$

- ex
  
  > 设X，Y的联合概率密度函数为
  > 
  >   $p(x,y) = \left\{ \begin{array}{l}
  > 2 & 0 \le x \le 1,0 \le y \le x\\
  > 0 & others
  > \end{array} \right.$
  > 
  > 求Cov(X,Y)
  > 
  > $\begin{array}{l}
  > E(X) = \iint\limits_D {xp(x,y)dxdy} \\
  >  = \int_0^1 {[\int_0^x {x*2dy} ]dx}  = 2/3 \\
  > E(Y) = \iint\limits_D {yp(x,y)dxdy} \\
  > = \int_0^1 {[\int_0^x {y*2dy} ]dx}  = 1/3 \\
  > E(XY) = \iint\limits_D {xyp(x,y)dxdy} \\
  > = \int_0^1 {[\int_0^x {xy*2dy} ]dx}  = 1/4 \\
  > \therefore Cov(X,Y) = E(XY) - E(X)E(Y) \\
  > = 1/4 - 2/3*1/3 = 1/36 \\ 
  > \end{array}$

### 相关系数

- 含义

> 上面的集中数字特征都是有单位的，期望的单位和原来的随机变量单位相同；方差的单位是原来随机变量单位的平方；协方差的单位是两个随机变量单位的乘积
> 消除单位的影响: $\rho_{XY} = \frac {Cov(X,Y)} {\sqrt{D(X)} \sqrt{D(Y)}}$
> 相关系数是: 标准尺度下的协方差 $X^*=\frac {X-E(X)} {D(X)}, y^* = \frac {Y-E(Y)} {D(Y)}, \rho_{XY} = Cov(X^*, Y^*)$

- 性质

> （1）若X,Y 相互独立，则$\rho_{XY} = 0$
> （2）<font color=red>相关系数是一个线性的相关系数，反应的是两个变量之间线性依赖的关系。</font>
> $\left| {{\rho _{XY}}} \right| \le 1$
> $\rho_{XY} = 1 \Leftrightarrow 存在a>0, b \in R, 使 Y=aX+b (完全正相关)$
> $\rho_{XY} = -1 \Leftrightarrow 存在a<0, b \in R, 使 Y=aX+b (完全负相关)$
> $\rho_{XY} = 0 X,Y不相关)$

### 实例

- ex1
  
  > 设$X \sim U(-\frac {1} {2}, \frac {1} {2} ), Y=cos(X), 求\rho_{XY}$
  > 分析：$\begin{array}{l}
  > E(X) = 0 \\
  > E(XY) = E(xcos(x)) = \int_{-1/2} ^{1/2} xcos(x) * 1 dx = 0 \\
  > Cov(X,Y)= E(XY) - E(X)E(Y) = 0 \\
  > \rho_{XY} = 0 => X与Y非线性相关
  > \end{array}$

- ex2
  
  > 投掷一枚硬币n 次，X表示正面出现次数，Y表示反面出现的次数，求 $\rho_{XY}$
  > 分析：X+Y=n
  > Y = -X +n
  > $\rho_{XY} = -1, 完全负相关关系$

- ex 3
  
  > 设(X,Y)服从平面上单位圆内的均匀分布，求$\rho_{XY}及X,Y的独立性$
  > $\begin{array}{l}
  > p(x,y) = \left\{ \begin{array}{l}
  > \frac{1}{\pi },{x^2} + {y^2} \le 1\\
  > 0,others
  > \end{array} \right.\\
  > p(x) = \int_{ - \infty }^{ + \infty } {p(x,y)dy = } \int_{ - \sqrt {1 - {x^2}} }^{ + \sqrt {1 - {x^2}} } {\frac{1}{\pi }dy = } \frac{2}{\pi }\sqrt {1 - {x^2}} ,( - 1 \le x \le 1)\\
  > p(y) = \int_{ - \infty }^{ + \infty } {p(x,y)dx = } \int_{ - \sqrt {1 - {y^2}} }^{ + \sqrt {1 - {y^2}} } {\frac{1}{\pi }dx = } \frac{2}{\pi }\sqrt {1 - {y^2}} ,( - 1 \le y \le 1)\\
  > E(X) = \int_{ - \infty }^{ + \infty } {xp(x)dx = } \int_{ - 1}^{ + 1} {x\frac{2}{\pi }\sqrt {1 - {x^2}} dx = } 0\\
  > E(Y) = \int_{ - \infty }^{ + \infty } {yp(y)dy = } \int_{ - 1}^{ + 1} {y\frac{2}{\pi }\sqrt {1 - {y^2}} dy = } 0\\
  > E(XY) = \int_{ - 1}^{ + 1} {(\int_{ - \sqrt {1 - {x^2}} }^{ + \sqrt {1 - {x^2}} } {\frac{1}{\pi }dy} )dx = } 0\\
  > Cov(X,Y) = E(XY) - E(X)E(Y) = 0\\
  > {\rho _{XY}} = 0, X,Y 不相关\\
  > p(x,y) \ne p(x)p(y) \Rightarrow X,Y 不独立
  > \end{array}$

- ex 4
  
  > 如果维随机变量服从维正态分布，那么它们两两独立等价于它们两两不相关

## 矩、协方差矩阵

- 协方差矩阵
  
  > 设有n维随机变量$(X_1,X_2,X_3, \ldots, X_n), C_{ij} = Cov(x_i, x_j), i,j=1,2,\ldots,n$
  > $C = \left[ \begin{array}{l}
  > {c_{11}} \quad {c_{12}} \quad \cdots \quad {c_{1n}}\\
  > {c_{21}} \quad {c_{22}} \quad \cdots \quad {c_{2n}}\\
  >  \vdots \quad \quad  \vdots \quad \quad  \cdots  \quad \vdots \\
  > {c_{n1}} \quad {c_{n2}} \quad \cdots \quad {c_{nn}}
  > \end{array} \right]$
  > 
  > 为n维随机变量

- 协方差矩阵性质
  
  > （1）对角线 $c{ij} = D(X_i), i=1,2,3,\cdots, n$
  > （2）$c_{ij} = c_{ji}, 即C=C^T => 对称矩阵$

- 矩
  
  > 若 $E(|X|^k) < +\infty$(小于 $+\infty$ 表示存在或者有限的，即有意义的期望值), 则称 $\alpha_k = E(X^k), k=1,2,\cdots$ 为k阶的原点矩。
  > 若$E(X)$存在，且 $E(|X-E(X)|^k < \infty$, 则称 $\beta_k = E((X - E(X))^k), k=1,2,\cdots$ k 阶中心距(含义: 随机变量的取值到期望值偏差的k次方的平均的度量).
  
  > 期望、方差、协方差、相关系数都是属于更一般意义的特征 -- 矩。
  > 期望E(X)是一阶的原点矩
  > 方差D(X)是二阶的中心距
  > 高阶矩存在，那么低阶矩肯定存在；反之未必

# 大数定律以及中心极限定理

## 两种收敛性概念

> 微积分种的收敛性，是依 "距离" 进行收敛性的判断; 而此处的收敛性是依 "概率" 进行收敛性的判断

### 依概率收敛

> 设 $X_1,X_2,\cdots, X_n, \cdots$ 是随机变量的序列，X是某一个随机变量(或者常数)， 对于 $\forall \epsilon > 0$, 若
> $\begin{array}{l}
> \mathop {\lim }\limits_{n \to \infty } P\{ |{X_n} - X| < \varepsilon \}  = 1 \\ 或
> \mathop {\lim }\limits_{n \to \infty } P\{ |{X_n} - X| \geqslant \varepsilon \}  = 0 \\ 
> \end{array}$, 则称随机序列 ${X_i}, i=1,2,3,...$依概率收敛于X，记做 ${X_n} \xrightarrow {P}X$

### 依分布收敛

> 设 $X_1,X_2,\cdots, X_n, \cdots$ 是随机变量的序列，X是某一个随机变量， $F_n(x)是X_n 的分布函数, i=1,2,3,...; F(x)是X的分布函数$
> 若在F(x)的连续点X处都有 $\mathop {\lim} \limits_{n \to \infty } F_n(x) = F(x)$, 则称 $X_i$依分布收敛于X，记作 $X_n \xrightarrow {L} X$ （这表明$\{X_n\}$ 以X的分布为极限分布）

## 切比雪夫不等式

> 估计概率、证明大数定律、统计推断等起到作用的不等式

- 定义

> 设随机变量X的期望为E(X)，D(X)都存在， 则对 $\forall \epsilon > 0$, 有
> $P\{ |X-E(X)| \ge \epsilon \} \le \frac {D(X)} {\epsilon^2}$ 或 
> $P\{ |X-E(X)| < \epsilon \} \ge 1 - \frac {D(X)} {\epsilon^2}$

> 证明:(以连续型随机变量为例，概率密度函数为p(x))
> $\begin{array}{l} 
> P \{ |X-E(X)| \ge \epsilon \} = \int \limits_{|X-E(X)| \ge \epsilon} p(x) dx \\
> \le \int \limits_{|X-E(X)| \ge \epsilon} \frac {|X-E(X)|^2} {\epsilon^2} p(x) dx \\
> \le \frac {1} {\epsilon^2} \int_{-\infty}^{+\infty} |X-E(X)|^2 p(x)dx \\
> = \frac {D(X)} {\epsilon^2}
> \end{array}$

- 具体含义

> 以E(X)为中心，$\epsilon$为半径的对称区间，随机变量发生的概率；或者说这个对称区间外部发生的概率.(这里是估计值)

- ex1

> 设X的分布未知，但 $E(X) = u, D(X) = \sigma^2$, 试估计 $P\{ |X-u| \ge 3\sigma \}$ 及 $P \{ |X-u|\} \le 4\sigma$
> 分析：$P\{ |X-u| \ge 3\sigma \} \le \frac {D(X)} {(3\sigma)^2} = \frac {1} {9}$
> $P\{ |X-u| < 4\sigma \} \ge 1 - \frac {D(X)} {(4\sigma)^2} = \frac {15} {16}$

- ex2

> 设 $\{ X_i\}$ 是独立同分布的随机变量序列，有公共的期望u和方差 $\sigma^2$， 证明: $\overline X = \frac {1} {n}\sum_{i=1}^n X_i \xrightarrow {P} u$
> 分析: 
> $\begin{array}{l} 
> E(\overline X) = E(\frac {1} {n} \sum_{i=1}^n X_i) = \frac {1} {n} (nu) = u \\
> D(\overline X) = D(\frac {1} {n} \sum_{i=1}^n X_i) = \frac {1} {n^2} (n \sigma^2) = \frac {\sigma^2} {n} \\
> \therefore P \{ |\overline X -u | \ge \epsilon \} \le \frac {\frac {\sigma^2} {n}} {\epsilon^2} = 0 (n-> +\infty)
> \end{array}$

## 大数定律

> 概率的统计学规律定义的合理性基础(随机现象的统计学规律：在相同的条件下进行大量的重复实验才能显现出来)

- 定义

> 设有随机变量序列 $\{X_i \}, i=1,2,3,\cdots; E(X_i), i =1,2,3, \cdots$都存在，若对 $\forall \epsilon > 0$
> 有: $\mathop {\lim} \limits_{n->\infty} P \{ |\frac {1} {n} \sum_{i=1}^n X_i - \frac {1} {n} \sum_{i=1}^n E(X_i)| < \epsilon \} = 1$
> 则称 $\{X_i\}$ 服从大数定律。即 ($\frac {1} {n} \sum_{i=1}^n X_i - \frac {1} {n} \sum_{i=1}^n E(X_i) \xrightarrow {P} 0$, 是指一列随机变量的算术平均和依概率收敛到这列随机变量的期望的算术平均值)

> 大数定律说明来算数平均值及频率(随着实验次数趋于无穷大)的稳定性

- 常见的大数定律

> （1）切比雪夫大数定律
> 设 $\{X_i\}$ 是相互独立的随机变量序列，$E(X_i), D(X_i), i=1,2,\cdots$ 都存在， 且 $\{ d(X_i) \}$ 一致有界($\exists M>0, \forall i, D(X_i) < M$), 则称 $\{X_i\}$服从大数定律
> 
> （2）独立同分布大数定律
> 设 $\{X_i\}$ 是独立、同分布序列，且 $E(X_i) = u, D(X_i) = \sigma^2,i=1,2,\cdots$， 则 \{ X_i\} 服从大数定律
> 
> （3）伯努利大数定律
> 设在n重伯努利试验中，A事件出现m次，P(A)= p, 则对 $\forall \epsilon > 0, \mathop {\lim} \limits_{n to \infty} P \{ |\frac {m} {n} - p| < \epsilon \} = 1$

- 小概率事件原理

> 如果A事件发生的概率很小，则发生的频率也很小，即，在通常做的若干次试验中，A几乎不会发生。所以在实际生活中，经常忽略那些概率很小的事件发生的可能性
> 
> 小概率事件原理：概率很小的事件在一次试验中几乎是不会发生的，我们就认为它(在一次试验中)是不可能事件。

> <font color=red>小概率事件是假设检验的理论基础</font>

## 中心极限定理

> 所有的分布中，最重要，应该用最广泛的是正态分布

> 中心极限定理奠定了正态分布至高无上的地位。研究的对象可能是由很多的个体所组成的，每个个体的分布可能都不一样，但可以不用关心，只需要关心总体呈现出来的是一个正态分布

- 定义
  
  > 设 $\{ X_i \}$ 是相互独立的随机变量序列,$Z_n = \frac {\sum_{i=1}^nX_i - \sum_{i=1}^n E(X_i)} {\sqrt {\sum_{i=1}^n D(X_i)} }$ (Zn是一个前n项和的标准化处理)
  > 记作 $Z_n$的分布函数为 $F_n(x)$, 如果 $\mathop {\lim} \limits_{n \to \infty} F_n(x) = \Phi(x) = \int_{-\infty}^x \frac {1} {\sqrt {2 \pi}} e^{- \frac {t^2} {2}}dt, (-\infty < x < +\infty)$, 则称 $\{X_i\}$服从中心极限定理. (Zn 依分布收敛于标准正态变量)
  
  > 现实生活中有很多变量可以表示为诸多相互独立的随机变量的和，而其中每个随机变量对总和的影响都非常小，则这个总和近似服从正态分布。

- 独立同分布中心极限定理
  
  > 设 $\{X_i\}$ 为独立同分布的随机变量序列, $E(X_i)=u, D(X_i) = \sigma^2, i=1,2,\cdots$, 
  > 则 $\mathop {\lim} \limits_{n \to \infty} \{ \frac {\sum_{i=1}^nX_i-nu} {\sqrt {n} \sigma} \le x \} = \Phi(X)$
  > ($\frac {\sum_{i=1}^nX_i-nu} {\sqrt {n} \sigma}$ 可以看成是标准正态分布)

- 隶莫佛-拉普拉斯中心极限定理
  
  > 设 $\{X_n\} \sim B(n, p), n=1,2,\cdots$ 那么 $P \{ \frac {X_n - np} {\sqrt {np(1-p)}} \le x \} = \Phi(X)$

- ex
  
  > 设有数量很大的一批产品，其次品率为0.02，先从中任取10000件，求次品率不超过221件的概率
  > 分析: 由于数量非常巨大，因此在抽样的过程中可以看成是有放回的抽样，可以看成是二项分布
  > X: 任取10000件的中的次品数，那么 $\begin{array}{l}
  > X \sim B(10000, 0.02) \\
  > E(X) = np = 200, D(X) = np(1-p) = 196 \\
  > \therefore P \{0 \le X \le 221\}  \\
  > = P \{ \frac {0-200} {\sqrt {196}} \le \frac {X-E(X)} {\sqrt {D(X)}} \le \frac  {221-200} {\sqrt {196}}\} \\
  > = \Phi(\frac  {221-200} {\sqrt {196}}) - \Phi (\frac {0-200} {\sqrt {196}})
  > \end{array}$

# 抽样分布理论

## 数理统计基本理论

### 数理统计研究的方向和性质

> 数理统计是数学的一个分支，它主要研究如何收集和使用随机性数据
> （1）有效收集数据：普查、抽样调查、安排实验
> 如何安排抽样调查，是有效收集数据的主要问题，这构成了数理统计的一个重要的分支 -- 《抽样调查方法》；
> 如何安排式样方案以及分析实验结果，构成了数理统计的另一个重要分支 -- 《实验的设计和分析》

> （2）有效使用数据：分析和提取数据中的信息，对所研究的问题作出“统计推断”
> 为了有效地使用数据进行统计推断，需要建立一个统计模型，并给出某些准则(评价不同的统计推断方法的好坏)

> （3）归纳性质
> 一般的数学是演绎推理式的，而统计是(从大量的个体)归纳推理所得。由于归纳推理依赖于随机性的数据，其结果也具有不确定性。统计就是提供归纳推理和计算不确定性程度的方法(比如用概率来进行估计)

### 数理统计的基本概念

> 数理统计的任务就是要通过样本去推断总体，这就要对样本的数据进行分析整理，构造出合适的量用以解决总体的相关问题

- 总体

> 由所研究问题的有关个体组成，至少有两个以上的个体
> 按着所包含个体的数目分为：有限总体和无限总体(如果总体虽然包含有限个，但是个体非常多，也可以近似的看成无限总体)

> 定义：统计问题所研究对象的全体成为总体，总体可以用一个随机变量或者多维随机向量及其概率分布来描述

- 样本

> 从总体中抽取的一部分个体. (不同的抽样方法得到不同的样本)
> 在统计研究中，不关心研究具体的比如人，物体等，而主要关心的是总体内个体的一项(或几项)数量指标，所以总体可以看成是这样的一个集合：
> （1）是数的集合(这的数就是群体中某个属性，比如群体的身高、体重等)
> （2）由于每个个体的出现是随机的，相应的数量指标也是随机的，则对应的总体被看成是随机变量，服从某个分布

> 样本的两重性：在实施抽样前，被看做是随机变量；完成抽样后，它是具体的数

- (简单随机)样本

> 两个要求: （1）代表性：总体中每个个体都有同等的机会被抽为样本，即每个个体与总体有相同的分布
> （2）独立性：样本中每个个体取值不影响其它个体取值，即样本中的各个个体都是相互独立的

> 有放回抽样 --> 简单随机样本
> 无放回抽样 --> 当总体中的个体很多或样本在总体中所占比例很小可以看成是简单随机样本 

> 设总体为X，分布函数为F(X). {X1,X2,...,Xn} 为总体中抽取出来的样本，则{X1,X2,...,Xn} (n维的随机向量) 的联合分布为：
> (由独立性可得) $F(X_1)F(X_2)\cdots F(X_n) = \prod_{i=1}^n F(X_i)$ （分布函数可以描述任意一种形式的随机变量）
> 若X的密度函数为f(x)(假设此处为连续型), 则样本的联合概率密度为$\prod_{i=1}^n F(X_i)$

- 统计模型

> 数学中的模型通常指某个函数或者某个方程；而统计中的模型指的是所研究问题的样本的分布
> 只有样本得分布明确了，研究的问题才能明确，样本 ----> 模型
> 例如正态分布样本 ----> 正态模型

- 统计推断

> 两大问题：（1）若样本的分布形式已知，对其所含未知参数的推断 -- 参数统计推断，比如参数估计、假设检验等
> （2）样本的分布未知 -- 非参数统计推断

### 统计量

- 定义

> 由样本所确定(计算)的量是统计量。或者统计量是样本的函数，即统计量完全由样本决定。(统计量只和样本有关，不包含总体的未知参数)

> 样本具有两重性，因此统计量也具有两重性: 既可以看成是具体的数，可以看成随机变量;
> 所以就有了概率分布，这就给了我们统计推断的依据

> 统计量应该最好的集中了样本的(与总体关联度最高的)信息以解决总体的相应的问题 

- 常见的统计量

> 设X是总体，$X_1,X_2,\cdots, X_n$是样本

> （1）样本均值: $\overline X = \frac {1} {n} \sum_{i=1}^n X_i$

> （2）样本方差: $S^2 = \frac {1} {n-1} \sum_{i=1}^n (X_i-\overline X)^2$
> ($S^2 = \frac {1} {n} \sum_{i=1}^n (X_i-\overline X)^2$ 样本(原始)方差， 与"无偏性"有关)

> （3）矩
> $\alpha_k = \frac {1} {n} \sum_{i=1}^n X_i^k, k=1,2,\cdots$ k阶原点矩
> $\beta_k = \frac {1} {n} \sum_{i=1}^n (X_i - \overline X)^k, k=1,2,\cdots$ k阶中心矩

> （4）次序统计量
> 将 $X_1,X_2,\cdots, X_n$  排列为 $X_{(1)},X_{(2)},\cdots, X_{(n)}$, 则称 $X_{(1)},X_{(2)},\cdots, X_{(n)}$ 为次序统计量，$X_{(n)},X_{(1)}$为样本的极大值和极小值

## 三大分布

### $\chi^2$ 分布

- 定义
  
  > 一个随机变量: 设$X \sim N(0, 1)$, 则 $Y = X^2 \sim \chi^2(1)$ (自由度为1[由一个标准正态分布生成])
  > 
  > 两个随机变量: 设$X_1 \sim N(0, 1),X_2 \sim N(0, 1)$ 且相互独立, 则 $Y = X_1^2 + X_2^2 \sim \chi^2(2)$ (自由度为2[由2个标准正态分布生成])
  > 
  > 设$X_1,X_2,\cdots,Z_k \sim N(0, 1)$ 且相互独立, 则 $Y = X_1^2 + X_2^2 + \cdots + X_k^2 = \sum_{i=1}^k X_i^2 \sim \chi^2(k)$

- 性质
  
  > （1）连续型随机变量，密度函数比较复杂。特点只在大于0的区域，自由度越大，密度曲线越对称
  > （2）$Y \sim \chi^2(k), E(Y)=k; D(Y) = 2k$
  > （3）$\chi^2$的可加性: 若$Y_1 \sim \chi^2(n_1), Y_2 \sim \chi^2(n_2)$ 独立，那么 $Y_1+Y_2 \sim \chi^(n_1+n_2)$

- 分位数/分位点
  
  > $X \sim \chi^2(n), P \{ X > \lambda \} = \alpha, \lambda = \chi_{\alpha}^2(n)$ 称为自由度为n 的 $\chi^2$分布的上 $\alpha$ 分位点

### t 分布

- 定义
  
  > 设 $X \sim N(0, 1), Y \sim \chi^2(n)$
  > 则$T = \frac {X} {\sqrt {\frac {Y} {n}}} \sim t(n)$

- 性质
  
  > （1）密度函数的特点类似于标准正态分布 N(0, 1)，关于x=0对称
  > （2）若 $T \sim t(n), n \ge 2 => E(T) = 0; n \ge 3 => D(T) = \frac {n} {n-2}$
  > （3）$n \to \infty$时，其极限的分布为 N(0,1)

- 分位数/分位点
  
  > 三种分布通过概率密度函数计算概率会非常复杂，因此数学家把常见的值编制成了表，通过分位点的概念，通过查表即可查出分布的概率
  > $P \{ |T| > \lambda \} = \alpha, 记 \lambda  = t_{\frac {\alpha} {2}}(n)$ 成为自由度为n的t分布的 双侧$\alpha$分位数或者分位点。即给定了 $\lambda$这个点，$\alpha || \frac {\alpha} {2}$ 可以通过查表查出来或者给定 $\alpha || \frac {\alpha} {2}$，那么$\lambda$这个点也可以通过查表查出来。

### F分布

- 定义
  
  > 设 $X \sim \chi^2(m), Y \sim \chi^2(n)$ 且独立
  > $F = \frac {\frac {X} {m}} {\frac {Y} {n}} \sim F(m, n)$

- 性质
  
  > （1）连续型随机变量，密度函数比较复杂。特点只在大于0的区域
  > （2）若 $X \sim F(m, n) => \frac {1} {X} \sim F(n, m)$
  > （3）若 $T \sim t(n) => T^2 \sim F(1, n)$
  > （4）$F_{1-\alpha} (m, n) = \frac {1} {F_{\alpha} (n, m)}$

- 分位数/分位点
  
  > $P \{ X > \lambda \} = \alpha, \lambda = F_{\alpha}(m, n)$ 称为自由度为(m,n) 的 F分布的上 $\alpha$ 分位点

## 抽样分布定理(正态总体均值、方差相关的分布)

> 设 $X_1, X_2, \cdots, X_n$ 是来自正态总体分布 $X \sim N(u, \sigma^2)$的样本
> 
> $\overline X = \frac {1} {n} \sum_{i=1}^n X_i, S^2 = \frac {1} {n-1} \sum_{i=1}^n (X_i - \overline X)^2$
> 
> 那么, (1) $\overline X \sim N(u, \frac {\sigma^2} {n})$
> 
> $E(\overline X) = E(\frac {1} {n} \sum_{i=1}^n X_i) = \frac {1} {n} * (nu) = u$
> 
> $D(\overline X) = D(\frac {1} {n} \sum_{i=1}^n X_i) = \frac {1} {n^2} * (n \sigma) = \frac {\sigma} {n}$

> ex: 用一把尺子，测量某件仪器，怎样可以测量误差最小？（多次测量取平均值，上面就是理论依据）

> (2) $\frac {(n-1)S^2} {\sigma^2} = \frac {n S_n^2} {\sigma^2} = \frac {\sum_{i=1}^n (X-\overline X)^2} {\sigma^2} \sim \chi^2(n-1)$ (样本均值)
> $X_i \sim N(0, 1) => \frac {X_i - u} {\sigma} => \sum_{i=1}^n (\frac {X_i -u} {\sigma})^2 \sim \chi^2(n)$ (总体均值)

> (3) $\overline X 与 S^2$是相互独立的

> （4）有(1)(2)构造t分布 $T = \frac {\sqrt{n} (\overline X - u)} {S} \sim t(n-1)$

> (5) 设 $X_1,X_2,\cdots,X_n$ 和 $Y_1,Y_2,\cdots,Y_n$ 分别来自正态总体$N(u_1, \sigma_1^2), N(u_2, \sigma_2^2)$，<font color=red>两个样本相互独立</font>
> 
> $\overline X = \frac {1} {n1} \sum_{i=1}^{n1} X_i, \overline Y = \frac {1} {n2} \sum_{i=1}^{n2} Y_i$
> 
> $S_1^2 = \frac {1} {n1-1} \sum_{i=1}^{n1} (X_i - \overline X)^2, S_2^2 = \frac {1} {n2-1} \sum_{i=1}^{n2} (X_i - \overline Y)^2$
> 
> 那么有 $\frac {S_1^2/S_2^2} {\sigma_1^2/\sigma_2^2} \sim F(n_1 -1, n_2 -1)$
> 
> $\sigma_1^2 = \sigma_2^2 = \sigma^2 => \frac {(\overline X - \overline Y) - (u1-u2)} {S_w \sqrt{1/n_1 + 1/n_2}} \sim t(n_1+n_2-2),S_w^2 = \frac {(n_1 - 1)S_1^2 + (n_2 - 1) S_2^2} {n_1+n_2-2}$
> 
> 证明：$\begin{array}{l}
> {V_1} = \frac{{({n_1} - 1){S_1}^2}}{{{\sigma _1}^2}} = \frac{{\sum\limits_{i = 1}^{{n_1}} {{{({X_i} - \overline X )}^2}} }}{{{\sigma _1}^2}} \sim {\chi ^2}({n_1} - 1)\\
> {V_2} = \frac{{({n_2} - 1){S_2}^2}}{{{\sigma _2}^2}} = \frac{{\sum\limits_{i = 1}^{{n_2}} {{{({Y_i} - \overline Y )}^2}} }}{{{\sigma _2}^2}} \sim {\chi ^2}({n_2} - 1)\\
> \frac{{{V_1}/({n_1} - 1)}}{{{V_2}/({n_2} - 1)}} = \frac{{{S_1}^2/{S_2}^2}}{{{\sigma _1}^2/{\sigma _2}^2}} \sim F({n_1} - 1,{n_2} - 1)
> \end{array}$
> 
> $\begin{array}{l}
> U = \overline X  - \overline Y  \sim ({u_1} - {u_2},\frac{{{\sigma ^2}}}{{{n_1}}} + \frac{{{\sigma ^2}}}{{{n_2}}} )\quad (正态分布可加性)\\
>  = \frac{{(\overline X  - \overline Y ) - ({u_1} - {u_2})}}{{\sigma \sqrt {\frac{1}{{{n_1}}} + \frac{1}{{{n_2}}}} }} \sim N(0,1)\\
> V = {V_1} + {V_2} = \frac{{({n_1} - 1){S_1}^2}}{{{\sigma ^2}}} + \frac{{({n_2} - 1){S_2}^2}}{{{\sigma ^2}}} \sim {\chi ^2}({n_1} + {n_2} - 2) \quad （独立，\chi^2分布可加性）\\
> \frac{U}{{\sqrt {V/({n_1} + {n_2} - 2)} }} = \frac{{(\overline X  - \overline Y ) - ({u_1} - {u_2})}}{{{S_w}\sqrt {\frac{1}{{{n_1}}} + \frac{1}{{{n_2}}}} }} \sim t({n_1} + {n_2} - 2)\\
> ({n_1} + {n_2} - 2){S^2}_w = ({n_1} - 1){S_1}^2 + ({n_2} - 1){S_2}^2\\
> \end{array}$

# 描述统计

> 描述统计学(Descriptive Statistics)通常用来组织和概括最初收集的数据。当统计学家在做调查时，会收集大量的数据，这些数据在原始状态下通常杂乱无章。为了消除这些混乱，希望使用一些易懂的方式重新组织和展现数据。这些方式包括图表和汇总计算。我们把这些描述、概括、和表现批量数据的方法和工具统称为统计描述。

## 变量类型

> 在统计应用中，通常需要考察一个变量或者多个变量的变化趋势及其关联性。变量是一个具有很多值(可能无穷多个)的特征或现象，它会随着环境等其他因素的变化而变化。比如身高、体重等。在统计和实验分析中，要区分自变量和因变量。

> 变量类型主要是基于相应的变量数值可做的有意义的数学运算进行区分的。比如学生的学号和成绩都是数字，但是它们能做的算术运算是不同的，学号的加减乘除算术运算没有意义；而成绩可以做适当的运算。特别需要注意的是，不同类型的变量，适用的统计方法也不同。

- 根据不同的度量水平将变量分为以下四类

(1) 定类变量(Nominal Variable)

> 又称名义变量，通常只能用来代表不同的分类。它是没有顺序、大小之分的比较低级的一类变量，变量相对应的数据没有数量的含义，只用来识别种类。
> 它只能用来表明一类事物不同于另外一类事物，但不代表一类事物比另外一类事物更好或更重要。比如我们常用1代表男性；0代表女性
> 定类变量之间的数学关系就是等于(=)或者不等于

(2) 定序变量(Ordinal Variable)

> 定序变量是量化尺度的最基本形式，它的一个典型特征就是采用数字表示顺序。定序变量的每个分类不但代表着差别，而且有等级之分。比如，更大、更快、更高、更强等。
> 定序变量之间的数学关系包括: 等于、不等于、大于、小于
> 并不能确定排名之间的距离

(3) 定距变量 (Interval Variable)

> 也成为间隔变量，描述事物类别或次序之间的间距。
> 定距变量不仅能将事物区分不同的类型并进行排序，而且还能准确地指出类别之间的差距是多少。
> 定序变量之间的数学关系包括: 加减乘除、等于、不等于、大于、小于等运算

> 在定距变量中，0是强行规定的，它不代表完全没有的意思。例如：摄氏温度中，零点不代表完全没有温度，没有热量，它仅仅代表水结冰的温度，是我们强行规定的一个零点。
> 我们在采用某种度量或者变量进行数据收集时，有可能不经意之间就设置了强制零点。比如，在英语考试的百分制考试中，我们不能说80分同学的英语水平是40分同学英语水平的2倍，因为英语考试是0分的同学不代表他完全没有英语知识。

(4) 定比变量 (Ratio Variable)

> 定比变量是在定距变量的基础上，扩展可作为比率的基数而成，通常能够显示出更加深刻的意义
> 定比变量通常需要一个统一的单位，比如米、厘米、公斤、秒等；身高、体重等都是一种定比变量它们对应于长度和重量的度量
> 和定距变量的一个根本的区别是定比变量的0点代表了完全没有的含义。

| 变量类型 | 特点             | 关系和运算                | 例子       |
| ---- | -------------- | -------------------- | -------- |
| 定类变量 | 无顺序分类          | 等于、不等于               | 性别、政党    |
| 定序变量 | 有顺序分类          | 等于、不等于、大于、小于         | 严重、一般、轻微 |
| 定距变量 | 等间隔，有单位，没有绝对零点 | 等于、不等于、大于、小于、加、减     | 温度、成绩    |
| 定比变量 | 等间隔，有单位，有绝对零点  | 等于、不等于、大于、小于、加、减、乘、除 | 身高、年龄、体重 |

> 一般来说，数据的等级越高，应用范围越广泛，等级越低，应用范围越受限。
> 不同测度级别的数据，应用范围不同。
> 等级高的数据，可以兼有等级低的数据的功能，而等级低的数据，不能兼有等级高的数据的功能

## 统计图表

> 图解分析方法的统计学工具
> 在假设检验、模型选择、统计模型验证、估计量选择、关系确定、因素效应判定以及离群值检出方面，这些图解工具可以作为最佳捷径用来深度认识数据集。
> 优质的统计图标还可以作为一种令人信服的沟通手段，用来向他人传达在数据之中的基本讯息

### 分类型数据的统计图表

> 分类数据来源于定类变量，主要用于事物的分类描述。因此在整理时除了要列出所分的类别，还要计算每一个类别的频数、频率、累积频率等。
> 基本的图表有如下：

- 频数分布表/累积频数分布表
  
  > 各类中数据出现的次数。

- 柱状图/条状图
  
  > 用等宽的垂直图条来显示按类别分组的数据，然后用柱状图的高度来表示描述统计量的值。柱状图和条状图对显示一段时间数据变化或者说明各项之间的比较来说十分有用
  > 使用场景：（1）说明各组之间的比较情况

- 饼图
  
  > 使用面积来表示数值大小的图形。主要用来描述频数、频率或百分比之间的相对关系，对于研究结构性问题十分有用。
  > 主要缺点：由于饼图使用面积代表了长度，加大了各个数据进行比较的难度，所以不建议在各组数据相近的情况下使用饼图
  > 使用场景：（1）饼图具有很好的视觉、结构比重效果，在商业领域及杂志中使用广泛
  > （2）可以表现的信息相对较少，只有当数据聚合成7个数据点或更少的数据点后才考虑使用饼图

- 折线图
  
  > 使用线段将各数据点连接起来而组成的图形，用折线表示数据的变化趋势。可以反映数据的递增、递减、周期性、螺旋性规律、峰值等特征。折线图，一般使用水平轴来表示时间的推移，使用垂直轴代表不同时间的数据大小。
  > 使用场景：（1）显示在相等时间间隔下的数据趋势
  > （2）分析多组数据随着时间的变化相互作用和相互影响

- 帕累托图
  
  > 图中包括柱状图和折线图，其中柱状图按着时间发生的评率降序排列，而折线则显示了累积频率。横轴表示分类，左纵轴表示出现的频率，右纵轴表示累积频率
  > 使用场景：（1）可以从大量的数据中找出最重要的最有影响力的因素，如项目实施失败的主要原因
  > （2）怕累托图通常用于质量控制中

### 数值型数据的统计图表

> 数值型数据包括定距和定比数据，在整理时通常需要进行数据分组，数据分组后再计算出各组中数据出现的频数，这就形成了一张频数分布表;
> 可以将数值型数据降维为分类型数据，这样就可以使用定类型的显示很分析;
> 数值型特有统计图形展示方法如下

> （1）确定分组: 一批数据分组的组数与数据的多少、数据本身的特点和领域的研究经验有关系。分组的一个主要目的就是为了观察数据分布的特征
> 如果没有前人的相关领域的研究经验可以供参照，可以使用Sturges提出的经典公式确定组数k $k = 1 + \frac {lnn} {ln 2}$
> 
> （2）确定组距: 均分。组距 = (最大值 - 最小值) / 分组数
> (3)频数、频率、累积频数、累积频率计算

- 直方图
  
  > 使用矩形的宽度和高度来表示频数分布的图形，这些数据会分组到各个数据段中。在平面直角坐标中，横轴表示分组，纵轴表示频数或者频率，各组与相应的频数就构成了一个矩形，即直方图
  > 使用场景：（1）描述数据集的分布，如数据的中心、范围、散布、倾斜度、众数等信息
  > （2）当数据量巨大时，可以使用直方图
  
  > 直方图和柱状图的区别
  > （1）直方图的横坐标是连续的数据，用于展示数据型的数据；柱状图则是分类轴，用于展示分类数据
  > （2）因为分组数据是连续，所以直方图的各矩形都是连续的；柱状图是分开的
  > （3）直方图用面积表示各个类别的频数或频率，高度和宽度都有意义；柱状图用高度表示

- 茎叶图
  
  > 优点
  > （1）从统计图上没有原始数据信息的损失，所有数据信息都可以从茎叶图中得到；
  > （2）茎叶图中的数据可以随时记录，随时添加，方便记录与表示。
  
  > 缺点：茎叶图只便于表示个位之前相差不大的数据，而且茎叶图只方便记录两组的数据。两个以上的数据虽然能够记录，但是没有表示两个记录那么直观、清晰

- 盒装图
  
  > 又称为箱型图，是一个用来表示数据集的位置和变异信息的工具，特别是用于发现不同数据组之间的位置和变异信息的变化。
  > 使用场景：当有多组数据，而且每一组数据量巨大时尤其推荐使用。可以用于比较多组数据之间的分布变化。

### 多变量数据的统计图表

- 散点图 -- 两个变量
  
  > 利用笛卡尔坐标系来表示值。散点图将序列显示为一组点，值由点在坐标中的位置表示，类别可以用图表中的不同标记来表示。
  > 横轴表示变量X(自变量)，纵轴表示变量Y(因变量)
  > 散点图可以看出：
  > （1）X,Y 是否相关
  > （2）X,Y 是否线性相关
  > （3）X,Y 是否非线性相关
  > （4）变量Y是否依赖于变量X
  > （5）是否存在离群点
  
  > 使用场景：（1）在不考虑时间因素的情况下，显示可比较数值，以处理值的分布和分簇

- 列联表 -- 多个变量
  
  > 将观测数据按着两个或更多属性(通常是定类变量或者定序变量)分类时所列出的频数表。
  > 列联表的目的是多变量分组，然后比较各组的分布状况，以期发现变量之间的关系

- 雷达图 -- 多个变量
  
  > 使用场景：（1）雷达图常用于比较和显示不同批次的数据和不同变量的数值总和的情形
  > （2）也通常用来比较和显示不同数据间的相似性

### 统计图表使用准则

## 数据汇总

### 集中趋势度量(Central Tendency)

> 集中趋势反应的是数据(样本或总体)的平均水平或者数据的中心值。

- 众数
  
  > 定义：一批数据中出现次数最多的那个值，通常记为M
  
  > 性质：（1）不受极值的影响
  > （2）通常用来描述离散型变量，尤其是定类变量
  > （3）对于定序变量、定距变量、定比变量，可以先分组再求众数
  > （4）对于定序变量、定距变量、定比变量，通常使用中位数和算术平均数表示集中趋势

- 中位数
  
  > （1）定义：数据从小到大排序后，处在数据序列中间位置的数值
  
  > 性质：（1）不受极值的影响

- 四分位数

- (算术)平均值
  
  > 性质：（1）易受极值影响(因为计算是以所有观察值为依据)，此时算术平均值不是描述这类数据集中趋势的最佳度量

- 加权平均值
  
  > 权重的设置通常要求某种性质，如重要性、频繁度等

- 几何平均值
  
  > 定义：n个数据相乘的n次方根。
  
  > 性质：（1）主要用来描述平均比率(如平均增长率、平均速度等)
  > （2）要求每个值都是非负的
  > （3）几何平均值受极端值的影响较算术平均数小。
  > （4）几何平均值的对数是 各变量值对数的算术平均数
  > （5）几何平均值适用于反映特定现象的平均水平，即现象的总标志值是 各单位标志值的连乘积，而不是各单位标志值之和
  
  > ex: 南京市某区5年的经济增长率分别为8%，9%，10%，12%，12%，则这5年的平均经济增长率计算如下
  > $\overline X_G = sqrt [5] {1.08 * 1.09 * 1.10 * 1.12 * 1.12} \approx 1.102$
  > $1.102 - 1 = 10.2%$
  > 分析：令该地区起始的经济总量为X0，则5年后的经济总量为 $X_0 * 1.08 * 1.09 * 1.10 * 1.12 * 1.12$, 设平均增长率为I，
  > 那么， $X_0 * 1.08 * 1.09 * 1.10 * 1.12 * 1.12 = X_0 * (1+I)^5$

- 调和平均数
  
  > 定义：又称为倒数平均值，它是对每个数据的倒数求平均，然后再求倒数
  > $\begin{array}{l}
  > \overline {{X_H}}  = \frac{1}{{\frac{{\frac{1}{{{X_1}}} + \frac{1}{{{X_2}}} +  \cdots  + \frac{1}{{{X_n}}}}}{n}}} = \frac{n}{{\sum\limits_{i = 1}^n {\frac{1}{{{X_i}}}} }}
  > \end{array}$
  
  > $\begin{array}{l}
  > \overline {{X_H}}  = \frac{1}{{\frac{{\frac{{{w_1}}}{{{X_1}}} + \frac{{{w_2}}}{{{X_2}}} +  \cdots  + \frac{{{w_n}}}{{{X_n}}}}}{{{w_1} + {w_2} +  \cdots  + {w_n}}}}} = \frac{{\sum\limits_{i = 1}^n {{w_i}} }}{{\sum\limits_{i = 1}^n {\frac{{{w_i}}}{{{X_i}}}} }}
  > \end{array}$
  
  > 性质：（1）易受极值的影响，且受极小值的影响比极大值的影响更大 （2）应用范围较小，当任一数据为0时，就不能使用调和平均值

### 离散趋势度量(Variation Tendency)

> 集中趋势度量经常是我们产品设计的目标，但还要考虑数据的离散程度，即考虑系统最高流量/访问量是多少。研究数据的变异对于统计分析往往是必要的。很多时候考虑单独一个数据是没有意思的，只有将它与同分布的其他数据相比较才有意义。例如，某班的平均成绩是80分，一个人考了85分，比平均分高了5分，然后，算他优秀还是良好？这5分的差距大吗？这取决于其它数据的分布。

> 只有知道了数据的集中趋势和离散趋势的度量，才能更好的理解数据，作出正确的判断。

> 不受极值影响的度量通常称为抵抗度量(Resistant Measures)， 通常有中位数、四分位数、四分位距(内距)

- 极差(又称全距)
  
  > 是样本观察值的最大值和最小值的差，反应一批数据总的离散趋势。但全距不考虑数据的分布情况.
  > 使用场景：当需要初步分析产品的波动情况，暂时不需要知道产品分布的详细离散程度时

- 内距
  
  > 又称为 内四分位距，用来描述中间50%的样本观察值的离散趋势度量，它是四分之三位数与四分之一分位数的差。
  > 使用场景：当数据分布有偏斜时，中位数通常用来作为集中趋势度量，内四分位距用作离散趋势度量
  > 缺点：（1）不能提供精确的数据分布信息  （2）不能用来进行精确的统计推断

- 方差、标准差
  
  > 考虑到了所有数据的分布和离散趋势情况

- 变异系数
  
  > 又称为标准差率，通常用来比较不同数据分布的离散趋势。当进行两个或多个离散趋势度量时，如果度量单位相同且平均值接近，可以直接用标准差表；如果单位不同或者平均值差异较大，需要采用变异系数来比较。变异系数通常记做CV= 样本标准差/ 样本均值

### 形态度量(Shape Tendency)

- 偏度
  
  > 描述数据的对称性，它是三阶距的一个形式。
  > 定义：设一批数据为 $X_1,X_2,\cdots, X_n$ 则 $s^3 = \frac {B_3} {(B_2)^{1.5}} = \frac {\frac {\sum_{i=1}^n (X_i - \overline X)^3} {n}} {(\frac {\sum_{i=1}^n (X_i - \overline X)^2} {n})^{1.5}}$
  
  > 近似公式，通过平均值和中位数的偏差来估计偏度的大小 $s'^3 = \frac {3(\overline X - M_e)} {s} = \frac {3(平均值-中位数)} {标准差}$
  
  > 性质：（1）偏度为0，那么数据是对称的，此时平均数和中位数相等
  > （2）如果偏度大于0，数据是是正偏的，此时平均值大于中位数
  > （3）如果偏度小于0，那么数据是负偏的，此时平均值小于中位数

- 峰度
  
  > 描述数据的尖峰程度，即数据是否集中在均值附近或是否存在较多偏大的极端值，它是四阶距的一个形式。
  > 定义：设一批数据为 $X_1,X_2,\cdots, X_n$则 $s^4 = \frac {B_4} {(B_2)^{2}} = \frac {\frac {\sum_{i=1}^n (X_i - \overline X)^4} {n}} {(\frac {\sum_{i=1}^n (X_i - \overline X)^2} {n})^{2}}$  
  
  > 近似计算公式, $s'^4 =  3 + \frac {Q_3 - Q_1} {2(P_{90} - P_{10})} = 3 + \frac {四分之三分位数 - 四分之一分位数} {2(90\%分位数 - 10\%分位数)}$  
  
  > 性质：标准正态分布的峰度为3（1）尖峰风度：峰度 > 3 （2）平顶峰度： 峰度 < 3 （3）矩形形态：峰度为1.8 左右 （4）U字形: 峰度 < 1.8

# 参数估计

> 在已知总体分布的前提下，用一个样本去推断出有未知的参数

## 点估计

> 设总体分布函数为 $F(x, \theta_1, \theta_2, \cdots, \theta_k)$ (分布已经确定，但有未知参数)。 
> 从样本 $X_1,X_2,\cdots, X_n$, 根据未知参数 $\theta_i, (i=1,2,\cdots,n)$ 的特点，构造一个合适的统计量 $\hat {\theta_i} = \hat {\theta_i(X_1,X_2,\cdots, X_n)}$
> 每当有一个具体的样本值 $x_1, x_2, \cdots, x_n$ 带入到统计量中就会得到一个值,那么这个值就作为未知参数 $\hat {\theta_i(x_1,x_2,\cdots, x_n)}$ 的一个估计(由于求出来的是一个数值，把这样的估计叫做点估计)

### 矩估计

- 思想
  
  > 矩估计发基于一种简单的"替代"思想: 以样本矩作为总体矩的估计(假定取到的样本比较好)

- 公式
  
  > 总体矩: $a_k = E(X^k), b_k = E (X - E(X))^k$
  > 样本矩: $\alpha_k = \frac {1} {n} \sum_{i=1}^n (x_i)^k, \beta_k = \frac {1} {n} \sum_{i=1}^n (x_i - \overline x)^k$
  > 由大数定律，当n区域无穷大时，$\alpha_k \xrightarrow {P} a_k, \beta_k \xrightarrow {P} b_k$
  > 那么可以建立等式和方程:
  > $\alpha_k = a_k; \beta_k = b_k$ (a_k, b_k 包含总体的未知参数)
  > 注意：（1）有几个未知参数，就建立几个方程
  > （2）能用低阶矩就不用高阶矩
  > （3）矩估计结果不唯一(比如用不同阶矩建立这个未知参数的方程，计算的结果是不相同的)

- ex1
  
  > 设总体的期望和方差都存在，分别为 $u, \sigma^2$, 但其值未知，求$u, \sigma^2$的矩估计
  > 分析：$u = E(X) = a_1, \sigma^2 = E(X-E(X))^2 = b_2$
  > $\hat {u} = \alpha_1 = \overline X$
  > $\hat {\sigma^2} = \beta_2 = S_n^2$

- ex2
  
  > 设Poisson分布为 $P(\lambda), \lambda$ 未知，求 $\lambda$的矩估计
  > 分析：$\hat {\lambda} = \overline X$
  > $D(X) = \lambda => \hat {\lambda} = S_n^2$
  > \therefore $\hat {\lambda} = \overline X$ (用低阶矩来表示)

- ex3
  
  > 设 $X \sim U[a, b]$, 求a，b的矩估计
  > 分析：
  > $\begin{array}{l}
  > E(X) = {a_1} = \frac{{a + b}}{2}\\
  > D(X) = {b_2} = \frac{{{{(b - a)}^2}}}{{12}}\\
  > \therefore \left\{ \begin{array}{l}
  > \frac{{a + b}}{2} = \overline X \\
  > \frac{{{{(b - a)}^2}}}{{12}} = {S^2}_n
  > \end{array} \right.\\
  > a = \overline X  - \sqrt {3{S^2}_n}  = \overline X  - \sqrt 3 {S_n}\\
  > a = \overline X  + \sqrt {3{S^2}_n}  = \overline X  + \sqrt 3 {S_n}
  > \end{array}$

- 特点
  
  > 矩估计简单易行；
  > 精度和可靠程度相对于极大似然估计不是太好

### 极大似然估计

- 思想
  
  > 英国学者费歇尔提出，其基本思想是：最大可能性原则
  > 例如：甲：黑球2个， 白球8个；乙：黑球5个，白球5个；丙：黑球9个，白球1个。现随机选择一个盒子，从中取出一个球，发现是黑球，请估计这个黑球来自哪个盒子？
  > 分析：（1）可以从贝叶斯公式计算
  > （2）由样本观测值对概率做估计

- 定义
  
  > 设总体分布p(x)已知，含有一个或者几个未知参数 $\theta_1, \theta_2, \cdots, \theta_k$, $X_1, X_2, \cdots, X_n$ 为来自该总体的样本; $x_1, x_2, \cdots, x_n$ 是样本的观测值
  > 样本的联合密度: $\prod_{i=1}^n p(x; \theta_1, \theta_2, \cdots, \theta_k$
  > 样本的似然函数: $L(x_1, x_2, \cdots, x_n; \theta_1, \theta_2, \cdots, \theta_k) = 样本的联合密度$
  > 使似然函数L 取得最大值的 $\hat {\theta_1}, \hat{\theta_2}, \cdots, \hat{\theta_k}$ 称为未知参数 $\theta_1, \theta_2, \cdots, \theta_k$的极大似然估计值;
  > 统计量 $\theta_i = \theta_i(x_1, x_2, \cdots, x_n), i=1,2,\cdots, k$ 是 $\theta_i$ 的极大似然估计量

- ex1
  
  > 设 $X_1, X_2, \cdots, X_n$ 为来自该正态总体 $(u, \sigma^2)$ 的样本, 参数 $(u, \sigma^2)$ 未知， 求 $(u, \sigma^2)$ 的极大似然估计
  > 分析：设 $x_1, x_2, \cdots, x_n$ 为观测值
  > $L = \prod_{i=1}^n \frac {1} {\sqrt{2\pi} \sigma} exp(- \frac {(x_i - u)^2} {2 \sigma^2})$
  > L为单调递增，可取对数
  > $ln(L) = - \frac {n} {2} ln(2\pi) - \frac {n} {2} ln(\sigma^2) - \frac {1} {2\sigma^2} \sum_{i=1}^n (x_i-u)^2$
  > $\left\{ \begin{array}{l}
  > \frac{{\partial \ln (L)}}{{\partial u}} = \frac{1}{{{\sigma ^2}}}\sum\limits_{i = 1}^n {{{({x_i} - u)}^2}}  = 0\\
  > \frac{{\partial \ln (L)}}{{\partial {\sigma ^2}}} =  - \frac{n}{{2{\sigma ^2}}} + \frac{1}{{2{\sigma ^4}}}\sum\limits_{i = 1}^n {{{({x_i} - u)}^2}}  = 0
  > \end{array} \right.$
  > $\therefore \hat {u} = \frac {1} {n} \sum x_i = \overline X,  \hat {\sigma^2} = \frac {1} {n} \sum (x_i - \overline x)^2 = S_n^2$

- ex2
  
  > 设$X_1, X_2, \cdots, X_n$ 为来自Poisson总体 $P(\lambda)$, 参数 $\lambda$ 未知， 求 $\lambda$ 的最大似然估计
  > 分析： $P \{X = x\} = \frac {\lambda ^x} {x!} e^{-\lambda}, x=0,1,2,\cdots$
  > $L = \prod_{i=1}^n (\ frac {\lambda ^x_i} {x_i!} e^{-\lambda})$
  > $ln(L) = (\sum_{i=1}^n x_i) ln\lambda -n\lambda - \sum_{i=1}^n ln(x_i !)$
  > $\frac {dln(L)} {d\lambda} = 0$
  > $\lambda = \overline X$

## 估计量的评价标准

> 不同的方法或者同一个方法，比如点估计或者最大似然估计得到的结果可能都不同，因此需要对拟估计出来的结果做一个评价

- 无偏性 <---> 均值
  
  > 由于样本的不同，估计量可能取到不同的值，但是平均下来应该是和要估计的未知参数是一样的。
  
  > 定义：设 $\hat {\theta} = \theta(X_1, X_2, \cdots, X_n)$ 是一个未知参数 $\theta$ 的一个估计量，如果 $E(\hat {\theta}) = \theta$, 则称 $\hat {\theta} 是 \theta$ 的一个无偏估计量 (否则就是有偏估计， 这时称 $E(\hat {\theta} - \theta)$ 为估计量 $\hat {\theta}$ 的偏差， 也叫 $\hat {\theta}$ 的系统误差)。 无偏估计也就是没有系统误差
  
  > ex: 设总体k阶原点矩 $a_k = E(X^k)$ 存在，证明样本的k阶原点矩 $\alpha_k = \frac {1} {n} \sum_{i=1}^n X_i^k$ 是$a_k$ 的无偏估计。
  > 证明：$E(\alpha_k) = E(\frac {1} {n} \sum_{i=1}^n X_i^k) = \frac {1} {n} E(\sum_{i=1}^n X_i^k)$
  > 因为 $X_i$与总体分布相同
  > 所以： $(E(X_i^k) = E(X_k) = a_k)$
  > $E(\alpha_k) = \frac {1} {n} * n a_k = a_k$
  
  > 正态总体 $N(u, \sigma^2)$ 中用 $\overline X$ 估计u
  > 指数分布 用 $\overline X$ 估计 $\frac {1} {\lambda}$
  > Poisson 分布用 用 $\overline X$ 估计 $\lambda$
  > 设总体方差 为 $\sigma^2$， 那么 $S^2 = \frac {1} {n-1} \sum_{i=1}^n (X_i - \overline X) 是 \sigma^2$的无偏估计； $S_n^2 = \frac {1} {n} \sum_{i=1}^n (X_i - \overline X)$ 不是

- 有效性 <---> 方差
  
  > 定义：设 $\hat {\theta_1} = \theta(X_1, X_2, \cdots, X_n), \hat {\theta_2} = \theta(X_1, X_2, \cdots, X_n)$ 是参数 $\theta$ 的两个无偏估计，如果$D( \hat {\theta_1)}) \le D( \hat {\theta_2)})$, 则称 $\hat {\theta_1}$ 比 $\hat {\theta_2}$ 更有效($\hat {\theta_1}$ 波动性小，有更好的稳定性)
  
  > 定义：设 $\hat {\theta_0}$ 是 $\theta$ 的无偏估计， $\hat {\theta}$ 是 $\theta$ 的任一个无偏估计，如果 $D( \hat {\theta_0)}) \le D( \hat {\theta)})$, 则称$\hat {\theta_0}$ 是 $\theta$  的最小方差无偏估计。

- 一致性
  
  > 估计量与样本容量n有关，随着n的增加，估计量的值应该越来越趋向于被估计参数的真实值。
  
  > 定义：设 $\hat {\theta_n} = \hat {\theta_n (X_1, X_2, \cdots, X_n)}$ 为 $\theta$ 的估计量， 当 $n -> + \infty, \hat {\theta_n} \xrightarrow {P} \theta$， 则称 $\hat {\theta_n}$ 为 $\theta$ 的一致(相合)估计量。
  
  > 一致性是对估计量的根本要求，由大数定律可以证明常见的矩估计量是一致的

## 区间估计

> 点估计只是未知参数的一个近似值，难以判断其误差大小； 区间估计给出一个范围，并在要求可靠程度下保证这个范围包含了未知参数
> 现在最流行的一种区间估计理论是上世纪30年代 J.Neyman建立起来的

- 思想
  
  > 设 $\theta$ 是总体分布中的一个未知参数， $X_1, X_2, \cdots, X_n$ 是样本，要设法确定两个统计量 $\hat {\theta_1(X_1, X_2, \cdots, X_n)}, \hat {\theta_2(X_1, X_2, \cdots, X_n)}$ 恒有 $\hat {\theta_1} \le \hat {\theta_2}$, 以它们的端点 $[\hat {\theta_1}, \hat {\theta_2}]$ 满足两个要求 （1）可信度：这个随机区间 $[\hat {\theta_1}, \hat {\theta_2}]$ 以多大的概率包含了未知参数 $\theta$ （2）精度：区间长度 $\hat {\theta_2} - \hat {\theta_1}$ 要尽可能小
  > 在样本资源约束下，这两个条件是相互矛盾的
  
  > 原则: 先确定一个能接受的可信度(可靠度), 在此前提下尽量提高精度
  
  > 主要工作：给定置信度后，寻找估计精度尽可能高的置信区间

- 定义
  
  > 给定一个很小的数 $\alpha > 0$, 若对于参数 $\theta$ 的所有可能取值，都有 $P \{ \hat {\theta_1(X_1, X_2, \cdots, X_n)} \le \theta \le \hat {\theta_2(X_1, X_2, \cdots, X_n)} \} = 1 - \alpha$ , 则称随机区间 $[\hat {\theta_1}, \hat {\theta_2}]$ 是 $\theta$ 的置信度为 $1 - \alpha$ 的置信区间。

- 枢轴变量法
  
  > 设 $X_1, X_2, \cdots, X_n$ 来自于总体 $N(u ,\sigma^2)$ , 其中 $\sigma^2$ 为已知参数，求未知参数 u 的置信度为 $1 - \alpha$ 的置信区间
  > 分析：（1）找出一个未知参数 $\theta$ 的良好的估计量， 此处 $\overline X$ 来估计 u
  > （2）依次构造一个包含 $\theta$ 的函数W，W不包含其他未知数，且分布明确，此处 $W = \frac {\overline X - u} {\frac {\sigma} {\sqrt{n}}} \sim N(0, 1) \quad (\overline X \sim (u, \frac {\sigma^2} {n}))$
  > $P \{ - u_{\frac {\alpha} {2}} \le W \le u_{\frac {\alpha} {2}} \} = 1 - \alpha$
  > ($\overline X 比较好的估计了u，所以W以较大的概率在0附近$)
  > （3）将关于W的不等式改写为关于 $\theta$ 的不等式, 此处, $P \{ \overline X - \frac {\sigma} {\sqrt{n}} u_{\frac {\alpha} {2}} \le u \le \overline X + \frac {\sigma} {\sqrt{n}} u_{\frac {\alpha} {2}} \} = 1 - \alpha$
  > （4）查表确定需要的分位点，求出置信区间(此处W叫枢轴变量)
  > $[\overline X - \frac {\sigma} {\sqrt{n}} u_{\frac {\alpha} {2}}, \overline X + \frac {\sigma} {\sqrt{n}} u_{\frac {\alpha} {2}}]$ 即为所求的置信区间

### 常见的集中区间估计

- 一个正态总体 $X \sim N(u, \sigma^2)$ 的情形
  
  > （1）方差 $\sigma^2$ 已知，u的置信区间为 $[\overline X - \frac {\sigma} {\sqrt{n}} z_{\frac {\alpha} {2}}, \overline X + \frac {\sigma} {\sqrt{n}} n_{\frac {\alpha} {2}}]$ (推到过程见上面实例)
  
  > （2）方差 $\sigma^2$ 未知，u的置信区间为 $[\overline X - \frac {S} {\sqrt{n}} t_{\frac {\alpha} {2}} (n-1), \overline X + \frac {S} {\sqrt{n}} t_{\frac {\alpha} {2}}(n-1)]$
  > 推导：$\begin{array}{l}
  > \overline X  \sim (u,\frac{\sigma }{n})\\
  > {W_1} = \frac{{\overline X  - u}}{{\sigma /\sqrt n }} \sim N(0,1)\\
  > {W_2} = \frac{{(n - 1){S^2}}}{{{\sigma ^2}}} \sim {\chi ^2}(n - 1)\\
  > \frac{{{W_1}}}{{\sqrt {\frac{{{W_2}}}{{n - 1}}} }} = \frac{{\frac{{\overline X  - u}}{{\sigma /\sqrt n }}}}{{\sqrt {\frac{{\frac{{(n - 1){S^2}}}{{{\sigma ^2}}}}}{{n - 1}}} }} = \frac{{\overline X  - u}}{{S/\sqrt n }} \sim t(n - 1)\\
  > P\{ \left| {\frac{{\overline X  - u}}{{S/\sqrt n }}} \right| \ge {t_{\frac{\alpha }{2}}}(n - 1)\} \\
  > [\overline X  - \frac{S}{{\sqrt n }}{t_{\frac{\alpha }{2}}}(n - 1),\overline X  + \frac{S}{{\sqrt n }}{t_{\frac{\alpha }{2}}}(n - 1)]
  > \end{array}$
  
  > （3）u已知，方差 $\sigma^2$ 的置信区间
  > $\begin{array}{l}
  > X \sim N(u,\sigma )\\
  > \frac{{X - u}}{\sigma } \sim N(0,1)\\
  > Q = \sum\limits_{i = 1}^n {(\frac{{{X_i} - u}}{\sigma }} {)^2} \sim {\chi ^2}(n)\\
  > P\{ {\chi ^2}_{1 - \frac{\alpha }{2}}(n) < \frac{{\sum\limits_{i = 1}^n {({X_i} - u} {)^2}}}{{{\sigma ^2}}} < {\chi ^2}_{\frac{\alpha }{2}}(n)\}  = 1 - \alpha \\
  > [\frac{{\sum\limits_{i = 1}^n {({X_i} - u} {)^2}}}{{{\chi ^2}_{\frac{\alpha }{2}}(n)}},\frac{{\sum\limits_{i = 1}^n {({X_i} - u} {)^2}}}{{{\chi ^2}_{1 - \frac{\alpha }{2}}(n)}}]
  > \end{array}$
  
  > （4）u未知，方差 $\sigma^2$ 的置信区间
  > $\begin{array}{l}
  > K = \frac{{(n - 1){S^2}}}{{{\sigma ^2}}} \sim {\chi ^2}(n - 1)\\
  > P\{ {\chi _{1 - \frac{\alpha }{2}}}^2(n - 1) < \frac{{(n - 1){S^2}}}{{{\sigma ^2}}} < {\chi ^2}_{\frac{\alpha }{2}}(n - 1)\}  = 1 - \alpha \\
  > [\frac{{(n - 1){S^2}}}{{{\chi ^2}_{\frac{\alpha }{2}}(n - 1)}},\frac{{(n - 1){S^2}}}{{{\chi ^2}_{1 - \frac{\alpha }{2}}(n - 1)}}]
  > \end{array}$

- 两个正态总体分布
  
  > $(X_1, X_2, \cdots, X_n)$ 为取自总体 $N(u_1, \sigma_1^2)$ 的样本； $(Y_1, Y_2, \cdots, Y_m)$ 为取自总体 $N(u_2, \sigma_2^2)$ 的样本
  > $\overline X, S_1^2; \overline Y, S_2^2$分别表示两个样本的均值和方差，置信度为 $1 - \alpha$
  
  > （1）$\sigma_1^2, \sigma_2^2$ 已知，求 $u_1 - u_2$ 的置信区间
  > $\begin{array}{l}
  > \overline X  \sim N({u_1},\frac{{{\sigma ^2}_1}}{n}),\overline Y  \sim N({u_2},\frac{{{\sigma ^2}_2}}{m}) , \overline X, \overline Y 相互独立\\
  > U = \frac{{(\overline X  - \overline Y ) - ({u_1} - {u_2})}}{{\sqrt {\frac{{{\sigma ^2}_1}}{n} + \frac{{{\sigma ^2}_2}}{m}} }} \sim N(0,1)\\
  > P\{  - {z_{\frac{\alpha }{2}}} \le U \le {z_{\frac{\alpha }{2}}}\}  = P\{  - {z_{\frac{\alpha }{2}}} \le \frac{{(\overline X  - \overline Y ) - ({u_1} - {u_2})}}{{\sqrt {\frac{{{\sigma ^2}_1}}{n} + \frac{{{\sigma ^2}_2}}{m}} }} \le {z_{\frac{\alpha }{2}}}\}  = 1 - \alpha \\
  > [(\overline X  - \overline Y ) - {z_{\frac{\alpha }{2}}}\sqrt {\frac{{{\sigma ^2}_1}}{n} + \frac{{{\sigma ^2}_2}}{m}} ,(\overline X  - \overline Y ) + {z_{\frac{\alpha }{2}}}\sqrt {\frac{{{\sigma ^2}_1}}{n} + \frac{{{\sigma ^2}_2}}{m}} ]
  > \end{array}$
  
  > （2）$\sigma_1^2, \sigma_2^2$ 未知, 但 $\sigma_1^2=\sigma_2^2 = \sigma^2$，求 $u_1 - u_2$ 的置信区间
  > $\begin{array}{l}
  > \overline X  \sim N({u_1},\frac{{{\sigma ^2}_1}}{n}),\overline Y  \sim N({u_2},\frac{{{\sigma ^2}_2}}{m})\\
  > U = \frac{{(\overline X  - \overline Y ) - ({u_1} - {u_2})}}{{\sqrt {\frac{1}{n} + \frac{1}{m}} \sigma }} \sim N(0,1)
  > \end{array}$
  > $\begin{array}{l}
  > \frac{{(n - 1){S^2}_1}}{{{\sigma ^2}}} \sim {\chi ^2}(n - 1)\\
  > \frac{{(m - 1){S^2}_2}}{{{\sigma ^2}}} \sim {\chi ^2}(m - 1)\\
  > V = \frac{{(n - 1){S^2}_1}}{{{\sigma ^2}}} + \frac{{(m - 1){S^2}_2}}{{{\sigma ^2}}} \sim {\chi ^2}(n + m - 2)
  > \end{array}$
  > $T = \frac{U}{{\sqrt {\frac{V}{{n + m - 2}}} }} = \frac{{\frac{{(\overline X  - \overline Y ) - ({u_1} - {u_2})}}{{\sqrt {\frac{1}{n} + \frac{1}{m}} \sigma }}}}{{\sqrt {\frac{{\frac{{(n - 1){S^2}_1}}{{{\sigma ^2}}} + \frac{{(m - 1){S^2}_2}}{{{\sigma ^2}}}}}{{n + m - 2}}} }} = \frac{{(\overline X  - \overline Y ) - ({u_1} - {u_2})}}{{\sqrt {\frac{1}{n} + \frac{1}{m}} \sqrt {\frac{{(n - 1){S^2}_1 + (m - 1){S^2}_2}}{{n + m - 2}}} }} \sim t(n + m - 2)$
  > $\begin{array}{l}
  > P\{  - {t_{\frac{\alpha }{2}}} \le T \le {t_{\frac{\alpha }{2}}}\}  = 1 - \alpha \\
  > (\overline X  - \overline Y ) \pm {t_{\frac{\alpha }{2}}}\sqrt {\frac{1}{n} + \frac{1}{m}} \sqrt {\frac{{(n - 1){S^2}_1 + (m - 1){S^2}_2}}{{n + m - 2}}} 
  > \end{array}$
  
  > （3）$\sigma_1^2, \sigma_2^2$ 未知, 但 n,m > 50，求 $u_1 - u_2$ 的置信区间
  > $\begin{array}{l}
  > \overline X  \sim N({u_1},\frac{{{\sigma ^2}_1}}{n}),\overline Y  \sim N({u_2},\frac{{{\sigma ^2}_2}}{m})\\
  > \frac{{{\sigma ^2}_1}}{n} + \frac{{{\sigma ^2}_2}}{m} \approx \frac{{{S^2}_1}}{n} + \frac{{{S^2}_2}}{m}\\
  > U = \frac{{(\overline X  - \overline Y ) - ({u_1} - {u_2})}}{{\sqrt {\frac{{{S^2}_1}}{n} + \frac{{{S^2}_2}}{m}} }} \sim N(0,1)\\
  > (\overline X  - \overline Y ) \pm {z_{\frac{\alpha }{2}}}\sqrt {\frac{{{S^2}_1}}{n} + \frac{{{S^2}_2}}{m}} 
  > \end{array}$
  
  > （4） $u_1,u_2$ 已知，求方差比 $\frac {\sigma_1^2} {\sigma_2^2}$ 的置信区间
  > $\begin{array}{l}
  > F = \frac{{\frac{1}{n}\sum\limits_{i = 1}^n {\frac{{{{({X_i} - {u_1})}^2}}}{{{\sigma ^2}_1}}} }}{{\frac{1}{m}\sum\limits_{i = 1}^m {\frac{{{{({Y_i} - {u_2})}^2}}}{{{\sigma ^2}_2}}} }} = \frac{{\frac{m}{n}\frac{{\sum\limits_{i = 1}^n {{{({X_i} - {u_1})}^2}} }}{{\sum\limits_{i = 1}^m {{{({Y_i} - {u_2})}^2}} }}}}{{\frac{{{\sigma ^2}_1}}{{{\sigma ^2}_2}}}} \sim F(n,m)\\
  > [\frac{{\frac{m}{n}\frac{{\sum\limits_{i = 1}^n {{{({X_i} - {u_1})}^2}} }}{{\sum\limits_{i = 1}^m {{{({Y_i} - {u_2})}^2}} }}}}{{{F_{\frac{\alpha }{2}}}(n,m)}},\frac{{\frac{m}{n}\frac{{\sum\limits_{i = 1}^n {{{({X_i} - {u_1})}^2}} }}{{\sum\limits_{i = 1}^m {{{({Y_i} - {u_2})}^2}} }}}}{{{F_{1 - \frac{\alpha }{2}}}(n,m)}}]
  > \end{array}$
  
  > （5）$u_1,u_2$ 未知，求方差比 $\frac {\sigma_1^2} {\sigma_2^2}$ 的置信区间
  > $\begin{array}{l}
  > \frac{{(n - 1){S^2}_1}}{{{\sigma _1}^2}} \sim {\chi ^2}(n - 1)\\
  > \frac{{(m - 1){S^2}_2}}{{{\sigma _2}^2}} \sim {\chi ^2}(m - 1)\\
  > F = \frac{{\frac{{(n - 1){S^2}_1}}{{{\sigma _1}^2(n - 1)}}}}{{\frac{{(m - 1){S^2}_2}}{{{\sigma _2}^2(m - 1)}}}} = \frac{{\frac{{{S^2}_1}}{{{S^2}_2}}}}{{\frac{{{\sigma _1}^2}}{{{\sigma _2}^2}}}} \sim F(n - 1,m - 1)\\
  > [\frac{{{S^2}_1}}{{{S^2}_2}}\frac{1}{{{F_{\frac{\alpha }{2}}}(n - 1,m - 1)}},\frac{{{S^2}_1}}{{{S^2}_2}}\frac{1}{{{F_{1 - \frac{\alpha }{2}}}(n - 1,m - 1)}}]
  > \end{array}$

## 火车头数量估计问题

# 假设检验

> 在统计推断中，会有两种类型的问题：（1）知道了总体的分布，但是其中有未知的参数，此时可以对未知的参数作出某种假设，然后利用样本的信息和数据对事先提出的假设进行检验。例如，我们知道了某学校学生的身高服从正态分布，但是不知道平均的身高是多少，此时可以给出一个假设，假设平均身高是1.68米，然后从总体中抽出一个样本，以样本的数据对事先提出1.68的这个假设可靠程度有多大（2）不知道总体的分布，可以根据某些信息或者数据事先认为它是某种分布的假设。比如说某个车站在12点等候车子的人数服从泊松分布，那么可以抽取一个样本来检验它是否是一个泊松分布

- 对参数进行假设检验

  > （1）对参数一无所知，用参数估计的方法进行处理，比如参数估计中的点估计、区间估计
  > （2）若对总体未知的参数有所了解，比如根据经验或者已经得到的信息有所推测，但并不能完全确认需要证实，可以抽出一个样本的信息假设检验的方法来处理

## 假设检验的基本概念

> 假设检验定义：是指施加于一个或多个总体的概率分布或者参数的假设。所有的假设可以是正确的，也可以使错误的；为判断所做的假设是否正确，从总体中抽取样本，根据样本的取值，按一定的原则进行检验，然后做出接受或者拒绝所做假设的决定

> 假设检验的内容
> （1）参数检验：总体均值、均值差的检验；总体方差、方差比的检验
> （2）非参数检验：分布拟合检验；符号检验；秩和检验

> 假设检验的理论依据
> 其理论背景为实际推断原理，即“小概率事件”

- 零假设

  > 零假设即为原假设记作 $H_0$；原假设的对立面成为备择假设，记为 $H_1$; 假设的任务就是要在原假设与备择假设之间做一个选择。

- 对立假设

- 显著水平

- 小概率事件

- 两类错误

  > 在给定 $\alpha$ 的前提下，接受还是拒绝原假设完全取决于样本值，因此检验可能会犯两类错误
  > 第一类错误: 弃真错误，概率通常记为 $\alpha$
  > 第二类错误: 取伪错误，概率通常记为 $\beta$

  > 任何检验方法都不可能完全排除犯错误的可能性。理想的检验方法应使犯两类错误的概率都很小，但在样本容量给定的情况下，不可能两者都很小，降低一个，往往使另一个增大；
  > 假设检验的指导思想：是控制犯第一类错误的概率不超过 $\alpha$; 然后，通过增加样本容量的方法来减少 $\beta$

- 拒绝域

- 样本容量

## 已知分布, 对参数的假设检验

### 单正态总体均值、方差的检验

### 双正态总体均值、方差的检验

## 对分布的假设检验

### 拟合优度检验

# 方差分析

# 回归分析
