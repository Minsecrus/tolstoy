---
title: "第二十章 一般同调理论"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第四部分导言：同调代数","link":"/library/volume-86/part-04"}
next: {"text":"第二十一章 有限自由解消","link":"/library/volume-86/chapter-021"}
---

# 第二十章 一般同调理论

<span class="original-page-anchor" id="pdf-page-769" aria-hidden="true"></span>

本章在很大程度上着眼于箭头之间的关系。线性代数中有相当丰富的一套内容，可以极为系统地加以形式化；它们构成了 Steenrod 所说的抽象的一般原理，并提供了一套运转顺畅、适用于许多领域的工具。我们将在论述过程中给出参考文献。

我们要做的大多数工作都适用于阿贝尔范畴，这在第三章 §3 的末尾已经提到。不过，初次阅读时，我建议读者暂且不考虑关于一般阿贝尔范畴的论述，而假设我们处理的是某个环上的模所组成的阿贝尔范畴，或其他具体的阿贝尔范畴，例如某个环上的模复形所组成的范畴。

## §1. 复形

设 $A$ 是一个环。所谓 $A$-模的**开复形**，是指由模与同态组成的序列 $\{(E^i,d^i)\}$，

$$
\to E^{i-1}\xrightarrow{d^{i-1}}E^i\xrightarrow{d^i}E^{i+1}\to,
$$

其中 $i$ 遍历所有整数，$d_i$ 将 $E^i$ 映入 $E^{i+1}$，并且对所有 $i$ 都有

$$
d^i\circ d^{i-1}=0.
$$

我们经常考虑有限的同态序列，例如

$$
E^1\to\cdots\to E^r
$$

<span class="original-page-anchor" id="pdf-page-770" aria-hidden="true"></span>

其中相邻两个同态的复合为 $0$。在两端各添上 $0$，就能把这个序列变成一个复形：

$$
\to0\to0\to E^1\to\cdots\to E^r\to0\to0\to.
$$

这样的复形称为**有限复形**或**有界复形**。

**注。** 复形可以用递减的整数序列作指标，即

$$
\to E_{i+1}\xrightarrow{d_{i+1}}E_i\xrightarrow{d_i}E_{i-1}\to.
$$

系统地采用这种记号时，对于用递增整数序列作指标的复形，则使用上标：

$$
\to E^{i-1}\xrightarrow{d^{i-1}}E^i\xrightarrow{d^i}E^{i+1}\to.
$$

本书主要使用递增的指标。

正如本章导言所说，我们可以用任意阿贝尔范畴中的对象来代替环上的模。

同态 $d^i$ 常称为**微分**，因为最早在实际问题中出现的一些复形来自分析学，其中涉及微分算子与微分形式。参见下面的例子。

我们将上述复形记为 $(E,d)$。如果复形正合，那么将微分的核与余核插入下面这样的图中往往很有用，其中令 $M_i=\operatorname{Ker}d^i=\operatorname{Im}d^{i-1}$。

![正合复形及其微分的核与余核](/library/volume-86/diagrams/pdf-0770-exact-complex.png)

于是根据定义，得到一族短正合列

$$
0\to M^i\to E^i\to M^{i+1}\to0.
$$

如果复形不正合，那么当然必须同时插入 $d^{i-1}$ 的像与 $d^i$ 的核。商模

$$
(\operatorname{Ker}d^i)/(\operatorname{Im}d^{i-1})
$$

将在下一节中研究。它称为**复形的同调**，用于度量偏离正合性的程度。

<span class="original-page-anchor" id="pdf-page-771" aria-hidden="true"></span>

设 $M$ 是一个模。所谓 $M$ 的一个**解消**，是指正合列

$$
\to E_n\to E_{n-1}\to\cdots\to E_0\to M\to0.
$$

因此，解消是一个正合复形，其中最右端的 $0$ 之前的一项是 $M$。解消的指标如上所示。我们通常用 $E_M$ 表示仅由各 $E_i$ 组成的那一部分复形，即

$$
E_M\text{ 为：}\quad\to E_n\to E_{n-1}\to\cdots\to E_0,
$$

到 $E_0$ 为止。然后用 $E$ 表示在右端添上 $0$ 所得的复形：

$$
E\text{ 为：}\quad\to E_n\to E_{n-1}\to\cdots\to E_0\to0.
$$

如果解消中的对象 $E_i$ 取自某一族对象，那么就用与这族对象相同的名称来限定解消。例如，若对所有 $i\geqq0$，$E_i$ 都是自由模，就称这个**解消为自由解消**。若对所有 $i\geqq0$，$E_i$ 都是投射模，就称这个**解消为投射解消**，依此类推。同样的术语也适用于向右的解消

$$
0\to M\to E^0\to E^1\to\cdots\to E^{n-1}\to E^n\to,
$$

也写成

$$
0\to M\to E_M.
$$

此时用 $E$ 表示复形

$$
0\to E^0\to E^1\to E^2\to\cdots.
$$

关于内射解消，参见 §5。

如果除有限多个指标 $i$ 外，$E_i$（或 $E^i$）都为 $0$，就称解消是**有限的**。

**例。** 每个模都存在一个（向左的）自由解消。这是自由模概念的一个简单应用。事实上，设 $M$ 是一个模，$\{x_j\}$ 是一族生成元，其中 $j$ 属于某个指标集 $J$。对每个 $j$，令 $Re_j$ 为以一个元素 $e_j$ 为基的自由 $R$-模。令

$$
F=\bigoplus_{j\in J}Re_j
$$

为它们的直和。存在唯一一个满态射

$$
F\to M\to0,
$$

将 $e_j$ 映到 $x_j$。现在令 $M_1$ 为它的核，并再次把 $M_1$ 表示成一个自由模的商。通过归纳，就能构造出所需的自由解消。

<span class="original-page-anchor" id="pdf-page-772" aria-hidden="true"></span>

**例。标准复形。** 设 $S$ 是一个集合。对于 $i=0,1,2,\ldots$，令 $E_i$ 为由满足 $x_0,\ldots,x_i\in S$ 的 $(i+1)$ 元组 $(x_0,\ldots,x_i)$ 生成的自由 $\mathbf Z$-模。因此，这些 $(i+1)$ 元组构成 $E_i$ 在 $\mathbf Z$ 上的一组基。存在唯一的同态

$$
d_{i+1}:E_{i+1}\to E_i,
$$

使得

$$
d_{i+1}(x_0,\ldots,x_{i+1})=\sum_{j=0}^{i+1}(-1)^j(x_0,\ldots,\widehat{x_j},\ldots,x_{i+1}),
$$

其中符号 $\widehat{x_j}$ 表示略去这一项。对于 $i=0$，定义 $d_0:E_0\to\mathbf Z$ 为满足 $d_0(x_0)=1$ 的唯一同态。映射 $d_0$ 有时称为**增广映射**，也记为 $\varepsilon$。于是，由复形

$$
\to E_{i+1}\to E_i\to\cdots\to E_0\xrightarrow{\varepsilon}\mathbf Z\to0
$$

得到 $\mathbf Z$ 的一个解消。

**译校注。** 原文先仅设“$S$ 是一个集合”，随后称上述复形给出 $\mathbf Z$ 的解消；这一结论需要 $S\ne\varnothing$。若 $S=\varnothing$，则 $E_0=0$，增广映射 $E_0\to\mathbf Z$ 不是满射，因此该增广复形不能成为 $\mathbf Z$ 的解消。

上述映射 $d_i$ 的形式在数学中无处不在。关于标准复形在群上同调理论中的应用，参见习题 2。作为这种形式的另一个例子，还可以与第二十一章 §4 的 Koszul 复形作比较。

给定一个模 $M$，可以对每个 $i$ 构造 $\operatorname{Hom}(E_i,M)$，于是通过映射的复合得到上边缘映射

$$
\delta^i:\operatorname{Hom}(E_i,M)\to\operatorname{Hom}(E_{i+1},M),\qquad\delta(f)=f\circ d^{i+1}.
$$

这个过程将在 §6 中用来得到导出函子。在习题 2 至 6 中，你将看到如何用这个过程来发展群的上同调理论。

也可以用单形与连续映射构造一个拓扑版本来代替同态；此时，标准复形产生拓扑空间的奇异同调理论。参见 [GreH 81] 第 9 章。

**例。有限自由解消。** 在第二十一章中，你将看到用不同工具、以各种方式构造的其他复形例子，特别是有限自由复形。后面的这一整章都可以看作在为本章提供例子。

**涉及微分形式的例子。** 在第十九章 §3 中，我们给出了代数环境下的 de Rham 复形。在微分流形理论中，de Rham 复形具有微分映射

$$
d^i:\Omega^i\to\Omega^{i+1},
$$

将 $i$ 次微分形式映为 $i+1$ 次微分形式，并可以用来计算流形的同调。

在复微分几何中也有类似情形，其中映射 $d^i$ 由 **Dolbeault** 的 $\bar\partial$ 算子给出：

$$
\bar\partial^i:\Omega^{p,i}\to\Omega^{p,i+1}
$$

<span class="original-page-anchor" id="pdf-page-773" aria-hidden="true"></span>

作用于 $(p,i)$ 型的形式。感兴趣的读者可以查阅例如第四部分导言中提到的 Gunning 的著作 [Gu 90]，第一卷 E 部分。这个复形的同调称为复流形的 **Dolbeault 上同调**或 **$\bar\partial$-上同调**。

现在回到复形与解消的一般代数方面。

哪些模存在有限解消，以及这一主题的各种变体，是一个有趣的问题。本章稍后以及第二十一章会讨论一些条件。如果解消

$$
0\to E_n\to E_{n-1}\to\cdots\to E_0\to M\to0
$$

满足当 $m>n$ 时 $E_m=0$，就称这个解消的**长度 $\leqq n$**（有时为了表述方便，也称其**长度为 $n$**）。

$A$-模的**闭复形**是由模与同态组成的序列 $\{(E^i,d^i)\}$，其中对某个 $n\geqq2$，$i$ 遍历模 $n$ 的整数，其他方面则满足与上面相同的性质。因此，闭复形的形式如下：

![闭复形](/library/volume-86/diagrams/pdf-0773-closed-complex.png)

我们称 $n$ 为闭复形的**长度**。

在不会引起混淆时，可以略去 $d^i$ 的指标 $i$，只写作 $d$。我们也用 $(E,d)$ 表示复形 $\{(E^i,d^i)\}$，甚至更简略地只写 $E$。

设 $(E,d)$ 和 $(E',d')$ 是两个复形（都为开复形或都为闭复形），$r$ 是一个整数。一个**次数为 $r$** 的（复形的）**态射**或**同态**

$$
f:(E',d')\to(E,d)
$$

是一列同态

$$
f_i:E'^i\to E^{i+r},
$$

使得对所有 $i$，下图都交换：

![定义 r 次态射的交换方块](/library/volume-86/diagrams/pdf-0773-degree-r-morphism.png)

正如用 $d$ 代替 $d^i$，我们也用 $f$ 代替 $f_i$。如果复形是闭的，只有当它们长度相同时，我们才定义一个到另一个的态射。

显然，复形构成一个范畴。事实上，它们构成一个阿贝尔范畴。确实，为简单起见，设我们处理的是以 $\mathbf Z$ 为指标的复形，以及次数为 $0$ 的态射。假设有复形的一个态射 $f:C\to C''$，或者<span class="original-page-anchor" id="pdf-page-774" aria-hidden="true"></span>添上指标后写成：

![带指标的复形态射](/library/volume-86/diagrams/pdf-0774-complex-kernel.png)

令 $C'_n=\operatorname{Ker}(C_n\to C''_n)$。那么这一族 $(C'_n)$ 构成一个复形，我们将其定义为 $f$ 的核。关于这一构造，以及余核和有限直和的类似定义如何使模复形构成阿贝尔范畴，其细节留给读者核查。此时，读者应参阅第三章 §9，其中在这一背景下讨论了核与余核。那一章的蛇引理现在将成为下一节的核心工具。

为了处理以幺半群为指标的对象，引入另一个概念会很有用。设 $G$ 是一个幺半群，为适应这里考虑的应用，我们假设它是交换的，并采用加法记号。设 $\{M_i\}_{i\in G}$ 是以 $G$ 为指标的一族模。直和

$$
M=\bigoplus_{i\in G}M_i
$$

称为**与族 $\{M_i\}_{i\in G}$ 相伴的 $G$-分次模**。设 $\{M_i\}_{i\in G}$ 和 $\{M'_i\}_{i\in G}$ 是以 $G$ 为指标的两族模，$M,M'$ 是它们相伴的 $G$-分次模。设 $r\in G$。所谓次数为 $r$ 的 **$G$-分次态射** $f:M'\to M$，是指一个同态，对每个 $i\in G$，它都将 $M'_i$ 映入 $M_{i+r}$（将 $M'_i$ 与直和的第 $i$ 个分量所对应的子模等同）。因此，$f$ 无非是一族同态 $f_i:M'_i\to M_{i+r}$。

如果 $(E,d)$ 是一个复形，可以将 $E$ 看作一个 $G$-分次模（取复形各分量的直和），并将 $d$ 看作一个次数为 $1$ 的 $G$-分次态射，其中令 $G$ 为 $\mathbf Z$ 或 $\mathbf Z/n\mathbf Z$。最常见的情形是 $G=\mathbf Z$。此时将复形写为

$$
E=\bigoplus E_i,\quad\text{且}\quad d:E\to E
$$

将 $E$ 映入自身。微分 $d$ 在每个直和项 $E_i$ 上定义为 $d_i$，且次数为 $1$。

反过来，若 $G$ 为 $\mathbf Z$ 或 $\mathbf Z/n\mathbf Z$，通过定义 $d$ 为零映射，就可以将一个 $G$-分次模看作复形。

为简单起见，处理 $G$-分次态射时，我们常省略“态射”一词前面的“$G$-分次”限定语。

<span class="original-page-anchor" id="pdf-page-775" aria-hidden="true"></span>

## §2. 同调序列

设 $(E,d)$ 是一个复形。令

$$
Z^i(E)=\operatorname{Ker}d^i,
$$

并称 $Z^i(E)$ 为 **$i$-循环模**。令

$$
B^i(E)=\operatorname{Im}d^{i-1},
$$

并称 $B^i(E)$ 为 **$i$-边缘模**。我们经常分别用 $Z^i$ 和 $B^i$ 代替 $Z^i(E)$ 和 $B^i(E)$。令

$$
H^i(E)=Z^i/B^i=\operatorname{Ker}d^i/\operatorname{Im}d^{i-1},
$$

并称 $H^i(E)$ 为复形的第 $i$ 个**同调群**。与族 $\{H^i\}$ 相伴的分次模记为 $H(E)$，称为 $E$ 的**同调**。有时也用 $H^*(E)$ 代替 $H(E)$。

若 $f:E'\to E$ 是复形的一个态射，例如次数为 $0$，那么在每个同调群上得到一个**诱导的典范同态**

$$
H^i(f):H^i(E')\to H^i(E).
$$

确实，从定义复形态射的交换图立刻看出，$f$ 将 $Z^i(E')$ 映入 $Z^i(E)$，将 $B^i(E')$ 映入 $B^i(E)$，因而得到诱导同态 $H^i(f)$。可与第三章 §9 开头的注记比较。这个诱导同态常记为 $f_{i*}$，而不用 $H_i(f)$；若 $H(E)$ 像上面那样表示同调的分次模，就写作

$$
H(f)=f_*:H(E')\to H(E).
$$

我们称 $H(f)$ 为 $f$ 在同调上**诱导**的映射。如果对所有 $i$，$H^i(f)$ 都是同构，就称 $f$ 为一个**同调同构**。

注意，若 $f:E'\to E$ 和 $g:E\to E''$ 是复形的态射，就可以立即验证

$$
H(g)\circ H(f)=H(g\circ f)\quad\text{且}\quad H(\mathrm{id})=\mathrm{id}.
$$

因此，$H$ 是从复形范畴到分次模范畴的函子。

我们将考虑次数为 $0$ 的态射所组成的复形短正合列：

$$
0\to E'\xrightarrow{f}E\xrightarrow{g}E''\to0,
$$

<span class="original-page-anchor" id="pdf-page-776" aria-hidden="true"></span>

将其完全展开，形式如下：

![完全展开的复形短正合列](/library/volume-86/diagrams/pdf-0776-short-exact-complexes.png)

*由蛇引理，可以定义一个次数为 $1$ 的态射*

$$
\delta:H(E'')\to H(E'),
$$

*换言之，定义一族同态*

$$
\delta^i:H''^i\to H'^{(i+1)}.
$$

**定理 2.1。** *设*

$$
0\to E'\xrightarrow{f}E\xrightarrow{g}E''\to0
$$

*是复形的正合列，其中 $f,g$ 的次数为 $0$。那么序列*

![正合同调序列](/library/volume-86/diagrams/pdf-0776-homology-triangle.png)

*是正合的。*

这个定理只是蛇引理的一种特殊应用。

将定理中的同调序列完全展开，形式如下：

$$
\xrightarrow{\delta}H'^i\to H^i\to H''^i\xrightarrow{\delta}H'^{(i+1)}\to H^{i+1}\to H''^{(i+1)}\xrightarrow{\delta}.
$$

<span class="original-page-anchor" id="pdf-page-777" aria-hidden="true"></span>

显然，我们的映射 $\delta$ 具有函子性（其含义是显然的），因而整个结构 $(H,\delta)$ 是从复形短正合列的范畴到复形范畴的一个函子。

## §3. 欧拉特征与 Grothendieck 群

本节可以看作第三章 §8 关于欧拉—庞加莱映射的继续。为简单起见，考虑 $A$-模的复形。

设 $E$ 是一个复形，几乎所有同调群 $H^i$ 都等于 $0$。假设 $E$ 是开复形。像第三章 §8 中那样，设 $\varphi$ 是模范畴（即 $A$-模范畴）上的一个欧拉—庞加莱映射。如果对所有 $H^i$，$\varphi(H^i)$ 都有定义，则定义关于 $\varphi$ 的**欧拉—庞加莱特征** $\chi_\varphi(E)$（或简称**欧拉特征**）为

$$
\chi_\varphi(E)=\sum(-1)^i\varphi(H^i).
$$

此时称 $\chi_\varphi$ 对复形 $E$ **有定义**。

如果 $E$ 是闭复形，就为模 $n$ 的整数选定一个顺序 $(E^1,\ldots,E^n)$，并同样在所有 $\varphi(H^i)$ 都有定义的前提下，以公式

$$
\chi_\varphi(E)=\sum_{i=1}^n(-1)^i\varphi(H^i)
$$

定义欧拉特征。

作为例子，读者可以参看第一章习题 28。

通过定义 $d$ 为零映射，可以将 $H$ 看作复形。在这种情形下，$\chi_\varphi(H)$ 就是上面给出的交错和。更一般地：

**定理 3.1。** *设 $F$ 是一个复形；若它是闭复形，假设其长度为偶数。假设对所有 $i$，$\varphi(F^i)$ 有定义，且对几乎所有 $i$，$\varphi(F^i)=0$，并且对几乎所有 $i$，$H^i(F)=0$。那么 $\chi_\varphi(F)$ 有定义，且*

$$
\chi_\varphi(F)=\sum_i(-1)^i\varphi(F^i).
$$

**证明。** 设 $Z^i$ 和 $B^i$ 分别为 $F^i$ 中的 $i$-循环群与 $i$-边缘群。我们有正合列

$$
0\to Z^i\to F^i\to B^{i+1}\to0.
$$

因此 $\chi_\varphi(F)$ 有定义，并且

$$
\varphi(F^i)=\varphi(Z^i)+\varphi(B^{i+1}).
$$

<span class="original-page-anchor" id="pdf-page-778" aria-hidden="true"></span>

取交错和，立刻得到所要的结论。

同调为零的复形称为**无环复形**。

**推论 3.2。** *设 $F$ 是无环复形，对所有 $i$，$\varphi(F^i)$ 都有定义，并且对几乎所有 $i$ 都等于 $0$。如果 $F$ 是闭复形，假设它的长度为偶数。那么*

$$
\chi_\varphi(F)=0.
$$

在许多应用中，开复形 $F$ 满足对几乎所有 $i$ 都有 $F^i=0$。此时，可以额外定义一个从最右端的零到最左端的零的映射，从而把这个复形当作闭复形来处理。因此，在这种情形下，对这类开复形的研究归结为对闭复形的研究。

**定理 3.3。** *设*

$$
0\to E'\to E\to E''\to0
$$

*是复形的正合列，其中态射的次数为 $0$。如果这些复形是闭的，假设其长度为偶数。设 $\varphi$ 是模范畴上的欧拉—庞加莱映射。如果 $\chi_\varphi$ 对上述三个复形中的两个有定义，那么它对第三个也有定义，并且*

$$
\chi_\varphi(E)=\chi_\varphi(E')+\chi_\varphi(E'').
$$

**证明。** 我们有正合同调序列

$$
\to H''^{(i-1)}\to H'^i\to H^i\to H''^i\to H'^{(i+1)}\to.
$$

这个同调序列本身就是一个同调为零的复形。此外，例如属于 $E$ 的每个同调群，都夹在 $E'$ 与 $E''$ 的同调群之间。因此，如果 $\chi_\varphi$ 对 $E'$ 和 $E''$ 有定义，它对 $E$ 也有定义。其他两种可能同理。如果这些复形是长度为偶数 $n$ 的闭复形，那么这个同调序列的长度为偶数 $3n$。所以可以应用定理 3.1 的推论，得到所需结论。

对于某些应用，构造一个泛欧拉映射很方便。设 $\mathfrak A$ 是某些模的同构类所组成的集合。若 $E$ 是模，令 $[E]$ 表示其同构类。我们要求 $\mathfrak A$ 满足**欧拉—庞加莱条件**，即如果有正合列

$$
0\to E'\to E\to E''\to0,
$$

那么 $[E]$ 属于 $\mathfrak A$，当且仅当 $[E']$ 和 $[E'']$ 都属于 $\mathfrak A$。此外，零模也属于 $\mathfrak A$。

<span class="original-page-anchor" id="pdf-page-779" aria-hidden="true"></span>

**定理 3.4。** *假设 $\mathfrak A$ 满足欧拉—庞加莱条件。那么存在映射*

$$
\gamma:\mathfrak A\to\mathbf K(\mathfrak A),
$$

*将 $\mathfrak A$ 映到一个阿贝尔群 $\mathbf K(\mathfrak A)$，并且对于定义在 $\mathfrak A$ 上的欧拉—庞加莱映射具有泛性质。*

为构造它，令 $F_{\mathrm{ab}}(\mathfrak A)$ 为由所有这样的 $[E]$ 组成的集合生成的自由阿贝尔群。令 $B$ 为由所有形如

$$
[E]-[E']-[E'']
$$

的元素生成的子群，其中

$$
0\to E'\to E\to E''\to0
$$

是各项属于 $\mathfrak A$ 的正合列。令 $\mathbf K(\mathfrak A)$ 为商群 $F_{\mathrm{ab}}(\mathfrak A)/B$，令 $\gamma:\mathfrak A\to\mathbf K(\mathfrak A)$ 为自然映射。显然，$\gamma$ 具有所需的泛性质。

可以看出，这一构造与幺半群的 Grothendieck 群的构造相似。事实上，这个群称为 $\mathfrak A$ 的**欧拉—Grothendieck 群**，通常省去“欧拉”二字。

读者应注意，虽然我们仍使用“**模**”这个词，上述论证在阿贝尔范畴中也成立。正如群的初等同构定理一样，我们有模的若尔当—赫尔德定理。对于模，当然不必担心子模的正规性。

现在进一步深入 **K** 理论。设 $\mathfrak A$ 为阿贝尔范畴。初次阅读时，可以只考虑某个环上的模构成的阿贝尔范畴。设 $\mathfrak C$ 是 $\mathfrak A$ 中的一族对象。如果满足下列条件，就称 $\mathfrak C$ 为 **K 族**。

**K 1。** $\mathfrak C$ 对有限直和封闭，且 $0$ 属于 $\mathfrak C$。

**K 2。** 给定 $\mathfrak A$ 中的对象 $E$，存在满态射

$$
L\to E\to0,
$$

其中 $L$ 属于 $\mathfrak C$。

**K 3。** 设对象 $E$ 存在长度为 $n$ 的有限解消

$$
0\to L_n\to\cdots\to L_0\to E\to0,
$$

其中对所有 $i$ 都有 $L_i\in\mathfrak C$。如果

$$
0\to N\to F_{n-1}\to\cdots\to F_0\to E\to0
$$

是一个解消，且 $N$ 属于 $\mathfrak A$，$F_0,\ldots,F_{n-1}$ 属于 $\mathfrak C$，那么 $N$ 也属于 $\mathfrak C$。

<span class="original-page-anchor" id="pdf-page-780" aria-hidden="true"></span>

注意，从这些公理可知：若 $F$ 属于 $\mathfrak C$，而 $F'$ 与 $F$ 同构，那么 $F'$ 也属于 $\mathfrak C$。只要考虑解消

$$
0\to F'\to F\to0\to0
$$

并应用 **K 3**，便可看出这一点。此外，给定正合列

$$
0\to F'\to F\to F''\to0,
$$

若 $F$ 和 $F''$ 属于 $\mathfrak C$，那么再次应用 **K 3**，可知 $F'$ 也属于 $\mathfrak C$。

**例。** 可以取 $\mathfrak A$ 为某个交换环上的模范畴，取 $\mathfrak C$ 为投射模族。稍后还将考虑诺特环，此时可以分别改取有限生成模与有限生成投射模。条件 **K 2** 将在 §8 中讨论。

从现在起，假设 $\mathfrak C$ 为一个 **K 族**。对于 $\mathfrak A$ 的每个对象 $E$，用 $[E]$ 表示其同构类。如果 $\mathfrak A$ 的对象 $E$ 存在一个各项属于 $\mathfrak C$ 的有限解消，就称 $E$ 具有**有限 $\mathfrak C$-维数**。令 $\mathfrak A(\mathfrak C)$ 为 $\mathfrak A$ 中具有有限 $\mathfrak C$-维数的对象族。于是可以构造

$$
\mathbf K(\mathfrak A(\mathfrak C))=\mathbf Z[\mathfrak A(\mathfrak C)]/R(\mathfrak A(\mathfrak C)),
$$

其中 $R(\mathfrak A(\mathfrak C))$ 为所有由 $\mathfrak A(\mathfrak C)$ 中的正合列

$$
0\to E'\to E\to E''\to0
$$

产生的元素 $[E]-[E']-[E'']$ 所生成的群。类似地，定义

$$
\mathbf K(\mathfrak C)=\mathbf Z[(\mathfrak C)]/R(\mathfrak C),
$$

其中 $R(\mathfrak C)$ 是按上述方法生成的关系群，但此时取 $E',E,E''$ 都在 $\mathfrak C$ 中。

存在自然映射

$$
\gamma_{\mathfrak A(\mathfrak C)}:\mathfrak A(\mathfrak C)\to\mathbf K(\mathfrak A(\mathfrak C))\quad\text{与}\quad\gamma_{\mathfrak C}:\mathfrak C\to\mathbf K(\mathfrak C),
$$

将每个对象映到其在相应 Grothendieck 群中的类。还存在自然同态

$$
\epsilon:\mathbf K(\mathfrak C)\to\mathbf K(\mathfrak A(\mathfrak C)),
$$

因为 $\mathfrak C$ 中对象的正合列也可以看成 $\mathfrak A(\mathfrak C)$ 中对象的正合列。

<span class="original-page-anchor" id="pdf-page-781" aria-hidden="true"></span>

**定理 3.5。** *设 $M\in\mathfrak A(\mathfrak C)$，并假设有两个解消*

$$
L_M\to M\to0\quad\text{与}\quad L'_M\to M\to0,
$$

*其中 $L_M$ 与 $L'_M$ 是 $\mathfrak C$ 中的有限复形。那么*

$$
\sum(-1)^i\gamma_{\mathfrak C}(L_i)=\sum(-1)^i\gamma_{\mathfrak C}(L'_i).
$$

**证明。** 先考虑存在满态射 $L'_M\to L_M$ 的特殊情形。其核 $E$ 如下正合交换图所示。

![解消的满射及其核](/library/volume-86/diagrams/pdf-0781-comparison-kernel.png)

这个核是复形

$$
0\to E_n\to E_{n-1}\to\cdots\to E_0\to0.
$$

它是正合的，因为有同调序列

$$
H_p(E)\to H_p(L')\to H_p(L)\to H_{p-1}(E).
$$

当 $p\geqq1$ 时，由定义有 $H_p(L)=H_p(L')=0$，所以当 $p\geqq1$ 时 $H_p(E)=0$。而当 $p=0$ 时，考虑正合列

$$
H_1(L)\to H_0(E)\to H_0(L')\to H_0(L).
$$

现在 $H_1(L)=0$，而 $H_0(L')\to H_0(L)$ 对应于 $M$ 上的恒等态射，因此是同构。于是 $H_0(E)=0$ 也成立。

由 **K** 族的定义，对象 $E_p$ 属于 $\mathfrak C$。然后在 $\mathbf K(\mathfrak C)$ 中取欧拉特征，得到

$$
\chi(L')-\chi(L)=\chi(E)=0,
$$

这就证明了特殊情形中的断言。

一般情形可以通过如下事实证明：给定 $M$ 在 $\mathfrak C$ 中的两个解消，总能找到第三个解消，使它同时映满这两个解消。下面一个引理将给出这一构造的模式。

<span class="original-page-anchor" id="pdf-page-782" aria-hidden="true"></span>

**引理 3.6。** *给定 $\mathfrak A$ 中的两个满态射 $u:M\to N$ 与 $v:M'\to N$，存在满态射 $F\to M$ 和 $F\to M'$，其中 $F$ 属于 $\mathfrak C$，使下图交换。*

![两个满态射的共同覆盖](/library/volume-86/diagrams/pdf-0782-common-cover.png)

**证明。** 令 $E=M\times_N M'$，即 $E$ 是由 $(x,y)\mapsto ux-vy$ 给出的态射

$$
M\times M'\to N
$$

的核。（这里实际上并未使用元素，也可以形式地写作 $u-v$。）存在某个属于 $\mathfrak C$ 的 $F$ 以及满态射 $F\to E\to0$。将这一满态射与 $E$ 到各个因子的自然投影复合，就得到所需的映射。

我们构造一个复形 $L''_M$，给出 $M$ 的解消，并具有如下正合交换图：

![同时映满两个给定解消的解消](/library/volume-86/diagrams/pdf-0782-resolutions-common-cover.png)

构造通过归纳进行，因此添上指标：

![带指标的归纳比较图](/library/volume-86/diagrams/pdf-0782-inductive-comparison.png)

<span class="original-page-anchor" id="pdf-page-783" aria-hidden="true"></span>

假设已经构造到 $L''_{i-1}$，并有到 $L_{i-1}$ 与 $L'_{i-1}$ 的所需满态射。我们要构造 $L''_i$。令 $B_i=\operatorname{Ker}(L_{i-1}\to L_{i-2})$，并类似地定义 $B'_i$ 和 $B''_i$。得到交换图：

![归纳构造中的边缘模](/library/volume-86/diagrams/pdf-0783-inductive-boundaries.png)

如果 $B''_i\to B_i$ 或 $B''_i\to B'_i$ 不是满态射，就将 $L''_{i-1}$ 替换为

$$
L''_{i-1}\oplus L_i\oplus L'_i.
$$

令到 $L''_{i-2}$ 的边缘映射在新增的直和项上为 $0$，并类似地将到 $L_{i-1}$ 和 $L'_{i-1}$ 的映射分别在 $L'_i$ 和 $L_{i-1}$ 上定义为 $0$。

**译校注。** 原文这里第二个取零的项印为 $L_{i-1}$，应读作 $L_i$。被替换后的源对象是 $L''_{i-1}\oplus L_i\oplus L'_i$，新增直和项为 $L_i,L'_i$；到 $L'_{i-1}$ 的映射应在新增的 $L_i$ 上取零，而 $L_{i-1}$ 是另一个映射的目标，并不是新增的源直和项。

现在不失一般性，可以假设

$$
B''_i\to B_i\quad\text{与}\quad B''_i\to B'_i
$$

都是满态射。然后使用前一个引理的构造。令

$$
E_i=L_i\bigoplus_{B_i}B''_i\quad\text{与}\quad E'_i=B''_i\bigoplus_{B'_i}L'_i.
$$

那么 $E_i$ 与 $E'_i$ 都有到 $B''_i$ 的自然满态射。再令

$$
N_i=E_i\bigoplus_{B''_i}E'_i,
$$

并取 $\mathfrak C$ 中的对象 $L''_i$ 以及满态射 $L''_i\to N_i$。这样就能归纳构造 $L''$，直到最后。为了终止这一过程，应用 **K 3**，取最后构造出的 $L''_i$ 的核，便完成证明。

**定理 3.7。** *自然映射*

$$
\epsilon:\mathbf K(\mathfrak C)\to\mathbf K(\mathfrak A(\mathfrak C))
$$

*是同构。*

**证明。** 此映射是满射，因为给定解消

$$
0\to F_n\to\cdots\to F_0\to M\to0,
$$

其中对所有 $i$ 都有 $F_i\in\mathfrak C$，元素

$$
\sum(-1)^i\gamma_{\mathfrak C}(F_i)
$$

<span class="original-page-anchor" id="pdf-page-784" aria-hidden="true"></span>

在 $\epsilon$ 下映到 $\gamma_{\mathfrak A(\mathfrak C)}(M)$。反过来，定理 3.5 说明对应

$$
M\mapsto\sum(-1)^i\gamma_{\mathfrak C}(F_i)
$$

是良定义的映射。由于对任意 $L\in\mathfrak C$ 都有短正合列 $0\to L\to L\to0$，可知先施行 $\epsilon$ 再施行这个映射，所得为 $\mathbf K(\mathfrak C)$ 上的恒等映射，所以 $\epsilon$ 是单态射。因此 $\epsilon$ 是同构，得证。

下面的引理更明确地说明逆映射的可加性，实际看一看这一引理或许会对读者有所帮助。

**引理 3.8。** *给定 $\mathfrak A(\mathfrak C)$ 中的正合列*

$$
0\to M'\to M\to M''\to0,
$$

*存在正合交换图*

![有限解消的正合列](/library/volume-86/diagrams/pdf-0784-exact-resolutions.png)

*其中 $L_{M'},L_M,L_{M''}$ 是 $\mathfrak C$ 中的有限解消。*

**证明。** 首先说明，可以找到 $\mathfrak C$ 中的 $L',L,L''$，使其组成如下正合交换图：

![构造正合解消的第一步](/library/volume-86/diagrams/pdf-0784-horseshoe-first-step.png)

先选取一个满态射 $L''\to M''$，其中 $L''$ 属于 $\mathfrak C$。由引理 3.6，存在 $L_1\in\mathfrak C$，以及满态射 $L_1\to M$、$L_1\to L''$，使图交换。再取一个满态射 $L_2\to M'$，其中 $L_2\in\mathfrak C$，最后定义 $L=L_1\oplus L_2$。于是以显然的方式得到态射 $L\to M$ 和 $L\to L''$。令 $L'$ 为 $L\to L''$ 的核。那么 $L_2\subset L'$，所以得到满态射 $L'\to M'$。

<span class="original-page-anchor" id="pdf-page-785" aria-hidden="true"></span>

现在可以归纳构造解消，直到第 $n$ 步，其中 $n$ 是使 $M,M''$ 在 $\mathfrak C$ 中存在长度为 $n$ 的解消的某个整数。最后得到的水平正合列是

$$
0\to L'_n\to L_n\to L''_n\to0,
$$

并且可以选取 $L''_n$ 为 $L''_{n-1}\to L''_{n-2}$ 的核。由 **K 3**，$L''_n$ 属于 $\mathfrak C$，而序列

$$
0\to L''_n\to L''_{n-1}
$$

正合。这说明在下一步归纳中，可以取 $L''_{n+1}=0$。于是

$$
0\to L'_{n+1}\to L_{n+1}\to0\to0
$$

正合。在再下一步，只需取竖直箭头的核，就能完成所需的 $\mathfrak C$ 中的有限解消。引理的证明至此完成。

**注。** 引理 3.8 的证明实际上说明：

*如果*

$$
0\to M'\to M\to M''\to0
$$

*是 $\mathfrak A$ 中的正合列，且 $M,M''$ 具有有限 $\mathfrak C$-维数，那么 $M'$ 也具有有限 $\mathfrak C$-维数。*

在模范畴中，有更精确的结论：

**定理 3.9。** *设 $\mathfrak A$ 为某个环上的模范畴，$\mathfrak P$ 为投射模族。给定模的正合列*

$$
0\to E'\to E\to E''\to0,
$$

*若 $E',E,E''$ 中的任意两个在 $\mathfrak P$ 中存在有限解消，那么第三个也存在。*

更微妙情形中的证明将在第二十一章定理 2.7 中给出。

接下来，用张量积研究 Grothendieck 群上的环结构。为简单起见，设我们处理的是某个交换环上的模组成的阿贝尔范畴，记为 $\mathfrak A$，以及如上的 **K** 族 $\mathfrak C$；现在进一步假设 $\mathfrak A$ 对张量积封闭。后面的结果实际只用到以下性质，记为 **TG**（分别取自“tensor”和“Grothendieck”）：

**TG 1。** 存在给出交换性的双函子同构

$$
M\otimes N\approx N\otimes M,
$$

对所有 $\mathfrak A$ 中的 $M,N$ 都成立；同样还有关于直和的分配律及结合律。

<span class="original-page-anchor" id="pdf-page-786" aria-hidden="true"></span>

**TG 2。** 对所有属于 $\mathfrak C$ 的 $L$，函子 $M\mapsto L\otimes M$ 都正合。

**TG 3。** 若 $L,L'$ 属于 $\mathfrak C$，那么 $L\otimes L'$ 也属于 $\mathfrak C$。

于是可以定义

$$
\operatorname{cl}_{\mathfrak C}(L)\operatorname{cl}_{\mathfrak C}(L')=\operatorname{cl}_{\mathfrak C}(L\otimes L'),
$$

赋予 $\mathbf K(\mathfrak C)$ 一个代数结构。

条件 **TG 1** 说明这个代数是交换的，我们称其为 **Grothendieck 代数**。在实际情形中存在单位元，但如果想在当前的公理化体系中得到单位元，必须明确作出假设：

**TG 4。** 存在 $\mathfrak C$ 中的对象 $R$，使得对所有 $\mathfrak A$ 中的 $M$ 都有 $R\otimes M\approx M$。

那么 $\operatorname{cl}_{\mathfrak C}(R)$ 就是单位元。

类似地，由条件 **TG 2**，可以用同样的公式

$$
\operatorname{cl}_{\mathfrak C}(L)\operatorname{cl}_{\mathfrak A}(M)=\operatorname{cl}_{\mathfrak A}(L\otimes M)
$$

在 $\mathbf K(\mathfrak A)$ 上定义一个 $\mathbf K(\mathfrak C)$-模结构。同样，$\mathbf K(\mathfrak A(\mathfrak C))$ 也是 $\mathbf K(\mathfrak C)$ 上的模；回顾，$\mathfrak A(\mathfrak C)$ 是 $\mathfrak A$ 中存在各项属于 $\mathfrak C$ 的有限解消的对象族。

由定理 3.7 已知 $\mathbf K(\mathfrak C)\approx\mathbf K(\mathfrak A(\mathfrak C))$，所以通过这个同构，也在 $\mathbf K(\mathfrak A(\mathfrak C))$ 上得到环结构。乘法可以进一步明确如下。

**命题 3.10。** *设 $M\in\mathfrak A(\mathfrak C)$，$N\in\mathfrak A$。设*

$$
0\to L_n\to\cdots\to L_0\to M\to0
$$

*是 $M$ 的一个由 $\mathfrak C$ 中对象组成的有限解消。那么*

$$
\begin{aligned}
\operatorname{cl}_{\mathfrak C}(M)\operatorname{cl}_{\mathfrak A}(N)&=\sum(-1)^i\operatorname{cl}_{\mathfrak A}(L_i\otimes N).\\
&=\sum(-1)^i\operatorname{cl}_{\mathfrak A}(H_i(K))
\end{aligned}
$$

*其中 $K$ 是复形*

$$
0\to L_n\otimes N\to\cdots\to L_0\otimes N\to M\otimes N\to0,
$$

*而 $H_i(K)$ 是这一复形的第 $i$ 个同调。*

**译校注。** 原文将 $K$ 印为包含末项 $M\otimes N$ 的增广复形；要使上述同调公式及下面的 $\operatorname{Tor}_i(M,N)$ 解释成立，此处应使用去掉该增广项的复形 $0\to L_n\otimes N\to\cdots\to L_0\otimes N\to0$。例如取非零环 $R$、$M=N=R$，以及长度为 $0$ 的解消 $L_0=R\xrightarrow{\mathrm{id}}R$，原印 $K$ 为 $0\to R\xrightarrow{\mathrm{id}}R\to0$，其同调全为零；但 $\operatorname{Tor}_0(R,R)=R$，故原印的增广复形不能用于所述同调计算。

**证明。** 这些公式是定义与定理 3.1 的直接推论。

**例。** 设 $\mathfrak A$ 是某个交换环上的模组成的阿贝尔范畴，$\mathfrak C$ 是投射模族。从 §6 关于导出函子的论述中，读者将知道命题 3.10 中的复形 $K$ 的同调就是 $\operatorname{Tor}(M,N)$。所以该命题的公式也可以写成

$$
\operatorname{cl}_{\mathfrak C}(M)\operatorname{cl}_{\mathfrak A}(N)=\sum(-1)^i\operatorname{cl}_{\mathfrak A}(\operatorname{Tor}_i(M,N)).
$$

<span class="original-page-anchor" id="pdf-page-787" aria-hidden="true"></span>

**例。** 设 $k$ 是一个域，$G$ 是一个群。所谓 **$(G,k)$-模**，是指一个二元组 $(E,\rho)$，由一个 $k$-空间 $E$ 和一个同态

$$
\rho:G\to\operatorname{Aut}_k(E)
$$

组成。

这样的同态也称为 $G$ 在 $E$ 中的一个**表示**。为表述方便，也称 $k$-空间 $E$ 为一个 $G$-模。群 $G$ 作用于 $E$，并用 $\sigma x$ 代替 $\rho(\sigma)x$。以下始终固定域 $k$。

令 $\operatorname{Mod}_k(G)$ 表示以 $(G,k)$-模为对象的范畴。$\operatorname{Mod}_k(G)$ 中的态射称为 **$G$-同态**，即对所有 $\sigma\in G$ 都满足 $f(\sigma x)=\sigma f(x)$ 的 $k$-线性映射 $f:E\to F$。$\operatorname{Mod}_k(G)$ 中的态射群记为 $\operatorname{Hom}_G$。

若 $E$ 是一个 $G$-模，$\sigma\in G$，那么由定义有 $k$-自同构 $\sigma:E\to E$。由于 $T^r$ 是函子，对每个 $r$ 都有诱导的自同构

$$
T^r(\sigma):T^r(E)\to T^r(E),
$$

所以 $T^r(E)$ 也是一个 $G$-模。取直和，可知 $T(E)$ 是 $G$-模，因而 $T$ 是从 $G$-模范畴到分次 $G$-模范畴的函子。$\bigwedge^r,S^r$ 以及 $\bigwedge,S$ 也类似。

显然，$G$-同态的核是 $G$-子模，$G$-模对 $G$-子模的商也仍是 $G$-模，所以 $G$-模范畴是阿贝尔范畴。

现在可以应用关于 Grothendieck 群的一般论述；在当前情形，为简单起见，记作

$$
\mathbf K(G)=\mathbf K(\operatorname{Mod}_k(G)).
$$

有典范映射

$$
\operatorname{cl}:\operatorname{Mod}_k(G)\to\mathbf K(G),
$$

将每个 $G$-模映到其在 $\mathbf K(G)$ 中的类。

若 $E,F$ 是 $G$-模，那么它们在 $k$ 上的张量积 $E\otimes F$ 也是 $G$-模。这里，$G$ 在 $E\otimes F$ 上的作用同样由函子性给出。如果 $\sigma\in G$，则存在唯一的 $k$-线性映射 $E\otimes F\to E\otimes F$，使得对 $x\in E,y\in F$，有 $x\otimes y\mapsto(\sigma x)\otimes(\sigma y)$。张量积在 $\operatorname{Mod}_k(G)$ 上诱导一个合成律，因为 $G$-同构的模的张量积仍然 $G$-同构。

此外，条件 **TG 1** 至 **TG 4** 都满足。因为 $k$ 是域，$k$ 上的 $G$-模正合列与任意 $k$ 上的 $G$-模取张量积后仍保持正合性，所以 **TG 2** 对所有 $(G,k)$-模都满足。因此，Grothendieck 群 $\mathbf K(G)$ 实际上是 Grothendieck 环，或 $k$ 上的 Grothendieck 代数。

**译校注。** 原文末句称“$k$ 上的 Grothendieck 代数”。这里由直和与张量积构造出的结构是交换环，因而自然是 $\mathbf Z$-代数；域 $k$ 本身并没有自动在 $\mathbf K(G)$ 上给出 $k$-标量乘法。如果专指 $k$-代数，还需另行指定这种作用，或将环扩张为 $\mathbf K(G)\otimes_{\mathbf Z}k$。例如，对于平凡群的有限维表示，Grothendieck 环是 $\mathbf Z$，不能直接将其视为任意域 $k$ 上的代数。

<span class="original-page-anchor" id="pdf-page-788" aria-hidden="true"></span>

由第十八章命题 2.1 与定理 2.3，还可看出：

*由特征为 $0$ 的域 $k$ 上有限维 $(G,k)$-空间的同构类构成的有限群 $G$ 的 Grothendieck 环，自然同构于特征标环 $X_{\mathbf Z}(G)$。*

我们可以进一步将其公理化。考虑某个交换环 $R$ 上的模构成的阿贝尔范畴，为简单起见记为 $\mathfrak A$。对于 $\mathfrak A$ 中的两个模 $M,N$，像通常一样，用 $\operatorname{Mor}(M,N)$ 表示 $\mathfrak A$ 中的态射，但 $\operatorname{Mor}(M,N)$ 是 $\operatorname{Hom}_R(M,N)$ 的阿贝尔子群。例如，可以取 $\mathfrak A$ 为刚才讨论的 $(G,k)$-模范畴，此时 $\operatorname{Mor}(M,N)=\operatorname{Hom}_G(M,N)$。

令 $\mathfrak C$ 为 $\mathfrak A$ 中的有限生成自由模族。*假设 $\mathfrak C$ 满足* **TG 1、TG 2、TG 3、TG 4**，*并且对交错积、张量积及对称积封闭。* 令 $\mathbf K=\mathbf K(\mathfrak C)$。已经知道，$\mathbf K$ 本身是交换环。简记 $\operatorname{cl}_{\mathfrak C}=\operatorname{cl}$。

我们将利用交错积定义非线性映射

$$
\lambda^i:\mathbf K\to\mathbf K.
$$

若 $E$ 为有限生成自由模，令

$$
\lambda^i(E)=\operatorname{cl}(\bigwedge^iE).
$$

第十九章命题 1.1 现在可以在 **K** 环中表述如下。

**命题 3.11。** *设*

$$
0\to E'\to E\to E''\to0
$$

*为 $\mathfrak A$ 中有限生成自由模的正合列。那么对每个整数 $n\geqq0$ 都有*

$$
\lambda^n(E)=\sum_{i=0}^n\lambda^i(E')\lambda^{n-i}(E'').
$$

由此命题，可以定义映射

$$
\lambda_t:\mathbf K\to1+t\mathbf K[[t]],
$$

将 $\mathbf K$ 映入系数在 $\mathbf K$ 中、常数项为 $1$ 的形式幂级数的乘法群，定义为

$$
\lambda_t(x)=\sum_{i=0}^{\infty}\lambda^i(x)t^i.
$$

<span class="original-page-anchor" id="pdf-page-789" aria-hidden="true"></span>

第十九章命题 1.4 可以表述为：

*映射*

$$
\lambda_t:\mathbf K\to1+t\mathbf K[[t]]
$$

*是同态。*

*注意，若 $L$ 是秩为 $1$ 的自由模，那么*

$$
\begin{aligned}
\lambda^0(L)&=\text{基环};\\
\lambda^1(L)&=\operatorname{cl}(L);\\
\lambda^i(L)&=0\quad\text{当}\quad i>1.
\end{aligned}
$$

这可以概括为

$$
\lambda_t(L)=1+\operatorname{cl}(L)t.
$$

接下来，可以用对称积代替交错积，进行类似构造。若 $E$ 是 $\mathfrak C$ 中的有限生成自由模，像通常一样，令

$$
\begin{aligned}
S(E)&=E\text{ 的对称代数};\\
S^i(E)&=S(E)\text{ 中次数为 }i\text{ 的齐次分量}.
\end{aligned}
$$

定义

$$
\sigma^i(E)=\operatorname{cl}(S^i(E)),
$$

以及相应的幂级数

$$
\sigma_t(E)=\sum\sigma^i(E)t^i.
$$

**定理 3.12。** *设 $E$ 为 $\mathfrak A$ 中秩为 $r$ 的有限生成自由模。那么对所有整数 $n\geqq1$ 都有*

$$
\sum_{i=0}^r(-1)^i\lambda^i(E)\sigma^{n-i}(E)=0,
$$

*其中根据定义，当 $j<0$ 时 $\sigma^j(E)=0$。此外，*

$$
\sigma_t(E)\lambda_{-t}(E)=1,
$$

*所以幂级数 $\sigma_t(E)$ 与 $\lambda_{-t}(E)$ 互为逆元。*

**证明。** 第一个公式依赖于第十九章命题 1.1 中的公式关于对称积与交错积的类似形式。

<span class="original-page-anchor" id="pdf-page-790" aria-hidden="true"></span>

现在可以直接证明它，不过读者将在第二十一章推论 4.14 中，作为 Koszul 复形理论的一个特例看到证明。幂级数关系本质上是第一个公式的另一种表述。

利用上述形式，还可以定义 $\lambda^i$ 和 $\sigma^i$ 以外的其他映射。

**例。** 假设群 $G$ 是平凡群，并将 Grothendieck 环 $\mathbf K(1)$ 简记为 $\mathbf K$。对 $x\in\mathbf K$，定义

$$
\psi_{-t}(x)=-t\frac{d}{dt}\log\lambda_t(x)=-t\lambda'_t(x)/\lambda_t(x).
$$

证明 $\psi_{-t}$ 是可加且可乘的同态。证明

$$
\psi_t(E)=1+\operatorname{cl}(E)t+\operatorname{cl}(E)^2t^2+\cdots.
$$

**译校注。** 原文此式的常数项印为 $1$；根据前面的定义，应删去这个常数项，因为 $\lambda_t(x)$ 的常数项为 $1$，而 $-t\lambda'_t(x)/\lambda_t(x)$ 的常数项必为 $0$。例如在秩为 $1$ 的情形，$\lambda_{-t}(E)=1-\operatorname{cl}(E)t$，故 $\psi_t(E)=\operatorname{cl}(E)t/(1-\operatorname{cl}(E)t)=\operatorname{cl}(E)t+\operatorname{cl}(E)^2t^2+\cdots$。

该幂次展开还需限定为上述秩为 $1$ 的类，不能直接用于任意 $E$。例如在平凡群的情形，若 $E$ 的秩为 $2$，则 $\lambda_t(E)=(1+t)^2$，由定义得 $\psi_t(E)=2t/(1-t)=2t+2t^2+\cdots$，而 $\operatorname{cl}(E)=2$，原列式的二次项系数却为 $2^2=4$。

这种利用对数导数的构造引出拓扑学与代数几何中的 **Adams 运算** $\psi^i$。参见第十八章习题 22。

**注。** 如果在定理 3.12 中，$E$ 在 **K** 群中能分解为一维自由模，那么利用当 $L$ 为一维时 $\lambda_t(L)=1+\operatorname{cl}(L)t$ 这一事实，证明就变得十分简单。但在 $k$ 为域的 $(G,k)$-空间的例子中，这通常办不到，在拓扑学与代数几何中自然出现的其他例子中也办不到。不过，通过“改变基底”，有时可以达到这种较简单的情形，而此时会用定理 3.12 来确立基本性质。参见第四部分导言中提到的 Grothendieck [SGA 6]，以及章末参考文献中的其他著作，即 [Ma 69]、[At 61]、[At 67]、[Ba 68]、[Bo 62]。Atiyah 和 Bott 的讲义侧重拓扑方面，与代数几何方面有所区别。Grothendieck [Gr 68] 实际说明，来自代数几何与拓扑学的陈类形式也进入了线性群的表示理论。另见 [FuL 85] 中的论述，特别是第一章 §6 的形式。关于表示论应用的专门论述，可参阅 Bröcker-tom Dieck [BtD 85]，特别是第二章 §7 中关于紧李群的内容。

## §4. 内射模

第三章 §4 定义了投射模，它们与自由模有自然联系。将箭头反向，可以定义模 $Q$ 为**内射模**，条件是它满足下面任意一个彼此等价的条件：

**I 1。** 给定任意模 $M$、子模 $M'$ 以及同态 $f:M'\to Q$，存在这一同态到 $M$ 的延拓，<span class="original-page-anchor" id="pdf-page-791" aria-hidden="true"></span>即存在 $h:M\to Q$，使下图交换：

![内射性定义中到 M 的延拓](/library/volume-86/diagrams/pdf-0791-injective-extension.png)

**I 2。** 函子 $M\mapsto\operatorname{Hom}_A(M,Q)$ 正合。

**I 3。** 每个正合列 $0\to Q\to M\to M''\to0$ 都分裂。

下面证明这些条件等价。如命题 2.1 中关于同态的一般论述所示，施行 Hom 后所得序列的正合性，只可能在一个地方失效，即给定

$$
0\to M'\to M\to M''\to0,
$$

问题在于

$$
\operatorname{Hom}_A(M,Q)\to\operatorname{Hom}_A(M',Q)\to0
$$

是否正合。但这恰好就是 **I 1** 中所表述的假设，所以 **I 1** 推出 **I 2** 本质上只是换一种说法；事实上，**I 1** 与 **I 2** 等价。

假设 **I 2** 或 **I 1** 成立，已经知道二者等价。对下图应用 **I 1**，立即得到 **I 3**：

![由内射性得到的收缩映射](/library/volume-86/diagrams/pdf-0791-injective-retraction.png)

要证明逆向蕴含，需要推出的概念（参见第一章习题 52）。给定正合图

![用于构造推出的正合图](/library/volume-86/diagrams/pdf-0791-pushout-input.png)

构造推出：

![推出 Q 在 M' 上与 M 的和](/library/volume-86/diagrams/pdf-0791-pushout-square.png)

<span class="original-page-anchor" id="pdf-page-792" aria-hidden="true"></span>

由于 $M'\to M$ 是单态射，从推出的构造立即可验证，$Q\to N$ 也是单态射。由 **I 3**，序列

$$
0\to Q\to N
$$

分裂。现在将分裂映射 $N\to Q$ 与推出映射 $M\to N$ 复合，就得到所需的 $h:M\to Q$，从而证明 **I 1**。

我们很容易看出，每个模都是某个自由模的同态像。但对于其对偶事实，没有同样直接的构造：

**定理 4.1。** *每个模都是某个内射模的子模。*

证明将通过对偶化并借助几个引理给出。先考虑阿贝尔群范畴中的情形。若 $M$ 是阿贝尔群，令其对偶群为 $M^\wedge=\operatorname{Hom}(M,\mathbf Q/\mathbf Z)$。若 $F$ 是自由阿贝尔群，合理地预期其对偶 $F^\wedge$ 为内射模；事实上这很容易证明，因为内射性是投射性的对偶概念。此外，$M$ 有一个到双对偶 $M^{\wedge\wedge}$ 的自然映射，可以证明这是单态射。现在将 $M^\wedge$ 表示为某个自由阿贝尔群的商，

$$
F\to M^\wedge\to0.
$$

对这一序列取对偶，得到单态射

$$
0\to M^{\wedge\wedge}\to F^\wedge.
$$

由于 $M$ 自然地作为子群嵌入 $M^{\wedge\wedge}$，于是得到所需的嵌入，将 $M$ 作为子群嵌入 $F^\wedge$。

这个证明在一般情形也适用，不过有一些细节需要补充。首先要证明自由模的对偶是内射的；其次，从阿贝尔群范畴过渡到任意环上的模范畴时必须谨慎。现在补充这些细节。

如果对每个整数 $m$，同态

$$
m_T:x\mapsto mx
$$

都是满射，就称阿贝尔群 $T$ 为**可除群**。

**译校注。** 原文印为“对每个整数 $m$”；这里应限定 $m\ne0$（等价地，只需所有正整数）。若包含 $m=0$，则 $m_T$ 是零映射，只有 $T=0$ 时它才满射，这与下一页给出的非零可除群 $\mathbf Q/\mathbf Z$、$\mathbf R/\mathbf Z$ 的例子不符。

**引理 4.2。** *若 $T$ 可除，那么它在阿贝尔群范畴中是内射的。*

**证明。** 设 $M'\subset M$ 是某个阿贝尔群的子群，$f:M'\to T$ 是同态。设 $x\in M$。首先要将 $f$ 延拓到由 $M'$ 与 $x$ 生成的模 $(M',x)$。若 $x$ 在 $M'$ 上自由，就任取一个值 $t\in T$，并令 $f(x)=t$；立即可验证，$f$ 延拓到 $(M',x)$。假设 $x$ 相对于 $M'$ 是挠的，即存在正整数 $m$ 使 $mx\in M'$。令 $d$ 为 $x\bmod M'$ 的周期，于是<span class="original-page-anchor" id="pdf-page-793" aria-hidden="true"></span>$dx\in M'$，且 $d$ 为满足 $dx\in M'$ 的最小正整数。由假设，存在元素 $u\in T$，使得 $du=f(dx)$。对任意整数 $n$ 及 $z\in M'$，定义

$$
f(z+nx)=f(z)+nu.
$$

根据 $d$ 的定义以及 $\mathbf Z$ 是主理想整环这一事实，可知 $f$ 的这个值与 $(M',x)$ 中元素写为 $z+nx$ 的表示方式无关。随后立即可知，这样延拓定义的 $f$ 是同态。因此，已将 $f$ 延拓到 $(M',x)$。

证明的其余部分只是佐恩引理的应用。考虑二元组 $(N,g)$，其中 $N$ 是 $M$ 的包含 $M'$ 的子模，$g$ 是 $f$ 到 $N$ 的延拓。如果 $N\subset N_1$，且 $g_1$ 在 $N$ 上的限制为 $g$，就定义 $(N,g)\leqq(N_1,g_1)$。这些二元组构成归纳有序集。设 $(N,g)$ 为极大元素。如果 $N\ne M$，就存在某个 $x\in M,x\notin N$，并可应用证明的第一部分，将同态延拓到 $(N,x)$。这与极大性矛盾，引理得证。

**例。** 阿贝尔群 $\mathbf Q/\mathbf Z$ 与 $\mathbf R/\mathbf Z$ 都可除，因此在阿贝尔群范畴中是内射的。

遵照前面描述的方法，就能在阿贝尔群范畴中证明定理 4.1。若 $F$ 为自由阿贝尔群，那么对偶 $F^\wedge$ 是同构于 $\mathbf Q/\mathbf Z$ 的群的直积，所以由引理 4.2，它在阿贝尔群范畴中是内射的。证明完成。

接下来，必须作出必要的说明，将这一体系扩展到模。设 $A$ 是一个环，$T$ 是一个阿贝尔群。如下将 $\operatorname{Hom}_{\mathbf Z}(A,T)$ 赋予 $A$-模结构。设 $f:A\to T$ 为阿贝尔群同态。对 $a\in A$，定义作用

$$
(af)(b)=f(ba).
$$

作用的法则立即可验证。于是对任意 $A$-模 $X$，有阿贝尔群的自然同构

$$
\operatorname{Hom}_{\mathbf Z}(X,T)\xrightarrow{\approx}\operatorname{Hom}_A(X,\operatorname{Hom}_{\mathbf Z}(A,T)).
$$

确实，设 $\psi:X\to T$ 是 $\mathbf Z$-同态。与 $\psi$ 相伴的同态为

$$
f:X\to\operatorname{Hom}_{\mathbf Z}(A,T),
$$

其中

$$
f(x)(a)=\psi(ax).
$$

<span class="original-page-anchor" id="pdf-page-794" aria-hidden="true"></span>

由 $\operatorname{Hom}_{\mathbf Z}(A,T)$ 上的 $A$-模结构的定义，$f$ 是 $A$-同态，因此得到从 $\operatorname{Hom}_{\mathbf Z}(X,T)$ 到

$$
\operatorname{Hom}_A(X,\operatorname{Hom}_{\mathbf Z}(A,T))
$$

的箭头。

反过来，设 $f:X\to\operatorname{Hom}_{\mathbf Z}(A,T)$ 是 $A$-同态。定义相应的 $\psi$ 为

$$
\psi(x)=f(x)(1).
$$

立即可验证，这些映射互为逆映射。

我们将在 $T$ 为任意可除群时应用这一结果，不过可以把 $T$ 想成 $\mathbf Q/\mathbf Z$，并按前面的方法将到 $T$ 的同态看成对偶群的元素。

**引理 4.3。** *若 $T$ 为可除阿贝尔群，那么 $\operatorname{Hom}_{\mathbf Z}(A,T)$ 在 $A$-模范畴中是内射的。*

**证明。** 只需证明：如果 $0\to X\to Y$ 在 $A$-模范畴中正合，那么取到 $\operatorname{Hom}_{\mathbf Z}(A,T)$ 的 $A$-同态所得的对偶序列正合，即下图顶端的映射是满射。

![证明 Hom 在 Z 上构造的模为内射模的交换图](/library/volume-86/diagrams/pdf-0794-coinduced-injective.png)

但是，引理之前描述的同构就是交换图中的竖直箭头。底端映射为满射，因为 $T$ 在阿贝尔群范畴中为内射模。因此顶端映射也是满射，引理得证。

现在对 $A$-模证明定理 4.1。设 $M$ 为 $A$-模。可以将 $M$ 嵌入某个可除阿贝尔群 $T$，

$$
0\to M\xrightarrow{f}T.
$$

然后通过 $x\mapsto f_x$，其中 $f_x(a)=f(ax)$，得到 $A$-同态

$$
M\to\operatorname{Hom}_{\mathbf Z}(A,T).
$$

立即可验证，$x\mapsto f_x$ 给出 $M$ 到 $\operatorname{Hom}_{\mathbf Z}(A,T)$ 的嵌入；后者由引理 4.3 为内射模。定理 4.1 得证。

<span class="original-page-anchor" id="pdf-page-795" aria-hidden="true"></span>

## §5. 复形态射的同伦

本节旨在描述一个条件，使复形同态在同调上诱导相同的映射，并说明这一条件在一个重要情形下满足；下一节将由此导出一些应用。

论证适用于任意阿贝尔范畴。读者可能更愿意考虑模，但我们采用同时适用于二者的语言，其复杂程度并不超过只处理模时的表述。

设 $E=\{(E^n,d^n)\}$ 与 $E'=\{(E'^n,d'^n)\}$ 为两个复形。设

$$
f,g:E\to E'
$$

为两个次数为 $0$ 的复形态射。如果存在一列同态

$$
h_n:E^n\to E'^{(n-1)},
$$

使得

$$
f_n-g_n=d'^{(n-1)}h_n+h_{n+1}d^n,
$$

就称 $f$ 与 $g$ **同伦**。

**引理 5.1。** *若 $f,g$ 同伦，那么 $f,g$ 在同调 $H(E)$ 上诱导相同的同态，即*

$$
H(f_n)=H(g_n):H^n(E)\to H^n(E').
$$

**证明。** 引理是直接的，因为 $f_n-g_n$ 在循环上为零，而循环就是 $d^n$ 的核；同伦条件还说明 $f_n-g_n$ 的像包含于边缘中，即包含于 $d'^{(n-1)}$ 的像中。

**译校注。** 原文称“$f_n-g_n$ 在循环上为零”；准确地说，在循环 $z$ 上为零的是 $h_{n+1}d^n(z)$，因此 $(f_n-g_n)(z)=d'^{(n-1)}h_n(z)$ 是边缘，并不必为零。由此在同调商群上才有 $H(f_n)=H(g_n)$。同样，关于像落在边缘中的结论是在限制到循环之后成立。

**注。** 使用同伦这一术语，是因为此概念与形式最初出现在拓扑学中。参见 [ES 52] 与 [GreH 81]。

将引理 5.1 应用于内射对象。注意，像通常一样，内射模的定义无需改变，就可用来定义任意阿贝尔范畴中的内射对象。在 **I 1** 中，用子对象或等价的单态射代替子模即可。定义内射模的三个条件的等价性证明，只依赖于箭头之间的操作，因此也适用于一般阿贝尔范畴。

如果对任意给定的对象 $M$，都存在单态射

$$
0\to M\to I,
$$

就称阿贝尔范畴具有**足够多的内射对象**，其中 $I$ 为<span class="original-page-anchor" id="pdf-page-796" aria-hidden="true"></span>内射对象。在 §4 中已经证明，某个环上的模范畴具有足够多的内射对象。*现在假设所处理的阿贝尔范畴具有足够多的内射对象。*

对象 $M$ 的一个**内射解消**，是指正合列

$$
0\to M\to I^0\to I^1\to I^2\to,
$$

其中每个 $I_n$（$n\geqq0$）都是内射的。给定 $M$，这样的解消存在。确实，由假设存在单态射

$$
0\to M\to I^0.
$$

令 $M^0$ 为它的像。再由假设，存在单态射

$$
0\to I^0/M^0\to I^1,
$$

而相应同态 $I^0\to I^1$ 的核为 $M^0$。这样就构造了解消的第一步，后面的步骤以同样方式进行。

内射解消当然不唯一，但具有某种唯一性，现在将它表述出来。

**引理 5.2。** *考虑两个复形：*

![两个增广复形及其初始对象间的同态](/library/volume-86/diagrams/pdf-0796-injective-comparison.png)

*假设顶端一行正合，并且每个 $I^n$（$n\geqq0$）都是内射的。设 $\varphi:M\to M'$ 是给定的同态。那么存在复形态射 $f$，使得 $f_{-1}=\varphi$；任意两个这样的态射都同伦。*

**证明。** 由内射对象的定义，经由 $M'$ 的同态 $M\to I^0$ 可以延拓为同态

$$
f_0:E^0\to I^0,
$$

使第一个方块交换：

![比较构造中的第一个交换方块](/library/volume-86/diagrams/pdf-0796-comparison-first-square.png)

<span class="original-page-anchor" id="pdf-page-797" aria-hidden="true"></span>

接下来要构造 $f_1$。将第二个方块写成

![比较构造中的第二个方块](/library/volume-86/diagrams/pdf-0797-comparison-second-square.png)

其中顶端一行如图所示正合。再利用 $I^1$ 的内射性，可以应用同样的论证，找到 $f_1$ 使第二个方块交换。继续这样做，就构造出复形态射 $f$。

**译校注。** 原图把商模 $E^0/M$ 到 $I^0$ 的箭头仍标为 $f_0$；一般而言 $f_0$ 在 $M$ 上并不为零，不能直接下降为这个箭头。实际用于延拓的映射是 $d'^0f_0:E^0\to I^1$，它在 $M$ 上为零，因而诱导 $E^0/M\to I^1$；沿 $E^0/M\hookrightarrow E^1$，利用 $I^1$ 的内射性将其延拓为 $f_1$。

假设 $f,g$ 为两个这样的态射。定义 $h_0:E^0\to M'$ 为 $0$。此时，在初始位置

$$
f_{-1}=g_{-1}=\varphi
$$

的情况下，同伦条件成立。

再令 $d^{-1}:M\to E^0$ 为 $M$ 到 $E^0$ 的嵌入。由于 $I^0$ 内射，可以将

$$
d^0:E^0/\operatorname{Im}d^{-1}\to E_1
$$

延拓为同态 $h_1:E^1\to I^0$。于是 $f_0-g_0$ 的同伦条件得到验证。由于 $h_0=0$，此时实际上有

**译校注。** 原文称将 $d^0:E^0/\operatorname{Im}d^{-1}\to E_1$ 延拓为 $h_1:E^1\to I^0$。这里 $d^0$ 是用于嵌入源对象的单态射；真正要延拓的是 $f_0-g_0$ 在商模上诱导的映射 $E^0/\operatorname{Im}d^{-1}\to I^0$。它能下降到商模，是因为 $f_{-1}=g_{-1}$；延拓之后才有下面的等式。

$$
f_0-g_0=h_1d^0.
$$

不过，这一简化对后面的归纳步骤容易造成误导。假设已构造映射 $h_{n+1}$，要证明存在 $h_{n+2}$，使

$$
f_{n+1}-g_{n+1}=d'^nh_{n+1}+h_{n+2}d^{n+1}.
$$

由于 $\operatorname{Im}d^n=\operatorname{Ker}d^{n+1}$，有单态射 $E^{n+1}/\operatorname{Im}d^n\to E^{n+2}$。根据内射对象的定义，这里的内射对象是 $I^{n+1}$，只需证明

$$
f_{n+1}-g_{n+1}-d'^nh_{n+1}\quad\text{在 }d^n\text{ 的像上为零},
$$

并使用正合图

![延拓同伦所用的正合图](/library/volume-86/diagrams/pdf-0797-homotopy-extension.png)

就可得到 $h_{n+2}:E^{n+2}\to I^{n+1}$，延拓 $f_{n+1}-g_{n+1}$。但是有：

**译校注。** 此处原图的竖直箭头及原文的延拓对象都只写了 $f_{n+1}-g_{n+1}$，应为完整差 $f_{n+1}-g_{n+1}-d'^nh_{n+1}$。前文要证明在 $\operatorname{Im}d^n$ 上为零的是这个完整差，后面的计算也是针对它；因此下降到商模并被 $h_{n+2}$ 延拓的正是它。

$$
\begin{aligned}
&(f_{n+1}-g_{n+1}-d'^nh_{n+1})d^n\\
&\qquad=(f_{n+1}-g_{n+1})d^n-d'^nh_{n+1}d^n.
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-798" aria-hidden="true"></span>

$$
\begin{aligned}
&=(f_{n+1}-g_{n+1})d^n-d'^n(f_n-g_n-d'^{(n-1)}h_n)&&\text{由归纳假设}\\
&=(f_{n+1}-g_{n+1})d^n-d'^n(f_n-g_n)&&\text{因为 }d'd'=0\\
&=0&&\text{因为 }f,g\text{ 是复形同态。}
\end{aligned}
$$

引理 5.2 的证明至此完成。

**注。** 对偶地，设 $P_{M'}\to M'\to0$ 是一个复形，其中对 $i\geqq0$，$P^i$ 都为投射对象；设 $E_M\to M\to0$ 是一个解消。设 $\varphi:M'\to M$ 为同态。那么 $\varphi$ 延拓为复形同态 $P\to E$。将引理 5.2 中的箭头反向，就得到证明。据我所知，同调代数教材实际上都处理投射情形，将内射情形留给读者。不过，我在这里的动机之一，是完成例如 [Ha 77] 第三章关于导出函子所需的内容，作为层上同调的预备。关于利用自由模的投射解消的例子，可参阅涉及群上同调的习题 2–7。

## §6. 导出函子

继续在阿贝尔范畴中工作。如果协变可加函子

$$
F:\mathfrak A\to\mathfrak B
$$

将正合列

$$
0\to M'\to M\to M''
$$

变为正合列 $0\to F(M')\to F(M)\to F(M'')$，就称 $F$ 为**左正合**的。提醒读者，若映射

$$
\operatorname{Hom}(A',A)\to\operatorname{Hom}(FA',FA)
$$

可加，就称 $F$ 为**可加函子**。

*除非另有说明，始终假设 $F$ 左正合且可加。继续假设所用的阿贝尔范畴具有足够多的内射对象。*

给定对象 $M$，设

$$
0\to M\to I^0\to I^1\to I^2\to
$$

是内射解消，将其简记为

$$
0\to M\to I_M,
$$

其中 $I_M$ 是复形 $I^0\to I^1\to I^2\to$。用 $I$ 表示复形

$$
0\to I^0\to I^1\to I^2\to
$$

<span class="original-page-anchor" id="pdf-page-799" aria-hidden="true"></span>

通过

$$
R^nF(M)=H^n(F(I))
$$

定义**右导出函子** $R^nF$；换言之，它是复形

$$
0\to F(I^0)\to F(I^1)\to F(I^2)\to
$$

的第 $n$ 个同调。

直接从定义以及单态射 $M\to I_0$ 可知，有同构

$$
R^0F(M)=F(M).
$$

乍看之下，这个同构似乎依赖于所选的内射解消，其他 $n$ 对应的函子 $R^nF(M)$ 也是如此。不过，由引理 5.1 与 5.2 可知，给定 $M$ 的两个内射解消，它们之间存在同态，并且任意两个这样的同态都同伦。将函子 $F$ 应用于这些同态及同伦，就可知复形 $F(I)$ 的同调实际上在唯一同构的意义下确定。因此，记号与表述中都省去所选解消。

**例 1。** 设 $R$ 为环，$\mathfrak A=\operatorname{Mod}(R)$ 为 $R$-模范畴。固定一个模 $A$。函子 $M\mapsto\operatorname{Hom}(A,M)$ 左正合，即给定正合列 $0\to M'\to M\to M''$，序列

$$
0\to\operatorname{Hom}(A,M')\to\operatorname{Hom}(A,M)\to\operatorname{Hom}(A,M'')
$$

正合。当 $M$ 变化时，其右导出函子记为 $\operatorname{Ext}^n(A,M)$。类似地，固定模 $B$ 时，函子 $X\mapsto\operatorname{Hom}(X,B)$ 右正合，并产生其**左导出函子**。这些术语的明确对偶表述见本节末尾。无论如何，也可以让 $A$ 变化。§8 将通过处理双函子，更深入地研究这一方面的形式。届时将看到，$\operatorname{Ext}^n(A,B)$ 既可解释为第一个变量的左导出函子，也可解释为第二个变量的右导出函子。参见推论 8.5。

在习题中，你将证明 $\operatorname{Ext}^1(A,M)$ 与 $M$ 被 $A$ 扩张的同构类一一对应，即与正合列

$$
0\to A\to E\to M\to0
$$

的同构类一一对应。

**译校注。** 按本页前面将 $\operatorname{Ext}^n(A,M)$ 定义为 $\operatorname{Hom}(A,-)$ 的右导出函子的约定，原印序列 $0\to A\to E\to M\to0$ 分类的是 $\operatorname{Ext}^1(M,A)$；$\operatorname{Ext}^1(A,M)$ 对应的序列应为 $0\to M\to E\to A\to0$。例如，取 $R=\mathbf Z$、$A=\mathbf Z$、$M=\mathbf Z/n\mathbf Z$（$n>1$），则 $\operatorname{Ext}^1(\mathbf Z,\mathbf Z/n\mathbf Z)=0$，而原次序下的序列 $0\to\mathbf Z\xrightarrow{n}\mathbf Z\to\mathbf Z/n\mathbf Z\to0$ 不分裂，不能由该零群分类。

Ext 这一名称来自维数 $1$ 时的这种解释。

关于某些重要情形下 $\operatorname{Ext}^i$ 的计算，参见第二十一章定理 4.6 与 4.11，它们为一般理论提供例子。

**例 2。** 设 $R$ 为交换环。函子 $M\mapsto A\otimes M$ 右正合，即序列

$$
A\otimes M'\to A\otimes M\to A\otimes M''\to0
$$

正合。当 $M$ 变化时，其左导出函子记为 $\operatorname{Tor}_n(A,M)$。

<span class="original-page-anchor" id="pdf-page-800" aria-hidden="true"></span>

**例 3。** 设 $G$ 为群，$R=\mathbf Z[G]$ 为群环。令 $\mathfrak A$ 为 $G$-模范畴，即 $\mathfrak A=\operatorname{Mod}(R)$，也记为 $\operatorname{Mod}(G)$。对于 $G$-模 $A$，令 $A^G$ 为由对所有 $x\in G$ 都满足 $xv=v$ 的元素 $v$ 组成的子模（阿贝尔群）。那么 $A\mapsto A^G$ 是从 $\operatorname{Mod}(R)$ 到阿贝尔群范畴的左正合函子。其左导出函子产生群的上同调。习题中将给出这一特殊上同调的一些结果，作为一般理论的进一步例子。

**译校注。** 原文这里印为“left derived functors”（左导出函子）。不变元函子 $A\mapsto A^G$ 是协变左正合函子，按本节定义应取其**右导出函子**来得到群上同调；下一例关于整体截面的同类构造也明确使用右导出函子。

**例 4。** 设 $X$ 为拓扑空间（假定读者知道其含义）。所谓 $X$ 上的阿贝尔群**层** $\mathfrak F$，是指以下数据：

**(a)** 对 $X$ 的每个开集 $U$，给定一个阿贝尔群 $\mathfrak F(U)$。

**(b)** 对开集之间的每个包含关系 $V\subset U$，给定同态

$$
\operatorname{res}^U_V:\mathfrak F(U)\to\mathfrak F(V),
$$

称为从 $U$ 到 $V$ 的**限制映射**，并满足下列条件：

**SH 1。** $\mathfrak F(\text{空集})=0$。

**SH 2。** $\operatorname{res}^U_U$ 是恒等映射 $\mathfrak F(U)\to\mathfrak F(U)$。

**SH 3。** 若 $W\subset V\subset U$ 为开集，则 $\operatorname{res}^V_W\circ\operatorname{res}^U_V=\operatorname{res}^U_W$。

**SH 4。** 设 $U$ 为开集，$\{V_i\}$ 为 $U$ 的开覆盖。设 $s\in\mathfrak F(U)$。如果 $s$ 在每个 $V_i$ 上的限制为 $0$，那么 $s=0$。

**SH 5。** 设 $U$ 为开集，$\{V_i\}$ 为 $U$ 的开覆盖。对每个 $i$，给定 $s_i\in\mathfrak F(V_i)$，使任意给定的 $i,j$ 对应的 $s_i,s_j$ 在 $V_i\cap V_j$ 上的限制相等。那么存在唯一的 $s\in\mathfrak F(U)$，对所有 $i$，其在 $V_i$ 上的限制都是 $s_i$。

$\mathfrak F(U)$ 的元素称为 $\mathfrak F$ 在 $U$ 上的**截面**，$\mathfrak F(X)$ 的元素称为**整体截面**。像阿贝尔群一样，可以定义层的同态、核、余核与正合列。对应 $\mathfrak F\mapsto\mathfrak F(X)$（整体截面函子）是从阿贝尔群层范畴到阿贝尔群范畴的函子，并且左正合。其右导出函子是拓扑学与代数几何（以及其他数学领域）中上同调理论的基础。在 [Ha 77] 第二章 §1 中，读者可以找到基本性质的简洁而自足的定义，以及这些对象构成阿贝尔范畴的证明。若需更详细的论述，我推荐第四部分导言中提到的 Gunning [Gu 91]，特别是论述层上同调的第三卷。

现在回到导出函子的一般理论。一般理论告诉我们，这些导出函子并不依赖于按函子的变性所选的投射或内射解消。§8 还将说明，甚至可以使用无环或正合等其他特殊类型的对象（稍后定义），从而使计算同调的方法更加灵活。通过某些显式解消，我们得到显式计算导出函子的<span class="original-page-anchor" id="pdf-page-801" aria-hidden="true"></span>方法。例如，在习题 16 中，通过给出适用于有限循环群的某个特定的 $\mathbf Z$ 的自由解消，就能直接计算其上同调。第二十一章将提供若干其他例子，说明如何构造显式的有限自由解消，从而确定各种情形下的导出函子。

下面的定理概括导出函子的基本性质。

**定理 6.1。** *设 $\mathfrak A$ 为具有足够多内射对象的阿贝尔范畴，$F:\mathfrak A\to\mathfrak B$ 为到另一个阿贝尔范畴 $\mathfrak B$ 的协变可加左正合函子。那么：*

**(i)** *对每个 $n\geqq0$，上面定义的 $R^nF$ 是从 $\mathfrak A$ 到 $\mathfrak B$ 的可加函子。此外，在函子的唯一同构意义下，它与所选的解消无关。*

**(ii)** *有自然同构 $F\approx R^0F$。*

**(iii)** *对每个短正合列*

$$
0\to M'\to M\to M''\to0
$$

*以及每个 $n\geqq0$，存在自然同态*

$$
\delta^n:R^nF(M'')\to R^{n+1}F(M),
$$

**译校注。** 原文此处的目标印为 $R^{n+1}F(M)$，应为 $R^{n+1}F(M')$。连接同态将短正合列的末项的第 $n$ 个同调映到首项的第 $n+1$ 个同调；紧接着的长正合列以及 (iv) 中的交换图也都使用 $M'$。

*使得得到长正合列：*

$$
\to R^nF(M')\to R^nF(M)\to R^nF(M'')\xrightarrow{\delta^n}R^{n+1}F(M')\to.
$$

**(iv)** *给定短正合列的态射*

![短正合列的态射](/library/volume-86/diagrams/pdf-0801-derived-naturality-input.png)

*各 $\delta$ 给出交换图：*

![连接同态的自然性](/library/volume-86/diagrams/pdf-0801-derived-naturality-square.png)

**(v)** *对 $A$ 的每个内射对象 $I$ 以及每个 $n>0$，都有 $R^nF(I)=0$。*

性质 (i)、(ii)、(iii)、(iv) 本质上说明 $R^nF$ 是一个 delta 函子，其含义将在下一节展开。最后的性质 (v) 将在处理完定理中关于 delta 函子的部分后讨论。

<span class="original-page-anchor" id="pdf-page-802" aria-hidden="true"></span>

现在描述如何构造 $\delta$-同态。给定一个短正合列，可以分别找到 $M',M,M''$ 的内射解消，但它们未必组成复形的正合列。因此必须做到这一点，才能应用 §1 的论述。考虑图：

![相容内射解消的初始图](/library/volume-86/diagrams/pdf-0802-injective-horseshoe-initial.png)

给定到内射对象的单态射 $M'\to I'^0$ 与 $M''\to I''^0$，要找到内射对象 $X$ 以及单态射 $M\to X$，使图正合。取 $X$ 为直和

$$
X=I'^0\oplus I''^0.
$$

由于 $I'^0$ 内射，单态射 $M'\to I'^0$ 可以延拓为同态 $M\to I'^0$。取 $M$ 到 $I'^0\oplus I''^0$ 的同态，其在第一个因子 $I'^0$ 上的分量由这个延拓给出，而在第二个因子上的分量为复合映射

$$
M\to M''\to I''^0.
$$

于是 $M\to X$ 是单态射。此外，$I'^0\to X$ 是到第一个因子的单态射，$X\to I''^0$ 是到第二个因子的投影。这样就构造了所需的图，给出相容解消的开端。

现在取商同态，定义第三行，得到正合图：

![内射解消下一步所用的商图](/library/volume-86/diagrams/pdf-0802-injective-horseshoe-quotients.png)

<span class="original-page-anchor" id="pdf-page-803" aria-hidden="true"></span>

其中令 $I^0=X$，而 $N',N,N''$ 按定义分别为各竖直映射的余核。$N$ 序列的正合性留给读者作为练习。再对 $N$ 序列重复这一构造，通过归纳，构造 $M$ 序列的内射解消

![短正合列的相容内射解消](/library/volume-86/diagrams/pdf-0803-compatible-injective-resolutions.png)

使这些解消组成的图正合。

现在将函子 $F$ 应用于这一图，得到复形的短序列

$$
0\to F(I')\to F(I)\to F(I'')\to0.
$$

它是正合的，因为 $I=I'\oplus I''$ 为直和，且 $F$ 左正合，因而 $F$ 与直和交换。现在可以应用 §1 的构造，得到同调序列中的上边缘算子：

$$
R^nF(M')\to R^nF(M)\to R^nF(M'')\xrightarrow{\delta^n}R^{n+1}F(M').
$$

由于右导出函子与所选解消无关，这样做是合理的。

至此，已经证明 (i)、(ii)、(iii)。为了证明 (iv)，即 delta 同态的自然性，需要处理一个三维交换图。这里我认为最好把它留给读者，因为只是重复相同的常规步骤。

最后，性质 (v) 是显然的，因为如果 $I$ 内射，就可以用解消

$$
0\to I\to I\to0
$$

计算导出函子，由此显然当 $n>0$ 时 $R^nF=0$。定理 6.1 的证明至此完成。

在应用中，通过内射解消以外的其他解消来确定导出函子很有用（内射解消适合理论用途，却不适合计算用途）。再次设 $F$ 为左正合可加函子。如果对所有 $n>0$，$R^nF(X)=0$，就称对象 $X$ 为 **$F$-无环的**。

<span class="original-page-anchor" id="pdf-page-804" aria-hidden="true"></span>

**定理 6.2。** *设*

$$
0\to M\to X^0\to X^1\to X^2\to\cdots
$$

*是 $M$ 的一个由 $F$-无环对象组成的解消。设*

$$
0\to M\to I^0\to I^1\to I^2\to\cdots
$$

*是内射解消。那么存在复形态射 $X_M\to I_M$，延拓 $M$ 上的恒等映射；这个态射对所有 $n\geqq0$ 都诱导同构*

$$
H^nF(X)\approx H^nF(I)=R^nF(M).
$$

**证明。** 延拓 $M$ 上恒等映射的复形态射的存在性，就是引理 5.2。这个定理通常通过谱序列证明，但也可以以下面的方式独立表述，这一方法由 David Benson 告诉我。需要一个引理。

**引理 6.3。** *设 $Y^i$（$i\geqq0$）为 $F$-无环对象，并假设序列*

$$
0\to Y^0\to Y^1\to Y^2\to\cdots
$$

*正合。那么*

$$
0\to F(Y^0)\to F(Y^1)\to F(Y^2)\to\cdots
$$

*正合。*

**证明。** 由于 $F$ 左正合，有正合列

$$
0\to F(Y^0)\to F(Y^1)\to F(Y^2).
$$

要说明下一个连接处的正合性。将余核画出：

![F-无环对象正合列中的余核](/library/volume-86/diagrams/pdf-0804-acyclic-cokernels.png)

于是 $Z_1=\operatorname{Coker}(Y^0\to Y^1)$，$Z_2=\operatorname{Coker}(Y^1\to Y^2)$，依此类推。应用 $F$，得到正合列

$$
0\to F(Y^0)\to F(Y^1)\to F(Z^1)\to R^1F(Y^0)=0.
$$

<span class="original-page-anchor" id="pdf-page-805" aria-hidden="true"></span>

所以 $F(Z_1)=\operatorname{Coker}(F(Y^0)\to F(Y^1))$。现在考察正合列

$$
0\to Z_1\to Y_2\to Y_3,
$$

由 $F$ 的左正合性得到正合列

$$
0\to F(Z^1)\to F(Y^2)\to F(Y^3),
$$

这就证明了所需的结论。不过现在可以继续作归纳，因为由正合列

$$
0\to R^nF(Y^1)\to R^nF(Z^1)\to R^{n+1}F(Y^0)=0
$$

可知 $Z_1$ 是 $F$-无环的。

引理 6.3 的证明至此完成。

回到定理 6.2 的证明。可以选取内射解消

$$
0\to M\to I_M,
$$

使同态 $X_n\to I_n$ 对于 $n\geqq0$ 都是单态，因为导出函子与内射解消的选取无关。因此不失一般性，可以假定有如下正合图：

![比较 X 与 I 并定义 Y 的正合图](/library/volume-86/diagrams/pdf-0805-acyclic-resolution-grid.png)

其中 $Y^n$ 定义为相应竖直映射的余核。

由于 $X^n$ 和 $I^n$ 都无环，由正合列

$$
R^kF(I^n)\to R^kF(Y^n)\to R^{k+1}F(X^n)
$$

可知 $Y^n$ 也无环。

施行 $F$，得到复形的短正合列

$$
0\to F(X)\to F(I)\to F(Y)\to0.
$$

<span class="original-page-anchor" id="pdf-page-806" aria-hidden="true"></span>

从而得到相应的同调序列

$$
H^{n-1}F(Y)\to H^nF(X)\to H^nF(I)\to H^nF(Y).
$$

由引理 6.3，两端都为 $0$，所以得到中间的同构；根据定义，这就是同构

$$
H^nF(X)\approx R^nF(M),
$$

定理因而得证。

### 左导出函子

以左导出函子的性质的概述结束本节。

考察箭头朝另一个方向的复形

$$
\to X_n\to\cdots\to X_2\to X_1\to X_0\to M\to0,
$$

将其简记为

$$
X_M\to M\to0.
$$

如果此序列正合，就称这个复形为 $M$ 的一个**解消**。如果 $X_n$ 对于所有 $n\geqq0$ 都是投射对象，就称它为**投射解消**。

*给定投射解消 $X_M,Y_{M'}$ 和同态*

$$
\varphi:M\to M',
$$

*总存在一个延拓 $\varphi$ 的同态 $X_M\to Y_{M'}$，而且任意两个这样的同态都同伦。*

事实上，为使证明成立，只需假定 $X_M$ 是投射解消，而 $Y_{M'}$ 是一个解消，不必是投射解消。

设 $T$ 是协变加性函子。固定对象 $M$ 的一个投射解消

$$
P_M\to M\to0.
$$

定义**左导出函子** $L_nT$ 为

$$
L_nT(M)=H_n(T(P)),
$$

其中 $T(P)$ 是复形

$$
\to T(P_n)\to\cdots\to T(P_2)\to T(P_1)\to T(P_0)\to0.
$$

同伦的存在表明，改变投射解消时，$L_nT(M)$ 在唯一同构的意义下唯一确定。

如果正合列

$$
M'\to M\to M''\to0
$$

<span class="original-page-anchor" id="pdf-page-807" aria-hidden="true"></span>

产生正合列

$$
T(M')\to T(M)\to T(M'')\to0,
$$

就称 $T$ 为右正合的。

*如果 $T$ 右正合，那么由定义立即得到*

$$
L_0T(M)\approx T(M).
$$

> **译校注：** 原文印为 $L_0T(M)\approx M$，应为 $L_0T(M)\approx T(M)$。根据上一页定义，$L_0T(M)$ 是 $T(P_1)\to T(P_0)$ 的余核；$T$ 的右正合性把这个余核识别为 $T(M)$，并非一般的 $M$。

定理 6.1 和 6.2 随后适用于这种情形，证明也类似。必须处处把“内射对象”换成“投射对象”，而在定理 6.1 中，最后一个条件表述为：当 $n>0$ 时，

$$
L_nT(P)=0\quad\text{如果 }P\text{ 是投射对象}.
$$

其余只需把证明中的某些箭头反向。关于这类左导出函子的一个例子，参见有关群的上同调的习题 2–7。

## §7. δ-函子

本节遵循 Grothendieck，把定理 6.1 所述的性质公理化。

设 $\mathfrak{A},\mathfrak{B}$ 是阿贝尔范畴。从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的一个（协变）**$\delta$-函子**，是一个加性函子族 $F=\{F_n\}_{n\geqq0}$，以及对于每个短正合列

$$
0\to M'\to M\to M''\to0
$$

所对应的一个态射族

$$
\delta^n:F^n(M'')\to F^{n+1}(M'),
$$

其中 $n\geqq0$，并满足以下条件：

**DEL 1.** 对于每个上述短正合列，都有长正合列

$$
\begin{aligned}
0\to F^0(M')\to F^0(M)\to F^0(M'')\to F^1(M')\to\cdots\\
\to F^n(M')\to F^n(M)\to F^n(M'')\to F^{n+1}(M')\to
\end{aligned}
$$

**DEL 2.** 对于从上述一个短正合列到另一个短正合列 $0\to N'\to N\to N''\to0$ 的每个态射，$\delta$ 给出交换图：

$$
\begin{array}{ccc}
F^n(M'')&\xrightarrow{\delta}&F^{n+1}(M')\\
\downarrow&&\downarrow\\
F^n(N'')&\xrightarrow{\delta}&F^{n+1}(N').
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-808" aria-hidden="true"></span>

在继续讨论之前，先给出另一个定义是有用的。同调论中的许多证明是从一个指标归纳到下一个指标。结果表明，为使指标增加一，所需的有关数据只涉及连续的两个维数，而其他指标无关。因此如下推广 $\delta$-函子的概念。

一个**定义在次数 $0,1$ 的 $\delta$-函子**，是一个函子对 $(F^0,F^1)$，以及对于每个短正合列

$$
0\to A'\to A\to A''\to0
$$

所对应的一个态射

$$
\delta:F^0(A'')\to F^1(A'),
$$

> **译校注：** 原文此处的目标印为 $F^1(A'')$，应为 $F^1(A')$。上一页的定义给出 $\delta^n:F^n(M'')\to F^{n+1}(M')$；取 $n=0$ 并将正合列写成这里的 $A',A,A''$，目标正是 $F^1(A')$。

满足与以前相同的两个条件，但取 $n=0$、$n+1=1$，而不考虑其他整数 $n$。也可以用任意两个连续的正整数为 $\delta$-函子编号，或用任意一列连续的非负整数。在实际中，只出现使用所有非负整数的情形；但在证明中，只用两个指标，例如 $0,1$，所提供的灵活性是有用的。

如果给定从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的任意其他 $\delta$-函子 $G$，以及任意函子态射

$$
f_0:F^0\to G^0,
$$

对于所有 $n\geqq0$，都存在唯一的态射序列

$$
f_n:F^n\to G^n,
$$

使它们对每个短正合列都与 $\delta^n$ 可交换，就称 $\delta$-函子 $F$ 为**泛的**。

根据泛性的定义，满足 $G^0=F^0$ 的 $\delta$-函子 $G$ 在唯一的函子同构意义下唯一确定。下面给出使函子为泛函子的一个条件。

> **译校注：** 这里的唯一性应在泛 $\delta$-函子之中理解，即 $G$ 也须是泛的。泛性只保证从 $F$ 到任意 $G$ 的唯一延拓态射，若 $G$ 也泛，才可反向构造态射并由唯一性得到互逆。若不作此限制，在向量空间范畴中取 $F^0=\operatorname{id}$、$F^{n>0}=0$，以及 $G^0=G^1=\operatorname{id}$、$G^{n>1}=0$，连接态射都为零；短正合列均分裂，故两者都是 $\delta$-函子，$F$ 泛，但两者并不同构。

从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的加性函子 $F$ 称为**可消去的**，如果对每个对象 $A$，都存在到某个 $M$ 的单态 $u:A\to M$，使得 $F(u)=0$。实际上，甚至会有 $F(M)=0$，但在公理化中并不需要这一点。

**语言说明。** Grothendieck 最初在法语中把这个概念称为“effaceable”。它在词典中的英语译词是“erasable”，正如我在上面所用的词。看来有些不懂法语的人在英语中用了这个法语词，但没有必要这样做，因为这个英语词同样有意义，而且使用方便。

如果此外可以取 $M$ 为内射对象，就称这个函子**可由内射对象消去**。

<span class="original-page-anchor" id="pdf-page-809" aria-hidden="true"></span>

**例。** 当然，右导出函子可由内射对象消去，左导出函子可由投射对象消去。不过，在许多情形中需要用其他类型的对象来消去。在讨论群的上同调的习题 9 和 14 中，你将看到如何用诱导模，或在 $G$ 有限时用正则模，来消去上同调函子。在代数几何的凝聚层范畴中，用有限秩的局部自由层来消去上同调。

**定理 7.1。** *设 $F=\{F^n\}$ 是从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的协变 $\delta$-函子。如果 $F^n$ 对每个 $n>0$ 都可消去，那么 $F$ 是泛的。*

*证明。* 给定对象 $A$，用单态 $u$ 消去它，得到短正合列

$$
0\to A\xrightarrow{\varphi}M\to X\to0.
$$

设 $G$ 是另一个 $\delta$-函子，并给定 $f_0:F^0\to G^0$。有如下正合交换图：

![构造 f1 的正合图](/library/volume-86/diagrams/pdf-0809-universality-construction.png)

右上方的 $0$ 来自可消去性的假设

$$
F^1(\varphi)=0.
$$

要构造

$$
f_1(A):F^1(A)\to G^1(A),
$$

使图交换，关于 $A$ 具有函子性，并且与 $\delta$ 可交换。左边方块的交换性表明 $\operatorname{Ker}\delta_F$ 包含于 $\delta_G\circ f_0$ 的核。因此存在唯一的同态

$$
f_1(A):F^1(A)\to G^1(A),
$$

使右边方块交换。下面证明 $f_1(A)$ 满足所需条件。其余证明随后遵循同样的方式作归纳。

首先证明关于 $A$ 的函子性。

设 $u:A\to B$ 是一个态射。在如下图中构造推出 $P$：

$$
\begin{array}{ccc}
A&\xrightarrow{\varphi}&M\\
{\scriptstyle u}\downarrow&&\downarrow\\
B&\longrightarrow&P
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-810" aria-hidden="true"></span>

由于 $\varphi$ 是单态，$B\to P$ 也是单态。再取一个消去 $F_1$ 的单态 $P\to N$。这给出交换图

$$
\begin{array}{ccccccccc}
0&\longrightarrow&A&\longrightarrow&M&\longrightarrow&X&\longrightarrow&0\\
&&{\scriptstyle u}\downarrow&&{\scriptstyle v}\downarrow&&{\scriptstyle w}\downarrow&&\\
0&\longrightarrow&B&\longrightarrow&N&\longrightarrow&Y&\longrightarrow&0
\end{array}
$$

其中 $B\to N$ 是复合 $B\to P\to N$，而 $Y$ 定义为 $B\to N$ 的余核。

关于 $A$ 的函子性是指下图交换：

$$
\begin{array}{ccc}
F^1(A)&\xrightarrow{F^1(u)}&F^1(B)\\
{\scriptstyle f_1(A)}\downarrow&&\downarrow{\scriptstyle f_1(B)}\\
G^1(A)&\xrightarrow{G^1(u)}&G^1(B)
\end{array}
$$

> **译校注：** 原图下方箭头的标签印为 $F^1(u)$，应为 $G^1(u)$，因为它从 $G^1(A)$ 映到 $G^1(B)$；紧接的立方体和下一页的等式也均在此处使用 $G^1(u)$。

这个方块是下列立方体的右侧面：

![证明函子性的立方体](/library/volume-86/diagrams/pdf-0810-functoriality-cube.png)

除右侧面可能不交换外，立方体的所有面都交换。于是一个一般事实是，如果这里记作 $\delta_F$ 的上方映射是满态，<span class="original-page-anchor" id="pdf-page-811" aria-hidden="true"></span>那么右侧面也交换。可以如下看出这一点。从 $f_1(B)F^1(u)\delta_F$ 出发，依次利用立方体的顶面、前面、左侧面、底面，最后是后面的交换性，得到

$$
f_1(B)F^1(u)\delta_F=G^1(u)f_1(A)\delta_F.
$$

由于 $\delta_F$ 是满态，可以消去 $\delta_F$，得到所需结论。

其次，必须证明 $f_1$ 与 $\delta$ 可交换。设

$$
0\to A'\to A\to A''\to0
$$

是短正合列。与以前相同的推出论证表明，存在一个用于消去的单态 $0\to A'\to M$ 和态射 $v,w$，使下图交换：

$$
\begin{array}{ccccccccc}
0&\longrightarrow&A'&\longrightarrow&A&\longrightarrow&A''&\longrightarrow&0\\
&&{\scriptstyle\operatorname{id}}\downarrow&&{\scriptstyle v}\downarrow&&{\scriptstyle w}\downarrow&&\\
0&\longrightarrow&A'&\longrightarrow&M&\longrightarrow&X&\longrightarrow&0
\end{array}
$$

这里 $X$ 定义为下行中相应的余核。现在考察下图：

![证明与 δ 相容的图](/library/volume-86/diagrams/pdf-0811-delta-compatibility-prism.png)

目的是证明右侧面交换。根据 $\delta$-函子的定义，上下两个三角形都交换。

<span class="original-page-anchor" id="pdf-page-812" aria-hidden="true"></span>

根据 $f_0$ 是函子态射的假设，左边方块交换。根据 $f_1(A')$ 的定义，前面的方块交换。因此得到：

$$
\begin{aligned}
f_1(A')\delta_F&=f_1(A')\delta_F F^0(w)&&\text{（上方三角形）}\\
&=\delta_G f_0F^0(w)&&\text{（前面方块）}\\
&=\delta_G G^0(w)f_0&&\text{（左边方块）}\\
&=\delta_G f_0&&\text{（下方三角形）}.
\end{aligned}
$$

> **译校注：** 原文从标注“front square”的第二行到最后一行，连接态射均印为 $\delta_F$，应为 $\delta_G$。上一页的前面方块给出 $f_1\delta_F=\delta_G f_0$；这些行中的连接态射作用于 $G^0$ 并取值于 $G^1$，也必须属于 $G$。

定理 7.1 的证明至此完成，因为可以用指标对 $(n,n+1)$ 代替 $(0,1)$。

**注。** 定理 7.1 中构造的态射 $f_1$ 以下述意义函子地依赖于 $f_0$。设有三个定义在次数 $0,1$ 的 δ-函子 $F,G,H$，并给定态射

$$
f_0:F^0\to G^0\quad\text{和}\quad g_0:G^0\to H^0.
$$

假定用于消去的单态同时消去 $F$ 和 $G$。那么应用该定理可以构造 $f_1$ 和 $g_1$。另一方面，复合

$$
g_0f_0=h_0:F^0\to H^0
$$

也是函子态射，而该定理给出态射

$$
h_1:F^1\to H^1
$$

的存在，使得 $(h_0,h_1)$ 是一个 $\delta$-态射。由唯一性，因此有

$$
h_1=g_1f_1.
$$

这就是上面所说的函子性依赖的含义。

**推论 7.2。** *假定 $\mathfrak{A}$ 有足够多的内射对象。那么对于任意左正合函子 $F:\mathfrak{A}\to\mathfrak{B}$，导出函子 $R^nF$，$n\geqq0$，构成一个泛 $\delta$-函子，且 $F\approx R^0F$，并且可由内射对象消去。反之，如果 $G=\{G^n\}_{n\geqq0}$ 是泛 $\delta$-函子，那么 $G^0$ 左正合，而且对每个 $n\geqq0$，$G^n$ 都同构于 $R^nG^0$。*

> **译校注：** 此处“可由内射对象消去”指正次数 $R^nF$（$n>0$），正如下方证明中的范围；不包括 $R^0F\approx F$。例如恒等函子不会把非零对象的单态变成零态射。

*证明。* 如果 $F$ 是左正合函子，那么由定理 6.1，$\{R^nF\}_{n\geqq0}$ 构成一个 $\delta$-函子。此外，对任意对象 $A$，取 $A$ 到一个内射对象的单态 $u:A\to I$。由定理 6.1(iv)，当 $n>0$ 时 $R^nF(I)=0$，所以 $R^nF(u)=0$。因此 $R^nF$ 对所有 $n>0$ 都可消去，可以应用定理 7.1。

**注。** 与通常一样，定理 7.1 适用于变性不同的函子。设 $\{F^n\}$ 是一个反变加性函子族，其中 $n$ 遍历<span class="original-page-anchor" id="pdf-page-813" aria-hidden="true"></span>一列连续的整数；为简单起见，取 $n\geqq0$。如果给定正合列

$$
0\to M'\to M\to M''\to0,
$$

就有相应的态射族

$$
\delta^n:F^n(M')\to F^{n+1}(M''),
$$

满足将 $M'$ 与 $M''$ 互换、$N'$ 与 $N''$ 互换后的 **DEL 1** 和 **DEL 2**，就称 $F$ 为**反变 $\delta$-函子**。

> **译校注：** 原文上述态射的目标印为 $F^{n+1}(M')$，应为 $F^{n+1}(M'')$。将协变定义中的 $M'$ 与 $M''$ 互换，恰好得到这里的目标；本页下方的维数移位正合列也使用这一形式。

如果对每个对象 $A$，都存在满态 $u:M\to A$，使 $F(u)=0$，就称 $F$ 为**余可消去的**。如果给定从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的任意其他 $\delta$-函子 $G$，以及函子态射

$$
f_0:F^0\to G^0,
$$

对所有 $n\geqq0$ 都存在唯一的态射序列

$$
f_n:F^n\to G^n,
$$

使其对于每个短正合列都与 $\delta$ 可交换，就称 $F$ 为**泛的**。

**定理 7.1′。** *设 $F=\{F^n\}$（$n$ 遍历一列连续的非负整数）是从 $\mathfrak{A}$ 到 $\mathfrak{B}$ 的反变 $\delta$-函子，并假定 $F^n$ 对 $n\geqq1$ 都余可消去。那么 $F$ 是泛的。*

下一节将结合双函子，给出具有定理 7.1 和 7.1′ 中的变性的 $\delta$-函子的例子。

### 维数移位

设 $F=\{F^n\}$ 是一个反变 δ-函子，$n\geqq0$。设 $\mathcal{E}$ 是一个对象族，对所有 $n\geqq1$ 都消去 $F^n$；也就是说，对于 $n\geqq1$ 和 $E\in\mathcal{E}$，都有 $F^n(E)=0$。这样的对象族允许进行下述所谓的**维数移位**。给定正合列

$$
0\to Q\to E\to M\to0,
$$

其中 $E\in\mathcal{E}$，对于 $n\geqq1$ 得到正合列

$$
0=F^n(E)\to F^n(Q)\to F^{n+1}(M)\to F^{n+1}(E)=0,
$$

因此得到同构

$$
F^n(Q)\xrightarrow{\approx}F^{n+1}(M),
$$

它表明维数移位了一。更一般地：

**命题 7.3。** *设*

$$
0\to Q\to E_{n-1}\to\cdots\to E_0\to M\to0
$$

<span class="original-page-anchor" id="pdf-page-814" aria-hidden="true"></span>

*是正合列，且 $E_i\in\mathcal{E}$。那么对于 $p\geqq1$ 有同构*

$$
F^p(Q)\approx F^{p+n}(M).
$$

*证明。* 令 $Q=Q_n$。此外，不失一般性，取 $p=1$。可以在每一步插入核与余核，如下：

![在解消中插入核与余核](/library/volume-86/diagrams/pdf-0814-dimension-shifting-zigzag.png)

然后对每个短正合列作维数移位，得到同构

$$
F^1(Q_n)\approx F^2(Q_{n-1})\approx\cdots\approx F^{n+1}(M).
$$

证明至此完成。

如果 $F^n(M)=0$ 对于 $n\geqq d+1$ 都成立，就称 $M$ 的 **$F$-维数** $\leqq d$。由维数移位可见，如果 $M$ 的 $F$-维数 $\leqq d$，那么命题 7.3 中 $Q$ 的 $F$-维数 $\leqq d-n$。特别地，如果 $M$ 的 $F$-维数为 $n$，那么 $Q$ 的 $F$-维数为 $0$。

> **译校注：** 原文界“$Q$ 的 $F$-维数 $\leqq d-n$”在 $d\geqq n$ 时有效；若 $d<n$，前面的移位同构只涉及 $p\geqq1$，故只能推出 $Q$ 的正次数函子值为零，即 $F$-维数 $\leqq0$，不能推出零次值也为零。例如在向量空间范畴取 $F^q=\operatorname{Ext}^q(-,k)$ 和正合列 $0\to k\to k^2\to k\to0$，此时 $d=0$、$n=1$，但 $F^0(Q)=\operatorname{Hom}(k,k)\ne0$，所以 $Q$ 的维数不满足 $\leqq-1$。

读者应改变记号，重写这一整套形式体系：在一个环上的模范畴中，用从 Hom 的第一个变量产生的标准函子作为 $F$。该范畴有足够多的投射对象，来消去固定 $B$ 时函子

$$
A\mapsto\operatorname{Hom}(A,B)
$$

的左导出函子。下一节将对这种情形作适当的公理化研究。

## §8. 双函子

在阿贝尔范畴中经常要处理 Hom，它可以看成两个变量的函子；还要处理张量积，它也是两个变量的函子，但它们的变性不同。无论如何，这些例子导向**双函子**的概念。这是一个对应

$$
(A,B)\mapsto T(A,B),
$$

<span class="original-page-anchor" id="pdf-page-815" aria-hidden="true"></span>

其中 $A,B$ 分别是阿贝尔范畴 $\mathfrak{A}$ 和 $\mathfrak{B}$ 中的对象，而取值属于某个阿贝尔范畴。这是说，$T$ 关于每个变量都具有函子性，并有相应的变性（协变与反变的所有可能组合共有四种）；而且例如当 $T$ 关于所有变量都协变时，还要求对于同态 $A'\to A$ 和 $B'\to B$，有交换图

$$
\begin{array}{ccc}
T(A',B')&\longrightarrow&T(A',B)\\
\downarrow&&\downarrow\\
T(A,B')&\longrightarrow&T(A,B).
\end{array}
$$

如果改变变性，就须以相应方式把图中的箭头反向。最后，要求 $T$ 作为每个变量的函子都是加性的。

注意，Hom 是双函子，关于第一个变量反变，关于第二个变量协变。张量积关于每个变量都协变。

Hom 函子是满足下列性质的双函子 $T$：

**HOM 1.** *$T$ 关于第一个变量反变且左正合。*

**HOM 2.** *$T$ 关于第二个变量协变且左正合。*

**HOM 3.** *对于任意内射对象 $J$，函子*

$$
A\mapsto T(A,J)
$$

*正合。*

本节只考虑这些性质。还有一个可能在其他时候用到的第四条性质：

**HOM 4.** *对于任意投射对象 $Q$，函子*

$$
B\mapsto T(Q,B)
$$

*正合。*

不过，下面将*采用不对称的处理，把 $T$ 看成第二个变量的函子，固定第一个变量，以得到关于第二个变量的导出函子。* 另一方面，利用双函子也将得到关于第一个变量的一个 $\delta$-函子，虽然这个 $\delta$-函子并不是导出函子。

如果 $\mathfrak{B}$ 有足够多的内射对象，那么可以构造关于第二个变量的右导出函子

$$
B\mapsto R^nT(A,B),\quad\text{也记作 }R^nT_A(B),
$$

<span class="original-page-anchor" id="pdf-page-816" aria-hidden="true"></span>

固定 $A$，把 $B$ 看成变量。如果 $T=\operatorname{Hom}$，那么这个右导出函子称为 **Ext**，所以根据定义有

$$
\operatorname{Ext}^n(A,X)=R^n\operatorname{Hom}(A,X).
$$

现在给出一个判据，以另一个（第一个）变量来计算右导出函子。如果函子 $B\mapsto T(A,B)$ 正合，就称对象 $A$ 为 **$T$-正合的**。对象 $A$ 的一个 **$T$-正合解消**，是指一个解消

$$
\to M_1\to M_0\to A\to0,
$$

其中 $M_n$ 对所有 $n\geqq0$ 都是 $T$-正合的。

**例。** 设 $\mathfrak{A}$ 和 $\mathfrak{B}$ 是交换环上的模范畴，$T=\operatorname{Hom}$。那么根据定义，$T$-正合对象就是投射模。现在把 $T$ 的**转置**定义为

$$
{}^tT(A,B)=T(B,A).
$$

那么根据定义，${}^tT$-正合对象就是内射模。

如果 $T$ 是张量积，即 $T(A,B)=A\otimes B$，那么 $T$-正合对象称为**平坦的**。

**注。** 在一个环上的模范畴中，有足够多的投射对象和内射对象。但也有并非如此的其他情形。想看到这些“抽象废话”如何实际运用的读者，可以查阅 [GriH 78]、[Ha 77]，更不用说 [SGA 6] 和 Grothendieck 的文集。在实际中，确实可能出现 $\mathfrak{B}$ 有足够多的内射对象，而 $\mathfrak{A}$ 没有足够多的投射对象的情况，所以这种情形并非完全对称。因此，固定 $B$ 时，函子 $A\mapsto R^nT(A,B)$ *不是*变量 $A$ 的导出函子。在上述参考文献中，可以取 $\mathfrak{A}$ 为一个簇上的凝聚层范畴，而取 $\mathfrak{B}$ 为所有层的范畴。令 $T=\operatorname{Hom}$。有限秩的局部自由层是 $T$-正合的，而且在 $\mathfrak{A}$ 中有足够多的这种层。$\mathfrak{B}$ 中有足够多的内射对象。情形就是这样。一边是 $T$-正合对象，另一边是内射对象；两者之间的平衡是这种情形固有的。

**引理 8.1。** *设 $T$ 是满足 **HOM 1**、**HOM 2** 的双函子。设 $A\in\mathfrak{A}$，且 $M_A\to A\to0$，即*

$$
\to M_1\to M_0\to A\to0,
$$

*是 $A$ 的一个 $T$-正合解消。对于 $B\in\mathfrak{B}$，令 $F^n(B)=H^n(T(M,B))$。那么 $F$ 是一个 $\delta$-函子，而且 $F^0(B)=T(A,B)$。如果此外 $T$ 满足 **HOM 3**，那么对于内射对象 $J$ 和 $n\geqq1$，有 $F^n(J)=0$。*

<span class="original-page-anchor" id="pdf-page-817" aria-hidden="true"></span>

*证明。* 给定正合列

$$
0\to B'\to B\to B''\to0,
$$

得到复形的正合列

$$
0\to T(M,B')\to T(M,B)\to T(M,B'')\to0,
$$

从而得到上同调序列，使 $F$ 成为一个 $\delta$-函子。当 $n=0$ 时得到 $F^0(B)=T(A,B)$，因为对于 $X\in\mathfrak{A}$，$X\mapsto T(X,B)$ 反变且左正合。如果 $B$ 内射，那么由 **HOM 3**，$F^n(B)=0$ 对于 $n\geqq1$ 成立，因为 $X\mapsto T(X,B)$ 正合。引理得证。

**命题 8.2。** *设 $T$ 是满足 **HOM 1**、**HOM 2**、**HOM 3** 的双函子。假定 $\mathfrak{B}$ 有足够多的内射对象。设 $A\in\mathfrak{A}$，且*

$$
M_A\to A\to0
$$

*是 $A$ 的一个 $T$-正合解消。那么两个 $\delta$-函子*

$$
B\mapsto R^nT(A,B)\quad\text{和}\quad B\mapsto H^n(T(M,B))
$$

*作为在内射对象上于 $n\geqq1$ 时取零值的泛 $\delta$-函子，是同构的，并满足*

$$
R^0T(A,B)=H^0(T(M,B))=T(A,B).
$$

> **译校注：** 原文中间项印为 $H^0(T(M),B)$，括号位置应为 $H^0(T(M,B))$；本命题刚定义的复形是 $T(M,B)$，上一页引理 8.1 也正以 $H^n(T(M,B))$ 定义 $F^n(B)$。

*证明。* 这仅仅来自可由内射对象消去的 $\delta$-函子的泛性。

现在考察关于 $A$ 的函子性。

**引理 8.3。** *设 $T$ 满足 **HOM 1**、**HOM 2** 和 **HOM 3**。假定 $\mathfrak{B}$ 有足够多的内射对象。设*

$$
0\to A'\to A\to A''\to0
$$

*是短正合列。那么对于固定的 $B$，有长正合列*

$$
\begin{aligned}
0\to T(A'',B)\to T(A,B)\to T(A',B)\to\\
\to R^1T(A'',B)\to R^1T(A,B)\to R^1T(A',B)\to
\end{aligned}
$$

*使得对应*

$$
A\mapsto R^nT(A,B)
$$

*是一个 $\delta$-函子。*

<span class="original-page-anchor" id="pdf-page-818" aria-hidden="true"></span>

*证明。* 设 $0\to B\to I_B$ 是 $B$ 的一个内射解消。由函子 $A\mapsto T(A,J)$ 在 $J$ 内射时的正合性，得到复形的短正合列

$$
0\to T(A'',I_B)\to T(A,I_B)\to T(A',I_B)\to0.
$$

取这些复形的同调群的相应长正合列，就得到命题中的序列。（函子性的证明留给读者。）

如果 $T=\operatorname{Hom}$，那么正合列具有如下形式：

$$
\begin{aligned}
0\to\operatorname{Hom}(A'',B)\to\operatorname{Hom}(A,B)\to\operatorname{Hom}(A',B)\to\\
\to\operatorname{Ext}^1(A'',B)\to\operatorname{Ext}^1(A,B)\to\operatorname{Ext}^1(A',B)\to
\end{aligned}
$$

依此继续。

如果给定 $\mathfrak{A}$ 中的对象 $A$，存在一个 $T$-正合对象 $M$ 和满态

$$
M\to A\to0,
$$

就说 $\mathfrak{A}$ 有**足够多的 $T$-正合对象**。

**命题 8.4。** *设 $T$ 满足 **HOM 1**、**HOM 2**、**HOM 3**。假定 $\mathfrak{B}$ 有足够多的内射对象。固定 $B\in\mathfrak{B}$。那么对应*

$$
A\mapsto R^nT(A,B)
$$

*是 $\mathfrak{A}$ 上的一个反变 $\delta$-函子，当 $n\geqq1$ 时在 $T$-正合对象上取零值。如果 $\mathfrak{A}$ 有足够多的 $T$-正合对象，那么这个函子是泛的，可由 $T$-正合对象余消去，并且其零次值为*

$$
R^0T(A,B)=T(A,B).
$$

*证明。* 由引理 8.3 知道这个对应是一个 $\delta$-函子，而由引理 8.1，它在 $T$-正合对象上取零值。最后一个断言仅仅是可消去的 $\delta$-函子的泛性的应用。

**推论 8.5。** *设 $\mathfrak{A}=\mathfrak{B}$ 是一个环上的模范畴。对于固定的 $B$，以 $\operatorname{ext}^n(A,B)$ 表示通过 $A$ 的投射解消得到的函子 $A\mapsto\operatorname{Hom}(A,B)$ 的左导出函子。那么*

$$
\operatorname{ext}^n(A,B)=\operatorname{Ext}^n(A,B).
$$

*证明。* 由命题 8.4 立即得到。

下面的命题从上同调的角度刻画 $T$-正合对象。

<span class="original-page-anchor" id="pdf-page-819" aria-hidden="true"></span>

**命题 8.6。** *设 $T$ 是满足 **HOM 1**、**HOM 2**、**HOM 3** 的双函子。假定 $\mathfrak{B}$ 有足够多的内射对象。那么下列条件等价：*

**TE 1.** *$A$ 是 $T$-正合的。*

**TE 2.** *对于每个 $B$ 和每个整数 $n\geqq1$，有 $R^nT(A,B)=0$。*

**TE 3.** *对于每个 $B$，有 $R^1T(A,B)=0$。*

*证明。* 设

$$
0\to B\to I^0\to I^1\to
$$

是 $B$ 的一个内射解消。根据定义，$R^nT(A,B)$ 是序列

$$
0\to T(A,I^0)\to T(A,I^1)\to T(A,I^2)\to
$$

的第 $n$ 个同调。

如果 $A$ 是 $T$-正合的，那么此序列对于 $n\geqq1$ 正合，所以同调为 $0$，从而 **TE 1** 蕴涵 **TE 2**。显然，**TE 2** 蕴涵 **TE 3**。最后假定 **TE 3**。给定正合列

$$
0\to B'\to B\to B''\to0,
$$

有同调序列

$$
0\to T(A,B')\to T(A,B)\to T(A,B'')\to R^1T(A,B')\to.
$$

如果 $R^1T(A,B')=0$，那么根据定义 $A$ 是 $T$-正合的，命题因而得证。

如果

$$
R^nT(A,B)=0\quad\text{对于 }n>d\text{ 和所有 }B,
$$

就说对象 $A$ 的 **$T$-维数** $\leqq d$。

于是该命题特别说明：*$A$ 是 $T$-正合的当且仅当 $A$ 的 $T$-维数为 $0$。*

**命题 8.7。** *设 $T$ 满足 **HOM 1**、**HOM 2**、**HOM 3**。假定 $\mathfrak{B}$ 有足够多的内射对象。假定对象 $A$ 有一个解消*

$$
0\to E_d\to E_{d-1}\to\cdots\to E_0\to A\to0,
$$

*其中 $E_0,\ldots,E_d$ 都是 $T$-正合的。那么 $A$ 的 $T$-维数 $\leqq d$。假定情况如此。设*

$$
0\to Q\to L_{d-1}\to\cdots\to L_0\to A\to0
$$

*是一个解消，其中 $L_0,\ldots,L_{d-1}$ 都是 $T$-正合的。那么 $Q$ 也是 $T$-正合的。*

*证明。* 由维数移位得出 $Q$ 的 $T$-维数为 $0$，所以由命题 8.6，$Q$ 是 $T$-正合的。

<span class="original-page-anchor" id="pdf-page-820" aria-hidden="true"></span>

与其他命题一样，命题 8.7 用于一个环上的模的情形。此时可以取 $T=\operatorname{Hom}$，且

$$
R^nT(A,B)=\operatorname{Ext}^n(A,B).
$$

$A$ 的 $T$-维数 $\leqq d$ 的含义是

$$
\operatorname{Ext}^n(A,B)=0\quad\text{对于 }n>d\text{ 和所有 }B.
$$

于是命题中的 $T$-正合可以理解为投射。

下面对一个适用于张量积的双函子表述类似的结果。考察下列性质。

**TEN 1.** *$T$ 关于第一个变量协变且右正合。*

**TEN 2.** *$T$ 关于第二个变量协变且右正合。*

**TEN 3.** *对于任意投射对象 $P$，函子*

$$
A\mapsto T(A,P)
$$

*正合。*

与 Hom 的情形一样，还有一条可能的第四性质，但在本节中不起作用：

**TEN 4.** *对于任意投射对象 $Q$，函子*

$$
B\mapsto T(Q,B)
$$

*正合。*

**命题 8.2′。** *设 $T$ 是满足 **TEN 1**、**TEN 2**、**TEN 3** 的双函子。假定 $\mathfrak{B}$ 有足够多的投射对象。设 $A\in\mathfrak{A}$，且*

$$
M_A\to A\to0
$$

*是 $A$ 的一个 $T$-正合解消。那么两个 $\delta$-函子*

$$
B\mapsto L_nT(A,B)\quad\text{和}\quad B\mapsto H_n(T(M,B))
$$

*作为在投射对象上取零值的泛 $\delta$-函子，是同构的，并且满足*

$$
L_0T(A,B)=H_0(T(M,B))=T(A,B).
$$

> **译校注：** 原文中间项印为 $H_0(T(M),B)$，应为 $H_0(T(M,B))$；本命题上方已给出复形 $T(M,B)$。这里在投射对象上取零值的范围是正次数 $n\geqq1$，零次值则如等式所示为 $T(A,B)$。

**引理 8.3′。** *假定 $T$ 满足 **TEN 1**、**TEN 2**、**TEN 3**。假定 $\mathfrak{B}$ 有足够多的投射对象。设*

$$
0\to A'\to A\to A''\to0
$$

<span class="original-page-anchor" id="pdf-page-821" aria-hidden="true"></span>

*是一个短正合列。那么对于固定的 $B$，有长正合列：*

$$
\begin{aligned}
\to L_1T(A',B)\to L_1T(A,B)\to L_1T(A'',B)\to\\
\to T(A',B)\to T(A,B)\to T(A'',B)\to0,
\end{aligned}
$$

*使对应 $A\mapsto L_nT(A,B)$ 成为一个 $\delta$-函子。*

**命题 8.4′。** *设 $T$ 满足 **TEN 1**、**TEN 2**、**TEN 3**。假定 $\mathfrak{B}$ 有足够多的投射对象。固定 $B\in\mathfrak{B}$。那么对应*

$$
A\mapsto L_nT(A,B)
$$

*是 $\mathfrak{A}$ 上的一个协变 $\delta$-函子，对于 $n\geqq1$ 在 $T$-正合对象上取零值。如果 $\mathfrak{A}$ 有足够多的 $T$-正合对象，那么这个函子是泛的，可由 $T$-正合对象余消去，并且零次值为*

$$
L_0T(A,B)=T(A,B).
$$

> **译校注：** 原文称此函子为“contravariant”，即反变，应为协变。**TEN 1** 规定 $T$ 关于第一个变量协变；上一引理的长正合列也把 $A'\to A\to A''$ 对应到同方向的映射 $L_nT(A',B)\to L_nT(A,B)\to L_nT(A'',B)$。

**推论 8.8。** *如果存在双函子同构 $T(A,B)\approx T(B,A)$，且 $B$ 是 $T$-正合的，那么对于所有 $A$，当 $n\geqq1$ 时有 $L_nT(A,B)=0$。简言之，$T$-正合蕴涵无环。*

*证明。* 在命题 8.2′ 中取 $M_A=P_A$ 为投射解消。根据假设，$X\mapsto T(X,B)$ 正合，所以对于 $n\geqq1$ 有 $H_n(T(P,B))=0$；因此这个推论是该命题的结果。

上述推论是为适用于张量积而表述的。

**命题 8.6′。** *设 $T$ 是满足 **TEN 1**、**TEN 2**、**TEN 3** 的双函子。假定 $\mathfrak{B}$ 有足够多的投射对象。那么下列条件等价：*

**TE 1.** *$A$ 是 $T$-正合的。*

**TE 2.** *对于每个 $B$ 和每个整数 $n\geqq1$，有 $L_nT(A,B)=0$。*

**TE 3.** *对于每个 $B$，有 $L_1T(A,B)=0$。*

*证明。* 重复 8.6 的证明，使读者能看到箭头指向不同的方向。

设

$$
\to Q_1\to Q_0\to B\to0
$$

是 $B$ 的一个投射解消。根据定义，$L_nT(A,B)$ 是序列

$$
\to T(A,Q_1)\to T(A,Q_0)\to0
$$

的第 $n$ 个同调。

<span class="original-page-anchor" id="pdf-page-822" aria-hidden="true"></span>

如果 $A$ 是 $T$-正合的，那么此序列对于 $n\geqq1$ 正合，所以同调为 $0$，从而 **TE 1** 蕴涵 **TE 2**。显然，**TE 2** 蕴涵 **TE 3**。最后假定 **TE 3**。给定正合列

$$
0\to B'\to B\to B''\to0,
$$

有同调序列

$$
\to L_1T(A,B'')\to T(A,B')\to T(A,B)\to T(A,B'')\to0.
$$

如果 $L_1T(A,B'')$ 为 $0$，那么根据定义，$A$ 是 $T$-正合的，命题因而得证。

## §9. 谱序列

本节为便于查阅而收入，并有两个目的：第一，使读者注意到一种在拓扑、微分几何和代数几何中有广泛应用的代数工具，参见 Griffiths–Harris，[GrH 78]；第二，说明在它最常出现的情形中，只需几页就能给出这种工具的基本描述。

在上述应用中，要处理一个滤过复形（将在后面定义）；复形可以看成带有一个次数为 $1$ 的微分 $d$ 的分次对象。为先简化记号，下面处理滤过对象，并从记号中省略分次指标。这个指标与谱序列的构造无关；关于此构造，我们遵循 Godement。

因此，设 $F$ 是带有一个微分（即自同态）$d$ 的对象，满足 $d^2=0$。假定 $F$ **有滤过**，即有序列

$$
F=F^0\supset F^1\supset F^2\supset\cdots\supset F^n\supset F^{n+1}=\{0\},
$$

并且 $dF^p\subset F^p$。这些数据称为一个**滤过微分对象**。（为方便起见，假定滤过经过有限步后终止于 $0$。）

定义**相伴分次对象**

$$
\operatorname{Gr}F=\bigoplus_{p\geqq0}\operatorname{Gr}^pF\quad\text{其中}\quad\operatorname{Gr}^pF=F^p/F^{p+1}.
$$

事实上，$\operatorname{Gr}F$ 是一个复形，其次数为 $0$ 的微分由 $d$ 本身诱导，并且有同调 $H(\operatorname{Gr}^pF)$。

滤过 $\{F^p\}$ 还在同调 $H(F,d)=H(F)$ 上诱导一个滤过；具体地，令

$$
H(F)^p=H(F^p)\text{ 在 }H(F)\text{ 中的像}.
$$

<span class="original-page-anchor" id="pdf-page-823" aria-hidden="true"></span>

由于 $d$ 把 $F^p$ 映到自身，$H(F^p)$ 是关于 $d$ 在 $F^p$ 上的限制所取的 $F^p$ 的同调，并且它在 $H(F)$ 中有一个自然的像，给出这个滤过。特别地，得到与滤过同调相伴的分次对象，即

$$
\operatorname{Gr}H(F)=\bigoplus\operatorname{Gr}^pH(F).
$$

一个**谱序列**是一个分次对象序列 $\{E_r,d_r\}$（$r\geqq0$），其中

$$
E_r=\bigoplus_{p\geqq0}E_r^p,
$$

连同次数为 $r$ 的同态（也称为**微分**）

$$
d_r:E_r^p\to E_r^{p+r},
$$

满足 $d_r^2=0$，且 $E_r$ 的同调是 $E_{r+1}$，即

$$
H(E_r)=E_{r+1}.
$$

实际上，通常当 $r\geqq r_0$ 时有 $E_r=E_{r+1}=\cdots$。这个极限对象称为 $E_\infty$，并称这个谱序列**收敛到** $E_\infty$。严格说来，应当给出同构而非等式；不过为简单起见，这里使用等式。

**命题 9.1。** *设 $F$ 是一个滤过微分对象。那么存在谱序列 $\{E_r\}$，满足：*

$$
E_0^p=F^p/F^{p+1};\qquad E_1^p=H(\operatorname{Gr}^pF);\qquad E_\infty^p=\operatorname{Gr}^pH(F).
$$

*证明。* 定义

$$
\boxed{\begin{aligned}
Z_r^p&=\{x\in F^p\mid dx\in F^{p+r}\}\\
E_r^p&=Z_r^p/[dZ_{r-1}^{p-(r-1)}+Z_{r-1}^{p+1}].
\end{aligned}}
$$

> **译校注：** 盒内的商式使用 $Z_{r-1}$，按 $r\geqq1$ 理解；零页另由上方的 $E_0^p=F^p/F^{p+1}$ 定义。涉及范围外的滤过指标时，采用自然的延拓约定 $F^q=F$（$q\leqq0$）和 $F^q=0$（$q\geqq n+1$），于是可能为负的 $p-(r-1)$ 等指标也有定义。

$E_r^p$ 的定义有意义，因为立即可验证 $Z_r^p$ 包含 $dZ_{r-1}^{p-(r-1)}+Z_{r-1}^{p+1}$。此外，$d$ 把 $Z_r^p$ 映到 $Z_r^{p+r}$，从而给出一个同态

$$
d_r:E_r^p\to E_r^{p+r}.
$$

现在计算同调，并证明它正是所需的对象。

首先考察闭链：元素 $x\in Z_r^p$ 在 $E_r$ 中代表一个次数为 $p$ 的闭链，当且仅当 $dx\in dZ_{r-1}^{p+1}+Z_{r-1}^{p+r+1}$；换言之，

$$
dx=dy+z,\quad\text{其中 }y\in Z_{r-1}^{p+1}\quad\text{且}\quad z\in Z_{r-1}^{p+r+1}.
$$

<span class="original-page-anchor" id="pdf-page-824" aria-hidden="true"></span>

写成 $x=y+u$，则 $du=z$。于是 $u\in F^p$ 且 $du\in F^{p+r+1}$，即 $u\in Z_{r+1}^p$。由此得到

$$
E_r\text{ 的 }p\text{-闭链}=(Z_{r+1}^p+Z_{r-1}^{p+1})/(dZ_{r-1}^{p-r+1}+Z_{r-1}^{p+1}).
$$

另一方面，$E_r$ 中的 $p$-边界由 $dZ_r^{p-r}$ 中的元素代表，而后者包含 $dZ_{r-1}^{p-r+1}$。因此

$$
E_r\text{ 的 }p\text{-边界}=(dZ_r^{p-r}+Z_{r-1}^{p+1})/(dZ_{r-1}^{p-r+1}+Z_{r-1}^{p+1}).
$$

所以

$$
\begin{aligned}
H^p(E_r)&=(Z_{r+1}^p+Z_{r-1}^{p+1})/(dZ_r^{p-r}+Z_{r-1}^{p+1})\\
&=Z_{r+1}^p/(Z_{r+1}^p\cap(dZ_r^{p-r}+Z_{r-1}^{p+1})).
\end{aligned}
$$

由于

$$
Z_{r+1}^p\supset dZ_r^{p-r}\quad\text{且}\quad Z_{r+1}^p\cap Z_{r-1}^{p+1}=Z_r^{p+1},
$$

得到

$$
H^p(E_r)=Z_{r+1}^p/(dZ_r^{p-r}+Z_r^{p+1})=E_{r+1}^p,
$$

从而证明了谱序列的性质。

**注。** 在应用中，注意到下述关系有时是有用的：

$$
dZ_{r-1}^{p-(r-1)}+Z_{r-1}^{p+1}=Z_r^p\cap(dF^{p-r+1}+F^{p+1}).
$$

验证是直接的，不过 Griffiths–Harris 在定义谱序列时使用右边的表达式，而 Godement 使用左边的表达式，正如我们上面所做的。因此谱序列也可以定义为

$$
\boxed{E_r^p=Z_r^p\quad\bmod(dF^{p-r+1}+F^{p+1}).}
$$

这里按下述意义理解：$Z\bmod S$ 表示

$$
(Z+S)/S\quad\text{或}\quad Z/(Z\cap S).
$$

由定义立即得到 $E_0^p=F^p/F^{p+1}$，而根据已经证明的一般性质，得到 $E_1^p=H(F^p/F^{p+1})$。至于 $E_\infty^p$，当 $r$ 足够大时，有 $Z_r^p=Z^p=F^p\text{ 中的闭链}$，且

$$
\boxed{E_\infty^p=Z^p/(Z^{p+1}+(dF^0\cap F^p))}
$$

<span class="original-page-anchor" id="pdf-page-825" aria-hidden="true"></span>

这与 $r$ 无关，而且恰好是 $\operatorname{Gr}^pH(F)$，即 $H(F)$ 的 $p$ 次分次分量，定理因而得证。

微分 $d_1$ 可以如下具体描述。

**命题 9.2。** *同态*

$$
d_1:E_1^p\to E_1^{p+1}
$$

*是从正合列*

$$
0\to F^{p+1}/F^{p+2}\to F^p/F^{p+2}\to F^p/F^{p+1}\to0
$$

*产生的上边缘算子，其中把每一项看成微分由 $d$ 诱导的复形。*

*证明。* 事实上，上边缘映射

$$
\delta:E_1^p=H(F^p/F^{p+1})\to H(F^{p+1}/F^{p+2})=E_1^{p+1}
$$

在一个代表闭链 $z$ 上由 $dz$ 定义，而这与定义 $d_1$ 的方式相同。

在大多数应用中，滤过微分对象本身也分次，因为它来自下列情形。设 $K$ 是复形，$K=(K^p,d)$，其中 $p\geqq0$，且 $d$ 的次数为 $1$。所谓**滤过** $FK$，也称为一个**滤过复形**，是指子复形的一个递减序列

$$
K=F^0K\supset F^1K\supset F^2K\supset\cdots\supset F^nK\supset F^{n+1}K=\{0\}.
$$

注意，复形的短正合列

$$
0\to K'\to K\to K''\to0
$$

产生滤过 $K\supset K'\supset\{0\}$，其中将 $K'$ 看成子复形。

对每个滤过复形 $FK$，相伴有复形

$$
\operatorname{Gr}FK=\operatorname{Gr}K=\bigoplus_{p\geqq0}\operatorname{Gr}^pK,
$$

其中

$$
\operatorname{Gr}^pK=F^pK/F^{p+1}K,
$$

微分则是显然的。$K$ 上的滤过 $F^pK$ 也在上同调上诱导滤过 $F^pH(K)$，由下式给出：

$$
F^pH^q(K)=F^pZ^q/F^pB^q.
$$

<span class="original-page-anchor" id="pdf-page-826" aria-hidden="true"></span>

相伴的分次同调是

$$
\operatorname{Gr}H(K)=\bigoplus_{p,q}\operatorname{Gr}^pH^q(K),
$$

其中

$$
\operatorname{Gr}^pH^q(K)=F^pH^q(K)/F^{p+1}H^q(K).
$$

一个**谱序列**是一个双分次对象序列 $\{E_r,d_r\}$（$r\geqq0$），其中

$$
E_r=\bigoplus_{p,q\geqq0}E_r^{p,q},
$$

连同同态（称为**微分**）

$$
d_r:E_r^{p,q}\to E_r^{p+r,q-r+1},\quad\text{满足}\quad d_r^2=0,
$$

而且 $E_r$ 的同调是 $E_{r+1}$，即

$$
H(E_r)=E_{r+1}.
$$

> **译校注：** 原文直和限于 $p,q\geqq0$，这是第一象限的情形。若要对上一页定义的一般滤过复形使用下方命题 9.3，还须允许 $q$ 为整数（$p\geqq0$、$p+q\geqq0$）；仅假定 $K$ 的次数非负并不足以保证 $q\geqq0$。例如取只有 $K^0=k$ 非零、微分为零，且 $F^0K=F^1K=K$、$F^2K=0$，则 $E_0^{1,-1}=k$。若另有 $F^pK^m=0$ 对所有 $p>m$ 成立，就可以限制在原文的第一象限。

通常用下图表示谱序列：

![双分次格点中的谱序列微分](/library/volume-86/diagrams/pdf-0826-spectral-differential-lattice.png)

在实际中，通常当 $r\geqq r_0$ 时有 $E_r=E_{r+1}=\cdots$。这个极限对象称为 $E_\infty$，并称谱序列收敛到 $E_\infty$。

**命题 9.3。** *设 $FK$ 是一个滤过复形。那么存在谱序列 $\{E_r\}$，满足：*

$$
\begin{aligned}
E_0^{p,q}&=F^pK^{p+q}/F^{p+1}K^{p+q};\\
E_1^{p,q}&=H^{p+q}(\operatorname{Gr}^pK);\\
E_\infty^{p,q}&=\operatorname{Gr}^p(H^{p+q}(K)).
\end{aligned}
$$

*最后一个关系通常写成*

$$
E_r\Rightarrow H(K),
$$

*并称谱序列收敛到 $H(K)$。*

<span class="original-page-anchor" id="pdf-page-827" aria-hidden="true"></span>

命题 9.3 的断言仅仅是命题 9.1 的一个特例，其中计入了额外的分次。

一个主要例子是与双复形相伴的谱序列，其中

$$
K=\bigoplus_{p,q\geqq0}K^{p,q}
$$

是双分次对象，连同微分

$$
d':K^{p,q}\to K^{p+1,q}\quad\text{和}\quad d'':K^{p,q}\to K^{p,q+1},
$$

满足

$$
d'^2=d''^2=0\quad\text{且}\quad d'd''+d''d'=0.
$$

把双复形记为 $(K,d',d'')$。相伴的单复形 $(\operatorname{Tot}(K),D)$（Tot 表示**总复形**），简记为 $K^*$，定义为

$$
K^n=\bigoplus_{p+q=n}K^{p,q}\quad\text{且}\quad D=d'+d''.
$$

在 $(K^*,D)$ 上有两个滤过，由下式给出：

$$
\begin{aligned}
{}'F^pK^n&=\bigoplus_{\substack{p'+q=n\\p'\geqq p}}K^{p',q},\\
{}''F^qK^n&=\bigoplus_{\substack{p+q'=n\\q'\geqq q}}K^{p,q'}.
\end{aligned}
$$

> **译校注：** 原文第二式的直和项印为 $K^{p,q''}$，但求和指标和限制均为 $q'$；此处应为 $K^{p,q'}$。原图放大后可确认印了两个撇号，译文按同一求和变量改为一个撇号。

有两个谱序列 $\{{}'E_r\}$ 和 $\{{}''E_r\}$，都收敛到 $H(\operatorname{Tot}(K))$。关于应用，参见 [GrH 78] 第 3 章 §5，以及例如 [FuL 85] 第 V 章。在许多情形中，直接处理双复形是使用谱序列的一个有用替代办法，而谱序列本来就是从双复形导出的。

现在推导一个最重要情形中的谱序列的存在，即与两个函子的复合相伴的 **Grothendieck 谱序列**。*假定所用的阿贝尔范畴有足够多的内射对象。*

设 $C=\bigoplus C^p$ 是复形，为简单起见，假定当 $p<0$ 时 $C^p=0$。将 $C$ 的**内射解消**定义为一个解消

$$
0\to C\to I^0\to I^1\to I^2\to\cdots,
$$

简记为

$$
0\to C\to I_C,
$$

其中每个 $I^j$ 都是复形，$I^j=\bigoplus I^{j,p}$，其微分为

$$
d^{j,p}:I^{j,p}\to I^{j,p+1}.
$$

<span class="original-page-anchor" id="pdf-page-828" aria-hidden="true"></span>

并且 $I^{j,p}$ 是内射对象。那么特别地，对于每个 $p$ 都得到 $C^p$ 的一个内射解消，即

$$
0\to C^p\to I^{0,p}\to I^{1,p}\to\cdots.
$$

令

$$
\begin{aligned}
Z^{j,p}&=\operatorname{Ker}d^{j,p}=p\text{ 次闭链},\\
B^{j,p}&=\operatorname{Im}d^{j,p-1}=p\text{ 次边界},\\
H^{j,p}&=Z^{j,p}/B^{j,p}=p\text{ 次同调}.
\end{aligned}
$$

于是得到复形

$$
\begin{aligned}
0&\to Z^p(C)\to Z^{0,p}\to Z^{1,p}\to,\\
0&\to B^p(C)\to B^{0,p}\to B^{1,p}\to,\\
0&\to H^p(C)\to H^{0,p}\to H^{1,p}\to.
\end{aligned}
$$

如果这三个复形分别是 $Z^p(C)$、$B^p(C)$ 和 $H^p(C)$ 的内射解消，就称解消 $0\to C\to I_C$ 为**完全内射的**。

**引理 9.4。** *设*

$$
0\to M'\to M\to M''\to0
$$

*是短正合列。设*

$$
0\to M'\to I_{M'}\quad\text{和}\quad0\to M''\to I_{M''}
$$

*分别是 $M'$ 和 $M''$ 的内射解消。那么存在 $M$ 的一个内射解消*

$$
0\to M\to I_M
$$

*以及使下图正合并交换的态射：*

$$
\begin{array}{ccccccccc}
0&\longrightarrow&I_{M'}&\longrightarrow&I_M&\longrightarrow&I_{M''}&\longrightarrow&0\\
&&\uparrow&&\uparrow&&\uparrow&&\\
0&\longrightarrow&M'&\longrightarrow&M&\longrightarrow&M''&\longrightarrow&0\\
&&\uparrow&&\uparrow&&\uparrow&&\\
&&0&&0&&0&&
\end{array}
$$

*证明。* 证明与定理 6.1 的证明开头相同。

<span class="original-page-anchor" id="pdf-page-829" aria-hidden="true"></span>

**引理 9.5。** *给定复形 $C$，存在 $C$ 的一个完全内射解消。*

*证明。* 在 $C$ 中插入核与余核，得到带有边界 $B^p$ 和闭链 $Z^p$ 的短正合列：

$$
\begin{aligned}
0&\to B^p\to Z^p\to H^p\to0,\\
0&\to Z^{p-1}\to C^{p-1}\to B^p\to0.
\end{aligned}
$$

作归纳。利用引理 9.4，从

$$
0\to Z^{p-1}\to C^{p-1}\to B^p\to0
$$

的一个内射解消开始。再设

$$
0\to H^p\to I_{H^p}
$$

是 $H^p$ 的一个内射解消。由引理 9.4，存在内射解消

$$
0\to Z^p\to I_{Z^p},
$$

它嵌在已经得到的 $B^p$ 和 $H^p$ 的内射解消之间。这就完成了归纳步骤，并结束证明。

给定有足够多的内射对象的阿贝尔范畴上的一个左正合函子 $G$，如果对于 $p\geqq1$ 有 $R^pG(X)=0$，就称对象 $X$ 为 **$G$-无环的**。当然，

$$
R^0G(X)=G(X).
$$

**定理 9.6（Grothendieck 谱序列）。** *设*

$$
T:\mathfrak{A}\to\mathfrak{B}\quad\text{和}\quad G:\mathfrak{B}\to\mathfrak{C}
$$

*是协变左正合函子，且如果 $I$ 在 $\mathfrak{A}$ 中内射，那么 $T(I)$ 是 $G$-无环的。于是对于 $\mathfrak{A}$ 中每个 $A$，都有一个谱序列 $\{E_r(A)\}$，满足*

$$
E_2^{p,q}(A)=R^pG(R^qT(A)),
$$

*而 $E_r^{p,q}$（关于 $p$）收敛到 $R^{p+q}(GT)(A)$，其中 $q$ 是分次指标。*

*证明。* 设 $A$ 是 $\mathfrak{A}$ 中的对象，$0\to A\to C_A$ 是内射解消。施行 $T$，得到复形

$$
TC:\quad0\to TC^0\to TC^1\to TC^2\to.
$$

由引理 9.5，存在完全内射解消

$$
0\to TC\to I_{TC},
$$

它有如下二维表示：

<span class="original-page-anchor" id="pdf-page-830" aria-hidden="true"></span>

![TC 的完全内射解消的二维图](/library/volume-86/diagrams/pdf-0830-fully-injective-grid.png)

于是 $GI$ 是双复形。设 $\operatorname{Tot}(GI)$ 是相伴的单复形。现在依次考察两个可能的谱序列，分别记为 ${}^1E_r^{p,q}$ 和 ${}^2E_r^{p,q}$。

> **译校注：** 总复形化时采用通常的符号约定：若内射解消的两方向微分作为复形态射原先可交换，就把竖直微分在横向次数 $p$ 处乘以 $(-1)^p$，使两方向反交换，即 $d'd''+d''d'=0$，从而可用前文的总微分 $D=d'+d''$。各列乘这个常符号不改变其核、像或同调；原图箭头和标签仍照原书保留。

第一个最容易。固定 $p$，有内射解消

$$
0\to TC^p\to I_{TC}^p,
$$

这里用 $I_{TC}^p$ 代替 $I_{TC^p}$。这就是图中的第 $p$ 列。根据导出函子的定义，$GI^p$ 是一个同调为 $R^qG$ 的复形；换言之，关于 $d''$ 取同调，得到

$$
{}''H^{p,q}(GI)=H^q(GI^p)=(R^qG)(TC^p).
$$

根据假设，$C^p$ 内射蕴涵当 $q>0$ 时 $(R^qG)(TC^p)=0$。由于 $G$ 左正合，有 $R^0G(TC^p)=G(TC^p)$。因此得到

$$
{}''H^{p,q}(GI)=\begin{cases}GT(C^p)&\text{如果 }q=0,\\0&\text{如果 }q>0.\end{cases}
$$

> **译校注：** 原文上句印为 $R^0G(TC^p)=TC^p$，右端漏了 $G$，应为 $G(TC^p)=GT(C^p)$；这是左正合函子与其零次右导出函子的识别，也与紧接的分段式一致。

因此非零项位于 $p$ 轴上，其形式为

$$
0\to GT(C^0)\to GT(C^1)\to GT(C^2)\to.
$$

取 ${}'H^p$，得到

$$
{}^1E_2^{p,q}(A)=\begin{cases}R^p(GT)(A)&\text{如果 }q=0,\\0&\text{如果 }q>0.\end{cases}
$$

由此得到

$$
H^n(\operatorname{Tot}(GI))\approx R^n(GT)(A).
$$

<span class="original-page-anchor" id="pdf-page-831" aria-hidden="true"></span>

第二个谱序列将充分利用引理 9.5，而在证明的第一部分中尚未用到其全部内容；因此现在解消 $I_{TC}$ 的完全内射性就很重要。于是有内射解消

$$
\begin{aligned}
0&\to Z^p(TC)\to{}^1Z^{0,p}\to{}^1Z^{1,p}\to{}^1Z^{2,p}\to,\\
0&\to B^p(TC)\to{}^1B^{0,p}\to{}^1B^{1,p}\to{}^1B^{2,p}\to,\\
0&\to H^p(TC)\to{}^1H^{0,p}\to{}^1H^{1,p}\to{}^1H^{2,p}\to,
\end{aligned}
$$

以及正合列

$$
\begin{aligned}
0&\to{}^1Z^{q,p}\to I^{q,p}\to{}^1B^{q+1,p}\to0,\\
0&\to{}^1B^{q,p}\to{}^1Z^{q,p}\to{}^1H^{q,p}\to0,
\end{aligned}
$$

由于各项的内射性，它们都分裂。以 $I^{(p)}$ 表示双复形 $I=\{I^{q,p}\}$ 的第 $p$ 行。于是得到：

> **译校注：** 原书的双指标次序发生切换：印刷页820的正文使用“解消次数、原复形次数”，印刷页822的二维图则把第一指标放在横向原复形方向，第二指标放在竖直解消方向。本页最上面的三条解消又沿用前一种次序，随后按第 $p$ 行取同调以及第二谱序列的推导，则以 $q$ 为原复形的次数（即 $T$ 的上同调次数），以 $p$ 为内射解消的次数（即 $G$ 的上同调次数），最终得到 $E_2^{p,q}=R^pG(R^qT(A))$。两种写法均照原书保留；阅读时须按各段所用的次序理解，而不把三条开头解消的指标顺序直接套到后面的计算。

$$
\begin{aligned}
{}'H^{q,p}(GI)&=H^q(GI^{(p)})=G{}^1Z^{q,p}/G{}^1B^{q,p}&&\text{由第一个分裂序列}\\
&=G{}'H^{q,p}(I)&&\text{由第二个分裂序列},
\end{aligned}
$$

因为对分裂正合列施行函子 $G$，仍得到分裂正合列。

于是

$$
{}^2E_2^{p,q}={}''H^p({}'H^{q,p}(GI))=H^p(G{}'H^{q,p}(I)).
$$

由解消的完全内射性，复形 ${}'H^{q,p}(I)$（$p\geqq0$）是

$$
H^q(TC)=(R^qT)(A)
$$

的一个内射解消。

此外，有

$$
H^p(G{}'H^{q,p})=R^pG(R^qT(A)),
$$

因为导出函子是内射解消的同调。这就证明 $(R^pG)R^qT(A)$ 收敛到 $R^n(GT)(A)$，并结束了定理的证明。

> **译校注：** 原文最后一句的表达式印为 $(R^pG)R^qT(A))$，末尾多了一个右括号；译文去除这个多余括号。

为看到谱序列如何起作用，给出一个与 §3 讨论的欧拉示性数有关的应用。

设 $\mathfrak{A}$ 有足够多的内射对象，且

$$
T:\mathfrak{A}\to\mathfrak{B}
$$

是协变左正合函子。设 $\mathfrak{F}_{\mathfrak{A}}$ 是 $\mathfrak{A}$ 中的一个对象族，产生一个 **K-群**。更具体地说，在 $\mathfrak{A}$ 的一个短正合列中，如果两个对象属于 $\mathfrak{F}_{\mathfrak{A}}$，那么第三个也属于它。还假定 $\mathfrak{F}_{\mathfrak{A}}$ 中的对象有**有限的 $RT$-维数**；根据定义，这是说，如果 $A\in\mathfrak{F}_{\mathfrak{A}}$，那么 $R^iT(A)=0$<span class="original-page-anchor" id="pdf-page-832" aria-hidden="true"></span>对于所有充分大的 $i$ 都成立。事实上，可以取 $\mathfrak{F}_{\mathfrak{A}}$ 为 $\mathfrak{A}$ 中所有具有有限 $RT$-维数的对象组成的族。

把 $\mathbf{K}(\mathfrak{F}_{\mathfrak{A}})$ 上的**与 $T$ 相伴的欧拉示性数**定义为

$$
\chi_T(A)=\sum_{i=0}^\infty(-1)^i\operatorname{cl}(R^iT(A)).
$$

这里 cl 表示 **K-群** $\mathbf{K}(\mathfrak{F}_{\mathfrak{B}})$ 中的类；这个群与 $\mathfrak{B}$ 中的某个对象族 $\mathfrak{F}_{\mathfrak{B}}$ 相伴，并要求对所有 $A\in\mathfrak{F}_{\mathfrak{A}}$，都有 $R^iT(A)\in\mathfrak{F}_{\mathfrak{B}}$。这是使公式有意义的最低要求。

**引理 9.7。** *映射 $\chi_T$ 延拓成一个同态*

$$
\mathbf{K}(\mathfrak{F}_{\mathfrak{A}})\to\mathbf{K}(\mathfrak{F}_{\mathfrak{B}}).
$$

*证明。* 设

$$
0\to A'\to A\to A''\to0
$$

是 $\mathfrak{F}$ 中的正合列。那么有上同调序列

$$
\to R^iT(A')\to R^iT(A)\to R^iT(A'')\to R^{i+1}T(A')\to,
$$

其中除有限项外，所有项都为 $0$。在 **K-群** 中取交错和，表明 $\chi_T$ 是欧拉–庞加莱映射，证明至此完成。

注意，这只是把 §3 中的内容放到一个更丰富的情形中重复了一遍。

在下一个定理中，有另一个函子

$$
G:\mathfrak{B}\to\mathfrak{C},
$$

还有一个产生 **K-群** $\mathbf{K}(\mathfrak{F}_{\mathfrak{C}})$ 的对象族 $\mathfrak{F}_{\mathfrak{C}}$。假定每一步都可以进行上述过程，还需要某个条件以便应用谱序列。确切地说，假定：

**CHAR 1.** 对所有 $i$，$R^iT$ 把 $\mathfrak{F}_{\mathfrak{A}}$ 映到 $\mathfrak{F}_{\mathfrak{B}}$，$R^iG$ 把 $\mathfrak{F}_{\mathfrak{B}}$ 映到 $\mathfrak{F}_{\mathfrak{C}}$，而 $R^i(GT)$ 把 $\mathfrak{F}_{\mathfrak{A}}$ 映到 $\mathfrak{F}_{\mathfrak{C}}$。

**CHAR 2.** $\mathfrak{F}_{\mathfrak{A}}$ 中一个元素的每个子对象都属于 $\mathfrak{F}_{\mathfrak{A}}$，并具有有限的 $RT$-维数和 $R(GT)$-维数；$\mathfrak{F}_{\mathfrak{B}}$ 中一个元素的每个子对象都属于 $\mathfrak{F}_{\mathfrak{B}}$，并具有有限的 $RG$-维数。

**定理 9.8。** *假定 $T:\mathfrak{A}\to\mathfrak{B}$ 和 $G:\mathfrak{B}\to\mathfrak{C}$ 满足条件 **CHAR 1** 和 **CHAR 2**。还假定 $T$ 把内射对象映到 $G$-无环对象。那么*

$$
\chi_G\circ\chi_T=\chi_{GT}.
$$

<span class="original-page-anchor" id="pdf-page-833" aria-hidden="true"></span>

*证明。* 根据定理 9.6，复合函子的 Grothendieck 谱序列给出 $R^n(GT)(A)$ 的一个滤过

$$
\cdots\supset F^pR^n(GT)(A)\supset F^{p+1}R^n(GT)(A)\supset\cdots,
$$

满足

$$
F^p/F^{p+1}\approx E_\infty^{p,n-p}.
$$

> **译校注：** 原文此处印为递增的包含关系 $\cdots\subset F^p\subset F^{p+1}\subset\cdots$，并把商印为 $F^{p+1}/F^p$。根据前文 §9 所定义的递减滤过和 $\operatorname{Gr}^p=F^p/F^{p+1}$，这里应采用上面的递减包含关系及商的顺序，使之与同一谱序列的 $E_\infty^{p,n-p}$ 一致。

于是

$$
\begin{aligned}
\chi_{GT}(A)&=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(R^n(GT)(A))\\
&=\sum_{n=0}^\infty(-1)^n\sum_{p=0}^\infty\operatorname{cl}(E_\infty^{p,n-p})\\
&=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_\infty^n).
\end{aligned}
$$

另一方面，

$$
\chi_T(A)=\sum_{q=0}^\infty(-1)^q\operatorname{cl}(R^qT(A)),
$$

所以

$$
\begin{aligned}
\chi_G\circ\chi_T(A)&=\sum_{q=0}^\infty(-1)^q\chi_G(R^qT(A))\\
&=\sum_{q=0}^\infty(-1)^q\sum_{p=0}^\infty(-1)^p\operatorname{cl}(R^pG(R^qT(A)))\\
&=\sum_{n=0}^\infty(-1)^n\sum_{p=0}^n\operatorname{cl}(R^pG(R^{n-p}T(A)))\\
&=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_2^n).
\end{aligned}
$$

由于 $E_{r+1}$ 是 $E_r$ 的同调，得到

$$
\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_2^n)=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_3^n)=\cdots=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_\infty^n).
$$

定理的证明至此完成。

<span class="original-page-anchor" id="pdf-page-834" aria-hidden="true"></span>

## 习题

**1.** 证明 §1 给出的标准复形的例子确实是一个复形，而且正合，因而给出 $\mathbf{Z}$ 的一个解消。［*提示：* 为证明标准复形的序列正合，选取元素 $z\in S$，并以下式定义 $h:E^i\to E^{i+1}$：

$$
h(x_0,\ldots,x_i)=(z,x_0,\ldots,x_i).
$$

证明 $dh+hd=\operatorname{id}$，并且 $dd=0$。正合性立即得出。］

### 群的上同调

**2.** 设 $G$ 是一个群。在标准复形中用 $G$ 作集合 $S$。以下式定义 $G$ 在标准复形 $E$ 上的作用：

$$
x(x_0,\ldots,x_i)=(xx_0,\ldots,xx_i).
$$

证明每个 $E_i$ 都是群环 $\mathbf{Z}[G]$ 上的自由模。因此，如果令 $R=\mathbf{Z}[G]$ 为群环，并考察 $G$-模的范畴 $\operatorname{Mod}(G)$，那么标准复形就在这个范畴中给出 $\mathbf{Z}$ 的一个自由解消。

**3.** 标准复形 $E$ 以齐次形式写出，所以边界映射具有某种对称性。还有另一个复形，表现出如下有用的特点。令 $F^i$ 为以 $i$-元组（而非 $(i+1)$-元组）$(x_1,\ldots,x_i)$ 为基的自由 $\mathbf{Z}[G]$-模。当 $i=0$ 时，取 $F_0=\mathbf{Z}[G]$ 本身。以下式定义边界算子：

$$
\begin{aligned}
d(x_1,\ldots,x_i)&=x_1(x_2,\ldots,x_i)+\sum_{j=1}^{i-1}(-1)^j(x_1,\ldots,x_jx_{j+1},\ldots,x_i)\\
&\qquad+(-1)^i(x_1,\ldots,x_{i-1}).
\end{aligned}
$$

> **译校注：** 原文最后一项印为 $(-1)^{i+1}(x_1,\ldots,x_i)$，应为 $(-1)^i(x_1,\ldots,x_{i-1})$。边界必须从 $i$-元组降到 $(i-1)$-元组；在下方对应的齐次 $(i+1)$-元组中，删去最后一个分量的符号为 $(-1)^i$，重新写成非齐次形式恰好得到这里的末项。

证明由对应

$$
(x_1,\ldots,x_i)\mapsto(1,x_1,x_1x_2,\ldots,x_1x_2\cdots x_i)
$$

得到 $E\approx F$（作为 $G$-模的复形），并且在这个同构下，给 $F$ 定义的算子 $d$ 对应于给 $E$ 定义的算子 $d$。

**4.** 如果 $A$ 是 $G$-模，令 $A^G$ 为由所有满足对任意 $x\in G$ 都有 $xv=v$ 的元素 $v\in A$ 组成的子模。因此 $A^G$ 上的 $G$-作用平凡。（这个记号使用方便，但与第 XVIII 章中诱导模所用的记号*不同*。）

(a) 证明，如果 $H^q(G,A)$ 表示复形 $\operatorname{Hom}_G(E,A)$ 的第 $q$ 个同调，那么 $H^0(G,A)=A^G$。因此，$A\mapsto A^G$ 的右导出函子是复形 $\operatorname{Hom}_G(E,A)$ 的同调群，或者也可以用复形 $\operatorname{Hom}(F,A)$，其中 $F$ 如习题 3 所定义。

> **译校注：** 原文称这里为“left derived functors”，即左导出函子，应为右导出函子：不变元函子 $A\mapsto A^G=\operatorname{Hom}_G(\mathbf{Z},A)$ 协变且左正合，其正次数导出函子是 $\operatorname{Ext}_G^q(\mathbf{Z},A)$。

(b) 证明 $1$-闭链的群 $Z^1(G,A)$ 由满足

$$
f(x)+xf(y)=f(xy)\quad\text{对所有 }x,y\in G
$$

的函数 $f:G\to A$ 组成。

证明上边界子群 $B^1(G,A)$ 由具有如下性质的函数 $f$ 组成：存在元素 $a\in A$，使 $f(x)=xa-a$。商群就是 $H^1(G,A)$。关于一个特殊情形的确定，参见第 VI 章 §10。

<span class="original-page-anchor" id="pdf-page-835" aria-hidden="true"></span>

(c) 证明 $2$-上闭链的群 $Z^2(G,A)$ 由满足

$$
xf(y,z)-f(xy,z)+f(x,yz)-f(x,y)=0
$$

的函数 $f:G\times G\to A$ 组成。

> **译校注：** 原文把函数的定义域印为 $G$，应为 $G\times G$，因为此处 $f$ 接受两个群元素，正如所列上闭链等式中的每一项所示。

这样的 $2$-上闭链也称为**因子集**，可以用来描述群扩张的同构类，如下。

**5. 群扩张。** 设 $W$ 是群，$A$ 是一个以乘法记号书写的正规子群。令 $G=W/A$ 为商群。设 $F:G\to W$ 是陪集代表元的一个选取。定义

$$
f(x,y)=F(x)F(y)F(xy)^{-1}.
$$

(a) 证明 $f$ 取值于 $A$，而且 $f:G\times G\to A$ 是一个 $2$-上闭链。

> **译校注：** 在前题的普通群上同调意义下，(a) 还须假定 $A$ 阿贝尔，并使用扩张诱导的 $G$-作用 $x\cdot a=F(x)aF(x)^{-1}$；此时该作用与代表元的选取无关，结合律给出 $2$-上闭链关系。若 $A$ 非阿贝尔，$f$ 仍是取值于 $A$ 的因子集，但伴随的共轭映射一般不能给出普通 $G$-模作用，不能直接称为上一题意义下的 $2$-上闭链。

(b) 给定群 $G$ 和阿贝尔群 $A$，把扩张 $W$ 看成正合列

$$
1\to A\to W\to G\to1.
$$

证明如果两个这样的扩张同构，那么像 (a) 中那样与它们相伴的 $2$-上闭链在 $H^2(G,A)$ 中确定相同的类。

> **译校注：** 原文此处印为 $H^1(G,A)$，应为 $H^2(G,A)$，因为所用的是 $2$-上闭链；下一问也明确使用 $H^2(G,A)$。这里及 (c) 的扩张分类须固定 $G$ 在 $A$ 上的作用，并把扩张同构理解为在两端 $A,G$ 上诱导恒等的正合列同构；不同作用或只考虑抽象群 $W$ 的同构，均不对应同一个 $H^2(G,A)$ 分类。

(c) 证明上面得到的从群扩张的同构类到 $H^2(G,A)$ 的映射是双射。

**6. 上同调函子的态射。** 设 $\lambda:G'\to G$ 是群同态。那么 $\lambda$ 产生一个正合函子

$$
\Phi_\lambda:\operatorname{Mod}(G)\to\operatorname{Mod}(G'),
$$

因为每个 $G$-模都可以看成 $G'$-模，只需把 $\sigma'\in G'$ 的作用定义为 $\sigma'a=\lambda(\sigma')a$。于是得到上同调函子 $H^{G'}\circ\Phi_\lambda$。

设 $G'$ 是 $G$ 的一个子群。在维数 $0$，有函子态射

$$
\lambda^*:H_G^0\to H_{G'}^0\circ\Phi_\lambda,\quad\text{由包含 }A^G\hookrightarrow A^{G'}=\Phi_\lambda(A)^{G'}\text{ 给出}.
$$

(a) 证明存在唯一的 $\delta$-函子态射

$$
\lambda^*:H_G\to H_{G'}\circ\Phi_\lambda,
$$

它在 $H_G^0$ 上具有上述作用。有以下重要的特殊情形。

**限制。** 设 $H$ 是 $G$ 的一个子群，$A$ 是 $G$-模。从 $G$ 到 $A$ 的函数限制为从 $H$ 到 $A$ 的函数。这样得到一个自然同态，称为**限制**：

$$
\operatorname{res}:H^q(G,A)\to H^q(H,A).
$$

**膨胀。** 假定 $H$ 在 $G$ 中正规。设 $A^H$ 是由 $A$ 中被 $H$ 固定的元素组成的子群。立即可验证 $A^H$ 在 $G$ 下稳定，因而是 $G/H$-模。包含 $A^H\hookrightarrow A$ 诱导同态

$$
H_G^q(u)=u_q:H^q(G,A^H)\to H^q(A).
$$

定义**膨胀映射**

$$
\operatorname{inf}_{G/H}^H:H^q(G/H,A^H)\to H^q(G,A)
$$

<span class="original-page-anchor" id="pdf-page-836" aria-hidden="true"></span>

为函子性态射 $H^q(G/H,A^H)\to H^q(G,A^H)$ 与上述诱导同态 $u_q=H_G^q(u)$ 的复合。

在维数 $0$，膨胀映射给出恒等 $(A^H)^{G/H}=A^G$。

(b) 证明膨胀映射在标准上链复形上可以由一个自然映射表示：它把一个从 $G/H$ 到 $A^H$ 的函数对应到一个从 $G$ 到 $A^H\subset A$ 的函数。

(c) 证明下列序列正合：

$$
0\to H^1(G/H,A^H)\xrightarrow{\operatorname{inf}}H^1(G,A)\xrightarrow{\operatorname{res}}H^1(H,A).
$$

(d) 描述如何“通过共轭”以及函子性，在上同调函子 $H_G$ 上得到 $G$ 的作用。

(e) 在 (c) 中，证明右边限制映射的像事实上属于 $H^1(H,A)^G$（在 $G$ 下固定的子群）。

**注。** 对于高次上同调群有类似结果，其证明需要 Hochschild–Serre 谱序列。参见 [La 96]，第 VI 章 §2，定理 2。实际上，当 $K$ 是伽罗瓦扩张时，正是这个关于 $H^2$ 的版本应用于 $H^2(G,K^*)$，并用于类域论 [ArT 67]。

**7.** 设 $G$ 是群，$B$ 是阿贝尔群，$M_G(B)=M(G,B)$ 是从 $G$ 到 $B$ 的映射的集合。对于 $x\in G$ 和 $f\in M(G,B)$，定义 $([x]f)(y)=f(yx)$。

(a) 证明 $B\mapsto M_G(B)$ 是从 $\operatorname{Mod}(\mathbf{Z})$（阿贝尔群的范畴）到 $\operatorname{Mod}(G)$ 的一个协变、加性、正合函子。

(b) 设 $G'$ 是 $G$ 的一个子群，$G=\bigcup x_jG'$ 是一个陪集分解。对于 $f\in M(G,B)$，令 $f_j$ 为 $M(G',B)$ 中满足 $f_j(y)=f(x_jy)$ 的函数。证明映射

$$
f\mapsto\prod_j f_j
$$

是从 $M(G,B)$ 到 $\prod_jM(G',B)$ 的一个 $G'$-同构。

**8.** 对每个 $G$-模 $A\in\operatorname{Mod}(G)$，由条件 $\varepsilon_A(a)=\text{函数 }f_a$，其中对于 $\sigma\in G$ 有 $f_a(\sigma)=\sigma a$，定义 $\varepsilon_A:A\to M(G,A)$。证明 $a\mapsto f_a$ 是 $G$-模的一个嵌入，并且正合列

$$
0\to A\xrightarrow{\varepsilon_A}M(G,A)\to X_A=\operatorname{coker}\varepsilon_A\to0
$$

在 $\mathbf{Z}$ 上分裂。（事实上，映射 $f\mapsto f(e)$ 使左边的箭头分裂。）

**9.** 设 $B\in\operatorname{Mod}(\mathbf{Z})$。令 $H^q$ 为 $A\mapsto A^G$ 的右导出函子。

> **译校注：** 原文仍印为“left derived functor”，应为右导出函子，理由与习题 4(a) 相同：不变元函子是协变左正合的 $\operatorname{Hom}_G(\mathbf{Z},-)$。

(a) 证明 $H^q(G,M_G(B))=0$ 对所有 $q>0$ 成立。［*提示：* 使用收缩同伦

$$
s:C^r(G,M_G(B))\to C^{r-1}(G,M_G(B)),\quad\text{定义为}\quad(sf)_{x_2,\ldots,x_r}(x)=f_{x,x_2,\ldots,x_r}(1).
$$

证明 $f=sdf+dsf$。］因此 $M_G$ 消去上同调函子。

(b) 还要证明，对 $G$ 的所有子群 $G'$，当 $q>0$ 时都有 $H^q(G',M_G(B))=0$。

**10.** 设 $G$ 是群，$S$ 是一个子群。证明定义在 $\operatorname{Mod}(G)\times\operatorname{Mod}(S)$ 上、取值于 $\operatorname{Mod}(\mathbf{Z})$ 的双函子

$$
(A,B)\mapsto\operatorname{Hom}_G(A,M_G^S(B))\quad\text{和}\quad(A,B)\mapsto\operatorname{Hom}_S(A,B)
$$

同构。这个同构由下列映射给出：

$$
\varphi\mapsto(a\mapsto g_a),\quad\text{其中 }\varphi\in\operatorname{Hom}_S(A,B),\quad g_a(\sigma)=\varphi(\sigma a),\quad g_a\in M_G^S(B).
$$

<span class="original-page-anchor" id="pdf-page-837" aria-hidden="true"></span>

逆映射由下式给出：

$$
f\mapsto f(1),\quad f\in\operatorname{Hom}_G(A,M_G^S(B)).
$$

> **译校注：** 此处的 $f(1)$ 是对函数值在 $1\in G$ 处求值的简记；展开写就是把 $f$ 对应到映射 $a\mapsto f(a)(1)$，不是把 $1$ 当成任意模 $A$ 的一个指定元素。

回忆 $M_G^S(B)$ 已在第 XVIII 章 §7 关于诱导表示的讨论中定义。基本上，你应该已经知道上述同构。

**11.** 设 $G$ 是群，$S$ 是一个子群。证明对于 $B\in\operatorname{Mod}(S)$，映射

$$
H^q(G,M_G^S(B))\to H^q(S,B),
$$

由限制映射 $\operatorname{res}_S^G$ 与 $S$-同态 $f\mapsto f(1)$ 复合得到，当 $q>0$ 时是同构。［*提示：* 使用上同调函子的唯一性定理。］

**12.** 设 $G$ 是群，$\varepsilon:\mathbf{Z}[G]\to\mathbf{Z}$ 是满足 $\varepsilon(\sum n(x)x)=\sum n(x)$ 的同态。令 $I_G$ 为它的核。证明 $I_G$ 是 $\mathbf{Z}[G]$ 的一个理想，而且有函子同构（在群的范畴上）

$$
G/G^c\approx I_G/I_G^2,\quad\text{由 }xG^c\mapsto(x-1)+I_G^2\text{ 给出}.
$$

**13.** 设 $A\in\operatorname{Mod}(G)$，$\alpha\in H^1(G,A)$。设 $\{a(x)\}_{x\in G}$ 是代表 $\alpha$ 的一个标准 $1$-上闭链。证明存在 $G$-同态 $f:I_G\to A$，满足 $f(x-1)=a(x)$，所以 $f\in(\operatorname{Hom}(I_G,A))^G$。证明序列

$$
0\to A=\operatorname{Hom}(\mathbf{Z},A)\to\operatorname{Hom}(\mathbf{Z}[G],A)\to\operatorname{Hom}(I_G,A)\to0
$$

正合，并且如果 $\delta$ 是上同调序列的上边缘映射，那么 $\delta(f)=-\alpha$。

### 有限群

现在转向*有限*群 $G$ 的情形。对这种群和一个 $G$-模 $A$，有**迹映射**

$$
T_G:A\to A,\quad\text{定义为}\quad T_G(a)=\sum_{\sigma\in G}\sigma a.
$$

如果存在一个 $\mathbf{Z}$-自同态 $u:A\to A$，使 $\operatorname{id}_A=T_G(u)$，就称模 $A$ 为 **$G$-正则的**。回忆 $G$ 在 $\operatorname{End}(A)$ 上的作用由下式给出：

$$
[\sigma]f(a)=\sigma f(\sigma^{-1}a)\quad\text{对于 }\sigma\in G.
$$

**14.** (a) 证明 $\operatorname{Mod}(G)$ 中的投射对象是 $G$-正则的。

(b) 设 $R$ 是交换环，$A$ 属于 $\operatorname{Mod}_R(G)$（$(G,R)$-模的范畴）。证明 $A$ 是 $R[G]$-投射的，当且仅当 $A$ 是 $R$-投射的且 $R[G]$-正则；后者的含义是对于某个 $R$-同态 $u:A\to A$，有 $\operatorname{id}_A=T_G(u)$。

**15.** 考察正合列：

$$
\begin{aligned}
\text{(1)}\qquad&0\to I_G\to\mathbf{Z}[G]\xrightarrow{\varepsilon}\mathbf{Z}\to0,\\
\text{(2)}\qquad&0\to\mathbf{Z}\xrightarrow{\varepsilon'}\mathbf{Z}[G]\to J_G\to0,
\end{aligned}
$$

其中第一个定义 $I_G$，第二个由嵌入

$$
\varepsilon':\mathbf{Z}\to\mathbf{Z}[G],\quad\text{满足 }\varepsilon'(n)=n\left(\sum\sigma\right)
$$

定义，即映到“对角线”上。按定义，$\varepsilon'$ 的余核是 $J_G$。

(a) 证明序列 (1) 和 (2) 都在 $\operatorname{Mod}(G)$ 中分裂。

> **译校注：** 对非平凡有限群 $G$，原题的“在 $\operatorname{Mod}(G)$ 中分裂”不成立；两列是在 $\operatorname{Mod}(\mathbf{Z})$ 中分裂。若 (1) 有 $G$-模截面，$1$ 的像须为 $\mathbf{Z}[G]^G$ 中的 $k\sum_{\sigma\in G}\sigma$，其增广为 $k|G|$，不可能等于 $1$。若 (2) 有 $G$-模收缩映射 $\mathbf{Z}[G]\to\mathbf{Z}$，它在各群元上的值同为某个整数 $k$，与 $\varepsilon'$ 复合也是乘以 $k|G|$，同样不可能为恒等。原题保留，以明确其范畴条件的问题。

<span class="original-page-anchor" id="pdf-page-838" aria-hidden="true"></span>

(b) 对于 $A\in\operatorname{Mod}(G)$，定义 $M'_G(A)=\mathbf{Z}[G]\otimes A$（在 $\mathbf{Z}$ 上的张量积）。证明 $M'_G(A)$ 是 $G$-正则的，并且把 (1) 和 (2) 与 $A$ 作张量积，就得到正合列 $(1_A)$ 和 $(2_A)$。由此得到嵌入

$$
\varepsilon'_A=\varepsilon'\otimes\operatorname{id}:A=\mathbf{Z}\otimes A\to\mathbf{Z}[G]\otimes A.
$$

**16. 循环群。** 设 $G$ 是阶为 $n$ 的有限循环群，$\sigma$ 是 $G$ 的一个生成元。令 $K^i=\mathbf{Z}[G]$，$i>0$。令 $\varepsilon:K^0\to\mathbf{Z}$ 为以前的增广映射。对于奇数 $i\geqq1$，令 $d^i:K^i\to K^{i-1}$ 为乘以 $1-\sigma$ 的映射。对于偶数 $i\geqq2$，令 $d^i$ 为乘以 $1+\sigma+\cdots+\sigma^{n-1}$ 的映射。证明 $K$ 是 $\mathbf{Z}$ 的一个解消。由此推出：

*对于奇数 $i$：* $H^i(G,A)=A_T/(1-\sigma)A$，其中 $T_G:a\mapsto(1+\sigma+\cdots+\sigma^{n-1})a$；

*对于偶数 $i\geqq2$：* $H^i(G,A)=A^G/T_GA$，其中 $A_T$ 是 $T_G$ 在 $A$ 中的核。

> **译校注：** 原文两种奇偶情形的结果印反了：奇数处印 $A^G/T_GA$，偶数处印 $A_T/(1-\sigma)A$。对给定解消施行 $\operatorname{Hom}_G(-,A)$，得到 $A\xrightarrow{1-\sigma}A\xrightarrow{T_G}A\xrightarrow{1-\sigma}A\to\cdots$，所以一阶同调为 $\ker T_G/(1-\sigma)A$，二阶为 $\ker(1-\sigma)/T_GA$，并按周期二重复。例如 $A=\mathbf{Z}$ 取平凡作用、$n>1$ 时，$H^1(G,\mathbf{Z})=0$，而原文奇数式给出 $\mathbf{Z}/n\mathbf{Z}$。构造中还按增广映射的用法取 $K^0=\mathbf{Z}[G]$；原文只明说了 $i>0$ 的项。

**17.** 设 $G$ 是有限群。证明存在从 $\operatorname{Mod}(G)$ 到 $\operatorname{Mod}(\mathbf{Z})$ 的一个 $\delta$-函子 $\mathbf{H}$，使得：

(1) $\mathbf{H}^0$ 同构于函子 $A\mapsto A^G/T_GA$。

(2) 如果 $A$ 内射且 $q>0$，那么 $\mathbf{H}^q(A)=0$；如果 $A$ 投射且 $q$ 任意，那么 $\mathbf{H}^q(A)=0$。

(3) $\mathbf{H}$ 可由 $G$-正则模消去。特别地，$\mathbf{H}$ 可由 $M_G$ 消去。

习题 17 的 $\delta$-函子称为**特殊上同调函子**。它仅在维数 $0$ 与另一个上同调函子不同。

> **译校注：** 这里的特殊零次函子 $A\mapsto A^G/T_GA$ 不左正合，因此“$\delta$-函子”不能严格采用 §7 **DEL 1** 中长正合列以 $0\to H^0(A')$ 开始的规定。例如 $|G|=n>1$ 时，短正合列 $0\to\mathbf{Z}\to\mathbf{Z}[G]\to J_G\to0$ 在特殊零次上同调上给出 $\mathbf{Z}/n\mathbf{Z}\to0$，不是单态。通常对特殊（Tate）上同调省去这个首端 $0$，或接入负次数的项，才得到完整长正合列；其正次数仍为普通群上同调。

**18.** 设 $\mathbf{H}=\mathbf{H}_G$ 是有限群 $G$ 的特殊上同调函子。证明：

$$
\begin{aligned}
\mathbf{H}^0(I_G)&=0;\quad\mathbf{H}^0(\mathbf{Z})\approx\mathbf{H}^1(I)\approx\mathbf{Z}/n\mathbf{Z}\quad\text{其中 }n=\#(G);\\
\mathbf{H}^0(\mathbf{Q}/\mathbf{Z})&=\mathbf{H}^1(\mathbf{Z})=\mathbf{H}^2(I)=0,\\
\mathbf{H}^1(\mathbf{Q}/\mathbf{Z})&\approx\mathbf{H}^2(\mathbf{Z})\approx\mathbf{H}^3(I)\approx\widehat{G}=\operatorname{Hom}(G,\mathbf{Q}/\mathbf{Z})\quad\text{按定义}.
\end{aligned}
$$

### 内射对象

**19.** (a) 证明如果阿贝尔群 $T$ 在阿贝尔群的范畴中内射，那么它可除。

(b) 设 $A$ 是主理想整环。仿照阿贝尔群的情形，对模定义由 $A$ 的元素可除的概念。证明一个 $A$-模内射当且仅当它是 $A$-可除的。［对 $\mathbf{Z}$ 的证明应以完全相同的方式成立。］

**20.** 设 $S$ 是交换诺特环 $A$ 的一个乘法子集。如果 $I$ 是内射 $A$-模，证明 $S^{-1}I$ 是内射 $S^{-1}A$-模。

**21.** (a) 证明投射模的直和是投射的。

(b) 证明内射模的直积是内射的。

**22.** 证明可除模的商模、直和项、直积及直和都可除。

**23.** 设 $Q$ 是交换环 $A$ 上的一个模。假定对于 $A$ 的每个左理想 $J$，每个同态 $\varphi:J\to Q$ 都可以延拓成从 $A$ 到 $Q$ 的同态。证明 $Q$ 内射。［*提示：* 给定 $M'\subset M$ 和 $f:M'\to Q$，取 $x_0\in M$ 且 $x_0\notin M'$。令 $J$ 为由满足 $ax_0\in M'$ 的元素 $a\in A$ 组成的左理想。令 $\varphi(a)=f(ax_0)$，并依假设把 $\varphi$ 延拓到 $A$。然后证明<span class="original-page-anchor" id="pdf-page-839" aria-hidden="true"></span>可以由公式

$$
f(x'+bx_0)=f(x')+\varphi(b)
$$

把 $f$ 延拓到 $M'+Ax_0$，其中 $x'\in M'$、$b\in A$。然后使用佐恩引理。这与引理 4.2 的证明具有相同的方式。］

> **译校注：** 原文此处印为“extend $f$ to $M$”以及“$x'\in M$”。按上一页给定的 $f:M'\to Q$，这个公式先定义在 $M'+Ax_0$ 上，并须取 $x'\in M'$，否则右端 $f(x')$ 尚未定义。随后再用佐恩引理，把这种单步延拓扩展到整个 $M$。

**24.** 设

$$
0\to I_1\to I_2\to I_3\to0
$$

是模的正合列。假定 $I_1,I_2$ 内射。

(a) 证明此序列分裂。

(b) 证明 $I_3$ 内射。

(c) 如果 $I$ 内射且 $I=M\oplus N$，证明 $M$ 内射。

**25.** （读过诺特环的内容之后再做此题。）设 $A$ 是诺特交换环，$Q$ 是内射 $A$-模。设 $\mathfrak{a}$ 是 $A$ 的一个理想，令 $Q^{(\mathfrak{a})}$ 为由满足对于某个依赖于 $x$ 的 $n$，有 $\mathfrak{a}^nx=0$ 的元素 $x\in Q$ 组成的子集。证明 $Q^{(\mathfrak{a})}$ 内射。［*提示：* 使用习题 23。］

**26.** 设 $A$ 是交换环，$E$ 是 $A$-模，$E^\wedge=\operatorname{Hom}_{\mathbf{Z}}(E,\mathbf{Q}/\mathbf{Z})$ 是对偶模。证明下列断言。

(a) 序列

$$
0\to N\to M\to E\to0
$$

正合，当且仅当对偶序列

$$
0\to E^\wedge\to M^\wedge\to N^\wedge\to0
$$

正合。

(b) 设 $F$ 在 $A$-模的范畴中平坦，$I$ 内射。证明 $\operatorname{Hom}_A(F,I)$ 内射。

(c) $E$ 平坦当且仅当 $E^\wedge$ 内射。

**27. 模的扩张。** 设 $M,N$ 是一个环上的模。所谓 $M$ 通过 $N$ 的一个**扩张**，是指一个正合列

$$
\text{(*)}\qquad0\to N\to E\to M\to0.
$$

现在定义从这种扩张到 $\operatorname{Ext}^1(M,N)$ 的映射。设 $P$ 投射，并有到 $M$ 的满同态，得到正合列

$$
\text{(**)}\qquad0\to K\xrightarrow{w}P\xrightarrow{p}M\to0,
$$

其中 $K$ 定义为核。由于 $P$ 投射，存在同态 $u:P\to E$，并有一个依赖于 $u$ 的唯一同态 $v:K\to N$，使图交换：

$$
\begin{array}{ccccccccc}
0&\longrightarrow&K&\longrightarrow&P&\longrightarrow&M&\longrightarrow&0\\
&&{\scriptstyle v}\downarrow&&{\scriptstyle u}\downarrow&&{\scriptstyle\operatorname{id}}\downarrow&&\\
0&\longrightarrow&N&\longrightarrow&E&\longrightarrow&M&\longrightarrow&0
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-840" aria-hidden="true"></span>

另一方面，有正合列

$$
\text{(***)}\qquad0\to\operatorname{Hom}(M,N)\to\operatorname{Hom}(P,N)\to\operatorname{Hom}(K,N)\to\operatorname{Ext}^1(M,N)\to0,
$$

其中右边的最后一项为 $0$，因为 $\operatorname{Ext}^1(P,N)=0$。把扩张 (\*) 对应到 $v$ 在 $\operatorname{Ext}^1(M,N)$ 中的像。

证明这一对应是扩张的同构类（即形如 (\*) 的正合列的同构类）与 $\operatorname{Ext}^1(M,N)$ 之间的双射。［*提示：* 如下构造逆映射。给定 $\operatorname{Ext}^1(M,N)$ 的元素 $e$，利用正合列 (\*\*)，存在某个元素 $v\in\operatorname{Hom}(K,N)$，在 (\*\*\*) 中映到 $e$。令 $E$ 为 $v$ 和 $w$ 的推出。换言之，令 $J$ 为 $N\oplus P$ 的子模，由所有 $x\in K$ 给出的元素 $(v(x),-w(x))$ 组成，并令 $E=(N\oplus P)/J$。证明映射 $y\mapsto(y,0)\bmod J$ 给出 $N$ 到 $E$ 的单射。证明映射 $N\oplus P\to M$ 在 $J$ 上为零，因而给出满同态 $E\to M\to0$。这样得到正合列 (\*)，即 $M$ 通过 $N$ 的扩张。因此，对 $\operatorname{Ext}^1(M,N)$ 的每个元素都对应了 $M$ 通过 $N$ 的扩张的一个同构类。证明所定义的映射，在扩张的同构类与 $\operatorname{Ext}^1(M,N)$ 的元素之间互为逆映射。］

> **译校注：** 本题的扩张同构采用固定两端的通常约定：它是正合列的同构，且在 $N$ 和 $M$ 上均为恒等。只有在这一等价关系下，同构类才由固定的 $\operatorname{Ext}^1(M,N)$ 分类。

**28.** 设 $R$ 是主理想整环，$a\in R$。对于每个 $R$-模 $N$，证明：

(a) $\operatorname{Ext}^1(R/aR,N)=N/aN$。

> **译校注：** (a) 还须假定 $a\ne0$。当 $a=0$ 时，左边是 $\operatorname{Ext}^1(R,N)=0$，右边却是 $N$，一般不相等。对于 $a\ne0$，自由解消 $0\to R\xrightarrow{a}R\to R/aR\to0$ 给出所述结果；下一问已经明确假定 $ab\ne0$。

(b) 对于 $b\in R$，有 $\operatorname{Ext}^1(R/aR,R/bR)=R/(a,b)$，其中 $(a,b)$ 是 $a$ 和 $b$ 的最大公因子，假定 $ab\ne0$。

### 复形的张量积

**29.** 设 $K=\bigoplus K_p$ 和 $L=\bigoplus L_q$ 是两个由整数编号的复形，边界映射使指标降低 $1$。定义 $K\otimes L$ 为模 $(K\otimes L)_n$ 的直和，其中

$$
(K\otimes L)_n=\bigoplus_{p+q=n}K_p\otimes L_q.
$$

证明存在唯一的同态

$$
d=d_n:(K\otimes L)_n\to(K\otimes L)_{n-1},
$$

使得

$$
d(x\otimes y)=d(x)\otimes y+(-1)^p x\otimes d(y).
$$

证明 $K\otimes L$ 连同这些同态构成复形，即 $d\circ d=0$。

**30.** 设 $K,L$ 是双复形，分别以 $K_{i\cdot}$ 和 $L_{i\cdot}$ 表示 $K$ 和 $L$ 的普通列复形。设 $\varphi:K\to L$ 是双复形的同态。假定每个同态

$$
\varphi_i:K_{i\cdot}\to L_{i\cdot}
$$

都是同调同构。

(a) 证明 $\operatorname{Tot}(\varphi):\operatorname{Tot}(K)\to\operatorname{Tot}(L)$ 是同调同构。（如果希望看到具体证明，参见 [FuL 85]，第 V 章，引理 5.4。）

(b) 用 (a) 代替谱序列证明定理 9.8。

<span class="original-page-anchor" id="pdf-page-841" aria-hidden="true"></span>

### 参考文献

[ArT 68] E. ARTIN 和 J. TATE，《类域论》（*Class Field Theory*），Benjamin，1968；Addison-Wesley，1991

[At 61] M. ATIYAH，《有限群的特征标与上同调》（Characters and cohomology of finite groups），*Pub. IHES* **9**（1961），第5–26页

[At 67] M. ATIYAH，《K-理论》（*K-theory*），Benjamin，1967；Addison-Wesley 重印，1991

[ABP 73] M. ATIYAH、R. BOTT 和 R. PATODI，《论热方程与指标定理》（On the heat equation and the index theorem），*Invent. Math.* **19**（1973），第279–330页

[Ba 68] H. BASS，《代数 K-理论》（*Algebraic K-theory*），Benjamin，1968

[Bo 69] R. BOTT，《$K(X)$ 讲义》（*Lectures on $K(X)$*），Benjamin，1969

[BtD 85] T. BROCKER 和 T. TOM DIECK，《紧李群的表示》（*Representations of Compact Lie Groups*），Springer Verlag，1985

[CaE 57] H. CARTAN 和 S. EILENBERG，《同调代数》（*Homological Algebra*），Princeton University Press，1957

[CuR 81] C. CURTIS 和 I. REINER，《表示论的方法》（*Methods of Representation Theory*），John Wiley & Sons，1981

[ES 52] S. EILENBERG 和 N. STEENROD，《代数拓扑基础》（*Foundations of Algebraic Topology*），Princeton University Press，1952

[FuL 85] W. FULTON 和 S. LANG，《黎曼–罗赫代数》（*Riemann-Roch algebra*），Springer Verlag，1985

[Go 58] R. GODEMENT，《层论》（*Théorie des faisceaux*），Hermann Paris，1958

[GreH 81] M. GREENBERG 和 J. HARPER，《代数拓扑：初级课程》（*Algebraic Topology: A First Course*），Benjamin-Addison-Wesley，1981

[GriH 78] P. GRIFFITHS 和 J. HARRIS，《代数几何原理》（*Principles of algebraic geometry*），Wiley Interscience，1978

[Gro 57] A. GROTHENDIECK，《论同调代数的若干问题》（Sur quelques points d’algèbre homologique），*Tohoku Math. J.* **9**（1957），第119–221页

[Gro 68] A. GROTHENDIECK，《离散群的陈类与线性表示》（*Classes de Chern et représentations linéaires des groupes discrets*），《概形的平展上同调十讲》（Dix exposés sur la cohomologie étale des schémas），North-Holland，Amsterdam，1968

[Gu 91] R. GUNNING，《多复变全纯函数导论》（*Introduction to holomorphic functions of several variables*），第 III 卷，Wadsworth & Brooks/Cole，1990

[Ha 77] R. HARTSHORNE，《代数几何》（*Algebraic Geometry*），Springer Verlag，1977

[HiS 70] P. J. HILTON 和 U. STAMMBACH，《同调代数教程》（*A Course in Homological Algebra*），Graduate Texts in Mathematics，Springer Verlag，1970。

[La 96] S. LANG，《群上同调专题》（*Topics in cohomology of groups*），Springer Lecture Notes，1996

[Man 69] J. MANIN，《代数几何中的 K-函子讲义》（*Lectures on the K-functor in Algebraic Geometry*），*Russian Math Surveys* **24**(5)（1969），第1–89页

[Mat 70] H. MATSUMURA，《交换代数》（*Commutative Algebra*），第二版，Benjamin-Cummings，1981

[No 68] D. NORTHCOTT，《环、模与重数讲义》（*Lessons on Rings, Modules and Multiplicities*），Cambridge University Press，1968

[No 76] D. NORTHCOTT，《有限自由解消》（*Finite Free Resolutions*），Cambridge University Press，1976

[Ro 79] J. ROTMAN，《同调代数导论》（*Introduction to Homological Algebra*），Academic Press，1979

[Se 64] J.-P. SERRE，《伽罗瓦上同调》（*Cohomologie Galoisienne*），Springer Lecture Notes **5**，1964

<span class="original-page-anchor" id="pdf-page-842" aria-hidden="true"></span>

[Se 65] J.-P. SERRE，《局部代数与重数》（*Algèbre locale, multiplicités*），Springer Lecture Notes **11**（1965），第三版，1975

[SGA 6] P. BERTHELOT、A. GROTHENDIECK、L. ILLUSIE 等，《相交理论与黎曼–罗赫定理》（*Théorie des intersections et théorème de Riemann-Roch*），Springer Lecture Notes 146，1970

[Sh 72] S. SHATZ，《副有限群、算术与几何》（*Profinite groups, arithmetic and geometry*），Ann. of Math Studies，Princeton University Press，1972
