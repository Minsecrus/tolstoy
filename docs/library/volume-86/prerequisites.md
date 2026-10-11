---
title: "逻辑预备知识"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"前言","link":"/library/volume-86/preface"}
next: {"text":"原书目录","link":"/library/volume-86/contents"}
---

# 逻辑预备知识

<span class="original-page-anchor" id="pdf-page-10" aria-hidden="true"></span>

我们假定读者熟悉集合，以及符号 $\cap$、$\cup$、$\supset$、$\subset$、$\in$。若 $A$、$B$ 是集合，我们用符号 $A\subset B$ 表示 $A$ 包含于 $B$，但允许 $A$ 与 $B$ 相等。对于 $A\supset B$ 也作类似的约定。

若 $f:A\to B$ 是从一个集合到另一个集合的映射，我们写

$$
x\mapsto f(x)
$$

来表示 $f$ 对 $A$ 的一个元素 $x$ 的作用。我们区分箭头 $\to$ 和 $\mapsto$。我们用 $f(A)$ 表示所有满足 $x\in A$ 的元素 $f(x)$ 所构成的集合。

设 $f:A\to B$ 是一个映射（mapping，也称 map）。若 $x\ne y$ 蕴含 $f(x)\ne f(y)$，则称 $f$ 为**单射**。若对于给定的 $b\in B$，存在 $a\in A$ 使得 $f(a)=b$，则称 $f$ 为**满射**。若 $f$ 既是满射又是单射，则称它为**双射**。

若集合 $B$ 的子集 $A$ 满足 $A\ne B$，则称 $A$ 为 $B$ 的**真子集**。

设 $f:A\to B$ 是一个映射，$A'$ 是 $A$ 的一个子集。$f$ 在 $A'$ 上的限制，是从 $A'$ 到 $B$ 的映射，记作 $f|A'$。

若 $f:A\to B$ 和 $g:B\to C$ 是映射，则我们有复合映射 $g\circ f$，它对所有 $x\in A$ 满足 $(g\circ f)(x)=g(f(x))$。

设 $f:A\to B$ 是一个映射，$B'$ 是 $B$ 的一个子集。我们用 $f^{-1}(B')$ 表示 $A$ 中所有满足 $f(x)\in B'$ 的元素 $x\in A$ 所构成的子集，称它为 $B'$ 的**原像**。我们称 $f(A)$ 为 $f$ 的**像**。

一个**图**

$$
\begin{array}{ccc}
A & \xrightarrow{f} & B \\
{\scriptstyle h}\searrow & & \swarrow{\scriptstyle g} \\
& C &
\end{array}
$$

若满足 $g\circ f=h$，则称为**交换图**。类似地，对于一个**图**

$$
\begin{array}{ccc}
A & \xrightarrow{f} & B \\
{\scriptstyle\varphi}\downarrow & & \downarrow{\scriptstyle g} \\
C & \xrightarrow{\psi} & D
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-11" aria-hidden="true"></span>

若满足 $g\circ f=\psi\circ\varphi$，就称这个图是**交换的**。我们有时会使用更复杂的图，其中包含不同对象之间的箭头。如果对于任意两列从一个对象到另一个对象的箭头，例如

$$
A_1\xrightarrow{f_1}A_2\xrightarrow{f_2}\cdots\xrightarrow{f_{n-1}}A_n
$$

以及

$$
A_1\xrightarrow{g_1}B_2\xrightarrow{g_2}\cdots\xrightarrow{g_{m-1}}B_m=A_n,
$$

都有

$$
f_{n-1}\circ\cdots\circ f_1=g_{m-1}\circ\cdots\circ g_1,
$$

换言之，两个复合映射相等，就称这样的图是交换的。我们的图大多由上述三角形或正方形组成；要验证一个由三角形或正方形组成的图是交换的，只须验证其中每一个三角形和正方形都是交换的。

我们假定读者熟悉整数和有理数，分别记作 $\mathbf{Z}$ 和 $\mathbf{Q}$。对于书中的许多例子，我们还假定读者了解实数和复数，分别记作 $\mathbf{R}$ 和 $\mathbf{C}$。

设 $A$ 和 $I$ 是两个集合。一个以 $I$ 为指标的 $A$ 中元素的族，是指一个映射 $f:I\to A$。因此，对于每个 $i\in I$，我们都给定了一个元素 $f(i)\in A$。虽然一个族与一个映射并无区别，但我们把它看作确定了 $A$ 中的一批对象，并经常将它写成

$$
\{f(i)\}_{i\in I}
$$

或

$$
\{a_i\}_{i\in I},
$$

即以 $a_i$ 代替 $f(i)$。我们称 $I$ 为指标集。

我们假定读者知道什么是等价关系。设 $A$ 是一个带有等价关系的集合，$E$ 是 $A$ 中元素的一个等价类。我们有时希望定义一个从这些等价类到某个集合 $B$ 的映射。为了在等价类 $E$ 上定义这样一个映射 $f$，我们有时先给出它在一个元素 $x\in E$（称为 $E$ 的一个代表元）上的值，然后证明这个值与代表元 $x\in E$ 的选择无关。在这种情况下，我们说 $f$ 是**良定义的**。

我们有集合的积，例如有限积 $A\times B$ 或 $A_1\times\cdots\times A_n$，以及集合族的积。

我们将使用佐恩引理，它将在附录 2 中说明。

我们用 $\#(S)$ 表示集合 $S$ 的元素个数，也称为 $S$ 的**基数**。这个记号通常用于 $S$ 为有限集的情形。我们也写作 $\#(S)=\operatorname{card}(S)$。
