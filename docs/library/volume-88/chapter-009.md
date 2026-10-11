---
title: "第九章 有限维代数的结构"
description: "《Introduction to Representation Theory》中文译文。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"第八章 同调代数","link":"/library/volume-88/chapter-008"}
next: {"text":"历史插曲参考文献","link":"/library/volume-88/historical-references"}
---

# 第九章 有限维代数的结构

<span class="original-page-anchor" id="pdf-page-217" aria-hidden="true"></span>

本章回到有限维代数的结构研究。全章都在代数闭域 $k$ 上讨论，$k$ 的特征任意。

## 9.1. 幂等元的提升

设 $A$ 是一个环，$I\subset A$ 是幂零理想。

**命题 9.1.1.** 设 $e_0\in A/I$ 是幂等元，即 $e_0^2=e_0$。则存在幂等元 $e\in A$，它是 $e_0$ 的提升（即模 $I$ 约化后得到 $e_0$）。这个幂等元在允许用 $1+I$ 中的元素共轭的意义下唯一。

**证明.** 先证明 $I^2=0$ 时的结论。注意此时 $I$ 同时是左、右 $A/I$-模。任取 $e_0$ 在 $A$ 中的一个提升 $e_*$，则 $e_*^2-e_*=a\in I$，且 $e_0a=ae_0$。我们寻找形如 $e=e_*+b$（$b\in I$）的 $e$。$b$ 应满足方程 $e_0b+be_0-b=-a$。取 $b=-(2e_0-1)a$，则

$$
e_0b+be_0-b=-2e_0a+(2e_0-1)a=-a,
$$

所以 $e$ 是幂等元。

**译校注.** 根据作者 2024 年 6 月 3 日的勘误，上述证明从 $b$ 的方程起，原书的 $a$ 应改为 $-a$；因此取 $b=-(2e_0-1)a$，相应等式也一并修正。

为了描述其他解，令 $e'=e+c$。若 $e'$ 是幂等元，必须有 $ec+ce-c=0$。这<span class="original-page-anchor" id="pdf-page-218" aria-hidden="true"></span>等价于 $ece=0$ 和 $(1-e)c(1-e)=0$，因此 $c=ec(1-e)+(1-e)ce=[e,[e,c]]$。于是 $e'=(1+[c,e])e(1+[c,e])^{-1}$。

一般情形下，我们对 $k$ 归纳，证明 $e_{k-1}$ 在 $A/I^{k+1}$ 中存在提升 $e_k$，且这个提升在允许用 $1+I^k$ 中的元素共轭的意义下唯一（由于 $I$ 幂零，这就足够了）。假设 $k=m-1$ 时结论成立，下面证明 $k=m$ 时的结论。此时已有幂等元 $e_{m-1}\in A/I^m$，需要把它提升到 $A/I^{m+1}$。但在 $A/I^{m+1}$ 中，$(I^m)^2=0$，所以证明完成。$\square$

**译校注.** 根据作者勘误，上段归纳步骤中被提升的元素应为 $e_{k-1}$，原书误写成了 $e_0$。

**定义 9.1.2.** 含单位元的代数 $B$ 中的**完备正交幂等元系**，是指一族元素 $e_1,\ldots,e_n\in B$，满足 $e_i e_j=\delta_{ij}e_i$ 且 $\sum_{i=1}^n e_i=1$。

**推论 9.1.3.** 设 $e_{01},\ldots,e_{0m}$ 是 $A/I$ 中的完备正交幂等元系，则 $A$ 中存在完备正交幂等元系 $e_1,\ldots,e_m$（$e_i e_j=\delta_{ij}e_i$，$\sum e_i=1$），分别提升 $e_{01},\ldots,e_{0m}$。

**证明.** 对 $m$ 归纳。当 $m=2$ 时，结论由命题 9.1.1 得到。当 $m>2$ 时，先用命题 9.1.1 把 $e_{01}$ 提升为 $e_1$，再对代数 $(1-e_1)A(1-e_1)$ 应用归纳假设。$\square$

## 9.2. 投射覆盖

显然，有限维代数 $A$ 上的每个有限生成投射模，都是不可分解投射模的直和。因此，要了解 $A$ 上的有限生成投射模，只需分类不可分解投射模。

设 $A$ 是一个有限维代数，其单模为 $M_1,\ldots,M_n$。

**定理 9.2.1.** (i) 对每个 $i=1,\ldots,n$，存在唯一的不可分解有限生成投射模 $P_i$，使得

$$
\dim\operatorname{Hom}(P_i,M_j)=\delta_{ij}.
$$

(ii) $A=\bigoplus_{i=1}^n(\dim M_i)P_i$。

(iii) $A$ 上任意不可分解有限生成投射模，都同构于某个 $P_i$。

<span class="original-page-anchor" id="pdf-page-219" aria-hidden="true"></span>

**证明.** 回顾 $A/\operatorname{Rad}(A)=\bigoplus_{i=1}^n\operatorname{End}(M_i)$，且 $\operatorname{Rad}(A)$ 是幂零理想。为 $M_i$ 选取一组基，并令 $e_{ij}^0=E_{jj}^i$ 为投影到各基向量的秩 $1$ 投影算子（$j=1,\ldots,\dim M_i$）。那么 $e_{ij}^0$ 是 $A/\operatorname{Rad}(A)$ 中的正交幂等元。由推论 9.1.3，可以把它们提升为 $A$ 中的正交幂等元 $e_{ij}$。现在定义 $P_{ij}=Ae_{ij}$。于是 $A=\bigoplus_i\bigoplus_{j=1}^{\dim M_i}P_{ij}$，所以各 $P_{ij}$ 都投射。另外，$\operatorname{Hom}(P_{ij},M_k)=e_{ij}M_k$，因此 $\dim\operatorname{Hom}(P_{ij},M_k)=\delta_{ik}$。最后，根据命题 9.1.1，固定 $i$ 后，各 $e_{ij}$ 在 $A^\times$ 的作用下共轭，所以 $P_{ij}$ 在同构意义下不依赖于 $j$；因此将 $P_{ij}$ 记为 $P_i$。

我们断言 $P_i$ 不可分解。事实上，若 $P_i=Q_1\oplus Q_2$，则要么 $l=1$ 时对所有 $j$ 都有 $\operatorname{Hom}(Q_l,M_j)=0$，要么 $l=2$ 时对所有 $j$ 都有此等式。因此，$Q_1=0$ 或 $Q_2=0$。

此外，不可能有其他不可分解有限生成投射模，因为任意不可分解投射模都必须出现在 $A$ 的分解中。定理得证。$\square$

**定义 9.2.2.** 投射模 $P_i$ 称为 $M_i$ 的**投射覆盖**。

**命题 9.2.3.** 设 $N$ 是任意有限维 $A$-模，则 $\dim\operatorname{Hom}_A(P_i,N)=[N:M_i]$，其中 $[N:M_i]$ 是 $M_i$ 在 $N$ 的若尔当–赫尔德列中出现的重数。

**证明.** 当 $N=M_j$ 时，结论显然成立。另外，若

$$
0\to N_1\to N_2\to N_3\to0
$$

是 $A$-模的正合序列，则由于 $P_i$ 投射，相应序列

$$
0\to\operatorname{Hom}_A(P_i,N_1)\to\operatorname{Hom}_A(P_i,N_2)\to\operatorname{Hom}_A(P_i,N_3)\to0
$$

也正合。由此得到结论。$\square$

## 9.3. 有限维代数的 Cartan 矩阵

设 $A$ 是一个有限维代数，其单模为 $M_i$（$i=1,\ldots,n$），投射覆盖为 $P_i$。令 $c_{ij}:=\dim\operatorname{Hom}_A(P_i,P_j)=[P_j:M_i]$。

<span class="original-page-anchor" id="pdf-page-220" aria-hidden="true"></span>

**定义 9.3.1.** 矩阵 $C=(c_{ij})$ 称为 $A$ 的 **Cartan 矩阵**。

显然，$A$ 的 Cartan 矩阵各项非负，对角项为正。

**习题 9.3.2.** 设 $A$ 是复数域上的代数，由元素 $g,x$ 生成，定义关系为 $gx=-xg$、$x^2=0$、$g^2=1$。求 $A$ 的单模、不可分解投射模及 Cartan 矩阵。

## 9.4. 同调维数

设 $A$ 是一个环，$M$ 是一个左 $A$-模。

**定义 9.4.1.** $M$ 的**投射维数** $\operatorname{pd}(M)$，是 $M$ 最短的有限投射解消的长度（约定 $0\to P_d\to\cdots\to P_0$ 的长度为 $d$）。若 $M$ 没有有限投射解消，则其投射维数为无穷。

例如，投射模恰好是投射维数为 $0$ 的模。

**习题 9.4.2.** (i) 证明 $\operatorname{pd}(M)\leq d$，当且仅当对任意左 $A$-模 $N$，在 $i>d$ 时都有 $\operatorname{Ext}^i(M,N)=0$。

提示：证明“如果”这一方向时，对 $d$ 归纳，并利用习题 8.2.6(v) 中 Ext 群的长正合序列。

(ii) 设 $0\to M\to P\to N\to0$ 是不分裂的短正合序列，且 $P$ 投射。证明 $\operatorname{pd}(N)=\operatorname{pd}(M)+1$。

(iii) 证明若 $\operatorname{pd}(M)=d>0$，$P_\bullet$ 是 $M$ 的任意投射解消，则此解消中映射 $P_{d-1}\to P_{d-2}$ 的核 $K_d$ 是投射模（约定 $P_{-1}=M$）。因此，把 $P_d$ 换成 $K_d$，并把 $P_d$ 左边的各项都换成零，就得到 $M$ 的一个长度为 $d$ 的投射解消。由此推出，若 $A$、$M$ 都有限维，则 $M$ 有一个有限解消 $P_\bullet$，且各 $P_i$ 都有限维。

<span class="original-page-anchor" id="pdf-page-221" aria-hidden="true"></span>

**定义 9.4.3.** 若每个左（分别为右）$A$-模 $M$ 的投射维数都 $\leq d$，就称环 $A$ 的左（分别为右）**同调维数** $\leq d$。若 $A$ 的同调维数 $\leq d$，但不 $\leq d-1$，则称其同调维数恰为 $d$。若这样的 $d$ 不存在，则称 $A$ 的同调维数为无穷。

**例 9.4.4.** 根据 Hilbert 合冲定理（见习题 8.2.10(iv)），多项式代数 $k[x_1,\ldots,x_n]$ 的同调维数是 $n$。

**习题 9.4.5.** (i) 设有限维代数 $A$ 的同调维数 $d$ 有限，$C$ 是 $A$ 的 Cartan 矩阵。证明 $\det(C)=\pm1$。

(ii) $k[t]/t^n$（$n>1$）的同调维数是多少？习题 9.3.2 中代数的同调维数又是多少？

**习题 9.4.6.** (i) 证明至少有一条边的任意箭图 $Q$，其路径代数 $P_Q$ 的同调维数为 $1$。特别地，自由代数 $k\langle x_1,\ldots,x_n\rangle$ 的同调维数为 $1$（$n\geq1$）。

(ii) 设 $Q$ 是没有有向圈的有限有向图。求其路径代数 $P_Q$ 的 Cartan 矩阵。

## 9.5. 块

设 $A$ 是代数闭域 $k$ 上的有限维代数，$\mathcal C$ 为有限维 $A$-模范畴。

**定义 9.5.1.** 若两个有限维单 $A$-模 $X,Y$ 之间存在链 $X=M_0,M_1,\ldots,M_n=Y$，使得对每个 $i=0,\ldots,n-1$，都有 $\operatorname{Ext}^1(M_i,M_{i+1})\neq0$ 或 $\operatorname{Ext}^1(M_{i+1},M_i)\neq0$（也可以两者都非零），就称 $X,Y$ **相联**。

这里约定 $X$ 与自身相联（用长度为 $0$ 的链）。

显然，相联关系是等价关系，因此把单 $A$-模的同构类集合 $S$ 分成等价类 $S_k$（$k\in B$）。按定义，$\mathcal C$ 的第 $k$ 个**块** $\mathcal C_k$，是由 $\mathcal C$ 中所有这样的对象 $M$ 构成的范畴：$M$ 的若尔当–赫尔德列中出现的所有单模都属于 $S_k$。

<span class="original-page-anchor" id="pdf-page-222" aria-hidden="true"></span>

**例 9.5.2.** 若 $A$ 半单，则每个块都等价于向量空间范畴（因此只有一个单对象）。若 $A$ 是交换局部阿廷代数，则只有一个块。习题 9.3.2 中的代数也只有一个块。

**习题 9.5.3.** (i) 证明 $\mathcal C$ 的块与 $A$ 的不可分解中心幂等元 $e_k$（即不能非平凡地分解为两个中心幂等元之和的幂等元）之间存在自然双射，且 $\mathcal C_k$ 是有限维 $e_k A$-模范畴。

(ii) 证明 $\mathcal C$ 的任意不可分解对象都属于某个 $\mathcal C_k$，并且当 $M\in\mathcal C_k$、$N\in\mathcal C_l$、$k\neq l$ 时，$\operatorname{Hom}(M,N)=0$。因此，$\mathcal C=\bigoplus_{k\in B}\mathcal C_k$。

(iii) 当 $A=k[S_3]$、$k$ 的特征为 $2$ 时，确定左 $A$-模范畴中的块。

## 9.6. 有限阿贝尔范畴

设 $\mathcal C$ 是一个 $k$-线性阿贝尔范畴，其中每个对象的长度都有限（即有一个有限滤过，逐次商都是单对象）。假设对 $\mathcal C$ 的每个单对象 $X$，都有 $\operatorname{End}(X)=k$。注意，在这样的范畴中，Hom 空间都是有限维的（请验证！）。

**定义 9.6.1.** 若 $\mathcal C$ 有足够多投射对象，且在同构意义下只有有限多个单对象，就称 $\mathcal C$ 是**有限的**。

例如，如前所证，有限维代数上的有限维模范畴是有限的。下面将看到，反过来也成立。

**定义 9.6.2.** 阿贝尔范畴 $\mathcal C$ 中的对象 $P$ 称为**投射生成元**（也称 **progenerator**），如果 $P$ 投射，且每个对象都是若干份 $P$ 的直和的商。

例如，在环 $A$ 的模范畴中，自由模 $A$ 是投射生成元。

**练习 9.6.3.** 设 $P$ 是有限阿贝尔范畴中的投射对象。证明 $P$ 是投射生成元，当且仅当对每个单对象 $L$，都有 $\operatorname{Hom}(P,L)\neq0$。由此推出，任意有限阿贝尔范畴都有投射生成元。

**译校注.** 原书未明确假设 $P$ 投射，而仅凭 $\operatorname{Hom}(P,L)\neq0$ 不能推出投射性，故补上这一必要假设。

<span class="original-page-anchor" id="pdf-page-223" aria-hidden="true"></span>

现在设 $\mathcal C$ 是有限阿贝尔范畴，$P$ 是它的一个投射生成元。令 $B=\operatorname{End}(P)^{\mathrm{op}}$，这是一个在 $P$ 右侧作用的有限维代数。用 $B\text{-}\mathrm{fmod}$ 表示有限维左 $B$-模范畴。考虑由公式 $F(M)=\operatorname{Hom}(P,M)$ 给出的函子 $F:\mathcal C\to B\text{-}\mathrm{fmod}$。

**定理 9.6.4.** 函子 $F$ 是范畴等价。因此，域 $k$ 上的任意有限阿贝尔范畴，都等价于某个有限维 $k$-代数的有限维模范畴。

**译校注.** 原书这一结论省略了“有限维”对模的限定；根据上文的 $B\text{-}\mathrm{fmod}$，这里所指的是有限维模范畴，已补全。

下面的问题给出了定理 9.6.4 的证明。

**习题 9.6.5.** 设函子 $G:B\text{-}\mathrm{fmod}\to\mathcal C$ 由 $G(X):=P\otimes_B X$ 定义。其中 $P\otimes_B X$ 是态射 $\psi:P\otimes B\otimes X\to P\otimes X$ 的余核，$\psi=a_P\otimes\operatorname{Id}-\operatorname{Id}\otimes a_X$（$a_P:P\otimes B\to P$、$a_X:B\otimes X\to X$ 分别是表示 $B$ 在 $P$、$X$ 上作用的态射）。

(i) 证明 $F\circ G\cong\operatorname{Id}$。也就是说，对每个 $X\in B\text{-}\mathrm{fmod}$，证明 $X$ 自然同构于 $\operatorname{Hom}(P,P\otimes_B X)$。（这里应该只需用到 $P$ 是非零投射对象。）

(ii) 对任意 $X\in\mathcal C$，构造自然态射

$$
\xi:P\otimes_B\operatorname{Hom}(P,X)\to X,
$$

并证明它是满射。

(iii) 证明 $G\circ F\cong\operatorname{Id}$。为此，考虑短正合序列

$$
0\to K\to P\otimes_B\operatorname{Hom}(P,X)\to X\to0,
$$

其中第三个映射是 $\xi$。把函子 $F$ 作用于此序列，并利用 (i)，推出 $K=0$，从而 $\xi$ 是同构。由此得出，函子 $G$、$F$ 互为拟逆，因此都是范畴等价。

## 9.7. Morita 等价

本节讨论有限维代数的 Morita 等价理论。经过适当调整，这一理论也可推广到无限维情形。

<span class="original-page-anchor" id="pdf-page-224" aria-hidden="true"></span>

定理 9.6.4 表明，只要为有限阿贝尔范畴 $\mathcal C$ 选定一个投射生成元 $P$，就可以把 $\mathcal C$ 与某个有限维代数 $B$ 上的有限维模范畴等同。不过，投射生成元并不唯一。具体地，设 $P_1,\ldots,P_m$ 是 $\mathcal C$ 的不可分解投射对象（根据定理 9.6.4，这些对象是有意义的）。那么，$\mathcal C$ 的所有投射生成元都是形如 $P_{\mathbf n}:=\bigoplus_{i=1}^m n_iP_i$ 的对象，其中 $n_i\geq1$（请验证！）。定义 $B_{\mathbf n}=B_{\mathbf n}(\mathcal C):=\operatorname{End}(P_{\mathbf n})^{\mathrm{op}}$，就得到所有有限维模范畴等价于 $\mathcal C$ 的有限维代数 $B_{\mathbf n}$。

**定义 9.7.1.** 若阿贝尔范畴 $A\text{-}\mathrm{fmod}$ 和 $B\text{-}\mathrm{fmod}$ 等价，就称有限维代数 $A$、$B$ **Morita 等价**。

因此，有限维代数的 Morita 等价类，就是形如 $\{B_{\mathbf n}(\mathcal C),\mathbf n\in\mathbb N^m\}$ 的集合。

注意，$B_{\mathbf n}$ 的维数为 $\sum c_{ij}n_i n_j$，其中 $(c_{ij})$ 是 $\mathcal C$ 的 Cartan 矩阵。特别地，维数最小的代数 $B=B_{\mathbf n}$ 对应于所有 $n_i=1$ 的情形，即投射生成元 $P=\bigoplus_i P_i$；其维数为 $\sum c_{ij}$。容易看出，在所有 $B_{\mathbf n}$ 中，只有这个代数的商 $B_{\mathbf n}/\operatorname{Rad}(B_{\mathbf n})=\bigoplus_i\operatorname{Mat}_{n_i}(k)$ 是交换的。

**定义 9.7.2.** 若有限维代数 $B$ 的商 $B/\operatorname{Rad}(B)$ 是交换的，就称 $B$ 为**基本代数**。

于是，由定理 9.6.4 得到如下推论。

**推论 9.7.3.** (i) 任意有限阿贝尔范畴 $\mathcal C$，都等价于唯一的基本代数 $B=B(\mathcal C)$ 上的有限维模范畴。

(ii) 任意有限维代数 $A$，都与唯一的基本代数 $B=B_A$ Morita 等价，且 $\dim B_A\leq\dim A$。
