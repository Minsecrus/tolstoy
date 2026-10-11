---
title: "第六章 伽罗瓦理论"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第五章 代数扩张","link":"/library/volume-86/chapter-005"}
next: {"text":"第七章 环的扩张","link":"/library/volume-86/chapter-007"}
---

# 第六章 伽罗瓦理论

<span class="original-page-anchor" id="pdf-page-275" aria-hidden="true"></span>

本章包含伽罗瓦理论的核心内容。我们将详细研究有限（有时也研究无限）伽罗瓦扩张的自同构群，并给出分圆扩张、阿贝尔扩张乃至非阿贝尔扩张等例子，由此引入伽罗瓦群的矩阵表示及其分类的研究。我们还将提及一些基本的未解决问题，其中最突出的是：给定一个有限群 $G$，是否存在一个以该群为伽罗瓦群的 $\mathbf{Q}$ 的伽罗瓦扩张？以下三篇综述提供了关于这些问题的较近观点以及大量参考文献：

B. Matzat，*Konstruktive Galoistheorie*（《构造性伽罗瓦理论》），Springer Lecture Notes **1284**，1987 年。

B. Matzat，Über das Umkehrproblem der Galoisschen Theorie（论伽罗瓦理论的逆问题），*Jahrsbericht Deutsch. Mat.-Verein.* **90**（1988），第 155–183 页。

J. P. Serre，*Topics in Galois theory*（《伽罗瓦理论专题》），1989 年哈佛大学课程，Jones and Bartlett，Boston，1992 年。

关于这个问题，以及确定特定域（尤其是有理数域）上的伽罗瓦群的问题，我们将在正文中的适当位置给出更具体的参考文献。

## §1. 伽罗瓦扩张

设 $K$ 为域，$G$ 为 $K$ 的一个自同构群。用 $K^G$ 表示 $K$ 的如下子集：它由所有满足对每个 $\sigma\in G$ 都有 $x^\sigma=x$ 的元素 $x\in K$ 组成。它也称为 $G$ 的**不动域**。它是一个域，因为如果 $x,y\in K^G$，那么

$$
(x+y)^\sigma=x^\sigma+y^\sigma=x+y
$$

<span class="original-page-anchor" id="pdf-page-276" aria-hidden="true"></span>

对所有 $\sigma\in G$ 都成立；类似地，可以验证 $K$ 对乘法、减法和取乘法逆元封闭。此外，$K^G$ 包含 $0$ 和 $1$，因而包含素域。

域 $k$ 的一个代数扩张 $K$，如果是正规且可分的，就称为**伽罗瓦扩张**。我们把 $K$ 看成嵌入在某个代数闭包中。$K$ 在 $k$ 上的自同构群称为 $K$ 在 $k$ 上的**伽罗瓦群**，记作 $G(K/k)$、$G_{K/k}$、$\operatorname{Gal}(K/k)$，或简记作 $G$。它与所有从 $K$ 到 $K^a$ 的 $k$-嵌入组成的集合相同。

为方便读者，现在先陈述有限伽罗瓦扩张的伽罗瓦理论的主要结论。

**定理 1.1。** *设 $K$ 为 $k$ 的有限伽罗瓦扩张，其伽罗瓦群为 $G$。$K$ 的包含 $k$ 的子域 $E$ 的集合，与 $G$ 的子群 $H$ 的集合之间有一个双射，由 $E=K^H$ 给出。域 $E$ 在 $k$ 上是伽罗瓦扩张，当且仅当 $H$ 是 $G$ 的正规子群；此时映射 $\sigma\mapsto\sigma|E$ 诱导出 $G/H$ 到 $E$ 在 $k$ 上的伽罗瓦群的同构。*

我们将逐步给出证明，并尽可能在无限扩张的情形下给出。

**定理 1.2。** *设 $K$ 为 $k$ 的伽罗瓦扩张，$G$ 为其伽罗瓦群。那么 $k=K^G$。如果 $F$ 是中间域，即 $k\subset F\subset K$，则 $K$ 在 $F$ 上是伽罗瓦扩张。映射*

$$
F\mapsto G(K/F)
$$

*从中间域的集合到 $G$ 的子群的集合是单射。*

*证明。* 设 $\alpha\in K^G$。设 $\sigma$ 为从 $k(\alpha)$ 到 $K^a$ 的任意嵌入，且在 $k$ 上诱导恒等映射。将 $\sigma$ 延拓为从 $K$ 到 $K^a$ 的嵌入，并仍将该延拓称为 $\sigma$。于是 $\sigma$ 是 $K$ 在 $k$ 上的自同构，因此是 $G$ 的元素。根据假设，$\sigma$ 固定 $\alpha$。所以

$$
[k(\alpha):k]_s=1.
$$

因为 $\alpha$ 在 $k$ 上可分，所以 $k(\alpha)=k$，且 $\alpha$ 是 $k$ 的元素。这就证明了第一个断言。

设 $F$ 为中间域。根据第 V 章的定理 3.4 和定理 4.5，$K$ 在 $F$ 上正规且可分。因此 $K$ 在 $F$ 上是伽罗瓦扩张。如果 $H=G(K/F)$，那么由上面的证明可得 $F=K^H$。如果 $F,F'$ 为中间域，且 $H=G(K/F)$、$H'=G(K/F')$，那么

$$
F=K^H\quad\text{且}\quad F'=K^{H'}.
$$

如果 $H=H'$，则 $F=F'$，所以映射

$$
F\mapsto G(K/F)
$$

是单射，定理得证。

<span class="original-page-anchor" id="pdf-page-277" aria-hidden="true"></span>

有时，我们把中间域的群 $G(K/F)$ 称为与 $F$ **相伴**的群。如果 $G$ 的子群 $H$ 满足 $H=G(K/F)$，就说 $H$ **属于**中间域 $F$。

**推论 1.3。** *设 $K/k$ 为伽罗瓦扩张，其群为 $G$。设 $F,F'$ 为两个中间域，$H,H'$ 分别为属于 $F,F'$ 的 $G$ 的子群。那么 $H\cap H'$ 属于 $FF'$。*

*证明。* $H\cap H'$ 的每个元素都固定 $FF'$；而 $G$ 中每个固定 $FF'$ 的元素也固定 $F$ 和 $F'$，因而属于 $H\cap H'$。断言得证。

**推论 1.4。** *沿用推论 1.3 的记号。$G$ 中包含 $H,H'$ 的最小子群的不动域是 $F\cap F'$。*

*证明。* 显然。

**推论 1.5。** *沿用推论 1.3 的记号。那么 $F\subset F'$ 当且仅当 $H'\subset H$。*

*证明。* 如果 $F\subset F'$，且 $\sigma\in H'$ 固定 $F'$，那么 $\sigma$ 固定 $F$，故 $\sigma$ 属于 $H$。反过来，如果 $H'\subset H$，那么 $H$ 的不动域包含在 $H'$ 的不动域中，所以 $F\subset F'$。

**推论 1.6。** *设 $E$ 为域 $k$ 的有限可分扩张，$K$ 为包含 $E$ 的 $k$ 的最小正规扩张。那么 $K$ 在 $k$ 上是有限伽罗瓦扩张。满足 $k\subset F\subset E$ 的中间域 $F$ 只有有限多个。*

*证明。* 我们知道 $K$ 正规且可分；并且 $K$ 在 $k$ 上有限，因为前面已知它是 $E$ 的有限多个共轭域的有限复合域。$K/k$ 的伽罗瓦群只有有限多个子群。因此 $K$ 中包含 $k$ 的子域只有有限多个，从而 $E$ 中包含 $k$ 的子域更只有有限多个。

当然，推论 1.6 的最后一个断言已在前一章证明，这里从另一个角度得到了另一个证明。

**引理 1.7。** *设 $E$ 为 $k$ 的代数可分扩张。假设存在整数 $n\geqq1$，使 $E$ 的每个元素 $\alpha$ 在 $k$ 上的次数都 $\leqq n$。那么 $E$ 在 $k$ 上有限，且 $[E:k]\leqq n$。*

*证明。* 取 $E$ 中的元素 $\alpha$，使次数 $[k(\alpha):k]$ 最大，记为 $m\leqq n$。我们断言 $k(\alpha)=E$。否则存在元素 $\beta\in E$，使得 $\beta\notin k(\alpha)$；根据本原元定理，存在元素 $\gamma\in k(\alpha,\beta)$，使得 $k(\alpha,\beta)=k(\gamma)$。但由域塔

$$
k\subset k(\alpha)\subset k(\alpha,\beta)
$$

可知 $[k(\alpha,\beta):k]>m$，所以 $\gamma$ 在 $k$ 上的次数 $>m$，矛盾。

<span class="original-page-anchor" id="pdf-page-278" aria-hidden="true"></span>

**定理 1.8。**（Artin。）*设 $K$ 为域，$G$ 为 $K$ 的一个有限自同构群，其阶为 $n$。设 $k=K^G$ 为不动域。那么 $K$ 是 $k$ 的有限伽罗瓦扩张，其伽罗瓦群为 $G$，并且 $[K:k]=n$。*

*证明。* 设 $\alpha\in K$，并取 $G$ 中一个极大的元素集合 $\sigma_1,\ldots,\sigma_r$，使 $\sigma_1\alpha,\ldots,\sigma_r\alpha$ 两两不同。如果 $\tau\in G$，则 $(\tau\sigma_1\alpha,\ldots,\tau\sigma_r\alpha)$ 与 $(\sigma_1\alpha,\ldots,\sigma_r\alpha)$ 仅相差一个置换，因为 $\tau$ 是单射，而且每个 $\tau\sigma_i\alpha$ 都属于集合 $\{\sigma_1\alpha,\ldots,\sigma_r\alpha\}$；否则这个集合就不是极大的。因此 $\alpha$ 是多项式

$$
f(X)=\prod_{i=1}^r(X-\sigma_i\alpha)
$$

的一个根，且对于任何 $\tau\in G$，都有 $f^\tau=f$。所以 $f$ 的系数属于 $K^G=k$。此外，$f$ 可分。因此 $K$ 的每个元素 $\alpha$ 都是某个系数在 $k$ 中、次数 $\leqq n$ 的可分多项式的根。并且这个多项式在 $K$ 中分解为一次因子。因此 $K$ 在 $k$ 上可分且正规，故为伽罗瓦扩张。根据引理 1.7，有 $[K:k]\leqq n$。$K$ 在 $k$ 上的伽罗瓦群的阶 $\leqq[K:k]$（由第 V 章定理 4.1），因此 $G$ 必须是整个伽罗瓦群。所有断言得证。

**推论 1.9。** *设 $K$ 为 $k$ 的有限伽罗瓦扩张，$G$ 为其伽罗瓦群。那么 $G$ 的每个子群都属于某个满足 $k\subset F\subset K$ 的子域 $F$。*

*证明。* 设 $H$ 为 $G$ 的子群，并令 $F=K^H$。根据 Artin 定理，$K$ 在 $F$ 上是伽罗瓦扩张，且群为 $H$。

**注。** 当 $K$ 为 $k$ 的无限伽罗瓦扩张时，上面的推论不再成立。这说明有限情形的证明必须采用某种计数论证。在这里的处理方式中，我们使用了一个较传统的论证。读者可查阅 Artin 著作 *Galois Theory*（《伽罗瓦理论》）中的原证明。在无限情形中，可以在伽罗瓦群 $G$ 上定义 Krull 拓扑（参见习题 43–45），使 $G$ 成为紧的全不连通群。属于中间域的子群是*闭*子群。读者在整个讨论中完全略去无限情形，也不会妨碍理解。无限情形的证明通常与有限情形相同。

伽罗瓦扩张和伽罗瓦群的概念完全由代数方式定义。因此，它们在同构下的形式行为，正如任何范畴中对象所应有的那样。我们针对目前的情形更明确地说明这种行为。

设 $K$ 为 $k$ 的伽罗瓦扩张。设

$$
\lambda:K\to\lambda K
$$

<span class="original-page-anchor" id="pdf-page-279" aria-hidden="true"></span>

为同构。那么 $\lambda K$ 是 $\lambda k$ 的伽罗瓦扩张。

![同构 lambda 把 K/k 变为 lambda K/lambda k。](/library/volume-86/diagrams/pdf-0279-isomorphism.png)

设 $G$ 为 $K$ 在 $k$ 上的伽罗瓦群。那么映射

$$
\sigma\mapsto\lambda\circ\sigma\circ\lambda^{-1}
$$

给出从 $G$ 到 $\lambda K$ 在 $\lambda k$ 上的伽罗瓦群的同态，其逆映射为

$$
\lambda^{-1}\circ\tau\circ\lambda\mapsfrom\tau.
$$

因此，在上述映射下，$G(\lambda K/\lambda k)$ 同构于 $G(K/k)$。可以写成

$$
G(\lambda K/\lambda k)^\lambda=G(K/k)
$$

或

$$
G(\lambda K/\lambda k)=\lambda G(K/k)\lambda^{-1},
$$

其中指数 $\lambda$ 表示“共轭”，即

$$
\sigma^\lambda=\lambda^{-1}\circ\sigma\circ\lambda.
$$

在复合映射 $\lambda$ 与 $\omega$ 时，如果希望保留规则

$$
(\sigma^\lambda)^\omega=\sigma^{\lambda\circ\omega},
$$

就无法避免这种反变性。

特别地，设 $F$ 为中间域，$k\subset F\subset K$，$\lambda:F\to\lambda F$ 为 $F$ 到 $K$ 中的嵌入，并假设它已延拓成 $K$ 的自同构。那么 $\lambda K=K$。因此

$$
G(K/\lambda F)^\lambda=G(K/F)
$$

且

$$
G(K/\lambda F)=\lambda G(K/F)\lambda^{-1}.
$$

**定理 1.10。** *设 $K$ 为 $k$ 的伽罗瓦扩张，其群为 $G$。设 $F$ 为子域，$k\subset F\subset K$，并令 $H=G(K/F)$。那么 $F$ 在 $k$ 上正规，当且仅当 $H$ 在 $G$ 中正规。如果 $F$ 在 $k$ 上正规，那么限制映射 $\sigma\mapsto\sigma|F$* <span class="original-page-anchor" id="pdf-page-280" aria-hidden="true"></span>*是从 $G$ 到 $F$ 在 $k$ 上的伽罗瓦群的满同态，其核为 $H$。因此有 $G(F/k)\approx G/H$。*

*证明。* 假设 $F$ 在 $k$ 上正规，并设 $G'$ 为它的伽罗瓦群。限制映射 $\sigma\mapsto\sigma|F$ 把 $G$ 映到 $G'$ 中；根据定义，它的核为 $H$。所以 $H$ 在 $G$ 中正规。此外，任意元素 $\tau\in G'$ 都能延拓为 $K$ 到 $K^a$ 中的嵌入，该嵌入必为 $K$ 的自同构，所以限制映射是满射。这就证明了最后的结论。最后，假设 $F$ 在 $k$ 上不正规。那么存在 $F$ 到 $K$ 中的一个 $k$-嵌入 $\lambda$，它不是自同构，即 $\lambda F\ne F$。将 $\lambda$ 延拓为 $K$ 在 $k$ 上的自同构。伽罗瓦群 $G(K/\lambda F)$ 与 $G(K/F)$ 共轭，而且属于不同的子域，因此不可能相等。所以 $H$ 在 $G$ 中不正规。

如果伽罗瓦扩张 $K/k$ 的伽罗瓦群 $G$ 是阿贝尔群（相应地，是循环群），就称 $K/k$ 是**阿贝尔扩张**（相应地，是**循环扩张**）。

**推论 1.11。** *设 $K/k$ 为阿贝尔扩张（相应地，为循环扩张）。如果 $F$ 是中间域，$k\subset F\subset K$，那么 $F$ 在 $k$ 上是伽罗瓦扩张，而且是阿贝尔扩张（相应地，是循环扩张）。*

*证明。* 由阿贝尔群的子群是正规的，以及阿贝尔群（相应地，循环群）的商群仍为阿贝尔群（相应地，循环群），立即可得。

**定理 1.12。** *设 $K$ 为 $k$ 的伽罗瓦扩张，$F$ 为任意扩张，并假设 $K,F$ 是某个域的子域。那么 $KF$ 在 $F$ 上是伽罗瓦扩张，$K$ 在 $K\cap F$ 上也是伽罗瓦扩张。设 $H$ 为 $KF$ 在 $F$ 上的伽罗瓦群，$G$ 为 $K$ 在 $k$ 上的伽罗瓦群。如果 $\sigma\in H$，则 $\sigma$ 在 $K$ 上的限制属于 $G$，而映射*

$$
\sigma\mapsto\sigma|K
$$

*给出 $H$ 到 $K$ 在 $K\cap F$ 上的伽罗瓦群的同构。*

*证明。* 设 $\sigma\in H$。$\sigma$ 在 $K$ 上的限制是 $K$ 的一个 $k$-嵌入；由于 $K$ 在 $k$ 上正规，它属于 $G$。映射 $\sigma\mapsto\sigma|K$ 显然是同态。如果 $\sigma|K$ 是恒等映射，那么 $\sigma$ 必为 $KF$ 的恒等映射（因为 $KF$ 的每个元素都可以表示为 $K$ 和 $F$ 中元素的和、积、商的组合）。因此，同态 $\sigma\mapsto\sigma|K$ 是单射。设 $H'$ 为其像。那么 $H'$ 固定 $K\cap F$；反过来，如果元素 $\alpha\in K$ 被 $H'$ 固定，则它也被 $H$ 固定，所以 $\alpha\in F$，且 $\alpha\in K\cap F$。因此 $K\cap F$ 是不动域。如果 $K$ 在 $k$ 上有限，甚至只要 $KF$ 在 $F$ 上有限，就由定理 1.8 知道 $H'$ 是 $K$ 在 $K\cap F$ 上的伽罗瓦群，该情形下定理得证。

（在无限情形中，还须补充：对于 Krull 拓扑，映射 $\sigma\mapsto\sigma|K$ 是连续的，因此由于 $H$ 紧，其像为闭集。参见定理 14.1；第 I 章定理 10.1；以及习题 43。）

<span class="original-page-anchor" id="pdf-page-281" aria-hidden="true"></span>

说明定理 1.12 的图如下：

![定理 1.12 的域图：KF 在 K 与 F 上方，二者下方为 K 与 F 的交，底端为 k；H 标在 KF/F 一边。](/library/volume-86/diagrams/pdf-0281-compositum.png)

把平行四边形的对边看成相等，会得到有启发性的理解。

**推论 1.13。** *设 $K$ 为 $k$ 的有限伽罗瓦扩张，$F$ 为 $k$ 的任意扩张。那么 $[KF:F]$ 整除 $[K:k]$。*

*证明。* 沿用上述记号，$H$ 的阶整除 $G$ 的阶，故断言成立。

**提醒。** 如果 $K$ 在 $k$ 上不是伽罗瓦扩张，这个推论的断言通常不成立。例如，设 $\alpha=\sqrt[3]{2}$ 为 $2$ 的实立方根，$\zeta$ 为 $1$ 的一个立方根，且 $\zeta\ne1$，例如

$$
\zeta=\frac{-1+\sqrt{-3}}2,
$$

并令 $\beta=\zeta\alpha$。设 $E=\mathbf{Q}(\beta)$。因为 $\beta$ 为非实复数而 $\alpha$ 为实数，所以

$$
\mathbf{Q}(\beta)\ne\mathbf{Q}(\alpha).
$$

令 $F=\mathbf{Q}(\alpha)$。那么 $E\cap F$ 是 $E$ 的一个子域，它在 $\mathbf{Q}$ 上的次数整除 $3$。因此这个次数是 $3$ 或 $1$；由于 $E\ne F$，只能是 $1$。但是

$$
EF=\mathbf{Q}(\alpha,\beta)=\mathbf{Q}(\alpha,\zeta)=\mathbf{Q}(\alpha,\sqrt{-3}).
$$

所以 $EF$ 在 $F$ 上的次数为 $2$。

**定理 1.14。** *设 $K_1$ 和 $K_2$ 为域 $k$ 的伽罗瓦扩张，其伽罗瓦群分别为 $G_1$ 和 $G_2$。假设 $K_1,K_2$ 是某个域的子域。那么 $K_1K_2$ 在 $k$ 上是伽罗瓦扩张。设 $G$ 为其伽罗瓦群。用限制定义映射 $G\to G_1\times G_2$，即*

$$
\sigma\mapsto(\sigma|K_1,\sigma|K_2).
$$

*这个映射是单射。如果 $K_1\cap K_2=k$，那么这个映射是同构。*

<span class="original-page-anchor" id="pdf-page-282" aria-hidden="true"></span>

*证明。* 两个域的复合域保持正规性与可分性，所以 $K_1K_2$ 在 $k$ 上是伽罗瓦扩张。我们的映射显然是从 $G$ 到 $G_1\times G_2$ 的同态。如果元素 $\sigma\in G$ 在 $K_1$ 和 $K_2$ 上诱导恒等映射，那么它在二者的复合域上也诱导恒等映射，所以该映射是单射。假设 $K_1\cap K_2=k$。根据定理 1.12，给定元素 $\sigma_1\in G_1$，存在 $K_1K_2$ 在 $K_2$ 上的伽罗瓦群的元素 $\sigma$，在 $K_1$ 上诱导 $\sigma_1$。这个 $\sigma$ 当然也属于 $G$，并在 $K_2$ 上诱导恒等映射。因此 $G_1\times\{e_2\}$ 包含在该同态的像中（这里 $e_2$ 为 $G_2$ 的单位元）。类似地，$\{e_1\}\times G_2$ 也包含在该像中。故它们的积包含在像中，而它们的积恰为 $G_1\times G_2$。定理 1.14 得证。

![复合域图：K_1 K_2 在 K_1 与 K_2 上方，二者下方为它们的交，底端为 k。](/library/volume-86/diagrams/pdf-0282-two-extensions.png)

**推论 1.15。** *设 $K_1,\ldots,K_n$ 为 $k$ 的伽罗瓦扩张，伽罗瓦群分别为 $G_1,\ldots,G_n$。假设对每个 $i=1,\ldots,n-1$，都有 $K_{i+1}\cap(K_1\cdots K_i)=k$。那么 $K_1\cdots K_n$ 的伽罗瓦群以自然方式同构于乘积 $G_1\times\cdots\times G_n$。*

*证明。* 用归纳法。

**推论 1.16。** *设 $K$ 为 $k$ 的有限伽罗瓦扩张，其群为 $G$；假设 $G$ 可以写成直积 $G=G_1\times\cdots\times G_n$。令 $K_i$ 为*

$$
G_1\times\cdots\times\{1\}\times\cdots\times G_n
$$

*的不动域，其中单元素群位于第 $i$ 个位置。那么 $K_i$ 在 $k$ 上是伽罗瓦扩张，且 $K_{i+1}\cap(K_1\cdots K_i)=k$。此外，$K=K_1\cdots K_n$。*

*证明。* 根据推论 1.3，所有 $K_i$ 的复合域属于其对应子群的交，而该交显然是单位群。因此复合域等于 $K$。$G$ 的每个因子都在 $G$ 中正规，所以 $K_i$ 在 $k$ 上是伽罗瓦扩张。根据推论 1.4，正规扩张的交属于其伽罗瓦群的乘积，于是显然有 $K_{i+1}\cap(K_1\cdots K_i)=k$。

<span class="original-page-anchor" id="pdf-page-283" aria-hidden="true"></span>

**定理 1.17。** *假设所有域都包含在某个共同的域中。*

(i) *如果 $K,L$ 在 $k$ 上是阿贝尔扩张，那么复合域 $KL$ 也是如此。*

(ii) *如果 $K$ 在 $k$ 上是阿贝尔扩张，且 $E$ 为 $k$ 的任意扩张，那么 $KE$ 在 $E$ 上是阿贝尔扩张。*

(iii) *如果 $K$ 在 $k$ 上是阿贝尔扩张，且 $K\supset E\supset k$，其中 $E$ 是中间域，那么 $E$ 在 $k$ 上是阿贝尔扩张，$K$ 在 $E$ 上也是阿贝尔扩张。*

*证明。* 由定理 1.12 和定理 1.14 立即可得。

如果 $k$ 是域，则在给定的代数闭包 $k^a$ 中，$k$ 的所有阿贝尔扩张的复合域称为 $k$ 的**最大阿贝尔扩张**，记作 $k^{\mathrm{ab}}$。

**记号说明。** 我们系统地采用以下记号：

$$
k^a=k\text{ 的代数闭包};
$$

$$
k^s=k\text{ 的可分闭包};
$$

$$
k^{\mathrm{ab}}=k\text{ 的阿贝尔闭包}=\text{最大阿贝尔扩张}.
$$

我们用 $k^a$ 代替其他人采用的记号 $\bar{k}$（本书第一版也采用过该记号），以便使记号在相关概念下具有函子性。

## §2. 例子与应用

设 $k$ 为域，$f(X)$ 为 $k[X]$ 中次数 $\geqq1$ 的可分多项式。设

$$
f(X)=(X-\alpha_1)\cdots(X-\alpha_n)
$$

是它在 $k$ 上分裂域 $K$ 中的分解。设 $G$ 为 $K$ 在 $k$ 上的伽罗瓦群。我们称 $G$ 为 $f$ 在 $k$ 上的**伽罗瓦群**。$G$ 的元素置换 $f$ 的根。因此得到从 $G$ 到 $n$ 个元素上的对称群 $S_n$ 的单射同态。未必每个置换都由 $G$ 的元素给出。下面将讨论一些例子。

**例 1。二次扩张。** 设 $k$ 为域，$a\in k$。如果 $a$ 不是 $k$ 中的平方，那么多项式 $X^2-a$ 在 $k$ 中没有根，因而不可约。假设 $\operatorname{char}k\ne2$。该多项式可分（因为 $2\ne0$）；如果 $\alpha$ 是一个根，那么 $k(\alpha)$ 就是分裂域，是伽罗瓦扩张，而且其伽罗瓦群为 $2$ 阶循环群。

*反过来，给定 $k$ 的一个 $2$ 次扩张 $K$，存在 $a\in k$，使得 $K=k(\alpha)$ 且 $\alpha^2=a$。* 这是由配方及初等的二次方程求根公式得到的。只要 $k$ 的特征 $\ne2$，该公式就有效。

<span class="original-page-anchor" id="pdf-page-284" aria-hidden="true"></span>

**例 2。三次扩张。** 设 $k$ 为特征不等于 $2$ 或 $3$ 的域。令

$$
f(X)=X^3+aX+b.
$$

任意三次多项式都可以通过三次式的配方化为这种形式。假设 $f$ 在 $k$ 中没有根。那么 $f$ 不可约，因为任何非平凡分解都必有一个一次因子。设 $\alpha$ 为 $f(X)$ 的根。那么

$$
[k(\alpha):k]=3.
$$

设 $K$ 为分裂域。因为 $\operatorname{char}k\ne2,3$，所以 $f$ 可分。设 $G$ 为伽罗瓦群。由于 $G$ 是对称群 $S_3$ 的子群，它的阶为 $3$ 或 $6$。在后一种情形下，$k(\alpha)$ 在 $k$ 上不正规。

有一种简单的方法来判断伽罗瓦群是否为整个对称群：考察判别式。如果 $\alpha_1,\alpha_2,\alpha_3$ 是 $f(X)$ 的三个不同的根，令

$$
\delta=(\alpha_1-\alpha_2)(\alpha_2-\alpha_3)(\alpha_1-\alpha_3)\quad\text{且}\quad\Delta=\delta^2.
$$

如果 $G$ 为伽罗瓦群，$\sigma\in G$，则 $\sigma(\delta)=\pm\delta$。所以 $\sigma$ 固定 $\Delta$。因此 $\Delta$ 属于基域 $k$；而在第 IV 章 §6 中，我们已经看到

$$
\Delta=-4a^3-27b^2.
$$

$G$ 中固定 $\delta$ 的 $\sigma$ 的集合，恰为偶置换的集合。因此 $G$ 是对称群，当且仅当 $\Delta$ 不是 $k$ 中的平方。上述说明可以归纳如下。

*设 $f(X)$ 为 $k[X]$ 中的三次多项式，且 $\operatorname{char}k\ne2,3$。那么：*

(a) *$f$ 在 $k$ 上不可约，当且仅当它在 $k$ 中没有根。*

(b) *假设 $f$ 不可约。那么 $f$ 的伽罗瓦群为 $S_3$，当且仅当 $f$ 的判别式不是 $k$ 中的平方。如果判别式是平方，那么伽罗瓦群为 $3$ 阶循环群；将其视为对 $f$ 的根的置换群时，它就是交错群 $A_3$。*

例如，考察有理数域上的

$$
f(X)=X^3-X+1.
$$

任意有理根只能是 $1$ 或 $-1$，所以 $f(X)$ 在 $\mathbf{Q}$ 上不可约。判别式为 $-23$，不是平方。因此伽罗瓦群为对称群。分裂域包含一个二次子域，即 $k(\delta)=k(\sqrt{\Delta})$。

另一方面，令 $f(X)=X^3-3X+1$。$f$ 在 $\mathbf{Z}$ 中没有根，因而在 $\mathbf{Q}$ 中没有根，所以不可约。判别式为 $81$，是一个平方，因此伽罗瓦群为 $3$ 阶循环群。

**例 3。** 考察有理数域 $\mathbf{Q}$ 上的多项式 $f(X)=X^4-2$。根据 Eisenstein 判别法，它不可约。设 $\alpha$ 为一个实根。

<span class="original-page-anchor" id="pdf-page-285" aria-hidden="true"></span>

令 $i=\sqrt{-1}$。那么 $\pm\alpha$ 和 $\pm i\alpha$ 是 $f(X)$ 的四个根，并且

$$
[\mathbf{Q}(\alpha):\mathbf{Q}]=4.
$$

因此 $f(X)$ 的分裂域为

$$
K=\mathbf{Q}(\alpha,i).
$$

域 $\mathbf{Q}(\alpha)\cap\mathbf{Q}(i)$ 在 $\mathbf{Q}$ 上的次数是 $1$ 或 $2$。次数不可能为 $2$，否则 $i\in\mathbf{Q}(\alpha)$，而 $\alpha$ 为实数，故不可能。因此次数为 $1$。所以 $i$ 在 $\mathbf{Q}(\alpha)$ 上的次数为 $2$，从而 $[K:\mathbf{Q}]=8$。$f(X)$ 的伽罗瓦群的阶为 $8$。

存在一个固定 $\mathbf{Q}(\alpha)$、把 $i$ 映到 $-i$ 的 $K$ 的自同构 $\tau$，因为 $K$ 在 $\mathbf{Q}(\alpha)$ 上是 $2$ 次伽罗瓦扩张。于是 $\tau^2=\mathrm{id}$。

![Q(alpha,i) 的次数图：到 Q(alpha) 的次数为 2，到 Q(i) 的次数为 4，后二域到 Q 的次数分别为 4 和 2。](/library/volume-86/diagrams/pdf-0285-degrees.png)

由域塔中次数的乘法性可知，各次数如图所示。因此 $X^4-2$ 在 $\mathbf{Q}(i)$ 上不可约。而且 $K$ 在 $\mathbf{Q}(i)$ 上正规。存在 $K$ 在 $\mathbf{Q}(i)$ 上的自同构 $\sigma$，把 $X^4-2$ 的根 $\alpha$ 映到根 $i\alpha$。立即可以验证 $1,\sigma,\sigma^2,\sigma^3$ 两两不同，且 $\sigma^4=\mathrm{id}$。所以 $\sigma$ 生成一个 $4$ 阶循环群，记作 $\langle\sigma\rangle$。因为 $\tau\notin\langle\sigma\rangle$，且 $\langle\sigma\rangle$ 的指数为 $2$，所以 $G=\langle\sigma,\tau\rangle$ 由 $\sigma$ 与 $\tau$ 生成。此外，可以直接验证

$$
\tau\sigma=\sigma^3\tau,
$$

因为把该关系作用于在 $\mathbf{Q}$ 上生成 $K$ 的 $\alpha$ 和 $i$ 时，关系成立。这就确定了 $G$ 的结构。随后容易验证，其子群格如下：

![该 8 阶伽罗瓦群的完整子群格，保留全部子群标记。](/library/volume-86/diagrams/pdf-0285-subgroup-lattice.png)

<span class="original-page-anchor" id="pdf-page-286" aria-hidden="true"></span>

**例 4。** 设 $k$ 为域，$t_1,\ldots,t_n$ 在 $k$ 上代数独立。令 $K=k(t_1,\ldots,t_n)$。$n$ 个字母上的对称群 $G$ 通过置换 $(t_1,\ldots,t_n)$ 作用于 $K$；它的不动域是对称函数域，即按定义由 $K$ 中被 $G$ 固定的元素组成的域。设 $s_1,\ldots,s_n$ 为初等对称多项式，并令

$$
f(X)=\prod_{i=1}^n(X-t_i).
$$

除去符号差异，$f$ 的系数就是 $s_1,\ldots,s_n$。令 $F=K^G$。我们断言 $F=k(s_1,\ldots,s_n)$。事实上，

$$
k(s_1,\ldots,s_n)\subset F.
$$

另一方面，$K$ 为 $f(X)$ 的分裂域，且在 $F$ 上的次数为 $n!$。它在 $k(s_1,\ldots,s_n)$ 上的次数 $\leqq n!$，因此必有等式 $F=k(s_1,\ldots,s_n)$。上述多项式 $f(X)$ 称为 $n$ 次一般多项式。我们刚刚构造出了一个以对称群为伽罗瓦群的伽罗瓦扩张。

用 Hilbert 不可约性定理，可以构造出 $\mathbf{Q}$ 的一个以对称群为伽罗瓦群的伽罗瓦扩张。（参见第 VII 章 §2 结尾，以及 [La 83] 第 IX 章。）给定任意有限群 $G$，是否存在一个以 $G$ 为伽罗瓦群的 $\mathbf{Q}$ 的伽罗瓦扩张，仍属未知。Emmy Noether 指出，通过参数特殊化，如果知道每个满足

$$
\mathbf{Q}(s_1,\ldots,s_n)\subset E\subset\mathbf{Q}(t_1,\ldots,t_n)
$$

的域 $E$ 都同构于由 $n$ 个代数独立元素生成的域，就能够证明这一点。不过，事情并不如此简单，因为 Swan 证明，对称群的循环子群的不动域，不一定由 $k$ 上的代数独立元素生成 [Sw 69]、[Sw 83]。

**例 5。** *我们将证明复数域是代数闭的。* 这将说明前面已经证明的几乎所有定理。

我们使用实数域 $\mathbf{R}$ 的以下性质：它是有序域，每个正元素都是平方，且 $\mathbf{R}[X]$ 中每个奇数次多项式都在 $\mathbf{R}$ 中有根。稍后将讨论一般的有序域，而这里的论证适用于具有上述性质的任意有序域。

令 $i=\sqrt{-1}$（即 $X^2+1$ 的一个根）。$\mathbf{R}(i)$ 中的每个元素都有平方根。如果 $a+bi\in\mathbf{R}(i)$，$a,b\in\mathbf{R}$，则一个平方根为 $c+di$，其中

$$
c^2=\frac{a+\sqrt{a^2+b^2}}2\quad\text{且}\quad
d^2=\frac{-a+\sqrt{a^2+b^2}}2.
$$

两个等式右端的元素都非负，因此在 $\mathbf{R}$ 中有平方根。随后容易确定 $c$ 和 $d$ 的符号，使得 $(c+di)^2=a+bi$。

> **译校注。** 原书此处写作“positive”（正），严格说应为“nonnegative”（非负）：例如 $b=0$ 时，某个右端可能为 $0$。两个陈列公式正确；译文修正了这一用词。

<span class="original-page-anchor" id="pdf-page-287" aria-hidden="true"></span>

因为 $\mathbf{R}$ 的特征为 $0$，每个有限扩张都可分。$\mathbf{R}(i)$ 的每个有限扩张都包含在某个在 $\mathbf{R}$ 上有限且伽罗瓦的扩张 $K$ 中。我们须证明 $K=\mathbf{R}(i)$。设 $G$ 为在 $\mathbf{R}$ 上的伽罗瓦群，$H$ 为 $G$ 的一个 $2$-西洛子群，$F$ 为它的不动域。通过计算次数与群的阶，可知 $F$ 在 $\mathbf{R}$ 上的次数为奇数。由本原元定理，存在元素 $\alpha\in F$，使得 $F=\mathbf{R}(\alpha)$。于是 $\alpha$ 是 $\mathbf{R}[X]$ 中某个奇数次不可约多项式的根。这只能发生在次数为 $1$ 时。因此 $G=H$ 是 $2$-群。

现在可知 $K$ 在 $\mathbf{R}(i)$ 上是伽罗瓦扩张。设 $G_1$ 为其伽罗瓦群。由于 $G_1$ 是 $p$-群（$p=2$），如果 $G_1$ 不是平凡群，就有一个指数为 $2$ 的子群 $G_2$。设 $F$ 为 $G_2$ 的不动域。那么 $F$ 在 $\mathbf{R}(i)$ 上的次数为 $2$，即为二次扩张。但我们已证明 $\mathbf{R}(i)$ 的每个元素都有平方根，因此 $\mathbf{R}(i)$ 没有二次扩张。所以 $G_1$ 是平凡群，$K=\mathbf{R}(i)$，这就是所需的结论。

（上述证明的基本思想在 Gauss 的工作中已经出现。这里选取的变体特别有效地使用了西洛群，这归功于 Artin。）

**例 6。** 设 $f(X)$ 为域 $k$ 上的不可约多项式，并假设 $f$ 可分。那么分裂域的伽罗瓦群 $G$ 表示为 $n$ 个根上的置换群，其中 $n=\deg f$。只要有一个判定该群是否为整个对称群 $S_n$ 的准则，就可以考察它是否适用于 $G$ 的这个表示。例如，一个简单的习题（参见第 I 章习题 38）表明，对于素数 $p$，$S_p$ 由 $[123\cdots p]$ 和任意一个对换生成。于是有如下结论。

*设 $f(X)$ 为有理系数不可约多项式，次数为素数 $p$。如果 $f$ 在复数中恰有两个非实根，那么 $f$ 的伽罗瓦群为 $S_p$。*

*证明。* $G$ 的阶被 $p$ 整除，所以根据西洛定理，$G$ 包含一个 $p$ 阶元素。因为 $G$ 是阶为 $p!$ 的 $S_p$ 的子群，适当排列各根后，$p$ 阶元素可以表示为 $p$-循环 $[123\cdots p]$，因为较短循环的阶小于 $p$，因而与 $p$ 互素。而那一对共轭复根表明，复共轭在 $G$ 中诱导一个对换。所以该群就是整个 $S_p$。

容易给出一个具体例子。作出

$$
f(X)=X^5-4X+2
$$

的图像，可以看出 $f$ 恰有三个实根，因而恰有两个共轭复根。此外，根据 Eisenstein 判别法，$f$ 在 $\mathbf{Q}$ 上不可约，所以应用上面证明的一般结论可知，$f$ 在 $\mathbf{Q}$ 上的伽罗瓦群为 $S_5$。另见第 IV 章习题 17。

<span class="original-page-anchor" id="pdf-page-288" aria-hidden="true"></span>

**例 7。** 上一个例子通过转到基域的某个扩张域、找出一些子群来确定伽罗瓦群。$\mathbf{Q}$ 的扩张不只有实数域，还有其他选择，例如本书后面将讨论的 $p$-进域。不过，也可以不转到扩张域，而采用模 $p$ 约化。为目前的目的，我们暂且采用下面的结论，它将在第 VII 章定理 2.9 中证明。

*设 $f(X)\in\mathbf{Z}[X]$ 为整系数多项式，首项系数为 $1$。设 $p$ 为素数，$\bar{f}(X)=f(X)\bmod p$ 为把系数模 $p$ 约化所得的多项式。假设 $\bar{f}$ 在 $\mathbf{F}_p$ 的代数闭包中没有重根。那么存在双射*

$$
(\alpha_1,\ldots,\alpha_n)\mapsto(\bar{\alpha}_1,\ldots,\bar{\alpha}_n),
$$

*把 $f$ 的根映到 $\bar{f}$ 的根；还存在把 $\bar{f}$ 的伽罗瓦群嵌入为 $f$ 的伽罗瓦群的子群的嵌入，它给出这些群在根集合上的作用的同构。*

第 VII 章将使这个嵌入的含义精确化，这里只想利用此结果计算伽罗瓦群。

例如，考察 $\mathbf{Z}$ 上的 $X^5-X-1$。模 $5$ 约化表明该多项式不可约。模 $2$ 约化给出不可约因子

$$
(X^2+X+1)(X^3+X^2+1)\quad(\bmod 2).
$$

所以在有理数域上的伽罗瓦群包含一个 $5$-循环，以及一个 $2$-循环与一个 $3$-循环的乘积。后一乘积的三次幂是一个 $2$-循环，即对换。因此伽罗瓦群包含一个对换和循环 $[12345]$，它们生成 $S_5$（参见第 I 章关于对称群的习题）。故 $X^5-X-1$ 的伽罗瓦群为 $S_5$。

**例 8。** Schur 利用模素数约化、在伽罗瓦群中获得许多元素的方法，确定了经典多项式的伽罗瓦群 [Schur 31]。例如，Schur 证明，下面这些 $\mathbf{Q}$ 上多项式在 $\mathbf{Q}$ 上的伽罗瓦群为对称群：

(a) $f(X)=\displaystyle\sum_{m=0}^nX^m/m!$（即截断的指数级数），其中 $n$ 不被 $4$ 整除。如果 $n$ 被 $4$ 整除，则得到交错群。

(b) 设

$$
H_m(X)=(-1)^me^{X^2/2}\frac{d^m}{dX^m}(e^{-X^2/2})
$$

为第 $m$ 个 Hermite 多项式。令

$$
H_{2n}(X)=K_n^{(0)}(X^2)\quad\text{且}\quad H_{2n+1}(X)=XK_n^{(1)}(X^2).
$$

那么，当 $n>12$ 时，$K_n^{(i)}(X)$ 在 $\mathbf{Q}$ 上的伽罗瓦群为对称群 $S_n$，其中 $i=0,1$。其余情形由 [Schulz 37] 解决。

<span class="original-page-anchor" id="pdf-page-289" aria-hidden="true"></span>

**例 9。** 这个例子面向略懂黎曼曲面和覆盖的读者。设 $t$ 在复数域 $\mathbf{C}$ 上超越，并令 $k=\mathbf{C}(t)$。$t$ 在 $\mathbf{C}$ 中的取值，以及值 $\infty$，对应于视作黎曼曲面的 Gauss 球面 $S$ 上的点。设 $P_1,\ldots,P_{n+1}$ 为 $S$ 上不同的点。$S-\{P_1,\ldots,P_{n+1}\}$ 的有限覆盖，与 $\mathbf{C}(t)$ 的某些有限扩张一一对应，这些扩张在 $P_1,\ldots,P_{n+1}$ 之外不分歧。设 $K$ 为对应于这些覆盖的所有扩张域的并，并以 $\pi_1^{(n)}$ 表示

$$
S-\{P_1,\ldots,P_{n+1}\}
$$

的基本群。

已知 $\pi_1^{(n)}$ 是一个以 $n$ 个生成元生成的自由群，并且可以嵌入到 $K$ 在 $\mathbf{C}(t)$ 上的伽罗瓦群中，使得 $K$ 中在 $\mathbf{C}(t)$ 上有限的子域，与 $\pi_1^{(n)}$ 的有限指数子群一一对应。给定由 $n$ 个元素 $\sigma_1,\ldots,\sigma_n$ 生成的有限群 $G$，可以找到满射同态 $\pi_1^{(n)}\to G$，把 $\pi_1^{(n)}$ 的生成元映到 $\sigma_1,\ldots,\sigma_n$。设 $H$ 为其核。那么 $H$ 对应于 $K$ 的子域 $K^H$，该子域在 $\mathbf{C}(t)$ 上正规，伽罗瓦群为 $G$。用覆盖的语言说，$H$ 对应于

$$
S-\{P_1,\ldots,P_{n+1}\}
$$

的一个有限覆盖。

在域 $\mathbf{C}(t)$ 上，可以利用解析方法确定伽罗瓦群。Douady [Dou 64] 证明，这个伽罗瓦群是自由群的完备化。关于向特征 $p$ 的推广，参见 [Pop 95]。一个基本问题是确定 $\mathbf{Q}(t)$ 上的伽罗瓦群，这需要更深入地理解该域的数论性质。Belyi [Be 80]、[Be 83] 作出了基本贡献，他还考虑了域 $\mathbf{Q}(\mu)(t)$，其中 $\mathbf{Q}(\mu)$ 是在有理数域上添加所有单位根所得的域。Belyi 证明，在后一域上，基本上所有经典有限群都可作为伽罗瓦群出现。另见下面的猜想 14.2。

关于 $\mathbf{Q}(t)$ 上的伽罗瓦群，参见含有参考文献目录的综述 [Se 88]。一种方法称为刚性方法，最先由 Shih [Shi 74] 应用；这里作简要介绍，因为它展示了本书各处定义的多种概念。问题是将带有给定伽罗瓦群 $G$ 的 $\mathbf{C}(t)$ 的扩张下降到带有相同伽罗瓦群的 $\mathbf{Q}(t)$ 的扩张。如果该扩张是 $K/\mathbf{Q}(t)$，还希望它在 $\mathbf{Q}$ 上为正则扩张（定义见第 VIII 章 §4）。为给出一个充分条件，需要一些定义。设 $G$ 为中心平凡的有限群，$C_1,C_2,C_3$ 为共轭类。令 $P=P(C_1,C_2,C_3)$ 为满足 $g_1g_2g_3=1$ 的元素

$$
(g_1,g_2,g_3)\in C_1\times C_2\times C_3
$$

组成的集合。设 $P'$ 为 $P$ 中所有满足 $G$ 由 $g_1,g_2,g_3$ 生成的元素 $(g_1,g_2,g_3)$ 组成的子集。如果 $G$ 在 $P'$ 上传递作用，且 $P'$ 非空，就称族 $(C_1,C_2,C_3)$ 是**刚性的**。

<span class="original-page-anchor" id="pdf-page-290" aria-hidden="true"></span>

如果对于 $g\in C$ 以及与 $g$ 的阶互素的正整数 $s$，都有 $g^s\in C$，就称 $G$ 的共轭类 $C$ 为**有理的**。（假设读者熟悉第 XVIII 章定义的特征标术语，那么这个有理性条件等价于：$G$ 的每个特征标 $\chi$ 在 $C$ 上的值都属于有理数域 $\mathbf{Q}$。）于是有下列定理，它包含在 Shih、Fried、Belyi、Matzat 和 Thompson 的工作中。

> **译校注。** 原书括号内写作“every character $\chi$ of $G$ has values in the rational numbers $\mathbf{Q}$”，省略了取值范围“on $C$”。这里讨论的是一个共轭类的有理性，正确的等价条件为 $\chi(g)\in\mathbf{Q}$ 对所有特征标 $\chi$ 及 $g\in C$ 成立，而非要求所有特征标在整个 $G$ 上均有理。译文补出了“在 $C$ 上”。

**刚性定理。** *设 $G$ 为中心平凡的有限群，$C_1,C_2,C_3$ 为有理共轭类，并且族 $(C_1,C_2,C_3)$ 是刚性的。那么存在一个以 $G$ 为伽罗瓦群的 $\mathbf{Q}(t)$ 的伽罗瓦扩张（而且该扩张在 $\mathbf{Q}$ 上正则）。*

### 参考文献

[Be 80] G. Belyi，Galois extensions of the maximal cyclotomic field（最大分圆域的伽罗瓦扩张），*Izv. Akad. Nauk SSR* **43**（1979），第 267–276 页（= *Math. USSR Izv.* **14**（1980），第 247–256 页）。

[Be 83] G. Belyi，On extensions of the maximal cyclotomic field having a given classical Galois group（具有给定经典伽罗瓦群的最大分圆域扩张），*J. reine angew. Math.* **341**（1983），第 147–156 页。

[Dou 64] A. Douady，Détermination d’un groupe de Galois（一个伽罗瓦群的确定），*C.R. Acad. Sci.* **258**（1964），第 5305–5308 页。

[La 83] S. Lang，*Fundamentals of Diophantine Geometry*（《丢番图几何基础》），Springer Verlag，1983 年。

[Pop 95] F. Pop，Etale Galois covers of affine smooth curves（仿射光滑曲线的平展伽罗瓦覆盖），*Invent. Math.* **120**（1995），第 555–578 页。

[Se 88] J.-P. Serre，Groupes de Galois sur $\mathbf{Q}$（$\mathbf{Q}$ 上的伽罗瓦群），*Séminaire Bourbaki*，1987–1988，*Astérisque* **161–162**，第 73–85 页。

[Shi 74] R.-Y. Shih，On the construction of Galois extensions of function fields and number fields（函数域与数域的伽罗瓦扩张的构造），*Math. Ann.* **207**（1974），第 99–120 页。

[Sw 69] R. Swan，Invariant rational functions and a problem of Steenrod（不变有理函数与 Steenrod 的一个问题），*Invent. Math.* **7**（1969），第 148–158 页。

[Sw 83] R. Swan，Noether’s problem in Galois theory（伽罗瓦理论中的 Noether 问题），载 *Emmy Noether in Bryn Mawr*，J. D. Sally、B. Srinivasan 编，Springer Verlag，1983 年，第 40 页。

## §3. 单位根

设 $k$ 为域。所谓（$k$ 中的）**单位根**，是指满足对某个整数 $n\geqq1$ 有 $\zeta^n=1$ 的元素 $\zeta\in k$。如果 $k$ 的特征为 $p$，那么方程

$$
X^{p^m}=1
$$

只有一个根，即 $1$；因此除 $1$ 之外，没有 $p^m$ 次单位根。

<span class="original-page-anchor" id="pdf-page-291" aria-hidden="true"></span>

设 $n$ 为整数，$n>1$，并且不被特征整除。多项式

$$
X^n-1
$$

是可分的，因为其导数为 $nX^{n-1}\ne0$，导数唯一的根为 $0$，所以二者没有共同根。因此在 $k^a$ 中，多项式 $X^n-1$ 有 $n$ 个不同的根，它们都是单位根。它们显然构成一个群；而我们知道，域中的每个有限乘法群都是循环群（第 IV 章定理 1.9）。因此 $n$ 次单位根群是循环群。这个群的生成元称为**本原** $n$ 次单位根。

如果 $\boldsymbol{\mu}_n$ 表示 $k^a$ 中所有 $n$ 次单位根构成的群，且 $m,n$ 为互素整数，那么

$$
\boldsymbol{\mu}_{mn}\approx\boldsymbol{\mu}_m\times\boldsymbol{\mu}_n.
$$

这是因为 $\boldsymbol{\mu}_m,\boldsymbol{\mu}_n$ 除 $1$ 外不能有共同元素，因而 $\boldsymbol{\mu}_m\boldsymbol{\mu}_n$ 有 $mn$ 个元素，每个都是 $mn$ 次单位根。所以 $\boldsymbol{\mu}_m\boldsymbol{\mu}_n=\boldsymbol{\mu}_{mn}$，且此分解为直积分解。

> **译校注。** 上述“有 $mn$ 个元素”的计数沿用 $m,n$ 都不被特征整除的前提；原书本段只明说二者互素。如果特征 $p$ 整除其中之一，单位根的个数应取该整数的素于 $p$ 部分。不过显示的直积同构以及群乘积等式仍成立。

在记号上，为避免双重下标，尤其是在素数幂的情形下，我们用 $\boldsymbol{\mu}[n]$ 代替 $\boldsymbol{\mu}_n$。因此，若 $p$ 为素数，则 $\boldsymbol{\mu}[p^r]$ 为 $p^r$ 次单位根群。$\boldsymbol{\mu}[p^\infty]$ 表示所有正整数 $r$ 所对应的 $\boldsymbol{\mu}[p^r]$ 的并。参见 §14 中的说明。

设 $k$ 为任意域，$n$ 不被特征 $p$ 整除。设 $\zeta=\zeta_n$ 为 $k^a$ 中的一个本原 $n$ 次单位根，$\sigma$ 为从 $k(\zeta)$ 到 $k^a$ 的一个 $k$-嵌入。那么

$$
(\sigma\zeta)^n=\sigma(\zeta^n)=1,
$$

所以 $\sigma\zeta$ 也是 $n$ 次单位根。因此，对于某个模 $n$ 唯一确定的整数 $i=i(\sigma)$，有 $\sigma\zeta=\zeta^i$。所以 $\sigma$ 把 $k(\zeta)$ 映到自身中，故 $k(\zeta)$ 在 $k$ 上正规。如果 $\tau$ 为 $k(\zeta)$ 在 $k$ 上的另一个自同构，那么

$$
\sigma\tau\zeta=\zeta^{i(\sigma)i(\tau)}.
$$

由于 $\sigma$ 和 $\tau$ 是自同构，$i(\sigma)$ 和 $i(\tau)$ 都与 $n$ 互素（否则 $\sigma\zeta$ 的周期将小于 $n$）。由此得到从 $k(\zeta)$ 在 $k$ 上的伽罗瓦群 $G$ 到乘法群 $(\mathbf{Z}/n\mathbf{Z})^*$ 的同态，该乘法群由模 $n$ 意义下与 $n$ 互素的整数构成。此同态显然是单射，因为 $i(\sigma)$ 由 $\sigma$ 模 $n$ 唯一确定，而 $\sigma$ 在 $k(\zeta)$ 上的作用由它在 $\zeta$ 上的作用确定。*因此，$k(\zeta)$ 在 $k$ 上是阿贝尔扩张。*

已知 $(\mathbf{Z}/n\mathbf{Z})^*$ 的阶为 $\varphi(n)$。因此次数 $[k(\zeta):k]$ 整除 $\varphi(n)$。

对于特定的域 $k$，会出现以下问题：$G_{k(\zeta)/k}$ 在 $(\mathbf{Z}/n\mathbf{Z})^*$ 中的像是否为整个 $(\mathbf{Z}/n\mathbf{Z})^*$？考察 $k=\mathbf{R}$ 或 $\mathbf{C}$，可知并非总是如此。现在给出一个确实如此的重要例子。

<span class="original-page-anchor" id="pdf-page-292" aria-hidden="true"></span>

**定理 3.1。** *设 $\zeta$ 为本原 $n$ 次单位根。那么*

$$
[\mathbf{Q}(\zeta):\mathbf{Q}]=\varphi(n),
$$

*其中 $\varphi$ 为 Euler 函数。映射 $\sigma\mapsto i(\sigma)$ 给出同构*

$$
G_{\mathbf{Q}(\zeta)/\mathbf{Q}}\xrightarrow{\approx}(\mathbf{Z}/n\mathbf{Z})^*.
$$

*证明。* 设 $f(X)$ 为 $\zeta$ 在 $\mathbf{Q}$ 上的不可约多项式。$f(X)$ 整除 $X^n-1$，设 $X^n-1=f(X)h(X)$，其中 $f,h$ 的首项系数都为 $1$。根据 Gauss 引理，$f,h$ 都具有整数系数。现在证明：若 $p$ 为不整除 $n$ 的素数，则 $\zeta^p$ 也是 $f$ 的根。因为 $\zeta^p$ 也是本原 $n$ 次单位根，而且任意本原 $n$ 次单位根都可通过对 $\zeta$ 依次取素数幂得到，其中各素数不整除 $n$；所以这将说明，所有本原 $n$ 次单位根都是 $f$ 的根。因此 $f$ 的次数必定 $\geqq\varphi(n)$，从而恰为 $\varphi(n)$。

假设 $\zeta^p$ 不是 $f$ 的根。那么 $\zeta^p$ 是 $h$ 的根，$\zeta$ 本身是 $h(X^p)$ 的根。因此 $f(X)$ 整除 $h(X^p)$，可以写成

$$
h(X^p)=f(X)g(X).
$$

由于 $f$ 为整系数多项式且首项系数为 $1$，可知 $g$ 也有整数系数。因为对任意整数 $a$ 都有 $a^p\equiv a\pmod p$，所以

$$
h(X^p)\equiv h(X)^p\quad(\bmod p),
$$

从而

$$
h(X)^p\equiv f(X)g(X)\quad(\bmod p).
$$

特别地，若用 $\bar f$ 和 $\bar h$ 表示分别将 $f,h$ 模 $p$ 约化得到的 $\mathbf{Z}/p\mathbf{Z}$ 上的多项式，则 $\bar f$ 和 $\bar h$ 不互素，即有共同因子。但 $X^n-\bar1=\bar f(X)\bar h(X)$，所以 $X^n-\bar1$ 有重根。求导即可看出这是不可能的，定理得证。

**推论 3.2。** *如果 $n,m$ 为互素的整数，且 $\geqq1$，那么*

$$
\mathbf{Q}(\zeta_n)\cap\mathbf{Q}(\zeta_m)=\mathbf{Q}.
$$

*证明。* 注意，$\zeta_n$ 和 $\zeta_m$ 都包含在 $\mathbf{Q}(\zeta_{mn})$ 中，因为 $\zeta_{mn}^n$ 为本原 $m$ 次单位根。此外，$\zeta_m\zeta_n$ 为本原 $mn$ 次单位根。因此

$$
\mathbf{Q}(\zeta_n)\mathbf{Q}(\zeta_m)=\mathbf{Q}(\zeta_{mn}).
$$

由乘法性 $\varphi(mn)=\varphi(m)\varphi(n)$ 可得断言。

假设 $n$ 为素数 $p$（与特征无关）。那么

$$
X^p-1=(X-1)(X^{p-1}+\cdots+1).
$$

<span class="original-page-anchor" id="pdf-page-293" aria-hidden="true"></span>

任意本原 $p$ 次单位根都是该等式右端第二个因子的根。因为恰有 $p-1$ 个本原 $p$ 次单位根，所以这些根恰为

$$
X^{p-1}+\cdots+1
$$

的根。

在第 IV 章 §3 中，我们看到，这个多项式可以变换为有理数域上的 Eisenstein 多项式。这给出 $[\mathbf{Q}(\zeta_p):\mathbf{Q}]=p-1$ 的另一个证明。

更仔细地考察 $X^n-1$ 的分解；为简单起见，假设特征为 $0$。

有

$$
X^n-1=\prod_\zeta(X-\zeta),
$$

其中乘积遍历所有 $n$ 次单位根。把对应于相同周期的单位根的项收集在一起。令

$$
\Phi_d(X)=\prod_{\text{周期 }\zeta=d}(X-\zeta).
$$

那么

$$
X^n-1=\prod_{d\mid n}\Phi_d(X).
$$

可以看出 $\Phi_1(X)=X-1$，而且

$$
\Phi_n(X)=\frac{X^n-1}{\displaystyle\prod_{\substack{d\mid n\\d<n}}\Phi_d(X)}.
$$

由此可以递归计算 $\Phi(X)$，并看出 $\Phi_n(X)$ 是 $\mathbf{Q}[X]$ 中的多项式，因为递归过程中除以的多项式的系数都属于 $\mathbf{Q}$。这些多项式的首项系数都为 $1$，所以根据第 IV 章定理 1.1，$\Phi_n(X)$ 实际上具有*整数系数*。因此，该构造本质上是普适的，在任意特征不整除 $n$ 的域上都适用。

称 $\Phi_n(X)$ 为第 $n$ 个**分圆多项式**。

$\Phi_n$ 的根恰为本原 $n$ 次单位根，因此

$$
\deg\Phi_n=\varphi(n).
$$

*由定理 3.1 可知，$\Phi_n$ 在 $\mathbf{Q}$ 上不可约，故*

$$
\Phi_n(X)=\operatorname{Irr}(\zeta_n,\mathbf{Q},X).
$$

<span class="original-page-anchor" id="pdf-page-294" aria-hidden="true"></span>

下列递推公式的证明留作习题：

**1。** 如果 $p$ 为素数，那么

$$
\Phi_p(X)=X^{p-1}+X^{p-2}+\cdots+1,
$$

而对于整数 $r\geqq1$，

$$
\Phi_{p^r}(X)=\Phi_p(X^{p^{r-1}}).
$$

**2。** 设正整数 $n$ 的素因子分解为 $n=p_1^{r_1}\cdots p_s^{r_s}$。那么

$$
\Phi_n(X)=\Phi_{p_1\cdots p_s}(X^{p_1^{r_1-1}\cdots p_s^{r_s-1}}).
$$

**3。** 如果 $n$ 为奇数且 $>1$，那么 $\Phi_{2n}(X)=\Phi_n(-X)$。

**4。** 如果 $p$ 为不整除 $n$ 的素数，那么

$$
\Phi_{pn}(X)=\frac{\Phi_n(X^p)}{\Phi_n(X)}.
$$

另一方面，如果 $p\mid n$，那么 $\Phi_{pn}(X)=\Phi_n(X^p)$。

**5。** 有

$$
\Phi_n(X)=\prod_{d\mid n}(X^{n/d}-1)^{\mu(d)}.
$$

照例，$\mu$ 为 Möbius 函数：

$$
\mu(n)=
\begin{cases}
0&\text{如果某个素数 }p\text{ 的平方 }p^2\text{ 整除 }n,\\
(-1)^r&\text{如果 }n=p_1\cdots p_r\text{ 为不同素数的乘积},\\
1&\text{如果 }n=1.
\end{cases}
$$

作为习题，证明

$$
\sum_{d\mid n}\mu(d)=
\begin{cases}1&\text{如果 }n=1,\\0&\text{如果 }n>1.\end{cases}
$$

**例。** 根据第 V 章习题 21，可以把对应 $n\mapsto\Phi_n(X)$ 看成从正整数到非零有理函数乘法群的函数。因此，可用卷积的一般形式体系反演乘法公式 $X^n-1=\prod\Phi_d(X)$。对若干分圆多项式的计算表明，在 $n$ 较小时，它们的系数为 $0$ 或 $\pm1$。不过，Keith Conrad 提醒我，这一问题已有大量文献，始于 Bang 在 1895 年的工作；对此我表示感谢。这里只列出最早和最后的两项：

A. S. Bang，Om Ligningen $\Phi_m(X)=0$（关于方程 $\Phi_m(X)=0$），*Nyt Tidsskrift for Matematik* **(B) 6**（1895），第 6–12 页。

H. L. Montgomery 和 R. C. Vaughn，The order of magnitude of the $m$-th coefficients of cyclotomic polynomials（分圆多项式第 $m$ 个系数的数量级），*Glasgow Math. J.* **27**（1985），第 143–159 页。

<span class="original-page-anchor" id="pdf-page-295" aria-hidden="true"></span>

特别地，若 $\Phi_n(X)=\sum a_{nj}X^j$，定义 $L(j)=\log\max_n|a_{nj}|$。那么 Montgomery 和 Vaughn 证明

$$
\frac{j^{1/2}}{(\log j)^{1/4}}\ll L(j)\ll\frac{j^{1/2}}{(\log j)^{1/4}},
$$

其中符号 $\ll$ 表示，当 $j\to\infty$ 时，左端至多等于右端乘上某个正常数。Bang 还指出，$\Phi_{105}(X)$ 是含有不等于 $0$ 或 $\pm1$ 的系数的最低次分圆多项式：$X^7$ 和 $X^{41}$ 的系数为 $-2$（其他系数均为 $0$ 或 $\pm1$）。

如果 $\zeta$ 是 $n$ 次单位根，且 $\zeta\ne1$，那么

$$
\frac{1-\zeta^n}{1-\zeta}=1+\zeta+\cdots+\zeta^{n-1}=0.
$$

这很简单，但很有用。

设 $\mathbf{F}_q$ 为有 $q$ 个元素的有限域，其中 $q$ 为奇素数 $p$ 的幂。那么 $\mathbf{F}_q^*$ 有 $q-1$ 个元素，且为循环群。因此有指数

$$
(\mathbf{F}_q^*:\mathbf{F}_q^{*2})=2.
$$

如果 $\nu$ 为不被 $p$ 整除的非零整数，令

$$
\left(\frac{\nu}{p}\right)=
\begin{cases}
1&\text{如果对某个 }x\text{ 有 }\nu\equiv x^2\quad(\bmod p),\\
-1&\text{如果对所有 }x\text{ 都有 }\nu\not\equiv x^2\quad(\bmod p).
\end{cases}
$$

它称为**二次符号**，仅依赖于 $\nu$ 模 $p$ 的剩余类。

由前面的说明可知，模 $p$ 的二次剩余与二次非剩余数量相等。

**定理 3.3。** *设 $\zeta$ 为本原 $p$ 次单位根，并令*

$$
S=\sum_\nu\left(\frac{\nu}{p}\right)\zeta^\nu,
$$

*其中求和遍历模 $p$ 的非零剩余类。那么*

$$
S^2=\left(\frac{-1}{p}\right)p.
$$

*$\mathbf{Q}$ 的每个二次扩张都包含在某个分圆扩张中。*

*证明。* 由 $\pm p$ 在 $\mathbf{Q}(\zeta)$ 中表示为一个平方的明确表达式，立即可得最后的结论，因为一个整数的平方根包含在以下<span class="original-page-anchor" id="pdf-page-296" aria-hidden="true"></span>域中：把其分解中的各素因子的平方根以及 $\sqrt{-1}$ 添加进去所得到的域。此外，对于素数 $2$，有 $(1+i)^2=2i$。现在证明关于 $S^2$ 的断言。有

$$
S^2=\sum_{\nu,\mu}\left(\frac{\nu}{p}\right)\left(\frac{\mu}{p}\right)\zeta^{\nu+\mu}
=\sum_{\nu,\mu}\left(\frac{\nu\mu}{p}\right)\zeta^{\nu+\mu}.
$$

当 $\nu$ 遍历非零剩余类时，对于固定的 $\mu$，$\nu\mu$ 也遍历非零剩余类。因此以 $\nu\mu$ 代替 $\nu$，得到

$$
\begin{aligned}
S^2&=\sum_{\nu,\mu}\left(\frac{\nu\mu^2}{p}\right)\zeta^{\mu(\nu+1)}
=\sum_{\nu,\mu}\left(\frac{\nu}{p}\right)\zeta^{\mu(\nu+1)}\\
&=\sum_\mu\left(\frac{-1}{p}\right)\zeta^0+
\sum_{\nu\ne-1}\left(\frac{\nu}{p}\right)\sum_\mu\zeta^{\mu(\nu+1)}.
\end{aligned}
$$

而 $1+\zeta+\cdots+\zeta^{p-1}=0$，所以右端关于 $\mu$ 的和等于 $-1$。因此

$$
\begin{aligned}
S^2&=\left(\frac{-1}{p}\right)(p-1)+(-1)\sum_{\nu\ne-1}\left(\frac{\nu}{p}\right)\\
&=p\left(\frac{-1}{p}\right)-\sum_\nu\left(\frac{\nu}{p}\right)\\
&=p\left(\frac{-1}{p}\right),
\end{aligned}
$$

如所需。

由此可见，$\mathbf{Q}(\sqrt p)$ 包含在 $\mathbf{Q}(\zeta,\sqrt{-1})$ 或 $\mathbf{Q}(\zeta)$ 中，具体取决于 $-1$ 的二次符号的符号。如果一个域扩张包含在通过添加单位根所得的域中，就称它为**分圆扩张**。上面已经证明，$\mathbf{Q}$ 的二次扩张是分圆扩张。Kronecker 的一个定理断言，$\mathbf{Q}$ 的每个阿贝尔扩张都是分圆扩张；但证明需要本书无法涵盖的技巧。

## §4. 特征标的线性无关性

设 $G$ 为幺半群，$K$ 为域。本章中所谓 $G$ 在 $K$ 中的**特征标**，是指从 $G$ 到 $K$ 的乘法群的同态

$$
\chi:G\to K^*.
$$

**平凡特征标**是这样的同态：

<span class="original-page-anchor" id="pdf-page-297" aria-hidden="true"></span>

恒取值 $1$。如果对于函数 $f_i:G\to K$，任何系数为 $a_i\in K$ 的关系

$$
a_1f_1+\cdots+a_nf_n=0
$$

都意味着所有 $a_i=0$，就称这些函数在 $K$ 上**线性无关**。

**例。** 本书中会在多种情境下遇到特征标。首先，一个扩张域到代数闭包中的各个共轭嵌入，可以看作特征标。它们是本章最关心的特征标。其次，在第 XVIII 章中，我们将在群表示的背景下，将下一个定理推广到更一般的特征标。

在分析中也会遇到特征标。例如，给定整数 $m$，满足 $f(x)=e^{2\pi imx}$ 的函数 $f:\mathbf{R}/\mathbf{Z}\to\mathbf{C}^*$ 是 $\mathbf{R}/\mathbf{Z}$ 上的特征标。可以证明，从 $\mathbf{R}/\mathbf{Z}$ 到 $\mathbf{C}^*$ 的所有连续同态都是这种形式。类似地，给定实数 $y$，函数 $x\mapsto e^{2\pi ixy}$ 是 $\mathbf{R}$ 上的连续特征标；Fourier 分析表明，$\mathbf{R}$ 上所有绝对值为 $1$ 的连续特征标都具有这种形式。

进一步，设 $X$ 为紧空间，$R$ 为 $X$ 上连续复值函数组成的环，$R^*$ 为 $R$ 的可逆元群。那么给定 $x\in X$，取值映射 $f\mapsto f(x)$ 是从 $R^*$ 到 $\mathbf{C}^*$ 的特征标。（实际上，这个取值映射是 $R$ 到 $\mathbf{C}$ 的满射环同态。）

Artin 找到一种简洁的表述线性无关性的方法，在下面的定理中涵盖了上述各种情形以及其他情形 [Ar 44]。

**定理 4.1。**（Artin。）*设 $G$ 为幺半群，$K$ 为域，$\chi_1,\ldots,\chi_n$ 为 $G$ 在 $K$ 中的不同特征标。那么它们在 $K$ 上线性无关。*

*证明。* 单个特征标显然线性无关。假设有关系

$$
a_1\chi_1+\cdots+a_n\chi_n=0,
$$

其中 $a_i\in K$，且不全为 $0$。选取 $n$ 尽可能小的这种关系。那么 $n\geqq2$，且每个 $a_i$ 都不为 $0$。因为 $\chi_1,\chi_2$ 不同，存在 $z\in G$，使 $\chi_1(z)\ne\chi_2(z)$。对所有 $x\in G$，有

$$
a_1\chi_1(xz)+\cdots+a_n\chi_n(xz)=0.
$$

因为 $\chi_i$ 为特征标，所以

$$
a_1\chi_1(z)\chi_1+\cdots+a_n\chi_n(z)\chi_n=0.
$$

除以 $\chi_1(z)$，再与原关系相减。项 $a_1\chi_1$ 消去，得到关系

$$
\left(a_2\frac{\chi_2(z)}{\chi_1(z)}-a_2\right)\chi_2+\cdots=0.
$$

<span class="original-page-anchor" id="pdf-page-298" aria-hidden="true"></span>

第一个系数不为 $0$，因此这是一个比原关系长度更短的关系，矛盾。

作为 Artin 定理的应用，可以考虑如下情形：$K$ 为域 $k$ 的有限正规扩张，特征标为 $K$ 在 $k$ 上的不同自同构 $\sigma_1,\ldots,\sigma_n$，把它们看作 $K^*$ 到 $K^*$ 的同态。Dedekind 已经研究过这个特例，但他以略有不同的方式表述定理：考虑由 $\sigma_i\omega_j$ 构成的行列式，其中 $\omega_j$ 是 $K$ 中适当的一组元素，并通过更复杂的方法证明该行列式不为 $0$。上述表述及其特别简洁的证明归功于 Artin。

另一个应用如下：

**推论 4.2。** *设 $\alpha_1,\ldots,\alpha_n$ 为域 $K$ 中不同的非零元素。如果 $a_1,\ldots,a_n$ 为 $K$ 的元素，并且对于所有整数 $\nu\geqq0$，都有*

$$
a_1\alpha_1^\nu+\cdots+a_n\alpha_n^\nu=0,
$$

*那么对所有 $i$，都有 $a_i=0$。*

*证明。* 将定理应用于从 $\mathbf{Z}_{\geqq0}$ 到 $K^*$ 的不同同态

$$
\nu\mapsto\alpha_i^\nu.
$$

另一个有趣的应用将作为习题给出（相对不变量）。

## §5. 范数与迹

设 $E$ 为 $k$ 的有限扩张。令 $[E:k]_s=r$；当特征为 $p>0$ 时，令

$$
p^\mu=[E:k]_i,
$$

否则令此数为 $1$。设 $\sigma_1,\ldots,\sigma_r$ 为 $E$ 到 $k$ 的代数闭包 $k^a$ 中的不同嵌入。如果 $\alpha$ 为 $E$ 的元素，定义其从 $E$ 到 $k$ 的**范数**为

$$
N_{E/k}(\alpha)=N_k^E(\alpha)
=\prod_{\nu=1}^r\sigma_\nu\alpha^{p^\mu}
=\left(\prod_{\nu=1}^r\sigma_\nu\alpha\right)^{[E:k]_i}.
$$

类似地，定义**迹**为

$$
\operatorname{Tr}_{E/k}(\alpha)=\operatorname{Tr}_k^E(\alpha)
=[E:k]_i\sum_{\nu=1}^r\sigma_\nu\alpha.
$$

如果 $[E:k]_i>1$，即 $E/k$ 不可分，那么迹等于 $0$。

<span class="original-page-anchor" id="pdf-page-299" aria-hidden="true"></span>

因此，如果 $E$ 在 $k$ 上可分，则有

$$
N_k^E(\alpha)=\prod_\sigma\sigma\alpha,
$$

其中乘积遍历 $E$ 到 $k^a$ 中的不同 $k$-嵌入。

类似地，如果 $E/k$ 可分，则

$$
\operatorname{Tr}_k^E(\alpha)=\sum_\sigma\sigma\alpha.
$$

**定理 5.1。** *设 $E/k$ 为有限扩张。那么范数 $N_k^E$ 是从 $E^*$ 到 $k^*$ 的乘法同态，迹是从 $E$ 到 $k$ 的加法同态。如果 $E\supset F\supset k$ 是域塔，则这两个映射具有传递性，即*

$$
N_k^E=N_k^F\circ N_F^E\quad\text{且}\quad
\operatorname{Tr}_k^E=\operatorname{Tr}_k^F\circ\operatorname{Tr}_F^E.
$$

*如果 $E=k(\alpha)$，且 $f(X)=\operatorname{Irr}(\alpha,k,X)=X^n+a_{n-1}X^{n-1}+\cdots+a_0$，那么*

$$
N_k^{k(\alpha)}(\alpha)=(-1)^na_0\quad\text{且}\quad
\operatorname{Tr}_k^{k(\alpha)}(\alpha)=-a_{n-1}.
$$

*证明。* 对于第一个断言，注意：若 $p^\mu=[E:k]_i$，则 $\alpha^{p^\mu}$ 在 $k$ 上可分。另一方面，乘积

$$
\prod_{\nu=1}^r\sigma_\nu\alpha^{p^\mu}
$$

在任何到 $k^a$ 中的同构下都保持不变，因为这样的同构只是置换各因子。由于 $\alpha^{p^\mu}$ 在 $k$ 上可分，该乘积必属于 $k$。对迹可采用类似的论证。

对于第二个断言，设 $\{\tau_j\}$ 为 $F$ 到 $k^a$ 中的不同 $k$-嵌入族。将每个 $\tau_j$ 延拓为 $k^a$ 的自同构，并仍以 $\tau_j$ 表示该延拓。设 $\{\sigma_i\}$ 为 $E$ 到 $k^a$ 中的 $F$-嵌入族。（不失一般性，可以假设 $E\subset k^a$。）如果 $\sigma$ 是 $E$ 到 $k^a$ 中的一个 $k$-嵌入，那么对于某个 $j$，$\tau_j^{-1}\sigma$ 固定 $F$，所以对于某个 $i$，有 $\tau_j^{-1}\sigma=\sigma_i$。因此 $\sigma=\tau_j\sigma_i$，从而族 $\{\tau_j\sigma_i\}$ 给出了 $E$ 到 $k^a$ 中的全部不同 $k$-嵌入。因为不可分次数在域塔中具有乘法性，关于范数和迹的传递性的断言就显然成立；我们已经证明 $N_F^E$ 把 $E$ 映到 $F$ 中，对迹亦然。

现在假设 $E=k(\alpha)$。若 $\alpha_1,\ldots,\alpha_r$ 为 $f$ 的不同根，则有

$$
f(X)=((X-\alpha_1)\cdots(X-\alpha_r))^{[E:k]_i}.
$$

考察 $f$ 的常数项，得到范数的表达式；考察次高次项，得到迹的表达式。

注意，迹是从 $E$ 到 $k$ 的 $k$-线性映射，即

$$
\operatorname{Tr}_k^E(c\alpha)=c\operatorname{Tr}_k^E(\alpha)
$$

<span class="original-page-anchor" id="pdf-page-300" aria-hidden="true"></span>

对所有 $\alpha\in E$ 和 $c\in k$ 都成立。这是显然的，因为 $E$ 的每个 $k$-嵌入都固定 $c$。因此迹是从 $E$ 到 $k$ 的 $k$-线性泛函。为简单起见，记 $\operatorname{Tr}=\operatorname{Tr}_k^E$。

**定理 5.2。** *设 $E$ 为 $k$ 的有限可分扩张。那么 $\operatorname{Tr}:E\to k$ 是非零泛函。映射*

$$
(x,y)\mapsto\operatorname{Tr}(xy)
$$

*从 $E\times E$ 到 $k$ 是双线性的，并把 $E$ 与其对偶空间等同起来。*

*证明。* 由特征标线性无关性定理可知 $\operatorname{Tr}$ 非零。对于每个 $x\in E$，满足 $\operatorname{Tr}_x(y)=\operatorname{Tr}(xy)$ 的映射

$$
\operatorname{Tr}_x:E\to k
$$

显然为 $k$-线性映射，而映射

$$
x\mapsto\operatorname{Tr}_x
$$

是从 $E$ 到其对偶空间 $E^\vee$ 的 $k$-同态。（我们不用 $E^*$ 表示对偶空间，因为星号用于表示 $E$ 的乘法群。）如果 $\operatorname{Tr}_x$ 是零映射，则 $\operatorname{Tr}(xE)=0$。若 $x\ne0$，则 $xE=E$。因此 $x\mapsto\operatorname{Tr}_x$ 的核为 $0$。于是得到从 $E$ 到对偶空间 $E^\vee$ 的单射同态。因为两个空间具有相同的有限维数，所以得到同构。定理得证。

**推论 5.3。** *设 $\omega_1,\ldots,\omega_n$ 为 $E$ 在 $k$ 上的一组基。那么存在 $E$ 在 $k$ 上的一组基 $\omega'_1,\ldots,\omega'_n$，使得 $\operatorname{Tr}(\omega_i\omega'_j)=\delta_{ij}$。*

*证明。* 基 $\omega'_1,\ldots,\omega'_n$ 正是讨论任意向量空间的对偶空间时所定义的对偶基。

**推论 5.4。** *设 $E$ 为 $k$ 的有限可分扩张，$\sigma_1,\ldots,\sigma_n$ 为 $E$ 到 $k^a$ 中的不同 $k$-嵌入。设 $w_1,\ldots,w_n$ 为 $E$ 的元素。那么，如果 $w_1,\ldots,w_n$ 构成 $E$ 在 $k$ 上的一组基，则向量*

$$
\begin{aligned}
\xi_1&=(\sigma_1w_1,\ldots,\sigma_1w_n),\\
&\cdots\\
\xi_n&=(\sigma_nw_1,\ldots,\sigma_nw_n)
\end{aligned}
$$

*在 $E$ 上线性无关。*

*证明。* 假设 $w_1,\ldots,w_n$ 构成 $E/k$ 的一组基。设 $\alpha_1,\ldots,\alpha_n$ 为 $E$ 的元素，且

$$
\alpha_1\xi_1+\cdots+\alpha_n\xi_n=0.
$$

于是可知

$$
\alpha_1\sigma_1+\cdots+\alpha_n\sigma_n
$$

<span class="original-page-anchor" id="pdf-page-301" aria-hidden="true"></span>

作用于每个 $w_1,\ldots,w_n$ 时，都取值 $0$。而作为从乘法群 $E^*$ 到 $k^{a*}$ 的特征标，$\sigma_1,\ldots,\sigma_n$ 线性无关。因此对 $i=1,\ldots,n$，都有 $\alpha_i=0$，故这些向量线性无关。

**注。** 在特征 $0$ 中，可以更直接地看出迹不恒为 $0$。事实上，如果 $c\in k$ 且 $c\ne0$，则 $\operatorname{Tr}(c)=nc$，其中 $n=[E:k]$，且 $n\ne0$。在特征 $p$ 中，如果 $n$ 与 $p$ 互素，这个论证同样成立。

**命题 5.5。** *设 $E=k(\alpha)$ 为可分扩张。令*

$$
f(X)=\operatorname{Irr}(\alpha,k,X),
$$

*并设 $f'(X)$ 为其导数。写成*

$$
\frac{f(X)}{(X-\alpha)}=\beta_0+\beta_1X+\cdots+\beta_{n-1}X^{n-1},
$$

*其中 $\beta_i\in E$。那么 $1,\alpha,\ldots,\alpha^{n-1}$ 的对偶基为*

$$
\frac{\beta_0}{f'(\alpha)},\ldots,\frac{\beta_{n-1}}{f'(\alpha)}.
$$

*证明。* 设 $\alpha_1,\ldots,\alpha_n$ 为 $f$ 的不同根。那么

$$
\sum_{i=1}^n\frac{f(X)}{(X-\alpha_i)}\frac{\alpha_i^r}{f'(\alpha_i)}=X^r
\quad\text{对 }0\leqq r\leqq n-1.
$$

为说明这一点，令 $g(X)$ 为此等式两端之差。那么 $g$ 的次数 $\leqq n-1$，且有 $n$ 个根 $\alpha_1,\ldots,\alpha_n$。所以 $g$ 恒为零。

多项式

$$
\frac{f(X)}{(X-\alpha_i)}\frac{\alpha_i^r}{f'(\alpha_i)}
$$

彼此共轭。如果把系数在 $E$ 中的多项式的迹定义为逐个系数取迹所得的多项式，那么

$$
\operatorname{Tr}\left[\frac{f(X)}{(X-\alpha)}\frac{\alpha^r}{f'(\alpha)}\right]=X^r.
$$

考察此等式中 $X$ 各次幂的系数，得到

$$
\operatorname{Tr}\left(\alpha^i\frac{\beta_j}{f'(\alpha)}\right)=\delta_{ij}.
$$

命题得证。

最后，建立与行列式的联系；这里假设读者知道行列式的基本性质。设 $E$ 为 $k$ 的有限扩张，把它看成 $k$ 上的有限维向量空间。对于每个 $\alpha\in E$，有一个 $k$-线性映射<span class="original-page-anchor" id="pdf-page-302" aria-hidden="true"></span>即乘以 $\alpha$：

$$
m_\alpha:E\to E,\quad\text{满足}\quad m_\alpha(x)=\alpha x.
$$

于是有行列式 $\det(m_\alpha)$，它可以由 $m_\alpha$ 关于一组基的表示矩阵 $M_\alpha$ 的行列式计算。类似地，有迹 $\operatorname{Tr}(m_\alpha)$，它是矩阵 $M_\alpha$ 的对角元素之和。

**命题 5.6。** *设 $E$ 为 $k$ 的有限扩张，$\alpha\in E$。那么*

$$
\det(m_\alpha)=N_{E/k}(\alpha)\quad\text{且}\quad
\operatorname{Tr}(m_\alpha)=\operatorname{Tr}_{E/k}(\alpha).
$$

*证明。* 令 $F=k(\alpha)$。若 $[F:k]=d$，则 $1,\alpha,\ldots,\alpha^{d-1}$ 是 $F$ 在 $k$ 上的一组基。设 $\{w_1,\ldots,w_r\}$ 是 $E$ 在 $F$ 上的一组基。那么 $\{\alpha^iw_j\}$（$i=0,\ldots,d-1$；$j=1,\ldots,r$）是 $E$ 在 $k$ 上的一组基。设

$$
f(X)=X^d+a_{d-1}X^{d-1}+\cdots+a_0
$$

为 $\alpha$ 在 $k$ 上的不可约多项式。于是 $N_{F/k}(\alpha)=(-1)^da_0$，并由范数的传递性得到

$$
N_{E/k}(\alpha)=N_{F/k}(\alpha)^r.
$$

读者可以在上述基上直接验证：$N_{F/k}(\alpha)$ 是 $m_\alpha$ 在 $F$ 上的行列式，而 $N_{F/k}(\alpha)^r$ 是 $m_\alpha$ 在 $E$ 上的行列式；行列式部分的证明完成。对迹的处理完全相同，只是使用 $\operatorname{Tr}_{E/k}(\alpha)=r\cdot\operatorname{Tr}_{F/k}(\alpha)$。$m_\alpha$ 在 $F$ 上的矩阵的迹等于 $-a_{d-1}$。由此立即可得两个迹相同，正如范数的情形一样。

## §6. 循环扩张

回顾一下，有限扩张若为伽罗瓦扩张，且其伽罗瓦群为循环群，就称为循环扩张。当基域中有足够多的单位根时，循环扩张的确定建立在下面的事实之上。

**定理 6.1。（Hilbert 第 90 定理。）** *设 $K/k$ 为 $n$ 次循环扩张，伽罗瓦群为 $G$。设 $\sigma$ 为 $G$ 的一个生成元，$\beta\in K$。范数 $N_k^K(\beta)=N(\beta)$ 等于 $1$，当且仅当 $K$ 中存在元素 $\alpha\ne0$，使得 $\beta=\alpha/\sigma\alpha$。*

*证明。* 假设这样的元素 $\alpha$ 存在。取 $\beta$ 的范数，得到 $N(\alpha)/N(\sigma\alpha)$。范数是关于 $G$ 的全部自同构的乘积，插入 $\sigma$ 只是置换这些自同构。因此范数等于 $1$。

采用以下指数记号会很方便。如果 $\tau,\tau'\in G$ 且 $\xi\in K$，写作

$$
\xi^{\tau+\tau'}=\xi^\tau\xi^{\tau'}.
$$

<span class="original-page-anchor" id="pdf-page-303" aria-hidden="true"></span>

由 Artin 的特征标定理可知，由

$$
\mathrm{id}+\beta\sigma+\beta^{1+\sigma}\sigma^2+\cdots+
\beta^{1+\sigma+\cdots+\sigma^{n-2}}\sigma^{n-1}
$$

给出的 $K$ 上的映射不恒为零。因此存在 $\theta\in K$，使元素

$$
\alpha=\theta+\beta\theta^\sigma+\beta^{1+\sigma}\theta^{\sigma^2}
+\cdots+\beta^{1+\sigma+\cdots+\sigma^{n-2}}\theta^{\sigma^{n-1}}
$$

不等于 $0$。利用 $N(\beta)=1$，可知把 $\beta\sigma$ 作用于和式的最后一项时，得到 $\theta$，因此显然有 $\beta\alpha^\sigma=\alpha$。除以 $\alpha^\sigma$，证明完成。

**定理 6.2。** *设 $k$ 为域，$n$ 为正整数，且当 $k$ 的特征非零时，$n$ 与其特征互素。假设 $k$ 中存在本原 $n$ 次单位根。*

(i) *设 $K$ 为 $n$ 次循环扩张。那么存在 $\alpha\in K$，使得 $K=k(\alpha)$，且 $\alpha$ 对于某个 $a\in k$ 满足方程 $X^n-a=0$。*

(ii) *反过来，设 $a\in k$，$\alpha$ 为 $X^n-a$ 的根。那么 $k(\alpha)$ 在 $k$ 上是循环扩张，次数为 $d$，其中 $d\mid n$，且 $\alpha^d$ 属于 $k$。*

*证明。* 设 $\zeta$ 为 $k$ 中的本原 $n$ 次单位根，$K/k$ 为循环扩张，其群为 $G$。设 $\sigma$ 为 $G$ 的生成元。有 $N(\zeta^{-1})=(\zeta^{-1})^n=1$。根据 Hilbert 第 90 定理，存在 $\alpha\in K$，使 $\sigma\alpha=\zeta\alpha$。由于 $\zeta\in k$，对 $i=1,\ldots,n$，有 $\sigma^i\alpha=\zeta^i\alpha$。因此元素 $\zeta^i\alpha$ 为 $\alpha$ 在 $k$ 上的 $n$ 个不同共轭元，从而 $[k(\alpha):k]$ 至少为 $n$。因为 $[K:k]=n$，所以 $K=k(\alpha)$。此外，

$$
\sigma(\alpha^n)=\sigma(\alpha)^n=(\zeta\alpha)^n=\alpha^n.
$$

所以 $\alpha^n$ 被 $\sigma$ 固定，因而被 $\sigma$ 的每个幂固定，从而被 $G$ 固定。因此 $\alpha^n$ 属于 $k$；令 $a=\alpha^n$，即证明了第一部分。

反过来，设 $a\in k$，$\alpha$ 为 $X^n-a$ 的根。那么对于每个 $i=1,\ldots,n$，$\alpha\zeta^i$ 也是根，故所有根都属于 $k(\alpha)$，所以 $k(\alpha)$ 在 $k$ 上正规。若 $a\ne0$，所有根都不同，因此 $k(\alpha)$ 在 $k$ 上是伽罗瓦扩张。设 $G$ 为伽罗瓦群。

> **译校注。** 原书这里直接说“All the roots are distinct”，隐含了 $a\ne0$。当 $a=0$ 时，$\alpha=0$，$k(\alpha)=k$，定理结论以 $d=1$ 立即成立。译文补出这一例外，以下论证针对 $a\ne0$。

如果 $\sigma$ 为 $k(\alpha)/k$ 的自同构，则 $\sigma\alpha$ 也是 $X^n-a$ 的根。因此 $\sigma\alpha=\omega_\sigma\alpha$，其中 $\omega_\sigma$ 为 $n$ 次单位根，未必本原。映射 $\sigma\mapsto\omega_\sigma$ 显然是从 $G$ 到 $n$ 次单位根群的同态，且为单射。由于循环群的子群仍为循环群，所以 $G$ 为 $d$ 阶循环群，且 $d\mid n$。$G$ 的像是 $d$ 阶循环群。如果 $\sigma$ 为 $G$ 的生成元，则 $\omega_\sigma$ 是本原 $d$ 次单位根。现在得到

$$
\sigma(\alpha^d)=(\sigma\alpha)^d=(\omega_\sigma\alpha)^d=\alpha^d.
$$

因此 $\alpha^d$ 被 $\sigma$ 固定，从而被 $G$ 固定。所以它属于 $k$，定理得证。

<span class="original-page-anchor" id="pdf-page-304" aria-hidden="true"></span>

现在转向特征 $p$ 中关于 $p$ 次循环扩张的 Hilbert 第 90 定理的类似结论。

**定理 6.3。（Hilbert 第 90 定理，加法形式。）** *设 $k$ 为域，$K/k$ 为 $n$ 次循环扩张，其群为 $G$。设 $\sigma$ 为 $G$ 的生成元，$\beta\in K$。迹 $\operatorname{Tr}_k^K(\beta)$ 等于 $0$，当且仅当存在元素 $\alpha\in K$，使得 $\beta=\alpha-\sigma\alpha$。*

*证明。* 如果这样的元素 $\alpha$ 存在，则迹为 $0$，因为迹等于遍历 $G$ 中所有元素的和，而作用 $\sigma$ 只是置换这些元素。

反过来，假设 $\operatorname{Tr}(\beta)=0$。存在元素 $\theta\in K$，使得 $\operatorname{Tr}(\theta)\ne0$。令

$$
\alpha=\frac1{\operatorname{Tr}(\theta)}
\left[\beta\theta^\sigma+(\beta+\sigma\beta)\theta^{\sigma^2}
+\cdots+(\beta+\sigma\beta+\cdots+\sigma^{n-2}\beta)\theta^{\sigma^{n-1}}\right].
$$

立即可得 $\beta=\alpha-\sigma\alpha$。

**定理 6.4。**（Artin-Schreier。）*设 $k$ 为特征 $p$ 的域。*

(i) *设 $K$ 为 $k$ 的 $p$ 次循环扩张。那么存在 $\alpha\in K$，使得 $K=k(\alpha)$，且 $\alpha$ 对于某个 $a\in k$ 满足方程 $X^p-X-a=0$。*

(ii) *反过来，给定 $a\in k$，多项式 $f(X)=X^p-X-a$ 要么在 $k$ 中有一个根，此时所有根都在 $k$ 中；要么不可约。在后一情形下，如果 $\alpha$ 是一个根，则 $k(\alpha)$ 在 $k$ 上是 $p$ 次循环扩张。*

*证明。* 设 $K/k$ 为 $p$ 次循环扩张。那么 $\operatorname{Tr}_k^K(-1)=0$（它就是 $-1$ 相加 $p$ 次）。设 $\sigma$ 为伽罗瓦群的生成元。根据 Hilbert 第 90 定理的加法形式，存在 $\alpha\in K$，使 $\sigma\alpha-\alpha=1$，即 $\sigma\alpha=\alpha+1$。因此，对于所有整数 $i=1,\ldots,p$，有 $\sigma^i\alpha=\alpha+i$，而 $\alpha$ 有 $p$ 个不同的共轭元。故 $[k(\alpha):k]\geqq p$，从而 $K=k(\alpha)$。注意

$$
\sigma(\alpha^p-\alpha)=\sigma(\alpha)^p-\sigma(\alpha)
=(\alpha+1)^p-(\alpha+1)=\alpha^p-\alpha.
$$

所以 $\alpha^p-\alpha$ 被 $\sigma$ 固定，因而被 $\sigma$ 的幂固定，从而被 $G$ 固定。它属于不动域 $k$。令 $a=\alpha^p-\alpha$，第一个断言得证。

反过来，设 $a\in k$。如果 $\alpha$ 是 $X^p-X-a$ 的一个根，那么对于 $i=1,\ldots,p$，$\alpha+i$ 也是根。因此 $f(X)$ 有 $p$ 个不同的根。如果一个根属于 $k$，所有根都属于 $k$。假设 $k$ 中没有根。我们断言这个<span class="original-page-anchor" id="pdf-page-305" aria-hidden="true"></span>多项式不可约。假设

$$
f(X)=g(X)h(X),
$$

其中 $g,h\in k[X]$，且 $1\leqq\deg g<p$。因为

$$
f(X)=\prod_{i=1}^p(X-\alpha-i),
$$

所以 $g(X)$ 是关于某些整数 $i$ 的乘积。令 $d=\deg g$。$g$ 中 $X^{d-1}$ 的系数是恰好 $d$ 个整数 $i$ 所对应的项 $-(\alpha+i)$ 的和。因此对于某个整数 $j$，它等于 $-d\alpha+j$。但 $d$ 在 $k$ 中不为 $0$，而 $g$ 的系数属于 $k$，所以 $\alpha\in k$，矛盾。因此 $f(X)$ 不可约。所有根都属于 $k(\alpha)$，故该域在 $k$ 上正规。因为 $f(X)$ 没有重根，$k(\alpha)$ 在 $k$ 上是伽罗瓦扩张。存在 $k(\alpha)$ 在 $k$ 上的自同构 $\sigma$，使得 $\sigma\alpha=\alpha+1$（因为 $\alpha+1$ 也是一个根）。所以 $\sigma$ 的幂 $\sigma^i$ 对 $i=1,\ldots,p$ 给出 $\sigma^i\alpha=\alpha+i$，并且两两不同。因此伽罗瓦群由这些幂组成，是循环群，定理得证。

关于 $p^r$ 次循环扩张，参见关于 Witt 向量的习题，以及 §8 结尾的参考文献。

## §7. 可解扩张与根式扩张

有限扩张 $E/k$（为方便起见，假设它可分），如果包含 $E$ 的 $k$ 的最小伽罗瓦扩张 $K$ 的伽罗瓦群是可解群，就称为**可解扩张**。这等价于存在 $k$ 的一个可解伽罗瓦扩张 $L$，使得 $k\subset E\subset L$。事实上，有 $k\subset E\subset K\subset L$，且 $G(K/k)$ 为 $G(L/k)$ 的同态像。

**命题 7.1。** *可解扩张构成扩张的一个特出类。*

*证明。* 设 $E/k$ 可解，$F$ 为包含 $k$ 的域，并假设 $E,F$ 为某个代数闭域的子域。设 $K$ 在 $k$ 上为可解伽罗瓦扩张，且 $E\subset K$。那么 $KF$ 在 $F$ 上是伽罗瓦扩张，并由定理 1.12 知 $G(KF/F)$ 是 $G(K/k)$ 的子群。因此 $EF/F$ 可解。可解扩张的子扩张显然可解。设 $E\supset F\supset k$ 为域塔，并假设 $E/F$ 和 $F/k$ 可解。取一个包含 $F$ 的 $k$ 的有限可解伽罗瓦扩张 $K$。刚才已知 $EK/K$ 可解。取一个包含 $EK$ 的 $K$ 的可解伽罗瓦扩张 $L$。如果 $\sigma$ 是 $L$ 到给定代数闭包中的任意 $k$-嵌入，那么 $\sigma K=K$，所以 $\sigma L$ 是 $K$ 的可解扩张。令 $M$ 为所有 $k$-嵌入 $\sigma$ 对应的扩张 $\sigma L$ 的复合域。

<span class="original-page-anchor" id="pdf-page-306" aria-hidden="true"></span>

那么 $M$ 在 $k$ 上是伽罗瓦扩张，因而在 $K$ 上也是伽罗瓦扩张。由定理 1.14，$M$ 在 $K$ 上的伽罗瓦群是乘积

$$
\prod_\sigma G(\sigma L/K)
$$

的子群。因此它可解。由定理 1.10，有满射同态 $G(M/k)\to G(K/k)$。所以 $M/k$ 的伽罗瓦群有一个可解正规子群，其商群也可解。因此该伽罗瓦群可解。由于 $E\subset M$，证明完成。

![域塔与复合域图：EK 在 E 和 K 上方，F 在 E 和 K 下方，再下面是 k。](/library/volume-86/diagrams/pdf-0306-solvable-tower.png)

如果 $k$ 的有限扩张 $F$ 可分，而且存在包含 $F$ 的 $k$ 的有限扩张 $E$，具有域塔分解

$$
k=E_0\subset E_1\subset E_2\subset\cdots\subset E_m=E,
$$

其中每一步 $E_{i+1}/E_i$ 都属于以下类型之一，就称 $F$ **可用根式解出**：

**1。** 通过添加一个单位根得到。

**2。** 通过添加多项式 $X^n-a$ 的一个根得到，其中 $a\in E_i$，且 $n$ 与特征互素。

**3。** 当特征为 $p>0$ 时，通过添加方程 $X^p-X-a$ 的一个根得到，其中 $a\in E_i$。

立即可知，可用根式解出的扩张构成一个特出类。

**定理 7.2。** *设 $E$ 为 $k$ 的可分扩张。那么 $E$ 可用根式解出，当且仅当 $E/k$ 可解。*

*证明。* 假设 $E/k$ 可解，并取包含 $E$ 的 $k$ 的有限可解伽罗瓦扩张 $K$。设 $m$ 为整除次数 $[K:k]$、且不等于特征的所有素数的乘积，令 $F=k(\zeta)$，其中 $\zeta$ 为本原 $m$ 次单位根。那么 $F/k$ 为阿贝尔扩张。将 $K$ 提升到 $F$ 上，则 $KF$ 在 $F$ 上可解。在 $F$ 与 $KF$ 之间存在一个中间域塔，每一步都是素数次循环扩张，因为每个可解群都有一个子群<span class="original-page-anchor" id="pdf-page-307" aria-hidden="true"></span>塔，具有相同的类型，因此可以用定理 1.10。由定理 6.2 和定理 6.4，可得 $KF$ 在 $F$ 上可用根式解出，从而在 $k$ 上也可用根式解出。因此 $E/k$ 可用根式解出。

![域图：KF 在 K 和 F 上方，k 在下方。](/library/volume-86/diagrams/pdf-0307-radical-compositum.png)

反过来，假设 $E/k$ 可用根式解出。对于 $E$ 到 $E^a$ 中的任意 $k$-嵌入 $\sigma$，扩张 $\sigma E/k$ 也可用根式解出。因此，包含 $E$ 的 $k$ 的最小伽罗瓦扩张 $K$，即 $E$ 与其各共轭域的复合域，也可用根式解出。设 $m$ 为整除次数 $[K:k]$、且不等于特征的所有素数的乘积；仍令 $F=k(\zeta)$，其中 $\zeta$ 为本原 $m$ 次单位根。只须证明 $KF$ 在 $F$ 上可解，因为这样就有 $KF$ 在 $k$ 上可解，而 $G(K/k)$ 是 $G(KF/k)$ 的同态像，因此也可解。但是，$KF/F$ 可以分解为一个扩张塔，每一步都是素数次，且属于定理 6.2 或定理 6.4 描述的类型，相应的单位根属于域 $F$。因此 $KF/F$ 可解，定理得证。

> **译校注。** 原书写作“the smallest Galois extension $K$ of $E$ containing $k$”，把基域与待包含的域颠倒了。这里是 $E$ 的伽罗瓦闭包，即“$k$ 的包含 $E$ 的最小伽罗瓦扩张”；这也与后面的“$E$ 与其共轭域的复合域”一致。译文已修正。

**注。** 可以不假设可分性，从而修改上述讨论。这时须考虑正规扩张而非伽罗瓦扩张，并且在用根式解出时，允许形如 $X^p-a$ 的方程，其中 $p$ 为特征。这时仍有与定理 7.2 对应的定理。由第 V 章 §6，证明是清楚的。

关于每个可解群都是有理数域上的伽罗瓦群的证明，参见 Shafarevich [Sh 54]，以及 Iwasawa 的贡献 [Iw 53]。

[Iw 53] K. Iwasawa，On solvable extension of algebraic number fields（代数数域的可解扩张），*Ann. of Math.* **58**（1953），第 548–572 页。

[Sh 54] I. Shafarevich，Construction of fields of algebraic numbers with given solvable Galois group（具有给定可解伽罗瓦群的代数数域的构造），*Izv. Akad. Nauk SSSR* **18**（1954），第 525–578 页（*Amer. Math. Soc. Transl.* **4**（1956），第 185–237 页）。

## §8. 阿贝尔 Kummer 理论

本节将推广关于基域中含有足够多单位根时的循环扩张的定理。

设 $k$ 为域，$m$ 为正整数。若 $k$ 的伽罗瓦扩张 $K$ 的群 $G$ 满足对所有 $\sigma\in G$ 都有 $\sigma^m=1$，就称该扩张**具有指数 $m$**。

<span class="original-page-anchor" id="pdf-page-308" aria-hidden="true"></span>

我们将研究指数为 $m$ 的阿贝尔扩张。首先假设当 $k$ 的特征非零时，$m$ 不是其倍数，并且 $k$ 包含 $m$ 次单位根群，记为 $\boldsymbol{\mu}_m$。本节假设所有代数扩张都包含在固定的代数闭包 $k^a$ 中。

设 $a\in k$。符号 $a^{1/m}$（或 $\sqrt[m]a$）不是良定义的。如果 $\alpha^m=a$，且 $\zeta$ 是 $m$ 次单位根，那么也有 $(\zeta\alpha)^m=a$。用符号 $a^{1/m}$ 表示任意这样的元素 $\alpha$，称为 $a$ 的一个 $m$ 次根。因为单位根都在基域中，无论选取 $a$ 的哪个 $m$ 次根 $\alpha$，域 $k(\alpha)$ 都相同。把该域记作 $k(a^{1/m})$。

用 $k^{*m}$ 表示 $k^*$ 中由 $k$ 的所有非零元素的 $m$ 次幂组成的子群。它是同态 $x\mapsto x^m$ 下 $k^*$ 的像。

设 $B$ 为包含 $k^{*m}$ 的 $k^*$ 的子群。用 $k(B^{1/m})$ 或 $K_B$ 表示所有满足 $a\in B$ 的域 $k(a^{1/m})$ 的复合域。作为 $k^a$ 的子域，它由 $B$ 唯一确定。

设 $a\in B$，$\alpha$ 为 $a$ 的一个 $m$ 次根。多项式 $X^m-a$ 在 $K_B$ 中分解为一次因子。因为这对所有 $a\in B$ 都成立，所以 $K_B$ 在 $k$ 上是伽罗瓦扩张。设 $G$ 为伽罗瓦群，$\sigma\in G$。那么对于某个 $m$ 次单位根 $\omega_\sigma\in\boldsymbol{\mu}_m\subset k^*$，有 $\sigma\alpha=\omega_\sigma\alpha$。映射

$$
\sigma\mapsto\omega_\sigma
$$

显然是从 $G$ 到 $\boldsymbol{\mu}_m$ 的同态，即对于 $\tau,\sigma\in G$，有

$$
\tau\sigma\alpha=\omega_\tau\omega_\sigma\alpha=\omega_\sigma\omega_\tau\alpha.
$$

可以写成 $\omega_\sigma=\sigma\alpha/\alpha$。这个单位根 $\omega_\sigma$ 与 $a$ 的 $m$ 次根的选择无关：若 $\alpha'$ 是另一个 $m$ 次根，则对于某个 $\zeta\in\boldsymbol{\mu}_m$，有 $\alpha'=\zeta\alpha$，从而

$$
\sigma\alpha'/\alpha'=\zeta\sigma\alpha/\zeta\alpha=\sigma\alpha/\alpha.
$$

把 $\omega_\sigma$ 记作 $\langle\sigma,a\rangle$。对应

$$
(\sigma,a)\mapsto\langle\sigma,a\rangle
$$

给出映射

$$
G\times B\to\boldsymbol{\mu}_m.
$$

如果 $a,b\in B$，且 $\alpha^m=a$、$\beta^m=b$，则 $(\alpha\beta)^m=ab$，并且

$$
\sigma(\alpha\beta)/\alpha\beta=(\sigma\alpha/\alpha)(\sigma\beta/\beta).
$$

因此上述映射是双线性的。此外，如果 $a\in k^{*m}$，则有 $\langle\sigma,a\rangle=1$。

**定理 8.1。** *设 $k$ 为域，$m$ 为正整数，且当 $k$ 的特征非零时，$m$ 与该特征互素。假设 $k$ 包含 $\boldsymbol{\mu}_m$。设 $B$ 为包含 $k^{*m}$ 的 $k^*$ 的子群，并令 $K_B=k(B^{1/m})$。那么 $K_B$ 是指数为 $m$ 的阿贝尔伽罗瓦扩张。设 $G$ 为其伽罗瓦群。有双线性映射*

$$
G\times B\to\boldsymbol{\mu}_m,\quad\text{由}\quad
(\sigma,a)\mapsto\langle\sigma,a\rangle\text{ 给出}.
$$

<span class="original-page-anchor" id="pdf-page-309" aria-hidden="true"></span>

*如果 $\sigma\in G$、$a\in B$，且 $\alpha^m=a$，那么 $\langle\sigma,a\rangle=\sigma\alpha/\alpha$。左核为 $1$，右核为 $k^{*m}$。扩张 $K_B/k$ 有限，当且仅当 $(B:k^{*m})$ 有限。此时*

$$
B/k^{*m}\approx G^\wedge,
$$

*特别地，有等式*

$$
[K_B:k]=(B:k^{*m}).
$$

*证明。* 设 $\sigma\in G$。假设对所有 $a\in B$，都有 $\langle\sigma,a\rangle=1$。那么对于 $K_B$ 中每个满足 $\alpha^m=a\in B$ 的生成元 $\alpha$，都有 $\sigma\alpha=\alpha$。因此 $\sigma$ 在 $K_B$ 上诱导恒等映射，左核为 $1$。设 $a\in B$，并假设对所有 $\sigma\in G$，都有 $\langle\sigma,a\rangle=1$。考虑 $K_B$ 的子域 $k(a^{1/m})$。如果 $a^{1/m}$ 不属于 $k$，则存在一个非恒等的 $k(a^{1/m})$ 的 $k$-自同构。将该自同构延拓到 $K_B$，并称此延拓为 $\sigma$。那么显然 $\langle\sigma,a\rangle\ne1$。这就证明了断言。

由第 I 章 §9 的对偶性定理可知，$G$ 有限，当且仅当 $B/k^{*m}$ 有限；此时有上述同构，特别地，$G$ 的阶等于 $(B:k^{*m})$，定理得证。

**定理 8.2。** *沿用定理 8.1 的记号。映射 $B\mapsto K_B$ 给出 $k^*$ 中包含 $k^{*m}$ 的子群的集合，与 $k$ 的指数为 $m$ 的阿贝尔扩张之间的双射。*

*证明。* 设 $B_1,B_2$ 为包含 $k^{*m}$ 的 $k^*$ 的子群。如果 $B_1\subset B_2$，则 $k(B_1^{1/m})\subset k(B_2^{1/m})$。反过来，假设 $k(B_1^{1/m})\subset k(B_2^{1/m})$。要证明 $B_1\subset B_2$。取 $b\in B_1$，则 $k(b^{1/m})\subset k(B_2^{1/m})$，且 $k(b^{1/m})$ 包含在 $k(B_2^{1/m})$ 的一个有限生成子扩张中。因此，不失一般性，可假设 $B_2/k^{*m}$ 有限生成，因而有限。设 $B_3$ 为 $k^*$ 中由 $B_2$ 和 $b$ 生成的子群。那么 $k(B_2^{1/m})=k(B_3^{1/m})$；根据上面的结论，这个域在 $k$ 上的次数恰为

$$
(B_2:k^{*m})\quad\text{或}\quad(B_3:k^{*m}).
$$

因此两个指数相等，且 $B_2=B_3$。这就证明 $B_1\subset B_2$。

现在已得到从群 $B$ 的集合到 $k$ 的指数为 $m$ 的阿贝尔扩张的集合的单射。最后假设 $K$ 是 $k$ 的指数为 $m$ 的阿贝尔扩张。任意有限子扩张都是指数为 $m$ 的循环扩张的复合域，因为任意有限阿贝尔群都是循环群的乘积，而且可以应用推论 1.16。根据定理 6.2，每个循环扩张都能通过添加一个 $m$ 次根得到。因此 $K$ 可以通过添加一个 $m$ 次根族得到，例如元素 $\{b_j\}_{j\in J}$ 的 $m$ 次根，其中 $b_j\in k^*$。设 $B$ 为 $k^*$ 中由所有 $b_j$ 和 $k^{*m}$ 生成的子群。如果 $b'=ba^m$，其中 $a,b\in k$，那么显然

$$
k(b'^{1/m})=k(b^{1/m}).
$$

所以 $k(B^{1/m})=K$，如所需。

<span class="original-page-anchor" id="pdf-page-310" aria-hidden="true"></span>

处理指数 $p$ 等于特征的阿贝尔扩张时，需要发展一个加法理论。它与定理 8.1、8.2 的关系，正如定理 6.4 与定理 6.2 的关系。

如果 $k$ 为域，对 $x\in k$，定义算子 $\wp$：

$$
\wp(x)=x^p-x.
$$

那么 $\wp$ 为 $k$ 到自身的加法同态。当 $m$ 为素数时，子群 $\wp(k)$ 在加法理论中的作用，与子群 $k^{*m}$ 在乘法理论中的作用相同。关于 $p$ 的幂的理论略为复杂，归功于 Witt。

现在假设 $k$ 的特征为 $p$。对 $a\in k$，把多项式 $X^p-X-a$ 的一个根记作 $\wp^{-1}a$。如果 $B$ 为 $k$ 的一个包含 $\wp k$ 的子群，则令 $K_B=k(\wp^{-1}B)$，即对所有 $a\in B$，向 $k$ 添加 $\wp^{-1}a$ 所得的域。强调一下，$B$ 是 $k$ 的*加法*子群。

**定理 8.3。** *设 $k$ 为特征 $p$ 的域。映射 $B\mapsto k(\wp^{-1}B)$ 给出包含 $\wp k$ 的 $k$ 的子群，与 $k$ 的指数为 $p$ 的阿贝尔扩张之间的双射。令 $K=K_B=k(\wp^{-1}B)$，并设 $G$ 为其伽罗瓦群。如果 $\sigma\in G$、$a\in B$，且 $\wp\alpha=a$，令 $\langle\sigma,a\rangle=\sigma\alpha-\alpha$。那么有双线性映射*

$$
G\times B\to\mathbf{Z}/p\mathbf{Z},\quad\text{由}\quad
(\sigma,a)\mapsto\langle\sigma,a\rangle\text{ 给出}.
$$

*左核为 $1$，右核为 $\wp k$。扩张 $K_B/k$ 有限，当且仅当 $(B:\wp k)$ 有限；此时*

$$
[K_B:k]=(B:\wp k).
$$

*证明。* 证明与定理 8.1 和定理 8.2 的证明完全类似。只须把乘法换成加法，并用“$\wp$ 次根”代替 $m$ 次根即可。除此以外，证明的措辞无需改变。

关于指数为 $p^n$ 的阿贝尔扩张的类似定理，需要 Witt 向量，将在习题中展开。

### 参考文献

[Wi 35] E. Witt，Der Existenzsatz für abelsche Funktionenkörper（阿贝尔函数域的存在定理），*J. reine angew. Math.* **173**（1935），第 43–51 页。

[Wi 36] E. Witt，Konstruktion von galoisschen Körpern der Charakteristik $p$ mit vorgegebener Gruppe der Ordung $p^f$（具有给定 $p^f$ 阶群的特征 $p$ 的伽罗瓦域的构造），*J. reine angew. Math.* **174**（1936），第 237–245 页。

[Wi 37] E. Witt，Zyklische Körper und Algebren der Charakteristik $p$ vom Grad $p^n$. Struktur diskret bewerteter perfekter Körper mit vollkommenem Restklassenkörper der Charakteristik $p$（特征 $p$、次数 $p^n$ 的循环域与代数；具有特征 $p$ 的完美剩余类域的离散赋值完美域的结构），*J. reine angew. Math.* **176**（1937），第 126–140 页。

<span class="original-page-anchor" id="pdf-page-311" aria-hidden="true"></span>

## §9. 方程 $X^n-a=0$

当单位根不在底域中时，方程 $X^n-a=0$ 仍然很有趣，不过处理起来稍微更为微妙。

**定理 9.1。** *设 $k$ 为一个域，$n$ 为整数且 $n\geqq2$。设 $a\in k$，$a\ne0$。假设对于所有满足 $p\mid n$ 的素数 $p$，都有 $a\notin k^p$；并且若 $4\mid n$，则 $a\notin-4k^4$。那么 $X^n-a$ 在 $k[X]$ 中不可约。*

*证明。* 第一个假设的含义是，$a$ 不是 $k$ 中的 $p$ 次幂。我们用归纳法把定理归结为 $n$ 是素数幂的情形。写成 $n=p^rm$，其中 $p$ 与 $m$ 互素，且 $p$ 为奇数。设

$$
X^m-a=\prod_{\nu=1}^m(X-\alpha_\nu)
$$

为 $X^m-a$ 的一次因式分解，并令 $\alpha=\alpha_1$。用 $X^{p^r}$ 代替 $X$，得到

$$
X^n-a=X^{p^rm}-a=\prod_{\nu=1}^m(X^{p^r}-\alpha_\nu).
$$

由归纳假设，可以假定 $X^m-a$ 在 $k[X]$ 中不可约。我们断言，$\alpha$ 不是 $k(\alpha)$ 中的 $p$ 次幂。否则，$\alpha=\beta^p$，其中 $\beta\in k(\alpha)$。设 $N$ 为从 $k(\alpha)$ 到 $k$ 的范数。则

$$
-a=(-1)^mN(\alpha)=(-1)^mN(\beta^p)=(-1)^mN(\beta)^p.
$$

若 $m$ 为奇数，则 $a$ 为 $p$ 次幂，这是不可能的。同样，若 $m$ 为偶数而 $p$ 为奇数，也得到矛盾。由于 $m$ 与 $p$ 互素，这就证明了我们的断言。如果已经知道定理对素数幂成立，那么可得 $X^{p^r}-\alpha$ 在 $k(\alpha)$ 上不可约。若 $A$ 为 $X^{p^r}-\alpha$ 的一个根，则 $k\subset k(\alpha)\subset k(A)$ 构成一个域塔，底层扩张的次数为 $m$，上层扩张的次数为 $p^r$。于是 $A$ 在 $k$ 上的次数为 $n$，因此 $X^n-a$ 不可约。现在假定 $n=p^r$ 为素数幂。

若 $p$ 就是特征，取 $a$ 的一个 $p$ 次根 $\alpha$。则 $X^p-a=(X-\alpha)^p$，所以当 $r\geqq2$ 时，$X^{p^r}-a=(X^{p^{r-1}}-\alpha)^p$。用一个比前面更简单的论证可见，$\alpha$ 不是 $k(\alpha)$ 中的 $p$ 次幂，所以由归纳假设，$X^{p^{r-1}}-\alpha$ 在 $k(\alpha)$ 上不可约。因此 $X^{p^r}-a$ 在 $k$ 上不可约。

假设 $p$ 不是特征。我们仍然使用归纳法，并取 $X^p-a$ 的一个根 $\alpha$。

假设 $a$ 不是 $k$ 中的 $p$ 次幂。我们断言 $X^p-a$ 不可约。否则，$X^p-a$ 的一个根 $\alpha$ 生成次数为 $d<p$ 的扩张 $k(\alpha)$，并且 $\alpha^p=a$。取从 $k(\alpha)$ 到 $k$ 的范数，得到 $N(\alpha)^p=a^d$。由于 $d$ 与 $p$ 互素，可知 $a$ 是 $k$ 中的 $p$ 次幂，矛盾。

<span class="original-page-anchor" id="pdf-page-312" aria-hidden="true"></span>

设 $r\geqq2$。令 $\alpha=\alpha_1$。有

$$
X^p-a=\prod_{\nu=1}^p(X-\alpha_\nu)
$$

以及

$$
X^{p^r}-a=\prod_{\nu=1}^p(X^{p^{r-1}}-\alpha_\nu).
$$

假定 $\alpha$ 不是 $k(\alpha)$ 中的 $p$ 次幂。设 $A$ 为 $X^{p^{r-1}}-\alpha$ 的一个根。若 $p$ 为奇数，则由归纳假设，$A$ 在 $k(\alpha)$ 上的次数为 $p^{r-1}$，因此在 $k$ 上的次数为 $p^r$，证明完成。若 $p=2$，假设 $\alpha=-4\beta^4$，其中 $\beta\in k(\alpha)$。设 $N$ 为从 $k(\alpha)$ 到 $k$ 的范数。则 $-a=N(\alpha)=16N(\beta)^4$，所以 $-a$ 是 $k$ 中的平方。由于 $p=2$，得到 $\sqrt{-1}\in k(\alpha)$，且 $\alpha=(\sqrt{-1}\,2\beta^2)^2$，矛盾。因此再用归纳法，可得 $A$ 在 $k$ 上的次数为 $p^r$。所以，下面假定对于某个 $\beta\in k(\alpha)$ 有 $\alpha=\beta^p$，并推导其后果。

取从 $k(\alpha)$ 到 $k$ 的范数，得到

$$
-a=(-1)^pN(\alpha)=(-1)^pN(\beta^p)=(-1)^pN(\beta)^p.
$$

若 $p$ 为奇数，则 $a$ 是 $k$ 中的 $p$ 次幂，矛盾。因此 $p=2$，且

$$
-a=N(\beta)^2
$$

是 $k$ 中的平方。写成 $-a=b^2$，其中 $b\in k$。由于 $a$ 不是 $k$ 中的平方，可知 $-1$ 不是 $k$ 中的平方。令 $i^2=-1$。在 $k(i)$ 上有因式分解

$$
X^{2^r}-a=X^{2^r}+b^2=(X^{2^{r-1}}+ib)(X^{2^{r-1}}-ib).
$$

每个因子的次数为 $2^{r-1}$，我们用归纳法论证。若 $X^{2^{r-1}}\pm ib$ 在 $k(i)$ 上可约，则 $\pm ib$ 是 $k(i)$ 中的平方，或者属于 $-4(k(i))^4$。无论哪种情形，$\pm ib$ 都是 $k(i)$ 中的平方，例如

$$
\pm ib=(c+di)^2=c^2+2cdi-d^2,
$$

其中 $c,d\in k$。于是 $c^2=d^2$，即 $c=\pm d$，且 $\pm ib=2cdi=\pm2c^2i$。平方后得到矛盾，即

$$
a=-b^2=-4c^4.
$$

现在由唯一分解可知，$X^{2^r}+b^2$ 在 $k[X]$ 中不能分解，这就证明了定理。

定理中的条件也是必要的，因为

$$
X^4+4b^4=(X^2+2bX+2b^2)(X^2-2bX+2b^2).
$$

若 $n=4m$ 且 $a\in-4k^4$，则 $X^n-a$ 可约。

<span class="original-page-anchor" id="pdf-page-313" aria-hidden="true"></span>

**推论 9.2。** *设 $k$ 为一个域，假定 $a\in k$，$a\ne0$，并且对于某个素数 $p$，$a$ 不是 $p$ 次幂。若 $p$ 等于特征，或者 $p$ 为奇数，则对于每个整数 $r\geqq1$，多项式 $X^{p^r}-a$ 在 $k$ 上不可约。*

*证明。* 这个断言在逻辑上比定理的断言弱。

**推论 9.3。** *设 $k$ 为一个域，假定 $k$ 的代数闭包 $k^a$ 在 $k$ 上的次数有限且 $>1$。则 $k^a=k(i)$，其中 $i^2=-1$，而且 $k$ 的特征为 $0$。*

*证明。* 注意，$k^a$ 在 $k$ 上正规。若 $k^a$ 在 $k$ 上不可分，从而 $\operatorname{char}k=p>0$，则 $k^a$ 在某个子域上的次数 $>1$ 且为纯不可分扩张（由第五章 §6），因此存在包含 $k$ 的一个子域 $E$ 以及一个元素 $a\in E$，使得 $X^p-a$ 在 $E$ 上不可约。由推论 9.2，$k^a$ 在 $E$ 上的次数不可能有限。（若略去了第五章 §6，读者可以只考虑特征为 $0$ 的情形。）

因此，可以假定 $k^a$ 在 $k$ 上是伽罗瓦扩张。令 $k_1=k(i)$。于是 $k^a$ 在 $k_1$ 上也是伽罗瓦扩张。设 $G$ 为 $k^a/k_1$ 的伽罗瓦群。假定有一个素数 $p$ 整除 $G$ 的阶，并取一个 $p$ 阶子群 $H$。设 $F$ 为它的固定域。则 $[k^a:F]=p$。若 $p$ 就是特征，本章末尾的习题 29 将给出矛盾。可以假定 $p$ 不是特征。不等于 $1$ 的 $p$ 次单位根是次数 $\leqq p-1$ 的多项式（即 $X^{p-1}+\cdots+1$）的根，因此必在 $F$ 中。由定理 6.2，$k^a$ 是某个多项式 $X^p-a$ 的分裂域，其中 $a\in F$。多项式 $X^{p^2}-a$ 必可约。由定理，必有 $p=2$，且 $a=-4b^4$，其中 $b\in F$。这意味着

$$
k^a=F(a^{1/2})=F(i).
$$

但是我们假定了 $i\in k_1$，矛盾。

这样，已经证明 $k^a=k(i)$。还须证明 $\operatorname{char}k=0$，为此我采用 Keith Conrad 告诉我的一个论证。先证明 $k$ 中若干平方的和仍是平方。只须证明两个平方的和的情形；此时把元素 $x+iy\in k(i)=k^a$ 写为一个平方：

$$
x+iy=(u+iv)^2,\qquad x,y,u,v\in k,
$$

于是 $x^2+y^2=(u^2+v^2)^2$。为了证明 $k$ 的特征为 $0$，只须注意：若特征 $>0$，则 $-1$ 是有限个 $1$ 的和 $1+\cdots+1$，所以由刚证明的结论它是平方；但 $k^a=k(i)$，这就完成了证明。

推论 9.3 归功于 Artin；参见第十一章末尾所列的 [Ar 24]。该章还会证明关于域 $k$ 的更多结论。

**例 1。** 设 $k=\mathbf Q$，并令 $G_{\mathbf Q}=G(\mathbf Q^a/\mathbf Q)$。则 $G_{\mathbf Q}$ 中仅有的非平凡挠元都是 $2$ 阶。由 Artin 的理论（如第十一章所述），这些挠元在 $G_{\mathbf Q}$ 中都彼此共轭。这里用到第十一章的定理 2.2、2.4 和 2.9。）

<span class="original-page-anchor" id="pdf-page-314" aria-hidden="true"></span>

**例 2。** 设 $k$ 为一个域，其特征不整除 $n$。设 $a\in k$，$a\ne0$，并令 $K$ 为 $X^n-a$ 的分裂域。取 $X^n-a$ 的一个根 $\alpha$，并取一个本原 $n$ 次单位根 $\zeta$。则

$$
K=k(\alpha,\zeta)=k(\alpha,\boldsymbol\mu_n).
$$

假定读者熟悉交换环上的矩阵。取 $\sigma\in G_{K/k}$。则 $(\sigma\alpha)^n=a$，所以存在一个模 $n$ 唯一确定的整数 $b=b(\sigma)$，使得

$$
\sigma(\alpha)=\alpha\zeta^{b(\sigma)}.
$$

由于 $\sigma$ 诱导循环群 $\boldsymbol\mu_n$ 的一个自同构，存在一个与 $n$ 互素且模 $n$ 唯一确定的整数 $d(\sigma)$，使得 $\sigma(\zeta)=\zeta^{d(\sigma)}$。设 $G(n)$ 为 $GL_2(\mathbf Z/n\mathbf Z)$ 中由所有下列矩阵组成的子群：

$$
M=\begin{pmatrix}1&0\\b&d\end{pmatrix},\quad\text{其中 }b\in\mathbf Z/n\mathbf Z,\quad d\in(\mathbf Z/n\mathbf Z)^*.
$$

注意 $\#G(n)=n\varphi(n)$。于是得到一个单射

$$
\sigma\mapsto M(\sigma)=\begin{pmatrix}1&0\\b(\sigma)&d(\sigma)\end{pmatrix},
\quad G_{K/k}\hookrightarrow G(n),
$$

可以立即验证它是单射同态。问题随之而来：什么时候它是同构？下面的定理在某些域上给出答案，尤其适用于有理数域。

**定理 9.4。** *设 $k$ 为一个域。设 $n$ 为与特征互素的奇正整数，并假定 $[k(\boldsymbol\mu_n):k]=\varphi(n)$。设 $a\in k$，并假定对于每个素数 $p\mid n$，元素 $a$ 都不是 $k$ 中的 $p$ 次幂。设 $K$ 为 $X^n-a$ 在 $k$ 上的分裂域。那么，上述同态 $\sigma\mapsto M(\sigma)$ 是 $G_{K/k}$ 到 $G(n)$ 的同构。交换子群为 $\operatorname{Gal}(K/k(\boldsymbol\mu_n))$，所以 $k(\boldsymbol\mu_n)$ 是 $K$ 的最大阿贝尔子扩张。*

*证明。* 考虑到 $G_{K/k}$ 在矩阵群中的表示，这是 §11 的一般理论以及习题 39 的一个特例。只须利用该习题给出的事实，即 $G_{K/k}$ 的阶为 $n\varphi(n)$，于是 $\#(G_{K/k})=\#G(n)$，从而 $G_{K/k}=G(n)$。不过，我们将给出一个独立的证明，作为伽罗瓦理论方法的例子。我们用归纳法证明定理。

先假定 $n=p$ 为素数。由于 $[k(\boldsymbol\mu_p):k]=p-1$ 与 $p$ 互素，若 $\alpha$ 为 $X^p-a$ 的一个根，则因 $[k(\alpha):k]=p$ 而有 $k(\alpha)\cap k(\boldsymbol\mu_p)=k$。因此 $[K:k]=p(p-1)$，所以 $G_{K/k}=G(p)$。

对任意 $n$，直接计算 $G(n)$ 中元素的交换子可知，交换子群包含在由下列矩阵组成的群中：

$$
\begin{pmatrix}1&0\\b&1\end{pmatrix},\qquad b\in\mathbf Z/n\mathbf Z,
$$

<span class="original-page-anchor" id="pdf-page-315" aria-hidden="true"></span>

因此必定就是这个子群，因为它的商群通过对角线上的投影同构于 $(\mathbf Z/n\mathbf Z)^*$。这就证明了 $n=p$ 时的定理。

现在取 $p\mid n$，写成 $n=pm$。由假设 $[k(\boldsymbol\mu_n):k]=\varphi(n)$，立即得到 $[k(\boldsymbol\mu_m):k]=\varphi(m)$。取 $X^n-a$ 的一个根 $\alpha$，并令 $\beta=\alpha^p$。则 $\beta$ 是 $X^m-a$ 的一个根，可以由归纳假设对 $X^m-a$ 应用定理。域图如下。

![域塔，保留全部包含关系以及次数 m 和 p](/library/volume-86/diagrams/pdf-0315-field-tower.png)

由于 $\alpha$ 在 $k$ 上的次数为 $pm$，它在 $k(\beta)$ 上的次数不可能小于 $p$，所以 $[k(\alpha):k(\beta)]=p$，且 $X^p-\beta$ 在 $k(\beta)$ 上不可约。对 $k(\beta)$ 上的 $X^p-\beta$ 应用证明的第一部分。关于分裂域的最大阿贝尔子扩张的性质表明，

$$
k(\alpha)\cap k(\beta,\boldsymbol\mu_n)=k(\beta).
$$

因此 $[k(\alpha,\boldsymbol\mu_n):k(\beta,\boldsymbol\mu_n)]=p$。由归纳假设，$[k(\beta,\boldsymbol\mu_n):k(\boldsymbol\mu_n)]=m$；这同样是由于 $X^m-a$ 在 $k$ 上的分裂域的最大阿贝尔子扩张的性质。这就证明了 $[K:k]=n\varphi(n)$，所以 $G_{K/k}=G(n)$；而关于交换子的断言已经证明。定理 9.4 的证明至此完成。

**注。** 当 $n$ 为偶数时会有一些复杂之处。例如，$\mathbf Q(\sqrt2)$ 包含在 $\mathbf Q(\boldsymbol\mu_8)$ 中，因此所讨论的域之间存在依赖关系。定理 9.4 中这样的非阿贝尔扩张本身就很有研究价值，因为它们是人们最先想到的此类扩张的例子；不过，它们也曾在其他重要背景中出现。例如，Artin 用它们给出一个概率模型，描述满足（例如）$2$ 为模 $p$ 的本原根的素数 $p$ 的密度（即 $2$ 生成循环群 $(\mathbf Z/p\mathbf Z)^*$。他实际考虑的并非只有 $2$，而是任意一个不等于 $\pm1$ 的非平方整数。起初，Artin 没有明确意识到上述类型的依赖关系，因此在一些情形下所得答案相差一个因子。Lehmer 通过计算发现了这一差异。正如 Artin 后来所说，必须乘上那个反映域之间依赖关系的“显然的”因子。Artin 从未发表自己的猜想，但 Lang–Tate 在他的论文集（Addison-Wesley，Springer Verlag）的导论中详细讨论了这件事。

Lang–Trotter 针对椭圆曲线，以及更一般的伽罗瓦群的某些 $p$ 进表示，构造了类似的猜想性概率模型，见“Primitive points on elliptic curves”，*Bull. AMS* **83**，第 2 期（1977），第 289–292 页，以及 [LaT 75]（§14 末尾）。

关于伽罗瓦群的 $p$ 进表示的进一步说明，参见 §14 和 §15。

<span class="original-page-anchor" id="pdf-page-316" aria-hidden="true"></span>

## §10. 伽罗瓦上同调

设 $G$ 为一个群，$A$ 为一个阿贝尔群。在定理之前的一般性说明中，我们把 $A$ 写成加法群。假定 $G$ 通过一个同态 $G\to\operatorname{Aut}(A)$ 作用于 $A$。所谓 $G$ 在 $A$ 中的一个 **1-上闭链**，是指一族元素 $\{\alpha_\sigma\}_{\sigma\in G}$，其中 $\alpha_\sigma\in A$，并且对所有 $\sigma,\tau\in G$ 都满足关系

$$
\alpha_\sigma+\sigma\alpha_\tau=\alpha_{\sigma\tau}.
$$

若 $\{\alpha_\sigma\}_{\sigma\in G}$ 和 $\{\beta_\sigma\}_{\sigma\in G}$ 都是 1-上闭链，就可以把它们相加，得到一个 1-上闭链 $\{\alpha_\sigma+\beta_\sigma\}_{\sigma\in G}$。于是显然，所有 1-上闭链构成一个群，记为 $Z^1(G,A)$。所谓 $G$ 在 $A$ 中的一个 **1-上边界**，是指一族元素 $\{\alpha_\sigma\}_{\sigma\in G}$，使得存在 $\beta\in A$，对所有 $\sigma\in G$ 都有 $\alpha_\sigma=\sigma\beta-\beta$。显然，1-上边界也是 1-上闭链，所有 1-上边界构成一个群，记为 $B^1(G,A)$。商群

$$
Z^1(G,A)/B^1(G,A)
$$

称为 $G$ 在 $A$ 中的**第一上同调群**，记为 $H^1(G,A)$。

**注。** 假设 $G$ 为循环群。设

$$
\operatorname{Tr}_G:A\to A\quad\text{为同态 }a\mapsto\sum_{\sigma\in G}\sigma(a).
$$

令 $\gamma$ 为 $G$ 的一个生成元。设 $(1-\gamma)A$ 为 $A$ 中所有形如 $a-\gamma(a)$（$a\in A$）的元素所构成的子群。则 $(1-\gamma)A$ 包含在 $\ker\operatorname{Tr}_G$ 中。读者可以作为练习验证，存在同构

$$
\ker\operatorname{Tr}_G/(1-\gamma)A\approx H^1(G,A).
$$

> **译校注。** 本注中的迹求和遍历 $G$，上述同构也要求 $G$ 是有限循环群，与下一定理中的有限伽罗瓦扩张一致。原书开头仅印作“循环群”，省略了“有限”。

对于循环群，下面的定理就是 §6 中的 Hilbert 第 90 定理。关于更一般的背景，还可参看第二十章习题 4 的群上同调。

**定理 10.1。** *设 $K/k$ 为一个有限伽罗瓦扩张，伽罗瓦群为 $G$。对于 $G$ 在 $K^*$ 上的作用，有 $H^1(G,K^*)=1$；对于 $G$ 在 $K$ 的加法群上的作用，有 $H^1(G,K)=0$。换言之，两种情形下的第一上同调群都是平凡群。*

*证明。* 设 $\{\alpha_\sigma\}_{\sigma\in G}$ 为 $G$ 在 $K^*$ 中的一个 1-上闭链。乘法形式的上闭链关系为

$$
\alpha_\sigma\alpha_\tau^\sigma=\alpha_{\sigma\tau}.
$$

<span class="original-page-anchor" id="pdf-page-317" aria-hidden="true"></span>

由特征标的线性无关性，存在 $\theta\in K$，使得元素

$$
\beta=\sum_{\tau\in G}\alpha_\tau\tau(\theta)
$$

不等于 $0$。于是

$$
\begin{aligned}
\sigma\beta&=\sum_{\tau\in G}\alpha_\tau^\sigma\sigma\tau(\theta)
=\sum_{\tau\in G}\alpha_{\sigma\tau}\alpha_\sigma^{-1}\sigma\tau(\theta)\\
&=\alpha_\sigma^{-1}\sum_{\tau\in G}\alpha_{\sigma\tau}\sigma\tau(\theta)
=\alpha_\sigma^{-1}\beta.
\end{aligned}
$$

得到 $\alpha_\sigma=\beta/\sigma\beta$，以 $\beta^{-1}$ 代替 $\beta$，就得到所需结论。

对于定理中的加法情形，取一个 $\theta\in K$，使得迹 $\operatorname{Tr}(\theta)$ 不等于 $0$。给定 $K$ 的加法群中的一个 1-上闭链 $\{\alpha_\sigma\}$，令

$$
\beta=\frac1{\operatorname{Tr}(\theta)}\sum_{\tau\in G}\alpha_\tau\tau(\theta).
$$

立即可得 $\alpha_\sigma=\beta-\sigma\beta$，如所要求。

下一个引理将用于下一节的非阿贝尔 Kummer 理论。

**引理 10.2。**（Sah）*设 $G$ 为一个群，$E$ 为一个 $G$-模。设 $\tau$ 在 $G$ 的中心中。则 $H^1(G,E)$ 被 $E$ 上的映射 $x\mapsto\tau x-x$ 零化。特别地，若这个映射是 $E$ 的自同构，则 $H^1(G,E)=0$。*

*证明。* 设 $f$ 为 $G$ 在 $E$ 中的一个 1-上闭链。则

$$
\begin{aligned}
f(\sigma)&=f(\tau\sigma\tau^{-1})=f(\tau)+\tau(f(\sigma\tau^{-1}))\\
&=f(\tau)+\tau[f(\sigma)+\sigma f(\tau^{-1})].
\end{aligned}
$$

因此

$$
\tau f(\sigma)-f(\sigma)=-\sigma\tau f(\tau^{-1})-f(\tau).
$$

但是，由 $f(1)=f(1)+f(1)$ 可得 $f(1)=0$，并且

$$
0=f(1)=f(\tau\tau^{-1})=f(\tau)+\tau f(\tau^{-1}).
$$

这表明 $(\tau-1)f(\sigma)=(\sigma-1)f(\tau)$，所以 $(\tau-1)f$ 是一个上边界。这就证明了引理。

<span class="original-page-anchor" id="pdf-page-318" aria-hidden="true"></span>

## §11. 非阿贝尔 Kummer 扩张

我们研究当 $n$ 次单位根不包含在底域中时，方程 $X^n-a=0$ 的分裂域。更一般地，我们希望大致知道（或尽可能精确地知道）若干这种类型的联立方程的伽罗瓦群。为此，我们用加法记号把证明的模式公理化；事实上，这会使论证的实质更容易看清。

固定一个整数 $N>1$，让 $M$ 遍历整除 $N$ 的正整数。令 $P$ 为整除 $N$ 的素数所组成的集合。令 $G$ 为一个群，并设：

$A=$ 一个 $G$-模，其中任一元素的稳定子群在 $G$ 中都有有限指数。此外，假定 $A$ 对素数 $p\mid N$ 都是可除的，即

$$
pA=A\quad\text{对所有 }p\in P.
$$

$\Gamma=$ $A$ 的一个有限生成子群，且 $G$ 逐点固定 $\Gamma$。

假定 $A_N$ 是有限的。则 $\frac1N\Gamma$ 也是有限生成的。注意

$$
\frac1N\Gamma\supset A_N.
$$

**例。** 对于我们在这里的目的，上面的设定概括了下面情形所满足的性质。设 $K$ 为有理数域上的一个有限生成域，甚至可以是有理数域的一个有限扩张。令 $A$ 为代数闭包 $K^a$ 的乘法群。令 $G=G_K$ 为伽罗瓦群 $\operatorname{Gal}(K^a/K)$。令 $\Gamma$ 为乘法群 $K^*$ 的一个有限生成子群。则上述性质全部成立。可见，$A_N=\boldsymbol\mu_N$ 是 $N$ 次单位根群。用加法记号写作 $\frac1N\Gamma$ 的群，用乘法记号写作 $\Gamma^{1/N}$。

接着，我们如下定义类似于 Kummer 理论中伽罗瓦群的相应群。对于 $A$ 的任意 $G$-子模 $B$，令：

$$
\begin{aligned}
G(B)&=G\text{ 在 }\operatorname{Aut}(B)\text{ 中的像},\\
G(N)=G(A_N)&=G\text{ 在 }\operatorname{Aut}(A_N)\text{ 中的像},\\
H(N)&=G\text{ 中逐点固定 }A_N\text{ 的子群},\\
H_\Gamma(M,N)\ (\text{其中 }M\mid N)&=H(N)\text{ 在 }\operatorname{Aut}\left(\frac1M\Gamma\right)\text{ 中的像}.
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-319" aria-hidden="true"></span>

于是有一个正合列：

$$
0\to H_\Gamma(M,N)\to G\left(\frac1M\Gamma+A_N\right)\to G(N)\to0.
$$

**例。** 在前面所述的具体情形中，读者容易认出这些群都是伽罗瓦群。例如，令 $A$ 为乘法群。则有如下域扩张格及其对应的伽罗瓦群：

![Kummer 域扩张格及对应的伽罗瓦群](/library/volume-86/diagrams/pdf-0319-kummer-lattice.png)

在应用中，我们想知道：当 $M\mid N$ 时，把 $K(\boldsymbol\mu_M,\Gamma^{1/M})$ 平移到 $K(\boldsymbol\mu_N)$ 上之后，会有多大程度的退化。这就是我们使用一对整数 $M,N$ 而不是单个 $N$ 的原因。

回到上面的一般 Kummer 表示。我们尤其关心 $(\mathbf Z/N\mathbf Z)^*$ 中包含于 $G(N)$ 的那一部分，即由满足下述条件的模 $N$ 整数 $n$ 所构成的群：$G(N)$ 中存在一个元素 $[n]$，使得

$$
[n]a=na\quad\text{对所有 }a\in A_N.
$$

这样的元素总是在 $G(N)$ 的中心中，称为**位似**。

写成

$$
N=\prod p^{n(p)}.
$$

设 $S$ 为 $P$ 的一个子集。我们要对 $G(N)$ 作一些非退化假设。把 $S$ 称为**特殊集合**。

存在乘积分解

$$
(\mathbf Z/N\mathbf Z)^*=\prod_{p\mid N}(\mathbf Z/p^{n(p)}\mathbf Z)^*.
$$

若 $2\mid N$，假定 $2\in S$。对于每个 $p\in S$，假定存在整数 $c(p)=p^{f(p)}$，其中 $f(p)\geqq1$，使得

$$
G(A_N)\supset\prod_{p\in S}U_{c(p)}\times\prod_{p\notin S}(\mathbf Z/p^{n(p)}\mathbf Z)^*,
$$

其中 $U_{c(p)}$ 为 $\mathbf Z(p^{n(p)})$ 中由那些模 $c(p)$ 同余于 $1$ 的元素构成的子群。

<span class="original-page-anchor" id="pdf-page-320" aria-hidden="true"></span>

右边的乘积分解对应于直和分解

$$
A_N=\bigoplus_{p\mid N}A_{p^{n(p)}}.
$$

上述假设称为**非退化假设**。整数 $c(p)$ 衡量 $G(A_N)$ 的退化程度。

在这个假设下，可以看到

$$
[2]\in G(A_M)\quad\text{若 }M\mid N\text{ 且 }M\text{ 不被 }S\text{ 中的素数整除};
$$

$$
[1+c]\in G(A_M)\quad\text{若 }M\mid N\text{ 且 }M\text{ 的素因子全部在 }S\text{ 中},
$$

其中

$$
c=c(S)=\prod_{p\in S}c(p).
$$

于是可以在引理 10.2 的背景中利用 $[2]-[1]=[1]$ 和 $[1+c]-[1]=[c]$，因为 $[1]$ 和 $[c]$ 在 $G$ 的中心中。

> **译校注。** 原书最后一句称 $[1]$ 和 $[c]$ 为 $G$ 的中心元素。应用引理 10.2 时，实际使用的中心群元素是作用于 $A_M$ 的相应像群中的位似 $[2]$ 或 $[1+c]$；它们减去恒等映射所得的算子才是 $[1]$ 或 $[c]$。特别地，$[c]$ 不一定可逆，不能一般地视为 $G$ 的群元素；此处应按上述算子关系理解。

对于任意 $M$，定义

$$
c(M)=\prod_{\substack{p\mid M\\p\in S}}c(p).
$$

**定义**

$$
\Gamma'=\frac1N\Gamma\cap A^G
$$

以及**指数**

$$
e(\Gamma'/\Gamma)=\text{使 }e\Gamma'\subset\Gamma\text{ 的最小正整数 }e.
$$

显然，上面定义的伽罗瓦群 $H_\Gamma(M,N)$ 的退化可能来自底域中存在许多单位根，或者至少来自单位根的伽罗瓦群的退化；此外，在考虑方程

$$
X^M-a=0
$$

时，还可能来自 $a$ 在 $K$ 中已经具有很高的可除性这一事实。观察 $\Gamma$ 的除元所对应的伽罗瓦群，就可以看出第二种退化来自指数 $e(\Gamma'/\Gamma)$。下一个定理表明，这些就是退化的全部来源。

对于 $M\mid N$，有阿贝尔 Kummer 配对

$$
H_\Gamma(M,N)\times\Gamma/M\Gamma\to A_M,\quad(\tau,x)\mapsto\tau y-y,
$$

其中 $y$ 为满足 $My=x$ 的任意元素。这个配对的值不依赖于<span class="original-page-anchor" id="pdf-page-321" aria-hidden="true"></span>$y$ 的选择。因此，对于 $x\in\Gamma$，有一个同态

$$
\varphi_x:H_\Gamma(M,N)\to A_M,
$$

满足

$$
\varphi_x(\tau)=\tau y-y,\qquad\text{其中 }My=x.
$$

**定理 11.1。** *设 $M\mid N$。设 $\varphi$ 为同态*

$$
\varphi:\Gamma\to\operatorname{Hom}(H_\Gamma(M,N),A_M),
$$

*并令 $\Gamma_\varphi$ 为它的核。令 $e_M(\Gamma)=\operatorname{g.c.d.}(e(\Gamma'/\Gamma),M)$。在非退化假设下，有*

$$
c(M)e_M(\Gamma)\Gamma_\varphi\subset M\Gamma.
$$

*证明。* 取 $x\in\Gamma$，假设 $\varphi_x=0$。令 $My=x$。对于 $\sigma\in G$，令

$$
y_\sigma=\sigma y-y.
$$

则 $\{y_\sigma\}$ 是 $G$ 在 $A_M$ 中的一个 1-上闭链。由假设 $\varphi_x=0$，这个上闭链仅依赖于 $\sigma$ 模 $G$ 中逐点固定 $A_N$ 的子群的类。换言之，可以把 $\{y_\sigma\}$ 看成 $G(N)$ 在 $A_M$ 中的上闭链。令 $c=c(N)$。由引理 10.2，$\{cy_\sigma\}$ 作为 $G(N)$ 在 $A_M$ 中的上闭链是分裂的。换言之，存在 $t_0\in A_M$，使得

$$
cy_\sigma=\sigma t_0-t_0,
$$

而且这个等式实际上对 $\sigma\in G$ 都成立。取 $t$ 使 $ct=t_0$。则

$$
c\sigma y-cy=\sigma ct-ct.
$$

> **译校注。** 原书上一等式右端印作 $\sigma ct-cy$。把 $t_0=ct$ 代入 $cy_\sigma=\sigma t_0-t_0$，可知最后一项应为 $ct$，即上面给出的修正式；这样才能推出下一句的 $c(y-t)$ 被固定。

由此可见，$c(y-t)$ 被所有 $\sigma\in G$ 固定，因此属于 $\frac1N\Gamma$。所以

$$
e(\Gamma'/\Gamma)c(y-t)\in\Gamma.
$$

两边乘以 $M$，注意到 $cM(y-t)=cMy=cx$。这表明

$$
c(N)e(\Gamma'/\Gamma)\Gamma_\varphi\subset M\Gamma.
$$

由于 $\Gamma/M\Gamma$ 的指数为 $M$，可以按定理的说法，把 $e(\Gamma'/\Gamma)$ 替换为最大公约数，并把 $c(N)$ 替换为 $c(M)$，证明完成。

**推论 11.2。** *假设 $M$ 与 $2(\Gamma':\Gamma)$ 互素，且不被特殊集合 $S$ 中的任何素数整除。则有单射*

$$
\varphi:\Gamma/M\Gamma\to\operatorname{Hom}(H_\Gamma(M,N),A_M).
$$

<span class="original-page-anchor" id="pdf-page-322" aria-hidden="true"></span>

*若再假定 $\Gamma$ 为自由阿贝尔群，一个基为 $\{a_1,\ldots,a_r\}$，并令 $\varphi_i=\varphi_{a_i}$，则映射*

$$
H_\Gamma(M,N)\to A_M^{(r)},\quad\tau\mapsto(\varphi_1(\tau),\ldots,\varphi_r(\tau))
$$

*是单射。若 $A_M$ 为 $M$ 阶循环群，则这个映射为同构。*

*证明。* 在推论的假设下，定理中有 $c(M)=1$，且 $e_M(\Gamma)=1$。

> **译校注。** 原书末项印作 $c_M(\Gamma)=1$；按定理 11.1 的定义，此处应为 $e_M(\Gamma)=1$，而推论的互素条件恰保证这一点。

**例。** 考虑伽罗瓦理论中 $A$ 为 $K^a$ 的乘法群的情形。设 $a_1,\ldots,a_r$ 为 $K^*$ 中乘法无关的元素。它们生成推论中所述的群。此外，$A_M=\boldsymbol\mu_M$ 是循环群，所以可以应用推论。若 $M$ 与 $2(\Gamma':\Gamma)$ 互素，且不被特殊集合 $S$ 中的任何素数整除，则有同构

$$
\varphi:\Gamma/M\Gamma\to\operatorname{Hom}(H_\Gamma(M,N),\boldsymbol\mu_M).
$$

## §12. 同态的代数无关性

设 $A$ 为加法群，$K$ 为域。设 $\lambda_1,\ldots,\lambda_n:A\to K$ 为加法同态。如果存在多项式 $f(X_1,\ldots,X_n)\in K[X_1,\ldots,X_n]$，使得对所有 $x\in A$ 都有

$$
f(\lambda_1(x),\ldots,\lambda_n(x))=0,
$$

但 $f$ 在 $K^{(n)}$（即 $K$ 与自身的 $n$ 重直积）上所诱导的函数不是零函数，就称 $\lambda_1,\ldots,\lambda_n$（在 $K$ 上）**代数相关**。我们知道，每个多项式都对应唯一的、给出同一函数的约化多项式。若 $K$ 为无限域，则这个约化多项式就是 $f$ 本身。在代数相关的定义中，也可以直接假定 $f$ 是约化的。

若多项式 $f(X_1,\ldots,X_n)$ 诱导一个从 $K^{(n)}$ 到 $K$ 的加法同态，就称它是**加法多项式**。令 $(Y)=(Y_1,\ldots,Y_n)$ 为独立于 $(X)$ 的变量。令

$$
g(X,Y)=f(X+Y)-f(X)-f(Y),
$$

其中 $X+Y$ 为逐分量的向量加法。把 $g$ 看作以 $K[Y]$ 为系数、关于 $(X)$ 的多项式，则它的总次数严格小于 $f$ 的总次数；对每个 $X_i$，它的次数不超过 $f$ 关于 $X_i$ 的次数。

> **译校注。** 原书在最后一项也印作“严格小于”，这一断言一般不成立。例如 $f=X_1X_2$ 时，$g=X_1Y_2+Y_1X_2$，关于 $X_1$ 的次数没有下降。正确界限为 $\deg_{X_i}g\leqq\deg_{X_i}f$。对于非常数 $f$，关于整组 $(X)$ 的总次数确实严格下降，这正是后面的证明所需的性质。

考虑单项式的差，便容易看出这一点，

<span class="original-page-anchor" id="pdf-page-323" aria-hidden="true"></span>

$$
\begin{aligned}
&M_{(v)}(X+Y)-M_{(v)}(X)-M_{(v)}(Y)\\
&\qquad=(X_1+Y_1)^{v_1}\cdots(X_n+Y_n)^{v_n}
-X_1^{v_1}\cdots X_n^{v_n}-Y_1^{v_1}\cdots Y_n^{v_n}.
\end{aligned}
$$

把 $g$ 看作以 $K[X]$ 为系数、关于 $(Y)$ 的多项式时，也有类似的断言。

若 $f$ 是约化的，则 $g$ 也是约化的。因此，若 $f$ 为加法多项式，则 $g$ 是零多项式。

**例。** 设 $K$ 的特征为 $p$。则在一个变量的情形中，对于 $a\in K$ 和 $m\geqq1$，映射

$$
\xi\mapsto a\xi^{p^m}
$$

是加法映射，由加法多项式 $aX^{p^m}$ 给出。以后将会看到，这是一个典型的例子。

**定理 12.1。**（Artin）*设 $\lambda_1,\ldots,\lambda_n:A\to K$ 为从一个加法群到一个域的加法同态。若这些同态在 $K$ 上代数相关，则存在 $K[X]$ 中的一个加法多项式*

$$
f(X_1,\ldots,X_n)\ne0,
$$

*使得对所有 $x\in A$ 都有*

$$
f(\lambda_1(x),\ldots,\lambda_n(x))=0.
$$

*证明。* 取一个次数尽可能低的约化多项式 $f(X)=f(X_1,\ldots,X_n)\in K[X]$，满足 $f\ne0$，但对所有 $x\in A$ 都有 $f(\Lambda(x))=0$，其中 $\Lambda(x)$ 为向量 $(\lambda_1(x),\ldots,\lambda_n(x))$。我们将证明 $f$ 是加法多项式。

令 $g(X,Y)=f(X+Y)-f(X)-f(Y)$。则对所有 $x,y\in A$ 都有

$$
g(\Lambda(x),\Lambda(y))=f(\Lambda(x+y))-f(\Lambda(x))-f(\Lambda(y))=0.
$$

我们将证明，$g$ 在 $K^{(n)}\times K^{(n)}$ 上诱导零函数。假设不是这样，分为两种情形。

*情形 1。* 对所有 $\xi\in K^{(n)}$ 和所有 $y\in A$，都有 $g(\xi,\Lambda(y))=0$。由假设，存在 $\xi'\in K^{(n)}$，使得 $g(\xi',Y)$ 不恒为 $0$。令 $P(Y)=g(\xi',Y)$。由于 $g$ 关于 $(Y)$ 的次数严格小于 $f$ 的次数，得到矛盾。

*情形 2。* 存在 $\xi'\in K^{(n)}$ 及 $y'\in A$，使得 $g(\xi',\Lambda(y'))\ne0$。令 $P(X)=g(X,\Lambda(y'))$。则 $P$ 不是零多项式，但对所有 $x\in A$ 都有 $P(\Lambda(x))=0$，再次得到矛盾。

<span class="original-page-anchor" id="pdf-page-324" aria-hidden="true"></span>

因此，$g$ 在 $K^{(n)}\times K^{(n)}$ 上诱导零函数，这就证明了我们所要的结论，即 $f$ 是加性的。

现在更仔细地考察加性多项式。

设 $f$ 是 $K$ 上的 $n$ 元加性多项式，并假定 $f$ 是约化的。令

$$
f_i(X_i)=f(0,\ldots,X_i,\ldots,0),
$$

其中 $X_i$ 位于第 $i$ 个位置，其余分量都是零。由加性可得

$$
f(X_1,\ldots,X_n)=f_1(X_1)+\cdots+f_n(X_n),
$$

因为右边与左边之差是一个约化多项式，在 $K^{(n)}$ 上取值均为 $0$。此外，每个 $f_i$ 都是一元加性多项式。下面研究这种多项式。

设 $f(X)$ 是一个一元约化多项式，它诱导 $K$ 到自身的线性映射。假设 $f$ 中有单项式 $a_rX^r$，其系数 $a_r\ne0$。那么

$$
g(X,Y)=f(X+Y)-f(X)-f(Y)
$$

中的 $r$ 次单项式由下式给出：

$$
a_r(X+Y)^r-a_rX^r-a_rY^r.
$$

我们已知 $g$ 恒为 $0$，所以上式也恒为 $0$。因此，多项式

$$
(X+Y)^r-X^r-Y^r
$$

是零多项式。它含有项 $rX^{r-1}Y$。所以，若 $r>1$，则所考虑的域必须具有特征 $p$，且 $r$ 被 $p$ 整除。写成 $r=p^ms$，其中 $s$ 与 $p$ 互素。于是

$$
0=(X+Y)^r-X^r-Y^r=(X^{p^m}+Y^{p^m})^s-(X^{p^m})^s-(Y^{p^m})^s.
$$

如前论证，可得 $s=1$。

因此，若 $f$ 是一元加性多项式，则有

$$
f(X)=\sum_{v=0}^m a_vX^{p^v},
$$

其中 $a_v\in K$。在特征 $0$ 时，一元加性多项式只能具有 $aX$ 的形式，其中 $a\in K$。

按预期的方式，我们定义 $\lambda_1,\ldots,\lambda_n$ **代数独立**，如果对于任意约化多项式 $f$，只要对所有 $x\in A$ 都有 $f(\Lambda(x))=0$，就必有 $f$ 为零多项式。

> **译校注。** 原书最后一个定义印作“对所有 $x\in K$”。本节起初定义的同态为 $\lambda_i:A\to K$，所以这里的量词范围应为定义域 $A$；译文已改为 $x\in A$。下一页应用于域自同构时，才取 $A=K$。

<span class="original-page-anchor" id="pdf-page-325" aria-hidden="true"></span>

我们将把定理 12.1 应用于 $\lambda_1,\ldots,\lambda_n$ 是一个域的自同构的情形，并将定理 12.1 与特征标的线性独立性定理结合起来。

**定理 12.2。** 设 $K$ 是无限域，$\sigma_1,\ldots,\sigma_n$ 是 $K$ 的一个有限自同构群的互不相同的元素。那么 $\sigma_1,\ldots,\sigma_n$ 在 $K$ 上代数独立。

**证明。**（Artin）在特征 $0$ 时，由定理 12.1 及特征标的线性独立性，便知所述结论成立。设特征为 $p>0$，并假设 $\sigma_1,\ldots,\sigma_n$ 代数相关。

存在 $K[X]$ 中的加性多项式 $f(X_1,\ldots,X_n)$，它是约化的，$f\ne0$，而且对所有 $x\in K$ 都有

$$
f(\sigma_1(x),\ldots,\sigma_n(x))=0.
$$

由上面的讨论，这个关系可以写成

$$
\sum_{i=1}^n\sum_{r=1}^m a_{ir}\sigma_i(x)^{p^r}=0,
$$

其中 $x$ 遍历 $K$，且系数 $a_{ir}$ 不全为 $0$。于是，由特征标的线性独立性，乘法特征标

$$
\{\sigma_i^{p^r}\}\qquad\text{其中 }i=1,\ldots,n,\quad r=1,\ldots,m
$$

不可能全部互不相同。因此有

**译校注。** 原书将这里的映射称为“automorphisms”（自同构）。记号 $\sigma_i^{p^r}$ 在此表示逐点取幂的映射 $x\mapsto\sigma_i(x)^{p^r}$；这些映射是乘法特征标，但当 $K$ 不完美时，Frobenius 映射未必为满射，所以它们未必是自同构。这一步只需特征标的线性独立性，论证仍然成立。

$$
\sigma_i^{p^r}=\sigma_j^{p^s},
$$

其中 $i\ne j$ 或 $r\ne s$。不妨设 $r\le s$。对所有 $x\in K$，有

$$
\sigma_i(x)^{p^r}=\sigma_j(x)^{p^s}.
$$

在特征 $p$ 时，开 $p$ 次方根具有唯一性。因此，对所有 $x\in K$，有

$$
\sigma_i(x)=\sigma_j(x)^{p^{s-r}}=\sigma_j(x^{p^{s-r}}).
$$

令 $\sigma=\sigma_j^{-1}\sigma_i$。则对所有 $x\in K$，有

$$
\sigma(x)=x^{p^{s-r}}.
$$

由 $\sigma^n=\mathrm{id}$ 可知，对所有 $x\in K$，

$$
x=x^{p^{n(s-r)}}.
$$

由于 $K$ 是无限域，这只有在 $s=r$ 时才可能成立。但此时 $\sigma_i=\sigma_j$，与起初这些自同构互不相同的假设矛盾。

<span class="original-page-anchor" id="pdf-page-326" aria-hidden="true"></span>

## §13. 正规基定理

**定理 13.1。** 设 $K/k$ 是次数为 $n$ 的有限伽罗瓦扩张，$\sigma_1,\ldots,\sigma_n$ 是伽罗瓦群 $G$ 的全部元素。那么存在元素 $w\in K$，使得 $\sigma_1w,\ldots,\sigma_nw$ 构成 $K$ 在 $k$ 上的一组基。

**证明。** 这里仅在 $k$ 为无限域时证明这个结论。$k$ 为有限域的情形，稍后可用线性代数方法证明，作为一道习题。

对每个 $\sigma\in G$，令 $X_\sigma$ 为一个变量，并令 $t_{\sigma,\tau}=X_{\sigma^{-1}\tau}$。令 $X_i=X_{\sigma_i}$，再令

$$
f(X_1,\ldots,X_n)=\det(t_{\sigma_i,\sigma_j}).
$$

在 $X_{\mathrm{id}}$ 处代入 $1$，并在 $\sigma\ne\mathrm{id}$ 时的 $X_\sigma$ 处代入 $0$，即可看出 $f$ 不恒为 $0$。由于 $k$ 是无限域，$f$ 是约化的。因此，若在 $f$ 中以 $\sigma_i(x)$ 代替 $X_i$，所得行列式不可能对所有 $x\in K$ 都为 $0$。所以存在 $w\in K$，使得

$$
\det(\sigma_i^{-1}\sigma_j(w))\ne0.
$$

假设 $a_1,\ldots,a_n\in k$ 满足

$$
a_1\sigma_1(w)+\cdots+a_n\sigma_n(w)=0.
$$

对每个 $i=1,\ldots,n$，将 $\sigma_i^{-1}$ 作用于这个关系。因为 $a_j\in k$，把各个 $a_j$ 看作未知数，就得到一个线性方程组。其系数行列式不等于 $0$，于是

$$
a_j=0\qquad\text{对 }j=1,\ldots,n.
$$

这说明 $w$ 就是所要求的元素。

**注。** 用第三章和第十八章中的表示论语言来说，正规基定理指出，伽罗瓦群在域的加法群上的表示是正则表示。也可以说，$K$ 是群环 $k[G]$ 上秩为 $1$ 的自由模。这个结果可以看作与代数数论有关的许多更精细研究的第一步。设 $K$ 是数域，即 $\mathbf Q$ 的有限扩张，令 $\mathfrak o_K$ 为它的代数整数环；此概念将在第七章 §1 中定义。于是可以要求描述 $\mathfrak o_K$ 的 $\mathbf Z[G]$ 模结构，这是困难得多的问题。有关这一问题的基础性工作，参见 A. Fröhlich，*Galois Module Structures of Algebraic Integers*，Ergebnisse der Math. 3 Folge Vol. 1，Springer Verlag（1983）。另见第三章 §1 末所列的文献 [CCFT 91]。

<span class="original-page-anchor" id="pdf-page-327" aria-hidden="true"></span>

## §14. 无限伽罗瓦扩张

虽然我们已经给出了伽罗瓦理论的一些基本定理，而且允许其中的扩张是无限扩张，但无限性还没有真正以实质性的方式出现。现在要更充分地讨论它的作用。

设 $K/k$ 是伽罗瓦扩张，其群为 $G$。对每个有限伽罗瓦子扩张 $F$，都有伽罗瓦群 $G_{K/F}$ 和 $G_{F/k}$。令 $H=G_{K/F}$。则 $H$ 的指数有限，等于 $\#(G_{F/k})=[F:k]$。这只是一般伽罗瓦理论的一个特例。存在典范同态

$$
G\longrightarrow G/H=G_{F/k}.
$$

因此，由逆极限的泛性质，得到同态

$$
G\longrightarrow\varprojlim_{H\in\mathfrak F}G/H,
$$

其中极限对上述伽罗瓦群 $G_{K/F}$ 所组成的族 $\mathfrak F$ 中的 $H$ 取遍。

**定理 14.1。** 同态 $G\longrightarrow\varprojlim G/H$ 是同构。

**证明。** 首先，它的核是平凡的，因为若 $\sigma$ 在核中，则 $\sigma$ 在 $K$ 的每个有限子扩张上的限制都平凡，从而在 $K$ 上平凡。回忆一下，逆极限的一个元素是由 $\sigma_H\in G/H$ 组成的族 $\{\sigma_H\}$，满足某种相容条件。这个相容条件使我们可以如下定义 $G$ 的元素 $\sigma$。取 $\alpha\in K$。则 $\alpha$ 属于某个有限伽罗瓦扩张 $F\subset K$。令 $H=\operatorname{Gal}(K/F)$，并令 $\sigma\alpha=\sigma_H\alpha$。相容条件说明 $\sigma_H\alpha$ 与 $F$ 的选择无关。随即便能验证，$\sigma$ 是 $K$ 在 $k$ 上的自同构，在 $G$ 到 $G/H$ 的典范映射下映为各个 $\sigma_H$。因此映射 $G\longrightarrow\varprojlim G/H$ 是满射，从而定理得证。

**注。** 关于拓扑解释，见第一章定理 10.1 及习题 43。

**例。** 设 $\boldsymbol\mu[p^\infty]$ 为所有单位根群 $\boldsymbol\mu[p^n]$ 的并，其中 $p$ 是素数，$n=1,2,\ldots$ 遍历正整数。令 $K=\mathbf Q(\boldsymbol\mu[p^\infty])$。则 $K$ 是 $\mathbf Q$ 的阿贝尔无限扩张。令 $\mathbf Z_p$ 为 $p$ 进整数环，$\mathbf Z_p^*$ 为其可逆元群。由 §3，已知 $(\mathbf Z/p^n\mathbf Z)^*$ 同构于 $\operatorname{Gal}(\mathbf Q(\boldsymbol\mu[p^n])/\mathbf Q)$。这些同构在 $p$ 次单位根的塔中相容，所以得到同构

$$
\mathbf Z_p^*\longrightarrow\operatorname{Gal}(\mathbf Q(\boldsymbol\mu[p^\infty])/\mathbf Q).
$$

**译校注。** 原书在以上两处分别印作 $\operatorname{Gal}(\mathbf Q(\boldsymbol\mu[p^n]/\mathbf Q))$ 和 $\operatorname{Gal}(\mathbf Q(\boldsymbol\mu[p^\infty]/\mathbf Q))$，将右括号放到了分母之后。这里的扩张分别是 $\mathbf Q(\boldsymbol\mu[p^n])/\mathbf Q$ 和 $\mathbf Q(\boldsymbol\mu[p^\infty])/\mathbf Q$，故译文据此调整括号。

<span class="original-page-anchor" id="pdf-page-328" aria-hidden="true"></span>

Iwasawa 对分圆域的塔作了广泛研究。系统的介绍及参考文献可参见 [La 90]。

关于群 $GL_2(\mathbf Z_p)$ 中的其他类型的表示，参见 Serre [Se 68]、[Se 72]，Shimura [Shi 71] 及 Lang–Trotter [LaT 75]。从椭圆曲线开始考虑交换代数群，就能在一个一般框架中理解伽罗瓦群在单位根上的表示。具体地，考虑方程

$$
y^2=4x^3-g_2x-g_3,
$$

其中 $g_2,g_3\in\mathbf Q$，且判别式非零：$\Delta=g_2^3-27g_3^2\ne0$。将解集加上一个无穷远点，记为 $E$。由复分析，或者用纯代数方法，可以看出：若 $K$ 是 $\mathbf Q$ 的扩张，则满足 $x,y\in K$ 的解连同 $\infty$ 组成的集合 $E(K)$ 构成一个群，称为 $E$ 在 $K$ 中的**有理点**群。我们关心代数闭包中点的挠群，例如 $E(\mathbf Q^a)_{\mathrm{tor}}$；也关心对于给定素数 $p$ 的群 $E(\mathbf Q^a)[p^r]$ 和 $E(\mathbf Q^a)[p^\infty]$。作为阿贝尔群，有同构

$$
E(\mathbf Q^a)[p^r]\approx(\mathbf Z/p^r\mathbf Z)\times(\mathbf Z/p^r\mathbf Z).
$$

所以伽罗瓦群通过 $GL_2(\mathbf Z/p^r\mathbf Z)$ 中的表示作用于 $p^r$ 阶的点，而单位根情形中相应的是 $GL_1(\mathbf Z/p^r\mathbf Z)=(\mathbf Z/p^r\mathbf Z)^*$。取逆极限，就得到 $\operatorname{Gal}(\mathbf Q^a/\mathbf Q)=G_{\mathbf Q}$ 在 $GL_2(\mathbf Z_p)$ 中的表示。Serre 的一个定理指出：如果 $\operatorname{End}_{\mathbf C}(E)=\mathbf Z$，那么 $G_{\mathbf Q}$ 在 $GL_2(\mathbf Z_p)$ 中的像是有限指数子群，而且除有限多个素数 $p$ 外，这个像都等于 $GL_2(\mathbf Z_p)$。

更一般地，自由使用代数几何的语言，若 $A$ 是交换代数群，例如其系数在 $\mathbf Q$ 中，则可以考虑它的点群 $A(\mathbf Q^a)_{\mathrm{tor}}$，并以类似方式考虑 $G_{\mathbf Q}$ 的表示。为了处理这些情形而发展所需的概念，便会进入代数几何。

除了考虑基域的分圆扩张外，也可以考虑分圆域的扩张。下面的猜想由 Shafarevich 提出。参见 §7 末的参考文献。

**猜想 14.2。** 设 $k_0=\mathbf Q(\boldsymbol\mu)$ 为给定代数闭包 $\mathbf Q^a$ 中 $\mathbf Q$ 的所有分圆扩张的合成域。设 $k$ 是 $k_0$ 的有限扩张，令 $G_k=\operatorname{Gal}(\mathbf Q^a/k)$。那么 $G_k$ 同构于一个具有可数多个生成元的自由群的完备化。

回忆一下，若 $G$ 是该自由群，则其完备化是逆极限 $\varprojlim G/H$，其中 $H$ 遍历所有有限指数正规子群。读者应将这一猜想与 §2 例 9 所述的黎曼曲面情形作类比。如果将 $\mathbf Q(\boldsymbol\mu)$ 换成 $\mathbf Q(A(\mathbf Q^a)_{\mathrm{tor}})$，其中 $A$ 是椭圆曲线，研究这个猜想在多大程度上仍然成立，将会很有意思。关于自由群作为伽罗瓦群出现的一些结果，另见 Wingberg [Wi 91]。

<span class="original-page-anchor" id="pdf-page-329" aria-hidden="true"></span>

### 参考文献

[La 90] S. Lang，*Cyclotomic Fields I and II*，第二版，Springer Verlag，1990（由 1978、1980 年的初版合编而成）

[LaT 75] S. Lang 与 H. Trotter，*Distribution of Frobenius Elements in $GL_2$-Extensions of the Rational Numbers*，Springer Lecture Notes 504（1975）

[Se 68] J.-P. Serre，*Abelian $l$-adic Representations and Elliptic Curves*，Benjamin，1968

[Se 72] J.-P. Serre，Propriétés galoisiennes des points d'ordre fini des courbes elliptiques，*Invent. Math.* **15**（1972），第 259–331 页

[Shi 71] G. Shimura，*Introduction to the arithmetic theory of Automorphic Functions*，Iwanami Shoten 与 Princeton University Press，1971

[Wi 91] K. Wingberg，On Galois groups of $p$-closed algebraic number fields with restricted ramification，I，*J. reine angew. Math.* **400**（1989），第 185–202 页；以及 II，同刊，**416**（1991），第 187–194 页

## §15. 与模形式的联系

本章最后这一节介绍伽罗瓦理论与模形式理论之间一个重要的联系；这个联系自 20 世纪 60 年代以来逐渐出现。

一个基本问题是：给定有限群 $G$，是否存在 $\mathbf Q$ 的伽罗瓦扩张 $K$，使其伽罗瓦群为 $G$？在习题 23 中，你将证明当 $G$ 为阿贝尔群时，答案是肯定的。

早在 19 世纪，数论学家就已认识到阿贝尔扩张与非阿贝尔扩张之间的重大差别，并开始理解阿贝尔扩张。Kronecker 断言，$\mathbf Q$ 的每个有限阿贝尔扩张都包含在某个扩张 $\mathbf Q(\zeta)$ 中，其中 $\zeta$ 是单位根；他给出的论证在今天看来尚不完整。困难在于素数 $2$ 的特殊性质。Weber 在 19 世纪末解决了这个问题。应注意，从那以后，素数 $2$ 一再系统性地造成困难。定理 9.4 后的注中提到的、有关原根密度的 Artin 猜想中，就出现了这一困难。类域论中的 Grunwald 定理中也出现了这一困难，后来由 Wang 修正；参见 Artin–Tate [ArT 68] 第 10 章。§7 末提到的 Shafarevich 的证明中也出现了这一困难：给定可解群，存在 $\mathbf Q$ 的伽罗瓦扩张，以该群为伽罗瓦群。

数域 $F$ 的阿贝尔扩张比有理数域上的阿贝尔扩张更难描述；描述这种扩张的基础理论称为类域论，见上述参考文献。我将给出一个有代表性的重要例子。设 $R_F$ 为 $F$ 的代数整数环。可以证明 $R_F$ 是戴德金环（参见 [La 70] 第一章 §6 定理 2）。设 $P$ 是 $R_F$ 的素理想。那么存在素数 $p$，使得 $P\cap\mathbf Z=(p)$。

<span class="original-page-anchor" id="pdf-page-330" aria-hidden="true"></span>

此外，$R_F/P$ 是一个具有 $q$ 个元素的有限域。设 $K$ 是 $F$ 的有限伽罗瓦扩张。第七章将证明，存在 $R_K$ 的素理想 $Q$，使得 $Q\cap R_F=P$。此外，存在元素

$$
\mathrm{Fr}_Q\in G=\operatorname{Gal}(K/F),
$$

满足 $\mathrm{Fr}_Q(Q)=Q$，且对所有 $\alpha\in R_K$，有

$$
\mathrm{Fr}_Q\alpha\equiv\alpha^q\pmod Q.
$$

我们称 $\mathrm{Fr}_Q$ 为伽罗瓦群 $G$ 中与 $Q$ 相联系的 **Frobenius 元素**，见第七章定理 2.9。此外，除有限多个 $Q$ 外，两个这样的元素在 $G$ 中彼此共轭。任取其中一个，记作 $\mathrm{Fr}_P$。若 $G$ 是阿贝尔群，则伽罗瓦群中只有一个元素 $\mathrm{Fr}_P$。

**定理 15.1。** 存在唯一的 $F$ 的有限阿贝尔扩张 $K$，具有如下性质：若 $P_1,P_2$ 是 $R_F$ 的素理想，则 $\mathrm{Fr}_{P_1}=\mathrm{Fr}_{P_2}$ 当且仅当存在 $K$ 中的元素 $\alpha$，使得 $\alpha P_1=P_2$。

以类似而更复杂的方式，可以刻画 $F$ 的所有阿贝尔扩张。这一理论称为类域论，由 Kronecker、Weber、Hilbert、Takagi 和 Artin 发展而成。上述有关 Frobenius 自同构的主要论断就是 Artin 互反律。Artin–Tate 的讲义从上同调的角度介绍类域论。我的 *Algebraic Number Theory* 则按照 Artin 在 1927 年给出的第一个证明来介绍，并采用了后来 Artin 自己作出的简化。两种方法都值得掌握。

应当从定理 15.1 的角度理解分圆扩张。事实上，设 $K=\mathbf Q(\zeta)$，其中 $\zeta$ 是本原 $n$ 次单位根。对于素数 $p\nmid n$，有 Frobenius 自同构 $\mathrm{Fr}_p$，它对 $\zeta$ 的作用为 $\mathrm{Fr}_p(\zeta)=\zeta^p$。于是

$$
\mathrm{Fr}_{p_1}=\mathrm{Fr}_{p_2}\quad\text{当且仅当}\quad p_1\equiv p_2\pmod n.
$$

为了在同一个框架中包含定理 15.1 和分圆情形，必须对广义理想类表述类域论的结果，而不能只用通常的理想类；在通常的定义中，两个理想等价，当且仅当它们相差一个非零域元素的乘法因子。关于这些广义理想类的描述，参见我的 *Algebraic Number Theory*。

非阿贝尔情形困难得多。我将简要说明一个特殊情形，借此展示其中的一些特点。问题在于，要对非阿贝尔扩张完成 Artin 对阿贝尔扩张所完成的工作。Artin 甚至说过，问题不在于给出证明，而在于表述需要证明的内容。Langlands 等人在 20 世纪 60 年代的洞见表明，Artin 其实判断错了：两方面都有困难。Shimura 在这一方向作过几项涉及“模形式”的计算 [Sh 66]。Langlands 提出了若干将伽罗瓦群与“自守形式”联系起来的猜想，表明答案位于更深的理论之中，而这些理论仅仅表述起来就已十分困难，更不用说证明了。20 世纪 70 年代，Serre 与 Deligne 取得了重大进展，证明了 Langlands 猜想的第一个情形 [DeS 74]。

<span class="original-page-anchor" id="pdf-page-331" aria-hidden="true"></span>

研究非阿贝尔伽罗瓦群，要通过它们的线性“表示”。例如，设 $l$ 是素数。可以问：$GL_n(\mathbf F_l)$、$GL_2(\mathbf F_l)$ 或 $PGL_2(\mathbf F_l)$ 是否作为 $\mathbf Q$ 上的伽罗瓦群出现，又是“如何”出现的？问题是寻找自然的对象，使伽罗瓦群在线性映射的意义下作用于这些对象，从而自然地得到这个伽罗瓦群与上述某个线性群之间的同构。指示寻找这些对象的方向的理论，远远超出了本课程的水平；它们属于模函数理论，同时涉及分析与代数，为数论应用提供背景。我仍选择一个特殊情形来展示其中的特点。

设 $K$ 是 $\mathbf Q$ 的有限伽罗瓦扩张，其伽罗瓦群为

$$
G=\operatorname{Gal}(K/\mathbf Q).
$$

设

$$
\rho:G\longrightarrow GL_2(\mathbf F_l)
$$

是 $G$ 到某个素数 $l$ 所对应的有限域 $\mathbf F_l$ 上的 $2\times2$ 矩阵群的同态。这种同态称为 $G$ 的一个**表示**。由初等线性代数，若

$$
M=\begin{pmatrix}a&b\\c&d\end{pmatrix}
$$

是一个 $2\times2$ 矩阵，则其迹与行列式分别定义为

$$
\operatorname{tr}(M)=a+d\qquad\text{和}\qquad\det M=ad-bc.
$$

因此，对于 $\sigma\in G$，可以取迹 $\operatorname{tr}\rho(\sigma)$ 和行列式 $\det\rho(\sigma)$。

考虑以 $q$ 为变量的无穷乘积：

$$
\Delta(q)=q\prod_{n=1}^\infty(1-q^n)^{24}=\sum_{n=1}^\infty a_nq^n.
$$

系数 $a_n$ 是整数，且 $a_1=1$。

**定理 15.2。** 对每个素数 $l$，存在唯一的 $\mathbf Q$ 的伽罗瓦扩张 $K$，其伽罗瓦群为 $G$，并存在单射同态

$$
\rho:G\longrightarrow GL_2(\mathbf F_l),
$$

具有如下性质：除有限多个素数 $p$ 外，若 $a_p$ 是 $\Delta(q)$ 中 $q^p$ 的系数，则有

$$
\operatorname{tr}\rho(\mathrm{Fr}_p)\equiv a_p\pmod l\qquad\text{和}\qquad
\det\rho(\mathrm{Fr}_p)\equiv p^{11}\pmod l.
$$

此外，对所有 $l\ne2,3,5,7,23,691$ 的素数，$GL_2(\mathbf F_l)$ 中的像 $\rho(G)$ 由满足下列条件的矩阵 $M\in GL_2(\mathbf F_l)$ 组成：$\det M$ 是 $\mathbf F_l^*$ 中的某个元素的十一次幂。

<span class="original-page-anchor" id="pdf-page-332" aria-hidden="true"></span>

上述定理由 Serre 于 1968 年提出为猜想 [Se 68]。第一项结论中所说的存在性，由 Deligne 给出证明 [De 68]。第二项结论描述伽罗瓦群在矩阵群 $GL_2(\mathbf F_l)$ 中究竟有多大，由 Serre 与 Swinnerton-Dyer 得到 [Se 72]、[SwD 73]。

$\Delta(q)$ 的关键在于：若置 $q=e^{2\pi iz}$，其中 $z$ 是上半平面中的变量，则 $\Delta$ 是一个权为 $12$ 的模形式。关于定义和入门介绍，参见 [Se 73] 的最后一章、[La 73]、[La 76] 以及下面的说明。定理 15.2 背后关于权 $\ge2$ 的模形式的一般结果，由 Deligne 得到 [De 73]。权为 $1$ 时的结果由 Deligne–Serre 得到 [DeS 74]。下面概述这一情形。

设 $N$ 是正整数。与 $N$ 相联系，定义 $SL_2(\mathbf Z)$ 的子群

$$
\Gamma(N)\subset\Gamma_1(N)\subset\Gamma_0(N),
$$

其定义由矩阵 $\alpha=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbf Z)$ 所满足的以下条件给出：

$\alpha\in\Gamma(N)$ 当且仅当 $a\equiv d\equiv1\pmod N$，且 $b\equiv c\equiv0\pmod N$；

$\alpha\in\Gamma_1(N)$ 当且仅当 $a\equiv d\equiv1\pmod N$，且 $c\equiv0\pmod N$；

$\alpha\in\Gamma_0(N)$ 当且仅当 $c\equiv0\pmod N$。

设 $f$ 是上半平面 $\mathfrak H=\{z\in\mathbf C,\ \operatorname{Im}(z)>0\}$ 上的函数，$k$ 是整数。对于

$$
\gamma=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in SL_2(\mathbf R),
$$

定义 $f\circ[\gamma]_k$（一个右作用）如下：

$$
f\circ[\gamma]_k(z)=(cz+d)^{-k}f(\gamma z),\qquad\text{其中}\qquad
\gamma z=\frac{az+b}{cz+d}.
$$

设 $\Gamma$ 是 $SL_2(\mathbf Z)$ 中包含 $\Gamma(N)$ 的子群。若满足下列条件，就定义 $f$ 是 **$\Gamma$ 上权为 $k$ 的模形式**：

**$\mathbf M_k$ 1。** $f$ 在 $\mathfrak H$ 上全纯；

**$\mathbf M_k$ 2。** $f$ 在尖点处全纯，即对所有 $\alpha\in SL_2(\mathbf Z)$，函数 $f\circ[\alpha]_k$ 具有幂级数展开

$$
f\circ[\alpha]_k(z)=\sum_{n=0}^\infty a_ne^{2\pi inz/N};
$$

**$\mathbf M_k$ 3。** 对所有 $\gamma\in\Gamma$，都有 $f\circ[\gamma]_k=f$。

若在 **$\mathbf M_k$ 2** 中的幂级数在展开原点取值为零，即幂次从 $n\ge1$ 开始，就称 $f$ 是**尖点形式**。

<span class="original-page-anchor" id="pdf-page-333" aria-hidden="true"></span>

假设 $f$ 是 $\Gamma(N)$ 上权为 $k$ 的模形式。那么 $f$ 是 $\Gamma_1(N)$ 上的模形式，当且仅当 $f(z+1)=f(z)$；等价地，$f$ 具有下列形式的展开：

$$
f(z)=f_\infty(q_z)=\sum_{n=0}^\infty a_nq^n,\qquad\text{其中}\qquad q=q_z=e^{2\pi iz}.
$$

这个幂级数称为 $f$ 的 **$q$ 展开**。

假设 $f$ 在 $\Gamma_1(N)$ 上具有权 $k$。若 $\gamma\in\Gamma_0(N)$，且 $\gamma$ 是上面写出的矩阵，则 $f\circ[\gamma]_k$ 仅依赖于 $d$ 在 $(\mathbf Z/N\mathbf Z)^*$ 中的像，于是将 $f\circ[\gamma]_k$ 记为 $f\circ[d]_k$。设

$$
\varepsilon:(\mathbf Z/N\mathbf Z)^*\longrightarrow\mathbf C^*
$$

是同态，也称为 **Dirichlet 特征标**。若 $\varepsilon(-1)=-1$，就称 $\varepsilon$ 为**奇特征标**；若 $\varepsilon(-1)=1$，则称为**偶特征标**。如果 $f$ 在 $\Gamma_1(N)$ 上具有权 $k$，并且

$$
f\circ[d]_k=\varepsilon(d)f\qquad\text{对所有 }d\in(\mathbf Z/N\mathbf Z)^*,
$$

就称 $f$ 是 **$\Gamma_0(N)$ 上类型为 $(k,\varepsilon)$ 的模形式**。

可以在给定类型的模形式空间上定义一个算子代数。这需要更广泛的背景知识，系统的介绍请参见 [La 76]。在所有这些形式中，可以区别出其中一些是这个 Hecke 代数的特征向量，或者说，是这个代数的特征函数。于是可以如下表述 Deligne–Serre 定理。

设 $f\ne0$ 是 $\Gamma_0(N)$ 上类型为 $(1,\varepsilon)$ 的模形式，因此 $f$ 的权为 $1$。假设 $\varepsilon$ 是奇特征标。假设 $f$ 是 Hecke 代数的特征函数，其 $q$ 展开为 $f_\infty=\sum a_nq^n$，并已归一化为 $a_1=1$。那么存在唯一的 $\mathbf Q$ 的有限伽罗瓦扩张 $K$，其伽罗瓦群为 $G$，并存在表示 $\rho:G\longrightarrow GL_2(\mathbf C)$，实际上它是单射同态，使得对所有素数 $p\nmid N$，$\rho(\mathrm{Fr}_p)$ 的特征多项式为

$$
X^2-a_pX+\varepsilon(p).
$$

表示 $\rho$ 不可约，当且仅当 $f$ 是尖点形式。

注意，表示 $\rho$ 的值在 $GL_2(\mathbf C)$ 中。关于 Serre 的大量工作及其有关有限域 $\mathbf F$ 上 $GL_2(\mathbf F)$ 中伽罗瓦群表示的猜想，参见 [Se 87]。大致说来，由 Taniyama–Shimura 的一个猜想和 Langlands 猜想开创的一般思想认为，所见的一切都是“模的”。定理 15.2 与 Deligne–Serre 定理，是这一方向上结果的典型。对于有限域 $\mathbf F$ 上 $GL_2(\mathbf F)$ 中的“模”表示，Serre 的猜想已经得到证明，主要由 Ribet 完成 [Ri 90]。由此，沿着 Frey 的一个想法，Ribet 还说明了 Taniyama–Shimura 猜想如何推出费马最后定理 [Ri 90b]。注意，Serre 关于 $GL_2(\mathbf F)$ 中某些表示是模的的猜想，蕴含 Taniyama–Shimura 猜想。

<span class="original-page-anchor" id="pdf-page-334" aria-hidden="true"></span>

### 参考文献

[ArT 68] E. Artin 与 J. Tate, *Class Field Theory*, Benjamin-Addison-Wesley, 1968 (重印者为 Addison-Wesley, 1991)

[De 68] P. Deligne, Formes modulaires et représentations $l$-adiques, *Séminaire Bourbaki* 1968–1969, exp. No. 355

[De 73] P. Deligne, Formes modulaires et représentations de $GL(2)$, *Springer Lecture Notes* **349** (1973), 页码：55–105

[DeS 74] P. Deligne 与 J. P. Serre, Formes modulaires de poids 1, *Ann. Sci. ENS* **7** (1974), 页码：507–530

[La 70] S. Lang, *Algebraic Number Theory*, Springer Verlag, 由下列版本重印： Addison-Wesley (1970)

[La 73] S. Lang, *Elliptic functions*, Springer Verlag, 1973

[La 76] S. Lang, *Introduction to modular forms*, Springer Verlag, 1976

[Ri 90a] K. Ribet, On modular representations of $\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)$ arising from modular forms, *Invent. Math.* **100** (1990), 页码：431–476

[Ri 90b] K. Ribet, From the Taniyama-Shimura conjecture to Fermat's last theorem, *Annales de la Fac. des Sci. Toulouse* (1990), 页码：116–139

[Se 68] J.-P. Serre, Une interprétation des congruences relatives à la fonction de Ramanujan, *Séminaire Delange-Pisot-Poitou*, 1967–1968

[Se 72] J.-P. Serre, Congruences et formes modulaires (d'après Swinnerton-Dyer), *Séminaire Bourbaki*, 1971–1972

[Se 73] J.-P. Serre, *A course in arithmetic*, Springer Verlag, 1973

[Se 87] J.-P. Serre, Sur les représentations modulaires de degré 2 de $\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)$, *Duke Math. J.* **54** (1987), 页码：179–230

[Shi 66] G. Shimura, A reciprocity law in non-solvable extensions, *J. reine angew. Math.* **221** (1966), 页码：209–220

[Shi 71] G. Shimura, *Introduction to the arithmetic theory of automorphic functions*, Iwanami Shoten and Princeton University Press, 1971

[SwD 73] H. P. Swinnerton-Dyer, On $l$-adic representations and congruences for coefficients of modular forms, （Antwerp 会议） *Springer Lecture Notes* **350** (1973)

## 习题

**1。** 下列多项式的伽罗瓦群是什么？

(a) $\mathbf Q$ 上的 $X^3-X-1$。

(b) $\mathbf Q$ 上的 $X^3-10$。

(c) $\mathbf Q(\sqrt2)$ 上的 $X^3-10$。

(d) $\mathbf Q(\sqrt{-3})$ 上的 $X^3-10$。

(e) $\mathbf Q(\sqrt{-23})$ 上的 $X^3-X-1$。

(f) $\mathbf Q$、$\mathbf Q(\sqrt5)$、$\mathbf Q(\sqrt{-5})$、$\mathbf Q(i)$ 上的 $X^4-5$。

(g) $\mathbf Q$ 上的 $X^4-a$，其中 $a$ 是任意无平方因子的整数，满足 $a\ne0$、$a\ne\pm1$。

<span class="original-page-anchor" id="pdf-page-335" aria-hidden="true"></span>

(h) $\mathbf Q$ 上的 $X^3-a$，其中 $a$ 是任意无平方因子的整数，满足 $a\ge2$。

(i) $\mathbf Q$、$\mathbf Q(i)$ 上的 $X^4+2$。

(j) $\mathbf Q$ 上的 $(X^2-2)(X^2-3)(X^2-5)(X^2-7)$。

(k) 设 $p_1,\ldots,p_n$ 是互不相同的素数。$\mathbf Q$ 上的 $(X^2-p_1)\cdots(X^2-p_n)$ 的伽罗瓦群是什么？

(l) $\mathbf Q(\sqrt{-3})$ 上的 $(X^3-2)(X^3-3)(X^2-2)$。

(m) $\mathbf C(t)$ 上的 $X^n-t$，其中 $t$ 在复数域 $\mathbf C$ 上超越，$n$ 是正整数。

(n) $\mathbf R(t)$ 上的 $X^4-t$，其中 $t$ 如前。

**2。** 求下列多项式在 $\mathbf Q$ 上的伽罗瓦群。

(a) $X^3+X+1$

(b) $X^3-X+1$

(c) $X^3+2X+1$

(d) $X^3-2X+1$

(e) $X^3-X-1$

(f) $X^3-12X+8$

(g) $X^3+X^2-2X-1$

**3。** 设 $k=\mathbf C(t)$ 是一元有理函数域。求下列多项式在 $k$ 上的伽罗瓦群：

(a) $X^3+X+t$

(b) $X^3-X+t$

(c) $X^3+tX+1$

(d) $X^3-2tX+t$

(e) $X^3-X-t$

(f) $X^3+t^2X-t^3$

**4。** 设 $k$ 是特征不为 $2$ 的域。设 $c\in k$、$c\notin k^2$，并令 $F=k(\sqrt c)$。设 $\alpha=a+b\sqrt c$，其中 $a,b\in k$，且 $a,b$ 不同时为 $0$。令 $E=F(\sqrt\alpha)$。证明下列条件等价。

(1) $E$ 是 $k$ 的伽罗瓦扩张。

(2) $E=F(\sqrt{\alpha'})$，其中 $\alpha'=a-b\sqrt c$。

(3) $\alpha\alpha'=a^2-cb^2\in k^2$ 或 $c\alpha\alpha'\in k^2$。

证明：这些条件成立时，$E$ 是 $k$ 的 $4$ 次循环扩张，当且仅当 $c\alpha\alpha'\in k^2$。

**5。** 设 $k$ 是特征不为 $2,3$ 的域。设 $f(X)$ 和 $g(X)=X^2-c$ 是 $k$ 上的不可约多项式，其次数分别为 $3$ 和 $2$。令 $D$ 为 $f$ 的判别式。假设

$$
[k(D^{1/2}):k]=2\qquad\text{且}\qquad k(D^{1/2})\ne k(c^{1/2}).
$$

在一个代数闭包中，令 $\alpha$ 为 $f$ 的一个根，$\beta$ 为 $g$ 的一个根。证明：

(a) $fg$ 在 $k$ 上的分裂域具有次数 $12$。

(b) 令 $\gamma=\alpha+\beta$。则 $[k(\gamma):k]=6$。

**6。** (a) 设 $K$ 是 $k$ 的 $4$ 次循环扩张，特征不为 $2$，并令 $G_{K/k}=\langle\sigma\rangle$。设 $E$ 为 $K$ 中在 $k$ 上次数为 $2$ 的唯一子域。由于 $[K:E]=2$，存在 $\alpha\in K$，使得 $\alpha^2=\gamma\in E$，且 $K=E(\alpha)$。证明存在 $z\in E$，使得

$$
z\sigma z=-1,\qquad \sigma\alpha=z\alpha,\qquad z^2=\sigma\gamma/\gamma.
$$

(b) 反过来，设 $E$ 是 $k$ 的二次扩张，并令 $G_{E/k}=\langle\tau\rangle$。设 $z\in E$ 满足 $z\tau z=-1$。证明存在 $\gamma\in E$，使得 $z^2=\tau\gamma/\gamma$。于是 $E=k(\gamma)$。令 $\alpha^2=\gamma$，并令 $K=k(\alpha)$。证明 $K$ 是 $k$ 的 $4$ 次伽罗瓦循环扩张。令 $\sigma$ 为 $\tau$ 到 $K$ 的一个扩张。证明 $\sigma$ 是生成 $G_{K/k}$ 的 $K$ 的自同构，满足 $\sigma^2\alpha=-\alpha$ 及 $\sigma\alpha=\pm z\alpha$。若必要，一开始将 $z$ 换成 $-z$，就可以使 $\sigma\alpha=z\alpha$。

<span class="original-page-anchor" id="pdf-page-336" aria-hidden="true"></span>

**7。** (a) 设 $K=\mathbf Q(\sqrt a)$，其中 $a\in\mathbf Z$、$a<0$。证明 $K$ 不能嵌入一个在 $\mathbf Q$ 上的次数被 $4$ 整除的循环扩张中。

(b) 令 $f(X)=X^4+30X^2+45$。设 $\alpha$ 是 $f$ 的一个根。证明 $\mathbf Q(\alpha)$ 是 $\mathbf Q$ 的 $4$ 次循环扩张。

**译校注。** 本小题原书将后一处多项式名称印作大写 $F$；这里所指的是刚定义的 $f$。

(c) 令 $f(X)=X^4+4X^2+2$。证明 $f$ 在 $\mathbf Q$ 上不可约，且伽罗瓦群是循环群。

**8。** 设 $f(X)=X^4+aX^2+b$ 是 $\mathbf Q$ 上的不可约多项式，其根为 $\pm\alpha$、$\pm\beta$，分裂域为 $K$。

(a) 证明 $\operatorname{Gal}(K/\mathbf Q)$ 同构于 $D_8$ 的一个子群，其中 $D_8$ 是除四元数群外的那个 $8$ 阶非阿贝尔群，因此同构于下列群之一：

(i) $\mathbf Z/4\mathbf Z$；(ii) $\mathbf Z/2\mathbf Z\times\mathbf Z/2\mathbf Z$；(iii) $D_8$。

(b) 证明第一种情形发生，当且仅当

$$
\frac{\alpha}{\beta}-\frac{\beta}{\alpha}\in\mathbf Q.
$$

情形 (ii) 发生，当且仅当 $\alpha\beta\in\mathbf Q$ 或 $\alpha^2-\beta^2\in\mathbf Q$。其余情况发生情形 (iii)。（实际上，在 (ii) 中，$\alpha^2-\beta^2\in\mathbf Q$ 的情况不可能发生。它对应于 $D_8\subset S_4$ 的一个子群，该子群同构于 $\mathbf Z/2\mathbf Z\times\mathbf Z/2\mathbf Z$，但在 $\{1,2,3,4\}$ 上并不传递。）

(c) 求多项式

$$
X^4-4X^2-1
$$

在 $\mathbf C$ 中的分裂域 $K$。确定这一分裂域在 $\mathbf Q$ 上的伽罗瓦群，并完整描述子域格和伽罗瓦群的子群格。

**9。** 设 $K$ 是域 $k$ 的有限可分扩张，其次数为素数 $p$。设 $\theta\in K$ 满足 $K=k(\theta)$，并设 $\theta_1,\ldots,\theta_p$ 是某个代数闭包中 $\theta$ 在 $k$ 上的共轭元。令 $\theta=\theta_1$。若 $\theta_2\in k(\theta)$，证明 $K$ 是 $k$ 的伽罗瓦扩张，而且实际上是循环扩张。

**10。** 设 $f(X)\in\mathbf Q[X]$ 是 $n$ 次多项式，$K$ 是 $f$ 在 $\mathbf Q$ 上的分裂域。假设 $\operatorname{Gal}(K/\mathbf Q)$ 是对称群 $S_n$，其中 $n>2$。

(a) 证明 $f$ 在 $\mathbf Q$ 上不可约。

(b) 若 $\alpha$ 是 $f$ 的一个根，证明 $\mathbf Q(\alpha)$ 的唯一自同构是恒等自同构。

(c) 若 $n\ge4$，证明 $\alpha^n\notin\mathbf Q$。

**11。** 若多项式 $f(X)$ 的每个根 $\zeta$ 的倒数 $1/\zeta$ 也都是它的根，就称 $f(X)$ 为**互反多项式**。假设 $f$ 的系数在子域 $k\subset\mathbf R\subset\mathbf C$ 中。若 $f$ 在 $k$ 上不可约，并有一个绝对值为 $1$ 的非实根，证明 $f$ 是偶数次互反多项式。

**12。** $X^5-4X+2$ 在有理数域上的伽罗瓦群是什么？

**13。** 下列多项式在有理数域上的伽罗瓦群是什么？

(a) $X^4+2X^2+X+3$

(b) $X^4+3X^3-3X-2$

(c) $X^6+22X^5-9X^4+12X^3-37X^2-29X-15$

[**提示：** 模 $2,3,5$ 约化。]

**14。** 证明：给定对称群 $S_n$，存在首项系数为 $1$ 的多项式 $f(X)\in\mathbf Z[X]$，其在 $\mathbf Q$ 上的伽罗瓦群为 $S_n$。[**提示：** 模 $2,3,5$ 约化，证明存在一个多项式，其约化具有使伽罗瓦群<span class="original-page-anchor" id="pdf-page-337" aria-hidden="true"></span>包含足够多的循环，从而生成 $S_n$ 的性质。使用中国剩余定理，也使得能够应用 Eisenstein 判别法。]

**15。** 设 $K/k$ 是伽罗瓦扩张，$F$ 是介于 $k$ 与 $K$ 之间的中间域。令 $H$ 为 $\operatorname{Gal}(K/k)$ 中将 $F$ 映入自身的元素组成的子群。证明 $H$ 是 $\operatorname{Gal}(K/F)$ 在 $\operatorname{Gal}(K/k)$ 中的正规化子。

**16。** 设 $K/k$ 是有限伽罗瓦扩张，其群为 $G$。设 $\alpha\in K$，使得 $\{\sigma\alpha\}_{\sigma\in G}$ 是正规基。对 $G$ 的每个子集 $S$，令 $S(\alpha)=\sum_{\sigma\in S}\sigma\alpha$。设 $H$ 是 $G$ 的子群，$F$ 是 $H$ 的不动域。证明 $F$ 在 $k$ 上存在一组基，由形如 $S(\alpha)$ 的元素组成。

### 分圆域

**17。** (a) 设 $n\ge1$ 为奇整数，$k$ 是特征不整除 $2n$ 的域，并且 $k$ 中有一个本原 $n$ 次单位根 $\zeta$。证明 $k$ 中也有一个本原 $2n$ 次单位根。

(b) 设 $k$ 是有理数域的有限扩张。证明 $k$ 中只有有限多个单位根。

**18。** (a) 确定下列域中有哪些单位根：$\mathbf Q(i)$、$\mathbf Q(\sqrt{-2})$、$\mathbf Q(\sqrt2)$、$\mathbf Q(\sqrt{-3})$、$\mathbf Q(\sqrt3)$、$\mathbf Q(\sqrt{-5})$。

(b) 对于哪些整数 $m$，一个本原 $m$ 次单位根在 $\mathbf Q$ 上的次数为 $2$？

**19。** 设 $\zeta$ 是本原 $n$ 次单位根，令 $K=\mathbf Q(\zeta)$。

(a) 若 $n=p^r$（$r\ge1$）是素数幂，证明 $N_{K/\mathbf Q}(1-\zeta)=p$。

(b) 若 $n$ 是合数，且被至少两个素数整除，则 $N_{K/\mathbf Q}(1-\zeta)=1$。

**20。** 设 $f(X)\in\mathbf Z[X]$ 是具有整数系数的非常数多项式。证明 $f(a)$（$a\in\mathbf Z^+$）这些值中出现无穷多个素因子。

*注：* 这是简单的。深刻得多的问题是，是否有无穷多个 $a$，使得 $f(a)$ 是素数。以下三个条件是必要的：

$f$ 的首项系数为正。

该多项式不可约。

值集 $f(\mathbf Z^+)$ 没有大于 $1$ 的公因数。

Bouniakowski 的一个猜想 [Bo 1854] 断言，这些条件也是充分的。后来 Schinzel 重新发现了这一猜想，并将其推广到多个多项式 [Sch 58]。一个特殊情形是猜想 $X^2+1$ 取无穷多个素数值。关于一般猜想以及给出猜想性渐近估计的定量形式的讨论，参见 Bateman 与 Horn [BaH 62]，另见 [HaR 74] 中的说明。更准确地说，设 $f_1,\ldots,f_r$ 为具有整数系数的多项式，满足前两个条件，即首项系数为正且不可约。令

$$
f=f_1\cdots f_r
$$

为它们的乘积，并假设 $f$ 满足第三个条件。定义：

$$
\pi_{(f)}(x)=\text{满足 }n\le x\text{ 且 }f_1(n),\ldots,f_r(n)\text{ 全为素数的正整数 }n\text{ 的个数}.
$$

（忽略那些使某个 $f_i(n)$ 为负的有限多个 $n$ 值。）该<span class="original-page-anchor" id="pdf-page-338" aria-hidden="true"></span>Bateman–Horn 猜想断言

$$
\pi_{(f)}(x)\sim(d_1\cdots d_r)^{-1}C(f)\int_2^x\frac{1}{(\log t)^r}\,dt,
$$

其中

$$
C(f)=\prod_p\left\{\left(1-\frac1p\right)^{-r}\left(1-\frac{N_f(p)}p\right)\right\},
$$

乘积对所有素数 $p$ 取遍，$N_f(p)$ 是同余式

$$
f(n)\equiv0\pmod p
$$

的解的个数。

Bateman 与 Horn 证明了该乘积收敛。当 $r=1$ 且 $f(n)=an+b$，其中 $a,b$ 为互素整数、$a>0$ 时，就得到 Dirichlet 关于等差数列中存在无穷多个素数的定理，以及这些素数的 Dirichlet 密度。

**译校注。** 原书积分下限印作 $0$。按通常的实积分解释，被积函数在 $t=1$ 有不可积奇点；这里的渐近公式应以任意固定的、大于 $1$ 的数作下限，译文取 $2$。原书另称乘积“converges absolutely”（绝对收敛），一般情形下这一说法过强。例如取 $f(X)=X^2+1$，对每个奇素数，乘积因子按照 $p\equiv1$ 或 $3\pmod4$ 分别为 $1-1/(p-1)$ 或 $1+1/(p-1)$。由于奇素数倒数之和发散，各因子与 $1$ 的差的绝对值之和也发散，故这个乘积不是绝对收敛的。

[BaH 62] P. T. Bateman 与 R. Horn, A heuristic asymptotic formula concerning the distribution of prime numbers, *Math. Comp.* **16** (1962) 页码：363–367

[Bo 1854] V. Bouniakowsky, Sur les diviseurs numériques invariables des fonctions rationnelles entières, *Mémoires sc. math. et phys.* T. VI (1854–1855) 页码：307–329

[HaR 74] H. Halberstam 与 H.-E. Richert, *Sieve methods*, Academic Press, 1974

[Sch 58] A. Schinzel 与 W. Sierpinski, Sur certaines hypothèses concernant les nombres premiers, *Acta Arith.* **4** (1958) 页码：185–208

**21。** (a) 设 $a$ 是非零整数，$p$ 是素数，$n$ 是正整数，且 $p\nmid n$。证明 $p\mid\Phi_n(a)$ 当且仅当 $a$ 在 $(\mathbf Z/p\mathbf Z)^*$ 中的周期为 $n$。

(b) 仍假设 $p\nmid n$。证明存在某个 $a\in\mathbf Z$ 使得 $p\mid\Phi_n(a)$，当且仅当 $p\equiv1\pmod n$。由此推出，满足 $\equiv1\pmod n$ 的素数有无穷多个；这是 Dirichlet 关于等差数列中存在素数的定理的一个特例。

**22。** 设 $F=\mathbf F_p$ 是特征为 $p$ 的素域。设 $K$ 是在 $F$ 中添加所有素数 $l\ne p$ 所对应的所有本原 $l$ 次单位根而得到的域。证明 $K$ 是代数闭的。[**提示：** 证明：若 $q$ 是素数、$r\ge1$ 是整数，则存在素数 $l$，使得 $p$ 模 $l$ 的周期为 $q^r$。使用 Van der Waerden 的以下老技巧：设 $l$ 是下述数的一个素因子：

$$
b=\frac{p^{q^r}-1}{p^{q^{r-1}}-1}
=(p^{q^{r-1}}-1)^{q-1}+q(p^{q^{r-1}}-1)^{q-2}+\cdots+q.
$$

若 $l$ 不整除 $p^{q^{r-1}}-1$，就完成了。否则，$l=q$。但在这种情况下，$q^2$ 不整除 $b$，因而存在一个素数 $l\ne q$ 整除 $b$。于是 $F(\zeta_l)$ 在 $F$ 上的次数为 $q^r$，所以 $K$ 包含在 $F$ 上任意次数的子域。]

> **译校注。** 原书提示声称上述断言对每个 $r\ge1$ 成立，但存在例外。例如 $p=3$、$q=2$、$r=1$ 时，$b=(3^2-1)/(3-1)=4$，所以 $q^2$ 确实整除 $b$，而且不存在使 $3$ 模 $l$ 的阶为 $2$ 的素数 $l$。证明本题只须对每个素数 $q$ 得到任意大的 $q$ 幂次数；相应的有限域包含所有较低的素数幂次数子域，因此这个例外不影响题目的结论。原提示保留如上。

**23。** (a) 设 $G$ 是有限阿贝尔群。证明存在 $\mathbf Q$ 的阿贝尔扩张，以 $G$ 为伽罗瓦群。

<span class="original-page-anchor" id="pdf-page-339" aria-hidden="true"></span>

(b) 设 $k$ 是 $\mathbf Q$ 的有限扩张，$G\ne\{1\}$ 是有限阿贝尔群。证明存在无穷多个 $k$ 的阿贝尔扩张，以 $G$ 为伽罗瓦群。

**24。** 证明存在无穷多对非零互素整数 $a,b$，使得 $-4a^3-27b^2$ 是 $\mathbf Z$ 中的平方。

**25。** 设 $k$ 是一个域，其每个有限扩张都是循环扩张。证明存在 $k^a$ 在 $k$ 上的自同构 $\sigma$，使得 $k$ 是 $\sigma$ 的不动域。

**26。** 设 $\mathbf Q^a$ 为 $\mathbf Q$ 的一个固定的代数闭包。设 $E$ 是 $\mathbf Q^a$ 中不包含 $\sqrt2$ 的极大子域；由 Zorn 引理，这样的子域存在。证明 $E$ 的每个有限扩张都是循环扩张。（你的证明应当在将 $\sqrt2$ 换成任意代数无理数时仍然适用。）

**27。** 设 $k$ 是域，$k^a$ 是一个代数闭包，$\sigma$ 是固定 $k$ 的 $k^a$ 的自同构。设 $F$ 是 $\sigma$ 的不动域。证明 $F$ 的每个有限扩张都是循环扩张。（以上两题是 Artin 给出的例子，说明如何在代数闭域中“挖洞”。）

**28。** 设 $E$ 是 $k$ 的代数扩张，并且 $k[X]$ 中每个非常数多项式 $f(X)$ 都在 $E$ 中至少有一个根。证明 $E$ 是代数闭的。[**提示：** 分别讨论可分和纯不可分情形，并使用本原元定理。]

**29。** (a) 设 $K$ 是域 $F$ 的循环扩张，伽罗瓦群 $G$ 由 $\sigma$ 生成。假设特征为 $p$，并且存在整数 $m\ge2$，使得 $[K:F]=p^{m-1}$。设 $\beta\in K$ 满足 $\operatorname{Tr}_F^K(\beta)=1$。证明存在 $\alpha\in K$，使得

$$
\sigma\alpha-\alpha=\beta^p-\beta.
$$

(b) 证明多项式 $X^p-X-\alpha$ 在 $K[X]$ 中不可约。

(c) 若 $\theta$ 是这个多项式的一个根，证明 $F(\theta)$ 是 $F$ 的 $p^m$ 次伽罗瓦循环扩张，而且其伽罗瓦群由 $\sigma$ 的一个扩张 $\sigma^*$ 生成，满足

$$
\sigma^*(\theta)=\theta+\beta.
$$

**30。** 设 $A$ 是阿贝尔群，$G$ 是作用于 $A$ 的有限循环群，其作用由同态 $G\longrightarrow\operatorname{Aut}(A)$ 给出。设 $\sigma$ 是 $G$ 的一个生成元。在 $A$ 上定义迹 $\operatorname{Tr}_G=\operatorname{Tr}$，令 $\operatorname{Tr}(x)=\sum_{\tau\in G}\tau x$。令 $A_{\operatorname{Tr}}$ 表示迹的核，$(1-\sigma)A$ 表示由所有形如 $y-\sigma y$ 的元素组成的 $A$ 的子群。证明

$$
H^1(G,A)\approx A_{\operatorname{Tr}}/(1-\sigma)A.
$$

**31。** 设 $F$ 是有限域，$K$ 是 $F$ 的有限扩张。证明范数 $N_F^K$ 和迹 $\operatorname{Tr}_F^K$ 都是满射，视为从 $K$ 到 $F$ 的映射。

**32。** 设 $E$ 是 $k$ 的有限可分扩张，次数为 $n$。设 $W=(w_1,\ldots,w_n)$ 是 $E$ 中的元素组。设 $\sigma_1,\ldots,\sigma_n$ 为 $E$ 到 $k^a$ 的互不相同的 $k$ 嵌入。将 $W$ 的**判别式**定义为

$$
D_{E/k}(W)=\det(\sigma_iw_j)^2.
$$

证明：

(a) 若 $V=(v_1,\ldots,v_n)$ 是 $E$ 中的另一组元素，且 $C=(c_{ij})$ 是一个元素在 $k$ 中的矩阵，满足 $w_i=\sum c_{ij}v_j$，则

$$
D_{E/k}(W)=\det(C)^2D_{E/k}(V).
$$

<span class="original-page-anchor" id="pdf-page-340" aria-hidden="true"></span>

(b) 判别式是 $k$ 的元素。

(c) 设 $E=k(\alpha)$，并令 $f(X)=\operatorname{Irr}(\alpha,k,X)$。设 $\alpha_1,\ldots,\alpha_n$ 是 $f$ 的根，并设 $\alpha=\alpha_1$。则

$$
f'(\alpha)=\prod_{j=2}^n(\alpha-\alpha_j).
$$

证明

$$
D_{E/k}(1,\alpha,\ldots,\alpha^{n-1})=(-1)^{n(n-1)/2}N_k^E(f'(\alpha)).
$$

(d) 采用 (a) 中的记号。证明 $\det(\operatorname{Tr}(w_iw_j))=(\det(\sigma_iw_j))^2$。[**提示：** 令 $A$ 为矩阵 $(\sigma_iw_j)$。证明 $\vphantom{A}{}^tAA$ 就是矩阵 $(\operatorname{Tr}(w_iw_j))$。]

### 有理函数

**33。** 设 $K=\mathbf C(x)$，其中 $x$ 在 $\mathbf C$ 上超越，并设 $\zeta$ 为 $\mathbf C$ 中的本原三次单位根。令 $\sigma$ 为满足 $\sigma x=\zeta x$ 的 $K$ 在 $\mathbf C$ 上的自同构。令 $\tau$ 为满足 $\tau x=x^{-1}$ 的 $K$ 在 $\mathbf C$ 上的自同构。证明

$$
\sigma^3=1=\tau^2\qquad\text{且}\qquad\tau\sigma=\sigma^{-1}\tau.
$$

证明由 $\sigma$ 和 $\tau$ 生成的自同构群 $G$ 的阶为 $6$，而 $K$ 中被 $G$ 固定的子域 $F$ 就是 $\mathbf C(y)$，其中 $y=x^3+x^{-3}$。

**34。** 举出一个域 $K$ 的例子，使得它在两个不同子域 $E$ 和 $F$ 上的次数分别都为 $2$，但 $K$ 在 $E\cap F$ 上不是代数扩张。

**35。** 设 $k$ 是域，$X$ 是 $k$ 上的变量。设

$$
\varphi(X)=\frac{f(X)}{g(X)}
$$

是 $k(X)$ 中的有理函数，表示为两个互素多项式 $f,g$ 的商。定义 $\varphi$ 的次数为 $\max(\deg f,\deg g)$。令 $Y=\varphi(X)$。

(a) 证明 $\varphi$ 的次数等于域扩张 $k(X)/k(Y)$ 的次数，假设 $Y\notin k$。

(b) 证明 $k(X)$ 在 $k$ 上的每个自同构都能由一个次数为 $1$ 的有理函数 $\varphi$ 表示，因此由下述映射诱导：

$$
X\longmapsto\frac{aX+b}{cX+d},
$$

其中 $a,b,c,d\in k$，且 $ad-bc\ne0$。

(c) 令 $G$ 为 $k(X)$ 在 $k$ 上的自同构群。证明 $G$ 由以下自同构生成：

$$
\tau_b:X\longmapsto X+b,\qquad \sigma_a:X\longmapsto aX\quad(a\ne0),\qquad X\longmapsto X^{-1},
$$

其中 $a,b\in k$。

**36。** 设 $k$ 是具有 $q$ 个元素的有限域。令 $K=k(X)$ 为一元有理函数域。令 $G$ 为由下述映射得到的 $K$ 的自同构群：

$$
X\longmapsto\frac{aX+b}{cX+d}
$$

<span class="original-page-anchor" id="pdf-page-341" aria-hidden="true"></span>

其中 $a,b,c,d\in k$，且 $ad-bc\ne0$。证明下列论断：

(a) $G$ 的阶为 $q^3-q$。

(b) $G$ 的不动域等于 $k(Y)$，其中

$$
Y=\frac{(X^{q^2}-X)^{q+1}}{(X^q-X)^{q^2+1}}.
$$

(c) 设 $H_1$ 是 $G$ 中由映射 $X\longmapsto aX+b$（$a\ne0$）组成的子群。$H_1$ 的不动域为 $k(T)$，其中 $T=(X^q-X)^{q-1}$。

(d) 设 $H_2$ 是 $H_1$ 中由映射 $X\longrightarrow X+b$（$b\in k$）组成的子群。$H_2$ 的不动域等于 $k(Z)$，其中 $Z=X^q-X$。

### Kummer 理论的若干方面

**37。** 设 $k$ 是特征为 $0$ 的域。假设对 $k$ 的每个有限扩张 $E$ 及每个正整数 $n$，指数 $(E^*:E^{*n})$ 都有限。证明对每个正整数 $n$，$k$ 只有有限多个次数为 $n$ 的阿贝尔扩张。

**38。** 设 $a\ne0$、$a\ne\pm1$ 是无平方因子的整数。对每个素数 $p$，令 $K_p$ 为多项式 $X^p-a$ 在 $\mathbf Q$ 上的分裂域。证明 $[K_p:\mathbf Q]=p(p-1)$。对每个无平方因子的整数 $m>0$，令

$$
K_m=\prod_{p\mid m}K_p
$$

为所有 $p\mid m$ 所对应的域 $K_p$ 的合成域。令 $d_m=[K_m:\mathbf Q]$ 为 $K_m$ 在 $\mathbf Q$ 上的次数。证明：若 $m$ 为奇数，则 $d_m=\prod_{p\mid m}d_p$；若 $m$ 为偶数，$m=2n$，则按照 $\sqrt a$ 是否属于 $m$ 次单位根的域 $\mathbf Q(\zeta_m)$，分别有 $d_{2n}=d_n$ 或 $d_{2n}=2d_n$。

**39。** 为简便起见，设 $K$ 是特征为 $0$ 的域。设 $\Gamma$ 是 $K^*$ 的有限生成子群。设 $N$ 是奇正整数。假定对每个素数 $p\mid N$ 都有

$$
\Gamma=\Gamma^{1/p}\cap K,
$$

并且 $\operatorname{Gal}(K(\boldsymbol\mu_N)/K)\approx\mathbf Z(N)^*$。证明：

(a) $\Gamma/\Gamma^N\approx\Gamma/(\Gamma\cap K^{*N})\approx\Gamma K^{*N}/K^{*N}$。

(b) 令 $K_N=K(\boldsymbol\mu_N)$。则

$$
\Gamma\cap K_N^{*N}=\Gamma^N.
$$

[**提示：** 若这两个群不相等，则对于某个素数 $p\mid N$，存在元素 $a\in\Gamma$，使得

$$
a=b^p,\qquad\text{其中 }b\in K_N,\quad\text{但 }b\notin K.
$$

换言之，$a$ 在 $K$ 中不是 $p$ 次幂，却在 $K_N$ 中成为 $p$ 次幂。方程 $X^p-a$ 在 $K$ 上不可约。证明 $b$ 在 $K(\boldsymbol\mu_p)$ 上的次数为 $p$，且 $K(\boldsymbol\mu_p,a^{1/p})$ 不是 $K$ 的阿贝尔扩张，因而 $a^{1/p}$ 在 $K(\boldsymbol\mu_p)$ 上的次数为 $p$。请自行完成证明。]

<span class="original-page-anchor" id="pdf-page-342" aria-hidden="true"></span>

(c) 推出自然的 Kummer 映射

$$
\Gamma/\Gamma^N\longrightarrow\operatorname{Hom}(H_\Gamma(N),\boldsymbol\mu_N)
$$

是同构。

(d) 令 $G_\Gamma(N)=\operatorname{Gal}(K(\Gamma^{1/N},\boldsymbol\mu_N)/K)$。则 $G_\Gamma(N)$ 的交换子群为 $H_\Gamma(N)$，特别地，$\operatorname{Gal}(K_N/K)$ 是 $G_\Gamma(N)$ 的最大阿贝尔商群。

**40。** 设 $K$ 是域，$p$ 是不等于 $K$ 的特征的素数。设 $\Gamma$ 是 $K^*$ 的有限生成子群，并假定 $\Gamma$ 等于它在 $K$ 中的 $p$ 除群，即若 $z\in K$ 且 $z^p\in\Gamma$，则 $z\in\Gamma$。若 $p$ 是奇数，假设 $\boldsymbol\mu_p\subset K$；若 $p=2$，假设 $\boldsymbol\mu_4\subset K$。令

$$
(\Gamma:\Gamma^p)=p^{r+1}.
$$

证明 $\Gamma^{1/p}$ 等于它在 $K(\Gamma^{1/p})$ 中的 $p$ 除群，而且对所有正整数 $m$，都有

$$
[K(\Gamma^{1/p^m}):K]=p^{m(r+1)}.
$$

**41。相对不变量（Sato）。** 设 $k$ 是域，$K$ 是 $k$ 的扩张。设 $G$ 是 $K$ 在 $k$ 上的一个自同构群，并假定 $k$ 是 $G$ 的不动域。（不假定 $K$ 在 $k$ 上代数。）所谓 $G$ 在 $K$ 中的**相对不变量**，是指一个元素 $P\in K$、$P\ne0$，使得对每个 $\sigma\in G$，存在元素 $\chi(\sigma)\in k$ 满足 $P^\sigma=\chi(\sigma)P$。由于 $\sigma$ 是自同构，$\chi(\sigma)\in k^*$。我们称映射 $\chi:G\longrightarrow k^*$ **属于** $P$，并称它为一个**特征标**。证明以下论断：

(a) 上述映射 $\chi$ 是同态。

(b) 若同一个特征标 $\chi$ 同时属于相对不变量 $P$ 和 $Q$，则存在 $c\in k^*$，使得 $P=cQ$。

(c) 相对不变量构成一个乘法群，记为 $I$。若 $I$ 的元素 $P_1,\ldots,P_m$ 在商群 $I/k^*$ 中的像乘法独立，就称它们**模 $k^*$ 乘法独立**；即对于整数 $\nu_1,\ldots,\nu_m$，若

$$
P_1^{\nu_1}\cdots P_m^{\nu_m}=c\in k^*,
$$

则 $\nu_1=\cdots=\nu_m=0$。

(d) 若 $P_1,\ldots,P_m$ 模 $k^*$ 乘法独立，证明它们在 $k$ 上代数独立。[**提示：** 使用 Artin 的特征标定理。]

(e) 假设 $K=k(X_1,\ldots,X_n)$ 是多项式环 $k[X_1,\ldots,X_n]=k[X]$ 的分式域，并假设 $G$ 诱导多项式环的自同构。证明：若 $F_1(X)$ 和 $F_2(X)$ 是相对不变量多项式，则它们的最大公因式也是相对不变量。若 $P(X)=F_1(X)/F_2(X)$ 是相对不变量，并表示为两个互素多项式的商，则 $F_1(X)$ 和 $F_2(X)$ 都是相对不变量。证明相对不变量多项式生成 $I/k^*$。令 $S$ 为不能分解成两个次数均 $\ge1$ 的相对不变量多项式之积的相对不变量多项式所组成的集合。证明 $S/k^*$ 的元素乘法独立，从而 $I/k^*$ 是自由阿贝尔群。[若你了解超越次数，则利用 (d)，可以推出这个群是有限生成的。]

<span class="original-page-anchor" id="pdf-page-343" aria-hidden="true"></span>

**42。** 设 $f(z)$ 是有理函数，其系数属于有理数域的某个有限扩张。假设存在无穷多个单位根 $\zeta$，使得 $f(\zeta)$ 也是单位根。证明存在整数 $n$，使得 $f(z)=cz^n$，其中 $c$ 为某个常数，实际上 $c$ 是单位根。

这道习题可以推广如下：设 $\Gamma_0$ 是复数的有限生成乘法群。设 $\Gamma$ 是由所有满足下述条件的复数 $\gamma$ 组成的群：对某个非零整数 $m$，$\gamma^m$ 属于 $\Gamma_0$。设 $f(z)$ 是具有复系数的有理函数，存在无穷多个 $\gamma\in\Gamma$，使得 $f(\gamma)$ 属于 $\Gamma$。那么仍有 $f(z)=cz^n$，其中 $c,n$ 为某个常数和整数。（参见 *Fundamentals of Diophantine Geometry*。）

**43。** 设 $K/k$ 是伽罗瓦扩张。在群 $G(K/k)=G$ 上定义 **Krull 拓扑**，其开集基由所有形如 $\sigma H$ 的集合组成，其中 $\sigma\in G$，且 $H=G(K/F)$，$F$ 为包含于 $K$ 中的 $k$ 的某个有限扩张。

(a) 证明：若仅取其中 $F$ 在 $k$ 上为有限伽罗瓦扩张的那些集合 $\sigma H$，便得到同一拓扑的另一个基。

(b) 投射极限 $\varprojlim G/H$ 嵌入直积中：

$$
\varprojlim_HG/H\longrightarrow\prod_HG/H.
$$

在直积上赋予乘积拓扑。由初等点集拓扑中的 Tychonoff 定理，这个直积是紧的，因为它是有限群的直积，而有限群是紧的，当然也是离散的。证明逆极限 $\varprojlim G/H$ 在直积中是闭的，因而是紧的。

(c) 推出 $G(K/k)$ 是紧的。

(d) 证明 $G(K/k)$ 的每个有限指数闭子群都是开子群。

(e) 证明 $G(K/k)$ 的闭子群恰好是形如 $G(K/F)$ 的子群，其中 $F$ 为包含于 $K$ 中的 $k$ 的某个扩张。

(f) 设 $H$ 为 $G$ 的任意子群，$F$ 为 $H$ 的不动域。证明 $G(K/F)$ 是 $H$ 在 $G$ 中的闭包。

**44。** 设 $k$ 是一个域，其每个有限扩张都是循环扩张，而且对每个整数 $n$，都有一个次数为 $n$ 的扩张。证明伽罗瓦群 $G=G(k^a/k)$ 是逆极限 $\varprojlim\mathbf Z/m\mathbf Z$，其中 $m\mathbf Z$ 遍历按包含关系排序的 $\mathbf Z$ 的所有理想。证明这个极限同构于以下各极限的直积：

$$
\prod_p\lim_{n\to\infty}\mathbf Z/p^n\mathbf Z=\prod_p\mathbf Z_p,
$$

其中取遍所有素数 $p$；换言之，它同构于所有 $p$ 进整数的直积。

**45。** 设 $k$ 是完美域，$k^a$ 是其代数闭包。设 $\sigma\in G(k^a/k)$ 是无限阶元素，并假设 $k$ 是 $\sigma$ 的不动域。对每个素数 $p$，令 $K_p$ 为所有在 $k$ 上次数是 $p$ 的幂的循环扩张的合成域。

(a) 证明 $k^a$ 是所有扩张 $K_p$ 的合成域。

(b) 证明要么 $K_p=k$，要么 $K_p$ 是 $k$ 的无限循环扩张。换言之，$K_p$ 不能既是 $k$ 的有限循环扩张，又满足 $K_p\ne k$。

(c) 假设对某个素数 $p$，$k^a=K_p$，所以 $k^a$ 是由 $p$ 扩张组成的无限循环塔。设 $u$ 是一个 $p$ 进可逆元，$u\in\mathbf Z_p^*$，且 $u$ 不表示有理数。定义 $\sigma^u$，并证明 $\sigma$、$\sigma^u$ 线性独立<span class="original-page-anchor" id="pdf-page-344" aria-hidden="true"></span>在 $\mathbf Z$ 上，即由 $\sigma$ 和 $\sigma^u$ 生成的群是秩为 $2$ 的自由阿贝尔群。特别地，$\{\sigma\}$ 与 $\{\sigma,\sigma^u\}$ 具有相同的不动域 $k$。

### Witt 向量

**46。** 设 $x_1,x_2,\ldots$ 是在整数环 $\mathbf Z$ 上代数独立的元素序列。对每个整数 $n\ge1$，定义

$$
x^{(n)}=\sum_{d\mid n}d x_d^{n/d}.
$$

证明 $x_n$ 能用 $d\mid n$ 所对应的 $x^{(d)}$ 表示，且系数为有理数。

采用向量记号，将 $(x_1,x_2,\ldots)$ 称为向量 $x$ 的 **Witt 分量**，将 $(x^{(1)},x^{(2)},\ldots)$ 称为它的**幽灵分量**。称 $x$ 为一个 **Witt 向量**。

定义幂级数

$$
f_x(t)=\prod_{n\ge1}(1-x_nt^n).
$$

证明

$$
-t\frac{d}{dt}\log f_x(t)=\sum_{n\ge1}x^{(n)}t^n.
$$

[若 $f(t)$ 是幂级数，则 $\frac{d}{dt}\log f(t)$ 表示 $f'(t)/f(t)$，其中导数 $f'(t)$ 按形式求导。]

若 $x,y$ 是两个 Witt 向量，则*对幽灵分量逐分量*定义它们的和与积，即

$$
(x+y)^{(n)}=x^{(n)}+y^{(n)}.
$$

那么 $(x+y)_n$ 是什么呢？证明

$$
f_x(t)f_y(t)=\prod(1-(x+y)_nt^n)=f_{x+y}(t).
$$

**译校注。** 原书中间的乘积印作 $\prod(1+(x+y)_nt^n)$，其中加号应为减号，与前面对 $f_x$ 的定义一致。仅比较一次项也可看出：左边 $t$ 的系数为 $-(x_1+y_1)$，原印中间乘积却给出 $+(x+y)_1$。

因此 $(x+y)_n$ 是 $x_1,y_1,\ldots,x_n,y_n$ 的整系数多项式。再证明

$$
f_{xy}(t)=\prod_{d,e\ge1}(1-x_d^{m/d}y_e^{m/e}t^m)^{de/m},
$$

其中 $m$ 是 $d,e$ 的最小公倍数，$d,e$ 遍历所有 $\ge1$ 的整数。因此，$(xy)_n$ 也是 $x_1,y_1,\ldots,x_n,y_n$ 的整系数多项式。上述论证来自 Witt 的口头交流，与他原论文中的论证不同。

若 $A$ 是交换环，则取 $\mathbf Z$ 上的多项式环到 $A$ 的同态像，便可看出：可以对分量在 $A$ 中的 Witt 向量定义加法和乘法，而且这些 Witt 向量构成环 $W(A)$。证明 $W$ 是函子，即任意从 $A$ 到交换环 $A'$ 的环同态 $\varphi$，都诱导一个同态 $W(\varphi):W(A)\longrightarrow W(A')$。

<span class="original-page-anchor" id="pdf-page-345" aria-hidden="true"></span>

**47。** 设 $p$ 是素数，考虑将 $W(A)$ 投影到那些分量以下标 $p$ 的幂编号的向量上。现在用以 $p$ 为底的对数来编号这些分量，因此将原来的 $x_{p^n}$ 写成 $x_n$。例如，现在的 $x_0$ 表示原来的 $x_1$。对 Witt 向量 $x=(x_0,x_1,\ldots,x_n,\ldots)$，定义

$$
Vx=(0,x_0,x_1,\ldots)\qquad\text{和}\qquad Fx=(x_0^p,x_1^p,\ldots).
$$

因此 $V$ 是移位算子。有 $V\circ F=F\circ V$。证明

$$
(Vx)^{(n)}=px^{(n-1)}\qquad\text{和}\qquad x^{(n)}=(Fx)^{(n-1)}+p^nx_n.
$$

由定义还可得

$$
x^{(n)}=x_0^{p^n}+px_1^{p^{n-1}}+\cdots+p^nx_n.
$$

**48。** 设 $k$ 是特征为 $p$ 的域，并考虑 $W(k)$。那么 $V$ 是 $W(k)$ 的加法自同态，$F$ 是 $W(k)$ 到自身的环同态。此外，若 $x\in W(k)$，则

$$
px=VFx.
$$

若 $x,y\in W(k)$，则 $(V^ix)(V^jy)=V^{i+j}(F^jx\cdot F^iy)$。对 $a\in k$，用 $\{a\}$ 表示 Witt 向量 $(a,0,0,\ldots)$。于是可以符号地写成

$$
x=\sum_{i=0}^\infty V^i\{x_i\}.
$$

**译校注。** 原书乘积公式中 $F$ 的指数分别印作 $pj$、$pi$，即 $V^{i+j}(F^{pj}x\cdot F^{pi}y)$。按照习题 47 中对算子 $F$ 的定义，正确指数应为 $j$、$i$。例如取 $i=1,j=0$，应得到 $(Vx)y=V(xFy)$，这也可由通用幽灵分量公式推出。若取 $k=\mathbf F_p(t)$、$x=1$、$y=\{t\}$，原印公式会给出 $V\{t^{p^p}\}$，而正确结果是 $V\{t^p\}$。

证明：若 $x\in W(k)$ 且 $x_0\ne0$，则 $x$ 是 $W(k)$ 的可逆元。*提示：* 有

$$
1-x\{x_0^{-1}\}=Vy,
$$

于是

$$
x\{x_0^{-1}\}\sum_0^\infty(Vy)^i=(1-Vy)\sum_0^\infty(Vy)^i=1.
$$

**49。** 再设 $n\ge1$ 为整数，$p$ 为素数。设 $k$ 是特征为 $p$ 的域。令 $W_n(k)$ 为截断 Witt 向量 $(x_0,\ldots,x_{n-1})$ 的环，其分量在 $k$ 中。将 $W_n(k)$ 看作加法群。若 $x\in W_n(k)$，定义 $\wp(x)=Fx-x$。则 $\wp$ 是同态。若 $K$ 是 $k$ 的伽罗瓦扩张，$\sigma\in G(K/k)$，且 $x\in W_n(K)$，可以定义 $\sigma x$ 的分量为 $(\sigma x_0,\ldots,\sigma x_{n-1})$。证明 Witt 向量的 Hilbert 定理 90 的类似结论，并证明第一上同调群是平凡的。（取一个迹不为 $0$ 的向量，并按定理 10.1 的证明中的同样方法找到一个上边界。）

**译校注。** 原书此处印作“first homology group”（第一同调群），但所要求的 Hilbert 90 结论、上边界及定理 10.1 的引用，针对的都是第一上同调群 $H^1$。

**50。** 若 $x\in W_n(k)$，证明存在 $\xi\in W_n(\overline k)$，使得 $\wp(\xi)=x$。用归纳法进行：先求解第一个分量，再证明向量 $(0,\alpha_1,\ldots,\alpha_{n-1})$ 在 $\wp$ 的像中，当且仅当 $(\alpha_1,\ldots,\alpha_{n-1})$ 在 $\wp$ 的像中。归纳证明：若对 $k$ 的某个扩张 $k'$，有 $\xi,\xi'\in W_n(k')$，且 $\wp\xi=\wp\xi'$，则 $\xi-\xi'$ 是分量均在素域中的向量。因此，对于给定 $x\in W_n(k)$，$\wp\xi=x$ 的所有解之差都是分量在素域中的向量，这样的向量共有 $p^n$ 个。定义

$$
k(\xi)=k(\xi_0,\ldots,\xi_{n-1}),
$$

<span class="original-page-anchor" id="pdf-page-346" aria-hidden="true"></span>

或者符号地记为

$$
k(\wp^{-1}x).
$$

证明它是 $k$ 的伽罗瓦扩张，并证明 $k$ 的 $p^n$ 次循环扩张，恰好是形如 $k(\wp^{-1}x)$ 的扩张，其中向量 $x$ 满足 $x_0\notin\wp k$。

**51。** 利用 $W_n(k)$，建立 $k$ 的指数为 $p^n$ 的阿贝尔扩张的 Kummer 理论。换言之，证明在 $W_n(k)$ 的包含 $\wp W_n(k)$ 的子群 $B$ 与上述阿贝尔扩张之间，存在双射

$$
B\longmapsto K_B,
$$

其中 $K_B=k(\wp^{-1}B)$。所有这些结果都来自 Witt；参见 §8 末的参考文献，尤其是 [Wi 37]。作必要的对应调整后，证明与正文中 Kummer 理论的证明相同。

### 进一步的进展与方向

20 世纪 90 年代，本章所提到的一些问题取得了重大进展。最突出的是 Wiles 证明了 Shimura–Taniyama 猜想的足够部分，从而推出费马最后定理 [Wil 95]、[TaW 95]。

[TaW 95] R. Taylor 与 A. Wiles，Ring-theoretic properties or certain Hecke algebras，*Annals of Math.* **141**（1995），第 553–572 页

[Wil 95] A. Wiles，Modular elliptic curves and Fermat's last theorem，*Annals. of Math.* **141**（1995），第 443–551 页

随后，完整的 Shimura–Taniyama 猜想的证明发表于 [BrCDT 01]。

[BrCDT 01] C. Breuil、B. Conrad、F. Diamond、R. Taylor，On the modularity of elliptic curves over $\mathbf Q$: Wild 3-adic exercises，*J. Amer. Math. Soc.* **14**（2001），第 843–939 页

**译校注。** 原书将该论文的页码范围印作倒序的“843–839”；据 [King's College London 的科研记录](https://kclpure.kcl.ac.uk/portal/en/publications/on-the-modularity-of-elliptic-curves-over-q-wild-3-adic-exercises/)，正确范围为 843–939。

在一个截然不同的方向上，Neukirch 开始研究用绝对伽罗瓦群刻画数域 [Ne 68]、[Ne 69a]、[Ne 69b]，并对 $\mathbf Q$ 的伽罗瓦扩张证明了这一刻画。他的结果由 Ikeda 与 Uchida 推广，随后提出的猜想也由他们证明 [Ik 77]、[Uch 77]、[Uch 79]、[Uch 81]。Pop 将这些结果推广到了 $\mathbf Q$ 的有限生成扩张，即函数域 [Pop 94]；他的文献中还列有这些问题以及代数几何相关问题的更广泛的参考文献。有关这些文献，见本书末的参考文献表。
