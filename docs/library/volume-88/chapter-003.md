---
title: "第三章 表示论的一般结果"
description: "《Introduction to Representation Theory》中文译文。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"第二章 表示论的基本概念","link":"/library/volume-88/chapter-002"}
next: {"text":"第四章 有限群的表示：基本结果","link":"/library/volume-88/chapter-004"}
---

# 第三章 表示论的一般结果

<span class="original-page-anchor" id="pdf-page-49" aria-hidden="true"></span>

## 3.1. 半单表示中的子表示

设 $A$ 是一个代数。

**定义 3.1.1.** $A$ 的**半单**表示（或**完全可约**表示）是不可约表示的直和。

**例 3.1.2.** 设 $V$ 是 $A$ 的一个 $n$ 维不可约表示。那么，让 $A$ 以左乘作用在 $Y=\operatorname{End}(V)$ 上，就得到 $A$ 的一个半单表示，它同构于 $nV$（即 $n$ 个 $V$ 的直和）。事实上，$V$ 的任意一组基 $v_1,\ldots,v_n$ 都给出表示的同构 $\operatorname{End}(V)\to nV$，其公式为 $x\mapsto(xv_1,\ldots,xv_n)$。

**注 3.1.3.** 由 Schur 引理，$A$ 的任意有限维半单表示 $V$ 都可以典范地等同于 $\bigoplus_X\operatorname{Hom}_A(X,V)\otimes X$，其中 $X$ 遍历 $A$ 的所有不可约表示。事实上，我们有自然映射 $f:\bigoplus_X\operatorname{Hom}(X,V)\otimes X\to V$，由 $g\otimes x\mapsto g(x)$ 给出，其中 $x\in X$、$g\in\operatorname{Hom}(X,V)$。容易验证，这个映射是同构。

**译校注：** 原文未注明 $V$ 有限维；这里按作者 2024 年 6 月 3 日的勘误补上这一条件。

<span class="original-page-anchor" id="pdf-page-50" aria-hidden="true"></span>

下面我们来看，如何用 Schur 引理分类有限维半单表示的子表示。

**命题 3.1.4.** 设 $V_i$（$1\le i\le m$）是 $A$ 的两两不同构的有限维不可约表示，$W$ 是 $V=\bigoplus_{i=1}^m n_iV_i$ 的一个子表示。那么，$W$ 同构于 $\bigoplus_{i=1}^m r_iV_i$，其中 $r_i\le n_i$；嵌入 $\phi:W\to V$ 是嵌入 $\phi_i:r_iV_i\to n_iV_i$ 的直和。每个这样的嵌入，都由一个长度为 $r_i$、元素属于 $V_i$ 的行向量右乘某个行向量线性无关的 $r_i\times n_i$ 矩阵 $X_i$ 给出，即 $\phi(v_1,\ldots,v_{r_i})=(v_1,\ldots,v_{r_i})X_i$。

**证明。** 对 $n:=\sum_{i=1}^m n_i$ 作归纳。归纳起点 $n=1$ 显然成立。下面证明归纳步骤。设 $W$ 非零，取一个不可约子表示 $P\subset W$。这样的 $P$ 存在（习题 2.3.15）。[^rt-50-1] 由 Schur 引理，$P$ 同构于某个 $V_i$，而嵌入 $\phi|_P:P\to V$ 经过 $n_iV_i$ 分解。把 $P$ 与 $V_i$ 等同后，这个嵌入的公式为 $v\mapsto(vq_1,\ldots,vq_{n_i})$，其中 $q_l\in k$ 不全为零。

注意，由 $k$ 上可逆的 $n_i\times n_i$ 矩阵组成的群 $G_i=GL_{n_i}(k)$，通过 $(v_1,\ldots,v_{n_i})\mapsto(v_1,\ldots,v_{n_i})g_i$ 作用在 $n_iV_i$ 上，并在 $n_jV_j$（$j\ne i$）上作恒等作用。因此，它作用在 $V$ 的子表示的集合上，且保持我们要证明的性质：在 $g_i$ 的作用下，矩阵 $X_i$ 变为 $X_ig_i$，而矩阵 $X_j$（$j\ne i$）不变。取 $g_i\in G_i$，使 $(q_1,\ldots,q_{n_i})g_i=(1,0,\ldots,0)$。这样，$Wg_i$ 包含 $n_iV_i$ 的第一个直和项 $V_i$（它就是 $Pg_i$）；于是 $Wg_i=V_i\oplus W'$。这里，$W'\subset n_1V_1\oplus\cdots\oplus(n_i-1)V_i\oplus\cdots\oplus n_mV_m$ 是沿其余直和项把 $Wg_i$ 投影到第一个直和项 $V_i$ 的映射的核。因此，所需结论由归纳假设得到。$\square$

**注 3.1.5.** 命题 3.1.4 并不要求 $k$ 是代数闭域，也不要求 $V$ 有限维。去掉这两个假设后，只需作一个改动：矩阵 $X_i$ 的元素不再属于 $k$，而是属于 $D_i=\operatorname{End}_A(V_i)$，<span class="original-page-anchor" id="pdf-page-51" aria-hidden="true"></span>而我们知道，$D_i$ 是一个除代数。命题 3.1.4 的这个推广版本，证明与先前相同（请验证！）。

## 3.2. 稠密性定理

设 $A$ 是代数闭域 $k$ 上的一个代数。

**推论 3.2.1.** 设 $V$ 是 $A$ 的一个有限维不可约表示，$v_1,\ldots,v_n\in V$ 是任意一组线性无关向量。那么，对任意 $w_1,\ldots,w_n\in V$，都存在元素 $a\in A$，使 $av_i=w_i$。

**证明。** 假设结论不成立。那么，映射 $A\to nV$（由 $a\mapsto(av_1,\ldots,av_n)$ 给出）的像是一个真子表示。由命题 3.1.4，它对应于某个 $r\times n$ 矩阵 $X$，其中 $r<n$。取 $a=1$，可知存在向量 $u_1,\ldots,u_r\in V$，使 $(u_1,\ldots,u_r)X=(v_1,\ldots,v_n)$。取一个非零向量 $(q_1,\ldots,q_n)$，使 $X(q_1,\ldots,q_n)^T=0$（因为 $r<n$，这样的向量存在）。于是 $\sum q_iv_i=(u_1,\ldots,u_r)X(q_1,\ldots,q_n)^T=0$，即 $\sum q_iv_i=0$，这与 $v_i$ 的线性无关性矛盾。$\square$

**定理 3.2.2（稠密性定理）。** (i) 设 $V$ 是 $A$ 的一个有限维不可约表示。那么，映射 $\rho:A\to\operatorname{End}V$ 是满射。

(ii) 设 $V=V_1\oplus\cdots\oplus V_r$，其中 $V_i$ 是 $A$ 的两两不同构的有限维不可约表示。那么，映射 $\bigoplus_{i=1}^r\rho_i:A\to\bigoplus_{i=1}^r\operatorname{End}(V_i)$ 是满射。

**证明。** (i) 设 $B$ 是 $A$ 在 $\operatorname{End}(V)$ 中的像。我们要证明 $B=\operatorname{End}(V)$。取 $c\in\operatorname{End}(V)$，取 $V$ 的一组基 $v_1,\ldots,v_n$，并令 $w_i=cv_i$。由推论 3.2.1，存在 $a\in A$，使 $av_i=w_i$。那么，$a$ 的像就是 $c$，所以 $c\in B$，结论得证。

(ii) 设 $B_i$ 是 $A$ 在 $\operatorname{End}(V_i)$ 中的像，$B$ 是 $A$ 在 $\bigoplus_{i=1}^r\operatorname{End}(V_i)$ 中的像。回顾一下，$\bigoplus_{i=1}^r\operatorname{End}(V_i)$ 作为 $A$ 的表示是半单的：它同构于 $\bigoplus_{i=1}^r d_iV_i$，其中 $d_i=\dim V_i$。由命题 3.1.4，$B=\bigoplus_i B_i$。另一方面，(i) 给出 $B_i=\operatorname{End}(V_i)$。因此 (ii) 成立。$\square$

<span class="original-page-anchor" id="pdf-page-52" aria-hidden="true"></span>

## 3.3. 矩阵代数直和的表示

本节考虑代数 $A=\bigoplus_i\operatorname{Mat}_{d_i}(k)$ 的表示，其中 $k$ 可以是任意域。

**定理 3.3.1.** 设 $A=\bigoplus_{i=1}^r\operatorname{Mat}_{d_i}(k)$。那么，$A$ 的不可约表示为 $V_1=k^{d_1},\ldots,V_r=k^{d_r}$，而 $A$ 的任意有限维表示都是若干个 $V_1,\ldots,V_r$ 的直和。

为了证明定理 3.3.1，我们需要对偶表示的概念。

**定义 3.3.2（对偶表示）。** 设 $V$ 是任意代数 $A$ 的一个表示。那么，**对偶表示** $V^*$ 是反代数 $A^{\mathrm{op}}$ 的表示（等价地，是右 $A$-模），其作用为

$$
(f\cdot a)(v):=f(av).
$$

**定理 3.3.1 的证明。** 首先，所列的表示显然不可约，因为对任意 $v\ne0$、$w\in V_i$，都存在 $a\in A$，使 $av=w$。接着，设 $X$ 是 $A$ 的一个 $n$ 维表示。那么，$X^*$ 是 $A^{\mathrm{op}}$ 的一个 $n$ 维表示。由于 $(BC)^T=C^TB^T$，映射 $\varphi(X)=X^T$ 给出同构 $(\operatorname{Mat}_{d_i}(k))^{\mathrm{op}}\cong\operatorname{Mat}_{d_i}(k)$。因此，$A\cong A^{\mathrm{op}}$，可以把 $X^*$ 看成 $A$ 的一个 $n$ 维表示。定义

$$
\phi:\underbrace{A\oplus\cdots\oplus A}_{n\text{份}}\longrightarrow X^*
$$

其公式为

$$
\phi(a_1,\ldots,a_n)=a_1y_1+\cdots+a_ny_n,
$$

其中 $\{y_i\}$ 是 $X^*$ 的一组基。由于 $k\subset A$，映射 $\phi$ 显然是满射。所以，对偶映射 $\phi^*:X\longrightarrow A^{n*}$ 是单射。但 $A^{n*}\cong A^n$ 作为 $A$ 的表示成立（请验证！）。因此，$\operatorname{Im}\phi^*\cong X$ 是 $A^n$ 的一个子表示。又因为 $\operatorname{Mat}_{d_i}(k)=d_iV_i$，所以作为 $A$ 的表示，有 $A=\bigoplus_{i=1}^r d_iV_i$、$A^n=\bigoplus_{i=1}^r nd_iV_i$。由命题 3.1.4，$X=\bigoplus_{i=1}^r m_iV_i$，结论得证。$\square$

<span class="original-page-anchor" id="pdf-page-53" aria-hidden="true"></span>

**习题 3.3.3.** 本题要求为定理 3.3.1 给出另一种证明，不使用本章前面任何结果。

设 $A_1,A_2,\ldots,A_n$ 是 $n$ 个代数，单位元分别为 $1_1,1_2,\ldots,1_n$。令 $A=A_1\oplus A_2\oplus\cdots\oplus A_n$。显然，$1_i1_j=\delta_{ij}1_i$，而 $A$ 的单位元为 $1=1_1+1_2+\cdots+1_n$。

对 $A$ 的任意表示 $V$，容易看出，对每个 $i\in\{1,2,\ldots,n\}$，$1_iV$ 都是 $A_i$ 的表示。反过来，如果 $V_1,V_2,\ldots,V_n$ 分别是 $A_1,A_2,\ldots,A_n$ 的表示，那么 $V_1\oplus V_2\oplus\cdots\oplus V_n$ 自然成为 $A$ 的表示，其中 $(a_1,a_2,\ldots,a_n)\in A$ 在这个直和上的作用为 $(v_1,v_2,\ldots,v_n)\mapsto(a_1v_1,a_2v_2,\ldots,a_nv_n)$。

(a) 证明：$A$ 的表示 $V$ 不可约，当且仅当恰好有一个 $i\in\{1,2,\ldots,n\}$，使 $1_iV$ 是 $A_i$ 的不可约表示，而对其余所有 $i$，都有 $1_iV=0$。由此，利用 $A_1,A_2,\ldots,A_n$ 的不可约表示，分类 $A$ 的不可约表示。

(b) 设 $d\in\mathbb{N}$。证明：$\operatorname{Mat}_d(k)$ 唯一的不可约表示是 $k^d$，而它的每个有限维表示都是若干个 $k^d$ 的直和。

提示：对每个 $(i,j)\in\{1,2,\ldots,d\}^2$，令 $E_{ij}\in\operatorname{Mat}_d(k)$ 为第 $i$ 行第 $j$ 列的元素是 $1$、其余元素都是 $0$ 的矩阵。设 $V$ 是 $\operatorname{Mat}_d(k)$ 的一个有限维表示。证明 $V=E_{11}V\oplus E_{22}V\oplus\cdots\oplus E_{dd}V$，且对每个 $i\in\{1,2,\ldots,d\}$，映射 $\Phi_i:E_{11}V\to E_{ii}V$、$v\mapsto E_{i1}v$ 都是同构。对每个非零 $v\in E_{11}V$，记 $S(v)=\langle E_{11}v,E_{21}v,\ldots,E_{d1}v\rangle$。证明 $S(v)$ 是 $V$ 的一个子表示，作为 $\operatorname{Mat}_d(k)$ 的表示同构于 $k^d$，并且 $v\in S(v)$。进而得出 $V=S(v_1)\oplus S(v_2)\oplus\cdots\oplus S(v_k)$，其中 $\{v_1,v_2,\ldots,v_k\}$ 是 $E_{11}V$ 的一组基。

**译校注：** 原文未要求 $v$ 非零；但 $S(0)=0$ 不同构于 $k^d$，因此在此补上非零条件。

(c) 推出定理 3.3.1。

## 3.4. 滤过

设 $A$ 是一个代数，$V$ 是 $A$ 的一个表示。

**定义 3.4.1.** $V$ 的一个（有限）**滤过**是子表示序列 $0=V_0\subset V_1\subset\cdots\subset V_n=V$。

<span class="original-page-anchor" id="pdf-page-54" aria-hidden="true"></span>

**引理 3.4.2.** 代数 $A$ 的任意有限维表示 $V$ 都有一个有限滤过 $0=V_0\subset V_1\subset\cdots\subset V_n=V$，使相邻商 $V_i/V_{i-1}$ 不可约。

**证明。** 对 $\dim(V)$ 作归纳。归纳起点显然，只需证明归纳步骤。取不可约子表示 $V_1\subset V$，并考虑表示 $U=V/V_1$。由归纳假设，$U$ 有一个滤过 $0=U_0\subset U_1\subset\cdots\subset U_{n-1}=U$，使 $U_i/U_{i-1}$ 不可约。对 $i\ge2$，令 $V_i$ 为 $U_{i-1}$ 在自然投影 $V\to V/V_1=U$ 下的原像。这样，$0=V_0\subset V_1\subset V_2\subset\cdots\subset V_n=V$ 就是具有所需性质的 $V$ 的滤过。$\square$

## 3.5. 有限维代数

**定义 3.5.1.** 有限维代数 $A$ 的**根基**，是 $A$ 中在所有不可约表示上都作用为 $0$ 的元素组成的集合，记为 $\operatorname{Rad}(A)$。

**命题 3.5.2.** $\operatorname{Rad}(A)$ 是一个双边理想。

**证明。** 容易证明。$\square$

**命题 3.5.3.** 设 $A$ 是一个有限维代数。

(i) 设 $I$ 是 $A$ 的一个幂零双边理想，即对某个 $n$，有 $I^n=0$。那么 $I\subset\operatorname{Rad}(A)$。

(ii) $\operatorname{Rad}(A)$ 是幂零理想。因此，$\operatorname{Rad}(A)$ 是 $A$ 中最大的幂零双边理想。

**证明。** (i) 设 $V$ 是 $A$ 的一个不可约表示，$v\in V$。那么 $Iv\subset V$ 是一个子表示。如果 $Iv\ne0$，就有 $Iv=V$，所以存在 $x\in I$，使 $xv=v$。于是 $x^n\ne0$，矛盾。因此 $Iv=0$，即 $I$ 在 $V$ 上作用为 $0$，从而 $I\subset\operatorname{Rad}(A)$。

(ii) 取 $A$ 的正则表示的一个子表示滤过 $0=A_0\subset A_1\subset\cdots\subset A_n=A$，使 $A_{i+1}/A_i$ 不可约。由引理 3.4.2，这样的滤过存在。取 $x\in\operatorname{Rad}(A)$。那么 $x$ 在 $A_{i+1}/A_i$ 上作用为零，所以 $x$ 把 $A_{i+1}$ 映入 $A_i$。由此得到 $\operatorname{Rad}(A)^n=0$，结论得证。$\square$

<span class="original-page-anchor" id="pdf-page-55" aria-hidden="true"></span>

**定理 3.5.4.** 在同构意义下，有限维代数 $A$ 只有有限多个不可约表示 $V_i$。这些表示都是有限维的，并且

$$
A/\operatorname{Rad}(A)\cong\bigoplus_i\operatorname{End}V_i.
$$

**证明。** 首先，对 $A$ 的任意不可约表示 $V$ 以及任意非零 $v\in V$，$Av\subseteq V$ 是 $V$ 的一个有限维子表示。（因为 $A$ 有限维，所以它也有限维。）由于 $V$ 不可约且 $Av\ne0$，有 $V=Av$，所以 $V$ 有限维。

接着，假设我们有两两不同构的不可约表示 $V_1,V_2,\ldots,V_r$。由定理 3.2.2，同态

$$
\bigoplus_i\rho_i:A\longrightarrow\bigoplus_i\operatorname{End}V_i
$$

是满射。因此 $r\le\sum_i\dim\operatorname{End}V_i\le\dim A$。所以，$A$ 只有有限多个两两不同构的不可约表示，个数不超过 $\dim A$。

现在，设 $V_1,V_2,\ldots,V_r$ 是 $A$ 的所有两两不同构的有限维不可约表示。由定理 3.2.2，同态

$$
\bigoplus_i\rho_i:A\longrightarrow\bigoplus_i\operatorname{End}V_i
$$

是满射。按定义，这个映射的核恰好是 $\operatorname{Rad}(A)$。$\square$

**推论 3.5.5.** $\sum_i(\dim V_i)^2\le\dim A$，其中 $V_i$ 是 $A$ 的不可约表示。

**证明。** 因为 $\dim\operatorname{End}V_i=(\dim V_i)^2$，定理 3.5.4 给出 $\dim A-\dim\operatorname{Rad}(A)=\sum_i\dim\operatorname{End}V_i=\sum_i(\dim V_i)^2$。又因为 $\dim\operatorname{Rad}(A)\ge0$，所以 $\sum_i(\dim V_i)^2\le\dim A$。$\square$

**例 3.5.6.** 1. 设 $A=k[x]/(x^n)$。这个代数只有一个不可约表示，即一维空间 $k$，其中 $x$ 作用为零。因此，根基 $\operatorname{Rad}(A)$ 就是理想 $(x)$。

2. 设 $A$ 是上三角 $n\times n$ 矩阵组成的代数。容易验证，$A$ 的不可约表示为 $V_i$（$i=1,\ldots,n$），它们都是一维的，任意矩阵 $x$ 在 $V_i$ 上以 $x_{ii}$ 作用。

<span class="original-page-anchor" id="pdf-page-56" aria-hidden="true"></span>

因此，根基 $\operatorname{Rad}(A)$ 就是严格上三角矩阵组成的理想，因为这个理想幂零且包含根基。分块三角矩阵也有类似的结果。

**定义 3.5.7.** 如果 $\operatorname{Rad}(A)=0$，就称有限维代数 $A$ 是**半单**的。

**命题 3.5.8.** 对有限维代数 $A$，以下条件等价：

(1) $A$ 是半单的。

(2) $\sum_i(\dim V_i)^2=\dim A$，其中 $V_i$ 是 $A$ 的不可约表示。

(3) 对某些 $d_i$，有 $A\cong\bigoplus_i\operatorname{Mat}_{d_i}(k)$。

(4) $A$ 的任意有限维表示都是完全可约的，即同构于不可约表示的直和。

(5) $A$ 作为自身的表示是完全可约的。

**证明。** 由于 $\dim A-\dim\operatorname{Rad}(A)=\sum_i(\dim V_i)^2$，显然 $\dim A=\sum_i(\dim V_i)^2$ 当且仅当 $\operatorname{Rad}(A)=0$。因此，$(1)\Leftrightarrow(2)$。

由定理 3.5.4，如果 $\operatorname{Rad}(A)=0$，那么显然有 $A\cong\bigoplus_i\operatorname{Mat}_{d_i}(k)$，其中 $d_i=\dim V_i$。所以 $(1)\Rightarrow(3)$。反过来，如果 $A\cong\bigoplus_i\operatorname{Mat}_{d_i}(k)$，那么由定理 3.3.1，$\operatorname{Rad}(A)=0$，所以 $A$ 是半单的。因此 $(3)\Rightarrow(1)$。

接下来，定理 3.3.1 给出 $(3)\Rightarrow(4)$，而 $(4)\Rightarrow(5)$ 显然成立。为了证明 $(5)\Rightarrow(3)$，设 $A=\bigoplus_i n_iV_i$。考虑 $\operatorname{End}_A(A)$，即 $A$ 作为自身的表示时的自同态代数。由于 $V_i$ 两两不同构，Schur 引理表明，从 $A$ 中任意一个 $V_i$ 到不同的 $V_j$ 的表示同态都为零。再次用 Schur 引理，得到 $\operatorname{End}_A(V_i)=k$。于是 $\operatorname{End}_A(A)\cong\bigoplus_i\operatorname{Mat}_{n_i}(k)$。但由习题 2.3.17，$\operatorname{End}_A(A)\cong A^{\mathrm{op}}$，所以 $A^{\mathrm{op}}\cong\bigoplus_i\operatorname{Mat}_{n_i}(k)$。因此，$A\cong(\bigoplus_i\operatorname{Mat}_{n_i}(k))^{\mathrm{op}}=\bigoplus_i\operatorname{Mat}_{n_i}(k)$，结论得证。$\square$

## 3.6. 表示的特征标

设 $A$ 是一个代数，$V$ 是 $A$ 的一个有限维表示，作用记为 $\rho$。那么，$V$ 的**特征标**是线性函数<span class="original-page-anchor" id="pdf-page-57" aria-hidden="true"></span>$\chi_V:A\longrightarrow k$，由下式给出：

$$
\chi_V(a)=\operatorname{Tr}|_V(\rho(a)).
$$

如果 $[A,A]$ 是所有 $x,y\in A$ 的交换子 $[x,y]:=xy-yx$ 张成的空间，那么 $[A,A]\subseteq\ker\chi_V$。因此，可以把特征标看成映射 $\chi_V:A/[A,A]\to k$。

**练习 3.6.1.** 证明：如果 $W\subset V$ 是 $A$ 的有限维表示，那么 $\chi_V=\chi_W+\chi_{V/W}$。

**定理 3.6.2.** (i) $A$ 的不同的有限维不可约表示的特征标线性无关。

(ii) 如果 $A$ 是一个有限维半单代数，那么这些特征标构成 $(A/[A,A])^*$ 的一组基。

**证明。** (i) 如果 $V_1,\ldots,V_r$ 是 $A$ 的两两不同构的有限维不可约表示，那么由稠密性定理，映射

$$
\rho_{V_1}\oplus\cdots\oplus\rho_{V_r}:A\to\operatorname{End}V_1\oplus\cdots\oplus\operatorname{End}V_r
$$

是满射，所以 $\chi_{V_1},\ldots,\chi_{V_r}$ 线性无关。（事实上，如果对所有 $a\in A$，都有 $\sum\lambda_i\chi_{V_i}(a)=0$，那么对所有 $M_i\in\operatorname{End}_k V_i$，都有 $\sum\lambda_i\operatorname{Tr}(M_i)=0$。但每个 $\operatorname{Tr}(M_i)$ 都可以独立地遍历 $k$，所以必有 $\lambda_1=\cdots=\lambda_r=0$。）

(ii) 首先证明 $[\operatorname{Mat}_d(k),\operatorname{Mat}_d(k)]=\mathfrak{sl}_d(k)$，即所有迹为 $0$ 的矩阵组成的空间。显然，$[\operatorname{Mat}_d(k),\operatorname{Mat}_d(k)]\subseteq\mathfrak{sl}_d(k)$。记 $E_{ij}$ 为第 $i$ 行第 $j$ 列的元素是 $1$、其余元素都是 $0$ 的矩阵。我们有 $[E_{ij},E_{jm}]=E_{im}$（$i\ne m$），以及 $[E_{i,i+1},E_{i+1,i}]=E_{ii}-E_{i+1,i+1}$。而 $\{E_{im}\}\cup\{E_{ii}-E_{i+1,i+1}\}$ 构成 $\mathfrak{sl}_d(k)$ 的一组基，所以确实有 $[\operatorname{Mat}_d(k),\operatorname{Mat}_d(k)]=\mathfrak{sl}_d(k)$。由半单性，可以写成 $A=\operatorname{Mat}_{d_1}(k)\oplus\cdots\oplus\operatorname{Mat}_{d_r}(k)$。于是 $[A,A]=\mathfrak{sl}_{d_1}(k)\oplus\cdots\oplus\mathfrak{sl}_{d_r}(k)$，且 $A/[A,A]\cong k^r$。由定理 3.3.1，$A$ 恰有 $r$ 个不可约表示，分别同构于 $k^{d_1},\ldots,k^{d_r}$。所以，在 $r$ 维向量空间 $A/[A,A]$ 上有 $r$ 个线性无关的特征标，它们构成一组基。$\square$

<span class="original-page-anchor" id="pdf-page-58" aria-hidden="true"></span>

## 3.7. 若尔当–赫尔德定理

下面叙述并证明关于有限维代数表示的两个重要定理：若尔当–赫尔德定理和克鲁尔–施密特定理。

**定理 3.7.1（若尔当–赫尔德定理）。** 设 $V$ 是 $A$ 的一个有限维表示，$0=V_0\subset V_1\subset\cdots\subset V_n=V$ 和 $0=V'_0\subset\cdots\subset V'_m=V$ 是 $V$ 的两个滤过，并且对所有 $i$，表示 $W_i:=V_i/V_{i-1}$ 与 $W'_i:=V'_i/V'_{i-1}$ 都不可约。那么，$n=m$，且存在 $1,\ldots,n$ 的一个置换 $\sigma$，使 $W_{\sigma(i)}$ 同构于 $W'_i$。

**证明。** *第一种证明*（$k$ 的特征为零时）。显然，$V$ 的特征标等于所有 $W_i$ 的特征标之和，也等于所有 $W'_i$ 的特征标之和。但由定理 3.6.2，不可约表示的特征标线性无关，所以 $A$ 的每个不可约表示 $W$ 在 $W_i$ 中和在 $W'_i$ 中的重数相同。定理由此得到。[^rt-58-2]

*第二种证明*（一般情形）。对 $\dim V$ 作归纳。归纳起点显然，下面证明归纳步骤。如果 $W_1=W'_1$（作为子空间相等），则由归纳假设，定理对 $V/W_1$ 成立，证明就完成了。因此，设 $W_1\ne W'_1$。由于 $W_1,W'_1$ 不可约，这时 $W_1\cap W'_1=0$，所以有嵌入 $f:W_1\oplus W'_1\to V$。令 $U=V/(W_1\oplus W'_1)$，并取 $U$ 的一个滤过 $0=U_0\subset U_1\subset\cdots\subset U_p=U$，使相邻商 $Z_i=U_i/U_{i-1}$ 为单表示（由引理 3.4.2，这样的滤过存在）。于是：

1) $V/W_1$ 有一个相邻商为 $W'_1,Z_1,\ldots,Z_p$ 的滤过，还有一个相邻商为 $W_2,\ldots,W_n$ 的滤过。

2) $V/W'_1$ 有一个相邻商为 $W_1,Z_1,\ldots,Z_p$ 的滤过，还有一个相邻商为 $W'_2,\ldots,W'_m$ 的滤过。

**译校注：** 原文第二项末尾为 $W'_n$；这里按作者勘误改为 $W'_m$，与第二个滤过的长度一致。

<span class="original-page-anchor" id="pdf-page-59" aria-hidden="true"></span>

由归纳假设，计入重数的不可约表示集合 $W_1,W'_1,Z_1,\ldots,Z_p$，一方面与 $W_1,\ldots,W_n$ 相同，另一方面与 $W'_1,\ldots,W'_m$ 相同。证明完成。$\square$

若尔当–赫尔德定理说明，$V$ 的相邻商不可约的滤过中，商的个数 $n$ 不依赖于滤过的选择，只依赖于 $V$。这个数称为 $V$ 的**长度**。容易看出，$n$ 也是 $V$ 的所有包含关系均严格的滤过所能达到的最大长度。

在 $V$ 的某个滤过中，将不可约表示 $W_1,\ldots,W_n$ 按它们作为相邻商出现的顺序排列，所得序列称为 $V$ 的一个**若尔当–赫尔德列**。

## 3.8. 克鲁尔–施密特定理

**定理 3.8.1（克鲁尔–施密特定理）。** $A$ 的任意有限维表示都能分解为不可分解表示的直和，并且这种分解在同构及直和项的顺序意义下唯一。

**证明。** 显然，$V$ 可以分解为不可分解表示的直和，所以只需证明唯一性。我们对 $\dim V$ 作归纳。设 $V=V_1\oplus\cdots\oplus V_m=V'_1\oplus\cdots\oplus V'_n$。记与这两个分解相应的自然映射为 $i_s:V_s\to V$、$i'_s:V'_s\to V$、$p_s:V\to V_s$、$p'_s:V\to V'_s$。令 $\theta_s=p_1i'_sp'_si_1:V_1\to V_1$。我们有 $\sum_{s=1}^n\theta_s=1$。现在需要以下引理。

**引理 3.8.2.** 设 $W$ 是 $A$ 的一个有限维不可分解表示。那么：

(i) 任意同态 $\theta:W\to W$，要么是同构，要么幂零。

(ii) 如果同态 $\theta_s:W\to W$（$s=1,\ldots,n$）都幂零，那么 $\theta:=\theta_1+\cdots+\theta_n$ 也幂零。

<span class="original-page-anchor" id="pdf-page-60" aria-hidden="true"></span>

**证明。** (i) $\theta$ 的广义特征子空间是 $W$ 的子表示，而 $W$ 是它们的直和。因此，$\theta$ 只能有一个特征值 $\lambda$。如果 $\lambda$ 为零，$\theta$ 就幂零；否则它是同构。

(ii) 对 $n$ 作归纳。归纳起点显然。为了证明从 $n-1$ 到 $n$ 的归纳步骤，假设 $\theta$ 不幂零。那么由 (i)，$\theta$ 是同构，所以 $\sum_{i=1}^n\theta^{-1}\theta_i=1$。态射 $\theta^{-1}\theta_i$ 都不是同构，因此都幂零。于是 $1-\theta^{-1}\theta_n=\theta^{-1}\theta_1+\cdots+\theta^{-1}\theta_{n-1}$ 是同构，这与归纳假设矛盾。$\square$

**译校注：** 原文求和下限印为 $i=0$，但这里只定义了 $\theta_1,\ldots,\theta_n$，因此改为 $i=1$。

由引理，某个 $\theta_s$ 必须是同构；不妨设 $s=1$。这时，$V'_1=\operatorname{Im}(p'_1i_1)\oplus\operatorname{Ker}(p_1i'_1)$。由于 $V'_1$ 不可分解，得到 $f:=p'_1i_1:V_1\to V'_1$ 和 $g:=p_1i'_1:V'_1\to V_1$ 都是同构。

令 $B=\bigoplus_{j>1}V_j$、$B'=\bigoplus_{j>1}V'_j$，则 $V=V_1\oplus B=V'_1\oplus B'$。考虑与这两个分解相应的自然映射的复合 $h:B\to V\to B'$。我们断言 $h$ 是同构。因为 $h$ 的定义域和值域维数相同，只需证明 $\operatorname{Ker}h=0$。设 $v\in\operatorname{Ker}h\subset B$，那么 $v\in V'_1$。另一方面，$v$ 到 $V_1$ 的投影为零，所以 $gv=0$。由于 $g$ 是同构，得到 $v=0$，断言得证。

现在由归纳假设，$m=n$，并且存在 $2,\ldots,n$ 的某个置换 $\sigma$，使 $V_j\cong V'_{\sigma(j)}$。定理得证。$\square$

**习题 3.8.3.** 上面对引理 3.8.2 的证明用了 $k$ 是代数闭域这一条件。不使用这一条件，证明引理 3.8.2，从而证明克鲁尔–施密特定理。

**习题 3.8.4.** (i) 设 $V,W$ 是域 $K$ 上代数 $A$ 的有限维表示，这里 $K$ 不一定是代数闭域。设 $L$ 是 $K$ 的一个域扩张。假设 $V\otimes_K L$ 与 $W\otimes_K L$ 作为 $L$-代数 $A\otimes_K L$ 的模同构。证明 $V$ 与 $W$ 作为 $A$-模同构。

提示：先归结到有限生成扩张的情形，再归结到某个次数为 $n$ 的有限扩张的情形。然后，把 $V\otimes_K L$ 与 $W\otimes_K L$ 看成<span class="original-page-anchor" id="pdf-page-61" aria-hidden="true"></span>$A$-模，并证明它们分别同构于 $V^n$ 和 $W^n$。由此得出 $V^n$ 同构于 $W^n$，再利用克鲁尔–施密特定理（由习题 3.8.3，它在任意域上都成立），推出 $V$ 同构于 $W$。

(ii)（Noether–Deuring 定理）在 (i) 的条件下，假设 $V\otimes_K L$ 是 $W\otimes_K L$ 的一个直和项，即 $W\otimes_K L\cong V\otimes_K L\oplus Y$，其中 $Y$ 是 $A\otimes_K L$ 的一个模。证明 $V$ 是 $W$ 的一个直和项。

**习题 3.8.5.** 设 $A$ 是 $\mathbb{R}$ 上周期为 $1$ 的实值连续函数组成的代数。设 $M$ 是 $\mathbb{R}$ 上反周期为 $1$ 的连续函数 $f$ 组成的 $A$-模，即 $f(x+1)=-f(x)$。

(i) 证明 $A$ 和 $M$ 都是不可分解的 $A$-模。

(ii) 证明 $A$ 不同构于 $M$，但 $A\oplus A$ 同构于 $M\oplus M$。

**注 3.8.6.** 由此可见，克鲁尔–施密特定理一般不适用于无限维模。不过，它仍然适用于**有限长度**的模，即存在某个常数 $l=l(M)$，使模 $M$ 的任何滤过的长度都不超过 $l$。

## 3.9. 习题

**习题 3.9.1. 表示的扩张。** 设 $A$ 是一个代数，$V,W$ 是 $A$ 的两个表示。我们想分类 $A$ 的所有满足下列条件的表示 $U$：$V$ 是 $U$ 的子表示，且 $U/V=W$。当然，$U=V\oplus W$ 是一个显然的例子，但还有别的例子吗？

假设有上述表示 $U$。作为向量空间，它可以与 $V\oplus W$ 等同，但这种等同并不唯一。于是，对任意 $a\in A$，相应的算子 $\rho_U(a)$ 都具有分块三角形式

$$
\rho_U(a)=\begin{pmatrix}\rho_V(a)&f(a)\\0&\rho_W(a)\end{pmatrix},
$$

其中 $f:A\to\operatorname{Hom}_k(W,V)$ 是线性映射。

(a) $f(a)$ 满足什么充要条件时，$\rho_U(a)$ 给出一个表示？满足这个条件的映射 $f$ 称为<span class="original-page-anchor" id="pdf-page-62" aria-hidden="true"></span>**1-上闭链**（指 $A$ 的、以 $\operatorname{Hom}_k(W,V)$ 为系数的上闭链）。它们组成一个向量空间，记为 $Z^1(W,V)$。

(b) 设 $X:W\to V$ 是线性映射。定义 $X$ 的上边缘 $dX$ 为函数 $A\to\operatorname{Hom}_k(W,V)$，其公式是 $dX(a)=\rho_V(a)X-X\rho_W(a)$。证明 $dX$ 是上闭链，并且 $dX$ 为零当且仅当 $X$ 是表示的同态。因此，上边缘组成一个子空间 $B^1(W,V)\subset Z^1(W,V)$，它同构于 $\operatorname{Hom}_k(W,V)/\operatorname{Hom}_A(W,V)$。商空间 $Z^1(W,V)/B^1(W,V)$ 记为 $\operatorname{Ext}^1(W,V)$。

(c) 证明：如果 $f,f'\in Z^1(W,V)$，且 $f-f'\in B^1(W,V)$，那么相应的扩张 $U,U'$ 作为 $A$ 的表示同构。反过来，如果 $\phi:U\to U'$ 是同构，且

$$
\phi=\begin{pmatrix}1_V&*\\0&1_W\end{pmatrix},
$$

那么 $f-f'\in B^1(W,V)$。因此，空间 $\operatorname{Ext}^1(W,V)$ “分类”了用 $V$ 对 $W$ 作的扩张。

**译校注：** 原式左端为 $\phi(a)$，按作者勘误改为 $\phi$。紧接着的 $B^1(V,W)$ 改为 $B^1(W,V)$，因为 $f,f'$ 都取值于 $\operatorname{Hom}_k(W,V)$，其差应属于 (b) 中定义的上边缘空间。

(d) 设 $W,V$ 是 $A$ 的有限维不可约表示。对任意 $f\in\operatorname{Ext}^1(W,V)$，令 $U_f$ 为相应的扩张。证明：$U_f$ 与 $U_{f'}$ 作为表示同构，当且仅当 $f$ 与 $f'$ 成比例。因此，非平凡的用 $V$ 对 $W$ 作的扩张（即不同构于 $W\oplus V$ 的扩张），其作为表示的同构类由射影空间 $\mathbb{P}\operatorname{Ext}^1(W,V)$ 参数化。特别地，每个扩张都平凡，当且仅当 $\operatorname{Ext}^1(W,V)=0$。

**习题 3.9.2.** (a) 设 $A=\mathbb{C}[x_1,\ldots,x_n]$，$V_a,V_b$ 是一维表示，其中元素 $x_i$ 分别以 $a_i$ 和 $b_i$ 作用（$a_i,b_i\in\mathbb{C}$）。求 $\operatorname{Ext}^1(V_a,V_b)$，并分类 $A$ 的二维表示。

(b) 设 $B$ 是由 $x_1,\ldots,x_n$ 生成的 $\mathbb{C}$ 上的代数，定义关系为对所有 $i,j$，都有 $x_ix_j=0$。证明：当 $n>1$ 时，代数 $B$ 有无穷多个两两不同构的不可分解表示。

**习题 3.9.3.** 设 $Q$ 是没有有向圈的箭图，$P_Q$ 是 $Q$ 的路径代数。求 $P_Q$ 的不可约表示，并计算它们之间的 $\operatorname{Ext}^1$。分类 $P_Q$ 的二维表示。

<span class="original-page-anchor" id="pdf-page-63" aria-hidden="true"></span>

**习题 3.9.4.** 设 $A$ 是一个代数，$V$ 是 $A$ 的一个表示，$\rho:A\to\operatorname{End}V$。$V$ 的一个**形式形变**是形式级数

$$
\widetilde{\rho}=\rho_0+t\rho_1+\cdots+t^n\rho_n+\cdots,
$$

其中 $\rho_i:A\to\operatorname{End}(V)$ 是线性映射，$\rho_0=\rho$，并且 $\widetilde{\rho}(ab)=\widetilde{\rho}(a)\widetilde{\rho}(b)$。

如果 $b(t)=1+b_1t+b_2t^2+\cdots$，其中 $b_i\in\operatorname{End}(V)$，且 $\widetilde{\rho}$ 是 $\rho$ 的一个形式形变，那么 $b\widetilde{\rho}b^{-1}$ 也是 $\rho$ 的形变，称它与 $\widetilde{\rho}$ 同构。

(a) 证明：如果 $\operatorname{Ext}^1(V,V)=0$，那么 $\rho$ 的任意形变都是平凡的，即同构于 $\rho$。

(b) (a) 的逆命题成立吗？（考虑对偶数代数 $A=k[x]/x^2$。）

**习题 3.9.5. Clifford 代数。** 设 $V$ 是一个有限维复向量空间，带有一个对称双线性型 $(\ ,\ )$。**Clifford 代数** $\operatorname{Cl}(V)$ 是张量代数 $TV$ 对所有元素 $v\otimes v-(v,v)1$（$v\in V$）生成的理想取商所得的代数。更具体地说，如果 $x_i$（$1\le i\le N$）是 $V$ 的一组基，且 $(x_i,x_j)=a_{ij}$，那么 $\operatorname{Cl}(V)$ 由 $x_i$ 生成，定义关系为

$$
x_ix_j+x_jx_i=2a_{ij},\qquad x_i^2=a_{ii}.
$$

因此，如果 $(\ ,\ )=0$，就有 $\operatorname{Cl}(V)=\wedge V$。

(i) 证明：如果 $(\ ,\ )$ 非退化，那么 $\operatorname{Cl}(V)$ 是半单的。当 $\dim V=2n$ 时，它只有一个不可约表示，维数为 $2^n$，所以这时 $\operatorname{Cl}(V)$ 是矩阵代数；当 $\dim(V)=2n+1$ 时，它有两个这样的表示，即这时 $\operatorname{Cl}(V)$ 是两个矩阵代数的直和。

提示：在偶数维情形，取 $V$ 的一组基 $a_1,\ldots,a_n,b_1,\ldots,b_n$，使 $(a_i,a_j)=(b_i,b_j)=0$、$(a_i,b_j)=\delta_{ij}/2$。在 $S:=\wedge(a_1,\ldots,a_n)$ 上构造 $\operatorname{Cl}(V)$ 的一个表示，使 $b_i$ 的作用是关于 $a_i$ 的“求导”。证明 $S$ 不可约。奇数维情形与此类似，只是要再添一个基向量 $c$，使 $(c,a_i)=(c,b_i)=0$、$(c,c)=1$。$c$ 在 $S$ 上的作用可以定义为 $(-1)^{\text{次数}}$，也可以定义为 $(-1)^{\text{次数}+1}$，由此得到两个表示 $S_+,S_-$（为什么它们不同构？）。

<span class="original-page-anchor" id="pdf-page-64" aria-hidden="true"></span>

找出 $\operatorname{Cl}(V)$ 的一个含 $2^{\dim V}$ 个元素的张成集，从而证明不存在其他不可约表示。

(ii) 证明：$\operatorname{Cl}(V)$ 是半单的，当且仅当 $(\ ,\ )$ 非退化。如果 $(\ ,\ )$ 退化，那么 $\operatorname{Cl}(V)/\operatorname{Rad}(\operatorname{Cl}(V))$ 是什么？

## 3.10. 张量积的表示

设 $A,B$ 是两个代数。那么 $A\otimes B$ 也是代数，其乘法为 $(a_1\otimes b_1)(a_2\otimes b_2)=a_1a_2\otimes b_1b_2$。

**练习 3.10.1.** 证明 $\operatorname{Mat}_m(k)\otimes\operatorname{Mat}_n(k)\cong\operatorname{Mat}_{mn}(k)$。

下面的定理用 $A$ 和 $B$ 的有限维不可约表示，描述 $A\otimes B$ 的有限维不可约表示。

**定理 3.10.2.** (i) 设 $V$ 是 $A$ 的一个有限维不可约表示，$W$ 是 $B$ 的一个有限维不可约表示。那么 $V\otimes W$ 是 $A\otimes B$ 的不可约表示。

(ii) $A\otimes B$ 的任意有限维不可约表示 $M$ 都具有 (i) 中的形式，且 $V,W$ 唯一确定。

**注 3.10.3.** 对无限维表示，定理的 (ii) 通常不成立，例如当 $A$ 是特征为零时的 Weyl 代数，就不成立。(i) 也可能不成立。例如，令 $A=B=V=W=\mathbb{C}(x)$，这时由于 $A\otimes B$ 不是域，(i) 不成立。

**证明。** (i) 由稠密性定理，映射 $A\to\operatorname{End}V$ 与 $B\to\operatorname{End}W$ 都是满射。因此，映射 $A\otimes B\to\operatorname{End}V\otimes\operatorname{End}W=\operatorname{End}(V\otimes W)$ 是满射。所以 $V\otimes W$ 不可约。

(ii) 首先证明 $V,W$ 存在。设 $A',B'$ 分别为 $A,B$ 在 $\operatorname{End}M$ 中的像。那么 $A',B'$ 是有限维代数，而 $M$ 是 $A'\otimes B'$ 的一个表示。因此，不失一般性，可以假设 $A,B$ 都有限维。

在这种情形下，我们断言

$$
\operatorname{Rad}(A\otimes B)=\operatorname{Rad}(A)\otimes B+A\otimes\operatorname{Rad}(B).
$$

<span class="original-page-anchor" id="pdf-page-65" aria-hidden="true"></span>

事实上，把右端记为 $J$。由于 $\operatorname{Rad}(A)$ 与 $\operatorname{Rad}(B)$ 都幂零，$J$ 是 $A\otimes B$ 的一个幂零理想。另一方面，$(A\otimes B)/J=(A/\operatorname{Rad}(A))\otimes(B/\operatorname{Rad}(B))$ 是两个半单代数的张量积，因而也是半单的。这给出 $J\supset\operatorname{Rad}(A\otimes B)$。综合起来，由命题 3.5.3，得到 $J=\operatorname{Rad}(A\otimes B)$，断言得证。

于是，我们得到

$$
(A\otimes B)/\operatorname{Rad}(A\otimes B)=A/\operatorname{Rad}(A)\otimes B/\operatorname{Rad}(B).
$$

现在，$M$ 是 $(A\otimes B)/\operatorname{Rad}(A\otimes B)$ 的一个不可约表示，所以显然具有形式 $M=V\otimes W$，其中 $V$ 是 $A/\operatorname{Rad}(A)$ 的不可约表示，$W$ 是 $B/\operatorname{Rad}(B)$ 的不可约表示。而且，$V,W$ 由 $M$ 唯一确定，因为涉及的所有代数都是矩阵代数的直和。$\square$

[^rt-50-1]: 也可以对 $n$ 作归纳来证明 $P$ 的存在性，这种证明不需要 $V$ 有限维。具体来说，如果 $W$ 本身不是不可约表示，就令 $K$ 为把 $W$ 投影到第一个直和项 $V_1$ 的映射的核。由于 $W$ 不是不可约表示，$K$ 是 $(n_1-1)V_1\oplus\cdots\oplus n_mV_m$ 的一个非零子表示，所以由归纳假设，$K$ 包含一个不可约子表示。

[^rt-58-2]: 这一证明在特征为 $p$ 时不成立，因为它只能说明 $W_i$ 与 $W'_i$ 的重数模 $p$ 相同，而这还不够。事实上，对任意表示 $V$，表示 $pV$ 的特征标都是零。
