---
title: "Structure of finite dimensional algebras"
description: "《Introduction to Representation Theory》English。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"Homological algebra","link":"/library/volume-88/original-chapter-008"}
next: {"text":"References for historical interludes","link":"/library/volume-88/original-historical-references"}
---

# Structure of finite dimensional algebras

<span class="original-page-anchor" id="pdf-page-217" aria-hidden="true"></span>

In this chapter we return to studying the structure of finite dimensional algebras. Throughout the chapter, we work over an algebraically closed field $k$ (of any characteristic).

## 9.1. Lifting of idempotents

Let $A$ be a ring, and let $I\subset A$ be a nilpotent ideal.

**Proposition 9.1.1.** Let $e_0\in A/I$ be an idempotent, i.e., $e_0^2=e_0$. There exists an idempotent $e\in A$ which is a lift of $e_0$ (i.e., it projects to $e_0$ under the reduction modulo $I$). This idempotent is unique up to conjugation by an element of $1+I$.

**Proof.** Let us first establish the statement in the case when $I^2=0$. Note that in this case $I$ is a left and right module over $A/I$. Let $e_*$ be any lift of $e_0$ to $A$. Then $e_*^2-e_*=a\in I$, and $e_0a=ae_0$. We look for $e$ in the form $e=e_*+b$, $b\in I$. The equation for $b$ is $e_0b+be_0-b=a$. Set $b=(2e_0-1)a$. Then

$$
e_0b+be_0-b=2e_0a-(2e_0-1)a=a,
$$

so $e$ is an idempotent. To classify other solutions, set $e'=e+c$. For $e'$ to be an idempotent, we must have $ec+ce-c=0$. This <span class="original-page-anchor" id="pdf-page-218" aria-hidden="true"></span>is equivalent to saying that $ece=0$ and $(1-e)c(1-e)=0$, so $c=ec(1-e)+(1-e)ce=[e,[e,c]]$. Hence $e'=(1+[c,e])e(1+[c,e])^{-1}$.

Now, in the general case, we prove by induction in $k$ that there exists a lift $e_k$ of $e_0$ to $A/I^{k+1}$, and it is unique up to conjugation by an element of $1+I^k$ (this is sufficient as $I$ is nilpotent). Assume it is true for $k=m-1$, and let us prove it for $k=m$. So we have an idempotent $e_{m-1}\in A/I^m$, and we have to lift it to $A/I^{m+1}$. But $(I^m)^2=0$ in $A/I^{m+1}$, so we are done. $\square$

**Definition 9.1.2.** A **complete system of orthogonal idempotents** in a unital algebra $B$ is a collection of elements $e_1,\ldots,e_n\in B$ such that $e_i e_j=\delta_{ij}e_i$ and $\sum_{i=1}^n e_i=1$.

**Corollary 9.1.3.** Let $e_{01},\ldots,e_{0m}$ be a complete system of orthogonal idempotents in $A/I$. Then there exists a complete system of orthogonal idempotents $e_1,\ldots,e_m$ ($e_i e_j=\delta_{ij}e_i$, $\sum e_i=1$) in $A$ which lifts $e_{01},\ldots,e_{0m}$.

**Proof.** The proof is by induction in $m$. For $m=2$ this follows from Proposition 9.1.1. For $m>2$, we lift $e_{01}$ to $e_1$ using Proposition 9.1.1 and then apply the induction assumption to the algebra $(1-e_1)A(1-e_1)$. $\square$

## 9.2. Projective covers

Obviously, every finitely generated projective module over a finite dimensional algebra $A$ is a direct sum of indecomposable projective modules, so to understand finitely generated projective modules over $A$, it suffices to classify indecomposable projective modules.

Let $A$ be a finite dimensional algebra with simple modules $M_1,\ldots,M_n$.

**Theorem 9.2.1.** (i) For each $i=1,\ldots,n$ there exists a unique indecomposable finitely generated projective module $P_i$ such that

$$
\dim\operatorname{Hom}(P_i,M_j)=\delta_{ij}.
$$

(ii) $A=\bigoplus_{i=1}^n(\dim M_i)P_i$.

(iii) Any indecomposable finitely generated projective module over $A$ is isomorphic to $P_i$ for some $i$.

<span class="original-page-anchor" id="pdf-page-219" aria-hidden="true"></span>

**Proof.** Recall that $A/\operatorname{Rad}(A)=\bigoplus_{i=1}^n\operatorname{End}(M_i)$ and that $\operatorname{Rad}(A)$ is a nilpotent ideal. Pick a basis of $M_i$, and let $e_{ij}^0=E_{jj}^i$, the rank $1$ projectors projecting to the basis vectors of this basis ($j=1,\ldots,\dim M_i$). Then $e_{ij}^0$ are orthogonal idempotents in $A/\operatorname{Rad}(A)$. So by Corollary 9.1.3 we can lift them to orthogonal idempotents $e_{ij}$ in $A$. Now define $P_{ij}=Ae_{ij}$. Then $A=\bigoplus_i\bigoplus_{j=1}^{\dim M_i}P_{ij}$, so $P_{ij}$ are projective. Also, we have $\operatorname{Hom}(P_{ij},M_k)=e_{ij}M_k$, so $\dim\operatorname{Hom}(P_{ij},M_k)=\delta_{ik}$. Finally, $P_{ij}$ is independent of $j$ up to an isomorphism, as $e_{ij}$ for fixed $i$ are conjugate under $A^\times$ by Proposition 9.1.1; thus we will denote $P_{ij}$ by $P_i$.

We claim that $P_i$ is indecomposable. Indeed, if $P_i=Q_1\oplus Q_2$, then $\operatorname{Hom}(Q_l,M_j)=0$ for all $j$ either for $l=1$ or for $l=2$, so either $Q_1=0$ or $Q_2=0$.

Also, there can be no other indecomposable finitely generated projective modules, since any indecomposable projective module has to occur in the decomposition of $A$. The theorem is proved. $\square$

**Definition 9.2.2.** The projective module $P_i$ is called the **projective cover** of $M_i$.

**Proposition 9.2.3.** Let $N$ be any finite dimensional $A$-module. Then one has $\dim\operatorname{Hom}_A(P_i,N)=[N:M_i]$, the multiplicity of occurrence on $M_i$ in the Jordan–Hölder series of $N$.

**Proof.** If $N=M_j$, the statement is clear. Also, if

$$
0\to N_1\to N_2\to N_3\to0
$$

is an exact sequence of $A$-modules, then the corresponding sequence

$$
0\to\operatorname{Hom}_A(P_i,N_1)\to\operatorname{Hom}_A(P_i,N_2)\to\operatorname{Hom}_A(P_i,N_3)\to0
$$

is exact, as $P_i$ is projective. This implies the statement. $\square$

## 9.3. The Cartan matrix of a finite dimensional algebra

Let $A$ be a finite dimensional algebra with simple modules $M_i$, $i=1,\ldots,n$, and projective covers $P_i$. Let $c_{ij}:=\dim\operatorname{Hom}_A(P_i,P_j)=[P_j:M_i]$.

<span class="original-page-anchor" id="pdf-page-220" aria-hidden="true"></span>

**Definition 9.3.1.** The matrix $C=(c_{ij})$ is called the **Cartan matrix** of $A$.

Obviously, the Cartan matrix of $A$ is a matrix with nonnegative entries, whose diagonal entries are positive.

**Problem 9.3.2.** Let $A$ be the algebra over complex numbers generated by elements $g,x$ with defining relations $gx=-xg$, $x^2=0$, $g^2=1$. Find the simple modules, the indecomposable projective modules, and the Cartan matrix of $A$.

## 9.4. Homological dimension

Let $A$ be a ring, and let $M$ be a left $A$-module.

**Definition 9.4.1.** The **projective dimension** $\operatorname{pd}(M)$ of $M$ is the length of the shortest finite projective resolution of $M$ (where we agree that the length of $0\to P_d\to\cdots\to P_0$ is $d$). If a finite projective resolution of $M$ does not exist, then the projective dimension of $M$ is infinite.

For instance, the projective modules are the modules of projective dimension $0$.

**Problem 9.4.2.** (i) Show that $\operatorname{pd}(M)\leq d$ if and only if for any left $A$-module $N$, one has $\operatorname{Ext}^i(M,N)=0$ for $i>d$.

Hint: To prove the “if” part, use induction in $d$ and the long exact sequence of Ext groups in Problem 8.2.6(v).

(ii) Let $0\to M\to P\to N\to0$ be a nonsplit short exact sequence, and assume that $P$ is projective. Show that $\operatorname{pd}(N)=\operatorname{pd}(M)+1$.

(iii) Show that if $\operatorname{pd}(M)=d>0$ and $P_\bullet$ is any projective resolution of $M$, then the kernel $K_d$ of the map $P_{d-1}\to P_{d-2}$ in this resolution is projective (where we agree that $P_{-1}=M$). Thus, by replacing $P_d$ with $K_d$ and all terms to the left of $P_d$ by zero, we get a projective resolution of $M$ of length $d$. Deduce that if $A$ and $M$ are finite dimensional, then there is a finite resolution $P_\bullet$ of $M$ with finite dimensional $P_i$.

<span class="original-page-anchor" id="pdf-page-221" aria-hidden="true"></span>

**Definition 9.4.3.** One says that a ring $A$ has left (respectively, right) **homological dimension** $\leq d$ if every left (respectively, right) $A$-module $M$ has projective dimension $\leq d$. The homological dimension of $A$ is exactly $d$ if it is $\leq d$ but not $\leq d-1$. If such a $d$ does not exist, one says that $A$ has infinite homological dimension.

**Example 9.4.4.** By the Hilbert syzygies theorem (see Problem 8.2.10(iv)), the homological dimension of the polynomial algebra $k[x_1,\ldots,x_n]$ is $n$.

**Problem 9.4.5.** (i) Show that if a finite dimensional algebra $A$ has finite homological dimension $d$ and if $C$ is the Cartan matrix of $A$, then $\det(C)=\pm1$.

(ii) What is the homological dimension of $k[t]/t^n$, $n>1$? Of the algebra of Problem 9.3.2?

**Problem 9.4.6.** (i) Show that the path algebra $P_Q$ of any quiver $Q$ with at least one edge has homological dimension $1$. In particular, the homological dimension of the free algebra $k\langle x_1,\ldots,x_n\rangle$ is $1$ (for $n\geq1$).

(ii) Let $Q$ be a finite oriented graph without oriented cycles. Find the Cartan matrix of its path algebra $P_Q$.

## 9.5. Blocks

Let $A$ be a finite dimensional algebra over an algebraically closed field $k$, and let $\mathcal C$ denote the category of finite dimensional $A$-modules.

**Definition 9.5.1.** Two simple finite dimensional $A$-modules $X,Y$ are said to be **linked** if there is a chain $X=M_0,M_1,\ldots,M_n=Y$ such that for each $i=0,\ldots,n-1$ either $\operatorname{Ext}^1(M_i,M_{i+1})\neq0$ or $\operatorname{Ext}^1(M_{i+1},M_i)\neq0$ (or both).

Here we agree that $X$ is linked to itself (by a chain of length $0$).

This linking relation is clearly an equivalence relation, so it defines a splitting of the set $S$ of isomorphism classes of simple $A$-modules into equivalence classes $S_k$, $k\in B$. The $k$th **block** $\mathcal C_k$ of $\mathcal C$ is, by definition, the category of all objects $M$ of $\mathcal C$ such that all simple modules occurring in the Jordan–Hölder series of $M$ are in $S_k$.

<span class="original-page-anchor" id="pdf-page-222" aria-hidden="true"></span>

**Example 9.5.2.** If $A$ is semisimple, each block is equivalent to the category of vector spaces (and thus has only one simple object). If $A$ is a commutative local artinian algebra, then there is only one block. Also there is just one block for the algebra of Problem 9.3.2.

**Problem 9.5.3.** (i) Show that there is a natural bijection between blocks of $\mathcal C$ and indecomposable central idempotents $e_k$ of $A$ (i.e., ones that cannot be nontrivially split in a sum of two central idempotents), such that $\mathcal C_k$ is the category of finite dimensional $e_k A$-modules.

(ii) Show that any indecomposable object of $\mathcal C$ lies in some $\mathcal C_k$ and that $\operatorname{Hom}(M,N)=0$ if $M\in\mathcal C_k$, $N\in\mathcal C_l$, $k\neq l$. Thus, $\mathcal C=\bigoplus_{k\in B}\mathcal C_k$.

(iii) Determine the blocks in the category of left $A$-modules for $A=k[S_3]$, where $k$ is of characteristic $2$.

## 9.6. Finite abelian categories

Let $\mathcal C$ be a $k$-linear abelian category in which any object has finite length (i.e., a finite filtration whose successive quotients are simple). Assume that for every simple object $X$ of $\mathcal C$, one has $\operatorname{End}(X)=k$. Note that in such a category, Hom spaces are finite dimensional (check it!).

**Definition 9.6.1.** Let us say that $\mathcal C$ is **finite** if it has enough projectives and finitely many simple objects (up to an isomorphism).

For example, as we have shown, the category of finite dimensional modules over a finite dimensional algebra is finite. Below we will see that the converse is also true.

**Definition 9.6.2.** An object $P$ of an abelian category $\mathcal C$ is said to be a **projective generator** (or **progenerator**) if it is projective and every object is a quotient of a multiple of $P$.

For example, in the category of modules over a ring $A$, the free module $A$ is a projective generator.

**Exercise 9.6.3.** Show that in a finite abelian category, $P$ is a projective generator if and only if for every simple object $L$, one has $\operatorname{Hom}(P,L)\neq0$. Deduce that any finite abelian category has a projective generator.

<span class="original-page-anchor" id="pdf-page-223" aria-hidden="true"></span>

Now let $\mathcal C$ be a finite abelian category with a projective generator $P$. Let $B=\operatorname{End}(P)^{\mathrm{op}}$ (a finite dimensional algebra acting on the right on $P$). Let $B\text{-}\mathrm{fmod}$ denote the category of finite dimensional left $B$-modules. Consider the functor $F:\mathcal C\to B\text{-}\mathrm{fmod}$ given by the formula $F(M)=\operatorname{Hom}(P,M)$.

**Theorem 9.6.4.** The functor $F$ is an equivalence of categories. Thus, any finite abelian category over a field $k$ is equivalent to the category of modules over a finite dimensional $k$-algebra.

The proof of Theorem 9.6.4 is contained in the following problem.

**Problem 9.6.5.** Let $G:B\text{-}\mathrm{fmod}\to\mathcal C$ be the functor defined by $G(X):=P\otimes_B X$, where $P\otimes_B X$ is the cokernel of the morphism $\psi:P\otimes B\otimes X\to P\otimes X$ given by $\psi=a_P\otimes\operatorname{Id}-\operatorname{Id}\otimes a_X$ (where $a_P:P\otimes B\to P$, $a_X:B\otimes X\to X$ are the morphisms representing the actions of $B$ on $P$ and $X$).

(i) Show that $F\circ G\cong\operatorname{Id}$. That is, for every $X\in B\text{-}\mathrm{fmod}$, show that $X$ is naturally isomorphic to $\operatorname{Hom}(P,P\otimes_B X)$. (For this you should only need that $P$ is a nonzero projective object.)

(ii) For any $X\in\mathcal C$, construct a natural morphism

$$
\xi:P\otimes_B\operatorname{Hom}(P,X)\to X,
$$

and show that it is surjective.

(iii) Show that $G\circ F\cong\operatorname{Id}$. To this end, consider the short exact sequence

$$
0\to K\to P\otimes_B\operatorname{Hom}(P,X)\to X\to0,
$$

where the third map is $\xi$. Apply the functor $F$ to this sequence and use (i) to conclude that $K=0$ and hence $\xi$ is an isomorphism. Conclude that the functors $G$ and $F$ are quasi-inverse to each other and hence are equivalences of categories.

## 9.7. Morita equivalence

In this section we will discuss the theory of Morita equivalence of finite dimensional algebras. We note that this theory extends with appropiate changes to the infinite dimensional case.

<span class="original-page-anchor" id="pdf-page-224" aria-hidden="true"></span>

Theorem 9.6.4 shows that a finite abelian category $\mathcal C$ can be identified with the category of finite dimensional modules over a finite dimensional algebra $B$, once we choose a projective generator $P$ of $\mathcal C$. However, the projective generator is not unique. Namely, let $P_1,\ldots,P_m$ be the indecomposable projective objects of $\mathcal C$ (they make sense by Theorem 9.6.4). Then all the projective generators of $\mathcal C$ are the objects of the form $P_{\mathbf n}:=\bigoplus_{i=1}^m n_iP_i$, where $n_i\geq1$ (check it!). Defining $B_{\mathbf n}=B_{\mathbf n}(\mathcal C):=\operatorname{End}(P_{\mathbf n})^{\mathrm{op}}$, we see that the algebras $B_{\mathbf n}$ are all the finite dimensional algebras whose category of finite dimensional modules is equivalent to $\mathcal C$.

**Definition 9.7.1.** Finite dimensional algebras $A$ and $B$ are said to be **Morita equivalent** if the abelian categories $A\text{-}\mathrm{fmod}$ and $B\text{-}\mathrm{fmod}$ are equivalent.

Thus, we obtain that Morita equivalence classes of finite dimensional algebras are the collections of the form $\{B_{\mathbf n}(\mathcal C),\mathbf n\in\mathbb N^m\}$.

Note that the dimension of $B_{\mathbf n}$ is $\sum c_{ij}n_i n_j$, where $(c_{ij})$ is the Cartan matrix of $\mathcal C$. In particular, the algebra $B=B_{\mathbf n}$ with the smallest possible dimension, $\sum c_{ij}$, corresponds to the case when all $n_i=1$, i.e., to the projective generator $P=\bigoplus_i P_i$. It is easy to see that this algebra is the only one of the $B_{\mathbf n}$ for which $B_{\mathbf n}/\operatorname{Rad}(B_{\mathbf n})=\bigoplus_i\operatorname{Mat}_{n_i}(k)$ is commutative.

**Definition 9.7.2.** A finite dimensional algebra $B$ with commutative $B/\operatorname{Rad}(B)$ is called **basic**.

So we have the following corollary of Theorem 9.6.4.

**Corollary 9.7.3.** (i) Any finite abelian category $\mathcal C$ is equivalent to the category of finite dimensional modules over a unique basic algebra $B=B(\mathcal C)$.

(ii) Any finite dimensional algebra $A$ is Morita equivalent to a unique basic algebra $B=B_A$, such that $\dim B_A\leq\dim A$.
