---
title: "Introduction to categories"
description: "《Introduction to Representation Theory》English。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"Quiver representations","link":"/library/volume-88/original-chapter-006"}
next: {"text":"Homological algebra","link":"/library/volume-88/original-chapter-008"}
---

# Introduction to categories

<span class="original-page-anchor" id="pdf-page-185" aria-hidden="true"></span>

## 7.1. The definition of a category

We have now seen many examples of representation theories and of operations with representations (direct sum, tensor product, induction, restriction, reflection functors, etc.). A context in which one can systematically talk about this is provided by **category theory**.

Category theory was founded by Saunders Mac Lane and Samuel Eilenberg in 1942–1945. It is a fairly abstract theory which seemingly has no content, for which reason it was christened “abstract nonsense” (see Section 7.10). Nevertheless, it is a very flexible and powerful language, which has become totally indispensable in many areas of mathematics, such as algebraic geometry, topology, representation theory, and many others.

We will now give a very short introduction to category theory, highlighting its relevance to the topics in representation theory we have discussed. For a serious acquaintance with category theory, the reader may use, for instance, the classical book [McL].

**Definition 7.1.1.** A **category** $\mathcal C$ is the following data:

(i) A class of objects $\operatorname{Ob}(\mathcal C)$.

<span class="original-page-anchor" id="pdf-page-186" aria-hidden="true"></span>

(ii) For every objects $X,Y\in\operatorname{Ob}(\mathcal C)$, the class $\operatorname{Hom}_{\mathcal C}(X,Y)=\operatorname{Hom}(X,Y)$ of morphisms (or arrows) from $X,Y$ (for $f\in\operatorname{Hom}(X,Y)$, one may write $f:X\to Y$).

(iii) For any objects $X,Y,Z\in\operatorname{Ob}(\mathcal C)$, a composition map

$$
\operatorname{Hom}(Y,Z)\times\operatorname{Hom}(X,Y)\longrightarrow\operatorname{Hom}(X,Z),\qquad(f,g)\longmapsto f\circ g.
$$

This data is required to satisfy the following axioms:

**1.** The composition is associative, i.e., $(f\circ g)\circ h=f\circ(g\circ h)$.

**2.** For each $X\in\operatorname{Ob}(\mathcal C)$, there is a morphism $1_X\in\operatorname{Hom}(X,X)$, called the **unit morphism**, such that $1_X\circ f=f$ and $g\circ 1_X=g$ for any $f,g$ for which compositions make sense.

**Remark 7.1.2.** We will write $X\in\mathcal C$ instead of $X\in\operatorname{Ob}(\mathcal C)$.

**Example 7.1.3.** **1.** The category **Sets** of sets (morphisms are arbitrary maps).

**2.** The categories **Groups**, **Rings** (morphisms are homomorphisms).

**3.** The category $\mathbf{Vect}_k$ of vector spaces over a field $k$ (morphisms are linear maps).

**4.** The category $\operatorname{Rep}(A)$ of representations of an algebra $A$ (morphisms are homomorphisms of representations).

**5.** The category of topological spaces (morphisms are continuous maps).

**6.** The homotopy category of topological spaces (morphisms are homotopy classes of continuous maps).

**Important remark.** Unfortunately, one cannot simplify this definition by replacing the word “class” by the much more familiar word “set”. Indeed, this would rule out the important Example 7.1.3(1), as it is well known that there is no set of all sets and that working with such a set leads to contradictions. The precise definition of a class and the precise distinction between a class and a set is the subject of set theory and cannot be discussed here. Luckily, for most practical purposes (in particular, in these notes) this distinction is not essential.

<span class="original-page-anchor" id="pdf-page-187" aria-hidden="true"></span>

We also mention that in many examples, including Examples 7.1.3(1)–(6), the word “class” in part (ii) of Definition 7.1.1 can be replaced by “set”. Categories with this property (that $\operatorname{Hom}(X,Y)$ is a set for any $X,Y$) are called **locally small**; many categories that we encounter are of this kind.

**Definition 7.1.4.** A **full subcategory** of a category $\mathcal C$ is a category $\mathcal C'$ whose objects are a subclass of objects of $\mathcal C$, and $\operatorname{Hom}_{\mathcal C'}(X,Y)=\operatorname{Hom}_{\mathcal C}(X,Y)$.

**Example 7.1.5.** The category **AbelianGroups** is a full subcategory of the category **Groups**.

Sometimes the collection $\operatorname{Hom}(X,Y)$ of morphisms from $X$ to $Y$ in a given locally small category $\mathcal C$ is not just a set but has some additional structure (say, the structure of an abelian group, or a vector space over some field). In this case one says that $\mathcal C$ is **enriched over** another category $\mathcal D$ (which is a monoidal category, i.e., has a product operation and a unit object under this product, e.g., the category of abelian groups or vector spaces with the tensor product operation). This means that for each $X,Y\in\mathcal C$, $\operatorname{Hom}(X,Y)$ is an object of $\mathcal D$, and the composition $\operatorname{Hom}(Y,Z)\times\operatorname{Hom}(X,Y)\to\operatorname{Hom}(X,Z)$ is a morphism in $\mathcal D$. E.g., if $\mathcal D$ is the category of vector spaces, this means that the composition is bilinear, i.e., gives rise to a linear map $\operatorname{Hom}(Y,Z)\otimes\operatorname{Hom}(X,Y)\to\operatorname{Hom}(X,Z)$. For a more detailed discussion of this, we refer the reader to [McL].

**Example 7.1.6.** The category $\operatorname{Rep}(A)$ of representations of a $k$-algebra $A$ is enriched over the category of $k$-vector spaces.

## 7.2. Functors

We would like to define arrows between categories. Such arrows are called **functors**.

**Definition 7.2.1.** A **functor** $F:\mathcal C\to\mathcal D$ between categories $\mathcal C$ and $\mathcal D$ is

(i) a map $F:\operatorname{Ob}(\mathcal C)\to\operatorname{Ob}(\mathcal D)$;

<span class="original-page-anchor" id="pdf-page-188" aria-hidden="true"></span>

(ii) for each $X,Y\in\mathcal C$, a map $F=F_{X,Y}:\operatorname{Hom}(X,Y)\to\operatorname{Hom}(F(X),F(Y))$ which preserves compositions and identity morphisms.

Note that functors can be composed in an obvious way. Also, any category has the identity functor.

**Example 7.2.2.** **1.** A (locally small) category $\mathcal C$ with one object $X$ is the same thing as a monoid. A functor between such categories is a homomorphism of monoids.

**2.** Forgetful functors

$$
\mathbf{Groups}\longrightarrow\mathbf{Sets},\qquad
\mathbf{Rings}\longrightarrow\mathbf{AbelianGroups}.
$$

**3.** The opposite category of a given category is the same category with the order of arrows and compositions reversed. Then $V\mapsto V^*$ is a functor $\mathbf{Vect}_k\to\mathbf{Vect}_k^{\mathrm{op}}$.

**4.** The Hom functors: if $\mathcal C$ is a locally small category, then we have the functor $\mathcal C\to\mathbf{Sets}$ given by $Y\mapsto\operatorname{Hom}(X,Y)$ and $\mathcal C^{\mathrm{op}}\to\mathbf{Sets}$ given by $Y\mapsto\operatorname{Hom}(Y,X)$.

**5.** The assignment $X\mapsto\operatorname{Fun}(X,\mathbb Z)$ is a functor $\mathbf{Sets}\to\mathbf{Rings}^{\mathrm{op}}$.

**6.** Let $Q$ be a quiver. Consider the category $\mathcal C(Q)$ whose objects are the vertices and morphisms are oriented paths between them. Then functors from $\mathcal C(Q)$ to $\mathbf{Vect}_k$ are representations of $Q$ over $k$.

**7.** Let $K\subset G$ be groups. Then we have the induction functor $\operatorname{Ind}_K^G:\operatorname{Rep}(K)\to\operatorname{Rep}(G)$ and the restriction functor $\operatorname{Res}_K^G:\operatorname{Rep}(G)\to\operatorname{Rep}(K)$.

**8.** We have an obvious notion of the Cartesian product of categories (obtained by taking the Cartesian products of the classes of objects and morphisms of the factors). The functors of direct sum and tensor product are then functors $\mathbf{Vect}_k\times\mathbf{Vect}_k\to\mathbf{Vect}_k$. Also the operations $V\mapsto V^{\otimes n}$, $V\mapsto S^nV$, $V\mapsto\bigwedge^nV$ are functors on $\mathbf{Vect}_k$. More generally, if $\pi$ is a representation of $S_n$, we have functors $V\mapsto\operatorname{Hom}_{S_n}(\pi,V^{\otimes n})$. Such functors are called the **Schur functors**. Thus, the irreducible Schur functors are labeled by Young diagrams.

**9.** The reflection functors $F_i^\pm:\operatorname{Rep}(Q)\to\operatorname{Rep}(\overline Q_i)$ are functors between representation categories of quivers.

<span class="original-page-anchor" id="pdf-page-189" aria-hidden="true"></span>

## 7.3. Morphisms of functors

One of the important features of functors between categories which distinguishes them from usual maps or functions is that the functors between two given categories themselves form a category; i.e., one can define a nontrivial notion of a morphism between two functors.

**Definition 7.3.1.** Let $\mathcal C,\mathcal D$ be categories and let $F,G:\mathcal C\to\mathcal D$ be functors between them. A **morphism** $a:F\to G$ (also called a **natural transformation** or a **functorial morphism**) is a collection of morphisms $a_X:F(X)\to G(X)$ labeled by the objects $X$ of $\mathcal C$, which is functorial in $X$; i.e., for any morphism $f:X\to Y$ (for $X,Y\in\mathcal C$) one has $a_Y\circ F(f)=G(f)\circ a_X$.

A morphism $a:F\to G$ is an **isomorphism** if there is another morphism $a^{-1}:G\to F$ such that $a\circ a^{-1}$ and $a^{-1}\circ a$ are the identities. The set of morphisms from $F$ to $G$ is denoted by $\operatorname{Hom}(F,G)$.

**Example 7.3.2.** 1. Let $\mathbf{FVect}_k$ be the category of finite dimensional vector spaces over $k$. Then the functors $\operatorname{id}$ and ${}^{**}$ on this category are isomorphic. The isomorphism is defined by the standard maps $a_V:V\to V^{**}$ given by $a_V(u)(f)=f(u)$, $u\in V$, $f\in V^*$. But these two functors are not isomorphic on the category of all vector spaces $\mathbf{Vect}_k$, since for an infinite dimensional vector space $V$, $V$ is not isomorphic to $V^{**}$.

2. Let $\mathbf{FVect}'_k$ be the category of finite dimensional $k$-vector spaces, where the morphisms are the isomorphisms. We have a functor $F$ from this category to itself sending any space $V$ to $V^*$ and any morphism $a$ to $(a^*)^{-1}$. This functor satisfies the property that $V$ is isomorphic to $F(V)$ for any $V$, but it is not isomorphic to the identity functor. This is because the isomorphism $V\mapsto F(V)=V^*$ cannot be chosen to be compatible with the action of $GL(V)$, as $V$ is not isomorphic to $V^*$ as a representation of $GL(V)$.

3. Let $A$ be an algebra over a field $k$, and let $F:A\text{-}\mathbf{mod}\to\mathbf{Vect}_k$ be the forgetful functor. Then as follows from Problem 2.3.17, $\operatorname{End}F=\operatorname{Hom}(F,F)=A$.

4. The set of endomorphisms of the identity functor on the category $A\text{-}\mathbf{mod}$ is the center of $A$ (check it!).

<span class="original-page-anchor" id="pdf-page-190" aria-hidden="true"></span>

## 7.4. Equivalence of categories

When two algebraic or geometric objects are isomorphic, it is usually not a good idea to say that they are equal (i.e., literally the same). The reason is that such objects are usually equal in many different ways, i.e., there are many ways to pick an isomorphism, but by saying that the objects are equal, we are misleading the reader or listener into thinking that we are providing a certain choice of the identification, which we actually do not do. A vivid example of this is a finite dimensional vector space $V$ and its dual space $V^*$.

For this reason, in category theory, most of the time one tries to avoid saying that two objects or two functors are equal. In particular, this applies to the definition of isomorphism of categories.

Namely, the naive notion of isomorphism of categories is defined in the obvious way: a functor $F:\mathcal C\to\mathcal D$ is an isomorphism if there exists $F^{-1}:\mathcal D\to\mathcal C$ such that $F\circ F^{-1}$ and $F^{-1}\circ F$ are equal to the identity functors. But this definition is not very useful. We might suspect so since we have used the word “equal” for objects of a category (namely, functors) which we are not supposed to do. In fact, here is an example of two categories which are “the same for all practical purposes” but are not isomorphic; it demonstrates the deficiency of our definition.

Namely, let $\mathcal C_1$ be the simplest possible category: $\operatorname{Ob}(\mathcal C_1)$ consists of one object $X$, with $\operatorname{Hom}(X,X)=\{1_X\}$. Also, let $\mathcal C_2$ have two objects $X,Y$ and four morphisms: $1_X$, $1_Y$, $a:X\to Y$, and $b:Y\to X$. So we must have $a\circ b=1_Y$, $b\circ a=1_X$.

It is easy to check that for any category $\mathcal D$, there is a natural bijection between the collections of isomorphism classes of functors $\mathcal C_1\to\mathcal D$ and $\mathcal C_2\to\mathcal D$ (both are identified with the collection of isomorphism classes of objects of $\mathcal D$). This is what we mean by saying that $\mathcal C_1$ and $\mathcal C_2$ are “the same for all practical purposes”. Nevertheless they are not isomorphic, since $\mathcal C_1$ has one object and $\mathcal C_2$ has two objects (even though these two objects are isomorphic to each other).

This shows that we should adopt a more flexible and less restrictive notion of isomorphism of categories. This is accomplished by the definition of an equivalence of categories.

<span class="original-page-anchor" id="pdf-page-191" aria-hidden="true"></span>

**Definition 7.4.1.** A functor $F:\mathcal C\to\mathcal D$ is an **equivalence of categories** if there exists $F':\mathcal D\to\mathcal C$ such that $F\circ F'$ and $F'\circ F$ are isomorphic to the identity functors.

In this situation, $F'$ is said to be a **quasi-inverse** to $F$.

In particular, the above categories $\mathcal C_1$ and $\mathcal C_2$ are equivalent (check it!).

Also, the category $\mathbf{FSet}$ of finite sets is equivalent to the category whose objects are nonnegative integers, and morphisms are given by

$$
\operatorname{Hom}(m,n)=\operatorname{Maps}(\{1,\ldots,m\},\{1,\ldots,n\}).
$$

Are these categories isomorphic? The answer to this question depends on whether you believe that there is only one finite set with a given number of elements, or that there are many of those. It seems better to think that there are many (without asking “how many”), so that isomorphic sets need not be literally equal, but this is really a matter of choice. In any case, this is not really a reasonable question; the answer to this question is irrelevant for any practical purpose, and thinking about it will give you nothing but a headache.

## 7.5. Representable functors

A fundamental notion in category theory is that of a **representable functor**. Namely, let $\mathcal C$ be a (locally small) category, and let $F:\mathcal C\to\mathbf{Sets}$ be a functor. We say that $F$ is **representable** if there exists an object $X\in\mathcal C$ such that $F$ is isomorphic to the functor $\operatorname{Hom}(X,?)$. More precisely, if we are given such an object $X$, together with an isomorphism $\xi:F\cong\operatorname{Hom}(X,?)$, we say that the functor $F$ **is represented by** $X$ (using $\xi$).

In a similar way, one can talk about representable functors from $\mathcal C^{\mathrm{op}}$ to $\mathbf{Sets}$. Namely, one calls such a functor representable if it is of the form $\operatorname{Hom}(?,X)$ for some object $X\in\mathcal C$, up to an isomorphism.

Not every functor is representable, but if a representing object $X$ exists, then it is unique. Namely, we have the following lemma.

**Lemma 7.5.1 (The Yoneda Lemma).** *If a functor $F$ is represented by an object $X$, then $X$ is unique up to a unique isomorphism. I.e., if $X,Y$ are two objects in $\mathcal C$, then for any isomorphism of functors* <span class="original-page-anchor" id="pdf-page-192" aria-hidden="true"></span>$\phi:\operatorname{Hom}(X,?)\to\operatorname{Hom}(Y,?)$ *there is a unique isomorphism $a_\phi:X\to Y$ inducing $\phi$.*

**Proof (Sketch).** One sets $a_\phi=\phi_Y^{-1}(1_Y)$ and shows that it is invertible by constructing the inverse, which is $a_\phi^{-1}=\phi_X(1_X)$. It remains to show that the composition both ways is the identity, which we will omit here. This establishes the existence of $a_\phi$. Its uniqueness is verified in a straightforward manner. $\square$

**Remark 7.5.2.** In a similar way, if a category $\mathcal C$ is enriched over another category $\mathcal D$ (say, the category of abelian groups or vector spaces), one can define the notion of a representable functor from $\mathcal C$ to $\mathcal D$.

**Example 7.5.3.** Let $A$ be an algebra. Then the forgetful functor from the category of left $A$-modules to the category of vector spaces is representable, and the representing object is the free rank $1$ module (= the regular representation) $M=A$. But if $A$ is infinite dimensional and we restrict attention to the category of finite dimensional modules, then the forgetful functor, in general, is not representable (this is so, for example, if $A$ is the algebra of complex functions on $\mathbb Z$ which are zero at all but finitely many points).

## 7.6. Adjoint functors

Another fundamental notion in category theory is the notion of adjoint functors.

**Definition 7.6.1.** Functors $F:\mathcal C\to\mathcal D$ and $G:\mathcal D\to\mathcal C$ are said to be a pair of **adjoint functors** if for any $X\in\mathcal C$, $Y\in\mathcal D$ we are given an isomorphism $\xi_{XY}:\operatorname{Hom}_{\mathcal C}(F(X),Y)\to\operatorname{Hom}_{\mathcal D}(X,G(Y))$ which is functorial in $X$ and $Y$, i.e., if we are given an isomorphism of functors $\operatorname{Hom}(F(?),?)\to\operatorname{Hom}(?,G(?))$ $(\mathcal C\times\mathcal D\to\mathbf{Sets})$. In this situation, we say that $F$ is **left adjoint** to $G$ and $G$ is **right adjoint** to $F$.

Not every functor has a left or right adjoint, but if it does, it is unique and can be constructed canonically (i.e., if we somehow found two such functors, then there is a canonical isomorphism between them). This follows easily from the Yoneda lemma, since if <span class="original-page-anchor" id="pdf-page-193" aria-hidden="true"></span>$F,G$ are a pair of adjoint functors, then $F(X)$ represents the functor $Y\mapsto\operatorname{Hom}(X,G(Y))$ and $G(Y)$ represents the functor $X\mapsto\operatorname{Hom}(F(X),Y)$.

**Remark 7.6.2.** The terminology “left and right adjoint functors” is motivated by the analogy between categories and inner product spaces. More specifically, in Table 1 we have a useful dictionary between category theory and linear algebra, which helps to better understand many notions of category theory.

**Table 1. Dictionary between category theory and linear algebra.**

| Category theory | Linear algebra |
| --- | --- |
| Category $\mathcal C$ | Vector space $V$ with a nondegenerate inner product |
| The set of morphisms $\operatorname{Hom}(X,Y)$ | Inner product $(x,y)$ on $V$ (maybe nonsymmetric) |
| Opposite category $\mathcal C^{\mathrm{op}}$ | Same space $V$ with reversed inner product |
| The category $\mathbf{Sets}$ | The ground field $k$ |
| Full subcategory in $\mathcal C$ | Nondegenerate subspace in $V$ |
| Functor $F:\mathcal C\to\mathcal D$ | Linear operator $f:V\to W$ |
| Functor $F:\mathcal C\to\mathbf{Sets}$ | Linear functional $f\in V^*=\operatorname{Hom}(V,k)$ |
| Representable functor | Linear functional $f\in V^*$ given by $f(v)=(u,v)$, $u\in V$ |
| Yoneda lemma | Nondegeneracy of the inner product (on both sides) |
| Not all functors are representable | If $\dim V=\infty$, not $\forall f\in V^*$, $f(v)=(u,v)$ |
| Left and right adjoint functors | Left and right adjoint operators |
| Adjoint functors don't always exist | Adjoint operators may not exist if $\dim V=\infty$ |
| If they do, they are unique | If they do, they are unique |
| Left and right adjoints may not coincide | The inner product may be nonsymmetric |

<span class="original-page-anchor" id="pdf-page-194" aria-hidden="true"></span>

**Example 7.6.3.** 1. Let $V$ be a finite dimensional representation of a group $G$ or a Lie algebra $\mathfrak g$. Then the left and right adjoint to the functor $V\otimes$ on the category of representations of $G$ is the functor $V^*\otimes$.

2. The functor $\operatorname{Res}_K^G$ is left adjoint to $\operatorname{Ind}_K^G$. This is nothing but the statement of the Frobenius reciprocity.

3. Let $\mathbf{Assoc}_k$ be the category of associative unital algebras, and let $\mathbf{Lie}_k$ be the category of Lie algebras over some field $k$. We have a functor $L:\mathbf{Assoc}_k\to\mathbf{Lie}_k$ which attaches to an associative algebra the same space regarded as a Lie algebra, with bracket $[a,b]=ab-ba$. Then the functor $L$ has a left adjoint, which is the functor $U$ of taking the universal enveloping algebra of a Lie algebra.

4. We have the functor $GL_1:\mathbf{Assoc}_k\to\mathbf{Groups}$, given by $A\mapsto GL_1(A)=A^\times$. This functor has a left adjoint, which is the functor $G\mapsto k[G]$, the group algebra of $G$.

5. The left adjoint to the forgetful functor $\mathbf{Assoc}_k\to\mathbf{Vect}_k$ is the functor of tensor algebra: $V\mapsto TV$. Also, if we denote by $\mathbf{Comm}_k$ the category of commutative algebras, then the left adjoint to the forgetful functor $\mathbf{Comm}_k\to\mathbf{Vect}_k$ is the functor of the symmetric algebra: $V\mapsto SV$.

One can give many more examples, spanning many fields. These examples show that adjoint functors are ubiquitous in mathematics.

## 7.7. Abelian categories

The type of categories that most often appears in representation theory is abelian categories. The standard definition of an abelian category is rather long, so we will not give it here, referring the reader to the textbook [Fr]; rather, we will use as the definition what is really the statement of the Freyd-Mitchell theorem:

**Definition 7.7.1.** An **abelian category** is a category (enriched over the category of abelian groups) which is equivalent to a full subcategory $\mathcal C$ of the category $A\text{-}\mathbf{mod}$ of left modules over a ring $A$, closed under taking finite direct sums, as well as kernels, cokernels, and images of morphisms.

<span class="original-page-anchor" id="pdf-page-195" aria-hidden="true"></span>

**Example 7.7.2.** The category of modules over an algebra $A$ and the category of finite dimensional modules over $A$ are abelian categories.

**Problem 7.7.3.** Let $A$ be a finitely generated commutative ring. Show that the category of finitely generated $A$-modules is an abelian category.

Hint: Use the Hilbert basis theorem.

We see from this definition that in an abelian category, $\operatorname{Hom}(X,Y)$ is an abelian group for each $X,Y$, compositions are group homomorphisms with respect to each argument, there is the zero object, the notions of an injective morphism (monomorphism) and surjective morphism (epimorphism), and every morphism has a kernel, a cokernel, and an image.

**Remark 7.7.4.** The good thing about Definition 7.7.1 is that it allows us to visualize objects, morphisms, kernels, and cokernels in terms of classical algebra. But the definition also has a big drawback, which is that even if $\mathcal C$ is the whole category $A\text{-}\mathbf{mod}$, the ring $A$ is not determined by $\mathcal C$. In particular, two different rings can have equivalent categories of modules (such rings are called **Morita equivalent**). Actually, it is worse than that: for many important abelian categories there is no natural (or even manageable) ring $A$ at all. This is why people prefer to use the standard definition, which is free from this drawback, even though it is more abstract.

Let $k$ be a field. We say that an abelian category $\mathcal C$ is **$k$-linear** if the groups $\operatorname{Hom}_{\mathcal C}(X,Y)$ are equipped with a structure of a vector space over $k$ and composition maps are $k$-linear in each argument. In particular, the categories in Example 7.7.2 are $k$-linear.

## 7.8. Complexes and cohomology

**Definition 7.8.1.** A sequence of objects $C_i$, $i\in\mathbb Z$, of an abelian category $\mathcal C$ and morphisms $d_i:C_i\to C_{i+1}$ is said to be a **complex** if the composition of any two consecutive arrows is zero. The morphisms $d_i$ are called the **differentials**.[^rt-195-1] The **cohomology** of this complex is <span class="original-page-anchor" id="pdf-page-196" aria-hidden="true"></span>$H^i=\operatorname{Ker}(d_i)/\operatorname{Im}(d_{i-1})$. The complex is said to be **exact** in the $i$th term if $H^i=0$ and is said to be an **exact sequence** if it is exact in all terms.

There is an obvious notion of a **morphism of complexes**. Namely, a morphism $f:C\to D$ is a collection of morphisms $f_i:C_i\to D_i$ such that $d_i\circ f_i=f_{i+1}\circ d_i$. Clearly, such morphisms can be composed, which makes the class of all complexes over $\mathcal C$ into a category, denoted $\operatorname{Compl}(\mathcal C)$.

In particular, one can consider complexes of abelian groups, vector spaces, modules over a ring, etc. In this case, elements of $\operatorname{Ker}(d_i)$ are called **$i$-cocycles**, the elements of $\operatorname{Im}(d_{i-1})$ are called **$i$-coboundaries**, and the elements of $H^i(C)$ are called **$i$th cohomology classes**. This terminology is adopted from topology. For this reason, exact sequences are also called **acyclic complexes** (as they are complexes which have no nontrivial cocycles, i.e., cocycles that are not coboundaries).

Often one considers complexes that are bounded in one or both directions; i.e., the objects $C_i$ are zero for $i\gg0$, $i\ll0$, or both. In this case one writes one zero on each side where the complex is bounded. For example, a complex bounded on both sides with $n+1$ terms will look like

$$
0\to C_0\to C_1\to\cdots\to C_n\to0.
$$

**Definition 7.8.2.** A **short exact sequence** is an exact sequence of the form

$$
0\to X\to Y\to Z\to0.
$$

Clearly, $0\to X\to Y\to Z\to0$ is a short exact sequence if and only if $X\to Y$ is injective, $Y\to Z$ is surjective, and the induced map $Y/X\to Z$ is an isomorphism. In other words, short exact sequences correspond to extensions of $Z$ by $X$.

**Example 7.8.3.** The sequence $0\to X\to X\oplus Z\to Z\to0$ with the obvious morphisms is a short exact sequence. Such a sequence is called **split**. It corresponds to the trivial extension of $Z$ by $X$.

<span class="original-page-anchor" id="pdf-page-197" aria-hidden="true"></span>

**Exercise 7.8.4.** Show that any exact sequence of vector spaces is isomorphic to a direct sum of complexes of the form

$$
0\to V\to V\to0,
$$

where $V$ stands at the places $i$ and $i+1$ and the map $V\to V$ is the identity (in particular, any short exact sequence of vector spaces is split). Is this true in the category of abelian groups?

**Problem 7.8.5.** Let $D_\bullet$ be a complex of abelian groups with differentials $d_i$, $i\in\mathbb Z$, let $C_\bullet$ be a subcomplex of $D_\bullet$ (i.e., a collection of subgroups $C_i\subset D_i$ such that $d_i(C_i)\subset C_{i+1}$), and let $E_\bullet=D_\bullet/C_\bullet$ be the quotient complex (i.e., $E_i=D_i/C_i$ with differentials induced by $d_i$).

Define a homomorphism $c_i:H^i(E)\to H^{i+1}(C)$ as follows. Given $x\in H^i(E)$, pick a representative $x'$ of $x$ in $E_i$. Let $x''$ be a lift of $x'$ to $D_i$. Let $y'=dx''\in D_{i+1}$ (we abbreviate the notation, denoting $d_i$ just by $d$). Since $dx'=0$, $y'=dx''\in C_{i+1}$. Also, $dy'=d^2x''=0$. So $y'$ represents an element $y\in H^{i+1}(C)$. We will set $c_i(x)=y$.

(i) Show that $c_i$ is well defined, i.e., $c_i(x)$ does not depend on the choice of $x'$ and $x''$.

(ii) Show that the sequence

$$
\cdots H^{i-1}(E)\to H^i(C)\to H^i(D)\to H^i(E)\to H^{i+1}(C)\cdots,\tag{7.8.1}
$$

where the first map is $c_{i-1}$, the middle two maps are induced by the maps $C_i\to D_i\to E_i$, and the last map is $c_i$, is exact.

**Definition 7.8.6.** The map $c_i$ is called the **connecting homomorphism**, and the sequence (7.8.1) is called the **long exact sequence of cohomology**.

**Problem 7.8.7.** Let $C_\bullet$ and $D_\bullet$ be complexes of modules over a commutative ring $A$. Define the tensor product complex $(C\otimes D)_\bullet$ by the formula

$$
(C\otimes D)_i=\bigoplus_{j+m=i}C_j\otimes_A D_m,
$$

with differentials

$$
d_i^{C\otimes D}\big|_{C_j\otimes D_m}=d_j^C\otimes1+(-1)^j\cdot1\otimes d_m^D.
$$

<span class="original-page-anchor" id="pdf-page-198" aria-hidden="true"></span>

(i) Show that this is a complex.

Now assume that $A=k$ is a field.

(ii) Show that if $C$ or $D$ is an exact sequence, then so is $C\otimes D$.

Hint: Use the decomposition of Exercise 7.8.4.

(iii) Show that any complex $C$ can be identified with a direct sum of an exact sequence and the complex consisting of $H^i(C)$ with the zero differentials, in such a way that the induced isomorphism $H^i(C)\to H^i(C)$ is the identity.

(iv) Show that there is a natural isomorphism of vector spaces

$$
H^i(C\otimes D)\cong\bigoplus_{j+m=i}H^j(C)\otimes H^m(D).
$$

This is the **Künneth formula**.

## 7.9. Exact functors

**Definition 7.9.1.** A functor $F$ between two abelian categories is **additive** if it induces homomorphisms on Hom groups. Also, for $k$-linear categories one says that $F$ is **$k$-linear** if it induces $k$-linear maps between Hom spaces.

It is easy to show that if $F$ is an additive functor, then $F(X\oplus Y)$ is canonically isomorphic to $F(X)\oplus F(Y)$.

**Example 7.9.2.** The functors $\operatorname{Ind}_K^G$, $\operatorname{Res}_K^G$, $\operatorname{Hom}_G(V,?)$ in the theory of group representations over a field $k$ are additive and $k$-linear.

**Definition 7.9.3.** An additive functor $F:\mathcal C\to\mathcal D$ between abelian categories is **left exact** if for any exact sequence

$$
0\to X\to Y\to Z,
$$

the sequence

$$
0\to F(X)\to F(Y)\to F(Z)
$$

is exact. $F$ is **right exact** if for any exact sequence

$$
X\to Y\to Z\to0,
$$

the sequence

$$
F(X)\to F(Y)\to F(Z)\to0
$$

is exact. $F$ is **exact** if it is both left and right exact.

<span class="original-page-anchor" id="pdf-page-199" aria-hidden="true"></span>

**Definition 7.9.4.** An abelian category $\mathcal C$ is **semisimple** if any short exact sequence in this category splits, i.e., is isomorphic to a sequence

$$
0\to X\to X\oplus Y\to Y\to0
$$

(where the maps are obvious).

**Example 7.9.5.** The category of representations of a finite group $G$ over a field of characteristic not dividing $|G|$ (or $0$) is semisimple.

Note that in a semisimple category, any additive functor is automatically exact on both sides.

**Example 7.9.6.** (i) The functors $\operatorname{Ind}_K^G$, $\operatorname{Res}_K^G$ are exact.

(ii) The functor $\operatorname{Hom}(X,?)$ is left exact, but not necessarily right exact. To see that it need not be right exact, it suffices to consider the exact sequence

$$
0\to\mathbb Z\to\mathbb Z\to\mathbb Z/2\mathbb Z\to0
$$

and to apply the functor $\operatorname{Hom}(\mathbb Z/2\mathbb Z,?)$.

(iii) The functor $X\otimes_A$ for a right $A$-module $X$ (on the category of left $A$-modules) is right exact but not necessarily left exact. To see this, it suffices to tensor multiply the above exact sequence by $\mathbb Z/2\mathbb Z$.

**Exercise 7.9.7.** Show that if $(F,G)$ is a pair of adjoint additive functors between abelian categories, then $F$ is right exact and $G$ is left exact.

**Exercise 7.9.8.** (a) Let $Q$ be a quiver and let $i\in Q$ be a source. Let $V$ be a representation of $Q$ and let $W$ be a representation of $\overline Q_i$ (the quiver obtained from $Q$ by reversing arrows at the vertex $i$). Prove that there is a natural isomorphism between $\operatorname{Hom}(F_i^-V,W)$ and $\operatorname{Hom}(V,F_i^+W)$. In other words, the functor $F_i^+$ is right adjoint to $F_i^-$.

(b) Deduce that the functor $F_i^+$ is left exact and $F_i^-$ is right exact.

<span class="original-page-anchor" id="pdf-page-200" aria-hidden="true"></span>

## 7.10. Historical interlude: Eilenberg, Mac Lane, and “general abstract nonsense”

Saunders Mac Lane’s (1909–2005) father and grandfather were both Congregational ministers, so young Saunders seemed destined for an ecclesiastical career. Early on, however, he started having “various theological doubts and questions”. “[A] ministerial career would have required my belief of things of which I was uncertain”, Mac Lane later recalled. “Mathematics, however, provided a different sort of certainty”. One thing he was certain about was that the minister’s income was woefully inadequate to provide for comfortable retirement. As a result, Mac Lane decided to pursue a career that would be “scientific rather than ministerial” [33, pp. 349–350]. He earned his bachelor’s degree at Yale and his master’s at Chicago.

Inspired by the “elegance of German abstract algebra”, in which the notions of rings and fields axiomatized addition and multiplication, Mac Lane devoted his master’s thesis to a similar axiomatization of exponentials, as well as plus and times. At Chicago, Mac Lane was put off by inadequate teaching and by examples of what he saw as a “display of pedantry”, and he concluded that the mathematics department there “had ceased to be really first class” [36, p. 152]. He recalled that he had been taught that a vector was an $n$-tuple, “an idea that I soon had to unlearn” [33, p. 39]. Mac Lane wanted to write a doctoral dissertation on logic but could not find an advisor and decided to leave for Göttingen, the preeminent center of mathematical logic research.

At Göttingen, the home of the famous Hilbert school, Mac Lane learned group representations from Hermann Weyl and linear associative algebras from Emmy Noether. “To live in Göttingen was to be immersed in mathematical culture”, Mac Lane wrote, recalling Göttingen as “an amalgam of research, teaching, and inspiration”. Despite this immersion, Mac Lane could hardly ignore the tense political climate, the vociferous clashes among 27 political parties, and the students dressed in the Nazi brownshirt uniform. Mac Lane did write a thesis on logic but managed to overlook Gödel’s famous incompleteness theorem, which appeared at that time. His thesis elicited <span class="original-page-anchor" id="pdf-page-201" aria-hidden="true"></span>common schemes of proof in Russell and Whitehead’s *Principia Mathematica* with the aim of abbreviating and perhaps mechanizing new proofs. The thesis was “naive in supposing that all mathematics would be *actually* written in Whitehead and Russell style”, Mac Lane admitted. Mac Lane was in Göttingen in 1933, when Hitler came to power, and he witnessed the ruthless destruction of the Hilbert school, as many leading Jewish mathematicians, including Courant and Noether, were dismissed from their jobs. The once famous mathematics department became “but a skeleton”. Mac Lane rushed up to finish his thesis. Unimpressive by Göttingen standards, the thesis was accepted with the grade *Genügend*, the lowest grade. Mac Lane became the last American to earn a doctorate in the famous Hilbert school. One more thing Mac Lane managed to do before departure was to get married to Dorothy Jones. Being at Göttingen as he was, Mac Lane went to hear a mathematical lecture right after his wedding ceremony [33, pp. 48, 54, 51–52, 58, 52, 56].

In the 1930s mathematical logic was looked down upon by most mathematicians, who considered it part of philosophy rather than of mathematics proper. When he started teaching as an instructor at Harvard, Mac Lane intended to offer a logic course, but departmental needs forced him to lecture on algebra. Eventually he realized that it was easier to get a job as an algebraist than as a logician. In 1941, Mac Lane and Garrett Birkhoff co-authored *Survey of Modern Algebra*, the first American undergraduate textbook that espoused the abstract approach of Emmy Noether and B. L. van der Waerden. Initially judged as a text that “won’t fly beyond the Hudson”, the book eventually became a standard textbook for undergraduate algebra courses [33, pp. 62, 68, 82].

In the spring of 1941, Mac Lane received a semester leave from Harvard and applied to visit the Institute for Advanced Study at Princeton. His application was turned down, and Mac Lane ended up going to the University of Michigan to give a series of six lectures. One of the Michigan mathematicians in the audience was Samuel (“Sammy”) Eilenberg (1913–1988). He sat through the first five lectures but had to miss the last one, and he asked Mac Lane to give him the gist of it privately. Mac Lane did, and Eilenberg noticed a <span class="original-page-anchor" id="pdf-page-202" aria-hidden="true"></span>similarity between Mac Lane’s results on group extensions and his colleague Norman Steenrod’s homology theory of solenoid-type spaces. “It was startling” to find that connection, Mac Lane later recalled. They stayed up all night and by morning they found not only “a new intrusion of algebra into topology” but also formed a lifelong collaborative duet, which eventually churned out 15 joint papers. Mac Lane later remarked that the rejection of his application to Princeton was fortuitous, for “had it been accepted, I might have missed working with Sammy” [33, pp. 101–104].

A Polish Jew, Eilenberg left Poland shortly before the start of World War II, following the truly wise advice of his father, once the best student in his town’s yeshiva. Among other European refugee mathematicians, Eilenberg was welcomed by Oswald Veblen and Solomon Lefschetz of Princeton University, who helped him find a position at Michigan. For Eilenberg, mathematics was a social activity. “Though his mathematical ideas may seem to have a kind of crystalline austerity, Sammy was a warm, robust, and very animated human being”, whose charm and humor were “hard to resist”, recalled his former colleague [6, pp. 1351–1352]. Described as “energetic …, expressive, charismatic, quick witted, often confrontational, and a brilliant thinker and good-humored conversationalist”, Eilenberg easily established contacts [7, p. 360]. His entire career was punctuated by various productive collaborations. Together with Steenrod, he “drained the Pontine Marshes of homology theory, turning an ugly morass of variously motivated constructions into a simple and elegant system of axioms applied, for the first time, to functors”. In collaboration with Henri Cartan, Eilenberg systematized homology theories in their *Homological Algebra* (1956). This field developed so rapidly that within a few years Alexander Grothendieck reportedly branded this foundational text “le diplodocus”, relegating it to the subject of paleontology [6, p. 1348].

Eilenberg believed that “the highest value in mathematics was to be found, not in specious depth nor in the overcoming of overwhelming difficulty, but rather in providing the definitive clarity that would illuminate its underlying order”. He insisted on “lucidity, order, and understanding as opposed to trophy hunting”. Eilenberg was called <span class="original-page-anchor" id="pdf-page-203" aria-hidden="true"></span>the “greatest mathematical stylist”, perhaps to the point of championing a “triumph of style over substance” [6, pp. 1349, 1348, 1344, 1350].

Eilenberg’s style called for a minimalist approach, which his colleague described as “always to find the absolutely essential ingredients in any problem and work only with those ingredients and nothing else — in other words, get rid of all the superfluous information”. Once asked if he could eat Chinese food with three chopsticks, he immediately answered in the affirmative and explained, “I’ll take the three chopsticks, I’ll put one of them aside on the table, and I’ll use the other two” [7, p. 361].

Eilenberg and Mac Lane pushed the homological envelope into more complicated spaces in their joint 1942 paper “Natural Isomorphisms in Group Theory”, which introduced the notion of a functor. André Weil, who reviewed their article in *Mathematical Reviews*, did not merely summarize it but added a remarkable note of praise. He wrote that the authors succeeded in finding “a precise definition” for the “vague idea of covariance and contravariance”, “which is likely to be helpful in classifying and systematizing known results and also in looking for new relations between groups” (Weil in [4, p. 743]).

In the war years both Mac Lane and Eilenberg came to New York to work for the Applied Mathematics Group at Columbia University under the National Defense Research Council. They toiled on problems of airborne fire control during the day and on pure mathematics at night. While dealing with the concrete problem of computing the cohomology of the solenoid, they arrived at their universal coefficient theorem and the very general and abstract notions of category and functor. “These notions were so general”, Mac Lane recalled, “that they hardly seemed to be real mathematics — would our mathematical colleagues accept them?” Mac Lane and Eilenberg hid their anxiety behind the jocular label “general abstract nonsense”, by which they occasionally referred to their subject. “We didn’t really mean the nonsense part, and we were proud of its generality”, admitted Mac Lane [33, pp. 125–126].

In 1945 Eilenberg and Mac Lane summed up their findings in the article “General Theory of Natural Equivalences”, which for the <span class="original-page-anchor" id="pdf-page-204" aria-hidden="true"></span>first time defined categories. The article was reportedly “rejected by the editor of an inauspicious journal as ‘more devoid of content than any I have read,’ to which Mac Lane is said to have replied, ‘That’s the point’” [7, p. 362]. Eventually they managed to publish it in the *Transactions of the American Mathematical Society*. This involved a fair amount of wheeling and dealing. “Eilenberg, who knew the editor well, persuaded him to choose as referee a young mathematician”, Mac Lane recalled, “one whom we could influence because he was then a junior member of the Applied Mathematics Group at Columbia University (war research), where Eilenberg and I were then also members, and I was Director” [37, p. 5983]. The article openly declared Eilenberg and Mac Lane’s ambitious goals. “In a metamathematical sense our theory provides general concepts applicable to all branches of mathematics”, they wrote, “and so contributes to the current trend towards uniform treatment of different mathematical disciplines” [12, p. 236].

The wide recognition of the power of Eilenberg and Mac Lane’s ideas was a bit slow to come. Years passed before the words *category* and *functor* “could be pronounced unapologetically in diverse mathematical company” (Freyd in [6, p. 1351]). Luckily, the Air Force Office of Scientific Research became an important sponsor of research and conferences on category theory — an unexpected benefit of Mac Lane and Eilenberg’s wartime work. Only by the mid-1960s did the Air Force eventually figure out that category theory was too abstract to bring any tangible improvements to air combat and discontinued its support [33, p. 239].

Category theory itself underwent quite a transformation after the initial insight. As Mac Lane recalled, when the 1945 paper came out, Eilenberg declared that “this would be the only paper necessary on the subject. It turned out that he was wrong” [33, p. 209]. Eilenberg and Mac Lane originally thought that the very concept of a category was “essentially an auxiliary one; our basic concepts are essentially those of a functor and of a natural transformation”. They even suggested dropping the category concept altogether and adopting “an even more intuitive standpoint”, according to which a functor “is not defined over the category of ‘all’ groups, but for each particular pair <span class="original-page-anchor" id="pdf-page-205" aria-hidden="true"></span>of groups which may be given” [12, p. 247]. Moreover, although Mac Lane and Eilenberg believed that category theory “offered a conceptual view of parts of mathematics”, they regarded it merely as “a handy language”, “a language of orientation”, not as a “field for further research effort” [35, pp. 334–335].

Although Eilenberg and Mac Lane invented category theory, for them “it was always an applied subject, not an end in itself. Categories were defined in order to define functors, which in turn were defined in order to define natural transformations, which were defined finally in order to prove theorems that could not be proved before”. They viewed categories as instruments of mainstream mathematics. The idea that categories could be used “to state theorems that could not be stated before, that they were not tools but objects of nature worthy of study in their own right”, sounded alien to them, for it seemed to place category theory on the fringe, outside the mainstream (Freyd in [6, p. 1351]). In the hands of Alexander Grothendieck, Daniel Kan, and Eilenberg’s students, however, category theory became a dynamic field in its own right, profoundly transformed algebraic geometry, topology, and representation theory, and resonated across a wide range of disciplines, from mathematical logic and theoretical computer science to linguistics and philosophy. In the work of William Lawvere, category theory came to be regarded as a foundation for all of mathematics (Heller in [6, p. 1349]; [7, p. 362]).

Category theory caused a controversy within the group of French mathematicians who worked under the pseudonym Nicolas Bourbaki with the aim of producing a multivolume rigorous treatment of all contemporary mathematics from a unified conceptual point of view. On Weil’s invitation, Eilenberg joined the group in 1950 and remained an active member for 15 years. “He knew admirably how to present his point of view, and he often made us agree to it”, recalled Henri Cartan, another Bourbaki member (Cartan in [6, p. 1345]). Mac Lane was invited to attend a private Bourbaki meeting in 1954, perhaps with the idea that he would persuade the group to adopt the category-theoretical approach. Cartier, Chevalley, Eilenberg, and Grothendieck supported Mac Lane, but André Weil took <span class="original-page-anchor" id="pdf-page-206" aria-hidden="true"></span>a cautious approach, which outweighed them [39, p. 5]. While genuinely interested in incorporating category theory, Bourbaki found it very difficult to abandon its prewar foundational concept of *structure*. Switching to categories would mean revising the whole body of previous work, while combining the two approaches seemed to undermine the Bourbakist ideal of unity of mathematics [5, p. 236]. “My facility in the French language was not sufficient to categorize Bourbaki”, remarked Mac Lane. As a result, important parts of recent mathematical research fell out of Bourbaki’s purview, perhaps contributing to the decline of their overall project. Mac Lane barely hid his disappointment in the outcome, calling the Bourbaki oeuvre a “magnificent multi-volume monster” and Bourbaki’s definition of *structure* “a cumbersome piece of pedantry”, which even Bourbaki never used (quoted in [39, p. 6]).

Ironically, the Bourbakist vision of unified mathematics found a powerful vehicle in category theory. General category-theoretical concepts have enjoyed wide use across many different mathematical fields; in fact, the very rigid division of mathematics into fields has been called into question. “Mathematics as it is today … can no longer be presented by piecemeal courses”, argued Mac Lane in a 1954 talk, “for it is simply no longer true that advanced mathematics can be split neatly into compartments labelled ‘algebra’, ‘analysis’, ‘geometry’, and ‘applied mathematics’”. He championed the “infusion of a geometrical point of view” and reminded his audience that “a vector is geometrical”. “A vector is not an $n$-tuple of numbers until a coordinate system has been chosen. Any teacher and any text book which starts with the idea that vectors are $n$-tuples is committing a crime for which the proper punishment is ridicule” (quoted in [40, p. 245]).

Mac Lane’s favorite pastime was sailing, which he considered “a much more serious sport” than skiing, which he had learned at Göttingen. On some sailing expeditions he spent time with prominent philosophers but showed little interest in their subject. “Thankfully, we paid more attention to sailing than to philosophical doctrine”, he recalled. He found that most studies in philosophy of mathematics “paid little attention to the actual substance of mathematics beyond <span class="original-page-anchor" id="pdf-page-207" aria-hidden="true"></span>the most elementary concerns” and set out to repair the situation. In his 1986 book *Mathematics, Form and Function*, Mac Lane quickly dispatched with an array of mathematical philosophies, from set theory (“often artificial”) to formalism (“can’t explain *which* of many formulas matter”) to intuitionism (“can be dogmatic”) to empiricism (“mathematics originates not just in facts”) to Platonism (“a useful mythology and a speculative ontology”). He even dismissed the Romantic ideal of mathematics as “a search for austere forms of beauty” and offered instead “formal functionalism” — his vision of mathematics as “an extensive network of formal rules, definitions and systems, tightly tied here and there to activities and to science”. Since mathematical entities do not necessarily correspond to any physical objects, Mac Lane argued, it would be meaningless to ask if mathematics is true. The “appropriate” questions about a particular piece of mathematics are different: is it correct (i.e., proved), responsive to some problem, illuminating, promising, relevant? According to Mac Lane, mathematics is correct but not *true* [33, pp. 143, 145, 455–456, 440, 441, 443].

Like Mac Lane, Eilenberg “had no patience for metaphysical argument” (Heller in [6, p. 1349]). He had his own passion outside mathematics, however. “A sophisticated and wise man who took a refined pleasure in life” (Bass in [6, p. 1352]), Eilenberg, in fact, had a parallel life. Known as “Sammy” to mathematicians, Eilenberg was equally famous as an art dealer and collector under the nickname “Professor” in the art world. Over the years, he amassed one of the most significant collections of Southeast Asian sculpture in the world and became a leading expert in the field. His biographer surmised that Eilenberg “found in ancient Hindu sculpture a formal elegance and imagination that resonated well with the same aesthetic sensibility — ‘classical rather than romantic,’ in the words of Alex Heller — that animated his mathematical work” [7, p. 362]. Eilenberg’s two lives rarely intersected. His colleagues recalled only one occasion on which he “moved from a conversation about sculpture to one about mathematics. Sculptors, he said, learn early to create from the inside out: what finally is to be seen on the surface is the result of a lot of work in conceptualizing the interior. But there are others for whom the interior is the result of a lot of work on getting the surface <span class="original-page-anchor" id="pdf-page-208" aria-hidden="true"></span>right. ‘And,’ Sammy asked, ‘isn’t that the case for my mathematics?’” (Freyd in [6, p. 1350]).

Mac Lane called his collaboration with Eilenberg “one small, but typical, example of East meets West. The great influx of refugee mathematicians from Europe presented a decisive stimulus for American mathematics in the 1940s” [33, p. 347]. The Eilenberg–Mac Lane collaboration not only brought together algebra and topology; it epitomized the cross-fertilization of different mathematical schools and the breaking down of internal disciplinary barriers within mathematics in the second half of the twentieth century.

[^rt-195-1]: A famous example of a complex is the **de Rham complex**, in which $C_m$ is the space of differential $m$-forms on a Euclidean space or, more generally, a manifold, and $d_m$ is the exterior differential of differential forms. This explains the term “differential”.
