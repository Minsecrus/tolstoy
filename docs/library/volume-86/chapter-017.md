---
title: "第十七章 半单性"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第十六章 张量积","link":"/library/volume-86/chapter-016"}
next: {"text":"第十八章 有限群的表示","link":"/library/volume-86/chapter-018"}
---

# 第十七章 半单性

<span class="original-page-anchor" id="pdf-page-650" aria-hidden="true"></span>

在许多应用中，一个模可以分解为单子模的直和；于是，无论在一般假设下还是在具体应用中，都能发展出相当精确的结构理论。本章讨论那些可以在一般情况下证明的结果。下一章则考虑在一个经典而重要的特殊情形中能够进一步证明的结果。

在雅各布森稠密性定理的证明中，我大体上遵循了 Bourbaki 的做法。

## §1. 非交换环上的矩阵与线性映射

在第十三章，我们只讨论了交换环上的矩阵。为了当前的目的，需要考虑更一般的情形。

设 $K$ 是一个环。像交换环的情形一样，定义系数在 $K$ 中的矩阵 $(\varphi_{ij})$。矩阵的乘积由同一个公式定义。只要运算中各矩阵的大小使运算有定义，我们仍有结合律和分配律。特别地，$K$ 上的 $n\times n$ 方阵组成一个环，仍记为 $\operatorname{Mat}_n(K)$。沿对角线有一个环同态

$$
K\to\operatorname{Mat}_n(K).
$$

<span class="original-page-anchor" id="pdf-page-651" aria-hidden="true"></span>

所谓**除环**，是指满足 $1\ne0$、且每个非零元素都有乘法逆元的环。

若 $K$ 是除环，则每个非零 $K$-模都有基，且任意两组基的基数相同。证明与交换的情形一样；这些论证从来不需要交换性。这个基数仍称为模在 $K$ 上的**维数**，除环上的模称为**向量空间**。

像交换的情形一样，可以根据有限基的选择，将矩阵与线性映射联系起来。不过，我们将考虑一个略有不同的情形，以便应用于半单模。

设 $R$ 为环，设

$$
E=E_1\oplus\cdots\oplus E_n,\qquad F=F_1\oplus\cdots\oplus F_m
$$

为表示成 $R$-子模直和的 $R$-模。我们希望描述从 $E$ 到 $F$ 的最一般的 $R$-同态。

首先假设 $F=F_1$ 只有一个分量。设

$$
\varphi:E_1\oplus\cdots\oplus E_n\to F
$$

为同态。令 $\varphi_j:E_j\to F$ 为 $\varphi$ 在因子 $E_j$ 上的限制。每个元素 $x\in E$ 都有唯一表示 $x=x_1+\cdots+x_n$，其中 $x_j\in E_j$。因此可以将 $x$ 与列向量 $X={}^t(x_1,\ldots,x_n)$ 联系起来，其各分量分别在 $E_1,\ldots,E_n$ 中。可以将 $\varphi$ 与行向量 $(\varphi_1,\ldots,\varphi_n)$ 联系起来，其中 $\varphi_j\in\operatorname{Hom}_R(E_j,F)$；$\varphi$ 对 $E$ 中元素 $x$ 的作用，由行向量乘以列向量的矩阵乘法描述。

更一般地，考虑同态

$$
\varphi:E_1\oplus\cdots\oplus E_n\to F_1\oplus\cdots\oplus F_m.
$$

令 $\pi_i:F_1\oplus\cdots\oplus F_m\to F_i$ 为到第 $i$ 个因子的投影。于是，对每个 $i$，都可以将前面的说明应用于 $\pi_i\circ\varphi$。这样便看出，存在唯一的元素 $\varphi_{ij}\in\operatorname{Hom}_R(E_j,F_i)$，使得 $\varphi$ 有矩阵表示

$$
M(\varphi)=\begin{pmatrix}\varphi_{11}&\cdots&\varphi_{1n}\\\vdots&&\vdots\\\varphi_{m1}&\cdots&\varphi_{mn}\end{pmatrix},
$$

它对元素 $x$ 的作用由矩阵乘法给出，即

$$
\begin{pmatrix}\varphi_{11}&\cdots&\varphi_{1n}\\\vdots&&\vdots\\\varphi_{m1}&\cdots&\varphi_{mn}\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}.
$$

<span class="original-page-anchor" id="pdf-page-652" aria-hidden="true"></span>

反过来，给定矩阵 $(\varphi_{ij})$，其中 $\varphi_{ij}\in\operatorname{Hom}_R(E_j,F_i)$，就可以通过这个矩阵定义 $\operatorname{Hom}_R(E,F)$ 中的一个元素。$\operatorname{Hom}_R(E,F)$ 与这个矩阵群之间存在一个加法群同构。

*特别地，设 $E$ 是一个固定的 $R$-模，令 $K=\operatorname{End}_R(E)$。则存在环同构*

$$
\operatorname{End}_R(E^{(n)})\to\operatorname{Mat}_n(K),
$$

*它将每个 $\varphi\in\operatorname{End}_R(E^{(n)})$ 对应于像前面那样确定的矩阵*

$$
\begin{pmatrix}\varphi_{11}&\cdots&\varphi_{1n}\\\vdots&&\vdots\\\varphi_{n1}&\cdots&\varphi_{nn}\end{pmatrix},
$$

*并从左侧作用于分量在 $E$ 中的 $E^{(n)}$ 的列向量。*

**说明。** 设 $E$ 是除环 $D$ 上的一维向量空间，$\{v\}$ 为一组基。对每个 $a\in D$，存在唯一的 $D$-线性映射 $f_a:E\to E$，使 $f_a(v)=av$。于是有法则

$$
f_af_b=f_{ba}.
$$

因此，依赖于一组基将矩阵与线性映射联系起来时，乘法会发生扭转。不过，我们刚才在此说明之前作出的陈述确实正确！！关键在于，在 $R=D$ 这个特殊情形中，我们所取的 $\varphi_{ij}$ 在 $\operatorname{End}_R(E)$ 中，而不是在 $D$ 中。因此，$K$ 与 $D$（在非交换情形中）不是同构，而是反同构。这是交换与非交换情形下线性映射的形式初等理论之间唯一的差别。

回顾一下：若 $R$-模 $E$ 非零，且除了 $0$ 和 $E$ 之外没有其他子模，则称 $E$ 是**单的**。

**命题 1.1（舒尔引理）。** *设 $E,F$ 是单 $R$-模。$E$ 到 $F$ 中的每个非零同态都是同构。环 $\operatorname{End}_R(E)$ 是除环。*

*证明。* 设 $f:E\to F$ 为非零同态。它的像与核都是子模，因此 $\operatorname{Ker}f=0$ 且 $\operatorname{Im}f=F$。所以 $f$ 为同构。若 $E=F$，则 $f$ 有逆映射，正如所需。

下一个命题完整描述了单模直和的自同态环。

**命题 1.2。** *设 $E=E_1^{(n_1)}\oplus\cdots\oplus E_r^{(n_r)}$ 为单模的直和，各 $E_i$ 互不同构，且每个 $E_i$ 以重复 $n_i$ 次的方式出现于该* <span class="original-page-anchor" id="pdf-page-653" aria-hidden="true"></span>*直和中。则在允许置换次序及同构的意义下，$E_1,\ldots,E_r$ 唯一确定，而重数 $n_1,\ldots,n_r$ 唯一确定。环 $\operatorname{End}_R(E)$ 同构于形如下式的矩阵环：*

![分块对角自同态矩阵](/library/volume-86/diagrams/pdf-0653-block-endomorphisms.png)

*其中 $M_i$ 是 $\operatorname{End}_R(E_i)$ 上的 $n_i\times n_i$ 矩阵。（这个同构就是相对于所给直和分解的同构。）*

*证明。* 最后一个陈述由前面的讨论结合命题 1.1 得出。

现在假设有两个 $R$-模，分别分解为单子模的直和，并有同构

$$
E_1^{(n_1)}\oplus\cdots\oplus E_r^{(n_r)}\to F_1^{(m_1)}\oplus\cdots\oplus F_s^{(m_s)},
$$

其中各 $E_i$ 互不同构，各 $F_j$ 也互不同构。由命题 1.1 可知，每个 $E_i$ 都同构于某个 $F_j$，反之亦然。所以 $r=s$，且经过一次置换后有 $E_i\approx F_i$。此外，这个同构对每个 $i$ 必须诱导同构

$$
E_i^{(n_i)}\to F_i^{(m_i)}.
$$

因为 $E_i\approx F_i$，可以不失一般性地假设实际上 $E_i=F_i$。这样便归约为证明：若一个模同时同构于某个单模 $E$ 的 $E^{(n)}$ 和 $E^{(m)}$，则 $n=m$。但是，$\operatorname{End}_R(E^{(n)})$ 同构于除环 $\operatorname{End}_R(E)=K$ 上的 $n\times n$ 矩阵环。而且立即可验证，这个同构也是 $K$-向量空间的同构。$K$ 上的 $n\times n$ 矩阵空间的维数为 $n^2$。这证明了重数 $n$ 唯一确定，从而证明了命题。

当 $E$ 具有单子模的（有限）直和分解时，一个给定同构类中的单模在分解中出现的次数，称为这个单模（或这个单模同构类）的**重数**。

此外，若

$$
E=E_1^{(n_1)}\oplus\cdots\oplus E_r^{(n_r)}
$$

表示为单子模的和，则称 $n_1+\cdots+n_r$ 为 $E$ 的**长度**。在许多应用中，我们也写成

$$
E=n_1E_1\oplus\cdots\oplus n_rE_r=\bigoplus_{i=1}^r n_iE_i.
$$

<span class="original-page-anchor" id="pdf-page-654" aria-hidden="true"></span>

## §2. 定义半单性的条件

*设 $R$ 为环。除非另有说明，本节中的所有模与同态均指 $R$-模与 $R$-同态。*

模 $E$ 的下述条件等价：

**SS 1。** $E$ 是一族单子模的和。

**SS 2。** $E$ 是一族单子模的直和。

**SS 3。** $E$ 的每个子模 $F$ 都是直和项，即存在子模 $F'$，使得 $E=F\oplus F'$。

现在证明这三个条件等价。

**引理 2.1。** *设 $E=\sum_{i\in I}E_i$ 为单子模的和（未必是直和）。则存在子集 $J\subset I$，使得 $E$ 是直和 $\bigoplus_{j\in J}E_j$。*

*证明。* 令 $J$ 为 $I$ 的极大子集，使和 $\sum_{j\in J}E_j$ 为直和。我们断言，这个和实际上等于 $E$。只需证明每个 $E_i$ 都包含于这个和中。但这个和与 $E_i$ 的交是 $E_i$ 的子模，因此等于 $0$ 或 $E_i$。若等于 $0$，则可以将 $i$ 添入 $J$，所以 $J$ 不是极大的。因此 $E_i$ 包含于这个和，引理得证。

这个引理表明 **SS 1** 蕴含 **SS 2**。为了证明 **SS 2** 蕴含 **SS 3**，取一个子模 $F$，并令 $J$ 为 $I$ 的极大子集，使得和 $F+\bigoplus_{j\in J}E_j$ 为直和。与前面相同的推理表明，这个和等于 $E$。

最后假设 **SS 3** 成立。为了证明 **SS 1**，先证明 $E$ 的每个非零子模都包含一个单子模。取 $v\in E$、$v\ne0$。按定义，$Rv$ 是主子模，同态

$$
R\to Rv
$$

的核是左理想 $L\ne R$。由佐恩引理，$L$ 包含于一个极大左理想 $M\ne R$。于是，$M/L$ 是 $R/L$ 的极大子模（不等于 $R/L$），从而 $Mv$ 是 $Rv$ 的极大子模，不等于 $Rv$；它在同构

$$
R/L\to Rv
$$

下对应于 $M/L$。

<span class="original-page-anchor" id="pdf-page-655" aria-hidden="true"></span>

对于某个子模 $M'$，可以写成 $E=Mv\oplus M'$。于是

$$
Rv=Mv\oplus(M'\cap Rv),
$$

因为每个元素 $x\in Rv$ 都可以唯一写成和 $x=\alpha v+x'$，其中 $\alpha\in M$、$x'\in M'$，而 $x'=x-\alpha v$ 属于 $Rv$。由于 $Mv$ 在 $Rv$ 中极大，可知 $M'\cap Rv$ 是单的，正如所需。

令 $E_0$ 为 $E$ 中所有单子模之和所构成的子模。若 $E_0\ne E$，则有 $E=E_0\oplus F$，其中 $F\ne0$，且 $F$ 中存在一个单子模，这与 $E_0$ 的定义矛盾。因此 **SS 3** 蕴含 **SS 1**。

满足上述三个条件的模 $E$ 称为**半单模**。

**命题 2.2。** *半单模的每个子模与每个商模都是半单的。*

*证明。* 设 $F$ 为子模。令 $F_0$ 为 $F$ 的所有单子模的和。写成 $E=F_0\oplus F'_0$。$F$ 的每个元素 $x$ 都有唯一表示 $x=x_0+x'_0$，其中 $x_0\in F_0$、$x'_0\in F'_0$。但 $x'_0=x-x_0\in F$。所以 $F$ 为直和

$$
F=F_0\oplus(F\cap F'_0).
$$

因此必须有 $F_0=F$，它是半单的。对于商模，写成 $E=F\oplus F'$。于是 $F'$ 是其单子模的和，典范映射 $E\to E/F$ 诱导 $F'$ 到 $E/F$ 上的同构。因此 $E/F$ 是半单的。

## §3. 稠密性定理

设 $E$ 是半单 $R$-模。令 $R'=R'(E)$ 为环 $\operatorname{End}_R(E)$。于是 $E$ 也是一个 $R'$-模，$R'$ 对 $E$ 的作用由

$$
(\varphi,x)\mapsto\varphi(x)
$$

给出，其中 $\varphi\in R'$、$x\in E$。每个 $\alpha\in R$ 通过映射 $f_\alpha(x)=\alpha x$，诱导一个 $R'$-同态 $f_\alpha:E\to E$。这正是条件

$$
\varphi(\alpha x)=\alpha\varphi(x)
$$

的含义。

令 $R''=R''(E)=\operatorname{End}_{R'}(E)$。称 $R'$ 为 $R$ 的**交换子环**，$R''$ 为**双交换子环**。这样便得到环同态

$$
R\to\operatorname{End}_{R'}(E)=R''(E)=R''.
$$

<span class="original-page-anchor" id="pdf-page-656" aria-hidden="true"></span>

由 $\alpha\mapsto f_\alpha$ 给出。现在要问：这个环同态的像有多大？稠密性定理说明，它的像相当大。

**引理 3.1。** *设 $E$ 在 $R$ 上半单。如前所述，令 $R'=\operatorname{End}_R(E)$，$f\in\operatorname{End}_{R'}(E)$。设 $x\in R$。则存在元素 $\alpha\in R$，使得 $\alpha x=f(x)$。*

**译校注：** 原书印作“Let $x\in R$”。这里 $f$ 的定义域为 $E$，而证明使用子模 $Rx\subset E$，所以应为“设 $x\in E$”。

*证明。* 由于 $E$ 是半单模，可以写成 $R$-直和

$$
E=Rx\oplus F,
$$

其中 $F$ 为某个子模。令 $\pi:E\to Rx$ 为投影。则 $\pi\in R'$，所以

$$
f(x)=f(\pi x)=\pi f(x).
$$

这说明 $f(x)\in Rx$，正如所需。

稠密性定理将这个引理推广到 $E$ 的有限多个元素，而不只是一个元素。证明中使用一个对角技巧。

**定理 3.2（Jacobson）。** *设 $E$ 在 $R$ 上半单，令 $R'=\operatorname{End}_R(E)$。设 $f\in\operatorname{End}_{R'}(E)$，$x_1,\ldots,x_n\in E$。则存在元素 $\alpha\in R$，使得*

$$
\alpha x_i=f(x_i)\quad\text{其中}\quad i=1,\ldots,n.
$$

*若 $E$ 在 $R'$ 上有限生成，则自然映射 $R\to\operatorname{End}_{R'}(E)$ 为满射。*

*证明。* 为使记号清楚，先在 $E$ 为单模的情形中进行证明。令 $f^{(n)}:E^{(n)}\to E^{(n)}$ 为乘积映射，从而

$$
f^{(n)}(y_1,\ldots,y_n)=(f(y_1),\ldots,f(y_n)).
$$

令 $R'_n=\operatorname{End}_R(E^{(n)})$。则 $R'_n$ 正是系数在 $R'$ 中的矩阵环。由于 $f$ 在 $E$ 上的作用与 $R'$ 的元素交换，立即可见 $f^{(n)}$ 属于 $\operatorname{End}_{R'_n}(E^{(n)})$。由引理，存在元素 $\alpha\in R$，使得

$$
(\alpha x_1,\ldots,\alpha x_n)=(f(x_1),\ldots,f(x_n)),
$$

这就是我们要证明的结论。

当 $E$ 不是单模时，假设 $E$ 等于有限多个单子模 $E_i$（互不同构）的直和，重数为 $n_i$：

$$
E=E_1^{(n_1)}\oplus\cdots\oplus E_r^{(n_r)}\qquad(E_i\not\approx E_j\quad\text{若}\quad i\ne j).
$$

那么，表示自同态环的矩阵按照直和分解中互不同构的单分量分成对应的块。因此，这里的论证也像前面一样成立。

<span class="original-page-anchor" id="pdf-page-657" aria-hidden="true"></span>

关键在于 $f^{(n)}$ 属于 $\operatorname{End}_{R'_n}(E^{(n)})$，而且可以应用引理。再注意，若 $E$ 在 $R'$ 上有限生成，则元素 $f\in\operatorname{End}_{R'}(E)$ 由它在 $E$ 的有限多个元素上的值确定，所以所断言的满射性 $R\to\operatorname{End}_{R'}(E)$ 立即成立。在下面的应用中，$E$ 是域 $k$ 上的有限维向量空间，$R$ 是 $k$-代数，因此有限性条件自动满足。

当 $E$ 是无限直和时，论证类似，但记号令人不便。不过，在应用中，我们只需要 $E$ 本身为有限多个单模的直和的情形；因此先在这种情形下给出证明，并让有兴趣的读者自行写出其他情形中的形式细节。

**推论 3.3（伯恩赛德定理）。** *设 $E$ 是代数闭域 $k$ 上的有限维向量空间，$R$ 是 $\operatorname{End}_k(E)$ 的子代数。若 $E$ 是单 $R$-模，则 $R=\operatorname{End}_{R'}(E)$。*

*证明。* 我们断言 $\operatorname{End}_R(E)=k$。无论如何，$\operatorname{End}_R(E)$ 是一个除环 $R'$，包含 $k$ 为子环，并且 $k$ 的每个元素都与 $R'$ 的每个元素交换。设 $\alpha\in R'$。则 $k(\alpha)$ 是域。此外，$R'$ 作为 $k$-子空间包含于 $\operatorname{End}_k(E)$，所以在 $k$ 上有限维。因此，$k(\alpha)$ 在 $k$ 上有限；因为 $k$ 代数闭，它等于 $k$。这证明了 $\operatorname{End}_R(E)=k$。现在取 $E$ 在 $k$ 上的一组基 $\{v_1,\ldots,v_n\}$。设 $A\in\operatorname{End}_k(E)$。由稠密性定理，存在 $\alpha\in R$，使得

$$
\alpha v_i=Av_i\quad\text{其中}\quad i=1,\ldots,n.
$$

由于 $A$ 的作用由它在基上的作用确定，得到 $R=\operatorname{End}_k(E)$。

推论 3.3 可用于习题 8 中所述的下述情形。设 $E$ 是域 $k$ 上的有限维向量空间。设 $G$ 为 $\operatorname{GL}(E)$ 的（乘法）子幺半群。$E$ 的一个 **$G$-不变**子空间 $F$，是指对所有 $\sigma\in G$ 均满足 $\sigma F\subset F$ 的子空间。若 $E\ne0$，且除了 $0$ 和 $E$ 本身以外没有其他 $G$-不变子空间，则称 $E$ 为 **$G$-单的**。令 $R=k[G]$ 为 $G$ 在 $k$ 上生成的 $\operatorname{End}_k(E)$ 的子代数。由于假设 $G$ 为幺半群，可知 $R$ 由线性组合

$$
\sum a_i\sigma_i
$$

组成，其中 $a_i\in k$、$\sigma_i\in G$。于是可见，$E$ 的子空间 $F$ 是 $G$-不变的，当且仅当它是 $R$-不变的。因此 $E$ 是 $G$-单的，当且仅当它按我们一直考虑的意义在 $R$ 上为单模。于是可以按 Burnside 原来的表述重新陈述其定理：

**推论 3.4。** *设 $E$ 是代数闭域 $k$ 上的有限维向量空间，$G$ 是 $\operatorname{GL}(E)$ 的一个（乘法）子幺半群。*

<span class="original-page-anchor" id="pdf-page-658" aria-hidden="true"></span>

*若 $E$ 是 $G$-单的，则 $k[G]=\operatorname{End}_k(E)$。*

当 $k$ 不是代数闭域时，仍能得到一些结果。一般地，设 $R$ 是环，$E$ 是单 $R$-模。已经看到，$\operatorname{End}_R(E)$ 是除环，记为 $D$，而 $E$ 是 $D$ 上的向量空间。

设 $R$ 是环，$E$ 是任意 $R$-模。若满足下述条件，则称 $E$ 是**忠实模**：给定 $\alpha\in R$，若对所有 $x\in E$ 都有 $\alpha x=0$，则 $\alpha=0$。在应用中，$E$ 是域 $k$ 上的向量空间，并有 $R$ 到 $\operatorname{End}_k(E)$ 中的环同态。这样，$E$ 成为 $R$-模；它忠实，当且仅当这个同态是单射。

**推论 3.5（韦德伯恩定理）。** *设 $R$ 是环，$E$ 是 $R$ 上的单忠实模。令 $D=\operatorname{End}_R(E)$，并假设 $E$ 在 $D$ 上有限维。则 $R=\operatorname{End}_D(E)$。*

*证明。* 设 $\{v_1,\ldots,v_n\}$ 为 $E$ 在 $D$ 上的一组基。给定 $A\in\operatorname{End}_D(E)$，由定理 3.2，存在 $\alpha\in R$，使得

$$
\alpha v_i=Av_i\quad\text{其中}\quad i=1,\ldots,n.
$$

所以映射 $R\to\operatorname{End}_D(E)$ 是满射。$E$ 在 $R$ 上忠实的假设说明它是单射，推论得证。

**例。** 设 $R$ 是域 $k$ 上的有限维代数，并假定 $R$ 有单位元，因此是环。如果除了 $0$ 和 $R$ 本身以外，$R$ 没有其他双边理想，则 $R$ 上的任意非零模 $E$ 都是忠实的，因为同态

$$
R\to\operatorname{End}_k(E)
$$

的核是一个不等于 $R$ 的双边理想。若 $E$ 是单模，则 $E$ 在 $k$ 上有限维。于是 $D$ 是 $k$ 上的有限维除代数。韦德伯恩定理给出了 $R$ 作为 $E$ 的 $D$-自同态环的一种表示。

在 $R$ 有限维的假设下，只需取一个非零极小左理想，就能找到一个单模。只要取 $k$ 上非零维数最小的左理想，就得到这样的理想。在这种情形中，下面还将给出韦德伯恩定理的一个更短的证明（Rieffel 定理）。

**推论 3.6。** *设 $R$ 是环，又是代数闭域 $k$ 上的有限维代数。设 $V$ 是 $k$ 上的有限维向量空间，具有单忠实表示 $\rho:R\to\operatorname{End}_k(V)$。则 $\rho$ 是同构，换言之，$R\approx\operatorname{Mat}_n(k)$。*

*证明。* 应用推论 3.5，并注意 $D$ 在 $k$ 上有限维。给定 $\alpha\in D$，注意 $k(\alpha)$ 是 $D$ 的交换子域，因此由 $k$ 代数闭的假设有 $k(\alpha)=k$，推论随即成立。

<span class="original-page-anchor" id="pdf-page-659" aria-hidden="true"></span>

**注。** 这个推论适用于下面将定义的单环。

接着假设 $V_1,\ldots,V_m$ 是域 $k$ 上的有限维向量空间，$R$ 是具有表示

$$
R\to\operatorname{End}_k(V_i),\quad i=1,\ldots,m
$$

的 $k$-代数，因此 $V_i$ 是 $R$-模。若令

$$
E=V_1\oplus\cdots\oplus V_m,
$$

则 $E$ 在 $R'(E)$ 上有限，因而由雅各布森稠密性定理得到下述结论。

**定理 3.7（投影算子的存在性）。** *设 $k$ 是域，$R$ 是 $k$-代数，$V_1,\ldots,V_m$ 是有限维 $k$-空间，同时也是单 $R$-模，且当 $i\ne j$ 时，$V_i$ 与 $V_j$ 不 $R$-同构。则存在元素 $e_i\in R$，使 $e_i$ 在 $V_i$ 上作用为恒等映射，且当 $j\ne i$ 时，$e_iV_j=0$。*

*证明。* 注意，从直和 $E$ 到第 $i$ 个因子的投影 $f_i$ 属于 $\operatorname{End}_{R'}(E)$，因为若 $\varphi\in R'$，则对所有 $j$ 均有 $\varphi(V_j)\subset V_j$。因此可以应用稠密性定理来完成证明。

**推论 3.8（Bourbaki）。** *设 $k$ 为特征 $0$ 的域，$R$ 为 $k$-代数，$E,F$ 为在 $k$ 上有限维的半单 $R$-模。对每个 $\alpha\in R$，令 $\alpha_E,\alpha_F$ 分别为对应的 $E$ 与 $F$ 上的 $k$-自同态。假定它们的迹相等，即*

$$
\operatorname{tr}(\alpha_E)=\operatorname{tr}(\alpha_F)\quad\text{对所有 }\alpha\in R.
$$

*则 $E$ 与 $F$ 作为 $R$-模同构。*

*证明。* $E$ 和 $F$ 分别同构于有限多个单 $R$-模带有一定重数的直和。设 $V$ 为单 $R$-模，并假设

$$
\begin{aligned}
E&=V^{(n)}\oplus\text{不同构于 }V\text{ 的直和项}\\
F&=V^{(m)}\oplus\text{不同构于 }V\text{ 的直和项}.
\end{aligned}
$$

只需证明 $m=n$。令 $e_V$ 为定理 3.7 中找到的 $R$ 的元素，它在 $V$ 上作用为恒等映射，在 $E,F$ 的其他直和项上作用为 $0$。于是

$$
\operatorname{tr}(e_E)=n\dim_k(V)\qquad\text{且}\qquad\operatorname{tr}(e_F)=m\dim_k(V).
$$

由于按假设迹相等，可得 $m=n$，证明完成。注意，这里使用了特征为 $0$，因为迹的值位于 $k$ 中。

**例。** 用表示的语言来说，设 $G$ 为幺半群，并且<span class="original-page-anchor" id="pdf-page-660" aria-hidden="true"></span>有两个取值于有限维 $k$-空间的半单表示

$$
\rho:G\to\operatorname{End}_k(E)\qquad\text{和}\qquad\rho':G\to\operatorname{End}_k(F)
$$

（因此 $\rho$ 与 $\rho'$ 将 $G$ 映入 $\operatorname{End}_k$ 的乘法幺半群）。假设对所有 $\sigma\in G$，均有 $\operatorname{tr}\rho(\sigma)=\operatorname{tr}\rho'(\sigma)$。则 $\rho$ 与 $\rho'$ 同构。事实上，令 $R=k[G]$，则 $\rho$ 和 $\rho'$ 都延拓为 $R$ 的表示。由线性性，对所有 $\alpha\in R$ 都有 $\operatorname{tr}\rho(\alpha)=\operatorname{tr}\rho'(\alpha)$，所以可以应用推论 3.8。

## §4. 半单环

若环 $R$ 满足 $1\ne0$，且 $R$ 作为自身上的左模是半单的，则称 $R$ 为**半单环**。

**命题 4.1。** *若 $R$ 是半单环，则每个 $R$-模都是半单的。*

*证明。* 一个 $R$-模是某个自由模的商模，而自由模是若干个 $R$ 的直和。应用命题 2.2，即完成证明。

**例。** 1) 设 $k$ 是域，令 $R=\operatorname{Mat}_n(k)$ 为 $k$ 上的 $n\times n$ 矩阵代数。则 $R$ 是半单的，实际上还是单的；其定义与证明将在 §5 的定理 5.5 中给出。

2) 设 $G$ 为有限群，并假设 $k$ 的特征不整除 $\#(G)$。则群环 $k[G]$ 是半单的；我们将在第十八章定理 1.2 中证明这一点。

3) 实数上的克利福德代数 $C_n$ 是半单的。参见第十九章习题 19。

$R$ 的左理想是 $R$-模，因此当它作为模是单的时，就称这个左理想为单的。若两个理想 $L,L'$ 作为模同构，则称它们同构。

现在将 $R$ 分解为其单左理想的和，从而得到 $R$ 的结构定理。

设 $\{L_i\}_{i\in I}$ 为一族单左理想，其中任何两个都不同构，并且每个单左理想都同构于它们中的一个。称这个族为单左理想的同构类的一族代表。

**引理 4.2。** *设 $L$ 为单左理想，$E$ 为单 $R$-模。若 $L$ 与 $E$ 不同构，则 $LE=0$。*

*证明。* 有 $RLE=LE$，而 $LE$ 是 $E$ 的子模，因此等于<span class="original-page-anchor" id="pdf-page-661" aria-hidden="true"></span>$0$ 或 $E$。假设 $LE=E$。取 $y\in E$，使得

$$
Ly\ne0.
$$

由于 $Ly$ 是 $E$ 的子模，所以 $Ly=E$。映射 $\alpha\mapsto\alpha y$ 是 $L$ 到 $E$ 中的同态，它为满射，因此非零。由于 $L$ 为单模，这个同态是同构。

令

$$
R_i=\sum_{L\approx L_i}L
$$

为所有同构于 $L_i$ 的单左理想的和。由引理得到，当 $i\ne j$ 时，$R_iR_j=0$。下面将不断使用这一点。注意，$R_i$ 是左理想，且 $R$ 为和

$$
R=\sum_{i\in I}R_i,
$$

因为 $R$ 是单左理想的和。因此对任意 $j\in I$，

$$
R_j\subset R_jR=R_jR_j\subset R_j,
$$

第一个包含关系是因为 $R$ 有单位元，最后一个是因为 $R_j$ 为左理想。所以 $R_j$ 也是右理想，即对所有 $j\in I$，$R_j$ 都是双边理想。

可以将 $R$ 的单位元 $1$ 表示为和

$$
1=\sum_{i\in I}e_i,
$$

其中 $e_i\in R_i$。这个和实际上是有限的，几乎所有 $e_i$ 都为 $0$。设 $e_i\ne0$ 的指标为 $i=1,\ldots,s$，于是写成

$$
1=e_1+\cdots+e_s.
$$

对于任意 $x\in R$，写成

$$
x=\sum_{i\in I}x_i,\qquad x_i\in R_i.
$$

对 $j=1,\ldots,s$，有 $e_jx=e_jx_j$，并且

$$
x_j=1\cdot x_j=e_1x_j+\cdots+e_sx_j=e_jx_j.
$$

此外，$x=e_1x+\cdots+e_sx$。这证明了不存在 $i=1,\ldots,s$ 之外的指标，而且 $x$ 的第 $i$ 个分量 $x_i$ 由 $e_ix=e_ix_i$ 唯一确定。因此和 $R=R_1+\cdots+R_s$ 为直和；进一步，$e_i$ 是 $R_i$ 的单位元，所以 $R_i$ 是环。由于<span class="original-page-anchor" id="pdf-page-662" aria-hidden="true"></span>当 $i\ne j$ 时，$R_iR_j=0$，所以实际上

$$
R=\prod_{i=1}^s R_i
$$

是各环 $R_i$ 的直积。

若环 $R$ 是半单的，并且只有一个单左理想的同构类，则称 $R$ 为**单环**。可见，我们已经证明了半单环的结构定理：

**定理 4.3。** *设 $R$ 为半单环。则互不同构的单左理想只有有限多个，记为 $L_1,\ldots,L_s$。若*

$$
R_i=\sum_{L\approx L_i}L
$$

*为所有同构于 $L_i$ 的单左理想的和，则 $R_i$ 为双边理想，同时也是环（运算由 $R$ 诱导），而 $R$ 作为环同构于直积*

$$
R=\prod_{i=1}^s R_i.
$$

*每个 $R_i$ 都是单环。若 $e_i$ 是它的单位元，则 $1=e_1+\cdots+e_s$，且 $R_i=Re_i$。当 $i\ne j$ 时，有 $e_ie_j=0$。*

现在讨论模。

**定理 4.4。** *设 $R$ 是半单环，$E$ 是非零 $R$-模。则*

$$
E=\bigoplus_{i=1}^s R_iE=\bigoplus_{i=1}^s e_iE,
$$

*而 $R_iE$ 是 $E$ 中由所有同构于 $L_i$ 的单子模之和构成的子模。*

*证明。* 令 $E_i$ 为 $E$ 中所有同构于 $L_i$ 的单子模的和。若 $V$ 是 $E$ 的单子模，则 $RV=V$，因此对某个 $i$ 有 $L_iV=V$。由前面的引理，$L_i\approx V$。所以 $E$ 是 $E_1,\ldots,E_s$ 的直和。于是显然有 $R_iE=E_i$。

**推论 4.5。** *设 $R$ 为半单环。每个单模都同构于单左理想 $L_i$ 中的一个。*

**推论 4.6。** *在同构意义下，单环恰有一个单模。*

<span class="original-page-anchor" id="pdf-page-663" aria-hidden="true"></span>

这两个推论都是定理 4.3 和 4.4 的直接结果。

**命题 4.7。** *设 $k$ 为域，$E$ 为 $k$ 上的有限维向量空间。设 $S$ 为 $\operatorname{End}_k(E)$ 的子集，$R$ 为 $S$ 的元素生成的 $k$-代数。则 $R$ 是半单的，当且仅当 $E$ 是半单 $R$（或 $S$）模。*

**译校注：** 原命题没有明确要求 $E\ne0$。按本节的定义，半单环须满足 $1\ne0$，而零模仍是半单模。因此，若 $E=0$，则 $R\subset\operatorname{End}_k(0)=0$ 为零环，所述等价关系不成立；本命题需要非零空间这一假设。原命题文字予以保留。

*证明。* 若 $R$ 半单，则由命题 4.1，$E$ 半单。反之，假设 $E$ 作为 $S$-模半单。于是 $E$ 作为 $R$-模半单，因此为直和

$$
E=\bigoplus_{i=1}^n E_i,
$$

其中每个 $E_i$ 均为单模。对每个 $i$，存在元素 $v_i\in E_i$，使 $E_i=Rv_i$。映射

$$
x\mapsto(xv_1,\ldots,xv_n)
$$

是 $R$ 到 $E$ 中的 $R$-同态；因为 $R$ 包含于 $\operatorname{End}_k(E)$，这个映射是单射。由命题 2.2，半单模的子模半单，因此得到所需的结果。

## §5. 单环

**引理 5.1。** *设 $R$ 为环，$\psi\in\operatorname{End}_R(R)$ 为把 $R$ 视为 $R$-模时到自身的同态。则存在 $\alpha\in R$，使得对所有 $x\in R$ 都有 $\psi(x)=x\alpha$。*

*证明。* 有 $\psi(x)=\psi(x\cdot1)=x\psi(1)$。令 $\alpha=\psi(1)$。

**定理 5.2。** *设 $R$ 为单环。则 $R$ 为单左理想的有限直和。除了 $0$ 和 $R$ 以外，没有其他双边理想。若 $L,M$ 为单左理想，则存在 $\alpha\in R$，使得 $L\alpha=M$。并且有 $LR=R$。*

*证明。* 根据定义，$R$ 也是半单的，因此是单左理想的直和，记为 $\bigoplus_{j\in J}L_j$。可以将 $1$ 写成有限和 $1=\sum_{j=1}^m\beta_j$，其中 $\beta_j\in L_j$。于是

$$
R=\bigoplus_{j=1}^m R\beta_j=\bigoplus_{j=1}^m L_j.
$$

<span class="original-page-anchor" id="pdf-page-664" aria-hidden="true"></span>

这证明了第一个断言。第二个断言是第三个断言的结果。因此设 $L$ 为单左理想。因为 $RLR=LR$，$LR$ 是左理想；由于 $R$ 半单，它是单左理想的直和，记为

$$
LR=\bigoplus_{j=1}^m L_j,\quad L=L_1.
$$

设 $M$ 为单左理想。有直和分解 $R=L\oplus L'$。令 $\pi:R\to L$ 为投影，它是 $R$-自同态。令 $\sigma:L\to M$ 为同构（由定理 4.3，它存在）。于是 $\sigma\circ\pi:R\to R$ 为 $R$-自同态。由引理，存在 $\alpha\in R$，使得

$$
\sigma\circ\pi(x)=x\alpha\quad\text{对所有 }x\in R.
$$

将其应用于 $x\in L$，得到

$$
\sigma(x)=x\alpha\quad\text{对所有 }x\in L.
$$

映射 $x\mapsto x\alpha$ 是 $L$ 到 $M$ 中的非零 $R$-同态，因此是同构。立即得出 $LR=R$，从而证明了定理。

**推论 5.3。** *设 $R$ 为单环，$E$ 为单 $R$-模，$L$ 为 $R$ 的单左理想。则 $LE=E$，且 $E$ 忠实。*

*证明。* 有 $LE=L(RE)=(LR)E=RE=E$。假设对某个 $\alpha\in R$ 有 $\alpha E=0$。则 $R\alpha RE=R\alpha E=0$。但是 $R\alpha R$ 是双边理想。因此 $R\alpha R=0$，所以 $\alpha=0$。这证明了 $E$ 忠实。

**定理 5.4（Rieffel）。** *设 $R$ 为一个除了 $0$ 与 $R$ 之外没有其他双边理想的环。设 $L$ 为非零左理想，$R'=\operatorname{End}_R(L)$，$R''=\operatorname{End}_{R'}(L)$。则自然映射 $\lambda:R\to R''$ 为同构。*

*证明。* $\lambda$ 的核是双边理想，所以 $\lambda$ 是单射。由于 $LR$ 为双边理想，有 $LR=R$，且 $\lambda(L)\lambda(R)=\lambda(R)$。对任意 $x,y\in L$ 及 $f\in R''$，有 $f(xy)=f(x)y$，因为右乘 $y$ 是 $L$ 的 $R$-自同态。因此 $\lambda(L)$ 是 $R''$ 的左理想，所以

$$
R''=R''\lambda(R)=R''\lambda(L)\lambda(R)=\lambda(L)\lambda(R)=\lambda(R),
$$

正如所需。

在 Rieffel 定理中，不必假设 $L$ 为单模。

<span class="original-page-anchor" id="pdf-page-665" aria-hidden="true"></span>

另一方面，$L$ 是理想。因此这个定理与前面同类的定理并不等价。在 §7 中，将给出一个很一般的条件，使环到模的双自同态环的典范同态

$$
R\to R''
$$

为同构。这个条件将涵盖前面的所有情形。

如韦德伯恩定理之后的例子所指出的，当 $R$ 是域 $k$ 上的有限维（含单位元）代数时，可以应用 Rieffel 定理给出另一个证明。

下一个定理给出逆向的结论，表明除代数上的矩阵环是单的。

**定理 5.5。** *设 $D$ 为除环，$E$ 为 $D$ 上的有限维向量空间。令 $R=\operatorname{End}_D(E)$。则 $R$ 是单环，$E$ 是单 $R$-模。此外，$D=\operatorname{End}_R(E)$。*

**译校注：** 原定理只写 $E$ 有限维，没有明确要求 $E\ne0$。若 $E=0$，则 $R=\operatorname{End}_D(0)=0$，既不是本节定义的单环，$E$ 也不是单模，而且 $\operatorname{End}_R(0)=0\ne D$。因此结论需要 $E\ne0$；原证明也以取 $v\ne0$ 开始。原定理文字予以保留。

*证明。* 首先证明 $E$ 是单 $R$-模。取 $v\in E$、$v\ne0$。可以将 $v$ 补成 $E$ 在 $D$ 上的一组基；所以给定 $w\in E$，存在 $\alpha\in R$，使 $\alpha v=w$。因此 $E$ 除了 $0$ 和自身以外，没有其他不变子空间，从而在 $R$ 上是单的。显然，$E$ 在 $R$ 上忠实。设 $\{v_1,\ldots,v_m\}$ 为 $E$ 在 $D$ 上的一组基。映射

$$
\alpha\mapsto(\alpha v_1,\ldots,\alpha v_m)
$$

是 $R$ 到 $E^{(m)}$ 中的单射 $R$-同态。给定 $(w_1,\ldots,w_m)\in E^{(m)}$，存在 $\alpha\in R$，使 $\alpha v_i=w_i$，所以 $R$ 与 $E^{(m)}$ $R$-同构。这表明 $R$（作为自身上的模）同构于单模的直和，因此半单。此外，这些单模全都彼此同构，所以由定理 4.3，$R$ 是单环。

还需证明 $D=\operatorname{End}_R(E)$。注意，$E$ 是 $D$ 上的半单模，因为它是向量空间，每个子空间都有补子空间。因此可以应用稠密性定理（现在互换了 $R$ 和 $D$ 的角色！）。设 $\varphi\in\operatorname{End}_R(E)$。取 $v\in E$、$v\ne0$。由稠密性定理，存在元素 $a\in D$，使 $\varphi(v)=av$。设 $w\in E$。存在元素 $f\in R$，使 $f(v)=w$。于是

$$
\varphi(w)=\varphi(f(v))=f(\varphi(v))=f(av)=af(v)=aw.
$$

因此，对所有 $w\in E$ 都有 $\varphi(w)=aw$。这意味着 $\varphi\in D$，证明完成。

**定理 5.6。** *设 $k$ 为域，$E$ 为一个有限维向量空间，其* <span class="original-page-anchor" id="pdf-page-666" aria-hidden="true"></span>*在 $k$ 上的维数为 $m$。令 $R=\operatorname{End}_k(E)$。则 $R$ 为 $k$-空间，且*

$$
\dim_kR=m^2.
$$

*此外，$m$ 是将 $R$ 分解为单左理想直和时出现的单左理想的个数。*

*证明。* $E$ 的 $k$-自同态构成的 $k$-空间，由 $k$ 中的 $m\times m$ 矩阵空间表示，所以 $R$ 作为 $k$-空间的维数为 $m^2$。另一方面，定理 5.5 的证明表明，$R$ 作为 $R$-模与直和 $E^{(m)}$ $R$-同构。我们知道，模分解为单模直和的分解具有唯一性（命题 1.2），因而结论得证。

用 §1 中引入的术语来说，定理 5.6 中的整数 $m$ 就是 $R$ 的**长度**。

选定 $E$ 的一组基后，可以将 $R=\operatorname{End}_k(E)$ 与矩阵环 $\operatorname{Mat}_m(k)$ 等同。这时，可以取理想 $L_i$（$i=1,\ldots,m$）为单左理想，其中 $L_i$ 中的矩阵除了第 $i$ 列以外，所有系数都为 $0$。因此，$L_1$ 的一个元素形如下式：

![第一列左理想中的矩阵](/library/volume-86/diagrams/pdf-0666-first-column-ideal.png)

可见，$R$ 是这 $m$ 列的直和。

还注意到，定理 5.5 蕴含下述结论：

*若矩阵 $M\in\operatorname{Mat}_m(k)$ 与 $\operatorname{Mat}_m(k)$ 的所有元素交换，则 $M$ 为标量矩阵。*

事实上，这样的矩阵 $M$ 可视为 $E$ 的 $R$-自同态，而由定理 5.5 知道，这种自同态位于 $k$ 中。当然，也可以用直接的计算验证这一点。

## §6. 雅各布森根、基变换与张量积

设 $R$ 为环，$M$ 为极大左理想。则 $R/M$ 为 $R$-模，而且实际上是单模。事实上，设 $\bar J$ 为 $R/M$ 的子模，满足 $\bar J\ne R/M$。令 $J$ 为它在典范同态下于 $R$ 中的原像。

<span class="original-page-anchor" id="pdf-page-667" aria-hidden="true"></span>

于是 $J$ 为不等于 $M$ 的左理想，因为 $\bar J\ne R/M$，所以 $J=R$，且 $\bar J=0$。

**译校注：** 原书印作“$J$ is a left ideal $\ne M$ ... so $J=R$”。由上一页条件 $\bar J\ne R/M$，原像 $J$ 应满足 $J\ne R$；它包含极大左理想 $M$，因此应得 $J=M$，继而 $\bar J=J/M=0$。原句中的两个理想符号互换了。

反之，设 $E$ 为单 $R$-模，取 $v\in E$、$v\ne0$。则 $Rv$ 是 $E$ 的非零子模，因此 $Rv=E$。令 $M$ 为同态 $x\mapsto xv$ 的核。则 $M$ 为左理想，而且极大；否则存在左理想 $M'$，满足 $R\supset M'\supset M$，且 $M'\ne R$、$M'\ne M$。于是 $R/M\approx E$，而 $R/M'$ 为 $E$ 的非零同态像；由于 $E$ 是单模，这不可能存在（舒尔引理，命题 1.1）。因此得到极大左理想与单 $R$-模（在同构意义下）之间的双射。

**译校注：** 原书这里用“a bijection”。具体映射 $M\mapsto[R/M]$ 一般是满射，并不是极大左理想集合到单模同构类集合的单射。例如 $\operatorname{Mat}_2(k)$ 有不同的极大左理想，但只有一个单模同构类。若按商模同构关系将极大左理想也取等价类，才能得到所述双射；原句不作这一等价处理时，应称满射对应。

定义 $R$ 的**雅各布森根**为 $R$ 的所有极大左理想的交所构成的左理想 $N$。也可记为 $N=\operatorname{Rad}(R)$。

**定理 6.1。**

(a) *对每个单 $R$-模，有 $NE=0$。*

(b) *根 $N$ 是双边理想，包含所有幂零双边理想。*

(c) *设 $R$ 是域 $k$ 上的有限维代数。它的根为 $\{0\}$，当且仅当 $R$ 半单。*

(d) *若 $R$ 是域 $k$ 上的有限维代数，则它的根 $N$ 幂零（即对某个正整数 $r$，有 $N^r=0$）。*

这些陈述很容易证明，将在适当处给出提示。参见习题 1 至 5。

注意，在有限维条件下，根为 $0$ 给出了环半单的一个有用判别；下一个结果将使用它。

**定理 6.2。** *设 $A$ 是域 $k$ 上有限维的半单代数，$K$ 是 $k$ 的有限可分扩张。则 $K\otimes_kA$ 在 $K$ 上半单。*

*证明。* 根据半单性的根判别，只需证明 $K\otimes_kA$ 的根为零；而且只需对一个比 $K$ 更大的扩张证明这一点，因此可以假定 $K$ 在 $k$ 上伽罗瓦，伽罗瓦群记为 $G$。则 $G$ 通过

$$
\sigma(x\otimes a)=\sigma x\otimes a\quad\text{其中 }x\in K\quad\text{且 }a\in A
$$

作用于 $K\otimes A$。

令 $N$ 为 $K\otimes A$ 的根。由于 $N$ 幂零，对所有 $\sigma\in G$，$\sigma N$ 也幂零；因此 $\sigma N=N$，因为 $N$ 是最大的幂零理想（习题 5）。设 $\{a_1,\ldots,a_m\}$ 是 $A$ 在 $k$ 上的一组基。假设 $N$ 包含元素

$$
\xi=\sum x_i\otimes a_i\ne0\quad\text{其中 }x_i\in K.
$$

对每个 $y\in K$，元素 $(y\otimes1)\xi=\sum yx_i\otimes a_i$ 也在 $N$ 中。于是

$$
\operatorname{trace}((y\otimes1)\xi)=\sum\sigma\xi=\sum\operatorname{Tr}(yx_i)\otimes a_i=\sum1\otimes a_i\operatorname{Tr}(yx_i)
$$

也在 $N$ 中，并且位于 $1\otimes A=A$ 中，从而证明了定理。

**译校注：** 原书等式中间印作 $\sum\sigma\xi$，漏掉了 $y\otimes1$。左侧取的是 $(y\otimes1)\xi$ 的伽罗瓦迹，所以这一项应为 $\sum_{\sigma\in G}\sigma((y\otimes1)\xi)$；展开后才得到后面的 $\operatorname{Tr}(yx_i)$。原式 $\sum\sigma\xi$ 展开会给出 $\operatorname{Tr}(x_i)$。

<span class="original-page-anchor" id="pdf-page-668" aria-hidden="true"></span>

**注。** 对于 $A$ 是 $k$ 的有限扩张的情形，可参照第十六章习题 1、2、3。

设 $A$ 是域 $k$ 上的有限维半单代数。由定理 6.2，若 $k$ 是完美域，则标量扩张 $A\otimes_k k^a$ 是半单的。一般地，若 $A\otimes_k k^a$ 是半单的，就称 $k$ 上的代数 $A$ 为**绝对半单的**。

现在考察代数闭域上的半单代数。

**定理 6.3。** *设 $A,B$ 是代数闭域 $k$ 上的有限维单代数。则 $A\otimes_k B$ 也是单的。存在有限维 $k$ 向量空间 $V,W$，使得 $A\approx\operatorname{End}_k(V)$、$B\approx\operatorname{End}_k(W)$，并且有自然同构*

$$
A\otimes_k B\approx\operatorname{End}_k(V\otimes_k W)\approx\operatorname{End}_k(V)\otimes_k\operatorname{End}_k(W).
$$

*证明。* 此公式是第十六章定理 2.5 的特例，而同构 $A\approx\operatorname{End}_k(V)$、$B\approx\operatorname{End}_k(W)$ 的存在性由韦德伯恩定理或其推论得到。

设 $A$ 是 $k$ 上的代数，$F$ 是 $k$ 的扩张域。用 $A_F$ 表示标量扩张

$$
A_F=A\otimes_k F.
$$

于是 $A_F$ 是 $F$ 上的代数。作为习题，证明：若 $k$ 是 $A$ 的中心，则 $F$ 是 $A_F$ 的中心。（这里将 $F$ 与 $1\otimes F$ 等同。）

设 $A,B$ 是 $k$ 上的代数。留给读者证明：对于 $k$ 的每个扩张域 $F$，都有自然同构

$$
(A\otimes_k B)_F=A_F\otimes_F B_F.
$$

将以上讨论应用于半单代数的张量积。

**定理 6.4。** *设 $A,B$ 是域 $k$ 上的有限维绝对半单代数。则 $A\otimes_k B$ 是绝对半单的。*

*证明。* 令 $F=k^a$。由假设，$A_F$ 是半单的，因而是若干单代数的直积；这些单代数是矩阵代数。特别地，可以应用定理 6.3，得知 $A_F\otimes_F B_F$ 的根为零。因此 $A\otimes_k B$ 的根为零（因为若 $N$ 是它的根，则 $N\otimes_k F=N_F$ 是 $A_F\otimes_F B_F$ 的幂零理想），由定理 6.1(c)，$A\otimes_k B$ 是半单的。

**注。** 我们在一些特殊情形下很快证明了上述张量积定理；这些情形在各种应用中已经很重要。对于更一般的处理，我推荐布尔巴基的《代数》第八章，其中详尽讨论了半单代数和单代数的张量积。

<span class="original-page-anchor" id="pdf-page-669" aria-hidden="true"></span>

## §7. 平衡模

设 $R$ 是环，$E$ 是模。令 $R'(E)=\operatorname{End}_R(E)$，并令

$$
R''(E)=\operatorname{End}_{R'}(E).
$$

设 $\lambda:R\to R''$ 是自然同态，满足：对于 $x\in R$、$v\in E$，有 $\lambda_x(v)=xv$。若 $\lambda$ 是同构，就称 $E$ 为**平衡的**。若每个模都是 $E$ 与自身的某个（可能无限的）直和的同态像，就称 $E$ 为（$R$ 模的）**生成元**。例如，$R$ 是生成元。

一个更有意思的例子是里费尔定理 5.4 中的左理想 $L$，它是生成元，因为 $LR=R$ 蕴含存在满同态 $L\times\cdots\times L\to R$：我们可以将 $1$ 写成有限组合

$$
1=x_1a_1+\cdots+x_na_n\quad\text{其中 }x_i\in L\text{ 且 }a_i\in R.
$$

映射 $(x_1,\ldots,x_n)\mapsto x_1a_1+\cdots+x_na_n$ 是左模到 $R$ 的满 $R$ 同态。

若 $E$ 是生成元，则存在满同态 $E^{(n)}\to R$（可以取有限的 $n$，因为 $R$ 是有限生成的，只由一个元素 $1$ 生成）。

**定理 7.1（森田）。** *设 $E$ 是 $R$ 模。则 $E$ 是生成元，当且仅当 $E$ 是平衡的，而且作为 $R'(E)$ 模是有限生成的投射模。*

*证明。* 我们将证明定理的一半，另一半留给读者利用类似想法证明（见习题 12）。因此，假设 $E$ 是生成元，并用费思给出的论证证明它具有其余性质。

首先证明：对于任意模 $F$，$R\oplus F$ 是平衡的。将 $R$、$F$ 分别与 $R\oplus F$ 的子模 $R\oplus0$、$0\oplus F$ 等同。对于 $w\in F$，令 $\psi_w:R\oplus F\to F$ 为映射 $\psi_w(x+v)=xw$。则任意 $f\in R''(R\oplus F)$ 都与 $\pi_1$、$\pi_2$ 以及每个 $\psi_w$ 交换。由此立即看出 $f(x+v)=f(1)(x+v)$，所以 $R\oplus F$ 是平衡的。设 $E$ 是生成元，并设 $E^{(n)}\to R$ 是满同态。因为 $R$ 是自由模，可写成 $E^{(n)}\approx R\oplus F$，其中 $F$ 是某个模，因而 $E^{(n)}$ 是平衡的。取 $g\in R'(E)$。则 $g^{(n)}$ 与 $R'(E^{(n)})$ 中的每个元素 $\varphi=(\varphi_{ij})$ 交换（其分量 $\varphi_{ij}\in R'(E)$），因此存在某个 $x\in R$，使得 $g^{(n)}=\lambda_x^{(n)}$。于是 $g=\lambda_x$，这证明了 $E$ 是平衡的，因为 $\lambda$ 显然是单射。

> **译校注：** 原文这里印作“Let $g\in R'(E)$”。此处要证明 $\lambda:R\to R''(E)$ 满射，且后一句需要 $g$ 与所有 $R'(E)$ 元素交换，故应取 $g\in R''(E)$。任意 $g\in R'(E)$ 一般不具有该交换性质；将此处的 $R'(E)$ 改为 $R''(E)$，后续对 $g^{(n)}$ 的论证才成立。英文保留原印。

为了证明 $E$ 作为 $R'(E)$ 模是有限生成的，我们有加法群的同构

$$
R'(E)^{(n)}\approx\operatorname{Hom}_R(E^{(n)},E)\approx\operatorname{Hom}_R(R,E)\oplus\operatorname{Hom}_R(F,E).
$$

若将 $R'$ 的作用定义为映射的合成（作用在左边），则这一关系显然也是 $R'$ 模之间的同构。因为在映射 $h\mapsto h(1)$ 下，$\operatorname{Hom}_R(R,E)$ 与 $E$ 是 $R'$ 同构的，所以 $E$ 是 $R'^{(n)}$ 的 $R'$ 同态像，从而作为 $R'$ 模是有限生成的。还可看出，$E$ 是自由 $R'$ 模 $R'^{(n)}$ 的直和项，因此作为 $R'(E)$ 模是投射的。证明完毕。

<span class="original-page-anchor" id="pdf-page-670" aria-hidden="true"></span>

## 习题

### 根

**1.** (a) 设 $R$ 是环。将 $R$ 的所有极大左理想的交所成的左理想 $N$ 定义为 $R$ 的**根**。证明：对于每个单 $R$ 模 $E$，有 $NE=0$。证明 $N$ 是双边理想。(b) 证明 $R/N$ 的根为 $0$。

**2.** 若每个满足 $J_i\ne J_{i+1}$ 的左理想严格下降列 $J_1\supset J_2\supset\cdots$ 都是有限的，就称环为**阿廷环**。(a) 证明域上的有限维代数是阿廷环。(b) 若 $R$ 是阿廷环，证明每个非零左理想都包含一个单左理想。(c) 若 $R$ 是阿廷环，证明每个非空的理想集合都含有一个极小理想。

**3.** 设 $R$ 是阿廷环。证明它的根为 $0$，当且仅当 $R$ 是半单的。[提示：构造 $R$ 到直和 $\bigoplus R/M_i$ 的单射，其中 $\{M_i\}$ 是极大左理想的一个有限集合。]

**4. 中山引理。** 设 $R$ 是任意环，$M$ 是有限生成模。设 $N$ 是 $R$ 的根。若 $NM=M$，证明 $M=0$。[提示：注意，中山引理的证明仍然适用。]

**5.** (a) 设 $J$ 是 $R$ 的双边幂零理想。证明 $J$ 包含在根中。(b) 反过来，假设 $R$ 是阿廷环。证明它的根是幂零的，即存在整数 $r\ge1$，使得 $N^r=0$。[提示：考察幂 $N^r$ 的下降列，并将中山引理应用于满足 $N^\infty L\ne0$ 的极小有限生成左理想 $L\subset N^\infty$。

**6.** 设 $R$ 是半单交换环。证明 $R$ 是若干域的直积。

**7.** 设 $R$ 是域 $k$ 上的有限维交换代数。若 $R$ 中没有非零幂零元素，证明 $R$ 是半单的。

**8.（科尔钦）** 设 $E$ 是域 $k$ 上的有限维向量空间。设 $G$ 是 $\operatorname{GL}(E)$ 的子群，其中每个元素 $A\in G$ 都具有 $I+N$ 的形式，$N$ 为幂零的。假设 $E\ne0$。证明：存在元素 $v\in E$、$v\ne0$，使得对于所有 $A\in G$，都有 $Av=v$。[提示：首先说明此问题归结为求解线性方程，从而将问题化归为 $k$ 代数闭的情形。其次，将其化归为 $E$ 是单 $k[G]$ 模的情形。结合伯恩赛德定理与对所有 $A\in G$ 都有 $\operatorname{tr}(A)=\operatorname{tr}(I)$ 这一事实，证明：若 $A_0\in G$、$A_0=I+N$，则对于所有 $X\in\operatorname{End}_k(E)$，有 $\operatorname{tr}(NX)=0$，从而 $N=0$、$A_0=I$。]

### 半单作用

**9.** 设 $E$ 是域 $k$ 上的有限维向量空间。设 $R$ 是 $\operatorname{End}_k(E)$ 的半单子代数。取 $a,b\in R$。假设

$$
\operatorname{Ker} b_E\supset\operatorname{Ker} a_E,
$$

其中 $b_E$ 是在 $E$ 上乘以 $b$ 的映射，$a_E$ 类似定义。证明：存在元素 $s\in R$，使得 $sa=b$。[提示：化归为 $R$ 单的情形。则 $R=\operatorname{End}_D(E_0)$ 且 $E=E_0^{(n)}$。取 $v_1,\ldots,v_r\in E$ 为 $aE$ 的一组 $D$ 基。由 $s(av_i)=bv_i$ 定义 $s$，并<span class="original-page-anchor" id="pdf-page-671" aria-hidden="true"></span>按 $D$ 线性性扩张 $s$。于是 $sa_E=b_E$，所以 $sa=b$。]

> **译校注（承前页习题 9 的提示）：** 原文印作“Let $v_1,\ldots,v_r\in E$ be a $D$-basis for $aE$”，接着指定 $s(av_i)=bv_i$。为了由此定义 $aE$ 上的映射，应选取预像 $v_i$，使 $av_1,\ldots,av_r$ 为 $aE$ 的 $D$ 基，而不能要求 $v_i$ 本身为 $aE$ 的基。核包含 $\operatorname{Ker}a_E\subset\operatorname{Ker}b_E$ 保证 $av\mapsto bv$ 与预像的选择无关。在提示已作的单环化归中，可先在简单分量 $E_0$ 上如此构造，再作用于各个同构分量。英文保留原印。

**10.** 设 $E$ 是域 $k$ 上的有限维向量空间。取 $A\in\operatorname{End}_k(E)$。若 $E$ 是半单的 $A$ 空间，就称 $A$ 为**半单的**；等价地，设 $R$ 是由 $A$ 生成的 $k$ 代数，要求 $E$ 作为 $R$ 模是半单的。证明：$A$ 是半单的，当且仅当它的极小多项式在 $k$ 上没有重数 $>1$ 的因子。

**11.** 设 $E$ 是域 $k$ 上的有限维向量空间，$S$ 是 $E$ 的一组彼此交换的自同态。令 $R=k[S]$。假设 $R$ 是半单的。证明 $S$ 的每个子集都是半单的。

**12.** 证明：$R$ 模 $E$ 是生成元，当且仅当它是平衡的，并且作为 $R'(E)$ 模是有限生成的投射模。证明定理 5.4 是定理 7.1 的推论。

**13.** 设 $A$ 是商域为 $K$ 的主理想整环。设 $A^n$ 是 $A$ 上的 $n$ 维空间，并令

$$
T=A^n\oplus A^n\oplus\cdots\oplus A^n
$$

为 $A^n$ 与自身的 $r$ 重直和。于是 $T$ 是 $A$ 上秩为 $nr$ 的自由模。若将 $A^n$ 的元素看成列向量，则 $T$ 是 $A$ 上 $n\times r$ 矩阵的空间。令 $M=\operatorname{Mat}_n(A)$ 为 $A$ 上 $n\times n$ 矩阵的环，在 $T$ 的左边作用。$T$ 中的**格** $L$ 是指 $A$ 上秩为 $nr$ 的一个 $A$ 子模。证明：任何这样的、在 $M$ 下稳定的格都与 $T$ 本身 $M$ 同构。因此，格只有一个 $M$ 同构类。[提示：取 $g\in M$ 为左上角元素为 $1$、其余各处为 $0$ 的矩阵，于是 $g$ 将 $A^n$ 投影到一个 $1$ 维子空间上。左乘映射 $g:T\to A_r$ 将 $T$ 映到第一行任意、其余各处为 $0$ 的 $n\times r$ 矩阵的空间上。此外，对于 $T$ 中的任何格 $L$，像 $gL$ 是 $A_r$ 中的一个格，即秩为 $r$ 的自由 $A$ 子模。由初等因子理论，存在 $r\times r$ 矩阵 $Q$，使得

$$
gL=A_rQ\qquad\text{（在右边相乘）}.
$$

再证明 $TQ=L$，并证明在右边乘以 $Q$ 是 $T$ 到 $L$ 的一个 $M$ 同构。]

**14.** 设 $F$ 是域。令 $\mathfrak n=\mathfrak n(F)$ 为 $F$ 上严格上三角 $n\times n$ 矩阵的向量空间。证明 $\mathfrak n$ 实际上是一个代数，且 $\mathfrak n$ 的所有元素都是幂零的（某个正整数次幂为 $0$）。

**15. 共轭表示。** 设 $A$ 是 $F$ 上对角分量非零的对角矩阵所成的乘法群。对于 $a\in A$，用 $c(a)$ 表示 $a$ 在 $\operatorname{Mat}_n(F)$ 上的**共轭作用**，即对于 $M\in\operatorname{Mat}_n(F)$，有 $c(a)M=aMa^{-1}$。(a) 证明 $\mathfrak n$ 在此作用下稳定。(b) 证明 $\mathfrak n$ 在此作用下是半单的。更确切地，对于 $1\le i<j\le n$，令 $E_{ij}$ 为 $(ij)$ 分量为 $1$、其余分量全为 $0$ 的矩阵。则这些矩阵 $E_{ij}$ 构成 $\mathfrak n$ 在 $F$ 上的一组基，且每个 $E_{ij}$ 都是共轭作用的特征向量，即对于 $a=\operatorname{diag}(a_1,\ldots,a_n)$，有

$$
aE_{ij}a^{-1}=(a_i/a_j)E_{ij},
$$

所以相应的特征标 $\chi_{ij}$ 由 $\chi_{ij}(a)=a_i/a_j$ 给出。(c) 证明 $\operatorname{Mat}_n(F)$ 是半单的，而且事实上等于 $\mathfrak d\oplus\mathfrak n\oplus{}^t\mathfrak n$，其中 $\mathfrak d$ 是对角矩阵的空间。
