---
title: "第十四章 单个自同态的表示"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第十三章 矩阵与线性映射","link":"/library/volume-86/chapter-013"}
next: {"text":"第十五章 双线性型的结构","link":"/library/volume-86/chapter-015"}
---

# 第十四章 单个自同态的表示

<span class="original-page-anchor" id="pdf-page-562" aria-hidden="true"></span>

这里讨论一个模的一个自同态，实际上讨论的是自由模，尤其是域 $k$ 上的有限维向量空间。我们将得到表示矩阵的若尔当标准形；当 $k$ 代数闭时，它具有特别简单的形式。这将引出关于特征值与特征多项式的讨论。主要定理可以视为主理想整环上的模的一般结构定理的一个例子。在这里，主理想整环就是一元多项式环 $k[X]$。

## §1. 表示

设 $k$ 为交换环，$E$ 为 $k$ 上的模。如通常一样，用 $\operatorname{End}_k(E)$ 表示 $E$ 的 $k$ 自同态环，即从 $E$ 到自身的 $k$ 线性映射组成的环。

设 $R$ 为 $k$ 代数（由环同态 $k\to R$ 给出，它使我们能够将 $R$ 视为 $k$ 模）。$R$ 在 $E$ 中的一个**表示**是指 $k$ 代数同态 $R\to\operatorname{End}_k(E)$，也就是一个环同态

$$
\rho:R\to\operatorname{End}_k(E),
$$

它使下面的图交换：

![表示的交换图](/library/volume-86/diagrams/pdf-0562-representation-triangle.png)

<span class="original-page-anchor" id="pdf-page-563" aria-hidden="true"></span>

[如通常一样，将 $\operatorname{End}_k(E)$ 视为 $k$ 代数；若 $I$ 表示 $E$ 的恒等映射，则由 $a\mapsto aI$ 给出从 $k$ 到 $\operatorname{End}_k(E)$ 的同态。若已经选择了基，也用 $I$ 表示单位矩阵。上下文总会使含义清楚。]

后面将遇到各种类型的环（交换环和非交换环）的若干表示的例子。本章中的环都将是交换的。

注意，$E$ 可以视为 $\operatorname{End}_k(E)$ 模。因此也可将 $E$ 视为 $R$ 模：对 $x\in R$ 和 $v\in E$，用

$$
(x,v)\mapsto\rho(x)v
$$

定义 $R$ 在 $E$ 上的作用。通常写 $xv$ 代替 $\rho(x)v$。

若 $E$ 的子群 $F$ 满足 $RF\subset F$，则称其为 $E$ 的**不变子模**。（它既是 $R$ 不变的，也是 $k$ 不变的。）也称它在该表示下不变。

若 $E\ne0$，且仅有的不变子模为 $0$ 和 $E$ 本身，则称表示为**不可约的**或**单的**。

表示论的目的是确定各种有趣的环的所有表示的结构，并对其不可约表示进行分类。在多数情况下，取 $k$ 为域，它可能代数闭，也可能不代数闭。因此，证明关于表示的定理时的困难，可能来自环 $R$ 的复杂性、域 $k$ 的复杂性、模 $E$ 的复杂性，或三者兼有。

若 $E$ 为 $R$ 子模 $E_i$ 的 $R$ 直和，

$$
E=E_1\oplus\cdots\oplus E_m,
$$

且每个 $E_i$ 都不可约，则称上述表示 $\rho$ 为**完全可约的**或**半单的**。也称 $E$ 完全可约。并非所有表示都完全可约，事实上，本章所考虑的表示一般并非如此。以后将研究某些类型的完全可约表示。

有一种特殊类型的表示将经常出现。设 $v\in E$，并假设 $E=Rv$。也写成 $E=(v)$。此时称 $E$ 为（$R$ 上的）**主模**，并称该表示为**主表示**。若是这种情况，则满足 $xv=0$ 的所有 $x\in R$ 组成 $R$ 的一个左理想 $\mathfrak a$（显然）。由

$$
x\mapsto xv
$$

给出的从 $R$ 到 $E$ 的满映射诱导一个 $R$ 模同构

$$
R/\mathfrak a\to E
$$

（将 $R$ 视为自身上的左模，将 $R/\mathfrak a$ 视为商模）。在这个映射中，$R$ 的单位元 $1$ 对应于 $E$ 的生成元 $v$。

<span class="original-page-anchor" id="pdf-page-564" aria-hidden="true"></span>

在记号上，若 $v_1,\ldots,v_n\in E$，则用 $(v_1,\ldots,v_n)$ 表示由 $v_1,\ldots,v_n$ 生成的 $E$ 的子模。

假设 $E$ 分解为 $R$ 子模的直和

$$
E=E_1\oplus\cdots\oplus E_s.
$$

假设每个 $E_i$ 都是 $k$ 上维数 $\geqq1$ 的自由模。设 $\mathfrak B_1,\ldots,\mathfrak B_s$ 分别为 $E_1,\ldots,E_s$ 在 $k$ 上的基。则 $\{\mathfrak B_1,\ldots,\mathfrak B_s\}$ 为 $E$ 的基。设 $\varphi\in R$，并设 $\varphi_i$ 为 $\varphi$ 在 $E_i$ 上诱导的自同态。令 $M_i$ 为 $\varphi_i$ 相对于基 $\mathfrak B_i$ 的矩阵。则 $\varphi$ 相对于 $\{\mathfrak B_1,\ldots,\mathfrak B_s\}$ 的矩阵 $M$ 形如

![分块对角矩阵](/library/volume-86/diagrams/pdf-0564-block-matrix.png)

这样的矩阵称为分解成了**块** $M_1,\ldots,M_s$。有这样的分解时，对 $\varphi$ 或其矩阵的研究就完全归结为（可以这样说）对这些块的研究。

并非总能得到这样的化简，但经常会出现几乎同样好的情形。设 $E'$ 为 $E$ 的 $R$ 不变子模。假设 $E'$ 在 $k$ 上有基，比如 $\{v_1,\ldots,v_m\}$，且该基可以扩充为 $E$ 的基

$$
\{v_1,\ldots,v_m,v_{m+1},\ldots,v_n\}.
$$

若 $k$ 为域，总是可以这样做。

设 $\varphi\in R$。则 $\varphi$ 相对于这个基的矩阵形如

$$
\begin{pmatrix}M'&*\\0&M''\end{pmatrix}.
$$

事实上，由于 $\varphi$ 将 $E'$ 映入自身，显然左上角得到 $M'$，其下方为零矩阵。此外，对每个 $j=m+1,\ldots,n$，可以写成

$$
\varphi v_j=c_{j1}v_1+\cdots+c_{jm}v_m+c_{j,m+1}v_{m+1}+\cdots+c_{jn}v_n.
$$

> **译校注：** 原印文的左侧为 $\varphi v$，没有下标。该句逐一讨论 $j=m+1,\ldots,n$，右侧的 $c_{ji}$ 是对应第 $j$ 个基向量的坐标，随后又用其转置组成表示矩阵的右侧各列；因此左侧应为 $\varphi v_j$。英文转录保留原印文。

于是矩阵 $(c_{ji})$ 的转置成为表示 $\varphi$ 的矩阵右侧出现的矩阵

$$
\begin{pmatrix}*\\M''\end{pmatrix}.
$$

<span class="original-page-anchor" id="pdf-page-565" aria-hidden="true"></span>

此外，考虑正合列

$$
0\to E'\to E\to E''\to0.
$$

设 $\bar v_{m+1},\ldots,\bar v_n$ 为 $v_{m+1},\ldots,v_n$ 在典范映射 $E\to E''$ 下的像。可以自然地定义线性映射

$$
\varphi'':E''\to E'',
$$

使得对所有 $v\in E$ 有 $\overline{(\varphi v)}=\varphi''(\bar v)$。于是显然，$\varphi''$ 相对于基 $\{\bar v_{m+1},\ldots,\bar v_n\}$ 的矩阵为 $M''$。

> **译校注：** 原印文在此将基写成 $\{\bar v_1,\ldots,\bar v_n\}$。前一页中 $v_1,\ldots,v_m$ 是 $E'$ 的基，故它们在商模 $E''$ 中的像为零，不能列入基；本页上一句也只定义了 $\bar v_{m+1},\ldots,\bar v_n$。因此这里的基应从下标 $m+1$ 开始，中文据此修正，英文保留原印文。

## §2. 关于一个自同态的分解

设 $k$ 为域，$E$ 为 $k$ 上的有限维向量空间，且 $E\ne0$。设 $A\in\operatorname{End}_k(E)$ 为 $E$ 到自身的线性映射。设 $t$ 在 $k$ 上超越。我们将定义多项式环 $k[t]$ 在 $E$ 中的表示。具体地，有一个同态

$$
k[t]\to k[A]\subset\operatorname{End}_k(E),
$$

它通过在多项式中用 $A$ 替换 $t$ 得到。环 $k[A]$ 是由 $A$ 生成的 $\operatorname{End}_k(E)$ 的子环，并且它是交换的，因为 $A$ 的各次幂彼此交换。因此，若 $f(t)$ 为多项式且 $v\in E$，则

$$
f(t)v=f(A)v.
$$

同态 $f(t)\mapsto f(A)$ 的核是 $k[t]$ 的主理想；由于 $k[A]$ 在 $k$ 上有限维，这个理想非零。它由唯一的次数 $>0$、首项系数为 $1$ 的多项式生成。这个多项式称为 $A$ 在 $k$ 上的**极小多项式**，记为 $q_A(t)$。当然，它不一定不可约。

*假设存在元素 $v\in E$，使得 $E=k[t]v=k[A]v$。* 这意味着 $E$ 在 $k$ 上由元素

$$
v,Av,A^2v,\ldots
$$

生成。我们称这样的模为**主模**；若 $R=k[t]$，则可以写成 $E=Rv=(v)$。

若 $q_A(t)=t^d+a_{d-1}t^{d-1}+\cdots+a_0$，则元素

$$
v,Av,\ldots,A^{d-1}v
$$

构成 $E$ 在 $k$ 上的基。这与有限域扩张中相应命题的证明相同。首先注意，它们线性无关，因为任何在 $k$ 上的线性相关关系都会给出一个多项式<span class="original-page-anchor" id="pdf-page-566" aria-hidden="true"></span>$g(t)$，它的次数小于 $\deg q_A$，且满足 $g(A)=0$。其次，它们生成 $E$，因为任意多项式 $f(t)$ 都可写成 $f(t)=g(t)q_A(t)+r(t)$，其中 $\deg r<\deg q_A$。因此 $f(A)=r(A)$。

显然，相对于这个基，$A$ 的矩阵为以下类型：

![极小多项式的友矩阵](/library/volume-86/diagrams/pdf-0566-companion-matrix.png)

若 $E=(v)$ 为主模，则通过映射 $f(t)\mapsto f(A)v$，$E$ 同构于 $k[t]/(q_A(t))$。多项式 $q_A$ 由 $A$ 唯一确定，与 $E$ 的生成元 $v$ 的选择无关。这一点基本上是显然的，因为若 $f_1,f_2$ 为首项系数为 $1$ 的两个多项式，则 $k[t]/(f_1(t))$ 同构于 $k[t]/(f_2(t))$ 当且仅当 $f_1=f_2$。（将每个多项式分解为素幂，并应用主理想整环上的模的结构定理。）

若 $E$ 为主模，则称上述多项式 $q_A$ 为 $E$ 关于 $A$ 的**多项式不变量**，或简称其**不变量**。

**定理 2.1。** *设 $E$ 为域 $k$ 上的非零有限维空间，$A\in\operatorname{End}_k(E)$。则 $E$ 有直和分解*

$$
E=E_1\oplus\cdots\oplus E_r,
$$

*其中每个 $E_i$ 都是主 $k[A]$ 子模，其不变量 $q_i\ne0$ 满足*

$$
q_1\mid q_2\mid\cdots\mid q_r.
$$

*序列 $(q_1,\ldots,q_r)$ 由 $E$ 和 $A$ 唯一确定，且 $q_r$ 是 $A$ 的极小多项式。*

*证明。* 第一个断言只是用当前的语言重新表述主理想整环上的模的结构定理。此外，由于对每个 $i$ 都有 $q_i\mid q_r$，显然 $q_r(A)=0$。次数低于 $q_r$ 的多项式不可能零化 $E$，因为特别地，这样的多项式不零化 $E_r$。因此 $q_r$ 为极小多项式。

称 $(q_1,\ldots,q_r)$ 为二元组 $(E,A)$ 的**不变量**。令 $E=k^{(n)}$，并设 $A$ 为 $n\times n$ 矩阵，将它视为 $E$ 到自身的线性映射。称不变量 $(q_1,\ldots,q_r)$ 为 $A$（在 $k$ 上）的**不变量**。

**推论 2.2。** *设 $k'$ 为 $k$ 的扩域，$A$ 为 $k$ 中的 $n\times n$ 矩阵。$A$ 在 $k$ 上的不变量与它在 $k'$ 上的不变量相同。*

<span class="original-page-anchor" id="pdf-page-567" aria-hidden="true"></span>

*证明。* 设 $\{v_1,\ldots,v_n\}$ 为 $k^{(n)}$ 在 $k$ 上的基。也可以将它视为 $k'^{(n)}$ 在 $k'$ 上的基。（单位向量属于由 $v_1,\ldots,v_n$ 生成的 $k$ 空间；因此 $v_1,\ldots,v_n$ 在 $k'$ 上生成 $n$ 维空间 $k'^{(n)}$。）令 $E=k^{(n)}$。设 $L_A$ 为 $A$ 确定的 $E$ 的线性映射，$L'_A$ 为 $A$ 确定的 $k'^{(n)}$ 的线性映射。$L_A$ 相对于给定基的矩阵与 $L'_A$ 的矩阵相同。可以选取与不变量 $q_1,\ldots,q_r$ 所确定的分解

$$
E=E_1\oplus\cdots\oplus E_r
$$

相对应的基。由此可知，将该基提升为 $k'^{(n)}$ 的基时，不变量不变。

**推论 2.3。** *设 $A,B$ 为域 $k$ 上的 $n\times n$ 矩阵，$k'$ 为 $k$ 的扩域。假设存在 $k'$ 中的可逆矩阵 $C'$，使得 $B=C'AC'^{-1}$。则存在 $k$ 中的可逆矩阵 $C$，使得 $B=CAC^{-1}$。*

*证明。* 留作练习。

主理想整环上的模的结构定理给出两种分解。一种按照前面定理中的不变量进行，另一种按照素幂进行。

设 $E\ne0$ 为域 $k$ 上的有限维空间，$A:E\to E$ 属于 $\operatorname{End}_k(E)$。令 $q=q_A$ 为其极小多项式。则 $q$ 有分解

$$
q=p_1^{e_1}\cdots p_s^{e_s}\quad(e_i\geqq1),
$$

分解为（不同的）素幂。因此 $E$ 为子模的直和

$$
E=E(p_1)\oplus\cdots\oplus E(p_s),
$$

其中每个 $E(p_i)$ 都被 $p_i^{e_i}$ 零化。此外，每个这样的子模都可表示为若干子模的直和，其中每个子模同构于某个 $k[t]/(p^e)$，$p$ 为某个不可约多项式，$e\geqq1$ 为整数。

**定理 2.4。** *设对某个 $\alpha\in k$、$e\geqq1$，有 $q_A(t)=(t-\alpha)^e$。假设 $E$ 同构于 $k[t]/(q)$。则 $E$ 有一个 $k$ 上的基，使 $A$ 相对于这个基的矩阵为以下类型：*

![对角线下方为1的若尔当块](/library/volume-86/diagrams/pdf-0567-jordan-block.png)

<span class="original-page-anchor" id="pdf-page-568" aria-hidden="true"></span>

*证明。* 由于 $E$ 同构于 $k[t]/(q)$，存在元素 $v\in E$，使得 $k[t]v=E$。在同构

$$
k[t]/(q)\to E
$$

中，该元素对应于 $k[t]$ 的单位元。

我们断言，元素

$$
v,(t-\alpha)v,\ldots,(t-\alpha)^{e-1}v,
$$

或等价地，

$$
v,(A-\alpha)v,\ldots,(A-\alpha)^{e-1}v,
$$

构成 $E$ 在 $k$ 上的基。它们在 $k$ 上线性无关，因为任何线性相关关系都将给出元素

$$
v,Av,\ldots,A^{e-1}v
$$

之间的线性相关关系，从而得到一个次数小于 $\deg q$、满足 $g(A)=0$ 的多项式 $g(t)$。由于 $\dim E=e$，这些元素就构成 $E$ 在 $k$ 上的基。而 $(A-\alpha)^e=0$。由定义立即可知，$A$ 相对于这个基的矩阵具有定理中所述的形式。

**推论 2.5。** *设 $k$ 代数闭，$E$ 为 $k$ 上的非零有限维向量空间。设 $A\in\operatorname{End}_k(E)$。则 $E$ 有一个 $k$ 上的基，使 $A$ 相对于这个基的矩阵由若干块组成，且每个块都为定理中描述的类型。*

具有前面推论所述形式的矩阵称为具有**若尔当标准形**。

**注 1。** 若矩阵（或自同态）$N$ 满足：存在整数 $d>0$，使得 $N^d=0$，则称 $N$ 为**幂零的**。可见，在定理 2.4 或推论 2.5 的分解中，矩阵 $M$ 写成

$$
M=B+N,
$$

其中 $N$ 幂零。事实上，$N$ 为三角矩阵（即在对角线上及其上方的系数为零），而 $B$ 为对角矩阵，其对角元素为极小多项式的根。只要域 $k$ 满足极小多项式的所有根都属于 $k$，就总能得到这样的分解。还注意到，矩阵 $N$ 为 $0$ 当且仅当极小多项式的所有根的重数均为 $1$。在这种情况下，若 $n=\dim E$，则矩阵 $M$ 为对角矩阵，对角线上有 $n$ 个元素。

> **译校注：** 原印文最后写作 “with $n$ distinct elements on the diagonal”。极小多项式的根互异只保证可对角化，并不保证这 $n$ 个对角元素互异。例如 $M=I_2$ 的极小多项式为 $t-1$，其根的重数为 $1$，但对角线上两个元素均为 $1$。因此中文不保留“互异”的断言；英文保留原印文。

<span class="original-page-anchor" id="pdf-page-569" aria-hidden="true"></span>

**注 2。** 本节的主要定理也可以视为以下一般模式的一个实例：尽可能将模分解成直和，并针对各种结构给出向量空间的规范化基，从而能够简单地看出一个自同态的作用。更形式化地，考虑二元组 $(E,A)$ 的范畴，其中 $E$ 为域 $k$ 上的有限维向量空间，$A:E\to E$ 为自同态。这样的二元组之间的态射

$$
f:(E,A)\to(E',A')
$$

是指一个 $k$ 同态 $f:E\to E'$，它使下面的图交换：

$$
\begin{array}{ccc}
E&\xrightarrow{f}&E'\\
A\downarrow&&\downarrow A'\\
E&\xrightarrow{f}&E'
\end{array}
$$

立即可见，这样的二元组构成一个范畴，因此有同构的概念。可以将定理 2.1 重新表述为：

**定理 2.6。** *两个二元组 $(E,A)$ 和 $(F,B)$ 同构，当且仅当它们具有相同的不变量。*

可以把这一点作为习题 19 来证明。若尔当基给出了与这样的二元组及一个适当的基相对应的矩阵的规范形式。

下一章将对复数上的厄米算子、对称算子和酉算子，找出使规范化矩阵实际为对角矩阵的条件。

作为定理 2.6 的一个例子和应用，证明：

**推论 2.7。** *设 $k$ 为域，$K$ 为次数为 $n$ 的有限可分扩张。设 $V$ 为 $k$ 上维数为 $n$ 的有限维向量空间，$\rho,\rho':K\to\operatorname{End}_k(V)$ 为 $K$ 在 $V$ 上的两个表示，即 $K$ 到 $\operatorname{End}_k(V)$ 的嵌入。则 $\rho,\rho'$ 共轭，即存在 $B\in\operatorname{Aut}_k(V)$，使得*

$$
\rho'(\xi)=B\rho(\xi)B^{-1}\quad\text{对所有 }\xi\in K.
$$

*证明。* 由域论的本原元定理，存在元素 $\alpha\in K$，使得 $K=k[\alpha]$。设 $p(t)$ 为 $\alpha$ 在 $k$ 上的不可约多项式。则 $(V,\rho(\alpha))$ 和 $(V,\rho'(\alpha))$ 具有相同的不变量，即 $p(t)$。由定理 2.6，这两个二元组同构，意味着存在 $B\in\operatorname{Aut}_k(V)$，使得

$$
\rho'(\alpha)=B\rho(\alpha)B^{-1}.
$$

但 $K$ 的所有元素都是 $\alpha$ 的各次幂的 $k$ 系数线性组合，因此立即得到，对所有 $\xi\in K$ 有 $\rho'(\xi)=B\rho(\xi)B^{-1}$，即得所需结论。

<span class="original-page-anchor" id="pdf-page-570" aria-hidden="true"></span>

为了得到推论 2.7 中那样的 $K$ 的表示，当然可以选择 $K$ 的一个基，并将 $K$ 的元素在 $K$ 上的乘法作用表示为相对于这个基的矩阵。在某种意义上，推论 2.7 告诉我们，这是得到这种表示的唯一方式。在第十八章 §12 讨论 $GL_n$ 的嘉当子群时，将回到这一观点。

## §3. 特征多项式

设 $k$ 为交换环，$E$ 为 $k$ 上维数为 $n$ 的自由模。考虑多项式环 $k[t]$ 及线性映射 $A:E\to E$。如前所述，有一个同态

$$
k[t]\to k[A],
$$

将多项式 $f(t)$ 映到 $f(A)$，从而 $E$ 成为环 $R=k[t]$ 上的模。设 $M$ 为 $k$ 中任意 $n\times n$ 矩阵（例如 $A$ 相对于 $E$ 的一个基的矩阵）。定义**特征多项式** $P_M(t)$ 为行列式

$$
\det(tI_n-M),
$$

其中 $I_n$ 为 $n\times n$ 单位矩阵。它是 $k[t]$ 的元素。此外，若 $N$ 为 $R$ 中的可逆矩阵，则

$$
\det(tI_n-N^{-1}MN)=\det(N^{-1}(tI_n-M)N)=\det(tI_n-M).
$$

因此 $N^{-1}MN$ 的特征多项式与 $M$ 的相同。于是可以定义 $A$ 的特征多项式，并用 $P_A$ 表示 $A$ 相对于某个基的任意表示矩阵 $M$ 的特征多项式。（若 $E=0$，则**定义特征多项式为** $1$。）

若 $\varphi:k\to k'$ 为交换环的同态，且 $M$ 为 $k$ 中的 $n\times n$ 矩阵，则显然

$$
P_{\varphi M}(t)=\varphi P_M(t),
$$

其中 $\varphi P_M$ 由对 $P_M$ 的各系数施加 $\varphi$ 得到。

**定理 3.1（凯莱–哈密顿）。** *有 $P_A(A)=0$。*

*证明。* 设 $\{v_1,\ldots,v_n\}$ 为 $E$ 在 $k$ 上的基。则

$$
tv_j=\sum_{i=1}^{n}a_{ij}v_i,
$$

其中 $(a_{ij})=M$ 为 $A$ 相对于这个基的矩阵。设 $\tilde B(t)$ 为第十三章所定义的、系数属于 $k[t]$ 的矩阵，使得

$$
\tilde B(t)B(t)=P_A(t)I_n.
$$

<span class="original-page-anchor" id="pdf-page-571" aria-hidden="true"></span>

于是

$$
\tilde B(t)B(t)\begin{pmatrix}v_1\\\vdots\\v_n\end{pmatrix}=\begin{pmatrix}P_A(t)v_1\\\vdots\\P_A(t)v_n\end{pmatrix}=\begin{pmatrix}0\\\vdots\\0\end{pmatrix},
$$

因为

$$
B(t)\begin{pmatrix}v_1\\\vdots\\v_n\end{pmatrix}=\begin{pmatrix}0\\\vdots\\0\end{pmatrix}.
$$

因此 $P_A(t)E=0$，从而 $P_A(A)E=0$。这意味着 $P_A(A)=0$，证毕。

现在假设 $k$ 为域。设 $E$ 为 $k$ 上的有限维向量空间，$A\in\operatorname{End}_k(E)$。$A$ 在 $E$ 中的**特征向量** $w$ 是指一个元素 $w\in E$，使得存在元素 $\lambda\in k$ 满足 $Aw=\lambda w$。若 $w\ne0$，则 $\lambda$ 唯一确定，称为 $A$ 的一个**特征值**。当然，不同的特征向量可能具有相同的特征值。

**定理 3.2。** *$A$ 的特征值恰为 $A$ 的特征多项式的根。*

*证明。* 设 $\lambda$ 为一个特征值。则 $A-\lambda I$ 在 $\operatorname{End}_k(E)$ 中不可逆，所以 $\det(A-\lambda I)=0$。因此 $\lambda$ 为 $P_A$ 的根。上述论证可以反过来进行，故也得到逆命题。

为简化记号，经常写 $A-\lambda$ 代替 $A-\lambda I$。

**定理 3.3。** *设 $w_1,\ldots,w_m$ 为 $A$ 的非零特征向量，具有互异的特征值。则它们线性无关。*

*证明。* 假设有

$$
a_1w_1+\cdots+a_mw_m=0,
$$

其中 $a_i\in k$，并令它为系数 $a_i$ 不全为零的最短关系（假设存在这样的关系）。则对所有 $i$ 有 $a_i\ne0$。设 $\lambda_1,\ldots,\lambda_m$ 为这些向量的特征值。对上述关系施加 $A-\lambda_1$，得到

$$
a_2(\lambda_2-\lambda_1)w_2+\cdots+a_m(\lambda_m-\lambda_1)w_m=0,
$$

使关系缩短，产生矛盾。

**推论 3.4。** *若 $A$ 有 $n$ 个互异的特征值 $\lambda_1,\ldots,\lambda_n$，分别对应特征向量 $v_1,\ldots,v_n$，且 $\dim E=n$，则 $\{v_1,\ldots,v_n\}$ 为 $E$ 的基。$A$ 相对于这个基的矩阵* <span class="original-page-anchor" id="pdf-page-572" aria-hidden="true"></span>*为对角矩阵：*

$$
\begin{pmatrix}
\lambda_1&&&0\\
&\lambda_2&&\\
&&\ddots&\\
0&&&\lambda_n
\end{pmatrix}.
$$

**提醒。** 并非总存在由特征向量组成的 $E$ 的基！

**注。** 设 $k$ 为 $k'$ 的子域。若 $M$ 为 $k$ 中的矩阵，可以定义它关于 $k$ 的特征多项式，也可以定义它关于 $k'$ 的特征多项式。显然，这样得到的特征多项式相等。若 $E$ 为 $k$ 上的向量空间，以后将说明如何将它扩张为 $k'$ 上的向量空间。线性映射 $A$ 扩张为扩张空间上的线性映射，其特征多项式也不变。事实上，若选择 $E$ 在 $k$ 上的基，则 $E\approx k^{(n)}$，且自然地有 $k^{(n)}\subset k'^{(n)}$。因此，选择一个基就能扩张向量空间，但这似乎依赖于基的选择。以后将给出不依赖于选择的定义。

设 $E=E_1\oplus\cdots\oplus E_r$ 为 $E$ 作为 $k$ 上向量空间直和的表达式。设 $A\in\operatorname{End}_k(E)$，并假设对所有 $i=1,\ldots,r$ 有 $AE_i\subset E_i$。于是 $A$ 在 $E_i$ 上诱导线性映射。可以选取由 $E_1,\ldots,E_r$ 的基组成的 $E$ 的基，此时 $A$ 的矩阵由若干块组成。因此有

$$
P_A(t)=\prod_{i=1}^{r}P_{A_i}(t).
$$

所以，特征多项式对于直和具有乘法性。

上述条件 $AE_i\subset E_i$ 也可以表述为：$E$ 表示为 $k[A]$ 子模的 $k[A]$ 直和，或者表示为 $k[t]$ 子模的 $k[t]$ 直和。我们将把这一点应用于定理 2.1 给出的 $E$ 的分解。

**定理 3.5。** *设 $E$ 为域 $k$ 上的有限维向量空间，$A\in\operatorname{End}_k(E)$，$q_1,\ldots,q_r$ 为 $(E,A)$ 的不变量。则*

$$
P_A(t)=q_1(t)\cdots q_r(t).
$$

*证明。* 假设 $E=k^{(n)}$，且 $A$ 由矩阵 $M$ 表示。已经知道，将 $k$ 扩张到更大的域时，不变量不变，特征多项式也不变。因此可以假设 $k$ 代数闭。由定理 2.1，可以假设 $M$ 具有一个<span class="original-page-anchor" id="pdf-page-573" aria-hidden="true"></span>单个不变量 $q$。写成

$$
q(t)=(t-\alpha_1)^{e_1}\cdots(t-\alpha_s)^{e_s},
$$

其中 $\alpha_1,\ldots,\alpha_s$ 互异。将 $M$ 视为线性映射，并将向量空间进一步分解为 $k[t]$ 子模的直和，这些子模的不变量分别为

$$
(t-\alpha_1)^{e_1},\ldots,(t-\alpha_s)^{e_s}
$$

（这就是素幂分解）。对每个这样的子模，可以选择一个基，使诱导线性映射的矩阵具有定理 2.4 中描述的形式。由此立即可见，不变量为 $(t-\alpha)^e$ 的映射的特征多项式恰为 $(t-\alpha)^e$，定理得证。

**推论 3.6。** *$A$ 的极小多项式与其特征多项式具有相同的不可约因子。*

*证明。* 因为由定理 2.1，$q_r$ 是极小多项式。

将前面关于特征多项式对于直和的乘法性的说明推广如下。

**定理 3.7。** *设 $k$ 为交换环，在下图中，*

$$
\begin{array}{ccccccccc}
0&\longrightarrow&E'&\longrightarrow&E&\longrightarrow&E''&\longrightarrow&0\\
&&A'\downarrow&&A\downarrow&&A''\downarrow&&\\
0&\longrightarrow&E'&\longrightarrow&E&\longrightarrow&E''&\longrightarrow&0
\end{array}
$$

*设两行均为 $k$ 上有限维自由模的正合列，垂直映射为使该图交换的 $k$ 线性映射。则*

$$
P_A(t)=P_{A'}(t)P_{A''}(t).
$$

*证明。* 可以假设 $E'$ 为 $E$ 的子模。选取 $E'$ 的基 $\{v_1,\ldots,v_m\}$。设 $\{\bar v_{m+1},\ldots,\bar v_n\}$ 为 $E''$ 的基，并设 $v_{m+1},\ldots,v_n$ 为 $E$ 中分别映到 $\bar v_{m+1},\ldots,\bar v_n$ 的元素。

> **译校注：** 原印文此处写 $\{\bar v_{m+1},\ldots,\bar v\}$，末项未带下标；同一句随后明确列出对应的像 $\bar v_{m+1},\ldots,\bar v_n$，故这里的末项应为 $\bar v_n$。中文补齐下标，英文保留原印文。

于是

$$
\{v_1,\ldots,v_m,v_{m+1},\ldots,v_n\}
$$

为 $E$ 的基（证明同第三章定理 5.2），因此处于 §1 中讨论的情形。$A$ 的矩阵形如

$$
\begin{pmatrix}M'&*\\0&M''\end{pmatrix},
$$

<span class="original-page-anchor" id="pdf-page-574" aria-hidden="true"></span>

其中 $M'$ 为 $A'$ 的矩阵，$M''$ 为 $A''$ 的矩阵。相对于这个矩阵取特征多项式，显然就得到所述的乘法性质。

**定理 3.8。** *设 $k$ 为交换环，$E$ 为 $k$ 上维数为 $n$ 的自由模。设 $A\in\operatorname{End}_k(E)$，并设*

$$
P_A(t)=t^n+c_{n-1}t^{n-1}+\cdots+c_0.
$$

*则*

$$
\operatorname{tr}(A)=-c_{n-1}\quad\text{且}\quad\det(A)=(-1)^nc_0.
$$

*证明。* 对于行列式，注意 $P_A(0)=c_0$。在用行列式定义的特征多项式中代入 $t=0$，得到 $c_0=(-1)^n\det(A)$。

对于迹，设 $M$ 为 $A$ 相对于某个基的表示矩阵，$M=(a_{ij})$。考虑行列式 $\det(tI_n-a_{ij})$。在按置换求和的展开式中，有一个对角项

$$
(t-a_{11})\cdots(t-a_{nn}),
$$

它对 $t^{n-1}$ 的系数的贡献等于

$$
-(a_{11}+\cdots+a_{nn}).
$$

展开式中的其他项对 $t^{n-1}$ 的系数没有贡献，因为其他项中 $t$ 的幂至多为 $t^{n-2}$。这就证明了关于迹的断言。

**推论 3.9。** *设记号同定理 3.7。则*

$$
\operatorname{tr}(A)=\operatorname{tr}(A')+\operatorname{tr}(A'')\quad\text{且}\quad\det(A)=\det(A')\det(A'').
$$

*证明。* 显然。

现在在欧拉–格罗滕迪克群中解释这些结果。

设 $k$ 为交换环。考虑一个范畴，其对象为二元组 $(E,A)$，其中 $E$ 为 $k$ 模，$A\in\operatorname{End}_k(E)$。定义态射

$$
(E',A')\to(E,A)
$$

为使下面的图交换的 $k$ 线性映射 $E'\xrightarrow{f}E$：

$$
\begin{array}{ccc}
E'&\xrightarrow{f}&E\\
A'\downarrow&&\downarrow A\\
E'&\xrightarrow{f}&E
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-575" aria-hidden="true"></span>

于是可以将这样的态射的核也定义为一个二元组。事实上，令 $E'_0$ 为 $f:E'\to E$ 的核。则 $A'$ 将 $E'_0$ 映入自身，因为

$$
fA'E'_0=AfE'_0=0.
$$

令 $A'_0$ 为 $A'$ 在 $E'_0$ 上的限制。定义二元组 $(E'_0,A'_0)$ 为该态射的核。

仍用 $f$ 表示二元组之间的态射 $(E',A')\to(E,A)$。可以谈论正合列

$$
(E',A')\to(E,A)\to(E'',A''),
$$

其含义是诱导的序列

$$
E'\to E\to E''
$$

正合。按照对所有表现得像零元的对象都用符号 $0$ 表示的一贯约定，也写 $0$ 代替 $(0,0)$。

注意，这些二元组现在在形式上像模一样，事实上构成一个阿贝尔范畴。

假设 $k$ 为域。令 $\mathfrak C$ 由所有二元组 $(E,A)$ 组成，其中 $E$ 在 $k$ 上有限维。

*于是定理 3.7 断言，特征多项式是一个欧拉–庞加莱映射，定义于范畴 $\mathfrak C$ 的每个对象，取值于首项系数为 $1$ 的多项式组成的乘法幺半群。*

由于映射取值于幺半群，这稍微推广了第三章 §8 中取值于群的概念。当然，$k$ 为域是最常见的应用，此时可以将映射的值视为属于非零有理函数的乘法群，因此先前的情形适用。

对迹和行列式也有类似说明。*若 $k$ 为域，则迹是到该域加法群的欧拉映射，而行列式是到该域乘法群的欧拉映射。* 还注意到，所有这些映射（如同所有欧拉映射）都定义于二元组的同构类上，并定义于欧拉–格罗滕迪克群上。

> **译校注：** 关于行列式的这两句在上述“所有二元组 $(E,A)$”的范畴中缺少条件：例如一维空间上的零自同态的行列式为 $0$，不属于域的乘法群 $k^*$。对任意自同态，行列式取值于含 $0$ 的乘法幺半群 $(k,\cdot)$，且在正合列上满足乘法性；若限定 $A$ 可逆，则它取值于 $k^*$，并可作为取群值的欧拉映射延伸到相应的欧拉–格罗滕迪克群。原文关于迹和特征多项式的群值说明不受这一问题影响。英文转录保留原印文。

**定理 3.10。** *设 $k$ 为交换环，$M$ 为 $k$ 中的 $n\times n$ 矩阵，$f$ 为 $k[t]$ 中的多项式。假设 $P_M(t)$ 在 $k$ 上有线性因子分解*

$$
P_M(t)=\prod_{i=1}^{n}(t-\alpha_i).
$$

*则 $f(M)$ 的特征多项式由下式给出：*

$$
P_{f(M)}(t)=\prod_{i=1}^{n}(t-f(\alpha_i)),
$$

<span class="original-page-anchor" id="pdf-page-576" aria-hidden="true"></span>

*且*

$$
\operatorname{tr}(f(M))=\sum_{i=1}^{n}f(\alpha_i),\qquad\det(f(M))=\prod_{i=1}^{n}f(\alpha_i).
$$

*证明。* 先假设 $k$ 为域。利用定理 2.4 给出的矩阵的标准分解，立即可见断言成立。当 $k$ 为环时，使用代入论证。不过，需要知道：若 $X=(x_{ij})$ 为系数在 $\mathbf{Z}$ 上代数无关的矩阵，则 $P_X(t)$ 有 $n$ 个互异根 $y_1,\ldots,y_n$［位于 $\mathbf{Q}(X)$ 的一个代数闭包中］，并且存在同态

$$
\mathbf{Z}[x_{ij},y_1,\ldots,y_n]\to k,
$$

将 $X$ 映到 $M$，将 $y_1,\ldots,y_n$ 映到 $\alpha_1,\ldots,\alpha_n$。对已经读过环的整扩张那一章的读者，这一点显然；尚未读过的读者可以暂且不考虑定理的这一部分。

## 习题

**1.** 设 $T$ 为交换环上的上三角方阵（即对角线下方及对角线上的所有元素均为 $0$）。证明 $T$ 幂零。

**2.** 明确写出以下断言的证明：矩阵

![习题2中的矩阵](/library/volume-86/diagrams/pdf-0576-exercise-2-matrix.png)

的行列式等于矩阵 $M_1,\ldots,M_s$ 的行列式的乘积，其中每个 $M_i$ 都为方阵。

**3.** 设 $k$ 为交换环，$M,M'$ 为 $k$ 中的 $n\times n$ 方阵。证明 $MM'$ 和 $M'M$ 的特征多项式相等。

**4.** 证明矩阵

$$
\begin{pmatrix}0&1&0&0\\0&0&1&0\\0&0&0&1\\1&0&0&0\end{pmatrix}
$$

在复数中的特征值为 $\pm1$、$\pm i$。

<span class="original-page-anchor" id="pdf-page-577" aria-hidden="true"></span>

**5.** 设 $M,M'$ 是域 $k$ 上的方阵，$q,q'$ 分别是它们的极小多项式。证明

$$
\begin{pmatrix}M&0\\0&M'\end{pmatrix}
$$

的极小多项式是 $q,q'$ 的最小公倍式。

**6.** 设 $A$ 是域 $k$ 上有限维向量空间 $E$ 的一个幂零自同态。证明 $\operatorname{tr}(A)=0$。

**7.** 设 $R$ 是主理想整环，$E$ 是 $R$ 上的自由模，$E^\vee=\operatorname{Hom}_R(E,R)$ 是它的对偶模。那么 $E^\vee$ 是维数为 $n$ 的自由模。设 $F$ 是 $E$ 的一个子模。证明 $E^\vee/F^\perp$ 可以看成 $F^\vee$ 的一个子模，而且它的不变因子与 $F$ 在 $E$ 中的不变因子相同。

**8.** 设 $E$ 是域 $k$ 上的有限维向量空间，$A\in\operatorname{Aut}_k(E)$。证明下列条件等价：

(a) $A=I+N$，其中 $N$ 幂零。

(b) $E$ 存在一组基，使得 $A$ 关于这组基的矩阵的所有对角元都等于 $1$，而对角线上方的所有元素都等于 $0$。

(c) $A$ 的特征多项式的所有根（在 $k$ 的代数闭包中）都等于 $1$。

**9.** 设 $k$ 是特征为 $0$ 的域，$M$ 是 $k$ 中的一个 $n\times n$ 矩阵。证明 $M$ 幂零当且仅当对于 $1\leqq\nu\leqq n$ 都有 $\operatorname{tr}(M^\nu)=0$。

**10.** 假定 $k$ 是域，把定理 3.10 推广到有理函数（代替多项式）。

**11.** 设 $E$ 是域 $k$ 上的有限维空间，$\alpha\in k$。设 $E_\alpha$ 是由 $E$ 的一个给定自同态 $A$ 的所有以 $\alpha$ 为特征值的特征向量生成的子空间。证明 $E_\alpha$ 的每个非零元素都是 $A$ 的一个以 $\alpha$ 为特征值的特征向量。

**12.** 设 $E$ 是域 $k$ 上的有限维空间，$A\in\operatorname{End}_k(E)$，$v$ 是 $A$ 的一个特征向量。设 $B\in\operatorname{End}_k(E)$ 满足 $AB=BA$。证明 $Bv$ 也是 $A$ 的一个特征向量（如果 $Bv\ne0$），并且具有相同的特征值。

### 可对角化的自同态

设 $E$ 是域 $k$ 上的有限维向量空间，$S\in\operatorname{End}_k(E)$。如果 $E$ 存在一组由 $S$ 的特征向量组成的基，就称 $S$ **可对角化**。此时 $S$ 关于这组基的矩阵是对角矩阵。

**13.** (a) 如果 $S$ 可对角化，那么它在 $k$ 上的极小多项式具有如下形式：

$$
q(t)=\prod_{i=1}^m(t-\lambda_i),
$$

其中 $\lambda_1,\ldots,\lambda_m$ 是 $k$ 中互不相同的元素。

(b) 反过来，如果 $S$ 的极小多项式具有上述形式，那么 $S$ 可对角化。［*提示：* 这个空间可以分解成被 $S-\lambda_i$ 零化的子空间 $E_{\lambda_i}$ 的直和。］

<span class="original-page-anchor" id="pdf-page-578" aria-hidden="true"></span>

(c) 如果 $S$ 可对角化，而 $F$ 是 $E$ 的一个满足 $SF\subset F$ 的子空间，证明 $S$ 作为 $F$ 的自同态也是可对角化的，也就是说，$F$ 有一组由 $S$ 的特征向量组成的基。

(d) 设 $S,T$ 是 $E$ 的自同态，且 $S,T$ 可交换。假定 $S,T$ 都可对角化。证明它们可以同时对角化，也就是说，$E$ 存在一组基，其中的每个向量都是 $S$ 和 $T$ 的特征向量。［*提示：* 如果 $\lambda$ 是 $S$ 的一个特征值，而 $E_\lambda$ 是 $E$ 中由所有满足 $Sv=\lambda v$ 的向量 $v$ 组成的子空间，那么 $TE_\lambda\subset E_\lambda$。］

**14.** 设 $E$ 是代数闭域 $k$ 上的有限维向量空间，$A\in\operatorname{End}_k(E)$。证明 $A$ 可以唯一地写成如下的和：

$$
A=S+N,
$$

其中 $S$ 可对角化，$N$ 幂零，并且 $SN=NS$。证明 $S,N$ 可以表示成 $A$ 的多项式。［*提示：* 设 $P_A(t)=\prod(t-\lambda_i)^{m_i}$ 是 $P_A(t)$ 的分解，其中 $\lambda_i$ 互不相同。令 $E_i$ 为 $(A-\lambda_i)^{m_i}$ 的核。那么 $E$ 是各 $E_i$ 的直和。在 $E$ 上定义 $S$，使得在 $E_i$ 上，对所有 $v\in E_i$ 都有 $Sv=\lambda_i v$。令 $N=A-S$。证明 $S,N$ 满足我们的要求。为把 $S$ 表示成 $A$ 的多项式，取一个多项式 $g$，使得对所有 $i$ 都有 $g(t)\equiv\lambda_i\bmod(t-\lambda_i)^{m_i}$，并且 $g(t)\equiv0\bmod t$。于是 $S=g(A)$，$N=A-g(A)$。］

**15.** 读过向量空间的张量积一节后，你可以容易地完成下列习题。设 $E,F$ 是代数闭域 $k$ 上的有限维向量空间，$A:E\to E$ 和 $B:F\to F$ 分别是 $E,F$ 的 $k$-自同态。设

$$
P_A(t)=\prod(t-\alpha_i)^{n_i}\quad\text{和}\quad P_B(t)=\prod(t-\beta_j)^{m_j}
$$

分别是它们的特征多项式按不同的一次因子所作的分解。那么

$$
P_{A\otimes B}(t)=\prod_{i,j}(t-\alpha_i\beta_j)^{n_i m_j}.
$$

［*提示：* 把 $E$ 分解成子空间 $E_i$ 的直和，其中 $E_i$ 是被 $A-\alpha_i$ 的某个幂零化的 $E$ 的子空间。对 $F$ 作同样处理，得到它分解成子空间 $F_j$ 的直和。然后证明 $A\otimes B-\alpha_i\beta_j$ 的某个幂零化 $E_i\otimes F_j$。利用如下事实：$E\otimes F$ 是子空间 $E_i\otimes F_j$ 的直和，而且 $\dim_k(E_i\otimes F_j)=n_i m_j$。］

**16.** 设 $\Gamma$ 是维数为 $n\geqq1$ 的自由阿贝尔群，$\Gamma'$ 是一个维数同样为 $n$ 的子群。设 $\{v_1,\ldots,v_n\}$ 是 $\Gamma$ 的一组基，$\{w_1,\ldots,w_n\}$ 是 $\Gamma'$ 的一组基。写成

$$
w_i=\sum a_{ij}v_j.
$$

证明指数 $(\Gamma:\Gamma')$ 等于矩阵 $(a_{ij})$ 的行列式的绝对值。

**17.** 证明有限域的有限扩张的正规基定理。

**18.** 设 $A=(a_{ij})$ 是交换环 $k$ 上的一个 $n\times n$ 方阵。设 $A_{ij}$ 是从 $A$ 中删去第 $i$ 行和第 $j$ 列所得的矩阵。令 $b_{ij}=(-1)^{i+j}\det(A_{ij})$，并设 $B$ 是矩阵 $(b_{ij})$。把问题归结到 $A$ 是整数上带有变量系数的矩阵这一情形，证明 $\det(B)=\det(A)^{n-1}$。用同样的方法给出凯莱–哈密顿定理的另一种证明，即证明 $P_A(A)=0$。

<span class="original-page-anchor" id="pdf-page-579" aria-hidden="true"></span>

**19.** 设 $(E,A)$ 和 $(E',A')$ 是由域 $k$ 上的一个有限维向量空间和一个 $k$-自同态组成的对。证明这些对同构当且仅当它们的不变因子相同。

**20.** (a) 在 $GL_2(\mathbf{C})$ 中，有多少个互不共轭的元素具有特征多项式 $t^3(t+1)^2(t-1)$？

(b) 有多少个具有特征多项式 $t^3-1001t$？

> **译校注：** 原文确实印为 $GL_2(\mathbf{C})$。两问的多项式次数分别为 $6$ 和 $3$，而 $2\times2$ 矩阵的特征多项式次数为 $2$；两者还有零根，因此不能是任何可逆矩阵的特征多项式。按原文两问的答案均为零。若作者意在询问一般方阵的共轭类，则须同时修改矩阵的阶数和可逆性要求；无法仅凭本页确定原拟题意，因此译文保留原题，不擅改环境。

**21.** 设 $V$ 是 $\mathbf{Q}$ 上的有限维向量空间，$A:V\to V$ 是一个满足 $A^5=\operatorname{Id}$ 的 $\mathbf{Q}$-线性映射。假定对于满足 $Av=v$ 的 $v\in V$，都有 $v=0$。证明 $\dim V$ 能被 $4$ 整除。

**22.** 设 $V$ 是 $\mathbf{R}$ 上的有限维向量空间，$A:V\to V$ 是一个满足 $A^2=-\operatorname{Id}$ 的 $\mathbf{R}$-线性映射。证明 $\dim V$ 是偶数，而且 $V$ 是若干个二维 $A$-不变子空间的直和。

**23.** 设 $E$ 是代数闭域 $k$ 上的有限维向量空间，$A,B$ 是 $E$ 的可交换的 $k$-自同态，即 $AB=BA$。证明 $A$ 和 $B$ 有一个共同的特征向量。［*提示：* 考察由所有以 $k$ 中某个固定元素为特征值的向量组成的子空间。］

**24.** 设 $V$ 是域 $k$ 上的有限维向量空间，$A$ 是 $V$ 的一个自同态。以 $\operatorname{Tr}(A^m)$ 表示 $A^m$ 作为 $V$ 的自同态的迹。证明下面关于变量 $t$ 的幂级数相等：

$$
\exp\left(\sum_{m=1}^\infty-\operatorname{Tr}(A^m)\frac{t^m}{m}\right)=\det(I-tA)\quad\text{或}\quad-\frac{d}{dt}\log\det(I-tA)=\sum_{m=1}^\infty\operatorname{Tr}(A^m)t^{m-1}.
$$

> **译校注：** 原文第二个等式的右端印为 $\sum_{m=1}^\infty\operatorname{Tr}(A^m)t^m$，这里应为 $\sum_{m=1}^\infty\operatorname{Tr}(A^m)t^{m-1}$，因为对 $t^m/m$ 求导得 $t^{m-1}$。例如一维情形 $A=1$ 时，左端为 $1/(1-t)$，原印右端为 $t/(1-t)$，常数项已经不符。此外，第一式中的除以任意正整数以及通常的形式指数、对数需要假定 $\operatorname{char}k=0$；原题没有给出这一条件。若把第二式左端理解为 $-(\det(I-tA))'/\det(I-tA)$，则改正后的第二式在任意特征下都成立。

与第 XVIII 章习题 23 比较。

**25.** 设 $V,W$ 是 $k$ 上的有限维向量空间，维数为 $n$。设 $(v,w)\mapsto\langle v,w\rangle$ 是 $V\times W$ 上的一个非奇异双线性形式。设 $c\in k$，$A:V\to V$ 和 $B:W\to W$ 是自同态，使得

$$
\langle Av,Bw\rangle=c\langle v,w\rangle\quad\text{对所有 }v\in V\text{ 和 }w\in W.
$$

> **译校注：** 原文在引入第二个自同态时印为 $V:W\to W$，应为 $B:W\to W$；紧接的条件和两个结论均使用 $B$，而 $V$ 已是向量空间的名称。

证明

$$
\det(A)\det(tI-B)=(-1)^n\det(cI-tA)
$$

以及

$$
\det(A)\det(B)=c^n.
$$

关于习题 24 和 25 在拓扑或代数几何中的一个应用，参见 Hartshorne 的 *Algebraic Geometry*，附录 C，§4。

**26.** 设 $G=SL_n(\mathbf{C})$，$K$ 是复酉群，$A$ 是对角线上各分量均为正实数的对角矩阵组成的群。

(a) 证明如果 $g\in\operatorname{Nor}_G(A)$（$A$ 在 $G$ 中的正规化子），那么 $c(g)$（由 $g$ 所作的共轭）置换 $A$ 的对角分量，因而产生一个同态 $\operatorname{Nor}_G(A)\to W$，其中 $W$ 是对角坐标的置换群。

按定义，上述同态的核是中心化子 $\operatorname{Cen}_G(A)$。

(b) 证明事实上坐标的所有置换都可以由 $K$ 中的元素实现，因此得到同构

$$
W\approx\operatorname{Nor}_G(A)/\operatorname{Cen}_G(A)\approx\operatorname{Nor}_K(A)/\operatorname{Cen}_K(A).
$$

事实上，右端的 $K$ 可以取为实酉群，因为置换矩阵可以取成具有实数分量（$0$ 或 $\pm1$）的矩阵。
