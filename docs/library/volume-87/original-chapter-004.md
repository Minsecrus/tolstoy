---
title: "Representables"
description: "Tom Leinster《Basic Category Theory》English。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"Interlude on sets","link":"/library/volume-87/original-chapter-003"}
next: {"text":"Limits","link":"/library/volume-87/original-chapter-005"}
---

# Representables

<span class="original-page-anchor" id="pdf-page-92" aria-hidden="true"></span>

A category is a world of objects, all looking at one another. Each sees the world from a different viewpoint.

Consider, for instance, the category of topological spaces, and let us ask how it looks when viewed from the one-point space $1$. A map from $1$ to a space $X$ is essentially the same thing as a point of $X$, so we might say that $1$ ‘sees points’. Similarly, a map from $\mathbb{R}$ to a space $X$ could reasonably be called a curve in $X$, and in this sense, $\mathbb{R}$ sees curves.

Now consider the category of groups. A map from the infinite cyclic group $\mathbb{Z}$ to a group $G$ amounts to an element of $G$. (For given $g\in G$, there is a unique homomorphism $\phi:\mathbb{Z}\to G$ such that $\phi(1)=g$.) So, $\mathbb{Z}$ sees elements. Similarly, if $p$ is a prime number then the cyclic group $\mathbb{Z}/p\mathbb{Z}$ sees elements of order $1$ or $p$.

Any ring homomorphism between fields is injective, so in the category of fields, a map $K\to L$ is a way of realizing $L$ as an extension of $K$. Hence each field $K$ sees the extensions of itself. If $K$ and $L$ are fields of different characteristic then there are no homomorphisms between $K$ and $L$, so the category of fields is the union of disjoint subcategories $\mathbf{Field}_0$, $\mathbf{Field}_2$, $\mathbf{Field}_3$, $\mathbf{Field}_5$, $\ldots$ consisting of the fields of characteristics $0$, $2$, $3$, $5$, $\ldots$. Each field is blind to the fields of different characteristic.

In the ordered set $(\mathbb{R},\leq)$, the object $0$ sees whether a number is nonnegative. In other words, if $x$ is nonnegative then there is one map $0\to x$, and if not, there are none.

We can also ask the dual question: fixing an object of a category, what are the maps *into* it? Let $S$ be the two-element set, for instance. For an arbitrary set $X$, the maps from $X$ to $S$ correspond to the subsets of $X$ (as we saw in Section 3.1). Now give $S$ the topology in which one of the singleton subsets is open but the other is not. For any topological space $X$, the continuous maps from $X$ into $S$ correspond to the *open* subsets of $X$.

<span class="original-page-anchor" id="pdf-page-93" aria-hidden="true"></span>

This chapter explores the theme of how each object sees and is seen by the category in which it lives. We are naturally led to the notion of representable functor, which (after adjunctions) provides our second approach to the idea of universal property.

## 4.1 Definitions and examples

Fix an object $A$ of a category $\mathscr{A}$. We will consider the totality of maps out of $A$. To each $B\in\mathscr{A}$, there is assigned the set (or class) $\mathscr{A}(A,B)$ of maps from $A$ to $B$. The content of the following definition is that this assignation is functorial in $B$: any map $B\to B'$ induces a function $\mathscr{A}(A,B)\to\mathscr{A}(A,B')$.

**Definition 4.1.1** Let $\mathscr{A}$ be a locally small category and $A\in\mathscr{A}$. We define a functor

$$
H^A=\mathscr{A}(A,-):\mathscr{A}\to\mathbf{Set}
$$

as follows:

- for objects $B\in\mathscr{A}$, put $H^A(B)=\mathscr{A}(A,B)$;
- for maps $B\xrightarrow{g}B'$ in $\mathscr{A}$, define

  $$
  H^A(g)=\mathscr{A}(A,g):\mathscr{A}(A,B)\to\mathscr{A}(A,B')
  $$

  by

  $$
  p\mapsto g\circ p
  $$

  for all $p:A\to B$.

**Remarks 4.1.2** (a) Recall that ‘locally small’ means that each class $\mathscr{A}(A,B)$ is in fact a set. This hypothesis is clearly necessary in order for the definition to make sense.

(b) Sometimes $H^A(g)$ is written as $g\circ-$ or $g_*$. All three forms, as well as $\mathscr{A}(A,g)$, are in use.

**Definition 4.1.3** Let $\mathscr{A}$ be a locally small category. A functor $X:\mathscr{A}\to\mathbf{Set}$ is **representable** if $X\cong H^A$ for some $A\in\mathscr{A}$. A **representation** of $X$ is a choice of an object $A\in\mathscr{A}$ and an isomorphism between $H^A$ and $X$.

Representable functors are sometimes just called ‘representables’. Only set-valued functors (that is, functors with codomain $\mathbf{Set}$) can be representable.

<span class="original-page-anchor" id="pdf-page-94" aria-hidden="true"></span>

**Example 4.1.4** Consider $H^1:\mathbf{Set}\to\mathbf{Set}$, where $1$ is the one-element set. Since a map from $1$ to a set $B$ amounts to an element of $B$, we have

$$
H^1(B)\cong B
$$

for each $B\in\mathbf{Set}$. It is easily verified that this isomorphism is natural in $B$, so $H^1$ is isomorphic to the identity functor $1_{\mathbf{Set}}$. Hence $1_{\mathbf{Set}}$ is representable.

**Example 4.1.5** All of the ‘seeing’ functors in the introduction to this chapter are representable. The forgetful functor $\mathbf{Top}\to\mathbf{Set}$ is isomorphic to $H^1=\mathbf{Top}(1,-)$, and the forgetful functor $\mathbf{Grp}\to\mathbf{Set}$ is isomorphic to $\mathbf{Grp}(\mathbb{Z},-)$. For each prime $p$, there is a functor $U_p:\mathbf{Grp}\to\mathbf{Set}$ defined on objects by

$$
U_p(G)=\{\text{elements of }G\text{ of order }1\text{ or }p\},
$$

and as claimed above, $U_p\cong\mathbf{Grp}(\mathbb{Z}/p\mathbb{Z},-)$ (Exercise 4.1.28). Hence $U_p$ is representable.

**Example 4.1.6** There is a functor $\operatorname{ob}:\mathbf{Cat}\to\mathbf{Set}$ sending a small category to its set of objects. (The category $\mathbf{Cat}$ was introduced in Definition 3.2.10.) It is representable. Indeed, consider the terminal category $\mathbf{1}$ (with one object and only the identity map). A functor from $\mathbf{1}$ to a category $\mathscr{B}$ simply picks out an object of $\mathscr{B}$. Thus,

$$
H^{\mathbf{1}}(\mathscr{B})\cong\operatorname{ob}\mathscr{B}.
$$

Again, it is easily verified that this isomorphism is natural in $\mathscr{B}$; hence $\operatorname{ob}\cong\mathbf{Cat}(\mathbf{1},-)$. It can be shown similarly that the functor $\mathbf{Cat}\to\mathbf{Set}$ sending a small category to its set of maps is representable (Exercise 4.1.31).

**Example 4.1.7** Let $M$ be a monoid, regarded as a one-object category. Recall from Example 1.2.8 that a set-valued functor on $M$ is just an $M$-set. Since the category $M$ has only one object, there is only one representable functor on it (up to isomorphism). As an $M$-set, the unique representable is the so-called **left regular representation** of $M$, that is, the underlying set of $M$ acted on by multiplication on the left.

**Example 4.1.8** Let $\mathbf{Toph}_*$ be the category whose objects are topological spaces equipped with a basepoint and whose arrows are homotopy classes of basepoint-preserving continuous maps. Let $S^1\in\mathbf{Toph}_*$ be the circle. Then for any object $X\in\mathbf{Toph}_*$, the maps $S^1\to X$ in $\mathbf{Toph}_*$ are the elements of the fundamental group $\pi_1(X)$. Formally, this says that the composite functor

$$
\mathbf{Toph}_*\xrightarrow{\pi_1}\mathbf{Grp}\xrightarrow{U}\mathbf{Set}
$$

is isomorphic to $\mathbf{Toph}_*(S^1,-)$. In particular, it is representable.

<span class="original-page-anchor" id="pdf-page-95" aria-hidden="true"></span>

**Example 4.1.9** Fix a field $k$ and vector spaces $U$ and $V$ over $k$. There is a functor

$$
\mathbf{Bilin}(U,V;-):\mathbf{Vect}_k\to\mathbf{Set}
$$

whose value $\mathbf{Bilin}(U,V;W)$ at $W\in\mathbf{Vect}_k$ is the set of bilinear maps $U\times V\to W$. It can be shown that this functor is representable; in other words, there is a space $T$ with the property that

$$
\mathbf{Bilin}(U,V;W)\cong\mathbf{Vect}_k(T,W)
$$

naturally in $W$. This $T$ is the tensor product $U\otimes V$, which we met just after the proof of Lemma 0.7.

Adjunctions give rise to representable functors in the following way.

**Lemma 4.1.10** Let

![Adjunction](/library/volume-87/diagrams/pdf-0095-adjunction.png)

be locally small categories, and let $A\in\mathscr{A}$. Then the functor

$$
\mathscr{A}(A,G(-)):\mathscr{B}\to\mathbf{Set}
$$

(that is, the composite $\mathscr{B}\xrightarrow{G}\mathscr{A}\xrightarrow{H^A}\mathbf{Set}$) is representable.

**Proof** We have

$$
\mathscr{A}(A,G(B))\cong\mathscr{B}(F(A),B)
$$

for each $B\in\mathscr{B}$. If we can show that this isomorphism is natural in $B$, then we will have proved that $\mathscr{A}(A,G(-))$ is isomorphic to $H^{F(A)}$ and is therefore representable. So, let $B\xrightarrow{q}B'$ be a map in $\mathscr{B}$. We must show that the square

![Naturality square](/library/volume-87/diagrams/pdf-0095-naturality-square.png)

commutes, where the horizontal arrows are the bijections provided by the adjunction. For $f:A\to G(B)$, we have

![Images of elements in the naturality square](/library/volume-87/diagrams/pdf-0095-elements-square.png)

so we must prove that $q\circ\bar{f}=\overline{G(q)\circ f}$. This follows immediately from the naturality condition (2.2) in the definition of adjunction (with $g=\bar{f}$). $\square$ <span class="original-page-anchor" id="pdf-page-96" aria-hidden="true"></span>You would not expect a randomly-chosen functor into $\mathbf{Set}$ to be representable. In some sense, rather few functors are. However, forgetful functors do tend to be representable:

**Proposition 4.1.11** Any set-valued functor with a left adjoint is representable.

**Proof** Let $G:\mathscr{A}\to\mathbf{Set}$ be a functor with a left adjoint $F$. Write $1$ for the one-point set. Then

$$
G(A)\cong\mathbf{Set}(1,G(A))
$$

naturally in $A\in\mathscr{A}$ (by Example 4.1.4), that is, $G\cong\mathbf{Set}(1,G(-))$. So by Lemma 4.1.10, $G$ is representable; indeed, $G\cong H^{F(1)}$. $\square$

**Example 4.1.12** Several of the examples of representables mentioned above arise as in Proposition 4.1.11. For instance, $U:\mathbf{Top}\to\mathbf{Set}$ has a left adjoint $D$ (Example 2.1.5), and $D(1)\cong1$, so we recover the result that $U\cong H^1$. Similarly, Exercise 3.2.16 asked you to construct a left adjoint $D$ to the objects functor $\operatorname{ob}:\mathbf{Cat}\to\mathbf{Set}$. This functor $D$ satisfies $D(1)\cong\mathbf{1}$, proving again that $\operatorname{ob}\cong H^{\mathbf{1}}$.

**Example 4.1.13** The forgetful functor $U:\mathbf{Vect}_k\to\mathbf{Set}$ is representable, since it has a left adjoint. Indeed, if $F$ denotes the left adjoint then $F(1)$ is the $1$-dimensional vector space $k$, so $U\cong H^k$. This is also easy to see directly: a map from $k$ to a vector space $V$ is uniquely determined by the image of $1$, which can be any element of $V$; hence $\mathbf{Vect}_k(k,V)\cong U(V)$ naturally in $V$.

**Example 4.1.14** Examples 2.1.3 began with the declaration that forgetful functors between categories of algebraic structures usually have left adjoints. Take the category $\mathbf{CRing}$ of commutative rings and the forgetful functor $U:\mathbf{CRing}\to\mathbf{Set}$. This general principle suggests that $U$ has a left adjoint, and Proposition 4.1.11 then tells us that $U$ is representable.

Let us see how this works explicitly. Given a set $S$, let $\mathbb{Z}[S]$ be the ring of polynomials over $\mathbb{Z}$ in commuting variables $x_s$ ($s\in S$). (This was called $F(S)$ in Example 1.2.4(b).) Then $S\mapsto\mathbb{Z}[S]$ defines a functor $\mathbf{Set}\to\mathbf{CRing}$, and this is left adjoint to $U$. Hence $U\cong H^{\mathbb{Z}[x]}$. Again, this can be verified directly: for any ring $R$, the maps $\mathbb{Z}[x]\to R$ correspond one-to-one with the elements of $R$ (Exercises 0.13 and 4.1.29).

We have defined, for each object $A$ of our category $\mathscr{A}$, a functor $H^A\in[\mathscr{A},\mathbf{Set}]$. This describes how $A$ sees the world. As $A$ varies, the view varies. On the other hand, it is always the same world being seen, so the different views from different objects are somehow related. (Compare aerial photos taken from a moving aeroplane, which agree well enough on their overlaps that they can be <span class="original-page-anchor" id="pdf-page-97" aria-hidden="true"></span>patched together to make one big picture.) So the family $(H^A)_{A\in\mathscr{A}}$ of ‘views’ has some consistency to it. What this means is that whenever there is a map between objects $A$ and $A'$, there is also a map between $H^A$ and $H^{A'}$.

Precisely, a map $A'\xrightarrow{f}A$ induces a natural transformation

![Natural transformation between representable functors](/library/volume-87/diagrams/pdf-0097-natural-transformation.png)

whose $B$-component (for $B\in\mathscr{A}$) is the function

$$
\begin{array}{rcl}
H^A(B)=\mathscr{A}(A,B)&\longrightarrow&H^{A'}(B)=\mathscr{A}(A',B)\\
p&\longmapsto&p\circ f.
\end{array}
$$

Again, $H^f$ goes by a variety of other names: $\mathscr{A}(f,-)$, $f^*$, and $-\circ f$.

Note the reversal of direction! Each functor $H^A$ is covariant, but they come together to form a *contravariant* functor, as in the following definition.

**Definition 4.1.15** Let $\mathscr{A}$ be a locally small category. The functor

$$
H^\bullet:\mathscr{A}^{\mathrm{op}}\to[\mathscr{A},\mathbf{Set}]
$$

is defined on objects $A$ by $H^\bullet(A)=H^A$ and on maps $f$ by $H^\bullet(f)=H^f$.

The symbol $\bullet$ is another type of blank, like $-$.

All of the definitions presented so far in this chapter can be dualized. At the formal level, this is trivial: reverse all the arrows, so that every $\mathscr{A}$ becomes an $\mathscr{A}^{\mathrm{op}}$ and vice versa. But in our usual examples, the flavour is different. We are no longer asking what objects *see*, but how they are *seen*.

Let us first dualize Definition 4.1.1.

**Definition 4.1.16** Let $\mathscr{A}$ be a locally small category and $A\in\mathscr{A}$. We define a functor

$$
H_A=\mathscr{A}(-,A):\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}
$$

as follows:

- for objects $B\in\mathscr{A}$, put $H_A(B)=\mathscr{A}(B,A)$;
- for maps $B'\xrightarrow{g}B$ in $\mathscr{A}$, define

  $$
  H_A(g)=\mathscr{A}(g,A)=g^*=-\circ g:\mathscr{A}(B,A)\to\mathscr{A}(B',A)
  $$

  by

  $$
  p\mapsto p\circ g
  $$

  for all $p:B\to A$.

<span class="original-page-anchor" id="pdf-page-98" aria-hidden="true"></span>

If you know about dual vector spaces, this construction will seem familiar. In particular, you will not be surprised that a map $B' \to B$ induces a map in the opposite direction, $H_A(B) \to H_A(B')$.

We now define representability for *contravariant* set-valued functors. Strictly speaking, this is unnecessary, as a contravariant functor on $\mathscr{A}$ is a covariant functor on $\mathscr{A}^{\mathrm{op}}$, and we already know what it means for a covariant set-valued functor to be representable. But it is useful to have a direct definition.

**Definition 4.1.17** Let $\mathscr{A}$ be a locally small category. A functor $X\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$ is **representable** if $X \cong H_A$ for some $A \in \mathscr{A}$. A **representation** of $X$ is a choice of an object $A \in \mathscr{A}$ and an isomorphism between $H_A$ and $X$.

**Example 4.1.18** There is a functor

$$
\mathscr{P}\colon \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}
$$

sending each set $B$ to its power set $\mathscr{P}(B)$, and defined on maps $g\colon B' \to B$ by $(\mathscr{P}(g))(U) = g^{-1}U$ for all $U \in \mathscr{P}(B)$. (Here $g^{-1}U$ denotes the inverse image or preimage of $U$ under $g$, defined by $g^{-1}U = \{x' \in B' \mid g(x') \in U\}$.) As we saw in Section 3.1, a subset amounts to a map into the two-point set $2$. Precisely put, $\mathscr{P} \cong H_2$.

**Example 4.1.19** Similarly, there is a functor

$$
\mathscr{O}\colon \mathbf{Top}^{\mathrm{op}} \to \mathbf{Set}
$$

defined on objects $B$ by taking $\mathscr{O}(B)$ to be the set of open subsets of $B$. If $S$ denotes the two-point topological space in which exactly one of the two singleton subsets is open, then continuous maps from a space $B$ into $S$ correspond naturally to open subsets of $B$ (Exercise 4.1.30). Hence $\mathscr{O} \cong H_S$, and $\mathscr{O}$ is representable.

**Example 4.1.20** In Example 1.2.11, we defined a functor $C\colon \mathbf{Top}^{\mathrm{op}} \to \mathbf{Ring}$, assigning to each space the ring of continuous real-valued functions on it. The composite functor

$$
\mathbf{Top}^{\mathrm{op}} \xrightarrow{C} \mathbf{Ring} \xrightarrow{U} \mathbf{Set}
$$

is representable, since by definition, $U(C(X)) = \mathbf{Top}(X, \mathbb{R})$ for topological spaces $X$.

Previously, we assembled the covariant representables $(H^A)_{A \in \mathscr{A}}$ into one big functor $H^\bullet$. We now do the same for the contravariant representables $(H_A)_{A \in \mathscr{A}}$.

<span class="original-page-anchor" id="pdf-page-99" aria-hidden="true"></span>

Any map $A \xrightarrow{f} A'$ in $\mathscr{A}$ induces a natural transformation

![Natural transformation from H_A to H_A′](/library/volume-87/diagrams/pdf-0099-natural-transformation.png)

(also called $\mathscr{A}(-,f)$, $f_*$ or $f \circ -$), whose component at an object $B \in \mathscr{A}$ is

$$
\begin{array}{ccc}
H_A(B) = \mathscr{A}(B,A) & \to & H_{A'}(B) = \mathscr{A}(B,A') \\
p & \mapsto & f \circ p.
\end{array}
$$

**Definition 4.1.21** Let $\mathscr{A}$ be a locally small category. The **Yoneda embedding** of $\mathscr{A}$ is the functor

$$
H_\bullet\colon \mathscr{A} \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]
$$

defined on objects $A$ by $H_\bullet(A) = H_A$ and on maps $f$ by $H_\bullet(f) = H_f$.

Here is a summary of the definitions so far.

For each $A \in \mathscr{A}$, we have a functor $\mathscr{A} \xrightarrow{H^A} \mathbf{Set}$. Putting them all together gives a functor $\mathscr{A}^{\mathrm{op}} \xrightarrow{H^\bullet} [\mathscr{A},\mathbf{Set}]$.

For each $A \in \mathscr{A}$, we have a functor $\mathscr{A}^{\mathrm{op}} \xrightarrow{H_A} \mathbf{Set}$. Putting them all together gives a functor $\mathscr{A} \xrightarrow{H_\bullet} [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$.

The second pair of functors is the dual of the first. Both involve contravariance; it cannot be avoided.

In the theory of representable functors, it does not make much difference whether we work with the first or the second pair. Any theorem that we prove about one dualizes to give a theorem about the other. We choose to work with the second pair, the $H_A$s and $H_\bullet$. In a sense to be explained, $H_\bullet$ ‘embeds’ $\mathscr{A}$ into $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$. This can be useful, because the category $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ has some good properties that $\mathscr{A}$ might not have.

Exercise 4.1.27 asks you to prove that $H_\bullet$ is injective on isomorphism classes of objects. It is strongly recommended that you do it before reading on, as it encapsulates the key ideas of the rest of this chapter.

There is one more functor to define. It unifies the first and second pairs of functors shown above.

**Definition 4.1.22** Let $\mathscr{A}$ be a locally small category. The functor

$$
\operatorname{Hom}_{\mathscr{A}}\colon \mathscr{A}^{\mathrm{op}} \times \mathscr{A} \to \mathbf{Set}
$$

<span class="original-page-anchor" id="pdf-page-100" aria-hidden="true"></span>

is defined by

![Action of the Hom functor on objects and maps](/library/volume-87/diagrams/pdf-0100-hom-functor-action.png)

In other words, $\operatorname{Hom}_{\mathscr{A}}(A,B) = \mathscr{A}(A,B)$ and $(\operatorname{Hom}_{\mathscr{A}}(f,g))(p) = g \circ p \circ f$, whenever $A' \xrightarrow{f} A \xrightarrow{p} B \xrightarrow{g} B'$.

**Remarks 4.1.23** (a) The existence of the functor $\operatorname{Hom}_{\mathscr{A}}$ is something like the fact that for a metric space $(X,d)$, the metric is itself a continuous map $d\colon X \times X \to \mathbb{R}$. (If we take two points and move each one slightly, the distance between them changes only slightly.)

(b) In terms of Exercise 1.2.25, $\operatorname{Hom}_{\mathscr{A}}$ is the functor $\mathscr{A}^{\mathrm{op}} \times \mathscr{A} \to \mathbf{Set}$ corresponding to the families of functors $(H^A)_{A \in \mathscr{A}}$ and $(H_B)_{B \in \mathscr{A}}$.

(c) In Example 2.1.6, we saw that for any set $B$, there is an adjunction $(- \times B) \dashv (-)^B$ of functors $\mathbf{Set} \to \mathbf{Set}$. Similarly, for any category $\mathscr{B}$, there is an adjunction $(- \times \mathscr{B}) \dashv [\mathscr{B},-]$ of functors $\mathbf{CAT} \to \mathbf{CAT}$; in other words, there is a canonical bijection

$$
\mathbf{CAT}(\mathscr{A} \times \mathscr{B},\mathscr{C}) \cong \mathbf{CAT}(\mathscr{A},[\mathscr{B},\mathscr{C}])
$$

for $\mathscr{A},\mathscr{B},\mathscr{C} \in \mathbf{CAT}$. Under this bijection, the functors

$$
\operatorname{Hom}_{\mathscr{A}}\colon \mathscr{A}^{\mathrm{op}} \times \mathscr{A} \to \mathbf{Set},\qquad H^\bullet\colon \mathscr{A}^{\mathrm{op}} \to [\mathscr{A},\mathbf{Set}]
$$

correspond to one another. Thus, $\operatorname{Hom}_{\mathscr{A}}$ carries the same information as $H^\bullet$ (or $H_\bullet$), presented slightly differently.

**Remark 4.1.24** We can now explain the naturality in the definition of adjunction (Definition 2.1.1). Take categories and functors

![The functors F and G between A and B](/library/volume-87/diagrams/pdf-0100-functors-fg.png)

They give rise to functors

![Functor square for naturality of an adjunction](/library/volume-87/diagrams/pdf-0100-adjunction-naturality.png)

The composite functor $\downarrow\!\rightarrow$ sends $(A,B)$ to $\mathscr{B}(F(A),B)$; it can be written as $\mathscr{B}(F(-),-)$. The composite $\rightarrow\!\downarrow$ sends $(A,B)$ to $\mathscr{A}(A,G(B))$. Exercise 4.1.32 asks you to show that these two functors

$$
\mathscr{B}(F(-),-),\ \mathscr{A}(-,G(-))\colon \mathscr{A}^{\mathrm{op}} \times \mathscr{B} \to \mathbf{Set}
$$

<span class="original-page-anchor" id="pdf-page-101" aria-hidden="true"></span>

are naturally isomorphic if and only if $F$ and $G$ are adjoint. This justifies the claim in Remark 2.1.2(a): the naturality requirements (2.2) and (2.3) in the definition of adjunction simply assert that two particular functors are naturally isomorphic.

Objects of an arbitrary category do not have elements in any obvious sense. However, *sets* certainly have elements, and we have observed that an element of a set $A$ is the same thing as a map $1 \to A$. This inspires the following definition.

**Definition 4.1.25** Let $A$ be an object of a category. A **generalized element** of $A$ is a map with codomain $A$. A map $S \to A$ is a generalized element of $A$ of **shape $S$**.

‘Generalized element’ is nothing more than a synonym of ‘map’, but sometimes it is useful to think of maps as generalized elements.

For example, when $A$ is a set, a generalized element of $A$ of shape $1$ is an ordinary element of $A$, and a generalized element of $A$ of shape $\mathbb{N}$ is a sequence in $A$. In the category of topological spaces, the generalized elements of shape $1$ (the one-point space) are the points, and the generalized elements of shape $S^1$ (the circle) are, by definition, loops. As this suggests, in categories of geometric objects, we might equally well say ‘figures of shape $S$’.

In algebra, we are often interested in solutions to equations such as $x^2+y^2=1$. Perhaps we begin by being particularly interested in solutions in $\mathbb{Q}$, but then realize that in order to study rational solutions, it will be helpful to study solutions in other rings first. (This is often a fruitful strategy.) Given a ring $A$, a pair $(a,b) \in A \times A$ satisfying $a^2+b^2=1$ amounts to a homomorphism of rings

$$
\mathbb{Z}[x,y]/(x^2+y^2-1) \to A.
$$

Thus, the solutions to our equation (in any ring) can be seen as the generalized elements of shape $\mathbb{Z}[x,y]/(x^2+y^2-1)$.

For an object $S$ of a category $\mathscr{A}$, the functor

$$
H^S\colon \mathscr{A} \to \mathbf{Set}
$$

sends an object to its set of generalized elements of shape $S$. The functoriality tells us that any map $A \to B$ in $\mathscr{A}$ transforms $S$-elements of $A$ into $S$-elements of $B$. For example, taking $\mathscr{A} = \mathbf{Top}$ and $S = S^1$, any continuous map $A \to B$ transforms loops in $A$ into loops in $B$.

### Exercises

**4.1.26** Find three examples of representable functors not mentioned above.

<span class="original-page-anchor" id="pdf-page-102" aria-hidden="true"></span>

**4.1.27** Let $\mathscr{A}$ be a locally small category, and let $A,A' \in \mathscr{A}$ with $H_A \cong H_{A'}$. Prove directly that $A \cong A'$.

**4.1.28** Let $p$ be a prime number. Show that the functor $U_p\colon \mathbf{Grp} \to \mathbf{Set}$ defined in Example 4.1.5 is isomorphic to $\mathbf{Grp}(\mathbb{Z}/p\mathbb{Z},-)$. (To check that there is an isomorphism of functors – that is, a natural isomorphism – you will first need to define $U_p$ on maps. There is only one sensible way to do this.)

**4.1.29** Using the result of Exercise 0.13(a), prove that the forgetful functor $\mathbf{CRing} \to \mathbf{Set}$ is isomorphic to $\mathbf{CRing}(\mathbb{Z}[x],-)$, as in Example 4.1.14.

**4.1.30** The **Sierpiński space** is the two-point topological space $S$ in which one of the singleton subsets is open but the other is not. Prove that for any topological space $X$, there is a canonical bijection between the open subsets of $X$ and the continuous maps $X \to S$. Use this to show that the functor $\mathscr{O}\colon \mathbf{Top}^{\mathrm{op}} \to \mathbf{Set}$ of Example 4.1.19 is represented by $S$.

**4.1.31** Let $M\colon \mathbf{Cat} \to \mathbf{Set}$ be the functor that sends a small category $\mathscr{A}$ to the set of all maps in $\mathscr{A}$. Prove that $M$ is representable.

**4.1.32** Take locally small categories $\mathscr{A}$ and $\mathscr{B}$, and functors

![Functors F and G](/library/volume-87/diagrams/pdf-0102-functors-fg.png)

Show that $F$ is left adjoint to $G$ if and only if the two functors

$$
\mathscr{B}(F(-),-),\ \mathscr{A}(-,G(-))\colon \mathscr{A}^{\mathrm{op}} \times \mathscr{B} \to \mathbf{Set}
$$

of Remark 4.1.24 are naturally isomorphic. (Hint: this is made easier by using either Exercise 1.3.29 or Exercise 2.1.14.)

## 4.2 The Yoneda lemma

What do representables see?

Recall from Definition 1.2.15 that functors $\mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$ are sometimes called ‘presheaves’ on $\mathscr{A}$. So for each $A \in \mathscr{A}$ we have a representable presheaf $H_A$, and we are asking how the rest of the presheaf category $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ looks from the viewpoint of $H_A$. In other words, if $X$ is another presheaf, what are the maps $H_A \to X$?

Newcomers to category theory commonly find that the material presented in this section is where they first get stuck. Typically, the core of the difficulty is in understanding the question just asked. Let us ask it again.

We start by fixing a locally small category $\mathscr{A}$. We then take an object $A \in \mathscr{A}$ and a functor $X\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$. The object $A$ gives rise to another functor <span class="original-page-anchor" id="pdf-page-103" aria-hidden="true"></span>$H_A = \mathscr{A}(-,A)\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$. The question is: what are the maps $H_A \to X$? Since $H_A$ and $X$ are both objects of the presheaf category $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$, the ‘maps’ concerned are maps in $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$. So, we are asking what natural transformations

![Natural transformations from H_A to X](/library/volume-87/diagrams/pdf-0103-yoneda-question.png)

(4.1)

there are. The set of such natural transformations is called

$$
[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X).
$$

(This is a special case of the notation $\mathscr{B}(B,B')$ for the set of maps $B \to B'$ in a category $\mathscr{B}$. Here, $\mathscr{B} = [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$, $B = H_A$, and $B' = X$.) We want to know what this set is.

There is an informal principle of general category theory that allows us to guess the answer. Look back at Remarks 1.1.2(b), 1.2.2(a) and 1.3.2(a) on the definitions of category, functor and natural transformation. Each remark is of the form ‘from input of one type, it is possible to construct exactly one output of another type’. For example, in Remark 1.1.2(b), the input is a sequence of maps $A_0 \xrightarrow{f_1} \cdots \xrightarrow{f_n} A_n$, the output is a map $A_0 \to A_n$, and the statement is that no matter what we do with the input data $f_1,\ldots,f_n$, there is only one map $A_0 \to A_n$ that we can construct.

Let us apply this principle to our question. We have just seen how, given as input an object $A \in \mathscr{A}$ and a presheaf $X$ on $\mathscr{A}$, we can construct a set, namely, $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X)$. Are there any other ways to construct a set from the same input data $(A,X)$? Yes: simply take the set $X(A)$! The informal principle suggests that these two sets are the same:

$$
[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X) \cong X(A) \tag{4.2}
$$

for all $A \in \mathscr{A}$ and $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$. This turns out to be true; and that is the Yoneda lemma.

Informally, then, the Yoneda lemma says that for any $A \in \mathscr{A}$ and presheaf $X$ on $\mathscr{A}$:

> *A natural transformation $H_A \to X$ is an element of $X(A)$.*

Here is the formal statement. The proof follows shortly.

**Theorem 4.2.1 (Yoneda)** Let $\mathscr{A}$ be a locally small category. Then

$$
[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X) \cong X(A) \tag{4.3}
$$

naturally in $A \in \mathscr{A}$ and $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$.

<span class="original-page-anchor" id="pdf-page-104" aria-hidden="true"></span>

This is exactly what was stated in (4.2), except that the word ‘naturally’ has appeared. Recall from Definition 1.3.12 that for functors $F,G\colon \mathscr{C} \to \mathscr{D}$, the phrase ‘$F(C) \cong G(C)$ naturally in $C$’ means that there is a natural isomorphism $F \cong G$. So the use of this phrase in the Yoneda lemma suggests that each side of (4.3) is functorial in both $A$ and $X$. This means, for instance, that a map $X \to X'$ must induce a map

$$
[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X) \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X'),
$$

and that not only does the isomorphism (4.3) hold for *every* $A$ and $X$, but also, the isomorphisms can be chosen in a way that is compatible with these induced maps. Precisely, the Yoneda lemma states that the composite functor

![The composite functor in the Yoneda lemma](/library/volume-87/diagrams/pdf-0104-yoneda-composite-functor.png)

is naturally isomorphic to the evaluation functor

$$
\begin{array}{ccc}
\mathscr{A}^{\mathrm{op}} \times [\mathscr{A}^{\mathrm{op}},\mathbf{Set}] & \to & \mathbf{Set} \\
(A,X) & \mapsto & X(A).
\end{array}
$$

If the Yoneda lemma were false then the world would look much more complex. For take a presheaf $X\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$, and define a new presheaf $X'$ by

$$
X' = [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_\bullet,X)\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set},
$$

that is, $X'(A) = [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X)$ for all $A \in \mathscr{A}$. Yoneda tells us that $X'(A) \cong X(A)$ naturally in $A$; in other words, $X' \cong X$. If Yoneda were false then starting from a single presheaf $X$, we could build an infinite sequence $X,X',X'',\ldots$ of new presheaves, potentially all different. But in reality, the situation is very simple: they are all the same.

The proof of the Yoneda lemma is the longest proof so far. Nevertheless, there is essentially only one way to proceed at each stage. If you suspect that you are one of those newcomers to category theory for whom the Yoneda lemma presents the first serious challenge, an excellent exercise is to work out the proof before reading it. No ingenuity is required, only an understanding of all the terms in the statement.

**Proof of the Yoneda lemma** We have to define, for each $A$ and $X$, a bijection between the sets $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,X)$ and $X(A)$. We then have to show that our bijection is natural in $A$ and $X$.

<span class="original-page-anchor" id="pdf-page-105" aria-hidden="true"></span>

First, fix $A \in \mathscr{A}$ and $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$. We define functions

![The two functions in the Yoneda bijection](/library/volume-87/diagrams/pdf-0105-yoneda-inverse-functions.png)

(4.4)

and show that they are mutually inverse. So we have to do four things: define the function $\hat{(\ )}$, define the function $\tilde{(\ )}$, show that $\widehat{\tilde{(\ )}}$ is the identity, and show that $\widetilde{\hat{(\ )}}$ is the identity.

- Given $\alpha\colon H_A \to X$, define $\hat{\alpha} \in X(A)$ by $\hat{\alpha} = \alpha_A(1_A)$. (How else could we possibly define it?)

- Let $x \in X(A)$. We have to define a natural transformation $\tilde{x}\colon H_A \to X$. That is, we have to define for each $B \in \mathscr{A}$ a function

$$
\tilde{x}_B\colon H_A(B) = \mathscr{A}(B,A) \to X(B)
$$

and show that the family $\tilde{x} = (\tilde{x}_B)_{B \in \mathscr{A}}$ satisfies naturality.

Given $B \in \mathscr{A}$ and $f \in \mathscr{A}(B,A)$, define

$$
\tilde{x}_B(f) = (X(f))(x) \in X(B).
$$

(How else could we possibly define it?) This makes sense, since $X(f)$ is a map $X(A) \to X(B)$. To prove naturality, we must show that for any map $B' \xrightarrow{g} B$ in $\mathscr{A}$, the square

![Naturality square for x̃](/library/volume-87/diagrams/pdf-0105-yoneda-naturality-square.png)

commutes. To reduce clutter, let us write $X(g)$ as $Xg$, and so on. Now for all $f \in \mathscr{A}(B,A)$, we have

![The corresponding element calculation](/library/volume-87/diagrams/pdf-0105-yoneda-naturality-elements.png)

and $X(f \circ g) = (Xg) \circ (Xf)$ by functoriality, so the square does commute.

- Given $x \in X(A)$, we have to show that $\widehat{\tilde{x}} = x$, and indeed,

$$
\widehat{\tilde{x}} = \tilde{x}_A(1_A) = (X1_A)(x) = 1_{X(A)}(x) = x.
$$

<span class="original-page-anchor" id="pdf-page-106" aria-hidden="true"></span>

- Given $\alpha\colon H_A \to X$, we have to show that $\widetilde{\hat{\alpha}} = \alpha$. Two natural transformations are equal if and only if all their components are equal; so, we have to show that $\bigl(\widetilde{\hat{\alpha}}\bigr)_B = \alpha_B$ for all $B \in \mathscr{A}$. Each side of this equation is a function from $H_A(B) = \mathscr{A}(B,A)$ to $X(B)$, and two functions are equal if and only if they take equal values at every element of the domain; so, we have to show that

$$
\bigl(\widetilde{\hat{\alpha}}\bigr)_B(f) = \alpha_B(f)
$$

for all $B \in \mathscr{A}$ and $f\colon B \to A$ in $\mathscr{A}$. The left-hand side is by definition

$$
\bigl(\widetilde{\hat{\alpha}}\bigr)_B(f) = (Xf)(\hat{\alpha}) = (Xf)(\alpha_A(1_A)),
$$

so it remains to prove that

$$
(Xf)(\alpha_A(1_A)) = \alpha_B(f). \tag{4.5}
$$

By naturality of $\alpha$ (the only tool at our disposal), the square

![Naturality square used to recover α](/library/volume-87/diagrams/pdf-0106-recover-transformation.png)

commutes, which when taken at $1_A \in \mathscr{A}(A,A)$ gives equation (4.5).

(The proof is not over yet, but it is worth pausing to consider the significance of the fact that $\widetilde{\hat{\alpha}} = \alpha$. Since $\hat{\alpha}$ is the value of $\alpha$ at $1_A$, this implies:

> *A natural transformation $H_A \to X$ is determined by its value at $1_A$.*

Just *how* a natural transformation $H_A \to X$ is determined by its value at $1_A$ is described in equation (4.5).)

This establishes the bijection (4.4) for each $A \in \mathscr{A}$ and $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$. We now show that the bijection is natural in $A$ and $X$.

We employ two mildly labour-saving devices. First, in principle we have to prove naturality of both $\hat{(\ )}$ and $\tilde{(\ )}$, but by Lemma 1.3.11, it is enough to prove naturality of just one of them. We prove naturality of $\hat{(\ )}$. Second, by Exercise 1.3.29, $\hat{(\ )}$ is natural in the pair $(A,X)$ if and only if it is natural in $A$ for each fixed $X$ and natural in $X$ for each fixed $A$. So, it remains to check these two types of naturality.

Naturality in $A$ states that for each $X \in [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ and $B \xrightarrow{f} A$ in $\mathscr{A}$, the <span class="original-page-anchor" id="pdf-page-107" aria-hidden="true"></span>square

![Naturality in A](/library/volume-87/diagrams/pdf-0107-naturality-in-a-square.png)

commutes. For $\alpha\colon H_A \to X$, we have

![Element calculation for naturality in A](/library/volume-87/diagrams/pdf-0107-naturality-in-a-elements.png)

so we have to show that $(\alpha \circ H_f)_B(1_B) = (Xf)(\alpha_A(1_A))$. Indeed,

$$
\begin{aligned}
(\alpha \circ H_f)_B(1_B) &= \alpha_B((H_f)_B(1_B)) \\
&= \alpha_B(f \circ 1_B) = \alpha_B(f) \\
&= (Xf)(\alpha_A(1_A)),
\end{aligned}
$$

where the first step is by definition of composition in $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$, the second is by definition of $H_f$, and the last is by equation (4.5).

Naturality in $X$ states that for each $A \in \mathscr{A}$ and map

![The natural transformation θ](/library/volume-87/diagrams/pdf-0107-theta-transformation.png)

in $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$, the square

![Naturality in X](/library/volume-87/diagrams/pdf-0107-naturality-in-x-square.png)

commutes. For $\alpha\colon H_A \to X$, we have

![Element calculation for naturality in X](/library/volume-87/diagrams/pdf-0107-naturality-in-x-elements.png)

and $(\theta \circ \alpha)_A = \theta_A \circ \alpha_A$ by definition of composition in $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$, so the square does commute. This completes the proof. $\square$

<span class="original-page-anchor" id="pdf-page-108" aria-hidden="true"></span>

### Exercises

**4.2.2** State the dual of the Yoneda lemma.

**4.2.3** One way to understand the Yoneda lemma is to examine some special cases. Here we consider one-object categories.

Let $M$ be a monoid. The underlying set of $M$ can be given a right $M$-action by multiplication: $x \cdot m = xm$ for all $x,m \in M$. This $M$-set is called the **right regular representation** of $M$. Let us write it as $\underline{M}$.

(a) When $M$ is regarded as a one-object category, functors $M^{\mathrm{op}} \to \mathbf{Set}$ correspond to right $M$-sets (Example 1.2.14). Show that the $M$-set corresponding to the unique representable functor $M^{\mathrm{op}} \to \mathbf{Set}$ is the right regular representation.

(b) Now let $X$ be any right $M$-set. Show that for each $x \in X$, there is a unique map $\alpha\colon \underline{M} \to X$ of right $M$-sets such that $\alpha(1) = x$. Deduce that there is a bijection between $\{\text{maps }\underline{M} \to X\text{ of right }M\text{-sets}\}$ and $X$.

(c) Deduce the Yoneda lemma for one-object categories.

## 4.3 Consequences of the Yoneda lemma

The Yoneda lemma is fundamental in category theory. Here we look at three important consequences.

**Notation 4.3.1** An arrow decorated with a $\sim$, as in $A \xrightarrow{\sim} B$, denotes an isomorphism.

### A representation is a universal element

**Corollary 4.3.2** Let $\mathscr{A}$ be a locally small category and $X\colon \mathscr{A}^{\mathrm{op}} \to \mathbf{Set}$. Then a representation of $X$ consists of an object $A \in \mathscr{A}$ together with an element $u \in X(A)$ such that:

> for each $B \in \mathscr{A}$ and $x \in X(B)$, there is a unique map $\bar{x}\colon B \to A$ such that $(X\bar{x})(u) = x$. (4.6)

To clarify the statement, first recall that by definition, a representation of $X$ is an object $A \in \mathscr{A}$ together with a natural isomorphism $\alpha\colon H_A \xrightarrow{\sim} X$. Corollary 4.3.2 states that such pairs $(A,\alpha)$ are in natural bijection with pairs $(A,u)$ satisfying condition (4.6).

Pairs $(B,x)$ with $B \in \mathscr{A}$ and $x \in X(B)$ are sometimes called **elements** of the presheaf $X$. (Indeed, the Yoneda lemma tells us that $x$ amounts to a generalized element of $X$ of shape $H_B$.) An element $u$ satisfying condition (4.6) <span class="original-page-anchor" id="pdf-page-109" aria-hidden="true"></span>is sometimes called a **universal** element of $X$. So, Corollary 4.3.2 says that a representation of a presheaf $X$ amounts to a universal element of $X$.

**Proof** By the Yoneda lemma, we have only to show that for $A \in \mathscr{A}$ and $u \in X(A)$, the natural transformation $\tilde{u}\colon H_A \to X$ is an isomorphism if and only if (4.6) holds. (Here we are using the notation introduced in the proof of the Yoneda lemma.) Now, $\tilde{u}$ is an isomorphism if and only if for all $B \in \mathscr{A}$, the function

$$
\tilde{u}_B\colon H_A(B) = \mathscr{A}(B,A) \to X(B)
$$

is a bijection, if and only if for all $B \in \mathscr{A}$ and $x \in X(B)$, there is a unique $\bar{x} \in \mathscr{A}(B,A)$ such that $\tilde{u}_B(\bar{x}) = x$. But $\tilde{u}_B(\bar{x}) = (X\bar{x})(u)$, so this is exactly condition (4.6). $\square$

Our examples will use the dual form, for covariant set-valued functors:

**Corollary 4.3.3** Let $\mathscr{A}$ be a locally small category and $X\colon \mathscr{A} \to \mathbf{Set}$. Then a representation of $X$ consists of an object $A \in \mathscr{A}$ together with an element $u \in X(A)$ such that:

> for each $B \in \mathscr{A}$ and $x \in X(B)$, there is a unique map $\bar{x}\colon A \to B$ such that $(X\bar{x})(u) = x$. (4.7)

**Proof** Follows immediately by duality. $\square$

**Example 4.3.4** Fix a set $S$ and consider the functor

$$
\begin{array}{cccc}
X = \mathbf{Set}(S,U(-))\colon & \mathbf{Vect}_k & \to & \mathbf{Set} \\
& V & \mapsto & \mathbf{Set}(S,U(V)).
\end{array}
$$

Here are two familiar (and true!) statements about $X$:

(a) there exist a vector space $F(S)$ and an isomorphism

$$
\mathbf{Vect}_k(F(S),V) \cong \mathbf{Set}(S,U(V)) \tag{4.8}
$$

natural in $V \in \mathbf{Vect}_k$ (Example 2.1.3(a));

(b) there exist a vector space $F(S)$ and a function $u\colon S \to U(F(S))$ such that:

> for each vector space $V$ and function $f\colon S \to U(V)$, there is a unique linear map $\bar{f}\colon F(S) \to V$ such that

![Universal property of the free vector space](/library/volume-87/diagrams/pdf-0109-free-vector-space-universal.png)

> commutes

<span class="original-page-anchor" id="pdf-page-110" aria-hidden="true"></span>

(as in the introduction to Section 2.3, where $u$ was called by its usual name, $\eta_S$).

Each of these two statements says that $X$ is representable. Statement (a) says that there is an isomorphism $X(V) \cong \mathbf{Vect}(F(S),V)$ natural in $V$, that is, an isomorphism $X \cong H^{F(S)}$. So $X$ is representable, by definition of representability. Statement (b) says that $u \in X(F(S))$ satisfies condition (4.7). So $X$ is representable, by Corollary 4.3.3.

You will have noticed that the first way of saying that $X$ is representable is substantially shorter than the second. Indeed, it is clear that if the situation of (b) holds then there is an isomorphism

$$
\mathbf{Vect}_k(F(S),V) \xrightarrow{\sim} \mathbf{Set}(S,U(V))
$$

natural in $V$, defined by $g \mapsto U(g) \circ u$. But it looks at first as if (b) says rather more than (a), since it states that the two functors are not only naturally isomorphic, but naturally isomorphic in a rather special way. Corollary 4.3.3 tells us that this is an illusion: all natural isomorphisms (4.8) arise in this way. It is the word ‘natural’ in (a) that hides the explicit detail.

**Example 4.3.5** The same can be said for any other adjunction

![An adjunction F ⊣ G](/library/volume-87/diagrams/pdf-0110-adjunction-fg.png)

Fix $A \in \mathscr{A}$ and put

$$
X = \mathscr{A}(A,G(-))\colon \mathscr{B} \to \mathbf{Set}.
$$

Then $X$ is representable, and this can be expressed in either of the following ways:

(a) $\mathscr{A}(A,G(B)) \cong \mathscr{B}(F(A),B)$ naturally in $B$; in other words, $X \cong H^{F(A)}$ (as in Lemma 4.1.10);

(b) the unit map $\eta_A\colon A \to G(F(A))$ is an initial object of the comma category $(A \Rightarrow G)$; that is, $\eta_A \in X(F(A))$ satisfies condition (4.7).

This observation can be developed into an alternative proof of Theorem 2.3.6, the reformulation of adjointness in terms of initial objects.

**Example 4.3.6** For any group $G$ and element $x \in G$, there is a unique homomorphism $\phi\colon \mathbb{Z} \to G$ such that $\phi(1) = x$. This means that $1 \in U(\mathbb{Z})$ is a universal element of the forgetful functor $U\colon \mathbf{Grp} \to \mathbf{Set}$; in other words, condition (4.7) holds when $\mathscr{A} = \mathbf{Grp}$, $X = U$, $A = \mathbb{Z}$ and $u = 1$. So $1 \in U(\mathbb{Z})$ gives a representation $H^{\mathbb{Z}} \xrightarrow{\sim} U$ of $U$.

On the other hand, the same is true with $-1$ in place of $1$. The isomorphisms <span class="original-page-anchor" id="pdf-page-111" aria-hidden="true"></span>$H^{\mathbb{Z}} \xrightarrow{\sim} U$ coming from $1$ and $-1$ are not equal, because Corollary 4.3.3 provides a *one-to-one* correspondence between universal elements and representations.

### The Yoneda embedding

Here is a second corollary of the Yoneda lemma.

**Corollary 4.3.7** For any locally small category $\mathscr{A}$, the Yoneda embedding

$$
H_\bullet\colon \mathscr{A} \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]
$$

is full and faithful.

Informally, this says that for $A,A' \in \mathscr{A}$, a map $H_A \to H_{A'}$ of presheaves is the same thing as a map $A \to A'$ in $\mathscr{A}$.

**Proof** We have to show that for each $A,A' \in \mathscr{A}$, the function

$$
\begin{array}{ccc}
\mathscr{A}(A,A') & \to & [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,H_{A'}) \\
f & \mapsto & H_f
\end{array} \tag{4.9}
$$

is bijective. By the Yoneda lemma (taking ‘$X$’ to be $H_{A'}$), the function

$$
\tilde{(\ )}\colon H_{A'}(A) \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}](H_A,H_{A'}) \tag{4.10}
$$

is bijective, so it is enough to prove that the functions (4.9) and (4.10) are equal. Thus, given $f\colon A \to A'$, we have to prove that $\tilde{f} = H_f$, or equivalently, $\widehat{H_f} = f$. And indeed,

$$
\widehat{H_f} = (H_f)_A(1_A) = f \circ 1_A = f,
$$

as required. $\square$

In mathematics at large, the word ‘embedding’ is used (sometimes informally) to mean a map $A \to B$ that makes $A$ isomorphic to its image in $B$. For example, an injection of sets $i\colon A \to B$ might be called an embedding, because it provides a bijection between $A$ and the subset $iA$ of $B$. Similarly, a map $i\colon A \to B$ of topological spaces might be called an embedding if it is a homeomorphism to its image, so that $A \cong iA$. Corollary 1.3.19 tells us that in category theory, a full and faithful functor $\mathscr{A} \to \mathscr{B}$ can reasonably be called an embedding, as it makes $\mathscr{A}$ equivalent to a full subcategory of $\mathscr{B}$.

In the case at hand, the Yoneda embedding $H_\bullet\colon \mathscr{A} \to [\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ embeds $\mathscr{A}$ into its own presheaf category (Figure 4.1). So, $\mathscr{A}$ is equivalent to the full subcategory of $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ whose objects are the representables.

<span class="original-page-anchor" id="pdf-page-112" aria-hidden="true"></span>

![A category embedded into its presheaf category](/library/volume-87/diagrams/pdf-0112-yoneda-embedding.png)

Figure 4.1 A category $\mathscr{A}$ embedded into its presheaf category.

In general, full subcategories are the easiest subcategories to handle. For instance, given objects $A$ and $A'$ of a full subcategory, we can speak unambiguously of the ‘maps’ from $A$ to $A'$; it makes no difference whether this is understood to mean maps in the subcategory or maps in the whole category. Similarly, we can speak unambiguously of isomorphism of objects of the subcategory, as in the following lemma.

**Lemma 4.3.8** Let $J\colon \mathscr{A} \to \mathscr{B}$ be a full and faithful functor and $A,A' \in \mathscr{A}$. Then:

(a) a map $f$ in $\mathscr{A}$ is an isomorphism if and only if the map $J(f)$ in $\mathscr{B}$ is an isomorphism;

(b) for any isomorphism $g\colon J(A) \to J(A')$ in $\mathscr{B}$, there is a unique isomorphism $f\colon A \to A'$ in $\mathscr{A}$ such that $J(f) = g$;

(c) the objects $A$ and $A'$ of $\mathscr{A}$ are isomorphic if and only if the objects $J(A)$ and $J(A')$ of $\mathscr{B}$ are isomorphic.

**Proof** Exercise 4.3.15. $\square$

**Example 4.3.9** In Example 4.3.6, we considered the representations of the forgetful functor $U\colon \mathbf{Grp} \to \mathbf{Set}$, and found two different isomorphisms $H^{\mathbb{Z}} \xrightarrow{\sim} U$. Did we find all of them?

Since $H^{\mathbb{Z}} \cong U$, there are as many isomorphisms $H^{\mathbb{Z}} \xrightarrow{\sim} U$ as there are isomorphisms $H^{\mathbb{Z}} \xrightarrow{\sim} H^{\mathbb{Z}}$. By Corollary 4.3.7 and Lemma 4.3.8(b), there are as many of *these* as there are group isomorphisms $\mathbb{Z} \xrightarrow{\sim} \mathbb{Z}$. There are precisely two such (corresponding to the two generators $\pm1$ of $\mathbb{Z}$), so we did indeed find all the isomorphisms $H^{\mathbb{Z}} \xrightarrow{\sim} U$. Differently put, there are exactly two universal elements of $U(\mathbb{Z})$.

In Section 6.2, we will see that every presheaf can be built from representables, in very roughly the same way that every positive integer can be built from primes.

<span class="original-page-anchor" id="pdf-page-113" aria-hidden="true"></span>

![Objects viewed from different viewpoints](/library/volume-87/diagrams/pdf-0113-objects-viewpoints.png)

Figure 4.2 If $\mathscr{A}(B,A) \cong \mathscr{A}(B,A')$ naturally in $B$, then $A \cong A'$.

### Isomorphism of representables

In Exercise 4.1.27, you were asked to prove directly that if $H_A \cong H_{A'}$ then $A \cong A'$. The proof contains all the main ideas in the proof of the Yoneda lemma. The result itself can also be deduced from the Yoneda lemma, as follows.

**Corollary 4.3.10** Let $\mathscr{A}$ be a locally small category and $A,A' \in \mathscr{A}$. Then

$$
H_A \cong H_{A'} \iff A \cong A' \iff H^A \cong H^{A'}.
$$

**Proof** By duality, it is enough to prove the first ‘$\Longleftrightarrow$’. This follows from Corollary 4.3.7 and Lemma 4.3.8(c). $\square$

Since functors always preserve isomorphism (Exercise 1.2.21), the force of this statement is that

$$
H_A \cong H_{A'} \implies A \cong A'.
$$

In other words, if $\mathscr{A}(B,A) \cong \mathscr{A}(B,A')$ naturally in $B$, then $A \cong A'$. Thinking of $\mathscr{A}(B,A)$ as ‘$A$ viewed from $B$’, the corollary tells us that two objects are the same if and only if they look the same from all viewpoints (Figure 4.2). (If it looks like a duck, walks like a duck, and quacks like a duck, then it probably is a duck.)

**Example 4.3.11** Consider Corollary 4.3.10 in the case $\mathscr{A} = \mathbf{Grp}$. Take two groups $A$ and $A'$, and suppose someone tells us that $A$ and $A'$ ‘look the same from $B$’ (meaning that $H_A(B) \cong H_{A'}(B)$) for all groups $B$. Then, for instance:

- $H_A(1) \cong H_{A'}(1)$, where $1$ is the trivial group. But $H_A(1) = \mathbf{Grp}(1,A)$ is a one-element set, as is $H_{A'}(1)$, no matter what $A$ and $A'$ are. So this tells us nothing at all.

- $H_A(\mathbb{Z}) \cong H_{A'}(\mathbb{Z})$. We know that $H_A(\mathbb{Z})$ is the underlying set of $A$, and similarly for $A'$. So $A$ and $A'$ have isomorphic underlying sets. But for all we know so far, they might have entirely different group structures.

<span class="original-page-anchor" id="pdf-page-114" aria-hidden="true"></span>

- $H_A(\mathbb{Z}/p\mathbb{Z}) \cong H_{A'}(\mathbb{Z}/p\mathbb{Z})$ for every prime $p$, so by Example 4.1.5, $A$ and $A'$ have the same number of elements of each prime order.

Each of these isomorphisms gives only partial information about the similarity of $A$ and $A'$. But if we know that $H_A(B) \cong H_{A'}(B)$ for all groups $B$, and *naturally* in $B$, then $A \cong A'$.

**Example 4.3.12** The category of sets is very unusual in this respect. For any set $A$, we have

$$
A \cong \mathbf{Set}(1,A)=H_A(1),
$$

so $H_A(1) \cong H_{A'}(1)$ implies $A \cong A'$. In other words, two objects of $\mathbf{Set}$ are the same if they look the same from the point of view of the one-element set. This is a familiar feature of sets: the only thing that matters about a set is its elements!

For a general category, Corollary 4.3.10 tells us that two objects are the same if they have the same generalized elements of all shapes. But the category of sets has a special property: if I choose an object and tell you only what its generalized elements of shape $1$ are, then you can deduce exactly what my object must be.

**Example 4.3.13** Let $G:\mathscr{B}\to\mathscr{A}$ be a functor, and suppose that both $F$ and $F'$ are left adjoint to $G$. Then for each $A\in\mathscr{A}$, we have

$$
\mathscr{B}(F(A),B)\cong\mathscr{A}(A,G(B))\cong\mathscr{B}(F'(A),B)
$$

naturally in $B\in\mathscr{B}$, so $H^{F(A)}\cong H^{F'(A)}$, so $F(A)\cong F'(A)$ by Corollary 4.3.10. In fact, this isomorphism is natural in $A$, so that $F\cong F'$. This shows that left adjoints are unique, as claimed in Remark 2.1.2(d). Dually, right adjoints are unique. See also Exercise 4.3.18.

**Example 4.3.14** Corollary 4.3.10 implies that if a set-valued functor is isomorphic to both $H^A$ and $H^{A'}$ then $A\cong A'$. So the functor *determines* the representing object, if one exists. For instance, take the functor

$$
\mathbf{Bilin}(U,V;-):\mathbf{Vect}_k\to\mathbf{Set}
$$

of Example 4.1.9. Corollary 4.3.10 implies that up to isomorphism, there is *at most one* vector space $T$ such that

$$
\mathbf{Bilin}(U,V;W)\cong\mathbf{Vect}_k(T,W)
$$

naturally in $W$. It can be shown that there does, in fact, exist such a vector space $T$. Since all such spaces $T$ are isomorphic, it is legitimate to refer to any of them as *the* tensor product of $U$ and $V$.

<span class="original-page-anchor" id="pdf-page-115" aria-hidden="true"></span>

### Exercises

**4.3.15** Prove Lemma 4.3.8.

**4.3.16** Let $\mathscr{A}$ be a locally small category. Prove each of the following statements directly (without using the Yoneda lemma).

(a) $H_\bullet:\mathscr{A}\to[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ is faithful.

(b) $H_\bullet$ is full.

(c) Given $A\in\mathscr{A}$ and a presheaf $X$ on $\mathscr{A}$, if $X(A)$ has an element $u$ that is universal in the sense of Corollary 4.3.2, then $X\cong H_A$.

**4.3.17** Interpret the theory of Chapter 4 in the case where the category $\mathscr{A}$ is discrete. For example, what do presheaves look like, and which ones are representable? What does the Yoneda lemma tell us? Does its proof become any shorter? What about the corollaries of the Yoneda lemma?

**4.3.18** Let $\mathscr{B}$ be a category and $J:\mathscr{C}\to\mathscr{D}$ a functor. There is an induced functor

$$
J\circ-:[\mathscr{B},\mathscr{C}]\to[\mathscr{B},\mathscr{D}]
$$

defined by composition with $J$.

(a) Show that if $J$ is full and faithful then so is $J\circ-$.

(b) Deduce that if $J$ is full and faithful and $G,G':\mathscr{B}\to\mathscr{C}$ with $J\circ G\cong J\circ G'$ then $G\cong G'$.

(c) Now deduce that right adjoints are unique: if $F:\mathscr{A}\to\mathscr{B}$ and $G,G':\mathscr{B}\to\mathscr{A}$ with $F\dashv G$ and $F\dashv G'$ then $G\cong G'$. (Hint: the Yoneda embedding is full and faithful.)
