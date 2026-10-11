---
title: "Adjoints"
description: "Tom Leinster《Basic Category Theory》English。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"Categories, functors and natural transformations","link":"/library/volume-87/original-chapter-001"}
next: {"text":"Interlude on sets","link":"/library/volume-87/original-chapter-003"}
---

# Adjoints

<span class="original-page-anchor" id="pdf-page-50" aria-hidden="true"></span>

The slogan of Saunders Mac Lane’s book *Categories for the Working Mathematician* is:

> *Adjoint functors arise everywhere.*

We will see the truth of this, meeting examples of adjoint functors from diverse parts of mathematics. To complement the understanding provided by examples, we will approach the theory of adjoints from three different directions, each of which carries its own intuition. Then we will prove that the three approaches are equivalent.

Understanding adjointness gives you a valuable addition to your mathematical toolkit. Most professional pure mathematicians know what categories and functors are, but far fewer know about adjoints. More should: adjoint functors are both common and easy, and knowing about adjoints helps you to spot patterns in the mathematical landscape.

## 2.1 Definition and examples

Consider a pair of functors in opposite directions, $F\colon\mathscr{A}\to\mathscr{B}$ and $G\colon\mathscr{B}\to\mathscr{A}$. Roughly speaking, $F$ is said to be left adjoint to $G$ if, whenever $A\in\mathscr{A}$ and $B\in\mathscr{B}$, maps $F(A)\to B$ are essentially the same thing as maps $A\to G(B)$.

**Definition 2.1.1** Let ![Categories and opposing functors F and G](/library/volume-87/diagrams/pdf-0050-functor-pair.png) be categories and functors. We say that $F$ is **left adjoint** to $G$, and $G$ is **right adjoint** to $F$, and write $F\dashv G$, if

$$
\mathscr{B}(F(A),B)\cong\mathscr{A}(A,G(B))\tag{2.1}
$$

naturally in $A\in\mathscr{A}$ and $B\in\mathscr{B}$. The meaning of ‘naturally’ is defined below. An **adjunction** between $F$ and $G$ is a choice of natural isomorphism (2.1).

<span class="original-page-anchor" id="pdf-page-51" aria-hidden="true"></span>

‘Naturally in $A\in\mathscr{A}$ and $B\in\mathscr{B}$’ means that there is a specified bijection (2.1) for each $A\in\mathscr{A}$ and $B\in\mathscr{B}$, and that it satisfies a naturality axiom. To state it, we need some notation. Given objects $A\in\mathscr{A}$ and $B\in\mathscr{B}$, the correspondence (2.1) between maps $F(A)\to B$ and $A\to G(B)$ is denoted by a horizontal bar, in both directions:

![The two directions of the transpose correspondence](/library/volume-87/diagrams/pdf-0051-transpose-correspondence.png)

So $\bar{\bar{f}}=f$ and $\bar{\bar{g}}=g$. We call $\bar{f}$ the **transpose** of $f$, and similarly for $g$. The naturality axiom has two parts:

$$
\overline{\Bigl(F(A)\xrightarrow{g} B\xrightarrow{q} B'\Bigr)}
\quad=\quad
\Bigl(A\xrightarrow{\bar{g}}G(B)\xrightarrow{G(q)}G(B')\Bigr)\tag{2.2}
$$

(that is, $\overline{q\circ g}=G(q)\circ\bar{g}$) for all $g$ and $q$, and

$$
\overline{\Bigl(A'\xrightarrow{p} A\xrightarrow{f} G(B)\Bigr)}
\quad=\quad
\Bigl(F(A')\xrightarrow{F(p)} F(A)\xrightarrow{\bar{f}} B\Bigr)\tag{2.3}
$$

for all $p$ and $f$. It makes no difference whether we put the long bar over the left or the right of these equations, since bar is self-inverse.

**Remarks 2.1.2** (a) The naturality axiom might seem ad hoc, but we will see in Chapter 4 that it simply says that two particular functors are naturally isomorphic. In this section, we ignore the naturality axiom altogether, trusting that it embodies our usual intuitive idea of naturality: something defined without making any arbitrary choices.

(b) The naturality axiom implies that from each array of maps

$$
A_0\to\cdots\to A_n,\qquad F(A_n)\to B_0,\qquad B_0\to\cdots\to B_m,
$$

it is possible to construct exactly one map

$$
A_0\to G(B_m).
$$

Compare the comments on the definitions of category, functor and natural transformation (Remarks 1.1.2(b), 1.2.2(a), and 1.3.2(a)).

(c) Not only do adjoint functors arise everywhere; better, whenever you see a pair of functors $\mathscr{A}\rightleftarrows\mathscr{B}$, there is an excellent chance that they are adjoint (one way round or the other).

For example, suppose you get talking to a mathematician who tells you that her work involves Lie algebras and associative algebras. You try to object that you don’t know what either of those things is, but she carries on talking anyway, explaining that there’s a way of turning any Lie algebra into an associative algebra, and also a way of turning any associative <span class="original-page-anchor" id="pdf-page-52" aria-hidden="true"></span>algebra into a Lie algebra. At this point, even without knowing what she’s talking about, you should bet her that one process is adjoint to the other. This almost always works.

(d) A given functor $G$ may or may not have a left adjoint, but if it does, it is unique up to isomorphism, so we may speak of ‘*the* left adjoint of $G$’. The same goes for right adjoints. We prove this later (Example 4.3.13).

You might ask ‘what do we gain from knowing that two functors are adjoint?’ The uniqueness is a crucial part of the answer. Let us return to the example of (c). It would take you only a few minutes to learn what Lie algebras are, what associative algebras are, and what the standard functor $G$ is that turns an associative algebra into a Lie algebra. What about the functor $F$ in the opposite direction? The description of $F$ that you will find in most algebra books (under ‘universal enveloping algebra’) takes much longer to understand. However, you can bypass that process completely, just by knowing that $F$ is the left adjoint of $G$. Since $G$ can have only *one* left adjoint, this characterizes $F$ completely. In a sense, it tells you all you need to know.

**Examples 2.1.3 (Algebra: free $\dashv$ forgetful)** Forgetful functors between categories of algebraic structures usually have left adjoints. For instance:

(a) Let $k$ be a field. There is an adjunction

![Free vector space and forgetful adjunction](/library/volume-87/diagrams/pdf-0052-free-vector-space.png)

where $U$ is the forgetful functor of Example 1.2.3(b) and $F$ is the free functor of Example 1.2.4(c). Adjointness says that given a set $S$ and a vector space $V$, a linear map $F(S)\to V$ is essentially the same thing as a function $S\to U(V)$.

We saw this in Example 0.4, but let us now check it in detail.

Fix a set $S$ and a vector space $V$. Given a linear map $g\colon F(S)\to V$, we may define a map of sets $\bar{g}\colon S\to U(V)$ by $\bar{g}(s)=g(s)$ for all $s\in S$. This gives a function

$$
\begin{array}{ccc}
\mathbf{Vect}_k(F(S),V)&\to&\mathbf{Set}(S,U(V))\\
g&\mapsto&\bar{g}.
\end{array}
$$

In the other direction, given a map of sets $f\colon S\to U(V)$, we may define a linear map $\bar{f}\colon F(S)\to V$ by $\bar{f}\bigl(\sum_{s\in S}\lambda_s s\bigr)=\sum_{s\in S}\lambda_s f(s)$ for all formal <span class="original-page-anchor" id="pdf-page-53" aria-hidden="true"></span>linear combinations $\sum\lambda_s s\in F(S)$. This gives a function

$$
\begin{array}{ccc}
\mathbf{Set}(S,U(V))&\to&\mathbf{Vect}_k(F(S),V)\\
f&\mapsto&\bar{f}.
\end{array}
$$

These two functions ‘bar’ are mutually inverse: for any linear map $g\colon F(S)\to V$, we have

$$
\bar{\bar{g}}\Biggl(\sum_{s\in S}\lambda_s s\Biggr)
=\sum_{s\in S}\lambda_s\bar{g}(s)
=\sum_{s\in S}\lambda_s g(s)
=g\Biggl(\sum_{s\in S}\lambda_s s\Biggr)
$$

for all $\sum\lambda_s s\in F(S)$, so $\bar{\bar{g}}=g$, and for any map of sets $f\colon S\to U(V)$, we have

$$
\bar{\bar{f}}(s)=\bar{f}(s)=f(s)
$$

for all $s\in S$, so $\bar{\bar{f}}=f$. We therefore have a canonical bijection between $\mathbf{Vect}_k(F(S),V)$ and $\mathbf{Set}(S,U(V))$ for each $S\in\mathbf{Set}$ and $V\in\mathbf{Vect}_k$, as required.

Here we have been careful to distinguish between the vector space $V$ and its underlying set $U(V)$. Very often, though, in category theory as in mathematics at large, the symbol for a forgetful functor is omitted. In this example, that would mean dropping the $U$ and leaving the reader to figure out whether each occurrence of $V$ is intended to denote the vector space itself or its underlying set. We will soon start using such notational shortcuts ourselves.

(b) In the same way, there is an adjunction

![Free group and forgetful adjunction](/library/volume-87/diagrams/pdf-0053-free-group.png)

where $F$ and $U$ are the free and forgetful functors of Examples 1.2.3(a) and 1.2.4(a).

The free group functor is tricky to construct explicitly. In Chapter 6, we will prove a result (the general adjoint functor theorem) guaranteeing that $U$ and many functors like it all have left adjoints. To some extent, this removes the need to construct $F$ explicitly, as observed in Remark 2.1.2(d). The point can be overstated: for a group theorist, the more descriptions of free groups that are available, the better. Explicit constructions really can be useful. But it is an important general principle that forgetful functors of this type always have left adjoints.

<span class="original-page-anchor" id="pdf-page-54" aria-hidden="true"></span>

(c) There is an adjunction

![Abelianization and inclusion adjunction](/library/volume-87/diagrams/pdf-0054-abelianization-adjunction.png)

where $U$ is the inclusion functor of Example 1.2.3(d). If $G$ is a group then $F(G)$ is the **abelianization** $G_{\mathrm{ab}}$ of $G$. This is an abelian quotient group of $G$, with the property that every map from $G$ to an abelian group factorizes uniquely through $G_{\mathrm{ab}}$:

![Universal property of the abelianization](/library/volume-87/diagrams/pdf-0054-abelianization-universal.png)

Here $\eta$ is the natural map from $G$ to its quotient $G_{\mathrm{ab}}$, and $A$ is any abelian group. (We have adopted the abuse of notation advertised in example (a), omitting the symbol $U$ at several places in this diagram.) The bijection

$$
\mathbf{Ab}(G_{\mathrm{ab}},A)\cong\mathbf{Grp}(G,U(A))
$$

is given in the left-to-right direction by $\psi\mapsto\psi\circ\eta$, and in the right-to-left direction by $\phi\mapsto\bar{\phi}$.

(To construct $G_{\mathrm{ab}}$, let $G'$ be the smallest normal subgroup of $G$ containing $xyx^{-1}y^{-1}$ for all $x,y\in G$, and put $G_{\mathrm{ab}}=G/G'$. The kernel of any homomorphism from $G$ to an abelian group contains $G'$, and the universal property follows.)

(d) There are adjunctions

![Left and right adjoints to the inclusion of groups into monoids](/library/volume-87/diagrams/pdf-0054-group-monoid-adjunctions.png)

between the categories of groups and monoids. The middle functor $U$ is inclusion. The left adjoint $F$ is, again, tricky to describe explicitly. Informally, $F(M)$ is obtained from $M$ by throwing in an inverse to every element. (For example, if $M$ is the additive monoid of natural numbers then $F(M)$ is the group of integers.) Again, the general adjoint functor theorem (Theorem 6.3.10) guarantees the existence of this adjoint.

This example is unusual in that forgetful functors do not usually have *right* adjoints. Here, given a monoid $M$, the group $R(M)$ is the submonoid of $M$ consisting of all the invertible elements.

<span class="original-page-anchor" id="pdf-page-55" aria-hidden="true"></span>

The category $\mathbf{Grp}$ is both a **reflective** and a **coreflective** subcategory of $\mathbf{Mon}$. This means, by definition, that the inclusion functor $\mathbf{Grp}\hookrightarrow\mathbf{Mon}$ has both a left and a right adjoint. The previous example tells us that $\mathbf{Ab}$ is a reflective subcategory of $\mathbf{Grp}$.

(e) Let $\mathbf{Field}$ be the category of fields, with ring homomorphisms as the maps. The forgetful functor $\mathbf{Field}\to\mathbf{Set}$ does *not* have a left adjoint. (For a proof, see Example 6.3.5.) The theory of fields is unlike the theories of groups, rings, and so on, because the operation $x\mapsto x^{-1}$ is not defined for *all* $x$ (only for $x\ne0$).

**Remark 2.1.4** At several points in this book, we make contact with the idea of an **algebraic theory**. You already know several examples: the theory of groups is an algebraic theory, as are the theory of rings, the theory of vector spaces over $\mathbb{R}$, the theory of vector spaces over $\mathbb{C}$, the theory of monoids, and (rather trivially) the theory of sets. After reading the description below, you might conclude that the word ‘theory’ is overly grand, and that ‘definition’ would be more appropriate. Nevertheless, this is the established usage.

We will not need to define ‘algebraic theory’ formally, but it will be important to have the general idea. Let us begin by considering the theory of groups.

A group can be defined as a set $X$ equipped with a function $\cdot\colon X\times X\to X$ (multiplication), another function $(\ )^{-1}\colon X\to X$ (inverse), and an element $e\in X$ (the identity), satisfying a familiar list of equations. More systematically, the three pieces of structure on $X$ can be seen as maps of sets

$$
\cdot\colon X^2\to X,\qquad
(\ )^{-1}\colon X^1\to X,\qquad
e\colon X^0\to X,
$$

where in the last case, $X^0$ is the one-element set $1$ and we are using the observation that a map $1\to X$ of sets is essentially the same thing as an element of $X$.

(You may be more familiar with a definition of group in which only the multiplication and perhaps the identity are specified as pieces of *structure*, with the existence of inverses required as a *property*. In that approach, the definition is swiftly followed by a lemma on uniqueness of inverses, guaranteeing that it makes sense to speak of *the* inverse of an element. The two approaches are equivalent, but for many purposes, it is better to frame the definition in the way described in the previous paragraph.)

An algebraic theory consists of two things: first, a collection of operations, each with a specified arity (number of inputs), and second, a collection of equations. For example, the theory of groups has one operation of arity $2$, one of arity $1$, and one of arity $0$. An **algebra** or **model** for an algebraic theory consists of a set $X$ together with a specified map $X^n\to X$ for each operation of <span class="original-page-anchor" id="pdf-page-56" aria-hidden="true"></span>arity $n$, such that the equations hold everywhere. For example, an algebra for the theory of groups is exactly a group.

A more subtle example is the theory of vector spaces over $\mathbb{R}$. This is an algebraic theory with, among other things, an infinite number of operations of arity $1$: for each $\lambda\in\mathbb{R}$, we have the operation $\lambda\cdot-\colon X\to X$ of scalar multiplication by $\lambda$ (for any vector space $X$). There is nothing special about the field $\mathbb{R}$ here; the only point is that it was chosen in advance. The theory of vector spaces over $\mathbb{R}$ is different from the theory of vector spaces over $\mathbb{C}$, because they have different operations of arity $1$.

In a nutshell, the main property of algebras for an algebraic theory is that the operations are defined everywhere on the set, and the equations hold everywhere too. For example, *every* element of a group has a specified inverse, and *every* element $x$ satisfies the equation $x\cdot x^{-1}=1$. This is why the theories of groups, rings, and so on, are algebraic theories, but the theory of fields is not.

**Example 2.1.5** There are adjunctions

![Discrete and indiscrete topology adjunctions](/library/volume-87/diagrams/pdf-0056-topology-adjunctions.png)

where $U$ sends a space to its set of points, $D$ equips a set with the discrete topology, and $I$ equips a set with the indiscrete topology.

**Example 2.1.6** Given sets $A$ and $B$, we can form their (cartesian) product $A\times B$. We can also form the set $B^A$ of functions from $A$ to $B$. This is the same as the set $\mathbf{Set}(A,B)$, but we tend to use the notation $B^A$ when we want to emphasize that it is an object of the same category as $A$ and $B$.

Now fix a set $B$. Taking the product with $B$ defines a functor

$$
\begin{array}{cccc}
-\times B\colon&\mathbf{Set}&\to&\mathbf{Set}\\
&A&\mapsto&A\times B.
\end{array}
$$

(Here we are using the blank notation introduced in Example 1.2.12.) There is also a functor

$$
\begin{array}{cccc}
(-)^B\colon&\mathbf{Set}&\to&\mathbf{Set}\\
&C&\mapsto&C^B.
\end{array}
$$

Moreover, there is a canonical bijection

$$
\mathbf{Set}(A\times B,C)\cong\mathbf{Set}(A,C^B)
$$

for any sets $A$ and $C$. It is defined by simply changing the punctuation: given a

<span class="original-page-anchor" id="pdf-page-57" aria-hidden="true"></span>

![A surface sliced into a family of functions](/library/volume-87/diagrams/pdf-0057-figure-2-1.png)

*Figure 2.1* In $\mathbf{Set}$, a map $A\times B\to C$ can be seen as a way of assigning to each element of $A$ a map $B\to C$.

map $g\colon A\times B\to C$, define $\bar{g}\colon A\to C^B$ by

$$
(\bar{g}(a))(b)=g(a,b)
$$

($a\in A$, $b\in B$), and in the other direction, given $f\colon A\to C^B$, define $\bar{f}\colon A\times B\to C$ by

$$
\bar{f}(a,b)=(f(a))(b)
$$

($a\in A$, $b\in B$). Figure 2.1 shows an example with $A=B=C=\mathbb{R}$. By slicing up the surface as shown, a map $\mathbb{R}^2\to\mathbb{R}$ can be seen as a map from $\mathbb{R}$ to $\{\text{maps }\mathbb{R}\to\mathbb{R}\}$.

Putting all this together, we obtain an adjunction

![Product and exponential adjunction](/library/volume-87/diagrams/pdf-0057-product-exponential-adjunction.png)

for every set $B$.

**Definition 2.1.7** Let $\mathscr{A}$ be a category. An object $I\in\mathscr{A}$ is **initial** if for every $A\in\mathscr{A}$, there is exactly one map $I\to A$. An object $T\in\mathscr{A}$ is **terminal** if for every $A\in\mathscr{A}$, there is exactly one map $A\to T$.

For example, the empty set is initial in $\mathbf{Set}$, the trivial group is initial in $\mathbf{Grp}$, and $\mathbb{Z}$ is initial in $\mathbf{Ring}$ (Example 0.2). The one-element set is terminal in $\mathbf{Set}$, the trivial group is terminal (as well as initial) in $\mathbf{Grp}$, and the trivial (one-element) ring is terminal in $\mathbf{Ring}$. The terminal object of $\mathbf{CAT}$ is the category $\mathbf{1}$ containing just one object and one map (necessarily the identity on that object).

A category need not have an initial object, but if it does have one, it is unique up to isomorphism. Indeed, it is unique up to *unique* isomorphism, as follows.

<span class="original-page-anchor" id="pdf-page-58" aria-hidden="true"></span>

**Lemma 2.1.8** Let $I$ and $I'$ be initial objects of a category. Then there is a unique isomorphism $I \to I'$. In particular, $I \cong I'$.

**Proof** Since $I$ is initial, there is a unique map $f: I \to I'$. Since $I'$ is initial, there is a unique map $f': I' \to I$. Now $f' \circ f$ and $1_I$ are both maps $I \to I$, and $I$ is initial, so $f' \circ f = 1_I$. Similarly, $f \circ f' = 1_{I'}$. Hence $f$ is an isomorphism, as required. $\square$

**Example 2.1.9** Initial and terminal objects can be described as adjoints. Let $\mathscr{A}$ be a category. There is precisely one functor $\mathscr{A} \to \mathbf{1}$. Also, a functor $\mathbf{1} \to \mathscr{A}$ is essentially just an object of $\mathscr{A}$ (namely, the object to which the unique object of $\mathbf{1}$ is mapped). Viewing functors $\mathbf{1} \to \mathscr{A}$ as objects of $\mathscr{A}$, a left adjoint to $\mathscr{A} \to \mathbf{1}$ is exactly an initial object of $\mathscr{A}$.

Similarly, a right adjoint to the unique functor $\mathscr{A} \to \mathbf{1}$ is exactly a terminal object of $\mathscr{A}$.

**Remark 2.1.10** In the language introduced in Remark 1.1.10, the concept of terminal object is dual to the concept of initial object. (More generally, the concepts of left and right adjoint are dual to one another.) Since any two initial objects of a category are uniquely isomorphic, the principle of duality implies that the same is true of terminal objects.

**Remark 2.1.11** Adjunctions can be composed. Take adjunctions

![Two composable adjunctions](/library/volume-87/diagrams/pdf-0058-composed-adjunctions.png)

where the $\perp$ symbol is a rotated $\dashv$ (thus, $F \dashv G$ and $F' \dashv G'$). Then we obtain an adjunction

![The composite adjunction](/library/volume-87/diagrams/pdf-0058-composite-adjunction.png)

since for $A \in \mathscr{A}$ and $A'' \in \mathscr{A}''$,

$$
\mathscr{A}''\bigl(F'(F(A)), A''\bigr) \cong \mathscr{A}'\bigl(F(A), G'(A'')\bigr) \cong \mathscr{A}\bigl(A, G(G'(A''))\bigr)
$$

naturally in $A$ and $A''$.

### Exercises

**2.1.12** Find three examples of adjoint functors not mentioned above. Do the same for initial and terminal objects.

**2.1.13** What can be said about adjunctions between discrete categories?

<span class="original-page-anchor" id="pdf-page-59" aria-hidden="true"></span>

**2.1.14** Show that the naturality equations (2.2) and (2.3) can equivalently be replaced by the single equation

$$
\overline{\Bigl(A' \xrightarrow{p} A \xrightarrow{f} G(B) \xrightarrow{G(q)} G(B')\Bigr)}
= \Bigl(F(A') \xrightarrow{F(p)} F(A) \xrightarrow{\bar{f}} B \xrightarrow{q} B'\Bigr)
$$

for all $p$, $f$ and $q$.

**2.1.15** Show that left adjoints preserve initial objects: that is, if

![An adjunction](/library/volume-87/diagrams/pdf-0059-adjunction.png)

and $I$ is an initial object of $\mathscr{A}$, then $F(I)$ is an initial object of $\mathscr{B}$. Dually, show that right adjoints preserve terminal objects.

(In Section 6.3, we will see this as part of a bigger picture: right adjoints preserve limits and left adjoints preserve colimits.)

**2.1.16** Let $G$ be a group.

(a) What interesting functors are there (in either direction) between $\mathbf{Set}$ and the category $[G, \mathbf{Set}]$ of left $G$-sets? Which of those functors are adjoint to which?

(b) Similarly, what interesting functors are there between $\mathbf{Vect}_k$ and the category $[G, \mathbf{Vect}_k]$ of $k$-linear representations of $G$, and what adjunctions are there between those functors?

**2.1.17** Fix a topological space $X$, and write $\mathscr{O}(X)$ for the poset of open subsets of $X$, ordered by inclusion. Let

$$
\Delta: \mathbf{Set} \to [\mathscr{O}(X)^{\mathrm{op}}, \mathbf{Set}]
$$

be the functor assigning to a set $A$ the presheaf $\Delta A$ with constant value $A$. Exhibit a chain of adjoint functors

$$
\Lambda \dashv \Pi \dashv \Delta \dashv \Gamma \dashv \nabla.
$$

## 2.2 Adjunctions via units and counits

In the previous section, we met the definition of adjunction. In this section and the next, we meet two ways of rephrasing the definition. The one in this section is most useful for theoretical purposes, while the one in the next fits well with many examples.

To start building the theory of adjoint functors, we have to take seriously the naturality requirement (equations (2.2) and (2.3)), which has so far been <span class="original-page-anchor" id="pdf-page-60" aria-hidden="true"></span>ignored. Take an adjunction

![An adjunction](/library/volume-87/diagrams/pdf-0060-adjunction.png)

. Intuitively, naturality says that as $A$ varies in $\mathscr{A}$ and $B$ varies in $\mathscr{B}$, the isomorphism between $\mathscr{B}(F(A), B)$ and $\mathscr{A}(A, G(B))$ varies in a way that is compatible with all the structure already in place. In other words, it is compatible with composition in the categories $\mathscr{A}$ and $\mathscr{B}$ and the action of the functors $F$ and $G$.

But what does ‘compatible’ mean? Suppose, for example, that we have maps

$$
F(A) \xrightarrow{g} B \xrightarrow{q} B'
$$

in $\mathscr{B}$. There are two things we can do with this data: either compose then take the transpose, which produces a map $\overline{q \circ g}: A \to G(B')$, or take the transpose of $g$ then compose it with $G(q)$, which produces a potentially different map $G(q) \circ \bar{g}: A \to G(B')$. Compatibility means that they are equal; and that is the first naturality equation (2.2). The second is its dual, and can be explained in a similar way.

For each $A \in \mathscr{A}$, we have a map

$$
\Bigl(A \xrightarrow{\eta_A} GF(A)\Bigr) = \overline{\Bigl(F(A) \xrightarrow{1} F(A)\Bigr)}.
$$

Dually, for each $B \in \mathscr{B}$, we have a map

$$
\Bigl(FG(B) \xrightarrow{\varepsilon_B} B\Bigr) = \overline{\Bigl(G(B) \xrightarrow{1} G(B)\Bigr)}.
$$

(We have begun to omit brackets, writing $GF(A)$ instead of $G(F(A))$, etc.) These define natural transformations

$$
\eta: 1_{\mathscr{A}} \to G \circ F, \qquad \varepsilon: F \circ G \to 1_{\mathscr{B}},
$$

called the **unit** and **counit** of the adjunction, respectively.

**Example 2.2.1** Take the usual adjunction

![The vector space and set adjunction](/library/volume-87/diagrams/pdf-0060-vector-adjunction.png)

. Its unit $\eta: 1_{\mathbf{Set}} \to U \circ F$ has components

$$
\begin{array}{rcl}
\eta_S: S &\to& UF(S) = \bigl\{\text{formal } k\text{-linear sums }\sum_{s \in S} \lambda_s s\bigr\} \\
s &\mapsto& s
\end{array}
$$

($S \in \mathbf{Set}$). The component of the counit $\varepsilon$ at a vector space $V$ is the linear map

$$
\varepsilon_V: FU(V) \to V
$$

that sends a *formal* linear sum $\sum_{v \in V} \lambda_v v$ to its *actual* value in $V$.

The vector space $FU(V)$ is enormous. For instance, if $k = \mathbb{R}$ and $V$ is the vector space $\mathbb{R}^2$, then $U(V)$ is the set $\mathbb{R}^2$ and $FU(V)$ is a vector space with <span class="original-page-anchor" id="pdf-page-61" aria-hidden="true"></span>one basis element for every element of $\mathbb{R}^2$; thus, it is uncountably infinite-dimensional. Then $\varepsilon_V$ is a map from this infinite-dimensional space to the $2$-dimensional space $V$.

**Lemma 2.2.2** Given an adjunction $F \dashv G$ with unit $\eta$ and counit $\varepsilon$, the triangles

![Triangle identities for the functors](/library/volume-87/diagrams/pdf-0061-triangle-identities.png)

commute.

**Remark 2.2.3** These are called the **triangle identities**. They are commutative diagrams in the functor categories $[\mathscr{A}, \mathscr{B}]$ and $[\mathscr{B}, \mathscr{A}]$, respectively. For an explanation of the notation, see Remarks 1.3.24 (particularly the special cases mentioned on page 37). An equivalent statement is that the triangles

![Component triangle identities, equation (2.4)](/library/volume-87/diagrams/pdf-0061-component-triangles.png)

commute for all $A \in \mathscr{A}$ and $B \in \mathscr{B}$.

**Proof of Lemma 2.2.2** We prove that the triangles (2.4) commute. Let $A \in \mathscr{A}$. Since $\overline{1_{GF(A)}} = \varepsilon_{F(A)}$, equation (2.3) gives

$$
\overline{\Bigl(A \xrightarrow{\eta_A} GF(A) \xrightarrow{1} GF(A)\Bigr)}
= \Bigl(F(A) \xrightarrow{F(\eta_A)} FGF(A) \xrightarrow{\varepsilon_{F(A)}} F(A)\Bigr).
$$

But the left-hand side is $\overline{\eta_A} = \overline{\overline{1_{F(A)}}} = 1_{F(A)}$, proving the first identity. The second follows by duality. $\square$

Amazingly, the unit and counit determine the whole adjunction, even though they appear to know only the transposes *of identities*. This is the main content of the following pair of results.

**Lemma 2.2.4** Let

![An adjunction](/library/volume-87/diagrams/pdf-0061-adjunction.png)

be an adjunction, with unit $\eta$ and counit $\varepsilon$. Then

$$
\bar{g} = G(g) \circ \eta_A
$$

<span class="original-page-anchor" id="pdf-page-62" aria-hidden="true"></span>

for any $g: F(A) \to B$, and

$$
\bar{f} = \varepsilon_B \circ F(f)
$$

for any $f: A \to G(B)$.

**Proof** For any map $g: F(A) \to B$, we have

$$
\begin{aligned}
\overline{\Bigl(F(A) \xrightarrow{g} B\Bigr)}
&= \overline{\Bigl(F(A) \xrightarrow{1} F(A) \xrightarrow{g} B\Bigr)} \\
&= \Bigl(A \xrightarrow{\eta_A} GF(A) \xrightarrow{G(g)} G(B)\Bigr)
\end{aligned}
$$

by equation (2.2), giving the first statement. The second follows by duality. $\square$

**Theorem 2.2.5** Take categories and functors

![A pair of functors in opposite directions](/library/volume-87/diagrams/pdf-0062-functor-pair.png)

. There is a one-to-one correspondence between:

(a) adjunctions between $F$ and $G$ (with $F$ on the left and $G$ on the right);

(b) pairs $\Bigl(1_{\mathscr{A}} \xrightarrow{\eta} GF,\ FG \xrightarrow{\varepsilon} 1_{\mathscr{B}}\Bigr)$ of natural transformations satisfying the triangle identities.

(Recall that by definition, an adjunction between $F$ and $G$ is a choice of isomorphism (2.1) for each $A$ and $B$, satisfying the naturality equations (2.2) and (2.3).)

**Proof** We have shown that every adjunction between $F$ and $G$ gives rise to a pair $(\eta, \varepsilon)$ satisfying the triangle identities. We now have to show that this process is bijective. So, take a pair $(\eta, \varepsilon)$ of natural transformations satisfying the triangle identities. We must show that there is a unique adjunction between $F$ and $G$ with unit $\eta$ and counit $\varepsilon$.

Uniqueness follows from Lemma 2.2.4. For existence, take natural transformations $\eta$ and $\varepsilon$ as in (b). For each $A$ and $B$, define functions

$$
\mathscr{B}(F(A), B) \rightleftarrows \mathscr{A}(A, G(B)), \tag{2.5}
$$

both denoted by a bar, as follows. Given $g \in \mathscr{B}(F(A), B)$, put $\bar{g} = G(g) \circ \eta_A \in \mathscr{A}(A, G(B))$. Similarly, in the opposite direction, put $\bar{f} = \varepsilon_B \circ F(f)$.

I claim that for each $A$ and $B$, the two functions $g \mapsto \bar{g}$ and $f \mapsto \bar{f}$ are mutually inverse. Indeed, given a map $g: F(A) \to B$ in $\mathscr{B}$, we have a commutative diagram

![The diagram proving that the transposition functions are inverse](/library/volume-87/diagrams/pdf-0062-inverse-transposes.png)

<span class="original-page-anchor" id="pdf-page-63" aria-hidden="true"></span>

The composite map from $F(A)$ to $B$ by one route around the outside of the diagram is

$$
\varepsilon_B \circ FG(g) \circ F(\eta_A) = \varepsilon_B \circ F(\bar{g}) = \bar{\bar{g}},
$$

and by the other is $g \circ 1 = g$, so $\bar{\bar{g}} = g$. Dually, $\bar{\bar{f}} = f$ for any map $f: A \to G(B)$ in $\mathscr{A}$. This proves the claim.

It is straightforward to check the naturality equations (2.2) and (2.3). The functions (2.5) therefore define an adjunction. Finally, its unit and counit are $\eta$ and $\varepsilon$, since the component of the unit at $A$ is

$$
\overline{1_{F(A)}} = G(1_{F(A)}) \circ \eta_A = 1 \circ \eta_A = \eta_A,
$$

and dually for the counit. $\square$

**Corollary 2.2.6** Take categories and functors

![A pair of functors in opposite directions](/library/volume-87/diagrams/pdf-0063-functor-pair.png)

. Then $F \dashv G$ if and only if there exist natural transformations $1 \xrightarrow{\eta} GF$ and $FG \xrightarrow{\varepsilon} 1$ satisfying the triangle identities. $\square$

**Example 2.2.7** An adjunction between ordered sets consists of order-preserving maps

![Order-preserving maps in opposite directions](/library/volume-87/diagrams/pdf-0063-ordered-pair.png)

such that

$$
\forall a \in A,\ \forall b \in B, \qquad f(a) \leq b \iff a \leq g(b). \tag{2.6}
$$

This is because both sides of the isomorphism (2.1) in the definition of adjunction are sets with at most one element, so they are isomorphic if and only if they are both empty or both nonempty. The naturality requirements (2.2) and (2.3) hold automatically, since in an ordered set, any two maps with the same domain and codomain are equal.

Recall from Example 1.3.9 that if

![Parallel order-preserving maps](/library/volume-87/diagrams/pdf-0063-parallel-pair.png)

are order-preserving maps of ordered sets then there is at most one natural transformation from $p$ to $q$, and there is one if and only if $p(c) \leq q(c)$ for all $c \in C$. The unit of the adjunction above is the statement that $a \leq gf(a)$ for all $a \in A$, and the counit is the statement that $fg(b) \leq b$ for all $b \in B$. The triangle identities say nothing, since they assert the equality of two maps in an ordered set with the same domain and codomain.

In the case of ordered sets, Corollary 2.2.6 states that condition (2.6) is equivalent to:

$$
\forall a \in A,\ a \leq gf(a) \qquad \text{and} \qquad \forall b \in B,\ fg(b) \leq b.
$$

This equivalence can also be proved directly (Exercise 2.2.10).

<span class="original-page-anchor" id="pdf-page-64" aria-hidden="true"></span>

For instance, let $X$ be a topological space. Take the set $\mathscr{C}(X)$ of closed subsets of $X$ and the set $\mathscr{P}(X)$ of all subsets of $X$, both ordered by $\subseteq$. There are order-preserving maps

![Closure and inclusion maps](/library/volume-87/diagrams/pdf-0064-closure-pair.png)

where $i$ is the inclusion map and $\operatorname{Cl}$ is closure. This is an adjunction, with $\operatorname{Cl}$ left adjoint to $i$, as witnessed by the fact that

$$
\operatorname{Cl}(A) \subseteq B \iff A \subseteq B
$$

for all $A \subseteq X$ and closed $B \subseteq X$. An equivalent statement is that $A \subseteq \operatorname{Cl}(A)$ for all $A \subseteq X$ and $\operatorname{Cl}(B) \subseteq B$ for all closed $B \subseteq X$. Either way, we see that the topological operation of closure arises as an adjoint functor.

**Remark 2.2.8** Theorem 2.2.5 states that an adjunction may be regarded as a quadruple $(F, G, \eta, \varepsilon)$ of functors and natural transformations satisfying the triangle identities. An equivalence $(F, G, \eta, \varepsilon)$ of categories (as in Definition 1.3.15) is not necessarily an adjunction. It *is* true that $F$ is left adjoint to $G$ (Exercise 2.3.10), but $\eta$ and $\varepsilon$ are not necessarily the unit and counit (because there is no reason why they should satisfy the triangle identities).

**Remark 2.2.9** There is a way of drawing natural transformations that makes the triangle identities intuitively plausible. Suppose, for instance, that we have categories and functors

$$
\mathscr{A} \xrightarrow{F_1} \mathscr{C}_1 \xrightarrow{F_2} \mathscr{C}_2 \xrightarrow{F_3} \mathscr{C}_3 \xrightarrow{F_4} \mathscr{B}, \qquad \mathscr{A} \xrightarrow{G_1} \mathscr{D}_1 \xrightarrow{G_2} \mathscr{B}
$$

and a natural transformation $\alpha: F_4 F_3 F_2 F_1 \to G_2 G_1$. We usually draw $\alpha$ like this:

![The usual diagram for the natural transformation](/library/volume-87/diagrams/pdf-0064-natural-transformation.png)

However, we can also draw $\alpha$ as a **string diagram**:

![A string diagram for the natural transformation](/library/volume-87/diagrams/pdf-0064-string-diagram.png)

<span class="original-page-anchor" id="pdf-page-65" aria-hidden="true"></span>

There is nothing special about $4$ and $2$; we could replace them by any natural numbers $m$ and $n$. If $m = 0$ then $\mathscr{A} = \mathscr{B}$ and the domain of $\alpha$ is $1_{\mathscr{A}}$ (keeping in mind the last paragraph of Remark 1.1.2(b)). In that case, the disk labelled $\alpha$ has no strings coming into the top. Similarly, if $n = 0$ then there are no strings coming out of the bottom.

Vertical composition of natural transformations corresponds to joining string diagrams together vertically, and horizontal composition corresponds to putting them side by side. The identity on a functor $F$ is drawn as a simple string,

![The identity on a functor as a string](/library/volume-87/diagrams/pdf-0065-identity-string.png)

Now let us apply this notation to adjunctions. The unit and counit are drawn as

![The unit as a string diagram](/library/volume-87/diagrams/pdf-0065-unit-string.png)

and

![The counit as a string diagram](/library/volume-87/diagrams/pdf-0065-counit-string.png)

The triangle identities now become the topologically plausible equations

![The triangle identity for F as a string diagram](/library/volume-87/diagrams/pdf-0065-triangle-string-f.png)

and

![The triangle identity for G as a string diagram](/library/volume-87/diagrams/pdf-0065-triangle-string-g.png)

In both equations, the right-hand side is obtained from the left by simply pulling the string straight.

### Exercises

**2.2.10** Let

![Order-preserving maps in opposite directions](/library/volume-87/diagrams/pdf-0065-ordered-pair.png)

be order-preserving maps between ordered sets. Prove *directly* that the following conditions are equivalent:

(a) for all $a \in A$ and $b \in B$,

$$
f(a) \leq b \iff a \leq g(b);
$$

<span class="original-page-anchor" id="pdf-page-66" aria-hidden="true"></span>

(b) $a \leq g(f(a))$ for all $a \in A$ and $f(g(b)) \leq b$ for all $b \in B$.

(Both conditions state that $f \dashv g$; see Example 2.2.7.)

**2.2.11** (a) Let

![Adjunction](/library/volume-87/diagrams/pdf-0066-adjunction-a.png)

be an adjunction with unit $\eta$ and counit $\varepsilon$. Write $\mathbf{Fix}(GF)$ for the full subcategory of $\mathscr{A}$ whose objects are those $A \in \mathscr{A}$ such that $\eta_A$ is an isomorphism, and dually $\mathbf{Fix}(FG) \subseteq \mathscr{B}$. Prove that the adjunction $(F,G,\eta,\varepsilon)$ restricts to an equivalence $(F',G',\eta',\varepsilon')$ between $\mathbf{Fix}(GF)$ and $\mathbf{Fix}(FG)$.

(b) Part (a) shows that every adjunction restricts to an equivalence between full subcategories in a canonical way. Take some examples of adjunctions and work out what this equivalence is.

**2.2.12** (a) Show that for any adjunction, the right adjoint is full and faithful if and only if the counit is an isomorphism.

(b) An adjunction satisfying the equivalent conditions of part (a) is called a **reflection**. (Compare Example 2.1.3(d).) Of the examples of adjunctions given in this chapter, which are reflections?

**2.2.13** (a) Let $f:K \to L$ be a map of sets, and denote by $f^*: \mathscr{P}(L) \to \mathscr{P}(K)$ the map sending a subset $S$ of $L$ to its inverse image $f^{-1}S \subseteq K$. Then $f^*$ is order-preserving with respect to the inclusion orderings on $\mathscr{P}(K)$ and $\mathscr{P}(L)$, and so can be seen as a functor. Find left and right adjoints to $f^*$.

(b) Now let $X$ and $Y$ be sets, and write $p:X \times Y \to X$ for first projection. Regard a subset $S$ of $X$ as a predicate $S(x)$ in one variable $x \in X$, and similarly a subset $R$ of $X \times Y$ as a predicate $R(x,y)$ in two variables. What, in terms of predicates, are the left and right adjoints to $p^*$? For each of the adjunctions, interpret the unit and counit as logical implications. (Hint: the left adjoint to $p^*$ is often written as $\exists_Y$, and the right adjoint as $\forall_Y$.)

**2.2.14** Given a functor $F:\mathscr{A} \to \mathscr{B}$ and a category $\mathscr{S}$, there is a functor $F^*:[\mathscr{B},\mathscr{S}] \to [\mathscr{A},\mathscr{S}]$ defined on objects $Y \in [\mathscr{B},\mathscr{S}]$ by $F^*(Y)=Y \circ F$ and on maps $\alpha$ by $F^*(\alpha)=\alpha F$. Show that any adjunction

![Adjunction](/library/volume-87/diagrams/pdf-0066-adjunction-b.png)

and category $\mathscr{S}$ give rise to an adjunction

![Induced adjunction](/library/volume-87/diagrams/pdf-0066-induced-adjunction.png)

(Hint: use Theorem 2.2.5.)

<span class="original-page-anchor" id="pdf-page-67" aria-hidden="true"></span>

## 2.3 Adjunctions via initial objects

We now come to the third formulation of adjointness, which is the one you will probably see most often in everyday mathematics.

Consider once more the adjunction

![Free and forgetful adjunction](/library/volume-87/diagrams/pdf-0067-free-forgetful.png)

Let $S$ be a set. The universal property of $F(S)$, the vector space whose basis is $S$, is most commonly stated like this:

> given a vector space $V$, any function $f:S \to V$ extends uniquely to a linear map $\bar f:F(S) \to V$.

As remarked in Example 2.1.3(a), forgetful functors are often forgotten: in this statement, ‘$f:S \to V$’ should strictly speaking be ‘$f:S \to U(V)$’. Also, the word ‘extends’ refers implicitly to the embedding

$$
\begin{array}{rccc}
\eta_S:&S&\longrightarrow&UF(S)\\
&s&\longmapsto&s.
\end{array}
$$

So in precise language, the statement reads:

> for any $V \in \mathbf{Vect}_k$ and $f \in \mathbf{Set}(S,U(V))$, there is a unique $\bar f \in \mathbf{Vect}_k(F(S),V)$ such that the diagram

![Universal property (2.7)](/library/volume-87/diagrams/pdf-0067-universal-property.png)

> commutes.

(Compare Example 0.4.) In this section, we show that this statement is equivalent to the statement that $F$ is left adjoint to $U$ with unit $\eta$.

To do this, we need a definition.

**Definition 2.3.1** Given categories and functors

![Input functors for a comma category](/library/volume-87/diagrams/pdf-0067-comma-input.png)

<span class="original-page-anchor" id="pdf-page-68" aria-hidden="true"></span>

the **comma category** $(P \Rightarrow Q)$ (often written as $(P \mathbin{\downarrow} Q)$) is the category defined as follows:

- objects are triples $(A,h,B)$ with $A \in \mathscr{A}$, $B \in \mathscr{B}$, and $h:P(A) \to Q(B)$ in $\mathscr{C}$;
- maps $(A,h,B) \to (A',h',B')$ are pairs $(f:A \to A',\,g:B \to B')$ of maps such that the square

![Comma category morphism square](/library/volume-87/diagrams/pdf-0068-comma-square.png)

commutes.

**Remark 2.3.2** Given $\mathscr{A}$, $\mathscr{B}$, $\mathscr{C}$, $P$ and $Q$ as above, there are canonical functors and a canonical natural transformation as shown:

![Canonical functors and natural transformation](/library/volume-87/diagrams/pdf-0068-comma-universal.png)

In a suitable 2-categorical sense, $(P \Rightarrow Q)$ is universal with this property.

**Example 2.3.3** Let $\mathscr{A}$ be a category and $A \in \mathscr{A}$. The **slice category** of $\mathscr{A}$ over $A$, denoted by $\mathscr{A}/A$, is the category whose objects are maps into $A$ and whose maps are commutative triangles. More precisely, an object is a pair $(X,h)$ with $X \in \mathscr{A}$ and $h:X \to A$ in $\mathscr{A}$, and a map $(X,h) \to (X',h')$ in $\mathscr{A}/A$ is a map $f:X \to X'$ in $\mathscr{A}$ making the triangle

![Slice category triangle](/library/volume-87/diagrams/pdf-0068-slice-triangle.png)

commute.

Slice categories are a special case of comma categories. Recall from Example 2.1.9 that functors $\mathbf{1} \to \mathscr{A}$ are just objects of $\mathscr{A}$. Now, given an object $A$ of $\mathscr{A}$, consider the comma category $(1_{\mathscr{A}} \Rightarrow A)$, as in the diagram

![Slice category as a comma category](/library/volume-87/diagrams/pdf-0068-slice-comma.png)

<span class="original-page-anchor" id="pdf-page-69" aria-hidden="true"></span>

An object of $(1_{\mathscr{A}} \Rightarrow A)$ is in principle a triple $(X,h,B)$ with $X \in \mathscr{A}$, $B \in \mathbf{1}$, and $h:X \to A$ in $\mathscr{A}$; but $\mathbf{1}$ has only one object, so it is essentially just a pair $(X,h)$. Hence the comma category $(1_{\mathscr{A}} \Rightarrow A)$ has the same objects as the slice category $\mathscr{A}/A$. One can check that it has the same maps too, so that $\mathscr{A}/A \cong (1_{\mathscr{A}} \Rightarrow A)$.

Dually (reversing all the arrows), there is a **coslice category** $A/\mathscr{A} \cong (A \Rightarrow 1_{\mathscr{A}})$, whose objects are the maps out of $A$.

**Example 2.3.4** Let $G:\mathscr{B} \to \mathscr{A}$ be a functor and let $A \in \mathscr{A}$. We can form the comma category $(A \Rightarrow G)$, as in the diagram

![Comma category input](/library/volume-87/diagrams/pdf-0069-comma-input.png)

Its objects are pairs $(B \in \mathscr{B},\,f:A \to G(B))$. A map $(B,f) \to (B',f')$ in $(A \Rightarrow G)$ is a map $q:B \to B'$ in $\mathscr{B}$ making the triangle

![Comma category morphism triangle](/library/volume-87/diagrams/pdf-0069-comma-triangle.png)

commute.

Notice how this diagram resembles the diagram (2.7) in the vector space example. We will use comma categories $(A \Rightarrow G)$ to capture the kind of universal property discussed there.

Speaking casually, we say that $f:A \to G(B)$ is an object of $(A \Rightarrow G)$, when what we should really say is that the pair $(B,f)$ is an object of $(A \Rightarrow G)$. There is potential for confusion here, since there may be different objects $B,B'$ of $\mathscr{B}$ with $G(B)=G(B')$. Nevertheless, we will often use this convention.

We now make the connection between comma categories and adjunctions.

**Lemma 2.3.5** Take an adjunction

![Adjunction](/library/volume-87/diagrams/pdf-0069-lemma-adjunction.png)

and an object $A \in \mathscr{A}$. Then the unit map $\eta_A:A \to GF(A)$ is an initial object of $(A \Rightarrow G)$.

**Proof** Let $(B,\,f:A \to G(B))$ be an object of $(A \Rightarrow G)$. We have to show that there is exactly one map from $(F(A),\eta_A)$ to $(B,f)$.

A map $(F(A),\eta_A) \to (B,f)$ in $(A \Rightarrow G)$ is a map $q:F(A) \to B$ in $\mathscr{B}$ such <span class="original-page-anchor" id="pdf-page-70" aria-hidden="true"></span>that

![Initiality of the unit (2.8)](/library/volume-87/diagrams/pdf-0070-unit-initial.png)

commutes. But $G(q) \circ \eta_A=\bar q$ by Lemma 2.2.4, so (2.8) commutes if and only if $f=\bar q$, if and only if $q=\bar f$. Hence $\bar f$ is the unique map $(F(A),\eta_A) \to (B,f)$ in $(A \Rightarrow G)$. $\square$

We now meet our third and final formulation of adjointness.

**Theorem 2.3.6** Take categories and functors

![Functors in opposite directions](/library/volume-87/diagrams/pdf-0070-theorem-functors.png).

There is a one-to-one correspondence between:

(a) adjunctions between $F$ and $G$ (with $F$ on the left and $G$ on the right);

(b) natural transformations $\eta:1_{\mathscr{A}} \to GF$ such that $\eta_A:A \to GF(A)$ is initial in $(A \Rightarrow G)$ for every $A \in \mathscr{A}$.

**Proof** We have just shown that every adjunction between $F$ and $G$ gives rise to a natural transformation $\eta$ with the property stated in (b). To prove the theorem, we have to show that every $\eta$ with the property in (b) is the unit of exactly one adjunction between $F$ and $G$.

By Theorem 2.2.5, an adjunction between $F$ and $G$ amounts to a pair $(\eta,\varepsilon)$ of natural transformations satisfying the triangle identities. So it is enough to prove that for every $\eta$ with the property in (b), there exists a unique natural transformation $\varepsilon:FG \to 1_{\mathscr{B}}$ such that the pair $(\eta,\varepsilon)$ satisfies the triangle identities.

Let $\eta:1_{\mathscr{A}} \to GF$ be a natural transformation with the property in (b).

**Uniqueness** Suppose that $\varepsilon,\varepsilon':FG \to 1_{\mathscr{B}}$ are natural transformations such that both $(\eta,\varepsilon)$ and $(\eta,\varepsilon')$ satisfy the triangle identities. One of the triangle identities states that for all $B \in \mathscr{B}$, the triangle

![First triangle identity (2.9)](/library/volume-87/diagrams/pdf-0070-triangle-identity.png)

commutes. Thus, $\varepsilon_B$ is a map

$$
\Bigl(FG(B),\ G(B) \xrightarrow{\eta_{G(B)}} G(FG(B))\Bigr)
\longrightarrow
\Bigl(B,\ G(B) \xrightarrow{1} G(B)\Bigr)
$$

<span class="original-page-anchor" id="pdf-page-71" aria-hidden="true"></span>

in $(G(B) \Rightarrow G)$. The same is true of $\varepsilon'_B$. But $\eta_{G(B)}$ is initial, so there is only one such map, so $\varepsilon_B=\varepsilon'_B$. This holds for all $B$, so $\varepsilon=\varepsilon'$.

**Existence** For $B \in \mathscr{B}$, define $\varepsilon_B:FG(B) \to B$ to be the unique map

$$
(FG(B),\eta_{G(B)}) \longrightarrow (B,1_{G(B)})
$$

in $(G(B) \Rightarrow G)$. (So by definition of $\varepsilon_B$, triangle (2.9) commutes.) We show that $(\varepsilon_B)_{B \in \mathscr{B}}$ is a natural transformation $FG \to 1$ such that $\eta$ and $\varepsilon$ satisfy the triangle identities.

To prove naturality, take $B \xrightarrow{q} B'$ in $\mathscr{B}$. We have commutative diagrams

![Diagrams proving naturality of the counit](/library/volume-87/diagrams/pdf-0071-counit-naturality.png)

So $q \circ \varepsilon_B$ and $\varepsilon_{B'} \circ FG(q)$ are both maps $\eta_{G(B)} \to G(q)$ in $(G(B) \Rightarrow G)$, and since $\eta_{G(B)}$ is initial, they must be equal. This proves naturality of $\varepsilon$ with respect to $q$. Hence $\varepsilon$ is a natural transformation.

We have already observed that one of the triangle identities, equation (2.9), holds. The other states that for $A \in \mathscr{A}$,

![Second triangle identity](/library/volume-87/diagrams/pdf-0071-second-triangle.png)

commutes. To prove it, we repeat our previous technique: there are commutative diagrams

![Diagrams proving the second triangle identity by initiality](/library/volume-87/diagrams/pdf-0071-initiality-diagrams.png)

<span class="original-page-anchor" id="pdf-page-72" aria-hidden="true"></span>

so by initiality of $\eta_A$, we have $\varepsilon_{F(A)} \circ F(\eta_A)=1_{F(A)}$, as required. $\square$

In Section 6.3 we will meet the adjoint functor theorems, which state conditions under which a functor is guaranteed to have a left adjoint. The following corollary is the starting point for their proofs.

**Corollary 2.3.7** Let $G:\mathscr{B} \to \mathscr{A}$ be a functor. Then $G$ has a left adjoint if and only if for each $A \in \mathscr{A}$, the category $(A \Rightarrow G)$ has an initial object.

**Proof** Lemma 2.3.5 proves ‘only if’. To prove ‘if’, let us choose for each $A \in \mathscr{A}$ an initial object of $(A \Rightarrow G)$ and call it $(F(A),\,\eta_A:A \to GF(A))$. (Here $F(A)$ and $\eta_A$ are just the names we choose to use.) For each map $f:A \to A'$ in $\mathscr{A}$, let $F(f):F(A) \to F(A')$ be the unique map such that

![Construction of the left adjoint](/library/volume-87/diagrams/pdf-0072-left-adjoint-construction.png)

commutes (in other words, the unique map $\eta_A \to \eta_{A'} \circ f$ in $(A \Rightarrow G)$). It is easily checked that $F$ is a functor $\mathscr{A} \to \mathscr{B}$, and the diagram tells us that $\eta$ is a natural transformation $1 \to GF$. So by Theorem 2.3.6, $F$ is left adjoint to $G$. $\square$

This corollary justifies the claim made at the beginning of the section: that given functors $F$ and $G$, to have an adjunction $F \dashv G$ amounts to having maps $\eta_A:A \to GF(A)$ with the universal property stated there.

### Exercises

**2.3.8** What can be said about adjunctions between groups (regarded as one-object categories)?

**2.3.9** State the dual of Corollary 2.3.7. How would you prove your dual statement?

**2.3.10** Let $(F,G,\eta,\varepsilon)$ be an equivalence of categories, as in Definition 1.3.15. Prove that $F$ is left adjoint to $G$ (heeding the warning in Remark 2.2.8).

**2.3.11** Let

![Adjunction with sets](/library/volume-87/diagrams/pdf-0072-exercise-adjunction.png)

be an adjunction. Suppose that for at least one $A \in \mathscr{A}$, the set $U(A)$ has at least two elements. Prove that for each set $S$, the unit map $\eta_S:S \to UF(S)$ is injective. What does this mean in the case of the usual adjunction between $\mathbf{Grp}$ and $\mathbf{Set}$?

<span class="original-page-anchor" id="pdf-page-73" aria-hidden="true"></span>

**2.3.12** Given sets $A$ and $B$, a **partial function** from $A$ to $B$ is a pair $(S,f)$ consisting of a subset $S \subseteq A$ and a function $S \to B$. (Think of it as like a function from $A$ to $B$, but undefined at certain elements of $A$.) Let $\mathbf{Par}$ be the category of sets and partial functions.

Show that $\mathbf{Par}$ is equivalent to $\mathbf{Set}_*$, the category of sets equipped with a distinguished element and functions preserving distinguished elements. Show also that $\mathbf{Set}_*$ can be described as a coslice category in a simple way.
