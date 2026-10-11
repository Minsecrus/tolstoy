---
title: "第四章 多项式"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第三章 模","link":"/library/volume-86/chapter-003"}
next: {"text":"第二部分导言：代数方程","link":"/library/volume-86/part-02"}
---

# 第四章 多项式

<span class="original-page-anchor" id="pdf-page-188" aria-hidden="true"></span>

本章接续第二章 §3。我们将证明多项式的标准性质。多数读者已经熟悉其中一些性质，尤其是开头关于一元多项式的性质。不过，我们的目的之一是说明：经过适当表述，其中一些性质在交换环上也成立。高斯引理以及不可约性的约化判别法将说明在环上讨论问题的重要性。第九章将给出一些例子，说明为了得到泛关系，在整数 $\mathbf{Z}$ 本身上讨论问题的重要性。有些代数命题具有普遍的有效性。要证明它们，先对 $\mathbf{Z}$ 上多项式环的元素证明，再通过特殊化，得到任意域（或视情况而定的交换环）中的命题。例如，第十五章中的凯莱–哈密顿定理就可以用这种方式证明。

最后一节关于幂级数的内容说明，多项式环的基本性质可以表述为也适用于幂级数环的形式。在该节末尾，我将给出几个例子，说明幂级数在数学各个领域中的重要性。

## §1. 一元多项式的基本性质

我们从欧几里得算法开始。

**定理 1.1。** *设 $A$ 为交换环，$f,g\in A[X]$ 为次数 $\geqq0$ 的一元多项式，并假设 $g$ 的首项* <span class="original-page-anchor" id="pdf-page-189" aria-hidden="true"></span>*系数是 $A$ 中的可逆元。则存在唯一的多项式 $q,r\in A[X]$，满足*

$$
f=gq+r
$$

*且 $\deg r<\deg g$。*

*证明。* 写成

$$
\begin{aligned}
f(X)&=a_nX^n+\cdots+a_0,\\
g(X)&=b_dX^d+\cdots+b_0,
\end{aligned}
$$

其中 $n=\deg f$、$d=\deg g$，所以 $a_n,b_d\ne0$，且 $b_d$ 为 $A$ 中的可逆元。对 $n$ 使用归纳法。

若 $n=0$ 且 $\deg g>\deg f$，令 $q=0$、$r=f$。若 $\deg g=\deg f=0$，则令 $r=0$、$q=a_nb_d^{-1}$。

假设定理对次数 $<n$ 的多项式已成立（其中 $n>0$）。可以假设 $\deg g\leqq\deg f$（否则，取 $q=0$、$r=f$）。于是

$$
f(X)=a_nb_d^{-1}X^{n-d}g(X)+f_1(X),
$$

其中 $f_1(X)$ 的次数 $<n$。由归纳假设，可以找到 $q_1,r$，使得

$$
f(X)=a_nb_d^{-1}X^{n-d}g(X)+q_1(X)g(X)+r(X)
$$

且 $\deg r<\deg g$。于是令

$$
q(X)=a_nb_d^{-1}X^{n-d}+q_1(X),
$$

就完成了 $q,r$ 的存在性证明。

至于唯一性，假设

$$
f=q_1g+r_1=q_2g+r_2,
$$

其中 $\deg r_1<\deg g$、$\deg r_2<\deg g$。相减得

$$
(q_1-q_2)g=r_2-r_1.
$$

由于假设 $g$ 的首项系数可逆，有

$$
\deg(q_1-q_2)g=\deg(q_1-q_2)+\deg g.
$$

因为 $\deg(r_2-r_1)<\deg g$，这一关系只有在 $q_1-q_2=0$ 时才可能成立，即 $q_1=q_2$，最终得到 $r_1=r_2$，证毕。

**定理 1.2。** *设 $k$ 为域。则一元多项式环 $k[X]$ 是主理想整环。*

<span class="original-page-anchor" id="pdf-page-190" aria-hidden="true"></span>

*证明。* 设 $\mathfrak{a}$ 为 $k[X]$ 的理想，并假设 $\mathfrak{a}\ne0$。取 $\mathfrak{a}$ 中次数 $\geqq0$ 且最小的元素 $g$。设 $f$ 为 $\mathfrak{a}$ 中任意非零元素。由欧几里得算法，可找到 $q,r\in k[X]$，满足

$$
f=qg+r
$$

且 $\deg r<\deg g$。而 $r=f-qg$，故 $r\in\mathfrak{a}$。由于 $g$ 的次数在 $\geqq0$ 的次数中最小，必有 $r=0$，所以 $\mathfrak{a}$ 由所有多项式 $qg$（其中 $q\in k[X]$）组成。这就证明了定理。由第二章定理 5.2 得到：

**推论 1.3。** *环 $k[X]$ 是唯一分解整环。*

若 $k$ 为域，则 $k$ 的每个非零元素都是 $k$ 中的可逆元，并且立即可见，$k[X]$ 的可逆元恰为 $k$ 的可逆元。（由乘积次数的加法公式，次数 $\geqq1$ 的多项式不可能是可逆元。）

若多项式 $f(X)\in k[X]$ 的次数 $\geqq1$，并且不能将 $f(X)$ 写成乘积

$$
f(X)=g(X)h(X),
$$

其中 $g,h\in k[X]$ 且二者均不属于 $k$，则称其为**不可约多项式**。$k$ 的元素通常称为**常数多项式**，因此也可以说，在这样的分解中，$g,h$ 至少有一个必须是常数。首项系数为 $1$ 的多项式称为**首一多项式**。

设 $A$ 为交换环，$f(X)$ 为 $A[X]$ 中的多项式。设 $A$ 为 $B$ 的子环。若元素 $b\in B$ 满足 $f(b)=0$，则称 $b$ 为 $f$ 在 $B$ 中的一个**根**或**零点**。同样，若 $(X)$ 为变量的 $n$ 元组，则满足 $f(b)=0$ 的 $n$ 元组 $(b)$ 称为 $f$ 的一个零点。

**定理 1.4。** *设 $k$ 为域，$f$ 为 $k[X]$ 中变量为 $X$ 的一元多项式，次数为 $n\geqq0$。则 $f$ 在 $k$ 中至多有 $n$ 个根；若 $a$ 为 $f$ 在 $k$ 中的一个根，则 $X-a$ 整除 $f(X)$。*

*证明。* 假设 $f(a)=0$。找到 $q,r$，使得

$$
f(X)=q(X)(X-a)+r(X)
$$

且 $\deg r<1$。于是

$$
0=f(a)=r(a).
$$

由于 $r=0$ 或 $r$ 是非零常数，必有 $r=0$，故 $X-a$ 整除 $f(X)$。若 $a_1,\ldots,a_m$ 为 $f$ 在 $k$ 中的互异根，则通过归纳可见，乘积

$$
(X-a_1)\cdots(X-a_m)
$$

<span class="original-page-anchor" id="pdf-page-191" aria-hidden="true"></span>

整除 $f(X)$，于是 $m\leqq n$，定理得证。接下来的推论给出定理 1.4 对多项式函数的应用。

**推论 1.5。** *设 $k$ 为域，$T$ 为 $k$ 的无限子集。设 $f(X)\in k[X]$ 为一元多项式。若对所有 $a\in T$ 都有 $f(a)=0$，则 $f=0$，即 $f$ 诱导零函数。*

**推论 1.6。** *设 $k$ 为域，$S_1,\ldots,S_n$ 为 $k$ 的无限子集。设 $f(X_1,\ldots,X_n)$ 为 $k$ 上的 $n$ 元多项式。若对所有 $a_i\in S_i$（$i=1,\ldots,n$）都有 $f(a_1,\ldots,a_n)=0$，则 $f=0$。*

*证明。* 使用归纳法。我们刚刚已知结论对一个变量成立。设 $n\geqq2$，并写成

$$
f(X_1,\ldots,X_n)=\sum_j f_j(X_1,\ldots,X_{n-1})X_n^j,
$$

将其视为系数属于 $k[X_1,\ldots,X_{n-1}]$ 的关于 $X_n$ 的多项式。若存在

$$
(b_1,\ldots,b_{n-1})\in S_1\times\cdots\times S_{n-1},
$$

使某个 $j$ 满足 $f_j(b_1,\ldots,b_{n-1})\ne0$，则

$$
f(b_1,\ldots,b_{n-1},X_n)
$$

是 $k[X_n]$ 中的非零多项式，却在无限集合 $S_n$ 的所有元素处取值 $0$。这不可能。因此，对所有 $j$，$f_j$ 在 $S_1\times\cdots\times S_{n-1}$ 上都诱导零函数；由归纳假设，所有 $j$ 均满足 $f_j=0$。故 $f=0$，证毕。

**推论 1.7。** *设 $k$ 为无限域，$f$ 为 $k$ 上的 $n$ 元多项式。若 $f$ 在 $k^{(n)}$ 上诱导零函数，则 $f=0$。*

现在考虑有限域的情形。设 $k$ 为具有 $q$ 个元素的有限域，$f(X_1,\ldots,X_n)$ 为 $k$ 上的 $n$ 元多项式。写成

$$
f(X_1,\ldots,X_n)=\sum a_{(\nu)}X_1^{\nu_1}\cdots X_n^{\nu_n}.
$$

回顾一下，若 $a_{(\nu)}\ne0$，则单项式 $M_{(\nu)}(X)$ 出现在 $f$ 中。假设是这种情形，并且在这个单项式 $M_{(\nu)}(X)$ 中，某个变量 $X_i$ 的指数满足 $\nu_i\geqq q$。可以写成

$$
X_i^{\nu_i}=X_i^{q+\mu},\quad\mu=\text{整数 }\geqq0.
$$

若在这个单项式中把 $X_i^{\nu_i}$ 替换为 $X_i^{\mu+1}$，则得到一个新多项式，它与 $f$ 诱导同一函数。这个新多项式的次数至多等于 $f$ 的次数。

<span class="original-page-anchor" id="pdf-page-192" aria-hidden="true"></span>

对 $f$ 中出现的所有单项式以及所有变量 $X_1,\ldots,X_n$，有限次地实施上述操作，就得到一个多项式 $f^*$，它与 $f$ 诱导同一函数，但对每个变量的次数均 $<q$。

**推论 1.8。** *设 $k$ 为具有 $q$ 个元素的有限域。设 $f$ 为 $k$ 上的 $n$ 元多项式，且 $f$ 对每个变量的次数均 $<q$。若 $f$ 在 $k^{(n)}$ 上诱导零函数，则 $f=0$。*

*证明。* 使用归纳法。若 $n=1$，则 $f$ 的次数 $<q$，所以除非 $f=0$，否则不可能有 $q$ 个根。归纳步骤与前面推论 1.6 的证明完全相同。

设 $f$ 为有限域 $k$ 上的 $n$ 元多项式。若多项式 $g$ 对每个变量的次数均 $<q$，就称其为**约化的**。前面已经证明，存在约化多项式 $f^*$，它在 $k^{(n)}$ 上与 $f$ 给出同一函数。现在推论 1.8 表明，*这个约化多项式是唯一的*。事实上，若 $g_1,g_2$ 为给出同一函数的约化多项式，则 $g_1-g_2$ 约化且给出零函数。因此 $g_1-g_2=0$，从而 $g_1=g_2$。

> **译校注：** 原文此处写作 “Theorem 1.8”（定理 1.8）；本节编号 1.8 的结果实际为上文的 “Corollary 1.8”（推论 1.8），故译文按推论引用。

我们再给出定理 1.4 的一个应用。设 $k$ 为域。$k$ 的**乘法子群**是指群 $k^*$（$k$ 的非零元素）的一个子群。

**定理 1.9。** *设 $k$ 为域，$U$ 为 $k$ 的一个有限乘法子群。则 $U$ 为循环群。*

*证明。* 将 $U$ 写成对应各个素数 $p$ 的子群 $U(p)$ 的乘积，其中 $U(p)$ 为 $p$ 群。由第一章命题 4.3(v)，只需证明每个 $U(p)$ 都是循环群。取 $U(p)$ 中周期最大的元素 $a$，其周期为某个整数 $r$ 对应的 $p^r$。于是对每个 $x\in U(p)$，都有 $x^{p^r}=1$，所以 $U(p)$ 的所有元素都是多项式

$$
X^{p^r}-1
$$

的根。$a$ 生成的循环群有 $p^r$ 个元素。若这个循环群不等于 $U(p)$，则该多项式有多于 $p^r$ 个根，这是不可能的。因此 $a$ 生成 $U(p)$，定理得证。

**推论 1.10。** *若 $k$ 为有限域，则 $k^*$ 为循环群。*

若域 $k$ 中的元素 $\zeta$ 满足：存在整数 $n\geqq1$ 使得 $\zeta^n=1$，则称其为**单位根**，更确切地说，为 **$n$ 次单位根**。因此，$n$ 次单位根的集合就是多项式 $X^n-1$ 的根的集合。这样的根至多有 $n$ 个，并且显然构成一个群；这个群<span class="original-page-anchor" id="pdf-page-193" aria-hidden="true"></span>由定理 1.9 可知为循环群。以后我们将更详细地研究单位根。$n$ 次单位根群的生成元称为**本原 $n$ 次单位根**。例如，在复数中，$e^{2\pi i/n}$ 为本原 $n$ 次单位根，而 $n$ 次单位根均形如 $e^{2\pi i\nu/n}$，其中 $1\leqq\nu\leqq n$。

单位根群记为 $\boldsymbol{\mu}$。域 $K$ 中的单位根群记为 $\boldsymbol{\mu}(K)$。

若 $k[X]$ 中每个次数 $\geqq1$ 的多项式在 $k$ 中都有根，则称域 $k$ 为**代数闭域**。分析学书籍证明了复数域是代数闭的。第五章将证明，域 $k$ 总包含在某个代数闭域中。若 $k$ 代数闭，则 $k[X]$ 中的不可约多项式就是次数为 $1$ 的多项式。在这种情况下，次数 $\geqq0$ 的多项式 $f$ 的唯一分解可写为

$$
f(X)=c\prod_{i=1}^{r}(X-\alpha_i)^{m_i},
$$

其中 $c\in k$、$c\ne0$，且根 $\alpha_1,\ldots,\alpha_r$ 互异。接下来，我们建立判别 $m_i>1$ 的方法。

设 $A$ 为交换环。定义多项式环到自身的映射

$$
D:A[X]\to A[X].
$$

若 $f(X)=a_nX^n+\cdots+a_0$，其中 $a_i\in A$，则定义**导数**

$$
Df(X)=f'(X)=\sum_{\nu=1}^{n}\nu a_\nu X^{\nu-1}=na_nX^{n-1}+\cdots+a_1.
$$

很容易验证，若 $f,g$ 为 $A[X]$ 中的多项式，则

$$
(f+g)'=f'+g',\quad(fg)'=f'g+fg';
$$

若 $a\in A$，则

$$
(af)'=af'.
$$

设 $K$ 为域，$f$ 为 $K[X]$ 中的非零多项式，$a$ 为 $f$ 在 $K$ 中的根。可以写成

$$
f(X)=(X-a)^mg(X),
$$

其中多项式 $g(X)$ 与 $X-a$ 互素（所以 $g(a)\ne0$）。称 $m$ 为 $a$ 在 $f$ 中的**重数**，并且当 $m>1$ 时，称 $a$ 为**重根**。

<span class="original-page-anchor" id="pdf-page-194" aria-hidden="true"></span>

**命题 1.11。** *设 $K,f$ 如上。$K$ 的元素 $a$ 是 $f$ 的重根，当且仅当它是根且 $f'(a)=0$。*

*证明。* 如上分解 $f$，得到

$$
f'(X)=(X-a)^mg'(X)+m(X-a)^{m-1}g(X).
$$

若 $m>1$，则显然 $f'(a)=0$。反过来，若 $m=1$，则

$$
f'(X)=(X-a)g'(X)+g(X),
$$

因此 $f'(a)=g(a)\ne0$。故若 $f'(a)=0$，必有 $m>1$，即得所需结论。

**命题 1.12。** *设 $f\in K[X]$。若 $K$ 的特征为 $0$，且 $f$ 的次数 $\geqq1$，则 $f'\ne0$。设 $K$ 的特征为 $p>0$，且 $f$ 的次数 $\geqq1$。则 $f'=0$ 当且仅当在表达式*

$$
f(X)=\sum_{\nu=0}^{n}a_\nu X^\nu
$$

*中，$p$ 整除每个满足 $a_\nu\ne0$ 的整数 $\nu$。*

*证明。* 若 $K$ 的特征为 $0$，则满足 $\nu\geqq1$、$a_\nu\ne0$ 的单项式 $a_\nu X^\nu$ 的导数非零，因为其导数为 $\nu a_\nu X^{\nu-1}$。若 $K$ 的特征为 $p>0$，则这种单项式的导数为 $0$ 当且仅当 $p\mid\nu$，正如所断言的。

设 $K$ 的特征为 $p>0$，$f$ 写成上述形式，且 $f'(X)=0$。则可以写成

$$
f(X)=\sum_{\mu=0}^{d}b_\mu X^{p\mu},
$$

其中 $b_\mu\in K$。

由于当 $1\leqq\nu\leqq p-1$ 时，二项式系数 $\binom p\nu$ 都能被 $p$ 整除，故若 $K$ 的特征为 $p$，则对 $a,b\in K$ 有

$$
(a+b)^p=a^p+b^p.
$$

又因为显然 $(ab)^p=a^pb^p$，映射

$$
x\mapsto x^p
$$

是 $K$ 到自身的同态，其核平凡，所以是单射。反复迭代可知，对每个整数 $r\geqq1$，映射 $x\mapsto x^{p^r}$<span class="original-page-anchor" id="pdf-page-195" aria-hidden="true"></span>是 $K$ 的自同态，称为**弗罗贝尼乌斯自同态**。归纳可知，若 $c_1,\ldots,c_n$ 为 $K$ 的元素，则

$$
(c_1+\cdots+c_n)^p=c_1^p+\cdots+c_n^p.
$$

将这些说明用于多项式，可见对任意元素 $a\in K$，都有

$$
(X-a)^{p^r}=X^{p^r}-a^{p^r}.
$$

若 $c\in K$，且多项式

$$
X^{p^r}-c
$$

在 $K$ 中有一个根 $a$，则 $a^{p^r}=c$，并且

$$
X^{p^r}-c=(X-a)^{p^r}.
$$

因此，该多项式恰有一个根，重数为 $p^r$。例如，$(X-1)^{p^r}=X^{p^r}-1$。

## §2. 唯一分解整环上的多项式

设 $A$ 为唯一分解整环，$K$ 为其分式域。设 $a\in K$、$a\ne0$。可以将 $a$ 写成 $A$ 中没有公共素因子的两个元素的商。若 $p$ 为 $A$ 的素元素，则可以写成

$$
a=p^rb,
$$

其中 $b\in K$、$r$ 为整数，且 $p$ 不整除 $b$ 的分子或分母。由 $A$ 中的唯一分解，立即可见 $r$ 由 $a$ 唯一确定；称 $r$ 为 **$a$ 在 $p$ 处的阶**（并写成 $r=\operatorname{ord}_p a$）。若 $a=0$，则定义其在 $p$ 处的阶为 $\infty$。

若 $a,a'\in K$ 且 $aa'\ne0$，则

$$
\operatorname{ord}_p(aa')=\operatorname{ord}_p a+\operatorname{ord}_p a'.
$$

这显然成立。

设 $f(X)\in K[X]$ 为一元多项式，写成

$$
f(X)=a_0+a_1X+\cdots+a_nX^n.
$$

若 $f=0$，则定义 $\operatorname{ord}_p f$ 为 $\infty$。若 $f\ne0$，则定义 $\operatorname{ord}_p f$ 为

<span class="original-page-anchor" id="pdf-page-196" aria-hidden="true"></span>

$$
\operatorname{ord}_p f=\min\operatorname{ord}_p a_i,
$$

其中最小值取遍所有满足 $a_i\ne0$ 的 $i$。

若 $r=\operatorname{ord}_p f$，则对 $A$ 中任意可逆元 $u$，称 $up^r$ 为 $f$ 的一个 **$p$ 容度**。定义 $f$ 的**容度（content）**为乘积

$$
\prod p^{\operatorname{ord}_p f},
$$

其中乘积取遍所有满足 $\operatorname{ord}_p f\ne0$ 的 $p$；也可以取该乘积乘以 $A$ 中任意可逆元所得的元素。因此，容度在相差一个 $A$ 中的可逆因子的意义下是良定义的。把 **content** 简写为 **cont**。

若 $b\in K$、$b\ne0$，则 $\operatorname{cont}(bf)=b\operatorname{cont}(f)$。这很清楚。因此可以写成

$$
f(X)=c\cdot f_1(X),
$$

其中 $c=\operatorname{cont}(f)$，而 $f_1(X)$ 的容度为 $1$。特别地，$f_1$ 的所有系数属于 $A$，且最大公因子为 $1$。容度为 $1$ 的多项式称为**本原多项式**。

**定理 2.1（高斯引理）。** *设 $A$ 为唯一分解整环，$K$ 为其分式域。设 $f,g\in K[X]$ 为一元多项式。则*

$$
\operatorname{cont}(fg)=\operatorname{cont}(f)\operatorname{cont}(g).
$$

*证明。* 写成 $f=cf_1$、$g=dg_1$，其中 $c=\operatorname{cont}(f)$、$d=\operatorname{cont}(g)$，可见只需证明：若 $f,g$ 的容度为 $1$，则 $fg$ 的容度也为 $1$。为此，只需证明对每个素元素 $p$ 都有 $\operatorname{ord}_p(fg)=0$。设

$$
\begin{aligned}
f(X)&=a_nX^n+\cdots+a_0,&a_n&\ne0,\\
g(X)&=b_mX^m+\cdots+b_0,&b_m&\ne0,
\end{aligned}
$$

为容度为 $1$ 的多项式。设 $p$ 为 $A$ 的素元素。只需证明 $p$ 不整除 $fg$ 的所有系数。令 $r$ 为满足 $0\leqq r\leqq n$、$a_r\ne0$ 且 $p$ 不整除 $a_r$ 的最大整数。同样，令 $b_s$ 为 $g$ 中最靠左、满足 $b_s\ne0$ 且 $p$ 不整除 $b_s$ 的系数。考虑 $f(X)g(X)$ 中 $X^{r+s}$ 的系数。该系数等于

$$
\begin{aligned}
c={}&a_rb_s+a_{r+1}b_{s-1}+\cdots\\
&+a_{r-1}b_{s+1}+\cdots,
\end{aligned}
$$

且 $p\nmid a_rb_s$。不过，$p$ 整除这个和中其他每个非零项，因为每一项都包含 $a_r$ 左侧的某个系数 $a_i$，或者 $b_s$ 左侧的某个系数 $b_j$。因此 $p$ 不整除 $c$，引理得证。

<span class="original-page-anchor" id="pdf-page-197" aria-hidden="true"></span>

现在对上述论证中的关键步骤给出另一个证明，即证明：

*若 $f,g\in A[X]$ 本原（即容度为 $1$），则 $fg$ 本原。*

*证明。* 需要证明，给定素元素 $p$ 不整除 $fg$ 的所有系数。考虑模 $p$ 约化，即典范同态 $A\to A/(p)=\bar A$。用上横线表示多项式的像，因此在约化同态下 $f\mapsto\bar f$、$g\mapsto\bar g$。于是

$$
\overline{fg}=\bar f\bar g.
$$

由假设，$\bar f\ne0$、$\bar g\ne0$。由于 $\bar A$ 是整环，得到 $\overline{fg}\ne0$，证毕。

**推论 2.2。** *设 $f(X)\in A[X]$ 在 $K[X]$ 中有分解 $f(X)=g(X)h(X)$。若 $c_g=\operatorname{cont}(g)$、$c_h=\operatorname{cont}(h)$，且 $g=c_gg_1$、$h=c_hh_1$，则*

$$
f(X)=c_gc_hg_1(X)h_1(X),
$$

*并且 $c_gc_h$ 是 $A$ 的元素。特别地，若 $f,g\in A[X]$ 的容度为 $1$，则也有 $h\in A[X]$。*

*证明。* 唯一需要证明的是 $c_gc_h\in A$。而

$$
\operatorname{cont}(f)=c_gc_h\operatorname{cont}(g_1h_1)=c_gc_h,
$$

由此即得断言。

**定理 2.3。** *设 $A$ 为唯一分解整环。则一元多项式环 $A[X]$ 是唯一分解整环。其素元素为 $A$ 的素元素，以及 $A[X]$ 中在 $K[X]$ 内不可约且容度为 $1$ 的多项式。*

*证明。* 设 $f\in A[X]$、$f\ne0$。利用 $K[X]$ 中的唯一分解及前面的推论，可找到分解

$$
f(X)=c\cdot p_1(X)\cdots p_r(X),
$$

其中 $c\in A$，且 $p_1,\ldots,p_r$ 为 $A[X]$ 中在 $K[X]$ 内不可约的多项式。提取它们的容度，不失一般性，可假设每个 $p_i$ 的容度为 $1$。由高斯引理，$c=\operatorname{cont}(f)$。这给出分解的存在性。由此可知，每个 $p_i(X)$ 在 $A[X]$ 中不可约。若还有另一个这样的分解，例如

$$
f(X)=d\cdot q_1(X)\cdots q_s(X),
$$

则由 $K[X]$ 中的唯一分解，可知 $r=s$，且对因子作一个置换后有

$$
p_i=a_iq_i,
$$

<span class="original-page-anchor" id="pdf-page-198" aria-hidden="true"></span>

其中 $a_i\in K$。由于假设 $p_i,q_i$ 的容度均为 $1$，可知 $a_i$ 实际属于 $A$，且是可逆元。定理得证。

**推论 2.4。** *设 $A$ 为唯一分解整环。则 $n$ 元多项式环 $A[X_1,\ldots,X_n]$ 是唯一分解整环。其可逆元恰为 $A$ 的可逆元，其素元素则为 $A$ 的素元素，或在 $K[X]$ 中不可约且容度为 $1$ 的多项式。*

*证明。* 归纳法。

由定理 2.3，在讨论唯一分解整环上容度为 $1$ 的多项式时，无须说明这样的多项式是在 $A$ 上不可约，还是在分式域 $K$ 上不可约。这两个概念等价。

**注 1。** 当 $n\geqq2$ 时，域 $K$ 上的多项式环 $K[X_1,\ldots,X_n]$ 不是主理想整环。例如，由 $X_1,\ldots,X_n$ 生成的理想不是主理想（证明很简单）。

**注 2。** 判定给定多项式（例如一元多项式）何时不可约，通常并不容易。例如，多项式 $X^4+4$ 在有理数域上*可约*，因为

$$
X^4+4=(X^2-2X+2)(X^2+2X+2).
$$

本书后面将给出多项式 $X^n-a$ 不可约的精确判别准则。下一节给出其他判别法。

## §3. 不可约性的判别法

第一个判别法如下：

**定理 3.1（艾森斯坦判别法）。** *设 $A$ 为唯一分解整环，$K$ 为其分式域。设 $f(X)=a_nX^n+\cdots+a_0$ 为 $A[X]$ 中次数为 $n\geqq1$ 的多项式。设 $p$ 为 $A$ 的素元素，并假设：*

$$
\begin{gathered}
a_n\not\equiv0\pmod p,\qquad a_i\equiv0\pmod p\quad\text{对所有 }i<n,\\
a_0\not\equiv0\pmod{p^2}.
\end{gathered}
$$

*则 $f(X)$ 在 $K[X]$ 中不可约。*

<span class="original-page-anchor" id="pdf-page-199" aria-hidden="true"></span>

*证明。* 提取 $f$ 的系数的最大公因子后，不失一般性，可假设 $f$ 的容度为 $1$。若在 $K[X]$ 中存在分解，其因子的次数均 $\geqq1$，则由高斯引理的推论，在 $A[X]$ 中存在分解，例如 $f(X)=g(X)h(X)$，其中

$$
\begin{aligned}
g(X)&=b_dX^d+\cdots+b_0,\\
h(X)&=c_mX^m+\cdots+c_0,
\end{aligned}
$$

满足 $d,m\geqq1$、$b_dc_m\ne0$。由于 $b_0c_0=a_0$ 能被 $p$ 整除，但不能被 $p^2$ 整除，$b_0,c_0$ 中有一个不能被 $p$ 整除，不妨设为 $b_0$。于是 $p\mid c_0$。因为 $c_mb_d=a_n$ 不能被 $p$ 整除，故 $p$ 不整除 $c_m$。令 $c_r$ 为 $h$ 中最靠右且满足 $c_r\not\equiv0\pmod p$ 的系数。于是

$$
a_r=b_0c_r+b_1c_{r-1}+\cdots.
$$

由于 $p\nmid b_0c_r$，而 $p$ 整除这个和中的其他每一项，可知 $p\nmid a_r$，产生矛盾，定理得证。

**例。** 设 $a$ 为非零无平方因子整数，且 $a\ne\pm1$。则对任意整数 $n\geqq1$，多项式 $X^n-a$ 在 $\mathbf{Q}$ 上不可约。多项式 $3X^5-15$ 和 $2X^{10}-21$ 在 $\mathbf{Q}$ 上不可约。

有时一个多项式不满足艾森斯坦判别法，但它的某个简单变换却满足。

**例。** 设 $p$ 为素数。则多项式

$$
f(X)=X^{p-1}+\cdots+1
$$

在 $\mathbf{Q}$ 上不可约。

*证明。* 只需证明多项式 $f(X+1)$ 在 $\mathbf{Q}$ 上不可约。注意，二项式系数

$$
\binom p\nu=\frac{p!}{\nu!(p-\nu)!},\quad1\leqq\nu\leqq p-1,
$$

都能被 $p$ 整除（因为分子能被 $p$ 整除，而分母不能，且该系数是整数）。有

$$
f(X+1)=\frac{(X+1)^p-1}{(X+1)-1}=\frac{X^p+pX^{p-1}+\cdots+pX}{X},
$$

由此可见 $f(X+1)$ 满足艾森斯坦判别法。

**例。** 设 $E$ 为域，$t$ 为某个包含 $E$ 的域的元素，并且 $t$ 在 $E$ 上超越。令 $K$ 为 $E[t]$ 的分式域。

<span class="original-page-anchor" id="pdf-page-200" aria-hidden="true"></span>

对任意整数 $n\geqq1$，多项式 $X^n-t$ 在 $K[X]$ 中不可约。这是因为环 $A=E[t]$ 是唯一分解整环，且 $t$ 为其中的素元素。

**定理 3.2（约化判别法）。** *设 $A,B$ 为整环，且*

$$
\varphi:A\to B
$$

*为同态。设 $K,L$ 分别为 $A,B$ 的分式域。设 $f\in A[X]$ 满足 $\varphi f\ne0$、$\deg\varphi f=\deg f$。若 $\varphi f$ 在 $L[X]$ 中不可约，则 $f$ 不存在分解 $f(X)=g(X)h(X)$，使得*

$$
g,h\in A[X]\quad\text{且}\quad\deg g,\deg h\geqq1.
$$

*证明。* 假设 $f$ 有这样的分解。则 $\varphi f=(\varphi g)(\varphi h)$。由于 $\deg\varphi g\leqq\deg g$、$\deg\varphi h\leqq\deg h$，由假设可知，这两个次数关系必须取等号。因此，由 $L[X]$ 中的不可约性，得到 $g$ 或 $h$ 为 $A$ 的元素，即得所需结论。

在前面的判别法中，假设 $A$ 为局部环，即具有唯一极大理想 $\mathfrak p$ 的环，并且 $\mathfrak p$ 为 $\varphi$ 的核。则由 $\varphi f$ 在 $L[X]$ 中不可约，可以得到 $f$ 在 $A[X]$ 中不可约。事实上，$A$ 中不属于 $\mathfrak p$ 的任意元素必为 $A$ 中的可逆元，所以证明中的最后结论可加强为：$g$ 或 $h$ 是 $A$ 中的可逆元。

当 $A$ 为唯一分解整环时，也可以应用该判别法，并由此得到 $f$ 在 $K[X]$ 中不可约。

**例。** 设 $p$ 为素数。以后将证明，$X^p-X-1$ 在域 $\mathbf{Z}/p\mathbf{Z}$ 上不可约。因此，$X^p-X-1$ 在 $\mathbf{Q}$ 上不可约。同样，

$$
X^5-5X^4-6X-1
$$

在 $\mathbf{Q}$ 上不可约。

还有一种学校里常见的初等方法，可判别多项式是否有根。

**命题 3.3（整根判别法）。** *设 $A$ 为唯一分解整环，$K$ 为其分式域。设*

$$
f(X)=a_nX^n+\cdots+a_0\in A[X].
$$

*设 $\alpha\in K$ 为 $f$ 的根，且 $\alpha=b/d$，其中 $b,d\in A$ 且二者互素。则 $b\mid a_0$、$d\mid a_n$。特别地，若首项系数 $a_n$ 为 $1$，则根 $\alpha$ 必属于 $A$，并整除 $a_0$。*

<span class="original-page-anchor" id="pdf-page-201" aria-hidden="true"></span>

证明留给读者，读者应该很早以前就熟悉这个证明了。作为不可约性判别法，它对次数为 $2$ 或 $3$ 的多项式尤其有用，此时可约性等价于在给定域中存在根。

## §4. 希尔伯特定理

本节证明希尔伯特关于多项式环的理想的一个基本定理。若交换环 $A$ 的每个理想都有限生成，则称 $A$ 为**诺特环**。

**定理 4.1。** *设 $A$ 为交换诺特环。则多项式环 $A[X]$ 也是诺特环。*

*证明。* 设 $\mathfrak A$ 为 $A[X]$ 的理想。令 $\mathfrak a_i$ 由 $0$ 以及所有这样的元素 $a\in A$ 组成：$a$ 是 $\mathfrak A$ 中某个多项式

$$
a_0+a_1X+\cdots+aX^i
$$

的首项系数。显然 $\mathfrak a_i$ 为理想。（若 $a,b\in\mathfrak a_i$，则将对应的多项式相加或相减，可见 $a\pm b\in\mathfrak a_i$。若 $x\in A$，则将对应的多项式乘以 $x$，可见 $xa\in\mathfrak a_i$。）此外有

$$
\mathfrak a_0\subset\mathfrak a_1\subset\mathfrak a_2\subset\cdots;
$$

换句话说，理想序列 $\{\mathfrak a_i\}$ 递增。事实上，将上述多项式乘以 $X$，便可看出 $a\in\mathfrak a_{i+1}$。

由第十章 §1 的判别准则 (2)，理想序列 $\{\mathfrak a_i\}$ 稳定下来，不妨设从 $\mathfrak a_r$ 开始稳定：

$$
\mathfrak a_0\subset\mathfrak a_1\subset\mathfrak a_2\subset\cdots\subset\mathfrak a_r=\mathfrak a_{r+1}=\cdots.
$$

设

$$
\begin{array}{lll}
a_{01},\ldots,a_{0n_0}&\text{为生成元，生成}&\mathfrak a_0,\\
\cdots\cdots\cdots&&\\
a_{r1},\ldots,a_{rn_r}&\text{为生成元，生成}&\mathfrak a_r.
\end{array}
$$

对每个 $i=0,\ldots,r$ 和 $j=1,\ldots,n_i$，令 $f_{ij}$ 为 $\mathfrak A$ 中次数为 $i$、首项系数为 $a_{ij}$ 的多项式。我们断言，多项式 $f_{ij}$ 构成 $\mathfrak A$ 的一个生成元集合。

设 $f$ 为 $\mathfrak A$ 中次数为 $d$ 的多项式。我们将对 $d$ 使用归纳法，证明 $f$ 属于由 $f_{ij}$ 生成的理想。设 $d\geqq0$。若 $d>r$，则<span class="original-page-anchor" id="pdf-page-202" aria-hidden="true"></span>注意到，

$$
X^{d-r}f_{r1},\ldots,X^{d-r}f_{rn_r}
$$

的首项系数生成 $\mathfrak a_d$。因此存在元素 $c_1,\ldots,c_{n_r}\in A$，使多项式

$$
f-c_1X^{d-r}f_{r1}-\cdots-c_{n_r}X^{d-r}f_{rn_r}
$$

的次数 $<d$，并且这个多项式也属于 $\mathfrak A$。若 $d\leqq r$，则可以减去一个线性组合，得到

$$
f-c_1f_{d1}-\cdots-c_{n_d}f_{dn_d},
$$

它是次数 $<d$、也属于 $\mathfrak A$ 的多项式。注意，从 $f$ 中减去的多项式属于由 $f_{ij}$ 生成的理想。由归纳假设，可以减去由 $f_{ij}$ 生成的理想中的一个多项式 $g$，使得 $f-g=0$，定理得证。

注意，若 $\varphi:A\to B$ 为交换环的满同态，且 $A$ 为诺特环，则 $B$ 也是诺特环。事实上，设 $\mathfrak b$ 为 $B$ 的理想，则 $\varphi^{-1}(\mathfrak b)$ 为 $A$ 的理想。因此，$\varphi^{-1}(\mathfrak b)$ 有有限个生成元 $(a_1,\ldots,a_n)$；由于 $\varphi$ 为满射，$\mathfrak b=\varphi(\varphi^{-1}(\mathfrak b))$ 由 $\varphi(a_1),\ldots,\varphi(a_n)$ 生成，即得结论。作为应用，得到：

**推论 4.2。** *设 $A$ 为诺特交换环，$B=A[x_1,\ldots,x_m]$ 为 $A$ 上有限生成的交换环。则 $B$ 为诺特环。*

*证明。* 将 $B$ 表示为多项式环的商环，使用定理 4.1 及前面的说明。

第九章将更深入地研究多项式环的理想。第十章将展开诺特环和诺特模的理论。

## §5. 部分分式

本节利用环的唯一分解性质，分析主理想整环的分式域。

**定理 5.1。** *设 $A$ 为主理想整环，$P$ 为其不可约元素的一个代表元集合。设 $K$ 为 $A$ 的分式域，$\alpha\in K$。对每个 $p\in P$，存在元素 $\alpha_p\in A$ 及整数 $j(p)\geqq0$，使几乎所有 $p\in P$ 均满足 $j(p)=0$，且 $\alpha_p$ 与 $p^{j(p)}$* <span class="original-page-anchor" id="pdf-page-203" aria-hidden="true"></span>*互素，并且*

$$
\alpha=\sum_{p\in P}\frac{\alpha_p}{p^{j(p)}}.
$$

*若另有这样的表达式*

$$
\alpha=\sum_{p\in P}\frac{\beta_p}{p^{i(p)}},
$$

*则对所有 $p$ 有 $j(p)=i(p)$，且对所有 $p$ 有 $\alpha_p\equiv\beta_p\bmod p^{j(p)}$。*

*证明。* 先在一种特殊情况下证明存在性。设 $a,b$ 为 $A$ 中互素的非零元素。则存在 $x,y\in A$，满足 $xa+yb=1$。因此

$$
\frac1{ab}=\frac xb+\frac ya.
$$

所以，对 $c\in A$，任意分式 $c/ab$ 均可分解为两个分式之和（即 $cx/b$ 和 $cy/a$），其分母分别整除 $b$ 和 $a$。由归纳法，现在可知任意 $\alpha\in K$ 均有定理中所述的表达式，惟一可能尚不满足的条件是 $p$ 可能整除 $\alpha_p$。约去最大公因子后，便得到满足全部所需条件的表达式。

至于唯一性，假设 $\alpha$ 有定理中所述的两个表达式。固定 $P$ 中的素元素 $q$。则

$$
\frac{\alpha_q}{q^{j(q)}}-\frac{\beta_q}{q^{i(q)}}=\sum_{p\ne q}\frac{\beta_p}{p^{i(p)}}-\frac{\alpha_p}{p^{j(p)}}.
$$

若 $j(q)=i(q)=0$，则关于 $q$ 的条件已满足。假设 $j(q)$ 或 $i(q)$ 中至少一个 $>0$，不妨设为 $j(q)$，并设 $j(q)\geqq i(q)$。令 $d$ 为所有满足 $p\ne q$ 的幂 $p^{j(p)}$ 与 $p^{i(p)}$ 的一个最小公倍数。将上式乘以 $dq^{j(q)}$，得到

$$
d(\alpha_q-q^{j(q)-i(q)}\beta_q)=q^{j(q)}\beta,
$$

其中 $\beta\in A$。此外，$q$ 不整除 $d$。若 $i(q)<j(q)$，则 $q$ 整除 $\alpha_q$，这是不可能的。因此 $i(q)=j(q)$。现在可见，$q^{j(q)}$ 整除 $\alpha_q-\beta_q$，定理得证。

将定理 5.1 应用于域 $k$ 上的多项式环 $k[X]$。令 $P$ 为不可约多项式的集合，并将它们规范化，使首项系数等于 $1$。于是 $P$ 为 $k[X]$ 中所有不可约元素的一个代表元集合。在定理 5.1 给出的 $\alpha$ 的表达式中，若 $\deg\alpha_p\geqq\deg p^{j(p)}$，现在可以用 $p^{j(p)}$ 除 $\alpha_p$，即使用欧几里得算法。把 $k[X]$ 的分式域记为 $k(X)$，称其元素为**有理函数**。

<span class="original-page-anchor" id="pdf-page-204" aria-hidden="true"></span>

**定理 5.2。** *设 $A=k[X]$ 为域 $k$ 上的一元多项式环。设 $P$ 为 $k[X]$ 中首项系数为 $1$ 的不可约多项式的集合。则 $k(X)$ 的任意元素 $f$ 有唯一的表达式*

$$
f(X)=\sum_{p\in P}\frac{f_p(X)}{p(X)^{j(p)}}+g(X),
$$

*其中 $f_p,g$ 为多项式；若 $j(p)=0$，则 $f_p=0$；若 $j(p)>0$，则 $f_p$ 与 $p$ 互素，并且 $\deg f_p<\deg p^{j(p)}$。*

*证明。* 存在性立即由前面的说明得到。至于唯一性，若有两个表达式，其对应元素分别为 $f_p$、$\varphi_p$，多项式部分分别为 $g,h$，则 $p^{j(p)}$ 整除 $f_p-\varphi_p$，故 $f_p-\varphi_p=0$，因此 $f_p=\varphi_p$、$g=h$。

还可以将 $f_p$ 按 $p$ 的幂展开，从而进一步分解项 $f_p/p^{j(p)}$。事实上，可以做得更一般。

**定理 5.3。** *设 $k$ 为域，$k[X]$ 为一元多项式环。设 $f,g\in k[X]$，且 $\deg g\geqq1$。则存在唯一的多项式*

$$
f_0,f_1,\ldots,f_d\in k[X],
$$

*使得 $\deg f_i<\deg g$，并且*

$$
f=f_0+f_1g+\cdots+f_dg^d.
$$

*证明。* 先证明存在性。若 $\deg g>\deg f$，则取 $f_0=f$，对 $i>0$ 取 $f_i=0$。假设 $\deg g\leqq\deg f$。可找到多项式 $q,r$，满足 $\deg r<\deg g$，且

$$
f=qg+r.
$$

由于 $\deg g\geqq1$，有 $\deg q<\deg f$。通过归纳，存在多项式 $h_0,h_1,\ldots,h_s$，使得

$$
q=h_0+h_1g+\cdots+h_sg^s,
$$

所以

$$
f=r+h_0g+\cdots+h_sg^{s+1},
$$

存在性得证。

至于唯一性，设

$$
f=f_0+f_1g+\cdots+f_dg^d=\varphi_0+\varphi_1g+\cdots+\varphi_mg^m
$$

为满足定理条件的两个表达式。在任一边添上<span class="original-page-anchor" id="pdf-page-205" aria-hidden="true"></span>等于 $0$ 的项，就可假设 $m=d$。相减得

$$
0=(f_0-\varphi_0)+\cdots+(f_d-\varphi_d)g^d.
$$

于是 $g$ 整除 $f_0-\varphi_0$；因为 $\deg(f_0-\varphi_0)<\deg g$，可知 $f_0=\varphi_0$。归纳地，取满足 $f_i\ne\varphi_i$ 的最小整数 $i$（若存在这样的 $i$）。将上式除以 $g^i$，得到 $g$ 整除 $f_i-\varphi_i$，所以这样的 $i$ 不可能存在。唯一性得证。

将定理 5.3 中用 $g$ 表示 $f$ 的表达式称为 $f$ 的 **$g$ 进展开**。若 $g(X)=X$，则 $g$ 进展开就是 $f$ 作为多项式的通常表达式。

**注。** 在某种意义上，定理 5.2 重做了第一章定理 8.1 对 $\mathbf{Q}/\mathbf{Z}$ 所做的事，即将 $K/A$ 的一个元素明确表示为其各个 $p$ 分量的直和。

## §6. 对称多项式

设 $A$ 为交换环，$t_1,\ldots,t_n$ 为 $A$ 上代数无关的元素。设 $X$ 为 $A[t_1,\ldots,t_n]$ 上的变量。构造多项式

$$
\begin{aligned}
F(X)&=(X-t_1)\cdots(X-t_n)\\
&=X^n-s_1X^{n-1}+\cdots+(-1)^ns_n,
\end{aligned}
$$

其中每个 $s_i=s_i(t_1,\ldots,t_n)$ 都是关于 $t_1,\ldots,t_n$ 的多项式。例如，

$$
s_1=t_1+\cdots+t_n\quad\text{且}\quad s_n=t_1\cdots t_n.
$$

多项式 $s_1,\ldots,s_n$ 称为 $t_1,\ldots,t_n$ 的**初等对称多项式**。

验证 $s_i$ **关于 $t_1,\ldots,t_n$ 是 $i$ 次齐次的**是一个简单练习，留给读者。

设 $\sigma$ 为整数 $(1,\ldots,n)$ 的一个置换。给定多项式 $f(t)\in A[t]=A[t_1,\ldots,t_n]$，定义 $\sigma f$ 为

$$
\sigma f(t_1,\ldots,t_n)=f(t_{\sigma(1)},\ldots,t_{\sigma(n)}).
$$

若 $\sigma,\tau$ 为两个置换，则 $\sigma\tau f=\sigma(\tau f)$，因此 $n$ 个字母上的对称群 $G$ 作用于多项式环 $A[t]$。若多项式对所有 $\sigma\in G$ 都满足 $\sigma f=f$，则称其为**对称多项式**。显然，对称多项式的集合是 $A[t]$ 的子环，包含常数多项式<span class="original-page-anchor" id="pdf-page-206" aria-hidden="true"></span>（即 $A$ 本身），也包含初等对称多项式 $s_1,\ldots,s_n$。下面将看到，$A[s_1,\ldots,s_n]$ 就是对称多项式环。

设 $X_1,\ldots,X_n$ 为变量。定义单项式

$$
X_1^{\nu_1}\cdots X_n^{\nu_n}
$$

的**权**为 $\nu_1+2\nu_2+\cdots+n\nu_n$。定义多项式 $g(X_1,\ldots,X_n)$ 的**权**为 $g$ 中出现的各单项式的权的最大值。

**定理 6.1。** *设 $f(t)\in A[t_1,\ldots,t_n]$ 为次数为 $d$ 的对称多项式。则存在权 $\leqq d$ 的多项式 $g(X_1,\ldots,X_n)$，使得*

$$
f(t)=g(s_1,\ldots,s_n).
$$

*若 $f$ 是 $d$ 次齐次多项式，则 $g$ 中出现的每个单项式的权均为 $d$。*

*证明。* 对 $n$ 使用归纳法。若 $n=1$，由于 $s_1=t_1$，定理显然成立。假设定理对 $n-1$ 元多项式已成立。

在 $F(X)$ 的表达式中代入 $t_n=0$，得到

$$
(X-t_1)\cdots(X-t_{n-1})X=X^n-(s_1)_0X^{n-1}+\cdots+(-1)^{n-1}(s_{n-1})_0X,
$$

其中 $(s_i)_0$ 为在 $s_i$ 中代入 $t_n=0$ 所得的表达式。可见，$(s_1)_0,\ldots,(s_{n-1})_0$ 正是 $t_1,\ldots,t_{n-1}$ 的初等对称多项式。

现在对 $d$ 使用归纳法。若 $d=0$，断言显然成立。假设 $d>0$，且断言对次数 $<d$ 的多项式已成立。设 $f(t_1,\ldots,t_n)$ 的次数为 $d$。存在权 $\leqq d$ 的多项式 $g_1(X_1,\ldots,X_{n-1})$，使得

$$
f(t_1,\ldots,t_{n-1},0)=g_1((s_1)_0,\ldots,(s_{n-1})_0).
$$

注意，$g_1(s_1,\ldots,s_{n-1})$ 关于 $t_1,\ldots,t_n$ 的次数 $\leqq d$。多项式

$$
f_1(t_1,\ldots,t_n)=f(t_1,\ldots,t_n)-g_1(s_1,\ldots,s_{n-1})
$$

的次数（关于 $t_1,\ldots,t_n$）$\leqq d$，并且是对称的。有

$$
f_1(t_1,\ldots,t_{n-1},0)=0.
$$

因此 $f_1$ 能被 $t_n$ 整除，即含有因子 $t_n$。由于 $f_1$ 对称，它含有因子 $t_1\cdots t_n$。所以

$$
f_1=s_nf_2(t_1,\ldots,t_n),
$$

其中 $f_2$ 为某个多项式，它必为对称的，其次数<span class="original-page-anchor" id="pdf-page-207" aria-hidden="true"></span>$\leqq d-n<d$。由归纳假设，存在 $n$ 元、权 $\leqq d-n$ 的多项式 $g_2$，使得

$$
f_2(t_1,\ldots,t_n)=g_2(s_1,\ldots,s_n).
$$

于是得到

$$
f(t)=g_1(s_1,\ldots,s_{n-1})+s_ng_2(s_1,\ldots,s_n),
$$

右侧每一项的权都 $\leqq d$。这就证明了定理，最后一个断言除外；该断言留给读者证明。

*现在证明，初等对称多项式 $s_1,\ldots,s_n$ 在 $A$ 上代数无关。*

若不然，取一个次数最小的非零多项式 $f(X_1,\ldots,X_n)\in A[X]$，使得

$$
f(s_1,\ldots,s_n)=0.
$$

将 $f$ 写成系数属于 $A[X_1,\ldots,X_{n-1}]$ 的关于 $X_n$ 的多项式：

$$
f(X_1,\ldots,X_n)=f_0(X_1,\ldots,X_{n-1})+\cdots+f_d(X_1,\ldots,X_{n-1})X_n^d.
$$

则 $f_0\ne0$。否则，可以写成

$$
f(X)=X_n\psi(X),
$$

其中 $\psi$ 为某个多项式，于是 $s_n\psi(s_1,\ldots,s_n)=0$。由此得到 $\psi(s_1,\ldots,s_n)=0$，而 $\psi$ 的次数小于 $f$ 的次数。

在上述关系中以 $s_i$ 替换 $X_i$，得到

$$
0=f_0(s_1,\ldots,s_{n-1})+\cdots+f_d(s_1,\ldots,s_{n-1})s_n^d.
$$

这是 $A[t_1,\ldots,t_n]$ 中的一个关系，在该关系中以 $0$ 替换 $t_n$。于是除第一项以外，各项都变为 $0$，得到

$$
0=f_0((s_1)_0,\ldots,(s_{n-1})_0),
$$

其中使用与定理 6.1 证明中相同的记号。这是 $t_1,\ldots,t_{n-1}$ 的初等对称多项式之间的非平凡关系，产生矛盾。

**例（判别式）。** 设 $f(X)=(X-t_1)\cdots(X-t_n)$。考虑乘积

$$
\delta(t)=\prod_{i<j}(t_i-t_j).
$$

对 $(1,\ldots,n)$ 的任意置换 $\sigma$，立即可见

$$
\delta^\sigma(t)=\pm\delta(t).
$$

<span class="original-page-anchor" id="pdf-page-208" aria-hidden="true"></span>

因此 $\delta(t)^2$ 为对称多项式，称其为**判别式**：

$$
D_f=D(s_1,\ldots,s_n)=\prod_{i<j}(t_i-t_j)^2.
$$

于是将判别式视为初等对称函数的多项式。一般理论的进一步内容参见 §8。现在考虑特殊情形。

**二次情形。** 请验证，对二次多项式 $f(X)=X^2+bX+c$，有

$$
D=b^2-4c.
$$

**三次情形。** 考虑 $f(X)=X^3+aX+b$。要证明

$$
D=-4a^3-27b^2.
$$

首先注意，$D$ 关于 $t_1,t_2$ 为 $6$ 次齐次多项式。此外，$a$ 为 $2$ 次齐次的，$b$ 为 $3$ 次齐次的。

由定理 6.1，可知存在权为 $6$ 的多项式 $g(X_2,X_3)$，使得 $D=g(a,b)$。权为 $6$ 的单项式 $X_2^mX_3^n$，即满足 $2m+3n=6$、$m,n\geqq0$ 为整数的单项式，只有 $m=3$、$n=0$，或 $m=0$、$n=2$ 这两种。因此

$$
g(X_2,X_3)=vX_2^3+wX_3^2,
$$

其中 $v,w$ 为现在需要确定的整数。

注意，整数 $v,w$ 具有普遍性，其含义是：对任意具体多项式，不论 $a,b$ 的具体取值为何，其判别式均由 $g(a,b)=va^3+wb^2$ 给出。

考虑多项式

$$
f_1(X)=X(X-1)(X+1)=X^3-X.
$$

此时 $a=-1$、$b=0$，且 $D=va^3=-v$。另一方面，由判别式为根的差的乘积的平方这一定义，有 $D=4$。因此得到 $v=-4$。再考虑多项式

$$
f_2(X)=X^3-1.
$$

此时 $a=0$、$b=-1$，且 $D=wb^2=w$。$f_2$ 的三个根是三次单位根，即

$$
1,\frac{-1+\sqrt{-3}}2,\frac{-1-\sqrt{-3}}2.
$$

使用判别式的定义，算得 $D=-27$。因此得到 $w=-27$。这就完成了不含 $X^2$ 项的三次多项式的判别式公式的证明。

<span class="original-page-anchor" id="pdf-page-209" aria-hidden="true"></span>

一般地，考虑三次多项式

$$
f(X)=X^3-s_1X^2+s_2X-s_3=(X-t_1)(X-t_2)(X-t_3).
$$

通过将它化为不含 $X^2$ 项的较简单情形，求出判别式的值。进行平移，令

$$
Y=X-\tfrac13s_1\quad\text{所以}\quad X=Y+\tfrac13s_1=Y+\tfrac13(t_1+t_2+t_3).
$$

于是 $f(X)$ 变为

$$
f(X)=f^*(Y)=Y^3+aY+b=(Y-u_1)(Y-u_2)(Y-u_3),
$$

其中 $a=u_1u_2+u_2u_3+u_1u_3$、$b=-u_1u_2u_3$，且 $u_1+u_2+u_3=0$。有

$$
u_i=t_i-\tfrac13s_1\quad\text{对 }i=1,2,3,
$$

并且对所有 $i\ne j$，都有 $u_i-u_j=t_i-t_j$，所以判别式不变，由此很容易得到一般情形下的公式。请做习题 12(b)。

## §7. 梅森–斯托瑟斯定理与 abc 猜想

20 世纪 80 年代初，一个全新关系的发现开启了关于多项式的新思路。设 $f(t)$ 为一元多项式，如愿意，可以取复数为系数域（特征为 $0$ 的代数闭域即可）。定义

$$
n_0(f)=f\text{ 的互异根的个数}.
$$

因此，$n_0(f)$ 将 $f$ 的每个零点都以重数 $1$ 计数；即使 $\deg f$ 很大，$n_0(f)$ 也可能很小。

**定理 7.1（梅森–斯托瑟斯，[Mas 84]，[Sto 81]）。** *设 $a(t),b(t),c(t)$ 为互素的多项式，满足 $a+b=c$。则*

$$
\max\deg\{a,b,c\}\leqq n_0(abc)-1.
$$

> **译校注：** 原文的定理假设只写“互素的多项式，满足 $a+b=c$”，遗漏了必要的非退化条件：$a,b,c$ 非零，且不全为常数。例如 $a=b=1,c=2$ 满足印出的条件，却使印出的结论成为 $0\leqq-1$。因此，应在上述假设中补上“非零且不全为常数”；下文的除法与对数导数证明也需要这些条件。英文转录保留原印文。

*证明。*（梅森）除以 $c$，并令 $f=a/c$、$g=b/c$，得到

$$
f+g=1,
$$

其中 $f,g$ 为有理函数。求导得到 $f'+g'=0$，将其重写为

$$
\frac{f'}f f+\frac{g'}g g=0,
$$

<span class="original-page-anchor" id="pdf-page-210" aria-hidden="true"></span>

因此

$$
\frac ba=\frac gf=-\frac{f'/f}{g'/g}.
$$

设

$$
a(t)=c_1\prod(t-\alpha_i)^{m_i},\quad b(t)=c_2\prod(t-\beta_j)^{n_j},\quad c(t)=c_3\prod(t-\gamma_k)^{r_k}.
$$

利用习题 11(c) 中将微积分代数化所得的结论，得到

$$
\frac ba=-\frac{f'/f}{g'/g}=-\frac{\displaystyle\sum\frac{m_i}{t-\alpha_i}-\sum\frac{r_k}{t-\gamma_k}}{\displaystyle\sum\frac{n_j}{t-\beta_j}-\sum\frac{r_k}{t-\gamma_k}}.
$$

$f'/f$ 和 $g'/g$ 的一个公分母由乘积

$$
N_0=\prod(t-\alpha_i)\prod(t-\beta_j)\prod(t-\gamma_k)
$$

给出，其次数为 $n_0(abc)$。注意，$N_0f'/f$ 和 $N_0g'/g$ 均为次数至多为 $n_0(abc)-1$ 的多项式。由关系

$$
\frac ba=-\frac{N_0f'/f}{N_0g'/g},
$$

以及假设 $a,b$ 互素这一事实，得到定理中的不等式。

作为应用，来证明多项式的**费马定理**。设 $x(t),y(t),z(t)$ 为互素的多项式，其中至少一个的次数 $\geqq1$，并满足

$$
x(t)^n+y(t)^n=z(t)^n.
$$

要证明 $n\leqq2$。由梅森–斯托瑟斯定理，得到

$$
n\deg x=\deg x(t)^n\leqq\deg x(t)+\deg y(t)+\deg z(t)-1,
$$

同样，在左侧用 $y$ 和 $z$ 替换 $x$ 也成立。相加得到

$$
n(\deg x+\deg y+\deg z)\leqq3(\deg x+\deg y+\deg z)-3.
$$

若 $n\geqq3$，就产生矛盾。

同一思路下的另一个应用是：

**达文波特定理。** *设 $f,g$ 为非常数多项式，且 $f^3-g^2\ne0$。则*

$$
\deg(f^3-g^2)\geqq\tfrac12\deg f-1.
$$

> **译校注。** 原书这里的下界印作 $\tfrac12\deg f-1$，正文照录。习题 13(a) 给出的锐利版本是 $\deg(f^3-g^2)\geqq\tfrac12\deg f+1$，等价于 $\deg f\leqq2\deg h-2$；印刷第 199 页的例子也在这个较强下界处取等号。因此这里的 $-1$ 给出的是较弱下界，后文所说的“最佳”应结合习题中的 $+1$ 版本理解。

参见习题 13。

<span class="original-page-anchor" id="pdf-page-211" aria-hidden="true"></span>

数学中最富成效的类比之一，是整数 $\mathbf{Z}$ 与域 $F$ 上多项式环 $F[t]$ 之间的类比。在梅森 [Ma 84]、弗雷 [Fr 87]、斯皮罗等人的见解基础上，马瑟和厄斯特莱提出了如下整数的 $abc$ 猜想。设 $m$ 为非零整数，定义 $m$ 的**根基**为

$$
N_0(m)=\prod_{p\mid m}p,
$$

即整除 $m$ 的所有素数的乘积，每个素数均取重数 $1$。

**$abc$ 猜想。** *给定 $\varepsilon>0$，存在正数 $C(\varepsilon)$，具有以下性质：对任意满足 $a+b=c$ 的非零互素整数 $a,b,c$，都有*

$$
\max(|a|,|b|,|c|)\leqq C(\varepsilon)N_0(abc)^{1+\varepsilon}.
$$

注意，这个不等式说明，$a,b,c$ 的许多素因子以一次幂出现；若“小”素数以高次幂出现，就必须有以一次幂出现的“大”素数来补偿。例如，可以考虑方程

$$
2^n\pm1=m.
$$

当 $m$ 很大时，$abc$ 猜想会说明，$m$ 必须能被以一次幂出现的大素数整除。[BLSTW 83] 的表中可以看到这种现象。

斯图尔特–泰德曼 [ST 86] 已证明，在猜想的表述中必须有 $\varepsilon$。随后，沃伊泰克·亚斯特热博夫斯基和丹·斯皮尔曼将下面的例子告诉了我。

需要给出这样的例子：对所有 $C>0$，都存在互素的自然数 $a,b,c$，满足 $a+b=c$ 且 $|a|>CN_0(abc)$。显然有

$$
2^n\mid(3^{2^n}-1).
$$

考虑由

$$
3^{2^n}-1=c_n
$$

给出的关系 $a_n+b_n=c_n$。

> **译校注：** 原文在要求 $a,b,c$ 为自然数之后，写出 $3^{2^n}-1=c_n$ 作为 $a_n+b_n=c_n$ 的例子；按左侧两项取 $a_n,b_n$ 会使 $b_n=-1$。若保持自然数条件，可将同一关系重排为 $(3^{2^n}-1)+1=3^{2^n}$，取 $a_n=3^{2^n}-1$、$b_n=1$、$c_n=3^{2^n}$。原印出的方程在正文和英文中均保留。

显然，这些关系给出了所需的例子。还可以类似地构造其他例子，因为 $3$ 和 $2$ 的作用可以由其他整数承担。将 $2$ 换成某个素数，将 $3$ 换成模 $p$ 与 $1$ 同余的整数。

$abc$ 猜想蕴含下面我们称为

**渐近费马定理**的结果。*对所有充分大的 $n$，方程*

$$
x^n+y^n=z^n
$$

*在非零互素整数中无解。*

<span class="original-page-anchor" id="pdf-page-212" aria-hidden="true"></span>

证明与多项式情形完全采用相同的模式，只是这里采用乘法形式来书写，而且还伴有一个 $1+\varepsilon$。如果能以一个显式常数 $C(\varepsilon)$（为使概念具体，也可以说 $C(1)$）证明 $abc$ 猜想，就能在上述应用中相应地显式确定 $n$ 的界。现在来看其他应用。

**Hall 猜想 [Ha 71]。** *若 $u,v$ 是互素的非零整数，满足 $u^3-v^2\neq0$，则*

$$
|u^3-v^2|\gg|u|^{1/2-\varepsilon}.
$$

符号 $\gg$ 表示左端大于或等于右端乘以一个仅依赖于 $\varepsilon$ 的常数。证明同样可直接由 $abc$ 猜想得到。事实上，$u,v$ 互素的假设并非必要；通过提取公因子，一般情形可以归结为互素情形，而 Hall 正是在这一更一般的形式下提出猜想的。不过，他还提出了指数中没有 epsilon 的形式，后来人们发现这个形式并不成立。与多项式情形一样，Hall 猜想描述 $|u^3-v^2|$ 可以有多小；答案是，它不能太小，正如右端所描述的那样。

Hall 猜想还可以理解为给下列方程的互素整数解提供一个界：

$$
v^2=u^3+b,\quad\text{其中 }b\text{ 为整数}.
$$

于是得到

$$
|u|\ll|b|^{2+\varepsilon}.
$$

更一般地，按照 Lang–Waldschmidt [La 78] 所猜测的不等式，固定非零整数 $A,B$，让 $u,v,k,m,n$ 变化，其中 $u,v$ 互素，且 $mv>m+n$。令

$$
Au^m+Bv^n=k.
$$

> **译校注。** 原书条件印为 $mv>m+n$；此处应为 $mn>m+n$，使下述指数的分母 $mn-(m+n)$ 为正。

由 $abc$ 猜想容易导出

$$
|u|\ll N_0(k)^{\frac{n}{mn-(m+n)}(1+\varepsilon)}\quad\text{且}\quad|v|\ll N_0(k)^{\frac{m}{mn-(m+n)}(1+\varepsilon)}.\tag{1}
$$

由此得到

$$
|k|\ll N_0(k)^{\frac{mn}{mn-(m+n)}(1+\varepsilon)}.
$$

把 $N_0(k)$ 换成 $|k|$ 后，Hall 猜想就是一个特例，因为 $N_0(k)\leq|k|$。

接下来取 $m=3$、$n=2$，但取 $A=4$、$B=-27$。此时写成

$$
D=4u^3-27v^2
$$

<span class="original-page-anchor" id="pdf-page-213" aria-hidden="true"></span>

于是得到

$$
|u|\ll N_0(D)^{2+\varepsilon}\quad\text{且}\quad|v|\ll N_0(D)^{3+\varepsilon}.\tag{2}
$$

这些不等式最初是要求对互素的 $u,v$ 成立的。现在允许 $u,v$ 有一个有界的公因子，比如 $d$。写成

$$
u=u'd\quad\text{且}\quad v=v'd,
$$

其中 $u',v'$ 互素。则

$$
D=4d^3u'^3-27d^2v'^2.
$$

此时可以在不等式 (1) 中取 $A=4d^3$、$B=-27d^2$，得到相同的不等式 (2)，但符号 $\ll$ 中隐含的常数还依赖于 $d$，或者依赖于这类公因子的某个固定上界。在这种情形下，我们把不等式 (2) 称为**广义 Szpiro 猜想**。

原来的 Szpiro 猜想是在一个更复杂的情形下提出的，相关介绍见 [La 90]；Szpiro 不等式的形式为

$$
|D|\ll N(D)^{6+\varepsilon},
$$

其中 $N(D)$ 是一个更精细的不变量，但对我们的目的来说，使用根基 $N_0(D)$ 就已足够，而且容易得多。

$D$ 的意义在于它作为判别式出现。我们讨论的这一思路始于 Frey [Fr 87]：他给 $a+b=c$ 的每一个解配上多项式

$$
x(x-a)(x+b),
$$

我们称它为 **Frey 多项式**。（事实上，出于更深刻的原因，Frey 配上的是由方程 $y^2=x(x-a)(x+b)$ 定义的曲线；但这里只需要右端的多项式。）多项式的判别式是各根之差的平方的乘积，因此

$$
D=(abc)^2.
$$

作平移

$$
\xi=x+\frac{b-a}{3},
$$

以消去 $x^2$ 项，于是多项式可以改写为

$$
\xi^3-\gamma_2\xi-\gamma_3,
$$

其中 $\gamma_2,\gamma_3$ 是关于 $a,b$ 的具有适当权的齐次式。判别式不变，因为关于 $\xi$ 的多项式的根是<span class="original-page-anchor" id="pdf-page-214" aria-hidden="true"></span>关于 $x$ 的多项式的根的平移。于是

$$
D=4\gamma_2^3-27\gamma_3^2.
$$

以 $(b-a)/3$ 作平移会引入一个小的分母。可以使用多项式 $x(x-3a)(x-3b)$ 来避免这个分母，这样 $\gamma_2,\gamma_3$ 就是整数，并且可以把广义 Szpiro 猜想应用于判别式，此时判别式多了一个因子，即 $D=3^6(abc)^2$。可以立即看出，广义 Szpiro 猜想蕴含渐近费马定理。反过来：

> **译校注。** 原书此处印为 $x(x-3a)(x-3b)$；按上一页的 Frey 多项式 $x(x-a)(x+b)$，应为 $x(x-3a)(x+3b)$。这样根之差给出的判别式才是下述 $3^6(abc)^2$。

*广义 Szpiro 猜想蕴含 $abc$ 猜想。*

事实上，对应 $(a,b)\leftrightarrow(\gamma_2,\gamma_3)$ 是可逆的，且具有“正确”的权。简单的代数运算表明，对 $\gamma_2,\gamma_3$ 的广义 Szpiro 估计蕴含所要的关于 $|a|,|b|$ 的估计。（做习题 14。）由 $abc$ 猜想和广义 Szpiro 猜想的等价性，可以用前面给出的例子说明，Szpiro 猜想中的 epsilon 是必要的。

最后注意，Mason–Stothers 定理的多项式情形与整数情形并非相互独立；更具体地说，Davenport 定理与 Hall 猜想是有关联的。把整数代入变量时，多项式情形中的例子就参数化了整数情形。这类例子见 [BCHS 65]，其中一个（由 Birch 给出）是

$$
f(t)=t^6+4t^4+10t^2+6\quad\text{且}\quad g(t)=t^9+6t^7+21t^5+35t^3+\frac{63}{2}t,
$$

因此

$$
\deg(f(t)^3-g(t)^2)=\frac12\deg f+1.
$$

这个例子表明，Davenport 不等式已是最佳的，因为次数达到该定理所允许的最低值。代入满足 $t\equiv2\bmod4$ 的大整数 $t$，便得到 $x^3-y^2$ 取类似低值的例子。关于这些问题的其他联系，参见 [La 90]。

### 参考文献

[BCHS 65] B. Birch、S. Chowla、M. Hall 和 A. Schinzel，“关于差 $x^3-y^2$”（On the difference $x^3-y^2$），*Norske Vid. Selsk. Forrh.* **38**（1965），第 65–69 页。

[BLSTW 83] J. Brillhart、D. H. Lehmer、J. L. Selfridge、B. Tuckerman 和 S. Wagstaff Jr.，“$b^n\pm1$ 的因式分解，其中 $b=2,3,5,6,7,10,11$，直到高次幂”（Factorization of $b^n\pm1$, $b=2,3,5,6,7,10,11$ up to high powers），*Contemporary Mathematics* 第 **22** 卷，AMS，Providence，RI，1983。

[Dav 65] H. Davenport，“关于 $f^3(t)-g^2(t)$”（On $f^3(t)-g^2(t)$），*Norske Vid. Selsk. Forrh.* **38**（1965），第 86–87 页。

[Fr 87] G. Frey，“$A-B=C$ 的解与椭圆曲线的联系”（Links between solutions of $A-B=C$ and elliptic curves），*Number Theory, Lecture Notes* **1380**，Springer-Verlag，New York，1989，第 31–62 页。

<span class="original-page-anchor" id="pdf-page-215" aria-hidden="true"></span>

[Ha 71] M. Hall，“丢番图方程 $x^3-y^2=k$”（The diophantine equation $x^3-y^2=k$），*Computers and Number Theory*，A. O. L. Atkin 和 B. Birch 编，Academic Press，London，1971，第 173–198 页。

[La 90] S. Lang，“新旧丢番图不等式猜想”（Old and new conjectured diophantine inequalities），*Bull. AMS* 第 **23** 卷，第 1 期（1990），第 37–75 页。

[Ma 84a] R. C. Mason，“函数域上的方程”（Equations over function fields），Springer Lecture Notes **1068**（1984），第 149–157 页；见 *Number Theory, Proceedings of the Noordwijkerhout*，1983。

[Ma 84b] R. C. Mason，《函数域上的丢番图方程》（Diophantine equations over function fields），*London Math. Soc. Lecture Note Series* 第 **96** 卷，Cambridge University Press，Cambridge，1984。

[Ma 84c] R. C. Mason，“函数域上的超椭圆方程”（The hyperelliptic equation over function fields），*Math. Proc. Cambridge Philos. Soc.* **93**（1983），第 219–230 页。

[Si 88] J. Silverman，“Wieferich 判据与 $abc$ 猜想”（Wieferich's criterion and the $abc$ conjecture），*Journal of Number Theory* **30**（1988），第 226–237 页。

[ST 86] C. L. Stewart 和 R. Tijdeman，“关于 Oesterle–Masser 猜想”（On the Oesterle–Masser Conjecture），*Mon. Math.* **102**（1986），第 251–257 页。

更多参考文献见本章末尾。

## §8. 结式

本节假定读者熟悉行列式。行列式理论将在后面讨论。本节可以看作给出对称函数的更多例子。

令 $A$ 为一个交换环，令 $v_0,\ldots,v_n,w_0,\ldots,w_m$ 在 $A$ 上代数独立。构造两个多项式：

$$
f_v(X)=v_0X^n+\cdots+v_n,
$$

$$
g_w(X)=w_0X^m+\cdots+w_m.
$$

把 $(v,w)$ 的**结式**，或 $f_v,g_w$ 的结式，定义为下列行列式：

![结式行列式：m 行逐次平移的 v 系数，n 行逐次平移的 w 系数，共 m+n 列。](/library/volume-86/diagrams/pdf-0215-resultant.png)

其中空白位置都应填入零。

<span class="original-page-anchor" id="pdf-page-216" aria-hidden="true"></span>

如果在 $f_v$ 和 $g_w$ 的系数中，分别用 $A$ 中的元素 $(a)=(a_0,\ldots,a_n)$ 和 $(b)=(b_0,\ldots,b_m)$ 代替 $(v)$ 和 $(w)$，便得到系数属于 $A$ 的多项式 $f_a$ 和 $g_b$；我们把**它们的结式**定义为在上述行列式中用 $(a)$ 代替 $(v)$、用 $(b)$ 代替 $(w)$ 所得到的行列式。$f_v,g_w$ 的结式记为

$$
\operatorname{Res}(f_v,g_w)\quad\text{或}\quad R(v,w).
$$

于是，结式 $\operatorname{Res}(f_a,g_b)$ 就是分别用 $(a),(b)$ 代替 $(v),(w)$ 得到的。

注意，$R(v,w)$ 是一个整系数多项式，即可以取 $A=\mathbf Z$。若 $z$ 是一个变量，则

$$
R(zv,w)=z^mR(v,w)\quad\text{且}\quad R(v,zw)=z^nR(v,w),
$$

这可以立即通过从行列式的前 $m$ 行（相应地，后 $n$ 行）中提出因子 $z$ 看出。因此，$R$ 关于第一组变量是 $m$ 次齐次的，关于第二组变量是 $n$ 次齐次的。此外，把 $R(v,w)$ 表示成单项式的和时，它包含系数为 $1$ 的单项式

$$
v_0^mw_m^n.
$$

若在结式中用 $0$ 代替 $v_0$ 和 $w_0$，就得到 $0$，因为行列式的第一列变为零。

现在在整数环 $\mathbf Z$ 上进行讨论。考虑线性方程

$$
\begin{aligned}
X^{m-1}f_v(X)&=v_0X^{n+m-1}+v_1X^{n+m-2}+\cdots+v_nX^{m-1}\\
X^{m-2}f_v(X)&=\phantom{v_0X^{n+m-1}+{}}v_0X^{n+m-2}+\cdots+v_nX^{m-2}\\
&\hspace{2em}\cdots\cdots\cdots\cdots\cdots\\
f_v(X)&=v_0X^n+\cdots+v_n\\
X^{n-1}g_w(X)&=w_0X^{n+m-1}+w_1X^{n+m-2}+\cdots+w_mX^{n-1}\\
X^{n-2}g_w(X)&=\phantom{w_0X^{n+m-1}+{}}w_0X^{n+m-2}+\cdots+w_mX^{n-2}\\
&\hspace{2em}\cdots\cdots\cdots\cdots\cdots\\
g_w(X)&=w_0X^m+\cdots+w_m.
\end{aligned}
$$

令 $C$ 为左端的列向量，令

$$
C_0,\ldots,C_{m+n}
$$

为系数的各列向量。上述方程可以写成

$$
C=X^{n+m-1}C_0+\cdots+1\cdot C_{m+n}.
$$

对最后一个等于 $1$ 的系数应用克拉默法则，得到

$$
R(v,w)=\det(C_0,\ldots,C_{m+n})=\det(C_0,\ldots,C_{m+n-1},C).
$$

> **译校注。** 结式矩阵有 $m+n$ 列，从 $C_0$ 起编号，最后一列应为 $C_{m+n-1}$。原书上述三处末尾列索引均多了 $1$；最后一式应为 $R(v,w)=\det(C_0,\ldots,C_{m+n-1})=\det(C_0,\ldots,C_{m+n-2},C)$。

<span class="original-page-anchor" id="pdf-page-217" aria-hidden="true"></span>

*由此可以看出，存在 $\mathbf Z[v,w][X]$ 中的多项式 $\varphi_{v,w}$ 和 $\psi_{v,w}$，使得*

$$
\varphi_{v,w}f_v+\psi_{v,w}g_w=R(v,w)=\operatorname{Res}(f_v,f_w).
$$

注意，$R(v,w)\in\mathbf Z[v,w]$，但左端的多项式涉及变量 $X$。

若 $\lambda:\mathbf Z[v,w]\to A$ 是到一个交换环 $A$ 的同态，令 $\lambda(v)=(a)$、$\lambda(w)=(b)$，则

$$
\varphi_{a,b}f_a+\psi_{a,b}g_b=R(a,b)=\operatorname{Res}(f_a,f_b).
$$

> **译校注。** 原书这两式分别印作 $\operatorname{Res}(f_v,f_w)$ 和 $\operatorname{Res}(f_a,f_b)$；按已定义的两个多项式，第二个参数应分别为 $g_w$ 和 $g_b$。

所以，由结式在 $\mathbf Z$ 上的泛关系，可以在任意交换环 $A$ 中，对每一对多项式得到一个类似关系。

**命题 8.1.** *设 $K$ 是域 $L$ 的一个子域，$f_a,g_b$ 是 $K[X]$ 中的多项式，在 $L$ 中有一个公共根 $\xi$。则 $R(a,b)=0$。*

*证明。* 若 $f_a(\xi)=g_b(\xi)=0$，就在已得到的 $R(a,b)$ 的表达式中用 $\xi$ 代替 $X$，得到 $R(a,b)=0$。

接下来研究结式与多项式 $f_v,g_w$ 的根之间的关系。需要一个引理。

**引理 8.2.** *令 $h(X_1,\ldots,X_n)$ 为整数环 $\mathbf Z$ 上的一个 $n$ 元多项式。若用 $X_1$ 代替 $X_2$，并保持其余 $X_i$（$i\neq2$）不变时，$h$ 的值为 $0$，则在 $\mathbf Z[X_1,\ldots,X_n]$ 中，$h(X_1,\ldots,X_n)$ 能被 $X_1-X_2$ 整除。*

*证明。* 留给读者作为练习。

令 $v_0,t_1,\ldots,t_n,w_0,u_1,\ldots,u_m$ 在 $\mathbf Z$ 上代数独立，并构造多项式

$$
f_v=v_0(X-t_1)\cdots(X-t_n)=v_0X^n+\cdots+v_n,
$$

$$
g_w=w_0(X-u_1)\cdots(X-u_m)=w_0X^m+\cdots+w_m.
$$

也就是令

$$
v_i=(-1)^iv_0s_i(t)\quad\text{且}\quad w_j=(-1)^jw_0s_j(u).
$$

以下容易验证的事实留给读者：

$$
v_0,v_1,\ldots,v_n,w_0,w_1,\ldots,w_m
$$

在 $\mathbf Z$ 上代数独立。

**命题 8.3.** *沿用上述记号，有*

$$
\operatorname{Res}(f_v,g_w)=v_0^mw_0^n\prod_{i=1}^n\prod_{j=1}^m(t_i-u_j).
$$

<span class="original-page-anchor" id="pdf-page-218" aria-hidden="true"></span>

*证明。* 令 $S$ 为命题中等式右端的表达式。

由于 $R(v,w)$ 关于第一组变量是 $m$ 次齐次的，关于第二组变量是 $n$ 次齐次的，可得

$$
R=v_0^mw_0^nh(t,u),
$$

其中 $h(t,u)\in\mathbf Z[t,u]$。由命题 8.1，若用 $t_i$ 代替 $u_j$（$i=1,\ldots,n$，$j=1,\ldots,m$），则结式为零；因此，由上述引理，把 $R$ 看成 $\mathbf Z[v_0,w_0,t,u]$ 的元素，对于每一对 $(i,j)$，$R$ 都能被 $t_i-u_j$ 整除。所以在 $\mathbf Z[v_0,w_0,t,u]$ 中，$S$ 整除 $R$，因为 $t_i-u_j$ 显然是该环中的素元，而且不同的 $(i,j)$ 给出不同的素元。

由 $S$ 的乘积表达式，即

$$
S=v_0^mw_0^n\prod_{i=1}^n\prod_{j=1}^m(t_i-u_j),\tag{1}
$$

得到

$$
\prod_{i=1}^ng(t_i)=w_0^n\prod_{i=1}^n\prod_{j=1}^m(t_i-u_j),
$$

因此

$$
S=v_0^m\prod_{i=1}^ng(t_i).\tag{2}
$$

类似地，

$$
S=(-1)^{nm}w_0^n\prod_{j=1}^mf(u_j).\tag{3}
$$

由 (2) 可知，$S$ 关于 $(w)$ 是 $n$ 次齐次的；由 (3) 可知，$S$ 关于 $(v)$ 是 $m$ 次齐次的。由于 $R$ 具有完全相同的齐次性质，且能被 $S$ 整除，可得 $R=cS$，其中 $c$ 为某个整数。由于 $R$ 和 $S$ 都包含系数为 $1$ 的单项式 $v_0^mw_m^n$，所以 $c=1$，命题得证。

还要注意，上面得到的 $S$ 的三个表达式现在给出了 $R$ 的因式分解。同时也得到命题 8.1 的逆命题。

**推论 8.4.** *令 $f_a,g_b$ 为系数属于域 $K$ 的多项式，满足 $a_0b_0\neq0$，且在 $K[X]$ 中都分解为一次因子的乘积。则 $\operatorname{Res}(f_a,g_b)=0$，当且仅当 $f_a$ 和 $g_b$ 有一个公共根。*

*证明。* 假设结式为 $0$。若 $f_a,g_b$ 的因式分解为

$$
f_a=a_0(X-\alpha_1)\cdots(X-\alpha_n),
$$

$$
g_b=b_0(X-\beta_1)\cdots(X-\beta_n),
$$

> **译校注。** 原书第二式末尾印作 $\beta_n$；$g_b$ 的次数为 $m$，该下标应为 $m$。

则有一个同态

<span class="original-page-anchor" id="pdf-page-219" aria-hidden="true"></span>

$$
\mathbf Z[v_0,t,w_0,u]\to K,
$$

使得对于所有 $i,j$，都有 $v_0\mapsto a_0$、$w_0\mapsto b_0$、$t_i\mapsto\alpha_i$、$u_j\mapsto\beta_j$。于是

$$
0=\operatorname{Res}(f_a,g_b)=a_0^mb_0^n\prod_i\prod_j(\alpha_i-\beta_j),
$$

所以 $f_a,f_b$ 有一个公共根。逆命题已经证明过了。

> **译校注。** 原书这里印作 $f_a,f_b$；按本段所讨论的两个多项式，应为 $f_a,g_b$。

在一个特殊情形下，再推导结式的一个关系。令 $f_v$ 如上，即

$$
f_v(X)=v_0X^n+\cdots+v_n=v_0(X-t_1)\cdots(X-t_n).
$$

由 (2) 可知，若 $f_v'$ 是 $f_v$ 的导数，则

$$
\operatorname{Res}(f_v,f_v')=v_0^{n-1}\prod_i f'(t_i).\tag{4}
$$

应用求导的乘积法则，得到：

$$
f_v'(X)=\sum_i v_0(X-t_1)\cdots\widehat{(X-t_i)}\cdots(X-t_n),
$$

$$
f_v'(t_i)=v_0(t_i-t_1)\cdots\widehat{(t_i-t_i)}\cdots(t_i-t_n),
$$

其中某一项上面的帽号表示该项应当省略。

把 $f_v$ 的**判别式**定义为

$$
D(f_v)=D(v)=(-1)^{n(n-1)/2}v_0^{2n-2}\prod_{i\neq j}(t_i-t_j).
$$

**命题 8.5.** *令 $f_v$ 如上，且其系数在 $\mathbf Z$ 上代数独立。则*

$$
\operatorname{Res}(f_v,f_v')=v_0^{2n-1}\prod_{i\neq j}(t_i-t_j)=(-1)^{n(n-1)/2}v_0D(f_v).\tag{5}
$$

*证明。* 把所得到的 $f_v'(t_i)$ 的表达式代入乘积 (4)，立即得到结果。

用 $1$ 代替 $v_0$ 时，可以看到，我们在上一节定义的判别式与现在的定义一致。特别地，得到判别式的一个显式公式。次数为 $2$ 和 $3$ 的多项式这两个特殊情形中的公式，将作为习题给出。

注意，判别式也可以写成乘积

$$
D(f_v)=v_0^{2n-2}\prod_{i<j}(t_i-t_j)^2.
$$

Serre 曾向我指出，本书第一版漏掉了符号 $(-1)^{n(n-1)/2}$；这一符号错误在文献中相当常见，van der Waerden、Samuel 和 Hilbert 的著作中都有（但 Hilbert 的全集中没有，Olga Taussky 已作订正）。另一方面，Weber 的 *Algebra* 第 I 卷，50，正确地给出了这个符号。

本节的后续内容见第 IX 章 §3 和 §4。

<span class="original-page-anchor" id="pdf-page-220" aria-hidden="true"></span>

## §9. 幂级数

令 $X$ 为一个字母，令 $G$ 为从集合 $\{X\}$ 到自然数的函数构成的幺半群。若 $\nu\in\mathbf N$，用 $X^\nu$ 表示在 $X$ 处取值为 $\nu$ 的函数。于是 $G$ 是一个乘法幺半群，我们在讨论多项式时已经遇到过。它的元素是 $X^0,X^1,X^2,\ldots,X^\nu,\ldots$。

令 $A$ 为一个交换环，令 $A[[X]]$ 为从 $G$ 到 $A$ 的函数组成的集合，不加任何限制。那么，$A[[X]]$ 的一个元素可以看作给每一个单项式 $X^\nu$ 指定一个系数 $a_\nu\in A$。把这个元素记为

$$
\sum_{\nu=0}^\infty a_\nu X^\nu.
$$

当然，这个求和符号并不是一个和，但我们也把上述表达式写成

$$
a_0X^0+a_1X^1+\cdots,
$$

称它为系数属于 $A$ 的一个一元**形式幂级数**。$a_0,a_1,\ldots$ 称为它的系数。

给定 $A[[X]]$ 的两个元素，比如

$$
\sum_{\nu=0}^\infty a_\nu X^\nu\quad\text{和}\quad\sum_{\mu=0}^\infty b_\mu X^\mu,
$$

把它们的乘积定义为

$$
\sum_{i=0}^\infty c_iX^i,
$$

其中

$$
c_i=\sum_{\nu+\mu=i}a_\nu b_\mu.
$$

与多项式一样，把它们的和定义为

$$
\sum_{\nu=0}^\infty(a_\nu+b_\nu)X^\nu.
$$

于是可知，幂级数构成一个环；证明与多项式的情形相同。

还可以构造多元幂级数环 $A[[X_1,\ldots,X_n]]$，其中每个元素都可以表示成

$$
\sum_{(\nu)}a_{(\nu)}X_1^{\nu_1}\cdots X_n^{\nu_n}=\sum a_{(\nu)}M_{(\nu)}(X_1,\ldots,X_n),
$$

系数 $a_{(\nu)}$ 不受限制，并与满足对所有 $i$ 都有 $\nu_i\geq0$ 的整数 $n$ 元组 $(\nu_1,\ldots,\nu_n)$ 一一对应。容易证明，$A[[X_1,\ldots,X_n]]$ 与迭代幂级数环 $A[[X_1]]\cdots[[X_n]]$ 之间存在一个同构。这留给读者作为练习。

<span class="original-page-anchor" id="pdf-page-221" aria-hidden="true"></span>

下一个定理将给出幂级数的欧几里得算法的类似物。不过，对于某些应用，采用比域更一般的系数是重要的，因此我们必须再引入一些术语。

令 $A$ 为一个环，$I$ 为一个理想。假定

$$
\bigcap_{\nu=1}^\infty I^\nu=\{0\}.
$$

可以把各个幂 $I^\nu$ 看作定义了 $A$ 中 $0$ 的邻域，并把分析中通常的柯西序列定义转用于这一情形，即：若给定任意一个幂 $I^\nu$，都存在整数 $N$，使得对所有 $m,n\geq N$ 都有

$$
a_m-a_n\in I^\nu,
$$

就称 $A$ 中的序列 $\{a_n\}$ 为**柯西序列**。

因此，$I^\nu$ 对应于分析中给定的 $\varepsilon$。随后便有序列收敛到 $A$ 的一个元素的通常概念。若每一个柯西序列都收敛，就称 $A$ **关于 $I$ 进拓扑完备**。

这种情形中或许最重要的例子是：$A$ 是一个局部环，$I=\mathfrak m$ 是其极大理想。所谓**完备局部环**，总是指关于 $\mathfrak m$ 进拓扑完备的局部环。

令 $k$ 为一个域。则 $n$ 元幂级数环

$$
R=k[[X_1,\ldots,X_n]]
$$

就是这样的完备局部环。事实上，令 $\mathfrak m$ 为由变量 $X_1,\ldots,X_n$ 生成的理想。那么 $R/\mathfrak m$ 自然同构于域 $k$ 本身，因此 $\mathfrak m$ 是一个极大理想。此外，任意形如

$$
f(X)=c_0-f_1(X)
$$

的幂级数，只要 $c_0\in k$、$c_0\neq0$ 且 $f_1(X)\in\mathfrak m$，就是可逆的。为证明这一点，首先可以不失一般性地假设 $c_0=1$。于是

$$
(1-f_1(X))^{-1}=1+f_1(X)+f_1(X)^2+f_1(X)^3+\cdots
$$

给出了逆元。因此可知，$\mathfrak m$ 是唯一的极大理想，$R$ 是局部环。可以立即验证，$R$ 按我们刚才定义的意义是完备的。同一论证表明，如果 $k$ 不是域，但 $c_0$ 在 $k$ 中可逆，那么 $f(X)$ 仍然可逆。

再令 $A$ 为一个环。可以把 $n$ 元幂级数环（$n>1$）看作以 $n-1$ 元幂级数环为系数环、关于一个变量 $X_n$ 的幂级数环，也就是说，有自然的等同

$$
A[[X_1,\ldots,X_n]]=A[[X_1,\ldots,X_{n-1}]][[X_n]].
$$

若 $A=k$ 是一个域，则环 $k[[X_1,\ldots,X_{n-1}]]$ 是一个完备局部环。更一般地，若 $\mathfrak o$ 是一个完备局部环，则幂级数环 $\mathfrak o[[X]]$ 是一个完备局部环，其极大理想是 $(\mathfrak m,X)$，其中 $\mathfrak m$ 是 $\mathfrak o$ 的极大理想。事实上，若幂级数 $\sum a_\nu X^\nu$ 有一个可逆的常数<span class="original-page-anchor" id="pdf-page-222" aria-hidden="true"></span>项 $a_0\in\mathfrak o^*$，则该幂级数是 $\mathfrak o[[X]]$ 中的可逆元，因为首先可以不失一般性地假设 $a_0=1$，然后对于 $h\in(\mathfrak m,X)$，可以用几何级数 $1-h+h^2-h^3+\cdots$ 求出 $1+h$ 的逆元。

在许多问题中，把域上的多元幂级数的某些问题归结为上述更复杂环上的一元幂级数问题是有用的。现在把这种分解应用于幂级数的欧几里得算法。

**定理 9.1.** *设 $\mathfrak o$ 是一个完备局部环，极大理想为 $\mathfrak m$。令*

$$
f(X)=\sum_{i=0}^\infty a_iX^i
$$

*为 $\mathfrak o[[X]]$ 中的一个（一元）幂级数，满足并非所有 $a_i$ 都属于 $\mathfrak m$。设 $a_0,\ldots,a_{n-1}\in\mathfrak m$，且 $a_n\in\mathfrak o^*$ 为可逆元。给定 $g\in\mathfrak o[[X]]$，方程*

$$
g=qf+r
$$

*有唯一的解，其中 $q\in\mathfrak o[[X]]$，$r\in\mathfrak o[X]$，且 $\deg r\leq n-1$。*

*证明*（Manin）。令 $\alpha$ 和 $\tau$ 分别为截取级数的开头部分和尾部的投影，定义为

$$
\alpha:\sum b_iX^i\mapsto\sum_{i=0}^{n-1}b_iX^i=b_0+b_1X+\cdots+b_{n-1}X^{n-1},
$$

$$
\tau:\sum b_iX^i\mapsto\sum_{i=n}^\infty b_iX^{i-n}=b_n+b_{n+1}X+b_{n+2}X^2+\cdots.
$$

注意，对任何 $h\in\mathfrak o[[X]]$ 都有 $\tau(hX^n)=h$；而 $h$ 是次数 $<n$ 的多项式，当且仅当 $\tau(h)=0$。

$q,r$ 的存在性等价于存在 $q$ 满足

$$
\tau(g)=\tau(qf).
$$

因此，问题等价于求解

$$
\tau(g)=\tau(q\alpha(f))+\tau(q\tau(f)X^n)=\tau(q\alpha(f))+q\tau(f).
$$

注意，$\tau(f)$ 可逆。令 $Z=q\tau(f)$，则上述方程等价于

$$
\tau(g)=\tau\left(Z\frac{\alpha(f)}{\tau(f)}\right)+Z=\left(I+\tau\circ\frac{\alpha(f)}{\tau(f)}\right)Z.
$$

注意，

$$
\tau\circ\frac{\alpha(f)}{\tau(f)}:\mathfrak o[[X]]\to\mathfrak m\mathfrak o[[X]],
$$

因为 $\alpha(f)/\tau(f)\in\mathfrak m\mathfrak o[[X]]$。所以可以取逆来求得 $Z$，即

<span class="original-page-anchor" id="pdf-page-223" aria-hidden="true"></span>

$$
Z=\left(I+\tau\circ\frac{\alpha(f)}{\tau(f)}\right)^{-1}\tau(g),
$$

这同时证明了存在性与唯一性，证明完毕。

**定理 9.2（魏尔斯特拉斯预备定理）。** *前一定理中的幂级数 $f$ 可以唯一地写成*

$$
f(X)=(X^n+b_{n-1}X^{n-1}+\cdots+b_0)u,
$$

*其中 $b_i\in\mathfrak m$，$u$ 为 $\mathfrak o[[X]]$ 中的可逆元。*

*证明。* 由欧几里得算法，可以唯一地写成

$$
X^n=qf+r.
$$

于是 $q$ 可逆，因为

$$
q=c_0+c_1X+\cdots,
$$

$$
f=\cdots+a_nX^n+\cdots,
$$

所以

$$
1\equiv c_0a_n\pmod{\mathfrak m},
$$

因而 $c_0$ 是 $\mathfrak o$ 中的可逆元。得到 $qf=X^n-r$，以及

$$
f=q^{-1}(X^n-r),
$$

其中 $r\equiv0\pmod{\mathfrak m}$。这证明了存在性。唯一性是直接的。

定理 9.1 和 9.2 中的整数 $n$ 称为 $f$ 的**魏尔斯特拉斯次数**，记为 $\deg_Wf$。我们看到，只要幂级数的系数并非全部属于 $\mathfrak m$，它就可以表示成一个具有该魏尔斯特拉斯次数的多项式与幂级数环中的一个可逆元的乘积。此外，该多项式除首项系数外的所有系数都属于极大理想。这样的多项式称为**优异多项式**（distinguished polynomial），或**魏尔斯特拉斯多项式**。

**注。** 我很喜欢在魏尔斯特拉斯预备定理的证明中使用欧几里得算法。不过，也可以给出一个直接证明，明确写出用来求解 $u$ 的系数的递推关系，如下。写 $u=\sum c_iX^i$，则需要求解方程组

$$
\begin{aligned}
b_0c_0&=a_0,\\
b_0c_1+b_1c_0&=a_1,\\
&\cdots\\
b_0c_{n-1}+\cdots+b_{n-1}c_0&=a_{n-1},\\
b_0c_n+\cdots+c_0&=a_n,\\
b_0c_{n+1}+\cdots+c_1&=a_{n+1},\\
&\cdots
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-224" aria-hidden="true"></span>

事实上，选定 $c_0$ 为可逆元，比如 $c_0=1$ 后，对每个正整数 $r$，这个方程组模 $\mathfrak m^r$ 都有唯一的解。因为，由前 $n$ 个方程（从 $0$ 到 $n-1$）可知，$b_0,\ldots,b_{n-1}$ 唯一地确定为模 $\mathfrak m$ 等于 $0$。随后，$c_n,c_{n+1},\ldots$ 由后面的方程模 $\mathfrak m$ 唯一确定。现在作归纳，假设已经证明系数 $b_i,c_j$ 模 $\mathfrak m^r$ 唯一确定。那么，由条件 $a_0,\ldots,a_{n-1}\equiv0\bmod\mathfrak m$，立即可知前 $n$ 个方程模 $\mathfrak m^{r+1}$ 唯一确定 $b_i$，因为所有 $b_i\equiv0\bmod\mathfrak m$。随后，后面的方程根据 $b_i$ 模 $\mathfrak m^{r+1}$ 的值和 $c_j$ 模 $\mathfrak m^r$ 的值，模 $\mathfrak m^{r+1}$ 唯一确定 $c_j$。每个 $r$ 所对应的模 $\mathfrak m^r$ 的唯一一组解，就在射影极限中定义一个解，而这个射影极限正是该完备局部环。

> **译校注。** 本段原文保留，但这里不能任意指定 $c_0=1$：例如在域 $\mathbf Q$ 上取 $f=2X$，首一的魏尔斯特拉斯多项式只能是 $X$，相应的 $u=2$，所以 $c_0=2$。模 $\mathfrak m$ 时，前 $n$ 个方程给出 $b_0,\ldots,b_{n-1}=0$，其后的方程从 $c_0=a_n$ 开始依次确定 $c_0,c_1,\ldots$，而不是原文所写的从 $c_n,c_{n+1},\ldots$ 开始。上述两处是这段直接递推说明的问题，不影响前面用除法定理完成的预备定理证明。

现在具备了处理一个重要情形中的唯一分解所需的全部工具。

**定理 9.3.** *令 $k$ 为一个域。则 $k[[X_1,\ldots,X_n]]$ 是唯一分解整环。*

*证明。* 令 $f(x)=f(X_1,\ldots,X_n)\in k[[X]]$，且 $f\neq0$。作一个足够一般的线性变量替换（当 $k$ 无限时）

$$
x_i=\sum c_{ij}Y_j,\quad\text{其中 }c_{ij}\in k,
$$

就可以不失一般性地假设 $f(0,\ldots,0,x_n)\neq0$。（当 $k$ 有限时，必须作非线性替换，参见第 VIII 章定理 2.1。）事实上，若写成 $f(X)=f_d(X)+\text{高次项}$，其中 $f_d(X)$ 是次数 $d\geq0$ 的齐次多项式，则上述变量替换保持 $f$ 的每个齐次分量的次数；由于假设 $k$ 无限，可以选取系数 $c_{ij}$，使每个幂 $Y_i^d$（$i=1,\ldots,n$）事实上都具有非零系数。

现在对 $n$ 作归纳。令 $R_n=k[[X_1,\ldots,X_n]]$ 为 $n$ 元幂级数环，并由归纳假设 $R_{n-1}$ 为唯一分解整环。由定理 9.2，写成 $f=gu$，其中 $u$ 为可逆元，$g$ 为 $R_{n-1}[X_n]$ 中的魏尔斯特拉斯多项式。由定理 2.3，$R_{n-1}[X_n]$ 是唯一分解整环，所以可以把 $g$ 写成不可约元素 $g_1,\ldots,g_r\in R_{n-1}[X_n]$ 的乘积，即 $f=g_1\cdots g_ru$，其中各因子 $g_i$ 在相差一个可逆元的意义下唯一确定。这证明了分解的存在性。关于唯一性，假设 $f$ 被表示为 $R_n$ 中不可约元素的乘积 $f=f_1\cdots f_s$。则对每个 $q=1,\ldots,s$，都有 $f_q(0,\ldots,0,x_n)\neq0$，因而可以写成 $f_q=h_qu_q'$，其中 $u_q'$ 为可逆元，$h_q$ 为魏尔斯特拉斯多项式，且在 $R_{n-1}[X_n]$ 中必定不可约。于是 $f=gu=\prod h_q\prod u_q'$，其中 $g$ 以及所有 $h_q$ 都是魏尔斯特拉斯多项式。由定理 9.2，必有 $g=\prod h_q$；又由于 $R_{n-1}[X_n]$ 是唯一分解整环，可知在相差可逆元的意义下，多项式 $h_q$ 与多项式 $g_i$ 相同。这证明了唯一性。

**注。** Dan Anderson 向我指出，我在以前的一次印刷中错误地断言：若 $\mathfrak O$ 是一个具有唯一分解的完备局部环，则 $\mathfrak O[[X]]$ 也具有唯一分解。这个断言是错误的，反例为

$$
k(t)[[X_1,X_2,X_3]]/(X_1^2+X_2^2+X_3^2),
$$

<span class="original-page-anchor" id="pdf-page-225" aria-hidden="true"></span>

由 P. Salmon 给出，见 *Su un problema posto da P. Samuel*，Atti Acad. Naz. Lincei Rend. Cl. Sc. Fis. Matem. **40(8)**（1966），第 801–803 页。如果 $\mathfrak O$ 除完备外**还是**一个正则局部环，那么 $\mathfrak O[[X]]$ 确实具有唯一分解，不过这是一个更深的定理。我给出的域上幂级数的简单证明是经典的，这里采用了 [GrH 78] 中的叙述。

**定理 9.4.** *若 $A$ 是诺特环，则 $A[[X]]$ 也是诺特环。*

*证明。* 我们的论证是对多项式的希尔伯特定理证明中所用论证的一个修改。我们考虑最低次的元素，而不是最高次的元素。

令 $\mathfrak A$ 为 $A[[X]]$ 的一个理想。令 $\mathfrak a_i$ 为那些元素 $a\in A$ 组成的集合，使 $a$ 是属于 $\mathfrak A$ 的某个幂级数

$$
aX^i+\text{更高次项}
$$

中的 $X^i$ 的系数。那么 $\mathfrak a_i$ 是 $A$ 的一个理想，且 $\mathfrak a_i\subset\mathfrak a_{i+1}$（这个断言的证明与多项式情形相同）。理想的升链终止：

$$
\mathfrak a_0\subset\mathfrak a_1\subset\mathfrak a_2\subset\cdots\subset\mathfrak a_r=\mathfrak a_{r+1}=\cdots.
$$

与前面一样，令 $a_{ij}$（$i=0,\ldots,r$，$j=1,\ldots,n_i$）为理想 $\mathfrak a_i$ 的生成元，令 $f_{ij}$ 为系数属于 $A$、起始系数为 $a_{ij}$ 的幂级数。给定 $f\in\mathfrak A$，其起始项次数为 $d$，不妨设 $d\leq r$，可以找到元素 $c_1,\ldots,c_{n_d}\in A$，使

$$
f-c_1f_{d1}-\cdots-c_{n_d}f_{dn_d}
$$

的起始项次数 $\geq d+1$。归纳进行下去，可以假设 $d>r$。然后使用线性组合

$$
f-c_1^{(d)}X^{d-r}f_{r1}-\cdots-c_{n_r}^{(d)}X^{d-r}f_{rn_r},
$$

得到一个起始项次数 $\geq d+1$ 的幂级数。这样，如果从次数 $d>r$ 的一个幂级数开始，就可以把它表示成 $f_{r1},\ldots,f_{rn_r}$ 的线性组合，所用的系数为

$$
g_1(X)=\sum_{\nu=d}^\infty c_1^{(\nu)}X^{\nu-r},\ldots,g_{n_r}(X)=\sum_{\nu=d}^\infty c_{n_r}^{(\nu)}X^{\nu-r}.
$$

于是可知，各个 $f_{ij}$ 生成理想 $\mathfrak A$，证明完毕。

**推论 9.5.** *若 $A$ 是一个诺特交换环，或者是一个域，则 $A[[X_1,\ldots,X_n]]$ 是诺特环。*

**例。** 一元幂级数是单复变函数理论的核心；类似地，多元幂级数也是高维情形中的核心。例如参见 [Gu 90]。

魏尔斯特拉斯多项式出现在许多背景中。首先，在研究解析集时，它们可以用来把幂级数问题归结为多项式问题。例如参见 [GrH 78] 第 0 章。在数论<span class="original-page-anchor" id="pdf-page-226" aria-hidden="true"></span>的背景中，这样的多项式作为特征多项式出现在分圆域的岩泽理论中。参见 [La 90]，从第 5 章开始。

幂级数也可以用作生成函数。假设给每个正整数 $n$ 配上一个数 $a(n)$。则**生成函数**就是幂级数 $\sum a(n)t^n$。在一些重要的情形中，这个函数实际上表示一个有理函数；证明这一点可能是一个重要的结果。

例如，在第 X 章 §6 中，我们将考虑与模的长度相联系的一个庞加莱级数。类似地，在拓扑学中，考虑一个拓扑空间 $X$，使得它的同调群（比如说）在系数域 $k$ 上是有限维的。令 $h_n=\dim H_n(X,k)$，其中 $H_n$ 为第 $n$ 个同调群。把**庞加莱级数**定义为生成级数

$$
P_X(t)=\sum h_nt^n.
$$

动力系统理论中也有例子。考虑从空间 $X$ 到自身的映射 $T:X\to X$，令 $N_n$ 为第 $n$ 次迭代 $T^n=T\circ T\circ\cdots\circ T$（$n$ 次）的不动点个数。生成函数为 $\sum N_nt^n$。由于这里引用了较多文献，我在本节末尾把它们系统地列出。首先参见 Artin–Mazur [ArM 65]；Manning 对 Smale 的一个猜想的证明 [Ma 71]；以及 Shub 的书 [Sh 87]，特别是第 10 章推论 10.42（Manning 定理）。

作为代数几何中的一个例子，令 $V$ 为在有限域 $k$ 上定义的一个代数簇。令 $K_n$ 为 $k$ 的 $n$ 次扩张（在一个给定的代数闭包内）。令 $N_n$ 为 $V$ 在 $K_n$ 中的点数。把 **zeta 函数** $Z(t)$ 定义为满足 $Z(0)=1$ 以及下式的幂级数：

$$
Z'/Z(t)=\sum_{n=1}^\infty N_nt^{n-1}.
$$

此时 $Z(t)$ 是一个有理函数（当 $V$ 的维数为 $1$ 时由 F. K. Schmidt 证明，高维情形由 Dwork 证明）。相关讨论和参考文献见 Hartshorne [Ha 77] 的附录 C。

最后提到**分拆函数** $p(n)$，它是把一个正整数表示成正整数之和的方式数。Euler 确定了它的生成函数为

$$
1+\sum_{n=1}^\infty p(n)t^n=\prod_{n=1}^\infty(1-t^n)^{-1}.
$$

例如参见 Hardy 和 Wright [HardW 71] 第 XIX 章。分拆函数的生成级数与一个通常用变量 $q$ 表示的幂级数有关，即

<span class="original-page-anchor" id="pdf-page-227" aria-hidden="true"></span>

$$
\Delta=q\prod_{n=1}^\infty(1-q^n)^{24}=\sum_{n=1}^\infty\tau(n)q^n,
$$

它是 **Ramanujan 函数** $\tau(n)$ 的生成级数。$\Delta$ 的幂级数也是模函数理论中一个函数的展开。入门介绍见 Serre 的书 [Se 73] 最后一章，以及椭圆函数方面的书，例如我的著作。我们将在伽罗瓦理论那一章提到 $\Delta$ 的幂级数的一个应用。

生成幂级数也出现在拓扑和代数几何的 $K$ 理论中，例如 Hirzebruch 关于黎曼–罗赫定理及其由 Grothendieck 给出的推广的形式体系。参见 Atiyah [At 67]、Hirzebruch [Hi 66] 以及 [FuL 86]。我在习题 21–27 中提取了一些直接涉及幂级数的形式上的初等内容，可以把它们看作基本例子。也可参看下一章的习题 31–34。

### 参考文献

[ArM 65] M. Artin 和 B. Mazur，“关于周期点”（On periodic points），*Ann. Math.*（2）**81**（1965），第 89–99 页。

[At 67] M. Atiyah，《K 理论》（*K-Theory*），Addison-Wesley，1991（重印自 Benjamin Lecture Notes，1967）。

[FuL 85] W. Fulton 和 S. Lang，《黎曼–罗赫代数》（*Riemann–Roch Algebra*），Springer-Verlag，New York，1985。

[GrH 78] P. Griffiths 和 J. Harris，《代数几何原理》（*Principles of Algebraic Geometry*），Wiley-Interscience，New York，1978。

[Gu 90] R. Gunning，《多复变全纯函数导论》（*Introduction to Holomorphic Functions of Several Variables*），第 II 卷：《局部理论》（*Local Theory*），Wadsworth and Brooks/Cole，1990。

[HardW 71] G. H. Hardy 和 E. M. Wright，《数论导引》（*An Introduction to the Theory of Numbers*），Oxford University Press，Oxford，UK，1938–1971（多个版本）。

[Hart 77] R. Hartshorne，《代数几何》（*Algebraic Geometry*），Springer-Verlag，New York，1977。

[Hi 66] F. Hirzebruch，《代数几何中的拓扑方法》（*Topological Methods in Algebraic Geometry*），Springer-Verlag，New York，1966（由 1956 年德文原版翻译并扩充）。

[La 90] S. Lang，《分圆域》（*Cyclotomic Fields*），I 和 II，Springer-Verlag，New York，1990，由原版（1978、1980）合编。

[Ma 71] A. Manning，“公理 A 微分同胚具有有理 zeta 函数”（Axiom A diffeomorphisms have rational zeta functions），*Bull. Lond. Math. Soc.* **3**（1971），第 215–220 页。

[Se 73] J. P. Serre，《算术教程》（*A Course in Arithmetic*），Springer-Verlag，New York，1973。

[Sh 87] M. Shub，《动力系统的全局稳定性》（*Global Stability of Dynamical Systems*），Springer-Verlag，New York，1987。

<span class="original-page-anchor" id="pdf-page-228" aria-hidden="true"></span>

## 习题

**1.** 令 $k$ 为一个域，$f(X)\in k[X]$ 为一个非零多项式。证明以下条件等价：

(a) 理想 $(f(X))$ 是素理想。

(b) 理想 $(f(X))$ 是极大理想。

(c) $f(X)$ 不可约。

**2.** (a) 叙述并证明定理 5.2 对于有理数的类似结论。

(b) 叙述并证明定理 5.3 对于正整数的类似结论。

**3.** 令 $f$ 为域 $k$ 上的一个一元多项式，$X,Y$ 为两个变量。证明在 $k[X,Y]$ 中有“泰勒级数”展开

$$
f(X+Y)=f(X)+\sum_{i=1}^n\varphi_i(X)Y^i,
$$

其中 $\varphi_i(X)$ 是系数属于 $k$ 的关于 $X$ 的多项式。若 $k$ 的特征为 $0$，证明

$$
\varphi_i(X)=\frac{D^if(X)}{i!}.
$$

**4.** 把前一习题推广到多元多项式（引入偏导数，并证明多元多项式有有限的泰勒展开）。

**5.** (a) 证明多项式 $X^4+1$ 和 $X^6+X^3+1$ 在有理数域上不可约。

(b) 证明域上的一个三次多项式或者不可约，或者在该域中有一个根。$X^3-5X^2+1$ 在有理数域上是否不可约？

(c) 证明二元多项式 $X^2+Y^2-1$ 在有理数域上不可约。它在复数域上是否不可约？

**6.** 证明 §3 中的整数根判别法。

**7.** (a) 令 $k$ 为一个含 $q=p^m$ 个元素的有限域。令 $f(X_1,\ldots,X_n)$ 为 $k[X]$ 中一个次数为 $d$ 的多项式，并假设 $f(0,\ldots,0)=0$。满足 $f(a)=0$ 的元素 $(a_1,\ldots,a_n)\in k^{(n)}$ 称为 $f$ 的一个零点。若 $n>d$，证明 $f$ 在 $k^{(n)}$ 中至少还有一个零点。[*提示：* 反证，并比较与

$$
1-f(X)^{q-1}
$$

相对应的约化多项式和 $(1-X_1^{q-1})\cdots(1-X_n^{q-1})$ 的次数。这个定理由 Chevalley 给出。]

(b) 按以下思路证明，$f$ 在 $k^{(n)}$ 中的零点个数 $N$ 满足 $\equiv0\pmod p$，从而加强上述结果。令 $i$ 为一个 $\geq1$ 的整数。证明

$$
\sum_{x\in k}x^i=\begin{cases}q-1=-1&\text{若 }q-1\text{ 整除 }i,\\0&\text{否则。}\end{cases}
$$

把上述关于 $i$ 的函数记为 $\psi(i)$。证明

<span class="original-page-anchor" id="pdf-page-229" aria-hidden="true"></span>

$$
N\equiv\sum_{x\in k^{(n)}}(1-f(x)^{q-1}),
$$

并对每个由 $\geq0$ 的整数组成的 $n$ 元组 $(i_1,\ldots,i_n)$，证明

$$
\sum_{x\in k^{(n)}}x_1^{i_1}\cdots x_n^{i_n}=\psi(i_1)\cdots\psi(i_n).
$$

证明上面关于 $N$ 的和中的两项模 $p$ 都为 $0$。（上述论证由 Warning 给出。）

(c) 把 Chevalley 定理推广到 $n$ 个变量的 $r$ 个多项式 $f_1,\ldots,f_r$，其次数分别为 $d_1,\ldots,d_r$。若它们没有常数项，且 $n>\sum d_i$，证明它们有一个非平凡公共零点。

(d) 证明任意函数 $f:k^{(n)}\to k$ 都可以用一个多项式表示。（与前面一样，$k$ 是一个有限域。）

**8.** 令 $A$ 为一个交换整环，$X$ 为 $A$ 上的一个变量。令 $a,b\in A$，并假设 $a$ 是 $A$ 中的可逆元。证明映射 $X\mapsto aX+b$ 可唯一地扩张为 $A[X]$ 的一个自同构，在 $A$ 上诱导恒等映射。它的逆自同构是什么？

**9.** 证明 $A[X]$ 的每个在 $A$ 上诱导恒等映射的自同构，都具有习题 8 中所述的形式。

**10.** 令 $K$ 为一个域，$K(X)$ 为 $K[X]$ 的分式域。证明 $K(X)$ 的每个在 $K$ 上诱导恒等映射的自同构，都具有如下形式：

$$
X\mapsto\frac{aX+b}{cX+d},
$$

其中 $a,b,c,d\in K$，使 $(aX+b)/(cX+d)$ 不属于 $K$；等价地，$ad-bc\neq0$。

**11.** 令 $A$ 为一个交换整环，$K$ 为其分式域。这里说明，微积分中的某些公式具有纯代数背景。令 $D:A\to A$ 为一个**导子**，即满足乘积求导法则的加法同态，该法则为

$$
D(xy)=xDy+yDx,\quad x,y\in A.
$$

(a) 证明 $D$ 可以唯一地扩张为从 $K$ 到自身的一个导子，且此扩张满足法则

$$
D(x/y)=\frac{yDx-xDy}{y^2},
$$

其中 $x,y\in A$，$y\neq0$。[用该公式定义扩张，证明它不依赖于用来表示分式 $x/y$ 的 $x,y$ 的选择，并证明它是一个在 $A$ 的元素上取原有值的导子。]

(b) 对于 $x\in K^*$，令 $L(x)=Dx/x$。证明 $L(xy)=L(x)+L(y)$。同态 $L$ 称为**对数导数**。

(c) 令 $D$ 为域 $k$ 上的多项式环 $k[X]$ 中的通常导数。令 $R(X)=c\prod(X-\alpha_i)^{m_i}$，其中 $\alpha_i\in k$、$c\in k$，$m_i\in\mathbf Z$，因此 $R(X)$ 是一个有理<span class="original-page-anchor" id="pdf-page-230" aria-hidden="true"></span>函数。证明

$$
R'/R=\sum\frac{m_i}{X-\alpha_i}.
$$

**12.** (a) 若 $f(X)=aX^2+bX+c$，证明 $f$ 的判别式为 $b^2-4ac$。

(b) 若 $f(X)=a_0X^3+a_1X^2+a_2X+a_3$，证明 $f$ 的判别式为

$$
a_1^2a_2^2-4a_0a_2^3-4a_1^3a_3-27a_0^2a_3^2+18a_0a_1a_2a_3.
$$

(c) 令 $f(X)=(X-t_1)\cdots(X-t_n)$。证明

$$
D_f=(-1)^{n(n-1)/2}\prod_{i=1}^nf'(t_i).
$$

**13.** 以下多项式都取在特征为 $0$ 的代数闭域上。

(a) 证明

**Davenport 定理。** *令 $f(t),g(t)$ 为满足 $f^3-g^2\neq0$ 的多项式。则*

$$
\deg(f^3-g^2)\geq\frac12\deg f+1.
$$

换一种说法，令 $h=f^3-g^2$，并假设 $h\neq0$，则

$$
\deg f\leq2\deg h-2.
$$

为证明这一点，首先假设 $f,g$ 互素，并应用 Mason 定理。一般情形按以下方式处理。

(b) *令 $A,B,f,g$ 为多项式，使 $Af,Bg$ 非零且互素。令 $h=Af^3+Bg^2$。则*

$$
\deg f\leq\deg A+\deg B+2\deg h-2.
$$

这直接由 Mason 定理得到。然后，从不一定互素的 $f,g$ 开始，不断提出公因子，直到不能再提出为止，以完成所需的归结。我自己做时，需要把这一步做三次，因此不要在得到结论之前停下来。

(c) 把 (b) 推广到 $f^m-g^n$ 的情形，其中指数 $m,n$ 为任意正整数。

**14.** 证明广义 Szpiro 猜想蕴含 $abc$ 猜想。

**15.** 证明 $abc$ 猜想蕴含以下猜想：存在无穷多个素数 $p$，使 $2^{p-1}\not\equiv1\bmod p^2$。[参见 §7 末尾的参考文献 [Sil 88] 和 [La 90]。]

**16.** 令 $w$ 为一个复数，$c=\max(1,|w|)$。令 $F,G$ 为具有复系数的非零一元多项式，次数分别为 $d,d'$，且满足 $|F|,|G|\geq1$。令 $R$ 为它们的结式。则

$$
|R|\leq c^{d+d'}[|F(w)|+|G(w)|]|F|^{d'}|G|^d(d+d')^{d+d'}.
$$

（用 $|F|$ 表示 $F$ 的各系数的绝对值的最大值。）

**17.** 令 $d$ 为一个 $\geq3$ 的整数。证明存在 $\mathbf Q$ 上一个次数为 $d$ 的不可约多项式，恰有 $d-2$ 个实根和一对共轭复根。使用以下构造。令 $b_1,\ldots,b_{d-2}$ 为互不相同的<span class="original-page-anchor" id="pdf-page-231" aria-hidden="true"></span>整数，令 $a$ 为一个 $>0$ 的整数。令

$$
g(X)=(X^2+a)(X-b_1)\cdots(X-b_{d-2})=X^d+c_{d-1}X^{d-1}+\cdots+c_0.
$$

注意，对所有 $i$ 都有 $c_i\in\mathbf Z$。令 $p$ 为一个素数，令

$$
g_n(X)=g(X)+\frac{p}{p^{dn}},
$$

于是 $g_n$ 收敛到 $g$（即 $g_n$ 的系数收敛到 $g$ 的系数）。

(a) 证明当 $n$ 足够大时，$g_n$ 恰有 $d-2$ 个实根。（可以用一点微积分，也可以使用你想用的任何方法。）

(b) 证明 $g_n$ 在 $\mathbf Q$ 上不可约。

### 整数值多项式

**18.** 令 $P(X)\in\mathbf Q[X]$ 为一个有理系数的一元多项式。可能对所有足够大的整数 $n$ 都有 $P(n)\in\mathbf Z$，而 $P$ 未必具有整数系数。

(a) 给出一个这样的例子。

(b) 假设 $P$ 有上述性质。证明存在整数 $c_0,c_1,\ldots,c_r$，使

$$
P(X)=c_0\binom Xr+c_1\binom X{r-1}+\cdots+c_r,
$$

其中

$$
\binom Xr=\frac1{r!}X(X-1)\cdots(X-r+1)
$$

为二项式系数函数。特别地，对所有 $n$ 都有 $P(n)\in\mathbf Z$。因此可以称 $P$ 为**整数值多项式**。

(c) 令 $f:\mathbf Z\to\mathbf Z$ 为一个函数。假设存在一个整数值多项式 $Q$，使由

$$
(\Delta f)(n)=f(n)-f(n-1)
$$

定义的差分函数 $\Delta f$，对所有足够大的正整数 $n$ 都等于 $Q(n)$。证明存在一个整数值多项式 $P$，使得对所有足够大的 $n$ 都有 $f(n)=P(n)$。

### 对称函数的习题

**19.** (a) 令 $X_1,\ldots,X_n$ 为变量。证明 $\mathbf Z[X_1,\ldots,X_n]$ 中任一次数 $>n(n-1)$ 的齐次多项式，都属于由初等对称函数 $s_1,\ldots,s_n$ 生成的理想。

(b) 沿用相同的记号，证明 $\mathbf Z[X_1,\ldots,X_n]$ 是自由的 $\mathbf Z[s_1,\ldots,s_n]$ 模，以单项式

$$
X^{(r)}=X_1^{r_1}\cdots X_n^{r_n}
$$

为一组基，其中 $0\leq r_i\leq n-i$。

<span class="original-page-anchor" id="pdf-page-232" aria-hidden="true"></span>

(c) 令 $X_1,\ldots,X_n$ 和 $Y_1,\ldots,Y_m$ 为两组独立的变量。令 $s_1,\ldots,s_n$ 为 $X$ 的初等对称函数，$s_1',\ldots,s_m'$ 为 $Y$ 的初等对称函数（采用向量记号）。证明 $\mathbf Z[X,Y]$ 是自由的 $\mathbf Z[s,s']$ 模，以 $X^{(r)}Y^{(q)}$ 为一组基，且指数 $(r),(q)$ 满足与 (b) 中相同的不等式。

(d) 令 $I$ 为 $\mathbf Z[s,s']$ 的一个理想，$J$ 为 $I$ 在 $\mathbf Z[X,Y]$ 中生成的理想。证明

$$
J\cap\mathbf Z[s,s']=I.
$$

**20.** 令 $A$ 为一个交换环，$t$ 为一个变量。令

$$
f(t)=\sum_{i=0}^ma_it^i\quad\text{和}\quad g(t)=\sum_{i=0}^nb_it^i
$$

为常数项 $a_0=b_0=1$ 的多项式。若

$$
f(t)g(t)=1,
$$

证明存在一个整数 $N$（$=(m+n)(m+n-1)$），使任一满足 $\sum jr_j>N$ 的单项式

$$
a_1^{r_1}\cdots a_n^{r_n}
$$

都等于 $0$。

> **译校注。** 原书单项式的末项印作 $a_n^{r_n}$；按 $f$ 的系数范围，末项应为 $a_m^{r_m}$。

[*提示：* 把各个 $a$ 和 $b$ 换成变量。用习题 19(b) 证明，任意权 $>N$ 的单项式 $M(a)$ 都属于由元素

$$
c_k=\sum_{i=0}^ka_ib_{k-i}
$$

生成的理想 $I$（令 $a_0=b_0=1$）。注意，$c_k$ 是 $m+n$ 个变量 $(X,Y)$ 的第 $k$ 个初等对称函数。]

[*注：* 关于一些涉及对称函数的有趣背景，参看 Cartier 在 Bourbaki 讨论班 1982–1983 年的报告。]

### $\lambda$ 环

以下习题开始了一条思路，它将在第 V 章习题 33、第 XVIII 章习题 22–24 以及第 XX 章 §3 中继续展开。这些思路很大程度上起源于 Hirzebruch 的黎曼–罗赫定理及 Grothendieck 的推广，后者给出了 $\lambda$ 环的一般定义。

令 $K$ 为一个交换环。所谓 **$\lambda$ 运算**，是指对每个整数 $i\geq0$，有一个映射

$$
\lambda^i:K\to K,
$$

并且对所有 $x\in K$ 满足关系

$$
\lambda^0(x)=1,\quad\lambda^1(x)=x,
$$

以及对所有整数 $n\geq0$ 和 $x,y\in K$，有

$$
\lambda^n(x+y)=\sum_{i=0}^n\lambda^i(x)\lambda^{n-i}(y).
$$

<span class="original-page-anchor" id="pdf-page-233" aria-hidden="true"></span>

读者将在讨论交错积和对称积的章节中遇到这类运算的例子。不过，这类运算的形式体系只依赖于上述关系，因此可以在这里的形式幂级数背景下建立。给定一个 $\lambda$ 运算，此时也称 $K$ 为一个 **$\lambda$ 环**，定义幂级数

$$
\lambda_t(x)=\sum_{i=0}^\infty\lambda^i(x)t^i.
$$

证明以下断言。

**21.** 映射 $x\mapsto\lambda_t(x)$ 是从 $K$ 的加法群到常数项为 $1$ 的幂级数所组成的乘法群 $1+tK[[t]]$ 的一个同态。反过来，满足 $\lambda_t(x)=1+xt+\text{高次项}$ 的任何这样的同态，都给出 $\lambda$ 运算。

**22.** 令 $s=at+\text{高次项}$ 为 $K[[t]]$ 中的一个幂级数，其中 $a$ 为 $K$ 中的可逆元。证明存在幂级数

$$
t=g(s)=\sum b_is^i,\quad\text{其中 }b_i\in K.
$$

证明任意幂级数 $f(t)\in K[[t]]$ 都可以写成 $h(s)$ 的形式，其中 $h$ 是另一个系数属于 $K$ 的幂级数。

给定 $K$ 上的一个 $\lambda$ 运算，定义相应的 **Grothendieck 幂级数**

$$
\gamma_t(x)=\lambda_{t/(1-t)}(x)=\lambda_s(x),
$$

其中 $s=t/(1-t)$。则映射

$$
x\mapsto\gamma_t(x)
$$

与前面一样是一个同态。通过关系

$$
\gamma_t(x)=\sum\gamma^i(x)t^i
$$

定义 $\gamma^i(x)$。证明 $\gamma$ 满足以下性质。

**23.** (a) 对每个整数 $n\geq0$，有

$$
\gamma^n(x+y)=\sum_{i=0}^n\gamma^i(x)\gamma^{n-i}(y).
$$

(b) $\gamma_t(1)=1/(1-t)$。

(c) $\gamma_t(-1)=1-t$。

> **译校注。** 要得到 (b)、(c)，需要通常另加的条件 $\lambda_t(1)=1+t$，即 $\lambda^i(1)=0$（$i>1$）。本节开头列出的加法运算公理本身没有包含这一条件；下面习题 24 也使用它。

**24.** 假设对 $i>1$ 有 $\lambda^iu=0$。证明：

(a) $\gamma_t(u-1)=1+(u-1)t$。

(b) $\gamma_t(1-u)=\sum_{i=0}^\infty(1-u)^it^i$。

**25. 伯努利数。** 把伯努利数 $B_k$ 定义为幂级数

$$
F(t)=\frac{t}{e^t-1}=\sum_{k=0}^\infty B_k\frac{t^k}{k!}
$$

中的系数。

<span class="original-page-anchor" id="pdf-page-234" aria-hidden="true"></span>

当然，$e^t=\sum t^n/n!$ 是系数为有理数 $1/n!$ 的标准幂级数。证明：

(a) $B_0=1$，$B_1=-\frac12$，$B_2=\frac16$。

(b) $F(-t)=t+F(t)$，且当 $k$ 是不等于 $1$ 的奇数时，$B_k=0$。

**26. 伯努利多项式。** 通过幂级数展开

$$
F(t,X)=\frac{te^{tX}}{e^t-1}=\sum_{k=0}^\infty\mathbf B_k(X)\frac{t^k}{k!}
$$

定义伯努利多项式 $\mathbf B_k(X)$。

显然 $B_k=\mathbf B_k(0)$，因此伯努利数是伯努利多项式的常数项。证明：

(a) $\mathbf B_0(X)=1$，$\mathbf B_1(X)=X-\frac12$，$\mathbf B_2(X)=X^2-X+\frac16$。

(b) 对每个正整数 $N$，

$$
\mathbf B_k(X)=N^{k-1}\sum_{a=0}^{N-1}\mathbf B_k\left(\frac{X+a}{N}\right).
$$

(c) $\mathbf B_k(X)=X^k-\frac12kX^{k-1}+\text{低次项}$。

(d) $F(t,X+1)-F(t,X)=te^{Xt}=t\sum X^k\dfrac{t^k}{k!}$。

(e) 对 $k\geq1$，有 $\mathbf B_k(X+1)-\mathbf B_k(X)=kX^{k-1}$。

**27.** 令 $N$ 为一个正整数，$f$ 为 $\mathbf Z/N\mathbf Z$ 上的一个函数。构造幂级数

$$
F_f(t,X)=\sum_{a=0}^{N-1}f(a)\frac{te^{(a+X)t}}{e^{Nt}-1}.
$$

按照 Leopoldt 的定义，通过

$$
F_f(t,X)=\sum_{k=0}^\infty\mathbf B_{k,f}(X)\frac{t^k}{k!}
$$

定义关于函数 $f$ 的**广义伯努利多项式**。

特别地，把 $\mathbf B_{k,f}(X)$ 的常数项定义为**广义伯努利数** $B_{k,f}=\mathbf B_{k,f}(0)$，这是 Leopoldt 在分圆域中引入的。证明：

(a) $F_f(t,X+k)=e^{kt}F_f(t,X)$。

(b) $F_f(t,X+N)-F_f(t,X)=(e^{Nt}-1)F_f(t,X)$。

(c)

$$
\frac1k[\mathbf B_{k,f}(X+N)-\mathbf B_{k,f}(X)]=\sum_{a=0}^{N-1}f(a)(a+X)^{k-1}.
$$

(d)

$$
\begin{aligned}
\mathbf B_{k,f}(X)&=\sum_{i=0}^k\binom kiB_{i,f}X^{n-i}\\
&=B_{k,f}+kB_{k-1,f}X+\cdots+kB_{1,f}X^{k-1}+B_{0,f}X^k.
\end{aligned}
$$

> **译校注。** 原书第一行的幂印为 $X^{n-i}$；本式的多项式指标和求和上限均为 $k$，应为 $X^{k-i}$，也与第二行展开一致。

*注。* 关于伯努利数与伯努利多项式的这些习题，不仅是为了给正文材料提供例子，也是为了说明这些材料如何引向数学中的重要领域：在拓扑学和代数几何中，围绕<span class="original-page-anchor" id="pdf-page-235" aria-hidden="true"></span>黎曼–罗赫定理；在解析数论与代数数论中，例如 zeta 函数理论和模形式理论。参见我的《模形式导论》（*Introduction to Modular Forms*），Springer-Verlag，New York，1976，第 XIV、XV 章；我的《分圆域》（*Cyclotomic Fields*），I 和 II，Springer-Verlag，New York，1990，第 2 章 §2；Kubert–Lang 的《模单位》（*Modular Units*），Springer-Verlag，New York，1981；等等。

### 进一步的说明，1996–2001

Umberto Zannier 告诉我，通常称为 Mason 定理的结果，Stothers 早在三年前就已证明，见 [Sto 81] 定理 1.1。Zannier 本人在不知道 Stothers 那篇论文的情况下，发表了一些关于 Davenport 定理的结果 [Za 95]，所用的方法与 Stothers 的方法类似，重新发现了 Stothers 的某些结果，并进一步超越了这些结果。事实上，Stothers 使用了代数几何中的“Belyi 方法”，这一方法越来越多地作为基本工具出现。Mason 给出了一个非常初等的证明，只需代数的基础知识就能理解。Noah Snyder [Sny 00] 给出了一个更短、非常优美的 Mason–Stothers 定理证明。我很感谢 Snyder 在发表前就把这个证明给我看，我在 [La 99b] 中重现了它。不过，我推荐读者查看 Snyder 的版本。

[La 99b] S. Lang，《面向本科生的数学讲座》（*Math Talks for Undergraduates*），Springer Verlag，1999。

[Sny 00] N. Snyder，“Mason 定理的另一个证明”（An alternate proof of Mason's theorem），*Elemente der Math.* **55**（2000），第 93–94 页。

[Sto 81] W. Stothers，“多项式恒等式与 hauptmoduln”（Polynomial identities and hauptmoduln），*Quart. J. Math. Oxford*（2）**32**（1981），第 349–370 页。

[Za 95] U. Zannier，“关于 $f^3-g^2$ 次数的 Davenport 界及黎曼存在定理”（On Davenport's bound for the degree of $f^3-g^2$ and Riemann's existence theorem），*Acta Arithm.* **LXXI.2**（1995），第 107–137 页。
