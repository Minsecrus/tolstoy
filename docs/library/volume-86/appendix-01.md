---
title: "附录一：e 与 π 的超越性"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第二十一章 有限自由解消","link":"/library/volume-86/chapter-021"}
next: {"text":"附录二：集合论基础","link":"/library/volume-86/appendix-02"}
---

# 附录一：e 与 π 的超越性

<span class="original-page-anchor" id="pdf-page-875" aria-hidden="true"></span>

我们在这里给出的证明，遵循经过适当表述的 Gelfond 和 Schneider 的经典方法。它以一个关于满足微分方程的函数的取值的定理为基础；人们早已认识到，在各种情形下，这类取值都受到严格的限制。这里，我们处理最一般的代数微分方程。

我们假设读者熟悉复变函数的基本事实。设 $f$ 是一个整函数（即在复平面上全纯的函数）。为本附录的目的，若存在一个数 $C>1$，使得对于所有充分大的 $R$，只要 $|z|\leqq R$，就有

$$
|f(z)|\leqq C^{R^\rho},
$$

则称 $f$ 的阶 $\leqq\rho$。若一个亚纯函数是两个阶 $\leqq\rho$ 的整函数之商，则称其阶 $\leqq\rho$。

**定理。** *设 $K$ 是有理数域的一个有限扩张。设 $f_1,\ldots,f_N$ 是阶 $\leqq\rho$ 的亚纯函数。假设域 $K(f_1,\ldots,f_N)$ 在 $K$ 上的超越次数 $\geqq2$，且微分算子 $D=d/dz$ 将环 $K[f_1,\ldots,f_N]$ 映入自身。设 $w_1,\ldots,w_m$ 是互不相同的复数，均不是任何 $f_i$ 的极点，并且对于所有 $i=1,\ldots,N$ 及 $\nu=1,\ldots,m$，都有*

$$
f_i(w_\nu)\in K.
$$

*则 $m\leqq10\rho[K:\mathbf Q]$。*

**推论 1。** （Hermite-Lindemann）*若 $\alpha$ 是（在 $\mathbf Q$ 上）代数的且 $\ne0$，则 $e^\alpha$ 是超越数。因此 $\pi$ 是超越数。*

<span class="original-page-anchor" id="pdf-page-876" aria-hidden="true"></span>

*证明。* 假设 $\alpha$ 和 $e^\alpha$ 都是代数数。令 $K=\mathbf Q(\alpha,e^\alpha)$。两个函数 $z$ 和 $e^z$ 在 $K$ 上代数独立（这是显然的），而微分算子显然将环 $K[z,e^z]$ 映入自身。对于任意 $m$，我们的函数在 $\alpha,2\alpha,\ldots,m\alpha$ 处都取 $K$ 中的代数值，矛盾。由于 $e^{2\pi i}=1$，可知 $2\pi i$ 是超越数。

**推论 2。** （Gelfond-Schneider）*若 $\alpha$ 是代数数且 $\ne0,1$，$\beta$ 是代数无理数，则 $\alpha^\beta=e^{\beta\log\alpha}$ 是超越数。*

*证明。* 按照推论 1 的方法，考虑函数 $e^{\beta t}$ 和 $e^t$；由于假设 $\beta$ 是无理数，它们代数独立。考察数 $\log\alpha,2\log\alpha,\ldots,m\log\alpha$，便如推论 1 中一样得到矛盾。

在给出证明定理的主要论证之前，先陈述几个引理。前两个引理由 Siegel 给出，涉及线性齐次方程的整数解。

**引理 1。** *设*

$$
\begin{gathered}
a_{11}x_1+\cdots+a_{1n}x_n=0\\
\cdots\\
a_{r1}x_1+\cdots+a_{rn}x_n=0
\end{gathered}
$$

*是一个具有整数系数 $a_{ij}$ 的线性方程组，且 $n>r$。设 $A$ 是一个数，使得对于所有 $i,j$，都有 $|a_{ij}|\leqq A$。则存在一个非平凡的整数解，满足*

$$
|x_j|\leqq2(2nA)^{r/(n-r)}.
$$

*证明。* 将此线性方程组看作一个线性方程 $L(X)=0$，其中 $L$ 是由系数矩阵确定的线性映射 $L:\mathbf Z^{(n)}\longrightarrow\mathbf Z^{(r)}$。若 $B$ 是正数，用 $\mathbf Z^{(n)}(B)$ 表示 $\mathbf Z^{(n)}$ 中满足 $|X|\leqq B$ 的向量 $X$ 的集合（其中 $|X|$ 是 $X$ 的各系数的绝对值的最大值）。于是 $L$ 将 $\mathbf Z^{(n)}(B)$ 映入 $\mathbf Z^{(r)}(nBA)$。$\mathbf Z^{(n)}(B)$ 中的元素个数 $\geqq B^n$ 且 $\leqq(2B+1)^n$。我们要寻找一个 $B$，使得 $\mathbf Z^{(n)}(B)$ 中有两个不同的元素 $X,Y$ 具有相同的像，即 $L(X)=L(Y)$。为此，只需 $B^n>(2nBA)^r$，因而只需

$$
B=(2nA)^{r/(n-r)}.
$$

取 $X-Y$ 作为问题的解。

设 $K$ 是 $\mathbf Q$ 的一个有限扩张，$I_K$ 是 $\mathbf Z$ 在 $K$ 中的整闭包。由第 IX 章习题 5，知道 $I_K$ 是 $\mathbf Z$ 上的自由模，其维数为 $[K:\mathbf Q]$。将 $K$ 看作包含于复数域中。若<span class="original-page-anchor" id="pdf-page-877" aria-hidden="true"></span>$\alpha\in K$，则将 $\alpha$ 的共轭定义为形如 $\sigma\alpha$ 的元素，其中 $\sigma$ 是 $K$ 到 $\mathbf C$ 的一个嵌入。所谓 $K$ 中一组元素的**大小**，是指这些元素的所有共轭的绝对值的最大值。

向量 $X=(x_1,\ldots,x_n)$ 的大小，是指其坐标集合的大小。

设 $\omega_1,\ldots,\omega_M$ 是 $I_K$ 在 $\mathbf Z$ 上的一组基。设 $\alpha\in I_K$，并写成

$$
\alpha=a_1\omega_1+\cdots+a_M\omega_M.
$$

设 $\omega'_1,\ldots,\omega'_M$ 是 $\omega_1,\ldots,\omega_M$ 关于迹的对偶基。于是可以将 $\alpha$ 的（Fourier）系数 $a_j$ 表示为一个迹：

$$
a_j=\operatorname{Tr}(\alpha\omega'_j).
$$

迹是各共轭之和。因此，这些系数的大小有上界，等于 $\alpha$ 的大小乘以一个固定常数，此常数取决于元素 $\omega'_j$ 的大小。

**引理 2。** *设 $K$ 是 $\mathbf Q$ 的一个有限扩张。设*

$$
\begin{gathered}
\alpha_{11}x_1+\cdots+\alpha_{1n}x_n=0\\
\cdots\\
\alpha_{r1}x_1+\cdots+\alpha_{rn}x_n=0
\end{gathered}
$$

*是一个系数在 $I_K$ 中的线性方程组，且 $n>r$。设 $A$ 是一个数，使得对于所有 $i,j$，都有 $\operatorname{size}(\alpha_{ij})\leqq A$。则存在 $I_K$ 中的一个非平凡解 $X$，满足*

$$
\operatorname{size}(X)\leqq C_1(C_2nA)^{r/(n-r)},
$$

*其中 $C_1,C_2$ 是仅取决于 $K$ 的常数。*

*证明。* 设 $\omega_1,\ldots,\omega_M$ 是 $I_K$ 在 $\mathbf Z$ 上的一组基。每个 $x_j$ 都可以写成

$$
x_j=\xi_{j1}\omega_1+\cdots+\xi_{jM}\omega_M,
$$

其中 $\xi_{j\lambda}$ 是未知数。每个 $\alpha_{ij}$ 都可以写成

$$
\alpha_{ij}=a_{ij1}\omega_1+\cdots+a_{ijM}\omega_M,
$$

其中整数 $a_{ij\lambda}\in\mathbf Z$。将 $\alpha_{ij}x_j$ 展开相乘，就发现这个系数在 $I_K$ 中的线性方程组，等价于一个关于 $nM$ 个未知数 $\xi_{j\lambda}$ 的 $rM$ 个线性方程的方程组，其系数在 $\mathbf Z$ 中，大小有上界 $CA$，其中 $C$ 是一个仅取决于 $M$、元素 $\omega_\lambda$ 的大小以及乘积 $\omega_\lambda\omega_\mu$ 的数；换言之，$C$ 仅取决于 $K$。应用引理 1，得到用 $\xi_{j\lambda}$ 表示的一个解，从而得到 $I_K$ 中的一个解 $X$，其大小满足所要求的上界。

<span class="original-page-anchor" id="pdf-page-878" aria-hidden="true"></span>

下一个引理涉及导数的估计。对于系数在 $K$ 中的多项式，其大小是指它的系数集合的大小。$K$ 中一组元素的一个**分母**，是指一个正有理整数，其与这组元素中每个元素的乘积都是代数整数。对于系数在 $K$ 中的多项式，也以类似方式定义分母。将“分母”缩写为 den。

设

$$
P(T_1,\ldots,T_N)=\sum\alpha_{(\nu)}M_{(\nu)}(T)
$$

是一个具有复系数的多项式，并设

$$
Q(T_1,\ldots,T_N)=\sum\beta_{(\nu)}M_{(\nu)}(T)
$$

是一个实系数 $\geqq0$ 的多项式。若对于所有 $(\nu)$ 都有 $|\alpha_{(\nu)}|\leqq\beta_{(\nu)}$，则称 **$Q$ 控制 $P$**。随即可以验证，控制关系在加法、乘法及对变量 $T_1,\ldots,T_N$ 求偏导数下保持。

**引理 3。** *设 $K$ 在 $\mathbf Q$ 上次数有限。设 $f_1,\ldots,f_N$ 是在点 $w\in\mathbf C$ 的某个邻域内全纯的函数，并假设 $D=d/dz$ 将环 $K[f_1,\ldots,f_N]$ 映入自身。假设对于所有 $i$，都有 $f_i(w)\in K$。则存在一个数 $C_1$，具有如下性质。设 $P(T_1,\ldots,T_N)$ 是系数在 $K$ 中、次数 $\leqq r$ 的多项式。若令 $f=P(f_1,\ldots,f_N)$，则对于所有正整数 $k$，都有*

$$
\operatorname{size}(D^kf(w))\leqq\operatorname{size}(P)r^kk!C_1^{k+r}.
$$

*此外，$D^kf(w)$ 有一个分母，其上界为 $\operatorname{den}(P)C_1^{k+r}$。*

*证明。* 存在系数在 $K$ 中的多项式 $P_i(T_1,\ldots,T_N)$，使得

$$
Df_i=P_i(f_1,\ldots,f_N).
$$

设 $h$ 是它们的次数的最大值。在 $K[T_1,\ldots,T_N]$ 上存在唯一的导子 $\bar D$，使得 $\bar DT_i=P_i(T_1,\ldots,T_N)$。对于任意多项式 $P$，都有

$$
\bar D(P(T_1,\ldots,T_N))=\sum_{i=1}^N(D_iP)(T_1,\ldots,T_N)\cdot P_i(T_1,\ldots,T_N),
$$

其中 $D_1,\ldots,D_N$ 是偏导数算子。多项式 $P$ 受

$$
\operatorname{size}(P)(1+T_1+\cdots+T_N)^r
$$

控制，而每个 $P_i$ 都受 $\operatorname{size}(P_i)(1+T_1+\cdots+T_N)^h$ 控制。因此 $\bar DP$ 受

$$
\operatorname{size}(P)C_2r(1+T_1+\cdots+T_N)^{r+h}
$$

控制。

<span class="original-page-anchor" id="pdf-page-879" aria-hidden="true"></span>

归纳下去，可以看到 $\bar D^kP$ 受

$$
\operatorname{size}(P)C_3^kr^kk!(1+T_1\cdots+T_N)^{r+kh}
$$

控制。

将 $T_i$ 替换为 $f_i(w)$，就得到所要求的 $D^kf(w)$ 的上界。关于分母的第二个断言，也可以用一个简单的归纳法证明。

现在进入定理证明的主要部分。设 $f,g$ 是 $f_1,\ldots,f_N$ 中在 $K$ 上代数独立的两个函数。设 $r$ 是一个可被 $2m$ 整除的正整数。在证明的最后将令 $r$ 趋于无穷。

设

$$
F=\sum_{i,j=1}^r b_{ij}f^ig^j
$$

的系数 $b_{ij}$ 在 $K$ 中。令 $n=r^2/2m$。可以选取不全为 $0$ 的 $b_{ij}$，使得对于 $0\leqq k<n$ 及 $\nu=1,\ldots,m$，有

$$
D^kF(w_\nu)=0.
$$

事实上，需要求解的是一个关于 $r^2=2mn$ 个未知数的 $mn$ 个线性方程的方程组。注意

$$
\frac{mn}{2mn-mn}=1.
$$

将这些方程乘以系数的一个分母。利用引理 3 的估计及引理 2，实际上可以取 $b_{ij}$ 为代数整数，其大小在 $n\longrightarrow\infty$ 时有上界

$$
O(r^nn!C_1^{n+r})\leqq O(n^{2n}).
$$

由于 $f,g$ 在 $K$ 上代数独立，函数 $F$ 不恒为零。令 $s$ 为最小的整数，使得 $F$ 的所有直到 $s-1$ 阶的导数都在各点 $w_1,\ldots,w_m$ 处为零，但 $D^sF$ 在其中一个 $w$ 处不为零，比如在 $w_1$ 处。于是 $s\geqq n$。令

$$
\gamma=D^sF(w_1)\ne0.
$$

于是 $\gamma$ 是 $K$ 的一个元素，并且由引理 3，它有一个分母，在 $s\longrightarrow\infty$ 时有上界 $O(C_1^s)$。设 $c$ 为这个分母。$c\gamma$ 从 $K$ 到 $\mathbf Q$ 的范数是一个非零的有理整数。$c\gamma$ 的每个共轭都有上界 $O(s^{5s})$。因此得到

$$
\tag{1}1\leqq|N_{\mathbf Q}^K(c\gamma)|\leqq O(s^{5s})^{[K:\mathbf Q]-1}|\gamma|,
$$

<span class="original-page-anchor" id="pdf-page-880" aria-hidden="true"></span>

其中 $|\gamma|$ 是 $\gamma$ 的固定绝对值，现在将通过整体性的论证对其作出很好的估计。

设 $\theta$ 是一个阶 $\leqq\rho$ 的整函数，使得 $\theta f$ 和 $\theta g$ 都是整函数，且 $\theta(w_1)\ne0$。于是 $\theta^{2r}F$ 是整函数。考虑整函数

$$
H(z)=\frac{\theta(z)^{2r}F(z)}{\displaystyle\prod_{\nu=1}^m(z-w_\nu)^s}.
$$

$H(w_1)$ 与 $D^sF(w_1)$ 相差若干显然的因子，这些因子的上界为 $C_4^ss!$。由最大模原理，其绝对值的上界为 $H$ 在半径 $R$ 的大圆上的最大值。若取 $R$ 充分大，则 $z-w_\nu$ 的绝对值近似等于 $R$；因此，在半径 $R$ 的圆上，$H(z)$ 的绝对值受如下形式的表达式控制：

$$
\frac{s^{3s}C_5^{2rR^\rho}}{R^{ms}}.
$$

选取 $R=s^{1/2\rho}$。于是得到估计

$$
|\gamma|\leqq\frac{s^{4s}C_6^s}{s^{ms/2\rho}}.
$$

现在令 $r$ 趋于无穷。于是 $n$ 和 $s$ 都趋于无穷。将最后一个不等式与不等式 (1) 结合，便得到所要求的 $m$ 的上界。证明完毕。

当然，在估计中出现的 $s$ 的幂次方面，我们并未力求特别精细；显然，只要在估计中更仔细一点，就可以减小数 $10$。

我们证明的定理，只是关于超越次数问题的一个广泛理论中最简单的结果。在某种意义上，若不添加假设，这个定理已经是最佳的。例如，若 $P(t)$ 是一个具有整数系数的多项式，则 $e^{P(t)}$ 在 $P$ 的所有根处都取值 $1$，而这些根都是代数数。此外，函数

$$
t,e^t,e^{t^2},\ldots,e^{t^n}
$$

是代数独立的，但在 $t$ 的所有整数值处都取 $\mathbf Q(e)$ 中的值。

然而，我们期望关于代数独立性的相当强的结果成立。Lindemann 证明了：*若 $\alpha_1,\ldots,\alpha_n$ 是在 $\mathbf Q$ 上线性独立的代数数，则*

$$
e^{\alpha_1},\ldots,e^{\alpha_n}
$$

*代数独立。*

<span class="original-page-anchor" id="pdf-page-881" aria-hidden="true"></span>

更一般地，Schanuel 提出了如下猜想：若 $\alpha_1,\ldots,\alpha_n$ 是在 $\mathbf Q$ 上线性独立的复数，则

$$
\alpha_1,\ldots,\alpha_n,e^{\alpha_1},\ldots,e^{\alpha_n}
$$

的超越次数应当 $\geqq n$。

由此可立即推出 $e$ 与 $\pi$ 的代数独立性（考察 $1,2\pi i,e,e^{2\pi i}$），以及关于普通指数函数和对数的一切其他我们认为应当成立的独立性断言。例如，$\pi$ 不可能属于这样得到的域：从代数数出发，添加指数函数的值，取代数闭包，并反复进行这两个操作。这类断言涉及指数函数的值落在某些超越次数 $<n$ 的域中的情形；我们希望通过适当地深化定理 1，能够得到所期望的结果。
