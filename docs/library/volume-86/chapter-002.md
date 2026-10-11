---
title: "第二章 环"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第一章 群","link":"/library/volume-86/chapter-001"}
next: {"text":"第三章 模","link":"/library/volume-86/chapter-003"}
---

# 第二章 环

<span class="original-page-anchor" id="pdf-page-98" aria-hidden="true"></span>

### §1. 环与同态

**环** $A$ 是一个集合，其上有两种合成法则，分别称为乘法和加法，分别写成积与和，并满足以下条件：

**RI 1.** 关于加法，$A$ 是交换群。

**RI 2.** 乘法满足结合律，并有单位元。

**RI 3.** 对所有 $x,y,z\in A$，有

$$
(x+y)z=xz+yz\qquad\text{以及}\qquad z(x+y)=zx+zy.
$$

（这称为**分配律**。）

和往常一样，我们用 $0$ 表示加法单位元，用 $1$ 表示乘法单位元。我们不假定 $1\ne0$。注意，对所有 $x\in A$，都有 $0x=0$。*证明：* 有 $0x+x=(0+1)x=1x=x$，所以 $0x=0$。特别地，若 $1=0$，则 $A$ 仅由 $0$ 组成。

对任意 $x,y\in A$，有 $(-x)y=-(xy)$。*证明：* 有

$$
xy+(-x)y=(x+(-x))y=0y=0,
$$

所以 $(-x)y$ 是 $xy$ 的加法逆元。

其他把加法和乘法联系起来的通常法则也容易证明，例如 $(-x)(-y)=xy$。我们把这些留作练习。

设 $A$ 为环，$U$ 为 $A$ 中同时有右逆元和左逆元的元素组成的集合。则 $U$ 是乘法群。事实上，若 $a$ 有一个<span class="original-page-anchor" id="pdf-page-99" aria-hidden="true"></span>右逆元 $b$，即 $ab=1$，又有一个左逆元 $c$，即 $ca=1$，则 $cab=b$，从而 $c=b$。由此可见，$c$（或 $b$）是一个双侧逆元，且 $c$ 本身也有双侧逆元，就是 $a$。因此 $U$ 满足乘法群的全部公理，称为 $A$ 的**可逆元群**。它有时记作 $A^*$，也称为 $A$ 的**可逆元素群**。若环 $A$ 满足 $1\ne0$，且每个非零元素都可逆，则称 $A$ 为**除环**。

**注。** 环中*左*可逆的元素未必构成群。

**例（移位算子）。** 设 $E$ 为所有整数序列

$$
a=(a_1,a_2,a_3,\ldots)
$$

组成的集合。可按分量定义加法。设 $R$ 为 $E$ 到自身的所有满足 $f(a+b)=f(a)+f(b)$ 的映射 $f:E\to E$ 组成的集合，合成法则定义为映射的复合。则 $R$ 是环。（证明？）令

$$
T(a_1,a_2,a_3,\ldots)=(0,a_1,a_2,a_3,\ldots).
$$

验证 $T$ 左可逆但不右可逆。

若对所有 $x,y\in A$ 都有 $xy=yx$，则称环 $A$ 为**交换环**。交换除环称为**域**。注意，由定义可知，域至少包含两个元素，即 $0$ 和 $1$。

若环 $A$ 的子集 $B$ 是加法子群，包含乘法单位元，且 $x,y\in B$ 蕴含 $xy\in B$，则称 $B$ 为**子环**。此时 $B$ 本身也是环，$B$ 中的运算法则与 $A$ 中的相同。

例如，环 $A$ 的**中心**是 $A$ 的一个子集，由所有对任意 $x\in A$ 都满足 $ax=xa$ 的元素 $a\in A$ 组成。立即可见，$A$ 的中心是子环。

正如我们由三个因子的结合律证明一般结合律一样，也可以证明一般分配律。若 $x,y_1,\ldots,y_n$ 是环 $A$ 中的元素，则用归纳法可得

$$
x(y_1+\cdots+y_n)=xy_1+\cdots+xy_n.
$$

若 $x_i$（$i=1,\ldots,n$）和 $y_j$（$j=1,\ldots,m$）是 $A$ 中的元素，则也容易证明

$$
\left(\sum_{i=1}^n x_i\right)\left(\sum_{j=1}^m y_j\right)=\sum_{i=1}^n\sum_{j=1}^m x_i y_j.
$$

此外，分配律对减法也成立，例如

$$
x(y_1-y_2)=xy_1-xy_2.
$$

所有证明均留给读者。

<span class="original-page-anchor" id="pdf-page-100" aria-hidden="true"></span>

**例。** *设 $S$ 为集合，$A$ 为环。设 $\operatorname{Map}(S,A)$ 为 $S$ 到 $A$ 的所有映射组成的集合。若对 $f,g\in\operatorname{Map}(S,A)$ 定义*

$$
(fg)(x)=f(x)g(x)\qquad\text{以及}\qquad(f+g)(x)=f(x)+g(x)
$$

*对所有 $x\in S$ 成立，则 $\operatorname{Map}(S,A)$ 是环。* 乘法单位元是值为 $A$ 的乘法单位元的常值映射；加法单位元是值为 $A$ 的加法单位元（即 $0$）的常值映射。验证 $\operatorname{Map}(S,A)$ 在上述合成法则下构成环是显然的，留给读者。

设 $M$ 为加法阿贝尔群，$A$ 为 $M$ 到自身的所有群同态组成的集合 $\operatorname{End}(M)$。我们把 $A$ 中的加法定义为映射的相加，把乘法定义为映射的**复合**。容易验证 $A$ 是环。它的单位元当然是恒等映射。一般而言，$A$ 不是交换环。

读者以前无疑见过域上的多项式。它们给出了环的一个基本例子，本书将在 §3 正式定义它们。

设 $K$ 为域。元素属于 $K$ 的所有 $n\times n$ 矩阵组成一个环。其可逆元正是可逆矩阵，等价地说，就是行列式非零的矩阵。

设 $S$ 为集合，$R$ 为 $S$ 上所有实值函数组成的集合。则 $R$ 是交换环。其可逆元正是处处不为 $0$ 的函数。这是上面所讨论的环 $\operatorname{Map}(S,A)$ 的一个特例。

**卷积积。** 现在给出一些环的例子，其中的乘法由所谓的卷积给出。设 $G$ 为群，$K$ 为域。用 $K[G]$ 表示所有形式线性组合 $\alpha=\sum a_x x$ 组成的集合，其中 $x\in G$，$a_x\in K$，且除有限多个 $a_x$ 外，其余均等于 $0$。（见 §3，以及第三章 §4。）若 $\beta=\sum b_x x\in K[G]$，则可定义乘积

$$
\alpha\beta=\sum_{x\in G}\sum_{y\in G}a_x b_y xy=\sum_{z\in G}\left(\sum_{xy=z}a_x b_y\right)z.
$$

在这一乘法下，**群环** $K[G]$ 是一个环；第十八章将对有限群 $G$ 的情形作深入研究。注意，$K[G]$ 是交换环当且仅当 $G$ 是交换群。上式右侧的第二个求和定义了所谓的**卷积积**。若 $f,g$ 是群 $G$ 上的两个函数，则把它们的**卷积** $f*g$ 定义为

$$
(f*g)(z)=\sum_{xy=z}f(x)g(y).
$$

当然，这个式子必须有意义。若 $G$ 是无限群，可以把这个定义限制于仅在有限多个元素处不为 $0$ 的函数。习题 12 将给出一个例子（实际上是在幺半群上），其中另一种限制使右侧的求和成为有限和。

**来自分析的例子。** 在分析中，人们考虑如下情形。设 $L^1=L^1(\mathbf R)$ 为绝对可积函数组成的空间。

<span class="original-page-anchor" id="pdf-page-101" aria-hidden="true"></span>

给定函数 $f,g\in L^1$，定义其**卷积积** $f*g$ 为

$$
(f*g)(x)=\int_{\mathbf R}f(x-y)g(y)\,dy.
$$

这一乘法满足环的全部公理，唯独没有单位元。在群环或习题 12 的卷积的情形中，存在单位元。（它是什么？）注意，$L^1(\mathbf R)$ 中的卷积积是交换的，其根本原因是 $\mathbf R$ 是交换的加法群。更一般地，设 $G$ 为具有 Haar 测度 $\mu$ 的局部紧群，则用类似公式定义卷积积：

$$
(f*g)(x)=\int_G f(xy^{-1})g(y)\,d\mu(y).
$$

给出这些例子后，我们回到环的一般理论。

环 $A$ 中的**左理想** $\mathfrak a$ 是 $A$ 的子集，它是 $A$ 的加法群的子群，且满足 $A\mathfrak a\subset\mathfrak a$（因 $A$ 包含 $1$，从而 $A\mathfrak a=\mathfrak a$）。定义右理想时，我们要求 $\mathfrak a A=\mathfrak a$；**双侧理想**则是既为左理想又为右理想的子集。本节把双侧理想简称为**理想**。注意，$(0)$ 和 $A$ 本身都是理想。

若 $A$ 为环，$a\in A$，则 $Aa$ 是左理想，称为**主**左理想。我们称 $a$ 为 $\mathfrak a$（在 $A$ 上）的一个生成元。类似地，若把 $AaA$ 定义为所有 $\sum x_i a y_i$（其中 $x_i,y_i\in A$）组成的集合，则 $AaA$ 是主双侧理想。参见下文关于理想乘积的定义。更一般地，设 $a_1,\ldots,a_n$ 为 $A$ 的元素。我们用 $(a_1,\ldots,a_n)$ 表示 $A$ 中所有可以写成如下形式的元素组成的集合：

$$
x_1 a_1+\cdots+x_n a_n\qquad\text{其中}\quad x_i\in A.
$$

立即可以验证，这个集合是左理想，而 $a_1,\ldots,a_n$ 称为此左理想的**生成元**。

若 $\{\mathfrak a_i\}_{i\in I}$ 是一族理想，则其交

$$
\bigcap_{i\in I}\mathfrak a_i
$$

也是理想。对左理想同样如此。读者容易验证，若 $\mathfrak a=(a_1,\ldots,a_n)$，则 $\mathfrak a$ 是包含元素 $a_1,\ldots,a_n$ 的所有左理想的交。

若对所有 $x,y\in A$ 都有 $xy=yx$，则称环 $A$ 为**交换环**。此时每个左理想或右理想都是双侧理想。

每个理想都是主理想且满足 $1\ne0$ 的**交换**环称为**主理想环**。

**例。** 整数 $\mathbf Z$ 组成一个交换环。设 $\mathfrak a$ 为不等于 $\mathbf Z$ 且不等于 $0$ 的理想。若 $n\in\mathfrak a$，则 $-n\in\mathfrak a$。设 $d$ 为 $\mathfrak a$ 中最小的正整数。若 $n\in\mathfrak a$，则存在整数 $q,r$，满足 $0\le r<d$，使得

$$
n=dq+r.
$$

<span class="original-page-anchor" id="pdf-page-102" aria-hidden="true"></span>

由于 $\mathfrak a$ 是理想，$r$ 属于 $\mathfrak a$，从而 $r=0$。所以 $\mathfrak a$ 由 $d$ 的所有倍数 $qd$（$q\in\mathbf Z$）组成，故 *$\mathbf Z$ 是主理想环*。

类似的例子是域上的一元多项式环；第四章将同样利用欧几里得算法证明这一点。

设 $R$ 为数域 $K$ 中的代数整数环。（定义见第七章。）$R$ 未必是主理想环。但设 $\mathfrak p$ 为素理想，并设 $R_{\mathfrak p}$ 为所有 $a/b$（其中 $a,b\in R$ 且 $b\notin\mathfrak p$）组成的环。代数数论证明，$R_{\mathfrak p}$ 是主理想环，具有一个素理想 $\mathfrak m_{\mathfrak p}$；这个理想由上述形式且 $a\in\mathfrak p$ 的所有元素 $a/b$ 组成。见习题 15、16 和 17。

**来自分析的一个例子。** 设 $A$ 为复平面上所有整函数组成的集合。则 $A$ 是交换环，每个有限生成理想都是主理想。给定复数的离散集合 $\{z_i\}$ 和整数 $m_i\ge0$，存在一个整函数 $f$，它在 $z_i$ 处有重数为 $m_i$ 的零点，且没有其他零点。每个主理想都具有 $Af$ 的形式，其中 $f$ 是这样的函数。$A$ 的可逆元群 $A^*$ 由无零点的函数组成。利用 Weierstrass 分解定理证明上述结论，是分析中的一个很好的练习。

现在回到一般概念。设 $\mathfrak a,\mathfrak b$ 为 $A$ 的理想。把 $\mathfrak a\mathfrak b$ 定义为所有如下的和组成的集合：

$$
x_1 y_1+\cdots+x_n y_n,
$$

其中 $x_i\in\mathfrak a$，$y_i\in\mathfrak b$。立即可验证，$\mathfrak a\mathfrak b$ 是理想，而理想的集合构成乘法幺半群，其单位元为环本身。这个单位元称为**单位理想**，常记作 $(1)$。若 $\mathfrak a,\mathfrak b$ 为左理想，则仍按上述方式定义它们的乘积 $\mathfrak a\mathfrak b$。它也是左理想；若 $\mathfrak a,\mathfrak b,\mathfrak c$ 为左理想，则仍有结合律：$(\mathfrak a\mathfrak b)\mathfrak c=\mathfrak a(\mathfrak b\mathfrak c)$。

若 $\mathfrak a,\mathfrak b$ 为 $A$ 的左理想，则 $\mathfrak a+\mathfrak b$（这里的和作为 $A$ 的加法子群来取）显然是左理想。对右理想和双侧理想同样如此。因此，理想在加法下也构成幺半群。还有分配律：若 $\mathfrak a_1,\ldots,\mathfrak a_n,\mathfrak b$ 为 $A$ 的理想，则显然

$$
\mathfrak b(\mathfrak a_1+\cdots+\mathfrak a_n)=\mathfrak b\mathfrak a_1+\cdots+\mathfrak b\mathfrak a_n,
$$

另一侧也有类似等式。（不过，理想的集合并不构成环！）

设 $\mathfrak a$ 为左理想。把 $\mathfrak a A$ 定义为所有 $a_1 x_1+\cdots+a_n x_n$（其中 $a_i\in\mathfrak a$，$x_i\in A$）组成的集合。则 $\mathfrak a A$ 是（双侧）理想。

假定 $A$ 是交换环，$\mathfrak a,\mathfrak b$ 为理想。显然

$$
\mathfrak a\mathfrak b\subset\mathfrak a\cap\mathfrak b,
$$

但等号未必成立。不过，请作为练习证明：若 $\mathfrak a+\mathfrak b=A$，则 $\mathfrak a\mathfrak b=\mathfrak a\cap\mathfrak b$。

读者应当知道，除每个理想都是主理想之外，整数 $\mathbf Z$ 还具有另一个性质，即唯一素因数分解。

<span class="original-page-anchor" id="pdf-page-103" aria-hidden="true"></span>

我们将在 §4 讨论这个一般现象。这里只指出：若环 $A$ 具有唯一素元分解性质，且 $p$ 是素元，则理想 $(p)$ 是素理想，上述定义的环 $R_{(p)}$ 是主理想环。见习题 6。因此，可以从非主理想环自然地得到主理想环。

正如 Dedekind 所发现的，在某些情况下，可以把唯一素元分解替换为（非零）理想的唯一素理想分解，从而恢复某种形式的唯一分解。

**例。** 某些情况下，非零理想可以产生一个群。设 $\mathfrak o$ 为域 $K$ 的子环，且 $K$ 的每个元素都是 $\mathfrak o$ 中元素的商，即形如 $a/b$，其中 $a,b\in\mathfrak o$，$b\ne0$。所谓**分式理想** $\mathfrak a$，是指 $K$ 的非零加法子群，满足 $\mathfrak o\mathfrak a\subset\mathfrak a$（因 $\mathfrak o$ 包含单位元，所以 $\mathfrak o\mathfrak a=\mathfrak a$），并且存在元素 $c\in\mathfrak o$，$c\ne0$，使 $c\mathfrak a\subset\mathfrak o$。可以说，分式理想具有有界分母。若上述环 $\mathfrak o$ 的分式理想在乘法下构成群，则称它为 **Dedekind 环**。代数数论的书籍证明，数域中的代数整数环是 Dedekind 环。完成习题 14 可得到唯一素理想分解性质。第七章习题 7 给出了这一证明的概要。

若 $a\in K$，$a\ne0$，则 $\mathfrak o a$ 是分式理想，这样的理想称为**主**分式理想。主分式理想构成一个子群。商群称为 $\mathfrak o$ 的**理想类群**或 **Picard 群**，记作 $\operatorname{Pic}(\mathfrak o)$。关于 Dedekind 环的一些初等事实，见习题 13–19。对代数数论和函数论中出现的各种 Dedekind 环，确定 $\operatorname{Pic}(\mathfrak o)$ 是一个基本问题。数域中这一理论的初步内容可参见拙著《Algebraic Number Theory》。在函数论的情形中，这会引向代数几何的问题，特别是代数簇上除子类群的研究及其带来的所有相关问题。分式理想构成群这一性质，在本质上与环具有“维数 1”有关（这里不作定义）。一般地，这将引向各种等价关系下模的研究；例如参见第三章 §4 末尾的评述。

我们回到环的一般理论。

所谓**环同态**，是指映射 $f:A\to B$，其中 $A,B$ 为环，且 $f$ 关于 $A$ 和 $B$ 的乘法结构是幺半群同态，关于加法结构也是幺半群同态。换言之，$f$ 必须满足：

$$
\begin{aligned}
f(a+a')&=f(a)+f(a'),& f(aa')&=f(a)f(a'),\\
f(1)&=1,& f(0)&=0,
\end{aligned}
$$

对所有 $a,a'\in A$ 成立。它的**核**定义为把 $f$ 看作加法同态时的核。

<span class="original-page-anchor" id="pdf-page-104" aria-hidden="true"></span>

*环同态 $f:A\to B$ 的核是 $A$ 的理想，*这立即可以验证。

反过来，设 $\mathfrak a$ 为环 $A$ 的理想。我们可以如下构造**商环** $A/\mathfrak a$。把 $A$ 和 $\mathfrak a$ 看作加法群，令 $A/\mathfrak a$ 为商群。在 $A/\mathfrak a$ 上定义乘法合成法则：若 $x+\mathfrak a$ 和 $y+\mathfrak a$ 为 $\mathfrak a$ 的两个陪集，则把 $(x+\mathfrak a)(y+\mathfrak a)$ 定义为陪集 $(xy+\mathfrak a)$。这个陪集是良定义的，因为若 $x_1,y_1$ 分别与 $x,y$ 属于同一个陪集，则立即可验证 $x_1 y_1$ 与 $xy$ 属于同一个陪集。于是，我们的乘法合成法则显然满足结合律，具有单位元（即陪集 $1+\mathfrak a$），并满足分配律，因为陪集代表元满足分配律。因此，我们在 $A/\mathfrak a$ 上定义了一个环结构，而典范映射

$$
f:A\to A/\mathfrak a
$$

显然是环同态。

*若 $g:A\to A'$ 为核包含 $\mathfrak a$ 的环同态，则存在唯一的环同态 $g_*:A/\mathfrak a\to A'$，使下图交换：*

$$
\begin{array}{ccc}
A&\xrightarrow{g}&A'\\
{}_{f}\searrow&&\nearrow_{g_*}\\
&A/\mathfrak a&
\end{array}
$$

事实上，把 $f,g$ 看作关于加法结构的群同态，则存在唯一的群同态 $g_*$ 使此图交换。我们断言，$g_*$ 实际上是环同态。这个显然的证明本可留给读者，但我们仍完整地给出。若 $x\in A$，则 $g(x)=g_* f(x)$。因此，对 $x,y\in A$，

$$
\begin{aligned}
g_*(f(x)f(y))&=g_*(f(xy))=g(xy)=g(x)g(y)\\
&=g_* f(x)g_* f(y).
\end{aligned}
$$

给定 $\xi,\eta\in A/\mathfrak a$，存在 $x,y\in A$ 使 $\xi=f(x)$，$\eta=f(y)$。因 $f(1)=1$，可得 $g_* f(1)=g(1)=1$，故 $g_*$ 为乘法幺半群同态的两个条件均成立，得证。

刚刚证明的结论等价于说：典范映射 $f:A\to A/\mathfrak a$ 在核包含 $\mathfrak a$ 的同态所构成的范畴中具有泛性质。

设 $A$ 为环，暂且用 $e$ 表示其单位元。映射

$$
\lambda:\mathbf Z\to A
$$

由 $\lambda(n)=ne$ 给出，显然是环同态，其核为由某个整数 $n\ge0$ 生成的理想 $(n)$。我们有典范的单射同态 $\mathbf Z/n\mathbf Z\to A$，它给出 $\mathbf Z/n\mathbf Z$ 与 $A$ 的一个<span class="original-page-anchor" id="pdf-page-105" aria-hidden="true"></span>子环之间的（环）同构。若 $n\mathbf Z$ 是素理想，则 $n=0$，或者 $n=p$，其中 $p$ 为某个素数。第一种情况下，$A$ 包含一个与 $\mathbf Z$ 同构的子环，常把这个子环与 $\mathbf Z$ 等同。此时称 $A$ 的**特征**为 $0$。另一方面，若 $n=p$，则称 $A$ 的**特征**为 $p$，而 $A$ 包含 $\mathbf Z/p\mathbf Z$（的一个同构像）作为子环。我们把 $\mathbf Z/p\mathbf Z$ 简记作 $\mathbf F_p$。

若 $K$ 为域，则 $K$ 的特征为 $0$ 或 $p>0$。第一种情况下，$K$ 包含有理数域的一个同构像作为子域；第二种情况下，它包含 $\mathbf F_p$ 的一个同构像。无论哪种情况，这个子域都称为（包含于 $K$ 的）**素域**。由于这个素域是 $K$ 中包含 $1$ 的最小子域，且除恒等自同构外没有其他自同构，习惯上依情形把它与 $\mathbf Q$ 或 $\mathbf F_p$ 等同。所谓（$K$ 中的）**素环**，是指：$K$ 的特征为 $0$ 时的整数环 $\mathbf Z$，或 $K$ 的特征为 $p$ 时的 $\mathbf F_p$。

设 $A$ 为环 $B$ 的子环，$S$ 为 $B$ 的一个与 $A$ 交换的子集；换言之，对所有 $a\in A$ 和 $s\in S$，都有 $as=sa$。用 $A[S]$ 表示所有如下元素组成的集合：

$$
\sum a_{i_1\cdots i_n}s_1^{i_1}\cdots s_n^{i_n},
$$

其中求和遍历有限多个非负整数的 $n$ 元组 $(i_1,\ldots,i_n)$，且 $a_{i_1\cdots i_n}\in A$，$s_1,\ldots,s_n\in S$。若 $B=A[S]$，则称 $S$ 为 $B$ 在 $A$ 上的一组**生成元**（更准确地说，**环生成元**），或者说 $B$ 在 $A$ 上由 $S$ **生成**。若 $S$ 有限，则称 $B$ 在 $A$ 上**作为环有限生成**。可以说，$A[S]$ 由以 $S$ 中元素为变量、以 $A$ 中元素为系数的所有未必交换的多项式组成。注意，$S$ 中的元素相互之间可能不交换。

**例。** 域上的矩阵环在该域上有限生成，但矩阵之间未必交换。

与群的情形一样，同态由其在生成元上的作用唯一确定。换言之，设 $f:A\to A'$ 为环同态，$B=A[S]$ 如上。则 $f$ 至多有一个延拓，成为 $B$ 上在 $S$ 上取指定值的环同态。

设 $A$ 为环，$\mathfrak a$ 为理想，$S$ 为 $A$ 的子集。若 $S\subset\mathfrak a$，则记

$$
S\equiv0\pmod{\mathfrak a}.
$$

若 $x,y\in A$ 且 $x-y\in\mathfrak a$，则记

$$
x\equiv y\pmod{\mathfrak a}.
$$

若 $\mathfrak a$ 为主理想，等于 $(a)$，则也记作

$$
x\equiv y\pmod a.
$$

若 $f:A\to A/\mathfrak a$ 为典范同态，则 $x\equiv y\pmod{\mathfrak a}$ 意味着 $f(x)=f(y)$。当我们希望避免显式写出典范映射 $f$ 时，同余记号有时很方便。

<span class="original-page-anchor" id="pdf-page-106" aria-hidden="true"></span>

商环 $A/\mathfrak a$ 也称为**剩余类环**。$\mathfrak a$ 在 $A$ 中的陪集称为模 $\mathfrak a$ 的**剩余类**；若 $x\in A$，则陪集 $x+\mathfrak a$ 称为 **$x$ 模 $\mathfrak a$ 的剩余类**。

我们已经定义了任意范畴中的同构概念，所以环同构就是具有双侧逆映射的环同态。和往常一样，有如下判据：

*双射环同态 $f:A\to B$ 是同构。*

事实上，存在集合意义下的逆映射 $g:B\to A$，而 $g$ 为环同态很容易验证。

当上下文清楚表明所指的是环时，我们有时把“环同态”简称为“同态”。注意，环构成一个范畴，其中态射为同态。

*设 $f:A\to B$ 为环同态，则 $f$ 的像 $f(A)$ 是 $B$ 的子环。* 证明显然。

显然，单射环同态 $f:A\to B$ 建立了 $A$ 与其像之间的环同构。这样的同态称为（环的）**嵌入**。

设 $f:A\to A'$ 为环同态，$\mathfrak a'$ 为 $A'$ 的理想。则 $f^{-1}(\mathfrak a')$ 是 $A$ 的理想 $\mathfrak a$，并且得到诱导的单射同态

$$
A/\mathfrak a\to A'/\mathfrak a'.
$$

显然的证明留给读者。

**命题 1.1。** *环范畴中存在积。*

事实上，设 $\{A_i\}_{i\in I}$ 为一族环，$A=\prod A_i$ 为它们作为加法阿贝尔群的积。我们以显然的方式定义 $A$ 中的乘法：若 $(x_i)_{i\in I}$ 和 $(y_i)_{i\in I}$ 为 $A$ 的两个元素，则把它们的乘积定义为 $(x_i y_i)_{i\in I}$，即和加法一样，按分量定义乘法。乘法单位元就是其第 $i$ 个分量为 $A_i$ 的单位元的元素。显然，这使 $A$ 具有环结构，而向第 $i$ 个因子的投影是环同态。再者，$A$ 连同这些投影显然满足所需的泛性质。

注意，把 $A_i$ 包含到第 $i$ 个因子中的通常包含映射*不是*环同态，因为它没有把 $A_i$ 的单位元 $e_i$ 映到 $A$ 的单位元。事实上，它把 $e_i$ 映到 $A$ 中第 $i$ 个分量为 $e_i$、其余所有分量为 $0$（$=0_i$）的元素。

设 $A$ 为环。若 $A$ 的元素 $x,y$ 满足 $x\ne0$、$y\ne0$ 且 $xy=0$，则称它们为**零因子**。我们所考虑的无零因子环大多是交换环。因此，若 $1\ne0$，$A$ 为交换环，且环中没有零因子，就称环 $A$ 为**整环**（entire ring）。（这也称为 **integral domain**。不过，从语言上说，我觉得<span class="original-page-anchor" id="pdf-page-107" aria-hidden="true"></span>需要一个形容词。“Integral” 本来可以，但在英语中它已经用于“在一个环上整”，如第七章 §1 中那样。在法语中，和英语一样，有两个具有相似词根的词：“integral”和“entire”。法国人两个词都用，英语为什么不能这样做？有一点心理上的障碍：若“integral”和“entire”的用法互换，以符合长期沿用的法语习惯，本来会更好。我不知道该如何处理这一点。）

**例。** 整数环 $\mathbf Z$ 没有零因子，所以是整环。若 $S$ 为至少有 $2$ 个元素的集合，$A$ 为满足 $1\ne0$ 的环，则映射环 $\operatorname{Map}(S,A)$ 有零因子。（证明？）

设 $m$ 为不等于 $1$ 的正整数。环 $\mathbf Z/m\mathbf Z$ 有零因子当且仅当 $m$ 不是素数。（证明留作练习。）若 $n\ge2$，则域上的 $n\times n$ 矩阵环有零因子。（证明？）

以下判据经常使用。

*设 $A$ 为整环，$a,b$ 为 $A$ 中的非零元素。则 $a,b$ 生成同一个理想，当且仅当存在 $A$ 的可逆元 $u$，使得 $b=au$。*

*证明。* 若这样的可逆元存在，则 $Ab=Aua=Aa$。反过来，假定 $Aa=Ab$。则对某些元素 $c,d\in A$，可写成 $a=bc$，$b=ad$。因此 $a=adc$，从而 $a(1-dc)=0$，故 $dc=1$。于是 $c$ 是可逆元。

### §2. 交换环

***本节始终以 $A$ 表示交换环。***

$A$ 中的**素理想**是指满足 $A/\mathfrak p$ 为整环的理想 $\mathfrak p\ne A$。等价地说，它是一个理想 $\mathfrak p\ne A$，满足：只要 $x,y\in A$ 且 $xy\in\mathfrak p$，就有 $x\in\mathfrak p$ 或 $y\in\mathfrak p$。素理想在英文中常简称为 **prime**。

设 $\mathfrak m$ 为理想。若 $\mathfrak m\ne A$，且不存在包含 $\mathfrak m$ 而不同于 $\mathfrak m$ 的理想 $\mathfrak a\ne A$，则称 $\mathfrak m$ 为**极大理想**。

***每个极大理想都是素理想。***

*证明。* 设 $\mathfrak m$ 为极大理想，$x,y\in A$ 满足 $xy\in\mathfrak m$。假定 $x\notin\mathfrak m$，则 $\mathfrak m+Ax$ 是严格包含 $\mathfrak m$ 的理想，故等于 $A$。因此可以写成

$$
1=u+ax,
$$

其中 $u\in\mathfrak m$，$a\in A$。乘以 $y$，得到

<span class="original-page-anchor" id="pdf-page-108" aria-hidden="true"></span>

$$
y=yu+axy,
$$

从而 $y\in\mathfrak m$，所以 $\mathfrak m$ 是素理想。

*设 $\mathfrak a$ 为不等于 $A$ 的理想，则 $\mathfrak a$ 包含于某个极大理想 $\mathfrak m$。*

*证明。* 所有包含 $\mathfrak a$ 且不等于 $A$ 的理想组成的集合，按包含关系递增排列时，是归纳有序的。事实上，若 $\{\mathfrak b_i\}$ 是这样的理想的一个全序集，则对任意 $i$，都有 $1\notin\mathfrak b_i$，故 $1$ 不属于理想 $\mathfrak b=\bigcup\mathfrak b_i$，而 $\mathfrak b$ 是所有 $\mathfrak b_i$ 的上界。若 $\mathfrak m$ 为此集合中的极大元，则 $\mathfrak m\ne A$，且 $\mathfrak m$ 是极大理想，得证。

*理想 $\{0\}$ 是 $A$ 的素理想，当且仅当 $A$ 是整环。*

（证明显然。）

我们把**域** $K$ 定义为满足 $1\ne0$ 且非零元素组成的乘法幺半群是群的交换环（即只要 $x\in K$ 且 $x\ne0$，就存在 $x$ 的逆元）。注意，域 $K$ 的理想只有 $K$ 和零理想。

*若 $\mathfrak m$ 为 $A$ 的极大理想，则 $A/\mathfrak m$ 是域。*

*证明。* 若 $x\in A$，用 $\bar x$ 表示它模 $\mathfrak m$ 的剩余类。因 $\mathfrak m\ne A$，$A/\mathfrak m$ 的单位元不等于 $0$。$A/\mathfrak m$ 的任意非零元素均可写为 $\bar x$，其中 $x\in A$ 且 $x\notin\mathfrak m$。为求它的逆元，注意 $\mathfrak m+Ax$ 是 $A$ 中不等于 $\mathfrak m$ 的理想，故等于 $A$。因此可写成

$$
1=u+yx,
$$

其中 $u\in\mathfrak m$，$y\in A$。这意味着 $\bar y\bar x=1$（即 $=\bar1$），所以 $\bar x$ 有逆元，得证。

反过来，以下结论留给读者作为练习证明：

*若 $\mathfrak m$ 为 $A$ 的理想，且 $A/\mathfrak m$ 为域，则 $\mathfrak m$ 是极大理想。*

*设 $f:A\to A'$ 为交换环的同态，$\mathfrak p'$ 为 $A'$ 的素理想，并令 $\mathfrak p=f^{-1}(\mathfrak p')$，则 $\mathfrak p$ 是素理想。*

为证明这一点，设 $x,y\in A$，$xy\in\mathfrak p$。假定 $x\notin\mathfrak p$，则 $f(x)\notin\mathfrak p'$。但 $f(x)f(y)=f(xy)\in\mathfrak p'$，所以 $f(y)\in\mathfrak p'$，得证。

请作为练习证明：若 $f$ 为满射，且 $\mathfrak m'$ 在 $A'$ 中极大，则 $f^{-1}(\mathfrak m')$ 在 $A$ 中极大。

**例。** 设 $\mathbf Z$ 为整数环。因理想也是 $\mathbf Z$ 的加法子群，每个非零理想都是主理想，形如 $n\mathbf Z$，其中 $n>0$ 为由该理想唯一确定的整数。设 $\mathfrak p$ 为非零素理想，$\mathfrak p=n\mathbf Z$。则 $n$ 必为素数，这基本上由素理想的定义直接得出。反过来，若 $p$ 为素数，则 $p\mathbf Z$ 为素理想（显然的练习）。再者，$p\mathbf Z$ 是极大理想。事实上，假定 $p\mathbf Z$ 包含于某个理想 $n\mathbf Z$，则对某个整数 $m$ 有 $p=nm$，从而 $n=p$ 或 $n=1$，这证明了 $p\mathbf Z$ 的极大性。

<span class="original-page-anchor" id="pdf-page-109" aria-hidden="true"></span>

若 $n$ 为整数，商环 $\mathbf Z/n\mathbf Z$ 称为**模 $n$ 的整数环**。我们也记

$$
\mathbf Z/n\mathbf Z=\mathbf Z(n).
$$

若 $n$ 是素数 $p$，则模 $p$ 的整数环实际上是域，记作 $\mathbf F_p$。特别地，$\mathbf F_p$ 的乘法群称为模 $p$ 的非零整数群。由群的初等性质，可得到初等数论中的一个标准事实：若整数 $x\not\equiv0\pmod p$，则 $x^{p-1}\equiv1\pmod p$。（为简便起见，习惯上用 $\operatorname{mod}p$ 代替 $\operatorname{mod}p\mathbf Z$；类似地，对任意整数 $n$，用 $\operatorname{mod}n$ 代替 $\operatorname{mod}n\mathbf Z$。）类似地，给定整数 $n>1$，环 $\mathbf Z/n\mathbf Z$ 的可逆元是那些由非零且与 $n$ 互素的整数 $m$ 所代表的模 $n\mathbf Z$ 剩余类。按定义，$\mathbf Z/n\mathbf Z$ 的可逆元群的阶记作 $\varphi(n)$（其中 $\varphi$ 称为 **Euler φ 函数**）。因此，若整数 $x$ 与 $n$ 互素，则 $x^{\varphi(n)}\equiv1\pmod n$。

**定理 2.1（中国剩余定理）。** *设 $\mathfrak a_1,\ldots,\mathfrak a_n$ 为 $A$ 的理想，且对所有 $i\ne j$ 都有 $\mathfrak a_i+\mathfrak a_j=A$。给定元素 $x_1,\ldots,x_n\in A$，存在 $x\in A$，使得对所有 $i$ 都有 $x\equiv x_i\pmod{\mathfrak a_i}$。*

*证明。* 若 $n=2$，则对某些元素 $a_i\in\mathfrak a_i$ 有表达式

$$
1=a_1+a_2,
$$

并令 $x=x_2 a_1+x_1 a_2$。

对每个 $i\ge2$，可以找到元素 $a_i\in\mathfrak a_1$，$b_i\in\mathfrak a_i$，使得

$$
a_i+b_i=1,\qquad i\ge2.
$$

乘积 $\prod_{i=2}^n(a_i+b_i)$ 等于 $1$，且属于

$$
\mathfrak a_1+\prod_{i=2}^n\mathfrak a_i,
$$

即属于 $\mathfrak a_1+\mathfrak a_2\cdots\mathfrak a_n$。因此

$$
\mathfrak a_1+\prod_{i=2}^n\mathfrak a_i=A.
$$

由 $n=2$ 的定理，可以找到元素 $y_1\in A$，使得

$$
\begin{aligned}
y_1&\equiv1\pmod{\mathfrak a_1},\\
y_1&=0\pmod{\prod_{i=2}^n\mathfrak a_i}.
\end{aligned}
$$

类似地，可找到元素 $y_2,\ldots,y_n$，使得

$$
y_j\equiv1\pmod{\mathfrak a_j}\qquad\text{以及}\qquad y_j\equiv0\pmod{\mathfrak a_i}\quad\text{对 }i\ne j.
$$

于是 $x=x_1 y_1+\cdots+x_n y_n$ 满足我们的要求。

<span class="original-page-anchor" id="pdf-page-110" aria-hidden="true"></span>

沿着上述思路，注意：若 $\mathfrak a_1,\ldots,\mathfrak a_n$ 为环 $A$ 的理想，且满足

$$
\mathfrak a_1+\cdots+\mathfrak a_n=A,
$$

而 $\nu_1,\ldots,\nu_n$ 为正整数，则

$$
\mathfrak a_1^{\nu_1}+\cdots+\mathfrak a_n^{\nu_n}=A.
$$

证明显然，留作练习。

**推论 2.2。** *设 $\mathfrak a_1,\ldots,\mathfrak a_n$ 为 $A$ 的理想，假定 $i\ne j$ 时 $\mathfrak a_i+\mathfrak a_j=A$。令*

$$
f:A\to\prod_{i=1}^n A/\mathfrak a_i=(A/\mathfrak a_1)\times\cdots\times(A/\mathfrak a_n)
$$

*为由 $A$ 到每个因子 $A/\mathfrak a_i$ 的典范映射所诱导的、$A$ 到积的映射。则 $f$ 的核为 $\bigcap_{i=1}^n\mathfrak a_i$，且 $f$ 为满射，从而给出同构*

$$
A/\bigcap\mathfrak a_i\xrightarrow{\approx}\prod A/\mathfrak a_i.
$$

*证明。* $f$ 的核如上所述，这一点显然。满射性由定理得出。

此定理及其推论常应用于整数环 $\mathbf Z$ 和互异的素理想 $(p_1),\ldots,(p_n)$。这些理想都是极大理想，所以满足定理的假设。类似地，也可取两两互素的整数 $m_1,\ldots,m_n$，将定理应用于主理想 $(m_1)=m_1\mathbf Z,\ldots,(m_n)=m_n\mathbf Z$。这就是中国剩余定理最经典的情形。

特别地，设 $m$ 为大于 $1$ 的整数，且

$$
m=\prod_i p_i^{r_i}
$$

为 $m$ 的素因数分解，其中指数 $r_i\ge1$。则有环同构：

$$
\mathbf Z/m\mathbf Z\approx\prod_i\mathbf Z/p_i^{r_i}\mathbf Z.
$$

若 $A$ 为环，照常用 $A^*$ 表示 $A$ 中可逆元素组成的乘法群。以下断言留作练习：

*上述从 $\mathbf Z/m\mathbf Z$ 到积的环同构诱导群同构*

$$
(\mathbf Z/m\mathbf Z)^*\approx\prod_i(\mathbf Z/p_i^{r_i}\mathbf Z)^*.
$$

由这个同构，得到

$$
\varphi(m)=\prod_i\varphi(p_i^{r_i}).
$$

<span class="original-page-anchor" id="pdf-page-111" aria-hidden="true"></span>

*若 $p$ 为素数，$r$ 为不小于 $1$ 的整数，则*

$$
\varphi(p^r)=(p-1)p^{r-1}.
$$

这个公式用归纳法证明。若 $r=1$，则 $\mathbf Z/p\mathbf Z$ 为域，该域的乘法群的阶为 $p-1$。设 $r\ge1$，考虑由理想的包含关系 $(p^{r+1})\subset(p^r)$ 产生的典范环同态

$$
\mathbf Z/p^{r+1}\mathbf Z\to\mathbf Z/p^r\mathbf Z.
$$

得到诱导的群同态

$$
\lambda:(\mathbf Z/p^{r+1}\mathbf Z)^*\to(\mathbf Z/p^r\mathbf Z)^*.
$$

它是满射，因为任何代表 $\mathbf Z/p^r\mathbf Z$ 的元素且与 $p$ 互素的整数 $a$，都代表 $(\mathbf Z/p^{r+1}\mathbf Z)^*$ 的一个元素。设整数 $a$ 代表 $(\mathbf Z/p^{r+1}\mathbf Z)^*$ 的一个元素，且 $\lambda(a)=1$。则

$$
a\equiv1\pmod{p^r\mathbf Z},
$$

从而对某个 $x\in\mathbf Z$，可以写成

$$
a=1+xp^r\pmod{p^{r+1}\mathbf Z}.
$$

令 $x=0,1,\ldots,p-1$，得到 $(\mathbf Z/p^{r+1}\mathbf Z)^*$ 的 $p$ 个互异元素，它们全属于 $\lambda$ 的核。此外，上面的元素 $x$ 可以选为这 $p$ 个整数之一，因为每个整数模 $(p)$ 都同余于其中一个。因此，$\lambda$ 的核的阶为 $p$，公式得证。

注意，$\lambda$ 的核同构于 $\mathbf Z/p\mathbf Z$。（证明？）

**应用：循环群的自同态环。** 环最初的例子之一，是阿贝尔群的自同态环。对循环群的情形，我们有如下完整的描述。

**定理 2.3。** *设 $A$ 为阶为 $n$ 的循环群。对每个 $k\in\mathbf Z$，令 $f_k:A\to A$ 为自同态 $x\mapsto kx$（把 $A$ 写成加法群）。则 $k\mapsto f_k$ 诱导环同构 $\mathbf Z/n\mathbf Z\approx\operatorname{End}(A)$，以及群同构 $(\mathbf Z/n\mathbf Z)^*\approx\operatorname{Aut}(A)$。*

*证明。* 回顾，$\operatorname{End}(A)$ 上的加法群结构就是映射的相加，乘法就是映射的复合。因此，$k\mapsto f_k$ 为环同态这一事实，只是把下列公式重新表述一遍：

$$
1a=a,\qquad(k+k')a=ka+k'a,\qquad\text{以及}\qquad(kk')a=k(k'a),
$$

其中 $k,k'\in\mathbf Z$，$a\in A$。若 $a$ 为 $A$ 的生成元，则 $ka=0$ 当且仅当 $k\equiv0\pmod n$，所以 $\mathbf Z/n\mathbf Z$ 嵌入 $\operatorname{End}(A)$。另一方面，设 $f:A\to A$ 为自同态。仍取生成元 $a$，有 $f(a)=ka$<span class="original-page-anchor" id="pdf-page-112" aria-hidden="true"></span>对某个 $k$ 成立，从而 $f=f_k$，因为每个 $x\in A$ 都可写为 $ma$，其中 $m\in\mathbf Z$，而且

$$
f(x)=f(ma)=mf(a)=mka=kma=kx.
$$

这证明了同构 $\mathbf Z/n\mathbf Z\approx\operatorname{End}(A)$。再者，若 $k\in(\mathbf Z/n\mathbf Z)^*$，则存在 $k'$ 使 $kk'\equiv1\pmod n$，所以 $f_k$ 有逆映射 $f_{k'}$，且 $f_k$ 是自同构。反过来，给定任意自同构 $f$ 及其逆映射 $g$，由证明的第一部分可知，对某些 $k,k'$，有 $f=f_k$，$g=g_{k'}$；而 $f\circ g=\operatorname{id}$ 意味着 $kk'\equiv1\pmod n$，所以 $k,k'\in(\mathbf Z/n\mathbf Z)^*$。这证明了同构 $(\mathbf Z/n\mathbf Z)^*\approx\operatorname{Aut}(A)$。

注意，若把 $A$ 写成乘法群 $C$，则映射 $f_k$ 由 $x\mapsto x^k$ 给出。例如，设 $\boldsymbol\mu_n$ 为 $\mathbf C$ 中的 $n$ 次单位根群。则 $\boldsymbol\mu_n$ 的所有自同构均由下式给出：

$$
\zeta\mapsto\zeta^k\qquad\text{其中}\quad k\in(\mathbf Z/n\mathbf Z)^*.
$$

### §3. 多项式与群环

尽管所有读者都见过多项式函数，本节仍将为一般多项式建立基础。在许多场合，需要任意环上的多项式。首先，有些有限域上的多项式不能与该域上的多项式函数等同。我们需要整系数多项式，也需要对素数 $p$ 将这些多项式模 $p$ 约化。在代数几何和分析中，都需要任意交换环上的多项式，例如多项式微分算子环。我们也见过在环 $A$ 上由一组元素生成的环 $B=A[S]$ 的例子。现在系统地叙述交换环 $A$ 上多项式的基本定义。

我们希望赋予如下表达式以意义：

$$
a_0+a_1 X+\cdots+a_n X^n,
$$

其中 $a_i\in A$，$X$ 是一个“变量”。有若干种办法，我们选取其中一种。（在拙著《Undergraduate Algebra》中，我选择了另一种。）考虑由元素 $X$ 生成的无限循环群。令 $S$ 为由幂 $X^r$（$r\ge0$）组成的子集，则 $S$ 为幺半群。把**多项式**的集合 $A[X]$ 定义为所有函数 $S\to A$ 组成的集合，这些函数仅在 $S$ 的有限多个元素处不为 $0$。对每个元素 $a\in A$，用 $aX^n$ 表示在 $X^n$ 处取值为 $a$、在 $S$ 的其余所有元素处取值为 $0$ 的函数。于是立即可见，多项式可以唯一地写为一个有限和

<span class="original-page-anchor" id="pdf-page-113" aria-hidden="true"></span>

$$
a_0 X^0+\cdots+a_n X^n,
$$

其中 $n\in\mathbf N$，$a_i\in A$。这样的多项式记为 $f(X)$。元素 $a_i\in A$ 称为 $f$ 的**系数**。我们按卷积法则定义乘法。因此，给定多项式

$$
f(X)=\sum_{i=0}^n a_i X^i\qquad\text{以及}\qquad g(X)=\sum_{j=0}^m b_j X^j,
$$

将其乘积定义为

$$
f(X)g(X)=\sum_{k=0}^{m+n}\left(\sum_{i+j=k}a_i b_j\right)X^k.
$$

立即可验证，这一乘法满足结合律与分配律。下文将在更一般的幺半群环的背景下给出结合律的证明细节。注意，存在单位元，即 $1X^0$。还存在嵌入

$$
A\to A[X]\qquad\text{由}\qquad a\mapsto aX^0\quad\text{给出}.
$$

通常不区分 $a$ 与其在 $A[X]$ 中的像，用 $a$ 代替 $aX^0$。注意，对 $c\in A$，有 $cf(x)=\sum ca_i X^i$。

注意，由我们的定义，多项式等式

$$
\sum a_i X^i=\sum b_i X^i
$$

成立当且仅当对所有 $i$ 都有 $a_i=b_i$。

设 $A$ 为交换环 $B$ 的子环，$x\in B$。若 $f\in A[X]$ 为多项式，则可以定义相应的**多项式函数**

$$
f_B:B\to B,
$$

令

$$
f_B(x)=f(x)=a_0+a_1 x+\cdots+a_n x^n.
$$

给定元素 $b\in B$，由多项式乘法的定义直接得到：

*对应*

$$
\operatorname{ev}_b:f\mapsto f(b)
$$

*是 $A[X]$ 到 $B$ 的环同态。*

此同态称为**求值同态**，也说它是把多项式中的 $X$ **代入**为 $b$ 而得到的。（参见下文命题 3.1。）

设 $x\in B$。现在可见，$B$ 中在 $A$ 上由 $x$ 生成的子环 $A[x]$，就是所有多项式值 $f(x)$（$f\in A[X]$）组成的环。若求值映射 $f\mapsto f(x)$ 给出 $A[X]$ 与 $A[x]$ 的同构，则称 $x$ 为<span class="original-page-anchor" id="pdf-page-114" aria-hidden="true"></span>在 $A$ 上**超越**的，或称 $x$ 为 $A$ 上的**变量**。特别地，$X$ 是 $A$ 上的变量。

**例。** 令 $\alpha=\sqrt2$。则所有形如 $a+b\alpha$（其中 $a,b\in\mathbf Z$）的实数组成实数的一个子环，它由 $\sqrt2$ 生成。注意，$\alpha$ 在 $\mathbf Z$ 上不是超越的，因为多项式 $X^2-2$ 属于求值映射 $f\mapsto f(\sqrt2)$ 的核。另一方面，可以证明 $e=2.718\ldots$ 和 $\pi$ 在 $\mathbf Q$ 上都是超越的。见附录 1。

**例。** 设 $p$ 为素数，$K=\mathbf Z/p\mathbf Z$，则 $K$ 为域。令 $f(X)=X^p-X\in K[X]$。$f$ 不是零多项式，但 $f_K$ 是零函数。事实上，$f_K(0)=0$。若 $x\in K$，$x\ne0$，则因 $K$ 的乘法群的阶为 $p-1$，有 $x^{p-1}=1$，从而 $x^p=x$，故 $f(x)=0$。因此，一个非零多项式可以给出 $K$ 上的零函数。

多项式环还有另一个与系数有关的同态。设

$$
\varphi:A\to B
$$

为交换环的同态。则有相应的多项式环同态 $A[X]\to B[X]$，使得

$$
f(X)=\sum a_i X^i\mapsto\sum\varphi(a_i)X^i=(\varphi f)(X).
$$

立即可验证，这个映射是同态；下文命题 3.2 将在更一般的背景下给出进一步的细节。我们称 $f\mapsto\varphi f$ 为**约化映射**。

**例。** 在某些应用中，映射 $\varphi$ 可以是同构。例如，若 $f(X)$ 的系数为复数，则对其系数施以复共轭，便得到它的复共轭 $\bar f(X)=\sum\bar a_i X^i$。

设 $\mathfrak p$ 为 $A$ 的素理想，$\varphi:A\to A'$ 为 $A$ 到 $A/\mathfrak p$ 的典范满射同态。若 $f(X)$ 是 $A[X]$ 中的多项式，则 $\varphi f$ 有时称为 **$f$ 模 $\mathfrak p$ 的约化**。

例如，取 $A=\mathbf Z$，$\mathfrak p=(p)$，其中 $p$ 为素数。把系数 $3,-1,2$ 看作模 $5$ 的整数，即 $\mathbf Z/5\mathbf Z$ 的元素，就可以把多项式 $3X^4-X+2$ 看作模 $5$ 的多项式。

现在可以把求值映射与约化映射结合起来，推广求值映射。

*设 $\varphi:A\to B$ 为交换环的同态。*

*设 $x\in B$。存在唯一的延拓 $\varphi$ 的同态*

$$
A[X]\to B\qquad\text{使得}\qquad X\mapsto x,
$$

*而在这个同态下，$\sum a_i X^i\mapsto\sum\varphi(a_i)x^i$。*

<span class="original-page-anchor" id="pdf-page-115" aria-hidden="true"></span>

上面结论中的同态可看成复合映射

$$
A[X]\longrightarrow B[X]\xrightarrow{\operatorname{ev}_x}B,
$$

其中第一个映射把 $\varphi$ 作用于多项式的系数，第二个映射是前面讨论过的在 $x$ 处的求值。

**例。** 第九章 §2 和 §3 将讨论多变量的这种情形：当 $(\varphi f)(x)=0$ 时，称 $x$ 为多项式 $f$ 的一个**零点**。

将多项式写作 $f(X)=\sum_{i=0}^n a_i X^i$ 时，若 $a_n\ne0$，则定义 $n$ 为 $f$ 的**次数**。因此，$f$ 的次数是使 $r>n$ 时 $a_r=0$ 成立的最小整数 $n$。若 $f=0$（即 $f$ 为零多项式），则约定 $f$ 的次数为 $-\infty$。我们约定，对所有 $n\in\mathbf Z$，

$$
-\infty+-\infty=-\infty,\qquad-\infty+n=-\infty,\qquad-\infty<n,
$$

而不定义涉及 $-\infty$ 的其他运算。次数为 $1$ 的多项式也称为**线性**多项式。若 $f\ne0$ 且 $\deg f=n$，则称 $a_n$ 为 $f$ 的**首项系数**，称 $a_0$ 为其**常数项**。

设

$$
g(X)=b_0+\cdots+b_m X^m
$$

为 $A[X]$ 中次数为 $m$ 的多项式，且假定 $g\ne0$。则

$$
f(X)g(X)=a_0 b_0+\cdots+a_n b_m X^{m+n}.
$$

因此：

*若假定首项系数 $a_n$ 或 $b_m$ 中至少有一个不是 $A$ 中的零因子，则*

$$
\deg(fg)=\deg f+\deg g,
$$

*且 $fg$ 的首项系数为 $a_n b_m$。特别地，当 $a_n$ 或 $b_m$ 为 $A$ 的可逆元，或 $A$ 为整环时，这一结论成立。所以，当 $A$ 为整环时，$A[X]$ 也是整环。*

若 $f$ 或 $g$ 为 $0$，只要约定对任意整数 $m$ 有 $-\infty+m=-\infty$，仍然有

$$
\deg(fg)=\deg f+\deg g.
$$

容易验证，对任意多项式 $f,g\in A[X]$，都有

$$
\deg(f+g)\le\max(\deg f,\deg g),
$$

这里仍约定对每个整数 $m$ 都有 $-\infty<m$。

<span class="original-page-anchor" id="pdf-page-116" aria-hidden="true"></span>

### 多元多项式

现在转向多元多项式。设 $A$ 是交换环 $B$ 的子环。设 $x_1,\ldots,x_n\in B$。对于每个整数 $n$ 元组 $(\nu_1,\ldots,\nu_n)=(\nu)\in\mathbf N^n$，我们采用向量记号，令 $(x)=(x_1,\ldots,x_n)$，并令

$$
M_{(\nu)}(x)=x_1^{\nu_1}\cdots x_n^{\nu_n}.
$$

这些元素的集合在乘法下构成一个幺半群。令 $A[x]=A[x_1,\ldots,x_n]$ 为 $B$ 中由 $x_1,\ldots,x_n$ 在 $A$ 上生成的子环。那么，$A[x]$ 的每个元素都可以写成有限和

$$
\sum a_{(\nu)}M_{(\nu)}(x),\qquad a_{(\nu)}\in A.
$$

反复使用一元多项式的构造，可以形成环

$$
A[X_1,\ldots,X_n]=A[X_1][X_2]\cdots[X_n],
$$

其中选取 $X_n$ 为 $A[X_1,\ldots,X_{n-1}]$ 上的一个变量。于是，$A[X_1,\ldots,X_n]=A[X]$ 的每个元素 $f$ 都有如下*唯一*的有限和表达式：

$$
f=\sum_{j=0}^{d_n}f_j(X_1,\ldots,X_{n-1})X_n^j,\qquad f_j\in A[X_1,\ldots,X_{n-1}].
$$

因此，由归纳法，可以把 $f$ 唯一地写成

$$
\begin{aligned}
f&=\sum_{\nu_n=0}^{d_n}\left(\sum_{\nu_1,\ldots,\nu_{n-1}}a_{\nu_1\cdots\nu_n}X_1^{\nu_1}\cdots X_{n-1}^{\nu_{n-1}}\right)X_n^{\nu_n}\\
&=\sum a_{(\nu)}M_{(\nu)}(X)=\sum a_{(\nu)}X_1^{\nu_1}\cdots X_n^{\nu_n},
\end{aligned}
$$

其中 $a_{(\nu)}\in A$，这些元素称为 $f$ 的**系数**。乘积

$$
M_{(\nu)}(X)=X_1^{\nu_1}\cdots X_n^{\nu_n}
$$

称为**原始单项式**。$A[X]$ 的元素称为（$n$ 元）**多项式**，$a_{(\nu)}$ 称为它的**系数**。

与一元情形一样，我们有求值映射。给定 $(x)=(x_1,\ldots,x_n)$ 以及上述 $f$，定义

$$
f(x)=\sum a_{(\nu)}M_{(\nu)}(x)=\sum a_{(\nu)}x_1^{\nu_1}\cdots x_n^{\nu_n}.
$$

于是，**求值映射**

$$
\operatorname{ev}_{(x)}:A[X]\to B,\qquad f\mapsto f(x),
$$

是环同态。它可以看作依次对 $i=n,\ldots,1$ 进行的一元求值映射 $X_i\mapsto x_i$ 的复合，因为 $A[X]\subset B[X]$。

与一元情形一样，如果 $f(X)\in A[X]$ 是一个 $n$ 元多项式，那么就得到一个函数

<span class="original-page-anchor" id="pdf-page-117" aria-hidden="true"></span>

$$
f_B:B^n\to B,\qquad(x)\mapsto f(x).
$$

我们说，$f(x)$ 是通过在 $f$ 中用 $(x)$ **代入** $(X)$，或者把 $(X)$ **特化**为 $(x)$ 得到的。与一元情形一样，如果 $K$ 是有限域，且 $f\in K[X]$，就可能出现 $f\ne 0$ 但 $f_K=0$ 的情况。参见第四章定理 1.4 及其推论。

其次，设 $\varphi:A\to B$ 为交换环同态。那么有如下**约化映射**（下文命题 3.2 将对它作推广）：

$$
f(X)=\sum a_{(\nu)}M_{(\nu)}(X)\mapsto\sum\varphi(a_{(\nu)})M_{(\nu)}(X)=(\varphi f)(X).
$$

我们也可以将求值映射与约化映射复合。如果 $(\varphi f)(x)=0$，就称元素 $(x)\in B^n$ 为 $f$ 的一个**零点**。这样的零点将在第九章研究。

重新设 $A$ 为 $B$ 的子环。如果求值映射

$$
f\mapsto f(x)
$$

是单射，就称元素 $x_1,\ldots,x_n\in B$ 在 $A$ 上**代数无关**。等价地，如果多项式 $f\in A[X]$ 满足 $f(x)=0$，则 $f=0$；换言之，$x_1,\ldots,x_n$ 之间不存在 $A$ 上的非平凡多项式关系。

**例。** 尚不清楚 $e$ 与 $\pi$ 在有理数域上是否代数无关。甚至连 $e+\pi$ 是否为有理数也尚不清楚。

现在讨论多元情形下次数的概念。原始单项式

$$
M_{(\nu)}(X)=X_1^{\nu_1}\cdots X_n^{\nu_n}
$$

的**次数**指整数 $|\nu|=\nu_1+\cdots+\nu_n$（它满足 $\geq 0$）。形如

$$
aX_1^{\nu_1}\cdots X_n^{\nu_n}\qquad(a\in A)
$$

的多项式称为**单项式**（不一定是原始单项式）。

如果 $f(X)$ 是 $A[X]$ 中的多项式，写成

$$
f(X)=\sum a_{(\nu)}X_1^{\nu_1}\cdots X_n^{\nu_n},
$$

那么，或者 $f=0$，此时称它的次数为 $-\infty$；或者 $f\ne 0$，此时定义 $f$ 的**次数**为所有满足 $a_{(\nu)}\ne 0$ 的单项式 $M_{(\nu)}(X)$ 的次数的最大值。（这样的单项式称为**出现**在该多项式中。）注意，$f$ 的次数为 $0$，当且仅当

$$
f(X)=a_0X_1^0\cdots X_n^0,
$$

其中 $a_0\in A$ 且 $a_0\ne 0$。这个多项式也简记为 $f(X)=a_0$，即用 $1$ 代替

$$
X_1^0\cdots X_n^0;
$$

换言之，我们把这个多项式与常数 $a_0$ 等同起来。

<span class="original-page-anchor" id="pdf-page-118" aria-hidden="true"></span>

注意，$n$ 元多项式 $f(X_1,\ldots,X_n)$ 可以看作以 $A[X_1,\ldots,X_{n-1}]$ 中的元素为系数的 $X_n$ 的多项式（当 $n\geq 2$ 时）。事实上，可以写成

$$
f(X)=\sum_{j=0}^{d_n}f_j(X_1,\ldots,X_{n-1})X_n^j,
$$

其中 $f_j$ 是 $A[X_1,\ldots,X_{n-1}]$ 的元素。所谓 **$f$ 关于 $X_n$ 的次数**，是指把它看作系数属于 $A[X_1,\ldots,X_{n-1}]$ 的 $X_n$ 的多项式时的次数。容易看出，如果这个次数为 $d$，那么 $d$ 就是所有满足 $a_{(\nu)}\ne 0$ 的单项式

$$
a_{(\nu)}X_1^{\nu_1}\cdots X_n^{\nu_n}
$$

中，作为 $X_n$ 的指数出现的最大整数。类似地，可以定义 $f$ 关于每个变量 $X_i$（$i=1,\ldots,n$）的次数。

当然，$f$ 关于每个变量的次数通常与它的次数不同（为了避免歧义，后者有时称为**总次数**）。例如，

$$
X_1^3X_2+X_2^2
$$

的总次数为 $4$，关于 $X_1$ 的次数为 $3$，关于 $X_2$ 的次数为 $2$。

在记号上，我们常把“degree”缩写成“deg.”。

给定多项式 $f$，对于每个整数 $d\geq 0$，令 $f^{(d)}$ 为出现在 $f$ 中且次数为 $d$ 的所有单项式之和。那么

$$
f=\sum_d f^{(d)}.
$$

设 $f\ne 0$。如果 $f=f^{(d)}$，就称 $f$ 为次数为 $d$ 的**齐次**多项式；因此，$f$ 可以写成

$$
f(X)=\sum a_{(\nu)}X_1^{\nu_1}\cdots X_n^{\nu_n},\qquad a_{(\nu)}\ne 0\ \text{时}\ \nu_1+\cdots+\nu_n=d.
$$

以下命题的证明留作练习：*$A$ 上的一个非零 $n$ 元多项式 $f$ 是次数为 $d$ 的齐次多项式，当且仅当对于每组在 $A$ 上代数无关的 $n+1$ 个元素 $u,t_1,\ldots,t_n$，都有*

$$
f(ut_1,\ldots,ut_n)=u^df(t_1,\ldots,t_n).
$$

注意，若 $f,g$ 分别是次数为 $d,e$ 的齐次多项式，且 $fg\ne 0$，则 $fg$ 是次数为 $d+e$ 的齐次多项式。如果 $d=e$ 且 $f+g\ne 0$，则 $f+g$ 是次数为 $d$ 的齐次多项式。

**注。** 考虑同构

$$
A[X_1,\ldots,X_n]\approx A[t_1,\ldots,t_n],
$$

它建立在 $n$ 元多项式环与一个在 $A$ 上由 $n$ 个<span class="original-page-anchor" id="pdf-page-119" aria-hidden="true"></span>代数无关的元素生成的环之间，因此可以把为多项式定义的所有术语用于 $A[t_1,\ldots,t_n]$ 的元素。因此，可以谈论 $A[t]$ 中元素的次数，乘积与和的次数法则也仍然成立。事实上，我们也把 $A[t]$ 的元素称为 $(t)$ 的多项式。代数无关的元素也称为**变量**（或独立变量）；我们对 $A[X]$ 与 $A[t]$ 所作的区分，更多是心理上的，而非数学上的。

其次，设 $A$ 是整环。由一元多项式的已知性质及归纳法可知，$A[X_1,\ldots,X_n]$ 也是整环。特别地，设 $f$ 的次数为 $d$，$g$ 的次数为 $e$。写成

$$
\begin{aligned}
f&=f^{(d)}+\text{次数较低的项},\\
g&=g^{(e)}+\text{次数较低的项}.
\end{aligned}
$$

那么 $fg=f^{(d)}g^{(e)}+\text{次数较低的项}$，而且若 $fg\ne 0$，则 $f^{(d)}g^{(e)}\ne 0$。因此得到

$$
\deg(fg)=\deg f+\deg g,
$$

$$
\deg(f+g)\leq\max(\deg f,\deg g).
$$

至此，多项式的基本术语已经介绍完毕。在本节结尾，我们将说明，多项式的构造实际上是另一种在其他背景中使用的构造的特例。感兴趣的读者可以直接跳到第四章，那里给出多项式的其他重要性质。关于调和多项式，另参见第十三章练习 33。

### 群环或幺半群环

设 $A$ 是交换环，$G$ 是采用乘法记号的幺半群。

令 $A[G]$ 为所有映射 $\alpha:G\to A$ 的集合，其中对几乎所有 $x\in G$ 都有 $\alpha(x)=0$。我们把 $A[G]$ 中的加法定义为取值于阿贝尔（加法）群的映射的通常加法。对于 $\alpha,\beta\in A[G]$，按以下规则定义它们的乘积 $\alpha\beta$：

$$
(\alpha\beta)(z)=\sum_{xy=z}\alpha(x)\beta(y).
$$

求和遍及所有满足 $x,y\in G$ 且 $xy=z$ 的有序对 $(x,y)$。这个和实际上是有限的，因为满足 $\alpha(x)\beta(y)\ne 0$ 的元素对 $(x,y)\in G\times G$ 只有有限多个。还可看出，对几乎所有 $t$，都有 $(\alpha\beta)(t)=0$，因而它属于集合 $A[G]$。

环的公理很容易验证。我们以结合律为例给出证明。设 $\alpha,\beta,\gamma\in A[G]$。那么

<span class="original-page-anchor" id="pdf-page-120" aria-hidden="true"></span>

$$
\begin{aligned}
((\alpha\beta)\gamma)(z)&=\sum_{xy=z}(\alpha\beta)(x)\gamma(y)\\
&=\sum_{xy=z}\left[\sum_{uv=x}\alpha(u)\beta(v)\right]\gamma(y)\\
&=\sum_{xy=z}\left[\sum_{uv=x}\alpha(u)\beta(v)\gamma(y)\right]\\
&=\sum_{\substack{(u,v,y)\\uvy=z}}\alpha(u)\beta(v)\gamma(y),
\end{aligned}
$$

最后这个和遍及所有乘积为 $z$ 的三元组 $(u,v,y)$。这个和现在是对称的；如果计算 $(\alpha(\beta\gamma))(z)$，也会得到这个和。这就证明了结合律。

**译校注：** 此句原书印作三元组“$(u\ v,y)$”，$u$ 与 $v$ 之间缺少逗号；依据紧邻的三重求和下标 $(u,v,y)$ 及“三元组”的表述，译文补为 $(u,v,y)$。

$A[G]$ 的单位元是函数 $\delta$，其中 $\delta(e)=1$，而对所有 $x\in G$、$x\ne e$，有 $\delta(x)=0$。容易验证，对所有 $\alpha\in A[G]$，都有 $\alpha=\delta\alpha=\alpha\delta$。

现在采用一种记号，使 $A[G]$ 的结构更清楚。设 $a\in A$ 且 $x\in G$。用 $a\cdot x$（有时也用 $ax$）表示这样一个函数：它在 $x$ 处的值为 $a$，在 $y\ne x$ 处的值为 $0$。那么，元素 $\alpha\in A[G]$ 可以写成和

$$
\alpha=\sum_{x\in G}\alpha(x)\cdot x.
$$

事实上，若 $\{a_x\}_{x\in G}$ 是 $A$ 的一组元素，其中几乎所有元素都为 $0$，并令

$$
\beta=\sum_{x\in G}a_x\cdot x,
$$

则对任意 $y\in G$，由定义直接可得 $\beta(y)=a_y$。这还表明，给定元素 $\alpha$ 有唯一的和式表达 $\sum a_x\cdot x$。

采用现在的记号，乘法可以写成

$$
\left(\sum_{x\in G}a_x\cdot x\right)\left(\sum_{y\in G}b_y\cdot y\right)=\sum_{x,y}a_xb_y\cdot xy,
$$

加法可以写成

$$
\sum_{x\in G}a_x\cdot x+\sum_{x\in G}b_x\cdot x=\sum_{x\in G}(a_x+b_x)\cdot x,
$$

这样就呈现出我们希望的形式。注意，$A[G]$ 的单位元就是 $1\cdot e$。

现在来说明，可以将 $A$ 与 $G$ 都自然地嵌入 $A[G]$。

令 $\varphi_0:G\to A[G]$ 为映射 $\varphi_0(x)=1\cdot x$。立即可以验证，$\varphi_0$ 是乘法幺半群同态，并且是单射，即一个嵌入。

**译校注：** 这里关于 $\varphi_0$ 为单射的断言需要系数环 $A$ 非零，即 $1\ne0$。本章允许零环；若 $A$ 是零环，则所有 $1\cdot x$ 都是同一个零函数，除非 $G$ 只有一个元素，否则该映射并非单射。原文的断言保留如上，此注说明所需条件。

令 $f_0:A\to A[G]$ 为如下映射：

$$
f_0(a)=a\cdot e.
$$

<span class="original-page-anchor" id="pdf-page-121" aria-hidden="true"></span>

立即可以验证，$f_0$ 是环同态，也是一种嵌入。因此，把 $A$ 看作 $A[G]$ 的子环。称 $A[G]$ 为 $G$ 在 $A$ 上的**幺半群环**或**幺半群代数**；如果 $G$ 是群，则称为**群代数**。

**例。** 当 $G$ 是有限群、$A=k$ 是域时，群环 $k[G]$ 将在第十八章研究。

多项式环是上述构造的特例。对于 $n$ 个变量，考虑一个秩为 $n$ 的乘法自由阿贝尔群。设 $X_1,\ldots,X_n$ 为生成元。令 $G$ 为由所有满足 $\nu_i\geq 0$（对每个 $i$）的元素 $X_1^{\nu_1}\cdots X_n^{\nu_n}$ 组成的乘法子集。那么 $G$ 是幺半群，读者可以立即验证，$A[G]$ 就是 $A[X_1,\ldots,X_n]$。

在记号上，写环 $A[G]$ 的元素时通常省略圆点，所以把这样的元素简记为 $\sum a_xx$。

更一般地，设 $I=\{i\}$ 是无限指标族，$S$ 是以 $X_i$ 为自由生成元、采用乘法记号的自由阿贝尔群。那么，取由以下乘积组成的幺半群，就可以形成多项式环 $A[X]$：

$$
M_{(\nu)}(X)=\prod_{i\in I}X_i^{\nu_i},
$$

其中，当然只有有限多个指数 $\nu_i$ 不等于 $0$。如果 $A$ 是交换环 $B$ 的子环，$S$ 是 $B$ 的子集，我们还采用下面的记号。设 $\nu:S\to\mathbf N$ 为映射，除 $S$ 的有限多个元素外，它的值都为 $0$。记

$$
M_{(\nu)}(S)=\prod_{x\in S}x^{\nu(x)}.
$$

这样便得到无限多个变量的多项式。使用这种多项式的一个有趣例子，是 Artin 对域的代数闭包存在性的证明，参见第五章定理 2.5。

现在在幺半群的背景下考虑求值同态与约化同态。

**命题 3.1。** *设 $\varphi:G\to G'$ 为幺半群同态。那么存在唯一的同态 $h:A[G]\to A[G']$，使得对所有 $x\in G$，都有 $h(x)=\varphi(x)$，且对所有 $a\in A$，都有 $h(a)=a$。*

*证明。* 事实上，设 $\alpha=\sum a_xx\in A[G]$。定义

$$
h(\alpha)=\sum a_x\varphi(x).
$$

立即可以验证，$h$ 是阿贝尔群同态，且 $h(x)=\varphi(x)$。设 $\beta=\sum b_yy$。那么

$$
h(\alpha\beta)=\sum_z\left(\sum_{xy=z}a_xb_y\right)\varphi(z).
$$

立即可得 $h(\alpha\beta)=h(\alpha)h(\beta)$，依据的是假设 $\varphi(xy)=$ <span class="original-page-anchor" id="pdf-page-122" aria-hidden="true"></span>$\varphi(x)\varphi(y)$。如果 $e$ 是 $G$ 的单位元，则由定义 $\varphi(e)=e'$，因此命题 3.1 得证。

**命题 3.2。** *设 $G$ 为幺半群，$f:A\to B$ 为交换环同态。那么存在唯一的同态*

$$
h:A[G]\to B[G],
$$

*使得*

$$
h\left(\sum_{x\in G}a_xx\right)=\sum_{x\in G}f(a_x)x.
$$

*证明。* 因为 $A[G]$ 的每个元素都有唯一的和式表达 $\sum a_xx$，所以定义 $h$ 的公式给出了从 $A[G]$ 到 $B[G]$ 的良定义映射。这个映射显然是阿贝尔群同态。对于乘法，令

$$
\alpha=\sum a_xx,\qquad\beta=\sum b_yy.
$$

那么

$$
\begin{aligned}
h(\alpha\beta)&=\sum_{z\in G}f\left(\sum_{xy=z}a_xb_y\right)z\\
&=\sum_{z\in G}\sum_{xy=z}f(a_x)f(b_y)z\\
&=h(\alpha)h(\beta).
\end{aligned}
$$

显然有 $h(1)=1$，所以 $h$ 是环同态，命题得证。

注意，把 $A$ 看作 $A[G]$ 的子环时，$h$ 在 $A$ 上的限制就是同态 $f$ 本身。换言之，如果 $e$ 是 $G$ 的单位元，则

$$
h(ae)=f(a)e.
$$

## §4. 局部化

*仍设 $A$ 为交换环。*

所谓 $A$ 的**乘法子集**，是指 $A$ 的子幺半群（依照公理 RI 2，把 $A$ 看作乘法幺半群）。换言之，它是一个包含 $1$ 的子集 $S$，并且若 $x,y\in S$，则 $xy\in S$。

现在构造 $A$ 关于 $S$ 的**商环**，也称为 $A$ 关于 $S$ 的**分式环**。

考虑满足 $a\in A$、$s\in S$ 的有序对 $(a,s)$。在这样的有序对之间定义关系

$$
(a,s)\sim(a',s'),
$$

其条件为存在元素 $s_1\in S$，使得

<span class="original-page-anchor" id="pdf-page-123" aria-hidden="true"></span>

$$
s_1(s'a-sa')=0.
$$

容易验证，这是一个等价关系；包含有序对 $(a,s)$ 的等价类记为 $a/s$。等价类的集合记为 $S^{-1}A$。

注意，若 $0\in S$，则 $S^{-1}A$ 恰好只有一个元素，即 $0/1$。按照下式定义 $S^{-1}A$ 中的乘法：

$$
(a/s)(a'/s')=aa'/ss'.
$$

容易验证，这一定义是良定义的。该乘法有单位元 $1/1$，而且显然满足结合律。

按照下式定义 $S^{-1}A$ 中的加法：

$$
\frac{a}{s}+\frac{a'}{s'}=\frac{s'a+sa'}{ss'}.
$$

容易验证，这也是良定义的。作为例子，详细给出证明。设 $a_1/s_1=a/s$，$a'_1/s'_1=a'/s'$。需要证明

$$
(s'_1a_1+s_1a'_1)/s_1s'_1=(s'a+sa')/ss'.
$$

存在 $s_2,s_3\in S$，使得

$$
s_2(sa_1-s_1a)=0,
$$

$$
s_3(s'a'_1-s'_1a')=0.
$$

将第一个等式乘以 $s_3s's'_1$，第二个等式乘以 $s_2ss_1$，然后相加，得到

$$
s_2s_3[s's'_1(sa_1-s_1a)+ss_1(s'a'_1-s'_1a')]=0.
$$

按照定义，这正是所要证明的：存在 $S$ 的一个元素（例如 $s_2s_3$），乘以

$$
ss'(s'_1a_1+s_1a'_1)-s_1s'_1(s'a+sa')
$$

后得到 $0$。

注意，给定 $a\in A$ 和 $s,s'\in S$，有

$$
a/s=s'a/s's.
$$

因此，分式的这一基本性质在当前的一般背景下仍然成立。

最后，也容易验证，$S^{-1}A$ 上这两个合成律定义了一个环结构。

令

$$
\varphi_S:A\to S^{-1}A
$$

为满足 $\varphi_S(a)=a/1$ 的映射。立即可以看出，$\varphi_S$ 是一个<span class="original-page-anchor" id="pdf-page-124" aria-hidden="true"></span>环同态。此外，$\varphi_S(S)$ 的每个元素在 $S^{-1}A$ 中都可逆（$s/1$ 的逆为 $1/s$）。

设 $\mathcal C$ 为如下范畴：其对象为环同态

$$
f:A\to B,
$$

并且对每个 $s\in S$，元素 $f(s)$ 在 $B$ 中都可逆。如果 $f:A\to B$ 和 $f':A\to B'$ 是 $\mathcal C$ 的两个对象，那么从 $f$ 到 $f'$ 的态射 $g$ 是一个同态

$$
g:B\to B',
$$

使下图交换：

$$
\begin{array}{ccc}
A&\xrightarrow{f}&B\\
&\scriptstyle f'\searrow\quad\swarrow\scriptstyle g&\\
&B'&
\end{array}
$$

*我们断言，$\varphi_S$ 是此范畴 $\mathcal C$ 中的一个泛对象。*

*证明。* 假设 $a/s=a'/s'$，换言之，二元组 $(a,s)$ 和 $(a',s')$ 等价。存在 $s_1\in S$，使得

$$
s_1(s'a-sa')=0.
$$

设 $f:A\to B$ 是 $\mathcal C$ 的一个对象。则

$$
f(s_1)[f(s')f(a)-f(s)f(a')]=0.
$$

乘以 $f(s_1)^{-1}$，再乘以 $f(s')^{-1}$ 和 $f(s)^{-1}$，得到

$$
f(a)f(s)^{-1}=f(a')f(s')^{-1}.
$$

因此，我们可以定义映射

$$
h:S^{-1}A\to B,
$$

使得对所有 $a/s\in S^{-1}A$，都有 $h(a/s)=f(a)f(s)^{-1}$。容易验证，$h$ 是一个同态，并使通常的图交换。也容易验证，这样的映射 $h$ 是唯一的，因此 $\varphi_S$ 就是所要求的泛对象。

*设 $A$ 为整环，$S$ 为不含 $0$ 的乘法子集。那么*

$$
\varphi_S:A\to S^{-1}A
$$

*是单射。*

事实上，根据定义，如果 $a/1=0$，则存在 $s\in S$，使得 $sa=0$，从而 $a=0$。

乘法集 $S$ 最重要的几种情形如下：

**1.** 设 $A$ 为交换环，$S$ 为 $A$ 的可逆元素的集合（即所有可逆元构成的集合）。显然，$S$ 是乘法集，且<span class="original-page-anchor" id="pdf-page-125" aria-hidden="true"></span>常记作 $A^*$。如果 $A$ 为域，那么 $A^*$ 就是 $A$ 的非零元素构成的乘法群。在这种情形下，$S^{-1}A$ 就是 $A$ 本身。

**2.** 设 $A$ 为整环，$S$ 为 $A$ 的非零元素的集合。那么 $S$ 是乘法集，而 $S^{-1}A$ 是一个域，称为 $A$ 的**商域**或**分式域**。通常将 $A$ 视为 $S^{-1}A$ 的一个子集，于是对 $a\in A$ 和 $s\in S$，可以写成

$$
a/s=s^{-1}a.
$$

我们在 §3 中已经看到，当 $A$ 为整环时，$A[X_1,\ldots,X_n]$ 也是整环。如果 $K$ 为 $A$ 的商域，那么 $A[X_1,\ldots,X_n]$ 的商域记作 $K(X_1,\ldots,X_n)$。$K(X_1,\ldots,X_n)$ 的元素称为**有理函数**。有理函数可以写成商 $f(X)/g(X)$，其中 $f,g$ 为多项式。如果 $(b_1,\ldots,b_n)\in K^{(n)}$，且某有理函数能够表示为商 $f/g$，满足 $g(b)\ne0$，那么我们称此有理函数**在 $(b)$ 处有定义**。由局部化的一般性质可知，此时可以将 $(b)$ 代入该有理函数，得到值 $f(b)/g(b)$。

**3.** 如果环 $A$ 是交换的，而且只有一个极大理想，就称 $A$ 为**局部环**。如果 $A$ 是局部环，$\mathfrak m$ 是其极大理想，且 $x\in A$、$x\notin\mathfrak m$，那么 $x$ 是可逆元（否则，$x$ 生成一个不包含于 $\mathfrak m$ 的真理想，这是不可能的）。设 $A$ 为环，$\mathfrak p$ 为素理想。设 $S$ 为 $\mathfrak p$ 在 $A$ 中的补集。那么 $S$ 是 $A$ 的乘法子集，$S^{-1}A$ 记作 $A_{\mathfrak p}$。它是局部环（参见习题 3），称为 **$A$ 在 $\mathfrak p$ 处的局部环**。另参见主理想整环的例子及习题 15、16。

设 $S$ 为 $A$ 的乘法子集。以 $J(A)$ 表示 $A$ 的理想的集合。于是可以定义映射

$$
\psi_S:J(A)\to J(S^{-1}A);
$$

具体地，令 $\psi_S(\mathfrak a)=S^{-1}\mathfrak a$ 为 $S^{-1}A$ 的如下子集：其中包含所有满足 $a\in\mathfrak a$、$s\in S$ 的分式 $a/s$。读者容易验证，$S^{-1}\mathfrak a$ 是一个 $S^{-1}A$-理想，并且 $\psi_S$ 对理想集 $J(A)$ 上的加法和乘法幺半群结构都是同态。此外，$\psi_S$ 还保持交集与包含关系；换言之，对 $A$ 的理想 $\mathfrak a,\mathfrak b$，有

$$
S^{-1}(\mathfrak a+\mathfrak b)=S^{-1}\mathfrak a+S^{-1}\mathfrak b,\qquad
S^{-1}(\mathfrak a\mathfrak b)=(S^{-1}\mathfrak a)(S^{-1}\mathfrak b),
$$

$$
S^{-1}(\mathfrak a\cap\mathfrak b)=S^{-1}\mathfrak a\cap S^{-1}\mathfrak b.
$$

作为例子，我们证明最后一个关系。设 $x\in\mathfrak a\cap\mathfrak b$。那么 $x/s$ 既属于 $S^{-1}\mathfrak a$，也属于 $S^{-1}\mathfrak b$，所以一个方向的包含关系是显然的。反过来，假设 $S^{-1}A$ 中的某个元素可写成 $a/s=b/s'$，其中 $a\in\mathfrak a$、$b\in\mathfrak b$，且 $s,s'\in S$。于是存在 $s_1\in S$，使得

$$
s_1s'a=s_1sb,
$$

<span class="original-page-anchor" id="pdf-page-126" aria-hidden="true"></span>

而这个元素同时属于 $\mathfrak a$ 和 $\mathfrak b$。因此

$$
a/s=s_1s'a/s_1s's
$$

属于 $S^{-1}(\mathfrak a\cap\mathfrak b)$，这就证明了所要证明的结论。

## §5. 主理想整环与唯一分解整环

*设 $A$ 为整环。* 如果元素 $a\ne0$ 不是可逆元，而且每当将它写成 $a=bc$，其中 $b\in A$、$c\in A$ 时，$b$ 或 $c$ 总有一个是可逆元，就称 $a$ 为**不可约元**。

*设 $a\ne0$ 为 $A$ 的元素，并假设主理想 $(a)$ 是素理想。那么 $a$ 是不可约元。* 事实上，如果写成 $a=bc$，那么 $b$ 或 $c$ 属于 $(a)$，不妨设是 $b$。于是可以写成 $b=ad$，其中 $d\in A$，从而 $a=acd$。由于 $A$ 是整环，得到 $cd=1$，换言之，$c$ 是可逆元。

上述断言的逆命题并不总是成立。我们将讨论它在什么条件下成立。对元素 $a\in A$、$a\ne0$，如果存在一个可逆元 $u$，以及 $A$ 中的不可约元 $p_i$（$i=1,\ldots,r$），使得

$$
a=u\prod_{i=1}^r p_i,
$$

并且对于任何两个不可约元分解

$$
a=u\prod_{i=1}^r p_i=u'\prod_{j=1}^s q_j,
$$

都有 $r=s$，且在对指标 $i$ 作一个置换后，有 $p_i=u_iq_i$，其中 $u_i$ 是 $A$ 中的某个可逆元，$i=1,\ldots,r$，那么就称 $a$ 具有**唯一的不可约元分解**。

我们注意到，如果 $p$ 不可约，$u$ 是可逆元，那么 $up$ 也不可约，所以分解中必须允许乘以可逆元。在整数环 $\mathbf Z$ 中，利用序关系，可以在两个相差一个可逆因子的不可约元，即 $\pm p$ 中选取正的那个，作为代表不可约元（一个素数）。当然，在更一般的环中不能这样做。

在上述定义中取 $r=0$，我们约定 $A$ 的可逆元具有不可约元分解。

如果一个环是整环，而且每个非零元素都有唯一的不可约元分解，就称它为**唯一分解整环**（也称**唯一分解环**）。下面我们将证明，主理想整环是唯一分解整环。

设 $A$ 为整环，$a,b\in A$，且 $ab\ne0$。如果存在 $c\in A$，使得 $ac=b$，就称 **$a$ 整除 $b$**，记作 $a\mid b$。如果 $d\in A$、$d\ne0$，满足 $d\mid a$、$d\mid b$，并且 $A$ 中任何同时整除 $a$ 和 $b$ 的非零元素 $e$ 都整除 $d$，就称 $d$ 为 $a$ 和 $b$ 的**最大公因子（g.c.d.）**。

<span class="original-page-anchor" id="pdf-page-127" aria-hidden="true"></span>

**命题 5.1。** *设 $A$ 为主理想整环，$a,b\in A$，且 $a,b\ne0$。设 $(a)+(b)=(c)$。那么 $c$ 是 $a$ 和 $b$ 的最大公因子。*

*证明。* 由于 $b$ 属于理想 $(c)$，可以写成 $b=xc$，其中 $x\in A$，所以 $c\mid b$。同理，$c\mid a$。设 $d$ 同时整除 $a$ 和 $b$，并写成 $a=dy$、$b=dz$，其中 $y,z\in A$。由于 $c$ 属于 $(a,b)$，可以写成

$$
c=wa+tb,
$$

其中 $w,t\in A$。于是 $c=w\,dy+t\,dz=d(wy+tz)$，从而 $d\mid c$，命题得证。

**定理 5.2。** *设 $A$ 为主理想整环。那么 $A$ 是唯一分解整环。*

*证明。* 我们首先证明，$A$ 的每个非零元素都有不可约元分解。设 $S$ 为那些生成元没有不可约元分解的非零主理想所构成的集合，并假设 $S$ 非空。取 $(a_1)\in S$。考虑 $S$ 中理想的升链

$$
(a_1)\subsetneq(a_2)\subsetneq\cdots\subsetneq(a_n)\subsetneq\cdots.
$$

我们断言，这样的链不能是无限的。事实上，这条链的并集是 $A$ 的一个理想，它是主理想，不妨设为 $(a)$。生成元 $a$ 必定已经属于链中的某个成员，不妨设为 $(a_n)$，于是有 $(a_n)\subset(a)\subset(a_n)$，从而这条链在 $(a_n)$ 处终止。因此，$S$ 是归纳有序的，并有一个极大元 $(a)$。所以，$A$ 的任何包含 $(a)$ 且不等于 $(a)$ 的理想，都有一个具有不可约元分解的生成元。

注意到 $a$ 不可能是不可约元（否则它已经有一个分解），因此可以写成 $a=bc$，其中 $b$ 和 $c$ 都不是可逆元。但这时 $(b)\ne(a)$ 且 $(c)\ne(a)$，所以 $b,c$ 都有不可约元分解。这两个分解的乘积就是 $a$ 的一个分解，这与 $S$ 非空的假设矛盾。

为证明唯一性，首先注意：如果 $p$ 为 $A$ 的不可约元，且 $a,b\in A$、$p\mid ab$，那么 $p\mid a$ 或 $p\mid b$。*证明：* 如果 $p\nmid a$，那么 $p,a$ 的最大公因子为 $1$，因而可以写成

$$
1=xp+ya,
$$

其中 $x,y\in A$。于是 $b=bxp+yab$，而由 $p\mid ab$ 可推出 $p\mid b$。

假设 $a$ 有两个不可约元分解

$$
a=p_1\cdots p_r=q_1\cdots q_s.
$$

由于 $p_1$ 整除最右边的乘积，它就整除其中的某个因子。重新编号后，可以假设该因子为 $q_1$。于是存在一个可逆元 $u_1$，使得 $q_1=u_1p_1$。现在可以从两个分解中约去 $p_1$，得到

<span class="original-page-anchor" id="pdf-page-128" aria-hidden="true"></span>

$$
p_2\cdots p_r=u_1q_2\cdots q_s.
$$

用归纳法即可完成证明。

如果存在可逆元 $u$，使得 $a=bu$，就可以称两个元素 $a,b\in A$ 等价。从每个不可约元所属的等价类中选取一个不可约元 $p$，以 $P$ 表示这些代表元构成的集合。设 $a\in A$、$a\ne0$。那么存在可逆元 $u$ 和整数 $v(p)\ge0$，其中除有限多个 $p\in P$ 外，其余的 $v(p)$ 均为 $0$，使得

$$
a=u\prod_{p\in P}p^{v(p)}.
$$

而且，可逆元 $u$ 和整数 $v(p)$ 均由 $a$ 唯一确定。我们称 $v(p)$ 为 **$a$ 在 $p$ 处的阶**，也记作 $\operatorname{ord}_p a$。

如果 $A$ 是唯一分解整环，那么不可约元 $p$ 生成素理想 $(p)$。因此，在唯一分解整环中，不可约元也称为**素元素**，或简称**素元**。

注意，可以用通常的方式定义 $A$ 中有限个非零元素的**最小公倍数**（l.c.m.）：如果

$$
a_1,\ldots,a_n\in A
$$

是这些元素，那么把任何满足下述条件的 $c\in A$ 定义为它们的一个最小公倍数：对 $A$ 的所有素元 $p$，都有

$$
\operatorname{ord}_p c=\max_i\operatorname{ord}_p a_i.
$$

这个元素 $c$ 在相差一个可逆因子的意义下确定。

如果 $a,b\in A$ 为非零元素，且 $a$ 和 $b$ 的最大公因子是可逆元，就称 $a,b$ **互素**。

**例。** 整数环 $\mathbf Z$ 是唯一分解整环。它的可逆元群由 $1$ 和 $-1$ 组成。从 $p$ 和 $-p$ 这两个可能的选择中，取正的素元（即所谓的素数）$p$ 作为代表素元，是很自然的。类似地，我们将在后面说明，域上的一元多项式环是唯一分解整环，并且选取首项系数为 $1$ 的不可约多项式作为素元的代表。

**例。** 在第四章中将证明，如果 $R$ 是唯一分解整环，那么 $n$ 元多项式环 $R[X_1,\ldots,X_n]$ 也是唯一分解整环。特别地，如果 $k$ 是域，那么多项式环 $k[X_1,\ldots,X_n]$ 是唯一分解整环。注意，$k[X_1]$ 是主理想整环，但当 $n\ge2$ 时，环 $k[X_1,\ldots,X_n]$ 不是主理想整环。

在习题 5 中，你将证明唯一分解整环的局部化仍是唯一分解整环。

在第四章 §9 中，我们将证明幂级数环 $k[[X_1,\ldots,X_n]]$ 是唯一分解整环。这个结果是一个更一般的命题——正则局部环是唯一分解整环——的特例，但本书不定义正则局部环。你可以在有关交换<span class="original-page-anchor" id="pdf-page-129" aria-hidden="true"></span>代数的书籍中查阅。我推荐：

H. MATSUMURA，《交换代数》（*Commutative Algebra*），第二版，Benjamin-Cummings，纽约，1980 年。

H. MATSUMURA，《交换环》（*Commutative Rings*），剑桥大学出版社，英国剑桥，1986 年。

**来自代数几何和复几何的例子。** 粗略地说，正则局部环出现在代数几何或复几何的如下背景中。考虑复流形或代数流形上某一点的邻域中的正则函数环。这个环是正则的。一个典型的例子是 $\mathbf C$ 中 $0$ 的某邻域内的收敛幂级数环。在第四章中，我们将证明一些关于幂级数的结果，它们为这些解析理论提供代数背景，并用于证明幂级数环的唯一分解性，无论这些幂级数是否收敛。

与上述例子相反，几何理论中的奇点可能产生不具有唯一分解性的例子。我们给出几个例子，其中用到的概念都足够基础，读者应该已在更初等的课程中接触过。

**非唯一分解环的例子。** 设 $k$ 为域，$x$ 为 $k$ 上的变量。令 $R=k[x^2,x^3]$。那么 $R$ 不是唯一分解整环（如何证明？）。可以把环 $R$ 看作曲线 $y^2=x^3$ 上的正则函数环。这条曲线在原点有一个奇点，画出它的实图像便能看出来。

设 $R$ 为所有形如 $a+b\sqrt{-5}$ 的数所构成的集合，其中 $a,b\in\mathbf Z$。那么 $R$ 的可逆元只有 $\pm1$，而元素 $3$、$2+\sqrt{-5}$、$2-\sqrt{-5}$ 都是不可约元，由此得到一个不唯一的分解

$$
3^2=(2+\sqrt{-5})(2-\sqrt{-5}).
$$

（做习题 10。）这里的不具有唯一分解性并非由奇点造成，而是因为 $R$ 的理想类群非平凡；$R$ 是戴德金环。有关定义，可参见第三章的习题，或直接阅读我的《代数数论》（*Algebraic Number Theory*）一书等。

正如 Trotter 曾指出的（*Math. Monthly*，1988 年 4 月），关系式

$$
\sin^2 x=(1+\cos x)(1-\cos x)
$$

可以看作三角多项式环 $\mathbf R[\sin x,\cos x]$ 中的一个不唯一的分解；这个环是在 $\mathbf R$ 上由函数 $\sin x$ 和 $\cos x$ 生成的。它是所有函数构成的环的子环，也可视为所有可微函数构成的环的子环。参见习题 11。

## 习题

*以 $A$ 表示交换环。*

**1.** 假设在 $A$ 中有 $1\ne0$。设 $S$ 为 $A$ 的一个不含 $0$ 的乘法子集。设 $\mathfrak p$ 为 $A$ 的那些与 $S$ 的交集为空的理想所构成的集合中的一个极大元。证明 $\mathfrak p$ 是素理想。

<span class="original-page-anchor" id="pdf-page-130" aria-hidden="true"></span>

**2.** 设 $f:A\to A'$ 为满的环同态，并假设 $A$ 是局部环，$A'\ne0$。证明 $A'$ 是局部环。

**3.** 设 $\mathfrak p$ 为 $A$ 的素理想。证明 $A_{\mathfrak p}$ 有唯一的极大理想，它由所有满足 $a\in\mathfrak p$、$s\notin\mathfrak p$ 的元素 $a/s$ 构成。

**4.** 设 $A$ 为主理想整环，$S$ 为乘法子集，且 $0\notin S$。证明 $S^{-1}A$ 是主理想整环。

**5.** 设 $A$ 为唯一分解整环，$S$ 为乘法子集，且 $0\notin S$。证明 $S^{-1}A$ 是唯一分解整环，并且 $S^{-1}A$ 的素元具有形式 $up$，其中 $p$ 是满足 $(p)\cap S$ 为空集的 $A$ 的素元，$u$ 是 $S^{-1}A$ 中的可逆元。

**6.** 设 $A$ 为唯一分解整环，$p$ 为素元。证明局部环 $A_{(p)}$ 是主理想整环。

**7.** 设 $A$ 为主理想整环，$a_1,\ldots,a_n$ 为 $A$ 的非零元素。设 $(a_1,\ldots,a_n)=(d)$。证明 $d$ 是这些 $a_i$（$i=1,\ldots,n$）的最大公因子。

**8.** 设 $p$ 为素数，$A$ 为环 $\mathbf Z/p^r\mathbf Z$（$r$ 为满足 $r\ge1$ 的整数）。设 $G$ 为 $A$ 的可逆元群，即与 $p$ 互素的整数模 $p^r$ 所构成的群。证明，$G$ 是循环群，只有如下情形例外：

$$
p=2,\qquad r\ge3;
$$

在此情形下，它的型为 $(2,2^{r-2})$。［*提示：* 在一般情形下，证明 $G$ 是由 $1+p$ 生成的循环群与一个阶为 $p-1$ 的循环群的乘积。在例外情形下，证明 $G$ 是群 $\{\pm1\}$ 与由 $5\bmod 2^r$ 的剩余类生成的循环群的乘积。］

**9.** 设 $i$ 为复数 $\sqrt{-1}$。证明环 $\mathbf Z[i]$ 是主理想整环，因而是唯一分解整环。它的可逆元有哪些？

**10.** 设 $D$ 为满足 $D\ge1$ 的整数，$R$ 为所有形如 $a+b\sqrt{-D}$ 的元素所构成的集合，其中 $a,b\in\mathbf Z$。

(a) 证明 $R$ 是环。

(b) 利用复共轭是 $\mathbf C$ 的自同构这一事实，证明复共轭诱导 $R$ 的一个自同构。

(c) 证明，如果 $D\ge2$，那么 $R$ 中的可逆元只有 $\pm1$。

(d) 证明 $3$、$2+\sqrt{-5}$、$2-\sqrt{-5}$ 是 $\mathbf Z[\sqrt{-5}]$ 中的不可约元。

**11.** 设 $R$ 为正文中定义的三角多项式环。证明 $R$ 由 $\mathbf R$ 上所有可表示为下列形式的函数 $f$ 构成：

$$
f(x)=a_0+\sum_{m=1}^n(a_m\cos mx+b_m\sin mx),
$$

其中 $a_0,a_m,b_m$ 为实数。把**三角次数** $\deg_{\mathrm{tr}}(f)$ 定义为满足 $a_r,b_s\ne0$ 的整数 $r,s$ 的最大值。证明

$$
\deg_{\mathrm{tr}}(fg)=\deg_{\mathrm{tr}}(f)+\deg_{\mathrm{tr}}(g).
$$

由此推出 $R$ 没有零因子，并且推出函数 $\sin x$ 和 $1-\cos x$ 都是这个环中的不可约元。

<span class="original-page-anchor" id="pdf-page-131" aria-hidden="true"></span>

**12.** 设 $P$ 为正整数的集合，$R$ 为定义在 $P$ 上、取值于交换环 $K$ 的函数的集合。把 $R$ 中的和定义为通常的函数相加，并用公式

$$
(f*g)(m)=\sum_{xy=m}f(x)g(y)
$$

定义**卷积乘积**，其中求和遍历所有满足 $xy=m$ 的正整数对 $(x,y)$。

(a) 证明 $R$ 是交换环，其单位元为函数 $\delta$，满足 $\delta(1)=1$，且当 $x\ne1$ 时，$\delta(x)=0$。

(b) 如果每当 $m,n$ 互素时，都有 $f(mn)=f(m)f(n)$，就称函数 $f$ 是**积性函数**。如果 $f,g$ 为积性函数，证明 $f*g$ 也是积性函数。

(c) 设 $\mu$ 为**莫比乌斯函数**，满足 $\mu(1)=1$；当 $p_1,\ldots,p_r$ 为互不相同的素数时，$\mu(p_1\cdots p_r)=(-1)^r$；而当 $m$ 被某个素数 $p$ 的平方 $p^2$ 整除时，$\mu(m)=0$。证明 $\mu*\varphi_1=\delta$，其中 $\varphi_1$ 表示值恒为 $1$ 的常值函数。［*提示：* 先证明 $\mu$ 是积性函数，再对素数幂证明所述断言。］初等数论中的莫比乌斯反演公式正是关系式 $\mu*\varphi_1*f=f$。

### 戴德金环

证明关于戴德金环 $\mathfrak o$ 的下列命题。为简化术语，除非另有说明，**理想**均指非零理想。以 $K$ 表示 $\mathfrak o$ 的商域。

**13.** 每个理想都是有限生成的。［*提示：* 给定理想 $\mathfrak a$，设 $\mathfrak b$ 为满足 $\mathfrak a\mathfrak b=\mathfrak o$ 的分式理想。写成 $1=\sum a_i b_i$，其中 $a_i\in\mathfrak a$、$b_i\in\mathfrak b$。证明 $\mathfrak a=(a_1,\ldots,a_n)$。］

**14.** 每个理想都有素理想乘积分解，且此分解在相差一个置换的意义下唯一确定。

**15.** 假设 $\mathfrak o$ 只有一个素理想 $\mathfrak p$。取 $t\in\mathfrak p$，且 $t\notin\mathfrak p^2$。那么 $\mathfrak p=(t)$ 是主理想。

**16.** 设 $\mathfrak o$ 为任意戴德金环，$\mathfrak p$ 为素理想。设 $\mathfrak o_{\mathfrak p}$ 为在 $\mathfrak p$ 处的局部环。那么 $\mathfrak o_{\mathfrak p}$ 是戴德金环，且只有一个素理想。

**17.** 与整数的情形一样，如果存在理想 $\mathfrak c$，使得 $\mathfrak b=\mathfrak a\mathfrak c$，就称 $\mathfrak a\mid\mathfrak b$（**$\mathfrak a$ 整除 $\mathfrak b$**）。证明：

(a) $\mathfrak a\mid\mathfrak b$ 当且仅当 $\mathfrak b\subset\mathfrak a$。

(b) 设 $\mathfrak a,\mathfrak b$ 为理想。那么 $\mathfrak a+\mathfrak b$ 是它们的最大公因子。特别地，$\mathfrak a,\mathfrak b$ 互素，当且仅当 $\mathfrak a+\mathfrak b=\mathfrak o$。

**18.** 每个素理想 $\mathfrak p$ 都是极大理想。（记住，根据约定，$\mathfrak p\ne0$。）特别地，如果 $\mathfrak p_1,\ldots,\mathfrak p_n$ 为互不相同的素理想，那么中国剩余定理适用于它们的幂 $\mathfrak p_1^{r_1},\ldots,\mathfrak p_n^{r_n}$。利用这一点证明：

**19.** 设 $\mathfrak a,\mathfrak b$ 为理想。证明存在元素 $c\in K$（$K$ 为 $\mathfrak o$ 的商域），使得 $c\mathfrak a$ 是与 $\mathfrak b$ 互素的理想。特别地，$\operatorname{Pic}(\mathfrak o)$ 中的每个理想类，都含有与某个给定理想互素的代表理想。

有关后续内容，参见第七章习题 7，以及第三章习题 11–13。
