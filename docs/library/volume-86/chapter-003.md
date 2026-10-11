---
title: "第三章 模"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第二章 环","link":"/library/volume-86/chapter-002"}
next: {"text":"第四章 多项式","link":"/library/volume-86/chapter-004"}
---

# 第三章 模

<span class="original-page-anchor" id="pdf-page-132" aria-hidden="true"></span>

虽然本章在逻辑上自成体系，并为后续主题作准备，但实际上，读者应当已经对域上的向量空间有所了解。在这里，我们将这个概念推广为环上的模。向量空间具有一组基，这是一个标准事实（我们将重新证明）；但对于模，情况并非总是如此。有时模有基，更多时候则没有。我们将研究模具有基的情形。

关于模的例子，以及它们与具有基的模之间的关系，读者应参看第 4 节末尾的评述。

## §1. 基本定义

设 $A$ 是一个环。$A$ 上的**左模**，或称左 $A$-模 $M$，是一个阿贝尔群，通常用加法记号书写，并带有 $A$ 在 $M$ 上的一个作用（依据 **RI 2**，将 $A$ 看成乘法幺半群），使得对于所有 $a,b\in A$ 和 $x,y\in M$，都有

$$
(a+b)x=ax+bx\quad\text{以及}\quad a(x+y)=ax+ay.
$$

我们将 $a(-x)=-(ax)$ 和 $0x=0$ 的证明留作习题。根据作用的定义，有 $1x=x$。

类似地，可以定义**右 $A$-模**。除非另有说明，我们只讨论左 $A$-模，因此将它们简称为 **$A$-模**；在所指明确时，甚至简称为**模**。

<span class="original-page-anchor" id="pdf-page-133" aria-hidden="true"></span>

设 $M$ 是一个 $A$-模。所谓 $M$ 的一个**子模** $N$，是指一个满足 $AN\subset N$ 的加法子群。于是 $N$ 是一个模（其作用由 $A$ 在 $M$ 上的作用诱导）。

### 例

注意，$A$ 是自身上的模。

任何交换群都是一个 $\mathbf{Z}$-模。

仅由 $0$ 构成的加法群是任意环上的模。

$A$ 的任何左理想都是一个 $A$ 上的模。

设 $J$ 是 $A$ 的一个双边理想。则商环 $A/J$ 实际上是一个 $A$ 上的模。若 $a\in A$，且 $x+J$ 是 $J$ 在 $A$ 中的一个陪集，则定义作用为 $a(x+J)=ax+J$。读者可以立即验证，这就在 $A/J$ 上定义了一个模结构。更一般地，若 $M$ 是一个模，$N$ 是一个子模，我们将在下文定义商模。因此，若 $L$ 是 $A$ 的一个左理想，则 $A/L$ 也是一个模。更多这类例子见第 4 节。

域上的模称为**向量空间**。即便从向量空间出发，我们也会被引向环上的模。事实上，设 $V$ 是域 $K$ 上的一个向量空间。读者无疑已经知道线性映射（下文将对此作系统的回顾）。设 $R$ 是从 $V$ 到自身的所有线性映射构成的环。则 $V$ 是一个 $R$ 上的模。类似地，若 $V=K^n$ 表示由 $K$ 中元素的（竖排）$n$ 元组构成的向量空间，而 $R$ 是分量在 $K$ 中的 $n\times n$ 矩阵所构成的环，则 $V$ 是一个 $R$ 上的模。关于这些内容的更多评述，见第 2 节末尾的例子。

设 $S$ 是一个非空集合，$M$ 是一个 $A$-模。则映射集合 $\operatorname{Map}(S,M)$ 是一个 $A$-模。我们之前已经指出它是一个交换群；对于 $f\in\operatorname{Map}(S,M)$、$a\in A$，我们定义 $af$ 为满足 $(af)(s)=af(s)$ 的映射。于是模的公理很容易验证。

更多例子见本节末尾。

在本节余下的内容中，我们讨论一个固定的环 $A$，因此可以省略前缀 $A$-。

设 $A$ 是一个整环，$M$ 是一个 $A$-模。我们将**挠子模** $M_{\mathrm{tor}}$ 定义为由如下元素 $x\in M$ 构成的子集：存在 $a\in A$、$a\ne0$，使得 $ax=0$。可以立即验证，$M_{\mathrm{tor}}$ 是一个子模。第 7 节将确定它在一个重要情形下的结构。

设 $\mathfrak{a}$ 是一个左理想，$M$ 是一个模。我们定义 $\mathfrak{a}M$ 为所有形如

$$
a_1x_1+\cdots+a_nx_n
$$

的元素构成的集合，其中 $a_i\in\mathfrak{a}$ 且 $x_i\in M$。显然，它是 $M$ 的一个子模。若 $\mathfrak{a},\mathfrak{b}$ 是左理想，则有结合律，即

$$
\mathfrak{a}(\mathfrak{b}M)=(\mathfrak{a}\mathfrak{b})M.
$$

<span class="original-page-anchor" id="pdf-page-134" aria-hidden="true"></span>

我们还有一些显然的分配律，例如 $(\mathfrak{a}+\mathfrak{b})M=\mathfrak{a}M+\mathfrak{b}M$。若 $N,N'$ 是 $M$ 的子模，则 $\mathfrak{a}(N+N')=\mathfrak{a}N+\mathfrak{a}N'$。

设 $M$ 是一个 $A$-模，$N$ 是一个子模。我们将在商群 $M/N$（相对于加法群结构）上定义一个模结构。设 $x+N$ 是 $N$ 在 $M$ 中的一个陪集，且 $a\in A$。我们定义 $a(x+N)$ 为陪集 $ax+N$。很容易验证，这个定义是良定义的（即若 $y$ 与 $x$ 属于同一陪集，则 $ay$ 与 $ax$ 也属于同一陪集）；并且，这是 $A$ 在 $M/N$ 上满足所需条件的一个作用，从而使 $M/N$ 成为一个模，称为 $M$ 对 $N$ 的**商模**。

所谓**模同态**，是指从一个模到另一个模的映射

$$
f:M\to M'
$$

（两个模都在同一个环 $A$ 上），它是一个加法群同态，并且对所有 $a\in A$ 和 $x\in M$ 满足

$$
f(ax)=af(x).
$$

于是显然，$A$-模构成一个范畴，其态射为模同态；在不致产生混淆时，为简便起见通常也简称为同态。若要明确指出环 $A$，我们也称 $f$ 为 **$A$-同态**，或称它为 **$A$-线性映射**。

若 $M$ 是一个模，则恒等映射是一个同态。对于任意模 $M'$，满足对所有 $x\in M$ 都有 $\zeta(x)=0$ 的映射 $\zeta:M\to M'$ 是一个同态，称为**零**同态。

下一节中，我们将讨论从一个模到自身的同态，并由此给出实际出现的模的更多例子。在这里，我们继续列出群的基本性质在模中的对应形式。

设 $M$ 是一个模，$N$ 是一个子模。我们有典范的加法群同态

$$
f:M\to M/N,
$$

很容易验证，它是一个模同态。

同样容易验证，在从 $M$ 出发、核包含 $N$ 的同态所构成的范畴中，$f$ 是泛的。

*若 $f:M\to M'$ 是一个模同态，则它的核与像分别是 $M$ 与 $M'$ 的子模*（验证很容易）。

设 $f:M\to M'$ 是一个同态。所谓 $f$ 的**余核**，是指商模 $M'/\operatorname{Im}f=M'/f(M)$。也可以用它来指典范同态<span class="original-page-anchor" id="pdf-page-135" aria-hidden="true"></span>$M'\to M'/f(M)$，而非模本身。上下文应当能明确所指。因此，余核是 $M'$ 的一个商模。

第 I 章第 3 节所讨论的典范同态，经过相应变更也适用于模。为方便读者，我们将这些同态概括如下：

*设 $N,N'$ 是一个模 $M$ 的两个子模。则 $N+N'$ 也是一个子模，并且有同构*

$$
N/(N\cap N')\approx(N+N')/N'.
$$

*若 $M\supset M'\supset M''$ 是模，则*

$$
(M/M'')/(M'/M'')\approx M/M'.
$$

*若 $f:M\to M'$ 是一个模同态，$N'$ 是 $M'$ 的一个子模，则 $f^{-1}(N')$ 是 $M$ 的一个子模，并且有一个典范的单射同态*

$$
\bar f:M/f^{-1}(N')\to M'/N'.
$$

*若 $f$ 是满射，则 $\bar f$ 是一个模同构。*

这些结论的证明，只需验证在讨论阿贝尔群时出现的所有同态，现在都是模的 $A$-同态。我们将验证留给读者。

与群的情况一样，我们注意到，一个双射的模同态是一个模同构。这里的证明也与群的情况相同，只需另外指出：已知为群同构的逆映射，实际上也是一个模同构。我们再次将验证留给读者。

与阿贝尔群一样，我们定义模同态列

$$
M'\xrightarrow{f}M\xrightarrow{g}M''
$$

是**正合的**，如果 $\operatorname{Im}f=\operatorname{Ker}g$。与模 $M$ 的一个子模 $N$ 相联系，有一个正合列，即

$$
0\to N\to M\to M/N\to0,
$$

其中从 $N$ 到 $M$ 的映射为包含映射，随后的映射为典范映射。正合性的概念源于 Eilenberg-Steenrod。

若一个同态 $u:N\to M$ 满足

$$
0\to N\xrightarrow{u}M
$$

是正合的，我们也称 $u$ 为**单态射**或**嵌入**。对偶地，若

$$
N\xrightarrow{u}M\to0
$$

是正合的，则称 $u$ 为**满态射**。

<span class="original-page-anchor" id="pdf-page-136" aria-hidden="true"></span>

### 代数

数学中有些对象满足环的全部公理，唯独没有单位元。第 II 章第 1 节给出的 $L^1(\mathbf{R})$ 就是一个例子。还有一些对象不满足结合律，但满足分配律。例如，设 $R$ 是一个环，对 $x,y\in R$ 定义**括号积**

$$
[x,y]=xy-yx.
$$

当 $R$ 不交换时，这个括号积在大多数情形下不满足结合律，但它满足分配律。

**例。** 一个典型例子是具有 $C^\infty$ 系数的微分算子环，它作用于 $\mathbf{R}^n$ 中一个开集上的 $C^\infty$ 函数环。两个微分算子的括号积

$$
[D_1,D_2]=D_1\circ D_2-D_2\circ D_1
$$

仍然是一个微分算子。在李群理论中，原点处的切空间也具有这样的括号积。

这些考虑引导我们定义比环更一般的概念。设 $A$ 是一个交换环，$E,F$ 是模。所谓**双线性映射**

$$
g:E\times E\to F,
$$

是指满足如下条件的映射：给定 $x\in E$，映射 $y\mapsto g(x,y)$ 是 $A$-线性的；给定 $y\in E$，映射 $x\mapsto g(x,y)$ 是 $A$-线性的。所谓 **$A$-代数**，是指一个模，并带有一个双线性映射 $g:E\times E\to E$。我们将这样的映射看成 $E$ 上的一个合成律。但在本书中，除非另有说明，我们假定所讨论的代数满足结合律并且具有单位元。

除已经提到的例子之外，我们注意到，群环 $A[G]$（当 $G$ 是幺半群时，则为幺半群环）是一个 $A$-代数，也称为**群代数**（或**幺半群代数**）。实际上，群代数可以看成以下情形的一个特例。

设 $f:A\to B$ 是一个环同态，使得 $f(A)$ 包含在 $B$ 的中心中，即对于每个 $a\in A$，$f(a)$ 都与 $B$ 的每一个元素交换。于是可以将 $B$ 看成一个 $A$-模，对所有 $a\in A$ 和 $b\in B$，用映射

$$
(a,b)\mapsto f(a)b
$$

定义 $A$ 在 $B$ 上的作用。模的公理显然成立，乘法合成律 $B\times B\to B$ 也显然是双线性的（即 $A$-双线性的）。本书中，除非另有说明，所谓 $A$ 上的**代数**，总是指上述形式的环同态。若 $B$ 作为 $f(A)$ 上的环是有限生成的，则称该代数是**有限生成的**。

下一节将给出多项式代数或群代数上的模的若干例子；在那里，我们也将建立关于表示的用语。

<span class="original-page-anchor" id="pdf-page-137" aria-hidden="true"></span>

## §2. 同态群

设 $A$ 是一个环，$X,X'$ 是 $A$-模。我们用 $\operatorname{Hom}_A(X',X)$ 表示从 $X'$ 到 $X$ 的 $A$-同态集合。则 $\operatorname{Hom}_A(X',X)$ 是一个阿贝尔群，其加法合成律就是取值于阿贝尔群的映射的加法。

若 $A$ 是*交换的*，则可以使 $\operatorname{Hom}_A(X',X)$ 成为一个 $A$-模：对于 $a\in A$ 和 $f\in\operatorname{Hom}_A(X',X)$，定义 $af$ 为满足

$$
(af)(x)=af(x)
$$

的映射。验证 $A$-模的公理成立是很容易的。但若 $A$ 不交换，我们就仅将 $\operatorname{Hom}_A(X',X)$ 看成一个阿贝尔群。

我们也将 $\operatorname{Hom}_A$ 看成一个函子。实际上，它是一个二元函子，对第一个变量反变，对第二个变量协变。事实上，设 $Y$ 是一个 $A$-模，且

$$
X'\xrightarrow{f}X
$$

是一个 $A$-同态。则得到一个诱导同态

$$
\operatorname{Hom}_A(f,Y):\operatorname{Hom}_A(X,Y)\to\operatorname{Hom}_A(X',Y)
$$

（箭头的方向反转了！），它由

$$
g\mapsto g\circ f
$$

给出。下面的映射列说明了这一点：

$$
X'\xrightarrow{f}X\xrightarrow{g}Y.
$$

$\operatorname{Hom}_A(f,Y)$ 是同态这一事实，不过是对性质 $(g_1+g_2)\circ f=g_1\circ f+g_2\circ f$ 的另一种表述；这个性质很容易验证。若 $f=\operatorname{id}$，则与 $f$ 复合相当于对 $g$ 作恒等映射，即 $g\circ\operatorname{id}=g$。

若有一个 $A$-同态列

$$
X'\to X\to X'',
$$

则得到一个诱导的列

$$
\operatorname{Hom}_A(X',Y)\leftarrow\operatorname{Hom}_A(X,Y)\leftarrow\operatorname{Hom}_A(X'',Y).
$$

**命题 2.1。** *列*

$$
X'\xrightarrow{\lambda}X\to X''\to0
$$

*是正合的，当且仅当对于所有 $Y$，列*

$$
\operatorname{Hom}_A(X',Y)\leftarrow\operatorname{Hom}_A(X,Y)\leftarrow\operatorname{Hom}_A(X'',Y)\leftarrow0
$$

*都是正合的。*

<span class="original-page-anchor" id="pdf-page-138" aria-hidden="true"></span>

*证明。* 这是一个重要事实，证明却很容易。例如，假定第一个列是正合的。若 $g:X''\to Y$ 是一个 $A$-同态，则它在 $\operatorname{Hom}_A(X,Y)$ 中的像，由 $g$ 与从 $X$ 到 $X''$ 的满射复合得到。若这个复合为 $0$，则因 $X\to X''$ 是满射，必有 $g=0$。再举一例，考虑一个同态 $g:X\to Y$，使得复合

$$
X'\xrightarrow{\lambda}X\xrightarrow{g}Y
$$

为 $0$。则 $g$ 在 $\lambda$ 的像上为零。因此，$g$ 可以通过商模分解：

$$
\begin{array}{ccc}
&X/\operatorname{Im}\lambda&\\
\nearrow&&\searrow\\
X&\xrightarrow{g}&Y
\end{array}
$$

由于 $X\to X''$ 是满射，有同构

$$
X/\operatorname{Im}\lambda\leftrightarrow X''.
$$

因此，$g$ 可以通过 $X''$ 分解，从而说明

$$
\operatorname{Hom}_A(X',Y)\leftarrow\operatorname{Hom}_A(X,Y)
$$

的核包含在

$$
\operatorname{Hom}_A(X,Y)\leftarrow\operatorname{Hom}_A(X'',Y)
$$

的像中。验证正合性所需的其他条件留给读者，逆命题也留给读者证明。

对于第二个变量，我们有类似的情况，但此时函子是协变的。因此，若 $X$ 固定，并且有一个 $A$-同态列

$$
Y'\to Y\to Y'',
$$

则得到诱导的列

$$
\operatorname{Hom}_A(X,Y')\to\operatorname{Hom}_A(X,Y)\to\operatorname{Hom}_A(X,Y'').
$$

**命题 2.2。** *列*

$$
0\to Y'\to Y\to Y'',
$$

*是正合的，当且仅当对于所有 $X$，*

$$
0\to\operatorname{Hom}_A(X,Y')\to\operatorname{Hom}_A(X,Y)\to\operatorname{Hom}_A(X,Y'')
$$

*都是正合的。*

<span class="original-page-anchor" id="pdf-page-139" aria-hidden="true"></span>

验证留给读者，它可由定义立即得到。

注意，说

$$
0\to Y'\to Y
$$

是正合的，意味着 $Y'$ 嵌入 $Y$ 中，即与 $Y$ 的一个子模同构。若有 $Y'\subset Y$，则一个取值于 $Y'$ 的同态可以看成取值于 $Y$ 的同态。这对应于单射

$$
0\to\operatorname{Hom}_A(X,Y')\to\operatorname{Hom}_A(X,Y).
$$

设 $\operatorname{Mod}(A)$ 和 $\operatorname{Mod}(B)$ 分别为环 $A$ 和 $B$ 上的模范畴，$F:\operatorname{Mod}(A)\to\operatorname{Mod}(B)$ 是一个函子。若 $F$ 将正合列变为正合列，就称 $F$ 是**正合的**。我们看到，当另一个变量固定时，Hom 函子对任一个变量都不一定是正合的。在后面的一节中，我们将定义使正合性得以保持的条件。

**自同态。** 设 $M$ 是一个 $A$-模。由关系

$$
(g_1+g_2)\circ f=g_1\circ f+g_2\circ f
$$

及其右侧的类似关系，即

$$
g\circ(f_1+f_2)=g\circ f_1+g\circ f_2,
$$

再加上复合运算具有单位元 $\operatorname{id}_M$，我们得出 $\operatorname{Hom}_A(M,M)$ 是一个环，其乘法定义为映射的复合。若 $n$ 是一个 $\geqq1$ 的整数，我们可以用 $f^n$ 表示 $f$ 与自身迭代复合 $n$ 次，并定义 $f^0$ 为 $\operatorname{id}$。根据范畴中自同态的一般定义，我们也用 $\operatorname{End}_A(M)$ 代替 $\operatorname{Hom}_A(M,M)$，并称 $\operatorname{End}_A(M)$ 为**自同态**环。

由于 $A$-模 $M$ 是一个阿贝尔群，我们看到 $\operatorname{Hom}_{\mathbf{Z}}(M,M)$（即从 $M$ 到自身的群同态集合）是一个环，并且本来也可以将 $A$ 在 $M$ 上的作用定义为一个环同态 $A\to\operatorname{Hom}_{\mathbf{Z}}(M,M)$。

设 $A$ 是*交换的*。则 $M$ 是 $\operatorname{End}_A(M)$ 上的一个模。若 $R$ 是 $\operatorname{End}_A(M)$ 的一个子环，则 $M$ 当然也是 $R$ 上的模。更一般地，设 $R$ 是一个环，$\rho:R\to\operatorname{End}_A(M)$ 是一个环同态。则称 $\rho$ 为 **$R$ 在 $M$ 上的表示**。尤其当 $A=K$ 是一个域时，会出现这种情况。环的表示的线性代数，将在第三部分中以几种背景来讨论，其中大多数是有限维的。分析中会出现无限维的例子，但此时表示论将代数与分析结合起来，因此超出了本课程的层次。

**例。** 设 $K$ 是一个域，$V$ 是 $K$ 上的一个向量空间。设 $D:V\to V$ 是一个自同态（$K$-线性映射）。对于每个多项式 $P(X)\in K[X]$，其中 $P(X)=\sum a_iX^i$、$a_i\in K$，我们可以定义

<span class="original-page-anchor" id="pdf-page-140" aria-hidden="true"></span>

$$
P(D)=\sum a_iD^i:V\to V,
$$

它是 $V$ 的一个自同态。对应 $P(X)\mapsto P(D)$ 给出一个表示

$$
\rho:K[X]\to\operatorname{End}_K(V),
$$

从而使 $V$ 成为一个 $K[X]$-模。第 IV 章将证明 $K[X]$ 是一个主理想整环。在第 7 节，我们将给出主理想整环上模的一般结构定理；第 XIV 章第 3 节将在有限维向量空间的线性代数背景中，将这个定理应用于上面的例子。已在本科课程中掌握基础线性代数的读者，也许愿意在此时就阅读第 XIV 章。

分析中会出现无限维向量空间的例子。例如，设 $V$ 是 $\mathbf{R}$ 上复值 $C^\infty$ 函数构成的向量空间。设 $D=d/dt$ 为求导算子（以 $t$ 为变量）。则 $D:V\to V$ 是一个线性映射，$\mathbf{C}[X]$ 有由 $P\mapsto P(D)$ 给出的表示 $\rho:\mathbf{C}[X]\to\operatorname{End}_{\mathbf{C}}(V)$。多元情形也类似：设 $V$ 是 $\mathbf{R}^n$ 的一个开集上的 $n$ 元 $C^\infty$ 函数构成的向量空间。令 $D_i=\partial/\partial t_i$ 为关于第 $i$ 个变量的偏导算子（$i=1,\ldots,n$）。则得到表示

$$
\rho:\mathbf{C}[X_1,\ldots,X_n]\to\operatorname{End}_{\mathbf{C}}(V),
$$

使得 $\rho(X_i)=D_i$。

**例。** 设 $H$ 是一个希尔伯特空间，$A$ 是 $H$ 上的一个有界厄米算子。**译校注：** 原文印为 “operator on $A$”；此处应为 “operator on $H$”，因为算子 $A$ 作用于希尔伯特空间 $H$。接着考虑从多项式环到 $H$ 的自同态代数的同态 $\mathbf{R}[X]\to\mathbf{R}[A]\subset\operatorname{End}(H)$，并将这个同态延拓到 $A$ 的谱上的连续函数代数。可参看我的《实分析与泛函分析》（*Real and Functional Analysis*），Springer Verlag，1993 年。

表示构成一个范畴，定义如下。从表示 $\rho:R\to\operatorname{End}_A(M)$ 到表示 $\rho':R\to\operatorname{End}_A(M')$ 的一个**态射**，换言之，**从 $R$ 的一个表示到另一个表示的同态**，定义为一个 $A$-模同态 $h:M\to M'$，使得对于每个 $\alpha\in R$，下面的图都是交换的：

![定义表示态射的交换图](/library/volume-86/diagrams/pdf-0140-representations.png)

当 $h$ 是同构时，可以用下面的交换图代替上图：

![以 h 作共轭的交换图](/library/volume-86/diagrams/pdf-0140-conjugation.png)

<span class="original-page-anchor" id="pdf-page-141" aria-hidden="true"></span>

其中符号 $[h]$ 表示由 $h$ 给出的共轭，即对于 $f\in\operatorname{End}_A(M)$，有 $[h]f=h\circ f\circ h^{-1}$。

**表示：从幺半群到幺半群代数。** 设 $G$ 是一个幺半群。所谓 **$G$ 在 $A$-模 $M$ 上的表示**，是指从 $G$ 到 $\operatorname{End}_A(M)$ 的乘法幺半群的同态 $\rho:G\to\operatorname{End}_A(M)$。于是可以将 $\rho$ 延拓为幺半群代数的一个同态

$$
A[G]\to\operatorname{End}_A(M),
$$

定义为

$$
\rho\left(\sum_{x\in G}a_xx\right)=\sum_{x\in G}a_x\rho(x).
$$

可以立即验证，$\rho$ 到 $A[G]$ 的这个延拓是一个环同态，它在 $G$ 的元素上与给定的 $\rho$ 一致。

**例：群环上的模。** 接下来的例子遵循一种与自同构群相联系的模式。一般地，假定有某个对象范畴，而且每个对象 $K$ 都对应一个阿贝尔群 $F(K)$，这种对应对同构具有函子性。这意味着，若 $\sigma:K\to K'$ 是一个同构，则存在对应的同构 $F(\sigma):F(K)\to F(K')$，使得 $F(\operatorname{id}_K)=\operatorname{id}_{F(K)}$，并且 $F(\sigma\tau)=F(\sigma)\circ F(\tau)$。**译校注：** 原页印为 $F(\operatorname{id}_K)=\operatorname{id}_{K'}$。函子必须把 $K$ 的恒等态射映为 $F(K)$ 的恒等态射，因此右端应为 $\operatorname{id}_{F(K)}$。于是，对象的自同构群 $\operatorname{Aut}(K)$ 作用于 $F(K)$；也就是说，有一个自然同态

$$
\operatorname{Aut}(K)\to\operatorname{Aut}(F(K)),\quad\text{由}\quad\sigma\mapsto F(\sigma)\quad\text{给出}。
$$

令 $G=\operatorname{Aut}(K)$。则与上面一样，可以使 $F(K)$（用加法记号）成为群环 $\mathbf{Z}[G]$ 上的一个模。给定元素 $\alpha=\sum a_\sigma\sigma\in\mathbf{Z}[G]$，其中 $a_\sigma\in\mathbf{Z}$，以及一个元素 $x\in F(K)$，我们定义

$$
\alpha x=\sum a_\sigma F(\sigma)x.
$$

定义模的条件显然满足。下面列出数学各领域中的若干具体情形，因此在术语使用上不作限制。

设 $K$ 是一个数域（即有理数域的一个有限扩张），$G$ 是它的自同构群。与 $K$ 相联系的对象有：

代数整数环 $\mathfrak{o}_K$；

可逆元群 $\mathfrak{o}_K^*$；

理想类群 $C(K)$；

单位根群 $\mu(K)$。

于是 $G$ 作用于上述每一个对象；一个问题是确定这些对象作为 $\mathbf{Z}[G]$-模的结构。仅仅对于分圆域，这种<span class="original-page-anchor" id="pdf-page-142" aria-hidden="true"></span>结构的确定，也已经产生了丰富的理论以及若干尚未解决的问题。

假定 $K$ 是 $k$ 的一个伽罗瓦扩张，伽罗瓦群为 $G$（见第 VI 章）。则可以把 $K$ 本身看成群环 $k[G]$ 上的一个模。在第 VI 章第 13 节，我们将证明，作为 $k[G]$ 上的模，$K$ 与 $k[G]$ 自身同构。

拓扑学中会考虑一个空间 $X_0$ 及其一个有限覆盖 $X$。于是 $\operatorname{Aut}(X/X_0)$ 作用于 $X$ 的同调，因此该同调是群环上的一个模。

再增加一些结构，假定 $X$ 是一个射影非奇异簇，例如定义在复数域上。则可以将以下对象与 $X$ 相联系：

除子类群（皮卡群）$\operatorname{Pic}(X)$；

给定维数中的闭链类群，或周群 $\operatorname{CH}^p(X)$；

$X$ 的普通同调；

一般的层上同调。

若 $X$ 定义在一个有理数域上的有限生成域 $K$ 上，我们还可以为它关联一种由 Grothendieck 用代数方法定义的、更精细的上同调，它对于伽罗瓦群的作用具有函子性。

于是，所有这些对象都可以看成自同构群的群环上的模；数学中的一些重大问题，就是确定它们的结构。这里向读者介绍两篇综述，其中含有大量参考文献。

[CCFT 91] P. CASSOU-NOGUES、T. CHINBURG、A. FRÖHLICH、M. J. TAYLOR：《L 函数与伽罗瓦模》（L-functions and Galois modules），载 J. Coates 和 M. J. Taylor 编《L 函数与算术》（*L-functions and Arithmetic*），1989 年 7 月达勒姆专题讨论会论文集（*Proceedings of the Durham Symposium*），伦敦数学会讲义丛书（*London Math. Soc. Lecture Note Series*）153，Cambridge University Press（1991），第 75-139 页。

[La 82] S. LANG：《数论与代数几何中的可逆元与类群》（Units and class groups in number theory and algebraic geometry），*Bull. AMS* **第 6 卷第 3 期**（1982），第 253-316 页。

## §3. 模的直积与直和

设 $A$ 是一个环，$\{M_i\}_{i\in I}$ 是一个模族。第 I 章第 9 节中，我们已将它们看成阿贝尔群并定义其直积。给定直积中的一个元素 $(x_i)_{i\in I}$，以及 $a\in A$，定义 $a(x_i)=(ax_i)$。换言之，我们逐分量地乘以元素 $a$。于是直积 $\prod M_i$ 是一个 $A$-模。读者可以立即验证，它也是 $A$-模范畴中的一个**直积**。

<span class="original-page-anchor" id="pdf-page-143" aria-hidden="true"></span>

类似地，设

$$
M=\bigoplus_{i\in I}M_i
$$

是它们作为阿贝尔群的直和。我们在 $M$ 上定义一个 $A$-模结构：若 $(x_i)_{i\in I}$ 是 $M$ 的一个元素，即一个由元素 $x_i\in M_i$ 构成的族，其中对几乎所有 $i$ 都有 $x_i=0$，且 $a\in A$，则定义

$$
a(x_i)_{i\in I}=(ax_i)_{i\in I},
$$

即逐分量定义乘以 $a$ 的运算。很容易验证，这是 $A$ 在 $M$ 上的一个作用，使 $M$ 成为 $A$-模。回顾阿贝尔群范畴中直和存在性的证明，就能立即看出，同样的证明也说明 $M$ 是模族 $\{M_i\}_{i\in I}$ 作为 $A$-模的直和。（例如，映射

$$
\lambda_j:M_j\to M
$$

满足 $\lambda_j(x)$ 的第 $j$ 个分量等于 $x$，而对 $i\ne j$，第 $i$ 个分量等于 $0$；现在可以看出，它是一个 $A$-同态。）

这个直和是 **$A$-模范畴中的余积**。事实上，读者可以立即验证，给定一个 $A$-同态族 $\{f_i:M_i\to N\}$，如同阿贝尔群证明中那样定义的映射 $f$，也是一个 $A$-同态，并且具有所需的性质。**译校注：** 原文将此处的 $f$ 称为 “$A$-isomorphism”。任意同态族所诱导的泛映射并不必然为同构，此处应为 “$A$-homomorphism”。参见第 I 章命题 7.1。

当 $I$ 是有限集时，有一个判定模为直积的有用准则。

**命题 3.1。** *设 $M$ 是一个 $A$-模，$n$ 是一个 $\geqq1$ 的整数。对于每个 $i=1,\ldots,n$，设 $\varphi_i:M\to M$ 是一个 $A$-同态，满足*

$$
\sum_{i=1}^n\varphi_i=\operatorname{id}\quad\text{以及}\quad\varphi_i\circ\varphi_j=0\quad\text{当 }i\ne j.
$$

*则对所有 $i$ 有 $\varphi_i^2=\varphi_i$。令 $M_i=\varphi_i(M)$，并设 $\varphi:M\to\prod M_i$ 满足*

$$
\varphi(x)=(\varphi_1(x),\ldots,\varphi_n(x)).
$$

*则 $\varphi$ 是从 $M$ 到直积 $\prod M_i$ 的一个 $A$-同构。*

*证明。* 对每个 $j$，有

$$
\varphi_j=\varphi_j\circ\operatorname{id}=\varphi_j\circ\sum_{i=1}^n\varphi_i=\varphi_j\circ\varphi_j=\varphi_j^2,
$$

从而证明了第一个断言。显然，$\varphi$ 是一个 $A$-同态。设 $x$ 在它的核中。由于

$$
x=\operatorname{id}(x)=\sum_{i=1}^n\varphi_i(x)
$$

<span class="original-page-anchor" id="pdf-page-144" aria-hidden="true"></span>

便可得出 $x=0$，因此 $\varphi$ 是单射。对于每个 $i=1,\ldots,n$，给定元素 $y_i\in M_i$，令 $x=y_1+\cdots+y_n$。显然，当 $i\ne j$ 时有 $\varphi_j(y_i)=0$。因此，对于每个 $j=1,\ldots,n$，都有

$$
\varphi_j(x)=y_j.
$$

这证明了 $\varphi$ 是满射，从而完成了命题的证明。

注意，当 $I$ 是有限集时，直和与直积相等。

与阿贝尔群一样，我们用符号 $\oplus$ 表示直和。

设 $M$ 是环 $A$ 上的一个模，$S$ 是 $M$ 的一个子集。所谓 $S$ 中元素的**线性组合**（系数在 $A$ 中），是指一个和

$$
\sum_{x\in S}a_xx,
$$

其中 $\{a_x\}$ 是 $A$ 中的一组元素，几乎所有元素都等于 $0$。这些元素 $a_x$ 称为线性组合的**系数**。设 $N$ 是 $S$ 中元素的所有线性组合构成的集合。则 $N$ 是 $M$ 的一个子模，因为若

$$
\sum_{x\in S}a_xx\quad\text{和}\quad\sum_{x\in S}b_xx
$$

是两个线性组合，则它们的和等于

$$
\sum_{x\in S}(a_x+b_x)x;
$$

若 $c\in A$，则

$$
c\left(\sum_{x\in S}a_xx\right)=\sum_{x\in S}ca_xx,
$$

这些元素仍然是 $S$ 中元素的线性组合。我们称 $N$ 为由 $S$ **生成**的子模，并称 $S$ 为 $N$ 的一组**生成元**。有时写作 $N=A\langle S\rangle$。若 $S$ 仅含一个元素 $x$，则由 $x$ 生成的模也记作 $Ax$，或简称 $(x)$；有时称 $(x)$ 为一个**主模**。

若一个模 $M$ 具有有限个生成元，则称 $M$ 是**有限生成的**，或称其在 $A$ 上是**有限型的**，或简称为**有限的**。

模 $M$ 的一个*子集* $S$ 称为（在 $A$ 上）**线性无关的**，如果每当有一个线性组合

$$
\sum_{x\in S}a_xx
$$

<span class="original-page-anchor" id="pdf-page-145" aria-hidden="true"></span>

等于 $0$ 时，对所有 $x\in S$ 都有 $a_x=0$。若 $S$ 线性无关，且两个线性组合

$$
\sum a_xx\quad\text{与}\quad\sum b_xx
$$

相等，则对于所有 $x\in S$ 都有 $a_x=b_x$。事实上，两式相减得到 $\sum(a_x-b_x)x=0$，从而对于所有 $x$ 都有 $a_x-b_x=0$。若 $S$ 线性无关，我们也说它的元素线性无关。类似地，$M$ 中元素的一个*族* $\{x_i\}_{i\in I}$ 称为线性无关的，如果每当有线性组合

$$
\sum_{i\in I}a_ix_i=0
$$

时，对所有 $i$ 都有 $a_i=0$。子集 $S$（相应地，族 $\{x_i\}$）称为**线性相关的**，如果它不是线性无关的，即存在关系

$$
\sum_{x\in S}a_xx=0\quad\text{相应地，}\quad\sum_{i\in I}a_ix_i=0,
$$

其中 $a_x$（相应地，$a_i$）不全为 $0$。**注意。** 设 $x$ 是 $M$ 的一个单独元素，并且线性无关。则当 $n>1$ 时，对所有 $i$ 都满足 $x_i=x$ 的族 $\{x_i\}_{i=1,\ldots,n}$ 是线性相关的；但仅由 $x$ 本身构成的集合是线性无关的。

设 $M$ 是一个 $A$-模，$\{M_i\}_{i\in I}$ 是一个子模族。由于有包含同态

$$
\lambda_i:M_i\to M,
$$

便有一个诱导同态

$$
\lambda_*:\bigoplus M_i\to M,
$$

对于任意除有限个元素外全部为 $0$ 的元素族 $(x_i)_{i\in I}$，它满足

$$
\lambda_*((x_i))=\sum_{i\in I}x_i.
$$

若 $\lambda_*$ 是一个同构，则称族 $\{M_i\}_{i\in I}$ 是 $M$ 的一个**直和分解**。显然，这等价于说 $M$ 的每一个元素都能唯一地表示为一个和

$$
\sum x_i,
$$

其中 $x_i\in M_i$，且几乎所有 $x_i=0$。在这种情况下，我们也滥用记号，写作

$$
M=\bigoplus M_i.
$$

<span class="original-page-anchor" id="pdf-page-146" aria-hidden="true"></span>

若族 $\{M_i\}$ 满足 $M$ 的每一个元素都可以表示为某个和 $\sum x_i$（不必唯一），则写作 $M=\sum M_i$。无论如何，对于任意子模族 $\{M_i\}$，上述同态 $\lambda_*$ 的像是 $M$ 的一个子模，将记作 $\sum M_i$。

若 $M$ 是一个模，$N,N'$ 是两个子模，满足 $N+N'=M$ 和 $N\cap N'=0$，则有模同构

$$
M\approx N\oplus N',
$$

这与阿贝尔群的情况相同；对于有限个子模，也有类似结论。

当然，只需将阿贝尔群看成 $\mathbf{Z}$ 上的模，就可看出我们关于阿贝尔群的讨论是关于模的讨论的一个特例。不过，通常似乎仍值得先对阿贝尔群建立一些命题，然后再指出这些命题（显然）对一般的模也成立，尽管这种做法效率不高。

设 $M,M',N$ 是模。则有阿贝尔群同构

![第一个方框中的 Hom 同构](/library/volume-86/diagrams/pdf-0146-hom-first.png)

类似地，有

![第二个方框中的 Hom 同构](/library/volume-86/diagrams/pdf-0146-hom-second.png)

第一个同构如下得到。若 $f:M\oplus M'\to N$ 是一个同态，则将 $f$ 分别与 $M$ 和 $M'$ 到其直和的单射复合，就得到同态 $f_1:M\to N$ 和同态 $f_2:M'\to N$：

$$
M\to M\oplus\{0\}\subset M\oplus M'\xrightarrow{f}N,
$$

$$
M'\to\{0\}\oplus M'\subset M\oplus M'\xrightarrow{f}N.
$$

我们将下面这个对应给出第一个方框中的同构的验证留给读者：

$$
f\mapsto(f_1,f_2).
$$

第二个方框中的同构也以类似方式得到。给定同态

$$
f_1:N\to M
$$

以及

$$
f_2:N\to M',
$$

<span class="original-page-anchor" id="pdf-page-147" aria-hidden="true"></span>

我们有同态 $f:N\to M\times M'$，定义为

$$
f(x)=(f_1(x),f_2(x)).
$$

很容易验证，对应

$$
(f_1,f_2)\mapsto f
$$

给出第二个方框中的同构。

当然，两个模的直和与直积同构；但为了体现函子性，并与无限情形相适应，我们在记号中区分了它们，见习题 22。

**命题 3.2。** *设 $0\to M'\xrightarrow{f}M\xrightarrow{g}M''\to0$ 是一个模的正合列。下列条件等价：*

**1.** *存在同态 $\varphi:M''\to M$，使得 $g\circ\varphi=\operatorname{id}$。*

**2.** *存在同态 $\psi:M\to M'$，使得 $\psi\circ f=\operatorname{id}$。*

*若这些条件满足，则有同构：*

$$
M=\operatorname{Im}f\oplus\operatorname{Ker}\psi,\qquad M=\operatorname{Ker}g\oplus\operatorname{Im}\varphi,
$$

$$
M\approx M'\oplus M''.
$$

*证明。* 将右侧的同态写出：

$$
M\underset{\varphi}{\overset{g}{\rightleftarrows}}M''\to0.
$$

设 $x\in M$。则

$$
x-\varphi(g(x))
$$

在 $g$ 的核中，因此 $M=\operatorname{Ker}g+\operatorname{Im}\varphi$。

这个和是直和，因为若

$$
x=y+z,
$$

其中 $y\in\operatorname{Ker}g$，$z\in\operatorname{Im}\varphi$，且 $z=\varphi(w)$、$w\in M''$，则作用 $g$ 得到 $g(x)=w$。因此 $w$ 由 $x$ 唯一确定，进而 $z$ 也由 $x$ 唯一确定。于是 $y$ 同样唯一确定，这就证明了这个和是直和。

关于正合列另一侧的论证类似，留作习题；两个条件的等价性也留作习题。当这些条件满足时，称命题 3.2 中的正合列**分裂**；也称 $\psi$ **分裂** $f$，$\varphi$ **分裂** $g$。

<span class="original-page-anchor" id="pdf-page-148" aria-hidden="true"></span>

### 阿贝尔范畴

环上模的理论中，许多内容只涉及箭头。事实上，所需的只是核与余核（商模）的概念。可以将一种特定的范畴概念公理化，使许多论证，尤其是本章使用的论证，在其中仍然成立。因此，我们现在给出这组公理；不过，为了保持具体性，本章开始的部分仍继续使用模的语言。读者应自行权衡，何时转入这个更一般的框架。

首先考虑一个范畴 $\mathfrak{A}$，使得对于 $\mathfrak{A}$ 的每一对对象 $E,F$，$\operatorname{Mor}(E,F)$ 都是一个阿贝尔群，并且满足下列两个条件：

**AB 1。** 态射的复合律是双线性的，并且存在一个零对象 $0$，即对于每个对象 $E$，$\operatorname{Mor}(0,E)$ 和 $\operatorname{Mor}(E,0)$ 都恰好只有一个元素。

**AB 2。** 范畴中存在有限积与有限余积。

此时称 $\mathfrak{A}$ 为一个**加性范畴**。

给定 $\mathfrak{A}$ 中的态射 $E\xrightarrow{f}F$，我们将 $f$ 的一个**核**定义为一个态射 $E'\to E$，使得对于范畴中的所有对象 $X$，下面的列都是正合的：

$$
0\to\operatorname{Mor}(X,E')\to\operatorname{Mor}(X,E)\to\operatorname{Mor}(X,F).
$$

我们将 $f$ 的一个**余核**定义为一个态射 $F\to F''$，使得对于范畴中的所有对象 $X$，下面的列都是正合的：

$$
0\to\operatorname{Mor}(F'',X)\to\operatorname{Mor}(F,X)\to\operatorname{Mor}(E,X).
$$

可以立即验证，核与余核在一个适当的范畴中是泛的，因此若存在，就在唯一同构的意义下唯一确定。

**AB 3。** 核与余核存在。

**AB 4。** 若 $f:E\to F$ 是一个核为 $0$ 的态射，则 $f$ 是其余核的核。若 $f:E\to F$ 是一个余核为 $0$ 的态射，则 $f$ 是其核的余核。核与余核都为 $0$ 的态射是一个同构。

满足上述四条公理的范畴 $\mathfrak{A}$ 称为**阿贝尔范畴**。

在阿贝尔范畴中，态射群通常记为 Hom，因此对于两个对象 $E,F$，我们写

$$
\operatorname{Mor}(E,F)=\operatorname{Hom}(E,F).
$$

这些态射通常称为**同态**。给定一个正合列

$$
0\to M'\to M,
$$

<span class="original-page-anchor" id="pdf-page-149" aria-hidden="true"></span>

我们称 $M'$ 为 $M$ 的一个**子对象**，或称从 $M'$ 到 $M$ 的同态为一个**单态射**。对偶地，在一个正合列

$$
M\to M''\to0
$$

中，我们称 $M''$ 为 $M$ 的一个**商对象**，或称从 $M$ 到 $M''$ 的同态为一个**满态射**，而不像在模范畴中那样说它是满射。虽然借助模与阿贝尔群的直观来构造证明很方便，但通常这些证明只涉及箭头的论证，因此也适用于任何阿贝尔范畴。不过，本书将遇到的所有阿贝尔范畴都有元素，核与余核也以一种与模的情况相近的自然方式定义，因此读者可以只关注这些具体情形。

**阿贝尔范畴的例子。** 当然，环上的模构成一个阿贝尔范畴，这是最常见的例子。诺特环上的有限生成模构成一个阿贝尔范畴，将在第 X 章中研究。

设 $k$ 是一个域。我们考虑二元组 $(V,A)$，其中 $V$ 是 $k$ 上的一个有限维向量空间，$A:V\to V$ 是一个自同态。这样的二元组之间的**同态**（**态射**）$f:(V,A)\to(W,B)$，是指一个 $k$-同态 $f:V\to W$，使得下面的图是交换的：

$$
\begin{array}{ccc}
V&\xrightarrow{f}&W\\
{\scriptstyle A}\downarrow&&\downarrow{\scriptstyle B}\\
V&\xrightarrow{f}&W
\end{array}
$$

按通常的方法即可验证，这些二元组及上述定义的态射构成一个阿贝尔范畴。第 XIV 章将研究其中的元素。

设 $k$ 是一个域，$G$ 是一个群。令 $\operatorname{Mod}_k(G)$ 为如下范畴：对象是 $k$ 上的有限维向量空间 $V$，带有 $G$ 在 $V$ 上的一个作用，即一个同态 $G\to\operatorname{Aut}_k(V)$。该范畴中的同态（态射）是一个 $k$-同态 $f:V\to W$，对所有 $x\in V$ 和 $\sigma\in G$ 满足 $f(\sigma x)=\sigma f(x)$。显然，$\operatorname{Mod}_k(G)$ 是一个阿贝尔范畴。第 XVIII 章将特别研究这个范畴。

第 XX 章第 1 节将考虑环上的模复形范畴。这个复形范畴是一个阿贝尔范畴。

在拓扑学与微分几何中，拓扑空间上的向量丛范畴是一个阿贝尔范畴。

**译校注：** 上一句忠实保留原书的断言，但它在一般情形下不成立。向量丛态射的秩可能随基空间中的点变化，其核和余核不一定仍是向量丛；因此通常的向量丛范畴不满足上述阿贝尔范畴公理。原文未说明所需的附加条件或预期的替代范畴，此处不擅自改写。

拓扑空间上的阿贝尔群层构成一个阿贝尔范畴，它将在第 XX 章第 6 节中定义。

<span class="original-page-anchor" id="pdf-page-150" aria-hidden="true"></span>

## §4. 自由模

设 $M$ 是环 $A$ 上的一个模，$S$ 是 $M$ 的一个子集。若 $S$ 非空、$S$ 生成 $M$，并且 $S$ 线性无关，则称 $S$ 为 $M$ 的一组**基**。若 $S$ 是 $M$ 的一组基，则特别地，当 $A\ne\{0\}$ 时有 $M\ne\{0\}$，且 $M$ 的每一个元素都可以唯一地表示为 $S$ 中元素的线性组合。类似地，设 $\{x_i\}_{i\in I}$ 是 $M$ 中元素的一个非空族。若它线性无关并生成 $M$，则称它为 $M$ 的一组**基**。

若 $A$ 是一个环，则作为自身上的模，$A$ 具有一组仅由单位元 $1$ 构成的基。

设 $I$ 是一个非空集合，对每个 $i\in I$，令 $A_i=A$，并将它看成一个 $A$-模。令

$$
F=\bigoplus_{i\in I}A_i.
$$

则 $F$ 具有一组基，由 $F$ 的元素 $e_i$ 构成；$e_i$ 的第 $i$ 个分量是 $A_i$ 的单位元，其余所有分量都等于 $0$。

所谓**自由模**，是指具有一组基的模，或零模。

**定理 4.1。** *设 $A$ 是一个环，$M$ 是 $A$ 上的一个模。设 $I$ 是一个非空集合，$\{x_i\}_{i\in I}$ 是 $M$ 的一组基。设 $N$ 是一个 $A$-模，$\{y_i\}_{i\in I}$ 是 $N$ 中元素的一个族。则存在唯一的同态 $f:M\to N$，使得对所有 $i$ 都有 $f(x_i)=y_i$。*

*证明。* 设 $x$ 是 $M$ 的一个元素。存在唯一的 $A$ 中元素族 $\{a_i\}_{i\in I}$，使得

$$
x=\sum_{i\in I}a_ix_i.
$$

我们定义

$$
f(x)=\sum a_iy_i.
$$

显然，$f$ 是一个满足所需条件的同态，并且是唯一的这样的同态，因为必有

$$
f(x)=\sum a_if(x_i).
$$

**推论 4.2。** *记号同定理，并假定 $\{y_i\}_{i\in I}$ 是 $N$ 的一组基。则同态 $f$ 是一个同构，即模同构。*

*证明。* 由对称性，存在唯一的同态

$$
g:N\to M,
$$

<span class="original-page-anchor" id="pdf-page-151" aria-hidden="true"></span>

使得对所有 $i$ 都有 $g(y_i)=x_i$，并且 $f\circ g$ 和 $g\circ f$ 分别是相应的恒等映射。

**推论 4.3。** *若两个模所具有的基的基数相等，则这两个模同构。*

*证明。* 显然。

我们将下列命题的证明留作习题。

设 $M$ 是 $A$ 上的一个自由模，基为 $\{x_i\}_{i\in I}$，从而

$$
M=\bigoplus_{i\in I}Ax_i.
$$

设 $\mathfrak{a}$ 是 $A$ 的一个双边理想。则 $\mathfrak{a}M$ 是 $M$ 的一个子模。每个 $\mathfrak{a}x_i$ 都是 $Ax_i$ 的一个子模。*有一个 $A$-模同构*

$$
\boxed{M/\mathfrak{a}M\approx\bigoplus_{i\in I}Ax_i/\mathfrak{a}x_i.}
$$

此外，作为 $A$-模，每个 $Ax_i/\mathfrak{a}x_i$ 都与 $A/\mathfrak{a}$ 同构。

*再假定 $A$ 交换。则 $A/\mathfrak{a}$ 是一个环。此外，$M/\mathfrak{a}M$ 是 $A/\mathfrak{a}$ 上的自由模，每个 $Ax_i/\mathfrak{a}x_i$ 也是 $A/\mathfrak{a}$ 上的自由模。若 $\bar x_i$ 是 $x_i$ 在典范同态*

$$
Ax_i\to Ax_i/\mathfrak{a}x_i
$$

*下的像，则单个元素 $\bar x_i$ 是 $Ax_i/\mathfrak{a}x_i$ 在 $A/\mathfrak{a}$ 上的一组基。*

读者应当很容易验证所有这些命题。现在设 $A$ 是任意交换环。若存在元素 $x\in M$，使得 $M=Ax$，则称模 $M$ 是**主模**。映射

$$
a\mapsto ax\quad(\text{其中 }a\in A)
$$

是从 $A$ 到 $M$ 的一个满射 $A$-模同态，其核为一个左理想 $\mathfrak{a}$，并诱导一个 $A$-模同构

$$
A/\mathfrak{a}\approx M.
$$

设 $M$ 是一个有限生成模，生成元为 $\{v_1,\ldots,v_n\}$。设 $F$ 是一个自由模，基为 $\{e_1,\ldots,e_n\}$。则存在唯一的满射同态 $f:F\to M$，使得 $f(e_i)=v_i$。$f$ 的核是一个子模 $M_1$。在某些条件下，$M_1$ 是有限生成的（参见第 X 章第 1 节关于诺特环的内容），于是这个过程可以继续下去。有关模的解消和同调的各章将系统地研究这个过程。

<span class="original-page-anchor" id="pdf-page-152" aria-hidden="true"></span>

当然，即使 $M$ 不是有限生成的，也可以使用任意指标集进行类似构造。事实上，设 $\{v_i\}$（$i\in I$）是一个生成元族。对每个 $i$，设 $F_i$ 是一个仅以单个元素 $e_i$ 为基的自由模，因此 $F_i\approx A$。如命题 3.1 中那样，令 $F$ 为模 $F_i$（$i\in I$）的直和。于是得到一个满射同态 $f:F\to M$，使得 $f(e_i)=v_i$。因此，**每一个模都是一个自由模的商模**。

如同第 I 章第 7 节对阿贝尔群所做的那样，我们也可以定义**由非空集合 $S$ 生成的、环 $A$ 上的自由模**。令 $A\langle S\rangle$ 为所有满足对几乎所有 $x\in S$ 都有 $\varphi(x)=0$ 的函数 $\varphi:S\to A$ 所构成的集合。若 $a\in A$ 且 $x\in S$，用 $ax$ 表示满足 $\varphi(x)=a$、对 $y\ne x$ 有 $\varphi(y)=0$ 的映射 $\varphi$。于是与阿贝尔群的情况一样，给定 $\varphi\in A\langle S\rangle$，存在元素 $a_i\in A$ 和 $x_i\in S$，使得

$$
\varphi=a_1x_1+\cdots+a_nx_n.
$$

可以立即验证，满足 $\delta_x(x)=1$、对 $y\ne x$ 有 $\delta_x(y)=0$ 的函数族 $\{\delta_x\}$（$x\in S$），构成 $A\langle S\rangle$ 的一组基。换言之，上述将 $\varphi$ 表示为 $\sum a_ix_i$ 的表达式是唯一的。当 $S$ 为群或幺半群 $G$ 时，也可以应用这个构造，由此得到第 II 章第 5 节中的群代数。

### 投射模

还有一类与自由模密切相关的重要的模，现在来讨论它。

设 $A$ 是一个环，$P$ 是一个模。下列性质等价，并定义了什么是**投射模** $P$。

**P 1。** 给定同态 $f:P\to M''$ 和满射同态 $g:M\to M''$，存在同态 $h:P\to M$，使下面的图交换。

$$
\begin{array}{ccccc}
&&P&&\\
&{\scriptstyle h}\swarrow&\downarrow{\scriptstyle f}&&\\
M&\xrightarrow{g}&M''&\longrightarrow&0
\end{array}
$$

**P 2。** 每个正合列 $0\to M'\to M''\to P\to0$ 都分裂。

**P 3。** 存在一个模 $M$，使得 $P\oplus M$ 是自由模；换言之，$P$ 是一个自由模的直和项。

**P 4。** 函子 $M\mapsto\operatorname{Hom}_A(P,M)$ 是正合的。

下面证明这四个条件的等价性。

<span class="original-page-anchor" id="pdf-page-153" aria-hidden="true"></span>

假定 **P 1** 成立。给定 **P 2** 中的正合列，在下图中考虑映射 $f=\operatorname{id}$：

$$
\begin{array}{ccccc}
&&P&&\\
&{\scriptstyle h}\swarrow&\downarrow{\scriptstyle\operatorname{id}}&&\\
M''&\longrightarrow&P&\longrightarrow&0
\end{array}
$$

于是 $h$ 给出正合列所需的分裂。

假定 **P 2** 成立。将 $P$ 表示为一个自由模的商（参见习题 1）：$F\to P\to0$；对此列应用 **P 2**，便得到所需的分裂，将 $F$ 表示为 $P$ 与某个模的直和。

假定 **P 3** 成立。由于 $\operatorname{Hom}_A(X\oplus Y,M)=\operatorname{Hom}_A(X,M)\oplus\operatorname{Hom}_A(Y,M)$，并且当 $F$ 是自由模时，$M\mapsto\operatorname{Hom}_A(F,M)$ 是正合函子，因此当 $P$ 是一个自由模的直和项时，$\operatorname{Hom}_A(P,M)$ 是正合的。这就证明了 **P 4**。

假定 **P 4** 成立。**P 1** 的证明留作习题。

**例。** 下一节将证明，域上的向量空间总是自由的，即具有一组基。在某些条件下，投射模是自由模，这是一个定理。第 7 节将证明，主理想整环上的有限生成投射模是自由模。第 X 章定理 4.4 将证明，局部环上的这样的模是自由模；第 XVI 章定理 3.8 将证明，局部环上的有限平坦模是自由模；第 XXI 章定理 3.7 将证明 Quillen-Suslin 定理：若 $A=k[X_1,\ldots,X_n]$ 是域 $k$ 上的多项式环，则 $A$ 上的每个有限投射模都是自由模。

投射模引出格罗滕迪克群。设 $A$ 是一个环。有限投射模的同构类构成一个幺半群。事实上，若 $P$ 是有限投射模，令 $[P]$ 表示其同构类。我们定义

$$
[P]+[Q]=[P\oplus Q].
$$

这个和与在相应同构类中选择的代表元 $P,Q$ 无关。定义幺半群的条件可以立即验证。相应的格罗滕迪克群记作 $K(A)$。

还可以加上一个进一步的等价关系：若存在有限自由模 $F$ 和 $F'$，使得 $P\oplus F$ 与 $P'\oplus F'$ 同构，则称 $P$ 与 $P'$ 等价。在这个等价关系下，我们得到另一个群，记作 $K_0(A)$。若 $A$ 是一个戴德金环（第 II 章第 1 节及习题 13-19），则可以证明，该群以一种自然的方式与理想类群 $\operatorname{Pic}(A)$（在第 II 章第 1 节中定义）同构。见习题 11、12、13。还有一个<span class="original-page-anchor" id="pdf-page-154" aria-hidden="true"></span>问题，就是对尽可能多的环，尽可能明确地确定 $K_0(A)$。当 $A$ 是一个数域的代数整数环时，代数数论会研究 $K_0(A)$。Quillen-Suslin 定理表明，若 $A$ 是上述多项式环，则 $K_0(A)$ 是平凡的。

当然，也可以对所有有限模进行类似的构造。令 $[M]$ 表示有限模 $M$ 的同构类，并将和定义为直和。于是，环上模的同构类构成一个幺半群，可以为这个幺半群关联其格罗滕迪克群。这种构造尤其应用于交换环。这一主题有许多变式。例如，参见 Bass 的《代数 K 理论》（*Algebraic K-theory*），Benjamin，1968 年。

格罗滕迪克群的定义还有如下变式。设 $F$ 是由环 $R$ 上有限模的同构类生成的自由阿贝尔群；也可以使用基数有界的模，以便我们所处理的是集合。在这个自由阿贝尔群中，令 $\Gamma$ 为由所有元素

$$
[M]-[M']-[M'']
$$

生成的子群，其中存在正合列 $0\to M'\to M\to M''\to0$。商群 $F/\Gamma$ 称为**格罗滕迪克群** $K(R)$。我们将在第 8 节以及第 XX 章第 3 节再次遇到这个群。注意，对于任意满足下列条件的模族，都可以构造类似的格罗滕迪克群：$M$ 属于这个模族，当且仅当 $M'$ 和 $M''$ 属于这个模族。若取有限投射模为该模族，则很容易看出，在这种情况下，格罗滕迪克群的两种定义一致。

## §5. 向量空间

域上的模称为**向量空间**。

**定理 5.1。** *设 $V$ 是域 $K$ 上的一个向量空间，并假定 $V\ne\{0\}$。设 $\Gamma$ 是 $V$ 在 $K$ 上的一组生成元，$S$ 是 $\Gamma$ 的一个线性无关子集。则存在 $V$ 的一组基 $\mathfrak{B}$，使得 $S\subset\mathfrak{B}\subset\Gamma$。*

*证明。* 令 $\mathfrak{T}$ 为如下集合：其元素为 $\Gamma$ 中包含 $S$ 且线性无关的子集 $T$。则 $\mathfrak{T}$ 非空（它包含 $S$），并且我们断言 $\mathfrak{T}$ 是归纳有序的。事实上，若 $\{T_i\}$ 是一个全序子集<span class="original-page-anchor" id="pdf-page-155" aria-hidden="true"></span>属于 $\mathfrak{T}$（按递增包含关系排列），则 $\bigcup T_i$ 仍然线性无关，并包含 $S$。由佐恩引理，取 $\mathfrak{T}$ 的一个极大元素 $\mathfrak{B}$。则 $\mathfrak{B}$ 线性无关。设 $W$ 是 $V$ 中由 $\mathfrak{B}$ 生成的子空间。若 $W\ne V$，则存在元素 $x\in\Gamma$，使得 $x\notin W$。此时 $\mathfrak{B}\cup\{x\}$ 线性无关，因为给定线性组合

$$
\sum_{y\in\mathfrak{B}}a_yy+bx=0,\qquad a_y,b\in K,
$$

必有 $b=0$，否则会得到

$$
x=-\sum_{y\in\mathfrak{B}}b^{-1}a_yy\in W.
$$

由构造可知，对于所有 $y\in\mathfrak{B}$ 都有 $a_y=0$，从而证明 $\mathfrak{B}\cup\{x\}$ 线性无关，这与 $\mathfrak{B}$ 的极大性矛盾。因此 $W=V$；又因为 $V\ne\{0\}$，$\mathfrak{B}$ 非空。这就证明了定理。

若 $V$ 是一个 $\ne\{0\}$ 的向量空间，则特别地，我们看到，$V$ 的任意线性无关元素集都可以扩充为一组基，并且可以从给定的生成元集中选出一组基。

**定理 5.2。** *设 $V$ 是域 $K$ 上的一个向量空间。则 $V$ 在 $K$ 上的任意两组基具有相同的基数。*

*证明。* 首先假定 $V$ 有一组只含有限个元素的基，记为 $\{v_1,\ldots,v_m\}$，$m\geqq1$。我们将证明，其他任何一组基也必有 $m$ 个元素。为此，只需证明：若 $w_1,\ldots,w_n$ 是 $V$ 中在 $K$ 上线性无关的元素，则 $n\leqq m$（然后利用对称性即可）。我们使用归纳法。存在 $K$ 中的元素 $c_1,\ldots,c_m$，使得

$$
w_1=c_1v_1+\cdots+c_mv_m,\tag{1}
$$

且某个 $c_i$，不妨设为 $c_1$，不等于 $0$。于是 $v_1$ 属于由 $w_1,v_2,\ldots,v_m$ 在 $K$ 上生成的空间，因此这个空间必等于 $V$ 本身。此外，$w_1,v_2,\ldots,v_m$ 线性无关：假定 $b_1,\ldots,b_m$ 是 $K$ 中的元素，满足

$$
b_1w_1+b_2v_2+\cdots+b_mv_m=0.
$$

若 $b_1\ne0$，则除以 $b_1$，可将 $w_1$ 表示为 $v_2,\ldots,v_m$ 的线性组合。将它从（1）中减去，就得到 $v_i$ 之间的一个线性相关关系，这是不可能的。因此 $b_1=0$；又因为 $v_i$ 线性无关，所有 $b_i$ 都必须为 $0$。

<span class="original-page-anchor" id="pdf-page-156" aria-hidden="true"></span>

归纳地假定，在适当重编号 $v_i$ 之后，已经找到 $w_1,\ldots,w_r$（$r<n$），使得

$$
\{w_1,\ldots,w_r,v_{r+1},\ldots,v_m\}
$$

是 $V$ 的一组基。将 $w_{r+1}$ 表示为线性组合

$$
w_{r+1}=c_1w_1+\cdots+c_rw_r+c_{r+1}v_{r+1}+\cdots+c_mv_m,\tag{2}
$$

其中 $c_i\in K$。这个关系中 $v_i$ 的系数不能全为 $0$，否则 $w_j$ 之间就会有一个线性相关关系。不妨设 $c_{r+1}\ne0$。用与上面类似的论证，可以将 $v_{r+1}$ 替换为 $w_{r+1}$，而仍得到 $V$ 的一组基。这意味着，可以重复这个过程直到 $r=n$，因此 $n\leqq m$，从而证明了定理。

无限基的一般情形留给读者作为习题。［*提示：* 利用如下事实：一组基中的有限个元素，包含在另一组基中的有限个元素生成的空间中。］

若向量空间 $V$ 有一组含有限个元素的基，设元素个数为 $m$，则称 $V$ 是**有限维的**，并称 $m$ 为其**维数**。根据定理 5.2，$m$ 就是 $V$ 的任意一组基的元素个数。若 $V=\{0\}$，则定义其维数为 $0$，并称 $V$ 为 $0$ 维的。我们将 “dimension”（维数）缩写为 “dim”；若为明确起见需指出域 $K$，则写成 “$\dim_K$”。

讨论域上的向量空间时，我们使用**子空间**和**商空间**，代替**子模**和**商模**。

**定理 5.3。** *设 $V$ 是域 $K$ 上的一个向量空间，$W$ 是一个子空间。则*

$$
\dim_K V=\dim_K W+\dim_K V/W.
$$

*若 $f:V\to U$ 是 $K$ 上向量空间的一个同态，则*

$$
\dim V=\dim\operatorname{Ker}f+\dim\operatorname{Im}f.
$$

*证明。* 第一个命题是第二个命题的特例，只需取 $f$ 为典范映射。设 $\{u_i\}_{i\in I}$ 是 $\operatorname{Im}f$ 的一组基，$\{w_j\}_{j\in J}$ 是 $\operatorname{Ker}f$ 的一组基。设 $\{v_i\}_{i\in I}$ 是 $V$ 中的一个元素族，满足对每个 $i\in I$ 都有 $f(v_i)=u_i$。我们断言

$$
\{v_i,w_j\}_{i\in I,j\in J}
$$

是 $V$ 的一组基。显然，这就能证明所需的结论。

<span class="original-page-anchor" id="pdf-page-157" aria-hidden="true"></span>

设 $x$ 是 $V$ 的一个元素。则存在 $K$ 中的元素 $\{a_i\}_{i\in I}$，几乎所有元素都为 $0$，使得

$$
f(x)=\sum_{i\in I}a_iu_i.
$$

因此 $f(x-\sum a_iv_i)=f(x)-\sum a_if(v_i)=0$。于是

$$
x-\sum a_iv_i
$$

在 $f$ 的核中，并且存在 $K$ 中的元素 $\{b_j\}_{j\in J}$，几乎所有元素都为 $0$，使得

$$
x-\sum a_iv_i=\sum b_jw_j.
$$

由此可知，$x=\sum a_iv_i+\sum b_jw_j$，因此 $\{v_i,w_j\}$ 生成 $V$。还需证明族 $\{v_i,w_j\}$ 线性无关。假定存在元素 $c_i,d_j$，使得

$$
0=\sum c_iv_i+\sum d_jw_j.
$$

作用 $f$ 得到

$$
0=\sum c_if(v_i)=\sum c_iu_i,
$$

从而所有 $c_i=0$。由此立即推出所有 $d_j=0$，因此族 $\{v_i,w_j\}$ 是 $V$ 在 $K$ 上的一组基，证毕。

**推论 5.4。** *设 $V$ 是一个向量空间，$W$ 是一个子空间。则*

$$
\dim W\leqq\dim V.
$$

*若 $V$ 有限维，且 $\dim W=\dim V$，则 $W=V$。*

*证明。* 显然。

## §6. 对偶空间与对偶模

设 $E$ 是交换环 $A$ 上的一个自由模。我们将 $A$ 看成自身上的秩为 $1$ 的自由模。所谓 $E$ 的**对偶模** $E^\vee$，是指模 $\operatorname{Hom}(E,A)$，其元素称为**泛函**。因此，$E$ 上的一个泛函就是一个 $A$-线性映射 $f:E\to A$。若 $x\in E$ 且 $f\in E^\vee$，有时用 $\langle x,f\rangle$ 表示 $f(x)$。固定 $x$，可以看出，符号 $\langle x,f\rangle$ 作为 $f\in E^\vee$ 的函数，对第二个变量是 $A$-线性的。因此 $x$ 诱导一个 $E^\vee$ 上的线性映射，这个映射为 $0$ 当且仅当 $x=0$。于是得到一个单射 $E\to E^{\vee\vee}$，它并不总是满射。

<span class="original-page-anchor" id="pdf-page-158" aria-hidden="true"></span>

设 $\{x_i\}_{i\in I}$ 是 $E$ 的一组基。对于每个 $i\in I$，令 $f_i$ 为满足 $f_i(x_j)=\delta_{ij}$ 的唯一泛函（换言之，当 $i=j$ 时取值 $1$，当 $i\ne j$ 时取值 $0$）。根据基的一般性质（定理 4.1），这样的线性映射存在。

**定理 6.1。** *设 $E$ 是交换环 $A$ 上的一个有限自由模，有限维数为 $n$。则 $E^\vee$ 也是自由模，并且 $\dim E^\vee=n$。若 $\{x_1,\ldots,x_n\}$ 是 $E$ 的一组基，$f_i$ 是满足 $f_i(x_j)=\delta_{ij}$ 的泛函，则 $\{f_1,\ldots,f_n\}$ 是 $E^\vee$ 的一组基。*

*证明。* 设 $f\in E^\vee$，令 $a_i=f(x_i)$（$i=1,\ldots,n$）。有

$$
f(c_1x_1+\cdots+c_nx_n)=c_1f(x_1)+\cdots+c_nf(x_n).
$$

因此 $f=a_1f_1+\cdots+a_nf_n$，可知 $f_i$ 生成 $E^\vee$。此外，它们线性无关，因为若

$$
b_1f_1+\cdots+b_nf_n=0,
$$

其中 $b_i\in A$，则将左侧在 $x_i$ 上求值，得到

$$
b_if_i(x_i)=0,
$$

从而对于所有 $i$ 都有 $b_i=0$。**译校注：** 原页此处印为 $b_i\in K$，但本定理的系数环是 $A$，且并未引入域 $K$；应为 $b_i\in A$。这就证明了定理。

给定定理中的一组基 $\{x_i\}$（$i=1,\ldots,n$），我们称基 $\{f_i\}$ 为**对偶基**。相对于这两组基，可以将 $E$ 的一个元素 $A$ 表示为坐标 $(a_1,\ldots,a_n)$，将 $E^\vee$ 的一个元素 $B$ 表示为坐标 $(b_1,\ldots,b_n)$，使得

$$
A=a_1x_1+\cdots+a_nx_n,\qquad B=b_1f_1+\cdots+b_nf_n.
$$

于是，用这些坐标表示，有

$$
\langle A,B\rangle=a_1b_1+\cdots+a_nb_n=A\cdot B,
$$

即通常的 $n$ 元组的点积。

**推论 6.2。** *当 $E$ 是有限维自由模时，将每个 $x\in E$ 对应到 $E^\vee$ 上的泛函 $f\mapsto\langle x,f\rangle$ 的映射 $E\to E^{\vee\vee}$，是从 $E$ 到 $E^{\vee\vee}$ 的一个同构。*

**译校注：** 原页此处印为 $x\in V$；这项推论讨论模 $E$ 及其双重对偶，且 $V$ 未在此定义，因此应为 $x\in E$。

*证明。* 注意，由于 $\{f_1,\ldots,f_n\}$ 是 $E^\vee$ 的一组基，根据定义，$\{x_1,\ldots,x_n\}$ 就是 $E$ 中的对偶基，因此 $E=E^{\vee\vee}$。

**定理 6.3。** *设 $U,V,W$ 是交换环 $A$ 上的有限自由模，并设*

$$
0\to W\xrightarrow{\lambda}V\xrightarrow{\varphi}U\to0
$$

*是一个 $A$-同态的正合列。则诱导的列*

$$
0\to\operatorname{Hom}_A(U,A)\to\operatorname{Hom}_A(V,A)\to\operatorname{Hom}_A(W,A)\to0,
$$

<span class="original-page-anchor" id="pdf-page-159" aria-hidden="true"></span>

*即*

$$
0\to U^\vee\to V^\vee\to W^\vee\to0
$$

*也是正合的。*

*证明。* 这是 **P 2** 的推论，因为自由模是投射模。

现在考虑专属于向量空间的一些性质，因为我们将取商空间。因此，假定所讨论的是域 $K$ 上的向量空间。

设 $V,V'$ 是两个向量空间，并假定给定映射

$$
V\times V'\to K,
$$

对于 $x\in V$ 和 $x'\in V'$，记为

$$
(x,x')\mapsto\langle x,x'\rangle.
$$

若对于每个 $x\in V$，函数 $x'\mapsto\langle x,x'\rangle$ 是线性的；并且类似地，对于每个 $x'\in V'$，函数 $x\mapsto\langle x,x'\rangle$ 是线性的，则称该映射为**双线性的**。若对于所有 $x'\in S'$ 都有 $\langle x,x'\rangle=0$，则称元素 $x\in V$ 与 $V'$ 的子集 $S'$ **正交**（或**垂直**）。反方向也作类似定义。显然，$V$ 中与 $S'$ 正交的元素构成 $V$ 的一个子空间。

我们将双线性映射的左侧**核**定义为 $V$ 中与 $V'$ 正交的子空间；右侧核的定义类似。

给定上述双线性映射

$$
V\times V'\to K,
$$

设 $W'$ 是其右侧核，$W$ 是其左侧核。设 $x'$ 是 $V'$ 的一个元素。则 $x'$ 通过规则 $x\mapsto\langle x,x'\rangle$ 给出 $V$ 上的一个泛函；显然，这个泛函只依赖于 $x'$ 模 $W'$ 的陪集。换言之，若 $x'_1\equiv x'_2\pmod{W'}$，则泛函 $x\mapsto\langle x,x'_1\rangle$ 与 $x\mapsto\langle x,x'_2\rangle$ 相等。因此得到同态

$$
V'\to V^\vee,
$$

根据定义，其核恰为 $W'$，从而得到一个单射同态

$$
0\to V'/W'\to V^\vee.
$$

由于来自 $V'$ 元素的所有泛函在 $W$ 上都为零，我们可以将它们看成 $V/W$ 上的泛函，即 $(V/W)^\vee$ 的元素。因此，实际上得到一个单射同态

$$
0\to V'/W'\to(V/W)^\vee.
$$

我们可以为同态

$$
g:V'\to V^\vee
$$

<span class="original-page-anchor" id="pdf-page-160" aria-hidden="true"></span>

使得对所有 $x\in V$ 与 $x'\in V'$，都有

$$
\langle x,x'\rangle=\langle x,g(x')\rangle.
$$

不过，通常可以用一个箭头来描述它，并称之为诱导映射或自然映射。给它另起一个名称，往往会使术语变得不必要地繁重。

**定理 6.4。** *设 $V\times V'\to K$ 为一个双线性映射，设 $W,W'$ 分别为它的左核与右核，并假设 $V'/W'$ 是有限维的。那么诱导同态 $V'/W'\to(V/W)^\vee$ 是一个同构。*

*证明。* 由对称性，我们有一个诱导同态

$$
V/W\to(V'/W')^\vee,
$$

它是单射。由于

$$
\dim(V'/W')^\vee=\dim V'/W',
$$

可知 $V/W$ 是有限维的。由上述单同态以及另一个单同态，即

$$
0\to V'/W'\to(V/W)^\vee,
$$

我们得到不等式

$$
\dim V/W\le\dim V'/W'
$$

和

$$
\dim V'/W'\le\dim V/W,
$$

因此两者的维数相等。于是这两个单同态也都是满射，因而都是同构，从而证明了定理。

**译校注：** 原文在这里说这两个同态“are surjective and inverse to each other”。所显示的两个同态分别为 $V/W\to(V'/W')^\vee$ 与 $V'/W'\to(V/W)^\vee$，源空间与目标空间并不彼此交换，因此它们不能直接说成互为逆映射。由有限维及维数相等，可以推出两者都是同构，这已足以证明定理；译文依此表述。

**注 1。** 定理 6.4 是第 I 章对偶性定理 9.2 在向量空间中的对应结果。

**注 2。** 设 $A$ 为一个交换环，$E$ 为一个 $A$-模。那么可以构造两种对偶：

$$
E^\wedge=\operatorname{Hom}(E,\mathbf Q/\mathbf Z),\quad\text{将 }E\text{ 看作阿贝尔群};
$$

$$
E^\vee=\operatorname{Hom}_A(E,A),\quad\text{将 }E\text{ 看作 }A\text{-模}.
$$

两者都称为**对偶**，通常用于不同的情境。例如，我们将在第 XIII 章中讨论 $E^\vee$，而在第 XX 章 §4 的内射模理论中讨论 $E^\wedge$。对偶模 $E^\vee$ 的一个例子见习题 11。若这两种对偶恰好同时出现，需要加以区分，则可把 $E^\wedge$ 称为 **Pontrjagin 对偶**。

<span class="original-page-anchor" id="pdf-page-161" aria-hidden="true"></span>

事实上，在拓扑群 $G$ 的理论中，从 $G$ 到 $\mathbf R/\mathbf Z$ 的连续同态构成的群，就是经典的 Pontrjagin 对偶，而且按传统记作 $G^\wedge$，因此我认为保留这一术语是适当的。

可以用其他自然的、同构于 $\mathbf R/\mathbf Z$ 的群来代替 $\mathbf R/\mathbf Z$。其中最常见的是绝对值为 $1$ 的复数构成的群，我们记作 $S^1$。它与 $\mathbf R/\mathbf Z$ 的同构由映射

$$
x\mapsto e^{2\pi ix}
$$

给出。

**注 3。** 满足 $V'=V$ 的双线性映射 $V\times V\to K$ 称为**双线性型**。若相应的映射

$$
V'\to V^\vee\quad\text{和}\quad V\to(V')^\vee
$$

都是同构，则称这个型为**非奇异的**。在第 XV 章中，我们将更详细地研究双线性映射与双线性型。第 XIII 章习题 33 也提供了一个很好的例子。

## §7. 主理想整环上的模

*在本节中，始终假设 $R$ 是一个主理想整环。除非另有说明，所有模都是 $R$-模，所有同态都是 $R$-同态。*

这里的定理将推广第 I 章中为阿贝尔群所证明的定理。我们也将指出，如何通过替换术语来调整第 I 章的证明，从而得到当前情形下的证明。

设 $F$ 为 $R$ 上的自由模，其一组基为 $\{x_i\}_{i\in I}$。那么 $I$ 的基数是唯一确定的，称为 $F$ 的**维数**。回顾一下，可以这样证明这一点：在 $R$ 中取一个素元素 $p$，并注意到 $F/pF$ 是域 $R/pR$ 上的向量空间，其维数恰为 $I$ 的基数。因此可以谈论 $R$ 上自由模的维数。

**定理 7.1。** *设 $F$ 为一个自由模，$M$ 为一个子模。那么 $M$ 是自由的，而且它的维数小于或等于 $F$ 的维数。*

*证明。* 为简单起见，我们在 $F$ 有一组有限基 $\{x_i\}$（$i=1,\ldots,n$）时给出证明。设 $M_r$ 为 $M$ 与 $(x_1,\ldots,x_r)$ 的交，后者是由 $x_1,\ldots,x_r$ 生成的模。那么 $M_1=M\cap(x_1)$ 是 $(x_1)$ 的一个子模，因此具有 $(a_1x_1)$ 的形式，其中 $a_1\in R$。所以 $M_1$ 要么为 $0$，要么是维数为 $1$ 的自由模。归纳地假设 $M_r$ 自由，且维数 $\le r$。设 $\mathfrak a$ 为所有满足以下条件的元素 $a\in R$ 构成的集合：存在元素 $x\in M$，可以写成

$$
x=b_1x_1+\cdots+b_rx_r+ax_{r+1},
$$

<span class="original-page-anchor" id="pdf-page-162" aria-hidden="true"></span>

其中 $b_i\in R$。那么 $\mathfrak a$ 显然是一个理想，而且是主理想；设它由元素 $a_{r+1}$ 生成。若 $a_{r+1}=0$，则 $M_{r+1}=M_r$，归纳步骤就完成了。若 $a_{r+1}\ne0$，取 $w\in M_{r+1}$，使得 $w$ 关于 $x_{r+1}$ 的系数为 $a_{r+1}$。若 $x\in M_{r+1}$，则 $x$ 关于 $x_{r+1}$ 的系数可被 $a_{r+1}$ 整除，所以存在 $c\in R$，使 $x-cw$ 属于 $M_r$。因此

$$
M_{r+1}=M_r+(w).
$$

另一方面，显然 $M_r\cap(w)$ 为 $0$，所以这个和是直和，从而证明了定理。（无限情形见附录 2，§2。）

**推论 7.2。** *设 $E$ 为一个有限生成模，$E'$ 为一个子模。那么 $E'$ 有限生成。*

*证明。* 可以把 $E$ 表示为有有限个生成元的自由模 $F$ 的商模：若 $v_1,\ldots,v_n$ 为 $E$ 的生成元，取具有基 $\{x_1,\ldots,x_n\}$ 的自由模 $F$，并把 $x_i$ 映为 $v_i$。$E'$ 在 $F$ 中的逆像是一个子模；根据定理，它是自由的，而且有限生成。因此 $E'$ 有限生成。利用诺特环与诺特模的简单性质，也可以得到这个结论。

若希望移用第 I 章的证明，则作如下定义。$R$ 上的 $1$ 维自由模称为**无限循环模**。无限循环模同构于作为自身上的模的 $R$。因此，无限循环模的每个非零子模都是无限循环模。第 I 章中对应于定理 7.1 的证明，无需进一步修改便可适用。

设 $E$ 为一个模。若对每个给定的 $x\in E$，都存在 $a\in R$、$a\ne0$，使得 $ax=0$，则称 $E$ 为**挠模**。**有限阿贝尔群**的推广是**有限生成挠模**。若存在 $a\in R$、$a\ne0$，使得 $ax=0$，则 $E$ 的元素 $x$ 称为**挠元**。

设 $E$ 为一个模。由 $E$ 的所有挠元构成的子模记为 $E_{\mathrm{tor}}$，称为 $E$ 的**挠子模**。若 $E_{\mathrm{tor}}=0$，则称 $E$ **无挠**。

**定理 7.3。** *设 $E$ 有限生成。那么 $E/E_{\mathrm{tor}}$ 是自由的。存在 $E$ 的一个自由子模 $F$，使 $E$ 为直和*

$$
E=E_{\mathrm{tor}}\oplus F.
$$

*这样的子模 $F$ 的维数是唯一确定的。*

*证明。* 首先证明 $E/E_{\mathrm{tor}}$ 无挠。若 $x\in E$，用 $\bar x$ 表示它模 $E_{\mathrm{tor}}$ 的剩余类。设 $b\in R$、$b\ne0$，满足 $b\bar x=0$。那么 $bx\in E_{\mathrm{tor}}$，所以存在 $c\in R$、$c\ne0$，使得 $cbx=0$。因此 $x\in E_{\mathrm{tor}}$，且 $\bar x=0$，从而证明了 $E/E_{\mathrm{tor}}$ 无挠。它也是有限生成的。

<span class="original-page-anchor" id="pdf-page-163" aria-hidden="true"></span>

现在假设 $M$ 为一个有限生成的无挠模。在给定的一组有限生成元 $\{y_1,\ldots,y_m\}$ 中，取 $M$ 的一个极大元素集 $\{v_1,\ldots,v_n\}$，使 $\{v_1,\ldots,v_n\}$ 线性无关。若 $y$ 为这些生成元之一，则存在不全为 $0$ 的元素 $a,b_1,\ldots,b_n\in R$，使得

$$
ay+b_1v_1+\cdots+b_nv_n=0.
$$

那么 $a\ne0$（否则便与 $v_1,\ldots,v_n$ 的线性无关性矛盾）。所以 $ay$ 属于 $(v_1,\ldots,v_n)$。因此，对每个 $j=1,\ldots,m$，都可找到 $a_j\in R$、$a_j\ne0$，使 $a_jy_j$ 属于 $(v_1,\ldots,v_n)$。令 $a=a_1\cdots a_m$ 为这些元素的乘积。那么 $aM$ 包含在 $(v_1,\ldots,v_n)$ 中，且 $a\ne0$。映射

$$
x\mapsto ax
$$

是一个单同态，它的像包含在一个自由模中。这个像同构于 $M$，由定理 7.1 可知 $M$ 是自由的，得到了所需结论。

为了得到子模 $F$，我们需要一个引理。

**引理 7.4。** *设 $E,E'$ 为模，并假设 $E'$ 自由。设 $f:E\to E'$ 为一个满同态。那么存在 $E$ 的一个自由子模 $F$，使得 $f$ 在 $F$ 上的限制诱导出 $F$ 与 $E'$ 的同构，而且 $E=F\oplus\operatorname{Ker}f$。*

*证明。* 设 $\{x'_i\}_{i\in I}$ 为 $E'$ 的一组基。对每个 $i$，取 $E$ 的一个元素 $x_i$，使 $f(x_i)=x'_i$。设 $F$ 为 $E$ 中由所有元素 $x_i$（$i\in I$）生成的子模。立即可以看出，元素族 $\{x_i\}_{i\in I}$ 线性无关，因此 $F$ 是自由的。给定 $x\in E$，存在元素 $a_i\in R$，使得

$$
f(x)=\sum a_ix'_i.
$$

于是 $x-\sum a_ix_i$ 属于 $f$ 的核，因此 $E=\operatorname{Ker}f+F$。显然 $\operatorname{Ker}f\cap F=0$，所以这个和是直和，从而证明了引理。

把该引理应用于定理 7.3 中的同态 $E\to E/E_{\mathrm{tor}}$，就得到分解 $E=E_{\mathrm{tor}}\oplus F$。$F$ 的维数是唯一确定的，因为对于定理中所述的 $E$ 的任意直和分解，$F$ 都同构于 $E/E_{\mathrm{tor}}$。

定理 7.3 中自由模 $F$ 的维数，称为 $E$ 的**秩**。

为了得到 $R$ 上有限生成模的结构定理，可以完全按阿贝尔群的情形来进行。我们将说明术语之间的对应关系，使我们可以移用证明而基本不作改变。

设 $E$ 为一个 $R$-模，$x\in E$。映射 $a\mapsto ax$ 是从 $R$ 到由 $x$ 生成的子模的满同态，其核是一个主理想，由某个元素 $m\in R$ 生成。我们称 $m$ 为 $x$ 的一个**周期**。我们<span class="original-page-anchor" id="pdf-page-164" aria-hidden="true"></span>注意到，$m$ 在相差一个可逆元倍数的意义下唯一确定（若 $m\ne0$）。若 $c\in R$、$c\ne0$，并满足 $cE=0$（分别为 $cx=0$），则称 $c$ 为 $E$（分别为 $x$）的一个**指数**。

设 $p$ 为一个素元素。我们用 $E(p)$ 表示 $E$ 的一个子模，它由所有具有某个指数 $p^r$（$r\ge1$）的元素 $x$ 构成。$E$ 的一个 $p$-子模，是指包含在 $E(p)$ 中的子模。

我们固定选取 $R$ 中素元素模可逆元的一套代表元。例如，若 $R$ 是域上的一元多项式环，则取首项系数为 $1$ 的不可约多项式作为代表元。

设 $m\in R$，$m\ne0$。映射 $x\mapsto mx$ 的核记为 $E_m$。它由 $E$ 中所有具有指数 $m$ 的元素构成。

若模 $E$ 对某个元素 $a\in R$ 同构于 $R/(a)$，则称 $E$ 为**循环模**。若 $a\ne0$，不失一般性，可以假设 $a$ 是我们选定的代表元系统中若干素元素的乘积，此时可以把 $a$ 称为这个模的阶。

设 $r_1,\ldots,r_s$ 为 $\ge1$ 的整数。若一个 $p$-模 $E$ 同构于循环模 $R/(p^{r_i})$（$i=1,\ldots,s$）的积，则称 $E$ 具有**型**

$$
(p^{r_1},\ldots,p^{r_s}).
$$

若 $p$ 固定，也可以说此模具有型 $(r_1,\ldots,r_s)$（相对于 $p$）。

第 I 章 §8 的全部证明现在都可以原样移用。凡是对正整数 $m$ 的大小进行论证的地方，都可以相应地对其素因子分解中素因子的数目进行论证。若处理的是素数幂 $p^r$，则可以认为阶由 $r$ 确定。读者现在可以检查，第 I 章 §8 的证明确实适用。

不过，我们仍将重新展开这一理论，而不假设读者了解第 I 章 §8 的内容。因此，这里的论述是自足的。

**定理 7.5。** *设 $E$ 为一个非零有限生成挠模。那么 $E$ 是直和*

$$
E=\bigoplus_p E(p),
$$

*其中遍历所有满足 $E(p)\ne0$ 的素元素 $p$。每个 $E(p)$ 都可以写成直和*

$$
E(p)=R/(p^{\nu_1})\oplus\cdots\oplus R/(p^{\nu_s}),
$$

*其中 $1\le\nu_1\le\cdots\le\nu_s$。序列 $\nu_1,\ldots,\nu_s$ 是唯一确定的。*

*证明。* 设 $a$ 为 $E$ 的一个指数，并假设 $a=bc$，其中 $(b,c)=(1)$。取 $x,y\in R$，使得

$$
1=xb+yc.
$$

<span class="original-page-anchor" id="pdf-page-165" aria-hidden="true"></span>

我们断言 $E=E_b\oplus E_c$。把 $a$ 表示为素元素幂的乘积，并利用归纳法，就可得到第一个断言。设 $v\in E$。那么

$$
v=xbv+ycv.
$$

由于 $cxbv=xav=0$，所以 $xbv\in E_c$。同样，$ycv\in E_b$。最后，立即可以看出 $E_b\cap E_c=0$。因此 $E$ 是 $E_b$ 与 $E_c$ 的直和。

现在必须证明，$E(p)$ 是所述形式的直和。若 $y_1,\ldots,y_m$ 为一个模的元素，并且只要有关系

$$
a_1y_1+\cdots+a_my_m=0
$$

（其中 $a_i\in R$），就必定对所有 $i$ 都有 $a_iy_i=0$，则称这些元素是**独立的**。（注意，**独立**并不意味着**线性无关**。）立即可以看出，$y_1,\ldots,y_m$ 独立，当且仅当模 $(y_1,\ldots,y_m)$ 具有由循环模 $(y_i)$（$i=1,\ldots,m$）组成的直和分解

$$
(y_1,\ldots,y_m)=(y_1)\oplus\cdots\oplus(y_m).
$$

现在我们有了引理 7.4 对于具有素元素幂指数的模的对应结果。

**引理 7.6。** *设 $E$ 为一个指数为 $p^r$（$r\ge1$）的挠模，其中 $p$ 是某个素元素。设 $x_1\in E$ 为周期为 $p^r$ 的元素。令 $\bar E=E/(x_1)$。设 $\bar y_1,\ldots,\bar y_m$ 为 $\bar E$ 的独立元素。那么对每个 $i$，都存在 $\bar y_i$ 的一个代表元 $y_i\in E$，使 $y_i$ 的周期与 $\bar y_i$ 的周期相同。元素 $x_1,y_1,\ldots,y_m$ 是独立的。*

*证明。* 设 $\bar y\in\bar E$ 的周期为 $p^n$，其中 $n\ge1$。设 $y$ 为 $\bar y$ 在 $E$ 中的一个代表元。那么 $p^ny\in(x_1)$，因此

$$
p^ny=p^scx_1,\qquad c\in R,\ p\nmid c,
$$

其中 $s\le r$。若 $s=r$，则可见 $y$ 与 $\bar y$ 的周期相同。若 $s<r$，则 $p^scx_1$ 的周期为 $p^{r-s}$，所以 $y$ 的周期为 $p^{n+r-s}$。必须有

$$
n+r-s\le r,
$$

因为 $p^r$ 是 $E$ 的一个指数。因此得到 $n\le s$，并且可以看出

$$
y-p^{s-n}cx_1
$$

是 $\bar y$ 的一个代表元，其周期为 $p^n$。

取 $\bar y_i$ 的一个具有相同周期的代表元 $y_i$。我们证明 $x_1,y_1,\ldots,y_m$ 独立。假设元素 $a,a_1,\ldots,a_m\in R$ 满足

$$
ax_1+a_1y_1+\cdots+a_my_m=0.
$$

<span class="original-page-anchor" id="pdf-page-166" aria-hidden="true"></span>

于是

$$
a_1\bar y_1+\cdots+a_m\bar y_m=0.
$$

根据假设，对每个 $i$ 都必须有 $a_i\bar y_i=0$。若 $\bar y_i$ 的周期为 $p^{r_i}$，则 $p^{r_i}$ 整除 $a_i$。由此可知，对每个 $i$ 都有 $a_iy_i=0$，最后得到 $ax_1=0$，从而证明了所需的独立性。

为了得到 $E(p)$ 的直和分解，首先注意到 $E(p)$ 有限生成。不失一般性，可以假设 $E=E(p)$。取 $E$ 的一个元素 $x_1$，其周期为 $p^{r_1}$，且 $r_1$ 最大。令 $\bar E=E/(x_1)$。我们断言，作为 $R/pR$ 上的向量空间，$\dim\bar E_p$ 严格小于 $\dim E_p$。事实上，若 $\bar y_1,\ldots,\bar y_m$ 是 $\bar E_p$ 中在 $R/pR$ 上线性无关的元素，则引理 7.6 蕴含 $\dim E_p\ge m+1$，因为总可以在 $(x_1)$ 中找到一个周期为 $p$、并与 $y_1,\ldots,y_m$ 独立的元素。因此 $\dim\bar E_p<\dim E_p$。我们可以用归纳法证明直和分解。若 $\bar E\ne0$，则存在元素 $\bar x_2,\ldots,\bar x_s$，周期分别为 $p^{r_2},\ldots,p^{r_s}$，且 $r_2\ge\cdots\ge r_s$。根据引理 7.6，存在 $E$ 中的代表元 $x_2,\ldots,x_s$，使 $x_i$ 的周期为 $p^{r_i}$，而且 $x_1,\ldots,x_s$ 独立。由于 $p^{r_1}$ 满足 $r_1$ 最大，所以 $r_1\ge r_2$，从而完成了所需的分解。

**译校注：** 原文在上述代表元及独立元素两处写作 $x_2,\ldots,x_r$ 和 $x_1,\ldots,x_r$。前文的商模元素为 $\bar x_2,\ldots,\bar x_s$，故这里的上界 $r$ 应为 $s$；译文依此更正。

唯一性将由一个更一般的唯一性定理推出，我们现在陈述该定理。

**定理 7.7。** *设 $E$ 为一个有限生成挠模，$E\ne0$。那么 $E$ 同构于非零因子的直和*

$$
R/(q_1)\oplus\cdots\oplus R/(q_r),
$$

*其中 $q_1,\ldots,q_r$ 为 $R$ 的非零不可逆元，且 $q_1\mid q_2\mid\cdots\mid q_r$。理想序列 $(q_1),\ldots,(q_r)$ 由上述条件唯一确定。*

*证明。* 利用定理 7.5，把 $E$ 分解为 $p$-子模的直和，设为 $E(p_1)\oplus\cdots\oplus E(p_l)$，再把每个 $E(p_i)$ 分解为周期为 $p_i^{r_{ij}}$ 的循环子模的直和。用下面的图可以象征性地表示这些数据：

$$
\begin{array}{ccccc}
E(p_1):&r_{11}&\le r_{12}&\le&\cdots\\
E(p_2):&r_{21}&\le r_{22}&\le&\cdots\\
\vdots&\vdots&\vdots&&\vdots\\
E(p_l):&r_{l1}&\le r_{l2}&\le&\cdots
\end{array}
$$

每一横行描述模相对于左端素元素的型。对每个固定的 $i=1,\ldots,l$，指数 $r_{ij}$ 按递增顺序排列。令 $q_1,\ldots,q_r$ 对应于指数矩阵的各列；换言之，

$$
\begin{aligned}
q_1&=p_1^{r_{11}}p_2^{r_{21}}\cdots p_l^{r_{l1}},\\
q_2&=p_1^{r_{12}}p_2^{r_{22}}\cdots p_l^{r_{l2}},\\
&\cdots
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-167" aria-hidden="true"></span>

第一列所表示的循环模的直和同构于 $R/(q_1)$，因为与阿贝尔群的情形相同，周期两两互素的循环模的直和仍是循环模。对每一列都有类似的结论，而且可以看到，我们的证明实际上把 $q_j$ 按整除关系的递增顺序排列，得到了所需结论。

现在证明唯一性。设 $p$ 为任意素元素，并假设 $E=R/(pb)$，其中 $b\in R$、$b\ne0$。那么由 $R$ 中的唯一分解性立即可知，$E_p$ 是子模 $bR/(pb)$。而复合映射

$$
R\to bR\to bR/(pb)
$$

的核恰为 $(p)$。因此有同构

$$
R/(p)\approx bR/(pb).
$$

现在设 $E$ 如定理所述，表示为 $r$ 项的直和。元素

$$
v=v_1\oplus\cdots\oplus v_r,\qquad v_i\in R/(q_i)
$$

属于 $E_p$，当且仅当对所有 $i$ 都有 $pv_i=0$。因此，$E_p$ 是各项中乘以 $p$ 的映射之核的直和。而 $E_p$ 是 $R/(p)$ 上的向量空间，所以其维数等于满足 $p$ 整除 $q_i$ 的项 $R/(q_i)$ 的数目。

假设 $p$ 为整除 $q_1$ 的素元素，因而对每个 $i=1,\ldots,r$，也整除 $q_i$。设 $E$ 有一个满足定理条件的 $s$ 项直和分解，即

$$
E=R/(q'_1)\oplus\cdots\oplus R/(q'_s).
$$

**译校注：** 原文在引出此分解时印作“$d$ terms”，但随后明确以 $s$ 为项数，并使用 $r\le s$；这里的 $d$ 应为 $s$，译文依此更正。

那么 $p$ 必须整除至少 $r$ 个元素 $q'_j$，所以 $r\le s$。由对称性，$r=s$，且对所有 $j$，$p$ 都整除 $q'_j$。

考虑模 $pE$。根据前面的一个结论，若写成 $q_i=pb_i$，则

$$
pE\approx R/(b_1)\oplus\cdots\oplus R/(b_r),
$$

而且 $b_1\mid\cdots\mid b_r$。有些 $b_i$ 可能是可逆元；但由归纳法，那些不可逆的 $b_i$ 所生成的主理想是唯一确定的。因此，若

$$
(b_1)=\cdots=(b_j)=1,
$$

而 $(b_{j+1})\ne(1)$，则理想序列

$$
(b_{j+1}),\ldots,(b_r)
$$

<span class="original-page-anchor" id="pdf-page-168" aria-hidden="true"></span>

是唯一确定的。这证明了我们的唯一性结论，并结束了定理 7.7 的证明。

理想 $(q_1),\ldots,(q_r)$ 称为 $E$ 的**不变量**。

定理 7.7 在线性代数中的一个主要应用，见第 XV 章 §2。

为使论述完整，我们加入下一个定理。它称为**初等因子定理**。

**定理 7.8。** *设 $F$ 为一个 $R$ 上的自由模，$M$ 为一个非零有限生成子模。那么存在 $F$ 的一组基 $\mathfrak B$、该基中的元素 $e_1,\ldots,e_m$，以及非零元素 $a_1,\ldots,a_m\in R$，使得：*

**(i)** *元素 $a_1e_1,\ldots,a_me_m$ 构成 $M$ 在 $R$ 上的一组基。*

**(ii)** *对 $i=1,\ldots,m-1$，有 $a_i\mid a_{i+1}$。*

*理想序列 $(a_1),\ldots,(a_m)$ 由上述条件唯一确定。*

*证明。* 把 $M$ 的一组有限生成元写为 $F$ 的一组基中有限个元素的线性组合。这些基元素生成一个有限秩自由子模，因此只需在 $F$ 有限秩时证明定理；以下假设如此。令 $n=\operatorname{rank}(F)$。

唯一性是定理 7.7 的推论。假设有一组满足定理条件的基。设 $a_1,\ldots,a_s$ 是可逆元，因而可取为 $1$；并设 $a_{s+j}=q_j$，其中不可逆元满足 $q_1\mid q_2\mid\cdots\mid q_r$。注意，$F/M=\bar F$ 是一个有限生成 $R$-模，具有直和表示

$$
F/M=\bar F\approx\bigoplus_{j=1}^r(R/q_jR)\bar e_{s+j}\oplus\text{秩为 }n-(r+s)\text{ 的自由模},
$$

其中横线表示 $F$ 的元素模 $M$ 的类。

**译校注：** 原式在上面直和中印作 $(R/q_jR)\bar e_j$。由于 $a_{s+j}=q_j$，相应的商模生成元应为 $\bar e_{s+j}$；前 $s$ 个 $a_i$ 都为可逆元，故 $\bar e_1,\ldots,\bar e_s$ 为零。译文将此下标更正为 $s+j$。

因此，$j=1,\ldots,r$ 上的直和就是 $\bar F$ 的挠子模，由定理 7.7 可知，元素 $q_1,\ldots,q_r$ 是唯一确定的。我们有 $r+s=m$，所以 $F/M$ 的秩为 $n-m$，从而唯一确定了 $m$。接着，$s=m-r$ 被唯一确定为 $a_1,\ldots,a_m$ 中可逆元的数目。这证明了定理的唯一性部分。下面证明存在性。

设 $\lambda$ 为 $F$ 上的一个泛函，即 $\operatorname{Hom}_R(F,R)$ 的一个元素。令 $J_\lambda=\lambda(M)$。那么 $J_\lambda$ 是 $R$ 的一个理想。选择 $\lambda_1$，使 $\lambda_1(M)$ 在理想集 $\{J_\lambda\}$ 中极大，即此集中不存在严格更大的理想。

设 $\lambda_1(M)=(a_1)$。那么 $a_1\ne0$，因为 $M$ 中存在一个非零元素；将它用 $F$ 的某组 $R$-基表示，必有某个非零坐标，取到该坐标的投影便得到一个在 $M$ 上取值不全为 $0$ 的泛函。取 $x_1\in M$，使 $\lambda_1(x_1)=a_1$。对任意泛函 $g$，都必须有 $g(x_1)\in(a_1)$［这直接由<span class="original-page-anchor" id="pdf-page-169" aria-hidden="true"></span>$\lambda_1(M)$ 的极大性得到］。用 $F$ 的任意一组基表示 $x_1$，可知它的系数都必须能被 $a_1$ 整除。（若某个系数不能被 $a_1$ 整除，则投影到此系数便得到一个不可能存在的泛函。）因此可以写成 $x_1=a_1e_1$，其中 $e_1\in F$。

接着证明 $F$ 是直和

$$
F=Re_1\oplus\operatorname{Ker}\lambda_1.
$$

由于 $\lambda_1(e_1)=1$，显然 $Re_1\cap\operatorname{Ker}\lambda_1=0$。此外，给定 $x\in F$，注意到 $x-\lambda_1(x)e_1$ 属于 $\lambda_1$ 的核。因此 $F$ 是上述两个子模的和，因而是它们的直和。

注意，$\operatorname{Ker}\lambda_1$ 是自由的，因为它是自由模的子模（定理 7.1）。令

$$
F_1=\operatorname{Ker}\lambda_1\quad\text{且}\quad M_1=M\cap\operatorname{Ker}\lambda_1.
$$

立即可见

$$
M=Rx_1\oplus M_1.
$$

因此 $M_1$ 是 $F_1$ 的一个子模，它的维数比 $M$ 的维数小 $1$。由 $\lambda_1(M)$ 的极大性条件，立即可知：对 $F_1$ 上的任意泛函 $\lambda$，像 $\lambda(M)$ 都包含在 $\lambda_1(M)$ 中（否则，泛函的一个适当线性组合将给出比 $(a_1)$ 更大的理想）。所以可以利用归纳法完成存在性的证明。

在定理 7.8 中，我们把理想 $(a_1),\ldots,(a_m)$ 称为 $M$ 在 $F$ 中的**不变量**。这些不变量的另一种刻画，见第 XIII 章命题 4.20。

**例。** 首先，在习题 5、7、8 中可见与定理 7.8 类似情形的例子；戴德金环的情形见习题 13。

**例。** 获得定理 7.8 中模 $M$ 的另一种方法，是将其视为关系模。设 $W$ 为一个有限生成 $R$-模，生成元为 $w_1,\ldots,w_n$。所谓 $\{w_1,\ldots,w_n\}$ 之间的一个**关系**，是指满足 $\sum a_iw_i=0$ 的元素 $(a_1,\ldots,a_n)\in R^n$。这样的关系所构成的集合是 $R^n$ 的一个子模，可以对它应用定理 7.8。

也可以把 $M$ 看作 $R^n$ 的子模，并应用行列运算的方法得到所需的基，从而给出定理 7.8 的证明。在这个背景下，我们作进一步的说明，以帮助理解定理 7.8。我们假设读者熟悉环上的矩阵。所谓**行运算**，是指：交换两行；将一行的某个倍数加到另一行；用环中的一个可逆元乘一行。**列运算**作类似定义。这些行列运算对应于乘以环上所谓的初等矩阵。

**定理 7.9。** *假设 $R$ 上的初等矩阵生成 $GL_n(R)$。设 $(x_{ij})$ 为元素取自 $R$ 的一个非零矩阵。那么经过有限次行列运算，可以把这个矩阵化为如下形式：*

<span class="original-page-anchor" id="pdf-page-170" aria-hidden="true"></span>

![矩阵的标准形，保留原书的全部对角元素、零及省略号](/library/volume-86/diagrams/pdf-0170-normal-form.png)

*其中 $a_1\cdots a_m\ne0$，且 $a_1\mid a_2\mid\cdots\mid a_m$。*

证明留给读者。可以把定理 7.9 看作与定理 7.8 等价，也可以给出直接证明。无论如何，定理 7.9 可用于以下情境。考虑一个线性方程组

$$
\begin{aligned}
c_{11}x_1+\cdots+c_{1n}x_n&=0\\
&\cdots\\
c_{r1}x_1+\cdots+c_{rn}x_n&=0,
\end{aligned}
$$

其中系数属于 $R$。设 $F$ 为 $R^n$ 中由该方程组的解向量 $X=(x_1,\ldots,x_n)$ 生成的子模。由定理 7.1 可知，$F$ 是维数 $\le n$ 的自由模。可以把定理 7.9 看作依照定理 7.8 为 $F$ 提供了一组规范化的基。

**另一个例子。** Paul Cohen 指出，行列运算方法也可以用于幂级数环 $\mathfrak o[[X]]$ 上的模，其中 $\mathfrak o$ 为一个完备离散赋值环。参见我的 *Cyclotomic Fields I and II*（Springer Verlag，1990）第 5 章定理 3.1。例如，可以取 $\mathfrak o$ 本身为域 $k$ 上的一元幂级数环 $k[[T]]$；但在上述参考文献的分圆域理论中，$\mathfrak o$ 取为 $p$ 进整数环。另一方面，George Bergman 提醒我注意 P. M. Cohn 的论文 “On the structure of $GL_2$ of a ring”，载于 *IHES Publ. Math.* 第 30 期（1966）；其中给出了某些主理想整环的例子，在这些环上不能使用定理 7.9 中的行列运算。

## §8. Euler–Poincaré 映射

本节可以看作给出了模的 Jordan–Hölder 定理的一个例子与应用。不过，正如下面的例子及参考文献所指出的，它也为进一步的理论提供了一个入口。

仍设 $A$ 为一个环。我们继续考虑 $A$-模。设 $\Gamma$ 为一个以加法记写的阿贝尔群。设 $\varphi$ 为一条规则，将某些模对应到 $\Gamma$ 的一个元素，并满足以下条件：

<span class="original-page-anchor" id="pdf-page-171" aria-hidden="true"></span>

*若 $0\to M'\to M\to M''\to0$ 正合，则 $\varphi(M)$ 有定义，当且仅当 $\varphi(M')$ 与 $\varphi(M'')$ 都有定义；此时有*

$$
\varphi(M)=\varphi(M')+\varphi(M'').
$$

*此外，$\varphi(0)$ 有定义，且等于 $0$。*

这样的规则 $\varphi$ 称为 $A$-模范畴上的 **Euler–Poincaré 映射**。若 $M'$ 同构于 $M$，则由正合列

$$
0\to M'\to M\to0\to0
$$

可知，只要 $\varphi(M)$ 有定义，$\varphi(M')$ 也有定义，且 $\varphi(M')=\varphi(M)$。因此，若对于模 $M$，$\varphi(M)$ 有定义，则 $\varphi$ 在 $M$ 的每个子模与商模上都有定义。特别地，若有模的正合列

$$
M'\to M\to M'',
$$

且 $\varphi(M')$ 与 $\varphi(M'')$ 都有定义，则 $\varphi(M)$ 也有定义；考虑这两个映射的核与像，并使用定义，立即可以看出这一点。

**例。** 可以取 $A=\mathbf Z$，并令 $\varphi$ 在所有有限阿贝尔群上有定义，且等于群的阶。$\varphi$ 的值属于正有理数的乘法群。

作为另一个例子，考虑域 $k$ 上的向量空间范畴。令 $\varphi$ 在有限维空间上有定义，且等于维数。那么 $\varphi$ 的值属于整数的加法群。

在第 XV 章中，我们将看到，特征多项式也可以看作一个 Euler–Poincaré 映射。

注意，从一个有限模到它在 §4 末尾所定义的 Grothendieck 群中的像的自然映射，是一个泛 Euler–Poincaré 映射。我们将在第 XX 章 §3 中更广泛地展开这个映射的理论。

若 $M$ 为一个模（环 $A$ 上），则子模序列

$$
M=M_1\supset M_2\supset\cdots\supset M_r=0
$$

也称为一个**有限滤过**，我们称 $r-1$ 为这个滤过的**长度**。

**译校注：** 原文此处写作“we call $r$ the length”。在所印的索引 $M_1,\ldots,M_r=0$ 下，相邻商因子共有 $r-1$ 个；为与下文定理 8.1 的可加长度一致，应为 $r-1$。译文依此更正。

若模 $M$ 除了 $0$ 和 $M$ 本身以外没有其他子模，且 $M\ne0$，则称 $M$ 为**单模**。若每个 $M_i/M_{i+1}$ 都是单模，则称滤过为**单滤过**。*Jordan–Hölder 定理断言，一个模的两个单滤过是等价的。*

若模 $M$ 为 $0$，或有一个单的（有限）滤过，则称 $M$ 为**有限长度**的模。根据模的 Jordan–Hölder 定理（证明与群的情形相同），这样的单滤过的长度是唯一确定的，称为**模的长度**。用欧拉特征的语言，可以把 Jordan–Hölder 定理改述如下：

<span class="original-page-anchor" id="pdf-page-172" aria-hidden="true"></span>

**定理 8.1。** *设 $\varphi$ 为一条规则，将每个单模对应到一个交换群 $\Gamma$ 中的元素，并且当 $M\approx M'$ 时，满足*

$$
\varphi(M)=\varphi(M').
$$

*那么 $\varphi$ 可以唯一地扩张为一个在所有有限长度模上有定义的 Euler–Poincaré 映射。*

*证明。* 给定一个单滤过

$$
M=M_1\supset M_2\supset\cdots\supset M_r=0,
$$

定义

$$
\varphi(M)=\sum_{i=1}^{r-1}\varphi(M_i/M_{i+1}).
$$

由 Jordan–Hölder 定理立即可知，这是良定的，而且 $\varphi$ 的这个扩张是一个 Euler–Poincaré 映射。

特别地，可以看出，长度函数就是取值于整数加法群的 Euler–Poincaré 映射，它在任何单模上的值均为 $1$。

## §9. 蛇引理

本节给出一个非常一般的引理，它将多次使用，因此我们在这里单独提出。读者可以暂且跳过本节，等遇到它时再读；不过，我们已经给出了一些展示其应用的习题：习题 15 中的五引理，以及习题 26。本书中的其他重要应用，将出现在第 XVI 章 §3 的张量积讨论中，以及第 XX 章关于复形、解消及导出函子的讨论中。

先作一些常规说明。考虑一个由模同态组成的交换图：

$$
\begin{array}{ccc}
M'&\xrightarrow{f}&M\\
{}_{d'}\downarrow&&\downarrow_{d}\\
N'&\xrightarrow{h}&N
\end{array}
$$

那么 $f$ 诱导出一个同态

$$
\operatorname{Ker}d'\to\operatorname{Ker}d.
$$

事实上，假设 $d'x'=0$。那么 $df(x')=0$，因为 $df(x')=hd'(x')=0$。

<span class="original-page-anchor" id="pdf-page-173" aria-hidden="true"></span>

同样，$h$ 自然地诱导出一个同态

$$
\operatorname{Coker}d'\to\operatorname{Coker}d,
$$

构造如下。取 $y'\in N'$，代表 $N'/d'M'$ 的一个元素。那么 $hy'$ 模 $dM$ 的类与代表给定元素的 $y'$ 的选取无关，因为若 $y''=y'+d'x'$，则

$$
hy''=hy'+hd'x'=hy'+dfx'\equiv hy'\bmod dM.
$$

因此得到映射

$$
h_*:N'/d'M'=\operatorname{Coker}d'\to N/dM=\operatorname{Coker}d,
$$

立即可以验证，它是一个同态。

在实际使用中，给定上述交换图，有时会用 $f$ 代替 $h$，于是图中上下两条水平映射都记为 $f$。这简化了记号，也不算不准确：可以将 $M',N'$ 看作一个直和的两个分量，对 $M,N$ 也作同样处理。那么 $f$ 只是一个从直和 $M'\oplus N'$ 到 $M\oplus N$ 的同态。

蛇引理涉及一个交换且正合的图，称为**蛇图**：

$$
\begin{array}{ccccccccc}
&&M'&\xrightarrow{f}&M&\xrightarrow{g}&M''&\longrightarrow&0\\
&&{}_{d'}\downarrow&&{}_{d}\downarrow&&{}_{d''}\downarrow&&\\
0&\longrightarrow&N'&\xrightarrow{f}&N&\xrightarrow{g}&N''&&
\end{array}
$$

设 $z''\in\operatorname{Ker}d''$。可以如下构造 $N'$ 的元素。由于 $g$ 是满射，存在元素 $z\in M$，使 $gz=z''$。现在沿 $d$ 竖直向下，取 $dz$。交换关系 $d''g=gd$ 表明 $gdz=0$，所以 $dz$ 属于 $N$ 中 $g$ 的核。根据正合性，存在元素 $z'\in N'$，使 $fz'=dz$。简略地记为

$$
z'=f^{-1}\circ d\circ g^{-1}z''.
$$

当然，由于取逆像时作了选择，$z'$ 并非良定的。不过，蛇引理将准确说明这里发生的事情。

**引理 9.1（蛇引理）。** *给定上述蛇图，由 $\delta z''=f^{-1}\circ d\circ g^{-1}z''$ 诱导的映射*

$$
\delta:\operatorname{Ker}d''\to\operatorname{Coker}d'
$$

*是良定的，而且有正合列*

$$
\operatorname{Ker}d'\to\operatorname{Ker}d\to\operatorname{Ker}d''\xrightarrow{\delta}\operatorname{Coker}d'\to\operatorname{Coker}d\to\operatorname{Coker}d''
$$

*其中除 $\delta$ 之外的映射都是自然映射。*

<span class="original-page-anchor" id="pdf-page-174" aria-hidden="true"></span>

*证明。* 按照通常的核查即可看出，$z'$ 模 $\operatorname{Im}d'$ 的类与取原像时所作的选择无关，从而定义了映射 $\delta$。接下来，证明这条序列的正合性也是例行的工作，其内容就是追逐交换图。希望培养对这类平凡论证的直觉的读者，应当亲自把它的全部细节补齐。作为一个例子，我们将证明

$$
\operatorname{Ker}\delta\subset\operatorname{Im}g_*,
$$

其中 $g_*$ 是在核上诱导的映射。假设 $z''$ 在 $\operatorname{Coker}d'$ 中的像为 $0$。按照定义，存在 $u'\in M'$，使得 $z'=d'u'$。由交换性，有

$$
dz=fz'=fd'u'=dfu'.
$$

因此

$$
d(z-fu')=0,
$$

故 $z-fu'$ 属于 $d$ 的核。但 $g(z-fu')=gz=z''$。这说明 $z''$ 属于 $g_*$ 的像，正如所需。其余各处正合性的证明都留给读者。

将核与余核补入原来的蛇形图，就得到下图（这也说明了这个引理名称的由来）：

![补全后的蛇形图](/library/volume-86/diagrams/pdf-0174-snake-completed.png)

## §10. 直极限与逆极限

我们回到极限这一话题，第一章中曾经讨论过群的极限。现在我们考虑其他范畴（环、模）中的极限，并指出，极限满足与第一章 §11 相一致的泛性质。

设 $I=\{i\}$ 是第一章 §10 中定义的有向指标系。设 $\mathfrak A$ 是一个范畴，$\{A_i\}$ 是 $\mathfrak A$ 中的一族对象。对于每一对满足下述条件的 $i,j$，<span class="original-page-anchor" id="pdf-page-175" aria-hidden="true"></span>$i\leqq j$，假设给定态射

$$
f_j^i:A_i\to A_j,
$$

使得每当 $i\leqq j\leqq k$ 时，都有

$$
f_k^j\circ f_j^i=f_k^i\qquad\text{且}\qquad f_i^i=\operatorname{id}.
$$

这样的一族称为**有向态射族**。族 $\{f_j^i\}$ 的一个**直极限**是下述范畴 $\mathfrak C$ 中的泛对象。$\operatorname{Ob}(\mathfrak C)$ 由形如 $(A,(f^i))$ 的对组成，其中 $A\in\operatorname{Ob}(\mathfrak A)$，而 $(f^i)$ 是一族态射 $f^i:A_i\to A$，$i\in I$，并且对所有 $i\leqq j$，下图均交换：

![直极限的锥](/library/volume-86/diagrams/pdf-0175-direct-cone.png)

（这里的“泛”当然指泛排斥。）

因此，若 $(A,(f^i))$ 是直极限，而 $(B,(g^i))$ 是上述范畴中的任意对象，则存在唯一的态射 $\varphi:A\to B$，使下图交换：

![直极限的泛性质](/library/volume-86/diagrams/pdf-0175-direct-universal.png)

为简便起见，通常写成

$$
A=\varinjlim_i A_i,
$$

在记号中省略 $f_j^i$。

**定理 10.1。** *在阿贝尔群范畴中，或者更一般地，在一个环上的模范畴中，直极限总是存在的。*

*证明。* 设 $\{M_i\}$ 是一个环上的模的有向系。令 $M$ 为这些模的直和。令 $N$ 为由所有形如下式的元素生成的子模：

$$
x_{ij}=(\ldots,0,x,0,\ldots,-f_j^i(x),0,\ldots),
$$

<span class="original-page-anchor" id="pdf-page-176" aria-hidden="true"></span>

其中，对于给定的一对满足 $j\geqq i$ 的指标 $(i,j)$，$x_{ij}$ 在 $M_i$ 中的分量为 $x$，在 $M_j$ 中的分量为 $f_j^i(x)$，其余位置的分量均为 $0$。

**译校注：** 原书此处印作“$f_j^i(x)$ in $M_j$”；上一页对 $x_{ij}$ 的定义明确给出的该分量是 $-f_j^i(x)$。因此，这里的分量应为 $-f_j^i(x)$，原句漏印了负号。

现在留给读者核查：商模 $M/N$ 是一个直极限，其中从 $M_i$ 到 $M/N$ 的映射是由复合同态

$$
M_i\to M\to M/N
$$

得到的自然映射。

**例。** 设 $X$ 是拓扑空间，$x\in X$。$x$ 的各个开邻域按照包含关系组成一个有向系。事实上，给定两个开邻域 $U$ 和 $V$，$U\cap V$ 也是一个开邻域，并且包含于 $U$ 和 $V$ 两者之中。在层论中，我们对每个 $U$ 指定一个阿贝尔群 $A(U)$，并对每一对 $U\supset V$ 指定同态 $h_V^U:A(U)\to A(V)$，使得若 $U\supset V\supset W$，则 $h_W^V\circ h_V^U=h_W^U$。这样，这些同态就组成一个有向族。直极限

$$
\varinjlim_U A(U)
$$

称为点 $x$ 处的**茎**。我们将在第二十章 §6 中给出阿贝尔群层的正式定义。至于进一步的阅读，我至少推荐两项参考文献。首先是 Hartshorne 的 *Algebraic Geometry*（《代数几何》），Springer Verlag，1977 年，其中第二章给出了自足的简短介绍。（请完成该节关于层的全部习题。）这一节仅有五页。其次，我推荐 Gunning 的 *Introduction to Holomorphic Functions of Several Variables*（《多复变量全纯函数导论》），Wadsworth and Brooks/Cole，1990 年中的论述。

现在我们把箭头反向，以定义逆极限。我们仍给定有向集 $I$ 和一族对象 $A_i$。若 $j\geqq i$，这次给定态射

$$
f_i^j:A_j\to A_i,
$$

并在 $j\geqq i$ 且 $i\geqq k$ 时满足关系

$$
f_k^i\circ f_i^j=f_k^j\qquad\text{且}\qquad f_i^i=\operatorname{id}.
$$

与直极限的情形一样，我们可以定义一个对象为 $(A,f_i)$ 的范畴，其中 $f_i:A\to A_i$，并且对于所有 $i,j$，下图均交换：

![逆极限的锥](/library/volume-86/diagrams/pdf-0176-inverse-cone.png)

这个范畴中的一个泛对象称为系 $(A_i,f_i^j)$ 的一个**逆极限**。

<span class="original-page-anchor" id="pdf-page-177" aria-hidden="true"></span>

和前面一样，我们常说

$$
A=\varprojlim_i A_i
$$

是逆极限，并在记号中省略 $f_j^i$。

**定理 10.2。** *在群范畴、一个环上的模范畴以及环范畴中，逆极限总是存在的。*

*证明。* 例如，设 $\{G_i\}$ 是一个有向群族，$\Gamma$ 是按第一章 §10 中的定义得到的逆极限。令 $p_i:\Gamma\to G_i$ 为投影（它是直积投影的限制，因为 $\Gamma$ 是 $\prod G_i$ 的子群）。例行核查即可证明，这些数据给出了群范畴中的一个逆极限。同样的构造也适用于环范畴和模范畴。

**例。** 设 $p$ 为素数。对于 $n\geqq m$，存在典范的满射环同态

$$
f_m^n:\mathbf Z/p^n\mathbf Z\to\mathbf Z/p^m\mathbf Z.
$$

相应的射影极限称为 **$p$ 进整数环**，记作 $\mathbf Z_p$。关于把这个环视作完备离散赋值环的讨论，参见习题 17 和第十二章。

设 $k$ 为域。单变量幂级数环 $k[[T]]$ 可以看作多项式商环 $k[T]/(T^n)$ 的逆极限，其中对于 $n\geqq m$，存在典范环同态

$$
f_m^n:k[T]/(T^n)\to k[T]/(T^m).
$$

类似的说明也适用于多变量幂级数。

更一般地，设 $R$ 为交换环，$J$ 为真理想。若 $n\geqq m$，则有典范环同态

$$
f_m^n:R/J^n\to R/J^m.
$$

令 $\bar R_J=\varprojlim R/J^n$ 为逆极限。那么，$R$ 有一个到 $\bar R_J$ 的自然同态。若 $R$ 是诺特局部环，由克鲁尔定理（第十章定理 5.6）可知 $\bigcap J^n=\{0\}$，所以 $R$ 到其完备化中的自然同态是嵌入。这个构造特别常用于 $J$ 是极大理想的情形。它给出了全纯函数概念的一个代数版本，理由如下。

设 $R$ 为交换环，$J$ 为真理想。把满足下述条件的 $R$ 中元素的序列 $\{x_n\}$ 定义为一个 **$J$ 柯西序列**：给定正整数 $k$，存在 $N$，使得对所有 $n,m\geqq N$，都有 $x_n-x_m\in J^k$。把满足如下条件的序列定义为**零序列**：给定 $k$，存在 $N$，使得对所有 $n\geqq N$，都有 $x_n\in J^k$。定义序列的加法与乘<span class="original-page-anchor" id="pdf-page-178" aria-hidden="true"></span>法为逐项进行。那么，柯西序列组成一个环 $\mathfrak C$，零序列组成一个理想 $\mathfrak N$，商环 $\mathfrak C/\mathfrak N$ 称为 $R$ 的 **$J$ 进完备化**。作为练习，请证明这些陈述，并证明存在自然同构

$$
\mathfrak C/\mathfrak N\approx\varprojlim R/J^n.
$$

因此，逆极限 $\varprojlim R/J^n$ 也称为 $J$ 进完备化。关于域上的绝对值背景下的完备化，参见第十二章。

**例。** 在某些情形中，我们希望判定一个多项式方程系 $f(X_1,\ldots,X_n)=0$ 是否有解，其中系数位于幂级数环 $k[[T]]$ 中，例如位于单变量幂级数环中。一种方法是考虑环模 $(T^N)$ 的商；这时，这个方程就相当于关于各个系数的有限个方程。于是，$f(X)=0$ 的一个解可以看作截断解的逆极限。这种方法的一个早期例子见 [La 52]；推广到多变量的情形见 [Ar 68]。

[La 52] S. LANG，On quasi algebraic closure（论拟代数闭性），*Ann of Math.* **55**（1952），第 373–390 页。

[Ar 68] M. ARTIN，On the solutions of analytic equations（论解析方程的解），*Invent. Math.* **5**（1968），第 277–291 页。

另见第十二章 §7。

在岩泽理论中，我们考虑数域 $k$ 上的一列伽罗瓦循环扩张 $K_n$，其次数为 $p^n$，其中 $p$ 为素数，且 $K_n\subset K_{n+1}$。令 $G_n$ 为 $K_n$ 在 $k$ 上的伽罗瓦群。然后，按照 Iwasawa 与 Serre 的做法，取群环 $(\mathbf Z/p^n\mathbf Z)[G_n]$ 的逆极限。参见我的 *Cyclotomic Fields*（《分圆域》）第 5 章。在这样的域塔中，也可以考虑 §1 末尾各例中所述的模的射影极限。具体而言，考虑 $p^n$ 次单位根群 $\boldsymbol\mu_{p^n}$，并令 $K_n=\mathbf Q(\boldsymbol\mu_{p^{n+1}})$，其中 $K_0=\mathbf Q(\boldsymbol\mu_p)$。我们令

$$
T_p(\boldsymbol\mu)=\varprojlim\boldsymbol\mu_{p^n},
$$

所用的同态是由 $\zeta\mapsto\zeta^p$ 给出的 $\boldsymbol\mu_{p^{n+1}}\to\boldsymbol\mu_{p^n}$。于是，$T_p(\boldsymbol\mu)$ 成为这些群环的射影极限上的一个模。类似地，也可以对 §1 末尾各例给出的每一个模考虑其逆极限。（参见习题 18。）确定这些逆极限的结构，会引出数论与代数几何中的基本问题。

举过这些基础代数之外的实际例子之后，我们回到关于逆极限的一些一般性讨论。

设 $(A_i,f_i^j)=(A_i)$ 和 $(B_i,g_i^j)=(B_i)$ 是两个阿贝尔群的逆系，它们使用同一个指标集。一个**同态** $(A_i)\to(B_i)$ 自然就是一族同态

$$
h_i:A_i\to B_i,
$$

<span class="original-page-anchor" id="pdf-page-179" aria-hidden="true"></span>

对每个 $i$ 都给定这样一个同态，并且这些同态与逆系中的映射交换：

![逆系的同态](/library/volume-86/diagrams/pdf-0179-inverse-morphism.png)

若对每个 $i$，对应的群序列都正合，则称序列

$$
0\to(A_i)\to(B_i)\to(C_i)\to0
$$

是**正合的**。

设 $(A_n)$ 是集合的一个逆系；为简便起见，使用正整数作为指标，并有连接映射

$$
u_{m,n}:A_m\to A_n\quad\text{其中}\quad m\geqq n.
$$

如果对每个 $n$，递减序列 $u_{m,n}(A_m)$（$m\geqq n$）最终稳定，也就是说，当 $m$ 足够大时保持不变，则称这个逆系满足 **Mittag-Leffler 条件 ML**。当对所有 $m,n$，$u_{m,n}$ 都是满射时，这一条件成立。

我们指出，逆极限函子显然是左正合的，即给定正合列

$$
0\to(A_n)\to(B_n)\to(C_n)\to0,
$$

则

$$
0\to\varprojlim A_n\to\varprojlim B_n\to\varprojlim C_n
$$

是正合列。

**命题 10.3。** *假设 $(A_n)$ 满足 ML。给定逆系的正合列*

$$
0\to(A_n)\to(B_n)\xrightarrow{g}(C_n)\to0,
$$

*则*

$$
0\to\varprojlim A_n\to\varprojlim B_n\to\varprojlim C_n\to0
$$

*是正合列。*

*证明。* 唯一需要证明的是最右边映射的满射性。设 $(c_n)$ 是逆极限中的一个元素。每个原像 $g^{-1}(c_n)$ 都是 $A_n$ 的一个陪集，因而与 $A_n$ 之间存在双射。这些原像组成一个逆系，而 $(A_n)$ 的 ML 条件蕴含 $(g^{-1}(c_n))$ 的 ML 条件。令 $S_n$ 为稳定子集

$$
S_n=\bigcap_{m\geqq n}u_{m,n}^B(g^{-1}(c_m)).
$$

<span class="original-page-anchor" id="pdf-page-180" aria-hidden="true"></span>

于是，逆系 $(S_n)$ 中的连接映射都是满射，所以其逆极限中存在一个元素 $(b_n)$。显然，$g$ 将这个元素映到给定的 $(c_n)$，命题的证明由此结束。

**命题 10.4。** *设 $(C_n)$ 是满足 ML 的阿贝尔群逆系，$(u_{m,n})$ 是它的连接映射系。那么有正合列*

$$
0\to\varprojlim C_n\to\prod C_n\xrightarrow{1-u}\prod C_n\to0.
$$

*证明。* 对每个正整数 $N$，我们有含有限乘积的正合列

$$
0\to\lim_{1\leqq n\leqq N}C_n\to\prod_{n=1}^N C_n\xrightarrow{1-u}\prod_{n=1}^N C_n\to0.
$$

**译校注：** 原书把最右侧乘积印成 $\prod_{n=1}^N C_n$。此有限序列的正确形式应是

$$
0\to\varprojlim_{1\leqq n\leqq N}C_n\to\prod_{n=1}^N C_n\xrightarrow{1-u}\prod_{n=1}^{N-1}C_n\to0,
$$

其中最后一个映射的第 $n$ 个分量为 $c_n-u_{n+1,n}c_{n+1}$（$1\leqq n<N$）。原式在 $N=1$ 时已不能正合：有限左移 $u$ 是零映射，$1-u$ 为恒等映射，其核为零，而左端有限逆极限为 $C_1$。把目标乘积的上限改为 $N-1$ 后，核正好是相容元素列，且该映射可从末端递推求原像，从而为满射。

映射 $u$ 是自然映射，它作用在向量上的方式为

$$
(0,\ldots,0,c_m,0,\ldots,0)\mapsto(0,\ldots,0,u_{m,m-1}c_m,0,\ldots,0).
$$

立即可见，这个序列是正合的。无限乘积是关于 $N$ 所取的逆极限。假设立即蕴含左端的逆极限满足 ML，因此我们可以应用命题 10.3 来完成证明。

## 习题

**1.** 设 $V$ 是域 $K$ 上的向量空间，$U,W$ 是子空间。证明

$$
\dim U+\dim W=\dim(U+W)+\dim(U\cap W).
$$

**2.** 将定理 5.2 中关于维数的陈述推广到非零交换环上的自由模。［*提示：* 回想对自由阿贝尔群如何证明类似的陈述，并用一个极大理想代替素数。］

**3.** 设 $R$ 是包含域 $k$ 作为子环的整环。假设在环的乘法所给出的作用下，$R$ 是 $k$ 上的有限维向量空间。证明 $R$ 是域。

**4. 直和。**

(a) 详细证明命题 3.2 中给出的序列分裂的各条件等价。证明序列 $0\to M'\xrightarrow{f}M\xrightarrow{g}M''\to0$ 分裂，当且仅当存在 $M$ 的子模 $N$，使得 $M$ 等于直和 $\operatorname{Im}f\oplus N$；并证明，若如此，则 $N$ 同构于 $M''$。补齐命题 3.2 证明中的全部细节。

<span class="original-page-anchor" id="pdf-page-181" aria-hidden="true"></span>

(b) 设 $E$ 和 $E_i$（$i=1,\ldots,m$）是某环上的模。设 $\varphi_i:E_i\to E$ 和 $\psi_i:E\to E_i$ 是具有下列性质的同态：

$$
\psi_i\circ\varphi_i=\mathrm{id},\qquad \psi_i\circ\varphi_j=0\quad\text{若 }i\ne j,
$$

$$
\sum_{i=1}^{m}\varphi_i\circ\psi_i=\mathrm{id}.
$$

证明映射 $x\mapsto(\psi_1x,\ldots,\psi_mx)$ 是 $E$ 到各 $E_i$（$i=1,\ldots,m$）的直积上的同构，并且映射

$$
(x_1,\ldots,x_m)\mapsto\varphi_1x_1+\cdots+\varphi_mx_m
$$

是这个直积到 $E$ 上的同构。

反过来，若 $E$ 等于子模 $E_i$（$i=1,\ldots,m$）的直积（或直和），令 $\varphi_i$ 为 $E_i$ 到 $E$ 中的包含映射，令 $\psi_i$ 为 $E$ 到 $E_i$ 上的投影，则这些映射满足上述性质。

**5.** 设 $A$ 是欧几里得空间 $\mathbf{R}^n$ 的一个加法子群，并假定空间的每个有界区域中都只有有限多个 $A$ 的元素。证明 $A$ 是由不超过 $n$ 个生成元生成的自由阿贝尔群。［*提示：* 对 $A$ 中在 $\mathbf{R}$ 上线性无关的元素的最大数目作归纳。设 $v_1,\ldots,v_m$ 是这样的一组极大元素集，并令 $A_0$ 为 $A$ 中包含在由 $v_1,\ldots,v_{m-1}$ 生成的 $\mathbf{R}$-空间中的子群。由归纳假设，可设 $A_0$ 的每个元素都是 $v_1,\ldots,v_{m-1}$ 的整系数线性组合。令 $S$ 为 $A$ 中具有形式 $v=a_1v_1+\cdots+a_mv_m$ 的元素组成的子集，其中实系数 $a_i$ 满足

$$
0\leqq a_i<1\quad\text{若 }i=1,\ldots,m-1,
$$

$$
0\leqq a_m\leqq1.
$$

若 $v'_m$ 是 $S$ 中非零的 $a_m$ 最小的一个元素，证明 $\{v_1,\ldots,v_{m-1},v'_m\}$ 是 $A$ 在 $\mathbf{Z}$ 上的一组基。］

*注。* 上面的习题用于代数数论中，证明数域的整数环的可逆元群模去挠子群后，同构于欧几里得空间中的一个格。见第 VII 章习题 4。

**6.** （Artin-Tate）。设 $G$ 是作用于有限集 $S$ 的有限群。对 $w\in S$，将 $1\cdot w$ 记为 $[w]$，于是我们有直和

$$
\mathbf{Z}\langle S\rangle=\sum_{w\in S}\mathbf{Z}[w].
$$

通过规定 $\sigma[w]=[\sigma w]$（$w\in S$），并将 $\sigma$ 按线性延拓到 $\mathbf{Z}\langle S\rangle$，定义 $G$ 在 $\mathbf{Z}\langle S\rangle$ 上的作用。设 $M$ 是 $\mathbf{Z}\langle S\rangle$ 的一个秩为 $\#[S]$ 的子群。证明 $M$ 有一组 $\mathbf{Z}$-基 $\{y_w\}_{w\in S}$，使得对所有 $w\in S$，都有 $\sigma y_w=y_{\sigma w}$。（参见我的 *Algebraic Number Theory*，第 IX 章 §4，定理 1。）

> 译校注：原文条件为“Let $M$ be a subgroup of $\mathbf{Z}\langle S\rangle$ of rank $\#[S]$”，未假定 $M$ 在 $G$ 作用下稳定，而结论 $\sigma y_w=y_{\sigma w}$ 会蕴含这种稳定性。例如，若 $G$ 交换两点 $S=\{s_1,s_2\}$，满秩子群 $2\mathbf{Z}[s_1]\oplus\mathbf{Z}[s_2]$ 就不稳定。因此原题条件不足，保留原题，不主张给出了完整修正。这里也不主张仅补充 $G$ 稳定性就能使原题成立。

**7.** 设 $M$ 是有限生成阿贝尔群。所谓 $M$ 上的**半范数**，是指满足下列性质的实值函数 $v\mapsto|v|$：

<span class="original-page-anchor" id="pdf-page-182" aria-hidden="true"></span>

$$
|v|\geqq0\quad\text{对所有 }v\in M;
$$

$$
|nv|=|n|\,|v|\quad\text{对 }n\in\mathbf{Z};
$$

$$
|v+w|\leqq|v|+|w|\quad\text{对所有 }v,w\in M.
$$

所谓半范数的**核**，是指满足 $|v|=0$ 的元素 $v$ 组成的子集。

(a) 设 $M_0$ 为核。证明 $M_0$ 是一个子群。若 $M_0=\{0\}$，则此半范数称为**范数**。

(b) 假定 $M$ 的秩为 $r$。设 $v_1,\ldots,v_r\in M$ 模 $M_0$ 后在 $\mathbf{Z}$ 上线性无关。证明 $M/M_0$ 存在一组基 $\{w_1,\ldots,w_r\}$，使得

$$
|w_i|\leqq\sum_{j=1}^{i}|v_j|.
$$

［*提示：* 将定理 7.8 的证明写成显式形式，就得到这个结果。不失一般性，可假定 $M_0=\{0\}$。令 $M_1=\langle v_1,\ldots,v_r\rangle$。令 $d$ 为 $M/M_1$ 的指数。则 $dM$ 在 $M_1$ 中具有有限指数。令 $n_{j,j}$ 为使得存在整数 $n_{j,1},\ldots,n_{j,j-1}$ 满足下式的最小正整数：

$$
n_{j,1}v_1+\cdots+n_{j,j}v_j=dw_j\quad\text{其中某个 }w_j\in M.
$$

不失一般性，可假定 $0\leqq n_{j,k}\leqq d-1$。则元素 $w_1,\ldots,w_r$ 构成所求的基。］

> 译校注：原文写作 $0\leqq n_{j,k}\leqq d-1$，未注明 $k$ 的范围；这个界应限制在 $k<j$ 的系数上。对角系数 $n_{j,j}$ 是正整数，应满足 $1\leqq n_{j,j}\leqq d$。例如 $M=M_1$ 时，$d=1$ 且 $n_{j,j}=1$，不满足原式若也施于 $k=j$ 所给出的上界 $0$。

**8.** 考虑非零有理数组成的乘法群 $\mathbf{Q}^*$。对非零有理数 $x=a/b$，其中 $a,b\in\mathbf{Z}$ 且 $(a,b)=1$，定义其**高度**为

$$
h(x)=\log\max(|a|,|b|).
$$

(a) 证明 $h$ 定义了 $\mathbf{Q}^*$ 上的一个半范数，其核由 $\pm1$ 组成（即挠群）。

(b) 设 $M_1$ 是 $\mathbf{Q}^*$ 的有限生成子群，由有理数 $x_1,\ldots,x_m$ 生成。设 $M$ 为 $\mathbf{Q}^*$ 中这样的元素 $x$ 组成的子群：对某个正整数 $s$，有 $x^s\in M_1$。证明 $M$ 是有限生成的，并利用习题 7，根据 $x_1,\ldots,x_m$ 的半范数，给出 $M$ 的某组生成元的半范数的一个界。

*注。* 上述两道习题应用于丢番图逼近问题。见我的 Diophantine approximation on toruses，*Am. J. Math.* **86**（1964），第 521-533 页，以及我在 *Encyclopedia of Mathematical Sciences, Number Theory III*，Springer Verlag，1991 年，第 240-243 页中给出的讨论与参考文献。

### 局部化

**9.** (a) 设 $A$ 是交换环，$M$ 是一个 $A$-模。设 $S$ 是 $A$ 的一个乘法子集。用与定义 $S^{-1}A$ 相类似的方式定义 $S^{-1}M$，并证明 $S^{-1}M$ 是一个 $S^{-1}A$-模。

(b) 若 $0\to M'\to M\to M''\to0$ 是正合列，证明列 $0\to S^{-1}M'\to S^{-1}M\to S^{-1}M''\to0$ 正合。

<span class="original-page-anchor" id="pdf-page-183" aria-hidden="true"></span>

**10.** (a) 若 $\mathfrak{p}$ 是素理想，$S=A-\mathfrak{p}$ 是 $\mathfrak{p}$ 在环 $A$ 中的补集，则将 $S^{-1}M$ 记为 $M_{\mathfrak{p}}$。证明自然映射

$$
M\to\prod M_{\mathfrak{p}}
$$

是单射，这里它将模 $M$ 映入所有局部化 $M_{\mathfrak{p}}$ 的直积，$\mathfrak{p}$ 遍历所有*极大*理想。

(b) 证明列 $0\to M'\to M\to M''\to0$ 正合，当且仅当对所有素理想 $\mathfrak{p}$，列 $0\to M'_{\mathfrak{p}}\to M_{\mathfrak{p}}\to M''_{\mathfrak{p}}\to0$ 都正合。

(c) 设 $A$ 是整环，$M$ 是无挠模。对 $A$ 的每个素理想 $\mathfrak{p}$，证明自然映射 $M\to M_{\mathfrak{p}}$ 是单射。特别地，$A\to A_{\mathfrak{p}}$ 是单射，不过也可直接从 $A$ 到其分式域 $K$ 中的嵌入看出这一点。

### 戴德金环上的投射模

对于下一道习题，我们假定你已经做过上一章中关于戴德金环的习题。我们将看到，对于这样的环，其模理论的某些部分可以通过局部化归约到主理想整环的情形。设 $\mathfrak{o}$ 为戴德金环，$K$ 为其分式域。

**11.** 设 $M$ 是 $\mathfrak{o}$ 上的有限生成无挠模。证明 $M$ 是投射模。［*提示：* 给定素理想 $\mathfrak{p}$，局部化模 $M_{\mathfrak{p}}$ 是 $\mathfrak{o}_{\mathfrak{p}}$ 上的有限生成无挠模，而 $\mathfrak{o}_{\mathfrak{p}}$ 是主理想整环。于是 $M_{\mathfrak{p}}$ 是投射模，因此，若 $F$ 是 $\mathfrak{o}$ 上的有限自由模，且 $f:F\to M$ 是满射同态，则 $f_{\mathfrak{p}}:F_{\mathfrak{p}}\to M_{\mathfrak{p}}$ 有分裂映射 $g_{\mathfrak{p}}:M_{\mathfrak{p}}\to F_{\mathfrak{p}}$，使得 $f_{\mathfrak{p}}\circ g_{\mathfrak{p}}=\mathrm{id}_{M_{\mathfrak{p}}}$。存在 $c_{\mathfrak{p}}\in\mathfrak{o}$，使得 $c_{\mathfrak{p}}\notin\mathfrak{p}$ 且 $c_{\mathfrak{p}}g_{\mathfrak{p}}(M)\subset F$。族 $\{c_{\mathfrak{p}}\}$ 生成单位理想 $\mathfrak{o}$（为什么？），所以存在有限多个元素 $c_{\mathfrak{p}_i}$ 以及元素 $x_i\in\mathfrak{o}$，使得 $\sum x_ic_{\mathfrak{p}_i}=1$。令

$$
g=\sum x_ic_{\mathfrak{p}_i}g_{\mathfrak{p}_i}.
$$

然后证明 $g:M\to F$ 给出一个满足 $f\circ g=\mathrm{id}_M$ 的同态。］

**12.** (a) 设 $\mathfrak{a},\mathfrak{b}$ 为理想。证明存在 $\mathfrak{o}$-模的同构

$$
\mathfrak{a}\oplus\mathfrak{b}\xrightarrow{\approx}\mathfrak{o}\oplus\mathfrak{a}\mathfrak{b}
$$

［*提示：* 先在 $\mathfrak{a},\mathfrak{b}$ 互素时证明。考虑同态 $\mathfrak{a}\oplus\mathfrak{b}\to\mathfrak{a}+\mathfrak{b}$，并使用习题 10。利用第 II 章习题 19，将一般情形归约到互素情形。］

(b) 设 $\mathfrak{a},\mathfrak{b}$ 是分式理想，$f:\mathfrak{a}\to\mathfrak{b}$ 是同构（当然是 $\mathfrak{o}$-模的同构）。则 $f$ 可以延拓为一个 $K$-线性映射 $f_K:K\to K$。令 $c=f_K(1)$。证明 $\mathfrak{b}=c\mathfrak{a}$，且 $f$ 由映射 $m_c:x\mapsto cx$ 给出（即乘以 $c$）。

(c) 设 $\mathfrak{a}$ 是分式理想。对每个 $b\in\mathfrak{a}^{-1}$，映射 $m_b:\mathfrak{a}\to\mathfrak{o}$ 是对偶模 $\mathfrak{a}^{\vee}$ 的一个元素。证明在此映射下，有 $\mathfrak{a}^{-1}=\mathfrak{a}^{\vee}=\operatorname{Hom}_{\mathfrak{o}}(\mathfrak{a},\mathfrak{o})$，因而 $\mathfrak{a}^{\vee\vee}=\mathfrak{a}$。

**13.** (a) 设 $M$ 是戴德金环 $\mathfrak{o}$ 上的有限投射模。证明存在自由模 $F$ 和 $F'$，使得 $F\supset M\supset F'$，且 $F,F'$ 具有相同的秩，这个秩称为 $M$ 的**秩**。

(b) 证明存在 $F$ 的一组基 $\{e_1,\ldots,e_n\}$ 和理想 $\mathfrak{a}_1,\ldots,\mathfrak{a}_n$，使得 $M=\mathfrak{a}_1e_1+\cdots+\mathfrak{a}_ne_n$，换言之，$M\approx\bigoplus\mathfrak{a}_i$。

<span class="original-page-anchor" id="pdf-page-184" aria-hidden="true"></span>

(c) 证明对某个理想 $\mathfrak{a}$，有 $M\approx\mathfrak{o}^{n-1}\oplus\mathfrak{a}$，而且对应 $M\mapsto\mathfrak{a}$ 诱导出 $K_0(\mathfrak{o})$ 与理想类群 $\operatorname{Pic}(\mathfrak{o})$ 的同构。（群 $K_0(\mathfrak{o})$ 是 §4 末尾定义的投射模的等价类群。）

### 几条蛇

**14.** 考虑一个由 $R$-模和同态组成的交换图，其中每一行均正合：

![习题14的交换图，纵向映射为 f、g、h。](/library/volume-86/diagrams/pdf-0184-ex14-snake.png)

证明：

(a) 若 $f,h$ 为单态射，则 $g$ 为单态射。

(b) 若 $f,h$ 为满射，则 $g$ 为满射。

(c) 另外假定 $0\to M'\to M$ 正合，且 $N\to N''\to0$ 正合。证明若 $f,g,h$ 中任意两个是同构，则第三个也是同构。［*提示：* 使用蛇引理。］

**15.** **五引理。** 考虑一个由 $R$-模和同态组成的交换图，其中每一行均正合：

![习题15的交换图，纵向映射为 f_1 至 f_5。](/library/volume-86/diagrams/pdf-0184-ex15-five-lemma.png)

证明：

(a) 若 $f_1$ 为满射，且 $f_2,f_4$ 为单态射，则 $f_3$ 为单态射。

(b) 若 $f_5$ 为单态射，且 $f_2,f_4$ 为满射，则 $f_3$ 为满射。［*提示：* 使用蛇引理。］

### 逆极限

**16.** 证明一个单群系统的逆极限，若其同态均为满射，则它或者是平凡群，或者是单群。

**17.** (a) 令 $n$ 遍历正整数，设 $p$ 为素数。证明阿贝尔群 $A_n=\mathbf{Z}/p^n\mathbf{Z}$ 在 $n\geqq m$ 时的典范同态下构成一个逆系。令 $\mathbf{Z}_p$ 为其逆极限。证明 $\mathbf{Z}_p$ 满射到每个 $\mathbf{Z}/p^n\mathbf{Z}$ 上；$\mathbf{Z}_p$ 没有零因子，并有唯一的极大理想，由 $p$ 生成。证明 $\mathbf{Z}_p$ 是唯一分解整环，只有一个素元，即 $p$ 本身。

<span class="original-page-anchor" id="pdf-page-185" aria-hidden="true"></span>

(b) 再考虑 $\mathbf Z$ 的所有非零理想，由整除关系使它们构成一个有向系。证明

$$
\varprojlim_{(a)}\mathbf Z/(a)=\prod_p\mathbf Z_p,
$$

其中极限取遍所有非零理想 $(a)$，而乘积取遍所有素数 $p$。

**18.** (a) 设 $\{A_n\}$ 是交换环的一个逆向有向序列，$\{M_n\}$ 是模的一个逆向有向序列，其中 $M_n$ 是 $A_n$ 上的模，并且下图交换：

![环作用相容的交换图](/library/volume-86/diagrams/pdf-0185-ex18.png)

竖直映射是该有向序列的同态，水平映射给出环在模上的作用。证明 $\varprojlim M_n$ 是 $\varprojlim A_n$ 上的模。

(b) 设 $M$ 是一个 $p$ 可除群。证明 $T_p(M)$ 是 $\mathbf Z_p$ 上的模。

> 译校注：原文印作 $T_p(A)$，应为 $T_p(M)$；本小题给定的群是 $M$，而 $T_p$ 在此作用于这个群。

(c) 设 $M,N$ 是 $p$ 可除群。证明，作为 $\mathbf Z_p$ 上的模，$T_p(M\oplus N)=T_p(M)\oplus T_p(N)$。

### 直极限

**19.** 设 $(A_i,f_j^i)$ 是模的一个有向族。对某个 $k$，取 $a_k\in A_k$，并假设 $a_k$ 在直极限 $A$ 中的像为 $0$。证明，存在某个指标 $j\geqq k$，使得 $f_j^k(a_k)=0$。换言之，某个群 $A_i$ 中的某个元素是否在直极限中变为零，从原来的数据中就已经可以看出来。说明这一点的一种方法，是利用定理 10.1 中的构造。

**20.** 设 $I,J$ 是两个有向集，并在乘积 $I\times J$ 上赋予显然的序：当 $i\leqq i'$ 且 $j\leqq j'$ 时，$(i,j)\leqq(i',j')$。设 $A_{ij}$ 是一个阿贝尔群族，其同态以 $I\times J$ 为指标，并构成一个有向族。证明，直极限

$$
\varinjlim_i\varinjlim_j A_{ij}\quad\text{和}\quad\varinjlim_j\varinjlim_i A_{ij}
$$

存在，并且以自然的方式同构。叙述并证明逆极限的相应结论。

**21.** 设 $(M_i',f_j^i),(M_i,g_j^i)$ 是某个环上模的有向系。一个**同态**

$$
(M_i')\xrightarrow{u}(M_i)
$$

是指对每个 $i$ 给定一个同态 $u_i:M_i'\to M_i$，这些同态与 $f_j^i,g_j^i$ 交换。假设给定有向系的一个正合列

$$
0\longrightarrow(M_i')\xrightarrow{u}(M_i)\xrightarrow{v}(M_i'')\longrightarrow0,
$$

也就是说，对每个 $i$，序列

$$
0\longrightarrow M_i'\longrightarrow M_i\longrightarrow M_i''\longrightarrow0
$$

<span class="original-page-anchor" id="pdf-page-186" aria-hidden="true"></span>

是正合的。证明直极限保持正合性，也就是说，

$$
0\longrightarrow\varinjlim M_i'\longrightarrow\varinjlim M_i\longrightarrow\varinjlim M_i''\longrightarrow0
$$

是正合的。

**22.** (a) 设 $\{M_i\}$ 是某个环上的一个模族。对任意模 $N$，证明

$$
\operatorname{Hom}\left(\bigoplus M_i,N\right)=\prod\operatorname{Hom}(M_i,N)
$$

(b) 证明

$$
\operatorname{Hom}\left(N,\prod M_i\right)=\prod\operatorname{Hom}(N,M_i).
$$

**23.** 设 $\{M_i\}$ 是某个环上模的一个有向族。对任意有限表示模 $N$，证明

$$
\varinjlim\operatorname{Hom}(N,M_i)=\operatorname{Hom}\left(N,\varinjlim M_i\right)
$$

> 译校注：原文写的是“对任意模 $N$”（“For any module $N$”），遗漏了 $N$ 有限表示的条件。对任意 $N$，上式一般不成立；$\operatorname{Hom}(N,-)$ 与所有有向直极限交换需要 $N$ 有限表示，参见第 26 题。这里补上该条件。

**24.** 证明任意模都是有限生成子模的直极限。

如果存在一个正合列

$$
F_1\longrightarrow F_0\longrightarrow M\longrightarrow0,
$$

其中 $F_0,F_1$ 都是具有有限基的自由模，那么模 $M$ 称为**有限表示的**。$F_1$ 在 $F_0$ 中的像称为 $F_0$ 的自由基元素之间的**关系**子模。

**25.** 证明任意模都是有限表示模的直极限（这些模未必是子模）。换言之，给定 $M$，存在有向系 $\{M_i,f_j^i\}$，其中对所有 $i$，$M_i$ 都是有限表示的，并且

$$
M\approx\varinjlim M_i.
$$

[提示：任意有限生成子模都是这样的直极限，因为一个无限生成的关系模可以看成有限生成关系模的极限。将这一点精确化，即可得到证明。]

**26.** 设 $E$ 是某个环上的模，$\{M_i\}$ 是模的一个有向族。如果 $E$ 是有限生成的，证明自然同态

$$
\varinjlim\operatorname{Hom}(E,M_i)\longrightarrow\operatorname{Hom}\left(E,\varinjlim M_i\right)
$$

是单射。如果 $E$ 是有限表示的，证明这个同态是同构。提示：先在 $E$ 是具有有限基的自由模时证明这些结论。然后，设 $E$ 由正合列 $F_1\to F_0\to E\to0$ 给出有限表示。考虑下图：

![比较 Hom 的直极限与到直极限的 Hom 的交换图](/library/volume-86/diagrams/pdf-0186-ex26.png)

<span class="original-page-anchor" id="pdf-page-187" aria-hidden="true"></span>

### 分次代数

设 $A$ 是域 $k$ 上的一个代数。所谓 $A$ 的一个**滤过**，是指一个 $k$ 向量空间序列 $A_i$ $(i=0,1,\ldots)$，满足

$$
A_0\subset A_1\subset A_2\subset\cdots\qquad\text{且}\qquad\bigcup A_i=A,
$$

并且对所有 $i,j\geqq0$，有 $A_iA_j\subset A_{i+j}$。这时称 $A$ 为一个**滤过代数**。设 $R$ 是一个代数。如果 $R$ 是子空间的直和 $R=\bigoplus R_i$，并且对所有 $i,j\geqq0$ 都有 $R_iR_j\subset R_{i+j}$，那么称 $R$ 是**分次的**。

**27.** 设 $A$ 是一个滤过代数。对 $i\geqq0$，定义 $R_i=A_i/A_{i-1}$。按定义，$A_{-1}=\{0\}$。令 $R=\bigoplus R_i$，并记 $R_i=\operatorname{gr}_i(A)$。在 $R$ 上定义一个自然的乘法，使 $R$ 成为一个分次代数，记作 $\operatorname{gr}(A)$，并称为**伴随分次代数**。

**28.** 设 $A,B$ 是滤过代数，$A=\bigcup A_i$，$B=\bigcup B_i$。设 $L:A\to B$ 是一个保持滤过的 $k$ 线性映射，也就是说，对所有 $i$，有 $L(A_i)\subset B_i$，并且对所有 $i$、$c\in k$ 和 $a\in A_i$，有 $L(ca)=L(c)L(a)$。

> 译校注：原文的 $L(ca)=L(c)L(a)$ 在此保留。一般 $k$ 线性映射的标量相容性是 $L(ca)=cL(a)$，原式对一般 $k$ 线性映射并不成立；它可以理解为一个附加条件，即 $L(1)$ 左乘 $L(A)$ 中的元素时起单位元的作用。无论保留这个附加条件，还是仅要求 $L$ 是保持滤过的 $k$ 线性映射，下面 (a)、(b) 的结论都成立。

(a) 证明 $L$ 对所有 $i$ 都诱导一个 $k$ 线性映射

$$
\operatorname{gr}_i(L):\operatorname{gr}_i(A)\longrightarrow\operatorname{gr}_i(B).
$$

(b) 假设对所有 $i$，$\operatorname{gr}_i(L)$ 都是同构。证明 $L$ 是一个 $k$ 线性同构。

**29.** 假设 $k$ 的特征为 $0$。设 $\mathfrak n$ 是 $k$ 上给定大小 $n\times n$ 的所有严格上三角矩阵构成的集合。

(a) 对给定矩阵 $X\in\mathfrak n$，设 $D_1(X),\ldots,D_n(X)$ 为它的各条对角线，于是 $D_1=D_1(X)$ 是主对角线，并且根据 $\mathfrak n$ 的定义，它为 $0$。设 $\mathfrak n_i$ 是 $\mathfrak n$ 的子集，由那些对角线 $D_1,\ldots,D_{n-i}$ 均为 $0$ 的矩阵组成。因此 $\mathfrak n_0=\{0\}$；$\mathfrak n_1$ 由除了 $x_{1n}$ 可能不为零之外所有分量均为 $0$ 的矩阵组成；$\mathfrak n_2$ 由除了最后两条对角线上的分量可能不为零之外所有分量均为 $0$ 的矩阵组成；依此类推。证明每个 $\mathfrak n_i$ 都是一个代数，其元素都是幂零的（事实上，其元素的第 $i+1$ 次幂为 $0$）。

> 译校注：原文将 $\mathfrak n_1$ 中唯一可能非零的分量印作 $x_{nn}$，应为 $x_{1n}$。按前面的定义，$D_1,\ldots,D_{n-1}$ 均为零，故只有最上方的第 $n$ 条对角线，即右上角分量 $x_{1n}$，可能非零；$x_{nn}$ 属于主对角线，必为零。

(b) 设 $U$ 为所有形如 $I+X$、其中 $X\in\mathfrak n$ 的元素构成的集合。证明 $U$ 是一个乘法群。

(c) 设 $\exp$ 是通常定义的指数级数。证明 $\exp$ 在 $\mathfrak n$ 上定义了一个多项式函数（在幂零矩阵处求值时，除有限项外所有项均为 $0$），并给出一个双射

$$
\exp:\mathfrak n\longrightarrow U.
$$

证明其逆映射由标准的 $\log$ 级数给出。
