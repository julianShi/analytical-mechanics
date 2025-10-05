## 角动量守恒

证明：

在空间中定义任意转轴 $\displaystyle \varphi $，那么对于封闭的质点系，有

$\displaystyle \delta \mathbf{r} =\delta \mathbf{\varphi } \times \mathbf{r}$

其中，$\displaystyle \delta \mathbf{\varphi }$ 是人为引入的参考系变化。粗体表示是（三维）矢量。

对上式进行时间微分

$\displaystyle \delta \mathbf{v} =\delta \mathbf{\varphi } \times \mathbf{v}$

将其带入拉格朗日函数

$\displaystyle \delta L=\sum _{i}\left(\frac{\partial L}{\partial \mathbf{r}_{i}} \cdot \delta \mathbf{r}_{i} +\frac{\partial L}{\partial \mathbf{v}_{i}} \cdot \delta \mathbf{v}_{i}\right) =0$

其中，下标 $i$ 表示质点系中的第 $i$ 个质点。

用广义动量表示，则是

$\displaystyle \sum _{i}[\mathbf{\dot{p}}_{i} \cdot ( \delta \mathbf{\varphi } \times \mathbf{r}) +\mathbf{p}_{i} \cdot ( \delta \mathbf{\varphi } \times \mathbf{v})] =0$

根据矢量乘法规则

$\displaystyle \delta \mathbf{\varphi } \cdot \sum _{i}(\mathbf{\dot{p}}_{i} \times \mathbf{r} +\mathbf{p}_{i} \times \mathbf{v}) =0$

即

$\displaystyle \sum _{i}(\mathbf{\dot{p}}_{i} \times \mathbf{r} +\mathbf{p}_{i} \times \mathbf{v}) =\frac{d}{dt}\sum _{i}(\mathbf{p}_{i} \times \mathbf{r}) =0$

这就能积分得到一个不变量

$\displaystyle \mathbf{M} =\sum _{i}(\mathbf{p}_{i} \times \mathbf{r})$

即封闭系统的角动量守恒