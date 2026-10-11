---
title: "第十八章 有限群的表示"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第十七章 半单性","link":"/library/volume-86/chapter-017"}
next: {"text":"第十九章 交错积","link":"/library/volume-86/chapter-019"}
---

# 第十八章 有限群的表示

<span class="original-page-anchor" id="pdf-page-672" aria-hidden="true"></span>

群表示理论出现在许多情境中。首先，它也为自身的目的而发展：确定一个给定群的所有不可约表示。例如可参看 Curtis–Reiner 的 *Methods of Representation Theory*（《表示论方法》，Wiley-Interscience，1981）。它也用于有限单群的分类。不过，在本书前面，我们已经见到了表示在伽罗瓦理论以及确定有理数域上的伽罗瓦群中的应用。此外，拓扑群也有类似的理论。在这种情形下，最接近的类比是紧群；读者可以在我的书 *SL₂(R)*（Springer Verlag）第二章 §2 中找到紧群情形的自足论述，与本章 §5 完全类似。实质上，只须把有限和换成积分，其他形式体系则相同。分析只在两处出现：一处是证明紧群的每个不可约表示都是有限维的；另一处是舒尔引理。上述参考书完整展开了这些额外考虑的细节。我撰写 §5 时特意顾及了这一类比。

类似地，读者可以在 *SL₂(R)* 第三章 §2 中找到有关诱导表示的类似材料（该节同样是自足的）。

一般理论的例子有各种形式。定理 8.4 可以看作一个例子，它说明某个表示如何表示为从一维表示诱导出的表示的直和。习题中给出了 $S_3$ 和 $S_4$ 的表示的例子。最后一节完整求出了群 $GL_2(\mathbf F)$ 在 $\mathbf F$ 为有限域时的单特征标，并说明这些特征标在本质上如何来自诱导特征标。

其他也通向李群的例子，可参看 W. Fulton 和 J. Harris 的 *Representation Theory*（《表示论》），Springer Verlag，1991。

<span class="original-page-anchor" id="pdf-page-673" aria-hidden="true"></span>

## §1. 表示与半单性

设 $R$ 是交换环，$G$ 是群。我们构造群代数 $R[G]$。如第二章 §3 所述，它由所有形式线性组合

$$
\sum_{\sigma\in G}a_\sigma\sigma
$$

组成，其中系数 $a_\sigma\in R$，且几乎所有系数都是 $0$。乘法按自然方式定义：

$$
\left(\sum_{\sigma\in G}a_\sigma\sigma\right)\left(\sum_{\tau\in G}b_\tau\tau\right)=\sum_{\sigma,\tau}a_\sigma b_\tau\sigma\tau.
$$

设 $E$ 是 $R$-模。每个代数同态

$$
R[G]\longrightarrow\operatorname{End}_R(E)
$$

都诱导一个群同态

$$
G\longrightarrow\operatorname{Aut}_R(E),
$$

因此环 $R[G]$ 在 $E$ 中的表示给出群的一个表示。给定这样的表示，我们也说 $R[G]$ 或 $G$ **作用**在 $E$ 上。注意，该表示使 $E$ 成为环 $R[G]$ 上的模。

反过来，给定群的一个表示，比如 $\rho:G\to\operatorname{Aut}_R(E)$，可以如下把 $\rho$ 扩张成 $R[G]$ 的表示。设 $\alpha=\sum a_\sigma\sigma$，$x\in E$。定义

$$
\rho(\alpha)x=\sum a_\sigma\rho(\sigma)x.
$$

立即可验证，$\rho$ 已扩张为 $R[G]$ 到 $\operatorname{End}_R(E)$ 的环同态。如果映射 $\rho:G\to\operatorname{Aut}_R(E)$ 是单射，就说 $\rho$ 在 $G$ 上是**忠实的**。不过，$\rho$ 到 $R[G]$ 的扩张未必忠实。

给定 $G$ 在 $E$ 上的表示，若整个讨论中都使用同一个固定的表示，我们常直接写 $\sigma x$ 代替 $\rho(\sigma)x$。

一个 $R$-模 $E$ 连同表示 $\rho$ 称为 **$G$-模**或 **$G$-空间**；若要指明环 $R$，也称为 $(G,R)$-模。若 $E,F$ 是 $G$-模，回忆 $G$-同态 $f:E\to F$ 是满足 $f(\sigma x)=\sigma f(x)$ 的 $R$-线性映射，其中条件对所有 $x\in E$ 和 $\sigma\in G$ 成立。

给定 $G$-同态 $f:E\to F$，注意 $f$ 的核是 $E$ 的 $G$-子模，而 $R$-商模 $F/f(E)$ 唯一地容许 $G$ 的一种作用，使典范映射 $F\to F/f(E)$ 成为 $G$-同态。

所谓**平凡表示** $\rho:G\to\operatorname{Aut}_R(E)$，是指满足 $\rho(G)=1$ 的表示。一个表示是平凡的，当且仅当对所有 $x\in E$ 都有 $\sigma x=x$。在这种情形下，也说 **$G$ 平凡地作用**。

<span class="original-page-anchor" id="pdf-page-674" aria-hidden="true"></span>

令 $G$ 在 $R$ 上平凡地作用，就使 $R$ 成为一个 $G$-模。

现在我们系统地讨论由给定表示在 Hom、对偶及张量积上产生的表示。以后讨论诱导表示时，我们还会重复这种模式。

首先，$\operatorname{Hom}_R(E,F)$ 在如下作用下是 $G$-模：对 $f\in\operatorname{Hom}_R(E,F)$ 定义

$$
([\sigma]f)(x)=\sigma f(\sigma^{-1}x).
$$

作用所需的条件很容易验证。注意表达式内部的 $\sigma^{-1}$。我们通常省略括号，把左边直接写作 $[\sigma]f(x)$。注意 $f$ 是 $G$-同态，当且仅当对所有 $\sigma\in G$ 都有 $[\sigma]f=f$。

我们特别关心 $F=R$（因此作用平凡）的情形，此时 $\operatorname{Hom}_R(E,R)=E^\vee$ 是对偶模。用表示的术语来说，若 $\rho:G\to\operatorname{Aut}_R(E)$ 是 $G$ 在 $E$ 上的表示，则刚才描述的作用给出一个表示，记为

$$
\rho^\vee:G\longrightarrow\operatorname{Aut}_R(E^\vee),
$$

并称为**对偶表示**（文献中也称为 contragredient，即反变表示——哎！）。

现在假设模 $E,F$ 是 $R$ 上的有限维自由模。设 $\rho$ 是 $G$ 在 $E$ 上的表示。设 $M$ 是 $\rho(\sigma)$ 关于某组基的矩阵，$M^\vee$ 是 $\rho^\vee(\sigma)$ 关于对偶基的矩阵。立即可验证

$$
M^\vee={}^tM^{-1}.\tag{1}
$$

接下来考虑张量积而非 Hom。设 $E,E'$ 是 $(G,R)$-模。可以构造它们的张量积 $E\otimes E'$，总是在 $R$ 上取张量积。那么 $G$ 在 $E\otimes E'$ 上有唯一的作用，使得对 $\sigma\in G$ 有

$$
\sigma(x\otimes x')=\sigma x\otimes\sigma x'.
$$

假设 $E,F$ 是 $R$ 上的有限自由模。第十六章推论 5.5 中的 $R$-同构

$$
E^\vee\otimes F\approx\operatorname{Hom}_R(E,F),\tag{2}
$$

立即可验证也是 $G$-同构。

无论 $E$ 是否自由，我们把 $E$ 的 $G$-不变子模定义为：$\operatorname{inv}_G(E)$ 是由满足对所有 $\sigma\in G$ 有 $\sigma x=x$ 的元素 $x\in E$ 构成的 $R$-子模。若 $E,F$ 自由，则有 $R$-同构

$$
\operatorname{inv}_G(E^\vee\otimes F)\approx\operatorname{Hom}_G(E,F).\tag{3}
$$

<span class="original-page-anchor" id="pdf-page-675" aria-hidden="true"></span>

若 $\rho:G\to\operatorname{Aut}_R(E)$ 和 $\rho':G\to\operatorname{Aut}_R(E')$ 分别是 $G$ 在 $E$ 和 $E'$ 上的表示，就把它们的**和** $\rho\oplus\rho'$ 定义为直和 $E\oplus E'$ 上的表示，其中 $\sigma\in G$ 按分量作用。注意，表示的 $G$-同构类在这个直和运算下具有加法幺半群结构，在张量积下也具有结合的乘法结构。用表示的记号，我们把这个乘积记为 $\rho\otimes\rho'$。此乘法对加法（直和）满足分配律。

若 $G$ 是有限群，$E$ 是 $G$-模，则可以定义**迹** $\operatorname{Tr}_G:E\to E$，它是一个 $R$-同态，具体为

$$
\operatorname{Tr}_G(x)=\sum_{\sigma\in G}\sigma x.
$$

注意 $\operatorname{Tr}_G(x)$ 属于 $\operatorname{inv}_G(E)$，即在 $G$ 的所有元素的作用下不变。这是因为

$$
\tau\operatorname{Tr}_G(x)=\sum_{\sigma\in G}\tau\sigma x,
$$

而左乘 $\tau$ 置换了 $G$ 的元素。

特别地，若 $f:E\to F$ 是 $G$-模之间的 $R$-同态，则 $\operatorname{Tr}_G(f):E\to F$ 是 $G$-同态。

**命题 1.1.** *设 $G$ 是有限群，$E',E,F,F'$ 是 $G$-模。设*

$$
E'\xrightarrow{\varphi}E\xrightarrow{f}F\xrightarrow{\psi}F'
$$

*是 $R$-同态，并假设 $\varphi,\psi$ 是 $G$-同态。那么*

$$
\operatorname{Tr}_G(\psi\circ f\circ\varphi)=\psi\circ\operatorname{Tr}_G(f)\circ\varphi.
$$

*证明。* 有

$$
\begin{aligned}
\operatorname{Tr}_G(\psi\circ f\circ\varphi)&=\sum_{\sigma\in G}\sigma(\psi\circ f\circ\varphi)=\sum_{\sigma\in G}(\sigma\psi)\circ(\sigma f)\circ(\sigma\varphi)\\
&=\psi\circ\left(\sum_{\sigma\in G}\sigma f\right)\circ\varphi=\psi\circ\operatorname{Tr}_G(f)\circ\varphi.
\end{aligned}
$$

**定理 1.2（马施克）。** *设 $G$ 是阶为 $n$ 的有限群，$k$ 是特征不整除 $n$ 的域。那么群环 $k[G]$ 是半单的。*

*证明。* 设 $E$ 是 $G$-模，$F$ 是 $G$-子模。由于 $k$ 是域，存在 $k$-子空间 $F'$，使 $E$ 是 $F$ 与 $F'$ 的 $k$-直和。令 $k$-线性映射 $\pi:E\to F$ 为到 $F$ 的投影。那么对所有 $x\in F$ 都有 $\pi(x)=x$。

<span class="original-page-anchor" id="pdf-page-676" aria-hidden="true"></span>

令

$$
\varphi=\frac1n\operatorname{Tr}_G(\pi).
$$

于是有两个 $G$-同态

$$
0\longrightarrow F\underset{\varphi}{\overset{j}{\rightleftarrows}}E
$$

其中 $j$ 是包含映射，且 $\varphi\circ j=\operatorname{id}$。因此 $E$ 是 $F$ 与 $\operatorname{Ker}\varphi$ 的 $G$-直和，这就证明了 $k[G]$ 是半单的。

**除 §7 外，我们用 $G$ 表示有限群，用 $E,F$ 表示有限维 $k$-空间，其中 $k$ 是特征不整除 $\#(G)$ 的域。通常把 $\#(G)$ 记为 $n$。**

## §2. 特征标

设 $\rho:k[G]\to\operatorname{End}_k(E)$ 是一个表示。所谓该表示的**特征标** $\chi_\rho$，是指 $k$-值函数

$$
\chi_\rho:k[G]\longrightarrow k,
$$

它对所有 $\alpha\in k[G]$ 满足 $\chi_\rho(\alpha)=\operatorname{tr}\rho(\alpha)$。这里的迹是第十三章 §3 定义的自同态的迹。若选取 $E$ 在 $k$ 上的一组基，它就是表示 $\rho(\alpha)$ 的矩阵的迹，即对角元之和。前面已经知道，迹不依赖基的选取。

有时我们写 $\chi_E$ 代替 $\chi_\rho$。

也把 $E$ 称为 $\rho$ 的**表示空间**。

所谓**平凡特征标**，是指 $G$ 在等于 $k$ 本身的 $k$-空间上的表示的特征标，其中对所有 $x\in k$ 都有 $\sigma x=x$。它是在 $G$ 的所有元素上取值 $1$ 的函数。我们把它记为 $\chi_0$；若须指明对 $G$ 的依赖，也记为 $1_G$。

注意，特征标是 $G$ 上的函数，而特征标在 $k[G]$ 的元素上的值由它在 $G$ 上的值决定（从 $G$ 到 $k[G]$ 的扩张按 $k$-线性进行）。

若 $E$ 与 $F$ 之间存在 $G$-同构，就说 $G$ 在空间 $E,F$ 上的两个表示 $\rho,\varphi$ **同构**。于是可见，若 $\rho,\varphi$ 是同构的表示，则它们的特征标相等。（换句话说，若 $E,F$ 是 $G$-空间且 $G$-同构，则 $\chi_E=\chi_F$。）以下所有讨论只关心表示的同构类。

<span class="original-page-anchor" id="pdf-page-677" aria-hidden="true"></span>

若 $E,F$ 是 $G$-空间，则它们的直和 $E\oplus F$ 也是 $G$-空间，$G$ 按分量作用。若 $x\oplus y\in E\oplus F$，其中 $x\in E$、$y\in F$，则 $\sigma(x\oplus y)=\sigma x\oplus\sigma y$。

类似地，张量积 $E\otimes_k F=E\otimes F$ 是 $G$-空间，$G$ 的作用由 $\sigma(x\otimes y)=\sigma x\otimes\sigma y$ 给出。

**命题 2.1.** *若 $E,F$ 是 $G$-空间，则*

$$
\chi_E+\chi_F=\chi_{E\oplus F}\qquad\text{且}\qquad\chi_E\chi_F=\chi_{E\otimes F}.
$$

*若 $\chi^\vee$ 表示 $E^\vee$ 上的对偶表示的特征标，则*

$$
\begin{aligned}
\chi^\vee(\sigma)&=\chi(\sigma^{-1})\\
&=\overline{\chi(\sigma)}\quad\text{若 }k=\mathbf C.
\end{aligned}
$$

*证明。* 第一个关系成立，是因为元素 $\sigma$ 在表示 $E\oplus F$ 中的矩阵分解成对应于 $E$ 中的表示和 $F$ 中的表示的块。至于第二个关系，若 $\{v_i\}$ 是 $E$ 的基，$\{w_j\}$ 是 $F$ 在 $k$ 上的基，则已知 $\{v_i\otimes w_j\}$ 是 $E\otimes F$ 的基。设 $(a_{i\nu})$ 是 $\sigma$ 关于所取 $E$ 的基的矩阵，$(b_{j\mu})$ 是它关于所取 $F$ 的基的矩阵。那么

$$
\begin{aligned}
\sigma(v_i\otimes w_j)&=\sigma v_i\otimes\sigma w_j=\sum_\nu a_{i\nu}v_\nu\otimes\sum_\mu b_{j\mu}w_\mu\\
&=\sum_{\nu,\mu}a_{i\nu}b_{j\mu}v_\nu\otimes w_\mu.
\end{aligned}
$$

按定义得到

$$
\chi_{E\otimes F}(\sigma)=\sum_i\sum_j a_{ii}b_{jj}=\chi_E(\sigma)\chi_F(\sigma),
$$

由此证明了关于张量积的论断。关于对偶表示的特征标的论断，由 §1 中给出的矩阵公式 ${}^tM^{-1}$ 得到。当 $k=\mathbf C$ 时所给出的复共轭值，将在后面的推论 3.2 中证明。

到目前为止，我们定义了与表示相关联的特征标。现在很自然地可以用比正整数更一般的系数构造这些特征标的线性组合。因此，所谓 $G$ 的**特征标**，是指 $G$ 上一个可写为表示的特征标的任意整数系数线性组合的函数。与表示相关联的特征标称为**有效特征标**。当然，所有这些定义都依赖于域 $k$；若须指明域 $k$，就在表述中加上“**在 $k$ 上**”。

<span class="original-page-anchor" id="pdf-page-678" aria-hidden="true"></span>

由命题 2.1 可见，特征标组成一个环。在我们的大部分工作中，只需要加法结构，不需要乘法结构。

$G$ 的**单特征标**或**不可约特征标**，是指单表示的特征标（即与单 $k[G]$-模相关联的特征标）。

考虑定理 1.2，以及前一章关于半单环上单模和半单模结构的结果（第十七章 §4），得到：

**定理 2.2.** *$G$（在 $k$ 上）只有有限多个单特征标。$G$ 的表示的特征标恰为单特征标的非负整数系数线性组合。*

我们将使用半单环的直积分解。有

$$
k[G]=\prod_{i=1}^s R_i,
$$

其中每个 $R_i$ 都是单环，且 $k[G]$ 的单位元有相应的分解：

$$
1=e_1+\cdots+e_s,
$$

其中 $e_i$ 是 $R_i$ 的单位元，且当 $i\ne j$ 时 $e_ie_j=0$。此外，当 $i\ne j$ 时 $R_iR_j=0$。*注意 $s=s(k)$ 依赖于 $k$。*

若 $L_i$ 表示 $R_i$ 的一个代表性的单模（比如某个单左理想），就令 $\chi_i$ 为 $L_i$ 上的表示的特征标。

*注意当 $i\ne j$ 时，对所有 $\alpha\in R_j$ 都有 $\chi_i(\alpha)=0$。这是一个基本的正交关系，虽然显然，但我们其他所有关系都将由它推出。*

**定理 2.3.** *假设 $k$ 的特征为 $0$。那么每个有效特征标都有唯一的线性组合表达式*

$$
\chi=\sum_{i=1}^s n_i\chi_i,\qquad n_i\in\mathbf Z,\ n_i\ge0,
$$

*其中 $\chi_1,\ldots,\chi_s$ 是 $G$ 在 $k$ 上的单特征标。两个表示同构，当且仅当它们相关联的特征标相等。*

<span class="original-page-anchor" id="pdf-page-679" aria-hidden="true"></span>

*证明。* 设 $E$ 是 $\chi$ 的表示空间。由第十七章定理 4.4，

$$
E\approx\bigoplus_{i=1}^s n_iL_i.
$$

这个和是有限的，因为我们始终假设 $E$ 有限维。由于 $e_i$ 在 $L_i$ 上作为单位元作用，得到

$$
\chi_i(e_i)=\dim_k L_i.
$$

已经知道，当 $i\ne j$ 时 $\chi_i(e_j)=0$。所以

$$
\chi(e_i)=n_i\dim_k L_i.
$$

由于 $\dim_k L_i$ 只依赖于群代数的结构，我们已经恢复了重数 $n_1,\ldots,n_s$。具体说，$n_i$ 是 $L_i$ 在 $\chi$ 的表示空间中出现的次数（相差同构视为相同），等于 $\chi(e_i)$ 的值除以 $\dim_k L_i$（我们处于特征 $0$）。这就证明了定理。

按定义，定理 2.3 中的 $n_i$ 称为 $\chi_i$ 在 $\chi$ 中的**重数**。

以下两个推论中，仍假设 $k$ 的特征为 $0$。

**推论 2.4.** *作为从 $G$ 到 $k$ 的函数，单特征标*

$$
\chi_1,\ldots,\chi_s
$$

*在 $k$ 上线性无关。*

*证明。* 假设 $\sum a_i\chi_i=0$，其中 $a_i\in k$。把该式作用于 $e_j$，得到

$$
0=\left(\sum a_i\chi_i\right)(e_j)=a_j\dim_k L_j.
$$

因此对所有 $j$ 都有 $a_j=0$。

*在特征 $0$ 时*，把有效特征标的**维数**定义为相关联的表示空间的维数。

**推论 2.5.** *函数 $\dim$ 是从有效特征标的幺半群到 $\mathbf Z$ 的同态。*

<span class="original-page-anchor" id="pdf-page-680" aria-hidden="true"></span>

**例。** 设 $G$ 是阶等于素数 $p$ 的循环群。构造群代数 $\mathbf Q[G]$。设 $\sigma$ 是 $G$ 的一个生成元。令

$$
e_1=\frac{1+\sigma+\sigma^2+\cdots+\sigma^{p-1}}p,\qquad e_2=1-e_1.
$$

那么对任意 $\tau\in G$ 都有 $\tau e_1=e_1$，因此 $e_1^2=e_1$。继而有 $e_2^2=e_2$ 和 $e_1e_2=0$。域 $\mathbf Qe_1$ 同构于 $\mathbf Q$。令 $\omega=\sigma e_2$。则 $\omega^p=e_2$。令 $\mathbf Q_2=\mathbf Qe_2$。由于 $\omega\ne e_2$，且满足 $\mathbf Q_2$ 上的不可约方程

$$
X^{p-1}+\cdots+1=0,
$$

可知 $\mathbf Q_2(\omega)$ 同构于在有理数域中添加一个本原 $p$ 次单位根得到的域。因此 $\mathbf Q[G]$ 容许直积分解

$$
\mathbf Q[G]\approx\mathbf Q\times\mathbf Q(\zeta),
$$

其中 $\zeta$ 是本原 $p$ 次单位根。

作为另一个例子，设 $G$ 是任意有限群，并令

$$
e_1=\frac1n\sum_{\sigma\in G}\sigma.
$$

那么对任意 $\tau\in G$ 有 $\tau e_1=e_1$，且 $e_1^2=e_1$。若令 $e'_1=1-e_1$，则 $e_1'^2=e'_1$，且 $e'_1e_1=e_1e'_1=0$。所以对任意域 $k$（按现行约定，其特征不整除 $G$ 的阶），有直积分解

$$
k[G]=ke_1\times k[G]e'_1.
$$

特别地，$G$ 在群代数 $k[G]$ 本身上的表示，在分量 $ke_1$ 上包含一个一维表示，其特征标是平凡特征标。

## §3. 一维表示

约定稍微扩展术语的用法，即使在特征 $p>0$ 时，若一个特征标是同态 $G\to k^*$，也说**该特征标是一维的**。

假设 $E$ 是 $k$ 上的一维向量空间。设

$$
\rho:G\longrightarrow\operatorname{Aut}_k(E)
$$

是一个表示。设 $\{v\}$ 是 $E$ 在 $k$ 上的一组基。那么对每个 $\sigma\in G$ 有

$$
\sigma v=\chi(\sigma)v,
$$

<span class="original-page-anchor" id="pdf-page-681" aria-hidden="true"></span>

其中 $\chi(\sigma)\in k$，且因为 $\sigma$ 诱导 $E$ 的自同构，所以 $\chi(\sigma)\ne0$。于是对 $\tau\in G$ 有

$$
\tau\sigma v=\chi(\sigma)\tau v=\chi(\sigma)\chi(\tau)v=\chi(\sigma\tau)v.
$$

可见 $\chi:G\to k^*$ 是同态，我们的一维特征标与伽罗瓦理论中的阿廷定理里出现的对象属于同一类型。

反过来，设 $\chi:G\to k^*$ 是同态。令 $E$ 是一维 $k$-空间，基为 $\{v\}$，并对所有 $a\in k$ 定义 $\sigma(av)=a\chi(\sigma)v$。立即可见，$G$ 在 $E$ 上的这个作用给出 $G$ 的表示，其相关联的特征标为 $\chi$。

因为 $G$ 有限，注意

$$
\chi(\sigma)^n=\chi(\sigma^n)=\chi(1)=1.
$$

因此一维特征标的值都是 $n$ 次单位根。一维特征标在乘法下组成一个群；当 $G$ 是有限阿贝尔群时，我们已在第一章 §9 中确定了它的一维特征标群。

**定理 3.1.** *设 $G$ 是有限阿贝尔群，并假设 $k$ 代数闭。那么 $G$ 的每个单表示都是一维的。$G$ 的单特征标就是从 $G$ 到 $k^*$ 的同态。*

*证明。* 群环 $k[G]$ 半单、交换，且是单环的直积。每个单环都是 $k$ 上的矩阵环（由第十七章推论 3.6），而它交换当且仅当它等于 $k$。

对 $G$ 的每个一维特征标 $\chi$ 有

$$
\chi(\sigma)^{-1}=\chi(\sigma^{-1}).
$$

若 $k$ 是复数域，则

$$
\overline{\chi(\sigma)}=\chi(\sigma)^{-1}=\chi(\sigma^{-1}).
$$

**推论 3.2.** *设 $k$ 代数闭，$G$ 是有限群。对任意特征标 $\chi$ 和 $\sigma\in G$，值 $\chi(\sigma)$ 等于单位根的整数系数和（即根据 $k$ 的特征，系数属于 $\mathbf Z$ 或 $\mathbf Z/p\mathbf Z$）。*

*证明。* 设 $H$ 是由 $\sigma$ 生成的子群。那么 $H$ 是循环子群。特征标为 $\chi$ 的 $G$ 的表示，限制后可以看作 $H$ 的表示，具有同一特征标。因此论断由定理 3.1 得到。

<span class="original-page-anchor" id="pdf-page-682" aria-hidden="true"></span>

## §4. 类函数空间

所谓 $G$ 的**类函数**（在 $k$ 上，或取值于 $k$），是指函数 $f:G\to k$，它对所有 $\sigma,\tau\in G$ 满足 $f(\sigma\tau\sigma^{-1})=f(\tau)$。显然，特征标是类函数，因为对方阵 $M,M'$ 有

$$
\operatorname{tr}(MM'M^{-1})=\operatorname{tr}(M').
$$

所以类函数可以看作共轭类上的函数。

我们总按线性把类函数的定义域扩张到群环。若

$$
\alpha=\sum_{\sigma\in G}a_\sigma\sigma,
$$

且 $f$ 是类函数，就定义

$$
f(\alpha)=\sum_{\sigma\in G}a_\sigma f(\sigma).
$$

设 $\sigma_0\in G$。若 $\sigma\in G$ 与 $\sigma_0$ 共轭，即存在元素 $\tau$ 使 $\sigma_0=\tau\sigma\tau^{-1}$，就写 $\sigma\sim\sigma_0$。形如

$$
\gamma=\sum_{\sigma\sim\sigma_0}\sigma
$$

的群环元素也称为**共轭类**。

**命题 4.1.** *$k[G]$ 的一个元素与 $G$ 的每个元素交换，当且仅当它是共轭类的 $k$-系数线性组合。*

*证明。* 设 $\alpha=\sum a_\sigma\sigma$，并假设对所有 $\tau\in G$ 都有 $\alpha\tau=\tau\alpha$。那么

$$
\sum_{\sigma\in G}a_\sigma\tau\sigma\tau^{-1}=\sum_{\sigma\in G}a_\sigma\sigma.
$$

所以只要 $\sigma$ 与 $\sigma_0$ 共轭，就有 $a_{\sigma_0}=a_\sigma$，这意味着可以写成

$$
\alpha=\sum_\gamma a_\gamma\gamma,
$$

其中和遍历所有共轭类 $\gamma$。

**注。** 注意共轭类实际上构成 $\mathbf Z[G]$ 的中心在 $\mathbf Z$ 上的一组基，因而在表示理论中起普遍的作用。

注意，共轭类在 $k$ 上线性无关，并构成 $k[G]$ 的中心在 $k$ 上的一组基。

<span class="original-page-anchor" id="pdf-page-683" aria-hidden="true"></span>

*在本节其余部分，假设 $k$ 代数闭。* 那么

$$
k[G]=\prod_{i=1}^s R_i
$$

是单环的直积，且每个 $R_i$ 是 $k$ 上的矩阵代数。在直积中，中心显然是各因子的中心的积。用 $k_i$ 表示 $k$ 在 $R_i$ 中的像，换句话说，

$$
k_i=ke_i,
$$

其中 $e_i$ 是 $R_i$ 的单位元。那么 $k[G]$ 的中心也等于

$$
\prod_{i=1}^s k_i,
$$

它在 $k$ 上为 $s$ 维。

若 $L_i$ 是 $R_i$ 的一个代表性的单左理想，则

$$
R_i\approx\operatorname{End}_k(L_i).
$$

令

$$
d_i=\dim_k L_i.
$$

那么

$$
\boxed{d_i^2=\dim_k R_i\quad\text{且}\quad\sum_{i=1}^s d_i^2=n.}
$$

作为 $(G,k)$-空间，还有直和分解

$$
R_i\approx L_i^{(d_i)}.
$$

从现在起固定使用上述记号。

可以把部分结果归纳如下。

**命题 4.2.** *设 $k$ 代数闭。那么 $G$ 的共轭类数等于 $G$ 的单特征标数，两者都等于上述数 $s$。共轭类 $\gamma_1,\ldots,\gamma_s$ 和单位元 $e_1,\ldots,e_s$ 分别构成 $k[G]$ 的中心的基。*

用 $h_i$ 表示 $\gamma_i$ 中的元素数。用 $h_\gamma$ 表示共轭类 $\gamma$ 中的元素数，称之为**类数**。群代数的中心记为 $Z_k(G)$。

<span class="original-page-anchor" id="pdf-page-684" aria-hidden="true"></span>

可以把 $k[G]$ 看作一个 $G$-模。它的特征标称为**正则特征标**，记为 $\chi_{\mathrm{reg}}$；若须指明对 $G$ 的依赖，则记为 $r_G$。$k[G]$ 上的表示称为**正则表示**。由 $k[G]$ 的直和分解得到

$$
\boxed{\chi_{\mathrm{reg}}=\sum_{i=1}^s d_i\chi_i.}
$$

我们来确定正则特征标的值。

**命题 4.3.** *设 $\chi_{\mathrm{reg}}$ 是正则特征标。那么*

$$
\chi_{\mathrm{reg}}(\sigma)=0\quad\text{若 }\sigma\in G,\ \sigma\ne1,
$$

$$
\chi_{\mathrm{reg}}(1)=n.
$$

*证明。* 设 $1=\sigma_1,\ldots,\sigma_n$ 是 $G$ 的元素。它们构成 $k[G]$ 在 $k$ 上的一组基。$1$ 的矩阵是 $n\times n$ 单位矩阵，因此第二个论断成立。若 $\sigma\ne1$，则乘以 $\sigma$ 置换了 $\sigma_1,\ldots,\sigma_n$，而且立即可见，表示 $\sigma$ 的矩阵的所有对角元都是 $0$。这就证明了所需的结论。

注意群环的中心 $Z_k(G)$ 有两组自然的基：第一组是 $G$ 的元素的共轭类；第二组是元素 $e_1,\ldots,e_s$（即环 $R_i$ 的单位元）。我们要找出两者之间的关系，换句话说，要找出把 $e_i$ 用群元素表达时的系数。下一个命题完成这一点。这些系数的值将在下一节解释为标量积，从而澄清它们看似神秘的出现方式。

**命题 4.4.** *再次假设 $k$ 代数闭。设*

$$
e_i=\sum_{\tau\in G}a_\tau\tau,\qquad a_\tau\in k.
$$

*那么*

$$
a_\tau=\frac1n\chi_{\mathrm{reg}}(e_i\tau^{-1})=\frac{d_i}n\chi_i(\tau^{-1}).
$$

*证明。* 对所有 $\tau\in G$ 有

$$
\chi_{\mathrm{reg}}(e_i\tau^{-1})=\chi_{\mathrm{reg}}\left(\sum_{\sigma\in G}a_\sigma\sigma\tau^{-1}\right)=\sum_{\sigma\in G}a_\sigma\chi_{\mathrm{reg}}(\sigma\tau^{-1}).
$$

<span class="original-page-anchor" id="pdf-page-685" aria-hidden="true"></span>

由命题 4.3 得到

$$
\chi_{\mathrm{reg}}(e_i\tau^{-1})=na_\tau.
$$

另一方面，

$$
\chi_{\mathrm{reg}}(e_i\tau^{-1})=\sum_{j=1}^s d_j\chi_j(e_i\tau^{-1})=d_i\chi_i(e_i\tau^{-1})=d_i\chi_i(\tau^{-1}).
$$

所以对所有 $\tau\in G$ 有

$$
d_i\chi_i(\tau^{-1})=na_\tau.
$$

这就证明了命题。

**推论 4.5.** *若 $m$ 是 $G$ 的一个指数，则每个 $e_i$ 都能用群元素表达，其系数属于在素域上由 $m$ 次单位根生成的域。*

**推论 4.6.** *维数 $d_i$ 不被 $k$ 的特征整除。*

*证明。* 否则 $e_i=0$，这是不可能的。

**推论 4.7.** *单特征标 $\chi_1,\ldots,\chi_s$ 在 $k$ 上线性无关。*

*证明。* 推论 2.4 中的证明适用，因为现在知道特征不整除 $d_i$。

**推论 4.8.** *再假设 $k$ 的特征为 $0$。那么对每个 $i$ 都有 $d_i\mid n$。*

*证明。* 把 $e_i$ 的表达式乘以 $n/d_i$，再乘以 $e_i$，得到

$$
\frac n{d_i}e_i=\sum_{\sigma\in G}\chi_i(\sigma^{-1})\sigma e_i.
$$

设 $\zeta$ 是本原 $m$ 次单位根，$M$ 是由有限多个元素 $\zeta^\nu\sigma e_i$（$\nu=0,\ldots,m-1$ 且 $\sigma\in G$）生成的 $\mathbf Z$-模。由前面的关系立即可见，乘以 $n/d_i$ 把 $M$ 映入自身。按定义，可知 $n/d_i$ 在 $\mathbf Z$ 上整，因而属于 $\mathbf Z$，这正是所要的结论。

**定理 4.9.** *设 $k$ 代数闭。设 $Z_k(G)$ 是 $k[G]$ 的中心，$X_k(G)$ 是 $G$ 上的类函数的 $k$-空间。那么在配对*

$$
(f,\alpha)\longmapsto f(\alpha)
$$

*下，$Z_k(G)$ 和 $X_k(G)$ 互为对偶空间。*

<span class="original-page-anchor" id="pdf-page-686" aria-hidden="true"></span>

*单特征标与单位元 $e_1,\ldots,e_s$ 构成彼此正交的基。有*

$$
\chi_i(e_j)=\delta_{ij}d_i.
$$

*证明。* 该公式已在定理 2.3 的证明中证出。这里涉及的两个空间都具有维数 $s$，且在 $k$ 中 $d_i\ne0$。于是命题显然成立。

## §5. 正交关系

***本节始终假设 $k$ 代数闭。***

若 $R$ 是 $k$ 的子环，就用 $X_R(G)$ 表示由 $G$ 的特征标在 $R$ 上生成的 $R$-模。因此它是由单特征标的 $R$-系数线性组合构成的函数模。若 $R$ 是素环（即整数环 $\mathbf Z$，或当 $k$ 的特征为 $p$ 时的模 $p$ 整数环），就把 $X_R(G)$ 记为 $X(G)$。

现在定义 $X(G)\times X(G)$ 上的双线性映射。若 $f,g\in X(G)$，定义

$$
\langle f,g\rangle=\frac1n\sum_{\sigma\in G}f(\sigma)g(\sigma^{-1}).
$$

**定理 5.1.** *当 $f,g\in X(G)$ 时，符号 $\langle f,g\rangle$ 的值属于素环。单特征标构成 $X(G)$ 的标准正交基，换句话说，*

$$
\langle\chi_i,\chi_j\rangle=\delta_{ij}.
$$

*对每个环 $R\subset k$，该符号唯一地扩张为 $R$-双线性形式 $X_R(G)\times X_R(G)\to R$，由上面同一公式给出。*

*证明。* 由命题 4.4 得到

$$
\chi_j(e_i)=\frac{d_i}n\sum_{\sigma\in G}\chi_i(\sigma^{-1})\chi_j(\sigma).
$$

若 $i\ne j$，左边是 $0$，故 $\chi_i$ 与 $\chi_j$ 正交。若 $i=j$，左边是 $d_i$，而由推论 4.6 知在 $k$ 中 $d_i\ne0$。所以 $\langle\chi_i,\chi_i\rangle=1$。由于 $X(G)$ 的每个元素都是单特征标的整数系数线性组合，可知该双线性映射的值属于素环。关于扩张的论断显然，从而定理得证。

<span class="original-page-anchor" id="pdf-page-687" aria-hidden="true"></span>

假设 $k$ 的特征为 $0$。设 $m$ 是 $G$ 的一个指数，且 $R$ 包含 $m$ 次单位根。若 $R$ 有一个阶为 $2$ 的自同构，它在单位根上的作用是 $\zeta\mapsto\zeta^{-1}$，就称这种自同构为**共轭**，记为 $a\mapsto\bar a$。

**定理 5.2.** *设 $k$ 的特征为 $0$，$R$ 是包含 $m$ 次单位根且具有共轭的子环。那么 $X(G)$ 上的双线性形式唯一地扩张为一个厄米形式*

$$
X_R(G)\times X_R(G)\longrightarrow R,
$$

*由公式*

$$
\langle f,g\rangle=\frac1n\sum_{\sigma\in G}f(\sigma)\overline{g(\sigma)}
$$

*给出。单特征标关于此形式构成 $X_R(G)$ 的标准正交基。*

*证明。* 当 $f,g$ 属于 $X(G)$ 时，定理陈述中的公式对符号 $\langle f,g\rangle$ 给出与先前相同的值。因此扩张存在，而且显然唯一。

回到 $k$ 具有任意特征的情形。

用 $Z(G)$ 表示在素环上由共轭类 $\gamma_1,\ldots,\gamma_s$ 生成的加法群。它的维数为 $s$。我们定义 $Z(G)\times Z(G)$ 上的双线性映射。若 $\alpha=\sum a_\sigma\sigma$ 的系数属于素环，就用 $\alpha^-$ 表示元素 $\sum a_\sigma\sigma^{-1}$。

**命题 5.3.** *对 $\alpha,\beta\in Z(G)$，可以用以下两个相等的表达式中的任一个定义符号 $\langle\alpha,\beta\rangle$：*

$$
\langle\alpha,\beta\rangle=\frac1n\chi_{\mathrm{reg}}(\alpha\beta^-)=\frac1n\sum_{\nu=1}^s\chi_\nu(\alpha)\chi_\nu(\beta^-).
$$

*该符号的值属于素环。*

*证明。* 每个表达式对第一和第二个变量都线性。因此要证明它们相等，只须在把 $\alpha$ 换成 $e_i$、$\beta$ 换成 $G$ 的一个元素 $\tau$ 时证明两个表达式相等。但这时所需的等式等价于

$$
\chi_{\mathrm{reg}}(e_i\tau^{-1})=\sum_{\nu=1}^s\chi_\nu(e_i)\chi_\nu(\tau^{-1}).
$$

除非 $\nu=i$，否则 $\chi_\nu(e_i)=0$，所以最后这个关系的右边等于 $d_i\chi_i(\tau^{-1})$。由命题 4.4 可知两个表达式相等。

<span class="original-page-anchor" id="pdf-page-688" aria-hidden="true"></span>

由命题 4.3 可知这些值属于素环：正则特征标在群元素上的值等于 $0$ 或 $n$，因此在特征 $0$ 时，是可被 $n$ 整除的整数。

与 $X_R(G)$ 类似，用记号 $Z_R(G)$ 表示在 $k$ 的任意子环 $R$ 上由 $\gamma_1,\ldots,\gamma_s$ 生成的 $R$-模。

**引理 5.4.** *对每个包含于 $k$ 的环 $R$，命题 5.3 的配对唯一地扩张为映射*

$$
Z_R(G)\times Z(G)\longrightarrow R,
$$

*它对第一个变量 $R$-线性。若 $R$ 包含 $m$ 次单位根，其中 $m$ 是 $G$ 的一个指数，并且也包含 $1/n$，则对所有 $i$ 都有 $e_i\in Z_R(G)$。类数 $h_i$ 不被 $k$ 的特征整除，且有*

$$
e_i=\sum_{\nu=1}^s\langle e_i,\gamma_\nu\rangle\frac1{h_\nu}\gamma_\nu.
$$

*证明。* 注意 $h_i$ 不被特征整除，因为它是 $G$ 的一个子群的指数（当 $G$ 以共轭作用时，$\gamma_i$ 中一个元素的迷向群），所以 $h_i$ 整除 $n$。所述配对的扩张显然，因为 $\gamma_1,\ldots,\gamma_s$ 构成 $Z(G)$ 在素环上的一组基。把 $e_i$ 用这组基表达，只是用当前配对重新解释命题 4.4。

设 $E$ 是 $k$ 的子环 $R$ 上的自由模，并假设 $E$ 上有一个对称双线性形式（或厄米形式）。设 $\{v_1,\ldots,v_s\}$ 是这个模的正交基。若

$$
v=a_1v_1+\cdots+a_sv_s,
$$

其中 $a_i\in R$，则称 $a_1,\ldots,a_s$ 为 $v$ 关于这组基的**傅里叶系数**。用该形式表示，这些系数为

$$
a_i=\frac{\langle v,v_i\rangle}{\langle v_i,v_i\rangle},
$$

条件是 $\langle v_i,v_i\rangle\ne0$。

将在下一个定理中看到，$e_i$ 用 $\gamma_1,\ldots,\gamma_s$ 表出的式子是傅里叶展开。

**定理 5.5.** *共轭类 $\gamma_1,\ldots,\gamma_s$ 构成 $Z(G)$ 的正交基。有 $\langle\gamma_i,\gamma_i\rangle=h_i$。对每个包含于 $k$ 的环 $R$，命题 5.3 的双线性映射唯一地扩张为 $R$-双线性映射*

$$
Z_R(G)\times Z_R(G)\longrightarrow R.
$$

<span class="original-page-anchor" id="pdf-page-689" aria-hidden="true"></span>

*证明。* 使用引理。由线性，在把 $R$ 换成 $k$，并把 $e_i$ 换成 $Z_k(G)$ 的任意元素时，引理中的公式仍成立，特别是把 $e_i$ 换成 $\gamma_i$ 时。但 $\{\gamma_1,\ldots,\gamma_s\}$ 是 $Z_k(G)$ 在 $k$ 上的一组基。因此得到 $\langle\gamma_i,\gamma_i\rangle=h_i$，且当 $i\ne j$ 时 $\langle\gamma_i,\gamma_j\rangle=0$，这就是所要证明的。

**推论 5.6.** *若 $G$ 交换，则*

$$
\frac1n\sum_{\nu=1}^n\chi_\nu(\sigma)\chi_\nu(\tau^{-1})=\begin{cases}0&\text{若 }\sigma\ne\tau,\\1&\text{若 }\sigma=\tau.\end{cases}
$$

*证明。* 当 $G$ 交换时，每个共轭类恰有一个元素，且单特征标数等于群的阶。

如同对 $X(G)$ 所做的那样，现在对 $Z(G)$ 考虑特征 $0$ 的情形。设 $k$ 的特征为 $0$，$R$ 是包含 $m$ 次单位根且具有共轭的 $k$ 的子环。设 $\alpha=\sum_{\sigma\in G}a_\sigma\sigma$，其中 $a_\sigma\in R$。定义

$$
\bar\alpha=\sum_{\sigma\in G}\bar a_\sigma\sigma^{-1}.
$$

**定理 5.7.** *设 $k$ 的特征为 $0$，$R$ 是 $k$ 的子环，包含 $m$ 次单位根且具有共轭。那么命题 5.3 的配对唯一地扩张为厄米形式*

$$
Z_R(G)\times Z_R(G)\longrightarrow R,
$$

*由公式*

$$
\langle\alpha,\beta\rangle=\frac1n\chi_{\mathrm{reg}}(\alpha\bar\beta)=\frac1n\sum_{\nu=1}^s\chi_\nu(\alpha)\overline{\chi_\nu(\beta)}
$$

*给出。共轭类 $\gamma_1,\ldots,\gamma_s$ 构成 $Z_R(G)$ 的正交基。若 $R$ 包含 $1/n$，则 $e_1,\ldots,e_s$ 属于 $Z_R(G)$，且也构成 $Z_R(G)$ 的正交基。有 $\langle e_i,e_i\rangle=d_i^2/n$。*

*证明。* 当 $\alpha,\beta$ 属于 $Z(G)$ 时，定理陈述中的公式与命题 5.3 的符号 $\langle\alpha,\beta\rangle$ 具有相同的值。所以扩张存在，而且显然唯一。使用命题 5.3 中定义标量积的第二个公式，并回忆当 $\nu\ne i$ 时 $\chi_\nu(e_i)=0$，可见

$$
\langle e_i,e_i\rangle=\frac1n\chi_i(e_i)\overline{\chi_i(e_i)},
$$

由此得到论断。

<span class="original-page-anchor" id="pdf-page-690" aria-hidden="true"></span>

注意，$e_i$ 关于基 $\gamma_1,\ldots,\gamma_s$ 的傅里叶系数，不论使用定理 5.5 的双线性形式还是定理 5.7 的厄米形式，都是相同的。这是因为 $\gamma_1,\ldots,\gamma_s$ 属于 $Z(G)$，且构成 $Z(G)$ 在素环上的一组基。

现在用另一种方法重新证明并推广正交关系。设 $E$ 是有限维 $(G,k)$-空间，因此有表示

$$
G\longrightarrow\operatorname{Aut}_k(E).
$$

选取 $E$ 的一组基后，得到 $G$ 的一个由 $d\times d$ 矩阵组成的表示。若 $\{v_1,\ldots,v_d\}$ 是这组基，则有对偶基 $\{\lambda_1,\ldots,\lambda_d\}$，满足 $\lambda_i(v_j)=\delta_{ij}$。若 $G$ 的元素 $\sigma$ 由矩阵 $(\rho_{ij}(\sigma))$ 表示，则每个系数 $\rho_{ij}(\sigma)$ 是 $\sigma$ 的函数，称为 **$ij$-系数函数**。也可以写成

$$
\rho_{ij}(\sigma)=\lambda_j(\sigma v_i).
$$

不过，可以不对基或对偶基中的元素编号，而使用 $E$ 上的任意泛函 $\lambda$ 和任意向量 $v$。于是得到函数

$$
\sigma\longmapsto\lambda(\sigma v)=\rho_{\lambda,v}(\sigma),
$$

它也称为**系数函数**。实际上，总可以把 $v=v_1$ 补成一组基，使 $\lambda=\lambda_1$ 是对偶基的第一个元素；不过，使用记号 $\rho_{\lambda,v}$ 在许多方面更为优雅。

**译校注：** 原文印作“one can always complete $v=v_1$ to a basis such that $\lambda=\lambda_1$”。对于前句所说的任意 $v$ 和 $\lambda$，这需要附加条件 $\lambda(v)=1$，因为对偶基必须满足 $\lambda_1(v_1)=1$。满足此条件时，以 $v$ 和 $\operatorname{Ker}\lambda$ 的一组基组成所需的基即可；系数函数的定义本身无需此条件。

我们将不断使用：

**舒尔引理。** *设 $E,F$ 是单 $(G,k)$-空间，设*

$$
\varphi:E\longrightarrow F
$$

*是同态。那么或者 $\varphi=0$，或者 $\varphi$ 是同构。*

*证明。* 确实，$\varphi$ 的核和像都是子空间，所以论断显然。

用与先前相同的公式在 $G$ 上的所有 $k$-值函数的空间上定义标量积，即

$$
\langle f,g\rangle=\frac1n\sum_{\sigma\in G}f(\sigma)g(\sigma^{-1}).
$$

我们将导出系数函数之间的各种正交关系。

**定理 5.8.** *设 $E,F$ 是单 $(G,k)$-空间。设 $\lambda$ 是 $E$ 上的 $k$-线性泛函，$x\in E$、$y\in F$。若 $E,F$ 不同构，则*

$$
\sum_{\sigma\in G}\lambda(\sigma x)\sigma^{-1}y=0.
$$

<span class="original-page-anchor" id="pdf-page-691" aria-hidden="true"></span>

*若 $\mu$ 是 $F$ 上的泛函，则系数函数 $\rho_{\lambda,x}$ 与 $\rho_{\mu,y}$ 正交，即*

$$
\sum_{\sigma\in G}\lambda(\sigma x)\mu(\sigma^{-1}y)=0.
$$

*证明。* 映射 $x\mapsto\sum\lambda(\sigma x)\sigma^{-1}y$ 是从 $E$ 到 $F$ 的 $G$-同态，所以舒尔引理完成了第一个论断的证明。作用泛函 $\mu$ 就得到第二个论断。

作为推论可见，若 $\chi,\psi$ 是 $G$ 在 $k$ 上两个不同的不可约特征标，则

$$
\langle\chi,\psi\rangle=0,
$$

即这些特征标正交。确实，与表示 $\rho$ 相关联的特征标是对角系数函数之和，

$$
\chi=\sum_{i=1}^d\rho_{ii},
$$

其中 $d$ 是表示的维数。两个不同的特征标对应不同构的表示，所以可以应用命题 5.8。

**引理 5.9.** *设 $E$ 是单 $(G,k)$-空间。那么 $E$ 的任意 $G$-自同态等于恒等映射的一个标量倍数。*

*证明。* 由舒尔引理，代数 $\operatorname{End}_{G,k}(E)$ 是除法代数，且在 $k$ 上有限维。由于假设 $k$ 代数闭，它必等于 $k$，因为任意元素在 $k$ 上生成一个交换子域。这就证明了引理。

**引理 5.10.** *设 $E$ 是 $G$ 的一个维数为 $d$ 的表示空间。设 $\lambda$ 是 $E$ 上的泛函，$x\in E$。设 $\varphi_{\lambda,x}\in\operatorname{End}_k(E)$ 是满足*

$$
\varphi_{\lambda,x}(y)=\lambda(y)x
$$

*的自同态。那么 $\operatorname{tr}(\varphi_{\lambda,x})=\lambda(x)$。*

*证明。* 若 $x=0$，论断显然。设 $x\ne0$。若 $\lambda(x)\ne0$，选取 $E$ 的一组基，由 $x$ 和 $\lambda$ 的核的一组基组成。若 $\lambda(x)=0$，选取 $E$ 的一组基，由 $\lambda$ 的核的一组基和另一个元素组成。在两种情形下，由表示 $\varphi_{\lambda,x}$ 的相应矩阵都立即可见，迹由引理所述公式给出。

**定理 5.11.** *设 $\rho:G\to\operatorname{Aut}_k(E)$ 是 $G$ 的一个维数为 $d$ 的单表示。那么 $k$ 的特征不整除 $d$。设 $x,y\in E$。则对 $E$ 上任意泛函 $\lambda,\mu$ 有*

$$
\sum_{\sigma\in G}\lambda(\sigma x)\mu(\sigma^{-1}y)=\frac nd\lambda(y)\mu(x).
$$

<span class="original-page-anchor" id="pdf-page-692" aria-hidden="true"></span>

*证明。* 只须证明

$$
\sum_{\sigma\in G}\lambda(\sigma x)\sigma^{-1}y=\frac nd\lambda(y)x.
$$

固定 $y$ 后，立即可验证映射

$$
x\longmapsto\sum_{\sigma\in G}\lambda(\sigma x)\sigma^{-1}y
$$

是 $E$ 的 $G$-自同态，因此由引理 5.9，它等于某个 $c\in k$ 所给出的 $cI$。实际上，它等于

$$
\sum_{\sigma\in G}\rho(\sigma^{-1})\circ\varphi_{\lambda,y}\circ\rho(\sigma).
$$

由引理 5.10，该表达式的迹等于 $n\cdot\operatorname{tr}(\varphi_{\lambda,y})$，同时也等于 $dc$。取 $\lambda,y$ 使 $\lambda(y)=1$，表明特征不整除 $d$，然后就能按定理所述解出 $c$。

**推论 5.12.** *设 $\chi$ 是 $G$ 在单空间 $E$ 上的表示的特征标。那么*

$$
\langle\chi,\chi\rangle=1.
$$

*证明。* 这直接由定理和 $\chi$ 的表达式

$$
\chi=\rho_{11}+\cdots+\rho_{dd}
$$

得到。

现在重新得到了单表示的特征标标准正交这一事实。于是可以重新得到群环中的幂等元：即若 $\chi_1,\ldots,\chi_s$ 是单特征标，现在可以定义

$$
e_i=\frac{d_i}n\sum_{\sigma\in G}\chi_i(\sigma)\sigma^{-1}.
$$

特征标的标准正交性给出公式：

**推论 5.13.** $\chi_i(e_j)=\delta_{ij}d_i$，*且* $\chi_{\mathrm{reg}}=\sum_{i=1}^s d_i\chi_i$。

*证明。* 第一个公式直接应用特征标的标准正交性得到。有关正则特征标的第二个公式，通过写成

$$
\chi_{\mathrm{reg}}=\sum_j m_j\chi_j
$$

<span class="original-page-anchor" id="pdf-page-693" aria-hidden="true"></span>

其中系数未知。我们知道 $\chi_{\mathrm{reg}}(1)=n$，且当 $\sigma\ne1$ 时有 $\chi_{\mathrm{reg}}(\sigma)=0$。对 $i=1,\ldots,s$ 取 $\chi_{\mathrm{reg}}$ 与 $\chi_i$ 的标量积，立即得到系数 $m_j$ 所需的值。

由于特征标是类函数，直接可见每个 $e_i$ 都是共轭类的线性组合，因而属于群环 $k[G]$ 的中心。

现在设 $E_i$ 是 $\chi_i$ 的表示空间，$\rho_i$ 是 $G$ 或 $k[G]$ 在 $E_i$ 上的表示。对 $\alpha\in k[G]$，令 $\rho_i(\alpha):E_i\to E_i$ 是对所有 $x\in E_i$ 满足 $\rho_i(\alpha)x=\alpha x$ 的映射。

**命题 5.14.** *有*

$$
\rho_i(e_i)=\operatorname{id}\quad\text{且}\quad\rho_i(e_j)=0\quad\text{若 }i\ne j.
$$

*证明。* 由于 $e_i$ 属于 $k[G]$ 的中心，映射 $x\mapsto e_ix$ 是 $E_i$ 到自身的 $G$-同态。因此由引理 5.9，这个同态是恒等映射的标量倍数。取迹并使用单特征标之间的正交关系，立即得到该标量所需的值。

现在得到

$$
\sum_{i=1}^s e_i=1,
$$

因为群环 $k[G]$ 是单空间的直和，可能带有重数，并且忠实地作用于自身。

标准正交关系还容许把函数展开为傅里叶表达式：若是类函数，就关于特征标展开；一般情形则关于系数函数展开。用两个定理陈述如下。

**定理 5.15.** *设 $f$ 是 $G$ 上的类函数。那么*

$$
f=\sum_{i=1}^s\langle f,\chi_i\rangle\chi_i.
$$

*证明。* 共轭类数等于不同的特征标数，而这些特征标线性无关，所以它们构成类函数的一组基。对 $f$ 与任意特征标 $\chi_j$ 取标量积，并使用标准正交性，就可见系数由所述公式给出。

**定理 5.16.** *设 $\rho^{(i)}$ 是 $G$ 在 $E_i$ 上关于所选基的矩阵表示，$\rho^{(i)}_{\nu,\mu}$ 是该矩阵的系数函数，$i=1,\ldots,s$ 且 $\nu,\mu=1,\ldots,d_i$。那么函数 $\rho^{(i)}_{\nu,\mu}$ 构成 $G$ 上所有函数空间的正交基，因此对 $G$ 上任意函数 $f$ 有*

$$
f=\sum_{i=1}^s\sum_{\nu,\mu}\frac1{d_i}\langle f,\rho^{(i)}_{\nu,\mu}\rangle\rho^{(i)}_{\nu,\mu}.
$$

**译校注：** 上述定理陈述及公式按原文保留。按本节所用双线性配对和系数定义 $\rho_{\nu,\mu}(\sigma)=\lambda_\mu(\sigma v_\nu)$，定理 5.11 给出 $\langle\rho^{(i)}_{\nu,\mu},\rho^{(j)}_{a,b}\rangle=\delta_{ij}\delta_{\mu a}\delta_{b\nu}/d_i$。所以非对角系数函数与转置指标的系数函数配对，它们一般并非相互正交。正确的双线性展开为 $f=\sum_i\sum_{\nu,\mu}d_i\langle f,\rho^{(i)}_{\mu,\nu}\rangle\rho^{(i)}_{\nu,\mu}$；原印公式同时遗漏了指标对换，并把因子 $d_i$ 印为 $1/d_i$。

<span class="original-page-anchor" id="pdf-page-694" aria-hidden="true"></span>

*证明。* 系数函数构成正交基，由定理 5.8 和 5.11 得到。$f$ 关于这组基的表达式，不过是关于任意标量积的标准傅里叶展开。这就结束了证明。

为具体起见，现在设 $k=\mathbf C$ 是复数域。回忆**有效特征标** $\chi$ 是 $X(G)$ 的元素，满足：若

$$
\chi=\sum_{i=1}^s m_i\chi_i
$$

是单特征标的整数系数线性组合，则对所有 $i$ 都有 $m_i\ge0$。由单特征标的标准正交性，对所有元素 $\chi\in X(G)$ 得到关系

$$
\|\chi\|^2=\langle\chi,\chi\rangle=\sum_{i=1}^s m_i^2\quad\text{且}\quad m_i=\langle\chi,\chi_i\rangle.
$$

由此得到下一个定理的 (a)。

**定理 5.17.** **(a)** *设 $\chi$ 是 $X(G)$ 中的有效特征标。那么 $\chi$ 在 $\mathbf C$ 上为单特征标，当且仅当 $\|\chi\|^2=1$，或者等价地，*

$$
\sum_{\sigma\in G}|\chi(\sigma)|^2=\#(G).
$$

**(b)** *设 $\chi,\psi$ 是 $X(G)$ 中的有效特征标，$E,F$ 是它们在 $\mathbf C$ 上的表示空间。那么*

$$
\langle\chi,\psi\rangle_G=\dim\operatorname{Hom}_G(E,F).
$$

*证明。* 第一部分已经证明。对于 (b)，设 $\psi=\sum q_i\chi_i$。由标准正交性得到

$$
\langle\chi,\psi\rangle_G=\sum m_iq_i.
$$

若 $E_i$ 是 $\chi_i$ 在 $\mathbf C$ 上的表示空间，则由舒尔引理

$$
\dim\operatorname{Hom}_G(E_i,E_i)=1\quad\text{且}\quad\dim\operatorname{Hom}_G(E_i,E_j)=0\quad\text{当 }i\ne j.
$$

所以 $\dim\operatorname{Hom}_G(E,F)=\sum m_iq_i$，从而证明了 (b)。

**推论 5.18.** 使用上述记号，并为简单起见取 $k=\mathbf C$，有：

**(a)** *$1_G$ 在 $E^\vee\otimes F$ 中的重数为 $\dim_k\operatorname{inv}_G(E^\vee\otimes F)$。*

**(b)** *$(G,k)$-空间 $E$ 是单的，当且仅当 $1_G$ 在 $E^\vee\otimes E$ 中的重数为 $1$。*

*证明。* 直接由定理 5.17 和 §1 的公式 (3) 得到。

**注。** 定理 5.17(a) 的判据对于检验一个表示是否为单表示很有用。实际中，表示往往由一维特征标诱导而得，这样的诱导表示确实常有不可约的倾向。我们将在 §12 中看到一个具体情形。

<span class="original-page-anchor" id="pdf-page-695" aria-hidden="true"></span>

## §6. 诱导特征标

记号与前一节相同。不过，不需要那里证明的全部结果；只需要 $X(G)$ 上的双线性配对，以及它到

$$
X_R(G)\times X_R(G)\longrightarrow R
$$

的扩张。根据定理 5.2，符号 $\langle\ ,\ \rangle$ 可以解释为双线性扩张或厄米扩张。

设 $S$ 是 $G$ 的子群。有称为限制的 $R$-线性映射

$$
\operatorname{res}_S^G:X_R(G)\longrightarrow X_R(S),
$$

它把 $G$ 上的每个类函数映为在 $S$ 上的限制。这是一个环同态。有时用 $f_S$ 表示 $f$ 在 $S$ 上的限制。

我们定义一个反方向的映射

$$
\operatorname{ind}_S^G:X_R(S)\longrightarrow X_R(G),
$$

称为**诱导映射**。若 $g\in X_R(S)$，就把 $g$ 扩张为 $G$ 上的 $g_S$，规定当 $\sigma\notin S$ 时 $g_S(\sigma)=0$。然后定义**诱导函数**

$$
g^G(\sigma)=\operatorname{ind}_S^G(g)(\sigma)=\frac1{(S:1)}\sum_{\tau\in G}g_S(\tau\sigma\tau^{-1}).
$$

那么 $\operatorname{ind}_S^G(g)$ 是 $G$ 上的类函数。显然 $\operatorname{ind}_S^G$ 是 $R$-线性的。

由于涉及两个群 $S$ 和 $G$，分别对这两个群取标量积时，记为 $\langle\ ,\ \rangle_S$ 和 $\langle\ ,\ \rangle_G$。下一个定理特别表明，限制与转移关于所用形式互为伴随。

**定理 6.1.** *设 $S$ 是 $G$ 的子群。那么有以下规则：*

**(i)（弗罗贝尼乌斯互反律）** *对 $f\in X_R(G)$ 和 $g\in X_R(S)$ 有*

$$
\langle\operatorname{ind}_S^G(g),f\rangle_G=\langle g,\operatorname{Res}_S^G(f)\rangle_S.
$$

**(ii)** $\operatorname{Ind}_S^G(g)f=\operatorname{ind}_S^G(gf_S)$。

**(iii)** *若 $T\subset S\subset G$ 是 $G$ 的子群，则*

$$
\operatorname{ind}_S^G\circ\operatorname{ind}_T^S=\operatorname{ind}_T^G.
$$

**(iv)** *若 $\sigma\in G$，且 $g^\sigma$ 由 $g^\sigma(\tau^\sigma)=g(\tau)$ 定义，其中 $\tau^\sigma=\sigma^{-1}\tau\sigma$，则*

$$
\operatorname{ind}_S^G(g)=\operatorname{ind}_{S^\sigma}^G(g^\sigma).
$$

**(v)** *若 $\psi$ 是 $S$ 的有效特征标，则 $\operatorname{ind}_S^G(\psi)$ 是有效的。*

<span class="original-page-anchor" id="pdf-page-696" aria-hidden="true"></span>

*证明。* 先证明 (ii)。须证明 $g^Gf=(gf_S)^G$。有

$$
(g^Gf)(\tau)=\frac1{(S:1)}\sum_{\sigma\in G}g_S(\sigma\tau\sigma^{-1})f(\tau)=\frac1{(S:1)}\sum_{\sigma\in G}g_S(\sigma\tau\sigma^{-1})f(\sigma\tau\sigma^{-1}).
$$

刚得到的最后一个表达式等于 $(gf_S)^G$，从而证明 (ii)。现在对 $G$ 中的 $\tau$ 求和。在这个双重和中，只有 $S$ 中能够写成 $\sigma\tau\sigma^{-1}$（$\sigma,\tau\in G$）的元素才产生非零贡献。使 $\sigma\tau\sigma^{-1}$ 等于 $G$ 中一个固定元素的配对 $(\sigma,\tau)$ 的数目等于 $n$（因为对每个 $\lambda\in G$，$(\sigma\lambda,\lambda^{-1}\tau\lambda)$ 是另一个这样的配对，而配对总数是 $n^2$）。所以该表达式等于

$$
(G:1)\frac1{(S:1)}\sum_{\lambda\in S}g(\lambda)f(\lambda).
$$

于是分别由 $G$ 和 $S$ 上的标量积的定义得到第一个规则。

现在设 $g=\psi$ 是 $S$ 的有效特征标，$f=\chi$ 是 $G$ 的单特征标。由 (i) 可知 $g^G$ 的傅里叶系数都是非负整数，因为 $\operatorname{res}_S^G(\chi)$ 是 $S$ 的有效特征标。因此标量积

$$
\langle\psi,\operatorname{res}_S^G(\chi)\rangle_S
$$

非负。所以 $\psi^G$ 是 $G$ 的有效特征标，从而证明 (v)。

为证明传递性，采用以下记号较方便。

用 $\{c\}$ 表示 $S$ 在 $G$ 中的右陪集集合。对每个右陪集 $c$，选取一个固定的陪集代表元，记为 $\bar c$。所以若 $\bar c_1,\ldots,\bar c_r$ 是这些代表元，则

$$
G=\bigcup_c c=\bigcup_c S\bar c=\bigcup_{i=1}^r S\bar c_i.
$$

**引理 6.2.** *设 $g$ 是 $S$ 上的类函数。那么*

$$
\operatorname{ind}_S^G(g)(\xi)=\sum_{i=1}^r g_S(\bar c_i\xi\bar c_i^{-1}).
$$

*证明。* 可以把诱导函数定义中对所有 $\sigma\in G$ 的和拆成双重和

$$
\sum_{\sigma\in G}=\sum_{\sigma\in S}\sum_{i=1}^r,
$$

<span class="original-page-anchor" id="pdf-page-697" aria-hidden="true"></span>

并注意到，当 $\sigma\in S$ 时，每一项 $g_S(\sigma\bar c\xi\bar c^{-1}\sigma^{-1})$ 等于 $g_S(\bar c\xi\bar c^{-1})$，因为 $g$ 是类函数。因此对 $\sigma\in S$ 的求和恰好约去前面的因子 $1/(S:1)$，得到引理中的表达式。

若 $T\subset S\subset G$ 是 $G$ 的子群，且

$$
G=\bigcup S\bar c_i\quad\text{且}\quad S=\bigcup T\bar d_j
$$

是右陪集分解，则 $\{\bar d_j\bar c_i\}$ 构成 $T$ 在 $G$ 中的右陪集代表元系。由此，传递性 (iii) 显然。

把 (iv) 留作习题（使用引理很容易）。

## §7. 诱导表示

设 $G$ 是群，$S$ 是有限指数子群。设 $F$ 是 $S$-模。考虑范畴 $\mathcal C$，其对象是 $F$ 到某个 $G$-模 $E$ 的 $S$-同态 $\varphi:F\to E$。（注意 $G$-模 $E$ 可以通过限制看作 $S$-模。）若 $\varphi':F\to E'$ 是 $\mathcal C$ 中另一个对象，就把 $\mathcal C$ 中的态射 $\varphi'\to\varphi$ 定义为使下图交换的 $G$-同态 $\eta:E'\to E$：

![由 F 出发的映射范畴中的态射](/library/volume-86/diagrams/pdf-0697-morphism-triangle.png)

$\mathcal C$ 中的泛对象在相差唯一的 $G$-同构的意义下确定。把它记为

$$
\operatorname{ind}_S^G:F\longrightarrow\operatorname{ind}_S^G(F).
$$

下面将证明泛对象总存在。若 $\varphi:F\to E$ 是泛对象，就把 $E$ 称为**诱导模**。在相差唯一的使图交换的 $G$-同构的意义下，它唯一确定。为方便起见，选取一个使 $\varphi$ 成为包含映射的诱导模。于是把这个特定的模 $\operatorname{ind}_S^G(F)$ 称为**由 $F$ 诱导的 $G$-模**。特别地，给定到一个 $G$-模 $E$ 的 $S$-同态 $\varphi:F\to E$，存在唯一的 $G$-同态 $\varphi_*:\operatorname{ind}_S^G(F)\to E$，使下图交换：

![诱导模的泛映射](/library/volume-86/diagrams/pdf-0697-universal-triangle.png)

<span class="original-page-anchor" id="pdf-page-698" aria-hidden="true"></span>

对应 $\varphi\mapsto\operatorname{ind}_S^G(\varphi)$ 因而诱导同构

$$
\boxed{\operatorname{Hom}_G(\operatorname{ind}_S^G(F),E)\approx\operatorname{Hom}_S(F,\operatorname{res}_S^G(E)),}
$$

其中 $F$ 是 $S$-模，$E$ 是 $G$-模。马上将看到 $\operatorname{ind}_S^G$ 是从 $\operatorname{Mod}(S)$ 到 $\operatorname{Mod}(G)$ 的函子，上述公式可以表述为：**诱导是限制的伴随函子**。也称此关系为**模的弗罗贝尼乌斯互反律**，因为定理 6.1(i) 是其推论。

有时，若已清楚 $F$ 是哪个群的 $S$-模，就省略下标 $S$，把诱导模直接写为

$$
\operatorname{ind}^G(F).
$$

设 $f:F'\to F$ 是 $S$-同态。若

$$
\varphi_S^G:F'\longrightarrow\operatorname{ind}_S^G(F')
$$

是由 $F'$ 诱导的 $G$-模，则存在唯一的 $G$-同态 $\operatorname{ind}_S^G(F')\to\operatorname{ind}_S^G(F)$，使下图交换：

![S-模同态的诱导](/library/volume-86/diagrams/pdf-0698-induced-morphism-square.png)

它就是图中虚线所表示的 $S$-同态 $\varphi_S^G\circ f$ 的泛性质所对应的 $G$-同态。因此，***$\operatorname{ind}_S^G$ 是从 $S$-模范畴到 $G$-模范畴的函子***。

由诱导模的泛性和唯一性，得到一些形式性质：

*$\operatorname{ind}_S^G$ 与直和交换：若有 $S$-直和 $F\oplus F'$，则*

$$
\operatorname{ind}_S^G(F\oplus F')\approx\operatorname{ind}_S^G(F)\oplus\operatorname{ind}_S^G(F'),
$$

*其中右边的直和是 $G$-直和。*

*若 $f,g:F'\to F$ 是 $S$-同态，则*

$$
\operatorname{ind}_S^G(f+g)=\operatorname{ind}_S^G(f)+\operatorname{ind}_S^G(g).
$$

*若 $T\subset S\subset G$ 是 $G$ 的子群，且 $F$ 是 $T$-模，则*

$$
\operatorname{ind}_S^G\circ\operatorname{ind}_T^S(F)\approx\operatorname{ind}_T^G(F).
$$

<span class="original-page-anchor" id="pdf-page-699" aria-hidden="true"></span>

在这三种情形中，使用泛对象的唯一性，立即得到方程左右两边相等。把验证留给读者。

为证明诱导模存在，用 $M_G^S(F)$ 表示由满足

$$
\sigma f(\xi)=f(\sigma\xi)
$$

的函数 $f:G\to F$ 构成的加法群，其中 $\sigma\in S$ 且 $\xi\in G$。定义 $G$ 在 $M_G^S(F)$ 上的作用如下：令

$$
(\sigma f)(\xi)=f(\xi\sigma),
$$

其中 $\sigma,\xi\in G$。显然 $M_G^S(F)$ 是 $G$-模。

**命题 7.1.** *设 $\varphi:F\to M_G^S(F)$ 满足 $\varphi(x)=\varphi_x$，其中 $\varphi_x$ 是映射*

$$
\varphi_x(\tau)=\begin{cases}0&\text{若 }\tau\notin S,\\\tau x&\text{若 }\tau\in S.\end{cases}
$$

*那么 $\varphi$ 是 $S$-同态，$\varphi:F\to M_G^S(F)$ 是泛的，且 $\varphi$ 是单射。$\varphi$ 的像由满足当 $\tau\notin S$ 时 $f(\tau)=0$ 的元素 $f\in M_G^S(F)$ 构成。*

*证明。* 设 $\sigma\in S$、$x\in F$。设 $\tau\in G$。那么

$$
(\sigma\varphi_x)(\tau)=\varphi_x(\tau\sigma).
$$

若 $\tau\in S$，最后这个表达式等于 $\varphi_{\sigma x}(\tau)$。若 $\tau\notin S$，则 $\tau\sigma\notin S$，所以 $\varphi_{\sigma x}(\tau)$ 和 $\varphi_x(\tau\sigma)$ 都等于 $0$。所以 $\varphi$ 是 $S$-同态，而且立即可见 $\varphi$ 是单射。此外，若 $f\in M_G^S(F)$ 满足当 $\tau\notin S$ 时 $f(\tau)=0$，则由定义得到 $f=\varphi_x$，其中 $x=f(1)$。

还须证明 $\varphi$ 是泛的。为此，更仔细地分析 $M_G^S(F)$ 的结构。

**命题 7.2.** *设 $G=\bigcup_{i=1}^r S\bar c_i$ 是 $G$ 的右陪集分解。令 $F_1$ 是 $M_G^S(F)$ 中在元素 $\xi\in G$、$\xi\notin S$ 上取值 $0$ 的函数的加法群。那么*

$$
M_G^S(F)=\bigoplus_{i=1}^r\bar c_i^{-1}F_1,
$$

*其中直和按阿贝尔群取。*

*证明。* 对每个 $f\in M_G^S(F)$，令 $f_i$ 为满足下式的函数：

$$
f_i(\xi)=\begin{cases}0&\text{若 }\xi\notin S\bar c_i,\\f(\xi)&\text{若 }\xi\in S\bar c_i.\end{cases}
$$

<span class="original-page-anchor" id="pdf-page-700" aria-hidden="true"></span>

对所有 $\sigma\in S$ 有 $f_i(\sigma\bar c_i)=(\bar c_if_i)(\sigma)$。立即可见 $\bar c_if_i$ 属于 $F_1$，且

$$
f=\sum_{i=1}^r\bar c_i^{-1}(\bar c_if_i).
$$

所以 $M_G^S(F)$ 是子群 $\bar c_i^{-1}F_1$ 之和。显然这个和是直和，符合所需。

注意 $\{\bar c_1^{-1},\ldots,\bar c_r^{-1}\}$ 构成 $S$ 在 $G$ 中的*左*陪集代表元系。$G$ 在 $M_G^S(F)$ 上的作用由前面的直和分解给出。可见 $G$ 传递地置换各因子。如命题 7.1 所述，因子 $F_1$ 与原来的模 $F$ 是 $S$-同构的。

假设不考虑任意模，而从交换环 $R$ 出发，只考虑带有 $G$ 的表示的 $R$-模 $E$，即带有同态 $G\to\operatorname{Aut}_R(E)$，从而得到我们称为 $(G,R)$-模的对象。显然，所有构造和定义都适用于这种情境。因此，若有 $S$ 在 $R$-模 $F$ 上的表示，就得到 $G$ 在 $\operatorname{ind}_S^G(F)$ 上的诱导表示。此时讨论的是从 $(S,R)$-模到 $(G,R)$-模的 $S$-同态所构成的范畴 $\mathcal C$。为简化记号，当这种环 $R$ 作为系数环出现时，可以写“$G$-模”表示“$(G,R)$-模”。

**定理 7.3.** *设 $\{\lambda_1,\ldots,\lambda_r\}$ 是 $S$ 在 $G$ 中的左陪集代表元系。存在一个 $G$-模 $E$，包含 $F$ 作为 $S$-子模，使*

$$
E=\bigoplus_{i=1}^r\lambda_iF
$$

*是直和（按 $R$-模）。设 $\varphi:F\to E$ 是包含映射。那么 $\varphi$ 在所用范畴 $\mathcal C$ 中是泛的，即 $E$ 是诱导模。*

*证明。* 通过通常的集合论手续，在 $M_G^S(F)$ 中把 $F_1$ 替换为 $F$，得到一个包含 $F$ 作为 $S$-子模并具有所需直和分解的 $G$-模 $E$。设 $\varphi':F\to E'$ 是到一个 $G$-模 $E'$ 的 $S$-同态。定义

$$
h:E\longrightarrow E'
$$

的规则为

$$
h(\lambda_1x_1+\cdots+\lambda_rx_r)=\lambda_1\varphi'(x_1)+\cdots+\lambda_r\varphi'(x_r),
$$

其中 $x_i\in F$。因为 $E$ 的和是直和，所以该映射定义良好。须证明 $h$ 是 $G$-同态。设 $\sigma\in G$。那么

$$
\sigma\lambda_i=\lambda_{\sigma(i)}\tau_{\sigma,i},
$$

其中 $\sigma(i)$ 是依赖于 $\sigma$ 和 $i$ 的某个指标，$\tau_{\sigma,i}$ 是 $S$ 的元素，也<span class="original-page-anchor" id="pdf-page-701" aria-hidden="true"></span>依赖于 $\sigma,i$。那么

$$
h(\sigma\lambda_ix_i)=h(\lambda_{\sigma(i)}\tau_{\sigma,i}x_i)=\lambda_{\sigma(i)}\varphi'(\tau_{\sigma,i}x_i).
$$

由于 $\varphi'$ 是 $S$-同态，可见该表达式等于

$$
\lambda_{\sigma(i)}\tau_{\sigma,i}\varphi'(x_i)=\sigma h(\lambda_ix_i).
$$

由线性可知 $h$ 是 $G$-同态，符合所需。

下一个命题中回到 $R$ 是域 $k$ 的情形。

**命题 7.4.** *设 $\psi$ 是 $S$ 在 $k$-空间 $F$ 上的表示的特征标。设 $E$ 是诱导表示的空间。那么 $E$ 的特征标 $\chi$ 等于诱导特征标 $\psi^G$，即由公式*

$$
\chi(\xi)=\sum_c\psi_0(\bar c\xi\bar c^{-1})
$$

*给出，其中和遍历 $S$ 在 $G$ 中的右陪集 $c$，$\bar c$ 是 $c$ 的固定陪集代表元，$\psi_0$ 是通过规定当 $\sigma\notin S$ 时 $\psi_0(\sigma)=0$ 而得到的 $\psi$ 到 $G$ 的扩张。*

*证明。* 设 $\{w_1,\ldots,w_m\}$ 是 $F$ 在 $k$ 上的一组基。已知

$$
E=\bigoplus\bar c^{-1}F.
$$

设 $\sigma$ 是 $G$ 的元素。元素 $\{\overline{c\sigma}^{-1}w_j\}_{c,j}$ 构成 $E$ 在 $k$ 上的一组基。注意 $\bar c\sigma\overline{c\sigma}^{-1}$ 是 $S$ 的元素，因为

$$
S\bar c\sigma=Sc\sigma=S\overline{c\sigma}.
$$

有

$$
\sigma(\overline{c\sigma}^{-1}w_j)=\bar c^{-1}(\bar c\sigma\overline{c\sigma}^{-1})w_j.
$$

令

$$
(\bar c\sigma\overline{c\sigma}^{-1})_{\mu j}
$$

为表示 $\bar c\sigma\overline{c\sigma}^{-1}$ 关于基 $\{w_1,\ldots,w_m\}$ 在 $F$ 上作用的矩阵的分量。那么 $\sigma$ 在 $E$ 上的作用为

$$
\begin{aligned}
\sigma(\overline{c\sigma}^{-1}w_j)&=\bar c^{-1}\sum_\mu(\bar c\sigma\overline{c\sigma}^{-1})_{\mu j}w_\mu\\
&=\sum_\mu(\bar c\sigma\overline{c\sigma}^{-1})_{\mu j}(\bar c^{-1}w_\mu).
\end{aligned}
$$

按定义，

$$
\chi(\sigma)=\sum_{c\sigma=c}\sum_j(\bar c\sigma\overline{c\sigma}^{-1})_{jj}.
$$

<span class="original-page-anchor" id="pdf-page-702" aria-hidden="true"></span>

但 $c\sigma=c$ 当且仅当 $\bar c\sigma\bar c^{-1}\in S$。此外，

$$
\psi(\bar c\sigma\bar c^{-1})=\sum_j(\bar c\sigma\bar c^{-1})_{jj}.
$$

所以

$$
\chi(\sigma)=\sum_c\psi_0(\bar c\sigma\bar c^{-1}),
$$

这就是所要证明的。

**注。** 给出诱导特征标的表示空间的显式描述后，在某种意义上，我们已经完成了诱导特征标理论中较初等的部分。有兴趣看应用的读者，可以直接阅读 §12。

### 双陪集

设 $G$ 是群，$S$ 是子群。为避免上标，使用以下记号。设 $\gamma\in G$。写成

$$
[\gamma]S=\gamma S\gamma^{-1}\quad\text{且}\quad S[\gamma]=\gamma^{-1}S\gamma.
$$

*假设 $S$ 有限指数。* 令 $H$ 是子群。形如 $H\gamma S$ 的 $G$ 的子集称为**双陪集**。与陪集类似，立即可验证 $G$ 是双陪集的不交并。设 $\{\gamma\}$ 是一族双陪集代表元，于是有不交并

$$
G=\bigcup_\gamma H\gamma S.
$$

对每个 $\gamma$，有通常的陪集分解

$$
H=\bigcup_{\tau_\gamma}\tau_\gamma(H\cap[\gamma]S),
$$

其中 $\{\tau_\gamma\}$ 是 $H$ 的一个有限元素族，依赖于 $\gamma$。

**引理 7.5.** *元素 $\{\tau_\gamma\gamma\}$ 构成 $S$ 在 $G$ 中的一族左陪集代表元；即有不交并*

$$
G=\bigcup_{\gamma,\tau_\gamma}\tau_\gamma\gamma S.
$$

*证明。* 首先，由假设有

$$
G=\bigcup_\gamma\bigcup_{\tau_\gamma}\tau_\gamma(H\cap[\gamma]S)\gamma S,
$$

所以 $G$ 的每个元素都可写成

$$
\tau_\gamma\gamma s_1\gamma^{-1}\gamma s_2=\tau_\gamma\gamma s\quad\text{其中 }s_1,s_2,s\in S.
$$

另一方面，元素 $\tau_\gamma\gamma$ 代表 $S$ 的不同陪集，因为若 $\tau_\gamma\gamma S=\tau_{\gamma'}\gamma'S$，则 $\gamma=\gamma'$，由于元素 $\gamma$ 代表不同的双陪集，<span class="original-page-anchor" id="pdf-page-703" aria-hidden="true"></span>于是 $\tau_\gamma$ 和 $\tau_{\gamma'}$ 代表 $\gamma S\gamma^{-1}$ 的同一个陪集，因此相等。这就证明了引理。

设 $F$ 是 $S$-模。给定 $\gamma\in G$，用 $[\gamma]F$ 表示 $[\gamma]S$-模，其中对 $\gamma s\gamma^{-1}\in[\gamma]S$，作用由下式给出：

$$
\gamma s\gamma^{-1}\cdot[\gamma]x=[\gamma]sx.
$$

这个记号与以下记号相容：若 $F$ 是 $G$-模 $E$ 的子模，则既可以按上述形式定义，也可以按 $G$ 的作用构造 $\gamma F$。两者自然同构（本质上相等）。将从 $S$-模 $F$ 到 $[\gamma]S$-模 $\gamma F$ 的上述同构记为

$$
[\gamma]:F\longrightarrow\gamma F\text{ 或 }[\gamma]F.
$$

若 $S_1$ 是 $S$ 的子群，则通过限制，$F$ 也是 $S_1$-模；在这种情境下也使用 $[\gamma]$，特别是对包含于 $[\gamma]S$ 的子群 $H\cap[\gamma]S$。

**定理 7.6.** *作用于 $S$-模 $F$ 时，有 $H$-模的同构*

$$
\operatorname{res}_H^G\circ\operatorname{ind}_S^G\approx\bigoplus_\gamma\operatorname{ind}_{H\cap[\gamma]S}^H\circ\operatorname{res}_{H\cap[\gamma]S}^{[\gamma]S}\circ[\gamma],
$$

*其中直和遍历双陪集代表元 $\gamma$。*

*证明。* 引理 7.5 给出 $S$ 在 $G$ 中的陪集代表元，因此由该引理和定理 7.3，诱导模 $\operatorname{ind}_S^G(F)$ 就是直和

$$
\operatorname{ind}_S^G(F)=\bigoplus_{\gamma,\tau_\gamma}\tau_\gamma\gamma F.
$$

另一方面，对每个 $\gamma$，模

$$
\bigoplus_{\tau_\gamma}\tau_\gamma\gamma F
$$

是把 $H\cap[\gamma]S$ 在 $\gamma F$ 上的表示诱导到 $H$ 所得的表示模。对 $\gamma$ 取直和，就得到定理中表达式的右边，从而证明定理。

**注。** 定理 7.6 的形式关系曾出现在阿廷关于诱导特征标和 $L$-函数的形式体系中；参看习题及 [La 70] 第十二章 §3。关于群上同调中的应用，参看 [La 96]。这种形式体系也出现在 Mackey 的工作 [Ma 51]、[Ma 53] 中，现在将更系统地讨论。本节余下部分归于 Mackey。更广泛的结果和应用，参看 Curtis–Reiner [CuR 81]，特别是第一章。另参看习题 15、16 和 17。

为更系统地处理共轭，我们作一些一般的函子性说明。设 $E$ 是 $G$-模。也可能有一个交换环 $R$，使 $E$ 是 $(G,R)$-模。我们将系统地讨论函子<span class="original-page-anchor" id="pdf-page-704" aria-hidden="true"></span>$\operatorname{Hom}_G$、$E^\vee$ 和张量积。设

$$
\lambda:E\longrightarrow\lambda E
$$

是 $R$-同构。把 $G$ 的元素解释为 $E$ 的自同态，就得到作用于 $\lambda E$ 的群 $\lambda G\lambda^{-1}$。也写 $[\lambda]G$ 代替 $\lambda G\lambda^{-1}$。设 $E_1,E_2$ 是 $(G,R)$-模，$\lambda_i:E_i\to\lambda_iE_i$ 是 $R$-同构。那么有自然的 $R$-同构

$$
\lambda_2\operatorname{Hom}_G(E_1,E_2)\lambda_1^{-1}=\operatorname{Hom}_{\lambda_2G\lambda_1^{-1}}(\lambda_1E_1,\lambda_2E_2),\tag{1}
$$

特别地，

$$
[\lambda]\operatorname{Hom}_G(E,E)=\operatorname{Hom}_{[\lambda]G}(\lambda E,\lambda E).
$$

作为一般情形的一个特例，设 $H,S$ 是 $G$ 的子群，$F_1,F_2$ 分别是 $(H,R)$-模和 $(S,R)$-模，$\sigma,\tau\in G$。假设 $\sigma^{-1}\tau$ 属于双陪集 $D=H\gamma S$。那么有 $R$-同构

$$
\operatorname{Hom}_{[\sigma]H\cap[\tau]S}([\sigma]F_1,[\tau]F_2)\approx\operatorname{Hom}_{H\cap[\gamma]S}(F_1,[\gamma]F_2).\tag{2}
$$

这是由共轭立即得到的：写成 $\tau=\sigma h\gamma s$，其中 $h\in H$、$s\in S$，先用 $[\sigma h]^{-1}$ 共轭，再注意对 $s\in S$ 和 $S$-模 $F$，有 $[s]S=S$，且 $[s^{-1}]F$ 同构于 $F$。由 (2) 可见，左边的 $R$-模只依赖于双陪集。设 $D$ 是双陪集。使用记号

$$
M_D(F_1,F_2)=\operatorname{Hom}_{H\cap[\gamma]S}(F_1,[\gamma]F_2),
$$

其中 $\gamma$ 代表双陪集 $D$。用此记号有：

**定理 7.7.** *设 $H,S$ 是 $G$ 的有限指数子群，$F_1,F_2$ 分别是 $(H,R)$-模和 $(S,R)$-模。那么有 $R$-模的同构*

$$
\operatorname{Hom}_G(\operatorname{ind}_H^G(F_1),\operatorname{ind}_S^G(F_2))\approx\bigoplus_D M_D(F_1,F_2),
$$

*其中直和遍历所有双陪集 $H\gamma S=D$。*

*证明。* 有同构：

$$
\begin{aligned}
\operatorname{Hom}_G(\operatorname{ind}_H^G(F_1),\operatorname{ind}_S^G(F_2))&\approx\operatorname{Hom}_H(F_1,\operatorname{res}_H^G\circ\operatorname{ind}_S^G(F_2))\\
&\approx\bigoplus_\gamma\operatorname{Hom}_H(F_1,\operatorname{ind}_{H\cap[\gamma]S}^H\circ\operatorname{res}_{H\cap[\gamma]S}^{[\gamma]S}\circ[\gamma]F_2)\\
&\approx\bigoplus_\gamma\operatorname{Hom}_{H\cap[\gamma]S}(F_1,[\gamma]F_2).
\end{aligned}
$$

第一步和第三步应用诱导模的定义，第二步应用定理 7.6。若 $\gamma$ 是双陪集 $D$ 的代表元，则最后表达式中的每一项就是记为 $M_D(F_1,F_2)$ 的对象。这就证明了定理。

<span class="original-page-anchor" id="pdf-page-705" aria-hidden="true"></span>

**推论 7.8.** *设 $R=k=\mathbf C$，$S,H$ 是有限群 $G$ 的子群。令 $D=H\gamma S$ 遍历双陪集，代表元为 $\gamma$。设 $\chi$ 是 $H$ 的有效特征标，$\psi$ 是 $S$ 的有效特征标。那么*

$$
\langle\operatorname{ind}_H^G(\chi),\operatorname{ind}_S^G(\psi)\rangle_G=\sum_\gamma\langle\chi,[\gamma]\psi\rangle_{H\cap[\gamma]S}.
$$

*证明。* 对等式两边取维数，直接由定理 5.17(b) 和定理 7.7 得到。

**推论 7.9（诱导特征标的不可约性）。** *设 $S$ 是有限群 $G$ 的子群，$R=k=\mathbf C$，$\psi$ 是 $S$ 的有效特征标。那么 $\operatorname{ind}_S^G(\psi)$ 不可约，当且仅当 $\psi$ 不可约，并且对所有 $\gamma\in G$、$\gamma\notin S$ 有*

$$
\langle\psi,[\gamma]\psi\rangle_{S\cap[\gamma]S}=0.
$$

*证明。* 直接由推论 7.8 和定理 5.17(a) 得到。当然，若 $\psi$ 可约，则诱导特征标也可约，这很显然。

推论 7.9 还有以下表述方式。设 $F,F'$ 是 $S$ 的表示空间（在 $\mathbf C$ 上）。若没有一个单 $S$-空间同时出现在 $F$ 和 $F'$ 中，就称 $F,F'$ **不相交**。于是推论 7.9 可以改述为：

**推论 7.9′.** *设 $S$ 是有限群 $G$ 的子群，$F$ 是 $(S,k)$-空间（其中 $k=\mathbf C$）。那么 $\operatorname{ind}_S^G(F)$ 是单的，当且仅当 $F$ 是单的，并且对所有 $\gamma\in G$ 且 $\gamma\notin S$，$S\cap[\gamma]S$-模 $F$ 与 $[\gamma]F$ 不相交。*

接下来说明对偶与诱导表示可交换。

**定理 7.10.** *设 $S$ 是 $G$ 的子群，$F$ 是有限自由 $R$-模。那么有 $G$-同构*

$$
\operatorname{ind}_S^G(F^\vee)\approx(\operatorname{ind}_S^G(F))^\vee.
$$

*证明。* 设 $G=\bigcup\lambda_iS$ 是左陪集分解。如定理 7.3，可以把 $\operatorname{ind}_S^G(F)$ 的表示空间表达为

$$
\operatorname{ind}_S^G(F)=\bigoplus\lambda_iF.
$$

可以选取 $\lambda_1=1$（$G$ 的单位元）。存在唯一的 $R$-同态

$$
f:F^\vee\longrightarrow(\operatorname{ind}_S^G(F))^\vee,
$$

使得对 $\varphi\in F^\vee$ 和 $x\in F$ 有

$$
f(\varphi)(\lambda_ix)=\begin{cases}0&\text{若 }i\ne1,\\\varphi(x)&\text{若 }i=1,\end{cases}
$$

它实际上是 $F^\vee$ 到 $(\lambda_1F)^\vee$ 的 $R$-同构。我们断言它是一个 $S$-<span class="original-page-anchor" id="pdf-page-706" aria-hidden="true"></span>同态。这是例行的验证，我们将其写出。我们有

$$
f([\sigma]\varphi)(\lambda_i x)=\begin{cases}0&\text{若 }i\neq1,\\\sigma(\varphi(\sigma^{-1}x))&\text{若 }i=1.\end{cases}
$$

另一方面，注意若 $\sigma\in S$，则 $\sigma^{-1}\lambda_1\in S$，所以对 $x\in F$ 有 $\sigma^{-1}\lambda_1x\in\lambda_1F$；但若 $\sigma\notin S$，则对 $i\neq1$ 有 $\sigma^{-1}\lambda_i\notin S$，因此 $\sigma^{-1}\lambda_ix\notin\lambda_1F$。于是

$$
[\sigma](f(\varphi))(\lambda_ix)=\sigma f(\varphi)(\sigma^{-1}\lambda_ix)=\begin{cases}0&\text{若 }i\neq1,\\\sigma(\varphi(\sigma^{-1}x))&\text{若 }i=1.\end{cases}
$$

这证明 $f$ 与 $S$ 的作用可交换。

**译校注：** 原文上一段第二种情形印作“but if $\sigma\notin S$”；这里正在验证 $f$ 是 $S$-同态，故应始终取 $\sigma\in S$。在此前提下，若 $i\ne1$，由 $\lambda_iS\ne S$ 才有 $\sigma^{-1}\lambda_i\notin S$。若取 $\sigma\notin S$，该断言并不成立，例如 $\sigma=\lambda_i$ 时 $\sigma^{-1}\lambda_i=1\in S$。

由诱导模的泛性质，存在唯一的 $(G,R)$-同态

$$
\operatorname{ind}_S^G(f):\operatorname{ind}_S^G(F^\vee)\longrightarrow(\operatorname{ind}_S^G(F))^\vee,
$$

它必为同构，因为 $f$ 在其像，即诱导模的 $\lambda_1$ 分量上是同构。定理得证。

有关 Hom 的定理和定义都有关于张量积的类似结果。我们从定义的类似结果开始。

**定理 7.11.** 设 $S$ 为 $G$ 的有限指数子群，$F$ 为 $S$-模，$E$ 为 $G$-模（均在交换环 $R$ 上）。则存在同构

$$
\operatorname{ind}_S^G(\operatorname{res}_S(E)\otimes F)\approx E\otimes\operatorname{ind}_S^G(F).
$$

**证明。** $G$-模 $\operatorname{ind}_S^G(F)$ 包含 $F$ 作为直和项，因为它是直和 $\bigoplus\lambda_iF$，其中 $\lambda_i$ 是定理 7.3 中的左陪集代表元。因此有自然的 $S$-同构

$$
f:\operatorname{res}_S(E)\otimes F\xrightarrow{\approx}E\otimes\lambda_1F\subset E\otimes\operatorname{ind}_S^G(F),
$$

这里取代表元 $\lambda_1=1$（$G$ 的单位元）。由诱导的泛性质，存在 $G$-同态

$$
\operatorname{ind}_S^G(f):\operatorname{ind}_S^G(\operatorname{res}_S(E)\otimes F)\longrightarrow E\otimes\operatorname{ind}_S^G(F),
$$

立即可验证它是同构，正如所求。（注意在最后一步只须验证双射性；这来自作为 $R$-模的直和结构。）

在继续之前，我们对函子性作一些说明。假设有同构 $G\approx G'$，$G$ 的子群 $H$ 在此同构下对应于 $G'$ 的子群 $H'$，并且有从 $H$-模 $F$ 到 $H'$-模 $F'$ 的同构 $F\approx F'$，与 $H,H'$ 的作用可交换。则得到同构

$$
\operatorname{ind}_H^G(F)\approx\operatorname{ind}_{H'}^{G'}(F').
$$

<span class="original-page-anchor" id="pdf-page-707" aria-hidden="true"></span>

特别地，可以取 $\sigma\in G$，令 $G'=[\sigma]G=G$、$H'=[\sigma]H$ 及 $F'=[\sigma]F$。

下面讨论定理 7.7 的类似结果。沿用该定理及其前面讨论中的记号。给定两个子群 $H$ 和 $S$，可以形成张量积

$$
[\sigma]F_1\otimes[\tau]F_2,
$$

其中 $\sigma,\tau\in G$。假设对某个双陪集 $D=H\gamma S$ 有 $\sigma^{-1}\tau\in D$。注意 $[\sigma]F_1\otimes[\tau]F_2$ 是 $[\sigma]H\cap[\tau]S$-模。由共轭作用有同构

$$
\tag{3}\operatorname{ind}_{[\sigma]H\cap[\tau]S}^G([\sigma]F_1\otimes[\tau]F_2)\approx\operatorname{ind}_{H\cap[\gamma]S}^G(F_1\otimes[\gamma]F_2).
$$

**定理 7.12.** 存在 $G$-同构

$$
\operatorname{ind}_H^G(F_1)\otimes\operatorname{ind}_S^G(F_2)\approx\bigoplus_\gamma\operatorname{ind}_{H\cap[\gamma]S}^G(F_1\otimes[\gamma]F_2),
$$

其中对双陪集代表元 $\gamma$ 求和。

**证明。** 有：

$$
\begin{aligned}
\operatorname{ind}_H^G(F_1)\otimes\operatorname{ind}_S^G(F_2)&\approx\operatorname{ind}_H^G(F_1\otimes\operatorname{res}_H\operatorname{ind}_S^G(F_2))&&\text{由定理 7.11}\\
&\approx\bigoplus_\gamma\operatorname{ind}_H^G\left(F_1\otimes\operatorname{ind}_{H\cap[\gamma]S}^H\operatorname{res}_{H\cap[\gamma]S}^{[\gamma]S}([\gamma]F_2)\right)&&\text{由定理 7.6}\\
&\approx\bigoplus_\gamma\operatorname{ind}_H^G\left(\operatorname{ind}_{H\cap[\gamma]S}^H\left(\operatorname{res}_{H\cap[\gamma]S}^H(F_1)\otimes\operatorname{res}_{H\cap[\gamma]S}^{[\gamma]S}([\gamma]F_2)\right)\right)&&\text{由定理 7.7}\\
&\approx\bigoplus_\gamma\operatorname{ind}_{H\cap[\gamma]S}^G(F_1\otimes[\gamma]F_2)&&\text{由诱导的传递性}
\end{aligned}
$$

在最后一行中，将 $F_1\otimes[\gamma]F_2$ 看作 $H\cap[\gamma]S$-模。〔译校注：原文此句印作 $F_1\cap[\gamma]F_2$；上述各行及定理讨论的是张量积，此处应为 $F_1\otimes[\gamma]F_2$。〕定理得证。

**译校注：** 第三步原印“by Theorem 7.7”；该步使用的是定理 7.11 关于张量积与诱导的同构，应用于 $H$ 及其子群 $H\cap[\gamma]S$。定理 7.7 是 Hom 的双陪集公式，故此处引用应为 7.11。

**一般说明。** 本节给出了诱导表示的许多关系。从群上同调的观点看，每个公式都可看成给出了维数 $0$ 的函子同构，因此会产生高阶上同调群 $H^q$ 的相应同构。读者可在 [La 96] 中看到比习题中更进一步的论述。

### 参考文献

[CuR 81] C. W. Curtis 和 I. Reiner，*Methods of Representation Theory*，John Wiley and Sons，1981

[La 96] S. Lang，*Topics in cohomology of groups*，Springer Lecture Notes，1996

[La 70] S. Lang，*Algebraic Number Theory*，Addison-Wesley，1970；Springer Verlag 重印，1986

[Ma 51] G. Mackey，On induced representations of groups，*Amer. J. Math.* **73** (1951)，576–592 页

[Ma 53] G. Mackey，Symmetric and anti-symmetric Kronecker squares of induced representations of finite groups，*Amer. J. Math.* **75** (1953)，387–405 页

<span class="original-page-anchor" id="pdf-page-708" aria-hidden="true"></span>

下面三节在实质上彼此独立，给出诱导表示的例子。在每一种情形中，我们证明某些表示或者从某些熟知的类型诱导而来，或者是某些熟知类型的整系数线性组合。最引人注目的是，我们将所有特征标表示为来自一维特征标的诱导特征标的线性组合。因此，特征标理论在很大程度上归结为研究一维特征标，即阿贝尔特征标。

## §8. 正则特征标的正分解

设 $G$ 为有限群，$k$ 为复数域。以 $1_G$ 表示平凡特征标，以 $r_G$ 表示正则特征标。

**命题 8.1.** 设 $H$ 为 $G$ 的子群，$\psi$ 为 $H$ 的特征标，$\psi^G$ 为诱导特征标。则 $1_H$ 在 $\psi$ 中的重数等于 $1_G$ 在 $\psi^G$ 中的重数。

**证明。** 由定理 6.1 (i)，有

$$
\langle\psi,1_H\rangle_H=\langle\psi^G,1_G\rangle_G.
$$

这些标量积恰为所讨论的重数。

**命题 8.2.** 正则表示是由 $G$ 的平凡子群上的平凡特征标诱导的表示。

**证明。** 在诱导特征标的定义

$$
\psi^G(\tau)=\sum_{\sigma\in G}\psi_H(\sigma\tau\sigma^{-1})
$$

中，取平凡子群上的 $\psi=1$，立即得到结论。

**推论 8.3.** $1_G$ 在正则特征标 $r_G$ 中的重数等于 $1$。

下面研究特征标

$$
u_G=r_G-1_G.
$$

**定理 8.4（Aramata）。** 特征标 $nu_G$ 是由 $G$ 的循环子群的一维特征标诱导的特征标的正整系数线性组合。

证明由两个命题组成，它们明确描述这些诱导特征标。这里的阐述得自 Brauer 的论述，我感谢 Serre 提供这种表述。

<span class="original-page-anchor" id="pdf-page-709" aria-hidden="true"></span>

若 $A$ 是阶为 $a$ 的循环群，在 $A$ 上定义函数 $\theta_A$，条件为：

$$
\theta_A(\sigma)=\begin{cases}a&\text{若 }\sigma\text{ 是 }A\text{ 的生成元，}\\0&\text{其他情形。}\end{cases}
$$

令 $\lambda_A=\varphi(a)r_A-\theta_A$（其中 $\varphi$ 是欧拉函数）；若 $a=1$，令 $\lambda_A=0$。

所需的结论包含在以下两个命题中。

**命题 8.5.** 设 $G$ 为阶为 $n$ 的有限群。则

$$
nu_G=\sum\lambda_A^G,
$$

其中对 $G$ 的所有循环子群求和。

**证明。** 给定 $G$ 上的两个类函数 $\chi,\psi$，有通常的标量积：

$$
\langle\psi,\chi\rangle_G=\frac1n\sum_{\sigma\in G}\psi(\sigma)\overline{\chi(\sigma)}.
$$

设 $\psi$ 为 $G$ 上任意类函数。则：

$$
\begin{aligned}\langle\psi,nu_G\rangle&=\langle\psi,nr_G\rangle-\langle\psi,n1_G\rangle\\&=n\psi(1)-\sum_{\sigma\in G}\psi(\sigma).\end{aligned}
$$

另一方面，利用诱导特征标是限制的转置这一事实，得到

$$
\begin{aligned}
\sum_A\langle\psi,\lambda_A^G\rangle&=\sum_A\langle\psi|A,\lambda_A\rangle\\
&=\sum_A\langle\psi|A,\varphi(a)r_A-\theta_A\rangle\\
&=\sum_A\varphi(a)\psi(1)-\sum_A\frac1a\sum_{\sigma\text{ gen }A}a\psi(\sigma)\\
&=n\psi(1)-\sum_{\sigma\in G}\psi(\sigma).
\end{aligned}
$$

命题等式左右两边的函数与任意函数的标量积都相同，因而它们相等。命题得证。

**命题 8.6.** 若 $A\neq\{1\}$，则函数 $\lambda_A$ 是 $A$ 的不可约非平凡特征标的正整系数线性组合。

<span class="original-page-anchor" id="pdf-page-710" aria-hidden="true"></span>

**证明。** 若 $A$ 是素数阶循环群，则由命题 8.5 知 $\lambda_A=nu_A$，我们的断言由正则表示的标准结构得到。

为了证明一般情形，只须证明 $\lambda_A$ 关于次数为 $1$ 的特征标的傅里叶系数是 $\geq0$ 的整数。设 $\psi$ 为次数为 $1$ 的特征标。取关于 $A$ 的标量积，得到：

$$
\begin{aligned}\langle\psi,\lambda_A\rangle&=\varphi(a)\psi(1)-\sum_{\sigma\text{ gen}}\psi(\sigma)\\&=\varphi(a)-\sum_{\sigma\text{ gen}}\psi(\sigma)\\&=\sum_{\sigma\text{ gen}}(1-\psi(\sigma)).\end{aligned}
$$

对 $A$ 的生成元求和所得的 $\sum\psi(\sigma)$ 是代数整数，而且事实上是有理数（可用许多初等理由说明），所以是有理整数。此外，若 $\psi$ 非平凡，则

$$
1-\psi(\sigma)
$$

的所有实部在 $\sigma\neq\mathrm{id}$ 时 $>0$，在 $\sigma=\mathrm{id}$ 时为 $0$。由最后这两个不等关系，得知这些和必须是正整数。若 $\psi$ 是平凡特征标，则和显然为 $0$。命题得证。

**注。** 定理 8.4 和命题 8.6 出现在泽塔函数与 $L$-函数的背景下，即 Aramata 证明数域的泽塔函数整除其有限扩张的泽塔函数的工作中 [Ar 31]、[Ar 33]。另见 Brauer [Br 47a]、[Br 47b]。Brauer 还利用这些结果证明了代数数论中的一个渐近关系，即

$$
\log(hR)\sim\log\mathbf D^{1/2}\quad\text{当 }[k:\mathbf Q]/\log\mathbf D\longrightarrow0,
$$

其中 $h$ 为数域 $k$ 的理想类数，$R$ 为调整子，$\mathbf D$ 为判别式的绝对值。关于这一应用的阐述，见 [La 70] 第十六章。

### 参考文献

[Ar 31] H. Aramata，Über die Teilbarkeit der Dedekindschen Zetafunktionen，*Proc. Imp. Acad. Tokyo* **7** (1931)，334–336 页

[Ar 33] H. Aramata，Über die Teilbarkeit der Dedekindschen Zetafunktionen，*Proc. Imp. Acad. Tokyo* **9** (1933)，31–34 页

[Br 47a] R. Brauer，On the zeta functions of algebraic number fields，*Amer. J. Math.* **69** (1947)，243–250 页

[Br 47b] R. Brauer，On Artin's L-series with general group characters，*Ann. Math.* **48** (1947)，502–514 页

[La 70] S. Lang，*Algebraic Number Theory*，Springer Verlag（据 Addison-Wesley，1970 年版重印）

<span class="original-page-anchor" id="pdf-page-711" aria-hidden="true"></span>

## §9. 超可解群

设 $G$ 为有限群。若存在子群序列

$$
\{1\}\subset G_1\subset G_2\subset\cdots\subset G_m=G,
$$

使每个 $G_i$ 都在 $G$ 中正规，且 $G_{i+1}/G_i$ 是素数阶循环群，则称 $G$ 为**超可解群**。

由 $p$-群理论，知道每个 $p$-群都是超可解群，$p$-群与阿贝尔群的直积也是超可解群。

**命题 9.1.** 超可解群的每个子群及每个商群都是超可解群。

**证明。** 利用标准同态定理，结论显然。

**命题 9.2.** 设 $G$ 为非阿贝尔超可解群。则存在一个正规阿贝尔子群，真包含其中心。

**证明。** 设 $C$ 为 $G$ 的中心，令 $\bar G=G/C$。设 $\bar H$ 为 $\bar G$ 的素数阶正规子群，$H$ 为它在典范映射 $G\longrightarrow G/C$ 下的原像。若 $\bar\sigma$ 是 $\bar H$ 的生成元，则 $\bar\sigma$ 的一个原像 $\sigma$ 与 $C$ 一起生成 $H$。因此 $H$ 是阿贝尔正规子群，且真包含中心。

**定理 9.3（Blichfeldt）。** 设 $G$ 为超可解群，$k$ 代数闭，$E$ 为单 $(G,k)$-空间。若 $\dim_kE>1$，则存在 $G$ 的真子群 $H$ 和单 $H$-空间 $F$，使 $E$ 由 $F$ 诱导。

**证明。** 阿贝尔群的单表示是一维的，所以假设蕴含 $G$ 不是阿贝尔群。

先在 $E$ 忠实这一附加假设下证明定理。（这意味着：若对所有 $x\in E$ 都有 $\sigma x=x$，则 $\sigma=1$。）最后很容易去掉此限制。

**引理 9.4.** 设 $G$ 为有限群，$k$ 代数闭，$E$ 为 $k$ 上的忠实单 $G$-空间。假设存在 $G$ 的正规阿贝尔子群 $H$，真包含 $G$ 的中心。则存在 $G$ 的真子群 $H_1$，包含 $H$，以及单 $H_1$-空间 $F$，使 $E$ 是 $F$ 从 $H_1$ 到 $G$ 的诱导模。

**证明。** 将 $E$ 看成 $H$-空间。它是单 $H$-空间的直和；由于 $H$ 是阿贝尔群，这样的单 $H$-空间是一维的。

设 $v\in E$ 生成一维 $H$-空间，$\psi$ 为其特征标。若 $w\in E$ 也生成具有相同特征标 $\psi$ 的一维 $H$-空间，则<span class="original-page-anchor" id="pdf-page-712" aria-hidden="true"></span>对所有 $a,b\in k$ 及 $\tau\in H$，有

$$
\tau(av+bw)=\psi(\tau)(av+bw).
$$

以 $F_\psi$ 表示 $E$ 中由所有具有特征标 $\psi$ 的一维 $H$-子空间生成的子空间，则有 $H$-直和分解

$$
E=\bigoplus_\psi F_\psi.
$$

我们断言 $E\neq F_\psi$。否则，取 $v\in E$、$v\neq0$ 及 $\sigma\in G$。由假设，$\sigma^{-1}v$ 是一维 $H$-空间，并具有特征标 $\psi$。所以对 $\tau\in H$，

$$
\tau(\sigma^{-1}v)=\psi(\tau)\sigma^{-1}v
$$

$$
(\sigma\tau\sigma^{-1})v=\sigma\psi(\tau)\sigma^{-1}v=\psi(\tau)v.
$$

这说明 $\sigma\tau\sigma^{-1}$ 与 $\tau$ 对 $E$ 的元素 $v$ 的作用相同。由于 $H$ 不包含于 $G$ 的中心，存在 $\tau\in H$ 和 $\sigma\in G$ 使 $\sigma\tau\sigma^{-1}\neq\tau$，这与 $E$ 忠实的假设矛盾。

我们将证明 $G$ 传递地置换各空间 $F_\psi$。

设 $v\in F_\psi$。对任意 $\tau\in H$ 和 $\sigma\in G$，有

$$
\tau(\sigma v)=\sigma(\sigma^{-1}\tau\sigma)v=\sigma\psi(\sigma^{-1}\tau\sigma)v=\psi_\sigma(\tau)\sigma v,
$$

其中 $\psi_\sigma$ 是 $H$ 上由 $\psi_\sigma(\tau)=\psi(\sigma^{-1}\tau\sigma)$ 定义的函数。这说明 $\sigma$ 将 $F_\psi$ 映入 $F_{\psi_\sigma}$。但由对称性，$\sigma^{-1}$ 将 $F_{\psi_\sigma}$ 映入 $F_\psi$，两个映射 $\sigma,\sigma^{-1}$ 在 $F_{\psi_\sigma}$ 和 $F_\psi$ 之间互逆。因此 $G$ 置换这些空间 $\{F_\psi\}$。

对某个固定的 $\psi_0$，令 $E'=GF_{\psi_0}=\sum\sigma F_{\psi_0}$。则 $E'$ 是 $E$ 的 $G$-子空间；由于假设 $E$ 是单空间，故 $E'=E$。这就证明各空间 $\{F_\psi\}$ 被传递地置换。

对某个固定的 $\psi_1$，令 $F=F_{\psi_1}$。则 $F$ 是 $E$ 的 $H$-子空间。设 $H_1$ 为所有满足 $\tau F=F$ 的元素 $\tau\in G$ 构成的子群。由于 $E\neq F_\psi$，有 $H_1\neq G$。我们断言 $F$ 是单 $H_1$-子空间，而 $E$ 是 $F$ 从 $H_1$ 到 $G$ 的诱导空间。

为此，设 $G=\bigcup H_1\bar c$ 是 $G$ 关于 $H_1$ 的右陪集分解。则元素 $\{\bar c^{-1}\}$ 构成 $H_1$ 的一组左陪集代表元。由于

$$
E=\sum_{\sigma\in G}\sigma F,
$$

故

$$
E=\sum_c\bar c^{-1}F.
$$

我们断言最后这个和是直和，且 $F$ 是单 $H_1$-空间。

<span class="original-page-anchor" id="pdf-page-713" aria-hidden="true"></span>

由于 $G$ 置换这些空间 $\{F_\psi\}$，按定义，$H_1$ 是 $G$ 在此空间集合上作用时 $F$ 的迷向群。因此，当 $c$ 遍历所有陪集时，轨道的元素恰为 $\{\bar c^{-1}F\}$。所以各空间 $\{\bar c^{-1}F\}$ 互不相同，得到直和分解

$$
E=\bigoplus_c\bar c^{-1}F.
$$

若 $W$ 是 $F$ 的真 $H_1$-子空间，则 $\bigoplus\bar c^{-1}W$ 是 $E$ 的真 $G$-子空间，与 $E$ 为单空间的假设矛盾。我们的断言得证。

现在可以应用定理 7.3，得出 $E$ 是从 $F$ 诱导的模，从而在 $E$ 忠实的情形下证明了定理 9.3。

现在假设 $E$ 不忠实。设 $G_0$ 为表示 $G\longrightarrow\operatorname{Aut}_k(E)$ 的核，它是 $G$ 的正规子群。令 $\bar G=G/G_0$。则 $E$ 给出 $\bar G$ 的忠实表示。由于 $E$ 不是一维的，$\bar G$ 不是阿贝尔群，并且存在 $\bar G$ 的真正规子群 $\bar H$ 和单 $\bar H$-空间 $F$，使

$$
E=\operatorname{ind}_{\bar H}^{\bar G}(F).
$$

设 $H$ 是 $\bar H$ 在自然映射 $G\longrightarrow\bar G$ 下的原像。则 $H\supset G_0$，且 $F$ 是单 $H$-空间。当 $\bar G$ 作为 $k$-子空间 $\{\sigma F\}_{\sigma\in\bar G}$ 的置换群作用时，知道 $\bar H$ 是一个分量的迷向群。于是 $H$ 是 $G$ 在同一作用下的迷向群。再次应用定理 7.3，得出 $E$ 在 $G$ 中由 $F$ 诱导，即

$$
E=\operatorname{ind}_H^G(F),
$$

从而证明定理 9.3。

**推论 9.5.** 设 $G$ 为 $p$-群与循环群的乘积，$k$ 代数闭。若 $E$ 是单 $(G,k)$-空间且不是一维的，则 $E$ 由某个子群的一维表示诱导。

**证明。** 利用诱导表示的传递性，逐步应用定理，直到得到某个子群的一维表示。

## §10. Brauer 定理

令 $k=\mathbf C$ 为复数域，$R$ 为 $k$ 的子环。我们研究 $X_R(G)$，即由 $G$ 在 $k$ 上的单特征标的所有 $R$ 系数线性组合构成的环。（由命题 2.1，它是环。）

<span class="original-page-anchor" id="pdf-page-714" aria-hidden="true"></span>

设 $H=\{H_\alpha\}$ 是 $G$ 的一族固定子群，以 $\{\alpha\}$ 为指标。令 $V_R(G)$ 为 $X_R(G)$ 的加法子群，由所有从这一族中某个 $H_\alpha$ 的 $X_R(H_\alpha)$ 中函数诱导出的函数生成。换言之，

$$
V_R(G)=\sum_\alpha\operatorname{ind}_{H_\alpha}^G(X_R(H_\alpha)).
$$

也可以说，$V_R(G)$ 是由从所有 $H_\alpha$ 诱导的所有特征标在 $R$ 上生成的子群。

**引理 10.1.** $V_R(G)$ 是 $X_R(G)$ 的理想。

**证明。** 由定理 6.1 立即得到。

在许多应用中，子群族由“初等”子群组成：设 $p$ 为素数。**$p$-初等群**是指一个 $p$-群与一个循环群的乘积（可假设该循环群的阶与 $p$ 互素，因为可将循环因子的 $p$ 部分并入 $p$-群）。若元素 $\sigma\in G$ 的周期与 $p$ 互素，称它为 **$p$-正则的**；若其周期为 $p$ 的幂，称它为 **$p$-奇异的**。给定 $x\in G$，可唯一地写成

$$
x=\sigma\tau,
$$

其中 $\sigma$ 是 $p$-奇异的，$\tau$ 是 $p$-正则的，且 $\sigma,\tau$ 可交换。事实上，若 $x$ 的周期为 $p^rm$，其中 $m$ 与 $p$ 互素，则有 $1=\nu p^r+\mu m$，从而 $x=(x^m)^\mu(x^{p^r})^\nu$，得到所需分解。唯一性显然，因为两个因子必须属于 $x$ 生成的循环子群。分别称这两个因子为 $x$ 的 **$p$-奇异因子和 $p$-正则因子**。

上述分解还说明：

**命题 10.2.** $p$-初等群的每个子群和每个商群都是 $p$-初等群。若 $S$ 是 $p$-初等群 $P\times C$ 的子群，其中 $P$ 是 $p$-群，$C$ 是阶与 $p$ 互素的循环群，则

$$
S=(S\cap P)\times(S\cap C).
$$

**证明。** 显然。

我们的目标之一是证明：若子群族 $\{H_\alpha\}$ 满足 $G$ 的每个 $p$-初等子群都包含于某个 $H_\alpha$，则对每个环 $R$ 都有 $V_R(G)=X_R(G)$。当然只需对 $R=\mathbf Z$ 证明，但为了我们的论证，需要先用较大的环证明。主要结果是 Brauer 的定理 10.11 和 10.13。我们将阐述 Brauer–Tate 的论证（*Annals of Math.*，1955 年 7 月）。

令 $R$ 为环 $\mathbf Z[\zeta]$，其中 $\zeta$ 是本原 $n$ 次单位根。对某个整数 $N$，$R$ 作为 $\mathbf Z$-模有基 $1,\zeta,\ldots,\zeta^{N-1}$。这是简单的事实，可取 $N$ 为 $\zeta$ 在 $\mathbf Q$ 上的不可约多项式的次数。此不可约多项式的首项系数为 $1$，而且<span class="original-page-anchor" id="pdf-page-715" aria-hidden="true"></span>具有整数系数，故

$$
1,\zeta,\ldots,\zeta^{N-1}
$$

构成 $\mathbf Z[\zeta]$ 的基这一事实由欧几里得算法得到。对次数 $N$，我们不需要了解更多。

先对上述环 $R$ 证明断言，其余部分由下面的引理得到。

**引理 10.3.** 若 $d\in\mathbf Z$，且常函数 $d.1_G$ 属于 $V_R$，则 $d.1_G$ 属于 $V_{\mathbf Z}$。

**证明。** 我们断言 $1,\zeta,\ldots,\zeta^{N-1}$ 在 $X_{\mathbf Z}(G)$ 上线性无关。事实上，若有线性相关关系，则得到

$$
\sum_{\nu=1}^s\sum_{j=0}^{N-1}c_{\nu j}\chi_\nu\zeta^j=0,
$$

其中整数 $c_{\nu j}$ 不全为 $0$。但单特征标在 $k$ 上线性无关，上式是这些单特征标之间系数在 $R$ 中的关系，产生矛盾。因此

$$
V_R=V_{\mathbf Z}\oplus V_{\mathbf Z}\zeta\oplus\cdots\oplus V_{\mathbf Z}\zeta^{N-1}
$$

是（阿贝尔群的）直和，引理随之得到。

若能证明常函数 $1_G$ 属于 $V_R(G)$，则由引理，它属于 $V_{\mathbf Z}(G)$；由于 $V_{\mathbf Z}(G)$ 是理想，便有 $X_{\mathbf Z}(G)=V_{\mathbf Z}(G)$。

为证明定理，需要一系列引理。

若 $G$ 中两个元素 $x,x'$ 的 $p$-正则因子在通常意义下共轭，则称它们 **$p$-共轭**。显然 $p$-共轭是等价关系，其等价类称为 **$p$-共轭类**，或简称 **$p$-类**。

**引理 10.4.** 设 $f\in X_R(G)$，且对所有 $\sigma\in G$ 都有 $f(\sigma)\in\mathbf Z$。则 $f$ 在每个 $p$-类上模 $p$ 为常数。

**证明。** 设 $x=\sigma\tau$，其中 $\sigma$ 是 $p$-奇异的，$\tau$ 是 $p$-正则的，且 $\sigma,\tau$ 可交换。只须证明

$$
f(x)\equiv f(\tau)\pmod p.
$$

设 $H$ 为 $x$ 生成的循环子群。则 $f$ 在 $H$ 上的限制可写成

$$
f_H=\sum a_j\psi_j,
$$

<span class="original-page-anchor" id="pdf-page-716" aria-hidden="true"></span>

其中 $a_j\in R$，$\psi_j$ 是 $H$ 的单特征标，因而是从 $H$ 到 $k^*$ 的同态。对某个幂 $p^r$，有 $x^{p^r}=\tau^{p^r}$，从而 $\psi_j(x)^{p^r}=\psi_j(\tau)^{p^r}$，因此

$$
f(x)^{p^r}\equiv f(\tau)^{p^r}\pmod{pR}.
$$

现在使用下面的引理。

**引理 10.5.** 设 $R=\mathbf Z[\zeta]$ 如前。若 $a\in\mathbf Z$ 且 $a\in pR$，则 $a\in p\mathbf Z$。

**证明。** 由 $R$ 在 $\mathbf Z$ 上有一组包含 $1$ 的基，立即得到。

应用引理 10.5，得出 $f(x)\equiv f(\tau)\pmod p$，因为对每个整数 $b$ 都有 $b^{p^r}\equiv b\pmod p$。

**引理 10.6.** 设 $\tau$ 是 $G$ 中的 $p$-正则元素，$T$ 为 $\tau$ 生成的循环子群，$C$ 为 $G$ 中所有与 $\tau$ 可交换的元素构成的子群，$P$ 为 $C$ 的 $p$-西洛子群。则存在元素 $\psi\in X_R(T\times P)$，使诱导函数 $f=\psi^G$ 满足以下性质：

(i) 对所有 $\sigma\in G$，$f(\sigma)\in\mathbf Z$。

(ii) 若 $\sigma$ 不属于 $\tau$ 的 $p$-类，则 $f(\sigma)=0$。

(iii) $f(\tau)=(C:P)\not\equiv0\pmod p$。

**证明。** 注意 $T$ 和 $P$ 生成的 $G$ 的子群是直积 $T\times P$。设 $\psi_1,\ldots,\psi_r$ 为循环群 $T$ 的单特征标，将其与投影复合，延拓到 $T\times P$：

$$
T\times P\longrightarrow T\longrightarrow k^*.
$$

仍以 $\psi_1,\ldots,\psi_r$ 表示延拓。令

$$
\psi=\sum_{\nu=1}^r\overline{\psi_\nu(\tau)}\psi_\nu.
$$

$T$ 的单特征标的正交关系说明

$$
\psi(\tau y)=\psi(\tau)=(T:1)\quad\text{对 }y\in P,
$$

$$
\psi(\sigma)=0\quad\text{若 }\sigma\in TP\text{ 且 }\sigma\notin\tau P.
$$

我们断言 $\psi^G$ 满足所需条件。

首先，显然 $\psi$ 属于 $X_R(TP)$。

<span class="original-page-anchor" id="pdf-page-717" aria-hidden="true"></span>

对 $\sigma\in G$，有：

$$
\psi^G(\sigma)=\frac1{(TP:1)}\sum_{x\in G}\psi_{TP}(x\sigma x^{-1})=\frac1{(P:1)}\mu(\sigma),
$$

其中 $\mu(\sigma)$ 是使 $x\sigma x^{-1}$ 属于 $\tau P$ 的元素 $x\in G$ 的个数。$\mu(\sigma)$ 被 $(P:1)$ 整除，因为若 $G$ 的元素 $x$ 通过共轭将 $\sigma$ 移到 $\tau P$ 中，则 $Px$ 的每个元素也如此。因此 $\psi^G$ 的值属于 $\mathbf Z$。

此外，只有当 $\sigma$ 与 $\tau$ 为 $p$-共轭时，才可能 $\mu(\sigma)\neq0$，由此得到条件 (ii)。

最后，若 $y\in P$，则只有在 $y=1$ 时才可能 $x\tau x^{-1}=\tau y$（因为 $\tau$ 的周期与 $p$ 互素）。所以 $\mu(\tau)=(C:1)$，得到条件 (iii)。

**引理 10.7.** 假设子群族 $\{H_\alpha\}$ 覆盖 $G$（即 $G$ 的每个元素都属于某个 $H_\alpha$）。若 $f$ 是 $G$ 上取值于 $\mathbf Z$ 的类函数，且所有值都被 $n=(G:1)$ 整除，则 $f$ 属于 $V_R(G)$。

**证明。** 设 $\gamma$ 为共轭类，$p$ 与 $n$ 互素。$G$ 的每个元素都是 $p$-正则的，$G$ 的所有 $p$-子群都是平凡的。此外，$p$-共轭与共轭相同。应用引理 10.6，得到 $V_R(G)$ 中存在一个函数，它在 $\sigma\notin\gamma$ 时取值 $0$，在 $\gamma$ 的元素上取一个整除 $n$ 的整数值。将此函数乘以某个整数，得到 $V_R(G)$ 中存在一个函数，在 $\gamma$ 的所有元素上取值 $n$，在其余元素上取值 $0$。引理立即得到。

**定理 10.8（Artin）。** $G$ 的每个特征标都是从循环子群诱导的特征标的有理系数线性组合。

**证明。** 在引理 10.7 中，令 $\{H_\alpha\}$ 为 $G$ 的循环子群族。常函数 $n.1_G$ 属于 $V_R(G)$。由引理 10.3，此函数属于 $V_{\mathbf Z}(G)$，故 $nX_{\mathbf Z}(G)\subset V_{\mathbf Z}(G)$。因此

$$
X_{\mathbf Z}(G)\subset\frac1n V_{\mathbf Z}(G),
$$

定理得证。

**引理 10.9.** 设 $p$ 为素数，且 $G$ 的每个 $p$-初等子群都包含于某个 $H_\alpha$。则存在函数 $f\in V_R(G)$，其值属于 $\mathbf Z$，且 $\equiv1\pmod{p^r}$。

**证明。** 再次应用引理 10.6。对每个 $p$-类 $\gamma$，可在 $V_R(G)$ 中找到函数 $f_\gamma$，它在 $\gamma$ 以外的元素上取值 $0$，在 $\gamma$ 的元素上模 $p$ 不为 $0$。令 $f=\sum f_\gamma$，其中对所有 $p$-类求和。则对所有 $\sigma\in G$ 都有 $f(\sigma)\not\equiv0\pmod p$。取 $f^{(p-1)p^{r-1}}$ 即得到所需结果。

<span class="original-page-anchor" id="pdf-page-718" aria-hidden="true"></span>

**引理 10.10.** 设 $p$ 为素数，并假设 $G$ 的每个 $p$-初等子群都包含于某个 $H_\alpha$。令 $n=n_0p^r$，其中 $n_0$ 与 $p$ 互素。则常函数 $n_0.1_G$ 属于 $V_{\mathbf Z}(G)$。

**证明。** 由引理 10.3，只须证明 $n_0.1_G$ 属于 $V_R(G)$。取引理 10.9 中的 $f$，则

$$
n_0.1_G=n_0(1_G-f)+n_0f.
$$

由于 $n_0(1_G-f)$ 的值被 $n_0p^r=n$ 整除，由引理 10.7 它属于 $V_R(G)$。另一方面，因为 $f\in V_R(G)$，有 $n_0f\in V_R(G)$。引理得证。

**定理 10.11（Brauer）。** 假设对每个素数 $p$，$G$ 的每个 $p$-初等子群都包含于某个 $H_\alpha$。则 $X(G)=V_{\mathbf Z}(G)$。$G$ 的每个特征标都是从子群 $H_\alpha$ 诱导的特征标的整系数线性组合。

**证明。** 由引理 10.10 立即得到，因为可以在 $V_{\mathbf Z}(G)$ 中找到函数 $n_0.1_G$，其中 $n_0$ 与任意给定素数互素。

**推论 10.12.** $G$ 上的类函数 $f$ 属于 $X(G)$，当且仅当对每个 $\alpha$，其在 $H_\alpha$ 上的限制属于 $X(H_\alpha)$。

**证明。** 假设对每个 $\alpha$，$f$ 在 $H_\alpha$ 上的限制是 $H_\alpha$ 的特征标。由定理，可写成

$$
1_G=\sum_\alpha c_\alpha\operatorname{ind}_{H_\alpha}^G(\psi_\alpha),
$$

其中 $c_\alpha\in\mathbf Z$，$\psi_\alpha\in X(H_\alpha)$。由定理 6.1，

$$
f=\sum_\alpha c_\alpha\operatorname{ind}_{H_\alpha}^G(\psi_\alpha f_{H_\alpha}).
$$

若 $f_{H_\alpha}\in X(H_\alpha)$，则得出 $f$ 属于 $X(G)$。反向结论当然显然。

**定理 10.13（Brauer）。** $G$ 的每个特征标都是由子群的一维特征标诱导的特征标的整系数线性组合。

**证明。** 由定理 10.11 和诱导的传递性，只须证明 $p$-初等群的每个特征标具有定理所述性质。但这已在前一节推论 9.5 中证明。

<span class="original-page-anchor" id="pdf-page-719" aria-hidden="true"></span>

## §11. 表示的定义域

回到 $k$ 的特征与 $\#G$ 互素的一般情形。设 $E$ 为 $k$-空间，并假设有 $G$ 在 $E$ 上的表示。设 $k'$ 为 $k$ 的扩张域。则 $G$ 按规则

$$
\sigma(a\otimes x)=a\otimes\sigma x
$$

作用于 $k'\otimes_kE$，其中 $a\in k'$、$x\in E$。此作用来自乘积 $k'\times E$ 上的双线性映射

$$
(a,x)\longmapsto a\otimes\sigma x.
$$

将 $E'=k'\otimes_kE$ 看成 $E$ 通过 $k'$ 的扩张，便得到 $G$ 在 $E'$ 上的表示。

**命题 11.1.** 记号如上。则 $G$ 在 $E$ 及 $E'$ 上的表示的特征标相等。

**证明。** 设 $\{v_1,\ldots,v_m\}$ 为 $E$ 在 $k$ 上的基。则

$$
\{1\otimes v_1,\ldots,1\otimes v_m\}
$$

为 $E'$ 在 $k'$ 上的基。因此，$G$ 的元素 $\sigma$ 关于两组基的表示矩阵相同，所以迹相等。

反过来，设 $k'$ 为域，$k$ 为其子域。若存在 $k$-空间 $E$ 及 $G$ 在 $E$ 上的表示，使 $k'$-空间 $E'$ 与 $k'\otimes_kE$ 为 $G$-同构，则称 $G$ 在 $E'$ 上的表示**可在 $k$ 上定义**。

**命题 11.2.** 设 $E,F$ 为有限群 $G$ 在 $k$ 上的单表示空间，$k'$ 为 $k$ 的扩张。假设 $E,F$ 不为 $G$-同构。则 $E_{k'}$ 的任何 $k'$-单分量都不出现在 $F_{k'}$ 分解为 $k'$-单子空间的直和分解中。

**证明。** 考虑在 $k$ 上分解为单环直积的分解

$$
k[G]=\prod_{\mu=1}^{s(k)}R_\mu(k).
$$

不失一般性，可假设 $E,F$ 是 $k[G]$ 的单左理想；由假设，它们属于此直积的不同因子。现在与 $k'$ 作张量积，得到的正是 $k'[G]$。于是得到在 $k'$ 上的直积分解。由于在 $\nu\neq\mu$ 时 $R_\nu(k)R_\mu(k)=0$，此分解实际上由每个因子的直积<span class="original-page-anchor" id="pdf-page-720" aria-hidden="true"></span>分解给出，即对各个 $R_\mu(k)$，有：

$$
k'[G]=\prod_{\mu=1}^{s(k)}\prod_{i=1}^{m(\mu)}R_{\mu i}(k').
$$

设 $E=L_\nu$、$F=L_\mu$，且 $\nu\neq\mu$。则 $R_\mu E=0$，故对每个 $i=1,\ldots,m(\mu)$ 都有 $R_{\mu i}E_{k'}=0$。这说明 $E_{k'}$ 的任何单分量都不可能与 $R_{\mu i}$ 的任一个单左理想为 $G$-同构，所需结论得证。

**推论 11.3.** $G$ 在 $k$ 上的单特征标 $\chi_1,\ldots,\chi_{s(k)}$ 在 $k$ 的任意扩张 $k'$ 上都线性无关。

**证明。** 由命题及 $k'$-单特征标在 $k'$ 上的线性无关性，立即得到。

命题 11.1 和 11.2 实质上是抽象的一般性陈述。下一个定理的证明使用 Brauer 定理。

**定理 11.4（Brauer）。** 设 $G$ 为指数为 $m$ 的有限群。$G$ 在复数域（或特征为 $0$ 的代数闭域）上的每个表示都可在域 $\mathbf Q(\zeta_m)$ 上定义，其中 $\zeta_m$ 为本原 $m$ 次单位根。

**证明。** 设 $\chi$ 为 $G$ 在 $\mathbf C$ 上某个表示的特征标，即有效特征标。由定理 10.13，可写成

$$
\chi=\sum_j c_j\operatorname{ind}_{S_j}^G(\psi_j),\qquad c_j\in\mathbf Z,
$$

其中对有限个子群 $S_j$ 求和，$\psi_j$ 是 $S_j$ 的一维特征标。显然每个 $\psi_j$ 都可在 $\mathbf Q(\zeta_m)$ 上定义，因此诱导特征标 $\psi_j^G$ 可在 $\mathbf Q(\zeta_m)$ 上定义。每个 $\psi_j^G$ 可写成

$$
\psi_j^G=\sum_\mu d_{j\mu}\chi_\mu,\qquad d_{j\mu}\in\mathbf Z,
$$

其中 $\{\chi_\mu\}$ 是 $G$ 在 $\mathbf Q(\zeta_m)$ 上的单特征标。因此

$$
\chi=\sum_\mu\left(\sum_j c_jd_{j\mu}\right)\chi_\mu.
$$

$\chi$ 作为 $k$ 上单特征标的线性组合的表达是唯一的，所以系数

$$
\sum_j c_jd_{j\mu}
$$

为 $\geq0$。所需结论得证。

<span class="original-page-anchor" id="pdf-page-721" aria-hidden="true"></span>

## §12. 例：有限域上的 $\mathrm{GL}_2$

设 $F$ 为域。将 $\mathrm{GL}_2(F)$ 看成作用于二维向量空间 $V=F^2$。照例以 $F^a$ 表示代数闭包，令 $V^a=F^a\times F^a=F^a\otimes V$（在 $F$ 上作张量积）。所谓**半单**，总是指绝对半单，即在代数闭包 $F^a$ 上半单。若 $V^a$ 在 $F^a[\alpha]$ 上半单，则称元素 $\alpha\in\mathrm{GL}_2(F)$ 为**半单元素**。若子群的每个元素都半单，则称该子群为**半单子群**。

设 $K$ 为 $F$ 的可分二次扩张，$\{\omega_1,\omega_2\}$ 为 $K$ 的一组基。则有 $K$ 关于此基的正则表示，即乘法将 $K^*$ 表示为 $\mathrm{GL}_2(F)$ 的子群。范数为 $1$ 的元素恰对应于 $K^*$ 的像中属于 $\mathrm{SL}_2(F)$ 的元素。对 $K$ 选择不同的基，对应于在 $\mathrm{GL}_2(F)$ 中对该像作共轭。以 $C_K$ 表示这样一个像，称 $C_K$ 为**非分裂 Cartan 子群**。子代数

$$
F[C_K]\subset\operatorname{Mat}_2(F)
$$

与 $K$ 本身同构，因此该代数的可逆元就是 $C_K\approx K^*$ 的元素。

**引理 12.1.** 子群 $C_K$ 是极大交换半单子群。

**证明。** 若 $\alpha\in\mathrm{GL}_2(F)$ 与 $C_K$ 的所有元素可交换，则 $\alpha$ 必须属于 $F[C_K]$，否则 $\{1,\alpha\}$ 在 $F[C_K]$ 上线性无关，从而 $\operatorname{Mat}_2(F)$ 将是交换的，与事实不符。由于 $\alpha$ 可逆，它是 $F[C_K]$ 的可逆元，故 $\alpha\in C_K$，即所需结论。

**分裂 Cartan 子群**是指如下对角矩阵组成的群：

$$
\begin{pmatrix}a&0\\0&d\end{pmatrix}\quad\text{其中 }a,d\in F^*.
$$

以 $A$ 表示分裂 Cartan 子群；若需指明域 $F$，则记作 $A(F)$。

**Cartan 子群**是指与分裂 Cartan 子群或上述某个 $C_K$ 共轭的子群。

**引理 12.2.** $\mathrm{GL}_2(F)$ 的每个极大交换半单子群都是 Cartan 子群，反之亦然。

**译校注：** 原文“反之亦然”包含分裂 Cartan 子群也极大的断言；这一断言在 $F=\mathbf F_2$ 时有例外。此时 $A(F)=\{1\}$，它严格包含于由 $\mathbf F_4^*$ 得到的三阶非分裂 Cartan 子群，后者交换且半单。故分裂情形的极大性须排除 $F=\mathbf F_2$；此处保留原文断言并说明这一条件限制。

**证明。** 显然分裂 Cartan 子群是极大交换半单子群。设 $H$ 是 $\mathrm{GL}_2(F)$ 的极大交换半单子群。若 $H$ 在 $F$ 上可对角化，则 $H$ 包含于分裂 Cartan 子群的某个共轭子群。另一方面，假设 $H$ 在 $F$ 上不可对角化。它在 $F$ 的可分闭包上可对角化，且两个维数为<span class="original-page-anchor" id="pdf-page-722" aria-hidden="true"></span>$1$ 的特征子空间给出 $H$ 到可分闭包乘法群的两个特征标

$$
\psi,\psi':H\longrightarrow F^{s*}.
$$

对每个 $\alpha\in H$，$\psi(\alpha)$ 和 $\psi'(\alpha)$ 是 $\alpha$ 的特征值；对某个 $\alpha\in H$，这两个特征值不同，否则 $H$ 在 $F$ 上可对角化。因此这对元素 $\psi(\alpha),\psi'(\alpha)$ 在 $F$ 上共轭。像 $\psi(H)$ 是循环的；若 $\psi(\alpha)$ 生成此像，则 $\psi(\alpha)$ 生成 $F$ 的二次扩张 $K$。映射

$$
\alpha\longmapsto\psi(\alpha)\quad\text{其中 }\alpha\in H
$$

延拓为代数 $F[H]$ 到 $K$ 的 $F$-线性映射，仍记为 $\psi$。由于 $F[H]$ 半单，$\psi:F[H]\longrightarrow K$ 是同构。因此 $\psi$ 将 $H$ 映入 $K^*$；事实上，它将 $H$ 映满 $K^*$，因为 $H$ 是极大的。引理得证。

在上述证明中，两个特征标 $\psi,\psi'$ 称为 **Cartan 子群的（本征）特征标**。在分裂情形中，若 $\alpha$ 的对角元素为 $a,d$，得到的两个特征标满足 $\psi(\alpha)=a$、$\psi'(\alpha)=d$。在分裂情形中，特征标的值属于 $F$；在非分裂情形中，这些值在 $F$ 上为二次共轭元素，并属于 $K$。

**命题 12.3.** 设 $H$ 为 $\mathrm{GL}_2(F)$ 的 Cartan 子群（分裂或非分裂）。则 $H$ 在其正规化子 $N(H)$ 中的指数为 $2$。

**译校注：** 前面证明中的原句“像 $\psi(H)$ 是循环的”在有限域 $F$ 下成立；本节此处尚设 $F$ 为一般域，不能普遍作此断言，例如 $F=\mathbf R$、$K=\mathbf C$ 时非分裂 Cartan 子群的本征特征标像为非循环群 $\mathbf C^*$。命题 12.3 的分裂情形也须排除 $F=\mathbf F_2$：此时 $A=\{1\}$，$N(A)=\mathrm{GL}_2(\mathbf F_2)$，指数为 $6$，而非原印的 $2$。原文证明所用“两本征特征标不同”在这一例外情形不成立。以上原句均予保留，并说明各自适用条件。

**证明。** 可将 $\mathrm{GL}_2(F)$ 看成作用于代数闭包 $F^a$ 上的二维向量空间 $V^a=F^a\oplus F^a$。无论 $H$ 是否分裂，本征特征标都不同（在非分裂情形中，这是因为可分性假设）；正规化子的元素必须固定或交换特征子空间。若它固定这些空间，则由引理 12.2 中 $H$ 的极大性，它属于 $H$。若它交换这些空间，则不属于 $H$，并生成 $N/H$ 中唯一的一个陪集，所以 $H$ 在 $N$ 中的指数为 $2$。

在分裂情形中，交换特征子空间的 $N/A$ 的一个代表元为

$$
w=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

在非分裂情形中，设 $\sigma:K\longrightarrow K$ 为非平凡自同构，$\{\alpha,\sigma\alpha\}$ 为正规基。关于此基，$\sigma$ 的矩阵恰为

$$
w=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

因此在这一情形中同样存在非平凡元素属于<span class="original-page-anchor" id="pdf-page-723" aria-hidden="true"></span>$C_K$ 的正规化子。〔译校注：原文此处印作“$A$ 的正规化子”；上一页此段讨论非分裂 Cartan 子群 $C_K$，$A$ 则表示分裂 Cartan 子群，故这里应为 $C_K$。〕注意，若 $M(x)$ 是元素 $x\in K$ 对应的矩阵，则立即可验证关系

$$
M(\sigma)M(x)M(\sigma^{-1})=M(\sigma x).
$$

由于域的乘法群中元素的阶与特征互素，得到：

若 $F$ 的特征为 $p$，则 $\mathrm{GL}_2(F)$ 的有限阶元素半单，当且仅当其阶与 $p$ 互素。

### 共轭类

我们将明确确定共轭类。将情形特殊化，以下令：

$$
\begin{aligned}
F&=\text{有 }q\text{ 个元素的有限域；}\\
G&=\mathrm{GL}_2(F);\\
Z&=G\text{ 的中心；}\\
A&=G\text{ 的对角子群；}\\
C&\approx K^*=G\text{ 的一个非分裂 Cartan 子群。}
\end{aligned}
$$

在共轭意义下只有一个非分裂 Cartan 子群，因为有限域只有一个二次扩张（在给定的代数闭包 $F^a$ 中）（参见第十四章推论 2.7）。回顾

$$
\#(G)=(q^2-1)(q^2-q)=q(q+1)(q-1)^2.
$$

此前应已将其作为习题算出。事实上，$F\times F$ 有 $q^2$ 个元素，$\#(G)$ 等于 $F\times F$ 的基的个数。第一个基向量有 $q^2-1$ 种选择，第二个有 $q^2-q$ 种选择（第一次排除 $(0,0)$，第二次排除所有已选出的元素）。由此得到 $\#(G)$ 的值。

元素 $\alpha$ 的共轭类有两种情形。

**情形 1。** 特征多项式可约，所以特征值属于 $F$。在此情形中，由 Jordan 标准形，该元素与以下某个矩阵共轭：

$$
\begin{pmatrix}a&0\\0&a\end{pmatrix},\qquad\begin{pmatrix}a&1\\0&a\end{pmatrix},\qquad\begin{pmatrix}a&0\\0&d\end{pmatrix}\quad\text{其中 }d\neq a.
$$

它们分别称为**中心的、幺幂的、或有理但非中心的**。

**情形 2。** 特征多项式不可约。则 $\alpha$ 满足 $F[\alpha]\approx E$，其中 $E$ 为 $F$ 的二次扩张。于是 $\{1,\alpha\}$ 是 $F[\alpha]$ 在 $F$ 上的基；在 $F[\alpha]$ 上的乘法表示中，与 $\alpha$ 对应的矩阵为

$$
\begin{pmatrix}0&-b\\1&-a\end{pmatrix},
$$

<span class="original-page-anchor" id="pdf-page-724" aria-hidden="true"></span>

其中 $a,b$ 是特征多项式 $X^2+ax+b$ 的系数。

于是有下表。

**表 12.4**

$$
\begin{array}{|c|c|c|}\hline
\text{类}&\text{类的个数}&\text{类中元素的个数}\\\hline
\begin{pmatrix}a&0\\0&a\end{pmatrix}&q-1&1\\\hline
\begin{pmatrix}a&1\\0&a\end{pmatrix}&q-1&q^2-1\\\hline
\begin{gathered}\begin{pmatrix}a&0\\0&d\end{pmatrix}\\a\neq d\end{gathered}&\frac12(q-1)(q-2)&q^2+q\\\hline
\alpha\in C-F^*&\frac12(q-1)q&q^2-q\\\hline
\end{array}
$$

每种情形中，给定类的元素个数都等于该元素的正规化子（或中心化子）的指数。情形 1 显然。情形 2 可直接计算，因为此时中心化子由矩阵

$$
\begin{pmatrix}x&y\\0&x\end{pmatrix},\quad x\in F,
$$

且 $x\neq0$ 构成。第三、第四种情形可利用命题 12.3。至于各类型中类的个数，第一、第二种情形对应于 $a\in F^*$ 的不同选择，因而各有 $q-1$ 个类。第三种情形的共轭类由特征值确定。$a$ 有 $q-1$ 种选择，随后 $d$ 有 $q-2$ 种选择。但决定共轭类的是无序特征值对，故须将 $(q-1)(q-2)$ 除以 $2$，得到类的个数。最后，对非分裂 Cartan 子群中的元素，已经看到：若 $\sigma$ 生成 $\operatorname{Gal}(K/F)$，则 $M(\sigma x)$ 与 $M(x)$ 在 $\mathrm{GL}_2(F)$ 中共轭。另一方面，假设 $x,x'\in K^*$，在关于给定基的 $K^*$ 在 $K$ 上的给定正则表示下，$M(x),M(x')$ 在 $\mathrm{GL}_2(F)$ 中共轭。此共轭诱导 $F[C_K]$ 的 $F$-代数同构，从而诱导 $K$ 的自同构，它或者是恒等自同构，或者是非平凡自同构 $\sigma$。因此第四类元素的共轭类个数等于

$$
\frac{\#(K)-\#(F)}2=\frac{q^2-q}2,
$$

这给出表中的值。

<span class="original-page-anchor" id="pdf-page-725" aria-hidden="true"></span>

### Borel 子群与诱导表示

令：

$$
\begin{aligned}U&=\text{由幺幂元素 }\begin{pmatrix}1&b\\0&1\end{pmatrix}\text{ 构成的群；}\\B&=\text{Borel 子群}=UA=AU.\end{aligned}
$$

则 $\#(B)=q(q-1)^2=(q-1)(q^2-q)$。我们将从 $B$ 诱导特征标来构造 $G$ 的表示，最后适当组合诱导表示，构造 $G$ 的全部不可约表示。将讨论四类特征标。第一类是一维的，显然为单特征标；对于其他类型，将通过计算诱导特征标证明其单性。一个情形中需要减去一维特征标；其余情形中，诱导特征标将是单的。我们的步骤是系统的：对每种类型给出值表；对每个要证明为单的特征标 $\chi$，验证

$$
\sum_{\beta\in G}|\chi(\beta)|^2=\#(G),
$$

再应用定理 5.17(a) 得到单性。对四种类型均完成这些步骤之后，由值表可见它们互不相同。最后，列出的不同特征标的总数等于共轭类的个数，由此得出已列出全部单特征标。

下面实施这一方案。我是在 Harvard 的一门课上，从 Tate 的一页讲义中学到 $\mathrm{GL}_2(F)$ 的单特征标的。该讲义给出后面的表以及特征标在共轭类上的值。我在随后几页中补充了证明。

### 第一类

以 $\mu:F^*\longrightarrow\mathbf C^*$ 表示同态。于是得到一维特征标

$$
\mu\circ\det:G\longrightarrow\mathbf C^*.
$$

它在共轭类代表元上的值如下表所示。

**表 12.5(I)**

$$
\begin{array}{|c|c|c|c|c|}\hline
\chi&\begin{pmatrix}a&0\\0&a\end{pmatrix}&\begin{pmatrix}a&1\\0&a\end{pmatrix}&\begin{pmatrix}a&0\\0&d\end{pmatrix}_{d\neq a}&\alpha\in C-F^*\\\hline
\mu\circ\det&\mu(a)^2&\mu(a)^2&\mu(ad)&\mu\circ\det(\alpha)\\\hline
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-726" aria-hidden="true"></span>

所列的值由定义得到。最后一个值也可写成

$$
\mu(\det\alpha)=\mu(N_{K/F}(\alpha)),
$$

这里将 $\alpha$ 看成 $K^*$ 的元素，因为读者应由域论知道行列式给出范数。

若 $G$ 的特征标等于某个 $\mu$ 对应的 $\mu\circ\det$，则称它属于**第一类**。由于 $\#(F^*)=q-1$，第一类特征标有 $q-1$ 个。

### 第二类

注意 $B/U=A$。因此可通过 $B/U$ 将 $A$ 的特征标看成 $B$ 的特征标。令：

$\psi_\mu=\operatorname{res}_A(\mu\circ\det)$，从而将 $\psi_\mu$ 看成 $B$ 的特征标。于是

$$
\psi_\mu\begin{pmatrix}a&b\\0&d\end{pmatrix}=\mu(ad).
$$

得到诱导特征标

$$
\psi_\mu^G=\operatorname{ind}_B^G(\psi_\mu).
$$

$\psi_\mu^G$ 不是单的，它包含 $\mu\circ\det$；这可由 Frobenius 互反律看出：

$$
\langle\operatorname{ind}_B^G\psi_\mu,\mu\circ\det\rangle_G=\langle\psi_\mu,\mu\circ\det\rangle_B=\frac1{\#(B)}\sum_{\beta\in B}|\mu\circ\det(\beta)|^2=1.
$$

称特征标 $\chi=\psi_\mu^G-\mu\circ\det$ 属于**第二类**。

它们在共轭类代表元上的值如下。

**表 12.5(II)**

$$
\begin{array}{|c|c|c|c|c|}\hline
\chi&\begin{pmatrix}a&0\\0&a\end{pmatrix}&\begin{pmatrix}a&1\\0&a\end{pmatrix}&\begin{pmatrix}a&0\\0&d\end{pmatrix}_{d\neq a}&\alpha\in C-F^*\\\hline
\psi_\mu^G-\mu\circ\det&q\mu(a)^2&0&\mu(ad)&-\mu\circ\det(\alpha)\\\hline
\end{array}
$$

实际计算时，先计算 $\psi_\mu^G$ 的值，再减去 $\mu\circ\det$ 的值。〔译校注：原文此句印作 $\theta\circ\det$；本段所定义的第二类特征标为 $\psi_\mu^G-\mu\circ\det$，故这里应为 $\mu\circ\det$。〕对此情形及随后两种情形，使用诱导函数公式：

$$
\operatorname{ind}_H^G(\varphi)(\alpha)=\frac1{\#(H)}\sum_{\beta\in G}\varphi_H(\beta\alpha\beta^{-1}),
$$

其中 $\varphi_H$ 在 $H$ 上等于 $\varphi$，在 $H$ 外等于 $0$。中心的元素与所有 $\beta\in G$ 可交换，因此对 $\varphi=\psi_\mu$，诱导特征标的值<span class="original-page-anchor" id="pdf-page-727" aria-hidden="true"></span>在这样的元素上为

$$
\frac{\#(G)}{\#(B)}\mu(a)^2=(q+1)\mu(a)^2,
$$

由此得到所列的值。

对元素 $u=\begin{pmatrix}a&1\\0&a\end{pmatrix}$，使 $\beta u\beta^{-1}$ 属于 $B$ 的元素 $\beta\in G$ 只有 $B$ 的元素（可直接验证）。于是立即得到

$$
\operatorname{ind}_B^G(\psi_\mu)\begin{pmatrix}a&1\\0&a\end{pmatrix}=\mu(a)^2,
$$

这给出特征标 $\chi$ 的所列值。利用表 12.4，立即算出 $\sum|\chi(\beta)|^2=\#(G)$，因此：

第二类特征标 $\chi$ 是单的。

值表还说明第二类特征标有 $q-1$ 个。

随后两种类型专门讨论 Cartan 子群。

### 第三类

**译校注：** 本段关于 $N(A)/A$ 的二阶代表元和在 $A$ 上“二阶自同构”的说法，须按命题 12.3 旁的注释排除 $F=\mathbf F_2$；该例中 $A=\{1\}$，共轭作用为恒等。第三类所要求的 $[w]\psi\ne\psi$ 在该例没有解，故其后该类特征标的数量仍为 $0$。

以 $\psi:A\longrightarrow\mathbf C^*$ 表示同态。

如命题 12.3 后所述，$N(A)/A$ 的代表元 $w=w_A=w^{-1}$ 满足

$$
w\begin{pmatrix}a&0\\0&d\end{pmatrix}w=\begin{pmatrix}d&0\\0&a\end{pmatrix}=\alpha^w\quad\text{若 }\alpha=\begin{pmatrix}a&0\\0&d\end{pmatrix}.
$$

因此由 $w$ 作共轭是 $A$ 的二阶自同构。令 $[w]\psi$ 为共轭特征标，即对 $\alpha\in A$，$([w]\psi)(\alpha)=\psi(w\alpha w)=\psi(\alpha^w)$。则 $[w](\mu\circ\det)=\mu\circ\det$。$A$ 上的特征标 $\mu\circ\det$ 恰为在 $[w]$ 下不变的那些特征标。其余特征标可写成

$$
\psi\begin{pmatrix}a&0\\0&d\end{pmatrix}=\psi_1(a)\psi_2(d),
$$

其中 $\psi_1,\psi_2:F^*\longrightarrow\mathbf C^*$ 是不同的特征标。由同构 $B/U\approx A$，将 $\psi$ 看成 $B$ 的特征标。于是构造诱导特征标

$$
\psi^G=\operatorname{ind}_B^G(\psi)=\operatorname{ind}_B^G([w]\psi).
$$

若 $\psi$ 满足 $[w]\psi\neq\psi$，则称特征标 $\chi=\psi^G$ 属于**第三类**。以下是它们的值表。

<span class="original-page-anchor" id="pdf-page-728" aria-hidden="true"></span>

**表 12.5(III)**

$$
\begin{array}{|c|c|c|c|c|}\hline
\chi&\begin{pmatrix}a&0\\0&a\end{pmatrix}&\begin{pmatrix}a&1\\0&a\end{pmatrix}&\alpha=\begin{pmatrix}a&0\\0&d\end{pmatrix}_{d\neq a}&\alpha\in C-F^*\\\hline
\begin{gathered}\psi^G\\\psi\neq[w]\psi\end{gathered}&(q+1)\psi(a)&\psi(a)&\psi(\alpha)+\psi(\alpha^w)&0\\\hline
\end{array}
$$

第一项在中心元素上的值是显然的。对第二项，已经看到，若 $\beta\in G$ 满足

$$
\beta\begin{pmatrix}a&1\\0&a\end{pmatrix}\beta^{-1}\in B,
$$

则 $\beta\in B$，所以公式

$$
\psi^G(\alpha)=\frac1{\#(B)}\sum_{\beta\in G}\psi_B(\beta\alpha\beta^{-1})
$$

立即给出 $\psi^G$ 在幺幂元素上的值。对 $A$ 中满足 $a\neq d$ 的元素，还可由 $A$ 的正规化子中的元素 $w$ 作共轭，表中的值随即由公式得到。对非分裂 Cartan 群的元素，$G$ 中没有元素将它们共轭到 $B$ 的元素，所以最后一列的值为 $0$。

我们断言第三类特征标 $\chi=\psi^G$ 是单的。

证明再次使用单性判别，即 $\sum|\chi(\beta)|^2=\#(G)$。注意两个元素 $\alpha,\alpha'\in A$ 在 $G$ 中属于同一共轭类，当且仅当 $\alpha'=\alpha$ 或 $\alpha'=[w]\alpha$。直接计算可验证这一点。因此按 $\beta$ 所在的各共轭类写出和 $\sum|\psi^G(\beta)|^2$，并利用表 12.4，得到：

$$
\begin{aligned}\sum_{\beta\in G}|\psi^G(\beta)|^2&=(q+1)^2(q-1)\\&\quad+(q-1)(q^2-1)+(q^2+q)\sum_{\alpha\in(A-F^*)/w}|\psi(\alpha)+\psi(\alpha^w)|^2.\end{aligned}
$$

第三项可写成

$$
\begin{aligned}
&\frac12(q^2+q)\sum_{\alpha\in A-F^*}(\psi(\alpha)+\psi(\alpha^w))(\psi(\alpha^{-1})+\psi(\alpha^{-w}))\\
&\qquad=\frac12(q^2+q)\sum_{\alpha\in A-F^*}(1+1+\psi(\alpha^{1-w})+\psi(\alpha^{w-1})).
\end{aligned}
$$

将对 $\alpha\in A-F^*$ 的和写成对 $\alpha\in A$ 的和减去对<span class="original-page-anchor" id="pdf-page-729" aria-hidden="true"></span>$\alpha\in F^*$ 的和。若 $\alpha\in F^*$，则 $\alpha^{1-w}=\alpha^{w-1}=1$。由对 $\psi$ 的假设，特征标

$$
\alpha\longmapsto\psi(\alpha^{1-w})\quad\text{其中 }\alpha\in A
$$

非平凡，所以对 $\alpha\in A$ 的和等于 $0$。综合这些说明，第三项等于

$$
\frac12(q^2+q)[2(q-1)^2-2(q-1)-2(q-1)]=q(q^2-1)(q-3).
$$

最后得到

$$
\begin{aligned}\sum_{\beta\in G}|\psi^G(\beta)|^2&=(q+1)(q^2-1)+(q-1)(q^2-1)+q(q^2-1)(q-3)\\&=q(q-1)(q^2-1)=\#(G),\end{aligned}
$$

从而证明 $\psi^G$ 是单的。

最后，第三类特征标有 $\frac12(q-1)(q-2)$ 个。这等于满足 $[w]\psi\neq\psi$ 的特征标 $\psi$ 的个数除以 $2$，因为每对 $\psi$ 与 $[w]\psi$ 给出相同的诱导特征标 $\psi^G$。值表说明，除了这种重合之外，诱导特征标互不相同。

### 第四类

以 $\theta:K^*\longrightarrow\mathbf C^*$ 表示同态，并将其看成 $C=C_K$ 上的特征标。

由命题 12.3，存在元素 $w\in N(C)$ 而 $w\notin C$，且 $w=w^{-1}$。于是

$$
\alpha\longmapsto w\alpha w=[w]\alpha
$$

是 $C$ 的自同构，而 $x\longmapsto wxw$ 也是 $F[C]\approx K$ 在 $F$ 上的域自同构。由于 $[K:F]=2$，由 $w$ 作共轭就是自同构 $\alpha\longmapsto\alpha^q$。由此得到共轭特征标 $[w]\theta$，满足

$$
([w]\theta)(\alpha)=\theta([w]\alpha)=\theta(\alpha^w),
$$

并得到诱导特征标

$$
\theta^G=\operatorname{ind}_C^G(\theta)=\operatorname{ind}_C^G([w]\theta).
$$

设 $\mu:F^*\longrightarrow\mathbf C^*$ 为第一类中那样的同态。令：

$\lambda:F^+\longrightarrow\mathbf C^*$ 为非平凡同态。

$(\mu,\lambda)=$ 满足下式的 $ZU$ 上的特征标：

$$
(\mu,\lambda)\begin{pmatrix}a&ax\\0&a\end{pmatrix}=\mu(a)\lambda(x).
$$

$$
(\mu,\lambda)^G=\operatorname{ind}_{ZU}^G(\mu,\lambda).
$$

<span class="original-page-anchor" id="pdf-page-730" aria-hidden="true"></span>

与前面性质相同的例行计算给出诱导特征标 $\theta^G$ 和 $(\mu,\lambda)^G$ 的以下值。

$$
\begin{array}{|c|c|c|c|c|}\hline
\chi&\begin{pmatrix}a&0\\0&a\end{pmatrix}&\begin{pmatrix}a&1\\0&a\end{pmatrix}&\begin{pmatrix}a&0\\0&d\end{pmatrix}_{d\neq a}&\alpha\in C-F^*\\\hline
\theta^G&(q^2-q)\theta(a)&0&0&\theta(\alpha)+\theta(\alpha^w)\\\hline
(\mu,\lambda)^G&(q^2-1)\mu(a)&-\mu(a)&0&0\\\hline
\end{array}
$$

这些是中间步骤。注意，由 Frobenius 互反律直接计算可知，$\theta^G$ 出现在特征标 $(\operatorname{res}\theta,\lambda)^G$ 中，其中 $\operatorname{res}\theta$ 是在群 $F^*$ 上的限制，故为上述某个特征标 $\mu$。因此定义：

$$
\theta'=(\operatorname{res}\theta,\lambda)^G-\theta^G=([w]\theta)',
$$

它是有效特征标。若 $\theta$ 满足 $\theta\neq[w]\theta$，则称特征标 $\theta'$ 属于**第四类**。这些就是我们要找的特征标。利用中间值表，得到第四类特征标的值表。

**表 12.5(IV)**

$$
\begin{array}{|c|c|c|c|c|}\hline
\chi&\begin{pmatrix}a&0\\0&a\end{pmatrix}&\begin{pmatrix}a&1\\0&a\end{pmatrix}&\begin{pmatrix}a&0\\0&d\end{pmatrix}_{d\neq a}&\alpha\in C-F^*\\\hline
\begin{gathered}\theta'\\\theta\neq[w]\theta\end{gathered}&(q-1)\theta(a)&-\theta(a)&0&-\theta(\alpha)-\theta(\alpha^w)\\\hline
\end{array}
$$

我们断言第四类特征标 $\theta'$ 是单的。

**译校注：** 上段原文在尚未提出 $\theta\ne[w]\theta$ 的条件时，就称 $\theta^G$ 出现在 $(\operatorname{res}\theta,\lambda)^G$ 中并称差 $\theta'$ 为有效特征标；这两个断言须在随后定义的第四类条件下理解，不能用于任意 $\theta$。例如 $q=2$ 时 $G\cong S_3$、$C\cong C_3$，取 $\theta=1_C$，则 $\theta^G=1_G+\mathrm{sgn}$，而非平凡 $\lambda$ 所给的 $(1,\lambda)^G=\mathrm{sgn}+\chi_2$，故差为 $\chi_2-1_G$，不是有效特征标。这里 $\chi_2$ 是二维不可约特征标。原文保留，以说明条件的适用范围。

为证明此断言，计算

$$
\begin{aligned}\sum_{\beta\in G}|\theta'(\beta)|^2&=(q-1)^2(q-1)+(q-1)(q^2-1)\\&\quad+\frac12(q^2-q)\sum_{\alpha\in K^*-F^*}|\theta(\alpha)+\theta(\alpha^w)|^2.\end{aligned}
$$

使用与第三类特征标相同的展开方式，最终的值确为 $\#(G)$，从而证明 $\theta'$ 为单特征标。

值表还说明第四类中不同的特征标有 $\frac12\#(C-F^*)=\frac12(q^2-q)$ 个。这样就得到计算的最终结果。

<span class="original-page-anchor" id="pdf-page-731" aria-hidden="true"></span>

**定理 12.6.** $G=\mathrm{GL}_2(F)$ 的不可约特征标如下。

$$
\begin{array}{|c|l|c|c|}\hline
\text{类型}&&\text{该类型的个数}&\text{维数}\\\hline
\mathrm I&\mu\circ\det&q-1&1\\\hline
\mathrm{II}&\psi_\mu^G-\mu\circ\det&q-1&q\\\hline
\mathrm{III}&\psi^G\text{ 来自配对 }\psi\neq[w]\psi&\frac12(q-1)(q-2)&q+1\\\hline
\mathrm{IV}&\theta'\text{ 来自配对 }\theta\neq[w]\theta&\frac12(q-1)q&q-1\\\hline
\end{array}
$$

**证明。** 已列出四种类型的特征标。每种情形中，由构造立即得到该类型中所列个数的不同特征标。诱导特征标的维数等于诱导所来自子群的指数，由此立即计算出所列维数；其中两种情形须减去某些项，以使该类型的特征标成为单特征标。最终结果如上表所示。列出的特征标总数恰等于表 12.4 中类的个数，因此已找到全部单特征标。定理得证。

## 习题

**1. 群 $S_3$。** 设 $S_3$ 为 $3$ 个元素上的对称群。

(a) 证明有三个共轭类。

(b) 在 $S_3/A_3$ 上有两个维数为 $1$ 的特征标。

(c) 设 $d_i$（$i=1,2,3$）为不可约特征标的维数。由于 $\sum d_i^2=6$，第三个不可约特征标的维数为 $2$。证明可通过考虑三次方程 $X^3+aX+b=0$ 来实现第三个表示，其中此方程在域 $k$ 上的伽罗瓦群为 $S_3$。设 $V$ 为其根生成的 $k$-向量空间。证明此空间为二维，并给出所需表示，而且与 $k^a$ 作张量积后仍不可约。

(d) 设 $G=S_3$。为 $\mathbf C[G]$ 的每个单分量写出一个幂等元。$G$ 的每个不可约表示在 $\mathbf C[G]$ 上的正则表示中的重数是多少？

<span class="original-page-anchor" id="pdf-page-732" aria-hidden="true"></span>

**2. 群 $S_4$ 与 $A_4$。** 设 $S_4$ 为 $4$ 个元素上的对称群。

(a) 证明有 $5$ 个共轭类。

(b) 证明 $A_4$ 有唯一的四阶子群，它不是循环群，且在 $S_4$ 中正规。证明商群与 $S_3$ 同构，所以习题 1 的表示给出 $S_4$ 的表示。

(c) 利用关系 $\sum d_i^2=\#(S_4)=24$，得出 $S_4$ 只有另外两个不可约特征标，每个的维数为 $3$。

(d) 设 $X^4+a_2X^2+a_1X+a_0$ 是域 $k$ 上的不可约多项式，伽罗瓦群为 $S_4$。证明其根在 $k$ 上生成三维向量空间 $V$，且 $S_4$ 在此空间上的表示不可约，于是得到两个尚缺的表示之一。

(e) 设 $\rho$ 为 (d) 中的表示，定义 $\rho'$ 为

$$
\rho'(\sigma)=\rho(\sigma)\quad\text{若 }\sigma\text{ 为偶置换；}
$$

$$
\rho'(\sigma)=-\rho(\sigma)\quad\text{若 }\sigma\text{ 为奇置换。}
$$

证明 $\rho'$ 也不可约，与 $k^a$ 作张量积后仍不可约，并且与 $\rho$ 不同构。这就完成 $S_4$ 的全部不可约表示的描述。

(f) 证明 $S_4$ 的三维不可约表示给出 $A_4$ 的不可约表示。

(g) 证明 $A_4$ 的全部不可约表示由 (f) 中的表示及另外三个一维表示给出。

**3. 四元数群。** 设 $Q=\{\pm1,\pm x,\pm y,\pm z\}$ 为四元数群，其中 $x^2=y^2=z^2=-1$，且 $xy=-yx$、$xz=-zx$、$yz=-zy$。

(a) 证明 $Q$ 有 $5$ 个共轭类。

令 $A=\{\pm1\}$。则 $Q/A$ 的类型为 $(2,2)$，因而有 $4$ 个单特征标，可看成 $Q$ 的单特征标。

(b) 证明 $Q$ 只有另外一个单特征标，其维数为 $2$。证明相应表示可给成如下矩阵表示：

$$
\rho(x)=\begin{pmatrix}i&0\\0&-i\end{pmatrix},\quad\rho(y)=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\quad\rho(z)=\begin{pmatrix}0&i\\i&0\end{pmatrix}.
$$

(c) 设 $\mathbf H$ 为四元数域，即在 $\mathbf R$ 上维数为 $4$ 的代数，其基如习题 3，为 $\{1,x,y,z\}$，关系如上。证明 $\mathbf C\otimes_{\mathbf R}\mathbf H\approx\operatorname{Mat}_2(\mathbf C)$（$2\times2$ 复矩阵），并将此与 (b) 联系起来。

**4.** 设 $S$ 为 $G$ 的正规子群，$\psi$ 为 $S$ 在 $\mathbf C$ 上的单特征标。证明 $\operatorname{ind}_S^G(\psi)$ 是单的，当且仅当对所有 $\sigma\in G-S$ 有 $\psi\neq[\sigma]\psi$。〔译校注：原文条件印作“对所有 $\sigma\in S$ 有 $\psi=[\sigma]\psi$”；此条件对 $S$ 的类函数自动成立。正规子群的诱导表示单性判别要求它与所有来自 $S$ 外元素的共轭特征标不同，因此应为这里所写的条件。〕

**5.** 设 $G$ 为有限群，$S$ 为正规子群，$\rho$ 为 $G$ 在 $\mathbf C$ 上的不可约表示。证明：或者 $\rho$ 在 $S$ 上的限制的所有不可约分量彼此 $S$-同构，或者存在 $G$ 的真子群 $H$，包含 $S$，以及 $H$ 的不可约表示 $\theta$，使 $\rho\approx\operatorname{ind}_H^G(\theta)$。

**6. 二面体群 $D_{2n}$。** 存在阶为 $2n$ 的群（$n$ 为 $\geq2$ 的偶整数），由两个元素 $\sigma,\tau$ 生成，满足

<span class="original-page-anchor" id="pdf-page-733" aria-hidden="true"></span>

$$
\sigma^n=1,\quad\tau^2=1,\quad\text{且}\quad\tau\sigma\tau=\sigma^{-1}.
$$

它称为**二面体群**。

(a) 证明有四个一维表示，来自 $\sigma$ 和 $\tau$ 各取 $\pm1$ 的四种选择。

(b) 设 $C_n$ 为 $D_{2n}$ 中由 $\sigma$ 生成的循环子群。对每个整数 $r=0,\ldots,n-1$，设 $\psi_r$ 为满足下式的 $C_n$ 的特征标：

$$
\psi_r(\sigma)=\zeta^r\qquad(\zeta=\text{本原 }n\text{ 次单位根})。
$$

设 $\chi_r$ 为诱导特征标。证明 $\chi_r=\chi_{n-r}$。

(c) 证明对 $0<r<n/2$，诱导特征标 $\chi_r$ 为单特征标，维数为 $2$，由此得到 $(n/2-1)$ 个不同的二维特征标。

(d) 证明 (a) 和 (c) 的单特征标给出 $D_{2n}$ 的全部单特征标。

**7.** 设 $G$ 为有限群，是 $A,H$ 的半直积，其中 $A$ 交换且正规。令 $A^\wedge=\operatorname{Hom}(A,\mathbf C^*)$ 为对偶群。令 $G$ 通过共轭作用于特征标，即对 $\sigma\in G$、$a\in A$，有

$$
[\sigma]\psi(a)=\psi(\sigma^{-1}a\sigma).
$$

设 $\psi_1,\ldots,\psi_r$ 为 $H$ 在 $A^\wedge$ 中的轨道代表元，$H_i$（$i=1,\ldots,r$）为 $\psi_i$ 的迷向群。令 $G_i=AH_i$。

(a) 对 $a\in A$ 和 $h\in H_i$，定义 $\psi_i(ah)=\psi_i(a)$。证明这样将 $\psi_i$ 延拓为 $G_i$ 的特征标。

设 $\theta$ 为 $H_i$ 的单表示（在 $\mathbf C$ 上的向量空间上）。由 $H_i=G_i/A$，将 $\theta$ 看成 $G_i$ 的单表示。令

$$
\rho_{i,\theta}=\operatorname{ind}_{G_i}^G(\psi_i\otimes\theta).
$$

(b) 证明 $\rho_{i,\theta}$ 为单表示。

(c) 证明 $\rho_{i,\theta}\approx\rho_{i',\theta'}$ 蕴含 $i=i'$ 且 $\theta\approx\theta'$。

(d) 证明 $G$ 的每个不可约表示都与某个 $\rho_{i,\theta}$ 同构。

**8.** 设有限群 $G$ 作用于有限集合 $S$。令 $\mathbf C[S]$ 为 $S$ 在 $\mathbf C$ 上生成的向量空间，$\psi$ 为 $G$ 在 $\mathbf C[S]$ 上相应表示的特征标。

(a) 设 $\sigma\in G$。证明 $\psi(\sigma)=$ $\sigma$ 在 $S$ 中的不动点个数。

(b) 证明 $\langle\psi,1_G\rangle_G$ 是 $S$ 中 $G$-轨道的个数。

**9.** 设 $A$ 为有限群 $G$ 的交换子群。证明 $G$ 在 $\mathbf C$ 上的每个不可约表示的维数 $\leq(G:A)$。

**10.** 设 $F$ 为有限域，$G=\mathrm{SL}_2(F)$。令 $B$ 为 $G$ 中由所有如下矩阵构成的子群：

$$
\alpha=\begin{pmatrix}a&b\\0&d\end{pmatrix}\in\mathrm{SL}_2(F),\quad\text{故 }d=a^{-1}.
$$

设 $\mu:F^*\longrightarrow\mathbf C^*$ 为同态，$\psi_\mu:B\longrightarrow\mathbf C^*$ 为满足 $\psi_\mu(\alpha)=\mu(a)$ 的同态。证明若 $\mu^2\neq1$，则诱导特征标 $\operatorname{ind}_B^G(\psi_\mu)$ 为单特征标。

<span class="original-page-anchor" id="pdf-page-734" aria-hidden="true"></span>

**11.** 确定 $\mathrm{SL}_2(F)$ 在复数域上的全部单特征标，像正文对 $\mathrm{GL}_2$ 所做的那样，给出这些特征标个数的表及共轭类代表元。

**12.** 注意 $A_5\approx\mathrm{SL}_2(\mathbf F_4)\approx\mathrm{PSL}_2(\mathbf F_5)$。由此验证有 $5$ 个共轭类，其元素的阶分别为 $1,2,3,5,5$；并像正文对 $\mathrm{GL}_2$ 所做的那样，明确写出 $A_5$ 的特征标表。

**13.** 设 $G$ 为 $p$-群，$G\longrightarrow\operatorname{Aut}(V)$ 为特征 $p$ 的域上有限维向量空间的表示。假设此表示不可约。证明此表示平凡，即 $G$ 在 $V$ 上作为恒等映射作用。

**14.** 设 $G$ 为有限群，$C$ 为共轭类。证明以下两条件等价。它们定义了共轭类为**有理的**的含义。

**RAT 1.** 对 $G$ 的所有特征标 $\chi$，当 $\sigma\in C$ 时，$\chi(\sigma)\in\mathbf Q$。

**RAT 2.** 对所有 $\sigma\in C$ 及与 $\sigma$ 的阶互素的 $j$，有 $\sigma^j\in C$。

**15.** 设 $G$ 为群，$H_1,H_2$ 为有限指数子群，$\rho_1,\rho_2$ 分别为 $H_1,H_2$ 在 $R$-模 $F_1,F_2$ 上的表示。令 $M_G(F_1,F_2)$ 为函数 $f:G\longrightarrow\operatorname{Hom}_R(F_1,F_2)$ 构成的 $R$-模，这些函数满足

$$
f(h_2\sigma h_1)=\rho_2(h_2)f(\sigma)\rho_1(h_1),
$$

其中 $\sigma\in G$、$h_i\in H_i$（$i=1,2$）。建立 $R$-模同构

$$
\operatorname{Hom}_{R[G]}(F_1^G,F_2^G)\xrightarrow{\approx}M_G(F_1,F_2).
$$

〔译校注：原文第一式左边印作 $f(h_1\sigma h_2)$，第二式的左边印作 $\operatorname{Hom}_R(F_1^G,F_2^G)$。对应于 $R[G]$-同态 $T$ 的函数可写为 $f(\sigma)=p_2\rho_2^G(\sigma)Tj_1$，其中 $j_1:F_1\to F_1^G$ 为自然包含，$p_2:F_2^G\to F_2$ 为单位陪集分量的投影；由此直接得到这里所写的左右 $H_2,H_1$ 等变条件。左侧 Hom 还必须要求 $G$-等变：例如 $H_1=H_2=\{1\}$、$F_1=F_2=\mathbf C$、$G$ 有限时，原左侧维数为 $|G|^2$，右侧只有 $|G|$。因此这里改为 $R[G]$-同态。〕

这里以 $F_i^G$ 简记 $\operatorname{ind}_{H_i}^G(F_i)$。

**16.** (a) 设 $G_1,G_2$ 为两个有限群，分别在 $\mathbf C$-空间 $E_1,E_2$ 上有表示。设 $E_1\otimes E_2$ 为通常的 $\mathbf C$ 上张量积；证明在此张量积上存在 $G_1\times G_2$ 的作用，满足

$$
(\sigma_1,\sigma_2)(x\otimes y)=\sigma_1x\otimes\sigma_2y\quad\text{对 }\sigma_1\in G_1,\ \sigma_2\in G_2.
$$

此作用称为另外两个作用的**张量积**。若 $\rho_1,\rho_2$ 分别为 $G_1,G_2$ 在 $E_1,E_2$ 上的表示，则其张量积记为 $\rho_1\otimes\rho_2$。证明：若 $\rho_1,\rho_2$ 不可约，则 $\rho_1\otimes\rho_2$ 也不可约。〔译校注：原文最后一个张量积印作 $\rho_2\otimes\rho_2$；本题刚定义的是 $G_1\times G_2$ 上的 $\rho_1\otimes\rho_2$，故应为后者。〕〔*提示：*使用定理 5.17。〕

(b) 设 $\chi_1,\chi_2$ 分别为 $\rho_1,\rho_2$ 的特征标。证明 $\chi_1\otimes\chi_2$ 为张量积的特征标。按定义，

$$
\chi_1\otimes\chi_2(\sigma_1,\sigma_2)=\chi_1(\sigma_1)\chi_2(\sigma_2).
$$

**17.** 使用与习题 16 相同的记号，证明 $G_1\times G_2$ 在 $\mathbf C$ 上的每个不可约表示都与习题 16 中那样的张量积表示同构。〔*提示：*证明若特征标与习题 16(b) 中所有乘积 $\chi_1\otimes\chi_2$ 都正交，则该特征标为 $0$。〕

### 张量积表示

**18.** 设 $P$ 为域 $k$ 上 $n$ 个变元的非交换多项式代数。设 $x_1,\ldots,x_r$ 为 $P_1$ 中互不相同的元素（即变元 $t_1,\ldots,t_n$ 的线性表达式），<span class="original-page-anchor" id="pdf-page-735" aria-hidden="true"></span>并设 $a_1,\ldots,a_r\in k$。若对所有整数 $\nu=1,\ldots,r$，有

$$
a_1x_1^\nu+\cdots+a_rx_r^\nu=0,
$$

证明对 $i=1,\ldots,r$ 有 $a_i=0$。〔*提示：*取到交换多项式代数的同态，并在那里论证。〕

**19.** 设 $G$ 为域 $k$ 上有限维向量空间 $E$ 的自同态组成的有限集合。对每个 $\sigma\in G$，设 $c_\sigma\in k$。证明若对所有整数 $r\geq1$ 都有

$$
\sum_{\sigma\in G}c_\sigma T^r(\sigma)=0,
$$

则对所有 $\sigma\in G$ 都有 $c_\sigma=0$。〔*提示：*使用上一题及第十六章命题 7.2。〕

**20.（Steinberg）。** 设 $G$ 为有限幺半群，$k[G]$ 为域 $k$ 上的幺半群代数，$G\longrightarrow\operatorname{End}_k(E)$ 为忠实表示（即单射），因此将 $G$ 与 $\operatorname{End}_k(E)$ 的乘法子集等同。证明 $T^r$ 诱导 $G$ 在 $T^r(E)$ 上的表示，进而由线性性得到 $k[G]$ 在 $T^r(E)$ 上的表示。若 $\alpha\in k[G]$，且对所有整数 $r\geq1$ 有 $T^r(\alpha)=0$，证明 $\alpha=0$。〔*提示：*应用上一题。〕

**译校注：** 习题 18–20 的原文都只取正次数，但没有排除零元。这时断言有例外：习题 18 取 $r=1,x_1=0,a_1=1$；习题 19 取 $G=\{0\}$、$c_0=1$，其中 $0$ 为零自同态，均满足全部所列等式而系数不为零。习题 20 取幺半群 $G=\{1,z\}$，$z^2=z$，在 $E=k$ 上忠实表示为 $1\mapsto\mathrm{id}$、$z\mapsto0$，则非零的幺半群代数基元 $\alpha=[z]$ 被所有正次张量幂表示湮灭。若保持原文的次数范围，须分别要求各 $x_i$ 非零、$G$ 不含零自同态，以及幺半群表示的像不含零自同态；另一处理方式是把零次张量幂及相应零次方条件也列入。此处保留原题及原次数，明确这一条件限制。

**21.（Burnside）。** 由习题 20 推出 Burnside 的如下定理：设 $G$ 为有限群，$k$ 为特征与 $G$ 的阶互素的域，$E$ 为有限维 $(G,k)$-空间，且 $G$ 的表示忠实。则 $G$ 的每个不可约表示都以 $\geq1$ 的重数出现在某个张量幂 $T^r(E)$ 中。

**22.** 设 $X(G)$ 为有限群 $G$ 的特征标环，由 $\mathbf C$ 上的单特征标在 $\mathbf Z$ 上生成。证明元素 $f\in X(G)$ 是有效不可约特征标，当且仅当 $\langle f,f\rangle_G=1$ 且 $f(1)\geq0$。

**23.** 本题假定已学习下一章的交替积。设 $\rho$ 为 $G$ 在 $\mathbf C$ 上向量空间 $E$ 的不可约表示。由函子性，有相应表示 $S^r(\rho)$ 和 $\bigwedge^r(\rho)$，分别在 $E$ 的 $r$ 次对称幂和 $r$ 次交替幂上。若 $\chi$ 为 $\rho$ 的特征标，令 $S^r(\chi)$ 和 $\bigwedge^r(\chi)$ 分别为 $S^r(E)$ 和 $\bigwedge^r(E)$ 上表示 $S^r(\rho)$ 和 $\bigwedge^r(\rho)$ 的特征标。设 $t$ 为变元，令

$$
\sigma_t(\chi)=\sum_{r=0}^\infty S^r(\chi)t^r,\qquad\lambda_t(\chi)=\sum_{r=0}^\infty\bigwedge^r(\chi)t^r.
$$

(a) 与第十四章习题 24 比较，证明对 $x\in G$，有

$$
\sigma_t(\chi)(x)=\det(I-\rho(x)t)^{-1}\quad\text{及}\quad\lambda_t(\chi)(x)=\det(I+\rho(x)t).
$$

(b) 对 $G$ 上的函数 $f$，以 $\Psi^n(f)(x)=f(x^n)$ 定义 $\Psi^n(f)$。证明

$$
t\frac d{dt}\log\sigma_t(\chi)=\sum_{n=1}^\infty\Psi^n(\chi)t^n\quad\text{及}\quad-t\frac d{dt}\log\lambda_{-t}(\chi)=\sum_{n=1}^\infty\Psi^n(\chi)t^n.
$$

〔译校注：原文两个左边分别印作 $-\frac d{dt}\log\sigma_t(\chi)$ 和 $-\frac d{dt}\log\lambda_{-t}(\chi)$。由 (a) 对行列式取对数并展开，导数的右边具有 $t^{n-1}$；与原文所写的 $t^n$ 对应时，左边应分别为 $t\frac d{dt}\log\sigma_t(\chi)$ 和 $-t\frac d{dt}\log\lambda_{-t}(\chi)$。〕

(c) 证明

$$
nS^n(\chi)=\sum_{r=1}^n\Psi^r(\chi)S^{n-r}(\chi)\quad\text{及}\quad n\bigwedge^n(\chi)=\sum_{r=1}^n(-1)^{r-1}\Psi^r(\chi)\bigwedge^{n-r}(\chi).
$$

〔译校注：原文第二个和的上限印作 $\infty$；比较 $t^n$ 的系数时只能有 $1\leq r\leq n$，且本题未定义负次数的交替幂，故上限应为 $n$。〕

<span class="original-page-anchor" id="pdf-page-736" aria-hidden="true"></span>

**24.** 设 $\chi$ 为 $G$ 的单特征标。证明 $\Psi^n(\chi)$ 也是单特征标。（特征标在 $\mathbf C$ 上。）

〔译校注：原题未限制 $n$，一般情形下该断言不成立。例如取 $G=S_3$ 的二维标准特征标 $\chi$ 和 $n=2$，有 $\Psi^2(\chi)=1-\operatorname{sgn}+\chi$，不是单特征标。若 $n$ 与 $|G|$ 互素，则将单位根映到其 $n$ 次幂的圆分域自同构将不可约特征标置换，因而该断言成立。此处保留原题，并指出这个充分条件。〕

**25.** 现在假设已学习第二十章 §3。

(a) 证明该节为 $\operatorname{Mod}_{\mathbf C}(G)$ 定义的 Grothendieck 环与特征标环 $X(G)$ 自然同构。

(b) 将上述公式与第二十章定理 3.12 联系起来。

(c) 阅读 Fulton–Lang 的 *Riemann-Roch Algebra* 第一章，特别是 §6，证明 $X(G)$ 为 $\lambda$-环，$\Psi^n$ 为 Adams 运算。

*说明。* 关于与同调及群上同调的更多联系，见第二十章 §3 及该节末所列参考文献。

**26.** 以下形式体系是数论中 Artin 的 $L$-级数形式体系的类似物。参见 Artin 的“Zur Theorie der L-Reihen mit allgemeinen Gruppencharakteren”（载 *Collected papers*），以及 S. Lang 的“L-series of a covering”，*Proc. Nat. Acad. Sc. USA* (1956)。关于分析背景下的 Artin 形式体系，见 J. Jorgenson 和 S. Lang 的“Artin formalism and heat kernels”，*J. reine angew. Math.* **447** (1994)，165–200 页。

考虑对象为 $\{U\}$ 的范畴。照例，若给定同态 $\rho:G\longrightarrow\operatorname{Aut}(U)$，则称有限群 $G$ 作用于 $U$。此时称 $U$ 为 $G$-对象，也称 $\rho$ 为 $G$ 在 $U$ 中的表示。若 $\rho(G)=\mathrm{id}$，则称 $G$ 平凡地作用。为简便起见，在记号中略去 $\rho$。$G$-对象之间的 $G$-态射 $f:U\longrightarrow V$ 是指满足对所有 $\sigma\in G$ 都有 $f\circ\sigma=\sigma\circ f$ 的态射。

假设对每个 $G$-对象 $U$，存在 $G$ 在其上平凡作用的对象 $U/G$，以及 $G$-态射 $\pi_{U,G}:U\longrightarrow U/G$，具有如下泛性质：若 $f:U\longrightarrow U'$ 为 $G$-态射，则存在唯一态射

$$
f/G:U/G\longrightarrow U'/G,
$$

使下图交换：

$$
\begin{array}{ccc}U&\xrightarrow{f}&U'\\\downarrow&&\downarrow\\U/G&\xrightarrow{f/G}&U'/G\end{array}
$$

特别地，若 $H$ 是 $G$ 的正规子群，证明 $G/H$ 自然作用于 $U/H$。

设 $k$ 为特征 $0$ 的代数闭域。假设给定从此范畴到有限维 $k$-空间范畴的函子 $E$。若 $U$ 是此范畴的对象，$f:U\longrightarrow U'$ 是态射，则得到同态

$$
E(f)=f_*:E(U)\longrightarrow E(U').
$$

（读者可记住一个特殊情形：考虑合适的拓扑空间范畴，$E$ 是给定维数的同调函子。）

若 $G$ 作用于 $U$，则由函子性得到 $G$ 在 $E(U)$ 上的作用。

设 $U$ 为 $G$-对象，$F:U\longrightarrow U$ 为 $G$-态射。若 $P_F(t)=\prod(t-\alpha_i)$ 为线性映射 $F_*:E(U)\longrightarrow E(U)$ 的特征多项式，定义

$$
Z_F(t)=\prod(1-\alpha_i t),
$$

<span class="original-page-anchor" id="pdf-page-737" aria-hidden="true"></span>

称其为 $F$ 的泽塔函数。若 $F$ 为恒等映射，则 $Z_F(t)=(1-t)^{B(U)}$，其中定义 $B(U)=\dim_kE(U)$。

设 $\chi$ 为 $G$ 的单特征标，$d_\chi$ 为 $G$ 对应于 $\chi$ 的单表示的维数，$n=\operatorname{ord}(G)$。在 $E(U)$ 上定义线性映射

$$
e_\chi=\frac{d_\chi}n\sum_{\sigma\in G}\chi(\sigma^{-1})\sigma_*.
$$

证明 $e_\chi^2=e_\chi$，且对任意正整数 $\mu$，有 $(e_\chi\circ F_*)^\mu=e_\chi\circ F_*^\mu$。

若 $P_\chi(t)=\prod(t-\beta_j(\chi))$ 为 $e_\chi\circ F_*$ 的特征多项式，定义

$$
L_F(t,\chi,U/G)=\prod(1-\beta_j(\chi)t).
$$

证明此函数的对数导数等于

$$
-\sum_{\mu=1}^\infty\operatorname{tr}(e_\chi\circ F_*^\mu)t^{\mu-1}.
$$

〔译校注：原文式前的系数印作 $-1/N$，本题未定义 $N$。由刚定义的 $L_F=\prod_j(1-\beta_j(\chi)t)$，其对数导数为 $-\sum_{\mu\geq1}(\sum_j\beta_j(\chi)^\mu)t^{\mu-1}$；内和等于 $\operatorname{tr}((e_\chi\circ F_*)^\mu)=\operatorname{tr}(e_\chi\circ F_*^\mu)$，故此定义下应无因子 $1/N$。〕

对任意特征标 $\chi$，由线性性定义 $L_F(t,\chi,U/G)$。若滥用记号写成 $V=U/G$，则也记作 $L_F(t,\chi,U/V)$。因此对任意 $\chi,\chi'$，按定义有

$$
L_F(t,\chi+\chi',U/V)=L_F(t,\chi,U/V)L_F(t,\chi',U/V).
$$

对上述情形再作一个附加假设：

假设

$$
\frac1n\sum_{\sigma\in G}\sigma_*\circ F_*
$$

的特征多项式等于 $F/G$ 在 $E(U/G)$ 上的特征多项式。证明以下陈述：

(a) 若 $G=\{1\}$，则

$$
L_F(t,1,U/U)=Z_F(t).
$$

(b) 设 $V=U/G$。则

$$
L_F(t,1,U/V)=Z_F(t).
$$

(c) 设 $H$ 为 $G$ 的子群，$\psi$ 为 $H$ 的特征标。令 $W=U/H$，$\psi^G$ 为从 $H$ 到 $G$ 的诱导特征标。则

$$
L_F(t,\psi,U/W)=L_F(t,\psi^G,U/V).
$$

**译校注：** 本题现写的定义使用 $e_\chi$ 所投影到的整个 $\chi$ 等型分量上的行列式。若另在 $\chi$ 的重数空间上取行列式，前者是后者的 $d_\chi$ 次幂；因而将通常的诱导公式用于（c）时，须核对作用空间与归一化，不能将这两种行列式直接混用。原文没有说明未定义的 $N$ 与何种归一化有关，所以不据此猜写新的 $L_F$ 定义。（b）、（c）及附加特征多项式假设均保留原式，须按本题实际采用的定义核对其适用范围。

(d) 设 $H$ 在 $G$ 中正规。则 $G/H$ 作用于 $U/H=W$。设 $\psi$ 为 $G/H$ 的特征标，$\chi$ 为将 $\psi$ 与典范映射 $G\longrightarrow G/H$ 复合所得的 $G$ 的特征标。令 $\varphi=F/H$ 为在

$$
U/H=W
$$

上诱导的态射。则

$$
L_\varphi(t,\psi,W/V)=L_F(t,\chi,U/V).
$$

(e) 若 $V=U/G$ 且 $B(V)=\dim_kE(V)$，证明 $(1-t)^{B(V)}$ 整除 $(1-t)^{B(U)}$。使用正则特征标确定 $(1-t)^{B(U)}$ 的一个分解。

<span class="original-page-anchor" id="pdf-page-738" aria-hidden="true"></span>

**27.** 在读过第七章的一些内容之后再做此题。关键是：在特征不整除群阶的域上，表示可通过“模素理想约化”得到。设 $G$ 为有限群，$p$ 为不整除 $G$ 的阶的素数。设 $F$ 为有理数域的有限扩张，其代数整数环为 $\mathfrak o_F$。假设 $F$ 足够大，使 $G$ 的所有 $F$-不可约表示与 $\mathbf Q^a=F^a$ 作张量积后仍不可约。设 $\mathfrak p$ 为 $\mathfrak o_F$ 中位于 $p$ 上方的素理想，$\mathfrak o_{\mathfrak p}$ 为相应的局部环。

(a) 证明不可约 $(G,F)$-空间 $V$ 可由一个在 $\mathfrak o_{\mathfrak p}$ 上自由的 $(G,\mathfrak o_{\mathfrak p})$-模 $E$，通过将基环从 $\mathfrak o_{\mathfrak p}$ 扩张为 $F$ 得到，即作张量积，使 $V=E\otimes F$（在 $\mathfrak o_{\mathfrak p}$ 上作张量积）。

(b) 证明 $E$ 模 $\mathfrak p$ 的约化是 $G$ 在特征 $p$ 中的不可约表示。换言之，令 $k=\mathfrak o/\mathfrak p=\mathfrak o_{\mathfrak p}/\mathfrak m_{\mathfrak p}$，其中 $\mathfrak m_{\mathfrak p}$ 是 $\mathfrak o_{\mathfrak p}$ 的极大理想。令 $E(\mathfrak p)=E\otimes k$（在 $\mathfrak o_{\mathfrak p}$ 上作张量积）。证明 $G$ 自然作用于 $E(\mathfrak p)$，且此表示不可约。事实上，若 $\chi$ 为 $G$ 在 $V$ 上的特征标，证明 $\chi$ 也是 $E$ 上的特征标，并且 $\chi\bmod\mathfrak m_{\mathfrak p}$ 是 $E(\mathfrak p)$ 上的特征标。

(c) 证明 $G$ 在特征 $p$ 中的全部不可约特征标都可按 (b) 的方式得到。
