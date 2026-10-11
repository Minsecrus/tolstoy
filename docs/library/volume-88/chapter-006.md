---
title: "第六章 箭图表示"
description: "《Introduction to Representation Theory》中文译文。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"第五章 有限群的表示：进一步的结果","link":"/library/volume-88/chapter-005"}
next: {"text":"第七章 范畴导论","link":"/library/volume-88/chapter-007"}
---

# 第六章 箭图表示

<span class="original-page-anchor" id="pdf-page-153" aria-hidden="true"></span>

## 6.1. 习题

**习题 6.1.1. 域嵌入。** 回顾一下，$k(y_1,\ldots,y_m)$ 表示域 $k$ 上关于 $y_1,\ldots,y_m$ 的有理函数域。设 $f:k[x_1,\ldots,x_n]\to k(y_1,\ldots,y_m)$ 是单射的 $k$-代数同态。证明 $m\ge n$。（考察 $N\to\infty$ 时，关于 $x_i$ 的 $N$ 次多项式空间 $W_N$ 及其在 $f$ 下的像的维数如何增长。）由此推出：若 $f:k(x_1,\ldots,x_n)\to k(y_1,\ldots,y_m)$ 是 $k$-线性的域嵌入，则 $m\ge n$。

**习题 6.1.2. 一点代数几何。** 设 $k$ 是代数闭域，$G=GL_n(k)$，$V$ 是 $G$ 的代数表示。证明：若 $G$ 在 $V$ 上只有有限个轨道，则 $\dim(V)\le n^2$。具体步骤如下：

(a) 设 $x_1,\ldots,x_N$ 是 $V$ 上的线性坐标。如果每个在 $X$ 上恒为零的多项式 $f(x_1,\ldots,x_N)$ 都是零多项式，即每个系数都为零，就称 $V$ 的子集 $X$ 是 **Zariski 稠密**的。证明：若 $G$ 在 $V$ 上只有有限个轨道，则至少有一个轨道在 $V$ 中 Zariski 稠密。

(b) 用 (a) 构造域嵌入 $k(x_1,\ldots,x_N)\to k(g_{pq})$，然后使用习题 6.1.1。

(c) 将本题的结论推广到 $G=GL_{n_1}(k)\times\cdots\times GL_{n_m}(k)$ 的情形。

<span class="original-page-anchor" id="pdf-page-154" aria-hidden="true"></span>

**习题 6.1.3. Dynkin 图。** 设 $\Gamma$ 是一个图，即由有限个点（顶点）和连接这些点的若干条边组成；这里允许重边。假设 $\Gamma$ 连通，即任意两个顶点都可以用一条边路径连接，并且没有自环，即连接某个顶点与其自身的边。将 $\Gamma$ 的各个顶点标记为整数 $1,\ldots,N$，便可给它对应一个 $N\times N$ 矩阵 $R_\Gamma=(r_{ij})$，其中 $r_{ij}$ 是连接顶点 $i$ 和 $j$ 的边数。这个矩阵显然是对称的，称为**邻接矩阵**。定义矩阵 $A_\Gamma=2I-R_\Gamma$，其中 $I$ 是单位矩阵。

**定义 6.1.4.** 如果矩阵 $A_\Gamma$ 在 $\mathbb R^N$ 上定义的二次型正定，就称 $\Gamma$ 是 **Dynkin 图**。

Dynkin 图出现在数学的许多领域中，例如奇点理论、李代数、表示论、代数几何和数学物理。本题将给出 Dynkin 图的完整分类，也就是说，你将证明下面的定理。

**定理.** $\Gamma$ 是 Dynkin 图，当且仅当它是下面这些图之一：

![A_N](/library/volume-88/diagrams/pdf-0154-an.png)

![D_N](/library/volume-88/diagrams/pdf-0154-dn.png)

![E_6](/library/volume-88/diagrams/pdf-0154-e6.png)

<span class="original-page-anchor" id="pdf-page-155" aria-hidden="true"></span>

![E_7](/library/volume-88/diagrams/pdf-0155-e7.png)

![E_8](/library/volume-88/diagrams/pdf-0155-e8.png)

(a) 计算 $\Gamma=A_N,D_N$ 时 $A_\Gamma$ 的行列式。（按行展开，并写出相应的递推方程。）用 Sylvester 判别法推出 $A_N,D_N$ 都是 Dynkin 图。[^sylvester-155]

(b) 计算 $E_6,E_7,E_8$ 对应的 $A_\Gamma$ 的行列式，方法是按行展开，将问题归结为 (a)。证明它们都是 Dynkin 图。

(c) 证明 Dynkin 图 $\Gamma$ 不可能含有环。为此，证明下图 $\Gamma$ 满足 $\det(A_\Gamma)=0$：[^labels-155]

![环](/library/volume-88/diagrams/pdf-0155-cycle.png)

（证明各行之和为 $0$。）因此，$\Gamma$ 必须是一棵树。

(d) 证明 Dynkin 图 $\Gamma$ 不可能含有连接四条或更多边的顶点，而且至多只能有一个连接三条边的顶点。为此，证明下图 $\Gamma$ 满足 $\det(A_\Gamma)=0$：

![两个分支顶点](/library/volume-88/diagrams/pdf-0155-fork.png)

(e) 证明下面的所有图 $\Gamma$ 都满足 $\det(A_\Gamma)=0$：

<span class="original-page-anchor" id="pdf-page-156" aria-hidden="true"></span>

![仿射 Dynkin 图](/library/volume-88/diagrams/pdf-0156-affine.png)

(f) 从 (a)–(e) 推出 Dynkin 图的分类定理。

(g) （单边的）**仿射 Dynkin 图**是没有自环的连通图，而且 $A_\Gamma$ 所定义的二次型半正定但不正定。分类所有仿射 Dynkin 图。（证明它们恰好就是 (c)–(e) 中排除的那些图。）

**译校注：** 原文定义只要求“半正定”，有限 Dynkin 图也满足这一条件。为与本题紧后的分类结论，即恰好为 (c)–(e) 中的图一致，这里补上“但不正定”。

**习题 6.1.5.** 设 $Q$ 是顶点集为 $D$ 的箭图。如果 $Q$ 只有有限个不可分解表示，就称 $Q$ 为**有限型**。记 $b_{ij}$ 为 $Q$ 中从 $i$ 到 $j$ 的边数，其中 $i,j\in D$。

P. Gabriel 在 20 世纪 70 年代初证明了下面这个引人注目的定理。

**定理.** 连通箭图 $Q$ 是有限型，当且仅当相应的无向图，即忘掉箭头方向后得到的图，是 Dynkin 图，见下面的定理 6.5.2。

本题将证明这个定理的“仅当”方向，也就是说明其他箭图为什么都不是有限型。

<span class="original-page-anchor" id="pdf-page-157" aria-hidden="true"></span>

(a) 假设 $Q$ 没有自环。证明：若 $Q$ 是有限型，则对任意不全为零的有理数 $x_i$，都有 $q(x_1,\ldots,x_N)>0$，其中

$$
q(x_1,\ldots,x_N):=\sum_{i\in D}x_i^2-\sum_{i,j\in D}b_{ij}x_ix_j.
$$

**译校注：** 根据作者的官方勘误，(a)、(b) 均须假设 $Q$ 没有自环；原式中的 $\frac12$ 应删去，(a) 中的条件 $x_i\ge0$ 也应删去。这里已按勘误修订。

提示：只需对整数 $x_i=n_i$ 验证。先假设 $n_i\ge0$，考虑满足 $\dim V_i=n_i$ 的 $Q$ 的表示 $V$ 所构成的空间 $W$。证明群 $\prod_i GL_{n_i}(k)$ 在 $W\oplus k$ 上的作用只有有限个轨道，然后用习题 6.1.2 得到所需不等式。再推出 $n_i$ 为任意整数时的结论。

(b) 仍假设 $Q$ 没有自环，推出 $q$ 是正定二次型。

提示：使用 $\mathbb Q$ 在 $\mathbb R$ 中稠密这一事实。

(c) 证明有限型箭图不可能有自环，然后用习题 6.1.3 推出定理。

**习题 6.1.6.** 设 $G\ne\{1\}$ 是 $SU(2)$ 的有限子群，$V$ 是由它到 $SU(2)$ 的嵌入得到的二维表示。设 $V_i$（$i\in I$）是 $G$ 的所有不可约表示，记 $r_{ij}$ 为 $V_i$ 在 $V\otimes V_j$ 中的重数。

(a) 证明 $r_{ij}=r_{ji}$。

(b) $G$ 的 **McKay 图** $M(G)$ 的顶点由 $i\in I$ 标记，顶点 $i$ 和 $j$ 之间有 $r_{ij}$ 条边。证明 $M(G)$ 连通。（使用习题 4.12.10。）

(c) 证明 $M(G)$ 是仿射 Dynkin 图，即习题 6.1.3 中“排除”的图之一。为此，证明矩阵 $a_{ij}=2\delta_{ij}-r_{ij}$ 半正定但不正定，再使用习题 6.1.3。

提示：令 $f=\sum x_i\chi_{V_i}$，其中 $\chi_{V_i}$ 是 $V_i$ 的特征标。直接证明 $((2-\chi_V)f,f)\ge0$。等号何时成立？接着，利用以下事实证明 $M(G)$ 没有自环：若 $G$ 不是循环群，则 $G$ 包含中心元素 $-\operatorname{Id}\in SU(2)$。

(d) 习题 4.12.8 中的各个群分别对应哪些图？

<span class="original-page-anchor" id="pdf-page-158" aria-hidden="true"></span>

(e) 用 McKay 图求出所有有限子群 $G\subset SU(2)$ 的不可约表示的维数。具体来说，证明这些维数就是我们所画的仿射 Dynkin 图中各顶点的数字标记。将结果与习题 4.12.8 中关于 $SO(3)$ 的子群所得的结果比较。

## 6.2. 箭图 $A_1,A_2,A_3$ 的不可分解表示

我们已经看到，研究箭图表示时，一个核心问题是：给定的连通箭图是否只有有限个不可分解表示。上一小节说明，只有底层无向图为 Dynkin 图的箭图才可能具有这个性质。为了判断它们是否确实具有这个性质，我们先对一些简单箭图的表示作出具体分解。

**注 6.2.1.** $1\longrightarrow0$ 这样的对象表示从一维向量空间到零空间的映射。同样，$0\longrightarrow1$ 表示从零空间到一维空间的映射，而 $1\longrightarrow1$ 表示两个一维空间之间的同构。这类图中的数字始终表示相应空间的维数；除非另有说明，各映射都是典范映射。

**例 6.2.2（$A_1$）。** 箭图 $A_1$ 只有一个顶点，没有边。它的表示就是一个向量空间，因此唯一的不可分解表示是基域，即一维空间。

**例 6.2.3（$A_2$）。** 箭图 $A_2$ 由两个顶点和连接它们的一条边组成：

$$
\bullet\longrightarrow\bullet
$$

它的一个表示由两个向量空间 $V,W$ 和一个算子 $A:V\to W$ 组成：

![A_2 的表示](/library/volume-88/diagrams/pdf-0158-a2.png)

<span class="original-page-anchor" id="pdf-page-159" aria-hidden="true"></span>

为了分解这个表示，先选取 $\ker A$ 在 $V$ 中的补空间 $V'$，以及 $\operatorname{Im}A$ 在 $W$ 中的补空间 $W'$。于是，表示可分解为

![A_2 表示的分解](/library/volume-88/diagrams/pdf-0159-a2-decomposition.png)

第一个直和项由若干个 $1\longrightarrow0$ 组成，第二个由若干个 $1\longrightarrow1$ 组成，第三个由若干个 $0\longrightarrow1$ 组成。因此，箭图 $A_2$ 有三个不可分解表示，分别是

$$
1\longrightarrow0,\qquad1\longrightarrow1,\qquad0\longrightarrow1.
$$

注意，这个结论就是矩阵的高斯消元定理。

**例 6.2.4（$A_3$）。** 箭图 $A_3$ 有三个顶点，以及连接它们的两条边。因此，需要在以下两种可能的定向中选择一种：

$$
\bullet\longrightarrow\bullet\longrightarrow\bullet,\qquad\bullet\longrightarrow\bullet\longleftarrow\bullet.
$$

(1) 先看下面这个定向：

$$
\bullet\longrightarrow\bullet\longrightarrow\bullet.
$$

这个箭图的表示形如

![A_3 的表示](/library/volume-88/diagrams/pdf-0159-a3.png)

像例 6.2.3 那样，先拆出

![拆出 A 的核](/library/volume-88/diagrams/pdf-0159-kernel.png)

这个对象由若干个 $1\longrightarrow0\longrightarrow0$ 组成。再选取 $\operatorname{Im}B$ 在 $Y$ 中的补空间 $Y'$，就还可以拆出

![拆出 B 的像的补空间](/library/volume-88/diagrams/pdf-0159-cokernel.png)

它由若干个 $0\longrightarrow0\longrightarrow1$ 组成。这样，剩下的表示中 $A$ 是单射，$B$ 是满射<span class="original-page-anchor" id="pdf-page-160" aria-hidden="true"></span>（为简化记号，我们将各个空间重新命名）：

![A 为单射、B 为满射](/library/volume-88/diagrams/pdf-0160-injective-surjective.png)

接着，令 $X=\ker(B\circ A)$，选取 $X$ 在 $V$ 中的补空间 $X'$，再选取 $A(X)$ 在 $W$ 中的补空间 $W'$，使 $A(X')\subset W'$。于是有

![第一次分解](/library/volume-88/diagrams/pdf-0160-first-decomposition.png)

第一个直和项由若干个 $1\xrightarrow{\sim}1\longrightarrow0$ 组成。看第二个直和项，此时 $A$ 是单射，$B$ 是满射，而且 $\ker(B\circ A)=0$。为简化记号，重新定义

$$
V=X',\qquad W=W'.
$$

然后，令 $X=\operatorname{Im}(B\circ A)$，选取 $X$ 在 $Y$ 中的补空间 $X'$，并令 $W'=B^{-1}(X')$。这样，$W'$ 就是 $A(V)$ 在 $W$ 中的补空间，从而得到分解

![第二次分解](/library/volume-88/diagrams/pdf-0160-second-decomposition.png)

这里，第一个直和项由若干个 $1\xrightarrow{\sim}1\xrightarrow{\sim}1$ 组成。第二个直和项再拆出 $B$ 的核后，就可分解为若干个 $0\longrightarrow1\xrightarrow{\sim}1$ 和 $0\longrightarrow1\longrightarrow0$。因此，这个箭图共有六个不可分解表示：

$$
\begin{gathered}
1\longrightarrow0\longrightarrow0,\quad0\longrightarrow0\longrightarrow1,\quad1\xrightarrow{\sim}1\longrightarrow0,\\
1\xrightarrow{\sim}1\xrightarrow{\sim}1,\quad0\longrightarrow1\xrightarrow{\sim}1,\quad0\longrightarrow1\longrightarrow0.
\end{gathered}
$$

(2) 现在看另一种定向：

$$
\bullet\longrightarrow\bullet\longleftarrow\bullet.
$$

<span class="original-page-anchor" id="pdf-page-161" aria-hidden="true"></span>

与上一种定向的处理类似，我们可以拆出如下类型的对象：

$$
1\longrightarrow0\longleftarrow0,\qquad0\longrightarrow0\longleftarrow1.
$$

这样，剩下的 $A$ 和 $B$ 都是单射：

![两个单射](/library/volume-88/diagrams/pdf-0161-injective-pair.png)

将 $V$ 和 $Y$ 视为 $W$ 的子空间后，问题就变成：在同构意义下，分类给定空间 $W$ 的子空间对，这称为**子空间对问题**。为此，先选取 $V\cap Y$ 在 $W$ 中的补空间 $W'$，并令 $V'=W'\cap V$、$Y'=W'\cap Y$。于是表示可以分解为

![拆出交空间](/library/volume-88/diagrams/pdf-0161-intersection-decomposition.png)

第二个直和项由若干个 $1\xrightarrow{\sim}1\xleftarrow{\sim}1$ 组成。继续分解第一个直和项。仍然为简化记号，令

$$
V=V',\qquad W=W',\qquad Y=Y'.
$$

现在可以假设 $V\cap Y=0$。再选取 $V\oplus Y$ 在 $W$ 中的补空间 $W'$，得到

![拆出和空间的补空间](/library/volume-88/diagrams/pdf-0161-sum-decomposition.png)

第二个直和项由若干个不可分解对象 $0\longrightarrow1\longleftarrow0$ 组成，第一个则可以继续分解为

![分解子空间的和](/library/volume-88/diagrams/pdf-0161-separate-decomposition.png)

这两个直和项分别由若干个以下对象组成：

$$
1\longrightarrow1\longleftarrow0,\qquad0\longrightarrow1\longleftarrow1.
$$

<span class="original-page-anchor" id="pdf-page-162" aria-hidden="true"></span>

因此，与上一种定向一样，我们得到 $A_3$ 的六个不可分解表示：

$$
\begin{gathered}
1\longrightarrow0\longleftarrow0,\quad0\longrightarrow0\longleftarrow1,\quad1\xrightarrow{\sim}1\xleftarrow{\sim}1,\\
0\longrightarrow1\longleftarrow0,\quad1\longrightarrow1\longleftarrow0,\quad0\longrightarrow1\longleftarrow1.
\end{gathered}
$$

## 6.3. 箭图 $D_4$ 的不可分解表示

最后考虑一个稍复杂的例子：箭图 $D_4$。

**例 6.3.1（$D_4$）。** 我们只讨论下面这个定向：

![D_4 的定向](/library/volume-88/diagrams/pdf-0162-d4.png)

这个箭图的表示形如

![D_4 的表示](/library/volume-88/diagrams/pdf-0162-representation.png)

首先仍可像前面一样，拆出映射 $A_1,A_2,A_3$ 的核。具体来说，拆出以下表示：

![A_1 的核](/library/volume-88/diagrams/pdf-0162-kernel1.png)

![A_2 的核](/library/volume-88/diagrams/pdf-0162-kernel2.png)

<span class="original-page-anchor" id="pdf-page-163" aria-hidden="true"></span>

![A_3 的核](/library/volume-88/diagrams/pdf-0163-kernel3.png)

这些表示分别由若干个以下不可分解对象组成：

![第一个外侧顶点的单表示](/library/volume-88/diagrams/pdf-0163-simple1.png)

![第二个外侧顶点的单表示](/library/volume-88/diagrams/pdf-0163-simple2.png)

![第三个外侧顶点的单表示](/library/volume-88/diagrams/pdf-0163-simple3.png)

拆出它们后，剩下的映射 $A_1,A_2,A_3$ 都是单射：

![三个单射](/library/volume-88/diagrams/pdf-0163-injective.png)

与例 6.2.4 一样，现在可以将空间 $V_1,V_2,V_3$ 看作 $V$ 的子空间。因此，我们得到**子空间三元组问题**，即分类给定空间 $V$ 的子空间三元组。

<span class="original-page-anchor" id="pdf-page-164" aria-hidden="true"></span>

下一步拆出若干个

![中心顶点的单表示](/library/volume-88/diagrams/pdf-0164-central-simple.png)

从而使剩下的表示满足

$$
V_1+V_2+V_3=V.
$$

令 $Y=V_1\cap V_2\cap V_3$，选取 $Y$ 在 $V$ 中的补空间 $V'$，并令 $V_i'=V'\cap V_i$，其中 $i=1,2,3$，就能将这个表示分解为

![拆出三个子空间的交](/library/volume-88/diagrams/pdf-0164-triple-intersection.png)

最后一个直和项由若干个以下不可分解表示组成：

![四个空间均为一维的表示](/library/volume-88/diagrams/pdf-0164-full-simple.png)

考虑第一个直和项，并将各空间重新命名以简化记号，现在得到

$$
V=V_1+V_2+V_3,\qquad V_1\cap V_2\cap V_3=0.
$$

接着，令 $Y=V_1\cap V_2$，选取 $Y$ 在 $V$ 中的补空间 $V'$，使 $V_3\subset V'$，并令 $V_1'=V'\cap V_1$、$V_2'=V'\cap V_2$。这样就<span class="original-page-anchor" id="pdf-page-165" aria-hidden="true"></span>得到分解

![拆出 V_1 与 V_2 的交](/library/volume-88/diagrams/pdf-0165-pair-intersection.png)

第二个直和项由若干个以下不可分解对象组成：

![V_1 与 V_2 的一维交空间](/library/volume-88/diagrams/pdf-0165-pair12.png)

这样，剩下的表示满足 $V_1\cap V_2=0$。类似地，再拆出若干个

![V_1 与 V_3 的交](/library/volume-88/diagrams/pdf-0165-pair13.png) 和 ![V_2 与 V_3 的交](/library/volume-88/diagrams/pdf-0165-pair23.png)

就能使空间 $V_1,V_2,V_3$ 两两相交于零：

$$
V_1\cap V_2=V_1\cap V_3=V_2\cap V_3=0.
$$

若 $V_1\nsubseteq V_2\oplus V_3$，令 $Y=V_1\cap(V_2\oplus V_3)$，并选取 $Y$ 在 $V_1$ 中的补空间 $V_1'$。这时 $V_1'\cap(V_2\oplus V_3)=0$，所以可以选取一个补空间<span class="original-page-anchor" id="pdf-page-166" aria-hidden="true"></span>$V'$，使它在 $V$ 中与 $V_1'$ 互补，并且包含 $V_2\oplus V_3$。这样得到分解

![拆出 V_1 中的补空间](/library/volume-88/diagrams/pdf-0166-sum-splitting.png)

第一个直和项由若干个

![只有 V_1 非零的外侧空间](/library/volume-88/diagrams/pdf-0166-arm1.png)

组成。拆出这些对象后，就有 $V_1\subseteq V_2\oplus V_3$。类似地，可以拆出以下类型的对象：

![只有 V_2 非零的外侧空间](/library/volume-88/diagrams/pdf-0166-arm2.png) 和 ![只有 V_3 非零的外侧空间](/library/volume-88/diagrams/pdf-0166-arm3.png)

使剩下的表示满足以下条件：

(1) $V_1+V_2+V_3=V$。

(2) $V_1\cap V_2=0$，$V_1\cap V_3=0$，$V_2\cap V_3=0$。

(3) $V_1\subseteq V_2\oplus V_3$，$V_2\subseteq V_1\oplus V_3$，$V_3\subseteq V_1\oplus V_2$。

于是

$$
V_1\oplus V_2=V_1\oplus V_3=V_2\oplus V_3=V.
$$

所以有

$$
\dim V_1=\dim V_2=\dim V_3=n
$$

<span class="original-page-anchor" id="pdf-page-167" aria-hidden="true"></span>

而且

$$
\dim V=2n.
$$

由于 $V_3\subseteq V_1\oplus V_2$，$V_3$ 中的每个元素都可写成

$$
x\in V_3,\qquad x=(x_1,x_2),\quad x_1\in V_1,\quad x_2\in V_2.
$$

于是可以定义投影

$$
B_1:V_3\to V_1,\quad(x_1,x_2)\mapsto x_1,
$$

$$
B_2:V_3\to V_2,\quad(x_1,x_2)\mapsto x_2.
$$

因为 $V_3\cap V_1=0$ 且 $V_3\cap V_2=0$，这两个映射都是单射，因此也是同构。再定义同构

$$
A=B_2\circ B_1^{-1}:V_1\to V_2.
$$

设 $e_1,\ldots,e_n$ 是 $V_1$ 的一组基，那么

$$
\begin{aligned}
V_1&= k e_1\oplus k e_2\oplus\cdots\oplus k e_n,\\
V_2&= k Ae_1\oplus k Ae_2\oplus\cdots\oplus k Ae_n,\\
V_3&= k (e_1+Ae_1)\oplus k (e_2+Ae_2)\oplus\cdots\oplus k (e_n+Ae_n).
\end{aligned}
$$

因此，可以将 $V_3$ 看作同构 $A:V_1\to V_2$ 的图像。由此得到分解

![分解为同构图像对应的表示](/library/volume-88/diagrams/pdf-0167-graph-decomposition.png)

这些直和项对应以下不可分解对象：

![中心空间为二维的不可分解表示](/library/volume-88/diagrams/pdf-0167-two-dimensional.png)

因此，采用上述定向的箭图 $D_4$ 有 12 个不可分解对象。对其他可能的定向作出具体分解，同样也会得到 12 个不可分解对象。

**译校注：** 根据作者的官方勘误，本小节末尾的复数域 $\mathbb C$ 应改为任意特征为零的代数闭域 $k$。上面的原生公式已作相应修订；保留的原书图像中，$\mathbb C$ 及 $\mathbb C^2$ 分别按 $k$ 及 $k^2$ 理解。

<span class="original-page-anchor" id="pdf-page-168" aria-hidden="true"></span>

看来，不可分解表示的数目与边的定向无关。Gabriel 定理确实会将这一观察推广到一般情形。

## 6.4. 根

从现在起，固定一个 $A_n,D_n,E_6,E_7,E_8$ 型的图 $\Gamma$，并将它的邻接矩阵记为 $R_\Gamma$。

**定义 6.4.1（Cartan 矩阵）。** 定义 $\Gamma$ 的 **Cartan 矩阵**为

$$
A_\Gamma=2\operatorname{Id}-R_\Gamma.
$$

然后在格 $\mathbb Z^n$ 或空间 $\mathbb R^n$ 上，定义图 $\Gamma$ 对应的内积

$$
B(x,y)=x^TA_\Gamma y.
$$

**引理 6.4.2.** (1) $B$ 正定。

(2) 对 $x\in\mathbb Z^n$，$B(x,x)$ 的值总是偶数。

**证明.** (1) 因为 $\Gamma$ 是 Dynkin 图，结论直接来自定义。

(2) 根据 Cartan 矩阵的定义，

$$
\begin{aligned}
B(x,x)=x^TA_\Gamma x
&=\sum_{i,j}x_i a_{ij}x_j
=2\sum_i x_i^2+\sum_{i,j,\ i\ne j}x_i a_{ij}x_j\\
&=2\sum_i x_i^2+2\cdot\sum_{i<j}a_{ij}x_ix_j,
\end{aligned}
$$

所以它是偶数。$\square$

**定义 6.4.3.** 对一个给定的正定内积，$\mathbb Z^n$ 中按此内积衡量长度最短的非零向量称为**根**。

因此，对内积 $B$ 而言，根就是满足

$$
B(x,x)=2
$$

的非零向量 $x\in\mathbb Z^n$。

**注 6.4.4.** 根只有有限个，因为所有根都必须落在某个球内。

<span class="original-page-anchor" id="pdf-page-169" aria-hidden="true"></span>

**定义 6.4.5。** 形如

$$
\alpha_i=(0,\ldots,\overbrace{1}^{\text{第 }i\text{ 个}},\ldots,0)
$$

的向量称为**单根**。

这些 $\alpha_i$ 自然构成格 $\mathbb Z^n$ 的一组基。

**引理 6.4.6。** 设 $\alpha$ 是一个根，且 $\alpha=\sum_{i=1}^n k_i\alpha_i$。那么，要么所有 $i$ 都满足 $k_i\geq 0$，要么所有 $i$ 都满足 $k_i\leq 0$。

**证明。** 反设不然，即有 $k_i>0$、$k_j<0$。不妨再假设，$i$ 与 $j$ 之间的所有 $s$ 都满足 $k_s=0$。我们把指标 $i,j$ 看成图 $\Gamma$ 的顶点：

![从 i 通向 j 的路径上，i 与 i′ 之间的边。](/library/volume-88/diagrams/pdf-0169-root-graph.png)

设 $\epsilon$ 是从 $i$ 向 $j$ 走时连接 $i$ 与下一顶点的边，$i'$ 是 $\epsilon$ 另一端的顶点。删去 $\epsilon$ 后，图 $\Gamma$ 分成两个图 $\Gamma_1,\Gamma_2$。由于 $\Gamma$ 是 Dynkin 图，没有圈或自环，所以 $\Gamma_1$ 和 $\Gamma_2$ 各自连通，彼此却不相连：

![删去该边后得到的两个连通分支 Γ₁ 和 Γ₂。](/library/volume-88/diagrams/pdf-0169-split-graph.png)

于是 $i\in\Gamma_1$、$j\in\Gamma_2$。定义

$$
\beta=\sum_{m\in\Gamma_1}k_m\alpha_m,\qquad
\gamma=\sum_{m\in\Gamma_2}k_m\alpha_m.
$$

这样就有

$$
\alpha=\beta+\gamma.
$$

由 $k_i>0$、$k_j<0$ 可知 $\beta\neq 0$、$\gamma\neq 0$，因而

$$
B(\beta,\beta)\geq 2,\qquad B(\gamma,\gamma)\geq 2.
$$

<span class="original-page-anchor" id="pdf-page-170" aria-hidden="true"></span>

此外，由于 $\Gamma_1,\Gamma_2$ 之间只有 $\epsilon$ 这一条连接边，

$$
B(\beta,\gamma)=-k_i k_{i'}.
$$

又因为 $k_i>0$ 而 $k_{i'}\leq 0$，这个数必定非负。因此

$$
B(\alpha,\alpha)=B(\beta+\gamma,\beta+\gamma)
=\underbrace{B(\beta,\beta)}_{\geq 2}
+2\underbrace{B(\beta,\gamma)}_{\geq 0}
+\underbrace{B(\gamma,\gamma)}_{\geq 2}\geq 4.
$$

这与 $\alpha$ 是根的假设矛盾。$\square$

**定义 6.4.7。** 若根 $\alpha=\sum_i k_i\alpha_i$ 的所有系数都满足 $k_i\geq 0$，就称其为**正根**。若所有 $i$ 都满足 $k_i\leq 0$，就称其为**负根**。

**注 6.4.8。** 引理 6.4.6 表明，每个根不是正根就是负根。

**例 6.4.9。** (1) 设 $\Gamma$ 为 $A_{N-1}$ 型。我们可以把格 $L=\mathbb Z^{N-1}$ 实现为格 $\mathbb Z^N$ 的一个子群：令 $L\subseteq\mathbb Z^N$ 由所有满足

$$
\sum_i x_i=0
$$

的向量 $(x_1,\ldots,x_N)$ 构成。

向量

$$
\begin{aligned}
\alpha_1&=(1,-1,0,\ldots,0),\\
\alpha_2&=(0,1,-1,0,\ldots,0),\\
&\phantom{=}\vdots\\
\alpha_{N-1}&=(0,\ldots,0,1,-1)
\end{aligned}
$$

自然构成 $L$ 的一组基。另外，$\mathbb Z^N$ 上的标准内积

$$
(x,y)=\sum_i x_i y_i
$$

限制到 $L$ 上，就是由 $\Gamma$ 给出的内积 $B$，因为二者在基向量上的取值相同：

$$
\begin{aligned}
(\alpha_i,\alpha_i)&=2,\\
(\alpha_i,\alpha_j)&=\begin{cases}
-1,&i,j\text{ 相邻},\\
0,&\text{否则}.
\end{cases}
\end{aligned}
$$

这说明，形如

$$
(0,\ldots,0,1,0,\ldots,0,-1,0,\ldots,0)
=\alpha_i+\alpha_{i+1}+\cdots+\alpha_{j-1}
$$

<span class="original-page-anchor" id="pdf-page-171" aria-hidden="true"></span>

以及

$$
(0,\ldots,0,-1,0,\ldots,0,1,0,\ldots,0)
=-(\alpha_i+\alpha_{i+1}+\cdots+\alpha_{j-1})
$$

的向量就是 $L$ 的根。因此，$L$ 中正根的个数为

$$
\frac{N(N-1)}{2}.
$$

(2) 我们也列出其他 Dynkin 图中正根的个数：

$$
\begin{aligned}
D_N:&\quad N(N-1)\text{ 个根},\\
E_6:&\quad 36\text{ 个根},\\
E_7:&\quad 63\text{ 个根},\\
E_8:&\quad 120\text{ 个根}.
\end{aligned}
$$

**定义 6.4.10。** 设 $\alpha\in\mathbb Z^n$ 是正根。用公式

$$
s_\alpha(v)=v-B(v,\alpha)\alpha
$$

定义反射 $s_\alpha$。

把 $s_{\alpha_i}$ 记作 $s_i$，称这些反射为**简单反射**。

**注 6.4.11。** 作为 $\mathbb R^n$ 上的线性算子，$s_\alpha$ 固定所有与 $\alpha$ 正交的向量，并且

$$
s_\alpha(\alpha)=-\alpha.
$$

所以 $s_\alpha$ 就是关于与 $\alpha$ 正交的超平面的反射，尤其保持 $B$ 不变。这些简单反射 $s_i:=s_{\alpha_i}$ 生成的子群 $W\subseteq O(\mathbb R^n)$ 称为 $\Gamma$ 的 **Weyl 群**。对每个 $w\in W$，$w(\alpha_i)$ 都是根；根只有有限多个，因此 $W$ 必为有限群。

**译校注：** 原书此处只写 $s_i$，译文依据作者 2024 年勘误明确写成 $s_i:=s_{\alpha_i}$。

## 6.5. Gabriel 定理

**定义 6.5.1。** 设 $Q$ 是一个箭图，将其顶点任意编号为 $1,\ldots,n$。设 $V=(V_1,\ldots,V_n)$ 是 $Q$ 的表示。称

$$
d(V)=(\dim V_1,\ldots,\dim V_n)
$$

为这个表示的**维数向量**。

现在可以用根来表述 Gabriel 定理了。

<span class="original-page-anchor" id="pdf-page-172" aria-hidden="true"></span>

**定理 6.5.2（Gabriel 定理）。** 设 $Q$ 是 $A_n$、$D_n$、$E_6$、$E_7$ 或 $E_8$ 型箭图。那么 $Q$ 的不可分解表示只有有限多个。具体地说，每个不可分解表示的维数向量都是一个正根（相对于 $B_\Gamma$），而对每个正根 $\alpha$，恰有一个维数向量为 $\alpha$ 的不可分解表示。

## 6.6. 反射函子

**定义 6.6.1。** 设 $Q$ 是任意箭图。如果与顶点 $i\in Q$ 相连的所有边都指向 $i$，就称 $i$ 为**汇点**：

![所有箭头都指向汇点 i。](/library/volume-88/diagrams/pdf-0172-sink.png)

如果与顶点 $i\in Q$ 相连的所有边都从 $i$ 指向外部，就称 $i$ 为**源点**：

![所有箭头都从源点 i 指向外部。](/library/volume-88/diagrams/pdf-0172-source.png)

**定义 6.6.2。** 设 $Q$ 是任意箭图，$i\in Q$ 是汇点（或源点）。把所有指向 $i$（或从 $i$ 出发）的箭头反向，所得的箭图记作 $\overline Q_i$。

现在可以定义**反射函子**（也称 **Coxeter 函子**）。

**定义 6.6.3。** 设 $Q$ 是箭图，$i\in Q$ 是汇点，$V$ 是 $Q$ 的表示。定义反射函子

$$
F_i^+:\operatorname{Rep}Q\longrightarrow\operatorname{Rep}\overline Q_i
$$

如下：

$$
\begin{aligned}
F_i^+(V)_k&=V_k\quad\text{若 }k\neq i,\\
F_i^+(V)_i&=\ker\left(\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i\right).
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-173" aria-hidden="true"></span>

所有映射都保持不变，只有现在从 $i$ 出发的那些映射需要替换：先将 $\ker\varphi$ 包含到 $\bigoplus_{j\to i}V_j$ 中，再复合到相应分量 $V_j$ 的投影。

**译校注：** 原文把这里的投影写成 $\bigoplus_j V_{j\to i}\to V_i$，直和下标和投影的目标空间都有误。按照反射后箭头从 $i$ 指向 $j$ 的定义，投影应为 $\bigoplus_{\ell\to i}V_\ell\to V_j$。

**定义 6.6.4。** 设 $Q$ 是箭图，$i\in Q$ 是源点，$V$ 是 $Q$ 的表示。设 $\psi$ 为典范映射

$$
\psi:V_i\longrightarrow\bigoplus_{i\to j}V_j.
$$

定义反射函子

$$
F_i^-:\operatorname{Rep}Q\longrightarrow\operatorname{Rep}\overline Q_i
$$

如下：

$$
\begin{aligned}
F_i^-(V)_k&=V_k\quad\text{若 }k\neq i,\\
F_i^-(V)_i&=\operatorname{Coker}(\psi)=\left(\bigoplus_{i\to j}V_j\right)/\operatorname{Im}\psi.
\end{aligned}
$$

同样，所有映射都保持不变，只有现在指向 $i$ 的那些映射需要替换：先作包含映射 $V_k\to\bigoplus_{i\to j}V_j$，再与自然映射 $\bigoplus_{i\to j}V_j\to\bigoplus_{i\to j}V_j/\operatorname{Im}\psi$ 复合。

**命题 6.6.5。** 设 $Q$ 是箭图，$V$ 是 $Q$ 的不可分解表示。

(1) 设 $i\in Q$ 是汇点。那么，要么 $\dim V_i=1$ 且所有 $j\neq i$ 都满足 $\dim V_j=0$，要么映射

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

是满射。

(2) 设 $i\in Q$ 是源点。那么，要么 $\dim V_i=1$ 且所有 $j\neq i$ 都满足 $\dim V_j=0$，要么映射

$$
\psi:V_i\longrightarrow\bigoplus_{i\to j}V_j
$$

是单射。

**证明。** (1) 取 $\operatorname{Im}\varphi$ 的一个补空间 $W$。于是得到

![V 分解为一个只在该顶点取空间 W 的表示与 V′ 的直和。](/library/volume-88/diagrams/pdf-0173-decomposition.png)

<span class="original-page-anchor" id="pdf-page-174" aria-hidden="true"></span>

由于 $V$ 不可分解，这两个直和项中必有一个为零。若第一项为零，则 $\varphi$ 必为满射。若第二项为零，则第一项必具有所需的形式，否则它还可以写成若干个如下对象的直和：

![汇点处为一维空间、其余各顶点处为零的表示。](/library/volume-88/diagrams/pdf-0174-simple-representation.png)

这与 $V$ 不可分解的假设矛盾。

(2) 同样，将 $\psi$ 的核分拆出来即可得到结论。$\square$

**命题 6.6.6。** 设 $Q$ 是箭图，$V$ 是 $Q$ 的表示。

(1) 若映射

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

是满射，则

$$
F_i^-F_i^+V=V.
$$

(2) 若映射

$$
\psi:V_i\longrightarrow\bigoplus_{i\to j}V_j
$$

是单射，则

$$
F_i^+F_i^-V=V.
$$

**证明。** 在下面的证明中，$i\to j$ 始终表示原箭图 $Q$ 中从 $i$ 指向 $j$ 的箭头。我们只证明第一个结论，而且只验证 $V$ 与 $F_i^-F_i^+V$ 的空间相同。只需对第 $i$ 个空间验证即可。设

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

是满射，并令

$$
K=\ker\varphi.
$$

<span class="original-page-anchor" id="pdf-page-175" aria-hidden="true"></span>

应用 $F_i^+$ 时，空间 $V_i$ 被替换为 $K$。再设

$$
\psi:K\longrightarrow\bigoplus_{j\to i}V_j.
$$

应用 $F_i^-$ 后，$K$ 被替换为

$$
K'=\left(\bigoplus_{j\to i}V_j\right)/(\operatorname{Im}\psi).
$$

然而

$$
\operatorname{Im}\psi=K,
$$

因此由同态定理，

$$
K'=\left(\bigoplus_{j\to i}V_j\right)
/\left(\ker\left(\varphi:\bigoplus_{j\to i}V_j\to V_i\right)\right)
=\operatorname{Im}\left(\varphi:\bigoplus_{j\to i}V_j\to V_i\right).
$$

由于假设 $\varphi$ 是满射，我们得到

$$
K'=V_i.
$$

$\square$

**命题 6.6.7。** 设 $Q$ 是箭图，$V$ 是 $Q$ 的不可分解表示。那么 $F_i^+V$ 和 $F_i^-V$（只要有定义）或者不可分解，或者为 $0$。

**证明。** 我们证明 $F_i^+V$ 的情形；$F_i^-V$ 的情形同理。由命题 6.6.5，要么映射

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

是满射，要么 $\dim V_i=1$，且 $j\neq i$ 时 $\dim V_j=0$。在后一种情形下，

$$
F_i^+V=0.
$$

所以不妨假设 $\varphi$ 是满射。此时，假设 $F_i^+V$ 可以分解为

$$
F_i^+V=X\oplus Y
$$

<span class="original-page-anchor" id="pdf-page-176" aria-hidden="true"></span>

其中 $X,Y\neq 0$。不过，$F_i^+V$ 在 $i$ 处是单射的，因为其各个映射都是典范投影，这些投影的直和就是自然的嵌入。因此 $X$ 和 $Y$ 在 $i$ 处也必须是单射的，从而由命题 6.6.6，

$$
F_i^+F_i^-X=X,\qquad F_i^+F_i^-Y=Y.
$$

特别地，

$$
F_i^-X\neq 0,\qquad F_i^-Y\neq 0.
$$

于是

$$
V=F_i^-F_i^+V=F_i^-X\oplus F_i^-Y,
$$

这与 $V$ 不可分解的假设矛盾。因此

$$
F_i^+V
$$

不可分解。$\square$

**命题 6.6.8。** 设 $Q$ 是箭图，$V$ 是 $Q$ 的表示。

(1) 设 $i\in Q$ 是汇点，且 $V$ 在 $i$ 处是满射的。那么

$$
d(F_i^+V)=s_i(d(V)).
$$

(2) 设 $i\in Q$ 是源点，且 $V$ 在 $i$ 处是单射的。那么

$$
d(F_i^-V)=s_i(d(V)).
$$

**证明。** 我们只证明第一个结论；第二个结论同理。设 $i\in Q$ 是汇点，且

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

是满射。令 $K=\ker\varphi$，则

$$
\dim K=\sum_{j\to i}\dim V_j-\dim V_i.
$$

因而

$$
(d(F_i^+V)-d(V))_i=\sum_{j\to i}\dim V_j-2\dim V_i=-B(d(V),\alpha_i)
$$

且

$$
(d(F_i^+V)-d(V))_j=0,\qquad j\neq i.
$$

<span class="original-page-anchor" id="pdf-page-177" aria-hidden="true"></span>

由此可得

$$
\begin{aligned}
d(F_i^+V)-d(V)&=-B(d(V),\alpha_i)\alpha_i\\
\Longleftrightarrow\quad d(F_i^+V)&=d(V)-B(d(V),\alpha_i)\alpha_i=s_i(d(V)).
\end{aligned}
$$

$\square$

## 6.7. Coxeter 元素

**定义 6.7.1。** 设 $Q$ 是箭图，$\Gamma$ 是其底图。把 $\Gamma$ 的顶点任意编号为 $1,\ldots,n$。与这一编号对应的 $Q$ 的 **Coxeter 元素** $c$ 定义为

$$
c=s_1s_2\cdots s_n.
$$

**引理 6.7.2。** 设

$$
\beta=\sum_i k_i\alpha_i,
$$

其中所有 $i$ 都满足 $k_i\geq 0$，而且这些 $k_i$ 不全为零。那么，存在 $N\in\mathbb N$，使得

$$
c^N\beta
$$

至少有一个系数严格小于零。

**证明。** Coxeter 元素 $c$ 属于有限群 $W$，所以存在 $M\in\mathbb N$，使得

$$
c^M=1.
$$

我们断言，作为 $\mathbb R^n$ 上的算子，

$$
1+c+c^2+\cdots+c^{M-1}=0.
$$

这就给出所需结论：$\beta$ 至少有一个系数严格大于零，因此

$$
c\beta,c^2\beta,\ldots,c^{M-1}\beta
$$

中至少有一个元素具有严格小于零的系数。此外，只需证明 $1$ 不是 $c$ 的特征值即可，因为

$$
\begin{aligned}
(1+c+c^2+\cdots+c^{M-1})v&=w\neq 0\\
\Longrightarrow\quad cw&=c(1+c+c^2+\cdots+c^{M-1})v\\
&=(c+c^2+c^3+\cdots+c^{M-1}+1)v=w.
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-178" aria-hidden="true"></span>

反设 $1$ 是 $c$ 的特征值，取相应的特征向量 $v$，则

$$
\begin{aligned}
cv=v&\Longrightarrow s_1\cdots s_n v=v\\
&\Longleftrightarrow s_2\cdots s_n v=s_1v.
\end{aligned}
$$

由于 $s_i$ 只改变 $v$ 的第 $i$ 个坐标，我们得到

$$
s_1v=v\quad\text{且}\quad s_2\cdots s_n v=v.
$$

重复这一过程，就得到对所有 $i$ 都有

$$
s_i v=v.
$$

这意味着对所有 $i$ 都有

$$
B(v,\alpha_i)=0.
$$

由于 $B$ 非退化，便有 $v=0$，这与 $v$ 是特征向量矛盾。$\square$

## 6.8. Gabriel 定理的证明

设 $V$ 是 $Q$ 的不可分解表示。我们把 $Q$ 的顶点固定编号为 $1,\ldots,n$，使得只要能从 $i$ 到达 $j$，就有 $i<j$。这样的编号是可以做到的：先把最大的编号赋给任意一个汇点，再从箭图中删去这个汇点；随后把次大的编号赋给剩余箭图中的一个汇点，依此类推。这样就能得到所需的编号。

现在考虑序列

$$
V^{(0)}=V,\quad V^{(1)}=F_n^+V,\quad V^{(2)}=F_{n-1}^+F_n^+V,\ldots.
$$

由于我们选择了上述编号，这个序列有良好定义：$n$ 必为 $Q$ 的汇点，$n-1$ 必为 $\overline Q_n$ 的汇点，依此类推；这里 $\overline Q_r$ 表示把 $Q$ 中顶点 $r$ 处的所有箭头反向所得的箭图。

**译校注：** 原书括号中的一般定义把 $\overline Q_r$ 误写成 $\overline Q_n$，译文依据作者 2024 年勘误改正。

此外，$V^{(n)}$ 又是 $Q$ 的表示，因为我们对每个顶点都应用了一次反射函子，每条箭头因此恰好反向了两次。于是还可以定义

$$
V^{(n+1)}=F_n^+V^{(n)},\ldots,
$$

将这个序列无限继续下去。

<span class="original-page-anchor" id="pdf-page-179" aria-hidden="true"></span>

**定理 6.8.1。** 存在 $m\in\mathbb N$，使得对某个 $p$，

$$
d\left(V^{(m)}\right)=\alpha_p.
$$

**证明。** 若 $V^{(i)}$ 在相应顶点 $k$ 处是满射的，则

$$
d\left(V^{(i+1)}\right)=d\left(F_k^+V^{(i)}\right)=s_k d\left(V^{(i)}\right).
$$

因此，若 $V^{(0)},\ldots,V^{(i-1)}$ 在各自的相应顶点处都是满射的，就有

$$
d\left(V^{(i)}\right)=\cdots s_{n-1}s_n d(V).
$$

由引理 6.7.2，这个过程不可能无限继续，因为 $d\left(V^{(i)}\right)$ 不能有负的分量。取最小的 $i$，使得 $V^{(i)}$ 在相应顶点处不是满射。由命题 6.6.7，它是不可分解的。再由命题 6.6.5，得到对某个 $p$，

$$
d\left(V^{(i)}\right)=\alpha_p.
$$

$\square$

现在可以证明 Gabriel 定理了。具体地，我们得到以下推论。

**推论 6.8.2。** 设 $Q$ 是箭图，$V$ 是任意不可分解表示。那么 $d(V)$ 是一个正根。

**证明。** 由定理 6.8.1 的证明，

$$
s_{i_1}\cdots s_{i_m}(d(V))=\alpha_p.
$$

**译校注：** 原书此处只写“由定理 6.8.1”，译文依据作者 2024 年勘误改为“由定理 6.8.1 的证明”。

由于 $s_i$ 保持 $B$ 不变，得到

$$
B(d(V),d(V))=B(\alpha_p,\alpha_p)=2.
$$

$\square$

**推论 6.8.3。** 设 $V,V'$ 是 $Q$ 的不可分解表示，且 $d(V)=d(V')$。那么 $V$ 与 $V'$ 同构。

<span class="original-page-anchor" id="pdf-page-180" aria-hidden="true"></span>

**证明。** 取满足

$$
d\left(V^{(i)}\right)=\alpha_p
$$

的最小整数 $i$。

**译校注：** 原书只说“取满足条件的 $i$”，译文依据作者 2024 年勘误补明应取最小的整数 $i$。

此时也有 $d\left(V'^{(i)}\right)=\alpha_p$，所以

$$
V'^{(i)}=V^{(i)}=:V^i.
$$

此外，

$$
\begin{aligned}
V^{(i)}&=F_k^+\cdots F_{n-1}^+F_n^+V^{(0)},\\
V'^{(i)}&=F_k^+\cdots F_{n-1}^+F_n^+V'^{(0)}.
\end{aligned}
$$

而 $V^{(i-1)},\ldots,V^{(0)}$ 与 $V'^{(i-1)},\ldots,V'^{(0)}$ 在各自的相应顶点处都必为满射。因此

$$
\begin{aligned}
&F_n^-F_{n-1}^-\cdots F_k^-V^i\\
&\quad=\begin{cases}
F_n^-F_{n-1}^-\cdots F_k^-F_k^+\cdots F_{n-1}^+F_n^+V^{(0)}=V^{(0)}=V,\\
F_n^-F_{n-1}^-\cdots F_k^-F_k^+\cdots F_{n-1}^+F_n^+V'^{(0)}=V'^{(0)}=V'.
\end{cases}
\end{aligned}
$$

$\square$

这两个推论表明，不可分解表示只有有限多个（因为根只有有限多个），而且每个不可分解表示的维数向量都是正根。Gabriel 定理的最后一个结论由下面的推论得到。

**推论 6.8.4。** 对每个正根 $\alpha$，都存在一个不可分解表示 $V$，使得

$$
d(V)=\alpha.
$$

**证明。** 考虑序列

$$
s_n\alpha,\ s_{n-1}s_n\alpha,\ldots.
$$

取这个序列中第一个为负根的元素（由引理 6.7.2，这样的元素必定出现），再看它的前一步，将那一步的元素记作 $\beta$。于是 $\beta$ 是正根，而对某个 $i$，$s_i\beta$ 是负根。由于 $s_i$ 只改变一个坐标，得到

$$
\beta=\alpha_i
$$

以及

$$
(s_q\cdots s_{n-1}s_n)\alpha=\alpha_i.
$$

<span class="original-page-anchor" id="pdf-page-181" aria-hidden="true"></span>

令 $\mathbb C_{(i)}$ 为维数向量等于 $\alpha_i$ 的表示，并定义

$$
V=F_n^-F_{n-1}^-\cdots F_q^-\mathbb C_{(i)}.
$$

这个表示不可分解，并且

$$
d(V)=\alpha.
$$

$\square$

**例 6.8.5。** 下面用一个例子说明反射函子怎样起作用。考虑箭图 $D_4$，将所有箭头都定向为指向中央顶点（编号为 $4$）。从集中在第四个顶点的一维表示 $V_{\alpha_4}$ 出发，对它应用函子 $F_3^-F_2^-F_1^-$，得到

$$
F_1^-F_2^-F_3^-V_{\alpha_4}=V_{\alpha_1+\alpha_2+\alpha_3+\alpha_4}.
$$

再应用 $F_4^-$，得到

$$
F_4^-F_1^-F_2^-F_3^-V_{\alpha_4}=V_{\alpha_1+\alpha_2+\alpha_3+2\alpha_4}.
$$

这恰好是三条直线包含到一个平面中的表示，也是 $D_4$ 箭图最复杂的不可分解表示。

## 6.9. 习题

**习题 6.9.1。** 设 $Q_n$ 是长度为 $n$ 的循环箭图，也就是 $n$ 个顶点由 $n$ 条有向边连接成一个圈。显然，$Q_1$ 的不可分解表示由若尔当标准形定理分类。对 $Q_2$ 的不可分解表示，给出类似的分类。换言之，在同构意义下，分类线性算子对 $A:V\to W$ 与 $B:W\to V$。具体如下：

(a) 考虑下列各对（$n\geq 1$）：

(1) $E_{n,\lambda}$：$V=W=\mathbb C^n$，$A$ 为大小为 $n$、特征值为 $\lambda$ 的若尔当块，$B=1$（$\lambda\in\mathbb C$）。

(2) $E_{n,\infty}$：由 $E_{n,0}$ 交换 $V$ 与 $W$、$A$ 与 $B$ 得到。

(3) $H_n$：$V=\mathbb C^n$，基为 $v_i$；$W=\mathbb C^{n-1}$，基为 $w_i$。当 $i<n$ 时，$Av_i=w_i$、$Bw_i=v_{i+1}$，并且 $Av_n=0$。

<span class="original-page-anchor" id="pdf-page-182" aria-hidden="true"></span>

(4) $K_n$ 由 $H_n$ 交换 $V$ 与 $W$、$A$ 与 $B$ 得到。

证明这些表示都不可分解，而且两两不同构。

(b) 证明，若 $E$ 是 $Q_2$ 的表示，且 $AB$ 不是幂零的，则 $E=E'\oplus E''$，其中 $E''=E_{n,\lambda}$，$\lambda\neq 0$。

(c) 考虑 $AB$ 幂零的情形，以及 $V\oplus W$ 上由 $X(v,w)=(Bw,Av)$ 给出的算子 $X$。证明 $X$ 幂零，并且有一组由链构成的基（链即序列 $u,Xu,X^2u,\ldots,X^{l-1}u$，其中 $X^lu=0$），这些链与直和分解相容（即每条链的 $u$ 都属于 $V$ 或属于 $W$）。由此推出，(1)–(4) 给出了 $Q_2$ 的全部不可分解表示。

(d)（较难！）将这个分类推广到 Kronecker 箭图：它有两个顶点 $1$ 和 $2$，以及两条都从 $1$ 指向 $2$ 的边。

(e)（更难！）能否把这个分类推广到任意定向的 $Q_n$，$n>2$？（较容易的版本：只考虑循环定向。）

**习题 6.9.2。** 设 $L\subset\frac12\mathbb Z^8$ 是由下列向量构成的格：其坐标要么全是整数，要么全是非整数的半整数，而且所有坐标之和是偶整数。

(a) 令 $\alpha_i=e_i-e_{i+1}$，$i=1,\ldots,6$，$\alpha_7=e_6+e_7$，$\alpha_8=-\frac12\sum_{i=1}^8 e_i$。证明这些 $\alpha_i$ 构成 $L$ 在 $\mathbb Z$ 上的一组基。

(b) 证明 $L$ 中的根（相对于通常的内积）构成 $E_8$ 型根系（计算各 $\alpha_i$ 的内积）。

(c) 证明 $E_7$ 与 $E_6$ 的格分别可以实现为 $E_8$ 格 $L$ 中前两个、前三个坐标相等的向量所成的集合（坐标相对于基 $e_i$）。

(d) 证明 $E_6,E_7,E_8$ 分别有 $72$、$126$、$240$ 个根（按它们在基 $e_i$ 下的表达式列举根的类型，并计算每种类型的根的个数）。

**习题 6.9.3。** 设 $V_\alpha$ 是 Dynkin 箭图 $Q$ 中与正根 $\alpha$ 对应的不可分解表示。例如，若 $\alpha_i$ 是单根，则 $V_{\alpha_i}$ 在顶点 $i$ 处为一维空间，在其他顶点处都为 $0$。

<span class="original-page-anchor" id="pdf-page-183" aria-hidden="true"></span>

(a) 证明，若 $i$ 是源点，则对 $Q$ 的任意表示 $V$，都有 $\operatorname{Ext}^1(V,V_{\alpha_i})=0$；若 $i$ 是汇点，则 $\operatorname{Ext}^1(V_{\alpha_i},V)=0$。

(b) 给定箭图的一个定向，求 $V_\alpha$ 在此定向下的一个若尔当–赫尔德列。

[^sylvester-155]: Sylvester 判别法是说，$\mathbb R^N$ 上的对称双线性型 $(\ ,\ )$ 正定，当且仅当对任意 $k\le N$，都有 $\det_{1\le i,j\le k}(e_i,e_j)>0$。

[^labels-155]: 先忽略各顶点的数字标记；它们将在下面的习题 6.1.6 中用到。
