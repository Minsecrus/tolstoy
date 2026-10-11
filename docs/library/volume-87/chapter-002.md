---
title: "第二章 伴随函子"
description: "Tom Leinster《Basic Category Theory》中文译文。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"第一章 范畴、函子与自然变换","link":"/library/volume-87/chapter-001"}
next: {"text":"第三章 集合论插曲","link":"/library/volume-87/chapter-003"}
---

# 第二章 伴随函子

<span class="original-page-anchor" id="pdf-page-50" aria-hidden="true"></span>

桑德斯·麦克莱恩的著作《工作数学家的范畴论》有一句口号：

> *伴随函子无处不在。*

我们将看到数学中不同领域的伴随函子实例，体会到这句话所言不虚。除了通过例子来理解伴随，我们还将从三个不同的方向研究伴随理论，每个方向都有各自的直观理解。随后，我们将证明这三种途径是等价的。

理解伴随关系，会为你的数学工具箱增添一件宝贵的工具。大多数从事纯数学研究的专业数学家都知道什么是范畴和函子，但了解伴随的人要少得多。其实应该有更多人了解它：伴随函子既常见又容易掌握，而且了解伴随有助于你发现数学世界中的模式。

## 2.1 定义与例子

考虑一对方向相反的函子 $F\colon\mathscr{A}\to\mathscr{B}$ 和 $G\colon\mathscr{B}\to\mathscr{A}$。粗略地说，如果对于任意 $A\in\mathscr{A}$ 和 $B\in\mathscr{B}$，态射 $F(A)\to B$ 与态射 $A\to G(B)$ 本质上是同一回事，就称 $F$ 是 $G$ 的左伴随。

**定义 2.1.1** 设 ![范畴与方向相反的函子 F 和 G](/library/volume-87/diagrams/pdf-0050-functor-pair.png) 是范畴和函子。如果

$$
\mathscr{B}(F(A),B)\cong\mathscr{A}(A,G(B))\tag{2.1}
$$

关于 $A\in\mathscr{A}$ 和 $B\in\mathscr{B}$ 是自然的，就称 $F$ 是 $G$ 的**左伴随**，$G$ 是 $F$ 的**右伴随**，并记作 $F\dashv G$。“自然的”一词的含义将在下文定义。$F$ 与 $G$ 之间的一个**伴随关系**，就是选定一个自然同构 (2.1)。

<span class="original-page-anchor" id="pdf-page-51" aria-hidden="true"></span>

“关于 $A\in\mathscr{A}$ 和 $B\in\mathscr{B}$ 是自然的”是说，对于每个 $A\in\mathscr{A}$ 和 $B\in\mathscr{B}$，都指定了一个双射 (2.1)，并且它满足一条自然性公理。为了陈述这条公理，我们需要一些记号。给定对象 $A\in\mathscr{A}$ 和 $B\in\mathscr{B}$，态射 $F(A)\to B$ 与 $A\to G(B)$ 之间的对应 (2.1)，在两个方向上都用一条横线表示：

![转置对应的两个方向](/library/volume-87/diagrams/pdf-0051-transpose-correspondence.png)

因此 $\bar{\bar{f}}=f$ 且 $\bar{\bar{g}}=g$。我们称 $\bar{f}$ 为 $f$ 的**转置**，对 $g$ 也作同样的称呼。自然性公理由两部分组成：

$$
\overline{\Bigl(F(A)\xrightarrow{g} B\xrightarrow{q} B'\Bigr)}
\quad=\quad
\Bigl(A\xrightarrow{\bar{g}}G(B)\xrightarrow{G(q)}G(B')\Bigr)\tag{2.2}
$$

（即 $\overline{q\circ g}=G(q)\circ\bar{g}$）对所有 $g$ 和 $q$ 成立，并且

$$
\overline{\Bigl(A'\xrightarrow{p} A\xrightarrow{f} G(B)\Bigr)}
\quad=\quad
\Bigl(F(A')\xrightarrow{F(p)} F(A)\xrightarrow{\bar{f}} B\Bigr)\tag{2.3}
$$

对所有 $p$ 和 $f$ 成立。由于加横线两次就会回到原来的态射，把这些等式中的长横线加在左边还是右边并没有区别。

**注记 2.1.2** (a) 自然性公理乍看可能有些随意，但我们将在第 4 章看到，它只是说两个特定的函子自然同构。本节暂不讨论这条公理，我们先相信它符合通常对自然性的直观理解：定义一个东西时，没有作出任何任意的选择。

(b) 自然性公理意味着，从每一组态射

$$
A_0\to\cdots\to A_n,\qquad F(A_n)\to B_0,\qquad B_0\to\cdots\to B_m,
$$

都恰好能构造出一个态射

$$
A_0\to G(B_m).
$$

请与有关范畴、函子和自然变换的定义的评论比较（注记 1.1.2(b)、1.2.2(a) 和 1.3.2(a)）。

(c) 伴随函子不仅无处不在；更妙的是，每当你看到一对函子 $\mathscr{A}\rightleftarrows\mathscr{B}$，它们很有可能是伴随的（无论哪一个在左）。

例如，假设你与一位数学家交谈，她说自己的工作涉及李代数和结合代数。你想插话，说这两种东西你都不了解，但她还是继续讲，解释说有一种方法能把任意李代数变成结合代数，也有一种方法能把任意结合<span class="original-page-anchor" id="pdf-page-52" aria-hidden="true"></span>代数变成李代数。到了这个时候，即使你不知道她在说什么，你也应当与她打赌：这两个过程中的一个是另一个的伴随。这几乎总是奏效。

(d) 给定一个函子 $G$，它可能有左伴随，也可能没有；但如果有，那么左伴随在同构意义下是唯一的，因此谈论“$G$ 的*左伴随*”是有意义的。右伴随也一样。我们将在后面证明这一点（例 4.3.13）。

你可能会问：“知道两个函子是伴随的，对我们有什么用？”唯一性是答案中至关重要的一部分。让我们回到 (c) 中的例子。只需几分钟，你就能了解什么是李代数、什么是结合代数，以及把结合代数变成李代数的标准函子 $G$ 是什么。那么反方向的函子 $F$ 呢？大多数代数书会在“泛包络代数”条目下描述 $F$，但理解这种描述要花长得多的时间。然而，只要知道 $F$ 是 $G$ 的左伴随，你就能完全绕过这个过程。由于 $G$ 只能有*一个*左伴随，这就完全刻画了 $F$。在某种意义上，它告诉了你需要知道的一切。

**例 2.1.3（代数：自由 $\dashv$ 遗忘）** 代数结构的范畴之间的遗忘函子通常都有左伴随。例如：

(a) 设 $k$ 是一个域。有伴随关系

![自由向量空间函子与遗忘函子的伴随关系](/library/volume-87/diagrams/pdf-0052-free-vector-space.png)

其中 $U$ 是例 1.2.3(b) 中的遗忘函子，$F$ 是例 1.2.4(c) 中的自由函子。伴随关系说明，给定集合 $S$ 和向量空间 $V$，线性映射 $F(S)\to V$ 与函数 $S\to U(V)$ 本质上是同一回事。

我们在例 0.4 中已经见过这一点，现在来详细验证。

固定一个集合 $S$ 和一个向量空间 $V$。给定线性映射 $g\colon F(S)\to V$，可以通过对所有 $s\in S$ 令 $\bar{g}(s)=g(s)$，定义集合间的映射 $\bar{g}\colon S\to U(V)$。这给出一个函数

$$
\begin{array}{ccc}
\mathbf{Vect}_k(F(S),V)&\to&\mathbf{Set}(S,U(V))\\
g&\mapsto&\bar{g}.
\end{array}
$$

反过来，给定集合间的映射 $f\colon S\to U(V)$，可以通过令 $\bar{f}\bigl(\sum_{s\in S}\lambda_s s\bigr)=\sum_{s\in S}\lambda_s f(s)$ 定义线性映射 $\bar{f}\colon F(S)\to V$，其中该公式适用于所有形式<span class="original-page-anchor" id="pdf-page-53" aria-hidden="true"></span>线性组合 $\sum\lambda_s s\in F(S)$。这给出一个函数

$$
\begin{array}{ccc}
\mathbf{Set}(S,U(V))&\to&\mathbf{Vect}_k(F(S),V)\\
f&\mapsto&\bar{f}.
\end{array}
$$

这两个由“加横线”定义的函数互为逆函数：对任意线性映射 $g\colon F(S)\to V$，我们有

$$
\bar{\bar{g}}\Biggl(\sum_{s\in S}\lambda_s s\Biggr)
=\sum_{s\in S}\lambda_s\bar{g}(s)
=\sum_{s\in S}\lambda_s g(s)
=g\Biggl(\sum_{s\in S}\lambda_s s\Biggr)
$$

对所有 $\sum\lambda_s s\in F(S)$ 成立，因此 $\bar{\bar{g}}=g$；而对任意集合间的映射 $f\colon S\to U(V)$，我们有

$$
\bar{\bar{f}}(s)=\bar{f}(s)=f(s)
$$

对所有 $s\in S$ 成立，因此 $\bar{\bar{f}}=f$。于是，对于每个 $S\in\mathbf{Set}$ 和 $V\in\mathbf{Vect}_k$，我们都得到了 $\mathbf{Vect}_k(F(S),V)$ 与 $\mathbf{Set}(S,U(V))$ 之间的一个典范双射，正如所要求的。

这里我们仔细地区分了向量空间 $V$ 与它的底层集合 $U(V)$。不过，范畴论和一般数学一样，常常省略遗忘函子的符号。在这个例子中，就是省掉 $U$，让读者自行判断每一次出现的 $V$ 究竟是指向量空间本身，还是它的底层集合。我们自己也很快就会开始使用这种简写。

(b) 同样地，有伴随关系

![自由群函子与遗忘函子的伴随关系](/library/volume-87/diagrams/pdf-0053-free-group.png)

其中 $F$ 和 $U$ 是例 1.2.3(a) 和 1.2.4(a) 中的自由函子与遗忘函子。

自由群函子的显式构造颇为棘手。在第 6 章，我们将证明一个结果（一般伴随函子定理），保证 $U$ 以及许多类似的函子都有左伴随。如注记 2.1.2(d) 所说，这在一定程度上使我们不必显式构造 $F$。不过，也不能把这一点说得太绝对：对群论研究者而言，可用的自由群描述越多越好。显式构造确实可能有用。不过，这类遗忘函子总有左伴随，是一条重要的一般原则。

<span class="original-page-anchor" id="pdf-page-54" aria-hidden="true"></span>

(c) 有伴随关系

![阿贝尔化函子与包含函子的伴随关系](/library/volume-87/diagrams/pdf-0054-abelianization-adjunction.png)

其中 $U$ 是例 1.2.3(d) 中的包含函子。如果 $G$ 是一个群，那么 $F(G)$ 是 $G$ 的**阿贝尔化** $G_{\mathrm{ab}}$。这是 $G$ 的一个阿贝尔商群，具有如下性质：从 $G$ 到任意阿贝尔群的态射，都可以唯一地通过 $G_{\mathrm{ab}}$ 分解：

![阿贝尔化的泛性质](/library/volume-87/diagrams/pdf-0054-abelianization-universal.png)

这里 $\eta$ 是从 $G$ 到其商群 $G_{\mathrm{ab}}$ 的自然映射，$A$ 是任意阿贝尔群。（我们采用了例 (a) 中预告的记号滥用，在此图的几处省略了符号 $U$。）双射

$$
\mathbf{Ab}(G_{\mathrm{ab}},A)\cong\mathbf{Grp}(G,U(A))
$$

从左到右由 $\psi\mapsto\psi\circ\eta$ 给出，从右到左由 $\phi\mapsto\bar{\phi}$ 给出。

（为了构造 $G_{\mathrm{ab}}$，令 $G'$ 为 $G$ 中包含所有 $xyx^{-1}y^{-1}$（$x,y\in G$）的最小正规子群，并令 $G_{\mathrm{ab}}=G/G'$。从 $G$ 到任意阿贝尔群的同态的核都包含 $G'$，从而得到上述泛性质。）

(d) 群的范畴与幺半群的范畴之间有伴随关系

![群到幺半群的包含函子的左伴随与右伴随](/library/volume-87/diagrams/pdf-0054-group-monoid-adjunctions.png)

中间的函子 $U$ 是包含函子。左伴随 $F$ 同样不容易显式描述。非正式地说，$F(M)$ 是在 $M$ 中为每个元素添入一个逆元而得到的。（例如，如果 $M$ 是自然数的加法幺半群，那么 $F(M)$ 就是整数群。）一般伴随函子定理（定理 6.3.10）同样保证了这个伴随的存在。

这个例子比较特殊，因为遗忘函子通常没有*右*伴随。这里，给定幺半群 $M$，群 $R(M)$ 是由 $M$ 中所有可逆元素构成的子幺半群。

<span class="original-page-anchor" id="pdf-page-55" aria-hidden="true"></span>

范畴 $\mathbf{Grp}$ 既是 $\mathbf{Mon}$ 的**反射**子范畴，也是它的**余反射**子范畴。按定义，这意味着包含函子 $\mathbf{Grp}\hookrightarrow\mathbf{Mon}$ 同时有左伴随和右伴随。前一个例子告诉我们，$\mathbf{Ab}$ 是 $\mathbf{Grp}$ 的反射子范畴。

(e) 令 $\mathbf{Field}$ 为域的范畴，以环同态为态射。遗忘函子 $\mathbf{Field}\to\mathbf{Set}$ *没有*左伴随。（证明见例 6.3.5。）域的理论不同于群、环等等的理论，因为运算 $x\mapsto x^{-1}$ 并非对*所有* $x$ 都有定义（仅在 $x\ne0$ 时有定义）。

**注记 2.1.4** 本书有几处会谈到**代数理论**这一概念。你已经知道若干例子：群的理论是一种代数理论，环的理论、$\mathbb{R}$ 上向量空间的理论、$\mathbb{C}$ 上向量空间的理论、幺半群的理论，以及（相当平凡的）集合的理论也都是。读完下面的描述，你可能觉得“理论”这个词用得有点大，不如“定义”贴切。不过，这已经是约定俗成的用法。

我们不需要正式定义“代数理论”，但了解其大体思想很重要。先从群的理论开始考虑。

群可以定义为一个集合 $X$，配备一个函数 $\cdot\colon X\times X\to X$（乘法）、另一个函数 $(\ )^{-1}\colon X\to X$（取逆），以及一个元素 $e\in X$（单位元），它们满足一组熟悉的等式。更系统地说，$X$ 上的这三项结构可看作集合间的映射

$$
\cdot\colon X^2\to X,\qquad
(\ )^{-1}\colon X^1\to X,\qquad
e\colon X^0\to X,
$$

其中最后一种情况下，$X^0$ 是单元素集合 $1$，并且我们用到了如下观察：集合间的映射 $1\to X$ 与 $X$ 的一个元素本质上是同一回事。

（你可能更熟悉这样一种群的定义：只把乘法，也许还有单位元，列为*结构*的一部分，而把逆元的存在作为一条*性质*来要求。在这种定义之后，通常紧接着就会证明一条关于逆元唯一性的引理，保证谈论某个元素的*逆元*是有意义的。这两种途径是等价的，但在许多情况下，采用上一段的定义方式会更好。）

一个代数理论由两部分组成：第一，一族运算，每个运算都指定了元数（输入的个数）；第二，一族等式。例如，群的理论有一个元数为 $2$ 的运算、一个元数为 $1$ 的运算和一个元数为 $0$ 的运算。一个代数理论的**代数**或**模型**，就是一个集合 $X$，再为每个运算指定一个映射 $X^n\to X$，其中该运算的<span class="original-page-anchor" id="pdf-page-56" aria-hidden="true"></span>元数为 $n$，并且这些等式处处成立。例如，群的理论的一个代数恰好就是一个群。

一个更微妙的例子是 $\mathbb{R}$ 上向量空间的理论。这是一个代数理论，其中除了其他运算之外，还有无穷多个元数为 $1$ 的运算：对每个 $\lambda\in\mathbb{R}$，我们都有用 $\lambda$ 作标量乘法的运算 $\lambda\cdot-\colon X\to X$（对于任意向量空间 $X$）。这里的域 $\mathbb{R}$ 并没有什么特殊之处，关键只是它已经事先选定。$\mathbb{R}$ 上向量空间的理论与 $\mathbb{C}$ 上向量空间的理论不同，因为它们具有不同的元数为 $1$ 的运算。

简而言之，代数理论的代数主要有这样一个特点：运算在整个集合上处处有定义，等式也处处成立。例如，群的*每个*元素都有一个指定的逆元，且*每个*元素 $x$ 都满足等式 $x\cdot x^{-1}=1$。这就是群、环等等的理论是代数理论，而域的理论不是的原因。

**例 2.1.5** 有伴随关系

![离散拓扑和平庸拓扑所给出的伴随关系](/library/volume-87/diagrams/pdf-0056-topology-adjunctions.png)

其中 $U$ 把一个空间送到它的点集，$D$ 为一个集合赋予离散拓扑，$I$ 为一个集合赋予平庸拓扑。

**例 2.1.6** 给定集合 $A$ 和 $B$，可以构造它们的（笛卡尔）积 $A\times B$。也可以构造由从 $A$ 到 $B$ 的函数组成的集合 $B^A$。这与集合 $\mathbf{Set}(A,B)$ 相同，但当我们想强调它与 $A$ 和 $B$ 一样，都是这个范畴的对象时，往往使用记号 $B^A$。

现在固定一个集合 $B$。与 $B$ 取积定义了一个函子

$$
\begin{array}{cccc}
-\times B\colon&\mathbf{Set}&\to&\mathbf{Set}\\
&A&\mapsto&A\times B.
\end{array}
$$

（这里我们使用了例 1.2.12 中引入的空位记号。）还有一个函子

$$
\begin{array}{cccc}
(-)^B\colon&\mathbf{Set}&\to&\mathbf{Set}\\
&C&\mapsto&C^B.
\end{array}
$$

此外，对任意集合 $A$ 和 $C$，都有一个典范双射

$$
\mathbf{Set}(A\times B,C)\cong\mathbf{Set}(A,C^B).
$$

定义这个双射只需调整一下标点：给定一个

<span class="original-page-anchor" id="pdf-page-57" aria-hidden="true"></span>

![把曲面切成一族函数](/library/volume-87/diagrams/pdf-0057-figure-2-1.png)

*图 2.1* 在 $\mathbf{Set}$ 中，一个映射 $A\times B\to C$ 可以看作一种给 $A$ 的每个元素指定一个映射 $B\to C$ 的方式。

映射 $g\colon A\times B\to C$，通过

$$
(\bar{g}(a))(b)=g(a,b)
$$

（$a\in A$，$b\in B$）定义 $\bar{g}\colon A\to C^B$；反过来，给定 $f\colon A\to C^B$，通过

$$
\bar{f}(a,b)=(f(a))(b)
$$

（$a\in A$，$b\in B$）定义 $\bar{f}\colon A\times B\to C$。图 2.1 展示了 $A=B=C=\mathbb{R}$ 时的一个例子。像图中那样把曲面切成一片片，一个映射 $\mathbb{R}^2\to\mathbb{R}$ 就可看作从 $\mathbb{R}$ 到 $\{\text{映射 }\mathbb{R}\to\mathbb{R}\}$ 的映射。

综合上面的结果可知，对每个集合 $B$，都有伴随关系

![积与指数的伴随关系](/library/volume-87/diagrams/pdf-0057-product-exponential-adjunction.png)

**定义 2.1.7** 设 $\mathscr{A}$ 是一个范畴。如果对于每个 $A\in\mathscr{A}$，都恰好有一个态射 $I\to A$，就称对象 $I\in\mathscr{A}$ 是**始对象**。如果对于每个 $A\in\mathscr{A}$，都恰好有一个态射 $A\to T$，就称对象 $T\in\mathscr{A}$ 是**终对象**。

例如，空集是 $\mathbf{Set}$ 中的始对象，平凡群是 $\mathbf{Grp}$ 中的始对象，而 $\mathbb{Z}$ 是 $\mathbf{Ring}$ 中的始对象（例 0.2）。单元素集合是 $\mathbf{Set}$ 中的终对象，平凡群在 $\mathbf{Grp}$ 中既是终对象也是始对象，平凡（单元素）环则是 $\mathbf{Ring}$ 中的终对象。$\mathbf{CAT}$ 的终对象是范畴 $\mathbf{1}$，它仅包含一个对象和一个态射（必然是该对象上的恒等态射）。

一个范畴不一定有始对象，但如果有，那么它在同构意义下是唯一的。事实上，任意两个始对象之间的同构也只有*一个*，证明如下。

<span class="original-page-anchor" id="pdf-page-58" aria-hidden="true"></span>

**引理 2.1.8** 设 $I$ 和 $I'$ 是一个范畴的始对象。那么存在唯一的同构 $I \to I'$。特别地，$I \cong I'$。

**证明** 由于 $I$ 是始对象，存在唯一的态射 $f: I \to I'$。由于 $I'$ 是始对象，存在唯一的态射 $f': I' \to I$。现在，$f' \circ f$ 和 $1_I$ 都是态射 $I \to I$，而 $I$ 是始对象，所以 $f' \circ f = 1_I$。同样，$f \circ f' = 1_{I'}$。因此 $f$ 是同构，结论得证。$\square$

**例 2.1.9** 始对象和终对象可以用伴随来描述。设 $\mathscr{A}$ 是一个范畴。函子 $\mathscr{A} \to \mathbf{1}$ 恰好有一个。另外，函子 $\mathbf{1} \to \mathscr{A}$ 实质上就是 $\mathscr{A}$ 的一个对象（也就是 $\mathbf{1}$ 的唯一对象所映到的对象）。把函子 $\mathbf{1} \to \mathscr{A}$ 看作 $\mathscr{A}$ 的对象后，$\mathscr{A} \to \mathbf{1}$ 的左伴随恰好就是 $\mathscr{A}$ 的始对象。

同样，唯一函子 $\mathscr{A} \to \mathbf{1}$ 的右伴随恰好是 $\mathscr{A}$ 的终对象。

**注 2.1.10** 用注 1.1.10 引入的语言来说，终对象的概念与始对象的概念对偶。（更一般地，左伴随与右伴随的概念互相对偶。）由于一个范畴的任意两个始对象之间存在唯一的同构，对偶原理意味着终对象也有同样的性质。

**注 2.1.11** 伴随关系可以复合。取伴随关系

![两个可复合的伴随关系](/library/volume-87/diagrams/pdf-0058-composed-adjunctions.png)

其中符号 $\perp$ 是旋转后的 $\dashv$（因此，$F \dashv G$ 且 $F' \dashv G'$）。于是得到伴随关系

![复合后的伴随关系](/library/volume-87/diagrams/pdf-0058-composite-adjunction.png)

因为对于 $A \in \mathscr{A}$ 和 $A'' \in \mathscr{A}''$，有

$$
\mathscr{A}''\bigl(F'(F(A)), A''\bigr) \cong \mathscr{A}'\bigl(F(A), G'(A'')\bigr) \cong \mathscr{A}\bigl(A, G(G'(A''))\bigr)
$$

并且这些同构关于 $A$ 和 $A''$ 自然。

### 习题

**2.1.12** 找出三个上文未提到的伴随函子例子。对始对象和终对象也做同样的事。

**2.1.13** 关于离散范畴之间的伴随关系，能说些什么？

<span class="original-page-anchor" id="pdf-page-59" aria-hidden="true"></span>

**2.1.14** 证明，自然性等式 (2.2) 和 (2.3) 可以等价地用下面一个等式来替代：

$$
\overline{\Bigl(A' \xrightarrow{p} A \xrightarrow{f} G(B) \xrightarrow{G(q)} G(B')\Bigr)}
= \Bigl(F(A') \xrightarrow{F(p)} F(A) \xrightarrow{\bar{f}} B \xrightarrow{q} B'\Bigr)
$$

其中 $p$、$f$ 和 $q$ 任意。

**2.1.15** 证明左伴随保持始对象：也就是说，如果

![一个伴随关系](/library/volume-87/diagrams/pdf-0059-adjunction.png)

且 $I$ 是 $\mathscr{A}$ 的始对象，那么 $F(I)$ 是 $\mathscr{B}$ 的始对象。对偶地，证明右伴随保持终对象。

（在第 6.3 节，我们将看到，这是一个更大图景的一部分：右伴随保持极限，左伴随保持余极限。）

**2.1.16** 设 $G$ 是一个群。

(a) 在 $\mathbf{Set}$ 与左 $G$-集的范畴 $[G, \mathbf{Set}]$ 之间（任一方向），有哪些有趣的函子？这些函子中哪些与哪些伴随？

(b) 同样，在 $\mathbf{Vect}_k$ 与 $G$ 的 $k$-线性表示的范畴 $[G, \mathbf{Vect}_k]$ 之间有哪些有趣的函子？这些函子之间有哪些伴随关系？

**2.1.17** 固定一个拓扑空间 $X$，用 $\mathscr{O}(X)$ 表示 $X$ 的开子集按包含关系排序所成的偏序集。令

$$
\Delta: \mathbf{Set} \to [\mathscr{O}(X)^{\mathrm{op}}, \mathbf{Set}]
$$

为如下函子：它把集合 $A$ 映到常值为 $A$ 的预层 $\Delta A$。给出一串伴随函子

$$
\Lambda \dashv \Pi \dashv \Delta \dashv \Gamma \dashv \nabla.
$$

## 2.2 通过单位和余单位描述伴随关系

上一节介绍了伴随关系的定义。本节和下一节将分别介绍这个定义的另一种表述。本节的表述最适合用于理论研究，下一节的表述则与许多例子十分契合。

要开始建立伴随函子的理论，就必须认真对待自然性要求（等式 (2.2) 和 (2.3)）；到目前为止，它一直被<span class="original-page-anchor" id="pdf-page-60" aria-hidden="true"></span>忽略。取伴随关系：

![一个伴随关系](/library/volume-87/diagrams/pdf-0060-adjunction.png)

直观地说，自然性意味着，当 $A$ 在 $\mathscr{A}$ 中变化、$B$ 在 $\mathscr{B}$ 中变化时，$\mathscr{B}(F(A), B)$ 与 $\mathscr{A}(A, G(B))$ 之间的同构也随之变化，而且这种变化与已有的全部结构相容。换句话说，它与范畴 $\mathscr{A}$ 和 $\mathscr{B}$ 中的复合以及函子 $F$ 和 $G$ 的作用相容。

但“相容”是什么意思？例如，假设在 $\mathscr{B}$ 中有态射：

$$
F(A) \xrightarrow{g} B \xrightarrow{q} B'
$$

对这些态射，有两种操作：先复合再取转置，得到态射 $\overline{q \circ g}: A \to G(B')$；或者先取 $g$ 的转置，再与 $G(q)$ 复合，得到一个可能不同的态射 $G(q) \circ \bar{g}: A \to G(B')$。相容性意味着这两个态射相等，这正是第一个自然性等式 (2.2)。第二个等式是它的对偶，可以作类似解释。

对于每个 $A \in \mathscr{A}$，有态射

$$
\Bigl(A \xrightarrow{\eta_A} GF(A)\Bigr) = \overline{\Bigl(F(A) \xrightarrow{1} F(A)\Bigr)}.
$$

对偶地，对于每个 $B \in \mathscr{B}$，有态射

$$
\Bigl(FG(B) \xrightarrow{\varepsilon_B} B\Bigr) = \overline{\Bigl(G(B) \xrightarrow{1} G(B)\Bigr)}.
$$

（我们开始省略括号，用 $GF(A)$ 代替 $G(F(A))$，等等。）这些态射定义了自然变换

$$
\eta: 1_{\mathscr{A}} \to G \circ F, \qquad \varepsilon: F \circ G \to 1_{\mathscr{B}},
$$

分别称为伴随关系的**单位**和**余单位**。

**例 2.2.1** 取通常的伴随关系：

![向量空间与集合之间的伴随关系](/library/volume-87/diagrams/pdf-0060-vector-adjunction.png)

它的单位 $\eta: 1_{\mathbf{Set}} \to U \circ F$ 的分量为

$$
\begin{array}{rcl}
\eta_S: S &\to& UF(S) = \bigl\{\text{形式 } k\text{-线性和 }\sum_{s \in S} \lambda_s s\bigr\} \\
s &\mapsto& s
\end{array}
$$

（$S \in \mathbf{Set}$）。余单位 $\varepsilon$ 在向量空间 $V$ 处的分量是线性映射

$$
\varepsilon_V: FU(V) \to V
$$

它把*形式*线性和 $\sum_{v \in V} \lambda_v v$ 映到这个和在 $V$ 中的*实际*值。

向量空间 $FU(V)$ 非常庞大。例如，若 $k = \mathbb{R}$，且 $V$ 是向量空间 $\mathbb{R}^2$，则 $U(V)$ 是集合 $\mathbb{R}^2$，而 $FU(V)$ 是一个向量空间，其中<span class="original-page-anchor" id="pdf-page-61" aria-hidden="true"></span>对 $\mathbb{R}^2$ 的每个元素都有一个基元素；因此，它是不可数无限维的。于是 $\varepsilon_V$ 是从这个无限维空间到 $2$ 维空间 $V$ 的映射。

**引理 2.2.2** 给定伴随关系 $F \dashv G$，其单位为 $\eta$、余单位为 $\varepsilon$，则三角形

![函子的三角恒等式](/library/volume-87/diagrams/pdf-0061-triangle-identities.png)

交换。

**注 2.2.3** 这些等式称为**三角恒等式**。它们分别是函子范畴 $[\mathscr{A}, \mathscr{B}]$ 和 $[\mathscr{B}, \mathscr{A}]$ 中的交换图。有关记号的解释，参见注 1.3.24（特别是第 37 页提到的特殊情形）。等价的表述是，三角形

![分量的三角恒等式，等式 (2.4)](/library/volume-87/diagrams/pdf-0061-component-triangles.png)

对于所有 $A \in \mathscr{A}$ 和 $B \in \mathscr{B}$ 都交换。

**引理 2.2.2 的证明** 我们来证明三角形 (2.4) 交换。设 $A \in \mathscr{A}$。由于 $\overline{1_{GF(A)}} = \varepsilon_{F(A)}$，由等式 (2.3) 得到

$$
\overline{\Bigl(A \xrightarrow{\eta_A} GF(A) \xrightarrow{1} GF(A)\Bigr)}
= \Bigl(F(A) \xrightarrow{F(\eta_A)} FGF(A) \xrightarrow{\varepsilon_{F(A)}} F(A)\Bigr).
$$

而左边是 $\overline{\eta_A} = \overline{\overline{1_{F(A)}}} = 1_{F(A)}$，这就证明了第一个恒等式。第二个由对偶性得到。$\square$

令人惊讶的是，虽然单位和余单位似乎只给出了*恒等态射*的转置，它们却能确定整个伴随关系。这是下面两个结果的主要内容。

**引理 2.2.4** 设

![一个伴随关系](/library/volume-87/diagrams/pdf-0061-adjunction.png)

是一个伴随关系，其单位为 $\eta$、余单位为 $\varepsilon$。则

$$
\bar{g} = G(g) \circ \eta_A
$$

<span class="original-page-anchor" id="pdf-page-62" aria-hidden="true"></span>

其中 $g: F(A) \to B$ 任意，并且

$$
\bar{f} = \varepsilon_B \circ F(f)
$$

其中 $f: A \to G(B)$ 任意。

**证明** 对于任意态射 $g: F(A) \to B$，有

$$
\begin{aligned}
\overline{\Bigl(F(A) \xrightarrow{g} B\Bigr)}
&= \overline{\Bigl(F(A) \xrightarrow{1} F(A) \xrightarrow{g} B\Bigr)} \\
&= \Bigl(A \xrightarrow{\eta_A} GF(A) \xrightarrow{G(g)} G(B)\Bigr)
\end{aligned}
$$

由等式 (2.2) 得到上述等式，也就证明了第一个断言。第二个由对偶性得到。$\square$

**定理 2.2.5** 取范畴和函子：

![两个方向相反的函子](/library/volume-87/diagrams/pdf-0062-functor-pair.png)

下列两者之间存在一一对应：

(a) $F$ 与 $G$ 之间的伴随关系（$F$ 在左，$G$ 在右）；

(b) 满足三角恒等式的自然变换对 $\Bigl(1_{\mathscr{A}} \xrightarrow{\eta} GF,\ FG \xrightarrow{\varepsilon} 1_{\mathscr{B}}\Bigr)$。

（回顾定义，$F$ 与 $G$ 之间的伴随关系，是对每个 $A$ 和 $B$ 选择同构 (2.1)，并满足自然性等式 (2.2) 和 (2.3)。）

**证明** 我们已经证明，$F$ 与 $G$ 之间的每个伴随关系都会给出满足三角恒等式的一对 $(\eta, \varepsilon)$。现在必须证明这个过程是双射。因此，取满足三角恒等式的一对自然变换 $(\eta, \varepsilon)$。我们必须证明，$F$ 与 $G$ 之间存在唯一的伴随关系，其单位为 $\eta$，余单位为 $\varepsilon$。

唯一性由引理 2.2.4 得到。为证明存在性，取 (b) 中的自然变换 $\eta$ 和 $\varepsilon$。对于每个 $A$ 和 $B$，定义如下两个函数

$$
\mathscr{B}(F(A), B) \rightleftarrows \mathscr{A}(A, G(B)), \tag{2.5}
$$

两个函数都用横线表示，具体定义如下。给定 $g \in \mathscr{B}(F(A), B)$，令 $\bar{g} = G(g) \circ \eta_A \in \mathscr{A}(A, G(B))$。同样，在相反方向上，令 $\bar{f} = \varepsilon_B \circ F(f)$。

我断言，对于每个 $A$ 和 $B$，两个函数 $g \mapsto \bar{g}$ 和 $f \mapsto \bar{f}$ 互为逆函数。事实上，给定 $\mathscr{B}$ 中的态射 $g: F(A) \to B$，我们有交换图

![证明转置函数互为逆函数的交换图](/library/volume-87/diagrams/pdf-0062-inverse-transposes.png)

<span class="original-page-anchor" id="pdf-page-63" aria-hidden="true"></span>

沿图的外缘从 $F(A)$ 到 $B$ 的一条路径所得的复合态射是

$$
\varepsilon_B \circ FG(g) \circ F(\eta_A) = \varepsilon_B \circ F(\bar{g}) = \bar{\bar{g}},
$$

沿另一条路径得到的则是 $g \circ 1 = g$，所以 $\bar{\bar{g}} = g$。对偶地，对 $\mathscr{A}$ 中的任意态射 $f: A \to G(B)$，都有 $\bar{\bar{f}} = f$。断言得证。

自然性等式 (2.2) 和 (2.3) 很容易核实，因此函数 (2.5) 定义了一个伴随关系。最后，这个伴随关系的单位和余单位分别是 $\eta$ 和 $\varepsilon$，因为单位在 $A$ 处的分量为

$$
\overline{1_{F(A)}} = G(1_{F(A)}) \circ \eta_A = 1 \circ \eta_A = \eta_A,
$$

余单位的情形由对偶性得到。$\square$

**推论 2.2.6** 取范畴和函子：

![两个方向相反的函子](/library/volume-87/diagrams/pdf-0063-functor-pair.png)

则 $F \dashv G$ 当且仅当存在满足三角恒等式的自然变换 $1 \xrightarrow{\eta} GF$ 和 $FG \xrightarrow{\varepsilon} 1$。$\square$

**例 2.2.7** 有序集之间的伴随关系由保序映射

![两个方向相反的保序映射](/library/volume-87/diagrams/pdf-0063-ordered-pair.png)

组成，并满足

$$
\forall a \in A,\ \forall b \in B, \qquad f(a) \leq b \iff a \leq g(b). \tag{2.6}
$$

这是因为，伴随关系定义中的同构 (2.1) 两边都是至多含一个元素的集合；这样的两个集合同构，当且仅当它们同时为空或同时非空。自然性要求 (2.2) 和 (2.3) 自动成立，因为在有序集中，任意两个定义域和余定义域相同的态射都相等。

回顾例 1.3.9，如果

![平行的保序映射](/library/volume-87/diagrams/pdf-0063-parallel-pair.png)

是有序集之间的保序映射，那么从 $p$ 到 $q$ 至多存在一个自然变换，并且存在这样的自然变换当且仅当对于所有 $c \in C$，都有 $p(c) \leq q(c)$。上述伴随关系的单位是说，对于所有 $a \in A$，都有 $a \leq gf(a)$；余单位是说，对于所有 $b \in B$，都有 $fg(b) \leq b$。三角恒等式没有增加任何信息，因为它们断言有序集中两个定义域和余定义域相同的态射相等。

对于有序集，推论 2.2.6 表明，条件 (2.6) 等价于：

$$
\forall a \in A,\ a \leq gf(a) \qquad \text{且} \qquad \forall b \in B,\ fg(b) \leq b.
$$

这一等价性也可以直接证明（习题 2.2.10）。

<span class="original-page-anchor" id="pdf-page-64" aria-hidden="true"></span>

例如，设 $X$ 是一个拓扑空间。取 $X$ 的闭子集所成的集合 $\mathscr{C}(X)$，以及 $X$ 的所有子集所成的集合 $\mathscr{P}(X)$，二者都按 $\subseteq$ 排序。有保序映射

![闭包映射与包含映射](/library/volume-87/diagrams/pdf-0064-closure-pair.png)

其中 $i$ 是包含映射，$\operatorname{Cl}$ 是闭包运算。这两个映射构成一个伴随关系，$\operatorname{Cl}$ 是 $i$ 的左伴随，因为

$$
\operatorname{Cl}(A) \subseteq B \iff A \subseteq B
$$

对所有 $A \subseteq X$ 和闭集 $B \subseteq X$ 都成立。也可以等价地表述为：对所有 $A \subseteq X$ 都有 $A \subseteq \operatorname{Cl}(A)$，对所有闭集 $B \subseteq X$ 都有 $\operatorname{Cl}(B) \subseteq B$。无论采用哪种表述，都可以看到，拓扑中的闭包运算是一个伴随函子。

**注 2.2.8** 定理 2.2.5 表明，伴随关系可以视为由函子和自然变换组成、并满足三角恒等式的四元组 $(F, G, \eta, \varepsilon)$。范畴的等价 $(F, G, \eta, \varepsilon)$（如定义 1.3.15 中所述）未必是伴随关系。$F$ *确实*是 $G$ 的左伴随（习题 2.3.10），但 $\eta$ 和 $\varepsilon$ 未必是单位和余单位（因为没有理由保证它们满足三角恒等式）。

**注 2.2.9** 有一种画自然变换的方法，使三角恒等式在直观上显得合理。例如，假设有范畴和函子

$$
\mathscr{A} \xrightarrow{F_1} \mathscr{C}_1 \xrightarrow{F_2} \mathscr{C}_2 \xrightarrow{F_3} \mathscr{C}_3 \xrightarrow{F_4} \mathscr{B}, \qquad \mathscr{A} \xrightarrow{G_1} \mathscr{D}_1 \xrightarrow{G_2} \mathscr{B}
$$

以及自然变换 $\alpha: F_4 F_3 F_2 F_1 \to G_2 G_1$。我们通常这样画 $\alpha$：

![自然变换通常的画法](/library/volume-87/diagrams/pdf-0064-natural-transformation.png)

然而，也可以将 $\alpha$ 画成**弦图**：

![自然变换的弦图](/library/volume-87/diagrams/pdf-0064-string-diagram.png)

<span class="original-page-anchor" id="pdf-page-65" aria-hidden="true"></span>

$4$ 和 $2$ 并没有特殊之处，可以用任意自然数 $m$ 和 $n$ 来代替。如果 $m = 0$，则 $\mathscr{A} = \mathscr{B}$，且 $\alpha$ 的定义域是 $1_{\mathscr{A}}$（请记住注 1.1.2(b) 的最后一段）。这时，标有 $\alpha$ 的圆盘上方没有弦接入。同样，如果 $n = 0$，则下方没有弦引出。

自然变换的垂直复合对应于将弦图上下连接，水平复合则对应于将它们并排放置。函子 $F$ 上的恒等自然变换画成一根简单的弦：

![函子上的恒等自然变换所对应的弦](/library/volume-87/diagrams/pdf-0065-identity-string.png)

现在将这种记号用于伴随关系。单位和余单位画成

![单位的弦图](/library/volume-87/diagrams/pdf-0065-unit-string.png)

和

![余单位的弦图](/library/volume-87/diagrams/pdf-0065-counit-string.png)

三角恒等式现在成为下面两个等式，从拓扑上看，它们很自然：

![$F$ 的三角恒等式的弦图](/library/volume-87/diagrams/pdf-0065-triangle-string-f.png)

和

![$G$ 的三角恒等式的弦图](/library/volume-87/diagrams/pdf-0065-triangle-string-g.png)

在两个等式中，只需将弦拉直，就从左边得到右边。

### 习题

**2.2.10** 设

![两个方向相反的保序映射](/library/volume-87/diagrams/pdf-0065-ordered-pair.png)

是有序集之间的保序映射。*直接*证明下列条件等价：

(a) 对于所有 $a \in A$ 和 $b \in B$，

$$
f(a) \leq b \iff a \leq g(b);
$$

<span class="original-page-anchor" id="pdf-page-66" aria-hidden="true"></span>

(b) 对所有 $a \in A$，都有 $a \leq g(f(a))$；对所有 $b \in B$，都有 $f(g(b)) \leq b$。

（这两个条件都表述了 $f \dashv g$；见例 2.2.7。）

**2.2.11** (a) 设

![伴随关系](/library/volume-87/diagrams/pdf-0066-adjunction-a.png)

是一个伴随关系，其单位为 $\eta$，余单位为 $\varepsilon$。用 $\mathbf{Fix}(GF)$ 表示 $\mathscr{A}$ 的充满子范畴，其对象是满足 $\eta_A$ 为同构的那些 $A \in \mathscr{A}$；对偶地定义 $\mathbf{Fix}(FG) \subseteq \mathscr{B}$。证明伴随关系 $(F,G,\eta,\varepsilon)$ 限制为 $\mathbf{Fix}(GF)$ 与 $\mathbf{Fix}(FG)$ 之间的等价 $(F',G',\eta',\varepsilon')$。

(b) (a) 表明，每个伴随关系都以典范的方式限制为充满子范畴之间的等价。选取几个伴随关系的例子，并求出这种等价是什么。

**2.2.12** (a) 证明：对于任意伴随关系，右伴随是充满且忠实的，当且仅当余单位是同构。

(b) 满足 (a) 中这些等价条件的伴随关系称为**反射**。（比较例 2.1.3(d)。）本章给出的伴随关系的例子中，哪些是反射？

**2.2.13** (a) 设 $f:K \to L$ 是集合间的映射，用 $f^*: \mathscr{P}(L) \to \mathscr{P}(K)$ 表示将 $L$ 的子集 $S$ 映到其逆像 $f^{-1}S \subseteq K$ 的映射。于是，关于 $\mathscr{P}(K)$ 和 $\mathscr{P}(L)$ 上的包含序，$f^*$ 是保序的，因此可以视为函子。求 $f^*$ 的左伴随和右伴随。

(b) 现在设 $X$ 和 $Y$ 是集合，用 $p:X \times Y \to X$ 表示第一投影。将 $X$ 的子集 $S$ 视为一个关于变量 $x \in X$ 的谓词 $S(x)$；类似地，将 $X \times Y$ 的子集 $R$ 视为二元谓词 $R(x,y)$。用谓词来表述，$p^*$ 的左伴随和右伴随是什么？对于每个伴随关系，将单位和余单位解释为逻辑蕴含。（提示：$p^*$ 的左伴随常记作 $\exists_Y$，右伴随常记作 $\forall_Y$。）

**2.2.14** 给定函子 $F:\mathscr{A} \to \mathscr{B}$ 和范畴 $\mathscr{S}$，有一个函子 $F^*:[\mathscr{B},\mathscr{S}] \to [\mathscr{A},\mathscr{S}]$，它在对象 $Y \in [\mathscr{B},\mathscr{S}]$ 上定义为 $F^*(Y)=Y \circ F$，在态射 $\alpha$ 上定义为 $F^*(\alpha)=\alpha F$。证明任意伴随关系

![伴随关系](/library/volume-87/diagrams/pdf-0066-adjunction-b.png)

和范畴 $\mathscr{S}$ 都产生一个伴随关系

![诱导的伴随关系](/library/volume-87/diagrams/pdf-0066-induced-adjunction.png)

（提示：使用定理 2.2.5。）

<span class="original-page-anchor" id="pdf-page-67" aria-hidden="true"></span>

## 2.3 通过始对象表述伴随关系

现在我们来到伴随性的第三种表述，这大概是你在日常数学中最常见到的表述。

再次考虑伴随关系

![自由函子与遗忘函子的伴随关系](/library/volume-87/diagrams/pdf-0067-free-forgetful.png)

设 $S$ 是集合。以 $S$ 为基的向量空间 $F(S)$ 的泛性质，最常表述如下：

> 给定向量空间 $V$，任意函数 $f:S \to V$ 都唯一地延拓为线性映射 $\bar f:F(S) \to V$。

如例 2.1.3(a) 所述，遗忘函子经常被遗忘：在这句话中，严格说来，‘$f:S \to V$’ 应该是 ‘$f:S \to U(V)$’。此外，‘延拓’ 一词隐含地涉及嵌入

$$
\begin{array}{rccc}
\eta_S:&S&\longrightarrow&UF(S)\\
&s&\longmapsto&s.
\end{array}
$$

因此，用精确的语言，这句话是：

> 对于任意 $V \in \mathbf{Vect}_k$ 和 $f \in \mathbf{Set}(S,U(V))$，存在唯一的 $\bar f \in \mathbf{Vect}_k(F(S),V)$，使得图

![泛性质 (2.7)](/library/volume-87/diagrams/pdf-0067-universal-property.png)

> 交换。

（比较例 0.4。）本节将证明，这句话等价于说 $F$ 是 $U$ 的左伴随，且单位为 $\eta$。

为此，我们需要一个定义。

**定义 2.3.1** 给定范畴和函子

![逗号范畴的输入函子](/library/volume-87/diagrams/pdf-0067-comma-input.png)

<span class="original-page-anchor" id="pdf-page-68" aria-hidden="true"></span>

**逗号范畴** $(P \Rightarrow Q)$（常记作 $(P \mathbin{\downarrow} Q)$）是按如下方式定义的范畴：

- 对象是三元组 $(A,h,B)$，其中 $A \in \mathscr{A}$，$B \in \mathscr{B}$，且 $h:P(A) \to Q(B)$ 是 $\mathscr{C}$ 中的态射；
- 态射 $(A,h,B) \to (A',h',B')$ 是态射对 $(f:A \to A',\,g:B \to B')$，使得方形图

![逗号范畴的态射方形图](/library/volume-87/diagrams/pdf-0068-comma-square.png)

交换。

**注 2.3.2** 给定如上的 $\mathscr{A}$、$\mathscr{B}$、$\mathscr{C}$、$P$ 和 $Q$，存在典范的函子和一个典范的自然变换，如图所示：

![典范函子及自然变换](/library/volume-87/diagrams/pdf-0068-comma-universal.png)

在适当的 2-范畴意义下，$(P \Rightarrow Q)$ 对于这一性质具有泛性。

**例 2.3.3** 设 $\mathscr{A}$ 是范畴，$A \in \mathscr{A}$。$\mathscr{A}$ 在 $A$ 上的**切片范畴**记作 $\mathscr{A}/A$，它的对象是指向 $A$ 的态射，它的态射是交换三角形。更精确地说，一个对象是二元组 $(X,h)$，其中 $X \in \mathscr{A}$，$h:X \to A$ 是 $\mathscr{A}$ 中的态射；$\mathscr{A}/A$ 中的态射 $(X,h) \to (X',h')$ 是 $\mathscr{A}$ 中的态射 $f:X \to X'$，使得三角形

![切片范畴的三角形](/library/volume-87/diagrams/pdf-0068-slice-triangle.png)

交换。

切片范畴是逗号范畴的特例。回忆例 2.1.9，函子 $\mathbf{1} \to \mathscr{A}$ 就是 $\mathscr{A}$ 的对象。现在给定 $\mathscr{A}$ 的对象 $A$，考虑逗号范畴 $(1_{\mathscr{A}} \Rightarrow A)$，如图所示：

![以逗号范畴表述切片范畴](/library/volume-87/diagrams/pdf-0068-slice-comma.png)

<span class="original-page-anchor" id="pdf-page-69" aria-hidden="true"></span>

原则上，$(1_{\mathscr{A}} \Rightarrow A)$ 的一个对象是三元组 $(X,h,B)$，其中 $X \in \mathscr{A}$，$B \in \mathbf{1}$，且 $h:X \to A$ 是 $\mathscr{A}$ 中的态射；但是 $\mathbf{1}$ 只有一个对象，所以它实质上只是一个二元组 $(X,h)$。因此，逗号范畴 $(1_{\mathscr{A}} \Rightarrow A)$ 与切片范畴 $\mathscr{A}/A$ 具有相同的对象。还可以核实它们具有相同的态射，所以 $\mathscr{A}/A \cong (1_{\mathscr{A}} \Rightarrow A)$。

对偶地（将所有箭头反向），有一个**余切片范畴** $A/\mathscr{A} \cong (A \Rightarrow 1_{\mathscr{A}})$，它的对象是从 $A$ 出发的态射。

**例 2.3.4** 设 $G:\mathscr{B} \to \mathscr{A}$ 是函子，$A \in \mathscr{A}$。可以构造逗号范畴 $(A \Rightarrow G)$，如图所示：

![逗号范畴的输入](/library/volume-87/diagrams/pdf-0069-comma-input.png)

它的对象是二元组 $(B \in \mathscr{B},\,f:A \to G(B))$。$(A \Rightarrow G)$ 中的态射 $(B,f) \to (B',f')$ 是 $\mathscr{B}$ 中的态射 $q:B \to B'$，使得三角形

![逗号范畴的态射三角形](/library/volume-87/diagrams/pdf-0069-comma-triangle.png)

交换。

注意，这张图与向量空间例子中的图 (2.7) 很相似。我们将用逗号范畴 $(A \Rightarrow G)$ 来刻画那里讨论的那一类泛性质。

在不严格的说法中，我们说 $f:A \to G(B)$ 是 $(A \Rightarrow G)$ 的一个对象，而真正应该说的是：二元组 $(B,f)$ 是 $(A \Rightarrow G)$ 的一个对象。这种说法有造成混淆的可能，因为 $\mathscr{B}$ 中可能有不同的对象 $B,B'$ 满足 $G(B)=G(B')$。尽管如此，我们还是会经常使用这一约定。

现在我们来建立逗号范畴与伴随关系之间的联系。

**引理 2.3.5** 取一个伴随关系

![伴随关系](/library/volume-87/diagrams/pdf-0069-lemma-adjunction.png)

以及一个对象 $A \in \mathscr{A}$。则单位态射 $\eta_A:A \to GF(A)$ 是 $(A \Rightarrow G)$ 的始对象。

**证明** 设 $(B,\,f:A \to G(B))$ 是 $(A \Rightarrow G)$ 的对象。我们要证明，从 $(F(A),\eta_A)$ 到 $(B,f)$ 恰有一个态射。

$(A \Rightarrow G)$ 中的态射 $(F(A),\eta_A) \to (B,f)$ 是 $\mathscr{B}$ 中的态射 $q:F(A) \to B$，使得<span class="original-page-anchor" id="pdf-page-70" aria-hidden="true"></span>图

![单位的始对象性质 (2.8)](/library/volume-87/diagrams/pdf-0070-unit-initial.png)

交换。但是由引理 2.2.4，$G(q) \circ \eta_A=\bar q$，所以 (2.8) 交换当且仅当 $f=\bar q$，也当且仅当 $q=\bar f$。因此，$\bar f$ 是 $(A \Rightarrow G)$ 中唯一的态射 $(F(A),\eta_A) \to (B,f)$。$\square$

现在我们来看伴随性的第三种、也是最后一种表述。

**定理 2.3.6** 取范畴和函子

![方向相反的函子](/library/volume-87/diagrams/pdf-0070-theorem-functors.png)。

以下两者之间存在一一对应：

(a) $F$ 与 $G$ 之间的伴随关系（$F$ 为左伴随，$G$ 为右伴随）；

(b) 自然变换 $\eta:1_{\mathscr{A}} \to GF$，使得对每个 $A \in \mathscr{A}$，$\eta_A:A \to GF(A)$ 都是 $(A \Rightarrow G)$ 中的始对象。

**证明** 我们刚刚证明，$F$ 与 $G$ 之间的每个伴随关系都会给出一个自然变换 $\eta$，具有 (b) 中所述的性质。要证明此定理，我们必须证明，具有 (b) 中性质的每个 $\eta$，都是 $F$ 与 $G$ 之间恰好一个伴随关系的单位。

由定理 2.2.5，$F$ 与 $G$ 之间的伴随关系相当于一对满足三角恒等式的自然变换 $(\eta,\varepsilon)$。因此，只需证明：对于具有 (b) 中性质的每个 $\eta$，存在唯一的自然变换 $\varepsilon:FG \to 1_{\mathscr{B}}$，使得 $(\eta,\varepsilon)$ 满足三角恒等式。

设 $\eta:1_{\mathscr{A}} \to GF$ 是具有 (b) 中性质的自然变换。

**唯一性** 假设 $\varepsilon,\varepsilon':FG \to 1_{\mathscr{B}}$ 是自然变换，并且 $(\eta,\varepsilon)$ 和 $(\eta,\varepsilon')$ 都满足三角恒等式。其中一条三角恒等式表明，对于所有 $B \in \mathscr{B}$，三角形

![第一条三角恒等式 (2.9)](/library/volume-87/diagrams/pdf-0070-triangle-identity.png)

交换。因此，$\varepsilon_B$ 是一个态射

$$
\Bigl(FG(B),\ G(B) \xrightarrow{\eta_{G(B)}} G(FG(B))\Bigr)
\longrightarrow
\Bigl(B,\ G(B) \xrightarrow{1} G(B)\Bigr)
$$

<span class="original-page-anchor" id="pdf-page-71" aria-hidden="true"></span>

它属于 $(G(B) \Rightarrow G)$。$\varepsilon'_B$ 也如此。但是 $\eta_{G(B)}$ 是始对象，所以这样的态射只有一个，因此 $\varepsilon_B=\varepsilon'_B$。这对所有 $B$ 都成立，所以 $\varepsilon=\varepsilon'$。

**存在性** 对于 $B \in \mathscr{B}$，定义 $\varepsilon_B:FG(B) \to B$ 为 $(G(B) \Rightarrow G)$ 中唯一的态射

$$
(FG(B),\eta_{G(B)}) \longrightarrow (B,1_{G(B)}).
$$

（所以根据 $\varepsilon_B$ 的定义，三角形 (2.9) 交换。）我们将证明 $(\varepsilon_B)_{B \in \mathscr{B}}$ 是自然变换 $FG \to 1$，且 $\eta$ 和 $\varepsilon$ 满足三角恒等式。

为证明自然性，取 $\mathscr{B}$ 中的 $B \xrightarrow{q} B'$。我们有交换图

![证明余单位自然性的图](/library/volume-87/diagrams/pdf-0071-counit-naturality.png)

所以 $q \circ \varepsilon_B$ 和 $\varepsilon_{B'} \circ FG(q)$ 都是 $(G(B) \Rightarrow G)$ 中的态射 $\eta_{G(B)} \to G(q)$；由于 $\eta_{G(B)}$ 是始对象，它们必然相等。这证明了 $\varepsilon$ 关于 $q$ 的自然性。因此，$\varepsilon$ 是自然变换。

我们已经注意到，一条三角恒等式，即等式 (2.9)，成立。另一条表明，对于 $A \in \mathscr{A}$，图

![第二条三角恒等式](/library/volume-87/diagrams/pdf-0071-second-triangle.png)

交换。为证明它，我们重复先前的方法：有交换图

![通过始对象性质证明第二条三角恒等式的图](/library/volume-87/diagrams/pdf-0071-initiality-diagrams.png)

<span class="original-page-anchor" id="pdf-page-72" aria-hidden="true"></span>

因此，由 $\eta_A$ 的始对象性质，有 $\varepsilon_{F(A)} \circ F(\eta_A)=1_{F(A)}$，得到所需结论。$\square$

在 6.3 节，我们将遇到伴随函子定理，它们给出保证一个函子具有左伴随的条件。以下推论是这些定理证明的出发点。

**推论 2.3.7** 设 $G:\mathscr{B} \to \mathscr{A}$ 是函子。则 $G$ 具有左伴随，当且仅当对每个 $A \in \mathscr{A}$，范畴 $(A \Rightarrow G)$ 都具有始对象。

**证明** 引理 2.3.5 已经证明了必要性。为证明充分性，对每个 $A \in \mathscr{A}$，选取 $(A \Rightarrow G)$ 的一个始对象，并将它记作 $(F(A),\,\eta_A:A \to GF(A))$。（这里 $F(A)$ 和 $\eta_A$ 只是我们选用的名称。）对于 $\mathscr{A}$ 中的每个态射 $f:A \to A'$，令 $F(f):F(A) \to F(A')$ 为使下图交换的唯一态射：

![左伴随的构造](/library/volume-87/diagrams/pdf-0072-left-adjoint-construction.png)

换句话说，它是 $(A \Rightarrow G)$ 中唯一的态射 $\eta_A \to \eta_{A'} \circ f$。容易核实 $F$ 是函子 $\mathscr{A} \to \mathscr{B}$，而这张图告诉我们 $\eta$ 是自然变换 $1 \to GF$。因此由定理 2.3.6，$F$ 是 $G$ 的左伴随。$\square$

这一推论说明本节开头的断言成立：给定函子 $F$ 和 $G$，具有一个伴随关系 $F \dashv G$，就相当于具有满足那里所述泛性质的态射 $\eta_A:A \to GF(A)$。

### 练习

**2.3.8** 对于群之间的伴随关系（将群视为单对象范畴），可以得出什么结论？

**2.3.9** 陈述推论 2.3.7 的对偶。你会如何证明这一对偶命题？

**2.3.10** 设 $(F,G,\eta,\varepsilon)$ 是定义 1.3.15 中的范畴等价。证明 $F$ 是 $G$ 的左伴随（注意注 2.2.8 中的提醒）。

**2.3.11** 设

![与集合范畴的伴随关系](/library/volume-87/diagrams/pdf-0072-exercise-adjunction.png)

是一个伴随关系。假设至少有一个 $A \in \mathscr{A}$，使得集合 $U(A)$ 至少有两个元素。证明对每个集合 $S$，单位态射 $\eta_S:S \to UF(S)$ 都是单射。在 $\mathbf{Grp}$ 与 $\mathbf{Set}$ 之间通常的伴随关系中，这意味着什么？

<span class="original-page-anchor" id="pdf-page-73" aria-hidden="true"></span>

**2.3.12** 给定集合 $A$ 和 $B$，从 $A$ 到 $B$ 的**部分函数**是一个二元组 $(S,f)$，由子集 $S \subseteq A$ 和函数 $S \to B$ 组成。（可以把它想成从 $A$ 到 $B$ 的函数，不过在 $A$ 的某些元素处没有定义。）令 $\mathbf{Par}$ 为集合与部分函数组成的范畴。

证明 $\mathbf{Par}$ 等价于 $\mathbf{Set}_*$，后者是带有指定元素的集合以及保持指定元素的函数所组成的范畴。再证明 $\mathbf{Set}_*$ 可以用简单的方式描述为一个余切片范畴。
