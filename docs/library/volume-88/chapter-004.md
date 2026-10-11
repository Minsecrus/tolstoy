---
title: "第四章 有限群的表示：基本结果"
description: "《Introduction to Representation Theory》中文译文。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"第三章 表示论的一般结果","link":"/library/volume-88/chapter-003"}
next: {"text":"第五章 有限群的表示：进一步的结果","link":"/library/volume-88/chapter-005"}
---

# 第四章 有限群的表示：基本结果

<span class="original-page-anchor" id="pdf-page-67" aria-hidden="true"></span>

回顾一下，群 $G$ 在域 $k$ 上的一个**表示**，由一个 $k$-向量空间 $V$ 和一个群同态 $\rho:G\to GL(V)$ 组成。正如前面所述，群 $G$ 在 $k$ 上的表示，与其群代数 $k[G]$ 的表示是一回事。

从本章开始，我们系统地研究有限群的表示论。

## 4.1. Maschke 定理

**定理 4.1.1（Maschke）。** 设 $G$ 是有限群，域 $k$ 的特征不整除 $|G|$。那么：

(i) 代数 $k[G]$ 是半单的。

(ii) 有代数同构 $\psi:k[G]\to\bigoplus_i\operatorname{End}V_i$，由 $g\mapsto\bigoplus_i g|_{V_i}$ 给出，其中 $V_i$ 是 $G$ 的不可约表示。特别地，这也是 $G$ 的表示的同构，这里 $G$ 在两侧都以左乘作用。因此，正则表示 $k[G]$ 分解为不可约表示的直和 $\bigoplus_i\dim(V_i)V_i$，并且有“平方和公式”

$$
|G|=\sum_i\dim(V_i)^2.
$$

<span class="original-page-anchor" id="pdf-page-68" aria-hidden="true"></span>

**证明。** 由命题 3.5.8，(i) 蕴含 (ii)。为了证明 (i)，只需证明：如果 $V$ 是 $G$ 的一个有限维表示，$W\subset V$ 是任意子表示，那么存在子表示 $W'\subset V$，使 $V=W\oplus W'$ 作为表示成立。

在 $V$ 中任取 $W$ 的一个补空间 $\widehat{W}$。这样，$V=W\oplus\widehat{W}$ 作为向量空间成立，但作为表示未必成立。令 $P$ 为沿 $\widehat{W}$ 到 $W$ 的投影，即 $V$ 上满足 $P|_W=\operatorname{Id}$、$P|_{\widehat{W}}=0$ 的算子。令

$$
\overline{P}:=\frac{1}{|G|}\sum_{g\in G}\rho(g)P\rho(g^{-1}),
$$

其中 $\rho(g)$ 是 $g$ 在 $V$ 上的作用，并令

$$
W'=\ker\overline{P}.
$$

现在，$\overline{P}|_W=\operatorname{Id}$，且 $\overline{P}(V)\subseteq W$，所以 $\overline{P}^2=\overline{P}$，从而 $\overline{P}$ 是沿 $W'$ 的投影。因此，$V=W\oplus W'$ 作为向量空间成立。

此外，对任意 $h\in G$ 和任意 $y\in W'$，有

$$
\begin{aligned}
\overline{P}\rho(h)y&=\frac{1}{|G|}\sum_{g\in G}\rho(g)P\rho(g^{-1}h)y\\
&=\frac{1}{|G|}\sum_{\ell\in G}\rho(h\ell)P\rho(\ell^{-1})y=\rho(h)\overline{P}y=0,
\end{aligned}
$$

所以 $\rho(h)y\in\ker\overline{P}=W'$。因此，$W'$ 在 $G$ 的作用下不变，故是 $V$ 的子表示。这样，$V=W\oplus W'$ 就是所需的子表示直和分解。$\square$

定理 4.1.1(i) 的逆命题也成立。

**命题 4.1.2.** 如果 $k[G]$ 是半单的，那么 $k$ 的特征不整除 $|G|$。

**证明。** 写成 $k[G]=\bigoplus_{i=1}^r\operatorname{End}V_i$，其中 $V_i$ 是不可约表示，$V_1=k$ 是一维平凡表示。那么

$$
k[G]=k\oplus\bigoplus_{i=2}^r\operatorname{End}V_i=k\oplus\bigoplus_{i=2}^r d_iV_i,
$$

<span class="original-page-anchor" id="pdf-page-69" aria-hidden="true"></span>

其中 $d_i=\dim V_i$。由舒尔引理，

$$
\operatorname{Hom}_{k[G]}(k,k[G])=k\Lambda,
\qquad \operatorname{Hom}_{k[G]}(k[G],k)=k\epsilon,
$$

这里 $\epsilon:k[G]\to k$ 和 $\Lambda:k\to k[G]$ 是非零表示同态，除相差一个非零倍数外都是唯一的。可以选取 $\epsilon$，使所有 $g\in G$ 都满足 $\epsilon(g)=1$；也可以选取 $\Lambda$，使 $\Lambda(1)=\sum_{g\in G}g$。于是

$$
\epsilon\circ\Lambda(1)=\epsilon\left(\sum_{g\in G}g\right)=\sum_{g\in G}1=|G|.
$$

若 $|G|=0$，那么 $\Lambda$ 没有左逆，因为对任意 $a\in k$，都有 $(a\epsilon)\circ\Lambda(1)=0$。这就产生了矛盾。$\square$

**例 4.1.3。** 若 $G=\mathbb Z/p\mathbb Z$，且 $k$ 的特征为 $p$，那么 $G$ 在 $k$ 上的每个不可约表示都是平凡表示（因此 $k[\mathbb Z/p\mathbb Z]$ 确实不是半单的）。事实上，这个群的不可约表示是一维空间，生成元在其上的作用是乘以某个 $p$ 次单位根。但 $k$ 中的每个 $p$ 次单位根都等于 $1$，因为在 $k$ 上有 $x^p-1=(x-1)^p$。

**习题 4.1.4。** 设 $G$ 是一个阶为 $p^n$ 的群。证明：$G$ 在特征为 $p$ 的域 $k$ 上的每个不可约表示都是平凡表示。

## 4.2 特征标

若 $V$ 是有限群 $G$ 的有限维表示，其特征标 $\chi_V:G\to k$ 定义为 $\chi_V(g)=\operatorname{Tr}|_V(\rho(g))$。

显然，$\chi_V(g)$ 就是将 $V$ 作为代数 $A=k[G]$ 的表示时的特征标 $\chi_V(a)$ 限制到基 $G\subset A$ 上，因此包含的信息完全相同。特征标是一个**中心函数**，也称**类函数**：$\chi_V(g)$ 只依赖于 $g$ 的共轭类；也就是说，$\chi_V(hgh^{-1})=\chi_V(g)$。

用 $F(G,k)$ 表示 $G$ 上的 $k$ 值函数空间，用 $F_c(G,k)\subset F(G,k)$ 表示其中由类函数组成的子空间。

**定理 4.2.1。** *若 $k$ 的特征不整除 $|G|$，那么 $G$ 的不可约表示的特征标构成空间 $F_c(G,k)$ 的一组基。*

<span class="original-page-anchor" id="pdf-page-70" aria-hidden="true"></span>

**证明。** 由 Maschke 定理，$k[G]$ 是半单代数。因此，根据定理 3.6.2，这些特征标线性无关，并构成 $(A/[A,A])^*$ 的一组基，其中 $A=k[G]$。只需注意，作为 $k$ 上的向量空间，

$$
\begin{aligned}
(A/[A,A])^*&\cong\{\varphi\in\operatorname{Hom}_k(k[G],k)\mid gh-hg\in\ker\varphi\ \forall g,h\in G\}\\
&\cong\{f\in F(G,k)\mid f(gh)=f(hg)\ \forall g,h\in G\},
\end{aligned}
$$

而这恰好就是 $F_c(G,k)$。$\square$

**推论 4.2.2。** *$G$ 的不可约表示的同构类个数，等于 $G$ 的共轭类个数（假设 $|G|$ 在 $k$ 中不为零）。*

**练习 4.2.3。** 证明：若 $|G|$ 在 $k$ 中为零，那么 $G$ 在 $k$ 上的不可约表示的同构类个数，严格小于 $G$ 的共轭类个数。

提示：令 $P=\sum_{g\in G}g\in k[G]$。则 $P^2=0$。因此，在 $G$ 的每个有限维 $k$ 表示中，$P$ 的迹都为零。

**推论 4.2.4。** *若 $k$ 的特征为 $0$，则 $G$ 的任意有限维表示都由其特征标确定；也就是说，$\chi_V=\chi_W$ 蕴含 $V\cong W$。*

**译校注：** 原书推论 4.2.4 中“任意表示”应为“任意有限维表示”；此处按作者官方勘误补上“有限维”。

## 4.3 例子

下面给出有限群在 $\mathbb C$ 上的若干表示。

(1) 有限阿贝尔群 $G=\mathbb Z_{n_1}\times\cdots\times\mathbb Z_{n_k}$。设 $G^\vee$ 是 $G$ 的不可约表示所成的集合。$G$ 的每个元素单独构成一个共轭类，所以 $|G^\vee|=|G|$。回顾一下：交换代数和交换群在 $\mathbb C$ 上（更一般地，在代数闭域上）的所有不可约表示都是一维的。因此，$G^\vee$ 是一个阿贝尔群：若 $\rho_1,\rho_2:G\to\mathbb C^\times$ 是不可约表示，那么 $\rho_1(g)\rho_2(g)$ 和 $\rho_1(g)^{-1}$ 也都是不可约表示。群 $G^\vee$ 称为 $G$ 的**对偶群**或**特征标群**。

给定 $n\ge1$，定义 $\rho:\mathbb Z_n\to\mathbb C^\times$，令 $\rho(m)=e^{2\pi im/n}$。则 $\mathbb Z_n^\vee=\{\rho^k:k=0,\ldots,n-1\}$，所以 $\mathbb Z_n^\vee\cong\mathbb Z_n$。一般地，

$$
(G_1\times G_2\times\cdots\times G_n)^\vee=G_1^\vee\times G_2^\vee\times\cdots\times G_n^\vee,
$$

因此，任意有限阿贝尔群 $G$ 都满足 $G^\vee\cong G$。不过，这个同构不是典范的：将 $G$ 具体分解为<span class="original-page-anchor" id="pdf-page-71" aria-hidden="true"></span>$\mathbb Z_{n_1}\times\cdots\times\mathbb Z_{n_k}$ 时，$G$ 中哪些元素对应于 $\mathbb Z_{n_1}$ 等因子，这种对应并不唯一。另一方面，$G\cong(G^\vee)^\vee$ 是一个典范同构，由映射 $\varphi:G\to(G^\vee)^\vee$ 给出，其中 $\varphi(g)(\chi)=\chi(g)$。

(2) 对称群 $S_3$。在对称群 $S_n$ 中，共轭类由循环分解中的循环长度确定：两个置换共轭，当且仅当它们对每一种长度都具有相同个数的循环。$S_3$ 有三个共轭类，所以它在 $\mathbb C$ 上有三个不同的不可约表示。若这些表示的维数为 $d_1,d_2,d_3$，则 $d_1^2+d_2^2+d_3^2=6$，因此 $S_3$ 必有两个一维表示和一个二维表示。一维表示分别是由 $\rho(\sigma)=1$ 给出的平凡表示 $\mathbb C_+$，以及由 $\rho(\sigma)=(-1)^\sigma$ 给出的符号表示 $\mathbb C_-$。

这个二维表示可以直观地看成等边三角形的对称作用，三角形的顶点 $1,2,3$ 分别位于坐标平面上的 $(\cos120^\circ,\sin120^\circ)$、$(\cos240^\circ,\sin240^\circ)$、$(1,0)$。例如，

$$
\rho((12))=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\rho((123))=\begin{pmatrix}\cos120^\circ&-\sin120^\circ\\\sin120^\circ&\cos120^\circ\end{pmatrix}.
$$

为了证明这个表示不可约，任取一个子表示 $V$。空间 $V$ 必须由 $\rho((12))$ 的一部分特征向量张成，而这些特征向量就是 $(1,0)$ 和 $(0,1)$ 的非零倍数。同时，$V$ 也必须由 $\rho((123))$ 的一部分特征向量张成，但它的特征向量不同。因此，$V$ 只能是 $\mathbb C^2$ 或 $0$。

(3) 四元数群 $Q_8=\{\pm1,\pm i,\pm j,\pm k\}$，其定义关系为

$$
i=jk=-kj,\quad j=ki=-ik,\quad k=ij=-ji,\quad -1=i^2=j^2=k^2.
$$

它的五个共轭类为 $\{1\}$、$\{-1\}$、$\{\pm i\}$、$\{\pm j\}$、$\{\pm k\}$，所以有五个不同的不可约表示。这些表示的维数平方和等于 $8$，因而维数必为 $1$、$1$、$1$、$1$ 和 $2$。

中心 $Z(Q_8)$ 为 $\{\pm1\}$，且 $Q_8/Z(Q_8)\cong\mathbb Z_2\times\mathbb Z_2$。$\mathbb Z_2\times\mathbb Z_2$ 的四个一维不可约表示可以“拉回”到 $Q_8$。也就是说，若 $q:Q_8\to Q_8/Z(Q_8)$ 是商映射，并且<span class="original-page-anchor" id="pdf-page-72" aria-hidden="true"></span>$\rho$ 是 $Q_8/Z(Q_8)$ 的任意表示，那么 $\rho\circ q$ 就给出了 $Q_8$ 的一个表示。

二维表示为 $V=\mathbb C^2$，由 $\rho(-1)=-\operatorname{Id}$ 和以下公式给出：

$$
\begin{aligned}
\rho(i)&=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\\
\rho(j)&=\begin{pmatrix}\sqrt{-1}&0\\0&-\sqrt{-1}\end{pmatrix},\\
\rho(k)&=\begin{pmatrix}0&-\sqrt{-1}\\-\sqrt{-1}&0\end{pmatrix}.
\end{aligned}\tag{4.3.1}
$$

这些是量子力学中出现的 Pauli 矩阵。

**练习 4.3.1。** 证明：$Q_8$ 的二维不可约表示可以实现在满足 $f(ig)=\sqrt{-1}f(g)$ 的函数 $f:Q_8\to\mathbb C$ 所成的空间中（$G$ 通过右乘作用，即 $g\circ f(x)=f(xg)$）。

**译校注：** 原书练习的条件写为 $f(gi)=\sqrt{-1}f(g)$，这个条件不被所给的右平移作用保持。此处改为 $f(ig)=\sqrt{-1}f(g)$，保留原书的右平移作用。

(4) 对称群 $S_4$。$S_4$ 的阶为 $24$，有五个共轭类，代表元为 $e$、$(12)$、$(123)$、$(1234)$、$(12)(34)$。因此，五个不可约表示的维数平方和为 $24$。与 $S_3$ 一样，其中有两个一维表示：平凡表示 $\mathbb C_+$ 和符号表示 $\mathbb C_-$。其余三个表示的维数必为 $2$、$3$ 和 $3$。由于 $S_3\cong S_4/\mathbb Z_2\times\mathbb Z_2$，其中 $\mathbb Z_2\times\mathbb Z_2$ 为 $\{e,(12)(34),(13)(24),(14)(23)\}$，所以可以将 $S_3$ 的二维表示拉回为 $S_4$ 的二维表示，记作 $\mathbb C^2$。

可以把 $S_4$ 看成一个立方体的旋转群，它通过置换立方体的体对角线来作用（等价地，也可以看成在正八面体上置换各对相对面的作用）。这就给出了三维表示 $\mathbb C_+^3$。

最后一个三维表示为 $\mathbb C_-^3$，它是 $\mathbb C_+^3$ 与符号表示的乘积。$\mathbb C_+^3$ 和 $\mathbb C_-^3$ 不同，因为若 $g$ 是一个对换，则 $\det g|_{\mathbb C_+^3}=1$，而 $\det g|_{\mathbb C_-^3}=(-1)^3=-1$。注意，$\mathbb C_-^3$ 还可以通过 $S_4$ 对正四面体的对称作用（不一定是旋转）来实现。这个表示还可以实现在一个含有<span class="original-page-anchor" id="pdf-page-73" aria-hidden="true"></span>四个元素的集合上的函数空间中，其中函数值之和为零，$S_4$ 通过置换这些元素来作用。

## 4.4 表示的对偶与张量积

若 $V$ 是群 $G$ 的表示，那么 $V^*$ 也通过下式成为一个表示：

$$
\rho_{V^*}(g)=(\rho_V(g)^*)^{-1}=(\rho_V(g)^{-1})^*=\rho_V(g^{-1})^*.
$$

其特征标为 $\chi_{V^*}(g)=\chi_V(g^{-1})$。

有 $\chi_V(g)=\sum\lambda_i$，其中 $\lambda_i$ 是 $g$ 在 $V$ 上作用的特征值。假设 $G$ 有限，这些特征值必为单位根，因为 $\rho(g)^{|G|}=\rho(g^{|G|})=\rho(e)=\operatorname{Id}$。

**译校注：** 原书这里未说明 $G$ 有限；作者官方勘误补充了这一条件，只有在此条件下才能作上述推断。

因此，对复表示有

$$
\chi_{V^*}(g)=\chi_V(g^{-1})=\sum\lambda_i^{-1}=\sum\overline{\lambda_i}=\overline{\sum\lambda_i}=\overline{\chi_V(g)}.
$$

特别地，$V$ 与 $V^*$ *作为表示*同构（不仅作为向量空间同构），当且仅当所有 $g\in G$ 都满足 $\chi_V(g)\in\mathbb R$。

若 $V,W$ 是 $G$ 的表示，则 $V\otimes W$ 也通过下式成为一个表示：

$$
\rho_{V\otimes W}(g)=\rho_V(g)\otimes\rho_W(g).
$$

因此，$\chi_{V\otimes W}(g)=\chi_V(g)\chi_W(g)$。

下面将讨论一个有趣的问题：当 $V,W$ 不可约时，如何将 $V\otimes W$ 分解成不可约表示的直和。

## 4.5 特征标的正交性

在中心函数空间 $F_c(G,\mathbb C)$ 上定义正定 Hermitian 内积

$$
(f_1,f_2)=\frac1{|G|}\sum_{g\in G}f_1(g)\overline{f_2(g)}.
$$

下面的定理说明，在这个内积下，$G$ 的不可约表示的特征标构成 $F_c(G,\mathbb C)$ 的一组标准正交基。

<span class="original-page-anchor" id="pdf-page-74" aria-hidden="true"></span>

**定理 4.5.1。** *对任意表示 $V,W$，有*

$$
(\chi_V,\chi_W)=\dim\operatorname{Hom}_G(W,V).
$$

*若 $V,W$ 不可约，则*

$$
(\chi_V,\chi_W)=\begin{cases}1,&\text{若 }V\cong W,\\0,&\text{若 }V\not\cong W.\end{cases}
$$

**证明。** 根据定义，

$$
\begin{aligned}
(\chi_V,\chi_W)&=\frac1{|G|}\sum_{g\in G}\chi_V(g)\overline{\chi_W(g)}=\frac1{|G|}\sum_{g\in G}\chi_V(g)\chi_{W^*}(g)\\
&=\frac1{|G|}\sum_{g\in G}\chi_{V\otimes W^*}(g)=\operatorname{Tr}|_{V\otimes W^*}(P),
\end{aligned}
$$

其中 $P=\frac1{|G|}\sum_{g\in G}g\in Z(\mathbb C[G])$。（这里 $Z(\mathbb C[G])$ 表示 $\mathbb C[G]$ 的中心。）若 $X$ 是 $G$ 的不可约表示，则

$$
P|_X=\begin{cases}\operatorname{Id},&\text{若 }X=\mathbb C,\\0,&X\ne\mathbb C.\end{cases}
$$

因此，对任意表示 $X$，算子 $P|_X$ 是到 $X$ 的 $G$ 不变向量子空间 $X^G$ 上的 $G$ 不变投影。于是

$$
\begin{aligned}
\operatorname{Tr}|_{V\otimes W^*}(P)&=\dim\operatorname{Hom}_G(\mathbb C,V\otimes W^*)\\
&=\dim(V\otimes W^*)^G=\dim\operatorname{Hom}_G(W,V).
\end{aligned}
$$

$\square$

定理 4.5.1 提供了一个有效方法，可以判断有限群 $G$ 的给定复表示 $V$ 是否不可约。事实上，它说明 $V$ 不可约，当且仅当 $(\chi_V,\chi_V)=1$。

**习题 4.5.2。** 设 $G$ 是有限群，$V_i$ 为 $G$ 的各个不可约复表示。

对每个 $i$，令

$$
\psi_i=\frac{\dim V_i}{|G|}\sum_{g\in G}\chi_{V_i}(g)\cdot g^{-1}\in\mathbb C[G].
$$

<span class="original-page-anchor" id="pdf-page-75" aria-hidden="true"></span>

(i) 证明：$\psi_i$ 在 $V_j$ 上的作用，当 $j=i$ 时是恒等映射，当 $j\ne i$ 时是零映射。

(ii) 证明：$\psi_i$ 是**幂等元**；即对任意 $i$ 都有 $\psi_i^2=\psi_i$，对任意 $i\ne j$ 都有 $\psi_i\psi_j=0$。

提示：在 (i) 中，注意 $\psi_i$ 与 $k[G]$ 的任意元素交换，因此在 $V_j$ 上作为交织算子作用。由推论 2.3.10，$\psi_i$ 在 $V_j$ 上的作用是乘以某个标量。计算它在 $V_j$ 中的迹，即可求出这个标量。

**注 4.5.3。** 可见，$G$ 的不可约复表示的特征标可以不借助不可约表示来定义。具体地，在 $G$ 上的复值函数空间 $F(G,\mathbb C)$ 上定义卷积乘积

$$
(f*g)(z)=\sum_{x,y\in G:xy=z}f(x)g(y).
$$

这个乘积使 $F(G,\mathbb C)$ 成为结合代数，单位元是 $\delta_e$（群单位元 $e\in G$ 的示性函数），而类函数空间 $F_c(G,\mathbb C)$ 是其中的一个交换子代数。随后，可以把重归一化的特征标 $\widetilde\chi_i\in F_c(G,\mathbb C)$ 定义为这个代数中的本原幂等元，即方程 $f*f=f$ 的解中，不能分解成其他非零解之和的那些解。再用公式

$$
\chi_i(g)=\sqrt{\frac{|G|}{\widetilde\chi_i(1)}}\widetilde\chi_i(g)
$$

定义特征标（请自行验证！）。Frobenius 定义特征标时，本质上采用的就是这种方法（见 [Cu]，公式 (7)）。注意，Frobenius 大约在同一时期也定义了表示，但在一段时间里，人们还不清楚不可约表示与特征标之间存在一个简单的关系：不可约特征标其实就是群元素在不可约表示中的迹。即使到了今天，许多群论学家有时也会谈论有限群的不可约特征标，而不是不可约表示。

下面给出特征标的另一个“正交公式”，其中对不可约表示求和，而不是对群元素求和。

<span class="original-page-anchor" id="pdf-page-76" aria-hidden="true"></span>

**定理 4.5.4。** *设 $g,h\in G$，用 $Z_g$ 表示 $g$ 在 $G$ 中的中心化子。则*

$$
\sum_V\chi_V(g)\overline{\chi_V(h)}=\begin{cases}|Z_g|,&\text{若 }g\text{ 与 }h\text{ 共轭},\\0,&\text{其他情形},\end{cases}
$$

*其中求和遍历 $G$ 的所有不可约表示。*

**证明。** 如上所述，$\overline{\chi_V(h)}=\chi_{V^*}(h)$，所以利用 Maschke 定理，左端等于

$$
\begin{aligned}
\sum_V\chi_V(g)\chi_{V^*}(h)&=\operatorname{Tr}|_{\bigoplus_V V\otimes V^*}(g\otimes(h^*)^{-1})\\
&=\operatorname{Tr}|_{\bigoplus_V\operatorname{End}V}(x\mapsto gxh^{-1})=\operatorname{Tr}|_{\mathbb C[G]}(x\mapsto gxh^{-1}).
\end{aligned}
$$

若 $g$ 与 $h$ 不共轭，这个迹显然为零，因为算子 $x\mapsto gxh^{-1}$ 在群元素构成的基下的矩阵，其对角元全为零。另一方面，若 $g$ 与 $h$ 属于同一个共轭类，这个迹就等于满足 $x=gxh^{-1}$ 的元素 $x$ 的个数，即 $g$ 的中心化子 $Z_g$ 的阶。证毕。$\square$

**注 4.5.5。** 这个结论还有下面的证明。考虑矩阵 $U$，其行由 $G$ 的不可约表示标记，列由共轭类标记，矩阵元为 $U_{V,g}=\chi_V(g)/\sqrt{|Z_g|}$。注意，$g$ 的共轭类为 $G/Z_g$；因此，$|G|/|Z_g|$ 就是与 $g$ 共轭的元素的个数。

**译校注：** 原书这句将“与 $g$ 共轭”误印为“与 $G$ 共轭”；根据前句的共轭类及公式，此处应为元素 $g$。

由定理 4.5.1，矩阵 $U$ 的各行标准正交。这说明 $U$ 是酉矩阵，因而它的各列也标准正交，从而得到所述结论。

## 4.6 酉表示：Maschke 定理对复表示的另一种证明

**定义 4.6.1。** 群 $G$ 的**酉有限维表示**，是 $G$ 在复有限维向量空间 $V$ 上的一个表示，且 $V$ 配有一个 $G$ 不变的正定<span class="original-page-anchor" id="pdf-page-77" aria-hidden="true"></span>Hermitian 型[^4-6-1] $(\ ,\ )$，也就是说，$\rho_V(g)$ 都是酉算子：$(\rho_V(g)v,\rho_V(g)w)=(v,w)$。

**定理 4.6.2。** *若 $G$ 有限，那么 $G$ 的任意有限维表示都具有酉结构。若该表示不可约，则这种结构除相差一个正实数倍外是唯一的。*

**证明。** 任取 $V$ 上一个正定型 $B$，按下式定义另一个型 $\overline B$：

$$
\overline B(v,w)=\sum_{g\in G}B(\rho_V(g)v,\rho_V(g)w).
$$

则 $\overline B$ 是 $V$ 上的正定 Hermitian 型，$\rho_V(g)$ 都是酉算子。若 $V$ 是不可约表示，$B_1,B_2$ 是 $V$ 上两个 $G$ 不变的正定 Hermitian 型，那么存在一个同态 $A:V\to V$，使 $B_1(v,w)=B_2(Av,w)$（因为任何正定 Hermitian 型都非退化）。

**译校注：** 原书这里遗漏了 $B_1,B_2$ 的 $G$ 不变性条件；此处按作者官方勘误补上。由这一条件，$A$ 才是表示同态。

由舒尔引理，$A=\lambda\operatorname{Id}$，且显然 $\lambda>0$。$\square$

定理 4.6.2 蕴含：若 $V$ 是有限群 $G$ 的有限维表示，那么**复共轭表示** $\overline V$ 与对偶表示 $V^*$ 同构。这里 $\overline V$ 与 $V$ 使用同一个空间、相同的加法和 $G$ 作用，但标量的作用取复共轭。事实上，表示同态 $\overline V\to V^*$ 显然等同于 $V$ 上的不变半双线性型（即两个变量都满足可加性，且对第一个变量线性、对第二个变量反线性的型），而同构则等同于非退化的不变半双线性型。因此，可以利用 $V$ 上的酉结构来定义一个同构 $\overline V\to V^*$。

**定理 4.6.3。** *任意群 $G$ 的有限维酉表示 $V$ 都完全可约。*

**证明。** 设 $W$ 是 $V$ 的一个子表示。令 $W^\perp$ 为 Hermitian 内积下 $W$ 在 $V$ 中的正交补。则 $W^\perp$ 是 $V$ 的子表示，且 $V=W\oplus W^\perp$。

**译校注：** 原书将“$V$ 的子表示”误印为“$W$ 的子表示”；正交补是取在 $V$ 中的，这里应为 $V$。

因此 $V$ 完全可约。$\square$

<span class="original-page-anchor" id="pdf-page-78" aria-hidden="true"></span>

定理 4.6.2 和 4.6.3 蕴含 Maschke 定理对复表示的结论（定理 4.1.1）。这样，我们就在复数域上得到了这个定理的一个新证明。

**注 4.6.4。** 定理 4.6.3 表明，对于无限群 $G$，有限维表示未必具有酉结构（因为存在不可分解但可约的有限维表示，例如 $G=\mathbb Z$ 时就有这样的表示）。

## 4.7 矩阵元的正交性

设 $V$ 是有限群 $G$ 的不可约表示，$v_1,v_2,\ldots,v_n$ 是不变 Hermitian 型下 $V$ 的一组标准正交基。$V$ 的矩阵元为 $t_{ij}^V(x)=(\rho_V(x)v_i,v_j)$。

**命题 4.7.1。** *(i) 非同构不可约表示的矩阵元，在 $F(G,\mathbb C)$ 中关于型 $(f,g)=\frac1{|G|}\sum_{x\in G}f(x)\overline{g(x)}$ 正交。*

*(ii) 有 $(t_{ij}^V,t_{i'j'}^V)=\delta_{ii'}\delta_{jj'}\cdot\frac1{\dim V}$。*

*因此，$G$ 的不可约表示的矩阵元构成 $F(G,\mathbb C)$ 的一组正交基。*

**证明。** 设 $V,W$ 是 $G$ 的两个不可约表示。在各自的正定不变 Hermitian 型下，分别取 $V$ 的标准正交基 $\{v_i\}$ 和 $W$ 的标准正交基 $\{w_i\}$。令 $w_i^*\in W^*$ 为通过与 $w_i$ 取内积而定义的线性函数：$w_i^*(u)=(u,w_i)$。则对 $x\in G$，有 $(xw_i^*,w_j^*)=\overline{(xw_i,w_j)}$。因此，令 $P=\frac1{|G|}\sum_{x\in G}x$，得到

$$
\begin{aligned}
(t_{ij}^V,t_{i'j'}^W)&=|G|^{-1}\sum_{x\in G}(xv_i,v_j)\overline{(xw_{i'},w_{j'})}\\
&=|G|^{-1}\sum_{x\in G}(xv_i,v_j)(xw_{i'}^*,w_{j'}^*)=(P(v_i\otimes w_{i'}^*),v_j\otimes w_{j'}^*).
\end{aligned}
$$

若 $V\ne W$，此式为零，因为 $P$ 投影到平凡表示上，而 $V\otimes W^*$ 中没有平凡表示。若 $V=W$，就需要考虑<span class="original-page-anchor" id="pdf-page-79" aria-hidden="true"></span>$(P(v_i\otimes v_{i'}^*),v_j\otimes v_{j'}^*)$。有如下 $G$ 不变分解：

$$
\begin{aligned}
V\otimes V^*&=\mathbb C\oplus L,\\
\mathbb C&=\operatorname{span}\left(\sum v_k\otimes v_k^*\right),\\
L&=\operatorname{span}_{a:\sum_k a_{kk}=0}\left(\sum_{k,l}a_{kl}v_k\otimes v_l^*\right),
\end{aligned}
$$

$P$ 沿第二个直和分量投影到第一个分量上。因此，$v_i\otimes v_{i'}^*$ 到 $\mathbb C\subset\mathbb C\oplus L$ 的投影为

$$
\frac{\delta_{ii'}}{\dim V}\sum v_k\otimes v_k^*.
$$

这说明

$$
(P(v_i\otimes v_{i'}^*),v_j\otimes v_{j'}^*)=\frac{\delta_{ii'}\delta_{jj'}}{\dim V},
$$

从而完成了 (i) 和 (ii) 的证明。最后一个结论直接由平方和公式得到。$\square$

## 4.8 特征标表及其例子

有限群的所有不可约表示的特征标可以排成一张**特征标表**，以元素的共轭类为列，以特征标为行。具体地说，特征标表的第一行列出共轭类的代表元，第二行列出各共轭类的元素个数，其余各行列出特征标在各共轭类上的取值。根据定理 4.5.1 和 4.5.4，特征标表的行和列关于相应的内积标准正交。

注意，在任意特征标表中，平凡表示对应的行全为 $1$，单位元对应的列则由各表示的维数组成。

例如，$S_3$ 的特征标表如下：

<span class="original-page-anchor" id="pdf-page-80" aria-hidden="true"></span>

$$
\begin{array}{c|c|c|c}
S_3&\operatorname{Id}&(12)&(123)\\\hline
\#&1&3&2\\\hline
\mathbb C_+&1&1&1\\\hline
\mathbb C_-&1&-1&1\\\hline
\mathbb C^2&2&0&-1
\end{array}
$$

这张表可以直接计算各不可约表示中的迹得到。

再看一个例子：$A_4$，即四个对象的偶置换群。它有三个一维表示（因为 $A_4$ 有正规子群 $\mathbb Z_2\oplus\mathbb Z_2$，且 $A_4/(\mathbb Z_2\oplus\mathbb Z_2)=\mathbb Z_3$）。由于总共有四个共轭类，还剩下一个三维不可约表示。最终得到的特征标表为

$$
\begin{array}{c|c|c|c|c}
A_4&\operatorname{Id}&(123)&(132)&(12)(34)\\\hline
\#&1&4&4&3\\\hline
\mathbb C&1&1&1&1\\\hline
\mathbb C_\epsilon&1&\epsilon&\epsilon^2&1\\\hline
\mathbb C_{\epsilon^2}&1&\epsilon^2&\epsilon&1\\\hline
\mathbb C^3&3&0&0&-1
\end{array}
$$

其中 $\epsilon=\exp(\frac{2\pi i}3)$。

最后一行可以利用各行的正交性算出。另一种算法是注意到，$\mathbb C^3$ 是 $A_4$ 通过正四面体的旋转给出的表示：此时，$(123),(132)$ 分别是绕垂直于四面体一个面的轴旋转 $120^\circ$ 和 $240^\circ$，而 $(12)(34)$ 是绕同时垂直于两条对边的轴旋转 $180^\circ$。

**例 4.8.1。** 下面三张特征标表依次对应于 $Q_8$、$S_4$ 和 $A_5$：

$$
\begin{array}{c|c|c|c|c|c}
Q_8&1&-1&i&j&k\\\hline
\#&1&1&2&2&2\\\hline
\mathbb C_{++}&1&1&1&1&1\\\hline
\mathbb C_{+-}&1&1&1&-1&-1\\\hline
\mathbb C_{-+}&1&1&-1&1&-1\\\hline
\mathbb C_{--}&1&1&-1&-1&1\\\hline
\mathbb C^2&2&-2&0&0&0
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-81" aria-hidden="true"></span>

$$
\begin{array}{c|c|c|c|c|c}
S_4&\operatorname{Id}&(12)&(12)(34)&(123)&(1234)\\\hline
\#&1&6&3&8&6\\\hline
\mathbb C_+&1&1&1&1&1\\\hline
\mathbb C_-&1&-1&1&1&-1\\\hline
\mathbb C^2&2&0&2&-1&0\\\hline
\mathbb C_+^3&3&-1&-1&0&1\\\hline
\mathbb C_-^3&3&1&-1&0&-1
\end{array}
$$

$$
\begin{array}{c|c|c|c|c|c}
A_5&\operatorname{Id}&(123)&(12)(34)&(12345)&(13245)\\\hline
\#&1&20&15&12&12\\\hline
\mathbb C&1&1&1&1&1\\\hline
\mathbb C_+^3&3&0&-1&\frac{1+\sqrt5}2&\frac{1-\sqrt5}2\\\hline
\mathbb C_-^3&3&0&-1&\frac{1-\sqrt5}2&\frac{1+\sqrt5}2\\\hline
\mathbb C^4&4&1&0&-1&-1\\\hline
\mathbb C^5&5&-1&1&0&0
\end{array}
$$

一维表示的特征标可以直接算出。

$Q_8$ 的二维表示的特征标，可以由这个表示的显式公式 (4.3.1) 算出，也可以利用正交性求得。

$S_4$ 的二维不可约表示由 $S_3$ 的二维不可约表示通过满同态 $S_4\to S_3$ 拉回得到，所以它的特征标可以从 $S_3$ 的特征标表中求得。

三维表示 $\mathbb C_+^3$ 的特征标，可以从它通过立方体旋转实现的几何描述中算出。具体地，$S_4$ 通过旋转立方体来置换其体对角线。因此，$(12)$ 是绕同时垂直于两条对边的轴旋转 $180^\circ$，$(12)(34)$ 是绕垂直于两个相对面的轴旋转 $180^\circ$，$(123)$ 是绕一条体对角线旋转 $120^\circ$，而 $(1234)$ 是绕垂直于两个相对面的轴旋转 $90^\circ$。利用 $\mathbb R^3$ 中旋转角为 $\varphi$ 的旋转的迹是 $1+2\cos\varphi$，就容易算出这些迹。再将 $\mathbb C_+^3$ 的特征标乘以符号表示的特征标，就得到 $\mathbb C_-^3$ 的特征标。

<span class="original-page-anchor" id="pdf-page-82" aria-hidden="true"></span>

最后，我们说明如何求得 $A_5$（五个对象的偶置换群）的特征标表。群 $A_5$ 是正二十面体的旋转群。因此，它有一个三维“旋转表示” $\mathbb C_+^3$：其中 $(12)(34)$ 是绕同时垂直于两条对边的轴旋转 $180^\circ$，$(123)$ 是绕垂直于两个相对面的轴旋转 $120^\circ$，而 $(12345),(13245)$ 分别是绕穿过两个相对顶点的轴旋转 $72^\circ$ 和 $144^\circ$。由这个描述，可以直接算出这个表示的特征标。

**译校注：** 原书第一段把第二个五循环印为 $(13254)$；这里按前页特征标表及本页下一段改为 $(13245)$。原印的 $(13254)$ 与 $(12345)$ 在 $A_5$ 中共轭，不能代表这两个不同角度的旋转。

$A_5$ 的另一个三维表示，是用 $S_5$ 中由 $(12)$ 共轭给出的 $A_5$ 自同构来扭转 $\mathbb C_+^3$ 而得到的表示，记作 $\mathbb C_-^3$。它的特征标与 $\mathbb C_+^3$ 相同，只是交换了共轭类 $(12345)$ 和 $(13245)$ 的取值。

还剩下两个不可约表示，由平方和公式，它们的维数为 $4$ 和 $5$。因此，分别记作 $\mathbb C^4$ 和 $\mathbb C^5$。

表示 $\mathbb C^4$ 实现在集合 $\{1,2,3,4,5\}$ 上函数值之和为零的函数空间中，$A_5$ 通过置换来作用（请验证它不可约！）。这个表示的特征标，等于五维置换表示的特征标减去一维平凡表示（常值函数）的特征标。前者在元素 $g$ 上的值，等于 $1,2,3,4,5$ 中被 $g$ 固定的对象个数。

表示 $\mathbb C^5$ 实现在正二十面体各对相对顶点上的、函数值之和为零的函数空间中（请验证它不可约！）。这个表示的特征标，可以用与 $\mathbb C^4$ 相似的方法算出，也可以利用正交公式求得。

## 4.9 利用特征标表计算张量积的重数

利用特征标表，可以通过下式计算张量积的重数 $N_{ij}^k$：

$$
V_i\otimes V_j=\sum N_{ij}^kV_k,\qquad N_{ij}^k=(\chi_i\chi_j,\chi_k).
$$

<span class="original-page-anchor" id="pdf-page-83" aria-hidden="true"></span>

**例 4.9.1。** 下面三张表依次列出 $S_3$、$S_4$ 和 $A_5$ 的不可约表示的张量积分解：


$$
\begin{array}{c|c|c|c}
S_3&\mathbb C_+&\mathbb C_-&\mathbb C^2\\\hline
\mathbb C_+&\mathbb C_+&\mathbb C_-&\mathbb C^2\\\hline
\mathbb C_-&&\mathbb C_+&\mathbb C^2\\\hline
\mathbb C^2&&&\mathbb C_+\oplus\mathbb C_-\oplus\mathbb C^2
\end{array}
$$

$$
\small\begin{array}{c|c|c|c|c|c}
S_4&\mathbb C_+&\mathbb C_-&\mathbb C^2&\mathbb C_+^3&\mathbb C_-^3\\\hline
\mathbb C_+&\mathbb C_+&\mathbb C_-&\mathbb C^2&\mathbb C_+^3&\mathbb C_-^3\\\hline
\mathbb C_-&&\mathbb C_+&\mathbb C^2&\mathbb C_-^3&\mathbb C_+^3\\\hline
\mathbb C^2&&&\mathbb C_+\oplus\mathbb C_-\oplus\mathbb C^2&\mathbb C_+^3\oplus\mathbb C_-^3&\mathbb C_+^3\oplus\mathbb C_-^3\\\hline
\mathbb C_+^3&&&&\mathbb C_+\oplus\mathbb C^2\oplus\mathbb C_+^3\oplus\mathbb C_-^3&\mathbb C_-\oplus\mathbb C^2\oplus\mathbb C_+^3\oplus\mathbb C_-^3\\\hline
\mathbb C_-^3&&&&&\mathbb C_+\oplus\mathbb C^2\oplus\mathbb C_+^3\oplus\mathbb C_-^3
\end{array}
$$

$$
\small\begin{array}{c|c|c|c|c|c}
A_5&\mathbb C&\mathbb C_+^3&\mathbb C_-^3&\mathbb C^4&\mathbb C^5\\\hline
\mathbb C&\mathbb C&\mathbb C_+^3&\mathbb C_-^3&\mathbb C^4&\mathbb C^5\\\hline
\mathbb C_+^3&&\mathbb C\oplus\mathbb C^5\oplus\mathbb C_+^3&\mathbb C^4\oplus\mathbb C^5&\mathbb C_-^3\oplus\mathbb C^4\oplus\mathbb C^5&\mathbb C_+^3\oplus\mathbb C_-^3\oplus\mathbb C^4\oplus\mathbb C^5\\\hline
\mathbb C_-^3&&&\mathbb C\oplus\mathbb C^5\oplus\mathbb C_-^3&\mathbb C_+^3\oplus\mathbb C^4\oplus\mathbb C^5&\mathbb C_+^3\oplus\mathbb C_-^3\oplus\mathbb C^4\oplus\mathbb C^5\\\hline
\mathbb C^4&&&&\substack{\mathbb C_+^3\oplus\mathbb C_-^3\oplus\mathbb C\\\oplus\mathbb C^4\oplus\mathbb C^5}&\mathbb C_+^3\oplus\mathbb C_-^3\oplus2\mathbb C^5\oplus\mathbb C^4\\\hline
\mathbb C^5&&&&&\substack{\mathbb C\oplus\mathbb C_+^3\oplus\mathbb C_-^3\\\oplus2\mathbb C^4\oplus2\mathbb C^5}
\end{array}
$$


**译校注：** 原书 $A_5$ 表中，平凡表示所在行的第二个表示误排为 $\mathbb C_3^+$，应为 $\mathbb C_+^3$；$\mathbb C_-^3\otimes\mathbb C_-^3$ 一格中的 $\mathbb C_+^3$ 应为 $\mathbb C_-^3$。后一个修订可由前页特征标表及 $N_{ij}^k=(\chi_i\chi_j,\chi_k)$ 直接验证。

## 4.10 Frobenius 行列式

将有限群 $G$ 的元素依次记为 $g_1,g_2,\ldots,g_n$，并引入以 $G$ 的元素为下标的 $n$ 个变量：

$$
x_{g_1},x_{g_2},\ldots,x_{g_n}.
$$

**定义 4.10.1。** 考虑矩阵 $X_G$，其矩阵元为 $a_{ij}=x_{g_ig_j}$。$X_G$ 的行列式是变量 $x_{g_1},x_{g_2},\ldots,x_{g_n}$ 的一个 $n$ 次多项式，称为 **Frobenius 行列式**，也称**群行列式**。

<span class="original-page-anchor" id="pdf-page-84" aria-hidden="true"></span>

下面的定理由 Dedekind 发现、Frobenius 证明，成为创立表示论的起点（见 [Cu] 及 4.11 节）。

**定理 4.10.2。**

$$
\det X_G=\prod_{j=1}^r P_j(x)^{\deg P_j},
$$

*其中 $P_j(x)$ 是一些两两不成比例的不可约多项式，$r$ 为 $G$ 的共轭类个数。*

我们需要下面这个简单引理。

**引理 4.10.3。** *设 $Y$ 是矩阵元为 $y_{ij}$ 的 $n\times n$ 矩阵，则 $\det Y$ 是变量 $\{y_{ij}\}$ 的不可约多项式。*

**证明。** 令 $X=t\cdot\operatorname{Id}+\sum_{i=1}^n x_iE_{i,i+1}$，其中 $i+1$ 按模 $n$ 计算，$E_{i,j}$ 是矩阵单位。则 $\det(X)=t^n-(-1)^nx_1\cdots x_n$，它显然不可约。因此，$\det(Y)$ 不可约：将 $Y$ 特化为 $X$ 后所得多项式不可约，而齐次多项式的不可约因子都是齐次的，不能特化为非零常数。$\square$

现在可以证明定理 4.10.2 了。

**证明。** 设 $V=\mathbb C[G]$ 是 $G$ 的正则表示。考虑取值为算子的多项式

$$
L(x)=\sum_{g\in G}x_g\rho(g),
$$

其中 $\rho(g)\in\operatorname{End}V$ 是由 $g$ 诱导的算子。$L(x)$ 在元素 $h\in G$ 上的作用为

$$
L(x)h=\sum_{g\in G}x_g\rho(g)h=\sum_{g\in G}x_ggh=\sum_{z\in G}x_{zh^{-1}}z.
$$

因此，线性算子 $L(x)$ 在基 $g_1,g_2,\ldots,g_n$ 下的矩阵，是对 $X_G$ 的列作置换所得的矩阵，所以两者的行列式至多相差一个符号。

<span class="original-page-anchor" id="pdf-page-85" aria-hidden="true"></span>

进一步，由 Maschke 定理，有

$$
\det_V L(x)=\prod_{i=1}^r(\det_{V_i}L(x))^{\dim V_i},
$$

其中 $V_i$ 是 $G$ 的各个不可约表示。令 $P_i=\det_{V_i}L(x)$。设 $\{e_{im}\}$ 是 $V_i$ 的基，$E_{i,jk}\in\operatorname{End}V_i$ 是这些基下的矩阵单位。则 $\{E_{i,jk}\}$ 是 $\mathbb C[G]$ 的一组基，且

$$
L(x)|_{V_i}=\sum_{j,k}y_{i,jk}E_{i,jk},
$$

其中 $y_{i,jk}$ 是 $\mathbb C[G]$ 上的新坐标，与 $x_g$ 通过一个线性变换联系起来。于是

$$
P_i(x)=\det_{V_i}L(x)=\det(y_{i,jk}).
$$

因此，$P_i$ 不可约（由引理 4.10.3），且两两不成比例（因为它们依赖于不同组的变量 $y_{i,jk}$）。定理得证。$\square$

## 4.11 历史插曲：Georg Frobenius 的“买马原则”

Ferdinand Georg Frobenius（1849—1917）曾在著名的柏林大学就读，师从 Karl Weierstrass 和 Leopold Kronecker；这两位伟大的数学家后来成了针锋相对的对手。Weierstrass 认为 Frobenius 是自己最出色的博士生之一，为他争取到苏黎世理工学院的正教授职位，助他走上顺利的学术道路。Frobenius 到苏黎世不久就结了婚，但美满婚姻的快乐并没有妨碍他继续卓有成效的研究。他在椭圆函数与 theta 函数、行列式与矩阵理论、双线性型等方面的研究，为他赢得了很高的声誉。大约十五年后，Kronecker 去世，柏林出现了一个空缺。Weierstrass 聘请自己的学生 Frobenius 接任 Kronecker 的教席，在老对手身后报了一箭之仇。1892 年，Frobenius 离开苏黎世前往柏林；四年后，Einstein 才进入苏黎世理工学院学习。

同事们称赞 Frobenius 是“一流的文章高手”，“行文清晰易懂，从不试图用空话蒙骗<span class="original-page-anchor" id="pdf-page-86" aria-hidden="true"></span>读者”。他很快当选为声望卓著的普鲁士科学院院士 [11，第 38 页]。这时，Frobenius 开始重新审视自己的研究兴趣。他在就职演说中解释说，theta 函数理论中的“公式迷宫”正在“让数学想象力枯萎”。他希望“不断到算术这口青春之泉寻求新生，以克服数学创造力的这种瘫痪”；这里的算术就是数论（引自 [24，第 220 页]）。四十多岁时，Frobenius 确实在“算术”中找到了这口“青春之泉”，具体说来，就是通过 Galois 理论与数论联系起来的有限群理论。

1896 年，Richard Dedekind 的几封来信毫不客气地打乱了 Frobenius 在柏林的舒适生活。Dedekind 是他的老相识，也是他在苏黎世理工学院的前任，此时已是德国抽象代数界的领军人物。寒暄一番，并感谢 Frobenius 照亮“群论如非洲般的黑暗”之后，Dedekind 分享了自己最近在群论上的一些成果，包括群行列式的概念，以及关于阿贝尔群的群行列式因式分解的定理。Dedekind 一直没有发表这方面的工作，因此 Frobenius 此前连群行列式都没有听说过。但他很快理解了这个概念，此后便一直钻研它。在回信中，Frobenius 温和地责备 Dedekind，不该向“你的朋友和仰慕者”隐瞒这些“极其优美的成果”，并请他提供更多细节。随后，Dedekind 提出一个“猜想中的定理”，难住了他的同事：群行列式中一次因子的个数等于交换子群的指数。他还承认：“我清楚地感到，自己在这里不会取得任何成果。”（引自 [24，第 223、224 页]）

Dedekind 的挑战恰好赶上春假，Frobenius 手头有些空闲，立刻就上了钩。他用军事比喻描述自己的工作，向群行列式发起了一场战争。他创造了广义的群特征标，借助它们进攻 Dedekind 的猜想。最初的结果似乎并不理想。他把结果告诉 Dedekind 时，还附上了这样一番保留意见：“我的结论<span class="original-page-anchor" id="pdf-page-87" aria-hidden="true"></span>如此复杂，连我自己都弄不清证明的关键究竟在哪里；事实上，我对它仍有些不放心。”（引自 [24，第 225、230 页]）

几天后，欣喜万分的 Frobenius 写信告诉 Dedekind，自己终于看到了通向解答的道路。他引用从前的同事 Friedrich Schottky 的话，把此前的挫折看成即将突破的预兆：“在研究中，经过艰苦的脑力劳动之后，如果产生了这样一种感觉，觉得在眼前的问题上不会有任何收获，那么便可以高兴起来，因为解答已近在眼前。”（引自 [24，第 230 页]）不到十天，Frobenius 就证明了群行列式理论的所有主要定理，只剩下一个最重要的结果。

用现代语言说，这个尚未证明的定理断言：不可约表示在正则表示中出现的重数，等于它的维数。Frobenius 将它称为“群行列式理论的基本定理”。他写道，如果它成立，“那就太好了”，“因为这样，我的理论就能提供确定不可约因子所需的一切”（引自 [24，第 235 页]）。证明花了五个月。在这段时间里，Frobenius 反复使用一种新的有效方法，始终保守秘密，只私下告诉了 Dedekind。这种方法借用了人们熟悉的讨价还价策略：“在市场上，尽可能不理会自己想要的那匹马，直到最后才正式表示看中了它。”（引自 [24，第 236 页]）按照 Frobenius 的理解，要解决一个数学问题，就得让自己忙于与数学毫不相干的活动。他广泛实践这条“买马原则”：陪妻子参观商贸展览和艺术展、阅读小说、清除花园里的毛毛虫。Frobenius 恳请 Dedekind 为这个巧妙的方法保密，并答应在身后出版的《论数学研究的方法》中公开它，还会附上捕捉毛毛虫的附录 [24，第 237 页]。遗憾的是，这本书从未问世，实在是捕捉毛毛虫这门科学的一大损失。

奇妙的是，暂时放下研究，再加上适度凌乱的书桌，确实帮助 Frobenius 理清了<span class="original-page-anchor" id="pdf-page-88" aria-hidden="true"></span>思路，找到了一种新方法。度假归来后，Frobenius 在自己“极其散乱、毫无条理的纸堆”里，找不到此前对那个未证定理的一个特例所作的证明。经历“一番痛苦折磨”之后，他却发现了一个新证明，并看到了将它推广的关键可能性 [24，第 237 页]。

同一年，Frobenius 通过一系列论文向世人公布了自己的成果。这是明智之举，因为他与 Dedekind 往来的大部分书信，后来竟落到一位美国律师手中。律师把信放在抽屉里保存了三十多年，直到退休后，才以 25 美元的价格交给一位数学教授 [27]。

Frobenius 以群行列式为主要武器，在短短几年内攻克了表示论中的一系列难题。虽然他的证明如今已被更简便的现代证明取代，但作为群行列式的大师，他的技艺至今无人超越，因为这个工具本身后来已不再使用。

Frobenius 不遗余力地想让柏林大学保持自己年轻求学时那段辉煌岁月的样貌。他指责应用数学的倡导者，认为他们试图把这所令人敬重的大学降格为技术学校。有人形容他的性格“有时暴躁、好争吵，且爱出言讥骂” [21]，这使他与许多同事疏远。尽管 Frobenius 坚持不妥协的立场（也许部分正是由于这种立场？），大学授予的博士学位数量和教学人员数量仍逐渐减少。Frobenius 指导过十九名博士生，只有一人的论文研究表示论。不过，培养这名学生却是一大幸事，因为他就是杰出的数学家 Issai Schur；此后数十年间，他一直延续着 Frobenius 的传统。

与此同时，柏林作为德国数学首要中心的声誉，正被哥廷根夺走。这当然不会使 Frobenius 喜欢上哥廷根风格的数学。他带着反感称其为“一个更爱玩赏美好图景，而不是钻研艰深思想的学派”（引自 [11，第 47 页]）。一位评论者说，他对哥廷根的领军人物 Felix Klein 以及 Sophus Lie 的厌恶“没有限度”（Biermann，见 [11，第 47 页]）。

<span class="original-page-anchor" id="pdf-page-89" aria-hidden="true"></span>

尽管 Frobenius 竭尽所能，想让这一学科保持纯粹，表示论此后还是不可挽回地受到了量子物理、化学、晶体学、光谱学乃至病毒学等应用的“污染”。更糟的是，在 Hermann Weyl 和 Claude Chevalley 的努力下，他心爱的表示论最终与 Lie 群理论融为一体。于是，Frobenius 终究与 Lie 和解了，虽然这场和解只发生在永恒数学对象的柏拉图世界里。

## 4.12. 习题

**习题 4.12.1.** 设 $G$ 为正 $N$ 边形的对称群（它有 $2N$ 个元素）。

(a) 描述这个群的所有不可约复表示（分别考虑 $N$ 为奇数和偶数的情形）。

(b) 将 $G$ 在实平面（即多边形所在的平面）上的标准表示复化，得到二维复表示 $V$。求 $V\otimes V$ 分解为不可约表示直和的结果。

**习题 4.12.2.** 设 $p$ 为素数。令 $G$ 为 $\mathbb F_p$ 上所有对角元均为 $1$ 的 $3\times3$ 上三角矩阵在乘法下构成的群（它的阶为 $p^3$），称为 **Heisenberg 群**。对任意满足 $z^p=1$ 的复数 $z$，在 $\mathbb F_p$ 上的复值函数空间 $V$ 上定义 $G$ 的表示，使得

$$
\left(\rho\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}f\right)(x)=f(x-1),
$$

$$
\left(\rho\begin{pmatrix}1&0&0\\0&1&1\\0&0&1\end{pmatrix}f\right)(x)=z^x f(x)
$$

（注意，由于 $z^p=1$，$z^x$ 有明确的意义）。

(a) 证明这样的表示存在且唯一，并对所有 $g\in G$ 求出 $\rho(g)$。

(b) 将这个表示记为 $R_z$。证明 $R_z$ 不可约，当且仅当 $z\ne1$。

<span class="original-page-anchor" id="pdf-page-90" aria-hidden="true"></span>

(c) 分类 $G$ 的所有一维表示。证明 $R_1$ 可以分解为一维表示的直和，其中每个表示恰好出现一次。

(d) 利用 (a)–(c) 和“平方和”公式，分类 $G$ 的所有不可约表示。

**习题 4.12.3.** 设 $V$ 为有限维复向量空间，$GL(V)$ 为 $V$ 上所有可逆线性变换构成的群。$S^mV$ 和 $\Lambda^mV$（$m\le\dim(V)$）自然成为 $GL(V)$ 的表示。证明它们都是不可约表示。

提示：在 $V$ 中选取一组基 $\{e_i\}$。找出 $GL(V)$ 的一个对角元素 $H$，使 $\rho(H)$ 的特征值互不相同（这里 $\rho$ 为上述表示之一）。由此可知，如果 $W$ 是子表示，那么它由 $\rho(H)$ 的某组特征向量基的一个子集 $S$ 张成。对所有 $i\ne j$，利用 $W$ 在算子 $\rho(1+E_{ij})$ 下的不变性，证明只要 $S$ 非空，它就必然是整组基；这里 $E_{ij}$ 由 $E_{ij}e_k=\delta_{jk}e_i$ 定义。

**习题 4.12.4.** 回顾一下，不含重边的图 $\Gamma$ 的邻接矩阵这样定义：若顶点 $i$ 和 $j$ 之间有边相连，则矩阵的第 $ij$ 个元素为 $1$，否则为零。设 $\Gamma$ 为有限图，其自同构群非阿贝尔。证明 $\Gamma$ 的邻接矩阵必有重特征值。

**习题 4.12.5.** 设 $I$ 为正二十面体的顶点集（$|I|=12$），$F(I)$ 为 $I$ 上的复值函数空间。回顾一下，五个对象的偶置换群 $G=A_5$ 作用于正二十面体，因此 $F(I)$ 给出了 $G$ 的一个十二维表示。

(a) 将这个表示分解为不可约表示的直和（即求出各个不可约表示出现的重数）。

(b) 对 $G$ 在正二十面体的面集和边集上的函数空间表示，分别作同样的分解。

**习题 4.12.6.** 设 $\mathbb F_q$ 为有 $q$ 个元素的有限域，$G$ 为 $\mathbb F_q$ 上所有非常数非齐次线性变换<span class="original-page-anchor" id="pdf-page-91" aria-hidden="true"></span>$x\to ax+b$ 构成的群（即 $a\in\mathbb F_q^\times$，$b\in\mathbb F_q$）。求 $G$ 的所有不可约复表示及其特征标，并计算不可约表示的张量积。

提示：令 $V$ 为 $\mathbb F_q$ 上所有函数值之和为零的函数空间所给出的 $G$ 的表示。证明 $V$ 是 $G$ 的不可约表示。

**习题 4.12.7.** 设 $G=SU(2)$（即行列式为 $1$ 的 $2\times2$ 酉矩阵群），令 $V=\mathbb C^2$ 为 $SU(2)$ 的标准二维表示。将 $V$ 看作实表示，此时它的维数为 $4$。

(a) 证明 $V$ 作为实表示不可约。

(b) 令 $\mathbb H$ 为 $\operatorname{End}_{\mathbb R}(V)$ 中由 $V$ 作为实表示的自同态构成的子空间。证明 $\mathbb H$ 的维数为 $4$，且对乘法封闭。证明 $\mathbb H$ 的每个非零元素都可逆，也就是说，$\mathbb H$ 是除代数。

(c) 找出 $\mathbb H$ 的一组基 $1,i,j,k$，使得 $1$ 为单位元，且

$$
i^2=j^2=k^2=-1,\quad ij=-ji=k,\quad jk=-kj=i,\quad ki=-ik=j.
$$

于是 $Q_8$ 是 $\mathbb H$ 中所有可逆元素在乘法下构成的群 $\mathbb H^\times$ 的一个子群。

代数 $\mathbb H$ 称为**四元数代数**，它的元素称为**四元数**。四元数由 W. R. Hamilton 于 1843 年发现（见第 4.13 节）。

(d) 对于 $q=a+bi+cj+dk$，$a,b,c,d\in\mathbb R$，令 $\bar q=a-bi-cj-dk$，并令 $\|q\|^2=q\bar q=a^2+b^2+c^2+d^2$。证明 $\overline{q_1q_2}=\bar q_2\bar q_1$ 以及 $\|q_1q_2\|=\|q_1\|\cdot\|q_2\|$。

(e) 令 $G$ 为范数等于 $1$ 的四元数构成的群。证明这个群同构于 $SU(2)$。（因此，从几何上看，$SU(2)$ 就是三维球面。）

(f) 在 $\mathbb H$ 中由 $i,j,k$ 张成的空间 $V$ 上，考虑 $G$ 的作用 $x\to qxq^{-1}$，其中 $q\in G$，$x\in V$。这个作用保持 $V$ 上的范数，因而给出同态 $h:SU(2)\to SO(3)$；这里 $SO(3)$ 为三维欧氏空间的旋转群。证明这个同态是满射，且其核为 $\{1,-1\}$。

<span class="original-page-anchor" id="pdf-page-92" aria-hidden="true"></span>

**习题 4.12.8.** 已知 $SO(3)$ 的有限子群分类如下：

1) 循环群 $\mathbb Z/n\mathbb Z$，$n\ge1$，由绕某条轴旋转 $2\pi/n$ 的旋转生成；

2) 阶为 $2n$ 的二面体群 $D_n$，$n\ge2$（即三维空间中，含有一个正 $n$ 边形[^regular-two-gon]的平面的旋转对称群）；

3) 正四面体的旋转群（$A_4$）；

4) 立方体或正八面体的旋转群（$S_4$）；

5) 正十二面体或正二十面体的旋转群（$A_5$）。

(a) 推导这个分类。

提示：设 $G$ 为 $SO(3)$ 的有限子群，考虑 $G$ 在单位球面上的作用。如果球面上一点被 $G$ 的某个非平凡元素固定，就称该点为极点。证明 $G$ 的每个非平凡元素恰好固定一对互为对跖点的极点；固定给定极点 $P$ 的子群是循环群，设其阶为 $m$（称为 $P$ 的阶）。于是 $P$ 的轨道有 $n/m$ 个元素，其中 $n=|G|$。令 $P_1,\ldots,P_k$ 分别代表 $G$ 在极点集上的各个轨道（每个轨道选一个代表），并令它们的阶为 $m_1,\ldots,m_k$。通过计数 $G$ 中的非平凡元素，证明

$$
2\left(1-\frac1n\right)=\sum_i\left(1-\frac1{m_i}\right).
$$

然后找出满足这个等式的所有可能的 $m_i$ 和 $n$，并分类相应的群。

(b) 利用这个分类，分类 $SU(2)$ 的有限子群（使用同态 $SU(2)\to SO(3)$）。

**习题 4.12.9.** 求习题 4.12.2 中 Heisenberg 群的不可约复表示的特征标与张量积。

**习题 4.12.10.** 设 $G$ 为有限群，$V$ 为 $G$ 的忠实复表示，即相应的映射 $G\to$ <span class="original-page-anchor" id="pdf-page-93" aria-hidden="true"></span>$GL(V)$ 为单射。证明对 $G$ 的任意不可约表示，都存在某个 $n$，使它出现在 $S^nV$ 中（因而也出现在 $V^{\otimes n}$ 中）。

提示：证明存在向量 $u\in V^*$，使其在 $G$ 中的稳定子为 $1$。然后定义映射 $SV\to F(G,\mathbb C)$，将 $V^*$ 上的多项式 $f$ 映到 $G$ 上的函数 $f_u$，其中 $f_u(g)=f(gu)$。证明这个映射为满射，并由此得出所需结论。

**习题 4.12.11.** 这个问题涉及表示论在物理学（弹性理论）中的一个应用。我们先说明物理背景，再提出数学问题。

设想一种材料占据物理空间 $V=\mathbb R^3$（带正定内积的空间）中的某个区域 $U$。假设材料发生了形变，也就是说，我们施加了微分同胚（即坐标变换）$g:U\to U'$。弹性理论要研究的问题是：这种形变会在材料内部产生多大的应力？

对每个点 $P\in U$，定义 $A_P:V\to V$ 为 $A_P=dg(P)$。$A_P$ 非退化，因此有极分解 $A_P=D_PO_P$，其中 $O_P$ 正交，$D_P$ 对称。矩阵 $O_P$ 描述 $A_P$ 的旋转部分（显然不会产生应力），而 $D_P$ 是实际产生应力的畸变部分。如果形变很小，则 $D_P$ 接近 $1$，故可写为 $D_P=1+d_P$，其中 $d_P$ 是一个很小的对称矩阵，即 $S^2V$ 的元素。这个矩阵称为 $P$ 点的**形变张量**。

下面定义刻画应力的应力张量。取 $V$ 中一个很小的非零向量 $v$，并令 $\sigma$ 为以 $P$ 为中心、垂直于 $v$、面积为 $\|v\|$ 的小圆盘。令 $F_v$ 为位于 $\sigma$ 的 $v$ 侧的材料对另一侧材料施加的力。由 Newton 定律很容易推出，$F_v$ 对 $v$ 是线性的，因此存在一个线性算子 $S_P:V\to V$，使得 $F_v=S_Pv$。这个算子称为**应力张量**。

弹性定律是形如 $S_P=f(d_P)$ 的方程，其中 $f$ 为函数。最简单的情形是线性定律（Hooke 定律），即 $f:S^2V\to\operatorname{End}(V)$ 为线性函数。一般来说，这样的函数由 $9\cdot6=54$ 个参数确定，但我们将证明，实际只有两个<span class="original-page-anchor" id="pdf-page-94" aria-hidden="true"></span>关键参数——**压缩模量** $K$ 和**剪切模量** $\mu$。为此，我们将使用表示论。

回顾一下，旋转群 $SO(3)$ 作用于 $V$，所以 $S^2V$ 和 $\operatorname{End}(V)$ 都是这个群的表示。物理定律必须在这个群（Galileo 变换）下保持不变，因此 $f$ 必须是表示的同态。

(a) 证明 $\operatorname{End}(V)$ 可以分解为 $\mathbb R\oplus V\oplus W$，其中 $\mathbb R$ 为平凡表示，$V$ 为标准三维表示，$W$ 为 $SO(3)$ 的一个五维表示。证明 $S^2V=\mathbb R\oplus W$。

(b) 证明 $V$ 和 $W$ 都不可约，甚至复化后也不可约。利用 Schur 引理推出：$S_P$ 总是对称的，并且对 $x\in\mathbb R$、$y\in W$，有 $f(x+y)=Kx+\mu y$，其中 $K,\mu$ 为某两个实数。

事实上，从物理上很清楚，$K,\mu$ 都是正数。压缩模量 $K$ 刻画材料抵抗压缩或膨胀的能力，而剪切模量 $\mu$ 刻画材料抵抗体积不变而形状改变的能力。例如，雕塑用的黏土具有较大的压缩模量，却具有较小的剪切模量。

## 4.13. 历史插曲：William Rowan Hamilton 的几何、代数、形而上学与诗歌四元组

William Rowan Hamilton 十七岁时发现 Laplace 的《天体力学》中的一个错误，由此燃起了对数学的兴趣。爱尔兰皇家天文学家对此印象深刻，几年后便为 Hamilton 争取到 Dunsinsk 天文台皇家天文学家的职位，此后 Hamilton 在那里度过了余生。在大学里，Hamilton 埋头学习，赢得了几乎所有能想得到的荣誉，还未毕业就接下了天文台的工作。然而，作为一名从事实际观测的天文学家，他却并不成功。繁琐的观测工作对他毫无吸引力，理论问题让他兴奋得多。

<span class="original-page-anchor" id="pdf-page-95" aria-hidden="true"></span>

Hamilton 的交往圈中有重要的浪漫主义诗人和哲学家。他自己也怀抱诗人的志向，不过 William Wordsworth 温和地引导他，把创造力重新投入数学。Hamilton 沉浸于 Kant 的著作，接受了 Kant 将空间和时间视为纯粹直观的观念。Kant 随口说过，正如几何是“空间的科学”，代数也可以看作“纯粹时间的科学”；这句话深深吸引了 Hamilton [61]。后来，Hamilton 坚持说，Kant 不过是印证了他自己的想法；阅读 Kant 更像是在“认出”已有的观念，而非“发现”新观念 [17, 2:96, 2:98]。

Hamilton 以他提出的特征函数概念为基础，研究光学和力学，由此赢得了数学家的声誉。他认为，自己的最大成就是把 $3n$ 个二阶常微分方程的求解，化为两个一阶二次偏微分方程的求解。这是否让实际求解问题取得了进展，并不显然。但 Hamilton 坚信，即使他的办法“没有带来实际上的便利”，把所有复杂计算都化为研究一个特征函数，仍应给人以“智性的愉悦”（引自 [18, p. 89]）。

Hamilton 将代数学家分为三个思想流派：实用派、语文学派和理论派。实用派把代数看作一种技艺，关心计算；语文学派把代数看作一种语言，即按照某些规则操作的一套符号；只有理论派将代数视为科学，是“严格、纯粹而独立的，由其自身的直观原理通过有效推理推导出来的”。Hamilton 谦逊地把自己归入了这一派 [17, 2:48]。

Hamilton 写道：“除非我觉得自己能够越过或穿透符号，看到符号所指的事物，否则我永远不会满足。”他无法在负数和虚数概念背后找到“所指的事物”，为此深感苦恼，也因此觉得这些概念荒谬。到 1828 年，他“即使不对那些极负盛名的分析学家的推理感到不满，也对他们的措辞极其不满”。他认为，要“清除挡在分析学入口处的形而上学障碍”，就必须或者舍弃负数与<span class="original-page-anchor" id="pdf-page-96" aria-hidden="true"></span>虚数，或者解释它们的“真正含义” [17, 2:143, 1:304]。Hamilton 很快了解到所谓的 Argand 图：它把复数表示为平面上的点，并将实部与虚部分别标在两条相互垂直的坐标轴上。受这种几何表示的启发，他开始寻找一种能定义所有有效运算的复数代数表示，很快提出了代数偶的概念。呼应 Kant 将代数视为时间科学的想法，Hamilton 把这些数偶看作时间中的“步进”，而不是量的大小，并把负号解释为时间性的反转 [43, p. 281]。他试图从纯粹时间或数学时间的直观概念中，为代数找到新的基础：时刻对于代数，就像点对于几何；时间区间对应有限的直线段，无限延伸的直线则代表时间本身。事务过于繁忙，使 Hamilton 无法继续沿这条大有希望的思路探索。他说：“即使要书写纯粹时间，也需要时间——需要有着小时和天数这些粗粝现实的时间。”[17, 2:144]

复数的二维表示也启发 Hamilton 去寻找与“真实”的三维空间相联系的超复数；他称之为“三元数”。“三元数”与他对唯心主义三段式“正题—反题—合题”的哲学兴趣十分契合 [20]。三元数很容易相加，却始终不肯相乘。这并非没有道理：在 Hamilton 去世后，Frobenius 才证明，这样的代数根本不可能存在。绝望之中，Hamilton 尝试四个数构成的有序组，即“四元数”。只有放弃交换律，它们才肯相乘。1843 年 10 月 16 日，当 Hamilton 与妻子沿都柏林的皇家运河散步时，他突然明白了这一点。后来他回忆说：“就在那一刻，我感到思维的电流回路接通了；从中迸出的火花，就是”四元数的“**基本方程**”。换一种没那么富于诗意的比喻，他把解决问题后的满足感比作“智性渴求得到了解脱” [17, 2:435–436]。Hamilton 立即拿出笔记本，记下四元数的基本公式。他急于检验新代数的相容性，于是在乘马车前往爱尔兰皇家科学院理事会会议的途中继续写个不停，随后又在以<span class="original-page-anchor" id="pdf-page-97" aria-hidden="true"></span>科学院院长身份主持那场会议时继续书写。看来，无论是与妻子交谈，还是主持学术会议，都不会打断他的数学思绪。

Hamilton 觉得，自己或许可以用十到十五年探索四元数理论的种种后果，恰好与他此前为建立这套理论所花的时间一样长。他推想，四元数的标量部分可以表示数量（比如电量），而虚部则可以确定方向和强度，例如电的极性。他甚至将四元数演算解释为“极性演算”，赋予它一种“半形而上学”的意义，呼应了他早年对唯心主义哲学的兴趣 [17, 2:436, 2:440]。后来，他的想法更加富于形而上学色彩：四元数是一种天然的时空代数，空间的三个维度与时间这个第四维度在其中结合。他写道：“四元数诞生了，成为四位亲本——不妨说是几何、代数、形而上学和诗歌——组成的四元组的奇妙后代。”接着，他引用了自己写给 John Herschel 爵士的十四行诗，认为这是对四元数思想最清楚的表达：

> “时间的一维与空间的三维，  
> 如何被符号的链条一同环围。”

（引自 [20, p. 176]。）

Hamilton 从一开始就选择了“**形而上学的表达风格**”，几乎尽其所能，让自己的理论难以为读者接受。Herschel 恳请他把思想讲得“清楚而熟悉，达到普通人无需形而上学也能理解的程度”，并“像逐渐给婴儿喂硬食那样引入新术语” [17, 2:633]，但毫无效果。Hamilton 在长达八百页的《四元数讲义》（1853）中塞满了难以理解的新术语，如 *vector*、*vehend*、*vection*、*vectum*、*revector*、*revehend*、*revection*、*revectum*、*provector*、*transvector*、*factor*、*profactor*、*versor* 和 *quandrantal versor* [10, p. 36]。他随后尝试写一部更基础的入门书《四元数原理》，结果篇幅比《讲义》还长。

Hamilton 的学生 Peter Tait 推广了四元数，并与提倡另一套向量分析方法的 Josiah Willard Gibbs 和 Oliver Heaviside 展开了长期论战。四元数乘法固然不满足交换律，向量的点积和叉积<span class="original-page-anchor" id="pdf-page-98" aria-hidden="true"></span>似乎却有更大的问题。Tait 因而把向量分析骂作“雌雄同体的怪物” [10, p. 185]。

二十三年后，Hamilton 向儿子讲述这次伟大发现时补充说，在灵感顿悟的那一刻，他“无法抗拒这股冲动——尽管它也许不合哲学精神——想用刀把（四元数公式）刻在”附近一座桥的“石头上” [17, 2:435]。这件事究竟是真的，还是 Hamilton 忍不住想为自己的故事添一点色彩，我们再也无法知道：时间早已抹去桥石上的刻痕，却没有抹去它在数学史上的印记。如今，Hamilton 当年破坏公物的地点立着一块纪念牌，上面写道：“1843 年 10 月 16 日，William Rowan Hamilton 爵士走过此处，天才的灵光一闪，发现了四元数乘法的基本公式 $i^2=j^2=k^2=ijk=-1$，并把它刻在这座桥的一块石头上。”如今，这座桥成了数学家的朝圣之地，他们希望借当年那道灵光的火花，点燃自己的想象力。

[^4-6-1]: 我们约定，Hermitian 型对第一个变量线性，对第二个变量反线性。

[^regular-two-gon]: 正二边形就是一条线段。
