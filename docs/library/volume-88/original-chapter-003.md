---
title: "General results of representation theory"
description: "《Introduction to Representation Theory》English。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"Basic notions of representation theory","link":"/library/volume-88/original-chapter-002"}
next: {"text":"Representations of finite groups: Basic results","link":"/library/volume-88/original-chapter-004"}
---

# General results of representation theory

<span class="original-page-anchor" id="pdf-page-49" aria-hidden="true"></span>

## 3.1. Subrepresentations in semisimple representations

Let $A$ be an algebra.

**Definition 3.1.1.** A **semisimple** (or **completely reducible**) representation of $A$ is a direct sum of irreducible representations.

**Example 3.1.2.** Let $V$ be an irreducible representation of $A$ of dimension $n$. Then $Y=\operatorname{End}(V)$, with action of $A$ by left multiplication, is a semisimple representation of $A$, isomorphic to $nV$ (the direct sum of $n$ copies of $V$). Indeed, any basis $v_1,\ldots,v_n$ of $V$ gives rise to an isomorphism of representations $\operatorname{End}(V)\to nV$, given by $x\mapsto(xv_1,\ldots,xv_n)$.

**Remark 3.1.3.** Note that by Schur’s lemma, any semisimple representation $V$ of $A$ is canonically identified with $\bigoplus_X\operatorname{Hom}_A(X,V)\otimes X$, where $X$ runs over all irreducible representations of $A$. Indeed, we have a natural map $f:\bigoplus_X\operatorname{Hom}(X,V)\otimes X\to V$, given by $g\otimes x\mapsto g(x)$, $x\in X$, $g\in\operatorname{Hom}(X,V)$, and it is easy to verify that this map is an isomorphism.

<span class="original-page-anchor" id="pdf-page-50" aria-hidden="true"></span>

We’ll see now how Schur’s lemma allows us to classify subrepresentations in finite dimensional semisimple representations.

**Proposition 3.1.4.** Let $V_i$, $1\le i\le m$, be irreducible finite dimensional pairwise nonisomorphic representations of $A$, and let $W$ be a subrepresentation of $V=\bigoplus_{i=1}^m n_iV_i$. Then $W$ is isomorphic to $\bigoplus_{i=1}^m r_iV_i$, $r_i\le n_i$, and the inclusion $\phi:W\to V$ is a direct sum of inclusions $\phi_i:r_iV_i\to n_iV_i$ given by multiplication of a row vector of elements of $V_i$ (of length $r_i$) by a certain $r_i\times n_i$ matrix $X_i$ with linearly independent rows: $\phi(v_1,\ldots,v_{r_i})=(v_1,\ldots,v_{r_i})X_i$.

**Proof.** The proof is by induction in $n:=\sum_{i=1}^m n_i$. The base of induction ($n=1$) is clear. To perform the induction step, let us assume that $W$ is nonzero, and fix an irreducible subrepresentation $P\subset W$. Such $P$ exists (Problem 2.3.15).[^rt-50-1] Now, by Schur’s lemma, $P$ is isomorphic to $V_i$ for some $i$, and the inclusion $\phi|_P:P\to V$ factors through $n_iV_i$ and upon identification of $P$ with $V_i$ is given by the formula $v\mapsto(vq_1,\ldots,vq_{n_i})$, where $q_l\in k$ are not all zero.

Now note that the group $G_i=GL_{n_i}(k)$ of invertible $n_i\times n_i$ matrices over $k$ acts on $n_iV_i$ by $(v_1,\ldots,v_{n_i})\mapsto(v_1,\ldots,v_{n_i})g_i$ (and by the identity on $n_jV_j$, $j\ne i$) and therefore acts on the set of subrepresentations of $V$, preserving the property we need to establish: namely, under the action of $g_i$, the matrix $X_i$ goes to $X_ig_i$, while the matrices $X_j$, $j\ne i$, don’t change. Take $g_i\in G_i$ such that $(q_1,\ldots,q_{n_i})g_i=(1,0,\ldots,0)$. Then $Wg_i$ contains the first summand $V_i$ of $n_iV_i$ (namely, it is $Pg_i$); hence $Wg_i=V_i\oplus W'$, where $W'\subset n_1V_1\oplus\cdots\oplus(n_i-1)V_i\oplus\cdots\oplus n_mV_m$ is the kernel of the projection of $Wg_i$ to the first summand $V_i$ along the other summands. Thus the required statement follows from the induction assumption. $\square$

**Remark 3.1.5.** In Proposition 3.1.4, it is not important that $k$ is algebraically closed, nor does it matter that $V$ is finite dimensional. If these assumptions are dropped, the only change needed is that the entries of the matrix $X_i$ are no longer in $k$ but in $D_i=\operatorname{End}_A(V_i)$, <span class="original-page-anchor" id="pdf-page-51" aria-hidden="true"></span>which is, as we know, a division algebra. The proof of this generalized version of Proposition 3.1.4 is the same as before (check it!).

## 3.2. The density theorem

Let $A$ be an algebra over an algebraically closed field $k$.

**Corollary 3.2.1.** Let $V$ be an irreducible finite dimensional representation of $A$, and let $v_1,\ldots,v_n\in V$ be any linearly independent vectors. Then for any $w_1,\ldots,w_n\in V$ there exists an element $a\in A$ such that $av_i=w_i$.

**Proof.** Assume the contrary. Then the image of the map $A\to nV$ given by $a\mapsto(av_1,\ldots,av_n)$ is a proper subrepresentation, so by Proposition 3.1.4 it corresponds to an $r\times n$ matrix $X$, $r<n$. Thus, taking $a=1$, we see that there exist vectors $u_1,\ldots,u_r\in V$ such that $(u_1,\ldots,u_r)X=(v_1,\ldots,v_n)$. Let $(q_1,\ldots,q_n)$ be a nonzero vector such that $X(q_1,\ldots,q_n)^T=0$ (it exists because $r<n$). Then $\sum q_iv_i=(u_1,\ldots,u_r)X(q_1,\ldots,q_n)^T=0$, i.e. $\sum q_iv_i=0$—a contradiction to the linear independence of $v_i$. $\square$

**Theorem 3.2.2 (The density theorem).** (i) Let $V$ be an irreducible finite dimensional representation of $A$. Then the map $\rho:A\to\operatorname{End}V$ is surjective.

(ii) Let $V=V_1\oplus\cdots\oplus V_r$, where $V_i$ are irreducible pairwise nonisomorphic finite dimensional representations of $A$. Then the map $\bigoplus_{i=1}^r\rho_i:A\to\bigoplus_{i=1}^r\operatorname{End}(V_i)$ is surjective.

**Proof.** (i) Let $B$ be the image of $A$ in $\operatorname{End}(V)$. We want to show that $B=\operatorname{End}(V)$. Let $c\in\operatorname{End}(V)$, let $v_1,\ldots,v_n$ be a basis of $V$, and let $w_i=cv_i$. By Corollary 3.2.1, there exists $a\in A$ such that $av_i=w_i$. Then $a$ maps to $c$, so $c\in B$, and we are done.

(ii) Let $B_i$ be the image of $A$ in $\operatorname{End}(V_i)$, and let $B$ be the image of $A$ in $\bigoplus_{i=1}^r\operatorname{End}(V_i)$. Recall that as a representation of $A$, $\bigoplus_{i=1}^r\operatorname{End}(V_i)$ is semisimple: it is isomorphic to $\bigoplus_{i=1}^r d_iV_i$, where $d_i=\dim V_i$. Then by Proposition 3.1.4, $B=\bigoplus_i B_i$. On the other hand, (i) implies that $B_i=\operatorname{End}(V_i)$. Thus (ii) follows. $\square$

<span class="original-page-anchor" id="pdf-page-52" aria-hidden="true"></span>

## 3.3. Representations of direct sums of matrix algebras

In this section we consider representations of algebras $A=\bigoplus_i\operatorname{Mat}_{d_i}(k)$ for any field $k$.

**Theorem 3.3.1.** Let $A=\bigoplus_{i=1}^r\operatorname{Mat}_{d_i}(k)$. Then the irreducible representations of $A$ are $V_1=k^{d_1},\ldots,V_r=k^{d_r}$, and any finite dimensional representation of $A$ is a direct sum of copies of $V_1,\ldots,V_r$.

In order to prove Theorem 3.3.1, we shall need the notion of a dual representation.

**Definition 3.3.2 (Dual representation).** Let $V$ be a representation of any algebra $A$. Then the **dual representation** $V^*$ is the representation of the opposite algebra $A^{\mathrm{op}}$ (or, equivalently, right $A$-module) with the action

$$
(f\cdot a)(v):=f(av).
$$

**Proof of Theorem 3.3.1.** First, the given representations are clearly irreducible, since for any $v\ne0$, $w\in V_i$, there exists $a\in A$ such that $av=w$. Next, let $X$ be an $n$-dimensional representation of $A$. Then, $X^*$ is an $n$-dimensional representation of $A^{\mathrm{op}}$. But $(\operatorname{Mat}_{d_i}(k))^{\mathrm{op}}\cong\operatorname{Mat}_{d_i}(k)$ with isomorphism $\varphi(X)=X^T$, as $(BC)^T=C^TB^T$. Thus, $A\cong A^{\mathrm{op}}$ and $X^*$ may be viewed as an $n$-dimensional representation of $A$. Define

$$
\phi:\underbrace{A\oplus\cdots\oplus A}_{n\text{ copies}}\longrightarrow X^*
$$

by

$$
\phi(a_1,\ldots,a_n)=a_1y_1+\cdots+a_ny_n
$$

where $\{y_i\}$ is a basis of $X^*$. The map $\phi$ is clearly surjective, as $k\subset A$. Thus, the dual map $\phi^*:X\longrightarrow A^{n*}$ is injective. But $A^{n*}\cong A^n$ as representations of $A$ (check it!). Hence, $\operatorname{Im}\phi^*\cong X$ is a subrepresentation of $A^n$. Next, $\operatorname{Mat}_{d_i}(k)=d_iV_i$, so $A=\bigoplus_{i=1}^r d_iV_i$, $A^n=\bigoplus_{i=1}^r nd_iV_i$, as a representation of $A$. Hence by Proposition 3.1.4, $X=\bigoplus_{i=1}^r m_iV_i$, as desired. $\square$

<span class="original-page-anchor" id="pdf-page-53" aria-hidden="true"></span>

**Problem 3.3.3.** The goal of this problem is to give an alternative proof of Theorem 3.3.1, not using any of the previous results of Chapter 3.

Let $A_1,A_2,\ldots,A_n$ be $n$ algebras with units $1_1,1_2,\ldots,1_n$, respectively. Let $A=A_1\oplus A_2\oplus\cdots\oplus A_n$. Clearly, $1_i1_j=\delta_{ij}1_i$, and the unit of $A$ is $1=1_1+1_2+\cdots+1_n$.

For every representation $V$ of $A$, it is easy to see that $1_iV$ is a representation of $A_i$ for every $i\in\{1,2,\ldots,n\}$. Conversely, if $V_1,V_2,\ldots,V_n$ are representations of $A_1,A_2,\ldots,A_n$, respectively, then $V_1\oplus V_2\oplus\cdots\oplus V_n$ canonically becomes a representation of $A$ (with $(a_1,a_2,\ldots,a_n)\in A$ acting on $V_1\oplus V_2\oplus\cdots\oplus V_n$ as $(v_1,v_2,\ldots,v_n)\mapsto(a_1v_1,a_2v_2,\ldots,a_nv_n)$).

(a) Show that a representation $V$ of $A$ is irreducible if and only if $1_iV$ is an irreducible representation of $A_i$ for exactly one $i\in\{1,2,\ldots,n\}$, while $1_iV=0$ for all the other $i$. Thus, classify the irreducible representations of $A$ in terms of those of $A_1,A_2,\ldots,A_n$.

(b) Let $d\in\mathbb{N}$. Show that the only irreducible representation of $\operatorname{Mat}_d(k)$ is $k^d$, and every finite dimensional representation of $\operatorname{Mat}_d(k)$ is a direct sum of copies of $k^d$.

Hint: For every $(i,j)\in\{1,2,\ldots,d\}^2$, let $E_{ij}\in\operatorname{Mat}_d(k)$ be the matrix with $1$ in the $i$th row of the $j$th column and $0$’s everywhere else. Let $V$ be a finite dimensional representation of $\operatorname{Mat}_d(k)$. Show that $V=E_{11}V\oplus E_{22}V\oplus\cdots\oplus E_{dd}V$, and that $\Phi_i:E_{11}V\to E_{ii}V$, $v\mapsto E_{i1}v$ is an isomorphism for every $i\in\{1,2,\ldots,d\}$. For every $v\in E_{11}V$, denote $S(v)=\langle E_{11}v,E_{21}v,\ldots,E_{d1}v\rangle$. Prove that $S(v)$ is a subrepresentation of $V$ isomorphic to $k^d$ (as a representation of $\operatorname{Mat}_d(k)$), and that $v\in S(v)$. Conclude that $V=S(v_1)\oplus S(v_2)\oplus\cdots\oplus S(v_k)$, where $\{v_1,v_2,\ldots,v_k\}$ is a basis of $E_{11}V$.

(c) Deduce Theorem 3.3.1.

## 3.4. Filtrations

Let $A$ be an algebra. Let $V$ be a representation of $A$.

**Definition 3.4.1.** A (finite) **filtration** of $V$ is a sequence of subrepresentations $0=V_0\subset V_1\subset\cdots\subset V_n=V$.

<span class="original-page-anchor" id="pdf-page-54" aria-hidden="true"></span>

**Lemma 3.4.2.** Any finite dimensional representation $V$ of an algebra $A$ admits a finite filtration $0=V_0\subset V_1\subset\cdots\subset V_n=V$ such that the successive quotients $V_i/V_{i-1}$ are irreducible.

**Proof.** The proof is by induction in $\dim(V)$. The base is clear, and only the induction step needs to be justified. Pick an irreducible subrepresentation $V_1\subset V$, and consider the representation $U=V/V_1$. Then by the induction assumption $U$ has a filtration $0=U_0\subset U_1\subset\cdots\subset U_{n-1}=U$ such that $U_i/U_{i-1}$ are irreducible. Define $V_i$ for $i\ge2$ to be the preimages of $U_{i-1}$ under the tautological projection $V\to V/V_1=U$. Then $0=V_0\subset V_1\subset V_2\subset\cdots\subset V_n=V$ is a filtration of $V$ with the desired property. $\square$

## 3.5. Finite dimensional algebras

**Definition 3.5.1.** The **radical** of a finite dimensional algebra $A$ is the set of all elements of $A$ which act by $0$ in all irreducible representations of $A$. It is denoted $\operatorname{Rad}(A)$.

**Proposition 3.5.2.** $\operatorname{Rad}(A)$ is a two-sided ideal.

**Proof.** Easy. $\square$

**Proposition 3.5.3.** Let $A$ be a finite dimensional algebra.

(i) Let $I$ be a nilpotent two-sided ideal in $A$; i.e., $I^n=0$ for some $n$. Then $I\subset\operatorname{Rad}(A)$.

(ii) $\operatorname{Rad}(A)$ is a nilpotent ideal. Thus, $\operatorname{Rad}(A)$ is the largest nilpotent two-sided ideal in $A$.

**Proof.** (i) Let $V$ be an irreducible representation of $A$. Let $v\in V$. Then $Iv\subset V$ is a subrepresentation. If $Iv\ne0$, then $Iv=V$ so there is $x\in I$ such that $xv=v$. Then $x^n\ne0$, a contradiction. Thus $Iv=0$, so $I$ acts by $0$ in $V$ and hence $I\subset\operatorname{Rad}(A)$.

(ii) Let $0=A_0\subset A_1\subset\cdots\subset A_n=A$ be a filtration of the regular representation of $A$ by subrepresentations such that $A_{i+1}/A_i$ are irreducible. It exists by Lemma 3.4.2. Let $x\in\operatorname{Rad}(A)$. Then $x$ acts on $A_{i+1}/A_i$ by zero, so $x$ maps $A_{i+1}$ to $A_i$. This implies that $\operatorname{Rad}(A)^n=0$, as desired. $\square$

<span class="original-page-anchor" id="pdf-page-55" aria-hidden="true"></span>

**Theorem 3.5.4.** A finite dimensional algebra $A$ has only finitely many irreducible representations $V_i$ up to an isomorphism. These representations are finite dimensional, and

$$
A/\operatorname{Rad}(A)\cong\bigoplus_i\operatorname{End}V_i.
$$

**Proof.** First, for any irreducible representation $V$ of $A$ and for any nonzero $v\in V$, $Av\subseteq V$ is a finite dimensional subrepresentation of $V$. (It is finite dimensional as $A$ is finite dimensional.) As $V$ is irreducible and $Av\ne0$, $V=Av$ and $V$ is finite dimensional.

Next, suppose we have nonisomorphic irreducible representations $V_1,V_2,\ldots,V_r$. By Theorem 3.2.2, the homomorphism

$$
\bigoplus_i\rho_i:A\longrightarrow\bigoplus_i\operatorname{End}V_i
$$

is surjective. So $r\le\sum_i\dim\operatorname{End}V_i\le\dim A$. Thus, $A$ has only finitely many nonisomorphic irreducible representations (not more than $\dim A$).

Now, let $V_1,V_2,\ldots,V_r$ be all nonisomorphic irreducible finite dimensional representations of $A$. By Theorem 3.2.2, the homomorphism

$$
\bigoplus_i\rho_i:A\longrightarrow\bigoplus_i\operatorname{End}V_i
$$

is surjective. The kernel of this map, by definition, is exactly $\operatorname{Rad}(A)$. $\square$

**Corollary 3.5.5.** $\sum_i(\dim V_i)^2\le\dim A$, where the $V_i$’s are the irreducible representations of $A$.

**Proof.** As $\dim\operatorname{End}V_i=(\dim V_i)^2$, Theorem 3.5.4 implies that $\dim A-\dim\operatorname{Rad}(A)=\sum_i\dim\operatorname{End}V_i=\sum_i(\dim V_i)^2$. As $\dim\operatorname{Rad}(A)\ge0$, $\sum_i(\dim V_i)^2\le\dim A$. $\square$

**Example 3.5.6.** 1. Let $A=k[x]/(x^n)$. This algebra has a unique irreducible representation, which is a $1$-dimensional space $k$, in which $x$ acts by zero. So the radical $\operatorname{Rad}(A)$ is the ideal $(x)$.

2. Let $A$ be the algebra of upper triangular $n\times n$ matrices. It is easy to check that the irreducible representations of $A$ are $V_i$, $i=1,\ldots,n$, which are $1$-dimensional, and any matrix $x$ acts by $x_{ii}$.

<span class="original-page-anchor" id="pdf-page-56" aria-hidden="true"></span>

So the radical $\operatorname{Rad}(A)$ is the ideal of strictly upper triangular matrices (as it is a nilpotent ideal and contains the radical). A similar result holds for block-triangular matrices.

**Definition 3.5.7.** A finite dimensional algebra $A$ is said to be **semisimple** if $\operatorname{Rad}(A)=0$.

**Proposition 3.5.8.** For a finite dimensional algebra $A$, the following are equivalent:

(1) $A$ is semisimple.

(2) $\sum_i(\dim V_i)^2=\dim A$, where the $V_i$’s are the irreducible representations of $A$.

(3) $A\cong\bigoplus_i\operatorname{Mat}_{d_i}(k)$ for some $d_i$.

(4) Any finite dimensional representation of $A$ is completely reducible (that is, isomorphic to a direct sum of irreducible representations).

(5) $A$ is a completely reducible representation of $A$.

**Proof.** As $\dim A-\dim\operatorname{Rad}(A)=\sum_i(\dim V_i)^2$, clearly $\dim A=\sum_i(\dim V_i)^2$ if and only if $\operatorname{Rad}(A)=0$. Thus, $(1)\Leftrightarrow(2)$.

By Theorem 3.5.4, if $\operatorname{Rad}(A)=0$, then clearly $A\cong\bigoplus_i\operatorname{Mat}_{d_i}(k)$ for $d_i=\dim V_i$. Thus, $(1)\Rightarrow(3)$. Conversely, if $A\cong\bigoplus_i\operatorname{Mat}_{d_i}(k)$, then by Theorem 3.3.1, $\operatorname{Rad}(A)=0$, so $A$ is semisimple. Thus $(3)\Rightarrow(1)$.

Next, $(3)\Rightarrow(4)$ by Theorem 3.3.1. Clearly $(4)\Rightarrow(5)$. To see that $(5)\Rightarrow(3)$, let $A=\bigoplus_i n_iV_i$. Consider $\operatorname{End}_A(A)$ (endomorphisms of $A$ as a representation of $A$). As the $V_i$’s are pairwise nonisomorphic, by Schur’s lemma, no copy of $V_i$ in $A$ can be mapped to a distinct $V_j$. Also, again by Schur’s lemma, $\operatorname{End}_A(V_i)=k$. Thus, $\operatorname{End}_A(A)\cong\bigoplus_i\operatorname{Mat}_{n_i}(k)$. But $\operatorname{End}_A(A)\cong A^{\mathrm{op}}$ by Problem 2.3.17, so $A^{\mathrm{op}}\cong\bigoplus_i\operatorname{Mat}_{n_i}(k)$. Thus, $A\cong(\bigoplus_i\operatorname{Mat}_{n_i}(k))^{\mathrm{op}}=\bigoplus_i\operatorname{Mat}_{n_i}(k)$, as desired. $\square$

## 3.6. Characters of representations

Let $A$ be an algebra and $V$ a finite dimensional representation of $A$ with action $\rho$. Then the **character** of $V$ is the linear function <span class="original-page-anchor" id="pdf-page-57" aria-hidden="true"></span>$\chi_V:A\longrightarrow k$ given by

$$
\chi_V(a)=\operatorname{Tr}|_V(\rho(a)).
$$

If $[A,A]$ is the span of commutators $[x,y]:=xy-yx$ over all $x,y\in A$, then $[A,A]\subseteq\ker\chi_V$. Thus, we may view the character as a mapping $\chi_V:A/[A,A]\to k$.

**Exercise 3.6.1.** Show that if $W\subset V$ are finite dimensional representations of $A$, then $\chi_V=\chi_W+\chi_{V/W}$.

**Theorem 3.6.2.** (i) Characters of (distinct) irreducible finite dimensional representations of $A$ are linearly independent.

(ii) If $A$ is a finite dimensional semisimple algebra, then these characters form a basis of $(A/[A,A])^*$.

**Proof.** (i) If $V_1,\ldots,V_r$ are nonisomorphic irreducible finite dimensional representations of $A$, then the map

$$
\rho_{V_1}\oplus\cdots\oplus\rho_{V_r}:A\to\operatorname{End}V_1\oplus\cdots\oplus\operatorname{End}V_r
$$

is surjective by the density theorem, so $\chi_{V_1},\ldots,\chi_{V_r}$ are linearly independent. (Indeed, if $\sum\lambda_i\chi_{V_i}(a)=0$ for all $a\in A$, then $\sum\lambda_i\operatorname{Tr}(M_i)=0$ for all $M_i\in\operatorname{End}_k V_i$. But each $\operatorname{Tr}(M_i)$ can range independently over $k$, so it must be that $\lambda_1=\cdots=\lambda_r=0$.)

(ii) First we prove that $[\operatorname{Mat}_d(k),\operatorname{Mat}_d(k)]=\mathfrak{sl}_d(k)$, the set of all matrices with trace $0$. It is clear that $[\operatorname{Mat}_d(k),\operatorname{Mat}_d(k)]\subseteq\mathfrak{sl}_d(k)$. If we denote by $E_{ij}$ the matrix with $1$ in the $i$th row of the $j$th column and $0$’s everywhere else, we have $[E_{ij},E_{jm}]=E_{im}$ for $i\ne m$ and $[E_{i,i+1},E_{i+1,i}]=E_{ii}-E_{i+1,i+1}$. Now $\{E_{im}\}\cup\{E_{ii}-E_{i+1,i+1}\}$ forms a basis in $\mathfrak{sl}_d(k)$, so indeed $[\operatorname{Mat}_d(k),\operatorname{Mat}_d(k)]=\mathfrak{sl}_d(k)$, as claimed. By semisimplicity, we can write $A=\operatorname{Mat}_{d_1}(k)\oplus\cdots\oplus\operatorname{Mat}_{d_r}(k)$. Then $[A,A]=\mathfrak{sl}_{d_1}(k)\oplus\cdots\oplus\mathfrak{sl}_{d_r}(k)$, and $A/[A,A]\cong k^r$. By Theorem 3.3.1, there are exactly $r$ irreducible representations of $A$ (isomorphic to $k^{d_1},\ldots,k^{d_r}$, respectively) and therefore $r$ linearly independent characters on the $r$-dimensional vector space $A/[A,A]$. Thus, the characters form a basis. $\square$

<span class="original-page-anchor" id="pdf-page-58" aria-hidden="true"></span>

## 3.7. The Jordan–Hölder theorem

We will now state and prove two important theorems about representations of finite dimensional algebras—the Jordan–Hölder theorem and the Krull–Schmidt theorem.

**Theorem 3.7.1 (Jordan–Hölder theorem).** Let $V$ be a finite dimensional representation of $A$, and let $0=V_0\subset V_1\subset\cdots\subset V_n=V$, $0=V'_0\subset\cdots\subset V'_m=V$ be filtrations of $V$, such that the representations $W_i:=V_i/V_{i-1}$ and $W'_i:=V'_i/V'_{i-1}$ are irreducible for all $i$. Then $n=m$, and there exists a permutation $\sigma$ of $1,\ldots,n$ such that $W_{\sigma(i)}$ is isomorphic to $W'_i$.

**Proof.** *First proof* (for $k$ of characteristic zero). The character of $V$ obviously equals the sum of characters of $W_i$ and also the sum of characters of $W'_i$. But by Theorem 3.6.2, the characters of irreducible representations are linearly independent, so the multiplicity of every irreducible representation $W$ of $A$ among $W_i$ and among $W'_i$ is the same. This implies the theorem.[^rt-58-2]

*Second proof* (general). The proof is by induction on $\dim V$. The base of induction is clear, so let us prove the induction step. If $W_1=W'_1$ (as subspaces), we are done, since by the induction assumption the theorem holds for $V/W_1$. So assume $W_1\ne W'_1$. In this case $W_1\cap W'_1=0$ (as $W_1,W'_1$ are irreducible), so we have an embedding $f:W_1\oplus W'_1\to V$. Let $U=V/(W_1\oplus W'_1)$, and let $0=U_0\subset U_1\subset\cdots\subset U_p=U$ be a filtration of $U$ with simple quotients $Z_i=U_i/U_{i-1}$ (it exists by Lemma 3.4.2). Then we see the following:

1) $V/W_1$ has a filtration with successive quotients $W'_1,Z_1,\ldots,Z_p$ and another filtration with successive quotients $W_2,\ldots,W_n$.

2) $V/W'_1$ has a filtration with successive quotients $W_1,Z_1,\ldots,Z_p$ and another filtration with successive quotients $W'_2,\ldots,W'_n$.

<span class="original-page-anchor" id="pdf-page-59" aria-hidden="true"></span>

By the induction assumption, this means that the collection of irreducible representations with multiplicities $W_1,W'_1,Z_1,\ldots,Z_p$ coincides on one hand with $W_1,\ldots,W_n$ and on the other hand with $W'_1,\ldots,W'_m$. We are done. $\square$

The Jordan–Hölder theorem shows that the number $n$ of terms in a filtration of $V$ with irreducible successive quotients does not depend on the choice of a filtration and depends only on $V$. This number is called the **length** of $V$. It is easy to see that $n$ is also the maximal length of a filtration of $V$ in which all the inclusions are strict.

The sequence of the irreducible representations $W_1,\ldots,W_n$ enumerated in the order they appear from some filtration of $V$ as successive quotients is called a **Jordan–Hölder series** of $V$.

## 3.8. The Krull–Schmidt theorem

**Theorem 3.8.1 (Krull–Schmidt theorem).** Any finite dimensional representation of $A$ can be uniquely (up to an isomorphism and the order of summands) decomposed into a direct sum of indecomposable representations.

**Proof.** It is clear that a decomposition of $V$ into a direct sum of indecomposable representations exists, so we just need to prove uniqueness. We will prove it by induction on $\dim V$. Let $V=V_1\oplus\cdots\oplus V_m=V'_1\oplus\cdots\oplus V'_n$. Let $i_s:V_s\to V$, $i'_s:V'_s\to V$, $p_s:V\to V_s$, $p'_s:V\to V'_s$ be the natural maps associated with these decompositions. Let $\theta_s=p_1i'_sp'_si_1:V_1\to V_1$. We have $\sum_{s=1}^n\theta_s=1$. Now we need the following lemma.

**Lemma 3.8.2.** Let $W$ be a finite dimensional indecomposable representation of $A$. Then:

(i) Any homomorphism $\theta:W\to W$ is either an isomorphism or nilpotent.

(ii) If $\theta_s:W\to W$, $s=1,\ldots,n$, are nilpotent homomorphisms, then so is $\theta:=\theta_1+\cdots+\theta_n$.

<span class="original-page-anchor" id="pdf-page-60" aria-hidden="true"></span>

**Proof.** (i) Generalized eigenspaces of $\theta$ are subrepresentations of $W$, and $W$ is their direct sum. Thus, $\theta$ can have only one eigenvalue $\lambda$. If $\lambda$ is zero, $\theta$ is nilpotent; otherwise it is an isomorphism.

(ii) The proof is by induction in $n$. The base is clear. To make the induction step ($n-1$ to $n$), assume that $\theta$ is not nilpotent. Then by (i), $\theta$ is an isomorphism, so $\sum_{i=0}^n\theta^{-1}\theta_i=1$. The morphisms $\theta^{-1}\theta_i$ are not isomorphisms, so they are nilpotent. Thus $1-\theta^{-1}\theta_n=\theta^{-1}\theta_1+\cdots+\theta^{-1}\theta_{n-1}$ is an isomorphism, which is a contradiction to the induction assumption. $\square$

By the lemma, we find that for some $s$, $\theta_s$ must be an isomorphism; we may assume that $s=1$. In this case, $V'_1=\operatorname{Im}(p'_1i_1)\oplus\operatorname{Ker}(p_1i'_1)$, so since $V'_1$ is indecomposable, we get that $f:=p'_1i_1:V_1\to V'_1$ and $g:=p_1i'_1:V'_1\to V_1$ are isomorphisms.

Let $B=\bigoplus_{j>1}V_j$, $B'=\bigoplus_{j>1}V'_j$; then we have $V=V_1\oplus B=V'_1\oplus B'$. Consider the map $h:B\to B'$ defined as a composition of the natural maps $B\to V\to B'$ attached to these decompositions. We claim that $h$ is an isomorphism. To show this, it suffices to show that $\operatorname{Ker}h=0$ (as $h$ is a map between spaces of the same dimension). Assume that $v\in\operatorname{Ker}h\subset B$. Then $v\in V'_1$. On the other hand, the projection of $v$ to $V_1$ is zero, so $gv=0$. Since $g$ is an isomorphism, we get $v=0$, as desired.

Now by the induction assumption, $m=n$, and $V_j\cong V'_{\sigma(j)}$ for some permutation $\sigma$ of $2,\ldots,n$. The theorem is proved. $\square$

**Problem 3.8.3.** The above proof of Lemma 3.8.2 uses the condition that $k$ is an algebraically closed field. Prove Lemma 3.8.2 (and hence the Krull–Schmidt theorem) without this condition.

**Problem 3.8.4.** (i) Let $V,W$ be finite dimensional representations of an algebra $A$ over a (not necessarily algebraically closed) field $K$. Let $L$ be a field extension of $K$. Suppose that $V\otimes_K L$ is isomorphic to $W\otimes_K L$ as a module over the $L$-algebra $A\otimes_K L$. Show that $V$ and $W$ are isomorphic as $A$-modules.

Hint: Reduce to the case of finitely generated, then finite extension, of some degree $n$. Then regard $V\otimes_K L$ and $W\otimes_K L$ as <span class="original-page-anchor" id="pdf-page-61" aria-hidden="true"></span>$A$-modules, and show that they are isomorphic to $V^n$ and $W^n$, respectively. Deduce that $V^n$ is isomorphic to $W^n$, and use the Krull–Schmidt theorem (valid over any field by Problem 3.8.3) to deduce that $V$ is isomorphic to $W$.

(ii) (The Noether–Deuring theorem) In the setting of (i), suppose that $V\otimes_K L$ is a direct summand in $W\otimes_K L$ (i.e., $W\otimes_K L\cong V\otimes_K L\oplus Y$, where $Y$ is a module over $A\otimes_K L$). Show that $V$ is a direct summand in $W$.

**Problem 3.8.5.** Let $A$ be the algebra of real-valued continuous functions on $\mathbb{R}$ which are periodic with period $1$. Let $M$ be the $A$-module of continuous functions $f$ on $\mathbb{R}$ which are antiperiodic with period $1$, i.e., $f(x+1)=-f(x)$.

(i) Show that $A$ and $M$ are indecomposable $A$-modules.

(ii) Show that $A$ is not isomorphic to $M$ but $A\oplus A$ is isomorphic to $M\oplus M$.

**Remark 3.8.6.** Thus, we see that, in general, the Krull–Schmidt theorem fails for infinite dimensional modules. However, it still holds for modules of **finite length**, i.e., modules $M$ such that any filtration of $M$ has length bounded above by a certain constant $l=l(M)$.

## 3.9. Problems

**Problem 3.9.1. Extensions of representations.** Let $A$ be an algebra, and let $V,W$ be a pair of representations of $A$. We would like to classify representations $U$ of $A$ such that $V$ is a subrepresentation of $U$ and $U/V=W$. Of course, there is an obvious example $U=V\oplus W$, but are there any others?

Suppose we have a representation $U$ as above. As a vector space, it can be (nonuniquely) identified with $V\oplus W$, so that for any $a\in A$ the corresponding operator $\rho_U(a)$ has block triangular form

$$
\rho_U(a)=\begin{pmatrix}\rho_V(a)&f(a)\\0&\rho_W(a)\end{pmatrix},
$$

where $f:A\to\operatorname{Hom}_k(W,V)$ is a linear map.

(a) What is the necessary and sufficient condition on $f(a)$ under which $\rho_U(a)$ is a representation? Maps $f$ satisfying this condition are <span class="original-page-anchor" id="pdf-page-62" aria-hidden="true"></span>called **1-cocycles** (of $A$ with coefficients in $\operatorname{Hom}_k(W,V)$). They form a vector space denoted by $Z^1(W,V)$.

(b) Let $X:W\to V$ be a linear map. The coboundary of $X$, $dX$, is defined to be the function $A\to\operatorname{Hom}_k(W,V)$ given by $dX(a)=\rho_V(a)X-X\rho_W(a)$. Show that $dX$ is a cocycle which vanishes if and only if $X$ is a homomorphism of representations. Thus coboundaries form a subspace $B^1(W,V)\subset Z^1(W,V)$, which is isomorphic to $\operatorname{Hom}_k(W,V)/\operatorname{Hom}_A(W,V)$. The quotient $Z^1(W,V)/B^1(W,V)$ is denoted by $\operatorname{Ext}^1(W,V)$.

(c) Show that if $f,f'\in Z^1(W,V)$ and $f-f'\in B^1(W,V)$, then the corresponding extensions $U,U'$ are isomorphic representations of $A$. Conversely, if $\phi:U\to U'$ is an isomorphism such that

$$
\phi(a)=\begin{pmatrix}1_V&*\\0&1_W\end{pmatrix},
$$

then $f-f'\in B^1(V,W)$. Thus, the space $\operatorname{Ext}^1(W,V)$ “classifies” extensions of $W$ by $V$.

(d) Assume that $W,V$ are finite dimensional irreducible representations of $A$. For any $f\in\operatorname{Ext}^1(W,V)$, let $U_f$ be the corresponding extension. Show that $U_f$ is isomorphic to $U_{f'}$ as representations if and only if $f$ and $f'$ are proportional. Thus isomorphism classes (as representations) of nontrivial extensions of $W$ by $V$ (i.e., those not isomorphic to $W\oplus V$) are parametrized by the projective space $\mathbb{P}\operatorname{Ext}^1(W,V)$. In particular, every extension is trivial if and only if $\operatorname{Ext}^1(W,V)=0$.

**Problem 3.9.2.** (a) Let $A=\mathbb{C}[x_1,\ldots,x_n]$, and let $V_a,V_b$ be $1$-dimensional representations in which the elements $x_i$ act by $a_i$ and $b_i$, respectively ($a_i,b_i\in\mathbb{C}$). Find $\operatorname{Ext}^1(V_a,V_b)$ and classify $2$-dimensional representations of $A$.

(b) Let $B$ be the algebra over $\mathbb{C}$ generated by $x_1,\ldots,x_n$ with the defining relations $x_ix_j=0$ for all $i,j$. Show that for $n>1$ the algebra $B$ has infinitely many nonisomorphic indecomposable representations.

**Problem 3.9.3.** Let $Q$ be a quiver without oriented cycles, and let $P_Q$ be the path algebra of $Q$. Find irreducible representations of $P_Q$ and compute $\operatorname{Ext}^1$ between them. Classify $2$-dimensional representations of $P_Q$.

<span class="original-page-anchor" id="pdf-page-63" aria-hidden="true"></span>

**Problem 3.9.4.** Let $A$ be an algebra, and let $V$ be a representation of $A$. Let $\rho:A\to\operatorname{End}V$. A **formal deformation** of $V$ is a formal series

$$
\widetilde{\rho}=\rho_0+t\rho_1+\cdots+t^n\rho_n+\cdots,
$$

where $\rho_i:A\to\operatorname{End}(V)$ are linear maps, $\rho_0=\rho$, and $\widetilde{\rho}(ab)=\widetilde{\rho}(a)\widetilde{\rho}(b)$.

If $b(t)=1+b_1t+b_2t^2+\cdots$, where $b_i\in\operatorname{End}(V)$, and $\widetilde{\rho}$ is a formal deformation of $\rho$, then $b\widetilde{\rho}b^{-1}$ is also a deformation of $\rho$, which is said to be isomorphic to $\widetilde{\rho}$.

(a) Show that if $\operatorname{Ext}^1(V,V)=0$, then any deformation of $\rho$ is trivial, i.e., isomorphic to $\rho$.

(b) Is the converse to (a) true? (Consider the algebra of dual numbers $A=k[x]/x^2$.)

**Problem 3.9.5. The Clifford algebra.** Let $V$ be a finite dimensional complex vector space equipped with a symmetric bilinear form $(\ ,\ )$. The **Clifford algebra** $\operatorname{Cl}(V)$ is the quotient of the tensor algebra $TV$ by the ideal generated by the elements $v\otimes v-(v,v)1$, $v\in V$. More explicitly, if $x_i$, $1\le i\le N$, is a basis of $V$ and $(x_i,x_j)=a_{ij}$ then $\operatorname{Cl}(V)$ is generated by $x_i$ with defining relations

$$
x_ix_j+x_jx_i=2a_{ij},\qquad x_i^2=a_{ii}.
$$

Thus, if $(\ ,\ )=0$, $\operatorname{Cl}(V)=\wedge V$.

(i) Show that if $(\ ,\ )$ is nondegenerate, then $\operatorname{Cl}(V)$ is semisimple and has one irreducible representation of dimension $2^n$ if $\dim V=2n$ (so in this case $\operatorname{Cl}(V)$ is a matrix algebra) and two such representations if $\dim(V)=2n+1$ (i.e., in this case $\operatorname{Cl}(V)$ is a direct sum of two matrix algebras).

Hint: In the even case, pick a basis $a_1,\ldots,a_n,b_1,\ldots,b_n$ of $V$ in which $(a_i,a_j)=(b_i,b_j)=0$, $(a_i,b_j)=\delta_{ij}/2$, and construct a representation of $\operatorname{Cl}(V)$ on $S:=\wedge(a_1,\ldots,a_n)$ in which $b_i$ acts as “differentiation” with respect to $a_i$. Show that $S$ is irreducible. In the odd case the situation is similar, except there should be an additional basis vector $c$ such that $(c,a_i)=(c,b_i)=0$, $(c,c)=1$ and the action of $c$ on $S$ may be defined either by $(-1)^{\mathrm{degree}}$ or by $(-1)^{\mathrm{degree}+1}$, giving two representations $S_+,S_-$ (why are they nonisomorphic?).

<span class="original-page-anchor" id="pdf-page-64" aria-hidden="true"></span>

Show that there is no other irreducible representations by finding a spanning set of $\operatorname{Cl}(V)$ with $2^{\dim V}$ elements.

(ii) Show that $\operatorname{Cl}(V)$ is semisimple if and only if $(\ ,\ )$ is nondegenerate. If $(\ ,\ )$ is degenerate, what is $\operatorname{Cl}(V)/\operatorname{Rad}(\operatorname{Cl}(V))$?

## 3.10. Representations of tensor products

Let $A,B$ be algebras. Then $A\otimes B$ is also an algebra, with multiplication $(a_1\otimes b_1)(a_2\otimes b_2)=a_1a_2\otimes b_1b_2$.

**Exercise 3.10.1.** Show that $\operatorname{Mat}_m(k)\otimes\operatorname{Mat}_n(k)\cong\operatorname{Mat}_{mn}(k)$.

The following theorem describes irreducible finite dimensional representations of $A\otimes B$ in terms of irreducible finite dimensional representations of $A$ and those of $B$.

**Theorem 3.10.2.** (i) Let $V$ be an irreducible finite dimensional representation of $A$ and let $W$ be an irreducible finite dimensional representation of $B$. Then $V\otimes W$ is an irreducible representation of $A\otimes B$.

(ii) Any irreducible finite dimensional representation $M$ of $A\otimes B$ has the form (i) for unique $V$ and $W$.

**Remark 3.10.3.** Part (ii) of the theorem typically fails for infinite dimensional representations; e.g. it fails when $A$ is the Weyl algebra in characteristic zero. Part (i) may also fail. E.g. let $A=B=V=W=\mathbb{C}(x)$. Then (i) fails, as $A\otimes B$ is not a field.

**Proof.** (i) By the density theorem, the maps $A\to\operatorname{End}V$ and $B\to\operatorname{End}W$ are surjective. Therefore, the map $A\otimes B\to\operatorname{End}V\otimes\operatorname{End}W=\operatorname{End}(V\otimes W)$ is surjective. Thus, $V\otimes W$ is irreducible.

(ii) First we show the existence of $V$ and $W$. Let $A',B'$ be the images of $A,B$ in $\operatorname{End}M$. Then $A',B'$ are finite dimensional algebras, and $M$ is a representation of $A'\otimes B'$, so we may assume without loss of generality that $A$ and $B$ are finite dimensional.

In this case, we claim that

$$
\operatorname{Rad}(A\otimes B)=\operatorname{Rad}(A)\otimes B+A\otimes\operatorname{Rad}(B).
$$

<span class="original-page-anchor" id="pdf-page-65" aria-hidden="true"></span>

Indeed, denote the latter by $J$. Then $J$ is a nilpotent ideal in $A\otimes B$, as $\operatorname{Rad}(A)$ and $\operatorname{Rad}(B)$ are nilpotent. On the other hand, $(A\otimes B)/J=(A/\operatorname{Rad}(A))\otimes(B/\operatorname{Rad}(B))$, which is a product of two semisimple algebras, hence semisimple. This implies $J\supset\operatorname{Rad}(A\otimes B)$. Altogether, by Proposition 3.5.3, we see that $J=\operatorname{Rad}(A\otimes B)$, proving the claim.

Thus, we see that

$$
(A\otimes B)/\operatorname{Rad}(A\otimes B)=A/\operatorname{Rad}(A)\otimes B/\operatorname{Rad}(B).
$$

Now, $M$ is an irreducible representation of $(A\otimes B)/\operatorname{Rad}(A\otimes B)$, so it is clearly of the form $M=V\otimes W$, where $V$ is an irreducible representation of $A/\operatorname{Rad}(A)$ and $W$ is an irreducible representation of $B/\operatorname{Rad}(B)$. Also, $V,W$ are uniquely determined by $M$ (as all of the algebras involved are direct sums of matrix algebras). $\square$

[^rt-50-1]: Another proof of the existence of $P$, which does not use the finite dimensionality of $V$, is by induction in $n$. Namely, if $W$ itself is not irreducible, let $K$ be the kernel of the projection of $W$ to the first summand $V_1$. Then $K$ is a subrepresentation of $(n_1-1)V_1\oplus\cdots\oplus n_mV_m$, which is nonzero since $W$ is not irreducible, so $K$ contains an irreducible subrepresentation by the induction assumption.

[^rt-58-2]: This proof does not work in characteristic $p$ because it only implies that the multiplicities of $W_i$ and $W'_i$ are the same modulo $p$, which is not sufficient. In fact, the character of the representation $pV$, where $V$ is any representation, is zero.
