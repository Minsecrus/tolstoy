---
title: "第五章 有限群的表示：进一步的结果"
description: "《Introduction to Representation Theory》中文译文。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"第四章 有限群的表示：基本结果","link":"/library/volume-88/chapter-004"}
next: {"text":"第六章 箭图表示","link":"/library/volume-88/chapter-006"}
---

# 第五章 有限群的表示：进一步的结果

<span class="original-page-anchor" id="pdf-page-99" aria-hidden="true"></span>

## 5.1. Frobenius–Schur 指标

设 $G$ 为有限群，$V$ 为 $G$ 在 $\mathbb C$ 上的不可约表示。

**定义 5.1.1.** 我们称 $V$ 为

- 复型，如果 $V\not\cong V^*$；
- 实型，如果 $V$ 上有一个 $G$ 不变的非退化对称型；
- 四元数型，如果 $V$ 上有一个 $G$ 不变的非退化斜对称型。

**习题 5.1.2.** (a) 证明：若 $V$ 为复型，则 $\operatorname{End}_{\mathbb R[G]}V$ 为 $\mathbb C$；若 $V$ 为实型，则为 $\operatorname{Mat}_2(\mathbb R)$；若 $V$ 为四元数型，则为 $\mathbb H$。这也解释了上述名称的由来。

提示：证明 $V$ 的复化 $V_{\mathbb C}$ 分解为 $V\oplus V^*$，并由此分别计算三种情形下 $\operatorname{End}_{\mathbb R[G]}V$ 的维数。利用 $\mathbb C\subset\operatorname{End}_{\mathbb R[G]}V$，证明复型情形的结论。在另外两种情形中，令 $B$ 为 $V$ 上的不变双线性型，$(\ ,\ )$ 为不变的正定 Hermitian 型（它们分别在相差一个非零复数倍和一个正<span class="original-page-anchor" id="pdf-page-100" aria-hidden="true"></span>实数倍的意义下唯一确定）。定义算子 $j:V\to V$，使 $B(v,w)=(v,jw)$。证明 $j$ 是复反线性的（$ji=-ij$），且 $j^2=\lambda\cdot\operatorname{Id}$，其中 $\lambda$ 为实数，在实型情形下为正，在四元数型情形下为负（如果重新归一化 $B$，则 $j$ 乘上某个非零复数 $z$；由于 $j$ 是反线性的，$j^2$ 就乘上 $z\bar z$）。因此可以将 $j$ 归一化，使实型情形下 $j^2=1$，四元数型情形下 $j^2=-1$。由此推出所需结论。

(b) 证明 $V$ 为实型，当且仅当它是实数域上某个表示 $V_{\mathbb R}$ 的复化。

**例 5.1.3.** 对 $\mathbb Z/n\mathbb Z$，除平凡表示以及 $n$ 为偶数时的“符号”表示 $m\to(-1)^m$ 是实型外，其余不可约表示都是复型。对 $S_3$，三个不可约表示 $\mathbb C_+,\mathbb C_-,\mathbb C^2$ 都是实型。$S_4$ 的五个不可约表示 $\mathbb C_+,\mathbb C_-,\mathbb C^2,\mathbb C_+^3,\mathbb C_-^3$ 也都是实型。同样，$A_5$ 的五个不可约表示 $\mathbb C,\mathbb C_+^3,\mathbb C_-^3,\mathbb C^4,\mathbb C^5$ 全部是实型。至于 $Q_8$，它的一维表示都是实型，二维表示则是四元数型。

**定义 5.1.4.** 不可约表示 $V$ 的 **Frobenius–Schur 指标** $FS(V)$ 定义如下：若 $V$ 为复型，则为 $0$；若为实型，则为 $1$；若为四元数型，则为 $-1$。

**定理 5.1.5（Frobenius–Schur）.** $G$ 中对合（即阶不超过 $2$ 的元素）的个数等于 $\sum_V\dim(V)FS(V)$，也就是 $G$ 的所有实型表示的维数之和，减去其四元数型表示的维数之和。

**证明.** 设 $A:V\to V$ 的特征值为 $\lambda_1,\lambda_2,\ldots,\lambda_n$。有

$$
\operatorname{Tr}|_{S^2V}(A\otimes A)=\sum_{i\le j}\lambda_i\lambda_j,
$$

$$
\operatorname{Tr}|_{\Lambda^2V}(A\otimes A)=\sum_{i<j}\lambda_i\lambda_j.
$$

因此，

$$
\operatorname{Tr}|_{S^2V}(A\otimes A)-\operatorname{Tr}|_{\Lambda^2V}(A\otimes A)=\sum_{1\le i\le n}\lambda_i^2=\operatorname{Tr}(A^2).
$$

<span class="original-page-anchor" id="pdf-page-101" aria-hidden="true"></span>

因此，对 $g\in G$，有

$$
\chi_V(g^2)=\chi_{S^2V}(g)-\chi_{\Lambda^2V}(g).
$$

令 $P=|G|^{-1}\sum_{g\in G}g$，就得到

$$
\begin{aligned}
|G|^{-1}\chi_V\left(\sum_{g\in G}g^2\right)
&=\chi_{S^2V}(P)-\chi_{\Lambda^2V}(P)\\
&=\dim(S^2V)^G-\dim(\Lambda^2V)^G\\
&=\begin{cases}
1&\text{若 }V\text{ 为实型},\\
-1&\text{若 }V\text{ 为四元数型},\\
0&\text{若 }V\text{ 为复型}.
\end{cases}
\end{aligned}
$$

最后，$G$ 中对合的个数等于

$$
\frac1{|G|}\sum_V\dim V\chi_V\left(\sum_{g\in G}g^2\right)=\sum_{V\text{ 为实型}}\dim V-\sum_{V\text{ 为四元数型}}\dim V.
$$

$\square$

**推论 5.1.6.** 假设有限群 $G$ 的所有表示都可以定义在实数域上（即 $G$ 的所有复表示都是实表示复化得到的）。那么，$G$ 的所有不可约表示的维数之和，等于 $G$ 中对合的个数。

**练习 5.1.7.** 证明任何非平凡的奇数阶有限群，都有一个不能定义在 $\mathbb R$ 上的不可约表示（即不能用实矩阵实现的表示）。

## 5.2. 代数数与代数整数

下面我们转向有限群表示论中更深入的结果。这些结果需要用到代数数理论，我们先作简要回顾。

**定义 5.2.1.** 若 $z\in\mathbb C$ 是某个有理系数首一多项式的根，则称 $z$ 为**代数数**；若是某个整数系数首一多项式的根，则称为**代数整数**。

**定义 5.2.2.** 若 $z\in\mathbb C$ 是某个有理数矩阵的特征值，则称 $z$ 为**代数数**；若是某个整数矩阵的特征值，则称为**代数整数**。

<span class="original-page-anchor" id="pdf-page-102" aria-hidden="true"></span>

**命题 5.2.3.** 定义 5.2.1 与定义 5.2.2 等价。

**证明.** 要说明定义 5.2.2 的条件蕴含定义 5.2.1 的条件，只需注意，$z$ 是该矩阵的特征多项式的根；这是一个有理系数（相应地，整数系数）首一多项式。反过来，假设 $z$ 是

$$
p(x)=x^n+a_1x^{n-1}+\cdots+a_{n-1}x+a_n
$$

的根。下面这个矩阵（称为**相伴矩阵**）的特征多项式就是 $p(x)$：

$$
\begin{pmatrix}
0&0&0&\cdots&0&-a_n\\
1&0&0&\cdots&0&-a_{n-1}\\
0&1&0&\cdots&0&-a_{n-2}\\
\vdots&\vdots&\ddots&\ddots&\vdots&\vdots\\
0&0&0&\cdots&1&-a_1
\end{pmatrix}.
$$

由于 $z$ 是这个矩阵的特征多项式的根，它也就是这个矩阵的特征值。$\square$

代数数的集合记为 $\overline{\mathbb Q}$，代数整数的集合记为 $\mathbb A$。

**命题 5.2.4.** (i) $\mathbb A$ 是环。

(ii) $\overline{\mathbb Q}$ 是域；具体来说，它是有理数域的一个代数闭包。

**证明.** 我们使用定义 5.2.2。设 $\alpha$ 是

$$
A\in\operatorname{Mat}_n(\mathbb C)
$$

的特征值，对应特征向量 $v$；设 $\beta$ 是

$$
B\in\operatorname{Mat}_m(\mathbb C)
$$

的特征值，对应特征向量 $w$。那么 $\alpha\pm\beta$ 是

$$
A\otimes\operatorname{Id}_m\pm\operatorname{Id}_n\otimes B
$$

的特征值，<span class="original-page-anchor" id="pdf-page-103" aria-hidden="true"></span>而 $\alpha\beta$ 是

$$
A\otimes B
$$

的特征值。两种情形下，相应的特征向量都是 $v\otimes w$。这说明 $\mathbb A$ 和 $\overline{\mathbb Q}$ 都是环。要说明后者是域，只需注意：若 $\alpha\ne0$ 是 $d$ 次多项式 $p(x)$ 的根，那么 $\alpha^{-1}$ 就是 $x^dp(1/x)$ 的根。最后一个断言也容易得到，因为一个数 $\alpha$ 是代数数，当且仅当它给出 $\mathbb Q$ 的有限扩张。$\square$

**命题 5.2.5.** $\mathbb A\cap\mathbb Q=\mathbb Z$。

**证明.** 我们使用定义 5.2.1。设 $z$ 是

$$
p(x)=x^n+a_1x^{n-1}+\cdots+a_{n-1}x+a_n
$$

的根，并设

$$
z=\frac pq\in\mathbb Q,\qquad\gcd(p,q)=1.
$$

注意，$p(z)$ 的首项的分母为 $q^n$，而其余各项分母中 $q$ 的幂次都更低。**译校注：**此处原书写作 $p(x)$，据作者官方勘误改为 $p(z)$，因为这里是在代入 $z=p/q$ 后比较各项的分母。因此，如果 $q\ne\pm1$，就有 $p(z)\notin\mathbb Z$，矛盾。于是 $z\in\mathbb A\cap\mathbb Q\Rightarrow z\in\mathbb Z$。反向包含关系成立，是因为每个 $n\in\mathbb Z$ 都是 $x-n$ 的根。$\square$

每个代数数 $\alpha$ 都有一个**最小多项式** $p(x)$，即满足 $p(\alpha)=0$ 的次数最小的有理系数首一多项式。任何满足 $q(\alpha)=0$ 的其他有理系数多项式 $q(x)$ 都被 $p(x)$ 整除。$p(x)$ 的根称为 $\alpha$ 的**代数共轭**；它们也是任何满足 $q(\alpha)=0$ 的有理系数多项式 $q$ 的根。

显然，代数整数的任意代数共轭仍是代数整数。因此，由 Vieta 定理可知，代数整数的最小多项式具有整数系数。

下面需要用到这个引理。

**引理 5.2.6.** 若 $\alpha_1,\ldots,\alpha_m$ 为代数数，则 $\alpha_1+\cdots+\alpha_m$ 的所有代数共轭都具有 $\alpha'_1+\cdots+\alpha'_m$ 的形式，其中 $\alpha'_i$ 是 $\alpha_i$ 的某个代数共轭。

**证明.** 只需对两个加数证明。设 $\alpha_i$ 为最小阶数的有理数矩阵 $A_i$ 的特征值（即这些矩阵的特征<span class="original-page-anchor" id="pdf-page-104" aria-hidden="true"></span>多项式就是 $\alpha_i$ 的最小多项式），则 $\alpha_1+\alpha_2$ 是 $A:=A_1\otimes\operatorname{Id}+\operatorname{Id}\otimes A_2$ 的特征值。因此，$\alpha_1+\alpha_2$ 的每个代数共轭也都是 $A$ 的特征值。而 $A$ 的所有特征值都具有 $\alpha'_1+\alpha'_2$ 的形式，证明完毕。$\square$

**习题 5.2.7.** (a) 证明对任意有限群 $G$，都存在 $\mathbb Q$ 的有限 Galois 扩张 $K\subset\mathbb C$，使得 $G$ 的每个有限维复表示都可以选取一组基，在这组基下，各个群元素的矩阵的元素都属于 $K$。

提示：考虑 $G$ 在代数数域 $\overline{\mathbb Q}$ 上的表示。

(b) 证明若 $V$ 为有限群 $G$ 的维数大于 $1$ 的不可约复表示，则存在 $g\in G$，使得 $\chi_V(g)=0$。

提示：假设结论不成立。利用特征标的标准正交性，证明所有 $g\ne1$ 对应的数 $|\chi_V(g)|^2$ 的算术平均值小于 $1$。由此推出，这些数的乘积 $\beta$ 满足 $0<\beta<1$。证明 $\beta$ 的所有共轭也满足同样的不等式（考虑表示 $V$ 的 Galois 共轭，即让 $K$ 在 $\mathbb Q$ 上的 Galois 群作用于 (a) 中那组基下各群元素的矩阵而得到的表示）。然后推出矛盾。

**注 5.2.8.** 上述论证可以稍作修改，从而不使用 (a)。令 $N=|G|$。对任意与 $N$ 互素且满足 $0<j<N$ 的 $j$，证明映射 $g\mapsto g^j$ 是 $G\to G$ 的双射。由此推出 $\prod_{g\ne1}|\chi_V(g^j)|^2=\beta$。再证明 $\beta\in K:=\mathbb Q(\zeta)$，其中 $\zeta=e^{2\pi i/N}$，且 $\beta$ 在由 $\zeta\mapsto\zeta^j$ 给出的 $K$ 的自同构下不变。由此推出 $\beta$ 为整数，进而得到矛盾。

## 5.3. Frobenius 整除性

**定理 5.3.1.** 设 $G$ 为有限群，$V$ 为 $G$ 在 $\mathbb C$ 上的不可约表示，则

$$
\dim V\mid |G|.
$$

<span class="original-page-anchor" id="pdf-page-105" aria-hidden="true"></span>

**证明.** 设 $C_1,C_2,\ldots,C_n$ 为 $G$ 的共轭类，$g_{C_i}$ 为 $C_i$ 的代表。令

$$
\lambda_i=\chi_V(g_{C_i})\frac{|C_i|}{\dim V}.
$$

**命题 5.3.2.** 对所有 $i$，$\lambda_i$ 都是代数整数。

**证明.** 设 $C$ 为 $G$ 的一个共轭类，令 $P=\sum_{h\in C}h$。$P$ 是 $\mathbb Z[G]$ 的中心元素，因而在 $V$ 上以某个标量 $\lambda$ 作用，而且 $\lambda$ 是代数整数。事实上，由于 $\mathbb Z[G]$ 是有限生成的 $\mathbb Z$-模，$\mathbb Z[G]$ 的任意元素都在 $\mathbb Z$ 上整，即满足某个整数系数首一多项式方程。另一方面，在 $V$ 中对 $P$ 取迹，得到 $|C|\chi_V(g)=\lambda\dim V$，其中 $g\in C$，所以 $\lambda=\frac{|C|\chi_V(g)}{\dim V}$。$\square$

现在考虑

$$
\sum_i\lambda_i\overline{\chi_V(g_{C_i})}.
$$

这是代数整数，因为：

(i) 由命题 5.3.2，$\lambda_i$ 都是代数整数；

(ii) $\chi_V(g_{C_i})$ 是单位根之和（它是 $\rho(g_{C_i})$ 的矩阵的特征值之和；由于在 $G$ 中有 $g_{C_i}^{|G|}=e$，$\rho(g_{C_i})$ 的特征值都是单位根）；

(iii) $\mathbb A$ 是环（命题 5.2.4）。

另一方面，由 $\lambda_i$ 的定义，

$$
\sum_{C_i}\lambda_i\overline{\chi_V(g_{C_i})}=\sum_i\frac{|C_i|\chi_V(g_{C_i})\overline{\chi_V(g_{C_i})}}{\dim V}.
$$

由于 $\chi_V$ 是类函数，这又等于

$$
\sum_{g\in G}\frac{\chi_V(g)\overline{\chi_V(g)}}{\dim V}=\frac{|G|(\chi_V,\chi_V)}{\dim V}.
$$

$V$ 是不可约表示，所以 $(\chi_V,\chi_V)=1$，从而

$$
\sum_{C_i}\lambda_i\overline{\chi_V(g_{C_i})}=\frac{|G|}{\dim V}.
$$

<span class="original-page-anchor" id="pdf-page-106" aria-hidden="true"></span>

由于 $\frac{|G|}{\dim V}\in\mathbb Q$，且 $\sum_{C_i}\lambda_i\overline{\chi_V(g_{C_i})}\in\mathbb A$，由命题 5.2.5，$\frac{|G|}{\dim V}\in\mathbb Z$。$\square$

## 5.4. Burnside 定理

**定义 5.4.1.** 如果群 $G$ 有一列嵌套的正规子群

$$
\{e\}=G_1\triangleleft G_2\triangleleft\cdots\triangleleft G_n=G,
$$

且对所有 $1\le i\le n-1$，$G_{i+1}/G_i$ 都是阿贝尔群，那么称 $G$ **可解**。

**注 5.4.2.** 这样的群之所以称为可解群，是因为它们最初作为可用根式求解的多项式方程的 Galois 群出现。

**定理 5.4.3（Burnside）.** 任意阶为 $p^aq^b$ 的群 $G$ 都是可解群，其中 $p,q$ 为素数，$a,b\ge0$。

这个群论中的著名结果，由英国数学家 William Burnside 在二十世纪初利用表示论证明（见第 5.5 节及 [Cu]）。下面用现代语言给出他的证明。

在证明 Burnside 定理之前，我们先证明几个本身也很有意义的结果。

**定理 5.4.4.** 设 $V$ 为有限群 $G$ 的不可约表示，$C$ 为 $G$ 的一个共轭类，并且 $\gcd(|C|,\dim(V))=1$。那么，对任意 $g\in C$，或者 $\chi_V(g)=0$，或者 $g$ 在 $V$ 上以标量作用。

证明将用到下面的引理。

**引理 5.4.5.** 若 $\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n$ 为单位根，且 $\frac1n(\varepsilon_1+\varepsilon_2+\cdots+\varepsilon_n)$ 为代数整数，那么或者 $\varepsilon_1=\cdots=\varepsilon_n$，或者 $\varepsilon_1+\cdots+\varepsilon_n=0$。

**证明.** 令 $a=\frac1n(\varepsilon_1+\cdots+\varepsilon_n)$。如果 $\varepsilon_i$ 不全相等，就有 $|a|<1$。此外，单位根的任何代数共轭仍是单位根，所以 $a$ 的任意代数共轭 $a'$ 都满足 $|a'|\le1$。而 $a$ 的所有代数共轭的乘积是整数，其绝对值小于 $1$，所以只能为零。因此 $a=0$。$\square$

<span class="original-page-anchor" id="pdf-page-107" aria-hidden="true"></span>

**定理 5.4.4 的证明.** 令 $\dim V=n$。设 $\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n$ 为 $\rho_V(g)$ 的特征值。它们都是单位根，所以 $\chi_V(g)$ 是代数整数。此外，由命题 5.3.2，$\frac1n|C|\chi_V(g)$ 也是代数整数。由于 $\gcd(n,|C|)=1$，存在整数 $a,b$，使 $a|C|+bn=1$。于是

$$
\frac{a|C|\chi_V(g)}n+b\chi_V(g)=\frac{\chi_V(g)}n=\frac1n(\varepsilon_1+\cdots+\varepsilon_n)
$$

是代数整数。由引理 5.4.5，或者 $\varepsilon_1=\cdots=\varepsilon_n$，或者 $\varepsilon_1+\cdots+\varepsilon_n=\chi_V(g)=0$。第一种情形下，$\rho_V(g)$ 可对角化，因此必为标量算子；第二种情形下，$\chi_V(g)=0$。定理得证。$\square$

**定理 5.4.6.** 设 $G$ 为有限群，$C$ 为 $G$ 中大小为 $p^k$ 的共轭类，其中 $p$ 为素数，$k>0$。那么 $G$ 有一个非平凡的真正规子群（即 $G$ 不是单群）。

**证明.** 取 $g\in C$。由于 $g\ne e$，由特征标表的列正交性，

$$
\sum_{V\in\operatorname{Irr}G}\dim V\chi_V(g)=0.\tag{5.4.1}
$$

我们可以将 $\operatorname{Irr}G$ 分为三部分：

(1) 平凡表示；

(2) $D$，即维数被 $p$ 整除的不可约表示的集合；

(3) $N$，即维数不被 $p$ 整除的非平凡不可约表示的集合。

**引理 5.4.7.** 存在 $V\in N$，使 $\chi_V(g)\ne0$。

**证明.** 若 $V\in D$，则 $\frac1p\dim(V)\chi_V(g)$ 是代数整数，所以

$$
a=\sum_{V\in D}\frac1p\dim(V)\chi_V(g)
$$

也是代数整数。

<span class="original-page-anchor" id="pdf-page-108" aria-hidden="true"></span>

由 (5.4.1)，有

$$
\begin{aligned}
0&=\chi_{\mathbb C}(g)+\sum_{V\in D}\dim V\chi_V(g)+\sum_{V\in N}\dim V\chi_V(g)\\
&=1+pa+\sum_{V\in N}\dim V\chi_V(g).
\end{aligned}
$$

这说明最后一项不为零。$\square$

现在选取满足 $\chi_V(g)\ne0$ 的 $V\in N$；由引理 5.4.7，这样的 $V$ 存在。由定理 5.4.4，$g$（因此 $C$ 中的每个元素）在 $V$ 上都以标量作用。令 $H$ 为 $G$ 中由所有 $ab^{-1}$（$a,b\in C$）生成的子群。它是正规子群，且在 $V$ 上平凡地作用。由于 $V$ 非平凡，$H\ne G$。另外，$|C|>1$，所以 $H\ne1$。$\square$

**Burnside 定理的证明.** 假设 Burnside 定理不成立，则存在阶为 $p^aq^b$ 的不可解群 $G$。取其中阶最小的一个。此时 $G$ 是单群，由定理 5.4.6，它不可能有大小为 $p^k$ 或 $q^k$（$k\ge1$）的共轭类。所以 $G$ 的每个共轭类的大小或者等于 $1$，或者被 $pq$ 整除。把各共轭类的大小相加，所得总和等于 $p^aq^b$，由此可知，只含一个元素的共轭类必定不止一个。因此 $G$ 有非平凡的中心，矛盾。$\square$

## 5.5. 历史插曲：William Burnside 与数学中的思想和谐

在剑桥期间，William Burnside（1852–1927）在赛艇运动中表现出众。他还有一些别的成就：在 1875 年的数学荣誉考试中名列第二，随后又在更为艰苦的 Smith 奖数学竞赛中击败了此前的第一名。此后，他在剑桥担任数学讲师，同时辅导数学荣誉考试的考生，并训练赛艇队。1885 年，Burnside 不改对水上活动的兴趣，接受了格林尼治皇家海军学院数学教授的职位，一直在那里任教到退休。当他对赛艇的热情消退后，钓鱼成了他最喜爱的业余活动。甚至<span class="original-page-anchor" id="pdf-page-109" aria-hidden="true"></span>在数学研究中，他也一直与水打交道，对流体动力学作出了重要贡献。

凭借在数学物理和复变函数论中的贡献，Burnside 于 1893 年当选英国皇家学会会员。然而，这一值得追求的目标实现以后，他就抛下了这些“小打小闹”的课题，转而钻研群论。四年后，他出版了这一领域的第一本英文教科书《有限阶群论》。他显然很高兴能暂时离开应用研究，沉浸在抽象理论中，因为他在序言里写道：“本书旨在向读者介绍有限阶群理论的主要轮廓，不涉及任何应用。”Burnside 指出，群论在英国还不怎么流行。他说：“如果通过本书，我能让英国数学家对这一纯数学分支产生兴趣，我将感到十分欣慰，因为它越研究越引人入胜。”（转引自 [11, pp. 88–89]。）

然而，英国数学家的兴趣似乎并不容易唤起。十年后，Burnside 在卸任伦敦数学学会主席的演说中苦涩地说道：“毫无疑问，到目前为止，有限阶群的理论只引起了极少数英国数学家的兴趣。”他提到，法国、美国，尤其是德国，开设了越来越多的群论课程（哥廷根竟有三十名学生听课！），而英国学生对这个课题完全无动于衷，令他十分遗憾。他认为原因在于群论的处理方式过于抽象，“年轻人很难理解，甚至根本理解不了”。他举出的例子是一条关于二十面体群性质的形式化陈述，并说：“要求验证这条陈述，就好像要人解答一连串谜题。这里没有任何东西能吸引学生，也看不出它除了最枯燥的形式主义以外还有什么；它与学生此前学过的数学完全脱节。”[8, pp. 1, 3, 5]。

不过，群论中这种纯粹抽象推理的风气，Burnside 自己也出力不少。他在<span class="original-page-anchor" id="pdf-page-110" aria-hidden="true"></span>1897 年出版的书的序言中写道，大学时的老师 Arthur Cayley 有一句名言：“群是通过其符号的组合规律来定义的。”这就意味着，“研究群论时，除非确有必要，否则不应使用更具体的表示方式”（转引自 [11, p. 90]）。难怪 Burnside 的书中没有任何应用，而他 1899 年关于 504 阶单群的论文，也只在最后一段提到一个具体例子 [1, p. 13]。他把简洁奉为最高美德。有一次，一位朋友希望他把《群论》中的某些内容写得更详细一些，他的回应却是“表示遗憾，没能把它写得更加精练”[15, p. 70]。Burnside 的理想在 Bourbaki 的传统中延续下来，也引发了以 Vladimir Arnold 为首、倡导“具有人性面貌的数学”的人的愤怒：“代数学家通常把群定义为带有运算的集合，这些运算满足一长串难以记住的公理。我觉得这样的定义是无法理解的。我认为代数学家在学生的道路上设置这种障碍，是为了让门外汉更难进入他们的领域。也许他们的目的，哪怕只是潜意识里的目的，就是提高自己领域的声望。”[2, p. 118]。

为了追求精练，Burnside 决定在 1897 年版《群论》中不讨论线性替换群。他为排除这个“无用”的课题辩护说：“很难找到一个结果，能够通过考察线性变换群最直接地得到。”（转引自 [11, p. 90]。）但仅仅几个月后，他读到了 Frobenius 关于群特征标的论文，不得不重新考虑自己的决定是否明智。Frobenius 的结果与他本人的有限群研究关系密切，于是他着手用自己的语言重新表述这些结果。与 Frobenius 不同，Burnside 很熟悉 Sophus Lie 的连续变换群工具，因此能够用李群和李代数的方法，推导出 Frobenius 关于特征标和群行列式的所有主要结果。发表研究时，他谦逊地声明，自己的论文“并无原创性，因为所得结果，除一两个小例外之外，都应归功于 Frobenius 先生。不过，证明方法一般与 Frobenius 先生使用的方法很不相同”（转引自 [11, p. 106]）。

<span class="original-page-anchor" id="pdf-page-111" aria-hidden="true"></span>

Frobenius 先生对此并不买账，觉得这只不过是抢占自己成果后的蹩脚借口。Richard Dedekind 在 Burnside 的一篇论文中看到自己关于阿贝尔群的群行列式分解的定理，也同样愤怒。Frobenius 讲起自己的损失来安慰朋友：“就是这位 Burnside 先生，几年前让我十分恼火。他迅速重新发现了我发表过的全部群论定理，顺序完全相同，一个也没漏：先是我对 Sylow 定理的证明，然后是关于阶无平方因子的群、阶为 $p^a q$ 的群、阶为四个或五个素数之积的群的定理，等等，等等。无论如何，这真是心智契合的一个非凡而惊人的例子，大概只有在英国，也许还有美国，才会发生。”（转引自 [24, p. 242]。）Burnside 则开始强调，自己“独立得到了 Frobenius 教授早期论文中的主要结果”（转引自 [23, p. 278]）。Burnside 和 Frobenius 两位先生从未通信澄清此事，而是把问题留给了历史学家。历史学家对 Burnside 所称的独立发现作出了一些限定：他的研究显然受到 Frobenius 的启发，不过他并不知道 Frobenius 所有相关的论文，因此仍有足够的空间自行探索 [23, p. 278]。

Burnside 和 Frobenius 在 $p^a q^b$ 阶群的可解性问题上齐头并进。Sylow（1872 年）、Frobenius（1895 年）和 Jordan（1898 年）证明了一些特殊情形，而 Burnside 于 1904 年证明了一般情形。有人形容 Burnside 的特征标论证明“如此轻松愉快”，以至于后来用群论方法给出的证明，甚至无法接近它那“令人折服的简洁”和“惊人的美”[30, p. 469]。Walter Feit 说：“这一命题及其证明的优美，吸引了许多人研究特征标，比该领域的任何其他结果都多。”[14, p. 4]。Feit 本人就是其中之一；1962 年，他与 J. G. Thompson 一起证明了 Burnside 的猜想：每个奇数阶群都是可解群。另一个影响深远的猜想是关于挠群结构的 Burnside 问题。一个多世纪以来，它一直吸引着群论和表示论专家；Efim Zelmanov 因解决了它的限制版本，于 1994 年获得 Fields 奖。

<span class="original-page-anchor" id="pdf-page-112" aria-hidden="true"></span>

人们过了很久才认识到 Burnside 工作的美。他在皇家海军学院任职，地理上远离大学里的同事。据他的传记作者说，他似乎没有“与其他对（群论这一）课题感兴趣的数学家进行广泛的直接接触。他似乎独自工作，孤立的程度可能比当时通常的情况还严重；他很少有机会——或许也很少有意愿——同别人讨论自己的想法”[41, p. 32]。Burnside 培养了好几代海军军官，却没有建立自己的数学学派。

1925 年 12 月，Burnside 中风，医生把做数学也列入禁做的不利健康的活动。Burnside 当然没有听从，之后没活多久。《伦敦晚报》的讣告几乎没有提到他的数学研究，却写道：“赛艇界将遗憾地得知 W. Burnside 逝世的消息；他是当年剑桥最知名的运动员之一。”（转引自 [11, p. 96]。）

去世前不久，Burnside 回答了一位名叫 Philip Hall 的年轻数学家的来信。Hall 希望他在群论研究课题上给予建议，于是他寄去一张明信片，列了几个值得研究的问题。这封投入大海的漂流瓶信，奇迹般地找到了最合适的收信人。刊登 Burnside 讣告的同一卷《伦敦数学学会杂志》也刊登了 Hall 的《可解群札记》，标志着 Hall 在这一领域毕生事业的开端。Hall 最终接过了 Burnside 的位置，成为群论在英国的主要推动者。后来他写道：“我的研究目标，在很大程度上，就是沿某些方向扩展并完成 Burnside 的工作。”（转引自 [11, p. 96]。）

## 5.6. 直积的表示

**定理 5.6.1。** 设 $G,H$ 是有限群，$\{V_i\}$ 是 $G$ 在域 $k$ 上的不可约表示，$\{W_j\}$ 是 $H$ 在 $k$ 上的不可约表示，其中 $k$ 的特征可以任意。那么 $G\times H$ 在 $k$ 上的不可约表示就是 $\{V_i\otimes W_j\}$。

<span class="original-page-anchor" id="pdf-page-113" aria-hidden="true"></span>

**证明。** 这由定理 3.10.2 得到。$\square$

## 5.7. 虚表示

**定义 5.7.1。** 有限群 $G$ 的**虚表示**是 $G$ 的不可约表示的整数线性组合：$V=\sum n_iV_i$，其中 $n_i\in\mathbb Z$（也就是说，$n_i$ 不必非负）。$V$ 的特征标定义为 $\chi_V:=\sum n_i\chi_{V_i}$。

下面的引理往往很有用，后面我们还会多次用到。

**引理 5.7.2。** 设虚表示 $V$ 的特征标为 $\chi_V$。如果 $(\chi_V,\chi_V)=1$ 且 $\chi_V(1)>0$，那么 $\chi_V$ 是 $G$ 的某个不可约表示的特征标。

**证明。** 设 $V_1,V_2,\ldots,V_m$ 是 $G$ 的不可约表示，$V=\sum n_iV_i$。由特征标的标准正交性，$(\chi_V,\chi_V)=\sum_i n_i^2$，因此 $\sum_i n_i^2=1$。这意味着恰好有一个 $i$ 满足 $n_i=\pm1$，其余 $n_j=0$（$j\ne i$）。又因为 $\chi_V(1)>0$，所以 $n_i=+1$，证明完成。$\square$

## 5.8. 诱导表示

给定群 $G$ 的表示 $V$ 和子群 $H\subset G$，我们可以自然地构造 $H$ 的一个表示。$V$ 在 $H$ 上的**限制** $\operatorname{Res}_H^G V$，就是以 $V$ 为向量空间、作用为 $\rho_{\operatorname{Res}_H^G V}=\rho_V|_H$ 的表示。

反过来，给定子群 $H$ 的一个表示 $V$，也可以自然地构造群 $G$ 的表示，只是这种构造稍复杂一些。

**定义 5.8.1。** 设 $G$ 是群，$H\subset G$，$V$ 是 $H$ 的表示。**诱导表示** $\operatorname{Ind}_H^G V$ 是 $G$ 的如下表示：

$$
\operatorname{Ind}_H^G V=\{f:G\to V\mid f(hx)=\rho_V(h)f(x)\ \forall x\in G,h\in H\},
$$

其作用为 $g(f)(x)=f(xg)$，$\forall g\in G$。

**注 5.8.2。** 事实上，$\operatorname{Ind}_H^G V$ 与表示 $\operatorname{Hom}_H(k[G],V)$ 自然同构。

<span class="original-page-anchor" id="pdf-page-114" aria-hidden="true"></span>

下面验证 $\operatorname{Ind}_H^G V$ 确实定义了一个表示。对任意 $g,g',x\in G$ 和 $h\in H$，有

$$
g(f)(hx)=f(hxg)=\rho_V(h)f(xg)=\rho_V(h)g(f)(x),
$$

以及

$$
g(g'(f))(x)=g'(f)(xg)=f(xgg')=(gg')(f)(x).
$$

**注 5.8.3。** 注意，从 $G$ 的每个右 $H$-陪集 $\sigma$ 中选取一个代表元 $x_\sigma$ 后，任意 $f\in\operatorname{Ind}_H^G V$ 都由 $\{f(x_\sigma)\}$ 唯一确定。

因此，在指数 $(G:H)$ 有限时，

$$
\dim(\operatorname{Ind}_H^G V)=\dim V\cdot(G:H).
$$

**译校注。** 原书写作 $\dim V\cdot|G|/|H|$。作者的官方勘误指出，这里的 $G$ 可以是无限群，因此应改用子群指数 $(G:H)$。这里的维数公式以及下面有限维诱导表示的特征标公式，以 $(G:H)$ 有限为前提。

**习题 5.8.4。** 设 $K\subset H\subset G$ 是群，$V$ 是 $K$ 的表示。验证 $\operatorname{Ind}_H^G\operatorname{Ind}_K^H V$ 与 $\operatorname{Ind}_K^G V$ 同构。

**练习 5.8.5。** 设 $K\subset G$ 是有限群，$\chi:K\to\mathbb C^*$ 是同态，$\mathbb C_\chi$ 是对应的 $K$ 的一维表示。令

$$
e_\chi=\frac{1}{|K|}\sum_{g\in K}\chi(g)^{-1}g\in\mathbb C[K]
$$

为对应于 $\chi$ 的幂等元。证明 $G$ 的表示 $\operatorname{Ind}_K^G\mathbb C_\chi$ 与 $\mathbb C[G]e_\chi$ 自然同构，其中 $G$ 在后者上按左乘作用。

## 5.9. 诱导表示特征标的 Frobenius 公式

现在计算 $\operatorname{Ind}_H^G V$ 的特征标 $\chi$。从每个右陪集 $\sigma\in H\backslash G$ 中选取一个代表元 $x_\sigma$。

**定理 5.9.1。** 有

$$
\chi(g)=\sum_{\substack{\sigma\in H\backslash G:\\x_\sigma g x_\sigma^{-1}\in H}}\chi_V(x_\sigma g x_\sigma^{-1}).
$$

这个公式称为 Frobenius 公式。

**译校注。** 按作者官方勘误，这里也须保证子群指数 $(G:H)$ 有限，才能在有限维表示的意义下使用该特征标公式。

<span class="original-page-anchor" id="pdf-page-115" aria-hidden="true"></span>

**注 5.9.2。** 如果底域 $k$ 的特征与 $|H|$ 互素，那么该公式可以写成

$$
\chi(g)=\frac{1}{|H|}\sum_{\substack{x\in G:\\xgx^{-1}\in H}}\chi_V(xgx^{-1}).
$$

**证明。** 对 $G$ 的一个右 $H$-陪集 $\sigma$，定义

$$
V_\sigma=\{f\in\operatorname{Ind}_H^G V\mid f(g)=0\ \forall g\notin\sigma\}.
$$

于是

$$
\operatorname{Ind}_H^G V=\bigoplus_\sigma V_\sigma,
$$

从而

$$
\chi(g)=\sum_\sigma\chi_\sigma(g),
$$

其中 $\chi_\sigma(g)$ 是 $\rho(g)$ 中对应于 $V_\sigma$ 的对角块的迹。

因为对任意右 $H$-陪集 $\sigma$，$g(\sigma)=\sigma g$ 也是右 $H$-陪集，所以当 $\sigma\ne\sigma g$ 时，$\chi_\sigma(g)=0$。

现在假设 $\sigma=\sigma g$。那么 $x_\sigma g=hx_\sigma$，其中 $h=x_\sigma g x_\sigma^{-1}\in H$。考虑映射 $\alpha:V_\sigma\to V$，定义为 $\alpha(f)=f(x_\sigma)$。由于 $f\in V_\sigma$ 由 $f(x_\sigma)$ 唯一确定，$\alpha$ 是同构。又有

$$
\alpha(gf)=g(f)(x_\sigma)=f(x_\sigma g)=f(hx_\sigma)=\rho_V(h)f(x_\sigma)=h\alpha(f),
$$

因此 $gf=\alpha^{-1}h\alpha(f)$，也就是说 $\chi_\sigma(g)=\chi_V(h)$。所以

$$
\chi(g)=\sum_{\substack{\sigma\in H\backslash G,\\\sigma g=\sigma}}\chi_V(x_\sigma g x_\sigma^{-1}).
$$

$\square$

## 5.10. Frobenius 互反性

关于诱导表示，一个非常重要的结果是 Frobenius 互反性定理，它把 $\operatorname{Ind}$ 和 $\operatorname{Res}$ 这两个运算联系起来。

**定理 5.10.1（Frobenius 互反性）。** 设 $H\subset G$ 是群，$V$ 是 $G$ 的表示，$W$ 是 $H$ 的表示。那么 $\operatorname{Hom}_G(V,\operatorname{Ind}_H^G W)$ 与 $\operatorname{Hom}_H(\operatorname{Res}_H^G V,W)$ 自然同构。

<span class="original-page-anchor" id="pdf-page-116" aria-hidden="true"></span>

**证明。** 令 $E=\operatorname{Hom}_G(V,\operatorname{Ind}_H^G W)$，$E'=\operatorname{Hom}_H(\operatorname{Res}_H^G V,W)$。定义 $F:E\to E'$ 和 $F':E'\to E$：对任意 $\alpha\in E$，令 $F(\alpha)v=(\alpha v)(e)$；对任意 $\beta\in E'$，令 $(F'(\beta)v)(x)=\beta(xv)$。

要验证 $F,F'$ 定义良好且互为逆映射，需要验证以下五点。

设 $\alpha\in E$，$\beta\in E'$，$v\in V$，$x,g\in G$。

(a) $F(\alpha)$ 是 $H$-同态，即 $F(\alpha)hv=hF(\alpha)v$。

确实，$F(\alpha)hv=(\alpha hv)(e)=(h\alpha v)(e)=(\alpha v)(he)=(\alpha v)(eh)=h\cdot(\alpha v)(e)=hF(\alpha)v$。

(b) $F'(\beta)v\in\operatorname{Ind}_H^G W$，即 $(F'(\beta)v)(hx)=h(F'(\beta)v)(x)$。

确实，$(F'(\beta)v)(hx)=\beta(hxv)=h\beta(xv)=h(F'(\beta)v)(x)$。

(c) $F'(\beta)$ 是 $G$-同态，即 $F'(\beta)gv=g(F'(\beta)v)$。

确实，$(F'(\beta)gv)(x)=\beta(xgv)=(F'(\beta)v)(xg)=(g(F'(\beta)v))(x)$。

(d) $F\circ F'=\operatorname{Id}_{E'}$。

因为 $F(F'(\beta))v=(F'(\beta)v)(e)=\beta(v)$，所以成立。

(e) $F'\circ F=\operatorname{Id}_E$，即 $(F'(F(\alpha))v)(x)=(\alpha v)(x)$。

确实，$(F'(F(\alpha))v)(x)=F(\alpha)(xv)=(\alpha xv)(e)=(x\alpha v)(e)=(\alpha v)(x)$。证明完成。$\square$

**译校注。** 原书 (e) 的等式中写作 $F(\alpha xv)$；按 $F$ 的定义，此处应为 $F(\alpha)(xv)$，译文已改正括号位置。

**习题 5.10.2。** 本题旨在把限制表示和诱导表示放进一个更深入的框架来理解，这个框架就是 $k$-代数上的张量积。特别地，这种理解将给出 Frobenius 互反性的新证明，也会揭示诱导和限制之间的一些类似之处。

本题始终使用习题 2.11.6 的记号和结果。

设 $G$ 是有限群，$H\subset G$ 是子群。把 $k[G]$ 看作 $(k[H],k[G])$-双模，两种模结构都由 $k[G]$ 内的乘法给出。将这个双模记为 $k[G]_1$。

另一方面，也可以把 $k[G]$ 看作 $(k[G],k[H])$-双模，两种模结构同样由乘法给出。将这个双模记为 $k[G]_2$。

<span class="original-page-anchor" id="pdf-page-117" aria-hidden="true"></span>

(a) 设 $V$ 是 $G$ 的表示，那么 $V$ 是左 $k[G]$-模，因此张量积 $k[G]_1\otimes_{k[G]}V$ 是左 $k[H]$-模。证明这个张量积作为左 $k[H]$-模与 $\operatorname{Res}_H^G V$ 同构。同构

$$
\operatorname{Res}_H^G V\to k[G]_1\otimes_{k[G]}V
$$

由 $v\mapsto1\otimes_{k[G]}v$ 给出，其中 $v\in\operatorname{Res}_H^G V$。

(b) 设 $W$ 是 $H$ 的表示，那么 $W$ 是左 $k[H]$-模。由注 5.8.2，$\operatorname{Ind}_H^G W\cong\operatorname{Hom}_H(k[G],W)$，也就是 $\operatorname{Ind}_H^G W\cong\operatorname{Hom}_{k[H]}(k[G]_1,W)$。利用习题 2.11.6(b) 推出定理 5.10.1。

(c) 设 $V$ 是 $G$ 的表示，那么 $V$ 是左 $k[G]$-模。证明不仅 $k[G]_1\otimes_{k[G]}V$，而且 $\operatorname{Hom}_{k[G]}(k[G]_2,V)$，作为左 $k[H]$-模都与 $\operatorname{Res}_H^G V$ 同构。同构

$$
\operatorname{Hom}_{k[G]}(k[G]_2,V)\to\operatorname{Res}_H^G V
$$

由 $f\mapsto f(1)$ 给出，其中 $f\in\operatorname{Hom}_{k[G]}(k[G]_2,V)$。

(d) 设 $W$ 是 $H$ 的表示，那么 $W$ 是左 $k[H]$-模。证明 $\operatorname{Ind}_H^G W$ 与 $k[G]_2\otimes_{k[H]}W$ 同构。同构 $\operatorname{Hom}_{k[H]}(k[G]_1,W)\to k[G]_2\otimes_{k[H]}W$ 由 $f\mapsto\sum_{g\in P}g^{-1}\otimes_{k[H]}f(g)$ 给出，其中 $f\in\operatorname{Hom}_{k[H]}(k[G]_1,W)$，$P$ 是 $G$ 中各个右 $H$-陪集的一组互不相同的代表元。（这一同构与代表元的选择无关。）

(e) 设 $V$ 是 $G$ 的表示，$W$ 是 $H$ 的表示。利用 (b) 证明 $\operatorname{Hom}_G(\operatorname{Ind}_H^G W,V)$ 与 $\operatorname{Hom}_H(W,\operatorname{Res}_H^G V)$ 自然同构。

(f) 设 $V$ 是 $H$ 的表示。证明 $\operatorname{Ind}_H^G(V^*)\cong(\operatorname{Ind}_H^G V)^*$，作为 $G$ 的表示成立。[提示：把 $\operatorname{Ind}_H^G V$ 写成 $k[G]_2\otimes_{k[H]}V$，把 $\operatorname{Ind}_H^G(V^*)$ 写成 $\operatorname{Hom}_{k[H]}(k[G]_1,V^*)$。证明映射 $\operatorname{Hom}_{k[H]}(k[G]_1,V^*)\times(\operatorname{Ind}_H^G V)\to k$，定义为 $(f,(x\otimes_{k[H]}v))\mapsto(f(Sx))(v)$，是非退化的 $G$-不变双线性型；其中 $S:k[G]\to k[G]$ 是线性映射，对任意 $g\in G$ 都有 $Sg=g^{-1}$。]

**译校注。** 原书在提示的配对定义域中误写为 $\operatorname{Ind}_H^G(V^*)$；依作者官方勘误，改为 $\operatorname{Ind}_H^G V$。

<span class="original-page-anchor" id="pdf-page-118" aria-hidden="true"></span>

## 5.11. 例子

下面给出几个诱导表示的例子，表示的记号沿用前面的特征标表。

(1) 设 $G=S_3$，$H=\mathbb Z_2$。由 Frobenius 互反性，得到 $\operatorname{Ind}_H^G\mathbb C_+=\mathbb C^2\oplus\mathbb C_+$，$\operatorname{Ind}_H^G\mathbb C_-=\mathbb C^2\oplus\mathbb C_-$。

(2) 设 $G=S_3$，$H=\mathbb Z_3$。得到 $\operatorname{Ind}_H^G\mathbb C_+=\mathbb C_+\oplus\mathbb C_-$，$\operatorname{Ind}_H^G\mathbb C_\varepsilon=\operatorname{Ind}_H^G\mathbb C_{\varepsilon^2}=\mathbb C^2$。

(3) 设 $G=S_4$，$H=S_3$。那么 $\operatorname{Ind}_H^G\mathbb C_+=\mathbb C_+\oplus\mathbb C_-^3$，$\operatorname{Ind}_H^G\mathbb C_-=\mathbb C_-\oplus\mathbb C_+^3$，$\operatorname{Ind}_H^G\mathbb C^2=\mathbb C^2\oplus\mathbb C_-^3\oplus\mathbb C_+^3$。

**习题 5.11.1。** 分别从下列子群的不可约表示出发，计算所诱导的所有 $A_5$ 表示的不可约分解：

(a) $\mathbb Z_2$；

(b) $\mathbb Z_3$；

(c) $\mathbb Z_5$；

(d) $A_4$；

(e) $\mathbb Z_2\times\mathbb Z_2$。

## 5.12. $S_n$ 的表示

本节描述任意 $n$ 对应的对称群 $S_n$ 的表示。

**定义 5.12.1。** $n$ 的一个**分拆** $\lambda$，是把 $n$ 写成 $n=\lambda_1+\lambda_2+\cdots+\lambda_p$ 的形式，其中 $\lambda_i$ 是正整数，且 $\lambda_i\ge\lambda_{i+1}$。

对每个这样的 $\lambda$，定义**杨图** $Y_\lambda$：它是坐标平面内矩形 $-i\le y\le-i+1$、$0\le x\le\lambda_i$（$i=1,\ldots,p$）的并。显然，$Y_\lambda$ 由 $n$ 个单位正方形组成。把数字 $1,\ldots,n$ 以某种方式填入 $Y_\lambda$ 的方格中，不允许重复，所得的就是对应于 $Y_\lambda$ 的一个**杨表**。例如，我们将使用这样的杨表 $T_\lambda$：按从左到右、从上到下的顺序，依次填入递增的数字。

可以定义与 $T_\lambda$ 对应的两个 $S_n$ 的子群：

<span class="original-page-anchor" id="pdf-page-119" aria-hidden="true"></span>

1. 行子群 $P_\lambda$：它把 $\{1,\ldots,n\}$ 中的每个元素映到 $T_\lambda$ 中同一行的元素。

2. 列子群 $Q_\lambda$：它把 $\{1,\ldots,n\}$ 中的每个元素映到 $T_\lambda$ 中同一列的元素。

显然，$P_\lambda\cap Q_\lambda=\{1\}$。

定义**杨投影算子**

$$
a_\lambda:=\frac{1}{|P_\lambda|}\sum_{g\in P_\lambda}g,
$$

$$
b_\lambda:=\frac{1}{|Q_\lambda|}\sum_{g\in Q_\lambda}(-1)^g g,
$$

其中 $(-1)^g$ 表示置换 $g$ 的符号。令 $c_\lambda=a_\lambda b_\lambda$。由于 $P_\lambda\cap Q_\lambda=\{1\}$，这个元素非零。

下面的定理给出 $S_n$ 的不可约表示。

**定理 5.12.2。** $\mathbb C[S_n]$ 的子空间 $V_\lambda:=\mathbb C[S_n]c_\lambda$ 在左乘作用下是 $S_n$ 的不可约表示。$S_n$ 的每个不可约表示都与唯一一个 $\lambda$ 对应的 $V_\lambda$ 同构。

这些模 $V_\lambda$ 称为 **Specht 模**。

这个定理的证明将在下一节给出。

**例 5.12.3。** 对分拆 $\lambda=(n)$，有 $P_\lambda=S_n$、$Q_\lambda=\{1\}$，所以 $c_\lambda$ 是对称化算子，$V_\lambda$ 因而是平凡表示。

对分拆 $\lambda=(1,\ldots,1)$，有 $Q_\lambda=S_n$、$P_\lambda=\{1\}$，所以 $c_\lambda$ 是反对称化算子，$V_\lambda$ 因而是符号表示。

$n=3$ 时，对 $\lambda=(2,1)$，有 $V_\lambda=\mathbb C^2$。

$n=4$ 时，对 $\lambda=(2,2)$，有 $V_\lambda=\mathbb C^2$；对 $\lambda=(3,1)$，有 $V_\lambda=\mathbb C_-^3$；对 $\lambda=(2,1,1)$，有 $V_\lambda=\mathbb C_+^3$。

**推论 5.12.4。** $S_n$ 的所有不可约表示都可以用有理数为元素的矩阵给出。

**习题 5.12.5。** 求对称群 $S_n$ 的所有不可约表示的维数之和。

<span class="original-page-anchor" id="pdf-page-120" aria-hidden="true"></span>

提示：证明 $S_n$ 的所有不可约表示都是实的，即都具有非退化的不变对称型。然后使用 Frobenius–Schur 定理。

## 5.13. $S_n$ 表示分类定理的证明

**引理 5.13.1。** 设 $x\in\mathbb C[S_n]$。那么 $a_\lambda x b_\lambda=\ell_\lambda(x)c_\lambda$，其中 $\ell_\lambda$ 是线性函数。

**证明。** 如果 $g\in P_\lambda Q_\lambda$，那么 $g$ 可以唯一地写成 $pq$，其中 $p\in P_\lambda$、$q\in Q_\lambda$，因此 $a_\lambda g b_\lambda=(-1)^q c_\lambda$。所以，只要证明：如果置换 $g$ 不属于 $P_\lambda Q_\lambda$，就有 $a_\lambda g b_\lambda=0$。

为此，只需找到一个换位 $t$，满足 $t\in P_\lambda$ 且 $g^{-1}tg\in Q_\lambda$。这时

$$
a_\lambda g b_\lambda=a_\lambda t g b_\lambda=a_\lambda g(g^{-1}tg)b_\lambda=-a_\lambda g b_\lambda,
$$

所以 $a_\lambda g b_\lambda=0$。换句话说，需要找到两个元素 $i,j$，它们在杨表 $T=T_\lambda$ 中位于同一行，在杨表 $T'=gT$ 中位于同一列。这里 $gT$ 是用置换 $g$ 置换 $T$ 的各个元素所得的杨表，形状与 $T$ 相同。因此，只要证明：若不存在这样的一对元素，那么 $g\in P_\lambda Q_\lambda$，也就是说，存在 $p\in P_\lambda$ 和 $q'\in Q'_\lambda:=gQ_\lambda g^{-1}$，使得 $pT=q'T'$。这时 $g=pq^{-1}$，其中 $q=g^{-1}q'g\in Q_\lambda$。

$T$ 第一行的任意两个元素必定在 $T'$ 的不同列中，所以存在 $q'_1\in Q'_\lambda$，能把这些元素全部移到第一行。于是存在 $p_1\in P_\lambda$，使 $p_1T$ 和 $q'_1T'$ 的第一行相同。再对第二行做同样的操作，找到 $p_2,q'_2$，使 $p_2p_1T$ 与 $q'_2q'_1T'$ 的前两行相同。继续下去，就能构造所需的 $p,q'$。引理得证。$\square$

在分拆上引入**字典序**：如果第一个非零的 $\lambda_i-\mu_i$ 为正，就规定 $\lambda>\mu$。

**引理 5.13.2。** 如果 $\lambda>\mu$，那么 $a_\lambda\mathbb C[S_n]b_\mu=0$。

<span class="original-page-anchor" id="pdf-page-121" aria-hidden="true"></span>

**证明。** 与前一个引理类似，只要证明：对任意 $g\in S_n$，都存在换位 $t\in P_\lambda$，使 $g^{-1}tg\in Q_\mu$。令 $T=T_\lambda$、$T'=gT_\mu$。我们断言，存在两个整数，它们在 $T$ 中位于同一行，在 $T'$ 中位于同一列。确实，如果 $\lambda_1>\mu_1$，由抽屉原理，第一行就有这样的一对元素。如果 $\lambda_1=\mu_1$，则像前一个引理的证明那样，找到 $p_1\in P_\lambda$、$q'_1\in gQ_\mu g^{-1}$，使 $p_1T$ 和 $q'_1T'$ 的第一行相同；然后对第二行重复这个论证，如此继续。最终，经过 $i-1$ 步后会遇到 $\lambda_i>\mu_i$。这时，第一个杨表的第 $i$ 行中必有两个元素位于第二个杨表的同一列，证明完成。$\square$

**引理 5.13.3。** $c_\lambda$ 与一个幂等元成比例。具体地，

$$
c_\lambda^2=\frac{n!}{|P_\lambda||Q_\lambda|\dim V_\lambda}c_\lambda.
$$

**证明。** 由引理 5.13.1，$c_\lambda^2$ 与 $c_\lambda$ 成比例。又容易看出，$c_\lambda$ 在正则表示中的迹为 $n!/(|P_\lambda||Q_\lambda|)$，因为 $c_\lambda$ 中单位元的系数为 $1/(|P_\lambda||Q_\lambda|)$。由此得到结论。$\square$

**译校注。** 原书在引理及证明中分别把上述分子写成 $n!$，并把单位元系数写成 $1$。依作者官方勘误，这些地方都应补上归一化因子 $1/(|P_\lambda||Q_\lambda|)$，与前面对杨投影算子的定义一致。

**引理 5.13.4。** 设 $A$ 是代数，$e\in A$ 是幂等元。那么对任意左 $A$-模 $M$，都有 $\operatorname{Hom}_A(Ae,M)\cong eM$。具体地，$x\in eM$ 对应映射 $f_x:Ae\to M$，其定义为 $f_x(a)=ax$，$a\in Ae$。

**证明。** 注意，$1-e$ 也是 $A$ 中的幂等元。由 $\operatorname{Hom}_A(A,M)\cong M$ 和分解 $A=Ae\oplus A(1-e)$，立即得到结论。$\square$

现在可以证明定理 5.12.2 了。设 $\lambda\ge\mu$，由引理 5.13.3 和 5.13.4，

$$
\operatorname{Hom}_{S_n}(V_\lambda,V_\mu)=\operatorname{Hom}_{S_n}(\mathbb C[S_n]c_\lambda,\mathbb C[S_n]c_\mu)=c_\lambda\mathbb C[S_n]c_\mu.
$$

由引理 5.13.2，当 $\lambda>\mu$ 时，最后一个空间为零；由引理 5.13.1 和 5.13.3，当 $\lambda=\mu$ 时，它是一维的。因此，各 $V_\lambda$ 都不可约，且当 $\lambda\ne\mu$ 时，$V_\lambda$ 与 $V_\mu$ 不同构。由于分拆的数目等于 $S_n$ 中共轭类的数目，这些 $V_\lambda$ 就给出了 $S_n$ 的全部不可约表示。定理得证。

<span class="original-page-anchor" id="pdf-page-122" aria-hidden="true"></span>

## 5.14. $S_n$ 的诱导表示

把表示 $\operatorname{Ind}_{P_\lambda}^{S_n}\mathbb C$ 记为 $U_\lambda$。容易看出，也可以把它定义为 $U_\lambda=\mathbb C[S_n]a_\lambda$。

**命题 5.14.1。** 当 $\mu<\lambda$ 时，$\operatorname{Hom}(U_\lambda,V_\mu)=0$，而 $\dim\operatorname{Hom}(U_\lambda,V_\lambda)=1$。因此，$U_\lambda=\bigoplus_{\mu\ge\lambda}K_{\mu\lambda}V_\mu$，其中 $K_{\mu\lambda}$ 是非负整数，且 $K_{\lambda\lambda}=1$。

**定义 5.14.2。** 整数 $K_{\mu\lambda}$ 称为 **Kostka 数**。

**证明。** 由引理 5.13.3 和 5.13.4，

$$
\operatorname{Hom}(U_\lambda,V_\mu)=\operatorname{Hom}(\mathbb C[S_n]a_\lambda,\mathbb C[S_n]a_\mu b_\mu)=a_\lambda\mathbb C[S_n]a_\mu b_\mu.
$$

再由引理 5.13.1 和 5.13.2 得到结论。$\square$

现在计算 $U_\lambda$ 的特征标。设 $C_{\mathbf i}$ 是 $S_n$ 的一个共轭类，其中的置换对每个 $l\ge1$ 都有 $i_l$ 个长度为 $l$ 的循环。这里 $\mathbf i$ 是 $(i_1,\ldots,i_l,\ldots)$ 的简写。另取变量 $x_1,\ldots,x_N$，令

$$
H_m(x)=\sum_i x_i^m
$$

为幂和多项式。

**定理 5.14.3。** 设 $N\ge p$，其中 $p$ 是 $\lambda$ 的分拆项数。那么 $\chi_{U_\lambda}(C_{\mathbf i})$ 是多项式

$$
\prod_{m\ge1}H_m(x)^{i_m}
$$

中 $x^\lambda:=\prod_j x_j^{\lambda_j}$ 的系数。[^pdf122-1]

**证明。** 由 Frobenius 公式很容易得到证明。具体地，选取代表元 $g\in C_{\mathbf i}$，则 $\chi_{U_\lambda}(C_{\mathbf i})$ 等于满足 $xgx^{-1}\in P_\lambda$ 的 $x\in S_n$ 的数目，除以 $|P_\lambda|$。$P_\lambda$ 的阶为 $\prod_i\lambda_i!$，而这样的 $x$ 的数目等于 $P_\lambda$ 中与 $g$ 共轭的元素数目，即 $|C_{\mathbf i}\cap P_\lambda|$，乘以 $g$ 的中心化子 $Z_g$ 的阶。后者等于 $n!/|C_{\mathbf i}|$。因此，

$$
\chi_{U_\lambda}(C_{\mathbf i})=\frac{|Z_g|}{\prod_j\lambda_j!}|C_{\mathbf i}\cap P_\lambda|.
$$

<span class="original-page-anchor" id="pdf-page-123" aria-hidden="true"></span>

容易看出，$g$ 的中心化子 $Z_g$ 同构于

$$
\prod_m\bigl(S_{i_m}\ltimes(\mathbb Z/m\mathbb Z)^{i_m}\bigr),
$$

因此，

$$
|Z_g|=\prod_m m^{i_m}i_m!,
$$

从而

$$
\chi_{U_\lambda}(C_{\mathbf i})=\frac{\prod_m m^{i_m}i_m!}{\prod_j\lambda_j!}|C_{\mathbf i}\cap P_\lambda|.
$$

由于 $P_\lambda=\prod_j S_{\lambda_j}$，有

$$
|C_{\mathbf i}\cap P_\lambda|=\sum_r\prod_{j\ge1}\frac{\lambda_j!}{\prod_{m\ge1}m^{r_{jm}}r_{jm}!},
$$

其中 $r=(r_{jm})$ 遍历满足下列条件的所有非负整数族：

$$
\sum_m mr_{jm}=\lambda_j,\qquad\sum_j r_{jm}=i_m.
$$

确实，$C_{\mathbf i}$ 中属于 $P_\lambda$ 的一个元素，会把每个 $\lambda_j$ 按循环长度分拆成各项，其中 $m$ 出现 $r_{jm}$ 次；把所有 $j$ 合在一起，每项 $m$ 出现的总次数为 $i_m$。于是得到

$$
\chi_{U_\lambda}(C_{\mathbf i})=\sum_r\prod_m\frac{i_m!}{\prod_j r_{jm}!}.
$$

这恰好是

$$
\prod_{m\ge1}(x_1^m+\cdots+x_N^m)^{i_m}
$$

中 $x^\lambda$ 的系数，其中 $r_{jm}$ 是选取 $x_j^m$ 的次数。$\square$

## 5.15. Frobenius 特征标公式

令 $\Delta(x)=\prod_{1\le i<j\le N}(x_i-x_j)$，$\rho=(N-1,N-2,\ldots,0)\in\mathbb C^N$。下面这个由 Frobenius 给出的定理，给出了 Specht 模 $V_\lambda$ 的特征标公式。

<span class="original-page-anchor" id="pdf-page-124" aria-hidden="true"></span>

**定理 5.15.1。** 设 $N\ge p$。那么 $\chi_{V_\lambda}(C_{\mathbf i})$ 是多项式

$$
\Delta(x)\prod_{m\ge1}H_m(x)^{i_m}
$$

中 $x^{\lambda+\rho}:=\prod_j x_j^{\lambda_j+N-j}$ 的系数。

**注 5.15.2。** 定理 5.15.1 有如下等价表述：$\chi_{V_\lambda}(C_{\mathbf i})$ 是 Laurent 多项式

$$
\prod_{i<j}\left(1-\frac{x_j}{x_i}\right)\prod_{m\ge1}H_m(x)^{i_m}
$$

中 $x^\lambda$ 的系数。

**证明。** 为简便起见，把 $\chi_{V_\lambda}$ 记为 $\chi_\lambda$，把定理所定义的类函数记为 $\theta_\lambda$。我们断言，$\theta_\lambda=\sum_{\mu\ge\lambda}L_{\mu\lambda}\chi_\mu$，其中 $L_{\mu\lambda}$ 是整数，且 $L_{\lambda\lambda}=1$。事实上，由定理 5.14.3，

$$
\theta_\lambda=\sum_{\sigma\in S_N}(-1)^\sigma\chi_{U_{\lambda+\rho-\sigma(\rho)}}.
$$

这里，如果向量 $\lambda+\rho-\sigma(\rho)$ 有负分量，就删去对应的项；如果各分量都非负，但不是非递增排列，就把它们按非递增顺序重新排列，所得的分拆记为 $\langle\lambda+\rho-\sigma(\rho)\rangle$。也就是说，约定 $U_{\lambda+\rho-\sigma(\rho)}:=U_{\langle\lambda+\rho-\sigma(\rho)\rangle}$。注意，$\mu=\langle\lambda+\rho-\sigma(\rho)\rangle$ 可以由 $\lambda$ 加上形如 $e_i-e_j$（$i<j$）的向量得到，因此 $\mu>\lambda$ 或 $\mu=\lambda$；而且只有在 $\sigma=1$ 时才会有 $\mu=\lambda$。这就得到了所需的性质。

因此，由引理 5.7.2，要证明 $\theta_\lambda=\chi_\lambda$，只需证明 $(\theta_\lambda,\theta_\lambda)=1$。

我们有

$$
(\theta_\lambda,\theta_\lambda)=\frac{1}{n!}\sum_{\mathbf i}|C_{\mathbf i}|\theta_\lambda(C_{\mathbf i})^2.
$$

利用

$$
|C_{\mathbf i}|=\frac{n!}{\prod_m m^{i_m}i_m!},
$$

可知 $(\theta_\lambda,\theta_\lambda)$ 是级数 $R(x,y)=\Delta(x)\Delta(y)S(x,y)$ 中 $x^{\lambda+\rho}y^{\lambda+\rho}$ 的系数，其中

$$
\begin{aligned}
S(x,y)&=\sum_{\mathbf i}\prod_m\frac{(\sum_j x_j^m)^{i_m}(\sum_k y_k^m)^{i_m}}{m^{i_m}i_m!}\\
&=\sum_{\mathbf i}\prod_m\frac{(\sum_{j,k}x_j^m y_k^m/m)^{i_m}}{i_m!}.
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-125" aria-hidden="true"></span>

对 $\mathbf i$ 和 $m$ 求和，得到

$$
\begin{aligned}
S(x,y)&=\prod_m\exp\left(\sum_{j,k}x_j^m y_k^m/m\right)\\
&=\exp\left(-\sum_{j,k}\log(1-x_jy_k)\right)=\prod_{j,k}(1-x_jy_k)^{-1}.
\end{aligned}
$$

因此，

$$
R(x,y)=\frac{\prod_{i<j}(x_i-x_j)(y_i-y_j)}{\prod_{i,j}(1-x_i y_j)}.
$$

下面需要一个引理。

**引理 5.15.3。**

$$
\frac{\prod_{i<j}(z_j-z_i)(y_i-y_j)}{\prod_{i,j}(z_i-y_j)}=\det\left(\frac{1}{z_i-y_j}\right).
$$

**证明。** 将两边乘以 $\prod_{i,j}(z_i-y_j)$。所得右边在超平面 $z_i=z_j$ 和 $y_i=y_j$ 上必定为零，也就是说，它能被 $\Delta(z)\Delta(y)$ 整除；同时它是次数为 $N(N-1)$ 的齐次多项式。因此，两边成比例。把两边乘以 $z_N-y_N$，再令 $z_N=y_N$，由归纳法可求出比例系数为 $1$。$\square$

在引理中令 $z_i=1/x_i$，得到

**推论 5.15.4（Cauchy 恒等式）。**

$$
R(x,y)=\det\left(\frac{1}{1-x_i y_j}\right)=\sum_{\sigma\in S_N}\frac{(-1)^\sigma}{\prod_{j=1}^N(1-x_j y_{\sigma(j)})}.
$$

**译校注。** 原书最后一个表达式的分子误写为 $1$；依作者官方勘误，改为 $(-1)^\sigma$，即行列式展开中的置换符号。

由推论 5.15.4 很容易看出，$x^{\lambda+\rho}y^{\lambda+\rho}$ 的系数为 $1$。确实，如果 $\sigma\in S_N$ 且 $\sigma\ne1$，那么这一单项式在 $\frac{1}{\prod_j(1-x_jy_{\sigma(j)})}$ 中的系数显然为零。$\square$

**注 5.15.5。** 对 $n$ 的两个分拆 $\lambda,\mu$，若 $\mu-\lambda$ 是若干形如 $e_i-e_j$（$i<j$）的向量之和，就记为 $\lambda\preceq\mu$ 或 $\mu\succeq\lambda$；这些向量称为正根。这是一个偏序，并且 $\mu\succ\lambda$ 蕴含 $\mu>\lambda$。由定理 5.15.1 及其证明，

$$
\chi_\lambda=\sum_{\mu\succeq\lambda}\widetilde K_{\mu\lambda}\chi_{U_\mu},
$$

<span class="original-page-anchor" id="pdf-page-126" aria-hidden="true"></span>

其中矩阵 $(\widetilde K_{\lambda\mu})$ 是 Kostka 数矩阵 $(K_{\lambda\mu})$ 的逆矩阵。这说明，除非 $\mu\succeq\lambda$，否则 Kostka 数 $K_{\mu\lambda}$ 为零。

## 5.16. 习题

在下面的习题中，我们不区分杨图与分拆。

**习题 5.16.1。** 对杨图 $\mu$，令 $A(\mu)$ 为在 $\mu$ 中增加一个方格所能得到的杨图的集合，$R(\mu)$ 为从 $\mu$ 中删去一个方格所能得到的杨图的集合。

(a) 证明 $\operatorname{Res}_{S_{n-1}}^{S_n}V_\mu=\bigoplus_{\lambda\in R(\mu)}V_\lambda$。

(b) 证明 $\operatorname{Ind}_{S_{n-1}}^{S_n}V_\mu=\bigoplus_{\lambda\in A(\mu)}V_\lambda$。

**习题 5.16.2。** 杨图 $\lambda$ 的**含量** $c(\lambda)$ 定义为 $\sum_j\sum_{i=1}^{\lambda_j}(i-j)$。设 $C=\sum_{i<j}(ij)\in\mathbb C[S_n]$ 是所有换位之和。证明 $C$ 在 Specht 模 $V_\lambda$ 上的作用是乘以 $c(\lambda)$。

**习题 5.16.3。** (a) 设 $V$ 是 $S_n$ 的任意有限维表示。证明元素 $E:=(12)+\cdots+(1n)$ 在 $V$ 上可对角化，且特征值都是介于 $1-n$ 和 $n-1$ 之间的整数。

提示：把 $E$ 写成 $C_n-C_{n-1}$，其中 $C_n=C$ 是习题 5.16.2 中的元素。

(b) 证明元素 $(12)+\cdots+(1n)$ 在 $V_\lambda$ 上按一个标量作用，当且仅当 $\lambda$ 是矩形杨图，并计算这个标量。

## 5.17. 钩长公式

下面用 Frobenius 特征标公式计算 $V_\lambda$ 的维数。由特征标公式，$\dim V_\lambda$ 是 $\Delta(x)(x_1+\cdots+x_N)^n$ 中 $x^{\lambda+\rho}$ 的系数。令 $l_j=\lambda_j+N-j$，利用 $\Delta(x)$ 的行列式公式，把行列式展开为<span class="original-page-anchor" id="pdf-page-127" aria-hidden="true"></span>对置换求和，得到

$$
\begin{aligned}
\dim V_\lambda
&=\sum_{\substack{s\in S_N:\\l_j\ge N-s(j)}}(-1)^s\frac{n!}{\prod_j(l_j-N+s(j))!}\\
&=\frac{n!}{l_1!\cdots l_N!}\sum_{s\in S_N}(-1)^s\prod_j l_j(l_j-1)\cdots(l_j-N+s(j)+1)\\
&=\frac{n!}{\prod_j l_j!}\det\bigl(l_j(l_j-1)\cdots(l_j-N+i+1)\bigr).
\end{aligned}
$$

对此作列变换，再用 Vandermonde 行列式公式，可得

$$
\dim V_\lambda=\frac{n!}{\prod_j l_j!}\det(l_j^{N-i})=\frac{n!}{\prod_j l_j!}\prod_{1\le i<j\le N}(l_i-l_j).\tag{5.17.1}
$$

这里 $N\ge p$。

这个公式中可以作许多约分。约去其中一些因子，就得到钩长公式。具体地，对杨图 $\lambda$ 的一个方格 $(i,j)$（$i,j\ge1$，$i\le\lambda_j$），定义它的**钩**为 $\lambda$ 中所有满足 $i'\ge i$、$j'=j$，或 $i'=i$、$j'\ge j$ 的方格 $(i',j')$ 的集合。记 $h(i,j)$ 为这个钩的长度，也就是其中的方格数。

**定理 5.17.1（钩长公式）。** 有

$$
\dim V_\lambda=\frac{n!}{\prod_{i\le\lambda_j}h(i,j)}.
$$

**证明。** 该公式由公式 (5.17.1) 得到。注意到

$$
\frac{l_1!}{\prod_{1<j\le N}(l_1-l_j)}=\prod_{\substack{1\le k\le l_1,\\k\ne l_1-l_j}}k.
$$

容易看出，这个乘积中的因子恰好就是各个钩长 $h(i,1)$。删去杨图的第一行，再用归纳法即可。$\square$

## 5.18. $\mathfrak{gl}(V)$ 的 Schur–Weyl 对偶

先从一个简单的结果开始，它称为**双中心化子定理**。

<span class="original-page-anchor" id="pdf-page-128" aria-hidden="true"></span>

**定理 5.18.1。** 设 $A,B$ 是有限维向量空间 $E$ 的自同态代数 $\operatorname{End}E$ 的两个子代数，$A$ 半单，且 $B=\operatorname{End}_A E$。那么：

(i) $A=\operatorname{End}_B E$，也就是说，$A$ 的中心化子的中心化子就是 $A$。

(ii) $B$ 半单。

(iii) 作为 $A\otimes B$ 的表示，$E$ 有分解

$$
E=\bigoplus_{i\in I}V_i\otimes W_i,
$$

其中 $V_i$ 遍历 $A$ 的所有不可约表示，$W_i$ 遍历 $B$ 的所有不可约表示。特别地，$A$ 和 $B$ 的不可约表示之间有一个自然双射。

**证明。** 由于 $A$ 半单，有自然分解 $E=\bigoplus_{i\in I}V_i\otimes W_i$，其中 $W_i:=\operatorname{Hom}_A(V_i,E)$，且 $A=\bigoplus_i\operatorname{End}V_i$。因此，由 Schur 引理，$B=\operatorname{End}_A(E)$ 自然地等同于 $\bigoplus_i\operatorname{End}(W_i)$。定理的所有结论都由此得到。$\square$

现在把定理 5.18.1 应用于如下情形：$E=V^{\otimes n}$，其中 $V$ 是特征零代数闭域 $k$ 上的有限维向量空间，$A$ 是 $k[S_n]$ 在 $\operatorname{End}E$ 中的像。接下来刻画代数 $B$。把 $\operatorname{End}V$ 配上运算 $ab-ba$ 看作李代数，记为 $\mathfrak{gl}(V)$。

**译校注。** 原书先说底域是特征零的域，随后使用 $\mathbb C[S_n]$。依作者官方勘误，第 5.18、5.19 节统一在任意特征零代数闭域 $k$ 上讨论，原书这些地方的 $\mathbb C$ 相应改为 $k$。

**定理 5.18.2。** 代数 $B=\operatorname{End}_A E$ 是泛包络代数 $\mathcal U(\mathfrak{gl}(V))$ 在 $E$ 上自然作用的像。换句话说，$B$ 由形如

$$
\Delta_n(b):=b\otimes1\otimes\cdots\otimes1+1\otimes b\otimes\cdots\otimes1+\cdots+1\otimes1\otimes\cdots\otimes b,
$$

的元素生成，其中 $b\in\mathfrak{gl}(V)$。

**证明。** 显然，$\mathcal U(\mathfrak{gl}(V))$ 的像包含在 $B$ 中，所以只需证明 $B$ 的每个元素都属于 $\mathcal U(\mathfrak{gl}(V))$ 的像。由定义，$B=S^n\operatorname{End}V$，所以结论由下面引理的 (ii) 得到。

**引理 5.18.3。** 设 $k$ 是特征零的域。

<span class="original-page-anchor" id="pdf-page-129" aria-hidden="true"></span>

(i) 对于域 $k$ 上任意有限维向量空间 $U$，空间 $S^nU$ 由形如 $u\otimes\cdots\otimes u$（$u\in U$）的元素张成。

(ii) 对于域 $k$ 上任意代数 $A$，代数 $S^nA$ 由元素 $\Delta_n(a)$（$a\in A$）生成。

**证明。** (i) 空间 $S^nU$ 是 $GL(U)$ 的不可约表示（习题 4.12.3）。由 $u\otimes\cdots\otimes u$ 张成的子空间是非零子表示，因此必定是整个空间。

(ii) 由对称函数基本定理，存在有理系数多项式 $P$，使得

$$
P(H_1(x),\ldots,H_n(x))=x_1\cdots x_n
$$

（其中 $x=(x_1,\ldots,x_n)$）。于是

$$
P(\Delta_n(a),\Delta_n(a^2),\ldots,\Delta_n(a^n))=a\otimes\cdots\otimes a.
$$

其余结论由 (i) 得到。$\square$

这就完成了定理的证明。$\square$

由 Maschke 定理，代数 $A$ 是半单的，因此可以应用双中心化子定理，得到以下结果。这个结果称为“Schur–Weyl 对偶”：它由 Schur 发现，后来由 Weyl 在《群论与量子力学》和《经典群》中推广开来（见第 5.20 节）。

**定理 5.18.4。** (i) $k[S_n]$ 和 $\mathcal U(\mathfrak{gl}(V))$ 在 $\operatorname{End}(V^{\otimes n})$ 中的像 $A$ 和 $B$ 互为中心化子。

**译校注：** 原书此处写作 $\mathbb C[S_n]$。按作者 2024 年勘误，第 5.18、5.19 节的 $\mathbb C$ 应改为任意特征零代数闭域 $k$；以上据此修订。

(ii) $A$ 和 $B$ 都是半单的。特别地，$V^{\otimes n}$ 是半单 $\mathfrak{gl}(V)$-模。

(iii) 有如下 $(A\otimes B)$-模分解：

$$
V^{\otimes n}=\bigoplus_\lambda V_\lambda\otimes L_\lambda,
$$

其中求和遍历 $n$ 的所有分拆，$V_\lambda$ 是 $S_n$ 的 Specht 模，$L_\lambda$ 则是一些彼此不同的 $\mathfrak{gl}(V)$ 不可约表示，或为零。

<span class="original-page-anchor" id="pdf-page-130" aria-hidden="true"></span>

## 5.19. $GL(V)$ 的 Schur–Weyl 对偶

李代数 $\mathfrak{gl}(V)$ 的 Schur–Weyl 对偶蕴含群 $GL(V)$ 的一个类似结论。

**命题 5.19.1。** $GL(V)$ 在 $\operatorname{End}(V^{\otimes n})$ 中的像张成 $B$。

**证明。** 将 $g^{\otimes n}$（$g\in GL(V)$）张成的空间记为 $B'$，并任取 $b\in\operatorname{End}V$。

我们断言 $B'$ 包含 $b^{\otimes n}$。事实上，除有限多个 $t$ 值外，$t\cdot\mathrm{Id}+b$ 都可逆，因此 $(t\cdot\mathrm{Id}+b)^{\otimes n}$ 属于 $B'$。由于 $(t\cdot\mathrm{Id}+b)^{\otimes n}$ 是 $t$ 的多项式，上述结论对所有 $t$ 都成立，特别是对 $t=0$ 成立。

其余结论由引理 5.18.3 得到。$\square$

**推论 5.19.2。** 作为 $S_n\times GL(V)$ 的表示，$V^{\otimes n}$ 分解为 $\bigoplus_\lambda V_\lambda\otimes L_\lambda$，其中 $L_\lambda=\operatorname{Hom}_{S_n}(V_\lambda,V^{\otimes n})$ 是一些彼此不同的 $GL(V)$ 不可约表示，或为零。

**例 5.19.3。** 若 $\lambda=(n)$，则 $L_\lambda=S^nV$；若 $\lambda=(1^n)$（$n$ 个 $1$），则 $L_\lambda=\wedge^nV$。习题 4.12.3 已经证明这些表示确实不可约（不过，当 $n>\dim V$ 时，$\wedge^nV$ 为零）。

## 5.20. 历史插曲：限制与自由交汇处的 Hermann Weyl

Hermann Weyl（1885—1955）在哥廷根大学师从 David Hilbert，获得博士学位。后来，他给导师献上了一句颇有歧义的赞美，称 Hilbert 是“花衣魔笛手……诱惑那么多老鼠，跟着他跳进数学的深河”。Hilbert 将数学物理称为数学的“一根生命神经”，而 Weyl 也从导师那里继承了让数学与物理相互促进的兴趣（引自 [53，第 357、358 页]）。哥廷根的数学家愿意投身物理问题，让自己的公式沾上泥土，这使他们有别于柏林数学学派那种执着的纯粹主义。

<span class="original-page-anchor" id="pdf-page-131" aria-hidden="true"></span>

1913 年，苏黎世联邦理工学院向 Weyl 提供了教授职位，尽管 Frobenius 的推荐多少有些冷淡。在 Frobenius 看来，所有出自哥廷根学派的候选人的工作都“非常一般，非常深刻，深刻得简直像无底深渊，以至于像我这样目光短浅的人，很难辨认出什么新思想”（引自 [22，第 421 页]）。Weyl 接受了聘请，并与当时在那里任教的 Albert Einstein 成了同事。不过，直到一场世界大战，Weyl 才开始留意 Einstein 正在做什么。德国政府起初判定 Weyl 的身体状况不适合参加第一次世界大战，但随着伤亡不断增加，政府重新界定了什么叫身体合格，将他拉上了战场。Weyl 与德国军队的这番相遇，几乎没让任何一方满意。1916 年，应瑞士政府的请求，Weyl 获准退伍，回到联邦理工学院继续工作。他后来回忆道：“我的数学头脑和任何退伍军人一样，一片空白，不知道该做什么。我开始研究代数曲面；但还没走多远，Einstein 的论文就到了我手上，让我热血沸腾。”（引自 [52，第 62 页]）这篇点燃他热情的论文，正是 Einstein 对广义相对论的论述。

1917 年，Weyl 在联邦理工学院开设了广义相对论课程，随后很快将讲稿写成广为流传的《空间—时间—物质》。这本书五年内出了四个不同的版本，连 Einstein 本人也赞叹它是一部“交响乐般的杰作”（引自 [46，第 65 页]）。然而，Weyl 几乎无法克制改进 Einstein 那套费力的数学表述的冲动。他确信，Einstein 理论所依据的黎曼几何并不是一种始终贯彻无穷小思想的几何，于是着手创建“纯粹的无穷小几何”。有一次，他向一名学生解释，在黎曼几何中，向量平行移动后的方向取决于所走的路径。学生天真地问，向量的长度是否也会改变。Weyl 回忆道：“当然，当时我给了他正统的答案，可是疑问却在我心中啃噬。”（引自 [52，第 154 页]）正统的答案是“不会”，但他很想看看，如果长度真的取决于路径，会发生什么。Weyl 质疑了黎曼几何中隐含的固定距离尺度，即“规范”的假设，并得到了一种更一般的几何，其中规范因子在<span class="original-page-anchor" id="pdf-page-132" aria-hidden="true"></span>时空中逐点变化，就像 20 世纪初各国的铁路轨距并不相同一样 [42，第 3 页]。

Weyl 渴望建立统一场论，把引力场与电磁场统一起来。Einstein 很高兴 Weyl 成为广义相对论的支持者，但看到他在构造物理理论方面与自己竞争，热情就少了许多。Einstein 称赞 Weyl 的理论是“最高层次的天才之笔”，又总结道：“除了与现实相符这一点之外，无论如何，它都是思想的一项宏伟成就。”（引自 [52，第 163—164 页]）作为一个真正的数学家，Weyl 很难认同 Einstein 对“现实”的执着。他后来说道：“现在显然必须给‘在现实中’这几个字加上引号；我们拥有的是一种符号构造，却没有任何东西能让我们认真宣称，那就是真实的现实世界。”（引自 [42，第 15 页]）在回复 Einstein 时，Weyl 针锋相对地写道：“必须强调，从数学的观点看，这里发展出来的几何才是真正的局部几何。如果自然界实现的并不是这种真正的（几何），而是一种片面的、不自洽的局部几何，再把电磁场粘在上面，那就奇怪了。”在讽刺的程度上，Weyl 轻易就能与 Einstein 匹敌：“如果你对现实世界的看法是正确的，那我很遗憾，不得不向亲爱的上帝指出一个数学上的不自洽之处。”（引自 [22，第 434 页]）

Weyl 将 Einstein 广义相对论的张量语言放进哥廷根学派的框架中重新塑造，专注于发展张量代数，尤其是具有物理应用所需的特定对称性质的张量。他希望从数学上统观各种可能的对称类型，并在 Frobenius 的有限群表示理论中找到了合适的观察角度。渐渐地，Weyl 越来越远离相对论，转向群论中纯粹数学的问题，试图为张量演算建立群论基础。借助 Élie Cartan 和 Issai Schur 的工作，Weyl 深入研究有限群表示论，称其为“数学中最精彩的理论之一”。Weyl 与 Schur 通信，<span class="original-page-anchor" id="pdf-page-133" aria-hidden="true"></span>Schur 写道：“我非常想看看，如何以 Cartan 的方法为基础，推导出我最近关于变量数目与特征标的结果。”（引自 [22，第 456、473 页]）Weyl 欣然应允，很快将 Élie Cartan 的无穷小方法与 Issai Schur 的整体方法结合起来。不过，他并未止步于重新推导 Schur 的结果，而是更进一步，建立了单李群表示的完整理论，包括不可约特征标和相应表示维数的显式公式。

量子力学的兴起，给了 Weyl 挑战数学连续统霸主地位的机会。他相信，数学的不同分支可能有不同的数概念，并赞同这样的观点：“每一个交由数学分析处理的对象，都带着它自身的一类数。这些数应当根据对象及其内在组成来定义，而不是用同一个先验构造、独立于应用的普遍数系去处理每一个对象。”（引自 [52，第 240 页]）在 1928 年的《群论与量子力学》中，Weyl 主张，量子力学核心的对称性，其本质应当到群论概念中去寻找，而非实数连续统中，尤其应当到对称置换群与一般线性群的表示之间的“互反性”中去寻找 [60，第 vii 页]。

物理学界以愤怒与厌恶的呼声，迎接这位数学家的帮助。美国理论物理学家 John Slater 将 Weyl 及其追随者的方法命名为“Gruppenpest”，也就是“群论之疫”。他后来坦承：“‘群论之疫’的作者们写出的论文，让像我这样没有学过群论的人无法理解。”在他看来，他们的成果“微不足道”；他向其他物理学家广泛讲述自己“令人沮丧、无愧于瘟疫之名的经历”，并声称他们“和我一样，厌恶用群论的方法处理这个问题”（引自 [55，第 x 页]）。甚至到了<span class="original-page-anchor" id="pdf-page-134" aria-hidden="true"></span>1975 年，他仍然相信自己已经“消灭了‘Gruppenfest’”，浑然不知群论在基本粒子物理中的重要应用如今已成为日常工作的一部分。

那些态度较友善的物理学家，理解 Weyl 的数学时也颇感吃力，但这反而加深了他们对他的敬仰。Julian Schwinger 不得不承认，自己“从未——哪怕直到今天——完全掌握”Weyl 的《群论与量子力学》。然而，他称 Weyl 为“我的神之一”，并解释说：“神的行事方式神秘莫测，难以窥透，超出了凡人的理解。”有人问 Paul Dirac 是否遇到过无法理解的学者，他毫不犹豫地回答：“Weyl。”然而，Weyl 关于电子与反电子必须具有相同质量的纯数学论证，又让他信服得无话可说。据说，正是这次接触使他得出了那句著名的格言：“让方程具有美，比让方程符合实验更重要。”（引自 [42，第 11、19、12 页]）Weyl 对数学也表达过类似感受：“我的工作一直试图把真与美结合起来；而当我必须二选一时，我通常选择美。”（引自 [45，第 161 页]）

Weyl 于 1930 年返回哥廷根，接任 Hilbert 的教席，却不幸正赶上纳粹势力上升。一位同时代的人私下评论说：“Weyl 教授是一个奇特的种族混合体，至少有七份荷尔斯泰因血统和一份犹太血统，带着荷尔斯泰因和弗里斯兰人身上较常见的那种特有的血管舒缩易激惹性。”（引自 [49，第 52 页]）无论他血液中的德国成分可能造成什么血管舒缩障碍，和他的犹太血统在纳粹德国可能带来的麻烦相比，都显然微不足道。虽然 Weyl 的犹太血统比例较低，使他免于纳粹的直接攻击，但他的妻子和孩子却会成为反犹措施的目标。Weyl 才刚回到祖国，就不得不再次面对移居国外的可能。这是一个艰难的决定。起初，他拒绝了普林斯顿高等研究院的邀请，因为他无法克服“那份将我的每一根心弦都系在德语上的爱”（引自 [52，第<span class="original-page-anchor" id="pdf-page-135" aria-hidden="true"></span>271 页]）。但 Hitler 上台之后，Weyl 的理智战胜了情感，一家人离开欧洲，前往美国。

来到普林斯顿后，Weyl 置身于一种数学文化之中，这种文化对他珍爱的思辨哲学很不友好。他察觉到，美国的数学研究存在“过分彻底的专业化与技术化的危险”，由此形成的“写作方式，必定让读者觉得自己被关在一间灯光明亮的牢房里，每个细节都以同样眩目的清晰程度凸显出来，却没有层次的变化”。Weyl 自己更喜欢“晴朗天空下开阔的景色，有着深远的透视感，近处丰富而轮廓分明的细节，朝着地平线逐渐隐去”[57，第 viii 页]。

1939 年，Weyl 一边与写作时套在身上的“外语枷锁”搏斗，一边在《经典群》中总结了自己关于群不变量和表示的成果 [57，第 viii 页]。正如 Michael Atiyah 爵士所指出的，这本书“不是一本沿直线展开、有开头、中间和结尾的书。它更像一幅精细的画作，必须从不同的角度、在不同的光线下加以研究。它让学生绝望，却让教授欣喜”[3，第 328 页]。

Weyl 将自己的数学著作既视为科学作品，也视为艺术作品。他坦承：“我自己的数学工作总是相当缺乏系统，没有固定的方式，也没有联系。表达和形式对我来说，几乎比知识本身更重要。但我相信，即使撇开我个人的特殊性格，数学本身也具有一种与实验学科不同、更接近自由创造艺术的特质。”（引自 [3，第 323 页]）Weyl 相信：“‘数学化’很可能是人类的一种创造性活动，如同语言或音乐，具有最根本的原创性，而其中历史上的选择，无法被完全客观地合理化。”[58，第 550 页]

Weyl 在数学创造的艺术性中，在公式的美中，在数学的永恒真理中，寻找庇护，以躲避世界大战的恐怖和欧洲文化的毁灭 [53，第 365 页]。然而，广岛事件之后，他意识到，即使优美的公式也可能用于致命的目的。他问道：“理论家应当而且能够在多大程度上，为自己的发现所产生的实际后果承担责任？量子物理是一座何等美丽的理论大厦，<span class="original-page-anchor" id="pdf-page-136" aria-hidden="true"></span>而原子弹又是何等可怕的东西！”Weyl 不赞同 G. H. Hardy 对纯数学的辩护，即将纯数学看作一种无用而无害的、对美的追求。Weyl 坚持认为，“误用数学所带来的致命威胁”，使数学自身的意义与价值都受到质疑（引自 [49，第 67—68 页]）。他在数学中看到了与现实生活中相同的道德选择。他早先对知识的“形而上学含义”的思考，如今获得了更广泛的意义。他曾写道：“数学并不是外行很容易在其中看到的那种僵硬而乏味的图式。相反，在数学中，我们恰好站在限制与自由的交汇点上，而这正是人自身的本质。”[59，第 68 页]

## 5.21. Schur 多项式

设 $\lambda=(\lambda_1,\ldots,\lambda_p)$ 是 $n$ 的一个分拆，且 $N\geq p$。令

$$
D_\lambda(x)=\sum_{s\in S_N}(-1)^s\prod_{j=1}^N x_{s(j)}^{\lambda_j+N-j}=\det(x_i^{\lambda_j+N-j}).
$$

定义多项式

$$
S_\lambda(x):=\frac{D_\lambda(x)}{D_0(x)}
$$

（显然，$D_0(x)$ 就是 $\Delta(x)$）。容易看出，这些确实是多项式，因为 $D_\lambda$ 是反对称的，因而必定能被 $\Delta$ 整除。多项式 $S_\lambda$ 称为 **Schur 多项式**。

**命题 5.21.1。**

$$
\prod_m(x_1^m+\cdots+x_N^m)^{i_m}=\sum_{\lambda:p\leq N}\chi_\lambda(C_i)S_\lambda(x).
$$

**证明。** 这个等式可由 Frobenius 特征标公式及

$$
\Delta(x)\prod_m(x_1^m+\cdots+x_N^m)^{i_m}
$$

的反对称性得到。$\square$

Schur 多项式的某些特殊值很重要。具体而言，有如下结论。

<span class="original-page-anchor" id="pdf-page-137" aria-hidden="true"></span>

**命题 5.21.2。**

$$
S_\lambda(1,z,z^2,\ldots,z^{N-1})=\prod_{1\leq i<j\leq N}\frac{z^{\lambda_i-i}-z^{\lambda_j-j}}{z^{-i}-z^{-j}}.
$$

因此，

$$
S_\lambda(1,\ldots,1)=\prod_{1\leq i<j\leq N}\frac{\lambda_i-\lambda_j+j-i}{j-i}.
$$

**证明。** 第一个等式由定义结合 Vandermonde 行列式得到；在第一个等式中令 $z=1$，便得到第二个等式。$\square$

## 5.22. $L_\lambda$ 的特征标

命题 5.21.1 使我们能够计算表示 $L_\lambda$ 的特征标。

具体地，设 $\dim V=N$，$g\in GL(V)$，并设 $x_1,\ldots,x_N$ 是 $g$ 在 $V$ 上的特征值。为了计算特征标 $\chi_{L_\lambda}(g)$，我们先计算 $\operatorname{Tr}_{V^{\otimes n}}(g^{\otimes n}s)$，其中 $s\in S_n$。若 $s\in C_i$，容易得到这个迹等于

$$
\prod_m\operatorname{Tr}(g^m)^{i_m}=\prod_m H_m(x)^{i_m}.
$$

另一方面，由 Schur–Weyl 对偶，

$$
\operatorname{Tr}_{V^{\otimes n}}(g^{\otimes n}s)=\sum_\lambda\chi_\lambda(C_i)\operatorname{Tr}_{L_\lambda}(g).
$$

将其与命题 5.21.1 比较，并利用 $S_n$ 的特征标表各列的线性无关性，得到如下结论。

**定理 5.22.1（Weyl 特征标公式）。** 表示 $L_\lambda$ 为零，当且仅当 $N<p$，其中 $p$ 是 $\lambda$ 的部分数。若 $N\geq p$，则 $L_\lambda$ 的特征标是 Schur 多项式 $S_\lambda(x)$。因此，$L_\lambda$ 的维数由以下公式给出：

$$
\dim L_\lambda=\prod_{1\leq i<j\leq N}\frac{\lambda_i-\lambda_j+j-i}{j-i}.
$$

<span class="original-page-anchor" id="pdf-page-138" aria-hidden="true"></span>

这表明，出现在某个 $V^{\otimes n}$ 中的 $GL(V)$ 不可约表示，可由杨图来标记。杨图的格子数可以任意，但行数至多为 $N=\dim V$。

**命题 5.22.2。** 表示 $L_{\lambda+1^N}$（其中 $1^N=(1,1,\ldots,1)\in\mathbb Z^N$）同构于 $L_\lambda\otimes\wedge^NV$。

**证明。** 事实上，$L_\lambda\otimes\wedge^NV\subset V^{\otimes n}\otimes\wedge^NV\subset V^{\otimes(n+N)}$，而 $V^{\otimes(n+N)}$ 中唯一与 $L_\lambda\otimes\wedge^NV$ 具有相同特征标的分量是 $L_{\lambda+1^N}$。由此得到结论。$\square$

## 5.23. $GL(V)$ 的代数表示

**定义 5.23.1。** 若 $GL(V)$ 的有限维表示 $Y$ 的矩阵元都是 $g,g^{-1}$（$g\in GL(V)$）的各矩阵元的多项式函数，即属于 $k[g_{ij}][1/\det(g)]$，就称 $Y$ 为**代数表示**，也称**有理表示**或**多项式表示**。

例如，$V^{\otimes n}$ 是代数表示，因此所有 $L_\lambda$ 也都是代数表示。再定义 $L_{\lambda-r\cdot1^N}:=L_\lambda\otimes(\wedge^NV^*)^{\otimes r}$（由命题 5.22.2，这个定义是有意义的）。这也是代数表示。因此，对于任何满足 $\lambda_1\geq\cdots\geq\lambda_N$ 的整数序列 $(\lambda_1,\ldots,\lambda_N)$（这些整数不必为正），我们都赋予了它一个唯一的 $GL(V)=GL_N$ 不可约代数表示 $L_\lambda$。这个序列称为 $L_\lambda$ 的**最高权**。

**定理 5.23.2。** (i) $GL(V)$ 的每个有限维代数表示都完全可约，并分解为形如 $L_\lambda$ 的直和项（这些表示两两不同构）。

(ii) （*$GL(V)$ 的 Peter–Weyl 定理*）设 $R$ 是 $GL(V)$ 上的多项式函数代数。将 $R$ 看成 $GL(V)\times GL(V)$ 的表示，作用为 $(\rho(g,h)\phi)(x)=\phi(g^{-1}xh)$，其中 $g,h,x\in GL(V)$、$\phi\in R$，则有分解

$$
R=\bigoplus_\lambda L_\lambda^*\otimes L_\lambda,
$$

其中求和遍历所有 $\lambda$。

**证明。** (i) 设 $Y$ 是 $GL(V)$ 的代数表示。由 $(u,\xi(v))(g):=u(gv)$（$u\in Y^*$）可定义一个嵌入 $\xi:Y\to Y\otimes R$。

<span class="original-page-anchor" id="pdf-page-139" aria-hidden="true"></span>

容易看出，$\xi$ 是表示同态（这里 $GL(V)$ 在 $Y\otimes R$ 的第一个因子上的作用是平凡的）。因此，只需对一个子表示 $Y\subset R^m$ 证明这个定理。$R$ 的每个元素都是 $g_{ij}$ 的一个多项式乘以 $\det(g)$ 的一个非正整数次幂。因此，$R$ 是若干形如 $S^r(V\otimes V^*)\otimes(\wedge^NV^*)^{\otimes s}$ 的表示的直和的商，其中群在乘积 $V\otimes V^*$ 的 $V^*$ 因子上的作用是平凡的。于是，可以假设 $Y$ 包含在这种表示的有限直和的一个商中。因此，$Y$ 包含在若干形如 $V^{\otimes n}\otimes(\wedge^NV^*)^{\otimes s}$ 的表示的直和中，证明完成。

**译校注：** 作者 2024 年勘误重写了原书第 131 页这段证明：补明 $V\otimes V^*$ 中 $V^*$ 上的群作用平凡，并删除此处原有的 $V^*=\wedge^{N-1}V\otimes\wedge^NV^*$ 论证步骤。以上按勘误修订；英文校录保留原书内容。

(ii) 设 $Y$ 是 $GL(V)$ 的代数表示，并通过 $(\rho(h)\phi)(x)=\phi(xh)$ 将 $R$ 看成 $GL(V)$ 的表示。

那么 $\operatorname{Hom}_{GL(V)}(Y,R)$ 就是 $GL(V)$ 上取值于 $Y^*$ 的、满足 $GL(V)$ 等变性的多项式函数 $f$ 所构成的空间；等变条件为 $f(xg)=g^{-1}f(x)$。这个空间自然地与 $Y^*$ 等同。结合 (i) 的证明，可知 $R$ 具有所需的分解，并且这个分解与 $GL(V)$ 的第二个作用（左乘作用）相容。由此得到结论。$\square$

**译校注：** 原书的等变条件写作 $f(gx)=gf(x)$；以上按作者 2024 年勘误改为 $f(xg)=g^{-1}f(x)$，与这里的右乘作用相符。

**注 5.23.3。** $V$ 上的无迹算子构成的李代数 $\mathfrak{sl}(V)$，是 $\mathfrak{gl}(V)$ 对标量算子取商得到的。因此，上述结果可以直接推广到李代数 $\mathfrak{sl}(V)$ 的表示。同样，关于 $GL(V)$ 的结果也可推广到由行列式为 $1$ 的算子构成的群 $SL(V)$。唯一的区别是，在这种情况下，表示 $L_\lambda$ 与 $L_{\lambda+1^N}$ 同构，因此不可约表示由整数序列 $\lambda_1\geq\cdots\geq\lambda_N$ 参数化，但同时给各项加上同一个常数视为等价。

**译校注：** 原书此处写作 $1^m$，与前文的 $N=\dim V$ 不一致；这里改为 $1^N$，即在全部 $N$ 个分量上同时加 $1$。

特别地，可以证明，$\mathfrak{sl}(V)$ 的任何有限维表示都完全可约，任何不可约表示都形如 $L_\lambda$（这里不作证明）。当 $\dim V=2$ 时，就重新得到习题 2.15.1 中研究过的 $\mathfrak{sl}(2)$ 的表示论。

## 5.24. 习题

**习题 5.24.1。** (a) 证明 $S_n$ 的表示

$$
V'_\lambda:=\mathbb C[S_n]b_\lambda a_\lambda
$$

同构于 $V_\lambda$。

<span class="original-page-anchor" id="pdf-page-140" aria-hidden="true"></span>

提示：用公式 $f(x)=xa_\lambda$ 和 $g(y)=yb_\lambda$ 定义 $S_n$-同态 $f:V_\lambda\to V'_\lambda$ 与 $g:V'_\lambda\to V_\lambda$，并证明，除去一个非零标量因子，它们互为逆映射。

(b) 设 $\phi:\mathbb C[S_n]\to\mathbb C[S_n]$ 是将每个置换 $s$ 映到 $(-1)^ss$ 的自同构。证明，$\phi$ 将 $S_n$ 的任意表示 $V$ 变为 $V\otimes\mathbb C_-$。再证明，对于 $a\in\mathbb C[S_n]$，有 $\phi(\mathbb C[S_n]a)=\mathbb C[S_n]\phi(a)$。利用 (a) 推出 $V_\lambda\otimes\mathbb C_-=V_{\lambda^*}$，其中 $\lambda^*$ 是 $\lambda$ 的共轭分拆，由反射 $\lambda$ 的杨图得到。

**习题 5.24.2。** 设 $R_{k,N}$ 是复 $N\times N$ 矩阵的 $k$ 元组 $X_1,\ldots,X_k$ 所构成的空间上，在同时共轭作用下不变的多项式的代数。例如，函数 $T_w:=\operatorname{Tr}(w(X_1,\ldots,X_k))$ 属于 $R_{k,N}$，其中 $w$ 是由 $k$ 个字母组成的字母表上的任意有限词。证明，$R_{k,N}$ 由元素 $T_w$ 生成。

提示：考虑对每个 $X_i$ 的次数均为 $d_i$ 的不变函数，将这个空间实现为张量积 $\bigotimes_i S^{d_i}(V\otimes V^*)$。然后，将这个张量积嵌入 $(V\otimes V^*)^{\otimes n}=\operatorname{End}(V)^{\otimes n}$，并利用 Schur–Weyl 对偶得到结论。

**译校注：** 原书最后一句左端的张量幂指数写作 $N$；以上按作者 2024 年勘误改为 $n$，与右端一致。

## 5.25. $GL_2(\mathbb F_q)$ 的表示

**5.25.1. $GL_2(\mathbb F_q)$ 中的共轭类。** 设 $\mathbb F_q$ 是一个含 $q$ 个元素、特征不为 $2$ 的有限域，并令 $G=GL_2(\mathbb F_q)$。则

$$
|G|=(q^2-1)(q^2-q),
$$

因为可逆 $2\times2$ 矩阵的第一列必须非零，而第二列不能是第一列的倍数。分解因子，得到

$$
|GL_2(\mathbb F_q)|=q(q+1)(q-1)^2.
$$

本节的目标是描述 $G$ 的不可约表示。

<span class="original-page-anchor" id="pdf-page-141" aria-hidden="true"></span>

首先，来确定 $GL_2(\mathbb F_q)$ 中的共轭类。

| 代表元 | 每个共轭类的元素数 | 共轭类的数目 |
| --- | --- | --- |
| 标量型 $\begin{pmatrix}x&0\\0&x\end{pmatrix}$ | $1$（这是中心元素） | $q-1$（每个非零 $x$ 对应一个） |
| 抛物型 $\begin{pmatrix}x&1\\0&x\end{pmatrix}$ | $q^2-1$（与它交换的元素形如 $\begin{pmatrix}t&u\\0&t\end{pmatrix}$，$t\ne0$） | $q-1$（每个非零 $x$ 对应一个） |
| 双曲型 $\begin{pmatrix}x&0\\0&y\end{pmatrix}$，$y\ne x$ | $q^2+q$（与它交换的元素形如 $\begin{pmatrix}t&0\\0&u\end{pmatrix}$，$t,u\ne0$） | $\frac12(q-1)(q-2)$（$x,y\ne0$ 且 $x\ne y$） |
| 椭圆型 $\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}$，$x\in\mathbb F_q$，$y\in\mathbb F_q^\times$，$\varepsilon\in\mathbb F_q\setminus\mathbb F_q^2$（在 $\mathbb F_q$ 上的特征多项式不可约） | $q^2-q$（原因将在下文说明） | $\frac12q(q-1)$（参数为 $y$ 与 $-y$ 的矩阵互相共轭） |

下面更详细地说明*椭圆型*矩阵的共轭类结构。这些矩阵的特征多项式在 $\mathbb F_q$ 上不可约，因此在 $\mathbb F_q$ 中没有特征值。设 $A$ 是这样的矩阵，并考虑 $\mathbb F_q$ 的一个二次扩域 $\mathbb F_q(\sqrt\varepsilon)$，其中 $\varepsilon\in\mathbb F_q\setminus\mathbb F_q^2$。在这个域上，$A$ 的特征值为

$$
\alpha=\alpha_1+\sqrt\varepsilon\alpha_2
$$

和

$$
\overline\alpha=\alpha_1-\sqrt\varepsilon\alpha_2,
$$

相应的特征向量为

$$
v,\ \overline v\qquad(Av=\alpha v,\ A\overline v=\overline\alpha\overline v).
$$

<span class="original-page-anchor" id="pdf-page-142" aria-hidden="true"></span>

选取基

$$
\{e_1=v+\overline v,\ e_2=\sqrt\varepsilon(v-\overline v)\}.
$$

在这组基下，矩阵 $A$ 具有形式

$$
\begin{pmatrix}\alpha_1&\varepsilon\alpha_2\\\alpha_2&\alpha_1\end{pmatrix},
$$

这就说明了为何该共轭类的代表元可以写成前述形式。

在基 $\{v,\overline v\}$ 下，与 $A$ 交换的矩阵形如

$$
\begin{pmatrix}\lambda&0\\0&\overline\lambda\end{pmatrix},
$$

其中

$$
\lambda\in\mathbb F_{q^2}^\times
$$

可以任取，因此这种矩阵共有 $q^2-1$ 个。

**5.25.2. 一维表示。** 首先描述 $G$ 的一维表示。

**命题 5.25.1。** $[G,G]=SL_2(\mathbb F_q)$。

**证明。** 显然，

$$
\det(xyx^{-1}y^{-1})=1,
$$

因此

$$
[G,G]\subseteq SL_2(\mathbb F_q).
$$

要证明反向包含，只需证明矩阵

$$
\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix},\quad\begin{pmatrix}1&0\\1&1\end{pmatrix}
$$

都是交换子，因为这类矩阵生成 $SL_2(\mathbb F_q)$。显然，利用转置，只需证明前两个矩阵是交换子。容易看出，矩阵

$$
\begin{pmatrix}1&1\\0&1\end{pmatrix}
$$

是矩阵

$$
A=\begin{pmatrix}1&1/2\\0&1\end{pmatrix},\quad B=\begin{pmatrix}1&0\\0&-1\end{pmatrix}
$$

的交换子，<span class="original-page-anchor" id="pdf-page-143" aria-hidden="true"></span>而矩阵

$$
\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix}
$$

是矩阵

$$
A=\begin{pmatrix}a&0\\0&1\end{pmatrix},\quad B=\begin{pmatrix}0&1\\1&0\end{pmatrix}
$$

的交换子。这就完成了证明。$\square$

因此，通过 $g\mapsto\det(g)$ 有同构

$$
G/[G,G]\cong\mathbb F_q^\times.
$$

所以 $G$ 的一维表示形如

$$
\rho(g)=\xi(\det(g)),
$$

其中 $\xi$ 是同态

$$
\xi:\mathbb F_q^\times\to\mathbb C^\times.
$$

因此，这种表示共有 $q-1$ 个，记为 $\mathbb C_\xi$。

**5.25.3. 主系列表示。** 令

$$
B\subset G,\quad B=\left\{\begin{pmatrix}*&*\\0&*\end{pmatrix}\right\}
$$

（即上三角矩阵的集合）。则

$$
|B|=(q-1)^2q,
$$

$$
[B,B]=U=\left\{\begin{pmatrix}1&*\\0&1\end{pmatrix}\right\},
$$

并且

$$
B/[B,B]\cong\mathbb F_q^\times\times\mathbb F_q^\times
$$

（这个同构将 $B$ 的元素映到它的两个对角元）。设同态

$$
\lambda:B\to\mathbb C^\times
$$

由公式

$$
\lambda\begin{pmatrix}a&b\\0&c\end{pmatrix}=\lambda_1(a)\lambda_2(c)
$$

定义，<span class="original-page-anchor" id="pdf-page-144" aria-hidden="true"></span>其中 $\lambda_1,\lambda_2:\mathbb F_q^\times\to\mathbb C^\times$ 是一对同态。定义

$$
V_{\lambda_1,\lambda_2}=\operatorname{Ind}_B^G\mathbb C_\lambda,
$$

其中 $\mathbb C_\lambda$ 是 $B$ 的一维表示，$B$ 在其上通过 $\lambda$ 作用。有

$$
\dim(V_{\lambda_1,\lambda_2})=\frac{|G|}{|B|}=q+1.
$$

**定理 5.25.2。** (1) 若 $\lambda_1\ne\lambda_2$，则 $V_{\lambda_1,\lambda_2}$ 不可约。

(2) 若 $\lambda_1=\lambda_2=\mu$，则 $V_{\lambda_1,\lambda_2}=\mathbb C_\mu\oplus W_\mu$，其中 $W_\mu$ 是 $G$ 的一个 $q$ 维不可约表示。

(3) $W_\mu\cong W_\nu$ 当且仅当 $\mu=\nu$；$V_{\lambda_1,\lambda_2}\cong V_{\lambda'_1,\lambda'_2}$ 当且仅当 $\{\lambda_1,\lambda_2\}=\{\lambda'_1,\lambda'_2\}$（后一种情形中，$\lambda_1\ne\lambda_2$ 且 $\lambda'_1\ne\lambda'_2$）。

**证明。** 由 Frobenius 公式，

$$
\operatorname{Tr}_{V_{\lambda_1,\lambda_2}}(g)=\frac1{|B|}\sum_{a\in G,\ aga^{-1}\in B}\lambda(aga^{-1}).
$$

若

$$
g=\begin{pmatrix}x&0\\0&x\end{pmatrix},
$$

则右端的值为

$$
\lambda(g)\frac{|G|}{|B|}=\lambda_1(x)\lambda_2(x)(q+1).
$$

若

$$
g=\begin{pmatrix}x&1\\0&x\end{pmatrix},
$$

则右端的值为

$$
\lambda(g)\cdot1,
$$

因为此时 $aga^{-1}\in B\Rightarrow a\in B$。

若

$$
g=\begin{pmatrix}x&0\\0&y\end{pmatrix},
$$

则右端的值为

$$
(\lambda_1(x)\lambda_2(y)+\lambda_1(y)\lambda_2(x))\cdot1,
$$

<span class="original-page-anchor" id="pdf-page-145" aria-hidden="true"></span>

因为此时 $aga^{-1}\in B$ 蕴含 $a\in B$，或者 $a$ 是 $B$ 中的一个元素乘以转置矩阵。

若

$$
g=\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix},\quad y\ne0,
$$

**译校注：** 原书在上面的椭圆型矩阵旁写作 $x\ne y$。应为 $y\ne0$，与第 5.25.1 节表中的条件一致；在 $\varepsilon$ 非平方的假设下，这才保证其特征多项式在 $\mathbb F_q$ 上不可约。英文校录保留原式。

则右端的值为 $0$，因为这类矩阵在 $\mathbb F_q$ 上没有特征值，因此不能共轭到 $B$ 中。由定义，$i=1,2$ 时，$\lambda_i(x)$ 是单位根，所以

$$
\begin{aligned}
|G|\langle\chi_{V_{\lambda_1,\lambda_2}},\chi_{V_{\lambda_1,\lambda_2}}\rangle
&=(q+1)^2(q-1)+(q^2-1)(q-1)\\
&\quad+2(q^2+q)\frac{(q-1)(q-2)}2\\
&\quad+(q^2+q)\sum_{x\ne y}\lambda_1(x)\lambda_2(y)\overline{\lambda_1(y)\lambda_2(x)}.
\end{aligned}
$$

最后两个加项来自展开式

$$
|a+b|^2=|a|^2+|b|^2+a\overline b+\overline a b.
$$

若

$$
\lambda_1=\lambda_2=\mu,
$$

则最后一项等于

$$
(q^2+q)(q-2)(q-1),
$$

于是，这种情形下的总和为

$$
\begin{aligned}
&(q+1)(q-1)[(q+1)+(q-1)+2q(q-2)]\\
&\qquad=(q+1)(q-1)2q(q-1)=2|G|,
\end{aligned}
$$

因此

$$
\langle\chi_{V_{\lambda_1,\lambda_2}},\chi_{V_{\lambda_1,\lambda_2}}\rangle=2.
$$

显然，

$$
\mathbb C_\mu\subseteq\operatorname{Ind}_B^G\mathbb C_{\mu,\mu},
$$

因为

$$
\operatorname{Hom}_G(\mathbb C_\mu,\operatorname{Ind}_B^G\mathbb C_{\mu,\mu})=\operatorname{Hom}_B(\mathbb C_\mu,\mathbb C_\mu)=\mathbb C
$$

（定理 5.10.1）。因此，$\operatorname{Ind}_B^G\mathbb C_{\mu,\mu}=\mathbb C_\mu\oplus W_\mu$，且 $W_\mu$ 不可约。不同 $\mu$ 值对应的 $W_\mu$ 的特征标不同，故这些 $W_\mu$ 彼此不同。

若 $\lambda_1\ne\lambda_2$，令 $z=xy^{-1}$。那么，求和中的最后一项为

$$
\begin{aligned}
&(q^2+q)\sum_{x\ne y}\lambda_1(z)\overline{\lambda_2(z)}\\
&\qquad=(q^2+q)\sum_{x;\ z\ne1}\frac{\lambda_1}{\lambda_2}(z)
=(q^2+q)(q-1)\sum_{z\ne1}\frac{\lambda_1}{\lambda_2}(z).
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-146" aria-hidden="true"></span>

由于任意给定阶数 $m>1$ 的全部单位根之和为零，有

$$
\sum_{z\in\mathbb F_q^\times}\frac{\lambda_1}{\lambda_2}(z)=0,
$$

因此最后一项变为

$$
-(q^2+q)(q-1)\frac{\lambda_1}{\lambda_2}(1)=-(q^2+q)(q-1).
$$

$\lambda_1=\lambda_2$ 的情形与这一情形的差等于

$$
(q^2+q)[(q-2)(q-1)+(q-1)]=|G|,
$$

故由引理 5.7.2，这个表示不可约。

**译校注：** 原书等式左端有一个负号；按作者 2024 年勘误将其删去，差值取为相等情形减去不相等情形。修订后两边均为正的群阶 $|G|$。

为证明定理的第三个断言，考察双曲型元素上的特征标，并注意到函数

$$
\lambda_1(x)\lambda_2(y)+\lambda_1(y)\lambda_2(x)
$$

可以确定 $\lambda_1,\lambda_2$，只差一个交换次序。$\square$

**译校注：** 作者 2024 年勘误还在本小节末补充：$V_{\lambda_1,\lambda_2}$ 与 $W_\mu$ 称为主系列表示。

**5.25.4. 补系列表示。** 设 $\mathbb F_{q^2}\supset\mathbb F_q$ 是二次扩域 $\mathbb F_q(\sqrt\varepsilon)$，其中 $\varepsilon\in\mathbb F_q\setminus\mathbb F_q^2$。将它看作 $\mathbb F_q$ 上的二维向量空间，则 $G$ 就是 $\mathbb F_{q^2}$ 在 $\mathbb F_q$ 上的线性变换群。设 $K\subset G$ 是由乘以 $\mathbb F_{q^2}^\times$ 中的元素所构成的循环群，

$$
K=\left\{\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}\right\},\qquad |K|=q^2-1.
$$

对于同态 $\nu:K\to\mathbb C^\times$，令

$$
Y_\nu=\operatorname{Ind}_K^G\mathbb C_\nu.
$$

当然，这个表示可约。利用 Frobenius 公式计算它的特征标，得到

$$
\chi\begin{pmatrix}x&0\\0&x\end{pmatrix}=q(q-1)\nu(x),
$$

当 $A$ 为抛物型或双曲型时，

$$
\chi(A)=0,
$$

并且

$$
\chi\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}
=\nu\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}
+\nu\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}^{q}.
$$

<span class="original-page-anchor" id="pdf-page-147" aria-hidden="true"></span>

最后一个等式成立，是因为若将矩阵看作 $\mathbb F_{q^2}$ 的元素，共轭就是 $\mathbb F_{q^2}$ 在 $\mathbb F_q$ 上的一个自同构，而这个扩域唯一的非平凡自同构就是取 $q$ 次幂的映射。

于是有

$$
\operatorname{Ind}_K^G\mathbb C_{\nu^q}\cong\operatorname{Ind}_K^G\mathbb C_\nu,
$$

因为它们的特征标相同。因此，在 $\nu^q\ne\nu$ 时，我们得到 $\frac12q(q-1)$ 个表示。

接下来考察张量积

$$
W_1\otimes V_{\alpha,1},
$$

其中 $1$ 是平凡特征标，$W_1$ 按上一小节的方式定义。这个表示的特征标为

$$
\chi\begin{pmatrix}x&0\\0&x\end{pmatrix}=q(q+1)\alpha(x),
$$

当 $A$ 为抛物型或椭圆型时，

$$
\chi(A)=0,
$$

并且

$$
\chi\begin{pmatrix}x&0\\0&y\end{pmatrix}=\alpha(x)+\alpha(y).
$$

因此，“虚表示”

$$
W_1\otimes V_{\alpha,1}-V_{\alpha,1}-\operatorname{Ind}_K^G\mathbb C_\nu
$$

的特征标为

$$
\chi\begin{pmatrix}x&0\\0&x\end{pmatrix}=(q-1)\alpha(x),
$$

$$
\chi\begin{pmatrix}x&1\\0&x\end{pmatrix}=-\alpha(x),
$$

$$
\chi\begin{pmatrix}x&0\\0&y\end{pmatrix}=0,
$$

$$
\chi\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}
=-\nu\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}
-\nu^q\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix},
$$

其中 $\alpha$ 是 $\nu$ 在标量上的限制。

以下始终假设 $\nu^q\ne\nu$。

下面两个引理将证明，这个特征标与自身的内积等于 $1$，并且它在 $1$ 处的值为<span class="original-page-anchor" id="pdf-page-148" aria-hidden="true"></span>正。由引理 5.7.2 可知，这两个性质意味着它是 $G$ 的一个不可约表示的特征标。

**引理 5.25.3。** 设 $\chi$ 是上面定义的虚表示的特征标。则

$$
\langle\chi,\chi\rangle=1
$$

且

$$
\chi(1)>0.
$$

**证明。**

$$
\chi(1)=q(q+1)-(q+1)-q(q-1)=q-1>0.
$$

现在计算内积 $\langle\chi,\chi\rangle$。由于 $\alpha$ 是单位根，这个内积等于

$$
\begin{aligned}
\frac1{(q-1)^2q(q+1)}\Big[&(q-1)\cdot(q-1)^2\cdot1+(q-1)\cdot1\cdot(q^2-1)\\
&+\frac{q(q-1)}2\cdot\sum_{\zeta\text{ 椭圆型}}(\nu(\zeta)+\nu^q(\zeta))\overline{(\nu(\zeta)+\nu^q(\zeta))}\Big].
\end{aligned}
$$

由于 $\nu$ 也是单位根，表达式的最后一项化为

$$
\sum_{\zeta\text{ 椭圆型}}(2+\nu^{q-1}(\zeta)+\nu^{1-q}(\zeta)).
$$

来计算最后一个加项。

由于 $\mathbb F_{q^2}^\times$ 是循环群，且 $\nu^q\ne\nu$，有

$$
\sum_{\zeta\in\mathbb F_{q^2}^\times}\nu^{q-1}(\zeta)=\sum_{\zeta\in\mathbb F_{q^2}^\times}\nu^{1-q}(\zeta)=0.
$$

因此，

$$
\begin{aligned}
\sum_{\zeta\text{ 椭圆型}}(\nu^{q-1}(\zeta)+\nu^{1-q}(\zeta))
&=-\sum_{\zeta\in\mathbb F_q^\times}(\nu^{q-1}(\zeta)+\nu^{1-q}(\zeta))\\
&=-2(q-1),
\end{aligned}
$$

因为 $\mathbb F_q^\times$ 是一个 $q-1$ 阶循环群。所以，

$$
\begin{aligned}
\langle\chi,\chi\rangle=\frac1{(q-1)^2q(q+1)}\Big(&(q-1)\cdot(q-1)^2\cdot1+(q-1)\cdot1\cdot(q^2-1)\\
&+\frac{q(q-1)}2\cdot(2(q^2-q)-2(q-1))\Big)=1.
\end{aligned}
$$

$\square$<span class="original-page-anchor" id="pdf-page-149" aria-hidden="true"></span>我们已经证明：只要 $\nu^q\ne\nu$，就存在不可约表示 $Y_\nu$，其特征标与

$$
W_1\otimes V_{\alpha,1}-V_{\alpha,1}-\operatorname{Ind}_K^G\mathbb C_\nu
$$

的特征标相同。不同的数对 $(\alpha,\nu)$ 给出不同的特征标，唯一需要合并的是 $\nu$ 与 $\nu^q$。因此，这样的表示共有 $\frac{q(q-1)}2$ 个，每个的维数都是 $q-1$。

**译校注：** 根据作者的官方勘误，上述表示称为补系列表示。

至此，我们找到了 $G$ 的 $q-1$ 个一维表示、$\frac{q(q-1)}2$ 个主系列表示，以及 $\frac{q(q-1)}2$ 个补系列表示，总计 $q^2-1$ 个表示。这个数恰好等于 $G$ 的共轭类数，所以我们实际上已经找到了 $GL_2(\mathbb F_q)$ 的全部不可约表示。

## 5.26. Artin 定理

**定理 5.26.1.** 设 $X$ 是有限群 $G$ 的一个在共轭下不变的子群族。以下两个条件等价：

(i) $G$ 中的每个元素都属于某个子群 $H\in X$。

(ii) $G$ 的每个不可约表示的特征标，都属于诱导表示 $\operatorname{Ind}_H^G V$ 的特征标在 $\mathbb Q$ 上的线性张成空间，其中 $H\in X$，$V$ 是 $H$ 的不可约表示。

**注 5.26.2.** 将定理 5.26.1 的条件 (ii) 中的 $\mathbb Q$ 上的线性张成空间换成 $\mathbb C$ 上的线性张成空间，得到的条件与原条件等价。事实上，对各个 $H,V$，将 $\operatorname{Ind}_H^G V$ 按 $G$ 的不可约表示分解，再将分解的系数作为矩阵的各列。这两个条件都等价于这个矩阵的各行线性无关。

**证明.** *先证明 (ii) 推出 (i)。* 假设 $g\in G$ 不属于任何子群 $H\in X$。由于 $X$ 在共轭下不变，$g$ 也不可能通过共轭变换进入这样的子群。由 Frobenius 公式，对所有 $H\in X$ 和 $V$ 都有 $\chi_{\operatorname{Ind}_H^G(V)}(g)=0$。于是根据 (ii)，$G$ 的任意不可约表示 $W$ 都满足 $\chi_W(g)=0$。然而，不可约特征标张成类函数空间，这就意味着每个类函数在 $g$ 处都为零，矛盾。

*再证明 (i) 推出 (ii)。* 设 $U$ 是 $G$ 在 $\mathbb C$ 上的一个虚表示，也就是不可约表示的线性组合，其中<span class="original-page-anchor" id="pdf-page-150" aria-hidden="true"></span>系数是非零整数，并且对所有 $H,V$ 都满足 $(\chi_U,\chi_{\operatorname{Ind}_H^G V})=0$。由 Frobenius 互反性，$(\chi_{U|_H},\chi_V)=0$。这意味着，对每个 $H\in X$，$\chi_U$ 在 $H$ 上都为零。由 (i)，$\chi_U$ 恒等于零。结合注 5.26.2，这就推出了 (ii)。$\square$

**推论 5.26.3.** 有限群的任意不可约特征标，都是从它的循环子群诱导得到的特征标的有理线性组合。

## 5.27. 半直积的表示

设 $G,A$ 是两个群，$\phi:G\to\operatorname{Aut}(A)$ 是群同态。对 $a\in A$，将 $\phi(g)a$ 记作 $g(a)$。**半直积** $G\ltimes A$ 定义为集合 $A\times G$，其乘法为

$$
(a_1,g_1)(a_2,g_2)=(a_1g_1(a_2),g_1g_2).
$$

显然，$G$ 和 $A$ 自然地成为 $G\ltimes A$ 的子群。

我们想研究 $G\ltimes A$ 的不可约复表示。为简单起见，先考虑 $A$ 是阿贝尔群的情况。

这时，$A$ 的不可约表示都是一维的，并构成特征标群 $A^\vee$，而 $G$ 作用在这个群上。设 $O$ 是这一作用的一个轨道，从中选定一个元素 $x\in O$，并记 $x$ 在 $G$ 中的稳定子为 $G_x$。设 $U$ 是 $G_x$ 的一个不可约表示。我们如下定义 $G\ltimes A$ 的表示 $V_{(O,U)}$。

先将它作为 $G$ 的表示，令

$$
V_{(O,x,U)}=\operatorname{Ind}_{G_x}^G U=\{f:G\to U\mid f(hg)=hf(g),\ h\in G_x\}.
$$

再用 $(af)(g)=x(g(a))f(g)$ 在这个空间上定义 $A$ 的作用。容易验证，这两个作用合在一起就给出了 $G\ltimes A$ 的作用。此外，这个表示在如下意义下与 $x$ 的选择无关：设 $x,y\in O$，$g\in G$ 满足 $gx=y$；将 $G_x$ 的表示 $U$ 经 $g$ 的作用变成 $G_y$ 的表示，记所得表示为 $g(U)$。那么 $V_{(O,x,U)}$ 与 $V_{(O,y,g(U))}$ 自然同构。因此，我们将 $V_{(O,x,U)}$ 记作 $V_{(O,U)}$，但仍须记住 $x$ 已经选定。

**定理 5.27.1.** (i) 表示 $V_{(O,U)}$ 都是不可约的。

<span class="original-page-anchor" id="pdf-page-151" aria-hidden="true"></span>

(ii) 它们两两不同构。

(iii) 它们给出了 $G\ltimes A$ 的全部不可约表示。

(iv) $V=V_{(O,U)}$ 的特征标由下面的 Frobenius 型公式给出：

$$
\chi_V(a,g)=\frac1{|G_x|}\sum_{h\in G:\,hgh^{-1}\in G_x}x(h(a))\chi_U(hgh^{-1}).
$$

**证明.** (i) 将 $V=V_{(O,U)}$ 作为 $A$-模分解，得到

$$
V=\bigoplus_{y\in O}V_y,
$$

其中 $V_y=\{v\in V_{(O,U)}\mid av=y(a)v,\ a\in A\}$。等价地，$V_y$ 由满足以下条件的 $v\in V_{(O,U)}$ 组成：除非 $gy=x$，否则 $v(g)=0$。

**译校注：** 原书这里写作 $(y,a)$；根据作者的官方勘误，应为 $y(a)$，即特征标 $y$ 在 $a$ 处的值。

因此，若 $W\subset V$ 是子表示，就有 $W=\bigoplus_{y\in O}W_y$，其中 $W_y\subset V_y$。现在，$V_y$ 是 $G_y$ 的表示；由任何将 $x$ 映到 $y$ 的元素 $g\in G$ 所确定的同构 $G_y\to G_x$，都会将这个表示变为 $U$。所以 $V_y$ 作为 $G_y$ 的表示是不可约的，对每个 $y$ 都有 $W_y=0$ 或 $W_y=V_y$。此外，若 $hy=z$，则 $hW_y=W_z$。于是，要么所有 $W_y$ 都为零，要么所有 $W_y$ 都等于 $V_y$，这就证明了所需结论。

(ii) $V$ 的 $A$-模结构确定了轨道 $O$，而 $V_x$ 的 $G_x$-模结构确定了表示 $U$。

(iii) 有

$$
\begin{aligned}
\sum_{U,O}\dim V_{(U,O)}^2
&=\sum_{U,O}|O|^2(\dim U)^2\\
&=\sum_O|O|^2|G_x|=\sum_O|O||G/G_x||G_x|\\
&=|G|\sum_O|O|=|G||A^\vee|=|G\ltimes A|.
\end{aligned}
$$

(iv) 证明与 Frobenius 公式的证明基本相同。$\square$

**练习 5.27.2.** 用定理 5.27.1 重新解习题 4.12.1(a)、4.12.2 和 4.12.6。

**练习 5.27.3.** 从定理 5.27.1 的 (iv) 推出 (i)–(iii)。

[^pdf122-1]: 当 $j>p$ 时，规定 $\lambda_j=0$。
