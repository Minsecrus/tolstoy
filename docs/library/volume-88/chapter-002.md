---
title: "第二章 表示论的基本概念"
description: "《Introduction to Representation Theory》中文译文。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"第一章 导论","link":"/library/volume-88/chapter-001"}
next: {"text":"第三章 表示论的一般结果","link":"/library/volume-88/chapter-003"}
---

# 第二章 表示论的基本概念

<span class="original-page-anchor" id="pdf-page-13" aria-hidden="true"></span>

## 2.1. 什么是表示论？

用专业术语来说，表示论研究结合代数的表示。其基本内容可以简要概括如下。

域 $k$ 上的**结合代数**是一个 $k$-向量空间 $A$，配备满足结合律的双线性乘法 $a,b\mapsto ab$，其中 $a,b\in A$。我们始终考虑带单位元的结合代数，也就是说，存在元素 $1$，使得对所有 $a\in A$ 都有 $1\cdot a=a\cdot1=a$。一个基本例子是向量空间 $V$ 到自身的线性算子所构成的代数 $\operatorname{End}V$。其他重要例子包括由生成元和关系定义的代数，如群代数和李代数的泛包络代数。

结合代数 $A$ 的一个**表示**（也称**左 $A$-模**）是一个向量空间 $V$，配备同态 $\rho:A\to\operatorname{End}V$，即保持乘法和单位元的线性映射。

表示 $V$ 的一个**子表示**是子空间 $U\subset V$，它在所有算子 $\rho(a)$（$a\in A$）作用下保持不变。此外，若 $V_1,V_2$ 是 $A$ 的两个表示，则其**直和** $V_1\oplus V_2$ 自然带有 $A$ 的表示结构。

<span class="original-page-anchor" id="pdf-page-14" aria-hidden="true"></span>

若 $A$ 的非零表示 $V$ 只有 $0$ 和 $V$ 自身这两个子表示，就称它**不可约**；若它不能写成两个非零子表示的直和，就称它**不可分解**。显然，不可约表示一定不可分解，但反过来不成立。

表示论中的典型问题有：

(1) 对给定代数 $A$ 的不可约表示进行分类。

(2) 对 $A$ 的不可分解表示进行分类。

(3) 只考虑有限维表示，解决 (1) 和 (2)。

前面提到，代数 $A$ 往往由生成元和关系给出。例如，李代数 $\mathfrak{sl}(2)$ 的泛包络代数 $U$ 由 $h,e,f$ 生成，定义关系为

$$
he-eh=2e,\quad hf-fh=-2f,\quad ef-fe=h.\tag{2.1.1}
$$

因此，求 $A$ 的 $N$ 维表示这样的问题，就转化为求解一组以若干未知 $N\times N$ 矩阵为变量的非线性代数方程，例如以未知矩阵 $h,e,f$ 为变量的方程组 (2.1.1)。

这些方程组乍看复杂得令人无从下手，竟然能用表示论的方法彻底求解，这实在令人惊叹！例如，我们将证明下面的定理。

**定理 2.1.1。** 设 $k=\mathbb{C}$ 是复数域，则：

(i) 在等价意义下，代数 $U$ 在每个维数上恰有一个不可约表示 $V_d$。它可以实现为二元变量 $x,y$ 的 $d-1$ 次齐次多项式空间上的表示，由以下公式定义：

$$
\rho(h)=x\frac{\partial}{\partial x}-y\frac{\partial}{\partial y},\quad
\rho(e)=x\frac{\partial}{\partial y},\quad
\rho(f)=y\frac{\partial}{\partial x}.
$$

(ii) $U$ 的任意不可分解有限维表示都是不可约的。也就是说，$U$ 的任意有限维表示都是不可约表示的直和。

另一个例子是箭图的表示论。

<span class="original-page-anchor" id="pdf-page-15" aria-hidden="true"></span>

**箭图**是一个有向图 $Q$（这里假定它是有限的）。$Q$ 在域 $k$ 上的一个**表示**，是为 $Q$ 的每个顶点 $i$ 指定一个 $k$-向量空间 $V_i$，并为每条从 $i$ 指向 $j$ 的有向边 $h$ 指定一个线性算子 $A_h:V_i\to V_j$（允许自环和重边）。我们将说明，箭图 $Q$ 的表示就是某个代数 $P_Q$ 的表示，这个代数称为 $Q$ 的路径代数。因此可以问：$Q$ 的不可分解有限维表示有哪些？

更具体地说，如果 $Q$ 只有有限多个不可分解表示，就称 $Q$ 是**有限型**的。

我们将证明下面这个引人瞩目的定理，它由 P. Gabriel 在 20 世纪 70 年代初证明：

**定理 2.1.2。** 设 $k$ 为一个固定的代数闭域。$Q$ 是否为有限型，与各条边的方向无关。能够产生有限型箭图的连通图如下：

**译校注：** 原书定理未写出 $k$ 必须为固定的代数闭域这一条件；此处按作者 2024 年 6 月 3 日的勘误补入。

- $A_n$：

![A_n Dynkin diagram](/library/volume-88/diagrams/pdf-0015-an.png)

- $D_n$：

![D_n Dynkin diagram](/library/volume-88/diagrams/pdf-0015-dn.png)

- $E_6$

![E_6 Dynkin diagram](/library/volume-88/diagrams/pdf-0015-e6.png)

- $E_7$

![E_7 Dynkin diagram](/library/volume-88/diagrams/pdf-0015-e7.png)

- $E_8$

![E_8 Dynkin diagram](/library/volume-88/diagrams/pdf-0015-e8.png)

<span class="original-page-anchor" id="pdf-page-16" aria-hidden="true"></span>

定理中列出的图称为（单边）**Dynkin 图**。它们出现在许多数学分类问题中，例如单李代数、奇点、柏拉图多面体和反射群的分类。事实上，假如我们要与外星文明建立联系，并向他们展示人类文明的精妙程度，也许展示 Dynkin 图会是最好的选择！

最后一个例子是有限群表示论，它是表示论中最引人入胜的部分之一。这一理论研究有限群 $G$ 的群代数 $A=\mathbb{C}[G]$ 的表示；该代数以 $a_g$（$g\in G$）为基，乘法法则为 $a_ga_h=a_{gh}$。我们将证明，$A$ 的任意有限维表示都是不可约表示的直和，即对于 $A$ 而言，不可约表示与不可分解表示是同一概念（Maschke 定理）。下文还将讨论另一个惊人的结果，即 Frobenius 整除性定理：$A$ 的任意不可约表示的维数都整除 $G$ 的阶。最后，我们将展示如何利用有限群表示论证明 Burnside 定理：若 $p,q$ 是素数，则任意阶为 $p^aq^b$ 的有限群都是可解群。这个定理的陈述完全没有提到表示，表示只出现在证明中；它也有不使用表示的纯群论证明，但要困难得多！

## 2.2. 代数

现在开始系统地讨论表示论。

设 $k$ 是一个域。除非另有说明，我们始终假定 $k$ 是代数闭域，即任意系数属于 $k$ 的非常数多项式都在 $k$ 中有根。最主要的例子是复数域 $\mathbb{C}$，但我们也会考虑特征为 $p$ 的域，例如有 $p$ 个元素的有限域 $\mathbb{F}_p$ 的代数闭包 $\overline{\mathbb{F}}_p$。

**定义 2.2.1。** $k$ 上的**结合代数**是一个 $k$-向量空间 $A$，配备双线性映射 $A\times A\to A$，$(a,b)\mapsto ab$，满足 $(ab)c=a(bc)$。

<span class="original-page-anchor" id="pdf-page-17" aria-hidden="true"></span>

**定义 2.2.2。** 结合代数 $A$ 的**单位元**是满足 $1a=a1=a$ 的元素 $1\in A$。

**命题 2.2.3。** 如果单位元存在，它就是唯一的。

**证明。** 设 $1,1'$ 都是单位元，则 $1=11'=1'$。$\square$

此后，我们所说的代数 $A$ 都指带单位元的结合代数。

**译校注：** 原书此处还假定 $A\ne0$。作者 2024 年 6 月 3 日的勘误指出，这里不需要该条件，而 §2.4 中单代数的定义需要它，因此此处删去，并在单代数定义中明确补入。

**例 2.2.4。** 以下是一些 $k$ 上的代数：

1. $A=k$。

2. $A=k[x_1,\ldots,x_n]$，即变量 $x_1,\ldots,x_n$ 的多项式代数。

3. $A=\operatorname{End}V$，即 $k$-向量空间 $V$ 的自同态代数（也就是从 $V$ 到自身的线性映射或线性算子所成的代数）。乘法为算子的复合。

4. **自由代数** $A=k\langle x_1,\ldots,x_n\rangle$。它的一组基由字母 $x_1,\ldots,x_n$ 构成的字组成，基元素之间的乘法就是字的拼接。

5. 群 $G$ 的**群代数** $A=k[G]$。其基为 $\{a_g,g\in G\}$，乘法法则为 $a_ga_h=a_{gh}$。

**定义 2.2.5。** 如果对所有 $a,b\in A$ 都有 $ab=ba$，就称代数 $A$ 是**交换的**。

例如，上面的例子 1、2 是交换代数，而例子 3（$\dim V>1$ 时）和例子 4（$n>1$ 时）不是交换代数。例子 5 中，$A$ 交换当且仅当 $G$ 交换。

**定义 2.2.6。** **代数同态** $f:A\to B$ 是一个线性映射，满足对所有 $x,y\in A$ 都有 $f(xy)=f(x)f(y)$，并且 $f(1)=1$。

## 2.3. 表示

**定义 2.3.1。** 代数 $A$ 的一个**表示**（也称**左 $A$-模**）是一个向量空间 $V$，配备代数同态 $\rho:A\to\operatorname{End}V$。

<span class="original-page-anchor" id="pdf-page-18" aria-hidden="true"></span>

类似地，**右 $A$-模**是一个空间 $V$，配备反同态 $\rho:A\to\operatorname{End}V$，即 $\rho$ 满足 $\rho(ab)=\rho(b)\rho(a)$ 和 $\rho(1)=1$。

通常把 $\rho(a)v$ 简记为 $av$（左模）或 $va$（右模）。这样，$\rho$ 为同态或反同态的性质就可以写成一种结合律：左模满足 $(ab)v=a(bv)$，右模满足 $(va)b=v(ab)$。

**注 2.3.2。** 设 $M$ 是交换环 $A$ 上的左模。令 $ma:=am$，就可以把 $M$ 看作右 $A$-模。类似地，任意右 $A$-模也可以看作左 $A$-模。因此，对于交换环，我们不区分左、右 $A$-模，统称为 $A$-模。

以下是一些表示的例子。

**例 2.3.3。** 1. $V=0$。

2. $V=A$，同态 $\rho:A\to\operatorname{End}A$ 定义如下：$\rho(a)$ 是左乘 $a$ 的算子，即 $\rho(a)b:=ab$（通常的乘积）。这个表示称为 $A$ 的正则表示。类似地，令 $\rho(a)b:=ba$，就可以赋予 $A$ 右 $A$-模结构。

3. $A=k$。此时 $A$ 的表示就是一个 $k$-向量空间。

4. $A=k\langle x_1,\ldots,x_n\rangle$。此时 $A$ 的表示就是一个 $k$-向量空间 $V$，配备任意一组线性算子 $\rho(x_1),\ldots,\rho(x_n):V\to V$（请说明原因！）。

**定义 2.3.4。** 代数 $A$ 的表示 $V$ 的一个**子表示**，是一个在所有算子 $\rho(a):V\to V$（$a\in A$）作用下保持不变的子空间 $W\subset V$。

例如，$0$ 和 $V$ 总是子表示。

**定义 2.3.5。** 如果 $A$ 的表示 $V\ne0$ 只有 $0$ 和 $V$ 两个子表示，就称它**不可约**（或**单**）。

**定义 2.3.6。** 设 $V_1,V_2$ 是代数 $A$ 的两个表示。**同态**（或**交织算子**）$\phi:V_1\to V_2$ 是一个<span class="original-page-anchor" id="pdf-page-19" aria-hidden="true"></span>与 $A$ 的作用交换的线性算子，即对任意 $v\in V_1$ 都有 $\phi(av)=a\phi(v)$。如果同态 $\phi$ 同时是向量空间的同构，就称它为**表示的同构**。从 $V_1$ 到 $V_2$ 的所有表示同态组成的集合（空间）记为 $\operatorname{Hom}_A(V_1,V_2)$。

如果线性算子 $\phi:V_1\to V_2$ 是表示的同构，则线性算子 $\phi^{-1}:V_2\to V_1$ 也是表示的同构（请验证！）。

若两个表示之间存在同构，就称它们**同构**。在实际使用中，两个同构的表示可以看作“相同”的。不过，两表示之间的同构即使存在，也并不唯一，这一事实有时会带来一些微妙之处。

**定义 2.3.7。** 设 $V_1,V_2$ 是代数 $A$ 的表示。空间 $V_1\oplus V_2$ 自然带有 $A$ 的表示结构，作用为 $a(v_1\oplus v_2)=av_1\oplus av_2$。这个表示称为 $V_1$ 和 $V_2$ 的**直和**。

**定义 2.3.8。** 若代数 $A$ 的非零表示 $V$ 不同构于两个非零表示的直和，就称它**不可分解**。

显然，不可约表示都是不可分解的。但我们将在下文看到，反过来一般并不成立。

表示论的一个主要问题，是在同构意义下对给定代数的不可约表示和不可分解表示进行分类。这个问题通常很难，往往只能部分解决，例如只处理有限维表示。下文将给出一些例子，展示如何对特定代数部分或完全解决这一问题。

现在证明我们的第一个结果——Schur 引理。它的证明虽然十分简单，却是整个表示论的基础。

**命题 2.3.9（Schur 引理）。** 设 $V_1,V_2$ 是任意域 $F$ 上的代数 $A$ 的表示（$F$ 不必是代数闭域）。

<span class="original-page-anchor" id="pdf-page-20" aria-hidden="true"></span>

设 $\phi:V_1\to V_2$ 是非零的表示同态，则：

(i) 如果 $V_1$ 不可约，$\phi$ 就是单射。

(ii) 如果 $V_2$ 不可约，$\phi$ 就是满射。

因此，如果 $V_1,V_2$ 都不可约，$\phi$ 就是同构。

**证明。** (i) $\phi$ 的核 $K$ 是 $V_1$ 的子表示。由于 $\phi\ne0$，这个子表示不可能是 $V_1$。由 $V_1$ 的不可约性，得到 $K=0$。

(ii) $\phi$ 的像 $I$ 是 $V_2$ 的子表示。由于 $\phi\ne0$，这个子表示不可能是 $0$。由 $V_2$ 的不可约性，得到 $I=V_2$。$\square$

**推论 2.3.10（代数闭域上的 Schur 引理）。** 设 $V$ 是代数闭域 $k$ 上的代数 $A$ 的有限维不可约表示，$\phi:V\to V$ 是交织算子。则存在 $\lambda\in k$，使得 $\phi=\lambda\cdot\operatorname{Id}$（即标量算子）。

**注 2.3.11。** 这个推论在实数域上不成立：取 $A=\mathbb{C}$（视为 $\mathbb{R}$-代数）和 $V=A$ 即可。

**证明。** 取 $\phi$ 的一个特征值 $\lambda$（即 $\phi$ 的特征多项式的一个根）。由于 $k$ 是代数闭域，这样的 $\lambda$ 一定存在。算子 $\phi-\lambda\operatorname{Id}$ 是从 $V$ 到 $V$ 的交织算子，但不是同构，因为其行列式为零。于是由命题 2.3.9，这个算子必为零，结论得证。$\square$

**推论 2.3.12。** 设 $A$ 是交换代数，则 $A$ 的任意有限维不可约表示 $V$ 都是一维的。

**注 2.3.13。** 任意代数的一维表示都自动不可约。

**证明。** 设 $V$ 不可约。对于任意元素 $a\in A$，算子 $\rho(a):V\to V$ 是交织算子。事实上，

$$
\rho(a)\rho(b)v=\rho(ab)v=\rho(ba)v=\rho(b)\rho(a)v
$$

（第二个等号由代数的交换性得到）。因此，由 Schur 引理，对任意 $a\in A$，$\rho(a)$ 都是标量算子。于是<span class="original-page-anchor" id="pdf-page-21" aria-hidden="true"></span>$V$ 的任意子空间都是子表示。但 $V$ 不可约，所以 $V$ 只有 $0$ 和 $V$ 两个子空间。这说明 $\dim V=1$，因为 $V\ne0$。$\square$

**例 2.3.14。** 本例中的表示均假定为有限维。

**译校注：** 原书未明确写出有限维假设；此处按作者 2024 年 6 月 3 日的勘误补入。

1. $A=k$。由于 $A$ 的表示就是向量空间，$V=A$ 是唯一的不可约表示，也是唯一的不可分解表示。

2. $A=k[x]$。由于这个代数是交换的，$A$ 的不可约表示就是它的一维表示。前面已经讨论过，这些表示由单个算子 $\rho(x)$ 决定。在一维情形下，这个算子就是 $k$ 中的一个数。因此，$A$ 的所有不可约表示为 $V_\lambda=k$（$\lambda\in k$），其中 $A$ 的作用由 $\rho(x)=\lambda$ 定义。显然，这些表示两两不同构。

$k[x]$ 的不可分解表示的分类更有意思。为此，回顾一下：有限维向量空间 $V$ 上的任意线性算子都能化为若尔当标准形。具体来说，若尔当块 $J_{\lambda,n}$ 是 $k^n$ 上的算子，在标准基下满足：当 $i>1$ 时，$J_{\lambda,n}e_i=\lambda e_i+e_{i-1}$；并且 $J_{\lambda,n}e_1=\lambda e_1$。对于任意线性算子 $B:V\to V$，都存在 $V$ 的一组基，使得 $B$ 在这组基下的矩阵是若尔当块的直和。因此，$A$ 的所有不可分解表示为 $V_{\lambda,n}=k^n$（$\lambda\in k$），其中 $\rho(x)=J_{\lambda,n}$。这些表示不可分解且两两不同构，都是若尔当标准形定理的推论；该定理尤其指出，算子的若尔当标准形在各块排列次序之外是唯一的。

这个例子说明，代数的不可分解表示不一定不可约。

3. 群代数 $A=k[G]$，其中 $G$ 为群。$A$ 的表示就是 $G$ 的表示，即一个向量空间 $V$，配备群同态 $\rho:G\to\operatorname{Aut}(V)$。这里 $\operatorname{Aut}(V)=GL(V)$ 表示空间 $V$ 到自身的可逆线性映射群（即 $V$ 的一般线性群）。

<span class="original-page-anchor" id="pdf-page-22" aria-hidden="true"></span>

**习题 2.3.15。** 设 $V$ 是代数 $A$ 的一个非零有限维表示。证明它有一个不可约子表示。再举例说明，这一结论对无限维表示并不总是成立。

**习题 2.3.16。** 设 $A$ 是域 $k$ 上的代数。$A$ 的**中心** $Z(A)$ 是与 $A$ 的所有元素都交换的元素 $z\in A$ 所成的集合。例如，若 $A$ 交换，则 $Z(A)=A$。

(a) 证明：若 $V$ 是 $A$ 的有限维不可约表示，则任意元素 $z\in Z(A)$ 在 $V$ 中的作用都是乘以某个标量 $\chi_V(z)$。证明 $\chi_V:Z(A)\to k$ 是同态。它称为 $V$ 的**中心特征标**。

(b) 证明：若 $V$ 是 $A$ 的有限维不可分解表示，则对任意 $z\in Z(A)$，$z$ 在 $V$ 中的作用算子 $\rho(z)$ 只有一个特征值 $\chi_V(z)$，它等于 $z$ 在 $V$ 的某个不可约子表示上的作用标量。因此 $\chi_V:Z(A)\to k$ 是同态，也称为 $V$ 的中心特征标。

(c) (b) 中的 $\rho(z)$ 一定是标量算子吗？

**习题 2.3.17。** 设 $A$ 是结合代数，$V$ 是 $A$ 的表示。用 $\operatorname{End}_A(V)$ 表示所有表示同态 $V\to V$ 构成的代数。证明 $\operatorname{End}_A(A)=A^{\mathrm{op}}$，其中 $A^{\mathrm{op}}$ 是将 $A$ 的乘法顺序反转得到的代数。

**习题 2.3.18。** 证明以下由 Dixmier 给出的“无限维 Schur 引理”：设 $A$ 是 $\mathbb{C}$ 上的代数，$V$ 是 $A$ 的不可约表示，且有一组至多可数的基。则任意表示同态 $\phi:V\to V$ 都是标量算子。

提示：由通常的 Schur 引理，代数 $D:=\operatorname{End}_A(V)$ 是除代数。证明 $D$ 的维数至多可数。假设 $\phi$ 不是标量，考虑子域 $\mathbb{C}(\phi)\subset D$。证明 $\mathbb{C}(\phi)$ 是 $\mathbb{C}$ 的超越扩张，由此推出 $\mathbb{C}(\phi)$ 的维数不可数，从而得到矛盾。

<span class="original-page-anchor" id="pdf-page-23" aria-hidden="true"></span>

## 2.4. 理想

代数 $A$ 的一个**左理想**是一个子空间 $I\subseteq A$，满足对所有 $a\in A$ 都有 $aI\subseteq I$。类似地，**右理想**是子空间 $I\subseteq A$，满足对所有 $a\in A$ 都有 $Ia\subseteq I$。同时是左理想和右理想的子空间称为**双边理想**。

左理想就是正则表示 $A$ 的子表示。右理想就是反代数 $A^{\mathrm{op}}$ 的正则表示的子表示。

以下是一些理想的例子：

- 对任意代数 $A$，$0$ 和 $A$ 都是双边理想。若代数 $A\ne0$ 只有 $0$ 和 $A$ 两个双边理想，就称 $A$ 是**单**的。

**译校注：** 原书将 $A\ne0$ 作为 §2.2 的统一假设。按作者 2024 年 6 月 3 日的勘误，已从该处删去，并在此处单代数的定义中明确补入。

- 若 $\phi:A\to B$ 是代数同态，则 $\ker\phi$ 是 $A$ 的双边理想。

- 若 $S$ 是代数 $A$ 的任意子集，则 **$S$ 生成的双边理想**记为 $\langle S\rangle$，它是所有形如 $asb$ 的元素张成的空间，其中 $a,b\in A$、$s\in S$。类似地，可定义 $S$ 生成的左理想 $\langle S\rangle_\ell=\operatorname{span}\{as\}$ 和右理想 $\langle S\rangle_r=\operatorname{span}\{sb\}$。

**习题 2.4.1。** 环 $A$ 的一个**极大理想**是一个理想 $I\ne A$，满足任何严格包含它的理想都等于 $A$。（此定义适用于左理想、右理想和双边理想。）证明任意非零含幺环都有极大左理想、极大右理想和极大双边理想。（提示：使用佐恩引理。）

**译校注：** 原书习题写作“任意含幺环”。由于本译文按作者勘误不再统一排除零代数，这里明确保留原题所需的非零条件；零环没有真理想。

## 2.5. 商

设 $A$ 是代数，$I$ 是 $A$ 的一个双边理想。$A/I$ 是 $I$ 的（加法）陪集所成的集合。设 $\pi:A\to A/I$ 为商映射。在 $A/I$ 中定义乘法 $\pi(a)\cdot\pi(b):=\pi(ab)$。这个定义是良定的：若 $\pi(a)=\pi(a')$，则

$$
\pi(a'b)=\pi(ab+(a'-a)b)=\pi(ab)+\pi((a'-a)b)=\pi(ab)
$$

因为 $I$ 是右理想，所以 $(a'-a)b\in Ib\subseteq I=\ker\pi$。类似地，若 $\pi(b)=\pi(b')$，则

$$
\pi(ab')=\pi(ab+a(b'-b))=\pi(ab)+\pi(a(b'-b))=\pi(ab)
$$

<span class="original-page-anchor" id="pdf-page-24" aria-hidden="true"></span>

因为 $I$ 也是左理想，所以 $a(b'-b)\in aI\subseteq I=\ker\pi$。因此，$A/I$ 是一个代数。

类似地，若 $V$ 是 $A$ 的表示，$W\subset V$ 是子表示，则 $V/W$ 也是表示。事实上，设 $\pi:V\to V/W$ 为商映射，定义 $\rho_{V/W}(a)\pi(x):=\pi(\rho_V(a)x)$ 即可。

前面已经指出，$A$ 的左理想就是 $A$ 的正则表示的子表示，反之亦然。因此，如果 $I$ 是 $A$ 的左理想，$A/I$ 就是 $A$ 的表示。

**习题 2.5.1。** 设 $A=k[x_1,\ldots,x_n]$，$I\ne A$ 是 $A$ 的任意理想，且包含所有次数 $\ge N$ 的齐次多项式。证明 $A/I$ 是 $A$ 的不可分解表示。

**习题 2.5.2。** 设 $V\ne0$ 是 $A$ 的表示。若向量 $v\in V$ 生成 $V$，即 $Av=V$，就称 $v$ 是**循环向量**。具有循环向量的表示称为**循环表示**。证明：

(a) $V$ 不可约，当且仅当 $V$ 的所有非零向量都是循环向量。

(b) $V$ 是循环表示，当且仅当它同构于某个 $A/I$，其中 $I$ 是 $A$ 的左理想。

(c) 举出一个不可分解但并非循环的表示。

提示：取 $A=\mathbb{C}[x,y]/I_2$，其中 $I_2$ 是所有次数 $\ge2$ 的齐次多项式张成的理想（所以 $A$ 有一组基 $1,x,y$）。设 $V=A^*$ 是 $A$ 上的线性泛函空间，$A$ 的作用由 $(\rho(a)f)(b)=f(ba)$ 给出。证明 $V$ 就是所求的例子。

## 2.6. 由生成元和关系定义的代数

设 $f_1,\ldots,f_m$ 是自由代数 $k\langle x_1,\ldots,x_n\rangle$ 的元素。我们称代数 $A:=k\langle x_1,\ldots,x_n\rangle/\langle\{f_1,\ldots,f_m\}\rangle$ **由 $x_1,\ldots,x_n$ 生成，定义关系为** $f_1=0,\ldots,f_m=0$。

<span class="original-page-anchor" id="pdf-page-25" aria-hidden="true"></span>

## 2.7. 代数的例子

下面两个例子，是非交换结合代数中最简单而又有意思的例子之一：

(1) **Weyl 代数** $k\langle x,y\rangle/\langle yx-xy-1\rangle$；

(2) **$q$-Weyl 代数**，由 $x,x^{-1},y,y^{-1}$ 生成，定义关系为 $yx=qxy$ 和 $xx^{-1}=x^{-1}x=yy^{-1}=y^{-1}y=1$。

**命题 2.7.1。** (i) Weyl 代数 $A$ 的一组基为 $\{x^iy^j,i,j\ge0\}$。

(ii) $q$-Weyl 代数 $A_q$ 的一组基为 $\{x^iy^j,i,j\in\mathbb{Z}\}$。

**证明。** (i) 先证明元素 $x^iy^j$ 张成 $A$。任意由 $x,y$ 组成的字，都可以通过交换其中一些 $x,y$ 的次序，整理成所有 $x$ 都在所有 $y$ 左边的形式。由于 $yx-xy=1$，交换时会产生误差项，但这些误差项是若干单项式之和，其中 $x,y$ 的总个数比原来的字更少。因此，继续整理下去，就能把所有项排好，并把任意字写成 $x^iy^j$ 的线性组合。

证明 $x^iy^j$ 线性无关则要用到表示论。取变量 $a$，令 $E=t^ak[a][t,t^{-1}]$（这里 $t^a$ 只是形式符号，所以实际上 $E=k[a][t,t^{-1}]$）。规定 $xf=tf$、$yf=\frac{df}{dt}$，其中 $\frac{d(t^{a+n})}{dt}:=(a+n)t^{a+n-1}$，就使 $E$ 成为 $A$ 的表示。现在假设存在非平凡线性关系 $\sum c_{ij}x^iy^j=0$，则算子

$$
L=\sum c_{ij}t^i\left(\frac{d}{dt}\right)^j
$$

在 $E$ 上作用为零。把 $L$ 写成

$$
L=\sum_{j=0}^r Q_j(t)\left(\frac{d}{dt}\right)^j,
$$

其中 $Q_r\ne0$。于是

$$
Lt^a=\sum_{j=0}^r Q_j(t)a(a-1)\cdots(a-j+1)t^{a-j}.
$$

<span class="original-page-anchor" id="pdf-page-26" aria-hidden="true"></span>

它必须为零，所以在 $k[a][t,t^{-1}]$ 中有 $\sum_{j=0}^r Q_j(t)a(a-1)\cdots(a-j+1)t^{-j}=0$。取关于 $a$ 的最高次项，得到 $Q_r(t)=0$，矛盾。

(ii) 任意由 $x,y,x^{-1},y^{-1}$ 组成的字，都可以通过乘以 $q$ 的某个幂来整理次序。由此容易得到它们的张成性和线性无关性。$\square$

**注 2.7.2。** (i) 的证明表明，Weyl 代数 $A$ 可以看作一个变量 $t$ 的多项式微分算子代数。

(i) 的证明还引出了忠实表示的概念。

**定义 2.7.3。** 若代数 $A$ 的表示 $\rho:A\to\operatorname{End}V$ 是单射，就称该表示是**忠实的**。

例如，当 $k$ 的特征为零时，$k[t]$ 是 Weyl 代数的忠实表示（请验证！）；但特征为 $p$ 时不是，因为对任意多项式 $Q$ 都有 $(d/dt)^pQ=0$。不过，我们已经看到，表示 $E=t^ak[a][t,t^{-1}]$ 在任意特征下都是忠实的。

**习题 2.7.4。** 设 $A$ 是 Weyl 代数。

(a) 若 $\operatorname{char}k=0$，$A$ 的有限维表示有哪些？$A$ 的双边理想有哪些？

提示：第一个问题可利用两个方阵 $B,C$ 满足 $\operatorname{Tr}(BC)=\operatorname{Tr}(CB)$ 这一事实。第二个问题中，先证明 $A$ 的任意非零双边理想都包含一个关于 $x$ 的非零多项式，再据此确定这个理想。

以下各问均假设 $\operatorname{char}k=p$。

(b) $A$ 的中心是什么？

提示：证明 $x^p,y^p$ 都是中心元素。

(c) 求 $A$ 的所有有限维不可约表示。

提示：设 $V$ 是 $A$ 的有限维不可约表示，$v$ 是 $V$ 中 $y$ 的一个特征向量。证明向量组 $\{v,xv,x^2v,\ldots,x^{p-1}v\}$ 是 $V$ 的一组基。

**习题 2.7.5。** 设 $q$ 是非零复数，$A$ 是 $\mathbb{C}$ 上的 $q$-Weyl 代数。

<span class="original-page-anchor" id="pdf-page-27" aria-hidden="true"></span>

(a) 对不同的 $q$，$A$ 的中心是什么？若 $q$ 不是单位根，$A$ 的双边理想有哪些？

(b) 对哪些 $q$，这个代数有有限维表示？

提示：使用行列式。

(c) 对这样的 $q$，求 $A$ 的所有有限维不可约表示。

提示：与上一题的 (c) 类似。

## 2.8. 箭图

**定义 2.8.1。** **箭图** $Q$ 是一个有向图，允许有自环，也允许两个顶点之间有重边。

**例 2.8.2。**

![四个顶点的箭图例子](/library/volume-88/diagrams/pdf-0027-example.png)

把箭图 $Q$ 的顶点集记为 $I$，边集记为 $E$。对于边 $h\in E$，分别用 $h',h''$ 表示 $h$ 的源点与终点：

![边 h 的源点与终点](/library/volume-88/diagrams/pdf-0027-source-target.png)

**定义 2.8.3。** **箭图 $Q$ 的一个表示**，是为每个顶点 $i\in I$ 指定一个向量空间 $V_i$，为每条边 $h\in E$ 指定一个线性映射 $x_h:V_{h'}\to V_{h''}$。

箭图表示论实际上是代数表示论的一部分：对于每个箭图 $Q$，都有一个称为 $Q$ 的**路径代数**的代数 $P_Q$，使得箭图 $Q$ 的表示与代数 $P_Q$ 的表示是“同一回事”。我们先定义箭图的路径代数，然后说明这两个对象的表示为什么是“同一回事”。

<span class="original-page-anchor" id="pdf-page-28" aria-hidden="true"></span>

**定义 2.8.4。** 箭图 $Q$ 的**路径代数** $P_Q$，以 $Q$ 中的有向路径为基，包括与各顶点对应的平凡路径 $p_i$（$i\in I$）。乘法为路径的拼接：$ab$ 是先走 $b$ 再走 $a$ 得到的路径。若两条路径不能拼接，就把乘积定义为零。

**注 2.8.5。** 容易看出，对有限箭图有 $\sum_{i\in I}p_i=1$，所以 $P_Q$ 是带单位元的代数。

**习题 2.8.6。** 设 $Q$ 是有限箭图。证明代数 $P_Q$ 由 $p_i$（$i\in I$）和 $a_h$（$h\in E$）生成，定义关系如下：

(1) $p_i^2=p_i$；当 $i\ne j$ 时，$p_ip_j=0$；

(2) $a_hp_{h'}=a_h$；当 $j\ne h'$ 时，$a_hp_j=0$；

(3) $p_{h''}a_h=a_h$；当 $i\ne h''$ 时，$p_ia_h=0$；

(4) $\sum_{i\in I}p_i=1$。

**译校注：** 原书习题未明确假定 $Q$ 有限，且定义关系漏写 $\sum_{i\in I}p_i=1$。这里按作者 2024 年 6 月 3 日的勘误补入。

现在说明，箭图的表示为什么就是其路径代数的表示。

设 $V$ 是路径代数 $P_Q$ 的表示。从它出发，可构造 $Q$ 的一个表示：令 $V_i=p_iV$；对任意边 $h$，令 $x_h=a_h|_{p_{h'}V}:p_{h'}V\to p_{h''}V$，即与单边路径 $h$ 对应的算子。

类似地，设 $(V_i,x_h)$ 是箭图 $Q$ 的一个表示。从它出发，可构造路径代数 $P_Q$ 的一个表示：令 $V=\bigoplus_i V_i$，令 $p_i:V\to V_i\to V$ 为投影到 $V_i$ 的映射；对任意路径 $p=h_1\cdots h_m$，令 $a_p=x_{h_1}\cdots x_{h_m}:V_{h_m'}\to V_{h_1''}$，即将 $p$ 中各条边所对应的算子复合起来（这个算子在其他 $V_i$ 上作用为零）。

显然，上述对应 $V\mapsto(p_iV)$ 与 $(V_i)\mapsto\bigoplus_i V_i$ 互为逆。因此，代数 $P_Q$ 的表示的同构类与箭图 $Q$ 的表示的同构类之间存在双射。

**注 2.8.7。** 在实际使用中，通常按定义 2.8.3 来看待箭图表示会更方便。

最后，我们把前面介绍过的几个概念用于箭图表示。

<span class="original-page-anchor" id="pdf-page-29" aria-hidden="true"></span>

**定义 2.8.8。** 箭图 $Q$ 的表示 $(V_i,x_h)$ 的一个**子表示**，是满足下列条件的表示 $(W_i,x'_h)$：对所有 $i\in I$，都有 $W_i\subseteq V_i$；对所有 $h\in E$，都有 $x_h(W_{h'})\subseteq W_{h''}$，且 $x'_h=x_h|_{W_{h'}}:W_{h'}\longrightarrow W_{h''}$。

**定义 2.8.9。** 两个表示 $(V_i,x_h)$ 与 $(W_i,y_h)$ 的**直和**，是表示 $(V_i\oplus W_i,x_h\oplus y_h)$。

与代数表示的情形一样，箭图 $Q$ 的非零表示 $(V_i)$ 如果只有 $(0)$ 和它自身 $(V_i)$ 这两个子表示，就称为**不可约表示**；如果它不同构于两个非零表示的直和，就称为**不可分解表示**。

**定义 2.8.10。** 设 $(V_i,x_h)$ 和 $(W_i,y_h)$ 是箭图 $Q$ 的表示。箭图表示的一个**同态** $\varphi:(V_i)\longrightarrow(W_i)$，是一族映射 $\varphi_i:V_i\longrightarrow W_i$，满足对所有 $h\in E$ 都有 $y_h\circ\varphi_{h'}=\varphi_{h''}\circ x_h$。

**习题 2.8.11。** 设 $A$ 是一个 $\mathbb Z_+$ 分次代数，即 $A=\bigoplus_{n\geq0}A[n]$，且 $A[n]\cdot A[m]\subset A[n+m]$。若 $A[n]$ 是有限维的，考虑 Hilbert 级数 $h_A(t)=\sum\dim A[n]t^n$（即各个 $A[n]$ 的维数的生成函数）往往很有用。这个级数常常收敛到一个有理函数，我们也就用这个有理函数来表示结果。例如，若 $A=k[x]$，且 $\deg(x^n)=n$，则

$$
h_A(t)=1+t+t^2+\cdots+t^n+\cdots=\frac{1}{1-t}.
$$

求下列分次代数的 Hilbert 级数：

(a) $A=k[x_1,\ldots,x_m]$（按多项式的次数分次）。

(b) $A=k\langle x_1,\ldots,x_m\rangle$（按字的长度分次）。

(c) $A$ 是外代数（也称 Grassmann 代数）$\wedge_k[x_1,\ldots,x_m]$，它在某个域 $k$ 上由 $x_1,\ldots,x_m$ 生成，定义关系为：对所有 $i,j$，都有 $x_ix_j+x_jx_i=0$ 和 $x_i^2=0$（按次数分次）。

(d) $A$ 是箭图 $Q$ 的路径代数 $P_Q$（分次由 $\deg(p_i)=0$、$\deg(a_h)=1$ 定义）。

提示：闭式结果可以用 $Q$ 的邻接矩阵 $M_Q$ 表示。

<span class="original-page-anchor" id="pdf-page-30" aria-hidden="true"></span>

## 2.9 李代数

设 $\mathfrak g$ 是域 $k$ 上的向量空间，$[\ ,\ ]:\mathfrak g\times\mathfrak g\longrightarrow\mathfrak g$ 是一个反对称双线性映射。（也就是说，$[a,a]=0$，因而 $[a,b]=-[b,a]$。）

**定义 2.9.1。** 若 $[\ ,\ ]$ 满足 Jacobi 恒等式

$$
[[a,b],c]+[[b,c],a]+[[c,a],b]=0,\tag{2.9.1}
$$

则称 $(\mathfrak g,[\ ,\ ])$ 为一个 **李代数**。

**例 2.9.2。** 以下都是李代数的例子：

(1) 任意向量空间 $\mathfrak g$，配上 $[\ ,\ ]=0$（阿贝尔李代数）。

(2) 任意结合代数 $A$，配上 $[a,b]=ab-ba$。特别地，向量空间 $V$ 的自同态代数 $A=\operatorname{End}(V)$ 就是一个例子。把这样的 $A$ 看作李代数时，通常记为 $\mathfrak{gl}(V)$（一般线性李代数）。

(3) 结合代数 $A$ 的任意子空间 $U$，只要对所有 $a,b\in U$ 都有 $[a,b]\in U$。

(4) 代数 $A$ 的导子所组成的空间 $\operatorname{Der}(A)$；所谓导子，就是满足 Leibniz 法则

$$
D(ab)=D(a)b+aD(b)
$$

的线性映射 $D:A\longrightarrow A$。

(5) 李代数 $\mathfrak g$ 的任意子空间 $\mathfrak a$，只要它对交换子映射 $[\ ,\ ]$ 封闭，即 $a,b\in\mathfrak a$ 时总有 $[a,b]\in\mathfrak a$。这样的子空间称为 $\mathfrak g$ 的 **李子代数**。

**注 2.9.3。** **Ado 定理**说，任意有限维李代数都是某个 $\mathfrak{gl}(V)$ 的李子代数，其中 $V$ 是一个适当的有限维向量空间。

**注 2.9.4。** 导子之所以重要，是因为它们是自同构（即到自身的同构）的“无穷小版本”。例如，设 $g(t)$ 是 $\mathbb R$ 或 $\mathbb C$ 上的有限维代数 $A$ 的一族自同构，关于参数 $t\in(-\epsilon,\epsilon)$ 可微，且 $g(0)=\operatorname{Id}$。那么 $D:=g'(0):A\longrightarrow A$ 是一个导子（请验证！）。反过来，若 $D:A\longrightarrow A$ 是一个导子，则 $e^{tD}$ 是一族单参数自同构（请给出证明！）。

<span class="original-page-anchor" id="pdf-page-31" aria-hidden="true"></span>

这也说明了为什么要引入李代数：我们看到，结合代数的无穷小自同构（即导子）所组成的空间自然构成李代数。事实上，李代数、Hopf 代数等各种线性代数结构的导子空间，也会以同样的方式产生李代数。因此，李代数在代数学中占有十分重要的地位。

下面再给出几个更具体的李代数的例子：

(1) $\mathbb R^3$，配上 $[u,v]=u\times v$，即 $u$ 与 $v$ 的叉积。

(2) $\mathfrak{sl}(n)$，即迹为 $0$ 的所有 $n\times n$ 矩阵。

例如，$\mathfrak{sl}(2)$ 的一组基是

$$
e=\begin{pmatrix}0&1\\0&0\end{pmatrix},\qquad
f=\begin{pmatrix}0&0\\1&0\end{pmatrix},\qquad
h=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

它们满足关系

$$
[h,e]=2e,\quad[h,f]=-2f,\quad[e,f]=h.
$$

(3) 由矩阵 $\begin{pmatrix}0&*&*\\0&0&*\\0&0&0\end{pmatrix}$ 构成的 Heisenberg 李代数 $\mathcal H$。它有一组基

$$
x=\begin{pmatrix}0&0&0\\0&0&1\\0&0&0\end{pmatrix},\quad
y=\begin{pmatrix}0&1&0\\0&0&0\\0&0&0\end{pmatrix},\quad
c=\begin{pmatrix}0&0&1\\0&0&0\\0&0&0\end{pmatrix},
$$

满足关系 $[y,x]=c$ 和 $[y,c]=[x,c]=0$。

(4) 由矩阵 $\begin{pmatrix}*&*\\0&0\end{pmatrix}$ 构成的代数 $\operatorname{aff}(1)$。它的一组基为 $X=\begin{pmatrix}1&0\\0&0\end{pmatrix}$ 和 $Y=\begin{pmatrix}0&1\\0&0\end{pmatrix}$，满足 $[X,Y]=Y$。

(5) $\mathfrak{so}(n)$，即所有反对称 $n\times n$ 矩阵所组成的空间，配上 $[a,b]=ab-ba$。

**练习 2.9.5。** 证明例子 (1) 是例子 (5) 在 $n=3$ 时的特例。

**定义 2.9.6。** 设 $\mathfrak g_1,\mathfrak g_2$ 是李代数。一个 **李代数同态** $\varphi:\mathfrak g_1\longrightarrow\mathfrak g_2$，是满足 $\varphi([a,b])=[\varphi(a),\varphi(b)]$ 的线性映射。

**定义 2.9.7。** 李代数 $\mathfrak g$ 的一个**表示**，是一个向量空间 $V$，配上一个李代数同态 $\rho:\mathfrak g\longrightarrow\operatorname{End}V$。

<span class="original-page-anchor" id="pdf-page-32" aria-hidden="true"></span>

**例 2.9.8。** 以下都是李代数表示的例子：

(1) $V=0$。

(2) 任意向量空间 $V$，配上 $\rho=0$（平凡表示）。

(3) **伴随表示**：$V=\mathfrak g$，$\rho(a)(b):=[a,b]$。由公式 (2.9.1) 可知，这确实是一个表示。因此，Jacobi 恒等式的意义就在于，它等价于伴随表示的存在。

事实上，李代数 $\mathfrak g$ 的表示，与某个结合代数 $\mathcal U(\mathfrak g)$ 的表示是一回事。因此，和箭图的情形一样，我们可以把李代数的表示论看作结合代数表示论的一部分。

**定义 2.9.9。** 设 $\mathfrak g$ 是一个李代数，基为 $x_i$，括号 $[\ ,\ ]$ 由 $[x_i,x_j]=\sum_k c_{ij}^k x_k$ 给出。它的**泛包络代数** $\mathcal U(\mathfrak g)$ 是由这些 $x_i$ 生成、以 $x_ix_j-x_jx_i=\sum_k c_{ij}^k x_k$ 为定义关系的结合代数。

**注 2.9.10。** 这个定义不太理想，因为它依赖于基的选择。后面我们会给出一个不依赖于基的等价定义。

**练习 2.9.11。** 说明为什么李代数的表示与它的泛包络代数的表示是一回事。

**例 2.9.12。** 结合代数 $\mathcal U(\mathfrak{sl}(2))$ 由 $e,f,h$ 生成，满足关系

$$
he-eh=2e,\qquad hf-fh=-2f,\qquad ef-fe=h.
$$

**例 2.9.13。** 设 $\mathcal H$ 是 Heisenberg 李代数。代数 $\mathcal U(\mathcal H)$ 由 $x,y,c$ 生成，满足关系

$$
yx-xy=c,\qquad yc-cy=0,\qquad xc-cx=0.
$$

注意，Weyl 代数就是在 $\mathcal U(\mathcal H)$ 中加入关系 $c=1$ 后得到的商代数。

**注 2.9.14。** Sophus Lie（见第 2.10 节）引入李代数，是把它看作 **李群**的无穷小版本（早期文献<span class="original-page-anchor" id="pdf-page-33" aria-hidden="true"></span>中称它们为“无穷小群”，后来 Hermann Weyl 为纪念 Lie，才把它们称为李代数）。李群是一个群 $G$，同时也是流形（即局部看起来像 $\mathbb R^n$ 的拓扑空间），并且乘法运算可微。这时，可以定义 $G$ 上的光滑函数代数 $C^\infty(G)$。群 $G$ 通过右平移作用于这个代数：$(g\circ f)(x):=f(xg)$。$G$ 的李代数 $\operatorname{Lie}(G)$，由这个代数中在该作用下不变的导子组成，李括号就是导子通常的交换子。显然，这样的导子由它在单位元 $e\in G$ 处的作用决定，因此作为向量空间，$\operatorname{Lie}(G)$ 可以与 $G$ 在 $e$ 处的切空间 $T_eG$ 等同起来。

Sophus Lie 证明，对应 $G\mapsto\operatorname{Lie}(G)$ 给出了单连通李群的同构类与 $\mathbb R$ 上有限维李代数的同构类之间的一一对应。这里单连通李群是指连通的李群，其中每条闭路都能收缩到一点。这样，我们就可以通过李代数的表示来研究李群的（可微）表示。李代数是“线性”对象，而李群是“非线性”对象，因而前者更容易处理。具体而言，$G$ 的有限维表示在 $e$ 处微分，就得到 $\operatorname{Lie}(G)$ 的表示；反过来，$\operatorname{Lie}(G)$ 的有限维表示可以通过取指数得到 $G$ 的表示。此外，这个对应还能推广到某些无限维表示。

李群最重要的例子是**线性代数群**，即由代数方程定义的 $GL_n(\mathbb R)$ 的子群，例如正交矩阵群 $O_n(\mathbb R)$。

此外，给定一个李子代数 $\mathfrak g\subset\mathfrak{gl}_n(\mathbb R)$（由 Ado 定理，它可以是任意有限维实李代数），可以把 $G$ 定义为由所有 $e^X$、$X\in\mathfrak g$ 生成的 $GL_n(\mathbb R)$ 的子群。可以证明，这个群自然具有连通李群的结构，其李代数就是 $\mathfrak g$，尽管它未必是闭子群。这个群未必单连通，但它的泛覆盖 $\widetilde G$ 是单连通的；在 Lie 的对应下，$\widetilde G$ 就是与 $\mathfrak g$ 对应的李群。

关于李群及其与李代数的关系，可以进一步参阅这一主题的教材，例如 **[Ki]**。

<span class="original-page-anchor" id="pdf-page-34" aria-hidden="true"></span>

## 2.10 历史插曲：Sophus Lie 的磨难与变换

说 Sophus Lie（1842—1899）是个事事追求第一的人，恐怕还说得太轻了。1859 年，他以第一名的成绩考入挪威的 Christiania 大学（Christiania 即今天的奥斯陆），并决心也以第一名的成绩毕业。但生物课遇到的问题打乱了这个计划，Lie 毕业时只拿到了第二名。他为此情绪低落，失眠，甚至想过自杀。那时，他并不想成为数学家。他靠做数学家教维持生活，逐渐阅读了越来越多的数学著作，最终开始发表研究论文。直到 26 岁，他才决定献身数学。

挪威政府认识到，培养本国有前途的科学家，最好的办法就是让他们走出挪威，于是 Lie 获得了一笔赴欧洲游学的资助。他直奔当时欧洲数学研究的重要中心柏林，却并不欣赏当地两位明星——Weierstrass 和 Kronecker——所做的数学。在那里，Lie 遇到了年轻的 Felix Klein；Klein 对此也深有同感。两人都对直线几何感兴趣，很快成为朋友。他们的性格恰好互补。数学家 Hans Freudenthal 这样形容：“无论作为普通人还是数学家，Lie 和 Klein 的性格都很不一样：代数学家 Klein 为迷人问题的独特之处着迷；分析学家 Lie 则从特殊情形出发，力求在恰当的推广中理解一个问题。”**[16，第 323 页]**

Lie 喜欢和这位朋友切磋想法，而 Klein 的回应往往很有力。特别是，Klein 指出了 Lie 对四面体线丛的研究与交换置换群的 Galois 理论之间的类比。Lie 还浑然不知前路的困难，便热情地接受了这个建议。此后的几年里，为代数方程的 Galois 理论建立一个连续的对应理论，成了 Lie 念念不忘的目标。

<span class="original-page-anchor" id="pdf-page-35" aria-hidden="true"></span>

Lie 与 Klein 一同前往巴黎。在那里，Lie 得到了著名的接触变换，把直线映成球面。然而，当他把这套本领用到地球这个球面上时，结果却不太妙。普法战争爆发后，Lie 想不出更好的回挪威办法，只好先徒步前往意大利。他徒步时有些奇怪的习惯，比如下雨时脱掉衣服，把衣服放进背包，所以没能走出多远。法国人很快抓住了他，并搜出了满是神秘符号的稿纸。Lie 尽力解释这些数学符号的含义，却没能打消当局对他是德国间谍的怀疑。短暂的牢狱生活倒给了他一段安静的时间，让他完成了研究；回到挪威后，他顺利通过了博士论文答辩。他在挪威找不到工作，决定去瑞典，但挪威的爱国人士出面干预，国民议会以压倒性多数投票决定，在 Christiania 大学为他专设一个特聘教授职位。虽然薪水并没有什么特别优厚之处，他还是留下了。

Lie 对球面映射的研究，以及他与 Klein 的热烈交流，使两人开始思考群论与几何之间更普遍的联系。1872 年，Klein 提出了著名的爱尔兰根纲领，建议把各种具体的几何统一在射影几何的一般框架下，并用群论来组织所有几何知识。Lie 与 Klein 清楚地提出了变换群的概念，作为置换群的连续对应物；它在几何和微分方程中有着很好的应用前景，但他们还没有建立起这一领域的一般理论。爱尔兰根纲领已经暗含了这项研究的一方面——群的分类问题——但 Lie 当时还无意攻克这座堡垒。他后来写信给 Klein：“你的文章没有提出确定所有群的问题，想来是因为当时在你看来，这个问题荒谬或者不可能解决，我当时也是这样想的。”**[22，第 41—42 页]**

到 1873 年底，Lie 的悲观情绪转变为明朗得多的信心。他钻研了 Jacobi 及其追随者发展的一阶微分方程理论，并在自己念念不忘的研究目标上取得了相当<span class="original-page-anchor" id="pdf-page-36" aria-hidden="true"></span>大的进展，终于具备了回应爱尔兰根纲领的挑战、研究连续变换群理论所需的数学工具。

身处欧洲边缘，Lie 感到自己在欧洲数学界也很边缘化。他的研究没有吸引到学生，感兴趣的外国同行也寥寥无几。他用德语写论文，却几乎只在挪威期刊上发表，因为他更看重发表的速度，而不是读者的广泛程度。然而几年后，他得知一位法国数学家独立得到了 Lie 关于微分方程工作的某些特殊情形，并因此获得法国科学院的大奖。Lie 意识到，在挪威发表论文并不是宣传成果的最佳途径，他需要让欧洲更多人知道自己的工作。他带着遗憾写信给 Klein：“要是我能把所有成果收集起来，整理成稿就好了。”**[22，第 77 页]** 务实的 Klein 很快想出了办法。他当时在莱比锡任教，便安排年轻数学家 Friedrich Engel 前往 Christiania，在数学上帮助 Lie。Engel 刚刚在 Klein 的一位同事指导下获得博士学位。

Lie 和 Engel 每天会面两次，彬彬有礼地讨论变换群。据 Engel 回忆，Lie 几乎把整个理论都装在脑子里，逐章向 Engel 口述提纲，“就像一个骨架，再由我为它添上血肉”。**[22，第 77 页]** Lie 阅读并修改 Engel 的笔记，最终形成了一部书稿的初稿。

Klein 离开莱比锡去哥廷根担任教授时，安排 Lie 接任空出的几何学教席。Lie 有些不情愿地离开祖国，来到莱比锡，希望在那里建立“一个健康的数学学派”。**[22，第 226 页]** 他继续与 Engel 合作，最终共同出版了三卷本的《变换群理论》（*Theorie der Transformationsgruppen*）。

Lie 的思想开始在欧洲传播，巴黎尤其成了一片沃土。受到 Lie 的启发，Henri Poincaré 说，整个数学都是一个关于群的故事；Émile Picard 则写信给 Lie：“巴黎正在成为群论的中心；这一切都在<span class="original-page-anchor" id="pdf-page-37" aria-hidden="true"></span>年轻人的头脑里发酵，等酒液稍稍沉淀，就会酿成佳酿。”德国数学家却没有那么欣赏。Weierstrass 认为 Lie 的理论不够严谨，必须从基础重新建立；Frobenius 则称它为一套“方法的理论”，用迂回的方式解微分方程，而不采用 Euler 和 Lagrange 的自然方法。**[22，第 186、188—189 页]**

学生纷纷涌来听 Lie 讲授自己的研究，但这只加重了他在莱比锡本已繁重的教学负担——每周 8 至 10 次讲课——与他在 Christiania 悠闲的工作节奏相比，实在相差甚远。Lie 热爱户外生活，习惯了在挪威一走就是几个星期的徒步旅行，如今不禁思念故乡的森林和山脉。这些事情开始损害他的身心。最让他难受的是，他觉得自己没有得到应有的认可，并越来越认定别人剽窃了他的工作、辜负了他的信任。他和同事们的关系逐渐恶化，尤其是与他最亲近的人。他先与 Engel 决裂，最后又与 Klein 决裂。Lie 觉得自己在爱尔兰根纲领的发展中所起的作用被低估了，便公开攻击 Klein，声称：“我不是 Klein 的学生，反过来也不是，尽管后一种说法或许更接近事实。我十分看重 Klein 的才能，也永远不会忘记他一贯对我的科学研究怀有的善意和兴趣。但我认为，他对归纳与证明之间的区别、概念与概念的应用之间的区别，并没有充分的理解。”**[56，第 371 页]** 不管这场争论中谁对谁错，Lie 公开指责广受尊重而又颇有影响力的 Klein，终究损害了自己的声誉。

最后，Lie 精神崩溃，被诊断患上“神经衰弱”。这种当时常见的精神疾病，又被称为“美国式紧张”或“美国病”，病因被归结为现代城市生活的压力，以及个人“神经能量”的耗尽。Lie 在一家精神病诊所待了几个月，人们认为那里的环境压力较小；但经过一番思考，他还是觉得回到数学系更好。他的数学能力恢复了，心理状态却始终没有完全康复。关于他精神疾病的传言<span class="original-page-anchor" id="pdf-page-38" aria-hidden="true"></span>四处传播，可能还有他的对手推波助澜，借此让人不再相信他的指责。

与此同时，挪威为了确立在文化上、进而在政治上独立于瑞典的地位，开始设法召回本国杰出的知识分子。挪威国民议会投票决定，为 Lie 专设一个变换群理论教席，薪水与他在莱比锡的高薪相当。Lie 急切地想回到祖国，但他的妻子和三个孩子并没有同样的思乡之情。他终于在 1898 年回到了挪威，此时生命已只剩下几个月。

一位评论者写道，Lie“思考和写作时总是气势恢宏；这种风格如今已经过时，也不会被我们的科学期刊接受”。**[26，第 iii 页]** Lie 始终更重视原创性，而不是严谨性。他讲课时常常高呼：“让我们用概念来推理！”随后画出几何图形，而不作分析证明。**[22，第 244 页]** 他写道：“没有想象力，一个人永远成不了数学家。”“尽管我的知识和形式有所欠缺，使我能在当今数学家中占有一席之地的，是我思想的大胆。”**[56，第 409 页]** Lie 并非真的缺乏相关知识，但他的确不善于把想法整理成可以发表的形式。多亏 Engel 的勤奋，他关于变换群的研究才汇成了三大卷著作；可 Lie 始终不喜欢这部由别人代笔的作品，宁愿引用自己早先的论文。**[47，第 310 页]** 他选择助手整理接触变换和偏微分方程的成果时，运气还要更差。Felix Hausdorff 的兴趣转向了别处，Lie 在这些领域的思想也就从未得到完整阐述。**[16，第 324 页]** 因此，我们也许永远无法认识“真正的 Lie”。

## 2.11 张量积

本节回顾向量空间的张量积这一概念，后面会大量用到它。

**定义 2.11.1。** 域 $k$ 上向量空间 $V$ 和 $W$ 的**张量积** $V\otimes W$，是空间 $V*W$ 的商空间；$V*W$ 的基<span class="original-page-anchor" id="pdf-page-39" aria-hidden="true"></span>由形式符号 $v\otimes w$（$v\in V$，$w\in W$）组成，而取商所用的子空间由下列元素张成：

$$
\begin{aligned}
&(v_1+v_2)\otimes w-v_1\otimes w-v_2\otimes w,\\
&v\otimes(w_1+w_2)-v\otimes w_1-v\otimes w_2,\\
&av\otimes w-a(v\otimes w),\\
&v\otimes aw-a(v\otimes w),
\end{aligned}
$$

其中 $v\in V,w\in W,a\in k$。

**练习 2.11.2。** 证明 $V\otimes W$ 也可以等价地定义为如下商群：先取由 $v\otimes w$（$v\in V,w\in W$）生成的自由阿贝尔群 $V\bullet W$，再对由下列元素生成的子群取商：

$$
\begin{aligned}
&(v_1+v_2)\otimes w-v_1\otimes w-v_2\otimes w,\\
&v\otimes(w_1+w_2)-v\otimes w_1-v\otimes w_2,\\
&av\otimes w-v\otimes aw,
\end{aligned}
$$

其中 $v\in V,w\in W,a\in k$。

对 $v\in V,w\in W$，元素 $v\otimes w\in V\otimes W$ 称为纯张量。注意，一般来说，$V\otimes W$ 中也有不是纯张量的元素。

这样就可以定义任意多个向量空间的张量积 $V_1\otimes\cdots\otimes V_n$。张量积具有结合性，也就是说，$(V_1\otimes V_2)\otimes V_3$ 可以自然地与 $V_1\otimes(V_2\otimes V_3)$ 等同起来。

特别地，对给定的向量空间 $V$，人们常常考虑 $V^{\otimes n}=V\otimes\cdots\otimes V$（共 $n$ 个因子）；更一般地，也考虑 $E:=V^{\otimes n}\otimes(V^*)^{\otimes m}$。这个空间称为 $V$ 上的 **$(m,n)$ 型张量空间**。例如，$(0,1)$ 型张量是向量，$(1,0)$ 型张量是线性泛函（余向量），$(1,1)$ 型张量是线性算子，$(2,0)$ 型张量是双线性形式，$(2,1)$ 型张量是代数结构，等等。

若 $V$ 是有限维的，基为 $e_i$（$i=1,\ldots,N$），而 $e^i$ 是 $V^*$ 的对偶基，则 $E$ 的一组基由下列向量组成：

$$
e_{i_1}\otimes\cdots\otimes e_{i_n}\otimes e^{j_1}\otimes\cdots\otimes e^{j_m},
$$

<span class="original-page-anchor" id="pdf-page-40" aria-hidden="true"></span>

而 $E$ 中的一般元素形如

$$
\sum_{i_1,\ldots,i_n,j_1,\ldots,j_m=1}^{N}
T^{i_1\cdots i_n}_{j_1\cdots j_m}
e_{i_1}\otimes\cdots\otimes e_{i_n}\otimes e^{j_1}\otimes\cdots\otimes e^{j_m},
$$

其中 $T$ 是一个多维数表。

物理学家把张量定义为一族这样的多维数表 $T_B$：$V$ 的每一组基 $B$ 都对应一个数表，换基时，数表按照某个规则变化（请推导这个规则！）。这里必须区分上指标和下指标，因为 $T$ 的上指标对应 $V$，下指标对应 $V^*$。

**译校注：** 原书这句话把 $T$ 的上下指标所对应的空间写反了。根据上面的展开式，$T$ 的上指标 $i_1,\ldots,i_n$ 对应 $V$ 的基向量 $e_{i_1},\ldots,e_{i_n}$，下指标 $j_1,\ldots,j_m$ 对应 $V^*$ 的基向量 $e^{j_1},\ldots,e^{j_m}$；这里据此改正。

物理学家不写求和号，但约定对出现两次的指标求和，其中一次必须是上指标，另一次必须是下指标。这一约定称为 *Einstein 求和约定*，它还规定：只出现一次的指标不求和，任何指标作为上指标或作为下指标都不能出现超过一次。

也可以定义线性映射的张量积。具体而言，若 $A:V\longrightarrow V'$ 和 $B:W\longrightarrow W'$ 是线性映射，就可以用公式 $(A\otimes B)(v\otimes w)=Av\otimes Bw$ 定义线性映射 $A\otimes B:V\otimes W\longrightarrow V'\otimes W'$（请验证它是良定义的！）。下面的习题概括了张量积最重要的性质。

**习题 2.11.3。** (a) 设 $U$ 是任意 $k$ 向量空间。在双线性映射 $V\times W\longrightarrow U$ 与线性映射 $V\otimes W\longrightarrow U$ 之间建立一个自然的一一对应（“自然”是指定义这个对应时不需要选取基）。

(b) 证明：若 $\{v_i\}$ 是 $V$ 的一组基，$\{w_j\}$ 是 $W$ 的一组基，则 $\{v_i\otimes w_j\}$ 是 $V\otimes W$ 的一组基。

(c) 在 $V$ 有限维时，构造自然同构 $V^*\otimes W\longrightarrow\operatorname{Hom}(V,W)$。

(d) 设 $V$ 是域 $k$ 上的向量空间。把 $V^{\otimes n}$（$V$ 的 $n$ 重张量积）对由所有 $T-s(T)$ 张成的子空间取商，所得空间记为 $S^nV$，其中 $T\in V^{\otimes n}$，$s$ 为一个对换。再把 $V^{\otimes n}$ 对由所有满足 $s(T)=T$ 的张量 $T$ 张成的子空间取商，所得空间记为 $\wedge^nV$；这里 $s$ 可以是任意一个对换。这两个空间称为<span class="original-page-anchor" id="pdf-page-41" aria-hidden="true"></span>$V$ 的 $n$ 次**对称幂**和 $n$ 次**外幂**。若 $\{v_i\}$ 是 $V$ 的一组基，你能构造出 $S^nV$ 和 $\wedge^nV$ 的基吗？若 $\dim V=m$，它们的维数分别是多少？

(e) 若 $k$ 的特征为零，把 $S^nV$ 自然地与满足对所有对换 $s$ 都有 $T=sT$ 的张量 $T\in V^{\otimes n}$ 所组成的空间等同起来；再把 $\wedge^nV$ 自然地与满足对所有对换 $s$ 都有 $T=-sT$ 的张量 $T\in V^{\otimes n}$ 所组成的空间等同起来。

(f) 设 $A:V\longrightarrow W$ 是线性算子。我们便有算子 $A^{\otimes n}:V^{\otimes n}\longrightarrow W^{\otimes n}$，以及以显然的方式定义的对称幂和外幂 $S^nA:S^nV\longrightarrow S^nW$、$\wedge^nA:\wedge^nV\longrightarrow\wedge^nW$。假设 $V=W$，$\dim V=N$，且 $A$ 的特征值为 $\lambda_1,\ldots,\lambda_N$。求 $\operatorname{Tr}(S^nA)$ 和 $\operatorname{Tr}(\wedge^nA)$。

(g) 证明 $\wedge^N A=\det(A)\operatorname{Id}$，并利用这个等式，用一行证明 $\det(AB)=\det(A)\det(B)$。

**注 2.11.4。** 与上面类似的定义也可以用来定义张量积 $V\otimes_A W$，其中 $A$ 为任意环，$V$ 是右 $A$ 模，$W$ 是左 $A$ 模。具体而言，$V\otimes_A W$ 是一个阿贝尔群：先取由形式符号 $v\otimes w$（$v\in V$，$w\in W$）自由生成的群 $V\bullet W$，再加入下列关系取商：

$$
\begin{aligned}
&(v_1+v_2)\otimes w-v_1\otimes w-v_2\otimes w,\\
&v\otimes(w_1+w_2)-v\otimes w_1-v\otimes w_2,\\
&va\otimes w-v\otimes aw,\qquad a\in A.
\end{aligned}
$$

**练习 2.11.5。** 设 $K$ 是域，$L$ 是 $K$ 的扩域。若 $A$ 是 $K$ 上的代数，证明 $A\otimes_K L$ 自然是 $L$ 上的代数。再证明：若 $V$ 是一个 $A$ 模，则 $V\otimes_K L$ 自然具有代数 $A\otimes_K L$ 上的模结构。

**习题 2.11.6。** 本题中始终假设 $k$ 为任意域，不要求特征为零，也不要求代数闭。

若 $A$ 和 $B$ 是两个 $k$ 代数，一个 **$(A,B)$ 双模**是指一个 $k$ 向量空间 $V$，它同时具有左 $A$ 模结构和右 $B$ 模结构，且对任意 $v\in V$、$a\in A$、$b\in B$ 都满足 $(av)b=a(vb)$。注意，“左 $A$ 模”<span class="original-page-anchor" id="pdf-page-42" aria-hidden="true"></span>和“右 $A$ 模”都是双模概念的特例；具体而言，左 $A$ 模就是 $(A,k)$ 双模，右 $A$ 模就是 $(k,A)$ 双模。

设 $B$ 是 $k$ 代数，$W$ 是左 $B$ 模，$V$ 是右 $B$ 模。用 $V\otimes_B W$ 表示 $k$ 向量空间 $(V\otimes_k W)/(vb\otimes w-v\otimes bw\mid v\in V,w\in W,b\in B)$。纯张量 $v\otimes w$（其中 $v\in V$，$w\in W$）在 $V\otimes_B W$ 中的像记作 $v\otimes_B w$。（这个张量积 $V\otimes_B W$ 就是注 2.11.4 中定义的张量积。）

如果还有另一个 $k$ 代数 $A$，且 $V$ 的右 $B$ 模结构是某个 $(A,B)$ 双模结构的一部分，那么对任意 $a\in A$、$v\in V$、$w\in W$，令 $a(v\otimes_B w)=av\otimes_B w$，便使 $V\otimes_B W$ 成为左 $A$ 模。

类似地，如果 $C$ 是另一个 $k$ 代数，且 $W$ 的左 $B$ 模结构是某个 $(B,C)$ 双模结构的一部分，那么对任意 $c\in C$、$v\in V$、$w\in W$，令 $(v\otimes_B w)c=v\otimes_B wc$，便使 $V\otimes_B W$ 成为右 $C$ 模。

若 $V$ 是 $(A,B)$ 双模，$W$ 是 $(B,C)$ 双模，就可以把 $V\otimes_B W$ 上的这两种结构合成一个 $(A,C)$ 双模结构。

(a) 设 $A,B,C,D$ 是四个代数，$V$ 是 $(A,B)$ 双模，$W$ 是 $(B,C)$ 双模，$X$ 是 $(C,D)$ 双模。证明 $(V\otimes_B W)\otimes_C X\cong V\otimes_B(W\otimes_C X)$，其中同构是 $(A,D)$ 双模的同构。从左向右的同构由公式

$$
(v\otimes_B w)\otimes_C x\mapsto v\otimes_B(w\otimes_C x)
$$

给出，对所有 $v\in V$、$w\in W$、$x\in X$ 都成立。

(b) 若 $A,B,C$ 是三个代数，$V$ 是 $(A,B)$ 双模，$W$ 是 $(A,C)$ 双模，则向量空间 $\operatorname{Hom}_A(V,W)$（即从 $V$ 到 $W$ 的所有左 $A$ 线性同态所组成的空间）自然具有 $(B,C)$ 双模结构：对所有 $b\in B$、$f\in\operatorname{Hom}_A(V,W)$、$v\in V$，令 $(bf)(v)=f(vb)$；对所有 $c\in C$、$f\in\operatorname{Hom}_A(V,W)$、$v\in V$，令 $(fc)(v)=f(v)c$。

<span class="original-page-anchor" id="pdf-page-43" aria-hidden="true"></span>

设 $A,B,C,D$ 是四个代数，$V$ 是 $(B,A)$ 双模，$W$ 是 $(C,B)$ 双模，$X$ 是 $(C,D)$ 双模。证明

$$
\operatorname{Hom}_B(V,\operatorname{Hom}_C(W,X))\cong\operatorname{Hom}_C(W\otimes_B V,X)
$$

是 $(A,D)$ 双模的同构。从左向右的同构由

$$
f\mapsto(w\otimes_B v\mapsto f(v)w)
$$

给出，对所有 $v\in V$、$w\in W$ 和 $f\in\operatorname{Hom}_B(V,\operatorname{Hom}_C(W,X))$ 都成立。

**练习 2.11.7。** 证明：若 $M$ 和 $N$ 是交换环 $A$ 上的模，则 $M\otimes_A N$ 自然具有 $A$ 模结构。

## 2.12 张量代数

借助张量积，我们可以给自由代数、多项式代数、外代数以及李代数的泛包络代数下更概念化的定义，也就是不依赖于坐标的定义。

具体而言，给定域 $k$ 上的向量空间 $V$，定义它的**张量代数**为 $TV=\bigoplus_{n\geq0}V^{\otimes n}$，乘法由 $a\cdot b:=a\otimes b$ 定义，其中 $a\in V^{\otimes n}$，$b\in V^{\otimes m}$。注意，在 $V$ 中选定一组基 $x_1,\ldots,x_N$，就给出了 $TV$ 与自由代数 $k\langle x_1,\ldots,x_N\rangle$ 的同构。

**译校注：** 原书此处将自由代数的最后一个生成元写为 $x_n$，但前面选定的基为 $x_1,\ldots,x_N$；这里将下标统一为 $N$。

此外，还可以作如下定义。

**定义 2.12.1。** (i) $V$ 的**对称代数** $SV$，是 $TV$ 对由 $v\otimes w-w\otimes v$（$v,w\in V$）生成的理想取商所得的代数。

(ii) $V$ 的**外代数** $\wedge V$，是 $TV$ 对由 $v\otimes v$（$v\in V$）生成的理想取商所得的代数。

(iii) 若 $V$ 是李代数，则它的**泛包络代数** $\mathcal U(V)$，是 $TV$ 对由 $v\otimes w-w\otimes v-[v,w]$（$v,w\in V$）生成的理想取商所得的代数。

容易看出，在 $V$ 中选定一组基 $x_1,\ldots,x_N$ 后，就可以把 $SV$ 与多项式代数 $k[x_1,\ldots,x_N]$、$\wedge V$ 与外代数 $\wedge_k(x_1,\ldots,x_N)$，以及泛包络代数 $\mathcal U(V)$ 与前面定义的泛包络代数分别等同起来。

<span class="original-page-anchor" id="pdf-page-44" aria-hidden="true"></span>

此外，容易看出有分解

$$
SV=\bigoplus_{n\geq0}S^nV,\qquad\wedge V=\bigoplus_{n\geq0}\wedge^nV.
$$

## 2.13 希尔伯特第三问题

**习题 2.13.1。** 已知：若 $A$ 和 $B$ 是两个面积相等的多边形，就可以用有限次直线切割把 $A$ 分成若干块，再用这些块拼成 $B$（请验证——这很有趣！）。David Hilbert 在 1900 年问道：对于三维空间中的多面体，这个结论是否也成立？特别地，体积相同的立方体和正四面体是否能这样分割、拼合？

Dehn 在 1901 年发现，答案是“不能”。证明十分漂亮。给任意多面体 $A$ 配上空间 $V=\mathbb R\otimes(\mathbb R/\mathbb Q)$ 中的“Dehn 不变量” $D(A)$；这里取的是 $\mathbb Q$ 向量空间的张量积。具体定义为

$$
D(A)=\sum_a l(a)\otimes\frac{\beta(a)}{\pi},
$$

其中 $a$ 遍历 $A$ 的所有棱，$l(a)$ 和 $\beta(a)$ 分别是棱 $a$ 的长度及该棱处的二面角。

(a) 证明：若用一次平面切割把 $A$ 分成 $B$ 和 $C$，则 $D(A)=D(B)+D(C)$。

(b) 证明 $\alpha=\arccos(1/3)/\pi$ 不是有理数。

提示：假设 $\alpha=2m/n$，其中 $m,n$ 为整数。推得方程 $x+x^{-1}=2/3$ 的根是 $n$ 次单位根。然后证明 $x^k+x^{-k}$ 的分母是 $3^k$，从而得到矛盾。

(c) 利用 (a)、(b)，证明 Hilbert 问题的答案是否定的。（计算正四面体和立方体的 Dehn 不变量。）

## 2.14 李代数表示的张量积与对偶

**定义 2.14.1。** 李代数 $\mathfrak g$ 的两个表示 $V,W$ 的**张量积**，是空间 $V\otimes W$，配上

$$
\rho_{V\otimes W}(x)=\rho_V(x)\otimes\operatorname{Id}+\operatorname{Id}\otimes\rho_W(x).
$$

<span class="original-page-anchor" id="pdf-page-45" aria-hidden="true"></span>

**定义 2.14.2。** 李代数 $\mathfrak g$ 的表示 $V$ 的**对偶表示** $V^*$，是 $V$ 的对偶空间 $V^*$，配上 $\rho_{V^*}(x)=-\rho_V(x)^*$。

容易验证，它们确实都是表示。

**习题 2.14.3。** 设 $V,W,U$ 是李代数 $\mathfrak g$ 的有限维表示。证明空间 $\operatorname{Hom}_{\mathfrak g}(V\otimes W,U)$ 与 $\operatorname{Hom}_{\mathfrak g}(V,U\otimes W^*)$ 同构。（这里 $\operatorname{Hom}_{\mathfrak g}:=\operatorname{Hom}_{\mathcal U(\mathfrak g)}$。）

## 2.15 $\mathfrak{sl}(2)$ 的表示

本节研究 $\mathfrak{sl}(2)$ 的表示论，它在数学的许多领域都占有核心地位。通过下面这一系列练习来学习这个主题很有帮助，每位数学家都应该以某种形式做过这些练习。

**习题 2.15.1。** 根据前面的讨论，$\mathfrak{sl}(2)$ 的表示就是一个向量空间 $V$，配上三个算子 $E,F,H$，满足 $HE-EH=2E$、$HF-FH=-2F$、$EF-FE=H$（对应的映射 $\rho$ 由 $\rho(e)=E,\rho(f)=F,\rho(h)=H$ 给出）。

设 $V$ 是 $\mathfrak{sl}(2)$ 的有限维表示（本题的基域为 $\mathbb C$）。

(a) 在 $H$ 的特征值中选取一个实部最大的，记为 $\lambda$。设 $\overline V(\lambda)$ 是与 $\lambda$ 对应的广义特征空间。证明 $E|_{\overline V(\lambda)}=0$。

(b) 设 $W$ 是 $\mathfrak{sl}(2)$ 的任意表示，$w\in W$ 是满足 $Ew=0$ 的非零向量。对任意 $k>0$，求一个 $k$ 次多项式 $P_k(x)$，使得 $E^kF^kw=P_k(H)w$。（先计算 $EF^kw$，再对 $k$ 用归纳法。）

(c) 设 $v\in\overline V(\lambda)$ 是 $H$ 对应于特征值 $\lambda$ 的广义特征向量。证明存在 $N>0$，使 $F^Nv=0$。

(d) 证明 $H$ 在 $\overline V(\lambda)$ 上可对角化。（选取 $N$，使得 $F^N$ 在 $\overline V(\lambda)$ 上为零，再利用 (b) 计算 $E^NF^Nv$，其中 $v\in\overline V(\lambda)$。利用 $P_k(x)$ 没有重根这一事实。）

(e) 设 $N_v$ 是满足 (c) 的最小 $N$。证明 $\lambda=N_v-1$。

<span class="original-page-anchor" id="pdf-page-46" aria-hidden="true"></span>

(f) 证明：对每个 $N>0$，$\mathfrak{sl}(2)$ 都有一个 $N$ 维不可约表示，且在同构意义下唯一。选取适当的基，计算这个表示中的矩阵 $E,F,H$。（若 $V$ 是有限维不可约表示，按 (a) 选取 $\lambda$，再取 $H$ 的一个特征向量 $v\in V(\lambda)$。证明 $v,Fv,\ldots,F^\lambda v$ 是 $V$ 的一组基，并计算算子 $E,F,H$ 在这组基下的矩阵。）

把 (f) 中的 $(\lambda+1)$ 维不可约表示记为 $V_\lambda$。下面将证明，任意有限维表示都是一些 $V_\lambda$ 的直和。

(g) 证明算子 $C=EF+FE+H^2/2$（称为 **Casimir 算子**）与 $E,F,H$ 交换，且它在 $V_\lambda$ 上等于 $\frac{\lambda(\lambda+2)}{2}\operatorname{Id}$。

现在很容易证明上述直和分解。反设结论不成立，取一个维数最小的可约表示 $V$，它不能分解为较小表示的直和。

(h) 证明 $C$ 在 $V$ 上只有一个特征值，即某个非负整数 $\lambda$ 对应的 $\frac{\lambda(\lambda+2)}{2}$（利用 $C$ 的广义特征空间分解一定也是表示的分解这一事实）。

(i) 证明 $V$ 有一个子表示 $W=V_\lambda$，使得对某个 $n$ 有 $V/W=nV_\lambda$（利用 (h)，以及 $V$ 是不能分解的可约表示中维数最小的这一事实）。

(j) 由 (i) 推出，$H$ 的特征空间 $V(\lambda)$ 的维数为 $n+1$。若 $v_1,\ldots,v_{n+1}$ 是它的一组基，证明向量 $F^jv_i$（$1\leq i\leq n+1$，$0\leq j\leq\lambda$）线性无关，因而构成 $V$ 的一组基（证明：若 $x\ne0$，$Fx=0$，$Hx=\mu x$，则 $Cx=\frac{\mu(\mu-2)}{2}x$，从而 $\mu=-\lambda$）。

(k) 定义 $W_i=\operatorname{span}(v_i,Fv_i,\ldots,F^\lambda v_i)$。证明这些 $W_i$ 都是 $V$ 的子表示，并推出矛盾，因为 $V$ 不能分解。

(l)（Jacobson–Morozov 引理）设 $V$ 是有限维复向量空间，$A:V\longrightarrow V$ 是幂零算子。证明在同构意义下存在唯一的 $\mathfrak{sl}(2)$ 表示，<span class="original-page-anchor" id="pdf-page-47" aria-hidden="true"></span>作用在 $V$ 上，且满足 $E=A$。（利用表示的分类和若尔当标准形定理。）

(m)（Clebsch–Gordan 分解）把 $\mathfrak{sl}(2)$ 的表示 $V_\lambda\otimes V_\mu$ 分解为不可约分量。

提示：对于 $\mathfrak{sl}(2)$ 的有限维表示 $V$，引入特征标 $\chi_V(x)=\operatorname{Tr}(e^{xH})$（$x\in\mathbb C$）很有用。证明 $\chi_{V\oplus W}(x)=\chi_V(x)+\chi_W(x)$，且 $\chi_{V\otimes W}(x)=\chi_V(x)\chi_W(x)$。然后计算 $V_\lambda$ 和 $V_\lambda\otimes V_\mu$ 的特征标，从中得出所求分解。这个分解在量子力学中有着根本的重要性。

(n) 设 $V=\mathbb C^M\otimes\mathbb C^N$，$A=J_{0,M}\otimes\operatorname{Id}_N+\operatorname{Id}_M\otimes J_{0,N}$，其中 $J_{0,n}$ 是特征值为零、大小为 $n$ 的若尔当块（即 $J_{0,n}e_i=e_{i-1}$，$i=2,\ldots,n$，且 $J_{0,n}e_1=0$）。利用 (l) 和 (m)，求 $A$ 的若尔当标准形。

## 2.16 关于李代数的习题

**习题 2.16.1（李定理）。** 李代数 $\mathfrak g$ 的**导出代数** $K(\mathfrak g)$，是所有元素 $[x,y]$（$x,y\in\mathfrak g$）的线性张成。它是 $\mathfrak g$ 的一个理想，也就是伴随表示的一个子表示。域 $k$ 上的有限维李代数 $\mathfrak g$，如果存在 $n$ 使 $K^n(\mathfrak g)=0$，就称为**可解李代数**。证明李定理：若 $k=\mathbb C$，$V$ 是可解李代数 $\mathfrak g$ 的有限维不可约表示，则 $V$ 是一维的。

提示：对维数用归纳法。根据归纳假设，$K(\mathfrak g)$ 在 $V$ 中有一个公共特征向量 $v$；也就是说，存在一个线性函数 $\chi:K(\mathfrak g)\longrightarrow\mathbb C$，使得对任意 $a\in K(\mathfrak g)$ 都有 $av=\chi(a)v$。证明 $\mathfrak g$ 保持 $K(\mathfrak g)$ 的公共特征空间。（为此，需要证明对 $x\in\mathfrak g$、$a\in K(\mathfrak g)$ 都有 $\chi([x,a])=0$。考虑包含 $v$ 且在 $x$ 作用下不变的最小子空间 $U$。这个子空间在 $K(\mathfrak g)$ 作用下也不变，并且任意 $a\in K(\mathfrak g)$ 在它上面作用的迹为 $\dim(U)\chi(a)$。特别地，$0=\operatorname{Tr}([x,a])=\dim(U)\chi([x,a])$。）

<span class="original-page-anchor" id="pdf-page-48" aria-hidden="true"></span>

**习题 2.16.2。** 对基为 $X,Y$、交换关系为 $[X,Y]=Y$ 的二维李代数，分类其有限维不可约表示。分别考虑特征为零和正特征的情形。李定理在正特征下还成立吗？

**习题 2.16.3。**（难！）对李代数 $\mathfrak g$ 的任意元素 $x$，用 $\operatorname{ad}(x)$ 表示算子 $\mathfrak g\longrightarrow\mathfrak g$、$y\mapsto[x,y]$。考虑由两个元素 $x,y$ 生成、定义关系为 $\operatorname{ad}(x)^2(y)=\operatorname{ad}(y)^{n+1}(x)=0$ 的李代数 $\mathfrak g_n$。

(a) 证明李代数 $\mathfrak g_1,\mathfrak g_2,\mathfrak g_3$ 都是有限维的，并求出它们的维数。

(b)（更难！）证明李代数 $\mathfrak g_4$ 是无限维的。显式构造这个代数的一组基。

**习题 2.16.4。** 在特征 $p>2$ 的代数闭域 $k$ 上，分类李代数 $\mathfrak{sl}(2)$ 的不可约表示。

**习题 2.16.5。** 设 $k$ 是特征为零的代数闭域，$q\in k^\times$，且 $q\ne\pm1$。**量子包络代数** $\mathcal U_q(\mathfrak{sl}(2))$ 由 $e,f,K,K^{-1}$ 生成，满足关系

$$
KeK^{-1}=q^2e,\qquad KfK^{-1}=q^{-2}f,\qquad[e,f]=\frac{K-K^{-1}}{q-q^{-1}}
$$

（若形式地令 $K=q^h$，就会看到，当 $q\longrightarrow1$ 时，这个代数在适当的意义下“退化”为 $\mathcal U(\mathfrak{sl}(2))$）。分类 $\mathcal U_q(\mathfrak{sl}(2))$ 的不可约表示。分别考虑 $q$ 是单位根和不是单位根的情形。
