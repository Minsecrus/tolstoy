---
title: "第一章 范畴、函子与自然变换"
description: "Tom Leinster《Basic Category Theory》中文译文。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"导论","link":"/library/volume-87/introduction"}
next: {"text":"第二章 伴随函子","link":"/library/volume-87/chapter-002"}
---

# 第一章 范畴、函子与自然变换

<span class="original-page-anchor" id="pdf-page-18" aria-hidden="true"></span>

范畴是一个由相互关联的对象组成的系统。这些对象并非孤立存在：对象之间有某种意义下的态射，把它们联系起来。

“对象”一词的典型例子有“群”和“拓扑空间”，而与之对应的“态射”的典型例子分别是“同态”和“连续映射”。我们将看到许多例子，也将了解到，有些范畴与刚才提到的这两种范畴风格大不相同。事实上，范畴论中的“态射”完全不必类似于你很可能已经熟悉的通常意义上的映射。

范畴*本身*也是数学对象；既然如此，“范畴之间的态射”也有一个恰当的概念，就不足为奇了。这种态射称为函子。也许更令人惊讶的是，还有第三个层次：我们可以讨论*函子*之间的态射，它们称为自然变换。因此，自然变换是函子之间的态射，而函子本身又是范畴之间的态射。

事实上，正是将自然变换的概念形式化的愿望，促成了范畴论的诞生。到 20 世纪 40 年代初，代数拓扑的研究者已经开始使用“自然变换”这个词组，但用法还只是非正式的。两位数学家 Samuel Eilenberg 和 Saunders Mac Lane 看出，需要给它一个精确的定义。然而，要定义自然变换，他们必须先定义函子；要定义函子，又必须先定义范畴。于是，这门学科便诞生了。

如今，范畴论的应用已经远远超出代数拓扑。它的触角伸入纯数学的大多数领域，也延伸到应用数学的某些领域；其中也许最显著的是，范畴论已经成为计算机科学某些领域中的标准工具。应用数学可不只是应用微分方程！

<span class="original-page-anchor" id="pdf-page-19" aria-hidden="true"></span>

## 1.1 范畴

**定义 1.1.1** 一个**范畴** $\mathscr{A}$ 由以下数据组成：

- 一个由**对象**组成的集类 $\operatorname{ob}(\mathscr{A})$；
- 对每一对 $A,B\in\operatorname{ob}(\mathscr{A})$，一个从 $A$ 到 $B$ 的**映射**、**箭头**或**态射**组成的集类 $\mathscr{A}(A,B)$；
- 对每一组 $A,B,C\in\operatorname{ob}(\mathscr{A})$，一个函数

$$
\begin{array}{ccc}
\mathscr{A}(B,C)\times\mathscr{A}(A,B)&\to&\mathscr{A}(A,C)\\
(g,f)&\mapsto&g\circ f,
\end{array}
$$

称为**复合**；

- 对每个 $A\in\operatorname{ob}(\mathscr{A})$，一个 $\mathscr{A}(A,A)$ 中的元素 $1_A$，称为 $A$ 上的**恒等态射**，

这些数据满足以下公理：

- **结合律**：对每个 $f\in\mathscr{A}(A,B)$、$g\in\mathscr{A}(B,C)$ 和 $h\in\mathscr{A}(C,D)$，都有 $(h\circ g)\circ f=h\circ(g\circ f)$；
- **恒等律**：对每个 $f\in\mathscr{A}(A,B)$，都有 $f\circ1_A=f=1_B\circ f$。

**注 1.1.2** (a) 我们常使用以下写法：

$$
\begin{array}{rcl}
A\in\mathscr{A}&\text{表示}&A\in\operatorname{ob}(\mathscr{A});\\
f\colon A\to B\text{ 或 }A\xrightarrow{f}B&\text{表示}&f\in\mathscr{A}(A,B);\\
gf&\text{表示}&g\circ f.
\end{array}
$$

人们也把 $\mathscr{A}(A,B)$ 写作 $\operatorname{Hom}_{\mathscr{A}}(A,B)$ 或 $\operatorname{Hom}(A,B)$。记号“$\operatorname{Hom}$”是 homomorphism（同态）的缩写，来自最早出现的范畴例子之一。

(b) 范畴的定义保证，一般来说，从 $\mathscr{A}$ 中的任意一串态射

$$
A_0\xrightarrow{f_1}A_1\xrightarrow{f_2}\ \cdots\ \xrightarrow{f_n}A_n
$$

出发，都恰好能够构造出一个态射

$$
A_0\to A_n
$$

（即 $f_n f_{n-1}\cdots f_1$）。如果还给出额外的信息，我们也许就能构造出其他态射 $A_0\to A_n$；例如，若恰好知道 $A_{n-1}=A_n$，那么 $f_{n-1}f_{n-2}\cdots f_1$ 也是一个这样的态射。但这里谈的是没有额外信息时的*一般*情形。

例如，当 $n=4$ 时，这样的一串态射产生如下态射

![从 A₀ 到 A₄ 的两个复合](/library/volume-87/diagrams/pdf-0019-associativity.png)

<span class="original-page-anchor" id="pdf-page-20" aria-hidden="true"></span>

但公理说明它们相等。因此，可以放心地省略括号，把两者都写成 $f_4 f_3 f_2 f_1$。

这里考虑的是 $n\geq0$ 的情形。当 $n=0$ 时，上面的陈述是说：对范畴中的每个对象 $A_0$，都恰好能够构造出一个态射 $A_0\to A_0$（即恒等态射 $1_{A_0}$）。恒等态射可以看作零重的复合，这与把数 $1$ 看作零个数的乘积十分相似。

(c) 我们常常谈到**交换图**。例如，给定一个范畴中的对象和态射

![一个交换图](/library/volume-87/diagrams/pdf-0020-commutative.png)

如果 $gf=jih$，就说这个图**交换**。一般而言，说一个图交换，是指只要从某个对象 $X$ 到某个对象 $Y$ 有两条路径，沿其中一条路径复合所得的从 $X$ 到 $Y$ 的态射，就等于沿另一条路径复合所得的态射。

(d) “集类”（collection）这个稍显含糊的词，意思与“集合”*大致*相同；不过，若熟悉这一方面的概念，最好把它理解为“类”。我们将在第 3 章回到这个问题。

(e) 若 $f\in\mathscr{A}(A,B)$，我们称 $A$ 为 $f$ 的**定义域**，称 $B$ 为它的**陪域**。每个范畴中的每个态射都有确定的定义域和确定的陪域。（如果你认为对任意一对抽象集合取交集是有意义的，那么就应当在范畴的定义中加上条件：除非 $A=A'$ 且 $B=B'$，否则 $\mathscr{A}(A,B)\cap\mathscr{A}(A',B')=\emptyset$。）

**例 1.1.3（数学结构构成的范畴）** (a) 有一个范畴 $\mathbf{Set}$，描述如下。它的对象是集合。给定集合 $A$ 和 $B$，范畴 $\mathbf{Set}$ 中从 $A$ 到 $B$ 的态射，恰好就是通常所说的从 $A$ 到 $B$ 的映射（或函数）。范畴中的复合就是通常的函数复合，而恒等态射也正是你所预期的。

在这样的情形中，我们往往不特意说明复合与恒等态射。我们写“集合与函数构成的范畴”，把其余部分留给读者自行推断。事实上，我们通常还会更进一步，直接把它叫作“集合范畴”。

(b) 有一个群范畴 $\mathbf{Grp}$，它的对象是群，态射是群同态。

(c) 类似地，有一个由环及环同态构成的范畴 $\mathbf{Ring}$。

<span class="original-page-anchor" id="pdf-page-21" aria-hidden="true"></span>

(d) 对每个域 $k$，有一个范畴 $\mathbf{Vect}_k$，由 $k$ 上的向量空间及它们之间的线性映射构成。

(e) 有一个由拓扑空间及连续映射构成的范畴 $\mathbf{Top}$。

本章主要讨论范畴*之间*的相互作用，而非它们*内部*发生的事情。不过，我们仍然需要下面的定义。

**定义 1.1.4** 范畴 $\mathscr{A}$ 中的态射 $f\colon A\to B$ 称为**同构**，如果 $\mathscr{A}$ 中存在态射 $g\colon B\to A$，使得 $gf=1_A$ 且 $fg=1_B$。

在定义 1.1.4 的情形中，我们称 $g$ 为 $f$ 的**逆**，并写作 $g=f^{-1}$。（为何能称作“这个”逆，见习题 1.1.13。）如果存在一个从 $A$ 到 $B$ 的同构，就说 $A$ 与 $B$ **同构**，并写作 $A\cong B$。

**例 1.1.5** $\mathbf{Set}$ 中的同构恰好是双射。这个结论从逻辑上说，并不是那么显然。它实际上是在说：一个函数有双侧逆，当且仅当它既是单射又是满射。

**例 1.1.6** $\mathbf{Grp}$ 中的同构恰好是群同构。同样，这也并非完全显然，至少在你所学的群同构定义是“双射的同态”时是这样。要说明这个定义与在 $\mathbf{Grp}$ 中成为同构是等价的，就必须证明：双射同态的逆也是同态。

类似地，$\mathbf{Ring}$ 中的同构恰好是环同构。

**例 1.1.7** $\mathbf{Top}$ 中的同构恰好是同胚。注意，与 $\mathbf{Grp}$ 和 $\mathbf{Ring}$ 中的情形不同，$\mathbf{Top}$ 中的双射态射不一定是同构。一个经典的例子是映射

$$
\begin{array}{ccc}
[0,1)&\to&\{z\in\mathbb{C}\mid |z|=1\}\\
t&\mapsto&e^{2\pi i t},
\end{array}
$$

它是连续双射，却不是同胚。

前面提到的范畴例子虽然重要，却可能给人一种错误印象。在每个例子中，范畴的对象都是带有结构的集合（例如群结构、拓扑，或者像 $\mathbf{Set}$ 的情形那样，根本没有任何结构）。态射则是在相应意义下保持这种结构的函数。而且，在每个例子中，都能清楚地说明给定对象的元素是什么。

然而，并非所有范畴都是如此。一般来说，范畴的对象并不是“添上了额外东西的集合”。因此，在一般的范畴中，谈论对象的“元素”并没有意义。（至少，这种意义并不<span class="original-page-anchor" id="pdf-page-22" aria-hidden="true"></span>显而易见；我们将在定义 4.1.25 中回到这个问题。）类似地，在一般的范畴中，态射也不必是通常意义下的映射或函数。因此：

*范畴的对象可以完全不像集合。*

*范畴中的态射可以完全不像函数。*

接下来的几个例子说明了这些观点。它们还表明，与前面可能给人的印象相反，范畴不必规模巨大。某些范畴本身就是小巧、易于掌握的结构，下面就来看一看。

**例 1.1.8（作为数学结构的范畴）** (a) 可以直接说明一个范畴的对象、态射、复合与恒等态射是什么，从而确定这个范畴。例如，有一个范畴 $\emptyset$，完全没有对象，也没有态射。有一个范畴 $\mathbf{1}$，只有一个对象，且仅有恒等态射。它可以画成这样：

$$
\bullet
$$

（因为每个对象都必须有一个自身的恒等态射，我们通常不特意把恒等态射画出来。）另一个范畴可以画成

$$
\bullet\to\bullet\qquad\text{或}\qquad A\xrightarrow{f}B,
$$

它有两个对象，以及一个从第一个对象到第二个对象的非恒等态射。（复合按唯一可能的方式定义。）再强调一下前面提到的观点：$A$ 或 $B$ 的“元素”究竟是什么，或者如何能把 $f$ 看作某种“函数”，都并不显然。

构造更复杂的例子很容易。例如，这里还有三个范畴：

![另外三个范畴](/library/volume-87/diagrams/pdf-0022-categories.png)

(b) 有些范畴除恒等态射以外，没有任何其他态射（作为范畴，恒等态射是它们必须具有的）。这样的范畴称为**离散**范畴。一个离散范畴仅仅相当于一个对象类。用更富诗意的说法，范畴是一个由彼此或多或少有所关联的对象组成的集类；离散范畴则是极端情形，其中每个对象都与其同伴完全隔绝。

<span class="original-page-anchor" id="pdf-page-23" aria-hidden="true"></span>

(c) 群本质上等同于只有一个对象、且所有态射都是同构的范畴。

为理解这一点，先考虑只有一个对象的范畴 $\mathscr{A}$。用什么字母或符号表示这个对象并不重要；不妨称它为 $A$。于是，$\mathscr{A}$ 由一个集合（或类）$\mathscr{A}(A,A)$、一个满足结合律的复合函数

$$
\circ\colon\mathscr{A}(A,A)\times\mathscr{A}(A,A)\to\mathscr{A}(A,A),
$$

以及一个双侧单位 $1_A\in\mathscr{A}(A,A)$ 组成。这样，$\mathscr{A}(A,A)$ 离成为群就只差尚未提到的逆了。然而，说 $\mathscr{A}$ 中的每个态射都是同构，恰好就是说 $\mathscr{A}(A,A)$ 的每个元素关于 $\circ$ 都有逆。

如果用 $G$ 表示群 $\mathscr{A}(A,A)$，对应关系如下：

$$
\begin{array}{ll}
\text{只有一个对象 }A\text{ 的范畴 }\mathscr{A}&\text{对应的群 }G\\[1ex]
\mathscr{A}\text{ 中的态射}&G\text{ 的元素}\\
\mathscr{A}\text{ 中的 }\circ&G\text{ 中的 }\cdot\\
1_A&1\in G
\end{array}
$$

范畴 $\mathscr{A}$ 大致如下：

![带有环形箭头的单对象范畴](/library/volume-87/diagrams/pdf-0023-group-category.png)

这些箭头表示不同的态射 $A\to A$，也就是群 $G$ 的不同元素。

$\mathscr{A}$ 的对象叫什么名字，并没有区别。这就像在代数问题中选用 $x$、$y$ 还是 $t$ 表示某个变量一样，毫不重要。稍后我们将定义范畴的“等价”，从而能够精确地说：群范畴等价于由（小的）单对象范畴组成的范畴，其中每个单对象范畴的所有态射都是同构（例 3.2.11）。

初次遇到群是一种范畴这一想法时，人们容易把它当成巧合或技巧而不以为意。但事实并非如此；其中确实包含实质内容。

为了看清这一点，假设你的学习顺序被打乱，在学习群之前就已经了解了范畴。在第一堂群论课上，教师宣布，群应当是某个对象的所有对称构成的系统。她说，对象 $X$ 的一个对称，就是以可逆的方式将 $X$ 映射到它自身的一种办法。这时，你意识到她谈论的是一种非常特殊的<span class="original-page-anchor" id="pdf-page-24" aria-hidden="true"></span>范畴。一般而言，一个范畴是由*许多*对象（通常不只有一个）之间的*所有*映射（通常不只有可逆映射）组成的系统。因此，群就是一种具有特殊性质的范畴：所有态射都可逆，而且只有一个对象。

(d) 在前一个例子中，逆元不是关键，所以不妨考虑一下“没有逆元的群”。它们称为幺半群。

形式上，**幺半群**是配备了一个满足结合律的二元运算和一个双侧单位元的集合。群描述可以施加于某个对象的可逆变换，也就是对称；幺半群描述不一定可逆的变换。例如，给定任意集合 $X$，所有双射 $X \to X$ 组成一个群，而所有函数 $X \to X$ 组成一个幺半群。在这两种情形中，二元运算都是复合，单位元都是 $X$ 上的恒等函数。幺半群的另一个例子是自然数集 $\mathbb{N} = \{0, 1, 2, \ldots\}$，以 $+$ 为运算，以 $0$ 为单位元。或者，我们也可以取集合 $\mathbb{N}$，以 $\cdot$ 为运算，以 $1$ 为单位元。

由与群的情形相同的论证，只有一个对象的范畴本质上与幺半群是同一回事。例 3.2.11 会给出正式表述。

(e) **预序**是一个自反、传递的二元关系。**预序集** $(S, {\leq})$ 是一个集合 $S$，连同其上的一个预序 $\leq$。例如：$S = \mathbb{R}$，而 $\leq$ 具有通常的含义；$S$ 是 $\{1, \ldots, 10\}$ 的所有子集组成的集合，而 $\leq$ 是 $\subseteq$（包含关系）；$S = \mathbb{Z}$，而 $a \leq b$ 表示 $a$ 整除 $b$。

一个预序集可以看作一个范畴 $\mathscr{A}$，其中对每一对 $A, B \in \mathscr{A}$，从 $A$ 到 $B$ 至多有一个态射。为了说明这一点，考虑一个具有此性质的范畴 $\mathscr{A}$。我们用什么字母表示从对象 $A$ 到对象 $B$ 的唯一态射并不重要；我们只需记录哪些对象对 $(A, B)$ 具有确实存在态射 $A \to B$ 这一性质。我们用 $A \leq B$ 表示存在态射 $A \to B$。

由于 $\mathscr{A}$ 是范畴，而范畴具有复合，因此若 $A \leq B \leq C$，则 $A \leq C$。由于范畴还具有恒等态射，因此对所有 $A$ 都有 $A \leq A$。结合律和恒等律公理自动成立。所以，$\mathscr{A}$ 就相当于一族对象，配备了一个传递、自反的二元关系，即预序。可以把唯一的态射 $A \to B$ 理解为陈述或断言 $A \leq B$。

集合上的一个**序**是满足下述性质的预序 $\leq$：若 $A \leq B$ 且 $B \leq A$，则 $A = B$。（等价地，若在相应的范畴中 $A \cong B$，则 $A = B$。）有序集也称为**偏序集**，英文简称 **poset**。

<span class="original-page-anchor" id="pdf-page-25" aria-hidden="true"></span>

预序不一定是序，例如 $\mathbb{Z}$ 上的整除关系 $\mid$：在这里，$2 \mid {-2}$ 且 $-2 \mid 2$，但 $2 \neq -2$。

下面给出从已有范畴构造新范畴的两种方法。

**构造 1.1.9** 每个范畴 $\mathscr{A}$ 都有一个**反范畴**或**对偶范畴** $\mathscr{A}^{\mathrm{op}}$，它通过反转箭头来定义。形式上，$\operatorname{ob}(\mathscr{A}^{\mathrm{op}}) = \operatorname{ob}(\mathscr{A})$，而且对所有对象 $A$ 和 $B$，都有 $\mathscr{A}^{\mathrm{op}}(B, A) = \mathscr{A}(A, B)$。$\mathscr{A}^{\mathrm{op}}$ 中的恒等态射与 $\mathscr{A}$ 中的相同。$\mathscr{A}^{\mathrm{op}}$ 中的复合也与 $\mathscr{A}$ 中的相同，只是参与复合的两个态射顺序相反。具体说来，若 $A \xrightarrow{f} B \xrightarrow{g} C$ 是 $\mathscr{A}^{\mathrm{op}}$ 中的态射，则 $A \xleftarrow{f} B \xleftarrow{g} C$ 是 $\mathscr{A}$ 中的态射；它们给出 $\mathscr{A}$ 中的一个态射 $A \xleftarrow{f \circ g} C$，而原来那一对态射的复合就是 $\mathscr{A}^{\mathrm{op}}$ 中相应的态射 $A \to C$。

因此，$\mathscr{A}$ 中的箭头 $A \to B$ 对应于 $\mathscr{A}^{\mathrm{op}}$ 中的箭头 $B \to A$。按照上述定义，若 $f\colon A \to B$ 是 $\mathscr{A}$ 中的箭头，那么 $\mathscr{A}^{\mathrm{op}}$ 中相应的箭头 $B \to A$ 也称为 $f$。有些人更愿意给它另一个名称，例如 $f^{\mathrm{op}}$。

**注 1.1.10** **对偶原理**是范畴论的一个基本原理。非正式地说，它指出每个范畴论定义、定理和证明都有一个**对偶**，可通过反转所有箭头得到。运用对偶原理可以节省工作：给定任意定理，将其陈述和证明中的所有箭头反转，就得到一个对偶定理。本书各处会出现许多对偶的例子。

**构造 1.1.11** 给定范畴 $\mathscr{A}$ 和 $\mathscr{B}$，有一个**积范畴** $\mathscr{A} \times \mathscr{B}$，其中

$$
\begin{aligned}
\operatorname{ob}(\mathscr{A} \times \mathscr{B}) &= \operatorname{ob}(\mathscr{A}) \times \operatorname{ob}(\mathscr{B}), \\
(\mathscr{A} \times \mathscr{B})((A, B), (A', B')) &= \mathscr{A}(A, A') \times \mathscr{B}(B, B').
\end{aligned}
$$

换句话说，积范畴 $\mathscr{A} \times \mathscr{B}$ 中的一个对象是一个有序对 $(A, B)$，其中 $A \in \mathscr{A}$ 且 $B \in \mathscr{B}$。$\mathscr{A} \times \mathscr{B}$ 中的一个态射 $(A, B) \to (A', B')$ 是一个有序对 $(f, g)$，其中 $f\colon A \to A'$ 是 $\mathscr{A}$ 中的态射，而 $g\colon B \to B'$ 是 $\mathscr{B}$ 中的态射。$\mathscr{A} \times \mathscr{B}$ 中复合与恒等态射的定义见习题 1.1.14。

### 习题

**1.1.12** 找出三个上文未提到的范畴的例子。

**1.1.13** 证明：范畴中的一个态射至多有一个逆态射。也就是说，给定态射 $f\colon A \to B$，证明至多存在一个态射 $g\colon B \to A$，使得 $gf = 1_A$ 且 $fg = 1_B$。

<span class="original-page-anchor" id="pdf-page-26" aria-hidden="true"></span>

**1.1.14** 设 $\mathscr{A}$ 和 $\mathscr{B}$ 为范畴。构造 1.1.11 定义了积范畴 $\mathscr{A} \times \mathscr{B}$，但没有给出 $\mathscr{A} \times \mathscr{B}$ 中复合与恒等态射的定义。定义它们只有一种合理的方法；请将其写出。

**1.1.15** 有一个范畴 $\mathbf{Toph}$，其对象是拓扑空间，其态射 $X \to Y$ 是从 $X$ 到 $Y$ 的连续映射的同伦类。为了证明 $\mathbf{Toph}$ 是一个范畴，你需要知道同伦的哪些性质？只用拓扑学术语来表述，$\mathbf{Toph}$ 中的两个对象同构意味着什么？

## 1.2 函子

范畴论告诉我们：每当遇到一类新的数学对象时，都应当问一问，这些对象之间是否有合理的“映射”概念。我们也可以对范畴本身提出这个问题。答案是有的，范畴之间的映射称为函子。

**定义 1.2.1** 设 $\mathscr{A}$ 和 $\mathscr{B}$ 为范畴。一个**函子** $F\colon \mathscr{A} \to \mathscr{B}$ 由以下数据组成：

- 一个函数

  $$
  \operatorname{ob}(\mathscr{A}) \to \operatorname{ob}(\mathscr{B}),
  $$

  记作 $A \mapsto F(A)$；

- 对每一对 $A, A' \in \mathscr{A}$，一个函数

  $$
  \mathscr{A}(A, A') \to \mathscr{B}(F(A), F(A')),
  $$

  记作 $f \mapsto F(f)$，

并满足下列公理：

- 只要 $A \xrightarrow{f} A' \xrightarrow{f'} A''$ 是 $\mathscr{A}$ 中的态射，就有 $F(f' \circ f) = F(f') \circ F(f)$；
- 只要 $A \in \mathscr{A}$，就有 $F(1_A) = 1_{F(A)}$。

**注 1.2.2** (a) 函子的定义保证，对于 $\mathscr{A}$ 中的每一串态射

$$
A_0 \xrightarrow{f_1} \cdots \xrightarrow{f_n} A_n
$$

（其中 $n \geq 0$），都恰好可以构造出 $\mathscr{B}$ 中的一个态射

$$
F(A_0) \to F(A_n).
$$

<span class="original-page-anchor" id="pdf-page-27" aria-hidden="true"></span>

例如，给定 $\mathscr{A}$ 中的态射

$$
A_0 \xrightarrow{f_1} A_1 \xrightarrow{f_2} A_2 \xrightarrow{f_3} A_3 \xrightarrow{f_4} A_4
$$

我们可以构造出 $\mathscr{B}$ 中的态射

![从 F(A₀) 到 F(A₄) 的两条平行箭头，标签分别为 F(f₄f₃)F(f₂f₁) 和 F(1_{A₄})F(f₄)F(f₃f₂)F(f₁)。](/library/volume-87/diagrams/pdf-0027-functor-parallel-maps.png)

但公理蕴含它们相等。

(b) 我们熟悉这样一个观念：各种结构及其间保持结构的映射组成一个范畴（例如 $\mathbf{Grp}$、$\mathbf{Ring}$ 等）。特别地，这也适用于范畴和函子：有一个范畴 $\mathbf{CAT}$，其对象是范畴，其态射是函子。

这首先意味着，函子可以复合。也就是说，给定函子 $\mathscr{A} \xrightarrow{F} \mathscr{B} \xrightarrow{G} \mathscr{C}$，按显而易见的方式将它们复合，就得到一个新函子 $\mathscr{A} \xrightarrow{G \circ F} \mathscr{C}$。这还意味着，对每个范畴 $\mathscr{A}$，都有一个恒等函子 $1_{\mathscr{A}}\colon \mathscr{A} \to \mathscr{A}$。

**例 1.2.3** 最容易理解的函子例子或许是所谓的**遗忘函子**。（这是一个非正式术语，没有精确定义。）例如：

(a) 有一个函子 $U\colon \mathbf{Grp} \to \mathbf{Set}$，定义如下：若 $G$ 是一个群，则 $U(G)$ 是 $G$ 的底集（即其元素组成的集合）；若 $f\colon G \to H$ 是一个群同态，则 $U(f)$ 就是函数 $f$ 本身。因此，$U$ 遗忘群的群结构，也遗忘群同态是同态这一事实。

(b) 类似地，有一个函子 $\mathbf{Ring} \to \mathbf{Set}$，遗忘环上的环结构；而且（对任意域 $k$）有一个函子 $\mathbf{Vect}_k \to \mathbf{Set}$，遗忘向量空间上的向量空间结构。

(c) 遗忘函子不必遗忘*所有*结构。例如，令 $\mathbf{Ab}$ 为阿贝尔群的范畴。有一个函子 $\mathbf{Ring} \to \mathbf{Ab}$，遗忘乘法结构，只记住底层的加法群。或者，令 $\mathbf{Mon}$ 为幺半群的范畴。有一个函子 $U\colon \mathbf{Ring} \to \mathbf{Mon}$，遗忘加法结构，只记住底层的乘法幺半群。（也就是说，若 $R$ 是环，则 $U(R)$ 就是通过 $\cdot$ 和 $1$ 构成幺半群的集合 $R$。）

(d) 有一个包含函子 $U\colon \mathbf{Ab} \to \mathbf{Grp}$，对任意阿贝尔群 $A$ 定义 $U(A) = A$，对任意阿贝尔群同态 $f$ 定义 $U(f) = f$。它遗忘阿贝尔群是阿贝尔的这一事实。

<span class="original-page-anchor" id="pdf-page-28" aria-hidden="true"></span>

例 (a)–(c) 中的遗忘函子遗忘对象上的*结构*，而例 (d) 中的函子遗忘一个*性质*。不过，在这两种情形中使用同一个词“遗忘”，仍然很方便。

虽然遗忘是一个平凡的操作，但在某些情形中却很有力量。例如，有一个定理说，任意有限域的阶都是某个素数的幂。其证明中的一个重要步骤，就是单纯遗忘这个域是域，只记住它是其子域 $\{0, 1, 1 + 1, 1 + 1 + 1, \ldots\}$ 上的一个向量空间。

**例 1.2.4** **自由函子**在某种意义上与遗忘函子对偶（我们将在下一章看到这一点），不过它们没有那么初等。同样，“自由函子”是一个非正式但有用的术语。

(a) 给定任意集合 $S$，可以构造 $S$ 上的**自由群** $F(S)$。这个群包含 $S$ 作为子集；除不得不满足的性质外，不再作其他要求，具体含义将在第 2.1 节中阐明。直观地说，群 $F(S)$ 是从集合 $S$ 出发，只添加成为群所必需的新元素而得到的，同时不施加群的定义所强制要求之外的任何等式。

稍微精确地说，$F(S)$ 的元素是形式表达式，或者称为**字**，例如 $x^{-4} y x^2 z y^{-3}$（其中 $x, y, z \in S$）。如果一个字可以通过通常的消去规则由另一个字得到，就认为这两个字相等；因此，例如 $x^3 x y$、$x^4 y$ 和 $x^2 y^{-1} y x^2 y$ 都表示 $F(S)$ 中的同一个元素。两个字相乘，只需将一个接在另一个后面写出；例如，$x^{-4} y x$ 乘以 $x z y^{-3}$ 就是 $x^{-4} y x^2 z y^{-3}$。

这一构造给每个集合 $S$ 指派一个群 $F(S)$。事实上，$F$ 是一个函子：任意集合映射 $f\colon S \to S'$ 都产生一个群同态 $F(f)\colon F(S) \to F(S')$。例如，取集合映射

$$
f\colon \{w, x, y, z\} \to \{u, v\}
$$

定义为 $f(w) = f(x) = f(y) = u$ 且 $f(z) = v$。这产生一个同态

$$
F(f)\colon F(\{w, x, y, z\}) \to F(\{u, v\}),
$$

它把 $x^{-4} y x^2 z y^{-3} \in F(\{w, x, y, z\})$ 映到

$$
u^{-4} u u^2 v u^{-3} = u^{-1} v u^{-3} \in F(\{u, v\}).
$$

(b) 类似地，我们可以构造集合 $S$ 上的自由交换环 $F(S)$，从而得到一个从 $\mathbf{Set}$ 到交换环范畴 $\mathbf{CRing}$ 的函子 $F$。事实上，$F(S)$ 是一个熟悉的对象，即以相互交换的变量 $x_s$（$s \in S$）为变量的 $\mathbb{Z}$ 上的多项式环。（毕竟，多项式不过是一个<span class="original-page-anchor" id="pdf-page-29" aria-hidden="true"></span>用环运算 $+$、$-$ 和 $\cdot$ 从这些变量构成的形式表达式。）例如，如果 $S$ 是一个二元集，那么 $F(S)\cong\mathbb{Z}[x,y]$。

(c) 我们也可以在一个集合上构造自由向量空间。固定一个域 $k$。自由函子 $F:\mathbf{Set}\to\mathbf{Vect}_k$ 在对象上的定义是：令 $F(S)$ 为一个以 $S$ 为基的向量空间。任意两个这样的向量空间都是同构的；但这样的向量空间是否存在，或许并不显然，因此我们必须构造一个。粗略地说，$F(S)$ 是 $S$ 的元素的一切形式 $k$-线性组合构成的集合，也就是形如

$$
\sum_{s\in S}\lambda_s s
$$

的表达式，其中每个 $\lambda_s$ 都是标量，而且只有有限多个 $s$ 满足 $\lambda_s\ne 0$。（加上这个限制，是因为在向量空间中只能取*有限*和。）$F(S)$ 的元素可以相加：

$$
\sum_{s\in S}\lambda_s s+\sum_{s\in S}\mu_s s=\sum_{s\in S}(\lambda_s+\mu_s)s.
$$

$F(S)$ 上还有一个标量乘法：

$$
c\cdot\sum_{s\in S}\lambda_s s=\sum_{s\in S}(c\lambda_s)s
$$

（$c\in k$）。这样，$F(S)$ 就成为一个向量空间。

为了完全精确，并避免谈论“表达式”，我们可以把 $F(S)$ 定义为所有满足 $\{s\in S\mid\lambda(s)\ne 0\}$ 为有限集的函数 $\lambda:S\to k$ 所构成的集合。（把这样的函数 $\lambda$ 看作对应于表达式 $\sum_{s\in S}\lambda(s)s$。）为了定义 $F(S)$ 上的加法，我们必须为每一对 $\lambda,\mu\in F(S)$ 定义一个和 $\lambda+\mu\in F(S)$；它由

$$
(\lambda+\mu)(s)=\lambda(s)+\mu(s)
$$

给出（$s\in S$）。类似地，标量乘法由 $(c\cdot\lambda)(s)=c\cdot\lambda(s)$ 给出（$c\in k$，$\lambda\in F(S)$，$s\in S$）。

环和向量空间有一个特殊性质：为自由函子写出显式公式相对容易。群的情形则典型得多。对于大多数类型的代数结构，描述自由函子所需的繁琐工作与群的情形一样多。我们将在例 2.1.3 和例 6.3.11 中回到这一点（在那里，我们会看到如何完全避开这些繁琐工作）。

**例 1.2.5（代数拓扑中的函子）** 从历史上看，最早的一些函子实例出现在代数拓扑中。在那里，采用的策略是<span class="original-page-anchor" id="pdf-page-30" aria-hidden="true"></span>以某种巧妙的方式从空间中提取数据，把这些数据组织成一个代数结构，然后转而研究这个代数结构，以此了解原来的空间。因此，代数拓扑涉及许多从空间范畴到代数范畴的函子。

(a) 令 $\mathbf{Top}_*$ 为由带有基点的拓扑空间及保持基点的连续映射构成的范畴。有一个函子 $\pi_1:\mathbf{Top}_*\to\mathbf{Grp}$，它把每个带有基点 $x$ 的空间 $X$ 送到 $X$ 在 $x$ 处的基本群 $\pi_1(X,x)$。（有些文献使用更简单的记号 $\pi_1(X)$，忽略基点的选择。如果 $X$ 是道路连通的，这样做大致不会出问题，但严格地说，始终应当指定基点。）

$\pi_1$ 是函子，意味着它不仅把每个带基点的空间 $(X,x)$ 对应到群 $\pi_1(X,x)$，而且还把每个保持基点的连续映射

$$
f:(X,x)\to(Y,y)
$$

对应到一个同态

$$
\pi_1(f):\pi_1(X,x)\to\pi_1(Y,y).
$$

通常把 $\pi_1(f)$ 记作 $f_*$。函子性公理表明 $(g\circ f)_*=g_*\circ f_*$，并且 $(1_{(X,x)})_*=1_{\pi_1(X,x)}$。

(b) 对于每个 $n\in\mathbb{N}$，都有一个函子 $H_n:\mathbf{Top}\to\mathbf{Ab}$，把一个空间对应到它的第 $n$ 个同调群（可以采用几种可能的意义中的任何一种）。

**例 1.2.6** 任何多项式方程组，例如

$$
2x^2+y^2-3z^2=1\tag{1.1}
$$

$$
x^3+x=y^2\tag{1.2}
$$

都产生一个函子 $\mathbf{CRing}\to\mathbf{Set}$。事实上，对于每个交换环 $A$，令 $F(A)$ 为满足方程 (1.1) 和 (1.2) 的三元组 $(x,y,z)\in A\times A\times A$ 构成的集合。每当 $f:A\to B$ 是一个环同态且 $(x,y,z)\in F(A)$ 时，都有 $(f(x),f(y),f(z))\in F(B)$；因此环映射 $f:A\to B$ 诱导一个集合映射 $F(f):F(A)\to F(B)$。这就定义了一个函子 $F:\mathbf{CRing}\to\mathbf{Set}$。

在代数几何中，**概形**是一个具有某些性质的函子 $\mathbf{CRing}\to\mathbf{Set}$。（这并非陈述该定义最常见的方式，但它是等价的。）上面的函子 $F$ 就是一个简单的例子。

**例 1.2.7** 令 $G$ 和 $H$ 为幺半群（也可以是群，如果你愿意），将它们视为单对象范畴 $\mathscr{G}$ 和 $\mathscr{H}$。函子 $F:\mathscr{G}\to\mathscr{H}$ 必须把 $\mathscr{G}$ 的唯一对象映到 $\mathscr{H}$ 的唯一对象，因此，它在态射上的<span class="original-page-anchor" id="pdf-page-31" aria-hidden="true"></span>作用便决定了这个函子。因此，函子 $F:\mathscr{G}\to\mathscr{H}$ 相当于一个函数 $F:G\to H$，满足对所有 $g',g\in G$ 都有 $F(g'g)=F(g')F(g)$，且 $F(1)=1$。换言之，函子 $\mathscr{G}\to\mathscr{H}$ 就是一个同态 $G\to H$。

**例 1.2.8** 令 $G$ 为一个幺半群，将其视为单对象范畴 $\mathscr{G}$。函子 $F:\mathscr{G}\to\mathbf{Set}$ 由一个集合 $S$（$F$ 在 $\mathscr{G}$ 的唯一对象处的值），以及对每个 $g\in G$ 给出的一个函数 $F(g):S\to S$ 组成，并满足函子性公理。记 $(F(g))(s)=g\cdot s$，我们便看到函子 $F$ 相当于一个集合 $S$ 连同一个函数

$$
\begin{array}{ccc}
G\times S&\to&S\\
(g,s)&\mapsto&g\cdot s
\end{array}
$$

满足对所有 $g,g'\in G$ 和 $s\in S$ 都有 $(g'g)\cdot s=g'\cdot(g\cdot s)$ 及 $1\cdot s=s$。换言之，函子 $\mathscr{G}\to\mathbf{Set}$ 就是一个配有 $G$ 的左作用的集合，简称**左 $G$-集**。

类似地，函子 $\mathscr{G}\to\mathbf{Vect}_k$ 恰好就是表示论意义下 $G$ 的一个 $k$-线性表示。把这一点作为表示的*定义*是合理的。

**例 1.2.9** 当 $A$ 和 $B$ 是（预）序集时，相应范畴之间的函子恰好就是一个**保序映射**，即满足 $a\le a'\implies f(a)\le f(a')$ 的函数 $f:A\to B$。习题 1.2.22 要求你验证这一点。

有时，我们会遇到类似函子、但把箭头反向的操作：$\mathscr{A}$ 中的态射 $A\to A'$ 产生 $\mathscr{B}$ 中的态射 $F(A)\leftarrow F(A')$。这样的操作称为反变函子。

**定义 1.2.10** 令 $\mathscr{A}$ 和 $\mathscr{B}$ 为范畴。从 $\mathscr{A}$ 到 $\mathscr{B}$ 的一个**反变函子**是一个函子 $\mathscr{A}^{\mathrm{op}}\to\mathscr{B}$。

为避免混淆，我们写“从 $\mathscr{A}$ 到 $\mathscr{B}$ 的反变函子”，而不写“反变函子 $\mathscr{A}\to\mathscr{B}$”。

函子 $\mathscr{C}\to\mathscr{D}$ 与函子 $\mathscr{C}^{\mathrm{op}}\to\mathscr{D}^{\mathrm{op}}$ 一一对应，而且 $(\mathscr{A}^{\mathrm{op}})^{\mathrm{op}}=\mathscr{A}$，因此从 $\mathscr{A}$ 到 $\mathscr{B}$ 的反变函子也可以描述为一个函子 $\mathscr{A}\to\mathscr{B}^{\mathrm{op}}$。这两种描述选哪一种都无大碍，不过从长远看，定义 1.2.10 中的约定用起来更方便。

为了强调，普通函子 $\mathscr{A}\to\mathscr{B}$ 有时称为从 $\mathscr{A}$ 到 $\mathscr{B}$ 的**协变函子**。

**例 1.2.11** 通过考察一个空间上的函数，我们可以获得有关该空间的大量信息。这一原则在二十世纪和二十一世纪数学中的重要性，几乎怎么强调都不过分。

<span class="original-page-anchor" id="pdf-page-32" aria-hidden="true"></span>

例如，给定一个拓扑空间 $X$，令 $C(X)$ 为 $X$ 上连续实值函数构成的环。环运算是“逐点”定义的：例如，如果 $p_1,p_2:X\to\mathbb{R}$ 是连续映射，那么映射 $p_1+p_2:X\to\mathbb{R}$ 由

$$
(p_1+p_2)(x)=p_1(x)+p_2(x)
$$

定义（$x\in X$）。连续映射 $f:X\to Y$ 诱导一个环同态 $C(f):C(Y)\to C(X)$。具体地，对 $q\in C(Y)$，把 $(C(f))(q)$ 定义为复合映射

$$
X\xrightarrow{f}Y\xrightarrow{q}\mathbb{R}.
$$

注意，$C(f)$ 的方向与 $f$ 相反。检验一些公理之后（习题 1.2.26），我们便得出 $C$ 是从 $\mathbf{Top}$ 到 $\mathbf{Ring}$ 的反变函子。

虽然这个具体的例子在本书中不会起很大作用，但仍值得仔细考察。它说明了一个重要思想：一个结构的元素本身可以是映射（这里是一个以连续函数为元素的环）。$C$ 通过复合成为函子的方式也很重要。类似的构造将在后续章节中起关键作用。

对于某些类型的空间，从 $X$ 到 $C(X)$ 的过程不会丢失任何信息：有一种方法可以从环 $C(X)$ 重建空间 $X$。基于这一原因及相关原因，人们有时说“代数与几何对偶”。

**例 1.2.12** 令 $k$ 为一个域。对于 $k$ 上的任意两个向量空间 $V$ 和 $W$，都有一个向量空间

$$
\mathbf{Hom}(V,W)=\{\text{线性映射 }V\to W\}.
$$

这个向量空间的元素本身就是映射，而向量空间的运算（加法和标量乘法）与上一个例子一样，是逐点定义的。

现在固定一个向量空间 $W$。任意线性映射 $f:V\to V'$ 都诱导一个线性映射

$$
f^*:\mathbf{Hom}(V',W)\to\mathbf{Hom}(V,W),
$$

具体地，对 $q\in\mathbf{Hom}(V',W)$，把 $f^*(q)$ 定义为复合映射

$$
V\xrightarrow{f}V'\xrightarrow{q}W.
$$

这就定义了一个函子

$$
\mathbf{Hom}(-,W):\mathbf{Vect}_k^{\mathrm{op}}\to\mathbf{Vect}_k.
$$

<span class="original-page-anchor" id="pdf-page-33" aria-hidden="true"></span>

符号“$-$”是一个空位或占位符，可以往其中填入参数。因此，$\mathbf{Hom}(-,W)$ 在 $V$ 处的值是 $\mathbf{Hom}(V,W)$。有时我们用空白代替 $-$，如 $\mathbf{Hom}(\hspace{1em},W)$。

一个重要的特例是 $W$ 为 $k$，把它视为其自身上的一维向量空间。向量空间 $\mathbf{Hom}(V,k)$ 称为 $V$ 的**对偶**，记作 $V^*$。因此有一个反变函子

$$
(\hspace{0.5em})^*=\mathbf{Hom}(-,k):\mathbf{Vect}_k^{\mathrm{op}}\to\mathbf{Vect}_k
$$

把每个向量空间映到它的对偶。

**例 1.2.13** 对于每个 $n\in\mathbb{N}$，都有一个函子 $H^n:\mathbf{Top}^{\mathrm{op}}\to\mathbf{Ab}$，把一个空间对应到它的第 $n$ 个上同调群。

**例 1.2.14** 令 $G$ 为一个幺半群，将其视为单对象范畴 $\mathscr{G}$。函子 $\mathscr{G}^{\mathrm{op}}\to\mathbf{Set}$ 就是一个*右* $G$-集，理由与例 1.2.8 中的理由基本相同。

左作用对应协变函子，右作用对应反变函子，这是因为我们采用了一个基本的记号约定：函数 $f$ 在元素 $x$ 处的值写作 $f(x)$，而不写作 $(x)f$。

以 $\mathbf{Set}$ 为陪域的反变函子很重要，因此有一个专门的名称。

**定义 1.2.15** 令 $\mathscr{A}$ 为一个范畴。$\mathscr{A}$ 上的一个**预层**是一个函子 $\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}$。

这个名称来自下面的特例。令 $X$ 为一个拓扑空间。用 $\mathscr{O}(X)$ 表示 $X$ 的开子集按包含关系排序构成的偏序集。像例 1.1.8(e) 中那样，把 $\mathscr{O}(X)$ 视为一个范畴。因此，$\mathscr{O}(X)$ 的对象是 $X$ 的开子集；对于 $U,U'\in\mathscr{O}(X)$，若 $U\subseteq U'$，则有一个态射 $U\to U'$，否则没有态射。空间 $X$ 上的一个**预层**就是范畴 $\mathscr{O}(X)$ 上的一个预层。例如，给定任意空间 $X$，在 $X$ 上有一个预层 $F$，定义为

$$
F(U)=\{\text{连续函数 }U\to\mathbb{R}\}
$$

（$U\in\mathscr{O}(X)$）；每当 $U$ 和 $U'$ 是 $X$ 的开子集且 $U\subseteq U'$ 时，就把映射 $F(U')\to F(U)$ 取为限制映射。预层以及称为层的某一类预层，在现代几何中起着重要作用。

我们很清楚，对于*集合*之间的*函数*，考虑单射、满射和双射等特殊类型的函数，有时很有用。我们也知道，单射与子集的概念是相关的：例如，

<span class="original-page-anchor" id="pdf-page-34" aria-hidden="true"></span>

![充满性与忠实性](/library/volume-87/diagrams/pdf-0034-full-faithful.png)

图 1.1 充满性与忠实性。

只要 $B$ 是 $A$ 的子集，就有由包含关系给出的单射 $B\to A$。在本节和下一节，我们将为*范畴*之间的*函子*引入一些类似的概念，先从以下定义开始。

**定义 1.2.16** 函子 $F\colon\mathscr{A}\to\mathscr{B}$ 称为**忠实的**（分别称为**充满的**），如果对每个 $A,A'\in\mathscr{A}$，函数

$$
\begin{array}{ccc}
\mathscr{A}(A,A') & \to & \mathscr{B}(F(A),F(A'))\\
f & \mapsto & F(f)
\end{array}
$$

都是单射（分别为满射）。

**提醒 1.2.17** 注意定义中 $A$ 和 $A'$ 的作用。忠实性*并不是*说，如果 $f_1$ 和 $f_2$ 是 $\mathscr{A}$ 中不同的态射，那么 $F(f_1)\neq F(f_2)$（练习 1.2.27）。在图 1.1 的情形中，$F$ 忠实的意思是：对图中每一组 $A,A'$ 和 $g$，至多有一个虚线箭头被 $F$ 映为 $g$。$F$ 充满的意思是：对每一组这样的 $A,A'$ 和 $g$，至少有一个虚线箭头被 $F$ 映为 $g$。

**定义 1.2.18** 设 $\mathscr{A}$ 是一个范畴。$\mathscr{A}$ 的一个**子范畴** $\mathscr{S}$ 由 $\operatorname{ob}(\mathscr{A})$ 的一个子类 $\operatorname{ob}(\mathscr{S})$，以及对每个 $S,S'\in\operatorname{ob}(\mathscr{S})$ 给定的 $\mathscr{A}(S,S')$ 的一个子类 $\mathscr{S}(S,S')$ 组成，并且 $\mathscr{S}$ 对复合和恒等态射封闭。如果对所有 $S,S'\in\operatorname{ob}(\mathscr{S})$ 都有 $\mathscr{S}(S,S')=\mathscr{A}(S,S')$，则称它为**充满**子范畴。

因此，一个充满子范畴由选出的一些对象和它们之间的全部态射组成。只要说明选了哪些对象，就能确定这个充满子范畴。例如，$\mathbf{Ab}$ 是 $\mathbf{Grp}$ 中由所有阿贝尔群组成的充满子范畴。

只要 $\mathscr{S}$ 是范畴 $\mathscr{A}$ 的子范畴，就有一个包含函子 $I\colon\mathscr{S}\to\mathscr{A}$，由 $I(S)=S$ 和 $I(f)=f$ 定义。它自动是忠实的，而且它充满当且仅当 $\mathscr{S}$ 是充满子范畴。

**提醒 1.2.19** 函子的像未必是子范畴。例如，<span class="original-page-anchor" id="pdf-page-35" aria-hidden="true"></span>考虑函子

![像不是子范畴的函子](/library/volume-87/diagrams/pdf-0035-functor-image.png)

它由 $F(A)=X$、$F(B)=F(B')=Y$、$F(C)=Z$、$F(f)=p$ 和 $F(g)=q$ 定义。那么 $p$ 和 $q$ 都在 $F$ 的像中，但 $qp$ 不在。

### 练习

**1.2.20** 找出三个上文未提及的函子例子。

**1.2.21** 证明函子保持同构。也就是说，证明：如果 $F\colon\mathscr{A}\to\mathscr{B}$ 是一个函子，且 $A,A'\in\mathscr{A}$ 满足 $A\cong A'$，那么 $F(A)\cong F(A')$。

**1.2.22** 证明例 1.2.9 中的断言。换言之，给定有序集 $A$ 和 $B$，并用 $\mathscr{A}$ 和 $\mathscr{B}$ 表示对应的范畴，证明函子 $\mathscr{A}\to\mathscr{B}$ 就相当于一个保序映射 $A\to B$。

**1.2.23** 如果两个范畴 $\mathscr{A}$ 和 $\mathscr{B}$ 作为 $\mathbf{CAT}$ 的对象是同构的，则称它们**同构**，记作 $\mathscr{A}\cong\mathscr{B}$。

(a) 设 $G$ 是一个群，把它看作所有态射都是同构的单对象范畴。那么它的对偶范畴 $G^{\mathrm{op}}$ 也是一个所有态射都是同构的单对象范畴，因此也可以看作一个群。完全用群论的语言来说，$G^{\mathrm{op}}$ 是什么？证明 $G$ 与 $G^{\mathrm{op}}$ 同构。

(b) 找出一个与其对偶不同构的幺半群。

**1.2.24** 是否存在函子 $Z\colon\mathbf{Grp}\to\mathbf{Grp}$，使得对所有群 $G$，$Z(G)$ 都是 $G$ 的中心？

**1.2.25** 有时，函子的定义域是两个范畴的积 $\mathscr{A}\times\mathscr{B}$。本题要你证明，这样的函子可以看作两族相互配合的函子：一族定义在 $\mathscr{A}$ 上，另一族定义在 $\mathscr{B}$ 上。（这与双线性映射和线性映射的情形非常相似。）

(a) 设 $F\colon\mathscr{A}\times\mathscr{B}\to\mathscr{C}$ 是一个函子。证明对每个 $A\in\mathscr{A}$，都有一个函子 $F^A\colon\mathscr{B}\to\mathscr{C}$，它在对象 $B\in\mathscr{B}$ 上由 $F^A(B)=F(A,B)$ 定义，在 $\mathscr{B}$ 中的态射 $g$ 上由 $F^A(g)=F(1_A,g)$ 定义。证明对每个 $B\in\mathscr{B}$，都有类似定义的函子 $F_B\colon\mathscr{A}\to\mathscr{C}$。

<span class="original-page-anchor" id="pdf-page-36" aria-hidden="true"></span>

(b) 设 $F\colon\mathscr{A}\times\mathscr{B}\to\mathscr{C}$ 是一个函子。沿用 (a) 中的记号，证明两族函子 $(F^A)_{A\in\mathscr{A}}$ 和 $(F_B)_{B\in\mathscr{B}}$ 满足以下两个条件：

- 如果 $A\in\mathscr{A}$ 且 $B\in\mathscr{B}$，那么 $F^A(B)=F_B(A)$；
- 如果 $f\colon A\to A'$ 是 $\mathscr{A}$ 中的态射，$g\colon B\to B'$ 是 $\mathscr{B}$ 中的态射，那么 $F^{A'}(g)\circ F_B(f)=F_{B'}(f)\circ F^A(g)$。

(c) 现在取范畴 $\mathscr{A}$、$\mathscr{B}$ 和 $\mathscr{C}$，以及满足 (b) 中两个条件的两族函子 $(F^A)_{A\in\mathscr{A}}$ 和 $(F_B)_{B\in\mathscr{B}}$。证明存在唯一的函子 $F\colon\mathscr{A}\times\mathscr{B}\to\mathscr{C}$ 满足 (a) 中的等式。（“存在唯一的函子”特别意味着*存在*一个函子，所以除了唯一性，你还必须证明存在性。）

**1.2.26** 补全例 1.2.11 的细节，从而构造函子 $C\colon\mathbf{Top}^{\mathrm{op}}\to\mathbf{Ring}$。

**1.2.27** 找出一个函子 $F\colon\mathscr{A}\to\mathscr{B}$ 的例子，使得 $F$ 忠实，但 $\mathscr{A}$ 中存在不同的态射 $f_1$ 和 $f_2$，满足 $F(f_1)=F(f_2)$。

**1.2.28** (a) 本节出现的函子例子中，哪些是忠实的，哪些是充满的？

(b) 写出一个既充满又忠实的函子例子，一个充满但不忠实的函子例子，一个忠实但不充满的函子例子，以及一个两者都不是的函子例子。

**1.2.29** (a) 有序集的子范畴是什么？其中哪些是充满的？

(b) 群的子范畴是什么？（要小心！）其中哪些是充满的？

## 1.3 自然变换

我们已经认识了范畴，也认识了函子，即范畴之间的态射。更进一步，我们还可以谈论“函子之间的态射”，这或许有些出人意料。这样的态射称为自然变换。这个概念只适用于具有相同定义域和陪域的函子：

$$
\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}.
$$

先通过一个特殊情形，看看这个概念会是什么样。设 $\mathscr{A}$ 是对象为自然数 $0,1,2,\ldots$ 的离散范畴（例 1.1.8(b)）。从 $\mathscr{A}$ 到另一个范畴 $\mathscr{B}$ 的函子 $F$，就只是一个序列<span class="original-page-anchor" id="pdf-page-37" aria-hidden="true"></span>$(F_0,F_1,F_2,\ldots)$，其中各项都是 $\mathscr{B}$ 的对象。设 $G$ 是另一个从 $\mathscr{A}$ 到 $\mathscr{B}$ 的函子，由 $\mathscr{B}$ 的对象构成的另一个序列 $(G_0,G_1,G_2,\ldots)$ 组成。把从 $F$ 到 $G$ 的“态射”定义为 $\mathscr{B}$ 中的一列态射

$$
\Bigl(F_0\xrightarrow{\alpha_0}G_0,\ F_1\xrightarrow{\alpha_1}G_1,\ F_2\xrightarrow{\alpha_2}G_2,\ \ldots\Bigr)
$$

是合理的。

**译校注：** 原文第三项印为 $F_1\xrightarrow{\alpha_2}G_2$，官方 TeX 源码也如此；结合各项的下标及下方图示，其源对象应为 $F_2$。英文校录保留原文，译文在此改为 $F_2$。

这一情形可以描绘如下：

![从离散范畴出发的自然变换的分量](/library/volume-87/diagrams/pdf-0037-discrete-components.png)

（右边的图不应按过于字面的方式理解。某些对象 $F_i$ 或 $G_i$ 可能相等，而且除了图中所示的部分，$\mathscr{B}$ 中还可能有许多其他东西。）

由此看来，在一般情形下，函子 $\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}$ 之间的自然变换应当由态射 $\alpha_A\colon F(A)\to G(A)$ 组成，对每个 $A\in\mathscr{A}$ 都有一个。上面的例子有一个特殊之处：范畴 $\mathscr{A}$ 不含任何非平凡态射。在一般情形下，我们还要求 $\mathscr{A}$ 中的态射与态射 $\alpha_A$ 之间具有某种相容性。

**定义 1.3.1** 设 $\mathscr{A}$ 和 $\mathscr{B}$ 是范畴，$\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}$ 是函子。一个**自然变换** $\alpha\colon F\to G$ 是 $\mathscr{B}$ 中的一族态射 $\bigl(F(A)\xrightarrow{\alpha_A}G(A)\bigr)_{A\in\mathscr{A}}$，使得对 $\mathscr{A}$ 中每个态射 $A\xrightarrow{f}A'$，正方形

![自然性正方形 (1.3)](/library/volume-87/diagrams/pdf-0037-naturality-square.png)

都是交换的。态射 $\alpha_A$ 称为 $\alpha$ 的**分量**。

**注记 1.3.2** (a) 自然变换的定义保证：从 $\mathscr{A}$ 中每个态射 $A\xrightarrow{f}A'$ 出发，恰好能够在 $\mathscr{B}$ 中构造出一个态射 $F(A)\to G(A')$。当 $f=1_A$ 时，这个态射就是 $\alpha_A$。对一般的 $f$，它是正方形 (1.3) 的对角线，而“恰好一个”意味着这个正方形交换。

<span class="original-page-anchor" id="pdf-page-38" aria-hidden="true"></span>

(b) 我们写

![自然变换的记号](/library/volume-87/diagrams/pdf-0038-two-cell.png)

来表示 $\alpha$ 是从 $F$ 到 $G$ 的自然变换。

**例 1.3.3** 设 $\mathscr{A}$ 是一个离散范畴，$F,G\colon\mathscr{A}\to\mathscr{B}$ 是函子。那么 $F$ 和 $G$ 就只是 $\mathscr{B}$ 的两族对象 $(F(A))_{A\in\mathscr{A}}$ 和 $(G(A))_{A\in\mathscr{A}}$。自然变换 $\alpha\colon F\to G$ 就只是 $\mathscr{B}$ 中的一族态射 $\bigl(F(A)\xrightarrow{\alpha_A}G(A)\bigr)_{A\in\mathscr{A}}$，正如上面在 $\operatorname{ob}\mathscr{A}=\mathbb{N}$ 的情形中所说的。原则上，这族态射必须对 $\mathscr{A}$ 中每个态射 $f$ 都满足自然性公理 (1.3)；但 $\mathscr{A}$ 中的态射只有恒等态射，而当 $f$ 是恒等态射时，这条公理自动成立。

**例 1.3.4** 回顾例 1.1.8，一个群（更一般地，一个幺半群）$G$ 可以看作单对象范畴。例 1.2.8 还告诉我们，从范畴 $G$ 到 $\mathbf{Set}$ 的函子无非就是一个左 $G$-集。（此前我们用 $\mathscr{G}$ 表示与群 $G$ 对应的范畴；从现在起，我们用 $G$ 同时表示两者。）取两个 $G$-集 $S$ 和 $T$。由于 $S$ 和 $T$ 可以看作函子 $G\to\mathbf{Set}$，我们可以问：自然变换

![G-集之间的自然变换](/library/volume-87/diagrams/pdf-0038-g-equivariant.png)

具体是什么？

这样的自然变换由 $\mathbf{Set}$ 中一个满足某些公理的态射组成（因为 $G$ 只有一个对象）。确切地说，它是一个函数 $\alpha\colon S\to T$，使得对所有 $s\in S$ 和 $g\in G$，都有 $\alpha(g\cdot s)=g\cdot\alpha(s)$。（为什么？）换言之，它就是一个 $G$-集的映射，有时称为 **$G$-等变**映射。

**例 1.3.5** 固定一个自然数 $n$。在这个例子中，我们将看到如何把“$n\times n$ 矩阵的行列式”理解为一个自然变换。

对任意交换环 $R$，元素取自 $R$ 的 $n\times n$ 矩阵在乘法下构成一个幺半群 $M_n(R)$。此外，任意环同态 $R\to S$ 都诱导一个幺半群同态 $M_n(R)\to M_n(S)$。这定义了一个从交换环范畴到幺半群范畴的函子 $M_n\colon\mathbf{CRing}\to\mathbf{Mon}$。

任意环 $R$ 的元素在乘法下也构成一个幺半群 $U(R)$，从而给出另一个函子 $U\colon\mathbf{CRing}\to\mathbf{Mon}$。

<span class="original-page-anchor" id="pdf-page-39" aria-hidden="true"></span>

现在，交换环 $R$ 上每个 $n\times n$ 矩阵 $X$ 都有一个行列式 $\det_R(X)$，它是 $R$ 的一个元素。行列式的熟知性质——

$$
\det_R(XY)=\det_R(X)\det_R(Y),\qquad \det_R(I)=1
$$

——告诉我们，对每个 $R$，函数 $\det_R\colon M_n(R)\to U(R)$ 都是一个幺半群同态。因此，我们得到一族态射

$$
\Bigl(M_n(R)\xrightarrow{\det_R}U(R)\Bigr)_{R\in\mathbf{CRing}},
$$

于是可以问，它们是否定义了一个自然变换

![作为自然变换的行列式](/library/volume-87/diagrams/pdf-0039-determinant.png)

答案确实是肯定的。自然性正方形交换（请核实！），反映的是行列式在所有环上都以相同方式定义。我们不会对一个环使用一种行列式定义，而对另一个环使用另一种定义。一般来说，自然性公理 (1.3) 要表达的是：这族态射 $(\alpha_A)_{A\in\mathscr{A}}$ 对所有 $A\in\mathscr{A}$ 都以统一的方式定义。

**构造 1.3.6** 自然变换是一种态射，我们自然会希望能够将它们复合。确实可以。给定自然变换

![两个可复合的自然变换](/library/volume-87/diagrams/pdf-0039-vertical-composition.png)

就有一个复合自然变换

![复合自然变换](/library/volume-87/diagrams/pdf-0039-composite.png)

它对所有 $A\in\mathscr{A}$ 都由 $(\beta\circ\alpha)_A=\beta_A\circ\alpha_A$ 定义。任意函子 $F$ 上还有一个恒等自然变换

![恒等自然变换](/library/volume-87/diagrams/pdf-0039-identity.png)

它由 $(1_F)_A=1_{F(A)}$ 定义。因此，对任意两个范畴 $\mathscr{A}$ 和 $\mathscr{B}$，都有一个范畴，其对象是从 $\mathscr{A}$ 到 $\mathscr{B}$ 的函子，其态射是这些函子之间的自然变换。它称为从 $\mathscr{A}$ 到 $\mathscr{B}$ 的**函子范畴**，记作 $[\mathscr{A},\mathscr{B}]$ 或 $\mathscr{B}^{\mathscr{A}}$。

<span class="original-page-anchor" id="pdf-page-40" aria-hidden="true"></span>

**例 1.3.7** 设 $2$ 是有两个对象的离散范畴。从 $2$ 到范畴 $\mathscr{B}$ 的函子就是 $\mathscr{B}$ 的一对对象，而自然变换就是一对态射。因此，函子范畴 $[2,\mathscr{B}]$ 与积范畴 $\mathscr{B}\times\mathscr{B}$ 同构（构造 1.1.11）。这与函子范畴的另一种记号 $\mathscr{B}^2$ 非常吻合。

**例 1.3.8** 设 $G$ 是一个幺半群。那么 $[G,\mathbf{Set}]$ 是左 $G$-集范畴，而 $[G^{\mathrm{op}},\mathbf{Set}]$ 是右 $G$-集范畴（例 1.2.14）。

**例 1.3.9** 取有序集 $A$ 和 $B$，并把它们看作范畴（如例 1.1.8(e) 中所述）。给定保序映射 $A\overset{f}{\underset{g}{\rightrightarrows}}B$，并把它们看作函子（如例 1.2.9 中所述），至多存在一个自然变换

![保序映射之间的自然变换](/library/volume-87/diagrams/pdf-0040-ordered-sets.png)

而且这样的自然变换存在，当且仅当对所有 $a\in A$ 都有 $f(a)\leq g(a)$。（自然性公理 (1.3) 自动成立，因为在有序集中，所有图都交换。）所以 $[A,B]$ 也是有序集；它的元素是从 $A$ 到 $B$ 的保序映射，并且 $f\leq g$ 当且仅当对所有 $a\in A$ 都有 $f(a)\leq g(a)$。

“那个 $6$ 阶循环群”和“两个空间的积”等日常说法，反映出这样一个事实：给定一个范畴中两个同构的对象，我们通常既不知道也不在意它们实际上是否相等。这一点极其重要。

特别地，当所讨论的范畴是函子范畴时，这个道理仍然适用。换言之，给定两个函子 $F,G\colon\mathscr{A}\to\mathscr{B}$，我们通常不在意它们是否在字面意义上相等。（如果相等，那么对所有 $A\in\mathscr{A}$，$\mathscr{B}$ 的对象 $F(A)$ 和 $G(A)$ 就都相等。但我们刚刚已经说过，并不关心这么细的区别。）真正要紧的是它们是否自然同构。

**定义 1.3.10** 设 $\mathscr{A}$ 和 $\mathscr{B}$ 是范畴。从 $\mathscr{A}$ 到 $\mathscr{B}$ 的函子之间的**自然同构**，就是 $[\mathscr{A},\mathscr{B}]$ 中的同构。

这个定义的一个等价形式常常很有用：

**引理 1.3.11** 设

![从 F 到 G 的自然变换 alpha](/library/volume-87/diagrams/pdf-0040-isomorphism-components.png)

是一个自然变换。那么 $\alpha$ 是自然同构，当且仅当对所有 $A\in\mathscr{A}$，$\alpha_A\colon F(A)\to G(A)$ 都是同构。

<span class="original-page-anchor" id="pdf-page-41" aria-hidden="true"></span>

**证明** 见练习 1.3.26。$\square$

当然，如果存在从 $F$ 到 $G$ 的自然同构，我们就说函子 $F$ 和 $G$ **自然同构**。由于自然同构就是某个特定范畴（即 $[\mathscr{A},\mathscr{B}]$）中的同构，我们已经有表示它的记号：$F\cong G$。

**定义 1.3.12** 给定函子 $\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}$，如果 $F$ 和 $G$ 自然同构，我们就说

$$
F(A)\cong G(A)\text{ \textbf{关于} }A\text{ \textbf{自然成立} }.
$$

这种说法可以这样理解：如果 $F(A)\cong G(A)$ 关于 $A$ 自然成立，那么对每个单独的 $A$ 当然都有 $F(A)\cong G(A)$。但它说的还不止这些：我们能够选择同构 $\alpha_A\colon F(A)\to G(A)$，使自然性公理 (1.3) 成立。

**例 1.3.13** 设 $F,G\colon\mathscr{A}\to\mathscr{B}$ 是从离散范畴 $\mathscr{A}$ 到范畴 $\mathscr{B}$ 的函子。那么 $F\cong G$ 当且仅当对所有 $A\in\mathscr{A}$ 都有 $F(A)\cong G(A)$。

所以在*这个*情形下，$F(A)\cong G(A)$ 关于 $A$ 自然成立，当且仅当对所有 $A$ 都有 $F(A)\cong G(A)$。但这只是因为 $\mathscr{A}$ 是离散的。在一般情形下，这个说法完全错误。存在许多范畴及函子 $\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}$ 的例子，使得对所有 $A\in\mathscr{A}$ 都有 $F(A)\cong G(A)$，却并不关于 $A$ *自然成立*。练习 1.3.31 给出了一个来自组合数学的例子。

**例 1.3.14** 设 $\mathbf{FDVect}$ 是某个域 $k$ 上的有限维向量空间范畴。对偶向量空间的构造定义了一个从 $\mathbf{FDVect}$ 到自身的反变函子（例 1.2.12），因此双重对偶的构造定义了一个从 $\mathbf{FDVect}$ 到自身的协变函子。

此外，对每个 $V\in\mathbf{FDVect}$，我们都有一个典范同构 $\alpha_V\colon V\to V^{**}$。给定 $v\in V$，$V^{**}$ 的元素 $\alpha_V(v)$ 是“在 $v$ 处求值”；也就是说，$\alpha_V(v)\colon V^*\to k$ 把 $\phi\in V^*$ 映为 $\phi(v)\in k$。$\alpha_V$ 是同构，这是有限维向量空间理论中的一个标准结果。

这定义了一个自然变换

![到双重对偶的自然映射](/library/volume-87/diagrams/pdf-0041-double-dual.png)

它从恒等函子到双重对偶函子。由引理 1.3.11，$\alpha$ 是<span class="original-page-anchor" id="pdf-page-42" aria-hidden="true"></span>一个自然同构。因此 $1_{\mathbf{FDVect}} \cong (\ )^{**}$。等价地，用定义 1.3.12 的语言来说，$V \cong V^{**}$ 关于 $V$ 是自然的。

这是范畴论把直觉变得精确的一个例子。即使还没学过范畴论，你也能凭直觉看出：有限维向量空间与其双重对偶之间的同构是“自然的”或“典范的”，因为定义它不需要作任何任意选择。相反，要给出 $V$ 与其对偶空间 $V^*$ 之间的一个同构，我们需要任意选取一组基，而且这个同构确实依赖于所选的基。

在向量空间的例子中，我们使用了“**典范**”这个词。这是一个非正式的说法，大意是“天赋的”或“无需作任意选择就能定义的”。例如，对任意两个集合 $A$ 和 $B$，都有一个由 $(a,b) \mapsto (b,a)$ 定义的典范双射 $A \times B \to B \times A$，也有一个由 $(a,b) \mapsto a$ 定义的典范函数 $A \times B \to A$。但是，以“选取一个元素 $a_0 \in A$，并把所有元素都映到 $a_0$”来定义的函数 $B \to A$ 就不是典范的，因为对 $a_0$ 的选择是任意的。

自然同构的概念不可避免地引出另一个核心概念：范畴的等价。

一个集合的两个元素，要么相等，要么不相等。一个范畴的两个对象，可以相等，可以不相等但同构，也可以连同构都不是。正如定义 1.3.10 之前所解释的，要求范畴中的两个对象相等，过于严格；我们通常关心的是它们是否同构。因此：

- 对集合中的两个元素来说，“相同”应当理解为相等；
- 对范畴中的两个对象来说，“相同”应当理解为同构。

把第二点应用于函子范畴 $[\mathscr{A},\mathscr{B}]$，它告诉我们：

- 对两个函子 $\mathscr{A} \rightrightarrows \mathscr{B}$ 来说，“相同”应当理解为自然同构。

但是，两个*范畴*“相同”，又应当怎样理解？把同构作为标准过于严格，因为若 $\mathscr{A} \cong \mathscr{B}$，则存在函子

![方向相反的函子 F 和 G，式 (1.4)。](/library/volume-87/diagrams/pdf-0042-equivalence-functors.png)

使得

$$
G \circ F = 1_{\mathscr{A}} \qquad \text{且} \qquad F \circ G = 1_{\mathscr{B}}, \tag{1.5}
$$

而我们刚刚已经看到，要求函子彼此相等，也过于严格。

对范畴来说，最有用的“相同”概念称为“等价”，它<span class="original-page-anchor" id="pdf-page-43" aria-hidden="true"></span>比同构更宽松。要给出它的定义，只需把式 (1.5) 中过于严格的相等替换为同构。这样得到

$$
G \circ F \cong 1_{\mathscr{A}} \qquad \text{且} \qquad F \circ G \cong 1_{\mathscr{B}}.
$$

**定义 1.3.15** 范畴 $\mathscr{A}$ 与 $\mathscr{B}$ 之间的一个**等价**由式 (1.4) 中的一对函子，以及自然同构

$$
\eta\colon 1_{\mathscr{A}} \to G \circ F, \qquad \varepsilon\colon F \circ G \to 1_{\mathscr{B}}
$$

组成。如果 $\mathscr{A}$ 与 $\mathscr{B}$ 之间存在一个等价，我们就称 $\mathscr{A}$ 与 $\mathscr{B}$ **等价**，记作 $\mathscr{A} \simeq \mathscr{B}$。我们也称函子 $F$ 和 $G$ 为**等价**。

$\eta$ 和 $\varepsilon$ 的方向并不十分重要，因为它们本来就是同构。等到讨论伴随关系时（第 2.2 节），我们就会明白为什么选择这样的方向。

**注意 1.3.16** 符号 $\cong$ 用来表示范畴中对象的同构，特别地，也用来表示范畴的同构（范畴是 $\mathbf{CAT}$ 的对象）。符号 $\simeq$ 用来表示范畴的等价。至少，本书和大多数范畴论学者采用这个约定，尽管整个数学界并不普遍采用它。

哪些函子是等价，还可以用另一种非常有用的方式来刻画。首先，我们需要一个定义。

**定义 1.3.17** 如果对所有 $B \in \mathscr{B}$，都存在 $A \in \mathscr{A}$ 使得 $F(A) \cong B$，则称函子 $F\colon \mathscr{A} \to \mathscr{B}$ **在对象上本质满射**。

**命题 1.3.18** *一个函子是等价，当且仅当它充满、忠实并且在对象上本质满射。*

**证明** 习题 1.3.32。$\square$

这个结果可以与以下定理作比较：每个双射群同态都是同构（即它的逆也是同态）；或者，每个分量都是同构的自然变换，本身也是同构（引理 1.3.11）。这两个结果的用处在于：不用直接构造逆，就能证明一个态射是同构。命题 1.3.18 有类似的作用：不用实际构造一个“逆” $G$，甚至不用构造 $\eta$ 或 $\varepsilon$（采用定义 1.3.15 中的记号），就能证明函子 $F$ 是等价。

命题 1.3.18 的一个推论让我们看到，充满且忠实的函子本质上可以看作充满子范畴的包含函子：

<span class="original-page-anchor" id="pdf-page-44" aria-hidden="true"></span>

**推论 1.3.19** *设 $F\colon \mathscr{C} \to \mathscr{D}$ 是一个充满且忠实的函子。则 $\mathscr{C}$ 等价于 $\mathscr{D}$ 的充满子范畴 $\mathscr{C}'$，其对象是那些具有 $F(C)$ 形式的对象，其中 $C \in \mathscr{C}$。*

**证明** 由 $F'(C) = F(C)$ 定义的函子 $F'\colon \mathscr{C} \to \mathscr{C}'$ 是充满且忠实的（因为 $F$ 具有这两个性质），并且在对象上本质满射（由 $\mathscr{C}'$ 的定义）。$\square$

无论把“具有 $F(C)$ 形式”理解为“等于 $F(C)$”还是“同构于 $F(C)$”，这个结果都成立，证明也相同。

**例 1.3.20** 设 $\mathscr{A}$ 是任意范畴，$\mathscr{B}$ 是任意充满子范畴，并且包含 $\mathscr{A}$ 每个同构类中的至少一个对象。那么包含函子 $\mathscr{B} \hookrightarrow \mathscr{A}$ 是忠实的（与任何子范畴的包含函子一样）、充满的，并且在对象上本质满射。因此 $\mathscr{B} \simeq \mathscr{A}$。

所以，如果我们从一个范畴的每个同构类中删去一些（但并非全部）对象，得到的精简版本就与原来的范畴等价。反过来，如果我们向一个范畴中加入一些对象，且每个新增对象都与某个已有对象同构，那么也不会造成区别：新的、更大的范畴与旧的范畴等价。

例如，设 $\mathbf{FinSet}$ 是有限集合及其间函数构成的范畴。对每个自然数 $n$，选取一个含有 $n$ 个元素的集合 $\mathbf{n}$，并设 $\mathscr{B}$ 是 $\mathbf{FinSet}$ 中以 $\mathbf{0},\mathbf{1},\ldots$ 为对象的充满子范畴。那么 $\mathscr{B} \simeq \mathbf{FinSet}$，尽管在某种意义上，$\mathscr{B}$ 比 $\mathbf{FinSet}$ 小得多。

**例 1.3.21** 在例 1.1.8(d) 中，我们看到幺半群与单对象范畴本质上是同一回事。现在有了等价的定义，我们差不多已经能精确地表述这一点了。不过，还需要一些集合论语言；等掌握这些语言后，我们会再回到这个结果（例 3.2.11）。但其中的核心意思，现在就可以说明。

设 $\mathscr{C}$ 是 $\mathbf{CAT}$ 中以单对象范畴为对象的充满子范畴。设 $\mathbf{Mon}$ 是幺半群的范畴。那么 $\mathscr{C} \simeq \mathbf{Mon}$。为说明这一点，首先注意：给定任意范畴中的任意对象 $A$，态射 $A \to A$ 在复合运算下构成一个幺半群（至少，在满足某些集合论限制的前提下）。因此，存在一个典范函子 $F\colon \mathscr{C} \to \mathbf{Mon}$，它把一个单对象范畴映到该唯一对象到自身的态射所构成的幺半群。这个函子 $F$ 是充满且忠实的（由例 1.2.7），并且在对象上本质满射。因此 $F$ 是一个等价。

**例 1.3.22** 形如 $\mathscr{A}^{\mathrm{op}} \simeq \mathscr{B}$ 的等价，有时称为 $\mathscr{A}$ 与 $\mathscr{B}$ 之间的一个**对偶**。我们称 $\mathscr{A}$ 与 $\mathscr{B}$ **对偶**。有许多著名的对偶，其中 $\mathscr{A}$ 是代数的范畴，$\mathscr{B}$ 是空间的范畴；回想例 1.2.11 中“代数与几何对偶”的说法。

<span class="original-page-anchor" id="pdf-page-45" aria-hidden="true"></span>

下面是一些相当高深的例子，远远超出本书的范围。

- Stone 对偶：布尔代数的范畴与完全不连通的紧 Hausdorff 空间的范畴对偶。
- Gelfand–Naimark 对偶：交换含幺 $C^*$ 代数的范畴与紧 Hausdorff 空间的范畴对偶。（$C^*$ 代数是在泛函分析中十分重要的一类代数结构。）
- 代数几何学家有几种“空间”的概念，其中一种是“仿射簇”。设 $k$ 是一个代数闭域。那么 $k$ 上仿射簇的范畴与没有非平凡幂零元的有限生成 $k$ 代数的范畴对偶。
- Pontryagin 对偶：局部紧阿贝尔拓扑群的范畴与自身对偶。正如“拓扑群”一词所暗示的，对偶的两边都兼有代数和几何性质。Pontryagin 对偶是对 Fourier 变换性质的抽象。

**例 1.3.23** 如果一个范畴的对象带有某种结构，态射却不保持这种结构，那么考虑这样的范畴通常没什么用处。例如，设 $\mathscr{A}$ 的对象是群，而态射是群之间的*所有*函数，不一定是同态。设 $\mathbf{Set}_{\neq\emptyset}$ 是非空集合的范畴。遗忘函子 $U\colon \mathscr{A} \to \mathbf{Set}_{\neq\emptyset}$ 是充满且忠实的。有一个并不深刻的事实：每个非空集合都可以赋予至少一种群结构。因此 $U$ 在对象上本质满射。于是 $U$ 是一个等价。这意味着，尽管范畴 $\mathscr{A}$ 是用群来定义的，它实际上就是非空集合的范畴。

**评注 1.3.24** 这里回顾一下本章到目前为止讲过的内容。我们已经定义了：

- 范畴（第 1.1 节）；
- 范畴之间的函子（第 1.2 节）；
- 函子之间的自然变换（第 1.3 节）；
- 函子的复合

  $$
  \cdot \to \cdot \to \cdot
  $$

  以及任意范畴上的恒等函子（评注 1.2.2(b)）；
- 自然变换的复合

  ![自然变换的垂直复合。](/library/volume-87/diagrams/pdf-0045-vertical-composition.png)

  以及任意函子上的恒等自然变换（构造 1.3.6）。

<span class="original-page-anchor" id="pdf-page-46" aria-hidden="true"></span>

这种自然变换的复合有时称为**垂直复合**。此外还有**水平复合**，它从自然变换

![两对函子之间的自然变换 α 和 α′。](/library/volume-87/diagrams/pdf-0046-horizontal-input.png)

产生一个自然变换

![复合函子之间所产生的自然变换。](/library/volume-87/diagrams/pdf-0046-horizontal-output.png)

按惯例记作 $\alpha' * \alpha$。$\alpha' * \alpha$ 在 $A \in \mathscr{A}$ 处的分量定义为自然性方块

![定义水平复合的自然性方块。](/library/volume-87/diagrams/pdf-0046-naturality-square.png)

的对角线。换句话说，$(\alpha' * \alpha)_A$ 可以定义为 $\alpha'_{G(A)} \circ F'(\alpha_A)$，也可以定义为 $G'(\alpha_A) \circ \alpha'_{F(A)}$；无论选哪一个都一样，因为这两个复合相等。

在水平复合中，$\alpha$ 或 $\alpha'$ 是恒等自然变换时的特殊情形尤其重要，也有专门的记号。于是，

![一个函子后接一个自然变换。](/library/volume-87/diagrams/pdf-0046-whisker-right-input.png)

产生

![复合函子之间的自然变换 α′F。](/library/volume-87/diagrams/pdf-0046-whisker-right-output.png)

其中 $(\alpha' F)_A = \alpha'_{F(A)}$；而

![一个自然变换后接一个函子。](/library/volume-87/diagrams/pdf-0046-whisker-left-input.png)

产生

![复合函子之间的自然变换 F′α。](/library/volume-87/diagrams/pdf-0046-whisker-left-output.png)

其中 $(F'\alpha)_A = F'(\alpha_A)$。

<span class="original-page-anchor" id="pdf-page-47" aria-hidden="true"></span>

垂直复合与水平复合之间有良好的相容性：自然变换

![交换律中的自然变换。](/library/volume-87/diagrams/pdf-0047-interchange.png)

满足**交换律**，

$$
(\beta' \circ \alpha') * (\beta \circ \alpha) = (\beta' * \beta) \circ (\alpha' * \alpha)\colon F' \circ F \to H' \circ H.
$$

像往常一样，讨论复合时也要相应地讨论恒等态射：同样有 $1_{F'} * 1_F = 1_{F' \circ F}$。

利用这些性质，对任意范畴 $\mathscr{A}$、$\mathscr{A}'$ 和 $\mathscr{A}''$，我们都能构造一个函子

$$
[\mathscr{A}',\mathscr{A}''] \times [\mathscr{A},\mathscr{A}'] \to [\mathscr{A},\mathscr{A}''],
$$

它在对象上由 $(F',F) \mapsto F' \circ F$ 给出，在态射上由 $(\alpha',\alpha) \mapsto \alpha' * \alpha$ 给出。特别地，如果 $F' \cong G'$ 且 $F \cong G$，那么 $F' \circ F \cong G' \circ G$，因为函子保持同构（习题 1.2.21）。

（这个函子的存在，与下面的事实很相似：在范畴 $\mathscr{C}$ *内部*，对任意对象 $A$、$A'$ 和 $A''$，都有一个*函数*

$$
\mathscr{C}(A',A'') \times \mathscr{C}(A,A') \to \mathscr{C}(A,A''),
$$

由 $(f',f) \mapsto f' \circ f$ 给出。）

上面的图中不仅有对象（0 维）和箭头 $\to$（1 维），还有双箭头 $\Rightarrow$，它们在箭头之间扫出二维区域。我们实际上已经在运用所谓的 2-范畴论。范畴、函子和自然变换构成一个 2-范畴，我们刚才一直在描述它的构造。要认真研究范畴，就得认真研究 2-范畴；要认真研究 2-范畴，就得认真研究 3-范畴……不知不觉间，我们就开始研究 $\infty$-范畴了。但在本书中，我们最多只登上这架无限阶梯的第一或第二级。

### 习题

**1.3.25** 找出三个上文没有提到的自然变换的例子。

**1.3.26** 证明引理 1.3.11。

<span class="original-page-anchor" id="pdf-page-48" aria-hidden="true"></span>

**1.3.27** 设 $\mathscr{A}$ 和 $\mathscr{B}$ 是范畴。证明 $[\mathscr{A}^{\mathrm{op}},\mathscr{B}^{\mathrm{op}}] \cong [\mathscr{A},\mathscr{B}]^{\mathrm{op}}$。

**1.3.28** 设 $A$ 和 $B$ 是集合，用 $B^A$ 表示从 $A$ 到 $B$ 的函数所构成的集合。写出：

(a) 一个典范函数 $A \times B^A \to B$；

(b) 一个典范函数 $A \to B^{(B^A)}$。

（虽然原则上可能有许多这样的典范函数，但在这两种情形中都只有一个。）

**1.3.29** 这里考虑的是定义域为积范畴 $\mathscr{A} \times \mathscr{B}$ 的函子之间的自然变换。你的任务是证明：同时关于两个变量的自然性，等价于分别关于每个变量的自然性。

取函子 $F,G\colon \mathscr{A} \times \mathscr{B} \to \mathscr{C}$。对每个 $A \in \mathscr{A}$，都有函子 $F^A,G^A\colon \mathscr{B} \to \mathscr{C}$，如习题 1.2.25 所述。类似地，对每个 $B \in \mathscr{B}$，都有函子 $F_B,G_B\colon \mathscr{A} \to \mathscr{C}$。

设 $\bigl(\alpha_{A,B}\colon F(A,B) \to G(A,B)\bigr)_{A\in\mathscr{A},B\in\mathscr{B}}$ 是一族态射。证明：这一族态射是一个自然变换 $F \to G$，当且仅当它满足以下两个条件：

- 对每个 $A \in \mathscr{A}$，族 $\bigl(\alpha_{A,B}\colon F^A(B) \to G^A(B)\bigr)_{B\in\mathscr{B}}$ 是一个自然变换 $F^A \to G^A$；
- 对每个 $B \in \mathscr{B}$，族 $\bigl(\alpha_{A,B}\colon F_B(A) \to G_B(A)\bigr)_{A\in\mathscr{A}}$ 是一个自然变换 $F_B \to G_B$。

**1.3.30** 设 $G$ 是一个群。对每个 $g \in G$，都有唯一的同态 $\phi\colon \mathbb{Z} \to G$ 满足 $\phi(1) = g$。因此，$G$ 的元素与同态 $\mathbb{Z} \to G$ 本质上是同一回事。当把群视为单对象范畴时，同态 $\mathbb{Z} \to G$ 又与函子 $\mathbb{Z} \to G$ 相同。自然同构在函子 $\mathbb{Z} \to G$ 的集合上定义了一个等价关系，因而也在 $G$ 本身上定义了一个等价关系。若只用群论语言来描述，这是什么等价关系？

（先猜一猜。对于一般的群 $G$，你能想到 $G$ 上哪些等价关系？）

**1.3.31** 集合 $X$ 的一个**置换**是一个双射 $X \to X$。用 $\mathbf{Sym}(X)$ 表示 $X$ 的置换所构成的集合。集合 $X$ 上的一个**全序**是一个序 $\leq$，使得对所有 $x,y \in X$，都有 $x \leq y$ 或 $y \leq x$；所以，给有限集合一个全序，就相当于把它的元素按顺序排好。用 $\mathbf{Ord}(X)$ 表示 $X$ 上全序所构成的集合。

用 $\mathscr{B}$ 表示有限集合与双射所构成的范畴。

<span class="original-page-anchor" id="pdf-page-49" aria-hidden="true"></span>

(a) 定义 $\mathbf{Sym}$ 在 $\mathscr{B}$ 的态射上的作用，使得 $\mathbf{Sym}$ 成为一个函子 $\mathscr{B} \to \mathbf{Set}$。对 $\mathbf{Ord}$ 也做同样的事。你的两个定义都应当是典范的（不作任意选择）。

(b) 证明不存在自然变换 $\mathbf{Sym} \to \mathbf{Ord}$。（提示：考虑恒等置换。）

(c) 对于一个含有 $n$ 个元素的集合 $X$，集合 $\mathbf{Sym}(X)$ 和 $\mathbf{Ord}(X)$ 各有多少个元素？

由此得出，对所有 $X \in \mathscr{B}$ 都有 $\mathbf{Sym}(X) \cong \mathbf{Ord}(X)$，但这个同构并不关于 $X \in \mathscr{B}$ *自然*。（这说明，对每个有限集合 $X$，$X$ 的置换与 $X$ 上的全序数目恰好相等，但是没有自然的方法把它们一一配对。）

**1.3.32** 本题要求你证明命题 1.3.18。设 $F\colon \mathscr{A} \to \mathscr{B}$ 是一个函子。

(a) 假设 $F$ 是一个等价。证明 $F$ 充满、忠实并且在对象上本质满射。（提示：先证明忠实，再证明充满。）

(b) 现在换一个假设：$F$ 充满、忠实并且在对象上本质满射。对每个 $B \in \mathscr{B}$，选取 $\mathscr{A}$ 的一个对象 $G(B)$ 以及一个同构 $\varepsilon_B\colon F(G(B)) \to B$。证明 $G$ 可以扩张为一个函子，使得 $(\varepsilon_B)_{B\in\mathscr{B}}$ 是一个自然同构 $FG \to 1_{\mathscr{B}}$。然后构造一个自然同构 $1_{\mathscr{A}} \to GF$，从而证明 $F$ 是等价。

**1.3.33** 本题把下面的想法说得更精确：做线性代数，用矩阵和用线性映射是等价的。

固定一个域 $k$。设 $\mathbf{Mat}$ 是以自然数为对象的范畴，并且

$$
\mathbf{Mat}(m,n) = \{k\text{ 上的 }n \times m\text{ 矩阵}\}.
$$

证明 $\mathbf{Mat}$ 等价于 $\mathbf{FDVect}$，即 $k$ 上有限维向量空间的范畴。你给出的等价，用到的是从 $\mathbf{Mat}$ 到 $\mathbf{FDVect}$ 的*典范*函子，还是从 $\mathbf{FDVect}$ 到 $\mathbf{Mat}$ 的典范函子？

（本题还需要你弄清楚范畴 $\mathbf{Mat}$ 中的复合应当是什么；只有一种合理的选择。命题 1.3.18 能使本题更容易。）

**1.3.34** 证明范畴的等价是一个等价关系。（并没有看上去那么显然。）
