---
title: "第六章 伴随函子、可表函子与极限"
description: "Tom Leinster《Basic Category Theory》中文译文。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"第五章 极限","link":"/library/volume-87/chapter-005"}
next: {"text":"附录 一般伴随函子定理的证明","link":"/library/volume-87/appendix"}
---

# 第六章 伴随函子、可表函子与极限

<span class="original-page-anchor" id="pdf-page-150" aria-hidden="true"></span>

我们已经从三个不同角度探讨了泛性质的思想，得到三种不同的形式化方式：伴随性、可表性以及极限。在这最后一章中，我们将弄清它们之间的联系。

原则上，凡是能用这三种形式化方式中的某一种描述的内容，也都能用另外两种描述。这与笛卡尔坐标和极坐标的情形相似：凡是能用极坐标完成的事情，原则上也都能用笛卡尔坐标完成，反之亦然；不过，有些事情在一种坐标系中处理起来比在另一种中更为简洁自然。

在比较这三种方法的过程中，我们会发现范畴论的许多基本结果。下面列出其中的几个要点。

- 函子范畴中的极限和余极限以最简单的方式运作。
- 把范畴 $\mathbf{A}$ 嵌入其预层范畴 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 的嵌入保持极限（但不保持余极限）。
- 可表函子就像预层中的素数：每一个预层都可以典范地表示为可表函子的余极限。
- 具有左伴随的函子保持极限。在适当的假设下，逆命题也成立。
- 预层范畴 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 的行为与集合范畴十分相似；由此开始的一段奇妙故事，将逻辑与几何这两个领域联系起来。

## 6.1 用可表函子和伴随描述极限

极限的定义有不止一种表述方式。在第 5 章，我们采用了一种明确展开的定义形式，它尤其便于处理例子。但我们很快就要发展极限和余极限的*理论*，<span class="original-page-anchor" id="pdf-page-151" aria-hidden="true"></span>而为此，换一种方式表述定义会很有用。事实上，我们将用两种不同方式重新表述它：一种用可表性，另一种用伴随。

我们首先说明，锥其实就是某种特殊的自然变换。为此，需要引入一些记号。给定范畴 $\mathbf{I}$ 和 $\mathscr{A}$ 以及对象 $A\in\mathscr{A}$，有一个函子 $\Delta A\colon\mathbf{I}\to\mathscr{A}$，它在所有对象上的值都是 $A$，在所有态射上的值都是 $1_A$。对每个 $\mathbf{I}$ 和 $\mathscr{A}$，由此定义了**对角函子**

$$
\Delta\colon\mathscr{A}\to[\mathbf{I},\mathscr{A}].
$$

考虑 $\mathbf{I}$ 是具有两个对象的离散范畴的情形，就能理解这一名称；此时 $[\mathbf{I},\mathscr{A}]=\mathscr{A}\times\mathscr{A}$，且 $\Delta(A)=(A,A)$。

现在，给定图表 $D\colon\mathbf{I}\to\mathscr{A}$ 和对象 $A\in\mathscr{A}$，$D$ 上以 $A$ 为顶点的锥就是一个自然变换

![作为自然变换的锥](/library/volume-87/diagrams/pdf-0151-cone-transformation.png)

用 $\operatorname{Cone}(A,D)$ 表示 $D$ 上以 $A$ 为顶点的所有锥组成的集合，于是有

$$
\operatorname{Cone}(A,D)=[\mathbf{I},\mathscr{A}](\Delta A,D).\tag{6.1}
$$

因此，$\operatorname{Cone}(A,D)$ 关于 $A$ 具有反变函子性，关于 $D$ 具有协变函子性。

下面是对极限定义的第一种重新表述。

**命题 6.1.1** 设 $\mathbf{I}$ 是小范畴，$\mathscr{A}$ 是范畴，$D\colon\mathbf{I}\to\mathscr{A}$ 是图表。那么，$D$ 上的极限锥与函子

$$
\operatorname{Cone}(-,D)\colon\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}
$$

的表示之间存在一一对应；其中，$\operatorname{Cone}(-,D)$ 的表示对象正是 $D$ 的极限对象（也就是极限锥的顶点）。

简要地说：$D$ 的极限就是 $[\mathbf{I},\mathscr{A}](\Delta-,D)$ 的一个表示。

**证明** 根据推论 4.3.2，$\operatorname{Cone}(-,D)$ 的一个表示由 $D$ 上具有某种泛性质的一个锥组成。这一泛性质恰好就是极限锥定义中的泛性质。$\square$

这个命题把如下想法形式化了：图表 $D$ 上的锥与指向 $\lim\limits_{\leftarrow\mathbf{I}}D$ 的态射一一对应。它意味着，如果 $D$ 具有极限，那么

$$
\operatorname{Cone}(A,D)\cong\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\tag{6.2}
$$

<span class="original-page-anchor" id="pdf-page-152" aria-hidden="true"></span>

![极限之间的诱导态射](/library/volume-87/diagrams/pdf-0152-induced-maps.png)

图 6.1 引理 6.1.3 的示意图。

关于 $A$ 是自然的。这个对应从左到右由下式给出

$$
(f_I)_{I\in\mathbf{I}}\mapsto\bar f
$$

（采用定义 5.1.19 中的记号），从右到左由下式给出

$$
(p_I\circ g)_{I\in\mathbf{I}}\mathrel{\leftarrow\!\vert}g,
$$

其中 $p_I\colon\lim\limits_{\leftarrow\mathbf{I}}D\to D(I)$ 是投影。

由命题 6.1.1 和推论 4.3.10，我们推出：

**推论 6.1.2** 极限在同构意义下唯一。$\square$

对锥的刻画 (6.1) 提示我们，可以同时让图表 $D$ 和顶点 $A$ 变化。这自然引出如下问题：给定图表之间的态射 $D\to D'$，是否会诱导出 $D$ 与 $D'$ 的极限之间的态射？答案是肯定的（图 6.1）：

**引理 6.1.3** 设 $\mathbf{I}$ 是小范畴，且

![从 D 到 D prime 的自然变换](/library/volume-87/diagrams/pdf-0152-natural-transformation.png)

是自然变换。设

$$
\biggl(\lim\limits_{\leftarrow\mathbf{I}}D\xrightarrow{p_I}D(I)\biggr)_{I\in\mathbf{I}}\qquad\text{和}\qquad\biggl(\lim\limits_{\leftarrow\mathbf{I}}D'\xrightarrow{p'_I}D'(I)\biggr)_{I\in\mathbf{I}}
$$

是极限锥。那么：

(a) 存在唯一态射 $\lim\limits_{\leftarrow\mathbf{I}}\alpha\colon\lim\limits_{\leftarrow\mathbf{I}}D\to\lim\limits_{\leftarrow\mathbf{I}}D'$，使得对所有 $I\in\mathbf{I}$，以下<span class="original-page-anchor" id="pdf-page-153" aria-hidden="true"></span>方块

![定义极限间诱导态射的方块](/library/volume-87/diagrams/pdf-0153-limit-square.png)

交换；

(b) 给定锥 $\bigl(A\xrightarrow{f_I}D(I)\bigr)_{I\in\mathbf{I}}$ 和 $\bigl(A'\xrightarrow{f'_I}D'(I)\bigr)_{I\in\mathbf{I}}$，以及态射 $s\colon A\to A'$，使得对所有 $I\in\mathbf{I}$，方块

![锥之间相容的态射](/library/volume-87/diagrams/pdf-0153-cone-square.png)

都交换，那么方块

![顶点与极限之间的对应方块](/library/volume-87/diagrams/pdf-0153-induced-square.png)

也交换。

**证明** (a) 直接由 $\bigl(\lim\limits_{\leftarrow\mathbf{I}}D\xrightarrow{\alpha_Ip_I}D'(I)\bigr)_{I\in\mathbf{I}}$ 是 $D'$ 上的锥这一事实得出。为证明 (b)，注意到对每个 $I\in\mathbf{I}$，都有

$$
p'_I\circ\biggl(\lim\limits_{\leftarrow\mathbf{I}}\alpha\biggr)\circ\bar f=\alpha_I\circ p_I\circ\bar f=\alpha_I\circ f_I=f'_I\circ s=p'_I\circ\overline{f'}\circ s.
$$

因此，根据练习 5.1.36(a)，$\bigl(\lim\limits_{\leftarrow\mathbf{I}}\alpha\bigr)\circ\bar f=\overline{f'}\circ s$。$\square$

现在，我们可以给出对极限定义的第二种重新表述。它只适用于范畴具有所讨论形状的*所有*极限的情形。

**命题 6.1.4** 设 $\mathbf{I}$ 是小范畴，$\mathscr{A}$ 是具有形状为 $\mathbf{I}$ 的所有极限的范畴。那么 $\lim\limits_{\leftarrow\mathbf{I}}$ 定义了一个函子 $[\mathbf{I},\mathscr{A}]\to\mathscr{A}$，而且这个函子是对角函子的右伴随。

**证明** 对每个 $D\in[\mathbf{I},\mathscr{A}]$，选取 $D$ 上的一个极限锥，并把它的顶点记作 $\lim\limits_{\leftarrow\mathbf{I}}D$。对 $[\mathbf{I},\mathscr{A}]$ 中的每个态射 $\alpha\colon D\to D'$，我们都有一个典范态射 $\lim\limits_{\leftarrow\mathbf{I}}\alpha\colon$ <span class="original-page-anchor" id="pdf-page-154" aria-hidden="true"></span>$\lim\limits_{\leftarrow\mathbf{I}}D\to\lim\limits_{\leftarrow\mathbf{I}}D'$，其定义与引理 6.1.3(a) 中相同。这样就把 $\lim\limits_{\leftarrow\mathbf{I}}$ 定义成了一个函子。命题 6.1.1 意味着

$$
[\mathbf{I},\mathscr{A}](\Delta A,D)=\operatorname{Cone}(A,D)\cong\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)
$$

关于 $A$ 是自然的；而在引理 6.1.3(b) 中取 $s=1_A$，就可知这个同构关于 $D$ 也是自然的。$\square$

为定义函子 $\lim\limits_{\leftarrow\mathbf{I}}$，我们必须为每个 $D$ *选取*一个 $D$ 上的极限锥。这一选取并不是典范的。不过，由伴随函子的唯一性可知，不同的选取所得的函子 $\lim\limits_{\leftarrow\mathbf{I}}$ 至多相差一个自然同构。

### 练习

**6.1.5** 在 $\mathbf{I}$ 是具有两个对象的离散范畴这一特殊情形下，解释本节的全部理论。

**6.1.6** 当 $\mathbf{I}$ 是群且 $\mathscr{A}=\mathbf{Set}$ 时，命题 6.1.4 说了什么？命题 6.1.4 的对偶命题又说了什么？

## 6.2 预层的极限与余极限

函子范畴 $[\mathscr{A},\mathscr{B}]$ 中的极限与余极限是什么样的？具体来说，预层范畴 $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 中的极限与余极限是什么样的？再具体一些，可表函子的极限和余极限又怎样？它们也可表吗？

我们将回答所有这些问题。为此，先证明可表函子保持极限。

### 可表函子保持极限

首先回顾一下：根据积的定义，一个态射 $A\to X\times Y$ 等同于一对态射 $(A\to X,A\to Y)$。这里 $A$、$X$ 和 $Y$ 都是具有二元积的范畴 $\mathscr{A}$ 的对象。因此，存在双射

$$
\mathscr{A}(A,X\times Y)\cong\mathscr{A}(A,X)\times\mathscr{A}(A,Y)\tag{6.3}
$$

它关于 $A,X,Y\in\mathscr{A}$ 是自然的。

这是积独有的性质，还是对每一种极限都有类似的结论？让我们试试等化子。假设 $\mathscr{A}$ 具有等化子，<span class="original-page-anchor" id="pdf-page-155" aria-hidden="true"></span>并用

![等化子的记号](/library/volume-87/diagrams/pdf-0155-equalizer-notation.png)

表示态射 $s$ 和 $t$ 的等化子。根据等化子的定义，态射

![指向等化子的态射，式 6.4](/library/volume-87/diagrams/pdf-0155-map-to-equalizer.png)

与满足 $s\circ f=t\circ f$ 的态射 $f\colon A\to X$ 一一对应。现在回顾一下，$s$ 诱导出态射

$$
s_* =\mathscr{A}(A,s)\colon\mathscr{A}(A,X)\to\mathscr{A}(A,Y),
$$

$t$ 也同样如此。用这个记号，我们刚才说的就是：态射 (6.4) 与满足

$$
\bigl(\mathscr{A}(A,s)\bigr)(f)=\bigl(\mathscr{A}(A,t)\bigr)(f)
$$

的元素 $f\in\mathscr{A}(A,X)$ 一一对应。由 $\mathbf{Set}$ 中等化子的明确公式（例 5.1.12）可知，这样的 $f$ 恰好就是 $\mathscr{A}(A,s)$ 和 $\mathscr{A}(A,t)$ 的等化子的一个元素。因此，我们有一个典范双射

![等化子的典范双射，式 6.5](/library/volume-87/diagrams/pdf-0155-equalizer-bijection.png)

这看起来与我们得到的关于积的同构 (6.3) 有些相似。

同构 (6.3) 和 (6.5) 提示我们，更一般地，只要 $\mathscr{A}$ 是具有形状为 $\mathbf{I}$ 的极限的范畴，或许就有

$$
\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\cong\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)\tag{6.6}
$$

并且它关于 $A\in\mathscr{A}$ 和 $D\in[\mathbf{I},\mathscr{A}]$ 是自然的。这里 $\mathscr{A}(A,D)$ 是函子

$$
\begin{array}{rccc}
\mathscr{A}(A,D)\colon&\mathbf{I}&\to&\mathbf{Set}\\
&I&\mapsto&\mathscr{A}(A,D(I)).
\end{array}
$$

这个函子也可以写成 $\mathscr{A}(A,D(-))$，它是以下复合

$$
\mathbf{I}\xrightarrow{D}\mathscr{A}\xrightarrow{\mathscr{A}(A,-)}\mathbf{Set}.
$$

所猜想的同构 (6.6) 实质上是在说，可表函子保持极限。现在我们来证明这一点。

**引理 6.2.1** 设 $\mathbf{I}$ 是小范畴，$\mathscr{A}$ 是局部小范畴，$D\colon\mathbf{I}\to\mathscr{A}$ 是图表，且 $A\in\mathscr{A}$。那么

$$
\operatorname{Cone}(A,D)\cong\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)
$$

关于 $A$ 和 $D$ 是自然的。

<span class="original-page-anchor" id="pdf-page-156" aria-hidden="true"></span>

**证明** 与所有从小范畴到 $\mathbf{Set}$ 的函子一样，函子 $\mathscr{A}(A,D)$ 确实具有极限，它由明确公式 (5.16) 给出。根据这个公式，$\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)$ 是所有族 $(f_I)_{I\in\mathbf{I}}$ 组成的集合，其中对所有 $I\in\mathbf{I}$ 都有 $f_I\in\mathscr{A}(A,D(I))$，而且对 $\mathbf{I}$ 中的所有 $I\xrightarrow{u}J$，都有

$$
(\mathscr{A}(A,Du))(f_I)=f_J.\tag{6.7}
$$

但等式 (6.7) 无非就是说 $(Du)\circ f_I=f_J$，因此 $\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)$ 的一个元素恰好就是 $D$ 上以 $A$ 为顶点的一个锥。$\square$

**命题 6.2.2（可表函子保持极限）** 设 $\mathscr{A}$ 是局部小范畴，且 $A\in\mathscr{A}$。那么 $\mathscr{A}(A,-)\colon\mathscr{A}\to\mathbf{Set}$ 保持极限。

**证明** 设 $\mathbf{I}$ 是小范畴，$D\colon\mathbf{I}\to\mathscr{A}$ 是具有极限的图表。那么

$$
\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\cong\operatorname{Cone}(A,D)\cong\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)
$$

关于 $A$ 是自然的。这里，第一个同构来自命题 6.1.1（更确切地说，来自紧随其后的同构 (6.2)），第二个同构来自引理 6.2.1。$\square$

**注 6.2.3** 命题 6.2.2 告诉我们，

$$
\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\cong\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D).\tag{6.8}
$$

要得到命题 6.2.2 的对偶，把 $\mathscr{A}$ 换成 $\mathscr{A}^{\mathrm{op}}$ 即可。于是 $\mathscr{A}(-,A)\colon\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}$ 保持极限。$\mathscr{A}^{\mathrm{op}}$ 中的极限就是 $\mathscr{A}$ 中的余极限，因此 $\mathscr{A}(-,A)$ 把 $\mathscr{A}$ 中的余极限变为 $\mathbf{Set}$ 中的极限：

$$
\mathscr{A}\biggl(\lim\limits_{\rightarrow\mathbf{I}}D,A\biggr)\cong\lim\limits_{\leftarrow\mathbf{I}^{\mathrm{op}}}\mathscr{A}(D,A).\tag{6.9}
$$

右边是*极限*，而不是余极限！所以，虽然 (6.8) 与 (6.9) 是对偶的陈述，两者总共涉及的极限仍比余极限多。极限似乎总是占上风。

例如，设 $X$、$Y$ 和 $A$ 是范畴 $\mathscr{A}$ 的对象，并假设余积 $X+Y$ 存在。根据余积的定义，一个态射 $X+Y\to A$ 等同于一对态射 $(X\to A,Y\to A)$。换句话说，有一个典范同构

$$
\mathscr{A}(X+Y,A)\cong\mathscr{A}(X,A)\times\mathscr{A}(Y,A).
$$

这就是当 $\mathbf{I}$ 是具有两个对象的离散范畴时的同构 (6.9)。

<span class="original-page-anchor" id="pdf-page-157" aria-hidden="true"></span>

### 函子范畴中的极限

前面我们了解到，有时把函子本身看作对象，而不是范畴之间的态射，会很有用。例如，当 $G$ 是群时，函子 $G\to\mathbf{Set}$ 就是 $G$-集合（例 1.2.8）；我们通常把它看成一个“东西”，而不是一个“映射”。这个观点引出了函子范畴的概念。

现在，我们开始分析函子范畴 $[\mathbf{A},\mathscr{S}]$ 中的极限与余极限。这里 $\mathbf{A}$ 是小范畴，$\mathscr{S}$ 是局部小范畴；这两个条件合起来保证 $[\mathbf{A},\mathscr{S}]$ 是局部小范畴。对我们而言，最重要的情形是 $\mathscr{S}=\mathbf{Set}$ 和 $\mathscr{S}=\mathbf{Set}^{\mathrm{op}}$。因此，只要有需要，我们就会假设 $\mathscr{S}$ 具有所有极限与余极限。

我们将说明，$[\mathbf{A},\mathscr{S}]$ 中的极限与余极限以所能想象的最简单方式运作。例如，如果 $\mathscr{S}$ 具有二元积，那么 $[\mathbf{A},\mathscr{S}]$ 也具有二元积；两个函子 $X,Y\colon\mathbf{A}\to\mathscr{S}$ 的积就是函子 $X\times Y\colon\mathbf{A}\to\mathscr{S}$，对所有 $A\in\mathbf{A}$，它满足

$$
(X\times Y)(A)=X(A)\times Y(A).
$$

**记号 6.2.4** 设 $\mathbf{A}$ 和 $\mathscr{S}$ 是范畴。对每个 $A\in\mathbf{A}$，都有一个函子

$$
\begin{array}{rccc}
\operatorname{ev}_A\colon &[\mathbf{A},\mathscr{S}]&\to&\mathscr{S}\\
&X&\mapsto&X(A),
\end{array}
$$

称为**在 $A$ 处取值**。我们将讨论 $[\mathbf{A},\mathscr{S}]$ 中的图表。给定这样的图表 $D\colon\mathbf{I}\to[\mathbf{A},\mathscr{S}]$，对每个 $A\in\mathbf{A}$，都有一个函子

$$
\begin{array}{rccc}
\operatorname{ev}_A\circ D\colon &\mathbf{I}&\to&\mathscr{S}\\
&I&\mapsto&D(I)(A).
\end{array}
$$

我们把 $\operatorname{ev}_A\circ D$ 记作 $D(-)(A)$。

**定理 6.2.5（函子范畴中的极限）** 设 $\mathbf{A}$ 和 $\mathbf{I}$ 是小范畴，$\mathscr{S}$ 是局部小范畴。设 $D\colon\mathbf{I}\to[\mathbf{A},\mathscr{S}]$ 是图表，并假设对每个 $A\in\mathbf{A}$，图表 $D(-)(A)\colon\mathbf{I}\to\mathscr{S}$ 都有极限。那么，存在 $D$ 上的一个锥，使得对每个 $A\in\mathbf{A}$，它在 $\operatorname{ev}_A$ 下的像都是 $D(-)(A)$ 上的极限锥。而且，$D$ 上任何这样的锥都是极限锥。

定理 6.2.5 常被概括为一句口号：

*函子范畴中的极限是逐点计算的。*

“逐点”中的“点”指的是 $\mathbf{A}$ 的对象。例如，这句口号的意思是，给定两个函子 $X,Y\in[\mathbf{A},\mathscr{S}]$，要计算它们的积，可以<span class="original-page-anchor" id="pdf-page-158" aria-hidden="true"></span>先对每个“点” $A$，在 $\mathscr{S}$ 中取积 $X(A)\times Y(A)$，再把它们组合成函子 $X\times Y$。

当然，定理 6.2.5 也有一个对偶版本，它说明函子范畴中的余极限也是逐点计算的。

**定理 6.2.5 的证明** 对每个 $A\in\mathbf{A}$，在图表 $D(-)(A)\colon\mathbf{I}\to\mathscr{S}$ 上取一个极限锥

$$
\bigl(L(A)\xrightarrow{p_{I,A}}D(I)(A)\bigr)_{I\in\mathbf{I}}.\tag{6.10}
$$

我们证明以下两点：

(a) 把 $L$ 扩充为 $\mathbf{A}$ 上的函子，使得 $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ 是 $D$ 上的锥，这样的扩充方式恰有一种；

(b) 这个锥 $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ 是极限锥。

定理便会立即由此得出。

为证明 (a)，取 $\mathbf{A}$ 中的态射 $f\colon A\to A'$。把引理 6.1.3(a) 应用于自然变换

![由 f 诱导的自然变换](/library/volume-87/diagrams/pdf-0158-parameter-transformation.png)

可知，存在唯一态射 $L(f)\colon L(A)\to L(A')$，使得对所有 $I\in\mathbf{I}$，方块

![投影的自然性方块，式 6.11](/library/volume-87/diagrams/pdf-0158-pointwise-square.png)

都交换。（这就是我们对 $L(f)$ 的*定义*。）现在，我们已经定义了 $L$ 在 $\mathbf{A}$ 的对象和态射上的作用。容易验证 $L$ 保持复合与恒等态射，因此它是一个函子 $L\colon\mathbf{A}\to\mathscr{S}$。此外，图 (6.11) 的交换性恰好说明：对每个 $I\in\mathbf{I}$，族 $\bigl(L(A)\xrightarrow{p_{I,A}}D(I)(A)\bigr)_{A\in\mathbf{A}}$ 是自然变换

![作为自然变换的投影](/library/volume-87/diagrams/pdf-0158-projection-transformation.png)

因此，我们得到 $[\mathbf{A},\mathscr{S}]$ 中的一族态射 $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$。由于对每个 $A\in\mathbf{A}$，(6.10) 都是 $D(-)(A)$ 上的锥，立即可知 $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ 是 $D$ 上的锥。

<span class="original-page-anchor" id="pdf-page-159" aria-hidden="true"></span>

为证明 (b)，设 $X\in[\mathbf{A},\mathscr{S}]$，并设 $\bigl(X\xrightarrow{q_I}D(I)\bigr)_{I\in\mathbf{I}}$ 是 $[\mathbf{A},\mathscr{S}]$ 中 $D$ 上的锥。对每个 $A\in\mathbf{A}$，在 $\mathscr{S}$ 中都有 $D(-)(A)$ 上的锥

$$
\bigl(X(A)\xrightarrow{q_{I,A}}D(I)(A)\bigr)_{I\in\mathbf{I}},
$$

因此存在唯一态射 $\bar q_A\colon X(A)\to L(A)$，使得对所有 $I\in\mathbf{I}$，都有 $p_{I,A}\circ\bar q_A=q_{I,A}$。只需再证明 $\bar q_A$ 关于 $A$ 是自然的，而这由引理 6.1.3(b) 得出。$\square$

定理 6.2.5 有许多重要推论。我们先记下这个定理（以及它的对偶）的一个较粗略的版本，后面会反复用到。

**推论 6.2.6** 设 $\mathbf{I}$ 和 $\mathbf{A}$ 是小范畴，$\mathscr{S}$ 是局部小范畴。如果 $\mathscr{S}$ 具有形状为 $\mathbf{I}$ 的所有极限（或所有余极限），那么 $[\mathbf{A},\mathscr{S}]$ 也具有这样的所有极限（或所有余极限）；而且对每个 $A\in\mathbf{A}$，取值函子 $\operatorname{ev}_A\colon[\mathbf{A},\mathscr{S}]\to\mathscr{S}$ 都保持它们。$\square$

**警告 6.2.7** 如果 $\mathscr{S}$ *并不*具有形状为 $\mathbf{I}$ 的所有极限，那么 $[\mathbf{A},\mathscr{S}]$ 中可能有形状为 $\mathbf{I}$ 的极限无法逐点计算，也就是说，并不是所有取值函子都保持它们。这样的例子可以构造出来，见 Kelly (1982) 第 3.3 节。

定理 6.2.5 还将帮助我们证明：极限与极限可交换，具体含义如下。取范畴 $\mathbf{I}$、$\mathbf{J}$ 和 $\mathscr{S}$。有范畴同构

$$
[\mathbf{I},[\mathbf{J},\mathscr{S}]]\cong[\mathbf{I}\times\mathbf{J},\mathscr{S}]\cong[\mathbf{J},[\mathbf{I},\mathscr{S}]].
$$

（见注 4.1.23(c) 和练习 1.2.25。）在这些同构下，函子 $D\colon\mathbf{I}\times\mathbf{J}\to\mathscr{S}$ 对应于以下函子

$$
\begin{array}{rccc}
D^\bullet\colon&\mathbf{I}&\to&[\mathbf{J},\mathscr{S}]\\
&I&\mapsto&D(I,-)
\end{array}
\qquad\text{和}\qquad
\begin{array}{rccc}
D_\bullet\colon&\mathbf{J}&\to&[\mathbf{I},\mathscr{S}]\\
&J&\mapsto&D(-,J).
\end{array}
$$

假设 $\mathscr{S}$ 具有所有极限，那么由推论 6.2.6，各个函子范畴也都具有所有极限。特别地，$[\mathbf{J},\mathscr{S}]$ 中存在对象 $\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$。它本身是 $\mathscr{S}$ 中的图表，所以我们又得到 $\mathscr{S}$ 的一个对象 $\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$。也可以按另一种顺序取极限，得到 $\mathscr{S}$ 的对象 $\lim\limits_{\leftarrow\mathbf{I}}\lim\limits_{\leftarrow\mathbf{J}}D_\bullet$。还有第三种可能：直接取 $D$ 的极限，得到 $\mathscr{S}$ 的另一个对象 $\lim\limits_{\leftarrow\mathbf{I}\times\mathbf{J}}D$。下面的结果说明，这三个对象是相同的。也就是说，取极限的顺序并不影响结果。

**命题 6.2.8（极限与极限可交换）** 设 $\mathbf{I}$ 和 $\mathbf{J}$ 是小范畴。设 $\mathscr{S}$ 是局部小范畴，它具有形状为 $\mathbf{I}$ 的极限以及形状为<span class="original-page-anchor" id="pdf-page-160" aria-hidden="true"></span>$\mathbf{J}$ 的极限。那么，对所有 $D\colon\mathbf{I}\times\mathbf{J}\to\mathscr{S}$，都有

$$
\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet\cong\lim\limits_{\leftarrow\mathbf{I}\times\mathbf{J}}D\cong\lim\limits_{\leftarrow\mathbf{I}}\lim\limits_{\leftarrow\mathbf{J}}D_\bullet,
$$

而且这些极限全都存在。特别地，$\mathscr{S}$ 具有形状为 $\mathbf{I}\times\mathbf{J}$ 的极限。

这个结果有时被半开玩笑地称为富比尼定理，因为它有点像交换二重积分的积分顺序。用*余*极限来作这个类比更贴切，因为与积分类似，余极限也可以看成依赖于具体情境的求和。

**证明** 由对称性，只需证明第一个同构。由于 $\mathscr{S}$ 具有形状为 $\mathbf{I}$ 的极限，$[\mathbf{J},\mathscr{S}]$ 也具有这样的极限（根据推论 6.2.6）。因此 $\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$ 存在，它是 $[\mathbf{J},\mathscr{S}]$ 的一个对象。又因为 $\mathscr{S}$ 具有形状为 $\mathbf{J}$ 的极限，$\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$ 也存在，它是 $\mathscr{S}$ 的一个对象。那么，对 $S\in\mathscr{S}$，有

$$
\begin{aligned}
\mathscr{S}\biggl(S,\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet\biggr)&\cong[\mathbf{J},\mathscr{S}]\biggl(\Delta S,\lim\limits_{\leftarrow\mathbf{I}}D^\bullet\biggr)\\
&\cong[\mathbf{I},[\mathbf{J},\mathscr{S}]](\Delta(\Delta S),D^\bullet)\\
&\cong[\mathbf{I}\times\mathbf{J},\mathscr{S}](\Delta S,D)
\end{aligned}
$$

关于 $S$ 是自然的。前两步分别由命题 6.1.1 得出。第三步使用同构 $[\mathbf{I},[\mathbf{J},\mathscr{S}]]\cong[\mathbf{I}\times\mathbf{J},\mathscr{S}]$；在这个同构下，$\Delta(\Delta S)$ 对应于 $\Delta S$，而 $D^\bullet$ 对应于 $D$。

因此，$\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$ 是函子 $[\mathbf{I}\times\mathbf{J},\mathscr{S}](\Delta-,D)$ 的表示对象。再次根据命题 6.1.1，这就是说 $\lim\limits_{\leftarrow\mathbf{I}\times\mathbf{J}}D$ 存在，且同构于 $\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$。$\square$

**例 6.2.9** 当 $\mathbf{I}=\mathbf{J}=$ ![具有两个对象的离散范畴](/library/volume-87/diagrams/pdf-0160-two-object-category.png) 时，命题 6.2.8 说明二元积与二元积可交换：如果 $\mathscr{S}$ 具有二元积，且 $S_{11},S_{12},S_{21},S_{22}\in\mathscr{S}$，那么四元积 $\prod_{i,j\in\{1,2\}}S_{ij}$ 存在，且满足

$$
(S_{11}\times S_{21})\times(S_{12}\times S_{22})\cong\prod_{i,j\in\{1,2\}}S_{ij}\cong(S_{11}\times S_{12})\times(S_{21}\times S_{22}).
$$

更一般地，无论按什么顺序写积，或把括号放在什么位置，都不影响结果：在任何具有二元积的范畴中，都有典范同构

$$
\begin{aligned}
S\times T&\cong T\times S,\\
(S\times T)\times U&\cong S\times(T\times U).
\end{aligned}
$$

如果还有终对象 $1$，则还存在典范同构

$$
S\times1\cong S\cong1\times S.
$$

<span class="original-page-anchor" id="pdf-page-161" aria-hidden="true"></span>

**警告 6.2.10** 命题 6.2.8 的对偶说明，余极限与余极限可交换。例如，在任何具有二元余积的范畴 $\mathscr{S}$ 中，都有

$$
(S_{11}+S_{21})+(S_{12}+S_{22})\cong(S_{11}+S_{12})+(S_{21}+S_{22}).
$$

但是，极限与余极限一般*不可*交换。例如，一般而言，

$$
(S_{11}+S_{21})\times(S_{12}+S_{22})\not\cong(S_{11}\times S_{12})+(S_{21}\times S_{22}).
$$

取 $\mathscr{S}=\mathbf{Set}$，并令每个 $S_{ij}$ 都是单元素集合，就得到一个反例。此时左边有 $(1+1)\times(1+1)=4$ 个元素，而右边有 $(1\times1)+(1\times1)=2$ 个元素。

下面是定理 6.2.5 的另外两个推论。

**推论 6.2.11** 设 $\mathbf{A}$ 是小范畴。那么 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 具有所有极限与余极限，而且对每个 $A\in\mathbf{A}$，取值函子 $\operatorname{ev}_A\colon[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]\to\mathbf{Set}$ 都保持它们。

**证明** 由于 $\mathbf{Set}$ 具有所有极限与余极限，这由推论 6.2.6 立即得出。$\square$

**推论 6.2.12** 对任意小范畴 $\mathbf{A}$，米田嵌入 $H_\bullet\colon\mathbf{A}\to[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 保持极限。

**证明** 设 $D\colon\mathbf{I}\to\mathbf{A}$ 是 $\mathbf{A}$ 中的图表，$\bigl(\lim\limits_{\leftarrow\mathbf{I}}D\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ 是极限锥。对每个 $A\in\mathbf{A}$，复合函子

$$
\mathbf{A}\xrightarrow{H_\bullet}[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]\xrightarrow{\operatorname{ev}_A}\mathbf{Set}
$$

就是 $H^A$，它保持极限（命题 6.2.2）。因此，对每个 $A\in\mathbf{A}$，

$$
\biggl(\operatorname{ev}_AH_\bullet\biggl(\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\xrightarrow{\operatorname{ev}_AH_\bullet(p_I)}\operatorname{ev}_AH_\bullet(D(I))\biggr)_{I\in\mathbf{I}}
$$

都是极限锥。随后，把定理 6.2.5 的“而且”部分应用于 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 中的图表 $H_\bullet\circ D$，可知锥

$$
\biggl(H_\bullet\biggl(\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\xrightarrow{H_\bullet(p_I)}H_\bullet(D(I))\biggr)_{I\in\mathbf{I}}
$$

也是极限，这正是所要证明的。$\square$

**例 6.2.13** 设 $\mathbf{A}$ 是具有二元积的范畴。推论 6.2.12 意味着，对所有 $X,Y\in\mathbf{A}$，都有

$$
H_{X\times Y}\cong H_X\times H_Y\tag{6.12}
$$

<span class="original-page-anchor" id="pdf-page-162" aria-hidden="true"></span>

在 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 中。在某个特定对象 $A$ 处求值，这就表明

$$
\mathbf{A}(A,X\times Y)\cong\mathbf{A}(A,X)\times\mathbf{A}(A,Y)
$$

（这里使用了积逐点计算这一事实）。这就是我们在本节开头遇到的同构 (6.3)。

假设我们把 $\mathbf{A}$ 看作 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 的子范畴，像图 4.1 那样，将 $A\in\mathbf{A}$ 与可表函子 $H_A\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 认同。那么，同构 (6.12) 的意思是：给定 $\mathbf{A}$ 的两个对象，要构造它们的积，无论是在 $\mathbf{A}$ 中还是在 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 中构造，结果都没有区别。类似地，如果 $\mathbf{A}$ 有所有极限，那么取极限也无法让我们走出 $\mathbf{A}$，进入 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 的其余部分：可表预层的任何极限仍然可表。

**警告 6.2.14** 米田嵌入*不*保持余极限。例如，如果 $\mathbf{A}$ 有始对象 $0$，那么 $H_0$ 并不是始对象，因为 $H_0(0)=\mathbf{A}(0,0)$ 是单元素集，而 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 的始对象是恒取值 $\varnothing$ 的预层。接下来我们研究可表函子的余极限。

### 每个预层都是可表函子的余极限

现在我们知道，米田嵌入保持极限，但不保持余极限。事实上，余极限的情形与极限的情形处在两个相反的极端：通过取可表预层的余极限，我们可以得到任意想要的预层！这是本节最后一个主要结果。

每个正整数都能以本质唯一的方式表示为素数的积。与此有些类似，每个预层都能以一种典范（但不唯一）的方式表示为可表函子的余极限。可表函子是构成预层的基本材料。

再作一个不同的类比：回忆一下，任何在 $0$ 的某个邻域内全纯的复函数都有幂级数展开，例如

$$
e^z=1+z+\frac{z^2}{2!}+\frac{z^3}{3!}+\cdots.
$$

从这个意义上说，幂函数 $z\mapsto z^n$ 是构成全纯函数的基本材料。我们甚至可以把这个类比再推进一步：$(\ )^n$ 类似于可表函子 $\operatorname{Hom}(n,-)$，而在范畴的语境中，商与和都是余极限的类型。

在陈述并证明这个定理之前，先来看一个简单的特殊情形。

**例 6.2.15** 设 $\mathbf{A}$ 是有两个对象 $K$ 和 $L$ 的离散范畴。$\mathbf{A}$ 上的一个<span class="original-page-anchor" id="pdf-page-163" aria-hidden="true"></span>预层 $X$ 就是一对集合 $(X(K),X(L))$，而且 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]\cong\mathbf{Set}\times\mathbf{Set}$。有两个可表函子 $H_K$ 和 $H_L$，其取值为

$$
H_A(B)=\mathbf{A}(B,A)\cong
\begin{cases}
1&\text{若 }A=B,\\
\varnothing&\text{若 }A\ne B
\end{cases}
$$

（$A,B\in\{K,L\}$）。将 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 与 $\mathbf{Set}\times\mathbf{Set}$ 认同，我们就有 $H_K\cong(1,\varnothing)$ 和 $H_L\cong(\varnothing,1)$。$\mathbf{Set}\times\mathbf{Set}$ 的每个对象都是若干个 $(1,\varnothing)$ 和 $(\varnothing,1)$ 的副本的和。例如，假设 $X(K)$ 有三个元素，而 $X(L)$ 有两个元素。那么在 $\mathbf{Set}\times\mathbf{Set}$ 中，

$$
(X(K),X(L))\cong(1,\varnothing)+(1,\varnothing)+(1,\varnothing)+(\varnothing,1)+(\varnothing,1).
$$

等价地，在 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 中，

$$
X\cong H_K+H_K+H_K+H_L+H_L,
$$

这就把 $X$ 表示成了可表函子的和。

在这个例子中，$X$ 被表示为五个可表函子的和，也就是说，是由 $X$ 的“元素”所组成的集合 $X(K)+X(L)$ 索引的和。和是离散范畴上的余极限。在一般情形下，范畴 $\mathbf{A}$ 上的预层 $X$ 被表示为某个范畴上的余极限，而这个范畴的对象可以看作 $X$ 的“元素”。下面的定义使这一点精确化。

**定义 6.2.16** 设 $\mathbf{A}$ 是一个范畴，$X$ 是 $\mathbf{A}$ 上的预层。$X$ 的**元素范畴** $\mathbf{E}(X)$ 是如下范畴：

- 对象是满足 $A\in\mathbf{A}$、$x\in X(A)$ 的对 $(A,x)$；
- 态射 $(A',x')\to(A,x)$ 是 $\mathbf{A}$ 中满足 $(Xf)(x)=x'$ 的态射 $f:A'\to A$。

有一个投影函子 $P:\mathbf{E}(X)\to\mathbf{A}$，由 $P(A,x)=A$ 和 $P(f)=f$ 定义。

下面的“稠密性定理”指出，每个预层都能以一种典范方式表示为可表函子的余极限。它与米田引理之间有着不易看出的对偶关系。如果用适当的高层次范畴语言（端的语言，或双模的语言）来表述二者，这一点就会显现出来；不过，这超出了本书的范围。

**定理 6.2.17（稠密性）** 设 $\mathbf{A}$ 是小范畴，$X$ 是 $\mathbf{A}$ 上的预层。那么 $X$ 是图表

$$
\mathbf{E}(X)\xrightarrow{P}\mathbf{A}\xrightarrow{H_\bullet}[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]
$$

在 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 中的余极限；也就是说，$X\cong\lim_{\rightarrow\mathbf{E}(X)}(H_\bullet\circ P)$。

<span class="original-page-anchor" id="pdf-page-164" aria-hidden="true"></span>

**证明** 首先注意，由于 $\mathbf{A}$ 是小范畴，$\mathbf{E}(X)$ 也是小范畴。因此，$H_\bullet\circ P$ 确实是我们通常意义下的图表（定义 5.1.18）。

现在设 $Y\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$。$H_\bullet\circ P$ 上顶点为 $Y$ 的余锥是一个自然变换族

$$
\bigl(H_A\xrightarrow{\alpha_{A,x}}Y\bigr)_{A\in\mathbf{A},x\in X(A)},
$$

并满足：对 $\mathbf{A}$ 中的所有态射 $A'\xrightarrow{f}A$ 以及所有 $x\in X(A)$，图

![余锥的相容性图](/library/volume-87/diagrams/pdf-0164-density-cocone.png)

交换。

等价地（根据米田引理），$H_\bullet\circ P$ 上顶点为 $Y$ 的余锥是一个族

$$
(y_{A,x})_{A\in\mathbf{A},x\in X(A)},
$$

其中 $y_{A,x}\in Y(A)$，并且对 $\mathbf{A}$ 中的所有态射 $A'\xrightarrow{f}A$ 以及所有 $x\in X(A)$，都有

$$
(Yf)(y_{A,x})=y_{A',(Xf)(x)}.
$$

要看出这一点，注意：如果 $\alpha_{A,x}\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}](H_A,Y)$ 对应于 $y_{A,x}\in Y(A)$，那么 $\alpha_{A,x}\circ H_f\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}](H_{A'},Y)$ 就对应于 $(Yf)(y_{A,x})\in Y(A')$。

等价地（将 $y_{A,x}$ 写成 $\bar\alpha_A(x)$），它是一个函数族

$$
\bigl(X(A)\xrightarrow{\bar\alpha_A}Y(A)\bigr)_{A\in\mathbf{A}},
$$

并满足：对 $\mathbf{A}$ 中的所有态射 $A'\xrightarrow{f}A$ 以及所有 $x\in X(A)$，都有

$$
(Yf)\bigl(\bar\alpha_A(x)\bigr)=\bar\alpha_{A'}\bigl((Xf)(x)\bigr).
$$

但这恰好就是自然变换 $\bar\alpha:X\to Y$。所以，对每个 $Y\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$，我们都有一个典范双射

$$
[\mathbf{E}(X),[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]](H_\bullet\circ P,\Delta Y)\cong[\mathbf{A}^{\mathrm{op}},\mathbf{Set}](X,Y).
$$

因此，$X$ 是 $H_\bullet\circ P$ 的余极限。$\square$

**例 6.2.18** 在例 6.2.15 中，我们将一个特定预层 $X$ 表示为可表函子的和。让我们检验，当时的做法是稠密性定理中一般构造的特殊情形。

由于 $\mathbf{A}$ 是离散的，元素范畴 $\mathbf{E}(X)$ 也是离散的；它就是有五个元素的集合 $X(K)+X(L)$。投影 $P:\mathbf{E}(X)\to\mathbf{A}$ 将其中三个<span class="original-page-anchor" id="pdf-page-165" aria-hidden="true"></span>元素送到 $K$，将另两个送到 $L$，所以图表 $H_\bullet\circ P:\mathbf{E}(X)\to[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 将其中三个元素送到 $H_K$，将另两个送到 $H_L$。$H_\bullet\circ P$ 的余极限就是这五个可表函子的和，也就是 $X$，正如例 6.2.15 中一样。

**注 6.2.19** (a) “元素范畴”这一术语与定义 4.1.25 中引入的广义元素术语相容。对象 $X$ 的广义元素就是一个到 $X$ 的态射，比如 $Z\to X$；不过，正如该定义之后所解释的，我们通常关注某些特殊形状 $Z$。现在假设我们在预层范畴 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 中工作。在所有预层中，可表函子具有特殊地位，因此，我们可能会特别关注具有可表形状的广义元素。米田引理表明，对预层 $X$ 来说，具有可表形状的 $X$ 的广义元素对应于满足 $A\in\mathbf{A}$、$x\in X(A)$ 的对 $(A,x)$。换言之，它们就是元素范畴的对象。

(b) 在拓扑学中，如果空间 $B$ 中的每一点都能作为 $A$ 中点的极限得到，就称 $B$ 的子空间 $A$ 是稠密的。这在一定程度上解释了定理 6.2.17 的名称：范畴 $\mathbf{A}$ 在 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 中是“稠密”的，因为 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 的每个对象都能作为 $\mathbf{A}$ 中对象的余极限得到。

### 练习

**6.2.20** 固定一个小范畴 $\mathbf{A}$。

(a) 设 $\mathscr{S}$ 是有拉回的局部小范畴。证明：自然变换

![从 X 到 Y 的自然变换 alpha](/library/volume-87/diagrams/pdf-0165-natural-transformation.png)

是单态射（作为 $[\mathbf{A},\mathscr{S}]$ 中的态射），当且仅当对所有 $A\in\mathbf{A}$，$\alpha_A$ 都是单态射。（提示：使用引理 5.1.32。）

(b) 明确描述 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 中的单态射和满态射。

(c) 能否不依赖预层的极限和余极限逐点计算这一事实，完成 (b)？

**6.2.21** (a) 证明可表函子具有如下连通性性质：给定局部小范畴 $\mathscr{A}$ 以及 $A\in\mathscr{A}$，若 $X,Y\in[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ 满足 $H_A\cong X+Y$，则 $X$ 或 $Y$ 中至少有一个是常值函子 $\varnothing$。

(b) 推出两个可表函子的和永远不可表。

<span class="original-page-anchor" id="pdf-page-166" aria-hidden="true"></span>

**6.2.22** 说明如何将元素范畴描述为逗号范畴。

**6.2.23** 设 $X$ 是局部小范畴上的预层。证明：$X$ 可表，当且仅当其元素范畴有终对象。

（由于终对象是空图表的极限，这表明可表性的概念可以从极限的概念导出。又由于范畴 $\mathscr{E}$ 的终对象也是唯一函子 $\mathscr{E}\to\mathbf{1}$ 的右伴随，因此，可表性的概念也可以从伴随的概念导出。）

**6.2.24** 证明预层范畴的每个切片范畴仍然是预层范畴。也就是说，给定小范畴 $\mathbf{A}$ 以及 $\mathbf{A}$ 上的预层 $X$，证明：对某个小范畴 $\mathbf{B}$，$[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]/X$ 等价于 $[\mathbf{B}^{\mathrm{op}},\mathbf{Set}]$。

**6.2.25** 设 $F:\mathbf{A}\to\mathbf{B}$ 是小范畴之间的函子。对每个对象 $B\in\mathbf{B}$，都有一个逗号范畴 $(F\Rightarrow B)$（其定义与例 2.3.4 中的逗号范畴对偶），并有一个投影函子 $P_B:(F\Rightarrow B)\to\mathbf{A}$。

(a) 设 $X:\mathbf{A}\to\mathscr{S}$ 是从 $\mathbf{A}$ 到有小余极限的范畴 $\mathscr{S}$ 的函子。对每个 $B\in\mathbf{B}$，令 $(\operatorname{Lan}_F X)(B)$ 是图表

$$
(F\Rightarrow B)\xrightarrow{P_B}\mathbf{A}\xrightarrow{X}\mathscr{S}
$$

的余极限。证明这定义了一个函子 $\operatorname{Lan}_F X:\mathbf{B}\to\mathscr{S}$，并且对函子 $Y:\mathbf{B}\to\mathscr{S}$，自然变换 $\operatorname{Lan}_F X\to Y$ 与自然变换 $X\to Y\circ F$ 之间有一个典范双射。

(b) 推出：对任何有小余极限的范畴 $\mathscr{S}$，函子

$$
-\circ F:[\mathbf{B},\mathscr{S}]\to[\mathbf{A},\mathscr{S}]
$$

都有左伴随。（这个左伴随 $\operatorname{Lan}_F$ 称为沿 $F$ 的**左 Kan 扩张**。）

(c) (b) 及其对偶表明，当 $\mathscr{S}$ 有小极限与小余极限时，函子 $-\circ F$ 同时有左伴随和右伴随。带着这一认识，重新考察练习 2.1.16，其中取 $F$ 为唯一函子 $\mathbf{1}\to G$，或者唯一函子 $G\to\mathbf{1}$。

## 6.3 伴随函子与极限的相互作用

我们在命题 4.1.11 中看到，任何有左伴随的集合值函子都是可表的；在命题 6.2.2 中看到，任何可表函子都保持极限。

<span class="original-page-anchor" id="pdf-page-167" aria-hidden="true"></span>

因此，任何有左伴随的集合值函子都保持极限。事实上，这个结论不仅对集合值函子成立，而且在完全一般的情形下都成立。

**定理 6.3.1** 设

![A 与 B 之间的伴随关系](/library/volume-87/diagrams/pdf-0167-adjunction.png)

是一个伴随关系。那么 $F$ 保持余极限，$G$ 保持极限。

**证明** 由对偶性，只需证明 $G$ 保持极限。设 $D:\mathbf{I}\to\mathscr{B}$ 是存在极限的图表。那么

$$
\mathscr{A}\left(A,G\left(\lim_{\leftarrow\mathbf{I}}D\right)\right)\cong\mathscr{B}\left(F(A),\lim_{\leftarrow\mathbf{I}}D\right)\tag{6.13}
$$

$$
\phantom{\mathscr{A}\left(A,G\left(\lim_{\leftarrow\mathbf{I}}D\right)\right)}\cong\lim_{\leftarrow\mathbf{I}}\mathscr{B}(F(A),D)\tag{6.14}
$$

$$
\phantom{\mathscr{A}\left(A,G\left(\lim_{\leftarrow\mathbf{I}}D\right)\right)}\cong\lim_{\leftarrow\mathbf{I}}\mathscr{A}(A,G\circ D)\tag{6.15}
$$

$$
\phantom{\mathscr{A}\left(A,G\left(\lim_{\leftarrow\mathbf{I}}D\right)\right)}\cong\operatorname{Cone}(A,G\circ D)\tag{6.16}
$$

这些同构关于 $A\in\mathscr{A}$ 自然。这里，同构 (6.13) 来自伴随性，(6.14) 来自可表函子保持极限，(6.15) 再次来自伴随性，而 (6.16) 来自引理 6.2.1。因此，$G\left(\lim_{\leftarrow\mathbf{I}}D\right)$ 表示 $\operatorname{Cone}(-,G\circ D)$；也就是说，它是 $G\circ D$ 的极限。$\square$

**例 6.3.2** 从代数的范畴到 $\mathbf{Set}$ 的遗忘函子有左伴随，但几乎都没有右伴随。相应地，它们保持所有极限，却很少保持所有余极限。

**例 6.3.3** 每个集合 $B$ 都给出从 $\mathbf{Set}$ 到 $\mathbf{Set}$ 的函子之间的伴随关系 $(-\times B)\dashv(-)^B$（例 2.1.6）。所以，$-\times B$ 保持余极限，$(-)^B$ 保持极限。特别地，$-\times B$ 保持有限和，$(-)^B$ 保持有限积，从而给出同构

$$
0\times B\cong0,\qquad(A_1+A_2)\times B\cong(A_1\times B)+(A_2\times B),\tag{6.17}
$$

$$
1^B\cong1,\qquad(A_1\times A_2)^B\cong A_1^B\times A_2^B.\tag{6.18}
$$

它们与通常的算术规则相对应。（另见例 6.2.9，以及第 69 页的“关于算术的题外话”。）事实上，即使我们只对有限集知道 (6.17) 和 (6.18)，只要在两边取基数，就恰好得到这些通常的规则。毕竟，自然数就是有限集的同构类。

**例 6.3.4** 给定有所有 $\mathbf{I}$ 形状的极限的范畴 $\mathscr{A}$，我们有伴随关系

![对角函子与极限函子的伴随关系](/library/volume-87/diagrams/pdf-0167-limit-adjunction.png)

（命题 6.1.4）。因此，$\lim_{\leftarrow\mathbf{I}}$ 保持极限，或者<span class="original-page-anchor" id="pdf-page-168" aria-hidden="true"></span>等价地说，$\mathbf{I}$ 形状的极限与（所有）极限可交换。这给出了极限与极限可交换（命题 6.2.8）的另一个证明，至少在该范畴具有所涉及的一种形状的所有极限时如此。

**例 6.3.5** 定理 6.3.1 常被用来证明某个函子*没有*伴随。例如，例 2.1.3(e) 声称，遗忘函子 $U:\mathbf{Field}\to\mathbf{Set}$ 没有左伴随。现在我们可以证明这一点。若 $U$ 有左伴随 $F:\mathbf{Set}\to\mathbf{Field}$，那么 $F$ 就保持余极限，特别是保持始对象。因此，$F(\varnothing)$ 就是 $\mathbf{Field}$ 的始对象。但 $\mathbf{Field}$ 没有始对象，因为不同特征的域之间没有态射。关于伴随不存在的更多例子，可见练习 6.3.21。

### 伴随函子定理

每个有左伴随的函子都保持极限，但单凭保持极限并不能保证左伴随存在。例如，设 $\mathscr{B}$ 是任意范畴。唯一函子 $\mathscr{B}\to\mathbf{1}$ 总保持极限，但根据例 2.1.9，只有当 $\mathscr{B}$ 有始对象时，它才有左伴随。

另一方面，如果有保持极限的函子 $G:\mathscr{B}\to\mathscr{A}$，*并且 $\mathscr{B}$ 有所有极限*，那么 $G$ 很有可能有左伴随。这仍然并非总是成立，但反例更难寻找。例如（再次取 $\mathscr{A}=\mathbf{1}$），你能找到一个有所有极限却没有始对象的范畴 $\mathscr{B}$ 吗？

具有所有极限这一条件如此重要，以至于有一个专门的词来称呼它：

**定义 6.3.6** 如果一个范畴有所有极限，就称它是**完备的**（或者，准确地说，是**小完备的**）。

有各种称为伴随函子定理的结果，它们都具有如下形式：

> 设 $\mathscr{A}$ 是范畴，$\mathscr{B}$ 是完备范畴，$G:\mathscr{B}\to\mathscr{A}$ 是函子。假设 $\mathscr{A}$、$\mathscr{B}$ 和 $G$ 满足某些进一步的条件。那么

$$
G\text{ 有左伴随}\quad\Longleftrightarrow\quad G\text{ 保持极限}.
$$

正向蕴含直接来自定理 6.3.1。这里我们关注的是反向蕴含。

通常，这些“进一步的条件”涉及小集族与<span class="original-page-anchor" id="pdf-page-169" aria-hidden="true"></span>大集族的区别。但有一个特殊情形，其中这些复杂因素都消失了，我将用它来解释伴随函子定理的证明所依据的主要思想。这就是范畴 $\mathscr{A}$ 和 $\mathscr{B}$ 都是偏序集的情形。

正如我们在第 5.1 节看到的，偏序集中的极限就是交。更精确地说，如果 $D:\mathbf{I}\to\mathbf{B}$ 是偏序集 $\mathbf{B}$ 中的图表，那么

$$
\lim_{\leftarrow\mathbf{I}}D=\bigwedge_{I\in\mathbf{I}}D(I),
$$

且一边有定义，当且仅当另一边有定义。所以，偏序集完备，当且仅当每个子集都有交。类似地，偏序集之间的映射 $G:\mathbf{B}\to\mathbf{A}$ 保持极限，当且仅当对每个有交的 $\mathbf{B}$ 中的元素族 $(B_i)_{i\in I}$，都有

$$
G\left(\bigwedge_{i\in I}B_i\right)=\bigwedge_{i\in I}G(B_i).
$$

现在我们证明：对偏序集，有一种最简单的伴随函子定理，完全没有任何“进一步的条件”。

**命题 6.3.7（偏序集的伴随函子定理）** 设 $\mathbf{A}$ 是偏序集，$\mathbf{B}$ 是完备偏序集，$G:\mathbf{B}\to\mathbf{A}$ 是保序映射。那么

$$
G\text{ 有左伴随}\quad\Longleftrightarrow\quad G\text{ 保持交}.
$$

**证明** 假设 $G$ 保持交。根据推论 2.3.7，只需证明：对每个 $A\in\mathbf{A}$，逗号范畴 $(A\Rightarrow G)$ 都有始对象。设 $A\in\mathbf{A}$。那么 $(A\Rightarrow G)$ 是偏序集，具体而言，它就是 $\{B\in\mathbf{B}\mid A\le G(B)\}$，其序关系继承自 $\mathbf{B}$。我们必须证明 $(A\Rightarrow G)$ 有最小元素。

由于 $\mathbf{B}$ 完备，交 $\bigwedge_{B\in\mathbf{B}:\ A\le G(B)}B$ 在 $\mathbf{B}$ 中存在。这是 $(A\Rightarrow G)$ 的所有元素的交，所以只需证明这个交本身是 $(A\Rightarrow G)$ 的元素。事实上，由于 $G$ 保持交，我们有

$$
G\left(\bigwedge_{B\in\mathbf{B}:\ A\le G(B)}B\right)=\bigwedge_{B\in\mathbf{B}:\ A\le G(B)}G(B)\ge A,
$$

正如所需。$\square$

在推论 2.3.7 的一般情形下，$(A\Rightarrow G)$ 的始对象是二元组 $\bigl(F(A),A\xrightarrow{\eta_A}GF(A)\bigr)$，其中 $F$ 是左伴随，$\eta$ 是单位态射。所以，在命题 6.3.7 中，左伴随 $F$ 由下式给出：

$$
F(A)=\bigwedge_{B\in\mathbf{B}:\ A\le G(B)}B.\tag{6.19}
$$

<span class="original-page-anchor" id="pdf-page-170" aria-hidden="true"></span>

**例 6.3.8** 考察命题 6.3.7 中 $\mathbf{A}=\mathbf{1}$ 的情形。唯一函子 $G:\mathbf{B}\to\mathbf{1}$ 自动保持交，而正如上面所指出的，$G$ 的左伴随就是 $\mathbf{B}$ 的始对象。所以，当 $\mathbf{A}=\mathbf{1}$ 时，该命题说的是：完备偏序集有最小元素。这并非完全显然，因为完备性意味着所有交都存在，而最小元素却是空*并*。

根据 (6.19)，$\mathbf{B}$ 的最小元素是 $\bigwedge_{B\in\mathbf{B}}B$。因此，最小元素不仅是函子 $\varnothing\to\mathbf{B}$ 的余极限，也是恒等函子 $\mathbf{B}\to\mathbf{B}$ 的极限。

“并”的同义词“最小上界”提示了一个定理：有所有交的偏序集也有所有并。事实上，给定有所有交的偏序集 $\mathbf{B}$，$\mathbf{B}$ 的一个子集的并，就是它的所有上界的交：这的确就是字面意义上的最小上界。

现在试着将命题 6.3.7 从偏序集推广到范畴。我们从完备范畴 $\mathscr{B}$ 到范畴 $\mathscr{A}$ 的保持极限的函子 $G$ 出发。在偏序集的情形中，对每个 $A\in\mathscr{A}$，都有包含映射 $P_A:(A\Rightarrow G)\hookrightarrow\mathbf{B}$，而我们已经证明左伴随 $F$ 由下式给出：

$$
F(A)=\lim_{\leftarrow(A\Rightarrow G)}P_A.\tag{6.20}
$$

在一般情形下，与包含函子对应的是投影函子

$$
\begin{array}{rccc}
P_A:&(A\Rightarrow G)&\to&\mathscr{B}\\
&\bigl(B,A\xrightarrow{f}G(B)\bigr)&\mapsto&B.
\end{array}\tag{6.21}
$$

偏序集的情形提示，在一般情形下，式 (6.20) 或许可以定义 $G$ 的左伴随 $F$。确实，可以证明：如果 $\mathscr{B}$ 中的这个极限存在，并被 $G$ 保持，那么 (6.20) 的确给出左伴随（Mac Lane (1971) 的定理 X.1.2）。

这似乎表明，我们的伴随函子定理能从偏序集顺利推广到任意范畴，无须进一步的条件。但事实并非如此，其原因相当微妙。

如果稍微放宽术语，这些原因就更容易解释。在定义极限时，我们纳入了形状范畴 $\mathbf{I}$ 是小范畴这一条件。不过，极限的定义对任意范畴 $\mathbf{I}$ 都有意义。在这段讨论中，我们需要用到这个涵盖范围更广的极限概念，所以暂且搁置“极限的形状范畴 $\mathbf{I}$ 总是小范畴”这一约定。

现在，在上面（定义 6.3.6 之后）陈述的伴随函子定理的模板中，我们只要求 $\mathscr{B}$ 具有、并且 $G$ 保持*小*极限。但是<span class="original-page-anchor" id="pdf-page-171" aria-hidden="true"></span>如果 $\mathscr{B}$ 是大范畴，那么 $(A\Rightarrow G)$ 也可能是大范畴，因为要指定 $(A\Rightarrow G)$ 中的对象或态射，我们就必须指定（除其他内容之外）$\mathscr{B}$ 中的对象或态射。因此，定义左伴随的极限 (6.20) 不一定是小极限。于是，我们无法保证这个极限在 $\mathscr{B}$ 中存在，也无法保证它被 $G$ 保持。这说明，由 (6.20)“定义”的函子 $F$ 可能根本没有定义，更不用说成为左伴随了。

（如果读者觉得关于小集族与大集族的推理难以理解，可以将其与有限集族和无限集族作比较。例如，如果 $\mathscr{B}$ 是有限范畴，而 $\mathscr{A}$ 的 hom 集都是有限的，那么 $(A\Rightarrow G)$ 也是有限的；否则，$(A\Rightarrow G)$ 可能是无限的。）

命题 6.3.7 仍然成立，因为那里讨论的是偏序*集*，它们作为范畴是小的。我们或许希望将其从偏序集推广到任意小范畴，因为刚才描述的问题只影响大范畴。但这实际上不会带来多少收获，因为事实上，完备偏序集是*仅有的*完备小范畴（练习 6.3.23）。

另一种办法是，假设 $\mathscr{B}$ 具有、而 $G$ 保持*所有*（可能是大的）极限，以挽救这个论证。但这也无济于事：这样的范畴 $\mathscr{B}$ 几乎不存在。

因此，情况变得更加复杂。最著名的各个伴随函子定理都施加了进一步的条件，由这些条件可知，大极限 $\lim_{\leftarrow(A\Rightarrow G)}P_A$ 可以通过某种巧妙方式替换成小极限。这样，就能继续上述论证。

两个最著名的伴随函子定理分别称为“一般”定理和“特殊”定理。它们的精确陈述与证明，或许不如它们的推论那么重要。

**定义 6.3.9** 设 $\mathscr{C}$ 是范畴。$\mathscr{C}$ 中的**弱始集**是一个对象集合 $\mathbf{S}$，其性质是：对每个 $C\in\mathscr{C}$，都存在元素 $S\in\mathbf{S}$ 以及态射 $S\to C$。

注意，$\mathbf{S}$ 必须是集合，也就是说，必须是小的。因此，弱始集的存在是一种大小限制。这类大小限制可与代数中的有限性条件相比。

**定理 6.3.10（一般伴随函子定理）** 设 $\mathscr{A}$ 是范畴，$\mathscr{B}$ 是完备范畴，$G:\mathscr{B}\to\mathscr{A}$ 是函子。假设 $\mathscr{B}$ 是局部小范畴，并且对每个 $A\in\mathscr{A}$，范畴 $(A\Rightarrow G)$ 都有弱始集。那么

$$
G\text{ 有左伴随}\quad\Longleftrightarrow\quad G\text{ 保持极限}.
$$

**证明** 见附录。$\square$

<span class="original-page-anchor" id="pdf-page-172" aria-hidden="true"></span>

**例 6.3.11** 一般伴随函子定理（GAFT）表明：对任意代数的范畴 $\mathscr{B}$（$\mathbf{Grp}$、$\mathbf{Vect}_k$、$\ldots$），遗忘函子 $U:\mathscr{B}\to\mathbf{Set}$ 都有左伴随。事实上，我们在例 5.1.23 中看到 $\mathscr{B}$ 有所有极限，在例 5.3.4 中看到 $U$ 保持这些极限。此外，$\mathscr{B}$ 是局部小范畴。要应用 GAFT，现在只需检验：对每个 $A\in\mathbf{Set}$，逗号范畴 $(A\Rightarrow U)$ 都有弱始集。这需要一点基数算术，此处略去；见练习 6.3.24。

所以，GAFT 告诉我们，例如，自由群函子存在。在例 1.2.4(a) 和 2.1.3(b) 中，我们已开始看到，显式构造生成集 $A$ 上的自由群是多么棘手。必须先定义“形式表达式”的集合（例如 $x^{-1}yx^2zy^{-3}$，其中 $x,y,z\in A$），然后说明两个这样的表达式等价是什么意思（使 $x^{-2}x^5y$ 与 $x^3y$ 等价），然后将 $F(A)$ 定义为所有等价类的集合，再定义群结构、检验群公理，最后证明所得群具有要求的泛性质。但借助 GAFT，我们可以完全避开这些复杂步骤。

代价是，GAFT 不会给出自由群（或更一般的左伴随）的显式描述。当人们说“显式地”知道某个对象时，通常是指知道它的元素。对象的元素是*进入*该对象的态射，而我们无法掌握进入 $F(A)$ 的态射：由于 $F$ 是左伴随，我们所知道的是*从* $F(A)$ *出发*的态射。这就是左伴随的显式描述往往难以获得的原因。

**例 6.3.12** 更一般地，GAFT 保证代数的范畴之间的遗忘函子，例如

$$
\mathbf{Ab}\to\mathbf{Grp},\quad\mathbf{Grp}\to\mathbf{Mon},\quad\mathbf{Ring}\to\mathbf{Mon},\quad\mathbf{Vect}_{\mathbb{C}}\to\mathbf{Vect}_{\mathbb{R}},
$$

都有左伴随。（其中一些在例 2.1.3 中有描述。）之所以说“更一般地”，是因为按照注 2.1.4 的意义，$\mathbf{Set}$ 可以看作代数的范畴的退化例子：群、环等都是配备了满足某些等式的运算的集合，而集合就是没有配备任何运算、也不要求满足任何等式的集合。

特殊伴随函子定理（SAFT）的假设比 GAFT 严格得多，适用范围也窄得多。它的主要优点是去除了弱始集的条件。事实上，它去除了对函子 $G$ 的*所有*进一步条件。

**定理 6.3.13（特殊伴随函子定理）** 设 $\mathscr{A}$ 是范畴，$\mathscr{B}$ 是完备范畴，$G:\mathscr{B}\to\mathscr{A}$ 是函子。假设 $\mathscr{A}$ 和 $\mathscr{B}$<span class="original-page-anchor" id="pdf-page-173" aria-hidden="true"></span>都是局部小范畴，并且 $\mathscr{B}$ 满足某些进一步的条件。那么

$$
G\text{ 有左伴随}\quad\Longleftrightarrow\quad G\text{ 保持极限}.
$$

精确陈述及证明可见 Mac Lane (1971) 第 V.8 节。

**例 6.3.14** 下面是 SAFT 的经典应用。设 $\mathbf{CptHff}$ 是紧 Hausdorff 空间的范畴，$U:\mathbf{CptHff}\to\mathbf{Top}$ 是遗忘函子。SAFT 告诉我们，$U$ 有左伴随 $F$，它以一种典范方式将任何空间变成紧 Hausdorff 空间。

这个左伴随的存在远非显然，而检验 SAFT 的假设（或者用任何其他方式构造 $F$）需要拓扑学中的一些深刻定理。给定空间 $X$，所得紧 Hausdorff 空间 $F(X)$ 称为它的 **Stone–Čech 紧化**。只要 $X$ 满足一些较弱的分离条件，这个伴随关系在 $X$ 处的单位就是一个嵌入，因此，$UF(X)$ 包含 $X$ 作为子空间。

SAFT 的另一个优点是，可以从其证明中提取左伴随的相当明确的公式。在这里，它告诉我们：$F(X)$ 是典范映射

$$
X\to[0,1]^{\mathbf{Top}(X,[0,1])}
$$

的像的闭包，其中陪域是 $\mathbf{Top}$ 中 $[0,1]$ 的一个幂。

### 笛卡尔闭范畴

我们已经看到，对每个集合 $B$，都有伴随关系 $(-\times B)\dashv(-)^B$（例 2.1.6）；对每个范畴 $\mathscr{B}$，也都有伴随关系 $(-\times\mathscr{B})\dashv[\mathscr{B},-]$（注 4.1.23(c)）。

**定义 6.3.15** 如果范畴 $\mathscr{A}$ 有有限积，并且对每个 $B\in\mathscr{A}$，函子 $-\times B:\mathscr{A}\to\mathscr{A}$ 都有右伴随，就称 $\mathscr{A}$ 是**笛卡尔闭的**。

我们将这个右伴随写作 $(-)^B$，并且对 $C\in\mathscr{A}$，称 $C^B$ 为**指数对象**。可以将 $C^B$ 看作从 $B$ 到 $C$ 的态射所组成的空间。伴随性说明：对所有 $A,B,C\in\mathscr{A}$，有

$$
\mathscr{A}(A\times B,C)\cong\mathscr{A}(A,C^B),
$$

且关于 $A$ 和 $C$ 自然。事实上，该同构也关于 $B$ 自然；这一点自动成立。

**例 6.3.16** $\mathbf{Set}$ 是笛卡尔闭的；$C^B$ 就是函数集 $\mathbf{Set}(B,C)$。

**例 6.3.17** $\mathbf{CAT}$ 是笛卡尔闭的；$\mathscr{C}^{\mathscr{B}}$ 就是函子范畴 $[\mathscr{B},\mathscr{C}]$。

<span class="original-page-anchor" id="pdf-page-174" aria-hidden="true"></span>

在任何有有限和的笛卡尔闭范畴中，例 6.3.3 的同构 (6.17) 和 (6.18) 都成立，理由与该例中的相同。因此，笛卡尔闭范畴的对象具有与自然数类似的算术。这一想法可以向几个有趣的方向发展，不过这里我们只指出：这些同构提供了一种证明范畴*不是*笛卡尔闭的方法。

**例 6.3.18** 对任何域 $k$，$\mathbf{Vect}_k$ 都不是笛卡尔闭的。它确实有有限积，正如例 5.1.5 中所见：二元积就是直和 $\oplus$，而终对象是平凡向量空间 $\{0\}$，它同时也是始对象。但如果 $\mathbf{Vect}_k$ 是笛卡尔闭的，那么式 (6.17) 就会成立，于是对所有向量空间 $B$，都有 $\{0\}\oplus B\cong\{0\}$。这显然不成立。

**注 6.3.19** 对任意向量空间 $V$ 和 $W$，线性映射组成的集合 $\mathbf{Vect}_k(V,W)$ 本身也可以赋予向量空间结构，如例 1.2.12 所示。现在将这个向量空间记为 $[V,W]$。

既然指数对象应当是“态射空间”，你可能会猜想 $\mathbf{Vect}_k$ 是笛卡尔闭的，以 $[-,-]$ 作为指数对象。我们刚刚看到，这不可能成立。不过，线性映射 $U\to[V,W]$ 实际上对应于*双*线性映射 $U\times V\to W$，或者等价地，对应于线性映射 $U\otimes V\to W$。用专业术语来说，$\mathbf{Vect}_k$ 是“幺半闭范畴”的一个例子。这类范畴类似于笛卡尔闭范畴，不过，其中的笛卡尔积（范畴积）被另一种称为“积”的运算所替代；在这里，就是向量空间的张量积。

对任意集合 $I$，积范畴 $\mathbf{Set}^I$ 都是笛卡尔闭的，原因仅仅是 $\mathbf{Set}$ 是笛卡尔闭的。（$\mathbf{Set}^I$ 中的指数对象和积一样，都逐点计算。）换言之，只要 $\mathbf{A}$ 是离散的，$[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 就是笛卡尔闭的。现在我们要证明，事实上，对任意小范畴 $\mathbf{A}$，$[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 都是笛卡尔闭的。

为证明这一点，先来作一个思想实验。记 $\hat{\mathbf{A}}=[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$。如果 $\hat{\mathbf{A}}$ *是*笛卡尔闭的，其中的指数对象应当是什么？换言之，给定预层 $Y$ 和 $Z$，$Z^Y$ 必须是什么，才能使

$$
\hat{\mathbf{A}}(X,Z^Y)\cong\hat{\mathbf{A}}(X\times Y,Z)\tag{6.22}
$$

对所有预层 $X$ 成立？如果这对所有预层 $X$ 成立，那么特别地，在 $X$ 可表时也成立，所以，对所有 $A\in\mathbf{A}$，

$$
Z^Y(A)\cong\hat{\mathbf{A}}(H_A,Z^Y)\cong\hat{\mathbf{A}}(H_A\times Y,Z),
$$

其中第一步来自米田引理。这告诉了我们 $Z^Y$ 必须是什么。注意，$Z^Y(A)$ 并不像初看时可能猜想的那样，简单地等于 $Z(A)^{Y(A)}$：预层范畴中的指数对象通常*不是*逐点计算的。

<span class="original-page-anchor" id="pdf-page-175" aria-hidden="true"></span>

**定理 6.3.20** 对任意小范畴 $\mathbf{A}$，预层范畴 $\hat{\mathbf{A}}$ 都是笛卡尔闭的。

证明的思路如下。思想实验中的论证在 $X$ 可表时给出了同构 (6.22)。一般的预层 $X$ 未必可表，但它是可表函子的余极限，因此，我们可以由可表的情形逐步得到一般情形。

**证明** 我们知道 $\hat{\mathbf{A}}$ 有所有极限，特别是有有限积。只需再证明 $\hat{\mathbf{A}}$ 有指数对象。固定 $Y\in\hat{\mathbf{A}}$。

首先证明 $-\times Y:\hat{\mathbf{A}}\to\hat{\mathbf{A}}$ 保持余极限。（最终我们将证明 $-\times Y$ 有右伴随，由此就能推出它保持余极限；但证明它有右伴随时，我们将*使用*它保持余极限这一性质。）事实上，由于 $\hat{\mathbf{A}}$ 中的积与余极限都逐点计算，只需证明：对任意集合 $S$，函子 $-\times S:\mathbf{Set}\to\mathbf{Set}$ 保持余极限。这由 $\mathbf{Set}$ 是笛卡尔闭的这一事实推出。

对 $\mathbf{A}$ 上的每个预层 $Z$，令 $Z^Y$ 为由下式定义的预层：

$$
Z^Y(A)=\hat{\mathbf{A}}(H_A\times Y,Z)
$$

（对所有 $A\in\mathbf{A}$）。这定义了函子 $(-)^Y:\hat{\mathbf{A}}\to\hat{\mathbf{A}}$。

我断言 $(-\times Y)\dashv(-)^Y$。设 $X,Z\in\hat{\mathbf{A}}$。用 $P:\mathbf{E}(X)\to\mathbf{A}$ 表示投影（如定义 6.2.16 中所述），并记 $H_P=H_\bullet\circ P$。那么

$$
\hat{\mathbf{A}}(X,Z^Y)\cong\hat{\mathbf{A}}\left(\lim_{\rightarrow\mathbf{E}(X)}H_P,Z^Y\right)\tag{6.23}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\lim_{\leftarrow\mathbf{E}(X)^{\mathrm{op}}}\hat{\mathbf{A}}(H_P,Z^Y)\tag{6.24}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\lim_{\leftarrow\mathbf{E}(X)^{\mathrm{op}}}Z^Y(P)\tag{6.25}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\lim_{\leftarrow\mathbf{E}(X)^{\mathrm{op}}}\hat{\mathbf{A}}(H_P\times Y,Z)\tag{6.26}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\hat{\mathbf{A}}\left(\lim_{\rightarrow\mathbf{E}(X)}(H_P\times Y),Z\right)\tag{6.27}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\hat{\mathbf{A}}\left(\left(\lim_{\rightarrow\mathbf{E}(X)}H_P\right)\times Y,Z\right)\tag{6.28}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\hat{\mathbf{A}}(X\times Y,Z)\tag{6.29}
$$

这些同构关于 $X$ 和 $Z$ 自然。其中，(6.23) 和 (6.29) 来自定理 6.2.17；(6.24) 和 (6.27) 来自可表函子保持极限（以注 6.2.3 中的改述形式使用）；(6.25) 来自米田引理；(6.26) 来自 $Z^Y$ 的定义；(6.28) 则来自 $-\times Y$ 保持余极限。$\square$

这个结果可以看作通往拓扑斯理论之路上的一步。拓扑斯是一个<span class="original-page-anchor" id="pdf-page-176" aria-hidden="true"></span>具有某些特殊性质的范畴。拓扑斯理论以一种非凡的方式，将逻辑与几何中的重要方面统一起来。

例如，拓扑斯可以看作一个“集合宇宙”：$\mathbf{Set}$ 是最基本的拓扑斯例子，而每个拓扑斯都有足够多与 $\mathbf{Set}$ 相同的特征，使我们能把它的对象当作某种奇异的集合来推理。另一方面，拓扑斯也可以看作广义的拓扑空间：每个空间都会给出一个拓扑斯（即该空间上的层的范畴），而该空间的拓扑性质可以重新解释为其相应拓扑斯的范畴性质，这种解释很有用。

按照定义，拓扑斯是有有限极限、并且还满足一个性质的笛卡尔闭范畴，这个额外性质就是存在所谓的子对象分类子。例如，双元素集 $2$ 是 $\mathbf{Set}$ 的子对象分类子；非正式地说，这意味着集合 $A$ 的子集与态射 $A\to2$ 一一对应。练习 6.3.26 和 6.3.27 给出了子对象分类子的正式定义，然后引导你证明 $\mathbf{Set}$，以及更一般的每个预层范畴，都是拓扑斯。

### 练习

**6.3.21** (a) 证明遗忘函子 $U:\mathbf{Grp}\to\mathbf{Set}$ 没有右伴随。

(b) 证明练习 3.2.16 中的伴随链 $C\dashv D\dashv O\dashv I$ 无法向任何一个方向继续延伸。

(c) 练习 2.1.17 中的伴随链能否向某个方向继续延伸？

**6.3.22** 设 $\mathscr{A}$ 是局部小范畴。对函子 $U:\mathscr{A}\to\mathbf{Set}$，考虑如下三个条件：(A) $U$ 有左伴随；(R) $U$ 可表；(L) $U$ 保持极限。

(a) 证明 (A) $\Longrightarrow$ (R) $\Longrightarrow$ (L)。

(b) 证明：若 $\mathscr{A}$ 有和，则 (R) $\Longrightarrow$ (A)。

（如果 $\mathscr{A}$ 满足特殊伴随函子定理的假设，那么还有 (L) $\Longrightarrow$ (A)，因此，这三个条件等价。）

**6.3.23** (a) 证明每个预序集都（作为范畴）等价于某个偏序集。

(b) 设 $\mathscr{A}$ 是有所有小积的范畴。假设 $\mathscr{A}$ 不是预序，因此，$\mathscr{A}$ 中存在一对平行态射

![从 A 到 B 的平行态射 f 与 g](/library/volume-87/diagrams/pdf-0176-parallel-pair.png)

满足<span class="original-page-anchor" id="pdf-page-177" aria-hidden="true"></span>$f\ne g$。通过对每个集合 $I$ 考察态射 $A\to B^I$，证明 $\mathscr{A}$ 不是小范畴。

(c) 推出每个有小积的小范畴都等价于某个完备偏序集。

(d) 调整上述论证，证明每个有有限积的有限范畴都等价于某个完备偏序集。

**6.3.24** 一般伴随函子定理最重要的应用，可能就是证明代数的范畴之间的遗忘函子有左伴随（例 6.3.11）。利用一些基数算术，就可以检验其假设。下面是一个典型例子。

(a) 设 $A$ 是集合。证明：对任意群 $G$ 以及 $G$ 中的元素族 $(g_a)_{a\in A}$，由 $\{g_a\mid a\in A\}$ 生成的 $G$ 的子群，其基数至多为 $\max\{|\mathbb{N}|,|A|\}$。

(b) 证明：对任意集合 $S$，基数至多为 $|S|$ 的群，其全体同构类是小的。

(c) 设 $U:\mathbf{Grp}\to\mathbf{Set}$ 是从群到集合的遗忘函子。由 (a) 和 (b) 推出：对每个集合 $A$，逗号范畴 $(A\Rightarrow U)$ 都有弱始集。

(d) 使用 GAFT 得出 $U$ 有左伴随。

**6.3.25** 设 $\mathbf{A}$ 是小的笛卡尔闭范畴。证明米田嵌入 $\mathbf{A}\to[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 保持整个笛卡尔闭结构（既保持积，也保持指数对象）。

**6.3.26** 回忆练习 5.1.40 中的子对象概念。如果对每个 $A\in\mathscr{A}$，$A$ 的子对象组成的类都是小的，也就是说，是集合，就称范畴 $\mathscr{A}$ 是**良幂的**。（我们通常遇到的范畴例子都是良幂的。）设 $\mathscr{A}$ 是有拉回的良幂范畴，用 $\operatorname{Sub}(A)$ 表示对象 $A\in\mathscr{A}$ 的子对象的集合。

(a) 由练习 5.1.42 推出：$\mathscr{A}$ 中的任意态射 $A'\xrightarrow{f}A$ 都诱导映射 $\operatorname{Sub}(f):\operatorname{Sub}(A)\to\operatorname{Sub}(A')$。

(b) 证明这确定了函子 $\operatorname{Sub}:\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}$。（提示：使用练习 5.1.35。）

(c) 对某些范畴 $\mathscr{A}$，函子 $\operatorname{Sub}$ 是可表的。$\mathscr{A}$ 的**子对象分类子**是满足 $\operatorname{Sub}\cong H_\Omega$ 的对象 $\Omega\in\mathscr{A}$。证明 $2$ 是 $\mathbf{Set}$ 的子对象分类子。

**拓扑斯**是有有限极限和子对象分类子的笛卡尔闭范畴。你刚刚完成了 $\mathbf{Set}$ 是拓扑斯的证明。

<span class="original-page-anchor" id="pdf-page-178" aria-hidden="true"></span>

**6.3.27** 本练习接续上一题，最后将证明每个预层范畴都是拓扑斯。设 $\mathbf{A}$ 是小范畴。

(a) 仿照定理 6.3.20 陈述之前的思想实验，找出 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 的子对象分类子 $\Omega$ 若存在，必须是什么。

(b) 证明这个 $\Omega$ 确实是子对象分类子。

(c) 得出 $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ 是拓扑斯。
