---
title: "第九章 代数空间"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第八章 超越扩张","link":"/library/volume-86/chapter-008"}
next: {"text":"第十章 诺特环与诺特模","link":"/library/volume-86/chapter-010"}
---

# 第九章 代数空间

<span class="original-page-anchor" id="pdf-page-390" aria-hidden="true"></span>

本章给出域 $k$ 上多元多项式方程的解的基本结果。首先将证明，如果这类方程在某个域中有公共零点，那么它们在 $k$ 的代数闭包中也有公共零点，并且这样的零点可以通过称为特化的过程得到。不过，同时处理 $k$ 的超越扩张也很有用。事实上，如果 $\mathfrak{p}$ 是 $k[X]=k[X_1,\ldots,X_n]$ 中的素理想，那么 $k[X]/\mathfrak{p}$ 是 $k$ 上的有限生成环，而 $X_i$ 在这个环中的像 $x_i$ 可能在 $k$ 上超越，因此我们自然要考虑这样的环。

即使我们只想处理域上的多项式方程，也会自然地要处理整数 $\mathbf{Z}$ 上的方程。事实上，如果方程关于变量是齐次的，我们将在 §3 和 §4 中证明：存在关于这些方程系数的泛多项式，可以判定这些方程是否有公共零点。“泛”意味着其系数是整数，任何给定的特殊情形都来自将这些泛多项式特化到该情形。

既然要考虑 $\mathbf{Z}$ 上的多项式方程，我们便进而考虑 $\mathbf{Z}[X]$ 中的理想 $\mathfrak{a}$。这样一个理想的零点构成所谓的代数空间。如果 $\mathfrak{p}$ 是素理想，$\mathfrak{p}$ 的零点构成所谓的算术簇。我们将在消去理论的讨论中遇到第一个例子；在这部分中，我遵循 van der Waerden 的 *Moderne Algebra*（《近世代数》）前两版第 XI 章的处理方法。

不过，当我们对某个理想 $\mathfrak{a}$ 取多项式环 $\mathbf{Z}[X]/\mathfrak{a}$ 时，这样的商环通常具有零因子，甚至具有幂零元素。因此，也自然要考虑任意交换环，并像格罗滕迪克那样建立任意交换环上的代数几何基础。为此，我们在 §5 中给出一些基本定义。本章展示处理具体多项式理想的代数几何的风貌，而下一章则展示从交换代数发展而来的几何，以及它对刚才所说的更一般情形的系统应用。

<span class="original-page-anchor" id="pdf-page-391" aria-hidden="true"></span>

本章及下一章还将帮助读者开始阅读代数几何著作，尤其是 Hartshorne 系统阐述基础知识的著作。例如，我纳入了阅读 Hartshorne 第 I、II 章所需的那些结果。

## §1. 希尔伯特零点定理

零点定理涉及将同态的延拓定理的一个特殊情形应用于域上的有限生成环。

**定理 1.1。** *设 $k$ 是域，$k[x]=k[x_1,\ldots,x_n]$ 是 $k$ 上的有限生成环。设 $\varphi:k\to L$ 是 $k$ 到代数闭域 $L$ 的一个嵌入。则存在 $\varphi$ 到从 $k[x]$ 到 $L$ 的同态的延拓。*

*证明。* 设 $\mathfrak{M}$ 是 $k[x]$ 的一个极大理想。设 $\sigma$ 为典范同态 $\sigma:k[x]\to k[x]/\mathfrak{M}$。则 $\sigma k[\sigma x_1,\ldots,\sigma x_n]$ 是域，实际上是 $\sigma k$ 的扩域。如果能在有限生成环实际上是域的情形证明定理，就可以在 $\sigma k$ 上应用 $\varphi\circ\sigma^{-1}$，并将它延拓为从 $\sigma k[\sigma x_1,\ldots,\sigma x_n]$ 到 $L$ 的同态，从而得到所要的结论。

因此，不失一般性，假定 $k[x]$ 是域。如果它在 $k$ 上代数，则由代数扩张的已知结果，证明完成。否则，设 $t_1,\ldots,t_r$ 是一个超越基，$r\geqq1$。不失一般性，可以假定 $\varphi$ 在 $k$ 上为恒等映射。每个元素 $x_1,\ldots,x_n$ 都在 $k(t_1,\ldots,t_r)$ 上代数。如果将不可约多项式 $\operatorname{Irr}(x_i,k(t),X)$ 乘以 $k[t]$ 中一个适当的非零元素，就得到一个所有系数都在 $k[t]$ 中的多项式。设 $a_1(t),\ldots,a_n(t)$ 为这些多项式的首项系数，并设 $a(t)$ 为它们的乘积，

$$
a(t)=a_1(t)\cdots a_n(t).
$$

因为 $a(t)\ne0$，存在元素 $t'_1,\ldots,t'_r\in k^a$，使得 $a(t')\ne0$，因而对任意 $i$ 都有 $a_i(t')\ne0$。每个 $x_i$ 都在环

$$
k\left[t_1,\ldots,t_r,\frac{1}{a_1(t)},\ldots,\frac{1}{a_r(t)}\right]
$$

上整。

> **译校注。** 原书中上式最后一个分母印作 $a_r(t)$。由于首项系数的指标为 $1,\ldots,n$，此处应读作 $a_n(t)$；正文保留原印式。

考虑同态

$$
\varphi:k[t_1,\ldots,t_r]\to k^a,
$$

使得 $\varphi$ 在 $k$ 上为恒等映射，且 $\varphi(t_j)=t'_j$。设 $\mathfrak{p}$ 为它的核。则 $a(t)\notin\mathfrak{p}$。

<span class="original-page-anchor" id="pdf-page-392" aria-hidden="true"></span>

我们的同态 $\varphi$ 唯一地延拓到局部环 $k[t]_{\mathfrak{p}}$，并且由前面的说明，利用第 VII 章命题 3.1，它进一步延拓为从

$$
k[t]_{\mathfrak{p}}[x_1,\ldots,x_n]
$$

到 $k^a$ 的同态。这就证明了所要的结论。

**推论 1.2。** *设 $k$ 是域，$k[x_1,\ldots,x_n]$ 是 $k$ 的有限生成扩环。如果 $k[x]$ 是域，则 $k[x]$ 在 $k$ 上代数。*

*证明。* 域的所有同态都是到其像的同构，而存在一个在 $k$ 上的、从 $k[x]$ 到 $k$ 的代数闭包的同态。

**推论 1.3。** *设 $k[x_1,\ldots,x_n]$ 是域 $k$ 上的有限生成整环，$y_1,\ldots,y_m$ 是这个环的非零元素。则存在一个在 $k$ 上的同态*

$$
\psi:k[x]\to k^a,
$$

*使得对所有 $j=1,\ldots,m$ 都有 $\psi(y_j)\ne0$。*

*证明。* 考虑环 $k[x_1,\ldots,x_n,y_1^{-1},\ldots,y_m^{-1}]$，并将定理应用于这个环。

设 $S$ 是 $n$ 个变量的多项式环 $k[X_1,\ldots,X_n]$ 中的一个多项式集合。设 $L$ 是 $k$ 的扩域。所谓 $S$ 在 $L$ 中的一个**零点**，是指 $L$ 中元素组成的 $n$ 元组 $(c_1,\ldots,c_n)$，使得对所有 $f\in S$ 都有

$$
f(c_1,\ldots,c_n)=0.
$$

如果 $S$ 只包含一个多项式 $f$，也称 $(c)$ 为 $f$ 的一个零点。$S$ 的所有零点组成的集合称为 $L$ 中（更准确地说，$L^{(n)}$ 中）的一个**代数集**。设 $\mathfrak{a}$ 是由 $S$ 的所有元素生成的理想。因为 $S\subset\mathfrak{a}$，显然 $\mathfrak{a}$ 的每个零点也都是 $S$ 的零点。不过，逆命题显然也成立，即 $S$ 的每个零点也都是 $\mathfrak{a}$ 的零点，因为 $\mathfrak{a}$ 的每个元素都形如

$$
g_1(X)f_1(X)+\cdots+g_m(X)f_m(X),
$$

其中 $f_j\in S$，$g_i\in k[X]$。因此，考虑集合 $S$ 的零点时，只需考虑一个理想的零点。顺便指出，每个理想都是有限生成的，所以每个代数集都是有限多个多项式的零点集。作为定理 1.1 的另一个推论，我们得到：

**定理 1.4。** *设 $\mathfrak{a}$ 是 $k[X]=k[X_1,\ldots,X_n]$ 中的理想。则或者 $\mathfrak{a}=k[X]$，或者 $\mathfrak{a}$ 在 $k^a$ 中有零点。*

<span class="original-page-anchor" id="pdf-page-393" aria-hidden="true"></span>

*证明。* 假定 $\mathfrak{a}\ne k[X]$。则 $\mathfrak{a}$ 包含于某个极大理想 $\mathfrak{m}$ 中，而 $k[X]/\mathfrak{m}$ 是域，且是 $k$ 的有限生成扩张，因为它由 $X_1,\ldots,X_n$ 模 $\mathfrak{m}$ 的像生成。由推论 2.2，这个域在 $k$ 上代数，因此可以嵌入代数闭包 $k^a$。将模 $\mathfrak{m}$ 的典范映射与这个嵌入复合得到 $k[X]$ 上的同态，它给出所要求的 $\mathfrak{a}$ 的零点，从而完成定理的证明。

> **译校注。** 原书引用“推论 2.2”，此处应为“推论 1.2”；后者说明作为环在 $k$ 上有限生成的域在 $k$ 上代数。

在 §3 中，我们将考虑一族多项式具有公共零点的条件。定理 1.4 表明，如果它们在某个域中有公共零点，那么它们在由其系数在素域上生成的域的代数闭包中也有公共零点。

**定理 1.5（希尔伯特零点定理）。** *设 $\mathfrak{a}$ 是 $k[X]$ 中的理想。设 $f$ 是 $k[X]$ 中的多项式，使得对 $\mathfrak{a}$ 在 $k^a$ 中的每个零点 $(c)=(c_1,\ldots,c_n)$ 都有 $f(c)=0$。则存在整数 $m>0$，使得 $f^m\in\mathfrak{a}$。*

*证明。* 可以假定 $f\ne0$。我们使用 Rabinowitsch 技巧：引入新变量 $Y$，并考虑 $k[X,Y]$ 中由 $\mathfrak{a}$ 和 $1-Yf$ 生成的理想 $\mathfrak{a}'$。由定理 1.4 及当前的假设，理想 $\mathfrak{a}'$ 必须是整个多项式环 $k[X,Y]$，因此存在多项式 $g_i\in k[X,Y]$ 及 $h_i\in\mathfrak{a}$，使得

$$
1=g_0(1-Yf)+g_1h_1+\cdots+g_rh_r.
$$

用 $f^{-1}$ 代替 $Y$，并乘以 $f$ 的适当幂 $f^m$，以消去右边的分母。这就完成了证明。

关于零点定理能做到何种有效程度的问题，可参见下列文献，它们也与本章稍后讨论的消去理论有关。

### 参考文献

[BeY 91] C. Berenstein 和 A. Yger，Effective Bezout identities in $\mathbf{Q}[z_1,\ldots,z_n]$（$\mathbf{Q}[z_1,\ldots,z_n]$ 中的有效贝祖恒等式），*Acta Math.* **166**（1991），第 69–120 页。

[Br 87] D. Brownawell，Bounds for the degree in Nullstellensatz（零点定理中的次数界），*Ann. of Math.* **126**（1987），第 577–592 页。

[Br 88] D. Brownawell，Local diophantine nullstellen inequalities（局部丢番图零点不等式），*J. Amer. Math. Soc.* **1**（1988），第 311–322 页。

[Br 89] D. Brownawell，Applications of Cayley-Chow forms（凯莱–周形式的应用），*Springer Lecture Notes* **1380**：*Number Theory, Ulm 1987*（《数论，乌尔姆 1987》），H. P. Schlickewei 和 E. Wirsing 编，第 1–18 页。

[Ko 88] J. Kollar，Sharp effective nullstellensatz（精确的有效零点定理），*J. Amer. Math. Soc.* **1 第 4 期**（1988），第 963–975 页。

<span class="original-page-anchor" id="pdf-page-394" aria-hidden="true"></span>

## §2. 代数集、代数空间与簇

我们将对代数集作一些非常初等的说明。设 $k$ 是域，$A$ 是某个固定的 $k$ 的代数闭扩域中的代数零点集。所有满足对任意 $(x)\in A$ 都有 $f(x)=0$ 的多项式 $f\in k[X_1,\ldots,X_n]$，显然组成 $k[X]$ 中的一个理想 $\mathfrak{a}$，并且它由 $A$ 确定。我们称它为**属于** $A$ 的理想，或说它是与 $A$ **相伴**的理想。如果 $A$ 是一个多项式集合 $S$ 的零点集，则 $S\subset\mathfrak{a}$，但 $\mathfrak{a}$ 可能比 $S$ 大。另一方面，注意到 $A$ 也是 $\mathfrak{a}$ 的零点集。

设 $A,B$ 是代数集，$\mathfrak{a},\mathfrak{b}$ 是它们的相伴理想。则显然 $A\subset B$ 当且仅当 $\mathfrak{a}\supset\mathfrak{b}$。所以 $A=B$ 当且仅当 $\mathfrak{a}=\mathfrak{b}$。这有一个重要的推论。由于多项式环 $k[X]$ 是诺特环，代数集满足对偶性质，即每个代数集的递降序列

$$
A_1\supset A_2\supset\cdots
$$

都必定对某个整数 $m$ 满足 $A_m=A_{m+1}=\cdots$，即当 $\nu\geqq m$ 时，所有 $A_\nu$ 都相等。此外，将诺特条件的另一个特征性质对偶化，可知每个非空的代数集族都包含一个极小元素。

**定理 2.1。** *代数集的有限并与有限交都是代数集。如果 $A,B$ 分别是理想 $\mathfrak{a},\mathfrak{b}$ 的代数零点集，则 $A\cup B$ 是 $\mathfrak{a}\cap\mathfrak{b}$ 的零点集，而 $A\cap B$ 是 $(\mathfrak{a},\mathfrak{b})$ 的零点集。*

*证明。* 先考虑 $A\cup B$。设 $(x)\in A\cup B$。则 $(x)$ 是 $\mathfrak{a}\cap\mathfrak{b}$ 的零点。反过来，设 $(x)$ 是 $\mathfrak{a}\cap\mathfrak{b}$ 的零点，并假定 $(x)\notin A$。存在一个多项式 $f\in\mathfrak{a}$，使得 $f(x)\ne0$。但是 $\mathfrak{a}\mathfrak{b}\subset\mathfrak{a}\cap\mathfrak{b}$，所以对所有 $g\in\mathfrak{b}$ 都有 $(fg)(x)=0$，从而对所有 $g\in\mathfrak{b}$ 都有 $g(x)=0$。因此 $(x)$ 属于 $B$，而 $A\cup B$ 是 $\mathfrak{a}\cap\mathfrak{b}$ 的代数零点集。

为证明 $A\cap B$ 是代数集，设 $(x)\in A\cap B$。则 $(x)$ 是 $(\mathfrak{a},\mathfrak{b})$ 的零点。反过来，设 $(x)$ 是 $(\mathfrak{a},\mathfrak{b})$ 的零点。则显然 $(x)\in A\cap B$，如所要求。定理得证。

如果代数集 $V$ 不能表示成代数集 $A,B$ 的并 $V=A\cup B$，其中 $A,B$ 均不等于 $V$，就称 $V$ 是 **$k$-不可约**的。我们也用“不可约”来代替“$k$-不可约”。

**定理 2.2。** *设 $A$ 是代数集。*

(i) *则 $A$ 可以表示为有限个不可约代数集的并 $A=V_1\cup\cdots\cup V_r$。*

(ii) *如果各 $V_i$ 之间没有包含关系，即当 $i\ne j$ 时 $V_i\not\subset V_j$，则这种表示唯一。*

<span class="original-page-anchor" id="pdf-page-395" aria-hidden="true"></span>

(iii) *设 $W,V_1,\ldots,V_r$ 是不可约代数集，且*

$$
W\subset V_1\cup\cdots\cup V_r.
$$

*则对某个 $i$ 有 $W\subset V_i$。*

*证明。* 先证明存在性。假定不能表示为有限个不可约代数集的并的代数集族非空。取其中的一个极小元素 $V$。则 $V$ 不可能不可约，因而可写成 $V=A\cup B$，其中 $A,B$ 是代数集，但 $A\ne V$ 且 $B\ne V$。由于 $A,B$ 各自都严格小于 $V$，可以将 $A,B$ 表示为有限个不可约代数集的并，从而得到 $V$ 的这种表示，矛盾。

唯一性将由 (iii) 推出，我们接着证明 (iii)。设 $W$ 包含于并集 $V_1\cup\cdots\cup V_r$ 中。则

$$
W=(W\cap V_1)\cup\cdots\cup(W\cap V_r).
$$

由于每个 $W\cap V_i$ 都是代数集，由 $W$ 的不可约性，必定对某个 $i$ 有 $W=W\cap V_i$。因此对某个 $i$ 有 $W\subset V_i$，从而证明了 (iii)。

现在为证明 (ii)，对每个 $W_j$ 应用 (iii)。则对每个 $j$，存在某个 $i$ 使得 $W_j\subset V_i$。类似地，对每个 $i$，存在 $\nu$ 使得 $V_i\subset W_\nu$。由于各 $W_j$ 之间没有包含关系，必定有 $W_j=V_i=W_\nu$。这表明每个 $W_j$ 都出现在各 $V_i$ 中，每个 $V_i$ 都出现在各 $W_j$ 中，从而证明了表示的唯一性。这也完成了定理 2.2 的证明。

**定理 2.3。** *代数集不可约，当且仅当其相伴理想是素理想。*

*证明。* 设 $V$ 不可约，$\mathfrak{p}$ 是它的相伴理想。如果 $\mathfrak{p}$ 不是素理想，就可以找到两个多项式 $f,g\in k[X]$，使得 $f\notin\mathfrak{p}$，$g\notin\mathfrak{p}$，但 $fg\in\mathfrak{p}$。令 $\mathfrak{a}=(\mathfrak{p},f)$，$\mathfrak{b}=(\mathfrak{p},g)$。设 $A$ 为 $\mathfrak{a}$ 的代数零点集，$B$ 为 $\mathfrak{b}$ 的代数零点集。则 $A\subset V$，$A\ne V$，且 $B\subset V$，$B\ne V$。此外，$A\cup B=V$。事实上，显然 $A\cup B\subset V$。反过来，设 $(x)\in V$。则由 $(fg)(x)=0$ 得到 $f(x)=0$ 或 $g(x)=0$。所以 $(x)\in A$ 或 $(x)\in B$，从而 $V=A\cup B$，$V$ 不是不可约的。反过来，设 $V$ 是素理想 $\mathfrak{p}$ 的代数零点集。假定 $V=A\cup B$，其中 $A\ne V$ 且 $B\ne V$。设 $\mathfrak{a},\mathfrak{b}$ 分别为 $A,B$ 的相伴理想。存在多项式 $f\in\mathfrak{a}$，$f\notin\mathfrak{p}$，以及 $g\in\mathfrak{b}$，$g\notin\mathfrak{p}$。但 $fg$ 在 $A\cup B$ 上恒为零，因而属于 $\mathfrak{p}$，矛盾，从而定理得证。

**警告。** 给定域 $k$ 及 $k[X]$ 中的素理想 $\mathfrak{p}$，由 $\mathfrak{p}$ 在 $k^a[X]$ 中生成的理想可能不是素理想，而由 $\mathfrak{p}k^a[X]$ 在 $k^a$ 上定义的代数集可能有不止一个分支，因而并非不可约。因此，指明 $k$ 的前缀确实是必要的。

如下推广代数集的术语也很有用。给定理想 $\mathfrak{a}\subset k[X]$，对每个包含 $k$ 的域 $K$，都可以将 $\mathfrak{a}$ 对应于集合<span class="original-page-anchor" id="pdf-page-396" aria-hidden="true"></span>$\mathcal{L}_{\mathfrak{a}}(K)$，它由 $\mathfrak{a}$ 在 $K$ 中的零点组成。因此 $\mathcal{L}_{\mathfrak{a}}$ 是一种对应

$$
\mathcal{L}_{\mathfrak{a}}:K\mapsto\mathcal{L}_{\mathfrak{a}}(K)\subset K^{(n)}.
$$

我们称 $\mathcal{L}_{\mathfrak{a}}$ 本身为一个**代数空间**，所以 $\mathcal{L}_{\mathfrak{a}}$ 不是一个集合，而是将每个域 $K$ 对应于集合 $\mathcal{L}_{\mathfrak{a}}(K)$。因此，$\mathcal{L}_{\mathfrak{a}}$ 是从 $k$ 的扩域 $K$ 到集合的函子（关于域同构具有函子性）。所谓 **$k$-簇**，是指与素理想 $\mathfrak{p}$ 相伴的代数空间。

相伴理想的概念也适用于这样的 $\mathcal{L}_{\mathfrak{a}}$，且 $\mathcal{L}_{\mathfrak{a}}$ 的相伴理想也为 $\operatorname{rad}(\mathfrak{a})$。我们将省略下标 $\mathfrak{a}$，只用 $\mathcal{L}$ 表示这个推广后的代数空间概念。当然，有

$$
\mathcal{L}_{\mathfrak{a}}=\mathcal{L}_{\operatorname{rad}(\mathfrak{a})}.
$$

我们称 $\mathcal{L}_{\mathfrak{a}}(K)$ 为 **$\mathcal{L}_{\mathfrak{a}}$ 在 $K$ 中的点**组成的集合。由希尔伯特零点定理，即定理 1.1 可知，如果 $K\subset K'$ 是两个包含 $k$ 的代数闭域，那么与 $\mathcal{L}_{\mathfrak{a}}(K)$ 和 $\mathcal{L}_{\mathfrak{a}}(K')$ 相伴的理想彼此相等，也等于 $\operatorname{rad}(\mathfrak{a})$。因此，包含 $k$ 的最小代数闭域 $k^a$ 已经确定了这些理想。不过，正如我们将看到的，考虑含有超越元素的更大的域也很有用。

再举一个例子，考虑多项式环 $k[X_1,\ldots,X_n]=k[X]$。用 $\mathbf{A}^n$ 表示与零理想相伴的代数空间。则 $\mathbf{A}^n$ 称为**仿射 $n$ 维空间**。设 $K$ 是包含 $k$ 的域。每个 $n$ 元组 $(c_1,\ldots,c_n)\in K^{(n)}$ 都给出一个同态

$$
\varphi:k[X_1,\ldots,X_n]\to K,
$$

使得对所有 $i$ 都有 $\varphi(X_i)=c_i$。因此，$\mathbf{A}^n(K)$ 中的点与从 $k(X)$ 到 $K$ 的同态一一对应。

> **译校注。** 原书在上一句印作 $k(X)$。刚刚定义的同态以多项式环 $k[X]$ 为定义域，所以此处应读作 $k[X]$。

更一般地，设 $V$ 是 $k$-簇，相伴的素理想为 $\mathfrak{p}$。则 $k[X]/\mathfrak{p}$ 是整环。用 $\xi_i$ 表示 $X_i$ 在典范同态 $k[X]\to k[X]/\mathfrak{p}$ 下的像。我们称 $(\xi)$ 为 $V$ 在 $k$ 上的**泛点**。另一方面，设 $(x)$ 是 $V$ 在某个域 $K$ 中的点。则 $\mathfrak{p}$ 在 $(x)$ 上消失，所以将 $X_i\mapsto x_i$ 的同态 $\varphi:k[X]\to k[x]$ 通过 $k[X]/\mathfrak{p}=k[\xi]$ 分解，从而得到自然同态 $k[\xi]\to k[x]$。如果这个同态是同构，就称 $(x)$ 为 $V$ 在 $K$ 中的**一个泛点**。

给定两点 $(x)\in\mathbf{A}^n(K)$ 和 $(x')\in\mathbf{A}^n(K')$，如果映射 $x_i\mapsto x'_i$ 由同态 $k[x]\to k[x']$ 诱导，就说 $(x')$ 是 $(x)$ 的一个（在 $k$ 上的）**特化**。由簇的泛点的定义，立即可知：

*簇 $V$ 是其泛点，或其一个泛点的所有特化组成的集合。*

换句话说，对每个包含 $k$ 的域 $K$，$V(K)$ 都是 $(\xi)$ 在 $K$ 中的特化组成的集合。

现在考察代数集的反向构造。设 $(x)=(x_1,\ldots,x_n)$ 是一个 $n$ 元组，其坐标 $x_i\in K$，其中 $K$ 是 $k$ 的某个扩域。设 $\mathfrak{p}$ 是 $k[X]$ 中由所有满足下述条件的多项式 $f(X)$ 组成的理想：

<span class="original-page-anchor" id="pdf-page-397" aria-hidden="true"></span>

$f(x)=0$。我们称 $\mathfrak{p}$ 为在 $(x)$ 上**消失**的理想。则 $\mathfrak{p}$ 是素理想，因为如果 $fg\in\mathfrak{p}$，所以 $f(x)g(x)=0$，那么由于 $K$ 没有零因子，$f\in\mathfrak{p}$ 或 $g\in\mathfrak{p}$。因此 $\mathcal{L}_{\mathfrak{p}}$ 是一个 $k$-簇 $V$，而 $(x)$ 是 $V$ 在 $k$ 上的一个泛点，因为 $k[X]/\mathfrak{p}\approx k[x]$。

为便于以后使用，我们对唯一分解整环上的多项式环，而不是域上的多项式环，陈述下一个结果。

**定理 2.4。** *设 $R$ 是唯一分解整环，$W_1,\ldots,W_m$ 是其分式域 $k$ 上的 $m$ 个独立变量。设 $k(w_1,\ldots,w_m)$ 是超越次数为 $m-1$ 的扩张。则 $R[W]$ 中在 $(w)$ 上消失的理想是主理想。*

*证明。* 由假设，存在某个次数 $\geqq1$ 的多项式 $P(W)\in R[W]$ 在 $(w)$ 上消失。取一个不可约因子后，可以假定这个多项式不可约，因此它是唯一分解整环 $R[W]$ 中的素元。设 $G(W)\in R[W]$ 在 $(w)$ 上消失。为证明 $P$ 整除 $G$，必要时选取 $G$ 的某个在 $(w)$ 上消失的不可约因子后，可以不失一般性地假定 $G$ 是 $R[W]$ 中的素元。某个变量 $W_i$ 出现在 $P(W)$ 中，设为 $W_m$，因而 $w_m$ 在 $k(w_1,\ldots,w_{m-1})$ 上代数。于是 $(w_1,\ldots,w_{m-1})$ 代数独立，因此 $W_m$ 也出现在 $G$ 中。此外，由第 IV 章定理 2.3 中的高斯引理，$P(w_1,\ldots,w_{m-1},W_m)$ 作为 $k(w_1,\ldots,w_{m-1})[W_m]$ 中的多项式不可约。因此存在多项式 $H(W_m)\in k(w_1,\ldots,w_{m-1})[W_m]$，使得

$$
G(W)=H(W_m)P(W).
$$

令 $R'=R[w_1,\ldots,w_{m-1}]$。则 $P,G$ 作为 $R'[W_m]$ 中的多项式都具有容度 $1$。由第 IV 章推论 2.2 可知 $H\in R'[W_m]\approx R[W]$，这就证明了定理 2.4。

接着考虑齐次理想和射影空间。多项式 $f(X)\in k[X]$ 可以写成线性组合

$$
f(X)=\sum c_{(\nu)}M_{(\nu)}(X),
$$

其中单项式 $M_{(\nu)}(X)=X_1^{\nu_1}\cdots X_n^{\nu_n}$，且 $c_{(\nu)}\in k$。将 $M_{(\nu)}$ 的**次数**记为

$$
|\nu|=\deg M_{(\nu)}=\sum\nu_i.
$$

如果在 $f$ 的这个表示中，所有单项式 $X^{(\nu)}$ 的次数都相同（只考虑系数 $c_{(\nu)}\ne0$ 的项），则称 $f$ 为一个**型**，或者说 $f$ 是（该次数的）**齐次**多项式。$K[X]$ 中任意的多项式 $f(X)$ 也可以写成

$$
f(X)=\sum f^{(d)}(X),
$$

其中每个 $f^{(d)}$ 都是一个 $d$ 次型（$d$ 可以为 $0$）。称 $f^{(d)}$ 为 $f$ 的 $d$ 次**齐次部分**。

如果只要 $f\in\mathfrak{a}$，其每个齐次部分 $f^{(d)}$ 也都属于 $\mathfrak{a}$，就称 $k[X]$ 的理想 $\mathfrak{a}$ 为**齐次**理想。

<span class="original-page-anchor" id="pdf-page-398" aria-hidden="true"></span>

**命题 2.5。** *理想 $\mathfrak{a}$ 齐次，当且仅当 $\mathfrak{a}$ 有一个由型组成的、在 $k[X]$ 上的生成元集。*

*证明。* 假定 $\mathfrak{a}$ 齐次，且 $f_1,\ldots,f_r$ 是生成元。由假设，对每个整数 $d\geqq0$，齐次分量 $f_i^{(d)}$ 也都属于 $\mathfrak{a}$，而所有这样的 $f_i^{(d)}$（遍历所有 $i,d$）构成一个齐次生成元集。反过来，设 $f$ 是 $\mathfrak{a}$ 中的齐次元素，$g\in K[X]$ 任意。对每个 $d$，$g^{(d)}f$ 属于 $\mathfrak{a}$，且 $g^{(d)}f$ 齐次，所以 $gf$ 的所有齐次分量也都属于 $\mathfrak{a}$。当 $f$ 遍历 $\mathfrak{a}$ 的一个齐次生成元集时应用这个说明，可知 $\mathfrak{a}$ 齐次，从而完成命题的证明。

如果对每个点 $(x)\in\mathcal{L}$ 以及在 $k(x)$ 上超越的 $t$，点 $(tx)$ 也都属于 $\mathcal{L}$，就称代数空间 $\mathcal{L}$ 为**齐次**的。如果 $t,u$ 都在 $k(x)$ 上超越，则存在同构

$$
k[x,t]\xrightarrow{\approx}k[x,u],
$$

它将 $t$ 映到 $u$，并且在 $k[x]$ 上限制为恒等映射，因此为验证上述条件，只需对某个在 $k(x)$ 上超越的 $t$ 验证它。

**命题 2.6。** *代数空间 $\mathcal{L}$ 齐次，当且仅当其相伴理想 $\mathfrak{a}$ 齐次。*

*证明。* 假定 $\mathcal{L}$ 齐次。设 $f(X)\in k[X]$ 在 $\mathcal{L}$ 上消失。对每个 $(x)\in\mathcal{L}$ 以及在 $k(x)$ 上超越的 $t$，有

$$
0=f(x)=f(tx)=\sum_d t^df^{(d)}(x).
$$

所以对所有 $d$ 都有 $f^{(d)}(x)=0$，从而对所有 $d$ 都有 $f^{(d)}\in\mathfrak{a}$。因此 $\mathfrak{a}$ 齐次。反过来，假定 $\mathfrak{a}$ 齐次。由希尔伯特零点定理，知道 $\mathcal{L}$ 由 $\mathfrak{a}$ 的零点组成，因而由 $\mathfrak{a}$ 的一组齐次生成元的零点组成。但是，如果 $f$ 是其中一个 $d$ 次齐次生成元，$(x)$ 是 $\mathcal{L}$ 中的点，那么对在 $k(x)$ 上超越的 $t$，有

$$
0=f(x)=t^df(x)=f(tx),
$$

所以 $(tx)$ 也是 $\mathfrak{a}$ 的零点。因此 $\mathcal{L}$ 齐次，从而命题得证。

**命题 2.7。** *设 $\mathcal{L}$ 是齐次代数空间。则 $\mathcal{L}$ 的每个不可约分支 $V$ 也都齐次。*

*证明。* 设 $V=V_1,\ldots,V_r$ 是 $\mathcal{L}$ 的不可约分支，彼此之间没有包含关系。由注 3.3，知道 $V_1\not\subset V_2\cup\cdots\cup V_r$，所以存在点 $(x)\in V_1$，使得对 $i=2,\ldots,r$ 都有 $(x)\notin V_i$。由假设，对在 $k(x)$ 上超越的 $t$，有 $(tx)\in\mathcal{L}$，所以对某个 $i$ 有 $(tx)\in V_i$。特化到 $t=1$，可知 $(x)\in V_i$，所以 $i=1$，这证明了 $V_1$ 齐次，如所要求。

> **译校注。** 原书引用“注 3.3”。这里使用的是定理 2.2(iii) 已证明的包含性质：不可约集若包含于有限个代数集的并中，则包含于其中一个代数集。

设 $V$ 是由 $k[X]$ 中的素理想 $\mathfrak{p}$ 在 $k$ 上定义的簇。设 $(x)$ 是 $V$ 在 $k$ 上的泛点。如果对于 $t$<span class="original-page-anchor" id="pdf-page-399" aria-hidden="true"></span>在 $k(x)$ 上超越时，点 $(tx)$ 也是 $V$ 的一个点，换句话说，$(tx)$ 是 $(x)$ 的一个特化，就称 $(x)$ **在 $k$ 上齐次**。在这种情形下，有同构

$$
k[x_1,\ldots,x_n]\approx k[tx_1,\ldots,tx_n],
$$

它在 $k$ 上为恒等映射，并将 $x_i$ 映到 $tx_i$。于是由前面的命题可知，对 $k$ 上的簇 $V$，下列条件等价：

*$V$ 齐次。*

*$V$ 在 $k[X]$ 中的素理想齐次。*

*$V$ 在 $k$ 上的一个泛点齐次。*

齐次理想总有一个零点，即原点 $(0)$，称为**平凡零点**。我们想知道齐次代数集何时在某个代数闭域中有非平凡零点。为此，如下引入射影空间的术语。设 $(x)$ 是 $\mathbf{A}^n$ 中的某个点，$\lambda$ 是某个包含 $k(x)$ 的域中的元素。用 $(\lambda x)$ 表示点 $(\lambda x_1,\ldots,\lambda x_n)$。对某个域 $K$，如果两点 $(x),(y)\in\mathbf{A}^n(K)$ 的坐标不全为 $0$，并且存在某个元素 $\lambda\in K$，$\lambda\ne0$，使得 $(\lambda x)=(y)$，就称这两点等价。$\mathbf{A}^n(K)$ 中这样的点的等价类称为 $K$ 中的**射影空间**的点。将这个射影空间记为 $\mathbf{P}^{n-1}$，将其在 $K$ 中的点集记为 $\mathbf{P}^{n-1}(K)$。我们将**射影空间中的代数空间**定义为齐次理想的非平凡零点所组成的空间，其中相差一个公共非零因子的两个零点被视为同一点。

### 环上的代数空间

正如下一节将看到的，只考察某个域 $k$ 的 $k[X]$ 中的理想是不够的。出于多种原因，有时，甚至常常需要处理整数 $\mathbf{Z}$ 上的多项式方程。在后面几节的例子中，我们将找到关于一组型的系数的、在 $\mathbf{Z}$ 上的泛条件，使得这些型具有非平凡公共零点。此外，在数论的丢番图问题中，需要考虑具有整数系数的方程组，并确定这些方程在整数或有理数中的解，或者确定对某个素数 $p$ 模 $p$ 约化后得到的解。因此，我们自然要如下推广代数空间和簇的概念。尽管下一节的应用是在 $\mathbf{Z}$ 上的，现在我们仍将对任意交换环 $R$ 给出一般定义。

设 $f(X)\in R[X]=R[X_1,\ldots,X_n]$ 是系数在 $R$ 中的多项式。设 $R\to A$ 是一个 $R$-代数，在本章其余部分中，这意味着一个交换环同态。在多项式环上得到相应的同态

$$
R[X]\to A[X],
$$

记为 $f\mapsto f_A$，其中 $f_A$ 的系数是 $f$ 的系数在同态 $R\to A$ 下的像。所谓 $f$ 在 $A$ 中的**零点**，是指 $f_A$ 在 $A$ 中的零点。类似地，设 $S$ 是 $R[X]$ 中的一个多项式集合。所谓 $S$ 在 $A$ 中的**零点**，是指所有多项式 $f\in S$ 在 $A$ 中的公共零点。设 $\mathfrak{a}$ 是 $S$ 在 $R[X]$ 中生成的理想。则 $S$ 在 $A$ 中的零点也都是<span class="original-page-anchor" id="pdf-page-400" aria-hidden="true"></span>$\mathfrak{a}$ 在 $A$ 中的零点。将 $S$ 在 $A$ 中的零点集记为 $\mathcal{L}_S(A)$，于是有

$$
\mathcal{L}_S(A)=\mathcal{L}_{\mathfrak{a}}(A).
$$

我们称 $\mathcal{L}_{\mathfrak{a}}(A)$ 为 $R$ 上的**代数集**。因此有一种对应

$$
\mathcal{L}_{\mathfrak{a}}:A\mapsto\mathcal{L}_{\mathfrak{a}}(A),
$$

它将每个 $R$-代数对应于 $\mathfrak{a}$ 在这个代数中的零点集。注意到 $R$-代数构成一个范畴，其中态射是使下图交换的环同态 $\varphi:A\to A'$：

$$
\begin{array}{ccc}
&&A\\
R&\nearrow&\downarrow\varphi\\
&\searrow&A'
\end{array}
$$

于是可以立即验证，$\mathcal{L}_{\mathfrak{a}}$ 是从 $R$-代数范畴到集合范畴的函子。我们仍称 $\mathcal{L}_{\mathfrak{a}}$ 为 $R$ 上的**代数空间**。

如果 $R$ 是诺特环，则 $R[X]$ 也是诺特环（第 IV 章定理 4.1），因此对于理想 $\mathfrak{a}$，总存在有限个多项式组成的集合 $S$ 生成这个理想，所以 $\mathcal{L}_S=\mathcal{L}_{\mathfrak{a}}$。

$\mathfrak{a}$ 的**根理想**仍定义为所有满足对某个正整数 $N$ 有 $h^N\in\mathfrak{a}$ 的多项式 $h\in R[X]$ 组成的集合。于是下述断言立即成立：

*假定 $R$ 是整环。则对每个 $R$-代数 $R\to K$，其中 $K$ 是域，都有*

$$
\mathcal{L}_{\mathfrak{a}}(K)=\mathcal{L}_{\operatorname{rad}(\mathfrak{a})}(K).
$$

我们可以定义 $R$ 上的**仿射空间** $\mathbf{A}^n$。其点由所有 $n$ 元组 $(x_1,\ldots,x_n)=(x)$ 组成，其中 $x_i$ 属于某个 $R$-代数 $A$。因此 $\mathbf{A}^n$ 仍是一种对应

$$
A\mapsto\mathbf{A}^n(A),
$$

从 $R$-代数对应到点集。这些点与从 $R$ 上的多项式环到 $A$ 的同态

$$
R[X]\to A
$$

一一对应。下一节中，我们将限于 $A=K$ 为域的情形，并且只考虑对域 $K$ 的函子 $K\mapsto\mathbf{A}^n(K)$。此外，我们尤其将处理 $R=\mathbf{Z}$ 的情形，此时 $\mathbf{Z}$ 到域 $K$ 有唯一的同态。因此，一个域 $K$ 总可以视为一个 $\mathbf{Z}$-代数。

最后，为简单起见，假定 $R$ 是整环。我们也可以考虑 $R$ 上的射影空间。设 $\mathfrak{a}$ 是 $R[X]$ 中的理想。如前一样定义 $\mathfrak{a}$ 为齐次的。于是 $R[X]$ 中的齐次理想可以看作对每个域 $K$（作为一个 $R$-代数）在射影空间 $\mathbf{P}^n(K)$ 中定义一个代数子集。如果 $R=\mathbf{Z}$，<span class="original-page-anchor" id="pdf-page-401" aria-hidden="true"></span>则 $\mathfrak{a}$ 对每个域 $K$ 都在 $\mathbf{P}^n(K)$ 中定义一个代数子集。类似地，可以定义 $R$ 上的齐次代数空间 $\mathcal{L}$ 的概念，在整数 $\mathbf{Z}$ 上当然更可以如此定义。将 $\mathcal{L}=\mathcal{L}_{\mathfrak{a}}$ 看作从域 $K$ 到集合 $\mathbf{P}^n(K)$ 的函子，命题 2.6、2.7 及其证明在这个更一般的情形中也成立。

如果 $\mathfrak{a}$ 是素理想 $\mathfrak{p}$，就称 $\mathcal{L}_{\mathfrak{p}}$ 为一个 **$R$-簇** $V$。如果 $R$ 是诺特环，因而 $R[X]$ 也是诺特环，就如前一样可知，$R$ 上的代数空间 $\mathcal{L}$ 是有限个没有包含关系的 $R$-簇的并。我们将在 §5 中，在交换环的十分一般的背景下完成这一论证。如同在域上所做的，可以形成商环 $\mathbf{Z}[X]/\mathfrak{p}$，并称 $(X)$ 在这个商环中的像 $(x)$ 为 $V$ 的一个**泛点**。

## §3. 投影与消去

设 $(W)=(W_1,\ldots,W_m)$ 和 $(X)=(X_1,\ldots,X_n)$ 是两组独立变量。则 $k[W,X]$ 中的理想在乘积空间 $\mathbf{A}^{m+n}$ 中定义代数空间。设 $\mathfrak{a}$ 是 $k[W,X]$ 中的理想。令 $\mathfrak{a}_1=\mathfrak{a}\cap k[W]$。设 $\mathcal{L}$ 为 $\mathfrak{a}$ 的代数零点空间，$\mathcal{L}_1$ 为 $\mathfrak{a}_1$ 的代数零点空间。有投影

$$
\operatorname{pr}:\mathcal{L}^{m+n}\to\mathcal{L}^m\quad\text{或}\quad\operatorname{pr}:\mathbf{A}^{m+n}\to\mathbf{A}^m,
$$

它将点 $(w,x)$ 映到其第一组坐标 $(w)$。显然 $\operatorname{pr}\mathcal{L}\subset\mathcal{L}_1$。一般来说，$\operatorname{pr}\mathcal{L}=\mathcal{L}_1$ 并不成立。例如，由单个多项式 $W_1^2-W_2X_1=0$ 生成的理想 $\mathfrak{p}$ 是素理想。它与 $k[W_1,W_2]$ 的交为零理想。但是，仿射 $(W_1,W_2)$-空间中的每个点并不都是簇 $\mathcal{L}_{\mathfrak{p}}$ 中某个点的投影。例如，点 $(1,0)$ 不是 $\mathfrak{p}$ 的任何零点的投影。这种情形称为投影**不完全**。现在我们将考虑不会出现这种现象的一种情形。

首先，设 $\mathfrak{p}$ 是 $k[W,X]$ 中的素理想，$V$ 是它的零点簇。设 $(w,x)$ 是 $V$ 的一个泛点。令 $\mathfrak{p}_1=\mathfrak{p}\cap k[W]$。则 $(w)$ 是簇 $V_1$ 的一个泛点，其中 $V_1$ 是 $\mathfrak{p}_1$ 的代数零点空间。这由典范单射同态

$$
k[W]/\mathfrak{p}_1\to k[W,X]/\mathfrak{p}
$$

立即得出。因此，$V_1$ 的泛点 $(w)$ 是 $V$ 的泛点 $(w,x)$ 的投影。问题在于，$V_1$ 的一个特殊点 $(w')$ 是否是 $V$ 中某个点的投影。

在后面的应用中，我们将考虑只关于 $X$ 变量齐次的理想，以及类似地考虑在 $\mathbf{A}^n$ 中关于第二组变量齐次的代数子集。

<span class="original-page-anchor" id="pdf-page-402" aria-hidden="true"></span>

$k[W,X]$ 中关于 $(X)$ 齐次的理想 $\mathfrak{a}$，在 $\mathbf{A}^m\times\mathbf{P}^{n-1}$ 中定义一个代数空间。如果 $V$ 是由 $\mathfrak{a}$ 定义的代数集的一个不可约分支，则可以将 $V$ 视为 $\mathbf{A}^m\times\mathbf{P}^{n-1}$ 的一个子簇。设 $\mathfrak{p}$ 为与 $V$ 相伴的素理想。则 $\mathfrak{p}$ 关于 $(X)$ 齐次。令 $\mathfrak{p}_1=\mathfrak{p}\cap k[W]$。我们将看到，在处理射影空间时，前面所说的投影不完全的情形会被消除。

也可以考虑由 $\mathbf{Z}$ 上的零理想定义的乘积 $\mathbf{A}^m\times\mathbf{P}^n$。对每个域 $K$，$\mathbf{A}^m\times\mathbf{P}^n$ 在 $K$ 中的点集为 $\mathbf{A}^m(K)\times\mathbf{P}^n(K)$。$\mathbf{Z}[W,X]$ 中关于 $(X)$ 齐次的理想 $\mathfrak{a}$，在 $\mathbf{A}^m\times\mathbf{P}^n$ 中定义代数空间 $\mathcal{L}=\mathcal{L}_{\mathfrak{a}}$。可以形成它在第一个因子上的投影 $\mathcal{L}_1$。这尤其适用于 $\mathfrak{a}$ 是素理想 $\mathfrak{p}$ 的情形，此时称 $\mathcal{L}_{\mathfrak{a}}$ 为 $\mathbf{A}^m\times\mathbf{P}^n$ 的一个**算术子簇**。其投影 $V_1$ 是 $\mathbf{A}^m$ 的一个算术子簇，与素理想 $\mathfrak{p}_1=\mathfrak{p}\cap\mathbf{Z}[W]$ 相伴。

**定理 3.1。** *设 $(W)=(W_1,\ldots,W_m)$ 和 $(X)=(X_1,\ldots,X_n)$ 是两族独立变量。设 $\mathfrak{p}$ 是 $k[W,X]$（相应地，$\mathbf{Z}[W,X]$）中的素理想，并假定 $\mathfrak{p}$ 关于 $(X)$ 齐次。设 $V$ 是 $\mathbf{A}^m\times\mathbf{P}^{n-1}$ 中相应的不可约代数空间。令 $\mathfrak{p}_1=\mathfrak{p}\cap k[W]$（相应地，$\mathfrak{p}\cap\mathbf{Z}[W]$），并设 $V_1$ 是 $V$ 在第一个因子上的投影。则 $V_1$ 是 $\mathfrak{p}_1$ 在 $\mathbf{A}^m$ 中的代数零点空间。*

*证明。* 设 $V$ 的泛点为 $(w,x)$。需要证明：$\mathfrak{p}_1$ 在一个域中的每个零点 $(w')$，都是 $\mathfrak{p}$ 的某个零点 $(w',x')$ 的投影，且 $(x')$ 的坐标不全等于 $0$。由假设，$(x)$ 的坐标不全等于 $0$，因为我们将 $V$ 视为 $\mathbf{A}^m\times\mathbf{P}^{n-1}$ 的子集。为明确起见，设我们处理的是域 $k$ 的情形。由第 VII 章命题 3.3，同态 $k[w]\to k[w']$ 可以延拓为 $k(w,x)$ 的一个位 $\varphi$。由第 VII 章命题 3.4，存在某个坐标 $x_j$，使得对所有 $i=1,\ldots,n$ 都有 $\varphi(x_i/x_j)\ne\infty$。对所有 $i$ 令 $x'_i=\varphi(x_i/x_j)$，即完成证明。处理 $\mathbf{Z}$ 上的代数空间时，只需将 $k$ 替换为 $\mathbf{Z}$，证明类似。

**注。** 给定点 $(w')\in\mathbf{A}^m$，$\mathbf{A}^m\times\mathbf{P}^{n-1}$ 中的点 $(w',x')$ 当然可能不在 $k(w')$ 中。坐标 $(x')$ 甚至可能在 $k(x')$ 上超越。不过，由希尔伯特零点定理的任意一种形式，例如定理 1.1 的推论 1.3，确实知道可以找到在 $k(w')$ 上代数的 $(x')$。根据零点定理的各种版本，如果一组型在某个域中有非平凡公共零点，就在由这些型的系数在素域上生成的域的代数闭包中有非平凡公共零点。因此，在如下文定理 1.2 这样的定理中，使这些型具有非平凡公共零点（或射影空间中的零点）的系数条件，也正是使它们在该代数闭包中有这种零点的条件。

> **译校注。** 原书印作“在 $k(x')$ 上超越”；由于坐标 $x'_i$ 本来就在 $k(x')$ 中，此处讨论的底域应为 $k(w')$。原书的“下文定理 1.2”指下一页的定理 3.2。

我们将应用定理 3.1 来说明：给定有限个齐次多项式，它们在某个<span class="original-page-anchor" id="pdf-page-403" aria-hidden="true"></span>代数闭域中有非平凡公共零点这一性质，可以用关于它们系数的有限个泛多项式方程表达。下面将其表述得更精确。

考虑有限个型 $(f)=(f_1,\ldots,f_r)$。设 $d_1,\ldots,d_r$ 为它们的次数。*假定对 $i=1,\ldots,r$ 都有 $d_i\geqq1$。* 每个 $f_i$ 可写成

$$
\tag{1}f_i=\sum w_{i,(\nu)}M_{(\nu)}(X),
$$

其中 $M_{(\nu)}(X)$ 是 $(X)$ 的一个 $d_i$ 次单项式，$w_{i,(\nu)}$ 是一个系数。如果 $(x)\ne(0)$ 且对所有 $i$ 都有 $f_i(x)=0$，就说 $(f)$ 有一个**非平凡零点** $(x)$。将这些型的系数 $w_{i,(\nu)}$ 按照某种确定的顺序排列所得到的点记为 $(w)=(w)_f$，并将它视为某个仿射空间 $\mathbf{A}^m$ 中的点，其中 $m$ 是这些系数的数目。整数 $m$ 由给定的次数 $d_1,\ldots,d_r$ 确定。换句话说，给定这些次数后，具有这些次数的所有型组 $(f)=(f_1,\ldots,f_r)$ 与 $\mathbf{A}^m$ 中的点一一对应。

**定理 3.2（消去理论基本定理）。** *给定次数 $d_1,\ldots,d_r$，所有具有非平凡公共零点的 $n$ 元型组 $(f_1,\ldots,f_r)$，组成 $\mathbf{Z}$ 上的 $\mathbf{A}^m$ 的一个代数子空间。*

*证明。* 设 $(W)=(W_{i,(\nu)})$ 是独立于 $(X)$ 的一族变量。设 $(F)=(F_1,\ldots,F_r)$ 是 $\mathbf{Z}[W,X]$ 中由下式给出的多项式族：

$$
\tag{2}F_i(W,X)=\sum W_{i,(\nu)}M_{(\nu)}(X),
$$

其中 $M_{(\nu)}(X)$ 遍历 $(X)$ 的所有 $d_i$ 次单项式，所以 $(W)=(W)_F$。称 $F_1,\ldots,F_r$ 为**泛型**。令

$$
\mathfrak{a}=\mathbf{Z}[W,X]\text{ 中由 }F_1,\ldots,F_r\text{ 生成的理想}.
$$

则 $\mathfrak{a}$ 关于 $(X)$ 齐次。因此，我们处于定理 3.1 的情形，其中 $\mathfrak{a}$ 在 $\mathbf{A}^m\times\mathbf{P}^{n-1}$ 中定义一个代数空间 $\mathfrak{A}$。注意，$(w)$ 是 $(W)$ 的一个特化，或者也可以说，$(f)$ 是 $(F)$ 的一个特化。如定理 3.1 中那样，设 $\mathfrak{A}_1$ 为 $\mathfrak{A}$ 在第一个因子上的投影。于是直接由定义，$(f)$ 有非平凡零点，当且仅当 $(w)_f$ 属于 $\mathfrak{A}_1$，所以定理 3.2 是定理 3.1 的一个特殊情形。

**推论 3.3。** *设 $(f)$ 是 $n$ 个变量中的 $n$ 个型组成的族，并假定 $(w)_f$ 是 $\mathbf{A}^m$ 的一个泛点，即这些型的系数代数独立。则 $(f)$ 没有非平凡零点。*

*证明。* 存在一个只有平凡零点的 $(f)$ 的特化，即 $f'_1=X_1^{d_1},\ldots,f'_n=X_n^{d_n}$。

接着，我们遵循 van der Waerden，证明 $\mathfrak{A}$ 从而 $\mathfrak{A}_1$ 不可约。

**定理 3.4。** *定理 3.2 中具有非平凡公共零点的型组成的代数空间 $\mathfrak{A}_1$，实际上是一个 $\mathbf{Z}$-簇，即它不可约。素理想* <span class="original-page-anchor" id="pdf-page-404" aria-hidden="true"></span>*与 $\mathfrak{A}$ 相伴的、$\mathbf{Z}[W,X]$ 中的 $\mathfrak{p}$，由所有满足下述条件的多项式 $G(W,X)\in\mathbf{Z}[W,X]$ 组成：存在某个指标 $j$ 和整数 $s\geqq0$，使得*

$$
{(*)}_j\qquad X_j^sG(W,X)\equiv0\bmod(F_1,\ldots,F_r);\quad\text{即 }X_j^sG(W,X)\in\mathfrak{a}.
$$

*如果关系 (\*) 对一个指标 $j$ 成立，则它对每个 $j=1,\ldots,n$ 都成立。（当然，整数 $s$ 依赖于 $j$。）*

*证明。* 我们构造 $\mathfrak{A}$ 的一个泛点。任选一个变量，设为 $X_q$，将型 $F_i$ 如下改写：

$$
F_i(W,X)=F_i^*+Z_iX_q^{d_i},
$$

其中 $F_i^*$ 是除含有 $X_q^{d_i}$ 的单项式以外所有单项式的和。系数 $(W)$ 因此分为两族，记为 $(Y)$ 和 $(Z)$，其中 $(Z)=(Z_1,\ldots,Z_r)$ 是 $(F_1,\ldots,F_r)$ 中 $(X_q^{d_1},\ldots,X_q^{d_r})$ 的系数，$(Y)$ 是 $F_1^*,\ldots,F_r^*$ 的其余系数组成的族。有 $(W)=(Y,Z)$，并可以将多项式 $F_i$ 写成

$$
F_i(W,X)=F_i(Y,Z,X)=F_i^*(Y,X)+Z_iX_q^{d_i}.
$$

对应于变量 $(Y,X)$，选取在 $\mathbf{Z}$ 上代数独立的量 $(y,x)$。令

$$
\tag{3}z_i=-F_i^*(y,x)/x_q^{d_i}=-F_i^*(y,x/x_q).
$$

我们将证明 $(y,z,x)$ 是 $\mathfrak{A}$ 的一个泛点。

由构造立即可知，对所有 $i$ 都有 $F_i(y,z,x)=0$，所以如果 $G(W,X)\in\mathbf{Z}[W,X]$ 满足 (\*)，则 $G(y,z,x)=0$。

反过来，设 $G(Y,Z,X)\in\mathbf{Z}[Y,Z,X]=\mathbf{Z}[W,X]$ 满足 $G(y,z,x)=0$。由多元泰勒公式，得到

$$
\begin{aligned}
G(Y,Z,X)&=G(Y,\ldots,-F_i^*/X_q^{d_i}+Z_i+F_i^*/X_q^{d_i},\ldots,X)\\
&=G(Y,-F_i^*/X_q^{d_i},X)+\sum(Z_i+F_i^*/X_q^{d_i})^{\mu_i}H_{\mu_i}(Y,Z,X),
\end{aligned}
$$

其中求和遍历这样的项：具有因子 $(Z_i+F_i^*/X_q^{d_i})$ 的某个幂 $\mu_i>0$，并具有 $\mathbf{Z}[Y,Z,X]$ 中的某个因子 $H_{\mu_i}$。由 $(y,z,x)$ 的构造方式，以及 $G(y,z,x)=0$ 这一事实，可知第一项消失，因此

$$
G(Y,Z,X)=\sum(Z_i+F_i^*/X_q^{d_i})^{\mu_i}H_{\mu_i}(Y,Z,X).
$$

清除 $X_q$ 的分母后，对某个整数 $s$ 得到

$$
X_q^sG(Y,Z,X)\equiv0\bmod(F_1,\ldots,F_r),
$$

换句话说，$(*)_q$ 成立。这就完成了定理的证明。

**注。** 当然，将 $\mathbf{Z}$ 替换为域 $k$ 后，定理 3.4 中同样的断言与证明仍成立。在这种情形下，用 $\mathfrak{a}_k$ 表示 $k[W,X]$ 中由这些泛型生成的理想，类似地用 $\mathfrak{p}_k$ 表示相伴的素<span class="original-page-anchor" id="pdf-page-405" aria-hidden="true"></span>理想。则

$$
\mathfrak{a}_{k,1}=\mathfrak{a}_k\cap k[W]\quad\text{且}\quad\mathfrak{p}_{k,1}=\mathfrak{p}_k\cap k[W].
$$

定理 3.4 中的理想 $\mathfrak{p}$ 称为**与泛型理想相伴的素理想**。交 $\mathfrak{p}_1=\mathfrak{p}\cap\mathbf{Z}[W]$ 称为这些型的素**消去理想**。如前一样，若 $\mathfrak{A}$ 表示 $\mathfrak{p}$（或 $\mathfrak{a}$）的零点空间，$\mathfrak{A}_1$ 是它在第一个因子上的投影，则 $\mathfrak{p}_1$ 是与 $\mathfrak{A}_1$ 相伴的素理想。如果在域 $k$ 上工作而不用 $\mathbf{Z}$，也使用同样的术语。（*注：* 经典文献遵循 Hurwitz，将 $\mathfrak{p}_1$ 的齐次元素称为**惯性型**。我避免使用这一术语，因为“惯性”一词现在已经标准地用于惯性群，如第 VII 章 §2 中那样。）$\mathfrak{p}_1$ 的零点簇称为**结式簇**。它由给定的次数 $d_1,\ldots,d_n$ 确定，所以可以记为 $\mathfrak{A}_1(d_1,\ldots,d_n)$。

**练习。** 证明：如果 $\mathfrak{p}$ 是与泛型理想相伴的素理想，则 $\mathfrak{p}\cap\mathbf{Z}=(0)$ 是零理想。

**定理 3.5。** *假定 $r=n$，即处理 $n$ 个变量中的 $n$ 个型。则 $\mathfrak{p}_1$ 是由一个多项式生成的主理想，所以 $\mathfrak{A}_1$ 是所谓的超曲面。如果 $(w)$ 是 $\mathfrak{A}_1$ 在域 $k$ 上的一个泛点，则 $k(w)$ 在 $k$ 上的超越次数为 $m-1$。*

*证明。* 我们先证明第二个断言，并使用定理 3.4 证明中的同样记号。令 $u_j=x_j/x_n$。则 $u_n=1$，且 $(y),(u_1,\ldots,u_{n-1})$ 代数独立。由 (3)，有 $z_i=-F_i^*(y,u)$，所以

$$
k(w)=k(y,z)\subset k(y,u),
$$

从而 $k(w)$ 在 $k$ 上的超越次数 $\leqq m-1$。我们断言这个超越次数为 $m-1$。只需证明 $u_1,\ldots,u_{n-1}$ 在 $k(w)=k(y,z)$ 上代数。假定不是如此。则存在 $k(w,u)$ 的一个位 $\varphi$，它在 $k(w)$ 上为恒等映射，并将某个 $u_j$ 映到 $\infty$。选取一个指标 $q$，使得对所有 $i=1,\ldots,n-1$，$\varphi(u_i/u_q)$ 都有限。令 $v_i=u_i/u_q$，$v'_i=\varphi(u_i/u_q)$。用 $Y_{iq}$ 表示 $F_i$ 中 $X_q^{d_i}$ 的系数，用 $Y^*$ 表示从 $(Y)$ 中删去 $Y_{1q},\ldots,Y_{nq}$ 后的变量。由 (3)，对 $i=1,\ldots,n$ 有

$$
\begin{aligned}
0&=y_{iq}u_q^{d_i}+z_i+F_i^{**}(y^*,u)\\
&=y_{iq}+z_i/u_q^{d_i}+F_i^{**}(y^*,u/u_q).
\end{aligned}
$$

应用这个位得到

$$
0=y_{iq}+F_i^{**}(y^*,v').
$$

特别地，对每个 $i=1,\ldots,n$，有 $y_{iq}\in k(y^*,v')$。但是 $k(v')$ 在 $k$ 上的超越次数至多为 $n-1$，而元素 $(y_{1q},\ldots,y_{nq},y^*)$ 在 $k$ 上代数独立，从而得到矛盾，证明了定理。

<span class="original-page-anchor" id="pdf-page-406" aria-hidden="true"></span>

**注。** 有一个比定理 3.5 更精确的结果（我从 [Jo 80] 得知）。事实上，设定理 3.5 中的 $\mathfrak{A}$ 为 $\mathfrak{p}$ 的零点簇，$\mathfrak{A}_1$ 为它的投影。则这个投影在如下意义下是双有理的。采用定理 3.5 证明中的记号，结论不只是 $k(w)$ 在 $k$ 上的超越次数为 $m-1$，实际上有

$$
\mathbf{Q}(y,z)=\mathbf{Q}(w)=\mathbf{Q}(y,u).
$$

*证明。* 设 $\mathfrak{p}_1=(R)$，所以 $R$ 是结式，生成主理想 $\mathfrak{p}_1$。需要下述引理。

**引理 3.6。** *存在具有下述性质的正整数 $s$。固定指标 $i$，满足 $1\leqq i\leqq n-1$。对每一对由 $\geqq0$ 的整数组成的 $n$ 元组*

$$
(\alpha)=(\alpha_1,\ldots,\alpha_n)\quad\text{和}\quad(\beta)=(\beta_1,\ldots,\beta_n),
$$

*其中 $|\alpha|=|\beta|=d_i$，有*

$$
X_n^s\left(M_{(\alpha)}(X)\frac{\partial R}{\partial W_{i,(\beta)}}-M_{(\beta)}(X)\frac{\partial R}{\partial W_{i,(\alpha)}}\right)\equiv0\bmod(F_1,\ldots,F_n).
$$

为证明这一点，使用定理 3.4 中的事实：对某个 $s$，

$$
X_n^sR(W)=Q_1F_1+\cdots+Q_nF_n\quad\text{其中 }Q_j\in\mathbf{Z}[W,X].
$$

关于 $W_{i,(\beta)}$ 求导，得到

$$
X_n^s\frac{\partial R}{\partial W_{i,(\beta)}}\equiv Q_iM_{(\beta)}(X)\bmod(F_1,\ldots,F_n),
$$

类似地，

$$
X_n^s\frac{\partial R}{\partial W_{i,(\alpha)}}\equiv Q_iM_{(\alpha)}(X)\bmod(F_1,\ldots,F_n).
$$

将第一个同余式乘以 $M_{(\alpha)}(X)$，第二个乘以 $M_{(\beta)}(X)$，再相减，就得到引理。

由上述结论，可知

$$
M_{(\alpha)}(X)\frac{\partial R}{\partial W_{i,(\beta)}}-M_{(\beta)}(X)\frac{\partial R}{\partial W_{i,(\alpha)}}
$$

在令 $X_n=1$ 后，在 $\mathfrak{A}$ 上，即在点 $(w,u)$ 上消失。接着选取

$$
M_{(\alpha)}(X)=X_i^{d_i}\quad\text{和}\quad M_{(\beta)}(X)=X_i^{d_i-1}X_n\quad\text{对 }i=1,\ldots,n-1,
$$

可见有如下有理表达式：

$$
u_i=\left.\frac{\partial R/\partial W_{i,(\beta)}}{\partial R/\partial W_{i,(\alpha)}}\right|_{(W)=(w)}\quad\text{对 }i=1,\ldots,n-1,
$$

> **译校注。** 原书上式的比值方向颠倒。由刚证明的关系 $M_{(\alpha)}R_{W_{i,(\beta)}}-M_{(\beta)}R_{W_{i,(\alpha)}}=0$，代入这两个单项式并令 $X_n=1$，得到 $u_iR_{W_{i,(\beta)}}=R_{W_{i,(\alpha)}}$。因此在相应分母不为零时，应为 $u_i=\left.(\partial R/\partial W_{i,(\alpha)})/(\partial R/\partial W_{i,(\beta)})\right|_{(W)=(w)}$；正文照录的原比值是其倒数。这一交换不影响所要证明的域包含关系。

从而如所断言，$\mathbf{Q}(u)\subset\mathbf{Q}(w)$。

<span class="original-page-anchor" id="pdf-page-407" aria-hidden="true"></span>

注意，上述论证在特征为 $p$ 的素域上也成立。唯一需要补充的说明是，存在某个偏导数 $\partial R/\partial W_{i,(\alpha)}$ 在 $(w)$ 上不为零。这是一个小的技术问题，留给读者。

上述论证取自 [Jo 80] 的命题 3.3.1。Jouanolou 将 Macaulay [Ma 16] 中那样的旧有结果，与交换代数的较新方法联系起来，包括科祖尔复形（将在第 XXI 章讨论）。另见其专著 [Jo 90]、[Jo 91]。

仍然遵循 van der Waerden，现在将相当明确地确定定理 3.5 中生成该理想的多项式。我们处理泛型 $F_i(W,X)$ $(i=1,\ldots,n)$。由定理 3.5，理想 $\mathfrak{p}_1$ 由一个元素生成。由于 $\mathbf{Z}[W]$ 的可逆元只有 $\pm1$，这个元素在相差符号的意义下唯一确定。设

$$
R(W)=R(F_1,\ldots,F_n)
$$

为这个元素的一种选择。稍后将看到如何以典范方式从这两种可能的选择中选取一个。我们将证明这个元素的各种性质，并称它为 $F_1,\ldots,F_n$ 的**结式**。

对每个 $i=1,\ldots,n$，令 $D_i$ 为省去 $d_i$ 后其余次数的乘积，即

$$
D_i=d_1\cdots\widehat{d_i}\cdots d_n.
$$

令 $d$ 为满足 $d-1=\sum(d_i-1)$ 的正整数。

**引理 3.7。** *给定一个指标，设为 $n$，存在一个属于 $\mathfrak{p}_1$ 的元素 $R_n(W)$，满足下述性质。*

(a) *对每个 $i$，在 $\mathbf{Z}[W,X]$ 中有 $R_n(W)X_i^d\equiv0\bmod(F_1,\ldots,F_n)$。*

(b) *对每个 $i$，$R_n(W)$ 关于变量组 $(W_{i,(\nu)})$ 齐次，并且关于 $(W_{n,(\nu)})$，即关于 $F_n$ 的系数，次数为 $D_n$。*

(c) *作为 $\mathbf{Z}[W]$ 中的多项式，$R_n(W)$ 的容度为 $1$，即它是本原的。*

*证明。* 我们将实际明确构造多项式 $R_n(W)$。用 $M_\sigma(X)$ 表示次数为 $|\sigma|=d$ 的单项式。如下将指标集 $S=\{\sigma\}$ 分为不相交的子集。

令 $S_1=\{\sigma_1\}$ 为使 $M_{\sigma_1}(X)$ 可被 $X_1^{d_1}$ 整除的指标集。

令 $S_2=\{\sigma_2\}$ 为使 $M_{\sigma_2}(X)$ 可被 $X_2^{d_2}$ 整除，但不可被 $X_1^{d_1}$ 整除的指标集。

$\ldots$

令 $S_n=\{\sigma_n\}$ 为使 $M_{\sigma_n}(X)$ 可被 $X_n^{d_n}$ 整除，但不可被 $X_1^{d_1},\ldots,X_{n-1}^{d_{n-1}}$ 整除的指标集。

<span class="original-page-anchor" id="pdf-page-408" aria-hidden="true"></span>

则 $S$ 是 $S_1,\ldots,S_n$ 的不相交并。将每个单项式如下写出：

$$
\begin{array}{lll}
M_{\sigma_1}(X)=H_{\sigma_1}(X)X_1^{d_1}&\text{所以}&\deg H_{\sigma_1}=d-d_1\\
\vdots\qquad\vdots&&\\
M_{\sigma_1}(X)=H_{\sigma_n}(X)X_n^{d_n}&\text{所以}&\deg H_{\sigma_n}=d-d_n.
\end{array}
$$

> **译校注。** 最后一行原书印作 $M_{\sigma_1}(X)$；根据划分中的 $S_n$ 以及对应因子 $H_{\sigma_n}$，此处应为 $M_{\sigma_n}(X)$。正文保留原印下标。

于是多项式

$$
H_{\sigma_1}F_1,\ldots,H_{\sigma_n}F_n\quad(\text{其中 }\sigma_1\in S_1,\ldots,\sigma_n\in S_n)
$$

的数目恰好等于 $d$ 次单项式的数目。将这些多项式视为关于 $(X)$ 的型，系数在 $\mathbf{Z}[W]$ 中，并令 $R_n$ 为它们的系数行列式。则 $R_n=R_n(W)\in\mathbf{Z}[W]$。我们断言 $R_n(W)$ 满足引理的性质。

首先注意到，如果 $\sigma_n\in S_n$，那么对于 $i=1,\ldots,n-1$，$H_{\sigma_n}(X)$ 中 $X_i$ 的幂至多为 $d_i-1$。另一方面，$H_{\sigma_n}(X)$ 关于 $X_n$ 的次数由总次数等于 $d-d_n$ 的条件确定。因此 $S_n$ 恰有 $D_n$ 个元素。立即可知，$R_n(W)$ 关于 $F_n$ 的系数，即关于 $(W_{n,(\nu)})$，是 $D_n$ 次齐次的。由构造还可知，对每个 $i=1,\ldots,n-1$，$R_n$ 关于变量组 $(W_{i,(\nu)})$ 齐次。

如果将型 $F_i$ $(i=1,\ldots,n)$ 特化为 $X_i^{d_i}$，则 $R_n$ 特化为 $1$，因而 $R_n\ne0$ 且 $R_n$ 本原。对每个 $\sigma_i$，可以写成

$$
H_{\sigma_i}F_i=\sum_{\sigma\in S}C_{\sigma,\sigma_i}(W)M_\sigma(X),
$$

其中 $M_\sigma(X)$ $(\sigma\in S)$ 遍历 $(X)$ 的所有 $d$ 次单项式，而 $C_{\sigma,\sigma_i}(W)$ 是变量 $(W)$ 之一。于是由定义，

$$
R_n(W)=\det(C_{\sigma,\sigma_1}(W)_{(\sigma_1\in S_1)},\ldots,C_{\sigma,\sigma_n}(W)_{(\sigma_n\in S_n)})=\det(C).
$$

其中 $\sigma_1\in S_1,\ldots,\sigma_n\in S_n$ 是列指标，$\sigma$ 是行指标。设 $B=\widehat{C}$ 是分量在 $\mathbf{Z}[W,X]$ 中、满足

$$
BC=\det(C)I=R_nI
$$

的矩阵。（参见第 XIII 章推论 4.17。）则对每个 $\sigma$，有

$$
R_n(W)M_\sigma(X)=\sum_i\sum_{\sigma_i\in S_i}B_{i,\sigma_i}F_i.
$$

> **译校注。** 上述矩阵推论保留原印式，但原书此式有误。例如，取 $n=2$、$d_1=d_2=1$、$F_1=X_1$、$F_2=X_2$，则 $C=B=I$，原式右边为 $X_1+X_2$，而当 $M_\sigma=X_1$ 时左边为 $X_1$。按照原书的行、列指标约定，令 $h=(H_{\sigma_i}F_i)$、$M=(M_\sigma)$ 为列向量，则 $h=C^tM$，而 $CB=R_nI$ 给出正确的系数恒等式 $R_nM_\sigma=\sum_i\sum_{\sigma_i\in S_i}B_{\sigma_i,\sigma}H_{\sigma_i}F_i$。该恒等式说明了原书意欲使用的理想包含论证；正文没有擅自替换原印公式。

给定 $i$，取使 $M_\sigma(X)=X_i^d$ 的指标 $\sigma$，就得到引理 3.7 的第一个关系。由定理 3.4，可知 $R_n(W)\in\mathfrak{p}_1$。这就完成了引理的证明。

当然，我们只是为了具体起见选取指标 $n$。对每个 $i$，都有一个满足类似性质的多项式 $R_i$；特别地，它关于变量 $(W_{i,(\nu)})$，即型 $F_i$ 的系数，是 $D_i$ 次齐次的。

<span class="original-page-anchor" id="pdf-page-409" aria-hidden="true"></span>

**定理 3.8。** *设 $R$ 是 $\mathbf{Z}$ 上 $n$ 个变量中的 $n$ 个泛型 $F_i$ 的结式。则 $R$ 满足下述性质。*

(a) *$R$ 是多项式 $R_1,\ldots,R_n$ 在 $\mathbf{Z}[W]$ 中的最大公因子。*

(b) *$R$ 关于 $F_i$ 的系数是 $D_i$ 次齐次的。*

(c) *设 $F_i=\cdots+W_{i,(d_i)}X_i^{d_i}$，所以 $W_{i,(d_i)}$ 是 $X_i^{d_i}$ 的系数。则 $R$ 包含单项式*

$$
\pm\prod_{i=1}^nW_{i,(d_i)}^{D_i}.
$$

*证明。* 思路是将型 $F_1,\ldots,F_n$ 特化为泛线性型的乘积，此时可以清楚看出所发生的情况。为此需要一个引理，它属于一个最终将要证明的更一般的性质。我们将使用下述记号。如果 $f_1,\ldots,f_n$ 是系数为 $(w)$ 的型，则写成

$$
R(f_1,\ldots,f_n)=R(w).
$$

**引理 3.9。** *设 $G,H$ 是独立的泛型，且 $\deg(GH)=d_1$。则 $R(GH,F_2,\ldots,F_n)$ 可被 $R(G,F_2,\ldots,F_n)R(H,F_2,\ldots,F_n)$ 整除。*

*证明。* 由定理 3.5，存在表达式

$$
X_n^sR(F_1,\ldots,F_n)=Q_1F_1+\cdots+Q_nF_n\quad\text{其中 }Q_i\in\mathbf{Z}[W,X].
$$

设 $W_G,W_H,W_{F_2},\ldots,W_{F_n}$ 分别为 $G,H,F_2,\ldots,F_n$ 的系数，设 $(w)$ 为 $GH,F_2,\ldots,F_n$ 的系数。则

$$
R(w)=R(GH,F_2,\ldots,F_n),
$$

并得到

$$
X_n^sR(w)=Q_1(w,X)GH+Q_2(w,X)F_2+\cdots+Q_n(w,X)F_n.
$$

因此，$R(GH,F_2,\ldots,F_n)$ 属于环 $\mathbf{Z}[W_G,W_H,W_{F_2},\ldots,W_{F_n}]$ 中 $G,F_2,\ldots,F_n$ 的消去理想，将 $G$ 换成 $H$ 也类似成立。由于 $W_H$ 是 $\mathbf{Z}[W_G,W_{F_2},\ldots,W_{F_n}]$ 上的一族独立变量，可知 $R(G,F_2,\ldots,F_n)$ 在这个环中整除 $R(GH,F_2,\ldots,F_n)$，对 $R(H,F_2,\ldots,F_n)$ 也类似成立。但是 $(W_G)$ 和 $(W_H)$ 是独立的变量组，所以 $R(G,F_2,\ldots,F_n),R(H,F_2,\ldots,F_n)$ 是这个环中不同的素元，因此如所断言，它们的乘积整除 $R(GH,F_2,\ldots,F_n)$，从而引理得证。

引理 3.9 适用于系数在域 $k$ 中的任意特化后的多项式族 $g,h,f_1,\ldots,f_n$。注意，对于 $n$ 个变量中的 $n$ 个线性型组成的组，其结式就是系数行列式。因此，如果 $L_1,\ldots,L_n$ 是变量 $X_1,\ldots,X_n$ 中泛独立的线性型，则它们的结式 $R(L_1,\ldots,L_n)$ 对每个 $i$ 都关于 $L_i$ 的系数为 1 次齐次。将引理 3.9 应用于型 $f_1,\ldots,f_{n-1}$ 都是泛独立线性型的乘积的情形。由引理 3.9 可知，对这个特化后的型族，它们的结式关于<span class="original-page-anchor" id="pdf-page-410" aria-hidden="true"></span>$F_n$ 的系数的次数至少为 $D_n$，因此对泛型 $F_1,\ldots,F_n$，其结式关于 $F_n$ 的系数的次数至少为 $D_n$。类似地，对每个 $i$，$R(F_1,\ldots,F_n)$ 关于 $F_i$ 的系数的次数至少为 $D_i$。但是 $R$ 整除引理 3.7 中构造的 $n$ 个元素 $R_1(W),\ldots,R_n(W)$。因此可知，$R$ 关于 $F_i$ 的系数的次数恰好为 $D_i$。由定理 3.5，知道 $R$ 整除每个 $R_i$。设 $G$ 是 $R_1,\ldots,R_n$ 在 $\mathbf{Z}[W]$ 中的最大公因子。则 $R$ 整除 $G$，并且对于 $i=1,\ldots,n$，在每组变量 $(W_{i,(\nu)})$ 中具有相同次数。因此存在 $c\in\mathbf{Z}$，使得 $G=cR$。必定有 $c=\pm1$，因为例如 $R_n$ 在 $\mathbf{Z}[W]$ 中本原。这证明了定理的 (a) 和 (b)。

关于第三部分，将这些型特化为 $f_i=X_i^{d_i}$，$i=1,\ldots,n$。则 $R_n$ 特化为 $1$，而由于 $R$ 整除 $R_n$，可知 $R$ 本身特化为 $\pm1$。由于除记为 $W_{i,(d_i)}$ 的那些系数以外，所有系数都特化为 $0$，可知 $R(W)$ 包含由这些变量各取 $D_i$ 次幂所得乘积的单项式，其符号为 $\pm1$。这证明了 (c)，并完成了定理 3.8 的证明。

现在可以选择符号，使 $R$ 包含系数为 $+1$ 的单项式

$$
M=\prod_{i=1}^nW_{i,(d_i)}^{D_i},
$$

从而将结式规范化。这个条件唯一确定 $R$，此后也将 $R$ 记为

$$
R=\operatorname{Res}(F_1,\ldots,F_n).
$$

给定系数 $(w)$ 在域 $K$（实际上在任意交换环）中的型 $f_1,\ldots,f_n$，就可以用规范化后的多项式 $R$ 定义它们的**结式**

$$
\operatorname{Res}(f_1,\ldots,f_n)=R(w).
$$

采用这种规范化后，就得到比引理 3.9 更强的结果。

**定理 3.10。** *设 $f_1=gh$ 是型的乘积，满足 $\deg(gh)=d_1$。设 $f_2,\ldots,f_n$ 是次数为 $d_2,\ldots,d_n$ 的任意型。则*

$$
\operatorname{Res}(gh,f_2,\ldots,f_n)=\operatorname{Res}(g,f_2,\ldots,f_n)\operatorname{Res}(h,f_2,\ldots,f_n).
$$

*证明。* 由多项式乘积中次数必须相加的事实，再结合定理 3.8(a)、(b)，现在可以看出，在尚不知道 $R$ 关于每组变量的准确次数时，引理 3.9 只得到整除关系，而此时必定得到准确的等式。

定理 3.10 在证明行列式的进一步性质时很有用，因为它使我们可以借助多项式的因式分解约化到简单情形。

<span class="original-page-anchor" id="pdf-page-411" aria-hidden="true"></span>

例如，有：

**定理 3.11。** *设 $F_1,\ldots,F_n$ 是 $n$ 个变量中的泛型，$\overline{F}_1,\ldots,\overline{F}_n$ 是代入 $X_n=0$ 所得到的型，所以 $\overline{F}_1,\ldots,\overline{F}_{n-1}$ 是 $n-1$ 个变量中的泛型。设 $n\geqq2$。则*

$$
\operatorname{Res}(F_1,\ldots,F_{n-1},X_n^{d_n})=\operatorname{Res}(\overline{F}_1,\ldots,\overline{F}_{n-1})^{d_n}.
$$

*证明。* 由定理 3.10，只需在 $d_n=1$ 时证明断言。由定理 3.4，对每个 $i=1,\ldots,n-1$，有表达式

$$
\tag{*}X_i^s\operatorname{Res}(F_1,\ldots,F_{n-1},X_n)=Q_1F_1+\cdots+Q_{n-1}F_{n-1}+Q_nX_n,
$$

其中 $Q_j\in\mathbf{Z}[W,X]$（依赖于 $i$ 的选择）。左边可以写成关于 $F_1,\ldots,F_{n-1}$ 的系数的多项式，采用记号

$$
X_i^sR(W_{F_1},\ldots,W_{F_{n-1}},1_{X_n})=X_i^sP(W_{F_1},\ldots,W_{F_{n-1}})=X_i^sP(W^{(n-1)}),
$$

也就是说，在关于 $X_1,\ldots,X_n$ 的泛线性型中，除 $X_n$ 的系数特化为 $1$ 以外，其余所有系数都特化为 $0$。在 (\*) 的右边代入 $X_n=0$。由定理 3.4，可知 $P(W^{(n-1)})$ 属于 $\overline{F}_1,\ldots,\overline{F}_{n-1}$ 的结式理想，因此 $\operatorname{Res}(\overline{F}_1,\ldots,\overline{F}_{n-1})$ 整除 $P(W^{(n-1)})$。由定理 3.8，知道 $P(W^{(n-1)})$ 关于 $W_{\overline{F}_i}$ $(i=1,\ldots,n-1)$ 的齐次次数，与 $\operatorname{Res}(\overline{F}_1,\ldots,\overline{F}_{n-1})$ 相同。因此存在 $c\in\mathbf{Z}$，使得

$$
c\operatorname{Res}(\overline{F}_1,\ldots,\overline{F}_{n-1})=\operatorname{Res}(F_1,\ldots,F_{n-1},X_n).
$$

将 $\overline{F}_1,\ldots,\overline{F}_{n-1}$ 分别特化为 $X_1^{d_1},\ldots,X_{n-1}^{d_{n-1}}$，即得 $c=1$，从而完成证明。

下一个基本引理的泛情形，例如在 Macaulay [Ma 16] 中有所陈述，而 [Jo 90] 的引理 5.6 又讨论了它。

**引理 3.12。** *设 $A$ 是交换环。设 $f_1,\ldots,f_n,g_1,\ldots,g_n$ 是 $A[X_1,\ldots,X_n]$ 中的齐次多项式。假定作为 $A[X]$ 中的理想，有*

$$
(g_1,\ldots,g_n)\subset(f_1,\ldots,f_n).
$$

*则*

$$
\operatorname{Res}(f_1,\ldots,f_n)\text{ 在 }A\text{ 中整除 }\operatorname{Res}(g_1,\ldots,g_n).
$$

*证明。* 将每个 $g_i$ 表示为 $g_i=\sum h_{ij}f_j$，其中 $h_{ij}$ 在 $A[X]$ 中齐次。通过特化，可以假定 $g_i=\sum H_{ij}F_j$，其中 $H_{ij}$ 和 $F_j$ 的系数在 $\mathbf{Z}$ 上代数独立。由定理 3.4，对每个 $i$，有关系

$$
X_i^s\operatorname{Res}(g_1,\ldots,g_n)=Q_1g_1+\cdots+Q_ng_n\quad\text{其中某些 }Q_i\in\mathbf{Z}[W_H,W_F],
$$

> **译校注。** 原书末式将 $Q_i$ 的所属环写作 $\mathbf{Z}[W_H,W_F]$。这里的理想表示一般需要 $X$ 的多项式系数，故应在 $\mathbf{Z}[W_H,W_F,X]$ 中理解；下一页也明确在这个环中作同余。比如两个泛型的次数分别为 $2$、$3$ 时，只用不含 $X$ 的系数无法把一个单项式 $X_i^s\operatorname{Res}(g_1,g_2)$ 表成它们的线性组合：按齐次次数分解，至少一项必须为零，而另一泛型也不是单项式。正文保留原书的环记号。

<span class="original-page-anchor" id="pdf-page-412" aria-hidden="true"></span>

其中 $W_H,W_F$ 分别表示多项式 $H_{ij}$ 和 $F_j$ 的独立变量系数。特别地，

$$
\tag{*}X_i^s\operatorname{Res}(g_1,\ldots,g_n)\equiv0\bmod(F_1,\ldots,F_n)\mathbf{Z}[W_H,W_F,X].
$$

注意，$\operatorname{Res}(g_1,\ldots,g_n)=P(W_H,W_F)\in\mathbf{Z}[W_H,W_F]$ 是一个整数系数多项式。如果 $(w_F)$ 是结式簇 $\mathfrak{A}_1$ 在 $\mathbf{Z}$ 上的一个泛点，则由 (\*)，$P(W_H,w_F)=0$。因此 $\operatorname{Res}(F_1,\ldots,F_n)$ 整除 $P(W_H,W_F)$，从而引理得证。

**定理 3.13。** *设 $A$ 是交换环，并如常设 $d_1,\ldots,d_n$ 是 $\geqq1$ 的整数。设 $f_i$ 是 $A[X]=A[X_1,\ldots,X_n]$ 中的 $d_i$ 次齐次多项式。设 $d$ 是 $\geqq1$ 的整数，$g_i,\ldots,g_n$ 是 $A[X]$ 中的 $d$ 次齐次多项式。则*

$$
f_i\circ g=f_i(g_1,\ldots,g_n)
$$

*是 $dd_i$ 次齐次的，且*

$$
\operatorname{Res}(f_1\circ g,\ldots,f_n\circ g)=\operatorname{Res}(g_1,\ldots,g_n)^{d_1\cdots d_n}\operatorname{Res}(f_1,\ldots,f_n)^{d^{n-1}}\text{ 在 }A\text{ 中成立}.
$$

*证明。* 从定理 3.4 的标准关系开始：

$$
\tag{*}X_i^s\operatorname{Res}(F_1,\ldots,F_n)\equiv0\bmod(F_1,\ldots,F_n)\mathbf{Z}[W_F,X].
$$

设 $G_1,\ldots,G_n$ 是独立的 $d$ 次泛多项式，用 $W_G$ 表示它们的独立变量系数。在 (\*) 中用 $G_i$ 代替 $X_i$，得到

$$
G_i^s\operatorname{Res}(F_1,\ldots,F_n)\equiv0\bmod(F_1\circ G,\ldots,F_n\circ G)\mathbf{Z}[W_F,W_G,X].
$$

将 $\operatorname{Res}(F_1,\ldots,F_n)$ 简记为 $R(F)$，并令 $g_i=G_i^sR(F)$。由引理 3.12，可知

$$
\operatorname{Res}(f_1\circ G,\ldots,F_n\circ G)\text{ 在 }\mathbf{Z}[W_F,W_G]\text{ 中整除 }\operatorname{Res}(G_1^sR(F),\ldots,G_n^sR(F)).
$$

> **译校注。** 原书在上一个显示公式的结式开头印作小写 $f_1$。本证明使用的泛多项式是 $F_1,\ldots,F_n$，所以此处应为 $F_1$。

由定理 3.10 及定理 3.8(b) 的齐次性，得到

$$
\operatorname{Res}(G_1^sR(F),\ldots,G_n^sR(F))=\operatorname{Res}(G_1,\ldots,G_n)^M\operatorname{Res}(F_1,\ldots,F_n)^N,
$$

其中整数 $M,N\geqq0$。由于 $\operatorname{Res}(G_1,\ldots,G_n)$ 和 $\operatorname{Res}(F_1,\ldots,F_n)$ 是 $\mathbf{Z}[W_G,W_F]$ 中不同的素元（它们涉及独立变量，因而不同），可知

$$
\tag{**}\operatorname{Res}(F_1\circ G,\ldots,F_n\circ G)=\varepsilon\operatorname{Res}(G_1,\ldots,G_n)^a\operatorname{Res}(F_1,\ldots,F_n)^b,
$$

其中整数 $a,b\geqq0$，且 $\varepsilon=1$ 或 $-1$。最后，将 $F_i$ 特化为 $W_iX_i^{d_i}$，将 $G_i$ 特化为 $U_iX_i^d$，其中 $(W_1,\ldots,W_n,U_1,\ldots,U_n)$ 是独立变量。

<span class="original-page-anchor" id="pdf-page-413" aria-hidden="true"></span>

在 (\*\*) 中代入，得到

$$
\begin{aligned}
\operatorname{Res}(W_1U_1^{d_1}X_1^{dd_1},\ldots,W_nU_n^{d_n}X_n^{dd_n})\\
=\varepsilon\operatorname{Res}(U_1X_1^d,\ldots,U_nX_n^d)^a\operatorname{Res}(W_1X_1^{d_1},\ldots,W_nX_n^{d_n})^b.
\end{aligned}
$$

由定理 3.8(b) 的齐次性，得到

$$
\prod_i(W_iU_i^{d_i})^{d_1\cdots\widehat{d_i}\cdots d_n d^{n-1}}=\varepsilon\prod_iU_i^{d^{n-1}a}\prod_iW_i^{d_1\cdots\widehat{d_i}\cdots d_n b}.
$$

由此立即得到 $\varepsilon=1$，且 $a,b$ 正是定理中所给出的值。

**推论 3.14。** *设 $C=(c_{ij})$ 是系数在 $A$ 中的方阵。令 $f_i(X)=F_i(CX)$（其中 $CX$ 是矩阵乘法，将 $X$ 看作列向量）。则*

$$
\operatorname{Res}(f_1,\ldots,f_n)=\det(C)^{d_1\cdots d_n}\operatorname{Res}(F_1,\ldots,F_n).
$$

*证明。* 这是 $d=1$ 且对每个 $i$，$g_i$ 都是线性型的情形。

**定理 3.15。** *设 $f_1,\ldots,f_n$ 在 $A[X]$ 中齐次，并假定对所有 $i$ 有 $d_n\geqq d_i$。设 $h_i$ 是 $A[X]$ 中的 $d_n-d_i$ 次齐次多项式。则*

$$
\operatorname{Res}\left(f_1,\ldots,f_{n-1},f_n+\sum_{j=1}^{n-1}h_jf_j\right)=\operatorname{Res}(f_1,\ldots,f_n)\text{ 在 }A\text{ 中成立}.
$$

*证明。* 可以假定 $f_i=F_i$ 是泛型，$H_i$ 是与 $F_1,\ldots,F_n$ 泛独立的型，且 $A=\mathbf{Z}[W_F,W_H]$，其中 $(W_F)$ 和 $(W_H)$ 是相应多项式的系数。注意到理想 $(F_1,\ldots,F_n)$ 和 $(F_1,\ldots,F_n+\sum_{j\ne n}H_jF_j)$ 相等。由引理 3.12，可知定理断言中的两个结式相差因子 $1$ 或 $-1$。现在可以将 $H_{ij}$ 特化为 $0$，从而确定该因子为 $+1$，证明完成。

**定理 3.16。** *设 $\pi$ 是 $\{1,\ldots,n\}$ 的一个置换，$\varepsilon(\pi)$ 为其符号。则*

$$
\operatorname{Res}(F_{\pi(1)},\ldots,F_{\pi(n)})=\varepsilon(\pi)^{d_1\cdots d_n}\operatorname{Res}(F_1,\ldots,F_n).
$$

*证明。* 再次将引理 3.12 应用于相等的理想 $(F_1,\ldots,F_n)$ 和 $(F_{\pi(1)},\ldots,F_{\pi(n)})$，得到所要求的等式在 $\mathbf{Z}[W_F]$ 中相差因子 $\pm1$。将 $F_i$ 特化为 $X_i^{d_i}$，并利用定理 3.10 的乘法性来确定这个符号。于是约化到 $F_i=X_i$，即线性型的情形，再应用推论 3.14 即完成证明。

下一个定理原是 van der Waerden 的 *Moderne Algebra*（《近世代数》）中的一个练习。

<span class="original-page-anchor" id="pdf-page-414" aria-hidden="true"></span>

**定理 3.17。** *设 $L_1,\ldots,L_{n-1},F$ 是 $n$ 个变量中的泛型，其中 $L_1,\ldots,L_{n-1}$ 的次数为 $1$，$F$ 的次数为 $d=d_n$。令*

$$
\Delta_j\quad(j=1,\ldots,n)
$$

*为型组 $(L_1,\ldots,L_{n-1})$ 的系数矩阵的第 $j$ 个子式的 $(-1)^{n-j}$ 倍。则*

$$
\operatorname{Res}(L_1,\ldots,L_{n-1},F)=F(\Delta_1,\ldots,\Delta_n).
$$

*证明。* 先断言，对所有 $j=1,\ldots,n$，有同余式

$$
\tag{*}X_n\Delta_j-X_j\Delta_n\equiv0\bmod(L_1,\ldots,L_{n-1})\mathbf{Z}[W,X],
$$

其中如常，$(W)$ 是型 $L_1,\ldots,L_{n-1},F$ 的系数。为证明这一点，考虑线性方程组

$$
\begin{aligned}
W_{11}X_1+\cdots+W_{1,n-1}X_{n-1}&=L_1(W,X)-W_{1,n}X_n\\
&\cdots\cdots\\
W_{n-1,1}X_1+\cdots+W_{n-1,n-1}X_{n-1}&=L_{n-1}(W,X)-W_{n-1,n}X_n.
\end{aligned}
$$

如果 $C=(C^1,\ldots,C^{n-1})$ 是列为 $C^j$ 的方阵，则线性方程组 $CX=C^n$ 的解满足克拉默法则

$$
X_j\det(C^1,\ldots,C^{n-1})=\det(C^1,\ldots,C^n,\ldots,C^{n-1}).
$$

利用行列式关于每列的线性性，便得到 (\*)。

接着，由同余式 (\*) 可知

$$
X_n^dF(\Delta_1,\ldots,\Delta_n)\equiv\Delta_n^dF(X_1,\ldots,X_n)\bmod(L_1,\ldots,L_{n-1})\mathbf{Z}[W,X],
$$

从而

$$
X_n^dF(\Delta_1,\ldots,\Delta_n)\equiv0\bmod(L_1,\ldots,L_{n-1},F).
$$

因此，由定理 3.4 以及 $\operatorname{Res}(L_1,\ldots,L_{n-1},F)=R(W)$ 生成消去理想这一事实，可知存在 $c\in\mathbf{Z}[W]$，使得

$$
F(\Delta_1,\ldots,\Delta_n)=c\operatorname{Res}(L_1,\ldots,L_{n-1},F).
$$

由于左边关于系数 $W_F$ 是 1 次齐次的，而且对每个 $i=1,\ldots,n-1$，关于系数 $W_{L_i}$ 是 $d$ 次齐次的，由定理 3.8 可知 $c\in\mathbf{Z}$。将 $L_i$ 特化为 $X_i$，$F$ 特化为 $X_n^d$，则当 $j\ne n$ 时 $\Delta_j$ 特化为 $0$，而 $\Delta_n$ 特化为 $1$。因此左边特化为 $1$，右边也如此，所以 $c=1$。证明完成。

<span class="original-page-anchor" id="pdf-page-415" aria-hidden="true"></span>

### 参考文献

[Jo 80] J. P. Jouanolou，Idéaux résultants（结式理想），*Advances in Mathematics* **37 第 3 期**（1980），第 212–238 页。

[Jo 90] J. P. Jouanolou，Le formalisme du résultant（结式的形式体系），*Advances in Mathematics* **90 第 2 期**（1991），第 117–263 页。

[Jo 91] J. P. Jouanolou，*Aspects invariants de l'élimination*（消去理论的不变性方面），Département de Mathématiques，Université Louis Pasteur，法国斯特拉斯堡（1991）。

[Ma 16] F. Macaulay，*The algebraic theory of modular systems*（模系的代数理论），Cambridge University Press，1916。

## §4. 结式系统

用于证明定理 3.4 的投影论证，优点是以非常明确的方式构造泛点。另一方面，它没有给出用来构造定义 $\mathfrak{A}_1$ 的型组的明确公式，甚至没有给出有效公式。现在将重新表述定理 3.4 在 $\mathbf{Z}$ 上的一个版本，并用完全不同的方法证明它；该方法有效地构造一个生成元组，生成定理 3.2 中算术簇 $\mathfrak{A}_1$ 的一个定义理想。

**定理 4.1。** *给定次数 $d_1,\ldots,d_r\geqq1$ 以及正整数 $m,n$。设 $(W)=(W_{i,(\nu)})$ 为 §3 的 (2) 中的变量，视为整数 $\mathbf{Z}$ 上的代数独立元素。存在可以有效确定的有限个多项式 $R_\rho(W)\in\mathbf{Z}[W]$，具有下述性质。设 $(f)$ 如 (1) 中那样，是给定次数的一组型，其系数 $(w)$ 在某个域 $k$ 中。则 $(f)$ 有非平凡公共零点，当且仅当对所有 $\rho$ 都有 $R_\rho(w)=0$。*

具有定理 4.1 所述性质的有限族 $\{R_\rho\}$，称为给定次数的一个**结式系统**。据 van der Waerden（*Moderne Algebra*，第一、第二版，§80）所述，下述利用结式的证明方法可以追溯到克罗内克消去法，以及 Kapferer 的一篇论文（Über Resultanten und Resultantensysteme，关于结式与结式系统，*Sitzungsber. Bayer. Akad. München* 1929，第 179–200 页）。多项式族 $\{R_\rho(W)\}$ 因其构造方式而称为**结式系统**。它们构成某个理想 $\mathfrak{b}_1$ 的生成元集，使得算术簇 $\mathfrak{A}_1$ 为 $\mathfrak{b}_1$ 的零点集。我不知道下面构造的系统，距离成为与 $\mathfrak{A}_1$ 相伴的 $\mathbf{Z}[W]$ 中素理想 $\mathfrak{p}_1$ 的生成元集还有多远。实际上不需要第 IV 章 §10 的全部理论；只需要结式的一个特征性质。

<span class="original-page-anchor" id="pdf-page-416" aria-hidden="true"></span>

设 $p,q$ 是正整数。设

$$
\begin{aligned}
f_v&=v_0X_1^p+v_1X_1^{p-1}X_2+\cdots+v_pX_2^p\\
g_w&=w_0X_1^q+w_1X_1^{q-1}X_2+\cdots+w_qX_2^q
\end{aligned}
$$

是 $\mathbf{Z}[v,w,X_1,X_2]=\mathbf{Z}[v,w][X]$ 中的两个泛齐次多项式。在第 IV 章 §10 中，我们在 $X_2=1$ 的情形定义了它们的结式 $\operatorname{Res}(f_v,g_w)$，不过现在发现使用齐次多项式更合适。为当前目的，只需知道结式 $R(v,w)$ 由如下性质刻画。如果在域 $K$ 中有 $(v,w)$ 的一个特化 $(a,b)$，且 $f_a,f_b$ 具有因式分解

$$
f_a=a_0\prod_{i=1}^p(X_1-\alpha_iX_2)
$$

$$
g_b=b_0\prod_{j=1}^q(X_1-\beta_jX_2),
$$

则有关于根的对称表达式：

$$
\begin{aligned}
R(a,b)&=\operatorname{Res}(f_a,f_b)=a_0^qb_0^p\prod_{i,j}(\alpha_i-\beta_j)\\
&=a_0^q\prod_i g_b(\alpha_i,1)=(-1)^{pq}b_0^p\prod_j f_a(\beta_j,1).
\end{aligned}
$$

> **译校注。** 原书在引出因式分解时以及 $\operatorname{Res}(f_a,f_b)$ 中使用 $f_b$；第二个多项式已定义为 $g_b$，所以这两处应读作 $g_b$。

由对称多项式的一般理论，事先就清楚 $R(v,w)$ 属于 $\mathbf{Z}[v,w]$，而第 IV 章 §10 给出一个明确表示

$$
\varphi_{v,w}f_v+\psi_{v,w}g_w=X_2^{p+q-1}R(v,w),
$$

其中 $\varphi_{v,w}$ 和 $\psi_{v,w}\in\mathbf{Z}[v,w,X]$。我们不需要这个表示。下一个性质将提供消去法的基本归纳步骤。

**命题 4.2。** *设 $f_a,g_b$ 是系数在域 $K$ 中的齐次多项式。则 $R(a,b)=0$，当且仅当方程组*

$$
f_a(X)=0,\quad g_b(X)=0
$$

*在 $K$ 的某个扩张中有非平凡零点（这个扩张可以取为有限扩张）。*

如果 $a_0=0$，则 $g_b$ 的一个零点也是 $f_a$ 的零点；如果 $b_0=0$，则 $f_a$ 的一个零点也是 $g_b$ 的零点。如果 $a_0b_0\ne0$，则由结式表示为根之差 $(\alpha_i-\beta_j)$ 的乘积，命题立即成立。

> **译校注。** 若不加 $R(a,b)=0$ 的假设，证明的第一句话不成立：$f_a=X_2$、$g_b=X_1$ 满足 $a_0=0$，却没有公共非平凡零点。该句应在证明中已假定 $R(a,b)=0$ 的方向理解；正文保留原文措辞。

现在将利用结式证明定理 4.1。证明对 $n$ 作归纳。

<span class="original-page-anchor" id="pdf-page-417" aria-hidden="true"></span>

如果 $n=1$，定理显然成立。

如果 $n=2$、$r=1$，定理同样显然成立，取 $(R_\rho)$ 为空集即可。

如果 $n=2$、$r=2$，定理就是命题 4.2。

现在假定 $n=2$ 且 $r>2$，于是有齐次方程组

$$
0=f_1(X)=f_2(X)=\cdots=f_r(X),
$$

其中 $(X)=(X_1,X_2)$。设 $d_i$ 为 $f_i$ 的次数，令 $d=\max d_i$。将族 $\{f_i(X)\}$ 替换为由所有多项式

$$
f_i(X)X_1^{d-d_i}\quad\text{和}\quad f_i(X)X_2^{d-d_i},\quad i=1,\ldots,r
$$

组成的族。这两个族具有相同的非平凡零点集，所以为证明定理 4.1，可以不失一般性地假定所有多项式 $f_1,\ldots,f_r$ 都有相同的次数 $d$。

当 $n=2$ 时，考虑关于 $(X)$ 的 $d$ 次泛型组：

$$
\tag{4}F_i(W,X)=0\text{，其中 }i=1,\ldots,r\text{，变量为 }(X)=(X_1,X_2),
$$

其中 $F_i$ 的系数为 $W_{i,0},\ldots,W_{i,d}$，所以

$$
(W)=(W_{1,0},\ldots,W_{1,d},\ldots,W_{r,0},\ldots,W_{r,d}).
$$

下一个命题是定理 4.1 的一个特殊情形，但它给出归纳法的第一步，说明如何对这样的更大方程组得到命题 4.2 的类似结果。设 $T_1,\ldots,T_r$ 和 $U_1,\ldots,U_r$ 是 $\mathbf{Z}[W,X]$ 上的独立变量。设 $F_1,\ldots,F_r$ 为 §3 的 (2) 中的泛型。令

$$
\begin{aligned}
f&=F_1(W,X)T_1+\cdots+F_r(W,X)T_r\\
g&=F_1(W,X)U_1+\cdots+F_r(W,X)U_r,
\end{aligned}
$$

所以 $f,g\in\mathbf{Z}[W,T,U][X]$。则 $f,g$ 是关于 $(X)$、系数在 $\mathbf{Z}[W,T,U]$ 中的多项式。可以形成它们的结式

$$
\operatorname{Res}(f,g)\in\mathbf{Z}[W,T,U].
$$

因此 $\operatorname{Res}(f,g)$ 是关于变量 $(T,U)$、系数在 $\mathbf{Z}[W]$ 中的多项式。用 $(Q_\mu(W))$ 表示这个多项式的系数组成的族。

**命题 4.3。** *刚刚构造的系统 $\{Q_\mu(W)\}$ 满足定理 4.1 的性质，即它是次数相同、均为 $d$ 的 $r$ 个型的一个结式系统。*

*证明。* 假定特定方程组 $F_j(W,X)=0$ 有非平凡解，其中 $(w)$ 在某个域 $k$ 中。则 $(w,T,U)$ 是 $f,g$ 的一个公共非平凡零点，所以 $\operatorname{Res}(f,g)=0$，因而对所有 $\mu$ 有 $Q_\mu(w)=0$。反过来，假定对所有 $\mu$ 有 $Q_\mu(w)=0$。令 $f_i(X)=F_i(w,X)$。我们希望证明，对于 $i=1,\ldots,r$，$f_i(X)$ 在<span class="original-page-anchor" id="pdf-page-418" aria-hidden="true"></span>$k$ 的某个扩张中有公共非平凡零点。如果所有 $f_i$ 在 $k[X_1,X_2]$ 中都为 $0$，则它们有公共非平凡零点。如果例如 $f_1$ 在 $k[X]$ 中非零，那么在结式 $\operatorname{Res}(f,g)$ 中将 $T_2,\ldots,T_r$ 特化为 $0$，将 $T_1$ 特化为 $1$，可知

$$
\operatorname{Res}(f_1,f_2U_2+\cdots+f_rU_r)=0
$$

作为 $k[U_2,\ldots,U_r]$ 中的多项式成立。必要时取 $k$ 的有限扩张后，可以假定 $f_1(X)$ 分裂为线性因子。设 $\{\alpha_i\}$ 为 $f_1(X_1,1)$ 的根。则某个 $(\alpha_i,1)$ 也必定是 $f_2U_2+\cdots+f_rU_r$ 的零点；由于 $U_2,\ldots,U_r$ 在 $k$ 上代数独立，这意味着 $(\alpha_i,1)$ 是 $f_1,\ldots,f_r$ 的公共零点。这就证明了命题 4.3。

> **译校注。** 这里用 $(\alpha_i,1)$ 表示根的步骤是在 $X_2\ne0$ 的仿射片中进行的。一般情形还须计入射影点 $(1,0)$，例如 $f_1=\cdots=f_r=X_2^d$ 有公共非平凡零点 $(1,0)$，而 $f_1(X_1,1)=1$ 没有根。将 $f_1$ 的齐次线性因子对应的所有射影零点（包括 $(1,0)$）一并纳入，利用齐次结式的乘积性质及 $U_2,\ldots,U_r$ 的代数独立性，就得到相同的结论。此处保留原书的仿射表述。

现在可以在 $n>2$ 时进行归纳步骤。再次令

$$
f_i(X)=F_i(w,X)\text{，其中 }j=1,\ldots,r,
$$

为系数 $(w)$ 在某个域 $k$ 中的多项式。

**注 4.4。** *方程组*

$$
f_i=0\quad(i=1,\ldots,r)
$$

*在 $k$ 的某个扩张中有非平凡零点，当且仅当在 $k$ 的某个扩张中存在*

$$
(x_1,\ldots,x_{n-1})\ne(0,\ldots,0)\quad\text{且}\quad(x_n,t)\ne(0,0),
$$

*使得*

$$
f_i(tx_1,\ldots,tx_{n-1},x_n)=0\text{ 对 }i=1,\ldots,r\text{ 成立}.
$$

因此，现在可以如下归纳地构造系统 $(R_\rho)$。

设 $T$ 是新变量，令 $X^{(n-1)}=(X_1,\ldots,X_{n-1})$。令

$$
g_i(W,X^{(n-1)},S_n,T)=F_i(W,TX_1,\ldots,TX_{n-1},X_n)\in\mathbf{Z}[W,X^{(n-1)}][X_n,T].
$$

> **译校注。** 原书在左边第三个自变量处印作 $S_n$。定义式以及随后的论证始终使用变量 $X_n$，所以此处应为 $X_n$。

则 $g_i$ 关于两个变量 $(X_n,T)$ 齐次。由两个变量的定理，存在 $\mathbf{Z}[W,X^{(n-1)}]$ 中的多项式系统 $(Q_\mu)$，具有如下性质：*如果 $(w,x^{(n-1)})$ 是域 $K$ 中的点，则*

*$g_i(w,x^{(n-1)},X_n,T)$ 对 $i=1,\ldots,r$ 有非平凡公共零点*

$$
\Longleftrightarrow Q_\mu(w,x^{(n-1)})=0\text{ 对所有 }\mu\text{ 成立}.
$$

将每个 $Q_\mu$ 视为关于变量 $(X^{(n-1)})$ 的多项式，将它分解为齐次项的和，并令 $(H_\lambda(W,X^{(n-1)}))$ 为这些多项式组成的族，它们关于 $(X^{(n-1)})$ 齐次。由型 $F_j$ 关于 $(X)$ 的齐次性可知，如果 $t$ 在 $K$ 上超越，且 $g_i(w,x^{(n-1)},X_n,T)$ 对 $j=1,\ldots,r$ 有非平凡公共零点，则 $g_i(w,tx^{(n-1)},X_n,T)$ 也有非平凡公共零点。因此<span class="original-page-anchor" id="pdf-page-419" aria-hidden="true"></span>对所有 $\mu$ 都有 $Q_\mu(w,tx^{(n-1)})=0$，所以 $H_\lambda(w,x^{(n-1)})=0$。因此可以用多项式族 $(H_\lambda)$ 代替 $(Q_\mu)$，并得到如下性质：*如果 $(w,x^{(n-1)})$ 是域 $K$ 中的点，则*

*$g_i(w,x^{(n-1)},X_n,T)$ 对 $i=1,\ldots,r$ 有非平凡公共零点*

$$
\Longleftrightarrow H_\lambda(w,x^{(n-1)})=0\text{ 对所有 }\lambda\text{ 成立}.
$$

对 $n$ 作归纳，存在 $\mathbf{Z}[W]$ 中的多项式族 $(R_\rho(W))$（实际上是齐次的），具有如下性质：*如果 $(w)$ 是域 $K$ 中的点，则*

*$H_\lambda(w,X^{(n-1)})$ 对所有 $\lambda$ 有非平凡公共零点*

$$
\Longleftrightarrow R_\rho(w)=0\text{ 对所有 }\rho\text{ 成立}.
$$

结合注 4.4，这就通过结式方法完成了定理 4.1 的证明。

## §5. 环的谱

我们将 §2 的概念推广到任意交换环。

设 $A$ 是交换环。用 $\operatorname{spec}(A)$ 表示 $A$ 的所有素理想组成的集合。$\operatorname{spec}(A)$ 的一个元素也称为 $\operatorname{spec}(A)$ 的一个**点**。

如果 $f\in A$，就将 $\operatorname{spec}(A)$ 中包含 $f$ 的素理想 $\mathfrak{p}$ 所组成的集合，视为 $f$ 的**零点**集。事实上，它正是使 $f$ 在典范同态

$$
A\to A/\mathfrak{p}
$$

下的像为 $0$ 的 $\mathfrak{p}$ 的集合。设 $\mathfrak{a}$ 是理想，令 $\mathcal{L}(\mathfrak{a})$（$\mathfrak{a}$ 的零点集）为 $A$ 的所有包含 $\mathfrak{a}$ 的素理想组成的集合。设 $\mathfrak{a},\mathfrak{b}$ 是理想。则有：

**命题 5.1。**

(i) $\mathcal{L}(\mathfrak{a}\mathfrak{b})=\mathcal{L}(\mathfrak{a})\cup\mathcal{L}(\mathfrak{b})$。

(ii) *如果 $\{\mathfrak{a}_i\}$ 是一族理想，则 $\mathcal{L}(\sum\mathfrak{a}_i)=\bigcap\mathcal{L}(\mathfrak{a}_i)$。*

(iii) *$\mathcal{L}(\mathfrak{a})\subset\mathcal{L}(\mathfrak{b})$ 当且仅当 $\operatorname{rad}(\mathfrak{a})\supset\operatorname{rad}(\mathfrak{b})$，其中 $\mathfrak{a}$ 的根理想 $\operatorname{rad}(\mathfrak{a})$ 是所有满足对某个正整数 $n$ 有 $x^n\in\mathfrak{a}$ 的元素 $x\in A$ 组成的集合。*

*证明。* 留作练习。参见第 X 章推论 2.3。

如果存在 $A$ 的理想 $\mathfrak{a}$，使得 $C$ 由满足 $\mathfrak{a}\subset\mathfrak{p}$ 的素理想 $\mathfrak{p}$ 组成，就称 $\operatorname{spec}(A)$ 的子集 $C$ 为**闭**的。$\operatorname{spec}(A)$ 的闭子集的补集称为 $\operatorname{spec}(A)$ 的**开子集**。下列断言都很容易验证，将留给读者。

<span class="original-page-anchor" id="pdf-page-420" aria-hidden="true"></span>

**命题 5.2。** *有限个闭集的并是闭的。任意闭集族的交是闭的。*

*有限个开集的交是开的。任意开集族的并是开的。*

*空集和 $\operatorname{spec}(A)$ 本身都是既开又闭的。*

如果 $S$ 是 $A$ 的子集，则使 $S\subset\mathfrak{p}$ 的素理想 $\mathfrak{p}\in\operatorname{spec}(A)$ 组成的集合，与包含由 $S$ 生成的理想的素理想 $\mathfrak{p}$ 组成的集合相同。

命题 5.2 中的开集族称为 $\operatorname{spec}(A)$ 上的一个**拓扑**，称为**扎里斯基拓扑**。

**注。** 在分析中，考虑紧豪斯多夫空间 $S$。“豪斯多夫”意味着，给定两点 $P,Q$，存在分别包含 $P,Q$ 的不相交开集 $U_P,U_Q$。在当前的代数背景中，这个拓扑不是豪斯多夫的。在分析背景中，设 $R$ 为 $S$ 上的复值连续函数环。则 $R$ 的极大理想与 $S$ 中的点一一对应（盖尔范德–奈马克定理）。对每个点 $P\in S$，对应由满足 $f(P)=0$ 的函数 $f$ 组成的理想 $M_P$。对应 $P\mapsto M_P$ 给出这个双射。在复解析情形中也有类似结果。一个非平凡的例子见第 XII 章练习 19。

设 $A,B$ 是交换环，$\varphi:A\to B$ 是同态。则 $\varphi$ 诱导映射

$$
\varphi^*=\operatorname{spec}(\varphi)=\varphi^{-1}:\operatorname{spec}(B)\to\operatorname{spec}(A),
$$

由

$$
\mathfrak{p}\mapsto\varphi^{-1}(\mathfrak{p})
$$

给出。事实上，可以立即验证 $\varphi^{-1}(\mathfrak{p})$ 是 $A$ 的素理想。不过注意，$B$ 的极大理想的逆像未必是 $A$ 的极大理想。举一个例子？读者将立即验证 $\operatorname{spec}(\varphi)$ 连续，意思是如果 $U$ 在 $\operatorname{spec}(B)$ 中开，则 $\varphi^{-1}(U)$ 在 $\operatorname{spec}(A)$ 中开。

> **译校注。** 原书在关于连续性的句子中将两个空间的方向颠倒了。对于 $\varphi^*:\operatorname{spec}(B)\to\operatorname{spec}(A)$，连续性指：开集 $U\subset\operatorname{spec}(A)$ 的逆像 $(\varphi^*)^{-1}(U)\subset\operatorname{spec}(B)$ 是开的。这也区分了拓扑映射 $\varphi^*$ 下集合的逆像与环映射 $\varphi$ 下理想的逆像。

于是可以将 $\operatorname{spec}$ 视为从交换环范畴到拓扑空间范畴的反变函子。

所谓 $\operatorname{spec}(A)$ **在域** $L$ 中的一个**点**，是指由从 $A$ 到 $L$ 的同态 $\varphi:A\to L$ 诱导的映射

$$
\operatorname{spec}(\varphi):\operatorname{spec}(L)\to\operatorname{spec}(A).
$$

例如，对每个素数 $p$，由约化映射

$$
\mathbf{Z}\to\mathbf{Z}/p\mathbf{Z}
$$

得到 $\operatorname{spec}(\mathbf{Z})$ 的一个点。

<span class="original-page-anchor" id="pdf-page-421" aria-hidden="true"></span>

相应的点由反向箭头给出，

$$
\operatorname{spec}(\mathbf{Z})\leftarrow\operatorname{spec}(\mathbf{Z}/p\mathbf{Z}).
$$

再举一个例子，考虑域 $k$ 上的多项式环 $k[X_1,\ldots,X_n]$。$k^{a(n)}$ 中的每个 $n$ 元组 $(c_1,\ldots,c_n)$ 都给出同态

$$
\varphi:k[X_1,\ldots,X_n]\to k^a,
$$

使得 $\varphi$ 在 $k$ 上为恒等映射，且对所有 $i$ 有 $\varphi(X_i)=c_i$。相应的点由反向箭头给出，

$$
\operatorname{spec}k[X]\leftarrow\operatorname{spec}(k^a).
$$

因此可以将 $n$ 维空间 $k^{a(n)}$ 中的点，与 $\operatorname{spec}k[X]$ 在 $k^a$ 中（在 $k$ 上）的点等同。

不过，我们并不想只取 $k$ 的代数闭包中的点，而且当然可以处理 $k$ 上任意簇 $V$ 的情形，而不只是整个仿射 $n$ 维空间。因此，设 $k[x_1,\ldots,x_n]$ 是 $k$ 上的有限生成整环，并选定一族生成元。设 $V=\operatorname{spec}k[x]$。设 $A$ 是交换 $k$-代数，对应于同态 $k\to A$。则 $V$ 在 $A$ 中的一个点，既可以描述为同态

$$
\varphi:k[x_1,\ldots,x_n]\to A,
$$

也可以描述为与该同态对应的反向箭头

$$
\operatorname{spec}(A)\to\operatorname{spec}(k[x]).
$$

如果令 $c_i=\varphi(x_i)$，就可以称 $(c)=(c_1,\ldots,c_n)$ 为 **$A$ 中该点的坐标**。所谓 $V$ 在域 $K$ 中的一个**泛点**，是指使映射 $\varphi:k[x]\to K$ 为单射的点，即 $k[x]$ 与 $K$ 的某个子环之间的同构。

设 $A$ 是交换诺特环。下述断言将诺特条件转换为扎里斯基拓扑中闭集的性质，其验证留作练习。

$\operatorname{spec}(A)$ 的闭子集满足**降链条件**，即如果

$$
C_1\supset C_2\supset C_3\supset\cdots
$$

是闭集的降链，则对所有充分大的 $n$，有 $C_n=C_{n+1}$。等价地，设 $\{C_i\}_{i\in I}$ 是一族闭集。则这个族有一个相对极小元素，即族中一个闭集 $C_{i_0}$，使得对所有 $i$，如果 $C_i\subset C_{i_0}$，则 $C_i=C_{i_0}$。证明由理想的相应性质，以及将闭集的并、交与理想的积、和联系起来的简单形式规则立即得出。

<span class="original-page-anchor" id="pdf-page-422" aria-hidden="true"></span>

如果闭集 $C$ 不能表示成两个闭集的并，即对于 $C_1\ne C$ 和 $C_2\ne C$ 有

$$
C\ne C_1\cup C_2,
$$

就称 $C$ 为**不可约**的。

**定理 5.3。** *设 $A$ 是诺特交换环。则每个闭集 $C$ 都可以表示为有限个不可约闭集的并，而且如果在不可约闭集的并*

$$
C=C_1\cup\cdots\cup C_r
$$

*中，当 $i\ne j$ 时 $C_i\not\subset C_j$，则这种表示唯一。*

*证明。* 我们给出这个证明作为例子，说明定理 2.2 的版本如何立即转换到 $\operatorname{spec}(A)$ 的更一般背景中。假定不能表示为有限个不可约闭集的并的闭集族非空。将诺特假设转换到这种情形，可知存在一个这样的极小集 $C$。则 $C$ 不可能不可约，可以将 $C$ 写成闭集的并

$$
C=C'\cup C'',
$$

其中 $C'\ne C$ 且 $C''\ne C$。由于 $C'$ 和 $C''$ 都严格小于 $C$，可以将 $C'$ 和 $C''$ 表示为有限个不可约闭集的并，从而得到 $C$ 的类似表示，产生矛盾，证明了存在性。

关于唯一性，设

$$
C=C_1\cup\cdots\cup C_r=Z_1\cup\cdots\cup Z_s
$$

是将 $C$ 表示为没有包含关系的不可约闭集之并的表示。对每个 $Z_j$，可以写成

$$
Z_j=(Z_j\cap C_1)\cup\cdots\cup(Z_j\cap C_r).
$$

由于每个 $Z_j\cap C_i$ 是闭集，必定对某个 $i$ 有 $Z_j=Z_j\cap C_i$。因此对某个 $i$ 有 $Z_j=C_i$。类似地，$C_i$ 包含于某个 $Z_k$ 中。由于各 $Z_j$ 之间没有包含关系，必定有 $Z_j=C_i=Z_k$。对每个 $Z_j$ 和每个 $C_i$ 都可以进行这一论证。这表明每个 $Z_j$ 都出现在各 $C_i$ 中，每个 $C_i$ 都出现在各 $Z_j$ 中，从而证明了表示的唯一性。定理得证。

> **译校注。** 第一个“因此”处，原书印作 $Z_j=C_i$。由 $Z_j=Z_j\cap C_i$ 立即得到的是 $Z_j\subset C_i$；等号要在随后利用 $C_i\subset Z_k$ 以及不同 $Z_j$ 之间没有包含关系的论证之后才成立。

**命题 5.4。** *设 $C$ 是 $\operatorname{spec}(A)$ 的闭子集。则 $C$ 不可约，当且仅当对某个素理想 $\mathfrak{p}$ 有 $C=\mathcal{L}(\mathfrak{p})$。*

*证明。* 留作练习。

同样基础程度的更多性质将在练习 14–19 中给出。

<span class="original-page-anchor" id="pdf-page-423" aria-hidden="true"></span>

## 习题

### 整性

**1.** （Hilbert-Zariski）设 $k$ 是一个域，$V$ 是一个齐次簇，其在 $k$ 上的泛点为 $(x)$。设 $\mathcal L$ 是由 $k[X]$ 中的型 $f_1,\ldots,f_r$ 生成的齐次理想在 $k^a$ 中的零点代数集。证明：$V\cap\mathcal L$ 只有平凡零点，当且仅当每个 $x_i$ 都在环 $k[f(x)]=k[f_1(x),\ldots,f_r(x)]$ 上整。（比较第 VII 章定理 3.7。）

**2.** 设 $f_1,\ldots,f_r$ 是 $n$ 个变量的型，并设 $n>r$。证明这些型有一个非平凡的公共零点。

**3.** 设 $R$ 是一个整环。证明：$R$ 整闭，当且仅当对于每个素理想 $\mathfrak p$，局部环 $R_{\mathfrak p}$ 都整闭。

**4.** 设 $R$ 是一个整环，分式域为 $K$。设 $t$ 在 $K$ 上超越。设 $f(t)=\sum a_it^i\in K[t]$。证明：

(a) 若 $f(t)$ 在 $R[t]$ 上整，则所有 $a_i$ 都在 $R$ 上整。

(b) 若 $R$ 整闭，则 $R[t]$ 整闭。

在以下习题中，令 $R=k[x]=k[X]/\mathfrak p$，其中 $\mathfrak p$ 是一个齐次素理想。于是 $(x)$ 是一个 $k$-簇 $V$ 的齐次泛点。令 $I$ 为 $R$ 在 $k(x)$ 中的整闭包。为简单起见，假设 $k(x)$ 是 $k$ 的正则扩张。

**5.** 设 $z=\sum c_ix_i$，其中 $c_i\in k$，且 $z\ne0$。若 $k[x]$ 整闭，证明 $k[x/z]$ 整闭。

**6.** 若对于在 $k(x)$ 上超越的 $t$ 以及某个整数 $d$，有 $f(tx)=t^df(x)$，则称元素 $f\in k(x)$ 是**齐次的**。设 $f\in I$。证明 $f$ 可以写成 $f=\sum f_i$ 的形式，其中每个 $f_i$ 都是次数为 $i\ge0$ 的齐次元素，并且还有 $f_i\in I$。（当然，某些 $f_i$ 可以为 $0$。）

令 $R_m$ 表示 $R$ 中次数为 $m$ 的齐次元素的集合。$I_m$ 的定义类似。注意，$R_m$ 和 $I_m$ 都是 $k$ 上的向量空间，并且 $R$（相应地，$I$）是所有空间 $R_m$（相应地，$I_m$）在 $m=0,1,\ldots$ 时的直和。这一点对 $R$ 是显然的；由习题 6，它对 $I$ 也成立。

**7.** 证明 $I$ 可以写成和 $I=Rz_1+\cdots+Rz_s$，其中每个 $z_i$ 都是某个次数 $d_i$ 的齐次元素。

**8.** 若对于所有整数 $q\ge1$ 都有 $I_m^q=I_{qm}$，则称整数 $m\ge1$ 是**良好的**。若 $R=I$，则所有 $m$ 都是良好的。在习题 7 中，假设 $m\ge\max d_i$。证明 $m$ 是良好的。

**9.** (a) 证明 $I_m$ 是 $k$ 上的有限维向量空间。设 $w_0,\ldots,w_M$ 是 $I_m$ 在 $k$ 上的一组基。于是 $k[I_m]=k[w]$。

(b) 若 $m$ 是良好的，证明 $k[I_m]$ 整闭。

(c) 用 $k((x))$ 表示由所有满足 $x_j\ne0$ 的商 $x_i/x_j$ 在 $k$ 上生成的域，$k((w))$ 的定义类似。证明 $k((x))=k((w))$。

（若想看习题 4–9 的解答，可参阅我的 *Introduction to Algebraic Geometry*，Interscience，1958 年，第 V 章。）

<span class="original-page-anchor" id="pdf-page-424" aria-hidden="true"></span>

### 结式

**10.** 证明 §3 中为 $n$ 个变量的 $n$ 个型所定义的结式，实际上与第 IV 章中的结式一致；当 $n=2$ 时，也与 §4 中的结式一致。

**11.** 设 $\mathfrak a=(f_1,\ldots,f_r)$ 是 $k[X_1,\ldots,X_n]$ 中的一个齐次理想（其中 $k$ 代数闭）。假设 $\mathfrak a$ 的零点仅由射影空间 $\mathbf P^{n-1}$ 中的有限个点 $(x^{(1)}),\ldots,(x^{(d)})$ 组成，因此每个 $x^{(j)}$ 的坐标都可取在 $k$ 中。设 $u_1,\ldots,u_n$ 是独立变量，并令

$$
L_u(X)=u_1X_1+\cdots+u_nX_n.
$$

设 $R_1(u),\ldots,R_s(u)\in k[u]$ 是 $f_1,\ldots,f_r,L_u$ 的一个结式系统。

(a) 证明 $R_i(u)$ $(i=1,\ldots,s)$ 这一组在 $k$ 中的非平凡公共零点，就是多项式

$$
\prod_j L_u(x^{(j)})\in k[u]
$$

的零点。

(b) 设 $D(u)$ 是 $R_1(u),\ldots,R_s(u)$ 在 $k[u]$ 中的最大公因子。证明存在整数 $m_j\ge1$，使得（允许相差一个 $k$ 中的因子）

$$
D(u)=\prod_{j=1}^d L_u(x^{(j)})^{m_j}.
$$

［参阅 van der Waerden，*Moderne Algebra*，第二版，第二卷，§79。］

**12.** 对于 $2$ 个变量的型，直接从 §4 中使用的定义证明

$$
\operatorname{Res}(fg,h)=\operatorname{Res}(f,h)\operatorname{Res}(g,h)
$$

$$
\operatorname{Res}(f,g)=(-1)^{(\deg f)(\deg g)}\operatorname{Res}(g,f).
$$

**13.** 设 $k$ 是一个域，$\mathbf Z\longrightarrow k$ 是典范同态。若 $F\in\mathbf Z[W,X]$，用 $\bar F$ 表示 $F$ 在此同态下在 $k[W,X]$ 中的像。这样便得到结式 $R$ 的像 $\bar R$。

(a) 证明 $\bar R$ 是定理 3.5 在域 $k$ 上的素理想 $\mathfrak p_{k,1}$ 的一个生成元。因此可将 $\bar R$ 记为 $R_k$。

(b) 证明 $\bar R$ 绝对不可约，因而 $R_k$ 也绝对不可约。换言之，$R_k$ 在 $k$ 的代数闭包上不可约。

### 环的谱

**14.** 设 $A$ 是一个交换环。若 $\operatorname{spec}(A)$ 不是两个互不相交的非空闭集的并（或等价地，$\operatorname{spec}(A)$ 不是两个互不相交的非空开集的并），则称 $\operatorname{spec}(A)$ **连通**。

(a) 假设 $A$ 中存在幂等元 $e_1,e_2$（即 $e_1^2=e_1$ 且 $e_2^2=e_2$），它们均不等于 $0,1$，并且满足 $e_1e_2=0$ 及 $e_1+e_2=1$。证明 $\operatorname{spec}(A)$ 不连通。

(b) 反之，若 $\operatorname{spec}(A)$ 不连通，证明存在 (a) 中那样的幂等元。

在任何一种情形下，这些幂等元的存在都等价于环 $A$ 是两个非零环的积，即 $A=A_1\times A_2$。

<span class="original-page-anchor" id="pdf-page-425" aria-hidden="true"></span>

**15.** 证明扎里斯基拓扑是**紧的**，换言之：设 $\{U_i\}_{i\in I}$ 是一族开集，满足

$$
\bigcup_i U_i=\operatorname{spec}(A).
$$

证明存在有限个开集 $U_{i_1},\ldots,U_{i_n}$，它们的并为 $\operatorname{spec}(A)$。［*提示：* 使用闭集，并使用如下事实：若一些理想的和是单位理想，则 $1$ 可以写成有限个元素的和。］

**16.** 设 $f$ 是 $A$ 的一个元素。设 $S$ 是由 $f$ 的幂组成的乘法子集 $\{1,f,f^2,f^3,\ldots\}$。如第 II 章 §3，用 $A_f$ 表示环 $S^{-1}A$。由自然同态 $A\longrightarrow A_f$，可得到相应的映射 $\operatorname{spec}(A_f)\longrightarrow\operatorname{spec}(A)$。

(a) 证明 $\operatorname{spec}(A_f)$ 映满 $\operatorname{spec}(A)$ 中由不是 $f$ 的零点的点组成的开集。

(b) 给定点 $\mathfrak p\in\operatorname{spec}(A)$ 及包含 $\mathfrak p$ 的开集 $U$，证明存在 $f$，使得 $\mathfrak p\in\operatorname{spec}(A_f)\subset U$。

**17.** 设 $U_i=\operatorname{spec}(A_{f_i})$ 是 $\operatorname{spec}(A)$ 的一族有限开子集，它们覆盖 $\operatorname{spec}(A)$。对于每个 $i$，设 $a_i/f_i\in A_{f_i}$。假设将它们视为 $U_i\cap U_j$ 上的函数时，对于所有 $i,j$ 都有 $a_i/f_i=a_j/f_j$。证明存在唯一的元素 $a\in A$，使得对于所有 $i$，在 $A_{f_i}$ 中都有 $a=a_i/f_i$。

**18.** 设 $k$ 是一个域，$k[x_1,\ldots,x_n]=A\subset K$ 是某个扩域 $K$ 的有限生成子环。假设 $k(x_1,\ldots,x_n)$ 的超越次数为 $r$。证明每条素理想极大链

$$
A\supset P_1\supset P_2\supset\cdots\supset P_m\supset\{0\},
$$

其中 $P_1\ne A$、$P_i\ne P_{i+1}$、$P_m\ne\{0\}$，都必须满足 $m=r$。

**19.** 设 $A=\mathbf Z[x_1,\ldots,x_n]$ 是 $\mathbf Z$ 上的有限生成整环。证明习题 18 中的每条素理想极大链都必须满足 $m=r+1$。这里，$r=$ $\mathbf Q(x_1,\ldots,x_n)$ 在 $\mathbf Q$ 上的超越次数。
