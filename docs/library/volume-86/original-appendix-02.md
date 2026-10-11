---
title: "Appendix 2: Some Set Theory"
description: "Serge Lang《Algebra》English。"
pageClass: algebra-reading
prev: {"text":"Appendix 1: The Transcendence of e and π","link":"/library/volume-86/original-appendix-01"}
next: {"text":"Bibliography","link":"/library/volume-86/original-bibliography"}
---

# Appendix 2: Some Set Theory

<span class="original-page-anchor" id="pdf-page-882" aria-hidden="true"></span>

## §1. DENUMERABLE SETS

Let $n$ be a positive integer. Let $J_n$ be the set consisting of all integers $k$, $1\leqq k\leqq n$. If $S$ is a set, we say that $S$ has $n$ elements if there is a bijection between $S$ and $J_n$. Such a bijection associates with each integer $k$ as above an element of $S$, say $k\mapsto a_k$. Thus we may use $J_n$ to “count” $S$. Part of what we assume about the basic facts concerning positive integers is that if $S$ has $n$ elements, then the integer $n$ is uniquely determined by $S$.

One also agrees to say that a set has $0$ elements if the set is empty.

We shall say that a set $S$ is **denumerable** if there exists a bijection of $S$ with the set of positive integers $\mathbf Z^+$. Such a bijection is then said to **enumerate** the set $S$. It is a mapping

$$
n\mapsto a_n
$$

which to each positive integer $n$ associates an element of $S$, the mapping being injective and surjective.

If $D$ is a denumerable set, and $f:S\longrightarrow D$ is a bijection of some set $S$ with $D$, then $S$ is also denumerable. Indeed, there is a bijection $g:D\longrightarrow\mathbf Z^+$, and hence $g\circ f$ is a bijection of $S$ with $\mathbf Z^+$.

Let $T$ be a set. A **sequence** of elements of $T$ is simply a mapping of $\mathbf Z^+$ into $T$. If the map is given by the association $n\mapsto x_n$, we also write the sequence as $\{x_n\}_{n\geqq1}$, or also $\{x_1,x_2,\ldots\}$. For simplicity, we also write $\{x_n\}$ for the sequence. Thus we think of the sequence as prescribing a first, second, $\ldots$, $n$-th element of $T$. We use the same braces for sequences as for sets, but the context will always make our meaning clear.

<span class="original-page-anchor" id="pdf-page-883" aria-hidden="true"></span>

**Examples.** The even positive integers may be viewed as a sequence $\{x_n\}$ if we put $x_n=2n$ for $n=1,2,\ldots$. The odd positive integers may also be viewed as a sequence $\{y_n\}$ if we put $y_n=2n-1$ for $n=1,2,\ldots$. In each case, the sequence gives an enumeration of the given set.

We also use the word *sequence* for mappings of the natural numbers into a set, thus allowing our sequences to start from $0$ instead of $1$. If we need to specify whether a sequence starts with the $0$-th term or the first term, we write

$$
\{x_n\}_{n\geqq0}\quad\text{or}\quad\{x_n\}_{n\geqq1}
$$

according to the desired case. Unless otherwise specified, however, we always assume that a sequence will start with the first term. Note that from a sequence $\{x_n\}_{n\geqq0}$ we can define a new sequence by letting $y_n=x_{n-1}$ for $n\geqq1$. Then $y_1=x_0,y_2=x_1,\ldots$. Thus there is no essential difference between the two kinds of sequences.

Given a sequence $\{x_n\}$, we call $x_n$ the $n$-th term of the sequence. A sequence may very well be such that all its terms are equal. For instance, if we let $x_n=1$ for all $n\geqq1$, we obtain the sequence $\{1,1,1,\ldots\}$. Thus there is a difference between a sequence of elements in a set $T$, and a subset of $T$. In the example just given, the set of all terms of the sequence consists of one element, namely the single number $1$.

Let $\{x_1,x_2,\ldots\}$ be a sequence in a set $S$. By a **subsequence** we shall mean a sequence $\{x_{n_1},x_{n_2},\ldots\}$ such that $n_1<n_2<\cdots$. For instance, if $\{x_n\}$ is the sequence of positive integers, $x_n=n$, the sequence of even positive integers $\{x_{2n}\}$ is a subsequence.

An enumeration of a set $S$ is of course a sequence in $S$.

A set is **finite** if the set is empty, or if the set has $n$ elements for some positive integer $n$. If a set is not finite, it is called **infinite**.

Occasionally, a map of $J_n$ into a set $T$ will be called a **finite sequence** in $T$. A finite sequence is written as usual,

$$
\{x_1,\ldots,x_n\}\quad\text{or}\quad\{x_i\}_{i=1,\ldots,n}.
$$

When we need to specify the distinction between finite sequences and maps of $\mathbf Z^+$ into $T$, we call the latter infinite sequences. Unless otherwise specified, we shall use the word sequence to mean infinite sequence.

**Proposition 1.1.** *Let $D$ be an infinite subset of $\mathbf Z^+$. Then $D$ is denumerable, and in fact there is a unique enumeration of $D$, say $\{k_1,k_2,\ldots\}$ such that*

$$
k_1<k_2<\cdots<k_n<k_{n+1}<\cdots.
$$

*Proof.* We let $k_1$ be the smallest element of $D$. Suppose inductively that we have defined $k_1<\cdots<k_n$, in such a way that any element $k$ in $D$ which is not equal to $k_1,\ldots,k_n$ is $>k_n$. We define $k_{n+1}$ to be the smallest element of $D$ which is $>k_n$. Then the map $n\mapsto k_n$ is the desired enumeration of $D$.

<span class="original-page-anchor" id="pdf-page-884" aria-hidden="true"></span>

**Corollary 1.2.** *Let $S$ be a denumerable set and $D$ an infinite subset of $S$. Then $D$ is denumerable.*

*Proof.* Given an enumeration of $S$, the subset $D$ corresponds to a subset of $\mathbf Z^+$ in this enumeration. Using Proposition 1.1, we conclude that we can enumerate $D$.

**Proposition 1.3.** *Every infinite set contains a denumerable subset.*

*Proof.* Let $S$ be an infinite set. For every non-empty subset $T$ of $S$, we select a definite element $a_T$ in $T$. We then proceed by induction. We let $x_1$ be the chosen element $a_S$. Suppose that we have chosen $x_1,\ldots,x_n$ having the property that for each $k=2,\ldots,n$ the element $x_k$ is the selected element in the subset which is the complement of $\{x_1,\ldots,x_{k-1}\}$. We let $x_{n+1}$ be the selected element in the complement of the set $\{x_1,\ldots,x_n\}$. By induction, we thus obtain an association $n\mapsto x_n$ for all positive integers $n$, and since $x_n\ne x_k$ for all $k<n$ it follows that our association is injective, i.e. gives an enumeration of a subset of $S$.

**Proposition 1.4.** *Let $D$ be a denumerable set, and $f:D\longrightarrow S$ a surjective mapping. Then $S$ is denumerable or finite.*

*Proof.* For each $y\in S$, there exists an element $x_y\in D$ such that $f(x_y)=y$ because $f$ is surjective. The association $y\mapsto x_y$ is an injective mapping of $S$ into $D$, because if

$$
y,z\in S\quad\text{and}\quad x_y=x_z
$$

then

$$
y=f(x_y)=f(x_z)=z.
$$

Let $g(y)=x_y$. The image of $g$ is a subset of $D$ and $D$ is denumerable. Since $g$ is a bijection between $S$ and its image, it follows that $S$ is denumerable or finite.

**Proposition 1.5.** *Let $D$ be a denumerable set. Then $D\times D$ (the set of all pairs $(x,y)$ with $x,y\in D$) is denumerable.*

*Proof.* There is a bijection between $D\times D$ and $\mathbf Z^+\times\mathbf Z^+$, so it will suffice to prove that $\mathbf Z^+\times\mathbf Z^+$ is denumerable. Consider the mapping of $\mathbf Z^+\times\mathbf Z^+\longrightarrow\mathbf Z^+$ given by

$$
(m,n)\mapsto2^n3^m.
$$

It is injective, and by Proposition 1.1, our result follows.

**Proposition 1.6.** *Let $\{D_1,D_2,\ldots\}$ be a sequence of denumerable sets. Let $S$ be the union of all sets $D_i$ $(i=1,2,\ldots)$. Then $S$ is denumerable.*

<span class="original-page-anchor" id="pdf-page-885" aria-hidden="true"></span>

*Proof.* For each $i=1,2,\ldots$ we enumerate the elements of $D_i$, as indicated in the following notation:

$$
\begin{array}{rl}
D_1:&\{x_{11},x_{12},x_{13},\ldots\}\\
D_2:&\{x_{21},x_{22},x_{23},\ldots\}\\
&\cdots\\
D_i:&\{x_{i1},x_{i2},x_{i3},\ldots\}\\
&\cdots
\end{array}
$$

The map $f:\mathbf Z^+\times\mathbf Z^+\longrightarrow D$ given by

$$
f(i,j)=x_{ij}
$$

is then a surjective map of $\mathbf Z^+\times\mathbf Z^+$ onto $S$. By Proposition 1.4, it follows that $S$ is denumerable.

**Corollary 1.7.** *Let $F$ be a non-empty finite set and $D$ a denumerable set. Then $F\times D$ is denumerable. If $S_1,S_2,\ldots$ are a sequence of sets, each of which is finite or denumerable, then the union $S_1\cup S_2\cup\cdots$ is denumerable or finite.*

*Proof.* There is an injection of $F$ into $\mathbf Z^+$ and a bijection of $D$ with $\mathbf Z^+$. Hence there is an injection of $F\times\mathbf Z^+$ into $\mathbf Z^+\times\mathbf Z^+$ and we can apply Corollary 1.2 and Proposition 1.6 to prove the first statement. One could also define a surjective map of $\mathbf Z^+\times\mathbf Z^+$ onto $F\times D$. (Cf. Exercises 1 and 4.) As for the second statement, each finite set is contained in some denumerable set, so that the second statement follows from Proposition 1.1 and 1.6.

For convenience, we shall say that a set is **countable** if it is either finite or denumerable.

## §2. ZORN’S LEMMA

In order to deal efficiently with infinitely many sets simultaneously, one needs a special property. To state it, we need some more terminology.

Let $S$ be a set. An **ordering** (also called partial ordering) of $S$ is a relation, written $x\leqq y$, among some pairs of elements of $S$, having the following properties.

**ORD 1.** *We have $x\leqq x$.*

**ORD 2.** *If $x\leqq y$ and $y\leqq z$ then $x\leqq z$.*

**ORD 3.** *If $x\leqq y$ and $y\leqq x$ then $x=y$.*

<span class="original-page-anchor" id="pdf-page-886" aria-hidden="true"></span>

We sometimes write $y\geqq x$ for $x\leqq y$. Note that we don’t require that the relation $x\leqq y$ or $y\leqq x$ hold for every pair of elements $(x,y)$ of $S$. Some pairs may not be comparable. If the ordering satisfies this additional property, then we say that it is a **total ordering**.

**Example 1.** Let $G$ be a group. Let $S$ be the set of subgroups. If $H,H'$ are subgroups of $G$, we define

$$
H\leqq H'
$$

if $H$ is a subgroup of $H'$. One verifies immediately that this relation defines an ordering on $S$. Given two subgroups $H,H'$ of $G$, we do not necessarily have $H\leqq H'$ or $H'\leqq H$.

**Example 2.** Let $R$ be a ring, and let $S$ be the set of left ideals of $R$. We define an ordering in $S$ in a way similar to the above, namely if $L,L'$ are left ideals of $R$, we define

$$
L\leqq L'
$$

if $L\subset L'$.

**Example 3.** Let $X$ be a set, and $S$ the set of subsets of $X$. If $Y,Z$ are subsets of $X$, we define $Y\leqq Z$ if $Y$ is a subset of $Z$. This defines an ordering on $S$.

In all these examples, the relation of ordering is said to be that of inclusion.

In an ordered set, if $x\leqq y$ and $x\ne y$ we then write $x<y$.

Let $A$ be an ordered set, and $B$ a subset. Then we can define an ordering on $B$ by defining $x\leqq y$ for $x,y\in B$ to hold if and only if $x\leqq y$ in $A$. We shall say that $R_0$ is the ordering on $B$ **induced** by $R$, or is the **restriction** to $B$ of the partial ordering of $A$.

Let $S$ be an ordered set. By a **least** element of $S$ (or a **smallest** element) one means an element $a\in S$ such that $a\leqq x$ for all $x\in S$. Similarly, by a **greatest element** one means an element $b$ such that $x\leqq b$ for all $x\in S$.

By a **maximal element** $m$ of $S$ one means an element such that if $x\in S$ and $x\geqq m$, then $x=m$. Note that a maximal element need not be a greatest element. There may be many maximal elements in $S$, whereas if a greatest element exists, then it is unique (proof ?).

Let $S$ be an ordered set. We shall say that $S$ is **totally ordered** if given $x,y\in S$ we have necessarily $x\leqq y$ or $y\leqq x$.

**Example 4.** The integers $\mathbf Z$ are totally ordered by the usual ordering. So are the real numbers.

Let $S$ be an ordered set, and $T$ a subset. An **upper bound** of $T$ (in $S$) is an element $b\in S$ such that $x\leqq b$ for all $x\in T$. A **least upper bound** of $T$ in $S$ is an upper bound $b$ such that, if $c$ is another upper bound, then $b\leqq c$. We shall say <span class="original-page-anchor" id="pdf-page-887" aria-hidden="true"></span>that $S$ is **inductively ordered** if every non-empty totally ordered subset has an upper bound.

We shall say that $S$ is **strictly** inductively ordered if every non-empty totally ordered subset has a least upper bound.

In Examples 1, 2, 3, in each case, the set is strictly inductively ordered. To prove this, let us take Example 1. Let $T$ be a non-empty totally ordered subset of the set of subgroups of $G$. This means that if $H,H'\in T$, then $H\subset H'$ or $H'\subset H$. Let $U$ be the union of all sets in $T$. Then:

**1.** $U$ is a subgroup. *Proof:* If $x,y\in U$, there exist subgroups $H,H'\in T$ such that $x\in H$ and $y\in H'$. If, say, $H\subset H'$, then both $x,y\in H'$ and hence $xy\in H'$. Hence $xy\in U$. Also, $x^{-1}\in H'$, so $x^{-1}\in U$. Hence $U$ is a subgroup.

**2.** $U$ is an upper bound for each element of $T$. *Proof:* Every $H\in T$ is contained in $U$, so $H\leqq U$ for all $H\in T$.

**3.** $U$ is a least upper bound for $T$. *Proof:* Any subgroup of $G$ which contains all the subgroups $H\in T$ must then contain their union $U$.

The proof that the sets in Examples 2, 3 are strictly inductively ordered is entirely similar.

We can now state the property mentioned at the beginning of the section.

**Zorn’s Lemma.** *Let $S$ be a non-empty inductively ordered set. Then there exists a maximal element in $S$.*

As an example of Zorn’s lemma, we shall now prove the infinite version of a theorem given in Chapters 1, §7, and XIV, §2, namely:

*Let $R$ be an entire, principal ring and let $E$ be a free module over $R$. Let $F$ be a submodule. Then $F$ is free. In fact, if $\{v_i\}_{i\in I}$ is a basis for $E$, and $F\ne\{0\}$, then there exists a basis for $F$ indexed by a subset of $I$.*

*Proof.* For each subset $J$ of $I$ we let $E_J$ be the free submodule of $E$ generated by all $v_j,j\in J$, and we let $F_J=E_J\cap F$. We let $S$ be the set of all pairs $(F_J,w)$ where $J$ is a subset of $I$, and $w:J'\longrightarrow F_J$ is a basis of $F_J$ indexed by a subset $J'$ of $J$. We write $w_j$ instead of $w(j)$ for $j\in J'$. If $(F_J,w)$ and $(F_K,u)$ are such pairs, we define $(F_J,w)\leqq(F_K,u)$ if $J\subset K$, if $J'\subset K'$, and if the restriction of $u$ to $J'$ is equal to $w$. (In other words, the basis $u$ for $F_K$ is an extension of the basis $w$ for $F_J$.) This defines an ordering on $S$, and it is immediately verified that $S$ is in fact inductively ordered, and non-empty (say by the finite case of the result). We can therefore apply Zorn’s lemma. Let $(F_J,w)$ be a maximal element. We contend that $J=I$ (this will prove our result). Suppose $J\ne I$ and let $k\in I$ but $k\notin J$. Let $K=J\cup\{k\}$. If

$$
E_{J\cup\{k\}}\cap F=F_J,
$$

<span class="original-page-anchor" id="pdf-page-888" aria-hidden="true"></span>

then $(F_K,w)$ is a bigger pair than $(F_J,w)$ contradicting the maximality assumption. Otherwise there exist elements of $F_K$ which can be written in the form

$$
cv_k+y
$$

with some $y\in E_J$ and $c\in R,c\ne0$. The set of all elements $c\in R$ such that there exists $y\in E_J$ for which $cv_k+y\in F$ is an ideal. Let $a$ be a generator of this ideal, and let

$$
w_k=av_k+y
$$

be an element of $F$, with $y\in E_J$. If $z\in F_K$ then there exists $b\in R$ such that $z-bw_k\in E_J$. But $z-bw_k\in F$, whence $z-bw_k\in F_J$. It follows at once that the family consisting of $w_j$ $(j\in J)$ and $w_k$ is a basis for $F_K$, thus contradicting the maximality again. This proves what we wanted.

Zorn’s lemma could be just taken as an axiom of set theory. However, it is not psychologically completely satisfactory as an axiom, because its statement is too involved, and one does not visualize easily the existence of the maximal element asserted in that statement. We show how one can prove Zorn’s lemma from other properties of sets which everyone would immediately grant as acceptable psychologically.

From now on to the end of the proof of Theorem 2.1, we let $A$ be a non-empty partially ordered and strictly inductively ordered set. We recall that **strictly inductively ordered** means that every nonempty totally ordered subset has a least upper bound. We assume given a map $f:A\longrightarrow A$ such that for all $x\in A$ we have $x\leqq f(x)$. We could call such a map an **increasing** map.

Let $a\in A$. Let $B$ be a subset of $A$. We shall say that $B$ is **admissible** if:

**1.** $B$ contains $a$.

**2.** We have $f(B)\subset B$.

**3.** Whenever $T$ is a non-empty totally ordered subset of $B$, the least upper bound of $T$ in $A$ lies in $B$.

Then $B$ is also strictly inductively ordered, by the induced ordering of $A$. We shall prove:

**Theorem 2.1.** (Bourbaki). *Let $A$ be a non-empty partially ordered and strictly inductively ordered set. Let $f:A\longrightarrow A$ be an increasing mapping. Then there exists an element $x_0\in A$ such that $f(x_0)=x_0$.*

*Proof.* Suppose that $A$ were totally ordered. By assumption, it would have a least upper bound $b\in A$, and then

$$
b\leqq f(b)\leqq b,
$$

<span class="original-page-anchor" id="pdf-page-889" aria-hidden="true"></span>

so that in this case, our theorem is clear. The whole problem is to reduce the theorem to that case. In other words, what we need to find is a totally ordered admissible subset of $A$.

If we throw out of $A$ all elements $x\in A$ such that $x$ is not $\geqq a$, then what remains is obviously an admissible subset. Thus without loss of generality, we may assume that $A$ has a least element $a$, that is $a\leqq x$ for all $x\in A$.

Let $M$ be the intersection of all admissible subsets of $A$. Note that $A$ itself is an admissible subset, and that all admissible subsets of $A$ contain $a$, so that $M$ is not empty. Furthermore, $M$ is itself an admissible subset of $A$. To see this, let $x\in M$. Then $x$ is in every admissible subset, so $f(x)$ is also in every admissible subset, and hence $f(x)\in M$. Hence $f(M)\subset M$. If $T$ is a totally ordered non-empty subset of $M$, and $b$ is the least upper bound of $T$ in $A$, then $b$ lies in every admissible subset of $A$, and hence lies in $M$. It follows that $M$ is the smallest admissible subset of $A$, and that any admissible subset of $A$ contained in $M$ is equal to $M$.

We shall prove that $M$ is totally ordered, and thereby prove Theorem 2.1.

[First we make some remarks which don’t belong to the proof, but will help in the understanding of the subsequent lemmas. Since $a\in M$, we see that $f(a)\in M$, $f\circ f(a)\in M$, and in general $f^n(a)\in M$. Furthermore,

$$
a\leqq f(a)\leqq f^2(a)\leqq\cdots.
$$

If we had an equality somewhere, we would be finished, so we may assume that the inequalities hold. Let $D_0$ be the totally ordered set $\{f^n(a)\}_{n\geqq0}$. Then $D_0$ looks like this:

$$
a<f(a)<f^2(a)<\cdots<f^n(a)<\cdots.
$$

Let $a_1$ be the least upper bound of $D_0$. Then we can form

$$
a_1<f(a_1)<f^2(a_1)<\cdots
$$

in the same way to obtain $D_1$, and we can continue this process, to obtain

$$
D_1,D_2,\ldots.
$$

It is clear that $D_1,D_2,\ldots$ are contained in $M$. If we had a precise way of expressing the fact that we can establish a never-ending string of such denumerable sets, then we would obtain what we want. The point is that we are now trying to prove Zorn’s lemma, which is the natural tool for guaranteeing the existence of such a string. However, given such a string, we observe that its elements have two properties: If $c$ is an element of such a string and $x<c$, then $f(x)\leqq c$. Furthermore, there is no element between $c$ and $f(c)$, that is if $x$ is an element of the string, then $x\leqq c$ or $f(c)\leqq x$. We shall now prove two lemmas which show that elements of $M$ have these properties.]

<span class="original-page-anchor" id="pdf-page-890" aria-hidden="true"></span>

Let $c\in M$. We shall say that $c$ is an **extreme point** of $M$ if whenever $x\in M$ and $x<c$, then $f(x)\leqq c$. For each extreme point $c\in M$ we let

$$
M_c=\text{set of }x\in M\quad\text{such that}\quad x\leqq c\quad\text{or}\quad f(c)\leqq x.
$$

Note that $M_c$ is not empty because $a$ is in it.

**Lemma 2.2.** *We have $M_c=M$ for every extreme point $c$ of $M$.*

*Proof.* It will suffice to prove that $M_c$ is an admissible subset. Let $x\in M_c$. If $x<c$ then $f(x)\leqq c$ so $f(x)\in M_c$. If $x=c$ then $f(x)=f(c)$ is again in $M_c$. If $f(c)\leqq x$, then $f(c)\leqq x\leqq f(x)$, so once more $f(x)\in M_c$. Thus we have proved that $f(M_c)\subset M_c$.

Let $T$ be a totally ordered subset of $M_c$ and let $b$ be the least upper bound of $T$ in $M$. If all elements $x\in T$ are $\leqq c$, then $b\leqq c$ and $b\in M_c$. If some $x\in T$ is such that $f(c)\leqq x$, then $f(c)\leqq x\leqq b$, and so $b$ is in $M_c$. This proves our lemma.

**Lemma 2.3.** *Every element of $M$ is an extreme point.*

*Proof.* Let $E$ be the set of extreme points of $M$. Then $E$ is not empty because $a\in E$. It will suffice to prove that $E$ is an admissible subset. We first prove that $f$ maps $E$ into itself. Let $c\in E$. Let $x\in M$ and suppose $x<f(c)$. We must prove that $f(x)\leqq f(c)$. By Lemma 2.2, $M=M_c$, and hence we have $x<c$, or $x=c$, or $f(c)\leqq x$. This last possibility cannot occur because $x<f(c)$. If $x<c$ then

$$
f(x)\leqq c\leqq f(c).
$$

If $x=c$ then $f(x)=f(c)$, and hence $f(E)\subset E$.

Next let $T$ be a totally ordered subset of $E$. Let $b$ be the least upper bound of $T$ in $M$. We must prove that $b\in E$. Let $x\in M$ and $x<b$. If for all $c\in T$ we have $f(c)\leqq x$, then $c\leqq f(c)\leqq x$ implies that $x$ is an upper bound for $T$, whence $b\leqq x$, which is impossible. Since $M_c=M$ for all $c\in E$, we must therefore have $x\leqq c$ for some $c\in T$. If $x<c$, then $f(x)\leqq c\leqq b$, and if $x=c$, then

$$
c=x<b.
$$

Since $c$ is an extreme point and $M_c=M$, we get $f(x)\leqq b$. This proves that $b\in E$, that $E$ is admissible, and thus proves Lemma 2.3.

We now see trivially that $M$ is totally ordered. For let $x,y\in M$. Then $x$ is an extreme point of $M$ by Lemma 2, and $y\in M_x$ so $y\leqq x$ or

$$
x\leqq f(x)\leqq y,
$$

thereby proving that $M$ is totally ordered. As remarked previously, this concludes the proof of Theorem 2.1.

<span class="original-page-anchor" id="pdf-page-891" aria-hidden="true"></span>

We shall obtain Zorn’s lemma essentially as a corollary of Theorem 2.1. We first obtain Zorn’s lemma in a slightly weaker form.

**Corollary 2.4.** *Let $A$ be a non-empty strictly inductively ordered set. Then $A$ has a maximal element.*

*Proof.* Suppose that $A$ does not have a maximal element. Then for each $x\in A$ there exists an element $y_x\in A$ such that $x<y_x$. Let $f:A\longrightarrow A$ be the map such that $f(x)=y_x$ for all $x\in A$. Then $A,f$ satisfy the hypotheses of Theorem 2.1 and applying Theorem 2.1 yields a contradiction.

The only difference between Corollary 2.4 and Zorn’s lemma is that in Corollary 2.4, we assume that a non-empty totally ordered subset has a *least* upper bound, rather than an upper bound. It is, however, a simple matter to reduce Zorn’s lemma to the seemingly weaker form of Corollary 2.4. We do this in the second corollary.

**Corollary 2.5. (Zorn’s lemma).** *Let $S$ be a non-empty inductively ordered set. Then $S$ has a maximal element.*

*Proof.* Let $A$ be the set of non-empty totally ordered subsets of $S$. Then $A$ is not empty since any subset of $S$ with one element belongs to $A$. If $X,Y\in A$, we define $X\leqq Y$ to mean $X\subset Y$. Then $A$ is partially ordered, and is in fact strictly inductively ordered. For let $T=\{X_i\}_{i\in I}$ be a totally ordered subset of $A$. Let

$$
Z=\bigcup_{i\in I}X_i.
$$

Then $Z$ is totally ordered. To see this, let $x,y\in Z$. Then $x\in X_i$ and $y\in X_j$ for some $i,j\in I$. Since $T$ is totally ordered, say $X_i\subset X_j$. Then $x,y\in X_j$ and since $X_j$ is totally ordered, $x\leqq y$ or $y\leqq x$. Thus $Z$ is totally ordered, and is obviously a least upper bound for $T$ in $A$. By Corollary 2.4, we conclude that $A$ has a maximal element $X_0$. This means that $X_0$ is a maximal totally ordered subset of $S$ (non-empty). Let $m$ be an upper bound for $X_0$ in $S$. Then $m$ is the desired maximal element of $S$. For if $x\in S$ and $m\leqq x$ then $X_0\cup\{x\}$ is totally ordered, whence equal to $X_0$ by the maximality of $X_0$. Thus $x\in X_0$ and $x\leqq m$. Hence $x=m$, as was to be shown.

## §3. CARDINAL NUMBERS

Let $A,B$ be sets. We shall say that the **cardinality** of $A$ is the same as the cardinality of $B$, and write

$$
\operatorname{card}(A)=\operatorname{card}(B)
$$

if there exists a bijection of $A$ onto $B$.

<span class="original-page-anchor" id="pdf-page-892" aria-hidden="true"></span>

We say $\operatorname{card}(A)\leqq\operatorname{card}(B)$ if there exists an injective mapping (injection) $f:A\longrightarrow B$. We also write $\operatorname{card}(B)\geqq\operatorname{card}(A)$ in this case. It is clear that if $\operatorname{card}(A)\leqq\operatorname{card}(B)$ and $\operatorname{card}(B)\leqq\operatorname{card}(C)$, then $\operatorname{card}(A)\leqq\operatorname{card}(C)$.

This amounts to saying that a composite of injective mappings is injective. Similarly, if $\operatorname{card}(A)=\operatorname{card}(B)$ and $\operatorname{card}(B)=\operatorname{card}(C)$ then $\operatorname{card}(A)=\operatorname{card}(C)$.

This amounts to saying that a composite of bijective mappings is bijective. **We clearly have $\operatorname{card}(A)=\operatorname{card}(A)$. Using Zorn’s lemma, it is easy to show (see Exercise 14) that**

$$
\operatorname{card}(A)\leqq\operatorname{card}(B)\quad\text{or}\quad\operatorname{card}(B)\leqq\operatorname{card}(A).
$$

*Let $f:A\longrightarrow B$ be a surjective map of a set $A$ onto a set $B$. Then*

$$
\operatorname{card}(B)\leqq\operatorname{card}(A).
$$

This is easily seen, because for each $y\in B$ there exists an element $x\in A$, denoted by $x_y$, such that $f(x_y)=y$. Then the association $y\mapsto x_y$ is an injective mapping of $B$ into $A$, whence by definition, $\operatorname{card}(B)\leqq\operatorname{card}(A)$.

***Given two nonempty sets $A,B$ we have $\operatorname{card}(A)\leqq\operatorname{card}(B)$ or $\operatorname{card}(B)\leqq\operatorname{card}(A)$.***

**This is a simple application of Zorn’s lemma. We consider the family of pairs $(S,f)$ where $S$ is a subset of $A$ and $f:S\longrightarrow B$ is an injective mapping. From the existence of a maximal element, the assertion follows at once.**

**Theorem 3.1.** (Schroeder-Bernstein). *Let $A,B$ be sets, and suppose that $\operatorname{card}(A)\leqq\operatorname{card}(B)$, and $\operatorname{card}(B)\leqq\operatorname{card}(A)$. Then*

$$
\operatorname{card}(A)=\operatorname{card}(B).
$$

*Proof.* Let

$$
f:A\longrightarrow B\quad\text{and}\quad g:B\longrightarrow A
$$

be injections. We separate $A$ into two disjoint sets $A_1$ and $A_2$. We let $A_1$ consist of all $x\in A$ such that, when we lift back $x$ by a succession of inverse maps,

$$
x,g^{-1}(x),f^{-1}\circ g^{-1}(x),g^{-1}\circ f^{-1}\circ g^{-1}(x),\ldots
$$

then at some stage we reach an element of $A$ which cannot be lifted back to $B$ by $g$. We let $A_2$ be the complement of $A_1$, in other words, the set of $x\in A$ which can be lifted back indefinitely, or such that we get stopped in $B$ (i.e. reach an element of $B$ which has no inverse image in $A$ by $f$). Then $A=A_1\cup A_2$. We shall define a bijection $h$ of $A$ onto $B$.

If $x\in A_1$, we define $h(x)=f(x)$.

If $x\in A_2$, we define $h(x)=g^{-1}(x)=$ unique element $y\in B$ such that $g(y)=x$.

Then trivially, $h$ is injective. We must prove that $h$ is surjective. Let $b\in B$. If, when we try to lift back $b$ by a succession of maps

$$
f^{-1},g^{-1}\circ f^{-1},f^{-1}\circ g^{-1}\circ f^{-1}(b)
$$

<span class="original-page-anchor" id="pdf-page-893" aria-hidden="true"></span>

**we can lift back indefinitely, or if we get stopped in $B$, then $g(b)$ belongs to $A_2$ and consequently $b=h(g(b))$, so $b$ lies in the image of $h$. On the other hand, if we cannot lift back $b$ indefinitely, and get stopped in $A$, then $f^{-1}(b)$ is defined (i.e., $b$ is in the image of $f$), and $f^{-1}(b)$ lies in $A_1$. In this case, $b=h(f^{-1}(b))$ is also in the image of $h$, as was to be shown.**

Next we consider theorems concerning sums and products of cardinalities. **We shall reduce the study of cardinalities of products of arbitrary sets to the denumerable case, using Zorn’s lemma. Note first that an infinite set $A$ always contains a denumerable set. Indeed, since $A$ is infinite, we can first select an element $a_1\in A$, and the complement of $\{a_1\}$ is infinite. Inductively, if we have selected distinct elements $a_1,\ldots,a_n$ in $A$, the complement of $\{a_1,\ldots,a_n\}$ is infinite, and we can select $a_{n+1}$ in this complement. In this way, we obtain a sequence of distinct elements of $A$, giving rise to a denumerable subset of $A$.**

Let $A$ be a set. By a **covering** of $A$ one means a set $\Gamma$ of subsets of $A$ such that the union

$$
\bigcup_{C\in\Gamma}C
$$

of all the elements of $\Gamma$ is equal to $A$. We shall say that $\Gamma$ is a **disjoint covering** if whenever $C,C'\in\Gamma$, and $C\ne C'$, then the intersection of $C$ and $C'$ is empty.

**Lemma 3.2.** *Let $A$ be an infinite set. Then there exists a disjoint covering of $A$ by denumerable sets.*

*Proof.* Let $S$ be the set whose elements are pairs $(B,\Gamma)$ consisting of a subset $B$ of $A$, and a disjoint covering of $B$ by denumerable sets. Then $S$ is not empty. Indeed, since $A$ is infinite, $A$ contains a denumerable set $D$, and the pair $(D,\{D\})$ is in $S$. If $(B,\Gamma)$ and $(B',\Gamma')$ are elements of $S$, we define

$$
(B,\Gamma)\leqq(B',\Gamma')
$$

to mean that $B\subset B'$, and $\Gamma\subset\Gamma'$. Let $T$ be a totally ordered non-empty subset of $S$. We may write $T=\{(B_i,\Gamma_i)\}_{i\in I}$ for some indexing set $I$. Let

$$
B=\bigcup_{i\in I}B_i\quad\text{and}\quad\Gamma=\bigcup_{i\in I}\Gamma_i.
$$

If $C,C'\in\Gamma,C\ne C'$, then there exists some indices $i,j$ such that $C\in\Gamma_i$ and $C'\in\Gamma_j$. Since $T$ is totally ordered, we have, say,

$$
(B_i,\Gamma_i)\leqq(B_j,\Gamma_j).
$$

Hence in fact, $C,C'$ are both elements of $\Gamma_j$, and hence $C,C'$ have an empty intersection. On the other hand, if $x\in B$, then $x\in B_i$ for some $i$, and hence there is some $C\in\Gamma_i$ such that $x\in C$. Hence $\Gamma$ is a disjoint covering of $B$. Since the <span class="original-page-anchor" id="pdf-page-894" aria-hidden="true"></span>elements of each $\Gamma_i$ are denumerable subsets of $A$, it follows that $\Gamma$ is a disjoint covering of $B$ by denumerable sets, so $(B,\Gamma)$ is in $S$, and is obviously an upper bound for $T$. Therefore $S$ is inductively ordered.

Let $(M,\Delta)$ be a maximal element of $S$, by Zorn’s lemma. Suppose that $M\ne A$. If the complement of $M$ in $A$ is infinite, then there exists a denumerable set $D$ contained in this complement. Then

$$
(M\cup D,\Delta\cup\{D\})
$$

is a bigger pair than $(M,\Delta)$, contradicting the maximality of $(M,\Delta)$. Hence the complement of $M$ in $A$ is a finite set $F$. Let $D_0$ be an element of $\Delta$. Let

$$
D_1=D_0\cup F.
$$

Then $D_1$ is denumerable. Let $\Delta_1$ be the set consisting of all elements of $\Delta$, except $D_0$, together with $D_1$. Then $\Delta_1$ is a disjoint covering of $A$ by denumerable sets, as was to be shown.

**Theorem 3.3.** *Let $A$ be an infinite set, and let $D$ be a denumerable set. Then*

$$
\operatorname{card}(A\times D)=\operatorname{card}(A).
$$

*Proof.* By the lemma, we can write

$$
A=\bigcup_{i\in I}D_i
$$

as a disjoint union of denumerable sets. Then

$$
A\times D=\bigcup_{i\in I}(D_i\times D).
$$

For each $i\in I$, there is a bijection of $D_i\times D$ on $D_i$ by Proposition 1.5. Since the sets $D_i\times D$ are disjoint, we get in this way a bijection of $A\times D$ on $A$, as desired.

**Corollary 3.4.** *If $F$ is a finite non-empty set, then*

$$
\operatorname{card}(A\times F)=\operatorname{card}(A).
$$

*Proof.* We have

$$
\operatorname{card}(A)\leqq\operatorname{card}(A\times F)\leqq\operatorname{card}(A\times D)=\operatorname{card}(A).
$$

We can then use Theorem 3.1 to get what we want.

**Corollary 3.5.** *Let $A,B$ be non-empty sets, $A$ infinite, and suppose*

$$
\operatorname{card}(B)\leqq\operatorname{card}(A).
$$

<span class="original-page-anchor" id="pdf-page-895" aria-hidden="true"></span>

*Then*

$$
\operatorname{card}(A\cup B)=\operatorname{card}(A).
$$

**Proof. We can write $A\cup B=A\cup C$ for some subset $C$ of $B$, such that $C$ and $A$ are disjoint. (We let $C$ be the set of all elements of $B$ which are not elements of $A$.) Then $\operatorname{card}(C)\leqq\operatorname{card}(A)$. We can then construct an injection of $A\cup C$ into the product**

$$
A\times\{1,2\}
$$

**of $A$ with a set consisting of $2$ elements. Namely, we have a bijection of $A$ with $A\times\{1\}$ in the obvious way, and also an injection of $C$ into $A\times\{2\}$. Thus**

$$
\operatorname{card}(A\cup C)\leqq\operatorname{card}(A\times\{1,2\}).
$$

**We conclude the proof by Corollary 3.4 and Theorem 3.1.**

**Theorem 3.6.** *Let $A$ be an infinite set. Then*

$$
\operatorname{card}(A\times A)=\operatorname{card}(A).
$$

**Proof. Let $S$ be the set consisting of pairs $(B,f)$ where $B$ is an infinite subset of $A$, and $f$ is a bijection of $B$ onto $B\times B$. Then $S$ is not empty because if $D$ is a denumerable subset of $A$, we can always find a bijection of $D$ on $D\times D$. If $(B,f)$ and $(B',f')$ are in $S$, we define $(B,f)\leqq(B',f')$ to mean $B\subset B'$, and the restriction of $f'$ to $B$ is equal to $f$. Then $S$ is partially ordered, and we contend that $S$ is inductively ordered. Let $T$ be a non-empty totally ordered subset of $S$, and say $T$ consists of the pairs $(B_i,f_i)$ for $i$ in some indexing set $I$. Let**

$$
M=\bigcup_{i\in I}B_i.
$$

**We shall define a bijection $g:M\longrightarrow M\times M$. If $x\in M$, then $x$ lies in some $B_i$. We define $g(x)=f_i(x)$. This value $f_i(x)$ is independent of the choice of $B_i$ in which $x$ lies. Indeed, if $x\in B_j$ for some $j\in I$, then say**

$$
(B_i,f_i)\leqq(B_j,f_j).
$$

**By assumption, $B_i\subset B_j$, and $f_j(x)=f_i(x)$, so $g$ is well defined. To show $g$ is surjective, let $x,y\in M$ and $(x,y)\in M\times M$. Then $x\in B_i$ for some $i\in I$ and $y\in B_j$ for some $j\in I$. Again since $T$ is totally ordered, say $(B_i,f_i)\leqq(B_j,f_j)$. Thus $B_i\subset B_j$, and $x,y\in B_j$. There exists an element $b\in B_j$ such that**

$$
f_j(b)=(x,y)\in B_j\times B_j.
$$

**By definition, $g(b)=(x,y)$, so $g$ is surjective. We leave the proof that $g$ is injective to the reader to conclude the proof that $g$ is a bijection. We then see** <span class="original-page-anchor" id="pdf-page-896" aria-hidden="true"></span>that $(M,g)$ is an upper bound for $T$ in $S$, and therefore that $S$ is inductively ordered.

**Let $(M,g)$ be a maximal element of $S$, and let $C$ be the complement of $M$ in $A$. If $\operatorname{card}(C)\leqq\operatorname{card}(M)$, then**

$$
\operatorname{card}(A)=\operatorname{card}(M\cup C)=\operatorname{card}(M)
$$

**by Corollary 3.5, and hence $\operatorname{card}(M)=\operatorname{card}(A)$. Since $\operatorname{card}(M)=\operatorname{card}(M\times M)$, we are done with the proof in this case. If**

$$
\operatorname{card}(M)\leqq\operatorname{card}(C),
$$

**then there exists a subset $M_1$ of $C$ having the same cardinality as $M$. We consider**

$$
\begin{aligned}
&(M\cup M_1)\times(M\cup M_1)\\
&\qquad=(M\times M)\cup(M_1\times M)\cup(M\times M_1)\cup(M_1\times M_1).
\end{aligned}
$$

**By the assumption on $M$ and Corollary 3.5, the last three sets in parentheses on the right of this equation have the same cardinality as $M$. Thus**

$$
(M\cup M_1)\times(M\cup M_1)=(M\times M)\cup M_2
$$

**where $M_2$ is disjoint from $M\times M$, and has the same cardinality as $M$. We now define a bijection**

$$
g_1:M\cup M_1\longrightarrow(M\cup M_1)\times(M\cup M_1).
$$

**We let $g_1(x)=g(x)$ if $x\in M$, and we let $g_1$ on $M_1$ be any bijection of $M_1$ on $M_2$. In this way we have extended $g$ to $M\cup M_1$, and the pair $(M\cup M_1,g_1)$ is in $S$, contradicting the maximality of $(M,g)$. The case $\operatorname{card}(M)\leqq\operatorname{card}(C)$ therefore cannot occur, and our theorem is proved (using Exercise 14 below).**

**Corollary 3.7.** *If $A$ is an infinite set, and $A^{(n)}=A\times\cdots\times A$ is the product taken $n$ times, then*

$$
\operatorname{card}(A^{(n)})=\operatorname{card}(A).
$$

*Proof.* Induction.

**Corollary 3.8.** *If $A_1,\ldots,A_n$ are non-empty sets with $A_n$ infinite, and*

$$
\operatorname{card}(A_i)\leqq\operatorname{card}(A_n)
$$

*for $i=1,\ldots,n$, then*

$$
\operatorname{card}(A_1\times\cdots\times A_n)=\operatorname{card}(A_n).
$$

<span class="original-page-anchor" id="pdf-page-897" aria-hidden="true"></span>

*Proof.* We have

$$
\operatorname{card}(A_n)\leqq\operatorname{card}(A_1\times\cdots\times A_n)\leqq\operatorname{card}(A_n\times\cdots\times A_n)
$$

and we use Corollary 3.7 and the Schroeder-Bernstein theorem to conclude the proof.

**Corollary 3.9.** *Let $A$ be an infinite set, and let $\Phi$ be the set of finite subsets of $A$. Then*

$$
\operatorname{card}(\Phi)=\operatorname{card}(A).
$$

*Proof.* Let $\Phi_n$ be the set of subsets of $A$ having exactly $n$ elements, for each integer $n=1,2,\ldots$. We first show that $\operatorname{card}(\Phi_n)\leqq\operatorname{card}(A)$. If $F$ is an element of $\Phi_n$, we order the elements of $F$ in any way, say

$$
F=\{x_1,\ldots,x_n\}.
$$

and we associate with $F$ the element $(x_1,\ldots,x_n)\in A^{(n)}$,

$$
F\mapsto(x_1,\ldots,x_n).
$$

If $G$ is another subset of $A$ having $n$ elements, say $G=\{y_1,\ldots,y_n\}$, and $G\ne F$, then

$$
(x_1,\ldots,x_n)\ne(y_1,\ldots,y_n).
$$

Hence our map

$$
F\mapsto(x_1,\ldots,x_n)
$$

of $\Phi_n$ into $A^{(n)}$ is injective. By Corollary 3.7, we conclude that

$$
\operatorname{card}(\Phi_n)\leqq\operatorname{card}(A).
$$

Now $\Phi$ is the disjoint union of the $\Phi_n$ for $n=1,2,\ldots$ and it is an exercise to show that $\operatorname{card}(\Phi)\leqq\operatorname{card}(A)$ (cf. Exercise 1). Since

$$
\operatorname{card}(A)\leqq\operatorname{card}(\Phi),
$$

because in particular, $\operatorname{card}(\Phi_1)=\operatorname{card}(A)$, we see that our corollary is proved.

In the next theorem, we shall see that given a set, there always exists another set whose cardinality is bigger.

**Theorem 3.10.** *Let $A$ be an infinite set, and $T$ the set consisting of two elements $\{0,1\}$. Let $M$ be the set of all maps of $A$ into $T$. Then*

$$
\operatorname{card}(A)\leqq\operatorname{card}(M)\quad\text{and}\quad\operatorname{card}(A)\ne\operatorname{card}(M).
$$

<span class="original-page-anchor" id="pdf-page-898" aria-hidden="true"></span>

*Proof.* For each $x\in A$ we let

$$
f_x:A\longrightarrow\{0,1\}
$$

be the map such that $f_x(x)=1$ and $f_x(y)=0$ if $y\ne x$. Then $x\mapsto f_x$ is obviously an injection of $A$ into $M$, so that $\operatorname{card}(A)\leqq\operatorname{card}(M)$. Suppose that

$$
\operatorname{card}(A)=\operatorname{card}(M).
$$

Let

$$
x\mapsto g_x
$$

be a bijection between $A$ and $M$. We define a map $h:A\longrightarrow\{0,1\}$ by the rule

$$
\begin{aligned}
h(x)&=0&&\text{if }g_x(x)=1,\\
h(x)&=1&&\text{if }g_x(x)=0.
\end{aligned}
$$

Then certainly $h\ne g_x$ for any $x$, and this contradicts the assumption that $x\mapsto g_x$ is a bijection, thereby proving Theorem 3.10.

**Corollary 3.11.** *Let $A$ be an infinite set, and let $S$ be the set of all subsets of $A$. Then $\operatorname{card}(A)\leqq\operatorname{card}(S)$ and $\operatorname{card}(A)\ne\operatorname{card}(S)$.*

*Proof.* We leave it as an exercise. [*Hint:* If $B$ is a non-empty subset of $A$, use the characteristic function $\varphi_B$ such that

$$
\begin{aligned}
\varphi_B(x)&=1&&\text{if }x\in B,\\
\varphi_B(x)&=0&&\text{if }x\notin B.
\end{aligned}
$$

What can you say about the association $B\mapsto\varphi_B$?]

## §4. WELL-ORDERING

An ordered set $A$ is said to be **well-ordered** if it is totally ordered, and if every non-empty subset $B$ has a least element, that is, an element $a\in B$ such that $a\leqq x$ for all $x\in B$.

**Example 1.** The set of positive integers $\mathbf Z^+$ is well-ordered. Any finite set can be well-ordered, and a denumerable set $D$ can be well-ordered: Any bijection of $D$ with $\mathbf Z^+$ will give rise to a well-ordering of $D$.

**Example 2.** Let $S$ be a well-ordered set and let $b$ be an element of some set, $b\notin S$. Let $A=S\cup\{b\}$. We define $x\leqq b$ for all $x\in S$. Then $A$ is totally ordered, and is in fact well-ordered.

<span class="original-page-anchor" id="pdf-page-899" aria-hidden="true"></span>

*Proof.* Let $B$ be a non-empty subset of $A$. If $B$ consists of $b$ alone, then $b$ is a least element of $B$. Otherwise, $B$ contains some element $a\in A$. Then $B\cap A$ is not empty, and hence has a least element, which is obviously also a least element for $B$.

**Theorem 4.1.** *Every non-empty set can be well-ordered.*

**Proof. Let $A$ be a non-empty set. Let $S$ be the set of all pairs $(X,\omega)$, where $X$ is a subset of $A$ and $\omega$ is a well-ordering of $X$. Note that $S$ is not empty because any single element of $A$ gives rise to such a pair. If $(X,\omega)$ and $(X',\omega')$ are such pairs, we define $(X,\omega)\leqq(X',\omega')$ if $X\subset X'$, if the ordering induced on $X$ by $\omega'$ is equal to $\omega$, and if $X$ is an initial segment of $X'$. It is obvious that this defines an ordering on $S$, and we contend that $S$ is inductively ordered. Let $\{(X_i,\omega_i)\}$ be a totally ordered non-empty subset of $S$. Let $X=\bigcup X_i$. If $a,b\in X$, then $a,b$ lie in some $X_i$, and we define $a\leqq b$ in $X$ if $a\leqq b$ with respect to the ordering $\omega_i$. This is independent of the choice of $i$ (immediate from the assumption of total ordering). In fact, $X$ is well ordered, for if $Y$ is a non-empty subset of $X$, then there is some element $y\in Y$ which lies in some $X_j$. Let $c$ be a least element of $X_j\cap Y$. One verifies at once that $c$ is a least element of $Y$. We can therefore apply Zorn’s lemma. Let $(X,\omega)$ be a maximal element in $S$. If $X\ne A$, then, using Example 2, we can define a well-ordering on a bigger subset than $X$, contradicting the maximality assumption. This proves Theorem 4.1.**

**Note.** Theorem 4.1 is an immediate and straightforward consequence of Zorn’s lemma. Usually in mathematics, Zorn’s lemma is the most efficient tool when dealing with infinite processes.

## EXERCISES

**1.** Prove the statement made in the proof of Corollary 3.9.

**2.** If $A$ is an infinite set, and $\Phi_n$ is the set of subsets of $A$ having exactly $n$ elements, show that

$$
\operatorname{card}(A)\leqq\operatorname{card}(\Phi_n)
$$

for $n\geqq1$.

**3.** Let $A_i$ be infinite sets for $i=1,2,\ldots$ and assume that

$$
\operatorname{card}(A_i)\leqq\operatorname{card}(A)
$$

for some set $A$, and all $i$. Show that

$$
\operatorname{card}\left(\bigcup_{i=1}^\infty A_i\right)\leqq\operatorname{card}(A).
$$

<span class="original-page-anchor" id="pdf-page-900" aria-hidden="true"></span>

**4.** Let $K$ be a subfield of the complex numbers. Show that for each integer $n\geqq1$, the cardinality of the set of extensions of $K$ of degree $n$ in $\mathbf C$ is $\leqq\operatorname{card}(K)$.

**5.** Let $K$ be an infinite field, and $E$ an algebraic extension of $K$. Show that

$$
\operatorname{card}(E)=\operatorname{card}(K).
$$

**6.** Finish the proof of the Corollary 3.11.

**7.** If $A,B$ are sets, denote by $M(A,B)$ the set of all maps of $A$ into $B$. If $B,B'$ are sets with the same cardinality, show that $M(A,B)$ and $M(A,B')$ have the same cardinality. If $A,A'$ have the same cardinality, show that $M(A,B)$ and $M(A',B)$ have the same cardinality.

**8.** Let $A$ be an infinite set and abbreviate $\operatorname{card}(A)$ by $\alpha$. If $B$ is an infinite set, abbreviate $\operatorname{card}(B)$ by $\beta$. Define $\alpha\beta$ to be $\operatorname{card}(A\times B)$. Let $B'$ be a set disjoint from $A$ such that $\operatorname{card}(B)=\operatorname{card}(B')$. Define $\alpha+\beta$ to be $\operatorname{card}(A\cup B')$. Denote by $B^A$ the set of all maps of $A$ into $B$, and denote $\operatorname{card}(B^A)$ by $\beta^\alpha$. Let $C$ be an infinite set and abbreviate $\operatorname{card}(C)$ by $\gamma$. Prove the following statements:

(a) $\alpha(\beta+\gamma)=\alpha\beta+\alpha\gamma$.

(b) $\alpha\beta=\beta\alpha$.

(c) $\alpha^{\beta+\gamma}=\alpha^\beta\alpha^\gamma$.

**9.** Let $K$ be an infinite field. Prove that there exists an algebraically closed field $K^a$ containing $K$ as a subfield, and algebraic over $K$. [*Hint:* Let $\Omega$ be a set of cardinality strictly greater than the cardinality of $K$, and containing $K$. Consider the set $S$ of all pairs $(E,\varphi)$ where $E$ is a subset of $\Omega$ such that $K\subset E$, and $\varphi$ denotes a law of addition and multiplication on $E$ which makes $E$ into a field such that $K$ is a subfield, and $E$ is algebraic over $K$. Define a partial ordering on $S$ in an obvious way; show that $S$ is inductively ordered, and that a maximal element is algebraic over $K$ and algebraically closed. You will need Exercise 5 in the last step.]

**10.** Let $K$ be an infinite field. Show that the field of rational functions $K(t)$ has the same cardinality as $K$.

**11.** Let $J_n$ be the set of integers $\{1,\ldots,n\}$. Let $\mathbf Z^+$ be the set of positive integers. Show that the following sets have the same cardinality:

(a) The set of all maps $M(\mathbf Z^+,J_n)$.

(b) The set of all maps $M(\mathbf Z^+,J_2)$.

(c) The set of all real numbers $x$ such that $0\leqq x<1$.

(d) The set of all real numbers.

**12.** Show that $M(\mathbf Z^+,\mathbf Z^+)$ has the same cardinality as the real numbers.

**13.** Let $S$ be a non-empty set. Let $S'$ denote the product $S$ with itself taken denumerably many times. Prove that $(S')'$ has the same cardinality as $S'$. [Given a set $S$ whose cardinality is strictly greater than the cardinality of $\mathbf R$, I do not know whether it is always true that $\operatorname{card}S=\operatorname{card}S'$.] Added 1994: The grapevine communicates to me that according to Solovay, the answer is “no.”

**14.** Let $A,B$ be non-empty sets. Prove that $\operatorname{card}(A)\leqq\operatorname{card}(B)$ or $\operatorname{card}(B)\leqq\operatorname{card}(A)$.

[*Hint:* consider the family of pairs $(C,f)$ where $C$ is a subset of $A$ and $f:C\longrightarrow B$ is an injective map. By Zorn’s lemma there is a maximal element. Now finish the proof].
