---
title: "第十九章 交错积"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第十八章 有限群的表示","link":"/library/volume-86/chapter-018"}
next: {"text":"第四部分导言：同调代数","link":"/library/volume-86/part-04"}
---

# 第十九章 交错积

<span class="original-page-anchor" id="pdf-page-739" aria-hidden="true"></span>

交错积在数学各领域都有应用。在微分几何中，对切空间取最高次交错积，可以得到流形上的典范线丛。中间各次的交错积给出微分形式（这些积在流形上的截面）。本章给出这些构造的代数背景。

关于双线性形式的各种自同构群在张量代数及交错代数上的作用，以及众多经典例子，一个较为自足的论述可参阅：

R. Howe，Remarks on classical invariant theory，*Trans. AMS* **313**（1989），第 539–569 页。

## §1. 定义与基本性质

考虑交换环 $R$ 上的模的范畴。

回顾：若 $r$ 重线性映射 $f:E^{(r)}\to F$ 在某两个不同下标 $i\ne j$ 满足 $x_i=x_j$ 时，总有 $f(x_1,\ldots,x_r)=0$，就称它为**交替**的。

设 $\mathfrak a_r$ 为张量积 $T^r(E)$ 中由所有形如

$$
x_1\otimes\cdots\otimes x_r
$$

的元素生成的子模，其中某两个不同下标 $i\ne j$ 满足 $x_i=x_j$。定义

$$
\bigwedge^r(E)=T^r(E)/\mathfrak a_r.
$$

于是有一个 $r$ 重线性映射 $E^{(r)}\to\bigwedge^r(E)$（称为典范映射），它由以下复合得到：

<span class="original-page-anchor" id="pdf-page-740" aria-hidden="true"></span>

复合映射为

$$
E^{(r)}\to T^r(E)\to T^r(E)/\mathfrak a_r=\bigwedge^r(E).
$$

这个映射显然是交替的。*而且，它对于 $E$ 上的 $r$ 重线性交替映射具有泛性质。* 换言之，若 $f:E^{(r)}\to F$ 为这样的映射，则存在唯一的线性映射 $f_*:\bigwedge^r(E)\to F$，使下图交换：

![交替映射的泛性质交换图](/library/volume-86/diagrams/pdf-0740-universal-alternating.png)

映射 $f_*$ 存在，是因为首先可以得到诱导映射 $T^r(E)\to F$，使下图交换：

![张量积诱导映射交换图](/library/volume-86/diagrams/pdf-0740-induced-tensor.png)

这个诱导映射在 $\mathfrak a_r$ 上为零，因而诱导出 $f_*$。

元素 $(x_1,\ldots,x_r)\in E^{(r)}$ 在到 $\bigwedge^r(E)$ 的典范映射下的像记作 $x_1\wedge\cdots\wedge x_r$。它也是 $x_1\otimes\cdots\otimes x_r$ 在商同态 $T^r(E)\to\bigwedge^r(E)$ 下的像。

这样，$\bigwedge^r$ 成为从模到模的函子。确实，设 $u:E\to F$ 为同态。给定 $x_1,\ldots,x_r\in E$，可作映射

$$
(x_1,\ldots,x_r)\mapsto u(x_1)\wedge\cdots\wedge u(x_r)\in\bigwedge^r(F).
$$

这个映射是多线性交替的，因此诱导出同态

$$
\bigwedge^r(u):\bigwedge^r(E)\to\bigwedge^r(F).
$$

对应 $u\mapsto\bigwedge^r(u)$ 显然具有函子性。

**例。** 翻开任何一本微分几何书（复的或实的），当 $E$ 是流形上一点的切空间，或该切空间的对偶空间时，就会看到这个构造的应用。对对偶空间作此构造，便得到微分形式。

用 $\bigwedge(E)$ 表示直和

$$
\bigwedge(E)=\bigoplus_{r=0}^\infty\bigwedge^r(E).
$$

<span class="original-page-anchor" id="pdf-page-741" aria-hidden="true"></span>

我们将赋予 $\bigwedge(E)$ 分次 $R$ 代数结构，并称它为 $E$ 的**交错代数**，也称**外代数**或**格拉斯曼代数**。先讨论任意分次环的一般情形。

再次设 $G$ 为加法幺半群，$A=\bigoplus_{r\in G}A_r$ 为 $G$ 分次 $R$ 代数。假设每个 $A_r$ 中给定了子模 $\mathfrak a_r$，令 $\mathfrak a=\bigoplus_{r\in G}\mathfrak a_r$。假设 $\mathfrak a$ 为 $A$ 的理想，便称 $\mathfrak a$ 为**齐次理想**，并可在 $A/\mathfrak a$ 上定义分次结构。确实，双线性映射

$$
A_r\times A_s\to A_{r+s}
$$

将 $\mathfrak a_r\times A_s$ 映入 $\mathfrak a_{r+s}$，同样将 $A_r\times\mathfrak a_s$ 映入 $\mathfrak a_{r+s}$。因此，分别使用 $A_r,A_s$ 中的代表元，可以定义双线性映射

$$
A_r/\mathfrak a_r\times A_s/\mathfrak a_s\to A_{r+s}/\mathfrak a_{r+s},
$$

进而定义双线性映射 $A/\mathfrak a\times A/\mathfrak a\to A/\mathfrak a$，它显然使 $A/\mathfrak a$ 成为分次 $R$ 代数。

将此应用于 $T^r(E)$ 及先前定义的模 $\mathfrak a_r$。若乘积 $x_1\wedge\cdots\wedge x_r$ 中有

$$
x_i=x_j\quad(i\ne j),
$$

则对任意 $y_1,\ldots,y_s\in E$，可见

$$
x_1\wedge\cdots\wedge x_r\wedge y_1\wedge\cdots\wedge y_s
$$

属于 $\mathfrak a_{r+s}$，左乘的情形也一样。因此直和 $\bigoplus\mathfrak a_r$ 是 $T(E)$ 的理想，可以在 $T(E)/\mathfrak a$ 上定义 $R$ 代数结构。齐次元素的乘积由下式给出：

$$
((x_1\wedge\cdots\wedge x_r),(y_1\wedge\cdots\wedge y_s))\mapsto x_1\wedge\cdots\wedge x_r\wedge y_1\wedge\cdots\wedge y_s.
$$

也用符号 $\wedge$ 表示 $\bigwedge(E)$ 中的乘积，称为**交错积**或**外积**。若 $x,y\in E$，则 $x\wedge y=-y\wedge x$，这由 $(x+y)\wedge(x+y)=0$ 得到。

*注意，$\bigwedge$ 是从模的范畴到分次 $R$ 代数的范畴的函子。* 对每个线性映射 $f:E\to F$，得到映射

$$
\bigwedge(f):\bigwedge(E)\to\bigwedge(F),
$$

使对 $x_1,\ldots,x_r\in E$，有

$$
\bigwedge(f)(x_1\wedge\cdots\wedge x_r)=f(x_1)\wedge\cdots\wedge f(x_r).
$$

而且，$\bigwedge(f)$ 是分次 $R$ 代数的同态。

<span class="original-page-anchor" id="pdf-page-742" aria-hidden="true"></span>

**命题 1.1。** *设 $E$ 在 $R$ 上自由，维数为 $n$。若 $r>n$，则 $\bigwedge^r(E)=0$。设 $\{v_1,\ldots,v_n\}$ 为 $E$ 在 $R$ 上的基。若 $1\le r\le n$，则 $\bigwedge^r(E)$ 在 $R$ 上自由，且元素*

$$
v_{i_1}\wedge\cdots\wedge v_{i_r},\qquad i_1<\cdots<i_r
$$

*构成 $\bigwedge^r(E)$ 在 $R$ 上的基。有*

$$
\dim_R\bigwedge^r(E)=\binom nr.
$$

> **译校注：** 首句关系符号的原印在大于号右侧带有一竖划，以下保留原图，英文也保留此原式而不猜测具体符号。这里依据本页证明末段明确的“$r>n$”情形及 $r=n$ 时最高次外幂有一个基的结论，按 $r>n$ 理解。另，原文“在 $k$ 上的基”中的 $k$ 在本章未定义，且命题针对一般环 $R$，这里按全文及证明改为 $R$。

![原书首句r与n的关系符号](/library/volume-86/diagrams/pdf-0742-r-relation.png)

**证明。** 先证明 $r=n$ 的断言。$E$ 的每个元素都可写为 $\sum a_iv_i$，因此利用 $x\wedge y=-y\wedge x$，可知 $v_1\wedge\cdots\wedge v_n$ 生成 $\bigwedge^n(E)$。另一方面，由行列式理论，给定 $a\in R$，存在唯一的 $E$ 上的多线性交替形式 $f_a$，使得

$$
f_a(v_1,\ldots,v_n)=a.
$$

因此存在唯一的线性映射

$$
\bigwedge^n(E)\to R,
$$

在 $v_1\wedge\cdots\wedge v_n$ 上取值 $a$。由此立即得到，$v_1\wedge\cdots\wedge v_n$ 是 $\bigwedge^n(E)$ 在 $R$ 上的基。

现在证明 $1\le r\le n$ 的断言。假设有关系式

$$
0=\sum a_{(i)}v_{i_1}\wedge\cdots\wedge v_{i_r},
$$

其中 $i_1<\cdots<i_r$，$a_{(i)}\in R$。任取 $r$ 元组 $(j)=(j_1,\ldots,j_r)$，满足 $j_1<\cdots<j_r$；设 $j_{r+1},\ldots,j_n$ 为未出现在 $(j_1,\ldots,j_r)$ 中的那些 $i$ 值。与 $v_{j_{r+1}}\wedge\cdots\wedge v_{j_n}$ 作交错积后，和式中除 $(j)$ 项以外的各项都含有重复分量，故得到

$$
0=a_{(j)}v_{j_1}\wedge\cdots\wedge v_{j_r}\wedge\cdots\wedge v_{j_n}.
$$

把 $v_{j_1}\wedge\cdots\wedge v_{j_n}$ 重排为 $v_1\wedge\cdots\wedge v_n$，只使右边变一个符号。由本证明开头所得的结论，有 $a_{(j)}=0$。因此证明了 $1\le r\le n$ 的断言。

当 $r=0$ 时，处理的是空积，$1$ 是 $\bigwedge^0(E)=R$ 在 $R$ 上的基。$r>n$ 的情形留给读者作为简单习题。

关于维数的断言显然，因为基元素的集合与整数集 $(1,\ldots,n)$ 的子集之间存在双射。

<span class="original-page-anchor" id="pdf-page-743" aria-hidden="true"></span>

**注。** 关于 $\bigwedge^n(E)$ 的证明的第一部分，可以不预先假设行列式存在。这时须证明 $\mathfrak a_n$ 在 $T^n(E)$ 中有一个一维补子模。这可用简单方法做到；我们将其留作习题，读者也可在 §4 的更一般情形中查到。当 $R$ 为域时，这个习题更为简单，因为可立即验证 $v_1\otimes\cdots\otimes v_n$ 不属于 $\mathfrak a_n$。以这种替代途径证明定理，随后便可证明行列式的存在性。

**命题 1.2。** *设*

$$
0\to E'\to E\to E''\to0
$$

*为有限秩自由 $R$ 模的正合列，三者的秩分别为 $r,n,s$。则存在自然同构*

$$
\varphi:\bigwedge^r E'\otimes\bigwedge^s E''\to\bigwedge^n E.
$$

*这个同构是具有以下性质的唯一同构：对于 $v_1,\ldots,v_r\in E'$ 和 $w_1,\ldots,w_s\in E''$，设 $u_1,\ldots,u_s$ 为 $w_1,\ldots,w_s$ 在 $E$ 中的提升，则*

$$
\varphi((v_1\wedge\cdots\wedge v_r)\otimes(w_1\wedge\cdots\wedge w_s))=v_1\wedge\cdots\wedge v_r\wedge u_1\wedge\cdots\wedge u_s.
$$

**证明。** 证明按通常的两步进行。首先证明具有所需作用的同态 $\varphi$ 存在。由交替性，上式右边的值不依赖于提升 $w_1,\ldots,w_s$ 的 $u_1,\ldots,u_s$ 的选择，因此得到同态 $\varphi$。特别选取 $\{v_1,\ldots,v_r\}$ 和 $\{w_1,\ldots,w_s\}$ 分别为 $E',E''$ 的基，便可看出 $\varphi$ 既单射又满射。细节留给读者。

给定秩为 $n$ 的自由模 $E$，把它的**行列式**定义为

$$
\det E=\bigwedge^{\max}E=\bigwedge^n E.
$$

于是命题 1.2 可改写为同构公式

$$
\det(E')\otimes\det(E'')\approx\det(E).
$$

若 $R=k$ 为域，则可称 $\det$ 为 $k$ 上有限维向量空间范畴上的欧拉–庞加莱映射。

**例。** 设 $V$ 为 $\mathbf R$ 上的有限维向量空间。$V$ 上的**体积**是指 $\det V$ 上的范数 $\|\ \|$。由于 $V$ 有限维，这样的范数等价于给 $\det(V)$ 的一个给定基指定正数 $c$。这样的基可写为 $e_1\wedge\cdots\wedge e_n$，其中 $\{e_1,\ldots,e_n\}$ 为 $V$ 的基。那么对 $a\in\mathbf R$，有

$$
\|ae_1\wedge\cdots\wedge e_n\|=|a|c.
$$

<span class="original-page-anchor" id="pdf-page-744" aria-hidden="true"></span>

在分析中，给定上述体积后，将集合 $S$ 的测度定义为

$$
\mu(S)=\int_S\|e_1\wedge\cdots\wedge e_n\|\,dx_1\cdots dx_n,
$$

从而在 $V$ 上定义哈尔测度 $\mu$，其中 $x_1,\ldots,x_n$ 为 $V$ 相对于上述基的坐标。作为习题，证明右边表达式不依赖基的选择。

命题 1.2 是以下更一般情形的特例。再次考虑上述有限秩自由 $R$ 模的正合列。对于 $E$ 的子模 $E'$，定义

$$
\bigwedge_i^n E=\bigwedge^n E\text{ 中由所有形如下式的元素生成的子模：}
$$

$$
x'_1\wedge\cdots\wedge x'_i\wedge y_{i+1}\wedge\cdots\wedge y_n,
$$

其中 $x'_1,\ldots,x'_i\in E'$，并将 $E'$ 视为 $E$ 的子模。

于是得到滤过

$$
\bigwedge_i^n E\supset\bigwedge_{i+1}^n E.
$$

**命题 1.3。** *存在自然同构*

$$
\bigwedge^i E'\otimes\bigwedge^{n-i}E''\to\bigwedge_i^n E/\bigwedge_{i+1}^n E.
$$

**证明。** 设 $x''_1,\ldots,x''_{n-i}$ 为 $E''$ 的元素，将它们提升为 $E$ 的元素 $y_1,\ldots,y_{n-i}$。考虑映射

$$
(x'_1,\ldots,x'_i,x''_1,\ldots,x''_{n-i})\mapsto x'_1\wedge\cdots\wedge x'_i\wedge y_1\wedge\cdots\wedge y_{n-i},
$$

右边取模 $\bigwedge_{i+1}^n E$。显然，该映射分解通过

$$
\bigwedge^i E'\otimes\bigwedge^{n-i}E''\to\bigwedge_i^n E/\bigwedge_{i+1}^n E.
$$

选取基即可看出得到的是所要的同构。

类似地，有：

**命题 1.4。** *设 $E=E'\oplus E''$ 为有限自由模的直和。则对每个正整数 $n$，有模同构*

$$
\bigwedge^n E\approx\bigoplus_{p+q=n}\bigwedge^p E'\otimes\bigwedge^q E''.
$$

<span class="original-page-anchor" id="pdf-page-745" aria-hidden="true"></span>

*用交错代数表述，有同构*

$$
\bigwedge E\approx\bigwedge E'\otimes_{su}\bigwedge E'',
$$

*其中 $\otimes_{su}$ 为分次代数的超积。*

**证明。** $E'$、$E''$ 到 $E$ 的每个自然嵌入，都诱导交错代数之间的自然映射，从而给出同态

$$
\bigwedge E'\otimes\bigwedge E''\to\bigwedge E.
$$

它是分次的，即对 $p=0,\ldots,n$，有

$$
\bigwedge^p E'\otimes\bigwedge^{n-p}E''\to\bigwedge^n E.
$$

要验证这给出所要的同构，可以选取基来论证，细节留给读者。交错积的反交换规则立即说明，对于超积 $\bigwedge E'\otimes_{su}\bigwedge E''$，这个同构是代数同构。

本节以关于对偶性的说明结束。在习题 3 中，你将证明：

**命题 1.5。** *设 $E$ 在 $R$ 上自由，秩为 $n$。对每个正整数 $r$，有自然同构*

$$
\bigwedge^r(E^\vee)\approx\bigwedge^r(E)^\vee.
$$

该同构在那道习题中有明确描述。比“自然”更精确的性质是：对于对象为 $R$ 上有限自由模、态射为同构的范畴，该同构具有函子性。

**例。** 设 $L$ 为 $R$ 上秩 $1$ 的自由模。其对偶模 $L^\vee=\operatorname{Hom}_R(L,R)$ 也自由且秩相同。对正整数 $m$，定义

$$
L^{\otimes-m}=(L^\vee)^{\otimes m}=L^\vee\otimes\cdots\otimes L^\vee\quad\text{（作 }m\text{ 重张量积）}.
$$

这样就为负整数定义了一条线与自身的张量积。定义 $L^{\otimes0}=R$。容易验证，对所有整数 $p,q\in\mathbf Z$，都有自然同构

$$
L^{\otimes p}\otimes L^{\otimes q}\approx L^{\otimes(p+q)}.
$$

特别地，若 $q=-p$，则右边得到 $R$ 本身。

现在设 $\mathbf E$ 为自由模的正合列：

$$
\mathbf E:0\to E_0\to E_1\to\cdots\to E_m\to0.
$$

<span class="original-page-anchor" id="pdf-page-746" aria-hidden="true"></span>

定义这个正合列的**行列式**为

$$
\det(\mathbf E)=\bigotimes\det(E_i)^{\otimes(-1)^i}.
$$

作为习题，证明 $\det(\mathbf E)$ 与 $R$ 自然同构，且对于正合列的同构具有函子性。

**例。** 向量空间或自由模的行列式出现在数学的多个分支，例如偏微分算子的复形、同调理论、代数几何中的行列式线丛理论等。例如，给定 $\mathbf C$ 上的非奇异射影簇 $V$，定义 $V$ 的**上同调行列式**为

$$
\det H(V)=\bigotimes\det H^i(V)^{\otimes(-1)^i},
$$

其中 $H^i(V)$ 为上同调群。于是 $\det H(V)$ 是 $\mathbf C$ 上的一维向量空间，但它与 $\mathbf C$ 之间没有自然的等同，因为先验地没有自然的基的选择。关于上同调行列式的一个重要应用，在法尔廷斯工作之后，可参阅 Deligne，Le determinant de la cohomologie，载于 Ribet, K.（编），*Current Trends in Arithmetical Algebraic Geometry*，Proc. Arcata 1985。（*Contemporary Math.* 第 **67** 卷，AMS（1985），第 93–178 页。）

## §2. 菲廷理想

由行列式生成的某些理想，在代数及代数几何的多个分支中越来越常用。因此我加入本节，概述它们的一些性质。更详尽的论述可参阅我所采用的诺思科特著作 *Finite Free Resolutions*，以及 Mazur–Wiles 的论文“Class Fields of abelian extensions of $\mathbf Q$”的附录；他们以自足的方式写成这篇附录。（*Invent. Math.* **76**（1984），第 179–330 页。）

设 $R$ 为交换环，$A$ 为 $p\times q$ 矩阵，$B$ 为 $q\times s$ 矩阵，系数都在 $R$ 中。设 $r\ge0$ 为整数。定义**行列式理想** $I_r(A)$ 为 $A$ 的所有 $r\times r$ 子矩阵的行列式生成的理想。也可如下描述这个理想。用 $S_r^p$ 表示序列

$$
J=(j_1,\ldots,j_r),\qquad1\le j_1<j_2<\cdots<j_r\le p
$$

的集合。

设 $A=(a_{ij})$，$1\le r\le\min(p,q)$。设 $K=(k_1,\ldots,k_r)$ 为 $S_r^q$ 的元素。*定义*

$$
A_{JK}^{(r)}=\begin{vmatrix}a_{j_1k_1}&a_{j_1k_2}&\cdots&a_{j_1k_r}\\a_{j_2k_1}&a_{j_2k_2}&\cdots&a_{j_2k_r}\\\vdots&\vdots&&\vdots\\a_{j_rk_1}&a_{j_rk_2}&\cdots&a_{j_rk_r}\end{vmatrix}.
$$

> **译校注：** 原书把列指标序列 $K$ 也写成 $S_r^p$ 的元素。由于 $A$ 有 $q$ 列，列下标应满足 $1\le k_1<\cdots<k_r\le q$，故此处应为 $S_r^q$。英文保留原印。

<span class="original-page-anchor" id="pdf-page-747" aria-hidden="true"></span>

其中竖线表示行列式。让 $J,K$ 分别遍历 $S_r^p,S_r^q$，可把 $A_{JK}^{(r)}$ 视为一个矩阵 $A^{(r)}$ 的 $JK$ 分量，称此矩阵为 **$A$ 的第 $r$ 次外幂**。

> **译校注：** 原书本句将 $J,K$ 都写为遍历 $S_r^p$，承接前页相同的列指标误写。这里分别取行指标集合 $S_r^p$ 和列指标集合 $S_r^q$，因为 $A$ 是 $p\times q$ 矩阵。

也可如下描述这个矩阵。设 $\{e_1,\ldots,e_p\}$ 为 $R^p$ 的基，$\{u_1,\ldots,u_q\}$ 为 $R^q$ 的基。则元素

$$
e_{j_1}\wedge\cdots\wedge e_{j_r}\qquad(j_1<j_2<\cdots<j_r)
$$

构成 $\bigwedge^rR^p$ 的基，$\bigwedge^rR^q$ 的基也类似。可将 $A$ 视为从 $R^p$ 到 $R^q$ 的线性映射，则 $A^{(r)}$ 是外幂 $\bigwedge^rA$ 的矩阵，后者视为从 $\bigwedge^rR^p$ 到 $\bigwedge^rR^q$ 的线性映射。总体来说，这种解释对某些计算并不特别有用，但确实为外幂提供了稍具概念性的背景。从一开始，这种解释便可立即证明命题 2.1。当 $r=0$ 时，定义 $A^{(0)}$ 为唯一元素是 $R$ 的单位元的 $1\times1$ 矩阵。另有 $A^{(1)}=A$。

**命题 2.1。** *设 $A$ 为 $p\times q$ 矩阵，$B$ 为 $q\times s$ 矩阵，则*

$$
(AB)^{(r)}=A^{(r)}B^{(r)}\quad\text{对 }r\ge0.
$$

若使用上面提到的交错积，证明只是说：线性映射的复合关于固定基的矩阵，是各矩阵的乘积。若不使用交错积，也可直接计算证明这个命题，留给读者完成。

我们已经构造了由有限集 $S_r^p$ 编指标的矩阵。对任意有限集 $S$ 和双指标族 $(c_{JK})$，其中 $J,K\in S$，也可定义**行列式**为

$$
\det(c_{JK})=\sum_\sigma\varepsilon(\sigma)\left(\prod_{J\in S}c_{J,\sigma(J)}\right),
$$

其中 $\sigma$ 遍历该集合的所有置换。

对 $r\ge0$，定义**行列式理想** $I_r(A)$ 为 $A^{(r)}$ 的所有分量生成的理想，等价地为 $A$ 的所有 $r\times r$ 子行列式生成的理想。由定义有

$$
I_0(A)=R,\qquad I_1(A)=A\text{ 的各分量生成的理想}.
$$

> **译校注：** 原书此处写成 $A^{(0)}=R$ 及 $A^{(1)}=\text{ideal}\ldots$，但本页上文已定义 $A^{(0)}$、$A^{(1)}$ 为矩阵。这里正在列举行列式理想的性质，且下式明确用 $I_0(A),I_1(A)$，故按定义改用理想符号；英文保留原印。

此外，

$$
I_r(A)=0\quad\text{当 }r>\min(p,q),
$$

并有包含关系

$$
R=I_0(A)\supset I_1(A)\supset I_2(A)\supset\cdots.
$$

<span class="original-page-anchor" id="pdf-page-748" aria-hidden="true"></span>

由命题 10.1，还有

**译校注：** 原书此处引用“命题 10.1”。本式直接由上一页命题 2.1 的 $(AB)^{(r)}=A^{(r)}B^{(r)}$ 得到：积矩阵的每个分量是各自分量的乘积之和，故所属理想同时包含于 $I_r(A)$ 和 $I_r(B)$。据此这里应用的是命题 2.1；保留原引用并说明其所指。

$$
I_r(AB)\subset I_r(A)\cap I_r(B).\tag{1}
$$

因此，若 $A=UBU'$，其中 $U,U'$ 是行列式为 $1$ 的方阵，则

$$
I_r(A)=I_r(B).\tag{2}
$$

其次，设 $E$ 为 $R$ 模，$x_1,\ldots,x_q$ 为 $E$ 的生成元。可以把满足

$$
\sum_{i=1}^q a_ix_i=0
$$

的关系 $(a_1,\ldots,a_q)\in R^q$ 排成关系矩阵。

先假设只取有限多个关系，从而得到 $p\times q$ 矩阵 $A$。构造行列式理想 $I_r(A)$。将生成元族的**行列式理想**定义为

$$
I_r(x_1,\ldots,x_q)=I_r(x)=\text{所有 }A\text{ 的 }I_r(A)\text{ 生成的理想}.
$$

因此，实际上可取无限关系矩阵，并说 $I_r(x)$ 由所有 $r\times r$ 子矩阵的行列式生成。式（1）的包含关系说明

$$
\begin{gathered}
R=I_0(x)\supset I_1(x)\supset I_2(x)\supset\cdots\ ,\\
I_r(x)=0\quad\text{若 }r>q.
\end{gathered}
$$

此外，容易看出，若在全部关系组成的矩阵中，只取一族生成 $R^q$ 中全部关系子模的关系，形成子矩阵 $M$，则有

$$
I_r(M)=I_r(x).
$$

> **译校注：** 原书将 $R^q$ 中全部关系称作“ideal”。这里准确地说是核 $\operatorname{Ker}(R^q\to E)$，即一个 $R$ 子模；按这个意义翻译为“关系子模”。

验证留给读者。当 $E$ 有限呈示时，可以取 $M$ 为有限矩阵；若 $R$ 为诺特环，就有这种情形。

用 $E$ 作为 $R^q$ 的商模的这种表示，可得到以下刻画。

**命题 2.2。** *设 $R^q\to E\to0$ 为 $E$ 作为 $R^q$ 的商模的表示，$x_1,\ldots,x_q$ 为 $R^q$ 的单位向量的像。则 $I_r(x)$ 为所有值*

$$
\lambda(w_1,\ldots,w_r)
$$

*生成的理想，其中 $w_1,\ldots,w_r\in\operatorname{Ker}(R^q\to E)$，$\lambda\in L_a^r(R^q,R)$。*

**证明。** 由行列式理想的定义立即得到。

<span class="original-page-anchor" id="pdf-page-749" aria-hidden="true"></span>

上述命题可用来将矩阵计算替换为下标较少、更具概念性的论证。读者可把下面的一些矩阵论证改写成这些更具不变性的语言，这样做很有益。

现在改变编号，将**菲廷理想**定义为

$$
\begin{aligned}
F_k(x)&=I_{q-k}(x)&&\text{当 }0\le k\le q,\\
F_k(x)&=R&&\text{当 }k>q.
\end{aligned}
$$

**引理 2.3。** *菲廷理想 $F_k(x)$ 不依赖生成元 $(x)$ 的选择。*

**证明。** 设 $y_1,\ldots,y_s$ 为 $E$ 的元素。将证明

$$
I_r(x)=I_{r+s}(x,y).
$$

$(x,y)$ 的关系构成形如以下的矩阵：

![关系矩阵W](/library/volume-86/diagrams/pdf-0749-relations-W.png)

利用初等列变换，可把它变成矩阵

$$
\begin{pmatrix}A&0\\0&1_s\end{pmatrix}.
$$

由式（2），这些变换不改变行列式理想。因此，对所有 $r\ge0$，有

$$
I_r(A)=I_{r+s}(W)\subset I_{r+s}(x,y).
$$

这证明了 $I_r(x)\subset I_{r+s}(x,y)$。

反之，设 $C$ 为生成元 $(x,y)$ 之间的关系矩阵。另有关系矩阵

![关系矩阵Z](/library/volume-86/diagrams/pdf-0749-relations-Z.png)

利用初等行变换，可将此矩阵变为与上面相同的形状，<span class="original-page-anchor" id="pdf-page-750" aria-hidden="true"></span>与上面的 $B$ 同形，其中 $A'$ 为 $(x)$ 的某个关系矩阵，即

$$
Z'=\begin{pmatrix}A'&0\\B&1_s\end{pmatrix}.
$$

于是

$$
I_r(A')=I_{r+s}(Z')=I_{r+s}(Z)\supset I_{r+s}(C),
$$

从而 $I_{r+s}(C)\subset I_r(x)$。让 $C$ 遍历所有可能的关系矩阵，得到 $I_{r+s}(x,y)\subset I_r(x)$。结合先前的包含关系，便有 $I_{r+s}(x,y)=I_r(x)$。

现在给定两个生成元族 $(x)$ 和 $(y)$，只须把它们并列成 $(x,y)$，再使用 $F_k$ 的新编号，就完成了引理的证明。

设 $E$ 为有限生成 $R$ 模，具有呈示

$$
0\to K\to R^q\to E\to0,
$$

此列正合，$K$ 定义为核。那么 $K$ 由 $q$ 维向量生成，可视为无限矩阵。$R^q$ 的单位向量的像为生成元 $(x_1,\ldots,x_q)$。定义此模的**菲廷理想**为

$$
F_k(E)=F_k(x).
$$

引理 2.3 说明，这个理想不依赖呈示的选择。矩阵的行列式理想 $I_r(A)$ 的包含关系，转变成菲廷理想的反向包含关系，即：

**命题 2.4。**

*（i）有*

$$
F_0(E)\subset F_1(E)\subset F_2(E)\subset\cdots.
$$

*（ii）若 $E$ 可由 $q$ 个元素生成，则*

$$
F_q(E)=R.
$$

*（iii）若 $E$ 有限呈示，则对所有 $k$，$F_k(E)$ 都有限生成。*

最后一条只是重述如下性质：若矩阵的行空间有限生成，则该矩阵的行列式理想可由某个有限子矩阵所对应的行列式生成。

<span class="original-page-anchor" id="pdf-page-751" aria-hidden="true"></span>

**例。** 设 $E=R^q$ 为维数 $q$ 的自由模。则

$$
F_k(E)=\begin{cases}0&\text{若 }0\le k<q,\\R&\text{若 }k\ge q.\end{cases}
$$

由定义及 $E$ 的基只有平凡关系这一事实，立即得出。

菲廷理想 $F_0(E)$ 称为**第零**或**初始菲廷理想**。在某些应用中只出现这个理想，此时就称它为 $E$ 的“那个”**菲廷理想** $F(E)$。它是模的 $q$ 个生成元的关系矩阵中所有 $q\times q$ 行列式生成的理想。

对任意模 $E$，用 $\operatorname{ann}_R(E)$ 表示 $E$ 在 $R$ 中的零化子，即满足 $aE=0$ 的元素 $a\in R$ 的集合。

**命题 2.5。** *假设 $E$ 可由 $q$ 个元素生成。则*

$$
(\operatorname{ann}_R(E))^q\subset F(E)\subset\operatorname{ann}_R(E).
$$

*特别地，若 $E$ 可由一个元素生成，则*

$$
F(E)=\operatorname{ann}_R(E).
$$

**证明。** 设 $x_1,\ldots,x_q$ 为 $E$ 的生成元，$a_1,\ldots,a_q$ 为 $R$ 中零化 $E$ 的元素。对角分量为 $a_1,\ldots,a_q$ 的对角矩阵是一个关系矩阵，因此菲廷理想的定义说明，这个矩阵的行列式，即乘积 $a_1\cdots a_q$，属于 $I_q(E)\subset F_0(E)$。这证明了包含关系

$$
\operatorname{ann}_R(E)^q\subset F(E).
$$

反之，设 $A$ 为 $x_1,\ldots,x_q$ 之间的 $q\times q$ 关系矩阵。则对所有 $i$，有 $\det(A)x_i=0$，故 $\det(A)\in\operatorname{ann}_R(E)$。由于 $F(E)$ 由这些行列式生成，得到反向包含关系，命题得证。

**推论 2.6。** *设 $E=R/\mathfrak a$，其中 $\mathfrak a$ 为某个理想。则 $F(E)=\mathfrak a$。*

**证明。** 模 $R/\mathfrak a$ 可由一个元素生成，因此推论由命题立即得到。

**命题 2.7。** *设*

$$
0\to E'\to E\to E''\to0
$$

*为有限生成 $R$ 模的正合列。对整数 $m,n\ge0$，有*

$$
F_m(E')F_n(E'')\subset F_{m+n}(E).
$$

<span class="original-page-anchor" id="pdf-page-752" aria-hidden="true"></span>

*特别地，对于 $F=F_0$，有*

$$
F(E')F(E'')\subset F(E).
$$

**证明。** 可假设 $E'$ 为 $E$ 的子模。选取 $E'$ 的生成元 $x_1,\ldots,x_p$，以及 $E$ 的元素 $y_1,\ldots,y_q$，使其在 $E''$ 中的像 $y''_1,\ldots,y''_q$ 生成 $E''$。则 $(x,y)$ 为 $E$ 的生成元族。先假设 $m\le p$ 且 $n\le q$。设 $A$ 为 $y''_1,\ldots,y''_q$ 的关系矩阵，有 $q$ 列。若 $(a_1,\ldots,a_q)$ 为这样的关系，则

$$
a_1y_1+\cdots+a_qy_q\in E',
$$

所以存在 $b_1,\ldots,b_p\in R$，使

$$
\sum a_iy_i+\sum b_jx_j=0.
$$

因此可找到一个有 $p$ 列、行数与 $A$ 相同的矩阵 $B$，使 $(B,A)$ 为 $(x,y)$ 的关系矩阵。设 $C$ 为 $(x_1,\ldots,x_p)$ 的关系矩阵，则

$$
\begin{pmatrix}B&A\\C&0\end{pmatrix}
$$

为 $(x,y)$ 的关系矩阵。若 $D''$ 为 $A$ 的 $(q-n)\times(q-n)$ 子行列式，$D'$ 为 $C$ 的 $(p-m)\times(p-m)$ 子行列式，则 $D''D'$ 是矩阵

$$
\begin{pmatrix}B&A\\C&0\end{pmatrix}
$$

的一个 $(p+q-m-n)\times(p+q-m-n)$ 子行列式，而且 $D''D'\in F_{m+n}(E)$。由于 $F_m(E')$ 由 $D'$ 这样的行列式生成，$F_n(E'')$ 由 $D''$ 这样的行列式生成，就证明了当前情形的命题。

若 $m>p$ 且 $n>q$，则 $F_{m+n}(E)=F_m(E')=F_n(E'')=R$，此时命题显然。

设 $m\le p$ 且 $n>q$。则 $F_n(E'')=R=F_q(E'')$，因此

$$
F_m(E')F_n(E'')=F_q(E'')F_m(E')\subset F_{m+q}(E)\subset F_{m+n}(E).
$$

> **译校注：** 原书此链中间印为 $F_{p+n}(E)$，已放大原图确认。按第一种情形，将第二个下标取 $q$，得到的是 $F_{m+q}(E)$；再由 $q<n$ 及菲廷理想随下标增大而增大，得到最后的包含关系。因此这里改为 $F_{m+q}(E)$，英文保留原印。

其中包含关系由第一种情形得到。对剩余的 $m>p$ 且 $n\le q$ 的情形，类似论证即可。这完成了证明。

**命题 2.8。** *设 $E',E''$ 为有限生成 $R$ 模。对任意整数 $n\ge0$，有*

$$
F_n(E'\oplus E'')=\sum_{r+s=n}F_r(E')F_s(E'').
$$

<span class="original-page-anchor" id="pdf-page-753" aria-hidden="true"></span>

**证明。** 设 $x_1,\ldots,x_p$ 生成 $E'$，$y_1,\ldots,y_q$ 生成 $E''$。则 $(x,y)$ 生成 $E'\oplus E''$。由命题 2.7，已有包含关系

$$
\sum F_r(E')F_s(E'')\subset F_n(E'\oplus E''),
$$

> **译校注：** 原文引用“命题 2.6”；这里使用的是上一命题 2.7 对分裂正合列 $0\to E'\to E'\oplus E''\to E''\to0$ 的结论。2.6 实为关于 $R/\mathfrak a$ 的推论，故将此处编号改为 2.7。

所以须证明反向包含关系。若 $n\ge p+q$，可取 $r\ge p$ 且 $s\ge q$，此时

$$
F_r(E')=F_s(E'')=F_n(E)=R,
$$

便完成了证明。因此假设 $n<p+q$。直和中 $(x,y)$ 之间的关系分裂成 $(x)$ 的关系及 $(y)$ 的关系，所以 $(x,y)$ 的关系矩阵形如

$$
C=\begin{pmatrix}A'&0\\0&A''\end{pmatrix},
$$

其中 $A'$ 为 $(x)$ 的关系矩阵，$A''$ 为 $(y)$ 的关系矩阵。因此

$$
F_n(E'\oplus E'')=\sum_C I_{p+q-n}(C),
$$

其中求和遍历上述所有矩阵 $C$。设 $D$ 为一个 $(p+q-n)\times(p+q-n)$ 子行列式，则 $D$ 形如

$$
D=\begin{vmatrix}B'&0\\0&B''\end{vmatrix},
$$

其中 $B'$ 为 $k'\times(p-r)$ 矩阵，$B''$ 为 $k''\times(q-s)$ 矩阵，某些非负整数 $k',k'',r,s$ 满足

$$
k'+k''=p+q-n,\qquad r+s=n.
$$

> **译校注：** 原书称这些整数为“positive”。此处必须允许零，例如命题包含 $n=0$，这时 $r+s=0$ 要求 $r=s=0$；子矩阵也可能在一个对角块中没有行或列。因此按子矩阵的实际大小取非负整数。

除非 $k'=p-r$ 且 $k''=q-s$，否则 $D=0$。若这两个等式成立，则

$$
D=\det(B')\det(B'')\in F_r(E')F_s(E''),
$$

这证明了反向包含关系，并完成命题的证明。

**推论 2.9。** *设*

$$
E=\bigoplus_{i=1}^s R/\mathfrak a_i,
$$

*其中 $\mathfrak a_i$ 为理想，则 $F(E)=\mathfrak a_1\cdots\mathfrak a_s$。*

**证明。** 这其实是命题 2.8 与推论 2.6 的推论。

<span class="original-page-anchor" id="pdf-page-754" aria-hidden="true"></span>

## §3. 泛导子与德拉姆复形

*本节假设所有环 $R,A$ 等都是交换环。*

设 $A$ 为 $R$ 代数，$M$ 为 $A$ 模。$R$ 上的**导子** $D:A\to M$ 是指满足通常规则

$$
D(ab)=aDb+bDa
$$

的 $R$ 线性映射。

注意，$D(1)=2D(1)$，所以 $D(1)=0$，从而 $D(R)=0$。这些导子自然构成 $A$ 模 $\operatorname{Der}_R(A,M)$，其中 $aD$ 定义为 $(aD)(b)=aDb$。

$A$ 在 $R$ 上的**泛导子**是指 $A$ 模 $\Omega$ 及导子

$$
d:A\to\Omega,
$$

使对任意导子 $D:A\to M$，存在唯一的 $A$ 同态 $f:\Omega\to M$，令下图交换：

![泛导子交换图](/library/volume-86/diagrams/pdf-0754-universal-derivation.png)

由定义立即可知，泛导子 $(d,\Omega)$ 在唯一同构意义下唯一确定。根据定义，有具有函子性的同构

$$
\boxed{\operatorname{Der}_R(A,M)\approx\operatorname{Hom}_A(\Omega,M)}.
$$

现在证明泛导子的存在性。

以下一般说明很有用。设

$$
f_1,f_2:A\to B
$$

为两个 $R$ 代数同态，$J$ 为 $B$ 中满足 $J^2=0$ 的理想。假设 $f_1\equiv f_2\bmod J$，即对所有 $x\in A$，有 $f_1(x)\equiv f_2(x)\bmod J$。则

$$
D=f_2-f_1
$$

是导子。直接验证如下：

$$
\begin{aligned}
f_2(ab)&=f_2(a)f_2(b)=[f_1(a)+D(a)][f_1(b)+D(b)]\\
&=f_1(ab)+f_1(b)D(a)+f_1(a)D(b).
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-755" aria-hidden="true"></span>

不过，$J$ 的 $A$ 模结构由 $f_1$ 或 $f_2$ 给出（根据对 $f_1,f_2$ 的假设，两者相同），因此上述事实得证。

以下张量积取在 $R$ 上。

设 $\mathbf m_A:A\otimes A\to A$ 为乘法同态，满足 $\mathbf m_A(a\otimes b)=ab$。令 $J=\operatorname{Ker}\mathbf m_A$。定义**微分模**

$$
\Omega_{A/R}=J/J^2,
$$

将其视为 $(A\otimes A)/J^2$ 中的理想。$A$ 模结构总由第一个因子上的嵌入给出：

$$
A\to A\otimes A,\qquad a\mapsto a\otimes1.
$$

注意，有 $A$ 模的直和分解

$$
A\otimes A=(A\otimes1)\oplus J,
$$

所以

$$
(A\otimes A)/J^2=(A\otimes1)\oplus J/J^2.
$$

设

$$
d:A\to J/J^2
$$

为 $R$ 线性映射 $a\mapsto1\otimes a-a\otimes1\bmod J^2$。取 $f_1:a\mapsto a\otimes1$ 和 $f_2:a\mapsto1\otimes a$，可见 $d=f_2-f_1$。因此将 $d$ 视为到 $J/J^2$ 的映射时，它是导子。

注意，$J$ 由形如

$$
\sum x_i\,dy_i
$$

的元素生成。确实，若 $\sum x_i\otimes y_i\in J$，则根据定义 $\sum x_iy_i=0$，从而

$$
\sum x_i\otimes y_i=\sum x_i(1\otimes y_i-y_i\otimes1),
$$

这里使用赋予 $A\otimes A$ 的 $A$ 模结构（$A$ 作用在左因子上）。

**定理 3.1。** *二元组 $(J/J^2,d)$ 对 $A$ 的导子具有泛性质。即：给定导子 $D:A\to M$，存在唯一的 $A$ 线性映射 $f:J/J^2\to M$，使下图交换。*

![微分模的泛性质交换图](/library/volume-86/diagrams/pdf-0755-differentials-universal.png)

<span class="original-page-anchor" id="pdf-page-756" aria-hidden="true"></span>

**证明。** 存在唯一的 $R$ 双线性映射

$$
f:A\otimes A\to M,\qquad x\otimes y\mapsto xDy,
$$

由我们对 $A\otimes A$ 上 $A$ 模结构的定义，它是 $A$ 线性的。根据定义，把 $f$ 限制在 $J$ 上时，该图在 $A$ 的元素上交换，因为

$$
f(1\otimes y-y\otimes1)=Dy.
$$

由于 $J/J^2$ 由形如 $x\,dy$ 的元素生成，定理交换图中映射的唯一性很清楚。这证明了所要求的泛性质。

定理所述结果可写成公式

$$
\boxed{\operatorname{Der}_R(A,M)\approx\operatorname{Hom}_A(J/J^2,M)}.
$$

读者将在习题中看到关于导子的习题，它们提供构造泛导子的另一种方法。在处理有限生成代数时，这种方法尤其有用，因为这些代数是多项式环的商。

这里不加证明地列出一些进一步的基本构造，它们在微分几何与代数几何中很重要。证明容易，可作为很好的习题。

设 $R\to A$ 为交换环的 $R$ 代数。对 $i\ge0$，定义

$$
\Omega_{A/R}^i=\bigwedge^i\Omega_{A/R}^1,
$$

其中 $\Omega_{A/R}^0=A$。

**定理 3.2。** *存在唯一的 $R$ 同态序列*

$$
d_i:\Omega_{A/R}^i\to\Omega_{A/R}^{i+1},
$$

*使对 $\omega\in\Omega^i$、$\eta\in\Omega^j$，有*

$$
d(\omega\wedge\eta)=d\omega\wedge\eta+(-1)^i\omega\wedge d\eta.
$$

*而且 $d\circ d=0$。*

证明留作习题。

回顾：模的**复形**是同态序列

$$
\cdots\to E^{i-1}\xrightarrow{d^{i-1}}E^i\xrightarrow{d^i}E^{i+1}\to,
$$

满足 $d^i\circ d^{i-1}=0$。通常省略映射 $d$ 的上标。用这个术语，$\Omega_{A/R}^i$ 构成复形，称为**德拉姆复形**。

<span class="original-page-anchor" id="pdf-page-757" aria-hidden="true"></span>

**定理 3.3。** *设 $k$ 为特征 $0$ 的域，$A=k[X_1,\ldots,X_n]$ 为 $n$ 个变量的多项式环。则德拉姆复形*

$$
0\to k\to A\to\Omega_{A/k}^1\to\cdots\to\Omega_{A/k}^n\to0
$$

*正合。*

证明再次留作习题。**提示：** 使用归纳法，并作形式积分。

有关联络的其他结果将在下面的习题中给出。

## §4. 克利福德代数

设 $k$ 为域。本节中的**代数**均指由环同态 $k\to A$ 给出的 $k$ 代数，且 $k$ 的像包含在 $A$ 的中心中。

设 $E$ 为域 $k$ 上有限维向量空间，$g$ 为 $E$ 上的对称形式。我们希望找到一个 $k$ 上的泛代数，可以将 $E$ 嵌入其中，而且代数中的平方对应于 $E$ 中二次型的值。更准确地说，$g$ 的**克利福德代数**是指 $k$ 代数 $C(g)$，也记作 $C_g(E)$，以及线性映射 $\rho:E\to C(g)$，具有如下性质：若 $\psi:E\to L$ 为从 $E$ 到 $k$ 代数 $L$ 的线性映射，且对所有 $x\in E$，有

$$
\psi(x)^2=g(x,x)\cdot1\quad\text{（}1=L\text{ 的单位元）},
$$

则存在唯一的代数同态

$$
C(\psi)=\psi_*:C(g)\to L,
$$

使下图交换：

![克利福德代数的泛性质交换图](/library/volume-86/diagrams/pdf-0757-clifford-universal.png)

由一般的抽象论证，$g$ 的克利福德代数在唯一同构意义下唯一确定。而且显然，若 $(C(g),\rho)$ 存在，则 $C(g)$ 作为 $k$ 代数由 $\rho$ 的像，即 $\rho(E)$，生成。

若需要明确指明所涉及的 $g$，便写 $\rho=\rho_g$。

<span class="original-page-anchor" id="pdf-page-758" aria-hidden="true"></span>

显然，对所有 $x\in E$，有

$$
\rho(x)^2=g(x,x)\cdot1,
$$

以及

$$
\rho(x)\rho(y)+\rho(y)\rho(x)=2g(x,y)\cdot1,
$$

后式由前式中把 $x$ 换为 $x+y$ 得到。

**定理 4.1。** *设 $g$ 为 $k$ 上有限维向量空间 $E$ 上的对称双线性形式。则克利福德代数 $(C(g),\rho)$ 存在。映射 $\rho$ 单射，而且若 $n=\dim E$，则 $C(g)$ 在 $k$ 上的维数为 $2^n$。*

**证明。** 设 $T(E)$ 为第十六章 §7 中的张量代数。在该代数中，设 $I_g$ 为所有元素

$$
x\otimes x-g(x,x)\cdot1\quad(x\in E)
$$

生成的双边理想。

定义 $C_g(E)=T(E)/I_g$。注意，$E$ 自然嵌入 $T(E)$，因为

$$
T(E)=k\oplus E\oplus(E\otimes E)\oplus\cdots.
$$

于是，把 $E$ 到 $TE$ 的自然嵌入与从 $T(E)$ 到 $C_g(E)$ 的典范同态复合，就定义了 $k$ 线性映射 $\rho:E\to C_g(E)$。由张量积的泛性质，立即可知如此定义的 $C_g(E)$ 满足克利福德代数的泛性质，故它存在。唯一的问题是证明它在 $k$ 上确有上述维数。

先证明维数 $\le2^n$。只在 $k$ 的特征不等于 $2$ 时给出证明，特征 $2$ 的情形留给读者。设 $\{v_1,\ldots,v_n\}$ 为第十五章定理 3.1 给出的 $E$ 的正交基。令 $e_i=\psi(v_i)$，其中 $\psi:E\to L$ 如本节开头所给。令 $c_i=g(v_i,v_i)$，则有关系

$$
e_i^2=c_i,\qquad e_ie_j=-e_je_i\quad(i\ne j).
$$

这立即说明，$L$ 中由 $\psi(E)$ 在 $k$ 上生成的子代数，作为 $k$ 向量空间由所有元素

$$
e_1^{\nu_1}\cdots e_n^{\nu_n},\qquad\nu_i=0\text{ 或 }1\quad(i=1,\ldots,n)
$$

生成。因此该子代数的维数 $\le2^n$。特别地，$\dim C_g(E)\le2^n$，如所要的。

还须证明至少存在一个 $\psi:E\to L$，使 $L$ 作为 $k$ 代数由 $\psi(E)$ 生成，且维数为 $2^n$。因为在这种情况下，同态 $\psi_*:C_g(E)\to L$ 满射，故 $\dim C_g(E)\ge2^n$，定理便得证。我们将如下构造 $L$，先引入一些一般概念。

设 $M$ 为交换环上的模，$i,j\in\mathbf Z/2\mathbf Z$。假设 $M$ 为直和 $M=M_0\oplus M_1$，其中 $0,1$ 视为 $\mathbf Z/2\mathbf Z$ 的元素。于是称 $M$ 为 **$\mathbf Z/2\mathbf Z$ 分次**的。若 $M$ 为该环上的代数，则称<span class="original-page-anchor" id="pdf-page-759" aria-hidden="true"></span>若对所有 $i,j\in\mathbf Z/2\mathbf Z$，有 $M_iM_j\subset M_{i+j}$，则称它为 **$\mathbf Z/2\mathbf Z$ 分次代数**。若整个讨论中已固定所指的是 $\mathbf Z/2\mathbf Z$，便省略此前缀，简称**分次**；本节余下部分就是如此。

设 $A,B$ 为上述分次模，$A=A_0\oplus A_1$，$B=B_0\oplus B_1$。则张量积 $A\otimes B$ 有直和分解

$$
A\otimes B=\bigoplus_{i,j}A_i\otimes B_j.
$$

在 $A\otimes B$ 上定义分次：令 $(A\otimes B)_0$ 为对满足 $i+j=0$（在 $\mathbf Z/2\mathbf Z$ 中）的下标 $i,j$ 求和所得的部分，$(A\otimes B)_1$ 为对满足 $i+j=1$ 的下标 $i,j$ 求和所得的部分。

假设 $A,B$ 为给定交换环上的分次代数。存在唯一的从 $A\otimes B$ 到自身的双线性映射，使

$$
(a\otimes b)(a'\otimes b')=(-1)^{ij}aa'\otimes bb'
$$

当 $a'\in A_i$、$b\in B_j$ 时成立。与第十六章 §6 一样，可验证结合律，并验证此乘积给出分次代数。这个乘积称为**超张量积**或**超积**。在记号上，对 $A,B$ 取超张量积时，将所得代数记作

$$
A\otimes_{su}B,
$$

以区别于第十六章 §6 的通常代数 $A\otimes B$。

接着假设 $E$ 在 $k$ 上维数为 $1$。立即可验证，多项式商环 $k[X]/(x^2-c_1)$ 是此情形的克利福德代数。令 $t_1$ 为 $X$ 在商环中的像，则 $C_g(E)=k[t_1]$，且 $t_1^2=c_1$。向量空间 $E$ 作为 $kt_1$ 嵌入直和 $k\oplus kt_1$ 中。

在一般情形，归纳地取超张量积：

$$
C_g(E)=k[t_1]\otimes_{su}k[t_2]\otimes_{su}\cdots\otimes_{su}k[t_n],\qquad k[t_i]=k[X]/(X^2-c_i).
$$

其维数为 $2^n$。于是 $E$ 通过映射

$$
a_1v_1+\cdots+a_nv_n\mapsto a_1t_1\oplus\cdots\oplus a_nt_n
$$

嵌入 $C_g(E)$。由超积的定义立即可验证 $t_i,t_j$ 之间所需的交换规则，从而完成克利福德代数维数的证明。

注意，此证明给出了代数关系的明确表示，也使代数中的计算容易进行。还应注意，自由模的交错代数是特殊情形，只须对所有 $i$ 取 $c_i=0$。令 $c_i$ 代数无关，可见交错代数是一般克利福德代数的特化；也可以说，克利福德代数是所谓交错代数的扰动。与交错代数一样，由构造立即得到：

**定理 4.2。** *设 $g,g'$ 分别为 $E,E'$ 上的对称形式。则我们* <span class="original-page-anchor" id="pdf-page-760" aria-hidden="true"></span>*有代数同构*

$$
C(g\oplus g')\approx C(g)\otimes_{su}C(g').
$$

**例。** 克利福德代数在物理、微分几何、拓扑、群表示（有限群及李群）以及数论中有越来越广泛的应用。首先，在拓扑方面，可参阅 Adams [Ad 62] 及 [ABS 64]，其中把克利福德代数应用于各种拓扑问题，特别描述了实数上的克利福德代数与球面上向量场的存在性之间的关系。克利福德代数中的乘法给出球面上的乘法，进而给出向量场。[ABS 64] 还给出许多关于克利福德代数及其在拓扑、物理中的应用的计算。例如，设 $E=\mathbf R^n$，$g$ 为标准点积的负值。或者以更具不变性的方式，取 $E$ 为 $\mathbf R$ 上的 $n$ 维向量空间，$g$ 为 $E$ 上的*负定*对称形式。令 $C_n=C(g)$。

运算

$$
v_1\otimes\cdots\otimes v_r\mapsto v_r\otimes\cdots\otimes v_1=(v_1\otimes\cdots\otimes v_r)^*\qquad(v_i\in E)
$$

对 $r\ge0$ 诱导 $T^r(E)$ 的自同态。由于 $v\otimes v-g(v,v)\cdot1$（$v\in E$）在此运算下不变，便有诱导自同态 $*:C_n\to C_n$。它实际上是一个对合，即对 $x\in C_n$，有 $x^{**}=x$ 及 $(xy)^*=y^*x^*$。用 $\operatorname{Spin}(n)$ 表示 $C_n$ 的可逆元中由 $E$ 的单位球面（即满足 $g(v,v)=-1$ 的元素集合）生成的群的、位于 $C_n$ 偶部分中的子群。等价地，$\operatorname{Spin}(n)$ 是满足 $xx^*=1$ 的元素 $x$ 的群。

> **译校注：** 最后一句须保留前一句所述的群的范围，不能把“$xx^*=1$”单独当作任意 $x\in C_n$ 属于自旋群的充分条件。例如 $n=3$ 时，取正交单位向量的像 $e_1,e_2,e_3$，满足 $e_i^2=-1$，令 $\omega=e_1e_2e_3$。则 $\omega^2=1$、$\omega^*=-\omega$，所以 $x=\sqrt2+\omega$ 满足 $xx^*=2-\omega^2=1$，却因有非零奇部分而不属于前一句定义的自旋群。英文保留原句。

这个名称可追溯到狄拉克，他在研究电子自旋时使用了这个群。拓扑学家等将其视为特殊正交群 $SO(n)=SU_n(\mathbf R)$ 的普适覆盖群。

**译校注：** 原文“普适覆盖群”的说法须取 $n\ge3$。在 $n=2$ 时，$\operatorname{Spin}(2)\cong S^1$ 到 $SO(2)\cong S^1$ 的映射是二重覆盖；圆的普适覆盖群为加法群 $\mathbf R$，所以此时不能称为普适覆盖。这里保留原句并说明维数条件。

在 [Hu 75] 第 11 章中也可找到 [Ad 62] 及 [ABS 64] 的一些结果的论述。其次，我提到跨越二十年的两项工作，涉及热核、狄拉克算子、指标定理及数论，从 Atiyah、Bott、Patodi [ABP 73] 到 Faltings [Fa 91]，特别参阅题为“The local index theorem for Dirac operators”的 §4。这套一般理论所应用的向量空间，主要是流形上一点的余切空间。我推荐 [BGV 92] 第 3 章。

最后，关于克利福德代数在表示论中的应用，可参阅 Bröcker 与 Tom Dieck [BtD 85]，从他们的第一章 §6 开始。

### 参考文献

[Ad 62] F. Adams，Vector Fields on Spheres，*Ann. Math.* **75**（1962），第 603–632 页。

[ABP 73] M. Atiyah、R. Bott、V. Patodi，On the heat equation and the index theorem，*Invent. Math.* **19**（1973），第 270–330 页；勘误 **38**（1975），第 277–280 页。

<span class="original-page-anchor" id="pdf-page-761" aria-hidden="true"></span>

[ABS 64] M. Atiyah、R. Bott、A. Shapiro，Clifford Modules，*Topology* **第 3 卷，增刊 1**（1964），第 3–38 页。

[BGV 92] N. Berline、E. Getzler、M. Vergne，*Heat Kernels and Dirac Operators*，Springer Verlag，1992。

[BtD 85] T. Bröcker、T. Tom Dieck，*Representations of Compact Lie Groups*，Springer Verlag，1985。

[Fa 91] G. Faltings，*Lectures on the arithmetic Riemann-Roch theorem*，Annals of Math. Studies，1991。

[Hu 75] D. Husemoller，*Fibre Bundles*，Springer Verlag，第二版，1975。

## 习题

**1。** 设 $E$ 为域 $k$ 上有限维向量空间，$x_1,\ldots,x_p$ 为 $E$ 的元素，满足 $x_1\wedge\cdots\wedge x_p\ne0$，同样有 $y_1\wedge\cdots\wedge y_p\ne0$。若 $c\in k$ 且

$$
x_1\wedge\cdots\wedge x_p=cy_1\wedge\cdots\wedge y_p,
$$

证明 $x_1,\ldots,x_p$ 与 $y_1,\ldots,y_p$ 生成同一子空间。因此，$\bigwedge^p E$ 中相差非零标量倍数的非零可分解向量，对应于 $E$ 的 $p$ 维子空间。

**2。** 设 $E$ 为交换环 $R$ 上维数 $n$ 的自由模，$f:E\to E$ 为线性映射。令 $\alpha_r(f)=\operatorname{tr}\bigwedge^r(f)$，其中 $\bigwedge^r(f)$ 为 $f$ 诱导的从 $\bigwedge^r(E)$ 到自身的自同态。有

$$
\alpha_0(f)=1,\qquad\alpha_1(f)=\operatorname{tr}(f),\qquad\alpha_n(f)=\det f,
$$

且若 $r>n$，则 $\alpha_r(f)=0$。证明

$$
\det(1+f)=\sum_{r\ge0}\alpha_r(f).
$$

［**提示：** 按通常方法，在 $f$ 由整数上具有变量系数的矩阵表示时证明此命题。］用 $f$ 的特征多项式的系数解释 $\alpha_r(f)$。

**3。** 设 $E$ 为交换环 $R$ 上的有限维自由模，$E^\vee$ 为其对偶模。对每个整数 $r\ge1$，证明在以下双线性映射下，$\bigwedge^r E$ 与 $\bigwedge^r E^\vee$ 互为对偶模：

$$
(v_1\wedge\cdots\wedge v_r,v'_1\wedge\cdots\wedge v'_r)\mapsto\det(\langle v_i,v'_j\rangle),
$$

其中通常记 $\langle v_i,v'_j\rangle$ 为 $v'_j$ 在 $v_i$ 上的值，$v_i\in E$、$v'_j\in E^\vee$。

**4。** 记号同前题。设 $F$ 为另一个有限维自由 $R$ 模，$f:E\to F$ 为线性映射。相对于前题的双线性映射，证明 $\bigwedge^r f$ 的转置为 $\bigwedge^r({}^tf)$，即等于 $f$ 的转置的第 $r$ 次交错积。

**5。** 设 $R$ 为交换环。若 $E$ 为 $R$ 模，用 $L_a^r(E)$ 表示<span class="original-page-anchor" id="pdf-page-762" aria-hidden="true"></span>从 $E$ 到 $R$ 本身的 *$r$ 重线性交替映射*（即 $E$ 上的 $r$ 重线性交替形式）构成的模。令 $L_a^0(E)=R$，并令

$$
\Omega(E)=\bigoplus_{r=0}^\infty L_a^r(E).
$$

证明 $\Omega(E)$ 是分次 $R$ 代数，乘法如下定义：若 $\omega\in L_a^r(E)$，$\psi\in L_a^s(E)$，且 $v_1,\ldots,v_{r+s}$ 为 $E$ 的元素，则

$$
(\omega\wedge\psi)(v_1,\ldots,v_{r+s})=\sum\varepsilon(\sigma)\omega(v_{\sigma1},\ldots,v_{\sigma r})\psi(v_{\sigma(r+1)},\ldots,v_{\sigma(r+s)}),
$$

其中求和遍历 $(1,\ldots,r+s)$ 的所有置换 $\sigma$，满足 $\sigma1<\cdots<\sigma r$ 及 $\sigma(r+1)<\cdots<\sigma(r+s)$。

> **译校注：** 原书公式中 $\psi$ 的最后一个自变量下标印为 $\sigma s$，后面的顺序条件也止于 $\sigma s$。由于 $\psi$ 为 $s$ 重线性，必须取第 $r+1$ 至第 $r+s$ 个位置，共 $s$ 个自变量，故两处均应止于 $\sigma(r+s)$。英文保留原印。

### 导子

*以下关于导子的习题中，所有环均假设交换。* 这些习题除其他内容外，也给出泛导子存在性的另一种证明。

设 $R\to A$ 为 $R$ 代数（根据约定，所涉及的环均交换）。用 $(d_{A/R},\Omega_{A/R}^1)$ 表示 $A$ 在 $R$ 上的泛导子模，但不假设它必然存在。若所指的 $A/R$ 很清楚，有时为简便写 $d$ 而不写 $d_{A/R}$。

**6。** 设 $A=R[X_\alpha]$ 为变量 $X_\alpha$ 的多项式环，$\alpha$ 遍历某个可能无限的指标集。设 $\Omega$ 为以符号 $dX_\alpha$ 为基的自由 $A$ 模，设

$$
d:A\to\Omega
$$

为由下式定义的映射：

$$
df(X)=\sum_\alpha\frac{\partial f}{\partial X_\alpha}\,dX_\alpha.
$$

证明二元组 $(d,\Omega)$ 是泛导子 $(d_{A/R},\Omega_{A/R}^1)$。

**7。** 设 $A\to B$ 为 $R$ 代数同态。假设 $A/R,B/R,B/A$ 的泛导子均存在。证明有自然正合列：

$$
B\otimes_A\Omega_{A/R}^1\to\Omega_{B/R}^1\to\Omega_{B/A}^1\to0.
$$

［**提示：** 考虑序列

$$
0\to\operatorname{Der}_A(B,M)\to\operatorname{Der}_R(B,M)\to\operatorname{Der}_R(A,M),
$$

并证明它正合。利用如下事实：$B$ 模序列

$$
N'\to N\to N''\to0
$$

正合，当且仅当对每个 $B$ 模 $M$，其到 $M$ 的 Hom 序列正合。将此应用于导子序列。］

**8。** 设 $R\to A$ 为 $R$ 代数，$I$ 为 $A$ 的理想，$B=A/I$。假设 $A$ 在 $R$ 上的泛导子存在。证明 $B$ 在 $R$ 上的泛导子<span class="original-page-anchor" id="pdf-page-763" aria-hidden="true"></span>也存在，并且有自然正合列

$$
I/I^2\xrightarrow{d_{A/R}}B\otimes_A\Omega_{A/R}^1\to\Omega_{B/R}^1\to0.
$$

［**提示：** 设 $M$ 为 $B$ 模。证明序列

$$
0\to\operatorname{Der}_R(B,M)\to\operatorname{Der}_R(A,M)\to\operatorname{Hom}_B(I/I^2,M)
$$

正合。］

**9。** 设 $R\to B$ 为 $R$ 代数。如下证明 $B$ 在 $R$ 上的泛导子存在：把 $B$ 表示为多项式环的商，允许有无限多个变量；应用习题 6 和 7。

**译校注：** 原书引用“习题 6 和 7”。习题 6 给出多项式环的泛导子，而将其下降到商环并证明存在的题目是习题 8；习题 7 的前提已经包括 $B/R$ 的泛导子存在，故不能用该题单独建立这里的存在性。此处所需的构造应应用习题 6 和 8；保留原引用并说明其所指。

**10。** 设 $R\to A$ 为 $R$ 代数，$S_0$ 为 $R$ 的乘法子集，$S$ 为 $A$ 的乘法子集，且 $S_0$ 映入 $S$。证明 $S^{-1}A$ 在 $S_0^{-1}R$ 上的泛导子是 $(d,S^{-1}\Omega_{A/R}^1)$，其中

$$
d(a/s)=(s\,d_{A/R}(a)-a\,d_{A/R}(s))/s^2.
$$

**11。** 设 $B$ 为 $R$ 代数，$M$ 为 $B$ 模。在 $B\oplus M$ 上定义乘法

$$
(b,x)(b',y)=(bb',by+b'x).
$$

将 $b\in B$ 与 $(b,0)$ 等同后，证明 $B\oplus M$ 为 $B$ 代数。对任意 $R$ 代数 $A$，证明代数同态 $\operatorname{Hom}_{\mathrm{Alg}/R}(A,B\oplus M)$ 由二元组 $(\varphi,D)$ 构成，其中 $\varphi:A\to B$ 为代数同态，$D:A\to M$ 为 $\varphi$ 诱导的 $M$ 上的 $A$ 模结构的导子。

**12。** 设 $A$ 为 $R$ 代数，$\varepsilon:A\to R$ 为代数同态，称其为**增广映射**。设 $M$ 为 $R$ 模。通过 $\varepsilon$ 在 $M$ 上定义 $A$ 模结构：

$$
a\cdot x=\varepsilon(a)x\qquad(a\in A,\ x\in M).
$$

用 $M_\varepsilon$ 表示具有这个新模结构的 $M$。令

$$
\begin{gathered}
\operatorname{Der}_\varepsilon(A,M)=\text{对于 }M\text{ 上的 }\varepsilon\text{ 模结构的导子构成的 }A\text{ 模},\\
I=\operatorname{Ker}\varepsilon.
\end{gathered}
$$

则 $\operatorname{Der}_\varepsilon(A,M)$ 为 $A/I$ 模。注意，有 $R$ 模的直和分解 $A=R\oplus I$。证明存在自然的 $A$ 模同构

$$
\Omega_{A/R}/I\Omega_{A/R}\approx I/I^2
$$

及 $R$ 模同构

$$
\operatorname{Der}_\varepsilon(A,M)\approx\operatorname{Hom}_R(I/I^2,M).
$$

特别地，设 $\eta:A\to I/I^2$ 为相对于直和分解 $A=R\oplus I$ 从 $A$ 到 $I/I^2$ 的投影，则 $\eta$ 为泛 $\varepsilon$ 导子。

### 导子与联络

**13。** 设 $R\to A$ 为交换环同态，因而将 $A$ 视为 $R$ 代数。

<span class="original-page-anchor" id="pdf-page-764" aria-hidden="true"></span>

设 $E$ 为 $A$ 模。$E$ 上的**联络**是阿贝尔群同态

$$
\nabla:E\to\Omega_{A/R}^1\otimes_A E,
$$

使对 $a\in A$、$x\in E$，有

$$
\nabla(ax)=a\nabla(x)+da\otimes x.
$$

除非另有说明，张量积均取在 $A$ 上。$\nabla$ 的核记作 $E_\nabla$，称为 $(E,\nabla)$ 的**水平元素子模**，或**水平子模**。

**译校注：** 此处“子模”指 $R$ 子模；一般不是 $A$ 子模。由联络规则，$\nabla(rx)=r\nabla(x)$ 对 $r\in R$ 成立，而对一般 $a\in A$ 还有 $da\otimes x$ 项。例如 $A=k[t]$、$E=A$、$\nabla=d$ 时，$1$ 水平而 $t\cdot1$ 不水平。原文名称保留，明确其基环。

**（a）** 对任意整数 $i\ge1$，定义

$$
\Omega_{A/R}^i=\bigwedge^i\Omega_{A/R}^1.
$$

证明 $\nabla$ 可延拓为 $R$ 模同态

$$
\nabla_i:\Omega_{A/R}^i\otimes E\to\Omega_{A/R}^{i+1}\otimes E,
$$

定义为

$$
\nabla_i(\omega\otimes x)=d\omega\otimes x+(-1)^i\omega\wedge\nabla(x).
$$

**（b）** 将联络的**曲率**定义为映射

$$
K=\nabla_1\circ\nabla:E\to\Omega_{A/R}^2\otimes_A E.
$$

证明 $K$ 为 $A$ 同态，并证明对 $\omega\in\Omega_{A/R}^i$、$x\in E$，有

$$
\nabla_{i+1}\circ\nabla_i(\omega\otimes x)=\omega\wedge K(x).
$$

**（c）** 用 $\operatorname{Der}(A/R)$ 表示从 $A$ 到自身的 $R$ 上导子构成的 $A$ 模。设 $\nabla$ 为 $E$ 上的联络。证明 $\nabla$ 诱导唯一的 $A$ 线性映射

$$
\nabla:\operatorname{Der}(A/R)\to\operatorname{End}_R(E),
$$

满足

$$
\nabla(D)(ax)=D(a)x+a\nabla(D)(x).
$$

**（d）** 证明公式

$$
[\nabla(D_1),\nabla(D_2)]-\nabla([D_1,D_2])=(D_1\wedge D_2)(K).
$$

其中对 $E$ 的两个自同态 $f,g$，括号定义为 $[f,g]=f\circ g-g\circ f$。右边是以下复合映射：

$$
E\xrightarrow{K}\Omega_{A/R}^2\otimes E\xrightarrow{D_1\wedge D_2}A\otimes E\approx E.
$$

<span class="original-page-anchor" id="pdf-page-765" aria-hidden="true"></span>

**14。（a）** 对环 $A$ 到自身的任意导子 $D$，证明**莱布尼茨法则**：

$$
D^n(xy)=\sum_{i=0}^n\binom ni D^i(x)D^{n-i}(y).
$$

**（b）** 假设 $A$ 的特征为 $p$。证明 $D^p$ 为导子。

**15。** 设 $A/R$ 为代数，$E$ 为具有联络 $\nabla$ 的 $A$ 模。假设 $R$ 的特征为 $p$。定义

$$
\psi:\operatorname{Der}(A/R)\to\operatorname{End}_R(E),
$$

由

$$
\psi(D)=(\nabla(D))^p-\nabla(D^p)
$$

给出。证明 $\psi(D)$ 为 $A$ 线性的。［**提示：** 使用莱布尼茨公式与联络的定义。］因此，$\psi$ 的像实际上包含在 $\operatorname{End}_A(E)$ 中。

### 若干克利福德代数习题

**16。** 设 $C_g(E)$ 为 §4 定义的克利福德代数。将 $E$ 视为嵌入 $C_g$，定义 $F_i(C_g)=(k+E)^i$。在交错代数中定义类似对象 $F_i(\bigwedge E)$。两种情形中均有 $F_{i+1}\supset F_i$，定义第 $i$ 个分次模 $\operatorname{gr}_i=F_i/F_{i-1}$。证明存在自然的（具有函子性的）同构

$$
\operatorname{gr}_i(C_g(E))\xrightarrow{\approx}\operatorname{gr}_i(\bigwedge E).
$$

**17。** 假设 $k=\mathbf R$，因此 $E$ 为实向量空间，现在假设其维数为偶数 $2m$。还假设 $g$ 非退化。由于对称形式已固定，省略下标 $g$；用 $C^+,C^-$ 分别表示 $\mathbf Z/2\mathbf Z$ 分次中次数 $0$ 和 $1$ 的空间。对 $C^+$ 或 $C^-$ 中的元素 $x,y$，定义其**超交换子**为

$$
\{x,y\}=xy-(-1)^{(\deg x)(\deg y)}yx.
$$

证明 $F_{2m-1}$ 由超交换子生成。

**18。** 仍假设 $g$ 非退化。设 $J$ 为 $(E,g)$ 的自同构（即对所有 $x,y\in E$，有 $g(Jx,Jy)=g(x,y)$），且 $J^2=-\mathrm{id}$。设 $E_{\mathbf C}=\mathbf C\otimes_{\mathbf R}E$ 为从 $\mathbf R$ 到 $\mathbf C$ 的标量扩张。那么 $E_{\mathbf C}$ 有直和分解

$$
E_{\mathbf C}=E_{\mathbf C}^+\oplus E_{\mathbf C}^-,
$$

分解为 $J$ 的特征空间，其特征值分别为 $i$ 和 $-i$。（证明？）

> **译校注：** 原书将特征值印为 $1$ 和 $-1$。由 $J^2=-\mathrm{id}$，复特征值 $\lambda$ 满足 $\lambda^2=-1$，故应为 $i,-i$。

有 $E_{\mathbf C}$ 在 $\bigwedge E_{\mathbf C}^+$ 上的表示，即同态 $E_{\mathbf C}\to\operatorname{End}_{\mathbf C}(\bigwedge E_{\mathbf C}^+)$，其中 $E_{\mathbf C}^+$ 的元素以外乘作用，$E_{\mathbf C}^-$ 的元素以内乘作用，定义如下。

> **译校注：** 原书本句的 $\operatorname{End}_{\mathbf C}(E_{\mathbf C}^+)$ 漏了外代数符号。该句已说作用在 $\bigwedge E_{\mathbf C}^+$ 上，且下一页结论明确写作 $\operatorname{End}_{\mathbf C}(\bigwedge E_{\mathbf C}^+)$，这里据此补回。

对 $x'\in E_{\mathbf C}^-$，存在唯一的 $\mathbf C$ 线性映射，具有以下作用：

$$
x'(x_1\wedge\cdots\wedge x_r)=-2\sum_{i=1}^r(-1)^{i-1}\langle x',x_i\rangle\,x_1\wedge\cdots\wedge\widehat{x_i}\wedge\cdots\wedge x_r.
$$

> **译校注：** 本页未明确说明尖括号配对的符号约定，因此保留原式的 $-2$，不猜改。若 $\langle\ ,\ \rangle$ 就是 $g$ 的复双线性延拓，则外乘与此内乘的反交换子为 $-2g(x',x)$，所得平方关系是 $\rho(x)^2=-g(x,x)$，与 §4 定义 $C_g(E)$ 时的正号约定相反。要得到下一页所述的 $C_g(E)$ 表示，应在这一解释下把系数取为 $+2$，或明确将尖括号配对取为 $-g$；这两种配对约定不应混用。

<span class="original-page-anchor" id="pdf-page-766" aria-hidden="true"></span>

证明在此运算下，得到同构

$$
C_g(E)_{\mathbf C}\to\operatorname{End}_{\mathbf C}(\bigwedge E_{\mathbf C}^+).
$$

［**提示：** 比较维数。］

**19。** 考虑 $\mathbf R$ 上的克利福德代数。当 $E=\mathbf R^n$ 带有负定形式时，标准记号是 $C_n$；带有正定形式时，标准记号是 $C'_n$。因此 $\dim C_n=\dim C'_n=2^n$。

**（a）** 证明

$$
\begin{aligned}
C_1&\approx\mathbf C& C_2&\approx\mathbf H\quad\text{（四元数除环）},\\
C'_1&\approx\mathbf R\times\mathbf R& C'_2&\approx M_2(\mathbf R)\quad\text{（}\mathbf R\text{ 上的 }2\times2\text{ 矩阵）}.
\end{aligned}
$$

**20。** 建立同构：

$$
\mathbf C\otimes_{\mathbf R}\mathbf C\approx\mathbf C\times\mathbf C;\qquad\mathbf C\otimes_{\mathbf R}\mathbf H\approx M_2(\mathbf C);\qquad\mathbf H\otimes_{\mathbf R}\mathbf H\approx M_4(\mathbf R),
$$

其中 $M_d(F)$ 为 $F$ 上的 $d\times d$ 矩阵。对于第三个，即 $\mathbf H\otimes\mathbf H$，定义同构

$$
f:\mathbf H\otimes_{\mathbf R}\mathbf H\to\operatorname{Hom}_{\mathbf R}(\mathbf H,\mathbf H)\approx M_4(\mathbf R),
$$

由 $f(x\otimes y)(z)=xz\bar y$ 给出，其中若 $y=y_0+y_1i+y_2j+y_3k$，则

$$
\bar y=y_0-y_1i-y_2j-y_3k.
$$

**21。（a）** 建立同构

$$
C_{n+2}\approx C'_n\otimes C_2,\qquad C'_{n+2}\approx C_n\otimes C'_2.
$$

［**提示：** 设 $\{e_1,\ldots,e_{n+2}\}$ 为满足 $e_i^2=-1$ 的规范正交基。对于第一个同构，对 $i=1,\ldots,n$，令 $e_i\mapsto e'_i\otimes e_1e_2$，并分别把 $e_{n+1},e_{n+2}$ 映到 $1\otimes e_1$、$1\otimes e_2$。］

**（b）** 证明 $C_{n+8}\approx C_n\otimes M_{16}(\mathbf R)$，这称为**周期性性质**。

**（c）** 推出对所有 $n$，$C_n$ 都是 $\mathbf R$ 上的半单代数。

由（c）可列出 $C_n$ 上的单模表。见 [ABS 64]，此表也重载于 Husemoller [Hu 75] 第 11 章 §6。
