---
title: "第五章 代数扩张"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第二部分导言：代数方程","link":"/library/volume-86/part-02"}
next: {"text":"第六章 伽罗瓦理论","link":"/library/volume-86/chapter-006"}
---

# 第五章 代数扩张

<span class="original-page-anchor" id="pdf-page-238" aria-hidden="true"></span>

在这一章关于多项式方程的初步讨论中，我们将证明：给定域上的一个多项式，总存在该域的某个扩张，使得多项式在其中有根；我们还将证明代数闭包的存在性。我们对这类扩张作初步研究，包括其自同构，并以有限域的代数扩张作为例子。

## §1. 有限扩张与代数扩张

设 $F$ 是一个域。如果 $F$ 是域 $E$ 的子域，我们也称 $E$ 是 $F$ 的一个**扩张域**。可以将 $E$ 看作 $F$ 上的向量空间；根据这个向量空间的维数是有限还是无限，我们分别称 $E$ 是 $F$ 的**有限**扩张或**无限**扩张。

设 $F$ 是域 $E$ 的子域。如果存在 $F$ 中不全为 $0$ 的元素 $a_0,\ldots,a_n$ $(n\geq1)$，使得

$$
a_0+a_1\alpha+\cdots+a_n\alpha^n=0,
$$

就称 $E$ 中的元素 $\alpha$ 在 $F$ 上是**代数的**。

如果 $\alpha\neq0$ 且 $\alpha$ 是代数的，那么总可以找到如上的元素 $a_i$，使得 $a_0\neq0$（约去 $\alpha$ 的适当次幂即可）。

设 $X$ 是 $F$ 上的一个变元。也可以这样表述：$\alpha$ 在 $F$ 上是代数的，当且仅当同态

$$
F[X]\to E
$$

<span class="original-page-anchor" id="pdf-page-239" aria-hidden="true"></span>

在 $F$ 上为恒等映射且把 $X$ 映到 $\alpha$ 的同态有非零的核。在这种情形下，这个核是一个主理想，由单个多项式 $p(X)$ 生成；可以假设它的首项系数为 $1$。于是有同构

$$
F[X]/(p(X))\approx F[\alpha],
$$

而由于 $F[\alpha]$ 是整环，可知 $p(X)$ 是不可约的。将 $p(X)$ 规范化，使其首项系数为 $1$ 后，$p(X)$ 就由 $\alpha$ 唯一确定；我们称它为 $\alpha$ 在 $F$ 上的**不可约多项式**。有时将其记作 $\operatorname{Irr}(\alpha,F,X)$。

如果 $E$ 的每个元素都在 $F$ 上是代数的，就称 $F$ 的扩张 $E$ 是**代数扩张**。

**命题 1.1。** *设 $E$ 是 $F$ 的有限扩张。那么 $E$ 在 $F$ 上是代数扩张。*

*证明。* 设 $\alpha\in E$，$\alpha\neq0$。$\alpha$ 的各次幂

$$
1,\alpha,\alpha^2,\ldots,\alpha^n
$$

不可能对所有正整数 $n$ 都在 $F$ 上线性无关，否则 $E$ 在 $F$ 上的维数将是无限的。这些幂之间的一个线性关系表明，$\alpha$ 在 $F$ 上是代数的。

注意，命题 1.1 的逆命题不成立：无限代数扩张是存在的。我们以后将看到，复数域中由所有在 $\mathbf Q$ 上代数的数组成的子域，是 $\mathbf Q$ 的无限扩张。

如果 $E$ 是 $F$ 的一个扩张，我们用

$$
[E:F]
$$

表示 $E$ 作为 $F$ 上向量空间的维数。这个维数可以是无限的。

**命题 1.2。** *设 $k$ 是一个域，$F\subset E$ 是 $k$ 的扩张域。那么*

$$
[E:k]=[E:F][F:k].
$$

*如果 $\{x_i\}_{i\in I}$ 是 $F$ 在 $k$ 上的一组基，$\{y_j\}_{j\in J}$ 是 $E$ 在 $F$ 上的一组基，那么 $\{x_iy_j\}_{(i,j)\in I\times J}$ 是 $E$ 在 $k$ 上的一组基。*

*证明。* 设 $z\in E$。由假设，存在元素 $\alpha_j\in F$，其中几乎所有 $\alpha_j=0$，使得

$$
z=\sum_{j\in J}\alpha_jy_j.
$$

对每个 $j\in J$，存在元素 $b_{ji}\in k$，其中几乎所有都等于 $0$，使得

<span class="original-page-anchor" id="pdf-page-240" aria-hidden="true"></span>

$$
\alpha_j=\sum_{i\in I}b_{ji}x_i,
$$

因而

$$
z=\sum_j\sum_i b_{ji}x_iy_j.
$$

这表明 $\{x_iy_j\}$ 是 $E$ 在 $k$ 上的一族生成元。我们必须证明它是线性无关的。设 $\{c_{ij}\}$ 是 $k$ 中的一族元素，其中几乎所有都为 $0$，并且

$$
\sum_j\sum_i c_{ij}x_iy_j=0.
$$

那么对每个 $j$，都有

$$
\sum_i c_{ij}x_i=0,
$$

因为元素 $y_j$ 在 $F$ 上线性无关。最后，由于 $\{x_i\}$ 是 $F$ 在 $k$ 上的一组基，对每个 $i$ 都有 $c_{ij}=0$，由此证明了命题。

**推论 1.3。** *$k$ 的扩张 $E$ 是有限的，当且仅当 $E$ 在 $F$ 上是有限的，并且 $F$ 在 $k$ 上是有限的。*

与群的情形一样，我们将扩张域组成的序列

$$
F_1\subset F_2\subset\cdots\subset F_n
$$

定义为一个**域塔**。域塔称为**有限的**，当且仅当每一步扩张都是有限的。

设 $k$ 是一个域，$E$ 是其扩张域，$\alpha\in E$。用 $k(\alpha)$ 表示 $E$ 中同时包含 $k$ 与 $\alpha$ 的最小子域。它由所有商 $f(\alpha)/g(\alpha)$ 组成，其中 $f,g$ 是系数在 $k$ 中的多项式，且 $g(\alpha)\neq0$。

**命题 1.4。** *设 $\alpha$ 在 $k$ 上是代数的。那么 $k(\alpha)=k[\alpha]$，并且 $k(\alpha)$ 在 $k$ 上是有限的。次数 $[k(\alpha):k]$ 等于 $\operatorname{Irr}(\alpha,k,X)$ 的次数。*

*证明。* 令 $p(X)=\operatorname{Irr}(\alpha,k,X)$。设 $f(X)\in k[X]$ 满足 $f(\alpha)\neq0$。那么 $p(X)$ 不整除 $f(X)$，所以存在多项式 $g(X),h(X)\in k[X]$，使得

$$
g(X)p(X)+h(X)f(X)=1.
$$

由此得到 $h(\alpha)f(\alpha)=1$，可见 $f(\alpha)$ 在 $k[\alpha]$ 中可逆。因此 $k[\alpha]$ 不仅是环，而且是域，所以必等于 $k(\alpha)$。设 $d=\deg p(X)$。各次幂

$$
1,\alpha,\ldots,\alpha^{d-1}
$$

在 $k$ 上线性无关，因为否则，假设

$$
a_0+a_1\alpha+\cdots+a_{d-1}\alpha^{d-1}=0
$$

<span class="original-page-anchor" id="pdf-page-241" aria-hidden="true"></span>

其中 $a_i\in k$，且并非所有 $a_i=0$。令 $g(X)=a_0+\cdots+a_{d-1}X^{d-1}$。那么 $g\neq0$ 且 $g(\alpha)=0$。于是 $p(X)$ 整除 $g(X)$，矛盾。最后，设 $f(\alpha)\in k[\alpha]$，其中 $f(X)\in k[X]$。存在多项式 $q(X),r(X)\in k[X]$，使得 $\deg r<d$，并且

$$
f(X)=q(X)p(X)+r(X).
$$

那么 $f(\alpha)=r(\alpha)$，可见 $1,\alpha,\ldots,\alpha^{d-1}$ 生成 $k[\alpha]$ 这个 $k$ 上的向量空间。这就证明了命题。

设 $E,F$ 是域 $k$ 的扩张。如果 $E$ 和 $F$ 都包含在某个域 $L$ 中，我们就用 $EF$ 表示 $L$ 中同时包含 $E$ 与 $F$ 的最小子域，称它为 $E$ 与 $F$ 在 $L$ 中的**合成域**。如果没有给定 $E,F$ 到同一个域 $L$ 中的嵌入，则无法定义合成域。

设 $k$ 是 $E$ 的子域，$\alpha_1,\ldots,\alpha_n$ 是 $E$ 中的元素。用

$$
k(\alpha_1,\ldots,\alpha_n)
$$

表示 $E$ 中包含 $k$ 和 $\alpha_1,\ldots,\alpha_n$ 的最小子域。它的元素由所有商

$$
\frac{f(\alpha_1,\ldots,\alpha_n)}{g(\alpha_1,\ldots,\alpha_n)}
$$

组成，其中 $f,g$ 是系数在 $k$ 中的 $n$ 元多项式，并且

$$
g(\alpha_1,\ldots,\alpha_n)\neq0.
$$

事实上，这些商的集合构成一个包含 $k$ 和 $\alpha_1,\ldots,\alpha_n$ 的域。反过来，任何包含 $k$ 和

$$
\alpha_1,\ldots,\alpha_n
$$

的域，都必须包含这些商。

注意，当 $(\alpha_1,\ldots,\alpha_n)$ 遍历 $E$ 中元素的有限子族时，所有子域 $k(\alpha_1,\ldots,\alpha_n)$ 的并就是 $E$。我们也可以将*域 $L$ 的子域的任意子族的合成域*定义为包含该族中所有域的最小子域。如果存在 $E$ 中的有限一族元素 $\alpha_1,\ldots,\alpha_n$，使得

$$
E=k(\alpha_1,\ldots,\alpha_n),
$$

就称 $E$ 在 $k$ 上是**有限生成的**。可见，$E$ 是它所有在 $k$ 上有限生成的子域的合成域。

**命题 1.5。** *设 $E$ 是 $k$ 的有限扩张。那么 $E$ 是有限生成的。*

*证明。* 设 $\{\alpha_1,\ldots,\alpha_n\}$ 是 $E$ 作为 $k$ 上向量空间的一组基。那么显然

$$
E=k(\alpha_1,\ldots,\alpha_n).
$$

<span class="original-page-anchor" id="pdf-page-242" aria-hidden="true"></span>

如果 $E=k(\alpha_1,\ldots,\alpha_n)$ 是有限生成的，$F$ 是 $k$ 的扩张，且 $F,E$ 都包含在 $L$ 中，那么

$$
EF=F(\alpha_1,\ldots,\alpha_n),
$$

并且 $EF$ 在 $F$ 上是有限生成的。我们经常画出下面的图：

![合成域的域包含关系图](/library/volume-86/diagrams/pdf-0242-compositum.png)

向上倾斜的线表示域之间的包含关系。我们也称 $F$ 的扩张 $EF$ 是 $E$ 到 $F$ 的**平移**，或称为 $E$ 到 $F$ 的**提升**。

设 $\alpha$ 在域 $k$ 上是代数的。设 $F$ 是 $k$ 的扩张，并假设 $k(\alpha),F$ 都包含在某个域 $L$ 中。那么 $\alpha$ 在 $F$ 上也是代数的。事实上，$\alpha$ 在 $k$ 上的不可约多项式的系数当然也属于 $F$，因而给出了 $\alpha$ 的各次幂在 $F$ 上的一个线性关系。

假设我们有一个域塔：

$$
k\subset k(\alpha_1)\subset k(\alpha_1,\alpha_2)\subset\cdots\subset k(\alpha_1,\ldots,\alpha_n),
$$

其中每个域都由前一个域添加单个元素生成。假设每个 $\alpha_i$ 都在 $k$ 上是代数的，$i=1,\ldots,n$。作为前面说明的一个特例，注意 $\alpha_{i+1}$ 在 $k(\alpha_1,\ldots,\alpha_i)$ 上是代数的。因此域塔的每一步都是代数扩张。

**命题 1.6。** *设 $E=k(\alpha_1,\ldots,\alpha_n)$ 是域 $k$ 的有限生成扩张，并且对每个 $i=1,\ldots,n$，$\alpha_i$ 都在 $k$ 上是代数的。那么 $E$ 在 $k$ 上是有限代数扩张。*

*证明。* 由上述说明，$E$ 可以作为一个域塔的终点而得到，其中每一步都是由一个代数元生成的，所以由命题 1.4，每一步都是有限扩张。由推论 1.3 得出 $E$ 在 $k$ 上是有限的，再由命题 1.1 得出它是代数的。

设 $\mathfrak C$ 是某个扩张域 $F\subset E$ 的类。如果 $\mathfrak C$ 满足以下条件，就称它是**特选的**：

(1) 设 $k\subset F\subset E$ 是一个域塔。扩张 $k\subset E$ 属于 $\mathfrak C$，当且仅当 $k\subset F$ 属于 $\mathfrak C$，且 $F\subset E$ 属于 $\mathfrak C$。

(2) 如果 $k\subset E$ 属于 $\mathfrak C$，$F$ 是 $k$ 的任意扩张，并且 $E,F$ 都包含在某个域中，那么 $F\subset EF$ 属于 $\mathfrak C$。

(3) 如果 $k\subset F$ 与 $k\subset E$ 都属于 $\mathfrak C$，且 $F,E$ 是同一个域的子域，那么 $k\subset FE$ 属于 $\mathfrak C$。

<span class="original-page-anchor" id="pdf-page-243" aria-hidden="true"></span>

说明这些性质的图如下：

![特选类的三个性质的示意图](/library/volume-86/diagrams/pdf-0243-extension-properties.png)

这些域的格图在处理扩张域时极富启发性。

注意，条件 (3) 在形式上可以由前两个条件推出。事实上，将 $EF$ 在 $k$ 上的扩张看成一个逐步为 $k\subset F\subset EF$ 的域塔即可。

在记号方面，用 $E/F$ 代替 $F\subset E$ 来表示扩张是很方便的。这不会与商群混淆，因为当 $E$ 是 $F$ 的扩张域时，我们绝不会用记号 $E/F$ 表示这种商群。

**命题 1.7。** *代数扩张的类是特选的，有限扩张的类也是特选的。*

*证明。* 先考虑有限扩张的类。我们已经证明了条件 (1)。对于条件 (2)，假设 $E/k$ 是有限的，设 $F$ 是 $k$ 的任意扩张。由命题 1.5，存在元素 $\alpha_1,\ldots,\alpha_n\in E$，使得 $E=k(\alpha_1,\ldots,\alpha_n)$。那么 $EF=F(\alpha_1,\ldots,\alpha_n)$，所以 $EF/F$ 由有限个代数元生成。应用命题 1.6，得出 $EF/F$ 是有限的。

接着考虑代数扩张的类，设

$$
k\subset F\subset E
$$

是一个域塔。假设 $E$ 在 $k$ 上是代数的。那么当然 $F$ 在 $k$ 上是代数的，而 $E$ 在 $F$ 上也是代数的。反过来，假设域塔的每一步都是代数扩张。设 $\alpha\in E$。则 $\alpha$ 满足方程

$$
a_n\alpha^n+\cdots+a_0=0,
$$

其中 $a_i\in F$，且并非所有 $a_i=0$。令 $F_0=k(a_n,\ldots,a_0)$。由命题 1.6，$F_0$ 在 $k$ 上是有限的，并且 $\alpha$ 在 $F_0$ 上是代数的。由域塔

$$
k\subset F_0=k(a_n,\ldots,a_0)\subset F_0(\alpha)
$$

以及其中每一步都是有限扩张这一事实，得出 $F_0(\alpha)$ 在 $k$ 上是有限的，因此 $\alpha$ 在 $k$ 上是代数的。这就证明了 $E$ 在 $k$ 上是代数的，也证明了代数扩张满足条件 (1)。我们已经指出条件 (2) 成立，即一个元素在提升后仍然是代数的，因此扩张也具有这一性质。

<span class="original-page-anchor" id="pdf-page-244" aria-hidden="true"></span>

**说明。** 有限生成扩张确实构成一个特选类，但证明条件 (1) 的一部分所需的一个论证，必须用到比目前更多的工具才能完成。参见超越扩张一章。

## §2. 代数闭包

本节和下一节将讨论从一个域到另一个域的嵌入。因此，我们先定义一些术语。

设 $E$ 是域 $F$ 的扩张，设

$$
\sigma:F\to L
$$

是从 $F$ 到 $L$ 的一个**嵌入**（即单同态）。那么 $\sigma$ 诱导 $F$ 与其像 $\sigma F$ 之间的同构，后者有时记作 $F^\sigma$。如果从 $E$ 到 $L$ 的嵌入 $\tau$ 在 $F$ 上的限制等于 $\sigma$，就称 $\tau$ 是**在 $\sigma$ 上的**嵌入。我们也称 $\tau$ **延拓了 $\sigma$**。如果 $\sigma$ 是恒等映射，则称 $\tau$ 是 $E$ **在 $F$ 上的**嵌入。

这些定义也可以在更一般的范畴中作出，因为它们只须依靠图表就能获得意义：

![在映射或域上的嵌入的定义图](/library/volume-86/diagrams/pdf-0244-embeddings.png)

我们将使用指数记号（以避免括号），因此用 $F^\sigma$ 代替 $\sigma F$；对多项式 $f$，将 $\sigma$ 作用于其系数后所得的多项式记作 $f^\sigma$，而不用 $\sigma f$。参见第二章 §5。

**说明。** 设 $f(X)\in F[X]$ 是一个多项式，$\alpha$ 是 $f$ 在 $E$ 中的一个根。设 $f(X)=a_0+\cdots+a_nX^n$。那么

$$
0=f(\alpha)=a_0+a_1\alpha+\cdots+a_n\alpha^n.
$$

如果 $\tau$ 如上延拓 $\sigma$，则 $\tau\alpha$ 是 $f^\sigma$ 的一个根，因为

$$
0=\tau(f(\alpha))=a_0^\sigma+a_1^\sigma(\tau\alpha)+\cdots+a_n^\sigma(\tau\alpha)^n.
$$

在研究嵌入时，关于代数扩张到其自身的嵌入的一个引理也很有用。为此注意，如果 $\sigma:E\to L$ 是在 $k$ 上的嵌入（即在 $k$ 上诱导恒等映射），那么可以将 $\sigma$ 看作向量空间的一个 $k$ 同态，因为 $E,L$ 都可以看作 $k$ 上的向量空间。此外，$\sigma$ 是单射。

<span class="original-page-anchor" id="pdf-page-245" aria-hidden="true"></span>

**引理 2.1。** *设 $E$ 是 $k$ 的代数扩张，$\sigma:E\to E$ 是 $E$ 在 $k$ 上到其自身的嵌入。那么 $\sigma$ 是自同构。*

*证明。* 由于 $\sigma$ 是单射，只须证明它是满射。设 $\alpha$ 是 $E$ 的一个元素，$p(X)$ 是它在 $k$ 上的不可约多项式，$E'$ 是由 $p(X)$ 所有属于 $E$ 的根生成的 $E$ 的子域。那么 $E'$ 是有限生成的，因此是 $k$ 的有限扩张。此外，$\sigma$ 必将 $p(X)$ 的根映到 $p(X)$ 的根，所以 $\sigma$ 将 $E'$ 映入自身。由于 $\sigma$ 在 $k$ 上诱导恒等映射，可以把它看作向量空间的 $k$ 同态。因为 $\sigma$ 是单射，它的像 $\sigma(E')$ 是 $E'$ 的一个子空间，且维数同样为 $[E':k]$。因此 $\sigma(E')=E'$。由于 $\alpha\in E'$，所以 $\alpha$ 在 $\sigma$ 的像中，引理得证。

设 $E,F$ 是域 $k$ 的扩张，并包含在某个更大的域 $L$ 中。可以构造由 $F$ 的元素在 $E$ 上生成的环 $E[F]$。于是 $E[F]=F[E]$，而 $EF$ 是这个环的分式域。显然，$E[F]$ 的元素可以写成

$$
a_1b_1+\cdots+a_nb_n
$$

的形式，其中 $a_i\in E$，$b_i\in F$。因此 $EF$ 是这些元素所组成的分式的域。

**引理 2.2。** *设 $E_1,E_2$ 是域 $k$ 的扩张，并包含在某个更大的域 $E$ 中，$\sigma$ 是从 $E$ 到某个域 $L$ 的嵌入。那么*

$$
\sigma(E_1E_2)=\sigma(E_1)\sigma(E_2).
$$

*证明。* 将 $\sigma$ 作用于上述类型的元素的一个商，例如

$$
\sigma\left(\frac{a_1b_1+\cdots+a_nb_n}{a'_1b'_1+\cdots+a'_mb'_m}\right)=\frac{a_1^\sigma b_1^\sigma+\cdots+a_n^\sigma b_n^\sigma}{a_1'{}^\sigma b_1'{}^\sigma+\cdots+a_m'{}^\sigma b_m'{}^\sigma},
$$

可见其像是 $\sigma(E_1)\sigma(E_2)$ 中的元素。显然，像 $\sigma(E_1E_2)$ 就是 $\sigma(E_1)\sigma(E_2)$。

设 $k$ 是一个域，$f(X)$ 是 $k[X]$ 中次数 $\geq1$ 的多项式。我们考虑寻找 $k$ 的一个扩张 $E$，使得 $f$ 在其中有根的问题。如果 $p(X)$ 是 $k[X]$ 中整除 $f(X)$ 的不可约多项式，那么 $p(X)$ 的任何根也是 $f(X)$ 的根，所以只须考虑不可约多项式。

设 $p(X)$ 是不可约的，考虑典范同态

$$
\sigma:k[X]\to k[X]/(p(X)).
$$

那么 $\sigma$ 在 $k$ 上诱导一个同态，其核为 $0$，因为 $k$ 的每个非零元素在 $k$ 中都可逆，都生成单位理想，而 $1$ 不属于这个核。设 $\xi$ 是 $X$ 在 $\sigma$ 下的像，即 $\xi=\sigma(X)$ 是 $X$ 模 $p(X)$ 的剩余类。那么

$$
p^\sigma(\xi)=p^\sigma(X^\sigma)=(p(X))^\sigma=0.
$$

<span class="original-page-anchor" id="pdf-page-246" aria-hidden="true"></span>

因此 $\xi$ 是 $p^\sigma$ 的一个根，所以在 $\sigma k$ 上是代数的。现在我们已经找到了 $\sigma k$ 的一个扩张，即 $\sigma k(\xi)$，使得 $p^\sigma$ 在其中有根。

通过一个简单的集合论论证，我们将得到：

**命题 2.3。** *设 $k$ 是一个域，$f$ 是 $k[X]$ 中次数 $\geq1$ 的多项式。那么存在 $k$ 的一个扩张 $E$，使得 $f$ 在其中有根。*

*证明。* 可以假设 $f=p$ 是不可约的。我们已经证明，存在域 $F$ 及嵌入

$$
\sigma:k\to F,
$$

使得 $p^\sigma$ 在 $F$ 中有根 $\xi$。取集合 $S$，使其基数与 $F-\sigma k$（即 $\sigma k$ 在 $F$ 中的补集）的基数相同，并且与 $k$ 不交。令 $E=k\cup S$。可以把 $\sigma:k\to F$ 延拓为从 $E$ 到 $F$ 上的双射。现在在 $E$ 上定义域结构。如果 $x,y\in E$，定义

$$
xy=\sigma^{-1}(\sigma(x)\sigma(y)),
$$

$$
x+y=\sigma^{-1}(\sigma(x)+\sigma(y)).
$$

限制到 $k$ 时，这里的加法和乘法与原来域 $k$ 中给定的加法和乘法一致，而且显然 $k$ 是 $E$ 的子域。令 $\alpha=\sigma^{-1}(\xi)$。于是显然有 $p(\alpha)=0$，正如所要求的。

**推论 2.4。** *设 $k$ 是一个域，$f_1,\ldots,f_n$ 是 $k[X]$ 中次数 $\geq1$ 的多项式。那么存在 $k$ 的一个扩张 $E$，使得每个 $f_i$ 都在其中有根，$i=1,\ldots,n$。*

*证明。* 设 $E_1$ 是一个使 $f_1$ 在其中有根的扩张。可以将 $f_2$ 看作 $E_1$ 上的多项式。取 $E_1$ 的扩张 $E_2$，使得 $f_2$ 在其中有根。归纳地继续这一过程，立即得到推论。

如果 $L[X]$ 中每个次数 $\geq1$ 的多项式都在 $L$ 中有根，就称域 $L$ 是**代数闭的**。

**定理 2.5。** *设 $k$ 是一个域。那么存在一个代数闭域，以 $k$ 为子域。*

*证明。* 我们先构造 $k$ 的一个扩张 $E_1$，使得 $k[X]$ 中每个次数 $\geq1$ 的多项式都在其中有根。可以按如下方法进行（Artin）。对 $k[X]$ 中每个次数 $\geq1$ 的多项式 $f$，配以一个字母 $X_f$，令 $S$ 是所有这些字母 $X_f$ 的集合（于是 $S$ 与 $k[X]$ 中次数 $\geq1$ 的多项式的集合之间存在双射）。构造多项式环 $k[S]$，并断言由 $k[S]$ 中所有多项式 $f(X_f)$ 生成的理想不是单位理想。如果它是单位理想，那么在这个理想中就有一个有限组合等于 $1$：

$$
g_1f_1(X_{f_1})+\cdots+g_nf_n(X_{f_n})=1
$$

<span class="original-page-anchor" id="pdf-page-247" aria-hidden="true"></span>

其中 $g_i\in k[S]$。为简便起见，用 $X_i$ 代替 $X_{f_i}$。多项式 $g_i$ 实际上只涉及有限多个变元，记为 $X_1,\ldots,X_N$（其中 $N\geq n$）。于是我们的关系式写成

$$
\sum_{i=1}^n g_i(X_1,\ldots,X_N)f_i(X_i)=1.
$$

设 $F$ 是一个有限扩张，使得每个多项式 $f_1,\ldots,f_n$ 都在其中有根，记 $\alpha_i$ 为 $f_i$ 在 $F$ 中的一个根，$i=1,\ldots,n$。对 $i>n$，令 $\alpha_i=0$。在关系式中以 $\alpha_i$ 代入 $X_i$，得到 $0=1$，矛盾。

设 $\mathfrak m$ 是包含 $k[S]$ 中所有多项式 $f(X_f)$ 所生成的理想的一个极大理想。那么 $k[S]/\mathfrak m$ 是一个域，并且我们有典范映射

$$
\sigma:k[S]\to k[S]/\mathfrak m.
$$

对于任意次数 $\geq1$ 的多项式 $f\in k[X]$，多项式 $f^\sigma$ 在 $k[S]/\mathfrak m$ 中有一个根，而后者是 $\sigma k$ 的扩张。使用与命题 2.3 中同样的集合论论证，得出存在 $k$ 的一个扩张 $E_1$，使得 $k[X]$ 中每个次数 $\geq1$ 的多项式 $f$ 都在 $E_1$ 中有根。

归纳地，可以构造一列域

$$
E_1\subset E_2\subset E_3\subset\cdots\subset E_n\cdots,
$$

使得 $E_n[X]$ 中每个次数 $\geq1$ 的多项式都在 $E_{n+1}$ 中有根。令 $E$ 为所有域 $E_n$ 的并，$n=1,2,\ldots$。那么 $E$ 自然成为一个域，因为若 $x,y\in E$，则存在某个 $n$，使得 $x,y\in E_n$，于是可以在 $E_n$ 中取积或和 $xy$ 或 $x+y$。这显然与满足 $x,y\in E_n$ 的 $n$ 的选取无关，并在 $E$ 上定义了域结构。$E[X]$ 中每个多项式的系数都属于某个子域 $E_n$，所以它在 $E_{n+1}$ 中有根，进而在 $E$ 中有根，正如所要求的。

**推论 2.6。** *设 $k$ 是一个域。存在一个扩张 $k^a$，它在 $k$ 上是代数的，并且是代数闭的。*

*证明。* 设 $E$ 是 $k$ 的一个代数闭扩张，令 $k^a$ 为 $E$ 中所有在 $k$ 上代数的子扩张的并。那么 $k^a$ 在 $k$ 上是代数的。如果 $\alpha\in E$ 且 $\alpha$ 在 $k^a$ 上是代数的，那么由命题 1.7，$\alpha$ 在 $k$ 上是代数的。如果 $f$ 是 $k^a[X]$ 中次数 $\geq1$ 的多项式，那么 $f$ 在 $E$ 中有一个根 $\alpha$，而 $\alpha$ 在 $k^a$ 上是代数的。因此 $\alpha$ 属于 $k^a$，且 $k^a$ 是代数闭的。

注意，如果 $L$ 是一个代数闭域，$f\in L[X]$ 的次数 $\geq1$，那么存在 $c\in L$ 以及 $\alpha_1,\ldots,\alpha_n\in L$，使得

$$
f(X)=c(X-\alpha_1)\cdots(X-\alpha_n).
$$

事实上，$f$ 在 $L$ 中有一个根 $\alpha_1$，所以存在 $g(X)\in L[X]$，使得

$$
f(X)=(X-\alpha_1)g(X).
$$

如果 $\deg g\geq1$，就可以归纳地重复这个论证，将 $f$ 表示为<span class="original-page-anchor" id="pdf-page-248" aria-hidden="true"></span>各项 $(X-\alpha_i)$ $(i=1,\ldots,n)$ 与一个元素 $c\in L$ 的积。注意 $c$ 是 $f$ 的首项系数，即

$$
f(X)=cX^n+\text{较低次项}.
$$

因此，如果 $f$ 的系数属于 $L$ 的子域 $k$，那么 $c\in k$。

设 $k$ 是一个域，$\sigma:k\to L$ 是从 $k$ 到代数闭域 $L$ 的嵌入。我们想研究把 $\sigma$ 延拓到 $k$ 的代数扩张 $E$ 的问题。先考虑 $E$ 由单个元素生成的特殊情形。

设 $E=k(\alpha)$，其中 $\alpha$ 在 $k$ 上是代数的。令

$$
p(X)=\operatorname{Irr}(\alpha,k,X).
$$

设 $\beta$ 是 $p^\sigma$ 在 $L$ 中的一个根。给定 $k(\alpha)=k[\alpha]$ 中的一个元素，可以将其写成 $f(\alpha)$ 的形式，其中 $f(X)\in k[X]$ 是某个多项式。通过映射

$$
f(\alpha)\mapsto f^\sigma(\beta)
$$

定义 $\sigma$ 的一个延拓。

这个定义确实是良定义的，即与用来表示 $k[\alpha]$ 中该元素的多项式 $f(X)$ 的选取无关。事实上，如果 $g(X)\in k[X]$ 且 $g(\alpha)=f(\alpha)$，则 $(g-f)(\alpha)=0$，所以 $p(X)$ 整除 $g(X)-f(X)$。因此 $p^\sigma(X)$ 整除 $g^\sigma(X)-f^\sigma(X)$，于是 $g^\sigma(\beta)=f^\sigma(\beta)$。现在显然，这个映射是一个同态，在 $k$ 上诱导 $\sigma$，而且是 $\sigma$ 到 $k(\alpha)$ 的延拓。因此得到：

**命题 2.7。** *$\sigma$ 到 $k(\alpha)$ 的所有可能延拓的个数 $\leq\deg p$，并且等于 $p$ 在 $k^a$ 中不同根的个数。*

这是一个重要事实，我们以后将作更细致的分析。目前，我们关心的是 $\sigma$ 到 $k$ 的任意代数扩张的延拓。应用 Zorn 引理可以得到这样的延拓。

**定理 2.8。** *设 $k$ 是一个域，$E$ 是 $k$ 的代数扩张，$\sigma:k\to L$ 是从 $k$ 到代数闭域 $L$ 的嵌入。那么存在 $\sigma$ 到 $E$ 在 $L$ 中的嵌入的延拓。如果 $E$ 是代数闭的，且 $L$ 在 $\sigma k$ 上是代数的，那么 $\sigma$ 的任意这种延拓都是从 $E$ 到 $L$ 上的同构。*

*证明。* 设 $S$ 是所有二元组 $(F,\tau)$ 的集合，其中 $F$ 是 $E$ 中包含 $k$ 的子域，$\tau$ 是 $\sigma$ 到 $F$ 在 $L$ 中的嵌入的延拓。对于这样的二元组 $(F,\tau)$ 与 $(F',\tau')$，如果 $F\subset F'$ 且 $\tau'|F=\tau$，就记 $(F,\tau)\leq(F',\tau')$。注意 $S$ 非空［它包含 $(k,\sigma)$］，并且是归纳有序的：如果 $\{(F_i,\tau_i)\}$ 是一个全序子集，则令 $F=\bigcup F_i$，并将 $F$ 上的 $\tau$ 定义为在每个 $F_i$ 上等于 $\tau_i$。那么 $(F,\tau)$ 是这个全序子集的一个上界。应用 Zorn 引理，取 $S$ 中的一个极大元素 $(K,\lambda)$。则 $\lambda$ 是 $\sigma$ 的延拓，我们断言 $K=E$。否则存在 $\alpha\in E$，<span class="original-page-anchor" id="pdf-page-249" aria-hidden="true"></span>且 $\alpha\notin K$。根据上面的讨论，嵌入 $\lambda$ 可以延拓到 $K(\alpha)$，这与 $(K,\lambda)$ 的极大性矛盾。这就证明存在 $\sigma$ 到 $E$ 的延拓。我们仍用 $\sigma$ 表示这个延拓。

如果 $E$ 是代数闭的，且 $L$ 在 $\sigma k$ 上是代数的，那么 $\sigma E$ 是代数闭的，而 $L$ 在 $\sigma E$ 上是代数的，因此 $L=\sigma E$。

作为推论，我们得到域 $k$ 的“代数闭包”的某种唯一性。

**推论 2.9。** *设 $k$ 是一个域，$E,E'$ 是 $k$ 的代数扩张。假设 $E,E'$ 都是代数闭的。那么存在从 $E$ 到 $E'$ 上的同构*

$$
\tau:E\to E',
$$

*它在 $k$ 上诱导恒等映射。*

*证明。* 将 $k$ 上的恒等映射延拓为从 $E$ 到 $E'$ 的嵌入，并应用定理即可。

可见，$k$ 的一个既是代数闭的又是代数的扩张，在同构意义下是唯一确定的。这样的扩张称为 $k$ 的一个**代数闭包**，经常记作 $k^a$。事实上，除非另有说明，我们只用符号 $k^a$ 表示代数闭包。

现在有必要回顾一下，在一般范畴中同构和自同构的一般情形。

设 $\mathfrak A$ 是一个范畴，$A,B$ 是 $\mathfrak A$ 中的对象。用 $\operatorname{Iso}(A,B)$ 表示从 $A$ 到 $B$ 上的同构的集合。假设至少存在一个这样的同构 $\sigma:A\to B$，其逆为 $\sigma^{-1}:B\to A$。如果 $\varphi$ 是 $A$ 的自同构，则 $\sigma\circ\varphi:A\to B$ 仍是同构。如果 $\psi$ 是 $B$ 的自同构，则 $\psi\circ\sigma:A\to B$ 仍是同构。此外，自同构群 $\operatorname{Aut}(A)$ 和 $\operatorname{Aut}(B)$ 在映射

$$
\varphi\mapsto\sigma\circ\varphi\circ\sigma^{-1},
$$

$$
\sigma^{-1}\circ\psi\circ\sigma\mapsfrom\psi
$$

下同构，这两个映射互为逆映射。同构 $\sigma\circ\varphi\circ\sigma^{-1}$ 正是使下图交换的同构：

$$
\begin{array}{ccc}
A&\xrightarrow{\sigma}&B\\
\varphi\downarrow&&\downarrow\sigma\circ\varphi\circ\sigma^{-1}\\
A&\xrightarrow{\sigma}&B
\end{array}
$$

对于 $\sigma^{-1}\circ\psi\circ\sigma$，也有类似的图。

设 $\tau:A\to B$ 是另一个同构。那么 $\tau^{-1}\circ\sigma$ 是 $A$ 的自同构，而 $\tau\circ\sigma^{-1}$ 是 $B$ 的自同构。因此两个同构之间相差一个（$A$ 或 $B$ 的）自同构。可见，群 $\operatorname{Aut}(B)$ 作用于<span class="original-page-anchor" id="pdf-page-250" aria-hidden="true"></span>集合 $\operatorname{Iso}(A,B)$ 的左边，而 $\operatorname{Aut}(A)$ 作用于集合 $\operatorname{Iso}(A,B)$ 的右边。

我们还看到，$\operatorname{Aut}(A)$ 在一个类似共轭的映射意义下是唯一确定的。这与范畴中泛对象所具有的唯一性很不相同。这样的对象只有恒等自同构，因此在唯一同构的意义下是唯一确定的。

域的代数闭包并非如此，它通常有大量自同构。本章和下一章的大部分内容都致力于研究这些自同构。

**例。** 本书以后将证明，复数域是代数闭的。复共轭是 $\mathbf C$ 的一个自同构。还有许多其他自同构，但其余不等于恒等映射的自同构是不连续的。我们将在超越扩张一章讨论其他可能的自同构。$\mathbf C$ 中由所有在 $\mathbf Q$ 上代数的数组成的子域，是 $\mathbf Q$ 的一个代数闭包 $\mathbf Q^a$。容易看出，$\mathbf Q^a$ 是可数的。事实上，请作为练习证明下面的命题：

*如果 $k$ 是一个无限域，那么 $k$ 的任意代数扩张都与 $k$ 有相同的基数。*

如果 $k$ 是可数的，可以先枚举 $k$ 中的所有多项式，再按次数枚举有限扩张，最后枚举任意代数扩张的元素。我们将计数的细节留作练习。

特别地，$\mathbf Q^a\neq\mathbf C$。如果 $\mathbf R$ 是实数域，则 $\mathbf R^a=\mathbf C$。

如果 $k$ 是有限域，那么 $k$ 的代数闭包 $k^a$ 是可数的。事实上，本章稍后将非常详细地描述有限域的代数扩张的性质。

并非所有有趣的域都是复数域的子域。例如，人们想研究域 $\mathbf C(X)$ 的代数扩张，其中 $X$ 是 $\mathbf C$ 上的变元。研究这些扩张相当于研究球面（看作黎曼曲面）的分歧覆盖；事实上，由于我们知道从球面删去有限多个点后所得空间的基本群，因此能够精确了解这类扩张的性质。以后讨论伽罗瓦群时，我们还将提到这个例子。

## §3. 分裂域与正规扩张

设 $k$ 是一个域，$f$ 是 $k[X]$ 中次数 $\geq1$ 的多项式。所谓 $f$ 的一个**分裂域** $K$，是指 $k$ 的一个扩张 $K$，使得 $f$ 在 $K$ 中分裂为一次因子的乘积，即

<span class="original-page-anchor" id="pdf-page-251" aria-hidden="true"></span>

$$
f(X)=c(X-\alpha_1)\cdots(X-\alpha_n),
$$

其中 $\alpha_i\in K$，$i=1,\ldots,n$；并且 $K=k(\alpha_1,\ldots,\alpha_n)$ 由 $f$ 的所有根生成。

**定理 3.1。** *设 $K$ 是多项式 $f(X)\in k[X]$ 的一个分裂域。如果 $E$ 是 $f$ 的另一个分裂域，那么存在同构 $\sigma:E\to K$，在 $k$ 上诱导恒等映射。如果 $k\subset K\subset k^a$，其中 $k^a$ 是 $k$ 的一个代数闭包，那么 $E$ 到 $k^a$ 的任何在 $k$ 上诱导恒等映射的嵌入，都必是从 $E$ 到 $K$ 上的同构。*

*证明。* 设 $K^a$ 是 $K$ 的一个代数闭包。那么 $K^a$ 在 $k$ 上是代数的，因此是 $k$ 的一个代数闭包。由定理 2.8，存在嵌入

$$
\sigma:E\to K^a,
$$

在 $k$ 上诱导恒等映射。我们有分解

$$
f(X)=c(X-\beta_1)\cdots(X-\beta_n),
$$

其中 $\beta_i\in E$，$i=1,\ldots,n$。首项系数 $c$ 属于 $k$。得到

$$
f(X)=f^\sigma(X)=c(X-\sigma\beta_1)\cdots(X-\sigma\beta_n).
$$

$K^a[X]$ 中有唯一分解。由于 $f$ 在 $K[X]$ 中有分解

$$
f(X)=c(X-\alpha_1)\cdots(X-\alpha_n),
$$

可知 $(\sigma\beta_1,\ldots,\sigma\beta_n)$ 与 $(\alpha_1,\ldots,\alpha_n)$ 仅相差一个置换。由此得出，对 $i=1,\ldots,n$ 都有 $\sigma\beta_i\in K$，从而 $\sigma E\subset K$。但 $K=k(\alpha_1,\ldots,\alpha_n)=k(\sigma\beta_1,\ldots,\sigma\beta_n)$，所以 $\sigma E=K$，因为

$$
E=k(\beta_1,\ldots,\beta_n).
$$

定理得证。

注意，多项式 $f(X)\in k[X]$ 总有分裂域，即在 $k$ 的某个给定代数闭包 $k^a$ 中由它的根生成的域。

设 $I$ 是一个指标集，$\{f_i\}_{i\in I}$ 是 $k[X]$ 中一族次数 $\geq1$ 的多项式。所谓这个族的一个**分裂域**，是指 $k$ 的一个扩张 $K$，使得每个 $f_i$ 都在 $K[X]$ 中分裂为一次因子的乘积，且 $K$ 由所有多项式 $f_i$ 的全部根生成，$i\in I$。在大多数应用中，指标集 $I$ 是有限的，但考虑无限代数扩张正变得越来越重要，因此我们将相当系统地讨论它们。还应注意，对于我们将给出的各种命题，即使将讨论限制在有限情形，证明也不会更简单。

设 $k^a$ 是 $k$ 的一个代数闭包，$K_i$ 是 $f_i$ 在 $k^a$ 中的一个分裂域。那么所有 $K_i$ 的合成域就是这个族的一个分裂域，<span class="original-page-anchor" id="pdf-page-252" aria-hidden="true"></span>因为分裂域定义中的两个条件都立即得到满足。此外，定理 3.1 可以立即推广到无限情形：

**推论 3.2。** *设 $K$ 是族 $\{f_i\}_{i\in I}$ 的一个分裂域，$E$ 是另一个分裂域。任意从 $E$ 到 $K^a$ 的、在 $k$ 上诱导恒等映射的嵌入，都给出从 $E$ 到 $K$ 上的同构。*

*证明。* 使用上述记号。注意，$E$ 中包含 $f_i$ 的唯一分裂域 $E_i$，$K$ 中包含 $f_i$ 的唯一分裂域 $K_i$。由定理 3.1，从 $E$ 到 $K^a$ 的任意嵌入 $\sigma$ 必将 $E_i$ 映到 $K_i$ 上，因而将 $E$ 映入 $K$。由于 $K$ 是各域 $K_i$ 的合成域，映射 $\sigma$ 必将 $E$ 映到 $K$ 上，从而诱导从 $E$ 到 $K$ 上的同构。

**说明。** 如果 $I$ 是有限的，而多项式为 $f_1,\ldots,f_n$，那么它们的一个分裂域就是取乘积所得的单个多项式 $f(X)=f_1(X)\cdots f_n(X)$ 的分裂域。不过，即使只讨论有限扩张，同时处理一组多项式而不是单个多项式，仍然是方便的。

**定理 3.3。** *设 $K$ 是 $k$ 的代数扩张，包含在 $k$ 的一个代数闭包 $k^a$ 中。那么下面的条件等价：*

**NOR 1。** *$K$ 在 $k$ 上到 $k^a$ 的每个嵌入都诱导 $K$ 的一个自同构。*

**NOR 2。** *$K$ 是 $k[X]$ 中一族多项式的分裂域。*

**NOR 3。** *$k[X]$ 中每个在 $K$ 中有根的不可约多项式，都在 $K$ 中分裂为一次因子的乘积。*

*证明。* 假设 NOR 1 成立。设 $\alpha$ 是 $K$ 的一个元素，$p_\alpha(X)$ 是它在 $k$ 上的不可约多项式。设 $\beta$ 是 $p_\alpha$ 在 $k^a$ 中的一个根。存在 $k$ 上从 $k(\alpha)$ 到 $k(\beta)$ 上的同构，将 $\alpha$ 映到 $\beta$。将这个同构延拓为从 $K$ 到 $k^a$ 的嵌入。由假设，这个延拓是 $K$ 的一个自同构 $\sigma$，所以 $\sigma\alpha=\beta$ 属于 $K$。因此 $p_\alpha$ 的每个根都属于 $K$，且 $p_\alpha$ 在 $K[X]$ 中分裂为一次因子的乘积。所以，当 $\alpha$ 遍历 $K$ 的所有元素时，$K$ 是族 $\{p_\alpha\}_{\alpha\in K}$ 的分裂域，NOR 2 得到满足。

反过来，假设 NOR 2 成立，设 $\{f_i\}_{i\in I}$ 是以 $K$ 为分裂域的多项式族。如果 $\alpha$ 是某个 $f_i$ 在 $K$ 中的根，则对于 $K$ 在 $k$ 上到 $k^a$ 的任意嵌入 $\sigma$，我们知道 $\sigma\alpha$ 也是 $f_i$ 的根。由于 $K$ 由所有多项式 $f_i$ 的根生成，可知 $\sigma$ 将 $K$ 映入自身。现在应用引理 2.1，得出 $\sigma$ 是自同构。

我们证明 NOR 1 蕴含 NOR 2 的论证，也表明 NOR 3 得到满足。反过来，假设 NOR 3 成立。设 $\sigma$ 是 $K$ 在 $k$ 上到 $k^a$ 的嵌入。设 $\alpha\in K$，$p(X)$ 是它在 $k$ 上的不可约多项式。如果 $\sigma$ 是 $K$ 在 $k$ 上到 $k^a$ 的嵌入，那么 $\sigma$ 把 $\alpha$ 映到 $p(X)$ 的一个根 $\beta$；根据假设，$\beta$ 属于 $K$。因此 $\sigma\alpha$ 属于 $K$，$\sigma$ 将 $K$ 映入自身。由引理 2.1，$\sigma$ 是自同构。

<span class="original-page-anchor" id="pdf-page-253" aria-hidden="true"></span>

满足条件 NOR 1、NOR 2、NOR 3 的 $k$ 的扩张 $K$，称为**正规扩张**。正规扩张的类并不是特选的。例如，容易证明次数为 $2$ 的扩张是正规的，但有理数域的扩张 $\mathbf Q(\sqrt[4]{2})$ 不是正规的（$X^4-2$ 的非实复根不在其中），而这个扩张却可以通过逐次作次数为 $2$ 的扩张得到，即

$$
E=\mathbf Q(\sqrt[4]{2})\supset F\supset\mathbf Q,
$$

其中

$$
F=\mathbf Q(\alpha),\qquad\alpha=\sqrt2\quad\text{且}\quad E=F(\sqrt\alpha).
$$

因此，正规扩张组成的域塔未必是正规的。不过，我们仍有其中的一些性质：

**定理 3.4。** *正规扩张在提升后仍然正规。如果 $K\supset E\supset k$ 且 $K$ 在 $k$ 上正规，则 $K$ 在 $E$ 上正规。如果 $K_1,K_2$ 在 $k$ 上正规，并包含在某个域 $L$ 中，则 $K_1K_2$ 在 $k$ 上正规，$K_1\cap K_2$ 也在 $k$ 上正规。*

*证明。* 对于第一个断言，设 $K$ 在 $k$ 上正规，$F$ 是 $k$ 的任意扩张，并假设 $K,F$ 都包含在某个更大的域中。设 $\sigma$ 是 $KF$ 在 $F$ 上的一个嵌入（嵌入到 $F^a$ 中）。那么 $\sigma$ 在 $F$ 上，因而在 $k$ 上诱导恒等映射；由假设，它在 $K$ 上的限制将 $K$ 映入自身。得到 $(KF)^\sigma=K^\sigma F^\sigma=KF$，因此 $KF$ 在 $F$ 上正规。

假设 $K\supset E\supset k$，且 $K$ 在 $k$ 上正规。设 $\sigma$ 是 $K$ 在 $E$ 上的嵌入。那么 $\sigma$ 也是 $K$ 在 $k$ 上的嵌入，由定义即可得到断言。

最后，如果 $K_1,K_2$ 在 $k$ 上正规，那么对于 $K_1K_2$ 在 $k$ 上的任意嵌入 $\sigma$，都有

$$
\sigma(K_1K_2)=\sigma(K_1)\sigma(K_2),
$$

断言再次由假设推出。关于交的断言成立，因为

$$
\sigma(K_1\cap K_2)=\sigma(K_1)\cap\sigma(K_2).
$$

注意，如果 $K$ 是 $k$ 的有限生成正规扩张，设

$$
K=k(\alpha_1,\ldots,\alpha_n),
$$

而 $p_1,\ldots,p_n$ 分别是 $\alpha_1,\ldots,\alpha_n$ 在 $k$ 上的不可约多项式，那么 $K$ 已经是有限族 $p_1,\ldots,p_n$ 的分裂域。我们以后将研究何时 $K$ 是单个不可约多项式的分裂域。

<span class="original-page-anchor" id="pdf-page-254" aria-hidden="true"></span>

## §4. 可分扩张

设 $E$ 是域 $F$ 的代数扩张，设

$$
\sigma:F\to L
$$

是从 $F$ 到代数闭域 $L$ 的嵌入。我们更仔细地研究 $\sigma$ 到 $E$ 的延拓。$\sigma$ 的任何这样的延拓都会将 $E$ 映到 $L$ 的一个在 $\sigma F$ 上代数的子域上。因此，为了我们的目的，将假设 $L$ 在 $\sigma F$ 上是代数的，也就是说，它等于 $\sigma F$ 的一个代数闭包。

设 $S_\sigma$ 是 $\sigma$ 到 $E$ 在 $L$ 中的嵌入的所有延拓的集合。

设 $L'$ 是另一个代数闭域，$\tau:F\to L'$ 是一个嵌入。与前面一样，假设 $L'$ 是 $\tau F$ 的一个代数闭包。由定理 2.8，存在同构 $\lambda:L\to L'$，延拓了定义在域 $\sigma F$ 上的映射 $\tau\circ\sigma^{-1}$。这由下图说明：

![比较两个嵌入的延拓的图](/library/volume-86/diagrams/pdf-0254-separable-degree.png)

用 $S_\tau$ 表示从 $E$ 到 $L'$ 的所有延拓 $\tau$ 的嵌入的集合。

如果 $\sigma^*\in S_\sigma$ 是 $\sigma$ 到 $E$ 在 $L$ 中的嵌入的一个延拓，那么 $\lambda\circ\sigma^*$ 是 $\tau$ 到 $E$ 在 $L'$ 中的嵌入的一个延拓，因为限制到 $F$ 时，有

$$
\lambda\circ\sigma^*=\tau\circ\sigma^{-1}\circ\sigma=\tau.
$$

因此，$\lambda$ 诱导从 $S_\sigma$ 到 $S_\tau$ 的映射。显然，其逆映射由 $\lambda^{-1}$ 诱导，所以 $S_\sigma,S_\tau$ 在映射

$$
\sigma^*\mapsto\lambda\circ\sigma^*
$$

下构成双射。

特别地，$S_\sigma,S_\tau$ 的基数相同。因此这个基数只依赖于扩张 $E/F$，记作

$$
[E:F]_s.
$$

我们称它为 $E$ 在 $F$ 上的**可分次数**。它主要在 $E/F$ 有限时有意义。

**定理 4.1。** *设 $E\supset F\supset k$ 是一个域塔。那么*

$$
[E:k]_s=[E:F]_s[F:k]_s.
$$

*此外，如果 $E$ 在 $k$ 上是有限的，则 $[E:k]_s$ 是有限的，并且*

<span class="original-page-anchor" id="pdf-page-255" aria-hidden="true"></span>

$$
[E:k]_s\leq[E:k].
$$

*可分次数至多等于扩张次数。*

*证明。* 设 $\sigma:k\to L$ 是从 $k$ 到代数闭域 $L$ 的嵌入。设 $\{\sigma_i\}_{i\in I}$ 是 $\sigma$ 到 $F$ 的所有不同延拓组成的族；对每个 $i$，设 $\{\tau_{ij}\}$ 是 $\sigma_i$ 到 $E$ 的所有不同延拓组成的族。由前面的讨论，每个 $\sigma_i$ 恰有 $[E:F]_s$ 个到 $E$ 在 $L$ 中的嵌入的延拓。嵌入的集合 $\{\tau_{ij}\}$ 恰好包含

$$
[E:F]_s[F:k]_s
$$

个元素。$E$ 在 $\sigma$ 上到 $L$ 的任意嵌入，必是某个 $\tau_{ij}$，因此第一个公式成立，即我们在域塔中有乘法性。

对于第二个断言，假设 $E/k$ 是有限的。那么可以将 $E$ 表示为一个扩张塔，其中每一步都由单个元素生成：

$$
k\subset k(\alpha_1)\subset k(\alpha_1,\alpha_2)\subset\cdots\subset k(\alpha_1,\ldots,\alpha_r)=E.
$$

如果归纳地定义 $F_{\nu+1}=F_\nu(\alpha_{\nu+1})$，则由命题 2.7，

$$
[F_\nu(\alpha_{\nu+1}):F_\nu]_s\leq[F_\nu(\alpha_{\nu+1}):F_\nu].
$$

因此，这个不等式在域塔的每一步都成立。由乘法性，得出它对于扩张 $E/k$ 也成立，证毕。

**推论 4.2。** *设 $E$ 在 $k$ 上是有限的，且 $E\supset F\supset k$。等式*

$$
[E:k]_s=[E:k]
$$

*成立，当且仅当对应的等式在域塔的每一步都成立，即对于 $E/F$ 和 $F/k$ 都成立。*

*证明。* 显然。

以后将证明（而且这并不难证明），当 $E$ 在 $k$ 上是有限的时，$[E:k]_s$ 整除次数 $[E:k]$。将这个商定义为 $[E:k]_i$，于是

$$
[E:k]_s[E:k]_i=[E:k].
$$

由可分次数和扩张次数在域塔中的乘法性可知，符号 $[E:k]_i$ 在域塔中也具有乘法性。我们将在 §6 中更详细地讨论它。

设 $E$ 是 $k$ 的有限扩张。如果 $[E:k]_s=[E:k]$，就称 $E$ 在 $k$ 上是**可分的**。

如果 $k(\alpha)$ 在 $k$ 上可分，就称在 $k$ 上代数的元素 $\alpha$ 在 $k$ 上是**可分的**。可见，这个条件等价于说不可约多项式 $\operatorname{Irr}(\alpha,k,X)$ 没有重根。

多项式 $f(X)\in k[X]$ 如果没有重根，就称它是**可分的**。

<span class="original-page-anchor" id="pdf-page-256" aria-hidden="true"></span>

如果 $\alpha$ 是可分多项式 $g(X)\in k[X]$ 的一个根，那么 $\alpha$ 在 $k$ 上的不可约多项式整除 $g$，因此 $\alpha$ 在 $k$ 上可分。

注意，如果 $k\subset F\subset K$，且 $\alpha\in K$ 在 $k$ 上可分，那么 $\alpha$ 在 $F$ 上也可分。事实上，如果 $f$ 是 $k[X]$ 中满足 $f(\alpha)=0$ 的可分多项式，那么 $f$ 的系数也属于 $F$，所以 $\alpha$ 在 $F$ 上可分。（可以说，一个可分元素在提升后仍然可分。）

**定理 4.3。** *设 $E$ 是 $k$ 的有限扩张。那么 $E$ 在 $k$ 上可分，当且仅当 $E$ 的每个元素都在 $k$ 上可分。*

*证明。* 假设 $E$ 在 $k$ 上可分，设 $\alpha\in E$。考虑域塔

$$
k\subset k(\alpha)\subset E.
$$

由推论 4.2，必有 $[k(\alpha):k]=[k(\alpha):k]_s$，所以 $\alpha$ 在 $k$ 上可分。反过来，假设 $E$ 的每个元素都在 $k$ 上可分。可以写成 $E=k(\alpha_1,\ldots,\alpha_n)$，其中每个 $\alpha_i$ 都在 $k$ 上可分。考虑域塔

$$
k\subset k(\alpha_1)\subset k(\alpha_1,\alpha_2)\subset\cdots\subset k(\alpha_1,\ldots,\alpha_n).
$$

由于每个 $\alpha_i$ 在 $k$ 上可分，所以对 $i\geq2$，每个 $\alpha_i$ 在 $k(\alpha_1,\ldots,\alpha_{i-1})$ 上可分。因此，由域塔定理得出 $E$ 在 $k$ 上可分。

注意，最后这个论证表明：如果 $E$ 由有限多个各自在 $k$ 上可分的元素生成，那么 $E$ 在 $k$ 上可分。

设 $E$ 是 $k$ 的任意代数扩张。如果每个有限生成子扩张都在 $k$ 上可分，也就是说，对任意 $\alpha_1,\ldots,\alpha_n\in E$，扩张 $k(\alpha_1,\ldots,\alpha_n)$ 都在 $k$ 上可分，就定义 $E$ 在 $k$ 上是**可分的**。

**定理 4.4。** *设 $E$ 是 $k$ 的代数扩张，由一族元素 $\{\alpha_i\}_{i\in I}$ 生成。如果每个 $\alpha_i$ 都在 $k$ 上可分，那么 $E$ 在 $k$ 上可分。*

*证明。* $E$ 的每个元素都属于某个有限生成子域

$$
k(\alpha_{i_1},\ldots,\alpha_{i_n}),
$$

而如上所述，每个这样的子域都在 $k$ 上可分。因此由定理 4.3，$E$ 的每个元素都在 $k$ 上可分，证明完成。

**定理 4.5。** *可分扩张构成一个特选的扩张类。*

<span class="original-page-anchor" id="pdf-page-257" aria-hidden="true"></span>

*证明。* 假设 $E$ 在 $k$ 上可分，且 $E\supset F\supset k$。$E$ 的每个元素都在 $F$ 上可分，而 $F$ 的每个元素都是 $E$ 的元素，因此在 $k$ 上可分。所以域塔的每一步都可分。反过来，假设扩张 $E\supset F\supset k$ 满足 $E/F$ 可分且 $F/k$ 可分。如果 $E$ 在 $k$ 上是有限的，就可以使用推论 4.2。具体地，域塔的每一步的可分次数都等于扩张次数，由乘法性，$E$ 在 $k$ 上也有这两个次数相等。

如果 $E$ 是无限的，设 $\alpha\in E$。那么 $\alpha$ 是系数在 $F$ 中的一个可分多项式 $f(X)$ 的根。记这些系数为 $a_n,\ldots,a_0$。令 $F_0=k(a_n,\ldots,a_0)$。则 $F_0$ 在 $k$ 上可分，$\alpha$ 在 $F_0$ 上可分。现在考虑有限域塔

$$
k\subset F_0\subset F_0(\alpha),
$$

因此得出 $F_0(\alpha)$ 在 $k$ 上可分，从而 $\alpha$ 在 $k$ 上可分。这证明了“特选”的定义中的条件 (1)。

设 $E$ 在 $k$ 上可分。设 $F$ 是 $k$ 的任意扩张，并假设 $E,F$ 都是某个域的子域。$E$ 的每个元素都在 $k$ 上可分，从而在 $F$ 上可分。由于 $EF$ 由 $E$ 的所有元素在 $F$ 上生成，定理 4.4 表明 $EF$ 在 $F$ 上可分。这证明了“特选”的定义中的条件 (2)，也完成了定理的证明。

设 $E$ 是 $k$ 的有限扩张。所有包含 $E$ 的 $k$ 的正规扩张 $K$（位于代数闭包 $E^a$ 中）的交，是一个包含 $E$ 的 $k$ 的正规扩张，且显然是包含 $E$ 的最小的 $k$ 的正规扩张。如果 $\sigma_1,\ldots,\sigma_n$ 是从 $E$ 到 $E^a$ 的所有不同嵌入，那么扩张

$$
K=(\sigma_1E)(\sigma_2E)\cdots(\sigma_nE),
$$

也就是所有这些嵌入的像的合成域，是 $k$ 的正规扩张。因为对于它的任意嵌入，记为 $\tau$，可以将 $\tau$ 作用于每个扩张 $\sigma_iE$。那么 $(\tau\sigma_1,\ldots,\tau\sigma_n)$ 是 $(\sigma_1,\ldots,\sigma_n)$ 的一个置换，因此 $\tau$ 将 $K$ 映入自身。$k$ 的任意包含 $E$ 的正规扩张都必须对每个 $i$ 包含 $\sigma_iE$，所以*包含 $E$ 的最小的 $k$ 的正规扩张恰好等于合成域*

$$
(\sigma_1E)\cdots(\sigma_nE).
$$

如果 $E$ 在 $k$ 上可分，那么由定理 4.5 和归纳法得出，包含 $E$ 的最小的 $k$ 的正规扩张也在 $k$ 上可分。

通过取无限合成域，对于 $k$ 的无限代数扩张 $E$ 也有类似结果。

<span class="original-page-anchor" id="pdf-page-258" aria-hidden="true"></span>

根据定理 4.5，在给定的代数闭包 $k^a$ 中，域 $k$ 的所有可分扩张的合成域是可分扩张，记作 $k^s$ 或 $k^{\mathrm{sep}}$，称为 $k$ 的**可分闭包**。在术语方面，如果 $E$ 是 $k$ 的代数扩张，而 $\sigma$ 是 $E$ 在 $k$ 上到 $k^a$ 的任意嵌入，就称 $\sigma E$ 为 $E$ 在 $k^a$ 中的一个**共轭域**。可以说，*包含 $E$ 的最小的 $k$ 的正规扩张，就是 $E$ 在 $E^a$ 中的所有共轭域的合成域*。

设 $\alpha$ 在 $k$ 上是代数的。如果 $\sigma_1,\ldots,\sigma_r$ 是 $k(\alpha)$ 在 $k$ 上到 $k^a$ 的所有不同嵌入，就称 $\sigma_1\alpha,\ldots,\sigma_r\alpha$ 为 $\alpha$ 在 $k^a$ 中的**共轭元**。这些元素就是 $\alpha$ 在 $k$ 上的不可约多项式的所有不同根。包含这些共轭元中的任意一个的最小的 $k$ 的正规扩张，就是 $k(\sigma_1\alpha,\ldots,\sigma_r\alpha)$。

**定理 4.6（本原元定理）。** *设 $E$ 是域 $k$ 的有限扩张。存在元素 $\alpha\in E$ 使得 $E=k(\alpha)$，当且仅当满足 $k\subset F\subset E$ 的域 $F$ 只有有限多个。如果 $E$ 在 $k$ 上可分，则存在这样的元素 $\alpha$。*

*证明。* 如果 $k$ 是有限的，我们知道 $E$ 的乘法群由一个元素生成，因此这个元素也将在 $k$ 上生成 $E$。现在假设 $k$ 是无限的。

假设 $k$ 与 $E$ 之间只有有限多个中间域。设 $\alpha,\beta\in E$。当 $c$ 遍历 $k$ 的元素时，形如 $k(\alpha+c\beta)$ 的域只有有限多个。因此存在元素 $c_1,c_2\in k$，满足 $c_1\neq c_2$，使得

$$
k(\alpha+c_1\beta)=k(\alpha+c_2\beta).
$$

注意，$\alpha+c_1\beta$ 与 $\alpha+c_2\beta$ 属于同一个域，所以 $(c_1-c_2)\beta$ 也属于这个域，因而 $\beta$ 也属于这个域。于是 $\alpha$ 也在这个域中，可见 $k(\alpha,\beta)$ 可以由单个元素生成。

归纳地继续，如果 $E=k(\alpha_1,\ldots,\alpha_n)$，则存在元素 $c_2,\ldots,c_n\in k$，使得

$$
E=k(\xi),
$$

其中 $\xi=\alpha_1+c_2\alpha_2+\cdots+c_n\alpha_n$。这就证明了定理的一半。

反过来，假设对某个 $\alpha$ 有 $E=k(\alpha)$，令 $f(X)=\operatorname{Irr}(\alpha,k,X)$。设 $k\subset F\subset E$，令 $g_F(X)=\operatorname{Irr}(\alpha,F,X)$。那么 $g_F$ 整除 $f$。$E[X]$ 中有唯一分解，而 $E[X]$ 中任何首项系数为 $1$ 且整除 $f(X)$ 的多项式，都等于一些因子 $(X-\alpha_i)$ 的积，其中 $\alpha_1,\ldots,\alpha_n$ 是 $f$ 在一个固定代数闭包中的根。因此这样的多项式只有有限多个。于是得到从中间域的集合到一个有限多项式集合的映射

$$
F\mapsto g_F.
$$

设 $F_0$ 为<span class="original-page-anchor" id="pdf-page-259" aria-hidden="true"></span>$F$ 中由 $g_F(X)$ 的系数在 $k$ 上生成的子域。那么 $g_F$ 的系数属于 $F_0$，并且由于它在 $F$ 上不可约，所以在 $F_0$ 上也不可约。因此，$\alpha$ 在 $F_0$ 上的次数与它在 $F$ 上的次数相同。所以 $F=F_0$。于是域 $F$ 由其对应的多项式 $g_F$ 唯一确定，故这个映射是单射。这就证明了定理的第一个断言。

对于关于可分扩张的断言，使用归纳法，不失一般性可以假设 $E=k(\alpha,\beta)$，其中 $\alpha,\beta$ 在 $k$ 上可分。设 $\sigma_1,\ldots,\sigma_n$ 是 $k(\alpha,\beta)$ 在 $k$ 上到 $k^a$ 的所有不同嵌入。令

$$
P(X)=\prod_{i\neq j}(\sigma_i\alpha+X\sigma_i\beta-\sigma_j\alpha-X\sigma_j\beta).
$$

那么 $P(X)$ 不是零多项式，因此存在 $c\in k$，使得 $P(c)\neq0$。于是元素 $\sigma_i(\alpha+c\beta)$ $(i=1,\ldots,n)$ 两两不同，所以 $k(\alpha+c\beta)$ 在 $k$ 上的次数至少为 $n$。但 $n=[k(\alpha,\beta):k]$，因此

$$
k(\alpha,\beta)=k(\alpha+c\beta),
$$

正如所要求的。

如果 $E=k(\alpha)$，就称 $\alpha$ 为 $E$（在 $k$ 上）的一个**本原元**。

## §5. 有限域

我们已经建立了足够的一般定理，可以用来描述有限域的结构。这本身就是有趣的，也为一般理论提供了例子。

设 $F$ 是具有 $q$ 个元素的有限域。正如前面指出的，有一个同态

$$
\mathbf Z\to F,
$$

将 $1$ 映到 $1$，其核不可能为 $0$，因而是由某个素数 $p$ 生成的主理想，因为 $\mathbf Z/p\mathbf Z$ 嵌入到 $F$ 中，而 $F$ 没有零因子。因此，$F$ 的特征为 $p$，并且包含一个与 $\mathbf Z/p\mathbf Z$ 同构的域。

注意，$\mathbf Z/p\mathbf Z$ 除恒等映射外没有其他自同构。事实上，任何自同构都必须把 $1$ 映到 $1$，所以保持每个元素不变，因为 $1$ 在加法下生成 $\mathbf Z/p\mathbf Z$。我们将 $\mathbf Z/p\mathbf Z$ 与它在 $F$ 中的像等同。那么 $F$ 是 $\mathbf Z/p\mathbf Z$ 上的向量空间，而这个向量空间必然是<span class="original-page-anchor" id="pdf-page-260" aria-hidden="true"></span>有限的，因为 $F$ 是有限的。设它的次数为 $n$。设 $\omega_1,\ldots,\omega_n$ 是 $F$ 在 $\mathbf Z/p\mathbf Z$ 上的一组基。$F$ 的每个元素都有唯一的表示

$$
a_1\omega_1+\cdots+a_n\omega_n,
$$

其中 $a_i\in\mathbf Z/p\mathbf Z$。因此 $q=p^n$。

$F$ 的乘法群 $F^*$ 的阶为 $q-1$。每个 $\alpha\in F^*$ 都满足方程 $X^{q-1}=1$。因此 $F$ 的每个元素都满足方程

$$
f(X)=X^q-X=0.
$$

这意味着多项式 $f(X)$ 在 $F$ 中有 $q$ 个不同的根，即 $F$ 的所有元素。因此 $f$ 在 $F$ 中分裂为一次因子的乘积，即

$$
X^q-X=\prod_{\alpha\in F}(X-\alpha).
$$

特别地，$F$ 是 $f$ 的分裂域。但分裂域在同构意义下是唯一确定的。因此，如果阶为 $p^n$ 的有限域存在，那么它在同构意义下唯一确定，等于 $X^{p^n}-X$ 在 $\mathbf Z/p\mathbf Z$ 上的分裂域。

在记号方面，用 $\mathbf F_p$ 表示 $\mathbf Z/p\mathbf Z$。设 $n$ 是一个 $\geq1$ 的整数，考虑

$$
X^{p^n}-X=f(X)
$$

在代数闭包 $\mathbf F_p^a$ 中的分裂域。我们断言，这个分裂域就是 $f(X)$ 在 $\mathbf F_p^a$ 中的根的集合。事实上，设 $\alpha,\beta$ 是根。那么

$$
(\alpha+\beta)^{p^n}-(\alpha+\beta)=\alpha^{p^n}+\beta^{p^n}-\alpha-\beta=0,
$$

所以 $\alpha+\beta$ 是根。此外，

$$
(\alpha\beta)^{p^n}-\alpha\beta=\alpha^{p^n}\beta^{p^n}-\alpha\beta=\alpha\beta-\alpha\beta=0,
$$

所以 $\alpha\beta$ 是根。注意 $0,1$ 都是 $f(X)$ 的根。如果 $\beta\neq0$，则

$$
(\beta^{-1})^{p^n}-\beta^{-1}=(\beta^{p^n})^{-1}-\beta^{-1}=0,
$$

所以 $\beta^{-1}$ 是根。最后，

$$
(-\beta)^{p^n}-(-\beta)=(-1)^{p^n}\beta^{p^n}+\beta.
$$

如果 $p$ 是奇数，则 $(-1)^{p^n}=-1$，可见 $-\beta$ 是根。如果 $p$ 是偶数，则 $-1=1$（在 $\mathbf Z/2\mathbf Z$ 中），所以 $-\beta=\beta$ 是根。这就证明了断言。

$f(X)$ 的导数为

$$
f'(X)=p^nX^{p^n-1}-1=-1.
$$

所以 $f(X)$ 没有重根，因此在 $\mathbf F_p^a$ 中有 $p^n$ 个不同的根。于是它的分裂域恰有 $p^n$ 个元素。我们将结果归纳如下：

<span class="original-page-anchor" id="pdf-page-261" aria-hidden="true"></span>

**定理 5.1。** *对每个素数 $p$ 和每个整数 $n\geq1$，都存在一个阶为 $p^n$ 的有限域，记作 $\mathbf F_{p^n}$，它作为代数闭包 $\mathbf F_p^a$ 的子域是唯一确定的。它是多项式*

$$
X^{p^n}-X
$$

*的分裂域，而它的元素就是这个多项式的根。每个有限域都恰好同构于一个域 $\mathbf F_{p^n}$。*

我们通常写成 $p^n=q$，并用 $\mathbf F_q$ 代替 $\mathbf F_{p^n}$。

**推论 5.2。** *设 $\mathbf F_q$ 是有限域，$n$ 是一个 $\geq1$ 的整数。在给定的代数闭包 $\mathbf F_q^a$ 中，存在唯一的 $\mathbf F_q$ 的 $n$ 次扩张，这个扩张就是域 $\mathbf F_{q^n}$。*

*证明。* 设 $q=p^m$。那么 $q^n=p^{mn}$。$X^{q^n}-X$ 的分裂域恰是 $\mathbf F_{p^{mn}}$，它在 $\mathbf Z/p\mathbf Z$ 上的次数为 $mn$。由于 $\mathbf F_q$ 在 $\mathbf Z/p\mathbf Z$ 上的次数为 $m$，可知 $\mathbf F_{q^n}$ 在 $\mathbf F_q$ 上的次数为 $n$。反过来，$\mathbf F_q$ 的任意 $n$ 次扩张在 $\mathbf F_p$ 上的次数为 $mn$，所以必为 $\mathbf F_{p^{mn}}$。推论得证。

**定理 5.3。** *有限域的乘法群是循环群。*

*证明。* 这已经在第四章定理 1.9 中得到证明。

我们将确定有限域的所有自同构。

设 $q=p^n$，$\mathbf F_q$ 是具有 $q$ 个元素的有限域。考虑 **Frobenius 映射**

$$
\varphi:\mathbf F_q\to\mathbf F_q,
$$

满足 $\varphi(x)=x^p$。那么 $\varphi$ 是同态，而且由于 $\mathbf F_q$ 是域，其核为 $0$。因此 $\varphi$ 是单射。由于 $\mathbf F_q$ 有限，可知 $\varphi$ 是满射，因而是同构。注意它保持 $\mathbf F_p$ 不变。

**定理 5.4。** *$\mathbf F_q$ 的自同构群是阶为 $n$ 的循环群，由 $\varphi$ 生成。*

*证明。* 设 $G$ 是由 $\varphi$ 生成的群。注意 $\varphi^n=\operatorname{id}$，因为对于所有 $x\in\mathbf F_q$，都有 $\varphi^n(x)=x^{p^n}=x$。因此 $n$ 是 $\varphi$ 的一个指数。设 $d$ 是 $\varphi$ 的周期，则 $d\geq1$。对所有 $x\in\mathbf F_q$，都有 $\varphi^d(x)=x^{p^d}$。因此每个 $x\in\mathbf F_q$ 都是方程

$$
X^{p^d}-X=0
$$

的根。这个方程至多有 $p^d$ 个根。可知 $d\geq n$，从而 $d=n$。

还须证明 $G$ 是 $\mathbf F_q$ 的全部自同构所成的群。$\mathbf F_q$ 的任意自同构都必须保持 $\mathbf F_p$ 不变。因此它是一个<span class="original-page-anchor" id="pdf-page-262" aria-hidden="true"></span>在 $\mathbf F_p$ 上的 $\mathbf F_q$ 的自同构。由定理 4.1，这样的自同构的个数 $\leq n$。因此，$\mathbf F_q$ 除 $G$ 中的自同构外，不可能再有其他自同构。

**定理 5.5。** *设 $m,n$ 是 $\geq1$ 的整数。那么，在 $\mathbf F_p$ 的任意代数闭包中，子域 $\mathbf F_{p^n}$ 包含于 $\mathbf F_{p^m}$，当且仅当 $n$ 整除 $m$。在这种情形下，令 $q=p^n$，并令 $m=nd$。则 $\mathbf F_{p^m}$ 在 $\mathbf F_q$ 上正规且可分，而且 $\mathbf F_{p^m}$ 在 $\mathbf F_q$ 上的自同构群是阶为 $d$ 的循环群，由 $\varphi^n$ 生成。*

*证明。* 所有这些断言都是已证明结果的直接推论，留给读者验证。

## §6. 不可分扩张

本节的技术性相当强，可以略过，而不妨碍理解本书其余大部分内容。

先给出一些说明，补充命题 2.7 中的讨论。

设 $f(X)=(X-\alpha)^mg(X)$ 是 $k[X]$ 中的一个多项式，并假设 $X-\alpha$ 不整除 $g(X)$。回顾一下，$m$ 称为 $\alpha$ 在 $f$ 中的**重数**。如果 $m>1$，就称 $\alpha$ 是 $f$ 的一个**重根**。否则，称 $\alpha$ 是一个**单根**。

**命题 6.1。** *设 $\alpha$ 在 $k$ 上是代数的，$\alpha\in k^a$，令*

$$
f(X)=\operatorname{Irr}(\alpha,k,X).
$$

*如果 $\operatorname{char}k=0$，那么 $f$ 的所有根的重数都为 $1$（$f$ 是可分的）。如果*

$$
\operatorname{char}k=p>0,
$$

*那么存在整数 $\mu\geq0$，使得 $f$ 的每个根的重数都为 $p^\mu$。我们有*

$$
[k(\alpha):k]=p^\mu[k(\alpha):k]_s,
$$

*并且 $\alpha^{p^\mu}$ 在 $k$ 上可分。*

*证明。* 设 $\alpha_1,\ldots,\alpha_r$ 是 $f$ 在 $k^a$ 中的所有不同根，并令 $\alpha=\alpha_1$。设 $m$ 是 $\alpha$ 在 $f$ 中的重数。给定 $1\leq i\leq r$，存在 $k$ 上的同构

$$
\sigma:k(\alpha)\to k(\alpha_i),
$$

满足 $\sigma\alpha=\alpha_i$。将 $\sigma$ 延拓为 $k^a$ 的一个自同构，并且<span class="original-page-anchor" id="pdf-page-263" aria-hidden="true"></span>仍用 $\sigma$ 表示这个延拓。由于 $f$ 的系数属于 $k$，有 $f^\sigma=f$。注意，如果 $m_j$ 是 $\alpha_j$ 在 $f$ 中的重数，则

$$
f(X)=\prod_{j=1}^r(X-\sigma\alpha_j)^{m_j}.
$$

由唯一分解，得出 $m_i=m_1$，因此所有 $m_i$ 都等于同一个整数 $m$。

考虑导数 $f'(X)$。如果 $f$ 和 $f'$ 有公共根，那么 $\alpha$ 就是一个次数小于 $\deg f$ 的多项式的根。这是不可能的，除非 $\deg f'=-\infty$，换句话说，$f'$ 恒等于 $0$。如果特征为 $0$，这种情形不可能发生。因此，如果 $f$ 有重根，那么特征为 $p$，且对某个多项式 $g(X)\in k[X]$ 有 $f(X)=g(X^p)$。所以 $\alpha^p$ 是一个次数 $<\deg f$ 的多项式 $g$ 的根。归纳地继续，取最小的整数 $\mu\geq0$，使得 $\alpha^{p^\mu}$ 是 $k[X]$ 中一个可分多项式的根；这个多项式就是满足

$$
f(X)=h(X^{p^\mu})
$$

的多项式 $h$。比较 $f$ 与 $g$ 的次数，得出

$$
[k(\alpha):k(\alpha^p)]=p.
$$

归纳地，得到

$$
[k(\alpha):k(\alpha^{p^\mu})]=p^\mu.
$$

由于 $h$ 的根的重数为 $1$，知道

$$
[k(\alpha^{p^\mu}):k]_s=[k(\alpha^{p^\mu}):k],
$$

比较 $f$ 的次数与 $h$ 的次数，可见 $f$ 的不同根的个数等于 $h$ 的不同根的个数。因此

$$
[k(\alpha):k]_s=[k(\alpha^{p^\mu}):k]_s.
$$

由此，关于次数的公式由乘法性推出，命题得证。注意 $h$ 的根为

$$
\alpha_1^{p^\mu},\ldots,\alpha_r^{p^\mu}.
$$

**推论 6.2。** *对于 $k$ 的任意有限扩张 $E$，可分次数 $[E:k]_s$ 整除次数 $[E:k]$。如果特征为 $0$，则商为 $1$；如果特征为 $p>0$，则商是 $p$ 的一个幂。*

*证明。* 将 $E/k$ 分解成一个域塔，其中每一步都由单个元素生成，并应用命题 6.1 以及这些指数在域塔中的乘法性。

如果 $E/k$ 是有限的，我们将商〔译校注：原文此处印作 $E/K$；与随后关于基域 $k$ 的商式一致，这里应为 $E/k$。〕

<span class="original-page-anchor" id="pdf-page-264" aria-hidden="true"></span>

$$
\frac{[E:k]}{[E:k]_s}
$$

称为**不可分次数**（或**不可分度**），并如 §4 那样记作 $[E:k]_i$。我们有

$$
[E:k]_s[E:k]_i=[E:k].
$$

**推论 6.3。** *一个有限扩张是可分的，当且仅当 $[E:k]_i=1$。*

*证明。* 由定义即得。

**推论 6.4。** *如果 $E\supset F\supset k$ 是两个有限扩张，那么*

$$
[E:k]_i=[E:F]_i[F:k]_i.
$$

*证明。* 由定理 4.1 立即得到。

现在始终假设 $k$ 是特征为 $p>0$ 的域。

如果存在整数 $n\geq0$，使得 $\alpha^{p^n}$ 属于 $k$，就称在 $k$ 上代数的元素 $\alpha$ 在 $k$ 上是**纯不可分的**。

设 $E$ 是 $k$ 的代数扩张。我们断言，下列条件等价：

**P. Ins. 1。** $[E:k]_s=1$。

**P. Ins. 2。** $E$ 的每个元素 $\alpha$ 都在 $k$ 上纯不可分。

**P. Ins. 3。** 对每个 $\alpha\in E$，$\alpha$ 在 $k$ 上的不可约方程都具有 $X^{p^n}-a=0$ 的形式，其中 $n\geq0$，$a\in k$。

**P. Ins. 4。** $E$ 在 $k$ 上存在一个生成元集 $\{\alpha_i\}_{i\in I}$，其中每个 $\alpha_i$ 都在 $k$ 上纯不可分。

为了证明等价性，假设 P. Ins. 1 成立。设 $\alpha\in E$。由定理 4.1，得出 $[k(\alpha):k]_s=1$。令 $f(X)=\operatorname{Irr}(\alpha,k,X)$。那么 $f$ 只有一个根，因为

$$
[k(\alpha):k]_s
$$

等于 $f(X)$ 的不同根的个数。令 $m=[k(\alpha):k]$。则 $\deg f=m$，而 $f$ 在 $k(\alpha)$ 上的分解为 $f(X)=(X-\alpha)^m$。写成 $m=p^nr$，其中 $r$ 是与 $p$ 互素的整数。那么

$$
\begin{aligned}
f(X)&=(X^{p^n}-\alpha^{p^n})^r\\
&=X^{p^nr}-r\alpha^{p^n}X^{p^n(r-1)}+\text{较低次项}.
\end{aligned}
$$

由于 $f(X)$ 的系数属于 $k$，可知

$$
r\alpha^{p^n}
$$

<span class="original-page-anchor" id="pdf-page-265" aria-hidden="true"></span>

属于 $k$，又由于 $r\neq0$（在 $k$ 中），所以 $\alpha^{p^n}$ 属于 $k$。令 $a=\alpha^{p^n}$。那么 $\alpha$ 是多项式 $X^{p^n}-a$ 的根，而这个多项式整除 $f(X)$。所以 $f(X)=X^{p^n}-a$。

与前面基本相同的论证表明，P. Ins. 2 蕴含 P. Ins. 3。第三个条件蕴含第四个条件是显然的。

最后，假设 P. Ins. 4 成立。设 $E$ 是由纯不可分元素 $\alpha_i$ $(i\in I)$ 生成的扩张。$E$ 在 $k$ 上的任意嵌入都将 $\alpha_i$ 映到

$$
f_i(X)=\operatorname{Irr}(\alpha_i,k,X)
$$

的一个根。但 $f_i(X)$ 整除某个多项式 $X^{p^n}-a$，后者只有一个根。因此，$E$ 在 $k$ 上的任意嵌入在每个 $\alpha_i$ 上都是恒等映射，从而在 $E$ 上是恒等映射，所以得出 $[E:k]_s=1$，正如所要求的。

满足上述四个性质的扩张称为**纯不可分扩张**。

**命题 6.5。** *纯不可分扩张构成一个特选的扩张类。*

*证明。* 域塔定理由定理 4.1 显然得到，而提升性质由条件 P. Ins. 4 显然得到。

**命题 6.6。** *设 $E$ 是 $k$ 的代数扩张。令 $E_0$ 为 $E$ 中所有满足 $F\supset k$ 且在 $k$ 上可分的子域 $F$ 的合成域。那么 $E_0$ 在 $k$ 上可分，而 $E$ 在 $E_0$ 上纯不可分。*

*证明。* 由于可分扩张构成一个特选类，知道 $E_0$ 在 $k$ 上可分。事实上，$E_0$ 由 $E$ 中所有在 $k$ 上可分的元素组成。由命题 6.1，给定 $\alpha\in E$，存在 $p$ 的一个幂，记为 $p^n$，使得 $\alpha^{p^n}$ 在 $k$ 上可分。因此 $E$ 在 $E_0$ 上纯不可分，证毕。

**推论 6.7。** *如果 $k$ 的代数扩张 $E$ 既可分又纯不可分，那么 $E=k$。*

*证明。* 显然。

**推论 6.8。** *设 $K$ 在 $k$ 上正规，$K_0$ 是它的最大可分子扩张。那么 $K_0$ 在 $k$ 上也正规。*

*证明。* 设 $\sigma$ 是 $K_0$ 在 $k$ 上到 $K^a$ 的嵌入，将 $\sigma$ 延拓为 $K$ 的嵌入。那么 $\sigma$ 是 $K$ 的自同构。此外，$\sigma K_0$ 在 $k$ 上可分，因此包含于 $K_0$，因为 $K_0$ 是最大可分子域。所以 $\sigma K_0=K_0$，正如所断言的。

<span class="original-page-anchor" id="pdf-page-266" aria-hidden="true"></span>

**推论 6.9。** *设 $E,F$ 是 $k$ 的两个有限扩张，并假设 $E/k$ 可分，$F/k$ 纯不可分。假设 $E,F$ 是同一个域的子域。那么*

$$
[EF:F]=[E:k]=[EF:k]_s,
$$

$$
[EF:E]=[F:k]=[EF:k]_i.
$$

*证明。* 图如下：

![可分扩张与纯不可分扩张的合成域](/library/volume-86/diagrams/pdf-0266-separable-inseparable.png)

应用命题 6.1 的推论，对各个指数作简单的运算即可证明。我们将其留作练习。

**推论 6.10。** *用 $E^p$ 表示由所有元素 $x^p$（$x\in E$）组成的域。设 $E$ 是 $k$ 的有限扩张。如果 $E^pk=E$，那么 $E$ 在 $k$ 上可分。如果 $E$ 在 $k$ 上可分，那么对所有 $n\geq1$ 都有 $E^{p^n}k=E$。*

*证明。* 设 $E_0$ 是 $E$ 的最大可分子域。假设 $E^pk=E$。令 $E=k(\alpha_1,\ldots,\alpha_n)$。由于 $E$ 在 $E_0$ 上纯不可分，存在 $m$，使得对每个 $i=1,\ldots,n$ 都有 $\alpha_i^{p^m}\in E_0$。因此 $E^{p^m}\subset E_0$。但 $E^{p^m}k=E$，所以 $E=E_0$ 在 $k$ 上可分。反过来，假设 $E$ 在 $k$ 上可分。那么 $E$ 在 $E^pk$ 上可分。由于 $E$ 在 $E^pk$ 上也纯不可分，得出 $E=E^pk$。类似地，对于 $n\geq1$，得到 $E=E^{p^n}k$，证毕。

命题 6.6 表明，任何代数扩张都可以分解成一个由最大可分子扩张以及其上方的纯不可分一步组成的域塔。通常不能颠倒域塔的顺序。不过，有一种重要的情形可以这样做。

**命题 6.11。** *设 $K$ 在 $k$ 上正规。设 $G$ 是它在 $k$ 上的自同构群。设 $K^G$ 是 $G$ 的不动域（见第六章 §1）。那么 $K^G$ 在 $k$ 上纯不可分，而 $K$ 在 $K^G$ 上可分。如果 $K_0$ 是 $K$ 的最大可分子扩张，那么 $K=K^GK_0$，且 $K_0\cap K^G=k$。*

*证明。* 设 $\alpha\in K^G$。设 $\tau$ 是 $k(\alpha)$ 在 $k$ 上到 $K^a$ 的嵌入，将 $\tau$ 延拓为 $K$ 的嵌入，仍记作 $\tau$。那么 $\tau$ 是 $K$ 的自同构，因为 $K$ 在 $k$ 上正规。由定义，$\tau\alpha=\alpha$，所以 $\tau$ 在 $k(\alpha)$ 上是恒等映射。因此 $[k(\alpha):k]_s=1$，而 $\alpha$ 是纯不可分的。所以 $K^G$ 在 $k$ 上纯不可分。$K_0$<span class="original-page-anchor" id="pdf-page-267" aria-hidden="true"></span>与 $K^G$ 的交在 $k$ 上既可分又纯不可分，因此等于 $k$。

为了证明 $K$ 在 $K^G$ 上可分，先假设 $K$ 在 $k$ 上是有限的，因而由定理 4.1，$G$ 是有限的。设 $\alpha\in K$。设 $\sigma_1,\ldots,\sigma_r$ 是 $G$ 中元素的一个极大子集，使得元素

$$
\sigma_1\alpha,\ldots,\sigma_r\alpha
$$

两两不同，并且 $\sigma_1$ 是恒等映射；那么 $\alpha$ 是多项式

$$
f(X)=\prod_{i=1}^r(X-\sigma_i\alpha)
$$

的一个根。对任意 $\tau\in G$，有 $f^\tau=f$，因为 $\tau$ 置换这些根。注意 $f$ 是可分的，且它的系数在不动域 $K^G$ 中。因此 $\alpha$ 在 $K^G$ 上可分。将无限情形归约到有限情形，只须注意 $K$ 的每个元素 $\alpha$ 都包含于 $K$ 的某个有限正规子扩张中。细节留给读者。

现在有如下图形：

![正规扩张的分解](/library/volume-86/diagrams/pdf-0267-normal-decomposition.png)

由命题 6.6，$K$ 在 $K_0$ 上纯不可分，因此在 $K_0K^G$ 上纯不可分。此外，$K$ 在 $K^G$ 上可分，所以在 $K_0K^G$ 上可分。因此 $K=K_0K^G$，命题得证。

可见，每个正规扩张都分解为一个纯不可分扩张和一个可分扩张的合成域。下一章将把伽罗瓦扩张定义为正规可分扩张。那么 $K_0$ 在 $k$ 上是伽罗瓦扩张，而正规扩张被分解为一个伽罗瓦扩张和一个纯不可分扩张。群 $G$ 称为扩张 $K/k$ 的伽罗瓦群。

如果 $k^p=k$，就称域 $k$ 是**完美域**。（每个特征为零的域也都称为完美域。）

**推论 6.12。** *如果 $k$ 是完美域，那么 $k$ 的每个代数扩张都可分，而且 $k$ 的每个代数扩张都是完美域。*

*证明。* 每个有限代数扩张都包含于一个正规扩张中，应用命题 6.11 即可得到所需结论。

<span class="original-page-anchor" id="pdf-page-268" aria-hidden="true"></span>

## 习题

**1.** 设 $E=\mathbf Q(\alpha)$，其中 $\alpha$ 是方程

$$
\alpha^3+\alpha^2+\alpha+2=0
$$

的一个根。将 $(\alpha^2+\alpha+1)(\alpha^2+\alpha)$ 与 $(\alpha-1)^{-1}$ 表示为

$$
a\alpha^2+b\alpha+c
$$

的形式，其中 $a,b,c\in\mathbf Q$。

**2.** 设 $E=F(\alpha)$，其中 $\alpha$ 在 $F$ 上是奇数次的代数元。证明 $E=F(\alpha^2)$。

**3.** 设 $\alpha$ 与 $\beta$ 是两个在 $F$ 上代数的元素。令 $f(X)=\operatorname{Irr}(\alpha,F,X)$，$g(X)=\operatorname{Irr}(\beta,F,X)$。假设 $\deg f$ 与 $\deg g$ 互素。证明 $g$ 在多项式环 $F(\alpha)[X]$ 中不可约。

**4.** 设 $\alpha$ 是 $2$ 的正实四次方根。求 $\mathbf Q$ 的扩张 $\mathbf Q(\alpha)$ 的所有中间域。

**5.** 如果 $\alpha$ 是 $X^6+X^3+1$ 的一个复根，求所有同态 $\sigma:\mathbf Q(\alpha)\to\mathbf C$。［*提示：* 这个多项式是 $X^9-1$ 的一个因子。］

**6.** 证明 $\sqrt2+\sqrt3$ 在 $\mathbf Q$ 上是次数为 $4$ 的代数元。

**7.** 设 $E,F$ 是域 $k$ 的两个有限扩张，包含在更大的域 $K$ 中。证明

$$
[EF:k]\leq[E:k][F:k].
$$

如果 $[E:k]$ 与 $[F:k]$ 互素，证明上式中取等号。

**8.** 设 $f(X)\in k[X]$ 是次数为 $n$ 的多项式，$K$ 是它的分裂域。证明 $[K:k]$ 整除 $n!$。

**9.** 求 $X^{p^8}-1$ 在域 $\mathbf Z/p\mathbf Z$ 上的分裂域。

**10.** 设 $\alpha$ 是满足 $\alpha^4=5$ 的实数。

(a) 证明 $\mathbf Q(i\alpha^2)$ 在 $\mathbf Q$ 上正规。

(b) 证明 $\mathbf Q(\alpha+i\alpha)$ 在 $\mathbf Q(i\alpha^2)$ 上正规。

(c) 证明 $\mathbf Q(\alpha+i\alpha)$ 在 $\mathbf Q$ 上不正规。

**11.** 描述下列多项式在 $\mathbf Q$ 上的分裂域，并求每个分裂域的次数。

(a) $X^2-2$

(b) $X^2-1$

(c) $X^3-2$

(d) $(X^3-2)(X^2-2)$

(e) $X^2+X+1$

(f) $X^6+X^3+1$

(g) $X^5-7$

**12.** 设 $K$ 是具有 $p^n$ 个元素的有限域。证明 $K$ 的每个元素在 $K$ 中都有唯一的 $p$ 次方根。

<span class="original-page-anchor" id="pdf-page-269" aria-hidden="true"></span>

**13.** 如果首一多项式 $f(X)\in k[X]$ 在某个分裂域中的根两两不同，并且组成一个域，那么 $\operatorname{char}k=p$，而且对某个 $n\geq1$ 有 $f(X)=X^{p^n}-X$。

**14.** 设 $\operatorname{char}K=p$。设 $L$ 是 $K$ 的有限扩张，并假设 $[L:K]$ 与 $p$ 互素。证明 $L$ 在 $K$ 上可分。

**15.** 假设 $\operatorname{char}K=p$。设 $a\in K$。如果 $a$ 在 $K$ 中没有 $p$ 次方根，证明对所有正整数 $n$，$X^{p^n}-a$ 都在 $K[X]$ 中不可约。

**16.** 设 $\operatorname{char}K=p$。设 $\alpha$ 在 $K$ 上是代数的。证明 $\alpha$ 可分，当且仅当对所有正整数 $n$ 都有 $K(\alpha)=K(\alpha^{p^n})$。

**17.** 证明下列两个性质等价：

(a) $K$ 的每个代数扩张都可分。

(b) 或者 $\operatorname{char}K=0$，或者 $\operatorname{char}K=p$ 且 $K$ 的每个元素都在 $K$ 中有 $p$ 次方根。

**18.** 证明有限域的每个元素都可以写成该域中两个平方的和。

**19.** 设 $E$ 是 $F$ 的代数扩张。证明 $E$ 中每个包含 $F$ 的子环实际上都是一个域。如果 $E$ 在 $F$ 上不是代数的，这个结论是否必然成立？证明或给出反例。

**20.** (a) 设 $E=F(x)$，其中 $x$ 在 $F$ 上是超越的。设 $K\neq F$ 是 $E$ 中包含 $F$ 的子域。证明 $x$ 在 $K$ 上是代数的。

(b) 设 $E=F(x)$。设 $y=f(x)/g(x)$ 是一个有理函数，其中多项式 $f,g\in F[x]$ 互素。令 $n=\max(\deg f,\deg g)$。假设 $n\geq1$。证明

$$
[F(x):F(y)]=n.
$$

**21.** 设 $\mathbf Z^+$ 是正整数集，$A$ 是加法阿贝尔群。设 $f:\mathbf Z^+\to A$ 与 $g:\mathbf Z^+\to A$ 是映射。假设对所有 $n$ 都有

$$
f(n)=\sum_{d\mid n}g(d).
$$

设 $\mu$ 是 Möbius 函数（参见第二章习题 12）。证明

$$
g(n)=\sum_{d\mid n}\mu(n/d)f(d).
$$

**22.** 设 $k$ 是具有 $q$ 个元素的有限域。设 $f(X)\in k[X]$ 不可约。证明 $f(X)$ 整除 $X^{q^n}-X$，当且仅当 $\deg f$ 整除 $n$。证明乘积公式

$$
X^{q^n}-X=\prod_{d\mid n}\prod_{f_d\text{ 不可约}}f_d(X),
$$

其中内层乘积遍历所有次数为 $d$、首项系数为 $1$ 的不可约多项式。计算次数，证明

$$
q^n=\sum_{d\mid n}d\psi(d),
$$

其中 $\psi(d)$ 是次数为 $d$ 的不可约多项式的个数。应用

<span class="original-page-anchor" id="pdf-page-270" aria-hidden="true"></span>

习题 21 作反演，得到

$$
n\psi(n)=\sum_{d\mid n}\mu(d)q^{n/d}.
$$

**23.** (a) 设 $k$ 是具有 $q$ 个元素的有限域。定义 **zeta 函数**

$$
Z(t)=(1-t)^{-1}\prod_p(1-t^{\deg p})^{-1},
$$

其中 $p$ 遍历 $k[X]$ 中所有首项系数为 $1$ 的不可约多项式 $p=p(X)$。证明 $Z(t)$ 是一个有理函数，并确定这个有理函数。

(b) 设 $\pi_q(n)$ 是 (a) 中次数 $\leq n$ 的素多项式 $p$ 的个数。证明

$$
\pi_q(m)\sim\frac{q}{q-1}\frac{q^m}{m}\qquad\text{当 }m\to\infty.
$$

**说明。** 这是数论中素数定理的类似物，但在当前情形下基本是平凡的，因为黎曼猜想在这里可以直接验证。在这种情形之后，情况很快就会变得更有趣。考虑有限域 $\mathbf F_q$ 上的方程 $y^2=x^3+ax+b$，其中域的特征 $\neq2,3$，并具有 $q$ 个元素。假设 $-4a^3-27b^2\neq0$，此时这个方程定义的曲线称为**椭圆曲线**。由下式定义 $N_n$：

$$
\begin{aligned}
N_n-1={}&\text{满足上述方程的点 }(x,y)\text{ 的个数，其中}\\
&x,y\in\mathbf F_{q^n}\quad\text{（}\mathbf F_q\text{ 的 }n\text{ 次扩张）}.
\end{aligned}
$$

将 zeta 函数 $Z(t)$ 定义为满足 $Z(0)=1$ 且

$$
Z'(t)/Z(t)=\sum N_nt^{n-1}
$$

的唯一有理函数。

Hasse 的一个著名定理断言，$Z(t)$ 是形如

$$
Z(t)=\frac{(1-\alpha t)(1-\bar\alpha t)}{(1-t)(1-qt)}
$$

的有理函数，其中 $\alpha$ 是一个虚二次数（非实数，且在 $\mathbf Q$ 上为二次），$\bar\alpha$ 是它的复共轭，并且 $\alpha\bar\alpha=q$，所以 $|\alpha|=q^{1/2}$。参见 Hasse，“Abstrakte Bergrundung der komplexen Multiplikation und Riemannsche Vermutung in Funktionenkörpern”，*Abh. Math. Sem. Univ. Hamburg* **10** (1934)，第 325–348 页。

〔译校注：原文称 $\alpha$ 为“非实数，且在 $\mathbf Q$ 上为二次”的数，此处须允许重根的例外。当 $q$ 为平方且达到 Hasse 界时，可能有 $\alpha=\bar\alpha=\pm\sqrt q$，此时 $\alpha$ 是实数。例如曲线 $y^2=x^3+1$ 在 $\mathbf F_{25}$ 上有 $36$ 个点（包括无穷远点），相应的 $\alpha=\bar\alpha=-5$；分子为 $(1+5t)^2$。原文的有理函数形式及 $|\alpha|=\sqrt q$ 仍成立。〕

**24.** 设 $k$ 是特征为 $p$ 的域，$t,u$ 在 $k$ 上代数无关。证明：

(a) $k(t,u)$ 在 $k(t^p,u^p)$ 上的次数为 $p^2$。

(b) 在 $k(t,u)$ 与 $k(t^p,u^p)$ 之间存在无限多个扩张。

**25.** 设 $E$ 是 $k$ 的有限扩张，令 $p^r=[E:k]_i$。假设特征为 $p>0$。假设不存在满足 $s<r$ 的指数 $p^s$，使得 $E^{p^s}k$ 在 $k$ 上可分（即使得对 $E$ 中每个 $\alpha$，$\alpha^{p^s}$ 都在 $k$ 上可分）。证明 $E$ 可以由单个元素在 $k$ 上生成。［*提示：* 先假设 $E$ 是纯不可分扩张。］

<span class="original-page-anchor" id="pdf-page-271" aria-hidden="true"></span>

**26.** 设 $k$ 是一个域，$f(X)$ 是 $k[X]$ 中的不可约多项式，$K$ 是 $k$ 的有限正规扩张。如果 $g,h$ 是 $f(X)$ 在 $K[X]$ 中的首一不可约因子，证明存在 $K$ 在 $k$ 上的自同构 $\sigma$，使得 $g=h^\sigma$。给出一个例子，说明若 $K$ 在 $k$ 上不正规，则这个结论可能不成立。

**27.** 设 $x_1,\ldots,x_n$ 在域 $k$ 上代数无关。设 $y$ 在 $k(x)=k(x_1,\ldots,x_n)$ 上是代数的。设 $P(X_{n+1})$ 是 $y$ 在 $k(x)$ 上的不可约多项式。设 $\varphi(x)$ 是 $P$ 的各系数的分母的最小公倍式。那么 $\varphi(x)P$ 的系数是 $k[x]$ 中的元素。证明，多项式

$$
f(X_1,\ldots,X_{n+1})=\varphi(X_1,\ldots,X_n)P(X_{n+1})
$$

作为 $n+1$ 元多项式在 $k$ 上不可约。

反过来，设 $f(X_1,\ldots,X_{n+1})$ 是 $k$ 上的不可约多项式。设 $x_1,\ldots,x_n$ 在 $k$ 上代数无关。证明

$$
f(x_1,\ldots,x_n,X_{n+1})
$$

在 $k(x_1,\ldots,x_n)$ 上不可约。

如果 $f$ 是一个 $n$ 元多项式，而 $(b)=(b_1,\ldots,b_n)$ 是满足 $f(b)=0$ 的元素的一个 $n$ 元组，就称 $(b)$ 是 $f$ 的一个**零点**。如果坐标 $b_i$ 并非全都等于 $0$，就称 $(b)$ 是**非平凡的**。

**28.** 设 $f(X_1,\ldots,X_n)$ 是域 $k$ 上次数为 $2$（相应地，$3$）的齐次多项式。证明，如果 $f$ 在 $k$ 的一个奇数次扩张（相应地，$2$ 次扩张）中有非平凡零点，那么 $f$ 在 $k$ 中有非平凡零点。

**29.** 设 $f(X,Y)$ 是域 $k$ 上的二元不可约多项式。设 $t$ 在 $k$ 上超越，并假设存在整数 $m,n\neq0$ 以及元素 $a,b\in k$，$ab\neq0$，使得 $f(at^n,bt^m)=0$。证明，在必要时将 $X$ 或 $Y$ 取逆后，且相差一个常数因子的意义下，$f$ 具有

$$
X^mY^n-c
$$

的形式，其中 $c\in k$。

下面这道习题的答案尚未知。

**30（Artin 猜想）。** 设 $f$ 是具有有理系数的 $n$ 元 $d$ 次齐次多项式。如果 $n>d$，证明存在一个单位根 $\zeta$ 以及不全为 $0$ 的元素

$$
x_1,\ldots,x_n\in\mathbf Q[\zeta],
$$

使得 $f(x_1,\ldots,x_n)=0$。

**31. 差分方程。** 设 $u_1,\ldots,u_d$ 是域 $K$ 中的元素。我们要解出满足

$$
(*)\qquad x_n=u_1x_{n-1}+\cdots+u_dx_{n-d}\qquad\text{对 }n\geq d
$$

的无穷向量 $(x_0,x_1,\ldots,x_n,\ldots)$。

将该系统的**特征多项式**定义为

$$
X^d-(u_1X^{d-1}+\cdots+u_d)=f(X).
$$

<span class="original-page-anchor" id="pdf-page-272" aria-hidden="true"></span>

假设 $\alpha$ 是 $f$ 的一个根。

(a) 证明 $x_n=\alpha^n$ $(n\geq0)$ 是 $(*)$ 的一个解。

(b) 证明 $(*)$ 的解的集合是一个维数为 $d$ 的向量空间。

(c) 假设特征多项式有 $d$ 个不同根 $\alpha_1,\ldots,\alpha_d$。证明解 $(\alpha_1^n),\ldots,(\alpha_d^n)$ 构成解空间的一组基。

(d) 设 $x_n=b_1\alpha_1^n+\cdots+b_d\alpha_d^n$，$n\geq0$。说明如何用 $\alpha_1,\ldots,\alpha_d$ 以及 $x_0,\ldots,x_{d-1}$ 解出 $b_1,\ldots,b_d$。（使用 Vandermonde 行列式。）

(e) 在 (d) 的条件下，令 $F(T)=\sum x_nT^n$。证明 $F(T)$ 表示一个有理函数，并给出它的部分分式分解。

**32.** 为简便起见，令 $d=2$。给定 $a_0,a_1,u,v,w,t\in K$，我们要求系统

$$
a_n=ua_{n-1}-va_{n-2}-t^nw\qquad\text{对 }n\geq2
$$

的解。设 $\alpha_1,\alpha_2$ 是特征多项式的根，即

$$
1-uX+vX^2=(1-\alpha_1X)(1-\alpha_2X).
$$

*假设 $\alpha_1,\alpha_2$ 互不相同，并且都不等于 $t$。令*

$$
F(X)=\sum_{n=0}^\infty a_nX^n.
$$

(a) 证明存在 $K$ 中的元素 $A,B,C$，使得

$$
F(X)=\frac A{1-\alpha_1X}+\frac B{1-\alpha_2X}+\frac C{1-tX}.
$$

(b) 证明差分方程有唯一的解，由下式给出：

$$
a_n=A\alpha_1^n+B\alpha_2^n+Ct^n\qquad\text{对 }n\geq0.
$$

（关于这一形式在模形式中的应用，如 Manin、Mazur 和 Swinnerton-Dyer 的工作，参见我的 *Introduction to Modular Forms*，Springer-Verlag，New York，1976，第十二章 §2。）

**33.** 设 $R$ 是一个环，为简单起见，假设它是整环。设

$$
g(T)=T^d-a_{d-1}T^{d-1}-\cdots-a_0
$$

是 $R[T]$ 中的一个多项式，考虑方程

$$
T^d=a_0+a_1T+\cdots+a_{d-1}T^{d-1}.
$$

设 $x$ 是 $g(T)$ 的一个根。

(a) 对任意整数 $n\geq d$，存在关系式

$$
x^n=a_{0,n}+a_{1,n}x+\cdots+a_{d-1,n}x^{d-1},
$$

其中系数 $a_{i,j}$ 属于 $\mathbf Z[a_0,\ldots,a_{d-1}]\subset R$。

(b) 设 $F(T)\in R[T]$ 是一个多项式。那么

$$
F(x)=a_0(F)+a_1(F)x+\cdots+a_{d-1}(F)x^{d-1},
$$

其中系数 $a_i(F)$ 属于 $R$，并且线性地依赖于 $F$。

<span class="original-page-anchor" id="pdf-page-273" aria-hidden="true"></span>

(c) 设 Vandermonde 行列式为

$$
V(x_1,\ldots,x_d)=\begin{vmatrix}
1&x_1&\cdots&x_1^{d-1}\\
1&x_2&\cdots&x_2^{d-1}\\
\vdots&\vdots&&\vdots\\
1&x_d&\cdots&x_d^{d-1}
\end{vmatrix}=\prod_{i<j}(x_j-x_i).
$$

假设方程 $g(T)=0$ 有 $d$ 个根，且有分解

$$
g(T)=\prod_{i=1}^d(T-x_i).
$$

将 $x_i$ 代入 $x$，其中 $i=1,\ldots,d$，并对所得的线性方程组使用 Cramer 法则，得到

$$
\Delta a_j(F)=\Delta_j(F),
$$

其中 $\Delta$ 是 Vandermonde 行列式，而 $\Delta_j(F)$ 是将第 $j$ 列替换为 ${}^t(F(x_1),\ldots,F(x_d))$ 后得到的行列式，所以

$$
\Delta_j(F)=\begin{vmatrix}
1&x_1&\cdots&F(x_1)&\cdots&x_1^{d-1}\\
1&x_2&\cdots&F(x_2)&\cdots&x_2^{d-1}\\
\vdots&\vdots&&\vdots&&\vdots\\
1&x_d&\cdots&F(x_d)&\cdots&x_d^{d-1}
\end{vmatrix}.
$$

如果 $\Delta\neq0$，就可以写成

$$
a_j(F)=\Delta_j(F)/\Delta.
$$

**说明。** 如果 $F(T)$ 是 $R[[T]]$ 中的幂级数，且 $R$ 是一个完备局部环，$x_1,\ldots,x_d$ 属于极大理想，并且对某个 $i$ 有 $x=x_i$，那么由于级数收敛，可以计算 $F(x)$。上述关于系数 $a_j(F)$ 的公式仍然有效。

**34.** 设 $x_1,\ldots,x_d$ 是独立变元，设 $A$ 是环

$$
\mathbf Q[[x_1,\ldots,x_d]][T]/\prod_{i=1}^d(T-x_i).
$$

以某个 $x_i$ 代入 $T$，诱导从 $A$ 到

$$
\mathbf Q[[x_1,\ldots,x_d]]=R
$$

上的自然同态 $\varphi_i$。〔译校注：原文此式印作 $\mathbf Q[[z_1,\ldots,x_d]]=R$；本题的变元为 $x_1,\ldots,x_d$，因此首个变元应为 $x_1$。〕而映射 $z\mapsto(\varphi_1(z),\ldots,\varphi_d(z))$ 给出 $A$ 到 $R$ 与自身的 $d$ 重积中的嵌入。

设 $k$ 是一个整数，考虑形式幂级数

$$
F(T)=e^{kT}\prod_{i=1}^d\frac{(T-x_i)e^{T-x_i}}{e^{T-x_i}-1}=e^{kT}\prod_{i=1}^d h(T-x_i),
$$

其中 $h(t)=te^t/(e^t-1)$。这是关于 $T,T-x_1,\ldots,T-x_d$ 的形式幂级数。以某个 $x_j$ 代入 $T$ 后，它成为关于 $x_j$ 与 $x_j-x_i$ 的幂级数，因而在 $\mathbf Q[[x_1,\ldots,x_d]]$ 中收敛。

<span class="original-page-anchor" id="pdf-page-274" aria-hidden="true"></span>

(a) 验证

$$
F(T)\equiv a_0(F)+\cdots+a_{d-1}(F)T^{d-1}\mod\prod_{i=1}^d(T-x_i),
$$

其中 $a_0(F),\ldots,a_{d-1}(F)\in\mathbf Q[[x_1,\ldots,x_d]]$，并且前一道习题给出的用 Vandermonde 行列式表示这些系数的公式仍然有效。

(b) 证明当 $-(d-1)\leq k<0$ 时，$a_{d-1}(F)=0$；而当 $k=0$ 时，$a_{d-1}(F)=1$。

**说明。** (a) 中的断言是一个简单的极限。(b) 中的断言是一个曾用于 Hirzebruch–Grothendieck–Riemann–Roch 定理证明中的事实；据我所知，直到 Roger Howe 指出可以如下使用前一道习题的公式来证明它之前，还没有简单的已知证明。我们有

$$
V(x_1,\ldots,x_d)a_{d-1}(F)=\begin{vmatrix}
1&x_1&\cdots&x_1^{d-2}&F(x_1)\\
\vdots&\vdots&&\vdots&\vdots\\
1&x_d&\cdots&x_d^{d-2}&F(x_d)
\end{vmatrix}.
$$

〔译校注：原文等式左边印作 $V(x_1,\ldots,x_n)a_{d-1}(F)$；右边的行列式有 $d$ 行，且本题共有 $d$ 个变元，所以这里应为 $V(x_1,\ldots,x_d)a_{d-1}(F)$。〕

此外，

$$
F(x_j)=e^{kx_j}\prod_{n\neq j}\frac{(x_j-x_n)e^{x_j-x_n}}{e^{x_j-x_n}-1}.
$$

使用 Vandermonde 行列式的归纳关系

$$
V(x_1,\ldots,x_d)=V(x_1,\ldots,\hat x_j,\ldots,x_d)(-1)^{d-j}\prod_{n\neq j}(x_j-x_n).
$$

将 $a_{d-1}(F)$ 的行列式按最后一列展开，得到

$$
a_{d-1}(F)=\sum_{j=1}^d e^{(k+d-1)x_j}\prod_{n\neq j}\frac1{e^{x_j}-e^{x_n}}.
$$

反向使用归纳关系，并将 $x_i$ 换成 $e^{x_i}$；为排版方便，记后者为 $y_i$。得到

$$
V(y_1,\ldots,y_d)a_{d-1}(F)=\begin{vmatrix}
1&y_1&\cdots&y_1^{d-2}&y_1^{k+d-1}\\
\vdots&\vdots&&\vdots&\vdots\\
1&y_d&\cdots&y_d^{d-2}&y_d^{k+d-1}
\end{vmatrix}.
$$

如果 $k\neq0$，则右边有两列相同，因此行列式为 $0$。如果 $k=0$，则右边就是 Vandermonde 行列式，所以 $a_{d-1}(F)=1$。这证明了所需的取值。
