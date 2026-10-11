---
title: "第八章 同调代数"
description: "《Introduction to Representation Theory》中文译文。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"第七章 范畴导论","link":"/library/volume-88/chapter-007"}
next: {"text":"第九章 有限维代数的结构","link":"/library/volume-88/chapter-009"}
---

# 第八章 同调代数

<span class="original-page-anchor" id="pdf-page-209" aria-hidden="true"></span>

本章介绍一些基本的同调代数工具。研究表示范畴的精细结构，需要用到这些工具。

## 8.1. 投射模与内射模

设 $A$ 是一个代数，$P$ 是一个左 $A$-模。

**定理 8.1.1.** $P$ 的下列性质等价：

(i) 若 $\alpha:M\to N$ 是满态射，$\nu:P\to N$ 是任意态射，则存在态射 $\mu:P\to M$，使得 $\alpha\circ\mu=\nu$。

(ii) 任意满态射 $\alpha:M\to P$ 都分裂；也就是说，存在 $\mu:P\to M$，使得 $\alpha\circ\mu=\operatorname{id}$。

(iii) 存在另一个 $A$-模 $Q$，使得 $P\oplus Q$ 是自由 $A$-模，即若干份 $A$ 的直和。

(iv) $A$-模范畴上的函子 $\operatorname{Hom}_A(P,?)$ 是正合的。

**证明.** 要证明 (i) 蕴含 (ii)，取 $N=P$ 即可。要证明 (ii) 蕴含 (iii)，取 $M$ 为自由模（总能这样做，因为任意模都是自由模的商）。要证明 (iii) 蕴含 (iv)，注意到当 $P$ 是自由模时，函子 $\operatorname{Hom}_A(P,?)$ 是正合的（因为<span class="original-page-anchor" id="pdf-page-210" aria-hidden="true"></span>$\operatorname{Hom}_A(A,N)=N$），而两个复形的直和若是正合的，则这两个复形各自也正合，于是结论成立。要证明 (iv) 蕴含 (i)，令 $K$ 为映射 $\alpha$ 的核，再把正合函子 $\operatorname{Hom}_A(P,?)$ 作用于正合序列

$$
0\to K\to M\to N\to0.
$$

$\square$

**定义 8.1.2.** 满足定理 8.1.1 中任一条件 (i)–(iv) 的模，称为**投射模**。

**习题 8.1.3.** 如果左 $A$-模范畴上的函子 $M\otimes_A$ 是正合的，就称右 $A$-模 $M$ 为**平坦模**。

(i) 证明任意投射模都是平坦模。

(ii) 设 $A$ 是交换环，$S$ 是 $A$ 的任意乘法封闭子集，则局部化 $S^{-1}A$ 是平坦 $A$-模。

(iii) 设 $A=\mathbb C[x]$，$M=\mathbb C[x,x^{-1}]$。证明 $M$ 平坦，但不投射。

**练习 8.1.4.** 设 $A$ 是一个环，$M_1,M_2$ 是左 $A$-模，$P_1,P_2$ 是投射左 $A$-模，$f_i:P_i\to M_i$ 是同态。设左 $A$-模 $M$ 包含 $M_1$，且 $M/M_1=M_2$。证明存在同态 $f:P_1\oplus P_2\to M$，使得 $f|_{P_1}=f_1$，且它诱导的同态 $P_2\to M_2$ 等于 $f_2$。

与投射模对偶的概念是内射模。具体来说，有如下定理。

设 $A$ 是一个代数，$I$ 是一个左 $A$-模。

**定理 8.1.5.** $I$ 的下列性质等价：

(i) 若 $\alpha:N\to M$ 是单态射，$\nu:N\to I$ 是任意态射，则存在态射 $\mu:M\to I$，使得 $\mu\circ\alpha=\nu$。

(ii) 任意单态射 $\alpha:I\to M$ 都分裂；也就是说，存在 $\mu:M\to I$，使得 $\mu\circ\alpha=\operatorname{id}$。

<span class="original-page-anchor" id="pdf-page-211" aria-hidden="true"></span>

(iii) $A$-模范畴上的函子 $\operatorname{Hom}_A(?,I)$ 是正合的。

**证明.** “(i) 蕴含 (ii)”和“(iii) 蕴含 (i)”的证明与定理 8.1.1 的证明类似。下面证明 (ii) 蕴含 (iii)。设

$$
0\to N\to M\to K\to0
$$

是正合序列，用 $j$ 表示嵌入 $N\to M$。考虑相应的序列

$$
0\to\operatorname{Hom}(K,I)\to\operatorname{Hom}(M,I)\to\operatorname{Hom}(N,I)\to0.
$$

取 $f\in\operatorname{Hom}(N,I)$，定义模 $E:=(M\oplus I)/N$，其中 $N$ 通过 $x\mapsto(j(x),-f(x))$ 嵌入 $M\oplus I$。显然，有嵌入 $I\to E$，因为 $N\oplus I$ 在 $E$ 中的像自然地与 $I$ 等同。因此，这个嵌入存在分裂 $E\to I$；也就是说，存在映射 $M\oplus I\to I$，$(m,i)\mapsto g(m)+i$，且 $g(j(x))-f(x)=0$。这表明映射 $j^*:\operatorname{Hom}(M,I)\to\operatorname{Hom}(N,I)$ 是满射，即函子 $\operatorname{Hom}(?,I)$ 正合，得到了所需结论。$\square$

**定义 8.1.6.** 满足定理 8.1.5 中任一条件 (i)–(iii) 的模，称为**内射模**。

**例 8.1.7.** 设 $A$ 是一个有限维代数，$P$ 是一个左 $A$-模。则 $P$ 投射，当且仅当 $P^*$ 是内射右 $A$-模。

**译校注.** 原书未假设 $A$ 有限维。一般只能由 $P$ 投射推出 $P^*$ 内射，而 $P^*$ 内射等价于 $P$ 平坦，不能保证 $P$ 投射。这里补上 $A$ 有限维这一充分条件，使原书的等价结论成立。

利用定理 8.1.1(iv) 和定理 8.1.5(iii)，可以在任意阿贝尔范畴中定义投射对象和内射对象。具体定义如下。

**定义 8.1.8.** 阿贝尔范畴 $\mathcal C$ 中的对象 $P$ 称为**投射对象**，如果函子 $\operatorname{Hom}_{\mathcal C}(P,?)$ 是正合的。

阿贝尔范畴 $\mathcal C$ 中的对象 $I$ 称为**内射对象**，如果函子 $\operatorname{Hom}_{\mathcal C}(?,I)$ 是正合的。

## 8.2. Tor 与 Ext 函子

设 $A$ 是含单位元的环。如例 7.9.6 中所述，左 $A$-模范畴上的函子 $M\otimes_A?$ 和 $\operatorname{Hom}_A(M,?)$（其中 $M$ 分别是右 $A$-模和<span class="original-page-anchor" id="pdf-page-212" aria-hidden="true"></span>左 $A$-模）通常并不正合（它们只在一侧正合）。函子 $\operatorname{Tor}_i^A(M,?)$ 和 $\operatorname{Ext}_A^i(M,?)$ 用来衡量函子 $M\otimes_A?$ 和 $\operatorname{Hom}_A(M,?)$ 不正合的程度。它们的定义如下。

**定义 8.2.1.** $M$ 的**投射解消**是一个正合序列

$$
\cdots\to P_2\to P_1\to P_0\to M\to0,
$$

其中所有模 $P_i$（$i\geq0$）都是投射模。

**练习 8.2.2.** 证明任意模都有投射解消（例如，可以取各项均为自由模的解消）。

**定义 8.2.3.** 设 $M$ 是右 $A$-模，$P_\bullet$ 是 $M$ 的投射解消，$N$ 是左 $A$-模。对 $i\geq0$，定义 $\operatorname{Tor}_i^A(M,N)=\operatorname{Tor}_i(M,N)$ 为解消 $P_\bullet$ 所诱导的复形

$$
\cdots\to P_2\otimes_A N\to P_1\otimes_A N\to P_0\otimes_A N\to0
$$

的第 $i$ 个上同调。

**定义 8.2.4.** 设 $M$ 是左 $A$-模，$P_\bullet$ 是 $M$ 的投射解消，$N$ 是左 $A$-模。对 $i\geq0$，定义 $\operatorname{Ext}_A^i(M,N)=\operatorname{Ext}^i(M,N)$ 为解消 $P_\bullet$ 所诱导的复形

$$
0\to\operatorname{Hom}_A(P_0,N)\to\operatorname{Hom}_A(P_1,N)\to\operatorname{Hom}_A(P_2,N)\to\cdots
$$

的第 $i$ 个上同调。

**习题 8.2.5.** 本题将证明，上同调群 $\operatorname{Tor}_i$ 和 $\operatorname{Ext}^i$ 在相当强的意义下确实不依赖于投射解消 $P_\bullet$。因此，在它们的记号中不注明 $P_\bullet$ 是合理的。

设 $P_\bullet,Q_\bullet$ 是 $M$ 的两个投射解消，相应的微分为 $d_i^P:P_i\to P_{i-1}$、$d_i^Q:Q_i\to Q_{i-1}$；特别地，有 $d_0^P:P_0\to M$、$d_0^Q:Q_0\to M$。

(i) 证明存在同态 $f_0:P_0\to Q_0$，使得 $d_0^Q\circ f_0=d_0^P$。

(ii) 接着对 $j$ 归纳，证明存在同态 $f_j:P_j\to Q_j$，使得 $d_j^Q\circ f_j=f_{j-1}\circ d_j^P$。

<span class="original-page-anchor" id="pdf-page-213" aria-hidden="true"></span>

满足 (i)、(ii) 中条件的这一族同态，称为**解消的态射** $f:P_\bullet\to Q_\bullet$。

(iii) 显然，这样的态射 $f$ 定义了线性映射 $\psi_i(P,Q,f):\operatorname{Tor}_i^P(M,N)\to\operatorname{Tor}_i^Q(M,N)$，其中上标 $P$、$Q$ 表示 Tor 群分别用解消 $P_\bullet$、$Q_\bullet$ 定义。证明映射 $\psi_i(P,Q,f)$ 实际上不依赖于 $f$（因此可记为 $\psi_i(P,Q)$）。

(iv) 推出 $\psi_i(P,Q)$ 都是同构（利用 $\psi_i(P,P)=\operatorname{id}$ 和 $\psi_i(Q,R)\circ\psi_i(P,Q)=\psi_i(P,R)$）。

(v) 定义类似的映射 $\xi_i(Q,P,f):\operatorname{Ext}_Q^i(M,N)\to\operatorname{Ext}_P^i(M,N)$，并证明它们不依赖于 $f$，且都是同构。

**译校注.** 原书此处的 Ext 箭头从 $P$ 指向 $Q$。由于 $f:P_\bullet\to Q_\bullet$ 经 $\operatorname{Hom}(-,N)$ 后方向反转，正确箭头应从 $Q$ 指向 $P$，已修正。

**习题 8.2.6.** (i) 证明 $\operatorname{Tor}_0(M,N)=M\otimes_A N$，且 $\operatorname{Ext}^0(M,N)=\operatorname{Hom}_A(M,N)$。

(ii) 证明这里定义的群 $\operatorname{Ext}^1(M,N)$ 与习题 3.9.1 中定义的群有典范同构。

(iii) 设

$$
0\to N_1\to N_2\to N_3\to0
$$

是左 $A$-模的短正合序列。

证明存在长正合序列

$$
\begin{aligned}
0&\to\operatorname{Hom}_A(M,N_1)\to\operatorname{Hom}_A(M,N_2)\to\operatorname{Hom}_A(M,N_3)\to{}\\
&\operatorname{Ext}^1(M,N_1)\to\operatorname{Ext}^1(M,N_2)\to\operatorname{Ext}^1(M,N_3)\to\operatorname{Ext}^2(M,N_1)\to\cdots
\end{aligned}
$$

以及

$$
\begin{aligned}
\cdots&\to\operatorname{Tor}_2(M,N_3)\to\operatorname{Tor}_1(M,N_1)\to\operatorname{Tor}_1(M,N_2)\to\operatorname{Tor}_1(M,N_3)\\
&\to M\otimes_A N_1\to M\otimes_A N_2\to M\otimes_A N_3\to0.
\end{aligned}
$$

如前所述，这说明 Tor 群和 Ext 群确实可以“衡量”函子 $M\otimes_A$ 与 $\operatorname{Hom}_A(M,?)$ 不正合的程度。

提示：利用习题 7.8.5。

(iv) 证明计算 $\operatorname{Tor}_i^A(M,N)$ 时，可以取 $N$ 的投射解消，再与 $M$ 作张量积，然后计算上同调。

<span class="original-page-anchor" id="pdf-page-214" aria-hidden="true"></span>

提示：先证明可以把 $M$、$N$ 各自的投射解消作张量积，再计算上同调，从而得到 $\operatorname{Tor}_i^A(M,N)$。

(v) 设 $0\to M_1\to M_2\to M_3\to0$ 是左 $A$-模的短正合序列，$P_\bullet^1$ 和 $P_\bullet^3$ 分别是 $M_1$、$M_3$ 的投射解消。构造 $M_2$ 的一个投射解消，使其各项为 $P_i^2:=P_i^1\oplus P_i^3$（利用练习 8.1.4）。利用这一解消证明，对任意左 $A$-模 $N$，存在长正合序列

$$
\begin{aligned}
0&\to\operatorname{Hom}_A(M_3,N)\to\operatorname{Hom}_A(M_2,N)\to\operatorname{Hom}_A(M_1,N)\to{}\\
&\operatorname{Ext}^1(M_3,N)\to\operatorname{Ext}^1(M_2,N)\to\operatorname{Ext}^1(M_1,N)\to\operatorname{Ext}^2(M_3,N)\to\cdots
\end{aligned}
$$

对相应的右 $A$-模短正合序列，以及左 $A$-模 $N$，还存在长正合序列

$$
\begin{aligned}
\cdots&\to\operatorname{Tor}_2(M_3,N)\to\operatorname{Tor}_1(M_1,N)\to\operatorname{Tor}_1(M_2,N)\to\operatorname{Tor}_1(M_3,N)\\
&\to M_1\otimes_A N\to M_2\otimes_A N\to M_3\otimes_A N\to0.
\end{aligned}
$$

**译校注.** 原书把本项中的 $M_i$ 统一写成左 $A$-模。Ext 序列使用左 $A$-模；但对一般非交换环，Tor 序列中的 $M_i$ 应为右 $A$-模，$N$ 则为左 $A$-模，已作区分。

**习题 8.2.7.** (i) 设 $A=\mathbb Z$，$M,N$ 是有限生成阿贝尔群。计算 $\operatorname{Tor}_i(M,N)$、$\operatorname{Ext}^i(M,N)$。（提示：利用有限阿贝尔群的分类定理，把问题归结为循环群的情形。）

(ii) 对 $A=k[x]$ 以及任意有限生成 $A$-模 $M,N$，完成同样的计算。

**习题 8.2.8.** 设 $A_1,A_2$ 是域 $k$ 上的代数，$M_i$ 是右 $A_i$-模，$N_i$ 是左 $A_i$-模。证明

$$
\operatorname{Tor}_i^{A_1\otimes A_2}(M_1\otimes M_2,N_1\otimes N_2)=\bigoplus_{j+m=i}\operatorname{Tor}_j^{A_1}(M_1,N_1)\otimes\operatorname{Tor}_m^{A_2}(M_2,N_2).
$$

**译校注.** 原书把 $M_i,N_i$ 都写成左 $A_i$-模。对于 Tor 式，$M_i$ 应为右模，$N_i$ 应为左模，已修正。

类似地，取 $M_i,N_i$ 都为左 $A_i$-模。若 $N_i$ 有限维，且各 $M_i$ 都有由有限生成投射模构成的投射解消，则

$$
\operatorname{Ext}_{A_1\otimes A_2}^i(M_1\otimes M_2,N_1\otimes N_2)=\bigoplus_{j+m=i}\operatorname{Ext}_{A_1}^j(M_1,N_1)\otimes\operatorname{Ext}_{A_2}^m(M_2,N_2).
$$

**译校注.** 原书只要求 $N_i$ 有限维，这不足以保证一般代数上的 Ext 公式成立。这里补上各 $M_i$ 具有上述投射解消的充分条件；例如，若 $A_i$、$M_i$ 均有限维，这一条件就满足。

用类似的方法，可以在任意具有**足够多投射对象**的阿贝尔范畴中定义 Tor 群和 Ext 群；所谓足够多投射对象，是指任意对象都是某个投射对象的商（这一条件保证每个对象都有投射解消）。

**译校注.** 上述范畴条件足以定义 Ext；定义 Tor 还需指定适当的张量积或右正合函子，任意阿贝尔范畴本身并不自带这样的结构。

<span class="original-page-anchor" id="pdf-page-215" aria-hidden="true"></span>

**练习 8.2.9.** (i) 证明有限阿贝尔群范畴和有限维 $k[x]$-模范畴都没有非零投射对象（因此也没有足够多投射对象）。

(ii) 设 $A$ 是有限生成交换环。证明有限生成 $A$-模范畴具有足够多投射对象。

**习题 8.2.10.** 设 $V$ 是域 $k$ 上的有限维向量空间，令 $C_i=SV\otimes\wedge^i V$。可以把 $C_i$ 看作 $V^*$ 上取值于 $\wedge^i V$ 的多项式函数空间。用公式

$$
d_i(f)(u)=\iota_u f(u),\qquad u\in V^*
$$

定义微分 $d_i:C_i\to C_{i-1}$，其中 $\iota_u:\wedge^i V\to\wedge^{i-1}V$ 是由下式定义的收缩：

$$
\iota_u(v_1\wedge\cdots\wedge v_i)=\sum_{j=1}^i(-1)^j u(v_j)v_1\wedge\cdots\widehat v_j\cdots\wedge v_i.
$$

(i) 证明 $C_\bullet$ 是 $k$ 作为 $SV$-模的投射解消（实际上是自由解消），其中 $V$ 在 $k$ 上的作用平凡。（这称为 **Koszul 解消**。）

(ii) 设 $V=U\oplus W$，则可以把 $SW$ 看作 $SV$-模（$U$ 的作用为零）。构造 $SW$ 的一个自由 $SV$-模解消，使其各项为 $C_i=SV\otimes\wedge^i U$。

提示：把 $k$ 作为 $SU$-模的 Koszul 解消与 $SW$ 作张量积。

(iii) 通过左右乘法，把 $SV$ 看作 $S(V\oplus V)=SV\otimes SV$-模。构造 $SV$ 作为 $SV\otimes SV$-模的自由解消，使其各项为 $C_i=SV\otimes\wedge^i V\otimes SV$（称为 Koszul 双模解消）。

(iv) 把 (iii) 中的解消与任意 $SV$-模 $M$ 在 $SV$ 上作张量积，构造 $M$ 的投射解消 $P_\bullet$（实际上是自由解消），并使 $i>\dim V$ 时 $P_i=0$。由此推出，对任意 $SV$-模 $N$ 和任意 $i>\dim V$，都有

$$
\operatorname{Tor}_i^{SV}(M,N)=\operatorname{Ext}_{SV}^i(M,N)=0
$$

（**Hilbert 合冲定理**）。

(v) 计算 $\operatorname{Ext}_{SV}^i(k,k)$ 和 $\operatorname{Tor}_i^{SV}(k,k)$。
