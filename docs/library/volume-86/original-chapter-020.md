---
title: "Chapter XX: General Homology Theory"
description: "Serge Lang《Algebra》English。"
pageClass: algebra-reading
prev: {"text":"Part Four: Homological Algebra","link":"/library/volume-86/original-part-04"}
next: {"text":"Chapter XXI: Finite Free Resolutions","link":"/library/volume-86/original-chapter-021"}
---

# Chapter XX: General Homology Theory

<span class="original-page-anchor" id="pdf-page-769" aria-hidden="true"></span>

To a large extent the present chapter is arrow-theoretic. There is a substantial body of linear algebra which can be formalized very systematically, and constitutes what Steenrod called abstract nonsense, but which provides a well-oiled machinery applicable to many domains. References will be given along the way.

Most of what we shall do applies to abelian categories, which were mentioned in Chapter III, end of §3. However, in first reading, I recommend that readers disregard any allusions to general abelian categories and assume that we are dealing with an abelian category of modules over a ring, or other specific abelian categories such as complexes of modules over a ring.

## §1. Complexes

Let $A$ be a ring. By an **open complex** of $A$-modules, one means a sequence of modules and homomorphisms $\{(E^i,d^i)\}$,

$$
\to E^{i-1}\xrightarrow{d^{i-1}}E^i\xrightarrow{d^i}E^{i+1}\to
$$

where $i$ ranges over all integers and $d_i$ maps $E^i$ into $E^{i+1}$, and such that

$$
d^i\circ d^{i-1}=0
$$

for all $i$.

One frequently considers a finite sequence of homomorphisms, say

$$
E^1\to\cdots\to E^r
$$

<span class="original-page-anchor" id="pdf-page-770" aria-hidden="true"></span>

such that the composite of two successive ones is $0$, and one can make this sequence into a complex by inserting $0$ at each end:

$$
\to0\to0\to E^1\to\cdots\to E^r\to0\to0\to
$$

Such a complex is called a **finite** or **bounded** complex.

**Remark.** Complexes can be indexed with a descending sequence of integers, namely,

$$
\to E_{i+1}\xrightarrow{d_{i+1}}E_i\xrightarrow{d_i}E_{i-1}\to
$$

When that notation is used systematically, then one uses upper indices for complexes which are indexed with an ascending sequence of integers:

$$
\to E^{i-1}\xrightarrow{d^{i-1}}E^i\xrightarrow{d^i}E^{i+1}\to
$$

In this book, I shall deal mostly with ascending indices.

As stated in the introduction of this chapter, instead of modules over a ring, we could have taken objects in an arbitrary abelian category.

The homomorphisms $d^i$ are often called **differentials**, because some of the first complexes which arose in practice were in analysis, with differential operators and differential forms. *Cf.* the examples below.

We denote a complex as above by $(E,d)$. If the complex is exact, it is often useful to insert the kernels and cokernels of the differentials in a diagram as follows, letting $M_i=\operatorname{Ker}d^i=\operatorname{Im}d^{i-1}$.

![An exact complex and its kernels and cokernels](/library/volume-86/diagrams/pdf-0770-exact-complex.png)

Thus by definition, we obtain a family of short exact sequences

$$
0\to M^i\to E^i\to M^{i+1}\to0.
$$

If the complex is not exact, then of course we have to insert both the image of $d^{i-1}$ and the kernel of $d^i$. The factor

$$
(\operatorname{Ker}d^i)/(\operatorname{Im}d^{i-1})
$$

will be studied in the next section. It is called the **homology of the complex**, and measures the deviation from exactness.

<span class="original-page-anchor" id="pdf-page-771" aria-hidden="true"></span>

Let $M$ be a module. By a **resolution** of $M$ we mean an exact sequence

$$
\to E_n\to E_{n-1}\to\cdots\to E_0\to M\to0.
$$

Thus a resolution is an exact complex whose furthest term on the right before $0$ is $M$. The resolution is indexed as shown. We usually write $E_M$ for the part of complex formed only of the $E_i$'s, thus:

$$
E_M\text{ is:}\quad\to E_n\to E_{n-1}\to\cdots\to E_0,
$$

stopping at $E_0$. We then write $E$ for the complex obtained by sticking $0$ on the right:

$$
E\text{ is:}\quad\to E_n\to E_{n-1}\to\cdots\to E_0\to0.
$$

If the objects $E_i$ of the resolution are taken in some family, then the resolution is qualified in the same way as the family. For instance, if $E_i$ is free for all $i\geqq0$ then we say that the **resolution is a free resolution**. If $E_i$ is projective for all $i\geqq0$ then we say that the **resolution is projective**. And so forth. The same terminology is applied to the right, with a resolution

$$
0\to M\to E^0\to E^1\to\cdots\to E^{n-1}\to E^n\to,
$$

also written

$$
0\to M\to E_M.
$$

We then write $E$ for the complex

$$
0\to E^0\to E^1\to E^2\to\cdots.
$$

See §5 for injective resolutions.

A resolution is said to be **finite** if $E_i$ (or $E^i$) $=0$ for all but a finite number of indices $i$.

**Example.** Every module admits a free resolution (on the left). This is a simple application of the notion of free module. Indeed, let $M$ be a module, and let $\{x_j\}$ be a family of generators, with $j$ in some indexing set $J$. For each $j$ let $Re_j$ be a free module over $R$ with a basis consisting of one element $e_j$. Let

$$
F=\bigoplus_{j\in J}Re_j
$$

be their direct sum. There is a unique epimorphism

$$
F\to M\to0
$$

sending $e_j$ on $x_j$. Now we let $M_1$ be the kernel, and again represent $M_1$ as the quotient of a free module. Inductively, we can construct the desired free resolution.

<span class="original-page-anchor" id="pdf-page-772" aria-hidden="true"></span>

**Example. The Standard Complex.** Let $S$ be a set. For $i=0,1,2,\ldots$ let $E_i$ be the free module over $\mathbf Z$ generated by $(i+1)$-tuples $(x_0,\ldots,x_i)$ with $x_0,\ldots,x_i\in S$. Thus such $(i+1)$-tuples form a basis of $E_i$ over $\mathbf Z$. There is a unique homomorphism

$$
d_{i+1}:E_{i+1}\to E_i
$$

such that

$$
d_{i+1}(x_0,\ldots,x_{i+1})=\sum_{j=0}^{i+1}(-1)^j(x_0,\ldots,\widehat{x_j},\ldots,x_{i+1}),
$$

where the symbol $\widehat{x_j}$ means that this term is to be omitted. For $i=0$, we define $d_0:E_0\to\mathbf Z$ to be the unique homomorphism such that $d_0(x_0)=1$. The map $d_0$ is sometimes called the **augmentation**, and is also denoted by $\varepsilon$. Then we obtain a resolution of $\mathbf Z$ by the complex

$$
\to E_{i+1}\to E_i\to\cdots\to E_0\xrightarrow{\varepsilon}\mathbf Z\to0.
$$

The formalism of the above maps $d_i$ is pervasive in mathematics. See Exercise 2 for the use of the standard complex in the cohomology theory of groups. For still another example of this same formalism, compare with the Koszul complex in Chapter XXI, §4.

Given a module $M$, one may form $\operatorname{Hom}(E_i,M)$ for each $i$, in which case one gets coboundary maps

$$
\delta^i:\operatorname{Hom}(E_i,M)\to\operatorname{Hom}(E_{i+1},M),\qquad\delta(f)=f\circ d^{i+1},
$$

obtained by composition of mappings. This procedure will be used to obtain derived functors in §6. In Exercises 2 through 6, you will see how this procedure is used to develop the cohomology theory of groups.

Instead of using homomorphisms, one may use a topological version with simplices, and continuous maps, in which case the standard complex gives rise to the singular homology theory of topological spaces. See [GreH 81], Chapter 9.

**Examples. Finite free resolutions.** In Chapter XXI, you will find other examples of complexes, especially finite free, constructed in various ways with different tools. This subsequent entire chapter may be viewed as providing examples for the current chapter.

**Examples with differential forms.** In Chapter XIX, §3, we gave the example of the de Rham complex in an algebraic setting. In the theory of differential manifolds, the de Rham complex has differential maps

$$
d^i:\Omega^i\to\Omega^{i+1},
$$

sending differential forms of degree $i$ to those of degree $i+1$, and allows for the computation of the homology of the manifold.

A similar situation occurs in complex differential geometry, when the maps $d^i$ are given by the **Dolbeault** $\bar\partial$-operators

$$
\bar\partial^i:\Omega^{p,i}\to\Omega^{p,i+1}
$$

<span class="original-page-anchor" id="pdf-page-773" aria-hidden="true"></span>

operating on forms of type $(p,i)$. Interested readers can look up for instance Gunning's book [Gu 90] mentioned in the introduction to Part IV, Volume I, E. The associated homology of this complex is called the **Dolbeault** or **$\bar\partial$-cohomology** of the complex manifold.

Let us return to the general algebraic aspects of complexes and resolutions.

It is an interesting problem to discuss which modules admit finite resolutions, and variations on this theme. Some conditions are discussed later in this chapter and in Chapter XXI. If a resolution

$$
0\to E_n\to E_{n-1}\to\cdots\to E_0\to M\to0
$$

is such that $E_m=0$ for $m>n$, then we say that the resolution has **length $\leqq n$** (sometimes we say it has **length $n$** by abuse of language).

A **closed complex** of $A$-modules is a sequence of modules and homomorphisms $\{(E^i,d^i)\}$ where $i$ ranges over the set of integers mod $n$ for some $n\geqq2$ and otherwise satisfying the same properties as above. Thus a closed complex looks like this:

![A closed complex](/library/volume-86/diagrams/pdf-0773-closed-complex.png)

We call $n$ the **length** of the closed complex.

Without fear of confusion, one can omit the index $i$ on $d^i$ and write just $d$. We also write $(E,d)$ for the complex $\{(E^i,d^i)\}$, or even more briefly, we write simply $E$.

Let $(E,d)$ and $(E',d')$ be complexes (both open or both closed). Let $r$ be an integer. A **morphism** or **homomorphism** (of complexes)

$$
f:(E',d')\to(E,d)
$$

of **degree $r$** is a sequence

$$
f_i:E'^i\to E^{i+r}
$$

of homomorphisms such that for all $i$ the following diagram is commutative:

![The commutative square defining a morphism of degree r](/library/volume-86/diagrams/pdf-0773-degree-r-morphism.png)

Just as we write $d$ instead of $d^i$, we shall also write $f$ instead of $f_i$. If the complexes are closed, we define a morphism from one into the other only if they have the same length.

It is clear that complexes form a category. In fact they form an abelian category. Indeed, say we deal with complexes indexed by $\mathbf Z$ for simplicity, and morphisms of degree $0$. Say we have a morphism of complexes $f:C\to C''$ or <span class="original-page-anchor" id="pdf-page-774" aria-hidden="true"></span>putting the indices:

![A morphism of complexes with indices](/library/volume-86/diagrams/pdf-0774-complex-kernel.png)

We let $C'_n=\operatorname{Ker}(C_n\to C''_n)$. Then the family $(C'_n)$ forms a complex, which we define to be the kernel of $f$. We let the reader check the details that this and a similar definition for cokernel and finite direct sums make complexes of modules into an abelian category. At this point, readers should refer to Chapter III, §9, where kernels and cokernels are discussed in this context. The snake lemma of that chapter will now become central to the next section.

It will be useful to have another notion to deal with objects indexed by a monoid. Let $G$ be a monoid, which we assume commutative and additive to fit the applications we have in mind here. Let $\{M_i\}_{i\in G}$ be a family of modules indexed by $G$. The direct sum

$$
M=\bigoplus_{i\in G}M_i
$$

will be called the **$G$-graded module associated with the family $\{M_i\}_{i\in G}$**. Let $\{M_i\}_{i\in G}$ and $\{M'_i\}_{i\in G}$ be families indexed by $G$, and let $M,M'$ be their associated $G$-graded modules. Let $r\in G$. By a **$G$-graded morphism** $f:M'\to M$ of degree $r$ we shall mean a homomorphism such that $f$ maps $M'_i$ into $M_{i+r}$ for each $i\in G$ (identifying $M'_i$ with the corresponding submodule of the direct sum on the $i$-th component). Thus $f$ is nothing else than a family of homomorphisms $f_i:M'_i\to M_{i+r}$.

If $(E,d)$ is a complex we may view $E$ as a $G$-graded module (taking the direct sum of the components of the complex), and we may view $d$ as a $G$-graded morphism of degree $1$, letting $G$ be $\mathbf Z$ or $\mathbf Z/n\mathbf Z$. The most common case we encounter is when $G=\mathbf Z$. Then we write the complex as

$$
E=\bigoplus E_i,\quad\text{and}\quad d:E\to E
$$

maps $E$ into itself. The differential $d$ is defined as $d_i$ on each direct summand $E_i$, and has degree $1$.

Conversely, if $G$ is $\mathbf Z$ or $\mathbf Z/n\mathbf Z$, one may view a $G$-graded module as a complex, by defining $d$ to be the zero map.

For simplicity, we shall often omit the prefix “$G$-graded” in front of the word “morphism”, when dealing with $G$-graded morphisms.

<span class="original-page-anchor" id="pdf-page-775" aria-hidden="true"></span>

## §2. Homology Sequence

Let $(E,d)$ be a complex. We let

$$
Z^i(E)=\operatorname{Ker}d^i
$$

and call $Z^i(E)$ the module of **$i$-cycles**. We let

$$
B^i(E)=\operatorname{Im}d^{i-1}
$$

and call $B^i(E)$ the module of **$i$-boundaries**. We frequently write $Z^i$ and $B^i$ instead of $Z^i(E)$ and $B^i(E)$, respectively. We let

$$
H^i(E)=Z^i/B^i=\operatorname{Ker}d^i/\operatorname{Im}d^{i-1},
$$

and call $H^i(E)$ the $i$-th **homology group** of the complex. The graded module associated with the family $\{H^i\}$ will be denoted by $H(E)$, and will be called the **homology** of $E$. One sometimes writes $H^*(E)$ instead of $H(E)$.

If $f:E'\to E$ is a morphism of complexes, say of degree $0$, then we get an **induced canonical homomorphism**

$$
H^i(f):H^i(E')\to H^i(E)
$$

on each homology group. Indeed, from the commutative diagram defining a morphism of complexes, one sees at once that $f$ maps $Z^i(E')$ into $Z^i(E)$ and $B^i(E')$ into $B^i(E)$, whence the induced homomorphism $H^i(f)$. Compare with the beginning remarks of Chapter III, §9. One often writes this induced homomorphism as $f_{i*}$ rather than $H_i(f)$, and if $H(E)$ denotes the graded module of homology as above, then we write

$$
H(f)=f_*:H(E')\to H(E).
$$

We call $H(f)$ the map **induced** by $f$ on homology. If $H^i(f)$ is an isomorphism for all $i$, then we say that $f$ is a **homology isomorphism**.

Note that if $f:E'\to E$ and $g:E\to E''$ are morphisms of complexes, then it is immediately verified that

$$
H(g)\circ H(f)=H(g\circ f)\quad\text{and}\quad H(\mathrm{id})=\mathrm{id}.
$$

Thus $H$ is a functor from the category of complexes to the category of graded modules.

We shall consider short exact sequences of complexes with morphisms of degree $0$:

$$
0\to E'\xrightarrow{f}E\xrightarrow{g}E''\to0,
$$

<span class="original-page-anchor" id="pdf-page-776" aria-hidden="true"></span>

which written out in full look like this:

![A short exact sequence of complexes written out](/library/volume-86/diagrams/pdf-0776-short-exact-complexes.png)

*One can define a morphism*

$$
\delta:H(E'')\to H(E')
$$

*of degree $1$, in other words, a family of homomorphisms*

$$
\delta^i:H''^i\to H'^{(i+1)}
$$

*by the snake lemma.*

**Theorem 2.1.** *Let*

$$
0\to E'\xrightarrow{f}E\xrightarrow{g}E''\to0
$$

*be an exact sequence of complexes with $f,g$ of degree $0$. Then the sequence*

![The exact homology sequence](/library/volume-86/diagrams/pdf-0776-homology-triangle.png)

*is exact.*

This theorem is merely a special application of the snake lemma.

If one writes out in full the homology sequence in the theorem, then it looks like this:

$$
\xrightarrow{\delta}H'^i\to H^i\to H''^i\xrightarrow{\delta}H'^{(i+1)}\to H^{i+1}\to H''^{(i+1)}\xrightarrow{\delta}
$$

<span class="original-page-anchor" id="pdf-page-777" aria-hidden="true"></span>

It is clear that our map $\delta$ is functorial (in an obvious sense), and hence that our whole structure $(H,\delta)$ is a functor from the category of short exact sequences of complexes into the category of complexes.

## §3. Euler Characteristic and the Grothendieck Group

This section may be viewed as a continuation of Chapter III, §8, on Euler-Poincaré maps. Consider complexes of $A$-modules, for simplicity.

Let $E$ be a complex such that almost all homology groups $H^i$ are equal to $0$. Assume that $E$ is an open complex. As in Chapter III, §8, let $\varphi$ be an Euler-Poincaré mapping on the category of modules (i.e. $A$-modules). We define the **Euler-Poincaré characteristic** $\chi_\varphi(E)$ (or more briefly the **Euler characteristic**) with respect to $\varphi$, to be

$$
\chi_\varphi(E)=\sum(-1)^i\varphi(H^i)
$$

provided $\varphi(H^i)$ is defined for all $H^i$, in which case we say that $\chi_\varphi$ **is defined** for the complex $E$.

If $E$ is a closed complex, we select a definite order $(E^1,\ldots,E^n)$ for the integers mod $n$ and define the Euler characteristic by the formula

$$
\chi_\varphi(E)=\sum_{i=1}^n(-1)^i\varphi(H^i)
$$

provided again all $\varphi(H^i)$ are defined.

For an example, the reader may refer to Exercise 28 of Chapter I.

One may view $H$ as a complex, defining $d$ to be the zero map. In that case, we see that $\chi_\varphi(H)$ is the alternating sum given above. More generally:

**Theorem 3.1.** *Let $F$ be a complex, which is of even length if it is closed. Assume that $\varphi(F^i)$ is defined for all $i$, $\varphi(F^i)=0$ for almost all $i$, and $H^i(F)=0$ for almost all $i$. Then $\chi_\varphi(F)$ is defined, and*

$$
\chi_\varphi(F)=\sum_i(-1)^i\varphi(F^i).
$$

*Proof.* Let $Z^i$ and $B^i$ be the groups of $i$-cycles and $i$-boundaries in $F^i$ respectively. We have an exact sequence

$$
0\to Z^i\to F^i\to B^{i+1}\to0.
$$

Hence $\chi_\varphi(F)$ is defined, and

$$
\varphi(F^i)=\varphi(Z^i)+\varphi(B^{i+1}).
$$

<span class="original-page-anchor" id="pdf-page-778" aria-hidden="true"></span>

Taking the alternating sum, our conclusion follows at once.

A complex whose homology is trivial is called **acyclic**.

**Corollary 3.2.** *Let $F$ be an acyclic complex, such that $\varphi(F^i)$ is defined for all $i$, and equal to $0$ for almost all $i$. If $F$ is closed, we assume that $F$ has even length. Then*

$$
\chi_\varphi(F)=0.
$$

In many applications, an open complex $F$ is such that $F^i=0$ for almost all $i$, and one can then treat this complex as a closed complex by defining an additional map going from a zero on the far right to a zero on the far left. Thus in this case, the study of such an open complex is reduced to the study of a closed complex.

**Theorem 3.3.** *Let*

$$
0\to E'\to E\to E''\to0
$$

*be an exact sequence of complexes, with morphisms of degree $0$. If the complexes are closed, assume that their length is even. Let $\varphi$ be an Euler-Poincaré mapping on the category of modules. If $\chi_\varphi$ is defined for two of the above three complexes, then it is defined for the third, and we have*

$$
\chi_\varphi(E)=\chi_\varphi(E')+\chi_\varphi(E'').
$$

*Proof.* We have an exact homology sequence

$$
\to H''^{(i-1)}\to H'^i\to H^i\to H''^i\to H'^{(i+1)}\to
$$

This homology sequence is nothing but a complex whose homology is trivial. Furthermore, each homology group belonging say to $E$ is between homology groups of $E'$ and $E''$. Hence if $\chi_\varphi$ is defined for $E'$ and $E''$ it is defined for $E$. Similarly for the other two possibilities. If our complexes are closed of even length $n$, then this homology sequence has even length $3n$. We can therefore apply the corollary of Theorem 3.1 to get what we want.

For certain applications, it is convenient to construct a universal Euler mapping. Let $\mathfrak A$ be the set of isomorphism classes of certain modules. If $E$ is a module, let $[E]$ denote its isomorphism class. We require that $\mathfrak A$ satisfy the **Euler-Poincaré condition**, i.e. if we have an exact sequence

$$
0\to E'\to E\to E''\to0,
$$

then $[E]$ is in $\mathfrak A$ if and only if $[E']$ and $[E'']$ are in $\mathfrak A$. Furthermore, the zero module is in $\mathfrak A$.

<span class="original-page-anchor" id="pdf-page-779" aria-hidden="true"></span>

**Theorem 3.4.** *Assume that $\mathfrak A$ satisfies the Euler-Poincaré condition. Then there is a map*

$$
\gamma:\mathfrak A\to\mathbf K(\mathfrak A)
$$

*of $\mathfrak A$ into an abelian group $\mathbf K(\mathfrak A)$ having the universal property with respect to Euler-Poincaré maps defined on $\mathfrak A$.*

To construct this, let $F_{\mathrm{ab}}(\mathfrak A)$ be the free abelian group generated by the set of such $[E]$. Let $B$ be the subgroup generated by all elements of type

$$
[E]-[E']-[E''],
$$

where

$$
0\to E'\to E\to E''\to0
$$

is an exact sequence whose members are in $\mathfrak A$. We let $\mathbf K(\mathfrak A)$ be the factor group $F_{\mathrm{ab}}(\mathfrak A)/B$, and let $\gamma:\mathfrak A\to\mathbf K(\mathfrak A)$ be the natural map. It is clear that $\gamma$ has the universal property.

We observe the similarity of construction with the Grothendieck group of a monoid. In fact, the present group is known as the **Euler-Grothendieck group** of $\mathfrak A$, with Euler usually left out.

The reader should observe that the above arguments are valid in abelian categories, although we still used the word **module**. Just as with the elementary isomorphism theorems for groups, we have the analogue of the Jordan-Hölder theorem for modules. Of course in the case of modules, we don't have to worry about the normality of submodules.

We now go a little deeper into **K**-theory. Let $\mathfrak A$ be an abelian category. In first reading, one may wish to limit attention to an abelian category of modules over a ring. Let $\mathfrak C$ be a family of objects in $\mathfrak A$. We shall say that $\mathfrak C$ is a **K-family** if it satisfies the following conditions.

**K 1.** $\mathfrak C$ is closed under taking finite direct sums, and $0$ is in $\mathfrak C$.

**K 2.** Given an object $E$ in $\mathfrak A$ there exists an epimorphism

$$
L\to E\to0
$$

with $L$ in $\mathfrak C$.

**K 3.** Let $E$ be an object admitting a finite resolution of length $n$

$$
0\to L_n\to\cdots\to L_0\to E\to0
$$

with $L_i\in\mathfrak C$ for all $i$. If

$$
0\to N\to F_{n-1}\to\cdots\to F_0\to E\to0
$$

is a resolution with $N$ in $\mathfrak A$ and $F_0,\ldots,F_{n-1}$ in $\mathfrak C$, then $N$ is also in $\mathfrak C$.

<span class="original-page-anchor" id="pdf-page-780" aria-hidden="true"></span>

We note that it follows from these axioms that if $F$ is in $\mathfrak C$ and $F'$ is isomorphic to $F$, then $F'$ is also in $\mathfrak C$, as one sees by looking at the resolution

$$
0\to F'\to F\to0\to0
$$

and applying **K 3**. Furthermore, given an exact sequence

$$
0\to F'\to F\to F''\to0
$$

with $F$ and $F''$ in $\mathfrak C$, then $F'$ is in $\mathfrak C$, again by applying **K 3**.

**Example.** One may take for $\mathfrak A$ the category of modules over a commutative ring, and for $\mathfrak C$ the family of projective modules. Later we shall also consider Noetherian rings, in which case one may take finite modules, and finite projective modules instead. Condition **K 2** will be discussed in §8.

From now on we assume that $\mathfrak C$ is a **K-family**. For each object $E$ in $\mathfrak A$, we let $[E]$ denote its isomorphism class. An object $E$ of $\mathfrak A$ will be said to have **finite $\mathfrak C$-dimension** if it admits a finite resolution with elements of $\mathfrak C$. We let $\mathfrak A(\mathfrak C)$ be the family of objects in $\mathfrak A$ which are of finite $\mathfrak C$-dimension. We may then form the

$$
\mathbf K(\mathfrak A(\mathfrak C))=\mathbf Z[\mathfrak A(\mathfrak C)]/R(\mathfrak A(\mathfrak C))
$$

where $R(\mathfrak A(\mathfrak C))$ is the group generated by all elements $[E]-[E']-[E'']$ arising from an exact sequence

$$
0\to E'\to E\to E''\to0
$$

in $\mathfrak A(\mathfrak C)$. Similarly we define

$$
\mathbf K(\mathfrak C)=\mathbf Z[(\mathfrak C)]/R(\mathfrak C),
$$

where $R(\mathfrak C)$ is the group of relations generated as above, but taking $E',E,E''$ in $\mathfrak C$ itself.

There are natural maps

$$
\gamma_{\mathfrak A(\mathfrak C)}:\mathfrak A(\mathfrak C)\to\mathbf K(\mathfrak A(\mathfrak C))\quad\text{and}\quad\gamma_{\mathfrak C}:\mathfrak C\to\mathbf K(\mathfrak C),
$$

which to each object associate its class in the corresponding Grothendieck group. There is also a natural homomorphism

$$
\epsilon:\mathbf K(\mathfrak C)\to\mathbf K(\mathfrak A(\mathfrak C))
$$

since an exact sequence of objects of $\mathfrak C$ can also be viewed as an exact sequence of objects of $\mathfrak A(\mathfrak C)$.

<span class="original-page-anchor" id="pdf-page-781" aria-hidden="true"></span>

**Theorem 3.5.** *Let $M\in\mathfrak A(\mathfrak C)$ and suppose we have two resolutions*

$$
L_M\to M\to0\quad\text{and}\quad L'_M\to M\to0,
$$

*by finite complexes $L_M$ and $L'_M$ in $\mathfrak C$. Then*

$$
\sum(-1)^i\gamma_{\mathfrak C}(L_i)=\sum(-1)^i\gamma_{\mathfrak C}(L'_i).
$$

*Proof.* Take first the special case when there is an epimorphism $L'_M\to L_M$, with kernel $E$ illustrated on the following commutative and exact diagram.

![A surjection of resolutions and its kernel](/library/volume-86/diagrams/pdf-0781-comparison-kernel.png)

The kernel is a complex

$$
0\to E_n\to E_{n-1}\to\cdots\to E_0\to0
$$

which is exact because we have the homology sequence

$$
H_p(E)\to H_p(L')\to H_p(L)\to H_{p-1}(E)
$$

For $p\geqq1$ we have $H_p(L)=H_p(L')=0$ by definition, so $H_p(E)=0$ for $p\geqq1$. And for $p=0$ we consider the exact sequence

$$
H_1(L)\to H_0(E)\to H_0(L')\to H_0(L)
$$

Now we have $H_1(L)=0$, and $H_0(L')\to H_0(L)$ corresponds to the identity morphisms on $M$ so is an isomorphism. It follows that $H_0(E)=0$ also.

By definition of **K**-family, the objects $E_p$ are in $\mathfrak C$. Then taking the Euler characteristic in $\mathbf K(\mathfrak C)$ we find

$$
\chi(L')-\chi(L)=\chi(E)=0
$$

which proves our assertion in the special case.

The general case follows by showing that given two resolutions of $M$ in $\mathfrak C$ we can always find a third one which tops both of them. The pattern of our construction will be given by a lemma.

<span class="original-page-anchor" id="pdf-page-782" aria-hidden="true"></span>

**Lemma 3.6.** *Given two epimorphisms $u:M\to N$ and $v:M'\to N$ in $\mathfrak A$, there exist epimorphisms $F\to M$ and $F\to M'$ with $F$ in $\mathfrak C$ making the following diagram commutative.*

![A common cover of two epimorphisms](/library/volume-86/diagrams/pdf-0782-common-cover.png)

*Proof.* Let $E=M\times_N M'$, that is $E$ is the kernel of the morphism

$$
M\times M'\to N
$$

given by $(x,y)\mapsto ux-vy$. (Elements are not really used here, and we could write formally $u-v$ instead.) There is some $F$ in $\mathfrak C$ and an epimorphism $F\to E\to0$. The composition of this epimorphism with the natural projections of $E$ on each factor gives us what we want.

We construct a complex $L''_M$ giving a resolution of $M$ with a commutative and exact diagram:

![A resolution mapping onto both given resolutions](/library/volume-86/diagrams/pdf-0782-resolutions-common-cover.png)

The construction is done inductively, so we put indices:

![The indexed inductive comparison](/library/volume-86/diagrams/pdf-0782-inductive-comparison.png)

<span class="original-page-anchor" id="pdf-page-783" aria-hidden="true"></span>

Suppose that we have constructed up to $L''_{i-1}$ with the desired epimorphisms on $L_{i-1}$ and $L'_{i-1}$. We want to construct $L''_i$. Let $B_i=\operatorname{Ker}(L_{i-1}\to L_{i-2})$ and similarly for $B'_i$ and $B''_i$. We obtain the commutative diagram:

![The boundary modules in the inductive construction](/library/volume-86/diagrams/pdf-0783-inductive-boundaries.png)

If $B''_i\to B_i$ or $B''_i\to B'_i$ are not epimorphisms, then we replace $L''_{i-1}$ by

$$
L''_{i-1}\oplus L_i\oplus L'_i.
$$

We let the boundary map to $L''_{i-2}$ be $0$ on the new summands, and similarly define the maps to $L_{i-1}$ and $L'_{i-1}$ to be $0$ on $L'_i$ and $L_{i-1}$ respectively.

Without loss of generality we may now assume that

$$
B''_i\to B_i\quad\text{and}\quad B''_i\to B'_i
$$

are epimorphisms. We then use the construction of the preceding lemma. We let

$$
E_i=L_i\bigoplus_{B_i}B''_i\quad\text{and}\quad E'_i=B''_i\bigoplus_{B'_i}L'_i.
$$

Then both $E_i$ and $E'_i$ have natural epimorphisms on $B''_i$. Then we let

$$
N_i=E_i\bigoplus_{B''_i}E'_i
$$

and we find an object $L''_i$ in $\mathfrak C$ with an epimorphism $L''_i\to N_i$. This gives us the inductive construction of $L''$ up to the very end. To stop the process, we use **K 3** and take the kernel of the last constructed $L''_i$ to conclude the proof.

**Theorem 3.7.** *The natural map*

$$
\epsilon:\mathbf K(\mathfrak C)\to\mathbf K(\mathfrak A(\mathfrak C))
$$

*is an isomorphism.*

*Proof.* The map is surjective because given a resolution

$$
0\to F_n\to\cdots\to F_0\to M\to0
$$

with $F_i\in\mathfrak C$ for all $i$, the element

$$
\sum(-1)^i\gamma_{\mathfrak C}(F_i)
$$

<span class="original-page-anchor" id="pdf-page-784" aria-hidden="true"></span>

maps on $\gamma_{\mathfrak A(\mathfrak C)}(M)$ under $\epsilon$. Conversely, Theorem 3.5 shows that the association

$$
M\mapsto\sum(-1)^i\gamma_{\mathfrak C}(F_i)
$$

is a well-defined mapping. Since for any $L\in\mathfrak C$ we have a short exact sequence $0\to L\to L\to0$, it follows that this mapping following $\epsilon$ is the identity on $\mathbf K(\mathfrak C)$, so $\epsilon$ is a monomorphism. Hence $\epsilon$ is an isomorphism, as was to be shown.

It may be helpful to the reader actually to see the next lemma which makes the additivity of the inverse more explicit.

**Lemma 3.8.** *Given an exact sequence in $\mathfrak A(\mathfrak C)$*

$$
0\to M'\to M\to M''\to0
$$

*there exists a commutative and exact diagram*

![An exact sequence of finite resolutions](/library/volume-86/diagrams/pdf-0784-exact-resolutions.png)

*with finite resolutions $L_{M'},L_M,L_{M''}$ in $\mathfrak C$.*

*Proof.* We first show that we can find $L',L,L''$ in $\mathfrak C$ to fit an exact and commutative diagram

![The first step of the construction of exact resolutions](/library/volume-86/diagrams/pdf-0784-horseshoe-first-step.png)

We first select an epimorphism $L''\to M''$ with $L''$ in $\mathfrak C$. By Lemma 3.6 there exists $L_1\in\mathfrak C$ and epimorphisms $L_1\to M$, $L_1\to L''$ making the diagram commutative. Then let $L_2\to M'$ be an epimorphism with $L_2\in\mathfrak C$, and finally define $L=L_1\oplus L_2$. Then we get morphisms $L\to M$ and $L\to L''$ in the obvious way. Let $L'$ be the kernel of $L\to L''$. Then $L_2\subset L'$ so we get an epimorphism $L'\to M'$.

<span class="original-page-anchor" id="pdf-page-785" aria-hidden="true"></span>

This now allows us to construct resolutions inductively until we hit the $n$-th step, where $n$ is some integer such that $M,M''$ admit resolutions of length $n$ in $\mathfrak C$. The last horizontal exact sequence that we obtain is

$$
0\to L'_n\to L_n\to L''_n\to0
$$

and $L''_n$ can be chosen to be the kernel of $L''_{n-1}\to L''_{n-2}$. By **K 3** we know that $L''_n$ lies in $\mathfrak C$, and the sequence

$$
0\to L''_n\to L''_{n-1}
$$

is exact. This implies that in the next inductive step, we can take $L''_{n+1}=0$. Then

$$
0\to L'_{n+1}\to L_{n+1}\to0\to0
$$

is exact, and at the next step we just take the kernels of the vertical arrows to complete the desired finite resolutions in $\mathfrak C$. This concludes the proof of the lemma.

**Remark.** The argument in the proof of Lemma 3.8 in fact shows:

*If*

$$
0\to M'\to M\to M''\to0
$$

*is an exact sequence in $\mathfrak A$, and if $M,M''$ have finite $\mathfrak C$-dimension, then so does $M'$.*

In the category of modules, one has a more precise statement:

**Theorem 3.9.** *Let $\mathfrak A$ be the category of modules over a ring. Let $\mathfrak P$ be the family of projective modules. Given an exact sequence of modules*

$$
0\to E'\to E\to E''\to0
$$

*if any two of $E',E,E''$ admit finite resolutions in $\mathfrak P$ then the third does also.*

Proofs in a more subtle case will be given in Chapter XXI, Theorem 2.7.

Next we shall use the tensor product to investigate a ring structure on the Grothendieck group. We suppose for simplicity that we deal with an abelian category of modules over a commutative ring, denoted by $\mathfrak A$, together with a **K**-family $\mathfrak C$ as above, but we now assume that $\mathfrak A$ is closed under the tensor product. The only properties we shall actually use for the next results are the following ones, denoted by **TG** (for “tensor” and “Grothendieck” respectively):

**TG 1.** There is a bifunctorial isomorphism giving commutativity

$$
M\otimes N\approx N\otimes M
$$

for all $M,N$ in $\mathfrak A$; and similarly for distributivity over direct sums, and associativity.

<span class="original-page-anchor" id="pdf-page-786" aria-hidden="true"></span>

**TG 2.** For all $L$ in $\mathfrak C$ the functor $M\mapsto L\otimes M$ is exact.

**TG 3.** If $L,L'$ are in $\mathfrak C$ then $L\otimes L'$ is in $\mathfrak C$.

Then we may give $\mathbf K(\mathfrak C)$ the structure of an algebra by defining

$$
\operatorname{cl}_{\mathfrak C}(L)\operatorname{cl}_{\mathfrak C}(L')=\operatorname{cl}_{\mathfrak C}(L\otimes L').
$$

Condition **TG 1** implies that this algebra is commutative, and we call it the **Grothendieck algebra**. In practice, there is a unit element, but if we want one in the present axiomatization, we have to make it an explicit assumption:

**TG 4.** There is an object $R$ in $\mathfrak C$ such that $R\otimes M\approx M$ for all $M$ in $\mathfrak A$.

Then $\operatorname{cl}_{\mathfrak C}(R)$ is the unit element.

Similarly, condition **TG 2** shows that we can define a module structure on $\mathbf K(\mathfrak A)$ over $\mathbf K(\mathfrak C)$ by the same formula

$$
\operatorname{cl}_{\mathfrak C}(L)\operatorname{cl}_{\mathfrak A}(M)=\operatorname{cl}_{\mathfrak A}(L\otimes M),
$$

and similarly $\mathbf K(\mathfrak A(\mathfrak C))$ is a module over $\mathbf K(\mathfrak C)$, where we recall that $\mathfrak A(\mathfrak C)$ is the family of objects in $\mathfrak A$ which admit finite resolutions by objects in $\mathfrak C$.

Since we know from Theorem 3.7 that $\mathbf K(\mathfrak C)\approx\mathbf K(\mathfrak A(\mathfrak C))$, we also have a ring structure on $\mathbf K(\mathfrak A(\mathfrak C))$ via this isomorphism. We then can make the product more explicit as follows.

**Proposition 3.10.** *Let $M\in\mathfrak A(\mathfrak C)$ and let $N\in\mathfrak A$. Let*

$$
0\to L_n\to\cdots\to L_0\to M\to0
$$

*be a finite resolution of $M$ by objects in $\mathfrak C$. Then*

$$
\begin{aligned}
\operatorname{cl}_{\mathfrak C}(M)\operatorname{cl}_{\mathfrak A}(N)&=\sum(-1)^i\operatorname{cl}_{\mathfrak A}(L_i\otimes N).\\
&=\sum(-1)^i\operatorname{cl}_{\mathfrak A}(H_i(K))
\end{aligned}
$$

*where $K$ is the complex*

$$
0\to L_n\otimes N\to\cdots\to L_0\otimes N\to M\otimes N\to0
$$

*and $H_i(K)$ is the $i$-th homology of this complex.*

*Proof.* The formulas are immediate consequences of the definitions, and of Theorem 3.1.

**Example.** Let $\mathfrak A$ be the abelian category of modules over a commutative ring. Let $\mathfrak C$ be the family of projective modules. From §6 on derived functors the reader will know that the homology of the complex $K$ in Proposition 3.10 is just $\operatorname{Tor}(M,N)$. Therefore the formula in that proposition can also be written

$$
\operatorname{cl}_{\mathfrak C}(M)\operatorname{cl}_{\mathfrak A}(N)=\sum(-1)^i\operatorname{cl}_{\mathfrak A}(\operatorname{Tor}_i(M,N)).
$$

<span class="original-page-anchor" id="pdf-page-787" aria-hidden="true"></span>

**Example.** Let $k$ be a field. Let $G$ be a group. By a **$(G,k)$-module**, we shall mean a pair $(E,\rho)$, consisting of a $k$-space $E$ and a homomorphism

$$
\rho:G\to\operatorname{Aut}_k(E).
$$

Such a homomorphism is also called a **representation** of $G$ in $E$. By abuse of language, we also say that the $k$-space $E$ is a $G$-module. The group $G$ operates on $E$, and we write $\sigma x$ instead of $\rho(\sigma)x$. The field $k$ will be kept fixed in what follows.

Let $\operatorname{Mod}_k(G)$ denote the category whose objects are $(G,k)$-modules. A morphism in $\operatorname{Mod}_k(G)$ is what we call a **$G$-homomorphism**, that is a $k$-linear map $f:E\to F$ such that $f(\sigma x)=\sigma f(x)$ for all $\sigma\in G$. The group of morphisms in $\operatorname{Mod}_k(G)$ is denoted by $\operatorname{Hom}_G$.

If $E$ is a $G$-module, and $\sigma\in G$, then we have by definition a $k$-automorphism $\sigma:E\to E$. Since $T^r$ is a functor, we have an induced automorphism

$$
T^r(\sigma):T^r(E)\to T^r(E)
$$

for each $r$, and thus $T^r(E)$ is also a $G$-module. Taking the direct sum, we see that $T(E)$ is a $G$-module, and hence that $T$ is a functor from the category of $G$-modules to the category of graded $G$-modules. Similarly for $\bigwedge^r,S^r$, and $\bigwedge,S$.

It is clear that the kernel of a $G$-homomorphism is a $G$-submodule, and that the factor module of a $G$-module by a $G$-submodule is again a $G$-module so the category of $G$-modules is an abelian category.

We can now apply the general considerations on the Grothendieck group which we write

$$
\mathbf K(G)=\mathbf K(\operatorname{Mod}_k(G))
$$

for simplicity in the present case. We have the canonical map

$$
\operatorname{cl}:\operatorname{Mod}_k(G)\to\mathbf K(G).
$$

which to each $G$-module associates its class in $\mathbf K(G)$.

If $E,F$ are $G$-modules, then their tensor product over $k$, $E\otimes F$, is also a $G$-module. Here again, the operation of $G$ on $E\otimes F$ is given functorially. If $\sigma\in G$, there exists a unique $k$-linear map $E\otimes F\to E\otimes F$ such that for $x\in E,y\in F$ we have $x\otimes y\mapsto(\sigma x)\otimes(\sigma y)$. The tensor product induces a law of composition on $\operatorname{Mod}_k(G)$ because the tensor products of $G$-isomorphic modules are $G$-isomorphic.

Furthermore all the conditions **TG 1** through **TG 4** are satisfied. Since $k$ is a field, we find also that tensoring an exact sequence of $G$-modules over $k$ with any $G$-module over $k$ preserves the exactness, so **TG 2** is satisfied for all $(G,k)$-modules. Thus the Grothendieck group $\mathbf K(G)$ is in fact the Grothendieck ring, or the Grothendieck algebra over $k$.

<span class="original-page-anchor" id="pdf-page-788" aria-hidden="true"></span>

By Proposition 2.1 and Theorem 2.3 of Chapter XVIII, we also see:

*The Grothendieck ring of a finite group $G$ consisting of isomorphism classes of finite dimensional $(G,k)$-spaces over a field $k$ of characteristic $0$ is naturally isomorphic to the character ring $X_{\mathbf Z}(G)$.*

We can axiomatize this a little more. We consider an abelian category of modules over a commutative ring $R$, which we denote by $\mathfrak A$ for simplicity. For two modules $M,N$ in $\mathfrak A$ we let $\operatorname{Mor}(M,N)$ as usual be the morphisms in $\mathfrak A$, but $\operatorname{Mor}(M,N)$ is an abelian subgroup of $\operatorname{Hom}_R(M,N)$. For example, we could take $\mathfrak A$ to be the category of $(G,k)$-modules as in the example we have just discussed, in which case $\operatorname{Mor}(M,N)=\operatorname{Hom}_G(M,N)$.

We let $\mathfrak C$ be the family of finite free modules in $\mathfrak A$. *We assume that $\mathfrak C$ satisfies* **TG 1, TG 2, TG 3, TG 4**, *and also that $\mathfrak C$ is closed under taking alternating products, tensor products and symmetric products.* We let $\mathbf K=\mathbf K(\mathfrak C)$. As we have seen, $\mathbf K$ is itself a commutative ring. We abbreviate $\operatorname{cl}_{\mathfrak C}=\operatorname{cl}$.

We shall define non-linear maps

$$
\lambda^i:\mathbf K\to\mathbf K
$$

using the alternating product. If $E$ is finite free, we let

$$
\lambda^i(E)=\operatorname{cl}(\bigwedge^iE).
$$

Proposition 1.1 of Chapter XIX can now be formulated for the **K**-ring as follows.

**Proposition 3.11.** *Let*

$$
0\to E'\to E\to E''\to0
$$

*be an exact sequence of finite free modules in $\mathfrak A$. Then for every integer $n\geqq0$ we have*

$$
\lambda^n(E)=\sum_{i=0}^n\lambda^i(E')\lambda^{n-i}(E'').
$$

As a result of the proposition, we can define a map

$$
\lambda_t:\mathbf K\to1+t\mathbf K[[t]]
$$

of $\mathbf K$ into the multiplicative group of formal power series with coefficients in $\mathbf K$, and with constant term $1$, by letting

$$
\lambda_t(x)=\sum_{i=0}^{\infty}\lambda^i(x)t^i.
$$

<span class="original-page-anchor" id="pdf-page-789" aria-hidden="true"></span>

Proposition 1.4 of Chapter XIX can be formulated by saying that:

*The map*

$$
\lambda_t:\mathbf K\to1+t\mathbf K[[t]]
$$

*is a homomorphism.*

*We note that if $L$ is free of rank $1$, then*

$$
\begin{aligned}
\lambda^0(L)&=\text{ground ring};\\
\lambda^1(L)&=\operatorname{cl}(L);\\
\lambda^i(L)&=0\quad\text{for}\quad i>1.
\end{aligned}
$$

This can be summarized by writing

$$
\lambda_t(L)=1+\operatorname{cl}(L)t.
$$

Next we can do a similar construction with the symmetric product instead of the alternating product. If $E$ is a finite free module in $\mathfrak C$ we let as usual:

$$
\begin{aligned}
S(E)&=\text{symmetric algebra of }E;\\
S^i(E)&=\text{homogeneous component of degree }i\text{ in }S(E).
\end{aligned}
$$

We define

$$
\sigma^i(E)=\operatorname{cl}(S^i(E))
$$

and the corresponding power series

$$
\sigma_t(E)=\sum\sigma^i(E)t^i.
$$

**Theorem 3.12.** *Let $E$ be a finite free module in $\mathfrak A$, of rank $r$. Then for all integers $n\geqq1$ we have*

$$
\sum_{i=0}^r(-1)^i\lambda^i(E)\sigma^{n-i}(E)=0,
$$

*where by definition $\sigma^j(E)=0$ for $j<0$. Furthermore*

$$
\sigma_t(E)\lambda_{-t}(E)=1,
$$

*so the power series $\sigma_t(E)$ and $\lambda_{-t}(E)$ are inverse to each other.*

*Proof.* The first formula depends on the analogue for the symmetric product and the alternating product of the formula given in Proposition 1.1 of Chapter <span class="original-page-anchor" id="pdf-page-790" aria-hidden="true"></span>XIX. It could be proved directly now, but the reader will find a proof as a special case of the theory of Koszul complexes in Chapter XXI, Corollary 4.14. The power series relation is essentially a reformulation of the first formula.

From the above formalism, it is possible to define other maps besides $\lambda^i$ and $\sigma^i$.

**Example.** Assume that the group $G$ is trivial, and just write $\mathbf K$ for the Grothendieck ring instead of $\mathbf K(1)$. For $x\in\mathbf K$ define

$$
\psi_{-t}(x)=-t\frac{d}{dt}\log\lambda_t(x)=-t\lambda'_t(x)/\lambda_t(x).
$$

Show that $\psi_{-t}$ is an additive and multiplicative homomorphism. Show that

$$
\psi_t(E)=1+\operatorname{cl}(E)t+\operatorname{cl}(E)^2t^2+\cdots.
$$

This kind of construction with the logarithmic derivative leads to the **Adams operations** $\psi^i$ in topology and algebraic geometry. See Exercise 22 of Chapter XVIII.

**Remark.** If it happens in Theorem 3.12 that $E$ admits a decomposition into 1-dimensional free modules in the **K**-group, then the proof trivializes by using the fact that $\lambda_t(L)=1+\operatorname{cl}(L)t$ if $L$ is 1-dimensional. But in the example of $(G,k)$-spaces when $k$ is a field, this is in general not possible, and it is also not possible in other examples arising naturally in topology and algebraic geometry. However, by “changing the base,” one can sometimes achieve this simpler situation, but Theorem 3.12 is then used in establishing the basic properties. *Cf.* Grothendieck [SGA 6], mentioned in the introduction to Part IV, and other works mentioned in the bibliography at the end, namely [Ma 69], [At 61], [At 67], [Ba 68], [Bo 62]. The lectures by Atiyah and Bott emphasize the topological aspects as distinguished from the algebraic-geometric aspects. Grothendieck [Gr 68] actually shows how the formalism of Chern classes from algebraic geometry and topology also enters the theory of representations of linear groups. See also the exposition in [FuL 85], especially the formalism of Chapter I, §6. For special emphasis on applications to representation theory, see Bröcker-tom Dieck [BtD 85], especially Chapter II, §7, concerning compact Lie groups.

## §4. Injective Modules

In Chapter III, §4, we defined projective modules, which have a natural relation to free modules. By reversing the arrows, we can define a module $Q$ to be **injective** if it satisfies any one of the following conditions which are equivalent:

**I 1.** Given any module $M$ and a submodule $M'$, and a homomorphism $f:M'\to Q$, there exists an extension of this homomorphism to $M$, <span class="original-page-anchor" id="pdf-page-791" aria-hidden="true"></span>that is there exists $h:M\to Q$ making the following diagram commutative:

![Extension to M in the definition of injectivity](/library/volume-86/diagrams/pdf-0791-injective-extension.png)

**I 2.** The functor $M\mapsto\operatorname{Hom}_A(M,Q)$ is exact.

**I 3.** Every exact sequence $0\to Q\to M\to M''\to0$ splits.

We prove the equivalence. General considerations on homomorphisms as in Proposition 2.1, show that exactness of the homed sequence may fail only at one point, namely given

$$
0\to M'\to M\to M''\to0,
$$

the question is whether

$$
\operatorname{Hom}_A(M,Q)\to\operatorname{Hom}_A(M',Q)\to0
$$

is exact. But this is precisely the hypothesis as formulated in **I 1**, so **I 1** implies **I 2** is essentially a matter of linguistic reformulation, and in fact **I 1** is equivalent to **I 2**.

Assume **I 2** or **I 1**, which we know are equivalent. To get **I 3** is immediate, by applying **I 1** to the diagram:

![A retraction given by injectivity](/library/volume-86/diagrams/pdf-0791-injective-retraction.png)

To prove the converse, we need the notion of push-out (cf. Exercise 52 of Chapter I). Given an exact diagram

![The exact diagram used to form a push-out](/library/volume-86/diagrams/pdf-0791-pushout-input.png)

we form the push-out:

![The push-out Q ⊕ over M' M](/library/volume-86/diagrams/pdf-0791-pushout-square.png)

<span class="original-page-anchor" id="pdf-page-792" aria-hidden="true"></span>

Since $M'\to M$ is a monomorphism, it is immediately verified from the construction of the push-out that $Q\to N$ is also a monomorphism. By **I 3**, the sequence

$$
0\to Q\to N
$$

splits, and we can now compose the splitting map $N\to Q$ with the push-out map $M\to N$ to get the desired $h:M\to Q$, thus proving **I 1**.

We saw easily that every module is a homomorphic image of a free module. There is no equally direct construction for the dual fact:

**Theorem 4.1.** *Every module is a submodule of an injective module.*

The proof will be given by dualizing the situation, with some lemmas. We first look at the situation in the category of abelian groups. If $M$ is an abelian group, let its dual group be $M^\wedge=\operatorname{Hom}(M,\mathbf Q/\mathbf Z)$. If $F$ is a free abelian group, it is reasonable to expect, and in fact it is easily proved that its dual $F^\wedge$ is an injective module, since injectivity is the dual notion of projectivity. Furthermore, $M$ has a natural map into the double dual $M^{\wedge\wedge}$, which is shown to be a monomorphism. Now represent $M^\wedge$ as a quotient of a free abelian group,

$$
F\to M^\wedge\to0.
$$

Dualizing this sequence yields a monomorphism

$$
0\to M^{\wedge\wedge}\to F^\wedge,
$$

and since $M$ is embedded naturally as a subgroup of $M^{\wedge\wedge}$, we get the desired embedding of $M$ as a subgroup of $F^\wedge$.

This proof also works in general, but there are details to be filled in. First we have to prove that the dual of a free module is injective, and second we have to be careful when passing from the category of abelian groups to the category of modules over an arbitrary ring. We now carry out the details.

We say that an abelian group $T$ is **divisible** if for every integer $m$, the homomorphism

$$
m_T:x\mapsto mx
$$

is surjective.

**Lemma 4.2.** *If $T$ is divisible, then $T$ is injective in the category of abelian groups.*

*Proof.* Let $M'\subset M$ be a subgroup of an abelian group, and let $f:M'\to T$ be a homomorphism. Let $x\in M$. We want first to extend $f$ to the module $(M',x)$ generated by $M'$ and $x$. If $x$ is free over $M'$, then we select any value $t\in T$, and it is immediately verified that $f$ extends to $(M',x)$ by giving the value $f(x)=t$. Suppose that $x$ is torsion with respect to $M'$, that is there is a positive integer $m$ such that $mx\in M'$. Let $d$ be the period of $x\bmod M'$, so <span class="original-page-anchor" id="pdf-page-793" aria-hidden="true"></span>$dx\in M'$, and $d$ is the least positive integer such that $dx\in M'$. By hypothesis, there exists an element $u\in T$ such that $du=f(dx)$. For any integer $n$, and $z\in M'$ define

$$
f(z+nx)=f(z)+nu.
$$

By the definition of $d$, and the fact that $\mathbf Z$ is principal, one sees that this value for $f$ is independent of the representation of an element of $(M',x)$ in the form $z+nx$, and then it follows at once that this extended definition of $f$ is a homomorphism. Thus we have extended $f$ to $(M',x)$.

The rest of the proof is merely an application of Zorn's lemma. We consider pairs $(N,g)$ consisting of submodules of $M$ containing $M'$, and an extension $g$ of $f$ to $N$. We say that $(N,g)\leqq(N_1,g_1)$ if $N\subset N_1$ and the restriction of $g_1$ to $N$ is $g$. Then such pairs are inductively ordered. Let $(N,g)$ be a maximal element. If $N\ne M$ then there is some $x\in M,x\notin N$ and we can apply the first part of the proof to extend the homomorphism to $(N,x)$, which contradicts the maximality, and concludes the proof of the lemma.

**Example.** The abelian groups $\mathbf Q/\mathbf Z$ and $\mathbf R/\mathbf Z$ are divisible, and hence are injective in the category of abelian groups.

We can prove Theorem 4.1 in the category of abelian groups following the pattern described above. If $F$ is a free abelian group, then the dual $F^\wedge$ is a direct product of groups isomorphic to $\mathbf Q/\mathbf Z$, and is therefore injective in the category of abelian groups by Lemma 4.2. This concludes the proof.

Next we must make the necessary remarks to extend the system to modules. Let $A$ be a ring and let $T$ be an abelian group. We make $\operatorname{Hom}_{\mathbf Z}(A,T)$ into an $A$-module as follows. Let $f:A\to T$ be an abelian group homomorphism. For $a\in A$ we define the operation

$$
(af)(b)=f(ba).
$$

The rules for an operation are then immediately verified. Then for any $A$-module $X$ we have a natural isomorphism of abelian groups:

$$
\operatorname{Hom}_{\mathbf Z}(X,T)\xrightarrow{\approx}\operatorname{Hom}_A(X,\operatorname{Hom}_{\mathbf Z}(A,T)).
$$

Indeed, let $\psi:X\to T$ be a $\mathbf Z$-homomorphism. We associate with $\psi$ the homomorphism

$$
f:X\to\operatorname{Hom}_{\mathbf Z}(A,T)
$$

such that

$$
f(x)(a)=\psi(ax).
$$

<span class="original-page-anchor" id="pdf-page-794" aria-hidden="true"></span>

The definition of the $A$-module structure on $\operatorname{Hom}_{\mathbf Z}(A,T)$ shows that $f$ is an $A$-homomorphism, so we get an arrow from $\operatorname{Hom}_{\mathbf Z}(X,T)$ to

$$
\operatorname{Hom}_A(X,\operatorname{Hom}_{\mathbf Z}(A,T)).
$$

Conversely, let $f:X\to\operatorname{Hom}_{\mathbf Z}(A,T)$ be an $A$-homomorphism. We define the corresponding $\psi$ by

$$
\psi(x)=f(x)(1).
$$

It is then immediately verified that these maps are inverse to each other.

We shall apply this when $T$ is any divisible group, although we think of $T$ as being $\mathbf Q/\mathbf Z$, and we think of the homomorphisms into $T$ as representing the dual group according to the pattern described previously.

**Lemma 4.3.** *If $T$ is a divisible abelian group, then $\operatorname{Hom}_{\mathbf Z}(A,T)$ is injective in the category of $A$-modules.*

*Proof.* It suffices to prove that if $0\to X\to Y$ is exact in the category of $A$-modules, then the dual sequence obtained by taking $A$-homomorphisms into $\operatorname{Hom}_{\mathbf Z}(A,T)$ is exact, that is the top map in the following diagram is surjective.

![The diagram proving the injectivity of Hom over Z](/library/volume-86/diagrams/pdf-0794-coinduced-injective.png)

But we have the isomorphisms described before the lemma, given by the vertical arrows of the diagram, which is commutative. The bottom map is surjective because $T$ is an injective module in the category of abelian groups. Therefore the top map is surjective, thus proving the lemma.

Now we prove Theorem 4.1 for $A$-modules. Let $M$ be an $A$-module. We can embed $M$ in a divisible abelian group $T$,

$$
0\to M\xrightarrow{f}T.
$$

Then we get an $A$-homomorphism

$$
M\to\operatorname{Hom}_{\mathbf Z}(A,T)
$$

by $x\mapsto f_x$, where $f_x(a)=f(ax)$. One verifies at once that $x\mapsto f_x$ gives an embedding of $M$ in $\operatorname{Hom}_{\mathbf Z}(A,T)$, which is an injective module by Lemma 4.3. This concludes the proof of Theorem 4.1.

<span class="original-page-anchor" id="pdf-page-795" aria-hidden="true"></span>

## §5. Homotopies of Morphisms of Complexes

The purpose of this section is to describe a condition under which homomorphisms of complexes induce the same map on the homology and to show that this condition is satisfied in an important case, from which we derive applications in the next section.

The arguments are applicable to any abelian category. The reader may prefer to think of modules, but we use a language which applies to both, and is no more complicated than if we insisted on dealing only with modules.

Let $E=\{(E^n,d^n)\}$ and $E'=\{(E'^n,d'^n)\}$ be two complexes. Let

$$
f,g:E\to E'
$$

be two morphisms of complexes (of degree $0$). We say that $f$ is **homotopic to** $g$ if there exists a sequence of homomorphisms

$$
h_n:E^n\to E'^{(n-1)}
$$

such that

$$
f_n-g_n=d'^{(n-1)}h_n+h_{n+1}d^n.
$$

**Lemma 5.1.** *If $f,g$ are homotopic, then $f,g$ induce the same homomorphism on the homology $H(E)$, that is*

$$
H(f_n)=H(g_n):H^n(E)\to H^n(E').
$$

*Proof.* The lemma is immediate, because $f_n-g_n$ vanishes on the cycles, which are the kernel of $d^n$, and the homotopy condition shows that the image of $f_n-g_n$ is contained in the boundaries, that is, in the image of $d'^{(n-1)}$.

**Remark.** The terminology of homotopy is used because the notion and formalism first arose in the context of topology. Cf. [ES 52] and [GreH 81].

We apply Lemma 5.1 to injective objects. Note that as usual the definition of an injective module applies without change to define an injective object in any abelian category. Instead of a submodule in **I 1**, we use a subobject, or equivalently a monomorphism. The proofs of the equivalence of the three conditions defining an injective module depended only on arrow-theoretic juggling, and apply in the general case of abelian categories.

We say that an abelian category has **enough injectives** if given any object $M$ there exists a monomorphism

$$
0\to M\to I
$$

<span class="original-page-anchor" id="pdf-page-796" aria-hidden="true"></span>

into an injective object. We proved in §4 that the category of modules over a ring has enough injectives. *We now assume that the abelian category we work with has enough injectives.*

By an **injective resolution** of an object $M$ one means an exact sequence

$$
0\to M\to I^0\to I^1\to I^2\to
$$

such that each $I_n$ $(n\geqq0)$ is injective. Given $M$, such a resolution exists. Indeed, the monomorphism

$$
0\to M\to I^0
$$

exists by hypothesis. Let $M^0$ be its image. Again by assumption, there exists a monomorphism

$$
0\to I^0/M^0\to I^1,
$$

and the corresponding homomorphism $I^0\to I^1$ has kernel $M^0$. So we have constructed the first step of the resolution, and the next steps proceed in the same fashion.

An injective resolution is of course not unique, but it has some uniqueness which we now formulate.

**Lemma 5.2.** *Consider two complexes:*

![Two augmented complexes and a homomorphism of their initial objects](/library/volume-86/diagrams/pdf-0796-injective-comparison.png)

*Suppose that the top row is exact, and that each $I^n$ $(n\geqq0)$ is injective. Let $\varphi:M\to M'$ be a given homomorphism. Then there exists a morphism $f$ of complexes such that $f_{-1}=\varphi$; and any two such are homotopic.*

*Proof.* By definition of an injective, the homomorphism $M\to I^0$ via $M'$ extends to a homomorphism

$$
f_0:E^0\to I^0,
$$

which makes the first square commute:

![The first square in the comparison construction](/library/volume-86/diagrams/pdf-0796-comparison-first-square.png)

<span class="original-page-anchor" id="pdf-page-797" aria-hidden="true"></span>

Next we must construct $f_1$. We write the second square in the form

![The second square in the comparison construction](/library/volume-86/diagrams/pdf-0797-comparison-second-square.png)

with the exact top row as shown. Again because $I^1$ is injective, we can apply the same argument and find $f_1$ to make the second square commute. And so on, thus constructing the morphism of complexes $f$.

Suppose $f,g$ are two such morphisms. We define $h_0:E^0\to M'$ to be $0$. Then the condition for a homotopy is satisfied in the first instance, when

$$
f_{-1}=g_{-1}=\varphi.
$$

Next let $d^{-1}:M\to E^0$ be the embedding of $M$ in $E^0$. Since $I^0$ is injective, we can extend

$$
d^0:E^0/\operatorname{Im}d^{-1}\to E_1
$$

to a homomorphism $h_1:E^1\to I^0$. Then the homotopy condition is verified for $f_0-g_0$. Since $h_0=0$ we actually have in this case

$$
f_0-g_0=h_1d^0,
$$

but this simplification is misleading for the inductive step which follows. We assume constructed the map $h_{n+1}$, and we wish to show the existence of $h_{n+2}$ satisfying

$$
f_{n+1}-g_{n+1}=d'^nh_{n+1}+h_{n+2}d^{n+1}.
$$

Since $\operatorname{Im}d^n=\operatorname{Ker}d^{n+1}$, we have a monomorphism $E^{n+1}/\operatorname{Im}d^n\to E^{n+2}$. By the definition of an injective object, which in this case is $I^{n+1}$, it suffices to prove that

$$
f_{n+1}-g_{n+1}-d'^nh_{n+1}\quad\text{vanishes on the image of }d^n,
$$

and to use the exact diagram:

![The exact diagram for extending the homotopy](/library/volume-86/diagrams/pdf-0797-homotopy-extension.png)

to get the existence of $h_{n+2}:E^{n+2}\to I^{n+1}$ extending $f_{n+1}-g_{n+1}$. But we have:

$$
\begin{aligned}
&(f_{n+1}-g_{n+1}-d'^nh_{n+1})d^n\\
&\qquad=(f_{n+1}-g_{n+1})d^n-d'^nh_{n+1}d^n
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-798" aria-hidden="true"></span>

$$
\begin{aligned}
&=(f_{n+1}-g_{n+1})d^n-d'^n(f_n-g_n-d'^{(n-1)}h_n)&&\text{by induction}\\
&=(f_{n+1}-g_{n+1})d^n-d'^n(f_n-g_n)&&\text{because }d'd'=0\\
&=0&&\text{because }f,g\text{ are homomorphisms of complexes.}
\end{aligned}
$$

This concludes the proof of Lemma 5.2.

**Remark.** Dually, let $P_{M'}\to M'\to0$ be a complex with $P^i$ projective for $i\geqq0$, and let $E_M\to M\to0$ be a resolution. Let $\varphi:M'\to M$ be a homomorphism. Then $\varphi$ extends to a homomorphism of complex $P\to E$. The proof is obtained by reversing arrows in Lemma 5.2. The books on homological algebra that I know of in fact carry out the projective case, and leave the injective case to the reader. However, one of my motivations is to do here what is needed, for instance in [Ha 77], Chapter III, on derived functors, as a preliminary to the cohomology of sheaves. For an example of projective resolutions using free modules, see Exercises 2–7, concerning the cohomology of groups.

## §6. Derived Functors

We continue to work in an abelian category. A covariant additive functor

$$
F:\mathfrak A\to\mathfrak B
$$

is said to be **left exact** if it transforms an exact sequence

$$
0\to M'\to M\to M''
$$

into an exact sequence $0\to F(M')\to F(M)\to F(M'')$. We remind the reader that $F$ is called **additive** if the map

$$
\operatorname{Hom}(A',A)\to\operatorname{Hom}(FA',FA)
$$

is additive.

*We assume throughout that $F$ is left exact unless otherwise specified, and additive. We continue to assume that our abelian category has enough injectives.*

Given an object $M$, let

$$
0\to M\to I^0\to I^1\to I^2\to
$$

be an injective resolution, which we abbreviate by

$$
0\to M\to I_M,
$$

where $I_M$ is the complex $I^0\to I^1\to I^2\to$. We let $I$ be the complex

$$
0\to I^0\to I^1\to I^2\to
$$

<span class="original-page-anchor" id="pdf-page-799" aria-hidden="true"></span>

We define the **right-derived functor** $R^nF$ by

$$
R^nF(M)=H^n(F(I)),
$$

in other words, the $n$-th homology of the complex

$$
0\to F(I^0)\to F(I^1)\to F(I^2)\to
$$

Directly from the definitions and the monomorphism $M\to I_0$, we see that there is an isomorphism

$$
R^0F(M)=F(M).
$$

This isomorphism seems at first to depend on the injective resolution, and so do the functors $R^nF(M)$ for other $n$. However, from Lemmas 5.1 and 5.2 we see that given two injective resolutions of $M$, there is a homomorphism between them, and that any two homomorphisms are homotopic. If we apply the functor $F$ to these homomorphisms and to the homotopy, then we see that the homology of the complex $F(I)$ is in fact determined up to a unique isomorphism. One therefore omits the resolution from the notation and from the language.

**Example 1.** Let $R$ be a ring and let $\mathfrak A=\operatorname{Mod}(R)$ be the category of $R$-modules. Fix a module $A$. The functor $M\mapsto\operatorname{Hom}(A,M)$ is left exact, i.e. given an exact sequence $0\to M'\to M\to M''$, the sequence

$$
0\to\operatorname{Hom}(A,M')\to\operatorname{Hom}(A,M)\to\operatorname{Hom}(A,M'')
$$

is exact. Its right derived functors are denoted by $\operatorname{Ext}^n(A,M)$ for $M$ variable. Similarly, for a fixed module $B$, the functor $X\mapsto\operatorname{Hom}(X,B)$ is right exact, and it gives rise to its **left derived functors**. For the explicit mirror image of the terminology, see the end of this section. In any case, we may consider $A$ as variable. In §8 we shall go more deeply into this aspect of the formalism, by dealing with bifunctors. It will turn out that $\operatorname{Ext}^n(A,B)$ has a dual interpretation as a left derived functor of the first variable and right derived functor of the second variable. See Corollary 8.5.

In the exercises, you will prove that $\operatorname{Ext}^1(A,M)$ is in bijection with isomorphism classes of extensions, of $M$ by $A$, that is, isomorphism classes of exact sequences

$$
0\to A\to E\to M\to0.
$$

The name Ext comes from this interpretation in dimension $1$.

For the computation of $\operatorname{Ext}^i$ in certain important cases, see Chapter XXI, Theorems 4.6 and 4.11, which serve as examples for the general theory.

**Example 2.** Let $R$ be commutative. The functor $M\mapsto A\otimes M$ is right exact, in other words, the sequence

$$
A\otimes M'\to A\otimes M\to A\otimes M''\to0
$$

is exact. Its left derived functors are denoted by $\operatorname{Tor}_n(A,M)$ for $M$ variable.

<span class="original-page-anchor" id="pdf-page-800" aria-hidden="true"></span>

**Example 3.** Let $G$ be a group and let $R=\mathbf Z[G]$ be the group ring. Let $\mathfrak A$ be the category of $G$-modules, i.e. $\mathfrak A=\operatorname{Mod}(R)$, also denoted by $\operatorname{Mod}(G)$. For a $G$-module $A$, let $A^G$ be the submodule (abelian group) consisting of those elements $v$ such that $xv=v$ for all $x\in G$. Then $A\mapsto A^G$ is a left exact functor from $\operatorname{Mod}(R)$ into the category of abelian groups. Its left derived functors give rise to the cohomology of groups. Some results from this special cohomology will be carried out in the exercises, as further examples of the general theory.

**Example 4.** Let $X$ be a topological space (we assume the reader knows what this is). By a **sheaf** $\mathfrak F$ of abelian groups on $X$, we mean the data:

**(a)** For every open set $U$ of $X$ there is given an abelian group $\mathfrak F(U)$.

**(b)** For every inclusion $V\subset U$ of open sets there is given a homomorphism

$$
\operatorname{res}^U_V:\mathfrak F(U)\to\mathfrak F(V),
$$

called the **restriction** from $U$ to $V$, subject to the following conditions:

**SH 1.** $\mathfrak F(\text{empty set})=0$.

**SH 2.** $\operatorname{res}^U_U$ is the identity $\mathfrak F(U)\to\mathfrak F(U)$.

**SH 3.** If $W\subset V\subset U$ are open sets, then $\operatorname{res}^V_W\circ\operatorname{res}^U_V=\operatorname{res}^U_W$.

**SH 4.** Let $U$ be an open set and $\{V_i\}$ be an open covering of $U$. Let $s\in\mathfrak F(U)$. If the restriction of $s$ to each $V_i$ is $0$, then $s=0$.

**SH 5.** Let $U$ be an open set and let $\{V_i\}$ be an open covering of $U$. Suppose given $s_i\in\mathfrak F(V_i)$ for each $i$, such that given $i,j$ the restrictions of $s_i$ and $s_j$ to $V_i\cap V_j$ are equal. Then there exists a unique $s\in\mathfrak F(U)$ whose restriction to $V_i$ is $s_i$ for all $i$.

Elements of $\mathfrak F(U)$ are called **sections** of $\mathfrak F$ over $U$. Elements of $\mathfrak F(X)$ are called **global sections**. Just as for abelian groups, it is possible to define the notion of homomorphisms of sheaves, kernels, cokernels, and exact sequences. The association $\mathfrak F\mapsto\mathfrak F(X)$ (global sections functor) is a functor from the category of sheaves of abelian groups to abelian groups, and this functor is left exact. Its right derived functors are the basis of cohomology theory in topology and algebraic geometry (among other fields of mathematics). The reader will find a self-contained brief definition of the basic properties in [Ha 77], Chapter II, §1, as well as a proof that these form an abelian category. For a more extensive treatment I recommend Gunning's [Gu 91], mentioned in the introduction to Part IV, notably Volume III, dealing with the cohomology of sheaves.

We now return to the general theory of derived functors. The general theory tells us that these derived functors do not depend on the resolution by projectives or injectives according to the variance. As we shall also see in §8, one can even use other special types of objects such as acyclic or exact (to be defined), which gives even more flexibility in the ways one has to compute homology. Through certain explicit resolutions, we obtain means of computing the derived functors <span class="original-page-anchor" id="pdf-page-801" aria-hidden="true"></span>explicitly. For example, in Exercise 16, you will see that the cohomology of finite cyclic groups can be computed immediately by exhibiting a specific free resolution of $\mathbf Z$ adapted to such groups. Chapter XXI will contain several other examples which show how to construct explicit finite free resolutions, which allow the determination of derived functors in various contexts.

The next theorem summarizes the basic properties of derived functors.

**Theorem 6.1.** *Let $\mathfrak A$ be an abelian category with enough injectives, and let $F:\mathfrak A\to\mathfrak B$ be a covariant additive left exact functor to another abelian category $\mathfrak B$. Then:*

**(i)** *For each $n\geqq0$, $R^nF$ as defined above is an additive functor from $\mathfrak A$ to $\mathfrak B$. Furthermore, it is independent, up to a unique isomorphism of functors, of the choices of resolutions made.*

**(ii)** *There is a natural isomorphism $F\approx R^0F$.*

**(iii)** *For each short exact sequence*

$$
0\to M'\to M\to M''\to0
$$

*and for each $n\geqq0$ there is a natural homomorphism*

$$
\delta^n:R^nF(M'')\to R^{n+1}F(M)
$$

*such that we obtain a long exact sequence:*

$$
\to R^nF(M')\to R^nF(M)\to R^nF(M'')\xrightarrow{\delta^n}R^{n+1}F(M')\to.
$$

**(iv)** *Given a morphism of short exact sequences*

![A morphism of short exact sequences](/library/volume-86/diagrams/pdf-0801-derived-naturality-input.png)

*the $\delta$'s give a commutative diagram:*

![Naturality of the connecting homomorphisms](/library/volume-86/diagrams/pdf-0801-derived-naturality-square.png)

**(v)** *For each injective object $I$ of $A$ and for each $n>0$ we have $R^nF(I)=0$.*

Properties (i), (ii), (iii), and (iv) essentially say that $R^nF$ is a delta-functor in a sense which will be expanded in the next section. The last property (v) will be discussed after we deal with the delta-functor part of the theorem.

<span class="original-page-anchor" id="pdf-page-802" aria-hidden="true"></span>

We now describe how to construct the $\delta$-homomorphisms. Given a short exact sequence, we can find an injective resolution of $M',M,M''$ separately, but they don't necessarily fit in an exact sequence of complexes. So we must achieve this to apply the considerations of §1. Consider the diagram:

![The initial diagram for compatible injective resolutions](/library/volume-86/diagrams/pdf-0802-injective-horseshoe-initial.png)

We give monomorphisms $M'\to I'^0$ and $M''\to I''^0$ into injectives, and we want to find $X$ injective with a monomorphism $M\to X$ such that the diagram is exact. We take $X$ to be the direct sum

$$
X=I'^0\oplus I''^0.
$$

Since $I'^0$ is injective, the monomorphism $M'\to I'^0$ can be extended to a homomorphism $M\to I'^0$. We take the homomorphism of $M$ into $I'^0\oplus I''^0$ which comes from this extension on the first factor $I'^0$, and is the composite map

$$
M\to M''\to I''^0
$$

on the second factor. Then $M\to X$ is a monomorphism. Furthermore $I'^0\to X$ is the monomorphism on the first factor, and $X\to I''^0$ is the projection on the second factor. So we have constructed the diagram we wanted, giving the beginning of the compatible resolutions.

Now we take the quotient homomorphism, defining the third row, to get an exact diagram:

![The quotient diagram for the next step of the injective resolutions](/library/volume-86/diagrams/pdf-0802-injective-horseshoe-quotients.png)

<span class="original-page-anchor" id="pdf-page-803" aria-hidden="true"></span>

where we let $I^0=X$, and $N',N,N''$ are the cokernels of the vertical maps by definition. The exactness of the $N$-sequence is left as an exercise to the reader. We then repeat the construction with the $N$-sequence, and by induction construct injective resolutions

![Compatible injective resolutions of a short exact sequence](/library/volume-86/diagrams/pdf-0803-compatible-injective-resolutions.png)

of the $M$-sequence such that the diagram of the resolutions is exact.

We now apply the functor $F$ to this diagram. We obtain a short sequence of complexes:

$$
0\to F(I')\to F(I)\to F(I'')\to0,
$$

which is exact because $I=I'\oplus I''$ is a direct sum and $F$ is left exact, so $F$ commutes with direct sums. We are now in a position to apply the construction of §1 to get the coboundary operator in the homology sequence:

$$
R^nF(M')\to R^nF(M)\to R^nF(M'')\xrightarrow{\delta^n}R^{n+1}F(M').
$$

This is legitimate because the right derived functor is independent of the chosen resolutions.

So far, we have proved (i), (ii), and (iii). To prove (iv), that is the naturality of the delta homomorphisms, it is necessary to go through a three-dimensional commutative diagram. At this point, I feel it is best to leave this to the reader, since it is just more of the same routine.

Finally, the last property (v) is obvious, for if $I$ is injective, then we can use the resolution

$$
0\to I\to I\to0
$$

to compute the derived functors, from which it is clear that $R^nF=0$ for $n>0$. This concludes the proof of Theorem 6.1.

In applications, it is useful to determine the derived functors by means of other resolutions besides injective ones (which are useful for theoretical purposes, but not for computational ones). Let again $F$ be a left exact additive functor. An object $X$ is called **$F$-acyclic** if $R^nF(X)=0$ for all $n>0$.

<span class="original-page-anchor" id="pdf-page-804" aria-hidden="true"></span>

**Theorem 6.2.** *Let*

$$
0\to M\to X^0\to X^1\to X^2\to\cdots
$$

*be a resolution of $M$ by $F$-acyclics. Let*

$$
0\to M\to I^0\to I^1\to I^2\to\cdots
$$

*be an injective resolution. Then there exists a morphism of complexes $X_M\to I_M$ extending the identity on $M$, and this morphism induces an isomorphism*

$$
H^nF(X)\approx H^nF(I)=R^nF(M)
$$

*for all $n\geqq0$.*

*Proof.* The existence of the morphism of complexes extending the identity on $M$ is merely Lemma 5.2. The usual proof of the theorem via spectral sequences can be formulated independently in the following manner, shown to me by David Benson. We need a lemma.

**Lemma 6.3.** *Let $Y^i$ $(i\geqq0)$ be $F$-acyclic, and suppose the sequence*

$$
0\to Y^0\to Y^1\to Y^2\to\cdots
$$

*is exact. Then*

$$
0\to F(Y^0)\to F(Y^1)\to F(Y^2)\to\cdots
$$

*is exact.*

*Proof.* Since $F$ is left exact, we have an exact sequence

$$
0\to F(Y^0)\to F(Y^1)\to F(Y^2).
$$

We want to show exactness at the next joint. We draw the cokernels:

![Cokernels in an exact sequence of F-acyclic objects](/library/volume-86/diagrams/pdf-0804-acyclic-cokernels.png)

So $Z_1=\operatorname{Coker}(Y^0\to Y^1)$; $Z_2=\operatorname{Coker}(Y^1\to Y^2)$; etc. Applying $F$ we have an exact sequence

$$
0\to F(Y^0)\to F(Y^1)\to F(Z^1)\to R^1F(Y^0)=0.
$$

<span class="original-page-anchor" id="pdf-page-805" aria-hidden="true"></span>

So $F(Z_1)=\operatorname{Coker}(F(Y^0)\to F(Y^1))$. We now consider the exact sequence

$$
0\to Z_1\to Y_2\to Y_3
$$

giving the exact sequence

$$
0\to F(Z^1)\to F(Y^2)\to F(Y^3)
$$

by the left-exactness of $F$, and proving what we wanted. But we can now continue by induction because $Z_1$ is $F$-acyclic, by the exact sequence

$$
0\to R^nF(Y^1)\to R^nF(Z^1)\to R^{n+1}F(Y^0)=0.
$$

This concludes the proof of Lemma 6.3.

We return to the proof of Theorem 6.2. The injective resolution

$$
0\to M\to I_M
$$

can be chosen such that the homomorphisms $X_n\to I_n$ are monomorphisms for $n\geqq0$, because the derived functor is independent of the choice of injective resolution. Thus we may assume without loss of generality that we have an exact diagram:

![Exact diagram comparing X and I and defining Y](/library/volume-86/diagrams/pdf-0805-acyclic-resolution-grid.png)

defining $Y^n$ as the appropriate cokernel of the vertical map.

Since $X^n$ and $I^n$ are acyclic, so is $Y^n$ from the exact sequence

$$
R^kF(I^n)\to R^kF(Y^n)\to R^{k+1}F(X^n).
$$

Applying $F$ we obtain a short exact sequence of complexes

$$
0\to F(X)\to F(I)\to F(Y)\to0.
$$

<span class="original-page-anchor" id="pdf-page-806" aria-hidden="true"></span>

whence the corresponding homology sequence

$$
H^{n-1}F(Y)\to H^nF(X)\to H^nF(I)\to H^nF(Y).
$$

Both extremes are $0$ by Lemma 6.3, so we get an isomorphism in the middle, which by definition is the isomorphism

$$
H^nF(X)\approx R^nF(M),
$$

thus proving the theorem.

### Left derived functors

We conclude this section by a summary of the properties of left derived functors.

We consider complexes going the other way,

$$
\to X_n\to\cdots\to X_2\to X_1\to X_0\to M\to0
$$

which we abbreviate by

$$
X_M\to M\to0.
$$

We call such a complex a **resolution** of $M$ if the sequence is exact. We call it a **projective resolution** if $X_n$ is projective for all $n\geqq0$.

*Given projective resolutions $X_M,Y_{M'}$ and a homomorphism*

$$
\varphi:M\to M'
$$

*there always exists a homomorphism $X_M\to Y_{M'}$ extending $\varphi$, and any two such are homotopic.*

In fact, one need only assume that $X_M$ is a projective resolution, and that $Y_{M'}$ is a resolution, not necessarily projective, for the proof to go through.

Let $T$ be a covariant additive functor. Fix a projective resolution of an object $M$,

$$
P_M\to M\to0.
$$

We define the **left derived functor** $L_nT$ by

$$
L_nT(M)=H_n(T(P)),
$$

where $T(P)$ is the complex

$$
\to T(P_n)\to\cdots\to T(P_2)\to T(P_1)\to T(P_0)\to0.
$$

The existence of homotopies shows that $L_nT(M)$ is uniquely determined up to a unique isomorphism if one changes the projective resolution.

We define $T$ to be **right exact** if an exact sequence

$$
M'\to M\to M''\to0
$$

<span class="original-page-anchor" id="pdf-page-807" aria-hidden="true"></span>

yields an exact sequence

$$
T(M')\to T(M)\to T(M'')\to0.
$$

*If $T$ is right exact, then we have immediately from the definitions*

$$
L_0T(M)\approx M.
$$

Theorems 6.1 and 6.2 then go over to this case with similar proofs. One has to replace “injectives” by “projectives” throughout, and in Theorem 6.1, the last condition states that for $n>0$,

$$
L_nT(P)=0\quad\text{if }P\text{ is projective}.
$$

Otherwise, it is just a question of reversing certain arrows in the proofs. For an example of such left derived functors, see Exercises 2–7 concerning the cohomology of groups.

## §7. DELTA-FUNCTORS

In this section, we axiomatize the properties stated in Theorem 6.1 following Grothendieck.

Let $\mathfrak{A},\mathfrak{B}$ be abelian categories. A (covariant) **$\delta$-functor** from $\mathfrak{A}$ to $\mathfrak{B}$ is a family of additive functors $F=\{F_n\}_{n\geqq0}$, and to each short exact sequence

$$
0\to M'\to M\to M''\to0
$$

an associated family of morphisms

$$
\delta^n:F^n(M'')\to F^{n+1}(M')
$$

with $n\geqq0$, satisfying the following conditions:

**DEL 1.** For each short exact sequence as above, there is a long exact sequence

$$
\begin{aligned}
0\to F^0(M')\to F^0(M)\to F^0(M'')\to F^1(M')\to\cdots\\
\to F^n(M')\to F^n(M)\to F^n(M'')\to F^{n+1}(M')\to
\end{aligned}
$$

**DEL 2.** For each morphism of one short exact sequence as above into another $0\to N'\to N\to N''\to0$, the $\delta$'s give a commutative diagram:

$$
\begin{array}{ccc}
F^n(M'')&\xrightarrow{\delta}&F^{n+1}(M')\\
\downarrow&&\downarrow\\
F^n(N'')&\xrightarrow{\delta}&F^{n+1}(N').
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-808" aria-hidden="true"></span>

Before going any further, it is useful to give another definition. Many proofs in homology theory are given by induction from one index to the next. It turns out that the only relevant data for going up by one index is given in two successive dimensions, and that the other indices are irrelevant. Therefore we generalize the notion of $\delta$-functor as follows.

A **$\delta$-functor defined in degrees $0,1$** is a pair of functors $(F^0,F^1)$ and to each short exact sequence

$$
0\to A'\to A\to A''\to0
$$

an associated morphism

$$
\delta:F^0(A'')\to F^1(A'')
$$

satisfying the two conditions as before, but putting $n=0$, $n+1=1$, and forgetting about all other integers $n$. We could also use any two consecutive positive integers to index the $\delta$-functor, or any sequence of consecutive integers $\geqq0$. In practice, only the case of all integers $\geqq0$ occurs, but for proofs, it is useful to have the flexibility provided by using only two indices, say $0,1$.

The $\delta$-functor $F$ is said to be **universal**, if given any other $\delta$-functor $G$ of $\mathfrak{A}$ into $\mathfrak{B}$, and given any morphism of functors

$$
f_0:F^0\to G^0,
$$

there exists a unique sequence of morphisms

$$
f_n:F^n\to G^n
$$

for all $n\geqq0$, which commute with the $\delta^n$ for each short exact sequence.

By the definition of universality, a $\delta$-functor $G$ such that $G^0=F^0$ is uniquely determined up to a unique isomorphism of functors. We shall give a condition for a functor to be universal.

An additive functor $F$ of $\mathfrak{A}$ into $\mathfrak{B}$ is called **erasable** if to each object $A$ there exists a monomorphism $u:A\to M$ for some $M$ such that $F(u)=0$. In practice, it even happens that $F(M)=0$, but we don't need it in the axiomatization.

**Linguistic note.** Grothendieck originally called the notion “effaceable” in French. The dictionary translation is “erasable,” as I have used above. Apparently people who did not know French have used the French word in English, but there is no need for this, since the English word is equally meaningful and convenient.

We say the functor is erasable **by injectives** if in addition $M$ can be taken to be injective.

<span class="original-page-anchor" id="pdf-page-809" aria-hidden="true"></span>

**Example.** Of course, a right derived functor is erasable by injectives, and a left derived functor by projectives. However, there are many cases when one wants erasability by other types of objects. In Exercises 9 and 14, dealing with the cohomology of groups, you will see how one erases the cohomology functor with induced modules, or regular modules when $G$ is finite. In the category of coherent sheaves in algebraic geometry, one erases the cohomology with locally free sheaves of finite rank.

**Theorem 7.1.** *Let $F=\{F^n\}$ be a covariant $\delta$-functor from $\mathfrak{A}$ into $\mathfrak{B}$. If $F^n$ is erasable for each $n>0$, then $F$ is universal.*

*Proof.* Given an object $A$, we erase it with a monomorphism $u$, and get a short exact sequence:

$$
0\to A\xrightarrow{\varphi}M\to X\to0.
$$

Let $G$ be another $\delta$-functor with given $f_0:F^0\to G^0$. We have an exact commutative diagram

![Exact diagram constructing f1](/library/volume-86/diagrams/pdf-0809-universality-construction.png)

We get the $0$ on the top right because of the erasability assumption that

$$
F^1(\varphi)=0.
$$

We want to construct

$$
f_1(A):F^1(A)\to G^1(A)
$$

which makes the diagram commutative, is functorial in $A$, and also commutes with the $\delta$. Commutativity in the left square shows that $\operatorname{Ker}\delta_F$ is contained in the kernel of $\delta_G\circ f_0$. Hence there exists a unique homomorphism

$$
f_1(A):F^1(A)\to G^1(A)
$$

which makes the right square commutative. We are going to show that $f_1(A)$ satisfies the desired conditions. The rest of the proof then proceeds by induction following the same pattern.

We first prove the functoriality in $A$.

Let $u:A\to B$ be a morphism. We form the push-out $P$ in the diagram

$$
\begin{array}{ccc}
A&\xrightarrow{\varphi}&M\\
{\scriptstyle u}\downarrow&&\downarrow\\
B&\longrightarrow&P
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-810" aria-hidden="true"></span>

Since $\varphi$ is a monomorphism, it follows that $B\to P$ is a monomorphism also. Then we let $P\to N$ be a monomorphism which erases $F_1$. This yields a commutative diagram

$$
\begin{array}{ccccccccc}
0&\longrightarrow&A&\longrightarrow&M&\longrightarrow&X&\longrightarrow&0\\
&&{\scriptstyle u}\downarrow&&{\scriptstyle v}\downarrow&&{\scriptstyle w}\downarrow&&\\
0&\longrightarrow&B&\longrightarrow&N&\longrightarrow&Y&\longrightarrow&0
\end{array}
$$

where $B\to N$ is the composite $B\to P\to N$, and $Y$ is defined to be the cokernel of $B\to N$.

Functoriality in $A$ means that the following diagram is commutative.

$$
\begin{array}{ccc}
F^1(A)&\xrightarrow{F^1(u)}&F^1(B)\\
{\scriptstyle f_1(A)}\downarrow&&\downarrow{\scriptstyle f_1(B)}\\
G^1(A)&\xrightarrow{F^1(u)}&G^1(B)
\end{array}
$$

This square is the right-hand side of the following cube:

![Cube proving functoriality](/library/volume-86/diagrams/pdf-0810-functoriality-cube.png)

All the faces of the cube are commutative except possibly the right-hand face. It is then a general fact that if the top maps here denoted by $\delta_F$ are epimorphisms, <span class="original-page-anchor" id="pdf-page-811" aria-hidden="true"></span>then the right-hand side is commutative also. This can be seen as follows. We start with $f_1(B)F^1(u)\delta_F$. We then use commutativity on the top of the cube, then the front face, then the left face, then the bottom, and finally the back face. This yields

$$
f_1(B)F^1(u)\delta_F=G^1(u)f_1(A)\delta_F.
$$

Since $\delta_F$ is an epimorphism, we can cancel $\delta_F$ to get what we want.

Second, we have to show that $f_1$ commutes with $\delta$. Let

$$
0\to A'\to A\to A''\to0
$$

be a short exact sequence. The same push-out argument as before shows that there exists an erasing monomorphism $0\to A'\to M$ and morphisms $v,w$ making the following diagram commutative:

$$
\begin{array}{ccccccccc}
0&\longrightarrow&A'&\longrightarrow&A&\longrightarrow&A''&\longrightarrow&0\\
&&{\scriptstyle\operatorname{id}}\downarrow&&{\scriptstyle v}\downarrow&&{\scriptstyle w}\downarrow&&\\
0&\longrightarrow&A'&\longrightarrow&M&\longrightarrow&X&\longrightarrow&0
\end{array}
$$

Here $X$ is defined as the appropriate cokernel of the bottom row. We now consider the following diagram:

![Diagram proving compatibility with delta](/library/volume-86/diagrams/pdf-0811-delta-compatibility-prism.png)

Our purpose is to prove that the right-hand face is commutative. The triangles on top and bottom are commutative by the definition of a $\delta$-functor. The <span class="original-page-anchor" id="pdf-page-812" aria-hidden="true"></span>left-hand square is commutative by the hypothesis that $f_0$ is a morphism of functors. The front square is commutative by the definition of $f_1(A')$. Therefore we find:

$$
\begin{aligned}
f_1(A')\delta_F&=f_1(A')\delta_F F^0(w)&&\text{(top triangle)}\\
&=\delta_F f_0F^0(w)&&\text{(front square)}\\
&=\delta_F G^0(w)f_0&&\text{(left square)}\\
&=\delta_F f_0&&\text{(bottom triangle)}.
\end{aligned}
$$

This concludes the proof of Theorem 7.1, since instead of the pair of indices $(0,1)$ we could have used $(n,n+1)$.

**Remark.** The morphism $f_1$ constructed in Theorem 7.1 depends functorially on $f_0$ in the following sense. Suppose we have three delta functors $F,G,H$ defined in degrees $0,1$. Suppose given morphisms

$$
f_0:F^0\to G^0\quad\text{and}\quad g_0:G^0\to H^0.
$$

Suppose that the erasing monomorphisms erase both $F$ and $G$. Then we can construct $f_1$ and $g_1$ by applying the theorem. On the other hand, the composite

$$
g_0f_0=h_0:F^0\to H^0
$$

is also a morphism of functors, and the theorem yields the existence of a morphism

$$
h_1:F^1\to H^1
$$

such that $(h_0,h_1)$ is a $\delta$-morphism. By uniqueness, we therefore have

$$
h_1=g_1f_1.
$$

This is what we mean by the functorial dependence as mentioned above.

**Corollary 7.2.** *Assume that $\mathfrak{A}$ has enough injectives. Then for any left exact functor $F:\mathfrak{A}\to\mathfrak{B}$, the derived functors $R^nF$ with $n\geqq0$ form a universal $\delta$-functor with $F\approx R^0F$, which is erasable by injectives. Conversely, if $G=\{G^n\}_{n\geqq0}$ is a universal $\delta$-functor, then $G^0$ is left exact, and the $G^n$ are isomorphic to $R^nG^0$ for each $n\geqq0$.*

*Proof.* If $F$ is a left exact functor, then the $\{R^nF\}_{n\geqq0}$ form a $\delta$-functor by Theorem 6.1. Furthermore, for any object $A$, let $u:A\to I$ be a monomorphism of $A$ into an injective. Then $R^nF(I)=0$ for $n>0$ by Theorem 6.1(iv), so $R^nF(u)=0$. Hence $R^nF$ is erasable for all $n>0$, and we can apply Theorem 7.1.

**Remark.** As usual, Theorem 7.1 applies to functors with different variance. Suppose $\{F^n\}$ is a family of contravariant additive functors, with $n$ ranging over <span class="original-page-anchor" id="pdf-page-813" aria-hidden="true"></span>a sequence of consecutive integers, say for simplicity $n\geqq0$. We say that $F$ is a **contravariant $\delta$-functor** if given an exact sequence

$$
0\to M'\to M\to M''\to0
$$

then there is an associated family of morphisms

$$
\delta^n:F^n(M')\to F^{n+1}(M')
$$

satisfying **DEL 1** and **DEL 2** with $M'$ interchanged with $M''$ and $N'$ interchanged with $N''$. We say that $F$ is **coerasable** if to each object $A$ there exists an epimorphism $u:M\to A$ such that $F(u)=0$. We say that $F$ is **universal** if given any other $\delta$-functor $G$ of $\mathfrak{A}$ into $\mathfrak{B}$ and given a morphism of functors

$$
f_0:F^0\to G^0
$$

there exists a unique sequence of morphisms

$$
f_n:F^n\to G^n
$$

for all $n\geqq0$ which commute with $\delta$ for each short exact sequence.

**Theorem 7.1′.** *Let $F=\{F^n\}$ ($n$ ranging over a consecutive sequence of integers $\geqq0$) be a contravariant $\delta$-functor from $\mathfrak{A}$ into $\mathfrak{B}$, and assume that $F^n$ is coerasable for $n\geqq1$. Then $F$ is universal.*

Examples of $\delta$-functors with the variances as in Theorems 7.1 and 7.1′ will be given in the next section in connection with bifunctors.

### Dimension shifting

Let $F=\{F^n\}$ be a contravariant delta functor with $n\geqq0$. Let $\mathcal{E}$ be a family of objects which erases $F^n$ for all $n\geqq1$, that is $F^n(E)=0$ for $n\geqq1$ and $E\in\mathcal{E}$. Then such a family allows us to do what is called **dimension shifting** as follows. Given an exact sequence

$$
0\to Q\to E\to M\to0
$$

with $E\in\mathcal{E}$, we get for $n\geqq1$ an exact sequence

$$
0=F^n(E)\to F^n(Q)\to F^{n+1}(M)\to F^{n+1}(E)=0,
$$

and therefore an isomorphism

$$
F^n(Q)\xrightarrow{\approx}F^{n+1}(M),
$$

which exhibits a shift of dimensions by one. More generally:

**Proposition 7.3.** *Let*

$$
0\to Q\to E_{n-1}\to\cdots\to E_0\to M\to0
$$

<span class="original-page-anchor" id="pdf-page-814" aria-hidden="true"></span>

*be an exact sequence, such that $E_i\in\mathcal{E}$. Then we have an isomorphism*

$$
F^p(Q)\approx F^{p+n}(M)\quad\text{for }p\geqq1.
$$

*Proof.* Let $Q=Q_n$. Also without loss of generality, take $p=1$. We may insert kernels and cokernels at each step as follows:

![Kernels and cokernels inserted into a resolution](/library/volume-86/diagrams/pdf-0814-dimension-shifting-zigzag.png)

Then shifting dimension with respect to each short exact sequence, we find isomorphisms

$$
F^1(Q_n)\approx F^2(Q_{n-1})\approx\cdots\approx F^{n+1}(M).
$$

This concludes the proof.

One says that $M$ has **$F$-dimension** $\leqq d$ if $F^n(M)=0$ for $n\geqq d+1$. By dimension shifting, we see that if $M$ has $F$-dimension $\leqq d$, then $Q$ has $F$-dimension $\leqq d-n$ in Proposition 7.3. In particular, if $M$ has $F$-dimension $n$, then $Q$ has $F$-dimension $0$.

The reader should rewrite all this formalism by changing notation, using for $F$ the standard functors arising from Hom in the first variable, on the category of modules over a ring, which has enough projectives to erase the left derived functors of

$$
A\mapsto\operatorname{Hom}(A,B),
$$

for $B$ fixed. We shall study this situation, suitably axiomatized, in the next section.

## §8. BIFUNCTORS

In an abelian category one often deals with Hom, which can be viewed as a functor in two variables; and also the tensor product, which is a functor in two variables, but their variance is different. In any case, these examples lead to the notion of **bifunctor**. This is an association

$$
(A,B)\mapsto T(A,B)
$$

<span class="original-page-anchor" id="pdf-page-815" aria-hidden="true"></span>

where $A,B$ are objects of abelian categories $\mathfrak{A}$ and $\mathfrak{B}$ respectively, with values in some abelian category. This means that $T$ is functorial in each variable, with the appropriate variance (there are four possibilities, with covariance and contravariance in all possible combinations); and if, say, $T$ is covariant in all variables, we also require that for homomorphisms $A'\to A$ and $B'\to B$ there is a commutative diagram

$$
\begin{array}{ccc}
T(A',B')&\longrightarrow&T(A',B)\\
\downarrow&&\downarrow\\
T(A,B')&\longrightarrow&T(A,B).
\end{array}
$$

If the variances are shuffled, then the arrows in the diagram are to be reversed in the appropriate manner. Finally, we require that as a functor in each variable, $T$ is additive.

Note that Hom is a bifunctor, contravariant in the first variable and covariant in the second. The tensor product is covariant in each variable.

The Hom functor is a bifunctor $T$ satisfying the following properties:

**HOM 1.** *$T$ is contravariant and left exact in the first variable.*

**HOM 2.** *$T$ is covariant and left exact in the second variable.*

**HOM 3.** *For any injective object $J$ the functor*

$$
A\mapsto T(A,J)
$$

*is exact.*

They are the only properties which will enter into consideration in this section. There is a possible fourth one which might come in other times:

**HOM 4.** *For any projective object $Q$ the functor*

$$
B\mapsto T(Q,B)
$$

*is exact.*

But we shall deal *non-symmetrically, and view $T$ as a functor of the second variable, keeping the first one fixed, in order to get derived functors of the second variable.* On the other hand, we shall also obtain a $\delta$-functor of the first variable by using the bifunctor, even though this $\delta$-functor is not a derived functor.

If $\mathfrak{B}$ has enough injectives, then we may form the right derived functors with respect to the second variable

$$
B\mapsto R^nT(A,B),\quad\text{also denoted by }R^nT_A(B),
$$

<span class="original-page-anchor" id="pdf-page-816" aria-hidden="true"></span>

fixing $A$, and viewing $B$ as variable. If $T=\operatorname{Hom}$, then this right derived functor is called **Ext**, so we have by definition

$$
\operatorname{Ext}^n(A,X)=R^n\operatorname{Hom}(A,X).
$$

We shall now give a criterion to compute the right derived functors in terms of the other (first) variable. We say that an object $A$ is **$T$-exact** if the functor $B\mapsto T(A,B)$ is exact. By a **$T$-exact resolution** of an object $A$, we mean a resolution

$$
\to M_1\to M_0\to A\to0
$$

where $M_n$ is $T$-exact for all $n\geqq0$.

**Examples.** Let $\mathfrak{A}$ and $\mathfrak{B}$ be the categories of modules over a commutative ring. Let $T=\operatorname{Hom}$. Then a $T$-exact object is by definition a projective module. Now let the **transpose** of $T$ be given by

$$
{}^tT(A,B)=T(B,A).
$$

Then a ${}^tT$-exact object is by definition an injective module.

If $T$ is the tensor product, such that $T(A,B)=A\otimes B$, then a $T$-exact object is called **flat**.

**Remark.** In the category of modules over a ring, there are enough projectives and injectives. But there are other situations when this is not the case. Readers who want to see all this abstract nonsense in action may consult [GriH 78], [Ha 77], not to speak of [SGA 6] and Grothendieck's collected works. It may genuinely happen in practice that $\mathfrak{B}$ has enough injectives but $\mathfrak{A}$ does not have enough projectives, so the situation is not all symmetric. Thus the functor $A\mapsto R^nT(A,B)$ for fixed $B$ is *not* a derived functor in the variable $A$. In the above references, we may take for $\mathfrak{A}$ the category of coherent sheaves on a variety, and for $\mathfrak{B}$ the category of all sheaves. We let $T=\operatorname{Hom}$. The locally free sheaves of finite rank are $T$-exact, and there are enough of them in $\mathfrak{A}$. There are enough injectives in $\mathfrak{B}$. And so it goes. The balancing act between $T$-exacts on one side, and injectives on the other is inherent to the situation.

**Lemma 8.1.** *Let $T$ be a bifunctor satisfying **HOM 1**, **HOM 2**. Let $A\in\mathfrak{A}$, and let $M_A\to A\to0$, that is*

$$
\to M_1\to M_0\to A\to0
$$

*be a $T$-exact resolution of $A$. Let $F^n(B)=H^n(T(M,B))$ for $B\in\mathfrak{B}$. Then $F$ is a $\delta$-functor and $F^0(B)=T(A,B)$. If in addition $T$ satisfies **HOM 3**, then $F^n(J)=0$ for $J$ injective and $n\geqq1$.*

<span class="original-page-anchor" id="pdf-page-817" aria-hidden="true"></span>

*Proof.* Given an exact sequence

$$
0\to B'\to B\to B''\to0
$$

we get an exact sequence of complexes

$$
0\to T(M,B')\to T(M,B)\to T(M,B'')\to0,
$$

whence a cohomology sequence which makes $F$ into a $\delta$-functor. For $n=0$ we get $F^0(B)=T(A,B)$ because $X\mapsto T(X,B)$ is contravariant and left exact for $X\in\mathfrak{A}$. If $B$ is injective, then $F^n(B)=0$ for $n\geqq1$ by **HOM 3**, because $X\mapsto T(X,B)$ is exact. This proves the lemma.

**Proposition 8.2.** *Let $T$ be a bifunctor satisfying **HOM 1**, **HOM 2**, **HOM 3**. Assume that $\mathfrak{B}$ has enough injectives. Let $A\in\mathfrak{A}$. Let*

$$
M_A\to A\to0
$$

*be a $T$-exact resolution of $A$. Then the two $\delta$-functors*

$$
B\mapsto R^nT(A,B)\quad\text{and}\quad B\mapsto H^n(T(M,B))
$$

*are isomorphic as universal $\delta$-functors vanishing on injectives, for $n\geqq1$, and such that*

$$
R^0T(A,B)=H^0(T(M),B)=T(A,B).
$$

*Proof.* This comes merely from the universality of a $\delta$-functor erasable by injectives.

We now look at the functoriality in $A$.

**Lemma 8.3.** *Let $T$ satisfy **HOM 1**, **HOM 2**, and **HOM 3**. Assume that $\mathfrak{B}$ has enough injectives. Let*

$$
0\to A'\to A\to A''\to0
$$

*be a short exact sequence. Then for fixed $B$, we have a long exact sequence*

$$
\begin{aligned}
0\to T(A'',B)\to T(A,B)\to T(A',B)\to\\
\to R^1T(A'',B)\to R^1T(A,B)\to R^1T(A',B)\to
\end{aligned}
$$

*such that the association*

$$
A\mapsto R^nT(A,B)
$$

*is a $\delta$-functor.*

<span class="original-page-anchor" id="pdf-page-818" aria-hidden="true"></span>

*Proof.* Let $0\to B\to I_B$ be an injective resolution of $B$. From the exactness of the functor $A\mapsto T(A,J)$, for $J$ injective we get a short exact sequence of complexes

$$
0\to T(A'',I_B)\to T(A,I_B)\to T(A',I_B)\to0.
$$

Taking the associated long exact sequence of homology groups of these complexes yields the sequence of the proposition. (The functorality is left to the readers.)

If $T=\operatorname{Hom}$, then the exact sequence looks like

$$
\begin{aligned}
0\to\operatorname{Hom}(A'',B)\to\operatorname{Hom}(A,B)\to\operatorname{Hom}(A',B)\to\\
\to\operatorname{Ext}^1(A'',B)\to\operatorname{Ext}^1(A,B)\to\operatorname{Ext}^1(A',B)\to
\end{aligned}
$$

and so forth.

We shall say that $\mathfrak{A}$ has **enough $T$-exacts** if given an object $A$ in $\mathfrak{A}$ there is a $T$-exact $M$ and an epimorphism

$$
M\to A\to0.
$$

**Proposition 8.4.** *Let $T$ satisfy **HOM 1**, **HOM 2**, **HOM 3**. Assume that $\mathfrak{B}$ has enough injectives. Fix $B\in\mathfrak{B}$. Then the association*

$$
A\mapsto R^nT(A,B)
$$

*is a contravariant $\delta$-functor on $\mathfrak{A}$ which vanishes on $T$-exacts, for $n\geqq1$. If $\mathfrak{A}$ has enough $T$-exacts, then this functor is universal, coerasable by $T$-exacts, with value*

$$
R^0T(A,B)=T(A,B).
$$

*Proof.* By Lemma 8.3 we know that the association is a $\delta$-functor, and it vanishes on $T$-exacts by Lemma 8.1. The last statement is then merely an application of the universality of erasable $\delta$-functors.

**Corollary 8.5.** *Let $\mathfrak{A}=\mathfrak{B}$ be the category of modules over a ring. For fixed $B$, let $\operatorname{ext}^n(A,B)$ be the left derived functor of $A\mapsto\operatorname{Hom}(A,B)$, obtained by means of projective resolutions of $A$. Then*

$$
\operatorname{ext}^n(A,B)=\operatorname{Ext}^n(A,B).
$$

*Proof.* Immediate from Proposition 8.4.

The following proposition characterizes $T$-exacts cohomologically.

<span class="original-page-anchor" id="pdf-page-819" aria-hidden="true"></span>

**Proposition 8.6.** *Let $T$ be a bifunctor satisfying **HOM 1**, **HOM 2**, **HOM 3**. Assume that $\mathfrak{B}$ has enough injectives. Then the following conditions are equivalent:*

**TE 1.** *$A$ is $T$-exact.*

**TE 2.** *For every $B$ and every integer $n\geqq1$, we have $R^nT(A,B)=0$.*

**TE 3.** *For every $B$ we have $R^1T(A,B)=0$.*

*Proof.* Let

$$
0\to B\to I^0\to I^1\to
$$

be an injective resolution of $B$. By definition, $R^nT(A,B)$ is the $n$-th homology of the sequence

$$
0\to T(A,I^0)\to T(A,I^1)\to T(A,I^2)\to
$$

If $A$ is $T$-exact, then this sequence is exact for $n\geqq1$, so the homology is $0$ and **TE 1** implies **TE 2**. Trivially, **TE 2** implies **TE 3**. Finally assume **TE 3**. Given an exact sequence

$$
0\to B'\to B\to B''\to0,
$$

we have the homology sequence

$$
0\to T(A,B')\to T(A,B)\to T(A,B'')\to R^1T(A,B')\to.
$$

If $R^1T(A,B')=0$, then by definition $A$ is $T$-exact, thus proving the proposition.

We shall say that an object $A$ has **$T$-dimension** $\leqq d$ if

$$
R^nT(A,B)=0\quad\text{for }n>d\text{ and all }B.
$$

Then the proposition states in particular that *$A$ is $T$-exact if and only if $A$ has $T$-dimension $0$.*

**Proposition 8.7.** *Let $T$ satisfy **HOM 1**, **HOM 2**, **HOM 3**. Assume that $\mathfrak{B}$ has enough injectives. Suppose that an object $A$ admits a resolution*

$$
0\to E_d\to E_{d-1}\to\cdots\to E_0\to A\to0
$$

*where $E_0,\ldots,E_d$ are $T$-exact. Then $A$ has $T$-dimension $\leqq d$. Assume this is the case. Let*

$$
0\to Q\to L_{d-1}\to\cdots\to L_0\to A\to0
$$

*be a resolution where $L_0,\ldots,L_{d-1}$ are $T$-exact. Then $Q$ is $T$-exact also.*

*Proof.* By dimension shifting we conclude that $Q$ has $T$-dimension $0$, whence $Q$ is $T$-exact by Proposition 8.6.

<span class="original-page-anchor" id="pdf-page-820" aria-hidden="true"></span>

Proposition 8.7, like others, is used in the context of modules over a ring. In that case, we can take $T=\operatorname{Hom}$, and

$$
R^nT(A,B)=\operatorname{Ext}^n(A,B).
$$

For $A$ to have $T$-dimension $\leqq d$ means that

$$
\operatorname{Ext}^n(A,B)=0\quad\text{for }n>d\text{ and all }B.
$$

Instead of $T$-exact, one can then read projective in the proposition.

Let us formulate the analogous result for a bifunctor that will apply to the tensor product. Consider the following properties.

**TEN 1.** *$T$ is covariant and right exact in the first variable.*

**TEN 2.** *$T$ is covariant and right exact in the second variable.*

**TEN 3.** *For any projective object $P$ the functor*

$$
A\mapsto T(A,P)
$$

*is exact.*

As for Hom, there is a possible fourth property which will play no role in this section:

**TEN 4.** *For any projective object $Q$ the functor*

$$
B\mapsto T(Q,B)
$$

*is exact.*

**Proposition 8.2′.** *Let $T$ be a bifunctor satisfying **TEN 1**, **TEN 2**, **TEN 3**. Assume that $\mathfrak{B}$ has enough projectives. Let $A\in\mathfrak{A}$. Let*

$$
M_A\to A\to0
$$

*be a $T$-exact resolution of $A$. Then the two $\delta$-functors*

$$
B\mapsto L_nT(A,B)\quad\text{and}\quad B\mapsto H_n(T(M,B))
$$

*are isomorphic as universal $\delta$-functors vanishing on projectives, and such that*

$$
L_0T(A,B)=H_0(T(M),B)=T(A,B).
$$

**Lemma 8.3′.** *Assume that $T$ satisfies **TEN 1**, **TEN 2**, **TEN 3**. Assume that $\mathfrak{B}$ has enough projectives. Let*

$$
0\to A'\to A\to A''\to0
$$

<span class="original-page-anchor" id="pdf-page-821" aria-hidden="true"></span>

*be a short exact sequence. Then for fixed $B$, we have a long exact sequence:*

$$
\begin{aligned}
\to L_1T(A',B)\to L_1T(A,B)\to L_1T(A'',B)\to\\
\to T(A',B)\to T(A,B)\to T(A'',B)\to0
\end{aligned}
$$

*which makes the association $A\mapsto L_nT(A,B)$ a $\delta$-functor.*

**Proposition 8.4′.** *Let $T$ satisfy **TEN 1**, **TEN 2**, **TEN 3**. Assume that $\mathfrak{B}$ has enough projectives. Fix $B\in\mathfrak{B}$. Then the association*

$$
A\mapsto L_nT(A,B)
$$

*is a contravariant $\delta$-functor on $\mathfrak{A}$ which vanishes on $T$-exacts for $n\geqq1$. If $\mathfrak{A}$ has enough $T$-exacts, then this functor is universal, coerasable by $T$-exacts, with the value*

$$
L_0T(A,B)=T(A,B).
$$

**Corollary 8.8.** *If there is a bifunctorial isomorphism $T(A,B)\approx T(B,A)$, and if $B$ is $T$-exact, then for all $A$, $L_nT(A,B)=0$ for $n\geqq1$. In short, $T$-exact implies acyclic.*

*Proof.* Let $M_A=P_A$ be a projective resolution in Proposition 8.2′. By hypotheses, $X\mapsto T(X,B)$ is exact so $H_n(T(P,B))=0$ for $n\geqq1$; so the corollary is a consequence of the proposition.

The above corollary is formulated so as to apply to the tensor product.

**Proposition 8.6′.** *Let $T$ be a bifunctor satisfying **TEN 1**, **TEN 2**, **TEN 3**. Assume that $\mathfrak{B}$ has enough projectives. Then the following conditions are equivalent:*

**TE 1.** *$A$ is $T$-exact.*

**TE 2.** *For every $B$ and every integer $n\geqq1$ we have $L_nT(A,B)=0$.*

**TE 3.** *For every $B$, we have $L_1T(A,B)=0$.*

*Proof.* We repeat the proof of 8.6 so the reader can see the arrows pointing in different ways.

Let

$$
\to Q_1\to Q_0\to B\to0
$$

be a projective resolution of $B$. By definition, $L_nT(A,B)$ is the $n$-th homology of the sequence

$$
\to T(A,Q_1)\to T(A,Q_0)\to0.
$$

<span class="original-page-anchor" id="pdf-page-822" aria-hidden="true"></span>

If $A$ is $T$-exact, then this sequence is exact for $n\geqq1$, so the homology is $0$, and **TE 1** implies **TE 2**. Trivially, **TE 2** implies **TE 3**. Finally, assume **TE 3**. Given an exact sequence

$$
0\to B'\to B\to B''\to0
$$

we have the homology sequence

$$
\to L_1T(A,B'')\to T(A,B')\to T(A,B)\to T(A,B'')\to0.
$$

If $L_1T(A,B'')$ is $0$, then by definition, $A$ is $T$-exact, thus proving the proposition.

## §9. SPECTRAL SEQUENCES

This section is included for convenience of reference, and has two purposes: first, to draw attention to an algebraic gadget which has wide applications in topology, differential geometry, and algebraic geometry, see Griffiths-Harris, [GrH 78]; second, to show that the basic description of this gadget in the context in which it occurs most frequently can be done in just a few pages.

In the applications mentioned above, one deals with a filtered complex (which we shall define later), and a complex may be viewed as a graded object, with a differential $d$ of degree $1$. To simplify the notation at first, we shall deal with filtered objects and omit the grading index from the notation. This index is irrelevant for the construction of the spectral sequence, for which we follow Godement.

So let $F$ be an object with a differential (i.e. endomorphism) $d$ such that $d^2=0$. We assume that $F$ is **filtered**, that is that we have a sequence

$$
F=F^0\supset F^1\supset F^2\supset\cdots\supset F^n\supset F^{n+1}=\{0\},
$$

and that $dF^p\subset F^p$. This data is called a **filtered differential object**. (We assume that the filtration ends with $0$ after a finite number of steps for convenience.)

One defines the **associated graded object**

$$
\operatorname{Gr}F=\bigoplus_{p\geqq0}\operatorname{Gr}^pF\quad\text{where}\quad\operatorname{Gr}^pF=F^p/F^{p+1}.
$$

In fact, $\operatorname{Gr}F$ is a complex, with a differential of degree $0$ induced by $d$ itself, and we have the homology $H(\operatorname{Gr}^pF)$.

The filtration $\{F^p\}$ also induces a filtration on the homology $H(F,d)=H(F)$; namely we let

$$
H(F)^p=\text{image of }H(F^p)\text{ in }H(F).
$$

<span class="original-page-anchor" id="pdf-page-823" aria-hidden="true"></span>

Since $d$ maps $F^p$ into itself, $H(F^p)$ is the homology of $F^p$ with respect to the restriction of $d$ to $F^p$, and it has a natural image in $H(F)$ which yields this filtration. In particular, we then obtain a graded object associated with the filtered homology, namely

$$
\operatorname{Gr}H(F)=\bigoplus\operatorname{Gr}^pH(F).
$$

A **spectral sequence** is a sequence $\{E_r,d_r\}$ ($r\geqq0$) of graded objects

$$
E_r=\bigoplus_{p\geqq0}E_r^p
$$

together with homomorphisms (also called **differentials**) of degree $r$,

$$
d_r:E_r^p\to E_r^{p+r}
$$

satisfying $d_r^2=0$, and such that the homology of $E_r$ is $E_{r+1}$, that is

$$
H(E_r)=E_{r+1}.
$$

In practice, one usually has $E_r=E_{r+1}=\cdots$ for $r\geqq r_0$. This limit object is called $E_\infty$, and one says that the spectral sequence **abuts to** $E_\infty$. Actually, to be perfectly strict, instead of equalities one should really be given isomorphisms, but for simplicity, we use equalities.

**Proposition 9.1.** *Let $F$ be a filtered differential object. Then there exists a spectral sequence $\{E_r\}$ with:*

$$
E_0^p=F^p/F^{p+1};\qquad E_1^p=H(\operatorname{Gr}^pF);\qquad E_\infty^p=\operatorname{Gr}^pH(F).
$$

*Proof.* Define

$$
\boxed{\begin{aligned}
Z_r^p&=\{x\in F^p\text{ such that }dx\in F^{p+r}\}\\
E_r^p&=Z_r^p/[dZ_{r-1}^{p-(r-1)}+Z_{r-1}^{p+1}].
\end{aligned}}
$$

The definition of $E_r^p$ makes sense, since $Z_r^p$ is immediately verified to contain $dZ_{r-1}^{p-(r-1)}+Z_{r-1}^{p+1}$. Furthermore, $d$ maps $Z_r^p$ into $Z_r^{p+r}$, and hence includes a homomorphism

$$
d_r:E_r^p\to E_r^{p+r}.
$$

We shall now compute the homology and show that it is what we want.

First, for the cycles: An element $x\in Z_r^p$ represents a cycle of degree $p$ in $E_r$ if and only if $dx\in dZ_{r-1}^{p+1}+Z_{r-1}^{p+r+1}$, in other words

$$
dx=dy+z,\quad\text{with }y\in Z_{r-1}^{p+1}\quad\text{and}\quad z\in Z_{r-1}^{p+r+1}.
$$

<span class="original-page-anchor" id="pdf-page-824" aria-hidden="true"></span>

Write $x=y+u$, so $du=z$. Then $u\in F^p$ and $du\in F^{p+r+1}$, that is $u\in Z_{r+1}^p$. It follows that

$$
p\text{-cycles of }E_r=(Z_{r+1}^p+Z_{r-1}^{p+1})/(dZ_{r-1}^{p-r+1}+Z_{r-1}^{p+1}).
$$

On the other hand, the $p$-boundaries in $E_r$ are represented by elements of $dZ_r^{p-r}$, which contains $dZ_{r-1}^{p-r+1}$. Hence

$$
p\text{-boundaries of }E_r=(dZ_r^{p-r}+Z_{r-1}^{p+1})/(dZ_{r-1}^{p-r+1}+Z_{r-1}^{p+1}).
$$

Therefore

$$
\begin{aligned}
H^p(E_r)&=(Z_{r+1}^p+Z_{r-1}^{p+1})/(dZ_r^{p-r}+Z_{r-1}^{p+1})\\
&=Z_{r+1}^p/(Z_{r+1}^p\cap(dZ_r^{p-r}+Z_{r-1}^{p+1})).
\end{aligned}
$$

Since

$$
Z_{r+1}^p\supset dZ_r^{p-r}\quad\text{and}\quad Z_{r+1}^p\cap Z_{r-1}^{p+1}=Z_r^{p+1},
$$

it follows that

$$
H^p(E_r)=Z_{r+1}^p/(dZ_r^{p-r}+Z_r^{p+1})=E_{r+1}^p,
$$

thus proving the property of a spectral sequence.

**Remarks.** It is sometimes useful in applications to note the relation

$$
dZ_{r-1}^{p-(r-1)}+Z_{r-1}^{p+1}=Z_r^p\cap(dF^{p-r+1}+F^{p+1}).
$$

The verification is immediate, but Griffiths-Harris use the expression on the right in defining the spectral sequence, whereas Godement uses the expression on the left as we have done above. Thus the spectral sequence may also be defined by

$$
\boxed{E_r^p=Z_r^p\quad\bmod(dF^{p-r+1}+F^{p+1}).}
$$

This is to be interpreted in the sense that $Z\bmod S$ means

$$
(Z+S)/S\quad\text{or}\quad Z/(Z\cap S).
$$

The term $E_0^p$ is $F^p/F^{p+1}$ immediately from the definitions, and by the general property already proved, we get $E_1^p=H(F^p/F^{p+1})$. As to $E_\infty^p$, for $r$ large we have $Z_r^p=Z^p=\text{cycles in }F^p$, and

$$
\boxed{E_\infty^p=Z^p/(Z^{p+1}+(dF^0\cap F^p))}
$$

<span class="original-page-anchor" id="pdf-page-825" aria-hidden="true"></span>

which is independent of $r$, and is precisely $\operatorname{Gr}^pH(F)$, namely the $p$-graded component of $H(F)$, thus proving the theorem.

The differential $d_1$ can be specified as follows.

**Proposition 9.2.** *The homomorphism*

$$
d_1:E_1^p\to E_1^{p+1}
$$

*is the coboundary operator arising from the exact sequence*

$$
0\to F^{p+1}/F^{p+2}\to F^p/F^{p+2}\to F^p/F^{p+1}\to0
$$

*viewing each term as a complex with differential induced by $d$.*

*Proof.* Indeed, the coboundary

$$
\delta:E_1^p=H(F^p/F^{p+1})\to H(F^{p+1}/F^{p+2})=E_1^{p+1}
$$

is defined on a representative cycle $z$ by $dz$, which is the same way that we defined $d_1$.

In most applications, the filtered differential object is itself graded, because it arises from the following situation. Let $K$ be a complex, $K=(K^p,d)$ with $p\geqq0$ and $d$ of degree $1$. By a **filtration** $FK$, also called a **filtered complex**, we mean a decreasing sequence of subcomplexes

$$
K=F^0K\supset F^1K\supset F^2K\supset\cdots\supset F^nK\supset F^{n+1}K=\{0\}.
$$

Observe that a short exact sequence of complexes

$$
0\to K'\to K\to K''\to0
$$

gives rise to a filtration $K\supset K'\supset\{0\}$, viewing $K'$ as a subcomplex.

To each filtered complex $FK$ we associated the complex

$$
\operatorname{Gr}FK=\operatorname{Gr}K=\bigoplus_{p\geqq0}\operatorname{Gr}^pK,
$$

where

$$
\operatorname{Gr}^pK=F^pK/F^{p+1}K,
$$

and the differential is the obvious one. The filtration $F^pK$ on $K$ also induces a filtration $F^pH(K)$ on the cohomology, by

$$
F^pH^q(K)=F^pZ^q/F^pB^q.
$$

<span class="original-page-anchor" id="pdf-page-826" aria-hidden="true"></span>

The associated graded homology is

$$
\operatorname{Gr}H(K)=\bigoplus_{p,q}\operatorname{Gr}^pH^q(K),
$$

where

$$
\operatorname{Gr}^pH^q(K)=F^pH^q(K)/F^{p+1}H^q(K).
$$

A **spectral sequence** is a sequence $\{E_r,d_r\}$ ($r\geqq0$) of bigraded objects

$$
E_r=\bigoplus_{p,q\geqq0}E_r^{p,q}
$$

together with homomorphisms (called **differentials**)

$$
d_r:E_r^{p,q}\to E_r^{p+r,q-r+1}\quad\text{satisfying}\quad d_r^2=0,
$$

and such that the homology of $E_r$ is $E_{r+1}$, that is

$$
H(E_r)=E_{r+1}.
$$

A spectral sequence is usually represented by the following picture:

![Spectral sequence differential in the bigraded lattice](/library/volume-86/diagrams/pdf-0826-spectral-differential-lattice.png)

In practice, one usually has $E_r=E_{r+1}=\cdots$ for $r\geqq r_0$. This limit object is called $E_\infty$, and one says that the spectral sequence abuts to $E_\infty$.

**Proposition 9.3.** *Let $FK$ be a filtered complex. Then there exists a spectral sequence $\{E_r\}$ with:*

$$
\begin{aligned}
E_0^{p,q}&=F^pK^{p+q}/F^{p+1}K^{p+q};\\
E_1^{p,q}&=H^{p+q}(\operatorname{Gr}^pK);\\
E_\infty^{p,q}&=\operatorname{Gr}^p(H^{p+q}(K)).
\end{aligned}
$$

*The last relation is usually written*

$$
E_r\Rightarrow H(K),
$$

*and we say that the spectral sequence abuts to $H(K)$.*

<span class="original-page-anchor" id="pdf-page-827" aria-hidden="true"></span>

The statement of Proposition 9.3 is merely a special case of Proposition 9.1, taking into account the extra graduation.

One of the main examples is the spectral sequence associated with a double complex

$$
K=\bigoplus_{p,q\geqq0}K^{p,q}
$$

which is a bigraded object, together with differentials

$$
d':K^{p,q}\to K^{p+1,q}\quad\text{and}\quad d'':K^{p,q}\to K^{p,q+1}
$$

satisfying

$$
d'^2=d''^2=0\quad\text{and}\quad d'd''+d''d'=0.
$$

We denote the double complex by $(K,d',d'')$. The associated single complex $(\operatorname{Tot}(K),D)$ (Tot for **total complex**), abbreviated $K^*$, is defined by

$$
K^n=\bigoplus_{p+q=n}K^{p,q}\quad\text{and}\quad D=d'+d''.
$$

There are two filtrations on $(K^*,D)$ given by

$$
\begin{aligned}
{}'F^pK^n&=\bigoplus_{\substack{p'+q=n\\p'\geqq p}}K^{p',q}\\
{}''F^qK^n&=\bigoplus_{\substack{p+q'=n\\q'\geqq q}}K^{p,q''}.
\end{aligned}
$$

There are two spectral sequences $\{{}'E_r\}$ and $\{{}''E_r\}$, both abutting to $H(\operatorname{Tot}(K))$. For applications, see [GrH 78], Chapter 3, §5; and also, for instance, [FuL 85], Chapter V. There are many situations when dealing with a double complex directly is a useful substitute for using spectral sequences, which are derived from double complexes anyhow.

We shall now derive the existence of a spectral sequence in one of the most important cases, the **Grothendieck spectral sequence** associated with the composite of two functors. *We assume that our abelian category has enough injectives.*

Let $C=\bigoplus C^p$ be a complex, and suppose $C^p=0$ if $p<0$ for simplicity. We define **injective resolution** of $C$ to be a resolution

$$
0\to C\to I^0\to I^1\to I^2\to\cdots
$$

written briefly

$$
0\to C\to I_C
$$

such that each $I^j$ is a complex, $I^j=\bigoplus I^{j,p}$, with differentials

$$
d^{j,p}:I^{j,p}\to I^{j,p+1}
$$

<span class="original-page-anchor" id="pdf-page-828" aria-hidden="true"></span>

and such that $I^{j,p}$ is an injective object. Then in particular, for each $p$ we get an injective resolution of $C^p$, namely:

$$
0\to C^p\to I^{0,p}\to I^{1,p}\to\cdots
$$

We let:

$$
\begin{aligned}
Z^{j,p}&=\operatorname{Ker}d^{j,p}=\text{cycles in degree }p\\
B^{j,p}&=\operatorname{Im}d^{j,p-1}=\text{boundaries in degree }p\\
H^{j,p}&=Z^{j,p}/B^{j,p}=\text{homology in degree }p.
\end{aligned}
$$

We then get complexes

$$
\begin{aligned}
0&\to Z^p(C)\to Z^{0,p}\to Z^{1,p}\to\\
0&\to B^p(C)\to B^{0,p}\to B^{1,p}\to\\
0&\to H^p(C)\to H^{0,p}\to H^{1,p}\to
\end{aligned}
$$

We say that the resolution $0\to C\to I_C$ is **fully injective** if these three complexes are injective resolutions of $Z^p(C)$, $B^p(C)$ and $H^p(C)$ respectively.

**Lemma 9.4.** *Let*

$$
0\to M'\to M\to M''\to0
$$

*be a short exact sequence. Let*

$$
0\to M'\to I_{M'}\quad\text{and}\quad0\to M''\to I_{M''}
$$

*be injective resolutions of $M'$ and $M''$. Then there exists an injective resolution*

$$
0\to M\to I_M
$$

*of $M$ and morphisms which make the following diagram exact and commutative:*

$$
\begin{array}{ccccccccc}
0&\longrightarrow&I_{M'}&\longrightarrow&I_M&\longrightarrow&I_{M''}&\longrightarrow&0\\
&&\uparrow&&\uparrow&&\uparrow&&\\
0&\longrightarrow&M'&\longrightarrow&M&\longrightarrow&M''&\longrightarrow&0\\
&&\uparrow&&\uparrow&&\uparrow&&\\
&&0&&0&&0&&
\end{array}
$$

*Proof.* The proof is the same as at the beginning of the proof of Theorem 6.1.

<span class="original-page-anchor" id="pdf-page-829" aria-hidden="true"></span>

**Lemma 9.5.** *Given a complex $C$ there exists a fully injective resolution of $C$.*

*Proof.* We insert the kernels and cokernels in $C$, giving rise to the short exact sequences with boundaries $B^p$ and cycles $Z^p$:

$$
\begin{aligned}
0&\to B^p\to Z^p\to H^p\to0\\
0&\to Z^{p-1}\to C^{p-1}\to B^p\to0.
\end{aligned}
$$

We proceed inductively. We start with an injective resolution of

$$
0\to Z^{p-1}\to C^{p-1}\to B^p\to0
$$

using Lemma 9.4. Next let

$$
0\to H^p\to I_{H^p}
$$

be an injective resolution of $H^p$. By Lemma 9.4 there exists an injective resolution

$$
0\to Z^p\to I_{Z^p}
$$

which fits in the middle of the injective resolutions we already have for $B^p$ and $H^p$. This establishes the inductive step, and concludes the proof.

Given a left exact functor $G$ on an abelian category with enough injectives, we say that an object $X$ is **$G$-acyclic** if $R^pG(X)=0$ for $p\geqq1$. Of course,

$$
R^0G(X)=G(X).
$$

**Theorem 9.6. (Grothendieck spectral sequence).** *Let*

$$
T:\mathfrak{A}\to\mathfrak{B}\quad\text{and}\quad G:\mathfrak{B}\to\mathfrak{C}
$$

*be covariant left exact functors such that if $I$ is injective in $\mathfrak{A}$, then $T(I)$ is $G$-acyclic. Then for each $A$ in $\mathfrak{A}$ there is a spectral sequence $\{E_r(A)\}$, such that*

$$
E_2^{p,q}(A)=R^pG(R^qT(A))
$$

*and $E_r^{p,q}$ abuts (with respect to $p$) to $R^{p+q}(GT)(A)$, where $q$ is the grading index.*

*Proof.* Let $A$ be an object of $\mathfrak{A}$, and let $0\to A\to C_A$ be an injective resolution. We apply $T$ to get a complex

$$
TC:\quad0\to TC^0\to TC^1\to TC^2\to
$$

By Lemma 9.5 there exists a fully injective resolution

$$
0\to TC\to I_{TC}
$$

which has the $2$-dimensional representation:

<span class="original-page-anchor" id="pdf-page-830" aria-hidden="true"></span>

![Two-dimensional fully injective resolution of TC](/library/volume-86/diagrams/pdf-0830-fully-injective-grid.png)

Then $GI$ is a double complex. Let $\operatorname{Tot}(GI)$ be the associated single complex. We now consider each of the two possible spectral sequences in succession, which we denote by ${}^1E_r^{p,q}$ and ${}^2E_r^{p,q}$.

The first one is the easiest. For fixed $p$, we have an injective resolution

$$
0\to TC^p\to I_{TC}^p
$$

where we write $I_{TC}^p$ instead of $I_{TC^p}$. This is the $p$-th column in the diagram. By definition of derived functors, $GI^p$ is a complex whose homology is $R^qG$, in other words, taking homology with respect to $d''$ we have

$$
{}''H^{p,q}(GI)=H^q(GI^p)=(R^qG)(TC^p).
$$

By hypothesis, $C^p$ injective implies that $(R^qG)(TC^p)=0$ for $q>0$. Since $G$ is left exact, we have $R^0G(TC^p)=TC^p$. Hence we get

$$
{}''H^{p,q}(GI)=\begin{cases}GT(C^p)&\text{if }q=0,\\0&\text{if }q>0.\end{cases}
$$

Hence the non-zero terms are on the $p$-axis, which looks like

$$
0\to GT(C^0)\to GT(C^1)\to GT(C^2)\to
$$

Taking ${}'H^p$ we get

$$
{}^1E_2^{p,q}(A)=\begin{cases}R^p(GT)(A)&\text{if }q=0\\0&\text{if }q>0.\end{cases}
$$

This yields

$$
H^n(\operatorname{Tot}(GI))\approx R^n(GT)(A).
$$

<span class="original-page-anchor" id="pdf-page-831" aria-hidden="true"></span>

The second one will use the full strength of Lemma 9.5, which had not been used in the first part of the proof, so it is now important that the resolution $I_{TC}$ is fully injective. We therefore have injective resolutions

$$
\begin{aligned}
0&\to Z^p(TC)\to{}^1Z^{0,p}\to{}^1Z^{1,p}\to{}^1Z^{2,p}\to\\
0&\to B^p(TC)\to{}^1B^{0,p}\to{}^1B^{1,p}\to{}^1B^{2,p}\to\\
0&\to H^p(TC)\to{}^1H^{0,p}\to{}^1H^{1,p}\to{}^1H^{2,p}\to
\end{aligned}
$$

and the exact sequences

$$
\begin{aligned}
0&\to{}^1Z^{q,p}\to I^{q,p}\to{}^1B^{q+1,p}\to0\\
0&\to{}^1B^{q,p}\to{}^1Z^{q,p}\to{}^1H^{q,p}\to0
\end{aligned}
$$

split because of the injectivity of the terms. We denote by $I^{(p)}$ the $p$-th row of the double complex $I=\{I^{q,p}\}$. Then we find:

$$
\begin{aligned}
{}'H^{q,p}(GI)&=H^q(GI^{(p)})=G{}^1Z^{q,p}/G{}^1B^{q,p}&&\text{by the first split sequence}\\
&=G{}'H^{q,p}(I)&&\text{by the second split sequence}
\end{aligned}
$$

because applying the functor $G$ to a split exact sequence yields a split exact sequence.

Then

$$
{}^2E_2^{p,q}={}''H^p({}'H^{q,p}(GI))=H^p(G{}'H^{q,p}(I)).
$$

By the full injectivity of the resolutions, the complex ${}'H^{q,p}(I)$ with $p\geqq0$ is an injective resolution of

$$
H^q(TC)=(R^qT)(A).
$$

Furthermore, we have

$$
H^p(G{}'H^{q,p})=R^pG(R^qT(A)),
$$

since a derived functor is the homology of an injective resolution. This proves that $(R^pG)R^qT(A))$ abuts to $R^n(GT)(A)$, and concludes the proof of the theorem.

Just to see the spectral sequence at work, we give one application relating it to the Euler characteristic discussed in §3.

Let $\mathfrak{A}$ have enough injectives, and let

$$
T:\mathfrak{A}\to\mathfrak{B}
$$

be a covariant left exact functor. Let $\mathfrak{F}_{\mathfrak{A}}$ be a family of objects in $\mathfrak{A}$ giving rise to a **K-group**. More precisely, in a short exact sequence in $\mathfrak{A}$, if two of the objects lie in $\mathfrak{F}_{\mathfrak{A}}$, then so does the third. We also assume that the objects of $\mathfrak{F}_{\mathfrak{A}}$ have **finite $RT$-dimension**, which means by definition that if $A\in\mathfrak{F}_{\mathfrak{A}}$ then $R^iT(A)=0$ <span class="original-page-anchor" id="pdf-page-832" aria-hidden="true"></span>for all $i$ sufficiently large. We could take $\mathfrak{F}_{\mathfrak{A}}$ in fact to be the family of all objects in $\mathfrak{A}$ which have finite $RT$-dimension.

We define the **Euler characteristic associated with $T$** on $\mathbf{K}(\mathfrak{F}_{\mathfrak{A}})$ to be

$$
\chi_T(A)=\sum_{i=0}^\infty(-1)^i\operatorname{cl}(R^iT(A)).
$$

The cl denotes the class in the **K-group** $\mathbf{K}(\mathfrak{F}_{\mathfrak{B}})$ associated with some family $\mathfrak{F}_{\mathfrak{B}}$ of objects in $\mathfrak{B}$, and such that $R^iT(A)\in\mathfrak{F}_{\mathfrak{B}}$ for all $A\in\mathfrak{F}_{\mathfrak{A}}$. This is the minimum required for the formula to make sense.

**Lemma 9.7.** *The map $\chi_T$ extends to a homomorphism*

$$
\mathbf{K}(\mathfrak{F}_{\mathfrak{A}})\to\mathbf{K}(\mathfrak{F}_{\mathfrak{B}}).
$$

*Proof.* Let

$$
0\to A'\to A\to A''\to0
$$

be an exact sequence in $\mathfrak{F}$. Then we have the cohomology sequence

$$
\to R^iT(A')\to R^iT(A)\to R^iT(A'')\to R^{i+1}T(A')\to
$$

in which all but a finite number of terms are $0$. Taking the alternating sum in the **K-group** shows that $\chi_T$ is an Euler–Poincaré map, and concludes the proof.

Note that we have merely repeated something from §3, in a jazzed up context.

In the next theorem, we have another functor

$$
G:\mathfrak{B}\to\mathfrak{C},
$$

and we also have a family $\mathfrak{F}_{\mathfrak{C}}$ giving rise to a **K-group** $\mathbf{K}(\mathfrak{F}_{\mathfrak{C}})$. We suppose that we can perform the above procedure at each step, and also need some condition so that we can apply the spectral sequence. So, precisely, we assume:

**CHAR 1.** For all $i$, $R^iT$ maps $\mathfrak{F}_{\mathfrak{A}}$ into $\mathfrak{F}_{\mathfrak{B}}$, $R^iG$ maps $\mathfrak{F}_{\mathfrak{B}}$ into $\mathfrak{F}_{\mathfrak{C}}$, and $R^i(GT)$ maps $\mathfrak{F}_{\mathfrak{A}}$ into $\mathfrak{F}_{\mathfrak{C}}$.

**CHAR 2.** Each subobject of an element of $\mathfrak{F}_{\mathfrak{A}}$ lies in $\mathfrak{F}_{\mathfrak{A}}$ and has finite $RT$- and $R(GT)$-dimension; each subobject of an element of $\mathfrak{F}_{\mathfrak{B}}$ lies in $\mathfrak{F}_{\mathfrak{B}}$ and has finite $RG$-dimension.

**Theorem 9.8.** *Assume that $T:\mathfrak{A}\to\mathfrak{B}$ and $G:\mathfrak{B}\to\mathfrak{C}$ satisfy the conditions **CHAR 1** and **CHAR 2**. Also assume that $T$ maps injectives to $G$-acyclics. Then*

$$
\chi_G\circ\chi_T=\chi_{GT}.
$$

<span class="original-page-anchor" id="pdf-page-833" aria-hidden="true"></span>

*Proof.* By Theorem 9.6, the Grothendieck spectral sequence of the composite functor implies the existence of a filtration

$$
\cdots\subset F^pR^n(GT)(A)\subset F^{p+1}R^n(GT)(A)\subset\cdots
$$

of $R^n(GT)(A)$, such that

$$
F^{p+1}/F^p\approx E_\infty^{p,n-p}.
$$

Then

$$
\begin{aligned}
\chi_{GT}(A)&=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(R^n(GT)(A))\\
&=\sum_{n=0}^\infty(-1)^n\sum_{p=0}^\infty\operatorname{cl}(E_\infty^{p,n-p})\\
&=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_\infty^n).
\end{aligned}
$$

On the other hand,

$$
\chi_T(A)=\sum_{q=0}^\infty(-1)^q\operatorname{cl}(R^qT(A))
$$

and so

$$
\begin{aligned}
\chi_G\circ\chi_T(A)&=\sum_{q=0}^\infty(-1)^q\chi_G(R^qT(A))\\
&=\sum_{q=0}^\infty(-1)^q\sum_{p=0}^\infty(-1)^p\operatorname{cl}(R^pG(R^qT(A)))\\
&=\sum_{n=0}^\infty(-1)^n\sum_{p=0}^n\operatorname{cl}(R^pG(R^{n-p}T(A)))\\
&=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_2^n).
\end{aligned}
$$

Since $E_{r+1}$ is the homology of $E_r$, we get

$$
\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_2^n)=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_3^n)=\cdots=\sum_{n=0}^\infty(-1)^n\operatorname{cl}(E_\infty^n).
$$

This concludes the proof of the theorem.

<span class="original-page-anchor" id="pdf-page-834" aria-hidden="true"></span>

## EXERCISES

**1.** Prove that the example of the standard complex given in §1 is actually a complex, and is exact, so it gives a resolution of $\mathbf{Z}$. [*Hint:* To show that the sequence of the standard complex is exact, choose an element $z\in S$ and define $h:E^i\to E^{i+1}$ by letting

$$
h(x_0,\ldots,x_i)=(z,x_0,\ldots,x_i).
$$

Prove that $dh+hd=\operatorname{id}$, and that $dd=0$. Exactness follows at once.]

### Cohomology of groups

**2.** Let $G$ be a group. Use $G$ as the set $S$ in the standard complex. Define an action of $G$ on the standard complex $E$ by letting

$$
x(x_0,\ldots,x_i)=(xx_0,\ldots,xx_i).
$$

Prove that each $E_i$ is a free module over the group ring $\mathbf{Z}[G]$. Thus if we let $R=\mathbf{Z}[G]$ be the group ring, and consider the category $\operatorname{Mod}(G)$ of $G$-modules, then the standard complex gives a free resolution of $\mathbf{Z}$ in this category.

**3.** The standard complex $E$ was written in homogeneous form, so the boundary maps have a certain symmetry. There is another complex which exhibits useful features as follows. Let $F^i$ be the free $\mathbf{Z}[G]$-module having for basis $i$-tuples (rather than $(i+1)$-tuples) $(x_1,\ldots,x_i)$. For $i=0$ we take $F_0=\mathbf{Z}[G]$ itself. Define the boundary operator by the formula

$$
\begin{aligned}
d(x_1,\ldots,x_i)&=x_1(x_2,\ldots,x_i)+\sum_{j=1}^{i-1}(-1)^j(x_1,\ldots,x_jx_{j+1},\ldots,x_i)\\
&\qquad+(-1)^{i+1}(x_1,\ldots,x_i).
\end{aligned}
$$

Show that $E\approx F$ (as complexes of $G$-modules) via the association

$$
(x_1,\ldots,x_i)\mapsto(1,x_1,x_1x_2,\ldots,x_1x_2\cdots x_i),
$$

and that the operator $d$ given for $F$ corresponds to the operator $d$ given for $E$ under this isomorphism.

**4.** If $A$ is a $G$-module, let $A^G$ be the submodule consisting of all elements $v\in A$ such that $xv=v$ for all $x\in G$. Thus $A^G$ has trivial $G$-action. (This notation is convenient, but is *not* the same as for the induced module of Chapter XVIII.)

(a) Show that if $H^q(G,A)$ denotes the $q$-th homology of the complex $\operatorname{Hom}_G(E,A)$, then $H^0(G,A)=A^G$. Thus the left derived functors of $A\mapsto A^G$ are the homology groups of the complex $\operatorname{Hom}_G(E,A)$, or for that matter, of the complex $\operatorname{Hom}(F,A)$, where $F$ is as in Exercise 3.

(b) Show that the group of $1$-cycles $Z^1(G,A)$ consists of those functions $f:G\to A$ satisfying

$$
f(x)+xf(y)=f(xy)\quad\text{for all }x,y\in G.
$$

Show that the subgroup of coboundaries $B^1(G,A)$ consists of those functions $f$ for which there exists an element $a\in A$ such that $f(x)=xa-a$. The factor group is then $H^1(G,A)$. See Chapter VI, §10 for the determination of a special case.

<span class="original-page-anchor" id="pdf-page-835" aria-hidden="true"></span>

(c) Show that the group of $2$-cocycles $Z^2(G,A)$ consists of those functions $f:G\to A$ satisfying

$$
xf(y,z)-f(xy,z)+f(x,yz)-f(x,y)=0.
$$

Such $2$-cocycles are also called **factor sets**, and they can be used to describe isomorphism classes of group extensions, as follows.

**5. Group extensions.** Let $W$ be a group and $A$ a normal subgroup, written multiplicatively. Let $G=W/A$ be the factor group. Let $F:G\to W$ be a choice of coset representatives. Define

$$
f(x,y)=F(x)F(y)F(xy)^{-1}.
$$

(a) Prove that $f$ is $A$-valued, and that $f:G\times G\to A$ is a $2$-cocycle.

(b) Given a group $G$ and an abelian group $A$, we view an extension $W$ as an exact sequence

$$
1\to A\to W\to G\to1.
$$

Show that if two such extensions are isomorphic then the $2$-cocycles associated to these extensions as in (a) define the same class in $H^1(G,A)$.

(c) Prove that the map which we obtained above from isomorphism classes of group extensions to $H^2(G,A)$ is a bijection.

**6. Morphisms of the cohomology functor.** Let $\lambda:G'\to G$ be a group homomorphism. Then $\lambda$ gives rise to an exact functor

$$
\Phi_\lambda:\operatorname{Mod}(G)\to\operatorname{Mod}(G'),
$$

because every $G$-module can be viewed as a $G'$-module by defining the operation of $\sigma'\in G'$ to be $\sigma'a=\lambda(\sigma')a$. Thus we obtain a cohomology functor $H^{G'}\circ\Phi_\lambda$.

Let $G'$ be a subgroup of $G$. In dimension $0$, we have a morphism of functors

$$
\lambda^*:H_G^0\to H_{G'}^0\circ\Phi_\lambda\quad\text{given by the inclusion }A^G\hookrightarrow A^{G'}=\Phi_\lambda(A)^{G'}.
$$

(a) Show that there is a unique morphism of $\delta$-functors

$$
\lambda^*:H_G\to H_{G'}\circ\Phi_\lambda
$$

which has the above effect on $H_G^0$. We have the following important special cases.

**Restriction.** Let $H$ be a subgroup of $G$. Let $A$ be a $G$-module. A function from $G$ into $A$ restricts to a function from $H$ into $A$. In this way, we get a natural homomorphism called the **restriction**

$$
\operatorname{res}:H^q(G,A)\to H^q(H,A).
$$

**Inflation.** Suppose that $H$ is normal in $G$. Let $A^H$ be the subgroup of $A$ consisting of those elements fixed by $H$. Then it is immediately verified that $A^H$ is stable under $G$, and so is a $G/H$-module. The inclusion $A^H\hookrightarrow A$ induces a homomorphism

$$
H_G^q(u)=u_q:H^q(G,A^H)\to H^q(A).
$$

Define the **inflation**

$$
\operatorname{inf}_{G/H}^H:H^q(G/H,A^H)\to H^q(G,A)
$$

<span class="original-page-anchor" id="pdf-page-836" aria-hidden="true"></span>

as the composite of the functorial morphism $H^q(G/H,A^H)\to H^q(G,A^H)$ followed by the induced homomorphism $u_q=H_G^q(u)$ as above.

In dimension $0$, the inflation gives the identity $(A^H)^{G/H}=A^G$.

(b) Show that the inflation can be expressed on the standard cochain complex by the natural map which to a function of $G/H$ in $A^H$ associates a function of $G$ into $A^H\subset A$.

(c) Prove that the following sequence is exact.

$$
0\to H^1(G/H,A^H)\xrightarrow{\operatorname{inf}}H^1(G,A)\xrightarrow{\operatorname{res}}H^1(H,A).
$$

(d) Describe how one gets an operation of $G$ on the cohomology functor $H_G$ “by conjugation” and functoriality.

(e) In (c), show that the image of restriction on the right actually lies in $H^1(H,A)^G$ (the fixed subgroup under $G$).

**Remark.** There is an analogous result for higher cohomology groups, whose proof needs a spectral sequence of Hochschild-Serre. See [La 96], Chapter VI, §2, Theorem 2. It is actually this version for $H^2$ which is applied to $H^2(G,K^*)$, when $K$ is a Galois extension, and is used in class field theory [ArT 67].

**7.** Let $G$ be a group, $B$ an abelian group and $M_G(B)=M(G,B)$ the set of mappings from $G$ into $B$. For $x\in G$ and $f\in M(G,B)$ define $([x]f)(y)=f(yx)$.

(a) Show that $B\mapsto M_G(B)$ is a covariant, additive, exact functor from $\operatorname{Mod}(\mathbf{Z})$ (category of abelian groups) into $\operatorname{Mod}(G)$.

(b) Let $G'$ be a subgroup of $G$ and $G=\bigcup x_jG'$ a coset decomposition. For $f\in M(G,B)$ let $f_j$ be the function in $M(G',B)$ such that $f_j(y)=f(x_jy)$. Show that the map

$$
f\mapsto\prod_j f_j
$$

is a $G'$-isomorphism from $M(G,B)$ to $\prod_jM(G',B)$.

**8.** For each $G$-module $A\in\operatorname{Mod}(G)$, define $\varepsilon_A:A\to M(G,A)$ by the condition $\varepsilon_A(a)=\text{the function }f_a$ such that $f_a(\sigma)=\sigma a$ for $\sigma\in G$. Show that $a\mapsto f_a$ is a $G$-module embedding, and that the exact sequence

$$
0\to A\xrightarrow{\varepsilon_A}M(G,A)\to X_A=\operatorname{coker}\varepsilon_A\to0
$$

splits over $\mathbf{Z}$. (In fact, the map $f\mapsto f(e)$ splits the left side arrow.)

**9.** Let $B\in\operatorname{Mod}(\mathbf{Z})$. Let $H^q$ be the left derived functor of $A\mapsto A^G$.

(a) Show that $H^q(G,M_G(B))=0$ for all $q>0$. [*Hint:* use a contracting homotopy

$$
s:C^r(G,M_G(B))\to C^{r-1}(G,M_G(B))\quad\text{by}\quad(sf)_{x_2,\ldots,x_r}(x)=f_{x,x_2,\ldots,x_r}(1).
$$

Show that $f=sdf+dsf$.] Thus $M_G$ erases the cohomology functor.

(b) Also show that for all subgroups $G'$ of $G$ one has $H^q(G',M_G(B))=0$ for $q>0$.

**10.** Let $G$ be a group and $S$ a subgroup. Show that the bifunctors

$$
(A,B)\mapsto\operatorname{Hom}_G(A,M_G^S(B))\quad\text{and}\quad(A,B)\mapsto\operatorname{Hom}_S(A,B)
$$

on $\operatorname{Mod}(G)\times\operatorname{Mod}(S)$ with value in $\operatorname{Mod}(\mathbf{Z})$ are isomorphic. The isomorphism is given by the maps

$$
\varphi\mapsto(a\mapsto g_a),\quad\text{for }\varphi\in\operatorname{Hom}_S(A,B),\text{ where }g_a(\sigma)=\varphi(\sigma a),\quad g_a\in M_G^S(B).
$$

<span class="original-page-anchor" id="pdf-page-837" aria-hidden="true"></span>

The inverse mapping is given by

$$
f\mapsto f(1)\quad\text{with }f\in\operatorname{Hom}_G(A,M_G^S(B)).
$$

Recall that $M_G^S(B)$ was defined in Chapter XVIII, §7 for the induced representation. Basically you should already know the above isomorphism.

**11.** Let $G$ be a group and $S$ a subgroup. Show that the map

$$
H^q(G,M_G^S(B))\to H^q(S,B)\quad\text{for }B\in\operatorname{Mod}(S),
$$

obtained by composing the restriction $\operatorname{res}_S^G$ with the $S$-homomorphism $f\mapsto f(1)$, is an isomorphism for $q>0$. [*Hint:* Use the uniqueness theorem for cohomology functors.]

**12.** Let $G$ be a group. Let $\varepsilon:\mathbf{Z}[G]\to\mathbf{Z}$ be the homomorphism such that $\varepsilon(\sum n(x)x)=\sum n(x)$. Let $I_G$ be its kernel. Prove that $I_G$ is an ideal of $\mathbf{Z}[G]$ and that there is an isomorphism of functors (on the category of groups)

$$
G/G^c\approx I_G/I_G^2,\quad\text{by }xG^c\mapsto(x-1)+I_G^2.
$$

**13.** Let $A\in\operatorname{Mod}(G)$ and $\alpha\in H^1(G,A)$. Let $\{a(x)\}_{x\in G}$ be a standard $1$-cocycle representing $\alpha$. Show that there exists a $G$-homomorphism $f:I_G\to A$ such that $f(x-1)=a(x)$, so $f\in(\operatorname{Hom}(I_G,A))^G$. Show that the sequence

$$
0\to A=\operatorname{Hom}(\mathbf{Z},A)\to\operatorname{Hom}(\mathbf{Z}[G],A)\to\operatorname{Hom}(I_G,A)\to0
$$

is exact, and that if $\delta$ is the coboundary for the cohomology sequence, then $\delta(f)=-\alpha$.

### Finite groups

We now turn to the case of *finite* groups $G$. For such groups and a $G$-module $A$ we have the **trace**

$$
T_G:A\to A\quad\text{defined by}\quad T_G(a)=\sum_{\sigma\in G}\sigma a.
$$

We define a module $A$ to be **$G$-regular** if there exists a $\mathbf{Z}$-endomorphism $u:A\to A$ such that $\operatorname{id}_A=T_G(u)$. Recall that the operation of $G$ on $\operatorname{End}(A)$ is given by

$$
[\sigma]f(a)=\sigma f(\sigma^{-1}a)\quad\text{for }\sigma\in G.
$$

**14.** (a) Show that a projective object in $\operatorname{Mod}(G)$ is $G$-regular.

(b) Let $R$ be a commutative ring and let $A$ be in $\operatorname{Mod}_R(G)$ (the category of $(G,R)$-modules). Show that $A$ is $R[G]$-projective if and only if $A$ is $R$-projective and $R[G]$-regular, meaning that $\operatorname{id}_A=T_G(u)$ for some $R$-homomorphism $u:A\to A$.

**15.** Consider the exact sequences:

$$
\begin{aligned}
\text{(1)}\qquad&0\to I_G\to\mathbf{Z}[G]\xrightarrow{\varepsilon}\mathbf{Z}\to0\\
\text{(2)}\qquad&0\to\mathbf{Z}\xrightarrow{\varepsilon'}\mathbf{Z}[G]\to J_G\to0
\end{aligned}
$$

where the first one defines $I_G$, and the second is defined by the embedding

$$
\varepsilon':\mathbf{Z}\to\mathbf{Z}[G]\quad\text{such that }\varepsilon'(n)=n\left(\sum\sigma\right),
$$

i.e. on the “diagonal”. The cokernel of $\varepsilon'$ is $J_G$ by definition.

(a) Prove that both sequences (1) and (2) split in $\operatorname{Mod}(G)$.

<span class="original-page-anchor" id="pdf-page-838" aria-hidden="true"></span>

(b) Define $M'_G(A)=\mathbf{Z}[G]\otimes A$ (tensor product over $\mathbf{Z}$) for $A\in\operatorname{Mod}(G)$. Show that $M'_G(A)$ is $G$-regular, and that one gets exact sequences $(1_A)$ and $(2_A)$ by tensoring (1) and (2) with $A$. As a result one gets an embedding

$$
\varepsilon'_A=\varepsilon'\otimes\operatorname{id}:A=\mathbf{Z}\otimes A\to\mathbf{Z}[G]\otimes A.
$$

**16. Cyclic groups.** Let $G$ be a finite cyclic group of order $n$. Let $\sigma$ be a generator of $G$. Let $K^i=\mathbf{Z}[G]$ for $i>0$. Let $\varepsilon:K^0\to\mathbf{Z}$ be the augmentation as before. For $i$ odd $\geqq1$, let $d^i:K^i\to K^{i-1}$ be multiplication by $1-\sigma$. For $i$ even $\geqq2$, let $d^i$ be multiplication by $1+\sigma+\cdots+\sigma^{n-1}$. Prove that $K$ is a resolution of $\mathbf{Z}$. Conclude that:

*For $i$ odd:* $H^i(G,A)=A^G/T_GA$ where $T_G:a\mapsto(1+\sigma+\cdots+\sigma^{n-1})a$;

*For $i$ even $\geqq2$:* $H^i(G,A)=A_T/(1-\sigma)A$, where $A_T$ is the kernel of $T_G$ in $A$.

**17.** Let $G$ be a finite group. Show that there exists a $\delta$-functor $\mathbf{H}$ from $\operatorname{Mod}(G)$ to $\operatorname{Mod}(\mathbf{Z})$ such that:

(1) $\mathbf{H}^0$ is (isomorphic to) the functor $A\mapsto A^G/T_GA$.

(2) $\mathbf{H}^q(A)=0$ if $A$ is injective and $q>0$, and $\mathbf{H}^q(A)=0$ if $A$ is projective and $q$ is arbitrary.

(3) $\mathbf{H}$ is erased by $G$-regular modules. In particular, $\mathbf{H}$ is erased by $M_G$.

The $\delta$-functor of Exercise 17 is called the **special cohomology functor**. It differs from the other one only in dimension $0$.

**18.** Let $\mathbf{H}=\mathbf{H}_G$ be the special cohomology functor for a finite group $G$. Show that:

$$
\begin{aligned}
\mathbf{H}^0(I_G)&=0;\quad\mathbf{H}^0(\mathbf{Z})\approx\mathbf{H}^1(I)\approx\mathbf{Z}/n\mathbf{Z}\quad\text{where }n=\#(G);\\
\mathbf{H}^0(\mathbf{Q}/\mathbf{Z})&=\mathbf{H}^1(\mathbf{Z})=\mathbf{H}^2(I)=0\\
\mathbf{H}^1(\mathbf{Q}/\mathbf{Z})&\approx\mathbf{H}^2(\mathbf{Z})\approx\mathbf{H}^3(I)\approx\widehat{G}=\operatorname{Hom}(G,\mathbf{Q}/\mathbf{Z})\quad\text{by definition}.
\end{aligned}
$$

### Injectives

**19.** (a) Show that if an abelian group $T$ is injective in the category of abelian groups, then it is divisible.

(b) Let $A$ be a principal entire ring. Define the notion of divisibility by elements of $A$ for modules in a manner analogous to that for abelian groups. Show that an $A$-module is injective if and only if it is $A$-divisible. [The proof for $\mathbf{Z}$ should work in exactly the same way.]

**20.** Let $S$ be a multiplicative subset of the commutative Noetherian ring $A$. If $I$ is an injective $A$-module, show that $S^{-1}I$ is an injective $S^{-1}A$-module.

**21.** (a) Show that a direct sum of projective modules is projective.

(b) Show that a direct product of injective modules is injective.

**22.** Show that a factor module, direct summand, direct product, and direct sum of divisible modules are divisible.

**23.** Let $Q$ be a module over a commutative ring $A$. Assume that for every left ideal $J$ of $A$, every homomorphism $\varphi:J\to Q$ can be extended to a homomorphism of $A$ into $Q$. Show that $Q$ is injective. [*Hint:* Given $M'\subset M$ and $f:M'\to Q$, let $x_0\in M$ and $x_0\notin M'$. Let $J$ be the left ideal of elements $a\in A$ such that $ax_0\in M'$. Let $\varphi(a)=f(ax_0)$ and extend $\varphi$ to $A$, as can be done by hypothesis. Then show that <span class="original-page-anchor" id="pdf-page-839" aria-hidden="true"></span>one can extend $f$ to $M$ by the formula

$$
f(x'+bx_0)=f(x')+\varphi(b),
$$

for $x'\in M$ and $b\in A$. Then use Zorn's lemma. This is the same pattern of proof as the proof of Lemma 4.2.]

**24.** Let

$$
0\to I_1\to I_2\to I_3\to0
$$

be an exact sequence of modules. Assume that $I_1,I_2$ are injective.

(a) Show that the sequence splits.

(b) Show that $I_3$ is injective.

(c) If $I$ is injective and $I=M\oplus N$, show that $M$ is injective.

**25.** (Do this exercise after you have read about Noetherian rings.) Let $A$ be a Noetherian commutative ring, and let $Q$ be an injective $A$-module. Let $\mathfrak{a}$ be an ideal of $A$, and let $Q^{(\mathfrak{a})}$ be the subset of elements $x\in Q$ such that $\mathfrak{a}^nx=0$ for some $n$, depending on $x$. Show that $Q^{(\mathfrak{a})}$ is injective. [*Hint:* Use Exercise 23.]

**26.** Let $A$ be a commutative ring. Let $E$ be an $A$-module, and let $E^\wedge=\operatorname{Hom}_{\mathbf{Z}}(E,\mathbf{Q}/\mathbf{Z})$ be the dual module. Prove the following statements.

(a) A sequence

$$
0\to N\to M\to E\to0
$$

is exact if and only if the dual sequence

$$
0\to E^\wedge\to M^\wedge\to N^\wedge\to0
$$

is exact.

(b) Let $F$ be flat and $I$ injective in the category of $A$-modules. Show that $\operatorname{Hom}_A(F,I)$ is injective.

(c) $E$ is flat if and only if $E^\wedge$ is injective.

**27. Extensions of modules.** Let $M,N$ be modules over a ring. By an **extension** of $M$ by $N$ we mean an exact sequence

$$
\text{(*)}\qquad0\to N\to E\to M\to0.
$$

We shall now define a map from such extensions to $\operatorname{Ext}^1(M,N)$. Let $P$ be projective, with a surjective homomorphism onto $M$, so we get an exact sequence

$$
\text{(**)}\qquad0\to K\xrightarrow{w}P\xrightarrow{p}M\to0
$$

where $K$ is defined to be the kernel. Since $P$ is projective, there exists a homomorphism $u:P\to E$, and depending on $u$ a unique homomorphism $v:K\to N$ making the diagram commutative:

$$
\begin{array}{ccccccccc}
0&\longrightarrow&K&\longrightarrow&P&\longrightarrow&M&\longrightarrow&0\\
&&{\scriptstyle v}\downarrow&&{\scriptstyle u}\downarrow&&{\scriptstyle\operatorname{id}}\downarrow&&\\
0&\longrightarrow&N&\longrightarrow&E&\longrightarrow&M&\longrightarrow&0
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-840" aria-hidden="true"></span>

On the other hand, we have the exact sequence

$$
\text{(***)}\qquad0\to\operatorname{Hom}(M,N)\to\operatorname{Hom}(P,N)\to\operatorname{Hom}(K,N)\to\operatorname{Ext}^1(M,N)\to0,
$$

with the last term on the right being equal to $0$ because $\operatorname{Ext}^1(P,N)=0$. To the extension (\*) we associate the image of $v$ in $\operatorname{Ext}^1(M,N)$.

Prove that this association is a bijection between isomorphism classes of extensions (i.e. isomorphism classes of exact sequences as in (\*)), and $\operatorname{Ext}^1(M,N)$. [*Hint:* Construct an inverse as follows. Given an element $e$ of $\operatorname{Ext}^1(M,N)$, using an exact sequence (\*\*), there is some element $v\in\operatorname{Hom}(K,N)$ which maps on $e$ in (\*\*\*). Let $E$ be the push-out of $v$ and $w$. In other words, let $J$ be the submodule of $N\oplus P$ consisting of all elements $(v(x),-w(x))$ with $x\in K$, and let $E=(N\oplus P)/J$. Show that the map $y\mapsto(y,0)\bmod J$ gives an injection of $N$ into $E$. Show that the map $N\oplus P\to M$ vanishes on $J$, and so gives a surjective homomorphism $E\to M\to0$. Thus we obtain an exact sequence (\*); that is, an extension of $M$ by $N$. Thus to each element of $\operatorname{Ext}^1(M,N)$ we have associated an isomorphism class of extensions of $M$ by $N$. Show that the maps we have defined are inverse to each other between isomorphism classes of extensions and elements of $\operatorname{Ext}^1(M,N)$.]

**28.** Let $R$ be a principal entire ring. Let $a\in R$. For every $R$-module $N$, prove:

(a) $\operatorname{Ext}^1(R/aR,N)=N/aN$.

(b) For $b\in R$ we have $\operatorname{Ext}^1(R/aR,R/bR)=R/(a,b)$, where $(a,b)$ is the g.c.d of $a$ and $b$, assuming $ab\ne0$.

### Tensor product of complexes.

**29.** Let $K=\bigoplus K_p$ and $L=\bigoplus L_q$ be two complexes indexed by the integers, and with boundary maps lower indices by $1$. Define $K\otimes L$ to be the direct sum of the modules $(K\otimes L)_n$, where

$$
(K\otimes L)_n=\bigoplus_{p+q=n}K_p\otimes L_q.
$$

Show that there exist unique homomorphisms

$$
d=d_n:(K\otimes L)_n\to(K\otimes L)_{n-1}
$$

such that

$$
d(x\otimes y)=d(x)\otimes y+(-1)^p x\otimes d(y).
$$

Show that $K\otimes L$ with these homomorphisms is a complex, that is $d\circ d=0$.

**30.** Let $K,L$ be double complexes. We write $K_{i\cdot}$ and $L_{i\cdot}$ for the ordinary column complexes of $K$ and $L$ respectively. Let $\varphi:K\to L$ be a homomorphism of double complexes. Assume that each homomorphism

$$
\varphi_i:K_{i\cdot}\to L_{i\cdot}
$$

is a homology isomorphism.

(a) Prove that $\operatorname{Tot}(\varphi):\operatorname{Tot}(K)\to\operatorname{Tot}(L)$ is a homology isomorphism. (If you want to see this worked out, cf. [FuL 85], Chapter V, Lemma 5.4.)

(b) Prove Theorem 9.8 using (a) instead of spectral sequences.

<span class="original-page-anchor" id="pdf-page-841" aria-hidden="true"></span>

### Bibliography

[ArT 68] E. ARTIN and J. TATE, *Class Field Theory*, Benjamin, 1968; Addison-Wesley, 1991

[At 61] M. ATIYAH, Characters and cohomology of finite groups, *Pub. IHES* **9** (1961), pp. 5–26

[At 67] M. ATIYAH, *K-theory*, Benjamin, 1967; reprinted Addison-Wesley, 1991

[ABP 73] M. ATIYAH, R. BOTT, and R. PATODI, On the heat equation and the index theorem, *Invent. Math.* **19** (1973), pp. 279–330

[Ba 68] H. BASS, *Algebraic K-theory*, Benjamin, 1968

[Bo 69] R. BOTT, *Lectures on $K(X)$*, Benjamin, 1969

[BtD 85] T. BROCKER and T. TOM DIECK, *Representations of Compact Lie Groups*, Springer Verlag, 1985

[CaE 57] H. CARTAN and S. EILENBERG, *Homological Algebra*, Princeton University Press, 1957

[CuR 81] C. CURTIS and I. REINER, *Methods of Representation Theory*, John Wiley & Sons, 1981

[ES 52] S. EILENBERG and N. STEENROD, *Foundations of Algebraic Topology*, Princeton University Press, 1952

[FuL 85] W. FULTON and S. LANG, *Riemann-Roch algebra*, Springer Verlag, 1985

[Go 58] R. GODEMENT, *Théorie des faisceaux*, Hermann Paris, 1958

[GreH 81] M. GREENBERG and J. HARPER, *Algebraic Topology: A First Course*, Benjamin-Addison-Wesley, 1981

[GriH 78] P. GRIFFITHS and J. HARRIS, *Principles of algebraic geometry*, Wiley Interscience 1978

[Gro 57] A. GROTHENDIECK, Sur quelques points d’algèbre homologique, *Tohoku Math. J.* **9** (1957) pp. 119–221

[Gro 68] A. GROTHENDIECK, *Classes de Chern et représentations linéaires des groupes discrets*, Dix exposés sur la cohomologie étale des schémas, North-Holland, Amsterdam, 1968

[Gu 91] R. GUNNING, *Introduction to holomorphic functions of several variables*, Vol. III Wadsworth & Brooks/Cole, 1990

[Ha 77] R. HARTSHORNE, *Algebraic Geometry*, Springer Verlag, 1977

[HiS 70] P. J. HILTON and U. STAMMBACH, *A Course in Homological Algebra*, Graduate Texts in Mathematics, Springer Verlag, 1970.

[La 96] S. LANG, *Topics in cohomology of groups*, Springer Lecture Notes, 1996

[Man 69] J. MANIN, *Lectures on the K-functor in Algebraic Geometry*, *Russian Math Surveys* **24**(5) (1969) pp. 1–89

[Mat 70] H. MATSUMURA, *Commutative Algebra*, Second Edition, Benjamin-Cummings, 1981

[No 68] D. NORTHCOTT, *Lessons on Rings, Modules and Multiplicities*, Cambridge University Press, 1968

[No 76] D. NORTHCOTT, *Finite Free Resolutions*, Cambridge University Press, 1976

[Ro 79] J. ROTMAN, *Introduction to Homological Algebra*, Academic Press, 1979

[Se 64] J.-P. SERRE, *Cohomologie Galoisienne*, Springer Lecture Notes **5**, 1964

<span class="original-page-anchor" id="pdf-page-842" aria-hidden="true"></span>

[Se 65] J.-P. SERRE, *Algèbre locale, multiplicités*, Springer Lecture Notes **11** (1965) Third Edition 1975

[SGA 6] P. BERTHELOT, A. GROTHENDIECK, L. ILLUSIE et al. *Théorie des intersections et théorème de Riemann-Roch*, Springer Lecture Notes 146, 1970

[Sh 72] S. SHATZ, *Profinite groups, arithmetic and geometry*, Ann. of Math Studies, Princeton University Press 1972
