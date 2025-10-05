## 链式法则

### 回顾

在《高等数学》微分章节中，我们学过复合函数求导的链式法则。即，对于复合函数

$\displaystyle z\big(y(x)\big)$

其导数满足链式法则：

$\displaystyle \frac{dz}{dx} = \frac{dz}{dy}\,\frac{dy}{dx}$

### 中心力场消去时间隐变量

在极坐标中求解轨道时，我们关心的是坐标之间的约束关系 \(r(\theta)\) 而非 \(r(t)\)。因此将对时间的一次微分转写为对角度的微分：

$\displaystyle \dot{r} = \frac{dr}{dt} = \frac{dr}{d\theta}\,\frac{d\theta}{dt} = \dot{\theta}\,\frac{dr}{d\theta}$

结合角动量守恒：

$mr^2\dot{\theta} = M_0$

可得：

$\displaystyle \dot{r} = \frac{M_{0}}{mr^{2}}\,\frac{dr}{d\theta}$

然后对时间再微分：

$\displaystyle \ddot{r} = \frac{d}{dt}\left(\frac{M_{0}}{mr^{2}}\,\frac{dr}{d\theta}\right) = \dot{\theta}\,\frac{d}{d\theta}\left(\frac{M_{0}}{mr^{2}}\,\frac{dr}{d\theta}\right)$

再由角动量守恒替换 \(\dot{\theta} = M_0/(mr^2)\)：

$\ddot{r} = \frac{M_{0}}{mr^{2}}\,\frac{d}{d\theta}\left(\frac{M_{0}}{mr^{2}}\,\frac{dr}{d\theta}\right)$

对乘积求导并化简：

$\displaystyle \ddot{r} = \frac{M_{0}}{mr^{2}}\,\frac{dr}{d\theta}\,\frac{d}{d\theta}\!\left(\frac{M_{0}}{mr^{2}}\right) + \left(\frac{M_{0}}{mr^{2}}\right)^{2}\,\frac{d^{2} r}{d\theta ^{2}}$

### 倒数替换

作替换 \(r=1/u\)。则有微分算子：

$\displaystyle \frac{d}{dr} = \frac{du}{dr}\,\frac{d}{du} = -\frac{1}{r^{2}}\,\frac{d}{du} = -u^{2}\,\frac{d}{du}$

由链式法则得到：

$\displaystyle \frac{dr}{d\theta } = \frac{du}{d\theta }\,\frac{dr}{du} = \frac{du}{d\theta }\left( -\frac{1}{u^{2}}\right)$

以及

$\displaystyle \frac{d^{2} r}{d\theta ^{2}} = -\frac{1}{u^{2}}\,\frac{d^{2} u}{d\theta ^{2}} + \frac{2}{u^{3}}\left(\frac{du}{d\theta }\right)^{2}$

代回并整理，可得经典结果：

$\displaystyle \ddot{r} = -\frac{M_{0}^{2} u^{2}}{m^{2}}\,\frac{d^{2} u}{d\theta ^{2}}$

## 代码验证

用 SymPy 可以验证上述推导过程。请安装环境，并尝试执行：

[chain-rule.ipynb](chain-rule.ipynb)
