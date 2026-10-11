---
title: "第十一章 实域"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第十章 诺特环与诺特模","link":"/library/volume-86/chapter-010"}
next: {"text":"第十二章 绝对值","link":"/library/volume-86/chapter-012"}
---

# 第十一章 实域

<span class="original-page-anchor" id="pdf-page-461" aria-hidden="true"></span>

## §1. 有序域

设 $K$ 是一个域。$K$ 的一个**定序**是 $K$ 的一个子集 $P$，它具有下述性质：

**ORD 1。** 给定 $x\in K$，则或者 $x\in P$，或者 $x=0$，或者 $-x\in P$，而且这三种可能性互不相容。换言之，$K$ 是 $P$、$\{0\}$ 与 $-P$ 的不交并。

**ORD 2。** 若 $x,y\in P$，则 $x+y$ 和 $xy$ 都属于 $P$。

我们也说 $K$ **由 $P$ 定序**，并称 $P$ 为**正元素集**。

假设 $K$ 由 $P$ 定序。由于 $1\ne0$ 且 $1=1^2=(-1)^2$，可见 $1\in P$。由 **ORD 2** 可得 $1+\cdots+1\in P$，从而 $K$ 的特征为 $0$。若 $x\in P$ 且 $x\ne0$，则 $xx^{-1}=1\in P$ 蕴含 $x^{-1}\in P$。

设 $x,y\in K$。我们定义 $x<y$（或 $y>x$）表示 $y-x\in P$。若 $x<0$，则称 $x$ 为**负的**。这意味着 $-x$ 是正的。通常的不等式关系很容易验证，例如：

$$
\begin{aligned}
x<y\quad\text{且}\quad y<z&\quad\text{蕴含}\quad x<z,\\
x<y\quad\text{且}\quad z>0&\quad\text{蕴含}\quad xz<yz,\\
x<y\quad\text{且}\quad x,y>0&\quad\text{蕴含}\quad \frac1y<\frac1x.
\end{aligned}
$$

我们定义 $x\leqq y$ 表示 $x<y$ 或 $x=y$。于是，$x\leqq y$ 且 $y\leqq x$ 蕴含 $x=y$。

若 $K$ 是有序域，$x\in K$ 且 $x\ne0$，则 $x^2$ 是正的，因为 $x^2=(-x)^2$，并且 $x\in P$ 或 $-x\in P$ 两者之一成立。因此，平方和或者是正的，或者为 $0$。

*设 $E$ 是一个域。则 $E$ 中若干平方和的乘积仍是平方和。若 $a,b\in E$ 是平方和且 $b\ne0$，则 $a/b$ 是平方和。*

<span class="original-page-anchor" id="pdf-page-462" aria-hidden="true"></span>

第一个断言是显然的；由等式 $a/b=ab(b^{-1})^2$，第二个断言也是显然的。

若 $E$ 的特征不为 $2$，且 $-1$ 是 $E$ 中的平方和，则每个元素 $a\in E$ 都是平方和，因为 $4a=(1+a)^2-(1-a)^2$。

若 $K$ 是具有定序 $P$ 的域，$F$ 是一个子域，则显然 $P\cap F$ 定义了 $F$ 的一个定序，称为**诱导定序**。

我们注意到，两个公理 ORD 1 和 ORD 2 也适用于环。若 $A$ 是有序环，且 $1\ne0$，则显然 $A$ 不可能有零因子，而且可以用显然的方式将 $A$ 的定序延拓到分式域：若一个分式可以写成 $a/b$ 的形式，其中 $a,b\in A$ 且 $a,b>0$，就称它为正的。很容易验证，这在分式域上定义了一个定序。

**例。** 我们在实数上的多项式环 $\mathbf R[t]$ 中定义一个定序。对于多项式

$$
f(t)=a_nt^n+\cdots+a_0,
$$

其中 $a_n\ne0$，当 $a_n>0$ 时就定义它为正的。于是两个公理很容易验证。注意，对所有 $a\in\mathbf R$ 都有 $t>a$。因此，相对于 $\mathbf R$ 而言，$t$ 是无穷大的。有序域中存在无穷大（或无穷小）元素，是这种域区别于实数域的子域的主要方面。

现在我们对这种现象，即无穷大元素的存在，作一些说明。

设 $K$ 是有序域，$F$ 是带有诱导定序的子域。像通常一样，若 $x>0$，令 $|x|=x$；若 $x<0$，令 $|x|=-x$。若对所有 $x\in F$ 都有 $|\alpha|\geqq x$，则称 $K$ 中的元素 $\alpha$ **在 $F$ 上是无穷大的**。若对所有 $x\in F$、$x\ne0$ 都有 $0\leqq|\alpha|<|x|$，则称它**在 $F$ 上是无穷小的**。可见，$\alpha$ 是无穷大的，当且仅当 $\alpha^{-1}$ 是无穷小的。若 $K$ 中不存在在 $F$ 上无穷大的元素，则称 $K$ **在 $F$ 上是阿基米德的**。如果中间域 $F_1$，$K\supset F_1\supset F$，在 $F$ 上是阿基米德的，而且不存在包含 $F_1$ 的其他中间域在 $F$ 上仍是阿基米德的，则称 $F_1$ **在 $K$ 中是 $F$ 上的极大阿基米德域**。若 $F_1$ 在 $F$ 上是阿基米德的，而 $F_2$ 在 $F_1$ 上是阿基米德的，则 $F_2$ 在 $F$ 上也是阿基米德的。因此，由佐恩引理，$K$ 中总存在一个在 $F$ 上极大阿基米德的子域 $F_1$。若 $F$ 在 $K$ 中是其自身之上的极大阿基米德域，则称 $F$ **在 $K$ 中是极大阿基米德的**。

设 $K$ 是有序域，$F$ 是子域。令 $\mathfrak o$ 为 $K$ 中所有在 $F$ 上不是无穷大的元素构成的集合。显然，$\mathfrak o$ 是一个环，并且对任意 $\alpha\in K$，有 $\alpha\in\mathfrak o$ 或 $\alpha^{-1}\in\mathfrak o$。因此，$\mathfrak o$ 是所谓的赋值环，它包含 $F$。令 $\mathfrak m$ 为所有在 $F$ 上无穷小的 $\alpha\in K$ 构成的理想。则 $\mathfrak m$ 是 $\mathfrak o$ 唯一的极大理想，因为 $\mathfrak o$ 中任何不属于 $\mathfrak m$ 的元素，其逆元都在 $\mathfrak o$ 中。我们称 $\mathfrak o$ 为**由 $K/F$ 的定序所确定的赋值环**。

<span class="original-page-anchor" id="pdf-page-463" aria-hidden="true"></span>

**命题 1.1。** *设 $K$ 是有序域，$F$ 是子域。设 $\mathfrak o$ 是由 $K/F$ 的定序所确定的赋值环，$\mathfrak m$ 是它的极大理想。则 $\mathfrak o/\mathfrak m$ 是实域。*

*证明。* 否则，我们可以写成

$$
-1=\sum\alpha_i^2+a,
$$

其中 $\alpha_i\in\mathfrak o$，$a\in\mathfrak m$。由于 $\sum\alpha_i^2$ 是正的，$a$ 是无穷小的，这样的关系显然不可能成立。

## §2. 实域

若 $-1$ 不是域 $K$ 中的平方和，则称 $K$ 是**实的**。若域 $K$ 是实的，而且 $K$ 的任何实代数扩张都必须等于 $K$，则称 $K$ 是**实闭的**。换言之，在一个代数闭包内，$K$ 关于实性这一性质是极大的。

**命题 2.1。** *设 $K$ 是实域。*

(i) *若 $a\in K$，则 $K(\sqrt a)$ 与 $K(\sqrt{-a})$ 中至少一个是实域。若 $a$ 是 $K$ 中的平方和，则 $K(\sqrt a)$ 是实域。若 $K(\sqrt a)$ 不是实域，则 $-a$ 是 $K$ 中的平方和。*

(ii) *若 $f$ 是 $K[X]$ 中一个次数为奇数 $n$ 的不可约多项式，$\alpha$ 是 $f$ 的一个根，则 $K(\alpha)$ 是实域。*

*证明。* 设 $a\in K$。若 $a$ 是 $K$ 中的平方，则 $K(\sqrt a)=K$，由假设，它是实域。假设 $a$ 不是 $K$ 中的平方。若 $K(\sqrt a)$ 不是实域，则存在 $b_i,c_i\in K$，使得

$$
\begin{aligned}
-1&=\sum(b_i+c_i\sqrt a)^2\\
&=\sum(b_i^2+2c_ib_i\sqrt a+c_i^2a).
\end{aligned}
$$

因为 $\sqrt a$ 在 $K$ 上的次数为 $2$，所以

$$
-1=\sum b_i^2+a\sum c_i^2.
$$

若 $a$ 是 $K$ 中的平方和，就得到矛盾。无论如何，我们得到

$$
-a=\frac{1+\sum b_i^2}{\sum c_i^2}
$$

是两个平方和的商；由前面的说明，$-a$ 是平方和。因此 $K(\sqrt{-a})$ 是实域，这就证明了第一个断言。

<span class="original-page-anchor" id="pdf-page-464" aria-hidden="true"></span>

对于第二个断言，假设 $K(\alpha)$ 不是实域。于是可写成

$$
-1=\sum g_i(\alpha)^2,
$$

其中 $g_i$ 是 $K[X]$ 中次数不超过 $n-1$ 的多项式。存在 $K[X]$ 中的多项式 $h$，使得

$$
-1=\sum g_i(X)^2+h(X)f(X).
$$

$g_i(X)^2$ 的和具有偶数次数，而且这个次数必须大于 $0$，否则 $-1$ 就是 $K$ 中的平方和。这个次数不超过 $2n-2$。由于 $f$ 的次数 $n$ 是奇数，可知 $h$ 的次数是一个不超过 $n-2$ 的奇数。若 $\beta$ 是 $h$ 的一个根，则可见 $-1$ 是 $K(\beta)$ 中的平方和。因为 $\deg h<\deg f$，通过归纳就完成了证明。

设 $K$ 是实域。所谓一个**实闭包**，是指在 $K$ 上代数的实闭域 $L$。

**定理 2.2。** *设 $K$ 是实域。则 $K$ 存在一个实闭包。若 $R$ 是实闭域，则 $R$ 有唯一的定序。正元素是 $R$ 的平方。每个正元素都是平方，且 $R[X]$ 中每个奇数次多项式在 $R$ 中都有一个根。我们有 $R^a=R(\sqrt{-1})$。*

*证明。* 由佐恩引理，域 $K$ 包含于某个在 $K$ 上代数的实闭域。现在设 $R$ 为实闭域。令 $P$ 为 $R$ 中那些是平方和的非零元素构成的集合。则 $P$ 对加法和乘法封闭。由命题 2.1，$P$ 的每个元素都是 $R$ 中的平方；而给定 $a\in R$、$a\ne0$，必有 $a\in P$ 或 $-a\in P$。所以 $P$ 定义了一个定序。再次由命题 2.1，$R$ 上每个奇数次多项式在 $R$ 中都有根。我们的断言由第六章 §2 的例 5 得出。

**推论 2.3。** *设 $K$ 是实域，$a$ 是 $K$ 中一个不是平方和的元素。则 $K$ 存在一个使 $a$ 为负的定序。*

*证明。* 由命题 1.1，域 $K(\sqrt{-a})$ 是实域，因此作为一个实闭包的子域，它具有一个定序。在这个定序中，$-a>0$，因而 $a$ 为负。

**译校注：** 原书这里引用的是“Proposition 1.1”。使 $K(\sqrt{-a})$ 为实域的结论来自本节命题 2.1(i)，其条件正是 $a$ 不是平方和；上一节的命题 1.1 讨论的是赋值环的剩余域。因此，此处引用应为“命题 2.1”。

**命题 2.4。** *设 $R$ 是满足 $R\ne R^a$ 但 $R^a=R(\sqrt{-1})$ 的域。则 $R$ 是实域，从而是实闭域。*

*证明。* 令 $P$ 为 $R$ 中非零平方元素构成的集合。我们断言，$P$ 是 $R$ 的一个定序。设 $a\in R$、$a\ne0$。假设 $a$ 不是 $R$ 中的平方。令 $\alpha$ 是 $X^2-a=0$ 的一个根。那么 $R(\alpha)=R(\sqrt{-1})$，故存在 $c,d\in R$，使 $\alpha=c+d\sqrt{-1}$。于是

$$
\alpha^2=c^2+2cd\sqrt{-1}-d^2.
$$

<span class="original-page-anchor" id="pdf-page-465" aria-hidden="true"></span>

由于 $1,\sqrt{-1}$ 在 $R$ 上线性无关，可得 $c=0$（因为 $a\notin R^2$），从而 $-a$ 是平方。

现在证明平方和仍是平方。为简便起见，记 $i=\sqrt{-1}$。由于 $R(i)$ 是代数闭域，对给定的 $a,b\in R$，可以找到 $c,d\in R$，使得 $(c+di)^2=a+bi$。于是 $a=c^2-d^2$，$b=2cd$。因此

$$
a^2+b^2=(c^2+d^2)^2,
$$

正如所需。

若 $a\in R$ 且 $a\ne0$，则 $a$ 和 $-a$ 不可能同时是 $R$ 中的平方。因此 $P$ 是一个定序，命题得证。

**定理 2.5。** *设 $R$ 是实闭域，$f(X)$ 是 $R[X]$ 中的多项式。设 $a,b\in R$，并假定 $f(a)<0$、$f(b)>0$。则在 $a$ 与 $b$ 之间存在 $c$，使得 $f(c)=0$。*

*证明。* 由于 $R(\sqrt{-1})$ 是代数闭域，$f$ 分解为次数为 $1$ 或 $2$ 的不可约因子的乘积。若 $X^2+\alpha X+\beta$ 不可约（$\alpha,\beta\in R$），则它是平方和，即

$$
\left(X+\frac\alpha2\right)^2+\left(\beta-\frac{\alpha^2}4\right),
$$

而且因为假定该因子不可约，必有 $4\beta>\alpha^2$。因此，$f$ 的符号变化必定来自某个一次因子的符号变化；很容易验证，相应的根位于 $a$ 与 $b$ 之间。

**引理 2.6。** *设 $K$ 是有序域 $E$ 的子域。设 $\alpha\in E$ 在 $K$ 上代数，并且是多项式*

$$
f(X)=X^n+a_{n-1}X^{n-1}+\cdots+a_0
$$

*的一个根，其中系数在 $K$ 中。则 $|\alpha|\leqq1+|a_{n-1}|+\cdots+|a_0|$。*

*证明。* 若 $|\alpha|\leqq1$，结论显然。若 $|\alpha|>1$，我们用较低次项表达 $|\alpha|^n$，再除以 $|\alpha|^{n-1}$，便证明了引理。

注意，这个引理说明：一个在有序域上代数的元素，相对于该域不可能是无穷大的。

设 $f(X)$ 是系数位于实闭域 $R$ 中的多项式，并假定 $f$ 没有重根。设 $u<v$ 是 $R$ 中的元素。所谓 $f$ 在区间 $[u,v]$ 上的一个**斯图姆序列**，是指满足下述性质的多项式序列

$$
S=\{f=f_0,f'=f_1,\ldots,f_m\}:
$$

<span class="original-page-anchor" id="pdf-page-466" aria-hidden="true"></span>

**ST 1。** 最后一个多项式 $f_m$ 是非零常数。

**ST 2。** 对任何 $0\leqq j\leqq m-1$，都不存在点 $x\in[u,v]$，使得 $f_j(x)=f_{j+1}(x)=0$。

**ST 3。** 若 $x\in[u,v]$ 且对某个 $j=1,\ldots,m-1$ 有 $f_j(x)=0$，则 $f_{j-1}(x)$ 与 $f_{j+1}(x)$ 符号相反。

**ST 4。** 对所有 $j=0,\ldots,m$，有 $f_j(u)\ne0$ 且 $f_j(v)\ne0$。

对于任何不是各多项式 $f_j$ 的根的 $x\in[u,v]$，用 $W_S(x)$ 表示序列

$$
\{f(x),f_1(x),\ldots,f_m(x)\}
$$

中的符号变化次数，并称 $W_S(x)$ 为**序列的变号数**。

**定理 2.7（斯图姆定理）。** *对于任何斯图姆序列 $S$，$f$ 在 $u$ 与 $v$ 之间的根的个数等于 $W_S(u)-W_S(v)$。*

*证明。* 注意，若 $\alpha_1<\alpha_2<\cdots<\alpha_r$ 是多项式 $f_j$ 在 $[u,v]$ 中的根按大小排列所得的序列（$j=0,\ldots,m-1$），则由定理 2.5，$W_S(x)$ 在这些根之间的各个开区间上为常数。因此，只需证明：若恰有一个元素 $\alpha$ 满足 $u<\alpha<v$，且 $\alpha$ 是某个 $f_j$ 的根，则当 $\alpha$ 是 $f$ 的根时，$W_S(u)-W_S(v)=1$；否则该差为 $0$。假设 $\alpha$ 是某个 $f_j$ 的根，其中 $1\leqq j\leqq m-1$。由 **ST 3**，$f_{j-1}(\alpha)$ 与 $f_{j+1}(\alpha)$ 符号相反；将 $\alpha$ 换成 $u$ 或 $v$，这些符号都不变。因此，两个序列

$$
\{f_{j-1}(u),f_j(u),f_{j+1}(u)\}\qquad\text{与}\qquad\{f_{j-1}(v),f_j(v),f_{j+1}(v)\}
$$

的变号数相同，即都等于 $2$。

**译校注：** 原书写作“namely equal to $2$”。这里三个非零数的首末符号相反，中间的符号无论为何，都恰好发生一次符号变化，因此应为“都等于 $1$”。两端的变号数相等这一结论仍然成立。

若 $\alpha$ 不是 $f$ 的根，便得到

$$
W_S(u)=W_S(v).
$$

若 $\alpha$ 是 $f$ 的根，则 $f(u)$ 与 $f(v)$ 符号相反，但 $f'(u)$ 与 $f'(v)$ 符号相同，即都是 $f'(\alpha)$ 的符号。所以此时

$$
W_S(u)=W_S(v)+1.
$$

这就证明了定理。

对于一个没有重根的多项式，很容易构造斯图姆序列。我们使用欧几里得算法，写成

$$
\begin{aligned}
f&=g_1f'-f_2,\\
f_2&=g_2f_1-f_3,\\
&\mathrel{\vdots}\\
f_{m-2}&=g_{m-1}f_{m-1}-f_m,
\end{aligned}
$$

**译校注：** 原书第二行印作 $f_2=g_2f_1-f_3$。欧几里得算法中，第二步应以 $f_1=f'$ 除以 $f_2$，所以正确递推式是 $f_1=g_2f_2-f_3$；原式将 $f_1$ 与 $f_2$ 的位置互换了。

<span class="original-page-anchor" id="pdf-page-467" aria-hidden="true"></span>

其中使用了 $f'=f_1$。由于 $f,f'$ 没有公因子，这个序列的最后一项是非零常数。斯图姆序列的其他性质很容易验证：若序列中两个相继的多项式有公共零点，则所有多项式在该点都必须为 $0$，这与最后一个多项式非零矛盾。

**推论 2.8。** *设 $K$ 是有序域，$f$ 是 $K$ 上一个次数至少为 $1$ 的不可约多项式。则在 $K$ 的任意两个在 $K$ 上诱导给定定序的实闭包中，$f$ 的根的个数相同。*

*证明。* 利用引理 2.6，可以在 $K$ 中取足够大的正元素 $v$ 与负得足够大的元素 $u$，使得 $f$ 的所有根以及斯图姆序列中各多项式的所有根都位于 $u$ 和 $v$ 之间。于是，$W_S(u)-W_S(v)$ 就是在 $K$ 的任何诱导给定定序的实闭包中，$f$ 的根的总数。

**定理 2.9。** *设 $K$ 是有序域，$R,R'$ 是 $K$ 的实闭包，它们的定序在 $K$ 上都诱导给定定序。则存在唯一的 $K$ 上同构 $\sigma:R\to R'$，而且这个同构保持序。*

*证明。* 首先证明，对给定的 $R/K$ 的有限子扩张 $E$，存在 $E$ 到 $R'$ 中的 $K$ 上嵌入。令 $E=K(\alpha)$，并令

$$
f(X)=\operatorname{Irr}(\alpha,K,X).
$$

于是 $f(\alpha)=0$，斯图姆定理的推论（推论 2.8）说明 $f$ 在 $R'$ 中有一个根 $\beta$。因此，存在 $K(\alpha)$ 到 $K(\beta)$ 上的 $K$ 上同构，它将 $\alpha$ 映到 $\beta$。

设 $\alpha_1,\ldots,\alpha_n$ 是 $f$ 在 $R$ 中的互异根，$\beta_1,\ldots,\beta_m$ 是 $f$ 在 $R'$ 中的互异根。设

$$
\begin{aligned}
\alpha_1<\cdots<\alpha_n&\quad\text{按 }R\text{ 的定序},\\
\beta_1<\cdots<\beta_m&\quad\text{按 }R'\text{ 的定序}.
\end{aligned}
$$

我们断言，$m=n$，而且可以选择 $K(\alpha_1,\ldots,\alpha_n)$ 到 $R'$ 中的嵌入 $\sigma$，使得对 $i=1,\ldots,n$ 都有 $\sigma\alpha_i=\beta_i$。事实上，取 $R$ 中的元素 $\gamma_i$，使得

$$
\gamma_i^2=\alpha_{i+1}-\alpha_i\quad\text{其中}\quad i=1,\ldots,n-1,
$$

并令 $E_1=K(\alpha_1,\ldots,\alpha_n,\gamma_1,\ldots,\gamma_{n-1})$。根据前面的论述，存在 $E_1$ 到 $R'$ 中的嵌入 $\sigma$，于是 $\sigma\alpha_{i+1}-\sigma\alpha_i$ 是 $R'$ 中的平方。因此

$$
\sigma\alpha_1<\cdots<\sigma\alpha_n.
$$

这证明了 $m\geqq n$。由对称性，得到 $m=n$。此外，对 $i=1,\ldots,n$ 的条件 $\sigma\alpha_i=\beta_i$ 决定了 $\sigma$ 在下述域上的作用：

<span class="original-page-anchor" id="pdf-page-468" aria-hidden="true"></span>

$K(\alpha_1,\ldots,\alpha_n)$。我们断言，$\sigma$ 保持序。设 $y\in K(\alpha_1,\ldots,\alpha_n)$ 且 $0<y$。取 $\gamma\in R$，使得 $\gamma^2=y$。存在

$$
K(\alpha_1,\ldots,\alpha_n,\gamma_1,\ldots,\gamma_{n-1},\gamma)
$$

到 $R'$ 中的 $K$ 上嵌入，它在 $K(\alpha_1,\ldots,\alpha_n)$ 上必定诱导 $\sigma$，并且使 $\sigma y$ 为平方，从而 $\sigma y>0$，正如所断言的。

现在利用佐恩引理，显然可以得到 $R$ 到 $R'$ 上的 $K$ 上同构。这个同构将平方映到平方，因而保持序，这就证明了定理。

**命题 2.10。** *设 $K$ 为有序域，$K'$ 为一个扩张，且不存在关系*

$$
-1=\sum_{i=1}^n a_i\alpha_i^2,
$$

*其中 $a_i\in K$、$a_i>0$，$\alpha_i\in K'$。设 $L$ 是从 $K'$ 添加 $K$ 中所有正元素的平方根所得的域。则 $L$ 是实域。*

*证明。* 否则，存在形如

$$
-1=\sum_{i=1}^n a_i\alpha_i^2
$$

的关系，其中 $a_i\in K$、$a_i>0$，$\alpha_i\in L$。（可以取 $a_i=1$。）令 $r$ 为最小整数，使得可以写出这样的关系，且各 $\alpha_i$ 都位于 $L$ 的一个形如

$$
K'(\sqrt{b_1},\ldots,\sqrt{b_r})
$$

的子域中，其中 $b_j\in K$、$b_j>0$。写成

$$
\alpha_i=x_i+y_i\sqrt{b_r},
$$

其中 $x_i,y_i\in K'(\sqrt{b_1},\ldots,\sqrt{b_{r-1}})$。于是

$$
\begin{aligned}
-1&=\sum a_i(x_i+y_i\sqrt{b_r})^2\\
&=\sum a_i(x_i^2+2x_iy_i\sqrt{b_r}+y_i^2b_r).
\end{aligned}
$$

根据假设，$\sqrt{b_r}$ 不在 $K'(b_1,\ldots,\sqrt{b_{r-1}})$ 中。

**译校注：** 原书这里将域印作 $K'(b_1,\ldots,\sqrt{b_{r-1}})$，首个生成元漏了根号。要按照上文的 $x_i,y_i$ 所属域比较系数，此处应为 $K'(\sqrt{b_1},\ldots,\sqrt{b_{r-1}})$；$\sqrt{b_r}$ 不属于这个域由 $r$ 的最小性保证，否则可用少一个平方根写出同一关系。

因此

$$
-1=\sum a_ix_i^2+\sum a_ib_ry_i^2,
$$

这与 $r$ 的最小性矛盾。

**定理 2.11。** *设 $K$ 是有序域。则存在 $K$ 的一个实闭包 $R$，它在 $K$ 上诱导给定定序。*

<span class="original-page-anchor" id="pdf-page-469" aria-hidden="true"></span>

*证明。* 在命题 2.10 中取 $K'=K$。则 $L$ 是实域，并包含于一个实闭包中。断言显然成立。

**推论 2.12。** *设 $K$ 是有序域，$K'$ 是一个扩张域。$K'$ 存在一个在 $K$ 上诱导给定定序的定序，其充分必要条件是不存在形如*

$$
-1=\sum_{i=1}^n a_i\alpha_i^2
$$

*的关系，其中 $a_i\in K$、$a_i>0$，$\alpha_i\in K'$。*

*证明。* 若不存在这种关系，则命题 2.10 说明 $L$ 包含于一个实闭包中，其定序在 $K'$ 上诱导一个定序，并且在 $K$ 上诱导给定的定序，正如所需。逆命题显然。

**例。** 设 $\mathbf Q^a$ 是代数数域。立即可见，$\mathbf Q$ 只允许一个定序，即通常的定序。因此，$\mathbf Q^a$ 中 $\mathbf Q$ 的任意两个实闭包都通过唯一的同构彼此同构。$\mathbf Q^a$ 中 $\mathbf Q$ 的实闭包，恰好是 $\mathbf Q^a$ 中那些使 $\mathbf Q^a$ 在其上为有限次扩张的子域。设 $K$ 是 $\mathbf Q$ 的一个有限实扩张，并包含于 $\mathbf Q^a$。$K$ 的一个元素 $\alpha$ 是 $K$ 中的平方和，当且仅当 $\alpha$ 在实数中的每个共轭都为正；等价地，当且仅当 $\alpha$ 在 $\mathbf Q^a$ 中 $\mathbf Q$ 的某个实闭包内的每个共轭都为正。

**译校注：** 原书对任意“An element $\alpha$”使用“is positive”。依本章的严格正元素定义，$\alpha=0$ 时它是平方和，但其共轭不是正元素。故该句应加上 $\alpha\ne0$，或将“positive”改为“非负”；对非零 $\alpha$，所述判别保持原样。

**注。** 本节及上一节中发展的理论归功于 Artin-Schreier。参见本章末尾的参考文献。

## §3. 实零点与同态

正如我们已经建立了将同态延拓到代数闭域中的理论，以及关于代数闭域中零点的希尔伯特零点定理，我们希望为取值于实闭域的情形建立相应理论。一个主要定理如下：

**定理 3.1。** *设 $k$ 是域，$K=k(x_1,\ldots,x_n)$ 是有限生成扩张。假设 $K$ 有序。设 $R_k$ 是 $k$ 的一个实闭包，它在 $k$ 上诱导的定序与 $K$ 相同。则存在 $k$ 上的同态*

$$
\varphi:k[x_1,\ldots,x_n]\to R_k.
$$

<span class="original-page-anchor" id="pdf-page-470" aria-hidden="true"></span>

作为定理 3.1 的应用，可以得到：

**推论 3.2。** *沿用定理中的记号，设 $y_1,\ldots,y_m\in k[x]$，并假定在 $K$ 的给定定序中有*

$$
y_1<y_2<\cdots<y_m.
$$

*则可以选择 $\varphi$，使得*

$$
\varphi y_1<\cdots<\varphi y_m.
$$

*证明。* 取 $\gamma_i\in K^a$，使 $\gamma_i^2=y_{i+1}-y_i$。那么 $K(\gamma_1,\ldots,\gamma_{n-1})$ 有一个在 $K$ 上诱导给定定序的定序。

**译校注：** 原书此处印作 $K(\gamma_1,\ldots,\gamma_{n-1})$。被比较的是 $m$ 个元素 $y_1,\ldots,y_m$，相邻差共有 $m-1$ 个，且下式中的平方根及其逆元也均取到 $m-1$，所以这里的最后指标应为 $m-1$，即 $K(\gamma_1,\ldots,\gamma_{m-1})$。

我们将定理应用于环

$$
k[x_1,\ldots,x_n,\gamma_1^{-1},\ldots,\gamma_{m-1}^{-1},\gamma_1,\ldots,\gamma_{m-1}].
$$

**推论 3.3（Artin）。** *设 $k$ 是只有一个定序的实域。设 $f(X_1,\ldots,X_n)\in k(X)$ 是有理函数，并满足如下性质：对所有使 $f(a)$ 有定义的 $(a)=(a_1,\ldots,a_n)\in R_k^{(n)}$，都有 $f(a)\geqq0$。则 $f(X)$ 是 $k(X)$ 中的平方和。*

*证明。* 假设结论不成立。由推论 2.3，$k(X)$ 存在一个使 $f$ 为负的定序。将推论 3.2 应用于环

$$
k[X_1,\ldots,X_n,h(X)^{-1}],
$$

其中 $h(X)$ 是 $f(X)$ 的一个多项式分母。可以找到这个环到 $R_k$ 中的同态 $\varphi$（它在 $k$ 上诱导恒等映射），使得 $\varphi(f)<0$。但

$$
\varphi(f)=f(\varphi X_1,\ldots,\varphi X_n),
$$

矛盾。令 $a_i=\varphi(X_i)$，即完成证明。

推论 3.3 曾是一个希尔伯特问题。我们将介绍的定理 3.1 的证明，在几个技术方面不同于 Artin 对这个推论的证明。

我们先看如何将定理 3.1 归约到 $K$ 在 $k$ 上的超越次数为 $1$、且 $k$ 实闭的情形。

**引理 3.4。** *设 $R$ 为实闭域，$R_0$ 为一个在 $R$ 中代数闭的子域（即 $R$ 中每个不在 $R_0$ 中的元素都在 $R_0$ 上超越）。则 $R_0$ 是实闭域。*

*证明。* 设 $f(X)$ 是 $R_0$ 上的不可约多项式。它在 $R$ 中分解为一次与二次因子。这些因子在 $R$ 中的系数在 $R_0$ 上代数，因此必定在 $R_0$ 中。所以 $f(X)$ 本身或者是一次多项式，或者是一个在 $R_0$ 上就已经不可约的二次多项式。由介值定理，可以假定 $f$ 是正<span class="original-page-anchor" id="pdf-page-471" aria-hidden="true"></span>定的，即对所有 $a\in R_0$ 都有 $f(a)>0$。不失一般性，可以假定对某个 $b\in R_0$，有 $f(X)=X^2+b^2$。这个多项式的任何一个根都将同时带来 $\sqrt{-1}$，因此 $R_0$ 唯一的代数扩张是 $R_0(\sqrt{-1})$。这证明了 $R_0$ 是实闭域。

设 $R_K$ 是 $K$ 的一个实闭包，在 $K$ 上诱导给定定序。令 $R_0$ 为 $k$ 在 $R_K$ 中的代数闭包。由引理，$R_0$ 是实闭域。

考虑域 $R_0(x_1,\ldots,x_n)$。若可以对环 $R_0[x_1,\ldots,x_n]$ 证明定理，并找到同态

$$
\psi:R_0[x_1,\ldots,x_n]\to R_0,
$$

则令 $\sigma:R_0\to R_K$ 为 $k$ 上的同构（它由定理 2.9 存在），并令 $\varphi=\sigma\circ\psi$，就解决了 $k$ 上的问题。

**译校注：** 原书同构的目标印作 $R_K$，应为定理 3.1 中的 $R_k$。$R_0$ 是 $k$ 的实闭包，定理 2.9 给出的同构是两个 $k$ 的实闭包之间的同构；$R_K$ 则是 $K$ 的实闭包，一般在 $k$ 上还包含超越元素。改为 $\sigma:R_0\to R_k$ 后，复合 $\varphi$ 的目标正是定理所需的 $R_k$。

这样就把定理归约到 $k$ 实闭的情形。

其次，设 $F$ 是一个中间域，$K\supset F\supset k$，使得 $K$ 在 $F$ 上的超越次数为 $1$。再取一个保持定序的 $K$ 的实闭包 $R_K$，并令 $R_F$ 为包含于 $R_K$ 中的 $F$ 的实闭包。若对于维数为 $1$ 的扩张已经知道定理成立，则可以找到同态

$$
\psi:R_F[x_1,\ldots,x_n]\to R_F.
$$

注意，域 $k(\psi x_1,\ldots,\psi x_n)$ 的超越次数不超过 $n-1$；它又是实域，因为它包含于 $R_F$。因此，通过归纳就把问题归约到 $K$ 的维数为 $1$，而且如上所见，$k$ 实闭的情形。

我们可以把这一陈述作如下几何解释。可以写 $K=R(x,y)$，其中 $x$ 在 $R$ 上超越，$(x,y)$ 满足 $R[X,Y]$ 中某个不可约多项式方程 $f(X,Y)=0$。我们本质上想证明的是：曲线 $f(X,Y)=0$ 上有无穷多个坐标在 $R$ 中的点，即有无穷多个实点。

主要思想是找到某个点 $(a,b)\in R^{(2)}$，使得 $f(a,b)=0$，但 $D_2f(a,b)\ne0$。然后就能使用介值定理。可见，当 $h$ 从一个小的正元素变为一个小的负元素时，$f(a,b+h)$ 改变符号。若取接近 $a$ 的 $a'\in R$，则对于小的 $h$，$f(a',b+h)$ 也改变符号；因此，对所有充分接近 $a$ 的 $a'$，$f(a',Y)$ 都在 $R$ 中有一个零点。这样就得到了无穷多个零点。

为了找到所需的点，把多项式 $f(x,Y)$ 看成系数在 $R(x)$ 中、变量为 $Y$ 的一元多项式。不失一般性，可以假定它的首项系数为 $1$。为这个多项式构造一个斯图姆序列，记作

$$
\{f(x,Y),f_1(x,Y),\ldots,f_m(x,Y)\}.
$$

令 $d=\deg f$。若用 $A(x)=(a_{d-1}(x),\ldots,a_0(x))$ 表示 $f(x,Y)$ 的系数，则由欧几里得算法可见，斯图姆序列中各多项式的<span class="original-page-anchor" id="pdf-page-472" aria-hidden="true"></span>系数都可以用关于 $a_{d-1}(x),\ldots,a_0(x)$ 的有理函数

$$
\{G_\nu(A(x))\}
$$

来表达。

令

$$
v(x)=1\pm a_{d-1}(x)\pm\cdots\pm a_0(x)+s,
$$

其中 $s$ 为正整数，选择正负号，使得这个和中的每一项都给出正的贡献。令 $u(x)=-v(x)$，并选取 $s$，使得 $u$ 和 $v$ 都不是 $f$ 的斯图姆序列中任何一个多项式的根。现在需要一个引理。

**引理 3.5。** *设 $R$ 为实闭域，$\{h_i(x)\}$ 为一组有限多个系数在 $R$ 中的单变量有理函数。假设有理函数域 $R(x)$ 以某种方式定序，从而每个 $h_i(x)$ 都具有一个确定的符号。则存在无穷多个 $x$ 在 $R$ 中的特殊值 $c$，使得对所有 $i$，$h_i(c)$ 都有定义，且与 $h_i(x)$ 符号相同。*

*证明。* 考虑有理函数的分子和分母，可以不失一般性地假定各 $h_i$ 都是多项式。于是写成

$$
h_i(x)=\alpha\prod(x-\lambda)\prod p(x),
$$

其中第一个乘积取遍 $h_i$ 在 $R$ 中的所有根 $\lambda$，第二个乘积取遍 $R$ 上的正定二次因子。对任何 $\xi\in R$，$p(\xi)$ 都为正。因此，只需证明：用无穷多个值 $\alpha$ 代替 $x$ 时，可以对所有 $\lambda$ 保持 $(x-\lambda)$ 的符号。将所有 $\lambda$ 的值与 $x$ 按大小排列，得到

$$
\cdots<\lambda_1<x<\lambda_2<\cdots,
$$

其中，若 $x$ 大于或小于所有 $\lambda$，则可能省去 $\lambda_1$ 或 $\lambda_2$。在 $R$ 中选择任何位于 $\lambda_1$ 与 $\lambda_2$ 之间的 $x$ 的值 $\alpha$，都满足引理的要求。

为了把引理应用于所需点的存在性，令有理函数族 $\{h_i(x)\}$ 包括所有系数 $a_{d-1}(x),\ldots,a_0(x)$、所有有理函数 $G_\nu(A(x))$，以及所有用其变号数满足斯图姆定理的值 $f_j(x,u(x))$、$f_j(x,v(x))$。于是可以找到无穷多个 $x$ 在 $R$ 中的特殊值 $\alpha$，保持这些有理函数的符号。这样，多项式 $f(\alpha,Y)$ 在 $R$ 中有根；并且除有限多个 $\alpha$ 外，这些根的重数都是 $1$。

随后，运用简单的技巧即可看出：除曲线上有限多个点以外，元素 $x_1,\ldots,x_n$ 都属于同态 $R[x,y]\to R$ 的局部环；该同态将 $(x,y)$ 映到 $(a,b)$，其中 $f(a,b)=0$，但<span class="original-page-anchor" id="pdf-page-473" aria-hidden="true"></span>$D_2f(a,b)\ne0$。（例如可参见第十二章 §4 末尾的例子，以及该章习题 18。）这里也可以给出直接证明。这样便得到同态

$$
R[x_1,\ldots,x_n]\to R,
$$

从而证明了定理 3.1。

**定理 3.6。** *设 $k$ 是实域，$K=k(x_1,\ldots,x_n,y)=k(x,y)$ 是有限生成扩张，其中 $x_1,\ldots,x_n$ 在 $k$ 上代数无关，而 $y$ 在 $k(x)$ 上代数。设 $f(X,Y)$ 是 $k[X,Y]$ 中满足 $f(x,y)=0$ 的不可约多项式。设 $R$ 是包含 $k$ 的实闭域，并假设存在 $(a,b)\in R^{(n+1)}$，使得 $f(a,b)=0$，但*

$$
D_{n+1}f(a,b)\ne0.
$$

*则 $K$ 是实域。*

*证明。* 设 $t_1,\ldots,t_n$ 在 $R$ 上代数无关。通过归纳，可以在 $R(t_1,\ldots,t_n)$ 上给出一个定序，使得每个 $t_i$ 相对于 $R$ 都是无穷小的（参见 §1 中的例子）。令 $R'$ 为保持这个定序的 $R(t_1,\ldots,t_n)$ 的一个实闭包。对每个 $i=1,\ldots,n$，令 $u_i=a_i+t_i$。那么，当 $h$ 取 $R$ 中足够小的正、负元素时，$f(u,b+h)$ 改变符号；因此 $f(u,Y)$ 在 $R'$ 中有一个根，记为 $v$。由于 $f$ 不可约，将 $x_i$ 映到 $u_i$ 的 $k(x)$ 到 $k(u)$ 上的同构，可延拓为 $k(x,y)$ 到 $R'$ 中的嵌入，从而 $K$ 是实域，正如所需。

用代数几何的语言来说，定理 3.1 和 3.6 表明：实域 $k$ 上的一个簇的函数域是实域，当且仅当这个簇在 $k$ 的某个实闭包中有一个非奇异点。

## 习题

**1.** 设 $\alpha$ 在 $\mathbf Q$ 上代数，并假设 $\mathbf Q(\alpha)$ 是实域。证明 $\alpha$ 是 $\mathbf Q(\alpha)$ 中的平方和，当且仅当对于 $\mathbf Q(\alpha)$ 到 $\mathbf R$ 中的每个嵌入 $\sigma$，都有 $\sigma\alpha>0$。

**译校注：** 原题未假设 $\alpha\ne0$，但结论印为 $\sigma\alpha>0$。当 $\alpha=0$ 时，$0$ 是平方和，而严格不等式不成立。因此应补充 $\alpha\ne0$，或将原式改为 $\sigma\alpha\geqq0$；这与前文实共轭的平方和判别相同。

**2.** 设 $F$ 是 $\mathbf Q$ 的有限扩张。设 $\varphi:F\to\mathbf Q$ 是一个 $\mathbf Q$ 线性泛函，且对所有 $x\in F$、$x\ne0$ 都有 $\varphi(x^2)>0$。设 $\alpha\in F$、$\alpha\ne0$。若对所有 $x\in F$ 都有 $\varphi(\alpha x^2)\geqq0$，证明 $\alpha$ 是 $F$ 中的平方和，并且 $F$ 是全实的，即 $F$ 到复数域中的每个嵌入的像都包含于实数域。［*提示：* 利用迹给出 $F$ 与它在 $\mathbf Q$ 上的对偶空间之间的对应这一事实，并使用第十二章 §1 的逼近定理。］

<span class="original-page-anchor" id="pdf-page-474" aria-hidden="true"></span>

**3.** 设 $\alpha\leqq t\leqq\beta$ 是实区间，$f(t)$ 是在这个区间上为正的实多项式。证明 $f(t)$ 可以写成

$$
c\left(\sum Q_\nu^2+\sum(t-\alpha)Q_\mu^2+\sum(\beta-t)Q_\lambda^2\right)
$$

的形式，其中 $Q^2$ 表示平方，$c\geqq0$。*提示：* 将多项式分解，并使用恒等式

$$
(t-\alpha)(\beta-t)=\frac{(t-\alpha)^2(\beta-t)+(t-\alpha)(\beta-t)^2}{\beta-\alpha}.
$$

**说明。** 上述看似平常的结果，是建立希尔伯特空间上有界厄米算子的谱定理时的一个关键步骤。参见 [La 72] 的附录及 [La 85]。

**4.** 证明实数域只有恒等自同构。［*提示：* 证明自同构保持定序。］

### 实位

以下习题可参见 Krull [Kr 32] 和 Lang [La 53]。这些习题组成一组相互联系的题目，它们的解答可以在 [La 53] 中找到。

**5.** 设 $K$ 是域，并假设 $K$ 存在一个实位；也就是说，存在一个取值于实域 $L$ 的位 $\varphi$。证明 $K$ 是实域。

**6.** 设 $K$ 是有序实域，$F$ 是一个在 $K$ 中极大阿基米德的子域。证明 $K$ 关于 $F$ 的典范位在 $F$ 上代数（即若 $\mathfrak o$ 是 $K$ 中那些在 $F$ 上不是无穷大的元素构成的赋值环，$\mathfrak m$ 是它的极大理想，则 $\mathfrak o/\mathfrak m$ 在 $F$ 上代数）。

**7.** 设 $K$ 是有序域，$F$ 是一个在 $K$ 中极大阿基米德的子域。令 $K'$ 为 $K$ 的实闭包（保持定序），并令 $F'$ 为包含于 $K'$ 中的 $F$ 的实闭包。令 $\varphi$ 为 $K'$ 关于 $F'$ 的典范位。证明 $\varphi(K')$ 取值于 $F'$，且 $\varphi$ 在 $K$ 上的限制等价于 $K$ 在 $F$ 上的典范位。

**8.** 若对于所有 $a\in K$，$\sqrt a$ 或 $\sqrt{-a}$ 两者之一在 $K$ 中，则定义实域 $K$ 为**二次闭的**。二次闭实域 $K$ 的定序由此唯一确定；这种域的实闭包在 $K$ 上同构的意义下也唯一确定。

假设 $K$ 二次闭。设 $F$ 是 $K$ 的子域，且 $F$ 在 $K$ 中极大阿基米德。令 $\varphi$ 为 $K$ 在 $F$ 上的一个位，它取值于一个在 $F$ 上代数的域。证明 $\varphi$ 等价于 $K$ 在 $F$ 上的典范位。

**9.** 设 $K$ 是二次闭实域。令 $\varphi$ 为 $K$ 的一个实位，它取值于实闭域 $R$。令 $F$ 为 $K$ 的一个极大子域，使得 $\varphi$ 在 $F$ 上是同构，并将 $F$ 与 $\varphi(F)$ 等同。证明这样的 $F$ 存在，且在 $K$ 中极大阿基米德。证明 $\varphi$ 的像在 $F$ 上代数，且 $\varphi$ 由 $K$ 在 $F$ 上的典范位诱导。

**10.** 设 $K$ 是实域，$\varphi$ 是 $K$ 的一个实位，它取值于实闭域 $R$。证明 $\varphi$ 可以延拓为 $K$ 的一个实闭包的取值于 $R$ 的位。［*提示：* 首先将 $\varphi$ 延拓到 $K$ 的一个二次闭包，再使用习题 5。］

<span class="original-page-anchor" id="pdf-page-475" aria-hidden="true"></span>

**11.** 设 $K\subset K_1\subset K_2$ 是实闭域。假设 $K$ 在 $K_1$ 中极大阿基米德，且 $K_1$ 在 $K_2$ 中极大阿基米德。证明 $K$ 在 $K_2$ 中极大阿基米德。

**12.** 设 $K$ 是实闭域。证明存在一个包含 $K$ 的实闭域 $R$，它在 $K$ 上具有任意大的超越次数，并且 $K$ 在 $R$ 中极大阿基米德。

**13.** 设 $R$ 是实闭域。设 $f_1,\ldots,f_r$ 是 $R$ 上 $n$ 个变量的奇数次齐次多项式。若 $n>r$，证明这些多项式在 $R$ 中有一个非平凡公共零点。（*说明：* 若这些型是泛的（按第九章的意义），且 $n=r+1$，则由贝祖定理，在代数闭包 $R^a$ 中，这些型恰有 $d_1\cdots d_m$ 个公共零点，其中 $d_i$ 为 $f_i$ 的次数。可以假设这一点来证明题目所述的结果。若希望看到详细推导，参见 [La 53] 的定理 15。与第九章习题 3 比较。）

**译校注：** 原书将次数的乘积印作 $d_1\cdots d_m$，但这里共有 $r$ 个型 $f_1,\ldots,f_r$，没有定义 $m$。贝祖计数中的次数乘积应为 $d_1\cdots d_r$。

## 参考文献

[Ar 24] E. ARTIN，Kennzeichnung des Körpers der reellen algebraischen Zahlen（实代数数域的刻画），*Abh. Math. Sem. Hansischen Univ.* **3**（1924），第 319–323 页。

[Ar 27] E. ARTIN，Über die Zerlegung definiter Funktionen in Quadrate（论定号函数分解为平方），*Abh. Math. Sem. Hansischen Univ.* **5**（1927），第 100–115 页。

[ArS 27] E. ARTIN 与 E. SCHREIER，Algebraische Konstruktion reeller Körper（实域的代数构造），*Abh. Math. Sem. Hansischen Univ.* **5**（1927），第 85–99 页。

[Kr 32] W. KRULL，Allgemeine Bewertungstheorie（一般赋值理论），*J. reine angew. Math.*（1932），第 169–196 页。

[La 53] S. LANG，The theory of real places（实位理论），*Ann. Math.* **57** 第 2 期（1953），第 378–391 页。

[La 72] S. LANG，*Differential manifolds*（《微分流形》），Addison-Wesley，1972 年；Springer Verlag 于 1985 年重印；后由 [La 99a] 取代。

[La 85] S. LANG，*Real and functional analysis*（《实分析与泛函分析》），第三版，Springer Verlag，1993 年。

[La 99a] S. LANG，*Fundamentals of Differential Geometry*（《微分几何基础》），Springer Verlag，1999 年。
