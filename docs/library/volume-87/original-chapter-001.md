---
title: "Categories, functors and natural transformations"
description: "Tom Leinster《Basic Category Theory》English。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"Introduction","link":"/library/volume-87/original-introduction"}
next: {"text":"Adjoints","link":"/library/volume-87/original-chapter-002"}
---

# Categories, functors and natural transformations

<span class="original-page-anchor" id="pdf-page-18" aria-hidden="true"></span>

A category is a system of related objects. The objects do not live in isolation: there is some notion of map between objects, binding them together.

Typical examples of what ‘object’ might mean are ‘group’ and ‘topological space’, and typical examples of what ‘map’ might mean are ‘homomorphism’ and ‘continuous map’, respectively. We will see many examples, and we will also learn that some categories have a very different flavour from the two just mentioned. In fact, the ‘maps’ of category theory need not be anything like maps in the sense that you are most likely to be familiar with.

Categories are *themselves* mathematical objects, and with that in mind, it is unsurprising that there is a good notion of ‘map between categories’. Such maps are called functors. More surprising, perhaps, is the existence of a third level: we can talk about maps between *functors*, which are called natural transformations. These, then, are maps between maps between categories.

In fact, it was the desire to formalize the notion of natural transformation that led to the birth of category theory. By the early 1940s, researchers in algebraic topology had started to use the phrase ‘natural transformation’, but only in an informal way. Two mathematicians, Samuel Eilenberg and Saunders Mac Lane, saw that a precise definition was needed. But before they could define natural transformation, they had to define functor; and before they could define functor, they had to define category. And so the subject was born.

Nowadays, the uses of category theory have spread far beyond algebraic topology. Its tentacles extend into most parts of pure mathematics. They also reach some parts of applied mathematics; perhaps most notably, category theory has become a standard tool in certain parts of computer science. Applied mathematics is more than just applied differential equations!

<span class="original-page-anchor" id="pdf-page-19" aria-hidden="true"></span>

## 1.1 Categories

**Definition 1.1.1** A **category** $\mathscr{A}$ consists of:

- a collection $\operatorname{ob}(\mathscr{A})$ of **objects**;
- for each $A,B\in\operatorname{ob}(\mathscr{A})$, a collection $\mathscr{A}(A,B)$ of **maps** or **arrows** or **morphisms** from $A$ to $B$;
- for each $A,B,C\in\operatorname{ob}(\mathscr{A})$, a function

$$
\begin{array}{ccc}
\mathscr{A}(B,C)\times\mathscr{A}(A,B)&\to&\mathscr{A}(A,C)\\
(g,f)&\mapsto&g\circ f,
\end{array}
$$

called **composition**;

- for each $A\in\operatorname{ob}(\mathscr{A})$, an element $1_A$ of $\mathscr{A}(A,A)$, called the **identity** on $A$,

satisfying the following axioms:

- **associativity**: for each $f\in\mathscr{A}(A,B)$, $g\in\mathscr{A}(B,C)$ and $h\in\mathscr{A}(C,D)$, we have $(h\circ g)\circ f=h\circ(g\circ f)$;
- **identity laws**: for each $f\in\mathscr{A}(A,B)$, we have $f\circ1_A=f=1_B\circ f$.

**Remarks 1.1.2** (a) We often write:

$$
\begin{array}{rcl}
A\in\mathscr{A}&\text{to mean}&A\in\operatorname{ob}(\mathscr{A});\\
f\colon A\to B\text{ or }A\xrightarrow{f}B&\text{to mean}&f\in\mathscr{A}(A,B);\\
gf&\text{to mean}&g\circ f.
\end{array}
$$

People also write $\mathscr{A}(A,B)$ as $\operatorname{Hom}_{\mathscr{A}}(A,B)$ or $\operatorname{Hom}(A,B)$. The notation ‘$\operatorname{Hom}$’ stands for homomorphism, from one of the earliest examples of a category.

(b) The definition of category is set up so that in general, from each string

$$
A_0\xrightarrow{f_1}A_1\xrightarrow{f_2}\ \cdots\ \xrightarrow{f_n}A_n
$$

of maps in $\mathscr{A}$, it is possible to construct exactly one map

$$
A_0\to A_n
$$

(namely, $f_n f_{n-1}\cdots f_1$). If we are given extra information then we may be able to construct other maps $A_0\to A_n$; for instance, if we happen to know that $A_{n-1}=A_n$, then $f_{n-1}f_{n-2}\cdots f_1$ is another such map. But we are speaking here of the *general* situation, in the absence of extra information.

For example, a string like this with $n=4$ gives rise to maps

![Two composites from A₀ to A₄](/library/volume-87/diagrams/pdf-0019-associativity.png)

<span class="original-page-anchor" id="pdf-page-20" aria-hidden="true"></span>

but the axioms imply that they are equal. It is safe to omit the brackets and write both as $f_4 f_3 f_2 f_1$.

Here it is intended that $n\geq0$. In the case $n=0$, the statement is that for each object $A_0$ of a category, it is possible to construct exactly one map $A_0\to A_0$ (namely, the identity $1_{A_0}$). An identity map can be thought of as a zero-fold composite, in much the same way that the number $1$ can be thought of as the product of zero numbers.

(c) We often speak of **commutative diagrams**. For instance, given objects and maps

![A commutative diagram](/library/volume-87/diagrams/pdf-0020-commutative.png)

in a category, we say that the diagram **commutes** if $gf=jih$. Generally, a diagram is said to commute if whenever there are two paths from an object $X$ to an object $Y$, the map from $X$ to $Y$ obtained by composing along one path is equal to the map obtained by composing along the other.

(d) The slightly vague word ‘collection’ means *roughly* the same as ‘set’, although if you know about such things, it is better to interpret it as meaning ‘class’. We come back to this in Chapter 3.

(e) If $f\in\mathscr{A}(A,B)$, we call $A$ the **domain** and $B$ the **codomain** of $f$. Every map in every category has a definite domain and a definite codomain. (If you believe it makes sense to form the intersection of an arbitrary pair of abstract sets, you should add to the definition of category the condition that $\mathscr{A}(A,B)\cap\mathscr{A}(A',B')=\emptyset$ unless $A=A'$ and $B=B'$.)

**Examples 1.1.3 (Categories of mathematical structures)** (a) There is a category $\mathbf{Set}$ described as follows. Its objects are sets. Given sets $A$ and $B$, a map from $A$ to $B$ in the category $\mathbf{Set}$ is exactly what is ordinarily called a map (or mapping, or function) from $A$ to $B$. Composition in the category is ordinary composition of functions, and the identity maps are again what you would expect.

In situations such as this, we often do not bother to specify the composition and identities. We write ‘the category of sets and functions’, leaving the reader to guess the rest. In fact, we usually go further and call it just ‘the category of sets’.

(b) There is a category $\mathbf{Grp}$ of groups, whose objects are groups and whose maps are group homomorphisms.

(c) Similarly, there is a category $\mathbf{Ring}$ of rings and ring homomorphisms.

<span class="original-page-anchor" id="pdf-page-21" aria-hidden="true"></span>

(d) For each field $k$, there is a category $\mathbf{Vect}_k$ of vector spaces over $k$ and linear maps between them.

(e) There is a category $\mathbf{Top}$ of topological spaces and continuous maps.

This chapter is mostly about the interaction *between* categories, rather than what goes on *inside* them. We will, however, need the following definition.

**Definition 1.1.4** A map $f\colon A\to B$ in a category $\mathscr{A}$ is an **isomorphism** if there exists a map $g\colon B\to A$ in $\mathscr{A}$ such that $gf=1_A$ and $fg=1_B$.

In the situation of Definition 1.1.4, we call $g$ the **inverse** of $f$ and write $g=f^{-1}$. (The word ‘the’ is justified by Exercise 1.1.13.) If there exists an isomorphism from $A$ to $B$, we say that $A$ and $B$ are **isomorphic** and write $A\cong B$.

**Example 1.1.5** The isomorphisms in $\mathbf{Set}$ are exactly the bijections. This statement is not quite a logical triviality. It amounts to the assertion that a function has a two-sided inverse if and only if it is injective and surjective.

**Example 1.1.6** The isomorphisms in $\mathbf{Grp}$ are exactly the isomorphisms of groups. Again, this is not quite trivial, at least if you were taught that the definition of group isomorphism is ‘bijective homomorphism’. In order to show that this is equivalent to being an isomorphism in $\mathbf{Grp}$, you have to prove that the inverse of a bijective homomorphism is also a homomorphism.

Similarly, the isomorphisms in $\mathbf{Ring}$ are exactly the isomorphisms of rings.

**Example 1.1.7** The isomorphisms in $\mathbf{Top}$ are exactly the homeomorphisms. Note that, in contrast to the situation in $\mathbf{Grp}$ and $\mathbf{Ring}$, a bijective map in $\mathbf{Top}$ is not necessarily an isomorphism. A classic example is the map

$$
\begin{array}{ccc}
[0,1)&\to&\{z\in\mathbb{C}\mid |z|=1\}\\
t&\mapsto&e^{2\pi i t},
\end{array}
$$

which is a continuous bijection but not a homeomorphism.

The examples of categories mentioned so far are important, but could give a false impression. In each of them, the objects of the category are sets with structure (such as a group structure, a topology, or, in the case of $\mathbf{Set}$, no structure at all). The maps are the functions preserving the structure, in the appropriate sense. And in each of them, there is a clear sense of what the elements of a given object are.

However, not all categories are like this. In general, the objects of a category are not ‘sets equipped with extra stuff’. Thus, in a general category, it does not make sense to talk about the ‘elements’ of an object. (At least, it does not make <span class="original-page-anchor" id="pdf-page-22" aria-hidden="true"></span>sense in an immediately obvious way; we return to this in Definition 4.1.25.) Similarly, in a general category, the maps need not be mappings or functions in the usual sense. So:

*The objects of a category need not be remotely like sets.*

*The maps in a category need not be remotely like functions.*

The next few examples illustrate these points. They also show that, contrary to the impression that might have been given so far, categories need not be enormous. Some categories are small, manageable structures in their own right, as we now see.

**Examples 1.1.8 (Categories as mathematical structures)** (a) A category can be specified by saying directly what its objects, maps, composition and identities are. For example, there is a category $\emptyset$ with no objects or maps at all. There is a category $\mathbf{1}$ with one object and only the identity map. It can be drawn like this:

$$
\bullet
$$

(Since every object is required to have an identity map on it, we usually do not bother to draw the identities.) There is another category that can be drawn as

$$
\bullet\to\bullet\qquad\text{or}\qquad A\xrightarrow{f}B,
$$

with two objects and one non-identity map, from the first object to the second. (Composition is defined in the only possible way.) To reiterate the points made above, it is not obvious what an ‘element’ of $A$ or $B$ would be, or how one could regard $f$ as a ‘function’ of any sort.

It is easy to make up more complicated examples. For instance, here are three more categories:

![Three further categories](/library/volume-87/diagrams/pdf-0022-categories.png)

(b) Some categories contain no maps at all apart from identities (which, as categories, they are obliged to have). These are called **discrete** categories. A discrete category amounts to just a class of objects. More poetically, a category is a collection of objects related to one another to a greater or lesser degree; a discrete category is the extreme case in which each object is totally isolated from its companions.

<span class="original-page-anchor" id="pdf-page-23" aria-hidden="true"></span>

(c) A group is essentially the same thing as a category that has only one object and in which all the maps are isomorphisms.

To understand this, first consider a category $\mathscr{A}$ with just one object. It is not important what letter or symbol we use to denote the object; let us call it $A$. Then $\mathscr{A}$ consists of a set (or class) $\mathscr{A}(A,A)$, an associative composition function

$$
\circ\colon\mathscr{A}(A,A)\times\mathscr{A}(A,A)\to\mathscr{A}(A,A),
$$

and a two-sided unit $1_A\in\mathscr{A}(A,A)$. This would make $\mathscr{A}(A,A)$ into a group, except that we have not mentioned inverses. However, to say that every map in $\mathscr{A}$ is an isomorphism is exactly to say that every element of $\mathscr{A}(A,A)$ has an inverse with respect to $\circ$.

If we write $G$ for the group $\mathscr{A}(A,A)$, then the situation is this:

$$
\begin{array}{ll}
\textit{category }\mathscr{A}\textit{ with single object }A&\textit{corresponding group }G\\[1ex]
\text{maps in }\mathscr{A}&\text{elements of }G\\
\circ\text{ in }\mathscr{A}&\cdot\text{ in }G\\
1_A&1\in G
\end{array}
$$

The category $\mathscr{A}$ looks something like this:

![A one-object category with loops](/library/volume-87/diagrams/pdf-0023-group-category.png)

The arrows represent different maps $A\to A$, that is, different elements of the group $G$.

What the object of $\mathscr{A}$ is called makes no difference. It matters exactly as much as whether we choose $x$ or $y$ or $t$ to denote some variable in an algebra problem, which is to say, not at all. Later we will define ‘equivalence’ of categories, which will enable us to make a precise statement: the category of groups is equivalent to the category of (small) one-object categories in which every map is an isomorphism (Example 3.2.11).

The first time one meets the idea that a group is a kind of category, it is tempting to dismiss it as a coincidence or a trick. But it is not; there is real content.

To see this, suppose that your education had been shuffled and that you already knew about categories before being taught about groups. In your first group theory class, the lecturer declares that a group is supposed to be the system of all symmetries of an object. A symmetry of an object $X$, she says, is a way of mapping $X$ to itself in a reversible or invertible manner. At this point, you realize that she is talking about a very special type of <span class="original-page-anchor" id="pdf-page-24" aria-hidden="true"></span>category. In general, a category is a system consisting of *all* the mappings (not usually just the invertible ones) between *many* objects (not usually just one). So a group is just a category with the special properties that all the maps are invertible and there is only one object.

(d) The inverses played no essential part in the previous example, suggesting that it is worth thinking about ‘groups without inverses’. These are called monoids.

Formally, a **monoid** is a set equipped with an associative binary operation and a two-sided unit element. Groups describe the reversible transformations, or symmetries, that can be applied to an object; monoids describe the not-necessarily-reversible transformations. For instance, given any set $X$, there is a group consisting of all bijections $X \to X$, and there is a monoid consisting of all functions $X \to X$. In both cases, the binary operation is composition and the unit is the identity function on $X$. Another example of a monoid is the set $\mathbb{N} = \{0, 1, 2, \ldots\}$ of natural numbers, with $+$ as the operation and $0$ as the unit. Alternatively, we could take the set $\mathbb{N}$ with $\cdot$ as the operation and $1$ as the unit.

A category with one object is essentially the same thing as a monoid, by the same argument as for groups. This is stated formally in Example 3.2.11.

(e) A **preorder** is a reflexive transitive binary relation. A **preordered set** $(S, {\leq})$ is a set $S$ together with a preorder $\leq$ on it. Examples: $S = \mathbb{R}$ and $\leq$ has its usual meaning; $S$ is the set of subsets of $\{1, \ldots, 10\}$ and $\leq$ is $\subseteq$ (inclusion); $S = \mathbb{Z}$ and $a \leq b$ means that $a$ divides $b$.

A preordered set can be regarded as a category $\mathscr{A}$ in which, for each $A, B \in \mathscr{A}$, there is at most one map from $A$ to $B$. To see this, consider a category $\mathscr{A}$ with this property. It is not important what letter we use to denote the unique map from an object $A$ to an object $B$; all we need to record is which pairs $(A, B)$ of objects have the property that a map $A \to B$ does exist. Let us write $A \leq B$ to mean that there exists a map $A \to B$.

Since $\mathscr{A}$ is a category, and categories have composition, if $A \leq B \leq C$ then $A \leq C$. Since categories also have identities, $A \leq A$ for all $A$. The associativity and identity axioms are automatic. So, $\mathscr{A}$ amounts to a collection of objects equipped with a transitive reflexive binary relation, that is, a preorder. One can think of the unique map $A \to B$ as the statement or assertion that $A \leq B$.

An **order** on a set is a preorder $\leq$ with the property that if $A \leq B$ and $B \leq A$ then $A = B$. (Equivalently, if $A \cong B$ in the corresponding category then $A = B$.) Ordered sets are also called **partially ordered sets** or **posets**.

<span class="original-page-anchor" id="pdf-page-25" aria-hidden="true"></span>

An example of a preorder that is not an order is the divisibility relation $\mid$ on $\mathbb{Z}$: for there we have $2 \mid {-2}$ and $-2 \mid 2$ but $2 \neq -2$.

Here are two ways of constructing new categories from old.

**Construction 1.1.9** Every category $\mathscr{A}$ has an **opposite** or **dual** category $\mathscr{A}^{\mathrm{op}}$, defined by reversing the arrows. Formally, $\operatorname{ob}(\mathscr{A}^{\mathrm{op}}) = \operatorname{ob}(\mathscr{A})$ and $\mathscr{A}^{\mathrm{op}}(B, A) = \mathscr{A}(A, B)$ for all objects $A$ and $B$. Identities in $\mathscr{A}^{\mathrm{op}}$ are the same as in $\mathscr{A}$. Composition in $\mathscr{A}^{\mathrm{op}}$ is the same as in $\mathscr{A}$, but with the arguments reversed. To spell this out: if $A \xrightarrow{f} B \xrightarrow{g} C$ are maps in $\mathscr{A}^{\mathrm{op}}$ then $A \xleftarrow{f} B \xleftarrow{g} C$ are maps in $\mathscr{A}$; these give rise to a map $A \xleftarrow{f \circ g} C$ in $\mathscr{A}$, and the composite of the original pair of maps is the corresponding map $A \to C$ in $\mathscr{A}^{\mathrm{op}}$.

So, arrows $A \to B$ in $\mathscr{A}$ correspond to arrows $B \to A$ in $\mathscr{A}^{\mathrm{op}}$. According to the definition above, if $f\colon A \to B$ is an arrow in $\mathscr{A}$ then the corresponding arrow $B \to A$ in $\mathscr{A}^{\mathrm{op}}$ is also called $f$. Some people prefer to give it a different name, such as $f^{\mathrm{op}}$.

**Remark 1.1.10** The **principle of duality** is fundamental to category theory. Informally, it states that every categorical definition, theorem and proof has a **dual**, obtained by reversing all the arrows. Invoking the principle of duality can save work: given any theorem, reversing the arrows throughout its statement and proof produces a dual theorem. Numerous examples of duality appear throughout this book.

**Construction 1.1.11** Given categories $\mathscr{A}$ and $\mathscr{B}$, there is a **product category** $\mathscr{A} \times \mathscr{B}$, in which

$$
\begin{aligned}
\operatorname{ob}(\mathscr{A} \times \mathscr{B}) &= \operatorname{ob}(\mathscr{A}) \times \operatorname{ob}(\mathscr{B}), \\
(\mathscr{A} \times \mathscr{B})((A, B), (A', B')) &= \mathscr{A}(A, A') \times \mathscr{B}(B, B').
\end{aligned}
$$

Put another way, an object of the product category $\mathscr{A} \times \mathscr{B}$ is a pair $(A, B)$ where $A \in \mathscr{A}$ and $B \in \mathscr{B}$. A map $(A, B) \to (A', B')$ in $\mathscr{A} \times \mathscr{B}$ is a pair $(f, g)$ where $f\colon A \to A'$ in $\mathscr{A}$ and $g\colon B \to B'$ in $\mathscr{B}$. For the definitions of composition and identities in $\mathscr{A} \times \mathscr{B}$, see Exercise 1.1.14.

### Exercises

**1.1.12** Find three examples of categories not mentioned above.

**1.1.13** Show that a map in a category can have at most one inverse. That is, given a map $f\colon A \to B$, show that there is at most one map $g\colon B \to A$ such that $gf = 1_A$ and $fg = 1_B$.

<span class="original-page-anchor" id="pdf-page-26" aria-hidden="true"></span>

**1.1.14** Let $\mathscr{A}$ and $\mathscr{B}$ be categories. Construction 1.1.11 defined the product category $\mathscr{A} \times \mathscr{B}$, except that the definitions of composition and identities in $\mathscr{A} \times \mathscr{B}$ were not given. There is only one sensible way to define them; write it down.

**1.1.15** There is a category $\mathbf{Toph}$ whose objects are topological spaces and whose maps $X \to Y$ are homotopy classes of continuous maps from $X$ to $Y$. What do you need to know about homotopy in order to prove that $\mathbf{Toph}$ is a category? What does it mean, in purely topological terms, for two objects of $\mathbf{Toph}$ to be isomorphic?

## 1.2 Functors

One of the lessons of category theory is that whenever we meet a new type of mathematical object, we should always ask whether there is a sensible notion of ‘map’ between such objects. We can ask this about categories themselves. The answer is yes, and a map between categories is called a functor.

**Definition 1.2.1** Let $\mathscr{A}$ and $\mathscr{B}$ be categories. A **functor** $F\colon \mathscr{A} \to \mathscr{B}$ consists of:

- a function

  $$
  \operatorname{ob}(\mathscr{A}) \to \operatorname{ob}(\mathscr{B}),
  $$

  written as $A \mapsto F(A)$;

- for each $A, A' \in \mathscr{A}$, a function

  $$
  \mathscr{A}(A, A') \to \mathscr{B}(F(A), F(A')),
  $$

  written as $f \mapsto F(f)$,

satisfying the following axioms:

- $F(f' \circ f) = F(f') \circ F(f)$ whenever $A \xrightarrow{f} A' \xrightarrow{f'} A''$ in $\mathscr{A}$;
- $F(1_A) = 1_{F(A)}$ whenever $A \in \mathscr{A}$.

**Remarks 1.2.2** (a) The definition of functor is set up so that from each string

$$
A_0 \xrightarrow{f_1} \cdots \xrightarrow{f_n} A_n
$$

of maps in $\mathscr{A}$ (with $n \geq 0$), it is possible to construct exactly one map

$$
F(A_0) \to F(A_n)
$$

<span class="original-page-anchor" id="pdf-page-27" aria-hidden="true"></span>

in $\mathscr{B}$. For example, given maps

$$
A_0 \xrightarrow{f_1} A_1 \xrightarrow{f_2} A_2 \xrightarrow{f_3} A_3 \xrightarrow{f_4} A_4
$$

in $\mathscr{A}$, we can construct maps

![Two parallel arrows from F(A₀) to F(A₄), labelled F(f₄f₃)F(f₂f₁) and F(1_{A₄})F(f₄)F(f₃f₂)F(f₁).](/library/volume-87/diagrams/pdf-0027-functor-parallel-maps.png)

in $\mathscr{B}$, but the axioms imply that they are equal.

(b) We are familiar with the idea that structures and the structure-preserving maps between them form a category (such as $\mathbf{Grp}$, $\mathbf{Ring}$, etc.). In particular, this applies to categories and functors: there is a category $\mathbf{CAT}$ whose objects are categories and whose maps are functors.

One part of this statement is that functors can be composed. That is, given functors $\mathscr{A} \xrightarrow{F} \mathscr{B} \xrightarrow{G} \mathscr{C}$, there arises a new functor $\mathscr{A} \xrightarrow{G \circ F} \mathscr{C}$, defined in the obvious way. Another is that for every category $\mathscr{A}$, there is an identity functor $1_{\mathscr{A}}\colon \mathscr{A} \to \mathscr{A}$.

**Examples 1.2.3** Perhaps the easiest examples of functors are the so-called **forgetful functors**. (This is an informal term, with no precise definition.) For instance:

(a) There is a functor $U\colon \mathbf{Grp} \to \mathbf{Set}$ defined as follows: if $G$ is a group then $U(G)$ is the underlying set of $G$ (that is, its set of elements), and if $f\colon G \to H$ is a group homomorphism then $U(f)$ is the function $f$ itself. So $U$ forgets the group structure of groups and forgets that group homomorphisms are homomorphisms.

(b) Similarly, there is a functor $\mathbf{Ring} \to \mathbf{Set}$ forgetting the ring structure on rings, and (for any field $k$) there is a functor $\mathbf{Vect}_k \to \mathbf{Set}$ forgetting the vector space structure on vector spaces.

(c) Forgetful functors do not have to forget *all* the structure. For example, let $\mathbf{Ab}$ be the category of abelian groups. There is a functor $\mathbf{Ring} \to \mathbf{Ab}$ that forgets the multiplicative structure, remembering just the underlying additive group. Or, let $\mathbf{Mon}$ be the category of monoids. There is a functor $U\colon \mathbf{Ring} \to \mathbf{Mon}$ that forgets the additive structure, remembering just the underlying multiplicative monoid. (That is, if $R$ is a ring then $U(R)$ is the set $R$ made into a monoid via $\cdot$ and $1$.)

(d) There is an inclusion functor $U\colon \mathbf{Ab} \to \mathbf{Grp}$ defined by $U(A) = A$ for any abelian group $A$ and $U(f) = f$ for any homomorphism $f$ of abelian groups. It forgets that abelian groups are abelian.

<span class="original-page-anchor" id="pdf-page-28" aria-hidden="true"></span>

The forgetful functors in examples (a)–(c) forget *structure* on the objects, but that of example (d) forgets a *property*. Nevertheless, it turns out to be convenient to use the same word, ‘forgetful’, in both situations.

Although forgetting is a trivial operation, there are situations in which it is powerful. For example, it is a theorem that the order of any finite field is a prime power. An important step in the proof is to simply forget that the field is a field, remembering only that it is a vector space over its subfield $\{0, 1, 1 + 1, 1 + 1 + 1, \ldots\}$.

**Examples 1.2.4** **Free functors** are in some sense dual to forgetful functors (as we will see in the next chapter), although they are less elementary. Again, ‘free functor’ is an informal but useful term.

(a) Given any set $S$, one can build the **free group** $F(S)$ on $S$. This is a group containing $S$ as a subset and with no further properties other than those it is forced to have, in a sense made precise in Section 2.1. Intuitively, the group $F(S)$ is obtained from the set $S$ by adding just enough new elements that it becomes a group, but without imposing any equations other than those forced by the definition of group.

A little more precisely, the elements of $F(S)$ are formal expressions or **words** such as $x^{-4} y x^2 z y^{-3}$ (where $x, y, z \in S$). Two such words are seen as equal if one can be obtained from the other by the usual cancellation rules, so that, for example, $x^3 x y$, $x^4 y$, and $x^2 y^{-1} y x^2 y$ all represent the same element of $F(S)$. To multiply two words, just write one followed by the other; for instance, $x^{-4} y x$ times $x z y^{-3}$ is $x^{-4} y x^2 z y^{-3}$.

This construction assigns to each set $S$ a group $F(S)$. In fact, $F$ is a functor: any map of sets $f\colon S \to S'$ gives rise to a homomorphism of groups $F(f)\colon F(S) \to F(S')$. For instance, take the map of sets

$$
f\colon \{w, x, y, z\} \to \{u, v\}
$$

defined by $f(w) = f(x) = f(y) = u$ and $f(z) = v$. This gives rise to a homomorphism

$$
F(f)\colon F(\{w, x, y, z\}) \to F(\{u, v\}),
$$

which maps $x^{-4} y x^2 z y^{-3} \in F(\{w, x, y, z\})$ to

$$
u^{-4} u u^2 v u^{-3} = u^{-1} v u^{-3} \in F(\{u, v\}).
$$

(b) Similarly, we can construct the free commutative ring $F(S)$ on a set $S$, giving a functor $F$ from $\mathbf{Set}$ to the category $\mathbf{CRing}$ of commutative rings. In fact, $F(S)$ is something familiar, namely, the ring of polynomials over $\mathbb{Z}$ in commuting variables $x_s$ ($s \in S$). (A polynomial is, after all, just a <span class="original-page-anchor" id="pdf-page-29" aria-hidden="true"></span>formal expression built from the variables using the ring operations $+$, $-$ and $\cdot$.) For example, if $S$ is a two-element set then $F(S) \cong \mathbb{Z}[x,y]$.

(c) We can also construct the free vector space on a set. Fix a field $k$. The free functor $F:\mathbf{Set}\to\mathbf{Vect}_k$ is defined on objects by taking $F(S)$ to be a vector space with basis $S$. Any two such vector spaces are isomorphic; but it is perhaps not obvious that there is any such vector space at all, so we have to construct one. Loosely, $F(S)$ is the set of all formal $k$-linear combinations of elements of $S$, that is, expressions

$$
\sum_{s\in S}\lambda_s s
$$

where each $\lambda_s$ is a scalar and there are only finitely many values of $s$ such that $\lambda_s\ne 0$. (This restriction is imposed because one can only take *finite* sums in a vector space.) Elements of $F(S)$ can be added:

$$
\sum_{s\in S}\lambda_s s+\sum_{s\in S}\mu_s s=\sum_{s\in S}(\lambda_s+\mu_s)s.
$$

There is also a scalar multiplication on $F(S)$:

$$
c\cdot\sum_{s\in S}\lambda_s s=\sum_{s\in S}(c\lambda_s)s
$$

($c\in k$). In this way, $F(S)$ becomes a vector space.

To be completely precise and avoid talking about ‘expressions’, we can define $F(S)$ to be the set of all functions $\lambda:S\to k$ such that $\{s\in S\mid\lambda(s)\ne 0\}$ is finite. (Think of such a function $\lambda$ as corresponding to the expression $\sum_{s\in S}\lambda(s)s$.) To define addition on $F(S)$, we must define for each $\lambda,\mu\in F(S)$ a sum $\lambda+\mu\in F(S)$; it is given by

$$
(\lambda+\mu)(s)=\lambda(s)+\mu(s)
$$

($s\in S$). Similarly, the scalar multiplication is given by $(c\cdot\lambda)(s)=c\cdot\lambda(s)$ ($c\in k$, $\lambda\in F(S)$, $s\in S$).

Rings and vector spaces have the special property that it is relatively easy to write down an explicit formula for the free functor. The case of groups is much more typical. For most types of algebraic structure, describing the free functor requires as much fussy work as it does for groups. We return to this point in Example 2.1.3 and Example 6.3.11 (where we see how to avoid the fussy work entirely).

**Examples 1.2.5 (Functors in algebraic topology)** Historically, some of the first examples of functors arose in algebraic topology. There, the strategy is <span class="original-page-anchor" id="pdf-page-30" aria-hidden="true"></span>to learn about a space by extracting data from it in some clever way, assembling that data into an algebraic structure, then studying the algebraic structure instead of the original space. Algebraic topology therefore involves many functors from categories of spaces to categories of algebras.

(a) Let $\mathbf{Top}_*$ be the category of topological spaces equipped with a basepoint, together with the continuous basepoint-preserving maps. There is a functor $\pi_1:\mathbf{Top}_*\to\mathbf{Grp}$ assigning to each space $X$ with basepoint $x$ the fundamental group $\pi_1(X,x)$ of $X$ at $x$. (Some texts use the simpler notation $\pi_1(X)$, ignoring the choice of basepoint. This is more or less safe if $X$ is path-connected, but strictly speaking, the basepoint should always be specified.)

That $\pi_1$ is a functor means that it not only assigns to each space-with-basepoint $(X,x)$ a group $\pi_1(X,x)$, but also assigns to each basepoint-preserving continuous map

$$
f:(X,x)\to(Y,y)
$$

a homomorphism

$$
\pi_1(f):\pi_1(X,x)\to\pi_1(Y,y).
$$

Usually $\pi_1(f)$ is written as $f_*$. The functoriality axioms say that $(g\circ f)_*=g_*\circ f_*$ and $(1_{(X,x)})_*=1_{\pi_1(X,x)}$.

(b) For each $n\in\mathbb{N}$, there is a functor $H_n:\mathbf{Top}\to\mathbf{Ab}$ assigning to a space its $n$th homology group (in any of several possible senses).

**Example 1.2.6** Any system of polynomial equations such as

$$
2x^2+y^2-3z^2=1\tag{1.1}
$$

$$
x^3+x=y^2\tag{1.2}
$$

gives rise to a functor $\mathbf{CRing}\to\mathbf{Set}$. Indeed, for each commutative ring $A$, let $F(A)$ be the set of triples $(x,y,z)\in A\times A\times A$ satisfying equations (1.1) and (1.2). Whenever $f:A\to B$ is a ring homomorphism and $(x,y,z)\in F(A)$, we have $(f(x),f(y),f(z))\in F(B)$; so the map of rings $f:A\to B$ induces a map of sets $F(f):F(A)\to F(B)$. This defines a functor $F:\mathbf{CRing}\to\mathbf{Set}$.

In algebraic geometry, a **scheme** is a functor $\mathbf{CRing}\to\mathbf{Set}$ with certain properties. (This is not the most common way of phrasing the definition, but it is equivalent.) The functor $F$ above is a simple example.

**Example 1.2.7** Let $G$ and $H$ be monoids (or groups, if you prefer), regarded as one-object categories $\mathscr{G}$ and $\mathscr{H}$. A functor $F:\mathscr{G}\to\mathscr{H}$ must send the unique object of $\mathscr{G}$ to the unique object of $\mathscr{H}$, so it is determined by its effect <span class="original-page-anchor" id="pdf-page-31" aria-hidden="true"></span>on maps. Hence, the functor $F:\mathscr{G}\to\mathscr{H}$ amounts to a function $F:G\to H$ such that $F(g'g)=F(g')F(g)$ for all $g',g\in G$, and $F(1)=1$. In other words, a functor $\mathscr{G}\to\mathscr{H}$ is just a homomorphism $G\to H$.

**Example 1.2.8** Let $G$ be a monoid, regarded as a one-object category $\mathscr{G}$. A functor $F:\mathscr{G}\to\mathbf{Set}$ consists of a set $S$ (the value of $F$ at the unique object of $\mathscr{G}$) together with, for each $g\in G$, a function $F(g):S\to S$, satisfying the functoriality axioms. Writing $(F(g))(s)=g\cdot s$, we see that the functor $F$ amounts to a set $S$ together with a function

$$
\begin{array}{ccc}
G\times S&\to&S\\
(g,s)&\mapsto&g\cdot s
\end{array}
$$

satisfying $(g'g)\cdot s=g'\cdot(g\cdot s)$ and $1\cdot s=s$ for all $g,g'\in G$ and $s\in S$. In other words, a functor $\mathscr{G}\to\mathbf{Set}$ is a set equipped with a left action by $G$: a **left $G$-set**, for short.

Similarly, a functor $\mathscr{G}\to\mathbf{Vect}_k$ is exactly a $k$-linear representation of $G$, in the sense of representation theory. This can reasonably be taken as the *definition* of representation.

**Example 1.2.9** When $A$ and $B$ are (pre)ordered sets, a functor between the corresponding categories is exactly an **order-preserving map**, that is, a function $f:A\to B$ such that $a\le a'\implies f(a)\le f(a')$. Exercise 1.2.22 asks you to verify this.

Sometimes we meet functor-like operations that reverse the arrows, with a map $A\to A'$ in $\mathscr{A}$ giving rise to a map $F(A)\leftarrow F(A')$ in $\mathscr{B}$. Such operations are called contravariant functors.

**Definition 1.2.10** Let $\mathscr{A}$ and $\mathscr{B}$ be categories. A **contravariant functor** from $\mathscr{A}$ to $\mathscr{B}$ is a functor $\mathscr{A}^{\mathrm{op}}\to\mathscr{B}$.

To avoid confusion, we write ‘a contravariant functor from $\mathscr{A}$ to $\mathscr{B}$’ rather than ‘a contravariant functor $\mathscr{A}\to\mathscr{B}$’.

Functors $\mathscr{C}\to\mathscr{D}$ correspond one-to-one with functors $\mathscr{C}^{\mathrm{op}}\to\mathscr{D}^{\mathrm{op}}$, and $(\mathscr{A}^{\mathrm{op}})^{\mathrm{op}}=\mathscr{A}$, so a contravariant functor from $\mathscr{A}$ to $\mathscr{B}$ can also be described as a functor $\mathscr{A}\to\mathscr{B}^{\mathrm{op}}$. Which description we use is not enormously important, but in the long run, the convention in Definition 1.2.10 makes life easier.

An ordinary functor $\mathscr{A}\to\mathscr{B}$ is sometimes called a **covariant functor** from $\mathscr{A}$ to $\mathscr{B}$, for emphasis.

**Example 1.2.11** We can tell a lot about a space by examining the functions on it. The importance of this principle in twentieth- and twenty-first-century mathematics can hardly be exaggerated.

<span class="original-page-anchor" id="pdf-page-32" aria-hidden="true"></span>

For example, given a topological space $X$, let $C(X)$ be the ring of continuous real-valued functions on $X$. The ring operations are defined ‘pointwise’: for instance, if $p_1,p_2:X\to\mathbb{R}$ are continuous maps then the map $p_1+p_2:X\to\mathbb{R}$ is defined by

$$
(p_1+p_2)(x)=p_1(x)+p_2(x)
$$

($x\in X$). A continuous map $f:X\to Y$ induces a ring homomorphism $C(f):C(Y)\to C(X)$, defined at $q\in C(Y)$ by taking $(C(f))(q)$ to be the composite map

$$
X\xrightarrow{f}Y\xrightarrow{q}\mathbb{R}.
$$

Note that $C(f)$ goes in the opposite direction from $f$. After checking some axioms (Exercise 1.2.26), we conclude that $C$ is a contravariant functor from $\mathbf{Top}$ to $\mathbf{Ring}$.

While this particular example will not play a large part in this text, it is worth close attention. It illustrates the important idea of a structure whose elements are maps (in this case, a ring whose elements are continuous functions). The way in which $C$ becomes a functor, via composition, is also important. Similar constructions will be crucial in later chapters.

For certain classes of space, the passage from $X$ to $C(X)$ loses no information: there is a way of reconstructing the space $X$ from the ring $C(X)$. For this and related reasons, it is sometimes said that ‘algebra is dual to geometry’.

**Example 1.2.12** Let $k$ be a field. For any two vector spaces $V$ and $W$ over $k$, there is a vector space

$$
\mathbf{Hom}(V,W)=\{\text{linear maps }V\to W\}.
$$

The elements of this vector space are themselves maps, and the vector space operations (addition and scalar multiplication) are defined pointwise, as in the last example.

Now fix a vector space $W$. Any linear map $f:V\to V'$ induces a linear map

$$
f^*:\mathbf{Hom}(V',W)\to\mathbf{Hom}(V,W),
$$

defined at $q\in\mathbf{Hom}(V',W)$ by taking $f^*(q)$ to be the composite map

$$
V\xrightarrow{f}V'\xrightarrow{q}W.
$$

This defines a functor

$$
\mathbf{Hom}(-,W):\mathbf{Vect}_k^{\mathrm{op}}\to\mathbf{Vect}_k.
$$

<span class="original-page-anchor" id="pdf-page-33" aria-hidden="true"></span>

The symbol ‘$-$’ is a blank or placeholder, into which arguments can be inserted. Thus, the value of $\mathbf{Hom}(-,W)$ at $V$ is $\mathbf{Hom}(V,W)$. Sometimes we use a blank space instead of $-$, as in $\mathbf{Hom}(\hspace{1em},W)$.

An important special case is where $W$ is $k$, seen as a one-dimensional vector space over itself. The vector space $\mathbf{Hom}(V,k)$ is called the **dual** of $V$, and is written as $V^*$. So there is a contravariant functor

$$
(\hspace{0.5em})^*=\mathbf{Hom}(-,k):\mathbf{Vect}_k^{\mathrm{op}}\to\mathbf{Vect}_k
$$

sending each vector space to its dual.

**Example 1.2.13** For each $n\in\mathbb{N}$, there is a functor $H^n:\mathbf{Top}^{\mathrm{op}}\to\mathbf{Ab}$ assigning to a space its $n$th cohomology group.

**Example 1.2.14** Let $G$ be a monoid, regarded as a one-object category $\mathscr{G}$. A functor $\mathscr{G}^{\mathrm{op}}\to\mathbf{Set}$ is a *right* $G$-set, for essentially the same reasons as in Example 1.2.8.

That left actions are covariant functors and right actions are contravariant functors is a consequence of a basic notational choice: we write the value of a function $f$ at an element $x$ as $f(x)$, not $(x)f$.

Contravariant functors whose codomain is $\mathbf{Set}$ are important enough to have their own special name.

**Definition 1.2.15** Let $\mathscr{A}$ be a category. A **presheaf** on $\mathscr{A}$ is a functor $\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}$.

The name comes from the following special case. Let $X$ be a topological space. Write $\mathscr{O}(X)$ for the poset of open subsets of $X$, ordered by inclusion. View $\mathscr{O}(X)$ as a category, as in Example 1.1.8(e). Thus, the objects of $\mathscr{O}(X)$ are the open subsets of $X$, and for $U,U'\in\mathscr{O}(X)$, there is one map $U\to U'$ if $U\subseteq U'$, and there are none otherwise. A **presheaf** on the space $X$ is a presheaf on the category $\mathscr{O}(X)$. For example, given any space $X$, there is a presheaf $F$ on $X$ defined by

$$
F(U)=\{\text{continuous functions }U\to\mathbb{R}\}
$$

($U\in\mathscr{O}(X)$) and, whenever $U\subseteq U'$ are open subsets of $X$, by taking the map $F(U')\to F(U)$ to be restriction. Presheaves, and a certain class of presheaves called sheaves, play an important role in modern geometry.

We know very well that for *functions* between *sets*, it is sometimes useful to consider special kinds of function such as injections, surjections and bijections. We also know that the notions of injection and subset are related: for instance,

<span class="original-page-anchor" id="pdf-page-34" aria-hidden="true"></span>

![Fullness and faithfulness](/library/volume-87/diagrams/pdf-0034-full-faithful.png)

Figure 1.1 Fullness and faithfulness.

whenever $B$ is a subset of $A$, there is an injection $B \to A$ given by inclusion. In this section and the next, we introduce some similar notions for *functors* between *categories*, beginning with the following definitions.

**Definition 1.2.16** A functor $F\colon \mathscr{A} \to \mathscr{B}$ is **faithful** (respectively, **full**) if for each $A,A'\in\mathscr{A}$, the function

$$
\begin{array}{ccc}
\mathscr{A}(A,A') & \to & \mathscr{B}(F(A),F(A'))\\
f & \mapsto & F(f)
\end{array}
$$

is injective (respectively, surjective).

**Warning 1.2.17** Note the roles of $A$ and $A'$ in the definition. Faithfulness does *not* say that if $f_1$ and $f_2$ are distinct maps in $\mathscr{A}$ then $F(f_1)\neq F(f_2)$ (Exercise 1.2.27). In the situation of Figure 1.1, $F$ is faithful if for each $A,A'$ and $g$ as shown, there is at most one dotted arrow that $F$ sends to $g$. It is full if for each such $A,A'$ and $g$, there is at least one dotted arrow that $F$ sends to $g$.

**Definition 1.2.18** Let $\mathscr{A}$ be a category. A **subcategory** $\mathscr{S}$ of $\mathscr{A}$ consists of a subclass $\operatorname{ob}(\mathscr{S})$ of $\operatorname{ob}(\mathscr{A})$ together with, for each $S,S'\in\operatorname{ob}(\mathscr{S})$, a subclass $\mathscr{S}(S,S')$ of $\mathscr{A}(S,S')$, such that $\mathscr{S}$ is closed under composition and identities. It is a **full** subcategory if $\mathscr{S}(S,S')=\mathscr{A}(S,S')$ for all $S,S'\in\operatorname{ob}(\mathscr{S})$.

A full subcategory therefore consists of a selection of the objects, with all of the maps between them. So, a full subcategory can be specified simply by saying what its objects are. For example, $\mathbf{Ab}$ is the full subcategory of $\mathbf{Grp}$ consisting of the groups that are abelian.

Whenever $\mathscr{S}$ is a subcategory of a category $\mathscr{A}$, there is an inclusion functor $I\colon\mathscr{S}\to\mathscr{A}$ defined by $I(S)=S$ and $I(f)=f$. It is automatically faithful, and it is full if and only if $\mathscr{S}$ is a full subcategory.

**Warning 1.2.19** The image of a functor need not be a subcategory. For ex<span class="original-page-anchor" id="pdf-page-35" aria-hidden="true"></span>ample, consider the functor

![A functor whose image is not a subcategory](/library/volume-87/diagrams/pdf-0035-functor-image.png)

defined by $F(A)=X$, $F(B)=F(B')=Y$, $F(C)=Z$, $F(f)=p$, and $F(g)=q$. Then $p$ and $q$ are in the image of $F$, but $qp$ is not.

### Exercises

**1.2.20** Find three examples of functors not mentioned above.

**1.2.21** Show that functors preserve isomorphism. That is, prove that if $F\colon\mathscr{A}\to\mathscr{B}$ is a functor and $A,A'\in\mathscr{A}$ with $A\cong A'$, then $F(A)\cong F(A')$.

**1.2.22** Prove the assertion made in Example 1.2.9. In other words, given ordered sets $A$ and $B$, and denoting by $\mathscr{A}$ and $\mathscr{B}$ the corresponding categories, show that a functor $\mathscr{A}\to\mathscr{B}$ amounts to an order-preserving map $A\to B$.

**1.2.23** Two categories $\mathscr{A}$ and $\mathscr{B}$ are **isomorphic**, written as $\mathscr{A}\cong\mathscr{B}$, if they are isomorphic as objects of $\mathbf{CAT}$.

(a) Let $G$ be a group, regarded as a one-object category all of whose maps are isomorphisms. Then its opposite $G^{\mathrm{op}}$ is also a one-object category all of whose maps are isomorphisms, and can therefore be regarded as a group too. What is $G^{\mathrm{op}}$, in purely group-theoretic terms? Prove that $G$ is isomorphic to $G^{\mathrm{op}}$.

(b) Find a monoid not isomorphic to its opposite.

**1.2.24** Is there a functor $Z\colon\mathbf{Grp}\to\mathbf{Grp}$ with the property that $Z(G)$ is the centre of $G$ for all groups $G$?

**1.2.25** Sometimes we meet functors whose domain is a product $\mathscr{A}\times\mathscr{B}$ of categories. Here you will show that such a functor can be regarded as an interlocking pair of families of functors, one defined on $\mathscr{A}$ and the other defined on $\mathscr{B}$. (This is very like the situation for bilinear and linear maps.)

(a) Let $F\colon\mathscr{A}\times\mathscr{B}\to\mathscr{C}$ be a functor. Prove that for each $A\in\mathscr{A}$, there is a functor $F^A\colon\mathscr{B}\to\mathscr{C}$ defined on objects $B\in\mathscr{B}$ by $F^A(B)=F(A,B)$ and on maps $g$ in $\mathscr{B}$ by $F^A(g)=F(1_A,g)$. Prove that for each $B\in\mathscr{B}$, there is a functor $F_B\colon\mathscr{A}\to\mathscr{C}$ defined similarly.

<span class="original-page-anchor" id="pdf-page-36" aria-hidden="true"></span>

(b) Let $F\colon\mathscr{A}\times\mathscr{B}\to\mathscr{C}$ be a functor. With notation as in (a), show that the families of functors $(F^A)_{A\in\mathscr{A}}$ and $(F_B)_{B\in\mathscr{B}}$ satisfy the following two conditions:

- if $A\in\mathscr{A}$ and $B\in\mathscr{B}$ then $F^A(B)=F_B(A)$;
- if $f\colon A\to A'$ in $\mathscr{A}$ and $g\colon B\to B'$ in $\mathscr{B}$ then $F^{A'}(g)\circ F_B(f)=F_{B'}(f)\circ F^A(g)$.

(c) Now take categories $\mathscr{A}$, $\mathscr{B}$ and $\mathscr{C}$, and take families of functors $(F^A)_{A\in\mathscr{A}}$ and $(F_B)_{B\in\mathscr{B}}$ satisfying the two conditions in (b). Prove that there is a unique functor $F\colon\mathscr{A}\times\mathscr{B}\to\mathscr{C}$ satisfying the equations in (a). (‘There is a unique functor’ means in particular that there *is* a functor, so you have to prove existence as well as uniqueness.)

**1.2.26** Fill in the details of Example 1.2.11, thus constructing a functor $C\colon\mathbf{Top}^{\mathrm{op}}\to\mathbf{Ring}$.

**1.2.27** Find an example of a functor $F\colon\mathscr{A}\to\mathscr{B}$ such that $F$ is faithful but there exist distinct maps $f_1$ and $f_2$ in $\mathscr{A}$ with $F(f_1)=F(f_2)$.

**1.2.28** (a) Of the examples of functors appearing in this section, which are faithful and which are full?

(b) Write down one example of a functor that is both full and faithful, one that is full but not faithful, one that is faithful but not full, and one that is neither.

**1.2.29** (a) What are the subcategories of an ordered set? Which are full?

(b) What are the subcategories of a group? (Careful!) Which are full?

## 1.3 Natural transformations

We now know about categories. We also know about functors, which are maps between categories. Perhaps surprisingly, there is a further notion of ‘map between functors’. Such maps are called natural transformations. This notion only applies when the functors have the same domain and codomain:

$$
\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}.
$$

To see how this might work, let us consider a special case. Let $\mathscr{A}$ be the discrete category (Example 1.1.8(b)) whose objects are the natural numbers $0,1,2,\ldots$. A functor $F$ from $\mathscr{A}$ to another category $\mathscr{B}$ is simply a sequence <span class="original-page-anchor" id="pdf-page-37" aria-hidden="true"></span>$(F_0,F_1,F_2,\ldots)$ of objects of $\mathscr{B}$. Let $G$ be another functor from $\mathscr{A}$ to $\mathscr{B}$, consisting of another sequence $(G_0,G_1,G_2,\ldots)$ of objects of $\mathscr{B}$. It would be reasonable to define a ‘map’ from $F$ to $G$ to be a sequence

$$
\Bigl(F_0\xrightarrow{\alpha_0}G_0,\ F_1\xrightarrow{\alpha_1}G_1,\ F_1\xrightarrow{\alpha_2}G_2,\ \ldots\Bigr)
$$

of maps in $\mathscr{B}$. The situation can be depicted as follows:

![Components of a natural transformation from a discrete category](/library/volume-87/diagrams/pdf-0037-discrete-components.png)

(The right-hand diagram should not be understood too literally. Some of the objects $F_i$ or $G_i$ might be equal, and there might be much else in $\mathscr{B}$ besides what is shown.)

This suggests that in the general case, a natural transformation between functors $\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}$ should consist of maps $\alpha_A\colon F(A)\to G(A)$, one for each $A\in\mathscr{A}$. In the example above, the category $\mathscr{A}$ had the special property of not containing any nontrivial maps. In general, we demand some kind of compatibility between the maps in $\mathscr{A}$ and the maps $\alpha_A$.

**Definition 1.3.1** Let $\mathscr{A}$ and $\mathscr{B}$ be categories and let $\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}$ be functors. A **natural transformation** $\alpha\colon F\to G$ is a family $\bigl(F(A)\xrightarrow{\alpha_A}G(A)\bigr)_{A\in\mathscr{A}}$ of maps in $\mathscr{B}$ such that for every map $A\xrightarrow{f}A'$ in $\mathscr{A}$, the square

![Naturality square (1.3)](/library/volume-87/diagrams/pdf-0037-naturality-square.png)

commutes. The maps $\alpha_A$ are called the **components** of $\alpha$.

**Remarks 1.3.2** (a) The definition of natural transformation is set up so that from each map $A\xrightarrow{f}A'$ in $\mathscr{A}$, it is possible to construct exactly one map $F(A)\to G(A')$ in $\mathscr{B}$. When $f=1_A$, this map is $\alpha_A$. For a general $f$, it is the diagonal of the square (1.3), and ‘exactly one’ implies that the square commutes.

<span class="original-page-anchor" id="pdf-page-38" aria-hidden="true"></span>

(b) We write

![Notation for a natural transformation](/library/volume-87/diagrams/pdf-0038-two-cell.png)

to mean that $\alpha$ is a natural transformation from $F$ to $G$.

**Example 1.3.3** Let $\mathscr{A}$ be a discrete category, and let $F,G\colon\mathscr{A}\to\mathscr{B}$ be functors. Then $F$ and $G$ are just families $(F(A))_{A\in\mathscr{A}}$ and $(G(A))_{A\in\mathscr{A}}$ of objects of $\mathscr{B}$. A natural transformation $\alpha\colon F\to G$ is just a family $\bigl(F(A)\xrightarrow{\alpha_A}G(A)\bigr)_{A\in\mathscr{A}}$ of maps in $\mathscr{B}$, as claimed above in the case $\operatorname{ob}\mathscr{A}=\mathbb{N}$. In principle, this family must satisfy the naturality axiom (1.3) for every map $f$ in $\mathscr{A}$; but the only maps in $\mathscr{A}$ are the identities, and when $f$ is an identity, this axiom holds automatically.

**Example 1.3.4** Recall from Examples 1.1.8 that a group (or more generally, a monoid) $G$ can be regarded as a one-object category. Also recall from Example 1.2.8 that a functor from the category $G$ to $\mathbf{Set}$ is nothing but a left $G$-set. (Previously we used $\mathscr{G}$ to denote the category corresponding to the group $G$; from now on we use $G$ to denote them both.) Take two $G$-sets, $S$ and $T$. Since $S$ and $T$ can be regarded as functors $G\to\mathbf{Set}$, we can ask: what is a natural transformation

![A natural transformation between G-sets](/library/volume-87/diagrams/pdf-0038-g-equivariant.png)

in concrete terms?

Such a natural transformation consists of a single map in $\mathbf{Set}$ (since $G$ has just one object), satisfying some axioms. Precisely, it is a function $\alpha\colon S\to T$ such that $\alpha(g\cdot s)=g\cdot\alpha(s)$ for all $s\in S$ and $g\in G$. (Why?) In other words, it is just a map of $G$-sets, sometimes called a **$G$-equivariant** map.

**Example 1.3.5** Fix a natural number $n$. In this example, we will see how ‘determinant of an $n\times n$ matrix’ can be understood as a natural transformation.

For any commutative ring $R$, the $n\times n$ matrices with entries in $R$ form a monoid $M_n(R)$ under multiplication. Moreover, any ring homomorphism $R\to S$ induces a monoid homomorphism $M_n(R)\to M_n(S)$. This defines a functor $M_n\colon\mathbf{CRing}\to\mathbf{Mon}$ from the category of commutative rings to the category of monoids.

Also, the elements of any ring $R$ form a monoid $U(R)$ under multiplication, giving another functor $U\colon\mathbf{CRing}\to\mathbf{Mon}$.

<span class="original-page-anchor" id="pdf-page-39" aria-hidden="true"></span>

Now, every $n\times n$ matrix $X$ over a commutative ring $R$ has a determinant $\det_R(X)$, which is an element of $R$. Familiar properties of determinant —

$$
\det_R(XY)=\det_R(X)\det_R(Y),\qquad \det_R(I)=1
$$

— tell us that for each $R$, the function $\det_R\colon M_n(R)\to U(R)$ is a monoid homomorphism. So, we have a family of maps

$$
\Bigl(M_n(R)\xrightarrow{\det_R}U(R)\Bigr)_{R\in\mathbf{CRing}},
$$

and it makes sense to ask whether they define a natural transformation

![Determinant as a natural transformation](/library/volume-87/diagrams/pdf-0039-determinant.png)

Indeed, they do. That the naturality squares commute (check!) reflects the fact that determinant is defined in the same way for all rings. We do not use one definition of determinant for one ring and a different definition for another ring. Generally speaking, the naturality axiom (1.3) is supposed to capture the idea that the family $(\alpha_A)_{A\in\mathscr{A}}$ is defined in a uniform way across all $A\in\mathscr{A}$.

**Construction 1.3.6** Natural transformations are a kind of map, so we would expect to be able to compose them. We can. Given natural transformations

![Two composable natural transformations](/library/volume-87/diagrams/pdf-0039-vertical-composition.png)

there is a composite natural transformation

![The composite natural transformation](/library/volume-87/diagrams/pdf-0039-composite.png)

defined by $(\beta\circ\alpha)_A=\beta_A\circ\alpha_A$ for all $A\in\mathscr{A}$. There is also an identity natural transformation

![The identity natural transformation](/library/volume-87/diagrams/pdf-0039-identity.png)

on any functor $F$, defined by $(1_F)_A=1_{F(A)}$. So for any two categories $\mathscr{A}$ and $\mathscr{B}$, there is a category whose objects are the functors from $\mathscr{A}$ to $\mathscr{B}$ and whose maps are the natural transformations between them. This is called the **functor category** from $\mathscr{A}$ to $\mathscr{B}$, and written as $[\mathscr{A},\mathscr{B}]$ or $\mathscr{B}^{\mathscr{A}}$.

<span class="original-page-anchor" id="pdf-page-40" aria-hidden="true"></span>

**Example 1.3.7** Let $2$ be the discrete category with two objects. A functor from $2$ to a category $\mathscr{B}$ is a pair of objects of $\mathscr{B}$, and a natural transformation is a pair of maps. The functor category $[2,\mathscr{B}]$ is therefore isomorphic to the product category $\mathscr{B}\times\mathscr{B}$ (Construction 1.1.11). This fits well with the alternative notation $\mathscr{B}^2$ for the functor category.

**Example 1.3.8** Let $G$ be a monoid. Then $[G,\mathbf{Set}]$ is the category of left $G$-sets, and $[G^{\mathrm{op}},\mathbf{Set}]$ is the category of right $G$-sets (Example 1.2.14).

**Example 1.3.9** Take ordered sets $A$ and $B$, viewed as categories (as in Example 1.1.8(e)). Given order-preserving maps $A\overset{f}{\underset{g}{\rightrightarrows}}B$, viewed as functors (as in Example 1.2.9), there is at most one natural transformation

![A natural transformation between order-preserving maps](/library/volume-87/diagrams/pdf-0040-ordered-sets.png)

and there is one if and only if $f(a)\leq g(a)$ for all $a\in A$. (The naturality axiom (1.3) holds automatically, because in an ordered set, all diagrams commute.) So $[A,B]$ is an ordered set too; its elements are the order-preserving maps from $A$ to $B$, and $f\leq g$ if and only if $f(a)\leq g(a)$ for all $a\in A$.

Everyday phrases such as ‘*the* cyclic group of order $6$’ and ‘*the* product of two spaces’ reflect the fact that given two isomorphic objects of a category, we usually neither know nor care whether they are actually equal. This is enormously important.

In particular, the lesson applies when the category concerned is a functor category. In other words, given two functors $F,G\colon\mathscr{A}\to\mathscr{B}$, we usually do not care whether they are literally equal. (Equality would imply that the objects $F(A)$ and $G(A)$ of $\mathscr{B}$ were equal for all $A\in\mathscr{A}$, a level of detail in which we have just declared ourselves to be uninterested.) What really matters is whether they are naturally isomorphic.

**Definition 1.3.10** Let $\mathscr{A}$ and $\mathscr{B}$ be categories. A **natural isomorphism** between functors from $\mathscr{A}$ to $\mathscr{B}$ is an isomorphism in $[\mathscr{A},\mathscr{B}]$.

An equivalent form of the definition is often useful:

**Lemma 1.3.11** Let

![A natural transformation alpha from F to G](/library/volume-87/diagrams/pdf-0040-isomorphism-components.png)

be a natural transformation. Then $\alpha$ is a natural isomorphism if and only if $\alpha_A\colon F(A)\to G(A)$ is an isomorphism for all $A\in\mathscr{A}$.

<span class="original-page-anchor" id="pdf-page-41" aria-hidden="true"></span>

**Proof** Exercise 1.3.26. $\square$

Of course, we say that functors $F$ and $G$ are **naturally isomorphic** if there exists a natural isomorphism from $F$ to $G$. Since natural isomorphism is just isomorphism in a particular category (namely, $[\mathscr{A},\mathscr{B}]$), we already have notation for this: $F\cong G$.

**Definition 1.3.12** Given functors $\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}$, we say that

$$
F(A)\cong G(A)\text{ \textbf{naturally in} }A
$$

if $F$ and $G$ are naturally isomorphic.

This alternative terminology can be understood as follows. If $F(A)\cong G(A)$ naturally in $A$ then certainly $F(A)\cong G(A)$ for each individual $A$, but more is true: we can choose isomorphisms $\alpha_A\colon F(A)\to G(A)$ in such a way that the naturality axiom (1.3) is satisfied.

**Example 1.3.13** Let $F,G\colon\mathscr{A}\to\mathscr{B}$ be functors from a discrete category $\mathscr{A}$ to a category $\mathscr{B}$. Then $F\cong G$ if and only if $F(A)\cong G(A)$ for all $A\in\mathscr{A}$.

So in *this* case, $F(A)\cong G(A)$ naturally in $A$ if and only if $F(A)\cong G(A)$ for all $A$. But this is only true because $\mathscr{A}$ is discrete. In general, it is emphatically false. There are many examples of categories and functors $\mathscr{A}\overset{F}{\underset{G}{\rightrightarrows}}\mathscr{B}$ such that $F(A)\cong G(A)$ for all $A\in\mathscr{A}$, but not *naturally* in $A$. Exercise 1.3.31 gives an example from combinatorics.

**Example 1.3.14** Let $\mathbf{FDVect}$ be the category of finite-dimensional vector spaces over some field $k$. The dual vector space construction defines a contravariant functor from $\mathbf{FDVect}$ to itself (Example 1.2.12), and the double dual construction therefore defines a covariant functor from $\mathbf{FDVect}$ to itself.

Moreover, we have for each $V\in\mathbf{FDVect}$ a canonical isomorphism $\alpha_V\colon V\to V^{**}$. Given $v\in V$, the element $\alpha_V(v)$ of $V^{**}$ is ‘evaluation at $v$’; that is, $\alpha_V(v)\colon V^*\to k$ maps $\phi\in V^*$ to $\phi(v)\in k$. That $\alpha_V$ is an isomorphism is a standard result in the theory of finite-dimensional vector spaces.

This defines a natural transformation

![The natural map to the double dual](/library/volume-87/diagrams/pdf-0041-double-dual.png)

from the identity functor to the double dual functor. By Lemma 1.3.11, $\alpha$ is <span class="original-page-anchor" id="pdf-page-42" aria-hidden="true"></span>a natural isomorphism. So $1_{\mathbf{FDVect}} \cong (\ )^{**}$. Equivalently, in the language of Definition 1.3.12, $V \cong V^{**}$ naturally in $V$.

This is one of those occasions on which category theory makes an intuition precise. In some informal sense, evident before you learn anything about category theory, the isomorphism between a finite-dimensional vector space and its double dual is ‘natural’ or ‘canonical’: no arbitrary choices are needed in order to define it. In contrast, to specify an isomorphism between $V$ and its single dual $V^*$, we need to make an arbitrary choice of basis, and the isomorphism really does depend on the basis that we choose.

In the example on vector spaces, the word **canonical** was used. It is an informal word, meaning something like ‘God-given’ or ‘defined without making arbitrary choices’. For example, for any two sets $A$ and $B$, there is a canonical bijection $A \times B \to B \times A$ defined by $(a,b) \mapsto (b,a)$, and there is a canonical function $A \times B \to A$ defined by $(a,b) \mapsto a$. But the function $B \to A$ defined by ‘choose an element $a_0 \in A$ and send everything to $a_0$’ is not canonical, because the choice of $a_0$ is arbitrary.

The concept of natural isomorphism leads unavoidably to another central concept: equivalence of categories.

Two elements of a set are either equal or not. Two objects of a category can be equal, not equal but isomorphic, or not even isomorphic. As explained before Definition 1.3.10, the notion of equality between two objects of a category is unreasonably strict; it is usually isomorphism that we care about. So:

- the right notion of sameness of two elements of a set is equality;
- the right notion of sameness of two objects of a category is isomorphism.

When applied to a functor category $[\mathscr{A},\mathscr{B}]$, the second point tells us that:

- the right notion of sameness of two functors $\mathscr{A} \rightrightarrows \mathscr{B}$ is natural isomorphism.

But what is the right notion of sameness of two *categories*? Isomorphism is unreasonably strict, as if $\mathscr{A} \cong \mathscr{B}$ then there are functors

![The functors F and G in opposite directions, equation (1.4).](/library/volume-87/diagrams/pdf-0042-equivalence-functors.png)

such that

$$
G \circ F = 1_{\mathscr{A}} \qquad \text{and} \qquad F \circ G = 1_{\mathscr{B}}, \tag{1.5}
$$

and we have just seen that the notion of equality between functors is too strict.

The most useful notion of sameness of categories, called ‘equivalence’, is <span class="original-page-anchor" id="pdf-page-43" aria-hidden="true"></span>looser than isomorphism. To obtain the definition, we simply replace the unreasonably strict equalities in (1.5) by isomorphisms. This gives

$$
G \circ F \cong 1_{\mathscr{A}} \qquad \text{and} \qquad F \circ G \cong 1_{\mathscr{B}}.
$$

**Definition 1.3.15** An **equivalence** between categories $\mathscr{A}$ and $\mathscr{B}$ consists of a pair (1.4) of functors together with natural isomorphisms

$$
\eta\colon 1_{\mathscr{A}} \to G \circ F, \qquad \varepsilon\colon F \circ G \to 1_{\mathscr{B}}.
$$

If there exists an equivalence between $\mathscr{A}$ and $\mathscr{B}$, we say that $\mathscr{A}$ and $\mathscr{B}$ are **equivalent**, and write $\mathscr{A} \simeq \mathscr{B}$. We also say that the functors $F$ and $G$ are **equivalences**.

The directions of $\eta$ and $\varepsilon$ are not very important, since they are isomorphisms anyway. The reason for this particular choice will become apparent when we come to discuss adjunctions (Section 2.2).

**Warning 1.3.16** The symbol $\cong$ is used for isomorphism of objects of a category, and in particular for isomorphism of categories (which are objects of $\mathbf{CAT}$). The symbol $\simeq$ is used for equivalence of categories. At least, this is the convention used in this book and by most category theorists, although it is far from universal in mathematics at large.

There is a very useful alternative characterization of those functors that are equivalences. First, we need a definition.

**Definition 1.3.17** A functor $F\colon \mathscr{A} \to \mathscr{B}$ is **essentially surjective on objects** if for all $B \in \mathscr{B}$, there exists $A \in \mathscr{A}$ such that $F(A) \cong B$.

**Proposition 1.3.18** *A functor is an equivalence if and only if it is full, faithful and essentially surjective on objects.*

**Proof** Exercise 1.3.32. $\square$

This result can be compared to the theorem that every bijective group homomorphism is an isomorphism (that is, its inverse is also a homomorphism), or that a natural transformation whose components are isomorphisms is itself an isomorphism (Lemma 1.3.11). Those two results are useful because they allow us to show that a map is an isomorphism without directly constructing an inverse. Proposition 1.3.18 provides a similar service, enabling us to prove that a functor $F$ is an equivalence without actually constructing an ‘inverse’ $G$, or indeed an $\eta$ or an $\varepsilon$ (in the notation of Definition 1.3.15).

A corollary of Proposition 1.3.18 invites us to view full and faithful functors as, essentially, inclusions of full subcategories:

<span class="original-page-anchor" id="pdf-page-44" aria-hidden="true"></span>

**Corollary 1.3.19** *Let $F\colon \mathscr{C} \to \mathscr{D}$ be a full and faithful functor. Then $\mathscr{C}$ is equivalent to the full subcategory $\mathscr{C}'$ of $\mathscr{D}$ whose objects are those of the form $F(C)$ for some $C \in \mathscr{C}$.*

**Proof** The functor $F'\colon \mathscr{C} \to \mathscr{C}'$ defined by $F'(C) = F(C)$ is full and faithful (since $F$ is) and essentially surjective on objects (by definition of $\mathscr{C}'$). $\square$

This result is true, with the same proof, whether we interpret ‘of the form $F(C)$’ to mean ‘equal to $F(C)$’ or ‘isomorphic to $F(C)$’.

**Example 1.3.20** Let $\mathscr{A}$ be any category, and let $\mathscr{B}$ be any full subcategory containing at least one object from each isomorphism class of $\mathscr{A}$. Then the inclusion functor $\mathscr{B} \hookrightarrow \mathscr{A}$ is faithful (like any inclusion of subcategories), full, and essentially surjective on objects. Hence $\mathscr{B} \simeq \mathscr{A}$.

So if we take a category and remove some (but not all) of the objects in each isomorphism class, the slimmed-down version is equivalent to the original. Conversely, if we take a category and throw in some more objects, each of them isomorphic to one of the existing objects, it makes no difference: the new, bigger, category is equivalent to the old one.

For example, let $\mathbf{FinSet}$ be the category of finite sets and functions between them. For each natural number $n$, choose a set $\mathbf{n}$ with $n$ elements, and let $\mathscr{B}$ be the full subcategory of $\mathbf{FinSet}$ with objects $\mathbf{0},\mathbf{1},\ldots$. Then $\mathscr{B} \simeq \mathbf{FinSet}$, even though $\mathscr{B}$ is in some sense much smaller than $\mathbf{FinSet}$.

**Example 1.3.21** In Example 1.1.8(d), we saw that monoids are essentially the same thing as one-object categories. With the definition of equivalence in hand, we are nearly ready to make this statement precise. We are missing some set-theoretic language, and we will return to this result once we have that language (Example 3.2.11), but the essential point can be stated now.

Let $\mathscr{C}$ be the full subcategory of $\mathbf{CAT}$ whose objects are the one-object categories. Let $\mathbf{Mon}$ be the category of monoids. Then $\mathscr{C} \simeq \mathbf{Mon}$. To see this, first note that given any object $A$ of any category, the maps $A \to A$ form a monoid under composition (at least, subject to some set-theoretic restrictions). There is, therefore, a canonical functor $F\colon \mathscr{C} \to \mathbf{Mon}$ sending a one-object category to the monoid of maps from the single object to itself. This functor $F$ is full and faithful (by Example 1.2.7) and essentially surjective on objects. Hence $F$ is an equivalence.

**Example 1.3.22** An equivalence of the form $\mathscr{A}^{\mathrm{op}} \simeq \mathscr{B}$ is sometimes called a **duality** between $\mathscr{A}$ and $\mathscr{B}$. One says that $\mathscr{A}$ is **dual** to $\mathscr{B}$. There are many famous dualities in which $\mathscr{A}$ is a category of algebras and $\mathscr{B}$ is a category of spaces; recall the slogan ‘algebra is dual to geometry’ from Example 1.2.11.

<span class="original-page-anchor" id="pdf-page-45" aria-hidden="true"></span>

Here are some quite advanced examples, well beyond the scope of this book.

- Stone duality: the category of Boolean algebras is dual to the category of totally disconnected compact Hausdorff spaces.
- Gelfand–Naimark duality: the category of commutative unital $C^*$-algebras is dual to the category of compact Hausdorff spaces. ($C^*$-algebras are certain algebraic structures important in functional analysis.)
- Algebraic geometers have several notions of ‘space’, one of which is ‘affine variety’. Let $k$ be an algebraically closed field. Then the category of affine varieties over $k$ is dual to the category of finitely generated $k$-algebras with no nontrivial nilpotents.
- Pontryagin duality: the category of locally compact abelian topological groups is dual to itself. As the words ‘topological group’ suggest, both sides of the duality are algebraic *and* geometric. Pontryagin duality is an abstraction of the properties of the Fourier transform.

**Example 1.3.23** It is rarely useful to consider a category of structured objects in which the maps do not respect that structure. For instance, let $\mathscr{A}$ be the category whose objects are groups and whose maps are *all* functions between them, not necessarily homomorphisms. Let $\mathbf{Set}_{\neq\emptyset}$ be the category of nonempty sets. The forgetful functor $U\colon \mathscr{A} \to \mathbf{Set}_{\neq\emptyset}$ is full and faithful. It is a (not profound) fact that every nonempty set can be given at least one group structure, so $U$ is essentially surjective on objects. Hence $U$ is an equivalence. This implies that the category $\mathscr{A}$, although defined in terms of groups, is really just the category of nonempty sets.

**Remarks 1.3.24** Here is a kind of review of the chapter so far. We have defined:

- categories (Section 1.1);
- functors between categories (Section 1.2);
- natural transformations between functors (Section 1.3);
- composition of functors

  $$
  \cdot \to \cdot \to \cdot
  $$

  and the identity functor on any category (Remark 1.2.2(b));
- composition of natural transformations

  ![Vertical composition of natural transformations.](/library/volume-87/diagrams/pdf-0045-vertical-composition.png)

  and the identity natural transformation on any functor (Construction 1.3.6).

<span class="original-page-anchor" id="pdf-page-46" aria-hidden="true"></span>

This composition of natural transformations is sometimes called **vertical composition**. There is also **horizontal composition**, which takes natural transformations

![Natural transformations alpha and alpha-prime between pairs of functors.](/library/volume-87/diagrams/pdf-0046-horizontal-input.png)

and produces a natural transformation

![The resulting natural transformation between the composite functors.](/library/volume-87/diagrams/pdf-0046-horizontal-output.png)

traditionally written as $\alpha' * \alpha$. The component of $\alpha' * \alpha$ at $A \in \mathscr{A}$ is defined to be the diagonal of the naturality square

![The naturality square defining horizontal composition.](/library/volume-87/diagrams/pdf-0046-naturality-square.png)

In other words, $(\alpha' * \alpha)_A$ can be defined as either $\alpha'_{G(A)} \circ F'(\alpha_A)$ or $G'(\alpha_A) \circ \alpha'_{F(A)}$; it makes no difference which, since they are equal.

The special cases of horizontal composition where either $\alpha$ or $\alpha'$ is an identity are especially important, and have their own notation. Thus,

![A functor followed by a natural transformation.](/library/volume-87/diagrams/pdf-0046-whisker-right-input.png)

gives rise to

![The natural transformation alpha-prime F between composite functors.](/library/volume-87/diagrams/pdf-0046-whisker-right-output.png)

where $(\alpha' F)_A = \alpha'_{F(A)}$, and

![A natural transformation followed by a functor.](/library/volume-87/diagrams/pdf-0046-whisker-left-input.png)

gives rise to

![The natural transformation F-prime alpha between composite functors.](/library/volume-87/diagrams/pdf-0046-whisker-left-output.png)

where $(F'\alpha)_A = F'(\alpha_A)$.

<span class="original-page-anchor" id="pdf-page-47" aria-hidden="true"></span>

Vertical and horizontal composition interact well: natural transformations

![The natural transformations entering the interchange law.](/library/volume-87/diagrams/pdf-0047-interchange.png)

obey the **interchange law**,

$$
(\beta' \circ \alpha') * (\beta \circ \alpha) = (\beta' * \beta) \circ (\alpha' * \alpha)\colon F' \circ F \to H' \circ H.
$$

As usual, a statement on composition is accompanied by a statement on identities: $1_{F'} * 1_F = 1_{F' \circ F}$ too.

All of this enables us to construct, for any categories $\mathscr{A}$, $\mathscr{A}'$ and $\mathscr{A}''$, a functor

$$
[\mathscr{A}',\mathscr{A}''] \times [\mathscr{A},\mathscr{A}'] \to [\mathscr{A},\mathscr{A}''],
$$

given on objects by $(F',F) \mapsto F' \circ F$ and on maps by $(\alpha',\alpha) \mapsto \alpha' * \alpha$. In particular, if $F' \cong G'$ and $F \cong G$ then $F' \circ F \cong G' \circ G$, since functors preserve isomorphism (Exercise 1.2.21).

(The existence of this functor is similar to the fact that *inside* a category $\mathscr{C}$, we have, for any objects $A$, $A'$ and $A''$, a funct*ion*

$$
\mathscr{C}(A',A'') \times \mathscr{C}(A,A') \to \mathscr{C}(A,A''),
$$

given by $(f',f) \mapsto f' \circ f$.)

The diagrams above contain not only objects (0-dimensional) and arrows $\to$ (1-dimensional), but also double arrows $\Rightarrow$ sweeping out 2-dimensional regions between arrows. What we are implicitly doing is called 2-category theory. There is a 2-category of categories, functors and natural transformations, whose anatomy we have just been describing. If we are really serious about categories, we have to get serious about 2-categories. And if we are really serious about 2-categories, we have to get serious about 3-categories… and before we know it, we are studying $\infty$-categories. But in this book, we climb no higher than the first rung or two of this infinite ladder.

### Exercises

**1.3.25** Find three examples of natural transformations not mentioned above.

**1.3.26** Prove Lemma 1.3.11.

<span class="original-page-anchor" id="pdf-page-48" aria-hidden="true"></span>

**1.3.27** Let $\mathscr{A}$ and $\mathscr{B}$ be categories. Prove that $[\mathscr{A}^{\mathrm{op}},\mathscr{B}^{\mathrm{op}}] \cong [\mathscr{A},\mathscr{B}]^{\mathrm{op}}$.

**1.3.28** Let $A$ and $B$ be sets, and denote by $B^A$ the set of functions from $A$ to $B$. Write down:

(a) a canonical function $A \times B^A \to B$;

(b) a canonical function $A \to B^{(B^A)}$.

(Although in principle there could be many such canonical functions, in both these cases there is only one.)

**1.3.29** Here we consider natural transformations between functors whose domain is a product category $\mathscr{A} \times \mathscr{B}$. Your task is to show that naturality in two variables simultaneously is equivalent to naturality in each variable separately.

Take functors $F,G\colon \mathscr{A} \times \mathscr{B} \to \mathscr{C}$. For each $A \in \mathscr{A}$, there are functors $F^A,G^A\colon \mathscr{B} \to \mathscr{C}$, as in Exercise 1.2.25. Similarly, for each $B \in \mathscr{B}$, there are functors $F_B,G_B\colon \mathscr{A} \to \mathscr{C}$.

Let $\bigl(\alpha_{A,B}\colon F(A,B) \to G(A,B)\bigr)_{A\in\mathscr{A},B\in\mathscr{B}}$ be a family of maps. Show that this family is a natural transformation $F \to G$ if and only if it satisfies the following two conditions:

- for each $A \in \mathscr{A}$, the family $\bigl(\alpha_{A,B}\colon F^A(B) \to G^A(B)\bigr)_{B\in\mathscr{B}}$ is a natural transformation $F^A \to G^A$;
- for each $B \in \mathscr{B}$, the family $\bigl(\alpha_{A,B}\colon F_B(A) \to G_B(A)\bigr)_{A\in\mathscr{A}}$ is a natural transformation $F_B \to G_B$.

**1.3.30** Let $G$ be a group. For each $g \in G$, there is a unique homomorphism $\phi\colon \mathbb{Z} \to G$ satisfying $\phi(1) = g$. Thus, elements of $G$ are essentially the same thing as homomorphisms $\mathbb{Z} \to G$. When groups are regarded as one-object categories, homomorphisms $\mathbb{Z} \to G$ are in turn the same as functors $\mathbb{Z} \to G$. Natural isomorphism defines an equivalence relation on the set of functors $\mathbb{Z} \to G$, and, therefore, an equivalence relation on $G$ itself. What is this equivalence relation, in purely group-theoretic terms?

(First have a guess. For a general group $G$, what equivalence relations on $G$ can you think of?)

**1.3.31** A **permutation** of a set $X$ is a bijection $X \to X$. Write $\mathbf{Sym}(X)$ for the set of permutations of $X$. A **total order** on a set $X$ is an order $\leq$ such that for all $x,y \in X$, either $x \leq y$ or $y \leq x$; so a total order on a finite set amounts to a way of placing its elements in sequence. Write $\mathbf{Ord}(X)$ for the set of total orders on $X$.

Let $\mathscr{B}$ denote the category of finite sets and bijections.

<span class="original-page-anchor" id="pdf-page-49" aria-hidden="true"></span>

(a) Give a definition of $\mathbf{Sym}$ on maps in $\mathscr{B}$ in such a way that $\mathbf{Sym}$ becomes a functor $\mathscr{B} \to \mathbf{Set}$. Do the same for $\mathbf{Ord}$. Both your definitions should be canonical (no arbitrary choices).

(b) Show that there is no natural transformation $\mathbf{Sym} \to \mathbf{Ord}$. (Hint: consider identity permutations.)

(c) For an $n$-element set $X$, how many elements do the sets $\mathbf{Sym}(X)$ and $\mathbf{Ord}(X)$ have?

Conclude that $\mathbf{Sym}(X) \cong \mathbf{Ord}(X)$ for all $X \in \mathscr{B}$, but not *naturally* in $X \in \mathscr{B}$. (The moral is that for each finite set $X$, there are exactly as many permutations of $X$ as there are total orders on $X$, but there is no natural way of matching them up.)

**1.3.32** In this exercise, you will prove Proposition 1.3.18. Let $F\colon \mathscr{A} \to \mathscr{B}$ be a functor.

(a) Suppose that $F$ is an equivalence. Prove that $F$ is full, faithful and essentially surjective on objects. (Hint: prove faithfulness before fullness.)

(b) Now suppose instead that $F$ is full, faithful and essentially surjective on objects. For each $B \in \mathscr{B}$, choose an object $G(B)$ of $\mathscr{A}$ and an isomorphism $\varepsilon_B\colon F(G(B)) \to B$. Prove that $G$ extends to a functor in such a way that $(\varepsilon_B)_{B\in\mathscr{B}}$ is a natural isomorphism $FG \to 1_{\mathscr{B}}$. Then construct a natural isomorphism $1_{\mathscr{A}} \to GF$, thus proving that $F$ is an equivalence.

**1.3.33** This exercise makes precise the idea that linear algebra can equivalently be done with matrices or with linear maps.

Fix a field $k$. Let $\mathbf{Mat}$ be the category whose objects are the natural numbers and with

$$
\mathbf{Mat}(m,n) = \{n \times m\text{ matrices over }k\}.
$$

Prove that $\mathbf{Mat}$ is equivalent to $\mathbf{FDVect}$, the category of finite-dimensional vector spaces over $k$. Does your equivalence involve a *canonical* functor from $\mathbf{Mat}$ to $\mathbf{FDVect}$, or from $\mathbf{FDVect}$ to $\mathbf{Mat}$?

(Part of the exercise is to work out what composition in the category $\mathbf{Mat}$ is supposed to be; there is only one sensible possibility. Proposition 1.3.18 makes the exercise easier.)

**1.3.34** Show that equivalence of categories is an equivalence relation. (Not as obvious as it looks.)
