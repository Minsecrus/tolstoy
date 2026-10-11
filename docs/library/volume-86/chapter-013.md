---
title: "第十三章 矩阵与线性映射"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第三部分导言：线性代数与表示","link":"/library/volume-86/part-03"}
next: {"text":"第十四章 单个自同态的表示","link":"/library/volume-86/chapter-014"}
---

# 第十三章 矩阵与线性映射

<span class="original-page-anchor" id="pdf-page-512" aria-hidden="true"></span>

本章的读者想必已在初等课程中对线性代数有一些基本了解。我们将超出这些课程的范围，指出许多结果对交换环上的自由模仍然成立。在处理线性映射族以及模一个理想的约化时，这一点很有用。

注意，§8 和 §9 给出了线性群背景下的群论例子。

**本章始终以 $R$ 表示交换环，以 $E,F$ 表示 $R$-模。在“线性映射”和“模”前省略前缀 $R$。**

## §1. 矩阵

所谓 $R$ 中的 **$m\times n$ 矩阵**，是指 $R$ 的元素构成的双指标族 $(a_{ij})$，其中 $i=1,\ldots,m$，$j=1,\ldots,n$，通常写成如下形式：

![以 a_ij 为元素的一般 m 行 n 列矩阵，按原书图形保留。](/library/volume-86/diagrams/pdf-0512-general-matrix.png)

元素 $a_{ij}$ 称为矩阵的**系数**或**分量**。$1\times n$ 矩阵称为**行向量**（维数或大小为 $n$），$m\times1$ 矩阵称为**列向量**（维数或大小为 $m$）。一般地，我们称 $(m,n)$ 为矩阵的大小，也记作 $m\times n$。

对于大小相同的矩阵，按分量定义加法。若 $A=(a_{ij})$ 和 $B=(b_{ij})$ 是大小相同的矩阵，则把 $A+B$ 定义为其第 $ij$ 个分量为 $a_{ij}+b_{ij}$ 的矩阵。加法显然满足结合律。把矩阵 $A$ 与元素 $c\in R$ 的乘积定义为矩阵 $(ca_{ij})$，<span class="original-page-anchor" id="pdf-page-513" aria-hidden="true"></span>其第 $ij$ 个分量为 $ca_{ij}$。于是，$R$ 中所有 $m\times n$ 矩阵组成一个模（即 $R$-模）。

只有满足一定条件时才定义两个矩阵的乘积 $AB$。具体来说，$A$ 的大小为 $(m,n)$，而 $B$ 的大小为 $(n,r)$；也就是说，只有当 $A$ 的行的大小与 $B$ 的列的大小相同时才定义乘积。在这种情况下，设 $A=(a_{ij})$，$B=(b_{jk})$。把 $AB$ 定义为第 $ik$ 个分量等于

$$
\sum_{j=1}^n a_{ij}b_{jk}
$$

的 $m\times r$ 矩阵。

*若矩阵 $A,B,C$ 满足 $AB$ 与 $BC$ 均有定义，则 $(AB)C$ 与 $A(BC)$ 也都有定义，并且*

$$
(AB)C=A(BC).
$$

这很容易证明。若 $C=(c_{kl})$，读者立即可见，上述两个乘积的第 $il$ 个分量都等于

$$
\sum_j\sum_k a_{ij}b_{jk}c_{kl}.
$$

如果 $m=n$，就称 $m\times n$ 矩阵为**方阵**。例如，$1\times1$ 矩阵是方阵，有时把它与作为其唯一分量的 $R$ 的元素等同起来。

*对于给定整数 $n\ge1$，所有 $n\times n$ 方阵构成一个环。*

这也很容易验证，留给读者。

$n\times n$ 矩阵环的单位元是矩阵

![单位矩阵 I_n，按原书图形保留。](/library/volume-86/diagrams/pdf-0513-identity-matrix.png)

其对角线上的分量等于 $1$，其他分量均等于 $0$。有时用 $I$ 代替 $I_n$。

对于方阵 $A=(a_{ij})$，一般把元素 $a_{ii}$ 定义为它的**对角分量**。

由下式给出一个从 $R$ 到 $n\times n$ 矩阵环的自然环同态：

$$
c\mapsto cI_n.
$$

因此，$cI_n$ 是对角分量都等于 $c$、其他分量都等于 $0$ 的 $n\times n$ 方阵。用<span class="original-page-anchor" id="pdf-page-514" aria-hidden="true"></span>$\operatorname{Mat}_n(R)$ 表示 $R$ 中的 $n\times n$ 矩阵环。那么，$\operatorname{Mat}_n(R)$ 是 $R$ 上的代数（相对于上述同态）。

设 $A=(a_{ij})$ 为 $m\times n$ 矩阵。把它的**转置** ${}^tA$ 定义为矩阵 $(a_{ji})$，其中 $j=1,\ldots,n$，$i=1,\ldots,m$。于是 ${}^tA$ 为 $n\times m$ 矩阵。读者立即可验证，若 $A,B$ 的大小相同，则

$$
{}^t(A+B)={}^tA+{}^tB.
$$

若 $c\in R$，则 ${}^t(cA)=c\,{}^tA$。若 $A,B$ 可以相乘，则 ${}^tB\,{}^tA$ 有定义，而且

$$
{}^t(AB)={}^tB\,{}^tA.
$$

注意，矩阵运算与同态交换。更准确地说，设 $\varphi:R\to R'$ 为环同态。若 $A,B$ 是 $R$ 中的矩阵，则把 $\varphi A$ 定义为将 $\varphi$ 作用于 $A$ 的每个分量所得的矩阵。那么

$$
\begin{gathered}
\varphi(A+B)=\varphi A+\varphi B,\qquad\varphi(AB)=(\varphi A)(\varphi B),\qquad\varphi(cA)=\varphi(c)\varphi A,\\
\varphi({}^tA)={}^t\varphi(A).
\end{gathered}
$$

类似的说明适用于随后整个关于矩阵的讨论（例如下一节）。

设 $A=(a_{ij})$ 为交换环 $R$ 中的 $n\times n$ 方阵。定义 $A$ 的**迹**为

$$
\operatorname{tr}(A)=\sum_{i=1}^n a_{ii};
$$

换言之，迹是对角元素之和。

*若 $A,B$ 是 $n\times n$ 矩阵，则*

$$
\operatorname{tr}(AB)=\operatorname{tr}(BA).
$$

事实上，若 $A=(a_{ij})$，$B=(b_{ij})$，则

$$
\operatorname{tr}(AB)=\sum_i\sum_v a_{iv}b_{vi}=\operatorname{tr}(BA).
$$

*作为应用，注意到若 $B$ 是可逆的 $n\times n$ 矩阵，则*

$$
\operatorname{tr}(B^{-1}AB)=\operatorname{tr}(A).
$$

事实上，$\operatorname{tr}(B^{-1}AB)=\operatorname{tr}(ABB^{-1})=\operatorname{tr}(A)$。

<span class="original-page-anchor" id="pdf-page-515" aria-hidden="true"></span>

## §2. 矩阵的秩

设 $k$ 为域，$A$ 为 $k$ 中的 $m\times n$ 矩阵。$A$ 的**行秩**是指 $A$ 的线性无关行的最大数目，$A$ 的**列秩**是指 $A$ 的线性无关列的最大数目。因此，这两个秩分别是 $A$ 的各行与各列所生成的向量空间的维数。我们断言这两个秩相等，并把这个共同的数定义为 $A$ 的**秩**。

设 $A^1,\ldots,A^n$ 为 $A$ 的各列，$A_1,\ldots,A_m$ 为各行。设 ${}^tX=(x_1,\ldots,x_m)$ 的分量为 $x_i\in k$。有线性映射

$$
X\mapsto x_1A_1+\cdots+x_mA_m,
$$

把 $k^{(m)}$ 映满到各行向量生成的空间。设 $W$ 为其核。则 $W$ 是 $k^{(m)}$ 的子空间，而且

$$
\dim W+\text{行秩}=m.
$$

若 $Y$ 为维数 $m$ 的列向量，则将 $1\times1$ 矩阵 ${}^tXY$ 视为 $k$ 中的元素后，映射

$$
(X,Y)\mapsto{}^tXY=X\cdot Y
$$

是取值于 $k$ 的双线性映射。空间 $W$ 是列向量 $A^1,\ldots,A^n$ 的正交空间，即满足对所有 $j=1,\ldots,n$ 都有 $X\cdot A^j=0$ 的所有 $X$ 构成的空间。由第三章的对偶定理，在配对

$$
(X,Y)\mapsto X\cdot Y
$$

下，$k^{(m)}$ 是自身的对偶，而 $k^{(m)}/W$ 与 $A^1,\ldots,A^n$ 生成的空间对偶。因此

$$
\dim k^{(m)}/W=\text{列秩},
$$

即

$$
\dim W+\text{列秩}=m.
$$

于是得到

$$
\text{列秩}=\text{行秩},
$$

这正是所要证明的。

空间 $W$ 可视为由 $n$ 个线性方程构成的方程组

$$
x_1A_1+\cdots+x_mA_m=0
$$

的解空间，<span class="original-page-anchor" id="pdf-page-516" aria-hidden="true"></span>其中有 $m$ 个未知数 $x_1,\ldots,x_m$。事实上，将上面的向量方程按所有坐标展开，就得到通常的 $n$ 个线性方程构成的方程组。读者如愿意，可自行写出这些方程。

## §3. 矩阵与线性映射

设 $E$ 为模，并假设 $E$ 在 $R$ 上有基 $\mathcal B=\{\xi_1,\ldots,\xi_n\}$。这意味着 $E$ 的每个元素都可以唯一地表示成线性组合

$$
x=x_1\xi_1+\cdots+x_n\xi_n,
$$

其中 $x_i\in R$。称 $(x_1,\ldots,x_n)$ 为 $x$ 相对于该基的**分量**。这个分量的 $n$ 元组可视为行向量。用 $X$ 表示行向量 $(x_1,\ldots,x_n)$ 的转置，称 $X$ 为 $x$ 相对于该基的**列向量**。

若 $\{\xi'_1,\ldots,\xi'_m\}$ 为 $E$ 在 $R$ 上的另一个基，则 $m=n$。设 $\mathfrak p$ 为 $R$ 的极大理想。于是 $E/\mathfrak pE$ 是域 $R/\mathfrak pR$ 上的向量空间。若 $\bar\xi_i$ 表示 $\xi_i\bmod\mathfrak pE$ 的剩余类，则 $\{\bar\xi_1,\ldots,\bar\xi_n\}$ 是 $E/\mathfrak pE$ 在 $R/\mathfrak pR$ 上的基。因此 $n$ 是这个向量空间的维数；我们已经证明了域上基的基数的不变性，故 $m=n$。称 $n$ 为模 $E$ 在 $R$ 上的**维数**。

> **译校注：** 本段通过选取极大理想证明基的基数不变，需假设 $R\ne0$。零环没有极大理想，而且所有 $R^{(n)}$ 都是零模，因而不能由此定义唯一的基的大小。正文保留原书叙述；在这里及随后使用自由模维数时，应加上 $R\ne0$ 的通常假设。

把 $R^{(n)}$ 视为大小为 $n$ 的列向量的集合，因而是 $R$ 上维数为 $n$ 的自由模。其一个基由单位向量 $e^1,\ldots,e^n$ 构成，其中

$$
{}^te^i=(0,\ldots,0,1,0,\ldots,0)
$$

的各分量都是 $0$，只有第 $i$ 个分量为 $1$。

一个 $m\times n$ 矩阵 $A$ 按规则

$$
X\mapsto AX
$$

定义线性映射

$$
L_A:R^{(n)}\to R^{(m)}.
$$

也就是说，对于列向量 $X,Y$ 和 $c\in R$，有 $A(X+Y)=AX+AY$，$A(cX)=cAX$。

<span class="original-page-anchor" id="pdf-page-517" aria-hidden="true"></span>

上述讨论可以扩展到稍一般的情形，这种扩展很有用。设 $E$ 为阿贝尔群，且 $R$ 是

$$
\operatorname{End}_{\mathbf Z}(E)=\operatorname{Hom}_{\mathbf Z}(E,E)
$$

的交换子环。那么 $E$ 是 $R$ 模。此外，若 $A$ 为 $R$ 中的 $m\times n$ 矩阵，就得到线性映射

$$
L_A:E^{(n)}\to E^{(m)},
$$

其定义规则与上面类似，即 $X\mapsto AX$。不过，这个规则须按显然的方式解释。若 $A=(a_{ij})$，$X$ 是由 $E$ 的元素组成的列向量，则

$$
AX=\begin{pmatrix}a_{11}&\cdots&a_{1n}\\&\cdots&\\a_{m1}&\cdots&a_{mn}\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}=\begin{pmatrix}y_1\\\vdots\\y_m\end{pmatrix},
$$

其中 $y_i=\sum_{j=1}^n a_{ij}x_j$。

若 $A,B$ 为 $R$ 中可以相乘的矩阵，则对任何 $c\in R$，有

$$
L_{AB}=L_AL_B,\qquad L_{cA}=cL_A.
$$

因此有结合律，即

$$
A(BX)=(AB)X.
$$

任意交换环 $R$ 都可以视为自身上的模。这样就恢复了从 $R^{(n)}$ 到 $R^{(m)}$ 的映射这一特殊情形。此外，若 $E$ 为 $R$ 模，则 $R$ 可以视为 $E$ 的自同态构成的环。

**命题 3.1。** *设 $E$ 为 $R$ 上的自由模，$\{x_1,\ldots,x_n\}$ 为其基。设 $y_1,\ldots,y_n$ 为 $E$ 的元素，$A$ 为 $R$ 中满足下式的矩阵：*

$$
A\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}=\begin{pmatrix}y_1\\\vdots\\y_n\end{pmatrix}.
$$

*则 $\{y_1,\ldots,y_n\}$ 是 $E$ 的基，当且仅当 $A$ 可逆。*

**证明。** 设 $X,Y$ 为这些元素构成的列向量，则 $AX=Y$。假设 $Y$ 是基，那么存在 $R$ 中的矩阵 $C$ 使得 $CY=X$。

<span class="original-page-anchor" id="pdf-page-518" aria-hidden="true"></span>

于是 $CAX=X$，从而 $CA=I$，$A$ 可逆。反之，假设 $A$ 可逆，则 $X=A^{-1}Y$，因此 $x_1,\ldots,x_n$ 属于 $y_1,\ldots,y_n$ 生成的模。假设有关系式

$$
b_1y_1+\cdots+b_ny_n=0,
$$

其中 $b_i\in R$。设 $B$ 为行向量 $(b_1,\ldots,b_n)$，则

$$
BY=0,
$$

从而 $BAX=0$。然而 $\{x_1,\ldots,x_n\}$ 是基，故 $BA=0$，于是 $BAA^{-1}=B=0$。这证明了 $Y$ 的各分量在 $R$ 上线性无关，也就证明了命题。

现在回到任意交换环 $R$ 上的模的情形。

设 $E,F$ 为模。我们将说明，在给定 $E,F$ 的基后，如何给线性映射配上矩阵。假设 $E,F$ 都是自由模，分别以 $\mathcal B=\{\xi_1,\ldots,\xi_n\}$ 和 $\mathcal B'=\{\xi'_1,\ldots,\xi'_m\}$ 为基。设

$$
f:E\to F
$$

为线性映射。存在唯一的元素 $a_{ij}\in R$，使得

$$
\begin{aligned}
f(\xi_1)&=a_{11}\xi'_1+\cdots+a_{m1}\xi'_m,\\
&\cdots\\
f(\xi_n)&=a_{1n}\xi'_1+\cdots+a_{mn}\xi'_m,
\end{aligned}
$$

换言之，

$$
f(\xi_j)=\sum_{i=1}^m a_{ij}\xi'_i.
$$

（注意，求和针对的是*第一个*下标。）定义

$$
M_{\mathcal B'}^{\mathcal B}(f)=(a_{ij}).
$$

若 $x=x_1\xi_1+\cdots+x_n\xi_n$ 是 $x$ 关于该基的表示，便用 $M_{\mathcal B}(x)$ 表示 $x$ 的分量列向量 $X$。可见

$$
M_{\mathcal B'}(f(x))=M_{\mathcal B'}^{\mathcal B}(f)M_{\mathcal B}(x).
$$

也就是说，若 $X'$ 为 $f(x)$ 的列向量，$M$ 为与 $f$ 相配的矩阵，则 $X'=MX$。因此，线性映射的作用体现为矩阵乘法，且 $f=L_M$。

<span class="original-page-anchor" id="pdf-page-519" aria-hidden="true"></span>

**命题 3.2。** *设 $E,F,D$ 为模，$\mathcal B,\mathcal B',\mathcal B''$ 分别为 $E,F,D$ 的有限基。设*

$$
E\xrightarrow{f}F\xrightarrow{g}D
$$

*为线性映射，则*

$$
M_{\mathcal B''}^{\mathcal B}(g\circ f)=M_{\mathcal B''}^{\mathcal B'}(g)M_{\mathcal B'}^{\mathcal B}(f).
$$

**证明。** 设 $A,B$ 分别为映射 $f,g$ 关于给定基的矩阵。若 $X$ 为 $x\in E$ 的列向量，则 $g(f(x))$ 的列向量为 $B(AX)=(BA)X$。因此，$BA$ 就是 $g\circ f$ 的矩阵。这证明了所要的结论。

**推论 3.3。** *设 $E=F$，则*

$$
M_{\mathcal B'}^{\mathcal B}(\mathrm{id})M_{\mathcal B}^{\mathcal B'}(\mathrm{id})=M_{\mathcal B'}^{\mathcal B'}(\mathrm{id})=I.
$$

*每个矩阵 $M_{\mathcal B'}^{\mathcal B}(\mathrm{id})$ 都可逆（即为矩阵环中的可逆元）。*

**证明。** 显然。

**推论 3.4。** *设 $N=M_{\mathcal B'}^{\mathcal B}(\mathrm{id})$，则*

$$
M_{\mathcal B'}^{\mathcal B'}(f)=M_{\mathcal B'}^{\mathcal B}(\mathrm{id})M_{\mathcal B}^{\mathcal B}(f)M_{\mathcal B}^{\mathcal B'}(\mathrm{id})=NM_{\mathcal B}^{\mathcal B}(f)N^{-1}.
$$

**证明。** 显然。

**推论 3.5。** *设 $E$ 为 $R$ 上维数 $n$ 的自由模，$\mathcal B$ 为 $E$ 在 $R$ 上的基。映射*

$$
f\mapsto M_{\mathcal B}^{\mathcal B}(f)
$$

*是从 $E$ 的自同态环到 $R$ 中的 $n\times n$ 矩阵环的环同构。事实上，它还是 $R$ 上的代数同构。*

称矩阵 $M_{\mathcal B}^{\mathcal B}(f)$ 为 **$f$ 关于基 $\mathcal B$ 的矩阵**。

设 $E$ 为 $R$ 上维数 $n$ 的自由模。$GL(E)$ 或 $\operatorname{Aut}_R(E)$ 表示 $E$ 的线性自同构群，它是 $\operatorname{End}_R(E)$ 的可逆元群。$GL_n(R)$ 表示 $R$ 中可逆的 $n\times n$ 矩阵所构成的群。为 $E$ 在 $R$ 上选定基后，就有关于该基的群同构

$$
GL(E)\leftrightarrow GL_n(R).
$$

<span class="original-page-anchor" id="pdf-page-520" aria-hidden="true"></span>

设 $E$ 如上。若

$$
f:E\to E
$$

为线性映射，选取基 $\mathcal B$，设 $M$ 为 $f$ 关于 $\mathcal B$ 的矩阵。把 $f$ 的**迹**定义为 $M$ 的迹，即

$$
\operatorname{tr}(f)=\operatorname{tr}(M).
$$

若 $M'$ 为 $f$ 关于另一个基的矩阵，则存在可逆矩阵 $N$，使 $M'=N^{-1}MN$。因此，迹与基的选择无关。

## §4. 行列式

设 $E_1,\ldots,E_n,F$ 为模。若映射

$$
f:E_1\times\cdots\times E_n\to F
$$

对每个变量都是线性的，就称其为 **$R$ 多线性**（或简称**多线性**）映射。也就是说，对每个下标 $i$ 和元素 $x_1,\ldots,x_{i-1},x_{i+1},\ldots,x_n$，其中 $x_j\in E_j$，映射

$$
x\mapsto f(x_1,\ldots,x_{i-1},x,x_{i+1},\ldots,x_n)
$$

是从 $E_i$ 到 $F$ 的线性映射。

定义在 $n$ 重积上的多线性映射也称为 **$n$ 重线性**映射。若 $E_1=\cdots=E_n=E$，也称 $f$ 为 **$E$ 上的多线性映射**，而不说它是 $E^{(n)}$ 上的多线性映射。

设 $f$ 为 $n$ 重线性映射。取两个不同的下标 $i,j$，固定第 $i$、第 $j$ 个变量以外的所有变量，就可将 $f$ 视为 $E_i\times E_j$ 上的双线性映射。

假设 $E_1=\cdots=E_n=E$。若只要存在下标 $i$，$1\le i\le n-1$，使 $x_i=x_{i+1}$，就有 $f(x_1,\ldots,x_n)=0$，则称多线性映射 $f$ 为**交替**的（换言之，相邻的两个元素相等时取值为零）。

**命题 4.1。** *设 $f$ 为 $E$ 上的 $n$ 重线性交替映射，$x_1,\ldots,x_n\in E$。则*

$$
f(\cdots,x_i,x_{i+1},\cdots)=-f(\cdots,x_{i+1},x_i,\cdots).
$$

*也就是说，交换 $f$ 的两个相邻自变量后，$f$ 的值变号。若 $i\ne j$ 而 $x_i=x_j$，则 $f(x_1,\ldots,x_n)=0$。*

<span class="original-page-anchor" id="pdf-page-521" aria-hidden="true"></span>

**证明。** 只考虑第 $i$、第 $j$ 个位置的因子，其中 $j=i+1$，证明第一个断言时可以假设 $f$ 是双线性的。于是对所有 $x,y\in E$，有

$$
0=f(x+y,x+y)=f(x,y)+f(y,x).
$$

这就证明了所要的等式 $f(y,x)=-f(x,y)$。对于第二个断言，可以连续交换 $f$ 的相邻自变量，直到得到具有两个相等的相邻自变量的 $E$ 中元素的 $n$ 元组。这说明，若 $x_i=x_j$ 且 $i\ne j$，则 $f(x_1,\ldots,x_n)=0$。

**推论 4.2。** *设 $f$ 为 $E$ 上的 $n$ 重线性交替映射，$x_1,\ldots,x_n\in E$，$i\ne j$，$a\in R$。若把 $x_i$ 换成 $x_i+ax_j$，并保持其余分量不变，则 $f$ 在 $(x_1,\ldots,x_n)$ 上的值不变。*

**证明。** 显然。

取值于 $R$ 的多线性交替映射称为**多线性交替形式**。

我们将多次求多线性交替映射在 $E$ 的元素的线性组合上的值。设

$$
\begin{aligned}
w_1&=a_{11}v_1+\cdots+a_{1n}v_n,\\
&\cdots\\
w_n&=a_{n1}v_1+\cdots+a_{nn}v_n.
\end{aligned}
$$

*设 $f$ 为 $E$ 上的 $n$ 重线性交替映射，则*

$$
f(w_1,\ldots,w_n)=f(a_{11}v_1+\cdots+a_{1n}v_n,\ldots,a_{n1}v_1+\cdots+a_{nn}v_n).
$$

利用多线性展开后，得到形如

$$
a_{1,\sigma(1)}\cdots a_{n,\sigma(n)}f(v_{\sigma(1)},\ldots,v_{\sigma(n)})
$$

的各项之和，其中 $\sigma$ 遍历从 $\{1,\ldots,n\}$ 到自身的任意映射。若 $\sigma$ 不是双射（即置换），则有 $i\ne j$，使两个自变量 $v_{\sigma(i)}$ 和 $v_{\sigma(j)}$ 相等，该项为 $0$。所以只需对置换 $\sigma$ 求和。把元素 $(v_{\sigma(1)},\ldots,v_{\sigma(n)})$ 重新排列为标准次序，并用命题 4.1，就得到以下展开式：

**引理 4.3。** *若 $w_1,\ldots,w_n$ 如上，则*

$$
f(w_1,\ldots,w_n)=\sum_\sigma\varepsilon(\sigma)a_{1,\sigma(1)}\cdots a_{n,\sigma(n)}f(v_1,\ldots,v_n),
$$

*其中求和遍历 $\{1,\ldots,n\}$ 的所有置换 $\sigma$，$\varepsilon(\sigma)$ 为置换的符号。*

<span class="original-page-anchor" id="pdf-page-522" aria-hidden="true"></span>

关于行列式，我将采用阿廷在《伽罗瓦理论》中的处理方法。

$n\times n$ **行列式**是指映射

$$
\det:\operatorname{Mat}_n(R)\to R,
$$

也记作

$$
D:\operatorname{Mat}_n(R)\to R,
$$

把它视为矩阵 $A$ 的列向量 $A^1,\ldots,A^n$ 的函数时，它是多线性交替的，并满足 $D(I)=1$。本章大多用字母 $D$ 表示行列式。

稍后我们将证明行列式存在。现在先推导其性质。

**定理 4.4（克拉默法则）。** *设 $A^1,\ldots,A^n$ 为维数 $n$ 的列向量，$x_1,\ldots,x_n\in R$ 满足*

$$
x_1A^1+\cdots+x_nA^n=B,
$$

*其中 $B$ 为某个列向量。那么对每个 $i$，有*

$$
x_iD(A^1,\ldots,A^n)=D(A^1,\ldots,B,\ldots,A^n),
$$

*其中最后一行的 $B$ 位于第 $i$ 个位置。*

**证明。** 不妨取 $i=1$。展开得

$$
D(B,A^2,\ldots,A^n)=\sum_{j=1}^n x_jD(A^j,A^2,\ldots,A^n).
$$

再用命题 4.1，就得到所要的结论（右边各项除含有 $x_1$ 的一项外，其余都为 $0$）。

**推论 4.5。** *假设 $R$ 为域，则 $A^1,\ldots,A^n$ 线性相关，当且仅当 $D(A^1,\ldots,A^n)=0$。*

**证明。** 假设有关系式

$$
x_1A^1+\cdots+x_nA^n=0,
$$

其中 $x_i\in R$。则对所有 $i$，都有 $x_iD(A)=0$。若某个 $x_i\ne0$，就有 $D(A)=0$。反之，假设 $A^1,\ldots,A^n$ 线性无关，则单位向量 $e^1,\ldots,e^n$ 可表示为线性组合

$$
\begin{aligned}
e^1&=b_{11}A^1+\cdots+b_{1n}A^n,\\
&\cdots\\
e^n&=b_{n1}A^1+\cdots+b_{nn}A^n.
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-523" aria-hidden="true"></span>

其中 $b_{ij}\in R$。但

$$
1=D(e^1,\ldots,e^n).
$$

利用前面的引理，这可展开成含有 $D(A^1,\ldots,A^n)$ 的各项之和，因此 $D(A)$ 不能为 $0$。

**命题 4.6。** *若行列式存在，则它是唯一的。若 $A^1,\ldots,A^n$ 是矩阵 $A=(a_{ij})$ 的维数为 $n$ 的列向量，则*

$$
D(A^1,\ldots,A^n)=\sum_\sigma\varepsilon(\sigma)a_{\sigma(1),1}\cdots a_{\sigma(n),n},
$$

*其中求和遍历 $\{1,\ldots,n\}$ 的所有置换 $\sigma$，$\varepsilon(\sigma)$ 为置换的符号。*

**证明。** 设 $e^1,\ldots,e^n$ 为通常的单位向量。可以写成

$$
\begin{aligned}
A^1&=a_{11}e^1+\cdots+a_{n1}e^n,\\
&\cdots\\
A^n&=a_{1n}e^1+\cdots+a_{nn}e^n.
\end{aligned}
$$

> **译校注：** 原书最后一行首项印为 $a_{1n}e^n$，这里改为 $a_{1n}e^1$。$a_{1n}$ 是第 $n$ 列的第一坐标，故应乘第一单位向量 $e^1$；放大原图后可确认原印上标为 $n$。

由引理，得到

$$
D(A^1,\ldots,A^n)=\sum_\sigma\varepsilon(\sigma)a_{\sigma(1),1}\cdots a_{\sigma(n),n}.
$$

这证明行列式的值唯一确定，且由预期的公式给出。

**推论 4.7。** *设 $\varphi:R\to R'$ 为到交换环的环同态。若 $A$ 为 $R$ 中的方阵，把 $\varphi A$ 定义为将 $\varphi$ 作用于 $A$ 的每个分量所得的矩阵。则*

$$
\varphi(D(A))=D(\varphi A).
$$

**证明。** 将 $\varphi$ 作用于命题 4.6 的表达式。

**命题 4.8。** *若 $A$ 为 $R$ 中的方阵，则*

$$
D(A)=D({}^tA).
$$

**证明。** 在乘积

$$
a_{\sigma(1),1}\cdots a_{\sigma(n),n}
$$

中，从 $1$ 到 $n$ 的每个整数 $k$ 都在 $\sigma(1),\ldots,\sigma(n)$ 中恰好出现一次。因此，这个乘积可改写为

$$
a_{1,\sigma^{-1}(1)}\cdots a_{n,\sigma^{-1}(n)}.
$$

<span class="original-page-anchor" id="pdf-page-524" aria-hidden="true"></span>

由于 $\varepsilon(\sigma)=\varepsilon(\sigma^{-1})$，命题 4.6 中的和式可改写为

$$
\sum_\sigma\varepsilon(\sigma^{-1})a_{1,\sigma^{-1}(1)}\cdots a_{n,\sigma^{-1}(n)}.
$$

其中每一项对应一个置换 $\sigma$。然而，当 $\sigma$ 遍历所有置换时，$\sigma^{-1}$ 也遍历所有置换。因此，这个和式等于

$$
\sum_\sigma\varepsilon(\sigma)a_{1,\sigma(1)}\cdots a_{n,\sigma(n)},
$$

这正是 $D({}^tA)$，故得证。

**推论 4.9。** *行列式对于矩阵的各行也是多线性交替的。*

现在证明存在性，并同时证明行列式的另一个重要性质。

当 $n=1$ 时，对任意 $a\in R$ 定义 $D(a)=a$。

假设已经对所有小于 $n$ 的整数证明了行列式的存在性，其中 $n\ge2$。设 $A=(a_{ij})$ 为 $R$ 中的 $n\times n$ 矩阵。用 $A_{ij}$ 表示从 $A$ 中删去第 $i$ 行和第 $j$ 列所得的 $(n-1)\times(n-1)$ 矩阵。固定整数 $i$，$1\le i\le n$，递归定义

$$
D(A)=(-1)^{i+1}a_{i1}D(A_{i1})+\cdots+(-1)^{i+n}a_{in}D(A_{in}).
$$

（这称为 **$D$ 按第 $i$ 行的展开**。）我们将证明 $D$ 满足行列式的定义。

把 $D$ 看成第 $k$ 列的函数，并考虑任意一项

$$
(-1)^{i+j}a_{ij}D(A_{ij}).
$$

若 $j\ne k$，则 $a_{ij}$ 不依赖第 $k$ 列，而 $D(A_{ij})$ 对第 $k$ 列线性。若 $j=k$，则 $a_{ij}$ 对第 $k$ 列线性，而 $D(A_{ij})$ 不依赖第 $k$ 列。在任何情况下，该项都对第 $k$ 列线性。由于 $D(A)$ 是这些项的和，它也对第 $k$ 列线性，因此 $D$ 是多线性的。

其次，假设 $A$ 的两个相邻列相等，例如 $A^k=A^{k+1}$。取下标 $j$，使 $j\ne k$ 且 $j\ne k+1$。则矩阵 $A_{ij}$ 有两个相等的相邻列，因而其行列式为 $0$。因此，对应于不同于 $k$、$k+1$ 的下标 $j$ 的项对 $D(A)$ 的贡献为零。其余两项可写为

$$
(-1)^{i+k}a_{ik}D(A_{ik})+(-1)^{i+k+1}a_{i,k+1}D(A_{i,k+1}).
$$

由第 $k$ 列与第 $(k+1)$ 列相等的假设，两个矩阵 $A_{ik}$ 与 $A_{i,k+1}$ 相等。同样，$a_{ik}=a_{i,k+1}$。

<span class="original-page-anchor" id="pdf-page-525" aria-hidden="true"></span>

因此，这两项符号相反，彼此抵消。这证明该形式是交替的，得到：

**命题 4.10。** *行列式存在，并满足按行或按列展开的规则。*

（对于列，利用 $D(A)=D({}^tA)$ 即可。）

**例。** 我们明确写出一个最重要的行列式。设 $x_1,\ldots,x_n$ 为交换环的元素。这些元素的**范德蒙德行列式** $V=V(x_1,\ldots,x_n)$ 定义为

$$
V=\begin{vmatrix}1&1&\cdots&1\\x_1&x_2&\cdots&x_n\\\vdots&\vdots&&\vdots\\x_1^{n-1}&x_2^{n-1}&\cdots&x_n^{n-1}\end{vmatrix},
$$

其值可明确求出为

$$
V=\prod_{i<j}(x_j-x_i).
$$

若该环为整环，且 $i\ne j$ 时 $x_i\ne x_j$，则 $V\ne0$。为证明上述求值公式，将倒数第二行乘 $x_1$，再从最后一行减去它。然后沿各行向上重复这一步，使第一列除左上角的 $1$ 以外，所有元素都变为 $0$。随后按第一列展开，并利用齐次性与归纳法，即可完成 $V$ 的求值证明。

**定理 4.11。** *设 $E$ 为 $R$ 模，$v_1,\ldots,v_n$ 为 $E$ 的元素。设 $A=(a_{ij})$ 为 $R$ 中的矩阵，且*

$$
A\begin{pmatrix}v_1\\\vdots\\v_n\end{pmatrix}=\begin{pmatrix}w_1\\\vdots\\w_n\end{pmatrix}.
$$

*设 $\Delta$ 为 $E$ 上的 $n$ 重线性交替映射，则*

$$
\Delta(w_1,\ldots,w_n)=D(A)\Delta(v_1,\ldots,v_n).
$$

**证明。** 展开

$$
\Delta(a_{11}v_1+\cdots+a_{1n}v_n,\ldots,a_{n1}v_1+\cdots+a_{nn}v_n),
$$

再考虑 $D(A)=D({}^tA)$，恰好得到所要的结论。

<span class="original-page-anchor" id="pdf-page-526" aria-hidden="true"></span>

设 $E,F$ 为模，用 $L_a^n(E,F)$ 表示从 $E$ 到 $F$ 的 $n$ 重线性交替映射的集合。若 $F=R$，也记 $L_a^n(E,R)=L_a^n(E)$。显然 $L_a^n(E,F)$ 是 $R$ 模，即对加法和乘以 $R$ 的元素封闭。

**推论 4.12。** *设 $E$ 为 $R$ 上的自由模，$\{v_1,\ldots,v_n\}$ 为其基。设 $F$ 为任意模，$w\in F$。存在唯一的 $n$ 重线性交替映射*

$$
\Delta_w:E\times\cdots\times E\to F,
$$

*使得 $\Delta_w(v_1,\ldots,v_n)=w$。*

**证明。** 不失一般性，可假设 $E=R^{(n)}$。于是对列向量 $A^1,\ldots,A^n$，定义

$$
\Delta_w(A^1,\ldots,A^n)=D(A)w.
$$

显然 $\Delta_w$ 具有所要求的性质。

**推论 4.13。** *若 $E$ 在 $R$ 上自由，且有一个由 $n$ 个元素组成的基，则 $L_a^n(E)$ 在 $R$ 上自由，且有一个由 $1$ 个元素组成的基。*

**证明。** 设 $\Delta_1$ 为在基 $\{v_1,\ldots,v_n\}$ 上取值 $1$ 的多线性交替映射。任意元素 $\varphi\in L_a^n(E)$ 都可唯一写为 $c\Delta_1$，其中 $c\in R$，即 $c=\varphi(v_1,\ldots,v_n)$。这证明了所要的结论。

上一个推论中的 $L_a^n(E)$ 的任意两个基相差一个 $R$ 中的可逆元。换言之，若 $\Delta$ 是 $L_a^n(E)$ 的基，则对某个 $c\in R$ 有 $\Delta=c\Delta_1=\Delta_c$，且 $c$ 必须可逆。当然，$\Delta_1$ 依赖 $E$ 的基的选择。考虑 $R^{(n)}$ 时，我们的行列式 $D$ 正是关于单位向量 $e^1,\ldots,e^n$ 构成的标准基的 $\Delta_1$。

有时为方便起见，把 $L_a^n(E)$ 的任意一个基称为 $E$ 上的**行列式**。采用这个术语后，克拉默法则的推论可表述如下。

**推论 4.14。** *设 $R$ 为域，$E$ 为维数 $n$ 的向量空间，$\Delta$ 为 $E$ 上的任意行列式，$v_1,\ldots,v_n\in E$。$\{v_1,\ldots,v_n\}$ 是 $E$ 的基的充要条件是*

$$
\Delta(v_1,\ldots,v_n)\ne0.
$$

**命题 4.15。** *设 $A,B$ 为 $R$ 中的 $n\times n$ 矩阵，则*

$$
D(AB)=D(A)D(B).
$$

<span class="original-page-anchor" id="pdf-page-527" aria-hidden="true"></span>

**证明。** 这实际上是定理 4.11 的推论。取 $v_1,\ldots,v_n$ 为单位向量 $e^1,\ldots,e^n$，并考虑

$$
AB\begin{pmatrix}e^1\\\vdots\\e^n\end{pmatrix}=\begin{pmatrix}w_1\\\vdots\\w_n\end{pmatrix}.
$$

得到

$$
D(w_1,\ldots,w_n)=D(AB)D(e^1,\ldots,e^n).
$$

另一方面，由结合律，应用两次定理 4.11，得

$$
D(w_1,\ldots,w_n)=D(A)D(B)D(e^1,\ldots,e^n).
$$

由于 $D(e^1,\ldots,e^n)=1$，命题成立。

设 $A=(a_{ij})$ 为 $R$ 中的 $n\times n$ 矩阵。设

$$
\widetilde A=(b_{ij})
$$

为满足

$$
b_{ij}=(-1)^{i+j}D(A_{ji})
$$

的矩阵。（注意下标次序颠倒了！）

**命题 4.16。** *设 $d=D(A)$，则 $A\widetilde A=\widetilde AA=dI$。行列式 $D(A)$ 在 $R$ 中可逆，当且仅当 $A$ 可逆，此时*

$$
A^{-1}=\frac1d\widetilde A.
$$

**证明。** 对任意下标 $i,k$，$A\widetilde A$ 的 $ik$ 分量为

$$
a_{i1}b_{1k}+a_{i2}b_{2k}+\cdots+a_{in}b_{nk}=a_{i1}(-1)^{k+1}D(A_{k1})+\cdots+a_{in}(-1)^{k+n}D(A_{kn}).
$$

若 $i=k$，此和就是行列式按第 $i$ 行的展开，故等于 $d$。若 $i\ne k$，设 $\bar A$ 为把 $A$ 的第 $k$ 行换为第 $i$ 行、其余行保持不变所得的矩阵。从 $\bar A$ 中删去第 $k$ 行和第 $j$ 列，所得矩阵与从 $A$ 中删去第 $k$ 行和第 $j$ 列的结果相同。因此

$$
\bar A_{kj}=A_{kj},
$$

所以，以上的和可写成

$$
a_{i1}(-1)^{k+1}D(\bar A_{k1})+\cdots+a_{in}(-1)^{k+n}D(\bar A_{kn}).
$$

<span class="original-page-anchor" id="pdf-page-528" aria-hidden="true"></span>

这就是 $\bar A$ 的行列式按第 $k$ 行的展开。因此 $D(\bar A)=0$，上述和为 $0$。

> **译校注：** 原书本句印为“按第 $i$ 行展开”。前页的余子式是 $\bar A_{kj}$，符号是 $(-1)^{k+j}$，而 $\bar A$ 的第 $k$ 行正是原矩阵的第 $i$ 行，故此处应为按 $\bar A$ 的第 $k$ 行展开。

因此我们证明了：$A\widetilde A$ 的 $ik$ 分量在 $i=k$ 时（即对角分量）等于 $d$，其他情况下等于 $0$。这证明了 $A\widetilde A=dI$。另一方面，由定义立即可见 ${}^t\widetilde A=\widetilde{{}^tA}$。于是

$$
{}^t(\widetilde AA)={}^tA\,{}^t\widetilde A={}^tA\,\widetilde{{}^tA}=dI.
$$

因 ${}^t(dI)=dI$，也有 $\widetilde AA=dI$。若 $d$ 为 $R$ 中的可逆元，则 $A$ 可逆，其逆为 $d^{-1}\widetilde A$。反之，若 $A$ 可逆且 $AA^{-1}=I$，则 $D(A)D(A^{-1})=1$，故 $D(A)$ 可逆，得证。

**推论 4.17。** *设 $F$ 为任意 $R$ 模，$w_1,\ldots,w_n$ 为 $F$ 的元素。设 $A=(a_{ij})$ 为 $R$ 中的 $n\times n$ 矩阵，且*

$$
\begin{aligned}
a_{11}w_1+\cdots+a_{1n}w_n&=v_1\\
&\cdots\\
a_{n1}w_1+\cdots+a_{nn}w_n&=v_n.
\end{aligned}
$$

*则可明确求得*

$$
\begin{pmatrix}D(A)w_1\\\vdots\\D(A)w_n\end{pmatrix}=D(A)\begin{pmatrix}w_1\\\vdots\\w_n\end{pmatrix}=\widetilde A\begin{pmatrix}v_1\\\vdots\\v_n\end{pmatrix}.
$$

*特别地，若对所有 $i$ 都有 $v_i=0$，则对所有 $i$ 都有 $D(A)w_i=0$。若所有 $v_i=0$，且 $F$ 由 $w_1,\ldots,w_n$ 生成，则 $D(A)F=0$。*

**证明。** 由关系 $\widetilde AA=D(A)I$，结合 §3 中关于矩阵作用于分量属于模的列向量的说明，立即得出结论。

**命题 4.18。** *设 $E,F$ 为 $R$ 上维数 $n$ 的自由模，$f:E\to F$ 为线性映射，$\mathcal B,\mathcal B'$ 分别为 $E,F$ 在 $R$ 上的基。则 $f$ 为同构，当且仅当其矩阵 $M_{\mathcal B'}^{\mathcal B}(f)$ 的行列式为 $R$ 中的可逆元。*

**证明。** 设 $A=M_{\mathcal B'}^{\mathcal B}(f)$。由定义，$f$ 为同构，当且仅当存在一个线性映射 $g:F\to E$，使 $g\circ f=\mathrm{id}$ 且 $f\circ g=\mathrm{id}$。若 $f$ 为同构，令 $B=M_{\mathcal B}^{\mathcal B'}(g)$，则 $AB=BA=I$。对乘积取行列式，可得 $D(A)$ 在 $R$ 中可逆。反之，若 $D(A)$ 为可逆元，则由命题 4.16 可定义 $A^{-1}$。它是某个线性映射 $g:F\to E$ 的矩阵，而 $g$ 是 $f$ 的逆，故得证。

最后，我们定义自同态的行列式。

<span class="original-page-anchor" id="pdf-page-529" aria-hidden="true"></span>

设 $E$ 为 $R$ 上的自由模，$\mathcal B$ 为其基，$f:E\to E$ 为 $E$ 的自同态。令

$$
M=M_{\mathcal B}^{\mathcal B}(f).
$$

若 $\mathcal B'$ 为 $E$ 的另一个基，且 $M'=M_{\mathcal B'}^{\mathcal B'}(f)$，则存在可逆矩阵 $N$，使

$$
M'=NMN^{-1}.
$$

取行列式可知 $D(M')=D(M)$。因此行列式不依赖基的选择，称为**线性映射 $f$ 的行列式**。下面将给出一个不依赖基的选择的刻画。

设 $E$ 为任意模，则可将 $L_a^n(E)$ 视为变量 $E$ 的反变函子。事实上，$L_a^n(E,F)$ 可视为两个变量的函子，对第一个变量反变，对第二个变量协变。确实，设

$$
E'\xrightarrow{f}E
$$

为线性映射。对每个多线性映射 $\varphi:E^{(n)}\to F$，可配上复合映射 $\varphi\circ f^{(n)}$，

$$
E'\times\cdots\times E'\xrightarrow{f^{(n)}}E\times\cdots\times E\xrightarrow{\varphi}F,
$$

其中 $f^{(n)}$ 为 $f$ 与自身的 $n$ 重积。由

$$
\varphi\mapsto\varphi\circ f^{(n)}
$$

给出的映射

$$
L_a^n(f):L_a^n(E,F)\to L_a^n(E',F)
$$

显然是线性的，它定义了我们的函子。有时用 $f^*$ 代替 $L_a^n(f)$。

特别地，考虑 $E=E'$、$F=R$ 的情形，得到诱导映射

$$
f^*:L_a^n(E)\to L_a^n(E).
$$

**命题 4.19。** *设 $E$ 为 $R$ 上维数 $n$ 的自由模，$\{\Delta\}$ 为 $L_a^n(E)$ 的基，$f:E\to E$ 为 $E$ 的自同态，则*

$$
f^*\Delta=D(f)\Delta.
$$

**证明。** 这是定理 4.11 的直接推论。具体地，取 $\{v_1,\ldots,v_n\}$ 为 $E$ 的基，再取 $A$（或 ${}^tA$）为 $f$ 关于该基的矩阵。由定义，

$$
f^*\Delta(v_1,\ldots,v_n)=\Delta(f(v_1),\ldots,f(v_n)),
$$

<span class="original-page-anchor" id="pdf-page-530" aria-hidden="true"></span>

而由定理 4.11，它等于

$$
D(A)\Delta(v_1,\ldots,v_n).
$$

由推论 4.12，因这两个形式在 $(v_1,\ldots,v_n)$ 上取相同的值，便得到 $f^*\Delta=D(A)\Delta$。

上述讨论把行列式看成自由模的所有自同态上的函数。也可以从乘法的角度把它看成同态

$$
\det:GL_n(R)\to R^*,
$$

从 $R$ 上可逆的 $n\times n$ 矩阵群映入 $R$ 的可逆元群。这个同态的核由行列式为 $1$ 的矩阵组成，称为**特殊线性群**，记作 $SL_n(R)$。

现在把行列式应用于第三章定理 7.8 中考虑的自由模及其子模的情形。

**命题 4.20。** *设 $R$ 为主理想整环，$F$ 为 $R$ 上的自由模，$M$ 为有限生成子模。设 $\{e_1,\ldots,e_m,\ldots\}$ 为 $F$ 的基，且存在非零元素 $a_1,\ldots,a_m\in R$，满足：*

*（i）元素 $a_1e_1,\ldots,a_me_m$ 构成 $M$ 在 $R$ 上的基。*

*（ii）对 $i=1,\ldots,m-1$，有 $a_i\mid a_{i+1}$。*

*设 $L_a^s$ 为 $F$ 上所有 $s$ 重线性交替形式的集合。设 $J_s$ 为所有元素 $f(y_1,\ldots,y_s)$ 生成的理想，其中 $f\in L_a^s$，$y_1,\ldots,y_s\in M$。则*

$$
J_s=(a_1\cdots a_s).
$$

> **译校注：** 这里的乘积按已列出的 $a_1,\ldots,a_m$ 解释，需取 $1\le s\le m$。若 $s>m$，交替性使所有这些值为零，因此 $J_s=0$，而原书没有定义此时右边的 $a_s$。

**证明。** 先证明 $J_s\subset(a_1\cdots a_s)$。事实上，元素 $y\in M$ 可写为

$$
y=c_1a_1e_1+\cdots+c_ra_re_r.
$$

若 $y_1,\ldots,y_s\in M$，且 $f$ 为 $F$ 上的多线性交替映射，则 $f(y_1,\ldots,y_s)$ 是形如

$$
c_{i_1}\cdots c_{i_s}a_{i_1}\cdots a_{i_s}f(e_{i_1},\ldots,e_{i_s})
$$

的各项之和。只有当 $e_{i_1},\ldots,e_{i_s}$ 互不相同时，该项才可能非零。这时乘积 $a_1\cdots a_s$ 整除该项，所以 $J_s$ 包含于所述理想。

反之，证明存在一个 $s$ 重线性交替形式，它恰好给出这个乘积。由行列式可推得这一点。可把 $F$ 写成直和

$$
F=(e_1,\ldots,e_r)\oplus F_r
$$

<span class="original-page-anchor" id="pdf-page-531" aria-hidden="true"></span>

其中 $F_r$ 为某个子模。设 $f_i$（$i=1,\ldots,r$）为线性映射 $F\to R$，满足 $f_i(e_j)=\delta_{ij}$，且在 $F_r$ 上取值为 $0$。对于 $v_1,\ldots,v_s\in F$，定义

$$
f(v_1,\ldots,v_s)=\det(f_i(v_j)).
$$

> **译校注：** 此处行列式取 $1\le i,j\le s$，即使用前 $s$ 个坐标函数；若直接把原文所列的全部 $r$ 个 $f_i$ 用作行，则 $r\ne s$ 时不是方阵。前页表示 $y\in M$ 的线性组合中，$r$ 可取命题中的 $m$；构造本形式时只需前 $s$ 个坐标。

于是 $f$ 是多线性交替的，并取值

$$
f(e_1,\ldots,e_s)=1,
$$

> **译校注：** 原书印为 $f(e_2,\ldots,e_s)=1$，遗漏了 $e_1$。由于 $f$ 有 $s$ 个自变量，且坐标矩阵在 $(e_1,\ldots,e_s)$ 上为单位矩阵，这里补回 $e_1$。

同时有

$$
f(a_1e_1,\ldots,a_se_s)=a_1\cdots a_s.
$$

这证明了命题。

第三章定理 7.8 的唯一性现在很明显：首先 $(a_1)$ 唯一，然后 $(a_1a_2)$ 唯一，其商 $(a_2)$ 唯一，如此归纳下去。

**注。** 可将上述定理与第十九章关于菲廷理想理论的定理 2.9 比较，后者为这个结果提供了更精细的背景。

## §5. 对偶性

设 $R$ 为交换环，$E,F$ 为 $R$ 模。$E\times F$ 上的 **$R$ 双线性形式**是映射

$$
f:E\times F\to R,
$$

满足以下性质：对每个 $x\in E$，映射

$$
y\mapsto f(x,y)
$$

是 $R$ 线性的；对每个 $y\in F$，映射

$$
x\mapsto f(x,y)
$$

也是 $R$ 线性的。本节余下部分省略前缀 $R$，并以 $\langle x,y\rangle_f$ 或 $\langle x,y\rangle$ 代替 $f(x,y)$。若 $x\in E$，当 $\langle x,y\rangle=0$ 时记 $x\perp y$。

> **译校注：** 原书本句印为“若 $x\in F$”，但配对 $f:E\times F\to R$ 的第一个变量及下面 $S^\perp$ 中的元素都属于 $E$，故这里改为 $x\in E$。

同样，若 $S$ 为 $F$ 的子集，当对所有 $y\in S$ 都有 $x\perp y$ 时，定义 $x\perp S$，称 $x$ **垂直于** $S$。用 $S^\perp$ 表示 $E$ 中所有垂直于 $S$ 的元素的集合，它显然是 $E$ 的子模。另一侧的垂直性以同样的方式定义。定义 $f$ 的左侧**核**为 $F^\perp$，右侧核为 $E^\perp$。若左侧核为 $0$，称 $f$ 在左侧**非退化**；若右侧核为 $0$，称 $f$ 在右侧**非退化**。若 $E_0$ 为 $f$ 的左侧核，则我们<span class="original-page-anchor" id="pdf-page-532" aria-hidden="true"></span>得到诱导的双线性映射

$$
E/E_0\times F\to R,
$$

它在左侧非退化，由定义容易验证。同样，若 $F_0$ 为 $f$ 的右侧核，便得到诱导的双线性映射

$$
E/E_0\times F/F_0\to R,
$$

它在两侧都非退化。这个映射源于以下事实：值 $\langle x,y\rangle$ 只依赖于 $x$ 模 $E_0$ 的陪集和 $y$ 模 $F_0$ 的陪集。

用 $L^2(E,F;R)$ 表示从 $E\times F$ 到 $R$ 的所有双线性映射的集合。显然，它是一个模（即 $R$ 模），映射的加法与乘以 $R$ 中元素的运算均按通常方式定义。

形式 $f$ 给出同态

$$
\varphi_f:E\to\operatorname{Hom}_R(F,R),
$$

满足对所有 $x\in E$、$y\in F$，有

$$
\varphi_f(x)(y)=f(x,y)=\langle x,y\rangle.
$$

称 $\operatorname{Hom}_R(F,R)$ 为 $F$ 的**对偶模**，记作 $F^\vee$。有同构

$$
\boxed{L^2(E,F;R)\leftrightarrow\operatorname{Hom}_R(E,\operatorname{Hom}_R(F,R))},
$$

由 $f\mapsto\varphi_f$ 给出。其逆按显然的方式定义：若

$$
\varphi:E\to\operatorname{Hom}_R(F,R)
$$

为同态，则令 $f$ 满足

$$
f(x,y)=\varphi(x)(y).
$$

若 $\varphi_f$ 为同构，称 $f$ **在左侧非奇异**；换言之，可借助该形式把 $E$ 与 $F$ 的对偶模等同。**在右侧非奇异**以类似方式定义。若 $f$ 在左侧和右侧都非奇异，则称它为**非奇异**的。

**提醒：** 非退化不一定意味着非奇异。

现在我们将得到同构

$$
\boxed{\operatorname{End}_R(E)\mapsto L^2(E,F;R)},
$$

*它依赖于一个固定的非奇异双线性映射 $f:E\times F\to R$。*

<span class="original-page-anchor" id="pdf-page-533" aria-hidden="true"></span>

设 $A\in\operatorname{End}_R(E)$ 为从 $E$ 到自身的线性映射。则映射

$$
(x,y)\mapsto\langle Ax,y\rangle=\langle Ax,y\rangle_f
$$

是双线性的；由此以线性的方式给每个 $A\in\operatorname{End}_R(E)$ 配上 $L^2(E,F;R)$ 中的双线性映射。

反之，设 $h:E\times F\to R$ 为双线性映射。给定 $x\in E$，满足 $h_x(y)=h(x,y)$ 的映射 $h_x:F\to R$ 是线性的，属于对偶空间 $F^\vee$。由假设，存在唯一的元素 $x'\in E$，使对所有 $y\in F$ 都有

$$
h(x,y)=\langle x',y\rangle.
$$

显然，对应 $x\mapsto x'$ 是从 $E$ 到自身的线性映射。因此，对每个双线性映射 $E\times F\to R$，都配上了线性映射 $E\to E$。

前两段中描述的映射显然是 $\operatorname{End}_R(E)$ 与 $L^2(E,F;R)$ 之间互逆的同构。当然，我们强调它们依赖于形式 $f$。

也可以在右侧进行同样的讨论，从而得到类似的同构

$$
\boxed{L^2(E,F;R)\leftrightarrow\operatorname{End}_R(F)},
$$

*它同样依赖于固定的非奇异形式 $f$。*

作为应用，设 $A:E\to E$ 为线性映射，$(x,y)\mapsto\langle Ax,y\rangle$ 为相应的双线性映射。存在唯一的线性映射

$$
{}^tA:F\to F,
$$

使对所有 $x\in E$、$y\in F$，都有

$$
\langle Ax,y\rangle=\langle x,{}^tAy\rangle.
$$

称 ${}^tA$ 为 **$A$ 关于 $f$ 的转置**。

立即可见，若 $A,B$ 为从 $E$ 到自身的线性映射，则对 $c\in R$，有

$$
{}^t(cA)=c\,{}^tA,\qquad{}^t(A+B)={}^tA+{}^tB,\quad{}^t(AB)={}^tB\,{}^tA.
$$

更一般地，设 $E,F$ 为带有非奇异双线性形式的模，形式分别记作 $\langle\ ,\ \rangle_E$ 和 $\langle\ ,\ \rangle_F$。设 $A:E\to F$ 为线性映射。由 $\langle\ ,\ \rangle_E$ 的非奇异性，存在唯一的线性映射 ${}^tA:F\to E$，使得

$$
\langle Ax,y\rangle_F=\langle x,{}^tAy\rangle_E\quad\text{对所有 }x\in E,\ y\in F.
$$

也称 ${}^tA$ 为关于这些形式的**转置**。

**例。** 关于转置的一个很好的经典例子，见习题 33。关于线性映射等于其转置时的系统研究，见<span class="original-page-anchor" id="pdf-page-534" aria-hidden="true"></span>第十五章的谱定理。下面再给出一个来自分析的转置的例子。设 $E$ 为 $\mathbf R$ 上具有紧支集的 $C^\infty$ 函数的（无限维）向量空间，即这些函数在某个有限区间外等于 $0$。定义标量积

$$
\langle f,g\rangle=\int_{-\infty}^{\infty}f(x)g(x)\,dx.
$$

设 $D:E\to E$ 为求导算子，则有公式

$$
\langle Df,g\rangle=-\langle f,Dg\rangle.
$$

因此可以说 ${}^tD=-D$，虽然该标量积并非“非奇异”，但非奇异形式的许多形式运算仍适用。在分析中，还会在空间上引入各种范数，并利用连续性将双线性形式延拓到完备化上；这样就从代数领域进入估计的领域（分析）。在这种分析背景下，谱定理也会变得更复杂。

假设 $E=F$，$f:E\times E\to R$ 为双线性映射。**二元组 $(E,f)$ 的自同构**，或简称 $f$ 的自同构，是指满足

$$
\langle Ax,Ay\rangle=\langle x,y\rangle
$$

对所有 $x,y\in E$ 都成立的线性自同构 $A:E\to E$。$f$ 的自同构群记作 $\operatorname{Aut}(f)$。

**命题 5.1。** *设 $f:E\times E\to R$ 为非奇异双线性形式，$A:E\to E$ 为线性映射。则 $A$ 为 $f$ 的自同构，当且仅当 ${}^tAA=\mathrm{id}$ 且 $A$ 可逆。*

**证明。** 由对所有 $x,y\in E$ 都成立的等式

$$
\langle x,y\rangle=\langle Ax,Ay\rangle=\langle x,{}^tAAy\rangle,
$$

若 $A$ 为 $f$ 的自同构，便得到 ${}^tAA=\mathrm{id}$。逆命题同样显然。

**注。** 若 $E$ 自由且有限维，则条件 ${}^tAA=\mathrm{id}$ 蕴含 $A$ 可逆。

设 $f:E\times E\to R$ 为双线性形式。若对所有 $x,y\in E$ 都有 $f(x,y)=f(y,x)$，称 $f$ 为**对称**的。$E$ 上的对称双线性形式的集合记作 $L_s^2(E)$。固定 $E$ 上一个对称非奇异双线性形式 $f$，记作 $(x,y)\mapsto\langle x,y\rangle$。若自同态 $A:E\to E$ 满足 ${}^tA=A$，称它**关于 $f$ 对称**。显然，$E$ 的对称自同态的集合是模，记作 $\operatorname{Sym}(E)$。

<span class="original-page-anchor" id="pdf-page-535" aria-hidden="true"></span>

*依赖于固定的对称非奇异形式 $f$，有同构*

$$
\boxed{L_s^2(E)\leftrightarrow\operatorname{Sym}(E)},
$$

其描述如下。若 $g$ 为 $E$ 上的对称双线性形式，则存在唯一的线性映射 $A$，使对所有 $x,y\in E$，都有

$$
g(x,y)=\langle Ax,y\rangle.
$$

利用 $f,g$ 都对称，得到

$$
\langle Ax,y\rangle=\langle Ay,x\rangle=\langle y,{}^tAx\rangle=\langle{}^tAx,y\rangle.
$$

因此 $A={}^tA$。对应 $g\mapsto A$ 给出从 $L_s^2(E)$ 到 $\operatorname{Sym}(E)$ 的同态。反之，给定 $E$ 的对称自同态 $A$，可按规则 $(x,y)\mapsto\langle Ax,y\rangle$ 定义对称形式；给 $A$ 配上这个形式，显然给出从 $\operatorname{Sym}(E)$ 到 $L_s^2(E)$ 的同态，它与前一个同态互逆。因此，$\operatorname{Sym}(E)$ 与 $L_s^2(E)$ 同构。

回顾：若双线性形式 $g:E\times E\to R$ 对所有 $x\in E$ 都满足 $g(x,x)=0$，就称它为**交替**的；于是对所有 $x,y\in E$，有 $g(x,y)=-g(y,x)$。$E$ 上的双线性交替形式的集合是模，记作 $L_a^2(E)$。

固定 $E$ 上的一个*对称*非奇异双线性形式 $f$。若自同态 $A:E\to E$ 满足 ${}^tA=-A$，并且对所有 $x\in E$ 都有 $\langle Ax,x\rangle=0$，称它关于 $f$ **斜对称**或**交替**。若对所有 $a\in R$，$2a=0$ 都蕴含 $a=0$，则第二个条件 $\langle Ax,x\rangle=0$ 是多余的，因为 $\langle Ax,x\rangle=-\langle Ax,x\rangle$ 蕴含 $\langle Ax,x\rangle=0$。显然，$E$ 的交替自同态的集合是模，记作 $\operatorname{Alt}(E)$。*依赖于固定的对称非奇异形式 $f$，有同构*

$$
\boxed{L_a^2(E)\leftrightarrow\operatorname{Alt}(E)},
$$

按通常的方式描述。若 $g$ 为 $E$ 上的交替双线性形式，则相应的线性映射 $A$ 满足对所有 $x,y\in E$，有

$$
g(x,y)=\langle Ax,y\rangle.
$$

用与对称情形类似的方法，容易验证对应 $g\leftrightarrow A$ 给出了所要的同构。

**例。** 设 $k$ 为域，$E$ 为 $k$ 上有限维向量空间。设 $f:E\times E\to E$ 为双线性映射，记作 $(x,y)\mapsto xy$。对于每个<span class="original-page-anchor" id="pdf-page-536" aria-hidden="true"></span>$x\in E$，配上线性映射 $\lambda_x:E\mapsto E$，使

$$
\lambda_x(y)=xy.
$$

随后取迹得到的映射

$$
(x,y)\mapsto\operatorname{tr}(\lambda_{xy})
$$

是 $E$ 上的双线性形式。若 $xy=yx$，则该双线性形式对称。

其次，设 $E$ 为区间 $[0,1]$ 上的连续函数空间。设 $K(s,t)$ 为定义在正方形 $0\le s\le1$、$0\le t\le1$ 上的二元实连续函数。对 $\varphi,\psi\in E$，定义

$$
\langle\varphi,\psi\rangle=\iint\varphi(s)K(s,t)\psi(t)\,ds\,dt,
$$

二重积分在该正方形上进行。于是得到 $E$ 上的双线性形式。若 $K(s,t)=K(t,s)$，则它对称。下一节讨论矩阵与双线性形式时，读者会注意到上式与矩阵定义的双线性形式之间的相似性。

第三，设 $U$ 为实巴拿赫空间 $E$ 的开子集（若读者坚持，也可取有限维欧几里得空间），$f:U\to\mathbf R$ 为二阶连续可微映射。对每个 $x\in U$，导数 $Df(x):E\to\mathbf R$ 是连续线性映射，二阶导数 $D^2f(x)$ 可视为从 $E\times E$ 到 $\mathbf R$ 的连续对称双线性映射。

## §6. 矩阵与双线性形式

我们将研究上述概念与矩阵的关系。设 $f:E\times F\to R$ 为双线性映射，且 $E,F$ 在 $R$ 上自由。设 $\mathcal B=\{v_1,\ldots,v_m\}$ 为 $E$ 在 $R$ 上的基，$\mathcal B'=\{w_1,\ldots,w_n\}$ 为 $F$ 在 $R$ 上的基。令 $g_{ij}=\langle v_i,w_j\rangle$。若

$$
x=x_1v_1+\cdots+x_mv_m
$$

和

$$
y=y_1w_1+\cdots+y_nw_n
$$

分别为 $E,F$ 中的元素，其坐标 $x_i,y_j\in R$，则

$$
\langle x,y\rangle=\sum_{i=1}^m\sum_{j=1}^n g_{ij}x_iy_j.
$$

<span class="original-page-anchor" id="pdf-page-537" aria-hidden="true"></span>

设 $X,Y$ 分别是 $x,y$ 关于所选基的坐标列向量。那么

$$
\langle x,y\rangle={}^tXGY,
$$

其中 $G$ 是矩阵 $(g_{ij})$。我们可以写成 $G=M_{\mathfrak{B}'}^{\mathfrak{B}}(f)$。称 $G$ 为**型 $f$ 关于基 $\mathfrak{B},\mathfrak{B}'$ 的矩阵**。

反之，给定一个 $m\times n$ 矩阵 $G$，由映射

$$
(X,Y)\longmapsto{}^tXGY
$$

可以得到一个双线性型。

这样，我们得到双线性型与矩阵之间的双向对应；显然，这个对应诱导一个（$R$ 模的）*同构*

$$
\boxed{L^2(E,F;R)\longleftrightarrow\operatorname{Mat}_{m\times n}(R)},
$$

它由

$$
f\longmapsto M_{\mathfrak{B}'}^{\mathfrak{B}}(f)
$$

给出。上述两个模之间的两个映射显然互为逆映射。

如果我们有基 $\mathfrak{B}=\{v_1,\ldots,v_n\}$ 和 $\mathfrak{B}'=\{w_1,\ldots,w_n\}$，满足 $\langle v_i,w_j\rangle=\delta_{ij}$，就称这两组基互为**对偶基**。在这种情况下，若 $X$ 是 $E$ 中一个元素的坐标向量，$Y$ 是 $F$ 中一个元素的坐标向量，那么这个双线性映射在 $X,Y$ 上的值就是通常的点积

$$
X\cdot Y=x_1y_1+\cdots+x_ny_n.
$$

一般地，不难推导当我们改变 $E$ 和 $F$ 的基时，矩阵 $G$ 如何变化。不过，我们只在 $E=F$ 且 $\mathfrak{B}=\mathfrak{B}'$ 时写出显式公式。因此，我们有一个双线性型 $f:E\times E\to R$。设 $\mathfrak{C}$ 是 $E$ 的另一组基，用 $X_{\mathfrak{B}}$ 和 $X_{\mathfrak{C}}$ 分别表示 $E$ 的元素 $x$ 关于这两组基的列向量。设 $C$ 是*可逆矩阵* $M_{\mathfrak{B}}^{\mathfrak{C}}(\operatorname{id})$，使得

$$
X_{\mathfrak{B}}=CX_{\mathfrak{C}}.
$$

那么我们的型由

$$
\langle x,y\rangle={}^tX_{\mathfrak{C}}{}^tCGCY_{\mathfrak{C}}
$$

给出。

*可以看出*

$$
M_{\mathfrak{C}}^{\mathfrak{C}}(f)={}^tCM_{\mathfrak{B}}^{\mathfrak{B}}(f)C.\tag{1}
$$

换言之，双线性型的矩阵通过*转置*作变换。

<span class="original-page-anchor" id="pdf-page-538" aria-hidden="true"></span>

*如果 $F$ 是 $R$ 上的自由模，具有基 $\{\eta_1,\ldots,\eta_n\}$，那么 $\operatorname{Hom}_R(F,R)$ 也是自由模，并且有一组对偶基 $\{\eta'_1,\ldots,\eta'_n\}$，满足*

$$
\eta'_i(\eta_j)=\delta_{ij}.
$$

这一点已经在第三章定理 6.1 中提到。

**命题 6.1。** *设 $E,F$ 是 $R$ 上维数为 $n$ 的自由模，$f:E\times F\to R$ 是一个双线性型。那么下列条件等价：*

*$f$ 左非奇异。*

*$f$ 右非奇异。*

*$f$ 非奇异。*

*$f$ 关于任意基的矩阵的行列式在 $R$ 中可逆。*

*证明。* 假设 $f$ 左非奇异。固定 $E$ 和 $F$ 的基，我们把这些模的元素关于所选基写成列向量，并得到 $f$ 的矩阵 $G$。于是我们的型由

$$
(X,Y)\longmapsto{}^tXGY
$$

给出，其中 $X,Y$ 是系数属于 $R$ 的列向量。由假设，映射

$$
X\longmapsto{}^tXG
$$

给出了列向量模与 $R$ 上长度为 $n$ 的行向量模之间的同构。因此 $G$ 可逆，从而其行列式是 $R$ 中的可逆元。逆命题同样清楚；如果 $\det(G)$ 是可逆元，我们看出映射

$$
Y\longrightarrow GY
$$

也必然是列向量模到自身的同构。这就证明了我们的断言。

现在我们研究转置在矩阵表示下的行为。设 $E,F$ 是 $R$ 上维数为 $n$ 的自由模。

设 $f:E\times F\to R$ 是一个非奇异双线性型，并给定 $E$ 的一组基 $\mathfrak{B}$ 和 $F$ 的一组基 $\mathfrak{B}'$。设 $G$ 是 $f$ 关于这些基的矩阵。设 $A:E\to E$ 是一个线性映射。

> **译校注：** 原书这里印作 $A:E\to F$。下文把 $A$ 关于 $E$ 的同一组基 $\mathfrak{B}$ 表示为矩阵，并将 $Ax$ 放入型的第一个变量；下一页命题 6.2 也明确写作 $A:E\to E$。因此这里的到达模应为 $E$。

若 $x\in E$、$y\in F$，用 $X,Y$ 表示它们关于 $\mathfrak{B},\mathfrak{B}'$ 的列向量。设 $M$ 是 $A$ 关于 $\mathfrak{B}$ 的矩阵。那么对于 $x\in E$ 和 $y\in F$，有

$$
\langle Ax,y\rangle={}^t(MX)GY={}^tX{}^tMGY.
$$

设 $N$ 是 ${}^tA$ 关于基 $\mathfrak{B}'$ 的矩阵。那么 $NY$ 是 ${}^tAy$ 关于 $\mathfrak{B}'$ 的列向量。因此

$$
\langle x,{}^tAy\rangle={}^tXGNY.
$$

<span class="original-page-anchor" id="pdf-page-539" aria-hidden="true"></span>

由此得到 ${}^tMG=GN$，而 $G$ 可逆，因而可以用 $M$ 表示 $N$。我们得到：

**命题 6.2。** *设 $E,F$ 是 $R$ 上维数为 $n$ 的自由模，$f:E\times F\to R$ 是非奇异双线性型。设 $\mathfrak{B},\mathfrak{B}'$ 分别是 $E$ 和 $F$ 在 $R$ 上的基，$G$ 是 $f$ 关于这些基的矩阵。设 $A:E\to E$ 是线性映射，$M$ 是它关于 $\mathfrak{B}$ 的矩阵。那么 ${}^tA$ 关于 $\mathfrak{B}'$ 的矩阵为*

$$
(G^{-1}){}^tMG.
$$

**推论 6.3。** *如果 $G$ 是单位矩阵，那么转置映射的矩阵等于原映射矩阵的转置。*

用矩阵与基来表述，就得到矩阵诱导型的自同构的如下刻画。

**推论 6.4。** *沿用命题 6.2 的记号，并设 $E=F$、$\mathfrak{B}=\mathfrak{B}'$。一个 $n\times n$ 矩阵 $M$ 是型 $f$ 的一个自同构的矩阵（关于所选基），当且仅当*

$$
{}^tMGM=G.
$$

*若这个条件成立，则特别地，$M$ 可逆。*

*证明。* 使用定义以及命题 6.2 给出的公式即可。注意 $M$ 可逆，例如因为它的行列式是 $R$ 中的可逆元。

如果 ${}^tM=M$，称矩阵 $M$ 为**对称矩阵**；如果 ${}^tM=-M$ 且 $M$ 的对角元均为 $0$，称它为**交错矩阵**。

设 $f:E\times E\to R$ 是双线性型。如果对所有 $x,y\in E$，都有 $f(x,y)=f(y,x)$，称 $f$ 为**对称型**。如果对所有 $x\in E$，都有 $f(x,x)=0$，称 $f$ 为**交错型**。

**命题 6.5。** *设 $E$ 是 $R$ 上维数为 $n$ 的自由模，$\mathfrak{B}$ 是一组固定的基。映射*

$$
f\longmapsto M_{\mathfrak{B}}^{\mathfrak{B}}(f)
$$

*诱导一个同构，把 $E\times E$ 上的对称双线性型模（分别地，$E\times E$ 上的交错型模）映到 $R$ 上的对称 $n\times n$ 矩阵模（分别地，$R$ 上的交错 $n\times n$ 矩阵模）。*

<span class="original-page-anchor" id="pdf-page-540" aria-hidden="true"></span>

*证明。* 先考虑对称情形。假设 $f$ 对称。在坐标表示下，设 $G=M_{\mathfrak{B}}^{\mathfrak{B}}(f)$。我们的型由 ${}^tXGY$ 给出，由对称性，它必须等于 ${}^tYGX$。然而，${}^tXGY$ 可以看作一个 $1\times1$ 矩阵，它等于其转置，即 ${}^tY{}^tGX$。因此，对于所有向量 $X,Y$，都有

$$
{}^tYGX={}^tY{}^tGX.
$$

由此得到 $G={}^tG$。反之，显然任意对称矩阵都定义一个对称型。

至于交错情形，在关系 $\langle x,x\rangle=0$ 中把 $x$ 换成 $x+y$，得到

$$
\langle x,y\rangle+\langle y,x\rangle=0.
$$

用坐标向量 $X,Y$ 和矩阵 $G$ 表示，这给出

$$
{}^tXGY+{}^tYGX=0.
$$

例如对这个关系中的第二个 $1\times1$ 矩阵取转置，就得到（对于所有 $X,Y$）：

$$
{}^tXGY+{}^tX{}^tGY=0.
$$

因此 $G+{}^tG=0$。此外，令 $X$ 为任意一个单位向量

$$
{}^t(0,\ldots,0,1,0,\ldots,0),
$$

并使用关系 ${}^tXGX=0$，可知 $G$ 的对角元必定均为 $0$。反之，如果 $G$ 是一个 $n\times n$ 矩阵，满足 ${}^tG+G=0$，且 $g_{ii}=0$（$i=1,\ldots,n$），则立即可以验证映射

$$
(X,Y)\longmapsto{}^tXGY
$$

定义了一个交错型。这就证明了命题。

当然，如果像通常的情形那样，$2$ 在 $R$ 中可逆，那么条件 ${}^tM=-M$ 蕴含 $M$ 的对角元必为 $0$。因此在这种情况下，证明 $G+{}^tG=0$ 就能推出 $G$ 是交错矩阵。

## §7. 半双线性对偶

有些型并非完全是双线性的，上述结果对它们几乎不作改变就成立；但为了使所涉及的记号清楚，我们必须单独处理这些型。

<span class="original-page-anchor" id="pdf-page-541" aria-hidden="true"></span>

设 $R$ 具有一个周期为 $2$ 的自同构。我们把这个自同构写成 $a\mapsto\bar a$（并把它想作复共轭）。

遵循 Bourbaki，若一个映射

$$
f:E\times F\longrightarrow R
$$

是 $\mathbf{Z}$ 双线性的，并且对于 $x\in E$、$y\in F$ 和 $a\in R$，有

$$
f(ax,y)=af(x,y)
$$

和

$$
f(x,ay)=\bar af(x,y),
$$

就称它为一个**半双线性型**。

（**Sesquilinear** 的意思是“线性的 $1\frac12$ 倍”，所以这个术语相当贴切。）

设 $E,E'$ 是模。如果映射 $\varphi:E\to E'$ 是 $\mathbf{Z}$ 线性的，并且对所有 $x\in E$ 都有 $\varphi(ax)=\bar a\varphi(x)$，就称它为**反线性**（或**半线性**）映射。因此，可以说一个半双线性型对其第一个变量是线性的，对第二个变量是反线性的。我们用 $\overline{\operatorname{Hom}}_R(E,E')$ 表示从 $E$ 到 $E'$ 的反线性映射模。

现在我们将系统地逐一讨论前面对双线性型所作的同样说明。

如前面一样，我们定义垂直性，并定义任意半双线性型 $f$ 的右核与左核。这些核是子模，不妨分别记为 $E_0$ 和 $F_0$，于是得到一个诱导的半双线性型

$$
E/E_0\times F/F_0\longrightarrow R,
$$

它在两侧都非退化。

设 $F$ 是一个 $R$ 模。我们把它的**反模** $\bar F$ 定义为如下的模：它的加法群与 $F$ 相同，而作用 $R\times\bar F\to\bar F$ 由

$$
(a,y)\longmapsto\bar ay
$$

给出。那么 $\bar F$ 是一个模。作为 $R$ 模，我们有一个自然同构

$$
\operatorname{Hom}_R(\bar F,R)\longleftrightarrow\overline{\operatorname{Hom}}_R(F,R).
$$

半双线性型 $f:E\times F\to R$ 诱导一个线性映射

$$
\varphi_f:E\longrightarrow\operatorname{Hom}_R(\bar F,R).
$$

若 $\varphi_f$ 是同构，就称 $f$ **左非奇异**。同样，我们有一个对应的线性映射

$$
\varphi'_f:\bar F\longrightarrow\operatorname{Hom}_R(E,R)
$$

<span class="original-page-anchor" id="pdf-page-542" aria-hidden="true"></span>

从 $\bar F$ 到 $E$ 的对偶空间；如果 $\varphi'_f$ 是同构，就称 $f$ **右非奇异**。如果 $f$ 既左非奇异又右非奇异，就称它**非奇异**。

我们注意到，半双线性型 $f$ 可以看作一个**双线性型**

$$
f:E\times\bar F\longrightarrow R,
$$

此时我们的非奇异性概念与前面对双线性型定义的非奇异性相容。

如果我们在 $E\times F$ 上固定一个非奇异半双线性型，那么依赖于这个型，就得到 $E\times F$ 上的半双线性型模与 $E$ 的自同态模之间的同构。还得到这些模与 $F$ 的自同态模之间的反同构。特别地，可以定义转置的类似物，在当前情形中称之为伴随。因此，设 $f:E\times F\to R$ 是非奇异半双线性型，$A:E\to E$ 是线性映射。存在唯一的线性映射

$$
A^*:F\longrightarrow F,
$$

使得对所有 $x\in E$ 和 $y\in F$，都有

$$
\langle Ax,y\rangle=\langle x,A^*y\rangle.
$$

注意，$A^*$ 是线性的，而不是反线性的。称 $A^*$ 为 $A$ 关于型 $f$ 的**伴随**。对于 $E$ 到自身的所有线性映射 $A,B$ 以及 $c\in R$，有运算法则

$$
(cA)^*=\bar cA^*,\qquad(A+B)^*=A^*+B^*,\qquad(AB)^*=B^*A^*.
$$

假设 $E=F$。设 $f:E\times E\to R$ 是半双线性的。与双线性型的情形一样，所谓 $f$ 的一个**自同构**，是指满足

$$
\langle Ax,Ay\rangle=\langle x,y\rangle
$$

的线性自同构 $A:E\to E$。

**命题 7.1。** *设 $f:E\times E\to R$ 是非奇异半双线性型，$A:E\to E$ 是线性映射。那么 $A$ 是 $f$ 的自同构，当且仅当 $A^*A=\operatorname{id}$ 且 $A$ 可逆。*

这个命题的证明以及后续命题的证明，与双线性情形的证明完全类似，故予以省略。

若半双线性型 $g:E\times E\to R$ 对所有 $x,y\in E$ 满足

$$
g(x,y)=\overline{g(y,x)},
$$

就称它为 **Hermite 型**。$E$ 上 Hermite 型的集合记为 $L_h^2(E)$。设 $R_0$ 为 $R$ 的子环，由我们的自同构所固定的所有元素组成<span class="original-page-anchor" id="pdf-page-543" aria-hidden="true"></span>$a\to\bar a$（即由满足 $a=\bar a$ 的所有元素 $a\in R$ 组成）。那么 $L_h^2(E)$ 是一个 $R_0$ 模。

我们在 $E$ 上固定一个非奇异 Hermite 型 $f$，记为 $(x,y)\mapsto\langle x,y\rangle$。若自同态 $A:E\to E$ 满足 $A^*=A$，就称它关于 $f$ 是 **Hermite 的**。显然，Hermite 自同态的集合是一个 $R_0$ 模，记为 $\operatorname{Herm}(E)$。*依赖于固定的非奇异 Hermite 型 $f$，我们有一个 $R_0$ 同构*

$$
\boxed{L_h^2(E)\longleftrightarrow\operatorname{Herm}(E)},
$$

它按通常的方式描述。一个 Hermite 型 $g$ 对应一个 Hermite 映射 $A$，当且仅当对于所有 $x,y\in E$，都有

$$
g(x,y)=\langle Ax,y\rangle.
$$

现在可以像对双线性型所做的那样，描述这些概念与矩阵之间的关系。

从一个半双线性型 $f:E\times F\to R$ 开始。

如果 $E,F$ 是自由模，并且像前面一样选定了基，那么又可以给这个型对应一个矩阵 $G$；用坐标向量 $X,Y$ 表示，我们的半双线性型由

$$
(X,Y)\longmapsto{}^tXG\bar Y
$$

给出，其中 $\bar Y$ 是对 $Y$ 的每个分量施加该自同构得到的。

如果 $E=F$，并且左右使用同一组基，那么沿用公式 (1) 的记号，在 $f$ 为半双线性型时，公式变为

$$
M_{\mathfrak{C}}^{\mathfrak{C}}(f)={}^tCM_{\mathfrak{B}}^{\mathfrak{B}}(f)\bar C.\tag{1S}
$$

*自同构出现在公式中。*

**命题 7.2。** *设 $E,F$ 是 $R$ 上维数为 $n$ 的自由模，$f:E\times F\to R$ 是一个半双线性型。那么下列条件等价。*

*$f$ 左非奇异。*

*$f$ 右非奇异。*

*$f$ 非奇异。*

*$f$ 关于任意基的矩阵的行列式在 $R$ 中可逆。*

<span class="original-page-anchor" id="pdf-page-544" aria-hidden="true"></span>

**命题 7.3。** *设 $E,F$ 是 $R$ 上维数为 $n$ 的自由模，$f:E\times F\to R$ 是非奇异半双线性型。设 $\mathfrak{B},\mathfrak{B}'$ 分别是 $E$ 和 $F$ 在 $R$ 上的基，$G$ 是 $f$ 关于这些基的矩阵。设 $A:E\to E$ 是线性映射，$M$ 是它关于 $\mathfrak{B}$ 的矩阵。那么 $A^*$ 关于 $\mathfrak{B}'$ 的矩阵为*

$$
(\bar G^{-1}){}^t\bar M\bar G.
$$

**推论 7.4。** *如果 $G$ 是单位矩阵，那么 $A^*$ 的矩阵等于 ${}^t\bar M$。*

**推论 7.5。** *沿用命题中的记号，设 $\mathfrak{B}=\mathfrak{B}'$ 是 $E$ 的一组基。一个 $n\times n$ 矩阵 $M$ 是 $f$ 的一个自同构的矩阵（关于所选基），当且仅当*

$$
{}^tMG\bar M=G.
$$

如果 ${}^tM=\bar M$，就称矩阵 $M$ 为 **Hermite 矩阵**。

像前面一样，设 $R_0$ 是 $R$ 中由自同构 $a\mapsto\bar a$ 所固定的所有元素组成的子环（即由满足 $a=\bar a$ 的所有元素 $a\in R$ 组成）。

**命题 7.6。** *设 $E$ 是 $R$ 上维数为 $n$ 的自由模，$\mathfrak{B}$ 是一组基。映射*

$$
f\longmapsto M_{\mathfrak{B}}^{\mathfrak{B}}(f)
$$

*诱导一个 $R_0$ 同构，把 $E$ 上的 Hermite 型的 $R_0$ 模映到 $R$ 中的 $n\times n$ Hermite 矩阵的 $R_0$ 模。*

**注。** 如果我们一开始就假设自同构 $a\to\bar a$ 的周期为 $2$ 或 $1$（即允许它是恒等映射），那么双线性型与对称型的结果就成为本节结果的特例。然而，记号上的差异相当令人困扰，足以使我们像上面那样重复陈述这些结果。

### 术语

由于某种令人困惑的原因，向量空间上一个对称型（分别地，交错型、Hermite 型）的自同构群，被称为这个型的**正交群**（分别地，**辛群**、**酉群**）。“正交”一词特别不恰当，因为正交映射所保持的不仅是正交性：它还保持标量积，即长度。此外，“辛”一词也不恰当。原来，在某些除环上（具有阶为 $2$ 的自同构）也可以讨论 Hermite 型，而它们的自同构群也被称为辛群，这就与该词用于交错型的情形造成了实质性的混淆。

<span class="original-page-anchor" id="pdf-page-545" aria-hidden="true"></span>

为了统一并改进术语，我曾与几个人讨论这个问题；看来可以采用以下约定。

如正文所说，任意型 $f$ 的自同构群记为 $\operatorname{Aut}(f)$。

另一方面，有一个标准型，在实数上用坐标表示为

$$
f(x,x)=x_1^2+\cdots+x_n^2,
$$

在复数上表示为

$$
f(x,x)=x_1\bar x_1+\cdots+x_n\bar x_n,
$$

在四元数上也由复数情形中的同一公式表示。这个型的自同构群可以称为**酉群**，记为 $U_n$。这个群的实点群（分别地，复点群、四元数点群）可以记为

$$
U_n(\mathbf{R}),\qquad U_n(\mathbf{C}),\qquad U_n(\mathbf{K}),
$$

并且这三个群可以称为**实酉群**（分别地，**复酉群**、**四元数酉群**）。同样，对于四元数的任意子域或子环 $k$，$U_n$ 的 $k$ 点群可以记为 $U_n(k)$。最后，如果 $f$ 是标准交错型，其矩阵为

$$
\begin{pmatrix}0&I_n\\-I_n&0\end{pmatrix},
$$

就可以把它的自同构群记为 $A_{2n}$，称为**交错型群**；若没有与置换群混淆的危险，也可以简称交错群。交错型群在域 $k$ 中的点群则可以记为 $A_{2n}(k)$。

照例，$\operatorname{Aut}(f)$ 中由行列式为 $1$ 的元素组成的子群，可以在前面加上字母 $S$ 来表示，并仍称为**特殊群**。在四种标准情形中，得到

$$
SU_n(\mathbf{R}),\qquad SU_n(\mathbf{C}),\qquad SU_n(\mathbf{K}),\qquad SA_{2n}(k).
$$

## §8. $SL_2(F)/\pm1$ 的单性

设 $F$ 是一个域，$n$ 是一个正整数。$GL_n(F)$ 表示 $F$ 上 $n\times n$ 可逆矩阵组成的群。$SL_n(F)$ 表示其中行列式等于 $1$ 的矩阵组成的子群。$PGL_n(F)$ 表示 $GL_n(F)$ 关于标量矩阵子群（这个子群包含在中心中）的商群。

<span class="original-page-anchor" id="pdf-page-546" aria-hidden="true"></span>

$PSL_n(F)$ 的定义类似。在本节中，我们希望给出矩阵在 $SL_2$ 的群论结构中的一个应用。对于 $n\geq3$ 的 $SL_n$，相应论述将在下一节证明。

$GL_2$ 的**标准 Borel 子群** $B$ 是由所有矩阵

$$
\begin{pmatrix}a&b\\0&d\end{pmatrix}
$$

组成的群，其中 $a,b,d\in F$ 且 $ad\ne0$。对于 $SL_2$ 的 Borel 子群，还要求 $ad=1$。所谓 **Borel 子群**，是指与标准 Borel 子群共轭的子群（在 $GL_2$ 或 $SL_2$ 中）。设 $U$ 为由矩阵

$$
u(b)=\begin{pmatrix}1&b\\0&1\end{pmatrix},\quad b\in F
$$

组成的群。

设 $A$ 为由对角矩阵

$$
\begin{pmatrix}a&0\\0&d\end{pmatrix},\quad a,d\in F^*
$$

组成的群。

令

$$
s(a)=\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix},\quad a\in F^*,
$$

以及

$$
w=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

本节以下令

$$
G=GL_2(F)\quad\text{或}\quad SL_2(F).
$$

**引理 8.1。** *矩阵*

$$
X(b)=\begin{pmatrix}1&b\\0&1\end{pmatrix}\quad\text{和}\quad Y(c)=\begin{pmatrix}1&0\\c&1\end{pmatrix}
$$

*生成 $SL_2(F)$。*

*证明。* 在一个任意的 $SL_2(F)$ 元素左右乘以上述类型的矩阵，相当于初等行变换与列变换，即把一行的标量倍加到另一行上，等等。因此，通过这样的乘法，总可以把给定矩阵化成形如

$$
\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix}
$$

<span class="original-page-anchor" id="pdf-page-547" aria-hidden="true"></span>

的形式。我们希望在 $a\ne1$ 时把这个矩阵表示为

$$
\begin{pmatrix}1&x\\0&1\end{pmatrix}\begin{pmatrix}1&0\\b&1\end{pmatrix}\begin{pmatrix}1&c\\0&1\end{pmatrix}\begin{pmatrix}1&0\\d&1\end{pmatrix}.
$$

矩阵乘法表明，这个方程可以求解：任取 $x\ne0$，然后依次解出 $b,c,d$，使得

$$
1+bx=a,\quad c=\frac{-x}{1+bx},\quad d=\frac{-b}{1+bc}.
$$

于是得到 $1+bc=(1+xb)^{-1}$ 以及两个对称的条件

$$
b+bcd+d=0\qquad c+bcx+x=0.
$$

这就得到了所需的表示，从而证明了引理。

设 $\bar U$ 为由下三角矩阵

$$
\begin{pmatrix}1&0\\c&1\end{pmatrix}
$$

组成的群。于是可以看出

$$
wUw^{-1}=\bar U.
$$

还要注意共轭关系

$$
w\begin{pmatrix}a&0\\0&d\end{pmatrix}w^{-1}=\begin{pmatrix}d&0\\0&a\end{pmatrix},
$$

因此 $w$ 正规化 $A$。同样，

$$
wBw^{-1}=\bar B
$$

是下三角矩阵群。

注意到

$$
B=AU=UA,
$$

并且 $A$ 正规化 $U$。

$G$ 可以分解为互不相交的子集：

$$
G=B\cup BwB.
$$

事实上，把 $G$ 看作从左边作用于列向量的群。向量

$$
e^1=\begin{pmatrix}1\\0\end{pmatrix}
$$

的稳定子显然是 $U$。

> **译校注：** 原书“稳定子是 $U$”对 $G=SL_2(F)$ 成立。若 $G=GL_2(F)$，由矩阵乘以 $e^1$ 可直接看出，稳定子应为 $\left\{\begin{pmatrix}1&b\\0&d\end{pmatrix}:b\in F,\ d\in F^*\right\}$。这个较大的稳定子仍包含在 $B$ 中，所以下页的 Bruhat 分解论证仍适用。另应注意，$Be^1$ 由非零向量组成；原书跨页的“所有第二分量为 $0$ 的列向量”应排除零向量。

轨道 $Be^1$ 由所有第二<span class="original-page-anchor" id="pdf-page-548" aria-hidden="true"></span>分量为 $0$ 的列向量组成。另一方面，

$$
we^1=\begin{pmatrix}0\\-1\end{pmatrix},
$$

因此轨道 $Bwe^1$ 由所有第二分量不为 $0$、第一分量任意的向量组成。由于 $B$ 与 $BwB$ 的这两个轨道覆盖轨道 $Ge^1$，可知 $B$ 与 $BwB$ 的并等于 $G$（因为稳定子 $U$ 包含在 $B$ 中），而且它们显然互不相交。这个分解称为 **Bruhat 分解**。

**命题 8.2。** *Borel 子群 $B$ 是一个极大真子群。*

*证明。* 由 Bruhat 分解，不属于 $B$ 的任意元素都在 $BwB$ 中；由于 $B,BwB$ 覆盖 $G$，断言随之成立。

**定理 8.3。** *若 $F$ 至少有四个元素，那么 $SL_2(F)$ 等于它自身的交换子群。*

*证明。* 通过矩阵乘法，得到交换子关系

$$
s(a)u(b)s(a)^{-1}u(b)^{-1}=u(ba^2-b)=u(b(a^2-1)).
$$

在这个证明中令 $G=SL_2(F)$。设 $G'$ 为交换子群，并类似地设 $B'$ 为 $B$ 的交换子群。我们证明第一个断言 $G=G'$。由 $F$ 至少有四个元素的假设，可以在 $F$ 中找到一个 $a\ne0$，满足 $a^2\ne1$，于是交换子关系表明 $B'=U$。由此有 $G'\supset U$，而 $G'$ 正规，所以得到

$$
G'\supset wUw^{-1}.
$$

由引理 8.1 得出 $G'=G$。

设 $Z$ 表示 $G$ 的中心。如果 $G=SL_2(F)$，它由 $\pm I$ 组成，即 $2\times2$ 单位矩阵及其负矩阵；如果 $G=GL_2(F)$，则 $Z$ 为标量矩阵子群。

**定理 8.4。** *若 $F$ 至少有四个元素，那么 $SL_2(F)/Z$ 是单群。*

这个证明将由两个引理得出。

**引理 8.5。** *$G$ 中 $B$ 的所有共轭子群的交等于 $Z$。*

*证明。* 这是使用与 $w$ 的共轭即可得到的简单事实，留给读者。

**引理 8.6。** *设 $G=SL_2(F)$。若 $H$ 在 $G$ 中正规，则或者 $H\subset Z$，或者 $H\supset G'$。*

*证明。* 由 $B$ 的极大性，必有

$$
HB=B\quad\text{或}\quad HB=G.
$$

<span class="original-page-anchor" id="pdf-page-549" aria-hidden="true"></span>

若 $HB=B$，则 $H\subset B$。由于 $H$ 正规，可知 $H$ 包含在 $B$ 的每个共轭子群中，从而由引理 8.5 包含在中心中。另一方面，假设 $HB=G$。写成

$$
w=hb,
$$

其中 $h\in H$、$b\in B$。那么

$$
wUw^{-1}=\bar U=hbUb^{-1}h^{-1}=hUh^{-1}\subset HU,
$$

因为 $H$ 正规。由于 $U\subset HU$，而 $U,\bar U$ 生成 $SL_2(F)$，得到 $HU=G$。因此

$$
G/H=HU/H\approx U/(U\cap H)
$$

是阿贝尔群，故 $H\supset G'$，正如所要证明的。

定理 8.4 的单性直接由引理 8.6 推出。

## §9. 群 $SL_n(F)$，$n\geq3$

本节研究 $n\geq3$ 的情形，并遵循 Artin 的《Geometric Algebra》第四章的部分内容。（Artin 甚至处理了以非交换除代数作为群的底环的情形，但为简单起见，我们略去这一点。）

对于 $i,j=1,\ldots,n$、$i\ne j$ 以及 $c\in F$，令

![初等矩阵](/library/volume-86/diagrams/pdf-0549-elementary-matrix-agent537.png)

为与单位矩阵仅在第 $ij$ 个分量不同的矩阵：该分量是 $c$，而不是 $0$。称这样的 $E_{ij}(c)$ 为**初等矩阵**。注意

$$
\det E_{ij}(c)=1.
$$

若 $A$ 是任意 $n\times n$ 矩阵，那么左乘得到 $E_{ij}(c)A$，即把 $A$ 的第 $j$ 行的 $c$ 倍加到第 $i$ 行上。右乘得到 $AE_{ij}(c)$，即把第 $i$ 列的 $c$ 倍加到第 $j$ 列上。我们主要使用左乘。

对于固定的 $i\ne j$，映射

$$
c\longmapsto E_{ij}(c)
$$

<span class="original-page-anchor" id="pdf-page-550" aria-hidden="true"></span>

是从 $F$ 到 $n\times n$ 矩阵的乘法群 $GL_n(F)$ 的一个同态。

**命题 9.1。** *群 $SL_n(F)$ 由初等矩阵生成。如果 $A\in GL_n(F)$，那么 $A$ 可以写成*

$$
A=SD,
$$

*其中 $S\in SL_n(F)$，$D$ 是形如*

$$
D=\begin{pmatrix}1&0&\cdots&0\\0&1&\cdots&0\\\cdots&\cdots&\cdots&\cdots\\0&0&\cdots&d\end{pmatrix}
$$

*的对角矩阵。因此 $D$ 的对角元都是 $1$，只有右下角的分量为 $d=\det(A)$。*

*证明。* 设 $A\in GL_n(F)$。由于 $A$ 非奇异，某一行的第一个分量不为零；通过一个初等行变换，可以使 $a_{11}\ne0$。把第一行的适当倍数加到第二行，使 $a_{21}\ne0$，再把第二行的适当倍数加到第一行，使 $a_{11}=1$。然后从其他行中减去第一行的适当倍数，使 $a_{i1}=0$（$i\ne1$）。

现在对第二行与第二列重复这一过程，使 $a_{22}=1$，且当 $i>2$ 时 $a_{i2}=0$。此时还可以从第一行减去第二行的适当倍数，使 $a_{12}=0$，从而得到 $a_{i2}=0$（$i\ne2$）。

重复这个过程，直到最后剩下 $a_{nn}=d\ne0$，且 $a_{nj}=0$（$j\ne n$）。从前面的各行减去最后一行的适当倍数，就得到命题所述形式的矩阵 $D$，从而完成证明。

**定理 9.2。** *对于 $n\geq3$，$SL_n(F)$ 等于它自身的交换子群。*

*证明。* 只需证明 $E_{ij}(c)$ 是一个交换子。利用 $n\geq3$，取 $k\ne i,j$。直接计算得到

$$
E_{ij}(c)=E_{ik}(c)E_{kj}(1)E_{ik}(-c)E_{kj}(-1),
$$

这把 $E_{ij}(c)$ 表示为一个交换子。定理得证。

注意，如果矩阵 $M$ 与 $SL_n(F)$ 的每个元素都可交换，那么它必定是标量矩阵。事实上，仅仅与初等矩阵

$$
E_{ij}(1)=I+\mathbf{1}_{ij}
$$

<span class="original-page-anchor" id="pdf-page-551" aria-hidden="true"></span>

可交换，就表明 $M$ 与所有矩阵 $\mathbf{1}_{ij}$（第 $ij$ 个分量为 $1$，其他分量为 $0$）可交换，因此 $M$ 与所有矩阵可交换，是一个标量矩阵。取行列式可知，中心由 $\boldsymbol{\mu}_n(F)I$ 组成，其中 $\boldsymbol{\mu}_n(F)$ 是 $F$ 中的 $n$ 次单位根群。

设 $Z$ 为 $SL_n(F)$ 的中心；我们刚刚看到，$Z$ 是由标量为 $n$ 次单位根的标量矩阵组成的群。于是定义

$$
PSL_n(F)=SL_n(F)/Z.
$$

**定理 9.3。** *对于 $n\geq3$，$PSL_n(F)$ 是单群。*

本节余下部分用来证明这一点。把 $GL_n(F)$ 看作作用于向量空间 $E=F^n$ 的群。若 $\lambda$ 是 $E$ 上的非零泛函，令

$$
H_\lambda=\operatorname{Ker}\lambda,
$$

并称 $H_\lambda$（或简称 $H$）为**与 $\lambda$ 对应的超平面**。于是 $\dim H=n-1$。反之，若 $H$ 是一个余维为 $1$ 的子空间，则 $E/H$ 的维数为 $1$，而 $H$ 是一个泛函的核。

> **译校注：** 原书这句话末尾印作 “and is the kernel of a functional”，省略了主语。这里作为泛函核的是子空间 $H$；商空间 $E/H$ 不是所讨论的 $E$ 上泛函的核。中文将这个指代写明。

如果元素 $T\in GL_n(F)$ 固定某个超平面 $H$ 的每个元素，并且对于所有 $x\in E$，都有

$$
Tx=x+h\quad\text{（其中某个 }h\in H\text{）},
$$

就称 $T$ 为一个**错切变换**。

给定任意元素 $u\in H_\lambda$，我们用

$$
T_ux=x+\lambda(x)u
$$

定义错切变换 $T_u$。

每个错切变换都具有这种形式。若 $u,v\in H_\lambda$，立即可知

$$
T_{u+v}=T_u\circ T_v.
$$

若 $T$ 是一个错切变换，$A\in GL_n(F)$，则共轭 $ATA^{-1}$ 显然也是错切变换。

初等矩阵 $E_{ij}(c)$ 都是错切变换；采用这一几何解释来使用它们，而不是像前面一样仅从形式上处理，将是有用的。事实上，设 $e_1,\ldots,e_n$ 是构成 $F^{(n)}$ 的一组基的标准单位向量。那么当 $k\ne j$ 时，$E_{ij}(c)$ 固定 $e_k$；剩下的向量 $e_j$ 则移动了 $e_i$ 的一个倍数。取 $H$ 为由 $k\ne j$ 的 $e_k$ 生成的超平面，就看出 $E_{ij}(c)$ 是一个错切变换。

**引理 9.4。** *对于 $n\geq3$，所有不等于 $I$ 的错切变换构成 $SL_n(F)$ 中的一个共轭类。*

*证明。* 首先，选取超平面 $H=H_\lambda$ 的一组基，再加上一个元素构成 $F^{(n)}$ 的一组基，从错切变换 $T$ 的矩阵可看出 $\det T=1$，即错切变换属于 $SL_n(F)$。

<span class="original-page-anchor" id="pdf-page-552" aria-hidden="true"></span>

设 $T'$ 是关于超平面 $H'$ 的另一个错切变换。不妨设

$$
Tx=x+\lambda(x)u\quad\text{和}\quad T'x=x+\lambda'(x)u',
$$

其中 $u\in H$、$u'\in H'$。取向量 $z,z'$，满足 $\lambda(z)=1$ 和 $\lambda'(z')=1$。由于 $H$ 的一组基连同 $z$ 构成 $F^{(n)}$ 的一组基，类似地，$H'$ 的一组基连同 $z'$ 构成 $F^{(n)}$ 的一组基，因而存在一个元素 $A\in GL_n(F)$，使得

$$
Au=u',\qquad AH=H',\qquad Az=z'.
$$

随即可以验证

$$
ATA^{-1}=T',
$$

所以 $T,T'$ 在 $GL_n(F)$ 中共轭。但实际上，利用 $n\geq3$，超平面 $H,H'$ 各自包含线性无关的向量。可以把 $H'$ 中一个与 $u'$ 线性无关的基向量所对应的像乘以 $F$ 中的适当因子，使 $\det A=1$，因而 $A\in SL_n(F)$。这就证明了引理。

现在我们要证明，$GL_n(F)$ 的某些子群要么包含在中心中，要么包含 $SL_n(F)$。设 $G$ 是 $GL_n(F)$ 的一个子群。如果

$$
AGA^{-1}\subset G\quad\text{对所有 }A\in SL_n(F),
$$

就称 $G$ 为 **$SL_n$ 不变的**。

**引理 9.5。** *设 $n\geq3$，$G$ 是 $SL_n$ 不变的，并假设 $G$ 包含一个错切变换 $T\ne I$。那么 $SL_n(F)\subset G$。*

*证明。* 由引理 9.4，所有错切变换都共轭，而错切变换的集合包含初等矩阵；由命题 9.1，这些初等矩阵生成 $SL_n(F)$，所以引理成立。

**定理 9.6。** *设 $n\geq3$。如果 $G$ 是 $GL_n(F)$ 的一个 $SL_n$ 不变子群，并且不包含在 $GL_n(F)$ 的中心中，那么 $SL_n(F)\subset G$。*

*证明。* 由前面的引理，只需证明 $G$ 包含一个错切变换；这是定理 9.3 的证明中的关键步骤。

从一个移动某条直线的元素 $A\in G$ 开始。这是可能的，因为 $G$ 不包含在中心中。因此存在一个向量 $u\ne0$，使 $Au$ 不是 $u$ 的标量倍，不妨令 $Au=v$。那么 $u,v$ 包含在某个超平面 $H=\operatorname{Ker}\lambda$ 中。令 $T=T_u$，并令

$$
B=ATA^{-1}T^{-1}.
$$

那么

$$
ATA^{-1}\ne T\quad\text{且}\quad B=ATA^{-1}T^{-1}\ne I.
$$

<span class="original-page-anchor" id="pdf-page-553" aria-hidden="true"></span>

例如，把 $B$ 作用于一个任意向量 $x$，并使用 $T_u$ 的定义，就容易看出这一点。每一种情形中，总存在某个 $x$，使左边不可能等于右边。

对于任意向量 $x\in F^{(n)}$，都有

$$
Bx-x\in(u,v),
$$

其中 $(u,v)$ 是由 $u,v$ 生成的平面。因此 $BH\subset H$，从而

$$
BH=H\quad\text{且}\quad Bx-x\in H.
$$

现在分两种情形完成证明。首先，假设 $B$ 与关于 $H$ 的所有错切变换可交换。设 $w\in H$。根据定义，对于任意向量 $x$，得到

$$
BT_wx=Bx+\lambda(x)Bw
$$

$$
T_wBx=Bx+\lambda(Bx)w=Bx+\lambda(x)w.
$$

由于处于 $BT_w=T_wB$ 的情形，得到 $Bw=w$。因此 $B$ 固定 $H$ 的每个向量。我们已经看到，对所有 $x$ 都有 $Bx-x\in H$，所以 $B$ 是一个错切变换，且属于 $G$，从而在这种情形中证明了定理。

其次，假设存在一个错切变换 $T_w$（$w\in H$），使 $B$ 与 $T_w$ 不可交换。令

$$
C=BT_wB^{-1}T_w^{-1}.
$$

那么 $C\ne I$ 且 $C\in G$。此外，$C$ 是 $T_w^{-1}$ 与 $BT_wB^{-1}$ 的乘积，它们的超平面分别是 $H$ 和 $BH$；由已经证明的结果，后者也等于 $H$。因此 $C$ 是一个错切变换，因为它是具有同一超平面的错切变换的乘积。而且 $C\in G$。这就完成了第二种情形的证明，也完成了定理 9.6 的证明。

现在回到主定理，即 $PSL_n(F)$ 是单群。设 $\bar G$ 是 $PSL_n(F)$ 的一个正规子群，$G$ 是它在 $SL_n(F)$ 中的逆像。那么 $G$ 是 $SL_n$ 不变的；如果 $\bar G\ne1$，则 $G$ 不等于 $SL_n(F)$ 的中心。因此，由定理 9.6，$G$ 包含 $SL_n(F)$，因而 $\bar G=PSL_n(F)$。这就证明了 $PSL_n(F)$ 是单群。

**例。** 由第一章习题 41，或者用任何其他方法，可以看出 $PSL_2(\mathbf{F}_5)\approx A_5$（其中 $\mathbf{F}_5$ 是具有 $5$ 个元素的有限域）。如果你兴致正浓，不妨再证明

$$
PGL_2(\mathbf{F}_3)\approx S_4\quad\text{但}\quad SL_2(\mathbf{F}_3)\not\approx S_4;\quad PSL_2(\mathbf{F}_3)\approx A_4.
$$

<span class="original-page-anchor" id="pdf-page-554" aria-hidden="true"></span>

## 习题

**1.** 用线性映射 $L_A$ 的像与核的维数，解释矩阵 $A$ 的秩。

**2.** (a) 设 $A$ 是交换环 $R$ 中的一个可逆矩阵。证明 $({}^tA)^{-1}={}^t(A^{-1})$。

(b) 设 $f$ 是 $R$ 模 $E$ 上的一个非奇异双线性型，$A$ 是 $E$ 的一个 $R$ 自同构。证明 $({}^tA)^{-1}={}^t(A^{-1})$。在 Hermite 情形中证明同样的结果，即 $(A^*)^{-1}=(A^{-1})^*$。

**3.** 设 $V,W$ 是域 $k$ 上的有限维向量空间，分别给定 $V$ 与 $W$ 上的非退化双线性型，都记为 $\langle\ ,\ \rangle$。设 $L:V\to W$ 是一个满射线性映射，${}^tL$ 是它的转置；即对于 $v\in V$ 和 $w\in W$，有 $\langle Lv,w\rangle=\langle v,{}^tLw\rangle$。

(a) 证明 ${}^tL$ 是单射。

(b) 再假设若 $v\in V$ 且 $v\ne0$，则 $\langle v,v\rangle\ne0$。证明

$$
V=\operatorname{Ker}L\oplus\operatorname{Im}{}^tL,
$$

且这两个直和分量互相正交。（例子参见习题 33。）

**4.** 设 $A_1,\ldots,A_r$ 是域 $k$ 上的 $n$ 维行向量。令 $X=(x_1,\ldots,x_n)$，取 $b_1,\ldots,b_r\in k$。所谓 $k$ 中的一个线性方程组，是指形如

$$
A_1\cdot X=b_1,\ldots,A_r\cdot X=b_r
$$

的方程组。如果 $b_1=\cdots=b_r=0$，称这个方程组为齐次的。称 $n$ 为变量的个数，$r$ 为方程的个数。若齐次方程组的一个解 $X$ 满足 $x_i=0$（$i=1,\ldots,n$），就称它为**平凡解**。

(a) 证明：一个含 $n$ 个未知数、$r$ 个线性方程的齐次方程组，在 $n>r$ 时总有非平凡解。

(b) 设 $L$ 是域 $k$ 上的一个齐次线性方程组，$k$ 是 $k'$ 的子域。若 $L$ 在 $k'$ 中有非平凡解，证明它在 $k$ 中也有非平凡解。

**5.** 设 $M$ 是域 $k$ 上的 $n\times n$ 矩阵。假设对 $k$ 中所有 $n\times n$ 矩阵 $X$ 都有 $\operatorname{tr}(MX)=0$。证明 $M=0$。

**6.** 设 $S$ 是域 $k$ 上的一组 $n\times n$ 矩阵。证明：存在 $k$ 中的一个 $n$ 维非零列向量 $X$，使得对所有 $M\in S$ 都有 $MX=X$，当且仅当在 $k$ 的某个扩域 $k'$ 中存在这样的向量。

**7.** 设 $\mathbf{H}$ 是由元素 $i,j,k$ 生成的实数上的除环，其中 $i^2=j^2=k^2=-1$，且

$$
ij=-ji=k,\qquad jk=-kj=i,\qquad ki=-ik=j.
$$

那么 $\mathbf{H}$ 有一个阶为 $2$ 的自同构，由

$$
a_0+a_1i+a_2j+a_3k\longmapsto a_0-a_1i-a_2j-a_3k
$$

给出。

> **译校注：** 原书将这个四元数共轭映射称为“automorphism”。它实际上是反自同构，满足 $\overline{\alpha\beta}=\bar\beta\bar\alpha$；例如 $\overline{ij}=\bar k=-k$，而 $\bar i\bar j=(-i)(-j)=k$，因此它不是保持乘法次序的环自同构。这里保留原书称谓并指出这一差别。

把这个自同构记为 $\alpha\mapsto\bar\alpha$。$\alpha\bar\alpha$ 是什么？证明 Hermite<span class="original-page-anchor" id="pdf-page-555" aria-hidden="true"></span>型的理论可以在 $\mathbf{H}$ 上开展，$\mathbf{H}$ 称为**四元数**除环（或者不严格地称为非交换四元数域）。

**8.** 设 $N$ 是一个严格上三角 $n\times n$ 矩阵，即 $N=(a_{ij})$，且当 $i\geq j$ 时 $a_{ij}=0$。证明 $N^n=0$。

**9.** 设 $E$ 是 $k$ 上的 $n$ 维向量空间，$T:E\to E$ 是一个幂零线性映射，即对某个正整数 $m$，有 $T^m=0$。证明：存在 $E$ 在 $k$ 上的一组基，使 $T$ 关于这组基的矩阵为严格上三角矩阵。

**10.** 若 $N$ 是一个幂零 $n\times n$ 矩阵，证明 $I+N$ 可逆。

**11.** 设 $R$ 是由所有上三角 $n\times n$ 矩阵 $(a_{ij})$ 组成的集合，其中 $a_{ij}$ 属于某个域 $k$，因此当 $i>j$ 时 $a_{ij}=0$。设 $J$ 为所有严格上三角矩阵的集合。证明 $J$ 是 $R$ 的一个双边理想。你会如何描述商环 $R/J$？

**12.** 设 $G$ 是对角元非零的上三角矩阵组成的群，$H$ 是其中对角元为 $1$ 的矩阵组成的子群。（确实证明 $H$ 是一个子群。）你会如何描述商群 $G/H$？

**13.** 设 $R$ 是域 $k$ 上的 $n\times n$ 矩阵环，$L$ 是除第一列外其余分量均为 $0$ 的矩阵组成的子集。

(a) 证明 $L$ 是一个左理想。

(b) 证明 $L$ 是一个极小左理想；即若 $L'\subset L$ 是左理想且 $L'\ne0$，则 $L'=L$。（有关这种情形的更多内容，参见第七章 §5。）

**14.** 设 $F$ 是任意域，$D$ 是 $GL_n(F)$ 中的对角矩阵子群，$N$ 是 $D$ 在 $GL_n(F)$ 中的正规化子。证明 $N/D$ 同构于 $n$ 个元素上的对称群。

> **译校注（条件例外）：** 原题的“任意域”包含 $F=\mathbf F_2$。此时所有可逆对角矩阵都是单位矩阵，所以 $D=\{I\}$，$N=GL_n(\mathbf F_2)$。取 $n=2$，则 $N/D$ 的阶为 $(2^2-1)(2^2-2)=6$，而 $S_2$ 的阶为 $2$，故原题的结论在此情形不成立。当 $|F|>2$ 时，可以选取 $a\in F^*$、$a\ne1$；分别令某一对角分量为 $a$、其余为 $1$，可区分各坐标轴，使 $D$ 的共同特征直线恰为这些坐标轴。因此正规化子置换坐标轴，由单项矩阵组成，其商 $N/D$ 才同构于 $S_n$。这里保留原题，明确其有限域例外。

**15.** 设 $F$ 是具有 $q$ 个元素的有限域。证明 $GL_n(F)$ 的阶为

$$
(q^n-1)(q^n-q)\cdots(q^n-q^{n-1})=q^{n(n-1)/2}\prod_{i=1}^n(q^i-1).
$$

［*提示：* 设 $x_1,\ldots,x_n$ 是 $F^n$ 的一组基。$GL_n(F)$ 的任意元素由它在这组基上的作用唯一确定，因此 $GL_n(F)$ 的阶等于所有可能的基的个数。若 $A\in GL_n(F)$，令 $Ax_i=y_i$。$y_1$ 可以选为 $F^n$ 中 $q^n-1$ 个非零向量中的任意一个。归纳地，假设已经选定了 $y_1,\ldots,y_r$，其中 $r<n$。这些向量张成一个 $r$ 维子空间，含有 $q^r$ 个元素。$y_{r+1}$ 可以选为这个子空间之外 $q^n-q^r$ 个元素中的任意一个。由此得到公式。］

> **译校注：** 原书提示最后印作 $y_{i+1}$；这里是继已选的 $r$ 个向量之后选取下一个向量，因此指标应为 $r+1$。

**16.** 再设 $F$ 是具有 $q$ 个元素的有限域。证明 $SL_n(F)$ 的阶为

$$
q^{n(n-1)/2}\prod_{i=2}^n(q^i-1);
$$

而 $PSL_n(F)$ 的阶为

$$
\frac1d q^{n(n-1)/2}\prod_{i=2}^{n}(q^i-1),
$$

其中 $d$ 是 $n$ 与 $q-1$ 的最大公因数。

> **译校注：** 原书第二个公式的乘积上限印作 $n-1$。由 $PSL_n(F)=SL_n(F)/Z$，其阶应为上一个 $SL_n(F)$ 的阶除以中心的阶 $d$，因此乘积上限仍应为 $n$；中文公式据此校正，英文保留原式。

<span class="original-page-anchor" id="pdf-page-556" aria-hidden="true"></span>

**17.** 设 $F$ 是具有 $q$ 个元素的有限域。证明所有对角元为 $1$ 的上三角矩阵组成的群，是 $GL_n(F)$ 和 $SL_n(F)$ 的西洛子群。

**18.** 约化映射 $\mathbf{Z}\to\mathbf{Z}/N\mathbf{Z}$（其中 $N$ 是正整数）定义一个同态

$$
SL_2(\mathbf{Z})\longrightarrow SL_2(\mathbf{Z}/N\mathbf{Z}).
$$

证明这个同态是满射。［*提示：* 使用初等因子，即主理想整环 $\mathbf{Z}$ 上秩为 $2$ 的子模的结构。］

**19.** 证明 $SL_2(\mathbf{Z}/N\mathbf{Z})$ 的阶等于

$$
N^3\prod_{p\mid N}\left(1-\frac1{p^2}\right),
$$

其中乘积遍历所有整除 $N$ 的素数。

**20.** 证明存在正合列

$$
1\longrightarrow SL_2(\mathbf{Z}/N\mathbf{Z})\longrightarrow GL_2(\mathbf{Z}/N\mathbf{Z})\xrightarrow{\det}(\mathbf{Z}/N\mathbf{Z})^*\longrightarrow1.
$$

事实上，证明

$$
GL_2(\mathbf{Z}/N\mathbf{Z})=SL_2(\mathbf{Z}/N\mathbf{Z})G_N,
$$

其中 $G_N$ 是由矩阵

$$
\begin{pmatrix}1&0\\0&d\end{pmatrix},\quad d\in(\mathbf{Z}/N\mathbf{Z})^*
$$

组成的群。

**21.** 证明 $SL_2(\mathbf{Z})$ 由矩阵

$$
\begin{pmatrix}1&1\\0&1\end{pmatrix}\quad\text{和}\quad\begin{pmatrix}0&-1\\1&0\end{pmatrix}
$$

生成。

**22.** 设 $p$ 是一个不小于 $5$ 的素数，$G$ 是 $SL_2(\mathbf{Z}/p^n\mathbf{Z})$ 的一个子群，其中 $n\geq1$。假设 $G$ 在自然同态下到 $SL_2(\mathbf{Z}/p\mathbf{Z})$ 的像，是整个 $SL_2(\mathbf{Z}/p\mathbf{Z})$。证明 $G=SL_2(\mathbf{Z}/p^n\mathbf{Z})$。

*注。* 习题 22 是 Serre 对 Shimura 的一个结果的推广；参见 Serre 的《Abelian $\ell$-adic Representations and elliptic curves》，Benjamin，1968，第四章 §3，引理 3。另见我在《Elliptic Functions》中的阐述，Springer Verlag，由 Addison-Wesley 1973 年版重印，第 17 章 §4。

**23.** 设 $k$ 是每个二次多项式都有根的域，$B$ 是 $GL_2(k)$ 的 Borel 子群。证明 $G$ 是 $B$ 的所有共轭子群的并。（有限群不可能有这种情形！）

**24.** 设 $A,B$ 是域 $k$ 上同样大小的方阵，假设 $B$ 非奇异。若 $t$ 是一个变量，证明 $\det(A+tB)$ 是 $t$ 的多项式，其首项系数为 $\det(B)$，常数项为 $\det(A)$。

**25.** 设 $a_{11},\ldots,a_{1n}$ 是一个主理想环中的元素，并假设它们生成单位理想。设 $n>1$。证明存在一个以这些给定元素为第一行的矩阵 $(a_{ij})$，其行列式等于 $1$。

<span class="original-page-anchor" id="pdf-page-557" aria-hidden="true"></span>

**26.** 设 $A$ 是一个交换环，$I=(x_1,\ldots,x_r)$ 是一个理想。取 $c_{ij}\in A$，令

$$
y_i=\sum_{j=1}^r c_{ij}x_j.
$$

设 $I'=(y_1,\ldots,y_r)$，$D=\det(c_{ij})$。证明 $DI\subset I'$。

**27.** 设 $L$ 是 $\mathbf{Z}$ 上的自由模，具有基 $e_1,\ldots,e_n$。设 $M$ 是一个具有相同秩的自由子模，具有基 $u_1,\ldots,u_n$。令 $u_i=\sum c_{ij}e_j$。证明指数 $(L:M)$ 由行列式给出：

$$
(L:M)=|\det(c_{ij})|.
$$

**28.（Dedekind 行列式）。** 设 $G$ 是一个有限交换群，$F$ 是从 $G$ 到 $\mathbf{C}$ 的函数组成的向量空间。证明 $G$ 的特征标（从 $G$ 到单位根的同态）构成这个空间的一组基。若 $f:G\to\mathbf{C}$ 是一个函数，对于 $a,b\in G$，证明

$$
\det(f(ab^{-1}))=\prod_\chi\sum_{a\in G}\chi(a)f(a),
$$

其中乘积遍历所有特征标。［*提示：* 分别用特征标和 $G$ 中元素的示性函数作为 $F$ 的基，并考虑线性映射

$$
T=\sum f(a)T_a,
$$

其中 $T_a$ 是按 $a$ 的平移。］还要证明

$$
\det(f(ab^{-1}))=\left(\sum_{a\in G}f(a)\right)\det(f(ab^{-1})-f(b^{-1})),
$$

其中左边的行列式遍历所有 $a,b\in G$，右边的行列式只遍历 $a,b\ne1$。

**29.** 设 $\mathfrak{g}$ 是交换环 $R$ 上的一个模。如果双线性映射 $\mathfrak{g}\times\mathfrak{g}\to\mathfrak{g}$，记为 $(x,y)\mapsto[x,y]$，是反对称的，即 $[x,y]=-[y,x]$，而且由 $D_x(y)=[x,y]$ 定义的映射 $D_x:\mathfrak{g}\to\mathfrak{g}$ 是 $\mathfrak{g}$ 到自身的一个导子，即对所有 $x,y,z\in\mathfrak{g}$ 和 $c\in R$，有

$$
D([y,z])=[Dy,z]+[y,Dz]\quad\text{和}\quad D(cy)=cD(y),
$$

就说这个映射使 $\mathfrak{g}$ 成为一个 **Lie 代数**。

(a) 设 $A$ 是 $R$ 上的结合代数。对于 $x,y\in A$，定义 $[x,y]=xy-yx$。证明这使 $A$ 成为一个 Lie 代数。例子：一个模 $M$ 的 $R$ 自同态代数，特别是矩阵代数 $\operatorname{Mat}_n(R)$。

(b) 设 $M$ 是 $R$ 上的一个模。对于 $M$ 的两个导子 $D_1,D_2$，定义 $[D_1,D_2]=D_1D_2-D_2D_1$。证明 $M$ 的导子集合是 $\operatorname{End}_R(M)$ 的一个 Lie 子代数。

> **译校注：** 原书在 (b) 中只给出“模 $M$”，没有给出定义导子所需的乘法或 Lie 括号结构。因此此处有一个未说明的代数结构假设；这里保留原题，不自行补造这个结构。

(c) 证明映射 $x\mapsto D_x$ 是从 $\mathfrak{g}$ 到 $\mathfrak{g}$ 自身导子的 Lie 代数的一个 Lie 同态。

> **译校注：** 原书 (c) 印作 $x\mapsto\bar E_x$，但本题定义的是 $D_x(y)=[x,y]$，没有定义 $\bar E_x$。中文依照本题已给的内导子记号校作 $D_x$，英文保留印式。

**30.** 给定多项式环 $R[X_{ij}]$（$1\leq i,j\leq n$）中的一组多项式 $\{P_\nu(X_{ij})\}$，所谓这组多项式在 $R$ 中的一个**零点**，是指一个矩阵 $x=(x_{ij})$，其中 $x_{ij}\in R$，且对所有 $\nu$ 都有 $P_\nu(x_{ij})=0$。我们使用向量记号，写成 $(X)=(X_{ij})$。用 $G(R)$ 表示这些多项式的零点集合<span class="original-page-anchor" id="pdf-page-558" aria-hidden="true"></span>即多项式组 $\{P_\nu\}$ 的零点。因此 $G(R)\subset M_n(R)$；如果 $R'$ 是任意交换结合 $R$ 代数，就有 $G(R')\subset M_n(R')$。如果对于所有 $R'$，$G(R')$ 都是群 $GL_n(R')$ 的子群（其中 $GL_n(R')$ 是 $R'$ 中可逆矩阵的乘法群），就说多项式组 $\{P_\nu\}$ 定义了一个 **$R$ 上的代数群**。

例如，满足方程 ${}^tXX=I_n$ 的矩阵组成的群是一个代数群。

设 $R'$ 是一个自由的 $R$ 代数，具有基 $\{1,t\}$，其中 $t^2=0$。因此 $R'=R[t]$。设 $\mathfrak{g}$ 为满足 $I_n+tx\in G(R[t])$ 的矩阵 $x\in M_n(R)$ 组成的集合。证明 $\mathfrak{g}$ 是一个 Lie 代数。［*提示：* 注意

$$
P_\nu(I_n+tX)=P_\nu(I_n)+\operatorname{grad}P_\nu(I_n)tX.
$$

使用满足 $t^2=u^2=0$ 的代数 $R[t,u]$，证明若 $I_n+tx\in G(R[t])$ 且 $I_n+uy\in G(R[u])$，则 $[x,y]\in\mathfrak{g}$。］

（以上内容取自 [Se 65] 的前四页。关于 Lie 代数与 Lie 群的更多内容，参见 [Bo 82] 和 [Ja 79]。

[Bo 82] N. BOURBAKI，《Lie Algebras and Lie Groups》，Masson，1982

[Ja 79] N. JACOBSON，《Lie Algebras》，Dover，1979（由 Interscience 1962 年版重印）

[Se 65] J. P. SERRE，《Lie Algebras and Lie Groups》，Benjamin，1965。重印为 Springer Lecture Notes 1500，Springer/Verlag，1992

### 非交换上闭链

设 $K$ 是域 $k$ 的有限伽罗瓦扩张。令 $\Gamma=GL_n(K)$，$G=\operatorname{Gal}(K/k)$。于是 $G$ 作用于 $\Gamma$。所谓 $G$ 在 $\Gamma$ 中的一个**上闭链**，是指满足关系

$$
A(\sigma)\sigma A(\tau)=A(\sigma\tau)
$$

的一族元素 $\{A(\sigma)\}$。

若存在 $B\in\Gamma$，使得

$$
A(\sigma)=B^{-1}\sigma B\quad\text{对所有 }\sigma\in G,
$$

就称这个上闭链**分裂**。

在这个非交换情形中，上闭链不组成一个群，但可以定义一个等价关系，以定义上同调类。这里我们只关心一个上闭链是否分裂。当每个上闭链都分裂时，也说 $H^1(G,\Gamma)=0$（或 $1$）。

**31.** 证明 $H^1(G,GL_n(K))=1$。［*提示：* 设 $\{e_1,\ldots,e_N\}$ 是 $\operatorname{Mat}_n(k)$ 在 $k$ 上的一组基，例如每个矩阵仅在某个分量为 $1$、其余分量为 $0$。令

$$
x=\sum_{i=1}^N x_ie_i,
$$

其中 $x_i$ 是变量。存在一个多项式 $P(X)$，使 $x$ 可逆当且仅当 $P(x_1,\ldots,x_N)\ne0$。我们也把 $P(x_1,\ldots,x_N)$ 写作 $P(x)$。设 $\{A(\sigma)\}$ 是一个上闭链。设 $\{t_\sigma\}$ 是在 $k$ 上代数独立的变量。那么

$$
P\left(\sum_{\gamma\in G}t_\gamma A(\gamma)\right)\ne0
$$

<span class="original-page-anchor" id="pdf-page-559" aria-hidden="true"></span>

因为当一个 $t_\gamma$ 被替换为 $1$、其他变量被替换为 $0$ 时，这个多项式不为零。由伽罗瓦理论中自同构的代数独立性，存在一个元素 $y\in K$，使得若令

$$
B=\sum_\gamma(\gamma y)A(\gamma),
$$

则 $P(B)\ne0$，所以 $B$ 可逆。随即可以验证 $A(\sigma)=B\sigma B^{-1}$。但当 $k$ 有限时，参见我的《Algebraic Groups over Finite Fields》，Am. J.，第 78 卷第 3 期，1956。］

**32. 不变基。**（A. Speiser，Zahlentheoretische Sätze aus der Gruppentheorie，《Math. Z.》5（1919），第 1–6 页。另见 Kolchin-Lang，《Proc. AMS》，第 11 卷第 1 期，1960。）与前一习题一样，设 $K$ 是 $k$ 的有限伽罗瓦扩张，$G=\operatorname{Gal}(K/k)$。设 $V$ 是 $K$ 上的有限维向量空间，并假设 $G$ 作用于 $V$，使得对于 $a\in K$ 和 $v\in V$，有 $\sigma(av)=\sigma(a)\sigma(v)$。证明存在一组基 $\{w_1,\ldots,w_n\}$，使对所有 $i=1,\ldots,n$ 和所有 $\sigma\in G$，都有 $\sigma w_i=w_i$（一组不变基）。*提示：* 设 $\{v_1,\ldots,v_n\}$ 是任意一组基，令

$$
\sigma\begin{pmatrix}v_1\\\vdots\\v_n\end{pmatrix}=A(\sigma)\begin{pmatrix}v_1\\\vdots\\v_n\end{pmatrix},
$$

其中 $A(\sigma)$ 是 $GL_n(K)$ 中的矩阵。在方程 $(\sigma B)A(\sigma)=B$ 中求解 $B$，并令

$$
\begin{pmatrix}w_1\\\vdots\\w_n\end{pmatrix}=B\begin{pmatrix}v_1\\\vdots\\v_n\end{pmatrix}.
$$

以下关于调和多项式的习题源自 Whittaker，《Math. Ann.》，1902；另见 Whittaker 与 Watson，《Modern Analysis》，第十三章。

**33. 调和多项式。** 用 $\operatorname{Pol}(n,d)$ 表示特征为 $0$ 的域 $k$ 上，$n$ 个变量 $X_1,\ldots,X_n$ 的 $d$ 次齐次多项式向量空间。对于一个整数 $n$ 元组 $(\nu_1,\ldots,\nu_n)$，其中 $\nu_i\geq0$，照例用 $M_{(\nu)}$ 表示单项式

$$
M_{(\nu)}(X)=X_1^{\nu_1}\cdots X_n^{\nu_n}.
$$

证明：

(a) $d$ 次单项式的个数是 $\binom{n-1+d}{n-1}$，因而这个数就是 $\operatorname{Pol}(n,d)$ 的维数。

(b) 令 $(D)=(D_1,\ldots,D_n)$，其中 $D_i$ 是关于第 $i$ 个变量的偏导数。于是可以照例定义 $P(D)$。对于 $P,Q\in\operatorname{Pol}(n,d)$，定义

$$
\langle P,Q\rangle=P(D)Q(0).
$$

证明这在 $\operatorname{Pol}(n,d)$ 上定义了一个对称非退化标量积。如果 $k$ 不是实域，可能有 $P\ne0$ 而 $\langle P,P\rangle=0$。然而，如果底域是实域，则 $P\ne0$ 时有 $\langle P,P\rangle>0$。还要证明 $d$ 次单项式构成一组正交基。$\langle M_{(\nu)},M_{(\nu)}\rangle$ 是什么？

(c) 映射 $P\mapsto P(D)$ 是从 $\operatorname{Pol}(n,d)$ 到它的对偶的一个同构。

<span class="original-page-anchor" id="pdf-page-560" aria-hidden="true"></span>

(d) 令 $\Delta=D_1^2+\cdots+D_n^2$。注意 $\Delta:\operatorname{Pol}(n,d)\to\operatorname{Pol}(n,d-2)$ 是一个线性映射。证明 $\Delta$ 是满射。

(e) 定义 $\operatorname{Har}(n,d)=\operatorname{Ker}\Delta=$ $d$ 次**调和齐次多项式**组成的向量空间。证明

$$
\dim\operatorname{Har}(n,d)=\frac{(n+d-3)!(n+2d-2)}{(n-2)!d!}.
$$

特别地，若 $n=3$，则 $\dim\operatorname{Har}(3,d)=2d+1$。

(f) 令 $r^2=X_1^2+\cdots+X_n^2$。设 $S$ 表示乘以 $r^2$ 的运算。证明

$$
\langle\Delta P,Q\rangle=\langle P,SQ\rangle\quad\text{对于 }P\in\operatorname{Pol}(n,d)\text{ 和 }Q\in\operatorname{Pol}(n,d-2),
$$

因而 ${}^t\Delta=S$。更一般地，对于 $R\in\operatorname{Pol}(n,m)$ 和 $Q\in\operatorname{Pol}(n,d-m)$，有

$$
\langle R(D)P,Q\rangle=\langle P,RQ\rangle.
$$

(g) 证明在 $\operatorname{Pol}(n,d)$ 上有 $[\Delta,S]=4d+2n$。这里 $[\Delta,S]=\Delta\circ S-S\circ\Delta$。实际上，$[\Delta,S]=4E+2n$，其中 $E$ 是 Euler 算子 $E=\sum X_iD_i$；它在齐次多项式上就是次数算子。

(h) 证明 $\operatorname{Pol}(n,d)=\operatorname{Har}(n,d)\oplus r^2\operatorname{Pol}(n,d-2)$，且两个直和分量互相正交。这是用于 Laplace 算子理论的一个经典定理。

(i) 取 $(c_1,\ldots,c_n)\in k^n$，满足 $\sum c_i^2=0$。令

$$
H_c^d(X)=(c_1X_1+\cdots+c_nX_n)^d.
$$

证明 $H_c^d$ 是调和的，即属于 $\operatorname{Har}(n,d)$。

(j) 对任意 $Q\in\operatorname{Pol}(n,d)$ 和正整数 $m$，证明

$$
Q(D)H_c^m(X)=m(m-1)\cdots(m-d+1)Q(c)H_c^{m-d}(X).
$$

> **译校注：** 原书只要求 $m$ 为正整数。若 $m<d$，左边的 $d$ 阶微分为零，但右边出现本题尚未定义的负次数符号 $H_c^{m-d}$。该式在 $m\geq d$ 时直接有意义；对于 $m<d$ 需另约定右边为零。这里保留原式并说明这个未写明的范围约定。

**34.**（续习题 33。）证明：

**定理。** *设 $k$ 是特征为 $0$ 的代数闭域，$n\geq3$。那么作为 $k$ 上的向量空间，$\operatorname{Har}(n,d)$ 由满足 $\sum c_i^2=0$ 的 $(c)\in k^n$ 所对应的所有多项式 $H_c^d$ 生成。*

［*提示：* 设 $Q\in\operatorname{Har}(n,d)$ 与所有 $(c)\in k^n$ 对应的多项式 $H_c^d$ 正交。由习题 33(h)，只需证明 $r^2\mid Q$。但是若 $\sum c_i^2=0$，则由习题 33(j) 得出 $Q(c)=0$。由 Hilbert 零点定理，存在一个多项式 $F(X)$，使得

$$
Q(X)^s=r^2(X)F(X)\quad\text{（其中某个正整数 }s\text{）}.
$$

但 $n\geq3$ 蕴含 $r^2(X)$ 不可约，因此 $r^2(X)$ 整除 $Q(X)$。］

**35.**（续习题 34。）证明 $O(n)=U_n(\mathbf{R})$ 在 $\operatorname{Har}(n,d)$ 上的表示不可约。

读者可以在以下著作中找到证明：

S. HELGASON，《Topics in Harmonic Analysis on Homogeneous Spaces》，Birkhäuser，1981（特别参见 §3，定理 3.1(ii)）

N. VILENKIN，《Special Functions and the Theory of Group Representations》，AMS Translations of mathematical monographs，第 22 卷，1968（俄文原版，1965），第九章 §2。

<span class="original-page-anchor" id="pdf-page-561" aria-hidden="true"></span>

R. HOWE 与 E. C. TAN，《Non-Abelian Harmonic Analysis》，Universitext，Springer Verlag，New York，1992。

Howe-Tan 的证明如下。现在使用 Hermite 内积

$$
\langle P,Q\rangle=\int_{S^{n-1}}P(x)\overline{Q(x)}\,d\sigma(x),
$$

其中 $\sigma$ 是 $(n-1)$ 维球面 $S^{n-1}$ 上的旋转不变测度。设 $e_1,\ldots,e_n$ 是 $\mathbf{R}^n$ 的单位向量。可以把 $O(n-1)$ 视为 $O(n)$ 中固定 $e_n$ 的子群。注意 $O(n)$ 作用于 $\operatorname{Har}(n,d)$，例如通过复合从右边作用：$P\mapsto P\circ A$，$A\in O(n)$；这个作用与 $\Delta$ 可交换。令

$$
\lambda:\operatorname{Har}(n,d)\longrightarrow\mathbf{C}
$$

为满足 $\lambda(P)=P(e_n)$ 的泛函。那么 $\lambda$ 是 $O(n-1)$ 不变的；由于 Hermite 内积非退化，存在一个调和多项式 $Q_n$，使得

$$
\lambda(P)=\langle P,Q_n\rangle\quad\text{对所有 }P\in\operatorname{Har}(n,d).
$$

设 $M\subset\operatorname{Har}(n,d)$ 是一个 $O(n)$ 子模。那么 $\lambda$ 在 $M$ 上的限制 $\lambda_M$ 非平凡，因为 $O(n)$ 在 $S^{n-1}$ 上传递作用。

> **译校注：** 这一步应在 $M\ne0$ 的前提下理解；若 $M=0$，则限制泛函当然为零。证明不可约性时只需讨论非零子模。

设 $Q_n^M$ 为 $Q_n$ 到 $M$ 的正交投影。那么 $Q_n^M$ 是 $O(n-1)$ 不变的，因而是一个线性组合

$$
Q_n^M(x)=\sum_{j+2k=d}c_jx_n^jr_{n-1}^{2k}.
$$

此外，$Q_n^M$ 是调和的。由此，可以通过证明系数 $c_j$ 之间存在递推关系，说明 $Q_n^M$ 被唯一确定。因此子模 $M$ 被唯一确定，并且必定是整个 $\operatorname{Har}(n,d)$。

> **译校注：** 原书这一段两次印作 $Q_n^H$，但前文定义的是投影 $Q_n^M$，并未定义 $Q_n^H$。中文依照相邻定义统一为 $Q_n^M$，英文保留印式。

### $\mathfrak{sl}_n(F)$ 的不可约性

**36.** 设 $F$ 是特征为 $0$ 的域，$\mathfrak{g}=\mathfrak{sl}_n(F)$ 是迹为 $0$ 的矩阵组成的向量空间，具有 Lie 代数结构 $[X,Y]=XY-YX$。设 $E_{ij}$ 是第 $(i,j)$ 个分量为 $1$、其他分量均为 $0$ 的矩阵。令 $G=SL_n(F)$，设 $A$ 是 $F$ 上对角矩阵的乘法群。

(a) 令 $H_i=E_{ii}-E_{i+1,i+1}$（$i=1,\ldots,n-1$）。证明元素 $E_{ij}$（$i\ne j$）、$H_1,\ldots,H_{n-1}$ 构成 $\mathfrak{g}$ 在 $F$ 上的一组基。

(b) 对 $g\in G$，设 $c(g)$ 为在 $\mathfrak{g}$ 上的共轭作用，即 $c(g)X=gXg^{-1}$。证明：把这个作用限制到群 $A$ 时，每个 $E_{ij}$ 都是特征向量。

(c) 证明 $G$ 在 $\mathfrak{g}$ 上的共轭表示不可约，即若 $V\ne0$ 是 $\mathfrak{g}$ 的一个在 $c(G)$ 下稳定的子空间，则 $V=\mathfrak{g}$。*提示：* 查阅 [JoL 01] 第七章定理 1.5 的证明梗概，并补上所有细节。注意，当 $i\ne j$ 时，矩阵 $E_{ij}$ 幂零，因此对于变量 $t$，指数级数 $\exp(tE_{ij})$ 实际上是一个多项式。关于 $t$ 的导数可以在形式幂级数 $F[[t]]$ 中进行，不使用极限。若 $X$ 是一个矩阵，$x(t)=\exp(tX)$，证明

$$
\left.\frac{d}{dt}x(t)Yx(t)^{-1}\right|_{t=0}=XY-YX=[X,Y].
$$
