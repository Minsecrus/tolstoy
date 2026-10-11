---
title: "第一章 群"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第一部分导言：代数的基本对象","link":"/library/volume-86/part-01"}
next: {"text":"第二章 环","link":"/library/volume-86/chapter-002"}
---

# 第一章 群

<span class="original-page-anchor" id="pdf-page-18" aria-hidden="true"></span>

## §1. 幺半群

设 $S$ 为一个集合。映射

$$
S\times S\to S
$$

有时称为（$S$ 到自身的）**合成律**。若 $x,y$ 是 $S$ 的元素，则有序对 $(x,y)$ 在这个映射下的像也称为它们在该合成律下的**积**，记为 $xy$。（有时我们也写成 $x\cdot y$；在许多情况下，使用加法记号也很方便，于是写成 $x+y$。这时，我们把这个元素称为 $x$ 与 $y$ 的**和**。通常只有在关系 $x+y=y+x$ 成立时才使用记号 $x+y$。）

设 $S$ 是一个带有合成律的集合。若 $x,y,z$ 是 $S$ 的元素，则它们的积可以按两种方式形成：$(xy)z$ 和 $x(yz)$。若对 $S$ 中所有的 $x,y,z$ 都有 $(xy)z=x(yz)$，就称该合成律满足**结合律**。

若 $S$ 的一个元素 $e$ 对所有 $x\in S$ 都满足 $ex=x=xe$，则称它为**单位元**。（当合成律用加法记号表示时，单位元记为 $0$，并称为**零元**。）单位元是唯一的，因为若 $e'$ 是另一个单位元，由假设可得

$$
e=ee'=e'.
$$

在大多数情况下，单位元直接记为 $1$（而不是 $e$）。不过，本章的大部分内容中我们将使用 $e$，以免在证明最基本的性质时产生混淆。

**幺半群**是一个集合 $G$，它带有满足结合律的合成律，并且具有单位元（因此，特别地，$G$ 非空）。

<span class="original-page-anchor" id="pdf-page-19" aria-hidden="true"></span>

设 $G$ 为幺半群，$x_1,\ldots,x_n$ 为 $G$ 的元素（其中 $n$ 为整数，且 $n>1$）。我们归纳地定义它们的积：

$$
\prod_{\nu=1}^{n}x_\nu=x_1\cdots x_n=(x_1\cdots x_{n-1})x_n.
$$

*于是有下列规则：*

$$
\prod_{\mu=1}^{m}x_\mu\cdot\prod_{\nu=1}^{n}x_{m+\nu}=\prod_{\nu=1}^{m+n}x_\nu,
$$

*其含义实质上是：可以用任意方式在积中插入括号，而不改变它的值。* 用归纳法很容易证明这一点，我们将它留作练习。

也可以写

$$
\prod_{m+1}^{m+n}x_\nu\quad\text{代替}\quad\prod_{\nu=1}^{n}x_{m+\nu},
$$

并且定义

$$
\prod_{\nu=1}^{0}x_\nu=e.
$$

作为约定，我们也规定空积等于单位元。

还可以用任意集合定义更一般的合成律，即映射 $S_1\times S_2\to S_3$。这样，在结合律和交换律有意义的任何情形中，都可以表述它们。例如，为了表述交换律，需要一个合成律

$$
f:S\times S\to T,
$$

其中两个出发集合相同。于是，**交换律**是指 $f(x,y)=f(y,x)$；若在记号中省略映射 $f$，则写成 $xy=yx$。至于结合律，我们请读者自行表述使它成立的最一般的集合组合。以后我们将遇到一些特殊情形，例如由映射

$$
S\times S\to S\quad\text{和}\quad S\times T\to T
$$

产生的情形。此时，对 $x\in S$、$y\in S$、$z\in T$，积 $(xy)z$ 有意义。对这样的元素 $x,y,z$，积 $x(yz)$ 也有意义；因此，说我们的合成律满足结合律也是有意义的，即对上述所有 $x,y,z$ 都有 $(xy)z=x(yz)$。

若 $G$ 的合成律满足交换律，也称 $G$ 是**交换的**（或**阿贝尔的**）。

<span class="original-page-anchor" id="pdf-page-20" aria-hidden="true"></span>

*设 $G$ 为交换幺半群，$x_1,\ldots,x_n$ 为 $G$ 的元素。设 $\psi$ 是整数集合 $(1,\ldots,n)$ 到自身的双射。则*

$$
\prod_{\nu=1}^{n}x_{\psi(\nu)}=\prod_{\nu=1}^{n}x_\nu.
$$

我们用归纳法证明。当 $n=1$ 时结论显然成立。假设结论对 $n-1$ 成立。取整数 $k$ 使得 $\psi(k)=n$。则

$$
\begin{aligned}
\prod_{1}^{n}x_{\psi(\nu)}&=\prod_{1}^{k-1}x_{\psi(\nu)}\cdot x_{\psi(k)}\cdot\prod_{1}^{n-k}x_{\psi(k+\nu)}\\
&=\prod_{1}^{k-1}x_{\psi(\nu)}\cdot\prod_{1}^{n-k}x_{\psi(k+\nu)}\cdot x_{\psi(k)}.
\end{aligned}
$$

按下列规则定义 $(1,\ldots,n-1)$ 到自身的映射 $\varphi$：

$$
\begin{aligned}
\varphi(\nu)&=\psi(\nu)&&\text{若 }\nu<k,\\
\varphi(\nu)&=\psi(\nu+1)&&\text{若 }\nu\geqq k.
\end{aligned}
$$

于是

$$
\begin{aligned}
\prod_{1}^{n}x_{\psi(\nu)}&=\prod_{1}^{k-1}x_{\varphi(\nu)}\prod_{1}^{n-k}x_{\varphi(k-1+\nu)}\cdot x_n\\
&=\prod_{1}^{n-1}x_{\varphi(\nu)}\cdot x_n,
\end{aligned}
$$

由归纳假设，这等于 $x_1\cdots x_n$，即得所需结论。

设 $G$ 为交换幺半群，$I$ 为集合，$f:I\to G$ 为映射，且对**几乎所有** $i\in I$ 都有 $f(i)=e$。（这里以及下文中，**几乎所有**均指*除有限个以外的所有*。）设 $I_0$ 是 $I$ 中由满足 $f(i)\ne e$ 的那些 $i$ 组成的子集。记号

$$
\prod_{i\in I}f(i)
$$

表示积

$$
\prod_{i\in I_0}f(i),
$$

其中各因子可按任意次序相乘（根据前面的说明，其值与次序无关）。约定空积等于 $e$。

当 $G$ 用加法记号表示时，我们用求和符号 $\Sigma$ 代替求积符号。

处理乘积有许多形式规则，要把它们全部列出会很繁琐。我们给出一个例子。设 $I,J$ 为两个集合，且<span class="original-page-anchor" id="pdf-page-21" aria-hidden="true"></span>$f:I\times J\to G$ 是到交换幺半群中的映射，并且对几乎所有有序对 $(i,j)$ 都取值 $e$。则

$$
\prod_{i\in I}\left[\prod_{j\in J}f(i,j)\right]=\prod_{j\in J}\left[\prod_{i\in I}f(i,j)\right].
$$

证明留作练习。

在记号上，若所指的指标集合清楚，我们有时写成 $\prod f(i)$，省略 $i\in I$。

设 $x$ 为幺半群 $G$ 的元素。对每个整数 $n\geqq0$，我们定义 $x^n$ 为

$$
\prod_{1}^{n}x,
$$

因此，特别地，有 $x^0=e$、$x^1=x$、$x^2=xx$、$\ldots$。显然有 $x^{(n+m)}=x^nx^m$ 和 $(x^n)^m=x^{nm}$。此外，根据前面关于结合律和交换律的规则，若 $G$ 的元素 $x,y$ 满足 $xy=yx$，则 $(xy)^n=x^ny^n$。严格证明留作练习。

若 $S,S'$ 是幺半群 $G$ 的两个子集，则定义 $SS'$ 为由所有满足 $x\in S$、$y\in S'$ 的元素 $xy$ 组成的子集。通过归纳，可以定义有限个子集的积，且该乘积满足结合律。例如，若 $S,S',S''$ 是 $G$ 的子集，则 $(SS')S''=S(S'S'')$。注意 $GG=G$（因为 $G$ 有单位元）。若 $x\in G$，则定义 $xS$ 为 $\{x\}S$，其中 $\{x\}$ 为仅含一个元素 $x$ 的集合。因此，$xS$ 由所有满足 $y\in S$ 的元素 $xy$ 组成。

$G$ 的**子幺半群**是指 $G$ 的一个子集 $H$，它包含单位元 $e$，并且若 $x,y\in H$，则 $xy\in H$（我们称 $H$ 对该合成律**封闭**）。于是显然，$H$ 在由 $G$ 的合成律所诱导的合成律下，本身也是幺半群。

若 $x$ 是幺半群 $G$ 的元素，则由幂 $x^n$（$n=0,1,\ldots$）组成的子集是 $G$ 的子幺半群。

所有 $\geqq0$ 的整数构成的集合在加法下是幺半群。

以后我们将定义环。若 $R$ 是交换环，我们将讨论乘法子集 $S$，即包含单位元，且当 $x,y\in S$ 时有 $xy\in S$ 的子集。这样的子集是幺半群。

**一个常见的例子。** 设 $\mathbf{N}$ 为自然数，即 $\geqq0$ 的整数。则 $\mathbf{N}$ 是加法幺半群。在某些应用中，使用一个乘法版本很有用。参见第二章 §3 中多项式的定义，那里在处理多元多项式时还使用了更高维的版本。

**一个有趣的例子。** 我们假设读者熟悉初等拓扑的术语。设 $M$ 为紧致（连通）曲面的同胚类所组成的集合。我们将在 $M$ 中定义加法。设 $S,S'$ 为紧致曲面。取 $S$ 中的一个小圆盘 $D$，以及 $S'$ 中的一个小圆盘 $D'$。设 $C,C'$ 分别为构成 $D$ 和 $D'$ 边界的圆周。设 $D_0,D'_0$ 分别为 $D$ 和 $D'$ 的内部；通过将 $C$ 与 $C'$ 等同，把 $S-D_0$ 与 $S'-D'_0$ 粘合。可以证明，所得曲面不依赖于<span class="original-page-anchor" id="pdf-page-22" aria-hidden="true"></span>前述构造中所作的各种选择（这里的独立性是在同胚意义下而言的）。若 $\sigma,\sigma'$ 分别表示 $S$ 和 $S'$ 的同胚类，则定义 $\sigma+\sigma'$ 为通过上述粘合过程得到的曲面的类。可以证明，这个加法在 $M$ 上定义了幺半群结构，其单位元为通常的 $2$ 维球面的类。此外，若 $\tau$ 表示环面的类，$\pi$ 表示射影平面的类，则 $M$ 的每个元素 $\sigma$ 都有唯一的如下形式的表示：

$$
\sigma=n\tau+m\pi,
$$

其中 $n$ 为 $\geqq0$ 的整数，$m=0,1$ 或 $2$。有 $3\pi=\tau+\pi$。

（插入前面这个例子有两个原因：第一，缓解本节本来颇为枯燥的内容；第二，向读者说明幺半群是自然存在的。不用说，本书余下部分不会以任何方式使用这个例子。）

**还有其他例子。** 在第三章 §4 的末尾，我们将指出，一个环上的模的同构类在直和运算下构成幺半群。在第十五章 §1 中，我们将讨论由二次型的等价类组成的幺半群。

## §2. 群

**群** $G$ 是一个幺半群，其中对每个元素 $x\in G$，都存在元素 $y\in G$ 使得 $xy=yx=e$。这样的元素 $y$ 称为 $x$ 的**逆元**。逆元是唯一的，因为若 $y'$ 也是 $x$ 的逆元，则

$$
y'=y'e=y'(xy)=(y'x)y=ey=y.
$$

这个逆元记为 $x^{-1}$（当合成律用加法记号表示时，则记为 $-x$）。

对任意正整数 $n$，令 $x^{-n}=(x^{-1})^n$。于是，通常的乘方规则对所有整数都成立，而不仅仅对 $\geqq0$ 的整数成立（我们在 §1 中讨论幺半群时已经指出了后一种情形）。这些简单的证明留给读者。

在单位元和逆元的定义中，也可以（按显然的方式）定义左单位元和左逆元。在适当的条件下，很容易证明它们也分别是单位元和逆元。具体来说：

*设 $G$ 为带有满足结合律的合成律的集合，$e$ 为该合成律的左单位元，并假设每个元素都有左逆元。则 $e$ 是单位元，且每个左逆元也是逆元。特别地，$G$ 是群。*

为证明这一点，取 $a\in G$，并取 $b\in G$ 使得 $ba=e$。则

$$
bab=eb=b.
$$

在左边乘以 $b$ 的一个左逆元，得到

$$
ab=e,
$$

换句话说，$b$ 也是 $a$ 的右逆元。还可以看出，$a$ 是 $b$ 的左<span class="original-page-anchor" id="pdf-page-23" aria-hidden="true"></span>逆元。此外，

$$
ae=aba=ea=a,
$$

由此 $e$ 是右单位元。

**例。** 设 $G$ 为群，$S$ 为非空集合。映射的集合 $M(S,G)$ 本身也是群；具体地，对从 $S$ 到 $G$ 的两个映射 $f,g$，定义 $fg$ 为满足

$$
(fg)(x)=f(x)g(x)
$$

的映射，并定义 $f^{-1}$ 为满足 $f^{-1}(x)=f(x)^{-1}$ 的映射。于是很容易验证 $M(S,G)$ 是群。若 $G$ 交换，则 $M(S,G)$ 也交换；当 $G$ 中的合成律用加法记号表示时，$M(S,G)$ 中的合成律也用加法记号表示，因此用 $f+g$ 代替 $fg$，用 $-f$ 代替 $f^{-1}$。

**例。** 设 $S$ 为非空集合。令 $G$ 为 $S$ 到自身的所有双射组成的集合。则 $G$ 为群，其合成律就是通常的映射复合。$G$ 的单位元是 $S$ 的恒等映射，其他群的性质也很容易验证。$G$ 的元素称为 $S$ 的**置换**。我们也把 $G$ 记为 $\operatorname{Perm}(S)$。关于有限集合 $S$ 的 $\operatorname{Perm}(S)$ 的更多内容，参见下面的 §5。

**例。** 这里假设读者了解线性代数的基本概念。设 $k$ 为域，$V$ 为 $k$ 上的向量空间。用 $GL(V)$ 表示 $V$ 到自身的可逆 $k$ 线性映射组成的集合。则 $GL(V)$ 在映射复合下构成群。同样，设 $k$ 为域，用 $GL(n,k)$ 表示元素属于 $k$ 的可逆 $n\times n$ 矩阵组成的集合。则 $GL(n,k)$ 在矩阵乘法下构成群。当 $n\geqq2$ 时，这个群不交换。

**例。自同构群。** 我们建议读者现在就参阅 §11，其中定义了范畴的概念，并给出了几个例子。对于范畴中的任意对象 $A$，其自同构构成一个群，记为 $\operatorname{Aut}(A)$。集合的置换与向量空间的线性自同构，只是这一更一般结构的例子。

**例。** 有理数集合在加法下构成群。非零有理数集合在乘法下构成群。实数和复数也有类似结论。

**例。循环群。** 整数 $\mathbf{Z}$ 构成加法群。若存在元素 $a\in G$，使得 $G$ 的每个元素（用乘法记号表示时）都可写为 $a^n$，其中 $n$ 为某个整数，则称该群为**循环群**。若 $G$ 用加法记号表示，则循环群的每个元素均可写为 $na$。称 $a$ 为一个**循环生成元**。因此，$\mathbf{Z}$ 是以 $1$ 为生成元的加法循环群，也以 $-1$ 为生成元。除此之外没有其他生成元。给定正整数 $n$，复数中的 $n$ 次单位根构成一个 $n$ 阶循环群。按照通常的记号，$e^{2\pi i/n}$ 是这个群的一个生成元。$e^{2\pi ir/n}$ 也是生成元，<span class="original-page-anchor" id="pdf-page-24" aria-hidden="true"></span>其中 $r\in\mathbf{Z}$，且 $r$ 与 $n$ 互素。这个群的生成元称为**本原 $n$ 次单位根**。

**例。直积。** 设 $G_1,G_2$ 为群。令 $G_1\times G_2$ 为它们作为集合的直积，因此 $G_1\times G_2$ 是由满足 $x_i\in G_i$ 的所有有序对 $(x_1,x_2)$ 组成的集合。我们按分量定义合成律：

$$
(x_1,x_2)(y_1,y_2)=(x_1y_1,x_2y_2).
$$

于是 $G_1\times G_2$ 为群，其单位元是 $(e_1,e_2)$（其中 $e_i$ 为 $G_i$ 的单位元）。同样，对 $n$ 个群，我们定义 $G_1\times\cdots\times G_n$ 为满足 $x_i\in G_i$（$i=1,\ldots,n$）的所有 $n$ 元组组成的集合，乘法按分量进行。更一般地，设 $I$ 为集合，对每个 $i\in I$，设 $G_i$ 为群。令 $G=\prod G_i$ 为集合 $G_i$ 的集合论乘积。于是 $G$ 为满足 $x_i\in G_i$ 的所有族 $(x_i)_{i\in I}$ 组成的集合。通过按分量相乘，可以在 $G$ 上定义群结构：具体地，若 $(x_i)_{i\in I}$ 和 $(y_i)_{i\in I}$ 为 $G$ 的两个元素，则定义它们的积为 $(x_iy_i)_{i\in I}$。定义 $(x_i)_{i\in I}$ 的逆元为 $(x_i^{-1})_{i\in I}$。于是显然，$G$ 为群，称为这个族的**直积**。

设 $G$ 为群。$G$ 的**子群** $H$ 是 $G$ 的一个子集，它包含单位元，并且对合成律和取逆运算封闭（即它是子幺半群，且若 $x\in H$，则 $x^{-1}\in H$）。若一个子群仅含单位元，则称其为**平凡子群**。任意非空子群族的交仍是子群（验证很简单）。

设 $G$ 为群，$S$ 为 $G$ 的子集。若 $G$ 的每个元素均可表示为 $S$ 中元素或 $S$ 中元素的逆元的乘积，即可表示为 $x_1\cdots x_n$，其中每个 $x_i$ 或 $x_i^{-1}$ 属于 $S$，则称 $S$ **生成** $G$，或称 $S$ 为 $G$ 的一个**生成元集合**。显然，所有这样的乘积组成的集合是 $G$ 的子群（空积为单位元），且是包含 $S$ 的最小子群。因此，$S$ 生成 $G$ 当且仅当包含 $S$ 的最小子群就是 $G$ 本身。若 $G$ 由 $S$ 生成，则写成 $G=\langle S\rangle$。根据定义，循环群就是具有一个生成元的群。给定元素 $x_1,\ldots,x_n\in G$，这些元素生成一个子群 $\langle x_1,\ldots,x_n\rangle$，即由 $G$ 中所有如下形式的元素组成的集合：

$$
x_{i_1}^{k_1}\cdots x_{i_r}^{k_r}\quad\text{其中 }k_1,\ldots,k_r\in\mathbf{Z}.
$$

单个元素 $x\in G$ 生成一个循环子群。

**例。** 有两个 $8$ 阶非阿贝尔群。其中一个是**正方形的对称群**，由两个元素 $\sigma,\tau$ 生成，满足

$$
\sigma^4=\tau^2=e\quad\text{且}\quad\tau\sigma\tau^{-1}=\sigma^3.
$$

另一个是**四元数群**，由两个元素 $i,j$ 生成；若令 $k=ij$、$m=i^2$，则

$$
i^4=j^4=k^4=e,\quad i^2=j^2=k^2=m,\quad ij=mji.
$$

在你掌握足够多的群的知识之后，习题 35 就很容易做了。

<span class="original-page-anchor" id="pdf-page-25" aria-hidden="true"></span>

设 $G,G'$ 为幺半群。$G$ 到 $G'$ 的**幺半群同态**（或简称**同态**）是一个映射 $f:G\to G'$，它对所有 $x,y\in G$ 都满足 $f(xy)=f(x)f(y)$，并将 $G$ 的单位元映到 $G'$ 的单位元。若 $G,G'$ 为群，则 $G$ 到 $G'$ 的**群同态**就是幺半群同态。

我们有时说“设 $f:G\to G'$ 为群同态”，其含义是：“设 $G,G'$ 为群，且 $f$ 为从 $G$ 到 $G'$ 的同态。”

设 $f:G\to G'$ 为群同态。则

$$
f(x^{-1})=f(x)^{-1},
$$

因为若 $e,e'$ 分别为 $G,G'$ 的单位元，则

$$
e'=f(e)=f(xx^{-1})=f(x)f(x^{-1}).
$$

此外，若 $G,G'$ 为群，$f:G\to G'$ 为一个映射，且对 $G$ 中所有 $x,y$ 都有

$$
f(xy)=f(x)f(y),
$$

则 $f(e)=e'$，因为 $f(ee)=f(e)$，同时又等于 $f(e)f(e)$。乘以 $f(e)$ 的逆元，就得到 $f(e)=e'$。

设 $G,G'$ 为幺半群。若存在同态 $g:G'\to G$，使得 $f\circ g$ 和 $g\circ f$ 分别为 $G'$ 和 $G$ 上的恒等映射，则称同态 $f:G\to G'$ 为**同构**。很容易验证，$f$ 为同构当且仅当 $f$ 为双射。两个群 $G$ 和 $G'$ 之间存在同构，有时记为 $G\approx G'$。若 $G=G'$，则称该同构为**自同构**。从 $G$ 到自身的同态也称为**自同态**。

**例。** 设 $G$ 为幺半群，$x$ 为 $G$ 的元素。用 $\mathbf{N}$ 表示由 $\geqq0$ 的整数构成的（加法）幺半群。则满足 $f(n)=x^n$ 的映射 $f:\mathbf{N}\to G$ 是同态。若 $G$ 为群，可以把 $f$ 延拓为从 $\mathbf{Z}$ 到 $G$ 的同态（如前面所指出的，对所有 $n\in\mathbf{Z}$ 都定义了 $x^n$）。这些简单的证明留给读者。

设 $n$ 为一个固定的整数，$G$ 为*交换*群。则很容易验证，从 $G$ 到自身的映射

$$
x\mapsto x^n
$$

为同态。映射 $x\mapsto x^{-1}$ 也为同态。映射 $x\mapsto x^n$ 称为 $n$ 次**幂映射**。

**例。** 设 $I=\{i\}$ 为指标集合，$\{G_i\}$ 为一个群族。令 $G=\prod G_i$ 为它们的直积。设

$$
p_i:G\to G_i
$$

为到第 $i$ 个因子的投影。则 $p_i$ 为同态。

*设 $G$ 为群，$S$ 为 $G$ 的一个生成元集合，$G'$ 为另一个群。设 $f:S\to G'$ 为映射。若存在从 $G$ 到 $G'$ 的同态 $\tilde f$，其在 $S$ 上的限制为 $f$，则这样的同态只有一个。*

<span class="original-page-anchor" id="pdf-page-26" aria-hidden="true"></span>

换句话说，$f$ 至多能以一种方式延拓为从 $G$ 到 $G'$ 的同态。这一点显然成立，但在后文中将多次用到。

设 $f:G\to G'$ 和 $g:G'\to G''$ 为两个群同态。则复合映射 $g\circ f$ 为群同态。若 $f,g$ 为同构，则 $g\circ f$ 也为同构。此外，$f^{-1}:G'\to G$ 也为同构。特别地，$G$ 的所有自同构组成的集合本身是群，记为 $\operatorname{Aut}(G)$。

设 $f:G\to G'$ 为群同态，$e,e'$ 分别为 $G,G'$ 的单位元。定义 $f$ 的**核**为 $G$ 中由所有满足 $f(x)=e'$ 的 $x$ 组成的子集。由定义立即可知，$f$ 的核 $H$ 为 $G$ 的子群。（例如，我们来证明 $H$ 对取逆映射封闭。设 $x\in H$。则

$$
f(x^{-1})f(x)=f(e)=e'.
$$

由于 $f(x)=e'$，有 $f(x^{-1})=e'$，由此 $x^{-1}\in H$。其余验证留给读者。）

再次设 $f:G\to G'$ 为群同态，$H'$ 为 $f$ 的像。则 $H'$ 为 $G'$ 的子群，因为它包含 $e'$，并且若 $f(x),f(y)\in H'$，则 $f(xy)=f(x)f(y)$ 也属于 $H'$。此外，$f(x^{-1})=f(x)^{-1}$ 属于 $H'$，因此 $H'$ 为 $G'$ 的子群。

$f$ 的核与像有时记为 $\operatorname{Ker}f$ 和 $\operatorname{Im}f$。

若同态 $f:G\to G'$ 在 $G$ 与它在 $G'$ 中的像之间建立了同构，则也称它为**嵌入**。

*核为平凡子群的同态是单射。*

为证明这一点，假设 $f$ 的核为平凡子群，并设某些 $x,y\in G$ 满足 $f(x)=f(y)$。乘以 $f(y^{-1})$，得到

$$
f(xy^{-1})=f(x)f(y^{-1})=e'.
$$

因此 $xy^{-1}$ 属于核，所以 $xy^{-1}=e$，从而 $x=y$。特别地，若 $f$ 还是满射，则 $f$ 为同构。因此，核为平凡子群的满同态必为同构。注意，单射同态是嵌入。

单射同态常用特殊的箭头表示，例如

$$
f:G\hookrightarrow G'.
$$

一个群是否为子群的直积，有如下有用的判别准则：

**命题 2.1。** *设 $G$ 为群，$H,K$ 为两个子群，满足 $H\cap K=e$、$HK=G$，并且对所有 $x\in H$ 和 $y\in K$ 都有 $xy=yx$。则满足 $(x,y)\mapsto xy$ 的映射*

$$
H\times K\to G
$$

*为同构。*

*证明。* 它显然是同态；由于 $HK=G$，它是满射。

<span class="original-page-anchor" id="pdf-page-27" aria-hidden="true"></span>

若 $(x,y)$ 属于其核，则 $x=y^{-1}$，因此 $x$ 同时属于 $H$ 与 $K$，于是 $x=e$，故也有 $y=e$，所以我们的映射是同构。

注意，命题 2.1 可以通过归纳推广到有限个子群 $H_1,\ldots,H_n$ 的情形：这些子群的元素彼此交换，并满足

$$
H_1\cdots H_n=G,
$$

以及

$$
H_{i+1}\cap(H_1\cdots H_i)=e.
$$

在这种情况下，$G$ 同构于直积

$$
H_1\times\cdots\times H_n.
$$

设 $G$ 为群，$H$ 为子群。$H$ 在 $G$ 中的一个**左陪集**是 $G$ 的形如 $aH$ 的子集，其中 $a$ 为 $G$ 的某个元素。$aH$ 的一个元素称为 $aH$ 的一个**陪集代表元**。映射 $x\mapsto ax$ 诱导了从 $H$ 到 $aH$ 的双射。因此，任意两个左陪集具有相同的基数。

注意，若 $a,b$ 为 $G$ 的元素，且陪集 $aH,bH$ 有一个公共元素，则它们相等。事实上，设 $ax=by$，其中 $x,y\in H$。则 $a=byx^{-1}$。而 $yx^{-1}\in H$。因此 $aH=b(yx^{-1})H=bH$，因为对任意 $z\in H$ 都有 $zH=H$。

由此可知，$G$ 是 $H$ 的所有左陪集的不交并。对于**右陪集**（即 $G$ 的形如 $Ha$ 的子集），也有类似结论。$H$ 在 $G$ 中的左陪集个数记为 $(G:H)$，称为 $H$ 在 $G$ 中的（左）**指数**。平凡子群的指数称为 $G$ 的**阶**，记为 $(G:1)$。由上述结论，得到：

**命题 2.2。** *设 $G$ 为群，$H$ 为子群。则*

$$
(G:H)(H:1)=(G:1),
$$

*其含义是：若这三个指数中的两个有限，则第三个也有限，且上述等式成立。若 $(G:1)$ 有限，则 $H$ 的阶整除 $G$ 的阶。*

*更一般地，设 $H,K$ 为 $G$ 的子群，且 $H\supset K$。设 $\{x_i\}$ 为 $K$ 在 $H$ 中的一个（左）陪集代表元集合，$\{y_j\}$ 为 $H$ 在 $G$ 中的一个陪集代表元集合。则我们断言，$\{y_jx_i\}$ 是 $K$ 在 $G$ 中的一个陪集代表元集合。*

*证明。* 注意

$$
\begin{aligned}
H&=\bigcup_i x_iK&&\text{（不交）},\\
G&=\bigcup_j y_jH&&\text{（不交）}.
\end{aligned}
$$

因此

$$
G=\bigcup_{i,j}y_jx_iK.
$$

我们必须证明这个并是不交的，即 $y_jx_i$ 代表不同的陪集。假设

<span class="original-page-anchor" id="pdf-page-28" aria-hidden="true"></span>

$$
y_jx_iK=y_{j'}x_{i'}K
$$

其中 $(j,i)$ 和 $(j',i')$ 是两对指标。在右侧乘以 $H$，并注意到 $x_i,x_{i'}$ 都在 $H$ 中，我们得到

$$
y_jH=y_{j'}H,
$$

由此 $y_j=y_{j'}$。于是 $x_iK=x_{i'}K$，从而 $x_i=x_{i'}$，这就证明了所需结论。

因此，命题 2.2 中的公式可以推广为

$$
(G:K)=(G:H)(H:K),
$$

其含义是：这个公式中出现的三个指数，只要其中两个有限，则第三个也有限，而且公式成立。

以上结果始终讨论的是左陪集。对于右陪集，参见习题 10。

**例。** 素数阶群是循环群。事实上，设 $G$ 的阶为 $p$，并取 $a\in G$，$a\ne e$。设 $H$ 为 $a$ 生成的子群。那么 $\#(H)$ 整除 $p$，且 $\#(H)\ne1$，所以 $\#(H)=p$，从而 $H=G$，因此 $G$ 是循环群。

**例。** 设 $J_n=\{1,\ldots,n\}$，设 $S_n$ 为 $J_n$ 上的置换群。我们把满足以下条件的置换 $\tau$ 称为**对换**：$J_n$ 中存在两个元素 $r\ne s$，使得 $\tau(r)=s$、$\tau(s)=r$，且对一切 $k\ne r,s$ 都有 $\tau(k)=k$。注意，对换生成 $S_n$。事实上，设 $\sigma$ 为一个置换，$\sigma(n)=k\ne n$。设 $\tau$ 为交换 $k,n$ 的对换。那么 $\tau\sigma$ 固定 $n$；利用归纳法，可以将 $\tau\sigma$ 写成 $\operatorname{Perm}(J_{n-1})$ 中若干对换的乘积，由此证明了对换生成 $S_n$。

接着注意到 $\#(S_n)=n!$。事实上，设 $H$ 为 $S_n$ 中所有固定 $n$ 的元素构成的子群。那么可以把 $H$ 与 $S_{n-1}$ 等同起来。若 $\sigma_i$ $(i=1,\ldots,n)$ 是 $S_n$ 中满足 $\sigma_i(n)=i$ 的元素，则立即可以验证，$\sigma_1,\ldots,\sigma_n$ 是 $H$ 的陪集代表元。因此由归纳法，

$$
(S_n:1)=n(H:1)=n!.
$$

注意，对于 $\sigma_i$，我们可以取交换 $i$ 和 $n$ 的对换 $\tau_i$（$i=n$ 的情形除外，此时可以取 $\sigma_n$ 为恒等置换）。

## §3. 正规子群

我们已经注意到，群同态的核是一个子群。现在我们希望刻画这样的子群。

设 $f:G\to G'$ 为一个群同态，设 $H$ 为它的核。若 $x$ 是 $G$ 的一个元素，则 $xH=Hx$，因为两者都等于 $f^{-1}(f(x))$。我们也可以把这个关系改写为 $xHx^{-1}=H$。

<span class="original-page-anchor" id="pdf-page-29" aria-hidden="true"></span>

反过来，设 $G$ 为一个群，$H$ 为一个子群。假设对于 $G$ 的一切元素 $x$，都有 $xH\subset Hx$（或者等价地，$xHx^{-1}\subset H$）。若用 $x^{-1}$ 代替 $x$，就得到 $H\subset xHx^{-1}$，因此 $xHx^{-1}=H$。所以，我们的条件等价于：对一切 $x\in G$，都有 $xHx^{-1}=H$。满足这个条件的子群 $H$ 称为**正规子群**。现在我们将看到，正规子群就是某个同态的核。

设 $G'$ 为 $H$ 的陪集所构成的集合。（根据假设，左陪集等于右陪集，因此不必区分它们。）若 $xH$ 和 $yH$ 为陪集，则它们的乘积 $(xH)(yH)$ 也是一个陪集，因为

$$
xHyH=xyHH=xyH.
$$

因此，借助这个乘积，我们在 $G'$ 上定义了一个满足结合律的合成法则。显然，陪集 $H$ 本身就是这个合成法则的单位元，而 $x^{-1}H$ 是陪集 $xH$ 的逆元。因此 $G'$ 是一个群。

设 $f:G\to G'$ 为将 $x$ 映为陪集 $xH$ 的映射。那么 $f$ 显然是一个同态，而且（子群）$H$ 包含在它的核中。若 $f(x)=H$，则 $xH=H$。由于 $H$ 包含单位元，可知 $x\in H$。因此 $H$ 就等于这个核，我们得到了所需的同态。

正规子群 $H$ 的陪集所构成的群记为 $G/H$（读作 $G$ 模 $H$，或 $G$ mod $H$）。以上构造的由 $G$ 到 $G/H$ 的满射 $f$ 称为**典范映射**，而 $G/H$ 称为 $G$ 关于 $H$ 的**商群**。

### 注

1. 设 $\{H_i\}_{i\in I}$ 为 $G$ 的一族正规子群。那么子群

$$
H=\bigcap_{i\in I}H_i
$$

是一个正规子群。事实上，若 $y\in H$ 且 $x\in G$，则 $xyx^{-1}$ 属于每个 $H_i$，因而属于 $H$。

2. 设 $S$ 为 $G$ 的一个子集，设 $N=N_S$ 为满足 $xSx^{-1}=S$ 的所有元素 $x\in G$ 构成的集合。那么 $N$ 显然是 $G$ 的一个子群，称为 $S$ 的**正规化子**。若 $S$ 仅由一个元素 $a$ 组成，则 $N$ 也称为 $a$ 的**中心化子**。更一般地，设 $Z_S$ 为满足对一切 $y\in S$ 都有 $xyx^{-1}=y$ 的所有元素 $x\in G$ 构成的集合。那么 $Z_S$ 称为 $S$ 的**中心化子**。$G$ 本身的中心化子称为 $G$ 的**中心**。它是由 $G$ 中所有与其他一切元素可交换的元素构成的子群，而且显然是 $G$ 的正规子群。

**例。** 以后，当我们有更多定理可用来证明正规性时，将给出更多正规子群的例子。这里仅给出两个例子。

首先，由线性代数可知，行列式是从方阵的乘法群到一个域的乘法群的同态。它的核称为**特殊线性群**，并且是正规子群。

<span class="original-page-anchor" id="pdf-page-30" aria-hidden="true"></span>

其次，设 $G$ 为形如 $T_{a,b}:\mathbf{R}\to\mathbf{R}$ 的所有映射构成的集合，其中 $T_{a,b}(x)=ax+b$，$a\ne0$，$b$ 任意。那么 $G$ 在映射的复合运算下构成一个群。设 $A$ 为形如 $T_{a,0}$ 的映射构成的乘法群（它同构于 $\mathbf{R}^*$，即 $\mathbf{R}$ 中非零元素构成的群），并设 $N$ 为平移 $T_{1,b}$（$b\in\mathbf{R}$）构成的群。读者立即可以验证，$T_{a,b}\mapsto a$ 是从 $G$ 到这个乘法群的满同态，其核为平移群，因此平移群是正规子群。此外，我们有 $G=AN=NA$，且 $N\cap A=\{\mathrm{id}\}$。按照习题 12 的术语，$G$ 是 $A$ 与 $N$ 的**半直积**。

设 $H$ 为 $G$ 的一个子群。那么 $H$ 显然是其正规化子 $N_H$ 的正规子群。以下命题留作习题：

*若 $K$ 为 $G$ 的任意一个包含 $H$、且使 $H$ 在 $K$ 中正规的子群，则 $K\subset N_H$。*

*若 $K$ 是 $N_H$ 的一个子群，则 $KH$ 是一个群，而且 $H$ 在 $KH$ 中正规。*

*$H$ 的正规化子是 $G$ 中使 $H$ 正规的最大子群。*

设 $G$ 为一个群，$H$ 为一个正规子群。设 $x,y\in G$。如果 $x$ 与 $y$ 属于 $H$ 的同一个陪集，或者等价地，如果 $xy^{-1}$（或 $y^{-1}x$）属于 $H$，我们记为

$$
x\equiv y\pmod H.
$$

这个关系读作“$x$ 与 $y$ 模 $H$ 同余”。

当 $G$ 为加法群时，

$$
x\equiv0\pmod H
$$

表示 $x$ 属于 $H$，而

$$
x\equiv y\pmod H
$$

表示 $x-y$（或 $y-x$）属于 $H$。这个同余记号主要用于加法群。

设

$$
G'\xrightarrow{f}G\xrightarrow{g}G''
$$

为一个同态序列。若 $\operatorname{Im}f=\operatorname{Ker}g$，则称此序列是**正合的**。例如，若 $H$ 是 $G$ 的正规子群，则序列

$$
H\xrightarrow{j}G\xrightarrow{\varphi}G/H
$$

是正合的（其中 $j=\text{包含映射}$，$\varphi=\text{典范映射}$）。具有多个项的同态序列，例如

$$
G_1\xrightarrow{f_1}G_2\xrightarrow{f_2}G_3\to\cdots\xrightarrow{f_{n-1}}G_n,
$$

若在每一个衔接处都正合，即对每个 $i=1,\ldots,n-2$，都有

$$
\operatorname{Im}f_i=\operatorname{Ker}f_{i+1},
$$

则称该序列是**正合的**。

例如，令 $0$ 表示平凡群，说序列

$$
0\to G'\xrightarrow{f}G\xrightarrow{g}G''\to0
$$

<span class="original-page-anchor" id="pdf-page-31" aria-hidden="true"></span>

正合，就是说 $f$ 是单射，$\operatorname{Im}f=\operatorname{Ker}g$，且 $g$ 是满射。若 $H=\operatorname{Ker}g$，那么此序列本质上等同于正合序列

$$
0\to H\to G\to G/H\to0.
$$

更确切地说，存在一个交换图

$$
\begin{array}{ccccccccc}
0&\longrightarrow&G'&\xrightarrow{f}&G&\xrightarrow{g}&G''&\longrightarrow&0\\
&&\downarrow&&\downarrow&&\downarrow&&\\
0&\longrightarrow&H&\longrightarrow&G&\longrightarrow&G/H&\longrightarrow&0
\end{array}
$$

其中竖直映射都是同构，而且两行都是正合的。

接下来，我们描述若干同态，这些同态都称为**典范同态**。

**(i)** 设 $G,G'$ 为群，$f:G\to G'$ 为核是 $H$ 的一个同态。设 $\varphi:G\to G/H$ 为典范映射。那么存在唯一的同态 $f_*:G/H\to G'$，使得 $f=f_*\circ\varphi$，而且 $f_*$ 是单射。

为了定义 $f_*$，设 $xH$ 为 $H$ 的一个陪集。由于对一切 $y\in H$ 都有 $f(xy)=f(x)$，我们定义 $f_*(xH)$ 为 $f(x)$。这个值与陪集代表元 $x$ 的选取无关；随后容易验证，$f_*$ 是一个同态，是单射，而且是满足我们要求的唯一同态。我们称 $f_*$ 是由 $f$ **诱导**的。

我们的同态 $f_*$ 诱导出一个同构

$$
\lambda:G/H\to\operatorname{Im}f,
$$

它将 $G/H$ 映到 $f$ 的像上。因此，$f$ 可以分解为以下一串同态的复合：

$$
G\xrightarrow{\varphi}G/H\xrightarrow{\lambda}\operatorname{Im}f\xrightarrow{j}G'.
$$

这里，$j$ 是 $\operatorname{Im}f$ 到 $G'$ 的包含映射。

**(ii)** 设 $G$ 为一个群，$H$ 为一个子群。设 $N$ 为所有包含 $H$ 的正规子群的交。那么 $N$ 是正规的，因此是 $G$ 中包含 $H$ 的最小正规子群。设 $f:G\to G'$ 为一个核包含 $H$ 的同态。那么 $f$ 的核包含 $N$，并且存在唯一的同态 $f_*:G/N\to G'$，称为由 $f$ 诱导的同态，使下图交换：

$$
\begin{array}{ccc}
G&\xrightarrow{f}&G'\\
{}_{\varphi}\searrow&&\nearrow_{f_*}\\
&G/N&
\end{array}
$$

和前面一样，$\varphi$ 是典范映射。

我们可以如 (1) 中那样，按规则

$$
f_*(xN)=f(x)
$$

定义 $f_*$。

这个定义是良定的，而且容易验证它满足我们的全部要求。

<span class="original-page-anchor" id="pdf-page-32" aria-hidden="true"></span>

**(iii)** 设 $G$ 为群，$H\supset K$ 为 $G$ 的两个正规子群。那么 $K$ 在 $H$ 中正规；把每个陪集 $xK$ 对应到陪集 $xH$，就定义了从 $G/K$ 到 $G/H$ 的一个满射。立即可以验证，这个映射是一个同态，其核由所有满足 $x\in H$ 的陪集 $xK$ 构成。因此，我们有一个典范同构

$$
\boxed{(G/K)/(H/K)\approx G/H.}
$$

也可以利用 (i) 和 (ii) 描述这个同构。我们把证明下图交换留给读者：

$$
\begin{array}{ccccccccc}
0&\longrightarrow&H&\longrightarrow&G&\longrightarrow&G/H&\longrightarrow&0\\
&&\downarrow\scriptstyle\mathrm{can}&&\downarrow\scriptstyle\mathrm{can}&&\downarrow\scriptstyle\mathrm{id}&&\\
0&\longrightarrow&H/K&\longrightarrow&G/K&\longrightarrow&G/H&\longrightarrow&0
\end{array}
$$

其中两行都是正合的。

**(iv)** 设 $G$ 为一个群，$H,K$ 为两个子群。假设 $H$ 包含在 $K$ 的正规化子中。那么 $H\cap K$ 显然是 $H$ 的正规子群，同样显然，$HK=KH$ 是 $G$ 的一个子群。存在一个满同态

$$
H\to HK/K,
$$

它把每个 $x\in H$ 对应到群 $HK$ 中 $K$ 的陪集 $xK$。读者立即可以验证，此同态的核恰为 $H\cap K$。因此我们有一个典范同构

$$
\boxed{H/(H\cap K)\approx HK/K.}
$$

**(v)** 设 $f:G\to G'$ 为一个群同态，设 $H'$ 为 $G'$ 的正规子群，并令 $H=f^{-1}(H')$。

$$
\begin{array}{ccc}
G&\longrightarrow&G'\\
\uparrow&&\uparrow\\
f^{-1}(H')&\longrightarrow&H'
\end{array}
$$

那么 $f^{-1}(H')$ 在 $G$ 中正规。［*证明：* 若 $x\in G$，则 $f(xHx^{-1})=f(x)f(H)f(x)^{-1}$ 包含在 $H'$ 中，所以 $xHx^{-1}\subset H$。］于是，将 $f$ 与从 $G'$ 到 $G'/H'$ 的典范满射复合，得到一个同态

$$
G\to G'\to G'/H',
$$

而这个复合同态的核为 $H$。因此我们得到一个单同态

$$
\bar f:G/H\to G'/H'
$$

<span class="original-page-anchor" id="pdf-page-33" aria-hidden="true"></span>

它也称为典范同态，并给出交换图

$$
\begin{array}{ccccccccc}
0&\longrightarrow&H&\longrightarrow&G&\longrightarrow&G/H&\longrightarrow&0\\
&&\downarrow&&\downarrow\scriptstyle f&&\downarrow\scriptstyle\bar f&&\\
0&\longrightarrow&H'&\longrightarrow&G'&\longrightarrow&G'/H'&\longrightarrow&0.
\end{array}
$$

若 $f$ 是满射，则 $\bar f$ 是同构。

现在我们将描述上述同态结论的一些应用。

设 $G$ 为一个群。子群序列

$$
G=G_0\supset G_1\supset G_2\supset\cdots\supset G_m
$$

称为一个子群**塔**。若每个 $G_{i+1}$ 都在 $G_i$ 中正规 $(i=0,\ldots,m-1)$，则称此塔是**正规的**。若它正规，而且每个商群 $G_i/G_{i+1}$ 都是阿贝尔群（分别为循环群），则称此塔为**阿贝尔塔**（分别为**循环塔**）。

设 $f:G\to G'$ 为一个同态，设

$$
G'=G'_0\supset G'_1\supset\cdots\supset G'_m
$$

为 $G'$ 中的一个正规塔。令 $G_i=f^{-1}(G'_i)$。那么这些 $G_i$ $(i=0,\ldots,m)$ 构成一个正规塔。若这些 $G'_i$ 构成阿贝尔塔（分别为循环塔），则这些 $G_i$ 也构成阿贝尔塔（分别为循环塔），因为对每个 $i$，我们都有一个单同态

$$
G_i/G_{i+1}\to G'_i/G'_{i+1},
$$

而且阿贝尔群（分别为循环群）的子群也是阿贝尔群（分别为循环群）。

塔

$$
G=G_0\supset G_1\supset\cdots\supset G_m
$$

的一个**加细**，是指通过在给定的塔中插入有限个子群所得到的塔。若一个群有一个阿贝尔塔，其最后一个元素是平凡子群（即在上述记号下，$G_m=\{e\}$），则称这个群是**可解的**。

**命题 3.1。** *设 $G$ 为一个有限群。$G$ 的一个阿贝尔塔有一个循环加细。设 $G$ 为一个有限可解群。那么 $G$ 有一个最后一项为 $\{e\}$ 的循环塔。*

*证明。* 第二个断言是第一个断言的直接推论，而且显然只需证明：若 $G$ 是有限阿贝尔群，则 $G$ 有一个以 $\{e\}$ 结尾的循环塔。我们对 $G$ 的阶使用归纳法。设 $x$ 为 $G$ 的一个元素。可以假设 $x\ne e$。设 $X$ 为 $x$ 生成的循环群。令 $G'=G/X$。由归纳法，我们可以在 $G'$ 中找到一个循环塔，它的逆像就是 $G$ 中最后一项为 $X$ 的循环塔。若在该塔末尾插入 $\{e\}$ 使其加细，就得到所需的循环塔。

**例。** 在定理 6.5 中，将证明阶为素数幂的群是可解的。

<span class="original-page-anchor" id="pdf-page-34" aria-hidden="true"></span>

**例。** 群论的重大结果之一是 Feit–Thompson 定理：所有奇数阶有限群都是可解群。参见 [Go 68]。

**例。** 在域论中，可解群将作为可解扩张的伽罗瓦群出现。参见第 VI 章定理 7.2。

**例。** 我们假设读者熟悉线性代数的基本概念。设 $k$ 为一个域。设 $G=GL(n,k)$ 为 $k$ 上可逆 $n\times n$ 矩阵构成的群。设 $T=T(n,k)$ 为上三角群，即由主对角线以下的元素均为 $0$ 的矩阵构成的子群。设 $D$ 为主对角线上元素均非零的对角矩阵构成的对角群。设 $N$ 为主对角线上及其以下的元素均为 $0$ 的矩阵构成的加法群，并令 $U=I+N$，其中 $I$ 为 $n\times n$ 单位矩阵。那么 $U$ 是 $G$ 的一个子群。（注意，$N$ 由幂零矩阵构成，即矩阵 $A$ 满足对某个正整数 $m$，有 $A^m=0$。此时可用几何级数计算得 $(I-A)^{-1}=I+A+A^2+\cdots+A^{m-1}$。）给定矩阵 $A\in T$，令 $\operatorname{diag}(A)$ 为主对角线上的元素与 $A$ 相同的对角矩阵。读者可以验证，由此得到一个满同态

$$
T\to D,\qquad A\mapsto\operatorname{diag}(A).
$$

这个同态的核恰为 $U$。更一般地，注意当 $r\ge2$ 时，集合 $N^{r-1}$ 由以下形式的所有矩阵构成：

![矩阵 M，保留原书的确切元素及下标](/library/volume-86/diagrams/pdf-0034-matrix.png)

令 $U_r=I+N^r$。那么 $U_1=U$，且 $U_r\supset U_{r+1}$。此外，$U_{r+1}$ 在 $U_r$ 中正规，而商群同构于加法群（！）$k^{n-r}$；该同构由将 $I+M$ 映为 $n-r$ 元组 $(a_{1r+1},\ldots,a_{n-r,n})\in k^{n-r}$ 的映射给出。这个 $n-r$ 元组可以称为第 $r$ 条上对角线。因此我们得到一个阿贝尔塔

$$
T\supset U=U_1\supset U_2\supset\cdots\supset U_n=\{I\}.
$$

**定理 3.2。** *设 $G$ 为一个群，$H$ 为一个正规子群。那么 $G$ 可解，当且仅当 $H$ 与 $G/H$ 都可解。*

*证明。* 我们证明 $G$ 可解蕴含 $H$ 可解。设 $G=G_0\supset G_1\supset\cdots\supset G_r=\{e\}$ 为一个群塔，其中 $G_{i+1}$ 在 $G_i$ 中正规，且 $G_i/G_{i+1}$ 是阿贝尔群。令 $H_i=H\cap G_i$。那么 $H_{i+1}$ 在 $H_i$ 中正规，而且我们有嵌入 $H_i/H_{i+1}\to G_i/G_{i+1}$，因此 $H_i/H_{i+1}$ 是阿贝尔群，由此证明 $H$ 可解。其他断言的证明留给读者。

<span class="original-page-anchor" id="pdf-page-35" aria-hidden="true"></span>

设 $G$ 为一个群。$G$ 中的一个**交换子**，是指形如 $xyx^{-1}y^{-1}$ 的群元素，其中 $x,y\in G$。设 $G^c$ 为 $G$ 中由交换子生成的子群。我们称 $G^c$ 为 $G$ 的**交换子群**。作为习题，请证明：$G^c$ 在 $G$ 中正规，而且每个到交换群 $G'$ 的同态 $f:G\to G'$，其核都包含 $G^c$，因而该同态经由交换子商群 $G/G^c$ 分解。注意，$G/G^c$ 本身是交换群。事实上，若用 $\bar x$ 表示 $x$ 在 $G/G^c$ 中的像，则根据定义，$\bar x\bar y\bar x^{-1}\bar y^{-1}=\bar e$，所以 $\bar x$ 与 $\bar y$ 可交换。结合可解性的定义，显然，交换子群是可解性与不可解性问题的核心。

若群 $G$ 非平凡，而且除了 $\{e\}$ 和 $G$ 本身以外没有其他正规子群，则称 $G$ 为**单群**。

**例。** 阿贝尔群是单群，当且仅当它是素数阶循环群。事实上，假设 $A$ 是非平凡阿贝尔群。取 $a\in A$，$a\ne e$。若 $a$ 生成一个无限循环群，则 $a^2$ 生成一个真子群，因此 $A$ 不是单群。若 $a$ 的周期有限，且 $A$ 是单群，则 $A=\langle a\rangle$。设周期为 $n$，并假设 $n$ 不是素数。写成 $n=rs$，其中 $r,s>1$。那么 $a^r\ne e$，而且 $a^r$ 生成一个真子群，这与 $A$ 的单性矛盾。因此 $a$ 的周期是素数，$A$ 是阶为 $p$ 的循环群。

**例。** 利用交换子，我们将在定理 5.5 中给出单群的例子（交错群），并在第 XIII 章定理 9.2 中给出另一个例子（$PSL_n(F)$，一个将在该章定义的矩阵群）。由于非循环的单群不可解，我们也就得到不可解群的例子。

有限群论中的一项重大计划，是对所有有限单群进行分类。基本上，它们中的大多数（即使不是全部）都可以自然地表示为适当的域上适当向量空间的线性映射群的子群。有关综述，参见 [Go 82]、[Go 86]、[Sol 01]。一些声称完成的证明已被发现存在漏洞。截至 2001 年，这些证明仍不完整。

接下来，我们研究商群 $G_i/G_{i+1}$ 都为单群的子群塔。下一个引理将用于 Jordan–Hölder 定理和 Schreier 定理的证明。

**引理 3.3（蝴蝶引理）。**（Zassenhaus）*设 $U,V$ 为一个群的子群。设 $u,v$ 分别为 $U$ 与 $V$ 的正规子群。那么*

$$
u(U\cap v)\quad\text{在}\quad u(U\cap V)\quad\text{中正规},
$$

$$
(u\cap V)v\quad\text{在}\quad(U\cap V)v\quad\text{中正规},
$$

*而且相应的商群同构，即*

$$
u(U\cap V)/u(U\cap v)\approx(U\cap V)v/(u\cap V)v.
$$

*证明。* 把下面的子群图画出来，就可以清楚地看出这些群与商群的组合关系（引理的名称正来自这个图）：

<span class="original-page-anchor" id="pdf-page-36" aria-hidden="true"></span>

![蝴蝶引理的子群图，保留原书全部标记、线段及商群标记](/library/volume-86/diagrams/pdf-0036-butterfly.png)

在这个图中，$U,u,V,v$ 是给定的。图中其他所有点都对应于某些群，可以按以下方式确定。两条向下的线段的交点表示群的交。两条向上的线段相交于一个点，该点表示两个子群的乘积（即包含这两个子群的最小子群）。

考虑表示蝴蝶双翼的两个平行四边形，我们将给出商群的下列同构：

$$
\frac{u(U\cap V)}{u(U\cap v)}\approx\frac{U\cap V}{(u\cap V)(U\cap v)}\approx\frac{(U\cap V)v}{(u\cap V)v}.
$$

事实上，两个平行四边形共有的竖边，其上端点为 $U\cap V$，下端点为 $(u\cap V)(U\cap v)$。我们有一个同构

$$
(U\cap V)/(u\cap V)(U\cap v)\approx u(U\cap V)/u(U\cap v).
$$

令 $H=U\cap V$，$N=u(U\cap v)$，由同构定理

$$
H/(H\cap N)\approx HN/N
$$

即可得到这个同构。这给出了左边的同构。利用对称性可得到右边相应的同构，从而证明了蝴蝶引理。

设 $G$ 为一个群，并设

$$
G=G_1\supset G_2\supset\cdots\supset G_r=\{e\},
$$

$$
G=H_1\supset H_2\supset\cdots\supset H_s=\{e\}
$$

为以平凡群结尾的正规子群塔。若 $r=s$，而且存在一个指标的置换，则称这两个塔是**等价的**；

<span class="original-page-anchor" id="pdf-page-37" aria-hidden="true"></span>

这些指标为 $i=1,\ldots,r-1$，置换记作 $i\mapsto i'$，并满足

$$
G_i/G_{i+1}\approx H_{i'}/H_{i'+1}.
$$

换言之，除了同构与指标的置换之外，这两个塔中的商群序列是相同的。

**定理 3.4。**（Schreier）*设 $G$ 为一个群。两个以平凡群结尾的正规子群塔有等价的加细。*

*证明。* 设这两个塔如上。对每个 $i=1,\ldots,r-1$ 和 $j=1,\ldots,s$，定义

$$
G_{ij}=G_{i+1}(H_j\cap G_i).
$$

那么 $G_{is}=G_{i+1}$，我们得到第一个塔的一个加细：

$$
\begin{aligned}
G=G_{11}&\supset G_{12}\supset\cdots\supset G_{1,s-1}\supset G_2\\
&=G_{21}\supset G_{22}\supset\cdots\supset G_{r-1,1}\supset\cdots\supset G_{r-1,s-1}\supset\{e\}.
\end{aligned}
$$

同样，对 $j=1,\ldots,s-1$ 和 $i=1,\ldots,r$，定义

$$
H_{ji}=H_{j+1}(G_i\cap H_j).
$$

这给出了第二个塔的一个加细。根据蝴蝶引理，对 $i=1,\ldots,r-1$ 和 $j=1,\ldots,s-1$，我们有同构

$$
G_{ij}/G_{i,j+1}\approx H_{ji}/H_{j,i+1}.
$$

我们把每个加细后的塔看作有 $(r-1)(s-1)+1$ 个元素：第一个塔中为 $G_{ij}$ $(i=1,\ldots,r-1;j=1,\ldots,s-1)$ 与 $\{e\}$，第二个塔中为 $H_{ji}$ 与 $\{e\}$。对于每一对指标 $(i,j)$，上述同构表明，加细后的两个塔是等价的，这就证明了所需结论。

若群 $G$ 非平凡，而且除了 $\{e\}$ 和 $G$ 本身以外没有其他正规子群，则称 $G$ 为**单群**。

**定理 3.5。**（Jordan–Hölder）*设 $G$ 为一个群，并设*

$$
G=G_1\supset G_2\supset\cdots\supset G_r=\{e\}
$$

*为一个正规塔，使得每个群 $G_i/G_{i+1}$ 都为单群，且对 $i=1,\ldots,r-1$，有 $G_i\ne G_{i+1}$。那么 $G$ 的任何另一个具有同样性质的正规塔，都与此塔等价。*

*证明。* 给定此塔的一个如前所述的加细 $\{G_{ij}\}$，我们注意到：对每个 $i$，恰好存在一个指标 $j$，使得 $G_i/G_{i+1}=G_{ij}/G_{i,j+1}$。因此，原来的塔与加细后的塔具有相同的非平凡商群序列。这就证明了我们的定理。

<span class="original-page-anchor" id="pdf-page-38" aria-hidden="true"></span>

### 参考文献

[Go 68] D. Gorenstein，《有限群》（*Finite groups*），Harper and Row，1968。

[Go 82] D. Gorenstein，《有限单群》（*Finite simple groups*），Plenum Press，1982。

[Go 83] D. Gorenstein，《有限单群的分类》（*The Classification of Finite Simple Groups*），Plenum Press，1983。

[Go 86] D. Gorenstein，“有限单群的分类”（Classifying the finite simple groups），*Bull. AMS* **14**，第 1 期（1986），第 1–98 页。

[So 01] R. Solomon，“有限单群分类简史”（A brief history of the classification of the finite simple groups），*Bull. AMS* **38**，第 3 期（2001），第 315–352 页。

## §4. 循环群

整数 $\mathbf Z$ 构成一个加法群。我们将确定它的子群。设 $H$ 是 $\mathbf Z$ 的一个子群。若 $H$ 非平凡，令 $a$ 为 $H$ 中最小的正整数。我们断言，$H$ 由所有形如 $na$（$n\in\mathbf Z$）的元素组成。为证明这一点，取 $y\in H$。存在整数 $n,r$，满足 $0\leq r<a$，使得

$$
y=na+r.
$$

由于 $H$ 是子群，且 $r=y-na$，我们有 $r\in H$，于是 $r=0$，从而得到我们的断言。

设 $G$ 是一个群。如果存在 $G$ 的一个元素 $a$，使 $G$ 的每一个元素 $x$ 都可以写成 $a^n$ 的形式，其中 $n\in\mathbf Z$，我们就称 $G$ 是**循环群**（换言之，满足 $f(n)=a^n$ 的映射 $f:\mathbf Z\to G$ 是满射）。此时，$G$ 的这样的元素 $a$ 称为 $G$ 的一个**生成元**。

设 $G$ 是一个群，$a\in G$。所有元素 $a^n$（$n\in\mathbf Z$）组成的子集显然是 $G$ 的一个循环子群。若整数 $m$ 满足 $a^m=e$ 且 $m>0$，我们便称 $m$ 为 $a$ 的一个**指数**。若对所有 $x\in G$ 都有 $x^m=e$，我们就称 $m>0$ 为 $G$ 的一个**指数**。

设 $G$ 是一个群，$a\in G$。令 $f:\mathbf Z\to G$ 为满足 $f(n)=a^n$ 的同态，令 $H$ 为 $f$ 的核。有以下两种情形：

**1.** 核是平凡的。此时 $f$ 是从 $\mathbf Z$ 到 $G$ 中由 $a$ 生成的循环子群的同构，该子群是无限循环群。如果 $a$ 生成 $G$，那么 $G$ 是循环群。我们也说 $a$ 具有**无限周期**。

**2.** 核非平凡。令 $d$ 为核中最小的正整数。此时 $d$ 称为 $a$ 的**周期**。若整数 $m$ 满足 $a^m=e$，则对于某个整数 $s$ 有 $m=ds$。我们注意到，元素 $e,a,\ldots,a^{d-1}$ 是<span class="original-page-anchor" id="pdf-page-39" aria-hidden="true"></span>互不相同的。事实上，若 $a^r=a^s$，其中 $0\leq r,s\leq d-1$，且不妨设 $r\leq s$，则 $a^{s-r}=e$。由于 $0\leq s-r<d$，必有 $s-r=0$。由 $a$ 生成的循环子群的阶为 $d$。因此，由命题 2.2 得到：

**命题 4.1.** *设 $G$ 是阶为 $n>1$ 的有限群。设 $a$ 是 $G$ 的一个元素，且 $a\neq e$。则 $a$ 的周期整除 $n$。若 $G$ 的阶是一个素数 $p$，则 $G$ 是循环群，且任一生成元的周期都等于 $p$。*

此外：

**命题 4.2.** *设 $G$ 是一个循环群。则 $G$ 的每个子群都是循环群。如果 $f$ 是 $G$ 的一个同态，则 $f$ 的像是循环群。*

*证明。* 若 $G$ 是无限循环群，则它同构于 $\mathbf Z$；而我们已经在上面确定了 $\mathbf Z$ 的所有子群，发现它们全都是循环群。若 $f:G\to G'$ 是一个同态，且 $a$ 是 $G$ 的一个生成元，则 $f(a)$ 显然是 $f(G)$ 的一个生成元，因而 $f(G)$ 是循环群，所以 $f$ 的像是循环群。接着，令 $H$ 为 $G$ 的一个子群。我们要证明 $H$ 是循环群。令 $a$ 为 $G$ 的一个生成元。于是存在一个满同态 $f:\mathbf Z\to G$，满足 $f(n)=a^n$。原像 $f^{-1}(H)$ 是 $\mathbf Z$ 的一个子群，因而对于某个正整数 $m$ 等于 $m\mathbf Z$。由于 $f$ 是满射，我们也有一个满同态 $m\mathbf Z\to H$。由于 $m\mathbf Z$ 是循环群（在加法运算下由 $m$ 生成），可知 $H$ 是循环群，命题得证。

我们注意到，两个具有相同阶 $m$ 的循环群是同构的。事实上，若 $G$ 是阶为 $m$、生成元为 $a$ 的循环群，则存在一个满同态 $f:\mathbf Z\to G$，满足 $f(n)=a^n$。若核为 $k\mathbf Z$，其中 $k$ 为正整数，则有同构 $\mathbf Z/k\mathbf Z\approx G$，所以 $k=m$。如果 $u:G_1\to\mathbf Z/m\mathbf Z$ 和 $v:G_2\to\mathbf Z/m\mathbf Z$ 是两个循环群到 $\mathbf Z/m\mathbf Z$ 的同构，则 $v^{-1}\circ u:G_1\to G_2$ 是一个同构。

**命题 4.3.**

(i) *无限循环群恰有两个生成元（若 $a$ 是一个生成元，则 $a^{-1}$ 是另一个且唯一的生成元）。*

(ii) *设 $G$ 是阶为 $n$ 的有限循环群，$x$ 是一个生成元。$G$ 的生成元集合由 $x$ 的那些幂 $x^v$ 组成，其中 $v$ 与 $n$ 互素。*

(iii) *设 $G$ 是一个循环群，$a,b$ 是它的两个生成元。则存在 $G$ 的一个自同构，把 $a$ 映为 $b$。反过来，$G$ 的任一自同构都把 $a$ 映为 $G$ 的某个生成元。*

(iv) *设 $G$ 是阶为 $n$ 的循环群。令 $d$ 为整除 $n$ 的一个正整数。则 $G$ 恰有一个阶为 $d$ 的子群。*

(v) *设 $G_1,G_2$ 分别为阶为 $m,n$ 的循环群。若 $m,n$ 互素，则 $G_1\times G_2$ 是循环群。*

<span class="original-page-anchor" id="pdf-page-40" aria-hidden="true"></span>

(vi) *设 $G$ 是一个有限阿贝尔群。若 $G$ 不是循环群，则存在一个素数 $p$，使得 $G$ 有一个同构于 $C\times C$ 的子群，其中 $C$ 是阶为 $p$ 的循环群。*

*证明。* 前三个断言留给读者证明，我们来证明其余的断言。

**(iv)** 设 $d\mid n$。令 $m=n/d$。令 $f:\mathbf Z\to G$ 为一个满同态。则 $f(m\mathbf Z)$ 是 $G$ 的一个子群，由同构 $\mathbf Z/m\mathbf Z\approx G/f(m\mathbf Z)$，可知 $f(m\mathbf Z)$ 在 $G$ 中的指数为 $m$，所以 $f(m\mathbf Z)$ 的阶为 $d$。反过来，设 $H$ 是一个阶为 $d$ 的子群。则对于某个正整数 $m$ 有 $f^{-1}(H)=m\mathbf Z$，所以 $H=f(m\mathbf Z)$，$\mathbf Z/m\mathbf Z\approx G/H$，因此 $n=md$，$m=n/d$，而 $H$ 被唯一确定。

**(v)** 设 $A=\langle a\rangle$ 和 $B=\langle b\rangle$ 是阶分别为 $m,n$ 的循环群，其中 $m,n$ 互素。考虑同态 $\mathbf Z\to A\times B$，它由 $k\mapsto(a^k,b^k)$ 给出。它的核中的元素必须同时被 $m$ 和 $n$ 整除；由于 $m,n$ 互素，也必被它们的乘积整除。反过来，显然 $mn\mathbf Z$ 包含在核中，所以核就是 $mn\mathbf Z$。由中国剩余定理，$\mathbf Z\to A\times B$ 的像是满的。这证明了 **(v)**。（不了解中国剩余定理的读者，可以参看第 II 章定理 2.2，那里在更一般的情形下给出了证明。）

**(vi)** 循环群的这个刻画是将在 §8 中证明的结构定理的直接推论。因为，若 $G$ 不是循环群，则由定理 8.1 和 **(v)**，可以归结为 $G$ 是一个 $p$ 群的情形；再由定理 8.2，直积（或直和）分解中至少有两个因子，每个因子都包含一个阶为 $p$ 的循环子群，所以 $G$ 包含它们的直积（或直和）。当然，断言 **(vi)** 比完整的结构定理更容易证明；让读者给出直接导出 **(vi)** 的更简单论证，是一个很好的练习。

**注。** 关于循环群的自同构群，参见第 II 章 §2 的末尾。

## §5. 群在集合上的作用

设 $G$ 是一个群，$S$ 是一个集合。$G$ 在 $S$ 上的一个**作用**（operation 或 action），是从 $G$ 到 $S$ 的置换群的一个同态

$$
\pi:G\to\operatorname{Perm}(S).
$$

此时，我们称 $S$ 为一个 **$G$ 集合**。我们用 $\pi_x$ 表示与元素 $x\in G$ 相对应的置换。因此，这个同态记为 $x\mapsto\pi_x$。给定 $s\in S$，$s$ 在置换 $\pi_x$ 下的像为 $\pi_x(s)$。由这样的作用，我们得到一个映射

$$
G\times S\to S,
$$

<span class="original-page-anchor" id="pdf-page-41" aria-hidden="true"></span>

它把每一对满足 $x\in G$ 和 $s\in S$ 的 $(x,s)$ 映为元素 $\pi_x(s)$。我们经常简化记号，用 $xs$ 代替 $\pi_x(s)$。用这个较简洁的记号，有以下两个性质：

*对所有 $x,y\in G$ 和 $s\in S$，都有 $x(ys)=(xy)s$。*

*若 $e$ 是 $G$ 的单位元，则对所有 $s\in S$ 都有 $es=s$。*

反过来，如果给定一个映射 $G\times S\to S$，记为 $(x,s)\mapsto xs$，满足这两个性质，那么对每个 $x\in G$，映射 $s\mapsto xs$ 都是 $S$ 的一个置换，我们把它记为 $\pi_x(s)$。于是 $x\mapsto\pi_x$ 是从 $G$ 到 $\operatorname{Perm}(S)$ 的一个同态。因此，$G$ 在 $S$ 上的作用也可以定义为满足上述两个性质的映射 $G\times S\to S$。以下是把 $G$ 表示成一个置换群的最重要的几个例子。

**1. 共轭。** 对每个 $x\in G$，令 $c_x:G\to G$ 为满足 $c_x(y)=xyx^{-1}$ 的映射。可以立即验证，对应 $x\mapsto c_x$ 是一个同态 $G\to\operatorname{Aut}(G)$，所以这个映射给出 $G$ 在自身上的一个作用，称为**共轭作用**。同态 $x\mapsto c_x$ 的核是 $G$ 的一个正规子群，它由所有满足对每个 $y\in G$ 都有 $xyx^{-1}=y$ 的 $x\in G$ 组成，也就是由那些与 $G$ 的每个元素都可交换的 $x\in G$ 组成。这个核称为 $G$ 的**中心**。形如 $c_x$ 的 $G$ 的自同构称为**内自同构**。

为避免对左作用产生混淆，我们不用 $xy$ 表示 $c_x(y)$。有时写成

$$
c_{x^{-1}}(y)=x^{-1}yx=y^x,
$$

也就是采用指数记号，从而得到如下法则：

$$
y^{(xz)}=(y^x)^z\quad\text{且}\quad y^e=y,
$$

其中 $x,y,z\in G$ 任意。类似地，${}^xy=xyx^{-1}$，且 ${}^z({}^xy)={}^{zx}y$。

我们注意到，$G$ 也以共轭作用作用于 $G$ 的所有子集组成的集合。事实上，令 $S$ 为 $G$ 的所有子集组成的集合，令 $A\in S$ 为 $G$ 的一个子集。则 $xAx^{-1}$ 也是 $G$ 的一个子集，可以记为 $c_x(A)$；很容易验证，映射

$$
(x,A)\mapsto xAx^{-1}
$$

即 $G\times S\to S$ 的这个映射，是 $G$ 在 $S$ 上的一个作用。此外，若 $A$ 是 $G$ 的一个子群，则 $xAx^{-1}$ 也是子群，因此 $G$ 以共轭作用作用于所有子群组成的集合。

若 $A,B$ 是 $G$ 的两个子集，且存在 $x\in G$ 使 $B=xAx^{-1}$，我们就称它们**共轭**。

**2. 平移。** 对每个 $x\in G$，我们通过 $T_x(y)=xy$ 定义平移 $T_x:G\to G$。于是映射

$$
(x,y)\mapsto xy=T_x(y)
$$

定义了 $G$ 在自身上的一个作用。*注意：*$T_x$ 不是群同态！它只是 $G$ 的一个置换。

<span class="original-page-anchor" id="pdf-page-42" aria-hidden="true"></span>

类似地，$G$ 以平移作用于所有子集组成的集合，因为若 $A$ 是 $G$ 的一个子集，则 $xA=T_x(A)$ 也是一个子集。若 $H$ 是 $G$ 的一个子群，则 $T_x(H)=xH$ 一般不是子群，而是 $H$ 的一个陪集，因此可以看出，$G$ 以平移作用于 $H$ 的所有陪集组成的集合。我们用 $G/H$ 表示 $H$ 的左陪集集合。因此，即使 $H$ 不一定正规，$G/H$ 也是一个 $G$ 集合。习惯上用 $H\backslash G$ 表示右陪集集合。

上面把 $G$ 表示为置换群的两种表示，在后文中会经常用到。特别是，共轭表示将贯穿下一节，应用于西洛定理的证明。

**3. 线性代数中的例子。** 我们假定读者了解线性代数的基本概念。设 $k$ 是一个域，$V$ 是 $k$ 上的一个向量空间。令 $G=GL(V)$ 为 $V$ 的线性自同构群。对于 $A\in G$ 和 $v\in V$，映射 $(A,v)\mapsto Av$ 定义了 $G$ 在 $V$ 上的一个作用。当然，$G$ 是置换群 $\operatorname{Perm}(V)$ 的一个子群。类似地，令 $V=k^n$ 为 $k$ 的元素组成的（列）$n$ 元组所构成的向量空间，令 $G$ 为元素属于 $k$ 的可逆 $n\times n$ 矩阵组成的群。则 $G$ 通过 $(A,X)\mapsto AX$ 作用于 $k^n$，其中 $A\in G$，$X\in k^n$。

设 $S,S'$ 是两个 $G$ 集合，$f:S\to S'$ 是一个映射。若对所有 $x\in G$ 和 $s\in S$ 都有

$$
f(xs)=xf(s),
$$

则称 $f$ 为一个 **$G$ 集合的态射**，或 **$G$ 映射**。（我们很快就会定义范畴，并看到 $G$ 集合构成一个范畴。）

现在回到一般情形，考虑一个群在集合 $S$ 上的作用。令 $s\in S$。满足 $xs=s$ 的所有元素 $x\in G$ 组成的集合，显然是 $G$ 的一个子群，称为 $s$ 在 $G$ 中的**稳定子群**（isotropy group），记为 $G_s$。

当 $G$ 以共轭作用于自身时，一个元素的稳定子群就是该元素的正规化子。类似地，当 $G$ 以共轭作用于所有子群组成的集合时，一个子群的稳定子群也就是它的正规化子。

设 $G$ 作用于集合 $S$。令 $s,s'$ 为 $S$ 的元素，$y$ 为 $G$ 的一个元素，满足 $ys=s'$。则

$$
G_{s'}=yG_sy^{-1}.
$$

事实上，可以立即看出，$yG_sy^{-1}$ 保持 $s'$ 不动。反过来，若 $x's'=s'$，则 $x'ys=ys$，所以 $y^{-1}x'y\in G_s$，且 $x'\in yG_sy^{-1}$。因此，$s$ 和 $s'$ 的稳定子群是共轭的。

令 $K$ 为表示 $G\to\operatorname{Perm}(S)$ 的核。直接由定义得到

$$
K=\bigcap_{s\in S}G_s=\text{所有稳定子群的交}.
$$

<span class="original-page-anchor" id="pdf-page-43" aria-hidden="true"></span>

如果 $K=\{e\}$，即 $G\to\operatorname{Perm}(S)$ 的核是平凡的，就称 $G$ 的这个作用是**忠实的**。$G$ 的一个**不动点**是满足对所有 $x\in G$ 都有 $xs=s$ 的元素 $s\in S$；换言之，$G=G_s$。

设 $G$ 作用于集合 $S$。令 $s\in S$。由所有元素 $xs$（$x\in G$）组成的 $S$ 的子集记为 $Gs$，称为 $s$ 在 $G$ 下的**轨道**。若 $x$ 和 $y$ 位于子群 $H=G_s$ 的同一个陪集中，则 $xs=ys$；反过来也成立（显然）。这样，我们得到映射

$$
f:G/H\to S,
$$

它由 $f(xH)=xs$ 给出，显然是 $G$ 集合的一个态射。事实上，可以立即看出，它诱导了从 $G/H$ 到轨道 $Gs$ 的一个双射。因此：

**命题 5.1.** *若 $G$ 是作用于集合 $S$ 的一个群，且 $s\in S$，则轨道 $Gs$ 的元素个数等于指数 $(G:G_s)$。*

特别地，当 $G$ 以共轭作用于所有子群组成的集合，而 $H$ 是一个子群时，有：

**命题 5.2.** *与 $H$ 共轭的子群的数目等于 $H$ 的正规化子的指数。*

**例。** 设 $G$ 是一个群，$H$ 是一个指数为 $2$ 的子群。则 $H$ 在 $G$ 中正规。

*证明。* 注意，$H$ 包含于它的正规化子 $N_H$ 中，因此 $N_H$ 在 $G$ 中的指数为 $1$ 或 $2$。若指数为 $1$，则结论已成立。设指数为 $2$。令 $G$ 以共轭作用于所有子群组成的集合。$H$ 的轨道有 $2$ 个元素，$G$ 作用于这个轨道。由此得到从 $G$ 到两个元素的置换群的一个同态。由于 $H$ 有一个不等于 $H$ 的共轭子群，这个同态的核就是一个指数为 $2$ 的正规子群，因此等于 $H$，于是 $H$ 正规，产生矛盾，证明完毕。

关于推广以及其他例子，参见引理 6.7。

一般地，若 $G$ 在 $S$ 上的作用只有一个轨道，就称这个作用是**传递的**。

**例。** 对称群 $S_n$ 传递地作用于 $\{1,2,\ldots,n\}$。（参见第 30 页。）在第 VII 章命题 2.1 中，我们将看到一个非平凡的例子：一个伽罗瓦群传递地作用于底环中某个给定素理想上方的素理想。在拓扑学中，设有一个万有覆盖空间 $p:X'\to X$，其中 $X$ 连通。给定 $x\in X$，基本群 $\pi_1(X)$ 传递地作用于原像 $p^{-1}(x)$。

<span class="original-page-anchor" id="pdf-page-44" aria-hidden="true"></span>

**例。** 令 $\mathfrak H$ 为上半平面，即满足 $y>0$ 的复数 $z=x+iy$ 组成的集合。令 $G=SL_2(\mathbf R)$（行列式为 $1$ 的 $2\times2$ 矩阵）。对于

$$
\alpha=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in G,\quad\text{令 }\alpha z=\frac{az+b}{cz+d}.
$$

读者可以通过直接计算验证，这定义了 $G$ 在 $\mathfrak H$ 上的一个作用。$i$ 的稳定子群是由如下矩阵组成的群：

$$
\begin{pmatrix}\cos\theta&\sin\theta\\-\sin\theta&\cos\theta\end{pmatrix},\quad\text{其中 }\theta\text{ 为实数}.
$$

这个群通常记为 $K$。群 $G$ 的作用是传递的。验证这些断言都可以作为简单的练习。

设 $G$ 作用于集合 $S$。则 $G$ 的两个轨道或者不相交，或者相等。事实上，若 $Gs_1$ 和 $Gs_2$ 是有一个公共元素 $s$ 的两个轨道，则对某个 $x\in G$ 有 $s=xs_1$，因而 $Gs=Gxs_1=Gs_1$。类似地，$Gs=Gs_2$。因此，$S$ 是各个不同轨道的不交并，可以写成

$$
S=\bigcup_{i\in I}Gs_i\quad\text{（不交）},\quad\text{也记为 }S=\coprod_{i\in I}Gs_i,
$$

其中 $I$ 是某个指标集，$s_i$ 是不同轨道中的元素。若 $S$ 有限，这就把 $S$ 的元素个数分解为各轨道元素个数的和；我们称之为**轨道分解公式**，即

$$
\boxed{\operatorname{card}(S)=\sum_{i\in I}(G:G_{s_i}).}
$$

令 $x,y$ 为群（或幺半群）$G$ 的元素。若 $xy=yx$，则称它们**可交换**。若 $G$ 是群，则所有与 $G$ 的每个元素都可交换的元素 $x\in G$ 组成 $G$ 的一个子群，我们曾称之为 $G$ 的**中心**。令 $G$ 以共轭作用于自身。那么，$x$ 属于中心，当且仅当 $x$ 的轨道只有 $x$ 自身，因而只有一个元素。一般地，$x$ 的轨道的元素个数等于 $x$ 的正规化子的指数。因此，当 $G$ 为有限群时，上述公式变为

$$
\boxed{(G:1)=\sum_{x\in C}(G:G_x)}
$$

其中 $C$ 是各个不同共轭类的一组代表元，求和遍及所有 $x\in C$。这个公式也称为**类公式**。

<span class="original-page-anchor" id="pdf-page-45" aria-hidden="true"></span>

下一节讨论西洛群时，将系统地使用类公式和轨道分解公式；这一节也可以看作给这些公式提供例子。

*对西洛群感兴趣的读者，可以直接跳到下一节。本节余下的内容讨论对称群的一些特殊性质，它们可以作为我们已建立的一般概念的例子。*

**对称群。** 令 $S_n$ 为一个含 $n$ 个元素的集合的置换群。这个集合可以取为整数集合 $J_n=\{1,2,\ldots,n\}$。给定任意 $\sigma\in S_n$ 和任意整数 $i$，$1\leq i\leq n$，可以考虑 $i$ 在由 $\sigma$ 生成的循环群下的轨道。这样的轨道称为 $\sigma$ 的一个**循环**，可以写成

$$
[i_1i_2\cdots i_r],\quad\text{从而}\quad\sigma(i_1)=i_2,\ldots,\sigma(i_{r-1})=i_r,\ \sigma(i_r)=i_1.
$$

于是，$\{1,\ldots,n\}$ 可以分解成由 $\sigma$ 生成的循环群的各轨道的不交并，因此分解为不相交的循环。因此，$\sigma$ 在 $\{1,\ldots,n\}$ 上的作用由若干不相交循环的乘积表示。

**例。** 循环 $[132]$ 表示满足下列条件的置换 $\sigma$：

$$
\sigma(1)=3,\quad\sigma(3)=2,\quad\text{且}\quad\sigma(2)=1.
$$

我们有 $\sigma^2(1)=2$，$\sigma^3(1)=1$。所以 $\{1,3,2\}$ 是 $1$ 在由 $\sigma$ 生成的循环群下的轨道。

**例。** 在习题 38 中，将会看到如何用特殊类型的生成元生成 $S_n$。该习题中或许最重要的部分是：若 $n$ 为素数，$\sigma$ 为一个 $n$ 循环，$\tau$ 为一个对换，则 $\sigma,\tau$ 生成 $S_n$。作为在伽罗瓦理论中的应用，如果要证明一个伽罗瓦群等于整个 $S_n$（作为根的置换群），只须证明该伽罗瓦群包含一个 $n$ 循环和一个对换。参见第 VI 章 §2 的例 6。

我们要给每个置换配上一个符号 $\pm1$。我们采用标准的方法来做这件事。令 $f$ 为一个 $n$ 元函数，比如 $f:\mathbf Z^n\to\mathbf Z$，这样就可以计算 $f(x_1,\ldots,x_n)$。令 $\sigma$ 为 $J_n$ 的一个置换。通过下式定义函数 $\pi(\sigma)f$：

$$
\pi(\sigma)f(x_1,\ldots,x_n)=f(x_{\sigma(1)},\ldots,x_{\sigma(n)}).
$$

于是，对 $\sigma,\tau\in S_n$，有 $\pi(\sigma\tau)=\pi(\sigma)\pi(\tau)$。事实上，把定义应用于函数 $g=\pi(\tau)f$，得到

$$
\begin{aligned}
\pi(\sigma)\pi(\tau)f(x_1,\ldots,x_n)&=(\pi(\tau)f)(x_{\sigma(1)},\ldots,x_{\sigma(n)})\\
&=f(x_{\sigma\tau(1)},\ldots,x_{\sigma\tau(n)})\\
&=\pi(\sigma\tau)f(x_1,\ldots,x_n).
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-46" aria-hidden="true"></span>

由于 $S_n$ 的恒等置换作为恒等映射作用于函数，我们得到 $S_n$ 在函数集合上的一个作用。我们将用较简洁的 $\sigma f$ 代替 $\pi(\sigma)f$。可以立即验证，对于两个函数 $f,g$，有

$$
\sigma(f+g)=\sigma f+\sigma g\quad\text{且}\quad\sigma(fg)=(\sigma f)(\sigma g).
$$

若 $c$ 为常数，则 $\sigma(cf)=c\sigma(f)$。

**命题 5.3.** *存在唯一的同态 $\varepsilon:S_n\to\{\pm1\}$，使得对每个对换 $\tau$ 都有 $\varepsilon(\tau)=-1$。*

*证明。* 令 $\Delta$ 为函数

$$
\Delta(x_1,\ldots,x_n)=\prod_{i<j}(x_j-x_i),
$$

其中乘积遍及所有满足 $1\leq i<j\leq n$ 的整数对 $i,j$。令 $\tau$ 为交换两个整数 $r$ 和 $s$ 的一个对换。不妨设 $r<s$。我们要确定

$$
\tau\Delta(x_1,\ldots,x_n)=\prod_{i<j}(x_{\tau(j)}-x_{\tau(i)}).
$$

对于 $j=s$、$i=r$ 的那个因子，可以看出，$\tau$ 把因子 $(x_s-x_r)$ 变为 $-(x_s-x_r)$。其余所有因子可以按如下方式成对考虑：

$$
\begin{array}{ll}
(x_k-x_s)(x_k-x_r)&\text{若 }k>s,\\
(x_s-x_k)(x_k-x_r)&\text{若 }r<k<s,\\
(x_s-x_k)(x_r-x_k)&\text{若 }k<r.
\end{array}
$$

作用 $\tau$ 后，上述每一对的乘积都保持不变。因此可知 $\tau\Delta=-\Delta$。

对于置换 $\sigma$，令 $\varepsilon(\sigma)$ 为满足 $\sigma\Delta=\varepsilon(\sigma)\Delta$ 的符号 $1$ 或 $-1$。由于 $\pi(\sigma\tau)=\pi(\sigma)\pi(\tau)$，立即可知 $\varepsilon$ 是同态，命题得证。

特别地，若 $\sigma=\tau_1\cdots\tau_m$ 是若干对换的乘积，则 $\varepsilon(\sigma)=(-1)^m$。在术语上，若 $\varepsilon(\sigma)=1$，我们称 $\sigma$ 为**偶置换**；若 $\varepsilon(\sigma)=-1$，则称为**奇置换**。所有偶置换组成 $\varepsilon$ 的核，它称为**交错群** $A_n$。

**定理 5.4.** *若 $n\geq5$，则 $S_n$ 不是可解群。*

*证明。* 我们先证明：若 $H,N$ 是 $S_n$ 的两个子群，满足 $N\subset H$，且 $N$ 在 $H$ 中正规；如果 $H$ 包含每一个 $3$ 循环，且 $H/N$ 是阿贝尔群，那么 $N$ 包含每一个 $3$ 循环。为说明这一点，令 $i,j,k,r,s$ 为 $J_n$ 中五个不同的整数，并令 $\sigma=[ijk]$，$\tau=[krs]$。直接计算它们的交换子得到

$$
\sigma\tau\sigma^{-1}\tau^{-1}=[rki].
$$

<span class="original-page-anchor" id="pdf-page-47" aria-hidden="true"></span>

由于 $i,j,k,r,s$ 的选择是任意的，可知对于任意三个不同的 $r,k,i$，循环 $[rki]$ 都属于 $N$，从而证明了所要的结论。

现在假设有一个子群列

$$
S_n=H_0\supset H_1\supset H_2\supset\cdots\supset H_m=\{e\},
$$

使得对 $v=1,\ldots,m$，$H_v$ 在 $H_{v-1}$ 中正规，且 $H_v/H_{v-1}$ 是阿贝尔群。由于 $S_n$ 包含每一个 $3$ 循环，可知 $H_1$ 包含每一个 $3$ 循环。由归纳法得到 $H_m=\{e\}$ 包含每一个 $3$ 循环，这是不可能的，定理得证。

> **译校注。** 原书此处印作 $H_v/H_{v-1}$。对于上述递减子群列，该论证所需的商群应为 $H_{v-1}/H_v$。

**关于符号 $\varepsilon(\sigma)$ 的说明。** 最初，我们是对给定的 $n$ 定义符号的，所以应写作 $\varepsilon_n(\sigma)$。但是，设 $n<m$。则 $\varepsilon_m$ 在 $S_n$ 上的限制（把 $S_n$ 的置换看成 $J_n$ 上的置换，并保持 $J_m$ 中不在 $J_n$ 内的元素不动）给出一个满足命题 5.3 条件的同态，因此这个限制等于 $\varepsilon_n$。所以 $A_m\cap S_n=A_n$。

接下来证明交错群的一些性质。

(a) *$A_n$ 由所有 $3$ 循环生成。* *证明：* 考虑两个对换的乘积 $[ij][rs]$。若它们有一个公共元素，则乘积或者是恒等置换，或者是一个 $3$ 循环。若它们没有公共元素，则

$$
[ij][rs]=[ijr][jrs],
$$

所以两个对换的乘积也能写成若干 $3$ 循环的乘积。由于偶置换是偶数个对换的乘积，结论得证。

(b) *若 $n\geq5$，则所有 $3$ 循环在 $A_n$ 中共轭。* *证明：* 若 $\gamma$ 是一个置换，则对于循环 $[i_1\ldots i_m]$，有

$$
\gamma[i_1\ldots i_m]\gamma^{-1}=[\gamma(i_1)\ldots\gamma(i_m)].
$$

给定两个 $3$ 循环 $[ijk]$ 和 $[i'j'k']$，存在一个置换 $\gamma$，使 $\gamma(i)=i'$，$\gamma(j)=j'$，$\gamma(k)=k'$。因此，两个 $3$ 循环在 $S_n$ 中通过某个元素 $\gamma$ 共轭。若 $\gamma$ 为偶置换，结论便已成立。否则，由假设 $n\geq5$，存在 $r,s$，它们都不等于 $i,j,k$ 中的任一元素。此时 $[rs]$ 与 $[ijk]$ 可交换，把 $\gamma$ 换成 $\gamma[rs]$ 即可证明 (b)。

**定理 5.5.** *若 $n\geq5$，则交错群 $A_n$ 是单群。*

*证明。* 设 $N$ 是 $A_n$ 的一个非平凡正规子群。我们证明 $N$ 包含某个 $3$ 循环；于是由 (b) 可推出定理。令 $\sigma\in N$，$\sigma\neq\mathrm{id}$，为具有最多不动点的一个元素；不动点指满足 $\sigma(i)=i$ 的整数 $i$。只须证明 $\sigma$ 是一个 $3$ 循环或恒等置换。把 $J_n$ 分解为 $\langle\sigma\rangle$ 的不相交轨道。此时有些轨道包含不止一个元素。假设除不动点外，所有轨道都有 $2$ 个元素。由于 $\sigma$ 是偶置换，这样的轨道至少有两个。在它们的并集上，$\sigma$ 表示为<span class="original-page-anchor" id="pdf-page-48" aria-hidden="true"></span>是两个对换的乘积 $[ij][rs]$。取 $k\ne i,j,r,s$。令 $\tau=[rsk]$，并令 $\sigma'=\tau\sigma\tau^{-1}\sigma^{-1}$。于是 $\sigma'$ 是 $\sigma$ 的一个共轭与 $\sigma^{-1}$ 的乘积，所以 $\sigma'\in N$。但是 $\sigma'$ 固定 $i,j$，而且任何被 $\sigma$ 固定的元素 $t\in J_n$，其中 $t\ne i,j,r,s,k$，也被 $\sigma'$ 固定。因此 $\sigma'$ 的不动点比 $\sigma$ 多，这与我们的假设矛盾。

这样，我们只需考虑 $\langle\sigma\rangle$ 的至少一个轨道含有 $\geqq3$ 个元素的情形，设这些元素为 $i,j,k,\ldots$。如果 $\sigma$ 不是 3-循环 $[ijk]$，那么 $\sigma$ 必须还移动 $J_n$ 中至少两个其他元素；否则，对某个 $r\in J_n$，$\sigma$ 就是奇置换 $[ijkr]$，这是不可能的。于是设 $\sigma$ 移动异于 $i,j,k$ 的 $r,s$，并令 $\tau=[krs]$。令 $\sigma'$ 为前面那样的交换子。则 $\sigma'\in N$ 且 $\sigma'(i)=i$，而 $\sigma$ 的所有不动点也都是 $\sigma'$ 的不动点。因此 $\sigma'$ 的不动点比 $\sigma$ 多，矛盾，从而证明了定理。

**例。** 当 $n=4$ 时，群 $A_4$ 不是单群。作为练习，证明 $A_4$ 含有唯一的 4 阶子群，这个子群不是循环群，而且是正规子群。这个子群在 $S_4$ 中也是正规的。将它的元素明确写成对换的乘积。

## §6. 西洛子群

设 $p$ 是一个素数。所谓 **$p$-群**，是指阶为 $p$ 的幂的有限群（即对于某个整数 $n\geqq0$，阶为 $p^n$）。设 $G$ 是有限群，$H$ 是它的一个子群。如果 $H$ 是 $p$-群，就称 $H$ 为 $G$ 的 **$p$-子群**。如果 $H$ 的阶为 $p^n$，并且 $p^n$ 是整除 $G$ 的阶的 $p$ 的最高次幂，就称 $H$ 为一个 **$p$-西洛子群**。下面我们将证明这样的子群总是存在。为此需要一个引理。

**引理 6.1。** *设 $G$ 是 $m$ 阶有限阿贝尔群，$p$ 是整除 $m$ 的素数。则 $G$ 有一个 $p$ 阶子群。*

*证明。* 我们先用归纳法证明：如果 $G$ 具有指数 $n$，那么 $G$ 的阶整除 $n$ 的某个幂。取 $b\in G$，$b\ne1$，并设 $H$ 为 $b$ 生成的循环子群。因为 $b^n=1$，所以 $H$ 的阶整除 $n$，而且 $n$ 是 $G/H$ 的一个指数。因此，由归纳假设，$G/H$ 的阶整除 $n$ 的一个幂，从而 $G$ 的阶也是如此，因为

$$
(G:1)=(G:H)(H:1).
$$

设 $G$ 的阶可被 $p$ 整除。由刚才所证明的结论，$G$ 中存在一个元素 $x$，其周期可被 $p$ 整除。设这个周期为 $ps$，其中 $s$ 为某个整数。于是 $x^s\ne1$，且显然 $x^s$ 的周期为 $p$，因而生成一个 $p$ 阶子群，这就是要证明的结论。

<span class="original-page-anchor" id="pdf-page-49" aria-hidden="true"></span>

**定理 6.2。** *设 $G$ 是有限群，$p$ 是整除 $G$ 的阶的素数。则 $G$ 存在一个 $p$-西洛子群。*

*证明。* 对 $G$ 的阶作归纳。如果 $G$ 的阶是素数，断言显然成立。现在假定给定一个有限群 $G$，并假定定理对所有阶小于 $G$ 的阶的群都已成立。如果 $G$ 存在一个真子群 $H$，其指数与 $p$ 互素，那么 $H$ 的一个 $p$-西洛子群也将是 $G$ 的 $p$-西洛子群，断言由归纳假设得出。因此，我们可以假定每个真子群的指数都可被 $p$ 整除。现在让 $G$ 通过共轭作用于自身。由类公式得到

$$
(G:1)=(Z:1)+\sum(G:G_x).
$$

这里，$Z$ 是 $G$ 的中心，项 $(Z:1)$ 对应于只有一个元素的轨道，也就是 $Z$ 的元素。右边的求和遍历其他轨道，而每个指数 $(G:G_x)$ 此时都 $>1$，因而可被 $p$ 整除。由于 $p$ 整除 $G$ 的阶，可知 $p$ 整除 $Z$ 的阶，因而特别地，$G$ 具有非平凡中心。

设 $a$ 是 $Z$ 中的一个 $p$ 阶元素，并设 $H$ 为 $a$ 生成的循环群。由于 $H$ 包含于 $Z$ 中，它是正规的。设 $f:G\to G/H$ 为典范映射。设 $p^n$ 是整除 $(G:1)$ 的 $p$ 的最高次幂。于是 $p^{n-1}$ 整除 $G/H$ 的阶。由归纳假设，取 $G/H$ 的一个 $p$-西洛子群 $K'$，并令 $K=f^{-1}(K')$。于是 $K\supset H$，且 $f$ 将 $K$ 映满 $K'$。因此有同构 $K/H\approx K'$。所以 $K$ 的阶为 $p^{n-1}p=p^n$，如所要求。

在其余定理中，我们将系统地使用不动点的概念。设 $G$ 是作用于集合 $S$ 的群。回忆，$G$ 在 $S$ 中的一个**不动点** $s$，是指 $S$ 中满足对所有 $x\in G$ 都有 $xs=s$ 的元素 $s$。

**引理 6.3。** *设 $H$ 是作用于有限集 $S$ 的 $p$-群。则：*

**(a)** *$H$ 的不动点数 $\equiv\#(S)\bmod p$。*

**(b)** *如果 $H$ 恰有一个不动点，则 $\#(S)\equiv1\bmod p$。*

**(c)** *如果 $p\mid\#(S)$，则 $H$ 的不动点数 $\equiv0\bmod p$。*

*证明。* 我们反复使用轨道公式

$$
\#(S)=\sum(H:H_{s_i}).
$$

对每个不动点 $s_i$，有 $H_{s_i}=H$。若 $s_i$ 不是不动点，则指数 $(H:H_{s_i})$ 可被 $p$ 整除，于是 (a) 立即成立。(b) 和 (c) 是 (a) 的特殊情形，从而引理得证。

**注。** 在引理 6.3(c) 中，如果 $H$ 有一个不动点，那么 $H$ 至少有 $p$ 个不动点。

**定理 6.4。** *设 $G$ 是有限群。*

(i) *如果 $H$ 是 $G$ 的一个 $p$-子群，那么 $H$ 包含于某个 $p$-西洛子群中。*

<span class="original-page-anchor" id="pdf-page-50" aria-hidden="true"></span>

(ii) *所有 $p$-西洛子群都彼此共轭。*

(iii) *$G$ 的 $p$-西洛子群的数目 $\equiv1\bmod p$。*

*证明。* 设 $P$ 是 $G$ 的一个 $p$-西洛子群。首先假定 $H$ 包含于 $P$ 的正规化子中。我们证明 $H\subset P$。事实上，此时 $HP$ 是这个正规化子的一个子群，且 $P$ 在 $HP$ 中正规。但是

$$
(HP:P)=(H:H\cap P),
$$

所以如果 $HP\ne P$，则 $HP$ 的阶是 $p$ 的幂，且这个阶大于 $\#(P)$，与 $P$ 是西洛群的假设矛盾。因此 $HP=P$ 且 $H\subset P$。

其次，设 $S$ 是 $P$ 在 $G$ 中所有共轭子群组成的集合。于是 $G$ 通过共轭作用于 $S$。由于 $P$ 的正规化子包含 $P$，其指数因而与 $p$ 互素，所以 $\#(S)$ 不可被 $p$ 整除。现在设 $H$ 是任意 $p$-子群。则 $H$ 也通过共轭作用于 $S$。由引理 6.3(a)，可知 $H$ 的不动点数不能为 $0$。设 $Q$ 是一个不动点。按照定义，这意味着 $H$ 包含于 $Q$ 的正规化子中，因而由证明的第一部分，$H\subset Q$，这证明了定理的第一部分。取 $H$ 为一个 $p$-西洛群，就立即得到第二部分：此时 $\#(H)=\#(Q)$，所以 $H=Q$。特别地，当 $H$ 是一个 $p$-西洛群时，可见 $H$ 只有一个不动点，因此 (iii) 由引理 6.3(b) 得出。定理得证。

**定理 6.5。** *设 $G$ 是有限 $p$-群。则 $G$ 可解。如果其阶 $>1$，那么 $G$ 有非平凡中心。*

*证明。* 第一个断言由第二个断言得出，因为如果 $G$ 的中心为 $Z$，并且由归纳假设得到 $G/Z$ 的一个阿贝尔群塔，那么可以将这个阿贝尔群塔提升到 $G$，从而证明 $G$ 可解。为了证明第二个断言，我们使用类方程

$$
(G:1)=\operatorname{card}(Z)+\sum(G:G_x),
$$

其中的求和遍历某些满足 $(G:G_x)\ne1$ 的 $x$。于是 $p$ 整除 $(G:1)$，也整除和式中的每一项，所以 $p$ 整除中心的阶，这就是所要证明的结论。

**推论 6.6。** *设 $G$ 是阶不为 $1$ 的 $p$-群。则存在一个子群序列*

$$
\{e\}=G_0\subset G_1\subset G_2\subset\cdots\subset G_n=G
$$

*使得 $G_i$ 在 $G$ 中正规，且 $G_{i+1}/G_i$ 是 $p$ 阶循环群。*

*证明。* 因为 $G$ 有非平凡中心，所以 $G$ 的中心中存在一个元素 $a\ne e$，且 $a$ 的阶为 $p$。设 $H$ 为 $a$ 生成的循环群。由归纳法，如果 $G\ne H$，则可以在商群 $G/H$ 中找到一个上述形式的子群序列。取这个群塔在 $G$ 中的逆像，就得到所要求的 $G$ 中的序列。

<span class="original-page-anchor" id="pdf-page-51" aria-hidden="true"></span>

现在我们给出一些例子，说明如何将部分群论知识综合运用。

**引理 6.7。** *设 $G$ 是有限群，$p$ 是整除 $G$ 的阶的最小素数。设 $H$ 是指数为 $p$ 的子群。则 $H$ 正规。*

*证明。* 设 $N(H)=N$ 为 $H$ 的正规化子。则 $N=G$ 或 $N=H$。如果 $N=G$，证明完成。假定 $N=H$。则 $H$ 在共轭作用下的轨道含有 $p=(G:H)$ 个元素，而 $G$ 在这个轨道上的表示给出一个从 $G$ 到 $p$ 个元素上的对称群的同态，该对称群的阶为 $p!$。设 $K$ 为核。则 $K$ 是各稳定子群的交，而由假设，$H$ 的稳定子群是 $H$，所以 $K\subset H$。如果 $K\ne H$，那么由

$$
(G:K)=(G:H)(H:K)=p(H:K),
$$

以及 $p!$ 中只有 $p$ 的一次幂可整除它这一事实，可得某个整除 $(p-1)!$ 的素数也整除 $(H:K)$。这与 $p$ 是整除 $G$ 的阶的最小素数的假设矛盾，从而引理得证。

**命题 6.8。** *设 $p,q$ 是不同的素数，$G$ 是一个 $pq$ 阶群。则 $G$ 可解。*

*证明。* 不妨设 $p<q$。设 $Q$ 是一个 $q$ 阶西洛子群。则 $Q$ 的指数为 $p$，所以由引理，$Q$ 正规，且商群的阶为 $p$。但是素数阶的群是循环群，命题因而成立。

**例。** 设 $G$ 是一个 35 阶群。我们断言 $G$ 是循环群。

*证明。* 设 $H_7$ 是 7 阶西洛子群。由引理 6.7，$H_7$ 正规。设 $H_5$ 是一个 5-西洛子群，其阶为 $5$。于是 $H_5$ 通过共轭作用于 $H_7$，从而得到一个同态 $H_5\to\operatorname{Aut}(H_7)$。但是 $\operatorname{Aut}(H_7)$ 是 6 阶循环群，所以 $H_5\to\operatorname{Aut}(H_7)$ 是平凡同态，于是 $H_5$ 的每个元素都与 $H_7$ 的元素交换。设 $H_5=\langle x\rangle$ 且 $H_7=\langle y\rangle$。那么 $x,y$ 彼此交换，也各自与自身交换，所以 $G$ 是阿贝尔群，从而由命题 4.3(v)，$G$ 是循环群。

**例。** 已经建立的这些方法足以处理上述类型的许多情形。例如，每个阶 $<60$ 的群都是可解群，这将在练习 27 中由你证明。

## §7. 直和与自由阿贝尔群

设 $\{A_i\}_{i\in I}$ 是一族阿贝尔群。我们将它们的**直和**

$$
A=\bigoplus_{i\in I}A_i
$$

定义为直积 $\prod A_i$ 中所有满足下述条件的族 $(x_i)_{i\in I}$ 所组成的子集：

<span class="original-page-anchor" id="pdf-page-52" aria-hidden="true"></span>

$x_i\in A_i$，且除有限多个指标 $i$ 以外都有 $x_i=0$。于是显然 $A$ 是这个直积的一个子群。对每个指标 $j\in I$，我们定义映射

$$
\lambda_j:A_j\to A,
$$

令 $\lambda_j(x)$ 为第 $j$ 个分量等于 $x$，其余所有分量等于 $0$ 的元素。则 $\lambda_i$ 是单射同态。

> **译校注。** 原书在定义 $\lambda_j$ 后，末句印作 $\lambda_i$。按前面固定的指标 $j$，应读作“则 $\lambda_j$ 是单射同态”。

**命题 7.1。** *设 $\{f_i:A_i\to B\}$ 是一族取值于阿贝尔群 $B$ 的同态。令 $A=\bigoplus A_i$。存在唯一的同态*

$$
f:A\to B
$$

*使得对所有 $j$ 都有 $f\circ\lambda_j=f_j$。*

*证明。* 可以按照规则

$$
f((x_i)_{i\in I})=\sum_{i\in I}f_i(x_i)
$$

定义一个映射 $f:A\to B$。右边的和实际上是有限和，因为除有限项以外所有项都为 $0$。可以立即验证映射 $f$ 是同态。此外，显然对每个 $j$ 以及每个 $x\in A_j$，都有 $f\circ\lambda_j(x)=f_j(x)$。因此 $f$ 具有所要求的交换性。映射 $f$ 被唯一确定也是显然的，这就是所要证明的结论。

命题 7.1 所表达的性质称为直和的**泛性质**。参见 §11。

**例。** 设 $A$ 是阿贝尔群，$\{A_i\}_{i\in I}$ 是一族子群。则得到同态

$$
\bigoplus_{i\in I}A_i\to A\quad\text{使得}\quad(x_i)\mapsto\sum x_i.
$$

定理 8.1 将给出一个重要的具体应用。

设 $A$ 是阿贝尔群，$B,C$ 是子群。如果 $B+C=A$ 且 $B\cap C=\{0\}$，那么由 $(x,y)\mapsto x+y$ 给出的映射

$$
B\times C\to A
$$

是同构（正如我们在非交换情形中已经指出的）。我们将不用 $A=B\times C$ 的写法，而写成

$$
A=B\oplus C,
$$

并称 $A$ 是 $B$ 与 $C$ 的**直和**。对于有限多个子群 $B_1,\ldots,B_n$ 的直和，我们使用类似的记号；这些子群满足

$$
B_1+\cdots+B_n=A
$$

以及

$$
B_{i+1}\cap(B_1+\cdots+B_i)=0.
$$

<span class="original-page-anchor" id="pdf-page-53" aria-hidden="true"></span>

在这种情形下，我们写成

$$
A=B_1\oplus\cdots\oplus B_n.
$$

设 $A$ 是阿贝尔群。设 $\{e_i\}$ $(i\in I)$ 是 $A$ 中的一族元素。如果这个族非空，并且 $A$ 的每个元素都可唯一地表示为线性组合

$$
x=\sum x_ie_i,
$$

其中 $x_i\in\mathbf{Z}$，且几乎所有 $x_i=0$，就称这个族为 $A$ 的一个**基**。因此，该和实际上是有限和。如果一个阿贝尔群有基，就称它为**自由**的。在这种情形下，显然若对所有 $i$ 都令 $Z_i=\mathbf{Z}$，则 $A$ 同构于直和

$$
A\approx\bigoplus_{i\in I}Z_i.
$$

其次，设 $S$ 是一个集合。我们将如下定义 $S$ 生成的自由阿贝尔群。设 $\mathbf{Z}\langle S\rangle$ 是所有满足对几乎所有 $x\in S$ 都有 $\varphi(x)=0$ 的映射 $\varphi:S\to\mathbf{Z}$ 组成的集合。则 $\mathbf{Z}\langle S\rangle$ 是一个阿贝尔群（加法为通常的映射加法）。如果 $k$ 是一个整数，$x$ 是 $S$ 中的一个元素，我们用 $k\cdot x$ 表示这样的映射 $\varphi$：$\varphi(x)=k$，且当 $y\ne x$ 时 $\varphi(y)=0$。于是显然 $\mathbf{Z}\langle S\rangle$ 的每个元素 $\varphi$ 都可写成

$$
\varphi=k_1\cdot x_1+\cdots+k_n\cdot x_n,
$$

其中 $k_i$ 是某些整数，$x_i\in S$ $(i=1,\ldots,n)$，且所有 $x_i$ 互不相同。此外，*$\varphi$ 具有唯一的这种表示*，因为如果有

$$
\varphi=\sum_{x\in S}k_x\cdot x=\sum_{x\in S}k'_x\cdot x,
$$

那么

$$
0=\sum_{x\in S}(k_x-k'_x)\cdot x,
$$

所以对所有 $x\in S$ 都有 $k'_x=k_x$。

通过满足 $f(x)=1\cdot x$ 的映射 $f_S=f$，我们将 $S$ 映入 $\mathbf{Z}\langle S\rangle$。于是显然 $f$ 是单射，且 $f(S)$ 生成 $\mathbf{Z}\langle S\rangle$。如果 $g:S\to B$ 是从 $S$ 到某个阿贝尔群 $B$ 的映射，则可以定义映射

$$
g_*:\mathbf{Z}\langle S\rangle\to B,
$$

使得

$$
g_*\left(\sum_{x\in S}k_x\cdot x\right)=\sum_{x\in S}k_xg(x).
$$

这个映射是同态（显然），且有 $g_*\circ f=g$（也显然）。它是唯一具有此性质的同态，因为任何这样的同态 $g_*$ 都必须满足 $g_*(1\cdot x)=g(x)$。

<span class="original-page-anchor" id="pdf-page-54" aria-hidden="true"></span>

通常将 $S$ 视为 $\mathbf{Z}\langle S\rangle$ 中的一个子集；写 $k_xx$ 或和式 $\sum k_xx$ 时，我们有时省略乘号圆点。

*如果 $\lambda:S\to S'$ 是集合之间的映射，则存在唯一的同态 $\bar\lambda$，使下图交换：*

$$
\begin{array}{ccc}
S&\xrightarrow{f_S}&\mathbf{Z}\langle S\rangle\\
\lambda\downarrow&&\downarrow\bar\lambda\\
S'&\xrightarrow{f_{S'}}&\mathbf{Z}\langle S'\rangle
\end{array}
$$

事实上，按照上一段的记号，$\bar\lambda$ 正是 $(f_{S'}\circ\lambda)_*$。这个断言的证明留作一个简单的练习。

我们也将 $\mathbf{Z}\langle S\rangle$ 记为 $F_{\mathrm{ab}}(S)$，并称 $F_{\mathrm{ab}}(S)$ 为 **$S$ 生成的自由阿贝尔群**。我们称 $S$ 的元素为它的**自由生成元**。

作为练习，证明每个阿贝尔群 $A$ 都同构于某个自由阿贝尔群 $F$ 的商群。如果 $A$ 是有限生成的，证明也可以选取有限生成的 $F$。

如果上述集合 $S$ 含有 $n$ 个元素，那么我们称自由阿贝尔群 $F_{\mathrm{ab}}(S)$ 为具有 $n$ 个生成元的自由阿贝尔群。如果 $S$ 是由 $n$ 个字母 $x_1,\ldots,x_n$ 组成的集合，则称 $F_{\mathrm{ab}}(S)$ 为具有自由生成元 $x_1,\ldots,x_n$ 的自由阿贝尔群。

一个阿贝尔群是**自由**的，当且仅当它同构于某个集合 $S$ 上的自由阿贝尔群 $F_{\mathrm{ab}}(S)$。设 $A$ 是阿贝尔群，$S$ 是 $A$ 的一个基。那么显然 $A$ 同构于自由阿贝尔群 $F_{\mathrm{ab}}(S)$。

在记号上，如果 $A$ 是阿贝尔群，$T$ 是由 $A$ 的元素组成的一个子集，则用 $\langle T\rangle$ 表示由 $T$ 的元素生成的子群，即包含 $T$ 的最小的 $A$ 的子群。

**例。格罗滕迪克群。** 设 $M$ 是一个用加法记号表示的交换幺半群。存在一个交换群 $K(M)$ 和一个幺半群同态

$$
\gamma:M\to K(M),
$$

它具有如下泛性质。如果 $f:M\to A$ 是取值于阿贝尔群 $A$ 的同态，则存在唯一的同态 $f_*:K(M)\to A$，使下图交换：

$$
\begin{array}{ccc}
M&\xrightarrow{\gamma}&K(M)\\
\searrow\!{\scriptstyle f}&&{\scriptstyle f_*}\!\swarrow\\
&A&
\end{array}
$$

*证明。* 设 $F_{\mathrm{ab}}(M)$ 是 $M$ 生成的自由阿贝尔群。将 $F_{\mathrm{ab}}(M)$ 中对应于元素 $x\in M$ 的生成元记为 $[x]$。设 $B$ 是所有形如

$$
[x+y]-[x]-[y]
$$

<span class="original-page-anchor" id="pdf-page-55" aria-hidden="true"></span>

的元素生成的子群，其中 $x,y\in M$。令 $K(M)=F_{\mathrm{ab}}(M)/B$，并令

$$
\gamma:M\to K(M)
$$

为如下两个映射的复合：由 $x\mapsto[x]$ 给出的从 $M$ 到 $F_{\mathrm{ab}}(M)$ 的单射，以及典范映射

$$
F_{\mathrm{ab}}(M)\to F_{\mathrm{ab}}(M)/B.
$$

于是显然 $\gamma$ 是同态，并满足所要求的泛性质。

泛群 $K(M)$ 称为**格罗滕迪克群**。

如果对任意 $x,y,z\in M$，由 $x+z=y+z$ 都能推出 $x=y$，就说 $M$ 中成立**消去律**。

由此得到关于上述泛映射 $\gamma$ 何时为单射的一个重要判据：

*如果 $M$ 中成立消去律，则从 $M$ 到其格罗滕迪克群的典范映射 $\gamma$ 是单射。*

*证明。* 这个证明与从自然数构造整数时的证明本质上相同。我们考虑元素对 $(x,y)$，其中 $x,y\in M$；若 $y+x'=x+y'$，就说 $(x,y)$ 与 $(x',y')$ 等价。按分量定义元素对的加法。则元素对的等价类构成一个群，它的 $0$ 元素是 $(0,0)$ 的类［或者任意 $x\in M$ 的 $(x,x)$ 的类］。元素 $(x,y)$ 的负元素是 $(y,x)$。我们有同态

$$
x\mapsto(0,x)\text{ 的类},
$$

应用消去律就立即可见这个同态是单射。因此我们构造了从 $M$ 到一个群的单射同态。由此可知泛同态也必定是单射。

**例。** 参见第 III 章 §4 中关于投射模的例子。对于一个较为精巧的背景，可参见：K. Kato，Logarithmic structures of Fontaine-Illusie（Fontaine-Illusie 的对数结构），*Algebraic Geometry, Analysis and Number Theory, Proc. JAMI Conference*（《代数几何、分析与数论：JAMI 会议论文集》），J. Igusa 编，Johns Hopkins Press（1989），第 195–224 页。

给定阿贝尔群 $A$ 和子群 $B$，有时希望找到一个子群 $C$，使 $A=B\oplus C$。下一个引理给出使这一结论成立的一个条件。

**引理 7.2。** *设 $A\xrightarrow{f}A'$ 是阿贝尔群之间的满射同态，并假定 $A'$ 是自由的。设 $B$ 是 $f$ 的核。则 $A$ 存在一个子群 $C$，使得 $f$ 在 $C$ 上的限制诱导 $C$ 与 $A'$ 之间的同构，且 $A=B\oplus C$。*

*证明。* 设 $\{x'_i\}_{i\in I}$ 是 $A'$ 的一个基，并且对每个 $i\in I$，取 $A$ 中的一个元素 $x_i$，使得 $f(x_i)=x'_i$。设 $C$ 是 $A$ 中由所有元素 $x_i$，$i\in I$ 生成的子群。如果有一个关系

$$
\sum_{i\in I}n_ix_i=0
$$

<span class="original-page-anchor" id="pdf-page-56" aria-hidden="true"></span>

其中 $n_i$ 是整数，几乎所有 $n_i$ 都等于 $0$，那么应用 $f$ 得到

$$
0=\sum_{i\in I}n_if(x_i)=\sum_{i\in I}n_ix'_i,
$$

所以所有 $n_i=0$。因此，族 $\{x_i\}_{i\in I}$ 是 $C$ 的一个基。类似地可见，如果 $z\in C$ 且 $f(z)=0$，则 $z=0$。所以 $B\cap C=0$。取 $x\in A$。由于 $f(x)\in A'$，存在整数 $n_i$，$i\in I$，使得

$$
f(x)=\sum_{i\in I}n_ix'_i.
$$

将 $f$ 应用于 $x-\sum_{i\in I}n_ix_i$，可知这个元素属于 $f$ 的核，设

$$
x-\sum_{i\in I}n_ix_i=b\in B.
$$

由此可见 $x\in B+C$，因而最终得到 $A=B\oplus C$ 是一个直和，如所断言。

**定理 7.3。** *设 $A$ 是自由阿贝尔群，$B$ 是一个子群。则 $B$ 也是自由阿贝尔群，且 $B$ 的一个基的基数 $\leqq$ $A$ 的一个基的基数。$B$ 的任意两个基都具有相同的基数。*

*证明。* 我们只在 $A$ 有限生成时给出证明，设其一个基为 $\{x_1,\ldots,x_n\}$ $(n\geqq1)$，并对 $n$ 作归纳。将 $A$ 表示成直和：

$$
A=\mathbf{Z}x_1\oplus\cdots\oplus\mathbf{Z}x_n.
$$

设 $f:A\to\mathbf{Z}x_1$ 是投影，即满足对任意 $m_i\in\mathbf{Z}$ 都有

$$
f(m_1x_1+\cdots+m_nx_n)=m_1x_1
$$

的同态。设 $B_1$ 是 $f|B$ 的核。则 $B_1$ 包含于自由子群 $\langle x_2,\ldots,x_n\rangle$ 中。由归纳假设，$B_1$ 是自由的，并有一个包含 $\leqq n-1$ 个元素的基。由引理，存在一个子群 $C_1$，它同构于 $\mathbf{Z}x_1$ 的一个子群（即 $f|B$ 的像），使得

$$
B=B_1\oplus C_1.
$$

由于 $f(B)$ 或者为 $0$，或者是无限循环群，即一个生成元上的自由群，这就证明了 $B$ 是自由的。

（当 $A$ 不是有限生成时，可以使用类似的超限论证。参见附录 2，§2，佐恩引理之后的例子。）

我们还注意到，上述证明表明 $B$ 至少存在一个基，其基数 $\leqq n$。因此，只要证明最后一个断言，即 $B$ 的任意两个基都具有相同的基数，证明就完成了。设 $S$ 是一个基，有有限个元素，个数为 $m$。设 $T$ 是另一个基，并假定 $T$ 至少含有 $r$ 个元素。只需证明 $r\leqq m$（然后<span class="original-page-anchor" id="pdf-page-57" aria-hidden="true"></span>即可使用对称性）。设 $p$ 是一个素数。则 $B/pB$ 是若干个 $p$ 阶循环群的直和，和式中共有 $m$ 项。因此它的阶为 $p^m$。以基 $T$ 代替 $S$，可知 $B/pB$ 包含 $r$ 个 $p$ 阶循环群的直积，所以 $p^r\leqq p^m$，且 $r\leqq m$，这就是所要证明的。（注意，我们并未预先假定 $T$ 是有限的。）

自由阿贝尔群 $A$ 的一个基中的元素个数称为 $A$ 的**秩**。

## §8. 有限生成阿贝尔群

本节标题中所说的群出现得如此频繁，因此值得给出一个完全描述其结构的定理。本节始终以加法记号表示阿贝尔群。

设 $A$ 是阿贝尔群。如果元素 $a\in A$ 的周期有限，就称它为一个**挠元**。$A$ 中所有挠元组成的子集是 $A$ 的一个子群，称为 $A$ 的**挠子群**。（如果 $a$ 的周期为 $m$，$b$ 的周期为 $n$，那么以加法记号表示群运算，可见 $a\pm b$ 的周期整除 $mn$。）

$A$ 的挠子群记为 $A_{\mathrm{tor}}$，或简记为 $A_t$。如果 $A=A_{\mathrm{tor}}$，即 $A$ 的所有元素都有有限阶，就称这个阿贝尔群为**挠群**。

有限生成的挠阿贝尔群显然是有限群。我们先研究挠阿贝尔群。如果 $A$ 是阿贝尔群，$p$ 是素数，则用 $A(p)$ 表示所有周期为 $p$ 的幂的元素 $x\in A$ 所组成的子群。则 $A(p)$ 是挠群，而且如果它是有限的，就是一个 $p$-群。

**定理 8.1。** *设 $A$ 是挠阿贝尔群。则 $A$ 是其子群 $A(p)$ 的直和，其中 $p$ 遍历所有满足 $A(p)\ne0$ 的素数。*

*证明。* 存在同态

$$
\bigoplus_p A(p)\to A,
$$

它将直和中的每个元素 $(x_p)$ 对应到 $A$ 中的元素 $\sum x_p$。我们证明这个同态既是满射又是单射。假定 $x$ 在核中，所以 $\sum x_p=0$。设 $q$ 是一个素数。则

$$
x_q=\sum_{p\ne q}(-x_p).
$$

设 $m$ 是右边满足 $x_q\ne0$ 且 $p\ne q$ 的元素 $x_p$ 的周期的最小公倍数。则 $mx_q=0$。另一方面，对于某个正整数 $r$，也有 $q^rx_q=0$。如果 $d$ 是 $m,q^r$ 的最大公约数，则 $dx_q=0$，但 $d=1$，所以 $x_q=0$。因此核是平凡的，同态是单射。

> **译校注。** 在定义 $m$ 时，原书印作 $x_q\ne0$。右边的元素以 $p$ 为指标，参与周期最小公倍数的非零项应满足 $x_p\ne0$ 且 $p\ne q$，因此这个条件应读作 $x_p\ne0$。

<span class="original-page-anchor" id="pdf-page-58" aria-hidden="true"></span>

至于满射性，对每个正整数 $m$，用 $A_m$ 表示乘以 $m$ 这一映射的核，即由满足 $mx=0$ 的元素 $x\in A$ 组成的子群。我们证明：

*若 $m=rs$，其中 $r,s$ 是互素的正整数，则 $A_m=A_r+A_s$。*

事实上，存在整数 $u,v$，使得 $ur+vs=1$。于是 $x=urx+vsx$，且 $urx\in A_s$，而 $vsx\in A_r$，因此我们的断言得证。归纳地重复这个过程，就得到：

$$
\text{若 }m=\prod_{p\mid m}p^{e(p)}\text{，则 }A_m=\sum_{p\mid m}A_{p^{e(p)}}.
$$

因此，映射 $\bigoplus A(p)\to A$ 是满射，定理得证。

**例。** 令 $A=\mathbf Q/\mathbf Z$。则 $\mathbf Q/\mathbf Z$ 是一个挠阿贝尔群，同构于其各子群 $(\mathbf Q/\mathbf Z)(p)$ 的直和。每个 $(\mathbf Q/\mathbf Z)(p)$ 都由可以用有理数 $a/p^k$ 表示的元素组成，其中 $a\in\mathbf Z$，$k$ 为某个正整数；也就是说，这些有理数的分母中只有 $p$ 的幂。另见第四章定理 5.1。

在下面的讨论中，我们将处理有限阿贝尔群，所以只会涉及有限多个素数（它们都整除群的阶）。在这种情形下，直和与直积是“相同的”。

我们接下来的任务是描述有限阿贝尔 $p$ 群的结构。设 $r_1,\ldots,r_s$ 是 $\geq 1$ 的整数。如果有限 $p$ 群 $A$ 同构于阶分别为 $p^{r_i}$ $(i=1,\ldots,s)$ 的循环群的积，就称 $A$ 的**型为 $(p^{r_1},\ldots,p^{r_s})$**。我们需要下面的说明。

**说明。** 设 $A$ 是有限阿贝尔 $p$ 群。设 $b$ 是 $A$ 的一个元素，$b\neq 0$。设 $k$ 是一个 $\geq 0$ 的整数，满足 $p^kb\neq 0$，并设 $p^kb$ 的周期为 $p^m$。那么 $b$ 的周期为 $p^{k+m}$。[*证明。* 显然有 $p^{k+m}b=0$；若 $p^nb=0$，则首先 $n\geq k$，其次 $n\geq k+m$，否则 $p^kb$ 的周期就会小于 $p^m$。]

**定理 8.2。** *每个有限阿贝尔 $p$ 群都同构于循环 $p$ 群的积。如果它的型为 $(p^{r_1},\ldots,p^{r_s})$，且*

$$
r_1\geq r_2\geq\cdots\geq r_s\geq 1,
$$

*则整数序列 $(r_1,\ldots,r_s)$ 是唯一确定的。*

*证明。* 我们用归纳法证明所需的积的存在性。设 $a_1\in A$ 是周期最大的元素。不失一般性，可以假设 $A$ 不是循环群。设 $A_1$ 是由 $a_1$ 生成的循环子群，其周期记为 $p^{r_1}$。我们需要一个引理。

**引理 8.3。** *设 $\bar b$ 是 $A/A_1$ 中一个周期为 $p^r$ 的元素。那么在 $A$ 中存在 $\bar b$ 的一个代表元 $a$，其周期也为 $p^r$。*

<span class="original-page-anchor" id="pdf-page-59" aria-hidden="true"></span>

*证明。* 设 $b$ 是 $\bar b$ 在 $A$ 中的任意一个代表元。那么 $p^rb$ 属于 $A_1$，可以写成 $p^rb=na_1$，其中 $n$ 是某个 $\geq 0$ 的整数。注意，$\bar b$ 的周期 $\leq b$ 的周期。如果 $n=0$，证明即告完成。否则，写成 $n=p^k\mu$，其中 $\mu$ 与 $p$ 互素。那么 $\mu a_1$ 也是 $A_1$ 的生成元，因此其周期为 $p^{r_1}$。我们可以假设 $k\leq r_1$。于是 $p^k\mu a_1$ 的周期为 $p^{r_1-k}$。由前面的说明，元素 $b$ 的周期为

$$
p^{r+r_1-k}
$$

因此由假设可知 $r+r_1-k\leq r_1$，且 $r\leq k$。这就证明存在元素 $c\in A_1$，使得 $p^rb=p^rc$。令 $a=b-c$。那么 $a$ 是 $\bar b$ 在 $A$ 中的一个代表元，且 $p^ra=0$。由于 $\operatorname{period}(a)\leq p^r$，我们得出 $a$ 的周期恰为 $p^r$。

现在回到主证明。由归纳假设，商群 $A/A_1$ 可以表示为

$$
A/A_1=\bar A_2\times\cdots\times\bar A_s,
$$

其中各因子分别是阶为 $p^{r_2},\ldots,p^{r_s}$ 的循环子群，并且可以假设 $r_2\geq\cdots\geq r_s$。设 $\bar a_i$ 是 $\bar A_i$ 的生成元 $(i=2,\ldots,s)$，并设 $a_i$ 是 $\bar a_i$ 在 $A$ 中的一个代表元，其周期与 $\bar a_i$ 相同。设 $A_i$ 是由 $a_i$ 生成的循环子群。我们断言 $A$ 是 $A_1,\ldots,A_s$ 的直和。

给定 $x\in A$，用 $\bar x$ 表示它在 $A/A_1$ 中的剩余类。存在整数 $m_i\geq 0$ $(i=2,\ldots,s)$，使得

$$
\bar x=m_2\bar a_2+\cdots+m_s\bar a_s.
$$

因此 $x-m_2a_2-\cdots-m_sa_s$ 属于 $A_1$，并且存在整数 $m_1\geq 0$，使得

$$
x=m_1a_1+m_2a_2+\cdots+m_sa_s.
$$

所以 $A_1+\cdots+A_s=A$。

反过来，假设 $m_1,\ldots,m_s$ 是 $\geq 0$ 的整数，满足

$$
0=m_1a_1+\cdots+m_sa_s.
$$

因为 $a_i$ 的周期为 $p^{r_i}$ $(i=1,\ldots,s)$，我们可以假设 $m_i<p^{r_i}$。给这个等式加上横线，得到

$$
0=m_2\bar a_2+\cdots+m_s\bar a_s.
$$

由于 $A/A_1$ 是 $\bar A_2,\ldots,\bar A_s$ 的直积，得出对 $i=2,\ldots,s$，每个 $m_i=0$。于是 $m_1=0$ 也成立，因此所有 $m_i=0$ $(i=1,\ldots,s)$。由此立即得到

$$
(A_1+\cdots+A_i)\cap A_{i+1}=0
$$

对每个 $i\geq 1$ 都成立，所以 $A$ 是 $A_1,\ldots,A_s$ 的直积，正如所要求的。

我们用归纳法证明唯一性。假设 $A$ 可以用两种方式写成循环群的直和，其型分别为

$$
(p^{r_1},\ldots,p^{r_s})\qquad\text{和}\qquad(p^{m_1},\ldots,p^{m_k})
$$

<span class="original-page-anchor" id="pdf-page-60" aria-hidden="true"></span>

其中 $r_1\geq\cdots\geq r_s\geq 1$，且 $m_1\geq\cdots\geq m_k\geq 1$。那么 $pA$ 也是一个 $p$ 群，其阶严格小于 $A$ 的阶，而它的型为

$$
(p^{r_1-1},\ldots,p^{r_s-1})\qquad\text{和}\qquad(p^{m_1-1},\ldots,p^{m_k-1}),
$$

这里的约定是：如果某个指数 $r_i$ 或 $m_j$ 等于 $1$，那么在 $pA$ 中，与

$$
p^{r_i-1}\qquad\text{或}\qquad p^{m_j-1}
$$

对应的因子就是平凡群 $0$。由归纳假设，序列

$$
(r_1-1,\ldots,r_s-1)
$$

中所有 $\geq 1$ 的整数组成的子序列是唯一确定的，并且与序列

$$
(m_1-1,\ldots,m_k-1)
$$

的对应子序列相同。换句话说，对所有满足 $r_i-1$ 或 $m_i-1\geq 1$ 的整数 $i$，都有 $r_i-1=m_i-1$。因此对这些整数 $i$ 都有 $r_i=m_i$，而两个序列

$$
(p^{r_1},\ldots,p^{r_s})\qquad\text{和}\qquad(p^{m_1},\ldots,p^{m_k})
$$

只有最后那些等于 $p$ 的分量可能不同。这些分量对应于型为 $(p,\ldots,p)$ 的因子；设 $p$ 在第一个序列中出现 $\nu$ 次，在第二个序列中出现 $\mu$ 次。于是对某个整数 $n$，$A$ 的型为

$$
(p^{r_1},\ldots,p^{r_n},\underbrace{p,\ldots,p}_{\nu\text{ 次}})\qquad\text{和}\qquad(p^{r_1},\ldots,p^{r_n},\underbrace{p,\ldots,p}_{\mu\text{ 次}}).
$$

因此，$A$ 的阶等于

$$
p^{r_1+\cdots+r_n}p^\nu=p^{r_1+\cdots+r_n}p^\mu,
$$

从而 $\nu=\mu$，定理得证。

如果群 $G$ 中一个元素 $x$ 的周期只要是有限的，$x$ 就必为单位元，那么称 $G$ **无挠**。

**定理 8.4。** *设 $A$ 是有限生成无挠阿贝尔群。那么 $A$ 是自由的。*

*证明。* 假设 $A\neq 0$。设 $S$ 是一个有限生成元集，并设 $x_1,\ldots,x_n$ 是 $S$ 中满足以下性质的一个极大子集：若整数 $v_1,\ldots,v_n$ 满足

$$
v_1x_1+\cdots+v_nx_n=0,
$$

则对所有 $j$ 都有 $v_j=0$。（注意，由于 $A\neq 0$，所以 $n\geq 1$。）设 $B$ 是由 $x_1,\ldots,x_n$ 生成的子群。那么 $B$ 是自由的。给定 $y\in S$，存在不全为零的整数 $m_1,\ldots,m_n,m$，使得

$$
my+m_1x_1+\cdots+m_nx_n=0,
$$

<span class="original-page-anchor" id="pdf-page-61" aria-hidden="true"></span>

这是由 $x_1,\ldots,x_n$ 的极大性假设得到的。进一步，$m\neq 0$；否则所有 $m_j=0$。所以 $my$ 属于 $B$。对 $A$ 的某个有限生成元集中的每一个生成元 $y$，这都成立，因此存在整数 $m\neq 0$，使得 $mA\subset B$。映射

$$
x\mapsto mx
$$

是从 $A$ 到自身的同态，由于 $A$ 无挠，其核是平凡的。因此它是从 $A$ 到 $B$ 的某个子群上的同构。由前一节的定理 7.3，得出 $mA$ 是自由的，从而 $A$ 是自由的。

**定理 8.5。** *设 $A$ 是有限生成阿贝尔群，并设 $A_{\mathrm{tor}}$ 是由 $A$ 中所有具有有限周期的元素组成的子群。那么 $A_{\mathrm{tor}}$ 是有限的，而 $A/A_{\mathrm{tor}}$ 是自由的。$A$ 中存在一个自由子群 $B$，使得 $A$ 是 $A_{\mathrm{tor}}$ 与 $B$ 的直和。*

*证明。* 回顾一下，有限生成挠阿贝尔群显然是有限的。设 $A$ 由 $n$ 个元素有限生成，并设 $F$ 是以 $n$ 个元素为生成元的自由阿贝尔群。由泛性质，存在一个从 $F$ 到 $A$ 上的满同态

$$
F\xrightarrow{\varphi}A.
$$

由定理 7.3，$F$ 的子群 $\varphi^{-1}(A_{\mathrm{tor}})$ 是有限生成的。因此 $A_{\mathrm{tor}}$ 本身是有限生成的，从而是有限的。

接下来证明 $A/A_{\mathrm{tor}}$ 无挠。设 $\bar x$ 是 $A/A_{\mathrm{tor}}$ 中的一个元素，且对某个整数 $m\neq 0$ 有 $m\bar x=0$。那么对于 $\bar x$ 在 $A$ 中的任意代表元 $x$，都有 $mx\in A_{\mathrm{tor}}$，从而对某个整数 $q\neq 0$ 有 $qmx=0$。于是 $x\in A_{\mathrm{tor}}$，所以 $\bar x=0$，且 $A/A_{\mathrm{tor}}$ 无挠。由定理 8.4，$A/A_{\mathrm{tor}}$ 是自由的。现在应用定理 7.3 中的引理，便完成了证明。

$A/A_{\mathrm{tor}}$ 的秩也称为 $A$ 的**秩**。

关于定理 8.5 在其他背景中的表述，参见第三章 §7 中主理想环上的模的结构定理，以及第三章的习题 5、6、7。

## §9. 对偶群

设 $A$ 是指数为 $m\geq 1$ 的阿贝尔群。这意味着对每个元素 $x\in A$，都有 $mx=0$。设 $Z_m$ 是阶为 $m$ 的循环群。我们用 $A^\wedge$ 或 $\operatorname{Hom}(A,Z_m)$ 表示从 $A$ 到 $Z_m$ 的同态所成的群，并称它为 $A$ 的**对偶群**。

设 $f:A\to B$ 是阿贝尔群的同态，并假设两者的指数均为 $m$。那么 $f$ 诱导一个同态

$$
f^\wedge:B^\wedge\to A^\wedge.
$$

<span class="original-page-anchor" id="pdf-page-62" aria-hidden="true"></span>

具体地，对每个 $\psi\in B^\wedge$，定义 $f^\wedge(\psi)=\psi\circ f$。容易验证，$f^\wedge$ 是同态。性质

$$
\operatorname{id}^\wedge=\operatorname{id}\qquad\text{和}\qquad(f\circ g)^\wedge=g^\wedge\circ f^\wedge
$$

也都容易验证。

**定理 9.1。** *如果有限阿贝尔群 $A$ 表示成积 $A=B\times C$，则 $A^\wedge$ 同构于 $B^\wedge\times C^\wedge$（同构由下面描述的映射给出）。有限阿贝尔群同构于它自身的对偶群。*

*证明。* 考虑 $B\times C$ 到两个分量上的投影

$$
\begin{array}{ccc}
& B\times C & \\
\overset{f}{\swarrow} && \overset{g}{\searrow}\\
B && C
\end{array}
$$

我们得到同态

$$
\begin{array}{ccc}
& (B\times C)^\wedge & \\
\overset{f^\wedge}{\nearrow} && \overset{g^\wedge}{\nwarrow}\\
B^\wedge && C^\wedge
\end{array}
$$

并且断言，这些同态诱导一个从 $B^\wedge\times C^\wedge$ 到 $(B\times C)^\wedge$ 上的同构。

事实上，设 $\psi_1,\psi_2$ 分别属于 $\operatorname{Hom}(B,Z_m)$ 和 $\operatorname{Hom}(C,Z_m)$。则 $(\psi_1,\psi_2)\in B^\wedge\times C^\wedge$；对于 $(x,y)\in B\times C$，定义

$$
(\psi_1,\psi_2)(x,y)=\psi_1(x)+\psi_2(y),
$$

就得到 $(B\times C)^\wedge$ 中的一个对应元素。这样就得到一个同态

$$
B^\wedge\times C^\wedge\to(B\times C)^\wedge.
$$

反过来，设 $\psi\in(B\times C)^\wedge$。那么

$$
\psi(x,y)=\psi(x,0)+\psi(0,y).
$$

$B$ 上由 $\psi_1(x)=\psi(x,0)$ 定义的函数 $\psi_1$ 属于 $B^\wedge$；同样，$C$ 上由 $\psi_2(y)=\psi(0,y)$ 定义的函数 $\psi_2$ 属于 $C^\wedge$。于是得到一个同态

$$
(B\times C)^\wedge\to B^\wedge\times C^\wedge,
$$

它显然是前面所定义同态的逆。因此得到一个同构，从而证明了定理中的第一个断言。

任何有限阿贝尔群都可以写成循环群的积。因此，要证明第二个断言，只须处理循环群的情形。

设 $A$ 是循环群，由一个周期为 $n$ 的元素 $x$ 生成。则 $n\mid m$，而 $Z_m$ 恰有一个阶为 $n$ 的子群 $Z_n$，它是循环群（命题 4.3(iv)）。

<span class="original-page-anchor" id="pdf-page-63" aria-hidden="true"></span>

如果 $\psi:A\to Z_m$ 是同态，且 $x$ 是 $A$ 的一个生成元，那么 $x$ 的周期是 $\psi(x)$ 的一个指数，因此 $\psi(x)$，进而整个 $\psi(A)$，都包含在 $Z_n$ 中。设 $y$ 是 $Z_n$ 的一个生成元。我们有同构

$$
\psi_1:A\to Z_n,
$$

满足 $\psi_1(x)=y$。对每个满足 $0\leq k<n$ 的整数 $k$，都有同态 $k\psi_1$，使得

$$
(k\psi_1)(x)=k\cdot\psi_1(x)=\psi_1(kx).
$$

这样就得到 $A^\wedge$ 的一个循环子群，由 $n$ 个元素 $k\psi_1$ $(0\leq k<n)$ 组成。反过来，$A^\wedge$ 的任意元素 $\psi$ 都由它在生成元 $x$ 上的作用唯一确定，而且必须把 $x$ 映到 $Z_n$ 的 $n$ 个元素 $ky$ $(0\leq k<n)$ 中的某一个。〔译校注：原文印作 $kx$；因目标群 $Z_n$ 的生成元为 $y$，此处应为 $ky$。〕因此 $\psi$ 等于映射 $k\psi_1$ 中的某一个。这些映射组成整个群 $A^\wedge$，所以它是阶为 $n$、由 $\psi_1$ 生成的循环群。这就证明了定理。

在考虑对偶群时，可以选取各种不同的循环群 $Z_m$。这类群在许多应用中都会出现，例如复数中的 $m$ 次单位根群、$\mathbf Q/\mathbf Z$ 中阶为 $m$ 的子群等等。

设 $A,A'$ 是两个阿贝尔群。从 $A\times A'$ 到阿贝尔群 $C$ 的**双线性映射**是一个映射

$$
A\times A'\to C,
$$

记作

$$
(x,x')\mapsto\langle x,x'\rangle,
$$

它具有以下性质：对于每个 $x\in A$，函数 $x'\mapsto\langle x,x'\rangle$ 是同态；同样，对于每个 $x'\in A'$，函数 $x\mapsto\langle x,x'\rangle$ 是同态。

双线性映射的一个特例是映射

$$
A\times\operatorname{Hom}(A,C)\to C,
$$

它把每个满足 $x\in A$ 且 $f\in\operatorname{Hom}(A,C)$ 的二元组 $(x,f)$ 映到 $C$ 中的元素 $f(x)$。

双线性映射也称为**配对**。

如果对所有 $x'\in S'$ 都有 $\langle x,x'\rangle=0$，就称元素 $x\in A$ 与 $A'$ 的子集 $S'$ **正交**（或**垂直**）。显然，$A$ 中与 $S'$ 正交的元素组成 $A$ 的一个子群。对于 $A'$ 中与 $A$ 的子集正交的元素，也作类似的定义。

这个双线性映射的左**核**是 $A$ 中与整个 $A'$ 正交的子群。其右核也作类似定义。

给定双线性映射 $A\times A'\to C$，设 $B,B'$ 分别是它的左核与右核。$A'$ 的一个元素 $x'$ 给出 $\operatorname{Hom}(A,C)$ 中的一个元素，即映射 $x\mapsto\langle x,x'\rangle$，我们将它记为 $\psi_{x'}$。由于 $\psi_{x'}$ 在 $B$ 上为零，所以 $\psi_{x'}$ 实际上是从 $A/B$ 到 $C$ 的同态。

<span class="original-page-anchor" id="pdf-page-64" aria-hidden="true"></span>

此外，如果 $x',y'$ 是 $A'$ 中满足

$$
x'\equiv y'\pmod{B'}
$$

的元素，则 $\psi_{x'}=\psi_{y'}$。所以 $\psi$ 实际上给出一个同态

$$
0\to A'/B'\to\operatorname{Hom}(A/B,C).
$$

它是单射，因为 $B'$ 被定义为与 $A$ 正交的群。类似地，我们得到单同态

$$
0\to A/B\to\operatorname{Hom}(A'/B',C).
$$

假设 $C$ 是阶为 $m$ 的循环群。那么对任意 $x'\in A'$，都有

$$
m\psi_{x'}=\psi_{mx'}=0,
$$

因此 $A'/B'$ 的指数为 $m$。同样，$A/B$ 的指数为 $m$。

**定理 9.2。** *设 $A\times A'\to C$ 是从两个阿贝尔群到阶为 $m$ 的循环群 $C$ 的双线性映射。设 $B,B'$ 分别为它的左核和右核。假设 $A'/B'$ 是有限的。那么 $A/B$ 是有限的，且 $A'/B'$ 同构于 $A/B$ 的对偶群（同构由映射 $\psi$ 给出）。*

*证明。* 从 $A/B$ 到 $\operatorname{Hom}(A'/B',C)$ 的单射表明，$A/B$ 是有限的。进一步，得到不等式

$$
\operatorname{ord}A/B\leq\operatorname{ord}(A'/B')^\wedge=\operatorname{ord}A'/B'
$$

以及

$$
\operatorname{ord}A'/B'\leq\operatorname{ord}(A/B)^\wedge=\operatorname{ord}A/B.
$$

由此可知，映射 $\psi$ 是双射，因而是同构。

**推论 9.3。** *设 $A$ 是有限阿贝尔群，$B$ 是它的一个子群，$A^\wedge$ 是对偶群，而 $B^\perp$ 是由满足 $\varphi(B)=0$ 的所有 $\varphi\in A^\wedge$ 组成的集合。那么 $A^\wedge/B^\perp$ 与 $B^\wedge$ 之间存在一个自然同构。*

*证明。* 这是定理 9.2 的一个特例。

## §10. 逆极限与完备化

考虑一列群 $\{G_n\}$ $(n=0,1,2,\ldots)$，并假设对所有 $n\geq 1$，给定同态

$$
f_n:G_n\to G_{n-1}.
$$

先假设这些同态都是满射。我们构造无穷序列

$$
x=(x_0,x_1,x_2,\ldots),\qquad\text{使得 }x_{n-1}=f_n(x_n).
$$

<span class="original-page-anchor" id="pdf-page-65" aria-hidden="true"></span>

由满射性假设，给定 $x_n\in G_n$，总可以通过 $f_{n+1}$ 将 $x_n$ 提升到 $G_{n+1}$，所以这样的无穷序列存在，并且可以投影到任意给定的 $x_0$。我们可以逐分量定义这些序列的乘法，随即容易验证，这些序列构成一个群，称为族 $\{(G_n,f_n)\}$ 的**逆极限**。我们把逆极限记作 $\varprojlim(G_n,f_n)$；如果所指的 $f_n$ 是清楚的，也可以简单地记作 $\varprojlim G_n$。

**例。** 设 $A$ 是一个加法阿贝尔群。设 $p$ 是素数。用 $p_A:A\to A$ 表示乘以 $p$ 的映射。如果 $p_A$ 是满射，就称 $A$ 是 **$p$ 可除的**。此时，对所有 $n$ 取 $A_n=A$，并对所有 $n$ 取 $f_n=p_A$，就可以构造逆极限。这个逆极限记作 $V_p(A)$。用 $T_p(A)$ 表示 $V_p(A)$ 中由上面那些满足 $x_0=0$ 的无穷序列组成的子集。设 $A[p^n]$ 是 $p_A^n$ 的核。那么

$$
T_p(A)=\varprojlim A[p^{n+1}].
$$

群 $T_p(A)$ 称为与 $p$ 可除群 $A$ 相联系的 **Tate 群**。它出现于 Deuring 和 Weil 所研究的相当深奥的代数几何背景中，即 20 世纪 40 年代发展起来的椭圆曲线与阿贝尔簇理论，这些内容远超出本书的范围。有兴趣的读者可以参阅这些主题的书籍。

最常见的 $p$ 可除群可按如下方式得到。首先，设 $A$ 是 $\mathbf Q/\mathbf Z$ 的子群，由可以写成 $a/p^k$ 形式的有理数（模 $\mathbf Z$）组成，其中 $k$ 是某个正整数，$a\in\mathbf Z$。那么 $A$ 是 $p$ 可除的。

其次，设 $\boldsymbol\mu[p^n]$ 是复数中的 $p^n$ 次单位根群。设 $\boldsymbol\mu[p^\infty]$ 是对所有 $n$ 的 $\boldsymbol\mu[p^n]$ 的并。那么 $\boldsymbol\mu[p^\infty]$ 是 $p$ 可除的，并且同构于前一段中的群 $A$。因此

$$
T_p(\boldsymbol\mu)=\varprojlim\boldsymbol\mu[p^n].
$$

这些群在数论和代数几何中十分重要。我们将在第三章 §10 中，在一个更广泛的背景下进一步讨论它们。

**例。** 假设给定一个群 $G$。设 $\{H_n\}$ 是一列正规子群，满足对所有 $n$ 都有 $H_n\supset H_{n+1}$。设

$$
f_n:G/H_n\to G/H_{n-1}
$$

是典范同态。那么可以构造逆极限 $\varprojlim G/H_n$。注意，$G$ 有一个自然同态

$$
g:G\to\varprojlim G/H_n,
$$

它把元素 $x$ 映到序列 $(\ldots,x_n,\ldots)$，其中 $x_n$ 是 $x$ 在 $G/H_n$ 中的像。

**例。** 对每个 $n\geq 0$，令 $G_n=\mathbf Z/p^{n+1}\mathbf Z$。设

$$
f_n:\mathbf Z/p^{n+1}\mathbf Z\to\mathbf Z/p^n\mathbf Z
$$

是典范同态。那么 $f_n$ 是满射，而这个极限称为<span class="original-page-anchor" id="pdf-page-66" aria-hidden="true"></span>**$p$ 进整数群**，记作 $\mathbf Z_p$。我们将在第三章 §10 中再讨论这一对象，届时将看到 $\mathbf Z_p$ 也是一个环。

在这些例子之后，我们要考虑更一般的情形：所处理的不是一列群，而是更一般类型的群族，其中的群也未必可交换。因此，我们来定义一般情形下群的逆极限。

设 $I$ 是一个指标集。假设 $I$ 上给定了一个偏序关系，即对某些二元组 $(i,j)$，有关系 $i\leq j$，并满足以下条件：对于 $I$ 中所有 $i,j,k$，都有 $i\leq i$；若 $i\leq j$ 且 $j\leq k$，则 $i\leq k$；若 $i\leq j$ 且 $j\leq i$，则 $i=j$。如果给定 $i,j\in I$，都存在 $k$，使得 $i\leq k$ 且 $j\leq k$，就称 $I$ 是**有向的**。假设 $I$ 是有向的。所谓群的一个**逆向有向族**，是指一个族 $\{G_i\}_{i\in I}$，以及对每对 $i\leq j$ 给定的同态

$$
f_i^j:G_j\to G_i,
$$

使得每当 $k\leq i\leq j$ 时，都有

$$
f_k^i\circ f_i^j=f_k^j\qquad\text{且}\qquad f_i^i=\operatorname{id}.
$$

设 $G=\prod G_i$ 是这个族的积。设 $\Gamma$ 是 $G$ 的子集，由所有满足 $x_i\in G_i$，且对所有 $i$ 及 $j\geq i$ 都有

$$
f_i^j(x_j)=x_i
$$

的元素 $(x_i)$ 组成。那么 $\Gamma$ 包含单位元，并且容易验证它是 $G$ 的一个子群。我们称 $\Gamma$ 为这个族的**逆极限**，并记作

$$
\Gamma=\varprojlim G_i.
$$

**例。** 设 $G$ 是一个群。设 $\mathfrak F$ 是所有有限指数正规子群组成的族。如果 $H,K$ 都是有限指数的正规子群，则 $H\cap K$ 也是如此，所以 $\mathfrak F$ 是一个有向族。因此，可以构造 $H\in\mathfrak F$ 时的逆极限 $\varprojlim G/H$。这个主题还有一个变形：不用 $\mathfrak F$，而是给定一个素数 $p$，令 $\mathfrak F_p$ 为所有指数有限且等于 $p$ 的某个幂的正规子群组成的族。那么也可以构造关于子群 $H\in\mathfrak F_p$ 的逆极限。（请验证：若正规子群 $H,K$ 的指数都是有限的 $p$ 的幂，则它们的交也具有这一性质。）

如果一个群是有限群的逆极限，就称它为**副有限群**。

**应用中的例子。** 这样的逆极限出现在伽罗瓦理论中。设 $k$ 是一个域，$A$ 是一个无限伽罗瓦扩张。例如，$k=\mathbf Q$，而 $A$ 是 $\mathbf Q$ 的一个代数闭包。设 $G$ 是伽罗瓦群，即 $A$ 在 $k$ 上的自同构群。那么 $G$ 是商群 $G/H$ 的逆极限，其中 $H$ 遍历 $A$ 在 $K$ 上的伽罗瓦群，而 $K$ 遍历 $A$ 中包含的所有 $k$ 的有限扩张。参见伽罗瓦理论一章中的 Shafarevich 猜想，即第六章猜想 14.2。

**译校注。** 原文保留“all finite extensions”（所有有限扩张）的表述。本段构造的是商群 $G/H$ 的逆极限，因而这里须取正规子群 $H$，即取 $A$ 中的有限伽罗瓦中间扩张 $K/k$。这些有限伽罗瓦中间扩张在所有有限中间扩张中共尾：任意有限中间扩张都包含在 $A$ 内的某个有限伽罗瓦中间扩张中。

类似地，考虑一个亏格 $\geq 2$ 的紧黎曼曲面 $X$。设 $p:X'\to X$ 是万有覆盖空间。设 $\mathbf C(X)=F$ 和 $\mathbf C(X')=F'$ 是函数域。那么存在嵌入 $\pi_1(X)\hookrightarrow\operatorname{Gal}(F'/F)$。复分析中证明了，$\pi_1(X)$ 是一个具有一个交换子<span class="original-page-anchor" id="pdf-page-67" aria-hidden="true"></span>关系的自由群。$F'/F$ 的整个伽罗瓦群是关于有限指数子群的逆极限，正如上面的一般情形。

### 群的完备化

现在假设给定一个群 $G$；先为简单起见，假设给定一列正规子群 $\{H_r\}$，满足对所有 $r$ 都有 $H_r\supset H_{r+1}$，并且这些子群具有有限指数。$G$ 中的一列元素 $\{x_n\}$ 称为**柯西序列**，如果给定 $H_r$，存在 $N$，使得对所有 $m,n\geq N$ 都有 $x_nx_m^{-1}\in H_r$。如果给定 $r$，存在 $N$，使得对所有 $n\geq N$ 都有 $x_n\in H_r$，则称 $\{x_n\}$ 是**零序列**。请作为练习证明：柯西序列在逐项乘法下构成一个群，而零序列构成一个正规子群。相应的商群称为 $G$ 的**完备化**（关于这列正规子群而言）。

注意，从 $G$ 到其完备化有一个自然同态：元素 $x\in G$ 映到常值序列 $(x,x,x,\ldots)$ 模掉零序列后所得的类。这个同态的核是交 $\bigcap H_r$，因此，如果这个交只有 $G$ 的单位元，那么从 $G$ 到其完备化的映射就是一个嵌入。

**定理 10.1。** *完备化与逆极限 $\varprojlim G/H_r$ 在自然映射下同构。*

*证明。* 我们给出这些映射。设 $x=\{x_n\}$ 是一个柯西序列。给定 $r$，由柯西序列的定义可知，当 $n$ 充分大时，$x_n$ 模 $H_r$ 的类与 $n$ 无关。将这个类记作 $x(r)$。那么序列 $(x(1),x(2),\ldots)$ 定义了逆极限中的一个元素。反过来，给定逆极限中的元素 $(\bar x_1,\bar x_2,\ldots)$，其中 $\bar x_n\in G/H_n$，取 $x_n$ 为其在 $G$ 中的一个代表元。那么序列 $\{x_n\}$ 是柯西序列。留给读者验证：柯西序列 $\{x_n\}$ 模零序列的类是良定义的，而且我们定义的映射是完备化与逆极限之间互为逆的同构。

我们使用序列和可数性，是为了更清楚地呈现与实数构造之间的类比。一般地，给定族 $\mathfrak F$，所谓柯西族，是指一个由任意有向集 $J$ 编号的族 $\{x_j\}_{j\in J}$，使得对每个 $H\in\mathfrak F$，都存在 $j\in J$，使得对所有 $k,k'\geq j$ 都有 $x_kx_{k'}^{-1}\in H$。实际中可以使用序列，因为自然出现的群通常具有这样的性质：有限指数子群组成的集合是可数的。当群 $G$ 是有限生成群时，就会出现这种情形。

更一般地，如果对于给定的 $H\in\mathfrak F$，都存在 $i$，使得 $H_i\subset H$，则称正规子群族 $\{H_i\}\subset\mathfrak F$ 在 $\mathfrak F$ 中是**共尾的**。假设存在这样一个可数的族，即 $i=1,2,\ldots$ 遍历正整数。那么请作为练习证明，存在同构

$$
\varprojlim_i G/H_i\approx\varprojlim_{H\in\mathfrak F}G/H,
$$

<span class="original-page-anchor" id="pdf-page-68" aria-hidden="true"></span>

或者等价地说，$G$ 关于序列 $\{H_i\}$ 的完备化，与它关于整个族 $\mathfrak{F}$ 的完备化是“相同的”。这一验证留给读者。

完备化过程在数学中经常出现。例如，我们将在第三章 §10 中提及环的完备化；而在第十二章中将讨论域的完备化。

## §11. 范畴与函子

在继续讨论之前，现在引入一些新术语会比较方便。我们已经遇到几种对象：集合、幺半群、群。以后还会遇到更多种对象，并且对于每一类这样的对象，我们都定义它们之间的特殊映射（例如同态）。所有这些对象都具有一些共同的形式性质，即存在从一个对象到自身的恒等映射，以及连续进行的映射满足结合律。我们引入范畴的概念，为所有这些情况提供一个一般的框架。

一个**范畴** $\mathfrak{A}$ 由如下资料组成：一族对象 $\operatorname{Ob}(\mathfrak{A})$；对于两个对象 $A,B\in\operatorname{Ob}(\mathfrak{A})$，有一个集合 $\operatorname{Mor}(A,B)$，称为从 $A$ 到 $B$ 的**态射**集合；对于三个对象 $A,B,C\in\operatorname{Ob}(\mathfrak{A})$，有一个复合运算（即一个映射）

$$
\operatorname{Mor}(B,C)\times\operatorname{Mor}(A,B)\longrightarrow\operatorname{Mor}(A,C),
$$

满足下列公理：

**CAT 1.** 两个集合 $\operatorname{Mor}(A,B)$ 与 $\operatorname{Mor}(A',B')$ 互不相交，除非 $A=A'$ 且 $B=B'$；在这种情况下，它们相等。

**CAT 2.** 对 $\mathfrak{A}$ 的每一个对象 $A$，都有一个态射 $\operatorname{id}_A\in\operatorname{Mor}(A,A)$，对于所有对象 $B\in\operatorname{Ob}(\mathfrak{A})$，它分别作为 $\operatorname{Mor}(A,B)$ 中元素的右单位元和 $\operatorname{Mor}(B,A)$ 中元素的左单位元。

**CAT 3.** 复合运算在有定义时满足结合律，即给定 $f\in\operatorname{Mor}(A,B)$、$g\in\operatorname{Mor}(B,C)$ 和 $h\in\operatorname{Mor}(C,D)$，则有

$$
(h\circ g)\circ f=h\circ(g\circ f),
$$

这里 $A,B,C,D$ 是 $\mathfrak{A}$ 的任意对象。

我们将 $\operatorname{Mor}(B,C)$ 中的元素 $g$ 与 $\operatorname{Mor}(A,B)$ 中的元素 $f$ 的复合写成 $g\circ f$，以使人联想到映射的复合。在本书的实际讨论中，我们将会看到，我们的大多数态射确实是映射，或者与映射密切相关。

范畴 $\mathfrak{A}$ 中全体态射组成的族记为 $\operatorname{Ar}(\mathfrak{A})$（“$\mathfrak{A}$ 的箭头”）。我们有时用符号“$f\in\operatorname{Ar}(\mathfrak{A})$”来表示<span class="original-page-anchor" id="pdf-page-69" aria-hidden="true"></span>$f$ 是 $\mathfrak{A}$ 的一个态射，即对于某些 $A,B\in\operatorname{Ob}(\mathfrak{A})$，$f$ 是某个集合 $\operatorname{Mor}(A,B)$ 的元素。

如果所指的态射已经清楚，我们有时会不严格地区分对象族与范畴本身，把对象族称为范畴。

一个元素 $f\in\operatorname{Mor}(A,B)$ 也写作 $f:A\to B$ 或

$$
A\xrightarrow{f}B.
$$

如果存在一个态射 $g:B\to A$，使得 $g\circ f$ 和 $f\circ g$ 分别是 $\operatorname{Mor}(A,A)$ 和 $\operatorname{Mor}(B,B)$ 中的恒等态射，就称态射 $f$ 为一个**同构**。若 $A=B$，也称这个同构为一个**自同构**。

从一个对象 $A$ 到自身的态射称为一个**自态射**。$A$ 的自态射集合记为 $\operatorname{End}(A)$。由我们的公理立即可知，$\operatorname{End}(A)$ 是一个幺半群。

设 $A$ 是范畴 $\mathfrak{A}$ 的一个对象。我们用 $\operatorname{Aut}(A)$ 表示 $A$ 的自同构集合。这个集合实际上是一个群，因为我们的所有定义都安排得恰好可以立即看出群公理成立（结合律、单位元以及逆元的存在性）。因此，我们现在开始看到抽象范畴与更具体的范畴之间的一些相互联系。

**例。** 设 $\mathfrak{S}$ 是以集合为对象、以集合之间的映射为态射的范畴。我们简称 $\mathfrak{S}$ 为集合范畴。三个公理 **CAT 1、2、3** 显然成立。

设 **Grp** 是群范畴，即以群为对象、以群同态为态射的范畴。这里三个公理也显然成立。同样，我们有幺半群范畴，记为 **Mon**。

以后，当我们定义了环和模，便会清楚环组成一个范畴，一个环上的模也组成一个范畴。

这里需要强调，存在态射集合不是阿贝尔群的范畴。其中一些最重要的例子是：

范畴 $\mathcal{C}^0$，其对象是 $\mathbf{R}^n$ 中的开集，态射是连续映射。

范畴 $\mathcal{C}^\infty$，其对象相同，但态射是 $C^\infty$ 映射。

范畴 **Hol**，其对象是 $\mathbf{C}^n$ 中的开集，态射是全纯映射。每一种情形都满足范畴的公理；例如，对 **Hol** 而言，全纯映射的复合仍是全纯映射，其他类型的映射也类似。因此，一个 $C^0$ 同构是一个连续映射 $f:U\to V$，它具有连续的逆映射 $g:V\to U$。注意，一个映射可以是 $C^0$ 同构，而不是 $C^\infty$ 同构。例如，$x\mapsto x^3$ 是 $\mathbf{R}$ 的一个 $C^0$ 自同构，但其逆映射不可微。

在数学中，人们研究上述任一范畴中的流形。确定各个范畴中的自同构群，是研究该范畴的数学领域的基本问题之一。在<span class="original-page-anchor" id="pdf-page-70" aria-hidden="true"></span>复分析中，人们在早期就确定了单位圆盘的全纯自同构群，它是由所有形如

$$
z\longmapsto e^{i\theta}\frac{c-z}{1-\bar c z}
$$

的映射组成的群，其中 $\theta$ 为实数，$c\in\mathbf{C}$，$|c|<1$。

接下来，我们考虑范畴中的作用概念。首先注意，如果 $G$ 是一个群，那么 $G$ 集组成一个范畴，它的态射是满足 $f(xs)=xf(s)$（$x\in G$、$s\in S$）的映射 $f:S\to S'$。

更一般地，我们现在可以定义群 $G$ 在任意范畴中的一个对象上的作用概念。事实上，设 $\mathfrak{A}$ 是一个范畴，$A\in\operatorname{Ob}(\mathfrak{A})$。我们把从 $G$ 到群 $\operatorname{Aut}(A)$ 的一个同态称为 $G$ 在 $A$ 上的一个**作用**。在实际情形中，对象 $A$ 是一个含有元素的集合，而 $\operatorname{Aut}(A)$ 中的一个自同构作用于作为集合的 $A$，即诱导 $A$ 的一个置换。因此，如果我们有一个同态

$$
\rho:G\longrightarrow\operatorname{Aut}(A),
$$

那么对于每个 $x\in G$，都有 $A$ 的一个自同构 $\rho(x)$，它是 $A$ 的一个置换。

群 $G$ 在对象 $A$ 上的一个作用，也称为 $G$ 在 $A$ 上的一个**表示**；这时我们说 $G$ 被**表示**为 $A$ 的一个自同构群。

**例。** 表示出现在许多场合。在本书中，我们将遇到群在有限维向量空间上的表示，第十八章将较为深入地讨论这一理论。我们还将讨论群在一个环上的模上的表示。在拓扑学和微分几何中，人们把群表示为作用于各种拓扑空间（例如球面）的群。因此，如果 $X$ 是一个微分流形或拓扑流形，而 $G$ 是一个群，就考虑所有可能的从 $G$ 到 $\operatorname{Aut}(X)$ 的同态，其中 Aut 是指当前所讨论的范畴中的自同构。因此，$G$ 可以被表示到 $C^0$ 自同构群、$C^\infty$ 自同构群或解析自同构群中。这些拓扑理论与代数理论并非相互独立，因为由函子性，$G$ 在流形上的作用会在各种代数函子（同调、$K$ 函子等）上诱导一个作用；从而在一定程度上，可以通过在相应群、向量空间或模上的函子性作用，分析拓扑问题或微分问题。

设 $A,B$ 是范畴 $\mathfrak{A}$ 的对象。设 $\operatorname{Iso}(A,B)$ 为从 $A$ 到 $B$ 的同构集合。那么群 $\operatorname{Aut}(B)$ 通过复合作用于 $\operatorname{Iso}(A,B)$；具体来说，若 $u\in\operatorname{Iso}(A,B)$ 且 $v\in\operatorname{Aut}(B)$，则 $(v,u)\mapsto v\circ u$ 给出这一作用。如果 $u_0$ 是 $\operatorname{Iso}(A,B)$ 的一个元素，那么 $u_0$ 的轨道就是整个 $\operatorname{Iso}(A,B)$，因此 $v\mapsto v\circ u_0$ 是一个双射 $\operatorname{Aut}(B)\to\operatorname{Iso}(A,B)$。它的逆映射由 $u\mapsto u\circ u_0^{-1}$ 给出。这个简单的形式论述十分基本，并且在上述每一种经典范畴中都不断得到应用。当然，在另一侧我们也有<span class="original-page-anchor" id="pdf-page-71" aria-hidden="true"></span>类似的双射，但群 $\operatorname{Aut}(A)$ 通过复合从 $\operatorname{Iso}(A,B)$ 的**右侧**作用。此外，如果 $u:A\to B$ 是一个同构，那么 $\operatorname{Aut}(A)$ 与 $\operatorname{Aut}(B)$ 通过共轭同构，即

$$
w\longmapsto uwu^{-1}\quad\text{是一个同构 }\operatorname{Aut}(A)\longrightarrow\operatorname{Aut}(B).
$$

两个这样的同构相差一个内自同构。可以通过下面的交换图直观地表示这一体系。

![交换图 1](/library/volume-86/diagrams/pdf-0071-diagram-1.png)

设 $\rho:G\to\operatorname{Aut}(A)$ 和 $\rho':G\to\operatorname{Aut}(A')$ 是群 $G$ 在同一个范畴中的两个对象 $A$ 和 $A'$ 上的表示。从 $\rho$ 到 $\rho'$ 的一个**态射**，是一个态射 $h:A\to A'$，使得对于所有 $x\in G$，下图交换：

![交换图 2](/library/volume-86/diagrams/pdf-0071-diagram-2.png)

于是很清楚，群 $G$ 在范畴 $\mathfrak{A}$ 的对象上的表示本身也组成一个范畴。因此，一个**表示的同构**就是使上述图交换的同构 $h:A\to A'$。表示的同构经常被称为等价，但我不喜欢改动范畴术语的一般体系。注意，如果 $h$ 是表示的一个同构，那么令 $[h]$ 表示以 $h$ 进行共轭，我们便可以用下面的等价图代替上面的交换图：

![交换图 3](/library/volume-86/diagrams/pdf-0071-diagram-3.png)

接下来考虑 $\mathfrak{A}$ 为阿贝尔群范畴的情形，我们可以把它记为 **Ab**。设 $A$ 是一个阿贝尔群，$G$ 是一个群。给定 $G$ 在阿贝尔群 $A$ 上的一个作用，即一个同态

$$
\rho:G\longrightarrow\operatorname{Aut}(A),
$$

我们用 $x\cdot a$ 表示元素 $\rho_x(a)$。于是可以看出，对于所有 $x,y\in G$、$a,b\in A$，有：

<span class="original-page-anchor" id="pdf-page-72" aria-hidden="true"></span>

$$
\begin{aligned}
x\cdot(y\cdot a)&=(xy)\cdot a,&x\cdot(a+b)&=x\cdot a+x\cdot b,\\
e\cdot a&=a,&x\cdot0&=0.
\end{aligned}
$$

我们注意到，当一个群 $G$ 通过共轭作用于自身时，$G$ 不仅作用于作为集合的自身，而且也作用于作为群范畴中对象的自身，即这个作用所诱导的置换实际上是群自同构。

同样，我们以后还将引入其他范畴（环、模、域），而我们已经给出了一个一般的定义，说明一个群作用于这些范畴中任一对象的含义。

设 $\mathfrak{A}$ 是一个范畴。我们可以取 $\mathfrak{A}$ 的态射作为一个新范畴 $\mathfrak{C}$ 的对象。如果 $f:A\to B$ 和 $f':A'\to B'$ 是 $\mathfrak{A}$ 中的两个态射（因而是 $\mathfrak{C}$ 的对象），那么我们把（$\mathfrak{C}$ 中的）一个**态射** $f\to f'$ 定义为 $\mathfrak{A}$ 中的一对态射 $(\varphi,\psi)$，它们使下图交换：

![交换图 1](/library/volume-86/diagrams/pdf-0072-diagram-1.png)

这样，显然 $\mathfrak{C}$ 是一个范畴。严格说来，与集合的映射一样，我们应当以 $f$ 和 $f'$ 为 $(\varphi,\psi)$ 加上指标（否则 **CAT 1** 未必满足），但在实际使用中省略这种指标。

这个例子有许多变式。例如，我们可以把注意力限制在 $\mathfrak{A}$ 中具有固定出发对象的态射上，或者具有固定到达对象的态射上。

因此，设 $A$ 是 $\mathfrak{A}$ 的一个对象，设 $\mathfrak{A}_A$ 是以 $\mathfrak{A}$ 中到达对象为 $A$ 的态射

$$
f:X\longrightarrow A
$$

为对象的范畴。$\mathfrak{A}_A$ 中从 $f:X\to A$ 到 $g:Y\to A$ 的一个态射，就是 $\mathfrak{A}$ 中使下图交换的一个态射

$$
h:X\longrightarrow Y:
$$

![交换图 2](/library/volume-86/diagrams/pdf-0072-diagram-2.png)

### 泛对象

设 $\mathfrak{C}$ 是一个范畴。如果从 $\mathfrak{C}$ 的每个对象到 $P$ 都存在唯一的态射，就称 $\mathfrak{C}$ 的对象 $P$ 为**泛吸引对象**；如果对于 $\mathfrak{C}$ 的每个对象，从 $P$ 到这个对象都存在唯一的态射，就称 $P$ 为**泛排斥对象**。

<span class="original-page-anchor" id="pdf-page-73" aria-hidden="true"></span>

当上下文使我们的意思清楚时，就称上述对象 $P$ 为**泛对象**。由于泛对象 $P$ 有到自身的恒等态射，显然，如果 $P,P'$ 是 $\mathfrak{C}$ 中的两个泛对象，那么它们之间存在唯一的同构。

**例。** 注意，只含一个元素的平凡群，是群范畴中的泛对象（既泛排斥又泛吸引）。同样，在关于环的第二章中，你将看到整数 $\mathbf{Z}$ 是环范畴中的泛对象（泛排斥）。

接下来，设 $S$ 是一个集合。设 $\mathfrak{C}$ 是这样一个范畴：它的对象是从 $S$ 到阿贝尔群的映射 $f:S\to A$，它的态射是显然应当取的那些态射。具体地说，若 $f:S\to A$ 和 $f':S\to A'$ 是两个到阿贝尔群的映射，那么从 $f$ 到 $f'$ 的一个态射，就是使通常的图交换的一个（群）同态 $g:A\to A'$，即 $g\circ f=f'$。那么由 $S$ 生成的自由阿贝尔群是这个范畴中的泛对象。这是我们已经证明的关于这个群的性质的另一种表述。

设 $M$ 是一个交换幺半群，设 $\gamma:M\to K(M)$ 是从 $M$ 到它的 Grothendieck 群的典范同态。那么 $\gamma$ 是从 $M$ 到阿贝尔群的同态所组成的范畴中的泛对象。

在本书中，我们将在许多场合定义泛对象。除了紧接这些例子之后的积与余积，还有正向极限和逆向极限；第十六章 §1 中的张量积；第十九章 §1 中的交错积；第十九章 §4 中的 Clifford 代数；等等。

现在我们转向任意范畴中的积的概念。

### 积与余积

设 $\mathfrak{A}$ 是一个范畴，$A,B$ 是 $\mathfrak{A}$ 的对象。所谓 **$\mathfrak{A}$ 中 $A,B$ 的一个积**，是指一个三元组 $(P,f,g)$，它由 $\mathfrak{A}$ 中的一个对象 $P$ 和两个态射

![交换图 1](/library/volume-86/diagrams/pdf-0073-diagram-1.png)

组成，并满足下列条件：给定 $\mathfrak{A}$ 中的两个态射

$$
\varphi:C\longrightarrow A\quad\text{和}\quad\psi:C\longrightarrow B,
$$

存在唯一的态射 $h:C\to P$，使下图交换：

![交换图 2](/library/volume-86/diagrams/pdf-0073-diagram-2.png)

换言之，$\varphi=f\circ h$ 且 $\psi=g\circ h$。

<span class="original-page-anchor" id="pdf-page-74" aria-hidden="true"></span>

更一般地，给定 $\mathfrak{A}$ 中的一族对象 $\{A_i\}_{i\in I}$，这一族的一个**积**由 $(P,\{f_i\}_{i\in I})$ 构成，其中 $P$ 是 $\mathfrak{A}$ 的一个对象，$\{f_i\}_{i\in I}$ 是一族态射

$$
f_i:P\longrightarrow A_i,
$$

并满足下列条件：给定一族态射

$$
g_i:C\longrightarrow A_i,
$$

存在唯一的态射 $h:C\to P$，使得对所有 $i$ 都有 $f_i\circ h=g_i$。

**例。** 设 $\mathfrak{A}$ 是集合范畴，$\{A_i\}_{i\in I}$ 是一族集合。设 $A=\prod_{i\in I}A_i$ 是它们的笛卡尔积，$p_i:A\to A_i$ 是到第 $i$ 个因子的投影。那么 $(A,\{p_i\})$ 显然满足集合范畴中一个积的要求。

在记号上，我们通常用 $A\times B$ 表示一个范畴中两个对象的积，用 $\prod_{i\in I}A_i$ 表示一个范畴中任意对象族的积，沿用集合范畴中的记号。

**例。** *设 $\{G_i\}_{i\in I}$ 是一族群，设 $G=\prod_iG_i$ 是它们的直积。设 $p_i:G\to G_i$ 是投影同态。那么这些资料构成这一族群在群范畴中的一个积。*

事实上，如果 $\{g_i:G'\to G_i\}_{i\in I}$ 是一族同态，那么存在唯一的同态 $g:G'\to\prod G_i$，使所要求的图交换。它就是对 $x'\in G'$ 和每个 $i\in I$ 满足 $g(x')_i=g_i(x')$ 的同态。

设 $A,B$ 是范畴 $\mathfrak{A}$ 的对象。我们注意到，$A,B$ 的积在下述范畴中是泛对象：它的对象由 $\mathfrak{A}$ 中的态射对 $f:C\to A$ 和 $g:C\to B$ 组成，它的态射如下描述。设 $f':C'\to A$ 和 $g':C'\to B$ 是另一对这样的态射。那么从第一对到第二对的一个态射，是 $\mathfrak{A}$ 中使下图交换的一个态射 $h:C\to C'$：

![交换图](/library/volume-86/diagrams/pdf-0074-diagram-1.png)

对于对象族 $\{A_i\}_{i\in I}$ 的积，情形也是类似的。

我们还将遇到对偶概念：设 $\{A_i\}_{i\in I}$ 是范畴 $\mathfrak{A}$ 中的一族对象。所谓它们的**余积**，是指一个二元组 $(S,\{f_i\}_{i\in I})$，它由一个对象 $S$ 和一族态射

$$
\{f_i:A_i\longrightarrow S\}
$$

组成，并满足下列性质。给定一族态射 $\{g_i:A_i\to C\}$，存在唯一的态射 $h:S\to C$，使得对所有 $i$ 都有 $h\circ f_i=g_i$。

<span class="original-page-anchor" id="pdf-page-75" aria-hidden="true"></span>

在积和余积中，我们把态射 $h$ 称为由态射族 $\{g_i\}$ **诱导**的态射。

**例。** 设 $\mathfrak{S}$ 是集合范畴。*那么余积存在*，即每一族对象都有余积。例如，设 $S,S'$ 是集合。设 $T$ 是与 $S'$ 具有相同基数、并与 $S$ 不相交的集合。设 $f_1:S\to S$ 是恒等映射，$f_2:S'\to T$ 是一个双射。设 $U$ 是 $S$ 和 $T$ 的并集。将 $f_1,f_2$ 看作到 $U$ 的映射，则 $(U,f_1,f_2)$ 是 $S,S'$ 的一个余积。

设 $\mathfrak{S}_0$ 是**带基点集合**范畴。它的对象是二元组 $(S,x)$，其中 $S$ 是一个集合，$x$ 是 $S$ 的一个元素。在这个范畴中，从 $(S,x)$ 到 $(S',x')$ 的一个态射，是满足 $g(x)=x'$ 的映射 $g:S\to S'$。*那么 $(S,x)$ 和 $(S',x')$ 的余积在这个范畴中存在*，并且可以如下构造。设 $T$ 是一个与 $S'$ 具有相同基数的集合，且 $T\cap S=\{x\}$。设 $U=S\cup T$，令

$$
f_1:(S,x)\longrightarrow(U,x)
$$

为在 $S$ 上诱导恒等映射的映射。令

$$
f_2:(S',x')\longrightarrow(U,x)
$$

为一个把 $x'$ 映到 $x$，并诱导从 $S'-\{x'\}$ 到 $T-\{x\}$ 的双射的映射。那么三元组 $((U,x),f_1,f_2)$ 是带基点集合范畴中 $(S,x)$ 和 $(S',x')$ 的一个余积。

对于任意集合族或带基点集合族的余积，可以作类似的构造。带基点集合范畴在同伦论中特别重要。

余积是泛对象。事实上，设 $\mathfrak{A}$ 是一个范畴，设 $\{A_i\}$ 是 $\mathfrak{A}$ 中的一族对象。现在我们定义 $\mathfrak{C}$。取态射族 $\{f_i:A_i\to B\}_{i\in I}$ 为 $\mathfrak{C}$ 的对象；给定两个这样的族，

$$
\{f_i:A_i\longrightarrow B\}\quad\text{和}\quad\{f'_i:A_i\longrightarrow B'\},
$$

我们把从第一个族到第二个族的一个态射定义为 $\mathfrak{A}$ 中的一个态射 $\varphi:B\to B'$，使得对所有 $i$ 都有 $\varphi\circ f_i=f'_i$。那么 $\{A_i\}$ 的一个余积，就是 $\mathfrak{C}$ 中的一个泛对象。

$\{A_i\}$ 的余积记为

$$
\coprod_{i\in I}A_i.
$$

两个对象 $A,B$ 的余积也记为 $A\amalg B$。

由一般的唯一性论述可知，它在相差一个唯一同构的意义下唯一确定。参见第 58 页顶部的说明。

**例。** 设 $\mathfrak{R}$ 是交换环范畴。给定两个这样的环 $A,B$，可以构造它们的张量积，并且存在自然的环同态 $A\to A\otimes B$ 和 $B\to A\otimes B$，它们满足

$$
a\longmapsto a\otimes1\quad\text{和}\quad b\longmapsto1\otimes b\quad(a\in A,\ b\in B).
$$

那么这个张量积是交换环范畴中的一个余积。

<span class="original-page-anchor" id="pdf-page-76" aria-hidden="true"></span>

### 纤维积与纤维余积
### 拉回与推出

设 $\mathfrak{C}$ 是一个范畴，$Z$ 是 $\mathfrak{C}$ 的一个对象。于是我们有一个新范畴，即 $Z$ 上对象的范畴，记为 $\mathfrak{C}_Z$。$\mathfrak{C}_Z$ 的对象是态射：

$$
f:X\longrightarrow Z\quad\text{（在 }\mathfrak{C}\text{ 中）}.
$$

$\mathfrak{C}_Z$ 中从 $f$ 到 $g:Y\to Z$ 的一个态射，就是 $\mathfrak{C}$ 中使下图交换的一个态射 $h:X\to Y$。

![交换图 1](/library/volume-86/diagrams/pdf-0076-diagram-1.png)

$\mathfrak{C}_Z$ 中的一个**积**称为 $f$ 与 $g$ 在 $\mathfrak{C}$ 中的**纤维积**，记为 $X\times_ZY$，并附带它到 $Z$ 上的 $X,Y$ 的自然态射。这些态射有时不使用任何记号，但我们把它们记为 $p_1,p_2$。

![交换图 2](/library/volume-86/diagrams/pdf-0076-diagram-2.png)

*阿贝尔群范畴中存在纤维积与纤维余积*

两个同态 $f:X\to Z$ 和 $g:Y\to Z$ 的纤维积，是 $X\times Y$ 中由满足

$$
f(x)=g(y)
$$

的所有元素对 $(x,y)$ 组成的子群。

两个同态 $f:Z\to X$ 和 $g:Z\to Y$ 的余积，是商群 $(X\oplus Y)/W$，其中 $W$ 是 $X\oplus Y$ 中由所有元素 $(f(z),-g(z))$（$z\in Z$）组成的子群。

这一简单的验证留给读者（参见习题 50–56）。

在纤维积图中，也把 $p_1$ 称为 $g$ 沿 $f$ 的**拉回**，把 $p_2$ 称为 $f$ 沿 $g$ 的**拉回**。纤维积满足下面的泛映射性质：

*给定 $\mathfrak{C}$ 中的任意对象 $T$ 以及使下图交换的态射：*

![交换图 3](/library/volume-86/diagrams/pdf-0076-diagram-3.png)

<span class="original-page-anchor" id="pdf-page-77" aria-hidden="true"></span>

*存在唯一的态射 $T\to X\times_ZY$，使下图交换：*

![交换图 1](/library/volume-86/diagrams/pdf-0077-diagram-1.png)

对偶地，我们有**以固定对象 $Z$ 为态射的出发对象的态射 $f:Z\to X$ 所组成的范畴中的余积概念。这个范畴可以记为 $\mathfrak{C}^Z$。我们把前面讨论中的箭头全部反向。** 给定这个范畴中的两个对象 $f$ 和 $g:Z\to Y$，就有它们的余积概念。它记为 $X\amalg_ZY$，并附有态射 $q_1,q_2$，如下列交换图所示：

![交换图 2](/library/volume-86/diagrams/pdf-0077-diagram-2.png)

它满足纤维积的对偶泛性质。我们称它为**纤维余积**。我们把 $q_1$ 称为 $g$ 沿 $f$ 的**推出**，把 $q_2$ 称为 $f$ 沿 $g$ 的**推出**。

**例。** 设 $\mathfrak{S}$ 是集合范畴。给定如上的两个映射 $f,g$，它们的积是由满足 $f(x)=g(y)$ 的所有元素对 $(x,y)\in X\times Y$ 组成的集合。

### 函子

设 $\mathfrak{A},\mathfrak{B}$ 是范畴。从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的一个**协变函子** $F$，是一个规则，它给 $\mathfrak{A}$ 中的每个对象 $A$ 对应 $\mathfrak{B}$ 中的一个对象 $F(A)$，并给每个态射 $f:A\to B$ 对应一个态射 $F(f):F(A)\to F(B)$，满足：

**FUN 1.** 对 $\mathfrak{A}$ 中的所有 $A$，有 $F(\operatorname{id}_A)=\operatorname{id}_{F(A)}$。

**FUN 2.** 若 $f:A\to B$ 和 $g:B\to C$ 是 $\mathfrak{A}$ 的两个态射，则有

$$
F(g\circ f)=F(g)\circ F(f).
$$

**例。** 如果给每个群 $G$ 对应它的集合（去掉群结构），并且给每个群同态对应它自身，只把它看作一个集合论意义下的映射，那么我们就得到一个从群范畴到集合范畴的函子。这样的函子称为**剥除函子**或**遗忘函子**。

我们注意到，函子把同构变成同构，因为 $f\circ g=\operatorname{id}$ 也蕴含 $F(f)\circ F(g)=\operatorname{id}$。

我们可以**使用本质上相同的定义，但把所有箭头 $F(f)$ 反向，来定义从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的反变函子**这一概念；即对于每一个态射 $f:A\to B$，反变函子对应一个态射

<span class="original-page-anchor" id="pdf-page-78" aria-hidden="true"></span>

$$
F(f):F(B)\to F(A)
$$

（方向相反），并且满足：如果

$$
f:A\to B\quad\text{和}\quad g:B\to C
$$

是 $\mathfrak{A}$ 中的态射，那么

$$
F(g\circ f)=F(f)\circ F(g).
$$

有时，协变函子中的 $F(f)$ 记作 $f_*$，反变函子中的 $F(f)$ 则记作 $f^*$。

**例。** 对应 $S\mapsto F_{\mathrm{ab}}(S)$ 是从集合范畴到阿贝尔群范畴的协变函子。

**例。** 把每个群对应到它关于有限指数子群族的完备化，这一对应是从群范畴到群范畴的函子。

**例。** 设 $p$ 为素数，$\mathfrak{C}$ 为 $p$-可除阿贝尔群的范畴。对应 $A\mapsto T_p(A)$ 是从 $\mathfrak{C}$ 到阿贝尔群（实际上是 $\mathbf{Z}_p$-模）的协变函子。

**例。** 习题 49 将给出一个遗忘函子的自同构群的例子。

**例。** 设 **Man** 为紧流形的范畴。同调是从 **Man** 到分次阿贝尔群的协变函子；上同调是到分次代数范畴（以系数环为基环）的反变函子，其中的乘法是杯积。为简单起见，如果上同调取特征为 $0$ 的域中的系数，那么上同调与积可交换。由于上同调是反变的，这意味着一个积的上同调是各因子的上同调的余积。这个余积恰好是带有分次乘法的张量积，这也给出了张量积应用的一个例子。参见 M. Greenberg 和 J. Harper，*Algebraic Topology*（《代数拓扑》，Benjamin-Addison-Wesley），1981 年，第 29 章。

**例。** 设 $\mathfrak{C}$ 为满足一些温和条件的带基点拓扑空间的范畴，即由一个空间 $X$ 和一点 $x_0$ 组成的二元组 $(X,x_0)$ 的范畴。在拓扑学中，可以把这样的空间 $(X,x_0)$ 和 $(Y,y_0)$ 在所选的点处粘合，定义它们的连通和。这一连通和是上述二元组范畴中的余积，其中的态射是满足 $f(x_0)=y_0$ 的连续映射 $f:X\to Y$。以 $\pi_1$ 表示基本群。那么 $(X,x_0)\mapsto\pi_1(X,x_0)$ 是从 $\mathfrak{C}$ 到群范畴的协变函子，并且与余积可交换。（群范畴中余积的存在性将在 §12 中证明。）

<span class="original-page-anchor" id="pdf-page-79" aria-hidden="true"></span>

**例。** 假设范畴 $\mathfrak{C}$ 中有一个态射 $f:X\to Y$。$f$ 的一个**截面**是指满足 $g\circ f=\mathrm{id}$ 的态射 $g:Y\to X$。假设存在一个从该范畴到群的协变函子 $H$，使得 $H(Y)=\{e\}$ 而 $H(X)\ne\{e\}$。那么 $f$ 没有截面。这由公式 $H(g\circ f)=\mathrm{id}$ 和 $H(f)=\text{平凡同态}$ 立即可得。在拓扑学中，可以用同调函子证明，例如，相对于包含映射 $f$，单位圆周 $X$ 不是闭单位圆盘的收缩子空间。（拓扑学家用“收缩”一词代替“截面”。）

**例。** 设 $\mathfrak{A}$ 为一个范畴，$A$ 为 $\mathfrak{A}$ 中一个固定的对象。对于 $\mathfrak{A}$ 的任意对象 $X$，令 $M_A(X)=\operatorname{Mor}(A,X)$，便得到一个协变函子

$$
M_A:\mathfrak{A}\to\mathfrak{S}.
$$

如果 $\varphi:X\to X'$ 是态射，则令

$$
M_A(\varphi):\operatorname{Mor}(A,X)\to\operatorname{Mor}(A,X')
$$

为由下列规则给出的映射：

$$
g\mapsto\varphi\circ g,
$$

其中 $g\in\operatorname{Mor}(A,X)$，即

$$
A\xrightarrow{g}X\xrightarrow{\varphi}X'.
$$

公理 **FUN 1** 和 **FUN 2** 显然成立。

类似地，对于 $\mathfrak{A}$ 的每个对象 $B$，我们有一个反变函子

$$
M^B:\mathfrak{A}\to\mathfrak{S},
$$

使得 $M^B(Y)=\operatorname{Mor}(Y,B)$。如果 $\psi:Y'\to Y$ 是态射，那么

$$
M^B(\psi):\operatorname{Mor}(Y,B)\to\operatorname{Mor}(Y',B)
$$

是由下列规则给出的映射：

$$
f\mapsto f\circ\psi,
$$

其中 $f\in\operatorname{Mor}(Y,B)$，即

$$
Y'\xrightarrow{\psi}Y\xrightarrow{f}B.
$$

上面的两个函子称为**表示函子**。

**例。** 设 $\mathfrak{A}$ 为阿贝尔群范畴。固定一个阿贝尔群 $A$。对应 $X\mapsto\operatorname{Hom}(A,X)$ 是从 $\mathfrak{A}$ 到自身的协变函子。对应 $X\mapsto\operatorname{Hom}(X,A)$ 是从 $\mathfrak{A}$ 到自身的反变函子。

**例。** 假设读者已经知道张量积。设 $A$ 为交换环，$M$ 为一个 $A$-模。对应 $X\mapsto M\otimes X$ 是从 $A$-模范畴到自身的协变函子。

注意，积与余积的定义方式与到集合范畴的表示函子相容。事实上，给定一个积 $P$，<span class="original-page-anchor" id="pdf-page-80" aria-hidden="true"></span>它是两个对象 $A$ 和 $B$ 的积，那么对于每个对象 $X$，集合 $\operatorname{Mor}(X,P)$ 是集合 $\operatorname{Mor}(X,A)$ 与 $\operatorname{Mor}(X,B)$ 在集合范畴中的积。这不过是任意范畴中积的定义性质的一种重新表述。这套体系确实行得通。

设 $\mathfrak{A},\mathfrak{B}$ 为两个范畴。从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的函子（例如单变量的协变函子）可以看作某个范畴的对象，其态射定义如下。设 $L,M$ 为两个这样的函子。**态射** $H:L\to M$（也称为**自然变换**）是一个规则，它把 $\mathfrak{A}$ 的每个对象 $X$ 对应到一个态射

$$
H_X:L(X)\to M(X),
$$

并且对于任何态射 $f:X\to Y$，下图都交换：

![自然变换的交换图：上边为 H_X，下边为 H_Y，两侧分别为 L(f)、M(f)。](/library/volume-86/diagrams/pdf-0080-natural-transformation.png)

因此，我们可以谈论函子的**同构**。如果一个函子同构于上述表示函子，就称它是**可表示的**。

正如 Grothendieck 所指出的，可以用表示函子把集合上某些结构的概念推广到任意范畴。例如，设 $\mathfrak{A}$ 为一个范畴，$G$ 为 $\mathfrak{A}$ 的一个对象。如果对于 $\mathfrak{A}$ 的每个对象 $X$，都给定集合 $\operatorname{Mor}(X,G)$ 上的一个群结构，使得对应

$$
X\mapsto\operatorname{Mor}(X,G)
$$

具有函子性（即为从 $\mathfrak{A}$ 到群范畴的函子），则称 $G$ 是 $\mathfrak{A}$ 中的一个**群对象**。有时把集合 $\operatorname{Mor}(X,G)$ 记作 $G(X)$，并把它看作 $G$ 在 $X$ 中的点的集合。关于这一术语的依据，读者可参阅第 IX 章 §2。

**例。** 设 **Var** 为复数域上射影非奇异簇的范畴。可以把 **Var** 的每个对象 $X$ 对应到各种群，例如 $\operatorname{Pic}(X)$（按有理等价得到的除子类群），这是到阿贝尔群范畴的反变函子。设 $\operatorname{Pic}_0(X)$ 为与 $0$ 代数等价的类组成的子群。那么 $\operatorname{Pic}_0$ 是可表示的。

在二十世纪五六十年代，Grothendieck 强调了表示函子的重要性，以及借助表示函子把较为标准的范畴中的概念转移到任意范畴的可能性。他本人证明了代数几何中的许多重要函子是可表示的。

<span class="original-page-anchor" id="pdf-page-81" aria-hidden="true"></span>

## §12. 自由群

现在转向群范畴中的余积。先作一个说明。设 $G=\prod G_i$ 是群的直积。

注意，每个 $G_j$ 都有一个到该直积的单射同态，把它放在第 $j$ 个分量上，即映射 $\lambda_j:G_j\to\prod_i G_i$：对于 $G_j$ 中的 $x$，当 $i\ne j$ 时，$\lambda_j(x)$ 的第 $i$ 个分量是 $G_i$ 的单位元；当 $i=j$ 时，该分量就是 $x$ 本身。这个嵌入称为**典范**嵌入。不过，这仍然没有给出该族的余积，因为这些因子彼此可交换。要得到余积，还需要多做一些工作。

设 $G$ 为群，$S$ 为 $G$ 的一个子集。回顾一下，如果 $G$ 的每个元素都能写成 $S$ 中元素及其逆元的有限乘积（空乘积始终视为 $G$ 的单位元），就说 $G$ 由 $S$ **生成**。此时 $S$ 的元素称为**生成元**。如果 $G$ 存在有限的生成元集合，就称 $G$ 是**有限生成的**。如果 $S$ 是集合，$\varphi:S\to G$ 是映射，而它的像生成 $G$，就说 $\varphi$ **生成** $G$。

设 $S$ 为集合，$f:S\to F$ 为到一个群的映射。另设 $g:S\to G$ 为一个映射。如果 $f(S)$（也可以说 $f$）生成 $F$，那么显然，至多存在一个从 $F$ 到 $G$ 的同态 $\psi$，使下图交换：

![生成性与唯一性的交换图：f 从 S 到 F，g 从 S 到 G，psi 从 F 到 G。](/library/volume-86/diagrams/pdf-0081-generation.png)

现在考虑范畴 $\mathfrak{C}$，其对象是从 $S$ 到群的映射。如果 $f:S\to G$ 和 $f':S\to G'$ 是这个范畴中的两个对象，就把从 $f$ 到 $f'$ 的态射定义为满足 $\varphi\circ f=f'$ 的同态 $\varphi:G\to G'$，即下图交换：

![从 f 到 f' 的态射交换图：phi 从 G 到 G'，并满足 phi 与 f 的复合等于 f'。](/library/volume-86/diagrams/pdf-0081-morphism.png)

所谓由 $S$ 确定的**自由群**，是指这一范畴中的泛元。

**命题 12.1。** *设 $S$ 为集合。那么存在一个由 $S$ 确定的自由群 $(F,f)$。此外，$f$ 是单射，$F$ 由 $f$ 的像生成。*

*证明。*（这个证明归功于 J. Tits。）我们先证明一个引理。

<span class="original-page-anchor" id="pdf-page-82" aria-hidden="true"></span>

**引理 12.2。** *存在一个集合 $I$ 和一个群族 $\{G_i\}_{i\in I}$，使得：如果 $g:S\to G$ 是从 $S$ 到群 $G$ 的映射，并且 $g$ 生成 $G$，那么 $G$ 同构于某个 $G_i$。*

*证明。* 这是一个简单的基数习题，我们把它做出来。如果 $S$ 有限，那么 $G$ 有限或可数无限。如果 $S$ 无限，那么 $G$ 的基数 $\leqq$ $S$ 的基数，因为 $G$ 由 $g(S)$ 中元素的有限乘积组成。取一个集合 $T$：当 $S$ 有限时，令 $T$ 可数无限；当 $S$ 无限时，令 $T$ 与 $S$ 有相同的基数。对于 $T$ 的每个非空子集 $H$，以 $\Gamma_H$ 表示 $H$ 上所有群结构组成的集合。对于每个 $\gamma\in\Gamma_H$，以 $H_\gamma$ 表示带有群结构 $\gamma$ 的集合 $H$。那么，让 $\gamma$ 遍历 $\Gamma_H$，$H$ 遍历 $T$ 的子集，所得到的族 $\{H_\gamma\}$ 就是所需的族。

回到命题的证明。对于每个 $i\in I$，令 $M_i$ 为从 $S$ 到 $G_i$ 的所有映射组成的集合。对于每个映射 $\varphi\in M_i$，令 $G_{i,\varphi}$ 为 $G_i$ 与单元素集合 $\{\varphi\}$ 的集合论乘积。因此，$G_{i,\varphi}$ 是用 $\varphi$ 作指标的、与 $G_i$ “相同”的群。令

$$
F_0=\prod_{i\in I}\prod_{\varphi\in M_i}G_{i,\varphi}
$$

为各群 $G_{i,\varphi}$ 的笛卡儿积。定义映射

$$
f_0:S\to F_0,
$$

其中到因子 $G_{i,\varphi}$ 的分量由 $\varphi$ 本身给出。我们断言，对于从 $S$ 到群 $G$ 的给定映射 $g:S\to G$，存在一个同态 $\psi_*:F_0\to G$，使通常的交换图成立：

![泛映射交换图：f_0 从 S 到 F_0，g 从 S 到 G，psi_* 从 F_0 到 G。](/library/volume-86/diagrams/pdf-0082-universal-map.png)

也就是说，$\psi_*\circ f_0=g$。为证明这一点，只需把注意力限制在 $G$ 中由 $g$ 的像生成的子群上，因此可以假设 $g$ 生成 $G$。根据引理，对于某个 $i$，存在一个同构 $\lambda:G\to G_i$，并且 $\lambda\circ g$ 是 $M_i$ 的一个元素 $\psi$。令 $\pi_{i,\psi}$ 为到 $(i,\psi)$ 因子的投影，并令 $\psi_*=\lambda^{-1}\circ\pi_{i,\psi}$。于是映射 $\psi_*$ 使下图交换。

![自由群构造的投影交换图：pi_{i,psi} 从 F_0 到 G_{i,psi}，lambda 从 G 到 G_{i,psi}，psi_* 从 F_0 到 G。](/library/volume-86/diagrams/pdf-0082-projection.png)

令 $F$ 为 $F_0$ 中由 $f_0$ 的像生成的子群，并令 $f$ 就是把 $f_0$ 视为从 $S$ 到 $F$ 的映射。令 $g_*$ 为 $\psi_*$ 在 $F$ 上的限制。这样，我们立即看出，$g_*$ 是唯一使<span class="original-page-anchor" id="pdf-page-83" aria-hidden="true"></span>我们的图交换的映射，从而 $(F,f)$ 就是所需的自由群。此外，显然 $f$ 是单射。

对于每个集合 $S$，选取一个由 $S$ 确定的自由群，记作 $(F(S),f_S)$，或简记作 $F(S)$。它由 $f_S$ 的像生成。可以把 $S$ 视为包含在 $F(S)$ 中，并把 $S$ 的元素称为 $F(S)$ 的**自由生成元**。如果 $g:S\to G$ 是映射，则以 $g_*:F(S)\to G$ 表示实现自由群 $F(S)$ 的泛性质的同态。

如果 $\lambda:S\to S'$ 是从一个集合到另一个集合的映射，就令 $F(\lambda):F(S)\to F(S')$ 为映射 $(f_{S'}\circ\lambda)_*$。

![自由群的函子性交换图：lambda 从 S 到 S'，lambda_* 等于从 F(S) 到 F(S') 的 F(lambda)。](/library/volume-86/diagrams/pdf-0083-functor.png)

于是可以把 $F$ 看作从集合范畴到群范畴的函子（函子性质的验证是显然的，留给读者）。

*如果 $\lambda$ 是满射，那么 $F(\lambda)$ 也是满射。*

证明仍留给读者。

如果两个集合 $S,S'$ 具有相同的基数，那么它们在集合范畴中同构（这里的同构就是双射！），所以 $F(S)$ 同构于 $F(S')$。如果 $S$ 有 $n$ 个元素，就称 $F(S)$ 为**以 $n$ 个生成元生成的自由群**。

设 $G$ 为群，$S$ 为与 $G$ 相同的集合（即把 $G$ 仅视为集合，不考虑群结构）。我们有恒等映射 $g:S\to G$，因而有满射同态

$$
g_*:F(S)\to G,
$$

称为**典范**同态。因此，每个群都是某个自由群的商群。

也可以用所谓的**生成元和关系**来构造群。设 $S$ 为集合，$F(S)$ 为自由群。假设 $f:S\to F(S)$ 是包含映射。设 $R$ 为 $F(S)$ 中元素组成的一个集合。$R$ 的每个元素都可以写成有限乘积

$$
\prod_{\nu=1}^{n}x_\nu,
$$

其中每个 $x_\nu$ 是 $S$ 的元素或某个 $S$ 中元素的逆元。令 $N$ 为 $F(S)$ 中包含 $R$ 的最小正规子群，即 $F(S)$ 中所有包含 $R$ 的正规子群的交。那么 $F(S)/N$ 就称为**由生成元 $S$ 和关系 $R$ 确定的群**。

<span class="original-page-anchor" id="pdf-page-84" aria-hidden="true"></span>

**例。** 容易证明，由一个生成元 $a$ 和关系 $\{a^2\}$ 确定的群的阶为 $2$。

典范同态 $\varphi:F(S)\to F(S)/N$ 对于从 $F(S)$ 到群 $G$ 的同态 $\psi$ 满足泛映射性质，其中要求对所有 $x\in R$ 都有 $\psi(x)=e$。因此，有时把群 $F(S)/N$ 称为由生成元 $S$ 和关系 $x=e$（对所有 $x\in R$）确定的群。例如，前一个例子中的群就称为由生成元 $a$ 和关系 $a^2=e$ 确定的群。

设 $G$ 为由有限个元素生成的群，并且对所有 $x\in G$ 都满足关系 $x^2=e$。$G$ 是什么样的群呢？容易证明 $G$ 是交换的。于是可以把 $G$ 看成 $\mathbf{Z}/2\mathbf{Z}$ 上的向量空间，所以在同构意义下，$G$ 由它的基数确定。

在习题 34 和 35 中，你将证明，存在满足某些关系并具有给定阶的群，从而可以完全确定由这些生成元和关系呈示的群。事先甚至不能确定一个由生成元和关系给出的群是否有限。即使它有限，事先也不知道它的阶。要证明某个给定阶的群存在，必须采用各种方法；一种常见的方法是把群表示为某个对象的自同构群，例如某个几何对象的对称群。这就是前述习题 34 和 35 中建议采用的方法。

**例。** 设 $G$ 为群。对于 $x,y\in G$，定义 $[x,y]=xyx^{-1}y^{-1}$（交换子）和 ${}^xy=xyx^{-1}$（共轭元）。那么有余循环关系

$$
[x,yz]=[x,y]\,{}^y[x,z].
$$

此外，假设 $x,y,z\in G$，并且

$$
[x,y]=y,\quad[y,z]=z,\quad[z,x]=x.
$$

那么 $x=y=z=e$。这些断言的证明留作习题，但由此可以看出，某些关系意味着：由 $x,y,z$ 生成并满足这些关系的群必然是平凡群。

接下来给出一个稍复杂的例子。假设读者知道第 XIII 章中有关域和矩阵的基本术语，但这里只把它们用于 $2\times2$ 矩阵。因此，$SL_2(F)$ 表示分量在域 $F$ 中、行列式等于 $1$ 的 $2\times2$ 矩阵所组成的群。

**例。$SL_2(F)$。** 设 $F$ 为域。对于 $b\in F$ 和 $a\in F$、$a\ne0$，令

$$
u(b)=\begin{pmatrix}1&b\\0&1\end{pmatrix},\quad
s(a)=\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix},\quad
\text{以及}\quad w=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

<span class="original-page-anchor" id="pdf-page-85" aria-hidden="true"></span>

于是立即可以验证：

**SL 0。** $s(a)=wu(a^{-1})wu(a)wu(a^{-1})$。

**SL 1。** $u$ 是加法同态。

**SL 2。** $s$ 是乘法同态。

**SL 3。** $w^2=s(-1)$。

**SL 4。** $s(a)u(b)s(a^{-1})=u(ba^2)$。

反过来，假设 $G$ 是一个任意群，其生成元为 $u(b)$（$b\in F$）和 $w$，并且对于 $a\ne0$，用 **SL 0** 定义 $s(a)$ 后，关系 **SL 1** 至 **SL 4** 都成立。那么 **SL 3** 和 **SL 4** 表明，$s(-1)$ 位于中心，且 $w^4=e$。此外，还可以验证：

**SL 5。** $ws(a)=s(a^{-1})w$。

进一步有如下定理：

*设 $G$ 为以 $u(b),w$ 为生成元、以 **SL 1** 至 **SL 4** 为关系的自由群，其中按 **SL 0** 定义 $s(a)$。那么自然同态*

$$
G\to SL_2(F)
$$

*是同构。*

上述各断言的证明可参见拙著 **SL₂(R)**，Springer Verlag，1975 年 Addison-Wesley 版的重印本，第 XI 章 §2。完成证明大约需要一页。

如果 $F=\mathbf{Q}_p$ 是 $p$-进数域，那么 Ihara [Ih 66] 证明了 $SL_2(\mathbf{Q}_p)$ 的每个离散无挠子群都是自由群。Serre 把这个定理置于群在树上作用的一般理论中 [Se 80]。

[Ih 66] Y. Ihara，On discrete subgroups of the two by two projective linear group over $p$-adic fields（关于 $p$-进域上二阶射影线性群的离散子群），*J. Math. Soc. Japan* **18**（1966），第 219–235 页。

[Se 80] J.-P. Serre，*Trees*（《树》），Springer Verlag，1980 年。

**更多例子。** 关于自由群构造的更多例子，参见习题 54 和 56。关于伽罗瓦理论中出现的自由群的例子（有时还是猜想），参见第 VI 章 §2 例 9，以及第 VI 章 §14 的结尾。

**命题 12.3。** *群范畴中存在余积。*

*证明。* 设 $\{G_i\}_{i\in I}$ 为一个群族。令 $\mathfrak{C}$ 为以下范畴，其对象是群同态族

$$
\{g_i:G_i\to G\}_{i\in I}
$$

<span class="original-page-anchor" id="pdf-page-86" aria-hidden="true"></span>

而态射则是显然的那些态射。我们必须在这个范畴中找到一个泛元。对于每个指标 $i$，当 $G_i$ 无限时，令 $S_i$ 为与 $G_i$ 相同的集合；当 $G_i$ 有限时，令 $S_i$ 为可数无限集合。令 $S$ 为与各集合 $S_i$ 的集合论不交并（即它们在集合范畴中的余积）具有相同基数的集合。令 $\Gamma$ 为 $S$ 上群结构组成的集合；对于每个 $\gamma\in\Gamma$，令 $\Phi_\gamma$ 为所有同态族

$$
\varphi=\{\varphi_i:G_i\to S_\gamma\}
$$

组成的集合。

于是每个二元组 $(S_\gamma,\varphi)$（其中 $\varphi\in\Phi_\gamma$）都是一个群，$\varphi$ 仅仅用作指标。令

$$
F_0=\prod_{\gamma\in\Gamma}\prod_{\varphi\in\Phi_\gamma}(S_\gamma,\varphi),
$$

并且对于每个 $i$，规定 $f_i$ 到各因子 $(S_\gamma,\varphi)$ 的分量与 $\varphi_i$ 相同，由此定义同态 $f_i:G_i\to F_0$。

现在设 $g=\{g_i:G_i\to G\}$ 为一个同态族。必要时把 $G$ 替换为由各 $g_i$ 的像生成的子群，就有 $\operatorname{card}(G)\leqq\operatorname{card}(S)$，因为 $G$ 的每个元素都是这些像中元素的有限乘积。对于某个 $\gamma$，把 $G$ 嵌入为乘积 $G\times S_\gamma$ 的一个因子，便可以假设 $\operatorname{card}(G)=\operatorname{card}(S)$。存在一个同态 $g_*:F_0\to G$，使得对所有 $i$，都有

$$
g_*\circ f_i=g_i.
$$

事实上，不失一般性，可以假设对于某个 $\gamma$，有 $G=S_\gamma$，并且对于某个 $\psi\in\Phi_\gamma$，有 $g=\psi$。令 $g_*$ 为 $F_0$ 到因子 $(S_\gamma,\psi)$ 的投影。

令 $F$ 为 $F_0$ 中由所有映射 $f_i$ 的像的并生成的子群。$g_*$ 在 $F$ 上的限制是唯一满足对所有 $i$ 都有 $g_*\circ f_i=g_i$ 的同态，因此我们构造出了所需的泛对象。

> **译校注。** 原书在上一句中印作 $f_i\circ g_*=g_i$，复合次序有误。因为 $f_i:G_i\to F$ 而 $g_*:F\to G$，所以应为 $g_*\circ f_i=g_i$，与前面的陈列公式一致。译文已按正确次序写出。

**例。** 设 $G_2$ 为 $2$ 阶循环群，$G_3$ 为 $3$ 阶循环群。它们的余积是什么呢？答案很简洁。可以证明，$G_2\amalg G_3$ 是由两个元素 $S,T$ 生成、满足关系 $S^2=1$、$(ST)^3=1$ 的群。把 $G_2$ 映到由 $S$ 生成的循环群，把 $G_3$ 映到由 $ST$ 生成的循环群，就把 $G_2$ 和 $G_3$ 嵌入了 $G_2\amalg G_3$。这个群可以如下表示。令

$$
G=SL_2(\mathbf{Z})/\pm1.
$$

<span class="original-page-anchor" id="pdf-page-87" aria-hidden="true"></span>

正如 §5 的一个例子中所见，群 $G$ 作用在上半平面 $\mathfrak{H}$ 上。设 $S,T$ 为以下映射：

$$
S(z)=-1/z\quad\text{和}\quad T(z)=z+1.
$$

因此，$S$ 和 $T$ 分别由矩阵

$$
S=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\quad\text{和}\quad
T=\begin{pmatrix}1&1\\0&1\end{pmatrix}
$$

表示，并满足关系 $S^2=1$、$(ST)^3=1$。读者可在 Serre 的 *Course in Arithmetic*（《算术教程》，Springer Verlag，1973 年，第 VII 章 §1）中找到 $S,T$ 的若干性质的证明，包括 $S,T$ 生成 $G$ 这一事实。在此基础上，证明 $G$ 确实是 $G_2$ 和 $G_3$ 的余积，可以作为一个习题。

注意，这些方法直接从命题 12.1 和命题 12.3 的证明中的泛定义和构造，转到相应自由群或余积的更明确的表示。这里要用到下面的命题。

**命题 12.4。** *设 $G$ 为群，$\{G_i\}_{i\in I}$ 为一个子群族。假设：*

(a) *这个族生成 $G$。*

(b) *如果*

$$
x=x_{i_1}\cdots x_{i_n},\quad\text{其中 }x_{i_\nu}\in G_{i_\nu},\ x_{i_\nu}\ne e,\ \text{且对所有 }\nu\text{ 有 }i_\nu\ne i_{\nu+1},
$$

*那么 $x\ne e$。*

*于是，把每个 $G_i$ 通过恒等映射映到自身，从而得到的由该族的余积到 $G$ 的自然同态，是一个同构。换句话说，$G$ 就是这个子群族的余积。*

*证明。* 由这个族生成 $G$ 的假设，从余积到 $G$ 的同态是满射。假设某个元素在核中。这样的元素有一个如 (b) 中那样的表示

$$
x_{i_1}\cdots x_{i_n},
$$

并且映到 $G$ 的单位元，所以所有 $x_{i_\nu}=e$，元素本身也等于 $e$。因此，从余积到 $G$ 的同态是单射，命题得证。

前面提到的习题 54 和 56 展示了命题 12.4 的一种应用。现在给出另一种方法，在两个子群的情形下展开。下一个命题的证明有这样简洁的安排，归功于 Eilenberg。

<span class="original-page-anchor" id="pdf-page-88" aria-hidden="true"></span>

**命题 12.5.** 设 $A,B$ 是两个群，其集合意义下的交为 $\{1\}$。存在一个群 $A\circ B$，以 $A,B$ 为子群，满足 $A\cap B=\{1\}$，并具有如下性质：$A\circ B$ 中每个不等于 $1$ 的元素都可以唯一地表示为乘积

$$
a_1\cdots a_n\qquad(n\geq 1,\ \text{对所有 }i\text{ 都有 }a_i\ne 1),
$$

其中 $a_i\in A$ 或 $a_i\in B$，并且若 $a_i\in A$，则 $a_{i+1}\in B$；若 $a_i\in B$，则 $a_{i+1}\in A$。

*证明。* 令 $A\circ B$ 为如下序列的集合：

$$
a=(a_1,\ldots,a_n)\qquad(n\geq 0),
$$

其中或者 $n=0$，序列为空；或者 $n\geq 1$，这时序列中的元素属于 $A$ 或 $B$，均不等于 $1$，且序列中相邻的两个元素不同时属于 $A$，也不同时属于 $B$。若 $b=(b_1,\ldots,b_m)$，则我们将乘积 $ab$ 定义为下列序列：

$$
\begin{array}{ll}
(a_1,\ldots,a_n,b_1,\ldots,b_m) & \\
& \text{若 }a_n\in A,\ b_1\in B\quad\text{或}\quad a_n\in B,\ b_1\in A,\\[4pt]
(a_1,\ldots,a_nb_1,\ldots,b_m) & \\
& \text{若 }a_n,b_1\in A\quad\text{或}\quad a_n,b_1\in B,\quad\text{且 }a_nb_1\ne 1,\\[4pt]
(a_1,\ldots,a_{n-1})(b_2,\ldots,b_m) & \text{按归纳定义},\\
& \text{若 }a_n,b_1\in A\quad\text{或}\quad a_n,b_1\in B\text{，且 }a_nb_1=1.
\end{array}
$$

$n=0$ 或 $m=0$ 的情形包含在第一种情形中，而空序列就是 $A\circ B$ 的单位元。显然，

$$
(a_1,\ldots,a_n)(a_n^{-1},\ldots,a_1^{-1})=\text{单位元},
$$

因此只需证明结合律。令 $c=(c_1,\ldots,c_r)$。

先考虑 $m=0$ 的情形，即 $b$ 为空。这时显然有 $(ab)c=a(bc)$；若 $n=0$ 或 $r=0$，也同样成立。再考虑 $m=1$ 的情形。令 $b=(x)$，其中 $x\in A$，$x\ne 1$。我们逐一验证所有可能情形中的等式 $(ab)c=a(bc)$。这些情形如下：

$$
\begin{array}{ll}
(a_1,\ldots,a_n,x,c_1,\ldots,c_r) & \text{若 }a_n\in B\quad\text{且}\quad c_1\in B,\\[4pt]
(a_1,\ldots,a_nx,c_1,\ldots,c_r) & \text{若 }a_n\in A,\ a_nx\ne 1,\ c_1\in B,\\[4pt]
(a_1,\ldots,a_n,xc_1,\ldots,c_r) & \text{若 }a_n\in B,\ c_1\in A,\ xc_1\ne 1,\\[4pt]
(a_1,\ldots,a_{n-1})(c_1,\ldots,c_r) & \text{若 }a_n=x^{-1}\quad\text{且}\quad c_1\in B,
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-89" aria-hidden="true"></span>

$$
\begin{array}{ll}
(a_1,\ldots,a_n)(c_2,\ldots,c_r) & \text{若 }a_n\in B\quad\text{且}\quad c_1=x^{-1},\\[4pt]
(a_1,\ldots,a_{n-1},a_nxc_1,c_2,\ldots,c_r) & \text{若 }a_n,c_1\in A,\ a_nxc_1\ne 1,\\[4pt]
(a_1,\ldots,a_{n-1})(c_2,\ldots,c_r) & \text{若 }a_n,c_1\in A\quad\text{且}\quad a_nxc_1=1.
\end{array}
$$

若 $m>1$，则用归纳法。将 $b$ 写成 $b'b''$，其中 $b'$ 和 $b''$ 都比 $b$ 短。于是

$$
(ab)c=(a(b'b''))c=((ab')b'')c=(ab')(b''c),
$$

$$
a(bc)=a((b'b'')c)=a(b'(b''c))=(ab')(b''c),
$$

这就证明了所需等式。

显然存在从 $A$ 和 $B$ 到 $A\circ B$ 的单射，将 $A,B$ 与它们在 $A\circ B$ 中的像等同起来，就得到了本命题的证明。

对于若干个因子，我们可以证明类似的结果。特别地，对于自由群得到如下推论。

**推论 12.6.** 设 $F(S)$ 是集合 $S$ 上的自由群，$x_1,\ldots,x_n$ 是 $S$ 中互不相同的元素。设 $\nu_1,\ldots,\nu_r$ 是不等于 $0$ 的整数，而 $i_1,\ldots,i_r$ 是整数，

$$
1\leq i_1,\ldots,i_r\leq n,
$$

且对于 $j=1,\ldots,r-1$ 有 $i_j\ne i_{j+1}$。则

$$
x_{i_1}^{\nu_1}\cdots x_{i_r}^{\nu_r}\ne 1.
$$

*证明。* 设 $G_1,\ldots,G_n$ 是分别由 $x_1,\ldots,x_n$ 生成的循环群。令 $G=G_1\circ\cdots\circ G_n$。令

$$
F(S)\longrightarrow G
$$

为将每个 $x_i$ 映到 $x_i$、将 $S$ 的所有其他元素映到 $G$ 的单位元的同态。所述结论立即成立。

**推论 12.7.** 设 $S$ 是含有 $n$ 个元素 $x_1,\ldots,x_n$ 的集合，$n\geq 1$。设 $G_1,\ldots,G_n$ 是由这些元素生成的无限循环群。则将每个 $x_i$ 映到自身的映射

$$
F(S)\longrightarrow G_1\circ\cdots\circ G_n
$$

是一个同构。

*证明。* 它显然既是满射又是单射。

**推论 12.8.** 设 $G_1,\ldots,G_n$ 是群，且当 $i\ne j$ 时有 $G_i\cap G_j=\{1\}$。由自然包含映射 $G_i\longrightarrow G_1\circ\cdots\circ G_n$ 所诱导的、从它们的余积到 $G_1\circ\cdots\circ G_n$ 的同态

$$
G_1\amalg\cdots\amalg G_n\longrightarrow G_1\circ\cdots\circ G_n
$$

是一个同构。

*证明。* 同样，它显然既是单射又是满射。

<span class="original-page-anchor" id="pdf-page-90" aria-hidden="true"></span>

## 习题

**1.** 证明每个阶 $\leq 5$ 的群都是阿贝尔群。

**2.** 证明存在两个互不同构的 $4$ 阶群，即循环群和两个 $2$ 阶循环群的积。

**3.** 设 $G$ 是一个群。$G$ 中的一个**交换子**是形如 $aba^{-1}b^{-1}$ 的元素，其中 $a,b\in G$。令 $G^c$ 为所有交换子生成的子群。$G^c$ 称为**交换子群**。证明 $G^c$ 是正规子群。证明从 $G$ 到一个阿贝尔群的任意同态都通过 $G/G^c$ 分解。

**4.** 设 $H,K$ 是有限群 $G$ 的子群，且 $K\subset N_H$。证明

$$
\#(HK)=\frac{\#(H)\#(K)}{\#(H\cap K)}.
$$

**5. Goursat 引理。** 设 $G,G'$ 是群，$H$ 是 $G\times G'$ 的子群，且两个投影 $p_1:H\to G$ 和 $p_2:H\to G'$ 都是满射。令 $N$ 为 $p_2$ 的核，$N'$ 为 $p_1$ 的核。可以将 $N$ 视为 $G$ 的一个正规子群，将 $N'$ 视为 $G'$ 的一个正规子群。证明 $H$ 在 $G/N\times G'/N'$ 中的像是某个同构

$$
G/N\approx G'/N'
$$

的图像。

**6.** 证明群 $G$ 的内自同构群是 $\operatorname{Aut}(G)$ 的正规子群。

**7.** 设 $G$ 是一个群，且 $\operatorname{Aut}(G)$ 是循环群。证明 $G$ 是阿贝尔群。

**8.** 设 $G$ 是一个群，$H,H'$ 是子群。$H,H'$ 的一个**双陪集**是指 $G$ 的形如 $HxH'$ 的子集。

(a) 证明 $G$ 是双陪集的不交并。

(b) 设 $\{c\}$ 是双陪集的一族代表元。对于每个 $a\in G$，以 $[a]H'$ 表示 $H'$ 的共轭 $aH'a^{-1}$。对于每个 $c$，有一个分解为普通陪集的式子

$$
H=\bigcup_{x_c} x_c(H\cap[c]H'),
$$

其中 $\{x_c\}$ 是 $H$ 中依赖于 $c$ 的一族元素。证明元素 $\{x_cc\}$ 构成 $H'$ 在 $G$ 中的一族左陪集代表元；也就是说，

$$
G=\bigcup_c\bigcup_{x_c}x_ccH',
$$

且此并是不交并。（双陪集直到第 XVIII 章才会再次出现。）

> **译校注：** 原书第一式的并集下标印作 $c$，应为 $x_c$；第二式外层并集的下标印作 $x_c$，应为 $c$。对每个固定的双陪集代表元 $c$，先取 $H/(H\cap[c]H')$ 的左陪集代表元 $x_c$，再遍历所有 $c$，才得到 $G$ 中的全部左陪集。译文按此更正；英文转录保留原书印式。

**9.** (a) 设 $G$ 是一个群，$H$ 是一个有限指数子群。证明存在 $G$ 的一个正规子群 $N$，它包含于 $H$ 且也具有有限指数。［*提示：* 若 $(G:H)=n$，找出一个从 $G$ 到 $S_n$ 的同态，使其核包含于 $H$。］

(b) 设 $G$ 是一个群，$H_1,H_2$ 是有限指数子群。证明 $H_1\cap H_2$ 具有有限指数。

**10.** 设 $G$ 是一个群，$H$ 是一个有限指数子群。证明 $H$ 的右陪集只有有限多个，且右陪集的数目等于左陪集的数目。

<span class="original-page-anchor" id="pdf-page-91" aria-hidden="true"></span>

**11.** 设 $G$ 是一个群，$A$ 是一个正规阿贝尔子群。证明 $G/A$ 通过共轭作用于 $A$，并由此得到从 $G/A$ 到 $\operatorname{Aut}(A)$ 的一个同态。

### 半直积

**12.** 设 $G$ 是一个群，$H,N$ 是子群，其中 $N$ 是正规子群。以 $\gamma_x$ 表示由元素 $x\in G$ 给出的共轭。

(a) 证明 $x\mapsto\gamma_x$ 诱导一个同态 $f:H\mapsto\operatorname{Aut}(N)$。

(b) 若 $H\cap N=\{e\}$，证明由 $(x,y)\mapsto xy$ 给出的映射 $H\times N\to HN$ 是一个双射，而且此映射为同构当且仅当 $f$ 是平凡的，即对于所有 $x\in H$ 都有 $f(x)=\operatorname{id}_N$。

若 $G=NH$ 且 $H\cap N=\{e\}$，则称 $G$ 为 $H$ 与 $N$ 的**半直积**。

(c) 反过来，设 $N,H$ 是群，$\psi:H\to\operatorname{Aut}(N)$ 是给定的同态。按如下方式构造一个半直积。令 $G$ 为所有有序对 $(x,h)$ 的集合，其中 $x\in N$，$h\in H$。定义合成法则

$$
(x_1,h_1)(x_2,h_2)=(x_1\psi(h_1)x_2,h_1h_2).
$$

证明这是一个群运算法则，并且在将 $N$ 与元素 $(x,1)$ 的集合、将 $H$ 与元素 $(1,h)$ 的集合等同起来后，得到 $N$ 与 $H$ 的一个半直积。

**13.** (a) 设 $H,N$ 是有限群 $G$ 的正规子群。假设 $H,N$ 的阶互素。证明对于所有 $x\in H$ 和 $y\in N$ 都有 $xy=yx$，并且 $H\times N\approx HN$。

(b) 设 $H_1,\ldots,H_r$ 是 $G$ 的正规子群，且当 $i\ne j$ 时，$H_i$ 的阶与 $H_j$ 的阶互素。证明

$$
H_1\times\cdots\times H_r\approx H_1\cdots H_r.
$$

**例。** 若一个有限群的 Sylow 子群都是正规子群，则 $G$ 是其 Sylow 子群的直积。

**14.** 设 $G$ 是有限群，$N$ 是一个正规子群，且 $N$ 与 $G/N$ 的阶互素。

(a) 设 $H$ 是 $G$ 的一个子群，其阶与 $G/N$ 的阶相同。证明 $G=HN$。

(b) 设 $g$ 是 $G$ 的一个自同构。证明 $g(N)=N$。

### 若干作用

**15.** 设有限群 $G$ 作用于有限集 $S$，且 $\#(S)\geq 2$。假设只有一个轨道。证明存在一个没有不动点的元素 $x\in G$，即对于所有 $s\in S$ 都有 $xs\ne s$。

**16.** 设 $H$ 是有限群 $G$ 的一个真子群。证明 $G$ 不是 $H$ 的所有共轭子群的并。（但参见第 XIII 章习题 23。）

**17.** 设 $X,Y$ 是有限集，$C$ 是 $X\times Y$ 的一个子集。对于 $x\in X$，令 $\varphi(x)$ 等于满足 $(x,y)\in C$ 的元素 $y\in Y$ 的数目。验证

$$
\#(C)=\sum_{x\in X}\varphi(x).
$$

<span class="original-page-anchor" id="pdf-page-92" aria-hidden="true"></span>

*注。* 上一题中的子集 $C$ 常称为一个**对应**，而 $\varphi(x)$ 是 $Y$ 中与给定元素 $x\in X$ 相对应的元素数目。

**18.** 设 $S,T$ 是有限集。证明 $\#\operatorname{Map}(S,T)=(\#T)^{\#(S)}$。

**19.** 设有限群 $G$ 作用于有限集 $S$。

(a) 对每个 $s\in S$，证明

$$
\sum_{t\in Gs}\frac{1}{\#(Gt)}=1.
$$

(b) 对每个 $x\in G$，令 $f(x)$ 为满足 $xs=s$ 的元素 $s\in S$ 的数目。证明 $G$ 在 $S$ 中的轨道数等于

$$
\frac{1}{\#(G)}\sum_{x\in G}f(x).
$$

*以下始终设 $p$ 为素数。*

**20.** 设 $P$ 是一个 $p$-群，$A$ 是一个 $p$ 阶正规子群。证明 $A$ 包含于 $P$ 的中心。

**21.** 设 $G$ 是有限群，$H$ 是子群。设 $P_H$ 是 $H$ 的一个 $p$-Sylow 子群。证明存在 $G$ 的一个 $p$-Sylow 子群 $P$，使得 $P_H=P\cap H$。

**22.** 设 $H$ 是有限群 $G$ 的一个正规子群，并假设 $\#(H)=p$。证明 $H$ 包含于 $G$ 的每一个 $p$-Sylow 子群。

**23.** 设 $P,P'$ 是有限群 $G$ 的 $p$-Sylow 子群。

(a) 若 $P'\subset N(P)$（$P$ 的正规化子），则 $P'=P$。

(b) 若 $N(P')=N(P)$，则 $P'=P$。

(c) 有 $N(N(P))=N(P)$。

### 群的具体确定

**24.** 设 $p$ 是素数。证明 $p^2$ 阶群是阿贝尔群，且在同构意义下，这样的群只有两个。

**25.** 设 $G$ 是 $p^3$ 阶群，其中 $p$ 是素数，且 $G$ 不是阿贝尔群。令 $Z$ 为其中心。设 $C$ 是一个 $p$ 阶循环群。

(a) 证明 $Z\approx C$ 且 $G/Z\approx C\times C$。

(b) $G$ 的每个 $p^2$ 阶子群都包含 $Z$，且都是正规子群。

(c) 假设对于所有 $x\in G$ 都有 $x^p=1$。证明 $G$ 包含一个正规子群 $H\approx C\times C$。

**26.** (a) 设 $G$ 是 $pq$ 阶群，其中 $p,q$ 是素数且 $p<q$。假设 $q\not\equiv 1\bmod p$。证明 $G$ 是循环群。

(b) 证明每个 $15$ 阶群都是循环群。

**27.** 证明每个阶 $<60$ 的群都是可解群。

**28.** 设 $p,q$ 是不同的素数。证明 $p^2q$ 阶群是可解群，并且它的某个 Sylow 子群是正规子群。

**29.** 设 $p,q$ 是奇素数。证明 $2pq$ 阶群是可解群。

<span class="original-page-anchor" id="pdf-page-93" aria-hidden="true"></span>

**30.** (a) 证明 $40$ 阶群的某个 Sylow 子群是正规子群。

(b) 证明 $12$ 阶群的某个 Sylow 子群是正规子群。

**31.** 在同构意义下确定所有阶 $\leq 10$ 的群。特别地，证明一个非阿贝尔的 $6$ 阶群同构于 $S_3$。

**32.** 设 $S_n$ 是 $n$ 个元素上的置换群。对于 $p=2$ 和 $p=3$，确定 $S_3,S_4,S_5$ 的 $p$-Sylow 子群。

**33.** 设 $\sigma$ 是有 $n$ 个元素的有限集 $I$ 上的一个置换。将 $e(\sigma)$ 定义为 $(-1)^m$，其中

$$
m=n-\sigma\text{ 的轨道数}.
$$

若 $I_1,\ldots,I_r$ 是 $\sigma$ 的轨道，则 $m$ 也等于下列和：

$$
m=\sum_{\nu=1}^r[\operatorname{card}(I_\nu)-1].
$$

若 $\tau$ 是一个对换，分别考虑 $i,j$ 位于 $\sigma$ 的同一轨道或不同轨道的两种情形，证明 $e(\sigma\tau)=-e(\sigma)$。在第一种情形中，$\sigma\tau$ 比 $\sigma$ 多一个轨道；在第二种情形中，则少一个轨道。特别地，一个对换的符号为 $-1$。证明 $e(\sigma)=\varepsilon(\sigma)$ 是该置换的符号。

**34.** (a) 设 $n$ 是正偶数。证明存在一个 $2n$ 阶群，由两个元素 $\sigma,\tau$ 生成，满足 $\sigma^n=e=\tau^2$ 且 $\sigma\tau=\tau\sigma^{n-1}$。（画出一个正 $n$ 边形，将顶点编号，并以此图为启发得到 $\sigma,\tau$。）这个群称为**二面体群**。

(b) 设 $n$ 是正奇数。令 $D_{4n}$ 为由矩阵

$$
\begin{pmatrix}0&-1\\1&0\end{pmatrix}\quad\text{和}\quad
\begin{pmatrix}\zeta&0\\0&\zeta^{-1}\end{pmatrix}
$$

生成的群，其中 $\zeta$ 是一个本原 $n$ 次单位根。证明 $D_{4n}$ 的阶为 $4n$，并给出上述生成元之间的交换关系。

**35.** 证明恰有两个互不同构的非阿贝尔 $8$ 阶群。（其中一个由生成元 $\sigma,\tau$ 及关系

$$
\sigma^4=1,\qquad\tau^2=1,\qquad\tau\sigma\tau=\sigma^3
$$

给出。另一个是四元数群。）

**36.** 令 $\sigma=[123\cdots n]\in S_n$。证明 $\sigma$ 的共轭类有 $(n-1)!$ 个元素。证明 $\sigma$ 的中心化子就是由 $\sigma$ 生成的循环群。

**37.** (a) 设 $\sigma=[i_1\cdots i_m]$ 是一个循环，$\gamma\in S_n$。证明 $\gamma\sigma\gamma^{-1}$ 是循环 $[\gamma(i_1)\cdots\gamma(i_m)]$。

(b) 假设 $S_n$ 中的一个置换 $\sigma$ 可以写成 $r$ 个不相交循环的乘积，令 $d_1,\ldots,d_r$ 为各循环的元素数，按递增顺序排列。设 $\tau$ 是另一个置换，它可以写成不相交循环的乘积，这些循环的基数按递增顺序为 $d'_1,\ldots,d'_s$。证明 $\sigma$ 与 $\tau$ 在 $S_n$ 中共轭，当且仅当 $r=s$ 且对于所有 $i=1,\ldots,r$ 都有 $d_i=d'_i$。

**38.** (a) 证明 $S_n$ 由对换 $[12],[13],\ldots,[1n]$ 生成。

(b) 证明 $S_n$ 由对换 $[12],[23],[34],\ldots,[n-1,n]$ 生成。

<span class="original-page-anchor" id="pdf-page-94" aria-hidden="true"></span>

(c) 证明 $S_n$ 由循环 $[12]$ 和 $[123\ldots n]$ 生成。

(d) 假设 $n$ 是素数。令 $\sigma=[123\ldots n]$，$\tau=[rs]$ 为任意一个对换。证明 $\sigma,\tau$ 生成 $S_n$。

设有限群 $G$ 作用于集合 $S$。则对于每个正整数 $n$，$G$ 都以自然的方式作用于笛卡尔积 $S^{(n)}$。若给定 $S$ 中 $n$ 个互不相同的元素 $(s_1,\ldots,s_n)$ 和另 $n$ 个互不相同的元素 $(s'_1,\ldots,s'_n)$，存在 $\sigma\in G$，使得对于所有 $i=1,\ldots,n$ 都有 $\sigma s_i=s'_i$，则称 $G$ 在 $S$ 上的作用是 **$n$ 重传递的**。

**39.** 证明交错群 $A_n$ 在 $\{1,\ldots,n\}$ 上的作用是 $(n-2)$ 重传递的。

**40.** 设 $A_n$ 是 $\{1,\ldots,n\}$ 上由偶置换构成的交错群。对于 $j=1,\ldots,n$，令 $H_j$ 为 $A_n$ 中固定 $j$ 的子群，于是 $H_j\approx A_{n-1}$，且对于 $n\geq 3$ 有 $(A_n:H_j)=n$。设 $n\geq 3$，$H$ 是 $A_n$ 中一个指数为 $n$ 的子群。

(a) 证明 $A_n$ 通过左平移作用于 $H$ 的陪集，给出 $A_n$ 与 $A_n/H$ 上的交错置换群之间的一个同构。

(b) 证明存在 $A_n$ 的一个自同构，将 $H_1$ 映到 $H$，而这样的自同构由 $S_n$ 的一个内自同构诱导，当且仅当对某个 $i$ 有 $H=H_i$。

**41.** 设 $H$ 是一个 $60$ 阶单群。

(a) 证明 $H$ 通过共轭作用于它的 Sylow 子群的集合，给出一个嵌入 $H\hookrightarrow A_6$。

(b) 利用上一题，证明 $H\approx A_5$。

(c) 证明 $A_6$ 有一个自同构，它不是由 $S_6$ 的内自同构诱导的。

### 阿贝尔群

**42.** 将 $\mathbb Z,\mathbb Q$ 视为加法群，证明 $\mathbb Q/\mathbb Z$ 是一个挠群，对于每个整数 $n\geq 1$，它有且仅有一个 $n$ 阶子群，且这个子群是循环群。

**43.** 设 $H$ 是有限阿贝尔群 $G$ 的一个子群。证明 $G$ 有一个子群同构于 $G/H$。

**44.** 设 $f:A\to A'$ 是阿贝尔群的一个同态，$B$ 是 $A$ 的一个子群。分别以 $A^f$ 和 $A_f$ 表示 $f$ 在 $A$ 上的像和核，$B^f$ 和 $B_f$ 也作类似定义。证明 $(A:B)=(A^f:B^f)(A_f:B_f)$；这里的意思是，若这三个指数中的两个是有限的，则第三个也有限，且所述等式成立。

**45.** 设 $G$ 是由元素 $\sigma$ 生成的 $n$ 阶有限循环群。假设 $G$ 作用于阿贝尔群 $A$，令 $f,g:A\to A$ 为由下式给出的 $A$ 的自同态：

$$
f(x)=\sigma x-x\quad\text{和}\quad g(x)=x+\sigma x+\cdots+\sigma^{n-1}x.
$$

若两个指数都有限，则用表达式 $q(A)=(A_f:A^g)/(A_g:A^f)$ 定义 **Herbrand 商**。现在假设 $B$ 是 $A$ 的一个子群，且 $GB\subset B$。

(a) 以自然的方式定义 $G$ 在 $A/B$ 上的作用。

(b) 证明

$$
q(A)=q(B)q(A/B),
$$

这里的意思是，若这些商中的两个是有限的，则第三个也有限，且所述等式成立。

(c) 若 $A$ 有限，证明 $q(A)=1$。

<span class="original-page-anchor" id="pdf-page-95" aria-hidden="true"></span>

（本题是第 XX 章定理 3.1 所讨论的欧拉示性数一般理论的一个特例。读过那里的内容后，本题就变得平凡了。为什么？）

### 本原群

**46.** 设 $G$ 作用于集合 $S$。设 $S=\bigcup S_i$ 是 $S$ 分解为不交子集的一个划分。若 $G$ 将每个 $S_i$ 映到某个 $S_j$ 上，从而 $G$ 诱导划分中各个集合之间的一个置换，则称该划分在 $G$ 下是**稳定的**。$S$ 有两个显然稳定的划分：仅由 $S$ 本身构成的划分，以及由各个单元素子集构成的划分。假设 $G$ 的作用是传递的，且 $S$ 有不止一个元素。证明以下两个条件等价：

**PRIM 1.** $S$ 的稳定划分只有上述两个划分。

**PRIM 2.** 若 $H$ 是 $S$ 的一个元素的稳定子群，则 $H$ 是 $G$ 的一个极大子群。

这两个条件定义了所谓的**本原群**，更准确地说，是 $G$ 在 $S$ 上的**本原作用**。

除了说群 $G$ 的作用是 $2$ 重传递的，也可以说它是**双重传递的**。

**47.** 设有限群 $G$ 传递且忠实地作用于一个至少有 $2$ 个元素的集合 $S$，$H$ 是 $S$ 中某个元素 $s$ 的稳定子群。（其他所有稳定子群都是 $H$ 的共轭。）证明下列结论：

(a) $G$ 是双重传递的，当且仅当 $H$ 在 $S$ 中 $s$ 的补集上传递地作用。

(b) $G$ 是双重传递的，当且仅当 $G=HTH$，其中 $T$ 是 $G$ 的一个不包含于 $H$ 的 $2$ 阶子群。

(c) 若 $G$ 是双重传递的，且 $(G:H)=n$，则

$$
\#(G)=d(n-1)n,
$$

其中 $d$ 是固定两个元素的子群的阶。此外，$H$ 是 $G$ 的一个极大子群，即 $G$ 是本原的。

**48.** 设群 $G$ 传递地作用于一个至少有 $2$ 个元素的集合 $S$。对于每个 $x\in G$，令 $f(x)$ 为 $S$ 中被 $x$ 固定的元素数。证明：

(a)

$$
\sum_{x\in G}f(x)=\#(G).
$$

(b) $G$ 是双重传递的，当且仅当

$$
\sum_{x\in G}f(x)^2=2\,\#(G).
$$

> **译校注：** 原文在习题 48 中未重述有限性假设。这里的两条求和恒等式按有限群 $G$ 的通常计数意义理解；由传递性，此时 $S$ 也有限。上文保留原题的假设与公式。

**49. 将群表示为自同构群。** 设 $G$ 是一个群，$\mathbf{Set}(G)$ 是 $G$-集（即带有 $G$ 作用的集合）组成的范畴。设 $F:\mathbf{Set}(G)\to\mathbf{Set}$ 是遗忘函子，它将每个 $G$-集对应到该集合本身。证明 $\operatorname{Aut}(F)$ 自然同构于 $G$。

<span class="original-page-anchor" id="pdf-page-96" aria-hidden="true"></span>

### 纤维积与纤维余积
### 拉回与推出

**50.** (a) 证明阿贝尔群范畴中存在纤维积。具体地，若 $X,Y$ 是阿贝尔群，且有同态 $f:X\to Z$ 和 $g:Y\to Z$，证明 $X\times_Z Y$ 是所有满足 $x\in X$、$y\in Y$ 且 $f(x)=g(y)$ 的有序对 $(x,y)$ 的集合。映射 $p_1,p_2$ 分别是到第一和第二个因子的投影。

(b) 证明满同态的拉回仍是满射。

**51.** (a) 证明集合范畴中存在纤维积。

(b) 在任意范畴 $\mathcal C$ 中，考虑 $Z$ 上的对象所构成的范畴 $\mathcal C_Z$。设 $h:T\to Z$ 是这个范畴中的一个固定对象。令 $F$ 为满足下式的函子：

$$
F(X)=\operatorname{Mor}_Z(T,X),
$$

其中 $X$ 是 $Z$ 上的一个对象，$\operatorname{Mor}_Z$ 表示 $Z$ 上的态射。证明 $F$ 将 $Z$ 上的纤维积变为集合范畴中的积。（事实上，一旦理解了这些定义，这个结论就是同义反复。）

**52.** (a) 证明阿贝尔群范畴中存在推出（即纤维余积）。在这种情况下，上述两个同态 $f,g$ 的纤维余积记为 $X\oplus_Z Y$。证明它是商群

$$
X\oplus_Z Y=(X\oplus Y)/W,
$$

其中 $W$ 是由所有元素 $(f(z),-g(z))$（$z\in Z$）组成的子群。

> **译校注：** 习题 52 的推出使用映射 $f:Z\to X$ 和 $g:Z\to Y$，与习题 50 中纤维积的箭头方向相反。此处对原文“上述”的指代作说明，公式保留原式。

(b) 证明单同态的推出仍是单射。

**注。** 学过环上的模之后，应当注意到上述两道习题既适用于阿贝尔群，也适用于模。

**53.** 设 $H,G,G'$ 是群，且

$$
f:H\to G,\qquad g:H\to G'
$$

是两个同态。定义这两个同态在 $H$ 上的余积的概念，并证明它存在。

**54.** （Tits）。设 $G$ 是一个群，$\{G_i\}_{i\in I}$ 是生成 $G$ 的一族子群。假设 $G$ 作用于集合 $S$。对每个 $i\in I$，设给定 $S$ 的一个子集 $S_i$，并取 $S-\bigcup_i S_i$ 中的一点 $s$。假设对于每个 $g\in G_i-\{e\}$，有

$$
\text{对所有 }j\ne i\text{，有 }gS_j\subset S_i,\quad\text{且对所有 }i\text{，有 }g(s)\in S_i.
$$

证明 $G$ 是族 $\{G_i\}_{i\in I}$ 的余积。（*提示：* 假设一个乘积 $g_1\cdots g_m=\operatorname{id}$ 在 $S$ 上成立。将此乘积作用于 $s$，并使用命题 12.4。）

**55.** 设 $M\in\operatorname{GL}_2(\mathbb C)$（行列式非零的 $2\times2$ 复矩阵）。令

$$
M=\begin{pmatrix}a&b\\c&d\end{pmatrix},\quad\text{并对 }z\in\mathbb C\text{ 令 }M(z)=\frac{az+b}{cz+d}.
$$

若 $z=-d/c$（$c\ne 0$），则令 $M(z)=\infty$。于是可以验证（在复分析课程中，应当已经见过类似的内容），$\operatorname{GL}_2(\mathbb C)$ 由此作用于 $\mathbb C\cup\{\infty\}$。设 $\lambda,\lambda'$ 是将 $M$ 视为 $\mathbb C^2$ 上的线性映射时的特征值。令 $W,W'$ 为相应的特征向量，

$$
W={}^t(w_1,w_2)\quad\text{和}\quad W'={}^t(w'_1,w'_2).
$$

<span class="original-page-anchor" id="pdf-page-97" aria-hidden="true"></span>

所谓 $M$ 在 $\mathbb C$ 上的一个**不动点**，是指满足 $M(z)=z$ 的复数 $z$。*假设 $M$ 有两个互不相同且不等于 $\infty$ 的不动点。*

(a) 证明不动点不可能超过两个，且这两个不动点是 $w=w_1/w_2$ 和 $w'=w'_1/w'_2$。事实上，可以取

$$
W={}^t(w,1),\quad W'={}^t(w',1).
$$

> **译校注：** 习题 55(a) 还需要排除 $M$ 为非零标量矩阵的情形。这样的矩阵所给出的 Möbius 变换是恒等变换，虽然满足“有两个不同的有限不动点”的题设，却有无穷多个不动点。原书未明示这一排除条件；(b) 中的严格不等式已经排除了标量矩阵。

(b) 假设 $|\lambda|<|\lambda'|$。给定 $z\ne w$，证明

$$
\lim_{k\to\infty}M^k(z)=w'.
$$

［*提示：* 令 $S=(W,W')$，并考虑 $S^{-1}M^kS(z)=\alpha^kz$，其中 $\alpha=\lambda/\lambda'$。］

**56.** （Tits）设 $M_1,\ldots,M_r\in\operatorname{GL}_2(\mathbb C)$ 是有限个矩阵。设 $\lambda_i,\lambda'_i$ 为 $M_i$ 的特征值。假设每个 $M_i$ 都有两个互不相同的复不动点，且 $|\lambda_i|<|\lambda'_i|$。再假设 $M_1,\ldots,M_r$ 的所有不动点彼此互不相同。证明存在一个正整数 $k$，使得 $M_1^k,\ldots,M_r^k$ 是 $\operatorname{GL}_2(\mathbb C)$ 的一个自由子群的自由生成元。［*提示：* 设 $w_i,w'_i$ 为 $M_i$ 的不动点。令 $U_i$ 为以 $w_i$ 为中心的小圆盘，$U'_i$ 为以 $w'_i$ 为中心的小圆盘。令 $S_i=U_i\cup U'_i$。取一个不属于任何 $S_i$ 的复数 $s$。令 $G_i=\langle M_i^k\rangle$。证明当 $k$ 足够大时，习题 54 的条件成立。］

![点 s 位于分别以 w_i 和 w'_i 为中心的圆盘 U_i 与 U'_i 之外。](/library/volume-86/diagrams/pdf-0097-tits-discs.png)

**57.** 设群 $G$ 作用于集合 $X$，$Y$ 是 $X$ 的一个子集。令 $G_Y$ 为 $G$ 中所有满足 $gY\cap Y$ 非空的元素 $g$ 构成的子集。令 $\overline G_Y$ 为 $G_Y$ 生成的 $G$ 的子群。则 $\overline G_YY$ 与 $(G-\overline G_Y)Y$ 不相交。［*提示：* 假设存在 $g_1\in\overline G_Y$ 和 $g_2\in G$，但 $g_2\notin\overline G_Y$，以及元素 $y_1,y_2\in Y$，使得 $g_1y_1=g_2y_2$。于是 $g_2^{-1}g_1y_1=y_2$，故 $g_2^{-1}g_1\in G_Y$，从而 $g_2\in\overline G_Y$，与假设矛盾。］

> **译校注：** 原书提示中的等式印作 $g_2y_1=g_2y_2$；左端应为 $g_1y_1$，即 $g_1y_1=g_2y_2$，这样才能表示两集合相交，并推出下一行的等式。译文据此更正；英文转录保留原书印式。

**应用。** 假设 $X=GY$，但除非上述两个集合之一为空，否则 $X$ 不能表示为上述形式的不交并。于是得出 $G-\overline G_Y$ 为空，因此 $G_Y$ 生成 $G$。

**例 1。** 假设 $X$ 是连通拓扑空间，$Y$ 是开集，$G$ 的作用是连续的。那么 $Y$ 的所有平移像都是开集，故 $G$ 由 $G_Y$ 生成。

**例 2。** 假设 $G$ 是一个离散群，在 $X$ 上连续且离散地作用。再假设 $X$ 连通，$Y$ 闭，且 $Y$ 在 $G$ 的元素作用下的平移像的任意并都是闭集。于是仍有 $G-\overline G_Y$ 为空，且 $G_Y$ 生成 $G$。
