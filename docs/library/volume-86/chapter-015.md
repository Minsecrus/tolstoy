---
title: "第十五章 双线性型的结构"
description: "Serge Lang《Algebra》中文译文。"
pageClass: algebra-reading
prev: {"text":"第十四章 单个自同态的表示","link":"/library/volume-86/chapter-014"}
next: {"text":"第十六章 张量积","link":"/library/volume-86/chapter-016"}
---

# 第十五章 双线性型的结构

<span class="original-page-anchor" id="pdf-page-580" aria-hidden="true"></span>

双线性型主要有三种类型：厄米型（或对称型）、酉型和交错型（斜对称型）。本章给出结构定理，在适当的基下为这些型给出规范化的表达式。本章也沿用通常的模式，尽可能把一个对象分解成简单对象的直和。

## §1. 预备知识，正交和

本章的目的是进一步研究这三类型的结构理论。为此，我们在大部分时候都假设基环是域，并且在对称型的情形中，假设该域的特征 $\ne2$。

回顾这三个定义。设 $E$ 是交换环 $R$ 上的模。设 $g:E\times E\to R$ 是映射。若 $g$ 是双线性的，并且对所有 $x,y\in E$ 都有 $g(x,y)=g(y,x)$，则称 $g$ 为**对称**型。若 $g(x,x)=0$，因而对所有 $x,y\in E$ 都有 $g(x,y)=-g(y,x)$，则称 $g$ 为**交错**型。若 $R$ 有一个阶为 $2$ 的自同构，记作 $a\mapsto\bar a$，而 $g$ 对第一个变量线性、对第二个变量反线性，并且

$$
g(x,y)=\overline{g(y,x)},
$$

则称 $g$ 为**厄米**型。

在所指的 $g$ 明确时，我们写 $g(x,y)=\langle x,y\rangle$。有时也写作 $g(x,y)=x\cdot y$ 或 $g(x,x)=x^2$。我们有时称 $g$ 为**标量积**。

<span class="original-page-anchor" id="pdf-page-581" aria-hidden="true"></span>

若 $v_1,\ldots,v_m\in E$，我们用 $(v_1,\ldots,v_m)$ 表示由 $v_1,\ldots,v_m$ 生成的 $E$ 的子模。

设 $g$ 为对称型、交错型或厄米型。显然，$g$ 的左核等于其右核，我们把它简称为 $g$ 的核。在上述任一情形中，若 $g$ 的核为 $0$，则称 $g$ **非退化**。假设 $E$ 是域 $k$ 上的有限维空间。该型非退化当且仅当它非奇异，即诱导出 $E$ 与其对偶空间之间的同构（对于厄米型，使用反对偶空间）。

除了前一章关于反线性的几条评述外，我们不用该章关于对偶性的结论。我们只需要第三章给出的域上的对偶性。此外，除了第10节关于普法夫式的评述外，我们基本上不会再涉及矩阵。

再引入一个记号。在研究向量空间上的型时，我们经常把向量空间分解成正交子空间的直和。若 $E$ 是带有上述型 $g$ 的向量空间，$F,F'$ 是子空间，我们写

$$
E=F\perp F',
$$

表示 $E$ 是 $F$ 与 $F'$ 的直和，并且 $F$ 与 $F'$ 正交（或垂直）；换言之，对所有 $x\in F$、$y\in F'$ 都有 $x\perp y$（或 $\langle x,y\rangle=0$）。这时我们称 $E$ 为 $F$ 与 $F'$ 的**正交和**。这不会与符号 $\perp$ 的另一种用法混淆：写 $F\perp F'$ 也可以仅表示 $F$ 与 $F'$ 垂直。上下文总能使我们的意思明确。

*本章大部分内容都用于给出带有这三类型之一的向量空间的某些正交分解，使和中的每个因子都属于易于辨认的类型。*

在对称型和厄米型的情形中，我们尤其关注分解成一维因子的直和分解。因此，若 $\langle\ ,\ \rangle$ 是对称型或厄米型，并且当 $i\ne j$ 时都有 $\langle v_i,v_j\rangle=0$，则称 $\{v_1,\ldots,v_n\}$ 为（关于该型的）**正交基**。可见，正交基给出了这样的分解。若该型非退化，并且 $\{v_1,\ldots,v_n\}$ 是正交基，则立即可见，对所有 $i$ 都有 $\langle v_i,v_i\rangle\ne0$。

**命题1.1。** *设 $E$ 是域 $k$ 上的向量空间，$g$ 是上述三类之一的型。假设 $E$ 写成正交和*

$$
E=E_1\perp\cdots\perp E_m.
$$

*则 $g$ 在 $E$ 上非退化当且仅当它在每个 $E_i$ 上非退化。若 $E_i^0$ 是 $g$ 在 $E_i$ 上的限制的核，则 $g$ 在 $E$ 中的核为正交和*

$$
E^0=E_1^0\perp\cdots\perp E_m^0.
$$

<span class="original-page-anchor" id="pdf-page-582" aria-hidden="true"></span>

*证明。* $E$ 的元素 $v,w$ 可以唯一地写成

$$
v=\sum_{i=1}^m v_i,\qquad w=\sum_{i=1}^m w_i,
$$

其中 $v_i,w_i\in E_i$。于是

$$
v\cdot w=\sum_{i=1}^m v_i\cdot w_i,
$$

且若对每个 $i=1,\ldots,m$ 都有 $v_i\cdot w_i=0$，则 $v\cdot w=0$。我们的断言由此显然成立。

注意，若 $E_1,\ldots,E_m$ 是 $k$ 上的向量空间，$g_1,\ldots,g_m$ 分别是这些空间上的型，则可以在直和 $E=E_1\oplus\cdots\oplus E_m$ 上定义型 $g=g_1\oplus\cdots\oplus g_m$；具体来说，若 $v,w$ 写成上述形式，我们就令

$$
g(v,w)=\sum_{i=1}^m g_i(v_i,w_i).
$$

于是显然，事实上有 $E=E_1\perp\cdots\perp E_m$。也可以写 $g=g_1\perp\cdots\perp g_m$。

**命题1.2。** *设 $E$ 是域 $k$ 上的有限维空间，$g$ 是 $E$ 上前述类型的型。假设 $g$ 非退化。设 $F$ 为 $E$ 的子空间。该型在 $F$ 上非退化当且仅当 $F+F^\perp=E$，也当且仅当该型在 $F^\perp$ 上非退化。*

*证明。* 有（这是第三章第5节的一个直接推论）

$$
\dim F+\dim F^\perp=\dim E=\dim(F+F^\perp)+\dim(F\cap F^\perp).
$$

因此，$F+F^\perp=E$ 当且仅当 $\dim(F\cap F^\perp)=0$。第一个断言立即成立。由于 $F,F^\perp$ 在维数条件中对称地出现，第二个断言也成立。

我们有时略微滥用术语，直接说 $E$ 非退化，来表示 $E$ 上的型非退化。

设 $E$ 是域 $k$ 上的有限维空间，$g$ 是前述类型的型。设 $E_0$ 是该型的核。于是得到同一类型的诱导型

$$
g_0:E/E_0\times E/E_0\to k,
$$

因为 $g(x,y)$ 只依赖于 $x$ 和 $y$ 模 $E_0$ 的陪集。此外，$g_0$ 非退化，因为它两侧的核均为 $0$。

设 $E,E'$ 是有限维向量空间，分别带有上述型 $g,g'$。若线性映射 $\sigma:E\to E'$ 满足

$$
g'(\sigma x,\sigma y)=g(x,y),
$$

则称其为**保度量映射**，<span class="original-page-anchor" id="pdf-page-583" aria-hidden="true"></span>或者，用点积记号表示，就是对所有 $x,y\in E$ 都有 $\sigma x\cdot\sigma y=x\cdot y$。若 $\sigma$ 是保度量的线性同构，则称 $\sigma$ 为**等距同构**。

设 $E,E_0$ 如上。于是商空间 $E/E_0$ 上有一个诱导型。若 $W$ 是 $E_0$ 的补子空间，即 $E=E_0\oplus W$，并且令 $\sigma:E\to E/E_0$ 为典范映射，则 $\sigma$ 保度量，并诱导出 $W$ 到 $E/E_0$ 的等距同构。这个断言是显然的，而且表明，若

$$
E=E_0\oplus W'
$$

是 $E$ 的另一个直和分解，则 $W'$ 与 $W$ 等距同构。我们知道 $W\approx E/E_0$ 非退化。因此，给定的型在核的补子空间上确定了一个在等距同构意义下唯一的非退化型。

## §2. 二次映射

设 $R$ 是交换环，$E,F$ 是 $R$-模。照例省略前缀 $R$-。回顾：若对所有 $x,y\in E$ 都有 $f(x,y)=f(y,x)$，则称双线性映射 $f:E\times E\to F$ 为对称的。

若每个满足 $2y=0$ 的 $y\in F$ 都为 $0$，则称 $F$ **没有 $2$-挠元**。（若 $2$ 在 $R$ 中可逆，这一点成立。）

设 $f:E\to F$ 是映射。若存在对称双线性映射 $g:E\times E\to F$ 和线性映射 $h:E\to F$，使得对所有 $x\in E$ 都有

$$
f(x)=g(x,x)+h(x),
$$

则称 $f$ 为**二次映射**（即 $R$-二次映射）。

**命题2.1。** *假设 $F$ 没有 $2$-挠元。设 $f:E\to F$ 为二次映射，像上面那样用一个对称双线性映射和一个线性映射表示。那么 $g,h$ 由 $f$ 唯一确定。对所有 $x,y\in E$，有*

$$
2g(x,y)=f(x+y)-f(x)-f(y).
$$

*证明。* 计算 $f(x+y)-f(x)-f(y)$ 得到 $2g(x,y)$。若 $g_1$ 对称双线性，$h_1$ 线性，且 $f(x)=g_1(x,x)+h_1(x)$，则 $2g(x,y)=2g_1(x,y)$。由 $F$ 没有 $2$-挠元，对所有 $x,y\in E$ 都有 $g(x,y)=g_1(x,y)$，所以 $g$ 唯一确定。随后，$h$ 由关系式

$$
h(x)=f(x)-g(x,x)
$$

确定。

我们称 $g,h$ 为与 $f$ **相伴**的双线性映射和线性映射。

若 $f:E\to F$ 是映射，定义

$$
\Delta f:E\times E\to F
$$

<span class="original-page-anchor" id="pdf-page-584" aria-hidden="true"></span>

其定义为

$$
\Delta f(x,y)=f(x+y)-f(x)-f(y).
$$

若 $f$ 是二次映射，并且与其相伴的线性映射为 $0$，则称 $f$ 为**齐次二次映射**。若对每个 $z\in F$ 都存在唯一的 $u\in F$，使 $2u=z$，则称 $F$ **可唯一地被 $2$ 除**。（同样，若 $2$ 在 $R$ 中可逆，这一点成立。）

**命题2.2。** *设 $f:E\to F$ 是映射，且 $\Delta f$ 双线性。假设 $F$ 可唯一地被 $2$ 除。那么映射 $x\mapsto f(x)-\frac12\Delta f(x,x)$ 是 $\mathbf Z$-线性的。若 $f$ 满足条件 $f(2x)=4f(x)$，则 $f$ 是齐次二次映射。*

*证明。* 显然。

$E$ 上的**二次型**是指取值于 $R$ 的齐次二次映射 $f:E\to R$。

以下主要讨论对称双线性型。二次型只处于次要地位。

## §3. 对称型，正交基

*设 $k$ 是特征 $\ne2$ 的域。*

设 $E$ 是 $k$ 上的向量空间，带有对称型 $g$。若对所有 $x,y\in E$ 都有 $\langle x,y\rangle=0$，则称 $g$ 为**零型**，或称 $E$ 为**全零空间**。由于已假设 $k$ 的特征 $\ne2$，条件“对所有 $x\in E$ 都有 $x^2=0$”蕴含 $g$ 是零型。事实上，

$$
4x\cdot y=(x+y)^2-(x-y)^2.
$$

**定理3.1。** *设 $E\ne0$，且在 $k$ 上有限维。设 $g$ 为 $E$ 上的对称型。那么存在一组正交基。*

*证明。* 先假设 $g$ 非退化，并在这种情形下用归纳法证明断言。若维数 $n$ 为 $1$，则断言显然成立。设 $n>1$。取 $v_1\in E$ 使 $v_1^2\ne0$（由于假设 $g$ 非退化，这样的元素存在）。设 $F=(v_1)$ 为由 $v_1$ 生成的子空间。那么 $F$ 非退化，由命题1.2，有

$$
E=F+F^\perp.
$$

此外，$\dim F^\perp=n-1$。设 $\{v_2,\ldots,v_n\}$ 为 $F^\perp$ 的一组正交基。

<span class="original-page-anchor" id="pdf-page-585" aria-hidden="true"></span>

那么 $\{v_1,\ldots,v_n\}$ 两两正交。此外，它们线性无关，因为若

$$
a_1v_1+\cdots+a_nv_n=0,
$$

其中 $a_i\in k$，则与 $v_i$ 取标量积，得到 $a_iv_i^2=0$，因而对所有 $i$ 都有 $a_i=0$。

**评述。** 事实上，我们已经证明：若 $g$ 非退化，且 $v\in E$ 满足 $v^2\ne0$，则可以把 $v$ 扩充成 $E$ 的一组正交基。

假设型 $g$ 退化。设 $E_0$ 为其核。可以把 $E$ 写成直和

$$
E=E_0\oplus W,
$$

其中 $W$ 为某个子空间。$g$ 在 $W$ 上的限制非退化；否则，$W$ 中就有一个非零元素属于 $E$ 的核。因此，若 $\{v_1,\ldots,v_r\}$ 为 $E_0$ 的一组基，$\{w_1,\ldots,w_{n-r}\}$ 为 $W$ 的一组正交基，则

$$
\{v_1,\ldots,v_r,w_1,\ldots,w_{n-r}\}
$$

为 $E$ 的一组正交基，证明完毕。

**推论3.2。** *设 $\{v_1,\ldots,v_n\}$ 为 $E$ 的一组正交基。假设 $i\leqq r$ 时 $v_i^2\ne0$，$i>r$ 时 $v_i^2=0$。那么 $E$ 的核等于 $(v_{r+1},\ldots,v_n)$。*

*证明。* 显然。

若 $\{v_1,\ldots,v_n\}$ 为 $E$ 的一组正交基，并写

$$
X=x_1v_1+\cdots+x_nv_n,
$$

其中 $x_i\in k$，则

$$
X^2=a_1x_1^2+\cdots+a_nx_n^2,
$$

其中 $a_i=\langle v_i,v_i\rangle$。以这种形式表示该型时，我们称它已被**对角化**。显然，关于一组正交基，该型对应的矩阵为对角矩阵，即

$$
\begin{pmatrix}
a_1&&&&&&\\
&a_2&&&0&&\\
&&\ddots&&&&\\
&&&a_r&&&\\
&0&&&0&&\\
&&&&&\ddots&\\
&&&&&&0
\end{pmatrix}.
$$

<span class="original-page-anchor" id="pdf-page-586" aria-hidden="true"></span>

**例。** 注意，第十三章习题33给出了一个涉及调和多项式的正交分解的有趣例子。

## §4. 有序域上的对称型

**定理4.1。**（西尔维斯特）*设 $k$ 是有序域，$E$ 是 $k$ 上的有限维向量空间，带有非退化对称型 $g$。存在整数 $r\geqq0$，使得若 $\{v_1,\ldots,v_n\}$ 是 $E$ 的一组正交基，则 $n$ 个元素 $v_1^2,\ldots,v_n^2$ 中恰有 $r$ 个 $>0$，恰有 $n-r$ 个 $<0$。*

*证明。* 对 $i=1,\ldots,n$，令 $a_i=v_i^2$。重新编号基元素，可设 $a_1,\ldots,a_r>0$，而 $i>r$ 时 $a_i<0$。设 $\{w_1,\ldots,w_n\}$ 是任意一组正交基，令 $b_i=w_i^2$。可设 $b_1,\ldots,b_s>0$，而 $j>s$ 时 $b_j<0$。我们要证明 $r=s$。事实上，只需证明

$$
v_1,\ldots,v_r,w_{s+1},\ldots,w_n
$$

线性无关，因为这样就有 $r+n-s\leqq n$，故 $r\leqq s$，再由对称性得 $r=s$。假设

$$
x_1v_1+\cdots+x_rv_r+y_{s+1}w_{s+1}+\cdots+y_nw_n=0.
$$

那么

$$
x_1v_1+\cdots+x_rv_r=-y_{s+1}w_{s+1}-\cdots-y_nw_n.
$$

两边平方，得

$$
a_1x_1^2+\cdots+a_rx_r^2=b_{s+1}y_{s+1}^2+\cdots+b_ny_n^2.
$$

左边 $\geqq0$，右边 $\leqq0$。因此两边都等于 $0$，由此得 $x_i=y_j=0$，即这些向量线性无关。

**推论4.2。** *假设 $k$ 的每个正元素都是平方。那么 $E$ 有一组正交基 $\{v_1,\ldots,v_n\}$，满足 $i\leqq r$ 时 $v_i^2=1$，$i>r$ 时 $v_i^2=-1$，并且 $r$ 唯一确定。*

*证明。* 将正交基中的每个向量除以其平方的绝对值的平方根。

具有该推论中性质的基称为**标准正交基**。若 $E$ 的元素 $X$ 关于这组基的坐标为 $(x_1,\ldots,x_n)$，则

$$
X^2=x_1^2+\cdots+x_r^2-x_{r+1}^2-\cdots-x_n^2.
$$

<span class="original-page-anchor" id="pdf-page-587" aria-hidden="true"></span>

若对所有 $X\in E$、$X\ne0$ 都有 $X^2>0$，则称对称型 $g$ **正定**。这当且仅当定理4.1中的 $r=n$。若对所有 $X\in E$、$X\ne0$ 都有 $X^2<0$，则称 $g$ **负定**。

**推论4.3。** *向量空间 $E$ 存在正交分解 $E=E^+\perp E^-$，使 $g$ 在 $E^+$ 上正定，在 $E^-$ 上负定。在所有这样的分解中，$E^+$（或 $E^-$）的维数相同。*

*现在假设型 $g$ 正定，并且 $k$ 的每个正元素都是平方。*

定义元素 $v\in E$ 的**范数**为

$$
|v|=\sqrt{v\cdot v}.
$$

于是，若 $v\ne0$，则 $|v|>0$。对所有 $v,w\in E$，还有**施瓦茨不等式**

$$
|v\cdot w|\leqq|v|\,|w|.
$$

其证明采用通常的方法：利用双线性展开

$$
0\leqq(av\pm bw)^2=(av\pm bw)\cdot(av\pm bw),
$$

并令 $b=|v|$、$a=|w|$。得到

$$
\mp2ab\,v\cdot w\leqq2|v|^2|w|^2.
$$

若 $|v|$ 或 $|w|$ 为 $0$，不等式显然成立。若两者均不为 $0$，则除以 $|v|\,|w|$，得到所需结论。

由施瓦茨不等式，得出三角不等式

$$
|v+w|\leqq|v|+|w|.
$$

我们将它留给读者，作为一个常规练习。

对于正定型，可以从任意一组基 $\{v_1,\ldots,v_n\}$ 出发，归纳地用典范方式得到一组标准正交基。令

$$
v'_1=\frac1{|v_1|}v_1.
$$

那么 $v'_1$ 的范数为 $1$。

**译校注：** 原书写作“Then $v_1$ has norm $1$”。这里刚刚归一化的是 $v'_1=v_1/|v_1|$；原来的 $v_1$ 是任意基向量，其范数未必为 $1$，故应为 $v'_1$。

令

$$
w_2=v_2-(v_2\cdot v'_1)v'_1,
$$

再令

$$
v'_2=\frac1{|w_2|}w_2.
$$

<span class="original-page-anchor" id="pdf-page-588" aria-hidden="true"></span>

归纳地，令

$$
w_r=v_r-(v_r\cdot v'_1)v'_1-\cdots-(v_r\cdot v'_{r-1})v'_{r-1},
$$

再令

$$
v'_r=\frac1{|w_r|}w_r.
$$

于是 $\{v'_1,\ldots,v'_n\}$ 为一组标准正交基。刚才描述的归纳过程称为**格拉姆—施密特正交化**。

## §5. 厄米型

设 $k_0$ 为有序域（如果愿意，可取实数域的一个子域），并令 $k=k_0(i)$，其中 $i=\sqrt{-1}$。那么 $k$ 有一个阶为 $2$ 的自同构，其不动域为 $k_0$。

设 $E$ 为 $k$ 上的有限维向量空间。我们要讨论 $E$ 上的厄米型，即映射

$$
E\times E\to k,
$$

记作

$$
(x,y)\mapsto\langle x,y\rangle,
$$

它对第一个变量 $k$-线性，对第二个变量 $k$-反线性，并且对所有 $x,y\in E$ 都有

$$
\langle x,y\rangle=\overline{\langle y,x\rangle}.
$$

注意，对所有 $x\in E$ 都有 $\langle x,x\rangle\in k_0$。这基本上就是关于对称型的各个断言的证明在厄米型情形中几乎无需改动就仍然成立的原因。现在列出适用于这种情形的性质。

**定理5.1。** *存在一组正交基。若该型非退化，则存在整数 $r$，具有以下性质：若 $\{v_1,\ldots,v_n\}$ 为一组正交基，则 $n$ 个元素*

$$
\langle v_1,v_1\rangle,\ldots,\langle v_n,v_n\rangle
$$

*中恰有 $r$ 个 $>0$，恰有 $n-r$ 个 $<0$。*

<span class="original-page-anchor" id="pdf-page-589" aria-hidden="true"></span>

满足 $\langle v_i,v_i\rangle=1$ 或 $-1$ 的正交基 $\{v_1,\ldots,v_n\}$ 称为**标准正交基**。

**推论5.2。** *假设该型非退化，并且 $k_0$ 的每个正元素都是平方。那么存在一组标准正交基。*

若对所有非零 $x\in E$ 都有 $\langle x,x\rangle>0$，则称该厄米型**正定**。

**译校注：** 原书正定的定义写作“$\langle x,x\rangle>0$ for all $x\in E$”，漏去 $x\ne0$。由线性性，$\langle0,0\rangle=0$，故不等式不可能在零向量处成立；应与前节的正定定义一样限定非零向量。

若对所有 $x\in E$、$x\ne0$ 都有 $\langle x,x\rangle<0$，则称其**负定**。

**推论5.3。** *假设该型非退化。那么 $E$ 存在正交分解 $E=E^+\perp E^-$，使该型在 $E^+$ 上正定，在 $E^-$ 上负定。在所有这样的分解中，$E^+$（或 $E^-$）的维数相同。*

定理5.1及其推论的证明与对称型情形的相应结论的证明相同，留给读者完成。

对任意 $k$-线性映射 $A:E\to E$，有**极化恒等式**

$$
\langle A(x+y),(x+y)\rangle-\langle A(x-y),(x-y)\rangle=2[\langle Ax,y\rangle+\langle Ay,x\rangle].
$$

若对所有 $x$ 都有 $\langle Ax,x\rangle=0$，将 $x$ 换成 $ix$，得到

$$
\langle Ax,y\rangle+\langle Ay,x\rangle=0,
$$

$$
i\langle Ax,y\rangle-i\langle Ay,x\rangle=0.
$$

由此得出：

*若对所有 $x$ 都有 $\langle Ax,x\rangle=0$，则 $A=0$。*

> **译校注：** 这里保留原书的结论“若对所有 $x$ 都有 $\langle Ax,x\rangle=0$，则 $A=0$”。由上面的极化等式实际先得到 $\langle Ax,y\rangle=0$ 对所有 $x,y$ 成立，即 $A(E)\subset\operatorname{rad}g$；若该厄米型非退化（例如正定），才由此推出 $A=0$。本节此前也允许一般厄米型，因此在退化情形中应保留这个条件区分。

这是唯一一个在对称型情形中没有对应结论的断言。上述一个线性方程中出现的 $i$ 对结论至关重要。实际应用中，人们在复数情形中使用这一断言；而在实数情形中，当 $A$ 对称时，会遇到类似的情况。这时，关于对称映射的断言是显然的。

*假设厄米型正定，并且 $k_0$ 的每个正元素都是平方。*

有**施瓦茨不等式**

$$
|\langle x,y\rangle|^2\leqq\langle x,x\rangle\langle y,y\rangle.
$$

其证明仍然通过展开

$$
0\leqq\langle\alpha x+\beta y,\alpha x+\beta y\rangle,
$$

并取 $\alpha=\langle y,y\rangle$、$\beta=-\langle x,y\rangle$ 得到。

定义范数 $|x|$ 为

$$
|x|=\sqrt{\langle x,x\rangle}.
$$

<span class="original-page-anchor" id="pdf-page-590" aria-hidden="true"></span>

立即得到三角不等式

$$
|x+y|\leqq|x|+|y|,
$$

并且对 $\alpha\in k$，有

$$
|\alpha x|=|\alpha|\,|x|.
$$

与对称型情形一样，给定一组基，可以通过逐次减去投影的归纳过程，得到一组标准正交基。这留给读者完成。

## §6. 谱定理（厄米情形）

*本节始终设 $E$ 为 $\mathbf C$ 上的有限维空间，维数 $\geqq1$，并赋予 $E$ 一个正定厄米型。*

设 $A:E\to E$ 是 $E$ 到自身的线性映射（即 $\mathbf C$-线性映射）。对固定的 $y\in E$，映射 $x\mapsto\langle Ax,y\rangle$ 是线性泛函，因此存在唯一的元素 $y^*\in E$，使得对所有 $x\in E$ 都有

$$
\langle Ax,y\rangle=\langle x,y^*\rangle.
$$

以 $A^*y=y^*$ 定义映射 $A^*:E\to E$。立即可见，$A^*$ 是线性的；我们称 $A^*$ 为 $A$ 关于给定厄米型的**伴随**。

对 $E$ 到自身的任意线性映射 $A,B$，容易验证以下公式：

$$
\begin{aligned}
(A+B)^*&=A^*+B^*,& A^{**}&=A,\\
(\alpha A)^*&=\bar\alpha A^*,& (AB)^*&=B^*A^*.
\end{aligned}
$$

若 $A^*=A$，则称线性映射 $A$ 为**自伴随的**（或**厄米的**）。

**命题6.1。** *$A$ 是厄米的当且仅当对所有 $x\in E$，$\langle Ax,x\rangle$ 都是实数。*

*证明。* 设 $A$ 是厄米的。那么

$$
\overline{\langle Ax,x\rangle}=\overline{\langle x,Ax\rangle}=\langle Ax,x\rangle,
$$

故 $\langle Ax,x\rangle$ 是实数。反过来，假设对所有 $x$，$\langle Ax,x\rangle$ 都是实数。那么

$$
\langle Ax,x\rangle=\overline{\langle Ax,x\rangle}=\langle x,Ax\rangle=\langle A^*x,x\rangle,
$$

因此，对所有 $x$ 都有 $\langle(A-A^*)x,x\rangle=0$。由极化恒等式，$A=A^*$。

<span class="original-page-anchor" id="pdf-page-591" aria-hidden="true"></span>

设 $A:E\to E$ 为线性映射。若存在 $\lambda\in\mathbf C$，使 $A\xi=\lambda\xi$，则称元素 $\xi\in E$ 为 $A$ 的**特征向量**。若 $\xi\ne0$，则称 $\lambda$ 为 $A$ 的属于 $\xi$ 的**特征值**。

**命题6.2。** *设 $A$ 为厄米映射。那么 $A$ 的所有属于非零特征向量的特征值都是实数。若 $\xi,\xi'$ 是非零特征向量，分别具有特征值 $\lambda,\lambda'$，且 $\lambda\ne\lambda'$，则 $\xi\perp\xi'$。*

*证明。* 设 $\lambda$ 是属于特征向量 $\xi\ne0$ 的特征值。那么 $\langle A\xi,\xi\rangle=\langle\xi,A\xi\rangle$，这两个数分别等于 $\lambda\langle\xi,\xi\rangle$ 和 $\bar\lambda\langle\xi,\xi\rangle$。由 $\xi\ne0$，得 $\lambda=\bar\lambda$，即 $\lambda$ 为实数。其次，假设 $\xi,\xi'$ 及 $\lambda,\lambda'$ 如上所述。那么

$$
\langle A\xi,\xi'\rangle=\lambda\langle\xi,\xi'\rangle=\langle\xi,A\xi'\rangle=\lambda'\langle\xi,\xi'\rangle,
$$

由此得 $\langle\xi,\xi'\rangle=0$。

**引理6.3。** *设 $A:E\to E$ 为线性映射，且 $\dim E\geqq1$。那么 $A$ 至少有一个非零特征向量。*

*证明。* 考虑 $\mathbf C[A]$，即由 $A$ 在 $\mathbf C$ 上生成的环。作为 $\mathbf C$ 上的向量空间，它包含在 $E$ 的自同态环中；后者有限维，若 $n=\dim E$，则其维数与所有 $n\times n$ 矩阵所构成的环的维数相同。因此存在系数在 $\mathbf C$ 中的非零多项式 $P$，使 $P(A)=0$。可将 $P$ 分解成一次因子的乘积，

$$
P(X)=(X-\lambda_1)\cdots(X-\lambda_m),
$$

其中 $\lambda_j\in\mathbf C$。于是 $(A-\lambda_1I)\cdots(A-\lambda_mI)=0$。因此各个因子 $A-\lambda_jI$ 不可能全为同构，故存在 $\lambda\in\mathbf C$，使 $A-\lambda I$ 不是同构。于是它的核中有一个元素 $\xi\ne0$，且 $A\xi-\lambda\xi=0$。这说明 $\xi$ 为非零特征向量，正是所需结论。

**定理6.4（谱定理，厄米情形）。** *设 $E$ 为复数域上的非零有限维向量空间，带有正定厄米型。设 $A:E\to E$ 为厄米线性映射。那么 $E$ 有一组由 $A$ 的特征向量构成的正交基。*

*证明。* 设 $\xi_1$ 为非零特征向量，特征值为 $\lambda_1$，设 $E_1$ 为由 $\xi_1$ 生成的子空间。那么 $A$ 把 $E_1^\perp$ 映到自身，因为

$$
\langle AE_1^\perp,\xi_1\rangle=\langle E_1^\perp,A\xi_1\rangle=\langle E_1^\perp,\lambda_1\xi_1\rangle=\lambda_1\langle E_1^\perp,\xi_1\rangle=0,
$$

故 $AE_1^\perp$ 与 $\xi_1$ 垂直。

由于 $\xi_1\ne0$，有 $\langle\xi_1,\xi_1\rangle>0$；而我们的厄米型非退化（因其正定），所以

$$
E=E_1\oplus E_1^\perp.
$$

<span class="original-page-anchor" id="pdf-page-592" aria-hidden="true"></span>

给定型在 $E_1^\perp$ 上的限制正定（若 $\dim E>1$）。由命题6.1，立即可见 $A$ 在 $E_1^\perp$ 上的限制是厄米的。因此可用归纳法完成证明。

**推论6.5。** *在定理的假设下，存在一组由 $A$ 的特征向量构成的标准正交基。*

*证明。* 把正交基中的每个向量除以其范数。

**推论6.6。** *设 $E$ 为复数域上的非零有限维向量空间，带有正定厄米型 $f$。设 $g$ 为 $E$ 上的另一个厄米型。那么 $E$ 有一组同时关于 $f$ 和 $g$ 正交的基。*

*证明。* 写 $f(x,y)=\langle x,y\rangle$。由于 $f$ 正定，从而非奇异，存在唯一的厄米线性映射 $A$，使得对所有 $x,y\in E$，都有 $g(x,y)=\langle Ax,y\rangle$。把定理应用于 $A$，得到定理中那样的一组基，记作 $\{v_1,\ldots,v_n\}$。设 $\lambda_i$ 为满足 $Av_i=\lambda_iv_i$ 的特征值。那么

$$
g(v_i,v_j)=\langle Av_i,v_j\rangle=\lambda_i\langle v_i,v_j\rangle,
$$

因此这组基也关于 $g$ 正交，证明完毕。

回顾：线性映射 $U:E\to E$ 是**酉映射**当且仅当 $U^*=U^{-1}$。此条件等价于：对所有元素 $x,y\in E$，都有 $\langle Ux,Uy\rangle=\langle x,y\rangle$。换言之，$U$ 是型 $f$ 的自同构。

**定理6.7（谱定理，酉情形）。** *设 $E$ 为复数域上的非零有限维向量空间，带有正定厄米型。设 $U:E\to E$ 为酉线性映射。那么 $E$ 有一组由 $U$ 的特征向量构成的正交基。*

*证明。* 设 $\xi_1\ne0$ 为 $U$ 的特征向量。利用关系 $U^*=U^{-1}$，立即可验证 $E$ 中与 $\xi_1$ 正交的子空间被 $U$ 映到自身，因为若 $\eta$ 与 $\xi_1$ 垂直，则

$$
\langle U\eta,\xi_1\rangle=\langle\eta,U^*\xi_1\rangle=\langle\eta,U^{-1}\xi_1\rangle=\langle\eta,\lambda^{-1}\xi_1\rangle=0.
$$

于是可像前面一样用归纳法完成证明。

**评述。** 若 $\lambda$ 为酉映射 $U$ 的特征值，则 $\lambda$ 的绝对值必为 $1$（因为 $U$ 保持长度），所以 $\lambda$ 可写成 $e^{i\theta}$，其中 $\theta$ 为实数，而我们可以把 $U$ 看作旋转。

设 $A:E\to E$ 为可逆线性映射。正如非零复数可写成 $z=re^{i\theta}$，其中 $r>0$，$A$ 也可以分解成一个乘积，称为其极分解。设 $P:E\to E$ 为线性映射。若 $P$ 是厄米的，并且对所有 $x\in E$ 都有 $\langle Px,x\rangle\geqq0$，则称 $P$ **半正定**。若对 $E$ 中所有 $x\ne0$ 都有 $\langle Px,x\rangle>0$，则称 $P$ **正定**。例如，<span class="original-page-anchor" id="pdf-page-593" aria-hidden="true"></span>若令 $P=A^*A$，则可见 $P$ 正定，因为

$$
\langle A^*Ax,x\rangle=\langle Ax,Ax\rangle>0\quad\text{若 }x\ne0.
$$

**命题6.8。** *设 $P$ 半正定。那么 $P$ 有唯一的半正定平方根 $B:E\to E$，即一个满足 $B^2=P$ 的半正定线性映射。*

*证明。* 为简单起见，假设 $P$ 正定。由谱定理，$E$ 有一组由特征向量构成的基。特征值必为 $>0$（由正定性条件立即可得）。将每个特征向量映到它与相应特征值的平方根的乘积，由此定义的线性映射满足所需条件。关于唯一性，由 $B^2=P$，$B$ 与 $P$ 交换；所以若 $\{v_1,\ldots,v_n\}$ 是由 $P$ 的特征向量构成的基，则每个 $v_i$ 也是 $B$ 的特征向量。（参见第十四章习题12和13(d)。）由于正数有唯一的正平方根，$B$ 唯一确定：它是唯一一个将 $v_i$ 乘以 $P$ 的相应特征值的平方根的线性映射。

**定理6.9。** *设 $A:E\to E$ 为可逆线性映射。那么 $A$ 可以唯一地写成乘积 $A=UP$，其中 $U$ 为酉映射，$P$ 正定。*

*证明。* 令 $P=(A^*A)^{1/2}$，$U=AP^{-1}$。利用定义，立即验证 $U$ 为酉映射，因此得到分解的存在性。关于唯一性，假设 $A=U_1P_1$。令

$$
U_2=PP_1^{-1}=U^{-1}U_1.
$$

那么 $U_2$ 为酉映射，故 $U_2^*U_2=I$。由 $P^*=P$ 和 $P_1^*=P_1$，得 $P^2=P_1^2$。由于 $P,P_1$ 都是厄米正定的，像命题6.8中那样，得 $P=P_1$，定理得证。

**评述。** 证明定理6.9所用的论证适用于分析中的希尔伯特空间。参见拙著《Real Analysis》。不过，由于可能不存在“特征值”，证明唯一性必须使用该书介绍的另一种分析方法。

术语上，定理6.9中的表达式 $A=UP$ 称为 $A$ 的**极分解**。当然，写出分解时，因子的次序确实重要。还有唯一的分解 $A=P_1U_1$，其中 $P_1$ 正定，$U_1$ 为酉映射（对 $A^{-1}$ 应用定理6.9，再取逆）。

## §7. 谱定理（对称情形）

*设 $E$ 为实数域上的有限维向量空间，$g$ 为 $E$ 上的对称正定型。* 若 $A:E\to E$ 为线性映射，我们知道<span class="original-page-anchor" id="pdf-page-594" aria-hidden="true"></span>其关于 $g$ 的转置由条件

$$
\langle Ax,y\rangle=\langle x,{}^tAy\rangle
$$

定义，其中 $x,y\in E$。若 $A={}^tA$，则称 $A$ **对称**。与前面一样，若存在 $\lambda\in\mathbf R$，使 $A\xi=\lambda\xi$，则称元素 $\xi\in E$ 为 $A$ 的特征向量；若 $\xi\ne0$，则称 $\lambda$ 为特征值。

**定理7.1（谱定理，对称情形）。** *设 $E\ne0$。设 $A:E\to E$ 为对称线性映射。那么 $E$ 有一组由 $A$ 的特征向量构成的正交基。*

*证明。* 若为正定型选取一组正交基，则 $A$ 关于这组基的矩阵为实对称矩阵，因而归结为考虑 $E=\mathbf R^n$ 的情形。

> **译校注（归一化说明）：** 原书这里写“an orthogonal basis”，并说关于该基的矩阵为实对称矩阵。要从关于给定正定型的自伴随性直接得到通常的实对称矩阵，应把这组正交基先归一化为标准正交基。若未归一化，其 Gram 矩阵为 $D$，矩阵条件一般是 ${}^tM D=DM$，而非 ${}^tM=M$；例如 $D=\operatorname{diag}(1,4)$、$M=\begin{pmatrix}0&4\\1&0\end{pmatrix}$ 满足前一条件，却不是对称矩阵。正定性保证可以逐个除以范数完成归一化，因而这里补足的是证明中选基的一步，定理结论不受影响。原句保留。

设 $M$ 为表示 $A$ 的矩阵。可以把 $M$ 看作作用于 $\mathbf C^n$，这时 $M$ 表示一个厄米线性映射。设 $z\ne0$ 为 $M$ 的复特征向量，写

$$
z=x+iy,
$$

其中 $x,y\in\mathbf R^n$。由命题6.2，$M$ 的属于 $z$ 的特征值 $\lambda$ 为实数，并且 $Mz=\lambda z$。因此 $Mx=\lambda x$，$My=\lambda y$。但必有 $x\ne0$ 或 $y\ne0$。这样就在 $E$ 中找到了 $M$，也就是 $A$，的一个非零特征向量。现在可像前面那样继续。该特征向量在 $E$ 中的正交补的维数为 $(n-1)$，且被 $A$ 映到自身。因此可以用归纳法完成证明。

**评述。** 谱定理在实闭域上仍然成立；我们的证明无需任何改动。此外，这些证明与分析中针对希尔伯特空间和紧算子的证明相当接近。不过，特征值和特征向量的存在性必须用不同方法证明，例如使用我们实际上已在第十二章证明的盖尔范德—马祖尔定理，或使用变分原理（即求出依赖于该算子的二次函数的极大值或极小值）。

**推论7.2。** *在定理的假设下，存在一组由 $A$ 的特征向量构成的标准正交基。*

*证明。* 把正交基中的每个向量除以其范数。

**推论7.3。** *设 $E$ 为实数域上的非零有限维向量空间，带有正定对称型 $f$。设 $g$ 为 $E$ 上的另一个对称型。那么 $E$ 有一组同时关于 $f$ 和 $g$ 正交的基。*

*证明。* 写 $f(x,y)=\langle x,y\rangle$。由于 $f$ 正定，从而非奇异，存在唯一的对称线性映射 $A$，使

$$
g(x,y)=\langle Ax,y\rangle
$$

<span class="original-page-anchor" id="pdf-page-595" aria-hidden="true"></span>

对所有 $x,y\in E$ 都成立。把定理应用于 $A$，得到定理中那样的一组基。显然，它是关于 $g$ 的正交基（参见厄米情形中的同一证明）。

命题6.8的对应结论和极分解在本情形中也成立，证明相同。见习题9。

## §8. 交错型

设 $E$ 为域 $k$ 上的向量空间，现在对 $k$ 不作任何限制。设 $f$ 为 $E$ 上的交错型，即双线性映射 $f:E\times E\to k$，使得对所有 $x\in E$ 都有 $f(x,x)=x^2=0$。那么对所有 $x,y\in E$，有

$$
x\cdot y=-y\cdot x;
$$

这是在 $x^2=0$ 中用 $(x+y)$ 替换 $x$ 得到的。

定义**双曲平面**（对于交错型）为非退化的二维空间。自然存在元素 $w$，使 $w^2=0$、$w\ne0$。若 $P$ 为双曲平面，$w\in P$、$w\ne0$，则 $P$ 中存在元素 $y\ne0$，使 $w\cdot y\ne0$。把 $y$ 除以某个常数后，可以假设 $w\cdot y=1$。那么 $y\cdot w=-1$。因此，该型关于基 $\{w,y\}$ 的矩阵为

$$
\begin{pmatrix}0&1\\-1&0\end{pmatrix}.
$$

像前面一样，称向量对 $w,y$ 为**双曲对**。给定 $k$ 上带有双线性型的二维向量空间，若元素对 $\{w,y\}$ 满足关系式

$$
w^2=y^2=0,\qquad y\cdot w=-1,\qquad w\cdot y=1,
$$

则可见该型交错，且 $(w,y)$ 是该型的一个双曲平面。

给定 $E$ 上的交错型 $f$，若 $E$ 为双曲平面的正交和，则称 $E$（或 $f$）为**双曲的**。若对所有 $x,y\in E$ 都有 $x\cdot y=0$，则称 $E$ 为**全零空间**（或称 $f$ 为**零型**）。

**定理8.1。** *设 $f$ 为 $k$ 上有限维向量空间 $E$ 上的交错型。那么 $E$ 为其核与一个双曲子空间的正交和。若 $E$ 非退化，则 $E$ 为双曲空间，其维数为偶数。*

*证明。* 核的补子空间非退化，因此可以假设 $E$ 非退化。取 $w\in E$、$w\ne0$。存在 $y\in E$，使 $w\cdot y\ne0$ 且 $y\ne0$。于是 $(w,y)$ 非退化，故为双曲平面 $P$。有 $E=P\oplus P^\perp$，并且 $P^\perp$ 非退化。我们<span class="original-page-anchor" id="pdf-page-596" aria-hidden="true"></span>用归纳法完成证明。

**推论8.2。** *域 $k$ 上给定维数的所有非退化交错型都等距同构。*

由定理8.1可见，$E$ 有一组基，使交错型关于这组基的矩阵为

![交错型在正交和基下的矩阵](/library/volume-86/diagrams/pdf-0596-alternating-normal-form.png)

为书写方便，将双曲平面的正交和的基元素重新排序，使该型的矩阵为

$$
\begin{pmatrix}0&I_r&0\\-I_r&0&0\\0&0&0\end{pmatrix},
$$

其中 $I_r$ 为 $r\times r$ 单位矩阵。矩阵

$$
\begin{pmatrix}0&I_r\\-I_r&0\end{pmatrix}
$$

称为**标准交错矩阵**。

**推论8.3。** *设 $E$ 为 $k$ 上的有限维向量空间，带有一个记作 $\langle\ ,\ \rangle$ 的非退化对称型。设 $\Omega$ 为 $E$ 上的非退化交错型。那么存在直和分解 $E=E_1\oplus E_2$，以及 $E$ 的一个（关于 $\langle\ ,\ \rangle$）对称自同构 $A$，具有以下性质。若 $x,y\in E$ 写成*

$$
\begin{aligned}
x&=(x_1,x_2),\quad x_1\in E_1,\quad x_2\in E_2,\\
y&=(y_1,y_2),\quad y_1\in E_1,\quad y_2\in E_2,
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-597" aria-hidden="true"></span>

*则*

$$
\Omega(x,y)=\langle Ax_1,y_2\rangle-\langle Ax_2,y_1\rangle.
$$

*证明。* 选取 $E$ 的一组基，使 $\Omega$ 关于这组基的矩阵为标准交错矩阵。设 $f$ 为由关于这组基的点积给出的 $E$ 上的非退化对称型。那么得到 $E$ 到子空间 $E_1,E_2$ 的直和分解（分别对应前 $n$ 个和后 $n$ 个坐标），使

$$
\Omega(x,y)=f(x_1,y_2)-f(x_2,y_1).
$$

> **译校注（配对说明）：** 原书把 $f$ 定义为“the dot product with respect to this basis”，随后写 $\Omega(x,y)=f(x_1,y_2)-f(x_2,y_1)$，其中 $E_1,E_2$ 是这组基的前、后两半坐标子空间。若 $f$ 按 $E$ 上通常的坐标点积理解，则两半互相正交，右端两项都为 $0$，不能给出非退化的 $\Omega$。因此，这一步不能仅由字面的点积定义推出，尚须说明所使用的跨子空间配对。这里保留原证明与公式，只指出这一具体限制，不主张给出了完整修正。

由于假设 $\langle\ ,\ \rangle$ 非退化，可以找到具有所需作用的自同构 $A$；而且，由 $f$ 对称，$A$ 也对称。

## §9. 普法夫式

交错矩阵是满足 ${}^tG=-G$ 且对角元全为 $0$ 的矩阵 $G$。如第十三章第6节所见，它是交错型的矩阵。设 $G$ 为 $n\times n$ 矩阵，并假设 $n$ 为*偶数*。（$n$ 为奇数时，参见习题。）

先在特征 $0$ 的域上讨论。由推论8.2，存在非奇异矩阵 $C$，使 ${}^tCGC$ 为矩阵

$$
\begin{pmatrix}0&I_r&0\\-I_r&0&0\\0&0&0\end{pmatrix},
$$

因而

$$
\det(C)^2\det(G)=1\quad\text{或}\quad0,
$$

分别对应交错型的核为零或非零的情形。所以，无论哪种情形，$\det(G)$ 都是该域中的平方。

现在转到整数环 $\mathbf Z$ 上。设 $t_{ij}$ $(1\leqq i<j\leqq n)$ 为 $\mathbf Q$ 上的 $n(n-1)/2$ 个代数无关的元素，对 $i=1,\ldots,n$，令 $t_{ii}=0$，并在 $i>j$ 时令 $t_{ij}=-t_{ji}$。那么矩阵 $T=(t_{ij})$ 交错，故 $\det(T)$ 是域 $\mathbf Q(t)$ 中的平方；该域由向 $\mathbf Q$ 添加所有变量 $t_{ij}$ 得到。不过，$\det(T)$ 是 $\mathbf Z[t]$ 中的多项式，而 $\mathbf Z[t]$ 中有唯一分解，因此 $\det(T)$ 是 $\mathbf Z[t]$ 中一个多项式的平方。可以写

$$
\det(T)=P(t)^2.
$$

多项式 $P$ 在相差一个因子 $\pm1$ 的意义下唯一确定。如果代入<span class="original-page-anchor" id="pdf-page-598" aria-hidden="true"></span>$t_{ij}$ 的值，使矩阵 $T$ 特化为

$$
\begin{pmatrix}0&I_{n/2}\\-I_{n/2}&0\end{pmatrix},
$$

则可见，存在唯一的整数系数多项式 $P$，在这组特化的 $(t)$ 值处取值 $1$。称 $P$ 为阶数 $n$ 的**一般普法夫式**，记作 $\operatorname{Pf}$。

设 $R$ 为交换环。由 $\mathbf Z$ 到 $R$ 的唯一同态诱导出同态

$$
\mathbf Z[t]\to R[t].
$$

阶数 $n$ 的一般普法夫式在 $R[t]$ 中的像是系数在 $R$ 中的多项式，仍记作 $\operatorname{Pf}$。若 $G$ 为系数在 $R$ 中的交错矩阵，则用 $\operatorname{Pf}(G)$ 表示在 $\operatorname{Pf}$ 中将 $t_{ij}$ 替换为 $g_{ij}$ 后所得的 $\operatorname{Pf}(t)$ 的值。由于行列式与同态可交换，有：

**定理9.1。** *设 $R$ 为交换环。设 $(g_{ij})=G$ 为交错矩阵，其中 $g_{ij}\in R$。那么*

$$
\det(G)=(\operatorname{Pf}(G))^2.
$$

*此外，若 $C$ 为 $R$ 上的 $n\times n$ 矩阵，则*

$$
\operatorname{Pf}(CG\,{}^tC)=\det(C)\operatorname{Pf}(G).
$$

*证明。* 第一个断言已在上面证明。第二个断言只需在 $\mathbf Z$ 上证明。设 $u_{ij}$ $(i,j=1,\ldots,n)$ 在 $\mathbf Q$ 上代数无关，并且 $u_{ij},t_{ij}$ 一起在 $\mathbf Q$ 上代数无关。设 $U$ 为矩阵 $(u_{ij})$。那么

$$
\operatorname{Pf}(UT\,{}^tU)=\pm\det(U)\operatorname{Pf}(T),
$$

两边平方便立即得到这一点。给 $U,T$ 代入值，使 $U$ 成为单位矩阵，$T$ 成为标准交错矩阵。由此得出右边必为 $+$ 号。像通常一样，对 $U$ 代入 $R$ 上的任意矩阵，对 $T$ 代入 $R$ 上的任意交错矩阵，便得到我们的断言，证明完毕。

## §10. 维特定理

回到对称型，设 $k$ 为特征 $\ne2$ 的域。

<span class="original-page-anchor" id="pdf-page-599" aria-hidden="true"></span>

设 $E$ 为 $k$ 上的向量空间，带有对称型。若该型非退化，$E$ 的维数为 $2$，并且 $E$ 中存在元素 $w\ne0$，使 $w^2=0$，则称 $E$ 为**双曲平面**。若 $E$ 为双曲平面的正交和，则称 $E$ 为**双曲空间**。也称 $E$ 上的型为双曲的。

假设 $E$ 为双曲平面，且有元素 $w\ne0$，使 $w^2=0$。取 $u\in E$，使 $E=(w,u)$。那么 $u\cdot w\ne0$；否则 $w$ 就是核中的非零元素。取 $b\in k$，使 $w\cdot bu=bw\cdot u=1$。再选 $a\in k$，使

$$
(aw+bu)^2=2ab\,w\cdot u+b^2u^2=0.
$$

（这是可以做到的，因为这里是关于 $a$ 的线性方程。）令 $v=aw+bu$。于是找到 $E$ 的一组基，即 $E=(w,v)$，满足

$$
w^2=v^2=0\quad\text{且}\quad w\cdot v=1.
$$

因此，给定型关于这组基的矩阵为

$$
\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

反过来，若空间 $E$ 有一组基 $\{w,v\}$，满足 $w^2=v^2=0$ 和 $w\cdot v=1$，则 $E$ 非退化，因而为双曲平面。满足这些关系式的基 $\{w,v\}$ 称为**双曲对**。

非退化空间的正交和非退化，因此双曲空间非退化。注意，双曲空间总有偶数维数。

**引理10.1。** *设 $E$ 为 $k$ 上的有限维向量空间，带有非退化对称型 $g$。设 $F$ 为子空间，$F_0$ 为 $F$ 的核，并假设有正交分解*

$$
F=F_0\perp U.
$$

*设 $\{w_1,\ldots,w_s\}$ 为 $F_0$ 的一组基。那么 $E$ 中存在与 $U$ 垂直的元素 $v_1,\ldots,v_s$，使每个元素对 $\{w_i,v_i\}$ 都是生成双曲平面 $P_i$ 的双曲对，并且有正交分解*

$$
U\perp P_1\perp\cdots\perp P_s.
$$

*证明。* 令

$$
U_1=(w_2,\ldots,w_s)\oplus U.
$$

那么 $U_1$ 严格包含在 $F_0\oplus U$ 中，因此 $(F_0\oplus U)^\perp$<span class="original-page-anchor" id="pdf-page-600" aria-hidden="true"></span>严格包含在 $U_1^\perp$ 中。因此存在元素 $u_1\in U_1^\perp$，但

$$
u_1\notin(F_0\oplus U)^\perp.
$$

有 $w_1\cdot u_1\ne0$，故 $(w_1,u_1)$ 为双曲平面 $P_1$。前面已经看到，可以找到 $v_1\in P_1$，使 $\{w_1,v_1\}$ 为双曲对。此外，得到正交和分解

$$
F_1=(w_2,\ldots,w_s)\perp P_1\perp U.
$$

显然 $(w_2,\ldots,w_s)$ 为 $F_1$ 的核，可以用归纳法完成证明。

**定理10.2。** *设 $E$ 为 $k$ 上的有限维向量空间，$g$ 为 $E$ 上的非退化对称型。设 $F,F'$ 为 $E$ 的子空间，$\sigma:F\to F'$ 为等距同构。那么 $\sigma$ 可以延拓为 $E$ 到自身的等距同构。*

*证明。* 先将证明归结到 $F$ 非退化的情形。像前一节的引理中那样，可写 $F=F_0\perp U$，于是 $\sigma F=F'=\sigma F_0\perp\sigma U$。此外，$\sigma F_0=F'_0$ 为 $F'$ 的核。现在，像引理中那样，可将 $F,F'$ 都扩大为正交和

$$
U\perp P_1\perp\cdots\perp P_s\quad\text{和}\quad\sigma U\perp P'_1\perp\cdots\perp P'_s,
$$

它们对应于 $F_0$ 中选取的一组基及其在 $F'_0$ 中的像。因此，可以将 $\sigma$ 延拓为这两个扩大的非退化空间之间的等距同构。这样就得到了所需的归结。

假设 $F,F'$ 非退化，分步进行证明。

先假设 $F'=F$，即 $\sigma$ 是 $F$ 到自身的等距同构。只需让 $F^\perp$ 的每个元素都保持不动，就能把 $\sigma$ 延拓到 $E$。

其次，假设 $\dim F=\dim F'=1$，且 $F\ne F'$。设 $F=(v)$，$F'=(v')$。那么 $v^2=v'^2$。此外，$(v,v')$ 的维数为 $2$。

若 $(v,v')$ 非退化，则它有一个延拓 $\sigma$ 的等距同构，将 $v$ 映到 $v'$，将 $v'$ 映到 $v$。应用上一步即可完成证明。

若 $(v,v')$ 退化，则其核的维数为 $1$。设 $w$ 为该核的一组基。存在 $a,b\in k$，使 $v'=av+bw$。那么 $v'^2=a^2v^2$，故 $a=\pm1$。必要时将 $v'$ 换成 $-v'$，可以假设 $a=1$。将 $w$ 换成 $bw$，可以假设 $v'=v+w$。令 $z=v+v'$。将引理10.1应用于空间

$$
(w,z)=(w)\perp(z).
$$

可以找到元素 $y\in E$，使

$$
y\cdot z=0,\qquad y^2=0,\quad\text{且}\quad w\cdot y=1.
$$

<span class="original-page-anchor" id="pdf-page-601" aria-hidden="true"></span>

空间 $(z,w,y)=(z)\perp(w,y)$ 非退化，因为它是 $(z)$ 与双曲平面 $(w,y)$ 的正交和。它有一个等距同构，满足

$$
z\mapsto z,\qquad w\mapsto-w,\qquad y\mapsto-y.
$$

而 $v=\frac12(z-w)$ 在这个等距同构下映到 $v'=\frac12(z+w)$。当前情形已经解决。

用归纳法完成证明。由正交基的存在性（定理3.1），每个维数 $>1$ 的子空间 $F$ 都有一个正交分解，分解为维数更小的子空间的和。设 $F=F_1\perp F_2$，其中 $\dim F_1$ 和 $\dim F_2\geqq1$。那么

$$
\sigma F=\sigma F_1\perp\sigma F_2.
$$

设 $\sigma_1=\sigma|F_1$ 为 $\sigma$ 在 $F_1$ 上的限制。由归纳假设，可将 $\sigma_1$ 延拓为等距同构

$$
\bar\sigma_1:E\to E.
$$

于是 $\bar\sigma_1(F_1^\perp)=(\sigma_1F_1)^\perp$。由于 $\sigma F_2$ 与 $\sigma F_1=\sigma_1F_1$ 垂直，$\sigma F_2$ 包含在 $\bar\sigma_1(F_1^\perp)$ 中。令 $\sigma_2=\sigma|F_2$。那么由归纳假设，等距同构

$$
\sigma_2:F_2\to\sigma_2F_2=\sigma F_2
$$

可延拓为等距同构

$$
\bar\sigma_2:F_1^\perp\to\bar\sigma_1(F_1^\perp).
$$

映射对 $(\sigma_1,\bar\sigma_2)$ 给出 $F_1\perp F_1^\perp=E$ 到自身的等距同构，正是所需结论。

**推论10.3。** *设 $E,E'$ 为带有非退化对称型的有限维向量空间，并假设它们等距同构。设 $F,F'$ 为子空间，$\sigma:F\to F'$ 为等距同构。那么 $\sigma$ 可以延拓为 $E$ 到 $E'$ 的等距同构。*

*证明。* 显然。

设 $E$ 为带有对称型 $g$ 的空间，$F$ 为全零子空间。那么由引理10.1，可将 $F$ 嵌入一个双曲子空间 $H$，其维数为 $2\dim F$。

> **译校注（引用条件）：** 原书本句写“a space with a symmetric form”，但所引用的引理10.1明确假设环境空间的型非退化。本句应在该前提下使用；若允许任意退化型，例如非零空间上的零型，则非零全零子空间无法在其中嵌入非退化的双曲子空间。原句保留，这里仅明确引用引理时需要沿用的条件。

应用定理10.2，得到若干推论。

**推论10.4。** *设 $E$ 为带有非退化对称型的有限维向量空间。设 $W$ 为极大全零子空间，$W'$ 为某个全零子空间。那么 $\dim W'\leqq\dim W$，且 $W'$ 包含在某个极大全零子空间中，后者的维数与 $\dim W$ 相同。*

<span class="original-page-anchor" id="pdf-page-602" aria-hidden="true"></span>

*证明。* 由佐恩引理，$W'$ 包含在一个极大全零子空间中。假设 $\dim W'\geqq\dim W$。存在 $W$ 到 $W'$ 的某个子空间的等距同构，可以将其延拓为 $E$ 到自身的等距同构。于是 $\sigma^{-1}(W')$ 为包含 $W$ 的全零子空间，故等于 $W$，因而 $\dim W=\dim W'$。由对称性得到各个断言。

设 $E$ 为带有非退化对称型的向量空间。设 $W$ 为全零子空间。由引理10.1，可将 $W$ 嵌入 $E$ 的一个双曲子空间 $H$，使 $W$ 为 $H$ 的极大全零子空间，且 $H$ 非退化。这样的 $H$ 称为 $W$ 的**双曲扩大**。

**推论10.5。** *设 $E$ 为带有非退化对称型的有限维向量空间。设 $W,W'$ 为极大全零子空间。设 $H,H'$ 分别为 $W,W'$ 的双曲扩大。那么 $H,H'$ 等距同构，$H^\perp,H'^\perp$ 也等距同构。*

*证明。* 显然存在 $H$ 到 $H'$ 的等距同构，可以将其延拓为 $E$ 到自身的等距同构。该等距同构将 $H^\perp$ 映到 $H'^\perp$，正是所需结论。

**推论10.6。** *设 $g_1,g_2,h$ 为域 $k$ 上有限维向量空间上的对称型。若 $g_1\oplus h$ 与 $g_2\oplus h$ 等距同构，且 $g_1,g_2$ 非退化，则 $g_1$ 与 $g_2$ 等距同构。*

*证明。* 设 $g_1$ 为 $E_1$ 上的型，$g_2$ 为 $E_2$ 上的型，$h$ 为 $F$ 上的型。那么 $F\oplus E_1$ 与 $F\oplus E_2$ 之间存在等距同构。由推论10.3，将恒等映射 $\operatorname{id}:F\to F$ 延拓为 $F\oplus E_1$ 到 $F\oplus E_2$ 的等距同构 $\sigma$。由于 $E_1,E_2$ 分别为 $F$ 在这两个空间中的正交补，必有 $\sigma(E_1)=E_2$，这证明了所需结论。

> **译校注（证明条件）：** 推论10.6只要求 $g_1,g_2$ 非退化，而原证明直接引用的推论10.3还要求整个环境空间非退化。若 $h$ 退化，则在 $F\oplus E_i$ 中实际有 $F^\perp=\operatorname{rad}h\oplus E_i$，并非原句所说的 $E_i$。这种情形可先把两边除以其根基 $\operatorname{rad}h$：给定等距同构诱导非退化空间 $(F/\operatorname{rad}h)\oplus E_1$ 与 $(F/\operatorname{rad}h)\oplus E_2$ 的等距同构，再对 $F/\operatorname{rad}h$ 的恒等映射使用推论10.3，就得到 $E_1,E_2$ 等距同构。这里保留原证明，明确处理退化 $h$ 时需先完成的步骤。

若 $g$ 为 $E$ 上的对称型，并且对任意 $x\in E$、$x\ne0$ 都有 $g(x,x)\ne0$（即 $x\ne0$ 时 $x^2\ne0$），则称 $g$ 为**定型**。

**推论10.7。** *设 $g$ 为 $E$ 上的对称型。那么 $g$ 有正交和分解*

$$
g=g_0\oplus g_{\mathrm{hyp}}\oplus g_{\mathrm{def}},
$$

*其中 $g_0$ 为零型，$g_{\mathrm{hyp}}$ 为双曲型，$g_{\mathrm{def}}$ 为定型。型 $g_{\mathrm{hyp}}\oplus g_{\mathrm{def}}$ 非退化。型 $g_0,g_{\mathrm{hyp}},g_{\mathrm{def}}$ 在等距同构意义下唯一确定。*

*证明。* 分解 $g=g_0\oplus g_1$，其中 $g_0$ 为零型，$g_1$ 非退化，在等距同构意义下唯一，因为 $g_0$ 对应于 $g$ 的核。

因此可以假设 $g$ 非退化。若

$$
g=g_h\oplus g_d,
$$

<span class="original-page-anchor" id="pdf-page-603" aria-hidden="true"></span>

其中 $g_h$ 为双曲型，$g_d$ 为定型，则 $g_h$ 对应于某个极大全零子空间的双曲扩大，由推论10.5可得 $g_h$ 唯一确定。因此，$g_d$ 作为 $g_h$ 的正交补也唯一确定。（所谓唯一确定，当然是指在等距同构意义下。）

把 $g_{\mathrm{hyp}}$ 简记为 $g_h$，把 $g_{\mathrm{def}}$ 简记为 $g_d$。

## §11. 维特群

设 $g,\varphi$ 为 $k$ 上有限维向量空间上的对称型。若 $g_d$ 与 $\varphi_d$ 等距同构，则称它们**等价**。读者可立即验证，这是等价关系。此外，两个零型的（正交）和为零型，两个双曲型的和为双曲型。不过，两个定型的和未必为定型。将等价关系写作 $g\sim\varphi$。正交和保持等价关系，因此对称型的等价类构成幺半群。

**定理11.1。** *对称型（在域 $k$ 上）的等价类构成的幺半群是一个群。*

*证明。* 只需证明每个元素都有加法逆元。设 $g$ 为对称型，可以假设它是定型。定义型 $-g$，使 $(-g)(x,y)=-g(x,y)$。我们断言 $g\oplus-g$ 与 $0$ 等价。设 $E$ 为 $g$ 的定义空间。那么 $g\oplus-g$ 定义在 $E\oplus E$ 上。设 $W$ 为由所有 $(x,x)$、$x\in E$ 构成的子空间。那么 $W$ 是 $g\oplus-g$ 的全零子空间。由于 $\dim(E\oplus E)=2\dim W$，$W$ 为极大全零子空间，且 $g\oplus-g$ 为双曲型，证明完毕。

定理11.1中的群称为 $k$ 的**维特群**，记作 $W(k)$。在研究用 $g$ 所产生的二次型 $f$［即 $f(x)=g(x,x)$］表示 $k$ 的元素时，这个群很重要，例如对定的二次型 $f$ 进行分类时。

现在定义另一个群，它对于从函子的角度进一步研究对称型很重要，例如研究拓扑中由流形产生的二次型。

注意，非退化对称型（在 $k$ 上）的等距同构类构成幺半群 $M(k)$，其合成律为正交和。此外，消去律成立（推论10.6）。令

$$
\operatorname{cl}:M(k)\to WG(k)
$$

<span class="original-page-anchor" id="pdf-page-604" aria-hidden="true"></span>

为 $M(k)$ 到该幺半群的格罗滕迪克群的典范映射，称后者为 $k$ 上的**维特—格罗滕迪克群**。我们知道，消去律蕴含 $\operatorname{cl}$ 为单射。

若 $g$ 为 $k$ 上的非退化对称型，定义其维数 $\dim g$ 为其定义空间 $E$ 的维数。显然，

$$
\dim(g\oplus g')=\dim g+\dim g'.
$$

因此 $\dim$ 通过同态

$$
\dim:WG(k)\to\mathbf Z
$$

分解。由于存在一维的非退化对称型，该同态分裂。

设 $WG_0(k)$ 为同态 $\dim$ 的核。若 $g$ 为非退化对称型，可以定义其行列式 $\det(g)$ 为关于某组基表示 $g$ 的矩阵 $G$ 的行列式，模去平方。这作为 $k^*/k^{*2}$ 的元素是良定义的。定义零维型的行列式为 $1$。于是行列式为同态

$$
\det:M(k)\to k^*/k^{*2},
$$

因而可以通过维特—格罗滕迪克群的同态 $\det:WG(k)\to k^*/k^{*2}$ 分解，后者仍记作 $\det$。

维特—格罗滕迪克群的其他性质将在习题中给出。

## 习题

**1.** (a) 设 $E$ 为复数域上的有限维空间，设

$$
h:E\times E\to\mathbf C
$$

为厄米型。写

$$
h(x,y)=g(x,y)+if(x,y),
$$

其中 $g,f$ 取实数值。证明 $g,f$ 为 $\mathbf R$-双线性的，$g$ 对称，$f$ 交错。

(b) 设 $E$ 在 $\mathbf C$ 上有限维。设 $g:E\times E\to\mathbf C$ 为 $\mathbf R$-双线性的。假设对所有 $x\in E$，映射 $y\mapsto g(x,y)$ 是 $\mathbf C$-线性的，而且 $\mathbf R$-双线性型

$$
f(x,y)=g(x,y)-g(y,x)
$$

<span class="original-page-anchor" id="pdf-page-605" aria-hidden="true"></span>

在 $E\times E$ 上取实数值。证明存在 $E$ 上的厄米型 $h$ 和对称的 $\mathbf C$-双线性型 $\psi$，使 $2ig=h+\psi$。证明 $h,\psi$ 唯一确定。

> **译校注（变量约定）：** 本题原文假设“the map $y\mapsto g(x,y)$ is $\mathbf C$-linear”，并要求 $2ig=h+\psi$。本章的厄米型约定是在第一变量 $x$ 上复线性，因此右端 $h+\psi$ 在 $x$ 上复线性，而所列假设不能保证左端具有这一性质。例如取 $E=\mathbf C$、$g(x,y)=i\overline{x}y$，则 $g$ 为实双线性且在 $y$ 上复线性，$g(x,y)-g(y,x)=i(\overline{x}y-\overline{y}x)$ 取实值；但 $2ig=-2\overline{x}y$ 在 $x$ 上不是复线性的，不能等于上述 $h+\psi$。按本章约定，原题条件不足；这里保留原题，不主张给出了完整修正。

**2.** 证明酉谱定理的实数情形：若 $E$ 为 $\mathbf R$ 上的非零有限维空间，带有正定对称型，且 $U:E\to E$ 为酉线性映射，则 $E$ 可正交分解为在 $U$ 下不变的一维或二维子空间。若 $\dim E=2$，则 $U$ 关于任意标准正交基的矩阵为

$$
\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}
\quad\text{或}\quad
\begin{pmatrix}-1&0\\0&1\end{pmatrix}\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
$$

分别对应 $\det(U)=1$ 或 $-1$。因此 $U$ 为旋转，或先旋转再反射。

**3.** 设 $E$ 为实数域上的非零有限维向量空间，带有正定标量积。设 $T:E\to E$ 为 $E$ 的酉自同构。证明 $E$ 为子空间的正交和

$$
E=E_1\perp\cdots\perp E_m,
$$

其中每个 $E_i$ 都在 $T$ 下不变，且维数为 $1$ 或 $2$。若 $E$ 的维数为 $2$，证明可以找到一组基，使 $T$ 关于这组基的矩阵为

$$
\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}
\quad\text{或}\quad
\begin{pmatrix}-\cos\theta&\sin\theta\\\sin\theta&\cos\theta\end{pmatrix},
$$

分别对应 $\det T=1$ 或 $\det T=-1$。

**4.** 设 $E$ 为 $\mathbf C$ 上的非零有限维向量空间，带有正定厄米积。设 $A,B:E\to E$ 为厄米自同态。假设 $AB=BA$。证明 $E$ 有一组由 $A,B$ 的共同特征向量构成的基。

**5.** 设 $E$ 为复数域上的有限维空间，带有正定厄米型。设 $S$ 为 $E$ 的（$\mathbf C$-线性）自同态的集合，没有除 $0,E$ 以外的不变子空间。（这意味着：若 $F$ 是 $E$ 的子空间，且对所有 $B\in S$ 都有 $BF\subset F$，则 $F=0$ 或 $F=E$。）设 $A$ 为 $E$ 到自身的厄米映射，且对所有 $B\in S$ 都有 $AB=BA$。证明对某个实数 $\lambda$，有 $A=\lambda I$。［*提示：* 证明 $A$ 恰有一个特征值。若有两个特征值，设为 $\lambda_1\ne\lambda_2$，则可以找到两个实系数多项式 $f,g$，使 $f(A)\ne0$、$g(A)\ne0$，但 $f(A)g(A)=0$。取 $F$ 为 $g(A)$ 的核，导出矛盾。］

**6.** 设 $E$ 如习题5。设 $T$ 为 $E$ 到自身的 $\mathbf C$-线性映射。令

$$
A=\tfrac12(T+T^*).
$$

证明 $A$ 是厄米的。证明 $T$ 可以写成 $A+iB$ 的形式，其中 $A,B$ 都是厄米的，且唯一确定。

**7.** 设 $S$ 为 $E$ 的 $\mathbf C$-线性自同态的一个交换集合，没有除 $0,E$ 以外的不变子空间。另假设若 $B\in S$，则 $B^*\in S$。证明每个<span class="original-page-anchor" id="pdf-page-606" aria-hidden="true"></span>$S$ 的元素都形如 $\alpha I$，其中 $\alpha$ 为某个复数。［*提示：* 取 $B_0\in S$。令

$$
A=\tfrac12(B_0+B_0^*).
$$

证明 $A=\lambda I$，其中 $\lambda$ 为某个实数。］

**8.** 若 $E$ 的自同态 $B$ 与 $B^*$ 交换，则称 $B$ 为**正规**自同态。叙述并证明正规自同态的谱定理。

### 对称自同态

*对于习题9、10和11，设 $E$ 为 $\mathbf R$ 上的非零有限维向量空间，带有对称正定标量积 $g$，它在 $E$ 上产生范数 $\|\ \|$。*

设 $A:E\to E$ 为 $E$ 关于 $g$ 的对称自同态。定义 $A\geqq0$ 表示对所有 $x\in E$ 都有 $\langle Ax,x\rangle\geqq0$。

**9.** (a) 证明 $A\geqq0$ 当且仅当 $A$ 的所有属于非零特征向量的特征值都 $\geqq0$。在厄米情形和对称情形中，若 $A\geqq0$，则称 $A$ **半正定**；若对所有 $x\ne0$ 都有 $\langle Ax,x\rangle>0$，则称 $A$ **正定**。

(b) 证明 $E$ 的自同构 $A$ 可以唯一地写成乘积 $A=UP$，其中 $U$ 为实酉映射（即 ${}^tUU=I$），$P$ 对称正定。对两个厄米或对称自同态 $A,B$，定义 $A\geqq B$ 表示 $A-B\geqq0$；$A>B$ 的定义类似。假设 $A>0$。证明存在两个实数 $\alpha>0$、$\beta>0$，使 $\alpha I\leqq A\leqq\beta I$。

**10.** 若 $A$ 为 $E$ 的自同态，定义其范数 $|A|$ 为满足“对所有 $x\in E$ 都有 $|Ax|\leqq C|x|$”的所有数 $C$ 的最大下界。

(a) 证明该范数满足三角不等式。

(b) 证明级数

$$
\exp(A)=I+A+\frac{A^2}{2!}+\cdots
$$

收敛，而且若 $A$ 与 $B$ 交换，则 $\exp(A+B)=\exp(A)\exp(B)$。若 $A$ 与 $I$ 充分接近，证明级数

$$
\log(A)=\frac{(A-I)}1-\frac{(A-I)^2}2+\cdots
$$

收敛，而且若 $A$ 与 $B$ 交换，则

$$
\log(AB)=\log A+\log B.
$$

(c) 利用谱定理，说明如何对任意正定自同态 $P$ 定义 $\log P$。

**11.** 再次设 $E$ 为 $\mathbf R$ 上的非零有限维空间，带有正定对称型。设 $A:E\to E$ 为线性映射。证明：

(a) 若 $A$ 对称（或交错），则 $\exp(A)$ 对称正定（相应地，为实酉映射）。

(b) 若 $A$ 为 $E$ 的线性自同构，与 $I$ 充分接近，而且对称<span class="original-page-anchor" id="pdf-page-607" aria-hidden="true"></span>正定（或为实酉映射），则 $\log A$ 对称（相应地，交错）。

(c) 更一般地，若 $A$ 正定，则 $\log A$ 对称。

**12.** 设 $R$ 为交换环，$E,F$ 为 $R$-模，$f:E\to F$ 为映射。假设 $F$ 上乘以 $2$ 的映射可逆。证明 $f$ 为齐次二次映射当且仅当 $f$ 对所有 $x,y\in E$ 满足**平行四边形恒等式**：

$$
f(x+y)+f(x-y)=2f(x)+2f(y).
$$

> **译校注（一般基环的条件）：** 原题在任意交换环 $R$ 上断言，平行四边形恒等式与“homogeneous quadratic”等价。按本章§2中以 $R$-双线性型定义齐次二次映射的约定，恒等式本身不能保证关于所有 $a\in R$ 的齐次性 $f(ax)=a^2f(x)$。例如取 $R=E=F=\mathbf C$、$f(z)=\overline z^{\,2}$，乘以 $2$ 可逆，且该恒等式成立；但 $f(1+i)=-2i$，而 $(1+i)^2f(1)=2i$。因此对于一般 $R$，所列条件不足。这里保留原题及公式，只指出已验证的限制，不主张给出了完整修正。

**13.**（泰特）设 $E,F$ 为实数域上的完备赋范向量空间。设 $f:E\to F$ 为具有如下性质的映射：存在数 $C>0$，使对所有 $x,y\in E$ 都有

$$
|f(x+y)-f(x)-f(y)|\leqq C.
$$

证明存在唯一的加法映射 $g:E\to F$，使 $|g-f|$ 有界（即 $|g(x)-f(x)|$ 作为 $x$ 的函数有界）。推广到双线性情形。［*提示：* 令

$$
g(x)=\lim_{n\to\infty}\frac{f(2^nx)}{2^n}.
$$

］

**14.**（泰特）设 $S$ 为集合，$f:S\to S$ 为 $S$ 到自身的映射。设 $h:S\to\mathbf R$ 为实值函数。假设存在实数 $d>1$，使 $h\circ f-dh$ 有界。

**译校注：** 原书写作“$h\circ f-df$”。此处 $f:S\to S$ 未必取实数值，而 $h\circ f$ 是实值函数，不能一般地减去 $df$。后面的目标等式为 $h_f\circ f=dh_f$，提示中的极限也对 $h$ 作归一化，故这里应为 $h\circ f-dh$。

证明存在唯一的函数 $h_f$，使 $h_f-h$ 有界，且 $h_f\circ f=dh_f$。［*提示：* 令 $h_f(x)=\lim h(f^n(x))/d^n$。］

**15.** 定义从一个模到另一个模的次数 $>2$ 的映射。［*提示：* 对次数 $3$，考虑表达式

$$
f(x+y+z)-f(x+y)-f(x+z)-f(y+z)+f(x)+f(y)+f(z).
$$

］

将已对二次映射证明的断言推广到这些更高次的映射，即其定义中出现的各种多重线性映射的唯一性。

### 交错型

**16.** 设 $E$ 为域 $k$ 上的向量空间，$g$ 为 $E$ 上的双线性型。假设只要 $x,y\in E$ 满足 $g(x,y)=0$，就有 $g(y,x)=0$。证明 $g$ 对称或交错。

**17.** 设 $E$ 为 $\mathbf Z$ 上的模。假设 $E$ 自由，维数为 $n\geqq1$，设 $f$ 为 $E$ 上的双线性交错型。证明存在一组基 $\{e_i\}$ $(i=1,\ldots,n)$ 和整数 $r$，使 $2r\leqq n$，且

$$
e_1\cdot e_2=a_1,\quad e_3\cdot e_4=a_2,\ldots,e_{2r-1}\cdot e_{2r}=a_r,
$$

其中 $a_1,\ldots,a_r\in\mathbf Z$，$a_i\ne0$，$a_i$ 在 $i=1,\ldots,r-1$ 时整除 $a_{i+1}$；最后，对所有其他指标对 $i\leqq j$，都有 $e_i\cdot e_j=0$。证明理想 $\mathbf Za_i$ 唯一确定。［*提示：* 考虑同态 $\varphi_f:E\to E^\vee$，它把 $E$ 映到其<span class="original-page-anchor" id="pdf-page-608" aria-hidden="true"></span>在 $\mathbf Z$ 上的对偶空间，并把 $\varphi_f(E)$ 看作 $E^\vee$ 的自由子模。］在知道主理想整环上模的基定理后，将此结论推广到主理想整环。

**译校注：** 原书在本提示开头称 $\varphi_f:E\to E^\vee$ 为“injective homomorphism”（单同态），但本题没有假设型 $f$ 非退化。例如 $f=0$ 时，该同态为零映射，而 $E$ 的秩至少为 $1$，因此并非单射。一般情形应考虑该同态及其像 $\varphi_f(E)$，不能一概称它为单同态。

**评述。** 习题18中的那种基称为**辛基**。关于这种基的一种应用，参见 theta 函数理论，例如拙著《Introduction to Algebraic and Abelian Functions》（第二版，Springer Verlag）第六章第3节。

**18.** 设 $E$ 为实数域上的有限维向量空间，$\langle\ ,\ \rangle$ 为对称正定型。设 $\Omega$ 为 $E$ 上的非退化交错型。证明存在直和分解

$$
E=E_1\oplus E_2,
$$

具有以下性质：若 $x,y\in E$ 写成

$$
\begin{aligned}
x&=(x_1,x_2),\quad x_1\in E_1,\quad x_2\in E_2,\\
y&=(y_1,y_2),\quad y_1\in E_1,\quad y_2\in E_2,
\end{aligned}
$$

则 $\Omega(x,y)=\langle x_1,y_2\rangle-\langle x_2,y_1\rangle$。［*提示：* 使用推论8.3，证明 $A$ 正定，并取其平方根，以变换该推论中得到的直和分解。］

**19.** 证明当 $n$ 为奇数时，交错 $n\times n$ 矩阵的普法夫式为 $0$。

**20.** 证明阿廷《Geometric Algebra》（Interscience，1957）第142页陈述的普法夫式的所有性质。

### 维特群

**21.** 明确说明 $W(k)$ 如何成为 $WG(k)$ 的同态像。

**22.** 证明 $WG(k)$ 可以表示为 $\mathbf Z[k^*/k^{*2}]$ 的同态像。［*提示：* 使用正交基的存在性。］

**23.** 维特定理对交错型仍然成立。证明它，或在阿廷的书中查阅（参考书见习题20）。

### $SL_n(\mathbf R)$

线性代数群构成整个研究领域，产生了广泛的代数理论，也使在这些群上进行傅里叶分析成为可能。群 $SL_n(\mathbf R)$（或 $SL_n(\mathbf C)$）可以作为原型，而且容易验证若干基本事实。下面把其中一些列为习题。想看解答的读者可查阅[JoL 01]，《Spherical Inversion on $SL_n(\mathbf R)$》第一章。

**24. 岩泽分解。** 从 $GL_n(\mathbf R)$ 开始。令：

$G=GL_n(\mathbf R)$；

$K=$ 实酉 $n\times n$ 矩阵的子群；

$U=$ 实幺幂上三角矩阵群，即对角元为 $1$、对角线上方的元素任意、对角线下方的元素为 $0$ 的矩阵群；

<span class="original-page-anchor" id="pdf-page-609" aria-hidden="true"></span>

$A=$ **对角元为正的对角矩阵群。**

**证明乘积映射 $U\times A\times K\to UAK\subset G$ 实际上是双射。这相当于格拉姆—施密特正交化。证明复数情形中的类似结论，即 $G(\mathbf C)=GL_n(\mathbf C)$，$K(\mathbf C)=$ 复酉群，$U(\mathbf C)=$ 复幺幂上三角群，而 $A$ 与实数情形中的正对角矩阵群相同。**

**25.** 现在令 $G=SL_n(\mathbf R)$，令 $K,A$ 为相应的行列式为 $1$ 的子群。证明乘积 $U\times A\times K\to UAK$ 再次给出到 $G$ 的双射。

**26.** 设 $\mathfrak a$ 为迹为 $0$ 的实对角矩阵构成的 $\mathbf R$-向量空间。设 $\mathfrak a^\vee$ 为对偶空间。设 $\alpha_i$ $(i=1,\ldots,n-1)$ 为以 $\alpha_i(H)=h_i-h_{i+1}$ 定义在元素 $H=\operatorname{diag}(h_1,\ldots,h_n)$ 上的泛函。(a) 证明 $\{\alpha_1,\ldots,\alpha_{n-1}\}$ 为 $\mathfrak a^\vee$ 在 $\mathbf R$ 上的一组基。(b) 设 $H_{i,i+1}$ 为对角矩阵，其 $h_i=1$、$h_{i+1}=-1$，且 $j\ne i,i+1$ 时 $h_j=0$。证明 $\{H_{1,2},\ldots,H_{n-1,n}\}$ 为 $\mathfrak a$ 的一组基。(c) 简记 $H_{i,i+1}=H_i$ $(i=1,\ldots,n-1)$。设 $\alpha'_i\in\mathfrak a^\vee$ 为满足 $\alpha'_i(H_j)=\delta_{ij}$（$i=j$ 时为 $1$，否则为 $0$）的泛函。因此 $\{\alpha'_1,\ldots,\alpha'_{n-1}\}$ 为 $\{H_1,\ldots,H_{n-1}\}$ 的对偶基。证明

$$
\alpha'_i(H)=h_1+\cdots+h_i.
$$

**27. 迹型。** **设 $\operatorname{Mat}_n(\mathbf R)$ 为实 $n\times n$ 矩阵构成的向量空间。在这个空间上定义扭曲迹型为**

$$
B_t(X,Y)=\operatorname{tr}(X\,{}^tY)=\langle X,Y\rangle_t.
$$

**照例，${}^tY$ 为矩阵 $Y$ 的转置。证明 $B_t$ 为 $\operatorname{Mat}_n(\mathbf R)$ 上的对称正定双线性型。$\operatorname{Mat}_n(\mathbf C)$ 上相应的正定厄米型是什么？**

**28. 正性。** **在 $\mathfrak a$（迹为 $0$ 的实对角矩阵）上，习题27中的型可以定义为 $\operatorname{tr}(XY)$，因为元素 $X,Y\in\mathfrak a$ 是对称的。设 $\mathcal A=\{\alpha_1,\ldots,\alpha_{n-1}\}$ 为习题26中的基。若对所有 $i=1,\ldots,n-1$ 都有 $\alpha_i(H)\geqq0$，则称元素 $H\in\mathfrak a$ 半正（记作 $H\geqq0$）。对每个 $\alpha\in\mathfrak a^\vee$，设 $H_\alpha\in\mathfrak a$ 关于 $B_t$ 表示 $\alpha$，即对所有 $H\in\mathfrak a$ 都有 $\langle H_\alpha,H\rangle=\alpha(H)$。**

**证明 $H\geqq0$ 当且仅当**

$$
H=\sum_{i=1}^{n-1}s_iH_{\alpha'_i},\quad s_i\geqq0.
$$

**类似地，定义 $H$ 为正，并写出 $s_i>0$ 时的相应条件。**

**29.** 证明元素 $n\alpha'_i$ $(i=1,\ldots,n-1)$ 可以表示为 $\alpha_1,\ldots,\alpha_{n-1}$ 的线性组合，其系数为 $\mathbf Z$ 中的正数。

**30.** 设 $W$ 为对角矩阵向量空间 $\mathfrak a$ 中的对角元的置换群。证明 $\mathfrak a_{\geqq0}$ 是 $W$ 在 $\mathfrak a$ 上作用的基本域（即给定 $H\in\mathfrak a$，存在唯一的 $H^+\geqq0$，使 $H^+=wH$ 对某个 $w\in W$ 成立）。
