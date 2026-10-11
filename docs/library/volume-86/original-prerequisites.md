---
title: "Logical Prerequisites"
description: "Serge Lang《Algebra》English。"
pageClass: algebra-reading
prev: {"text":"Foreword","link":"/library/volume-86/original-preface"}
next: {"text":"Contents","link":"/library/volume-86/original-contents"}
---

# Logical Prerequisites

<span class="original-page-anchor" id="pdf-page-10" aria-hidden="true"></span>

We assume that the reader is familiar with sets, and with the symbols $\cap$, $\cup$, $\supset$, $\subset$, $\in$. If $A$, $B$ are sets, we use the symbol $A\subset B$ to mean that $A$ is contained in $B$ but may be equal to $B$. Similarly for $A\supset B$.

If $f:A\to B$ is a mapping of one set into another, we write

$$
x\mapsto f(x)
$$

to denote the effect of $f$ on an element $x$ of $A$. We distinguish between the arrows $\to$ and $\mapsto$. We denote by $f(A)$ the set of all elements $f(x)$, with $x\in A$.

Let $f:A\to B$ be a mapping (also called a map). We say that $f$ is **injective** if $x\ne y$ implies $f(x)\ne f(y)$. We say $f$ is **surjective** if given $b\in B$ there exists $a\in A$ such that $f(a)=b$. We say that $f$ is **bijective** if it is both surjective and injective.

A subset $A$ of a set $B$ is said to be **proper** if $A\ne B$.

Let $f:A\to B$ be a map, and $A'$ a subset of $A$. The restriction of $f$ to $A'$ is a map of $A'$ into $B$ denoted by $f|A'$.

If $f:A\to B$ and $g:B\to C$ are maps, then we have a composite map $g\circ f$ such that $(g\circ f)(x)=g(f(x))$ for all $x\in A$.

Let $f:A\to B$ be a map, and $B'$ a subset of $B$. By $f^{-1}(B')$ we mean the subset of $A$ consisting of all $x\in A$ such that $f(x)\in B'$. We call it the **inverse image** of $B'$. We call $f(A)$ the **image** of $f$.

A **diagram**

$$
\begin{array}{ccc}
A & \xrightarrow{f} & B \\
{\scriptstyle h}\searrow & & \swarrow{\scriptstyle g} \\
& C &
\end{array}
$$

is said to be **commutative** if $g\circ f=h$. Similarly, a **diagram**

$$
\begin{array}{ccc}
A & \xrightarrow{f} & B \\
{\scriptstyle\varphi}\downarrow & & \downarrow{\scriptstyle g} \\
C & \xrightarrow{\psi} & D
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-11" aria-hidden="true"></span>

is said to be **commutative** if $g\circ f=\psi\circ\varphi$. We deal sometimes with more complicated diagrams, consisting of arrows between various objects. Such diagrams are called commutative if, whenever it is possible to go from one object to another by means of two sequences of arrows, say

$$
A_1\xrightarrow{f_1}A_2\xrightarrow{f_2}\cdots\xrightarrow{f_{n-1}}A_n
$$

and

$$
A_1\xrightarrow{g_1}B_2\xrightarrow{g_2}\cdots\xrightarrow{g_{m-1}}B_m=A_n,
$$

then

$$
f_{n-1}\circ\cdots\circ f_1=g_{m-1}\circ\cdots\circ g_1,
$$

in other words, the composite maps are equal. Most of our diagrams are composed of triangles or squares as above, and to verify that a diagram consisting of triangles or squares is commutative, it suffices to verify that each triangle and square in it is commutative.

We assume that the reader is acquainted with the integers and rational numbers, denoted respectively by $\mathbf{Z}$ and $\mathbf{Q}$. For many of our examples, we also assume that the reader knows the real and complex numbers, denoted by $\mathbf{R}$ and $\mathbf{C}$.

Let $A$ and $I$ be two sets. By a family of elements of $A$, indexed by $I$, one means a map $f:I\to A$. Thus for each $i\in I$ we are given an element $f(i)\in A$. Although a family does not differ from a map, we think of it as determining a collection of objects from $A$, and write it often as

$$
\{f(i)\}_{i\in I}
$$

or

$$
\{a_i\}_{i\in I},
$$

writing $a_i$ instead of $f(i)$. We call $I$ the indexing set.

We assume that the reader knows what an equivalence relation is. Let $A$ be a set with an equivalence relation, let $E$ be an equivalence class of elements of $A$. We sometimes try to define a map of the equivalence classes into some set $B$. To define such a map $f$ on the class $E$, we sometimes first give its value on an element $x\in E$ (called a representative of $E$), and then show that it is independent of the choice of representative $x\in E$. In that case we say that $f$ is **well defined**.

We have products of sets, say finite products $A\times B$, or $A_1\times\cdots\times A_n$, and products of families of sets.

We shall use Zorn's lemma, which we describe in Appendix 2.

We let $\#(S)$ denote the number of elements of a set $S$, also called the **cardinality** of $S$. The notation is usually employed when $S$ is finite. We also write $\#(S)=\operatorname{card}(S)$.
