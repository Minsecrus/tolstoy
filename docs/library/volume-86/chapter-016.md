---
title: "第十六章 张量积"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第十五章 双线性型的结构","link":"/library/volume-86/chapter-015"}
next: {"text":"第十七章 半单性","link":"/library/volume-86/chapter-017"}
---

# 第十六章 张量积

<span class="original-page-anchor" id="pdf-page-610" aria-hidden="true"></span>

讨论了双线性映射之后，现在转向多重线性映射以及有关其结构的基本定理。存在一个表示多重线性映射的泛模，称为张量积。我们将推导它的基本性质，把交错积这一特殊情形留到第 XIX 章。张量积的名称源于它在微分几何中的应用，即将这种积应用于流形的切空间或余切空间。张量积也可以看作提供了一种“扩张基环”的机制，也就是从一个环上的模过渡到该环上某个代数上的模。这种“扩张”也可能包含模一个理想的约化，因为关键在于给定一个环同态 $f:A\to B$，并从 $A$ 上的模过渡到 $B$ 上的模。同态 $f$ 可以是这两种类型中的任一种：包含映射，或对某个理想 $J$，具有 $B=A/J$ 的典范映射；也可以是二者的复合。

我努力提供能直接用于许多领域各种应用的基础材料，例如拓扑学、代数、微分几何、代数几何等。

## §1. 张量积

令 $R$ 为一个交换环。若 $E_1,\ldots,E_n,F$ 是模，用

$$
L^n(E_1,\ldots,E_n;F)
$$

表示 $n$ 重线性映射

$$
f:E_1\times\cdots\times E_n\to F
$$

组成的模。

<span class="original-page-anchor" id="pdf-page-611" aria-hidden="true"></span>

回顾一下，多重线性映射是对每个变量都线性（即 $R$ 线性）的映射。我们交替使用“线性”和“同态”这两个词。*除非另有说明，模、同态、线性、多重线性都是针对环 $R$ 而言的。*

可以把固定的一组模 $E_1,\ldots,E_n$ 的多重线性映射看成一个范畴的对象。事实上，若

$$
f:E_1\times\cdots\times E_n\to F\quad\text{和}\quad g:E_1\times\cdots\times E_n\to G
$$

都是多重线性的，就把态射 $f\to g$ 定义为使下图交换的同态 $h:F\to G$：

![交换三角图：f 映到 F，g 映到 G，h 从 F 映到 G。](/library/volume-86/diagrams/pdf-0611-universal-triangle.png)

这个范畴中的一个泛对象称为 $E_1,\ldots,E_n$ 的一个（在 $R$ 上的）**张量积**。

*现在证明张量积存在*，并且以自然的方式实际构造一个。由抽象的一般原理，当然知道张量积在相差唯一同构的意义下唯一确定。

令 $M$ 为由所有 $n$ 元组 $(x_1,\ldots,x_n)$（$x_i\in E_i$）组成的集合生成的自由模，即由集合 $E_1\times\cdots\times E_n$ 生成的自由模。令 $N$ 为由以下类型的所有元素生成的子模：

$$
(x_1,\ldots,x_i+x_i',\ldots,x_n)-(x_1,\ldots,x_i,\ldots,x_n)-(x_1,\ldots,x_i',\ldots,x_n),
$$

$$
(x_1,\ldots,ax_i,\ldots,x_n)-a(x_1,\ldots,x_n),
$$

其中 $x_i\in E_i$、$x_i'\in E_i$、$a\in R$ 任意。有从这个集合到由它生成的自由模的典范单射

$$
E_1\times\cdots\times E_n\to M.
$$

把它与到商模的典范映射 $M\to M/N$ 复合，得到映射

$$
\varphi:E_1\times\cdots\times E_n\to M/N.
$$

我们断言，$\varphi$ 是多重线性的，并且是一个张量积。

显然 $\varphi$ 是多重线性的——我们的定义正是为此而设。令

$$
f:E_1\times\cdots\times E_n\to G
$$

为一个多重线性映射。根据由

$$
E_1\times\cdots\times E_n
$$

生成的自由模的定义，<span class="original-page-anchor" id="pdf-page-612" aria-hidden="true"></span>有一个诱导的线性映射 $M\to G$，使下图交换：

![从积到 M 和 G 的交换三角图，f 映到 G，并有诱导映射 M 到 G。](/library/volume-86/diagrams/pdf-0612-free-module-triangle.png)

由于 $f$ 是多重线性的，诱导映射 $M\to G$ 在 $N$ 上取值为 $0$。因此，由商模的泛性质，它可以通过 $M/N$ 分解，从而有同态 $f_*:M/N\to G$，使下图交换：

![交换三角图：phi 映到 M/N，f 映到 G，f_* 从 M/N 映到 G。](/library/volume-86/diagrams/pdf-0612-quotient-triangle.png)

由于 $\varphi$ 的像生成 $M/N$，诱导映射 $f_*$ 唯一确定。这证明了所要的结论。

模 $M/N$ 记为

$$
E_1\otimes\cdots\otimes E_n\quad\text{或}\quad\bigotimes_{i=1}^nE_i.
$$

我们在张量积的同构类中构造了一个具体的张量积，以下称它为 $E_1,\ldots,E_n$ 的**张量积**。若 $x_i\in E_i$，写作

$$
\varphi(x_1,\ldots,x_n)=x_1\otimes\cdots\otimes x_n=x_1\otimes_R\cdots\otimes_R x_n.
$$

对所有 $i$，都有

$$
x_1\otimes\cdots\otimes ax_i\otimes\cdots\otimes x_n=a(x_1\otimes\cdots\otimes x_n),
$$

$$
\begin{aligned}
x_1\otimes\cdots\otimes(x_i+x_i')\otimes\cdots\otimes x_n
&=(x_1\otimes\cdots\otimes x_n)\\
&\quad+(x_1\otimes\cdots\otimes x_i'\otimes\cdots\otimes x_n),
\end{aligned}
$$

其中 $x_i,x_i'\in E_i$，$a\in R$。

若只有两个因子，比如 $E\otimes F$，则 $E\otimes F$ 的每个元素都可以写成若干项 $x\otimes y$（$x\in E$，$y\in F$）的和，因为这些项在 $R$ 上生成 $E\otimes F$，并且对 $a\in R$ 有 $a(x\otimes y)=ax\otimes y$。

<span class="original-page-anchor" id="pdf-page-613" aria-hidden="true"></span>

**注。** 若张量积中的一个元素为 $0$，则已经可以用定义张量积的有限多个关系来表示这一事实。因此，若 $E$ 是子模 $E_i$ 的直极限，则

$$
\varinjlim F\otimes E_i=F\otimes\varinjlim E_i=F\otimes E.
$$

特别地，每个模都是其有限生成子模的直极限。经常使用的一个方法是：让 $E_i$ 遍及 $E$ 的各有限生成子模，通过检验一个元素在 $F\otimes E_i$ 中的像是否为 $0$，来检验 $F\otimes E$ 中这个元素是否为 $0$。

**注意。** 张量积可能使模中的大量信息消失。例如，取 $\mathbf Z/m\mathbf Z$ 和 $\mathbf Z/n\mathbf Z$ 在 $\mathbf Z$ 上的张量积，其中 $m,n$ 为互素且 $>1$ 的整数。此时

$$
\mathbf Z/n\mathbf Z\otimes\mathbf Z/m\mathbf Z=0.
$$

事实上，有 $n(x\otimes y)=(nx)\otimes y=0$ 以及 $m(x\otimes y)=x\otimes my=0$。所以对所有 $x\in\mathbf Z/n\mathbf Z$ 和 $y\in\mathbf Z/m\mathbf Z$，都有 $x\otimes y=0$。形如 $x\otimes y$ 的元素生成张量积，所以张量积为 $0$。后面将看到避免这种消失的条件。

在后面的许多结果中，我们将断言某些从张量积出发的线性映射存在。通过使用双线性映射经过张量积分解的泛映射性质，可以证明这一存在性。由于形如 $x\otimes y$ 的元素（以两个因子为例）生成张量积，规定线性映射在这类元素上的取值就得到唯一性。

现在证明张量积的结合律。

**命题 1.1.** *令 $E_1,E_2,E_3$ 为模。则存在唯一的同构*

$$
(E_1\otimes E_2)\otimes E_3\to E_1\otimes(E_2\otimes E_3),
$$

*使得*

$$
(x\otimes y)\otimes z\mapsto x\otimes(y\otimes z),
$$

*其中 $x\in E_1$，$y\in E_2$，$z\in E_3$。*

*证明。* 由于形如 $(x\otimes y)\otimes z$ 的元素生成张量积，所需线性映射的唯一性显然成立。为证明存在性，令 $x\in E_1$。映射

$$
\lambda_x:E_2\times E_3\to(E_1\otimes E_2)\otimes E_3
$$

<span class="original-page-anchor" id="pdf-page-614" aria-hidden="true"></span>

由 $\lambda_x(y,z)=(x\otimes y)\otimes z$ 给出，显然是双线性的，所以通过张量积上的一个线性映射分解：

$$
\widetilde\lambda_x:E_2\otimes E_3\to(E_1\otimes E_2)\otimes E_3.
$$

于是映射

$$
E_1\times(E_2\otimes E_3)\to(E_1\otimes E_2)\otimes E_3,
$$

由

$$
(x,\alpha)\mapsto\widetilde\lambda_x(\alpha)
$$

给出，其中 $x\in E_1$，$\alpha\in E_2\otimes E_3$，显然是双线性的，并通过一个线性映射分解：

$$
E_1\otimes(E_2\otimes E_3)\to(E_1\otimes E_2)\otimes E_3.
$$

这个映射具有所需性质（由构造可清楚看出）。

**命题 1.2.** *令 $E,F$ 为模。则存在唯一的同构*

$$
E\otimes F\to F\otimes E,
$$

*使得对 $x\in E$ 和 $y\in F$，有 $x\otimes y\mapsto y\otimes x$。*

*证明。* 由 $(x,y)\mapsto y\otimes x$ 给出的映射 $E\times F\to F\otimes E$ 是双线性的，所以通过张量积 $E\otimes F$ 分解，把 $x\otimes y$ 映为 $y\otimes x$。由于最后这个映射有逆映射（由对称性），得到所需的同构。

张量积具有各种函子性质。首先，假设

$$
f_i:E_i'\to E_i\quad(i=1,\ldots,n)
$$

是一组线性映射。得到积上的诱导映射

$$
\prod f_i:\prod E_i'\to\prod E_i.
$$

把 $\prod f_i$ 与到张量积的典范映射复合，就得到一个诱导的线性映射，可以记为 $T(f_1,\ldots,f_n)$，使下图交换：

![张量积函子的交换方图：左边为积映射，右边为 T(f_1,...,f_n)，水平方向为典范张量映射。](/library/volume-86/diagrams/pdf-0614-tensor-functor-square.png)

<span class="original-page-anchor" id="pdf-page-615" aria-hidden="true"></span>

可以立即验证，$T$ 是函子性的，即若有线性映射的复合 $f_i\circ g_i$（$i=1,\ldots,n$），则

$$
T(f_1\circ g_1,\ldots,f_n\circ g_n)=T(f_1,\ldots,f_n)\circ T(g_1,\ldots,g_n),
$$

并且

$$
T(\mathrm{id},\ldots,\mathrm{id})=\mathrm{id}.
$$

注意，$T(f_1,\ldots,f_n)$ 是唯一的线性映射，它在 $E_1'\otimes\cdots\otimes E_n'$ 的元素 $x_1'\otimes\cdots\otimes x_n'$ 上的作用为

$$
x_1'\otimes\cdots\otimes x_n'\mapsto f_1(x_1')\otimes\cdots\otimes f_n(x_n').
$$

可以把 $T$ 看成映射

$$
\prod_{i=1}^nL(E_i',E_i)\to L\left(\bigotimes_{i=1}^nE_i',\bigotimes_{i=1}^nE_i\right),
$$

读者不难验证，这个映射是多重线性的。对于两个因子，明确写出其意义，此时映射可以记为

$$
(f,g)\mapsto T(f,g).
$$

给定同态 $f:F'\to F$ 和 $g_1,g_2:E'\to E$，有

$$
T(f,g_1+g_2)=T(f,g_1)+T(f,g_2),
$$

$$
T(f,ag_1)=aT(f,g_1).
$$

特别地，固定一个模 $F$，考虑从模到模的函子 $\tau=\tau_F$，满足

$$
\tau(E)=F\otimes E.
$$

于是对每一对模 $E',E$，$\tau$ 通过公式

$$
\tau(f)=T(\mathrm{id},f)
$$

给出一个线性映射

$$
\tau:L(E',E)\to L(\tau(E'),\tau(E)).
$$

**注。** 有时为方便起见，略微滥用记号，写作

$$
f_1\otimes\cdots\otimes f_n\quad\text{代替}\quad T(f_1,\ldots,f_n).
$$

<span class="original-page-anchor" id="pdf-page-616" aria-hidden="true"></span>

这不应与在模的张量积

$$
L(E_1',E_1)\otimes\cdots\otimes L(E_n',E_n)
$$

中所取的元素的张量积混淆。上下文总会使我们的意思明确。

## §2. 基本性质

联系线性映射、双线性映射和张量积的最基本关系如下：对于三个模 $E,F,G$，

$$
\boxed{L(E,L(F,G))\approx L^2(E,F;G)\approx L(E\otimes F,G).}
$$

其中的同构可以用自然的方式描述。

(i) $L^2(E,F;G)\to L(E,L(F,G))$。

若 $f:E\times F\to G$ 是双线性的，$x\in E$，则由 $f_x(y)=f(x,y)$ 给出的映射

$$
f_x:F\to G
$$

是线性的。此外，映射 $x\mapsto f_x$ 是线性的，把它与 $f$ 配对就得到 (i)。

(ii) $L(E,L(F,G))\to L^2(E,F;G)$。

令 $\varphi\in L(E,L(F,G))$。令 $f_\varphi:E\times F\to G$ 为满足

$$
f_\varphi(x,y)=\varphi(x)(y)
$$

的双线性映射。于是 $\varphi\mapsto f_\varphi$ 定义了 (ii)。

显然，(i) 和 (ii) 的同态互为逆映射，因而给出框内前两个对象之间的同构。

(iii) $L^2(E,F;G)\to L(E\otimes F,G)$。

这是映射 $f\mapsto f_*$，把每个双线性映射 $f$ 配上张量积上的诱导线性映射。对应 $f\mapsto f_*$ 是单射（因为 $f_*$ 由 $f$ 唯一确定），也是满射，因为张量积上的任意线性映射与典范映射 $E\times F\to E\otimes F$ 复合，都会给出 $E\times F$ 上的一个双线性映射。

<span class="original-page-anchor" id="pdf-page-617" aria-hidden="true"></span>

**命题 2.1.** *令 $E=\bigoplus_{i=1}^nE_i$ 为一个直和。则有同构*

$$
F\otimes E\leftrightarrow\bigoplus_{i=1}^n(F\otimes E_i).
$$

*证明。* 这个同构由抽象的一般原理给出。固定 $F$，考虑函子 $\tau:X\mapsto F\otimes X$。如上所见，$\tau$ 是线性的。有 $E$ 到 $E_i$ 的投影 $\pi_i:E\to E$。于是

$$
\pi_i\circ\pi_i=\pi_i,\quad\pi_i\circ\pi_j=0\quad\text{若 }i\neq j,
$$

$$
\sum_{i=1}^n\pi_i=\mathrm{id}.
$$

应用函子 $\tau$，可见 $\tau(\pi_i)$ 满足相同的关系，因而给出 $\tau(E)=F\otimes E$ 的一个直和分解。注意，$\tau(\pi_i)=\mathrm{id}\otimes\pi_i$。

**推论 2.2.** *令 $I$ 为一个指标集，$E=\bigoplus_{i\in I}E_i$。则有同构*

$$
\left(\bigoplus_{i\in I}E_i\right)\otimes F\approx\bigoplus_{i\in I}(E_i\otimes F).
$$

*证明。* 令 $S$ 为 $I$ 的一个有限子集。有一列映射

$$
\left(\bigoplus_{i\in S}E_i\right)\times F\to\bigoplus_{i\in S}(E_i\otimes F)\to\bigoplus_{i\in I}(E_i\otimes F),
$$

其中第一个是双线性的，第二个是由 $S$ 到 $I$ 的包含映射诱导的线性映射。第一个是显然的映射。若 $S\subset S'$，则一个简单的交换图表明，映射

$$
\left(\bigoplus_{i\in S'}E_i\right)\times F\to\bigoplus_{i\in I}(E_i\otimes F)
$$

在 $i\in S$ 的直和上的限制，给出前述映射。不过，有一个*单射*

$$
\left(\bigoplus_{i\in S}E_i\right)\times F\to\left(\bigoplus_{i\in S'}E_i\right)\times F.
$$

因此，由相容性，可以定义一个双线性映射

$$
\left(\bigoplus_{i\in I}E_i\right)\times F\to\bigoplus_{i\in I}(E_i\otimes F),
$$

<span class="original-page-anchor" id="pdf-page-618" aria-hidden="true"></span>

从而得到一个线性映射

$$
\left(\bigoplus_{i\in I}E_i\right)\otimes F\to\bigoplus_{i\in I}(E_i\otimes F).
$$

以类似方式可以定义反方向的映射；显然，这些映射互为逆映射，因此给出一个同构。

现在假设 $E$ 在 $R$ 上自由，维数为 $1$。令 $\{v\}$ 为一组基，考虑 $F\otimes E$。$F\otimes E$ 的每个元素都可写成若干项 $y\otimes av$ 的和，其中 $y\in F$，$a\in R$。不过，$y\otimes av=ay\otimes v$。在这些项的和中，可以使用左边的线性性：

$$
\sum_{i=1}^n(y_i\otimes v)=\left(\sum_{i=1}^ny_i\right)\otimes v,\quad y_i\in F.
$$

因此，每个元素实际上都具有 $y\otimes v$ 的形式，其中某个 $y\in F$。

有一个双线性映射

$$
F\times E\to F,
$$

由 $(y,av)\mapsto ay$ 给出，它诱导一个线性映射

$$
F\otimes E\mapsto F.
$$

另外还有线性映射 $F\to F\otimes E$，由 $y\mapsto y\otimes v$ 给出。显然，这些映射互为逆映射，因此有同构

$$
F\otimes E\approx F.
$$

所以，$F\otimes E$ 的每个元素都可以*唯一地*写成 $y\otimes v$ 的形式，其中 $y\in F$。

**命题 2.3.** *令 $E$ 在 $R$ 上自由，具有基 $\{v_i\}_{i\in I}$。则 $F\otimes E$ 的每个元素都有唯一的表达式*

$$
\sum_{i\in I}y_i\otimes v_i,\quad y_i\in F,
$$

*其中除有限多个外，所有 $y_i=0$。*

*证明。* 这立即由一维情形的讨论及命题 2.1 的推论得到。

**推论 2.4.** *令 $E,F$ 在 $R$ 上自由，分别具有基 $\{v_i\}_{i\in I}$ 和 $\{w_j\}_{j\in J}$。则 $E\otimes F$ 自由，具有基 $\{v_i\otimes w_j\}$。有*

$$
\dim(E\otimes F)=(\dim E)(\dim F).
$$

<span class="original-page-anchor" id="pdf-page-619" aria-hidden="true"></span>

*证明。* 直接由命题得到。

可见，当 $E$ 在 $R$ 上自由时，张量积中没有信息消失。$F\otimes E$ 的每个元素都可看作 $E$ 的一组基中各元素的“形式”线性组合，系数属于 $F$。

特别地，在对应 $x\mapsto x\otimes1$ 下，$R\otimes E$（或 $E\otimes R$）同构于 $E$。

**命题 2.5.** *令 $E,F$ 为 $R$ 上有限维的自由模。则有同构*

$$
\operatorname{End}_R(E)\otimes\operatorname{End}_R(F)\to\operatorname{End}_R(E\otimes F),
$$

*它是唯一满足*

$$
f\otimes g\mapsto T(f,g)
$$

*的线性映射，其中 $f\in\operatorname{End}_R(E)$，$g\in\operatorname{End}_R(F)$。*

[注意，这里的左端张量积是在两个模 $\operatorname{End}_R(E)$ 和 $\operatorname{End}_R(F)$ 的张量积中取的。]

*证明。* 令 $\{v_i\}$ 为 $E$ 的一组基，$\{w_j\}$ 为 $F$ 的一组基。则 $\{v_i\otimes w_j\}$ 为 $E\otimes F$ 的一组基。对每一对指标 $(i',j')$，存在唯一的 $E$ 的自同态 $f=f_{i,i'}$ 和 $F$ 的自同态 $g=g_{j,j'}$，使

$$
f(v_i)=v_{i'}\quad\text{且}\quad f(v_\nu)=0\quad\text{若 }\nu\neq i,
$$

$$
g(w_j)=w_{j'}\quad\text{且}\quad g(w_\mu)=0\quad\text{若 }\mu\neq j.
$$

此外，族 $\{f_{i,i'}\}$ 和 $\{g_{j,j'}\}$ 分别为 $\operatorname{End}_R(E)$ 和 $\operatorname{End}_R(F)$ 的基。于是

$$
T(f,g)(v_\nu\otimes w_\mu)=\begin{cases}v_{i'}\otimes w_{j'}&\text{若 }(\nu,\mu)=(i,j),\\0&\text{若 }(\nu,\mu)\neq(i,j).\end{cases}
$$

因此，族 $\{T(f_{i,i'},g_{j,j'})\}$ 为 $\operatorname{End}_R(E\otimes F)$ 的一组基。由于族 $\{f_{i,i'}\otimes g_{j,j'}\}$ 是 $\operatorname{End}_R(E)\otimes\operatorname{End}_R(F)$ 的一组基，命题的断言已经清楚。

在命题 2.5 中可见，对于自由有限维模这一重要特殊情形，$f\otimes g$ 中张量积符号的歧义实际上消除了。后面讨论模的张量代数时，将看到命题 2.5 的一个重要应用。

**命题 2.6.** *令*

$$
0\to E'\xrightarrow{\varphi}E\xrightarrow{\psi}E''\to0
$$

<span class="original-page-anchor" id="pdf-page-620" aria-hidden="true"></span>

*为一个正合列，$F$ 为任意模。则序列*

$$
F\otimes E'\to F\otimes E\to F\otimes E''\to0
$$

*正合。*

*证明。* 给定 $x''\in E''$ 和 $y\in F$，存在 $x\in E$，使 $x''=\psi(x)$，因此 $y\otimes x''$ 是 $y\otimes x$ 在线性映射

$$
F\otimes E\to F\otimes E''
$$

下的像。

由于形如 $y\otimes x''$ 的元素生成 $F\otimes E''$，前述线性映射是满射。还容易验证，映射

$$
F\otimes E'\to F\otimes E
$$

的像包含在映射

$$
F\otimes E\to F\otimes E''
$$

的核中。

反过来，令 $I$ 为 $F\otimes E'\to F\otimes E$ 的像，令

$$
f:(F\otimes E)/I\to F\otimes E''
$$

为典范映射。我们将定义一个线性映射

$$
g:F\otimes E''\to(F\otimes E)/I,
$$

使 $g\circ f=\mathrm{id}$。这显然意味着 $f$ 是单射，因而证明所需的逆向包含关系。

令 $y\in F$，$x''\in E''$。取 $x\in E$，使 $\psi(x)=x''$。通过

$$
(y,x'')\mapsto y\otimes x\pmod I
$$

定义映射 $F\times E''\to(F\otimes E)/I$，并断言这个映射良定义，即不依赖于满足 $\psi(x)=x''$ 的 $x$ 的选择。若 $\psi(x_1)=\psi(x_2)=x''$，则 $\psi(x_1-x_2)=0$；由假设，对于某个 $x'\in E'$，有 $x_1-x_2=\varphi(x')$。于是

$$
y\otimes x_1-y\otimes x_2=y\otimes(x_1-x_2)=y\otimes\varphi(x').
$$

这表明 $y\otimes x_1\equiv y\otimes x_2\pmod I$，证明了映射良定义。它显然是双线性的，所以通过张量积上的一个线性映射 $g$ 分解。显然，$g\circ f$ 在形如 $y\otimes x$ 的元素上的限制是恒等映射。由于这些元素生成 $F\otimes E$，可知 $f$ 是单射，证明完毕。

<span class="original-page-anchor" id="pdf-page-621" aria-hidden="true"></span>

*序列*

$$
0\to F\otimes E'\to F\otimes E\to F\otimes E''\to0
$$

*并非总是正合的。* 如果命题 2.6 中的第一个序列分裂，也就是说 $E$ 本质上是 $E'$ 和 $E''$ 的直和，那么它正合。这是命题 2.1 的一个直接推论。读者应补全细节，以熟悉张量积的形式体系。

**命题 2.7.** *令 $\mathfrak a$ 为 $R$ 的一个理想，$E$ 为一个模。则由*

$$
(a,x)\mapsto ax\pmod{\mathfrak a E},\quad a\in R,\ x\in E
$$

*诱导的映射 $(R/\mathfrak a)\times E\to E/\mathfrak a E$ 是双线性的，并诱导同构*

$$
(R/\mathfrak a)\otimes E\xrightarrow{\approx}E/\mathfrak a E.
$$

*证明。* 映射 $(a,x)\mapsto ax\pmod{\mathfrak a E}$ 显然诱导从 $R/\mathfrak a\times E$ 到 $E/\mathfrak a E$ 的满双线性映射，因而诱导从 $R/\mathfrak a\otimes E$ 到 $E/\mathfrak a E$ 的满线性映射。可以构造逆映射，因为有一个良定义的线性映射

$$
E\to R/\mathfrak a\otimes E,
$$

由 $x\mapsto\overline1\otimes x$ 给出（其中 $\overline1$ 是 $1$ 在 $R/\mathfrak a$ 中的剩余类）。显然，$\mathfrak a E$ 包含于最后这个线性映射的核中，从而得到同态

$$
E/\mathfrak a E\to R/\mathfrak a\otimes E.
$$

可以立即验证，它是命题中所述同态的逆映射。

对应 $E\mapsto E/\mathfrak a E\approx R/\mathfrak a\otimes E$ 常称为**约化映射**。在 §4 中，将把这一约化映射解释为基环的扩张。

## §3. 平坦模

命题 2.6 中左边的箭头在什么条件下是单射，这个问题引出了满足这一性质的模的理论。我们沿用 Serre 的称呼，把它们称为平坦模。因此，形式上，以下条件等价，并定义一个**平坦模** $F$，它本应称为**张量正合模**。

**F 1.** 对每个正合列

$$
E'\to E\to E'',
$$

<span class="original-page-anchor" id="pdf-page-622" aria-hidden="true"></span>

序列

$$
F\otimes E'\to F\otimes E\to F\otimes E''
$$

正合。

**F 2.** 对每个短正合列

$$
0\to E'\to E\to E''\to0,
$$

序列

$$
0\to F\otimes E'\to F\otimes E\to F\otimes E''\to0
$$

正合。

**F 3.** 对每个单射 $0\to E'\to E$，序列

$$
0\to F\otimes E'\to F\otimes E
$$

正合。

显然，**F 1** 蕴含 **F 2**，**F 2** 蕴含 **F 3**。最后，写出映射 $E'\to E$ 的核和像，并应用 **F 3**，就可见 **F 3** 蕴含 **F 1**。细节留给读者。

下面的命题给出平坦性的判别法以及例子。

**命题 3.1.**

(i) *基环作为自身上的模是平坦的。*

(ii) *令 $F=\bigoplus F_i$ 为一个直和。则 $F$ 平坦，当且仅当每个 $F_i$ 都平坦。*

(iii) *投射模是平坦的。*

本命题中表述的性质基本上是范畴性的，参见本节末尾关于抽象的一般原理的说明。另一方面，还有以下与局部化有关的判别法。

**命题 3.2.**

(i) *令 $S$ 为 $R$ 的一个乘法子集。则 $S^{-1}R$ 在 $R$ 上平坦。*

(ii) *模 $M$ 在 $R$ 上平坦，当且仅当对 $R$ 的每个素理想 $\mathfrak p$，局部化 $M_{\mathfrak p}$ 在 $R_{\mathfrak p}$ 上平坦。*

(iii) *令 $R$ 为一个主理想整环。模 $F$ 平坦，当且仅当 $F$ 无挠。*

证明很简单，留给读者。不过，下文将证明更困难的平坦性判别法。

**非平坦的例子。** 若 $R$ 为一个整环，且 $R$ 上的模 $M$ 有挠，则 $M$ 不平坦。（证明这一点，它是直接的。）

<span class="original-page-anchor" id="pdf-page-623" aria-hidden="true"></span>

另一类例子说明了另一种不良现象。令 $R$ 为 $\mathbf Q$ 的一个有限扩张 $K$ 中的某个环，使 $R$ 是 $\mathbf Z$ 上的有限模，但不是整闭的。令 $R'$ 为其整闭包。令 $\mathfrak p$ 为 $R$ 的一个极大理想，并假设 $\mathfrak pR'$ 包含在两个不同的极大理想 $\mathfrak P_1$ 和 $\mathfrak P_2$ 中。则可以证明 $R'$ 在 $R$ 上不平坦；否则 $R'$ 在局部环 $R_{\mathfrak p}$ 上将是自由的，且秩必须为 $1$，从而排除了两个素理想 $\mathfrak P_1$ 和 $\mathfrak P_2$ 的可能性。实际构造这种情形的一个数值例子，是给读者的很好的练习。同类型的例子可以用环 $R=k[x,y]$ 构造，其中 $k$ 为一个代数闭域，甚至可以取特征为 $0$，而 $x,y$ 由 $k$ 上一个不可约多项式方程 $f(x,y)=0$ 联系起来。取 $R$ 为非整闭环，使其整闭包同样将 $R$ 的一个素理想 $\mathfrak p$ 分裂成两个素理想。在这些类似情形的每一种中，都称 $\mathfrak p$ 处有一个奇点。

第三个例子，令 $R$ 为域 $k$ 上多于一个变量的幂级数环。令 $\mathfrak m$ 为极大理想。则 $\mathfrak m$ 不平坦；否则，由下文的定理 3.8，$\mathfrak m$ 将是自由的；若 $R=k[[x_1,\ldots,x_n]]$，则 $x_1,\ldots,x_n$ 将是 $\mathfrak m$ 在 $R$ 上的一组基，而这显然不成立，因为当 $n\geq2$ 时，$x_1,x_2$ 在 $R$ 上线性相关。当然，同一论证适用于任何满足 $\mathfrak m/\mathfrak m^2$ 在 $R/\mathfrak m$ 上维数 $\geq2$ 的局部环 $R$。

接下来给出模平坦的更多判别法。证明中，我们将处处应用蛇引理。参见本节末尾的说明。

**引理 3.3.** *令 $F$ 平坦，并假设*

$$
0\to N\to M\to F\to0
$$

*为一个正合列。则对任意 $E$，有正合列*

$$
0\to N\otimes E\to M\otimes E\to F\otimes E\to0.
$$

*证明。* 用正合列

$$
0\to K\to L\to E\to0
$$

把 $E$ 表示为一个平坦模 $L$ 的商模。

<span class="original-page-anchor" id="pdf-page-624" aria-hidden="true"></span>

于是有以下正合且交换的图：

![张量积的正合交换图：各行依次为 N、M、F，各列依次为 K、L、E，保留了原图的全部零项。](/library/volume-86/diagrams/pdf-0624-flat-snake-diagram.png)

右上方的 $0$ 来自 $F$ 平坦的假设。左边的 $0$ 来自 $L$ 平坦这一事实。蛇引理给出正合列

$$
0\to N\otimes E\to M\otimes E,
$$

从而证明引理。

**命题 3.4.** *令*

$$
0\to F'\to F\to F''\to0
$$

*为一个正合列，并假设 $F''$ 平坦。则 $F$ 平坦，当且仅当 $F'$ 平坦。更一般地，令*

$$
0\to F^0\to F^1\to\cdots\to F^n\to0
$$

*为一个正合列，其中 $F^1,\ldots,F^n$ 平坦。则 $F^0$ 平坦。*

<span class="original-page-anchor" id="pdf-page-625" aria-hidden="true"></span>

**证明。** 设 $0\to E'\to E$ 是单射。我们有如下正合交换图：

![用于证明平坦性的正合交换图](/library/volume-86/diagrams/pdf-0625-flat-comparison.png)

顶端的 $0$ 来自 $F''$ 平坦这一假设，左端的两个零则由引理 3.3 保证。若 $F'$ 平坦，则第一个竖直映射是单射，由蛇引理可知 $F$ 平坦。若 $F$ 平坦，则中间一列的映射是单射。于是，由左端的两个零以及左侧方块的交换性，映射 $F'\otimes E'\to F'\otimes E$ 是单射，因此 $F'$ 平坦。这就证明了第一个断言。

第二个断言用归纳法证明：像维数移位中那样，在每一步引入核与余核，并在每一步应用第一个断言。这就证明了命题。

为了能够灵活地检验平坦性，下面两个引理很有用，它们将平坦性的概念与某个特定的模联系起来。具体而言，我们称 $F$ 为 **$E$-平坦的**，或称 $F$ **对 $E$ 平坦**，如果对每个单态射

$$
0\to E'\to E,
$$

取张量积后所得的序列

$$
0\to F\otimes E'\to F\otimes E
$$

也正合。

**引理 3.5。** *假设 $F$ 是 $E$-平坦的。那么 $F$ 对 $E$ 的每个子模以及每个商模也都平坦。*

**证明。** 关于子模的部分是直接的，因为如果 $E'_1\subset E'_2\subset E$ 是子模，并且 $F\otimes E'_1\to F\otimes E$ 是单态射，那么 $F\otimes E'_1\to F\otimes E'_2$ 也是单态射：它与 $F\otimes E'_2\to F\otimes E$ 的复合映射是单态射。需要考虑的只有商模。假设有正合列

$$
0\to N\to E\to M\to 0.
$$

设 $M'$ 是 $M$ 的子模，$E'$ 是它在 $E$ 中的逆像。那么我们有一个<span class="original-page-anchor" id="pdf-page-626" aria-hidden="true"></span>由正合列组成的交换图：

![商模的子模所对应的正合列交换图](/library/volume-86/diagrams/pdf-0626-subquotient-sequences.png)

与 $F$ 取张量积后，得到如下正合交换图：

![取张量积后的交换图及核 K](/library/volume-86/diagrams/pdf-0626-subquotient-snake.png)

其中 $K$ 是我们要证明为 $0$ 的、尚待确定的核。但是，由蛇引理得到正合列

$$
0\to K\to 0,
$$

证明即告完成。

**引理 3.6。** *设 $\{E_i\}$ 是一族模，并假设 $F$ 对每个 $E_i$ 都平坦。那么 $F$ 对它们的直和也平坦。*

**证明。** 令 $E=\bigoplus E_i$ 为它们的直和。我们必须证明：给定 $E$ 的任意子模 $E'$，序列

$$
0\to F\otimes E'\to F\otimes E=\bigoplus F\otimes E_i
$$

是正合的。注意，如果 $F\otimes E'$ 的某个元素映入直和后变为 $0$，那么它在某个有限子直和中就已经变为 $0$，所以不失一般性，可以假设指标集是有限的。再由归纳法，可以假设指标集由两个元素组成，因此有两个模 $E_1$ 和 $E_2$，且 $E=E_1\oplus E_2$。设 $N$ 是 $E$ 的子模。令 $N_1=N\cap E_1$，并令 $N_2$ 为 $N$ 在投影到 $E_2$ 下的像。那么<span class="original-page-anchor" id="pdf-page-627" aria-hidden="true"></span>我们有如下交换正合图：

![直和的子模所对应的交换正合图](/library/volume-86/diagrams/pdf-0627-direct-sum-sequences.png)

与 $F$ 取张量积，得到如下正合交换图：

![直和所对应的取张量积后的正合交换图](/library/volume-86/diagrams/pdf-0627-direct-sum-tensor-sequences.png)

左下方的正合性来自 $E=E_1\oplus E_2$ 这一事实。于是，蛇引理说明中间竖直映射的核为 $0$。引理得证。

下面的命题说明，为了检验平坦性，只需对由理想产生的一类特殊的正合列进行检验。

**命题 3.7。** *$F$ 平坦，当且仅当对 $R$ 的每个理想 $\mathfrak a$，自然映射*

$$
\mathfrak a\otimes F\to\mathfrak aF
$$

*是同构。事实上，$F$ 平坦，当且仅当对 $R$ 的每个理想 $\mathfrak a$，将序列*

$$
0\to\mathfrak a\to R\to R/\mathfrak a\to 0
$$

*与 $F$ 取张量积后得到正合列。*

**证明。** 若 $F$ 平坦，那么与 $F$ 取张量积并应用命题 2.7，就可知这个自然映射是同构，因为 $\mathfrak aM$ 是 $M\to M/\mathfrak aM$ 的核。反过来，假设对所有理想 $\mathfrak a$，此映射都是同构。这意味着<span class="original-page-anchor" id="pdf-page-628" aria-hidden="true"></span>$F$ 是 $R$-平坦的。由引理 3.6，$F$ 对任意多个 $R$ 的直和都平坦，而任意模 $M$ 都是这样一个直和的商模，所以由引理 3.5，$F$ 是 $M$-平坦的，证明即告完成。

**关于抽象的一般原理的注记。** 命题 3.1(i)、(ii)、(iii) 以及命题 3.3 至 3.7 的证明，本质上都植根于抽象的一般原理，且只依赖于箭头之间的论证。具体地，像第二十章 §8 中那样，假设在两个不同的阿贝尔范畴 $\mathfrak A$ 和 $\mathfrak B$ 上有一个双函子 $T$，对每个 $A$，函子 $B\mapsto T(A,B)$ 都右正合，对每个 $B$，函子 $A\mapsto T(A,B)$ 也都右正合。我们用另一种说法来代替“平坦”：如果 $B\mapsto T(A,B)$ 是正合函子，就称 $\mathfrak A$ 的对象 $A$ 为 **$T$-正合的**；如果 $A\mapsto T(A,L)$ 正合，就称 $\mathfrak B$ 的对象 $L$ 为 **${}^tT$-正合的**。于是，与基环和自由模有关的条件可以用如下抽象的一般条件代替。

在引理 3.3 使用 $L$ 的地方，需要假设：对 $\mathfrak B$ 的每个对象 $E$，都有一个 ${}^tT$-正合的 $L$，以及一个满态射

$$
L\to E\to 0.
$$

对于命题 3.7 的类似结论，需要假设 $\mathfrak B$ 中存在某个对象 $R$，使得 $F$ 是 $R$-正合的，也就是说，给定一个正合列

$$
0\to\mathfrak a\to R,
$$

则 $0\to T(F,\mathfrak a)\to T(F,R)$ 正合；还需假设 $R$ 是一个生成对象，即每个对象 $B$ 都是以某个指标族为指标的若干个 $R$ 的直和的商，并且 $T$ 保持直和。

蛇引理在任意阿贝尔范畴中都成立，这既可以归因于其证明具有“函子性”，也可以通过表示函子将问题归约到阿贝尔群范畴。你可以任选一种方法。

特别地，我们实际上不需要基环是交换环；先前作此假设，只是为了使表述简洁。

现在我们转向一些稍有不同的考虑。

**定理 3.8。** *设 $R$ 是交换局部环，$M$ 是 $R$ 上的有限生成平坦模。那么 $M$ 是自由模。事实上，若 $x_1,\ldots,x_n\in M$ 是 $M$ 的元素，它们的剩余类构成 $M/\mathfrak mM$ 在 $R/\mathfrak m$ 上的一组基，那么 $x_1,\ldots,x_n$ 就构成 $M$ 在 $R$ 上的一组基。*

**证明。** 设 $R^{(n)}\to M$ 是将 $R^{(n)}$ 的单位向量分别映到 $x_1,\ldots,x_n$ 的映射，令 $N$ 为它的核。我们得到正合列

$$
0\to N\to R^{(n)}\to M,
$$

<span class="original-page-anchor" id="pdf-page-629" aria-hidden="true"></span>

从而得到交换图

![局部环上的有限生成平坦模所对应的交换图](/library/volume-86/diagrams/pdf-0629-local-flat-module.png)

其中各行正合。由于假设 $M$ 平坦，映射 $h$ 是单射。由蛇引理得到正合列

$$
0\to\operatorname{coker}f\to\operatorname{coker}g\to\operatorname{coker}h,
$$

而右侧的箭头就是

$$
R^{(n)}/\mathfrak mR^{(n)}\to M/\mathfrak mM.
$$

根据对 $x_1,\ldots,x_n$ 的假设，这是同构。因此 $\operatorname{coker}f=0$，从而 $\mathfrak mN=N$；如果 $R$ 是诺特环，那么 $N$ 是有限生成的，于是由中山引理得 $N=0$。如果不假设 $R$ 是诺特环，那么在 $M$ 是有限表示模的情形，需要补充下面这样一个小论证。

**引理 3.9。** *假设 $M$ 是有限表示模，并且*

$$
0\to N\to E\to M\to 0
$$

*正合，其中 $E$ 是有限生成自由模。那么 $N$ 是有限生成的。*

**证明。** 设

$$
L_1\to L_2\to M\to 0
$$

是 $M$ 的一个有限表示，即一个正合列，其中 $L_1,L_2$ 都是有限生成自由模。利用自由性，存在交换图

![有限表示与给定正合列之间的交换图](/library/volume-86/diagrams/pdf-0629-finite-presentation.png)

使得 $L_2\to E$ 是满射。于是蛇引理立即给出正合列

$$
0\to\operatorname{coker}(L_1\to N)\to 0,
$$

所以 $\operatorname{coker}(L_1\to N)=0$，从而 $N$ 是 $L_1$ 的一个像，因此有限生成。这就证明了引理，并且也完成了 $M$ 有限表示时定理 3.8 的证明。

<span class="original-page-anchor" id="pdf-page-630" aria-hidden="true"></span>

我们还没有在完全一般的情形下证明定理 3.8。为此，我们采用 Matsumura 的证明（见他的 *Commutative Algebra* 第 2 章），它建立在下面的引理之上。

**引理 3.10。** *假设 $M$ 是平坦 $R$-模。设 $a_i\in R$、$x_i\in M$（$i=1,\ldots,n$），并假设有关系*

$$
\sum_{i=1}^n a_ix_i=0.
$$

*那么存在整数 $s$ 以及元素 $b_{ij}\in R$ 和 $y_j\in M$（$j=1,\ldots,s$），使得*

$$
\sum_i a_ib_{ij}=0\quad\text{对所有 }j,
\qquad\text{且}\qquad
x_i=\sum_j b_{ij}y_j\quad\text{对所有 }i.
$$

**译校注：** 原书引理陈述中两处系数所属的环印作 $A$，即 $a_i\in A$、$b_{ij}\in A$。本引理的基环为 $R$，证明中的映射定义在 $R^{(n)}$ 上，末句也明确写 $b_{ij}\in R$；此处未另定义 $A$。译文据此统一为 $R$，英文转录保留原字。

*证明。* 考虑正合列

$$
0\to K\to R^{(n)}\to R,
$$

其中映射 $R^{(n)}\to R$ 定义为

$$
(b_1,\ldots,b_n)\mapsto\sum_{i=1}^n a_ib_i,
$$

$K$ 是它的核。由于 $M$ 平坦，可知

$$
K\otimes M\to M^{(n)}\xrightarrow{f_M}M
$$

正合，其中 $f_M$ 定义为

$$
f_M(z_1,\ldots,z_n)=\sum_{i=1}^n a_iz_i.
$$

因此，存在元素 $\beta_j\in K$ 和 $y_j\in M$，使得

$$
(x_1,\ldots,x_n)=\sum_{j=1}^s\beta_jy_j.
$$

将 $\beta_j$ 写成 $(b_{1j},\ldots,b_{nj})$，其中 $b_{ij}\in R$。这就证明了引理。

现在可以应用这个引理，完全按照第 X 章定理 4.4 中证明局部环上的有限投射模是自由模的相同方法，用归纳法证明本定理。证明到此结束。

**注。** 在我所知道的应用中，基环都是诺特环，因此最初给出的那个非常简单的证明就够用了。我不愿损害这个证明的简洁性，正因如此，才按照一般性逐步增加的顺序给出这些额外的技术细节。

<span class="original-page-anchor" id="pdf-page-631" aria-hidden="true"></span>

**同调的应用。** 本节最后，我们为希望沿这一思路继续研究的读者，指出张量积与第 XX 章 §8 中的同调讨论之间的联系。张量积是一个双函子，可以对它应用第 XX 章 §8 中的讨论。设 $M,N$ 为模。设

$$
\cdots\to E_i\to E_{i-1}\to E_0\to M\to0
$$

是 $M$ 的一个自由解消或投射解消，即一个正合列，其中对所有 $i\geqq0$，$E_i$ 都是自由模或投射模。把这个序列记作

$$
E_M\to M\to0.
$$

于是，按定义，

$$
\operatorname{Tor}_i(M,N)=\text{复形 }E\otimes N\text{ 的第 }i\text{ 个同调},
$$

也就是复形

$$
\cdots\to E_i\otimes N\to E_{i-1}\otimes N\to\cdots\to E_0\otimes N\to0
$$

的同调。

这个同调在相差唯一同构的意义下确定。读者可以采用任何合适的约定，固定一个解消，从而确定 $\operatorname{Tor}_i(M,N)$ 的一个固定表示；其他所有表示都通过唯一同构与它同构。

由于有双函子性的同构 $M\otimes N\approx N\otimes M$，还可得到对所有 $i$ 成立的双函子性同构

$$
\operatorname{Tor}_i(M,N)\approx\operatorname{Tor}_i(N,M).
$$

参见第 XX 章命题 8.2 和 8.2′。

按照一般原则，如果对所有 $i>d$ 及所有 $N$，都有 $\operatorname{Tor}_i(M,N)=0$，就称 $M$ 的 **Tor 维数** $\leqq d$。由第 XX 章 §8 可得下面的结果，它只是把 $T$-正合替换为平坦。

**定理 3.11。** *关于模 $M$，下列三个条件等价。*

(i) *$M$ 平坦。*

(ii) *对所有 $N$，都有 $\operatorname{Tor}_1(M,N)=0$。*

(iii) *对所有 $i\geqq1$ 及所有 $N$，都有 $\operatorname{Tor}_i(M,N)=0$；换言之，$M$ 的 Tor 维数为 $0$。*

**注。** 愿意使用这一刻画的读者，可以用 Tor 维数的论证替换前面 3.3 至 3.6 中的某些证明。这种论证更为形式化，或者至少以另一种方式形式化，可能显得更快捷。前面的每个情形中，都是专门使用蛇引理来证明所需的结果。一旦建立了导出函子的一般理论，一般同调理论便只需以相应的形式同调步骤代替蛇引理的这种用法。

<span class="original-page-anchor" id="pdf-page-632" aria-hidden="true"></span>

## §4. 基环的扩张

设 $R$ 为交换环，$E$ 为一个 $R$-模。这里特别指明 $R$，因为接下来将同时处理几个环。设 $R\to R'$ 为交换环同态，于是 $R'$ 是一个 $R$-代数，也可以看作一个 $R$-模。有一个三重多线性映射

$$
R'\times R'\times E\to R'\otimes E,
$$

定义规则为

$$
(a,b,x)\mapsto ab\otimes x.
$$

因此，它诱导出一个 $R$-线性映射

$$
R'\otimes(R'\otimes E)\to R'\otimes E,
$$

从而也得到一个 $R$-双线性映射 $R'\times(R'\otimes E)\to R'\otimes E$。立即可以验证，最后这个映射使 $R'\otimes E$ 成为一个 $R'$-模。我们称它为 **$E$ 在 $R'$ 上的扩张**，记作 $E_{R'}$。也说 $E_{R'}$ 是将**基环扩张**，从 $R$ 扩张到 $R'$ 而得到的。

**例 1。** 设 $\mathfrak a$ 为 $R$ 的理想，$R\to R/\mathfrak a$ 为典范同态。那么，$E$ 到 $R/\mathfrak a$ 的扩张也称为 $E$ 模 $\mathfrak a$ 的**约化**。在整数环上，这种情形经常出现：将一个对象模素数 $p$ 约化，即模素理想 $(p)$ 约化。

**例 2。** 设 $R$ 为域，$R'$ 为扩域。那么 $E$ 是 $R$ 上的向量空间，$E_{R'}$ 是 $R'$ 上的向量空间。借助一组基，可以看到这个扩张正好给出上一章提到的构造。习题中将进一步展开这个例子。

画出与域论中相同的图：

![基环扩张示意图](/library/volume-86/diagrams/pdf-0632-base-diamond.png)

以直观表示基环的扩张。由命题 2.3 可得：

**命题 4.1。** *设 $E$ 是 $R$ 上的自由模，基为 $\{v_i\}_{i\in I}$。令 $v_i'=1\otimes v_i$。那么 $E_{R'}$ 是 $R'$ 上的自由模，基为 $\{v_i'\}_{i\in I}$。*

我们在说明自由模的维数有定义，即两组基具有相同的<span class="original-page-anchor" id="pdf-page-633" aria-hidden="true"></span>基数时，已经使用了这个命题的一个特殊情形。事实上，当时我们模 $R$ 的一个极大理想约化，把问题归结为域上的向量空间问题。

开始变换环时，最好在张量积的记号中指明 $R$。因此写成

$$
E_{R'}=R'\otimes E=R'\otimes_R E.
$$

*基环的扩张具有传递性*，即若 $R\to R'\to R''$ 为一连串交换环同态，则有同构

$$
R''\otimes_R E\approx R''\otimes_{R'}(R'\otimes_R E),
$$

而且这是一个 $R''$-模同构。证明很简单，留给读者。

如果 $E$ 具有乘法结构，也可以针对这个乘法扩张基环。设 $R\to A$ 为环同态，使得 $R$ 在 $A$ 中的像的每个元素都与 $A$ 的每个元素交换，即给定一个 $R$-代数。设 $R\to R'$ 为交换环同态。有一个四重多线性映射

$$
R'\times A\times R'\times A\to R'\otimes A,
$$

定义为

$$
(a,x,b,y)\mapsto ab\otimes xy.
$$

它诱导出一个 $R$-线性映射

$$
R'\otimes A\otimes R'\otimes A\to R'\otimes A,
$$

从而诱导出一个 $R$-双线性映射

$$
(R'\otimes A)\times(R'\otimes A)\to R'\otimes A.
$$

很容易验证，刚刚定义的 $R'\otimes A$ 上的合成律满足结合律。$R'\otimes A$ 中有单位元，即 $1\otimes1$。还有一个从 $R'$ 到 $R'\otimes A$ 的环同态，定义为 $a\mapsto a\otimes1$。这样立即可见，$R'\otimes A=A_{R'}$ 是一个 $R'$-代数。注意，映射

$$
x\mapsto1\otimes x
$$

是从 $A$ 到 $R'\otimes A$ 的环同态，由此得到一个由环同态组成的交换图：

![代数基环扩张的交换图](/library/volume-86/diagrams/pdf-0633-algebra-diamond.png)

<span class="original-page-anchor" id="pdf-page-634" aria-hidden="true"></span>

为完整起见，我们给出基环扩张情形下几个常用的平坦性判别。

**命题 4.2。** *设 $R\to A$ 为一个 $R$-代数，并假定 $A$ 交换。*

(i) **基变换。** *若 $F$ 为平坦 $R$-模，则 $A\otimes_R F$ 为平坦 $A$-模。*

(ii) **传递性。** *若 $A$ 为平坦的交换 $R$-代数，$M$ 为平坦 $A$-模，则 $M$ 作为 $R$-模也是平坦的。*

证明是直接的，留给读者。

## §5. 若干函子性同构

先回顾一个抽象定义。设 $\mathfrak A,\mathfrak B$ 为两个范畴。从 $\mathfrak A$ 到 $\mathfrak B$ 的函子，例如单变量协变函子，可以看成一个范畴的对象，其态射定义如下。若 $L,M$ 为两个这样的函子，则态射 $H:L\to M$ 是一条规则：它给 $\mathfrak A$ 的每个对象 $X$ 指定 $\mathfrak B$ 中的态射 $H_X:L(X)\to M(X)$，使得对 $\mathfrak A$ 中的任意态射 $f:X\to Y$，下图交换：

$$
\begin{array}{ccc}
L(X)&\xrightarrow{H_X}&M(X)\\
{}_{L(f)}\downarrow&&\downarrow_{M(f)}\\
L(Y)&\xrightarrow{H_Y}&M(Y)
\end{array}
$$

因此，可以谈论函子的同构。下面的张量积理论中将给出这样的例子。在我们的应用中，范畴是加性的，即态射集是一个加法群，合成律是 $\mathbf Z$-双线性的。此时，若函子 $L$ 满足

$$
L(f+g)=L(f)+L(g),
$$

就称它为**加性函子**。

设 $R$ 为交换环，考虑从 $R$-模范畴到自身的加性函子。例如，可以把对偶模看成一个函子：

$$
E\mapsto E^\vee=L(E,R)=\operatorname{Hom}_R(E,R).
$$

类似地，有一个双变量函子：

$$
(E,F)\mapsto L(E,F)=\operatorname{Hom}_R(E,F),
$$

它对第一个变量反变，对第二个变量协变，并且是双加性的。

<span class="original-page-anchor" id="pdf-page-635" aria-hidden="true"></span>

下面给出几个与张量积有关的函子性同构的例子。为此，最方便的是先陈述一个一般定理，给出判别函子态射何时确为同构的准则。

**命题 5.1。** *设 $L,M$ 为从 $R$-模范畴到自身的两个函子，它们或者都协变，或者都反变。假设两个函子都是加性的。设 $H:L\to M$ 为函子态射。如果对每个 $R$ 上的一维自由模 $E$，$H_E:L(E)\to M(E)$ 都是同构，那么对每个 $R$ 上的有限维自由模，$H_E$ 都是同构。*

*证明。* 先给出一个引理。

**引理 5.2。** *设 $E$ 和 $E_i$（$i=1,\ldots,m$）为某个环上的模。设 $\varphi_i:E_i\to E$ 和 $\psi_i:E\to E_i$ 为满足下列性质的同态：*

$$
\psi_i\circ\varphi_i=\operatorname{id},\qquad
\psi_i\circ\varphi_j=0\quad\text{若 }i\ne j,
$$

$$
\sum_{i=1}^m\varphi_i\circ\psi_i=\operatorname{id}.
$$

*那么映射*

$$
x\mapsto(\psi_1x,\ldots,\psi_mx)
$$

*是 $E$ 到直积 $\prod_{i=1}^m E_i$ 上的同构，而映射*

$$
(x_1,\ldots,x_m)\mapsto\varphi_1x_1+\cdots+\varphi_mx_m
$$

*是该直积到 $E$ 上的同构。反过来，若 $E$ 等于子模 $E_i$（$i=1,\ldots,m$）的直和，令 $\varphi_i$ 为 $E_i$ 到 $E$ 中的包含映射，$\psi_i$ 为 $E$ 到 $E_i$ 上的投影，则这些映射满足上述性质。*

**译校注：** 原书逆向陈述把包含映射记为 $\psi_i$、投影记为 $\varphi_i$；这与引理开头的定义域和值域相反。按 $\varphi_i:E_i\to E$、$\psi_i:E\to E_i$，包含应为 $\varphi_i$，投影应为 $\psi_i$。译文据此更正，英文保留原字。

*证明。* 证明是常规的，实质上与第 III 章命题 3.1 的证明相同。将它留给读者作为练习。

注意，满足引理各性质的族 $\{\varphi_i\}$ 和 $\{\psi_i\}$ 具有函子性。例如，若 $T$ 是一个加性反变函子，那么族 $\{T(\psi_i)\}$ 和 $\{T(\varphi_i)\}$ 也满足引理中的性质。当 $T$ 为协变函子时也类似。

应用引理时，取各个模 $E_i$ 为按一组基分解 $E$ 所得的一维分量。例如，假定 $L,M$ 都协变。对每个模 $E$，有一个<span class="original-page-anchor" id="pdf-page-636" aria-hidden="true"></span>交换图：

$$
\begin{array}{ccc}
L(E)&\xrightarrow{H_E}&M(E)\\
{}_{L(\varphi_i)}\uparrow&&\uparrow_{M(\varphi_i)}\\
L(E_i)&\xrightarrow{H_{E_i}}&M(E_i)
\end{array}
$$

还有一个类似的图，将 $\varphi_i$ 换成 $\psi_i$，并将两个竖直箭头反向。因此，借助 $L(\psi_i)$ 和 $L(\varphi_i)$，得到 $L(E)$ 的一个直和分解；类似地，借助 $M(\psi_i)$ 和 $M(\varphi_i)$，得到 $M(E)$ 的直和分解。根据假设，$H_{E_i}$ 是同构。由此很容易推出 $H_E$ 是同构。例如，为证明单射性，将元素 $v\in L(E)$ 写成

$$
v=\sum L(\varphi_i)v_i,
$$

其中 $v_i\in L(E_i)$。若 $H_Ev=0$，则

$$
0=\sum H_EL(\varphi_i)v_i=\sum M(\varphi_i)H_{E_i}v_i.
$$

由于映射 $M(\varphi_i)$（$i=1,\ldots,m$）给出 $M(E)$ 的直和分解，可得对所有 $i$ 都有 $H_{E_i}v_i=0$，从而 $v_i=0$，于是 $v=0$。满射性也同样简单。

对于每个变量都加性的多变量函子，可以固定除一个变量以外的全部变量，然后应用这个命题。下面的推论中就采用这种方法。

**推论 5.3。** *设 $E',E,F',F$ 都是 $R$ 上的有限维自由模。那么有函子性同构*

$$
L(E',E)\otimes L(F',F)\to L(E'\otimes F',E\otimes F),
$$

*它满足*

$$
f\otimes g\mapsto T(f,g).
$$

*证明。* 固定 $E,F',F$，将 $L(E',E)\otimes L(F',F)$ 看成变量 $E'$ 的函子。同样，将

$$
L(E'\otimes F',E\otimes F)
$$

看成 $E'$ 的函子。映射 $f\otimes g\mapsto T(f,g)$ 具有函子性，因此由引理，只需证明在 $E'$ 的维数为 $1$ 时，它给出一个同构。现在假设处于这种情形：固定一维的 $E'$，将推论中的两个表达式看成变量 $E$ 的函子。再次应用引理，<span class="original-page-anchor" id="pdf-page-637" aria-hidden="true"></span>只需证明在 $E$ 的维数为 $1$ 时，这个箭头是同构。同样，也可假设 $F,F'$ 的维数为 $1$。此时，验证该箭头为同构是很简单的事，正如所需。

**推论 5.4。** *设 $E,F$ 为有限维自由模。那么有自然同构*

$$
\operatorname{End}_R(E)\otimes\operatorname{End}_R(F)\to\operatorname{End}_R(E\otimes F).
$$

*证明。* 这是推论 5.3 的特殊情形。

注意，推论 5.4 前面已经证明过。这里再次提到它，只是为了看出它如何与当前的观点相配合。

**推论 5.5。** *设 $E,F$ 为 $R$ 上的有限维自由模。有一个函子性同构*

$$
E^\vee\otimes F\to L(E,F),
$$

*它对 $\lambda\in E^\vee$ 和 $y\in F$ 由以下映射给出：*

$$
\lambda\otimes y\mapsto A_{\lambda,y},
$$

*其中 $A_{\lambda,y}$ 满足：对所有 $x\in E$，有 $A_{\lambda,y}(x)=\lambda(x)y$。*

推论 5.5 中的逆同构可以如下描述。设 $\{v_1,\ldots,v_n\}$ 为 $E$ 的一组基，$\{v_1',\ldots,v_n'\}$ 为对偶基。若 $A\in L(E,F)$，则元素

$$
\sum_{i=1}^n v_i'\otimes A(v_i)\in E^\vee\otimes F
$$

映到 $A$。特别地，若 $E=F$，则映到恒等映射 $\operatorname{id}_E$ 的元素称为 **Casimir 元素**：

$$
\sum_{i=1}^n v_i'\otimes v_i,
$$

它与基的选择无关。参见习题 14。

为了证明推论 5.5，先说明所写公式给出了一个从 $E^\vee\otimes F$ 到 $L(E,F)$ 的良定同态，再验证它既是单射又是满射。细节留作练习。

微分几何学家很喜欢同构

$$
L(E,E)\to E^\vee\otimes E,
$$

在从几何角度考虑 $L(E,E)$ 时，经常使用 $E^\vee\otimes E$。这样就强调了一次不必要的对偶化和一种无关的形式体系，而直接处理 $L(E,E)$ 本来更加容易。在微分几何中，人们把各种函子 $L$ 应用于流形上一点处的切空间，所得空间中的元素称为**张量**（类型为 $L$）。

<span class="original-page-anchor" id="pdf-page-638" aria-hidden="true"></span>

**推论 5.6。** *设 $E,F$ 为 $R$ 上的有限维自由模。有一个函子性同构*

$$
E^\vee\otimes F^\vee\to(E\otimes F)^\vee,
$$

*它对 $\lambda\in E^\vee$ 和 $\mu\in F^\vee$ 由以下映射给出：*

$$
\lambda\otimes\mu\mapsto\Lambda,
$$

*其中 $\Lambda$ 满足：对所有 $x\in E$ 和 $y\in F$，有*

$$
\Lambda(x\otimes y)=\lambda(x)\mu(y).
$$

*证明。* 与前面相同。

最后，将下面的结果留作练习。

**命题 5.7。** *设 $E$ 为 $R$ 上的有限维自由模。$L(E,E)$ 上的迹函数等于以下两个映射的复合：*

$$
L(E,E)\to E^\vee\otimes E\to R,
$$

*其中，第一个映射是推论 5.5 中所描述同构的逆映射，第二个映射由双线性映射*

$$
(\lambda,x)\mapsto\lambda(x)
$$

*诱导。*

当然，正是在涉及迹的情形中，推论 5.5 的同构才显得重要，并且用到了 $E$ 的有限维性。在许多应用中，这种有限维性不起作用，直接处理 $L(E,E)$ 更合适。

## §6. 代数的张量积

本节仍设 $R$ 为交换环。所谓 **$R$-代数**，是指从 $R$ 到环 $A$ 的一个环同态 $R\to A$，使得 $R$ 的像包含在 $A$ 的中心中。

设 $A,B$ 为 $R$-代数。我们将使 $A\otimes B$ 成为一个 $R$-代数。给定 $(a,b)\in A\times B$，有一个 $R$-双线性映射

$$
M_{a,b}:A\times B\to A\otimes B,
\quad\text{满足}\quad
M_{a,b}(a',b')=aa'\otimes bb'.
$$

因此，$M_{a,b}$ 诱导一个 $R$-线性映射 $m_{a,b}:A\otimes B\to A\otimes B$，满足 $m_{a,b}(a'\otimes b')=aa'\otimes bb'$。

**译校注：** 原书在描述诱导线性映射时仍写作 $m_{a,b}(a',b')$。译文将这一写法展开为 $m_{a,b}(a'\otimes b')$，明确它的自变量是 $A\otimes B$ 中的纯张量；前一个双线性映射 $M_{a,b}$ 的自变量才是有序对 $(a',b')$。这里说明诱导映射的记号含义，乘法公式保持原意。

但 $m_{a,b}$ 双线性地依赖于 $a$ 和 $b$，因此最终得到唯一的 $R$-双线性映射

$$
A\otimes B\times A\otimes B\to A\otimes B,
$$

<span class="original-page-anchor" id="pdf-page-639" aria-hidden="true"></span>

使得 $(a\otimes b)(a'\otimes b')=aa'\otimes bb'$。这个映射显然满足结合律，并且有一个自然环同态

$$
R\to A\otimes B,\quad\text{定义为}\quad c\mapsto1\otimes c=c\otimes1.
$$

因此，$A\otimes B$ 是一个 $R$-代数，称为**通常的张量积**。

### 应用：交换环

现在看看上述讨论对于交换环的意义。

**命题 6.1。** *交换环范畴中存在有限余积；一个交换环上的交换代数范畴中也存在有限余积。若 $R\to A$ 和 $R\to B$ 是两个交换环同态，则它们在 $R$ 上的余积是环同态 $R\to A\otimes B$，定义为*

$$
a\mapsto a\otimes1=1\otimes a.
$$

*证明。* 只证明两个环同态 $R\to A$ 和 $R\to B$ 的余积情形。一般情形可用归纳法。

设 $A,B$ 为交换环，并假设给定到交换环 $C$ 的环同态

$$
\varphi:A\to C\qquad\text{和}\qquad\psi:B\to C.
$$

于是可定义一个 $\mathbf Z$-双线性映射

$$
A\times B\to C,
$$

定义为 $(x,y)\mapsto\varphi(x)\psi(y)$。由此得到唯一的加法同态

$$
A\otimes B\to C,
$$

满足 $x\otimes y\mapsto\varphi(x)\psi(y)$。上面已经说明，可以在 $A\otimes B$ 上定义环结构，使得

$$
(a\otimes b)(c\otimes d)=ac\otimes bd.
$$

于是显然，映射 $A\otimes B\to C$ 是环同态。另有两个环同态

$$
A\xrightarrow{f}A\otimes B\qquad\text{和}\qquad B\xrightarrow{g}A\otimes B,
$$

定义为

$$
x\mapsto x\otimes1\qquad\text{和}\qquad y\mapsto1\otimes y.
$$

张量积的泛性质表明，$(A\otimes B,f,g)$ 是环 $A$ 和 $B$ 的余积。

若 $A,B,C$ 为 $R$-代数，并且 $\varphi,\psi$ 使下图<span class="original-page-anchor" id="pdf-page-640" aria-hidden="true"></span>交换，

![R-代数的交换图](/library/volume-86/diagrams/pdf-0640-coproduct-diamond.png)

则 $A\otimes B$ 也是一个 $R$-代数；事实上，按照使用上的需要，它可以看作 $R$、$A$ 或 $B$ 上的代数。而上面得到的映射 $A\otimes B\to C$ 是一个 $R$-代数同态。

交换环总能看作一个 $\mathbf Z$-代数，即整数环上的代数。因此，交换环的余积可看作 $R$-代数余积的特殊情形。

**分次代数。** 设 $G$ 为以加法记写的交换幺半群。所谓 **$G$-分次环**，是指一个环 $A$，它作为加法群可表示成直和

$$
A=\bigoplus_{r\in G}A_r,
$$

并且对所有 $r,s\in G$，环乘法将 $A_r\times A_s$ 映入 $A_{r+s}$。特别地，可见 $A_0$ 是一个子环。

$A_r$ 的元素称为**次数为 $r$ 的齐次元素**。

下面按同一种模式构造分次环的几个例子。假设对每个 $r\in G$ 给定一个以加法记写的阿贝尔群 $A_r$，并对每对 $r,s\in G$ 给定映射 $A_r\times A_s\to A_{r+s}$。假设 $A_0$ 为交换环，且这些映射下的合成满足结合律并具有 $A_0$-双线性。那么直和 $A=\bigoplus_{r\in G}A_r$ 是一个环：可按显然的方式定义乘法，即

$$
\left(\sum_{r\in G}x_r\right)\left(\sum_{s\in G}y_s\right)
=\sum_{t\in G}\left(\sum_{r+s=t}x_ry_s\right).
$$

上述乘积称为**通常乘积**。不过，还有另一种方式。假设分次取值于 $\mathbf Z$ 或 $\mathbf Z/2\mathbf Z$。将 $x\in A_r$ 与 $y\in A_s$ 的**超乘积**定义为 $(-1)^{rs}xy$，其中 $xy$ 为已给定的乘积。很容易验证，这个乘积满足结合律，并且扩张为与这些双线性映射相联系的所谓**超乘积** $A\otimes A\to A$。若 $R$ 为交换环，且 $A$ 是一个分次 $R$-代数，即除 $A$ 是分次环外，还对所有 $r$ 满足 $RA_r\subset A_r$，则在超乘积下 $A$ 仍是一个 $R$-代数，记为 $A_{\mathrm{su}}$，称为与 $A$ 相联系的**超代数**。

<span class="original-page-anchor" id="pdf-page-641" aria-hidden="true"></span>

**例。** 下一节将遇到张量代数 $T(E)$，它按照各个 $T^r(E)$ 的直和而分次，因此可按上述方法得到相应的超张量代数 $T_{\mathrm{su}}(E)$。

类似地，设 $A,B$ 为分次代数，像上面一样按自然数分次。将它们的**超张量积**

$$
A\otimes_{\mathrm{su}}B
$$

定义为作为分次模的通常张量积，但乘法采用**超乘积**

$$
(a\otimes b)(a'\otimes b')=(-1)^{(\deg b)(\deg a')}aa'\otimes bb',
$$

其中 $b,a'$ 分别为 $B$ 和 $A$ 的齐次元素。按通常方法可验证，$A\otimes_{\mathrm{su}}B$ 此时是一个环，同时也是分次代数。除符号外，乘法与通常乘法相同，但必须明确验证结合律。设 $a'\in A_i$、$b\in B_j$、$a''\in A_s$、$b'\in B_r$。读者立即会发现，用两种方式计算

$$
(a\otimes_{\mathrm{su}}b)(a'\otimes_{\mathrm{su}}b')(a''\otimes_{\mathrm{su}}b'')
$$

所得的符号相同，均为 $(-1)^{ij+js+sr}$。由于双线性显然成立，$A\otimes_{\mathrm{su}}B$ 确实是一个代数。

超乘积在许多方面比我们所称的通常乘积更自然。例如，它就是拓扑学中上同调的自然乘积。参见 Greenberg–Harper 的 *Algebraic Topology* 第 29 章。关于按 $\mathbf Z/2\mathbf Z$ 分次的类似构造，见第 XIX 章 §4。

## §7. 模的张量代数

仍设 $R$ 为交换环，$E$ 为一个模，即一个 $R$-模。对每个整数 $r\geqq0$，令

$$
T^r(E)=\bigotimes_{i=1}^r E\qquad\text{且}\qquad T^0(E)=R.
$$

因此 $T^r(E)=E\otimes\cdots\otimes E$，张量积取 $r$ 次。于是 $T^r$ 是一个函子，它在线性映射上的作用如下给出：若 $f:E\to F$ 为线性映射，则

$$
T^r(f)=T(f,\ldots,f),
$$

这里采用 §1 中的含义。

由张量积的结合性，得到一个双线性映射

$$
T^r(E)\times T^s(E)\to T^{r+s}(E),
$$

<span class="original-page-anchor" id="pdf-page-642" aria-hidden="true"></span>

它满足结合律。因此，借助这个双线性映射，可以在直和

$$
T(E)=\bigoplus_{r=0}^{\infty}T^r(E)
$$

上定义环结构，事实上还可定义代数结构，把 $R$ 映到 $T^0(E)=R$。我们称 $T(E)$ 为 $R$ 上的 **$E$ 的张量代数**。一般而言，它不交换。若 $x,y\in T(E)$，仍以 $x\otimes y$ 表示 $T(E)$ 中的环运算。

设 $f:E\to F$ 为线性映射。则对每个 $r\geqq0$，$f$ 诱导线性映射

$$
T^r(f):T^r(E)\to T^r(F),
$$

由此诱导 $T(E)$ 上的映射，记为 $T(f)$。（这不会与 §1 中的映射混淆，后者现在应写成 $T^1(f)$；由于 $T^1(E)=E$，它事实上等于 $f$。）显然，$T(f)$ 是满足以下条件的唯一线性映射：对 $x_1,\ldots,x_r\in E$，有

$$
T(f)(x_1\otimes\cdots\otimes x_r)=f(x_1)\otimes\cdots\otimes f(x_r).
$$

事实上，$T^1(E)=E$ 的元素是 $T(E)$ 在 $R$ 上的代数生成元。因此，$T(f)$ 是代数同态。*于是，可以把 $T$ 看成从模范畴到分次代数范畴的函子，其中 $T(f)$ 是次数为 $0$ 的同态。*

当 $E$ 为 $R$ 上的有限维自由模时，利用命题 2.3 可以完全确定 $T(E)$ 的结构。设 $P$ 为一个 $R$-代数。如果存在元素 $t_1,\ldots,t_n\in P$，使得元素

$$
M_{(i)}(\mathbf t)=t_{i_1}\cdots t_{i_s},
$$

其中 $1\leqq i_\nu\leqq n$，构成 $P$ 在 $R$ 上的一组基，就称 $P$ 为一个**非交换多项式代数**。可以把这些元素称为 $(t)$ 中的非交换单项式。通常约定，当 $r=0$ 时，相应的单项式是 $P$ 的单位元。可见，$t_1,\ldots,t_n$ 生成 $P$ 作为 $R$-代数，而且 $P$ 实际上是一个分次代数，其中 $P_r$ 由单项式 $t_{i_1}\cdots t_{i_r}$ 的 $R$ 系数线性组合构成。自然地，可称 $t_1,\ldots,t_n$ 为 $R$ 上的**独立非交换变量**。

**译校注：** 本段原书两处印作“over $k$”：设 $P$ 为 $k$ 上的代数、由 $t_1,\ldots,t_n$ 生成 $P$ 作为 $k$ 上的代数。但本节设定的基环是 $R$，同段的基与系数均取于 $R$，且未另定义 $k$。译文将这两处统一为 $R$，英文保留原字。

**命题 7.1。** *设 $E$ 为 $R$ 上维数为 $n$ 的自由模。那么 $T(E)$ 同构于 $R$ 上有 $n$ 个变量的非交换多项式代数。换言之，若 $\{v_1,\ldots,v_n\}$ 为 $E$ 在 $R$ 上的一组基，则元素*

$$
M_{(i)}(\mathbf v)=v_{i_1}\otimes\cdots\otimes v_{i_r},
\qquad1\leqq i_\nu\leqq n
$$

*构成 $T^r(E)$ 的一组基，并且 $T(E)$ 的每个元素都能唯一表示为有限和*

$$
\sum_{(i)}a_{(i)}M_{(i)}(\mathbf v),\qquad a_{(i)}\in R,
$$

<span class="original-page-anchor" id="pdf-page-643" aria-hidden="true"></span>

*其中除有限多个外，所有 $a_{(i)}$ 都等于 $0$。*

*证明。* 由命题 2.3 立即得出。

现在从张量代数的角度解释线性映射的张量积。

*为方便起见，本节余下部分把自同态模 $\operatorname{End}_R(E)$ 记为 $L(E)$。*

构造直和

$$
(LT)(E)=\bigoplus_{r=0}^{\infty}L(T^r(E)),
$$

为简便也记作 $LT(E)$。（当然，$LT(E)$ 不等于 $\operatorname{End}_R(T(E))$，所以必须把 $LT$ 看成一个整体符号。）通过在 $LT(E)$ 上定义合适的乘法，我们将看到 $LT$ 是从模到分次代数的函子。

**译校注：** 原书这里写“$LT$ is a functor from modules to graded algebras”。以下构造确实给出每个 $LT(E)$ 的分次代数结构，但未给出任意模同态 $E\to F$ 上的函子作用。自同态模 $\operatorname{End}_R(E)$ 并不能单由任意线性映射自然地诱导同方向的自同态模映射；对于同构，可用共轭来传递自同态。此处保留原书说法，提醒读者它若指整个模范畴，尚需额外说明，译文不擅自补出这种作用。

设 $f\in L(T^r(E))$、$g\in L(T^s(E))$、$h\in L(T^m(E))$。按 §1 的记号，将乘积 $fg\in L(T^{r+s}(E))$ 定义为 $T(f,g)$；换言之，它是唯一的线性映射，对 $x\in T^r(E)$ 和 $y\in T^s(E)$，其作用为

$$
x\otimes y\mapsto f(x)\otimes g(y).
$$

由张量积的结合性，立即得到结合律 $(fg)h=f(gh)$，也可见这个乘法是双线性的。因此 $LT(E)$ 是一个 $R$-代数。

**译校注：** 上一句原书印作“$LT(E)$ is a $k$-algebra”。本节的基环为 $R$，各自同态模与张量积均在 $R$ 上构造，$k$ 未另定义；译文据此将 $k$ 改为 $R$。

有一个代数同态

$$
T(L(E))\to LT(E),
$$

它在每个维数 $r$ 上由线性映射

$$
f_1\otimes\cdots\otimes f_r\mapsto T(f_1,\ldots,f_r)=f_1\cdots f_r
$$

给出。

这里特意说明，左边的张量积取在

$$
L(E)\otimes\cdots\otimes L(E)
$$

中。

还需注意，这个同态一般既不是满射，也不是单射。当 $E$ 是 $R$ 上的有限维自由模时，这个同态既是满射又是单射，因而可清楚地把 $LT(E)$ 看成由 $L(E)$ 生成的非交换多项式代数。具体地，由命题 2.5 可得：

**命题 7.2。** *设 $E$ 为 $R$ 上的有限维自由模。那么有代数同构*

$$
T(L(E))=T(\operatorname{End}_R(E))\to LT(E)
=\bigoplus_{r=0}^{\infty}\operatorname{End}_R(T^r(E)),
$$

<span class="original-page-anchor" id="pdf-page-644" aria-hidden="true"></span>

*它由以下映射给出：*

$$
f\otimes g\mapsto T(f,g).
$$

*证明。* 由命题 2.5，在每个维数上都有线性同构，而且显然这个映射保持乘法。

特别地，可见 $LT(E)$ 是一个非交换多项式代数。

## §8. 对称积

以 $\mathfrak S_n$ 表示 $n$ 个字母上的对称群，例如让它作用在整数 $(1,\ldots,n)$ 上。若一个 $r$ 重多线性映射

$$
f:E^{(r)}\to F
$$

对所有 $\sigma\in\mathfrak S_r$ 都满足 $f(x_1,\ldots,x_r)=f(x_{\sigma(1)},\ldots,x_{\sigma(r)})$，就称它为**对称的**。

在 $T^r(E)$ 中，令 $\mathfrak b_r$ 为由所有形如

$$
x_1\otimes\cdots\otimes x_r-x_{\sigma(1)}\otimes\cdots\otimes x_{\sigma(r)}
$$

的元素生成的子模，其中 $x_i\in E$，$\sigma\in\mathfrak S_r$。定义商模

$$
S^r(E)=T^r(E)/\mathfrak b_r,
$$

并令直和为

$$
S(E)=\bigoplus_{r=0}^\infty S^r(E).
$$

显然，直和

$$
\mathfrak b=\bigoplus_{r=0}^\infty\mathfrak b_r
$$

是 $T(E)$ 中的理想，因此 $S(E)$ 是一个分次 $R$-代数，称为 $E$ 的**对称代数**。

此外，典范映射

$$
E^{(r)}\to S^r(E),
$$

由映射

$$
E^{(r)}\to T^r(E)\to T^r(E)/\mathfrak b_r=S^r(E)
$$

复合而成，对 $r$ 重多线性对称映射具有泛性质。

<span class="original-page-anchor" id="pdf-page-645" aria-hidden="true"></span>

*可见，$S$ 是从模范畴到分次 $R$-代数范畴的函子。* $(x_1,\ldots,x_r)$ 在典范映射

$$
E^{(r)}\to S^r(E)
$$

下的像，简单地记为 $x_1\cdots x_r$。

**命题 8.1。** *设 $E$ 为 $R$ 上维数为 $n$ 的自由模，$\{v_1,\ldots,v_n\}$ 为 $E$ 在 $R$ 上的一组基。把这些基元素看成 $S(E)$ 中的 $S^1(E)$ 的元素时，它们在 $R$ 上代数无关。因此，$S(E)$ 同构于 $R$ 上有 $n$ 个变量的多项式代数。*

*证明。* 设 $t_1,\ldots,t_n$ 为 $R$ 上代数无关的变量，构造多项式代数 $R[t_1,\ldots,t_n]$。令 $P_r$ 为 $r$ 次齐次多项式组成的 $R$-模。如下定义映射 $E^{(r)}\to P_r$。若 $w_1,\ldots,w_r$ 为 $E$ 中可写成

$$
w_i=\sum_{\nu=1}^n a_{i\nu}v_\nu,\qquad i=1,\ldots,r
$$

的元素，则映射定义为

$$
(w_1,\ldots,w_r)\mapsto
(a_{11}t_1+\cdots+a_{1n}t_n)\cdots(a_{r1}t_1+\cdots+a_{rn}t_n).
$$

显然，这个映射是多线性的且对称。因此，它通过一个从 $S^r(E)$ 到 $P_r$ 的线性映射分解：

![对称多线性映射的分解](/library/volume-86/diagrams/pdf-0645-symmetric-triangle.png)

由交换图可见，对每个整数的 $r$ 元组 $(i)=(i_1,\ldots,i_r)$，$S^r(E)$ 中的元素 $v_{i_1}\cdots v_{i_s}$ 映到 $P_r$ 中的 $t_{i_1}\cdots t_{i_s}$。由于 $r$ 次单项式 $M_{(i)}(\mathbf t)$ 在 $R$ 上线性无关，所以 $S^r(E)$ 中的单项式 $M_{(i)}(\mathbf v)$ 也在 $R$ 上线性无关，而映射 $S^r(E)\to P_r$ 为同构。立即可以验证，$S(E)$ 中的乘法对应于 $R[\mathbf t]$ 中多项式的乘法。因此，如上对各分量 $S^r(E)$ 所定义的从 $S(E)$ 到多项式代数的映射，诱导出 $S(E)$ 到 $R[\mathbf t]$ 上的代数同构，正如所需。

**译校注：** 原书在命题中把基写作“a basis of $E$ over $k$”，证明中又写单项式“linearly independent over $k$”。此处未另设 $k$；命题的自由模、整段多项式环和系数均以 $R$ 为基环，因此译文把这两处统一为 $R$，英文保留原字。原文同句在 $r$ 元组的单项式末端使用下标 $i_s$，译文保留其写法，按该 $r$ 元组理解长度。

**命题 8.2。** *设 $E=E'\oplus E''$ 为有限自由模的直和。那么有自然同构*

$$
S^n(E'\oplus E'')\approx\bigoplus_{p+q=n}S^pE'\otimes S^qE''.
$$

*事实上，这只是分次同构*

$$
S(E'\oplus E'')\approx SE'\otimes SE''
$$

*的 $n$ 次分量。*

<span class="original-page-anchor" id="pdf-page-646" aria-hidden="true"></span>

*证明。* 这个同构来自下述映射。$E'$ 和 $E''$ 到它们直和中的包含映射给出函子性映射

$$
SE'\otimes SE''\to SE,
$$

而我们断言它是分次同构。注意，$SE'$ 和 $SE''$ 都是交换环，因此它们的张量积就是 §6 讨论的交换环的张量积。读者可以构造反方向的函子性映射，以证明所需的同构；也可以更具体地指出，$SE'$ 是以一个有限变量族为变量的多项式环，$SE''$ 是以另一个变量族为变量的多项式环，而它们的张量积就是以这两个变量族为变量的多项式环。无论采用哪一种方法都很容易，形式上的证明留给读者。

## 习题

**1.** 设 $k$ 是域，$k(\alpha)$ 是有限扩张。令 $f(X)=\operatorname{Irr}(\alpha,k,X)$，并假设 $f$ 可分。设 $k'$ 是 $k$ 的任意扩张。证明 $k(\alpha)\otimes k'$ 是若干域的直和。如果 $k'$ 代数闭，证明这些域对应于 $k(\alpha)$ 到 $k'$ 中的各个嵌入。

**2.** 设 $k$ 是域，$f(X)$ 是 $k$ 上的不可约多项式，$\alpha$ 是 $f$ 的一个根。证明 $k(\alpha)\otimes k'$ 作为 $k'$-代数同构于 $k'[X]/(f(X))$。

**3.** 设 $E$ 是域 $k$ 的有限扩张。证明，$E$ 在 $k$ 上可分，当且仅当对 $k$ 的每一个扩张 $L$，$E\otimes_k L$ 都没有非零幂零元；也证明仅取 $L=k^a$ 就足以刻画可分性。

**4.** 设 $\varphi:A\to B$ 是交换环同态，$E$ 是 $A$-模，$F$ 是 $B$-模。令 $F_A$ 表示通过 $\varphi$ 所给出的 $A$ 在 $F$ 上的作用，将 $F$ 看成的 $A$-模；也就是说，对 $y\in F_A$ 和 $a\in A$，该作用为

$$
(a,y)\mapsto\varphi(a)y.
$$

证明存在自然同构

$$
\operatorname{Hom}_B(B\otimes_A E,F)\approx\operatorname{Hom}_A(E,F_A).
$$

**5. 范数。** 设 $B$ 是交换环 $R$ 上的交换代数，并假设 $B$ 是秩为 $r$ 的自由模。设 $A$ 是任意交换 $R$-代数。于是 $A\otimes B$ 既是 $A$-代数，也是 $B$-代数。我们将 $A\otimes B$ 看成 $A$-代数；它也是秩为 $r$ 的自由模。如果 $\{e_1,\ldots,e_r\}$ 是 $B$ 在 $R$ 上的一组基，那么

$$
1_A\otimes e_1,\ldots,1_A\otimes e_r
$$

是 $A\otimes B$ 在 $A$ 上的一组基。于是可以定义**范数**

$$
N=N_{A\otimes B,A}:A\otimes B\to A,
$$

它是与正则表示的行列式相一致的唯一映射。

<span class="original-page-anchor" id="pdf-page-647" aria-hidden="true"></span>

换言之，如果 $b\in B$，并且 $b_B$ 表示乘以 $b$ 的映射，那么

$$
N_{B,R}(b)=\det(b_B);
$$

基环扩张之后也类似。证明：

(a) 设 $\varphi:A\to C$ 是 $R$-代数同态。那么下图交换：

$$
\begin{array}{ccc}
A\otimes B&\xrightarrow{\varphi\otimes\operatorname{id}}&C\otimes B\\
{\scriptstyle N}\downarrow&&\downarrow{\scriptstyle N}\\
A&\xrightarrow{\varphi}&C
\end{array}
$$

(b) 设 $x,y\in A\otimes B$。那么 $N(xy)=N(x)N(y)$。［*提示：* 使用交换关系 $e_i e_j=e_j e_i$ 以及结合律。］

> **译校注：** 原书写作 $N(x\otimes_B y)=N(x)\otimes N(y)$。本题的范数定义域是代数 $A\otimes B$，值域是 $A$；若将这里的符号按另一次张量积理解，则 $x\otimes_B y$ 属于 $(A\otimes B)\otimes_B(A\otimes B)$，右端也不再是 $A$ 中的元素。根据正则表示的行列式定义及本题提示，这里表达的是范数对代数乘法的乘法性，故译文将式子明确写为 $N(xy)=N(x)N(y)$。

### 关于平坦性的一些习题

**6.** 设 $M,N$ 平坦。证明 $M\otimes N$ 平坦。

**7.** 设 $F$ 是平坦 $R$-模，$a\in R$ 不是零因子。证明，若某个 $x\in F$ 满足 $ax=0$，则 $x=0$。

**8.** 证明命题 3.2。

### 忠实平坦

**9.** 我们继续假设环都是交换的。设 $M$ 是 $A$-模。如果 $M$ 平坦，且函子

$$
T_M:E\mapsto M\otimes_A E
$$

忠实，即 $E\ne0$ 蕴含 $M\otimes_A E\ne0$，就称 $M$ **忠实平坦**。证明下列条件等价。

(i) $M$ 忠实平坦。

(ii) $M$ 平坦，并且如果 $u:F\to E$ 是 $A$-模同态，$u\ne0$，那么 $T_M(u):M\otimes_A F\to M\otimes_A E$ 也不为零。

(iii) $M$ 平坦，并且对 $A$ 的所有极大理想 $\mathfrak m$，都有 $\mathfrak mM\ne M$。

(iv) $A$-模序列 $N'\to N\to N''$ 正合，当且仅当将其与 $M$ 作张量积所得的序列正合。

**10.** (a) 设 $A\to B$ 是环同态。如果 $M$ 在 $A$ 上忠实平坦，则 $B\otimes_A M$ 在 $B$ 上忠实平坦。

(b) 设 $M$ 在 $B$ 上忠实平坦。如果 $B$ 在 $A$ 上忠实平坦，那么通过同态 $A\to B$ 将 $M$ 看成的 $A$-模在 $A$ 上忠实平坦。

**11.** 设 $P,M,E$ 是交换环 $A$ 上的模。如果 $P$ 有限生成（分别地，有限表现），并且 $E$ 平坦，证明自然同态

$$
\operatorname{Hom}_A(P,M)\otimes_A E\to\operatorname{Hom}_A(P,M\otimes_A E)
$$

是单同态（分别地，同构）。

<span class="original-page-anchor" id="pdf-page-648" aria-hidden="true"></span>

［*提示：* 不妨设 $F_1\to F_0\to P\to0$ 是一个有限表现。考虑下图：

![Hom 与平坦张量积的交换图](/library/volume-86/diagrams/pdf-0648-hom-flatness.png)

### 张量积与直极限

**12.** 证明张量积与直极限交换。换言之，如果 $\{E_i\}$ 是模的一个有向族，$M$ 是任意模，那么存在自然同构

$$
\varinjlim(E_i\otimes_A M)\approx(\varinjlim E_i)\otimes_A M.
$$

**13.** （D. Lazard）设 $E$ 是交换环 $A$ 上的模。所有张量积都在这个环上取。证明下列条件等价：

(i) 存在有限型自由模的一个有向族 $\{F_i\}$，使得

$$
E\approx\varinjlim F_i.
$$

(ii) $E$ 平坦。

(iii) 对每一个有限表现模 $P$，自然同态

$$
\operatorname{Hom}_A(P,A)\otimes_A E\to\operatorname{Hom}_A(P,E)
$$

是满射。

(iv) 对每一个有限表现模 $P$ 以及同态 $f:P\to E$，都存在有限生成自由模 $F$ 以及同态

$$
g:P\to F\qquad\text{和}\qquad h:F\to E,
$$

使得 $f=h\circ g$。

**注。** Lazard 定理的要点在于前两个条件：*$E$ 平坦，当且仅当 $E$ 是有限型自由模的直极限。*

［*提示：* 由于张量积与直极限交换，由上一题和平坦性的定义可得 (i) 蕴含 (ii)。

使用习题 11 证明 (ii) 蕴含 (iii)。

由假设很容易证明 (iii) 蕴含 (iv)。

为证明 (iv) 蕴含 (i)，利用每个模都是有限表现模的直极限这一事实（第三章中的一道习题），再利用 (iv) 将这些模换成自由模。完整的细节可参见例如 Bourbaki，*Algèbre*，第十章 §1，定理 1，第 14 页。］

### 卡西米尔元

**14.** 设 $k$ 是交换域，$E$ 是 $k$ 上维数为有限数 $n$ 的向量空间。设 $B$ 是 $E$ 上的非退化对称双线性形式，它诱导出一个同构<span class="original-page-anchor" id="pdf-page-649" aria-hidden="true"></span>$E\to E^\vee$，将 $E$ 与它的对偶空间同构起来。设 $\{v_1,\ldots,v_n\}$ 是 $E$ 的一组基。$B$-对偶基 $\{v_1',\ldots,v_n'\}$ 由 $E$ 中满足 $B(v_i,v_j')=\delta_{ij}$ 的元素组成。

(a) 证明 $E\otimes E$ 中的元素 $\sum v_i\otimes v_i'$ 与基的选择无关。我们称这个元素为**卡西米尔元**（见下文）。

(b) 在对称代数 $S(E)$ 中，令 $Q_B=\sum v_i v_i'$。证明 $Q_B$ 与基的选择无关。我们称 $Q_B$ 为**卡西米尔多项式**。当然，它依赖于 $B$。

(c) 更一般地，设 $\mathbf D$ 是 $k$ 上的一个（结合）代数，$\mathcal D:E\to\mathbf D$ 是将 $E$ 映入 $\mathbf D$ 的单射线性映射。证明元素 $\sum\mathcal D(v_i)\mathcal D(v_i')=\omega_{B,\mathcal D}$ 与基的选择无关。我们称它为 $\mathbf D$ 中由 $\mathcal D$ 和 $B$ 所确定的**卡西米尔元**。

**注。** 卡西米尔元的术语源于经典情形：$G$ 是李群，$E=\mathfrak g=\operatorname{Lie}(G)$ 是 $G$ 的李代数（即原点处的切空间，其李代数乘法由李导数确定），而 $\mathcal D(v)$ 是与 $v$ 对应的微分算子（沿 $v$ 方向的李导数）。此时卡西米尔元是 $G$ 上全体微分算子组成的代数中的一个偏微分算子。可参见有关流形和李理论的基础书籍，例如 [JoL 01]，第二章 §1 和第七章 §2。

**15.** 设 $E=\mathfrak{sl}_n(k)=$ 由所有迹为 $0$ 的矩阵组成的 $\operatorname{Mat}_n(k)$ 的子空间。设 $B$ 是由 $B(X,Y)=\operatorname{tr}(XY)$ 定义的双线性形式。令 $G=SL_n(k)$。证明：

(a) $B$ 在 $c(G)$ 下不变，其中 $c(g)$ 是由元素 $g\in G$ 给出的共轭作用。

(b) $B$ 在转置映射 $(X,Y)\mapsto({}^tX,{}^tY)$ 下不变。

(c) 设 $k=\mathbf R$。那么 $B$ 在对称矩阵上正定，在反对称矩阵上负定。

(d) 假设给定 $G$ 在习题 14 的代数 $\mathbf D$ 上的作用，并且线性映射 $\mathcal D:E\to\mathbf D$ 是 $G$-线性的。证明卡西米尔元在 $G$ 下不变（这里 $S(E)$ 上取共轭作用，$\mathbf D$ 上取给定的作用）。

> **译校注（条件说明）：** (d) 引用的是习题 14 的卡西米尔元构造，该构造使用 $B$ 的非退化性来定义 $B$-对偶基。对本题的迹形式，当 $\operatorname{char}k$ 不整除 $n$ 时，这一条件成立；若正特征整除 $n$，则非零标量矩阵 $I_n$ 属于 $\mathfrak{sl}_n(k)$，且对所有 $Y\in\mathfrak{sl}_n(k)$ 有 $B(I_n,Y)=\operatorname{tr}Y=0$，所以 $B$ 退化。此时不能直接使用习题 14 的构造。本题原有条件和各项结论均按原文保留；这条说明仅明确引用上一题构造时所需的条件。
