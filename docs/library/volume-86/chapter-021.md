---
title: "第二十一章 有限自由解消"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第二十章 一般同调理论","link":"/library/volume-86/chapter-020"}
next: {"text":"附录一：e 与 π 的超越性","link":"/library/volume-86/appendix-01"}
---

# 第二十一章 有限自由解消

<span class="original-page-anchor" id="pdf-page-843" aria-hidden="true"></span>

本章汇集复形和同调的一些具体计算。其中一部分为第二十章的一般理论提供例子，另一部分给出一个世纪以来一直吸引代数学家研究的具体结果。它们有一个共同点：同调的计算借助有限自由解消（resolution）进行，即一个各模均为有限自由模的有限复形。

第一节介绍一种一般技巧（映射柱），可以用另一个有限自由复形来计算某个复形产生的同调。第十章已给出这类复形的一项应用，将命题4.5与其后的该章习题10–15结合起来。

接着讨论重要定理，从一个世纪前的希尔伯特合冲定理，到关于多项式环上模的有限自由解消的塞尔定理，以及奎伦—苏斯林定理。我们还讨论由科斯祖尔复形得到的某些有限自由解消。这些解消有多种应用，其中包括代数几何中的格罗滕迪克—黎曼—罗赫定理。

参考文献的引注均指第二十章末尾给出的书目。

## §1. 特殊复形

与前一章一样，我们研究环上模的范畴，但读者会注意到，这些论证在阿贝尔范畴中相当一般地成立。

在某些应用中，我们从一个复形确定同调，但该复形不适合其他类型的构造，例如更换基环。本节给出一个一般程序，构造另一个复形，其<span class="original-page-anchor" id="pdf-page-844" aria-hidden="true"></span>性质比原复形更好，同时给出相同的同调。关于诺特模的应用，见第十章习题12–15。

设 $f:K\to C$ 为复形态射。若自然映射

$$
H(f):H(K)\to H(C)
$$

为同构，则称 $f$ 为**同调同构**。这个定义适用于阿贝尔范畴，但读者可以把对象看作环上的模，甚至阿贝尔群。若给定对象 $E$，对象族 $\mathfrak F$ 中存在元素 $F$ 及满态射

$$
F\to E\to0,
$$

并且 $\mathfrak F$ 对有限直和封闭，则称 $\mathfrak F$ **充分**。例如，可以取自由模族作为 $\mathfrak F$。不过，在重要的应用中，我们研究有限生成模，这时可取有限自由模族作为 $\mathfrak F$。这些实际上就是我所考虑的应用，促使我将此情形公理化。

**命题1.1。** *设 $C$ 为复形，且仅当 $0\leqq p\leqq n$ 时 $H^p(C)$ 才可能非零。设 $\mathfrak F$ 为投射对象的充分族。存在复形*

$$
0\to K^0\to K^1\to\cdots\to K^n\to0,
$$

*满足：*

$$
\begin{gathered}
K^p\ne0\quad\text{仅可能在}\quad0\leqq p\leqq n\text{时成立};\\
p\geqq1\text{ 时，}K^p\in\mathfrak F;
\end{gathered}
$$

*并且存在复形同态*

$$
f:K\to C,
$$

*它是同调同构。*

*证明。* 对 $m$ 作降序归纳来定义 $f_m$：

$$
\begin{array}{ccccccccc}
\longrightarrow&K^m&\longrightarrow&K^{m+1}&\xrightarrow{\delta_K^{m+1}}&K^{m+2}&\longrightarrow\\
&\downarrow\scriptstyle f_m&&\downarrow\scriptstyle f_{m+1}&&\downarrow\scriptstyle f_{m+2}&\\
\longrightarrow&C^m&\longrightarrow&C^{m+1}&\xrightarrow{\delta_C^{m+1}}&C^{m+2}&\longrightarrow
\end{array}
$$

假设已经在 $p\geqq m+1$ 时定义了复形态射，使 $p\geqq m+2$ 时 $H^p(f)$ 为同构，并且

$$
f_{m+1}:Z^{m+1}(K)\to H^{m+1}(C)
$$

<span class="original-page-anchor" id="pdf-page-845" aria-hidden="true"></span>

为满态射，其中 $Z$ 表示闭链，即 $\operatorname{Ker}\delta$。我们要构造 $K^m$ 和 $f_m$，从而向左推进。先设 $m\geqq0$。设 $B^{m+1}$ 为映射

$$
\operatorname{Ker}\delta_K^{m+1}\to H^{m+1}(C)
$$

的核。

取 $K'\in\mathfrak F$，并有满态射

$$
\delta':K'\to B^{m+1}.
$$

设 $K''\to H^m(C)$ 为满态射，且 $K''\in\mathfrak F$，并令

$$
f'':K''\to Z^m(C)
$$

为任意一个提升；由于 $K''$ 投射，这样的提升存在。令

$$
K^m=K'\oplus K'',
$$

并定义 $\delta^m:K^m\to K^{m+1}$ 在 $K'$ 上为 $\delta'$，在 $K''$ 上为 $0$。于是

$$
f_{m+1}\circ\delta'(K')\subset\delta_C(C_m),
$$

因而存在 $f':K'\to C^m$，使

$$
\delta_C\circ f'=f_{m+1}\circ\delta'.
$$

现在定义 $f_m:K^m\to C^m$，在 $K'$ 上为 $f'$，在 $K''$ 上为 $f''$。这样就按要求定义了截断到次数 $m$ 的复形态射。

最后，若 $m=-1$，我们已经构造到 $K^0,\delta^0,f_0$，并且

$$
K^0\xrightarrow{f_0}H^0(C)\to0
$$

正合。定义 $K^{-1}=0$，最后一个方形如下：

![复形构造中的最后一个交换图](/library/volume-86/diagrams/pdf-0845-last-square.png)

将 $K^0$ 替换为 $K^0/(\operatorname{Ker}\delta^0\cap\operatorname{Ker}f_0)$。于是 $H^0(f)$ 成为同构，命题得证。

我们想进一步说明 $K^0$ 的性质。为此定义一个新概念。设 $\mathfrak F$ 为给定阿贝尔范畴中的对象族（初读时可考虑模）。若 $\mathfrak F$ 充分，并且对任何正合列

$$
0\to F'\to F\to F''\to0,
$$

只要 $F'',F\in\mathfrak F$，就有 $F'\in\mathfrak F$，则称 $\mathfrak F$ **完备**。

<span class="original-page-anchor" id="pdf-page-846" aria-hidden="true"></span>

**例。** 在第十六章定理3.4中，我们证明了诺特环上有限模范畴中的有限平坦模族是完备的。同样，环上模范畴中的平坦模族是完备的。仅有投射模或自由模还不够，因为命题中的 $K^0$ 未必自由，而我们希望它也属于这一对象族，具有特别好的性质。实际应用中，该族由平坦模或有限平坦模组成。参见第十章定理4.4和第十六章定理3.8。

**命题1.2。** *设 $f:K\to C$ 为复形态射，其中仅当 $p=1,\ldots,n$ 时，$K^p,H^p(C)$ 才可能非零。设 $\mathfrak F$ 为完备族，并假设对所有 $p$，$K^p,C^p$ 都在 $\mathfrak F$ 中，唯独 $K^0$ 可能例外。若 $f$ 为同调同构，则 $K^0$ 也在 $\mathfrak F$ 中。*

在证明之前，对任意复形态射 $f$ 定义一个新复形，称为其**映射柱**。令

$$
M^p=K^p\oplus C^{p-1},
$$

并以

$$
\delta_M(x,y)=(\delta x,fx-\delta y)
$$

定义 $\delta_M:M^p\to M^{p+1}$。

容易验证，$M$ 是复形，即 $\delta\circ\delta=0$。若 $C'$ 是将 $C$ 的次数平移一（并将 $\delta_C$ 的符号改变）得到的复形，即 $C'^p=C^{p-1}$，则得到复形的正合列

$$
0\to C'\to M\to K\to0,
$$

因而得到**映射柱的上同调正合列**

![映射柱的上同调正合列](/library/volume-86/diagrams/pdf-0846-mapping-cylinder-sequence.png)

从定义可见，上同调映射

$$
H^p(K)\to H^{p+1}(C')\approx H^p(C)
$$

正是由 $f:K\to C$ 诱导的映射。

现在回到命题1.2的假设，于是这些映射为同构。得到 $H(M)=0$。这蕴含序列

$$
0\to K^0\to M^1\to M^2\to\cdots\to M^{n+1}\to0
$$

正合。由假设，每个 $M^p$ 都在 $\mathfrak F$ 中。在每一步插入核和余核，结合完备族的定义运用归纳法，得出 $K^0\in\mathfrak F$，证明完毕。

<span class="original-page-anchor" id="pdf-page-847" aria-hidden="true"></span>

在下一个命题中，我们把这一情形公理化，使它适用于后面讨论的张量积，也适用于族 $\mathfrak F$ 由第十六章定义的平坦模组成的情形。不过，这里无需了解该章，因为公理化只使用函子与正合性的一般语言。

再次设 $\mathfrak F$ 为完备族，$T$ 为给定范畴上的协变加性函子。若对 $\mathfrak F$ 中给定的正合列

$$
0\to F'\to F\to F''\to0,
$$

序列

$$
0\to T(F')\to T(F)\to T(F'')\to0
$$

也正合，则称 $\mathfrak F$ **对 $T$ 正合**。

**命题1.3。** *设 $\mathfrak F$ 为对 $T$ 正合的完备族。设 $f:K\to C$ 为复形态射，对所有 $p$，$K^p,C^p$ 都属于 $\mathfrak F$，且除有限多个 $p$ 外，$K^p,H^p(C)$ 均为零。假设 $f$ 为同调同构。那么*

$$
T(f):T(K)\to T(C)
$$

*为同调同构。*

*证明。* 构造 $f$ 的映射柱 $M$。像命题1.2的证明中那样，得到 $H(M)=0$，故 $M$ 正合。从右端的零开始归纳。设 $Z^p$ 为 $M^p$ 中的闭链，利用短正合列

$$
0\to Z^p\to M^p\to Z^{p+1}\to0,
$$

结合完备族的定义，得出对所有 $p$ 都有 $Z^p\in\mathfrak F$。因此，应用 $T$ 后得到的短序列正合。而 $T(M)$ 是态射

$$
T(f):T(K)\to T(C)
$$

的映射柱，因此从映射柱的同调序列可见，该态射为同调同构。

**译校注：** 原书此处写“which is therefore an isomorphism”（因而为同构）。这里由映射柱的同调为零推出的是 $H(T(f))$ 为同构，即命题所述的“同调同构”；并不推出 $T(f)$ 在每个次数上都是同构。例如，取 $T$ 为恒等函子，零复形到任一非零无环复形的态射诱导同调同构，但不是复形同构。

证明完成。

## §2. 有限自由解消

本节第一部分发展一种比投射解消稍微微妙的情形中的解消概念，并为第二十章的讨论提供一个很好的例子。诺斯科特在[No 76]中指出，对标准证明作少量调整，也适用于非诺特环；这些环只在某些时候比诺特环稍难处理。

<span class="original-page-anchor" id="pdf-page-848" aria-hidden="true"></span>

*设 $A$ 为环。* 若存在有限自由模 $F$，使 $E\oplus F$ 有限自由，因而对某个正整数 $n$ 同构于 $A^{(n)}$，则称模 $E$ **稳定自由**。特别地，$E$ 是有限生成投射模。

若存在解消

$$
0\to E_n\to\cdots\to E_0\to M\to0,
$$

其中每个 $E_i$ 都有限自由，则称模 $M$ 有**有限自由解消**。

**定理2.1。** *设 $M$ 为投射模。那么 $M$ 稳定自由当且仅当 $M$ 有有限自由解消。*

*证明。* 若 $M$ 稳定自由，则显然 $M$ 有有限自由解消。反过来，假设存在上述记号下的解消。对 $n$ 归纳，证明 $M$ 稳定自由。$n=0$ 时断言显然成立。设 $n\geqq1$。仿照维数移位的方法，在每一步插入核和余核。令

$$
M_1=\operatorname{Ker}(E_0\to M),
$$

**译校注：** 原书印作“$M_1=\operatorname{Ker}(E_0\to P)$”。本定理及给定解消的末项均为 $M$，并未定义 $P$；紧接着的正合列也为 $0\to M_1\to E_0\to M\to0$，故此处应为 $E_0\to M$ 的核。

由此得到正合列

$$
0\to M_1\to E_0\to M\to0.
$$

由于 $M$ 投射，该序列分裂，且 $E_0\approx M\oplus M_1$。而 $M_1$ 有长度比 $M$ 的解消更小的有限自由解消，所以存在有限自由模 $F$，使 $M_1\oplus F$ 自由。由于 $E_0\oplus F$ 也自由，定理得证。

若解消

$$
0\to E_n\to\cdots\to E_0\to M\to0
$$

中的所有模 $E_i$ $(i=0,\ldots,n)$ 都稳定自由，则称该解消**稳定自由**。

**命题2.2。** *设 $M$ 为 $A$-模。那么 $M$ 有长度 $n\geqq1$ 的有限自由解消当且仅当 $M$ 有长度 $n$ 的稳定自由解消。*

*证明。* 一个方向显然成立，所以假设给定了上述记号下的稳定自由解消。设 $0\leqq i<n$ 为某个整数，取有限自由模 $F_i,F_{i+1}$，使 $E_i\oplus F_i$ 和 $E_{i+1}\oplus F_{i+1}$ 自由。令 $F=F_i\oplus F_{i+1}$。于是可以用显然的方式构造正合列

$$
0\to E_n\to\cdots\to E_{i+1}\oplus F\to E_i\oplus F\to\cdots\to E_0\to M\to0.
$$

这样就改变了解消中两个相邻的模，使其自由。归纳进行，可以先使 $E_0,E_1$ 自由，再使 $E_1,E_2$ 自由，如此继续，即可完成命题的证明。

<span class="original-page-anchor" id="pdf-page-849" aria-hidden="true"></span>

下一个引理旨在便于进行维数移位。

若存在有限自由模 $F_1,F_2$，使 $M_1\oplus F_1\approx M_2\oplus F_2$，则称两个模 $M_1,M_2$ **稳定同构**。

**引理2.3。** *设 $M_1$ 与 $M_2$ 稳定同构。设*

$$
\begin{gathered}
0\to N_1\to E_1\to M_1\to0\\
0\to N_2\to E_2\to M_2\to0
\end{gathered}
$$

*为正合列，其中 $M_1$ 与 $M_2$ 稳定同构，$E_1,E_2$ 稳定自由。那么 $N_1$ 与 $N_2$ 稳定同构。*

*证明。* 由定义，有同构 $M_1\oplus F_1\approx M_2\oplus F_2$。有正合列

$$
\begin{gathered}
0\to N_1\to E_1\oplus F_1\to M_1\oplus F_1\to0\\
0\to N_2\to E_2\oplus F_2\to M_2\oplus F_2\to0.
\end{gathered}
$$

由沙纽尔引理（见下文），得到

$$
N_1\oplus E_2\oplus F_2\approx N_2\oplus E_1\oplus F_1.
$$

由于 $E_1,E_2,F_1,F_2$ 稳定自由，可以在两边各加上有限自由模，使与 $N_1,N_2$ 相加的直和项成为自由模；必要时再加上一维自由模，可以保持同构。这就证明了 $N_1$ 与 $N_2$ 稳定同构。

还需处理**沙纽尔引理**：

**引理2.4。** *设*

$$
\begin{gathered}
0\to K\to P\to M\to0\\
0\to K'\to P'\to M\to0
\end{gathered}
$$

*为正合列，其中 $P,P'$ 投射。那么有同构*

$$
K\oplus P'\approx K'\oplus P.
$$

*证明。* 由于 $P$ 投射，存在同态 $P\to P'$，使下图右侧的方形交换。

$$
\begin{array}{ccccccccc}
0&\longrightarrow&K&\xrightarrow{i}&P&\longrightarrow&M&\longrightarrow&0\\
&&\downarrow\scriptstyle u&&\downarrow\scriptstyle w&&\downarrow\scriptstyle\mathrm{id}&&\\
0&\longrightarrow&K'&\xrightarrow{j}&P'&\longrightarrow&M&\longrightarrow&0
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-850" aria-hidden="true"></span>

于是可以找到同态 $K\to K'$，使左侧的方形交换。由此得到正合列

$$
0\to K\to P\oplus K'\to P'\to0,
$$

其映射为 $x\mapsto(ix,ux)$（$x\in K$）和 $(y,z)\mapsto wy-jz$。正合性的验证留给读者。由于 $P'$ 投射，该序列分裂，沙纽尔引理得证。这也完成了引理2.3的证明。

一个模的稳定自由解消的最小长度称为其**稳定自由维数**。构造有限模的稳定自由解消时，我们归纳进行。前面的引理使我们能够进行归纳，也使我们能在模具有有限稳定自由维数时终止构造。

**定理2.5。** *设模 $M$ 有长度为 $n$ 的稳定自由解消*

$$
0\to E_n\to\cdots\to E_0\to M\to0.
$$

*设*

$$
F_m\to\cdots\to F_0\to M\to0
$$

*为正合列，其中 $i=0,\ldots,m$ 时 $F_i$ 稳定自由。*

*(i) 若 $m<n-1$，则存在稳定自由的 $F_{m+1}$，使该正合列可以正合地延长为*

$$
F_{m+1}\to\cdots\to F_0\to M\to0.
$$

*(ii) 若 $m=n-1$，令 $F_n=\operatorname{Ker}(F_{n-1}\to F_{n-2})$。那么 $F_n$ 稳定自由，因而*

$$
0\to F_n\to F_{n-1}\to\cdots\to F_0\to M\to0
$$

*为稳定自由解消。*

**评述。** 若 $A$ 为诺特环，则(i)当然是显然的，甚至可以取 $F_{m+1}$ 有限自由。

*证明。* 在每个序列中插入核和余核，设

$$
\begin{aligned}
K_m&=\operatorname{Ker}(E_m\to E_{m-1})\quad\text{若 }m\ne0,\\
K_0&=\operatorname{Ker}(E_0\to M),
\end{aligned}
$$

并类似地定义 $K'_m$。由引理2.3，$K_m$ 与 $K'_m$ 稳定同构，设

$$
K_m\oplus F\approx K'_m\oplus F',
$$

其中 $F,F'$ 有限自由。

<span class="original-page-anchor" id="pdf-page-851" aria-hidden="true"></span>

若 $m<n-1$，则 $K_m$ 为 $E_{m+1}$ 的同态像；因此 $K_m\oplus F$ 与 $K'_m\oplus F'$ 都是 $E_{m+1}\oplus F$ 的同态像。所以 $K'_m$ 为稳定自由模 $E_{m+1}\oplus F$ 的同态像。令 $F_{m+1}=E_{m+1}\oplus F$，完成这种情形的证明。

若 $m=n-1$，则可取 $K_m=E_n$。因此 $K_m\oplus F$ 稳定自由，由证明第一部分的同构，$K'_m\oplus F'$ 也稳定自由。由此显然可得 $K'_m$ 稳定自由，而由定义，在此情形中 $K'_m=F_{m+1}$。定理得证。

**推论2.6。** *若 $0\to M_1\to E\to M\to0$ 正合，$M$ 的稳定自由维数 $\leqq n$，且 $E$ 稳定自由，则 $M_1$ 的稳定自由维数 $\leqq n-1$。*

**定理2.7。** *设*

$$
0\to M'\to M\to M''\to0
$$

*为正合列。若其中任意两个模有有限自由解消，则第三个也有。*

*证明。* 假设 $M',M$ 有有限自由解消。由于 $M$ 有限，$M''$ 也有限。用与第二十章引理3.8基本相同的构造，可以构造正合交换图，其中 $E',E,E''$ 稳定自由：

![定理2.7证明中的三个正合列](/library/volume-86/diagrams/pdf-0851-three-exact-sequences.png)

然后对 $M$ 的稳定自由维数归纳。可见，$M_1$ 的稳定自由维数 $\leqq n-1$（实际上为 $n-1$，但这无关紧要），而 $M'_1$ 的稳定自由维数有限。由归纳，归结到 $M$ 的稳定自由维数为 $0$ 的情形，即 $M$ 稳定自由。由假设，$M'$ 有有限自由解消，因此 $M''$ 也有有限自由解消，完成第一个断言的证明。

<span class="original-page-anchor" id="pdf-page-852" aria-hidden="true"></span>

其次，假设 $M',M''$ 有有限自由解消。那么 $M$ 有限。若 $M',M''$ 的稳定自由维数都为 $0$，则 $M',M''$ 投射，$M\approx M'\oplus M''$ 也稳定自由，证明完成。现在对它们的稳定自由维数的最大值 $n$ 归纳，并假设 $n\geqq1$。像前一种情形一样，可以构造正合交换图，其中 $E',E,E''$ 有限自由（细节留给读者）。但 $M'_1,M''_1$ 的稳定自由维数的最大值至多为 $n-1$，因此由归纳可得 $M_1$ 的稳定自由维数有限。第二种情形得证。

注意，第三个断言已在第二十章引理3.8中，在 $A$ 为诺特环时证明；当时取 $\mathfrak C$ 为有限模的阿贝尔范畴，取 $\mathcal C$ 为稳定自由模族。米切尔·斯托克斯向我指出，不作诺特假设，这个断言在一般情形中仍成立，可按如下方式证明。假设 $M,M''$ 有有限自由解消。先证明 $M'$ 有限生成。事实上，先假设 $M$ 有限自由。有两个正合列

$$
\begin{gathered}
0\to M'\to M\to M''\to0\\
0\to K''\to F''\to M''\to0,
\end{gathered}
$$

其中 $F''$ 有限自由，由 $M''$ 有有限自由解消的假设，$K''$ 有限生成。由沙纽尔引理可得 $M'$ 有限生成。若 $M$ 不自由，可以用拉回将 $M'$ 的有限生成性归结到 $M$ 自由的情形，这留给读者。

现在假设 $M''$ 的稳定自由维数为正。使用与前面各种情形相同的正合交换图，其中 $E',E,E''$ 有限自由。$M''_1$ 的稳定自由维数比 $M''$ 小一，由归纳即可完成。这完成了定理2.7的证明。

这也结束了关于有限自由解消的一般讨论。更多信息见诺斯科特关于这一主题的书。

现在进入本节第二部分，给出对多项式环的应用。

**定理2.8。** *设 $R$ 为交换诺特环。设 $x$ 为变量。若每个有限 $R$-模都有有限自由解消，则每个有限 $R[x]$-模都有有限自由解消。*

换言之，在有限 $R$-模范畴中，若每个对象的稳定自由维数都有限，则同样的性质适用于有限 $R[x]$-模范畴。在证明定理之前，先陈述我们所考虑的应用。

**定理2.9。**（塞尔）*若 $k$ 为域，$x_1,\ldots,x_r$ 为独立变量，则 $k[x_1,\ldots,x_r]$ 上的每个有限投射模都稳定自由，或等价地说，都有有限自由解消。*

<span class="original-page-anchor" id="pdf-page-853" aria-hidden="true"></span>

*证明。* 由归纳和定理2.8，得到 $k[x_1,\ldots,x_r]$ 上的每个有限模都具有有限稳定自由维数。（这里使用了定理2.1。）证明完成。

本节余下部分用于证明定理2.8。

设 $M$ 为有限 $R[x]$-模。由第十章推论2.8，$M$ 有有限滤列

$$
M=M_0\supset M_1\supset\cdots\supset M_n=0,
$$

使每个商 $M_i/M_{i+1}$ 对某个素理想 $P_i$ 同构于 $R[x]/P_i$。由定理2.7，只需在 $M=R[x]/P$、$P$ 为素理想的情形中证明定理，现在就作此假设。由正合列

$$
0\to P\to R[x]\to R[x]/P\to0
$$

和定理2.7可知，$M$ 有有限自由解消当且仅当 $P$ 有。

令 $\mathfrak p=P\cap R$。那么 $\mathfrak p$ 为 $R$ 的素理想。假设存在某个 $M=R[x]/P$，没有有限自由解消。在所有这样的 $M$ 中，选择一个，使交 $\mathfrak p$ 在上述得到的素理想族中极大。由刻画诺特环的一项基本性质，这样的选择是可能的。

令 $R_0=R/\mathfrak p$，则 $R_0$ 为整环。令 $P_0=P/\mathfrak pR[x]$。于是可将 $M$ 看作 $R_0[x]$-模，等于 $R_0[x]/P_0$。

**译校注：** 原书写作“equal to $R_0/P_0$”。这里 $P_0=P/\mathfrak pR[x]$ 是 $R[x]/\mathfrak pR[x]=R_0[x]$ 的理想，而所讨论的是 $M=R[x]/P$；由商环的同构定理，$M=R_0[x]/P_0$，故原式漏去 $[x]$。

设 $f_1,\ldots,f_n$ 为 $P_0$ 的一组有限生成元，设 $f$ 为 $P_0$ 中次数最小的多项式。设 $K_0$ 为 $R_0$ 的分式域。用欧几里得算法，可写

$$
f_i=q_if+r_i\quad(i=1,\ldots,n),
$$

其中 $q_i,r_i\in K_0[x]$，且 $\deg r_i<\deg f$。设 $d_0$ 为所有 $q_i,r_i$ 的系数的公分母。那么 $d_0\ne0$，且

$$
d_0f_i=q'_if+r'_i,
$$

其中 $q'_i=d_0q_i$ 和 $r'_i=d_0r_i$ 属于 $R_0[x]$。由于 $\deg f$ 在 $P_0$ 中最小，对所有 $i$ 都有 $r'_i=0$，所以

$$
d_0P_0\subset R_0[x]f=(f).
$$

令 $N_0=P_0/(f)$，则 $N_0$ 为 $R_0[x]$ 上的模，也可将 $N_0$ 看作 $R[x]$ 上的模；这样看待时，记作 $N$。取任意 $d\in R$，使其模 $\mathfrak p$ 约化为 $d_0$。由于 $d_0\ne0$，有 $d\notin\mathfrak p$。模 $N_0$ 有有限滤列，其每个商模同构于某个 $R_0[x]/Q_0$，其中 $Q_0$ 为 $N_0$ 的相伴素理想。设 $Q$ 为 $Q_0$ 在 $R[x]$ 中的原像。这些素理想 $Q$ 恰为 $N$ 在 $R[x]$ 中的相伴素理想。由于 $d_0$ 消去 $N_0$，$d$ 消去 $N$，因此 $d$ 属于 $N$ 的每个相伴素理想。由选择 $P$ 时的极大性，<span class="original-page-anchor" id="pdf-page-854" aria-hidden="true"></span>得到 $N$ 的滤列中的每个商模都有有限自由解消，再由定理2.7，$N$ 本身也有有限自由解消。

现在通过典范同态

$$
R[x]\to R_0[x]=R[x]/\mathfrak pR[x]
$$

将 $R_0[x]$ 看作 $R[x]$-模。

**由假设，$\mathfrak p$ 作为 $R$-模有有限自由解消，设为**

$$
0\to E_n\to\cdots\to E_0\to\mathfrak p\to0.
$$

可以按显然的含义构造模 $E_i[x]$，得到 $\mathfrak p[x]=\mathfrak pR[x]$ 的有限自由解消。由正合列

$$
0\to\mathfrak pR[x]\to R[x]\to R_0[x]\to0,
$$

得到 $R_0[x]$ 作为 $R[x]$-模有有限自由解消。

由于 $R_0$ 为整环，$R_0[x]$ 中的主理想 $(f)$ 与 $R_0[x]$ 作为 $R[x]$-模同构，因此作为 $R[x]$-模有有限自由解消。将定理2.7应用于 $R[x]$-模的正合列

$$
0\to(f)\to P_0\to N\to0,
$$

得到 $P_0$ 有有限自由解消；再应用于正合列

$$
0\to\mathfrak pR[x]\to P\to P_0\to0,
$$

得到 $P$ 有有限自由解消，定理2.8得证。

## §3. 幺模多项式向量

设 $A$ 为交换环。设 $(f_1,\ldots,f_n)$ 为生成单位理想的 $A$ 中元素。称这些元素为**幺模的**。若存在 $GL_n(A)$ 中的矩阵，其第一列为 ${}^t(f_1,\ldots,f_n)$，则称它们具有**幺模延拓性质**。若 $A$ 为主理想整环，则证明这一性质总成立是一个简单练习。塞尔最初提出问题：对于域 $k$ 上的多项式环 $k[x_1,\ldots,x_r]$，这是否成立？奎伦和苏斯林解决了这一问题。这里给出瓦瑟斯坦对苏斯林证明的简化，也使用霍罗克斯先前的一个结果。这个方法以某种方式对变量个数进行归纳。

用 $f={}^t(f_1,\ldots,f_n)$ 表示列向量。先注意到，$f$ 具有幺模延拓性质当且仅当将其分量置换后得到的向量具有此性质。同样，我们可以进行<span class="original-page-anchor" id="pdf-page-855" aria-hidden="true"></span>使用通常的行变换，即将倍数 $gf_i$ 加到 $f_j$ 上（$j\ne i$），而 $f$ 具有幺模延拓性质当且仅当它经行变换得到的任意一个向量具有此性质。

先在允许归纳的背景下证明定理。

**定理3.1。**（霍罗克斯）*设 $(\mathfrak o,\mathfrak m)$ 为局部环，$A=\mathfrak o[x]$ 为 $\mathfrak o$ 上的一元多项式环。设 $f$ 为 $A^{(n)}$ 中的幺模向量，且某个分量的首项系数为 $1$。那么 $f$ 具有幺模延拓性质。*

*证明。*（苏斯林）若 $n=1$ 或 $2$，则即使不假设 $\mathfrak o$ 局部，定理也显然成立。所以假设 $n\geqq3$，对 $f$ 的首项系数为 $1$ 的分量中的最小次数 $d$ 归纳。先注意到，利用欧几里得算法和行变换，可以假设 $f_1$ 的首项系数为 $1$、次数为 $d$，且 $j\ne1$ 时 $\deg f_i<d$。由于 $f$ 幺模，关系式 $\sum g_if_i=1$ 表明，$f_2,\ldots,f_n$ 的系数不可能全在极大理想 $\mathfrak m$ 中。不失一般性，可以假设 $f_2$ 的某个系数不在 $\mathfrak m$ 中，因 $\mathfrak o$ 局部，该系数为可逆元。写

$$
\begin{aligned}
f_1(x)&=x^d+a_{d-1}x^{d-1}+\cdots+a_0,\quad a_i\in\mathfrak o,\\
f_2(x)&=b_sx^s+\cdots+b_0,\quad b_i\in\mathfrak o,\ s\leqq d-1,
\end{aligned}
$$

其中某个 $b_i$ 为可逆元。设 $\mathfrak a$ 为由所有次数 $\leqq d-1$ 的多项式 $g_1f_1+g_2f_2$ 的首项系数生成的理想。那么 $\mathfrak a$ 包含所有系数 $b_i$，$i=0,\ldots,s$。对此可作降序归纳：从显然的 $b_s$ 开始，再使用线性组合

$$
x^{d-s}f_2(x)-b_sf_1(x).
$$

因此 $\mathfrak a$ 为单位理想，并存在次数 $\leqq d-1$、首项系数为 $1$ 的多项式 $g_1f_1+g_2f_2$。通过行变换，现在可在某个 $i\ne1,2$ 的第 $i$ 个位置得到次数 $\leqq d-1$、首项系数为 $1$ 的分量。因此，最终通过归纳，可以假设 $d=0$，此时定理显然成立。证明完成。

在任意交换环 $A$ 上，对于两个列向量 $f,g$，写 $f\sim g$ 于 $A$ 上，表示存在 $M\in GL_n(A)$，使

$$
f=Mg,
$$

并称 $f$ **在 $A$ 上与 $g$ 等价**。霍罗克斯定理说明，若幺模向量 $f$ 的某个分量的首项系数为 $1$，则它在 $\mathfrak o[x]$ 上与第一个单位向量 $e^1$ 等价。我们希望在非局部环上得到类似的下降。可以写 $f=f(x)$，其常数系数自然组成一个“常向量”$f(0)$。由霍罗克斯定理，得到以下推论：

<span class="original-page-anchor" id="pdf-page-856" aria-hidden="true"></span>

**推论3.2。** *设 $\mathfrak o$ 为局部环。设 $f$ 为 $\mathfrak o[x]^{(n)}$ 中的幺模向量，且某个分量的首项系数为 $1$。那么在 $\mathfrak o[x]$ 上 $f\sim f(0)$。*

*证明。* 注意，$f(0)\in\mathfrak o^{(n)}$ 有一个分量为可逆元。只需证明：在任意交换环 $R$ 上，任何有可逆分量的元素 $c\in R^{(n)}$ 都在 $R$ 上与 $e^1$ 等价；这一点显然成立。

**引理3.3。** *设 $R$ 为整环，$S$ 为乘法子集。设 $x,y$ 为独立变量。若在 $S^{-1}R[x]$ 上 $f(x)\sim f(0)$，则存在 $c\in S$，使在 $R[x,y]$ 上 $f(x+cy)\sim f(x)$。*

*证明。* 取 $M\in GL_n(S^{-1}R[x])$，使 $f(x)=M(x)f(0)$。那么 $M(x)^{-1}f(x)=f(0)$ 为常向量，因而在平移 $x\mapsto x+y$ 下不变。令

$$
G(x,y)=M(x)M(x+y)^{-1}.
$$

那么 $G(x,y)f(x+y)=f(x)$。有 $G(x,0)=I$，故

$$
G(x,y)=I+yH(x,y),
$$

其中 $H(x,y)\in S^{-1}R[x,y]$。存在 $c\in S$，使 $cH$ 的系数在 $R$ 中。于是 $G(x,cy)$ 的系数在 $R$ 中。由于 $\det M(x)$ 是 $S^{-1}R$ 中的常数，$\det M(x+cy)$ 等于同一常数，因此 $\det G(x,cy)=1$。引理得证。

**定理3.4。** *设 $R$ 为整环，$f$ 为 $R[x]^{(n)}$ 中的幺模向量，且某个分量的首项系数为 $1$。那么在 $R[x]$ 上 $f(x)\sim f(0)$。*

*证明。* 设 $J$ 为所有使 $f(x+cy)$ 在 $R[x,y]$ 上与 $f(x)$ 等价的元素 $c\in R$ 的集合。那么 $J$ 是理想，因为若 $c\in J$、$a\in R$，则在等价定义中将 $y$ 换成 $ay$，可见 $f(x+cay)$ 在 $R[x,ay]$ 上与 $f(x)$ 等价，因而在 $R[x,y]$ 上等价。同样容易看出，若 $c,c'\in J$，则 $c+c'\in J$。现在设 $\mathfrak p$ 为 $R$ 的素理想。由推论3.2，$f(x)$ 在 $R_{\mathfrak p}[x]$ 上与 $f(0)$ 等价；再由引理3.3，存在 $c\in R$、$c\notin\mathfrak p$，使 $f(x+cy)$ 在 $R[x,y]$ 上与 $f(x)$ 等价。因此 $J$ 不包含在 $\mathfrak p$ 中，所以 $J$ 为 $R$ 中的单位理想，故存在 $R[x,y]$ 上的可逆矩阵 $M(x,y)$，使

$$
f(x+y)=M(x,y)f(x).
$$

由于可逆矩阵的同态像可逆，在这个关系式中将 $x$ 替换为 $0$，即可完成定理的证明。

**定理3.5。**（奎伦—苏斯林）*设 $k$ 为域，$f$ 为 $k[x_1,\ldots,x_r]^{(n)}$ 中的幺模向量。那么 $f$ 具有幺模延拓性质。*

<span class="original-page-anchor" id="pdf-page-857" aria-hidden="true"></span>

*证明。* 对 $r$ 归纳。若 $r=1$，则 $k[x_1]$ 为主理想整环，定理的证明留给读者。设 $r\geqq2$，假设定理对 $r-1$ 个变量成立，令

$$
R=k[x_1,\ldots,x_{r-1}].
$$

把 $f$ 看作最后一个变量 $x_r$ 的多项式向量，并希望应用定理3.4。若 $f$ 的某个分量关于变量 $x_r$ 的首项系数为 $1$，便可如此。按下面的方法将定理归结到这种情形。诺特正规化定理（第八章定理2.1）的证明表明，若令

$$
\begin{aligned}
y_r&=x_r,\\
y_i&=x_i-x_r^{m_i},
\end{aligned}
$$

则多项式向量

$$
f(x_1,\ldots,x_r)=g(y_1,\ldots,y_r)
$$

有一个分量的 $y_r$-首项系数等于 $1$。因此存在在 $R[x_r]=R[y_r]$ 上可逆的矩阵 $N(y)=M(x)$，使

$$
g(y_1,\ldots,y_r)=N(y_1,\ldots,y_r)g(y_1,\ldots,y_{r-1},0),
$$

且 $g(y_1,\ldots,y_{r-1},0)$ 在 $k[y_1,\ldots,y_{r-1}]^{(n)}$ 中幺模。因此可以用归纳法完成证明。

现在给出定理的其他表述。先回顾：若存在有限自由模 $F$，使 $E\oplus F$ 有限自由，则称交换环 $A$ 上的模 $E$ **稳定自由**。

若对于所有正整数 $n$，每个幺模向量 $f\in A^{(n)}$ 都具有幺模延拓性质，则称交换环 $A$ 具有**幺模列延拓性质**。

**定理3.6。** *设 $A$ 为具有幺模列延拓性质的交换环。那么 $A$ 上的每个稳定自由模都自由。*

*证明。* 设 $E$ 稳定自由。对使 $E\oplus F$ 自由的自由模 $F$ 的秩归纳。由归纳，只需证明：若 $E\oplus A$ 自由，则 $E$ 自由。设 $E\oplus A=A^{(n)}$，令

$$
p:A^{(n)}\to A
$$

为投影。设 $u^1$ 为 $A$ 在自身上的一组基。把 $A$ 看作 $E\oplus A=A^{(n)}$ 中的直和项，写

$$
u^1={}^t(a_{11},\ldots,a_{n1}),\quad a_{i1}\in A.
$$

<span class="original-page-anchor" id="pdf-page-858" aria-hidden="true"></span>

那么 $u^1$ 幺模，由假设，$u^1$ 是某个矩阵 $M=(a_{ij})$ 的第一列，其行列式为 $A$ 中的可逆元。令

$$
u^j=Me^j\quad(j=1,\ldots,n),
$$

其中 $e^j$ 为 $A^{(n)}$ 的第 $j$ 个单位列向量。注意，$u^1$ 是 $M$ 的第一列。通过初等列变换，可以改变 $M$，使 $j=2,\ldots,n$ 时 $u^j\in E$。事实上，若 $j\geqq2$ 时 $pe^j=cu^1$，只需将 $e^j$ 替换为 $e^j-ce^1$。因此不失一般性，可假设 $u^2,\ldots,u^n$ 属于 $E$。

**译校注：** 原书在这里印作“$pe^j=cu^1$”并写“将 $e^j$ 替换为 $e^j-ce^1$”。按上一页的定义，$p$ 是 $E\oplus A$ 到 $A$ 的投影，矩阵 $M$ 的列是 $u^j=Me^j$。列变换的准确计算是：选择 $c\in A$ 使 $p(u^j)=c\,p(u^1)$，再把第 $j$ 列 $u^j$ 换成 $u^j-cu^1$，便有 $p(u^j-cu^1)=0$，因而该列属于 $E$。在列的原像上，这等价于把 $e^j$ 换成 $e^j-ce^1$；在这个写法中，对原像使用的投影应为 $p\circ M$。

由于 $M$ 在 $A$ 上可逆，它通过

$$
X\mapsto MX
$$

诱导 $A^{(n)}$ 作为 $A$-模到自身的自同构。

由构造和 $A^{(n)}=E\oplus A$，立即可见，$M$ 将以 $\{e^2,\ldots,e^n\}$ 为基的自由模映到整个 $E$。证明完成。

现在把塞尔定理2.9与上述由奎伦—苏斯林定理和定理3.6组成的方法结合起来，得到奎伦—苏斯林定理的另一种表述：

**定理3.7。** *设 $k$ 为域。那么多项式环 $k[x_1,\ldots,x_r]$ 上的每个有限投射模都自由。*

## §4. 科斯祖尔复形

本节描述一个由自由模的外积构造的有限复形。这给出了外积的一项应用，也给出代数几何中使用的基本构造，既用于抽象代数几何，也用于复代数几何。读者可查阅格里菲思—哈里斯[GrH 78]第五章第3节；格罗滕迪克的[SGA 6]；哈茨霍恩[Ha 77]第三章第7节；以及富尔顿—朗[FuL 85]第四章第2节来验证。

由第二十章可知，模的自由解消使我们能计算某个函子的同调或上同调群。现在将它应用于 Hom 和张量积。因此，通过科斯祖尔复形，也得到同调的显式计算的例子，说明第二十章的理论。我们还将导出所谓的希尔伯特合冲定理，得到一个经典应用。

设 $A$ 为环（始终假设交换），$M$ 为模。称 $A$ 中的元素序列 $x_1,\ldots,x_r$ 为 **$M$-正则序列**，如果 $M/(x_1,\ldots,x_r)M\ne0$，且 $x_1$<span class="original-page-anchor" id="pdf-page-859" aria-hidden="true"></span>在 $M$ 中不是零因子，并且 $i\geqq2$ 时，$x_i$ 在

$$
M/(x_1,\ldots,x_{i-1})M
$$

中不是零因子。

当 $M=A$ 时，称其为**正则序列**。

**命题4.1。** *设 $I=(x_1,\ldots,x_r)$ 由 $A$ 中的正则序列生成。那么 $I/I^2$ 为 $A/I$ 上维数 $r$ 的自由模。*

*证明。* 设 $\bar x_i$ 为 $x_i$ 模 $I^2$ 的类。只需证明 $\bar x_1,\ldots,\bar x_r$ 线性无关。对 $r$ 归纳。$r=1$ 时，若 $\bar a\bar x=0$，则对某个 $b\in A$，有 $ax=bx^2$，故 $x(a-bx)=0$。由于 $x$ 在 $A$ 中不是零因子，有 $a=bx$，所以 $\bar a=0$。

现在假设命题对正则序列 $x_1,\ldots,x_{r-1}$ 成立。假设

$$
\sum_{i=1}^r\bar a_i\bar x_i=0\quad\text{于}\quad I/I^2.
$$

可以假设在 $A$ 中 $\sum a_ix_i=0$；否则 $\sum a_ix_i=\sum y_ix_i$，其中 $y_i\in I$，可把 $a_i$ 换成 $a_i-y_i$，而不改变 $\bar a_i$。

由于 $x_r$ 在 $A/(x_1,\ldots,x_{r-1})$ 中不是零因子，存在 $b_i\in A$，使

$$
a_rx_r+\sum_{i=1}^{r-1}a_ix_i=0\Rightarrow a_r=\sum_{i=1}^{r-1}b_ix_i\Rightarrow\sum_{i=1}^{r-1}(a_i+b_ix_r)x_i=0.
$$

由归纳假设，

$$
a_j+b_jx_r\in\sum_{i=1}^{r-1}Ax_i\qquad(j=1,\ldots,r-1),
$$

因此对所有 $j$ 都有 $a_j\in I$，从而 $\bar a_j=0$，命题得证。

设 $K,L$ 为复形，写成直和

$$
K=\bigoplus K_p\quad\text{和}\quad L=\bigoplus L_q,
$$

其中 $p,q\in\mathbf Z$。通常，当 $p,q<0$ 时，$K_p=L_q=0$。那么**张量积** $K\otimes L$ 是满足

$$
(K\otimes L)_n=\bigoplus_{p+q=n}K_p\otimes L_q
$$

的复形；对 $u\in K_p,v\in L_q$，微分定义为

$$
d(u\otimes v)=du\otimes v+(-1)^pu\otimes dv.
$$

（请详细验证这确实给出一个复形；这是常规核查。）

<span class="original-page-anchor" id="pdf-page-860" aria-hidden="true"></span>

设 $A$ 为交换环，$x\in A$。定义复形 $K(x)$，使 $K_0(x)=A$、$K_1(x)=Ae_1$，其中 $e_1$ 为符号，$Ae_1$ 为以 $\{e_1\}$ 为基的秩 $1$ 自由模，边缘映射由 $de_1=x$ 定义。因此复形可以表示为序列

$$
\begin{array}{ccccccccc}
0&\longrightarrow&Ae_1&\xrightarrow{d}&A&\longrightarrow&0\\
&&\Vert&&\Vert&&\\
0&\longrightarrow&K_1(x)&\longrightarrow&K_0(x)&\longrightarrow&0
\end{array}
$$

更一般地，对元素 $x_1,\ldots,x_r\in A$，如下定义**科斯祖尔复形** $K(x)=K(x_1,\ldots,x_r)$。令：

$K_0(x)=A$；

$K_1(x)=$ 以 $\{e_1,\ldots,e_r\}$ 为基的自由模 $E$；

$K_p(x)=$ 以 $\{e_{i_1}\wedge\cdots\wedge e_{i_p}\}$ 为基的自由模 $\bigwedge^pE$，其中 $i_1<\cdots<i_p$；

$K_r(x)=$ 以 $e_1\wedge\cdots\wedge e_r$ 为基的秩 $1$ 自由模 $\bigwedge^rE$。

以 $de_i=x_i$ 定义**边缘映射**，一般地，用

$$
d(e_{i_1}\wedge\cdots\wedge e_{i_p})=\sum_{j=1}^p(-1)^{j-1}x_{i_j}e_{i_1}\wedge\cdots\wedge\widehat e_{i_j}\wedge\cdots\wedge e_{i_p}
$$

定义

$$
d:K_p(x)\to K_{p-1}(x).
$$

直接验证可得 $d^2=0$，因此有复形

$$
0\to K_r(x)\to\cdots\to K_p(x)\to\cdots\to K_1(x)\to A\to0.
$$

下一个引理说明该复形在多大程度上与由 $(x)$ 生成的理想 $I=(x_1,\ldots,x_r)$ 无关。设

$$
I=(x_1,\ldots,x_r)\supset I'=(y_1,\ldots,y_r)
$$

为 $A$ 的两个理想。有自然环同态

$$
\operatorname{can}:A/I'\to A/I.
$$

设 $\{e'_1,\ldots,e'_r\}$ 为 $K_1(y)$ 的一组基，令

$$
y_i=\sum c_{ij}x_j,\quad c_{ij}\in A.
$$

以

$$
f_1e'_i=\sum c_{ij}e_j
$$

定义 $f_1:K_1(y)\to K_1(x)$。

<span class="original-page-anchor" id="pdf-page-861" aria-hidden="true"></span>

以及

$$
f_p=f_1\wedge\cdots\wedge f_1,\qquad\text{此乘积含 }p\text{ 个因子}.
$$

令 $D=\det(c_{ij})$ 为该行列式。则在 $p=r$ 时，

$$
f_r:K_r(y)\to K_r(x)\text{ 是乘以 }D\text{ 的映射}.
$$

**引理4.2。** *采用上述记号，同态 $f_p$ 定义一个科斯祖尔复形的态射：*

![科斯祖尔复形的态射；竖直映射依次为 fr = D、fp、f1、恒等映射和典范映射。](/library/volume-86/diagrams/pdf-0861-koszul-morphism.png)

*如果 $D$ 是 $A$ 中的可逆元，则这些同态定义一个同构；例如，当 $(y)$ 是 $(x)$ 的一个排列时便是如此。*

*证明。* 根据定义，

$$
f(e'_{i_1}\wedge\cdots\wedge e'_{i_p})=\left(\sum_{j=1}^r c_{i_1j}e_j\right)\wedge\cdots\wedge\left(\sum_{j=1}^r c_{i_pj}e_j\right).
$$

于是

![原书完整的 fd = df 计算；帽号与 omitted 均表示略去第 k 个外积因子。](/library/volume-86/diagrams/pdf-0861-koszul-calculation.png)

**译校注：** 原图倒数第二行把包含 $\sum_j c_{i_kj}x_je_j$ 的整个第 $k$ 个外积因子标为“omitted”（略去），同时不再在外面写标量 $y_{i_k}$。若按字面删去整个因子，这一行便少了该标量：例如 $r=p=1$、$c_{11}=1$、$x_1=2$ 时，$fd(e'_1)=2$，而删去唯一因子后的空外积为 $1$。所以略去第 $k$ 个外积因子之后，仍应在其余因子的外积前保留标量 $y_{i_k}=\sum_j c_{i_kj}x_j$；这也与上一行及最终的 $df$ 相符。原图在此完整保留。

这里使用了 $y_{i_k}=\sum c_{i_kj}x_j$。这就证明了 $f_p$ 定义一个复形同态。

特别地，如果 $(x)$ 和 $(y)$ 生成同一理想，而且行列式 $D$ 是可逆元（即从 $(x)$ 到 $(y)$ 的线性变换在该环上可逆），那么这两个科斯祖尔复形同构。

<span class="original-page-anchor" id="pdf-page-862" aria-hidden="true"></span>

下面的引理提供了一种有用的方法，供后面进行归纳之用。

**命题4.3。** *存在自然同构*

$$
K(x_1,\ldots,x_r)\approx K(x_1)\otimes\cdots\otimes K(x_r).
$$

*证明。* 证明留作练习。

令 $I=(x_1,\ldots,x_r)$ 为由 $x_1,\ldots,x_r$ 生成的理想。直接由定义便可看出，科斯祖尔复形的第 $0$ 个同调就是 $A/IA$。

更一般地，设 $M$ 为 $A$-模。定义 **$M$ 的科斯祖尔复形**为

$$
K(x;M)=K(x_1,\ldots,x_r;M)=K(x_1,\ldots,x_r)\otimes_A M.
$$

于是这个复形具有如下形式：

$$
0\to K_r(x)\otimes M\to\cdots\to K_2(x)\otimes_A M\to M^{(r)}\to M\to0.
$$

有时我们将 $H_pK(x;M)$ 简记为 $H_p(x;M)$。首尾两个同调群可直接由边缘映射的定义求出。得到

$$
H_0(K(x;M))\approx M/IM;
$$

$$
H_r(K(x);M)=\{v\in M\mid\text{对所有 }i=1,\ldots,r,\ x_iv=0\}.
$$

根据命题4.3，我们一般地研究任意复形与 $K(x)$ 的张量积在 $x$ 仅包含一个元素时会发生什么。设 $y\in A$，并设 $C$ 为任意 $A$-模复形。有如下复形的正合列：

$$
\tag{1}0\to C\to C\otimes K(y)\to(C\otimes K(y))/C\to0,
$$

其具体形式如下。

![复形短正合列的三行具体形式，含全部张量直和项；右侧竖直映射为 dn 张量恒等映射及 dn−1 张量恒等映射。](/library/volume-86/diagrams/pdf-0862-koszul-short-exact.png)

<span class="original-page-anchor" id="pdf-page-863" aria-hidden="true"></span>

注意，$C\otimes K_1(y)$ 就是将 $C$ 的次数平移一位所得的复形，换句话说，

$$
\tag{2}(C\otimes K_1(y))_{n+1}=C_n\otimes K_1(y).
$$

特别地，

$$
\tag{3}H_{n+1}(C\otimes K(y)/C)\approx H_n(C).
$$

复形的正合列有相应的同调序列，在这里给出如下长正合列：

![原书的同调长正合列，以及商复形同调与 Hn(C) 的同构。](/library/volume-86/diagrams/pdf-0863-long-homology-sequence.png)

**译校注：** 图中第二项原印为 $H_{n+1}(C\otimes K_1(y))$；按上一页的短正合列(1)，该项应是 $H_{n+1}(C\otimes K(y))$，即完整张量复形的同调，而不是仅取次数为1的项。下文(4)也使用 $K(y)$。原图保留原印记号。

按指标将这个序列上下排列，写成：

$$
\tag{4}\begin{aligned}
&\to H_{p+1}(C)\to H_{p+1}(C)\to H_{p+1}(C\otimes K(y))\to\\
&\to H_p(C)\to H_p(C)\to H_p(C\otimes K(y))\to
\end{aligned}
$$

其最低次数的末尾为

$$
\tag{5}\to H_1(C)\to H_1(C\otimes K(y))\to H_0(C)\to H_0(C).
$$

此外，直接应用边缘映射以及复形张量积的定义，得到：

*在 $H_p(C)$ 上的边缘映射（$p\geq0$）由乘以 $(-1)^py$ 的映射诱导：*

$$
\tag{6}\partial=(-1)^pm(y):H_p(C)\to H_p(C).
$$

事实上，写成

$$
(C\otimes K(y))_p=(C_p\otimes A)\oplus(C_{p-1}\otimes K_1(y))\approx C_p\oplus C_{p-1}.
$$

取 $(v,w)\in C_p\oplus C_{p-1}$，其中 $v\in C_p$、$w\in C_{p-1}$。直接由定义有

$$
\tag{7}d(v,w)=(dv+(-1)^{p-1}yw,dw).
$$

要得到(6)，只需遵循边缘映射的定义：取元素 $w\in C_p\approx C_p\otimes K_1(y)$，将其提升为 $(0,w)$，作用以 $d$，再提升回 $C_p$。如果最初取的是闭链，即 $dw=0$，那么所得映射在同调类上良定义，并取值于同调。

**引理4.4。** *设 $y\in A$，且 $C$ 为上述复形。那么对于所有 $p\geq0$，$m(y)$ 都零化 $H_p(C\otimes K(y))$。*

*证明。* 如果 $(v,w)$ 为闭链，即 $d(v,w)=0$，由(7)立刻得到 $(yv,yw)=d(0,(-1)^pv)$，引理得证。

<span class="original-page-anchor" id="pdf-page-864" aria-hidden="true"></span>

在我们所考虑的应用中，令 $y=x_r$，并令

$$
C=K(x_1,\ldots,x_{r-1};M)=K(x_1,\ldots,x_{r-1})\otimes M.
$$

于是得到：

**定理4.5。** (a) *存在如下正合列，其中的映射如上：*

$$
\begin{aligned}
&\to H_pK(x_1,\ldots,x_{r-1};M)\to H_pK(x_1,\ldots,x_{r-1};M)\to H_pK(x_1,\ldots,x_r;M)\\
&\cdots\to H_1(x_1,\ldots,x_r;M)\to H_0(x_1,\ldots,x_{r-1};M)\xrightarrow{m(x_r)}H_0(x_1,\ldots,x_{r-1};M).
\end{aligned}
$$

(b) *理想 $I=(x_1,\ldots,x_r)$ 的每个元素都零化 $H_p(x;M)$（$p\geq0$）。*

(c) *若 $I=A$，则对于所有 $p\geq0$，都有 $H_p(x;M)=0$。*

*证明。* 这直接由命题4.3和引理4.4得到。

定义**增广科斯祖尔复形**为

$$
0\to K_r(x;M)\to\cdots\to K_1(x;M)=M^{(r)}\to M\to M/IM\to0.
$$

**定理4.6。** *设 $M$ 为 $A$-模。*

(a) *设 $x_1,\ldots,x_r$ 为 $M$ 的正则序列。则当 $p>0$ 时，$H_pK(x;M)=0$。（当然，$H_0K(x;M)=M/IM$。）换句话说，增广科斯祖尔复形正合。*

(b) *反过来，设 $A$ 为局部环，而且 $x_1,\ldots,x_r$ 属于 $A$ 的极大理想。设 $M$ 在 $A$ 上有限，并且假设 $H_1K(x;M)=0$。则 $(x_1,\ldots,x_r)$ 是 $M$-正则序列。*

**译校注：** (b) 的原陈述未排除 $M=0$。按本书前面正则序列的定义，还要求 $M/(x_1,\ldots,x_r)M\ne0$，所以此处应限制为 $M\ne0$；对于非零有限模，局部环及 $x_i$ 属于极大理想的假设通过中山引理保证这一商模非零。若 $M=0$，虽然 $H_1=0$，却不满足该定义的非零商模条件。

*证明。* 对 $r$ 归纳证明(a)。若 $r=1$，则直接由定义有 $H_1(x;M)=0$。设 $r>1$。使用定理4.5(a)中的正合列。当 $p>1$ 时，$H_p(x;M)$ 位于两个为 $0$ 的同调群之间，所以 $H_p(x;M)=0$。若 $p=1$，则使用定理4.5(a)正合列的最末部分，注意 $m(x_r)$ 单射，结合归纳假设得到 $H_1(x;M)=0$，从而证明(a)。

对于(b)，由引理4.4及假设得到正合列

$$
H_1(x_1,\ldots,x_{r-1};M)\xrightarrow{m(x_r)}H_1(x_1,\ldots,x_{r-1};M)\to H_1(x;M)=0,
$$

所以 $m(x_r)$ 满射。由中山引理，得到

$$
H_1(x_1,\ldots,x_{r-1};M)=0.
$$

由归纳假设，$(x_1,\ldots,x_{r-1})$ 为 $M$-正则序列。再像(a)中那样考察该正合列的末尾，便知 $x_r$ 是 $M/(x_1,\ldots,x_{r-1})M$-正则的，故(b)成立，定理得证。

注意，(b)只使用 $H_1$ 为零，而不要求所有 $H_p$ 都为零；这一结果出自 Northcott [No 68]，8.5，定理8。由(a)可知，$p>0$ 时 $H_p=0$。

<span class="original-page-anchor" id="pdf-page-865" aria-hidden="true"></span>

定理4.6(a)的一个重要特例是 $M=A$，此时可将该定理重述为：

*设 $x_1,\ldots,x_r$ 是 $A$ 中的正则序列。则 $K(x_1,\ldots,x_r)$ 是 $A/I$ 的自由解消：*

$$
0\to K_r(x)\to\cdots\to K_1(x)\to A\to A/I\to0.
$$

*特别地，$A/I$ 的 Tor 维数 $\leq r$。*

对于 Hom 函子，有：

**定理4.7。** *设 $x_1,\ldots,x_r$ 为 $A$ 中的正则序列。则存在同构*

$$
\varphi_{x,M}:H^r(\operatorname{Hom}(K(x),M))\to M/IM,
$$

*其具体形式将在下面描述。*

*证明。* 模 $K_r(x)$ 是1维的，以 $e_1\wedge\cdots\wedge e_r$ 为基。依赖于这个基，有同构

$$
\operatorname{Hom}(K_r(x),M)\approx M,
$$

其中一个同态由它在该基元素处的值（属于 $M$）确定。科斯祖尔复形的边缘映射 $d_r$ 定义为

$$
d_r:e_1\wedge\cdots\wedge e_r\mapsto\sum_{j=1}^r(-1)^{j-1}x_je_1\wedge\cdots\wedge\widehat{e_j}\wedge\cdots\wedge e_r,
$$

因此直接看出

$$
\begin{aligned}
H^r(\operatorname{Hom}(K(x),M))&\approx\operatorname{Hom}(K_r(x),M)/d^{r-1}\operatorname{Hom}(K_{r-1}(x),M)\\
&\approx M/IM.
\end{aligned}
$$

**译校注：** 上式左端原印为 $H^r(\operatorname{Hom}(K_r(x),M))$。这里取同调的对象应是完整复形 $\operatorname{Hom}(K(x),M)$；右端所除去的 $d^{r-1}$ 边缘项来自其前一项 $\operatorname{Hom}(K_{r-1}(x),M)$。这也与定理4.7的陈述一致。

定理得证。

读过第二十章的读者知道，$\operatorname{Hom}(K(x),M)$ 的第 $i$ 个同调群称为 $\operatorname{Ext}_A^i(A/I,M)$，由该复形确定至唯一同构，因为 $A/I$ 的任意两个解消之间存在复形态射，而两个这样的态射相差一个同伦，该同伦给出同调同构。因此定理4.7给出同构

$$
\varphi_{x,M}:\operatorname{Ext}^r(A/I,M)\to M/IM.
$$

实际上，我们将通过改变序列得到科斯祖尔复形的态射。现在回到引理4.2的假设。

<span class="original-page-anchor" id="pdf-page-866" aria-hidden="true"></span>

**引理4.8。** *若 $I=(x)=(y)$，其中 $(x)$、$(y)$ 是两个正则序列，则有交换图*

![由 Ext r(A/I,M) 到两个 M/IM 的交换三角形，映射为 phi x,M、phi y,M，以及乘以 D = det(cij)。](/library/volume-86/diagrams/pdf-0866-determinant-triangle.png)

*其中所有映射都是 $A/I$-模的同构。*

这里涉及的是 $A/I$-模，这一点是直接的，因为乘以 $A$ 中元素的映射与所有出现的同态都交换，而且 $I$ 零化 $A/I$。

由命题4.1，$I/I^2$ 是 $A/I$ 上秩为 $r$ 的自由模。因此

$$
\bigwedge^r(I/I^2)
$$

是秩为1的自由模，以 $\bar x_1\wedge\cdots\wedge\bar x_r$ 为基（上横线表示模 $I^2$ 的剩余类）。对这个外积取对偶，可见在换基时，它按模 $I$ 的行列式的逆进行变换。这使我们能够得到下一个定理中的典范同构。

**定理4.9。** *设 $x_1,\ldots,x_r$ 为 $A$ 中的正则序列，令 $I=(x)$。设 $M$ 为 $A$-模。令*

$$
\psi_{x,M}:M/IM\to(M/IM)\otimes\bigwedge^r(I/I^2)^{\mathrm{dual}}
$$

*为由 $\bigwedge^r(I/I^2)^{\mathrm{dual}}$ 的基 $(\bar x_1\wedge\cdots\wedge\bar x_r)^{\mathrm{dual}}$ 确定的嵌入。则复合同构*

$$
\operatorname{Ext}^r(A/I,M)\xrightarrow{\varphi_{x,M}}M/IM\xrightarrow{\psi_{x,M}}(M/IM)\otimes\bigwedge^r(I/I^2)^{\mathrm{dual}}
$$

*是函子性同构，不依赖于 $I$ 的正则生成元的选择。*

在中间次数上，也有定理4.5的类似结果。

**定理4.10。** *设 $x_1,\ldots,x_r$ 为 $A$ 中的 $M$-正则序列。令 $I=(x)$。则*

$$
\operatorname{Ext}^i(A/I,M)=0\quad\text{当 }i<r.
$$

*证明。* 在证明中，假定读者熟悉同调正合列。归纳假定 $\operatorname{Ext}^i(A/I,M)=0$ 对于<span class="original-page-anchor" id="pdf-page-867" aria-hidden="true"></span>$i<r-1$ 成立。于是有正合列

$$
0=\operatorname{Ext}^{i-1}(A/I,M/x_1M)\to\operatorname{Ext}^i(A/I,M)\xrightarrow{x_1}\operatorname{Ext}^i(A/I,M),
$$

其中 $i<r$。但 $x_1\in I$，所以乘以 $x_1$ 在同调群上诱导零映射，从而得到所需的 $\operatorname{Ext}^i(A/I,M)=0$。

设 $L_N\to N\to0$ 为模 $N$ 的自由解消。根据定义，

$$
\operatorname{Tor}_i^A(N,M)=\text{复形 }L\otimes M\text{ 的第 }i\text{ 个同调}.
$$

这与 $L_N$ 的选择无关，确定至唯一同构。现在我们要对 Tor 做刚才对 Ext 所做的工作。

**定理4.11。** *设 $I=(x_1,\ldots,x_r)$ 为 $A$ 的理想，由长度为 $r$ 的正则序列生成。*

(i) *存在自然同构*

$$
\operatorname{Tor}_i^A(A/I,A/I)\approx\bigwedge_{A/I}^i(I/I^2),\quad\text{对 }i\geq0.
$$

(ii) *设 $L$ 为自由 $A/I$-模，通过自然方式视为 $A$-模。则*

$$
\operatorname{Tor}_i^A(L,A/I)\approx L\otimes\bigwedge_{A/I}^i(I/I^2),\quad\text{对 }i\geq0.
$$

这些同构将由下面的讨论得到。

首先再次利用：模 $I^2$ 的剩余类 $\bar x_1,\ldots,\bar x_r$ 构成 $I/I^2$ 在 $A/I$ 上的基。因此存在唯一的复形同构

$$
\varphi_x:K(x)\otimes A/I\to\bigwedge(I/I^2)=\bigoplus\bigwedge^i(I/I^2),
$$

右端的微分都为零，并且

$$
e_{i_1}\wedge\cdots\wedge e_{i_p}\mapsto\bar x_{i_1}\wedge\cdots\wedge\bar x_{i_p}.
$$

**引理4.12。** *设 $I=(x)\supset I'=(y)$ 为两个理想，均由长度为 $r$ 的正则序列生成。设 $f:K(y)\to K(x)$ 为引理4.2中定义的科斯祖尔复形态射。则下图交换：*

![交换方形：张量以 A/I′、A/I 的科斯祖尔复形映到相应的外代数；竖直映射为 f 张量典范映射及典范同态。](/library/volume-86/diagrams/pdf-0867-exterior-square.png)

<span class="original-page-anchor" id="pdf-page-868" aria-hidden="true"></span>

*证明。* 有

$$
\begin{aligned}
&\varphi_x\circ(f\otimes\mathrm{can})(e'_{i_1}\wedge\cdots\wedge e'_{i_p}\otimes1)\\
&\qquad=\sum_{j=1}^r c_{i_1j}\bar x_j\wedge\cdots\wedge\sum_{j=1}^r c_{i_pj}\bar x_j\\
&\qquad=\bar y_{i_1}\wedge\cdots\wedge\bar y_{i_p}=\mathrm{can}(\varphi_y(e'_{i_1}\wedge\cdots\wedge e'_{i_p})).
\end{aligned}
$$

**译校注：** 第一处求和下限原印为 $j=2$，此处应为 $j=1$。由 $y_i=\sum_{j=1}^r c_{ij}x_j$，不能略去 $c_{i_1,1}\bar x_1$；例如取 $f$ 为恒等映射、$i_1=1$ 时，原下限会将应为 $\bar x_1$ 的项变为零。

引理得证。

特别地，如果 $I'=I$，则有交换图

![将两个科斯祖尔复形映到 I/I² 的外代数的交换三角形。](/library/volume-86/diagrams/pdf-0868-exterior-triangle.png)

这表明，通过选择基所给出的 $\operatorname{Tor}_i(A/I,A/I)$ 与 $\bigwedge^i(I/I^2)$ 的识别，在这些科斯祖尔复形的一个同构下相容；这些复形给出 $A/I$ 的解消。由于任何其他科斯祖尔复形同态都与这个同态同伦，所以该识别不依赖于所作的选择，从而证明了定理4.11的第一部分。第二部分立即成立，因为

$$
\begin{aligned}
\operatorname{Tor}_i^A(A/I,L)&=H_i(K(x)\otimes L)=H_i((K(x)\otimes_A A/I)\otimes_{A/I}L)\\
&=\bigwedge_{A/I}^i(I/I^2)\otimes L.
\end{aligned}
$$

**译校注：** 原式中 $H_i((K(x)\otimes_A A/I)\otimes_{A/I}L$ 的末尾漏去右括号；这里补出，表示取整个张量复形的第 $i$ 个同调。

这完成了定理4.11的证明。

**例。** 设 $k$ 为域，$A=k[x_1,\ldots,x_r]$ 为 $r$ 个变量的多项式环。令 $I=(x_1,\ldots,x_r)$ 为由这些变量生成的理想。则 $A/I=k$，故由定理4.11，当 $i\geq0$ 时有

$$
\operatorname{Tor}_i^A(k,k)\approx\bigwedge_k^i(I/I^2),
$$

$$
\operatorname{Tor}_i^A(L,k)\approx L\otimes\bigwedge_k^i(I/I^2).
$$

注意，在这里可将 $I/I^2$ 看作以 $\bar x_1,\ldots,\bar x_r$ 为基的 $k$ 上向量空间。于是可以把 $A$ 看作对称代数 $SE$，其中 $E$ 就是这个向量空间。在这个背景下，可以像下一个定理那样给出科斯祖尔复形的一个具体例子；该定理针对自由模给出。

<span class="original-page-anchor" id="pdf-page-869" aria-hidden="true"></span>

**定理4.13。** *设 $E$ 为环 $R$ 上秩为 $r$ 的有限自由模。对于每个 $p=1,\ldots,r$，存在唯一同态*

$$
d_p:\bigwedge^pE\otimes SE\to\bigwedge^{p-1}E\otimes SE,
$$

*使得*

$$
\begin{aligned}
&d_p((x_1\wedge\cdots\wedge x_p)\otimes y)\\
&\qquad=\sum_{i=1}^p(-1)^{i-1}(x_1\wedge\cdots\wedge\widehat{x_i}\wedge\cdots\wedge x_p)\otimes(x_i\otimes y),
\end{aligned}
$$

*其中 $x_i\in E$、$y\in SE$。这给出解消*

$$
0\to\bigwedge^rE\otimes SE\to\bigwedge^{r-1}E\otimes SE\to\cdots\to\bigwedge^0E\otimes SE\to R\to0.
$$

**译校注：** 定义式左端原印为 $d_i$；该同态的定义域是第 $p$ 次外幂，故指标应为 $p$，而 $i$ 是右端的求和指标。这里保留作者用 $x_i\otimes y$ 表示对称代数中相应乘积的记号。

*证明。* 上述定义不过是对称代数 $SE$ 的科斯祖尔复形的例子，其正则序列由 $E$ 的某个基构成。

由于 $d_p$ 将 $\bigwedge^pE\otimes S^qE$ 映入 $\bigwedge^{p-1}E\otimes S^{q+1}E$，可以按给定的分次分量将该复形分解为直和。因此：

**推论4.14。** *对于每个整数 $n\geq1$，存在正合列*

$$
0\to\bigwedge^rE\otimes S^{n-r}E\to\cdots\to\bigwedge^1E\otimes S^{n-1}E\to S^nE\to0,
$$

*其中当 $j<0$ 时，$S^jE=0$。*

最后，给出对希尔伯特一个经典定理的应用。多项式环 $A=k[x_1,\ldots,x_r]$ 按齐次分量的次数自然分次。*我们考虑次数均 $\geq0$ 的分次模，并假定同态都是次数为0的分次同态。*

设 $M$ 为分次模（因此当 $i<0$ 时 $M_i=0$），且 $M$ 在 $A$ 上有限。那么可以找到分次满同态

$$
L_0\to M\to0,
$$

其中 $L_0$ 有限自由。事实上，取 $M$ 的齐次生成元 $w_1,\ldots,w_n$。取 $A$ 上自由模 $L_0$ 的基元素 $e_1,\ldots,e_n$。赋予 $L_0$ 如下分次：若 $a\in A$ 是次数为 $d$ 的齐次元素，则 $ae_i$ 为齐次元素，其次数为

$$
\deg ae_i=\deg a+\deg w_i.
$$

于是将 $e_i$ 映到 $w_i$ 的 $L_0$ 到 $M$ 的满同态，就是所需的分次同态。

<span class="original-page-anchor" id="pdf-page-870" aria-hidden="true"></span>

核 $M_1$ 是 $L_0$ 的分次子模。重复这个过程，可以找到满同态

$$
L_1\to M_1\to0.
$$

继续这样做便得到 $M$ 的分次解消。我们希望这个解消能够终止，下一个定理给出了它能够终止的依据。

**定理4.15（希尔伯特合冲定理）。** *设 $k$ 为域，*

$$
A=k[x_1,\ldots,x_r]
$$

*为 $r$ 个变量的多项式环。设 $M$ 为 $A$ 上分次模，并设*

$$
0\to K\to L_{r-1}\to\cdots\to L_0\to M\to0
$$

*为分次模及其分次同态的正合列，其中 $L_0,\ldots,L_{r-1}$ 自由。则 $K$ 自由。如果 $M$ 还在 $A$ 上有限，且 $L_0,\ldots,L_{r-1}$ 有限自由，则 $K$ 有限自由。*

*证明。* 由科斯祖尔复形知道，对于所有 $M$，当 $i>r$ 时都有 $\operatorname{Tor}_i(M,k)=0$。由维数移位，得到

$$
\operatorname{Tor}_i(K,k)=0\quad\text{当 }i>0.
$$

于是该定理由下面的结果推出。

**定理4.16。** *设 $F$ 为 $A=k[x_1,\ldots,x_r]$ 上的分次有限模。若 $\operatorname{Tor}_1(F,k)=0$，则 $F$ 自由。*

*证明。* 所用方法本质上是在非局部环 $A$ 的情形中进行中山引理式的论证。首先注意

$$
F\otimes k=F/IF,
$$

其中 $I=(x_1,\ldots,x_r)$。因此 $F\otimes k$ 自然是 $A/I=k$-模。取 $F$ 的齐次元素 $v_1,\ldots,v_n$，使它们模 $IF$ 的剩余类构成 $F/IF$ 在 $k$ 上的基。设 $L$ 为以 $e_1,\ldots,e_n$ 为基的自由模。令

$$
L\to F
$$

为将 $e_i$ 映到 $v_i$ 的分次同态（$i=1,\ldots,n$）。只需证明它是同构。令 $C$ 为余核，则有正合列

$$
L\to F\to C\to0.
$$

张量以 $k$，得到正合列

$$
L\otimes k\to F\otimes k\to C\otimes k\to0.
$$

<span class="original-page-anchor" id="pdf-page-871" aria-hidden="true"></span>

由于按构造映射 $L\otimes k\to F\otimes k$ 满射，所以 $C\otimes k=0$。但 $C$ 分次，因而下面的引理表明 $C=0$。

**引理4.17。** *设 $N$ 为 $A=k[x_1,\ldots,x_r]$ 上的分次模。令 $I=(x_1,\ldots,x_r)$。若 $N/IN=0$，则 $N=0$。*

*证明。* 利用分次，考察 $N$ 中次数最小的元素（若它们存在），并利用 $N$ 中元素的次数都 $>0$，即可直接得出。

**译校注：** 原文确印“$N$ 中元素的次数 $>0$”。这里证明所需的是理想 $I=(x_1,\ldots,x_r)$ 的非零齐次元素具有正次数；$N$ 本身可以有次数为 $0$ 的元素，例如 $N=A$。因此这句话中的 $N$ 应读作 $I$。

现在得到分次模的正合列

$$
0\to E\to L\to F\to0,
$$

必须证明 $E=0$。但由同调正合列及我们的假设，得到

$$
0=\operatorname{Tor}_1(F,k)\to E\otimes k\to L\otimes k\to F\otimes k\to0.
$$

按构造，$L\otimes k\to F\otimes k$ 是同构，故 $E\otimes k=0$。现在引理4.17表明 $E=0$。这完成了合冲定理的证明。

**评述。** 证明中唯一使用 $k$ 为域的地方，是定理4.16的证明里选取 $M$ 的齐次元素 $v_1,\ldots,v_n$，使它们模 $IM$ 的剩余类构成 $M/IM$ 在 $A/IA$ 上的基。通过作出适当的假设，保证这一步能够进行，可以如下推广希尔伯特定理。

**定理4.18。** *设 $R$ 为交换局部环，$A=R[x_1,\ldots,x_r]$ 为 $r$ 个变量的多项式环。设 $M$ 为 $A$ 上的分次有限模，在 $R$ 上投射。设*

$$
0\to K\to L_{r-1}\to\cdots\to L_0\to M\to0
$$

*为分次模及其分次同态的正合列，其中 $L_0,\ldots,L_{r-1}$ 有限自由。则 $K$ 有限自由。*

*证明。* 在希尔伯特合冲定理的证明中，将所有 $k$ 都替换为 $R$。使用局部环上的有限投射模为自由模这一事实。除以下一点外，上面的证明一字不必改动。注意，投射性会传递到给定解消的核与余核。因此可假定定理4.16陈述中的 $F$ 投射，并且每个分次分量都投射。于是 $F/IF$ 在 $A/IA=R$ 上投射，其每个分次分量也投射。由于局部环上的有限投射模自由，而且可以通过提升剩余类域的一个基得到自由性，所以可以像定理4.16的证明中完全一样，选取齐次的 $v_1,\ldots,v_n$。证明完成。

<span class="original-page-anchor" id="pdf-page-872" aria-hidden="true"></span>

## 习题

关于科斯祖尔复形的习题1至4，参见 [No 68] 第8章。

**1。** 设 $0\to M'\to M\to M''\to0$ 为 $A$-模的正合列。证明，张量以科斯祖尔复形 $K(x)$ 后得到复形的正合列，因而得到同调正合列

$$
\begin{aligned}
&0\to H_rK(x;M')\to H_rK(x;M)\to H_rK(x;M'')\to\cdots\\
&\cdots\to H_pK(x;M')\to H_pK(x;M)\to H_pK(x;M'')\to\cdots\\
&\cdots\to H_0K(x;M')\to H_0K(x;M)\to H_0K(x;M'')\to0.
\end{aligned}
$$

**2。** (a) 证明，存在唯一的复形同态

$$
f:K(x;M)\to K(x_1,\ldots,x_{r-1},1;M),
$$

使对于 $v\in M$：

$$
f_p(e_{i_1}\wedge\cdots\wedge e_{i_p}\otimes v)=\begin{cases}
e_{i_1}\wedge\cdots\wedge e_{i_p}\otimes x_rv&\text{若 }i_p=r,\\
e_{i_1}\wedge\cdots\wedge e_{i_p}\otimes v&\text{若 }i_p<r.
\end{cases}
$$

**译校注：** 第二个分支的条件原印同样为 $i_p=r$。两分支分别处理外积是否含最后一个基元素；若第二个条件仍为 $i_p=r$，就会对同一输入给出两个通常不同的值，并且没有定义 $i_p<r$ 时的值。因此第二个条件应为 $i_p<r$。

(b) 若 $x_r$ 不是 $M$ 中的零因子，证明 $f$ 单射。

(c) 对复形 $C$，用 $C(-1)$ 表示向左平移一位的复形，故对所有 $n$ 有 $C(-1)_n=C_{n-1}$。令 $\bar M=M/x_rM$。证明，存在唯一的复形同态

$$
g:K(x_1,\ldots,x_{r-1},1;M)\to K(x_1,\ldots,x_{r-1};\bar M)(-1),
$$

使对于 $v\in M$：

$$
g_p(e_{i_1}\wedge\cdots\wedge e_{i_p}\otimes v)=\begin{cases}
e_{i_1}\wedge\cdots\wedge e_{i_{p-1}}\otimes\bar v&\text{若 }i_p=r,\\
0&\text{若 }i_p<r.
\end{cases}
$$

(d) 若 $x_r$ 不是 $M$ 中的零因子，证明下列序列正合：

$$
0\to K(x;M)\xrightarrow{f}K(x_1,\ldots,x_{r-1},1;M)\xrightarrow{g}K(x_1,\ldots,x_{r-1};\bar M)(-1)\to0.
$$

利用定理4.5(c)，推出对所有 $p\geq0$，存在同构

$$
H_pK(x;M)\xrightarrow{\approx}H_pK(x_1,\ldots,x_{r-1};\bar M).
$$

**3。** 假设 $A$、$M$ 都诺特。设 $I$ 为 $A$ 的理想，$a_1,\ldots,a_k$ 为 $I$ 中的 $M$-正则序列。证明，该序列可以延长为 $I$ 中的极大 $M$-正则序列 $a_1,\ldots,a_q$，也就是说，它是一个 $M$-正则序列，且不存在 $I$ 中的 $M$-正则序列 $a_1,\ldots,a_{q+1}$。

**4。** 再次假设 $A$、$M$ 都诺特。令 $I=(x_1,\ldots,x_r)$，并设 $a_1,\ldots,a_q$ 为 $I$ 中的极大 $M$-正则序列。假设 $IM\ne M$。证明

$$
H_{r-q}(x;M)\ne0,\text{ 但当 }p>r-q\text{ 时 }H_p(x;M)=0.
$$

[参见 [No 68]，8.5，定理6。此结果与习题5中的结果类似，并推广了定理4.5(a)。另见 [Mat 80]，第100—103页。这个结果表明<span class="original-page-anchor" id="pdf-page-873" aria-hidden="true"></span>$I$ 中的所有极大 $M$-正则序列具有相同长度，这个长度称为 **$M$ 的 $I$-深度**，记为 $\operatorname{depth}_I(M)$。为证明这一点，令 $s$ 为使 $H_sK(x;M)\ne0$ 的最大整数。由假设，$H_0(x;M)=M/IM\ne0$，故 $s$ 存在。须证明 $q+s=r$。先注意，如果 $q=0$，则 $s=r$。事实上，若 $q=0$，则 $I$ 的每个元素都是 $M$ 中的零因子，因此 $I$ 包含在 $M$ 的关联素理想的并中，进而包含在 $M$ 的某个关联素理想中。故 $H_r(x;M)\ne0$。

**译校注：** 页首原文为 “all maximal $M$-regular sequences in $M$”；所讨论的序列的元素属于理想 $I\subset A$，并非一般属于模 $M$。上一页习题4及本段的 $I$-深度定义均表明这里的 “in $M$” 应为 “in $I$”。

接着设 $q>0$，进行归纳。考虑正合列

$$
0\to M\xrightarrow{a_1}M\to M/a_1M\to0,
$$

其中第一个映射为 $m(a_1)$。由于 $I$ 零化 $H_p(x;M)$，得到正合列

$$
0\to H_p(x;M)\to H_p(x;M/a_1M)\to H_{p-1}(x;M)\to0.
$$

**译校注：** 零化性质在原文中引作定理4.5(c)，实际是定理4.5(b)；(c)陈述的是 $I=A$ 时全部同调为零。

因此 $H_{s+1}(x;M/a_1M)\ne0$，但当 $p\geq s+2$ 时，$H_p(x;M/a_1M)=0$。由 $a_1,\ldots,a_q$ 为极大 $M$-正则序列的假设，立即可知 $a_2,\ldots,a_q$ 是 $I$ 中的极大 $M/a_1M$-正则序列。所以由归纳假设，$q-1=r-(s+1)$，从而 $q+s=r$，证毕。]

**5。** 下面的习题结合了第二十章同调论中的一些概念，以及本章和第十章§5中讨论的一些概念。设 $M$ 为 $A$-模。

设 $A$ 诺特，$M$ 为 $A$ 上有限模，$I$ 为 $A$ 的理想，且 $IM\ne M$。设 $r$ 为整数且 $r\geq1$。证明，下列条件等价：

(i) 对所有 $i<r$ 及所有满足 $\operatorname{supp}(N)\subset\mathscr L(I)$ 的有限模 $N$，都有 $\operatorname{Ext}^i(N,M)=0$。

(ii) 对所有 $i<r$，有 $\operatorname{Ext}^i(A/I,M)=0$。

(iii) 存在有限模 $N$，满足 $\operatorname{supp}(N)=\mathscr L(I)$，并且

$$
\operatorname{Ext}^i(N,M)=0\quad\text{对所有 }i<r.
$$

(iv) $I$ 中存在 $M$-正则序列 $a_1,\ldots,a_r$。

[**提示：** (i) $\Rightarrow$ (ii) $\Rightarrow$ (iii) 显然。对于(iii) $\Rightarrow$ (iv)，首先注意

$$
0=\operatorname{Ext}^0(N,M)=\operatorname{Hom}(N,M).
$$

假定 $\operatorname{supp}(N)=\mathscr L(I)$。在 $I$ 中寻找一个 $M$-正则元素。如果不存在这样的元素，则 $I$ 包含在 $A$ 中关于 $M$ 的零因子集合内，这个集合是关联素理想的并。因此对于某个关联素理想 $P$，有 $I\subset P$。由此得到单射 $A/P\subset M$，所以

$$
0\ne\operatorname{Hom}_{A_P}(A_P/PA_P,M_P).
$$

**译校注：** 上式的第二个变量原印为 $M$。在 $A_P$ 上取同态时，按这里对 $A/P\subset M$ 作局部化的论证，目标应为 $M_P$；后面两式也使用 $M_P$。一般的 $A$-模 $M$ 本身并没有给定 $A_P$-模结构。

由假设，$N_P\ne0$，所以 $N_P/PN_P\ne0$，而 $N_P/PN_P$ 是 $A_P/PA_P$ 上的向量空间，故存在非零的 $A_P/PA_P$-同态

$$
N_P/PN_P\to M_P.
$$

于是 $\operatorname{Hom}_{A_P}(N_P,M_P)\ne0$，从而 $\operatorname{Hom}(N,M)\ne0$，矛盾。这证明了存在一个正则元素 $a_1$。

<span class="original-page-anchor" id="pdf-page-874" aria-hidden="true"></span>

现在令 $M_1=M/a_1M$。正合列

$$
0\to M\xrightarrow{a_1}M\to M/a_1M\to0
$$

给出上同调正合列

$$
\to\operatorname{Ext}^i(N,M)\to\operatorname{Ext}^i(N,M/a_1M)\to\operatorname{Ext}^{i+1}(N,M)\to,
$$

所以当 $i<r-1$ 时，$\operatorname{Ext}^i(N,M/a_1M)=0$。由归纳假设，存在 $M_1$-正则序列 $a_2,\ldots,a_r$，于是完成了证明。

最后证明(iv) $\Rightarrow$ (i)。假定存在该正则序列。由归纳假设，当 $i<r-1$ 时，$\operatorname{Ext}^i(N,M/a_1M)=0$。当 $i<r$ 时有正合列：

$$
0\to\operatorname{Ext}^i(N,M)\xrightarrow{a_1}\operatorname{Ext}^i(N,M).
$$

**译校注：** 归纳消失式的第二个变量原印为 $a_1M$，此处应为 $M/a_1M$。剩下的正则序列作用于商模 $M_1$，而用于得到上述单射的长正合列前项为 $\operatorname{Ext}^{i-1}(N,M/a_1M)$；归纳正是使这一项为零。

但 $\operatorname{supp}(N)=\mathscr L(\operatorname{ann}(N))\subset\mathscr L(I)$，所以 $I\subset\operatorname{rad}(\operatorname{ann}(N))$，因而 $a_1$ 在 $N$ 上幂零。于是 $a_1$ 在 $\operatorname{Ext}^i(N,M)$ 上也幂零，所以 $\operatorname{Ext}^i(N,M)=0$。证毕。] 参见 Matsumura 的 [Mat 70]，第100页，定理28。这个结果在代数几何中很有用，例如可以取 $M=A$ 本身。将 $A$ 看作某个簇的仿射坐标环，将方程 $a_i=0$ 看作定义该簇的超曲面截面，并将联立方程 $a_1=\cdots=a_r=0$ 看作定义一个完全交。该定理以 Ext 给出了这种完全交存在性的上同调判据。
