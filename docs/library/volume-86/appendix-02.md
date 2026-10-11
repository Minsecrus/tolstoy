---
title: "附录二：集合论基础"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"附录一：e 与 π 的超越性","link":"/library/volume-86/appendix-01"}
next: {"text":"参考文献","link":"/library/volume-86/bibliography"}
---

# 附录二：集合论基础

<span class="original-page-anchor" id="pdf-page-882" aria-hidden="true"></span>

## §1. 可列集

设 $n$ 是一个正整数。令 $J_n$ 为由所有整数 $k$，$1\leqq k\leqq n$，组成的集合。若 $S$ 是一个集合，当 $S$ 与 $J_n$ 之间存在双射时，就称 $S$ 有 $n$ 个元素。这样的双射将上述每个整数 $k$ 对应到 $S$ 的一个元素，比如 $k\mapsto a_k$。因此，可以用 $J_n$ 来“数” $S$。关于正整数的基本事实，我们所假定的一部分内容是：若 $S$ 有 $n$ 个元素，则整数 $n$ 由 $S$ 唯一确定。

也约定空集有 $0$ 个元素。

若集合 $S$ 与正整数集 $\mathbf Z^+$ 之间存在双射，则称 $S$ 是**可列的**。这时，称这样的双射**列举**集合 $S$。它是一个映射

$$
n\mapsto a_n,
$$

将每个正整数 $n$ 对应到 $S$ 的一个元素，并且该映射既是单射又是满射。

若 $D$ 是可列集，且 $f:S\longrightarrow D$ 是某个集合 $S$ 与 $D$ 之间的双射，则 $S$ 也可列。事实上，存在双射 $g:D\longrightarrow\mathbf Z^+$，因此 $g\circ f$ 是 $S$ 与 $\mathbf Z^+$ 之间的双射。

设 $T$ 是一个集合。$T$ 中元素的一个**序列**，就是 $\mathbf Z^+$ 到 $T$ 的一个映射。若此映射由对应 $n\mapsto x_n$ 给出，也将序列写成 $\{x_n\}_{n\geqq1}$ 或 $\{x_1,x_2,\ldots\}$。为简单起见，也用 $\{x_n\}$ 表示该序列。这样，将序列看作指定了 $T$ 中的第一、第二、$\ldots$、第 $n$ 个元素。对序列和集合使用相同的花括号，不过上下文总能使我们的意思明确。

<span class="original-page-anchor" id="pdf-page-883" aria-hidden="true"></span>

**例。** 若令 $x_n=2n$，$n=1,2,\ldots$，则可将正偶数看作序列 $\{x_n\}$。若令 $y_n=2n-1$，$n=1,2,\ldots$，则也可将正奇数看作序列 $\{y_n\}$。在这两种情形下，序列都给出了相应集合的一种列举。

也用*序列*一词表示自然数集到一个集合的映射，从而允许序列从 $0$ 开始而不是从 $1$ 开始。若需要说明序列是从第 $0$ 项还是从第一项开始，就按相应的情形写成

$$
\{x_n\}_{n\geqq0}\quad\text{或}\quad\{x_n\}_{n\geqq1}.
$$

然而，除非另有说明，总是假定序列从第一项开始。注意，由序列 $\{x_n\}_{n\geqq0}$，可以令 $y_n=x_{n-1}$，$n\geqq1$，从而定义一个新序列。于是 $y_1=x_0,y_2=x_1,\ldots$。因此，这两种序列之间没有本质区别。

给定序列 $\{x_n\}$，称 $x_n$ 为序列的第 $n$ 项。一个序列完全可能各项都相等。例如，若对于所有 $n\geqq1$，令 $x_n=1$，则得到序列 $\{1,1,1,\ldots\}$。因此，集合 $T$ 中元素的一个序列与 $T$ 的一个子集是有区别的。在刚才的例子中，序列所有项组成的集合只有一个元素，即数 $1$。

设 $\{x_1,x_2,\ldots\}$ 是集合 $S$ 中的一个序列。所谓**子序列**，是指满足 $n_1<n_2<\cdots$ 的序列 $\{x_{n_1},x_{n_2},\ldots\}$。例如，若 $\{x_n\}$ 是正整数序列，即 $x_n=n$，则正偶数序列 $\{x_{2n}\}$ 是一个子序列。

集合 $S$ 的一种列举，当然是 $S$ 中的一个序列。

若集合为空，或者集合有 $n$ 个元素，其中 $n$ 是某个正整数，则称该集合是**有限的**。若一个集合不是有限的，则称它是**无限的**。

有时，将 $J_n$ 到集合 $T$ 的映射称为 $T$ 中的一个**有限序列**。有限序列通常写成

$$
\{x_1,\ldots,x_n\}\quad\text{或}\quad\{x_i\}_{i=1,\ldots,n}.
$$

当需要明确区分有限序列与 $\mathbf Z^+$ 到 $T$ 的映射时，就将后者称为无限序列。除非另有说明，我们用序列一词表示无限序列。

**命题 1.1。** *设 $D$ 是 $\mathbf Z^+$ 的一个无限子集。则 $D$ 可列，并且事实上，$D$ 有唯一的一种列举，比如 $\{k_1,k_2,\ldots\}$，满足*

$$
k_1<k_2<\cdots<k_n<k_{n+1}<\cdots.
$$

*证明。* 令 $k_1$ 为 $D$ 的最小元素。归纳假设已定义 $k_1<\cdots<k_n$，使得 $D$ 中任何不等于 $k_1,\ldots,k_n$ 的元素 $k$ 都 $>k_n$。将 $k_{n+1}$ 定义为 $D$ 中 $>k_n$ 的最小元素。于是映射 $n\mapsto k_n$ 就是所要求的 $D$ 的列举。

<span class="original-page-anchor" id="pdf-page-884" aria-hidden="true"></span>

**推论 1.2。** *设 $S$ 是一个可列集，$D$ 是 $S$ 的一个无限子集。则 $D$ 可列。*

*证明。* 给定 $S$ 的一种列举，在此列举中，子集 $D$ 对应于 $\mathbf Z^+$ 的一个子集。由命题 1.1，可知能够列举 $D$。

**命题 1.3。** *每个无限集都包含一个可列子集。*

*证明。* 设 $S$ 是一个无限集。对于 $S$ 的每个非空子集 $T$，在 $T$ 中选定一个元素 $a_T$。然后用归纳法进行。令 $x_1$ 为所选的元素 $a_S$。假设已选出 $x_1,\ldots,x_n$，具有如下性质：对于每个 $k=2,\ldots,n$，元素 $x_k$ 是在 $\{x_1,\ldots,x_{k-1}\}$ 的补集中选定的元素。令 $x_{n+1}$ 为在集合 $\{x_1,\ldots,x_n\}$ 的补集中选定的元素。这样，通过归纳，对所有正整数 $n$ 得到对应 $n\mapsto x_n$；由于对于所有 $k<n$ 都有 $x_n\ne x_k$，此对应是单射，即给出了 $S$ 的一个子集的一种列举。

**命题 1.4。** *设 $D$ 是一个可列集，$f:D\longrightarrow S$ 是一个满射。则 $S$ 可列或有限。*

*证明。* 由于 $f$ 是满射，对于每个 $y\in S$，存在一个元素 $x_y\in D$，使得 $f(x_y)=y$。对应 $y\mapsto x_y$ 是 $S$ 到 $D$ 的单射，因为若

$$
y,z\in S\quad\text{且}\quad x_y=x_z,
$$

则

$$
y=f(x_y)=f(x_z)=z.
$$

令 $g(y)=x_y$。$g$ 的像是 $D$ 的一个子集，而 $D$ 可列。由于 $g$ 是 $S$ 与其像之间的双射，可知 $S$ 可列或有限。

**命题 1.5。** *设 $D$ 是一个可列集。则 $D\times D$（所有满足 $x,y\in D$ 的有序对 $(x,y)$ 的集合）可列。*

*证明。* $D\times D$ 与 $\mathbf Z^+\times\mathbf Z^+$ 之间有双射，因此只需证明 $\mathbf Z^+\times\mathbf Z^+$ 可列。考虑由

$$
(m,n)\mapsto2^n3^m
$$

给出的映射 $\mathbf Z^+\times\mathbf Z^+\longrightarrow\mathbf Z^+$。

它是单射，由命题 1.1，结论成立。

**命题 1.6。** *设 $\{D_1,D_2,\ldots\}$ 是一个可列集序列。设 $S$ 是所有集合 $D_i$ $(i=1,2,\ldots)$ 的并。则 $S$ 可列。*

<span class="original-page-anchor" id="pdf-page-885" aria-hidden="true"></span>

*证明。* 对每个 $i=1,2,\ldots$，列举 $D_i$ 的元素，如下列记号所示：

$$
\begin{array}{rl}
D_1:&\{x_{11},x_{12},x_{13},\ldots\}\\
D_2:&\{x_{21},x_{22},x_{23},\ldots\}\\
&\cdots\\
D_i:&\{x_{i1},x_{i2},x_{i3},\ldots\}\\
&\cdots
\end{array}
$$

于是，由

$$
f(i,j)=x_{ij}
$$

给出的映射 $f:\mathbf Z^+\times\mathbf Z^+\longrightarrow D$ 是 $\mathbf Z^+\times\mathbf Z^+$ 到 $S$ 的满射。由命题 1.4，可知 $S$ 可列。

> **译校注。** 原文在此将目标集印作 $D$，而命题 1.6 及紧接着的句子中，被列举的并集是 $S$。因此，由 $f(i,j)=x_{ij}$ 定义的映射，其目标集应为 $S$。上文保留原印字母。

**推论 1.7。** *设 $F$ 是一个非空有限集，$D$ 是一个可列集。则 $F\times D$ 可列。若 $S_1,S_2,\ldots$ 是一个集合序列，其中每个集合都有限或可列，则并集 $S_1\cup S_2\cup\cdots$ 可列或有限。*

*证明。* 存在 $F$ 到 $\mathbf Z^+$ 的单射，以及 $D$ 与 $\mathbf Z^+$ 之间的双射。因此，存在 $F\times\mathbf Z^+$ 到 $\mathbf Z^+\times\mathbf Z^+$ 的单射；可以应用推论 1.2 和命题 1.6 证明第一个断言。也可以定义 $\mathbf Z^+\times\mathbf Z^+$ 到 $F\times D$ 的满射。（参见习题 1 和 4。）至于第二个断言，每个有限集都包含于某个可列集中，因此第二个断言由命题 1.1 和 1.6 得到。

为方便起见，若一个集合有限或可列，则称其**可数**。

## §2. 佐恩引理

为了有效地同时处理无穷多个集合，需要一个特殊的性质。为陈述它，还需要一些术语。

设 $S$ 是一个集合。$S$ 上的一个**序**（也称偏序）是 $S$ 中某些元素对之间的一种关系，记为 $x\leqq y$，具有下列性质。

**ORD 1。** *有 $x\leqq x$。*

**ORD 2。** *若 $x\leqq y$ 且 $y\leqq z$，则 $x\leqq z$。*

**ORD 3。** *若 $x\leqq y$ 且 $y\leqq x$，则 $x=y$。*

<span class="original-page-anchor" id="pdf-page-886" aria-hidden="true"></span>

有时用 $y\geqq x$ 表示 $x\leqq y$。注意，我们不要求对于 $S$ 的每对元素 $(x,y)$，都有关系 $x\leqq y$ 或 $y\leqq x$。某些元素对可能不可比较。若这个序还满足此附加性质，则称其为**全序**。

**例 1。** 设 $G$ 是一个群。令 $S$ 为子群的集合。若 $H,H'$ 是 $G$ 的子群，当 $H$ 是 $H'$ 的子群时，定义

$$
H\leqq H'.
$$

立即可以验证，此关系定义了 $S$ 上的一个序。给定 $G$ 的两个子群 $H,H'$，未必有 $H\leqq H'$ 或 $H'\leqq H$。

**例 2。** 设 $R$ 是一个环，$S$ 是 $R$ 的左理想的集合。按照与上面类似的方式定义 $S$ 中的序，即若 $L,L'$ 是 $R$ 的左理想，当 $L\subset L'$ 时，定义

$$
L\leqq L'.
$$

**例 3。** 设 $X$ 是一个集合，$S$ 是 $X$ 的子集的集合。若 $Y,Z$ 是 $X$ 的子集，当 $Y$ 是 $Z$ 的子集时，定义 $Y\leqq Z$。这定义了 $S$ 上的一个序。

在所有这些例子中，此序关系称为包含关系。

在一个有序集中，若 $x\leqq y$ 且 $x\ne y$，则写作 $x<y$。

设 $A$ 是一个有序集，$B$ 是一个子集。对于 $x,y\in B$，规定 $x\leqq y$ 成立当且仅当在 $A$ 中有 $x\leqq y$，便在 $B$ 上定义了一个序。称 $R_0$ 是由 $R$ **诱导**的 $B$ 上的序，或称它是 $A$ 上偏序在 $B$ 上的**限制**。

设 $S$ 是一个有序集。所谓 $S$ 的一个**最小**元素，是指元素 $a\in S$，使得对于所有 $x\in S$，都有 $a\leqq x$。类似地，所谓**最大元素**，是指元素 $b$，使得对于所有 $x\in S$，都有 $x\leqq b$。

所谓 $S$ 的一个**极大元素** $m$，是指一个元素，满足：若 $x\in S$ 且 $x\geqq m$，则 $x=m$。注意，极大元素未必是最大元素。$S$ 中可能有许多个极大元素，而若最大元素存在，则它是唯一的（证明？）。

设 $S$ 是一个有序集。若给定 $x,y\in S$，必有 $x\leqq y$ 或 $y\leqq x$，则称 $S$ 是**全序的**。

**例 4。** 整数集 $\mathbf Z$ 在通常的序下是全序的。实数集也是如此。

设 $S$ 是一个有序集，$T$ 是一个子集。$T$ 的一个**上界**（在 $S$ 中），是指元素 $b\in S$，使得对于所有 $x\in T$，都有 $x\leqq b$。$T$ 在 $S$ 中的一个**最小上界**，是指一个上界 $b$，使得若 $c$ 是另一个上界，则 $b\leqq c$。我们将称<span class="original-page-anchor" id="pdf-page-887" aria-hidden="true"></span>若每个非空全序子集都有一个上界，则称 $S$ 是**归纳有序的**。

若每个非空全序子集都有一个最小上界，则称 $S$ 是**严格**归纳有序的。

在例 1、2、3 的每一种情形下，相应集合都严格归纳有序。为证明这一点，考察例 1。设 $T$ 是 $G$ 的子群集中的一个非空全序子集。这意味着，若 $H,H'\in T$，则 $H\subset H'$ 或 $H'\subset H$。设 $U$ 是 $T$ 中所有集合的并。则：

**1.** $U$ 是一个子群。*证明：* 若 $x,y\in U$，则存在子群 $H,H'\in T$，使得 $x\in H$ 且 $y\in H'$。若比如 $H\subset H'$，则 $x,y$ 都在 $H'$ 中，因此 $xy\in H'$。故 $xy\in U$。又有 $x^{-1}\in H'$，因此 $x^{-1}\in U$。故 $U$ 是一个子群。

**2.** $U$ 是 $T$ 中每个元素的上界。*证明：* 每个 $H\in T$ 都包含于 $U$ 中，因此对于所有 $H\in T$，有 $H\leqq U$。

**3.** $U$ 是 $T$ 的一个最小上界。*证明：* $G$ 的任何包含所有子群 $H\in T$ 的子群，必然包含它们的并 $U$。

证明例 2、3 中的集合严格归纳有序，方法完全类似。

现在可以陈述本节开始时提到的性质。

**佐恩引理。** *设 $S$ 是一个非空的归纳有序集。则 $S$ 中存在一个极大元素。*

作为佐恩引理的一个应用，现在证明第 1 章 §7 和第 XIV 章 §2 中一个定理的无限版本，即：

*设 $R$ 是一个主理想整环，$E$ 是 $R$ 上的一个自由模。设 $F$ 是一个子模。则 $F$ 是自由的。事实上，若 $\{v_i\}_{i\in I}$ 是 $E$ 的一组基，且 $F\ne\{0\}$，则 $F$ 有一组以 $I$ 的一个子集为指标集的基。*

*证明。* 对 $I$ 的每个子集 $J$，令 $E_J$ 为由所有 $v_j,j\in J$ 生成的 $E$ 的自由子模，并令 $F_J=E_J\cap F$。令 $S$ 为所有对 $(F_J,w)$ 的集合，其中 $J$ 是 $I$ 的一个子集，而 $w:J'\longrightarrow F_J$ 是 $F_J$ 的一组基，以 $J$ 的一个子集 $J'$ 为指标集。对于 $j\in J'$，用 $w_j$ 代替 $w(j)$。若 $(F_J,w)$ 和 $(F_K,u)$ 是这样的两个对，当 $J\subset K$、$J'\subset K'$，且 $u$ 在 $J'$ 上的限制等于 $w$ 时，定义 $(F_J,w)\leqq(F_K,u)$。（换言之，$F_K$ 的基 $u$ 是 $F_J$ 的基 $w$ 的扩张。）这定义了 $S$ 上的一个序，而且立即可以验证，$S$ 实际上是归纳有序的，并且非空（例如由此结果的有限情形可知）。因此可以应用佐恩引理。设 $(F_J,w)$ 是一个极大元素。我们断言 $J=I$（这将证明结论）。假设 $J\ne I$，并取 $k\in I$ 但 $k\notin J$。令 $K=J\cup\{k\}$。若

$$
E_{J\cup\{k\}}\cap F=F_J,
$$

<span class="original-page-anchor" id="pdf-page-888" aria-hidden="true"></span>

则 $(F_K,w)$ 是一个比 $(F_J,w)$ 更大的对，与极大性假设矛盾。否则，$F_K$ 中存在可以写成如下形式的元素：

$$
cv_k+y,
$$

其中某个 $y\in E_J$，且 $c\in R,c\ne0$。所有满足“存在 $y\in E_J$ 使得 $cv_k+y\in F$”的元素 $c\in R$ 组成一个理想。设 $a$ 为此理想的一个生成元，并设

$$
w_k=av_k+y
$$

为 $F$ 的一个元素，其中 $y\in E_J$。若 $z\in F_K$，则存在 $b\in R$，使得 $z-bw_k\in E_J$。但 $z-bw_k\in F$，故 $z-bw_k\in F_J$。立即可知，由 $w_j$ $(j\in J)$ 和 $w_k$ 组成的族是 $F_K$ 的一组基，从而再次与极大性矛盾。这证明了所要的结论。

> **译校注。** 此处原印的基指标为 $j\in J$。前面的定义给出已有基为 $w:J'\longrightarrow F_J$，因此此族应使用 $j\in J'$；新增基元素的指标为 $k\notin J$。上文保留原式。

可以直接将佐恩引理作为集合论的一个公理。然而，从直觉上说，它作为公理并非完全令人满意，因为它的陈述过于复杂，不容易直观地理解其中所断言的极大元素的存在。我们将展示如何从集合的其他性质证明佐恩引理，而这些性质在直觉上是人人都会立即认可的。

从现在起，直到定理 2.1 的证明结束，令 $A$ 为一个非空的偏序集，并且严格归纳有序。回忆，**严格归纳有序**意味着每个非空全序子集都有最小上界。假设给定映射 $f:A\longrightarrow A$，使得对于所有 $x\in A$，都有 $x\leqq f(x)$。可以称这样的映射为**递增**映射。

设 $a\in A$。设 $B$ 是 $A$ 的一个子集。若满足下列条件，则称 $B$ 是**容许的**：

**1.** $B$ 包含 $a$。

**2.** 有 $f(B)\subset B$。

**3.** 只要 $T$ 是 $B$ 的一个非空全序子集，$T$ 在 $A$ 中的最小上界就属于 $B$。

于是，$B$ 在 $A$ 的诱导序下也严格归纳有序。我们将证明：

**定理 2.1。** （Bourbaki）*设 $A$ 是一个非空的偏序集，并且严格归纳有序。设 $f:A\longrightarrow A$ 是一个递增映射。则存在元素 $x_0\in A$，使得 $f(x_0)=x_0$。*

*证明。* 假设 $A$ 是全序的。由假设，它有一个最小上界 $b\in A$，于是

$$
b\leqq f(b)\leqq b,
$$

<span class="original-page-anchor" id="pdf-page-889" aria-hidden="true"></span>

因此，在这种情形下，定理显然成立。整个问题在于将定理归结到此情形。换言之，需要找到 $A$ 的一个全序容许子集。

若从 $A$ 中去掉所有不满足 $x\geqq a$ 的元素 $x\in A$，则剩下的部分显然是一个容许子集。因此，不失一般性，可以假设 $A$ 有一个最小元素 $a$，即对于所有 $x\in A$，都有 $a\leqq x$。

令 $M$ 为 $A$ 的所有容许子集的交。注意，$A$ 自身是一个容许子集，并且 $A$ 的所有容许子集都包含 $a$，因此 $M$ 非空。此外，$M$ 自身也是 $A$ 的一个容许子集。为说明这一点，设 $x\in M$。于是 $x$ 属于每个容许子集，因此 $f(x)$ 也属于每个容许子集，故 $f(x)\in M$。于是 $f(M)\subset M$。若 $T$ 是 $M$ 的一个非空全序子集，$b$ 是 $T$ 在 $A$ 中的最小上界，则 $b$ 属于 $A$ 的每个容许子集，因此属于 $M$。可知 $M$ 是 $A$ 的最小容许子集，并且 $A$ 的任何包含于 $M$ 中的容许子集都等于 $M$。

我们将证明 $M$ 全序，从而证明定理 2.1。

［先作一些不属于证明的说明，但它们有助于理解下面的引理。由于 $a\in M$，可知 $f(a)\in M$、$f\circ f(a)\in M$，一般地，$f^n(a)\in M$。此外，

$$
a\leqq f(a)\leqq f^2(a)\leqq\cdots.
$$

若某处出现等号，就已经完成证明，因此可以假设这些不等式成立。令 $D_0$ 为全序集 $\{f^n(a)\}_{n\geqq0}$。于是 $D_0$ 的形状如下：

$$
a<f(a)<f^2(a)<\cdots<f^n(a)<\cdots.
$$

令 $a_1$ 为 $D_0$ 的最小上界。然后可以以相同方式构造

$$
a_1<f(a_1)<f^2(a_1)<\cdots,
$$

得到 $D_1$；继续此过程，得到

$$
D_1,D_2,\ldots.
$$

显然，$D_1,D_2,\ldots$ 都包含于 $M$ 中。若能精确地表达我们可以建立由这样的可列集组成的一个永不终止的串这一事实，就能得到所要的结论。问题在于，我们现在正试图证明佐恩引理，而它恰好是保证这样的串存在的自然工具。然而，给定这样的串，可以观察到其元素有两个性质：若 $c$ 是此串的一个元素且 $x<c$，则 $f(x)\leqq c$。此外，$c$ 与 $f(c)$ 之间没有元素，即若 $x$ 是此串的一个元素，则 $x\leqq c$ 或 $f(c)\leqq x$。现在将证明两个引理，说明 $M$ 的元素具有这些性质。］

<span class="original-page-anchor" id="pdf-page-890" aria-hidden="true"></span>

设 $c\in M$。若只要 $x\in M$ 且 $x<c$，就有 $f(x)\leqq c$，则称 $c$ 是 $M$ 的一个**极端点**。对每个极端点 $c\in M$，令

$$
M_c=\{x\in M\mid x\leqq c\text{ 或 }f(c)\leqq x\}.
$$

注意，$M_c$ 非空，因为 $a$ 属于它。

**引理 2.2。** *对于 $M$ 的每个极端点 $c$，都有 $M_c=M$。*

*证明。* 只需证明 $M_c$ 是一个容许子集。设 $x\in M_c$。若 $x<c$，则 $f(x)\leqq c$，故 $f(x)\in M_c$。若 $x=c$，则 $f(x)=f(c)$ 也在 $M_c$ 中。若 $f(c)\leqq x$，则 $f(c)\leqq x\leqq f(x)$，于是仍有 $f(x)\in M_c$。这样就证明了 $f(M_c)\subset M_c$。

设 $T$ 是 $M_c$ 的一个全序子集，$b$ 是 $T$ 在 $M$ 中的最小上界。若所有元素 $x\in T$ 都 $\leqq c$，则 $b\leqq c$ 且 $b\in M_c$。若某个 $x\in T$ 满足 $f(c)\leqq x$，则 $f(c)\leqq x\leqq b$，故 $b$ 属于 $M_c$。这证明了引理。

**引理 2.3。** *$M$ 的每个元素都是极端点。*

*证明。* 令 $E$ 为 $M$ 的极端点的集合。由于 $a\in E$，$E$ 非空。只需证明 $E$ 是一个容许子集。首先证明 $f$ 将 $E$ 映入自身。设 $c\in E$。设 $x\in M$ 且 $x<f(c)$。必须证明 $f(x)\leqq f(c)$。由引理 2.2，$M=M_c$，因此有 $x<c$，或 $x=c$，或 $f(c)\leqq x$。由于 $x<f(c)$，最后一种可能不能发生。若 $x<c$，则

$$
f(x)\leqq c\leqq f(c).
$$

若 $x=c$，则 $f(x)=f(c)$，因此 $f(E)\subset E$。

接着设 $T$ 是 $E$ 的一个全序子集。设 $b$ 为 $T$ 在 $M$ 中的最小上界。必须证明 $b\in E$。设 $x\in M$ 且 $x<b$。若对于所有 $c\in T$，都有 $f(c)\leqq x$，则 $c\leqq f(c)\leqq x$ 意味着 $x$ 是 $T$ 的一个上界，因此 $b\leqq x$，这是不可能的。由于对于所有 $c\in E$ 都有 $M_c=M$，必有某个 $c\in T$ 使得 $x\leqq c$。若 $x<c$，则 $f(x)\leqq c\leqq b$；若 $x=c$，则

$$
c=x<b.
$$

由于 $c$ 是极端点且 $M_c=M$，得到 $f(x)\leqq b$。这证明了 $b\in E$，$E$ 是容许的，从而证明了引理 2.3。

现在显然可见 $M$ 全序。设 $x,y\in M$。由引理 2，$x$ 是 $M$ 的一个极端点，而 $y\in M_x$，所以 $y\leqq x$ 或

$$
x\leqq f(x)\leqq y,
$$

从而证明 $M$ 全序。如前面所述，这完成了定理 2.1 的证明。

<span class="original-page-anchor" id="pdf-page-891" aria-hidden="true"></span>

我们将基本上把佐恩引理作为定理 2.1 的一个推论得到。先得到佐恩引理的一个稍弱形式。

**推论 2.4。** *设 $A$ 是一个非空的严格归纳有序集。则 $A$ 有一个极大元素。*

*证明。* 假设 $A$ 没有极大元素。则对于每个 $x\in A$，存在元素 $y_x\in A$，使得 $x<y_x$。令 $f:A\longrightarrow A$ 为对所有 $x\in A$ 都满足 $f(x)=y_x$ 的映射。于是 $A,f$ 满足定理 2.1 的假设，应用定理 2.1 便得到矛盾。

推论 2.4 与佐恩引理的唯一区别是：在推论 2.4 中，假设非空全序子集有*最小*上界，而不只是有上界。然而，将佐恩引理归结到推论 2.4 这个看似较弱的形式，是一件简单的事。在第二个推论中来做这件事。

**推论 2.5（佐恩引理）。** *设 $S$ 是一个非空的归纳有序集。则 $S$ 有一个极大元素。*

*证明。* 令 $A$ 为 $S$ 的非空全序子集的集合。由于 $S$ 的任何单元素子集都属于 $A$，$A$ 非空。若 $X,Y\in A$，定义 $X\leqq Y$ 的意思为 $X\subset Y$。于是 $A$ 是偏序的，而且实际上严格归纳有序。设 $T=\{X_i\}_{i\in I}$ 是 $A$ 的一个全序子集。令

$$
Z=\bigcup_{i\in I}X_i.
$$

则 $Z$ 全序。为说明这一点，设 $x,y\in Z$。于是对于某些 $i,j\in I$，有 $x\in X_i$ 且 $y\in X_j$。由于 $T$ 全序，不妨设 $X_i\subset X_j$。于是 $x,y\in X_j$，而 $X_j$ 全序，所以 $x\leqq y$ 或 $y\leqq x$。因此 $Z$ 全序，而且显然是 $T$ 在 $A$ 中的一个最小上界。由推论 2.4，$A$ 有一个极大元素 $X_0$。这意味着 $X_0$ 是 $S$ 的一个极大全序子集（非空）。设 $m$ 为 $X_0$ 在 $S$ 中的一个上界。则 $m$ 是所要的 $S$ 的极大元素。因为若 $x\in S$ 且 $m\leqq x$，则 $X_0\cup\{x\}$ 全序，从而由 $X_0$ 的极大性，它等于 $X_0$。因此 $x\in X_0$ 且 $x\leqq m$。故 $x=m$，证毕。

## §3. 基数

设 $A,B$ 是集合。若存在 $A$ 到 $B$ 的双射，则称 $A$ 的**基数**与 $B$ 的基数相同，并写成

$$
\operatorname{card}(A)=\operatorname{card}(B).
$$

<span class="original-page-anchor" id="pdf-page-892" aria-hidden="true"></span>

若存在一个单射 $f:A\longrightarrow B$，则称 $\operatorname{card}(A)\leqq\operatorname{card}(B)$。在此情形下，也写作 $\operatorname{card}(B)\geqq\operatorname{card}(A)$。显然，若 $\operatorname{card}(A)\leqq\operatorname{card}(B)$ 且 $\operatorname{card}(B)\leqq\operatorname{card}(C)$，则 $\operatorname{card}(A)\leqq\operatorname{card}(C)$。

这就是说，单射的复合仍是单射。类似地，若 $\operatorname{card}(A)=\operatorname{card}(B)$ 且 $\operatorname{card}(B)=\operatorname{card}(C)$，则 $\operatorname{card}(A)=\operatorname{card}(C)$。

这就是说，双射的复合仍是双射。**显然有 $\operatorname{card}(A)=\operatorname{card}(A)$。利用佐恩引理，容易证明（见习题 14）**

$$
\operatorname{card}(A)\leqq\operatorname{card}(B)\quad\text{或}\quad\operatorname{card}(B)\leqq\operatorname{card}(A).
$$

*设 $f:A\longrightarrow B$ 是集合 $A$ 到集合 $B$ 的满射。则*

$$
\operatorname{card}(B)\leqq\operatorname{card}(A).
$$

这很容易看出，因为对于每个 $y\in B$，存在一个元素 $x\in A$，记为 $x_y$，使得 $f(x_y)=y$。于是对应 $y\mapsto x_y$ 是 $B$ 到 $A$ 的单射，因此由定义，$\operatorname{card}(B)\leqq\operatorname{card}(A)$。

***给定两个非空集 $A,B$，有 $\operatorname{card}(A)\leqq\operatorname{card}(B)$ 或 $\operatorname{card}(B)\leqq\operatorname{card}(A)$。***

**这是佐恩引理的一个简单应用。考虑所有对 $(S,f)$ 组成的族，其中 $S$ 是 $A$ 的一个子集，$f:S\longrightarrow B$ 是一个单射。由极大元素的存在，立即得到这个断言。**

**定理 3.1。** （Schroeder-Bernstein）*设 $A,B$ 是集合，并假设 $\operatorname{card}(A)\leqq\operatorname{card}(B)$ 且 $\operatorname{card}(B)\leqq\operatorname{card}(A)$。则*

$$
\operatorname{card}(A)=\operatorname{card}(B).
$$

*证明。* 设

$$
f:A\longrightarrow B\quad\text{及}\quad g:B\longrightarrow A
$$

是单射。将 $A$ 分成两个不相交的集合 $A_1$ 和 $A_2$。令 $A_1$ 由所有这样的 $x\in A$ 组成：通过接连应用逆映射将 $x$ 向前追溯，

$$
x,g^{-1}(x),f^{-1}\circ g^{-1}(x),g^{-1}\circ f^{-1}\circ g^{-1}(x),\ldots,
$$

则在某一步到达一个 $A$ 中的元素，它无法再通过 $g$ 追溯到 $B$。令 $A_2$ 为 $A_1$ 的补集；换言之，它由可以无限追溯的 $x\in A$，或最终在 $B$ 中停止的 $x\in A$ 组成（即到达一个在 $f$ 下没有 $A$ 中原像的 $B$ 中元素）。于是 $A=A_1\cup A_2$。将定义一个 $A$ 到 $B$ 的双射 $h$。

若 $x\in A_1$，定义 $h(x)=f(x)$。

若 $x\in A_2$，定义 $h(x)=g^{-1}(x)=$ 满足 $g(y)=x$ 的唯一元素 $y\in B$。

于是 $h$ 显然是单射。必须证明 $h$ 是满射。设 $b\in B$。若试图通过接连应用映射

$$
f^{-1},g^{-1}\circ f^{-1},f^{-1}\circ g^{-1}\circ f^{-1}(b)
$$

来追溯 $b$，<span class="original-page-anchor" id="pdf-page-893" aria-hidden="true"></span>**若能够无限追溯，或者在 $B$ 中停止，则 $g(b)$ 属于 $A_2$，因而 $b=h(g(b))$，故 $b$ 属于 $h$ 的像。另一方面，若不能无限追溯 $b$，并在 $A$ 中停止，则 $f^{-1}(b)$ 有定义（即 $b$ 属于 $f$ 的像），且 $f^{-1}(b)$ 属于 $A_1$。在此情形下，$b=h(f^{-1}(b))$ 也属于 $h$ 的像，证毕。**

接着考虑关于基数的和与积的定理。**我们将利用佐恩引理，把任意集合的积的基数研究归结到可列的情形。先注意，无限集 $A$ 总包含一个可列集。事实上，由于 $A$ 无限，可以先选取元素 $a_1\in A$，而 $\{a_1\}$ 的补集仍无限。归纳地，若已在 $A$ 中选出不同的元素 $a_1,\ldots,a_n$，则 $\{a_1,\ldots,a_n\}$ 的补集无限，可以在此补集中选取 $a_{n+1}$。这样就得到 $A$ 中的一个不同元素序列，从而得到 $A$ 的一个可列子集。**

设 $A$ 是一个集合。所谓 $A$ 的一个**覆盖**，是指由 $A$ 的子集组成的集合 $\Gamma$，使得 $\Gamma$ 的所有元素的并

$$
\bigcup_{C\in\Gamma}C
$$

等于 $A$。若只要 $C,C'\in\Gamma$ 且 $C\ne C'$，$C$ 与 $C'$ 的交就为空，则称 $\Gamma$ 为一个**不交覆盖**。

**引理 3.2。** *设 $A$ 是一个无限集。则存在由可列集组成的 $A$ 的一个不交覆盖。*

*证明。* 令 $S$ 为这样一个集合，其元素为对 $(B,\Gamma)$，由 $A$ 的一个子集 $B$ 和由可列集组成的 $B$ 的一个不交覆盖构成。于是 $S$ 非空。事实上，由于 $A$ 无限，它包含一个可列集 $D$，而对 $(D,\{D\})$ 属于 $S$。若 $(B,\Gamma)$ 与 $(B',\Gamma')$ 是 $S$ 的元素，定义

$$
(B,\Gamma)\leqq(B',\Gamma')
$$

的意思为 $B\subset B'$ 且 $\Gamma\subset\Gamma'$。设 $T$ 是 $S$ 的一个非空全序子集。对于某个指标集 $I$，可写成 $T=\{(B_i,\Gamma_i)\}_{i\in I}$。令

$$
B=\bigcup_{i\in I}B_i\quad\text{及}\quad\Gamma=\bigcup_{i\in I}\Gamma_i.
$$

若 $C,C'\in\Gamma,C\ne C'$，则存在某些指标 $i,j$，使得 $C\in\Gamma_i$ 且 $C'\in\Gamma_j$。由于 $T$ 全序，不妨设

$$
(B_i,\Gamma_i)\leqq(B_j,\Gamma_j).
$$

因此，实际上 $C,C'$ 都是 $\Gamma_j$ 的元素，故 $C,C'$ 的交为空。另一方面，若 $x\in B$，则对于某个 $i$，有 $x\in B_i$，因此存在某个 $C\in\Gamma_i$，使得 $x\in C$。故 $\Gamma$ 是 $B$ 的一个不交覆盖。由于<span class="original-page-anchor" id="pdf-page-894" aria-hidden="true"></span>每个 $\Gamma_i$ 的元素都是 $A$ 的可列子集，可知 $\Gamma$ 是由可列集组成的 $B$ 的一个不交覆盖，因此 $(B,\Gamma)$ 属于 $S$，而且显然是 $T$ 的一个上界。所以 $S$ 归纳有序。

由佐恩引理，设 $(M,\Delta)$ 为 $S$ 的一个极大元素。假设 $M\ne A$。若 $M$ 在 $A$ 中的补集无限，则此补集中包含一个可列集 $D$。于是

$$
(M\cup D,\Delta\cup\{D\})
$$

是一个比 $(M,\Delta)$ 更大的对，与 $(M,\Delta)$ 的极大性矛盾。因此，$M$ 在 $A$ 中的补集是一个有限集 $F$。设 $D_0$ 为 $\Delta$ 的一个元素。令

$$
D_1=D_0\cup F.
$$

则 $D_1$ 可列。令 $\Delta_1$ 为由 $\Delta$ 中除 $D_0$ 以外的所有元素以及 $D_1$ 组成的集合。则 $\Delta_1$ 是由可列集组成的 $A$ 的一个不交覆盖，证毕。

**定理 3.3。** *设 $A$ 是一个无限集，$D$ 是一个可列集。则*

$$
\operatorname{card}(A\times D)=\operatorname{card}(A).
$$

*证明。* 由引理，可以将 $A$ 写成可列集的不交并

$$
A=\bigcup_{i\in I}D_i.
$$

于是

$$
A\times D=\bigcup_{i\in I}(D_i\times D).
$$

对于每个 $i\in I$，由命题 1.5，有 $D_i\times D$ 到 $D_i$ 的双射。由于集合 $D_i\times D$ 两两不交，这样便得到 $A\times D$ 到 $A$ 的一个双射，正如所要求的。

**推论 3.4。** *若 $F$ 是一个非空有限集，则*

$$
\operatorname{card}(A\times F)=\operatorname{card}(A).
$$

*证明。* 有

$$
\operatorname{card}(A)\leqq\operatorname{card}(A\times F)\leqq\operatorname{card}(A\times D)=\operatorname{card}(A).
$$

然后可以利用定理 3.1 得到所要的结论。

**推论 3.5。** *设 $A,B$ 是非空集，$A$ 无限，并假设*

$$
\operatorname{card}(B)\leqq\operatorname{card}(A).
$$

<span class="original-page-anchor" id="pdf-page-895" aria-hidden="true"></span>

*则*

$$
\operatorname{card}(A\cup B)=\operatorname{card}(A).
$$

**证明。对于 $B$ 的某个子集 $C$，可以写成 $A\cup B=A\cup C$，其中 $C$ 与 $A$ 不交。（令 $C$ 为 $B$ 中所有不属于 $A$ 的元素的集合。）于是 $\operatorname{card}(C)\leqq\operatorname{card}(A)$。然后可以构造 $A\cup C$ 到 $A$ 与一个具有 $2$ 个元素的集合的积**

$$
A\times\{1,2\}
$$

**的单射。具体说，$A$ 与 $A\times\{1\}$ 之间有一个显然的双射，而且还有 $C$ 到 $A\times\{2\}$ 的单射。因此**

$$
\operatorname{card}(A\cup C)\leqq\operatorname{card}(A\times\{1,2\}).
$$

**由推论 3.4 和定理 3.1，完成证明。**

**定理 3.6。** *设 $A$ 是一个无限集。则*

$$
\operatorname{card}(A\times A)=\operatorname{card}(A).
$$

**证明。令 $S$ 为所有对 $(B,f)$ 组成的集合，其中 $B$ 是 $A$ 的一个无限子集，$f$ 是 $B$ 到 $B\times B$ 的双射。于是 $S$ 非空，因为若 $D$ 是 $A$ 的一个可列子集，总能找到 $D$ 到 $D\times D$ 的双射。若 $(B,f)$ 和 $(B',f')$ 属于 $S$，规定 $(B,f)\leqq(B',f')$ 的意思为 $B\subset B'$，且 $f'$ 在 $B$ 上的限制等于 $f$。于是 $S$ 是偏序的，我们断言 $S$ 归纳有序。设 $T$ 是 $S$ 的一个非空全序子集，并设对于某个指标集 $I$，$T$ 由对 $(B_i,f_i)$，$i\in I$，组成。令**

$$
M=\bigcup_{i\in I}B_i.
$$

**将定义一个双射 $g:M\longrightarrow M\times M$。若 $x\in M$，则 $x$ 属于某个 $B_i$。定义 $g(x)=f_i(x)$。此值 $f_i(x)$ 与所选的包含 $x$ 的 $B_i$ 无关。事实上，若对于某个 $j\in I$，有 $x\in B_j$，则不妨设**

$$
(B_i,f_i)\leqq(B_j,f_j).
$$

**由假设，$B_i\subset B_j$ 且 $f_j(x)=f_i(x)$，所以 $g$ 定义良好。为证明 $g$ 是满射，设 $x,y\in M$ 及 $(x,y)\in M\times M$。于是对于某个 $i\in I$，有 $x\in B_i$，对于某个 $j\in I$，有 $y\in B_j$。仍由 $T$ 全序，不妨设 $(B_i,f_i)\leqq(B_j,f_j)$。因此 $B_i\subset B_j$，且 $x,y\in B_j$。存在元素 $b\in B_j$，使得**

$$
f_j(b)=(x,y)\in B_j\times B_j.
$$

**由定义，$g(b)=(x,y)$，因此 $g$ 是满射。将 $g$ 为单射的证明留给读者，从而完成 $g$ 为双射的证明。于是可以看到**<span class="original-page-anchor" id="pdf-page-896" aria-hidden="true"></span>$(M,g)$ 是 $T$ 在 $S$ 中的一个上界，因此 $S$ 归纳有序。

**设 $(M,g)$ 是 $S$ 的一个极大元素，$C$ 是 $M$ 在 $A$ 中的补集。若 $\operatorname{card}(C)\leqq\operatorname{card}(M)$，则由推论 3.5，**

$$
\operatorname{card}(A)=\operatorname{card}(M\cup C)=\operatorname{card}(M),
$$

**因此 $\operatorname{card}(M)=\operatorname{card}(A)$。由于 $\operatorname{card}(M)=\operatorname{card}(M\times M)$，在此情形下已完成证明。若**

$$
\operatorname{card}(M)\leqq\operatorname{card}(C),
$$

**则 $C$ 有一个子集 $M_1$，与 $M$ 的基数相同。考虑**

$$
\begin{aligned}
&(M\cup M_1)\times(M\cup M_1)\\
&\qquad=(M\times M)\cup(M_1\times M)\cup(M\times M_1)\cup(M_1\times M_1).
\end{aligned}
$$

**由关于 $M$ 的假设和推论 3.5，此等式右边最后三个括号中的集合与 $M$ 的基数相同。因此**

$$
(M\cup M_1)\times(M\cup M_1)=(M\times M)\cup M_2,
$$

**其中 $M_2$ 与 $M\times M$ 不交，并且与 $M$ 的基数相同。现在定义一个双射**

$$
g_1:M\cup M_1\longrightarrow(M\cup M_1)\times(M\cup M_1).
$$

**若 $x\in M$，令 $g_1(x)=g(x)$，并令 $g_1$ 在 $M_1$ 上为任意一个 $M_1$ 到 $M_2$ 的双射。这样便将 $g$ 扩张到了 $M\cup M_1$，而对 $(M\cup M_1,g_1)$ 属于 $S$，与 $(M,g)$ 的极大性矛盾。因此，$\operatorname{card}(M)\leqq\operatorname{card}(C)$ 这一情形不能发生，定理得证（使用下面的习题 14）。**

**推论 3.7。** *若 $A$ 是一个无限集，$A^{(n)}=A\times\cdots\times A$ 是 $n$ 次乘积，则*

$$
\operatorname{card}(A^{(n)})=\operatorname{card}(A).
$$

*证明。* 归纳法。

**推论 3.8。** *若 $A_1,\ldots,A_n$ 是非空集，$A_n$ 无限，并且对于 $i=1,\ldots,n$，都有*

$$
\operatorname{card}(A_i)\leqq\operatorname{card}(A_n),
$$

*则*

$$
\operatorname{card}(A_1\times\cdots\times A_n)=\operatorname{card}(A_n).
$$

<span class="original-page-anchor" id="pdf-page-897" aria-hidden="true"></span>

*证明。* 有

$$
\operatorname{card}(A_n)\leqq\operatorname{card}(A_1\times\cdots\times A_n)\leqq\operatorname{card}(A_n\times\cdots\times A_n),
$$

利用推论 3.7 和 Schroeder-Bernstein 定理，完成证明。

**推论 3.9。** *设 $A$ 是一个无限集，$\Phi$ 是 $A$ 的有限子集组成的集合。则*

$$
\operatorname{card}(\Phi)=\operatorname{card}(A).
$$

*证明。* 对每个整数 $n=1,2,\ldots$，令 $\Phi_n$ 为 $A$ 的恰有 $n$ 个元素的子集组成的集合。先证明 $\operatorname{card}(\Phi_n)\leqq\operatorname{card}(A)$。若 $F$ 是 $\Phi_n$ 的一个元素，以任意方式排列 $F$ 的元素，比如

$$
F=\{x_1,\ldots,x_n\},
$$

并将 $F$ 对应到元素 $(x_1,\ldots,x_n)\in A^{(n)}$：

$$
F\mapsto(x_1,\ldots,x_n).
$$

若 $G$ 是 $A$ 的另一个具有 $n$ 个元素的子集，比如 $G=\{y_1,\ldots,y_n\}$，且 $G\ne F$，则

$$
(x_1,\ldots,x_n)\ne(y_1,\ldots,y_n).
$$

因此，映射

$$
F\mapsto(x_1,\ldots,x_n)
$$

是 $\Phi_n$ 到 $A^{(n)}$ 的单射。由推论 3.7，得到

$$
\operatorname{card}(\Phi_n)\leqq\operatorname{card}(A).
$$

现在 $\Phi$ 是各 $\Phi_n$，$n=1,2,\ldots$，的不交并；证明 $\operatorname{card}(\Phi)\leqq\operatorname{card}(A)$ 留作习题（参见习题 1）。由于

$$
\operatorname{card}(A)\leqq\operatorname{card}(\Phi),
$$

因为特别有 $\operatorname{card}(\Phi_1)=\operatorname{card}(A)$，可知推论得证。

> **译校注。** 原文的并集从 $n=1$ 开始。按照 §1 的定义，有限子集包括空集，因此准确的并集应为 $\Phi=\{\varnothing\}\cup\bigcup_{n\geqq1}\Phi_n$。由推论 3.5，对于无限集 $A$，补入这一单元素层不改变结论。上文保留原句。

在下一个定理中，将看到给定一个集合，总存在另一个基数更大的集合。

**定理 3.10。** *设 $A$ 是一个无限集，$T$ 是由两个元素 $\{0,1\}$ 组成的集合。设 $M$ 为所有 $A$ 到 $T$ 的映射组成的集合。则*

$$
\operatorname{card}(A)\leqq\operatorname{card}(M)\quad\text{且}\quad\operatorname{card}(A)\ne\operatorname{card}(M).
$$

<span class="original-page-anchor" id="pdf-page-898" aria-hidden="true"></span>

*证明。* 对每个 $x\in A$，令

$$
f_x:A\longrightarrow\{0,1\}
$$

为满足 $f_x(x)=1$，且当 $y\ne x$ 时 $f_x(y)=0$ 的映射。于是 $x\mapsto f_x$ 显然是 $A$ 到 $M$ 的单射，因此 $\operatorname{card}(A)\leqq\operatorname{card}(M)$。假设

$$
\operatorname{card}(A)=\operatorname{card}(M).
$$

设

$$
x\mapsto g_x
$$

为 $A$ 与 $M$ 之间的双射。按照规则

$$
\begin{aligned}
h(x)&=0&&\text{若 }g_x(x)=1,\\
h(x)&=1&&\text{若 }g_x(x)=0,
\end{aligned}
$$

定义映射 $h:A\longrightarrow\{0,1\}$。

于是，对于任何 $x$，当然都有 $h\ne g_x$，这与 $x\mapsto g_x$ 是双射的假设矛盾，从而证明定理 3.10。

**推论 3.11。** *设 $A$ 是一个无限集，$S$ 是 $A$ 的所有子集组成的集合。则 $\operatorname{card}(A)\leqq\operatorname{card}(S)$ 且 $\operatorname{card}(A)\ne\operatorname{card}(S)$。*

*证明。* 留作习题。［*提示：* 若 $B$ 是 $A$ 的一个非空子集，使用特征函数 $\varphi_B$，满足

$$
\begin{aligned}
\varphi_B(x)&=1&&\text{若 }x\in B,\\
\varphi_B(x)&=0&&\text{若 }x\notin B.
\end{aligned}
$$

关于对应 $B\mapsto\varphi_B$，可以说些什么？］

## §4. 良序

若有序集 $A$ 全序，并且每个非空子集 $B$ 都有一个最小元素，即有元素 $a\in B$，使得对于所有 $x\in B$，都有 $a\leqq x$，则称 $A$ 是**良序的**。

**例 1。** 正整数集 $\mathbf Z^+$ 是良序的。任何有限集都可以赋予良序，可列集 $D$ 也可以赋予良序：$D$ 与 $\mathbf Z^+$ 之间的任何双射，都在 $D$ 上给出一个良序。

**例 2。** 设 $S$ 是一个良序集，$b$ 是某个集合的一个元素，$b\notin S$。令 $A=S\cup\{b\}$。对所有 $x\in S$，定义 $x\leqq b$。于是 $A$ 全序，而且实际上良序。

<span class="original-page-anchor" id="pdf-page-899" aria-hidden="true"></span>

*证明。* 设 $B$ 是 $A$ 的一个非空子集。若 $B$ 仅由 $b$ 组成，则 $b$ 是 $B$ 的一个最小元素。否则，$B$ 包含某个元素 $a\in A$。于是 $B\cap A$ 非空，因此有一个最小元素，它显然也是 $B$ 的一个最小元素。

> **译校注。** 在例 2 中，$A=S\cup\{b\}$，而已知的良序在 $S$ 上。此证明中的原印字样 $a\in A$ 和 $B\cap A$ 因此应读作 $a\in S$ 和 $B\cap S$：若 $B$ 不仅是 $\{b\}$，则它包含 $S$ 的一个元素，其与 $S$ 的非空交集有最小元素。使用 $B\cap A=B$ 则会预先假定正在证明的结论。上文保留原句。

**定理 4.1。** *每个非空集都可以赋予良序。*

**证明。设 $A$ 是一个非空集。令 $S$ 为所有对 $(X,\omega)$ 组成的集合，其中 $X$ 是 $A$ 的一个子集，$\omega$ 是 $X$ 上的一个良序。注意，$S$ 非空，因为 $A$ 中任意一个单元素都给出这样的一个对。若 $(X,\omega)$ 与 $(X',\omega')$ 是这样的两个对，当 $X\subset X'$、$\omega'$ 在 $X$ 上诱导的序等于 $\omega$，且 $X$ 是 $X'$ 的一个始段时，定义 $(X,\omega)\leqq(X',\omega')$。显然，这定义了 $S$ 上的一个序；我们断言 $S$ 归纳有序。设 $\{(X_i,\omega_i)\}$ 是 $S$ 的一个非空全序子集。令 $X=\bigcup X_i$。若 $a,b\in X$，则 $a,b$ 属于某个 $X_i$，当在序 $\omega_i$ 下有 $a\leqq b$ 时，定义在 $X$ 中有 $a\leqq b$。这与 $i$ 的选择无关（由全序假设立即可知）。事实上，$X$ 良序，因为若 $Y$ 是 $X$ 的一个非空子集，则存在某个元素 $y\in Y$，属于某个 $X_j$。设 $c$ 为 $X_j\cap Y$ 的一个最小元素。立即可验证，$c$ 是 $Y$ 的一个最小元素。因此可以应用佐恩引理。设 $(X,\omega)$ 是 $S$ 的一个极大元素。若 $X\ne A$，则利用例 2，可以在一个比 $X$ 更大的子集上定义良序，与极大性假设矛盾。这证明了定理 4.1。**

**注。** 定理 4.1 是佐恩引理的一个直接而简单的推论。通常，在数学中处理无限过程时，佐恩引理是最有效的工具。

## 习题

**1.** 证明推论 3.9 的证明中所述的断言。

**2.** 若 $A$ 是一个无限集，$\Phi_n$ 是 $A$ 的恰有 $n$ 个元素的子集组成的集合，证明对于 $n\geqq1$，有

$$
\operatorname{card}(A)\leqq\operatorname{card}(\Phi_n).
$$

**3.** 设 $A_i$ 是无限集，$i=1,2,\ldots$，并假设对于某个集合 $A$ 及所有 $i$，有

$$
\operatorname{card}(A_i)\leqq\operatorname{card}(A).
$$

证明

$$
\operatorname{card}\left(\bigcup_{i=1}^\infty A_i\right)\leqq\operatorname{card}(A).
$$

<span class="original-page-anchor" id="pdf-page-900" aria-hidden="true"></span>

**4.** 设 $K$ 是复数域的一个子域。证明对于每个整数 $n\geqq1$，$\mathbf C$ 中 $K$ 的次数为 $n$ 的扩张所组成的集合，其基数 $\leqq\operatorname{card}(K)$。

**5.** 设 $K$ 是一个无限域，$E$ 是 $K$ 的一个代数扩张。证明

$$
\operatorname{card}(E)=\operatorname{card}(K).
$$

**6.** 完成推论 3.11 的证明。

**7.** 若 $A,B$ 是集合，用 $M(A,B)$ 表示所有 $A$ 到 $B$ 的映射组成的集合。若 $B,B'$ 的基数相同，证明 $M(A,B)$ 与 $M(A,B')$ 的基数相同。若 $A,A'$ 的基数相同，证明 $M(A,B)$ 与 $M(A',B)$ 的基数相同。

**8.** 设 $A$ 是一个无限集，将 $\operatorname{card}(A)$ 简记为 $\alpha$。若 $B$ 是一个无限集，将 $\operatorname{card}(B)$ 简记为 $\beta$。将 $\alpha\beta$ 定义为 $\operatorname{card}(A\times B)$。设 $B'$ 是一个与 $A$ 不交的集合，满足 $\operatorname{card}(B)=\operatorname{card}(B')$。将 $\alpha+\beta$ 定义为 $\operatorname{card}(A\cup B')$。用 $B^A$ 表示所有 $A$ 到 $B$ 的映射组成的集合，并将 $\operatorname{card}(B^A)$ 记为 $\beta^\alpha$。设 $C$ 是一个无限集，将 $\operatorname{card}(C)$ 简记为 $\gamma$。证明下列断言：

(a) $\alpha(\beta+\gamma)=\alpha\beta+\alpha\gamma$。

(b) $\alpha\beta=\beta\alpha$。

(c) $\alpha^{\beta+\gamma}=\alpha^\beta\alpha^\gamma$。

**9.** 设 $K$ 是一个无限域。证明存在一个代数闭域 $K^a$，包含 $K$ 为子域，且在 $K$ 上代数。［*提示：* 设 $\Omega$ 是一个包含 $K$ 的集合，其基数严格大于 $K$ 的基数。考虑所有对 $(E,\varphi)$ 组成的集合 $S$，其中 $E$ 是 $\Omega$ 的一个子集，满足 $K\subset E$；$\varphi$ 表示 $E$ 上的加法与乘法合成律，使 $E$ 成为一个域，$K$ 是其子域，且 $E$ 在 $K$ 上代数。以显然的方式定义 $S$ 上的一个偏序；证明 $S$ 归纳有序，而且一个极大元素在 $K$ 上代数并且代数闭。在最后一步需要使用习题 5。］

**10.** 设 $K$ 是一个无限域。证明有理函数域 $K(t)$ 与 $K$ 的基数相同。

**11.** 设 $J_n$ 是整数集 $\{1,\ldots,n\}$。设 $\mathbf Z^+$ 是正整数集。证明下列集合的基数相同：

(a) 所有映射 $M(\mathbf Z^+,J_n)$ 组成的集合。

(b) 所有映射 $M(\mathbf Z^+,J_2)$ 组成的集合。

(c) 所有满足 $0\leqq x<1$ 的实数 $x$ 组成的集合。

(d) 所有实数组成的集合。

> **译校注。** 此习题需要 $n\geqq2$。当 $n=1$ 时，$M(\mathbf Z^+,J_1)$ 只有一个映射，而 (b)–(d) 中的集合都是无限的。原印陈述未给出这一限制，上文保留原文。

**12.** 证明 $M(\mathbf Z^+,\mathbf Z^+)$ 与实数集的基数相同。

**13.** 设 $S$ 是一个非空集。用 $S'$ 表示 $S$ 与自身取可列多次的乘积。证明 $(S')'$ 与 $S'$ 的基数相同。［给定一个基数严格大于 $\mathbf R$ 的基数的集合 $S$，我不知道是否总有 $\operatorname{card}S=\operatorname{card}S'$。］1994 年补记：我从传闻中得知，据 Solovay 说，答案是“否”。

**14.** 设 $A,B$ 是非空集。证明 $\operatorname{card}(A)\leqq\operatorname{card}(B)$ 或 $\operatorname{card}(B)\leqq\operatorname{card}(A)$。

［*提示：* 考虑所有对 $(C,f)$ 组成的族，其中 $C$ 是 $A$ 的一个子集，$f:C\longrightarrow B$ 是一个单射。由佐恩引理，存在一个极大元素。现在完成证明。］
