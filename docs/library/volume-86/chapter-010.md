---
title: "第十章 诺特环与诺特模"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第九章 代数空间","link":"/library/volume-86/chapter-009"}
next: {"text":"第十一章 实域","link":"/library/volume-86/chapter-011"}
---

# 第十章 诺特环与诺特模

<span class="original-page-anchor" id="pdf-page-426" aria-hidden="true"></span>

本章可以作为代数几何方法的入门，这些方法植根于交换代数和模论，主要是诺特环上的模论。

## §1. 基本判据

设 $A$ 为环，$M$ 为模（即左 $A$ 模）。若 $M$ 满足以下三个条件中的任意一个，就称 $M$ 为**诺特模**：

(1) $M$ 的每个子模都是有限生成的。

(2) $M$ 的每个递增子模序列

$$
M_1\subset M_2\subset M_3\subset\cdots,
$$

若满足 $M_i\ne M_{i+1}$，则必为有限序列。

(3) $M$ 的子模组成的每个非空集合 $S$ 都有极大元（即存在子模 $M_0$，使得对 $S$ 中任何包含 $M_0$ 的元素 $N$，均有 $N=M_0$）。

现在证明上述三个条件等价。

$(1)\Rightarrow(2)$ 假设有上述 $M$ 的递增子模序列。令 $N$ 为所有 $M_i$（$i=1,2,\ldots$）的并。则 $N$ 有限生成，设生成元为 $x_1,\ldots,x_r$，而每个生成元都属于某个 $M_i$。因此存在指标 $j$，使得

$$
x_1,\ldots,x_r\in M_j.
$$

<span class="original-page-anchor" id="pdf-page-427" aria-hidden="true"></span>

于是

$$
\langle x_1,\ldots,x_r\rangle\subset M_j\subset N=\langle x_1,\ldots,x_r\rangle,
$$

从而等号成立，这一蕴含得证。

$(2)\Rightarrow(3)$ 取 $S$ 的一个元素 $N_0$。若 $N_0$ 不是极大元，则它严格包含于一个子模 $N_1$。若 $N_1$ 不是极大元，则它严格包含于一个子模 $N_2$。归纳地，若已找到非极大的 $N_i$，则它严格包含于一个子模 $N_{i+1}$。这样可以构造无限链，这是不可能的。

$(3)\Rightarrow(1)$ 设 $N$ 为 $M$ 的子模，$a_0\in N$。若 $N\ne\langle a_0\rangle$，则存在元素 $a_1\in N$ 不属于 $\langle a_0\rangle$。继续归纳，可以得到 $N$ 的递增子模序列

$$
\langle a_0\rangle\subset\langle a_0,a_1\rangle\subset\langle a_0,a_1,a_2\rangle\subset\cdots,
$$

其中每次包含都是严格的。这些子模组成的集合有极大元，设为子模 $\langle a_0,a_1,\ldots,a_r\rangle$；显然这个有限生成子模必须等于 $N$，得证。

**命题 1.1。** *设 $M$ 为诺特 $A$ 模，则 $M$ 的每个子模和每个商模都是诺特模。*

*证明。* 对子模，这一断言显然成立，例如可由第一个条件得出。对商模，设 $N$ 为子模，$f:M\to M/N$ 为典范同态。设 $\overline M_1\subset\overline M_2\subset\cdots$ 为 $M/N$ 的递增子模链，并令 $M_i=f^{-1}(\overline M_i)$。则 $M_1\subset M_2\subset\cdots$ 为 $M$ 的递增子模链，必有极大元，设为 $M_r$，于是当 $i\ge r$ 时 $M_i=M_r$。又 $f(M_i)=\overline M_i$，故断言成立。

**译校注：** 原文这里印作“$M_i=M_r$ for $r\ge i$”；递增链在第 $r$ 项达到极大元后，其后各项才相等，因此应为 $i\ge r$。

**命题 1.2。** *设 $M$ 为模，$N$ 为子模。假定 $N$ 和 $M/N$ 都是诺特模，则 $M$ 是诺特模。*

*证明。* 对 $M$ 的每个子模 $L$，赋予一对子模

$$
L\mapsto(L\cap N,(L+N)/N).
$$

我们断言：若 $E\subset F$ 为 $M$ 的两个子模，且对应的两对子模相等，则 $E=F$。为此取 $x\in F$。由假设 $(E+N)/N=(F+N)/N$，存在元素 $u,v\in N$，$y\in E$，使 $y+u=x+v$。于是

$$
x-y=u-v\in F\cap N=E\cap N.
$$

因 $y\in E$，故 $x\in E$，断言得证。若有递增序列

$$
E_1\subset E_2\subset\cdots,
$$

<span class="original-page-anchor" id="pdf-page-428" aria-hidden="true"></span>

则对应的两对子模分别构成 $N$ 和 $M/N$ 的递增子模序列，这些序列必定终止。因此，由前面的断言，序列 $E_1\subset E_2\cdots$ 也终止。

命题 1.1 和 1.2 可以概括为：在正合列 $0\to M'\to M\to M''\to0$ 中，$M$ 为诺特模当且仅当 $M'$ 和 $M''$ 都为诺特模。

**推论 1.3。** *设 $M$ 为模，$N,N'$ 为子模。若 $M=N+N'$，且 $N,N'$ 都是诺特模，则 $M$ 是诺特模。诺特模的有限直和是诺特模。*

*证明。* 首先注意，直积 $N\times N'$ 为诺特模，因为它包含子模 $N$，其商模同构于 $N'$，所以可应用命题 1.2。存在满射同态

$$
N\times N'\to M,
$$

把元素对 $(x,x')$（其中 $x\in N$，$x'\in N'$）映为 $x+x'$。由命题 1.1，$M$ 是诺特模。有限积（或和）的情形由归纳法得出。

若环 $A$ 作为自身上的左模是诺特模，则称 $A$ 为**诺特环**。这意味着每个左理想都是有限生成的。

**命题 1.4。** *设 $A$ 为诺特环，$M$ 为有限生成模，则 $M$ 是诺特模。*

*证明。* 设 $x_1,\ldots,x_n$ 为 $M$ 的生成元。存在同态

$$
f:A\times A\times\cdots\times A\to M,
$$

定义在 $A$ 的 $n$ 重积上，使得

$$
f(a_1,\ldots,a_n)=a_1x_1+\cdots+a_nx_n.
$$

这个同态为满射。由前述命题的推论，此积是诺特模，因此由命题 1.1，$M$ 是诺特模。

**命题 1.5。** *设 $A$ 为诺特环，$\varphi:A\to B$ 为满射环同态，则 $B$ 是诺特环。*

*证明。* 设 $\mathfrak b_1\subset\cdots\subset\mathfrak b_n\subset\cdots$ 为 $B$ 的递增左理想链，并令 $\mathfrak a_i=\varphi^{-1}(\mathfrak b_i)$。则 $\mathfrak a_i$ 构成 $A$ 的递增左理想链，必定终止，设终止于 $\mathfrak a_r$。因对所有 $i$ 都有 $\varphi(\mathfrak a_i)=\mathfrak b_i$，命题得证。

**命题 1.6。** *设 $A$ 为交换诺特环，$S$ 为 $A$ 的乘法子集，则 $S^{-1}A$ 是诺特环。*

*证明。* 留作练习。

<span class="original-page-anchor" id="pdf-page-429" aria-hidden="true"></span>

**例。** 第四章给出了诺特环的基本例子，即多项式环和幂级数环。上述命题说明，如何通过取商环、商模或子模，从这些例子构造其他例子。

我们已经提到，为了应用于代数几何，考虑形如 $k[X]/\mathfrak a$ 的商环很有价值，其中 $\mathfrak a$ 为任意理想。由于这个及类似的原因，人们发现应当以模来建立基础，而不只用理想或商环。特别地，我们首先将看到，与不可约代数集相关联的素理想，在模的语言中有相应的概念。还将看到，代数集分解为不可约分支，可以用模自然地表述，即把一个子模表示为准素模的交。

在 §6，我们将应用一些一般概念，得到有限长度模的 Hilbert 多项式，并讨论如何以几何概念解释它。因此，本章的部分目的，是在基础代数与代数几何之间架起桥梁。

## §2. 伴随素理想

*本节始终设 $A$ 为交换环。除非另有说明，模与同态均指 $A$ 模与 $A$ 同态。*

**命题 2.1。** *设 $S$ 为 $A$ 的乘法子集，且 $S$ 不含 $0$。则存在 $A$ 的一个理想，在不与 $S$ 相交的理想集合中极大；任何这样的理想都是素理想。*

*证明。* 这样的理想 $\mathfrak p$ 的存在性由 Zorn 引理得出（不与 $S$ 相交的理想集合非空，因为它包含零理想，而且显然归纳有序）。设 $\mathfrak p$ 在此集合中极大。设 $a,b\in A$，$ab\in\mathfrak p$，但 $a\notin\mathfrak p$ 且 $b\notin\mathfrak p$。由假设，分别由 $a$ 与 $\mathfrak p$、以及 $b$ 与 $\mathfrak p$ 生成的理想 $(a,\mathfrak p)$ 和 $(b,\mathfrak p)$ 都与 $S$ 相交。因此存在元素 $s,s'\in S$，$c,c',x,x'\in A$，$p,p'\in\mathfrak p$，使得

$$
s=ca+xp\qquad\text{以及}\qquad s'=c'b+x'p'.
$$

将两个式子相乘，得到

$$
ss'=cc'ab+p'',
$$

其中 $p''\in\mathfrak p$，所以 $ss'$ 属于 $\mathfrak p$。这与 $\mathfrak p$ 不与 $S$ 相交矛盾，故 $\mathfrak p$ 是素理想。

若存在整数 $n\ge1$，使 $a^n=0$，则称 $A$ 的元素 $a$ 为**幂零元**。

<span class="original-page-anchor" id="pdf-page-430" aria-hidden="true"></span>

**推论 2.2。** *$A$ 的元素 $a$ 为幂零元，当且仅当它属于 $A$ 的每个素理想。*

*证明。* 若 $a^n=0$，则对每个素理想 $\mathfrak p$ 都有 $a^n\in\mathfrak p$，故 $a\in\mathfrak p$。若对任意正整数 $n$ 都有 $a^n\ne0$，令 $S$ 为 $a$ 的幂组成的乘法子集，即 $\{1,a,a^2,\ldots\}$，再像命题中那样找到一个素理想，即可证明逆命题。

设 $\mathfrak a$ 为 $A$ 的理想。$\mathfrak a$ 的**根理想**是所有满足某个整数 $n\ge1$ 下 $a^n\in\mathfrak a$ 的元素 $a\in A$ 组成的集合（等价地，它由在商环 $A/\mathfrak a$ 中的像为幂零元的元素 $a\in A$ 组成）。注意，$\mathfrak a$ 的根理想是理想，因为若 $a^n=0$ 且 $b^m=0$，则当 $k$ 足够大时 $(a+b)^k=0$：在二项式展开中，$a$ 或 $b$ 必定以至少等于 $n$ 或 $m$ 的幂出现。

**推论 2.3。** *$A$ 的元素 $a$ 属于理想 $\mathfrak a$ 的根理想，当且仅当它属于每个包含 $\mathfrak a$ 的素理想。*

*证明。* 推论 2.3 等价于将推论 2.2 应用于环 $A/\mathfrak a$。

我们将把推论 2.2 推广到模。先讨论局部化。设 $S$ 为 $A$ 的乘法子集。若 $M$ 为模，可以像定义 $S^{-1}A$ 那样定义 $S^{-1}M$。考虑元素对 $(x,s)$ 的等价类，其中 $x\in M$，$s\in S$；若存在 $s_1\in S$ 使 $s_1(s'x-sx')=0$，则称 $(x,s)$ 与 $(x',s')$ 等价。用 $x/s$ 表示 $(x,s)$ 的等价类，立即可验证，等价类的集合在显然的运算下是加法群。实际上，它在运算

$$
(a,x/s)\mapsto ax/s
$$

下是 $A$ 模。

把这个等价类模记作 $S^{-1}M$。（注意，$S^{-1}M$ 也可看作 $S^{-1}A$ 模。）

若 $\mathfrak p$ 为 $A$ 的素理想，$S$ 为 $\mathfrak p$ 在 $A$ 中的补集，则 $S^{-1}M$ 也记作 $M_{\mathfrak p}$。

由定义显然可知，若 $N\to M$ 为单射同态，则存在自然单射 $S^{-1}N\to S^{-1}M$。换言之，若 $N$ 为 $M$ 的子模，则 $S^{-1}N$ 可看作 $S^{-1}M$ 的子模。若 $x\in N$，$s\in S$，则分式 $x/s$ 可看作 $S^{-1}N$ 或 $S^{-1}M$ 的元素。若在 $S^{-1}M$ 中 $x/s=0$，则存在 $s_1\in S$ 使 $s_1x=0$，这意味着在 $S^{-1}N$ 中 $x/s$ 也为 $0$。因此，若 $\mathfrak p$ 为素理想，$N$ 为 $M$ 的子模，则有 $N_{\mathfrak p}$ 到 $M_{\mathfrak p}$ 的自然包含。我们将把 $N_{\mathfrak p}$ 等同于 $M_{\mathfrak p}$ 的子模。特别地，$M_{\mathfrak p}$ 是其子模 $(Ax)_{\mathfrak p}$（$x\in M$）的和，当然通常不是直和。

设 $x\in M$。$x$ 的**零化理想** $\mathfrak a$ 是由所有满足 $ax=0$ 的元素 $a\in A$ 组成的理想。有模的同构

$$
A/\mathfrak a\xrightarrow{\approx}Ax,
$$

<span class="original-page-anchor" id="pdf-page-431" aria-hidden="true"></span>

由映射

$$
a\to ax
$$

给出。

**引理 2.4。** *设 $x$ 为模 $M$ 的元素，$\mathfrak a$ 为其零化理想，$\mathfrak p$ 为 $A$ 的素理想。则 $(Ax)_{\mathfrak p}\ne0$ 当且仅当 $\mathfrak p$ 包含 $\mathfrak a$。*

*证明。* 此引理由定义直接得出，留给读者。

设 $a$ 为 $A$ 的元素，$M$ 为模。同态

$$
x\mapsto ax,\qquad x\in M
$$

称为与 $a$ 相关联的**主同态**，记作 $a_M$。若对每个 $x\in M$，都存在整数 $n(x)\ge1$ 使 $a^{n(x)}x=0$，则称 $a_M$ 为**局部幂零**的。这一条件蕴含：对 $M$ 的每个有限生成子模 $N$，存在整数 $n\ge1$ 使 $a^nN=0$；只须取零化 $N$ 的有限个生成元所需的 $a$ 的最大幂次作为 $n$。因此，*若 $M$ 有限生成，则 $a_M$ 局部幂零当且仅当它幂零*。

**命题 2.5。** *设 $M$ 为模，$a\in A$。则 $a_M$ 局部幂零，当且仅当 $a$ 属于每个满足 $M_{\mathfrak p}\ne0$ 的素理想 $\mathfrak p$。*

*证明。* 假设 $a_M$ 局部幂零。设 $\mathfrak p$ 为 $A$ 的素理想，且 $M_{\mathfrak p}\ne0$。则存在 $x\in M$ 使 $(Ax)_{\mathfrak p}\ne0$。取正整数 $n$ 使 $a^nx=0$，并设 $\mathfrak a$ 为 $x$ 的零化理想。则 $a^n\in\mathfrak a$，故可以应用引理和推论 2.3，得出 $a$ 属于每个满足 $M_{\mathfrak p}\ne0$ 的素理想 $\mathfrak p$。反过来，假设 $a_M$ 不局部幂零，则存在 $x\in M$ 使对所有 $n\ge0$ 都有 $a^nx\ne0$。令 $S=\{1,a,a^2,\ldots\}$，利用命题 2.1，取一个不与 $S$ 相交的素理想 $\mathfrak p$。则 $(Ax)_{\mathfrak p}\ne0$，从而 $M_{\mathfrak p}\ne0$ 且 $a\notin\mathfrak p$，得证。

**译校注：** 原文引用“Corollary 4.3”，此处所用的是本节推论 2.3。原文在逆向证明中印作“$a^nx=0$ for all $n\ge0$”；这与“不局部幂零”及 $n=0$ 时 $x\ne0$ 矛盾，应为 $a^nx\ne0$。此外，这里应用命题 2.1 时，须选取包含 $\operatorname{Ann}(x)$ 且不与 $S$ 相交的素理想，即在 $A/\operatorname{Ann}(x)$ 中应用该命题后取逆像，才能由引理 2.4 得到 $(Ax)_{\mathfrak p}\ne0$。

设 $M$ 为模。若存在元素 $x\in M$，使 $\mathfrak p$ 为 $x$ 的零化理想，则称 $A$ 的素理想 $\mathfrak p$ 与 $M$ **伴随**。特别地，由于 $\mathfrak p\ne A$，必有 $x\ne0$。

**命题 2.6。** *设 $M$ 为非零模。设 $\mathfrak p$ 在非零元素 $x\in M$ 的零化理想所组成的理想集合中为极大元，则 $\mathfrak p$ 是素理想。*

*证明。* 设 $\mathfrak p$ 为元素 $x\ne0$ 的零化理想，则 $\mathfrak p\ne A$。设 $a,b\in A$，$ab\in\mathfrak p$，$a\notin\mathfrak p$。则 $ax\ne0$。但理想 $(b,\mathfrak p)$ 零化 $ax$，且包含 $\mathfrak p$。因 $\mathfrak p$ 极大，故 $b\in\mathfrak p$，所以 $\mathfrak p$ 是素理想。

**推论 2.7。** *若 $A$ 为诺特环，$M$ 为非零模，则存在与 $M$ 伴随的素理想。*

*证明。* 因 $M\ne0$，命题 2.6 中的理想集合非空；又因 $A$ 为诺特环，它有极大元。

<span class="original-page-anchor" id="pdf-page-432" aria-hidden="true"></span>

**推论 2.8。** *假定 $A$ 和 $M$ 都是诺特的，且 $M\ne0$。则存在子模序列*

$$
M=M_1\supset M_2\supset\cdots\supset M_r=0,
$$

*使每个商模 $M_i/M_{i+1}$ 都同构于某个素理想 $\mathfrak p_i$ 对应的 $A/\mathfrak p_i$。*

*证明。* 考虑满足推论所述性质的子模集合。它非空，因为 $M$ 存在伴随素理想 $\mathfrak p$，若 $\mathfrak p$ 为 $x$ 的零化理想，则 $Ax\approx A/\mathfrak p$。设 $N$ 为这个集合的极大元。若 $N\ne M$，则将前述论证应用于 $M/N$，得到 $M$ 的子模 $N'$，它包含 $N$，且 $N'/N$ 同构于某个 $A/\mathfrak p$，这与 $N$ 的极大性矛盾。

**命题 2.9。** *设 $A$ 为诺特环，$a\in A$，$M$ 为模。则 $a_M$ 为单射，当且仅当 $a$ 不属于 $M$ 的任何伴随素理想。*

*证明。* 假设 $a_M$ 不是单射，则对某个 $x\in M$，$x\ne0$，有 $ax=0$。由推论 2.7，$Ax$ 存在伴随素理想 $\mathfrak p$，而 $a$ 属于 $\mathfrak p$。反过来，若 $a_M$ 为单射，则 $a$ 不能属于任何伴随素理想，因为 $a$ 不零化 $M$ 的任何非零元素。

**命题 2.10。** *设 $A$ 为诺特环，$M$ 为模，$a\in A$。以下条件等价：*

(i) *$a_M$ 局部幂零。*

(ii) *$a$ 属于 $M$ 的每个伴随素理想。*

(iii) *$a$ 属于每个满足 $M_{\mathfrak p}\ne0$ 的素理想 $\mathfrak p$。*

*若 $\mathfrak p$ 为满足 $M_{\mathfrak p}\ne0$ 的素理想，则 $\mathfrak p$ 包含 $M$ 的一个伴随素理想。*

*证明。* (i) 蕴含 (ii) 由定义显然成立，不需要 $A$ 为诺特环的假设。(iii) 蕴含 (i) 也不需要这一假设，命题 2.5 已经证明了它。因此只须证明 (ii) 蕴含 (iii)，而最后一个断言实际上蕴含这一点。该断言证明如下。设 $\mathfrak p$ 为满足 $M_{\mathfrak p}\ne0$ 的素理想，则存在 $x\in M$ 使 $(Ax)_{\mathfrak p}\ne0$。由推论 2.7，$(Ax)_{\mathfrak p}$ 在 $A$ 中存在伴随素理想 $\mathfrak q$。因此存在 $(Ax)_{\mathfrak p}$ 的元素 $y/s$，其中 $y\in Ax$，$s\notin\mathfrak p$，$y/s\ne0$，使 $\mathfrak q$ 为 $y/s$ 的零化理想。可得 $\mathfrak q\subset\mathfrak p$，否则存在 $b\in\mathfrak q$，$b\notin\mathfrak p$，且 $0=by/s$，从而 $y/s=0$，矛盾。设 $b_1,\ldots,b_n$ 为 $\mathfrak q$ 的生成元。对每个 $i$，因 $b_i y/s=0$，存在 $s_i\in A$，$s_i\notin\mathfrak p$，使 $s_i b_i y=0$。令 $t=s_1\cdots s_n$，容易验证，$\mathfrak q$ 为 $ty$ 在 $A$ 中的零化理想。因此 $\mathfrak q\subset\mathfrak p$，得证。

定义 $M$ 的**支集**为

$$
\operatorname{supp}(M)=\text{所有满足 }M_{\mathfrak p}\ne0\text{ 的素理想 }\mathfrak p\text{ 的集合}.
$$

<span class="original-page-anchor" id="pdf-page-433" aria-hidden="true"></span>

还有 $M$ 的**零化理想**：

$$
\operatorname{ann}(M)=\text{所有满足 }aM=0\text{ 的元素 }a\in A\text{ 的集合}.
$$

使用记号

$$
\operatorname{ass}(M)=M\text{ 的伴随素理想集合}.
$$

对任意理想 $\mathfrak a$，有其**根理想**：

$$
\operatorname{rad}(\mathfrak a)=\text{所有对某个整数 }n\ge1\text{ 满足 }a^n\in\mathfrak a\text{ 的元素 }a\in A\text{ 的集合}.
$$

若 $M$ *有限生成*，则命题 2.10 可以用下式重新表述：

$$
\boxed{\operatorname{rad}(\operatorname{ann}(M))=\bigcap_{\mathfrak p\in\operatorname{supp}(M)}\mathfrak p=\bigcap_{\mathfrak p\in\operatorname{ass}(M)}\mathfrak p.}
$$

**推论 2.11。** *设 $A$ 为诺特环，$M$ 为模。以下条件等价：*

(i) *$M$ 恰有一个伴随素理想。*

(ii) *$M\ne0$，且对每个 $a\in A$，同态 $a_M$ 或为单射，或为局部幂零。*

*若这些条件成立，则所有使 $a_M$ 局部幂零的元素 $a\in A$ 组成的集合，等于 $M$ 的那个伴随素理想。*

*证明。* 由命题 2.9 和 2.10 直接得出。

**命题 2.12。** *设 $N$ 为 $M$ 的子模。$N$ 的每个伴随素理想也与 $M$ 伴随。$M$ 的一个伴随素理想，或与 $N$ 伴随，或与 $M/N$ 伴随。*

*证明。* 第一个断言显然。设 $\mathfrak p$ 为 $M$ 的伴随素理想，且为元素 $x\ne0$ 的零化理想。若 $Ax\cap N=0$，则 $Ax$ 同构于 $M/N$ 的一个子模，所以 $\mathfrak p$ 与 $M/N$ 伴随。假设 $Ax\cap N\ne0$。取 $y=ax\in N$，其中 $a\in A$，$y\ne0$。则 $\mathfrak p$ 零化 $y$。我们断言 $\mathfrak p=\operatorname{ann}(y)$。设 $b\in A$ 且 $by=0$，则 $ba\in\mathfrak p$，但 $a\notin\mathfrak p$，故 $b\in\mathfrak p$。因此 $\mathfrak p$ 为 $y$ 在 $A$ 中的零化理想，故与 $N$ 伴随，得证。

<span class="original-page-anchor" id="pdf-page-434" aria-hidden="true"></span>

## §3. 准素分解

*除非另有说明，继续假定 $A$ 为交换环，模（分别地，同态）为 $A$ 模（分别地，$A$ 同态）。*

设 $M$ 为模。若 $M$ 的子模 $Q$ 满足 $Q\ne M$，且对任意 $a\in A$，同态 $a_{M/Q}$ 或为单射，或为幂零，则称 $Q$ 为**准素**子模。把 $A$ 看作自身上的模，可知理想 $\mathfrak q$ 为**准素理想**当且仅当它满足以下条件：

*给定 $a,b\in A$，若 $ab\in\mathfrak q$ 且 $a\notin\mathfrak q$，则对某个 $n\ge1$ 有 $b^n\in\mathfrak q$。*

设 $Q$ 为准素子模。令 $\mathfrak p$ 为所有使 $a_{M/Q}$ 幂零的元素 $a\in A$ 组成的理想，则 $\mathfrak p$ 为素理想。事实上，设 $a,b\in A$，$ab\in\mathfrak p$，$a\notin\mathfrak p$，则 $a_{M/Q}$ 为单射，所以对所有 $n\ge1$，$a_{M/Q}^n$ 也是单射。因 $(ab)_{M/Q}$ 幂零，$b_{M/Q}$ 必须幂零，所以 $b\in\mathfrak p$，这证明了 $\mathfrak p$ 为素理想。我们称 $\mathfrak p$ 为**属于** $Q$ 的素理想，也称 $Q$ 为 $\mathfrak p$ 准素的。

注意，具有素理想 $\mathfrak p$ 的准素子模 $Q$ 有如下相应性质：

*设 $b\in A$，$x\in M$，且 $bx\in Q$。若 $x\notin Q$，则 $b\in\mathfrak p$。*

**例。** 设 $\mathfrak m$ 为 $A$ 的极大理想，$\mathfrak q$ 为 $A$ 的理想，且对某个正整数 $k$ 有 $\mathfrak m^k\subset\mathfrak q$。则 $\mathfrak q$ 为准素理想，且 $\mathfrak m$ 属于 $\mathfrak q$。证明留给读者。

若把 $\mathfrak m$ 换成某个素理想 $\mathfrak p$，上述结论不总成立。例如，设 $R$ 为有素元 $t$ 的唯一分解整环。设 $A$ 为多项式 $f(X)\in R[X]$ 组成的子环，其中

$$
f(X)=a_0+a_1X+\cdots,
$$

且 $a_1$ 可被 $t$ 整除。令 $\mathfrak p=(tX,X^2,X^3)$。则 $\mathfrak p$ 为素理想，但

$$
\mathfrak p^2=(t^2X^2,tX^3,X^4)
$$

不是准素理想，因为 $X^2\notin\mathfrak p^2$，对所有 $k\ge1$ 都有 $t^k\notin\mathfrak p^2$，而 $t^2X^2\in\mathfrak p^2$。

**命题 3.1。** *设 $M$ 为模，$Q_1,\ldots,Q_r$ 为对同一素理想 $\mathfrak p$ 而言都是 $\mathfrak p$ 准素的子模，则 $Q_1\cap\cdots\cap Q_r$ 也为 $\mathfrak p$ 准素的。*

*证明。* 令 $Q=Q_1\cap\cdots\cap Q_r$。取 $a\in\mathfrak p$。对每个 $i=1,\ldots,r$，取 $n_i$ 使 $(a_{M/Q_i})^{n_i}=0$，并令 $n$ 为 $n_1,\ldots,n_r$ 的最大值。则 $a_{M/Q}^n=0$，故 $a_{M/Q}$ 幂零。反过来，假设 $a\notin\mathfrak p$。设 $x\in M$，且对某个 $j$，$x\notin Q_j$。则对所有正整数 $n$，都有 $a^nx\notin Q_j$，从而 $a_{M/Q}$ 为单射。命题得证。

<span class="original-page-anchor" id="pdf-page-435" aria-hidden="true"></span>

设 $N$ 为 $M$ 的子模。若把 $N$ 写成有限个准素子模的交，例如

$$
N=Q_1\cap\cdots\cap Q_r,
$$

就称之为 $N$ 的**准素分解**。由命题 3.1，把 $Q_i$ 按照所属的素理想分组，总能从一个给定的准素分解得到另一个分解，使属于各准素理想的素理想互不相同。若上述准素分解中，分别属于 $Q_1,\ldots,Q_r$ 的素理想 $\mathfrak p_1,\ldots,\mathfrak p_r$ 互异，且 $N$ 不能表示为准素理想族 $\{Q_1,\ldots,Q_r\}$ 的真子族的交，则称该分解为**约化**的。删去给定分解中的某些准素模，可见若 $N$ 有准素分解，则它也有约化准素分解。我们将证明一个结果，给出约化准素分解的某些唯一性性质。

设 $N$ 为 $M$ 的子模，$x\mapsto\bar x$ 为典范同态。设 $\overline Q$ 为 $\overline M=M/N$ 的子模，$Q$ 为它在 $M$ 中的逆像。由定义直接可见，$\overline Q$ 为准素子模当且仅当 $Q$ 为准素子模；若它们为准素子模，则属于 $Q$ 的素理想也属于 $\overline Q$。再者，若 $N=Q_1\cap\cdots\cap Q_r$ 为 $N$ 在 $M$ 中的准素分解，则

$$
(0)=\overline Q_1\cap\cdots\cap\overline Q_r
$$

为 $(0)$ 在 $\overline M$ 中的准素分解，读者可直接由定义验证。此外，$N$ 的分解约化当且仅当 $(0)$ 的分解约化，因为属于两者的素理想相同。

设 $Q_1\cap\cdots\cap Q_r=N$ 为约化准素分解，$\mathfrak p_i$ 属于 $Q_i$。若 $\mathfrak p_i$ 不包含 $\mathfrak p_j$（$j\ne i$），则称 $\mathfrak p_i$ 为**孤立**素理想。因此，孤立素理想正是在属于各准素模 $Q_i$ 的素理想集合中的极小元。

**定理 3.2。** *设 $N$ 为 $M$ 的子模，且*

$$
N=Q_1\cap\cdots\cap Q_r=Q'_1\cap\cdots\cap Q'_s
$$

*为 $N$ 的约化准素分解。则 $r=s$，属于 $Q_1,\ldots,Q_r$ 和 $Q'_1,\ldots,Q'_r$ 的素理想集合相同。若 $\{\mathfrak p_1,\ldots,\mathfrak p_m\}$ 为属于这些分解的孤立素理想集合，则对 $i=1,\ldots,m$ 有 $Q_i=Q'_i$；换言之，对应于孤立素理想的准素模唯一确定。*

*证明。* 约化分解的项数的唯一性，以及属于准素分支的素理想族的唯一性，将由下文定理 3.5 得出。

<span class="original-page-anchor" id="pdf-page-436" aria-hidden="true"></span>

还须证明属于某个孤立素理想（设为 $\mathfrak p_1$）的准素模的唯一性。由定义，对每个 $j=2,\ldots,r$，存在 $a_j\in\mathfrak p_j$，且 $a_j\notin\mathfrak p_1$。令 $a=a_2\cdots a_r$ 为它们的乘积，则对所有 $j>1$ 有 $a\in\mathfrak p_j$，但 $a\notin\mathfrak p_1$。可以找到整数 $n\ge1$，使对 $j=2,\ldots,r$ 都有 $a_{M/Q_j}^n=0$。令

$$
N_1=\text{所有满足 }a^nx\in N\text{ 的 }x\in M\text{ 的集合}.
$$

我们断言 $Q_1=N_1$，这将证明所需的唯一性。取 $x\in Q_1$，则 $a^nx\in Q_1\cap\cdots\cap Q_r=N$，故 $x\in N_1$。反过来，取 $x\in N_1$，则 $a^nx\in N$，特别地 $a^nx\in Q_1$。因 $a\notin\mathfrak p_1$，由定义可知 $a_{M/Q_1}$ 为单射。故 $x\in Q_1$，定理得证。

**定理 3.3。** *设 $M$ 为诺特模，$N$ 为 $M$ 的子模，则 $N$ 有准素分解。*

*证明。* 考虑 $M$ 中没有准素分解的子模集合。若此集合非空，则因 $M$ 为诺特模，它有极大元。设 $N$ 为这个极大元，则 $N$ 不为准素子模，存在 $a\in A$ 使 $a_{M/N}$ 既非单射也非幂零。递增子模序列

$$
\operatorname{Ker}a_{M/N}\subset\operatorname{Ker}a_{M/N}^2\subset\operatorname{Ker}a_{M/N}^3\subset\cdots
$$

终止，设终止于 $a_{M/N}^r$。令自同态 $\varphi:M/N\to M/N$ 为 $\varphi=a_{M/N}^r$，则 $\operatorname{Ker}\varphi^2=\operatorname{Ker}\varphi$。故在 $M/N$ 中有 $0=\operatorname{Ker}\varphi\cap\operatorname{Im}\varphi$，且 $\varphi$ 的核和像都非零。取它们在 $M$ 中的逆像，可见 $N$ 是 $M$ 中两个不等于 $N$ 的子模的交。由 $N$ 的极大性，这两个子模各自都有准素分解，所以 $N$ 也有准素分解，矛盾。

最后，把属于准素分解的素理想与上一节讨论的伴随素理想联系起来。

**命题 3.4。** *设 $A$ 和 $M$ 都是诺特的。$M$ 的子模 $Q$ 为准素子模，当且仅当 $M/Q$ 恰有一个伴随素理想 $\mathfrak p$；此时 $\mathfrak p$ 属于 $Q$，即 $Q$ 为 $\mathfrak p$ 准素的。*

*证明。* 由定义及推论 2.11 直接得出。

**定理 3.5。** *设 $A$ 和 $M$ 都是诺特的。$M$ 的伴随素理想，恰为属于 $0$ 在 $M$ 中的一个约化准素分解中的各准素模的素理想。特别地，伴随素理想集合有限。*

*证明。* 设

$$
0=Q_1\cap\cdots\cap Q_r
$$

<span class="original-page-anchor" id="pdf-page-437" aria-hidden="true"></span>

为 $0$ 在 $M$ 中的约化准素分解。存在单射同态

$$
M\to\bigoplus_{i=1}^r M/Q_i.
$$

由命题 2.12 和 3.4，$M$ 的每个伴随素理想都属于某个 $Q_i$。反过来，令 $N=Q_2\cap\cdots\cap Q_r$。因分解约化，$N\ne0$。有

$$
N=N/(N\cap Q_1)\approx(N+Q_1)/Q_1\subset M/Q_1.
$$

因此 $N$ 同构于 $M/Q_1$ 的子模，所以有一个伴随素理想，这个素理想只能是属于 $Q_1$ 的素理想 $\mathfrak p_1$。定理得证。

**定理 3.6。** *设 $A$ 为诺特环，则 $A$ 的零因子集合，是属于 $0$ 的一个约化准素分解中各准素理想的素理想的集合论意义下的并。*

*证明。* 元素 $a\in A$ 为零因子，当且仅当 $a_A$ 不是单射。由命题 2.9，这等价于 $a$ 属于 $A$（视为自身上的模）的某个伴随素理想。应用定理 3.5，证明完成。

## §4. Nakayama 引理

*令 $A$ 表示交换环，但未必为诺特环。*

研究环上的模时，许多性质可以先通过局部化得到，从而把问题化为局部环上的模的问题。在实际应用中，如本节所讨论的，这些模将是有限生成的。本节说明，模去局部环的极大理想后，可以把某些问题化为域上的向量空间问题。在域上，模总有基。我们尽可能把这一性质推广到局部环上的有限模。下面的前三个结论称为 **Nakayama 引理**。

**引理 4.1。** *设 $\mathfrak a$ 为 $A$ 的一个理想，包含于 $A$ 的每个极大理想。设 $E$ 为有限生成 $A$ 模，且 $\mathfrak a E=E$。则 $E=\{0\}$。*

<span class="original-page-anchor" id="pdf-page-438" aria-hidden="true"></span>

*证明。* 对 $E$ 的生成元个数作归纳。设 $x_1,\ldots,x_s$ 为 $E$ 的生成元。由假设，存在元素 $a_1,\ldots,a_s\in\mathfrak a$，使得

$$
x_s=a_1x_1+\cdots+a_sx_s,
$$

所以存在 $\mathfrak a$ 的元素 $a$（即 $-a_s$），使 $(1+a)x_s$ 属于前 $s-1$ 个生成元生成的子模。此外，$1+a$ 是 $A$ 的可逆元；否则 $1+a$ 属于某个极大理想，而 $a$ 属于所有极大理想，所以 $1$ 属于一个极大理想，这是不可能的。因此，$x_s$ 本身属于由 $s-1$ 个生成元生成的子模，归纳完成证明。

**译校注：** 原文此处印作“$a$ (namely $a_s$)”并使用 $(1+a)x_s$。由前式应有 $(1-a_s)x_s=a_1x_1+\cdots+a_{s-1}x_{s-1}$，因此保留 $(1+a)$ 时须取 $a=-a_s$。

引理 4.1 特别适用于 $A$ 为局部环、$\mathfrak a=\mathfrak m$ 为其极大理想的情形。

**引理 4.2。** *设 $A$ 为局部环，$E$ 为有限生成 $A$ 模，$F$ 为子模。若 $E=F+\mathfrak m E$，则 $E=F$。*

*证明。* 将引理 4.1 应用于 $E/F$。

**引理 4.3。** *设 $A$ 为局部环，$E$ 为有限生成 $A$ 模。若 $x_1,\ldots,x_n$ 为 $E$ 模 $\mathfrak m E$ 的生成元，则它们也是 $E$ 的生成元。*

*证明。* 取 $F$ 为由 $x_1,\ldots,x_n$ 生成的子模。

**定理 4.4。** *设 $A$ 为局部环，$E$ 为有限投射 $A$ 模，则 $E$ 自由。事实上，若 $x_1,\ldots,x_n$ 为 $E$ 的元素，其剩余类 $\bar x_1,\ldots,\bar x_n$ 为 $E/\mathfrak m E$ 在 $A/\mathfrak m$ 上的一组基，则 $x_1,\ldots,x_n$ 为 $E$ 在 $A$ 上的一组基。若 $x_1,\ldots,x_r$ 使 $\bar x_1,\ldots,\bar x_r$ 在 $A/\mathfrak m$ 上线性无关，则它们可以扩充为 $E$ 在 $A$ 上的一组基。*

*证明。* 第一个断言的以下证明应归功于 George Bergman。设 $F$ 为以 $e_1,\ldots,e_n$ 为基的自由模，$f:F\to E$ 为把 $e_i$ 映为 $x_i$ 的同态。我们要证明 $f$ 为同构。由引理 4.3，$f$ 为满射。因 $E$ 为投射模，$f$ 分裂，即可以写成 $F=P_0\oplus P_1$，其中 $P_0=\operatorname{Ker}f$，而 $P_1$ 由 $f$ 同构地映到 $E$ 上。现在，$x_1,\ldots,x_n$ 模 $\mathfrak m E$ 的线性无关性说明

$$
P_0\subset\mathfrak m F=\mathfrak m P_0\oplus\mathfrak m P_1.
$$

故 $P_0\subset\mathfrak m P_0$。此外，作为有限生成模的直和项，$P_0$ 有限生成。所以由引理 4.3，$P_0=(0)$，$f$ 为同构，得证。

至于第二个断言，它立即成立，因为可以把给定的<span class="original-page-anchor" id="pdf-page-439" aria-hidden="true"></span>序列 $x_1,\ldots,x_r$（其中 $\bar x_1,\ldots,\bar x_r$ 在 $A/\mathfrak m$ 上线性无关）扩充为序列 $x_1,\ldots,x_n$，使 $\bar x_1,\ldots,\bar x_n$ 在 $A/\mathfrak m$ 上线性无关，再应用证明的第一部分。定理证明完成。

设 $E$ 为局部环 $A$ 上的模，$\mathfrak m$ 为极大理想。令 $E(\mathfrak m)=E/\mathfrak m E$。若 $f:E\to F$ 为同态，则 $f$ 诱导同态

$$
f_{(\mathfrak m)}:E(\mathfrak m)\to F(\mathfrak m).
$$

若 $f$ 为满射，则显然 $f_{(\mathfrak m)}$ 为满射。

**命题 4.5。** *设 $f:E\to F$ 为局部环 $A$ 上有限模之间的同态，则：*

(i) *若 $f_{(\mathfrak m)}$ 为满射，则 $f$ 为满射。*

(ii) *假设 $f$ 为单射。若 $f_{(\mathfrak m)}$ 为满射，则 $f$ 为同构。*

(iii) *假设 $E,F$ 自由。若 $f_{(\mathfrak m)}$ 为单射（分别地，为同构），则 $f$ 为单射（分别地，为同构）。*

*证明。* 这些结论由 Nakayama 引理直接得出，证明留给读者。例如，第一个断言中，考虑正合列

$$
E\to F\to F/\operatorname{Im}f\to0,
$$

并对右边的项应用 Nakayama 引理。在 (iii) 中，使用定理 4.4 中基的提升。

## §5. 滤过模与分次模

设 $A$ 为交换环，$E$ 为模。$E$ 的**滤过**是指子模序列

$$
E=E_0\supset E_1\supset E_2\supset\cdots\supset E_n\supset\cdots.
$$

严格地说，这应称为递降滤过。我们不考虑其他滤过。

**例。** 设 $\mathfrak a$ 为环 $A$ 的理想，$E$ 为 $A$ 模。令

$$
E_n=\mathfrak a^nE.
$$

则子模序列 $\{E_n\}$ 是滤过。

更一般地，设 $\{E_n\}$ 为模 $E$ 的任意滤过。若对所有 $n$ 都有 $\mathfrak a E_n\subset E_{n+1}$，则称它为 **$\mathfrak a$ 滤过**。前面的例子就是 $\mathfrak a$ 滤过。

<span class="original-page-anchor" id="pdf-page-440" aria-hidden="true"></span>

若对所有充分大的 $n$ 都有 $\mathfrak a E_n=E_{n+1}$，则称 $\mathfrak a$ 滤过为 **$\mathfrak a$ 稳定**的，或简称**稳定**的。

**命题 5.1。** *设 $\{E_n\}$ 和 $\{E'_n\}$ 为 $E$ 的稳定 $\mathfrak a$ 滤过。则存在正整数 $d$，使对所有 $n\ge0$ 有*

$$
E_{n+d}\subset E'_n\qquad\text{以及}\qquad E'_{n+d}\subset E_n.
$$

*证明。* 只须证明 $E'_n=\mathfrak a^nE$ 的情形。因对所有 $n$ 有 $\mathfrak a E_n\subset E_{n+1}$，故 $\mathfrak a^nE\subset E_n$。由稳定性假设，存在 $d$ 使

$$
E_{n+d}=\mathfrak a^nE_d\subset\mathfrak a^nE,
$$

命题得证。

若环 $A$ 可以写成阿贝尔群的直和

$$
A=\bigoplus_{n=0}^{\infty}A_n,
$$

且对所有整数 $m,n\ge0$ 有 $A_n A_m\subset A_{n+m}$，则称 $A$ 为（按自然数）**分次**环。特别地，$A_0$ 为子环，每个分量 $A_n$ 为 $A_0$ 模。

设 $A$ 为分次环。若模 $E$ 可以写成阿贝尔群的直和

$$
E=\bigoplus_{n=0}^{\infty}E_n,
$$

且满足 $A_n E_m\subset E_{n+m}$，则称 $E$ 为**分次模**。特别地，$E_n$ 为 $A_0$ 模。$E_n$ 的元素称为**次数为 $n$ 的齐次元素**。由定义，$E$ 的任意元素可以唯一地写成齐次元素的有限和。

**例。** 设 $k$ 为域，$X_0,\ldots,X_r$ 为独立变量。多项式环 $A=k[X_0,\ldots,X_r]$ 为分次代数，且 $k=A_0$。次数为 $n$ 的齐次元素，是由 $X_0,\ldots,X_r$ 中次数为 $n$ 的单项式生成的多项式；这些单项式为

$$
X_0^{d_0}\cdots X_r^{d_r}\qquad\text{其中}\quad\sum_{i=0}^r d_i=n.
$$

若 $A$ 的理想 $I$ 作为 $A$ 模是分次的，则称它为齐次理想。此时商环 $A/I$ 也是分次环。

**命题 5.2。** *设 $A$ 为分次环，则 $A$ 为诺特环当且仅当 $A_0$ 为诺特环，且 $A$ 作为 $A_0$ 代数有限生成。*

<span class="original-page-anchor" id="pdf-page-441" aria-hidden="true"></span>

*证明。* 诺特环上的有限生成代数是诺特环，因为它是有限变量多项式环的同态像，可以应用 Hilbert 定理。

反过来，假设 $A$ 为诺特环。和

$$
A^+=\bigoplus_{n=1}^{\infty}A_n
$$

为 $A$ 的理想，其剩余类环为 $A_0$，因此 $A_0$ 为 $A$ 的同态像，故为诺特环。此外，由假设，$A^+$ 有有限个生成元 $x_1,\ldots,x_s$。把每个生成元表示为齐次元素之和，可以不失一般性地假设这些生成元齐次，次数分别为 $d_1,\ldots,d_s$，且所有 $d_i>0$。设 $B$ 为 $A$ 中在 $A_0$ 上由 $x_1,\ldots,x_s$ 生成的子环。我们断言，对所有 $n$ 都有 $A_n\subset B$。$n=0$ 时显然成立。设 $n>0$，$x$ 为次数为 $n$ 的齐次元素，则存在元素 $a_i\in A_{n-d_i}$，使

$$
x=\sum_{i=1}^s a_i x_i.
$$

因 $d_i>0$，由归纳法，每个 $a_i$ 都属于 $A_0[x_1,\ldots,x_s]=B$，所以 $x\in B$，证明完成。

现在讨论从滤过构造分次环的两种方法。

首先，设 $A$ 为环，$\mathfrak a$ 为理想。由幂 $\mathfrak a^n$ 把 $A$ 看作滤过环。定义**第一伴随分次环**为

$$
S_{\mathfrak a}(A)=S=\bigoplus_{n=0}^{\infty}\mathfrak a^n.
$$

类似地，若 $E$ 为 $A$ 模，且赋有 $\mathfrak a$ 滤过，则定义

$$
E_S=\bigoplus_{n=0}^{\infty}E_n.
$$

立即可验证，$E_S$ 为分次 $S$ 模。

注意，若 $A$ 为诺特环，$\mathfrak a$ 由元素 $x_1,\ldots,x_s$ 生成，则 $S$ 作为 $A$ 代数也由 $x_1,\ldots,x_s$ 生成，所以也是诺特环。

**引理 5.3。** *设 $A$ 为诺特环，$E$ 为具有 $\mathfrak a$ 滤过的有限生成模，则 $E_S$ 在 $S$ 上有限，当且仅当 $E$ 的滤过为 $\mathfrak a$ 稳定的。*

*证明。* 令

$$
F_n=\bigoplus_{i=0}^n E_i,
$$

<span class="original-page-anchor" id="pdf-page-442" aria-hidden="true"></span>

并令

$$
G_n=E_0\oplus\cdots\oplus E_n\oplus\mathfrak a E_n\oplus\mathfrak a^2E_n\oplus\mathfrak a^3E_n\oplus\cdots.
$$

则 $G_n$ 为 $E_S$ 的 $S$ 子模；因 $F_n$ 在 $A$ 上有限，$G_n$ 在 $S$ 上有限。有

$$
G_n\subset G_{n+1}\qquad\text{以及}\qquad\bigcup G_n=E_S.
$$

因 $S$ 为诺特环，可得：

$$
\begin{aligned}
E_S\text{ 在 }S\text{ 上有限}&\Longleftrightarrow\text{对某个 }N\text{ 有 }E_S=G_N\\
&\Longleftrightarrow\text{对所有 }m\ge0\text{ 有 }E_{N+m}=\mathfrak a^mE_N\\
&\Longleftrightarrow E\text{ 的滤过为 }\mathfrak a\text{ 稳定的}.
\end{aligned}
$$

引理得证。

**定理 5.4（Artin-Rees）。** *设 $A$ 为诺特环，$\mathfrak a$ 为理想，$E$ 为具有稳定 $\mathfrak a$ 滤过的有限 $A$ 模。设 $F$ 为子模，令 $F_n=F\cap E_n$，则 $\{F_n\}$ 为 $F$ 的稳定 $\mathfrak a$ 滤过。*

*证明。* 有

$$
\mathfrak a(F\cap E_n)\subset\mathfrak a F\cap\mathfrak a E_n\subset F\cap E_{n+1},
$$

故 $\{F_n\}$ 为 $F$ 的 $\mathfrak a$ 滤过。因此可构造伴随分次 $S$ 模 $F_S$；它是 $E_S$ 的子模，因 $S$ 为诺特环，它在 $S$ 上有限。应用引理 5.3，证明完成。

把 Artin-Rees 定理改写为它的原始形式如下。

**推论 5.5。** *设 $A$ 为诺特环，$E$ 为有限 $A$ 模，$F$ 为子模，$\mathfrak a$ 为理想。存在整数 $s$，使对所有整数 $n\ge s$ 都有*

$$
\mathfrak a^nE\cap F=\mathfrak a^{n-s}(\mathfrak a^sE\cap F).
$$

*证明。* 由定理 5.4 的特例和定义得出。

**定理 5.6（Krull）。** *设 $A$ 为诺特环，$\mathfrak a$ 为包含于 $A$ 的每个极大理想的理想，$E$ 为有限 $A$ 模，则*

$$
\bigcap_{n=1}^{\infty}\mathfrak a^nE=0.
$$

*证明。* 令 $F=\bigcap\mathfrak a^nE$，应用 Nakayama 引理，证明完成。

<span class="original-page-anchor" id="pdf-page-443" aria-hidden="true"></span>

**推论 5.7。** *设 $\mathfrak o$ 为极大理想为 $\mathfrak m$ 的局部诺特环，则*

$$
\bigcap_{n=1}^{\infty}\mathfrak m^n=0.
$$

*证明。* 这是定理 5.6 在 $E=A$ 时的特例。

构造分次环或分次模的第二种方法如下。设 $A$ 为环，$\mathfrak a$ 为 $A$ 的理想。定义**第二伴随分次环**

$$
\operatorname{gr}_{\mathfrak a}(A)=\bigoplus_{n=0}^{\infty}\mathfrak a^n/\mathfrak a^{n+1}.
$$

以显然的方式定义乘法。设 $a\in\mathfrak a^n$，用 $\bar a$ 表示其模 $\mathfrak a^{n+1}$ 的剩余类；设 $b\in\mathfrak a^m$，用 $\bar b$ 表示其模 $\mathfrak a^{m+1}$ 的剩余类。把乘积 $\bar a\bar b$ 定义为 $ab$ 模 $\mathfrak a^{m+n+1}$ 的剩余类。容易验证，这个定义与代表元的选择无关，并在 $\operatorname{gr}_{\mathfrak a}(A)$ 上定义了乘法，使之成为分次环。

设 $E$ 为滤过 $A$ 模。定义

$$
\operatorname{gr}(E)=\bigoplus_{n=0}^{\infty}E_n/E_{n+1}.
$$

若滤过为 $\mathfrak a$ 滤过，则 $\operatorname{gr}(E)$ 为分次 $\operatorname{gr}_{\mathfrak a}(A)$ 模。

**命题 5.8。** *假定 $A$ 为诺特环，$\mathfrak a$ 为 $A$ 的理想，则 $\operatorname{gr}_{\mathfrak a}(A)$ 为诺特环。若 $E$ 为具有稳定 $\mathfrak a$ 滤过的有限 $A$ 模，则 $\operatorname{gr}(E)$ 为有限 $\operatorname{gr}_{\mathfrak a}(A)$ 模。*

*证明。* 设 $x_1,\ldots,x_s$ 为 $\mathfrak a$ 的生成元，$\bar x_i$ 为 $x_i$ 在 $\mathfrak a/\mathfrak a^2$ 中的剩余类。则

$$
\operatorname{gr}_{\mathfrak a}(A)=(A/\mathfrak a)[\bar x_1,\ldots,\bar x_s]
$$

为诺特环，第一个断言得证。对第二个断言，存在某个 $d$，使

$$
E_{d+m}=\mathfrak a^mE_d\qquad\text{对所有 }m\ge0.
$$

因此，$\operatorname{gr}(E)$ 由有限直和

$$
\operatorname{gr}(E)_0\oplus\cdots\oplus\operatorname{gr}(E)_d
$$

生成。但每个 $\operatorname{gr}(E)_n=E_n/E_{n+1}$ 都在 $A$ 上有限生成，且被 $\mathfrak a$ 零化，所以为有限 $A/\mathfrak a$ 模。因此上述有限直和是有限 $A/\mathfrak a$ 模，所以 $\operatorname{gr}(E)$ 为有限 $\operatorname{gr}_{\mathfrak a}(A)$ 模，命题证明完成。

<span class="original-page-anchor" id="pdf-page-444" aria-hidden="true"></span>

## §6. Hilbert 多项式

本节主要研究局部环上某些滤过模的长度，并说明在适当情形下，它们是多项式。不过，先研究分次模，再利用上一节末尾的构造，把滤过模与分次模联系起来。

从分次诺特环及有限分次 $A$ 模 $E$ 出发，因此

$$
A=\bigoplus_{n=0}^{\infty}A_n\qquad\text{以及}\qquad E=\bigoplus_{n=0}^{\infty}E_n.
$$

命题 5.2 已说明，$A_0$ 为诺特环，$A$ 为有限生成 $A_0$ 代数。类似的论证说明，$E$ 有有限个齐次生成元，且对所有 $n\ge0$，$E_n$ 为有限 $A_0$ 模。

设 $\varphi$ 为所有有限 $A_0$ 模组成的类上的取值于 $\mathbf Z$ 的 Euler-Poincaré 函数，如第三章 §8 中所述。定义关于 $\varphi$ 的 **Poincaré 级数**为幂级数

$$
P_{\varphi}(E,t)=\sum_{n=0}^{\infty}\varphi(E_n)t^n\in\mathbf Z[[t]].
$$

为简便，用 $P(E,t)$ 代替 $P_{\varphi}(E,t)$。

**定理 6.1（Hilbert-Serre）。** *设 $s$ 为 $A$ 作为 $A_0$ 代数的生成元个数，则 $P(E,t)$ 是形如*

$$
P(E,t)=\frac{f(t)}{\prod_{i=1}^s(1-t^{d_i})}
$$

*的有理函数，其中 $d_i$ 为适当的正整数，$f(t)\in\mathbf Z[t]$。*

*证明。* 对 $s$ 归纳。$s=0$ 时断言显然成立。设 $s\ge1$。令 $A=A_0[x_1,\ldots,x_s]$，$\deg x_i=d_i\ge1$。$E$ 上乘以 $x_s$ 的映射产生正合列

$$
0\to K_n\to E_n\xrightarrow{x_s}E_{n+d_s}\to L_{n+d_s}\to0.
$$

令

$$
K=\bigoplus K_n\qquad\text{以及}\qquad L=\bigoplus L_n.
$$

<span class="original-page-anchor" id="pdf-page-445" aria-hidden="true"></span>

则 $K,L$ 为有限 $A$ 模（分别为 $E$ 的子模与商模），且被 $x_s$ 零化，因此实际上是分次 $A_0[x_1,\ldots,x_{s-1}]$ 模。由 Euler-Poincaré 函数的定义，得到

$$
\varphi(K_n)-\varphi(E_n)+\varphi(E_{n+d_s})-\varphi(L_{n+d_s})=0.
$$

乘以 $t^{n+d_s}$，再对 $n$ 求和，得到

$$
(1-t^{d_s})P(E,t)=P(L,t)-t^{d_s}P(K,t)+g(t),
$$

其中 $g(t)$ 为 $\mathbf Z[t]$ 中的多项式。定理由归纳法得出。

**注。** 定理 6.1 中，若 $A=A_0[x_1,\ldots,x_s]$，则如证明所示，$d_i=\deg x_i$。下面的结果说明所有次数均为 $1$ 时的情形。

**定理 6.2。** *假设 $A$ 作为 $A_0$ 代数由次数为 $1$ 的齐次元素生成。设 $d$ 为 $P(E,t)$ 在 $t=1$ 处的极点阶数。则对所有充分大的 $n$，$\varphi(E_n)$ 是关于 $n$ 的次数为 $d-1$ 的多项式。（在本结论中，约定零多项式的次数为 $-1$。）*

*证明。* 由定理 6.1，$\varphi(E_n)$ 为有理函数

$$
P(E,t)=f(t)/(1-t)^s
$$

中 $t^n$ 的系数。约去 $1-t$ 的幂，写成 $P(E,t)=h(t)/(1-t)^d$，其中 $h(1)\ne0$，$h(t)\in\mathbf Z[t]$。令

$$
h(t)=\sum_{k=0}^m a_kt^k.
$$

有二项式展开

$$
(1-t)^{-d}=\sum_{k=0}^{\infty}\binom{d+k-1}{d-1}t^k.
$$

为方便起见，约定 $n\ge0$ 时 $\binom n{-1}=0$，$n=-1$ 时 $\binom n{-1}=1$。于是

$$
\varphi(E_n)=\sum_{k=0}^m a_k\binom{d+n-k-1}{d-1}\qquad\text{对所有 }n\ge m.
$$

右侧的和是关于 $n$ 的多项式，其首项为

$$
\left(\sum a_k\right)\frac{n^{d-1}}{(d-1)!}\ne0.
$$

定理得证。

<span class="original-page-anchor" id="pdf-page-446" aria-hidden="true"></span>

定理 6.2 中的多项式，称为分次模 $E$ 关于 $\varphi$ 的 **Hilbert 多项式**。

现在汇集本章的若干结果，把定理 6.2 应用于某些滤过模。

设 $A$ 为极大理想为 $\mathfrak m$ 的局部诺特环，$\mathfrak q$ 为 $\mathfrak m$ 准素理想。则 $A/\mathfrak q$ 也为局部诺特环。因 $\mathfrak m$ 的某个幂包含于 $\mathfrak q$，$A/\mathfrak q$ 作为自身上的模只有一个伴随素理想，即 $\mathfrak m/\mathfrak q$ 本身。类似地，若 $M$ 为有限 $A/\mathfrak q$ 模，则 $M$ 只有一个伴随素理想；而唯一的单 $A/\mathfrak q$ 模实际上是一维 $A/\mathfrak m$ 模。又因 $\mathfrak m$ 的某个幂包含于 $\mathfrak q$，$A/\mathfrak q$ 有有限长度，$M$ 也有有限长度。现在应用定理 6.2 时，把长度函数作为 Euler-Poincaré 函数。

**定理 6.3。** *设 $A$ 为极大理想为 $\mathfrak m$ 的局部诺特环，$\mathfrak q$ 为 $\mathfrak m$ 准素理想，$E$ 为具有稳定 $\mathfrak q$ 滤过的有限生成 $A$ 模，则：*

(i) *对 $n\ge0$，$E/E_n$ 有有限长度。*

(ii) *对所有充分大的 $n$，这个长度为次数不超过 $s$ 的多项式 $g(n)$，其中 $s$ 为 $\mathfrak q$ 的最少生成元个数。*

(iii) *$g(n)$ 的次数和首项系数只依赖于 $E$ 和 $\mathfrak q$，而与所选择的滤过无关。*

*证明。* 令

$$
G=\operatorname{gr}_{\mathfrak q}(A)=\bigoplus\mathfrak q^n/\mathfrak q^{n+1}.
$$

则 $\operatorname{gr}(E)=\bigoplus E_n/E_{n+1}$ 为分次 $G$ 模，且 $G_0=A/\mathfrak q$。由命题 5.8，$G$ 为诺特环，$\operatorname{gr}(E)$ 为有限 $G$ 模。由定理前的讨论，$E/E_n$ 有有限长度；若用 $\varphi$ 表示长度，则

$$
\varphi(E/E_n)=\sum_{j=1}^n\varphi(E_{j-1}/E_j).
$$

若 $x_1,\ldots,x_s$ 生成 $\mathfrak q$，则它们在 $\mathfrak q/\mathfrak q^2$ 中的像 $\bar x_1,\ldots,\bar x_s$ 生成 $G$ 作为 $A/\mathfrak q$ 代数，且每个 $\bar x_i$ 的次数为 $1$。由定理 6.2，

$$
\varphi(E_n/E_{n+1})=h(n)
$$

对充分大的 $n$ 是关于 $n$ 的次数不超过 $s-1$ 的多项式。因为

$$
\varphi(E/E_{n+1})-\varphi(E/E_n)=h(n),
$$

由下文引理 6.4，$\varphi(E/E_n)$ 对所有充分大的 $n$ 是次数不超过 $s$ 的多项式 $g(n)$。最后一个关于次数不依赖于所选滤过的断言<span class="original-page-anchor" id="pdf-page-447" aria-hidden="true"></span>以及首项系数不依赖于所选滤过，直接由命题 5.1 得出，留给读者。证明完成。

由定理可见，存在多项式 $\chi_{E,\mathfrak q}$，使对所有充分大的 $n$ 有

$$
\chi_{E,\mathfrak q}(n)=\operatorname{length}(E/\mathfrak q^nE).
$$

若 $E=A$，通常称 $\chi_{A,\mathfrak q}$ 为 $\mathfrak q$ 的**特征多项式**。特别地，对所有充分大的 $n$ 有

$$
\chi_{A,\mathfrak q}(n)=\operatorname{length}(A/\mathfrak q^n).
$$

关于这些主题在维数理论中的进一步发展，见 [AtM 69] 和 [Mat 80]。

现在研究与多项式理想有关的一个特别重要的特例。设 $k$ 为域，

$$
A=k[X_0,\ldots,X_N]
$$

为 $N+1$ 个变量的多项式环。则 $A$ 为分次环，次数为 $n$ 的元素就是次数为 $n$ 的齐次多项式。设 $\mathfrak a$ 为 $A$ 的齐次理想，对整数 $n\ge0$ 定义：

$$
\begin{aligned}
\varphi(n)&=\dim_k A_n\\
\varphi(n,\mathfrak a)&=\dim_k\mathfrak a_n\\
\chi(n,\mathfrak a)&=\dim_k A_n/\mathfrak a_n=\dim_k A_n-\dim_k\mathfrak a_n=\varphi(n)-\varphi(n,\mathfrak a).
\end{aligned}
$$

与本节前面的记号相同，$A_n$ 表示 $A$ 中次数为 $n$ 的齐次元素组成的 $k$ 向量空间，$\mathfrak a_n$ 同理。于是

$$
\varphi(n)=\binom{N+n}{N}.
$$

我们考虑**二项式多项式**

$$
\binom Td=\frac{T(T-1)\cdots(T-d+1)}{d!}=\frac{T^d}{d!}+\text{低次项}.\tag{1}
$$

若 $f$ 为函数，定义其**差分函数** $\Delta f$ 为

$$
\Delta f(T)=f(T+1)-f(T).
$$

直接可验证

$$
\Delta\binom Td=\binom T{d-1}.\tag{2}
$$

<span class="original-page-anchor" id="pdf-page-448" aria-hidden="true"></span>

**引理 6.4。** *设 $P\in\mathbf Q[T]$ 为次数为 $d$ 的有理系数多项式。*

(a) *若对所有充分大的整数 $n$ 都有 $P(n)\in\mathbf Z$，则存在整数 $c_0,\ldots,c_d$，使*

$$
P(T)=c_0\binom Td+c_1\binom T{d-1}+\cdots+c_d.
$$

*特别地，对所有整数 $n$ 都有 $P(n)\in\mathbf Z$。*

(b) *若 $f:\mathbf Z\to\mathbf Z$ 为任意函数，且存在多项式 $Q(T)\in\mathbf Q[T]$，使 $Q(\mathbf Z)\subset\mathbf Z$，并对所有充分大的 $n$ 有 $\Delta f(n)=Q(n)$，则存在 (a) 中那样的多项式 $P$，使对所有充分大的 $n$ 有 $f(n)=P(n)$。*

*证明。* 用归纳法证明 (a)。若 $P$ 的次数为 $0$，断言显然。假设 $\deg P\ge1$。由 (1)，存在有理数 $c_0,\ldots,c_d$，使 $P(T)$ 具有 (a) 中的表达式。但 $\Delta P$ 的次数严格小于 $\deg P$。由 (2) 和归纳法，$c_0,\ldots,c_{d-1}$ 必须为整数。最后，因对充分大的 $n$ 有 $P(n)\in\mathbf Z$，$c_d$ 也为整数。(a) 得证。

对 (b)，利用 (a)，可写为

$$
Q(T)=c_0\binom T{d-1}+\cdots+c_{d-1},
$$

其中 $c_0,\ldots,c_{d-1}$ 为整数。令 $P_1$ 为 $Q$ 的“积分”，即

$$
P_1(T)=c_0\binom Td+\cdots+c_{d-1}\binom T1,\qquad\text{于是}\quad\Delta P_1=Q.
$$

则对所有充分大的 $n$，有 $\Delta(f-P_1)(n)=0$。故对所有充分大的 $n$，$(f-P_1)(n)$ 等于常数 $c_d$。令 $P=P_1+c_d$，证明完成。

**命题 6.5。** *设 $\mathfrak a,\mathfrak b$ 为 $A$ 的齐次理想，则*

$$
\begin{aligned}
\varphi(n,\mathfrak a+\mathfrak b)&=\varphi(n,\mathfrak a)+\varphi(n,\mathfrak b)-\varphi(n,\mathfrak a\cap\mathfrak b)\\
\chi(n,\mathfrak a+\mathfrak b)&=\chi(n,\mathfrak a)+\chi(n,\mathfrak b)-\chi(n,\mathfrak a\cap\mathfrak b).
\end{aligned}
$$

*证明。* 第一个等式显然，第二个由 $\chi$ 的定义得出。

<span class="original-page-anchor" id="pdf-page-449" aria-hidden="true"></span>

**定理 6.6。** *设 $F$ 为次数为 $d$ 的齐次多项式。假设 $F$ 模 $\mathfrak a$ 不是零因子，即若 $G\in A$ 且 $FG\in\mathfrak a$，则 $G\in\mathfrak a$。于是*

$$
\chi(n,\mathfrak a+(F))=\chi(n,\mathfrak a)-\chi(n-d,\mathfrak a).
$$

*证明。* 首先显然有

$$
\varphi(n,(F))=\varphi(n-d),
$$

因为积的次数为因子次数之和。然后，利用 $F$ 模 $\mathfrak a$ 不是零因子的假设，立即得到

$$
\varphi(n,\mathfrak a\cap(F))=\varphi(n-d,\mathfrak a).
$$

最后，由命题 6.5 中关于 $\chi$ 的公式，得到：

$$
\begin{aligned}
\chi(n,\mathfrak a+(F))&=\chi(n,\mathfrak a)+\chi(n,(F))-\chi(n,\mathfrak a\cap(F))\\
&=\chi(n,\mathfrak a)+\varphi(n)-\varphi(n,(F))-\varphi(n)+\varphi(n,\mathfrak a\cap(F))\\
&=\chi(n,\mathfrak a)-\varphi(n-d)+\varphi(n-d,\mathfrak a)\\
&=\chi(n,\mathfrak a)-\chi(n-d,\mathfrak a),
\end{aligned}
$$

定理得证。

用 $\mathfrak m$ 表示 $A$ 中的极大理想 $\mathfrak m=(X_0,\ldots,X_N)$，称 $\mathfrak m$ 为**无关素理想**。若某个正次幂 $\mathfrak m^r$ 包含于一个理想，则称该理想为**无关**理想。特别地，准素理想 $\mathfrak q$ 无关当且仅当 $\mathfrak m$ 属于 $\mathfrak q$。注意，由 Hilbert 零点定理，$\mathfrak m$ 的某个幂包含于 $\mathfrak a$，等价于 $\mathfrak a$ 在某个包含 $k$ 的代数闭域中唯一的零点是平凡零点。

**命题 6.7。** *设 $\mathfrak a$ 为齐次理想。*

**(a)** *若 $\mathfrak a$ 无关，则对充分大的 $n$ 有 $\chi(n,\mathfrak a)=0$。*

**(b)** *一般地，存在约化准素分解 $\mathfrak a=\mathfrak q_1\cap\cdots\cap\mathfrak q_s$，使所有 $\mathfrak q_i$ 都齐次。*

**(c)** *若分解中出现一个无关准素理想，设 $\mathfrak b$ 为所有其他准素理想的交，则对所有充分大的 $n$ 有*

$$
\chi(n,\mathfrak a)=\chi(n,\mathfrak b).
$$

*证明。* 对 (a)，由假设，对充分大的 $n$ 有 $A_n=\mathfrak a_n$，因此 (a) 显然。把 (b) 留作练习。对 (c)，设 $\mathfrak q_s$ 无关，并令 $\mathfrak b=\mathfrak q_1\cap\cdots\cap\mathfrak q_{s-1}$。由命题 6.5，

$$
\chi(n,\mathfrak b+\mathfrak q_s)=\chi(n,\mathfrak b)+\chi(n,\mathfrak q_s)-\chi(n,\mathfrak a).
$$

但 $\mathfrak b+\mathfrak q_s$ 无关，因此由 (a) 得出 (c)，证明完成。

<span class="original-page-anchor" id="pdf-page-450" aria-hidden="true"></span>

现在要证明，对任意齐次理想 $\mathfrak a$，由

$$
f(n)=\chi(n,\mathfrak a)
$$

定义的函数 $f$ 满足引理 6.4(b) 的条件。首先，若把基域从 $k$ 换成包含 $k$ 的代数闭域 $K$，并令 $A_K=K[X_0,\ldots,X_N]$，$\mathfrak a_K=K\mathfrak a$，则

$$
\dim_k A_n=\dim_K A_{K,n}\qquad\text{以及}\qquad\dim_k\mathfrak a_n=\dim_K\mathfrak a_{K,n}.
$$

因此可以假定 $k$ 代数闭。

其次，需要一个几何概念，即维数。设 $V$ 为 $k$ 上的簇，比如仿射簇，其泛点为 $(x)=(x_1,\ldots,x_N)$。定义其**维数**为 $k(x)$ 在 $k$ 上的超越次数。对由齐次素理想 $\mathfrak p$ 定义的射影簇，定义其维数为 $\mathfrak p$ 定义的齐次簇的维数减 $1$。

现在需要以下引理。

**引理 6.8。** *设 $V,W$ 为域 $k$ 上的簇。*

*若 $V\supset W$ 且 $\dim V=\dim W$，则 $V=W$。*

*证明。* 设 $V,W$ 位于仿射空间 $\mathbf A^N$ 中，$\mathfrak p_V$ 和 $\mathfrak p_W$ 分别为 $V$ 和 $W$ 在 $k[X]$ 中的素理想。则有典范同态

$$
k[X]/\mathfrak p_V\approx k[x]\to k[y]\approx k[X]/\mathfrak p_W,
$$

由 $V$ 的仿射坐标环满射到 $W$ 的仿射坐标环。若 $k(x)$ 和 $k(y)$ 的超越次数相同，且 $y_1,\ldots,y_r$ 为 $k(y)$ 在 $k$ 上的超越基，则 $x_1,\ldots,x_r$ 为 $k(x)$ 在 $k$ 上的超越基，同态 $k[x]\to k[y]$ 诱导同构

$$
k[x_1,\ldots,x_r]\xrightarrow{\approx}k[y_1,\ldots,y_r],
$$

从而在有限扩张 $k[x]$ 到 $k[y]$ 上诱导同构，得证。

**定理 6.9。** *设 $\mathfrak a$ 为 $A$ 的齐次理想，$r$ 为 $\mathfrak a$ 在射影空间中定义的代数空间的不可约分支的最大维数。则存在次数不超过 $r$ 的多项式 $P\in\mathbf Q[T]$，满足 $P(\mathbf Z)\subset\mathbf Z$，且对所有充分大的 $n$ 有*

$$
P(n)=\chi(n,\mathfrak a).
$$

<span class="original-page-anchor" id="pdf-page-451" aria-hidden="true"></span>

*证明。* 由命题 6.7(c)，可以假定 $\mathfrak a$ 的准素分解中没有无关的准素分支。设 $Z$ 为 $\mathfrak a$ 在射影空间中的零点代数空间。如前所述，可以假定 $k$ 代数闭。则存在次数为 $1$ 的齐次多项式 $L\in k[X]$（一个线性型），不属于给定分解中任何准素理想所属的素理想。特别地，$L$ 模 $\mathfrak a$ 不是零因子。于是 $\mathfrak a+(L)$ 的零点代数空间的各分支的维数必不超过 $r-1$。由归纳法和定理 6.6，差

$$
\chi(n,\mathfrak a)-\chi(n-1,\mathfrak a)
$$

满足引理 6.4(b) 的条件，证明完成。

定理 6.9 中的多项式称为理想 $\mathfrak a$ 的 **Hilbert 多项式**。

**注。** 上述结果可作为 Hartshorne 的 [Ha 77] 第一章，特别是 §7 的入门。若 $Z$ 非空，且写成

$$
\chi(n,\mathfrak a)=c\frac{n^r}{r!}+\text{低次项},
$$

则 $c>0$，$c$ 可以解释为 $Z$ 的**次数**；用几何语言说，就是 $Z$ 与一个充分一般的、维数互补的线性簇的交点个数，其中各点按一定的重数计数。解释与细节见 [Ha 77] 第一章命题 7.6 和定理 7.7；van der Waerden 的 [vdW 29] 对多重齐次多项式理想作了同样的研究；还可见第八章 §2 末尾提到的 [La 58]，以及论文 [MaW 85]、[Ph 86]，它们与约六十年前 van der Waerden 的工作建立了联系。

### 参考文献

[AtM 69] M. Atiyah 和 I. MacDonald，《交换代数导论》（*Introduction to commutative algebra*），Addison-Wesley，1969。

[Ha 77] R. Hartshorne，《代数几何》（*Algebraic Geometry*），Springer Verlag，1977。

[MaW 85] D. Masser 和 G. Wüstholz，《群簇上的零点估计 II》（Zero estimates on group varieties II），*Invent. Math.* **80** (1985)，第 233–267 页。

[Mat 80] H. Matsumura，《交换代数》（*Commutative algebra*），第二版，Benjamin-Cummings，1980。

[Ph 86] P. Philippon，《交换代数群中的零点引理》（Lemmes de zéros dans les groupes algébriques commutatifs），*Bull. Soc. Math. France* **114** (1986)，第 355–383 页。

[vdW 29] B. L. Van der Waerden，《关于 Hilbert 函数、理想的合成列及 Bezout 定理的推广》（On Hilbert's function, series of composition of ideals and a generalization of the theorem of Bezout），*Proc. R. Soc. Amsterdam* **31** (1929)，第 749–770 页。

<span class="original-page-anchor" id="pdf-page-452" aria-hidden="true"></span>

## §7. 不可分解模

设 $A$ 为未必交换的环，$E$ 为 $A$ 模。若 $E$ 满足子模的降链条件，即序列

$$
E_1\supset E_2\supset E_3\cdots
$$

必定稳定，就称 $E$ 为**阿廷模**：存在整数 $N$，使 $n\ge N$ 时 $E_n=E_{n+1}$。

**例 1。** 若 $k$ 为域，$A$ 为 $k$ 代数，$E$ 为同时具有 $A$ 模结构的有限维 $k$ 向量空间，则 $E$ 既是阿廷模也是诺特模。

**例 2。** 设 $A$ 为极大理想为 $\mathfrak m$ 的交换局部诺特环，$\mathfrak q$ 为 $\mathfrak m$ 准素理想。则对每个正整数 $n$，$A/\mathfrak q^n$ 是阿廷模。事实上，$A/\mathfrak q^n$ 有 Jordan-Hölder 滤过，其中每个商因子都是域 $A/\mathfrak m$ 上的有限维向量空间，且是有限长度模。见命题 7.2。

反过来，假设 $A$ 为同时是诺特环和阿廷环的局部环，$\mathfrak m$ 为极大理想。则存在正整数 $n$ 使 $\mathfrak m^n=0$。事实上，递降序列 $\mathfrak m^n$ 稳定，Nakayama 引理即得这一断言。进而，每个准素理想都是幂零的。

与诺特环和诺特模一样，以下结论容易验证：

**命题 7.1。** *设 $A$ 为环，且*

$$
0\to E'\to E\to E''\to0
$$

*为 $A$ 模的正合列，则 $E$ 为阿廷模当且仅当 $E'$ 和 $E''$ 为阿廷模。*

证明留给读者。证明与诺特情形相同，只须把模之间的包含关系反向。

**命题 7.2。** *模 $E$ 有有限单模滤过，当且仅当 $E$ 既为诺特模又为阿廷模。*

*证明。* 单模由一个元素生成，所以为诺特模。由于它没有非零真子模，它也为阿廷模。命题 7.2 于是由命题 7.1 直接得出。

若模 $E$ 可以写成直和

$$
E=E_1\oplus E_2,
$$

<span class="original-page-anchor" id="pdf-page-453" aria-hidden="true"></span>

其中 $E_1\ne E$，$E_2\ne E$，则称 $E$ 为可分解模。否则称 $E$ 为**不可分解**模。若 $E$ 如上可分解，令 $e_1$ 为到第一个因子的投影，$e_2=1-e_1$ 为到第二个因子的投影。则 $e_1,e_2$ 为幂等元，满足

$$
e_1\ne1,\qquad e_2\ne1,\qquad e_1+e_2=1\qquad\text{以及}\qquad e_1e_2=e_2e_1=0.
$$

反过来，若某个模 $E$ 的 $\operatorname{End}(E)$ 中存在这样的幂等元，则 $E$ 可分解，$e_i$ 为到子模 $e_iE$ 的投影。

设 $u:E\to E$ 为某个模 $E$ 的自同态。可以构造递降序列

$$
\operatorname{Im}u\supset\operatorname{Im}u^2\supset\operatorname{Im}u^3\supset\cdots.
$$

若 $E$ 为阿廷模，则这个序列稳定，对所有充分大的 $n$ 有

$$
\operatorname{Im}u^n=\operatorname{Im}u^{n+1}.
$$

把这个子模称为 $u^{\infty}(E)$ 或 $\operatorname{Im}u^{\infty}$。

类似地，有递增序列

$$
\operatorname{Ker}u\subset\operatorname{Ker}u^2\subset\operatorname{Ker}u^3\subset\cdots,
$$

若 $E$ 为诺特模，它就稳定；此时，对充分大的 $n$，记

$$
\operatorname{Ker}u^{\infty}=\operatorname{Ker}u^n.
$$

**命题 7.3（Fitting 引理）。** *假设 $E$ 为诺特模且为阿廷模，$u\in\operatorname{End}(E)$，则 $E$ 有直和分解*

$$
E=\operatorname{Im}u^{\infty}\oplus\operatorname{Ker}u^{\infty}.
$$

*此外，$u$ 在 $\operatorname{Im}u^{\infty}$ 上的限制为自同构，在 $\operatorname{Ker}u^{\infty}$ 上的限制为幂零自同态。*

*证明。* 取 $n$ 使 $\operatorname{Im}u^{\infty}=\operatorname{Im}u^n$，$\operatorname{Ker}u^{\infty}=\operatorname{Ker}u^n$。有

$$
\operatorname{Im}u^{\infty}\cap\operatorname{Ker}u^{\infty}=\{0\},
$$

因为若 $x$ 属于此交，则对某个 $y\in E$ 有 $x=u^n(y)$，于是 $0=u^n(x)=u^{2n}(y)$。所以 $y\in\operatorname{Ker}u^{2n}=\operatorname{Ker}u^n$，故 $x=u^n(y)=0$。

其次，取 $x\in E$。则对某个 $y\in u^n(E)$ 有

$$
u^n(x)=u^n(y).
$$

<span class="original-page-anchor" id="pdf-page-454" aria-hidden="true"></span>

于是可写为

$$
x=x-y+y,
$$

这说明 $E=\operatorname{Im}u^{\infty}+\operatorname{Ker}u^{\infty}$。结合证明的第一步，$E$ 是所述直和。

**译校注：** 原文印作 $x=x-u^n(y)+u^n(y)$。前页已选取 $y\in u^n(E)$ 且 $u^n(x)=u^n(y)$，所以属于核的是 $x-y$，属于像的是 $y$；这里应使用 $x=(x-y)+y$。

最后的断言显然成立，因为 $u$ 在 $\operatorname{Im}u^{\infty}$ 上的限制为满射，而由证明的第一部分，其核为 $0$。$u$ 在 $\operatorname{Ker}u^{\infty}$ 上的限制幂零，因为 $\operatorname{Ker}u^{\infty}=\operatorname{Ker}u^n$。命题证明完成。

现在把局部环的概念推广到非交换环。若环 $A$ 的非可逆元集合为双侧理想，则称 $A$ 为**局部环**。

**命题 7.4。** *设 $E$ 为环 $A$ 上的不可分解模，且 $E$ 为诺特模和阿廷模。$E$ 的任意自同态，或幂零，或为自同构。此外，$\operatorname{End}(E)$ 为局部环。*

*证明。* 由 Fitting 引理，对任意自同态 $u$，有 $E=\operatorname{Im}u^{\infty}$ 或 $E=\operatorname{Ker}u^{\infty}$。所以只须证明 $\operatorname{End}(E)$ 为局部环。设 $u$ 为不是可逆元的自同态，则 $u$ 幂零。对任意自同态 $v$，$uv$ 和 $vu$ 分别不是满射和单射，所以不是自同构。设 $u_1,u_2$ 为不是可逆元的自同态。须证明 $u_1+u_2$ 不是可逆元。若它是 $\operatorname{End}(E)$ 中的可逆元，令 $v_i=u_i(u_1+u_2)^{-1}$，则 $v_1+v_2=1$。此外，因 $v_2$ 幂零，由几何级数可知 $v_1=1-v_2$ 可逆。但由证明的第一部分，$v_1$ 不是可逆元，矛盾。证明完成。

**定理 7.5（Krull-Remak-Schmidt）。** *设 $E\ne0$ 为同时是诺特模和阿廷模的模，则 $E$ 是有限个不可分解模的直和。不计排列次序，这种直和中的不可分解分支在同构意义下唯一确定。*

*证明。* 分解为不可分解模直和的存在性，由阿廷条件得出。若先有 $E=E_1\oplus E_2$，则或 $E_1,E_2$ 均不可分解，分解完成；或例如 $E_1$ 可分解。重复此论证，这个分解不能无限继续，否则与阿廷假设矛盾。

还须证明唯一性。假设

$$
E=E_1\oplus\cdots\oplus E_r=F_1\oplus\cdots\oplus F_s,
$$

其中 $E_i,F_j$ 不可分解。须证明 $r=s$，且经某个排列后有 $E_i\approx F_i$。令 $e_i$ 为 $E$ 到 $E_i$ 的投影，$u_j$ 为 $E$ 到 $F_j$ 的投影，均相对于上述直和分解。令：

$$
v_j=e_1u_j\qquad\text{以及}\qquad w_j=u_je_1.
$$

<span class="original-page-anchor" id="pdf-page-455" aria-hidden="true"></span>

于是 $\sum u_j=\operatorname{id}_E$ 蕴含

$$
\sum_{j=1}^s v_jw_j\big|_{E_1}=\operatorname{id}_{E_1}.
$$

由命题 7.4，$\operatorname{End}(E_1)$ 为局部环，因此某个 $v_jw_j$ 为 $E_1$ 的自同构。重新编号后，可以假定 $v_1w_1$ 为 $E_1$ 的自同构。我们断言，$v_1$ 和 $w_1$ 在 $E_1$ 与 $F_1$ 之间诱导同构。这由以下引理得出。

**引理 7.6。** *设 $M,N$ 为模，且 $N$ 不可分解。设 $u:M\to N$ 和 $v:N\to M$ 满足 $vu$ 为自同构，则 $u,v$ 为同构。*

> **译校注。** 下面的证明使用 $\operatorname{id}_M\ne0$，即 $M\ne0$；在本定理的应用中，$M$ 是所考虑的非零不可分解分支 $E_1$。若独立使用此引理，须保留这一非零条件：取 $M=0$、$N\ne0$，则零映射的复合是零模的自同构，却不会使 $u,v$ 成为同构。正文保留原书的陈述。

*证明。* 令 $e=u(vu)^{-1}v$。则 $e^2=e$，为 $\operatorname{End}(N)$ 中的幂等元；因 $N$ 不可分解，它等于 $0$ 或 $1$。但 $e\ne0$，因为 $\operatorname{id}_M\ne0$，且

$$
0\ne\operatorname{id}_M=\operatorname{id}_M^2=(vu)^{-1}vu(vu)^{-1}vu.
$$

所以 $e=\operatorname{id}_N$。于是，因 $vu$ 为自同构，$u$ 为单射；因 $e=\operatorname{id}_N$ 为单射，$v$ 为单射；因 $e=\operatorname{id}_N$，$u$ 为满射；因 $vu$ 为自同构，$v$ 为满射。引理证明完成。

回到定理，现在可见

$$
E=F_1\oplus(E_2\oplus\cdots\oplus E_r).
$$

事实上，$e_1$ 从 $F_1$ 到 $E_1$ 诱导同构，而 $e_1$ 的核为 $E_2\oplus\cdots\oplus E_r$，所以

$$
F_1\cap(E_2\oplus\cdots\oplus E_r)=0.
$$

又 $F_1\equiv E_1\pmod{E_2\oplus\cdots\oplus E_r}$，所以 $E$ 为 $F_1$ 与 $E_2\oplus\cdots\oplus E_r$ 的和，故为所述直和。于是

$$
E/F_1\approx F_2\oplus\cdots\oplus F_s\approx E_2\oplus\cdots\oplus E_r.
$$

由归纳法完成证明。

将前述结果应用于交换环 $A$。注意，把 $A$ 看作自身上的模，则 $A$ 作为环的幂等元，与 $\operatorname{End}(A)$ 中的幂等元是同一回事。此外，$\operatorname{End}(A)\approx A$。因此得到以下特例：

**定理 7.7。** *设 $A$ 为同时是诺特环和阿廷环的交换环。*

<span class="original-page-anchor" id="pdf-page-456" aria-hidden="true"></span>

(i) *若 $A$ 作为环不可分解，则 $A$ 为局部环。*

(ii) *一般地，$A$ 为局部环的直积，这些局部环均为阿廷环和诺特环。*

习题中将给出推导本定理的另一种方法。

## 习题

**1.** 设 $A$ 为交换环，$M$ 为模，$N$ 为子模。设 $N=Q_1\cap\cdots\cap Q_r$ 为 $N$ 的准素分解，令 $\overline Q_i=Q_i/N$。证明 $0=\overline Q_1\cap\cdots\cap\overline Q_r$ 为 $0$ 在 $M/N$ 中的准素分解。陈述并证明逆命题。

**2.** 设 $\mathfrak p$ 为素理想，$\mathfrak a,\mathfrak b$ 为 $A$ 的理想。若 $\mathfrak a\mathfrak b\subset\mathfrak p$，证明 $\mathfrak a\subset\mathfrak p$ 或 $\mathfrak b\subset\mathfrak p$。

**3.** 设 $\mathfrak q$ 为准素理想，$\mathfrak a,\mathfrak b$ 为理想，且 $\mathfrak a\mathfrak b\subset\mathfrak q$。假设 $\mathfrak b$ 有限生成。证明 $\mathfrak a\subset\mathfrak q$，或存在正整数 $n$ 使 $\mathfrak b^n\subset\mathfrak q$。

**4.** 设 $A$ 为诺特环，$\mathfrak q$ 为 $\mathfrak p$ 准素理想。证明存在 $n\ge1$ 使 $\mathfrak p^n\subset\mathfrak q$。

**5.** 设 $A$ 为任意交换环，$S$ 为乘法子集。设 $\mathfrak p$ 为素理想，$\mathfrak q$ 为 $\mathfrak p$ 准素理想。则 $\mathfrak p$ 与 $S$ 相交当且仅当 $\mathfrak q$ 与 $S$ 相交。此外，若 $\mathfrak q$ 不与 $S$ 相交，则 $S^{-1}\mathfrak q$ 在 $S^{-1}A$ 中为 $S^{-1}\mathfrak p$ 准素理想。

**6.** 若 $\mathfrak a$ 为 $A$ 的理想，令 $\mathfrak a_S=S^{-1}\mathfrak a$。若 $\varphi_S:A\to S^{-1}A$ 为典范映射，即使 $\varphi_S$ 不是单射，也把 $\varphi_S^{-1}(\mathfrak a_S)$ 简记为 $\mathfrak a_S\cap A$。证明，$A$ 中不与 $S$ 相交的素理想与 $S^{-1}A$ 的素理想之间存在双射，由

$$
\mathfrak p\mapsto\mathfrak p_S\qquad\text{以及}\qquad\mathfrak p_S\mapsto\mathfrak p_S\cap A=\mathfrak p
$$

给出。把素理想换成准素理想，证明类似的结论。

**7.** 设 $\mathfrak a=\mathfrak q_1\cap\cdots\cap\mathfrak q_r$ 为理想的约化准素分解。假设 $\mathfrak q_1,\ldots,\mathfrak q_i$ 不与 $S$ 相交，而 $j>i$ 时 $\mathfrak q_j$ 与 $S$ 相交。证明

$$
\mathfrak a_S=\mathfrak q_{1S}\cap\cdots\cap\mathfrak q_{iS}
$$

为 $\mathfrak a_S$ 的约化准素分解。

**8.** 设 $A$ 为局部环。证明，$A$ 中任何非零幂等元必为单位元。（**幂等元**是满足 $e^2=e$ 的元素 $e\in A$。）

**9.** 设 $A$ 为交换阿廷环。证明：

(a) 所有素理想都是极大理想。[*提示：* 给定素理想 $\mathfrak p$，取 $x\in A$，$x(\mathfrak p)\ne0$。考虑递降链 $(x)\supset(x^2)\supset(x^3)\supset\cdots$。]

**译校注：** 原文提示印作 $x(\mathfrak p)=0$。要证明整环 $A/\mathfrak p$ 是域，须考虑其非零元素，因此此处应为 $x(\mathfrak p)\ne0$。

<span class="original-page-anchor" id="pdf-page-457" aria-hidden="true"></span>

(b) 素理想或极大理想只有有限个。[*提示：* 在极大理想的所有有限交中选取一个极小的。]

(c) $A$ 的幂零元素组成的理想 $N$ 是幂零理想，即存在正整数 $k$ 使 $N^k=(0)$。[*提示：* 取 $k$ 使 $N^k=N^{k+1}$。令 $\mathfrak a=N^k$。设 $\mathfrak b$ 为满足 $\mathfrak b\mathfrak a\ne0$ 的非零极小理想，则 $\mathfrak b$ 为主理想，且 $\mathfrak b\mathfrak a=\mathfrak b$。]

(d) $A$ 为诺特环。

(e) 存在整数 $r$，使

$$
A=\prod A/\mathfrak m^r,
$$

其中积遍历所有极大理想。

(f) 有

$$
A=\prod A_{\mathfrak p},
$$

其中积仍遍历所有素理想 $\mathfrak p$。

**10.** 设 $A,B$ 为局部环，极大理想分别为 $\mathfrak m_A,\mathfrak m_B$，$f:A\to B$ 为同态。若 $f^{-1}(\mathfrak m_B)=\mathfrak m_A$，则称 $f$ 为**局部**同态。假定这一条件成立。假设 $A,B$ 为诺特环，且：

**1.** $A/\mathfrak m_A\to B/\mathfrak m_B$ 为同构；

**2.** $\mathfrak m_A\to\mathfrak m_B/\mathfrak m_B^2$ 为满射；

**3.** $B$ 通过 $f$ 成为有限 $A$ 模。

证明 $f$ 为满射。[*提示：* 两次应用 Nakayama 引理。]

对理想 $\mathfrak a$，回顾第九章 §5：$\mathcal L(\mathfrak a)$ 是包含 $\mathfrak a$ 的素理想集合。

**11.** 设 $A$ 为交换环，$M$ 为 $A$ 模。定义 $M$ 的**支集**为

$$
\operatorname{supp}(M)=\{\mathfrak p\in\operatorname{spec}(A):M_{\mathfrak p}\ne0\}.
$$

若 $M$ 在 $A$ 上有限，证明 $\operatorname{supp}(M)=\mathcal L(\operatorname{ann}(M))$，其中 $\operatorname{ann}(M)$ 为 $M$ 在 $A$ 中的零化理想，即所有满足 $aM=0$ 的元素 $a\in A$ 的集合。

**12.** 设 $A$ 为诺特环，$M$ 为有限 $A$ 模。设 $I$ 为 $A$ 的理想，且 $\operatorname{supp}(M)\subset\mathcal L(I)$，则对某个 $n>0$ 有 $I^nM=0$。

**13.** 设 $A$ 为任意交换环，$M,N$ 为 $A$ 模。若 $M$ 有限表示，且 $S$ 为 $A$ 的乘法子集，证明

$$
S^{-1}\operatorname{Hom}_A(M,N)\approx\operatorname{Hom}_{S^{-1}A}(S^{-1}M,S^{-1}N).
$$

通常在 $A$ 为诺特环且 $M$ 有限生成时应用这一结论；此时 $M$ 也有限表示，因为关系模是有限生成自由模的子模。

**14.** (a) 证明命题 6.7(b)。

(b) 证明定理 6.9 中多项式 $P$ 的次数恰为 $r$。

### 局部常值的维数

**15.** 设 $A$ 为局部诺特环，$E$ 为有限 $A$ 模。假定 $A$ 没有幂零元素。对 $A$ 的每个素理想 $\mathfrak p$，设 $k(\mathfrak p)$ 为剩余类域。若 $\dim_{k(\mathfrak p)}E_{\mathfrak p}/\mathfrak p E_{\mathfrak p}$ 对所有 $\mathfrak p$ 为常数，证明 $E$ 自由。[*提示：* 取 $x_1,\ldots,x_r\in A$，使<span class="original-page-anchor" id="pdf-page-458" aria-hidden="true"></span>其模极大理想的剩余类为 $E/\mathfrak m E$ 在 $k(\mathfrak m)$ 上的一组基。得到满射同态

$$
A^r\to E\to0.
$$

设 $J$ 为核。证明对所有 $\mathfrak p$ 有 $J_{\mathfrak p}\subset\mathfrak m_{\mathfrak p}A_{\mathfrak p}^r$，从而对所有 $\mathfrak p$ 有 $J\subset\mathfrak p$，故 $J=0$。]

**译校注：** 习题 15 的提示在前页印作 $x_1,\ldots,x_r\in A$；这些元素的剩余类须在 $E/\mathfrak m E$ 中构成基，所以应取 $x_1,\ldots,x_r\in E$。此外，$J$ 是 $A^r$ 的子模，提示中 $J\subset\mathfrak p$ 应按各坐标理解为 $J\subset\mathfrak p A^r$。

**16.** 设 $A$ 为没有幂零元素的局部诺特环，$f:E\to F$ 为 $A$ 模同态，且 $E,F$ 为有限自由模。对 $A$ 的每个素理想 $\mathfrak p$，设

$$
f_{(\mathfrak p)}:E_{\mathfrak p}/\mathfrak p E_{\mathfrak p}\to F_{\mathfrak p}/\mathfrak p F_{\mathfrak p}
$$

为相应的 $k(\mathfrak p)$ 同态，其中 $k(\mathfrak p)=A_{\mathfrak p}/\mathfrak p A_{\mathfrak p}$ 为 $\mathfrak p$ 处的剩余类域。假设

$$
\dim_{k(\mathfrak p)}\operatorname{Im}f_{(\mathfrak p)}
$$

为常数。

(a) 证明 $F/\operatorname{Im}f$ 和 $\operatorname{Im}f$ 自由，且存在同构

$$
F\approx\operatorname{Im}f\oplus(F/\operatorname{Im}f).
$$

[*提示：* 使用习题 15。]

(b) 证明 $\operatorname{Ker}f$ 自由，且 $E\approx(\operatorname{Ker}f)\oplus(\operatorname{Im}f)$。[*提示：* 利用有限投射模自由这一事实。]

以下习题依赖于尚未正式定义的复形概念。**（有限）复形** $E$ 为模同态的序列

$$
0\to E^0\xrightarrow{d^0}E^1\xrightarrow{d^1}\cdots\xrightarrow{d^n}E^n\to0,
$$

以及同态 $d^i:E^i\to E^{i+1}$，满足对所有 $i$ 有 $d^{i+1}\circ d^i=0$。于是 $\operatorname{Im}(d^i)\subset\operatorname{Ker}(d^{i+1})$。复形的**同调** $H^i$ 定义为

$$
H^i=\operatorname{Ker}(d^{i+1})/\operatorname{Im}(d^i).
$$

按定义，$H^0=E^0$，$H^n=E^n/\operatorname{Im}(d^n)$。可以参阅第二十章第一节，因为这里仅使用基本概念及下面容易证明的性质。设 $E,F$ 为两个复形。所谓**同态** $f:E\to F$，是指一列同态

$$
f_i:E^i\to F^i,
$$

使对所有 $i$，下图交换：

![保留原书箭头方向与标签的交换图](/library/volume-86/diagrams/pdf-0458-complex-square.png)

**译校注：** 本页原文的微分编号存在冲突。按已声明的 $d^i:E^i\to E^{i+1}$，$i$ 次同调应为 $H^i=\operatorname{Ker}(d^i)/\operatorname{Im}(d^{i-1})$，端点应为 $H^0=\operatorname{Ker}(d^0)$、$H^n=E^n/\operatorname{Im}(d^{n-1})$；序列中进入 $E^n$ 的最后箭头也应标为 $d^{n-1}$。原文分别印作 $H^i=\operatorname{Ker}(d^{i+1})/\operatorname{Im}(d^i)$、$H^0=E^0$、$H^n=E^n/\operatorname{Im}(d^n)$。上图忠实保留原图向上的竖直箭头，但要与正文的 $f_i:E^i\to F^i$ 一致，应把两个竖直箭头改为向下。

证明，这样的同态 $f$ 在同调上诱导同态 $H(f):H(E)\to H(F)$；即对每个 $i$，有诱导同态

$$
H^i(f):H^i(E)\to H^i(F).
$$

<span class="original-page-anchor" id="pdf-page-459" aria-hidden="true"></span>

以下习题受到代数几何应用的启发，例如 Hartshorne《Algebraic Geometry》第三章定理 12.8。也可参阅第二十一章 §1，了解如何构造以下习题中的这类复形，以便计算较难处理的复形的同调。

### 复形模 $\mathfrak p$ 的约化

**17.** 设 $0\to K^0\to K^1\to\cdots\to K^n\to0$ 为无幂零元素的局部诺特环 $A$ 上有限自由模的复形。对 $A$ 的每个素理想 $\mathfrak p$ 和模 $E$，令 $E(\mathfrak p)=E_{\mathfrak p}/\mathfrak p E_{\mathfrak p}$；类似地，设 $K(\mathfrak p)$ 为局部化后再模 $\mathfrak p$ 约化的复形。对给定整数 $i$，假设

$$
\dim_{k(\mathfrak p)}H^i(K(\mathfrak p))
$$

为常数，其中 $H^i$ 是约化复形的第 $i$ 次同调。证明 $H^i(K)$ 自由，且有自然同构

$$
H^i(K)(\mathfrak p)\xrightarrow{\approx}H^i(K(\mathfrak p)).
$$

[*提示：* 先用 $d^i_{(\mathfrak p)}$ 表示由 $d^i$ 在 $K^i(\mathfrak p)$ 上诱导的映射。写出

$$
\dim_{k(\mathfrak p)}\operatorname{Ker}d^i_{(\mathfrak p)}=\dim_{k(\mathfrak p)}K^i(\mathfrak p)-\dim_{k(\mathfrak p)}\operatorname{Im}d^i_{(\mathfrak p)}.
$$

然后证明维数 $\dim_{k(\mathfrak p)}\operatorname{Im}d^i_{(\mathfrak p)}$ 和 $\dim_{k(\mathfrak p)}\operatorname{Im}d^{i-1}_{(\mathfrak p)}$ 必为常数。再应用习题 16。]

**译校注：** 原文提示最后印作“Then apply Exercise 12”；这里需要的是习题 16 关于约化映射的像维数为常数时核与像的自由性的结论，故应引用习题 16。

### 特殊点处同调的比较

**18.** 设 $A$ 为局部诺特环，$K$ 为如下有限复形：

$$
0\to K^0\to\cdots\to K^n\to0,
$$

其中对所有 $i$，$K^i$ 都为*有限自由模*。对某个指标 $i$，假设

$$
H^i(K)(\mathfrak m)\to H^i(K(\mathfrak m))
$$

为满射。证明：

(a) 此映射为同构。

(b) 以下正合列分裂：

$$
0\to\operatorname{Ker}d^i\to K^i\to\operatorname{Im}d^i\to0
$$

$$
0\to\operatorname{Im}d^i\to K^{i+1}.
$$

(c) 这些序列中的每一项均自由。

**19.** 设 $A$ 为局部诺特环，$K$ 为上一习题中的复形。对某个 $i$，假设

$$
H^i(K)(\mathfrak m)\to H^i(K(\mathfrak m))
$$

为满射（由前一习题，等价地为同构）。证明<span class="original-page-anchor" id="pdf-page-460" aria-hidden="true"></span>以下条件等价：

(a) $H^{i-1}(K)(\mathfrak m)\to H^{i-1}(K(\mathfrak m))$ 为满射。

(b) $H^{i-1}(K)(\mathfrak m)\to H^{i-1}(K(\mathfrak m))$ 为同构。

(c) $H^i(K)$ 自由。

[*提示：* 不断提升基，直到你筋疲力尽。]

(d) 若这些条件成立，则两个包含映射

$$
\operatorname{Im}d^{i-1}\subset\operatorname{Ker}d^i\subset K^i
$$

各自分裂，且这些模各自自由。模 $\mathfrak m$ 约化得到相应的包含关系

$$
\operatorname{Im}d^{i-1}_{(\mathfrak m)}\subset\operatorname{Ker}d^i_{(\mathfrak m)}\subset K^i(\mathfrak m),
$$

并诱导 (b) 中所述的上同调同构。[*提示：* 应用前一习题。]
