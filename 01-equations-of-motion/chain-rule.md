## 链式法则

### 回顾

在《高等数学》微分章节中，我们学过复合函数求导的链式法则。即，对于复合函数

$\displaystyle z( y( x))$

其导数满足链式法则

$\displaystyle \frac{dz}{dx} =\frac{dy}{dx}\frac{dz}{dy}$

### 中心力场消去时间隐变量

在极坐标中求解轨道的时候，由于我们关心的不是坐标作为时间的函数 $r(t)$ ，而是坐标之间的约束方程 $\displaystyle r( \theta )$，所以我们将对时间的一次微分写成对角度的微分

$\displaystyle \dot{r} = \frac{dr}{dt} =\frac{d\theta }{dr}\frac{dr}{d\theta } =\dot{\theta }\frac{dr}{d\theta }$

然后代入角动量守恒方程

$mr^2\dot{\theta} = M_0$

得到

$\displaystyle \dot{r} = \frac{M_{0}}{mr^{2}}\frac{dr}{d\theta }$


然后，对时间二次微分

$\displaystyle \ddot{r} =\frac{d}{dt}\left(\frac{M_{0}}{mr^{2}}\frac{dr}{d\theta }\right) =\dot{\theta }\frac{d}{d\theta }\left(\frac{M_{0}}{mr^{2}}\frac{dr}{d\theta }\right)$

中心力场动量守恒方程替换

$\ddot{r} =\frac{M_{0}}{mr^{2}}\frac{d}{d\theta }\left(\frac{M_{0}}{mr^{2}}\frac{dr}{d\theta }\right)$

函数积的求导法则

$\displaystyle \ddot{r} =\frac{M_{0}}{mr^{2}}\frac{dr}{d\theta }\frac{d}{d\theta }\left(\frac{M_{0}}{mr^{2}}\right) +\frac{M_{0}}{mr^{2}}\frac{M_{0}}{mr^{2}}\frac{d}{d\theta }\left(\frac{dr}{d\theta }\right)$

cont.

$\displaystyle \ddot{r} =\frac{M_{0}}{mr^{2}}\left(\frac{dr}{d\theta }\right)^{2}\left(\frac{-2M_{0}}{mr^{3}}\right) +\frac{M_{0}}{mr^{2}}\frac{M_{0}}{mr^{2}}\frac{d^{2} r}{d\theta ^{2}}$

cont.

$\displaystyle \ddot{r} =-\frac{2M_{0}^{2}}{m^{2} r^{5}}\left(\frac{dr}{d\theta }\right)^{2} +\frac{M_{0}^{2}}{m^{2} r^{4}}\frac{d^{2} r}{d\theta ^{2}}$

### 倒数替换

并且作替换 $\displaystyle r=1/u$

则其微分算号

$\displaystyle \frac{d}{dr} =\frac{du}{dr}\frac{d}{du} =-\frac{1}{r^{2}}\frac{d}{du} =-u^{2}\frac{d}{du}$

并且，通过链式法则，类似得到 一次微分

$\displaystyle \frac{dr}{d\theta } =\frac{du}{d\theta }\frac{dr}{du} =\frac{du}{d\theta }\left( -\frac{1}{u^{2}}\right)$

二次微分

$\displaystyle \frac{d^{2} r}{d\theta ^{2}} =\frac{d}{d\theta }\left[\frac{du}{d\theta }\left( -\frac{1}{u^{2}}\right)\right] =-\frac{1}{u^{2}}\frac{d}{d\theta }\frac{du}{d\theta } +\frac{du}{d\theta }\frac{d}{d\theta }\left( -\frac{1}{u^{2}}\right)$

cont.

$\displaystyle \frac{d^{2} r}{d\theta ^{2}} =-\frac{1}{u^{2}}\frac{d^{2} u}{d\theta ^{2}} +\left(\frac{du}{d\theta }\right)^{2}\left(\frac{2}{u^{3}}\right)$

代回原表达式

$\displaystyle \ddot{r} =-\frac{2M_{0}^{2} u^{5}}{m^{2}}\left(\frac{1}{u^{4}}\frac{du}{d\theta }\right)^{2} +\frac{M_{0}^{2} u^{4}}{m^{2}}\left[ -\frac{1}{u^{2}}\frac{d^{2} u}{d\theta ^{2}} +\left(\frac{du}{d\theta }\right)^{2}\left(\frac{2}{u^{3}}\right)\right]$

cont.

$\displaystyle \ddot{r} =-\frac{M_{0}^{2} u^{2}}{m^{2}}\frac{d^{2} u}{d\theta ^{2}}$

