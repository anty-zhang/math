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

# 大数定律以中心极限定理

## 两种收敛性概念

> 微积分种的收敛性，是依 "距离" 进行收敛性的判断; 而此处的收敛性是依 "概率" 进行收敛性的判断

### 依概率收敛

> 设 $X_1,X_2,\cdots, X_n, \cdots$ 是随机变量的序列，X是某一个随机变量(或者常数)， 对于 $\forall \epsilon > 0$, 若
> $\begin{array}{l}
> \mathop {\lim }\limits_{n \to \infty } P\{ |{X_n} - X| < \varepsilon \}  = 1 \\ 或
> \mathop {\lim }\limits_{n \to \infty } P\{ |{X_n} - X| \geqslant \varepsilon \}  = 0 \\ 
> \end{array}$, 则称随机序列 ${X_i}, i=1,2,3,...$依概率收敛于X，记做 ${X_n} \xrightarrow {P}X$

### 依分布收敛

> 设 $X_1,X_2,\cdots, X_n, \cdots$ 是随机变量的序列，X是某一个随机变量， $F_n(x)是X_n d的分布函数, i=1,2,3,...; F(x)是X的分布函数$
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

> 概率的统计学定义的合理性(随机现象的统计学规律：在相同的条件下进行大量的重复实验才能显现出来)

- 定义

> 设有随机变量序列 $\{X_i \}, i=1,2,3,\cdots; E(X_i), i =1,2,3, \cdots$都存在，若对 $\forall \epsilon > 0$
> 有: $\mathop {\lim} \limits_{n->\infty} P \{ |\frac {1} {n} \sum_{i=1}^n X_i - \frac {1} {n} \sum_{i=1}^n E(X_i)| < \epsilon \} = 1$
> 则称 \{X_i\} 服从大数定律。即 ($\frac {1} {n} \sum_{i=1}^n X_i - \frac {1} {n} \sum_{i=1}^n E(X_i) \xrightarrow {P} 0$)

> 大叔定律说明来算数平均值及频率(随着实验次数趋于无穷大)的稳定性

- 常见的大数定律

> （1）切比雪夫大数定律
> 
> （2）独立同分布
> 
> （3）伯努利

- 小概率事件原理

## 中心极限定理

> 正太分布的重要性

# 抽样分布理论

# 描述统计

# 参数估计

# 假设试验

# 方差分析

# 回归分析
