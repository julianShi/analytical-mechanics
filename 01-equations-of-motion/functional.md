## 变分

定义：和自变量 $x$ 的微小变化不同，变分符号表示的是函数 $y$ 的微小变化

$\displaystyle \delta y=y_{1}( x) -y_{2}( x)$

比方说 

$y_1(x)=e^{x}, y_2(x)=1+x+\frac{x^2}{2}$

定理：变分符号和导数符号相互独立，满足交换性

$\displaystyle \delta ( y') =y_{1} '( x) -y_{2} '( x) =[ y_{1}( x) -y_{2}( x)] '=( \delta y) '$



## 积分形泛函

定义：介绍一种特殊的，最高阶为一阶的泛函，也叫最简泛函

$\displaystyle J=\int _{x_{1}}^{x_{2}} F( x,y( x) ,y'( x)) dx$

其一阶变分是

$\displaystyle \delta J=\int _{x_{1}}^{x_{2}}[ F_{y} \delta y+F_{y'} \delta y'] dx$



定理：如果 $\displaystyle F$ 光滑（二阶偏导数连续），那么使得最简泛函取对于任意 $\displaystyle \delta y$ 取极值的充分必要条件是 欧拉方程

$\displaystyle F_{y} =\frac{d}{dx} F_{y'}$

证明：

根据分部积分公式

$\displaystyle \int udv=uv-\int vdu$

令

$\displaystyle u=F_{y'} ,dv=\delta y'dx=d\delta y$

则有

$\displaystyle \int _{x_{1}}^{x_{2}} F_{y'} \delta y'dx=F_{y'} \delta y|_{x_{1}}^{x_{2}} -\int _{x_{1}}^{x_{2}} \delta y\frac{dF_{y'}}{dx} dx$

根据固定边界条件

$\displaystyle \delta y( x_{1}) =\delta y( x_{2}) =0$

以及泛函取极值的题设，有

$\displaystyle \delta L=\int _{x_{1}}^{x_{2}}[ F_{y} \delta y+F_{y'} \delta y'] dx=\int _{x_{1}}^{x_{2}}\left[ F_{y} \delta y-\delta y\frac{dF_{y'}}{dx}\right] dx=0$

即得到

$\displaystyle \delta y\left( F_{y} -\frac{dF_{y'}}{dx}\right) =0$

证毕