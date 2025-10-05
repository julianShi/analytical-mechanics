## 二维弹簧振子

假设水平桌面上有一个拴在固定点上的二维弹簧振子，自然长度为 $l$ 。那么其拉格朗日量为

$\displaystyle L=T-U=\frac{1}{2} mv_{x}^{2} +\frac{1}{2} mv_{y}^{2} -\frac{1}{2} k\left(\sqrt{x^{2} +y^{2}} -l\right)^{2}$

显然，用极坐标表示更加简洁

$\displaystyle L( r,\theta ) =\frac{1}{2} m\dot{r}^{2} +\frac{1}{2} mr^{2}\dot{\theta }^{2} -\frac{1}{2} k( r-l)^{2}$

于是得到，径向动量

$\displaystyle p_{r} =\frac{\partial L}{\partial \dot{r}} =m\dot{r}$

切向动量

$\displaystyle p_{\theta } =\frac{\partial L}{\partial \dot{\theta }} =mr^{2}\dot{\theta }$

径向力

$\displaystyle F_{r} =\frac{\partial L}{\partial r} =mr\dot{\theta }^{2} -k( r-l)$

则得到两组拉格朗日方程

径向

$\displaystyle mr\dot{\theta }^{2} -k( r-l) =\frac{d}{dt} m\dot{r} =m\ddot{r}$

切向

$\displaystyle 0=\frac{d}{dt} mr^{2}\dot{\theta } ,mr^{2}\dot{\theta } =M_{0}$

说明角动量 $\displaystyle M_{0}$ 守恒

代回径向方程，消去角度项

$\displaystyle mr\left(\frac{M_{0}}{mr^{2}}\right)^{2} -k( r-l) =m\ddot{r}$

移项，得到关于 $\displaystyle r( t)$ 的二阶非线性方程

$\displaystyle m\ddot{r} +kr-\frac{M_{0}^{2}}{mr^{3}} =kl$

## SymPy 验证

请参考 [../README.md](../README.md) 访问在线SymPy环境，并执行 [spring-mass.ipynb](spring-mass.ipynb) 代码

