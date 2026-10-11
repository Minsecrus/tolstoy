---
title: "Homological algebra"
description: "《Introduction to Representation Theory》English。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"Introduction to categories","link":"/library/volume-88/original-chapter-007"}
next: {"text":"Structure of finite dimensional algebras","link":"/library/volume-88/original-chapter-009"}
---

# Homological algebra

<span class="original-page-anchor" id="pdf-page-209" aria-hidden="true"></span>

In this chapter we develop some basic homological algebra tools, which are necessary to study the fine structure of representation categories.

## 8.1. Projective and injective modules

Let $A$ be an algebra, and let $P$ be a left $A$-module.

**Theorem 8.1.1.** The following properties of $P$ are equivalent:

(i) If $\alpha:M\to N$ is a surjective morphism and $\nu:P\to N$ is any morphism, then there exists a morphism $\mu:P\to M$ such that $\alpha\circ\mu=\nu$.

(ii) Any surjective morphism $\alpha:M\to P$ splits; i.e., there exists $\mu:P\to M$ such that $\alpha\circ\mu=\operatorname{id}$.

(iii) There exists another $A$-module $Q$ such that $P\oplus Q$ is a free $A$-module, i.e., a direct sum of copies of $A$.

(iv) The functor $\operatorname{Hom}_A(P,?)$ on the category of $A$-modules is exact.

**Proof.** To prove that (i) implies (ii), take $N=P$. To prove that (ii) implies (iii), take $M$ to be free (this can always be done since any module is a quotient of a free module). To prove that (iii) implies (iv), note that the functor $\operatorname{Hom}_A(P,?)$ is exact if $P$ is free (as <span class="original-page-anchor" id="pdf-page-210" aria-hidden="true"></span>$\operatorname{Hom}_A(A,N)=N$), so the statement follows, since if the direct sum of two complexes is exact, then each of them is exact. To prove that (iv) implies (i), let $K$ be the kernel of the map $\alpha$, and apply the exact functor $\operatorname{Hom}_A(P,?)$ to the exact sequence

$$
0\to K\to M\to N\to0.
$$

$\square$

**Definition 8.1.2.** A module satisfying any of the conditions (i)–(iv) of Theorem 8.1.1 is said to be **projective**.

**Problem 8.1.3.** A right $A$-module $M$ is said to be **flat** if the functor $M\otimes_A$ on the category of left $A$-modules is exact.

(i) Show that any projective module is flat.

(ii) Let $A$ be a commutative ring and let $S$ be any multiplicatively closed subset of $A$. Then, the localization $S^{-1}A$ is a flat $A$-module.

(iii) Let $A=\mathbb C[x]$, $M=\mathbb C[x,x^{-1}]$. Show that $M$ is flat but not projective.

**Exercise 8.1.4.** Let $A$ be a ring, let $M_1,M_2$ be left $A$-modules, let $P_1,P_2$ be projective left $A$-modules, and let $f_i:P_i\to M_i$ be homomorphisms. Let $M$ be a left $A$-module containing $M_1$ such that $M/M_1=M_2$. Show that there exists a homomorphism $f:P_1\oplus P_2\to M$ such that $f|_{P_1}=f_1$ and the induced homomorphism $P_2\to M_2$ is $f_2$.

There is also a notion of an injective module, which is dual to the notion of a projective module. Namely, we have the following theorem.

Let $A$ be an algebra and let $I$ be a left $A$-module.

**Theorem 8.1.5.** The following properties of $I$ are equivalent:

(i) If $\alpha:N\to M$ is an injective morphism and $\nu:N\to I$ is any morphism, then there exists a morphism $\mu:M\to I$ such that $\mu\circ\alpha=\nu$.

(ii) Any injective morphism $\alpha:I\to M$ splits; i.e., there exists $\mu:M\to I$ such that $\mu\circ\alpha=\operatorname{id}$.

<span class="original-page-anchor" id="pdf-page-211" aria-hidden="true"></span>

(iii) The functor $\operatorname{Hom}_A(?,I)$ on the category of $A$-modules is exact.

**Proof.** The proof of the implications “(i) implies (ii)” and “(iii) implies (i)” is similar to the proof of Theorem 8.1.1. Let us prove that (ii) implies (iii). Let

$$
0\to N\to M\to K\to0
$$

be an exact sequence. Denote the embedding $N\to M$ by $j$. Consider the corresponding sequence

$$
0\to\operatorname{Hom}(K,I)\to\operatorname{Hom}(M,I)\to\operatorname{Hom}(N,I)\to0.
$$

Let $f\in\operatorname{Hom}(N,I)$, and define the module $E:=(M\oplus I)/N$, where $N$ is embedded into $M\oplus I$ via $x\mapsto(j(x),-f(x))$. Clearly, we have an inclusion $I\to E$, since the image of $N\oplus I$ in $E$ is naturally identified with $I$. So there is a splitting $E\to I$ of this inclusion, i.e., a map $M\oplus I\to I$, $(m,i)\mapsto g(m)+i$ such that $g(j(x))-f(x)=0$. This means that the map $j^*:\operatorname{Hom}(M,I)\to\operatorname{Hom}(N,I)$ is surjective, i.e., the functor $\operatorname{Hom}(?,I)$ is exact, as desired. $\square$

**Definition 8.1.6.** A module satisfying any of the conditions (i)–(iii) of Theorem 8.1.5 is said to be **injective**.

**Example 8.1.7.** Let $A$ be an algebra and $P$ be a left $A$-module. Then $P$ is projective if and only if $P^*$ is an injective right $A$-module.

Theorem 8.1.1(iv) and Theorem 8.1.5(iii) can be used to define a projective and an injective object in any abelian category. Namely, we make the following definition.

**Definition 8.1.8.** A **projective object** in an abelian category $\mathcal C$ is an object $P$ such that the functor $\operatorname{Hom}_{\mathcal C}(P,?)$ is exact.

An **injective object** in an abelian category $\mathcal C$ is an object $I$ such that the functor $\operatorname{Hom}_{\mathcal C}(?,I)$ is exact.

## 8.2. Tor and Ext functors

Let $A$ be a unital ring. As we have mentioned in Example 7.9.6, the functors $M\otimes_A?$ and $\operatorname{Hom}_A(M,?)$ (where $M$ is a right, respectively <span class="original-page-anchor" id="pdf-page-212" aria-hidden="true"></span>left, $A$-module) on the category of left $A$-modules are, in general, not exact (they are only exact on one side). The job of the functors $\operatorname{Tor}_i^A(M,?)$ and $\operatorname{Ext}_A^i(M,?)$ is to quantify the extent to which the functors $M\otimes_A?$ and $\operatorname{Hom}_A(M,?)$ fail to be exact. Namely, these functors are defined as follows.

**Definition 8.2.1.** A **projective resolution** of $M$ is an exact sequence

$$
\cdots\to P_2\to P_1\to P_0\to M\to0
$$

such that all modules $P_i$, $i\geq0$, are projective.

**Exercise 8.2.2.** Show that any module has a projective resolution (for example, one consisting of free modules).

**Definition 8.2.3.** Let $M$ be a right $A$-module, $P_\bullet$ a projective resolution of $M$, and $N$ a left $A$-module. For $i\geq0$ we define $\operatorname{Tor}_i^A(M,N)=\operatorname{Tor}_i(M,N)$ to be the $i$th cohomology of the complex

$$
\cdots\to P_2\otimes_A N\to P_1\otimes_A N\to P_0\otimes_A N\to0
$$

induced by the resolution $P_\bullet$.

**Definition 8.2.4.** Let $M$ be a left $A$-module, $P_\bullet$ a projective resolution of $M$, and $N$ a left $A$-module. For $i\geq0$ we define $\operatorname{Ext}_A^i(M,N)=\operatorname{Ext}^i(M,N)$ to be the $i$th cohomology of the complex

$$
0\to\operatorname{Hom}_A(P_0,N)\to\operatorname{Hom}_A(P_1,N)\to\operatorname{Hom}_A(P_2,N)\to\cdots
$$

induced by the resolution $P_\bullet$.

**Problem 8.2.5.** In this problem we will show that the cohomology groups $\operatorname{Tor}_i$ and $\operatorname{Ext}^i$ don't really depend on the projective resolution $P_\bullet$, in a fairly strong sense, which justifies the fact that we don't mention $P_\bullet$ in the notation for them.

Let $P_\bullet,Q_\bullet$ be two projective resolutions of $M$. Let $d_i^P:P_i\to P_{i-1}$, $d_i^Q:Q_i\to Q_{i-1}$ be the corresponding differentials; in particular, $d_0^P:P_0\to M$, $d_0^Q:Q_0\to M$.

(i) Show that there exists a homomorphism $f_0:P_0\to Q_0$ such that $d_0^Q\circ f_0=d_0^P$.

(ii) Proceed to show by induction in $j$ that there exists a homomorphism $f_j:P_j\to Q_j$ such that $d_j^Q\circ f_j=f_{j-1}\circ d_j^P$.

<span class="original-page-anchor" id="pdf-page-213" aria-hidden="true"></span>

The collection of homomorphisms satisfying the conditions of (i) and (ii) is called a **morphism of resolutions**, $f:P_\bullet\to Q_\bullet$.

(iii) Clearly, such a morphism $f$ defines a linear map $\psi_i(P,Q,f):\operatorname{Tor}_i^P(M,N)\to\operatorname{Tor}_i^Q(M,N)$, where the superscripts $P$ and $Q$ mean that the Tor groups are defined using the resolutions $P_\bullet$ and $Q_\bullet$. Show that the maps $\psi_i(P,Q,f)$ don't really depend on $f$ (so they can be denoted by $\psi_i(P,Q)$).

(iv) Deduce that $\psi_i(P,Q)$ are isomorphisms (use that $\psi_i(P,P)=\operatorname{id}$ and $\psi_i(Q,R)\circ\psi_i(P,Q)=\psi_i(P,R)$).

(v) Define similar maps $\xi_i(Q,P,f):\operatorname{Ext}_P^i(M,N)\to\operatorname{Ext}_Q^i(M,N)$ and show that they are independent on $f$ and are isomorphisms.

**Problem 8.2.6.** (i) Show that $\operatorname{Tor}_0(M,N)=M\otimes_A N$ and that $\operatorname{Ext}^0(M,N)=\operatorname{Hom}_A(M,N)$.

(ii) Show that the group $\operatorname{Ext}^1(M,N)$ as defined here is canonically isomorphic to the one defined in Problem 3.9.1.

(iii) Let

$$
0\to N_1\to N_2\to N_3\to0
$$

be a short exact sequence of left $A$-modules.

Show that there are long exact sequences

$$
\begin{aligned}
0&\to\operatorname{Hom}_A(M,N_1)\to\operatorname{Hom}_A(M,N_2)\to\operatorname{Hom}_A(M,N_3)\to{}\\
&\operatorname{Ext}^1(M,N_1)\to\operatorname{Ext}^1(M,N_2)\to\operatorname{Ext}^1(M,N_3)\to\operatorname{Ext}^2(M,N_1)\to\cdots
\end{aligned}
$$

and

$$
\begin{aligned}
\cdots&\to\operatorname{Tor}_2(M,N_3)\to\operatorname{Tor}_1(M,N_1)\to\operatorname{Tor}_1(M,N_2)\to\operatorname{Tor}_1(M,N_3)\\
&\to M\otimes_A N_1\to M\otimes_A N_2\to M\otimes_A N_3\to0.
\end{aligned}
$$

This shows that, as we mentioned above, the Tor and Ext groups “quantify” the extent to which the functors $M\otimes_A$ and $\operatorname{Hom}_A(M,?)$ are not exact.

Hint: Use Problem 7.8.5.

(iv) Show that $\operatorname{Tor}_i^A(M,N)$ can be computed by taking a projective resolution of $N$, tensoring it with $M$, and computing cohomology.

<span class="original-page-anchor" id="pdf-page-214" aria-hidden="true"></span>

Hint: Show first that $\operatorname{Tor}_i^A(M,N)$ can be computed by tensoring two projective resolutions, for $M$ and for $N$, and computing cohomology.

(v) Let $0\to M_1\to M_2\to M_3\to0$ be a short exact sequence of left $A$-modules. Let $P_\bullet^1$ and $P_\bullet^3$ be projective resolutions of $M_1$ and $M_3$. Construct a projective resolution of $M_2$ with terms $P_i^2:=P_i^1\oplus P_i^3$ (use Exercise 8.1.4). Use it to show that for any left $A$-module $N$ there are long exact sequences

$$
\begin{aligned}
0&\to\operatorname{Hom}_A(M_3,N)\to\operatorname{Hom}_A(M_2,N)\to\operatorname{Hom}_A(M_1,N)\to{}\\
&\operatorname{Ext}^1(M_3,N)\to\operatorname{Ext}^1(M_2,N)\to\operatorname{Ext}^1(M_1,N)\to\operatorname{Ext}^2(M_3,N)\to\cdots
\end{aligned}
$$

and

$$
\begin{aligned}
\cdots&\to\operatorname{Tor}_2(M_3,N)\to\operatorname{Tor}_1(M_1,N)\to\operatorname{Tor}_1(M_2,N)\to\operatorname{Tor}_1(M_3,N)\\
&\to M_1\otimes_A N\to M_2\otimes_A N\to M_3\otimes_A N\to0.
\end{aligned}
$$

**Problem 8.2.7.** (i) Let $A=\mathbb Z$ and let $M,N$ be finitely generated abelian groups. Compute $\operatorname{Tor}_i(M,N)$, $\operatorname{Ext}^i(M,N)$. (Hint: Reduce to the case of cyclic groups using the classification theorem for finite abelian groups.)

(ii) Do the same for $A=k[x]$ and $M,N$ being any finitely generated $A$-modules.

**Problem 8.2.8.** Show that if $A_1,A_2$ are algebras over a field $k$ and $M_i,N_i$ are left $A_i$-modules, then

$$
\operatorname{Tor}_i^{A_1\otimes A_2}(M_1\otimes M_2,N_1\otimes N_2)=\bigoplus_{j+m=i}\operatorname{Tor}_j^{A_1}(M_1,N_1)\otimes\operatorname{Tor}_m^{A_2}(M_2,N_2).
$$

Similarly,

$$
\operatorname{Ext}_{A_1\otimes A_2}^i(M_1\otimes M_2,N_1\otimes N_2)=\bigoplus_{j+m=i}\operatorname{Ext}_{A_1}^j(M_1,N_1)\otimes\operatorname{Ext}_{A_2}^m(M_2,N_2),
$$

if $N_i$ are finite dimensional.

In a similar way one can define Tor and Ext groups in any abelian category which has **enough projectives**; i.e., any object is a quotient of a projective object (this condition insures that every object has a projective resolution).

<span class="original-page-anchor" id="pdf-page-215" aria-hidden="true"></span>

**Exercise 8.2.9.** (i) Show that the category of finite abelian groups or finite dimensional $k[x]$-modules does not contain nonzero projective objects (so it does not have enough projectives).

(ii) Let $A$ be a finitely generated commutative ring. Show that the category of finitely generated $A$-modules has enough projectives.

**Problem 8.2.10.** Let $V$ be a finite dimensional vector space over a field $k$. Let $C_i=SV\otimes\wedge^i V$. We can view $C_i$ as the space of polynomial functions on $V^*$ with values in $\wedge^i V$. Define the differential $d_i:C_i\to C_{i-1}$ by the formula

$$
d_i(f)(u)=\iota_u f(u),\qquad u\in V^*,
$$

where $\iota_u:\wedge^i V\to\wedge^{i-1}V$ is the contraction defined by the formula

$$
\iota_u(v_1\wedge\cdots\wedge v_i)=\sum_{j=1}^i(-1)^j u(v_j)v_1\wedge\cdots\widehat v_j\cdots\wedge v_i.
$$

(i) Show that $C_\bullet$ is a projective (in fact, free) resolution of $k$ (with trivial action of $V$) as an $SV$-module. (It is called the **Koszul resolution**.)

(ii) Let $V=U\oplus W$. Then we can view $SW$ as an $SV$-module ($U$ acts by zero). Construct a resolution of $SW$ by free $SV$-modules whose terms are $C_i=SV\otimes\wedge^i U$.

Hint: Tensor the Koszul resolution of $k$ as an $SU$-module by $SW$.

(iii) Regard $SV$ as an $S(V\oplus V)=SV\otimes SV$-module using left and right multiplication. Construct a free resolution of $SV$ as an $SV\otimes SV$-module with terms $C_i=SV\otimes\wedge^i V\otimes SV$ (called the Koszul bimodule resolution).

(iv) By tensoring the resolution of (iii) over $SV$ with any $SV$-module $M$, construct a projective (in fact, free) resolution $P_\bullet$ of $M$ with $P_i=0$ for $i>\dim V$. Deduce that for any $SV$-module $N$ and any $i>\dim V$, one has

$$
\operatorname{Tor}_i^{SV}(M,N)=\operatorname{Ext}_{SV}^i(M,N)=0
$$

(the **Hilbert syzygies theorem**).

(v) Compute $\operatorname{Ext}_{SV}^i(k,k)$ and $\operatorname{Tor}_i^{SV}(k,k)$.
