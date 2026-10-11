---
title: "第十二章 绝对值"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第十一章 实域","link":"/library/volume-86/chapter-011"}
next: {"text":"第三部分导言：线性代数与表示","link":"/library/volume-86/part-03"}
---

# 第十二章 绝对值

<span class="original-page-anchor" id="pdf-page-476" aria-hidden="true"></span>

## §1. 定义、相关与独立

设 $K$ 为一个域。$K$ 上的**绝对值** $v$ 是定义在 $K$ 上的实值函数 $x\mapsto|x|_v$，满足以下三个性质：

**AV 1。** 对所有 $x\in K$，有 $|x|_v\ge0$，而且 $|x|_v=0$ 当且仅当 $x=0$。

**AV 2。** 对所有 $x,y\in K$，有 $|xy|_v=|x|_v|y|_v$。

**AV 3。** 对所有 $x,y\in K$，有 $|x+y|_v\le|x|_v+|y|_v$。

若绝对值满足以下更强的条件来代替 **AV 3**：

**AV 4。** $|x+y|_v\le\max(|x|_v,|y|_v)$，

则称其为一个**赋值**，或称其为**非阿基米德的**。

对所有 $x\ne0$ 都满足 $|x|_v=1$ 的绝对值，称为**平凡的**绝对值。

如果只讨论一个固定的绝对值，则用 $|x|$ 代替 $|x|_v$。我们也用 $v$ 来指这个绝对值。

$K$ 上的一个绝对值定义了一个度量。在这个度量中，$K$ 的两个元素 $x,y$ 之间的距离为 $|x-y|$。因此，一个绝对值定义了 $K$ 上的一个拓扑。若两个绝对值定义相同的拓扑，则称它们**相关**；否则，称它们独立。

注意到 $|1|=|1^2|=|(-1)^2|=|1|^2$，因此

$$
|1|=|-1|=1.
$$

此外，对所有 $x\in K$，有 $|-x|=|x|$；对 $x\ne0$，有 $|x^{-1}|=|x|^{-1}$。

<span class="original-page-anchor" id="pdf-page-477" aria-hidden="true"></span>

**命题 1.1。** *设 $|\ |_1$ 与 $|\ |_2$ 为域 $K$ 上的非平凡绝对值。它们相关，当且仅当关系*

$$
|x|_1<1
$$

*蕴含 $|x|_2<1$。若它们相关，则存在数 $\lambda>0$，使对所有 $x\in K$，都有 $|x|_1=|x|_2^\lambda$。*

*证明。* 若两个绝对值相关，则所述条件成立，因为满足 $|x|_1<1$ 的元素 $x\in K$ 构成的集合，恰好就是满足 $n\to\infty$ 时 $\lim x^n=0$ 的元素构成的集合。反过来，假设条件成立。那么 $|x|_1>1$ 蕴含 $|x|_2>1$，因为 $|x^{-1}|_1<1$。根据假设，存在元素 $x_0\in K$，使 $|x_0|_1>1$。令 $a=|x_0|_1$，$b=|x_0|_2$，并令

$$
\lambda=\frac{\log b}{\log a}.
$$

设 $x\in K$，$x\ne0$。那么对某个数 $\alpha$，有 $|x|_1=|x_0|_1^\alpha$。若 $m,n$ 为满足 $m/n>\alpha$ 且 $n>0$ 的整数，则有

$$
|x|_1<|x_0|_1^{m/n}.
$$

**译校注：** 原书在此印作 $|x|_1>|x_0|_1^{m/n}$。由于 $|x_0|_1>1$ 且 $m/n>\alpha$，正确方向为 $<$；这也正是下一步所得商的绝对值小于 $1$ 所要求的方向。

所以

$$
|x^n/x_0^m|_1<1,
$$

因此

$$
|x^n/x_0^m|_2<1.
$$

这蕴含 $|x|_2<|x_0|_2^{m/n}$。于是

$$
|x|_2\le|x_0|_2^\alpha.
$$

类似地可以证明反向不等式，因此对所有 $x\in K$、$x\ne0$，得到

$$
|x|_2=|x_0|_2^\alpha.
$$

命题的结论现在显然成立，即 $|x|_2=|x|_1^\lambda$。

**译校注：** 证明中定义的 $\lambda=\log b/\log a$ 给出的是 $|x|_2=|x|_1^\lambda$，而命题陈述写作 $|x|_1=|x|_2^\lambda$。要与命题的写法一致，应取证明中这个正数的倒数；正参数的存在性不受影响。

下面给出绝对值的一些例子。

先考虑有理数。它们有通常的绝对值，对每个正整数 $m$，满足 $|m|=m$。

对于每个素数 $p$，都有 $p$ 进绝对值 $v_p$，定义公式为

$$
|p^rm/n|_p=1/p^r,
$$

<span class="original-page-anchor" id="pdf-page-478" aria-hidden="true"></span>

其中 $r$ 为一个整数，$m,n$ 为不被 $p$ 整除的非零整数。立即可以看出，$p$ 进绝对值是非阿基米德的。

对于任何作为主理想整环的分式域的域 $K$，都可以类似地定义赋值。例如，设 $K=k(t)$，其中 $k$ 为一个域，$t$ 为 $k$ 上的一个变量。对于 $k[t]$ 中的每个不可约多项式 $p(t)$，都有一个赋值 $v_p$，定义方式与有理数的情形相同；不过，没有一种自然的方式来将它规范化。因此，选取一个满足 $0<c<1$ 的数 $c$，并对任何有理函数 $p^rf/g$（其中 $f,g$ 为不被 $p$ 整除的多项式），定义

$$
|p^rf/g|_p=c^r.
$$

常数 $c$ 的各种选择给出相关的赋值。

复数（或实数）的任意子域都有一个绝对值，由复数上通常的绝对值诱导。后面我们将看到，如何把某些域嵌入已经带有自然绝对值的其他域，从而得到这些域上的绝对值。

*假设一个域上的绝对值在素子环上有界（即特征为 $0$ 时的整数环 $\mathbf Z$，或特征为 $p$ 时的模 $p$ 整数环）。那么这个绝对值必然是非阿基米德的。*

*证明。* 对任意元素 $x,y$ 和任意正整数 $n$，有

$$
|(x+y)^n|\le\sum\left|\binom n\nu x^\nu y^{n-\nu}\right|\le(n+1)C\max(|x|,|y|)^n.
$$

**译校注：** 原书最后一个上界印作 $nC\max(|x|,|y|)^n$，没有单独定义常数 $C$。若 $C$ 直接表示素子环上绝对值的统一上界，二项式展开中 $\nu=0,\ldots,n$ 共 $n+1$ 项，逐项估计得到 $(n+1)C$。原文的 $nC$ 也可通过事先把常数加倍来成立，因为 $n+1\le2n$；译文采用直接的项数估计，两种写法都不改变取 $n$ 次方根并令 $n\to\infty$ 的论证。

取 $n$ 次方根并令 $n$ 趋于无穷，就证明了所需结论。注意，在特征 $>0$ 时总是如此，因为素子环是有限的！

若绝对值为阿基米德的，我们请读者参阅其他讨论绝对值的书，以了解它与通常绝对值相关这一事实的证明。这个事实基本上没有用途（下文也从不使用它），因为我们始终从所研究的域上一组具体给定的绝对值出发。

在命题 1.1 中，我们导出了相关绝对值的一个强条件。现在将导出独立绝对值的一个条件。

**定理 1.2（逼近定理）。**（Artin–Whaples）*设 $K$ 为一个域，$|\ |_1,\ldots,|\ |_s$ 为 $K$ 上两两独立的非平凡绝对值。设 $x_1,\ldots,x_s$ 为 $K$ 的元素，$\epsilon>0$。那么存在 $x\in K$，使对所有 $i$，都有*

$$
|x-x_i|_i<\epsilon.
$$

<span class="original-page-anchor" id="pdf-page-479" aria-hidden="true"></span>

*证明。* 先考虑其中的两个绝对值，设为 $v_1$ 与 $v_s$。根据假设，可以找到 $\alpha\in K$，使 $|\alpha|_1<1$ 且 $|\alpha|_s\ge1$。类似地，可以找到 $\beta\in K$，使 $|\beta|_1\ge1$ 且 $|\beta|_s<1$。令 $y=\beta/\alpha$。那么 $|y|_1>1$ 且 $|y|_s<1$。

**译校注：** 原文首句印作“$v_1$ and $v_2$”，但本段所有第二个绝对值的下标都为 $s$，后面的归纳步骤也使用这个针对 $v_1,v_s$ 构造的 $y$；故这里应为 $v_1$ 与 $v_s$。当 $s=2$ 时两种写法一致。

现在证明，存在 $z\in K$，使 $|z|_1>1$，且对 $j=2,\ldots,s$，都有 $|z|_j<1$。用归纳法证明，$s=2$ 的情形刚刚已经证明。假设已经找到 $z\in K$，满足

$$
|z|_1>1\quad\text{且}\quad|z|_j<1\quad\text{对 }j=2,\ldots,s-1.
$$

若 $|z|_s\le1$，则当 $n$ 足够大时，元素 $z^ny$ 满足我们的要求。

若 $|z|_s>1$，则序列

$$
t_n=\frac{z^n}{1+z^n}
$$

在 $v_1$ 与 $v_s$ 下趋于 $1$，在 $v_j$（$j=2,\ldots,s-1$）下趋于 $0$。于是，当 $n$ 足够大时，显然 $t_ny$ 满足我们的要求。

使用刚才构造的元素 $z$，可知序列 $z^n/(1+z^n)$ 在 $v_1$ 下趋于 $1$，并在 $v_j$（$j=2,\ldots,s$）下趋于 $0$。因此，对每个 $i=1,\ldots,s$，都可以构造一个元素 $z_i$，它在 $v_i$ 下十分接近 $1$，而在 $v_j$（$j\ne i$）下十分接近 $0$。于是元素

$$
x=z_1x_1+\cdots+z_sx_s
$$

满足定理的要求。

## §2. 完备化

设 $K$ 为一个具有非平凡绝对值 $v$ 的域，本节始终固定这个绝对值。然后可以按通常的方式定义柯西序列的概念：它是 $K$ 中元素的序列 $\{x_n\}$，满足给定 $\epsilon>0$ 时，存在整数 $N$，使对所有 $n,m>N$，都有

$$
|x_n-x_m|<\epsilon.
$$

若每个柯西序列都收敛，则称 $K$ 为**完备的**。

**命题 2.1。** *存在一对 $(K_v,i)$，由一个在某个绝对值下完备的域 $K_v$ 与一个嵌入 $i:K\to K_v$ 组成，使得 $K$ 上的绝对值由 $K_v$ 上的绝对值诱导（即对 $x\in K$，有 $|x|_v=|ix|$），而且 $iK$ 在 $K_v$ 中稠密。若 $(K'_v,i')$ 是另一对满足这些条件的对象，则存在唯一的* <span class="original-page-anchor" id="pdf-page-480" aria-hidden="true"></span>*同构 $\varphi:K_v\to K'_v$，它保持绝对值，并使下图交换：*

$$
\begin{array}{ccc}
K_v&\xrightarrow{\varphi}&K'_v\\
{}_{i}\nwarrow&&\nearrow_{i'}\\
&K&
\end{array}
$$

*证明。* 唯一性是显然的。存在性可以用众所周知的方法证明；现在简略回顾，细节留给读者。

柯西序列构成一个环，其中加法与乘法逐分量进行。

若序列 $\{x_n\}$ 满足 $\lim_{n\to\infty}x_n=0$，则称它为零序列。零序列在柯西序列环中构成一个理想，而且事实上是一个极大理想。（若一个柯西序列不是零序列，则当 $n$ 足够大时，它始终与 $0$ 保持一定距离，因此可以对几乎所有项取逆。忽略有限项后，所得仍是一个柯西序列。）

柯西序列模零序列所得的剩余类域，就是域 $K_v$。我们把 $K$ “沿对角线”嵌入 $K_v$，即将 $x\in K$ 映为序列 $(x,x,x,\ldots)$。

通过连续性，将 $K$ 的绝对值扩张到 $K_v$。若 $\{x_n\}$ 为一个柯西序列，代表 $K_v$ 中的元素 $\xi$，则定义 $|\xi|=\lim|x_n|$。容易证明，这给出一个绝对值（与代表 $\xi$ 的序列 $\{x_n\}$ 的选取无关），而且这个绝对值在 $K$ 上诱导出原先给定的绝对值。

最后证明 $K_v$ 完备。设 $\{\xi_n\}$ 为 $K_v$ 中的一个柯西序列。对每个 $n$，可以找到元素 $x_n\in K$，使 $|\xi_n-x_n|<1/n$。立即可以验证，$\{x_n\}$ 是 $K$ 中的一个柯西序列。设 $\xi$ 为它在 $K_v$ 中的极限。利用三-$\epsilon$ 论证，可知 $\{\xi_n\}$ 收敛于 $\xi$，从而证明了完备性。

命题 2.1 中的一对 $(K_v,i)$ 可以称为 $K$ 的一个**完备化**。由上述构造得到的标准的一对对象，可以称为 $K$ 的**完备化**。

设 $K$ 具有一个非平凡的阿基米德绝对值 $v$。若已知 $v$ 在有理数上的限制与通常绝对值相关，则完备化 $K_v$ 是一个完备域，包含 $\mathbf Q$ 的完备化作为闭子域，即包含实数域 $\mathbf R$ 作为闭子域。值得陈述 Gelfand–Mazur 关于这种域的结构的定理。首先定义赋范向量空间的概念。

设 $K$ 为一个具有非平凡绝对值的域，$E$ 为一个 $K$ 上的向量空间。$E$ 上的一个**范数**（与 $K$ 的绝对值相容），是指一个由 $E$ 到实数的函数 $\xi\mapsto|\xi|$，满足：

**NO 1。** 对所有 $\xi\in E$，有 $|\xi|\ge0$，而且等于 $0$ 当且仅当 $\xi=0$。

<span class="original-page-anchor" id="pdf-page-481" aria-hidden="true"></span>

**NO 2。** 对所有 $x\in K$ 和 $\xi\in E$，有 $|x\xi|=|x||\xi|$。

**NO 3。** 若 $\xi,\xi'\in E$，则 $|\xi+\xi'|\le|\xi|+|\xi'|$。

若存在数 $C_1,C_2>0$，使对所有 $\xi\in E$，都有

$$
C_1|\xi|_1\le|\xi|_2\le C_2|\xi|_1,
$$

则称两个范数 $|\ |_1$ 与 $|\ |_2$ **等价**。

假设 $E$ 有限维，并设 $\omega_1,\ldots,\omega_n$ 为 $E$ 的一组 $K$-基。若一个元素用此基写成

$$
\xi=x_1\omega_1+\cdots+x_n\omega_n,
$$

其中 $x_i\in K$，则可以定义范数

$$
|\xi|=\max_i|x_i|.
$$

定义范数的三个性质显然都满足。

**命题 2.2。** *设 $K$ 为一个在非平凡绝对值下完备的域，$E$ 为一个有限维 $K$-空间。那么 $E$ 上任意两个范数（与 $K$ 上给定的绝对值相容）都等价。*

*证明。* 首先证明，$E$ 上的拓扑是积空间的拓扑，即若 $\omega_1,\ldots,\omega_n$ 为 $E$ 的一组 $K$-基，则序列

$$
\xi^{(\nu)}=x_1^{(\nu)}\omega_1+\cdots+x_n^{(\nu)}\omega_n,\qquad x_i^{(\nu)}\in K,
$$

在 $E$ 中为柯西序列，只有当这 $n$ 个序列 $x_i^{(\nu)}$ 中每一个都在 $K$ 中为柯西序列。对 $n$ 使用归纳法。$n=1$ 时显然成立。假设 $n\ge2$。考虑如上的一个序列；不失一般性，可以假设它收敛于 $0$。（必要时，可以考虑 $\nu,\mu\to\infty$ 时的 $\xi^{(\nu)}-\xi^{(\mu)}$。）于是必须证明，系数序列也都收敛于 $0$。若非如此，则存在数 $a>0$，使对某个 $j$，不妨设 $j=1$，有

$$
|x_1^{(\nu)}|>a
$$

对于任意大的 $\nu$ 成立。因此，对 $(\nu)$ 的一个子序列，$\xi^{(\nu)}/x_1^{(\nu)}$ 收敛于 $0$，并且可以写成

$$
\frac{\xi^{(\nu)}}{x_1^{(\nu)}}-\omega_1=\frac{x_2^{(\nu)}}{x_1^{(\nu)}}\omega_2+\cdots+\frac{x_n^{(\nu)}}{x_1^{(\nu)}}\omega_n.
$$

令 $\eta^{(\nu)}$ 为这个等式的右端。那么子序列 $\eta^{(\nu)}$ 收敛（由等式左端可知）。根据归纳假设，我们<span class="original-page-anchor" id="pdf-page-482" aria-hidden="true"></span>可知它关于 $\omega_2,\ldots,\omega_n$ 的系数也在 $K$ 中收敛，设极限为 $y_2,\ldots,y_n$。取极限，得到

$$
-\omega_1=y_2\omega_2+\cdots+y_n\omega_n,
$$

这与 $\omega_i$ 的线性无关性矛盾。

**译校注：** 原文左端印作 $\omega_1$。前页等式左端为 $\xi^{(\nu)}/x_1^{(\nu)}-\omega_1$，其极限为 $-\omega_1$；故这里漏印负号。两种写法都产生线性相关的矛盾，译文按实际极限更正。

最后，还必须说明，诱导相同拓扑的两个范数是等价的。设 $|\ |_1$ 与 $|\ |_2$ 为这两个范数。存在数 $C>0$，使对任意 $\xi\in E$，有

$$
|\xi|_1\le C\quad\text{蕴含}\quad|\xi|_2\le1.
$$

取 $a\in K$，使 $0<|a|<1$。对每个非零的 $\xi\in E$，都存在唯一的整数 $s$，使得

$$
C|a|<|a^s\xi|_1\le C.
$$

**译校注：** 原文说“for every $\xi\in E$”。当 $\xi=0$ 时，此处严格下界不可能成立；应在选择 $s$ 时限定 $\xi\ne0$。最后所需的范数不等式对零元素当然成立。

因此 $|a^s\xi|_2\le1$，立即得到

$$
|\xi|_2\le C^{-1}|a|^{-1}|\xi|_1.
$$

另一个不等式由对称性得出，常数也类似。

**定理 2.3。**（Gelfand–Mazur）*设 $A$ 为实数上的一个交换代数，并假设 $A$ 包含一个满足 $j^2=-1$ 的元素 $j$。令 $\mathbf C=\mathbf R+\mathbf Rj$。假设 $A$ 是赋范的（作为 $\mathbf R$ 上的向量空间），而且对所有 $x,y\in A$，有 $|xy|\le|x||y|$。给定 $x_0\in A$、$x_0\ne0$，则存在元素 $c\in\mathbf C$，使 $x_0-c$ 在 $A$ 中不可逆。*

*证明。*（Tornheim）假设对所有 $z\in\mathbf C$，$x_0-z$ 都可逆。考虑由下式定义的映射 $f:\mathbf C\to A$：

$$
f(z)=(x_0-z)^{-1}.
$$

容易按通常方法验证，取逆是一个连续运算。因此 $f$ 连续，且对 $z\ne0$，有

$$
f(z)=z^{-1}(x_0z^{-1}-1)^{-1}=\frac1z\left(\frac1{\dfrac{x_0}{z}-1}\right).
$$

由此可知，当 $z$ 在 $\mathbf C$ 中趋于无穷时，$f(z)$ 趋于 $0$。因此映射 $z\mapsto|f(z)|$ 是从 $\mathbf C$ 到非负实数的连续映射，它有界，而且在某个大圆之外很小。所以它有一个最大值，设为 $M$。令 $D$<span class="original-page-anchor" id="pdf-page-483" aria-hidden="true"></span>为满足 $|f(z)|=M$ 的元素 $z\in\mathbf C$ 所构成的集合。那么 $D$ 非空、有界且闭。我们将证明 $D$ 是开的，从而得到矛盾。

取 $D$ 的一点 $c_0$；平移后，可以假设它是原点。我们将看到，若实数 $r>0$ 足够小，则半径为 $r$ 的圆上的所有点都属于 $D$。事实上，考虑和

$$
S(n)=\frac1n\sum_{k=1}^n\frac1{x_0-\omega^kr},
$$

其中 $\omega$ 为一个本原 $n$ 次单位根。形式地对 $X^n-r^n=\prod_{k=1}^n(X-\omega^kr)$ 取对数导数，可知

$$
\frac{nX^{n-1}}{X^n-r^n}=\sum_{k=1}^n\frac1{X-\omega^kr}.
$$

因此，除以 $n$ 及 $X^{n-1}$，再用 $x_0$ 代入 $X$，得到

$$
S(n)=\frac1{x_0-r(r/x_0)^{n-1}}.
$$

若 $r$ 足够小（例如 $|r/x_0|<1$），则可知

$$
\lim_{n\to\infty}|S(n)|=\left|\frac1{x_0}\right|=M.
$$

假设存在一个绝对值为 $1$ 的复数 $\lambda$，使得

$$
\left|\frac1{x_0-\lambda r}\right|<M.
$$

那么在单位圆上靠近 $\lambda$ 的地方存在一个区间，并且存在 $\epsilon>0$，使对位于这个区间内的所有单位根 $\zeta$，都有

$$
\left|\frac1{x_0-\zeta r}\right|<M-\epsilon.
$$

（这由连续性成立。）取 $n$ 足够大。设 $b_n$ 为位于这个区间内的 $n$ 次单位根的数目。那么 $b_n/n$ 近似等于这个区间的弧长除以 $2\pi$。

**译校注：** 原文印作“length of the interval (times $2\pi$)”。在半径为 $1$ 的圆上，$n$ 次单位根等角距分布，所占比例应为弧长除以圆周长 $2\pi$；所需结论是这个比例趋于一个正数。

可以将 $S(n)$ 表示为和

$$
S(n)=\frac1n\left[\sum_{\mathrm I}\frac1{x_0-\omega^kr}+\sum_{\mathrm{II}}\frac1{x_0-\omega^kr}\right],
$$

<span class="original-page-anchor" id="pdf-page-484" aria-hidden="true"></span>

其中第一个和 $\sum_{\mathrm I}$ 遍历位于该区间内的单位根 $\omega^k$，第二个和遍历其余单位根。由于 $M$ 是最大值，第二个和中的每一项范数都 $\le M$。因此得到估计

$$
\begin{aligned}
|S(n)|&\le\frac1n\left[\left|\sum_{\mathrm I}\right|+\left|\sum_{\mathrm{II}}\right|\right]\\
&\le\frac1n\bigl(b_n(M-\epsilon)+(n-b_n)M\bigr)\\
&\le M-\frac{b_n}{n}\epsilon.
\end{aligned}
$$

这与 $|S(n)|$ 的极限为 $M$ 矛盾。

**推论 2.4。** *设 $K$ 为实数域 $\mathbf R$ 的一个扩域，并具有一个扩张 $\mathbf R$ 上通常绝对值的绝对值。那么 $K=\mathbf R$ 或 $K=\mathbf C$。*

*证明。* 先假设 $K$ 包含 $\mathbf C$。那么 $K$ 为域这一假设和定理 2.3 蕴含 $K=\mathbf C$。

若 $K$ 不包含 $\mathbf C$，即不包含 $-1$ 的平方根，则令 $L=K(j)$，其中 $j^2=-1$。在 $L$ 上（作为 $\mathbf R$-空间）定义范数

$$
|x+yj|=|x|+|y|,
$$

其中 $x,y\in K$。这显然使 $L$ 成为一个赋范 $\mathbf R$-空间。此外，若 $z=x+yj$ 与 $z'=x'+y'j$ 属于 $L$，则

$$
\begin{aligned}
|zz'|&=|xx'-yy'|+|xy'+x'y|\\
&\le|xx'|+|yy'|+|xy'|+|x'y|\\
&\le|x||x'|+|y||y'|+|x||y'|+|x'||y|\\
&\le(|x|+|y|)(|x'|+|y'|)\\
&\le|z||z'|,
\end{aligned}
$$

因此再次应用定理 2.3，即可完成证明。

作为命题 2.2 的一个重要应用，有：

**命题 2.5。** *设 $K$ 关于非平凡绝对值 $v$ 完备。若 $E$ 为 $K$ 的任意代数扩张，则 $v$ 可以唯一地扩张到 $E$。若 $E$ 在 $K$ 上有限，则 $E$ 完备。*

*证明。* 在阿基米德情形，存在性是显然的，因为处理的是实数与复数。在非阿基米德情形，我们将<span class="original-page-anchor" id="pdf-page-485" aria-hidden="true"></span>存在性的证明推迟到后面一节。它使用与当前完全不同的思想。对于唯一性，可以假设 $E$ 在 $K$ 上有限。由命题 2.2，$v$ 到 $E$ 的一个扩张所定义的拓扑，与以上用一组基得到的最大值范数所定义的拓扑相同。给定 $E$ 中的一个柯西序列 $\xi^{(\nu)}$，

$$
\xi^{(\nu)}=x_{\nu1}\omega_1+\cdots+x_{\nu n}\omega_n,
$$

根据最大值范数的定义，$n$ 个序列 $\{x_{\nu i}\}$（$i=1,\ldots,n$）都必须是 $K$ 中的柯西序列。若 $\{x_{\nu i}\}$ 收敛于 $K$ 的元素 $z_i$，则显然序列 $\xi^{(\nu)}$ 收敛于 $z_1\omega_1+\cdots+z_n\omega_n$。因此 $E$ 完备。此外，由于 $v$ 到 $E$ 的任意两个扩张都等价，可以应用命题 1.1，得到必须有 $\lambda=1$，因为这两个扩张在 $K$ 上诱导同一个绝对值 $v$。这就证明了所需结论。

由唯一性，可以明确确定 $K$ 的代数扩张上的绝对值。首先注意，若 $E$ 为 $K$ 的正规扩张，$\sigma$ 为 $E$ 的一个 $K$-自同构，则函数

$$
x\mapsto|\sigma x|
$$

是 $E$ 上扩张 $K$ 的绝对值的一个绝对值。因此，对所有 $x\in E$，都必须有

$$
|\sigma x|=|x|.
$$

若 $E$ 在 $K$ 上代数，$\sigma$ 为 $E$ 到 $K^a$ 的一个 $K$-嵌入，则同一结论仍成立；把 $E$ 嵌入 $K$ 的一个正规扩张就可立即看出这一点。特别地，若 $\alpha$ 在 $K$ 上代数，次数为 $n$，而 $\alpha_1,\ldots,\alpha_n$ 为它的共轭元（计入重数，重数等于不可分次数），则所有绝对值 $|\alpha_i|$ 都相等。用 $N$ 表示从 $K(\alpha)$ 到 $K$ 的范数，则有

$$
|N(\alpha)|=|\alpha|^n.
$$

取 $n$ 次方根，得到：

**命题 2.6。** *设 $K$ 关于一个非平凡绝对值完备。设 $\alpha$ 在 $K$ 上代数，$N$ 为从 $K(\alpha)$ 到 $K$ 的范数。令 $n=[K(\alpha):K]$。那么*

$$
|\alpha|=|N(\alpha)|^{1/n}.
$$

在复数域作为实数域扩张这一特殊情形，可以写成 $\alpha=a+bi$，其中 $a,b\in\mathbf R$。由此可见，命题 2.6 的公式推广了复数绝对值的公式

$$
|\alpha|=(a^2+b^2)^{1/2},
$$

因为 $a^2+b^2$ 正是 $\alpha$ 从 $\mathbf C$ 到 $\mathbf R$ 的范数。

**译校注：** 原书此式左端印作 $\alpha$，漏了绝对值符号；一般的复数 $a+bi$ 不等于非负实数 $(a^2+b^2)^{1/2}$，正确公式如译文所示。

<span class="original-page-anchor" id="pdf-page-486" aria-hidden="true"></span>

**说明与例子。** 完备化过程在数学中广泛出现。第一个例子是从有理数得到实数，并且加上定序的性质。我在 [La 90a] 第 IX 章 §3 中完整地进行了这一过程。在我所知的所有其他例子中，定序性质都不起作用。本章已经见到了域的完备化的例子，特别是 $p$ 进绝对值的情形，它们与给域定序相去甚远。不过，实数仍然是绝对值或更一般的范数的值域。

在分析中，人们以各种范数将各种空间完备化。例如，设 $V$ 为一个复向量空间。在许多应用中，还必须处理半范数，它满足相同的条件，只是在 **NO 1** 中仅要求 $\|\xi\|\ge0$。即使 $\xi\ne0$，也允许 $\|\xi\|=0$。

于是可以构造柯西序列空间、零序列子空间及商空间 $\bar V$。通过连续性，半范数可以扩张为 $\bar V$ 上的半范数，而这个扩张实际上是一个范数。一般而言，$\bar V$ 在此扩张下是完备的。**巴拿赫空间**是一个完备赋范向量空间。

**例。** 设 $V$ 为 $\mathbf R$ 上阶梯函数的向量空间；这里阶梯函数是由有限个区间的示性函数相加得到的复值函数，区间可以是闭的、开的或半闭的，即可以包含或不包含端点。对 $f\in V$，定义 **$L^1$-半范数**

$$
\|f\|_1=\int_{\mathbf R}|f(x)|\,dx.
$$

**译校注：** 原文没有限制这些区间有界或函数可积。若允许无界区间，例如 $(0,\infty)$ 的示性函数，则上式积分为无穷，不能作为实值半范数。此处需使用可积阶梯函数（例如有限个有界区间的示性函数的线性组合）；原文定义保留，并明确指出这一遗漏。

$V$ 关于这个半范数的完备化定义为 $L^1(\mathbf R)$。然后，希望更好地了解 $L^1(\mathbf R)$ 的元素是什么样的。一个简单引理说明：给定 $V$ 中的一个 $L^1$-柯西序列，并给定 $\epsilon>0$，存在一个子序列，在除去一个测度小于 $\epsilon$ 的集合之后一致收敛。因此，$L^1(\mathbf R)$ 的元素可以与 $V$ 中 $L^1$-柯西序列的逐点极限相认同。详细论述见 [La 85]。

当然，分析学家还使用其他范数或半范数以及其他空间，例如 $\mathbf R$ 上具有紧支集的 $C^\infty$ 函数空间，以及可能控制导数的范数。可能的变化无穷无尽。

定理 2.3 与推论 2.4 也用于巴拿赫代数理论，通过 Gelfand–Mazur 和 Gelfand–Naimark 定理，将某种巴拿赫代数表示为紧空间上的连续函数代数。参见 [Ri 60] 与 [Ru 73]。

**算术例子。** 关于与 Dwork 的数论工作相关的 $p$ 进巴拿赫空间，例如参见 Serre [Se 62]，或 [La 90b] 第 15 章。

本书仅讨论完备域及其有限扩张。

<span class="original-page-anchor" id="pdf-page-487" aria-hidden="true"></span>

### 参考文献

[La 85] S. LANG，*Real and Functional Analysis*，Springer Verlag，1993

[La 90a] S. LANG，*Undergraduate Algebra*，第二版，Springer Verlag，1990

[La 90b] S. LANG，*Cyclotomic Fields I and II*，Springer Verlag，1990（由 1978 年与 1980 年的初版合并而成）

[Ri 60] C. RICKART，*Banach Algebras*，Van Nostrand（1960），定理 1.7.1 与 4.2.2。

[Ru 73] W. RUDIN，*Functional Analysis*，McGraw Hill（1973），定理 10.14 与 11.18。

[Se 62] J. P. SERRE，Endomorphismes complètement continus des espaces de Banach $p$-adiques，*Pub. Math. IHES* **12**（1962），第 69–85 页

## §3. 有限扩张

本节始终讨论一个具有非平凡绝对值 $v$ 的域 $K$。

希望描述这个绝对值如何扩张到 $K$ 的有限扩张。若 $E$ 为 $K$ 的一个扩张，$w$ 为 $E$ 上扩张 $v$ 的一个绝对值，则记作 $w\mid v$。

设 $K_v$ 为完备化。我们知道 $v$ 可以扩张到 $K_v$，随后唯一地扩张到其代数闭包 $K_v^a$。若 $E$ 为 $K$ 的有限扩张，甚至任意代数扩张，则可以借助一个 $K$-同构把 $E$ 嵌入 $K_v^a$，并取 $E$ 上诱导出的绝对值，从而将 $v$ 扩张到 $E$。现在将证明，$v$ 的每一个扩张都可以这样得到。

**命题 3.1。** *设 $E$ 为 $K$ 的一个有限扩张，$w$ 为 $E$ 上扩张 $v$ 的一个绝对值，并设 $E_w$ 为完备化。设 $K_w$ 为 $K$ 在 $E_w$ 中的闭包，并把 $E$ 等同于它在 $E_w$ 中的像。那么 $E_w=EK_w$（合成域）。*

*证明。* 注意，$K_w$ 是 $K$ 的一个完备化，而合成域 $EK_w$ 在 $K_w$ 上代数，因此由命题 2.5 可知它完备。由于它包含 $E$，所以 $E$ 在其中稠密，因而 $E_w=EK_w$。

若从一个嵌入 $\sigma:E\to K_v^a$ 出发（始终假设为 $K$-嵌入），则由命题 2.5 同样可知，$\sigma E\cdot K_v$ 是完备的。因此，此构造与命题中的构造在同构意义下本质相同。今后我们采用嵌入的观点。现在必须确定，何时两个嵌入在 $E$ 上给出相同的绝对值。

给定两个嵌入 $\sigma,\tau:E\to K_v^a$，若存在 $K_v^a$ 的一个 $K_v$-自同构 $\lambda$，使 $\sigma=\lambda\tau$，则称它们**在 $K_v$ 上共轭**。可以看出，实际上 $\lambda$ 由它在 $\tau E$ 或 $\tau E\cdot K_v$ 上的作用决定。

<span class="original-page-anchor" id="pdf-page-488" aria-hidden="true"></span>

**命题 3.2。** *设 $E$ 为 $K$ 的一个代数扩张。两个嵌入 $\sigma,\tau:E\to K_v^a$ 在 $E$ 上给出相同的绝对值，当且仅当它们在 $K_v$ 上共轭。*

*证明。* 假设它们在 $K_v$ 上共轭。那么绝对值从 $K_v$ 到 $K_v^a$ 的扩张的唯一性，保证 $E$ 上诱导出的绝对值相等。反过来，假设如此。设 $\lambda:\tau E\to\sigma E$ 为一个 $K$-同构。我们将证明，$\lambda$ 可以扩张为从 $\tau E\cdot K_v$ 到 $\sigma E\cdot K_v$ 的一个 $K_v$-同构。由于 $\tau E$ 在 $\tau E\cdot K_v$ 中稠密，元素 $x\in\tau E\cdot K_v$ 可以写成

$$
x=\lim\tau x_n,
$$

其中 $x_n\in E$。由于 $\sigma$ 与 $\tau$ 在 $E$ 上诱导的绝对值相同，序列 $\lambda\tau x_n=\sigma x_n$ 收敛于 $\sigma E\cdot K_v$ 的一个元素，记为 $\lambda x$。立即可以验证，$\lambda x$ 与所使用的具体序列 $\tau x_n$ 无关，而且映射 $\lambda:\tau E\cdot K_v\to\sigma E\cdot K_v$ 是一个同构，显然逐点固定 $K_v$。这就证明了命题。

由前两个命题，若 $w$ 为 $v$ 到 $K$ 的有限扩张 $E$ 的一个扩张，则可以把 $E_w$ 与 $E$ 及 $K_v$ 的合成扩张 $EK_v$ 等同起来。若 $N=[E:K]$ 有限，则把

$$
N_w=[E_w:K_v]
$$

称为**局部次数**。

**命题 3.3。** *设 $E$ 为 $K$ 的一个有限可分扩张，次数为 $N$。那么*

$$
N=\sum_{w\mid v}N_w.
$$

*证明。* 可以对一个元素 $\alpha$ 写成 $E=K(\alpha)$。设 $f(X)$ 为它在 $K$ 上的不可约多项式。那么在 $K_v$ 上，有分解

$$
f(X)=f_1(X)\cdots f_r(X),
$$

其中 $f_i(X)$ 为不可约因子。根据可分性假设，每个因子都以重数 $1$ 出现。$E$ 到 $K_v^a$ 的嵌入，对应于把 $\alpha$ 映到各个 $f_i$ 的根的映射。两个嵌入共轭，当且仅当它们把 $\alpha$ 映为同一个多项式 $f_i$ 的根。另一方面，显然每种情形的局部次数恰好等于 $f_i$ 的次数。这就证明了命题。

**命题 3.4。** *设 $E$ 为 $K$ 的一个有限扩张。那么*

$$
\sum_{w\mid v}[E_w:K_v]\le[E:K].
$$

<span class="original-page-anchor" id="pdf-page-489" aria-hidden="true"></span>

*若 $E$ 在 $K$ 上纯不可分，则 $E$ 上扩张 $v$ 的绝对值 $w$ 只有一个。*

*证明。* 先证明第二个断言。若 $E$ 在 $K$ 上纯不可分，且 $p^r$ 为其不可分次数，则对 $E$ 中的每个 $\alpha$，都有 $\alpha^{p^r}\in K$。因此 $v$ 可以唯一地扩张到 $E$。现在考虑有限扩张的一般情形，并令 $F=E^{p^r}K$。那么 $F$ 在 $K$ 上可分，而 $E$ 在 $F$ 上纯不可分。由前一命题，

$$
\sum_{w\mid v}[F_w:K_v]=[F:K].
$$

而对每个 $w$，有 $[E_w:F_w]\le[E:F]$。由此，命题陈述中的不等式是显然的。

若 $K$ 上的绝对值 $v$ 对于 $K$ 的任意有限扩张 $E$ 都满足 $[E:K]=\sum_{w\mid v}[E_w:K_v]$，则称 $v$ **性态良好**。假设有一个有限扩张塔 $L\supset E\supset K$。令 $w$ 遍历 $E$ 上扩张 $v$ 的绝对值，$u$ 遍历 $L$ 上扩张 $v$ 的绝对值。若 $u\mid w$，则 $L_u$ 包含 $E_w$。因此有：

$$
\begin{aligned}
\sum_{u\mid v}[L_u:K_v]&=\sum_{w\mid v}\sum_{u\mid w}[L_u:E_w][E_w:K_v]\\
&=\sum_{w\mid v}[E_w:K_v]\sum_{u\mid w}[L_u:E_w]\\
&\le\sum_{w\mid v}[E_w:K_v][L:E]\\
&\le[E:K][L:E].
\end{aligned}
$$

由此立即可见，若 $v$ 性态良好，$E$ 在 $K$ 上有限，且 $w$ 为 $v$ 在 $E$ 上的扩张，则 $w$ 性态良好（各处都必须取等号）。

设 $E$ 为 $K$ 的一个有限扩张，$p^r$ 为其不可分次数。回顾一下，元素 $\alpha\in K$ 的范数由公式

$$
N_K^E(\alpha)=\prod_\sigma\sigma\alpha^{p^r}
$$

给出，其中 $\sigma$ 遍历 $E$ 的所有不同的 $K$-同构（到一个给定的代数闭包中）。

若 $w$ 为 $E$ 上扩张 $v$ 的一个绝对值，则从 $E_w$ 到 $K_v$ 的范数称为**局部范数**。

把上述乘积替换为和，就得到迹与局部迹。我们把迹简记为 $\operatorname{Tr}$。

> **译校注（重数说明）：** 原书的“把上述乘积替换为和”应理解为对全部共轭按重数求和。若 $\sigma$ 遍历不同的 $K$-嵌入，不可分次数为 $p^r$，则正确公式为 $\operatorname{Tr}_K^E(\alpha)=p^r\sum_\sigma\sigma\alpha$，而不是把显示的范数因子直接相加为 $\sum_\sigma(\sigma\alpha)^{p^r}$；局部迹同理。例如特征 $2$ 时，取 $K=\mathbf F_2(s^2)$、$E=\mathbf F_2(s)$，这是次数 $2$ 的纯不可分扩张。元素 $1\in K$ 的乘法线性变换是二维恒等变换，故迹为 $2=0$，但直接把唯一的范数因子 $1^2$ 相加会得到 $1$。

**命题 3.8。** *设 $E$ 为 $K$ 的一个有限扩张，并假设 $v$ 性态* <span class="original-page-anchor" id="pdf-page-490" aria-hidden="true"></span>*良好。设 $\alpha\in E$。那么：*

$$
N_K^E(\alpha)=\prod_{w\mid v}N_{K_v}^{E_w}(\alpha)
$$

$$
\operatorname{Tr}_K^E(\alpha)=\sum_{w\mid v}\operatorname{Tr}_{K_v}^{E_w}(\alpha)
$$

*证明。* 先假设 $E=K(\alpha)$，设 $f(X)$ 为 $\alpha$ 在 $K$ 上的不可约多项式。若在 $K_v$ 上把 $f(X)$ 分解为不可约因子，则

$$
f(X)=f_1(X)\cdots f_r(X),
$$

其中每个 $f_i(X)$ 都不可约，而且根据 $v$ 性态良好的假设，这些 $f_i$ 互不相同。范数 $N_K^E(\alpha)$ 等于 $(-1)^{\deg f}$ 乘以 $f$ 的常数项，对每个 $f_i$ 也同样如此。由于 $f$ 的常数项等于各个 $f_i$ 的常数项的乘积，就得到命题的第一部分。迹的结论，则由考察 $f$ 与各个 $f_i$ 的次高项系数得出。

若 $E$ 不等于 $K(\alpha)$，只需使用范数与迹的传递性。细节留给读者。

也可以直接用嵌入来论证。设 $\sigma_1,\ldots,\sigma_m$ 为 $E$ 到 $K_v^a$ 的各个不同的 $K$-嵌入，并设 $p^r$ 为 $E$ 在 $K$ 上的不可分次数。对于任意 $\sigma$，$\sigma E\cdot K_v$ 在 $K_v$ 上的不可分次数至多为 $p^r$。若将 $\sigma_1,\ldots,\sigma_m$ 分成 $K_v$ 上的不同共轭类，则根据 $v$ 性态良好的假设，立即可知：对每个 $i$，$\sigma_iE\cdot K_v$ 在 $K_v$ 上的不可分次数也必须等于 $p^r$。因此，把范数表示为带有重数 $p^r$ 的共轭元乘积的公式，可以分成对应于 $K_v$ 上各个共轭类的因子的乘积。

结合命题 2.6，有：

**命题 3.6。** *设 $K$ 具有一个性态良好的绝对值 $v$。设 $E$ 为 $K$ 的一个有限扩张，$\alpha\in E$。对 $E$ 上每个扩张 $v$ 的绝对值 $w$，令*

$$
N_w=[E_w:K_v].
$$

*那么*

$$
\prod_{w\mid v}|\alpha|_w^{N_w}=|N_K^E(\alpha)|_v.
$$

<span class="original-page-anchor" id="pdf-page-491" aria-hidden="true"></span>

## §4. 赋值

本节将得到若干结果，其中包括非阿基米德绝对值可以扩张到代数扩张上的存在性定理。首先推广非阿基米德绝对值的概念。

设 $\Gamma$ 为一个乘法交换群。若给定 $\Gamma$ 的一个在乘法下封闭的子集 $S$，使 $\Gamma$ 为 $S$、单位元 $1$ 以及由 $S$ 中所有元素的逆构成的集合 $S^{-1}$ 的不交并，则称在 $\Gamma$ 上定义了一个**定序**。

若 $\alpha,\beta\in\Gamma$，定义 $\alpha<\beta$ 表示 $\alpha\beta^{-1}\in S$。有 $\alpha<1$ 当且仅当 $\alpha\in S$。容易验证关系 $<$ 的以下性质：

**1。** 对 $\alpha,\beta\in\Gamma$，有 $\alpha<\beta$、$\alpha=\beta$ 或 $\beta<\alpha$，而且这些可能性互不相容。

**2。** $\alpha<\beta$ 蕴含对任意 $\gamma\in\Gamma$，有 $\alpha\gamma<\beta\gamma$。

**3。** $\alpha<\beta$ 与 $\beta<\gamma$ 蕴含 $\alpha<\gamma$。

（反过来，满足这三个性质的关系给出一个由所有 $<1$ 的元素构成的子集 $S$。不过，下文不需要这个事实。）

形式地给一个有序群添加额外元素 $0$ 很方便，使 $0\alpha=0$，且对所有 $\alpha\in\Gamma$，有 $0<\alpha$。这个有序群就类似于正实数乘法群，但其定序可能是非阿基米德的。

若 $\alpha\in\Gamma$，$n$ 为一个非零整数，且 $\alpha^n=1$，则 $\alpha=1$。这直接来自 $S$ 在乘法下封闭且不包含 $1$ 的假设。特别地，映射 $\alpha\mapsto\alpha^n$ 为单射。

设 $K$ 为一个域。$K$ 的一个**赋值**是指由 $K$ 到一个有序群 $\Gamma$ 连同额外元素 $0$ 的映射 $x\mapsto|x|$，满足：

**VAL 1。** $|x|=0$ 当且仅当 $x=0$。

**VAL 2。** 对所有 $x,y\in K$，有 $|xy|=|x||y|$。

**VAL 3。** $|x+y|\le\max(|x|,|y|)$。

可以看出，一个赋值给出从乘法群 $K^*$ 到 $\Gamma$ 的一个同态。若它把 $K^*$ 映为 $1$，则称赋值为**平凡的**。若给出赋值的映射不是满射，则其像为 $\Gamma$ 的一个有序子群；把值域限制为这个像，就得到到一个有序群的满赋值，该有序群称为**值群**。

赋值也记作 $v$。若 $v_1,v_2$ 为 $K$ 的两个赋值，而且存在一个从 $v_1$ 的像到 $v_2$ 的像的保序同构 $\lambda$，使得

$$
|x|_2=\lambda|x|_1,
$$

则称它们**等价**；

<span class="original-page-anchor" id="pdf-page-492" aria-hidden="true"></span>

此式对所有 $x\in K$ 成立。（约定 $\lambda(0)=0$。）

赋值与绝对值一样，还有其他性质。例如，$|1|=1$，因为 $|1|=|1|^2$。此外，对所有 $x\in K$，有

$$
|\pm x|=|x|.
$$

证明是显然的。又若 $|x|<|y|$，则

$$
|x+y|=|y|.
$$

要看出这一点，注意在假设下有

$$
|y|=|y+x-x|\le\max(|y+x|,|x|)=|x+y|\le\max(|x|,|y|)=|y|.
$$

最后，在和

$$
x_1+\cdots+x_n=0
$$

中，至少有两个元素具有相同的值。这是前面说明的一个直接推论。

设 $K$ 为一个域。若 $K$ 的子环 $\mathfrak o$ 满足：对任意 $x\in K$，有 $x\in\mathfrak o$ 或 $x^{-1}\in\mathfrak o$，则称 $\mathfrak o$ 为一个**赋值环**。

现在说明赋值环给出赋值。设 $\mathfrak o$ 为 $K$ 的一个赋值环，$U$ 为 $\mathfrak o$ 的可逆元群。我们断言 $\mathfrak o$ 为一个局部环。事实上，假设 $x,y\in\mathfrak o$ 不是可逆元。不妨设 $x/y\in\mathfrak o$。那么

$$
1+x/y=(x+y)/y\in\mathfrak o.
$$

若 $x+y$ 为可逆元，则 $1/y\in\mathfrak o$，这与 $y$ 不可逆的假设矛盾。因此 $x+y$ 不是可逆元。显然，对于 $z\in\mathfrak o$，$zx$ 也不是可逆元。所以所有不可逆元构成一个理想，它必定是 $\mathfrak o$ 的唯一极大理想。

设 $\mathfrak m$ 为 $\mathfrak o$ 的极大理想，$\mathfrak m^*$ 为 $\mathfrak m$ 中非零元素的乘法系。那么

$$
K^*=\mathfrak m^*\cup U\cup\mathfrak m^{*-1}
$$

为 $\mathfrak m^*$、$U$ 和 $\mathfrak m^{*-1}$ 的不交并。现在可以给商群 $K^*/U$ 定序。若 $x\in K^*$，用 $|x|$ 表示陪集 $xU$，并令 $|0|=0$。定义 $|x|<1$（即 $|x|\in S$）当且仅当 $x\in\mathfrak m^*$。集合 $S$ 显然在乘法下封闭；令 $\Gamma=K^*/U$，则 $\Gamma$ 是 $S,1,S^{-1}$ 的不交并。这样就得到 $K$ 的一个赋值。

注意，若 $x,y\in K$ 且 $x,y\ne0$，则

$$
|x|<|y|\Leftrightarrow|x/y|<1\Leftrightarrow x/y\in\mathfrak m^*.
$$

反过来，给定 $K$ 到一个有序群的赋值，令 $\mathfrak o$ 为 $K$ 中满足 $|x|\le1$ 的所有元素 $x$ 构成的子集。

**译校注：** 原文在此印作 $|x|<1$。这样得到的是赋值环的极大理想，并不包含 $1$；要得到下页所述、可逆元满足 $|x|=1$ 的赋值环，必须采用 $|x|\le1$。

由<span class="original-page-anchor" id="pdf-page-493" aria-hidden="true"></span>赋值的公理立即可知，$\mathfrak o$ 为一个环。若 $|x|<1$，则 $|x^{-1}|>1$，所以 $x^{-1}$ 不在 $\mathfrak o$ 中。若 $|x|=1$，则 $|x^{-1}|=1$。可见 $\mathfrak o$ 为一个赋值环，其极大理想由满足 $|x|<1$ 的元素 $x$ 构成，而其可逆元由满足 $|x|=1$ 的元素 $x$ 构成。读者立即可以验证，$K$ 的赋值环与赋值的等价类之间存在一个双射。

第 VII 章关于位与赋值环的扩张定理，现在立即给出赋值的扩张定理。

**定理 4.1。** *设 $K$ 为域 $L$ 的一个子域。那么 $K$ 上的一个赋值可以扩张为 $L$ 上的一个赋值。*

*证明。* 设 $\mathfrak o$ 为 $K$ 中对应于给定赋值的赋值环。设 $\varphi:\mathfrak o\to\mathfrak o/\mathfrak m$ 为到剩余类域的典范同态，并按第 VII 章 §3 将 $\varphi$ 扩张为 $L$ 的一个赋值环 $\mathfrak O$ 上的同态。设 $\mathfrak M$ 为 $\mathfrak O$ 的极大理想。由于 $\mathfrak M\cap\mathfrak o$ 包含 $\mathfrak m$，但不包含 $1$，所以 $\mathfrak M\cap\mathfrak o=\mathfrak m$。设 $U'$ 为 $\mathfrak O$ 的可逆元群。那么 $U'\cap K=U$ 是 $\mathfrak o$ 的可逆元群。因此有一个典范单射

$$
K^*/U\to L^*/U',
$$

立即可以验证它是保序的。把 $K^*/U$ 等同于 $L^*/U'$ 中的像，就把 $K$ 的赋值扩张为 $L$ 的赋值。

当然，在处理绝对值时，要求值群为实数乘法群的一个子群。因此，当 $L$ 在 $K$ 上代数时，还必须对值群 $L^*/U'$ 的性质作进一步证明。

**命题 4.2。** *设 $L$ 为 $K$ 的一个有限扩张，次数为 $n$。设 $w$ 为 $L$ 的一个赋值，值群为 $\Gamma'$。设 $\Gamma$ 为 $K$ 的值群。那么 $(\Gamma':\Gamma)\le n$。*

*证明。* 设 $y_1,\ldots,y_r$ 为 $L$ 的元素，其值代表 $\Gamma'$ 中 $\Gamma$ 的不同陪集。我们将证明这些 $y_j$ 在 $K$ 上线性无关。在关系 $a_1y_1+\cdots+a_ry_r=0$（其中 $a_i\in K$、$a_i\ne0$）中，两个项必须具有相同的值，设为 $|a_iy_i|=|a_jy_j|$，其中 $i\ne j$。于是

$$
|y_i|=|a_i^{-1}a_j||y_j|.
$$

这与 $y_i,y_j$（$i\ne j$）的值代表 $\Gamma'$ 中 $\Gamma$ 的不同陪集这一假设矛盾，从而证明了命题。

**推论 4.3。** *存在整数 $e\ge1$，使映射 $\gamma\mapsto\gamma^e$ 诱导出从 $\Gamma'$ 到 $\Gamma$ 的一个单同态。*

*证明。* 取 $e$ 为指数 $(\Gamma':\Gamma)$。

<span class="original-page-anchor" id="pdf-page-494" aria-hidden="true"></span>

**推论 4.4。** *设 $K$ 是带有赋值 $v$ 的域，其值群是正实数有序群的一个有序子群；若 $L$ 是 $K$ 的代数扩张，则存在 $v$ 到 $L$ 的一个延拓，其值群也是正实数群的一个有序子群。*

*证明。* 我们知道，可以把 $v$ 延拓为 $L$ 上的一个赋值 $w$，其值群为某个 $\Gamma'$，而 $v$ 的值群 $\Gamma$ 可以与 $\mathbf R^+$ 的一个子群认同。由推论 4.3，$\Gamma'$ 的每个元素模 $\Gamma$ 都有有限阶。因为对于每个整数 $e\geq1$，$\mathbf R^+$ 的每个元素都有唯一的 $e$ 次方根，所以显然可以找到 $\Gamma'$ 到 $\mathbf R^+$ 的一个保序嵌入，它在 $\Gamma$ 上诱导恒等映射。这样就得到了把 $v$ 延拓为 $L$ 上的绝对值。

**推论 4.5。** *若 $L$ 在 $K$ 上有限，且 $\Gamma$ 是无限循环群，则 $\Gamma'$ 也是无限循环群。*

*证明。* 利用推论 4.3，以及循环群的子群仍是循环群这一事实。

现在我们把前面的命题稍加加强。我们把 $(\Gamma':\Gamma)$ 称为**分歧指数**。

**命题 4.6。** *设 $L$ 是域 $K$ 的一个次数为 $n$ 的有限扩张，$\mathfrak O$ 是 $L$ 的一个赋值环。设 $\mathfrak M$ 是其极大理想，令 $\mathfrak o=\mathfrak O\cap K$，并设 $\mathfrak m$ 是 $\mathfrak o$ 的极大理想，即 $\mathfrak m=\mathfrak M\cap\mathfrak o$。那么剩余域次数 $[\mathfrak O/\mathfrak M:\mathfrak o/\mathfrak m]$ 有限。若将它记为 $f$，并设 $e$ 为分歧指数，则 $ef\leq n$。*

*证明。* 取 $L^*$ 中的元素 $y_1,\ldots,y_e$，作为 $\Gamma'/\Gamma$ 中不同陪集的代表，并取 $\mathfrak O$ 的元素 $z_1,\ldots,z_s$，使它们模 $\mathfrak M$ 的剩余类在 $\mathfrak o/\mathfrak m$ 上线性无关。考虑一个关系

$$
\sum_{i,j}a_{ij}z_jy_i=0,
$$

其中 $a_{ij}\in K$，且 $a_{ij}$ 不全为 $0$。对于一个内层和

$$
\sum_{j=1}^s a_{ij}z_j,
$$

将它除以具有最大赋值的系数 $a_{i\nu}$。我们得到 $z_1,\ldots,z_s$ 的一个线性组合，其系数属于 $\mathfrak o$，且至少有一个系数是可逆元。由于 $z_1,\ldots,z_s$ 模 $\mathfrak M$ 在 $\mathfrak o/\mathfrak m$ 上线性无关，所得线性组合是可逆元。因此

$$
\left|\sum_{j=1}^s a_{ij}z_j\right|=|a_{i\nu}|
$$

<span class="original-page-anchor" id="pdf-page-495" aria-hidden="true"></span>

其中 $\nu$ 是某个指标。在和式

$$
\sum_{i=1}^e\left(\sum_{j=1}^s a_{ij}z_j\right)y_i=0
$$

中，将其看成关于 $i$ 的求和，则至少有两项具有相同的值。如同命题 4.2 的证明，这与 $|y_1|,\ldots,|y_e|$ 模 $\Gamma$ 的独立性矛盾。

**注。** 我们的证明还表明，元素 $\{z_jy_i\}$ 在 $K$ 上线性无关。稍后还会用到这一点。

若 $w$ 是赋值 $v$ 的一个延拓，则分歧指数记为 $e(w|v)$，剩余域次数记为 $f(w|v)$。

**命题 4.7。** *设 $K$ 是带有赋值 $v$ 的域，并设 $K\subset E\subset L$ 是 $K$ 的有限扩张。设 $w$ 是 $v$ 到 $E$ 的一个延拓，$u$ 是 $w$ 到 $L$ 的一个延拓。那么*

$$
e(u|w)e(w|v)=e(u|v),
$$

$$
f(u|w)f(w|v)=f(u|v).
$$

*证明。* 显然。

上述命题也可以表述为：分歧指数与剩余域次数在扩张塔中具有乘法性。

最后，我们通过说明有限扩张中的赋值环与整闭包之间的关系来结束本节。

**命题 4.8。** *设 $\mathfrak o$ 是域 $K$ 中的一个赋值环，$L$ 是 $K$ 的一个有限扩张。设 $\mathfrak O$ 是 $L$ 的一个位于 $\mathfrak o$ 之上的赋值环，$\mathfrak M$ 是其极大理想。设 $B$ 是 $\mathfrak o$ 在 $L$ 中的整闭包，且令 $\mathfrak P=\mathfrak M\cap B$。则 $\mathfrak O$ 等于局部环 $B_{\mathfrak P}$。*

*证明。* 显然 $B_{\mathfrak P}$ 包含在 $\mathfrak O$ 中。反过来，设 $x$ 是 $\mathfrak O$ 的一个元素。则 $x$ 满足一个系数属于 $K$ 且不全为 $0$ 的方程，例如

$$
a_nx^n+\cdots+a_0=0,\qquad a_i\in K.
$$

设在与赋值环 $\mathfrak o$ 对应的赋值下，$a_s$ 是诸 $a_i$ 中具有最大值的系数，并且是具有此值的系数中最靠左的一个。令 $b_i=a_i/a_s$。则所有 $b_i\in\mathfrak o$，且

$$
b_n,\ldots,b_{s+1}\in\mathfrak M.
$$

<span class="original-page-anchor" id="pdf-page-496" aria-hidden="true"></span>

把方程除以 $x^s$，得到

$$
\left(b_nx^{n-s}+\cdots+b_{s+1}x+1\right)+\frac1x\left(b_{s-1}+\cdots+b_0\frac1{x^{s-1}}\right)=0.
$$

设 $y$ 和 $z$ 分别为上式两个括号内的量，于是可以写成

$$
-y=z/x\quad\text{以及}\quad-xy=z.
$$

为了证明命题，只需证明 $y$ 和 $z$ 属于 $B$，而 $y$ 不属于 $\mathfrak P$。

我们利用第七章命题 3.5。若 $L$ 的一个位于 $\mathfrak o$ 之上的赋值环含有 $x$，则它含有 $y$，因为 $y$ 是 $x$ 的一个系数属于 $\mathfrak o$ 的多项式。因此这个赋值环也含有 $z=-xy$。另一方面，若 $L$ 的这个位于 $\mathfrak o$ 之上的赋值环含有 $1/x$，则它含有 $z$，因为 $z$ 是 $1/x$ 的一个系数属于 $\mathfrak o$ 的多项式。因此这个赋值环也含有 $y$。由此根据第七章命题 3.5，得到 $y,z$ 属于 $B$。

> **译校注：** 原页此段在两处 “above” 之后及两处 “coefficients in” 之后均留有空白。根据前页 $b_i\in\mathfrak o$ 以及本段所引用的整闭包判别，四处均补为 $\mathfrak o$；英文转录明确标出原页空白。

此外，由于 $x\in\mathfrak O$，并且按构造 $b_n,\ldots,b_{s+1}$ 都属于 $\mathfrak M$，所以 $y$ 不可能属于 $\mathfrak M$，从而也不可能属于 $\mathfrak P$。证明完毕。

**推论 4.9。** *沿用命题中的记号。则 $L$ 的位于 $\mathfrak o$ 之上的赋值环只有有限多个。*

> **译校注：** 原书此处印为 “lying above $\mathfrak P$”。根据命题 4.8 及紧随的证明，这里应为位于 $\mathfrak o$ 之上；$\mathfrak P$ 是整闭包 $B$ 中的极大理想。

*证明。* 这是因为 $B$ 中位于 $\mathfrak o$ 的极大理想之上的极大理想 $\mathfrak P$ 只有有限多个（第七章命题 2.1 的推论）。

**推论 4.10。** *沿用命题中的记号。另外假设 $L$ 在 $K$ 上是伽罗瓦扩张。若 $\mathfrak O$ 和 $\mathfrak O'$ 是 $L$ 的两个位于 $\mathfrak o$ 之上的赋值环，其极大理想分别为 $\mathfrak M,\mathfrak M'$，则存在 $L$ 在 $K$ 上的一个自同构 $\sigma$，使得 $\sigma\mathfrak O=\mathfrak O'$ 且 $\sigma\mathfrak M=\mathfrak M'$。*

*证明。* 令 $\mathfrak P=\mathfrak M\cap B$，$\mathfrak P'=\mathfrak M'\cap B$。由第七章命题 2.1，存在 $L$ 在 $K$ 上的一个自同构 $\sigma$，使得 $\sigma\mathfrak P=\mathfrak P'$。由此结论显然成立。

> **译校注：** 原书印为 $\mathfrak P=\mathfrak O\cap B$ 和 $\mathfrak P'=\mathfrak O'\cap B$。但 $B\subset\mathfrak O,\mathfrak O'$，这些交集等于 $B$；这里所需的是命题 4.8 中的极大理想，故改为 $\mathfrak M\cap B$ 和 $\mathfrak M'\cap B$。

**例。** 设 $k$ 是一个域，$K$ 是一个超越次数为 $1$ 的有限生成扩张。若 $t$ 是 $K$ 在 $k$ 上的一个超越基，则 $K$ 在 $k(t)$ 上是有限代数扩张。设 $\mathfrak O$ 是 $K$ 的一个包含 $k$ 的赋值环，并假设 $\mathfrak O\ne K$。令 $\mathfrak o=\mathfrak O\cap k(t)$。则 $\mathfrak o$ 显然是 $k(t)$ 的一个赋值环（<span class="original-page-anchor" id="pdf-page-497" aria-hidden="true"></span>关于逆元的条件更是自动满足），而 $k(t)$ 的相应赋值不可能是平凡的。$t$ 或 $t^{-1}$ 至少有一个属于 $\mathfrak o$。不妨设 $t\in\mathfrak o$。则 $\mathfrak m\cap k[t]$ 不可能是零理想，否则把 $\mathfrak o$ 模其极大理想的典范同态 $\mathfrak o\longrightarrow\mathfrak o/\mathfrak m$ 将在 $k[t]$ 上诱导一个同构，进而在 $k(t)$ 上诱导一个同构，这与假设矛盾。因此 $\mathfrak m\cap k[t]$ 是一个由不可约多项式 $p(t)$ 生成的素理想 $\mathfrak p$。局部环 $k[t]_{\mathfrak p}$ 显然是一个赋值环，而且它必定等于 $\mathfrak o$，因为 $k(t)$ 的每个元素都具有 $p^ru$ 形式的表达式，其中 $u$ 是 $k[t]_{\mathfrak p}$ 中的可逆元。这样就确定了 $k(t)$ 的所有包含 $k$ 的赋值环，而且可以看到值群是循环群。这种赋值将称为离散赋值，下面会更详细地研究它们。由推论 4.5，$K$ 的赋值环 $\mathfrak O$ 也是离散的。

> **译校注：** 原书第一处印为 “$\mathfrak o\cap k[t]$ cannot be the zero ideal”。由于此时 $k[t]\subset\mathfrak o$，这个交集本就是 $k[t]$；后面的模极大理想论证所需的是 $\mathfrak m\cap k[t]$，故改正第一处符号。

剩余域 $\mathfrak o/\mathfrak m$ 等于 $k[t]/\mathfrak p$，因此是 $k$ 的一个有限扩张。由命题 4.6，$\mathfrak O/\mathfrak M$ 在 $k$ 上有限（这里 $\mathfrak M$ 表示 $\mathfrak O$ 的极大理想）。

最后，我们注意到，$K$ 中包含 $k$ 且使 $t$ 属于其极大理想的赋值环 $\mathfrak O$ 只有有限多个。事实上，这样的赋值环必定位于 $k[t]_{\mathfrak p}$ 之上，其中 $\mathfrak p=(t)$ 是由 $t$ 生成的素理想；于是可以应用推论 4.9。

## §5. 完备化与赋值

本节始终讨论域 $K$ 上的一个非阿基米德绝对值 $v$。这个绝对值也是一个赋值，其值群 $\Gamma_K$ 是正实数群的一个子群。记其赋值环为 $\mathfrak o$，极大理想为 $\mathfrak m$。

以 $\widehat K$ 表示 $K$ 关于 $v$ 的完备化，令 $\widehat{\mathfrak o}$（分别地，$\widehat{\mathfrak m}$）是 $\mathfrak o$（分别地，$\mathfrak m$）在 $\widehat K$ 中的闭包。由连续性，$\widehat{\mathfrak o}$ 的每个元素的值都 $\leq1$，而 $\widehat K$ 中不属于 $\widehat{\mathfrak o}$ 的每个元素的值都 $>1$。若 $x\in\widehat K$，则存在 $y\in K$，使 $|x-y|$ 很小，从而对这样的 $y$ 有 $|x|=|y|$（由非阿基米德性质）。因此 $\widehat{\mathfrak o}$ 是 $\widehat K$ 的一个赋值环，$\widehat{\mathfrak m}$ 是其极大理想。此外，

$$
\widehat{\mathfrak o}\cap K=\mathfrak o\quad\text{且}\quad\widehat{\mathfrak m}\cap K=\mathfrak m,
$$

并且有一个同构

$$
\mathfrak o/\mathfrak m\overset{\approx}{\longrightarrow}\widehat{\mathfrak o}/\widehat{\mathfrak m}.
$$

因此剩余域 $\mathfrak o/\mathfrak m$ 在完备化下不变。

设 $E$ 是 $K$ 的一个扩张，$\mathfrak o_E$ 是 $E$ 的一个位于 $\mathfrak o$ 之上的赋值环。设 $\mathfrak m_E$ 为其极大理想。假设与 $\mathfrak o_E$ 对应的赋值实际上是一个绝对值，从而可以构造完备化 $\widehat E$。于是有<span class="original-page-anchor" id="pdf-page-498" aria-hidden="true"></span>一个交换图：

$$
\begin{array}{ccc}
\mathfrak o_E/\mathfrak m_E&\overset{\approx}{\longrightarrow}&\widehat{\mathfrak o}_E/\widehat{\mathfrak m}_E\\
\uparrow&&\uparrow\\
\mathfrak o/\mathfrak m&\overset{\approx}{\longrightarrow}&\widehat{\mathfrak o}/\widehat{\mathfrak m}
\end{array}
$$

其中竖直箭头是单射，水平箭头是同构。因此，我们所讨论的赋值的剩余域扩张，可以在 $E$ 与 $K$ 的完备化上研究。

> **译校注：** 原书印为 “the completions $\widehat E$ of $K$”。由上面的交换图，所指为 $E$ 与 $K$ 的完备化 $\widehat E$ 与 $\widehat K$，而非把 $\widehat E$ 当作 $K$ 的完备化。

对于分歧指数，也有类似的说明。设 $\Gamma_v(K)$ 与 $\Gamma_v(\widehat K)$ 分别表示 $K$ 与 $\widehat K$ 上赋值的值群（即映射 $x\mapsto|x|$ 分别对 $x\in K^*$ 和 $x\in\widehat K^*$ 所得的像）。上面已经看到 $\Gamma_v(K)=\Gamma_v(\widehat K)$；换言之，由于非阿基米德性质，值群在完备化下保持不变。（在阿基米德情形这当然不成立。）若 $E$ 仍是 $K$ 的一个扩张，而 $w$ 是 $E$ 上延拓 $v$ 的绝对值，则有一个交换图

$$
\begin{array}{ccc}
\Gamma_w(E)&\overset{=}{\longrightarrow}&\Gamma_w(\widehat E)\\
\uparrow&&\uparrow\\
\Gamma_v(K)&\overset{=}{\longrightarrow}&\Gamma_v(\widehat K)
\end{array}
$$

由此可见，分歧指数 $(\Gamma_w(E):\Gamma_v(K))$ 也在完备化下保持不变。

## §6. 离散赋值

若一个赋值的值群是循环群，就称它为**离散的**。在这种情况下，该赋值是一个绝对值（把值群看成正实数群的一个子群）。对于每个素数 $p$，有理数上的 $p$ 进赋值都是离散的。由推论 4.5，离散赋值到一个有限扩张域的延拓也仍是离散的。除了把域嵌入实数或复数而得到的绝对值以外，离散赋值是实际应用中最重要的赋值。下面给出关于它们的一些说明。

设 $v$ 是域 $K$ 上的一个离散赋值，$\mathfrak o$ 是其赋值环，$\mathfrak m$ 是极大理想。存在 $\mathfrak m$ 的一个元素 $\pi$，使其值 $|\pi|$ 生成值群。（值群的另一个生成元是 $|\pi^{-1}|$。）这样的元素 $\pi$ 称为 $v$（或 $\mathfrak m$）的一个**局部参数**。每个<span class="original-page-anchor" id="pdf-page-499" aria-hidden="true"></span>$K$ 的非零元素 $x$ 都可以写成

$$
x=u\pi^r,
$$

其中 $u$ 是 $\mathfrak o$ 的某个可逆元，$r$ 是某个整数。事实上，对某个 $r\in\mathbf Z$ 有 $|x|=|\pi|^r=|\pi^r|$，所以 $x/\pi^r$ 是 $\mathfrak o$ 的可逆元。我们称 $r$ 为 $x$ 在 $v$ 处的**阶**。它显然不依赖于所选参数。我们也说 $x$ 有一个 **$r$ 阶零点**。（若 $r$ 为负，则称 $x$ 有一个 $-r$ 阶**极点**。）

> **译校注：** 原书此处为 “Every element $x$ of $K$”。因为 $u\pi^r\ne0$，这一表达式只适用于非零元素；中文补明这一限制。

特别地，可以看到 $\mathfrak m$ 是由 $\pi$ 生成的主理想。作为练习，留给读者验证：$\mathfrak o$ 的每个非零理想都是主理想，并且是 $\mathfrak m$ 的一个幂。此外，$\mathfrak o$ 是唯一分解整环，且只有一个素元（相差可逆元的视为相同），即 $\pi$。

> **译校注：** 原书印为 “every ideal ... is a power of $\mathfrak m$”。零理想不是 $\mathfrak m$ 的有限非负整数次幂，故幂的断言须限于非零理想；零理想当然仍是主理想。

若 $x,y\in K$ 且 $|x|=|y|$，就记 $x\sim y$。设 $\pi_i$（$i=1,2,\ldots$）是 $\mathfrak o$ 的一个元素序列，满足 $\pi_i\sim\pi^i$。设 $R$ 是 $\mathfrak o/\mathfrak m$ 在 $\mathfrak o$ 中的一组代表。这意味着典范映射 $\mathfrak o\longrightarrow\mathfrak o/\mathfrak m$ 在 $R$ 上诱导到 $\mathfrak o/\mathfrak m$ 的一个双射。

*假设 $K$ 关于所讨论的赋值完备。则 $\mathfrak o$ 的每个元素 $x$ 都可以写成一个收敛级数*

$$
x=a_0+a_1\pi_1+a_2\pi_2+\cdots,
$$

*其中 $a_i\in R$，而且 $a_i$ 由 $x$ 唯一确定。*

这很容易用递归论证证明。假设已经写成

$$
x\equiv a_0+\cdots+a_n\pi_n\pmod{\mathfrak m^{n+1}},
$$

则对于某个 $y\in\mathfrak o$，有 $x-(a_0+\cdots+a_n\pi_n)=\pi_{n+1}y$。由假设，可以写成 $y=a_{n+1}+\pi z$，其中 $a_{n+1}\in R$。于是得到

$$
x\equiv a_0+\cdots+a_{n+1}\pi_{n+1}\pmod{\mathfrak m^{n+2}},
$$

而且显然，这个级数的第 $n$ 项趋于 $0$。因此级数收敛（由非阿基米德性质！）。由于 $R$ 对每个模 $\mathfrak m$ 的剩余类恰含一个代表，$a_i$ 唯一确定。

**例。** 先考虑带有 $p$ 进赋值 $v_p$ 的有理数域。其完备化记为 $\mathbf Q_p$，称为 **$p$ 进数域**。$\mathbf Z$ 在 $\mathbf Q_p$ 中的闭包是 **$p$ 进整数环 $\mathbf Z_p$**。注意，素数 $p$ 在 $\mathbf Z$ 以及它的闭包 $\mathbf Z_p$ 中都是素元。可以选取整数集合 $(0,1,\ldots,p-1)$ 为代表集 $R$。因此每个 $p$ 进整数都可以唯一写成收敛和 $\sum a_ip^i$，其中 $a_i$ 是整数，$0\leq a_i\leq p-1$。这个和称为其 **$p$ 进展开**。这种和按收敛级数的通常方法进行加法和乘法。

<span class="original-page-anchor" id="pdf-page-500" aria-hidden="true"></span>

例如，可以使用等比级数的通常形式；若取 $p=3$，则

$$
-1=\frac2{1-3}=2(1+3+3^2+\cdots).
$$

注意，$(0,1,\ldots,p-1)$ 绝不是唯一可用的代表。事实上，可以证明 $\mathbf Z_p$ 含有 $(p-1)$ 次单位根，而且常常选取这些单位根作为剩余域中非零元素的代表更为方便。

接下来考虑有理函数域 $k(t)$，其中 $k$ 是任意域，$t$ 在 $k$ 上超越。环 $k[t]$ 中的素元 $t$ 确定一个赋值。这个赋值是离散的，而 $k[t]$ 关于这个赋值的完备化是幂级数环 $k[[t]]$。这时，可以取 $k$ 本身的元素作为剩余域的代表，而该剩余域与 $k$ 典范同构。$k[[t]]$ 的极大理想是由 $t$ 生成的理想。

这种情形相当于把复变函数论中的通常情形代数化。例如，设 $z_0$ 是复平面上的一个点，$\mathfrak o$ 是在 $z_0$ 周围某个圆盘中全纯的函数所成的环。那么 $\mathfrak o$ 是一个离散赋值环，其极大理想由在 $z_0$ 处有零点的函数组成。$\mathfrak o$ 的每个元素都有幂级数展开

$$
f(z)=\sum_{\nu=m}^{\infty}a_\nu(z-z_0)^\nu.
$$

可以取复数 $a_\nu$ 为剩余域的代表。若 $a_m\ne0$，则称 $f(z)$ 有一个 $m$ 阶零点。无论把阶看作代数意义下关于离散赋值的阶，还是看作复变函数论意义下的阶，它都是相同的。可以选取一个典范的一致化参数，即 $z-z_0$，并且

$$
f(z)=(z-z_0)^m g(z),
$$

其中 $g(z)$ 是一个以非零常数项开始的幂级数。因此 $g(z)$ 可逆。

再次设 $K$ 关于一个离散赋值完备，$E$ 是 $K$ 的一个有限扩张。设 $\mathfrak o_E,\mathfrak m_E$ 是 $E$ 中位于 $K$ 中的 $\mathfrak o,\mathfrak m$ 之上的赋值环与极大理想。设 $\Pi$ 是 $E$ 中的一个素元。若 $\Gamma_E$ 和 $\Gamma_K$ 分别为 $E$ 和 $K$ 中赋值的值群，并且

$$
e=(\Gamma_E:\Gamma_K)
$$

为分歧指数，则

$$
|\Pi^e|=|\pi|,
$$

<span class="original-page-anchor" id="pdf-page-501" aria-hidden="true"></span>

而元素

$$
\Pi^i\pi^j,\qquad0\leq i\leq e-1,\ j=0,1,2,\ldots
$$

在 $E$ 中的阶为 $je+i$。

设 $\omega_1,\ldots,\omega_f$ 是 $E$ 的元素，其模 $\mathfrak m_E$ 的剩余类构成 $\mathfrak o_E/\mathfrak m_E$ 的一个基。若 $R$ 仍是 $\mathfrak o/\mathfrak m$ 在 $\mathfrak o$ 中的一组代表，则所有形如

$$
a_1\omega_1+\cdots+a_f\omega_f
$$

的元素（$a_j\in R$）组成 $\mathfrak o_E/\mathfrak m_E$ 在 $\mathfrak o_E$ 中的一组代表。由此可见，$\mathfrak o_E$ 的每个元素都有一个收敛展开

$$
\sum_{i=0}^{e-1}\sum_{\nu=1}^f\sum_{j=0}^{\infty}a_{\nu,i,j}\pi^j\omega_\nu\Pi^i.
$$

因此，元素 $\{\omega_\nu\Pi^i\}$ 构成 $\mathfrak o_E$ 作为 $\mathfrak o$ 上的模的一组生成元。另一方面，在命题 4.6 的证明中已经看到，这些元素在 $K$ 上线性无关。于是得到：

**命题 6.1。** *设 $K$ 关于一个离散赋值完备。设 $E$ 是 $K$ 的一个有限扩张，$e,f$ 分别为分歧指数与剩余域次数。那么*

$$
ef=[E:K].
$$

**推论 6.2。** *设 $\alpha\in E$，$\alpha\ne0$。设 $v$ 是 $K$ 上的赋值，$w$ 是它到 $E$ 的延拓。那么*

$$
\operatorname{ord}_v N_K^E(\alpha)=f(w|v)\operatorname{ord}_w\alpha.
$$

*证明。* 由公式

$$
|N_K^E(\alpha)|=|\alpha|^{ef}
$$

及有关定义立即得出。

**推论 6.3。** *设 $K$ 是任意域，$v$ 是 $K$ 上的一个离散赋值，$E$ 是 $K$ 的一个有限扩张。若 $v$ 在 $E$ 中表现良好（例如 $E$ 在 $K$ 上可分），则*

$$
\sum_{w|v}e(w|v)f(w|v)=[E:K].
$$

*若 $E$ 在 $K$ 上是伽罗瓦扩张，则所有 $e_w$ 都等于同一个数 $e$，所有 $f_w$ 都* <span class="original-page-anchor" id="pdf-page-502" aria-hidden="true"></span>*等于同一个数 $f$，所以*

$$
efr=[E:K],
$$

*其中 $r$ 是 $v$ 到 $E$ 的延拓数目。*

*证明。* 第一个断言来自假设和命题 3.3。若 $E$ 在 $K$ 上是伽罗瓦扩张，则由推论 4.10，$E$ 上位于 $v$ 之上的任意两个赋值都共轭。因此所有分歧指数相等，剩余域次数也同样相等。于是关系 $efr=[E:K]$ 显然成立。

## §7. 完备域中多项式的零点

*设 $K$ 关于一个非平凡绝对值完备。*

设

$$
f(X)=\prod(X-\alpha_i)^{r_i}
$$

是 $K[X]$ 中首项系数为 $1$ 的一个多项式，并假设根 $\alpha_i$ 互不相同，其重数为 $r_i$。设 $d$ 是 $f$ 的次数。设 $g$ 是另一个系数属于 $K^a$ 的多项式，并假设 $g$ 的次数也是 $d$，首项系数也为 $1$。用 $|g|$ 表示 $g$ 各系数绝对值的最大值。容易看出，若 $|g|$ 有界，则 $g$ 的各根的绝对值也有界。

假设 $g$ 接近 $f$，意思是 $|f-g|$ 很小。若 $\beta$ 是 $g$ 的任意一个根，则

$$
|f(\beta)-g(\beta)|=|f(\beta)|=\prod|\alpha_i-\beta|^{r_i}
$$

很小，因此 $\beta$ 必定接近 $f$ 的某个根。当 $\beta$ 接近例如 $\alpha=\alpha_1$ 时，它到 $f$ 其余根的距离趋于 $\alpha_1$ 到那些根的距离，因而有正的下界。在这种情况下，称 **$\beta$ 属于 $\alpha$**。

**命题 7.1。** *若 $g$ 充分接近 $f$，且 $\beta_1,\ldots,\beta_s$ 是 $g$ 的属于 $\alpha$ 的根（按重数计数），则 $s=r_1$，即 $\alpha$ 在 $f$ 中的重数。*

*证明。* 反设结论不成立。则可以找到一个趋于 $f$ 的多项式序列 $g_\nu$，其中恰有 $s$ 个根 $\beta_1^{(\nu)},\ldots,\beta_s^{(\nu)}$ 属于 $\alpha$，但是 $s\ne r$。（因为重数的可能选择只有有限多个，所以可以取相同的重数 $s$。）此外，$g$ 的其他根也<span class="original-page-anchor" id="pdf-page-503" aria-hidden="true"></span>属于 $f$ 的某些根；可以假设按照它们所属于的 $f$ 的根，把这些根分组放在一起。由于 $\lim g_\nu=f$，得到 $\alpha$ 在 $f$ 中必有重数 $s$，矛盾。

下面研究一个多项式在完备域中有根的条件。

*假设 $K$ 关于一个离散赋值完备，赋值环为 $\mathfrak o$，极大理想为 $\mathfrak p$。* 固定 $\mathfrak p$ 的一个素元 $\pi$。

我们讨论 $\mathfrak o$ 上的 $n$ 维空间。把各 $a_i\in\mathfrak o$ 的向量 $(a_1,\ldots,a_n)$ 记为 $A$。若 $f(X_1,\ldots,X_n)\in\mathfrak o[X]$ 是一个具有整系数的 $n$ 元多项式，则当 $f(A)=0$ 时，称 $A$ 是 $f$ 的一个**零点**；当 $f(A)\equiv0\pmod{\mathfrak p^m}$ 时，称 $A$ 是 **$f$ 模 $\mathfrak p^m$ 的一个零点**。

设 $C=(c_0,\ldots,c_n)$ 属于 $\mathfrak o^{(n+1)}$，$m$ 是一个 $\geq1$ 的整数。我们考虑形如

$$
\pi^m(c_0+c_1x_1+\cdots+c_nx_n)\equiv0\pmod{\mathfrak p^{m+1}}\tag{*}
$$

的同余式的解的性质。这个同余式等价于线性同余式

$$
c_0+c_1x_1+\cdots+c_nx_n\equiv0\pmod{\mathfrak p}.\tag{**}
$$

若某个系数 $c_i$（$i=1,\ldots,n$）不 $\equiv0\pmod{\mathfrak p}$，则解集非空，并具有域 $\mathfrak o/\mathfrak p$ 上一个非齐次线性方程的解集的通常结构。特别地，其维数为 $n-1$。若 (\*) 或 (\*\*) 中有某个 $c_i\not\equiv0\pmod{\mathfrak p}$，则称它为一个**真同余式**。

在记号上，以 $D_if$ 表示 $f$ 关于 $X_i$ 的形式偏导数，并记

$$
\operatorname{grad}f(X)=(D_1f(X),\ldots,D_nf(X)).
$$

**命题 7.2。** *设 $f(X)\in\mathfrak o[X]$。设 $r$ 是一个 $\geq1$ 的整数，$A\in\mathfrak o^{(n)}$ 满足*

$$
\begin{aligned}
f(A)&\equiv0\pmod{\mathfrak p^{2r-1}},\\
D_if(A)&\equiv0\pmod{\mathfrak p^{r-1}},&&\text{对所有 }i=1,\ldots,n,\\
D_if(A)&\not\equiv0\pmod{\mathfrak p^r},&&\text{对某个 }i=1,\ldots,n.
\end{aligned}
$$

*设 $v$ 是一个 $\geq0$ 的整数，$B\in\mathfrak o^{(n)}$ 满足*

$$
B\equiv A\pmod{\mathfrak p^r}\quad\text{且}\quad f(B)\equiv0\pmod{\mathfrak p^{2r-1+v}}.
$$

*向量 $Y\in\mathfrak o^{(n)}$ 满足*

$$
Y\equiv B\pmod{\mathfrak p^{r+v}}\quad\text{且}\quad f(Y)\equiv0\pmod{\mathfrak p^{2r+v}}
$$

<span class="original-page-anchor" id="pdf-page-504" aria-hidden="true"></span>

*当且仅当 $Y$ 可以写成 $Y=B+\pi^{r+v}C$，其中某个 $C\in\mathfrak o^{(n)}$ 满足真同余式*

$$
f(B)+\pi^{r+v}\operatorname{grad}f(B)\cdot C\equiv0\pmod{\mathfrak p^{2r+v}}.
$$

*证明。* 证明比命题的叙述还短。写 $Y=B+\pi^{r+v}C$。由泰勒展开，

$$
f(B+\pi^{r+v}C)\equiv f(B)+\pi^{r+v}\operatorname{grad}f(B)\cdot C\pmod{\mathfrak p^{2r+2v}}.
$$

要模 $\mathfrak p^{2r+v}$ 解这个同余式，由假设会得到一个真同余式，因为 $\operatorname{grad}f(B)\equiv\operatorname{grad}f(A)\equiv0\pmod{\mathfrak p^{r-1}}$。

**推论 7.3。** *在命题 7.2 的假设下，$f$ 在 $\mathfrak o^{(n)}$ 中有一个零点，它模 $\mathfrak p^r$ 与 $A$ 同余。*

*证明。* 可以把这个零点写成一个收敛和

$$
A+\pi^r C_1+\pi^{r+1}C_2+\cdots,
$$

按命题中的方法归纳求出 $C_1,C_2,\ldots$。

> **译校注：** 原书印为 $A+\pi^{r+1}C_1+\pi^{r+2}C_2+\cdots$。命题中从 $B=A$、$v=0$ 开始的首次修正是 $\pi^rC_1$，故这里各指数应减 $1$。例如 $r=1$、$f(X)=X-\pi$、$A=0$ 满足假设，但根 $\pi$ 不能表示为从 $\pi^2$ 开始的原式。

**推论 7.4。** *设 $f$ 是 $\mathfrak o[X]$ 中的一个一元多项式，$a\in\mathfrak o$ 满足 $f(a)\equiv0\pmod{\mathfrak p}$，但 $f'(a)\not\equiv0\pmod{\mathfrak p}$。则存在 $b\in\mathfrak o$，$b\equiv a\pmod{\mathfrak p}$，使 $f(b)=0$。*

*证明。* 在命题中取 $n=1$、$r=1$，并应用推论 7.3。

**推论 7.5。** *设 $m$ 是一个不被 $K$ 的特征整除的正整数。存在一个整数 $r$，使得对于任意 $a\in\mathfrak o$，只要 $a\equiv1\pmod{\mathfrak p^r}$，方程 $X^m-a=0$ 就在 $K$ 中有根。*

*证明。* 应用该命题。

**例。** 在 $2$ 进数域 $\mathbf Q_2$ 中，$-7$ 有平方根，即 $\sqrt{-7}\in\mathbf Q_2$，因为 $-7=1-8$。

当绝对值并非离散时，仍然可以用**牛顿逼近**给出多项式有零点的判别准则。（参见我的论文 “On quasi-algebraic closure”，*Annals of Math.*（1952），第 373–390 页。

**命题 7.6。** *设 $K$ 关于一个非阿基米德绝对值（非平凡）完备。设 $\mathfrak o$ 是赋值环，$f(X)\in\mathfrak o[X]$ 是一个一元多项式。设 $\alpha_0\in\mathfrak o$ 满足*

$$
|f(\alpha_0)|<|f'(\alpha_0)^2|
$$

*（这里 $f'$ 表示 $f$ 的形式导数）。则序列*

$$
\alpha_{i+1}=\alpha_i-\frac{f(\alpha_i)}{f'(\alpha_i)}
$$

<span class="original-page-anchor" id="pdf-page-505" aria-hidden="true"></span>

*收敛到 $f$ 在 $\mathfrak o$ 中的一个根 $\alpha$，并且有*

$$
|\alpha-\alpha_0|\leq\left|\frac{f(\alpha_0)}{f'(\alpha_0)^2}\right|<1.
$$

*证明。* 令 $c=|f(\alpha_0)/f'(\alpha_0)^2|<1$。我们归纳证明：

**1.** $|\alpha_i|\leq1$，

**2.** $|\alpha_i-\alpha_0|\leq c$，

**3.** $\displaystyle\left|\frac{f(\alpha_i)}{f'(\alpha_i)^2}\right|\leq c^{2^i}$。

这三个条件显然蕴含命题。当 $i=0$ 时，它们就是假设。现归纳假设它们对于 $i$ 成立。于是：

**1.** $|f(\alpha_i)/f'(\alpha_i)^2|\leq c^{2^i}$ 给出 $|\alpha_{i+1}-\alpha_i|\leq c^{2^i}<1$，从而 $|\alpha_{i+1}|\leq1$。

**2.** $|\alpha_{i+1}-\alpha_0|\leq\max\{|\alpha_{i+1}-\alpha_i|,|\alpha_i-\alpha_0|\}\leq c$。

> **译校注：** 原书此行最后印为 $\max\{|\alpha_{i+1}-\alpha_i|,|\alpha_i-\alpha_0|\}=c$。归纳假设只保证这两个量均不超过 $c$，故此处应为 $\leq c$；这已足以完成所需的估计。

**3.** 由泰勒展开，有

$$
f(\alpha_{i+1})=f(\alpha_i)-f'(\alpha_i)\frac{f(\alpha_i)}{f'(\alpha_i)}+\beta\left(\frac{f(\alpha_i)}{f'(\alpha_i)}\right)^2,
$$

其中某个 $\beta\in\mathfrak o$。其绝对值小于或等于

$$
\left|\frac{f(\alpha_i)}{f'(\alpha_i)}\right|^2.
$$

对 $f'(\alpha_{i+1})$ 使用泰勒展开，得到

$$
|f'(\alpha_{i+1})|=|f'(\alpha_i)|.
$$

由此得到

$$
\left|\frac{f(\alpha_{i+1})}{f'(\alpha_{i+1})^2}\right|\leq c^{2^{i+1}},
$$

正如所需。

这个命题的方法在处理环时也很有用，例如一个局部环 $\mathfrak o$，其极大理想 $\mathfrak m$ 满足：对于某个整数 $r>0$ 有 $\mathfrak m^r=0$。若有 $\mathfrak o[X]$ 中的一个多项式 $f$，以及一个近似根 $\alpha_0$，使得

$$
f'(\alpha_0)\not\equiv0\bmod\mathfrak m,
$$

则牛顿逼近序列说明如何把 $\alpha_0$ 改进为 $f$ 的一个根。

**多变量的例子。** *设 $K$ 关于一个非阿基米德绝对值完备。设 $f(X_1,\ldots,X_{n+1})\in K[X]$ 是一个系数属于 $K$ 的多项式。设 $(a_1,\ldots,a_n,b)\in K^{n+1}$，并假设 $f(a,b)=0$。设 $D_{n+1}$ 是* <span class="original-page-anchor" id="pdf-page-506" aria-hidden="true"></span>*关于第 $(n+1)$ 个变量的偏导数，并假设 $D_{n+1}f(a,b)\ne0$。设 $(\bar a)\in K^n$ 充分接近 $(a)$。则存在 $K$ 的一个接近 $b$ 的元素 $\bar b$，使 $f(\bar a,\bar b)=0$。*

这一断言是命题 7.6 的直接推论。把所有 $a_i,b$ 乘以 $K$ 的一个适当非零元素，可以使它们变成 $\mathfrak o$ 的元素。相应地变换变量后，可以不失一般性地假设 $a_i,b\in\mathfrak o$，而偏导数不为零这一条件仍然保持。因此可以应用命题 7.6。把 $(a)$ 扰动为 $(\bar a)$ 后，元素 $b$ 成为 $f(\bar a,X)$ 的一个近似解。当 $(\bar a)$ 趋于 $(a)$ 时，$f(\bar a,b)$ 趋于 $0$，而 $D_{n+1}f(\bar a,b)$ 趋于 $D_{n+1}f(a,b)\ne0$。因此当 $(\bar a)$ 充分接近 $(a)$ 时，命题 7.6 的条件成立，可以把 $b$ 改进为 $f(\bar a,X)$ 的一个根，从而证明断言。

这个结果在我的论文 “On Quasi Algebraic Closure” 中起了关键作用。它是第十一章关于实域的定理 3.6 的类似结果。

用代数几何的语言（现在假定读者熟悉这种语言），可以把结果重新表述如下。设 $V$ 是定义在 $K$ 上的一个簇，$P$ 是 $V$ 的一个 $K$ 有理非奇异点。则 $P$ 在 $V(K)$ 中有一个全部由非奇异点组成的邻域。特别地，假设 $V$ 由某个素域上的有限生成域 $k$ 上的有限多个多项式方程定义。经过一个适当的投影，可以假设该簇是仿射的，并且如上述断言中那样由一个方程 $f(X_1,\ldots,X_{n+1})=0$ 定义，而该点为上述 $P=(a_1,\ldots,a_n,b)$。于是可以选取接近 $a_i$ 的 $\bar a_i=x_i$，同时使 $(x_1,\ldots,x_n)$ 在 $k$ 上代数无关。设 $y$ 是把 $b$ 改进所得的元素，使 $f(x,y)=0$。则 $(x,y)$ 是 $V$ 在 $k$ 上的一个一般点，而 $(x,y)$ 的坐标属于 $K$。用几何术语说，这意味着该簇的函数域可以在 $k$ 上嵌入 $K$，如同第十一章定理 3.6 给出了嵌入实闭域（例如实数域）的类似结果。

## 习题

**1. (a)** 设 $K$ 是带有一个赋值的域。若

$$
f(X)=a_0+a_1X+\cdots+a_nX^n
$$

是 $K[X]$ 中的一个多项式，定义 $|f|$ 为各值 $|a_i|$（$i=0,\ldots,n$）的最大值。证明这定义了赋值到 $K[X]$ 的一个延拓，并证明该赋值还可以延拓到有理函数域 $K(X)$。高斯引理如何成为上述断言的一个特殊情形？推广到多变量多项式。

**(b)** 设 $f$ 是具有复系数的一个多项式。定义 $|f|$ 为各系数绝对值的最大值。设 $d$ 是一个 $\geq1$ 的整数。证明<span class="original-page-anchor" id="pdf-page-507" aria-hidden="true"></span>存在常数 $C_1,C_2$（只依赖于 $d$），使得若 $f,g$ 是 $\mathbf C[X]$ 中次数 $\leq d$ 的多项式，则

$$
C_1|f||g|\leq|fg|\leq C_2|f||g|.
$$

[**提示：** 对一次因子的数目作归纳。注意右边的不等式是平凡的。]

**2.** 设 $M_{\mathbf Q}$ 是由有理数域 $\mathbf Q$ 上的通常绝对值以及所有 $p$ 进绝对值 $v_p$ 组成的集合。证明对于任意有理数 $a\in\mathbf Q$，$a\ne0$，有

$$
\prod_{v\in M_{\mathbf Q}}|a|_v=1.
$$

若 $K$ 是 $\mathbf Q$ 的一个有限扩张，$M_K$ 表示 $K$ 上延拓 $M_{\mathbf Q}$ 中绝对值的绝对值所成的集合，并且对每个 $w\in M_K$，以 $N_w$ 表示局部次数 $[K_w:\mathbf Q_v]$，则证明对于 $\alpha\in K$，$\alpha\ne0$，有

$$
\prod_{w\in M_K}|\alpha|_w^{N_w}=1.
$$

**3.** 证明 $p$ 进数域 $\mathbf Q_p$ 除了恒等映射之外没有其他自同构。[**提示：** 证明这样的自同构关于 $p$ 进拓扑连续。利用推论 7.5，给出接近 $1$ 的元素的代数刻画。]

**4.** 设 $A$ 是主理想整环，$K$ 是它的分式域。设 $\mathfrak o$ 是 $K$ 的一个包含 $A$ 的赋值环，并假设 $\mathfrak o\ne K$。证明对于某个素元 $p$，$\mathfrak o$ 是局部环 $A_{(p)}$。[这既适用于环 $\mathbf Z$，也适用于域 $k$ 上的多项式环 $k[X]$。]

**5.** 设 $A$ 是由常数项系数属于 $\mathbf Z$ 的多项式 $f(X)\in\mathbf Q[X]$ 组成的子环。证明 $A$ 中的每个有限生成理想都是主理想，但 $A$ 中常数项系数为 $0$ 的多项式组成的理想不是主理想。[Laura Wesson 向我指出了上述例子，它给出了此前各版和印次中所述习题的一个反例：取 $\mathbf Q(X)$ 上包含 $\mathbf Q$ 且使 $X$ 的阶为 $1$ 的赋值环 $\mathfrak o$。那么对于 $A$ 的任意元素 $p$，都有 $\mathfrak o\ne A_{(p)}$。]

**6.** 设 $\mathbf Q_p$ 是一个 $p$ 进数域。证明 $\mathbf Q_p$ 包含无限多个形如 $\mathbf Q(\sqrt{-m})$ 的二次域，其中 $m$ 为正整数。

**7.** 证明 $p$ 进整数环 $\mathbf Z_p$ 是紧的。证明 $\mathbf Z_p$ 的可逆元群是紧的。

**8.** 若 $K$ 是关于一个离散赋值完备且剩余域有限的域，$\mathfrak o$ 是 $K$ 中阶 $\geq0$ 的元素所成的环，则证明 $\mathfrak o$ 是紧的。证明 $\mathfrak o$ 的可逆元群在 $\mathfrak o$ 中闭，并且是紧的。

**9.** 设 $K$ 是关于一个离散赋值完备的域，$\mathfrak o$ 是 $K$ 的整数环，并假设 $\mathfrak o$ 是紧的。设 $f_1,f_2,\ldots$ 是系数属于 $\mathfrak o$ 的 $n$ 元多项式序列。假设所有这些多项式的次数都 $\leq d$，并且它们收敛到一个多项式 $f$（即当 $i\longrightarrow\infty$ 时，$|f-f_i|\longrightarrow0$）。若每个 $f_i$ 在 $\mathfrak o$ 中都有零点，证明 $f$ 在 $\mathfrak o$ 中也有零点。若多项式 $f_i$ 都是 $d$ 次齐次多项式，而且每个 $f_i$ 在 $\mathfrak o$ 中都有非平凡零点，证明 $f$ 在 $\mathfrak o$ 中也有非平凡零点。[**提示：** 利用 $\mathfrak o$ 的紧性；在齐次情形，还利用 $\mathfrak o$ 的可逆元群的紧性。]

（关于本题以及命题 7.6 的应用，参见我的论文 “On quasi-algebraic closure”，*Annals of Math.*，**55**（1952），第 412–444 页。）

<span class="original-page-anchor" id="pdf-page-508" aria-hidden="true"></span>

**10.** 证明若 $p,p'$ 是两个不同的素数，则域 $\mathbf Q_p$ 与 $\mathbf Q_{p'}$ 不同构。

**11.** 证明域 $\mathbf Q_p$ 含有所有 $(p-1)$ 次单位根。[**提示：** 将命题 7.6 应用于多项式 $X^{p-1}-1$，它在剩余域中分裂为一次因子。] 证明两个不同的 $(p-1)$ 次单位根不可能模 $p$ 同余。

**12. (a)** 设 $f(X)$ 是 $\mathbf Z[X]$ 中次数 $\geq1$ 的一个多项式。证明当 $a$ 遍历 $\mathbf Z$ 时，各值 $f(a)$ 被无限多个素数整除。

**(b)** 设 $F$ 是 $\mathbf Q$ 的一个有限扩张。证明有无限多个素数 $p$，使 $F$ 的所有共轭域（在 $\mathbf Q_p$ 的一个代数闭包中）实际上都包含在 $\mathbf Q_p$ 中。[**提示：** 利用一个包含 $F$ 的 $\mathbf Q$ 的伽罗瓦扩张的生成元的不可约多项式。]

**13.** 设 $K$ 是特征为 $0$、关于一个非阿基米德绝对值完备的域。证明级数

$$
\exp(x)=1+x+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots
$$

$$
\log(1+x)=x-\frac{x^2}{2}+\frac{x^3}{3}-\cdots
$$

在 $0$ 的某个邻域中收敛。（主要困难发生在剩余域的特征为 $p>0$ 时，因为此时 $p$ 整除分母 $n!$ 和 $n$。求出一个确定 $n!$ 中所含 $p$ 的幂次的表达式。）证明 exp 与 log 给出互逆的映射，把 $0$ 的一个邻域与 $1$ 的一个邻域相对应。

**14.** 设 $K$ 如上一题，是特征为 $0$、关于一个非阿基米德绝对值完备的域。对于每个整数 $n>0$，证明 $(1+x)^{1/n}$ 的通常二项式展开在 $0$ 的某个邻域中收敛。先在剩余域的特征不整除 $n$ 的假设下证明，此时证明要简单得多。

**15.** 设 $F$ 是关于一个离散赋值完备的域，$\mathfrak o$ 是赋值环，$\pi$ 是一个素元，并假设 $\mathfrak o/(\pi)=k$。证明若 $a,b\in\mathfrak o$ 且 $a\equiv b\pmod{\pi^r}$，其中 $r>0$，则对所有整数 $n\geq0$，有 $a^{p^n}\equiv b^{p^n}\pmod{\pi^{r+n}}$。

> **译校注：** 原题没有定义 $p$，也没有假设 $k$ 的特征为正数。所用同余结论需要 $p=\operatorname{char}k>0$：若 $p$ 在赋值环中可逆，则取 $a=1+\pi$、$b=1$，通常 $a^p-b^p$ 只有一阶，不能模 $\pi^2$ 为零。此处保留原题并明确缺失的条件。

**16.** 设 $F$ 如上。证明 $\mathfrak o/(\pi)$ 在 $\mathfrak o$ 中存在一组代表 $R$，满足 $R^p=R$，而且这组代表唯一（Teichmüller）。[**提示：** 设 $\alpha$ 是 $k$ 中的一个剩余类。对于每个 $\nu\geq0$，取 $\alpha^{p^{-\nu}}$ 在 $\mathfrak o$ 中的一个代表 $a_\nu$，并证明序列 $a_\nu^{p^\nu}$ 在 $\nu\longrightarrow\infty$ 时收敛，而且收敛到 $\alpha$ 的一个代表 $a$，不依赖于 $a_\nu$ 的选择。] 证明这样得到的代表集 $R$ 对乘法封闭；若 $F$ 的特征为 $p$，则 $R$ 还对加法封闭，并且与 $k$ 同构。

> **译校注：** 除上一题漏写的 $p=\operatorname{char}k>0$ 外，本题还需要 $k$ 为完美域，否则提示中的 $\alpha^{p^{-\nu}}$ 不一定存在，且 $R^p=R$ 会迫使 $k^p=k$。例如取 $k=\mathbf F_p(t)$、$F=k((\pi))$，便不可能有这样的 $R$。此处保留原题，不把其结论用于不满足这些条件的剩余域。

**17. (a)（再论维特向量）。** 设 $k$ 是特征为 $p$ 的完美域。使用第六章习题中所述的维特向量。可以在 $W(k)$ 上定义一个绝对值：若 $x_r$ 是 $x$ 的第一个非零分量，则令 $|x|=p^{-r}$。证明这是环上定义的一个绝对值，它显然是离散的，并且可以立即延拓到分式域。证明这个分式域是完备的，并注意 $W(k)$ 是其赋值环。极大理想由满足 $x_0=0$ 的 $x$ 组成，即等于 $pW(k)$。

<span class="original-page-anchor" id="pdf-page-509" aria-hidden="true"></span>

**(b)** 假设 $F$ 的特征为 $0$。把每个向量 $x\in W(k)$ 映到元素

$$
\sum\xi_i^{p^{-i}}p^i,
$$

其中 $\xi_i$ 是 $x_i$ 在习题 16 的特殊代表系中的代表。证明这个映射是 $W(k)$ 到 $\mathfrak o$ 的一个嵌入。

> **译校注：** 原书这里引用 “Exercise 15”，但特殊代表系是在习题 16 中构造的，故改为习题 16。公式中的指数 $p^{-i}$ 按原页逐字核对保留。

**18.（局部一致化）。** 设 $k$ 是一个域，$K$ 是超越次数为 $1$ 的有限生成扩张，$\mathfrak o$ 是 $K$ 在 $k$ 上的一个离散赋值环，极大理想为 $\mathfrak m$。假设 $\mathfrak o/\mathfrak m=k$。设 $x$ 是 $\mathfrak m$ 的一个生成元，并假设 $K$ 在 $k(x)$ 上可分。证明存在一个元素 $y\in\mathfrak o$，使 $K=k(x,y)$，而且具有下述性质。设 $\varphi$ 是由 $\mathfrak o$ 确定的 $K$ 上的地方。令 $a=\varphi(x)$、$b=\varphi(y)$（当然 $a=0$）。设 $f(X,Y)$ 是 $k[X,Y]$ 中满足 $f(x,y)=0$ 的不可约多项式。则 $D_2f(a,b)\ne0$。[**提示：** 先写成 $K=k(x,z)$，其中 $z$ 在 $k[x]$ 上整。设 $z=z_1,\ldots,z_n$（$n\geq2$）是 $z$ 在 $k(x)$ 上的共轭元素，并把 $\mathfrak o$ 延拓为 $k(x,z_1,\ldots,z_n)$ 的一个赋值环 $\mathfrak O$。设

$$
z=a_0+a_1x+\cdots+a_rx^r+\cdots
$$

是 $z$ 的幂级数展开，$a_i\in k$，并令 $P_r(x)=a_0+\cdots+a_rx^r$。对于 $i=1,\ldots,n$，令

$$
y_i=\frac{z_i-P_r(x)}{x^r}.
$$

取 $r$ 充分大，证明 $y_1$ 在 $\mathfrak O$ 处没有极点，但 $y_2,\ldots,y_n$ 在 $\mathfrak O$ 处有极点。元素 $y_1,\ldots,y_n$ 在 $k(x)$ 上共轭。设 $f(X,Y)$ 是 $(x,y)$ 在 $k$ 上的不可约多项式。则 $f(x,Y)=\psi_n(x)Y^n+\cdots+\psi_0(x)$，其中 $\psi_i(x)\in k[x]$。还可以假设 $\psi_i(0)\ne0$（因为 $f$ 不可约）。把 $f(x,Y)$ 写成

$$
f(x,Y)=\psi_n(x)y_2\cdots y_n(Y-y_1)(y_2^{-1}Y-1)\cdots(y_n^{-1}Y-1).
$$

> **译校注：** 原书 “with $\psi_i(x)k[x]$” 中漏印了关系符号；由各系数的定义补为 $\psi_i(x)\in k[x]$。随后 $\psi_i(0)\ne0$ 指至少有一个系数在 $0$ 处非零，否则 $x$ 将整除整个不可约多项式。

证明 $\psi_n(x)y_2\cdots y_n=u$ 在 $\mathfrak O$ 处没有极点。若 $w\in\mathfrak O$，以 $\bar w$ 表示其模 $\mathfrak O$ 的极大理想的剩余类。则

$$
0\ne\bar f(\bar x,Y)=(-1)^{n-1}\bar u(Y-\bar y_1).
$$

令 $y=y_1$，$\bar y=b$。得到 $D_2f(a,b)=(-1)^{n-1}\bar u\ne0$。]

**19.** 证明习题 18 的逆命题：若 $K=k(x,y)$，$f(X,Y)$ 是 $(x,y)$ 在 $k$ 上的不可约多项式，且 $a,b\in k$ 满足 $f(a,b)=0$，但 $D_2f(a,b)\ne0$，则 $K$ 存在唯一的赋值环 $\mathfrak o$，极大理想为 $\mathfrak m$，使 $x\equiv a$、$y\equiv b\pmod{\mathfrak m}$。此外，$\mathfrak o/\mathfrak m=k$，且 $x-a$ 是 $\mathfrak m$ 的一个生成元。[**提示：** 若 $g(x,y)\in k[x,y]$ 满足 $g(a,b)=0$，证明 $g(x,y)=(x-a)A(x,y)/B(x,y)$，其中 $A,B$ 是多项式，且 $B(a,b)\ne0$。若 $A(a,b)=0$，则重复这个过程。证明该过程不能无限重复，从而得到所需断言的证明。]

> **译校注：** 原书印为 “converse of Exercise 17”。这里关于 $k(x,y)$ 的断言对应上一题的局部一致化，故应为习题 18。

**20.（Iss’sa-Hironaka，*Ann. of Math* 83（1966），第 34–46 页）。** 本题要求熟练掌握复变函数知识。设 $K$ 是复平面 $\mathbf C$ 上亚纯函数所成的域。设 $\mathfrak O$ 是 $K$ 的一个离散赋值环（包含常数<span class="original-page-anchor" id="pdf-page-510" aria-hidden="true"></span>$\mathbf C$）。证明函数 $z$ 属于 $\mathfrak O$。[**提示：** 设 $a_1,a_2,\ldots$ 是一个趋于无穷的离散复数序列，例如正整数序列。对某个素数 $p$，取一个整数序列 $v_1,v_2,\ldots$，其中 $0\leq v_i\leq p-1$，使 $\sum v_ip^i$ 不是一个有理数的 $p$ 进展开。设 $f$ 是一个整函数，在每个 $a_i$ 处有一个 $v_ip^i$ 阶零点，且没有其他零点。若 $z$ 不属于 $\mathfrak o$，考虑商

$$
g(z)=\frac{f(z)}{\prod_{i=1}^n(z-a_i)^{v_ip^i}}.
$$

由整函数的魏尔斯特拉斯分解，证明对某个整函数 $h(z)$ 有 $g(z)=h(z)^{p^{n+1}}$。现在用 $f$ 以及 $\prod(z-a_i)^{v_ip^i}$ 在 $\mathfrak o$ 的离散赋值下的阶，分析 $g$ 在这个赋值下的零点，从而得到矛盾。]

若 $U$ 是一个非紧黎曼面，$L$ 是 $U$ 上亚纯函数所成的域，而 $\mathfrak o$ 是 $L$ 的一个包含常数的离散赋值环，证明 $U$ 上的每个全纯函数 $\varphi$ 都属于 $\mathfrak o$。[**提示：** 取映射 $\varphi:U\longrightarrow\mathbf C$，将 $\varphi$ 与 $\mathbf C$ 上的亚纯函数复合，从而得到 $K$ 的一个离散赋值。应用本题的第一部分。] 证明这个赋值环是与 $U$ 的某个点对应的赋值环。[**进一步提示：** 若不熟悉黎曼面，就在复平面上证明。对每个 $z\in U$，取一个在 $U$ 上全纯且仅在 $z$ 处有一个一阶零点的函数 $f_z$。若对于某个 $z_0$，函数 $f_{z_0}$ 在 $\mathfrak o$ 处的阶 $\geq1$，则证明 $\mathfrak o$ 是与 $z_0$ 对应的赋值环。否则，每个函数 $f_z$ 在 $\mathfrak o$ 处的阶都是 $0$。用一个与本题第一部分相似的极限技巧，推出 $\mathfrak o$ 的赋值在任何全纯函数上都是平凡的。]

> **译校注：** 在一般黎曼面的段落中，原书印为 “associated with a complex number”。后面的提示所用的是 $z_0\in U$，故一般情形应说与 $U$ 的一个点对应；当 $U=\mathbf C$ 时，该点才是一个复数。
