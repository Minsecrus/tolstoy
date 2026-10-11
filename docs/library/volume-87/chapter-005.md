---
title: "第五章 极限"
description: "Tom Leinster《Basic Category Theory》中文译文。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"第四章 可表函子","link":"/library/volume-87/chapter-004"}
next: {"text":"第六章 伴随函子、可表函子与极限","link":"/library/volume-87/chapter-006"}
---

# 第五章 极限

<span class="original-page-anchor" id="pdf-page-116" aria-hidden="true"></span>

极限及其对偶概念余极限，为我们提供了理解泛性质这一思想的第三种途径。

伴随性讨论的是范畴*之间*的关系。可表性是*集合值*函子的一种性质。极限讨论的是范畴*内部*发生的事情。

极限的概念统一了数学中许多熟悉的构造。每当你遇到一种方法，从某个范畴中的一些对象和态射出发，由它们构造一个新对象时，你看到的很可能就是极限或余极限。例如，在群论中，我们可以取两个群之间的一个同态，并构造它的核，这是一个新的群。这个构造是群范畴中的极限的一个例子。或者，我们可以取两个自然数并构造它们的最小公倍数。这是以整除关系为序的自然数偏序集中的余极限的一个例子。

## 5.1 极限：定义与例子

极限的定义非常一般。我们先考察几种特别有用的极限：积、等化子和拉回，再逐步引出这个定义。

### 积

设 $X$ 与 $Y$ 是集合。熟悉的笛卡尔积 $X\times Y$ 的特征是：$X\times Y$ 的一个元素，就是 $X$ 的一个元素连同 $Y$ 的一个元素。由于元素就是从 $1$ 出发的映射，这就是说，一个映射 $1\to X\times Y$ 等同于一个映射 $1\to X$ 连同一个映射 $1\to Y$。

稍加思考就会发现，当所有的 $1$ 都被替换为<span class="original-page-anchor" id="pdf-page-117" aria-hidden="true"></span>任意集合 $A$ 时，同样成立。（换句话说，$X\times Y$ 的一个形状为 $A$ 的广义元素，等同于 $X$ 的一个形状为 $A$ 的广义元素连同 $Y$ 的一个形状为 $A$ 的广义元素。）

$$
\text{映射 }A\to X\times Y
$$

与

$$
\text{映射对 }(A\to X,\ A\to Y)
$$

之间的双射，由与投影映射复合给出：

![投影映射及其在元素上的作用](/library/volume-87/diagrams/pdf-0117-projections.png)

这启发了以下定义。

**定义 5.1.1** 设 $\mathscr{A}$ 是范畴，$X,Y\in\mathscr{A}$。$X$ 与 $Y$ 的一个**积**由对象 $P$ 以及态射

![积的投影](/library/volume-87/diagrams/pdf-0117-product.png)

组成，具有如下性质：对 $\mathscr{A}$ 中任意对象和态射

![对象与态射（5.1）](/library/volume-87/diagrams/pdf-0117-cone-5-1.png)

都存在唯一态射 $\bar f:A\to P$，使得

![泛性质（5.2）](/library/volume-87/diagrams/pdf-0117-universal-5-2.png)

交换。态射 $p_1$ 和 $p_2$ 称为**投影**。

**注 5.1.2** (a) 积并不总是存在。例如，如果 $\mathscr{A}$ 是离散的双对象范畴

![离散的双对象范畴](/library/volume-87/diagrams/pdf-0117-discrete.png)

<span class="original-page-anchor" id="pdf-page-118" aria-hidden="true"></span>

那么 $X$ 和 $Y$ 就没有积。但是，当一个范畴中的对象 $X$ 和 $Y$ 确实有积时，它在相差同构的意义下是唯一的。（这可以直接证明，方法与引理 2.1.8 很相似。它也由推论 6.1.2 得出。）因此，称它为 $X$ 与 $Y$ 的积是有依据的。

(b) 严格地说，积由对象 $P$ *连同*投影 $p_1$ 与 $p_2$ 组成。但在非正式用语中，我们常常仅把 $P$ 称为 $X$ 与 $Y$ 的积。我们把 $P$ 写作 $X\times Y$。

**例 5.1.3** 任意两个集合 $X$ 与 $Y$ 在 $\mathbf{Set}$ 中都有积。它就是通常的笛卡尔积 $X\times Y$，配备通常的投影映射 $p_1$ 与 $p_2$。

我们来验证它确实是定义 5.1.1 意义下的积。取图（5.1）中的集合与函数。定义 $\bar f:A\to X\times Y$ 为 $\bar f(a)=(f_1(a),f_2(a))$。那么对 $i=1,2$ 有 $p_i\circ\bar f=f_i$；也就是说，取 $P=X\times Y$ 时，图（5.2）交换。而且，这是使图（5.2）交换的*唯一*映射。因为，假设用 $\hat f:A\to X\times Y$ 代替 $\bar f$，也使（5.2）交换。设 $a\in A$，并将 $\hat f(a)$ 写成 $(x,y)$。那么

$$
f_1(a)=p_1(\hat f(a))=p_1(x,y)=x,
$$

类似地，$f_2(a)=y$。因此，对所有 $a\in A$ 都有 $\hat f(a)=(f_1(a),f_2(a))=\bar f(a)$，由此得到所需的 $\hat f=\bar f$。

一般而言，在任意范畴中，图（5.2）中的态射 $\bar f$ 通常写成 $(f_1,f_2)$。

**例 5.1.4** 在拓扑空间范畴中，任意两个对象 $X$ 与 $Y$ 都有积。它是集合 $X\times Y$，配备积拓扑与标准投影映射。积拓扑的设计，正是为了使一个函数

$$
\begin{array}{ccc}
A&\to&X\times Y\\
t&\mapsto&(x(t),y(t))
\end{array}
$$

连续当且仅当它在每个坐标上都连续（也就是说，两个函数

$$
t\mapsto x(t),\qquad t\mapsto y(t)
$$

都连续）。这对任意空间 $A$ 都成立，但当 $A=\mathbb{R}$ 且我们将 $t$ 看作时间参数时，这一思想或许最具有直观吸引力。

一个密切相关的陈述是：积拓扑是 $X\times Y$ 上使各投影连续的最小拓扑。这里“最小”的意思是，对于 $X\times Y$ 上使 $p_1$ 与 $p_2$ 连续的任意其他拓扑 $\mathcal{T}$，$X\times Y$ 的每个在积拓扑中是开集的子集，在 $\mathcal{T}$ 中也都是开集。因此，<span class="original-page-anchor" id="pdf-page-119" aria-hidden="true"></span>为了定义积拓扑，我们声明恰好足够多的集合是开集，使各投影连续。

**例 5.1.5** 现在设 $X$ 与 $Y$ 是向量空间。我们可以构造它们的直和 $X\oplus Y$，其中的元素可以按个人喜好写成 $(x,y)$ 或 $x+y$（其中 $x\in X$、$y\in Y$）。有如下线性投影映射：

![线性投影映射](/library/volume-87/diagrams/pdf-0119-vector-product.png)

可以证明，$X\oplus Y$ 连同 $p_1$ 与 $p_2$，就是向量空间范畴中 $X$ 与 $Y$ 的积（习题 5.1.33）。

**例 5.1.6（有序集的元素）** (a) 设 $x,y\in\mathbb{R}$。它们的最小值 $\min\{x,y\}$ 满足

$$
\min\{x,y\}\leq x,\qquad\min\{x,y\}\leq y,
$$

并且还具有如下性质：若 $a\in\mathbb{R}$ 满足

$$
a\leq x,\qquad a\leq y,
$$

那么 $a\leq\min\{x,y\}$。这恰好意味着，当偏序集 $(\mathbb{R},\leq)$ 被看作范畴时，$x,y\in\mathbb{R}$ 的积就是 $\min\{x,y\}$。在偏序集中解释积的定义时，它会简化，因为所有图都交换。

(b) 固定一个集合 $S$。设 $X,Y\in\mathscr{P}(S)$。那么 $X\cap Y$ 满足

$$
X\cap Y\subseteq X,\qquad X\cap Y\subseteq Y,
$$

并且还具有如下性质：若 $A\in\mathscr{P}(S)$ 满足

$$
A\subseteq X,\qquad A\subseteq Y,
$$

那么 $A\subseteq X\cap Y$。这意味着，$X\cap Y$ 就是视作范畴的偏序集 $(\mathscr{P}(S),\subseteq)$ 中 $X$ 与 $Y$ 的积。

(c) 设 $x,y\in\mathbb{N}$。它们的最大公约数 $\gcd(x,y)$ 满足

$$
\gcd(x,y)\mid x,\qquad\gcd(x,y)\mid y
$$

（它是一个公约数！），并且还具有如下性质：若 $a\in\mathbb{N}$ 满足

$$
a\mid x,\qquad a\mid y,
$$

<span class="original-page-anchor" id="pdf-page-120" aria-hidden="true"></span>

那么 $a\mid\gcd(x,y)$。这意味着，$\gcd(x,y)$ 就是视作范畴的偏序集 $(\mathbb{N},\mid)$ 中 $x$ 与 $y$ 的积。

一般地，设 $(A,\leq)$ 是偏序集，$x,y\in A$。$x$ 与 $y$ 的一个**下界**是满足 $a\leq x$ 且 $a\leq y$ 的元素 $a\in A$。$x$ 与 $y$ 的一个**最大下界**或**交**，是它们的一个下界 $z$，并且还具有如下性质：只要 $a$ 是 $x$ 与 $y$ 的下界，就有 $a\leq z$。

当偏序集被看作范畴时，交恰好就是积。它们并不总是存在，但若存在，就是唯一的。$x$ 与 $y$ 的交通常写作 $x\wedge y$，而不是 $x\times y$。因此，在上面的三个例子中，

$$
x\wedge y=\min\{x,y\},\qquad X\wedge Y=X\cap Y,\qquad x\wedge y=\gcd(x,y),
$$

其中第二个例子就是这一记号的来源。

我们一直讨论的是*两个*对象的积 $X\times Y$，即所谓的**二元积**。但没有理由只限于两个。我们同样可以讨论三个对象的积 $X\times Y\times Z$，或无穷多个对象的积。定义按最显然的方式改变：

**定义 5.1.7** 设 $\mathscr{A}$ 是范畴，$I$ 是集合，$(X_i)_{i\in I}$ 是 $\mathscr{A}$ 的一族对象。$(X_i)_{i\in I}$ 的一个**积**由对象 $P$ 和一族态射

$$
\bigl(P\xrightarrow{p_i}X_i\bigr)_{i\in I}
$$

组成，具有如下性质：对任意对象 $A$ 和态射族

$$
\bigl(A\xrightarrow{f_i}X_i\bigr)_{i\in I}\tag{5.3}
$$

都存在唯一态射 $\bar f:A\to P$，使得对所有 $i\in I$ 都有 $p_i\circ\bar f=f_i$。

注 5.1.2 同样适用于这个定义。当积 $P$ 存在时，我们把 $P$ 写作 $\prod_{i\in I}X_i$，并将态射 $\bar f$ 写作 $(f_i)_{i\in I}$。我们称各态射 $f_i$ 为态射 $(f_i)_{i\in I}$ 的**分量**。取 $I$ 为双元素集合，就得到二元积这一特殊情形。

**例 5.1.8** 在有序集中，从二元积推广到任意积的方式是显然的：给定有序集 $(A,\leq)$，元素族 $(x_i)_{i\in I}$ 的一个**下界**是满足对所有 $i$ 都有 $a\leq x_i$ 的元素 $a\in A$；而这一族的一个**最大下界**或**交**，是不小于任何其他下界的下界，记作 $\bigwedge_{i\in I}x_i$。这些就是 $(A,\leq)$ 中的积。

例如，在具有通常次序的 $\mathbb{R}$ 中，元素族 $(x_i)_{i\in I}$ 的交是 $\inf\{x_i\mid i\in I\}$（而且其中一个存在，当且仅当另一个存在）。

**例 5.1.9** 当指标集 $I$ 为空时，积的定义会变成什么样？设 $\mathscr{A}$ 是范畴。一般而言，$\mathscr{A}$ 中以 $I$ 为指标的对象族 $(X_i)_{i\in I}$<span class="original-page-anchor" id="pdf-page-121" aria-hidden="true"></span>就是一个函数 $I\to\operatorname{ob}(\mathscr{A})$。当 $I$ 为空时，恰好有一个这样的函数。换句话说，恰好有一个族 $(X_i)_{i\in\emptyset}$，即**空族**。类似地，当 $I$ 为空时，对于任意给定对象 $A$，都恰好有一个族（5.3）。

因此，空族的一个积由 $\mathscr{A}$ 的对象 $P$ 组成，使得对 $\mathscr{A}$ 的每个对象 $A$，都存在唯一态射 $\bar f:A\to P$。（条件“对所有 $i\in I$ 都有 $p_i\circ\bar f=f_i$”平凡地成立。）换句话说，空族的积恰好就是终对象。

我们一直用 $1$ 表示终对象，其依据是：在 $\mathbf{Set}$、$\mathbf{Top}$、$\mathbf{Ring}$ 和 $\mathbf{Grp}$ 等范畴中，终对象只有一个元素。但是我们刚刚看到，终对象是零个东西的积；而在初等算术中，这就是数 $1$。这是使用这一记号的第二个相关理由。

**例 5.1.10** 取一个范畴 $\mathscr{A}$ 的对象 $X$，以及一个集合 $I$。有一个常值族 $(X)_{i\in I}$。若它的积 $\prod_{i\in I}X$ 存在，就记作 $X^I$，称为 $X$ 的一个**幂**。

我们在第 3.1 节中见过 $\mathbf{Set}$ 中的幂。当 $X$ 是集合时，$X^I$ 是从 $I$ 到 $X$ 的函数的集合，也记作 $\mathbf{Set}(I,X)$。

### 等化子

为了定义第二种极限，我们需要先引入一个术语：范畴中的一个**叉**由对象和态射

![叉（5.4）](/library/volume-87/diagrams/pdf-0121-fork-5-4.png)

组成，使得 $sf=tf$。

**定义 5.1.11** 设 $\mathscr{A}$ 是范畴，$X\overset{s}{\underset{t}{\rightrightarrows}}Y$ 是 $\mathscr{A}$ 中的对象和态射。$s$ 与 $t$ 的一个**等化子**是对象 $E$ 连同态射 $E\xrightarrow{i}X$，使得

![等化子之叉](/library/volume-87/diagrams/pdf-0121-equalizer.png)

是一个叉，并且具有如下性质：对任意叉（5.4），都存在唯一态射 $\bar f:A\to E$，使得

![等化子的泛性质（5.5）](/library/volume-87/diagrams/pdf-0121-universal-5-5.png)

<span class="original-page-anchor" id="pdf-page-122" aria-hidden="true"></span>

交换。

关于积的注 5.1.2 也适用于等化子。

**例 5.1.12** 我们已经在 $\mathbf{Set}$ 中见过等化子（第 3.1 节）。它们确实是定义 5.1.11 意义下的等化子。事实上，取集合和函数 $X\overset{s}{\underset{t}{\rightrightarrows}}Y$，记

$$
E=\{x\in X\mid s(x)=t(x)\},
$$

并用 $i:E\to X$ 表示包含映射。那么 $si=ti$，所以我们有一个叉，而且可以验证它在 $s$ 与 $t$ 上的所有叉之中具有泛性质。

一个等化子描述一个方程的解集，但把等化子与积结合起来，我们也能描述任意联立方程组的解集。取集合 $\Lambda$ 以及 $\mathbf{Set}$ 中的态射对族

![态射对族](/library/volume-87/diagrams/pdf-0122-family.png)

那么解集

$$
\{x\in X\mid \text{对所有 }\lambda\in\Lambda\text{ 都有 }s_\lambda(x)=t_\lambda(x)\}
$$

就是以下函数的等化子：

![到积的函数](/library/volume-87/diagrams/pdf-0122-product-pair.png)

（使用定义 5.1.7 后引入的记号）。为说明这一点，注意对 $x\in X$ 有

$$
\begin{aligned}
(s_\lambda)_{\lambda\in\Lambda}(x)=(t_\lambda)_{\lambda\in\Lambda}(x)
&\iff\bigl(s_\lambda(x)\bigr)_{\lambda\in\Lambda}=\bigl(t_\lambda(x)\bigr)_{\lambda\in\Lambda}\\
&\iff\text{对所有 }\lambda\in\Lambda\text{ 都有 }s_\lambda(x)=t_\lambda(x),
\end{aligned}
$$

这就是所需的结论。

**例 5.1.13** 取拓扑空间之间的连续映射 $X\overset{s}{\underset{t}{\rightrightarrows}}Y$。我们可以在集合范畴中构造它们的等化子 $E$，设包含映射为 $i:E\to X$。由于 $E$ 是空间 $X$ 的子集，它从 $X$ 获得子空间拓扑，于是 $i$ 连续。空间 $E$ 连同 $i$，就是 $s$ 与 $t$ 的等化子。

证明这一点，等同于证明对 $\mathbf{Top}$ 中任意叉（5.4），所诱导的函数 $\bar f$ 都连续。这由子空间拓扑的定义得出：它是使包含映射连续的最小拓扑。可与例 5.1.4 中关于积的说明相比较。

<span class="original-page-anchor" id="pdf-page-123" aria-hidden="true"></span>

**例 5.1.14** 设 $\theta:G\to H$ 是群同态。如例 0.8，同态 $\theta$ 产生一个叉

![核构成的叉](/library/volume-87/diagrams/pdf-0123-kernel.png)

其中 $\iota$ 是包含映射，$\varepsilon$ 是平凡同态。这是 $\mathbf{Grp}$ 中的等化子。要证明这一点，只需证明我们一直称作 $\bar f$ 的态射是同态；这留给读者完成。

因此，核是等化子的一个特殊情形。

**例 5.1.15** 设 $V\overset{s}{\underset{t}{\rightrightarrows}}W$ 是向量空间之间的线性映射。有一个线性映射 $t-s:V\to W$，而向量空间范畴中 $s$ 与 $t$ 的等化子，就是空间 $\ker(t-s)$ 连同包含映射 $\ker(t-s)\hookrightarrow V$。

### 拉回

在给出一般定义之前，我们再探讨一种极限。

**定义 5.1.16** 设 $\mathscr{A}$ 是范畴，并取 $\mathscr{A}$ 中的对象与态射

![拉回的起始图（5.6）](/library/volume-87/diagrams/pdf-0123-corner-5-6.png)

这个图的一个**拉回**是对象 $P\in\mathscr{A}$ 连同态射 $p_1:P\to X$ 和 $p_2:P\to Y$，使得

![拉回方形（5.7）](/library/volume-87/diagrams/pdf-0123-square-5-7.png)

交换，并且具有如下性质：对于任意交换方形

![交换方形（5.8）](/library/volume-87/diagrams/pdf-0123-cone-5-8.png)

<span class="original-page-anchor" id="pdf-page-124" aria-hidden="true"></span>

（在 $\mathscr{A}$ 中），都存在唯一态射 $\bar f:A\to P$，使得

![拉回的泛性质（5.9）](/library/volume-87/diagrams/pdf-0124-universal-5-9.png)

交换。（图（5.9）交换只意味着 $p_1\bar f=f_1$ 与 $p_2\bar f=f_2$，因为其中方形的交换性已经给定。）

注 5.1.2 再次适用。

我们称（5.7）为一个**拉回方形**。拉回也称为**纤维积**。下面的事实部分解释了这个名称：当 $Z$ 是终对象时（此时 $s$ 和 $t$ 分别只能是唯一可能的态射），图（5.6）的一个拉回就是 $X$ 与 $Y$ 的一个积。

**例 5.1.17（$\mathbf{Set}$ 中的拉回）** $\mathbf{Set}$ 中图（5.6）的拉回是

$$
P=\{(x,y)\in X\times Y\mid s(x)=t(y)\},
$$

其中投影 $p_1$ 与 $p_2$ 由 $p_1(x,y)=x$ 和 $p_2(x,y)=y$ 给出。

虽然你可能不熟悉 $\mathbf{Set}$ 中的一般拉回，但至少有两个实例是你很可能见过的。

(a) 集合与函数的一个基本构造是取逆像。它们就是拉回的实例。事实上，给定函数 $f:X\to Y$ 和子集 $Y'\subseteq Y$，我们得到一个新集合，即逆像

$$
f^{-1}Y'=\{x\in X\mid f(x)\in Y'\}\subseteq X,
$$

以及一个新函数

$$
\begin{array}{cccc}
f':&f^{-1}Y'&\to&Y'\\
&x&\mapsto&f(x).
\end{array}
$$

此外，我们还有包含函数 $j:Y'\hookrightarrow Y$ 和 $i:f^{-1}Y'\hookrightarrow X$。把这些合在一起，就得到一个交换方形

![逆像方形（5.10）](/library/volume-87/diagrams/pdf-0124-inverse-5-10.png)

<span class="original-page-anchor" id="pdf-page-125" aria-hidden="true"></span>

我们起初给定的数据，是这个方形的右下部分（$X$、$Y$、$Y'$、$f$ 和 $j$）；从这些数据出发，我们构造出了方形的其余部分（$f^{-1}Y'$、$f'$ 和 $i$）。

方形（5.10）是一个拉回。我们来详细验证这一点。取任意交换方形

![逆像对应的交换方形](/library/volume-87/diagrams/pdf-0125-cone.png)

我们必须证明，存在唯一态射 $k:A\to f^{-1}Y'$，使得

![逆像的泛性质](/library/volume-87/diagrams/pdf-0125-universal.png)

交换。先证唯一性：设 $k$ 是使此图交换的态射。那么对所有 $a\in A$，都有 $i(k(a))=g(a)$，也就是说 $k(a)=g(a)$，从而唯一地确定了 $k$。再证存在性：首先注意，对所有 $a\in A$，都有 $f(g(a))=j(h(a))\in Y'$，所以 $g(a)\in f^{-1}Y'$。因此，我们可以对所有 $a\in A$ 用 $k(a)=g(a)$ 定义 $k:A\to f^{-1}Y'$。于是对所有 $a\in A$，都有 $i(k(a))=k(a)=g(a)$ 以及

$$
f'(k(a))=f(k(a))=f(g(a))=j(h(a))=h(a).
$$

因此 $i\circ k=g$ 且 $f'\circ k=h$，这就是所需的结论。

(b) 子集的交提供了拉回的另一个例子。事实上，设 $X$ 与 $Y$ 是集合 $Z$ 的子集。那么

![作为拉回的交集](/library/volume-87/diagrams/pdf-0125-intersection.png)

是一个拉回方形，其中所有箭头都是子集的包含映射。

事实上，这是 (a) 的一个特殊情形，因为 $X\cap Y$ 就是 $Y\subseteq Z$ 在包含映射 $X\hookrightarrow Z$ 下的逆像。

<span class="original-page-anchor" id="pdf-page-126" aria-hidden="true"></span>

在例 5.1.17(a) 的情形中，我们有映射 $f:X\to Y$ 和 $Y$ 的子集 $Y'$。人们有时会说，$f^{-1}Y'$ 是沿着 $f$ 把 $Y'$“拉回”得到的；名称便由此而来。

### 极限的定义

我们已经考察了三种构造：积、等化子和拉回。它们显然有共同之处。每种构造都从一些对象出发，而等化子和拉回还给定了这些对象之间的一些态射。每种构造的目标都是构造一个新对象，连同从它到原来各对象的一些态射，并使它们具有泛性质。

我们来仔细分析一下。每种构造的起始数据是什么？对于（二元）积，是一对对象

$$
X\qquad Y.\tag{5.11}
$$

对于等化子，是一个图

![等化子的起始数据（5.12）](/library/volume-87/diagrams/pdf-0126-equalizer-5-12.png)

对于拉回，是一个图

![拉回的起始数据（5.13）](/library/volume-87/diagrams/pdf-0126-pullback-5-13.png)

在定义 4.1.25 中，我们介绍了广义元素的概念，并看到几何对象中的“图形”往往可以由映入其中的映射来描述。例如，拓扑空间 $A$ 中的一条曲线，可以看作映射 $\mathbb{R}\to A$。类似地，范畴 $\mathscr{A}$ 的一个对象，等同于一个函子 $D:\mathbf{1}\to\mathscr{A}$；可以把 $\mathbf{1}=\boxed{\bullet}$ 看作一个没有标记的对象，而 $D$ 则用 $\mathscr{A}$ 的某个对象的名称给它加上标记。再类似地，范畴 $\mathscr{A}$ 中的一个态射，就是一个函子 $\mathbf{2}\to\mathscr{A}$，其中 $\mathbf{2}=\boxed{\bullet\to\bullet}$。（这里 $\mathbf{2}$ 是具有两个对象的范畴，不妨称这两个对象为 $0$ 和 $1$；其中有一个态射 $0\to1$，而除恒等态射外没有其他态射。）最后，如果取 $\mathbf{I}$ 为下列范畴之一

![极限的形状范畴（5.14）](/library/volume-87/diagrams/pdf-0126-shapes-5-14.png)

那么函子 $\mathbf{I}\to\mathscr{A}$ 就分别由 $\mathscr{A}$ 中的数据（5.11）、（5.12）或（5.13）组成。

<span class="original-page-anchor" id="pdf-page-127" aria-hidden="true"></span>

![极限的定义](/library/volume-87/diagrams/pdf-0127-limit-figure.png)

图 5.1 极限的定义。

我们刚开始采用这样的约定：一种字体（$\mathbf{A},\mathbf{B},\mathbf{C},\ldots$）表示小范畴，另一种字体（$\mathscr{A},\mathscr{B},\mathscr{C},\ldots$）表示任意范畴。虽然这不是严格必需的，但这一约定很有帮助，因为小范畴与任意范畴在理论中往往扮演不同的角色。

**定义 5.1.18** 设 $\mathscr{A}$ 是范畴，$\mathbf{I}$ 是小范畴。函子 $\mathbf{I}\to\mathscr{A}$ 称为 $\mathscr{A}$ 中一个**形状为 $\mathbf{I}$ 的图**。

所以（5.11）、（5.12）和（5.13）分别是形状为 $\mathbf{T}$、$\mathbf{E}$ 和 $\mathbf{P}$ 的图。

我们已经定义了形状为 $\mathbf{T}$ 的图的积、形状为 $\mathbf{E}$ 的图的等化子，以及形状为 $\mathbf{P}$ 的图的拉回。现在，我们用极限的定义将它们统一起来（图 5.1）。

**定义 5.1.19** 设 $\mathscr{A}$ 是范畴，$\mathbf{I}$ 是小范畴，$D:\mathbf{I}\to\mathscr{A}$ 是 $\mathscr{A}$ 中的图。

(a) $D$ 上的一个**锥**是对象 $A\in\mathscr{A}$（称为锥的**顶点**），连同 $\mathscr{A}$ 中的一族态射

$$
\bigl(A\xrightarrow{f_I}D(I)\bigr)_{I\in\mathbf{I}}\tag{5.15}
$$

使得对 $\mathbf{I}$ 中的所有态射 $I\xrightarrow{u}J$，三角形

![锥的相容性三角形](/library/volume-87/diagrams/pdf-0127-cone-triangle.png)

都交换。（在这里以及下文中，我们将 $D(u)$ 简写为 $Du$。）

(b) $D$ 的一个**极限**是锥 $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$，具有如下性质：对 $D$ 上任意一个锥（5.15），都存在唯一态射 $\bar f:A\to L$，使得对所有 $I\in\mathbf{I}$ 都有 $p_I\circ\bar f=f_I$。各态射 $p_I$ 称为极限的**投影**。

<span class="original-page-anchor" id="pdf-page-128" aria-hidden="true"></span>

**注 5.1.20** (a) 粗略地说，泛性质的意思是：对于任意 $A\in\mathscr{A}$，态射 $A\to L$ 与 $D$ 上以 $A$ 为顶点的锥一一对应。（任意态射 $g:A\to L$ 都产生一个锥 $\bigl(A\xrightarrow{p_Ig}D(I)\bigr)_{I\in\mathbf{I}}$，而极限的定义就是要求对每个 $A$，这个过程都是双射。）在第 6.1 节中，我们将用这一想法，从可表性的角度重新表述极限的定义。由此可得：极限若存在，则在相差典范同构的意义下唯一（推论 6.1.2）。也可以像引理 2.1.8 那样，用通常的直接论证来证明唯一性。

(b) 如果 $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ 是 $D$ 的极限，我们有时稍微不严格地使用语言，把 $L$（而不是整个锥）称为 $D$ 的极限。为了强调，有时我们把 $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ 称为一个**极限锥**。我们记 $L=\lim_{\leftarrow\mathbf{I}}D$。于是 (a) 可以表述为：

*一个映入 $\lim_{\leftarrow\mathbf{I}}D$ 的态射，就是 $D$ 上的一个锥。*

(c) 从一开始就假设形状范畴 $\mathbf{I}$ 是小范畴，这使我们只讨论正式称为**小极限**的极限。我们很少会关心其他种类的极限。

**例 5.1.21（极限的形状）** 设 $\mathscr{A}$ 是任意范畴。回顾（5.14）中的范畴 $\mathbf{T}$、$\mathbf{E}$ 和 $\mathbf{P}$。

(a) $\mathscr{A}$ 中形状为 $\mathbf{T}$ 的图 $D$，就是 $\mathscr{A}$ 的一对对象 $(X,Y)$。$D$ 上的一个锥是对象 $A$，连同态射 $f_1:A\to X$ 与 $f_2:A\to Y$（如定义 5.1.1），而 $D$ 的一个极限就是 $X$ 与 $Y$ 的一个积。

更一般地，设 $I$ 是集合，并用 $\mathbf{I}$ 表示 $I$ 上的离散范畴。函子 $D:\mathbf{I}\to\mathscr{A}$ 就是以 $I$ 为指标的 $\mathscr{A}$ 的对象族 $(X_i)_{i\in I}$，而 $D$ 的一个极限恰好是这一族 $(X_i)_{i\in I}$ 的一个积。

特别地，唯一函子 $\emptyset\to\mathscr{A}$ 的一个极限，就是 $\mathscr{A}$ 的一个终对象，其中 $\emptyset$ 表示空范畴。

(b) $\mathscr{A}$ 中形状为 $\mathbf{E}$ 的图 $D$，就是 $\mathscr{A}$ 中的一个平行态射对 $X\overset{s}{\underset{t}{\rightrightarrows}}Y$。$D$ 上的一个锥由对象和态射

![平行态射对上的锥](/library/volume-87/diagrams/pdf-0128-parallel-cone.png)

组成，使得 $s\circ f=g$ 且 $t\circ f=g$。但由于 $g$ 由 $f$ 确定，等价地可以说，$D$ 上的一个锥由对象 $A$ 和一个态射 $f:$

<span class="original-page-anchor" id="pdf-page-129" aria-hidden="true"></span>

$A\to X$ 组成，使得

![平行态射对上的叉](/library/volume-87/diagrams/pdf-0129-fork.png)

是一个叉。$D$ 的一个极限，就是 $s$ 与 $t$ 上具有泛性质的叉，也就是 $s$ 与 $t$ 的一个等化子。

(c) $\mathscr{A}$ 中形状为 $\mathbf{P}$ 的图 $D$，由 $\mathscr{A}$ 中的对象和态射

![拉回形状的图](/library/volume-87/diagrams/pdf-0129-corner.png)

组成。作与 (b) 中类似的简化，就可以看到 $D$ 上的一个锥就是一个交换方形（5.8）。$D$ 的一个极限就是一个拉回。

(d) 设 $\mathbf{I}=(\mathbb{N},\leq)^{\mathrm{op}}$。图 $D:\mathbf{I}\to\mathscr{A}$ 由对象和态射

$$
\cdots\xrightarrow{s_3}X_2\xrightarrow{s_2}X_1\xrightarrow{s_1}X_0
$$

组成。例如，假设我们有一个集合 $X_0$ 和一条子集链

$$
\cdots\subseteq X_2\subseteq X_1\subseteq X_0.
$$

这些包含映射在 $\mathbf{Set}$ 中构成上述类型的图，其极限是 $\bigcap_{i\in\mathbb{N}}X_i$。在这种及类似的情形中，极限有时被称为**逆极限**，虽然许多范畴论学者认为这一用法有些过时。

一般地，图 $D$ 的极限就是 $D$ 上的锥所成范畴中的终对象，因此它是 $D$ 上的锥的一个极端实例。“极限”一词可以理解为“在边界上”，而不是表示分析中遇到的那种趋于极限的过程。不过，这两种思想在例 5.1.21(d) 中发生了联系。

到目前为止，我们很少讨论哪些极限存在，只在注 5.1.2(a) 中指出过它们并不总是存在。现在我们证明，在许多熟悉的范畴中，所有极限都确实存在；事实上，我们可以显式地构造它们。

**例 5.1.22** 设 $D:\mathbf{I}\to\mathbf{Set}$。我们来做一个思想实验：如果 $\lim_{\leftarrow\mathbf{I}}D$ 存在，它必定是什么？（我们还不知道<span class="original-page-anchor" id="pdf-page-130" aria-hidden="true"></span>它确实存在。）那么会有

$$
\begin{aligned}
\varprojlim_{\mathbf{I}}D
&\cong\mathbf{Set}\left(1,\varprojlim_{\mathbf{I}}D\right)\\
&\cong\{D\text{ 上以 }1\text{ 为顶点的锥}\}\\
&\cong\Bigl\{(x_I)_{I\in\mathbf{I}}\ \Big|\ \text{对所有 }I\in\mathbf{I},\ x_I\in D(I),\text{ 且 }(Du)(x_I)=x_J\\
&\hspace{5em}\text{对 }\mathbf{I}\text{ 中所有 }I\xrightarrow{u}J\text{ 成立}\Bigr\},
\end{aligned}\tag{5.16}
$$

其中第二个同构来自注 5.1.20(a)，第三个同构来自锥的定义。事实上，(5.16) 确实*就是* $D$ 在 $\mathbf{Set}$ 中的极限，其投影 $p_J:\varprojlim_{\mathbf{I}}D\to D(J)$ 由 $p_J((x_I)_{I\in\mathbf{I}})=x_J$ 给出（习题 5.1.37）。因此，在 $\mathbf{Set}$ 中，所有极限都存在。

**例 5.1.23** 同一个公式给出了 $\mathbf{Grp}$、$\mathbf{Ring}$、$\mathbf{Vect}_k$ 等代数结构范畴中的极限。当然，我们还必须说明集合 (5.16) 上的群、环等结构是什么，不过这完全可以用最直接的方式来做。例如，在 $\mathbf{Vect}_k$ 中，若 $(x_I)_{I\in\mathbf{I}},(y_I)_{I\in\mathbf{I}}\in\varprojlim_{\mathbf{I}}D$，则

$$
(x_I)_{I\in\mathbf{I}}+(y_I)_{I\in\mathbf{I}}=(x_I+y_I)_{I\in\mathbf{I}}.
$$

**例 5.1.24** 同一个公式也给出了 $\mathbf{Top}$ 中的极限。集合 (5.16) 上的拓扑是使各投影映射连续的最小拓扑。

**定义 5.1.25** (a) 设 $\mathbf{I}$ 是小范畴。如果 $\mathscr{A}$ 中每个形状为 $\mathbf{I}$ 的图式 $D$ 都存在极限，就称范畴 $\mathscr{A}$ **具有形状为 $\mathbf{I}$ 的极限**。

(b) 如果一个范畴对所有小范畴 $\mathbf{I}$ 都具有形状为 $\mathbf{I}$ 的极限，就称它**具有所有极限**（更准确地说，**具有小极限**）。

所以，$\mathbf{Set}$、$\mathbf{Top}$、$\mathbf{Grp}$、$\mathbf{Ring}$、$\mathbf{Vect}_k$ 等都具有所有极限。

类似的术语也可以用于特殊种类的极限（例如“具有拉回”）。有限极限这一类尤其重要。按定义，如果一个范畴只含有有限多个态射（此时它也只含有有限多个对象），就称它是**有限的**。**有限极限**是形状为某个有限范畴 $\mathbf{I}$ 的极限。例如，二元积、终对象、等化子和拉回都是有限极限。

下面的结果告诉我们，所有极限都可以由几种熟悉的基本类型的极限构造出来。

**命题 5.1.26** *设 $\mathscr{A}$ 是范畴。*

(a) *如果 $\mathscr{A}$ 具有所有积和等化子，那么 $\mathscr{A}$ 具有所有极限。*

(b) *如果 $\mathscr{A}$ 具有二元积、一个终对象和等化子，那么 $\mathscr{A}$ 具有有限极限。*

<span class="original-page-anchor" id="pdf-page-131" aria-hidden="true"></span>

为理解这个想法，考虑 $\mathbf{Set}$ 中极限的公式 (5.16)。在那里，图式 $D$ 的极限被描述为积 $\prod_{I\in\mathbf{I}}D(I)$ 的一个子集，由满足某些方程的那些元素组成。我们在例 5.1.12 中看到，任何联立方程组的解集都可以通过积和等化子来描述。因此，$\mathbf{Set}$ 中的任意极限都可以用积和等化子来描述。而事实上，这一描述在任何范畴中都有效。

现在我们更仔细地考察这一想法，为证明作准备（习题 5.1.38）。初次阅读的读者可以跳过下面两段，从例 5.1.27 继续。

等式 (5.16) 表明，在 $\mathbf{Set}$ 中，图式 $D:\mathbf{I}\to\mathbf{Set}$ 的极限由这样的元素 $(x_I)_{I\in\mathbf{I}}\in\prod_{I\in\mathbf{I}}D(I)$ 组成：对于 $\mathbf{I}$ 中每个态射 $J\xrightarrow{u}K$，在 $D(K)$ 中都有

$$
(Du)(x_J)=x_K.
$$

对于每个这样的态射 $u$，定义映射

![分量映射](/library/volume-87/diagrams/pdf-0131-component-pair.png)

如下：

$$
s_u((x_I)_{I\in\mathbf{I}})=(Du)(x_J),\qquad t_u((x_I)_{I\in\mathbf{I}})=x_K.
$$

于是 $\varprojlim_{\mathbf{I}}D$ 是由这样的族 $x=(x_I)_{I\in\mathbf{I}}$ 组成的集合：对于 $\mathbf{I}$ 中每个态射 $u$，都有 $s_u(x)=t_u(x)$。由例 5.1.12 可知，$\varprojlim_{\mathbf{I}}D$ 是下列两个映射的等化子：

![积之间的映射](/library/volume-87/diagrams/pdf-0131-product-pair.png)

其中 $s$ 和 $t$ 的分量分别为 $s_u$ 和 $t_u$。

这样，我们已经用积和等化子描述了 $\mathbf{Set}$ 中的任意极限。尽管整个论证都在 $\mathbf{Set}$ 中进行，它仍然提示我们如何在任意范畴中开展同样的工作。沿着这个思路，命题 5.1.26 的证明就很直接，留作习题 5.1.38。

**例 5.1.27** 用 $\mathbf{CptHff}$ 表示紧 Hausdorff 空间和连续映射组成的范畴。拓扑学中的一道经典习题是证明：给定从拓扑空间 $X$ 到 Hausdorff 空间 $Y$ 的连续映射 $s$ 和 $t$，$X$ 的子集 $\{x\in X\mid s(x)=t(x)\}$ 是闭的。由此可知，$\mathbf{CptHff}$ 具有等化子。此外，Tychonoff 定理断言，紧空间的任意积（在 $\mathbf{Top}$ 中）都是紧的；而且容易证明，Hausdorff 空间的任意积（在<span class="original-page-anchor" id="pdf-page-132" aria-hidden="true"></span>$\mathbf{Top}$ 中）都是 Hausdorff 的。由此可知，$\mathbf{CptHff}$ 具有所有积。所以由命题 5.1.26(a)，$\mathbf{CptHff}$ 具有所有极限。

**例 5.1.28** 回忆例 5.1.15，核给出了 $\mathbf{Vect}_k$ 中的等化子。由命题 5.1.26(b)，$\mathbf{Vect}_k$ 中的有限极限总可以用 $\oplus$（二元直和）、$\{0\}$ 和核来表达。在 $\mathbf{Ab}$ 中也是如此。

### 单态射

对集合之间的函数而言，单射性是一个重要概念。对于任意范畴中的态射，单射性没有意义，不过有一个概念发挥着类似的作用。

**定义 5.1.29** 设 $\mathscr{A}$ 是范畴。如果对所有对象 $A$ 和态射 $A\overset{x}{\underset{x'}{\rightrightarrows}}X$ 都有

$$
f\circ x=f\circ x'\implies x=x',
$$

就称 $\mathscr{A}$ 中的态射 $X\xrightarrow{f}Y$ 是**单态射**（monic 或 monomorphism）。

用广义元素的语言，可以更直观地重述这个定义：如果对于 $X$ 的所有（形状相同的）广义元素 $x$ 和 $x'$，都有 $fx=fx'\implies x=x'$，那么 $f$ 就是单态射。因此，单态射性就是单射性在广义元素意义下的对应概念。

**例 5.1.30** 在 $\mathbf{Set}$ 中，一个态射是单态射当且仅当它是单射。事实上，若 $f$ 是单射，它当然是单态射；对于逆命题，取 $A=1$ 即可。

**例 5.1.31** 在 $\mathbf{Grp}$、$\mathbf{Vect}_k$、$\mathbf{Ring}$ 等代数结构范畴中，单态射也恰好就是单射。同样，容易证明单射是单态射。对于逆命题，取 $A=F(1)$，其中 $F$ 是自由函子（例 2.1.3）。

为什么单态射的定义会出现在讨论极限的一章里？原因如下：

**引理 5.1.32** *态射 $X\xrightarrow{f}Y$ 是单态射，当且仅当方形*

![单态射的拉回方形](/library/volume-87/diagrams/pdf-0132-monic-pullback.png)

*是拉回。*

**证明** 习题 5.1.41。$\square$<span class="original-page-anchor" id="pdf-page-133" aria-hidden="true"></span>这个引理的意义在于，每当我们证明一个关于极限的结果，就会随之得到一个关于单态射的结果。例如，我们很快会证明，从 $\mathbf{Grp}$、$\mathbf{Vect}_k$ 等到 $\mathbf{Set}$ 的遗忘函子保持极限（其含义稍后定义）；由此立即可知，它们也保持单态射。这又给出了这些范畴中的单态射是单射的另一种证明。

### 习题

**5.1.33** 验证在向量空间范畴中，两个向量空间的积是它们的直和（例 5.1.5）。

**5.1.34** 在某个范畴中取对象和态射 $E\xrightarrow{i}X\overset{f}{\underset{g}{\rightrightarrows}}Y$。如果这是一个等化子，那么方形

![等化子与拉回方形](/library/volume-87/diagrams/pdf-0133-equalizer-square.png)

是否必然是拉回？逆命题又如何？给出证明或反例。

**5.1.35** 在某个范畴中取一个交换图

![两个相邻方形](/library/volume-87/diagrams/pdf-0133-pasting-pullbacks.png)

假设右侧的方形是拉回。证明：左侧的方形是拉回，当且仅当外部的矩形是拉回。

**5.1.36** 设 $D:\mathbf{I}\to\mathscr{A}$ 是图式，$(L\xrightarrow{p_I}D(I))_{I\in\mathbf{I}}$ 是 $D$ 上的极限锥。

(a) 证明：若态射 $A\overset{h}{\underset{h'}{\rightrightarrows}}L$ 对所有 $I\in\mathbf{I}$ 都满足 $p_I\circ h=p_I\circ h'$，则 $h=h'$。

(b) 当 $\mathbf{I}$ 是有两个对象的离散范畴，$\mathscr{A}=\mathbf{Set}$，且 $A=1$ 时，(a) 的结果是什么意思？回答时不要使用任何范畴论术语。

**5.1.37** 证明例 5.1.22 中的集合 (5.16) 确实是 $D$ 的极限。

<span class="original-page-anchor" id="pdf-page-134" aria-hidden="true"></span>

**5.1.38** 在本题中，你将按照命题 5.1.26 陈述之后介绍的思路证明该命题。

(a) 设 $\mathscr{A}$ 是具有所有积和等化子的范畴，$D:\mathbf{I}\to\mathscr{A}$ 是 $\mathscr{A}$ 中的图式。定义态射

![积之间的态射](/library/volume-87/diagrams/pdf-0134-product-pair.png)

如下：给定 $\mathbf{I}$ 中的 $J\xrightarrow{u}K$，$s$ 的 $u$ 分量是复合

$$
\prod_{I\in\mathbf{I}}D(I)\xrightarrow{\operatorname{pr}_J}D(J)\xrightarrow{Du}D(K)
$$

（其中 $\operatorname{pr}$ 表示积的投影），而 $t$ 的 $u$ 分量是 $\operatorname{pr}_K$。设 $L\xrightarrow{p}\prod_{I\in\mathbf{I}}D(I)$ 是 $s$ 和 $t$ 的等化子，用 $p_I$ 表示 $p$ 的 $I$ 分量。证明 $(L\xrightarrow{p_I}D(I))_{I\in\mathbf{I}}$ 是 $D$ 上的极限锥，从而证明命题 5.1.26(a)。

(b) 调整上述论证，证明命题 5.1.26(b)。

**5.1.39** 证明：一个具有拉回和一个终对象的范畴具有所有有限极限。

**5.1.40** 设 $\mathscr{A}$ 是范畴，$A\in\mathscr{A}$。$A$ 的一个**子对象**是以 $A$ 为靶的单态射的一个同构类。更准确地说，设 $\mathbf{Monic}(A)$ 是 $\mathscr{A}/A$ 中以单态射为对象的充满子范畴；那么 $A$ 的一个子对象就是 $\mathbf{Monic}(A)$ 中对象的一个同构类。

(a) 设 $X\xrightarrow{m}A$ 和 $X'\xrightarrow{m'}A$ 是 $\mathbf{Set}$ 中的单态射。证明：$m$ 与 $m'$ 在 $\mathbf{Monic}(A)$ 中同构，当且仅当它们具有相同的像。推导出 $A$ 的子对象与 $A$ 的子集之间存在典范的一一对应。

(b) (a) 表明，在 $\mathbf{Set}$ 中，子对象就是子集。在 $\mathbf{Grp}$、$\mathbf{Ring}$ 和 $\mathbf{Vect}_k$ 中，子对象是什么？

(c) $\mathbf{Top}$ 中的子对象是什么？（小心！）

**5.1.41** 证明引理 5.1.32。

**5.1.42** 设

![单态射的拉回](/library/volume-87/diagrams/pdf-0134-pullback-monic.png)

<span class="original-page-anchor" id="pdf-page-135" aria-hidden="true"></span>

是某个范畴中的拉回方形。证明：如果 $m$ 是单态射，那么 $m'$ 也是。（由例 5.1.17(a)，我们已经知道这在集合范畴中成立。）

## 5.2 余极限：定义与例子

我们已经看到，极限的例子遍布数学各处。因此，考察其对偶概念——余极限——并询问它是否同样无处不在，是很自然的。

通过对偶化，我们可以立即写出余极限的定义。随后再考察特殊情形：余积、余等化子和推出，它们分别是积、等化子和拉回的对偶。

为对偶概念命名有两种常见惯例：有时添加或去掉前缀“co”（如 limit/colimit，即极限/余极限），有时使用“左”和“右”（如伴随函子）。也有一些不规则的名称，例如终对象/始对象、拉回/推出。

**定义 5.2.1** 设 $\mathscr{A}$ 是范畴，$\mathbf{I}$ 是小范畴。设 $D:\mathbf{I}\to\mathscr{A}$ 是 $\mathscr{A}$ 中的图式，用 $D^{\mathrm{op}}$ 表示相应的函子 $\mathbf{I}^{\mathrm{op}}\to\mathscr{A}^{\mathrm{op}}$。$D$ 上的一个**余锥**就是 $D^{\mathrm{op}}$ 上的一个锥，而 $D$ 的一个**余极限**就是 $D^{\mathrm{op}}$ 的一个极限。

具体而言，$D$ 上的一个余锥由对象 $A\in\mathscr{A}$（余锥的**顶点**）以及 $\mathscr{A}$ 中的一族态射

$$
\left(D(I)\xrightarrow{f_I}A\right)_{I\in\mathbf{I}}\tag{5.17}
$$

组成，满足：对于 $\mathbf{I}$ 中的所有态射 $I\xrightarrow{u}J$，图

![余锥条件](/library/volume-87/diagrams/pdf-0135-cocone.png)

都交换。$D$ 的一个余极限是一个余锥

$$
\left(D(I)\xrightarrow{p_I}C\right)_{I\in\mathbf{I}},
$$

满足这样的性质：对于 $D$ 上的任意余锥 (5.17)，存在唯一的态射 $\bar{f}:C\to A$，使得对所有 $I\in\mathbf{I}$ 都有 $\bar{f}\circ p_I=f_I$。对应的图是图 5.1 的镜像。

当然，注 5.1.20 在这里同样适用。我们把余极限（的顶点）记作 $\varinjlim_{\mathbf{I}}D$，并把态射 $p_I$ 称为**余投影**。

<span class="original-page-anchor" id="pdf-page-136" aria-hidden="true"></span>

### 余积

**定义 5.2.2** **余积**（也称**和**，sum 或 coproduct）是离散范畴上的余极限。（即对某个离散范畴 $\mathbf{I}$，它是形状为 $\mathbf{I}$ 的余极限。）

设 $(X_i)_{i\in I}$ 是一个范畴中的对象族。它们的余积（若存在）记为 $\sum_{i\in I}X_i$ 或 $\coprod_{i\in I}X_i$。当 $I$ 是有限集 $\{1,\ldots,n\}$ 时，我们把 $\sum_{i\in I}X_i$ 写成 $X_1+\cdots+X_n$；若 $n=0$，则写成 $0$。

**例 5.2.3** 根据例 5.1.9 的对偶，空族的余积恰好就是始对象。

**例 5.2.4** 第 3.1 节已经描述了 $\mathbf{Set}$ 中的余积。现在我们仔细考察二元余积的泛性质。取两个集合 $X_1$ 和 $X_2$，构造它们的余积 $X_1+X_2$，并考虑包含映射

![到余积的包含映射](/library/volume-87/diagrams/pdf-0136-sum-coprojections.png)

这是一个余极限余锥。为证明这一点，我们必须证明如下泛性质：对于任意由集合和函数组成的图

![两个集合上的余锥](/library/volume-87/diagrams/pdf-0136-sum-cocone.png)

都存在唯一的函数 $\bar{f}:X_1+X_2\to A$，使图

![余积的泛性质](/library/volume-87/diagrams/pdf-0136-sum-universal.png)

交换。我们在第 3.1 节指出，$p_1$ 和 $p_2$ 是单射，其像构成 $X_1+X_2$ 的一个划分。这意味着 $X_1+X_2$ 的每个元素 $x$ *要么*等于某个 $x_1\in X_1$ 的 $p_1(x_1)$（且此时 $x_1$ 唯一），*要么*等于某个 $x_2\in X_2$ 的 $p_2(x_2)$（且此时 $x_2$ 唯一），两种情况不会同时成立。因此，我们可以在第一种情况下把 $\bar{f}(x)$ 定义为 $f_1(x_1)$，在第二种情况下把它定义为 $f_2(x_2)$。这样就定义了使图交换的函数 $\bar{f}$，而且它显然是唯一具有这一性质的函数。

**例 5.2.5** 设 $X_1$ 和 $X_2$ 是向量空间。有线性映射

![直和的余投影](/library/volume-87/diagrams/pdf-0136-direct-sum-coprojections.png)

由 $i_1(x_1)=(x_1,0)$ 和 $i_2(x_2)=(0,x_2)$ 定义，而且可以验证 (5.18)<span class="original-page-anchor" id="pdf-page-137" aria-hidden="true"></span>是 $\mathbf{Vect}_k$ 中的余极限余锥。因此，二元直和是范畴意义下的余积。这一点很引人注目，因为我们在例 5.1.5 中已经看到，$X_1\oplus X_2$ 也是 $X_1$ 和 $X_2$ 的*积*！与此相比，在集合范畴（以及几乎所有其他范畴）中，余积与积截然不同。

**例 5.2.6** 设 $(A,\leq)$ 是有序集。$A$ 中的**上界**和**最小上界**（或**并**）是对偶化例 5.1.6 中的定义得到的；对偶地，它们是相应范畴中的余积。族 $(x_i)_{i\in I}$ 的并记为 $\bigvee_{i\in I}x_i$。在二元情形（$I$ 有两个元素）中，$x_1$ 和 $x_2$ 的并记为 $x_1\vee x_2$。空族（$I=\emptyset$）的并是范畴 $A$ 的始对象，如例 5.2.3 所述。等价地，它是 $A$ 的一个**最小元素**：一个满足对所有 $a\in A$ 都有 $0\leq a$ 的元素 $0\in A$。

例如，在 $(\mathbb{R},\leq)$ 中，并就是上确界，而且不存在最小元素。在幂集 $(\mathscr{P}(S),\subseteq)$ 中，并就是集合的并，最小元素是 $\emptyset$。在 $(\mathbb{N},\mid)$ 中，并就是最小公倍数，最小元素是 $1$（因为 $1$ 整除所有数）。所以在自然数的这个次序下，$1$ 最小；但所有数也都整除 $0$，因此 $0$ 最大！

### 余等化子

我们继续用 $\mathbf{E}$ 表示范畴 $\boxed{\bullet\rightrightarrows\bullet}$。

**定义 5.2.7** **余等化子**是形状为 $\mathbf{E}$ 的余极限。

换言之，给定图式 $X\overset{s}{\underset{t}{\rightrightarrows}}Y$，$s$ 和 $t$ 的一个余等化子是一个满足 $p\circ s=p\circ t$，且对于这一性质是泛的态射 $Y\xrightarrow{p}C$。

我们将看到，余等化子类似于商。不过首先，我们需要一些关于等价关系的背景知识。

**注 5.2.8** 集合 $A$ 上的一个二元关系 $R$ 可以看作一个子集 $R\subseteq A\times A$。把 $(a,a')\in R$ 理解为“$a$ 与 $a'$ 有关系”。我们可以说 $A$ 上的一个关系 $S$“包含”另一个这样的关系 $R$。这意味着 $R\subseteq S$：只要 $a$ 与 $a'$ 具有 $R$ 关系，它们也就具有 $S$ 关系。

我们需要使用以下事实：对于集合 $A$ 上的任意二元关系 $R$，存在一个包含 $R$ 的最小等价关系 $\sim$。这称为由 $R$ **生成**的等价关系。“最小”是指，任何包含 $R$ 的等价关系也都包含 $\sim$。

我们可以把 $\sim$ 构造为 $A$ 上所有包含 $R$ 的等价关系的交，因为任意一族等价关系的交仍然是等价关系。还有一种显式的构造。大致的思路<span class="original-page-anchor" id="pdf-page-138" aria-hidden="true"></span>如下：用 $x\to y$ 表示 $(x,y)\in R$，那么 $a\sim a'$ 应当成立，当且仅当 $a$ 与 $a'$ 之间存在如下这样的锯齿链：

$$
a\to b\leftarrow c\leftarrow d\to e\leftarrow a'.
$$

为使这精确化，首先在 $A$ 上定义关系 $S$：

$$
S=\{(a,a')\in A\times A\mid(a,a')\in R\text{ 或 }(a',a)\in R\}
$$

（这把 $R$ 扩大为一个对称关系），然后定义 $\sim$：规定 $a\sim a'$ 当且仅当存在 $n\geq0$ 及 $a_0,\ldots,a_n\in A$，使得

$$
a=a_0,\ (a_0,a_1)\in S,\ (a_1,a_2)\in S,\ \ldots,\ (a_{n-1},a_n)\in S,\ a_n=a'
$$

（这使关系具有自反性和传递性，同时保持对称性）。

接下来，回忆第 3.1 节中关于等价关系的一些事实。给定集合 $A$ 上的任意等价关系 $\sim$，我们可以构造等价类的集合 $A/{\sim}$ 以及商映射 $p:A\to A/{\sim}$。这个商映射 $p$ 是满射，并且对于 $a,a'\in A$，具有性质 $p(a)=p(a')\iff a\sim a'$。我们已经看到，对于任意集合 $B$，映射 $A/{\sim}\to B$ 与满足下式的映射 $f:A\to B$ 通过与 $p$ 复合而一一对应：

$$
\forall a,a'\in A,\qquad a\sim a'\implies f(a)=f(a').\tag{5.19}
$$

最后，考虑 $\sim$ 是由某个关系 $R$ 生成的等价关系时的这一泛性质。此时，条件 (5.19) 等价于：

$$
\forall a,a'\in A,\qquad (a,a')\in R\implies f(a)=f(a').\tag{5.20}
$$

（证明：在 $A$ 上用 $a\approx a'\iff f(a)=f(a')$ 定义等价关系 $\approx$。条件 (5.19) 表示 ${\sim}\subseteq{\approx}$，条件 (5.20) 则表示 $R\subseteq{\approx}$。但 $\sim$ 是包含 $R$ 的最小等价关系，所以这两个陈述等价。）总之，对于任意集合 $B$，映射 $A/{\sim}\to B$ 与满足 (5.20) 的映射 $f:A\to B$ 一一对应。

**例 5.2.9** 取集合和函数 $X\overset{s}{\underset{t}{\rightrightarrows}}Y$。为求 $s$ 和 $t$ 的余等化子，我们必须用某种典范的方式构造集合 $C$ 和函数 $p:Y\to C$，使对所有 $x\in X$ 都有 $p(s(x))=p(t(x))$。因此，设 $\sim$ 是 $Y$ 上由所有 $x\in X$ 的 $s(x)\sim t(x)$ 生成的等价关系。（换言之，$\sim$ 是由 $Y$ 上的关系

$$
R=\{(s(x),t(x))\mid x\in X\}
$$

生成的。）取商映射 $p:Y\to Y/{\sim}$。根据注 5.2.8 中描述的对应，这确实是 $s$ 和 $t$ 的余等化子。

<span class="original-page-anchor" id="pdf-page-139" aria-hidden="true"></span>

**例 5.2.10** 对于 $\mathbf{Ab}$ 中的每对同态 $A\overset{s}{\underset{t}{\rightrightarrows}}B$，都有一个同态 $t-s:A\to B$，从而得到 $B$ 的子群 $\operatorname{im}(t-s)$。$s$ 和 $t$ 的余等化子是典范同态 $B\to B/\operatorname{im}(t-s)$。（比较例 5.1.15。）

### 推出

**定义 5.2.11** **推出**是形状为下列范畴的余极限：

![推出的形状](/library/volume-87/diagrams/pdf-0139-pushout-shape.png)

换言之，图式

![用于推出的图式](/library/volume-87/diagrams/pdf-0139-pushout-diagram.png)

的推出（若存在）是一个交换方形

![推出方形](/library/volume-87/diagrams/pdf-0139-pushout-square.png)

而且对于这一性质是泛的。再换一种说法，范畴 $\mathscr{A}$ 中的推出就是 $\mathscr{A}^{\mathrm{op}}$ 中的拉回。

**例 5.2.12** 在 $\mathbf{Set}$ 中取一个图式 (5.21)。它的推出 $P$ 是 $(Y+Z)/{\sim}$，其中 $\sim$ 是 $Y+Z$ 上由所有 $x\in X$ 的 $s(x)\sim t(x)$ 生成的等价关系。余投影 $Y\to P$ 把 $y\in Y$ 映到它在 $P$ 中的等价类，余投影 $Z\to P$ 也类似。

例如，设 $Y$ 和 $Z$ 是某个集合 $A$ 的子集。那么

![并集给出的推出](/library/volume-87/diagrams/pdf-0139-union-pushout.png)

是 $\mathbf{Set}$ 中的推出方形。（它也是拉回方形！这种巧合是集合范畴的特殊性质。）你可以通过验证<span class="original-page-anchor" id="pdf-page-140" aria-hidden="true"></span>泛性质，或使用刚刚给出的公式来核实这一点。在这种情况下，公式把两个集合 $Y$ 和 $Z$ 并排放置（得到 $Y+Z$），然后把 $Y$ 中的子集 $Y\cap Z$ 与 $Z$ 中的子集 $Y\cap Z$ 粘合（得到 $(Y+Z)/{\sim}=Y\cup Z$）。

**例 5.2.13** 如果 $\mathscr{A}$ 是具有始对象 $0$ 的范畴，且 $Y,Z\in\mathscr{A}$，那么唯一的图式

![沿始对象的推出](/library/volume-87/diagrams/pdf-0140-initial-pushout.png)

的一个推出恰好就是 $Y$ 和 $Z$ 的一个余积。

**例 5.2.14** van Kampen 定理（例 0.9）指出，给定 $\mathbf{Top}$ 中满足某些额外假设的推出方形，对整个方形取基本群所得到的 $\mathbf{Grp}$ 中的方形也是推出。

下面还有一种余极限的形状，它与例 5.1.21(d) 中的形状对偶。

**例 5.2.15** 图式 $D:(\mathbb{N},\leq)\to\mathscr{A}$ 由 $\mathscr{A}$ 中的对象和态射

$$
X_0\xrightarrow{s_1}X_1\xrightarrow{s_2}X_2\xrightarrow{s_3}\cdots
$$

组成。这样的图式的余极限传统上称为**正向极限**。虽然旧术语“逆极限”（例 5.1.21(d)）和“正向极限”分别已被一般的范畴论术语“极限”和“余极限”所涵盖，但仍应了解这些名称。

考虑了所有这些例子之后，我们现在写出 $\mathbf{Set}$ 中余极限的一般公式。

**例 5.2.16** 图式 $D:\mathbf{I}\to\mathbf{Set}$ 的余极限由下式给出：

$$
\varinjlim_{\mathbf{I}}D=\left(\sum_{I\in\mathbf{I}}D(I)\right)\Big/{\sim},
$$

其中 $\sim$ 是 $\sum D(I)$ 上由

$$
x\sim(Du)(x)
$$

生成的等价关系，这里遍历 $\mathbf{I}$ 中所有 $I\xrightarrow{u}J$ 和所有 $x\in D(I)$。为说明这一点，注意对于任意集合 $A$，映射

$$
\left(\sum D(I)\right)\Big/{\sim}\;\to A
$$

与满足下式的映射 $f:\sum D(I)\to A$ 双射对应：

$$
f(x)=f((Du)(x))
$$

<span class="original-page-anchor" id="pdf-page-141" aria-hidden="true"></span>

![球面作为极限与余极限](/library/volume-87/diagrams/pdf-0141-sphere-limit-colimit.png)

图 5.2 球面作为 (a) 极限，以及 (b) 余极限。

对所有 $u$ 和 $x$ 成立（由注 5.2.8）。这些映射又对应于满足对所有 $u$ 和 $x$ 都有 $f_I(x)=f_J((Du)(x))$ 的态射族 $(D(I)\xrightarrow{f_I}A)_{I\in\mathbf{I}}$；而这些恰好就是 $D$ 上以 $A$ 为顶点的余锥。

$\mathbf{Set}$ 中极限的公式（例 5.1.22）与 $\mathbf{Set}$ 中余极限的公式之间存在某种对偶性。极限构造为一个*积*的*子集*，而余极限则是一个*余积*的*商*。

图 5.2 用一个具体的拓扑例子来呈现极限和余极限各自的特点。在初等教材中，曲面几乎总被看作欧氏空间 $\mathbb{R}^3$ 的子集，而球面 $S^2$ 通常定义为

$$
\{(x,y,z)\in\mathbb{R}^3\mid x^2+y^2+z^2=1\}.
$$

这是*积*空间 $\mathbb{R}^3=\mathbb{R}\times\mathbb{R}\times\mathbb{R}$ 的一个*子空间*，这提示我们它是一个极限。事实上，球面是等化子

![球面作为等化子](/library/volume-87/diagrams/pdf-0141-sphere-equalizer.png)

其中映射 $s,t:\mathbb{R}^3\to\mathbb{R}$ 定义为

$$
s(x,y,z)=x^2+y^2+z^2,\qquad t(x,y,z)=1.
$$

（方程由等化子来刻画。）

然而，在更高等的数学中，这一观点使用得较少。我们可以把曲面看成许多小片粘合在一起的结果，每个小片都与开单位圆盘 $D$ 同构。例如，原则上我们可以<span class="original-page-anchor" id="pdf-page-142" aria-hidden="true"></span>通过把大量补胎片粘在一起，构造出一整条自行车内胎。图 5.2(b) 给出了一个更简单的例子：把两个圆盘粘合成一个球面。这样就把球面实现为两份 $D$ 的*余积*（不交并）的一个*商*（粘合），这提示我们，球面是作为余极限构造出来的。事实上，球面是余等化子

![球面作为余等化子](/library/volume-87/diagrams/pdf-0142-sphere-coequalizer.png)

其中 $S^1$ 是圆周，圆柱 $S^1\times(0,1)$ 是两份 $D$ 的交（图 5.2(b) 中央的带状区域），而到 $D+D$ 的两个映射分别是把圆柱包含进第一份和第二份 $D$ 的包含映射。

从极限的观点来看空间，有一个缺点：它任意选定了一个坐标系。一般来说，最好把空间看作独立的对象，其存在不依赖于嵌入欧氏空间的任何特定方式。

从余极限的观点来看空间，也有一个缺点：它任意选定了一种分解。例如，我们可以把球面分成三个小片而不是两个，或者使用与图中不同的两个小片。

余极限的观点在现代几何中占据上风。（如果你熟悉流形的定义，就会意识到，图册本质上就是把流形看作欧氏球的余极限的一种方式。）一个原因是，我们常常关心*从*空间 $X$ 出发的映射，例如 $X\to\mathbb{R}$。*从*余极限出发的映射很容易处理；余极限的定义本身就告诉我们，从它出发的映射是什么。

### 满态射

**定义 5.2.17** 设 $\mathscr{A}$ 是范畴。如果对所有对象 $Z$ 和态射 $Y\overset{g}{\underset{g'}{\rightrightarrows}}Z$ 都有

$$
g\circ f=g'\circ f\implies g=g',
$$

就称 $\mathscr{A}$ 中的态射 $X\xrightarrow{f}Y$ 是**满态射**（epic 或 epimorphism）。

这是单态射定义的形式对偶。（换言之，$\mathscr{A}$ 中的满态射就是 $\mathscr{A}^{\mathrm{op}}$ 中的单态射。）从某种意义上说，它是满射性的范畴版本。不过，单态射的定义与单射的定义很相似，满态射的定义却与满射的定义不太相像。下面的例子证实，在满射性有意义的范畴中，它只有在某些情况下才等价于满态射性。

**例 5.2.18** 在 $\mathbf{Set}$ 中，一个态射是满态射，当且仅当它是满射。如果 $f$ 是<span class="original-page-anchor" id="pdf-page-143" aria-hidden="true"></span>满射，那么 $f$ 当然是满态射。为证明逆命题，取 $Z$ 为二元集 $\{\texttt{true},\texttt{false}\}$，取 $g$ 为 $f$ 的像的特征函数（其定义见第 3.1 节），并取 $g'$ 为恒取值 $\texttt{true}$ 的函数。

任何范畴中的任何同构都是单态射和满态射。在 $\mathbf{Set}$ 中，逆命题也成立，因为任何同时为单射和满射的函数都是可逆的（例 1.1.5）。

**例 5.2.19** 在代数结构范畴中，任何满射当然都是满态射。在包括 $\mathbf{Ab}$、$\mathbf{Vect}_k$ 和 $\mathbf{Grp}$ 在内的某些这样的范畴中，逆命题也成立。（对于 $\mathbf{Ab}$ 和 $\mathbf{Vect}_k$，证明很直接；对于 $\mathbf{Grp}$，证明则困难得多。）不过，在其他一些代数结构范畴中，逆命题不成立。例如，在 $\mathbf{Ring}$ 中，包含映射 $\mathbb{Z}\hookrightarrow\mathbb{Q}$ 是满态射，却不是满射（习题 5.2.23）。这也是一个同时为单态射和满态射、却不是同构的态射的例子。

**例 5.2.20** 在 Hausdorff 拓扑空间和连续映射组成的范畴中，任何像稠密的映射都是满态射。

当然，引理 5.1.32 也有一个对偶版本：一个态射是满态射，当且仅当某个方形是推出。

### 习题

**5.2.21** 设 $X\overset{s}{\underset{t}{\rightrightarrows}}Y$ 是某个范畴中的态射。证明以下三个条件等价：$s=t$；$s$ 和 $t$ 的等化子存在并且是同构；$s$ 和 $t$ 的余等化子存在并且是同构。

**5.2.22** (a) 设 $X$ 是集合，$f:X\to X$ 是映射。尽可能明确地描述 $X\overset{f}{\underset{1}{\rightrightarrows}}X$ 在 $\mathbf{Set}$ 中的余等化子。

(b) 在 $\mathbf{Top}$ 中做同样的事。当 $X$ 是圆周 $S^1$ 时，找出一个 $f$，使其余等化子是一个具有平庸拓扑的不可数空间。

**5.2.23** (a) 证明在幺半群范畴中，包含映射 $(\mathbb{N},+,0)\hookrightarrow(\mathbb{Z},+,0)$ 是满态射，尽管它不是满射。

(b) 证明在环范畴中，包含映射 $\mathbb{Z}\hookrightarrow\mathbb{Q}$ 是满态射，尽管它不是满射。

**5.2.24** （比较习题 5.1.40。）设 $\mathscr{A}$ 是范畴，$A\in\mathscr{A}$。把 $A$ 的一个**商对象**定义为从 $A$ 出发的满态射的一个同构类。也就是说，设 $\mathbf{Epic}(A)$ 是 $A/\mathscr{A}$ 中以满态射为对象的充满子范畴；那么 $A$ 的一个商对象就是 $\mathbf{Epic}(A)$ 中对象的一个同构类。

<span class="original-page-anchor" id="pdf-page-144" aria-hidden="true"></span>

(a) 设 $A\xrightarrow{e}X$ 和 $A\xrightarrow{e'}X'$ 是 $\mathbf{Set}$ 中的满态射。证明：$e$ 与 $e'$ 在 $\mathbf{Epic}(A)$ 中同构，当且仅当它们在 $A$ 上诱导相同的等价关系。推导出 $A$ 的商对象与 $A$ 上的等价关系之间存在典范的一一对应。

(b) 假设 $\mathbf{Grp}$ 中的满态射就是满射（这并非一个显然的事实），证明一个群的商对象与它的正规子群一一对应。

（“商对象”不是一个标准名称，事实上这一概念没有标准名称。可以说，“商对象”更适合用来称呼*正则*满态射的同构类，其定义见下面的习题。）

**5.2.25** 如果存在对象 $C$ 和态射 $B\rightrightarrows C$，使 $m$ 是它们的等化子，就称态射 $m:A\to B$ 是**正则单态射**。如果存在态射 $e:B\to A$，使 $em=1_A$，就称态射 $m:A\to B$ 是**分裂单态射**。

(a) 证明：分裂单态射 $\implies$ 正则单态射 $\implies$ 单态射。

(b) 在 $\mathbf{Ab}$ 中，证明所有单态射都是正则的，但并非所有单态射都是分裂的。（第一部分的提示：$\mathbf{Ab}$ 中的等化子按例 5.1.15 中的方式计算。）

(c) 在 $\mathbf{Top}$ 中，描述正则单态射，并找出一个不是正则单态射的单态射。

**5.2.26** 把习题 5.2.25 中的定义对偶化，就得到**正则满态射**和**分裂满态射**的定义。

(a) 我们在例 5.2.19 中看到，一个态射可能同时是单态射和满态射，却不是同构。证明：在任意范畴中，一个态射是同构，当且仅当它既是单态射，又是*正则*满态射。

(b) 利用我们的集合范畴满足选择公理这一假设（第 3.1 节），证明在 $\mathbf{Set}$ 中有

$$
\text{满态射}\iff\text{正则满态射}\iff\text{分裂满态射}.
$$

(c) 如果范畴 $\mathscr{A}$ 中所有满态射都是分裂的，就称 $\mathscr{A}$ 满足**选择公理**。证明 $\mathbf{Top}$ 和 $\mathbf{Grp}$ 都不满足选择公理。

**5.2.27** 习题 5.1.42 的结果可以表述为“单态射这一类在拉回下稳定”。另一个事实是，两个单态射的复合总是单态射；我们说单态射这一类“对复合封闭”。

考虑下面六类态射：

单态射、正则单态射、分裂单态射、满态射、正则满态射、分裂满态射。

判断每一类是否在拉回下稳定，是否对复合封闭。

<span class="original-page-anchor" id="pdf-page-145" aria-hidden="true"></span>

## 5.3 函子与极限的相互作用

我们在例 5.1.23 中看到，要计算 $\mathbf{Grp}$、$\mathbf{Ring}$、$\mathbf{Vect}_k$ 等范畴中的极限，可以先在集合范畴中求极限，再给所得结果赋予适当的代数结构。另一方面，这些范畴中的余极限与 $\mathbf{Set}$ 中的余极限并不相同。例如，$\mathbf{Grp}$ 的始对象的底层集合（有一个元素）不是 $\mathbf{Set}$ 的始对象（没有元素）；两个向量空间的直和 $X\oplus Y$ 的底层集合，也不是 $X$ 和 $Y$ 的底层集合的余积。因此，这些遗忘函子与极限配合得很好，与余极限却配合得不好。

在本节中，我们将引入一些术语，以便精确表达这些想法。

**定义 5.3.1** (a) 设 $\mathbf{I}$ 是小范畴。如果对所有图式 $D:\mathbf{I}\to\mathscr{A}$ 以及 $D$ 上的所有锥 $(A\xrightarrow{p_I}D(I))_{I\in\mathbf{I}}$，都有

$$
\begin{aligned}
&\left(A\xrightarrow{p_I}D(I)\right)_{I\in\mathbf{I}}\text{ 是 }\mathscr{A}\text{ 中 }D\text{ 上的极限锥}\\
\implies\quad&\left(F(A)\xrightarrow{Fp_I}FD(I)\right)_{I\in\mathbf{I}}\text{ 是 }\mathscr{B}\text{ 中 }F\circ D\text{ 上的极限锥},
\end{aligned}
$$

就称函子 $F:\mathscr{A}\to\mathscr{B}$ **保持形状为 $\mathbf{I}$ 的极限**。

(b) 如果函子 $F:\mathscr{A}\to\mathscr{B}$ 对所有小范畴 $\mathbf{I}$ 都保持形状为 $\mathbf{I}$ 的极限，就称它**保持极限**。

(c) **反映**极限的定义与 (a) 相同，但要把 $\Longrightarrow$ 换成 $\Longleftarrow$。

当然，同样的术语也适用于余极限。

保持极限的定义还有另一种表述。函子 $F:\mathscr{A}\to\mathscr{B}$ 保持极限，当且仅当它具有如下性质：只要图式 $D:\mathbf{I}\to\mathscr{A}$ 存在极限，复合 $F\circ D:\mathbf{I}\to\mathscr{B}$ 也存在极限，而且典范态射

$$
F\left(\varprojlim_{\mathbf{I}}D\right)\to\varprojlim_{\mathbf{I}}(F\circ D)
$$

是同构。这里的“典范态射”的 $I$ 分量是

$$
F\left(\varprojlim_{\mathbf{I}}D\right)\xrightarrow{F(p_I)}F(D(I)),
$$

其中 $p_I$ 是 $D$ 上的极限锥的第 $I$ 个投影。

特别地，如果 $F$ 保持极限，那么对于任何存在极限的图式 $D$，都有

$$
F\left(\varprojlim_{\mathbf{I}}D\right)\cong\varprojlim_{\mathbf{I}}(F\circ D).\tag{5.22}
$$

保持极限所表达的内容<span class="original-page-anchor" id="pdf-page-146" aria-hidden="true"></span>比 (5.22) 所表达的更多：要求等式两边不仅同构，而且要*以某种特定方式*同构。不过，我们有时会略去这一检查，仿佛保持极限仅仅意味着 (5.22) 成立。

**例 5.3.2** 遗忘函子 $U\colon\mathbf{Top}\to\mathbf{Set}$ 既保持极限，也保持余极限。（我们将看到，这源于 $U$ 的两侧都有伴随函子这一事实。）它并不反映所有极限，也不反映所有余极限。例如，任取非离散空间 $X$ 和 $Y$，令 $Z$ 为赋予离散拓扑的集合 $U(X)\times U(Y)$。（这里唯一要紧的是，$Z$ 上的拓扑严格大于积拓扑。）于是，在 $\mathbf{Top}$ 中有一个锥

$$
X\leftarrow Z\to Y\tag{5.23}
$$

它在 $\mathbf{Set}$ 中的像是积锥

$$
U(X)\leftarrow U(X)\times U(Y)\to U(Y).
$$

但是 (5.23) 并不是 $\mathbf{Top}$ 中的积锥，因为 $U(X)\times U(Y)$ 上的离散拓扑不是积拓扑。

**例 5.3.3** 在本节第一段中，我们指出，遗忘函子 $\mathbf{Grp}\to\mathbf{Set}$ 不保持始对象，而遗忘函子 $\mathbf{Vect}_k\to\mathbf{Set}$ 不保持二元余积。从代数结构的范畴出发的遗忘函子很少保持所有余极限。

**例 5.3.4** 我们还看到，（在所提到的例子中）代数结构范畴上的遗忘函子的确保持极限。事实上，还有更强的结论成立。让我们考察 $\mathbf{Grp}$ 中的二元积，不过，以下所有论述也适用于 $\mathbf{Grp}$、$\mathbf{Ab}$、$\mathbf{Vect}_k$、$\mathbf{Ring}$ 等任一范畴中的任意极限。

取群 $X_1$ 和 $X_2$。我们可以构造积集合 $U(X_1)\times U(X_2)$，它带有投影

$$
U(X_1)\xleftarrow{p_1}U(X_1)\times U(X_2)\xrightarrow{p_2}U(X_2).
$$

我断言，集合 $U(X_1)\times U(X_2)$ 上恰有一个群结构，使 $p_1$ 和 $p_2$ 都是同态。为证明唯一性，假设 $U(X_1)\times U(X_2)$ 上有一个具有此性质的群结构。取 $U(X_1)\times U(X_2)$ 的元素 $(x_1,x_2)$ 和 $(x'_1,x'_2)$，并记 $(x_1,x_2)\cdot(x'_1,x'_2)=(y_1,y_2)$。由于 $p_1$ 是同态，

$$
y_1=p_1(y_1,y_2)=p_1((x_1,x_2)\cdot(x'_1,x'_2))=p_1(x_1,x_2)\cdot p_1(x'_1,x'_2)=x_1\cdot x'_1,
$$

类似地，$y_2=x_2\cdot x'_2$。因此

$$
(x_1,x_2)\cdot(x'_1,x'_2)=(x_1x'_1,x_2x'_2).
$$

<span class="original-page-anchor" id="pdf-page-147" aria-hidden="true"></span>

![创造极限](/library/volume-87/diagrams/pdf-0147-creation.png)

图 5.3 创造极限。

类似的论证表明，$(x_1,x_2)^{-1}=(x_1^{-1},x_2^{-1})$，并且群的单位元 $1$ 是 $(1,1)$。现在，为证明存在性，用刚才给出的公式定义 $\cdot$、$(\ )^{-1}$ 和 $1$；随后便可验证群公理成立，而且 $p_1$ 和 $p_2$ 都是群同态。这就证明了该断言。

用 $L$ 表示赋予这一群结构的集合 $U(X_1)\times U(X_2)$。于是，在 $\mathbf{Grp}$ 中有一个锥

$$
X_1\xleftarrow{p_1}L\xrightarrow{p_2}X_2.
$$

容易验证，它事实上是 $\mathbf{Grp}$ 中的一个*积*锥。

我们可以用不依赖于群论的语言概括这一点。给定 $\mathbf{Grp}$ 的对象 $X_1$ 和 $X_2$，

- 对 $\mathbf{Set}$ 中 $(U(X_1),U(X_2))$ 上的任意积锥，在 $\mathbf{Grp}$ 中都有唯一一个 $(X_1,X_2)$ 上的锥，使它在 $U$ 下的像就是我们起初给定的锥；
- 这个 $(X_1,X_2)$ 上的锥是积锥。

这启发我们给出如下定义（图 5.3）。

**定义 5.3.5** 如果每当 $D\colon\mathbf{I}\to\mathscr{A}$ 是 $\mathscr{A}$ 中的一个图表时，以下条件都成立，就称函子 $F\colon\mathscr{A}\to\mathscr{B}$ **创造（形状为 $\mathbf{I}$ 的）极限**：

- 对图表 $F\circ D$ 上的任意极限锥 $\bigl(B\xrightarrow{q_I}FD(I)\bigr)_{I\in\mathbf{I}}$，在 $D$ 上都有唯一一个锥 $\bigl(A\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$，使得 $F(A)=B$，并且对所有 $I\in\mathbf{I}$ 都有 $F(p_I)=q_I$；
- 这个锥 $\bigl(A\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ 是 $D$ 上的极限锥。

从 $\mathbf{Grp}$、$\mathbf{Ring}$、$\ldots$ 到 $\mathbf{Set}$ 的遗忘函子都创造极限（练习 5.3.11）。下面的结果说明了“*创造*”一词的含义。

<span class="original-page-anchor" id="pdf-page-148" aria-hidden="true"></span>

**引理 5.3.6** 设 $F\colon\mathscr{A}\to\mathscr{B}$ 是函子，$\mathbf{I}$ 是小范畴。假设 $\mathscr{B}$ 具有形状为 $\mathbf{I}$ 的极限，而 $F$ 创造这样的极限。那么 $\mathscr{A}$ 具有形状为 $\mathbf{I}$ 的极限，而 $F$ 保持这样的极限。

**证明** 练习 5.3.12。$\square$

由于 $\mathbf{Set}$ 具有所有极限，可知我们所讨论的代数结构范畴全都具有所有极限，并且遗忘函子保持这些极限。

**注 5.3.7** 定义 5.3.5 有一点值得怀疑。它提到了范畴中对象的*相等*关系，而正如我们在第 31 页所看到的，这一关系通常过于严格，并不合适。几乎总是把相等换成同构更好。如果在“创造极限”的整个定义中把相等换成同构，我们就会得到一个更健全、涵盖范围更广的概念。用定义 5.3.5 中的记号来说，我们要求：如果 $F\circ D$ 具有极限，那么存在 $D$ 上的一个锥，使它在 $F$ 下的像是极限锥，而且每一个这样的锥本身都是极限锥。

事实上，我们所称的创造极限，真正应该称为*严格*创造极限，而把“创造极限”留给那个涵盖范围更广的概念。在大多数文献中，“创造”一词就是这样使用的。我选择在这里使用严格版本，是因为它的表述略为简单，也因为眼下的例子都满足这个更严格的条件。

### 练习

**5.3.8** 取极限是一个过程：它以范畴 $\mathscr{A}$ 中的图表为输入，并输出 $\mathscr{A}$ 的一个新对象。稍后我们将看到，这个过程具有函子性（命题 6.1.4）。这里要求你在二元积的情形证明这一点。

设 $\mathscr{A}$ 是具有二元积的范畴。假设我们已为每一对对象 $(X,Y)$ 选取了一个积锥

$$
X\xleftarrow{p_1^{X,Y}}X\times Y\xrightarrow{p_2^{X,Y}}Y.
$$

构造一个函子 $\mathscr{A}\times\mathscr{A}\to\mathscr{A}$，它在对象上的作用为 $(X,Y)\mapsto X\times Y$。

**5.3.9** 设 $\mathscr{A}$ 是具有二元积的范畴。直接证明

$$
\mathscr{A}(A,X\times Y)\cong\mathscr{A}(A,X)\times\mathscr{A}(A,Y)
$$

关于 $A,X,Y\in\mathscr{A}$ 是自然的。（这里预先假定，我们已为每个 $X$ 和 $Y$ 选取了 $(X,Y)$ 上的一个积锥。根据练习 5.3.8，指派 $(X,Y)\mapsto X\times Y$ 因而具有函子性；要使“自然”一词有意义，它就必须具有这一性质。）

<span class="original-page-anchor" id="pdf-page-149" aria-hidden="true"></span>

**5.3.10** 证明：如果一个函子创造极限，那么它也反映极限。

**5.3.11** 例 5.3.4 已经说明，遗忘函子 $U\colon\mathbf{Grp}\to\mathbf{Set}$ 创造二元积。

(a) 利用 $\mathbf{Set}$ 中极限的公式（例 5.1.22），证明事实上 $U$ 创造任意极限。

(b) 自行确认：如果把 $\mathbf{Grp}$ 换成任意其他代数结构范畴，如 $\mathbf{Ring}$、$\mathbf{Ab}$ 或 $\mathbf{Vect}_k$，同样的结论也成立。

**5.3.12** 证明引理 5.3.6。

**5.3.13** (a) 如果范畴 $\mathscr{B}$ 的对象 $P$ 使得 $\mathscr{B}(P,-)\colon\mathscr{B}\to\mathbf{Set}$ 保持满态射，就称 $P$ 是**投射的**。（这意味着，如果 $f$ 是满态射，那么 $\mathscr{B}(P,f)$ 也是满态射。）设

![伴随关系](/library/volume-87/diagrams/pdf-0149-adjunction.png)

是一个伴随关系，其中 $G$ 保持满态射。证明：对所有集合 $S$，$F(S)$ 都是投射对象。

(b) 在 $\mathbf{Ab}$ 中找出一个非投射对象。

(c) 如果范畴 $\mathscr{B}$ 的对象 $I$ 在 $\mathscr{B}^{\mathrm{op}}$ 中是投射的，或者等价地，$\mathscr{B}(-,I)\colon\mathscr{B}^{\mathrm{op}}\to\mathbf{Set}$ 保持满态射，就称 $I$ 是**内射的**。说明 $\mathbf{Vect}_k$ 的所有对象都是内射的，并在 $\mathbf{Ab}$ 中找出一个非内射对象。
