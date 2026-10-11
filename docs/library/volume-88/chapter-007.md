---
title: "第七章 范畴导论"
description: "《Introduction to Representation Theory》中文译文。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"第六章 箭图表示","link":"/library/volume-88/chapter-006"}
next: {"text":"第八章 同调代数","link":"/library/volume-88/chapter-008"}
---

# 第七章 范畴导论

<span class="original-page-anchor" id="pdf-page-185" aria-hidden="true"></span>

## 7.1. 范畴的定义

我们已经见过许多表示理论的例子，也见过许多对表示的运算，如直和、张量积、诱导、限制和反射函子等。**范畴论**提供了一个框架，让我们能够系统地讨论这些内容。

范畴论由 Saunders Mac Lane 和 Samuel Eilenberg 于 1942–1945 年间创立。这个理论相当抽象，似乎没有什么内容，因此被戏称为“抽象废话”（见第 7.10 节）。不过，它是一种灵活而有力的语言，在代数几何、拓扑、表示论等许多数学领域中已经不可或缺。

下面简要介绍范畴论，重点说明它与我们已经讨论的表示论内容有什么联系。要深入学习范畴论，读者可以参考经典著作 [McL] 等。

**定义 7.1.1。** 一个**范畴** $\mathcal C$ 由下列数据组成：

(i) 一个对象类 $\operatorname{Ob}(\mathcal C)$。

<span class="original-page-anchor" id="pdf-page-186" aria-hidden="true"></span>

(ii) 对每对对象 $X,Y\in\operatorname{Ob}(\mathcal C)$，有一个从 $X$ 到 $Y$ 的态射（或箭头）类 $\operatorname{Hom}_{\mathcal C}(X,Y)=\operatorname{Hom}(X,Y)$（对 $f\in\operatorname{Hom}(X,Y)$，也可以写成 $f:X\to Y$）。

(iii) 对任意对象 $X,Y,Z\in\operatorname{Ob}(\mathcal C)$，有一个复合映射

$$
\operatorname{Hom}(Y,Z)\times\operatorname{Hom}(X,Y)\longrightarrow\operatorname{Hom}(X,Z),\qquad(f,g)\longmapsto f\circ g.
$$

这些数据须满足以下公理：

**1.** 复合满足结合律，即 $(f\circ g)\circ h=f\circ(g\circ h)$。

**2.** 对每个 $X\in\operatorname{Ob}(\mathcal C)$，存在一个态射 $1_X\in\operatorname{Hom}(X,X)$，称为**单位态射**，使得只要相应复合有意义，就有 $1_X\circ f=f$ 和 $g\circ 1_X=g$。

**注 7.1.2。** 我们用 $X\in\mathcal C$ 代替 $X\in\operatorname{Ob}(\mathcal C)$。

**例 7.1.3。** **1.** 集合范畴 **Sets**（态射是任意映射）。

**2.** 群范畴 **Groups** 和环范畴 **Rings**（态射是同态）。

**3.** 域 $k$ 上的向量空间范畴 $\mathbf{Vect}_k$（态射是线性映射）。

**4.** 代数 $A$ 的表示范畴 $\operatorname{Rep}(A)$（态射是表示的同态）。

**5.** 拓扑空间范畴（态射是连续映射）。

**6.** 拓扑空间的同伦范畴（态射是连续映射的同伦类）。

**重要说明。** 遗憾的是，不能把这里的“类”换成更熟悉的“集合”来简化定义。这样做会排除例 7.1.3(1) 这个重要例子：众所周知，不存在由所有集合构成的集合，使用这样的集合会导致矛盾。类的精确定义，以及类与集合的确切区别，属于集合论的内容，这里无法展开讨论。好在对大多数实际用途而言（尤其在本书中），这一区别并不重要。

<span class="original-page-anchor" id="pdf-page-187" aria-hidden="true"></span>

还要说明，在许多例子中，包括例 7.1.3(1)–(6)，定义 7.1.1 的第 (ii) 项里的“类”可以换成“集合”。具有这一性质的范畴，即对任意 $X,Y$，$\operatorname{Hom}(X,Y)$ 都是集合的范畴，称为**局部小范畴**。我们遇到的许多范畴都属于这一类。

**定义 7.1.4。** 范畴 $\mathcal C$ 的一个**满子范畴**是一个范畴 $\mathcal C'$，其对象组成 $\mathcal C$ 的对象的一个子类，而且 $\operatorname{Hom}_{\mathcal C'}(X,Y)=\operatorname{Hom}_{\mathcal C}(X,Y)$。

**例 7.1.5。** 范畴 **AbelianGroups** 是范畴 **Groups** 的满子范畴。

有时，在一个局部小范畴 $\mathcal C$ 中，从 $X$ 到 $Y$ 的态射所成的 $\operatorname{Hom}(X,Y)$ 不仅是集合，还带有其他结构，例如阿贝尔群结构或某个域上的向量空间结构。此时称 $\mathcal C$ **在另一个范畴 $\mathcal D$ 上富集**。这里 $\mathcal D$ 是一个幺半范畴，也就是说，它有一种乘积运算和这一乘积下的单位对象，例如阿贝尔群范畴，或以张量积为乘积运算的向量空间范畴。这意味着，对每对 $X,Y\in\mathcal C$，$\operatorname{Hom}(X,Y)$ 都是 $\mathcal D$ 的对象，且复合 $\operatorname{Hom}(Y,Z)\times\operatorname{Hom}(X,Y)\to\operatorname{Hom}(X,Z)$ 是 $\mathcal D$ 中的态射。例如，若 $\mathcal D$ 是向量空间范畴，这意味着复合是双线性的，即它给出一个线性映射 $\operatorname{Hom}(Y,Z)\otimes\operatorname{Hom}(X,Y)\to\operatorname{Hom}(X,Z)$。更详细的讨论可见 [McL]。

**例 7.1.6。** $k$-代数 $A$ 的表示范畴 $\operatorname{Rep}(A)$ 在 $k$-向量空间范畴上富集。

## 7.2. 函子

我们想定义范畴之间的箭头。这样的箭头称为**函子**。

**定义 7.2.1。** 范畴 $\mathcal C$ 与 $\mathcal D$ 之间的一个**函子** $F:\mathcal C\to\mathcal D$ 包含：

(i) 一个映射 $F:\operatorname{Ob}(\mathcal C)\to\operatorname{Ob}(\mathcal D)$；

<span class="original-page-anchor" id="pdf-page-188" aria-hidden="true"></span>

(ii) 对每对 $X,Y\in\mathcal C$，有一个保持复合和恒等态射的映射 $F=F_{X,Y}:\operatorname{Hom}(X,Y)\to\operatorname{Hom}(F(X),F(Y))$。

函子的复合方式是显然的。此外，每个范畴都有恒等函子。

**例 7.2.2。** **1.** 只有一个对象 $X$ 的（局部小）范畴 $\mathcal C$ 与一个幺半群是同一回事。这类范畴之间的函子就是幺半群同态。

**2.** 遗忘函子

$$
\mathbf{Groups}\longrightarrow\mathbf{Sets},\qquad
\mathbf{Rings}\longrightarrow\mathbf{AbelianGroups}.
$$

**3.** 一个范畴 $\mathcal C$ 的对偶范畴记作 $\mathcal C^{\mathrm{op}}$，由原范畴将箭头方向和复合顺序反转得到。于是 $V\mapsto V^*$ 是一个函子 $\mathbf{Vect}_k\to\mathbf{Vect}_k^{\mathrm{op}}$。

**译校注：** 原书这里未说明对偶范畴的记号，译文依据作者 2024 年勘误补入 $\mathcal C^{\mathrm{op}}$。

**4.** Hom 函子：若 $\mathcal C$ 是局部小范畴，则 $Y\mapsto\operatorname{Hom}(X,Y)$ 给出函子 $\mathcal C\to\mathbf{Sets}$，$Y\mapsto\operatorname{Hom}(Y,X)$ 给出函子 $\mathcal C^{\mathrm{op}}\to\mathbf{Sets}$。

**5.** 对应 $X\mapsto\operatorname{Fun}(X,\mathbb Z)$ 是一个函子 $\mathbf{Sets}\to\mathbf{Rings}^{\mathrm{op}}$。

**6.** 设 $Q$ 是箭图。考虑范畴 $\mathcal C(Q)$，其对象是箭图的顶点，态射是顶点之间的有向路径。于是从 $\mathcal C(Q)$ 到 $\mathbf{Vect}_k$ 的函子，就是 $Q$ 在 $k$ 上的表示。

**7.** 设 $K\subset G$ 是群。我们有诱导函子 $\operatorname{Ind}_K^G:\operatorname{Rep}(K)\to\operatorname{Rep}(G)$ 和限制函子 $\operatorname{Res}_K^G:\operatorname{Rep}(G)\to\operatorname{Rep}(K)$。

**8.** 范畴的笛卡尔积有显然的定义：分别对各因子的对象类和态射类取笛卡尔积即可。直和与张量积于是给出函子 $\mathbf{Vect}_k\times\mathbf{Vect}_k\to\mathbf{Vect}_k$。此外，$V\mapsto V^{\otimes n}$、$V\mapsto S^nV$、$V\mapsto\bigwedge^nV$ 这些运算都是 $\mathbf{Vect}_k$ 上的函子。更一般地，若 $\pi$ 是 $S_n$ 的表示，则有函子 $V\mapsto\operatorname{Hom}_{S_n}(\pi,V^{\otimes n})$。这样的函子称为 **Schur 函子**。因此，不可约 Schur 函子由杨图标记。

**9.** 反射函子 $F_i^\pm:\operatorname{Rep}(Q)\to\operatorname{Rep}(\overline Q_i)$ 是箭图的表示范畴之间的函子。

<span class="original-page-anchor" id="pdf-page-189" aria-hidden="true"></span>

## 7.3. 函子的态射

范畴之间的函子有一个重要特点，使它与通常的映射或函数有所不同：两个给定范畴之间的函子本身也构成一个范畴。也就是说，两个函子之间可以定义一种非平凡的态射概念。

**定义 7.3.1.** 设 $\mathcal C,\mathcal D$ 是两个范畴，$F,G:\mathcal C\to\mathcal D$ 是它们之间的函子。**态射** $a:F\to G$（也称**自然变换**或**函子态射**）是一族以 $\mathcal C$ 的对象 $X$ 为指标的态射 $a_X:F(X)\to G(X)$，并且它关于 $X$ 具有函子性：对任意态射 $f:X\to Y$（$X,Y\in\mathcal C$），都有 $a_Y\circ F(f)=G(f)\circ a_X$。

如果存在另一个态射 $a^{-1}:G\to F$，使 $a\circ a^{-1}$ 和 $a^{-1}\circ a$ 都是恒等态射，就称态射 $a:F\to G$ 为**同构**。从 $F$ 到 $G$ 的态射集合记为 $\operatorname{Hom}(F,G)$。

**例 7.3.2.** 1. 设 $\mathbf{FVect}_k$ 是 $k$ 上有限维向量空间组成的范畴。这个范畴上的函子 $\operatorname{id}$ 与 ${}^{**}$ 同构。同构由通常的映射 $a_V:V\to V^{**}$ 给出，其定义为 $a_V(u)(f)=f(u)$，其中 $u\in V$，$f\in V^*$。但在所有向量空间组成的范畴 $\mathbf{Vect}_k$ 上，这两个函子并不同构，因为当 $V$ 是无限维向量空间时，$V$ 与 $V^{**}$ 不同构。

2. 设 $\mathbf{FVect}'_k$ 的对象是有限维 $k$-向量空间，态射是这些空间之间的同构。这个范畴上有一个到自身的函子 $F$：它把空间 $V$ 送到 $V^*$，把态射 $a$ 送到 $(a^*)^{-1}$。虽然对每个 $V$ 都有 $V\cong F(V)$，这个函子却不与恒等函子同构。原因是无法选取与 $GL(V)$ 的作用相容的同构 $V\mapsto F(V)=V^*$：作为 $GL(V)$ 的表示，$V$ 与 $V^*$ 不同构。

3. 设 $A$ 是域 $k$ 上的代数，$F:A\text{-}\mathbf{mod}\to\mathbf{Vect}_k$ 是遗忘函子。由习题 2.3.17 可知，$\operatorname{End}F=\operatorname{Hom}(F,F)=A$。

4. 范畴 $A\text{-}\mathbf{mod}$ 上恒等函子的自同态集合就是 $A$ 的中心（请验证！）。

<span class="original-page-anchor" id="pdf-page-190" aria-hidden="true"></span>

## 7.4. 范畴的等价

两个代数或几何对象同构时，通常不宜说它们相等，也就是完全是同一个对象。因为它们往往可以通过许多不同的方式对应起来，即同构的选法有很多。如果说它们相等，就容易让读者或听者误以为我们已经选定了某个具体的对应，实际上却并没有。有限维向量空间 $V$ 及其对偶空间 $V^*$ 就是一个鲜明的例子。

因此，在范畴论中，人们大多尽量避免说两个对象或两个函子相等。定义范畴之间的同构时，也应如此。

最直接的范畴同构概念可以这样定义：函子 $F:\mathcal C\to\mathcal D$ 是同构，如果存在 $F^{-1}:\mathcal D\to\mathcal C$，使 $F\circ F^{-1}$ 和 $F^{-1}\circ F$ 等于恒等函子。但这个定义并不太有用。我们或许已经能察觉这一点，因为这里对范畴中的对象，也就是函子，使用了本应避免的“相等”一词。下面给出两个“在实际使用中完全一样”却不同构的范畴，这个例子会展示上述定义的不足。

设 $\mathcal C_1$ 是最简单的范畴：$\operatorname{Ob}(\mathcal C_1)$ 只有一个对象 $X$，且 $\operatorname{Hom}(X,X)=\{1_X\}$。再设 $\mathcal C_2$ 有两个对象 $X,Y$ 和四个态射：$1_X$、$1_Y$、$a:X\to Y$、$b:Y\to X$。于是必有 $a\circ b=1_Y$，$b\circ a=1_X$。

容易验证，对任意范畴 $\mathcal D$，从 $\mathcal C_1$ 到 $\mathcal D$ 的函子同构类与从 $\mathcal C_2$ 到 $\mathcal D$ 的函子同构类之间存在自然双射；两者都可以看作 $\mathcal D$ 的对象同构类所组成的集族。这就是所谓 $\mathcal C_1$ 和 $\mathcal C_2$“在实际使用中完全一样”的意思。不过，它们并不同构，因为 $\mathcal C_1$ 只有一个对象，而 $\mathcal C_2$ 有两个对象，尽管后者的两个对象彼此同构。

这说明，我们需要一种更灵活、限制更少的范畴同构概念。为此，就要定义范畴的等价。

<span class="original-page-anchor" id="pdf-page-191" aria-hidden="true"></span>

**定义 7.4.1.** 函子 $F:\mathcal C\to\mathcal D$ 称为**范畴等价**，如果存在 $F':\mathcal D\to\mathcal C$，使 $F\circ F'$ 和 $F'\circ F$ 都与恒等函子同构。

这时称 $F'$ 为 $F$ 的**拟逆**。

特别地，上面的范畴 $\mathcal C_1$ 与 $\mathcal C_2$ 是等价的（请验证！）。

有限集范畴 $\mathbf{FSet}$ 也等价于下面这个范畴：对象是非负整数，态射由下式给出：

$$
\operatorname{Hom}(m,n)=\operatorname{Maps}(\{1,\ldots,m\},\{1,\ldots,n\}).
$$

这两个范畴同构吗？答案取决于你认为具有给定元素个数的有限集只有一个，还是有很多个。认为有很多个似乎更好，至于“有多少个”就不必追问了；这样，同构的集合就不必真的是同一个集合。不过，这终究是选择的问题。无论如何，这个问题并不怎么合理：它的答案对实际使用毫无影响，思考它只会让人头疼。

## 7.5. 可表函子

**可表函子**是范畴论中的一个基本概念。设 $\mathcal C$ 是一个局部小范畴，$F:\mathcal C\to\mathbf{Sets}$ 是函子。如果存在对象 $X\in\mathcal C$，使 $F$ 与函子 $\operatorname{Hom}(X,?)$ 同构，就称 $F$ **可表**。更确切地说，给定这样的对象 $X$ 以及同构 $\xi:F\cong\operatorname{Hom}(X,?)$ 时，就说函子 $F$ **由 $X$ 表示**，所用的同构为 $\xi$。

类似地，也可以谈论从 $\mathcal C^{\mathrm{op}}$ 到 $\mathbf{Sets}$ 的可表函子。如果这样的函子在同构意义下具有 $\operatorname{Hom}(?,X)$ 的形式，其中 $X\in\mathcal C$，就称它可表。

并非所有函子都可表；但如果表示对象 $X$ 存在，它就是唯一的。确切的说法是下面的引理。

**引理 7.5.1（Yoneda 引理）.** *如果函子 $F$ 由对象 $X$ 表示，那么 $X$ 在唯一同构的意义下唯一。也就是说，设 $X,Y$ 是 $\mathcal C$ 中的两个对象，则对任意函子同构*<span class="original-page-anchor" id="pdf-page-192" aria-hidden="true"></span>$\phi:\operatorname{Hom}(X,?)\to\operatorname{Hom}(Y,?)$，*都存在唯一的同构 $a_\phi:X\to Y$ 诱导出 $\phi$。*

**证明（概要）.** 令 $a_\phi=\phi_Y^{-1}(1_Y)$，并构造其逆 $a_\phi^{-1}=\phi_X(1_X)$，从而证明它可逆。还需验证这两个态射按两个顺序复合都得到恒等态射，这里略去。这样便证明了 $a_\phi$ 的存在性。唯一性可以直接验证。$\square$

**注 7.5.2.** 类似地，如果范畴 $\mathcal C$ 在另一个范畴 $\mathcal D$ 上丰盈，例如在阿贝尔群范畴或向量空间范畴上丰盈，也可以定义从 $\mathcal C$ 到 $\mathcal D$ 的可表函子。

**例 7.5.3.** 设 $A$ 是代数。从左 $A$-模范畴到向量空间范畴的遗忘函子可表，表示对象是秩为 $1$ 的自由模 $M=A$，也就是正则表示。但如果 $A$ 无限维，而且我们只考虑有限维模组成的范畴，那么遗忘函子通常不可表。例如，当 $A$ 是 $\mathbb Z$ 上仅在有限多个点非零的复函数所组成的代数时，情形就是如此。

## 7.6. 伴随函子

范畴论的另一个基本概念是伴随函子。

**定义 7.6.1.** 函子 $F:\mathcal C\to\mathcal D$ 和 $G:\mathcal D\to\mathcal C$ 称为一对**伴随函子**，如果对任意 $X\in\mathcal C$、$Y\in\mathcal D$，都给定一个关于 $X$ 和 $Y$ 具有函子性的同构 $\xi_{XY}:\operatorname{Hom}_{\mathcal D}(F(X),Y)\to\operatorname{Hom}_{\mathcal C}(X,G(Y))$。也就是说，给定一个函子同构 $\operatorname{Hom}(F(?),?)\to\operatorname{Hom}(?,G(?))$，其中这些函子为 $\mathcal C^{\mathrm{op}}\times\mathcal D\to\mathbf{Sets}$。这时称 $F$ 是 $G$ 的**左伴随**，$G$ 是 $F$ 的**右伴随**。

**译校注：** 原书上述同构两侧的 $\operatorname{Hom}$ 下标分别写作 $\mathcal C$、$\mathcal D$。由于 $F(X),Y$ 都是 $\mathcal D$ 的对象，而 $X,G(Y)$ 都是 $\mathcal C$ 的对象，译文按照作者官方勘误将这两个下标对调。此外，原书把函子的定义域写作 $\mathcal C\times\mathcal D$；由于 $\operatorname{Hom}$ 对第一变量逆变，此处改为 $\mathcal C^{\mathrm{op}}\times\mathcal D$。

并非每个函子都有左伴随或右伴随，但只要存在，它就是唯一的，而且可以作典范构造：如果以某种方式找到了两个这样的函子，它们之间便存在典范同构。由 Yoneda 引理很容易得到这一点，因为如果<span class="original-page-anchor" id="pdf-page-193" aria-hidden="true"></span>$F,G$ 是一对伴随函子，那么 $F(X)$ 表示函子 $Y\mapsto\operatorname{Hom}(X,G(Y))$，而 $G(Y)$ 表示函子 $X\mapsto\operatorname{Hom}(F(X),Y)$。

**注 7.6.2.** “左伴随函子”和“右伴随函子”的名称来自范畴与内积空间之间的类比。表 1 给出了范畴论与线性代数之间一些有用的对应关系，有助于理解范畴论中的许多概念。

**表 1. 范畴论与线性代数的对应关系。**

| 范畴论 | 线性代数 |
| --- | --- |
| 范畴 $\mathcal C$ | 带有非退化内积的向量空间 $V$ |
| 态射集合 $\operatorname{Hom}(X,Y)$ | $V$ 上的内积 $(x,y)$，可以不对称 |
| 对偶范畴 $\mathcal C^{\mathrm{op}}$ | 同一个空间 $V$，但交换内积的两个变量 |
| 集合范畴 $\mathbf{Sets}$ | 基域 $k$ |
| $\mathcal C$ 中的满子范畴 | $V$ 中的非退化子空间 |
| 函子 $F:\mathcal C\to\mathcal D$ | 线性算子 $f:V\to W$ |
| 函子 $F:\mathcal C\to\mathbf{Sets}$ | 线性泛函 $f\in V^*=\operatorname{Hom}(V,k)$ |
| 可表函子 | 形如 $f(v)=(u,v)$ 的线性泛函 $f\in V^*$，其中 $u\in V$ |
| Yoneda 引理 | 内积在两个变量上都非退化 |
| 并非所有函子都可表 | 若 $\dim V=\infty$，并非所有 $f\in V^*$ 都能写成 $f(v)=(u,v)$ |
| 左伴随函子和右伴随函子 | 左伴随算子和右伴随算子 |
| 伴随函子不一定存在 | 若 $\dim V=\infty$，伴随算子可能不存在 |
| 只要存在，它们就是唯一的 | 只要存在，它们就是唯一的 |
| 左伴随与右伴随可能不同 | 内积可能不对称 |

<span class="original-page-anchor" id="pdf-page-194" aria-hidden="true"></span>

**例 7.6.3.** 1. 设 $V$ 是群 $G$ 或 Lie 代数 $\mathfrak g$ 的一个有限维表示。在 $G$ 的表示范畴上，函子 $V\otimes$ 的左伴随和右伴随都是函子 $V^*\otimes$。

2. 函子 $\operatorname{Res}_K^G$ 是 $\operatorname{Ind}_K^G$ 的左伴随。这正是 Frobenius 互反性的陈述。

3. 设 $\mathbf{Assoc}_k$ 是含单位元的结合代数组成的范畴，$\mathbf{Lie}_k$ 是域 $k$ 上 Lie 代数组成的范畴。我们有函子 $L:\mathbf{Assoc}_k\to\mathbf{Lie}_k$：它把结合代数的底层空间看作 Lie 代数，其括号为 $[a,b]=ab-ba$。函子 $L$ 有左伴随，就是取 Lie 代数的泛包络代数的函子 $U$。

4. 函子 $GL_1:\mathbf{Assoc}_k\to\mathbf{Groups}$ 由 $A\mapsto GL_1(A)=A^\times$ 给出。它的左伴随是取群代数的函子 $G\mapsto k[G]$。

5. 遗忘函子 $\mathbf{Assoc}_k\to\mathbf{Vect}_k$ 的左伴随是张量代数函子 $V\mapsto TV$。如果用 $\mathbf{Comm}_k$ 表示交换代数范畴，那么遗忘函子 $\mathbf{Comm}_k\to\mathbf{Vect}_k$ 的左伴随是对称代数函子 $V\mapsto SV$。

还可以从许多不同领域举出更多例子。这些例子说明，伴随函子在数学中随处可见。

## 7.7. 阿贝尔范畴

表示论中最常见的一类范畴是阿贝尔范畴。阿贝尔范畴的标准定义比较长，这里不再给出，读者可参阅教科书 [Fr]。我们改用 Freyd–Mitchell 定理的陈述作为定义：

**定义 7.7.1.** **阿贝尔范畴**是一个在阿贝尔群范畴上丰盈的范畴，它等价于某个环 $A$ 上左模范畴 $A\text{-}\mathbf{mod}$ 的满子范畴 $\mathcal C$；并且 $\mathcal C$ 对有限直和以及态射的核、余核和像封闭。

<span class="original-page-anchor" id="pdf-page-195" aria-hidden="true"></span>

**例 7.7.2.** 代数 $A$ 上的模范畴，以及 $A$ 上的有限维模范畴，都是阿贝尔范畴。

**习题 7.7.3.** 设 $A$ 是有限生成的交换环。证明，有限生成 $A$-模组成的范畴是阿贝尔范畴。

提示：使用 Hilbert 基定理。

由这个定义可见，在阿贝尔范畴中，对任意 $X,Y$，$\operatorname{Hom}(X,Y)$ 都是阿贝尔群；复合对每个变量都是群同态。此外，还有零对象、单射态射（单态射）和满射态射（满态射）的概念，而且每个态射都有核、余核和像。

**注 7.7.4.** 定义 7.7.1 的好处是，可以借助经典代数来直观理解对象、态射、核和余核。但它也有一个很大的缺点：即使 $\mathcal C$ 是整个范畴 $A\text{-}\mathbf{mod}$，$\mathcal C$ 也不能确定环 $A$。特别地，两个不同的环可能有等价的模范畴；这样的环称为 **Morita 等价**的环。实际情况还更糟：对于许多重要的阿贝尔范畴，根本找不到自然的、甚至易于处理的环 $A$。因此，人们更愿意使用标准定义，尽管它更抽象，却没有这个缺点。

设 $k$ 是域。如果阿贝尔范畴 $\mathcal C$ 中的群 $\operatorname{Hom}_{\mathcal C}(X,Y)$ 都带有 $k$-向量空间结构，而且复合映射对每个变量都是 $k$-线性的，就称 $\mathcal C$ 是 **$k$-线性的**。特别地，例 7.7.2 中的范畴都是 $k$-线性的。

## 7.8. 复形与上同调

**定义 7.8.1.** 设 $C_i$（$i\in\mathbb Z$）是阿贝尔范畴 $\mathcal C$ 中的一列对象，$d_i:C_i\to C_{i+1}$ 是一列态射。如果任意两个相邻箭头的复合都为零，就称这列对象和态射组成一个**复形**。态射 $d_i$ 称为**微分**。[^rt-195-1] 这个复形的**上同调**为<span class="original-page-anchor" id="pdf-page-196" aria-hidden="true"></span>$H^i=\operatorname{Ker}(d_i)/\operatorname{Im}(d_{i-1})$。如果 $H^i=0$，就称复形在第 $i$ 项**正合**；如果它在每一项都正合，就称它为**正合列**。

**复形态射**的定义很直接：态射 $f:C\to D$ 是一族态射 $f_i:C_i\to D_i$，满足 $d_i\circ f_i=f_{i+1}\circ d_i$。显然，这样的态射可以复合，因而 $\mathcal C$ 中所有复形构成一个范畴，记为 $\operatorname{Compl}(\mathcal C)$。

特别地，可以考虑阿贝尔群、向量空间、环上的模等组成的复形。这时，$\operatorname{Ker}(d_i)$ 的元素称为 **$i$-上闭链**，$\operatorname{Im}(d_{i-1})$ 的元素称为 **$i$-上边缘**，$H^i(C)$ 的元素称为**第 $i$ 阶上同调类**。这些术语来自拓扑学。也因此，正合列又称为**无环复形**，因为这样的复形没有非平凡的上闭链，也就是每个上闭链都是上边缘。

我们经常考虑在一个方向或两个方向有界的复形，即当 $i\gg0$、$i\ll0$ 或两种情况都发生时，对象 $C_i$ 为零。这时，在复形有界的那一侧写一个零。例如，一个两端有界且有 $n+1$ 项的复形写成

$$
0\to C_0\to C_1\to\cdots\to C_n\to0.
$$

**定义 7.8.2.** **短正合列**是形如

$$
0\to X\to Y\to Z\to0
$$

的正合列。

显然，$0\to X\to Y\to Z\to0$ 是短正合列，当且仅当 $X\to Y$ 是单射，$Y\to Z$ 是满射，并且诱导的映射 $Y/X\to Z$ 是同构。换句话说，短正合列对应于用 $X$ 扩张 $Z$。

**例 7.8.3.** 取通常的态射，序列 $0\to X\to X\oplus Z\to Z\to0$ 是短正合列。这样的序列称为**分裂**的短正合列，它对应于用 $X$ 对 $Z$ 作的平凡扩张。

<span class="original-page-anchor" id="pdf-page-197" aria-hidden="true"></span>

**练习 7.8.4.** 证明，任意向量空间正合列都同构于若干形如

$$
0\to V\to V\to0
$$

的复形的直和，其中 $V$ 位于第 $i$ 和第 $i+1$ 项，映射 $V\to V$ 是恒等映射。特别地，每个向量空间短正合列都分裂。在阿贝尔群范畴中，这一结论还成立吗？

**习题 7.8.5.** 设 $D_\bullet$ 是阿贝尔群复形，其微分为 $d_i$，$i\in\mathbb Z$。设 $C_\bullet$ 是 $D_\bullet$ 的子复形，即一族子群 $C_i\subset D_i$，满足 $d_i(C_i)\subset C_{i+1}$。再设 $E_\bullet=D_\bullet/C_\bullet$ 是商复形，即 $E_i=D_i/C_i$，微分由 $d_i$ 诱导。

如下定义同态 $c_i:H^i(E)\to H^{i+1}(C)$。给定 $x\in H^i(E)$，在 $E_i$ 中选取 $x$ 的一个代表元 $x'$，再将 $x'$ 提升为 $D_i$ 中的元素 $x''$。令 $y'=dx''\in D_{i+1}$；这里简化记号，把 $d_i$ 记作 $d$。由于 $dx'=0$，有 $y'=dx''\in C_{i+1}$。此外，$dy'=d^2x''=0$。因此，$y'$ 代表一个元素 $y\in H^{i+1}(C)$。我们定义 $c_i(x)=y$。

(i) 证明 $c_i$ 定义良好，即 $c_i(x)$ 不依赖于 $x'$ 和 $x''$ 的选取。

(ii) 证明下面的序列正合：

$$
\cdots H^{i-1}(E)\to H^i(C)\to H^i(D)\to H^i(E)\to H^{i+1}(C)\cdots,\tag{7.8.1}
$$

其中第一个映射是 $c_{i-1}$，中间两个映射由 $C_i\to D_i\to E_i$ 诱导，最后一个映射是 $c_i$。

**定义 7.8.6.** 映射 $c_i$ 称为**连接同态**，序列 (7.8.1) 称为**上同调长正合列**。

**习题 7.8.7.** 设 $C_\bullet$ 和 $D_\bullet$ 是交换环 $A$ 上的模复形。用下式定义张量积复形 $(C\otimes D)_\bullet$：

$$
(C\otimes D)_i=\bigoplus_{j+m=i}C_j\otimes_A D_m,
$$

其微分为

$$
d_i^{C\otimes D}\big|_{C_j\otimes D_m}=d_j^C\otimes1+(-1)^j\cdot1\otimes d_m^D.
$$

<span class="original-page-anchor" id="pdf-page-198" aria-hidden="true"></span>

(i) 证明它是一个复形。

现在假设 $A=k$ 是域。

(ii) 证明，如果 $C$ 或 $D$ 是正合列，那么 $C\otimes D$ 也是正合列。

提示：使用练习 7.8.4 中的分解。

(iii) 证明，任意复形 $C$ 都可以看作一个正合列与一个由 $H^i(C)$ 组成、微分全为零的复形的直和，并且可以使诱导的同构 $H^i(C)\to H^i(C)$ 为恒等映射。

(iv) 证明存在自然的向量空间同构

$$
H^i(C\otimes D)\cong\bigoplus_{j+m=i}H^j(C)\otimes H^m(D).
$$

这就是 **Künneth 公式**。

## 7.9. 正合函子

**定义 7.9.1.** 两个阿贝尔范畴之间的函子 $F$ 称为**加性函子**，如果它在 Hom 群上诱导群同态。对于 $k$-线性范畴，如果 $F$ 在 Hom 空间之间诱导 $k$-线性映射，就称 $F$ 为 **$k$-线性函子**。

容易证明，如果 $F$ 是加性函子，那么 $F(X\oplus Y)$ 与 $F(X)\oplus F(Y)$ 典范同构。

**例 7.9.2.** 域 $k$ 上群表示论中的函子 $\operatorname{Ind}_K^G$、$\operatorname{Res}_K^G$、$\operatorname{Hom}_G(V,?)$ 都是加性的、$k$-线性的。

**定义 7.9.3.** 阿贝尔范畴之间的加性函子 $F:\mathcal C\to\mathcal D$ 称为**左正合**的，如果对任意正合列

$$
0\to X\to Y\to Z,
$$

序列

$$
0\to F(X)\to F(Y)\to F(Z)
$$

都正合。如果对任意正合列

$$
X\to Y\to Z\to0,
$$

序列

$$
F(X)\to F(Y)\to F(Z)\to0
$$

都正合，就称 $F$ 为**右正合**的。如果 $F$ 既左正合又右正合，就称它为**正合**的。

<span class="original-page-anchor" id="pdf-page-199" aria-hidden="true"></span>

**定义 7.9.4.** 阿贝尔范畴 $\mathcal C$ 称为**半单**的，如果其中每个短正合列都分裂，即都同构于形如

$$
0\to X\to X\oplus Y\to Y\to0
$$

的序列，其中各映射取通常的映射。

**例 7.9.5.** 设 $G$ 是有限群。如果域的特征不整除 $|G|$，或者特征为 $0$，那么这个域上的 $G$-表示范畴是半单的。

注意，在半单范畴中，任何加性函子都自动既左正合又右正合。

**例 7.9.6.** (i) 函子 $\operatorname{Ind}_K^G$ 和 $\operatorname{Res}_K^G$ 都是正合的。

(ii) 函子 $\operatorname{Hom}(X,?)$ 左正合，但未必右正合。要看出它不一定右正合，只需考虑正合列

$$
0\to\mathbb Z\to\mathbb Z\to\mathbb Z/2\mathbb Z\to0
$$

并对它应用函子 $\operatorname{Hom}(\mathbb Z/2\mathbb Z,?)$。

(iii) 对右 $A$-模 $X$，左 $A$-模范畴上的函子 $X\otimes_A$ 右正合，但未必左正合。只需将上面的正合列与 $\mathbb Z/2\mathbb Z$ 作张量积，就能看出这一点。

**练习 7.9.7.** 证明，如果 $(F,G)$ 是阿贝尔范畴之间的一对加性伴随函子，那么 $F$ 右正合，$G$ 左正合。

**练习 7.9.8.** (a) 设 $Q$ 是箭图，$i\in Q$ 是源点。设 $V$ 是 $Q$ 的表示，$W$ 是 $\overline Q_i$ 的表示，其中 $\overline Q_i$ 是将 $Q$ 在顶点 $i$ 处的箭头反向后得到的箭图。证明，$\operatorname{Hom}(F_i^-V,W)$ 与 $\operatorname{Hom}(V,F_i^+W)$ 之间存在自然同构。换句话说，函子 $F_i^+$ 是 $F_i^-$ 的右伴随。

(b) 由此推出，函子 $F_i^+$ 左正合，$F_i^-$ 右正合。

<span class="original-page-anchor" id="pdf-page-200" aria-hidden="true"></span>

## 7.10. 历史插曲：Eilenberg、Mac Lane 与“一般抽象废话”

Saunders Mac Lane（1909–2005）的父亲和祖父都是公理会牧师，所以年轻的 Saunders 似乎注定也会从事宗教职业。然而，他很早就开始产生“各种神学上的疑惑和问题”。Mac Lane 后来回忆：“牧师这个职业会要求我相信一些自己并不确定的事情。”“数学却提供了另一种确定性。”有一件事他倒是十分确定：牧师的收入少得可怜，远不足以保障舒适的退休生活。因此，他决定选择“科学而非牧师”的职业道路 [33, pp. 349–350]。他在耶鲁取得学士学位，随后在芝加哥取得硕士学位。

“德国抽象代数的优雅”令 Mac Lane 深受启发；其中，环和域的概念将加法与乘法公理化。他在硕士论文中也尝试以类似方式将指数运算，以及加法和乘法公理化。在芝加哥，欠佳的教学和在他看来是“卖弄学问”的一些做法让他感到失望。他认为，那里的数学系“已经算不上真正的一流数学系了” [36, p. 152]。他回忆说，自己曾被教导向量就是一个 $n$ 元组，“而我很快就得摆脱这种认识” [33, p. 39]。Mac Lane 想写一篇逻辑学博士论文，却找不到导师，于是决定前往当时数学逻辑研究的首要中心哥廷根。

在著名 Hilbert 学派所在的哥廷根，Mac Lane 向 Hermann Weyl 学习群表示，向 Emmy Noether 学习线性结合代数。他写道：“住在哥廷根，就是沉浸在数学文化之中。”在他的回忆里，哥廷根“将研究、教学和启迪融为一体”。但即使置身于这样的环境，他也难以忽视紧张的政治气氛、27 个政党之间激烈的冲突，以及身穿纳粹褐衫制服的学生。Mac Lane 确实写了一篇逻辑学论文，却漏掉了当时发表的 Gödel 著名的不完备性定理。他的论文提炼出<span class="original-page-anchor" id="pdf-page-201" aria-hidden="true"></span>Russell 与 Whitehead 的《数学原理》中常见的证明模式，目的是简化新的证明，甚至将证明过程机械化。Mac Lane 承认，这篇论文“天真地以为，所有数学都会真的按照 Whitehead 和 Russell 的风格写出来”。1933 年，Hitler 上台时，Mac Lane 仍在哥廷根。他目睹了 Hilbert 学派遭到无情摧毁：Courant、Noether 等许多杰出的犹太数学家被解雇，曾经享有盛名的数学系变得“只剩下一副骨架”。Mac Lane 匆忙完成论文。按照哥廷根的标准，这篇论文并不出色，最后以最低的及格等级 *Genügend* 通过。Mac Lane 成了最后一个在著名 Hilbert 学派获得博士学位的美国人。离开之前，他还完成了一件事：与 Dorothy Jones 结婚。既然身在哥廷根，婚礼一结束，他就去听了一场数学讲座 [33, pp. 48, 54, 51–52, 58, 52, 56]。

20 世纪 30 年代，多数数学家看不上数学逻辑，认为它属于哲学，而非数学本身。Mac Lane 开始在哈佛担任讲师时，本想开设逻辑课程，却因系里的需要而改教代数。后来他意识到，做代数学家比做逻辑学家更容易找到工作。1941 年，他与 Garrett Birkhoff 合著《现代代数概论》，这是美国第一本采用 Emmy Noether 和 B. L. van der Waerden 的抽象方法的本科教科书。起初有人认为它“飞不过哈德逊河”，但它最终成为本科代数课程的标准教材 [33, pp. 62, 68, 82]。

1941 年春，Mac Lane 从哈佛获得一个学期的休假，并申请到普林斯顿高等研究院访问。申请遭到拒绝后，他转而前往密歇根大学，作了六场系列讲座。听众中有一位密歇根的数学家 Samuel Eilenberg（1913–1998），人们称他为“Sammy”。（译校注：原书生卒年作 1913–1988，与本书参考文献 [6] 的纪念文章题名“Samuel Eilenberg（1913–1998）”不符，此处据该文订正。）他听了前五场，却不得不错过最后一场，于是请 Mac Lane 私下向他介绍那一讲的要点。Mac Lane 照做了，而 Eilenberg 发现<span class="original-page-anchor" id="pdf-page-202" aria-hidden="true"></span>Mac Lane 关于群扩张的结果，与他的同事 Norman Steenrod 对螺线管型空间建立的同调理论很相似。Mac Lane 后来回忆，发现这种联系“令人惊讶”。他们一夜未眠。到天亮时，两人不仅发现了“代数对拓扑的一次新介入”，也结成了一对终生的合作伙伴，最后共同发表了 15 篇论文。Mac Lane 后来还说，普林斯顿拒绝他的申请倒是一件幸事，因为“如果申请通过了，我也许就会错过与 Sammy 合作的机会” [33, pp. 101–104]。

Eilenberg 是波兰犹太人。他的父亲曾是镇上犹太宗教学校最优秀的学生；听从父亲极为明智的建议，他在第二次世界大战爆发前不久离开了波兰。普林斯顿大学的 Oswald Veblen 和 Solomon Lefschetz 接纳了他和其他逃难到美国的欧洲数学家，并帮他在密歇根找到了职位。对 Eilenberg 来说，数学是一种社会活动。他的一位旧同事回忆：“虽然他的数学思想似乎带有一种水晶般的冷峻感，Sammy 本人却热情、强健而且非常活泼。”他的魅力与幽默“令人难以抗拒” [6, pp. 1351–1352]。人们形容他“精力充沛……，善于表达，富有魅力，思维敏捷，经常与人针锋相对，既是出色的思想家，又是风趣健谈的人”；他很容易与人建立联系 [7, p. 360]。他的一生中有许多富有成果的合作。他与 Steenrod 一起“排干了同调理论的庞廷沼泽，将各种出于不同动机的构造所形成的一团乱麻，化为简洁优雅的公理系统，并首次将这个系统用于函子”。他与 Henri Cartan 合作，在《同调代数》（1956）中将同调理论系统化。这个领域发展得如此迅速，以至于据说仅仅几年之后，Alexander Grothendieck 就将这部奠基之作称为“梁龙”，把它归入古生物学的研究对象 [6, p. 1348]。

Eilenberg 相信：“数学的最高价值，不在于貌似深刻，也不在于克服极大的困难，而在于给出足够清晰的阐述，让内在的秩序显现出来。”他坚持追求“清晰、秩序和理解，而不是猎取战利品”。人们称他为<span class="original-page-anchor" id="pdf-page-203" aria-hidden="true"></span>“最伟大的数学文体家”，甚至有人认为，他推崇的是“风格胜过实质” [6, pp. 1349, 1348, 1344, 1350]。

Eilenberg 的风格要求采用极简的方法。他的同事将这种方法描述为：“无论什么问题，总要找出绝对必需的要素，只处理这些要素，不碰别的；换句话说，去掉所有多余的信息。”有一次，有人问他能不能用三根筷子吃中餐。他立即回答说能，并解释：“我拿起三根筷子，把其中一根放在桌上，再用剩下的两根吃饭。”[7, p. 361]

在 1942 年合写的论文《群论中的自然同构》中，Eilenberg 与 Mac Lane 将同调方法推进到更复杂的空间，并引入了函子的概念。André Weil 在《数学评论》上评介这篇论文时，不仅概括了它的内容，还给予了非同寻常的赞扬。他写道，两位作者成功地为“协变与反变的模糊想法”找到了“精确的定义”，“这很可能有助于对已有结果进行分类和系统整理，也有助于寻找群之间的新联系”（Weil，见 [4, p. 743]）。

战争期间，Mac Lane 与 Eilenberg 都来到纽约，在隶属美国国防研究委员会的哥伦比亚大学应用数学小组工作。他们白天研究机载火力控制问题，晚上研究纯数学。在处理计算螺线管上同调这一具体问题时，他们得到了泛系数定理，并提出了范畴和函子这两个十分一般而抽象的概念。Mac Lane 回忆：“这些概念太一般了，看上去简直不像真正的数学——我们的数学同行会接受它们吗？”两人用“一般抽象废话”这个诙谐的称呼掩饰自己的不安，有时也用它来指称自己的研究领域。Mac Lane 承认：“我们并不真的认为它是废话，而且我们为它的一般性而自豪。”[33, pp. 125–126]

1945 年，Eilenberg 与 Mac Lane 在论文《自然等价的一般理论》中总结了他们的成果，这篇论文首次<span class="original-page-anchor" id="pdf-page-204" aria-hidden="true"></span>定义了范畴。据说，这篇论文“被一家前景不佳的期刊的编辑拒绝了，理由是‘比我读过的任何论文都更空洞’。据说 Mac Lane 回答道：‘这正是我们要做的。’”[7, p. 362] 最后，他们设法将论文发表在《美国数学会汇刊》上。这中间颇费了一番周旋。Mac Lane 回忆：“Eilenberg 与编辑很熟，劝他选一位年轻数学家做审稿人。我们能影响这位审稿人，因为他当时是哥伦比亚大学应用数学小组的初级成员，从事战争研究。Eilenberg 和我当时也在这个小组里，而且我是负责人。”[37, p. 5983] 论文公开表达了两人的雄心：“从元数学的意义上说，我们的理论提供了适用于数学各分支的一般概念，从而推动了当时以统一方式处理不同数学学科的趋势。”[12, p. 236]

Eilenberg 与 Mac Lane 的思想威力，并没有很快得到广泛认可。许多年以后，人们才可以“在不同领域的数学家面前，坦然说出‘范畴’和‘函子’这两个词”（Freyd，见 [6, p. 1351]）。幸运的是，美国空军科学研究办公室成了范畴论研究与会议的重要资助者，这是两人在战争期间工作的意外收获。直到 20 世纪 60 年代中期，空军才终于意识到范畴论过于抽象，无法给空战带来实质改进，于是停止了资助 [33, p. 239]。

在最初的发现之后，范畴论本身也经历了很大的变化。Mac Lane 回忆，1945 年那篇论文发表时，Eilenberg 宣称：“这个领域只需要这一篇论文。结果证明，他错了。”[33, p. 209] 两人原本认为，范畴概念“本质上只是辅助性的；我们的基本概念其实是函子和自然变换”。他们甚至建议完全抛开范畴概念，采取“一种更直观的立场”：函子“不是定义在‘所有’群组成的范畴上，而是对每一对<span class="original-page-anchor" id="pdf-page-205" aria-hidden="true"></span>给定的群来定义的” [12, p. 247]。此外，虽然两人相信范畴论“从概念上看待数学的某些部分”，却只把它视为“一种方便的语言”“一种指明方向的语言”，而非“值得继续投入研究的领域” [35, pp. 334–335]。

虽然 Eilenberg 与 Mac Lane 创立了范畴论，但对他们来说，“它始终是一门应用学科，而不是目的本身。定义范畴是为了定义函子，定义函子是为了定义自然变换，而定义自然变换最终是为了证明以前无法证明的定理”。他们将范畴看作主流数学的工具。至于用范畴“陈述以前无法陈述的定理，将范畴看作值得独立研究的天然对象，而非工具”，这样的想法对他们来说十分陌生，因为这似乎会把范畴论推向主流之外的边缘（Freyd，见 [6, p. 1351]）。然而，在 Alexander Grothendieck、Daniel Kan 和 Eilenberg 的学生们手中，范畴论成为了一个蓬勃发展的独立领域，深刻改变了代数几何、拓扑学和表示论，并在从数学逻辑、理论计算机科学到语言学和哲学的广泛学科中产生了回响。在 William Lawvere 的工作中，范畴论被看作整个数学的基础（Heller，见 [6, p. 1349]；[7, p. 362]）。

范畴论在以 Nicolas Bourbaki 为共同笔名的法国数学家群体中引发了争论。这个群体计划以统一的概念视角，用一套多卷著作严格阐述当代数学的全部内容。应 Weil 之邀，Eilenberg 于 1950 年加入，并在此后的 15 年里一直积极参与。另一位 Bourbaki 成员 Henri Cartan 回忆：“他很善于阐明自己的观点，常常能让我们赞同。”（Cartan，见 [6, p. 1345]）1954 年，Mac Lane 应邀参加 Bourbaki 的一次内部会议，也许是希望他能说服这个群体采用范畴论的方法。Cartier、Chevalley、Eilenberg 和 Grothendieck 都支持他，但 André Weil 采取了<span class="original-page-anchor" id="pdf-page-206" aria-hidden="true"></span>谨慎的态度，而他的意见压过了其他人 [39, p. 5]。Bourbaki 的确有意引入范畴论，但很难放弃战前以“结构”为基础的观念。改用范畴，就意味着要修改全部既有工作；把两种方法结合起来，又似乎会破坏 Bourbaki 关于数学统一性的理想 [5, p. 236]。Mac Lane 说：“我的法语还不够好，没法让 Bourbaki 范畴化。”结果，近期数学研究中的一些重要部分没有进入 Bourbaki 的视野，这或许也促成了整个计划的衰落。Mac Lane 几乎不掩饰自己的失望，称 Bourbaki 的著作为“宏伟的多卷怪物”，并称其结构定义为“繁琐的学究式产物”，连 Bourbaki 自己都从未使用过它（引自 [39, p. 6]）。

颇具讽刺意味的是，Bourbaki 所设想的统一数学，却在范畴论中找到了强有力的载体。一般的范畴论概念在许多不同数学领域得到了广泛运用；事实上，将数学严格划分为各个领域的做法本身也受到了质疑。Mac Lane 在 1954 年的一次演讲中说：“今天的数学……已经不能再通过零散的课程来呈现，因为高等数学能够被整齐地分装在标有‘代数’‘分析’‘几何’和‘应用数学’的格子中，这种说法已经不成立了。”他主张“注入几何的观点”，并提醒听众，“向量是几何性的”。“只有选定坐标系之后，向量才是一个由数构成的 $n$ 元组。任何教师或教科书，如果从向量就是 $n$ 元组这一观念讲起，都是在犯罪，而恰当的惩罚就是嘲笑。”（引自 [40, p. 245]）

Mac Lane 最喜欢的休闲活动是帆船运动；他认为它比自己在哥廷根学会的滑雪“严肃得多”。有几次出海时，他与著名哲学家同行，却对他们的学科兴趣不大。他回忆：“幸好，我们对航行的关注多于对哲学学说的关注。”他发现，许多数学哲学研究“除了<span class="original-page-anchor" id="pdf-page-207" aria-hidden="true"></span>最基本的问题之外，对数学的实际内容几乎不加关注”，于是决心改变这一状况。在 1986 年的《数学：形式与功能》中，他很快批评了一系列数学哲学立场：集合论“往往是人为的”，形式主义“无法解释众多公式中哪些才重要”，直觉主义“可能流于教条”，经验主义忽视了“数学并非只来源于事实”，柏拉图主义则是“一套有用的神话和思辨的本体论”。他甚至否定了将数学视为“寻找冷峻之美的形式”的浪漫主义理想，转而提出“形式功能主义”：在他看来，数学是“由形式规则、定义和系统构成的庞大网络，在许多地方与活动和科学紧密相连”。他认为，数学实体未必对应任何物理对象，因此追问数学是否为真并没有意义。对于某一部分数学，适当的问题应当是：它是否正确，也就是是否已被证明？是否回应了某个问题？是否有启发性、发展前景或关联性？在 Mac Lane 看来，数学是正确的，却并不“为真” [33, pp. 143, 145, 455–456, 440, 441, 443]。

与 Mac Lane 一样，Eilenberg“对形而上学的论争没有耐心”（Heller，见 [6, p. 1349]）。不过，他在数学之外也有自己的热爱。这位“阅历丰富而明智、懂得品味生活的人”（Bass，见 [6, p. 1352]），实际上还过着另一种生活。数学家们叫他“Sammy”，艺术界则称他为“教授”；作为艺术商和收藏家，他同样享有盛名。多年来，他积累了世界上最重要的东南亚雕塑收藏之一，也成为这一领域的顶尖专家。他的传记作者推测，他“在古代印度教雕塑中发现了形式的优雅和想象力，与支撑其数学工作的审美感受产生了共鸣。用 Alex Heller 的话说，那是一种‘古典而非浪漫’的审美” [7, p. 362]。Eilenberg 的这两种生活很少交汇。他的同事只记得有一次，他“从讨论雕塑转到了讨论数学。他说，雕塑家很早就学会从内向外创作：最后在表面呈现的形态，来自对内部构思的大量工作。但也有另外一些人，他们先花大量功夫把表面<span class="original-page-anchor" id="pdf-page-208" aria-hidden="true"></span>处理好，内部结构才随之形成。‘那么，’Sammy 问，‘我的数学不也是这样吗？’”（Freyd，见 [6, p. 1350]）

Mac Lane 将他与 Eilenberg 的合作称为“东西相遇的一个虽小却典型的例子。大批欧洲难民数学家的涌入，给 20 世纪 40 年代的美国数学带来了决定性的推动” [33, p. 347]。Eilenberg 与 Mac Lane 的合作不仅把代数与拓扑联系起来，也体现了 20 世纪下半叶不同数学学派之间的相互促进，以及数学内部学科壁垒的逐渐打破。

[^rt-195-1]: 一个著名的复形是 **de Rham 复形**：其中 $C_m$ 是欧氏空间或更一般的流形上微分 $m$-形式组成的空间，$d_m$ 是微分形式的外微分。这就是“微分”一词的由来。
