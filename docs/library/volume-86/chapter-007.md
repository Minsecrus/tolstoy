---
title: "第七章 环的扩张"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第六章 伽罗瓦理论","link":"/library/volume-86/chapter-006"}
next: {"text":"第八章 超越扩张","link":"/library/volume-86/chapter-008"}
---

# 第七章 环的扩张

<span class="original-page-anchor" id="pdf-page-347" aria-hidden="true"></span>

只处理域扩张并非总是合适。有时，我们希望将一个环扩张模某个素理想约化，从而得到域扩张。这一过程出现在若干背景中，因此需要介绍环上的伽罗瓦自同构的基本理论，尤其考察伽罗瓦自同构如何作用于素理想或剩余类域。定理 2.9 后的两个例子说明，在环上研究，从而在两个很不相同的背景下得到扩张族，是非常重要的。

**在本章中，$A,B,C$ 始终表示交换环。**

## §1. 环的整扩张

在第五章和第六章中，我们研究了域的代数扩张。出于若干原因，有必要研究环的代数扩张。例如，给定一个整系数多项式，如 $X^5-X-1$，对于任意素数 $p$，都可以把这个多项式模 $p$ 约化，从而得到一个系数属于有限域的多项式。再举一例，考虑多项式

$$
X^n+s_{n-1}X^{n-1}+\cdots+s_0,
$$

其中 $s_{n-1},\ldots,s_0$ 在域 $k$ 上代数无关。这个多项式的系数属于 $k[s_0,\ldots,s_{n-1}]$，用 $k$ 中的元素代入 $s_0,\ldots,s_{n-1}$，便得到系数属于 $k$ 的多项式。这样就可以<span class="original-page-anchor" id="pdf-page-348" aria-hidden="true"></span>通过对多项式系数所在的环取一个同态，获得有关多项式的信息。本章将简要介绍环上多项式的基本事实。

设 $M$ 为 $A$-模。如果对于任意 $a\in A$，只要 $aM=0$ 就有 $a=0$，则称 $M$ 为**忠实模**。注意，$A$ 作为自身上的模是忠实的，因为 $A$ 含有单位元。此外，如果 $A\ne 0$，则 $A$ 上的忠实模不可能是零模。

设 $A$ 为 $B$ 的子环，$\alpha\in B$。下面的条件等价：

**INT 1。** 元素 $\alpha$ 是某个多项式

$$
X^n+a_{n-1}X^{n-1}+\cdots+a_0
$$

的根，其中系数 $a_i\in A$，次数 $n\geq 1$。（关键之处是首项系数等于 $1$。）

**INT 2。** 子环 $A[\alpha]$ 是有限生成 $A$-模。

**INT 3。** 存在一个 $A[\alpha]$ 上的忠实模，它是有限生成 $A$-模。

下面证明这些条件等价。假设 **INT 1** 成立。设 $g(X)$ 是 $A[X]$ 中次数 $\geq 1$、首项系数为 $1$ 且满足 $g(\alpha)=0$ 的多项式。如果 $f(X)\in A[X]$，则

$$
f(X)=q(X)g(X)+r(X),
$$

其中 $q,r\in A[X]$，且 $\deg r<\deg g$。因此 $f(\alpha)=r(\alpha)$；如果 $\deg g=n$，则 $1,\alpha,\ldots,\alpha^{n-1}$ 是 $A[\alpha]$ 作为 $A$-模的一组生成元。

对于上述 $g$，若 $g(\alpha)=0$，则称方程 $g(X)=0$ 为 $\alpha$ 在 $A$ 上的一个**整方程**。

假设 **INT 2** 成立。取模为 $A[\alpha]$ 本身。

假设 **INT 3** 成立，设 $M$ 为 $A[\alpha]$ 上的忠实模，并且在 $A$ 上由有限个元素 $w_1,\ldots,w_n$ 生成。由于 $\alpha M\subset M$，存在元素 $a_{ij}\in A$，使得

$$
\begin{aligned}
\alpha w_1&=a_{11}w_1+\cdots+a_{1n}w_n,\\
&\cdots\\
\alpha w_n&=a_{n1}w_1+\cdots+a_{nn}w_n.
\end{aligned}
$$

把 $\alpha w_1,\ldots,\alpha w_n$ 移到这些等式右边，可知行列式

$$
d=\begin{vmatrix}
\alpha-a_{11}&&&\\
&\alpha-a_{22}&&-a_{ij}\\
-a_{ij}&&\ddots&\\
&&&\alpha-a_{nn}
\end{vmatrix}
$$

<span class="original-page-anchor" id="pdf-page-349" aria-hidden="true"></span>

满足 $dM=0$。（这一点将在讨论行列式的那一章证明。）由于 $M$ 是忠实模，必有 $d=0$。因此，$\alpha$ 是多项式

$$
\det(X\delta_{ij}-a_{ij})
$$

的根，从而得到 $\alpha$ 在 $A$ 上的一个整方程。

满足条件 **INT 1、2、3** 的元素 $\alpha$，称为在 $A$ 上**整的**元素。

**命题 1.1。** *设 $A$ 为整环，$K$ 为其分式域，$\alpha$ 在 $K$ 上代数。那么存在 $A$ 中的元素 $c\ne 0$，使得 $c\alpha$ 在 $A$ 上整。*

*证明。* 存在方程

$$
a_n\alpha^n+a_{n-1}\alpha^{n-1}+\cdots+a_0=0,
$$

其中 $a_i\in A$，且 $a_n\ne 0$。将它乘以 $a_n^{n-1}$，则

$$
(a_n\alpha)^n+\cdots+a_0a_n^{n-1}=0
$$

是 $a_n\alpha$ 在 $A$ 上的整方程。命题得证。

设 $A\subset B$ 为交换环 $C$ 的子环，$\alpha\in C$。如果 $\alpha$ 在 $A$ 上整，则它当然也在 $B$ 上整。因此，扩大基环时整性保持不变。特别地，$\alpha$ 在 $A$ 与 $B$ 之间的任意中间环上都整。

设 $B$ 包含 $A$ 作为子环。如果 $B$ 的每个元素都在 $A$ 上整，就称 $B$ 在 $A$ 上**整**。

**命题 1.2。** *如果 $B$ 在 $A$ 上整，而且是有限生成 $A$-代数，则 $B$ 是有限生成 $A$-模。*

*证明。* 可以对环生成元的个数作归纳。因此，考虑环塔

$$
A\subset A[\alpha_1]\subset A[\alpha_1,\alpha_2]\subset\cdots\subset A[\alpha_1,\ldots,\alpha_n]=B,
$$

就可以假设 $B=A[\alpha]$，其中 $\alpha$ 在 $A$ 上整。然而已经知道，在这种情形下结论成立，这是整性的定义的一部分。

与域扩张的情形一样，如果环扩张 $A\subset B$ 的一个类 $\mathcal C$ 满足下列类似性质，就称它为**特殊类**：

**(1)** 设 $A\subset B\subset C$ 为环塔。扩张 $A\subset C$ 属于 $\mathcal C$，当且仅当 $A\subset B$ 与 $B\subset C$ 都属于 $\mathcal C$。

**(2)** 如果 $A\subset B$ 属于 $\mathcal C$，$C$ 为 $A$ 的任意扩环，并且 $B,C$ 都是某个环的子环，则 $C\subset B[C]$ 属于 $\mathcal C$。（注意，$B[C]=C[B]$ 是同时包含 $B$ 与 $C$ 的最小环。）

<span class="original-page-anchor" id="pdf-page-350" aria-hidden="true"></span>

与域的情形一样，形式上由 (1) 和 (2) 可推出 (3)，即：

**(3)** 如果 $A\subset B$ 和 $A\subset C$ 都属于 $\mathcal C$，并且 $B,C$ 是某个环的子环，则 $A\subset B[C]$ 属于 $\mathcal C$。

**命题 1.3。** *环的整扩张构成特殊类。*

*证明。* 设 $A\subset B\subset C$ 为环塔。如果 $C$ 在 $A$ 上整，显然 $B$ 在 $A$ 上整，且 $C$ 在 $B$ 上整。反过来，假设塔中每一步扩张都整。取 $\alpha\in C$，则 $\alpha$ 满足整方程

$$
\alpha^n+b_{n-1}\alpha^{n-1}+\cdots+b_0=0,
$$

其中 $b_i\in B$。令 $B_1=A[b_0,\ldots,b_{n-1}]$。由命题 1.2，$B_1$ 是有限生成 $A$-模，而且显然忠实。于是 $B_1[\alpha]$ 在 $B_1$ 上有限，因而在 $A$ 上有限，所以 $\alpha$ 在 $A$ 上整。因此，$C$ 在 $A$ 上整。最后，设 $B,C$ 为 $A$ 的扩环，并假设 $B$ 在 $A$ 上整。假设 $B,C$ 是某个环的子环。则 $C[B]$ 在 $C$ 上由 $B$ 的元素生成，而 $B$ 的每个元素都在 $C$ 上整。由下面的命题立即可得，$C[B]$ 在 $C$ 上整。

**命题 1.4。** *设 $A$ 为 $C$ 的子环。那么，$C$ 中在 $A$ 上整的元素构成 $C$ 的子环。*

*证明。* 设 $\alpha,\beta\in C$ 在 $A$ 上整。令 $M=A[\alpha]$，$N=A[\beta]$。则 $MN$ 包含 $1$，因此作为 $A$-模是忠实的。此外，$\alpha M\subset M$，$\beta N\subset N$。所以，乘以 $\alpha\pm\beta$ 或 $\alpha\beta$ 都把 $MN$ 映入自身。另外，$MN$ 在 $A$ 上有限生成（若 $\{w_i\}$ 是 $M$ 的生成元，$\{v_j\}$ 是 $N$ 的生成元，则 $\{w_iv_j\}$ 是 $MN$ 的生成元）。命题得证。

命题 1.4 中，$C$ 内所有在 $A$ 上整的元素的集合，称为 **$A$ 在 $C$ 中的整闭包**。

**例。** 考虑整数环 $\mathbf Z$。设 $K$ 为 $\mathbf Q$ 的有限扩张，称 $K$ 为**数域**。$\mathbf Z$ 在 $K$ 中的整闭包称为 $K$ 的**代数整数**环。这是最经典的例子。

在代数几何中，考虑 $\mathbf Z$ 或域 $k$ 上的有限生成整环 $R$。设 $F$ 为 $R$ 的分式域。再考虑 $R$ 在 $F$ 中的整闭包，可以证明它在 $R$ 上有限。如果 $K$ 是 $F$ 的有限扩张，还可考虑 $R$ 在 $K$ 中的整闭包。

**命题 1.5。** *设 $A\subset B$ 为环扩张，且 $B$ 在 $A$ 上整。设 $\sigma$ 为 $B$ 的同态。那么 $\sigma(B)$ 在 $\sigma(A)$ 上整。*

*证明。* 取 $\alpha\in B$，设

$$
\alpha^n+a_{n-1}\alpha^{n-1}+\cdots+a_0=0
$$

<span class="original-page-anchor" id="pdf-page-351" aria-hidden="true"></span>

为 $\alpha$ 在 $A$ 上的整方程。施以 $\sigma$，得到

$$
\sigma(\alpha)^n+\sigma(a_{n-1})\sigma(\alpha)^{n-1}+\cdots+\sigma(a_0)=0,
$$

从而证明了结论。

**推论 1.6。** *设 $A$ 为整环，$k$ 为其分式域，$E$ 为 $k$ 的有限扩张。设 $\alpha\in E$ 在 $A$ 上整。那么 $\alpha$（从 $E$ 到 $k$）的范数与迹在 $A$ 上整，$\alpha$ 在 $k$ 上满足的不可约多项式的系数也在 $A$ 上整。*

*证明。* 对 $E$ 在 $k$ 上的每个嵌入 $\sigma$，$\sigma\alpha$ 都在 $A$ 上整。由于范数是所有这样的 $\sigma\alpha$ 的乘积（再取特征的某个幂次），所以范数在 $A$ 上整。迹同理；$\operatorname{Irr}(\alpha,k,X)$ 的系数也同理，因为它们是根的初等对称函数。

设 $A$ 为整环，$k$ 为其分式域。如果 $A$ 等于它在 $k$ 中的整闭包，则称 $A$ 为**整闭**的。

**命题 1.7。** *设 $A$ 为唯一分解整环。那么 $A$ 整闭。*

*证明。* 假设存在商 $a/b$，其中 $a,b\in A$，它在 $A$ 上整；又存在 $A$ 中的素元 $p$，它整除 $b$ 但不整除 $a$。对于某个整数 $n\geq 1$ 及 $a_i\in A$，有

$$
(a/b)^n+a_{n-1}(a/b)^{n-1}+\cdots+a_0=0,
$$

因此

$$
a^n+a_{n-1}ba^{n-1}+\cdots+a_0b^n=0.
$$

由于 $p$ 整除 $b$，必整除 $a^n$，因而必整除 $a$，矛盾。

设 $f:A\to B$ 为环同态（$A,B$ 为交换环）。回忆，这样的同态也称为 **$A$-代数**。可以把 $B$ 看作 $A$-模。如果 $B$ 在 $f(A)$ 上整，就说 $B$（关于环同态 $f$）在 $A$ 上整。这样推广整性的定义很有用，因为在某些应用中发生部分塌缩时，我们仍希望谈论整性。严格地说，不应说 $B$ 在 $A$ 上整，而应说 **$f$ 是整环同态**，或简称 **$f$ 整**。我们将经常使用这一术语。

前面的某些命题对于整环同态有直接推论。例如，如果 $f:A\to B$ 和 $g:B\to C$ 都整，则 $g\circ f:A\to C$ 整。然而，$g\circ f$ 整并不一定推出 $f$ 整。

设 $f:A\to B$ 整，$S$ 为 $A$ 的乘法子集。于是得到同态

$$
S^{-1}f:S^{-1}A\to S^{-1}B,
$$

其中严格地说，$S^{-1}B=(f(S))^{-1}B$，而 $S^{-1}f$ 定义为

$$
(S^{-1}f)(x/s)=f(x)/f(s).
$$

<span class="original-page-anchor" id="pdf-page-352" aria-hidden="true"></span>

容易验证，这是一个同态。有交换图

$$
\begin{array}{ccc}
B&\longrightarrow&S^{-1}B\\
f\ \uparrow&&\uparrow\ S^{-1}f\\
A&\longrightarrow&S^{-1}A
\end{array}
$$

其中横向映射为典范映射：$x\to x/1$。

**命题 1.8。** *设 $f:A\to B$ 整，$S$ 为 $A$ 的乘法子集。那么 $S^{-1}f:S^{-1}A\to S^{-1}B$ 整。*

*证明。* 如果 $\alpha\in B$ 在 $f(A)$ 上整，对于 $a\in A$ 和 $\beta\in B$，以 $a\beta$ 代替 $f(a)\beta$，则有

$$
\alpha^n+a_{n-1}\alpha^{n-1}+\cdots+a_0=0,
$$

其中 $a_i\in A$。分别取在 $S^{-1}A$ 与 $S^{-1}B$ 中的典范像，可以看出，此关系证明 $\alpha/1$ 在 $S^{-1}A$ 上整；此时系数为 $a_i/1$。

**命题 1.9。** *设 $A$ 为整闭整环，$S$ 为 $A$ 的乘法子集，且 $0\notin S$。那么 $S^{-1}A$ 整闭。*

*证明。* 设 $\alpha$ 是分式域中在 $S^{-1}A$ 上整的元素。有方程

$$
\alpha^n+\frac{a_{n-1}}{s_{n-1}}\alpha^{n-1}+\cdots+\frac{a_0}{s_0}=0,
$$

其中 $a_i\in A$，$s_i\in S$。令 $s=s_{n-1}\cdots s_0$。显然 $s\alpha$ 在 $A$ 上整，所以属于 $A$。因此 $\alpha\in S^{-1}A$，故 $S^{-1}A$ 整闭。

设 $\mathfrak p$ 为环 $A$ 的素理想，$S$ 为 $\mathfrak p$ 在 $A$ 中的补集，记 $S=A-\mathfrak p$。如果 $f:A\to B$ 是 $A$-代数（即环同态），则用 $B_{\mathfrak p}$ 代替 $S^{-1}B$。可以把 $B_{\mathfrak p}$ 看作 $A_{\mathfrak p}=S^{-1}A$-模。

设 $A$ 为 $B$ 的子环，$\mathfrak p$ 为 $A$ 的素理想，$\mathfrak P$ 为 $B$ 的素理想。如果 $\mathfrak P\cap A=\mathfrak p$，就说 **$\mathfrak P$ 位于 $\mathfrak p$ 之上**。在这种情形下，单射 $A\to B$ 诱导商环之间的单射

$$
A/\mathfrak p\to B/\mathfrak P,
$$

实际上有交换图：

$$
\begin{array}{ccc}
B&\longrightarrow&B/\mathfrak P\\
\uparrow&&\uparrow\\
A&\longrightarrow&A/\mathfrak p
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-353" aria-hidden="true"></span>

其中横向箭头为典范同态，纵向箭头为单射。

如果 $B$ 在 $A$ 上整，则由命题 1.5，$B/\mathfrak P$ 在 $A/\mathfrak p$ 上整。

**命题 1.10。** *设 $A$ 为 $B$ 的子环，$\mathfrak p$ 为 $A$ 的素理想，并假设 $B$ 在 $A$ 上整。那么 $\mathfrak pB\ne B$，且存在 $B$ 的素理想 $\mathfrak P$ 位于 $\mathfrak p$ 之上。*

*证明。* 已知 $B_{\mathfrak p}$ 在 $A_{\mathfrak p}$ 上整，而 $A_{\mathfrak p}$ 是局部环，其极大理想为 $\mathfrak m_{\mathfrak p}=S^{-1}\mathfrak p$，其中 $S=A-\mathfrak p$。显然

$$
\mathfrak pB_{\mathfrak p}=\mathfrak pA_{\mathfrak p}B_{\mathfrak p}=\mathfrak m_{\mathfrak p}B_{\mathfrak p},
$$

所以只需在 $A$ 为局部环时证明第一个结论。（注意，素理想 $\mathfrak p$ 的存在说明 $1\ne 0$，而且 $\mathfrak pB=B$ 当且仅当 $1\in\mathfrak pB$。）在这种情形下，如果 $\mathfrak pB=B$，则 $1$ 可以表示为 $B$ 中元素的有限线性组合，系数属于 $\mathfrak p$：

$$
1=a_1b_1+\cdots+a_nb_n,
$$

其中 $a_i\in\mathfrak p$，$b_i\in B$。现在采用仿佛 $A_{\mathfrak p}\subset B_{\mathfrak p}$ 的记号。即使只使用典范同态 $A_{\mathfrak p}\to B_{\mathfrak p}$，以下论证仍然有效，这一点留给读者验证作为练习。令 $B_0=A[b_1,\ldots,b_n]$。则 $\mathfrak pB_0=B_0$，而由命题 1.2，$B_0$ 是有限 $A$-模。由 Nakayama 引理，$B_0=0$，矛盾。（参见第十章引理 4.1。）

为了证明第二个结论，考虑交换图：

$$
\begin{array}{ccc}
B&\longrightarrow&B_{\mathfrak p}\\
\uparrow&&\uparrow\\
A&\longrightarrow&A_{\mathfrak p}
\end{array}
$$

刚才已经证明 $\mathfrak m_{\mathfrak p}B_{\mathfrak p}\ne B_{\mathfrak p}$。因此 $\mathfrak m_{\mathfrak p}B_{\mathfrak p}$ 包含于 $B_{\mathfrak p}$ 的某个极大理想 $\mathfrak M$。取原像可知，$\mathfrak M$ 在 $A_{\mathfrak p}$ 中的原像是包含 $\mathfrak m_{\mathfrak p}$ 的理想（在包含关系 $A_{\mathfrak p}\subset B_{\mathfrak p}$ 下，原像就是 $\mathfrak M\cap A_{\mathfrak p}$）。由于 $\mathfrak m_{\mathfrak p}$ 极大，有 $\mathfrak M\cap A_{\mathfrak p}=\mathfrak m_{\mathfrak p}$。令 $\mathfrak P$ 为 $\mathfrak M$ 在 $B$ 中的原像（在包含关系下，$\mathfrak P=\mathfrak M\cap B$）。则 $\mathfrak P$ 为 $B$ 的素理想。$\mathfrak m_{\mathfrak p}$ 在 $A$ 中的原像就是 $\mathfrak p$。沿图中的两条路径取 $\mathfrak M$ 的原像，得到

$$
\mathfrak P\cap A=\mathfrak p,
$$

结论得证。

**命题 1.11。** *设 $A$ 为 $B$ 的子环，并假设 $B$ 在 $A$ 上整。设 $\mathfrak P$ 为 $B$ 的素理想，位于 $A$ 的素理想 $\mathfrak p$ 之上。那么 $\mathfrak P$ 极大，当且仅当 $\mathfrak p$ 极大。*

<span class="original-page-anchor" id="pdf-page-354" aria-hidden="true"></span>

*证明。* 假设 $\mathfrak p$ 在 $A$ 中极大。则 $A/\mathfrak p$ 是域，$B/\mathfrak P$ 是在 $A/\mathfrak p$ 上整的整环。如果 $\alpha\in B/\mathfrak P$，则 $\alpha$ 在 $A/\mathfrak p$ 上代数，已知 $A/\mathfrak p[\alpha]$ 是域。因此 $B/\mathfrak P$ 的每个非零元素都在 $B/\mathfrak P$ 中可逆，所以它是域。反过来，假设 $\mathfrak P$ 在 $B$ 中极大。则 $B/\mathfrak P$ 是域，并且在整环 $A/\mathfrak p$ 上整。如果 $A/\mathfrak p$ 不是域，它就有非零极大理想 $\mathfrak m$。由命题 1.10，存在 $B/\mathfrak P$ 的素理想 $\mathfrak M$ 位于 $\mathfrak m$ 之上，且 $\mathfrak M\ne 0$，矛盾。

## §2. 整伽罗瓦扩张

现在研究一个多项式的伽罗瓦理论与同一多项式模某个素理想约化后的伽罗瓦理论之间的关系。

**命题 2.1。** *设 $A$ 为整环，在其分式域 $K$ 中整闭。设 $L$ 为 $K$ 的有限伽罗瓦扩张，伽罗瓦群为 $G$。设 $\mathfrak p$ 为 $A$ 的极大理想，$\mathfrak P,\mathfrak Q$ 为 $A$ 在 $L$ 中的整闭包 $B$ 的素理想，并且位于 $\mathfrak p$ 之上。那么存在 $\sigma\in G$，使得 $\sigma\mathfrak P=\mathfrak Q$。*

*证明。* 假设对任意 $\sigma\in G$，都有 $\mathfrak Q\ne\sigma\mathfrak P$。那么对于任意一对元素 $\sigma,\tau\in G$，都有 $\tau\mathfrak Q\ne\sigma\mathfrak P$。由中国剩余定理，存在 $x\in B$，使得

$$
\begin{aligned}
x&\equiv 0\pmod{\sigma\mathfrak P},&&\text{所有 }\sigma\in G,\\
x&\equiv 1\pmod{\sigma\mathfrak Q},&&\text{所有 }\sigma\in G.
\end{aligned}
$$

范数

$$
N_K^L(x)=\prod_{\sigma\in G}\sigma x
$$

属于 $B\cap K=A$（因为 $A$ 整闭），而且属于 $\mathfrak P\cap A=\mathfrak p$。然而，对于所有 $\sigma\in G$，都有 $x\notin\sigma\mathfrak Q$，所以对所有 $\sigma\in G$，都有 $\sigma x\notin\mathfrak Q$。这与 $x$ 的范数属于 $\mathfrak p=\mathfrak Q\cap A$ 矛盾。

通过局部化，可以去掉 $\mathfrak p$ 极大的假设，只需假设 $\mathfrak p$ 为素理想。

**推论 2.2。** *设 $A$ 在其分式域 $K$ 中整闭。设 $E$ 为 $K$ 的有限可分扩张，$B$ 为 $A$ 在 $E$ 中的整闭包。设 $\mathfrak p$ 为 $A$ 的极大理想。那么位于 $\mathfrak p$ 之上的 $B$ 的素理想只有有限多个。*

*证明。* 设 $L$ 为包含 $E$ 的最小的 $K$ 的伽罗瓦扩张。如果 $\mathfrak Q_1,\mathfrak Q_2$ 是 $B$ 中位于 $\mathfrak p$ 之上的两个不同素理想，$\mathfrak P_1,\mathfrak P_2$ 是 $A$ 在 $L$ 中的整闭包的素理想，分别位于 $\mathfrak Q_1,\mathfrak Q_2$ 之上，则 $\mathfrak P_1\ne\mathfrak P_2$。这一论证把问题归结到 $E$ 在 $K$ 上伽罗瓦的情形，此时结论就是命题的直接推论。

<span class="original-page-anchor" id="pdf-page-355" aria-hidden="true"></span>

设 $A$ 在其分式域 $K$ 中整闭，$B$ 为 $A$ 在有限伽罗瓦扩张 $L$ 中的整闭包，伽罗瓦群为 $G$。那么对每个 $\sigma\in G$，都有 $\sigma B=B$。设 $\mathfrak p$ 为 $A$ 的极大理想，$\mathfrak P$ 为 $B$ 中位于 $\mathfrak p$ 之上的极大理想。用 $G_{\mathfrak P}$ 表示 $G$ 中由所有满足 $\sigma\mathfrak P=\mathfrak P$ 的自同构组成的子群。则 $G_{\mathfrak P}$ 自然作用于剩余类域 $B/\mathfrak P$，并固定 $A/\mathfrak p$。对每个 $\sigma\in G_{\mathfrak P}$，可对应一个 $B/\mathfrak P$ 在 $A/\mathfrak p$ 上的自同构 $\bar\sigma$，映射

$$
\sigma\mapsto\bar\sigma
$$

诱导从 $G_{\mathfrak P}$ 到 $B/\mathfrak P$ 在 $A/\mathfrak p$ 上的自同构群的同态。

群 $G_{\mathfrak P}$ 称为 $\mathfrak P$ 的**分解群**。其固定域记为 $L^{\mathrm{dec}}$，称为 $\mathfrak P$ 的**分解域**。令 $B^{\mathrm{dec}}$ 为 $A$ 在 $L^{\mathrm{dec}}$ 中的整闭包，$\mathfrak Q=\mathfrak P\cap B^{\mathrm{dec}}$。由命题 2.1，$\mathfrak P$ 是 $B$ 中位于 $\mathfrak Q$ 之上的唯一素理想。

设 $G=\bigcup\sigma_jG_{\mathfrak P}$ 为 $G_{\mathfrak P}$ 在 $G$ 中的陪集分解。素理想 $\sigma_j\mathfrak P$ 恰好是 $B$ 中位于 $\mathfrak p$ 之上的所有不同素理想。事实上，对于 $\sigma,\tau\in G$，有 $\sigma\mathfrak P=\tau\mathfrak P$ 当且仅当 $\tau^{-1}\sigma\mathfrak P=\mathfrak P$，即 $\tau^{-1}\sigma\in G_{\mathfrak P}$。因此 $\tau,\sigma$ 属于模 $G_{\mathfrak P}$ 的同一个陪集。

于是立即可知，素理想 $\sigma\mathfrak P$ 的分解群为 $\sigma G_{\mathfrak P}\sigma^{-1}$。

**命题 2.3。** *域 $L^{\mathrm{dec}}$ 是 $L$ 中包含 $K$ 的最小子域 $E$，使得 $\mathfrak P$ 是 $B$ 中位于 $\mathfrak P\cap E$ 之上的唯一素理想（$\mathfrak P\cap E$ 是 $B\cap E$ 的素理想）。*

*证明。* 设 $E$ 如上，$H$ 为 $L$ 在 $E$ 上的伽罗瓦群。令 $\mathfrak q=\mathfrak P\cap E$。由命题 2.1，$B$ 中位于 $\mathfrak q$ 之上的所有素理想都在 $H$ 的元素作用下共轭。由于只有一个这样的素理想，即 $\mathfrak P$，故 $H$ 保持 $\mathfrak P$ 不变。因此 $H\subset G_{\mathfrak P}$，且 $E\supset L^{\mathrm{dec}}$。已经指出，$L^{\mathrm{dec}}$ 具有所要求的性质。

**译校注：** 原书此处印作“$G\subset G_{\mathfrak P}$”。按前句“$H$ 保持 $\mathfrak P$ 不变”以及分解群的定义，应为“$H\subset G_{\mathfrak P}$”；译文据此修正。

**命题 2.4。** *沿用上述记号，在典范单射 $A/\mathfrak p\to B^{\mathrm{dec}}/\mathfrak Q$ 下，有 $A/\mathfrak p=B^{\mathrm{dec}}/\mathfrak Q$。*

*证明。* 如果 $\sigma\in G$ 但 $\sigma\notin G_{\mathfrak P}$，则 $\sigma\mathfrak P\ne\mathfrak P$，且 $\sigma^{-1}\mathfrak P\ne\mathfrak P$。令

$$
\mathfrak Q_\sigma=\sigma^{-1}\mathfrak P\cap B^{\mathrm{dec}}.
$$

则 $\mathfrak Q_\sigma\ne\mathfrak Q$。取 $x\in B^{\mathrm{dec}}$，存在 $y\in B^{\mathrm{dec}}$，使得

$$
\begin{aligned}
y&\equiv x\pmod{\mathfrak Q}\\
y&\equiv 1\pmod{\mathfrak Q_\sigma}
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-356" aria-hidden="true"></span>

对每个属于 $G$ 但不属于 $G_{\mathfrak P}$ 的 $\sigma$ 成立。因此特别地，

$$
\begin{aligned}
y&\equiv x\pmod{\mathfrak P}\\
y&\equiv 1\pmod{\sigma^{-1}\mathfrak P}
\end{aligned}
$$

对每个 $\sigma\notin G_{\mathfrak P}$ 成立。第二个同余式给出

$$
\sigma y\equiv 1\pmod{\mathfrak P},
$$

对所有 $\sigma\notin G_{\mathfrak P}$ 成立。$y$ 从 $L^{\mathrm{dec}}$ 到 $K$ 的范数，是 $y$ 与其他满足 $\sigma\notin G_{\mathfrak P}$ 的因子 $\sigma y$ 的乘积。因此得到

$$
N_K^{L^{\mathrm{dec}}}(y)\equiv x\pmod{\mathfrak P}.
$$

然而，该范数属于 $K$，甚至属于 $A$，因为它是在 $A$ 上整的元素的乘积。由于 $x$ 和该范数都属于 $B^{\mathrm{dec}}$，最后这个同余式也模 $\mathfrak Q$ 成立。这恰好就是命题中结论的含义。

对于 $B$ 的元素 $x$，用 $\bar x$ 表示它在同态 $B\to B/\mathfrak P$ 下的像。于是 $\bar\sigma$ 是 $B/\mathfrak P$ 上满足

$$
\bar\sigma\bar x=(\overline{\sigma x})
$$

的自同构。

如果 $f(X)$ 是系数属于 $B$ 的多项式，用 $\tilde f(X)$ 表示它在上述同态下的自然像。即若

$$
f(X)=b_nX^n+\cdots+b_0,
$$

则

$$
\tilde f(X)=\bar b_nX^n+\cdots+\bar b_0.
$$

**命题 2.5。** *设 $A$ 在其分式域 $K$ 中整闭，$B$ 为 $A$ 在 $K$ 的有限伽罗瓦扩张 $L$ 中的整闭包，伽罗瓦群为 $G$。设 $\mathfrak p$ 为 $A$ 的极大理想，$\mathfrak P$ 为 $B$ 中位于 $\mathfrak p$ 之上的极大理想。那么 $B/\mathfrak P$ 是 $A/\mathfrak p$ 的正规扩张，映射 $\sigma\mapsto\bar\sigma$ 诱导从 $G_{\mathfrak P}$ 到 $B/\mathfrak P$ 在 $A/\mathfrak p$ 上的伽罗瓦群的满同态。*

*证明。* 令 $\bar B=B/\mathfrak P$，$\bar A=A/\mathfrak p$。$\bar B$ 的任意元素都可写成 $\bar x$，其中 $x\in B$。设 $\bar x$ 生成 $\bar B$ 在 $\bar A$ 上的一个可分子扩张，$f$ 为 $x$ 在 $K$ 上的不可约多项式。由于 $x$ 在 $A$ 上整，$f$ 的系数都属于 $A$，而且 $f$ 的所有根都在 $A$ 上整。因此

$$
f(X)=\prod_{i=1}^m(X-x_i)
$$

<span class="original-page-anchor" id="pdf-page-357" aria-hidden="true"></span>

在 $B$ 中分裂为一次因子。由于

$$
\tilde f(X)=\prod_{i=1}^m(X-\bar x_i),
$$

且所有 $\bar x_i$ 都属于 $\bar B$，故 $\tilde f$ 在 $\bar B$ 中分裂为一次因子。注意，$f(x)=0$ 推出 $\tilde f(\bar x)=0$。因此 $\bar B$ 在 $\bar A$ 上正规，而且

$$
[\bar A(\bar x):\bar A]\leq[K(x):K]\leq[L:K].
$$

这说明，$\bar A$ 在 $\bar B$ 中的最大可分子扩张在 $\bar A$ 上次数有限（使用初等域论中的本原元定理）。事实上，这个次数以 $[L:K]$ 为上界。

还需证明，映射 $\sigma\mapsto\bar\sigma$ 给出从 $G_{\mathfrak P}$ 到 $\bar B$ 在 $\bar A$ 上的伽罗瓦群的满同态。为此，先把问题归结到 $\mathfrak P$ 是 $B$ 中位于 $\mathfrak p$ 之上的唯一素理想的情形。事实上，由命题 2.4，基环与分解域中的环 $B^{\mathrm{dec}}$ 的剩余类域相同。这意味着，为证明满射性，可以取 $L^{\mathrm{dec}}$ 为基域。这就是所需的化归，可以假设 $K=L^{\mathrm{dec}}$，$G=G_{\mathfrak P}$。

在这种情形下，取 $\bar B$ 在 $\bar A$ 上的最大可分子扩张的一个生成元，设它为 $\bar x$，其中 $x\in B$。设 $f$ 为 $x$ 在 $K$ 上的不可约多项式。$\bar B$ 的任意自同构由它在 $\bar x$ 上的作用决定，并且把 $\bar x$ 映到 $\tilde f$ 的某个根。假设 $x=x_1$。给定 $f$ 的任意根 $x_i$，存在 $\sigma\in G=G_{\mathfrak P}$，使得 $\sigma x=x_i$。因此 $\bar\sigma\bar x=\bar x_i$。所以，由 $G$ 的元素诱导的 $\bar B$ 在 $\bar A$ 上的自同构在 $\tilde f$ 的根上传递作用，从而给出剩余类域的全部自同构，结论得证。

**推论 2.6。** *设 $A$ 在其分式域 $K$ 中整闭。设 $L$ 为 $K$ 的有限伽罗瓦扩张，$B$ 为 $A$ 在 $L$ 中的整闭包。设 $\mathfrak p$ 为 $A$ 的极大理想，$\varphi:A\to A/\mathfrak p$ 为典范同态，$\psi_1,\psi_2$ 为 $B$ 到给定的 $A/\mathfrak p$ 的代数闭包中的两个同态，并且延拓 $\varphi$。那么存在 $L$ 在 $K$ 上的自同构 $\sigma$，使得*

$$
\psi_1=\psi_2\circ\sigma.
$$

*证明。* $\psi_1,\psi_2$ 的核是 $B$ 的素理想，由命题 2.1，它们共轭。因此存在伽罗瓦群 $G$ 的元素 $\tau$，使 $\psi_1,\psi_2\circ\tau$ 具有相同的核。所以不失一般性，可以假设 $\psi_1,\psi_2$ 具有相同的核 $\mathfrak P$。于是存在从 $\psi_1(B)$ 到 $\psi_2(B)$ 的自同构 $\omega$，使得 $\omega\circ\psi_1=\psi_2$。由前一命题，存在 $\sigma\in G_{\mathfrak P}$，使得 $\omega\circ\psi_1=\psi_1\circ\sigma$。这就证明了所需结论。

<span class="original-page-anchor" id="pdf-page-358" aria-hidden="true"></span>

**注。** 在以上所有命题中，都可以假设 $\mathfrak p$ 为素理想而非极大理想。在这种情形下，需要在 $\mathfrak p$ 处局部化，以便应用上述证明。

在以上讨论中，映射

$$
G_{\mathfrak P}\to\bar G_{\mathfrak P}
$$

的核称为 $\mathfrak P$ 的**惯性群**。它由 $G_{\mathfrak P}$ 中在剩余类域上诱导平凡自同构的那些自同构组成。它的固定域称为**惯性域**，记为 $L^{\mathrm{in}}$。

**推论 2.7。** *假设与推论 2.6 相同，并假设 $\mathfrak P$ 是 $B$ 中位于 $\mathfrak p$ 之上的唯一素理想。设 $f(X)$ 为 $A[X]$ 中首项系数为 $1$ 的多项式。假设 $f$ 在 $K[X]$ 中不可约，并且有根 $\alpha\in B$。那么约化后的多项式 $\tilde f$ 是 $\bar A[X]$ 中某个不可约多项式的幂。*

*证明。* 由推论 2.6，$\tilde f$ 的任意两个根都在 $\bar B$ 在 $\bar A$ 上的某个同构下共轭，因此 $\tilde f$ 不能分解成互素的多项式。所以 $\tilde f$ 是一个不可约多项式的幂。

**命题 2.8。** *设 $A$ 为整环，在其分式域 $K$ 中整闭。设 $L$ 为 $K$ 的有限伽罗瓦扩张，$L=K(\alpha)$，其中 $\alpha$ 在 $A$ 上整，且设*

$$
f(X)=X^n+a_{n-1}X^{n-1}+\cdots+a_0
$$

*为 $\alpha$ 在 $K$ 上的不可约多项式，其中 $a_i\in A$。设 $\mathfrak p$ 为 $A$ 的极大理想，$\mathfrak P$ 为 $A$ 在 $L$ 中的整闭包 $B$ 的素理想，并且位于 $\mathfrak p$ 之上。设 $\tilde f(X)$ 为系数属于 $A/\mathfrak p$ 的约化多项式，$G_{\mathfrak P}$ 为分解群。如果 $\tilde f$ 无重根，则映射 $\sigma\mapsto\bar\sigma$ 的核平凡，并给出从 $G_{\mathfrak P}$ 到 $\tilde f$ 在 $A/\mathfrak p$ 上的伽罗瓦群的同构。*

**译校注：** 原书“$\alpha$ 在 $k$ 上的不可约多项式”中的 $k$ 为小写；此命题只定义了基域 $K$，且 $L=K(\alpha)$，故应为 $K$，译文据此修正。

*证明。* 设

$$
f(X)=\prod(X-x_i)
$$

为 $f$ 在 $L$ 中的分解。已知所有 $x_i\in B$。若 $\sigma\in G_{\mathfrak P}$，则如前，用 $\bar\sigma$ 表示 $\sigma$ 在群 $\bar G_{\mathfrak P}$ 中的同态像。有

$$
\tilde f(X)=\prod(X-\bar x_i).
$$

假设对所有 $i$，都有 $\bar\sigma\bar x_i=\bar x_i$。由于 $(\overline{\sigma x_i})=\bar\sigma\bar x_i$，且 $\tilde f$ 无重根，可知 $\sigma$ 也是恒等映射。因此该映射为单射，惯性群平凡。域 $\bar A[\bar x_1,\ldots,\bar x_n]$ 是 $\bar B$ 的子域，而任意自同构<span class="original-page-anchor" id="pdf-page-359" aria-hidden="true"></span>若 $\bar B$ 在 $\bar A$ 上的自同构在这个子域上的限制为恒等映射，则它本身必为恒等映射，因为 $G_{\mathfrak P}\to\bar G_{\mathfrak P}$ 满射到 $\bar B$ 在 $\bar A$ 上的伽罗瓦群。因此 $\bar B$ 在 $\bar A[\bar x_1,\ldots,\bar x_n]$ 上纯不可分，所以 $G_{\mathfrak P}$ 同构于 $\tilde f$ 在 $\bar A$ 上的伽罗瓦群。

命题 2.8 只是更一般情形的一个特例：一个多项式的根并不一定生成伽罗瓦扩张。下面给出一个适用于计算伽罗瓦群的版本。

**定理 2.9。** *设 $A$ 为整环，在其分式域 $K$ 中整闭。设 $f(X)\in A[X]$ 的首项系数为 $1$，且在 $K$ 上不可约（或在 $A$ 上不可约，两者相同）。设 $\mathfrak p$ 为 $A$ 的极大理想，$\tilde f=f\bmod\mathfrak p$。假设 $\tilde f$ 在 $A/\mathfrak p$ 的代数闭包中无重根。设 $L$ 为 $f$ 在 $K$ 上的分裂域，$B$ 为 $A$ 在 $L$ 中的整闭包。设 $\mathfrak P$ 为 $B$ 中位于 $\mathfrak p$ 之上的任意素理想，以横线表示模 $\mathfrak p$ 约化。那么映射*

$$
G_{\mathfrak P}\to\bar G_{\mathfrak P}
$$

*给出 $G_{\mathfrak P}$ 与 $\tilde f$ 在 $\bar A$ 上的伽罗瓦群之间的同构。*

*证明。* 设 $(\alpha_1,\ldots,\alpha_n)$ 为 $f$ 在 $B$ 中的根，$(\bar\alpha_1,\ldots,\bar\alpha_n)$ 为它们模 $\mathfrak P$ 的约化。由于

$$
f(X)=\prod_{i=1}^n(X-\alpha_i),
$$

可得

$$
\tilde f(X)=\prod_{i=1}^n(X-\bar\alpha_i).
$$

$G$ 的任意元素都由其作为根的置换的作用决定，而对 $\sigma\in G_{\mathfrak P}$，有

$$
\bar\sigma\bar\alpha_i=\overline{\sigma\alpha_i}.
$$

**译校注：** 原书等式左边印作 $\bar\sigma\bar x_i$，右边为 $\overline{\sigma\alpha_i}$；本证明以 $\alpha_i$ 表示根，故左边应为 $\bar\sigma\bar\alpha_i$，译文据此统一。

因此，如果 $\bar\sigma=\operatorname{id}$，则 $\sigma=\operatorname{id}$，所以映射 $G_{\mathfrak P}\to\bar G_{\mathfrak P}$ 为单射。由命题 2.5，它为满射，故定理得证。

这一定理证明了第六章 §2 中用来计算伽罗瓦群的结论。

定理 2.9 为分析环上的多项式提供了非常有效的工具。

**例。** 考虑“通用”多项式

$$
f_w(X)=X^n+w_{n-1}X^{n-1}+\cdots+w_0
$$

<span class="original-page-anchor" id="pdf-page-360" aria-hidden="true"></span>

其中 $w_0,\ldots,w_{n-1}$ 在域 $k$ 上代数无关。已知这个多项式在域 $K=k(w_0,\ldots,w_{n-1})$ 上的伽罗瓦群是对称群。设 $t_1,\ldots,t_n$ 为其根，$\alpha$ 为分裂域 $L$ 的一个生成元，即 $L=K(\alpha)$。不失一般性，可以选取 $\alpha$ 在环 $k[w_0,\ldots,w_{n-1}]$ 上整（把任意给定的生成元乘以一个适当选取的多项式，并使用命题 1.1）。设 $g_w(X)$ 为 $\alpha$ 在 $k(w_0,\ldots,w_{n-1})$ 上的不可约多项式。$g$ 的系数是 $(w)$ 的多项式。如果能以 $(a)$ 代入 $(w)$，其中 $a_0,\ldots,a_{n-1}\in k$，并使 $g_a$ 仍不可约，那么由命题 2.8 立即可知，$g_a$ 的伽罗瓦群也是对称群。类似地，如果 $k(w_0,\ldots,w_{n-1})$ 的一个有限伽罗瓦扩张的伽罗瓦群为 $G$，则只要特化后的多项式 $g_a$ 仍不可约，就可以进行类似代入，得到伽罗瓦群为 $G$ 的 $k$ 的伽罗瓦扩张。

> **译校注：** 原书这里以“特化后的 $g_a$ 仍不可约”为充分条件；要使用命题 2.8，还须保证 $g_a$ 无重根，即可分。在特征 $0$ 下，不可约多项式自动可分；正特征下该条件不能省略。例如取 $k=\mathbf F_2(a)$（$a$ 为不定元），$g_w(X)=X^2+wX+a$。这个多项式在 $k(w)$ 上不可约：若有根 $r\in k(w)$，比较 $w=0$ 处的阶可知 $r$ 无极点且非零，约化后必有 $r(0)^2=a$，与 $a$ 在 $k$ 中无平方根矛盾。它的导数为 $w\ne0$，两个根为 $\alpha,\alpha+w$，故 $k(w)(\alpha)/k(w)$ 是伽罗瓦群为 $C_2$ 的扩张。但 $w=0$ 时，$g_0(X)=X^2+a$ 仍不可约，却定义纯不可分扩张，其自同构群平凡。上文保留原书陈述，并在此明确其所需的可分性条件。

**例。** 设 $K$ 为数域，即 $\mathbf Q$ 的有限扩张，$\mathfrak o$ 为其代数整数环。设 $L$ 为 $K$ 的有限伽罗瓦扩张，$\mathfrak O$ 为 $L$ 的代数整数环。设 $\mathfrak p$ 为 $\mathfrak o$ 的素理想，$\mathfrak P$ 为 $\mathfrak O$ 中位于 $\mathfrak p$ 之上的素理想。则 $\mathfrak o/\mathfrak p$ 为有限域，设它有 $q$ 个元素。于是 $\mathfrak O/\mathfrak P$ 是 $\mathfrak o/\mathfrak p$ 的有限扩张。由有限域理论，$\bar G_{\mathfrak P}$ 中存在唯一的元素，称为 **Frobenius 元** $\overline{\operatorname{Fr}}_{\mathfrak P}$，满足对所有 $\bar x\in\mathfrak O/\mathfrak P$，都有 $\overline{\operatorname{Fr}}_{\mathfrak P}(\bar x)=\bar x^q$。除有限多个素理想 $\mathfrak p$ 外，定理 2.9 的条件均成立；对于这样的素理想，存在唯一的 $\operatorname{Fr}_{\mathfrak P}\in G_{\mathfrak P}$，使得对所有 $x\in\mathfrak O$，都有 $\operatorname{Fr}_{\mathfrak P}(x)\equiv x^q\bmod\mathfrak P$。称 $\operatorname{Fr}_{\mathfrak P}$ 为 $G_{\mathfrak P}$ 中的 **Frobenius 元**。参见第六章 §15，那里解释了 Frobenius 元的部分意义。

## §3. 同态的延拓

最初讨论局部化过程时，我们曾很简略地考虑把同态延拓到局部环。在讨论域论时，也叙述了将一个域嵌入另一个域的延拓定理。现在将以完全一般的形式讨论延拓问题。

首先回忆局部环的情形。设 $A$ 为交换环，$\mathfrak p$ 为素理想。已知局部环 $A_{\mathfrak p}$ 是所有分式 $x/y$ 的集合，其中 $x,y\in A$，$y\notin\mathfrak p$。它的极大理想由满足 $x\in\mathfrak p$ 的分式组成。设 $L$ 为域，$\varphi:A\to L$ 为核等于 $\mathfrak p$ 的同态。对于上述 $A_{\mathfrak p}$ 的元素 $x/y$，令

$$
\varphi(x/y)=\varphi(x)/\varphi(y),
$$

便可将 $\varphi$ 延拓为从 $A_{\mathfrak p}$ 到 $L$ 的同态。

其次，考虑环的整扩张。设 $\mathfrak o$ 为极大理想为 $\mathfrak m$ 的局部环，$B$ 在 $\mathfrak o$ 上整，$\varphi:\mathfrak o\to L$ 为 $\mathfrak o$ 的一个同态<span class="original-page-anchor" id="pdf-page-361" aria-hidden="true"></span>到代数闭域 $L$。假设 $\varphi$ 的核为 $\mathfrak m$。由命题 1.10，存在 $B$ 的极大理想 $\mathfrak M$ 位于 $\mathfrak m$ 之上，即 $\mathfrak M\cap\mathfrak o=\mathfrak m$。那么 $B/\mathfrak M$ 是域，是 $\mathfrak o/\mathfrak m$ 的代数扩张；由于 $\varphi$ 的核为 $\mathfrak m$，$\mathfrak o/\mathfrak m$ 同构于 $L$ 的子域 $\varphi(\mathfrak o)$。

可以找到从 $\mathfrak o/\mathfrak m$ 到 $\varphi(\mathfrak o)$ 的同构，使复合同态

$$
\mathfrak o\to\mathfrak o/\mathfrak m\to L
$$

等于 $\varphi$。再把 $B/\mathfrak M$ 嵌入 $L$，使下图交换：

$$
\begin{array}{ccccc}
B&\longrightarrow&B/\mathfrak M&&\\
\uparrow&&\uparrow&\searrow&\\
\mathfrak o&\longrightarrow&\mathfrak o/\mathfrak m&\longrightarrow&L
\end{array}
$$

这样便得到从 $B$ 到 $L$ 的同态，延拓 $\varphi$。

**命题 3.1。** *设 $A$ 为 $B$ 的子环，并假设 $B$ 在 $A$ 上整。设 $\varphi:A\to L$ 为到代数闭域 $L$ 的同态。那么 $\varphi$ 可以延拓为从 $B$ 到 $L$ 的同态。*

*证明。* 设 $\mathfrak p$ 为 $\varphi$ 的核，$S$ 为 $\mathfrak p$ 在 $A$ 中的补集。则有交换图

$$
\begin{array}{ccc}
B&\longrightarrow&S^{-1}B\\
\uparrow&&\uparrow\\
A&\longrightarrow&S^{-1}A=A_{\mathfrak p}
\end{array}
$$

而 $\varphi$ 可以通过从 $A$ 到 $S^{-1}A$ 的典范同态分解。此外，$S^{-1}B$ 在 $S^{-1}A$ 上整。这便将问题归结到局部环的情形，而该情形刚才已经讨论过。

**定理 3.2。** *设 $A$ 为域 $K$ 的子环，$x\in K$，$x\ne 0$。设 $\varphi:A\to L$ 为 $A$ 到代数闭域 $L$ 的同态。那么 $\varphi$ 可以延拓为 $A[x]$ 或 $A[x^{-1}]$ 到 $L$ 的同态。*

*证明。* 可以先将 $\varphi$ 延拓为局部环 $A_{\mathfrak p}$ 的同态，其中 $\mathfrak p$ 为 $\varphi$ 的核。因此不失一般性，可以假设 $A$ 为极大理想为 $\mathfrak m$ 的局部环。假设

$$
\mathfrak mA[x^{-1}]=A[x^{-1}].
$$

<span class="original-page-anchor" id="pdf-page-362" aria-hidden="true"></span>

则可写成

$$
1=a_0+a_1x^{-1}+\cdots+a_nx^{-n},
$$

其中 $a_i\in\mathfrak m$。乘以 $x^n$，得到

$$
(1-a_0)x^n+b_{n-1}x^{n-1}+\cdots+b_0=0,
$$

其中 $b_i\in A$ 为适当的元素。由于 $a_0\in\mathfrak m$，可知 $1-a_0\notin\mathfrak m$；又因 $A$ 为局部环，故 $1-a_0$ 是 $A$ 中的可逆元。除以 $1-a_0$，便知 $x$ 在 $A$ 上整；因此由命题 3.1，该同态可以延拓到 $A[x]$。

另一方面，如果

$$
\mathfrak mA[x^{-1}]\ne A[x^{-1}],
$$

则 $\mathfrak mA[x^{-1}]$ 包含于 $A[x^{-1}]$ 的某个极大理想 $\mathfrak P$，而 $\mathfrak P\cap A$ 包含 $\mathfrak m$。由于 $\mathfrak m$ 极大，必有 $\mathfrak P\cap A=\mathfrak m$。$\varphi$ 与典范映射 $A\to A/\mathfrak m$ 有相同的核 $\mathfrak m$，所以可以找到从 $A/\mathfrak m$ 到 $L$ 的嵌入 $\psi$，使复合映射

$$
A\to A/\mathfrak m\xrightarrow{\psi}L
$$

等于 $\varphi$。注意，$A/\mathfrak m$ 典范地嵌入 $B/\mathfrak P$，其中 $B=A[x^{-1}]$。把 $\psi$ 延拓到 $B/\mathfrak P$ 到 $L$ 的同态；无论 $x^{-1}$ 在 $B/\mathfrak P$ 中的像在 $A/\mathfrak m$ 上超越还是代数，这都可以做到。复合映射 $B\to B/\mathfrak P\to L$ 就给出了所需延拓。

**推论 3.3。** *设 $A$ 为域 $K$ 的子环，$L$ 为代数闭域。设 $\varphi:A\to L$ 为同态，$B$ 为 $K$ 中可将 $\varphi$ 延拓为到 $L$ 的同态的极大子环。那么 $B$ 为局部环，且若 $x\in K$、$x\ne 0$，则 $x\in B$ 或 $x^{-1}\in B$。*

*证明。* 令 $S$ 为所有有序对 $(C,\psi)$ 的集合，其中 $C$ 为 $K$ 的子环，$\psi:C\to L$ 为延拓 $\varphi$ 的同态。则 $S$ 非空（包含 $(A,\varphi)$），并按递增包含关系与限制关系赋予偏序。即如果 $C\subset C'$，且 $\psi'$ 在 $C$ 上的限制等于 $\psi$，则 $(C,\psi)\leq(C',\psi')$。显然 $S$ 具有归纳序，由 Zorn 引理，存在极大元素，设为 $(B,\psi_0)$。首先，$B$ 为局部环，否则 $\psi_0$ 可延拓到由其核产生的局部环；其次，由定理 3.2，$B$ 具有所要求的性质。

设 $B$ 为域 $K$ 的子环，并具有如下性质：对于 $x\in K$、$x\ne 0$，有 $x\in B$ 或 $x^{-1}\in B$。则称 $B$ 为 $K$ 中的**赋值环**。第十二章将更详细地研究这种环。不过，下一章也会给出一些应用，所以这里再作一些说明。

<span class="original-page-anchor" id="pdf-page-363" aria-hidden="true"></span>

设 $F$ 为域。令符号 $\infty$ 满足通常的代数法则。对于 $a\in F$，定义

$$
\begin{aligned}
a\pm\infty&=\infty,\qquad a\cdot\infty=\infty\quad\text{当 }a\ne 0,\\
\infty\cdot\infty&=\infty,\qquad \frac{1}{0}=\infty,\qquad\frac{1}{\infty}=0.
\end{aligned}
$$

表达式 $\infty\pm\infty$、$0\cdot\infty$、$0/0$ 和 $\infty/\infty$ 不定义。

域 $K$ 到域 $F$ 的一个**位** $\varphi$，是从 $K$ 到由 $F$ 和 $\infty$ 组成的集合的映射

$$
\varphi:K\to\{F,\infty\},
$$

满足通常的同态法则，即只要下列公式右边的表达式有定义，就有

$$
\varphi(a+b)=\varphi(a)+\varphi(b),
$$

$$
\varphi(ab)=\varphi(a)\varphi(b),
$$

并且 $\varphi(1)=1$。也称这个位为 **$F$-值**位。$K$ 中不被映到 $\infty$ 的元素称为在该位下**有限**，其余元素称为**无限**。

读者可以立即验证，$K$ 中在一个位下有限的元素组成的集合 $\mathfrak o$，是 $K$ 的赋值环。其极大理想由满足 $\varphi(x)=0$ 的元素 $x$ 组成。反过来，如果 $\mathfrak o$ 为 $K$ 的赋值环，极大理想为 $\mathfrak m$，令 $\varphi:\mathfrak o\to\mathfrak o/\mathfrak m$ 为典范同态，并对 $x\in K$、$x\notin\mathfrak o$ 定义 $\varphi(x)=\infty$。容易验证，$\varphi$ 为一个位。

如果 $\varphi_1:K\to\{F_1,\infty\}$ 和 $\varphi_2:K\to\{F_2,\infty\}$ 是 $K$ 的位，把它们的值域限制到各自的像。因此可以假设它们都是满射。如果存在同构 $\lambda:F_1\to F_2$，使得 $\varphi_2=\lambda\circ\varphi_1$，就称它们**等价**。（令 $\lambda(\infty)=\infty$。）两个位等价，当且仅当它们具有相同的赋值环。显然，$K$ 的位的等价类与 $K$ 的赋值环之间有双射。如果一个位为单射，就称其为平凡位。平凡位的赋值环就是 $K$ 本身。

**译校注：** 原书复合公式印作 $\varphi_2=\varphi_1\circ\lambda$。由于 $\varphi_1:K\to F_1\cup\{\infty\}$、$\lambda:F_1\to F_2$，按复合映射的定义应为 $\varphi_2=\lambda\circ\varphi_1$，译文据此修正。

与同态一样，两个位的复合仍为一个位（容易验证）。

用位代替赋值环往往更方便，正如使用同态，而非总是使用典范同态或模一个理想的商环，往往更方便一样。

赋值与赋值环的一般理论归功于 Krull，见 Allgemeine Bewertungstheorie，*J. reine angew. Math.* **167**（1932），第 169-196 页。然而，上述同态延拓理论直到约 1945 年才由 Chevalley 和 Zariski 认识到。

<span class="original-page-anchor" id="pdf-page-364" aria-hidden="true"></span>

下面给出位与赋值环的一些例子。

**例 1。** 设 $p$ 为素数，$\mathbf Z_{(p)}$ 为所有分母不被 $p$ 整除的有理数组成的环。那么 $\mathbf Z_{(p)}$ 是赋值环。其极大理想由分子被 $p$ 整除的有理数组成。

**例 2。** 设 $k$ 为域，$R=k[X]$ 为一元多项式环，$p=p(X)$ 为不可约多项式。设 $\mathfrak o$ 为分母不被 $p$ 整除的有理函数组成的环。那么 $\mathfrak o$ 是赋值环，与例 1 类似。

**例 3。** 设 $R$ 为一元幂级数环 $k[[X]]$。那么 $R$ 是赋值环，极大理想由被 $X$ 整除的幂级数组成。剩余类域就是 $k$ 本身。

**例 4。** 设 $R=k[[X_1,\ldots,X_n]]$ 为多元幂级数环。则 $R$ 不是赋值环，但 $R$ 嵌入逐次幂级数域 $k((X_1))((X_2))\cdots((X_n))=K_n$。由例 3，存在一个 $K_{n-1}$-值的 $K_n$ 的位。通过归纳与复合，可以定义一个 $k$-值的 $K_n$ 的位。由于有理函数域 $k(X_1,\ldots,X_n)$ 包含于 $K_n$，把这个位限制到 $k(X_1,\ldots,X_n)$，便得到 $n$ 元有理函数域的一个 $k$-值位。

**例 5。** 第十一章将讨论有序域的概念。设 $k$ 为有序域 $K$ 的有序子域。设 $\mathfrak o$ 为 $K$ 中相对于 $k$ 不是无穷大的元素所组成的子集，$\mathfrak m$ 为 $\mathfrak o$ 中相对于 $k$ 为无穷小的元素所组成的子集。那么 $\mathfrak o$ 是 $K$ 中的赋值环，$\mathfrak m$ 是其极大理想。

位的以下性质将在下一章讨论射影空间时使用。

**命题 3.4。** *设 $\varphi:K\to\{L,\infty\}$ 为 $K$ 的一个 $L$-值位。给定有限个非零元素 $x_1,\ldots,x_n\in K$，存在指标 $j$，使 $\varphi$ 在 $x_i/x_j$ 上有限，对 $i=1,\ldots,n$ 都成立。*

*证明。* 设 $B$ 为该位的赋值环。定义 $x_i\leqq x_j$ 表示 $x_i/x_j\in B$。关系 $\leqq$ 具有传递性，即若 $x_i\leqq x_j$ 且 $x_j\leqq x_r$，则 $x_i\leqq x_r$。此外，由赋值环的性质，对于任意一对指标 $i,j$，总有 $x_i\leqq x_j$ 或 $x_j\leqq x_i$。因此可以将这些元素排序，并选取指标 $j$，使对所有 $i$，都有 $x_i\leqq x_j$。这个指标 $j$ 满足命题的要求。

借助赋值环，可以刻画整元素。采用以下术语：如果 $\mathfrak o,\mathfrak O$ 为局部环，其极大理想分别为 $\mathfrak m,\mathfrak M$，且 $\mathfrak o\subset\mathfrak O$、$\mathfrak M\cap\mathfrak o=\mathfrak m$，则称 **$\mathfrak O$ 位于 $\mathfrak o$ 之上**。于是有典范单射 $\mathfrak o/\mathfrak m\to\mathfrak O/\mathfrak M$。

<span class="original-page-anchor" id="pdf-page-365" aria-hidden="true"></span>

**命题 3.5。** *设 $\mathfrak o$ 为包含于域 $L$ 的局部环。$L$ 的元素 $x$ 在 $\mathfrak o$ 上整，当且仅当 $x$ 属于 $L$ 中每个位于 $\mathfrak o$ 之上的赋值环 $\mathfrak O$。*

*证明。* 假设 $x$ 在 $\mathfrak o$ 上不整。设 $\mathfrak m$ 为 $\mathfrak o$ 的极大理想。则 $\mathfrak o[1/x]$ 的理想 $(\mathfrak m,1/x)$ 不可能是整个环，否则可以写成

$$
-1=a_n(1/x)^n+\cdots+a_1(1/x)+y,
$$

其中 $y\in\mathfrak m$，$a_i\in\mathfrak o$。由此得到

$$
(1+y)x^n+\cdots+a_n=0.
$$

然而 $1+y\notin\mathfrak m$，所以它是 $\mathfrak o$ 的可逆元。将方程除以 $1+y$，可知 $x$ 在 $\mathfrak o$ 上整，与假设矛盾。因此 $(\mathfrak m,1/x)$ 不是整个环，并且包含于某个极大理想 $\mathfrak P$。$\mathfrak P$ 与 $\mathfrak o$ 的交包含 $\mathfrak m$，因而必等于 $\mathfrak m$。将典范同态 $\mathfrak o[1/x]\to\mathfrak o[1/x]/\mathfrak P$ 延拓为 $L$ 的某个赋值环 $\mathfrak O$ 的同态，可知 $1/x$ 的像为 $0$，所以 $x$ 不可能属于这个赋值环。

反过来，假设 $x$ 在 $\mathfrak o$ 上整，设

$$
x^n+a_{n-1}x^{n-1}+\cdots+a_0=0
$$

为 $x$ 的一个整方程，系数属于 $\mathfrak o$。设 $\mathfrak O$ 为 $L$ 中任意一个位于 $\mathfrak o$ 之上的赋值环。假设 $x\notin\mathfrak O$。令 $\varphi$ 为 $\mathfrak O$ 模其极大理想的典范同态给出的位。则 $\varphi(x)=\infty$，故 $\varphi(1/x)=0$。将上述方程除以 $x^n$，再施以 $\varphi$。除第一项外，每一项都在 $\varphi$ 下映为 $0$，所以得到 $\varphi(1)=0$，矛盾，命题得证。

**命题 3.6。** *设 $A$ 为包含于域 $L$ 的环。$L$ 的元素 $x$ 在 $A$ 上整，当且仅当 $x$ 属于 $L$ 中每个包含 $A$ 的赋值环 $\mathfrak O$。用位表述，$x$ 在 $A$ 上整，当且仅当 $L$ 的每个在 $A$ 上有限的位都在 $x$ 上有限。*

*证明。* 假设每个在 $A$ 上有限的位都在 $x$ 上有限。可以假设 $x\ne 0$。如果 $1/x$ 是 $A[1/x]$ 中的可逆元，则可以写成

$$
x=c_0+c_1(1/x)+\cdots+c_{n-1}(1/x)^{n-1},
$$

其中 $c_i\in A$，$n$ 为某个整数。乘以 $x^{n-1}$，可得 $x$ 在 $A$ 上整。如果 $1/x$ 不是 $A[1/x]$ 中的可逆元，则它生成一个真主理想。由 Zorn 引理，这个理想包含于某个极大理想 $\mathfrak M$。同态 $A[1/x]\to A[1/x]/\mathfrak M$ 可以延拓为一个在 $A$ 上有限的位，却把<span class="original-page-anchor" id="pdf-page-366" aria-hidden="true"></span>$1/x$ 映到 $0$，从而把 $x$ 映到 $\infty$。这排除了 $1/x$ 在 $A[1/x]$ 中不可逆的可能，并证明 $x$ 在 $A$ 上整。反向蕴含的证明与命题 3.5 的后半部分相同。

**注。** 设 $K$ 为 $L$ 的子域，$x\in L$。则 $x$ 在 $K$ 上整，当且仅当 $x$ 在 $K$ 上代数。因此，如果 $L$ 的一个位 $\varphi$ 在 $K$ 上有限，且 $x$ 在 $K$ 上代数，则 $\varphi$ 在 $K(x)$ 上有限。当然，这是整性判据的一个平凡情形，也可以直接看出。设

$$
x^n+a_{n-1}x^{n-1}+\cdots+a_0=0
$$

为 $x$ 在 $K$ 上的不可约方程。假设 $x\ne 0$，则 $a_0\ne 0$。由方程立即得 $\varphi(x)\ne 0$，故 $\varphi$ 给出 $K(x)$ 与其像之间的同构。

下面的结论是一个推广，其证明方法还可用于第九章练习 1（Hilbert-Zariski 定理）。

**定理 3.7。一般整性判据。** *设 $A$ 为整环。设 $z_1,\ldots,z_m$ 为其分式域 $K$ 的某个扩域中的元素。假设每个 $z_s$（$s=1,\ldots,m$）满足多项式关系*

$$
z_s^{d_s}+g_s(z_1,\ldots,z_m)=0,
$$

*其中 $g_s(Z_1,\ldots,Z_m)\in A[Z_1,\ldots,Z_m]$ 为总次数 $<d_s$ 的多项式，且 $g_s$ 中具有非零系数的 $Z_s$ 的每个纯幂的指数都严格小于 $d_s$。那么 $z_1,\ldots,z_m$ 在 $A$ 上整。*

*证明。* 应用命题 3.6。假设某个 $z_s$ 在 $A$ 上不整。则存在包含这些 $z_s$ 的扩域的一个位 $\varphi$，在 $A$ 上有限，且对某个 $s$ 有 $\varphi(z_s)=\infty$。

**译校注：** 原书此处写“$K$ 的位”，但 $K$ 是 $A$ 的分式域，而 $z_s$ 只假设在其扩域中；要使 $\varphi(z_s)$ 有定义，并应用命题 3.6，应在包含 $z_1,\ldots,z_m$ 的扩域上取位，译文据此修正。

由命题 3.4，可以选取指标 $s$，使对所有 $j$ 都有 $\varphi(z_j/z_s)\ne\infty$。把引理假设中的多项式关系除以 $z_s^{d_s}$，再施以该位。由关于 $g_s$ 的假设，得到 $\varphi(g_s(z)/z_s^{d_s})=0$，从而得到 $1=0$，矛盾，定理得证。

## 练习

**1。** 设 $K$ 为有理数域 $\mathbf Q$ 的伽罗瓦扩张，伽罗瓦群为 $G$。设 $B$ 为 $\mathbf Z$ 在 $K$ 中的整闭包，$\alpha\in B$ 满足 $K=\mathbf Q(\alpha)$。令 $f(X)=\operatorname{Irr}(\alpha,\mathbf Q,X)$。设 $p$ 为素数，并假设 $f$ 模 $p$ 后在 $\mathbf Z/p\mathbf Z$ 上仍不可约。对于伽罗瓦群 $G$，可以得出什么结论？（Artin 在 Tate 的资格考试中曾问过这个问题。）

**2。** 设 $A$ 为整环，$K$ 为其分式域，$t$ 在 $K$ 上超越。如果 $A$ 整闭，证明 $A[t]$ 整闭。

<span class="original-page-anchor" id="pdf-page-367" aria-hidden="true"></span>

*以下习题可以使用第十章第1节。*

**3.** 设 $A$ 为整环，并且在其分式域 $K$ 中整闭。设 $L$ 为 $K$ 的有限可分扩张，$B$ 为 $A$ 在 $L$ 中的整闭包。若 $A$ 是诺特环，证明 $B$ 是有限 $A$-模。［*提示：* 设 $\{\omega_1,\ldots,\omega_n\}$ 为 $L$ 在 $K$ 上的一组基。把这组基的所有元素都乘以 $A$ 中一个适当的元素，不失一般性，可以假设所有 $\omega_i$ 都在 $A$ 上整。设 $\{\omega'_1,\ldots,\omega'_n\}$ 为相对于迹的对偶基，即 $\operatorname{Tr}(\omega_i\omega'_j)=\delta_{ij}$。把 $L$ 中在 $A$ 上整的元素 $\alpha$ 写成

$$
\alpha=b_1\omega'_1+\cdots+b_n\omega'_n,
$$

其中 $b_j\in K$。对 $i=1,\ldots,n$，取迹 $\operatorname{Tr}(\alpha\omega_i)$，由此得出 $B$ 包含在有限模 $A\omega'_1+\cdots+A\omega'_n$ 中。］因此 $B$ 是诺特环。

**4.** 前一题适用于 $A=\mathbf Z$、$k=\mathbf Q$ 的情形。设 $L$ 为 $\mathbf Q$ 的有限扩张，$\mathfrak o_L$ 为 $L$ 中代数整数构成的环。设 $\sigma_1,\ldots,\sigma_n$ 为 $L$ 到复数域的各个不同的嵌入。用映射

$$
\alpha\mapsto(\sigma_1\alpha,\ldots,\sigma_n\alpha)
$$

把 $\mathfrak o_L$ 嵌入欧几里得空间。证明空间中任何有界区域都只含有有限多个 $\mathfrak o_L$ 的元素。［*提示：* $\alpha$ 的整性方程的系数是 $\alpha$ 的共轭元的初等对称函数，因此是有界的整数。］用第三章习题5得出 $\mathfrak o_L$ 是维数 $\leqq n$ 的自由 $\mathbf Z$-模。事实上，证明该维数等于 $n$，而且 $\mathfrak o_L$ 在 $\mathbf Z$ 上的一组基也是 $L$ 在 $\mathbf Q$ 上的一组基。

**5.** 设 $E$ 为 $\mathbf Q$ 的有限扩张，$\mathfrak o_E$ 为 $E$ 的代数整数环。设 $U$ 为 $\mathfrak o_E$ 的可逆元群。设 $\sigma_1,\ldots,\sigma_n$ 为 $E$ 到 $\mathbf C$ 的各个不同的嵌入。用映射

$$
l:\alpha\mapsto(\log|\sigma_1\alpha|,\ldots,\log|\sigma_n\alpha|)
$$

把 $U$ 映到欧几里得空间。通过证明空间中任何有限区域都只含有有限多个 $l(U)$ 的元素，证明 $l(U)$ 是有限生成的自由阿贝尔群。证明 $l$ 的核是有限群，因而就是 $E$ 中的单位根群。因此 $U$ 本身是有限生成的阿贝尔群。

**6.** 使用佐恩引理，把第2节的结论推广到无限伽罗瓦扩张，特别是命题2.1和2.5。

**7. 戴德金环。** 设 $\mathfrak o$ 为诺特整闭整环，并且每个非零素理想都是极大理想。分式理想 $\mathfrak a$ 定义为分式域 $K$ 的非零 $\mathfrak o$-子模，满足存在 $c\in\mathfrak o$、$c\ne0$，使 $c\mathfrak a\subset\mathfrak o$。证明分式理想在乘法下构成群。沿用范德瓦尔登的提示：依次证明以下各项：

(a) 给定 $\mathfrak o$ 中的理想 $\mathfrak a\ne0$，存在素理想的乘积 $\mathfrak p_1\cdots\mathfrak p_r\subset\mathfrak a$。

(b) 每个极大理想 $\mathfrak p$ 都可逆，即若定义 $\mathfrak p^{-1}$ 为满足 $x\mathfrak p\subset\mathfrak o$ 的元素 $x\in K$ 的集合，则 $\mathfrak p^{-1}\mathfrak p=\mathfrak o$。

(c) 每个非零理想都有一个分式理想作为其逆。（利用诺特性质：若此结论不成立，就存在一个极大的不可逆理想 $\mathfrak a$；由此导出矛盾。）

<span class="original-page-anchor" id="pdf-page-368" aria-hidden="true"></span>

**8.** 对戴德金环 $A$，用素理想代替素数，仿照高斯引理定义容度的概念，并证明：若 $f(X),g(X)\in A[X]$ 是系数在 $A$ 中、次数 $\geqq0$ 的多项式，则 $\operatorname{cont}(fg)=\operatorname{cont}(f)\operatorname{cont}(g)$。此外，若 $K$ 为 $A$ 的分式域，对 $f,g\in K[X]$ 证明同一结论。

**9.** 设 $A$ 为整闭整环。设 $B$ 为整环，并且在 $A$ 上整。设 $Q_1,Q_2$ 为 $B$ 的素理想，满足 $Q_1\supset Q_2$，但 $Q_1\ne Q_2$。令 $P_i=Q_i\cap A$。证明 $P_1\ne P_2$。

**10.** 设 $n$ 为正整数，$\zeta,\zeta'$ 为本原 $n$ 次单位根。

(a) 证明 $(1-\zeta)/(1-\zeta')$ 是代数整数。

(b) 若 $n\geqq6$ 至少可被两个素数整除，证明 $1-\zeta$ 是环 $\mathbf Z[\zeta]$ 中的可逆元。

**11.** 设 $p$ 为素数，$\zeta$ 为本原 $p$ 次单位根。证明 $\mathbf Z[\zeta]$ 中存在主理想 $J$，使 $J^{p-1}=(p)$（由 $p$ 生成的主理想）。

### 对称多项式

**12.** 设 $F$ 为特征 $0$ 的域。设 $t_1,\ldots,t_n$ 在 $F$ 上代数无关。设 $s_1,\ldots,s_n$ 为初等对称函数。那么 $R=F[t_1,\ldots,t_n]$ 是 $S=F[s_1,\ldots,s_n]$ 的整扩张，而且实际上是 $S$ 在有理函数域 $F(t_1,\ldots,t_n)$ 中的整闭包。设 $W$ 为变量 $t_1,\ldots,t_n$ 的置换群。

(a) 证明 $S=R^W$ 是 $R$ 在 $W$ 下的不动子环。

(b) 证明满足 $0\leqq r_i\leqq n-i$ 的元素 $t_1^{r_1}\cdots t_n^{r_n}$ 构成 $R$ 在 $S$ 上的一组基，因此特别地，$R$ 在 $S$ 上是自由模。

有人告诉我，上述基是克罗内克给出的。还有一组有趣得多的基，可按如下方式定义。

设 $\partial_1,\ldots,\partial_n$ 为关于 $t_1,\ldots,t_n$ 的偏导数，即 $\partial_i=\partial/\partial t_i$。设 $P\in F[t]=F[t_1,\ldots,t_n]$。用 $\partial_i$ 替换 $t_i$ $(i=1,\ldots,n)$，便得到 $R$ 上的偏微分算子 $P(\partial)=P(\partial_1,\ldots,\partial_n)$。$S$ 的元素也可以看作 $R$ 的元素。设 $Q\in R$。如果对所有常数项为 $0$ 的对称多项式 $P\in S$ 都有 $P(\partial)Q=0$，我们就说 $Q$ 是 **$W$-调和的**。可以证明，$W$-调和多项式构成有限维空间。此外，若 $\{H_1,\ldots,H_N\}$ 为这个空间在 $F$ 上的一组基，那么它也是 $R$ 在 $S$ 上的一组基。这是舍瓦莱的一个一般定理的特殊情形。见[La 99b]，其中详细讨论了这个特殊情形。
