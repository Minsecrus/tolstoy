---
title: "Chapter XVII: Semisimplicity"
description: "Serge Lang《Algebra》English。"
pageClass: algebra-reading
prev: {"text":"Chapter XVI: The Tensor Product","link":"/library/volume-86/original-chapter-016"}
next: {"text":"Chapter XVIII: Representations of Finite Groups","link":"/library/volume-86/original-chapter-018"}
---

# Chapter XVII: Semisimplicity

<span class="original-page-anchor" id="pdf-page-650" aria-hidden="true"></span>

In many applications, a module decomposes as a direct sum of simple submodules, and then one can develop a fairly precise structure theory, both under general assumptions, and particular applications. This chapter is devoted to those results which can be proved in general. In the next chapter, we consider those additional results which can be proved in a classical and important special case.

I have more or less followed Bourbaki in the proof of Jacobson's density theorem.

## §1. MATRICES AND LINEAR MAPS OVER NON-COMMUTATIVE RINGS

In Chapter XIII, we considered exclusively matrices over commutative rings. For our present purposes, it is necessary to consider a more general situation.

Let $K$ be a ring. We define a matrix $(\varphi_{ij})$ with coefficients in $K$ just as we did for commutative rings. The product of matrices is defined by the same formula. Then we again have associativity and distributivity, whenever the size of the matrices involved in the operations makes the operations defined. In particular, the square $n\times n$ matrices over $K$ form a ring, again denoted by $\operatorname{Mat}_n(K)$. We have a ring-homomorphism

$$
K\to\operatorname{Mat}_n(K)
$$

on the diagonal.

<span class="original-page-anchor" id="pdf-page-651" aria-hidden="true"></span>

By a **division ring** we shall mean a ring with $1\ne0$, and such that every non-zero element has a multiplicative inverse.

If $K$ is a division ring, then every non-zero $K$-module has a basis, and the cardinalities of two bases are equal. The proof is the same as in the commutative case; we never needed commutativity in the arguments. This cardinality is again called the **dimension** of the module over $K$, and a module over a division ring is called a **vector space**.

We can associate a matrix with linear maps, depending on the choice of a finite basis, just as in the commutative case. However, we shall consider a somewhat different situation which we want to apply to semisimple modules.

Let $R$ be a ring, and let

$$
E=E_1\oplus\cdots\oplus E_n,\qquad F=F_1\oplus\cdots\oplus F_m
$$

be $R$-modules, expressed as direct sums of $R$-submodules. We wish to describe the most general $R$-homomorphism of $E$ into $F$.

Suppose first $F=F_1$ has one component. Let

$$
\varphi:E_1\oplus\cdots\oplus E_n\to F
$$

be a homomorphism. Let $\varphi_j:E_j\to F$ be the restriction of $\varphi$ to the factor $E_j$. Every element $x\in E$ has a unique expression $x=x_1+\cdots+x_n$, with $x_j\in E_j$. We may therefore associate with $x$ the column vector $X={}^t(x_1,\ldots,x_n)$, whose components are in $E_1,\ldots,E_n$ respectively. We can associate with $\varphi$ the row vector $(\varphi_1,\ldots,\varphi_n)$, $\varphi_j\in\operatorname{Hom}_R(E_j,F)$, and the effect of $\varphi$ on the element $x$ of $E$ is described by matrix multiplication, of the row vector times the column vector.

More generally, consider a homomorphism

$$
\varphi:E_1\oplus\cdots\oplus E_n\to F_1\oplus\cdots\oplus F_m.
$$

Let $\pi_i:F_1\oplus\cdots\oplus F_m\to F_i$ be the projection on the $i$-th factor. Then we can apply our previous remarks to $\pi_i\circ\varphi$, for each $i$. In this way, we see that there exist unique elements $\varphi_{ij}\in\operatorname{Hom}_R(E_j,F_i)$, such that $\varphi$ has a matrix representation

$$
M(\varphi)=\begin{pmatrix}\varphi_{11}&\cdots&\varphi_{1n}\\\vdots&&\vdots\\\varphi_{m1}&\cdots&\varphi_{mn}\end{pmatrix}
$$

whose effect on an element $x$ is given by matrix multiplication, namely

$$
\begin{pmatrix}\varphi_{11}&\cdots&\varphi_{1n}\\\vdots&&\vdots\\\varphi_{m1}&\cdots&\varphi_{mn}\end{pmatrix}\begin{pmatrix}x_1\\\vdots\\x_n\end{pmatrix}.
$$

<span class="original-page-anchor" id="pdf-page-652" aria-hidden="true"></span>

Conversely, given a matrix $(\varphi_{ij})$ with $\varphi_{ij}\in\operatorname{Hom}_R(E_j,F_i)$, we can define an element of $\operatorname{Hom}_R(E,F)$ by means of this matrix. We have an additive group-isomorphism between $\operatorname{Hom}_R(E,F)$ and this group of matrices.

*In particular, let $E$ be a fixed $R$-module, and let $K=\operatorname{End}_R(E)$. Then we have a ring-isomorphism*

$$
\operatorname{End}_R(E^{(n)})\to\operatorname{Mat}_n(K)
$$

*which to each $\varphi\in\operatorname{End}_R(E^{(n)})$ associates the matrix*

$$
\begin{pmatrix}\varphi_{11}&\cdots&\varphi_{1n}\\\vdots&&\vdots\\\varphi_{n1}&\cdots&\varphi_{nn}\end{pmatrix}
$$

*determined as before, and operating on the left on column vectors of $E^{(n)}$, with components in $E$.*

**Remark.** Let $E$ be a $1$-dimensional vector space over a division ring $D$, and let $\{v\}$ be a basis. For each $a\in D$, there exists a unique $D$-linear map $f_a:E\to E$ such that $f_a(v)=av$. Then we have the rule

$$
f_af_b=f_{ba}.
$$

Thus when we associate a matrix with a linear map, depending on a basis, the multiplication gets twisted. Nevertheless, the statement we just made preceding this remark is correct!! The point is that we took the $\varphi_{ij}$ in $\operatorname{End}_R(E)$, and not in $D$, in the special case that $R=D$. Thus $K$ is not isomorphic to $D$ (in the non-commutative case), but anti-isomorphic. This is the only point of difference of the formal elementary theory of linear maps in the commutative or non-commutative case.

We recall that an $R$-module $E$ is said to be **simple** if it is $\ne0$ and if it has no submodule other than $0$ or $E$.

**Proposition 1.1. Schur's Lemma.** *Let $E,F$ be simple $R$-modules. Every non-zero homomorphism of $E$ into $F$ is an isomorphism. The ring $\operatorname{End}_R(E)$ is a division ring.*

*Proof.* Let $f:E\to F$ be a non-zero homomorphism. Its image and kernel are submodules, hence $\operatorname{Ker}f=0$ and $\operatorname{Im}f=F$. Hence $f$ is an isomorphism. If $E=F$, then $f$ has an inverse, as desired.

The next proposition describes completely the ring of endomorphisms of a direct sum of simple modules.

**Proposition 1.2.** *Let $E=E_1^{(n_1)}\oplus\cdots\oplus E_r^{(n_r)}$ be a direct sum of simple modules, the $E_i$ being non-isomorphic, and each $E_i$ being repeated $n_i$ times in* <span class="original-page-anchor" id="pdf-page-653" aria-hidden="true"></span>*the sum. Then, up to a permutation, $E_1,\ldots,E_r$ are uniquely determined up to isomorphisms, and the multiplicities $n_1,\ldots,n_r$ are uniquely determined. The ring $\operatorname{End}_R(E)$ is isomorphic to a ring of matrices, of type*

![Block diagonal endomorphism matrix](/library/volume-86/diagrams/pdf-0653-block-endomorphisms.png)

*where $M_i$ is an $n_i\times n_i$ matrix over $\operatorname{End}_R(E_i)$. (The isomorphism is the one with respect to our direct sum decomposition.)*

*Proof.* The last statement follows from our previous considerations, taking into account Proposition 1.1.

Suppose now that we have two $R$-modules, with direct sum decompositions into simple submodules, and an isomorphism

$$
E_1^{(n_1)}\oplus\cdots\oplus E_r^{(n_r)}\to F_1^{(m_1)}\oplus\cdots\oplus F_s^{(m_s)},
$$

such that the $E_i$ are non-isomorphic, and the $F_j$ are non-isomorphic. From Proposition 1.1, we conclude that each $E_i$ is isomorphic to some $F_j$, and conversely. It follows that $r=s$, and that after a permutation, $E_i\approx F_i$. Furthermore, the isomorphism must induce an isomorphism

$$
E_i^{(n_i)}\to F_i^{(m_i)}
$$

for each $i$. Since $E_i\approx F_i$, we may assume without loss of generality that in fact $E_i=F_i$. Thus we are reduced to proving: If a module is isomorphic to $E^{(n)}$ and to $E^{(m)}$, with some simple module $E$, then $n=m$. But $\operatorname{End}_R(E^{(n)})$ is isomorphic to the $n\times n$ matrix ring over the division ring $\operatorname{End}_R(E)=K$. Furthermore this isomorphism is verified at once to be an isomorphism as $K$-vector space. The dimension of the space of $n\times n$ matrices over $K$ is $n^2$. This proves that the multiplicity $n$ is uniquely determined, and proves our proposition.

When $E$ admits a (finite) direct sum decomposition of simple submodules, the number of times that a simple module of a given isomorphism class occurs in a decomposition will be called the **multiplicity** of the simple module (or of the isomorphism class of the simple module).

Furthermore, if

$$
E=E_1^{(n_1)}\oplus\cdots\oplus E_r^{(n_r)}
$$

is expressed as a sum of simple submodules, we shall call $n_1+\cdots+n_r$ the **length** of $E$. In many applications, we shall also write

$$
E=n_1E_1\oplus\cdots\oplus n_rE_r=\bigoplus_{i=1}^r n_iE_i.
$$

<span class="original-page-anchor" id="pdf-page-654" aria-hidden="true"></span>

## §2. CONDITIONS DEFINING SEMISIMPLICITY

*Let $R$ be a ring. Unless otherwise specified in this section all modules and homomorphisms will be $R$-modules and $R$-homomorphisms.*

The following conditions on a module $E$ are equivalent:

**SS 1.** $E$ is the sum of a family of simple submodules.

**SS 2.** $E$ is the direct sum of a family of simple submodules.

**SS 3.** Every submodule $F$ of $E$ is a direct summand, i.e. there exists a submodule $F'$ such that $E=F\oplus F'$.

We shall now prove that these three conditions are equivalent.

**Lemma 2.1.** *Let $E=\sum_{i\in I}E_i$ be a sum (not necessarily direct) of simple submodules. Then there exists a subset $J\subset I$ such that $E$ is the direct sum $\bigoplus_{j\in J}E_j$.*

*Proof.* Let $J$ be a maximal subset of $I$ such that the sum $\sum_{j\in J}E_j$ is direct. We contend that this sum is in fact equal to $E$. It will suffice to prove that each $E_i$ is contained in this sum. But the intersection of our sum with $E_i$ is a submodule of $E_i$, hence equal to $0$ or $E_i$. If it is equal to $0$, then $J$ is not maximal, since we can adjoin $i$ to it. Hence $E_i$ is contained in the sum, and our lemma is proved.

The lemma shows that **SS 1** implies **SS 2**. To see that **SS 2** implies **SS 3**, take a submodule $F$, and let $J$ be a maximal subset of $I$ such that the sum $F+\bigoplus_{j\in J}E_j$ is direct. The same reasoning as before shows that this sum is equal to $E$.

Finally assume **SS 3**. To show **SS 1**, we shall first prove that every non-zero submodule of $E$ contains a simple submodule. Let $v\in E$, $v\ne0$. Then by definition, $Rv$ is a principal submodule, and the kernel of the homomorphism

$$
R\to Rv
$$

is a left ideal $L\ne R$. Hence $L$ is contained in a maximal left ideal $M\ne R$ (by Zorn's lemma). Then $M/L$ is a maximal submodule of $R/L$ (unequal to $R/L$), and hence $Mv$ is a maximal submodule of $Rv$, unequal to $Rv$, corresponding to $M/L$ under the isomorphism

$$
R/L\to Rv.
$$

<span class="original-page-anchor" id="pdf-page-655" aria-hidden="true"></span>

We can write $E=Mv\oplus M'$ with some submodule $M'$. Then

$$
Rv=Mv\oplus(M'\cap Rv),
$$

because every element $x\in Rv$ can be written uniquely as a sum $x=\alpha v+x'$ with $\alpha\in M$ and $x'\in M'$, and $x'=x-\alpha v$ lies in $Rv$. Since $Mv$ is maximal in $Rv$, it follows that $M'\cap Rv$ is simple, as desired.

Let $E_0$ be the submodule of $E$ which is the sum of all simple submodules of $E$. If $E_0\ne E$, then $E=E_0\oplus F$ with $F\ne0$, and there exists a simple submodule of $F$, contradicting the definition of $E_0$. This proves that **SS 3** implies **SS 1**.

A module $E$ satisfying our three conditions is said to be **semisimple**.

**Proposition 2.2.** *Every submodule and every factor module of a semisimple module is semisimple.*

*Proof.* Let $F$ be a submodule. Let $F_0$ be the sum of all simple submodules of $F$. Write $E=F_0\oplus F'_0$. Every element $x$ of $F$ has a unique expression $x=x_0+x'_0$ with $x_0\in F_0$ and $x'_0\in F'_0$. But $x'_0=x-x_0\in F$. Hence $F$ is the direct sum

$$
F=F_0\oplus(F\cap F'_0).
$$

We must therefore have $F_0=F$, which is semisimple. As for the factor module, write $E=F\oplus F'$. Then $F'$ is a sum of its simple submodules, and the canonical map $E\to E/F$ induces an isomorphism of $F'$ onto $E/F$. Hence $E/F$ is semisimple.

## §3. THE DENSITY THEOREM

Let $E$ be a semisimple $R$-module. Let $R'=R'(E)$ be the ring $\operatorname{End}_R(E)$. Then $E$ is also a $R'$-module, the operation of $R'$ on $E$ being given by

$$
(\varphi,x)\mapsto\varphi(x)
$$

for $\varphi\in R'$ and $x\in E$. Each $\alpha\in R$ induces a $R'$-homomorphism $f_\alpha:E\to E$ by the map $f_\alpha(x)=\alpha x$. This is what is meant by the condition

$$
\varphi(\alpha x)=\alpha\varphi(x).
$$

We let $R''=R''(E)=\operatorname{End}_{R'}(E)$. We call $R'$ the **commutant** of $R$ and $R''$ the **bicommutant**. Thus we get a ring-homomorphism

$$
R\to\operatorname{End}_{R'}(E)=R''(E)=R''
$$

<span class="original-page-anchor" id="pdf-page-656" aria-hidden="true"></span>

by $\alpha\mapsto f_\alpha$. We now ask how big is the image of this ring-homomorphism. The density theorem states that it is quite big.

**Lemma 3.1.** *Let $E$ be semisimple over $R$. Let $R'=\operatorname{End}_R(E)$, $f\in\operatorname{End}_{R'}(E)$ as above. Let $x\in R$. There exists an element $\alpha\in R$ such that $\alpha x=f(x)$.*

*Proof.* Since $E$ is semisimple, we can write an $R$-direct sum

$$
E=Rx\oplus F
$$

with some submodule $F$. Let $\pi:E\to Rx$ be the projection. Then $\pi\in R'$, and hence

$$
f(x)=f(\pi x)=\pi f(x).
$$

This shows that $f(x)\in Rx$, as desired.

The density theorem generalizes the lemma by dealing with a finite number of elements of $E$ instead of just one. For the proof, we use a diagonal trick.

**Theorem 3.2. (Jacobson).** *Let $E$ be semisimple over $R$, and let $R'=\operatorname{End}_R(E)$. Let $f\in\operatorname{End}_{R'}(E)$. Let $x_1,\ldots,x_n\in E$. Then there exists an element $\alpha\in R$ such that*

$$
\alpha x_i=f(x_i)\quad\text{for}\quad i=1,\ldots,n.
$$

*If $E$ is finitely generated over $R'$, then the natural map $R\to\operatorname{End}_{R'}(E)$ is surjective.*

*Proof.* For clarity of notation, we shall first carry out the proof in case $E$ is simple. Let $f^{(n)}:E^{(n)}\to E^{(n)}$ be the product map, so that

$$
f^{(n)}(y_1,\ldots,y_n)=(f(y_1),\ldots,f(y_n)).
$$

Let $R'_n=\operatorname{End}_R(E^{(n)})$. Then $R'_n$ is none other than the ring of matrices with coefficients in $R'$. Since $f$ commutes with elements of $R'$ in its action on $E$, one sees immediately that $f^{(n)}$ is in $\operatorname{End}_{R'_n}(E^{(n)})$. By the lemma, there exists an element $\alpha\in R$ such that

$$
(\alpha x_1,\ldots,\alpha x_n)=(f(x_1),\ldots,f(x_n)),
$$

which is what we wanted to prove.

When $E$ is not simple, suppose that $E$ is equal to a finite direct sum of simple submodules $E_i$ (non-isomorphic), with multiplicities $n_i$:

$$
E=E_1^{(n_1)}\oplus\cdots\oplus E_r^{(n_r)}\qquad(E_i\not\approx E_j\quad\text{if}\quad i\ne j),
$$

then the matrices representing the ring of endomorphisms split according to blocks corresponding to the non-isomorphic simple components in our direct sum decomposition. Hence here again the argument goes through as before.

<span class="original-page-anchor" id="pdf-page-657" aria-hidden="true"></span>

The main point is that $f^{(n)}$ lies in $\operatorname{End}_{R'_n}(E^{(n)})$, and that we can apply the lemma. We add the observation that if $E$ is finitely generated over $R'$, then an element $f\in\operatorname{End}_{R'}(E)$ is determined by its value on a finite number of elements of $E$, so the asserted surjectivity $R\to\operatorname{End}_{R'}(E)$ follows at once. In the applications below, $E$ will be a finite dimensional vector space over a field $k$, and $R$ will be a $k$-algebra, so the finiteness condition is automatically satisfied.

The argument when $E$ is an infinite direct sum would be similar, but the notation is disagreeable. However, in the applications we shall never need the theorem in any case other than the case when $E$ itself is a finite direct sum of simple modules, and this is the reason why we first gave the proof in that case, and let the reader write out the formal details in the other cases, if desired.

**Corollary 3.3. (Burnside's Theorem).** *Let $E$ be a finite-dimensional vector space over an algebraically closed field $k$, and let $R$ be a subalgebra of $\operatorname{End}_k(E)$. If $E$ is a simple $R$-module, then $R=\operatorname{End}_{R'}(E)$.*

*Proof.* We contend that $\operatorname{End}_R(E)=k$. At any rate, $\operatorname{End}_R(E)$ is a division ring $R'$, containing $k$ as a subring and every element of $k$ commutes with every element of $R'$. Let $\alpha\in R'$. Then $k(\alpha)$ is a field. Furthermore, $R'$ is contained in $\operatorname{End}_k(E)$ as a $k$-subspace, and is therefore finite dimensional over $k$. Hence $k(\alpha)$ is finite over $k$, and therefore equal to $k$ since $k$ is algebraically closed. This proves that $\operatorname{End}_R(E)=k$. Let now $\{v_1,\ldots,v_n\}$ be a basis of $E$ over $k$. Let $A\in\operatorname{End}_k(E)$. According to the density theorem, there exists $\alpha\in R$ such that

$$
\alpha v_i=Av_i\quad\text{for}\quad i=1,\ldots,n.
$$

Since the effect of $A$ is determined by its effect on a basis, we conclude that $R=\operatorname{End}_k(E)$.

Corollary 3.3 is used in the following situation as in Exercise 8. Let $E$ be a finite-dimensional vector space over field $k$. Let $G$ be a submonoid of $\operatorname{GL}(E)$ (multiplicative). A **$G$-invariant** subspace $F$ of $E$ is a subspace such that $\sigma F\subset F$ for all $\sigma\in G$. We say that $E$ is **$G$-simple** if it has no $G$-invariant subspace other than $0$ and $E$ itself, and $E\ne0$. Let $R=k[G]$ be the subalgebra of $\operatorname{End}_k(E)$ generated by $G$ over $k$. Since we assumed that $G$ is a monoid, it follows that $R$ consists of linear combinations

$$
\sum a_i\sigma_i
$$

with $a_i\in k$ and $\sigma_i\in G$. Then we see that a subspace $F$ of $E$ is $G$-invariant if and only if it is $R$-invariant. Thus $E$ is $G$-simple if and only if it is simple over $R$ in the sense which we have been considering. We can then restate Burnside's theorem as he stated it:

**Corollary 3.4.** *Let $E$ be a finite dimensional vector space over an algebraically closed field $k$, and let $G$ be a (multiplicative) submonoid of $\operatorname{GL}(E)$.*

<span class="original-page-anchor" id="pdf-page-658" aria-hidden="true"></span>

*If $E$ is $G$-simple, then $k[G]=\operatorname{End}_k(E)$.*

When $k$ is not algebraically closed, then we still get some result. Quite generally, let $R$ be a ring and $E$ a simple $R$-module. We have seen that $\operatorname{End}_R(E)$ is a division ring, which we denote by $D$, and $E$ is a vector space over $D$.

Let $R$ be a ring, and $E$ any $R$-module. We shall say that $E$ is a **faithful** module if the following condition is satisfied. Given $\alpha\in R$ such that $\alpha x=0$ for all $x\in E$, we have $\alpha=0$. In the applications, $E$ is a vector space over a field $k$, and we have a ring-homomorphism of $R$ into $\operatorname{End}_k(E)$. In this way, $E$ is an $R$-module, and it is faithful if and only if this homomorphism is injective.

**Corollary 3.5. (Wedderburn's Theorem).** *Let $R$ be a ring, and $E$ a simple, faithful module over $R$. Let $D=\operatorname{End}_R(E)$, and assume that $E$ is finite dimensional over $D$. Then $R=\operatorname{End}_D(E)$.*

*Proof.* Let $\{v_1,\ldots,v_n\}$ be a basis of $E$ over $D$. Given $A\in\operatorname{End}_D(E)$, by Theorem 3.2 there exists $\alpha\in R$ such that

$$
\alpha v_i=Av_i\quad\text{for}\quad i=1,\ldots,n.
$$

Hence the map $R\to\operatorname{End}_D(E)$ is surjective. Our assumption that $E$ is faithful over $R$ implies that it is injective, and our corollary is proved.

**Example.** Let $R$ be a finite-dimensional algebra over a field $k$, and assume that $R$ has a unit element, so is a ring. If $R$ does not have any two-sided ideals other than $0$ and $R$ itself, then any nonzero module $E$ over $R$ is faithful, because the kernel of the homomorphism

$$
R\to\operatorname{End}_k(E)
$$

is a two-sided ideal $\ne R$. If $E$ is simple, then $E$ is finite dimensional over $k$. Then $D$ is a finite-dimensional division algebra over $k$. Wedderburn's theorem gives a representation of $R$ as the ring of $D$-endomorphisms of $E$.

Under the assumption that $R$ is finite dimensional, one can find a simple module simply by taking a minimal left ideal $\ne0$. Such an ideal exists merely by taking a left ideal of minimal non-zero dimension over $k$. An even shorter proof of Wedderburn's theorem will be given below (Rieffel's theorem) in this case.

**Corollary 3.6.** *Let $R$ be a ring, finite dimensional algebra over a field $k$ which is algebraically closed. Let $V$ be a finite dimensional vector space over $k$, with a simple faithful representation $\rho:R\to\operatorname{End}_k(V)$. Then $\rho$ is an isomorphism, in other words, $R\approx\operatorname{Mat}_n(k)$.*

*Proof.* We apply Corollary 3.5, noting that $D$ is finite dimensional over $k$. Given $\alpha\in D$, we note that $k(\alpha)$ is a commutative subfield of $D$, whence $k(\alpha)=k$ by assumption that $k$ is algebraically closed, and the corollary follows.

<span class="original-page-anchor" id="pdf-page-659" aria-hidden="true"></span>

**Note.** The corollary applies to simple rings, which will be defined below.

Suppose next that $V_1,\ldots,V_m$ are finite dimensional vector spaces over a field $k$, and that $R$ is a $k$-algebra with representations

$$
R\to\operatorname{End}_k(V_i),\quad i=1,\ldots,m,
$$

so $V_i$ is an $R$-module. If we let

$$
E=V_1\oplus\cdots\oplus V_m,
$$

then $E$ is finite over $R'(E)$, so we get the following consequence of Jacobson's density theorem.

**Theorem 3.7. Existence of projection operators.** *Let $k$ be a field, $R$ a $k$-algebra, and $V_1,\ldots,V_m$ finite dimensional $k$-spaces which are also simple $R$-modules, and such that $V_i$ is not $R$-isomorphic to $V_j$ for $i\ne j$. Then there exist elements $e_i\in R$ such that $e_i$ acts as the identity on $V_i$ and $e_iV_j=0$ if $j\ne i$.*

*Proof.* We observe that the projection $f_i$ from the direct sum $E$ to the $i$-th factor is in $\operatorname{End}_{R'}(E)$, because if $\varphi\in R'$ then $\varphi(V_j)\subset V_j$ for all $j$. We may therefore apply the density theorem to conclude the proof.

**Corollary 3.8. (Bourbaki).** *Let $k$ be a field of characteristic $0$. Let $R$ be a $k$-algebra, and let $E,F$ be semisimple $R$-modules, finite dimensional over $k$. For each $\alpha\in R$, let $\alpha_E,\alpha_F$ be the corresponding $k$-endomorphisms on $E$ and $F$ respectively. Suppose that the traces are equal; that is,*

$$
\operatorname{tr}(\alpha_E)=\operatorname{tr}(\alpha_F)\quad\text{for all }\alpha\in R.
$$

*Then $E$ is isomorphic to $F$ as $R$-module.*

*Proof.* Each of $E$ and $F$ is isomorphic to a finite direct sum of simple $R$-modules, with certain multiplicities. Let $V$ be a simple $R$-module, and suppose

$$
\begin{aligned}
E&=V^{(n)}\oplus\text{direct summands not isomorphic to }V\\
F&=V^{(m)}\oplus\text{direct summands not isomorphic to }V.
\end{aligned}
$$

It will suffice to prove that $m=n$. Let $e_V$ be the element of $R$ found in Theorem 3.7 such that $e_V$ acts as the identity on $V$, and is $0$ on the other direct summands of $E$ and $F$. Then

$$
\operatorname{tr}(e_E)=n\dim_k(V)\qquad\text{and}\qquad\operatorname{tr}(e_F)=m\dim_k(V).
$$

Since the traces are equal by assumption, it follows that $m=n$, thus concluding the proof. Note that the characteristic $0$ is used here, because the values of the trace are in $k$.

**Example.** In the language of representations, suppose $G$ is a monoid, and <span class="original-page-anchor" id="pdf-page-660" aria-hidden="true"></span>we have two semisimple representations into finite dimensional $k$-spaces

$$
\rho:G\to\operatorname{End}_k(E)\qquad\text{and}\qquad\rho':G\to\operatorname{End}_k(F)
$$

(so $\rho$ and $\rho'$ map $G$ into the multiplicative monoid of $\operatorname{End}_k$). Assume that $\operatorname{tr}\rho(\sigma)=\operatorname{tr}\rho'(\sigma)$ for all $\sigma\in G$. Then $\rho$ and $\rho'$ are isomorphic. Indeed, we let $R=k[G]$, so that $\rho$ and $\rho'$ extend to representations of $R$. By linearity, one has that $\operatorname{tr}\rho(\alpha)=\operatorname{tr}\rho'(\alpha)$ for all $\alpha\in R$, so one can apply Corollary 3.8.

## §4. SEMISIMPLE RINGS

A ring $R$ is called **semisimple** if $1\ne0$, and if $R$ is semisimple as a left module over itself.

**Proposition 4.1.** *If $R$ is semisimple, then every $R$-module is semisimple.*

*Proof.* An $R$-module is a factor module of a free module, and a free module is a direct sum of $R$ with itself a certain number of times. We can apply Proposition 2.2 to conclude the proof.

**Examples.** 1) Let $k$ be a field and let $R=\operatorname{Mat}_n(k)$ be the algebra of $n\times n$ matrices over $k$. Then $R$ is semisimple, and actually simple, as we shall define and prove in §5, Theorem 5.5.

2) Let $G$ be a finite group and suppose that the characteristic of $k$ does not divide $\#(G)$. Then the group ring $k[G]$ is semisimple, as we shall prove in Chapter XVIII, Theorem 1.2.

3) The Clifford algebras $C_n$ over the real numbers are semisimple. See Exercise 19 of Chapter XIX.

A left ideal of $R$ is an $R$-module, and is thus called simple if it is simple as a module. Two ideals $L,L'$ are called isomorphic if they are isomorphic as modules.

We shall now decompose $R$ as a sum of its simple left ideals, and thereby get a structure theorem for $R$.

Let $\{L_i\}_{i\in I}$ be a family of simple left ideals, no two of which are isomorphic, and such that each simple left ideal is isomorphic to one of them. We say that this family is a family of representatives for the isomorphism classes of simple left ideals.

**Lemma 4.2.** *Let $L$ be a simple left ideal, and let $E$ be a simple $R$-module. If $L$ is not isomorphic to $E$, then $LE=0$.*

*Proof.* We have $RLE=LE$, and $LE$ is a submodule of $E$, hence equal to <span class="original-page-anchor" id="pdf-page-661" aria-hidden="true"></span>$0$ or $E$. Suppose $LE=E$. Let $y\in E$ be such that

$$
Ly\ne0.
$$

Since $Ly$ is a submodule of $E$, it follows that $Ly=E$. The map $\alpha\mapsto\alpha y$ of $L$ into $E$ is a homomorphism of $L$ into $E$, which is surjective, and hence nonzero. Since $L$ is simple, this homomorphism is an isomorphism.

Let

$$
R_i=\sum_{L\approx L_i}L
$$

be the sum of all simple left ideals isomorphic to $L_i$. From the lemma, we conclude that $R_iR_j=0$ if $i\ne j$. This will be used constantly in what follows. We note that $R_i$ is a left ideal, and that $R$ is the sum

$$
R=\sum_{i\in I}R_i,
$$

because $R$ is a sum of simple left ideals. Hence for any $j\in I$,

$$
R_j\subset R_jR=R_jR_j\subset R_j,
$$

the first inclusion because $R$ contains a unit element, and the last because $R_j$ is a left ideal. We conclude that $R_j$ is also a right ideal, i.e. $R_j$ is a two-sided ideal for all $j\in I$.

We can express the unit element $1$ of $R$ as a sum

$$
1=\sum_{i\in I}e_i
$$

with $e_i\in R_i$. This sum is actually finite, almost all $e_i=0$. Say $e_i\ne0$ for indices $i=1,\ldots,s$, so that we write

$$
1=e_1+\cdots+e_s.
$$

For any $x\in R$, write

$$
x=\sum_{i\in I}x_i,\qquad x_i\in R_i.
$$

For $j=1,\ldots,s$ we have $e_jx=e_jx_j$ and also

$$
x_j=1\cdot x_j=e_1x_j+\cdots+e_sx_j=e_jx_j.
$$

Furthermore, $x=e_1x+\cdots+e_sx$. This proves that there is no index $i$ other than $i=1,\ldots,s$ and also that the $i$-th component $x_i$ of $x$ is uniquely determined as $e_ix=e_ix_i$. Hence the sum $R=R_1+\cdots+R_s$ is direct, and furthermore, $e_i$ is a unit element for $R_i$, which is therefore a ring. Since <span class="original-page-anchor" id="pdf-page-662" aria-hidden="true"></span>$R_iR_j=0$ for $i\ne j$, we find that in fact

$$
R=\prod_{i=1}^s R_i
$$

is a direct product of the rings $R_i$.

A ring $R$ is said to be **simple** if it is semisimple, and if it has only one isomorphism class of simple left ideals. We see that we have proved a structure theorem for semisimple rings:

**Theorem 4.3.** *Let $R$ be semisimple. Then there is only a finite number of non-isomorphic simple left ideals, say $L_1,\ldots,L_s$. If*

$$
R_i=\sum_{L\approx L_i}L
$$

*is the sum of all simple left ideals isomorphic to $L_i$, then $R_i$ is a two-sided ideal, which is also a ring (the operations being those induced by $R$), and $R$ is ring isomorphic to the direct product*

$$
R=\prod_{i=1}^s R_i.
$$

*Each $R_i$ is a simple ring. If $e_i$ is its unit element, then $1=e_1+\cdots+e_s$, and $R_i=Re_i$. We have $e_ie_j=0$ if $i\ne j$.*

We shall now discuss modules.

**Theorem 4.4.** *Let $R$ be semisimple, and let $E$ be an $R$-module $\ne0$. Then*

$$
E=\bigoplus_{i=1}^s R_iE=\bigoplus_{i=1}^s e_iE,
$$

*and $R_iE$ is the submodule of $E$ consisting of the sum of all simple submodules isomorphic to $L_i$.*

*Proof.* Let $E_i$ be the sum of all simple submodules of $E$ isomorphic to $L_i$. If $V$ is a simple submodule of $E$, then $RV=V$, and hence $L_iV=V$ for some $i$. By a previous lemma, we have $L_i\approx V$. Hence $E$ is the direct sum of $E_1,\ldots,E_s$. It is then clear that $R_iE=E_i$.

**Corollary 4.5.** *Let $R$ be semisimple. Every simple module is isomorphic to one of the simple left ideals $L_i$.*

**Corollary 4.6.** *A simple ring has exactly one simple module, up to isomorphism.*

<span class="original-page-anchor" id="pdf-page-663" aria-hidden="true"></span>

Both these corollaries are immediate consequences of Theorems 4.3 and 4.4.

**Proposition 4.7.** *Let $k$ be a field and $E$ a finite dimensional vector space over $k$. Let $S$ be a subset of $\operatorname{End}_k(E)$. Let $R$ be the $k$-algebra generated by the elements of $S$. Then $R$ is semisimple if and only if $E$ is a semisimple $R$ (or $S$) module.*

*Proof.* If $R$ is semisimple, then $E$ is semisimple by Proposition 4.1. Conversely, assume $E$ semisimple as $S$-module. Then $E$ is semisimple as $R$-module, and so is a direct sum

$$
E=\bigoplus_{i=1}^n E_i
$$

where each $E_i$ is simple. Then for each $i$ there exists an element $v_i\in E_i$ such that $E_i=Rv_i$. The map

$$
x\mapsto(xv_1,\ldots,xv_n)
$$

is a $R$-homomorphism of $R$ into $E$, and is an injection since $R$ is contained in $\operatorname{End}_k(E)$. Since a submodule of a semisimple module is semisimple by Proposition 2.2, the desired result follows.

## §5. SIMPLE RINGS

**Lemma 5.1.** *Let $R$ be a ring, and $\psi\in\operatorname{End}_R(R)$ a homomorphism of $R$ into itself, viewed as $R$-module. Then there exists $\alpha\in R$ such that $\psi(x)=x\alpha$ for all $x\in R$.*

*Proof.* We have $\psi(x)=\psi(x\cdot1)=x\psi(1)$. Let $\alpha=\psi(1)$.

**Theorem 5.2.** *Let $R$ be a simple ring. Then $R$ is a finite direct sum of simple left ideals. There are no two-sided ideals except $0$ and $R$. If $L,M$ are simple left ideals, then there exists $\alpha\in R$ such that $L\alpha=M$. We have $LR=R$.*

*Proof.* Since $R$ is by definition also semisimple, it is a direct sum of simple left ideals, say $\bigoplus_{j\in J}L_j$. We can write $1$ as a finite sum $1=\sum_{j=1}^m\beta_j$, with $\beta_j\in L_j$. Then

$$
R=\bigoplus_{j=1}^m R\beta_j=\bigoplus_{j=1}^m L_j.
$$

<span class="original-page-anchor" id="pdf-page-664" aria-hidden="true"></span>

This proves our first assertion. As to the second, it is a consequence of the third. Let therefore $L$ be a simple left ideal. Then $LR$ is a left ideal, because $RLR=LR$, hence ($R$ being semisimple) is a direct sum of simple left ideals, say

$$
LR=\bigoplus_{j=1}^m L_j,\quad L=L_1.
$$

Let $M$ be a simple left ideal. We have a direct sum decomposition $R=L\oplus L'$. Let $\pi:R\to L$ be the projection. It is an $R$-endomorphism. Let $\sigma:L\to M$ be an isomorphism (it exists by Theorem 4.3). Then $\sigma\circ\pi:R\to R$ is an $R$-endomorphism. By the lemma, there exists $\alpha\in R$ such that

$$
\sigma\circ\pi(x)=x\alpha\quad\text{for all }x\in R.
$$

Apply this to elements $x\in L$. We find

$$
\sigma(x)=x\alpha\quad\text{for all }x\in L.
$$

The map $x\mapsto x\alpha$ is a $R$-homomorphism of $L$ into $M$, is non-zero, hence is an isomorphism. From this it follows at once that $LR=R$, thereby proving our theorem.

**Corollary 5.3.** *Let $R$ be a simple ring. Let $E$ be a simple $R$-module, and $L$ a simple left ideal of $R$. Then $LE=E$ and $E$ is faithful.*

*Proof.* We have $LE=L(RE)=(LR)E=RE=E$. Suppose $\alpha E=0$ for some $\alpha\in R$. Then $R\alpha RE=R\alpha E=0$. But $R\alpha R$ is a two-sided ideal. Hence $R\alpha R=0$, and $\alpha=0$. This proves that $E$ is faithful.

**Theorem 5.4. (Rieffel).** *Let $R$ be a ring without two-sided ideals except $0$ and $R$. Let $L$ be a nonzero left ideal, $R'=\operatorname{End}_R(L)$ and $R''=\operatorname{End}_{R'}(L)$. Then the natural map $\lambda:R\to R''$ is an isomorphism.*

*Proof.* The kernel of $\lambda$ is a two-sided ideal, so $\lambda$ is injective. Since $LR$ is a two-sided ideal, we have $LR=R$ and $\lambda(L)\lambda(R)=\lambda(R)$. For any $x,y\in L$, and $f\in R''$, we have $f(xy)=f(x)y$, because right multiplication by $y$ is an $R$-endomorphism of $L$. Hence $\lambda(L)$ is a left ideal of $R''$, so

$$
R''=R''\lambda(R)=R''\lambda(L)\lambda(R)=\lambda(L)\lambda(R)=\lambda(R),
$$

as was to be shown.

In Rieffel's theorem, we do not need to assume that $L$ is a simple module.

<span class="original-page-anchor" id="pdf-page-665" aria-hidden="true"></span>

On the other hand, $L$ is an ideal. So this theorem is not equivalent with previous ones of the same nature. In §7, we shall give a very general condition under which the canonical homomorphism

$$
R\to R''
$$

of a ring into the double endomorphism ring of a module is an isomorphism. This will cover all the previous cases.

As pointed out in the example following Wedderburn's theorem, Rieffel's theorem applies to give another proof when $R$ is a finite-dimensional algebra (with unit) over a field $k$.

The next theorem gives a converse, showing that matrix rings over division algebras are simple.

**Theorem 5.5.** *Let $D$ be a division ring, and $E$ a finite-dimensional vector space over $D$. Let $R=\operatorname{End}_D(E)$. Then $R$ is simple and $E$ is a simple $R$-module. Furthermore, $D=\operatorname{End}_R(E)$.*

*Proof.* We first show that $E$ is a simple $R$-module. Let $v\in E$, $v\ne0$. Then $v$ can be completed to a basis of $E$ over $D$, and hence, given $w\in E$, there exists $\alpha\in R$ such that $\alpha v=w$. Hence $E$ cannot have any invariant subspaces other than $0$ or itself, and is simple over $R$. It is clear that $E$ is faithful over $R$. Let $\{v_1,\ldots,v_m\}$ be a basis of $E$ over $D$. The map

$$
\alpha\mapsto(\alpha v_1,\ldots,\alpha v_m)
$$

of $R$ into $E^{(m)}$ is an $R$-homomorphism of $R$ into $E^{(m)}$, and is injective. Given $(w_1,\ldots,w_m)\in E^{(m)}$, there exists $\alpha\in R$ such that $\alpha v_i=w_i$ and hence $R$ is $R$-isomorphic to $E^{(m)}$. This shows that $R$ (as a module over itself) is isomorphic to a direct sum of simple modules and is therefore semisimple. Furthermore, all these simple modules are isomorphic to each other, and hence $R$ is simple by Theorem 4.3.

There remains to prove that $D=\operatorname{End}_R(E)$. We note that $E$ is a semisimple module over $D$ since it is a vector space, and every subspace admits a complementary subspace. We can therefore apply the density theorem (the roles of $R$ and $D$ are now permuted!). Let $\varphi\in\operatorname{End}_R(E)$. Let $v\in E$, $v\ne0$. By the density theorem, there exists an element $a\in D$ such that $\varphi(v)=av$. Let $w\in E$. There exists an element $f\in R$ such that $f(v)=w$. Then

$$
\varphi(w)=\varphi(f(v))=f(\varphi(v))=f(av)=af(v)=aw.
$$

Therefore $\varphi(w)=aw$ for all $w\in E$. This means that $\varphi\in D$, and concludes our proof.

**Theorem 5.6.** *Let $k$ be a field and $E$ a finite-dimensional vector space of* <span class="original-page-anchor" id="pdf-page-666" aria-hidden="true"></span>*dimension $m$ over $k$. Let $R=\operatorname{End}_k(E)$. Then $R$ is a $k$-space, and*

$$
\dim_kR=m^2.
$$

*Furthermore, $m$ is the number of simple left ideals appearing in a direct sum decomposition of $R$ as such a sum.*

*Proof.* The $k$-space of $k$-endomorphisms of $E$ is represented by the space of $m\times m$ matrices in $k$, so the dimension of $R$ as a $k$-space is $m^2$. On the other hand, the proof of Theorem 5.5 showed that $R$ is $R$-isomorphic as an $R$-module to the direct sum $E^{(m)}$. We know the uniqueness of the decomposition of a module into a direct sum of simple modules (Proposition 1.2), and this proves our assertion.

In the terminology introduced in §1, we see that the integer $m$ in Theorem 5.6 is the **length** of $R$.

We can identify $R=\operatorname{End}_k(E)$ with the ring of matrices $\operatorname{Mat}_m(k)$, once a basis of $E$ is selected. In that case, we can take the simple left ideals to be the ideals $L_i$ ($i=1,\ldots,m$) where a matrix in $L_i$ has coefficients equal to $0$ except in the $i$-th column. An element of $L_1$ thus looks like

![Matrix in the first-column left ideal](/library/volume-86/diagrams/pdf-0666-first-column-ideal.png)

We see that $R$ is the direct sum of the $m$ columns.

We also observe that Theorem 5.5 implies the following:

*If a matrix $M\in\operatorname{Mat}_m(k)$ commutes with all elements of $\operatorname{Mat}_m(k)$, then $M$ is a scalar matrix.*

Indeed, such a matrix $M$ can then be viewed as an $R$-endomorphism of $E$, and we know by Theorem 5.5 that such an endomorphism lies in $k$. Of course, one can also verify this directly by a brute force computation.

## §6. THE JACOBSON RADICAL, BASE CHANGE, AND TENSOR PRODUCTS

Let $R$ be a ring and let $M$ be a maximal left ideal. Then $R/M$ is an $R$-module, and actually $R/M$ is simple. Indeed, let $\bar J$ be a submodule of $R/M$ with $\bar J\ne R/M$. Let $J$ be its inverse image in $R$ under the canonical homomorphism.

<span class="original-page-anchor" id="pdf-page-667" aria-hidden="true"></span>

Then $J$ is a left ideal $\ne M$ because $\bar J\ne R/M$, so $J=R$ and $\bar J=0$. Conversely, let $E$ be a simple $R$-module and let $v\in E$, $v\ne0$. Then $Rv$ is a submodule $\ne0$ of $E$, and hence $Rv=E$. Let $M$ be the kernel of the homomorphism $x\mapsto xv$. Then $M$ is a left ideal, and $M$ is maximal; otherwise there is a left ideal $M'$ with $R\supset M'\supset M$ and $M'\ne R$, $\ne M$. Then $R/M\approx E$ and $R/M'$ is a non-zero homomorphic image of $E$, which cannot exist since $E$ is simple (Schur's lemma, Proposition 1.1). Thus we obtain a bijection between maximal left ideals and simple $R$-modules (up to isomorphism).

We define the **Jacobson radical** of $R$ to be the left ideal $N$ which is the intersection of all maximal left ideals of $R$. We may also denote $N=\operatorname{Rad}(R)$.

**Theorem 6.1.**

(a) *For every simple $R$-module we have $NE=0$.*

(b) *The radical $N$ is a two-sided ideal, containing all nilpotent two-sided ideals.*

(c) *Let $R$ be a finite dimensional algebra over field $k$. Its radical is $\{0\}$, if and only if $R$ is semisimple.*

(d) *If $R$ is a finite dimensional algebra over a field $k$, then its radical $N$ is nilpotent (i.e. $N^r=0$ for some positive integer $r$).*

These statements are easy to prove, and hints will be given appropriately. See Exercises 1 through 5.

Observe that under finite dimensionality conditions, the radical's being $0$ gives us a useful criterion for a ring to be semisimple, which we shall use in the next result.

**Theorem 6.2.** *Let $A$ be a semisimple algebra, finite dimensional over a field $k$. Let $K$ be a finite separable extension of $k$. Then $K\otimes_kA$ is a semisimple over $K$.*

*Proof.* In light of the radical criterion for semisimplicity, it suffices to prove that $K\otimes_kA$ has zero radical, and it suffices to do so for an even larger extension than $K$, so that we may assume $K$ is Galois over $k$, say with Galois group $G$. Then $G$ operates on $K\otimes A$ by

$$
\sigma(x\otimes a)=\sigma x\otimes a\quad\text{for }x\in K\quad\text{and }a\in A.
$$

Let $N$ be the radical of $K\otimes A$. Since $N$ is nilpotent, it follows that $\sigma N$ is also nilpotent for all $\sigma\in G$, whence $\sigma N=N$ because $N$ is the maximal nilpotent ideal (Exercise 5). Let $\{a_1,\ldots,a_m\}$ be a basis of $A$ over $k$. Suppose $N$ contains the element

$$
\xi=\sum x_i\otimes a_i\ne0\quad\text{with }x_i\in K.
$$

For every $y\in K$ the element $(y\otimes1)\xi=\sum yx_i\otimes a_i$ also lies in $N$. Then

$$
\operatorname{trace}((y\otimes1)\xi)=\sum\sigma\xi=\sum\operatorname{Tr}(yx_i)\otimes a_i=\sum1\otimes a_i\operatorname{Tr}(yx_i)
$$

also lies in $N$, and lies in $1\otimes A=A$, thus proving the theorem.

<span class="original-page-anchor" id="pdf-page-668" aria-hidden="true"></span>

**Remark.** For the case when $A$ is a finite extension of $k$, compare with Exercises 1, 2, 3 of Chapter XVI.

Let $A$ be a semisimple algebra, finite dimensional over a field $k$. Then by Theorem 6.2 the extension of scalars $A\otimes_k k^a$ is semisimple if $k$ is perfect. In general, an algebra $A$ over $k$ is said to be **absolutely semisimple** if $A\otimes_k k^a$ is semisimple.

We now look at semisimple algebras over an algebraically closed field.

**Theorem 6.3.** *Let $A,B$ be simple algebras, finite dimensional over a field $k$ which is algebraically closed. Then $A\otimes_k B$ is also simple. We have $A\approx\operatorname{End}_k(V)$ and $B\approx\operatorname{End}_k(W)$ where $V,W$ are finite dimensional vector spaces over $k$ and there is a natural isomorphism*

$$
A\otimes_k B\approx\operatorname{End}_k(V\otimes_k W)\approx\operatorname{End}_k(V)\otimes_k\operatorname{End}_k(W).
$$

*Proof.* The formula is a special case of Theorem 2.5 of Chapter XVI, and the isomorphisms $A\approx\operatorname{End}_k(V)$, $B\approx\operatorname{End}_k(W)$ exist by Wedderburn's theorem or its corollaries.

Let $A$ be an algebra over $k$ and let $F$ be an extension field of $k$. We denote by $A_F$ the extension of scalars

$$
A_F=A\otimes_k F.
$$

Thus $A_F$ is an algebra over $F$. As an exercise, prove that if $k$ is the center of $A$, then $F$ is the center of $A_F$. (Here we identify $F$ with $1\otimes F$.)

Let $A,B$ be algebras over $k$. We leave to the reader the proof that for every extension field $F$ of $k$, we have a natural isomorphism

$$
(A\otimes_k B)_F=A_F\otimes_F B_F.
$$

We apply the above considerations to the tensor product of semisimple algebras.

**Theorem 6.4.** *Let $A,B$ be absolutely semisimple algebras finite dimensional over a field $k$. Then $A\otimes_k B$ is absolutely semisimple.*

*Proof.* Let $F=k^a$. Then $A_F$ is semisimple by hypothesis, so it is a direct product of simple algebras, which are matrix algebras, and in particular we can apply Theorem 6.3 to see that $A_F\otimes_F B_F$ has no radical. Hence $A\otimes_k B$ has no radical (because if $N$ is its radical, then $N\otimes_k F=N_F$ is a nilpotent ideal of $A_F\otimes_F B_F$), whence $A\otimes_k B$ is semisimple by Theorem 6.1(c).

**Remark.** We have proved the above tensor product theorems rapidly in special cases, which are already important in various applications. For a more general treatment, I recommend Bourbaki's *Algebra*, Chapter VIII, which gives an exhaustive treatment of tensor products of semisimple and simple algebras.

<span class="original-page-anchor" id="pdf-page-669" aria-hidden="true"></span>

## §7. BALANCED MODULES

Let $R$ be a ring and $E$ a module. We let $R'(E)=\operatorname{End}_R(E)$ and

$$
R''(E)=\operatorname{End}_{R'}(E).
$$

Let $\lambda:R\to R''$ be the natural homomorphism such that $\lambda_x(v)=xv$ for $x\in R$ and $v\in E$. If $\lambda$ is an isomorphism, we shall say that $E$ is **balanced**. We shall say that $E$ is a **generator** (for $R$-modules) if every module is a homomorphic image of a (possibly infinite) direct sum of $E$ with itself. For example, $R$ is a generator.

More interestingly, in Rieffel's Theorem 5.4, the left ideal $L$ is a generator, because $LR=R$ implies that there is a surjective homomorphism $L\times\cdots\times L\to R$ since we can write $1$ as a finite combination

$$
1=x_1a_1+\cdots+x_na_n\quad\text{with }x_i\in L\text{ and }a_i\in R.
$$

The map $(x_1,\ldots,x_n)\mapsto x_1a_1+\cdots+x_na_n$ is a $R$-homomorphism of left module onto $R$.

If $E$ is a generator, then there is a surjective homomorphism $E^{(n)}\to R$ (we can take $n$ finite since $R$ is finitely generated, by one element $1$).

**Theorem 7.1. (Morita).** *Let $E$ be an $R$-module. Then $E$ is a generator if and only if $E$ is balanced and finitely generated projective over $R'(E)$.*

*Proof.* We shall prove half of the theorem, leaving the other half to the reader, using similar ideas (see Exercise 12). So we assume that $E$ is a generator, and we prove that it satisfies the other properties by arguments due to Faith.

We first prove that for any module $F$, $R\oplus F$ is balanced. We identify $R$ and $F$ as the submodules $R\oplus0$ and $0\oplus F$ of $R\oplus F$, respectively. For $w\in F$, let $\psi_w:R\oplus F\to F$ be the map $\psi_w(x+v)=xw$. Then any $f\in R''(R\oplus F)$ commutes with $\pi_1$, $\pi_2$, and each $\psi_w$. From this we see at once that $f(x+v)=f(1)(x+v)$ and hence that $R\oplus F$ is balanced. Let $E$ be a generator, and $E^{(n)}\to R$ a surjective homomorphism. Since $R$ is free, we can write $E^{(n)}\approx R\oplus F$ for some module $F$, so that $E^{(n)}$ is balanced. Let $g\in R'(E)$. Then $g^{(n)}$ commutes with every element $\varphi=(\varphi_{ij})$ in $R'(E^{(n)})$ (with components $\varphi_{ij}\in R'(E)$), and hence there is some $x\in R$ such that $g^{(n)}=\lambda_x^{(n)}$. Hence $g=\lambda_x$, thereby proving that $E$ is balanced, since $\lambda$ is obviously injective.

To prove that $E$ is finitely generated over $R'(E)$, we have

$$
R'(E)^{(n)}\approx\operatorname{Hom}_R(E^{(n)},E)\approx\operatorname{Hom}_R(R,E)\oplus\operatorname{Hom}_R(F,E)
$$

as additive groups. This relation also obviously holds as $R'$-modules if we define the operation of $R'$ to be composition of mappings (on the left). Since $\operatorname{Hom}_R(R,E)$ is $R'$-isomorphic to $E$ under the map $h\mapsto h(1)$, it follows that $E$ is an $R'$-homomorphic image of $R'^{(n)}$, whence finitely generated over $R'$. We also see that $E$ is a direct summand of the free $R'$-module $R'^{(n)}$ and is therefore projective over $R'(E)$. This concludes the proof.

<span class="original-page-anchor" id="pdf-page-670" aria-hidden="true"></span>

## EXERCISES

### The radical

**1.** (a) Let $R$ be a ring. We define the **radical** of $R$ to be the left ideal $N$ which is the intersection of all maximal left ideals of $R$. Show that $NE=0$ for every simple $R$-module $E$. Show that $N$ is a two-sided ideal. (b) Show that the radical of $R/N$ is $0$.

**2.** A ring is said to be **Artinian** if every descending sequence of left ideals $J_1\supset J_2\supset\cdots$ with $J_i\ne J_{i+1}$ is finite. (a) Show that a finite dimensional algebra over a field is Artinian. (b) If $R$ is Artinian, show that every non-zero left ideal contains a simple left ideal. (c) If $R$ is Artinian, show that every non-empty set of ideals contains a minimal ideal.

**3.** Let $R$ be Artinian. Show that its radical is $0$ if and only if $R$ is semisimple. [*Hint:* Get an injection of $R$ into a direct sum $\bigoplus R/M_i$ where $\{M_i\}$ is a finite set of maximal left ideals.]

**4. Nakayama's lemma.** Let $R$ be any ring and $M$ a finitely generated module. Let $N$ be the radical of $R$. If $NM=M$ show that $M=0$. [*Hint:* Observe that the proof of Nakayama's lemma still holds.]

**5.** (a) Let $J$ be a two-sided nilpotent ideal of $R$. Show that $J$ is contained in the radical. (b) Conversely, assume that $R$ is Artinian. Show that its radical is nilpotent, i.e., that there exists an integer $r\ge1$ such that $N^r=0$. [*Hint:* Consider the descending sequence of powers $N^r$, and apply Nakayama to a minimal finitely generated left ideal $L\subset N^\infty$ such that $N^\infty L\ne0$.

**6.** Let $R$ be a semisimple commutative ring. Show that $R$ is a direct product of fields.

**7.** Let $R$ be a finite dimensional commutative algebra over a field $k$. If $R$ has no nilpotent element $\ne0$, show that $R$ is semisimple.

**8. (Kolchin)** Let $E$ be a finite-dimensional vector space over a field $k$. Let $G$ be a subgroup of $\operatorname{GL}(E)$ such that every element $A\in G$ is of type $I+N$ where $N$ is nilpotent. Assume $E\ne0$. Show that there exists an element $v\in E$, $v\ne0$ such that $Av=v$ for all $A\in G$. [*Hint:* First reduce the question to the case when $k$ is algebraically closed by showing that the problem amounts to solving linear equations. Secondly, reduce it to the case when $E$ is a simple $k[G]$-module. Combining Burnside's theorem with the fact that $\operatorname{tr}(A)=\operatorname{tr}(I)$ for all $A\in G$, show that if $A_0\in G$, $A_0=I+N$, then $\operatorname{tr}(NX)=0$ for all $X\in\operatorname{End}_k(E)$, and hence that $N=0$, $A_0=I$.]

### Semisimple operations

**9.** Let $E$ be a finite dimensional vector space over a field $k$. Let $R$ be a semisimple subalgebra of $\operatorname{End}_k(E)$. Let $a,b\in R$. Assume that

$$
\operatorname{Ker} b_E\supset\operatorname{Ker} a_E,
$$

where $b_E$ is multiplication by $b$ on $E$ and similarly for $a_E$. Show that there exists an element $s\in R$ such that $sa=b$. [*Hint:* Reduce to $R$ simple. Then $R=\operatorname{End}_D(E_0)$ and $E=E_0^{(n)}$. Let $v_1,\ldots,v_r\in E$ be a $D$-basis for $aE$. Define $s$ by $s(av_i)=bv_i$ and <span class="original-page-anchor" id="pdf-page-671" aria-hidden="true"></span>extend $s$ by $D$-linearity. Then $sa_E=b_E$, so $sa=b$.]

**10.** Let $E$ be a finite-dimensional vector space over a field $k$. Let $A\in\operatorname{End}_k(E)$. We say that $A$ is **semisimple** if $E$ is a semisimple $A$-space, or equivalently, let $R$ be the $k$-algebra generated by $A$, then $E$ is semisimple over $R$. Show that $A$ is semisimple if and only if its minimal polynomial has no factors of multiplicity $>1$ over $k$.

**11.** Let $E$ be a finite-dimensional vector space over a field $k$, and let $S$ be a commutative set of endomorphisms of $E$. Let $R=k[S]$. Assume that $R$ is semisimple. Show that every subset of $S$ is semisimple.

**12.** Prove that an $R$-module $E$ is a generator if and only if it is balanced, and finitely generated projective over $R'(E)$. Show that Theorem 5.4 is a consequence of Theorem 7.1.

**13.** Let $A$ be a principal ring with quotient field $K$. Let $A^n$ be $n$-space over $A$, and let

$$
T=A^n\oplus A^n\oplus\cdots\oplus A^n
$$

be the direct sum of $A^n$ with itself $r$ times. Then $T$ is free of rank $nr$ over $A$. If we view elements of $A^n$ as column vectors, then $T$ is the space of $n\times r$ matrices over $A$. Let $M=\operatorname{Mat}_n(A)$ be the ring of $n\times n$ matrices over $A$, operating on the left of $T$. By a **lattice** $L$ in $T$ we mean an $A$-submodule of rank $nr$ over $A$. Prove that any such lattice which is $M$-stable is $M$-isomorphic to $T$ itself. Thus there is just one $M$-isomorphism class of lattices. [*Hint:* Let $g\in M$ be the matrix with $1$ in the upper left corner and $0$ everywhere else, so $g$ is a projection of $A^n$ on a $1$-dimensional subspace. Then multiplication on the left $g:T\to A_r$ maps $T$ on the space of $n\times r$ matrices with arbitrary first row and $0$ everywhere else. Furthermore, for any lattice $L$ in $T$ the image $gL$ is a lattice in $A_r$, that is a free $A$-submodule of rank $r$. By elementary divisors there exists an $r\times r$ matrix $Q$ such that

$$
gL=A_rQ\qquad\text{(multiplication on the right).}
$$

Then show that $TQ=L$ and that multiplication by $Q$ on the right is an $M$-isomorphism of $T$ with $L$.]

**14.** Let $F$ be a field. Let $\mathfrak n=\mathfrak n(F)$ be the vector space of strictly upper triangular $n\times n$ matrices over $F$. Show that $\mathfrak n$ is actually an algebra, and all elements of $\mathfrak n$ are nilpotent (some positive integral power is $0$).

**15. Conjugation representation.** Let $A$ be the multiplicative group of diagonal matrices in $F$ with non-zero diagonal components. For $a\in A$, the **conjugation action** of $a$ on $\operatorname{Mat}_n(F)$ is denoted by $c(a)$, so $c(a)M=aMa^{-1}$ for $M\in\operatorname{Mat}_n(F)$. (a) Show that $\mathfrak n$ is stable under this action. (b) Show that $\mathfrak n$ is semisimple under this action. More precisely, for $1\le i<j\le n$, let $E_{ij}$ be the matrix with $(ij)$-component $1$, and all other components $0$. Then these matrices $E_{ij}$ form a basis for $\mathfrak n$ over $F$, and each $E_{ij}$ is an eigenvector for the conjugation action, namely for $a=\operatorname{diag}(a_1,\ldots,a_n)$, we have

$$
aE_{ij}a^{-1}=(a_i/a_j)E_{ij},
$$

so the corresponding character $\chi_{ij}$ is given by $\chi_{ij}(a)=a_i/a_j$. (c) Show that $\operatorname{Mat}_n(F)$ is semisimple, and in fact is equal to $\mathfrak d\oplus\mathfrak n\oplus{}^t\mathfrak n$, where $\mathfrak d$ is the space of diagonal matrices.
