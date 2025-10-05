## 免费网页SymPy计算器

忘记怎么求解微分方程？这个好办。可以使用免费的 网页计算器 https://bubbleuniverse.github.io/symbolic/calculator

### 3维比耐方程

针对3维比耐方程

$$ \frac{d}{dx}\frac{d}{dx}f\left(x\right)+f\left(x\right)-\frac{GMm^2}{L^2} = 0 $$

在网页上

1. 粘贴下述 LaTeX 公式到输入框

```latex
 \frac{d}{dx}\frac{d}{dx}f\left(x\right)+f\left(x\right)-\frac{GMm^2}{L^2} 
```

2. 选择  ”求解微分方程 dsolve “
3. 点击“计算 Calculate” 按钮，即可得到通解

$$ f{\left(x \right)} = C_{1} \sin{\left(x \right)} + C_{2} \cos{\left(x \right)} + \frac{G M m^{2}}{L^{2}} $$

### 4维比耐方程

针对4维比耐方程

$$ \frac{d}{dx}\frac{d}{dx}f\left(x\right)+\left(1-\frac{GMm^2}{L^2}\right)f\left(x\right) = 0 $$ 

在网页上

1. 粘贴下述 LaTeX 公式到输入框

```latex
 \frac{d}{dx}\frac{d}{dx}f\left(x\right)+\left(1-\frac{GMm^2}{L^2}\right)f\left(x\right) 
```

2. 选择  ”求解微分方程 dsolve “
3. 点击“计算 Calculate” 按钮，即可得到通解

$$ f{\left(x \right)} = C_{1} e^{- \frac{x \sqrt{G M m^{2} - L^{2}}}{L}} + C_{2} e^{\frac{x \sqrt{G M m^{2} - L^{2}}}{L}} $$

