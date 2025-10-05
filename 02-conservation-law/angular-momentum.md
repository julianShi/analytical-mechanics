## 角动量守恒

证明：

在空间中定义任意转轴 $\displaystyle \boldsymbol{\varphi}$，对于封闭的质点系，有：

$\displaystyle \delta \mathbf{r}_i = \delta \boldsymbol{\varphi} \times \mathbf{r}_i$

其中，$\displaystyle \delta \boldsymbol{\varphi}$ 是人为引入的参考系变化。粗体表示（三维）矢量。

对上式进行时间微分：

$\displaystyle \delta \mathbf{v}_i = \delta \boldsymbol{\varphi} \times \mathbf{v}_i$

将其带入拉格朗日函数的变分：

$\displaystyle \delta L=\sum _{i}\left(\frac{\partial L}{\partial \mathbf{r}_{i}} \cdot \delta \mathbf{r}_{i} +\frac{\partial L}{\partial \mathbf{v}_{i}} \cdot \delta \mathbf{v}_{i}\right) =0$

其中，下标 $i$ 表示质点系中的第 $i$ 个质点。

用广义动量表示，则：

$\displaystyle \sum _{i}[\dot{\mathbf{p}}_{i} \cdot ( \delta \boldsymbol{\varphi} \times \mathbf{r}_i) +\mathbf{p}_{i} \cdot ( \delta \boldsymbol{\varphi} \times \mathbf{v}_i)] =0$

根据矢量乘法规则：

$\displaystyle \delta \boldsymbol{\varphi} \cdot \sum _{i}(\dot{\mathbf{p}}_{i} \times \mathbf{r}_i +\mathbf{p}_{i} \times \mathbf{v}_i) =0$

即：

$\displaystyle \sum _{i}(\dot{\mathbf{p}}_{i} \times \mathbf{r}_i +\mathbf{p}_{i} \times \mathbf{v}_i) =\frac{d}{dt}\sum _{i}(\mathbf{p}_{i} \times \mathbf{r}_i) =0$

这就能积分得到一个不变量：

$\displaystyle \mathbf{M} =\sum _{i}(\mathbf{p}_{i} \times \mathbf{r}_i)$

即封闭系统的角动量守恒。