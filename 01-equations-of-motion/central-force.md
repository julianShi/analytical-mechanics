本文从最基本的拉格朗日方程，来推导在中心力场（地球-太阳系统）下的行星运行轨迹（椭圆轨道，开普勒第一定律）。讨论将不局限于三维（各项同性）空间。将推广到二维，四维。

## 地日中心保守力场

### 受力分析

为了推导地球轨道，考虑地球的受力：

1. 星际尘埃的阻尼：产生和速度方向相反的切向受力分量
2. 太阳风和光压：仍然是中心力场，但是能量不守恒
3. 木星等其他星体的拉扯：角动量不守恒
4. 地球不是一个质点：受太阳潮汐力

但是因为距离较远，地球-太阳 可简化为 二体质点系统，并且假设能量守恒和角动量守恒。

地日系统的质量中心不是太阳中心，太阳也作回归运动。但是为了方便讨论，假设太阳被固定在坐标原点。读者读完本篇之后，可以把太阳回归运动也考虑进来，也能得到类似形式的解。

### 2，3，4维空间引力公式

三维均匀各向同性空间（以下简称三位空间）中，把太阳看作一个质点的话，地日之间的万有引力随距离的平方衰减

$$F=-\frac{GMm}{r^{2}}$$

其中 $G$ 为引力常数， $M$ 是太阳质量， $m$ 是地球质量， $r$ 是地日距离

用矢量表示的话，

$$m\ddot{\mathbf{r}} =\mathbf{F} =-\frac{GMm}{| \mathbf{r}| ^{3}}\mathbf{r}$$

其中，粗体表示矢量， $$\ddot{\mathbf{r}}$$ 表示 位置矢量 对时间的二次微分，即加速度。

将讨论推广到其他维度，总结如下

| 维度 | 引力                 | 引力势 $U(r)$         |
| ---- | -------------------- | --------------------- |
| 2    | $-\frac{GMm}{r}$     | $GMm\ln{r}+C$         |
| 3    | $-\frac{GMm}{r^{2}}$ | $-\frac{GMm}{r}$      |
| 4    | $-\frac{GMm}{r^{3}}$ | $-\frac{GMm}{2r^{2}}$ |

其力和势能的关系是

$\mathbf{F} =-\nabla U$

## 中心力场拉格朗日表示

用极坐标表示 拉格朗日函数

$\displaystyle L( r,\theta ) =\frac{1}{2} m\dot{r}^{2} +\frac{1}{2} mr^{2}\dot{\theta }^{2} -U( r)$

重复 上一节步骤得到，径向动量

$\displaystyle p_{r} =\frac{\partial L}{\partial \dot{r}} =m\dot{r}$

切向动量

$\displaystyle p_{\theta } =\frac{\partial L}{\partial \dot{\theta }} =mr^{2}\dot{\theta }$

径向力

$\displaystyle F_{r} =\frac{\partial L}{\partial r} =mr\dot{\theta }^{2} -\frac{d}{dr} U( r)$

则得到两组拉格朗日方程

径向

$\displaystyle mr\dot{\theta }^{2} -\frac{d}{dr} U( r) =m\ddot{r}$

切向

$\displaystyle 0=\frac{d}{dt} mr^{2}\dot{\theta } ,mr^{2}\dot{\theta } =M_{0}$

其中 $M_0$ 是行星角动量。通常写作 $L$ ，为了避免和拉格朗日量混淆，所以用 $M_0$

参考**链式法则** [chain-rule.md](chain-rule.md) 

根据角动量守恒消去时间隐变量，并作导数替换，原径向拉格朗日方程变成

$\displaystyle -\frac{M_{0}^{2} u^{2}}{m}\frac{d^{2} u}{d\theta ^{2}} -\frac{M_{0}^{2}}{m} u^{3} -u^{2}\frac{d}{du} U( 1/u) =0$

除以 公约项，得到如下简洁的二阶微分方程，也叫比耐 Binet 方程  https://wuli.wiki/online/Binet.html

$\displaystyle \frac{d^{2} u}{d\theta ^{2}} +u+\frac{m}{M_{0}^{2}}\frac{d}{du} U( 1/u) =0$

## 3维空间行星轨道

已知三维空间的引力势能

$\displaystyle U=-\frac{GMm}{r} =-GMmu$

那么

$\displaystyle \frac{d}{du} U( 1/u) =-GMm$

得到

$\displaystyle \frac{d^{2} u}{d\theta ^{2}} +u=\frac{GMm^{2}}{M_{0}^{2}}$

这是 二阶非齐次常系数线性微分方程，有通解

$$\frac{1}{r} =u=C_{3}\cos \theta +C_{4}\sin \theta +\frac{GM}{C_{1}^{2}} = (e\cos (\theta +\theta _{0} )+1)\frac{GMm^{2}}{M_0^{2}}$$

其中 待定系数 $e$ 是偏心率。写成 倒数形式

$$ r=\frac{M_0^{2}}{GMm^{2}}\frac{1}{1+e\cos (\theta +\theta _{0} )} $$

即为标准的圆锥曲线方程。坐标原点是圆锥曲线的一个焦点。

这即是开普勒辛辛苦苦花费8年，1609年才拼凑出来的行星轨道。而我们用1665年牛顿发明微积分，8分钟就求解出了圆锥曲线轨道解。可见，物理人掌握先进的数学工具有多么重要。珍惜生命，学好数学。

## 4维空间行星轨道

已知三维空间的引力势能

$\displaystyle U=-\frac{GMm}{2r^{2}} =-\frac{GMmu^{2}}{2}$

微分

$\displaystyle \frac{d}{du} U( 1/u) =-GMmu$

得到

$\displaystyle \frac{d^{2} u}{d\theta ^{2}} +\left( 1-\frac{GMm^{2}}{M_{0}^{2}}\right) u=0$

这是二元齐次常系数线性微分方程。

因为力学中常用 $L$ ，而不是 $M_0$ 表示角动量，所以如下讨论沿用 $L$ 表示角动量，而不是拉格朗日量。

根据其特征根的正负号，作如下讨论

### 自由态

角动量大的时候

$$1-\frac{GMm^2}{L^{2}}  >0$$ 

有通解

$$\frac{1}{r} =u=C_{6}\cos\left(\sqrt{1-\frac{GMm^{2}}{L^{2}}} \theta +\theta _{0}\right)$$

### 临界态

角动量刚好的时候

$$1-\frac{GMm^2}{L^{2}} =0$$

有通解

$$\frac{1}{r} =u=C_{7} +C_{8} \theta $$

是一条螺旋线。当 $C_8>0$  行星旋出。当 $C_8<0$  行星旋进。当 $C_8=0$  行星是不稳定的圆形轨道。

如果旋进的话，行星会不会旋进到太阳呢？

对通解两侧对时间微分

$$-\frac{1}{r^{2}}\dot{r} =C_{8}\dot{\theta }$$

代入动量公式

$$L=mr^{2}\dot{\theta }$$

消去角度，得到

$$-\frac{1}{r^{2}}\dot{r} =C_{8}\dot{\theta } =\frac{C_{8} L}{mr^{2}}$$

消去相同因式，得到

$$\dot{r} =-\frac{C_{8} L}{m}$$

积分得到

$$r( t) =R_0-\frac{C_{8} L}{m} t$$

即行星会以恒定径向速度，坠入恒星（角速度越来越快），或者远离恒星。

### 束缚态

角动量小的时候

 $1-\frac{GMm^2}{L^{2}} < 0$ 

有通解

$$\frac{1}{r} =u=C_{7}\exp\left(\sqrt{\frac{GMm^{2}}{L^{2}} -1} \theta \right) +C_{8}\exp\left( -\sqrt{\frac{GMm^{2}}{L^{2}} -1} \theta \right)$$

假设 $\theta(t)$ 单调递增。

当 $C_7C_8>0$ ，即同号 ， $r$ 有最大值。意味着，即使行星刚开始旋出，也会随后旋入，最终坠落到恒星。

当 $C_7 C_8<0$  ， $r$ 无最大值。意味着，即使行星旋出的话，将以渐近线的方式运动到无穷远。

当 $C_7C_8=0$  ，行星轨道退化成螺旋线

### 总结

| 分类   | 判定  | 3维轨道 | 判定        | 4维轨道            |
| ------ | ----- | ------- | ----------- | ------------------ |
| 自由态 | $T>V$ | 双曲线  | $L^2>GMm^2$ | 可相交渐近线       |
| 临界态 | $T=V$ | 抛物线  | $L^2=GMm^2$ | 螺旋线             |
| 束缚态 | $T<V$ | 椭圆    | $L^2<GMm^2$ | 首尾在原点的螺旋线 |

## 2维空间行星轨道

已知2维空间引力势能

$\displaystyle U=GMm\ln r=-GMm\ln u$

变量替换得到

$\displaystyle \frac{d}{du} U( 1/u) =-\frac{GMm}{u}$

代入拉格朗日方程

$\displaystyle \frac{d^{2} u}{d\theta ^{2}} +u-\frac{GMm^{2}}{M_{0}^{2} u} =0$

这不是线性方程，没有解析解。但是根据其引力势场表达式知道，在无穷远处为无穷大，所以知道，对于有限动能的行星，其轨道一定不会到无穷远。

## 智慧生命诞生的可能

可以从上述分析看出来：

- 4维宇宙：相当不稳定，行星要么坠落到恒星，要么飞到无穷远。难以产生智慧生命进化的稳定环境。
- 2维宇宙：宇宙不会永远膨胀下去。恒星行星会因为彼此引力的束缚，而约束在有限距离内。甚至连光，都无法穿过整个宇宙。
- 3维宇宙：束缚态的行星能够稳定地环绕恒星，有充足的时间，是智慧生命进化的完美家园。

这也从人择原理解释了，为什么弦理论预言了9维空间，但是宇宙对我们隐藏了额外的6个维度。

当然，也可以乐观地考虑，虽然4维空间中，二体运动很难有稳定轨道。但是复杂的三体或者多体运动，或许能给4维空间增色。即，在极小的概率下，三颗自由态的星体靠近，其中一颗窃取系统的总动能，被弹射出去，剩下两颗刚好处于临界状态，说不定也能维持相当长时间的圆周运动，给智慧生命进化创造稳定的环境。

## 参考

https://www.bilibili.com/video/BV1aL4y1678A

https://zhuanlan.zhihu.com/p/1953971141803750793

https://wuli.wiki/online/Binet.html

https://github.com/julianShi/math-calculus/blob/planet-orbit/07-differential-equation/planet-orbits.md

## 附录

免费网页SymPy符号计算器 [sympy-calculator.md](sympy-calculator.md)

免费网页Desmos画图工具 [desmos-plot.md](desmos-plot.md)

