# 中心力场

本文从最基本的拉格朗日方程，来推导在中心力场（地球-太阳系统）下的行星运行轨迹（椭圆轨道，开普勒第一定律）。讨论将不局限于三维（各向同性）空间，并推广到二维、四维。

## 地日中心保守力场

### 受力分析

为了推导地球轨道，考虑地球的受力：

1. 星际尘埃的阻尼：产生与速度方向相反的切向受力分量
2. 太阳风和光压：仍然是中心力场，但是能量不守恒
3. 木星等其他星体的拉扯：角动量不守恒
4. 地球不是一个质点：受太阳潮汐力

由于距离较远，地球-太阳可简化为二体质点系统，并且假设能量守恒和角动量守恒。

地日系统的质量中心不是太阳中心，太阳也作回归运动。但为方便讨论，暂设太阳固定在坐标原点。读者读完本篇后，可进一步把太阳回归运动考虑进来，能得到类似形式的解。

### 2、3、4 维空间引力公式

三维均匀各向同性空间（以下简称三维空间）中，把太阳看作一个质点，地日之间的万有引力随距离的平方衰减：

$$F=-\frac{GMm}{r^{2}}$$

其中 \(G\) 为引力常数，\(M\) 是太阳质量，\(m\) 是地球质量，\(r\) 是地日距离。

用矢量表示：

$$m\ddot{\mathbf{r}} =\mathbf{F} =-\frac{GMm}{| \mathbf{r}| ^{3}}\mathbf{r}$$

其中，粗体表示矢量，\(\ddot{\mathbf{r}}\) 表示位置矢量对时间的二次微分（加速度）。

将讨论推广到其他维度，总结如下：

| 维度 | 引力                 | 引力势 \(U(r)\)         |
| ---- | -------------------- | --------------------- |
| 2    | $-\frac{GMm}{r}$     | $GMm\ln{r}+C$         |
| 3    | $-\frac{GMm}{r^{2}}$ | $-\frac{GMm}{r}$      |
| 4    | $-\frac{GMm}{r^{3}}$ | $-\frac{GMm}{2r^{2}}$ |

力与势能的关系：

$$\mathbf{F} =-\nabla U$$

## 中心力场的拉格朗日表示

在极坐标下，拉格朗日函数：

$$ L(r,\theta) = \tfrac{1}{2} m\dot{r}^{2} + \tfrac{1}{2} mr^{2}\dot{\theta}^{2} - U(r) $$

径向动量：

$$ p_{r} = \frac{\partial L}{\partial \dot{r}} = m\dot{r} $$

切向动量：

$$ p_{\theta} = \frac{\partial L}{\partial \dot{\theta}} = mr^{2}\dot{\theta} $$

径向“力”：

$$ F_{r} = \frac{\partial L}{\partial r} = mr\dot{\theta}^{2} - \frac{d}{dr} U(r) $$

拉格朗日方程：

- 径向：

$$ mr\dot{\theta}^{2} - \frac{d}{dr} U(r) = m\ddot{r} $$

- 切向（角动量守恒）：

$$ 0 = \frac{d}{dt} (mr^{2}\dot{\theta}) \quad \Rightarrow \quad mr^{2}\dot{\theta} = M_{0} $$

参考**链式法则** [chain-rule.md](chain-rule.md)。根据角动量守恒消去时间隐变量，并作倒数替换，可得径向方程化为 Binet 方程（参见[维基条目](https://wuli.wiki/online/Binet.html)）：

$$ -\frac{M_{0}^{2} u^{2}}{m}\frac{d^{2} u}{d\theta ^{2}} -\frac{M_{0}^{2}}{m} u^{3} -u^{2}\frac{d}{du} U\!\left( \tfrac{1}{u}\right) =0 $$

约去公因子，得：

$$ \frac{d^{2} u}{d\theta ^{2}} + u + \frac{m}{M_{0}^{2}}\frac{d}{du} U\!\left( \tfrac{1}{u}\right) = 0 $$

## 3 维空间行星轨道

已知三维空间的引力势能：

$$ U = -\frac{GMm}{r} = -GMmu $$

因此：

$$ \frac{d}{du} U\!\left( \tfrac{1}{u}\right) = -GMm $$

代回可得：

$$ \frac{d^{2} u}{d\theta ^{2}} + u = \frac{GMm^{2}}{M_{0}^{2}} $$

这是二阶非齐次常系数线性微分方程，通解为：

$$ \frac{1}{r} = u = C_{3}\cos \theta + C_{4}\sin \theta + \frac{GM}{C_{1}^{2}} = (e\cos (\theta + \theta_{0}) + 1)\,\frac{GMm^{2}}{M_{0}^{2}} $$

写成倒数形式：

$$ r = \frac{M_{0}^{2}}{GMm^{2}}\,\frac{1}{1 + e\cos(\theta + \theta_{0})} $$

即为标准的圆锥曲线方程，坐标原点是圆锥曲线的一个焦点。

历史上，开普勒历经多年在 1609 年提出行星运动三定律。基于牛顿力学与微积分，上式可较为直接地导出圆锥曲线轨道解，显示出数学工具在物理研究中的重要性。

## 4 维空间行星轨道（概要）

四维空间引力势能：

$$ U = -\frac{GMm}{2r^{2}} = -\frac{GMm u^{2}}{2} $$

可得：

$$ \frac{d}{du} U\!\left( \tfrac{1}{u}\right) = -GMm u $$

代回得到：

$$ \frac{d^{2} u}{d\theta ^{2}} + \left( 1 - \frac{GMm^{2}}{M_{0}^{2}} \right) u = 0 $$

更详细讨论见：[4d-planet-orbit.md](4d-planet-orbit.md)。

## 2 维空间行星轨道（概要）

二维空间引力势能：

$$ U = GMm\ln r = -GMm\ln u $$

变量替换得到：

$$ \frac{d}{du} U\!\left( \tfrac{1}{u}\right) = -\frac{GMm}{u} $$

代入得到：

$$ \frac{d^{2} u}{d\theta ^{2}} + u - \frac{GMm^{2}}{M_{0}^{2} u} = 0 $$

该方程非线性，无解析解。根据势能形式，在无穷远处势能发散，因此有限动能的行星轨道不会到达无穷远。

## 智慧生命诞生的可能

从上述分析可见：

- 4 维宇宙：不稳定，行星要么坠落恒星，要么飞至无穷远，难以产生长期稳定环境。
- 2 维宇宙：宇宙不会无限膨胀，恒星与行星会因引力束缚在有限距离内，连光也可能无法贯穿整个宇宙。
- 3 维宇宙：束缚态行星可稳定环绕恒星，具备充足时间，是智慧生命演化的理想环境。

这从人择原理角度亦可理解：为何弦理论预言 9 维空间，而我们观测到的宏观空间为 3 维。

当然，也可设想：虽在 4 维空间二体难以稳定，但复杂的三体或多体相互作用，或许在极小概率下产生长时间准稳定构型。

## 参考

- https://www.bilibili.com/video/BV1aL4y1678A
- https://zhuanlan.zhihu.com/p/1953971141803750793
- https://wuli.wiki/online/Binet.html
- https://github.com/julianShi/math-calculus/blob/planet-orbit/07-differential-equation/planet-orbits.md

## 附录

- 免费网页 SymPy 符号计算器 [sympy-calculator.md](sympy-calculator.md)
- 免费网页 Desmos 画图工具 [desmos-plot.md](desmos-plot.md)

## SymPy 验证

请参考 [../README.md](../README.md) 访问在线 SymPy 环境，并执行 [central-force.ipynb](central-force.ipynb) 代码
