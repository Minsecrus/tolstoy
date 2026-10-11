---
title: "第四章 可表函子"
description: "Tom Leinster《Basic Category Theory》中文译文。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"第三章 集合论插曲","link":"/library/volume-87/chapter-003"}
next: {"text":"第五章 极限","link":"/library/volume-87/chapter-005"}
---

# 第四章 可表函子

<span class="original-page-anchor" id="pdf-page-92" aria-hidden="true"></span>

一个范畴是由对象构成的世界，所有对象都在彼此观察。每个对象从不同的视角看这个世界。

例如，考虑拓扑空间范畴，并问：从单点空间 $1$ 出发观察，它是什么样的？从 $1$ 到空间 $X$ 的一个态射，本质上就等同于 $X$ 的一个点，因此我们可以说 $1$“看见点”。类似地，从 $\mathbb{R}$ 到空间 $X$ 的态射可以合理地称为 $X$ 中的一条曲线；在这个意义上，$\mathbb{R}$ 看见曲线。

现在考虑群范畴。从无限循环群 $\mathbb{Z}$ 到群 $G$ 的一个态射，就相当于 $G$ 的一个元素。（因为给定 $g\in G$，存在唯一的同态 $\phi:\mathbb{Z}\to G$，使得 $\phi(1)=g$。）所以，$\mathbb{Z}$ 看见元素。类似地，如果 $p$ 是素数，那么循环群 $\mathbb{Z}/p\mathbb{Z}$ 看见阶为 $1$ 或 $p$ 的元素。

域之间的任何环同态都是单射，所以在域范畴中，一个态射 $K\to L$ 就是将 $L$ 实现为 $K$ 的一个扩张的方式。因此，每个域 $K$ 都看见自身的扩张。如果 $K$ 和 $L$ 是特征不同的域，那么 $K$ 与 $L$ 之间不存在同态，所以域范畴是不相交的子范畴 $\mathbf{Field}_0$、$\mathbf{Field}_2$、$\mathbf{Field}_3$、$\mathbf{Field}_5$、$\ldots$ 的并；这些子范畴分别由特征为 $0$、$2$、$3$、$5$、$\ldots$ 的域组成。每个域都看不见特征不同的域。

在有序集 $(\mathbb{R},\leq)$ 中，对象 $0$ 能看出一个数是否非负。也就是说，如果 $x$ 非负，就有一个态射 $0\to x$；否则就没有这样的态射。

我们还可以提出对偶的问题：固定范畴的一个对象，映*入*它的态射有哪些？例如，设 $S$ 为两元素集合。对于任意集合 $X$，从 $X$ 到 $S$ 的态射对应于 $X$ 的子集（正如我们在第 3.1 节所看到的）。现在赋予 $S$ 一个拓扑，使其中一个单元素子集是开的，而另一个不是开的。对于任意拓扑空间 $X$，从 $X$ 到 $S$ 的连续映射对应于 $X$ 的*开*子集。

<span class="original-page-anchor" id="pdf-page-93" aria-hidden="true"></span>

本章探讨的主题是：每个对象如何观察它所处的范畴，以及它如何被这个范畴观察。这自然引出可表函子的概念；在伴随关系之后，它提供了理解泛性质思想的第二种途径。

## 4.1 定义与例子

固定范畴 $\mathscr{A}$ 的一个对象 $A$。我们将考虑从 $A$ 出发的全体态射。对每个 $B\in\mathscr{A}$，指定从 $A$ 到 $B$ 的态射组成的集合（或类）$\mathscr{A}(A,B)$。下面的定义说明，这一指定对 $B$ 而言具有函子性：任意态射 $B\to B'$ 都诱导一个函数 $\mathscr{A}(A,B)\to\mathscr{A}(A,B')$。

**定义 4.1.1** 设 $\mathscr{A}$ 为局部小范畴，$A\in\mathscr{A}$。我们如下定义函子

$$
H^A=\mathscr{A}(A,-):\mathscr{A}\to\mathbf{Set}:
$$

- 对对象 $B\in\mathscr{A}$，令 $H^A(B)=\mathscr{A}(A,B)$；
- 对 $\mathscr{A}$ 中的态射 $B\xrightarrow{g}B'$，定义

  $$
  H^A(g)=\mathscr{A}(A,g):\mathscr{A}(A,B)\to\mathscr{A}(A,B')
  $$

  其作用为

  $$
  p\mapsto g\circ p,
  $$

  其中 $p:A\to B$ 任意。

**注 4.1.2** (a) 回忆，“局部小”意味着每个类 $\mathscr{A}(A,B)$ 实际上都是一个集合。要使这一定义有意义，这个假设显然是必要的。

(b) 有时将 $H^A(g)$ 写作 $g\circ-$ 或 $g_*$。这三种写法以及 $\mathscr{A}(A,g)$ 都有人使用。

**定义 4.1.3** 设 $\mathscr{A}$ 为局部小范畴。如果对某个 $A\in\mathscr{A}$ 有 $X\cong H^A$，就称函子 $X:\mathscr{A}\to\mathbf{Set}$ 是**可表的**。$X$ 的一个**表示**，就是选定一个对象 $A\in\mathscr{A}$，以及 $H^A$ 与 $X$ 之间的一个同构。

可表函子有时也简称为“可表者”。只有集合值函子（即以 $\mathbf{Set}$ 为陪域的函子）才可能是可表的。

<span class="original-page-anchor" id="pdf-page-94" aria-hidden="true"></span>

**例 4.1.4** 考虑 $H^1:\mathbf{Set}\to\mathbf{Set}$，其中 $1$ 是单元素集合。从 $1$ 到集合 $B$ 的一个态射，就相当于 $B$ 的一个元素，因此对每个 $B\in\mathbf{Set}$ 都有

$$
H^1(B)\cong B.
$$

容易验证，这个同构对 $B$ 是自然的，所以 $H^1$ 与恒等函子 $1_{\mathbf{Set}}$ 同构。因此 $1_{\mathbf{Set}}$ 是可表函子。

**例 4.1.5** 本章引言中所有用于“观察”的函子都是可表函子。遗忘函子 $\mathbf{Top}\to\mathbf{Set}$ 与 $H^1=\mathbf{Top}(1,-)$ 同构，而遗忘函子 $\mathbf{Grp}\to\mathbf{Set}$ 与 $\mathbf{Grp}(\mathbb{Z},-)$ 同构。对每个素数 $p$，有一个函子 $U_p:\mathbf{Grp}\to\mathbf{Set}$，它在对象上的定义为

$$
U_p(G)=\{G\text{ 中阶为 }1\text{ 或 }p\text{ 的元素}\},
$$

并且如前所述，$U_p\cong\mathbf{Grp}(\mathbb{Z}/p\mathbb{Z},-)$（练习 4.1.28）。因此 $U_p$ 是可表函子。

**例 4.1.6** 有一个函子 $\operatorname{ob}:\mathbf{Cat}\to\mathbf{Set}$，将小范畴送到其对象集。（范畴 $\mathbf{Cat}$ 在定义 3.2.10 中引入。）这个函子是可表的。事实上，考虑终范畴 $\mathbf{1}$（只有一个对象和一个恒等态射）。从 $\mathbf{1}$ 到范畴 $\mathscr{B}$ 的函子，只是从 $\mathscr{B}$ 中选出一个对象。因此，

$$
H^{\mathbf{1}}(\mathscr{B})\cong\operatorname{ob}\mathscr{B}.
$$

同样，容易验证这个同构对 $\mathscr{B}$ 是自然的；因此 $\operatorname{ob}\cong\mathbf{Cat}(\mathbf{1},-)$。类似地可以证明，将小范畴送到其态射集的函子 $\mathbf{Cat}\to\mathbf{Set}$ 也是可表的（练习 4.1.31）。

**例 4.1.7** 设 $M$ 为幺半群，将其视为单对象范畴。回忆例 1.2.8，$M$ 上的集合值函子就是一个 $M$-集。由于范畴 $M$ 只有一个对象，其上的可表函子也只有一个（在同构意义下）。作为一个 $M$-集，这个唯一的可表函子就是所谓的 $M$ 的**左正则表示**，即 $M$ 的底层集合，作用由左乘给出。

**例 4.1.8** 设 $\mathbf{Toph}_*$ 为如下范畴：对象是配备了基点的拓扑空间，态射是保持基点的连续映射的同伦类。设 $S^1\in\mathbf{Toph}_*$ 为圆。则对任意对象 $X\in\mathbf{Toph}_*$，$\mathbf{Toph}_*$ 中的态射 $S^1\to X$ 就是基本群 $\pi_1(X)$ 的元素。形式化地说，复合函子

$$
\mathbf{Toph}_*\xrightarrow{\pi_1}\mathbf{Grp}\xrightarrow{U}\mathbf{Set}
$$

与 $\mathbf{Toph}_*(S^1,-)$ 同构。特别地，它是可表函子。

<span class="original-page-anchor" id="pdf-page-95" aria-hidden="true"></span>

**例 4.1.9** 固定一个域 $k$ 以及 $k$ 上的向量空间 $U$ 和 $V$。有一个函子

$$
\mathbf{Bilin}(U,V;-):\mathbf{Vect}_k\to\mathbf{Set},
$$

它在 $W\in\mathbf{Vect}_k$ 处的值 $\mathbf{Bilin}(U,V;W)$ 是所有双线性映射 $U\times V\to W$ 构成的集合。可以证明，这个函子是可表的；换句话说，存在一个空间 $T$，使得

$$
\mathbf{Bilin}(U,V;W)\cong\mathbf{Vect}_k(T,W),
$$

并且这个同构对 $W$ 是自然的。这个 $T$ 就是张量积 $U\otimes V$，我们在引理 0.7 的证明之后已经遇到过它。

伴随关系可以通过如下方式产生可表函子。

**引理 4.1.10** 设下图中的范畴均为局部小范畴，并令 $A\in\mathscr{A}$。

![伴随关系](/library/volume-87/diagrams/pdf-0095-adjunction.png)

那么函子

$$
\mathscr{A}(A,G(-)):\mathscr{B}\to\mathbf{Set}
$$

（即复合 $\mathscr{B}\xrightarrow{G}\mathscr{A}\xrightarrow{H^A}\mathbf{Set}$）是可表的。

**证明** 对每个 $B\in\mathscr{B}$ 都有

$$
\mathscr{A}(A,G(B))\cong\mathscr{B}(F(A),B).
$$

如果能够证明这个同构对 $B$ 是自然的，我们就证明了 $\mathscr{A}(A,G(-))$ 与 $H^{F(A)}$ 同构，因此它是可表函子。于是，取 $\mathscr{B}$ 中的一个态射 $B\xrightarrow{q}B'$。我们必须证明下面的方块交换：

![自然性方块](/library/volume-87/diagrams/pdf-0095-naturality-square.png)

其中水平箭头是伴随关系给出的双射。对于 $f:A\to G(B)$，有

![自然性方块中元素的像](/library/volume-87/diagrams/pdf-0095-elements-square.png)

因此，我们必须证明 $q\circ\bar{f}=\overline{G(q)\circ f}$。在伴随关系定义中的自然性条件 (2.2) 里取 $g=\bar{f}$，就立即得到这个等式。$\square$<span class="original-page-anchor" id="pdf-page-96" aria-hidden="true"></span>随便选一个取值于 $\mathbf{Set}$ 的函子，我们通常不会期待它是可表的。在某种意义上，可表函子相当少。不过，遗忘函子往往确实是可表的：

**命题 4.1.11** 任何具有左伴随的集合值函子都是可表函子。

**证明** 设 $G:\mathscr{A}\to\mathbf{Set}$ 是具有左伴随 $F$ 的函子。用 $1$ 表示单点集合。由例 4.1.4，

$$
G(A)\cong\mathbf{Set}(1,G(A)),
$$

并且这个同构对 $A\in\mathscr{A}$ 是自然的，也就是说，$G\cong\mathbf{Set}(1,G(-))$。所以由引理 4.1.10，$G$ 是可表函子；事实上，$G\cong H^{F(1)}$。$\square$

**例 4.1.12** 上面提到的几个可表函子例子，都可以按命题 4.1.11 的方式得到。例如，$U:\mathbf{Top}\to\mathbf{Set}$ 有一个左伴随 $D$（例 2.1.5），而 $D(1)\cong1$，于是我们再次得到 $U\cong H^1$。类似地，练习 3.2.16 要求你为对象函子 $\operatorname{ob}:\mathbf{Cat}\to\mathbf{Set}$ 构造一个左伴随 $D$。这个函子 $D$ 满足 $D(1)\cong\mathbf{1}$，从而再次证明 $\operatorname{ob}\cong H^{\mathbf{1}}$。

**例 4.1.13** 遗忘函子 $U:\mathbf{Vect}_k\to\mathbf{Set}$ 是可表函子，因为它有左伴随。事实上，如果用 $F$ 表示这个左伴随，那么 $F(1)$ 就是一维向量空间 $k$，所以 $U\cong H^k$。这也很容易直接看出：从 $k$ 到向量空间 $V$ 的一个态射，由 $1$ 的像唯一确定，而这个像可以是 $V$ 的任意元素；因此 $\mathbf{Vect}_k(k,V)\cong U(V)$，且这个同构对 $V$ 是自然的。

**例 4.1.14** 例 2.1.3 一开始就指出，代数结构范畴之间的遗忘函子通常有左伴随。考虑交换环范畴 $\mathbf{CRing}$ 以及遗忘函子 $U:\mathbf{CRing}\to\mathbf{Set}$。根据这一一般原则，我们预期 $U$ 有左伴随，而命题 4.1.11 随即告诉我们，$U$ 是可表函子。

我们来具体看看这是如何实现的。给定集合 $S$，令 $\mathbb{Z}[S]$ 为以 $\mathbb{Z}$ 为系数、以彼此可交换的 $x_s$（$s\in S$）为变量的多项式环。（在例 1.2.4(b) 中，它被称为 $F(S)$。）那么 $S\mapsto\mathbb{Z}[S]$ 定义了一个函子 $\mathbf{Set}\to\mathbf{CRing}$，它是 $U$ 的左伴随。因此 $U\cong H^{\mathbb{Z}[x]}$。同样，这也可以直接验证：对任意环 $R$，态射 $\mathbb{Z}[x]\to R$ 与 $R$ 的元素一一对应（练习 0.13 和 4.1.29）。

我们已经为范畴 $\mathscr{A}$ 的每个对象 $A$ 定义了一个函子 $H^A\in[\mathscr{A},\mathbf{Set}]$。它描述了 $A$ 如何观察这个世界。随着 $A$ 的改变，视野也会改变。另一方面，被观察的始终是同一个世界，所以不同对象所看到的不同景象之间总有某种联系。（可以想想从飞行中的飞机拍摄的航拍照片：它们的重叠部分足够吻合，因而能够<span class="original-page-anchor" id="pdf-page-97" aria-hidden="true"></span>拼接成一张大图。）所以，“视野”这一族 $(H^A)_{A\in\mathscr{A}}$ 具有某种一致性。这意味着，只要对象 $A$ 与 $A'$ 之间有一个态射，$H^A$ 与 $H^{A'}$ 之间也就有一个态射。

确切地说，一个态射 $A'\xrightarrow{f}A$ 诱导一个自然变换

![可表函子之间的自然变换](/library/volume-87/diagrams/pdf-0097-natural-transformation.png)

其 $B$-分量（$B\in\mathscr{A}$）是函数

$$
\begin{array}{rcl}
H^A(B)=\mathscr{A}(A,B)&\longrightarrow&H^{A'}(B)=\mathscr{A}(A',B)\\
p&\longmapsto&p\circ f.
\end{array}
$$

同样，$H^f$ 还有多种其他名称：$\mathscr{A}(f,-)$、$f^*$ 和 $-\circ f$。

注意方向反转了！每个函子 $H^A$ 都是协变的，但把它们放在一起，就构成一个*反变*函子，如下面的定义所述。

**定义 4.1.15** 设 $\mathscr{A}$ 为局部小范畴。函子

$$
H^\bullet:\mathscr{A}^{\mathrm{op}}\to[\mathscr{A},\mathbf{Set}]
$$

在对象 $A$ 上定义为 $H^\bullet(A)=H^A$，在态射 $f$ 上定义为 $H^\bullet(f)=H^f$。

符号 $\bullet$ 和 $-$ 一样，也是表示空位的一种方式。

本章到目前为止给出的所有定义都可以对偶化。在形式层面上，这很简单：把所有箭头反向，于是每个 $\mathscr{A}$ 都变成 $\mathscr{A}^{\mathrm{op}}$，反之亦然。但在我们通常的例子中，二者的意味不同。我们不再问对象*看见*什么，而是问它们如何*被看见*。

先将定义 4.1.1 对偶化。

**定义 4.1.16** 设 $\mathscr{A}$ 为局部小范畴，$A\in\mathscr{A}$。我们如下定义函子

$$
H_A=\mathscr{A}(-,A):\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}:
$$

- 对对象 $B\in\mathscr{A}$，令 $H_A(B)=\mathscr{A}(B,A)$；
- 对 $\mathscr{A}$ 中的态射 $B'\xrightarrow{g}B$，定义

  $$
  H_A(g)=\mathscr{A}(g,A)=g^*=-\circ g:\mathscr{A}(B,A)\to\mathscr{A}(B',A)
  $$

  其作用为

  $$
  p\mapsto p\circ g,
  $$

  其中 $p:B\to A$ 任意。

<span class="original-page-anchor" id="pdf-page-98" aria-hidden="true"></span>

如果你了解对偶向量空间，这个构造会显得很熟悉。尤其是，一个态射 $B' \to B$ 会诱导出方向相反的态射 $H_A(B) \to H_A(B')$，你对此不会感到意外。

现在我们为*反变*的集合值函子定义可表性。严格说来，这并无必要，因为 $\mathscr{A}$ 上的反变函子就是 $\mathscr{A}^{\mathrm{op}}$ 上的协变函子，而我们已经知道协变的集合值函子可表是什么意思。不过，直接给出一个定义仍然很有用。

**定义 4.1.17** 设 $\mathscr{A}$ 是局部小范畴。如果存在某个 $A \in \mathscr{A}$ 使得 $X \cong H_A$，则称函子 $X\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$ **可表**。$X$ 的一个**表示**，是选定一个对象 $A \in \mathscr{A}$，以及 $H_A$ 与 $X$ 之间的一个同构。

**例 4.1.18** 有一个函子

$$
\mathscr{P}\colon \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}
$$

把每个集合 $B$ 送到其幂集 $\mathscr{P}(B)$；对态射 $g\colon B' \to B$，它由 $(\mathscr{P}(g))(U) = g^{-1}U$ 定义，其中 $U \in \mathscr{P}(B)$。（这里，$g^{-1}U$ 表示 $U$ 在 $g$ 下的逆像或原像，其定义为 $g^{-1}U = \{x' \in B' \mid g(x') \in U\}$。）我们在第 3.1 节看到，一个子集相当于一个到二点集合 $2$ 的态射。确切地说，$\mathscr{P} \cong H_2$。

**例 4.1.19** 类似地，有一个函子

$$
\mathscr{O}\colon \mathbf{Top}^{\mathrm{op}} \to \mathbf{Set}
$$

其在对象 $B$ 上的定义是：令 $\mathscr{O}(B)$ 为 $B$ 的所有开子集组成的集合。若 $S$ 表示二点拓扑空间，其中两个单点子集恰有一个是开的，那么从空间 $B$ 到 $S$ 的连续映射与 $B$ 的开子集自然地对应（习题 4.1.30）。因此 $\mathscr{O} \cong H_S$，所以 $\mathscr{O}$ 可表。

**例 4.1.20** 在例 1.2.11 中，我们定义了函子 $C\colon \mathbf{Top}^{\mathrm{op}} \to \mathbf{Ring}$，把每个空间送到其上的连续实值函数组成的环。复合函子

$$
\mathbf{Top}^{\mathrm{op}} \xrightarrow{C} \mathbf{Ring} \xrightarrow{U} \mathbf{Set}
$$

是可表的，因为根据定义，对拓扑空间 $X$，有 $U(C(X)) = \mathbf{Top}(X, \mathbb{R})$。

此前，我们把协变的可表函子族 $(H^A)_{A \in \mathscr{A}}$ 汇集成一个大函子 $H^\bullet$。现在，我们对反变的可表函子族 $(H_A)_{A \in \mathscr{A}}$ 做同样的事。

<span class="original-page-anchor" id="pdf-page-99" aria-hidden="true"></span>

$\mathscr{A}$ 中的任意态射 $A \xrightarrow{f} A'$ 都诱导出一个自然变换

![从 H_A 到 H_A′ 的自然变换](/library/volume-87/diagrams/pdf-0099-natural-transformation.png)

（也称为 $\mathscr{A}(-,f)$、$f_*$ 或 $f \circ -$），其在对象 $B \in \mathscr{A}$ 处的分量是

$$
\begin{array}{ccc}
H_A(B) = \mathscr{A}(B,A) & \to & H_{A'}(B) = \mathscr{A}(B,A') \\
p & \mapsto & f \circ p.
\end{array}
$$

**定义 4.1.21** 设 $\mathscr{A}$ 是局部小范畴。$\mathscr{A}$ 的**米田嵌入**是函子

$$
H_\bullet\colon \mathscr{A} \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]
$$

它在对象 $A$ 上由 $H_\bullet(A) = H_A$ 定义，在态射 $f$ 上由 $H_\bullet(f) = H_f$ 定义。

下面汇总至今给出的定义。

对每个 $A \in \mathscr{A}$，我们有一个函子 $\mathscr{A} \xrightarrow{H^A} \mathbf{Set}$。把它们全部汇集起来，得到函子 $\mathscr{A}^{\mathrm{op}} \xrightarrow{H^\bullet} [\mathscr{A},\mathbf{Set}]$。

对每个 $A \in \mathscr{A}$，我们有一个函子 $\mathscr{A}^{\mathrm{op}} \xrightarrow{H_A} \mathbf{Set}$。把它们全部汇集起来，得到函子 $\mathscr{A} \xrightarrow{H_\bullet} [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$。

第二对函子是第一对的对偶。两者都涉及反变性；这是无法避免的。

在可表函子的理论中，采用第一对还是第二对，差别不大。我们对其中一对证明的任何定理，都可以通过对偶化得到关于另一对的定理。我们选择采用第二对，即各个 $H_A$ 和 $H_\bullet$。在稍后解释的意义下，$H_\bullet$ 把 $\mathscr{A}$“嵌入”$[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$。这可能很有用，因为范畴 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 有一些 $\mathscr{A}$ 未必具有的良好性质。

习题 4.1.27 要求你证明，$H_\bullet$ 在对象的同构类上是单射。强烈建议你在继续阅读之前完成它，因为它概括了本章余下部分的关键思想。

还有一个函子需要定义。它把上面所示的第一对和第二对函子统一起来。

**定义 4.1.22** 设 $\mathscr{A}$ 是局部小范畴。函子

$$
\operatorname{Hom}_{\mathscr{A}}\colon \mathscr{A}^{\mathrm{op}} \times \mathscr{A} \to \mathbf{Set}
$$

<span class="original-page-anchor" id="pdf-page-100" aria-hidden="true"></span>

由下式定义：

![Hom 函子在对象和态射上的作用](/library/volume-87/diagrams/pdf-0100-hom-functor-action.png)

换言之，$\operatorname{Hom}_{\mathscr{A}}(A,B) = \mathscr{A}(A,B)$，并且只要有 $A' \xrightarrow{f} A \xrightarrow{p} B \xrightarrow{g} B'$，就有 $(\operatorname{Hom}_{\mathscr{A}}(f,g))(p) = g \circ p \circ f$。

**注 4.1.23** (a) 函子 $\operatorname{Hom}_{\mathscr{A}}$ 的存在，有点类似于下面这个事实：对于度量空间 $(X,d)$，度量本身就是连续映射 $d\colon X \times X \to \mathbb{R}$。（若取两个点，并把每个点稍稍移动一点，它们之间的距离也只会稍稍改变一点。）

(b) 用习题 1.2.25 的说法，$\operatorname{Hom}_{\mathscr{A}}$ 是与函子族 $(H^A)_{A \in \mathscr{A}}$ 和 $(H_B)_{B \in \mathscr{A}}$ 相对应的函子 $\mathscr{A}^{\mathrm{op}} \times \mathscr{A} \to \mathbf{Set}$。

(c) 在例 2.1.6 中，我们看到，对任意集合 $B$，存在函子 $\mathbf{Set} \to \mathbf{Set}$ 的伴随关系 $(- \times B) \dashv (-)^B$。类似地，对任意范畴 $\mathscr{B}$，存在函子 $\mathbf{CAT} \to \mathbf{CAT}$ 的伴随关系 $(- \times \mathscr{B}) \dashv [\mathscr{B},-]$；换言之，对于 $\mathscr{A},\mathscr{B},\mathscr{C} \in \mathbf{CAT}$，存在典范双射

$$
\mathbf{CAT}(\mathscr{A} \times \mathscr{B},\mathscr{C}) \cong \mathbf{CAT}(\mathscr{A},[\mathscr{B},\mathscr{C}]).
$$

在这个双射下，函子

$$
\operatorname{Hom}_{\mathscr{A}}\colon \mathscr{A}^{\mathrm{op}} \times \mathscr{A} \to \mathbf{Set},\qquad H^\bullet\colon \mathscr{A}^{\mathrm{op}} \to [\mathscr{A},\mathbf{Set}]
$$

彼此对应。因此，$\operatorname{Hom}_{\mathscr{A}}$ 携带了与 $H^\bullet$（或 $H_\bullet$）相同的信息，只是呈现方式略有不同。

**注 4.1.24** 现在我们可以解释伴随关系定义（定义 2.1.1）中的自然性。取范畴和函子

![A 与 B 之间的函子 F 和 G](/library/volume-87/diagrams/pdf-0100-functors-fg.png)

它们给出函子

![伴随关系自然性的函子方图](/library/volume-87/diagrams/pdf-0100-adjunction-naturality.png)

沿先下后右路径 $\downarrow\!\rightarrow$ 的复合函子把 $(A,B)$ 送到 $\mathscr{B}(F(A),B)$；它可以写成 $\mathscr{B}(F(-),-)$。沿先右后下路径 $\rightarrow\!\downarrow$ 的复合函子把 $(A,B)$ 送到 $\mathscr{A}(A,G(B))$。习题 4.1.32 要求你证明，这两个函子

$$
\mathscr{B}(F(-),-),\ \mathscr{A}(-,G(-))\colon \mathscr{A}^{\mathrm{op}} \times \mathscr{B} \to \mathbf{Set}
$$

<span class="original-page-anchor" id="pdf-page-101" aria-hidden="true"></span>

自然同构，当且仅当 $F$ 和 $G$ 互为伴随。这就说明了注 2.1.2(a) 中的断言：伴随关系定义中的自然性要求 (2.2) 和 (2.3)，只是断言两个特定函子自然同构。

任意范畴中的对象，并没有显而易见的元素概念。不过，*集合*当然具有元素，而且我们已经看到，集合 $A$ 的一个元素，与态射 $1 \to A$ 是同一回事。由此，我们给出下面的定义。

**定义 4.1.25** 设 $A$ 是某个范畴的对象。$A$ 的一个**广义元素**是以 $A$ 为余域的态射。态射 $S \to A$ 是 $A$ 的一个**形状为 $S$** 的广义元素。

“广义元素”无非就是“态射”的同义词，但有时，把态射看作广义元素会很有用。

例如，当 $A$ 是集合时，$A$ 的形状为 $1$ 的广义元素就是 $A$ 的普通元素，而 $A$ 的形状为 $\mathbb{N}$ 的广义元素就是 $A$ 中的一个序列。在拓扑空间范畴中，形状为 $1$（单点空间）的广义元素就是点；根据定义，形状为 $S^1$（圆周）的广义元素就是环路。由此可见，在几何对象的范畴中，我们也完全可以说“形状为 $S$ 的图形”。

在代数中，我们往往关心 $x^2+y^2=1$ 这样的方程的解。起初，也许我们特别关心 $\mathbb{Q}$ 中的解，但随后意识到，为了研究有理数解，先研究其他环中的解会有帮助。（这常常是一个富有成效的策略。）给定一个环 $A$，满足 $a^2+b^2=1$ 的有序对 $(a,b) \in A \times A$，相当于一个环同态

$$
\mathbb{Z}[x,y]/(x^2+y^2-1) \to A.
$$

因此，我们的方程在任意环中的解，都可以看作形状为 $\mathbb{Z}[x,y]/(x^2+y^2-1)$ 的广义元素。

对于范畴 $\mathscr{A}$ 的对象 $S$，函子

$$
H^S\colon \mathscr{A} \to \mathbf{Set}
$$

把一个对象送到其形状为 $S$ 的广义元素组成的集合。函子性告诉我们，$\mathscr{A}$ 中的任意态射 $A \to B$ 都把 $A$ 的 $S$-元素变成 $B$ 的 $S$-元素。例如，取 $\mathscr{A} = \mathbf{Top}$、$S = S^1$，则任意连续映射 $A \to B$ 都把 $A$ 中的环路变成 $B$ 中的环路。

### 习题

**4.1.26** 找出三个上面没有提到过的可表函子的例子。

<span class="original-page-anchor" id="pdf-page-102" aria-hidden="true"></span>

**4.1.27** 设 $\mathscr{A}$ 是局部小范畴，且 $A,A' \in \mathscr{A}$ 满足 $H_A \cong H_{A'}$。直接证明 $A \cong A'$。

**4.1.28** 设 $p$ 是素数。证明例 4.1.5 中定义的函子 $U_p\colon \mathbf{Grp} \to \mathbf{Set}$ 同构于 $\mathbf{Grp}(\mathbb{Z}/p\mathbb{Z},-)$。（要检验存在函子之间的同构——也就是自然同构——你首先需要定义 $U_p$ 在态射上的作用。这样做只有一种合理的方式。）

**4.1.29** 利用习题 0.13(a) 的结果，证明遗忘函子 $\mathbf{CRing} \to \mathbf{Set}$ 同构于 $\mathbf{CRing}(\mathbb{Z}[x],-)$，如例 4.1.14 所述。

**4.1.30** **谢尔宾斯基空间**是二点拓扑空间 $S$，其中两个单点子集一个是开的，另一个不是。证明：对任意拓扑空间 $X$，$X$ 的开子集与连续映射 $X \to S$ 之间存在一个典范双射。利用这一点证明例 4.1.19 中的函子 $\mathscr{O}\colon \mathbf{Top}^{\mathrm{op}} \to \mathbf{Set}$ 由 $S$ 表示。

**4.1.31** 设 $M\colon \mathbf{Cat} \to \mathbf{Set}$ 是把小范畴 $\mathscr{A}$ 送到 $\mathscr{A}$ 中所有态射组成的集合的函子。证明 $M$ 可表。

**4.1.32** 取局部小范畴 $\mathscr{A}$ 和 $\mathscr{B}$，以及函子

![函子 F 和 G](/library/volume-87/diagrams/pdf-0102-functors-fg.png)

证明：$F$ 是 $G$ 的左伴随，当且仅当注 4.1.24 中的两个函子

$$
\mathscr{B}(F(-),-),\ \mathscr{A}(-,G(-))\colon \mathscr{A}^{\mathrm{op}} \times \mathscr{B} \to \mathbf{Set}
$$

自然同构。（提示：利用习题 1.3.29 或习题 2.1.14，都可以使证明更容易。）

## 4.2 米田引理

可表函子看到了什么？

回忆定义 1.2.15，函子 $\mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$ 有时称为 $\mathscr{A}$ 上的“预层”。因此，对每个 $A \in \mathscr{A}$，我们有一个可表预层 $H_A$，而我们所问的是：从 $H_A$ 的视角看，预层范畴 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 的其余部分是什么样的？换言之，若 $X$ 是另一个预层，那么态射 $H_A \to X$ 是什么？

初学范畴论的人，常常在本节所讲的内容上第一次遇到困难。通常，困难的核心在于理解刚才提出的问题。让我们再问一遍。

首先固定一个局部小范畴 $\mathscr{A}$。然后取一个对象 $A \in \mathscr{A}$ 和一个函子 $X\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$。对象 $A$ 给出另一个函子<span class="original-page-anchor" id="pdf-page-103" aria-hidden="true"></span>$H_A = \mathscr{A}(-,A)\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$。问题是：态射 $H_A \to X$ 是什么？因为 $H_A$ 和 $X$ 都是预层范畴 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 的对象，所以这里的“态射”是 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 中的态射。因此，我们在问有哪些自然变换

![从 H_A 到 X 的自然变换](/library/volume-87/diagrams/pdf-0103-yoneda-question.png)

(4.1)

存在。这样的自然变换组成的集合记作

$$
[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X).
$$

（这是记号 $\mathscr{B}(B,B')$ 的一个特例；该记号表示范畴 $\mathscr{B}$ 中态射 $B \to B'$ 组成的集合。这里，$\mathscr{B} = [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$，$B = H_A$，$B' = X$。）我们想知道这个集合是什么。

范畴论的一般理论中有一条非正式原则，可以让我们猜到答案。回顾关于范畴、函子和自然变换定义的注 1.1.2(b)、1.2.2(a) 和 1.3.2(a)。每条注都具有这样的形式：“由某一类型的输入，恰好能够构造出另一类型的一个输出。”例如，在注 1.1.2(b) 中，输入是态射序列 $A_0 \xrightarrow{f_1} \cdots \xrightarrow{f_n} A_n$，输出是一个态射 $A_0 \to A_n$，而其断言是：无论我们怎样处理输入数据 $f_1,\ldots,f_n$，能够构造出的态射 $A_0 \to A_n$ 都只有一个。

把这条原则用于我们的问题。刚才我们看到，给定对象 $A \in \mathscr{A}$ 和 $\mathscr{A}$ 上的预层 $X$ 作为输入，就能构造出一个集合，即 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X)$。由同样的输入数据 $(A,X)$，还有其他构造集合的方法吗？有：只需取集合 $X(A)$！这条非正式原则提示，这两个集合是相同的：

$$
[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X) \cong X(A) \tag{4.2}
$$

对所有 $A \in \mathscr{A}$ 和 $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 都成立。这确实是真的；这就是米田引理。

因此，非正式地说，米田引理断言：对于任意 $A \in \mathscr{A}$ 和 $\mathscr{A}$ 上的预层 $X$，

> *自然变换 $H_A \to X$ 就是 $X(A)$ 的一个元素。*

下面是正式陈述。证明稍后给出。

**定理 4.2.1（米田）** 设 $\mathscr{A}$ 是局部小范畴。则

$$
[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X) \cong X(A) \tag{4.3}
$$

关于 $A \in \mathscr{A}$ 和 $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 都是自然的。

<span class="original-page-anchor" id="pdf-page-104" aria-hidden="true"></span>

这与 (4.2) 所陈述的完全相同，只是多了“自然地”这个词。回忆定义 1.3.12，对函子 $F,G\colon \mathscr{C} \to \mathscr{D}$，短语“$F(C) \cong G(C)$ 关于 $C$ 是自然的”，意味着存在自然同构 $F \cong G$。所以，在米田引理中使用这个短语，表明 (4.3) 的两边对于 $A$ 和 $X$ 都具有函子性。例如，这意味着态射 $X \to X'$ 必须诱导出态射

$$
[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X) \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X'),
$$

而且，同构 (4.3) 不仅对*每个* $A$ 和 $X$ 都成立，还可以选择这些同构，使它们与这些诱导态射相容。确切地说，米田引理断言，复合函子

![米田引理中的复合函子](/library/volume-87/diagrams/pdf-0104-yoneda-composite-functor.png)

自然同构于求值函子

$$
\begin{array}{ccc}
\mathscr{A}^{\mathrm{op}} \times [\mathscr{A}^{\mathrm{op}},\mathbf{Set}] & \to & \mathbf{Set} \\
(A,X) & \mapsto & X(A).
\end{array}
$$

如果米田引理是假的，世界看起来就会复杂得多。因为，取一个预层 $X\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$，并由

$$
X' = [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_\bullet,X)\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}
$$

定义一个新预层 $X'$，也就是说，对所有 $A \in \mathscr{A}$，令 $X'(A) = [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X)$。米田引理告诉我们，$X'(A) \cong X(A)$ 关于 $A$ 是自然的；换言之，$X' \cong X$。如果米田引理是假的，那么从单个预层 $X$ 出发，我们就可以构造出新预层的无限序列 $X,X',X'',\ldots$，它们可能全都不同。但实际上，情形十分简单：它们全都相同。

米田引理的证明是迄今为止最长的证明。不过，在每个阶段，基本上都只有一种进行下去的方式。如果你觉得自己属于那些在米田引理处首次遇到严峻挑战的范畴论初学者，那么在阅读证明之前自己把它推导出来，会是一个极好的练习。这不需要任何巧思，只需要理解陈述中的所有术语。

**米田引理的证明** 我们必须对每个 $A$ 和 $X$，定义集合 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X)$ 与 $X(A)$ 之间的双射。然后，还必须证明我们的双射关于 $A$ 和 $X$ 是自然的。

<span class="original-page-anchor" id="pdf-page-105" aria-hidden="true"></span>

首先，固定 $A \in \mathscr{A}$ 和 $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$。我们定义函数

![米田双射中的两个函数](/library/volume-87/diagrams/pdf-0105-yoneda-inverse-functions.png)

(4.4)

并证明它们互为逆函数。因此，我们必须做四件事：定义函数 $\hat{(\ )}$，定义函数 $\tilde{(\ )}$，证明 $\widehat{\tilde{(\ )}}$ 是恒等映射，以及证明 $\widetilde{\hat{(\ )}}$ 是恒等映射。

- 给定 $\alpha\colon H_A \to X$，由 $\hat{\alpha} = \alpha_A(1_A)$ 定义 $\hat{\alpha} \in X(A)$。（我们还能怎样定义它呢？）

- 设 $x \in X(A)$。我们必须定义一个自然变换 $\tilde{x}\colon H_A \to X$。也就是说，我们必须对每个 $B \in \mathscr{A}$ 定义函数

$$
\tilde{x}_B\colon H_A(B) = \mathscr{A}(B,A) \to X(B)
$$

并证明分量族 $\tilde{x} = (\tilde{x}_B)_{B \in \mathscr{A}}$ 满足自然性。

给定 $B \in \mathscr{A}$ 和 $f \in \mathscr{A}(B,A)$，定义

$$
\tilde{x}_B(f) = (X(f))(x) \in X(B).
$$

（我们还能怎样定义它呢？）这是有意义的，因为 $X(f)$ 是态射 $X(A) \to X(B)$。为了证明自然性，我们必须证明：对 $\mathscr{A}$ 中的任意态射 $B' \xrightarrow{g} B$，方图

![x̃ 的自然性方图](/library/volume-87/diagrams/pdf-0105-yoneda-naturality-square.png)

交换。为了减少符号的繁杂，我们把 $X(g)$ 写作 $Xg$，依此类推。现在，对所有 $f \in \mathscr{A}(B,A)$，有

![相应的元素计算](/library/volume-87/diagrams/pdf-0105-yoneda-naturality-elements.png)

而由函子性，$X(f \circ g) = (Xg) \circ (Xf)$，所以这个方图确实交换。

- 给定 $x \in X(A)$，我们必须证明 $\widehat{\tilde{x}} = x$；事实上，

$$
\widehat{\tilde{x}} = \tilde{x}_A(1_A) = (X1_A)(x) = 1_{X(A)}(x) = x.
$$

<span class="original-page-anchor" id="pdf-page-106" aria-hidden="true"></span>

- 给定 $\alpha\colon H_A \to X$，我们必须证明 $\widetilde{\hat{\alpha}} = \alpha$。两个自然变换相等，当且仅当它们的所有分量都相等；因此，我们必须对所有 $B \in \mathscr{A}$ 证明 $\bigl(\widetilde{\hat{\alpha}}\bigr)_B = \alpha_B$。这个等式的两边都是从 $H_A(B) = \mathscr{A}(B,A)$ 到 $X(B)$ 的函数，而两个函数相等，当且仅当它们在定义域的每个元素处都取相同的值。所以，我们必须证明

$$
\bigl(\widetilde{\hat{\alpha}}\bigr)_B(f) = \alpha_B(f)
$$

对所有 $B \in \mathscr{A}$ 和 $\mathscr{A}$ 中的态射 $f\colon B \to A$ 成立。由定义，左边为

$$
\bigl(\widetilde{\hat{\alpha}}\bigr)_B(f) = (Xf)(\hat{\alpha}) = (Xf)(\alpha_A(1_A)),
$$

所以只剩下证明

$$
(Xf)(\alpha_A(1_A)) = \alpha_B(f). \tag{4.5}
$$

由 $\alpha$ 的自然性（这是我们手头唯一的工具），方图

![用于恢复 α 的自然性方图](/library/volume-87/diagrams/pdf-0106-recover-transformation.png)

交换。在这个交换图中代入 $1_A \in \mathscr{A}(A,A)$，就得到等式 (4.5)。

（证明尚未结束，不过此时停下来思考 $\widetilde{\hat{\alpha}} = \alpha$ 这一事实的意义很有帮助。因为 $\hat{\alpha}$ 是 $\alpha$ 在 $1_A$ 上的值，所以这意味着：

> *一个自然变换 $H_A \to X$ 由它在 $1_A$ 上的值决定。*

至于自然变换 $H_A \to X$ 究竟*怎样*由它在 $1_A$ 上的值决定，等式 (4.5) 已经作出了描述。）

这就对每个 $A \in \mathscr{A}$ 和 $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 建立了双射 (4.4)。现在我们证明，这个双射关于 $A$ 和 $X$ 是自然的。

我们使用两个略省力的方法。首先，原则上需要证明 $\hat{(\ )}$ 和 $\tilde{(\ )}$ 都具有自然性，但根据引理 1.3.11，只需证明其中一个具有自然性即可。我们证明 $\hat{(\ )}$ 的自然性。其次，根据习题 1.3.29，$\hat{(\ )}$ 关于有序对 $(A,X)$ 是自然的，当且仅当对每个固定的 $X$，它关于 $A$ 是自然的，并且对每个固定的 $A$，它关于 $X$ 是自然的。因此，只需分别检查这两种自然性。

关于 $A$ 的自然性断言：对于每个 $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 和 $\mathscr{A}$ 中的态射 $B \xrightarrow{f} A$，<span class="original-page-anchor" id="pdf-page-107" aria-hidden="true"></span>方图

![关于 A 的自然性](/library/volume-87/diagrams/pdf-0107-naturality-in-a-square.png)

交换。对于 $\alpha\colon H_A \to X$，有

![关于 A 的自然性的元素计算](/library/volume-87/diagrams/pdf-0107-naturality-in-a-elements.png)

所以必须证明 $(\alpha \circ H_f)_B(1_B) = (Xf)(\alpha_A(1_A))$。事实上，

$$
\begin{aligned}
(\alpha \circ H_f)_B(1_B) &= \alpha_B((H_f)_B(1_B)) \\
&= \alpha_B(f \circ 1_B) = \alpha_B(f) \\
&= (Xf)(\alpha_A(1_A)),
\end{aligned}
$$

其中，第一步使用 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 中复合的定义，第二步使用 $H_f$ 的定义，最后一步使用等式 (4.5)。

关于 $X$ 的自然性断言：对于每个 $A \in \mathscr{A}$ 以及 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 中的态射

![自然变换 θ](/library/volume-87/diagrams/pdf-0107-theta-transformation.png)

方图

![关于 X 的自然性](/library/volume-87/diagrams/pdf-0107-naturality-in-x-square.png)

交换。对于 $\alpha\colon H_A \to X$，有

![关于 X 的自然性的元素计算](/library/volume-87/diagrams/pdf-0107-naturality-in-x-elements.png)

而根据 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 中复合的定义，$(\theta \circ \alpha)_A = \theta_A \circ \alpha_A$，所以这个方图确实交换。证明至此完成。$\square$

<span class="original-page-anchor" id="pdf-page-108" aria-hidden="true"></span>

### 习题

**4.2.2** 陈述米田引理的对偶。

**4.2.3** 理解米田引理的一种方式，是考察一些特殊情形。这里我们考虑单对象范畴。

设 $M$ 是幺半群。可以通过乘法在 $M$ 的底集合上赋予一个右 $M$-作用：对所有 $x,m \in M$，令 $x \cdot m = xm$。这个 $M$-集合称为 $M$ 的**右正则表示**。我们把它记作 $\underline{M}$。

(a) 把 $M$ 看作单对象范畴时，函子 $M^{\mathrm{op}} \to \mathbf{Set}$ 对应于右 $M$-集合（例 1.2.14）。证明：唯一的可表函子 $M^{\mathrm{op}} \to \mathbf{Set}$ 所对应的 $M$-集合，就是右正则表示。

(b) 现在设 $X$ 是任意右 $M$-集合。证明：对每个 $x \in X$，存在唯一的右 $M$-集合态射 $\alpha\colon \underline{M} \to X$，使得 $\alpha(1) = x$。由此推出，$\{\underline{M} \to X\text{ 的右 }M\text{-集合态射}\}$ 与 $X$ 之间存在双射。

(c) 由此推出单对象范畴的米田引理。

## 4.3 米田引理的推论

米田引理在范畴论中具有根本地位。这里我们考察它的三个重要推论。

**记号 4.3.1** 标有 $\sim$ 的箭头，例如 $A \xrightarrow{\sim} B$，表示同构。

### 一个表示就是一个泛元素

**推论 4.3.2** 设 $\mathscr{A}$ 是局部小范畴，$X\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$。那么，$X$ 的一个表示由对象 $A \in \mathscr{A}$ 和元素 $u \in X(A)$ 组成，并满足：

> 对每个 $B \in \mathscr{A}$ 和 $x \in X(B)$，存在唯一的态射 $\bar{x}\colon B \to A$，使得 $(X\bar{x})(u) = x$。 (4.6)

为了说明这条陈述，先回忆定义：$X$ 的一个表示是对象 $A \in \mathscr{A}$，连同自然同构 $\alpha\colon H_A \xrightarrow{\sim} X$。推论 4.3.2 断言，这样的有序对 $(A,\alpha)$ 与满足条件 (4.6) 的有序对 $(A,u)$ 之间存在自然双射。

满足 $B \in \mathscr{A}$ 和 $x \in X(B)$ 的有序对 $(B,x)$，有时称为预层 $X$ 的**元素**。（事实上，米田引理告诉我们，$x$ 相当于 $X$ 的一个形状为 $H_B$ 的广义元素。）满足条件 (4.6) 的元素 $u$<span class="original-page-anchor" id="pdf-page-109" aria-hidden="true"></span>有时称为 $X$ 的**泛**元素。因此，推论 4.3.2 说，预层 $X$ 的一个表示相当于 $X$ 的一个泛元素。

**证明** 由米田引理，我们只需证明：对于 $A \in \mathscr{A}$ 和 $u \in X(A)$，自然变换 $\tilde{u}\colon H_A \to X$ 是同构，当且仅当 (4.6) 成立。（这里使用的是米田引理证明中引入的记号。）现在，$\tilde{u}$ 是同构，当且仅当对所有 $B \in \mathscr{A}$，函数

$$
\tilde{u}_B\colon H_A(B) = \mathscr{A}(B,A) \to X(B)
$$

都是双射；而这又等价于：对所有 $B \in \mathscr{A}$ 和 $x \in X(B)$，存在唯一的 $\bar{x} \in \mathscr{A}(B,A)$，使得 $\tilde{u}_B(\bar{x}) = x$。由于 $\tilde{u}_B(\bar{x}) = (X\bar{x})(u)$，这恰好就是条件 (4.6)。$\square$

以下例子使用它关于协变集合值函子的对偶形式：

**推论 4.3.3** 设 $\mathscr{A}$ 是局部小范畴，$X\colon \mathscr{A} \to \mathbf{Set}$。那么，$X$ 的一个表示由对象 $A \in \mathscr{A}$ 和元素 $u \in X(A)$ 组成，并满足：

> 对每个 $B \in \mathscr{A}$ 和 $x \in X(B)$，存在唯一的态射 $\bar{x}\colon A \to B$，使得 $(X\bar{x})(u) = x$。 (4.7)

**证明** 由对偶性立即得到。$\square$

**例 4.3.4** 固定一个集合 $S$，并考虑函子

$$
\begin{array}{cccc}
X = \mathbf{Set}(S,U(-))\colon & \mathbf{Vect}_k & \to & \mathbf{Set} \\
& V & \mapsto & \mathbf{Set}(S,U(V)).
\end{array}
$$

关于 $X$，有下面两个熟悉的（而且是真的！）陈述：

(a) 存在向量空间 $F(S)$ 和同构

$$
\mathbf{Vect}_k(F(S),V) \cong \mathbf{Set}(S,U(V)) \tag{4.8}
$$

并且这个同构关于 $V \in \mathbf{Vect}_k$ 是自然的（例 2.1.3(a)）；

(b) 存在向量空间 $F(S)$ 和函数 $u\colon S \to U(F(S))$，使得：

> 对每个向量空间 $V$ 和函数 $f\colon S \to U(V)$，存在唯一的线性映射 $\bar{f}\colon F(S) \to V$，使得下图

![自由向量空间的泛性质](/library/volume-87/diagrams/pdf-0109-free-vector-space-universal.png)

> 交换

<span class="original-page-anchor" id="pdf-page-110" aria-hidden="true"></span>

（如第 2.3 节的引言所述，在那里，$u$ 用其通常的记号 $\eta_S$ 表示）。

这两个陈述都在说 $X$ 可表。陈述 (a) 说，存在同构 $X(V) \cong \mathbf{Vect}(F(S),V)$，且关于 $V$ 是自然的，也就是说，存在同构 $X \cong H^{F(S)}$。因此，由可表性的定义，$X$ 可表。陈述 (b) 说，$u \in X(F(S))$ 满足条件 (4.7)。因此，由推论 4.3.3，$X$ 可表。

你会注意到，说明 $X$ 可表的第一种说法，比第二种简短得多。确实，显然如果 (b) 所述的情形成立，就存在同构

$$
\mathbf{Vect}_k(F(S),V) \xrightarrow{\sim} \mathbf{Set}(S,U(V))
$$

它关于 $V$ 是自然的，且由 $g \mapsto U(g) \circ u$ 定义。但乍看之下，(b) 似乎比 (a) 说得更多，因为它断言两个函子不仅自然同构，而且以一种相当特殊的方式自然同构。推论 4.3.3 告诉我们，这只是一种错觉：所有自然同构 (4.8) 都是以这种方式得到的。正是 (a) 中的“自然”一词，包含了这些没有明说的细节。

**例 4.3.5** 对任意其他伴随关系也可以作同样的陈述：

![伴随关系 F ⊣ G](/library/volume-87/diagrams/pdf-0110-adjunction-fg.png)

固定 $A \in \mathscr{A}$，令

$$
X = \mathscr{A}(A,G(-))\colon \mathscr{B} \to \mathbf{Set}.
$$

那么 $X$ 可表，而这可以用以下任一方式来表述：

(a) $\mathscr{A}(A,G(B)) \cong \mathscr{B}(F(A),B)$ 关于 $B$ 是自然的；换言之，$X \cong H^{F(A)}$（如引理 4.1.10 所述）；

(b) 单位态射 $\eta_A\colon A \to G(F(A))$ 是逗号范畴 $(A \Rightarrow G)$ 的始对象；也就是说，$\eta_A \in X(F(A))$ 满足条件 (4.7)。

沿着这一观察可以得到定理 2.3.6 的另一种证明；该定理用始对象重新表述了伴随关系。

**例 4.3.6** 对任意群 $G$ 和元素 $x \in G$，存在唯一的同态 $\phi\colon \mathbb{Z} \to G$，使得 $\phi(1) = x$。这意味着 $1 \in U(\mathbb{Z})$ 是遗忘函子 $U\colon \mathbf{Grp} \to \mathbf{Set}$ 的一个泛元素；换言之，当 $\mathscr{A} = \mathbf{Grp}$、$X = U$、$A = \mathbb{Z}$、$u = 1$ 时，条件 (4.7) 成立。因此，$1 \in U(\mathbb{Z})$ 给出了 $U$ 的一个表示 $H^{\mathbb{Z}} \xrightarrow{\sim} U$。

另一方面，把 $1$ 换成 $-1$，同样的结论也成立。由此得到的同构<span class="original-page-anchor" id="pdf-page-111" aria-hidden="true"></span>$H^{\mathbb{Z}} \xrightarrow{\sim} U$，一个来自 $1$，一个来自 $-1$，二者并不相等，因为推论 4.3.3 给出了泛元素与表示之间的*一一*对应。

### 米田嵌入

下面是米田引理的第二个推论。

**推论 4.3.7** 对任意局部小范畴 $\mathscr{A}$，米田嵌入

$$
H_\bullet\colon \mathscr{A} \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]
$$

都是充满且忠实的。

非正式地说，这意味着：对于 $A,A' \in \mathscr{A}$，预层态射 $H_A \to H_{A'}$ 与 $\mathscr{A}$ 中的态射 $A \to A'$ 是同一回事。

**证明** 我们必须对每个 $A,A' \in \mathscr{A}$ 证明函数

$$
\begin{array}{ccc}
\mathscr{A}(A,A') & \to & [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,H_{A'}) \\
f & \mapsto & H_f
\end{array} \tag{4.9}
$$

是双射。由米田引理（取其中的“$X$”为 $H_{A'}$），函数

$$
\tilde{(\ )}\colon H_{A'}(A) \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,H_{A'}) \tag{4.10}
$$

是双射，所以只需证明函数 (4.9) 与 (4.10) 相等。因此，给定 $f\colon A \to A'$，我们必须证明 $\tilde{f} = H_f$，或者等价地，证明 $\widehat{H_f} = f$。事实上，

$$
\widehat{H_f} = (H_f)_A(1_A) = f \circ 1_A = f,
$$

这就是所要证明的。$\square$

在数学中，“嵌入”一词有时非正式地用来表示这样的态射 $A \to B$：它使 $A$ 同构于其在 $B$ 中的像。例如，集合之间的单射 $i\colon A \to B$ 可以称为嵌入，因为它给出了 $A$ 与 $B$ 的子集 $iA$ 之间的双射。类似地，拓扑空间之间的映射 $i\colon A \to B$，如果它到自身的像是同胚，从而 $A \cong iA$，也可以称为嵌入。推论 1.3.19 告诉我们，在范畴论中，把充满且忠实的函子 $\mathscr{A} \to \mathscr{B}$ 称为嵌入是合理的，因为它使 $\mathscr{A}$ 等价于 $\mathscr{B}$ 的一个充满子范畴。

在当前情形中，米田嵌入 $H_\bullet\colon \mathscr{A} \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 把 $\mathscr{A}$ 嵌入自身的预层范畴（图 4.1）。因此，$\mathscr{A}$ 等价于 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 中以可表函子为对象的充满子范畴。

<span class="original-page-anchor" id="pdf-page-112" aria-hidden="true"></span>

![范畴嵌入自身的预层范畴](/library/volume-87/diagrams/pdf-0112-yoneda-embedding.png)

图 4.1 范畴 $\mathscr{A}$ 嵌入自身的预层范畴。

一般来说，充满子范畴是最容易处理的子范畴。例如，给定一个充满子范畴的对象 $A$ 和 $A'$，我们可以毫无歧义地谈论从 $A$ 到 $A'$ 的“态射”；无论把它理解为子范畴中的态射，还是整个范畴中的态射，都没有区别。类似地，我们也可以毫无歧义地谈论子范畴中对象的同构，如下面的引理所述。

**引理 4.3.8** 设 $J\colon \mathscr{A} \to \mathscr{B}$ 是充满且忠实的函子，$A,A' \in \mathscr{A}$。则：

(a) $\mathscr{A}$ 中的态射 $f$ 是同构，当且仅当 $\mathscr{B}$ 中的态射 $J(f)$ 是同构；

(b) 对 $\mathscr{B}$ 中的任意同构 $g\colon J(A) \to J(A')$，存在唯一的 $\mathscr{A}$ 中的同构 $f\colon A \to A'$，使得 $J(f) = g$；

(c) $\mathscr{A}$ 的对象 $A$ 与 $A'$ 同构，当且仅当 $\mathscr{B}$ 的对象 $J(A)$ 与 $J(A')$ 同构。

**证明** 见习题 4.3.15。$\square$

**例 4.3.9** 在例 4.3.6 中，我们考察了遗忘函子 $U\colon \mathbf{Grp} \to \mathbf{Set}$ 的表示，并找到了两个不同的同构 $H^{\mathbb{Z}} \xrightarrow{\sim} U$。我们把它们全部找到了吗？

由于 $H^{\mathbb{Z}} \cong U$，同构 $H^{\mathbb{Z}} \xrightarrow{\sim} U$ 的个数与同构 $H^{\mathbb{Z}} \xrightarrow{\sim} H^{\mathbb{Z}}$ 的个数相同。由推论 4.3.7 和引理 4.3.8(b)，*后者*的个数又与群同构 $\mathbb{Z} \xrightarrow{\sim} \mathbb{Z}$ 的个数相同。这样的群同构恰好有两个（对应于 $\mathbb{Z}$ 的两个生成元 $\pm1$），所以我们确实找到了全部同构 $H^{\mathbb{Z}} \xrightarrow{\sim} U$。换一种说法，$U(\mathbb{Z})$ 恰好有两个泛元素。

在第 6.2 节中，我们将看到，每个预层都可以由可表函子构造出来，粗略地说，就像每个正整数都可以由素数构造出来一样。

<span class="original-page-anchor" id="pdf-page-113" aria-hidden="true"></span>

![从不同视角观察对象](/library/volume-87/diagrams/pdf-0113-objects-viewpoints.png)

图 4.2 若 $\mathscr{A}(B,A) \cong \mathscr{A}(B,A')$ 关于 $B$ 是自然的，则 $A \cong A'$。

### 可表函子的同构

在习题 4.1.27 中，你被要求直接证明：若 $H_A \cong H_{A'}$，则 $A \cong A'$。那个证明包含了米田引理证明中的所有主要思想。这个结果本身也可以由米田引理推出，具体如下。

**推论 4.3.10** 设 $\mathscr{A}$ 是局部小范畴，$A,A' \in \mathscr{A}$。则

$$
H_A \cong H_{A'} \iff A \cong A' \iff H^A \cong H^{A'}.
$$

**证明** 由对偶性，只需证明第一个“$\Longleftrightarrow$”。这可由推论 4.3.7 和引理 4.3.8(c) 得到。$\square$

由于函子总是保持同构（习题 1.2.21），这条陈述的关键在于

$$
H_A \cong H_{A'} \implies A \cong A'.
$$

换言之，若 $\mathscr{A}(B,A) \cong \mathscr{A}(B,A')$ 关于 $B$ 是自然的，则 $A \cong A'$。把 $\mathscr{A}(B,A)$ 看作“从 $B$ 看 $A$”，这个推论就告诉我们：两个对象相同，当且仅当从所有视角看，它们都显得相同（图 4.2）。（如果它看起来像鸭子，走起路来像鸭子，叫起来也像鸭子，那么它大概就是鸭子。）

**例 4.3.11** 考虑推论 4.3.10 中 $\mathscr{A} = \mathbf{Grp}$ 的情形。取两个群 $A$ 和 $A'$，并假设有人告诉我们：对所有群 $B$，$A$ 和 $A'$“从 $B$ 看起来相同”（即 $H_A(B) \cong H_{A'}(B)$）。那么，例如：

- $H_A(1) \cong H_{A'}(1)$，其中 $1$ 是平凡群。但无论 $A$ 和 $A'$ 是什么，$H_A(1) = \mathbf{Grp}(1,A)$ 都是单元素集合，$H_{A'}(1)$ 也是如此。因此，这一点什么也没有告诉我们。

- $H_A(\mathbb{Z}) \cong H_{A'}(\mathbb{Z})$。我们知道 $H_A(\mathbb{Z})$ 是 $A$ 的底集合，$A'$ 的情形也类似。因此，$A$ 与 $A'$ 的底集合同构。不过，仅凭目前所知，它们仍然可能具有完全不同的群结构。

<span class="original-page-anchor" id="pdf-page-114" aria-hidden="true"></span>

- 对每个素数 $p$ 都有 $H_A(\mathbb{Z}/p\mathbb{Z})\cong H_{A'}(\mathbb{Z}/p\mathbb{Z})$，所以由例 4.1.5，$A$ 与 $A'$ 中每一种素数阶的元素个数都相同。

这些同构中的每一个，都只给出关于 $A$ 与 $A'$ 相似性的部分信息。但是，如果我们知道对所有群 $B$ 都有 $H_A(B)\cong H_{A'}(B)$，而且关于 $B$ *自然*，那么 $A\cong A'$。

**例 4.3.12** 集合范畴在这方面非常特殊。对任意集合 $A$，我们有

$$
A\cong\mathbf{Set}(1,A)=H_A(1),
$$

所以 $H_A(1)\cong H_{A'}(1)$ 蕴含 $A\cong A'$。换句话说，如果从单元素集合的观点来看，$\mathbf{Set}$ 中的两个对象看起来相同，那么它们就是相同的。这是集合的一个熟悉特征：一个集合唯一要紧的就是它的元素！

对于一般范畴，推论 4.3.10 告诉我们，如果两个对象具有相同的、所有形状的广义元素，那么它们就是相同的。但是集合范畴具有一个特殊性质：如果我选定一个对象，只告诉你它的形状为 $1$ 的广义元素是什么，那么你就能准确地推断出我的对象必定是什么。

**例 4.3.13** 设 $G:\mathscr{B}\to\mathscr{A}$ 是函子，并且假设 $F$ 和 $F'$ 都是 $G$ 的左伴随。那么对每个 $A\in\mathscr{A}$，我们有

$$
\mathscr{B}(F(A),B)\cong\mathscr{A}(A,G(B))\cong\mathscr{B}(F'(A),B)
$$

关于 $B\in\mathscr{B}$ 自然，所以 $H^{F(A)}\cong H^{F'(A)}$，于是由推论 4.3.10，$F(A)\cong F'(A)$。事实上，这个同构关于 $A$ 自然，因此 $F\cong F'$。这说明左伴随是唯一的，正如注 2.1.2(d) 所断言的那样。对偶地，右伴随是唯一的。另见习题 4.3.18。

**例 4.3.14** 推论 4.3.10 蕴含：如果一个集合值函子同时与 $H^A$ 和 $H^{A'}$ 同构，那么 $A\cong A'$。因此，若表示对象存在，则函子就*确定*了表示对象。例如，考虑例 4.1.9 中的函子

$$
\mathbf{Bilin}(U,V;-):\mathbf{Vect}_k\to\mathbf{Set}
$$

推论 4.3.10 蕴含：在相差同构的意义下，满足

$$
\mathbf{Bilin}(U,V;W)\cong\mathbf{Vect}_k(T,W)
$$

且关于 $W$ 自然的向量空间 $T$ *至多有一个*。可以证明，这样的向量空间 $T$ 确实存在。由于所有这样的空间 $T$ 都同构，因此，把其中任意一个称为 $U$ 与 $V$ 的张量积都是合理的。

<span class="original-page-anchor" id="pdf-page-115" aria-hidden="true"></span>

### 习题

**4.3.15** 证明引理 4.3.8。

**4.3.16** 设 $\mathscr{A}$ 是局部小范畴。直接证明以下各个命题（不使用米田引理）。

(a) $H_\bullet:\mathscr{A}\to[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 是忠实的。

(b) $H_\bullet$ 是充满的。

(c) 给定 $A\in\mathscr{A}$ 和 $\mathscr{A}$ 上的预层 $X$，如果 $X(A)$ 有一个在推论 4.3.2 的意义下具有泛性质的元素 $u$，那么 $X\cong H_A$。

**4.3.17** 在范畴 $\mathscr{A}$ 是离散范畴的情形下，解释第 4 章的理论。例如，预层是什么样的，其中哪些是可表的？米田引理告诉我们什么？它的证明会不会变短？米田引理的各个推论又如何？

**4.3.18** 设 $\mathscr{B}$ 是范畴，$J:\mathscr{C}\to\mathscr{D}$ 是函子。通过与 $J$ 复合，定义了一个诱导函子：

$$
J\circ-:[\mathscr{B},\mathscr{C}]\to[\mathscr{B},\mathscr{D}]
$$

(a) 证明：若 $J$ 充满且忠实，则 $J\circ-$ 也充满且忠实。

(b) 推出：若 $J$ 充满且忠实，且 $G,G':\mathscr{B}\to\mathscr{C}$ 满足 $J\circ G\cong J\circ G'$，那么 $G\cong G'$。

(c) 再推出右伴随是唯一的：若 $F:\mathscr{A}\to\mathscr{B}$ 和 $G,G':\mathscr{B}\to\mathscr{A}$ 满足 $F\dashv G$ 与 $F\dashv G'$，那么 $G\cong G'$。（提示：米田嵌入充满且忠实。）
