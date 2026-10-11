---
title: "Adjoints, representables and limits"
description: "Tom Leinster《Basic Category Theory》English。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"Limits","link":"/library/volume-87/original-chapter-005"}
next: {"text":"Proof of the general adjoint functor theorem","link":"/library/volume-87/original-appendix"}
---

# Adjoints, representables and limits

<span class="original-page-anchor" id="pdf-page-150" aria-hidden="true"></span>

We have approached the idea of universal property from three different angles, producing three different formalisms: adjointness, representability, and limits. In this final chapter, we work out the connections between them.

In principle, anything that can be described in one of the three formalisms can also be described in the others. The situation is similar to that of cartesian and polar coordinates: anything that can be done in polar coordinates can in principle be done in cartesian coordinates, and vice versa, but some things are more gracefully done in one system than the other.

In comparing the three approaches, we will discover many of the fundamental results of category theory. Here are some highlights.

- Limits and colimits in functor categories work in the simplest possible way.
- The embedding of a category $\mathbf{A}$ into its presheaf category $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ preserves limits (but not colimits).
- The representables are the prime numbers of presheaves: every presheaf can be expressed canonically as a colimit of representables.
- A functor with a left adjoint preserves limits. Under suitable hypotheses, the converse holds too.
- Categories of presheaves $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ behave very much like the category of sets, the beginning of an incredible story that brings together the subjects of logic and geometry.

## 6.1 Limits in terms of representables and adjoints

There is more than one way to present the definition of limit. In Chapter 5, we used an explicit form of the definition that is particularly convenient for examples. But we will soon be developing the *theory* of limits and colimits, <span class="original-page-anchor" id="pdf-page-151" aria-hidden="true"></span>and for that, a rephrased form of the definition is useful. In fact, we rephrase it in two different ways: once in terms of representability, and once in terms of adjoints.

We begin by showing that cones are simply natural transformations of a special kind. To do this, we need some notation. Given categories $\mathbf{I}$ and $\mathscr{A}$ and an object $A\in\mathscr{A}$, there is a functor $\Delta A\colon\mathbf{I}\to\mathscr{A}$ with constant value $A$ on objects and $1_A$ on maps. This defines, for each $\mathbf{I}$ and $\mathscr{A}$, the **diagonal functor**

$$
\Delta\colon\mathscr{A}\to[\mathbf{I},\mathscr{A}].
$$

The name can be understood by considering the case in which $\mathbf{I}$ is the discrete category with two objects; then $[\mathbf{I},\mathscr{A}]=\mathscr{A}\times\mathscr{A}$ and $\Delta(A)=(A,A)$.

Now, given a diagram $D\colon\mathbf{I}\to\mathscr{A}$ and an object $A\in\mathscr{A}$, a cone on $D$ with vertex $A$ is simply a natural transformation

![A cone as a natural transformation](/library/volume-87/diagrams/pdf-0151-cone-transformation.png)

Writing $\operatorname{Cone}(A,D)$ for the set of cones on $D$ with vertex $A$, we therefore have

$$
\operatorname{Cone}(A,D)=[\mathbf{I},\mathscr{A}](\Delta A,D).\tag{6.1}
$$

Thus, $\operatorname{Cone}(A,D)$ is functorial in $A$ (contravariantly) and $D$ (covariantly).

Here is our first rephrasing of the definition of limit.

**Proposition 6.1.1** Let $\mathbf{I}$ be a small category, $\mathscr{A}$ a category, and $D\colon\mathbf{I}\to\mathscr{A}$ a diagram. Then there is a one-to-one correspondence between limit cones on $D$ and representations of the functor

$$
\operatorname{Cone}(-,D)\colon\mathscr{A}^{\mathrm{op}}\to\mathbf{Set},
$$

with the representing objects of $\operatorname{Cone}(-,D)$ being the limit objects (that is, the vertices of the limit cones) of $D$.

Briefly put: a limit of $D$ is a representation of $[\mathbf{I},\mathscr{A}](\Delta-,D)$.

**Proof** By Corollary 4.3.2, a representation of $\operatorname{Cone}(-,D)$ consists of a cone on $D$ with a certain universal property. This is exactly the universal property in the definition of limit cone. $\square$

The proposition formalizes the thought that cones on a diagram $D$ correspond one-to-one with maps into $\lim\limits_{\leftarrow\mathbf{I}}D$. It implies that if $D$ has a limit then

$$
\operatorname{Cone}(A,D)\cong\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\tag{6.2}
$$

<span class="original-page-anchor" id="pdf-page-152" aria-hidden="true"></span>

![Induced maps between limits](/library/volume-87/diagrams/pdf-0152-induced-maps.png)

Figure 6.1 Illustration of Lemma 6.1.3.

naturally in $A$. The correspondence is given from left to right by

$$
(f_I)_{I\in\mathbf{I}}\mapsto\bar f
$$

(in the notation of Definition 5.1.19), and from right to left by

$$
(p_I\circ g)_{I\in\mathbf{I}}\mathrel{\leftarrow\!\vert}g
$$

where $p_I\colon\lim\limits_{\leftarrow\mathbf{I}}D\to D(I)$ are the projections.

From Proposition 6.1.1 and Corollary 4.3.10 we deduce:

**Corollary 6.1.2** Limits are unique up to isomorphism. $\square$

The characterization (6.1) of cones suggests that we might consider varying the diagram $D$ as well as the vertex $A$. We are naturally led to ask questions such as: given a map $D\to D'$ between diagrams, is there an induced map between the limits of $D$ and $D'$? The answer is yes (Figure 6.1):

**Lemma 6.1.3** Let $\mathbf{I}$ be a small category and

![A natural transformation from D to D prime](/library/volume-87/diagrams/pdf-0152-natural-transformation.png)

a natural transformation. Let

$$
\biggl(\lim\limits_{\leftarrow\mathbf{I}}D\xrightarrow{p_I}D(I)\biggr)_{I\in\mathbf{I}}\qquad\text{and}\qquad\biggl(\lim\limits_{\leftarrow\mathbf{I}}D'\xrightarrow{p'_I}D'(I)\biggr)_{I\in\mathbf{I}}
$$

be limit cones. Then:

(a) there is a unique map $\lim\limits_{\leftarrow\mathbf{I}}\alpha\colon\lim\limits_{\leftarrow\mathbf{I}}D\to\lim\limits_{\leftarrow\mathbf{I}}D'$ such that for all $I\in\mathbf{I}$, the <span class="original-page-anchor" id="pdf-page-153" aria-hidden="true"></span>square

![The square defining the induced map between limits](/library/volume-87/diagrams/pdf-0153-limit-square.png)

commutes;

(b) given cones $\bigl(A\xrightarrow{f_I}D(I)\bigr)_{I\in\mathbf{I}}$ and $\bigl(A'\xrightarrow{f'_I}D'(I)\bigr)_{I\in\mathbf{I}}$ and a map $s\colon A\to A'$ such that

![A compatible map between cones](/library/volume-87/diagrams/pdf-0153-cone-square.png)

commutes for all $I\in\mathbf{I}$, the square

![The corresponding square between vertices and limits](/library/volume-87/diagrams/pdf-0153-induced-square.png)

also commutes.

**Proof** Part (a) follows immediately from the fact that $\bigl(\lim\limits_{\leftarrow\mathbf{I}}D\xrightarrow{\alpha_Ip_I}D'(I)\bigr)_{I\in\mathbf{I}}$ is a cone on $D'$. To prove (b), note that for each $I\in\mathbf{I}$, we have

$$
p'_I\circ\biggl(\lim\limits_{\leftarrow\mathbf{I}}\alpha\biggr)\circ\bar f=\alpha_I\circ p_I\circ\bar f=\alpha_I\circ f_I=f'_I\circ s=p'_I\circ\overline{f'}\circ s.
$$

So by Exercise 5.1.36(a), $\bigl(\lim\limits_{\leftarrow\mathbf{I}}\alpha\bigr)\circ\bar f=\overline{f'}\circ s$. $\square$

We can now give the second rephrasing of the definition of limit. It only applies when the category has *all* limits of the shape concerned.

**Proposition 6.1.4** Let $\mathbf{I}$ be a small category and $\mathscr{A}$ a category with all limits of shape $\mathbf{I}$. Then $\lim\limits_{\leftarrow\mathbf{I}}$ defines a functor $[\mathbf{I},\mathscr{A}]\to\mathscr{A}$, and this functor is right adjoint to the diagonal functor.

**Proof** Choose for each $D\in[\mathbf{I},\mathscr{A}]$ a limit cone on $D$, and call its vertex $\lim\limits_{\leftarrow\mathbf{I}}D$. For each map $\alpha\colon D\to D'$ in $[\mathbf{I},\mathscr{A}]$, we have a canonical map $\lim\limits_{\leftarrow\mathbf{I}}\alpha\colon$ <span class="original-page-anchor" id="pdf-page-154" aria-hidden="true"></span>$\lim\limits_{\leftarrow\mathbf{I}}D\to\lim\limits_{\leftarrow\mathbf{I}}D'$, defined as in Lemma 6.1.3(a). This makes $\lim\limits_{\leftarrow\mathbf{I}}$ into a functor. Proposition 6.1.1 implies that

$$
[\mathbf{I},\mathscr{A}](\Delta A,D)=\operatorname{Cone}(A,D)\cong\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)
$$

naturally in $A$, and taking $s=1_A$ in Lemma 6.1.3(b) tells us that the isomorphism is also natural in $D$. $\square$

To define the functor $\lim\limits_{\leftarrow\mathbf{I}}$, we had to *choose* for each $D$ a limit cone on $D$. This is a non-canonical choice. Nevertheless, different choices only affect the functor $\lim\limits_{\leftarrow\mathbf{I}}$ up to natural isomorphism, by uniqueness of adjoints.

### Exercises

**6.1.5** Interpret all the theory of this section in the special case where $\mathbf{I}$ is the discrete category with two objects.

**6.1.6** What is the content of Proposition 6.1.4 when $\mathbf{I}$ is a group and $\mathscr{A}=\mathbf{Set}$? What about the dual of Proposition 6.1.4?

## 6.2 Limits and colimits of presheaves

What do limits and colimits look like in functor categories $[\mathscr{A},\mathscr{B}]$? In particular, what do they look like in presheaf categories $[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$? More particularly still, what about limits and colimits of representables? Are they, too, representable?

We will answer all these questions. In order to do so, we first prove that representables preserve limits.

### Representables preserve limits

Let us begin by recalling that, by definition of product, a map $A\to X\times Y$ amounts to a pair of maps $(A\to X,A\to Y)$. Here $A$, $X$ and $Y$ are objects of a category $\mathscr{A}$ with binary products. There is, therefore, a bijection

$$
\mathscr{A}(A,X\times Y)\cong\mathscr{A}(A,X)\times\mathscr{A}(A,Y)\tag{6.3}
$$

natural in $A,X,Y\in\mathscr{A}$.

Is this a special feature of products, or does some analogous statement hold for every kind of limit? Let us try equalizers. Suppose that $\mathscr{A}$ has equalizers, <span class="original-page-anchor" id="pdf-page-155" aria-hidden="true"></span>and write

![Equalizer notation](/library/volume-87/diagrams/pdf-0155-equalizer-notation.png)

for the equalizer of maps $s$ and $t$. By definition of equalizer, maps

![Maps into the equalizer, equation 6.4](/library/volume-87/diagrams/pdf-0155-map-to-equalizer.png)

correspond one-to-one with maps $f\colon A\to X$ such that $s\circ f=t\circ f$. Now recall that $s$ induces a map

$$
s_* =\mathscr{A}(A,s)\colon\mathscr{A}(A,X)\to\mathscr{A}(A,Y),
$$

and similarly for $t$. In this notation, what we have just said is that maps (6.4) correspond one-to-one with elements $f\in\mathscr{A}(A,X)$ such that

$$
\bigl(\mathscr{A}(A,s)\bigr)(f)=\bigl(\mathscr{A}(A,t)\bigr)(f).
$$

By the explicit formula for equalizers in $\mathbf{Set}$ (Example 5.1.12), such an $f$ is exactly an element of the equalizer of $\mathscr{A}(A,s)$ and $\mathscr{A}(A,t)$. So, we have a canonical bijection

![The canonical bijection for equalizers, equation 6.5](/library/volume-87/diagrams/pdf-0155-equalizer-bijection.png)

This looks something like our isomorphism (6.3) for products.

The isomorphisms (6.3) and (6.5) suggest that, more generally, we might have

$$
\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\cong\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)\tag{6.6}
$$

naturally in $A\in\mathscr{A}$ and $D\in[\mathbf{I},\mathscr{A}]$, whenever $\mathscr{A}$ is a category with limits of shape $\mathbf{I}$. Here $\mathscr{A}(A,D)$ is the functor

$$
\begin{array}{rccc}
\mathscr{A}(A,D)\colon&\mathbf{I}&\to&\mathbf{Set}\\
&I&\mapsto&\mathscr{A}(A,D(I)).
\end{array}
$$

This functor could also be written as $\mathscr{A}(A,D(-))$, and is the composite

$$
\mathbf{I}\xrightarrow{D}\mathscr{A}\xrightarrow{\mathscr{A}(A,-)}\mathbf{Set}.
$$

The conjectured isomorphism (6.6) states, essentially, that representables preserve limits. We now set about proving this.

**Lemma 6.2.1** Let $\mathbf{I}$ be a small category, $\mathscr{A}$ a locally small category, $D\colon\mathbf{I}\to\mathscr{A}$ a diagram, and $A\in\mathscr{A}$. Then

$$
\operatorname{Cone}(A,D)\cong\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)
$$

naturally in $A$ and $D$.

<span class="original-page-anchor" id="pdf-page-156" aria-hidden="true"></span>

**Proof** Like all functors from a small category into $\mathbf{Set}$, the functor $\mathscr{A}(A,D)$ does have a limit, given by the explicit formula (5.16). According to this formula, $\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)$ is the set of all families $(f_I)_{I\in\mathbf{I}}$ such that $f_I\in\mathscr{A}(A,D(I))$ for all $I\in\mathbf{I}$ and

$$
(\mathscr{A}(A,Du))(f_I)=f_J\tag{6.7}
$$

for all $I\xrightarrow{u}J$ in $\mathbf{I}$. But equation (6.7) just says that $(Du)\circ f_I=f_J$, so an element of $\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)$ is nothing but a cone on $D$ with vertex $A$. $\square$

**Proposition 6.2.2 (Representables preserve limits)** Let $\mathscr{A}$ be a locally small category and $A\in\mathscr{A}$. Then $\mathscr{A}(A,-)\colon\mathscr{A}\to\mathbf{Set}$ preserves limits.

**Proof** Let $\mathbf{I}$ be a small category and let $D\colon\mathbf{I}\to\mathscr{A}$ be a diagram that has a limit. Then

$$
\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\cong\operatorname{Cone}(A,D)\cong\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D)
$$

naturally in $A$. Here the first isomorphism is Proposition 6.1.1 (or more particularly, the isomorphism (6.2) that follows it), and the second is Lemma 6.2.1. $\square$

**Remark 6.2.3** Proposition 6.2.2 tells us that

$$
\mathscr{A}\biggl(A,\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\cong\lim\limits_{\leftarrow\mathbf{I}}\mathscr{A}(A,D).\tag{6.8}
$$

To dualize Proposition 6.2.2, we replace $\mathscr{A}$ by $\mathscr{A}^{\mathrm{op}}$. Thus, $\mathscr{A}(-,A)\colon\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}$ preserves limits. A limit in $\mathscr{A}^{\mathrm{op}}$ is a colimit in $\mathscr{A}$, so $\mathscr{A}(-,A)$ transforms colimits in $\mathscr{A}$ into limits in $\mathbf{Set}$:

$$
\mathscr{A}\biggl(\lim\limits_{\rightarrow\mathbf{I}}D,A\biggr)\cong\lim\limits_{\leftarrow\mathbf{I}^{\mathrm{op}}}\mathscr{A}(D,A).\tag{6.9}
$$

The right-hand side is a *limit*, not a colimit! So even though (6.8) and (6.9) are dual statements, there are, in total, more limits than colimits involved. Somehow, limits have the upper hand.

For example, let $X$, $Y$ and $A$ be objects of a category $\mathscr{A}$, and suppose that the sum $X+Y$ exists. By definition of sum, a map $X+Y\to A$ amounts to a pair of maps $(X\to A,Y\to A)$. In other words, there is a canonical isomorphism

$$
\mathscr{A}(X+Y,A)\cong\mathscr{A}(X,A)\times\mathscr{A}(Y,A).
$$

This is the isomorphism (6.9) in the case where $\mathbf{I}$ is the discrete category with two objects.

<span class="original-page-anchor" id="pdf-page-157" aria-hidden="true"></span>

### Limits in functor categories

Earlier, we learned that it is sometimes useful to view functors as objects in their own right, rather than as maps of categories. For instance, when $G$ is a group, functors $G\to\mathbf{Set}$ are $G$-sets (Example 1.2.8), which one would usually regard as ‘things’ rather than ‘maps’. This point of view leads to the concept of functor category.

We now begin an analysis of limits and colimits in functor categories $[\mathbf{A},\mathscr{S}]$. Here $\mathbf{A}$ is small and $\mathscr{S}$ is locally small; these conditions together guarantee that $[\mathbf{A},\mathscr{S}]$ is locally small. The most important cases for us will be $\mathscr{S}=\mathbf{Set}$ and $\mathscr{S}=\mathbf{Set}^{\mathrm{op}}$. For that reason, we will assume whenever necessary that $\mathscr{S}$ has all limits and colimits.

We show that limits and colimits in $[\mathbf{A},\mathscr{S}]$ work in the simplest way imaginable. For instance, if $\mathscr{S}$ has binary products then so does $[\mathbf{A},\mathscr{S}]$, and the product of two functors $X,Y\colon\mathbf{A}\to\mathscr{S}$ is the functor $X\times Y\colon\mathbf{A}\to\mathscr{S}$ given by

$$
(X\times Y)(A)=X(A)\times Y(A)
$$

for all $A\in\mathbf{A}$.

**Notation 6.2.4** Let $\mathbf{A}$ and $\mathscr{S}$ be categories. For each $A\in\mathbf{A}$, there is a functor

$$
\begin{array}{rccc}
\operatorname{ev}_A\colon &[\mathbf{A},\mathscr{S}]&\to&\mathscr{S}\\
&X&\mapsto&X(A),
\end{array}
$$

called **evaluation** at $A$. We will be working with diagrams in $[\mathbf{A},\mathscr{S}]$, and given such a diagram $D\colon\mathbf{I}\to[\mathbf{A},\mathscr{S}]$, we have for each $A\in\mathbf{A}$ a functor

$$
\begin{array}{rccc}
\operatorname{ev}_A\circ D\colon &\mathbf{I}&\to&\mathscr{S}\\
&I&\mapsto&D(I)(A).
\end{array}
$$

We write $\operatorname{ev}_A\circ D$ as $D(-)(A)$.

**Theorem 6.2.5 (Limits in functor categories)** Let $\mathbf{A}$ and $\mathbf{I}$ be small categories and $\mathscr{S}$ a locally small category. Let $D\colon\mathbf{I}\to[\mathbf{A},\mathscr{S}]$ be a diagram, and suppose that for each $A\in\mathbf{A}$, the diagram $D(-)(A)\colon\mathbf{I}\to\mathscr{S}$ has a limit. Then there is a cone on $D$ whose image under $\operatorname{ev}_A$ is a limit cone on $D(-)(A)$ for each $A\in\mathbf{A}$. Moreover, any such cone on $D$ is a limit cone.

Theorem 6.2.5 is often expressed as a slogan:

*Limits in a functor category are computed pointwise.*

The ‘points’ in the word ‘pointwise’ are the objects of $\mathbf{A}$. The slogan means, for example, that given two functors $X,Y\in[\mathbf{A},\mathscr{S}]$, their product can be computed <span class="original-page-anchor" id="pdf-page-158" aria-hidden="true"></span>by first taking the product $X(A)\times Y(A)$ in $\mathscr{S}$ for each ‘point’ $A$, then assembling them to form a functor $X\times Y$.

Of course, Theorem 6.2.5 has a dual, stating that colimits in a functor category are also computed pointwise.

**Proof of Theorem 6.2.5** Take for each $A\in\mathbf{A}$ a limit cone

$$
\bigl(L(A)\xrightarrow{p_{I,A}}D(I)(A)\bigr)_{I\in\mathbf{I}}\tag{6.10}
$$

on the diagram $D(-)(A)\colon\mathbf{I}\to\mathscr{S}$. We prove two statements:

(a) there is exactly one way of extending $L$ to a functor on $\mathbf{A}$ with the property that $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ is a cone on $D$;

(b) this cone $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ is a limit cone.

The theorem will follow immediately.

For (a), take a map $f\colon A\to A'$ in $\mathbf{A}$. Lemma 6.1.3(a) applied to the natural transformation

![The natural transformation induced by f](/library/volume-87/diagrams/pdf-0158-parameter-transformation.png)

implies that there is a unique map $L(f)\colon L(A)\to L(A')$ such that for all $I\in\mathbf{I}$, the square

![The naturality square for the projections, equation 6.11](/library/volume-87/diagrams/pdf-0158-pointwise-square.png)

commutes. (This is our *definition* of $L(f)$.) We have now defined $L$ on objects and maps of $\mathbf{A}$. It is easy to check that $L$ preserves composition and identities, and is therefore a functor $L\colon\mathbf{A}\to\mathscr{S}$. Moreover, the commutativity of diagram (6.11) says exactly that for each $I\in\mathbf{I}$, the family $\bigl(L(A)\xrightarrow{p_{I,A}}D(I)(A)\bigr)_{A\in\mathbf{A}}$ is a natural transformation

![The projection as a natural transformation](/library/volume-87/diagrams/pdf-0158-projection-transformation.png)

So we have a family $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ of maps in $[\mathbf{A},\mathscr{S}]$, and from the fact that (6.10) is a cone on $D(-)(A)$ for each $A\in\mathbf{A}$, it follows immediately that $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ is a cone on $D$.

<span class="original-page-anchor" id="pdf-page-159" aria-hidden="true"></span>

For (b), let $X\in[\mathbf{A},\mathscr{S}]$ and let $\bigl(X\xrightarrow{q_I}D(I)\bigr)_{I\in\mathbf{I}}$ be a cone on $D$ in $[\mathbf{A},\mathscr{S}]$. For each $A\in\mathbf{A}$, we have a cone

$$
\bigl(X(A)\xrightarrow{q_{I,A}}D(I)(A)\bigr)_{I\in\mathbf{I}}
$$

on $D(-)(A)$ in $\mathscr{S}$, so there is a unique map $\bar q_A\colon X(A)\to L(A)$ such that $p_{I,A}\circ\bar q_A=q_{I,A}$ for all $I\in\mathbf{I}$. It only remains to prove that $\bar q_A$ is natural in $A$, and that follows from Lemma 6.1.3(b). $\square$

Theorem 6.2.5 has many important consequences. We begin by recording a cruder form of the theorem (and its dual), which we will use repeatedly.

**Corollary 6.2.6** Let $\mathbf{I}$ and $\mathbf{A}$ be small categories, and $\mathscr{S}$ a locally small category. If $\mathscr{S}$ has all limits (respectively, colimits) of shape $\mathbf{I}$ then so does $[\mathbf{A},\mathscr{S}]$, and for each $A\in\mathbf{A}$, the evaluation functor $\operatorname{ev}_A\colon[\mathbf{A},\mathscr{S}]\to\mathscr{S}$ preserves them. $\square$

**Warning 6.2.7** If $\mathscr{S}$ does *not* have all limits of shape $\mathbf{I}$ then $[\mathbf{A},\mathscr{S}]$ may contain limits of shape $\mathbf{I}$ that are not computed pointwise, that is, are not preserved by all the evaluation functors. Examples can be constructed, as in Section 3.3 of Kelly (1982).

Theorem 6.2.5 will also help us to prove that limits commute with limits, in the following sense. Take categories $\mathbf{I}$, $\mathbf{J}$ and $\mathscr{S}$. There are isomorphisms of categories

$$
[\mathbf{I},[\mathbf{J},\mathscr{S}]]\cong[\mathbf{I}\times\mathbf{J},\mathscr{S}]\cong[\mathbf{J},[\mathbf{I},\mathscr{S}]].
$$

(See Remark 4.1.23(c) and Exercise 1.2.25.) Under these isomorphisms, a functor $D\colon\mathbf{I}\times\mathbf{J}\to\mathscr{S}$ corresponds to the functors

$$
\begin{array}{rccc}
D^\bullet\colon&\mathbf{I}&\to&[\mathbf{J},\mathscr{S}]\\
&I&\mapsto&D(I,-)
\end{array}
\qquad\text{and}\qquad
\begin{array}{rccc}
D_\bullet\colon&\mathbf{J}&\to&[\mathbf{I},\mathscr{S}]\\
&J&\mapsto&D(-,J).
\end{array}
$$

Supposing that $\mathscr{S}$ has all limits, so do the various functor categories, by Corollary 6.2.6. In particular, there is an object $\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$ of $[\mathbf{J},\mathscr{S}]$. This is itself a diagram in $\mathscr{S}$, so we obtain in turn an object $\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$ of $\mathscr{S}$. Alternatively, we can take limits in the other order, producing an object $\lim\limits_{\leftarrow\mathbf{I}}\lim\limits_{\leftarrow\mathbf{J}}D_\bullet$ of $\mathscr{S}$. And there is a third possibility: taking the limit of $D$ itself, we obtain another object $\lim\limits_{\leftarrow\mathbf{I}\times\mathbf{J}}D$ of $\mathscr{S}$. The next result states that these three objects are the same. That is, it makes no difference what order we take limits in.

**Proposition 6.2.8 (Limits commute with limits)** Let $\mathbf{I}$ and $\mathbf{J}$ be small categories. Let $\mathscr{S}$ be a locally small category with limits of shape $\mathbf{I}$ and of shape <span class="original-page-anchor" id="pdf-page-160" aria-hidden="true"></span>$\mathbf{J}$. Then for all $D\colon\mathbf{I}\times\mathbf{J}\to\mathscr{S}$, we have

$$
\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet\cong\lim\limits_{\leftarrow\mathbf{I}\times\mathbf{J}}D\cong\lim\limits_{\leftarrow\mathbf{I}}\lim\limits_{\leftarrow\mathbf{J}}D_\bullet,
$$

and all these limits exist. In particular, $\mathscr{S}$ has limits of shape $\mathbf{I}\times\mathbf{J}$.

This is sometimes half-jokingly called Fubini’s theorem, as it is something like changing the order of integration in a double integral. The analogy is more appealing with *co*limits, since, like integrals, colimits can be thought of as a context-sensitive version of sums.

**Proof** By symmetry, it is enough to prove the first isomorphism. Since $\mathscr{S}$ has limits of shape $\mathbf{I}$, so does $[\mathbf{J},\mathscr{S}]$ (by Corollary 6.2.6). So $\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$ exists; it is an object of $[\mathbf{J},\mathscr{S}]$. Since $\mathscr{S}$ has limits of shape $\mathbf{J}$, $\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$ exists; it is an object of $\mathscr{S}$. Then for $S\in\mathscr{S}$,

$$
\begin{aligned}
\mathscr{S}\biggl(S,\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet\biggr)&\cong[\mathbf{J},\mathscr{S}]\biggl(\Delta S,\lim\limits_{\leftarrow\mathbf{I}}D^\bullet\biggr)\\
&\cong[\mathbf{I},[\mathbf{J},\mathscr{S}]](\Delta(\Delta S),D^\bullet)\\
&\cong[\mathbf{I}\times\mathbf{J},\mathscr{S}](\Delta S,D)
\end{aligned}
$$

naturally in $S$. The first two steps each follow from Proposition 6.1.1. The third uses the isomorphism $[\mathbf{I},[\mathbf{J},\mathscr{S}]]\cong[\mathbf{I}\times\mathbf{J},\mathscr{S}]$, under which $\Delta(\Delta S)$ corresponds to $\Delta S$ and $D^\bullet$ corresponds to $D$.

Hence $\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$ is a representing object for the functor $[\mathbf{I}\times\mathbf{J},\mathscr{S}](\Delta-,D)$. By Proposition 6.1.1 again, this says that $\lim\limits_{\leftarrow\mathbf{I}\times\mathbf{J}}D$ exists and is isomorphic to $\lim\limits_{\leftarrow\mathbf{J}}\lim\limits_{\leftarrow\mathbf{I}}D^\bullet$. $\square$

**Example 6.2.9** When $\mathbf{I}=\mathbf{J}=$ ![The discrete category with two objects](/library/volume-87/diagrams/pdf-0160-two-object-category.png), Proposition 6.2.8 says that binary products commute with binary products: if $\mathscr{S}$ has binary products and $S_{11},S_{12},S_{21},S_{22}\in\mathscr{S}$ then the 4-fold product $\prod_{i,j\in\{1,2\}}S_{ij}$ exists and satisfies

$$
(S_{11}\times S_{21})\times(S_{12}\times S_{22})\cong\prod_{i,j\in\{1,2\}}S_{ij}\cong(S_{11}\times S_{12})\times(S_{21}\times S_{22}).
$$

More generally, it makes no difference what order we write products in or where we put the brackets: there are canonical isomorphisms

$$
\begin{aligned}
S\times T&\cong T\times S,\\
(S\times T)\times U&\cong S\times(T\times U)
\end{aligned}
$$

in any category with binary products. If there is also a terminal object $1$, there are further canonical isomorphisms

$$
S\times1\cong S\cong1\times S.
$$

<span class="original-page-anchor" id="pdf-page-161" aria-hidden="true"></span>

**Warning 6.2.10** The dual of Proposition 6.2.8 states that colimits commute with colimits. For instance,

$$
(S_{11}+S_{21})+(S_{12}+S_{22})\cong(S_{11}+S_{12})+(S_{21}+S_{22})
$$

in any category $\mathscr{S}$ with binary sums. But limits do *not* in general commute with colimits. For instance, in general,

$$
(S_{11}+S_{21})\times(S_{12}+S_{22})\not\cong(S_{11}\times S_{12})+(S_{21}\times S_{22}).
$$

A counterexample is given by taking $\mathscr{S}=\mathbf{Set}$ and each $S_{ij}$ to be a one-element set. Then the left-hand side has $(1+1)\times(1+1)=4$ elements, whereas the right-hand side has $(1\times1)+(1\times1)=2$ elements.

Here are two further consequences of Theorem 6.2.5.

**Corollary 6.2.11** Let $\mathbf{A}$ be a small category. Then $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ has all limits and colimits, and for each $A\in\mathbf{A}$, the evaluation functor $\operatorname{ev}_A\colon[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]\to\mathbf{Set}$ preserves them.

**Proof** Since $\mathbf{Set}$ has all limits and colimits, this is immediate from Corollary 6.2.6. $\square$

**Corollary 6.2.12** The Yoneda embedding $H_\bullet\colon\mathbf{A}\to[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ preserves limits, for any small category $\mathbf{A}$.

**Proof** Let $D\colon\mathbf{I}\to\mathbf{A}$ be a diagram in $\mathbf{A}$, and let $\bigl(\lim\limits_{\leftarrow\mathbf{I}}D\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ be a limit cone. For each $A\in\mathbf{A}$, the composite functor

$$
\mathbf{A}\xrightarrow{H_\bullet}[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]\xrightarrow{\operatorname{ev}_A}\mathbf{Set}
$$

is $H^A$, which preserves limits (Proposition 6.2.2). So for each $A\in\mathbf{A}$,

$$
\biggl(\operatorname{ev}_AH_\bullet\biggl(\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\xrightarrow{\operatorname{ev}_AH_\bullet(p_I)}\operatorname{ev}_AH_\bullet(D(I))\biggr)_{I\in\mathbf{I}}
$$

is a limit cone. But then, by the ‘moreover’ part of Theorem 6.2.5 applied to the diagram $H_\bullet\circ D$ in $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$, the cone

$$
\biggl(H_\bullet\biggl(\lim\limits_{\leftarrow\mathbf{I}}D\biggr)\xrightarrow{H_\bullet(p_I)}H_\bullet(D(I))\biggr)_{I\in\mathbf{I}}
$$

is also a limit, as required. $\square$

**Example 6.2.13** Let $\mathbf{A}$ be a category with binary products. Corollary 6.2.12 implies that for all $X,Y\in\mathbf{A}$,

$$
H_{X\times Y}\cong H_X\times H_Y\tag{6.12}
$$

<span class="original-page-anchor" id="pdf-page-162" aria-hidden="true"></span>

in $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$. When evaluated at a particular object $A$, this says that

$$
\mathbf{A}(A,X\times Y)\cong\mathbf{A}(A,X)\times\mathbf{A}(A,Y)
$$

(using the fact that products are computed pointwise). This is the isomorphism (6.3) that we met at the beginning of this section.

Suppose that we view $\mathbf{A}$ as a subcategory of $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$, identifying $A\in\mathbf{A}$ with the representable $H_A\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ as in Figure 4.1. Then the isomorphism (6.12) means that given two objects of $\mathbf{A}$ whose product we want to form, it makes no difference whether we think of the product as taking place in $\mathbf{A}$ or $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$. Similarly, if $\mathbf{A}$ has all limits, taking limits does not help us to escape from $\mathbf{A}$ into the rest of $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$: any limit of representable presheaves is again representable.

**Warning 6.2.14** The Yoneda embedding does *not* preserve colimits. For example, if $\mathbf{A}$ has an initial object $0$ then $H_0$ is not initial, since $H_0(0)=\mathbf{A}(0,0)$ is a one-element set, whereas the initial object of $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ is the presheaf with constant value $\varnothing$. We investigate colimits of representables next.

### Every presheaf is a colimit of representables

We now know that the Yoneda embedding preserves limits but not colimits. In fact, the situation for colimits is at the opposite extreme from the situation for limits: by taking colimits of representable presheaves, we can obtain any presheaf we like! This is the last main result of this section.

Every positive integer can be expressed as a product of primes in an essentially unique way. Somewhat similarly, every presheaf can be expressed as a colimit of representables in a canonical (though not unique) way. The representables are the building blocks of presheaves.

For a different analogy, recall that any complex function holomorphic in a neighbourhood of $0$ has a power series expansion, such as

$$
e^z=1+z+\frac{z^2}{2!}+\frac{z^3}{3!}+\cdots.
$$

In this sense, the power functions $z\mapsto z^n$ are the building blocks of holomorphic functions. We could even take the analogy further: $(\ )^n$ is like a representable $\operatorname{Hom}(n,-)$, and in the categorical context, quotients and sums are types of colimit.

Before we state and prove the theorem, let us look at an easy special case.

**Example 6.2.15** Let $\mathbf{A}$ be the discrete category with two objects, $K$ and $L$. A <span class="original-page-anchor" id="pdf-page-163" aria-hidden="true"></span>presheaf $X$ on $\mathbf{A}$ is just a pair $(X(K),X(L))$ of sets, and $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]\cong\mathbf{Set}\times\mathbf{Set}$. There are two representables, $H_K$ and $H_L$, given by

$$
H_A(B)=\mathbf{A}(B,A)\cong
\begin{cases}
1&\text{if }A=B,\\
\varnothing&\text{if }A\ne B
\end{cases}
$$

($A,B\in\{K,L\}$). Identifying $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ with $\mathbf{Set}\times\mathbf{Set}$, we have $H_K\cong(1,\varnothing)$ and $H_L\cong(\varnothing,1)$. Every object of $\mathbf{Set}\times\mathbf{Set}$ is a sum of copies of $(1,\varnothing)$ and $(\varnothing,1)$. Suppose, for instance, that $X(K)$ has three elements and $X(L)$ has two elements. Then

$$
(X(K),X(L))\cong(1,\varnothing)+(1,\varnothing)+(1,\varnothing)+(\varnothing,1)+(\varnothing,1)
$$

in $\mathbf{Set}\times\mathbf{Set}$. Equivalently,

$$
X\cong H_K+H_K+H_K+H_L+H_L
$$

in $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$, exhibiting $X$ as a sum of representables.

In this example, $X$ is expressed as a sum of five representables, that is, a sum indexed by the set $X(K)+X(L)$ of ‘elements’ of $X$. A sum is a colimit over a discrete category. In the general case, a presheaf $X$ on a category $\mathbf{A}$ is expressed as a colimit over a category whose objects can be thought of as the ‘elements’ of $X$. This is made precise by the following definition.

**Definition 6.2.16** Let $\mathbf{A}$ be a category and $X$ a presheaf on $\mathbf{A}$. The **category of elements** $\mathbf{E}(X)$ of $X$ is the category in which:

- objects are pairs $(A,x)$ with $A\in\mathbf{A}$ and $x\in X(A)$;
- maps $(A',x')\to(A,x)$ are maps $f:A'\to A$ in $\mathbf{A}$ such that $(Xf)(x)=x'$.

There is a projection functor $P:\mathbf{E}(X)\to\mathbf{A}$ defined by $P(A,x)=A$ and $P(f)=f$.

The following ‘density theorem’ states that every presheaf is a colimit of representables in a canonical way. It is secretly dual to the Yoneda lemma. This becomes apparent if one expresses both in suitably lofty categorical language (that of ends, or that of bimodules); but that is beyond the scope of this book.

**Theorem 6.2.17 (Density)** Let $\mathbf{A}$ be a small category and $X$ a presheaf on $\mathbf{A}$. Then $X$ is the colimit of the diagram

$$
\mathbf{E}(X)\xrightarrow{P}\mathbf{A}\xrightarrow{H_\bullet}[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]
$$

in $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$; that is, $X\cong\lim_{\rightarrow\mathbf{E}(X)}(H_\bullet\circ P)$.

<span class="original-page-anchor" id="pdf-page-164" aria-hidden="true"></span>

**Proof** First note that since $\mathbf{A}$ is small, so too is $\mathbf{E}(X)$. Hence $H_\bullet\circ P$ really is a diagram in our customary sense (Definition 5.1.18).

Now let $Y\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$. A cocone on $H_\bullet\circ P$ with vertex $Y$ is a family

$$
\bigl(H_A\xrightarrow{\alpha_{A,x}}Y\bigr)_{A\in\mathbf{A},x\in X(A)}
$$

of natural transformations with the property that for all maps $A'\xrightarrow{f}A$ in $\mathbf{A}$ and all $x\in X(A)$, the diagram

![Cocone compatibility diagram](/library/volume-87/diagrams/pdf-0164-density-cocone.png)

commutes.

Equivalently (by the Yoneda lemma), a cocone on $H_\bullet\circ P$ with vertex $Y$ is a family

$$
(y_{A,x})_{A\in\mathbf{A},x\in X(A)},
$$

with $y_{A,x}\in Y(A)$, such that for all maps $A'\xrightarrow{f}A$ in $\mathbf{A}$ and all $x\in X(A)$,

$$
(Yf)(y_{A,x})=y_{A',(Xf)(x)}.
$$

To see this, note that if $\alpha_{A,x}\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}](H_A,Y)$ corresponds to $y_{A,x}\in Y(A)$, then $\alpha_{A,x}\circ H_f\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}](H_{A'},Y)$ corresponds to $(Yf)(y_{A,x})\in Y(A')$.

Equivalently (writing $y_{A,x}$ as $\bar\alpha_A(x)$), it is a family

$$
\bigl(X(A)\xrightarrow{\bar\alpha_A}Y(A)\bigr)_{A\in\mathbf{A}}
$$

of functions with the property that for all maps $A'\xrightarrow{f}A$ in $\mathbf{A}$ and all $x\in X(A)$,

$$
(Yf)\bigl(\bar\alpha_A(x)\bigr)=\bar\alpha_{A'}\bigl((Xf)(x)\bigr).
$$

But this is simply a natural transformation $\bar\alpha:X\to Y$. So we have, for each $Y\in[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$, a canonical bijection

$$
[\mathbf{E}(X),[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]](H_\bullet\circ P,\Delta Y)\cong[\mathbf{A}^{\mathrm{op}},\mathbf{Set}](X,Y).
$$

Hence $X$ is the colimit of $H_\bullet\circ P$. $\square$

**Example 6.2.18** In Example 6.2.15, we expressed a particular presheaf $X$ as a sum of representables. Let us check that the way we did this is a special case of the general construction in the density theorem.

Since $\mathbf{A}$ is discrete, the category of elements $\mathbf{E}(X)$ is also discrete; it is the set $X(K)+X(L)$ with five elements. The projection $P:\mathbf{E}(X)\to\mathbf{A}$ sends three of the <span class="original-page-anchor" id="pdf-page-165" aria-hidden="true"></span>elements to $K$ and the other two to $L$, so the diagram $H_\bullet\circ P:\mathbf{E}(X)\to[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ sends three of the elements to $H_K$ and two to $H_L$. The colimit of $H_\bullet\circ P$ is the sum of these five representables, which is $X$, just as in Example 6.2.15.

**Remarks 6.2.19** (a) The term ‘category of elements’ is compatible with the generalized element terminology introduced in Definition 4.1.25. A generalized element of an object $X$ is just a map into $X$, say $Z\to X$; but, as explained after that definition, we often focus on certain special shapes $Z$. Now suppose that we are working in a presheaf category $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$. Among all presheaves, the representables have a special status, so we might be especially interested in generalized elements of representable shape. The Yoneda lemma implies that for a presheaf $X$, the generalized elements of $X$ of representable shape correspond to pairs $(A,x)$ with $A\in\mathbf{A}$ and $x\in X(A)$. In other words, they are the objects of the category of elements.

(b) In topology, a subspace $A$ of a space $B$ is called dense if every point in $B$ can be obtained as a limit of points in $A$. This provides some explanation for the name of Theorem 6.2.17: the category $\mathbf{A}$ is ‘dense’ in $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ because every object of $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ can be obtained as a colimit of objects of $\mathbf{A}$.

### Exercises

**6.2.20** Fix a small category $\mathbf{A}$.

(a) Let $\mathscr{S}$ be a locally small category with pullbacks. Show that a natural transformation

![Natural transformation alpha from X to Y](/library/volume-87/diagrams/pdf-0165-natural-transformation.png)

is monic (as a map in $[\mathbf{A},\mathscr{S}]$) if and only if $\alpha_A$ is monic for all $A\in\mathbf{A}$. (Hint: use Lemma 5.1.32.)

(b) Describe explicitly the monics and epics in $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$.

(c) Can you do part (b) without relying on the fact that limits and colimits of presheaves are computed pointwise?

**6.2.21** (a) Prove that representables have the following connectedness property: given a locally small category $\mathscr{A}$ and $A\in\mathscr{A}$, if $X,Y\in[\mathscr{A}^{\mathrm{op}},\mathbf{Set}]$ with $H_A\cong X+Y$, then either $X$ or $Y$ is the constant functor $\varnothing$.

(b) Deduce that the sum of two representables is never representable.

<span class="original-page-anchor" id="pdf-page-166" aria-hidden="true"></span>

**6.2.22** Show how a category of elements can be described as a comma category.

**6.2.23** Let $X$ be a presheaf on a locally small category. Show that $X$ is representable if and only if its category of elements has a terminal object.

(Since a terminal object is a limit of the empty diagram, this implies that the concept of representability can be derived from the concept of limit. Since a terminal object of a category $\mathscr{E}$ is also a right adjoint to the unique functor $\mathscr{E}\to\mathbf{1}$, the concept of representability can also be derived from the concept of adjoint.)

**6.2.24** Prove that every slice of a presheaf category is again a presheaf category. That is, given a small category $\mathbf{A}$ and a presheaf $X$ on $\mathbf{A}$, prove that $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]/X$ is equivalent to $[\mathbf{B}^{\mathrm{op}},\mathbf{Set}]$ for some small category $\mathbf{B}$.

**6.2.25** Let $F:\mathbf{A}\to\mathbf{B}$ be a functor between small categories. For each object $B\in\mathbf{B}$, there is a comma category $(F\Rightarrow B)$ (defined dually to the comma category in Example 2.3.4), and there is a projection functor $P_B:(F\Rightarrow B)\to\mathbf{A}$.

(a) Let $X:\mathbf{A}\to\mathscr{S}$ be a functor from $\mathbf{A}$ to a category $\mathscr{S}$ with small colimits. For each $B\in\mathbf{B}$, let $(\operatorname{Lan}_F X)(B)$ be the colimit of the diagram

$$
(F\Rightarrow B)\xrightarrow{P_B}\mathbf{A}\xrightarrow{X}\mathscr{S}.
$$

Show that this defines a functor $\operatorname{Lan}_F X:\mathbf{B}\to\mathscr{S}$, and that for functors $Y:\mathbf{B}\to\mathscr{S}$, there is a canonical bijection between natural transformations $\operatorname{Lan}_F X\to Y$ and natural transformations $X\to Y\circ F$.

(b) Deduce that for any category $\mathscr{S}$ with small colimits, the functor

$$
-\circ F:[\mathbf{B},\mathscr{S}]\to[\mathbf{A},\mathscr{S}]
$$

has a left adjoint. (This left adjoint, $\operatorname{Lan}_F$, is called **left Kan extension** along $F$.)

(c) Part (b) and its dual imply that when $\mathscr{S}$ has small limits and colimits, the functor $-\circ F$ has both left and right adjoints. Revisit Exercise 2.1.16 with this in mind, taking $F$ to be either the unique functor $\mathbf{1}\to G$ or the unique functor $G\to\mathbf{1}$.

## 6.3 Interactions between adjoint functors and limits

We saw in Proposition 4.1.11 that any set-valued functor with a left adjoint is representable, and in Proposition 6.2.2 that any representable preserves limits.

<span class="original-page-anchor" id="pdf-page-167" aria-hidden="true"></span>

Hence, any set-valued functor with a left adjoint preserves limits. In fact, this conclusion holds not only for set-valued functors, but in complete generality.

**Theorem 6.3.1** Let

![Adjunction between A and B](/library/volume-87/diagrams/pdf-0167-adjunction.png)

be an adjunction. Then $F$ preserves colimits and $G$ preserves limits.

**Proof** By duality, it is enough to prove that $G$ preserves limits. Let $D:\mathbf{I}\to\mathscr{B}$ be a diagram for which a limit exists. Then

$$
\mathscr{A}\left(A,G\left(\lim_{\leftarrow\mathbf{I}}D\right)\right)\cong\mathscr{B}\left(F(A),\lim_{\leftarrow\mathbf{I}}D\right)\tag{6.13}
$$

$$
\phantom{\mathscr{A}\left(A,G\left(\lim_{\leftarrow\mathbf{I}}D\right)\right)}\cong\lim_{\leftarrow\mathbf{I}}\mathscr{B}(F(A),D)\tag{6.14}
$$

$$
\phantom{\mathscr{A}\left(A,G\left(\lim_{\leftarrow\mathbf{I}}D\right)\right)}\cong\lim_{\leftarrow\mathbf{I}}\mathscr{A}(A,G\circ D)\tag{6.15}
$$

$$
\phantom{\mathscr{A}\left(A,G\left(\lim_{\leftarrow\mathbf{I}}D\right)\right)}\cong\operatorname{Cone}(A,G\circ D)\tag{6.16}
$$

naturally in $A\in\mathscr{A}$. Here, the isomorphism (6.13) is by adjointness, (6.14) is because representables preserve limits, (6.15) is by adjointness again, and (6.16) is by Lemma 6.2.1. So $G\left(\lim_{\leftarrow\mathbf{I}}D\right)$ represents $\operatorname{Cone}(-,G\circ D)$; that is, it is a limit of $G\circ D$. $\square$

**Example 6.3.2** Forgetful functors from categories of algebras to $\mathbf{Set}$ have left adjoints, but hardly ever right adjoints. Correspondingly, they preserve all limits, but rarely all colimits.

**Example 6.3.3** Every set $B$ gives rise to an adjunction $(-\times B)\dashv(-)^B$ of functors from $\mathbf{Set}$ to $\mathbf{Set}$ (Example 2.1.6). So $-\times B$ preserves colimits and $(-)^B$ preserves limits. In particular, $-\times B$ preserves finite sums and $(-)^B$ preserves finite products, giving isomorphisms

$$
0\times B\cong0,\qquad(A_1+A_2)\times B\cong(A_1\times B)+(A_2\times B),\tag{6.17}
$$

$$
1^B\cong1,\qquad(A_1\times A_2)^B\cong A_1^B\times A_2^B.\tag{6.18}
$$

These are the analogues of standard rules of arithmetic. (See also Example 6.2.9 and the ‘Digression on arithmetic’ on page 69.) Indeed, if we know (6.17) and (6.18) for just finite sets then by taking cardinality on both sides, we obtain exactly these standard rules. The natural numbers are, after all, just the isomorphism classes of finite sets.

**Example 6.3.4** Given a category $\mathscr{A}$ with all limits of shape $\mathbf{I}$, we have the adjunction

![Diagonal functor and limit functor adjunction](/library/volume-87/diagrams/pdf-0167-limit-adjunction.png)

(Proposition 6.1.4). Hence $\lim_{\leftarrow\mathbf{I}}$ preserves limits, or <span class="original-page-anchor" id="pdf-page-168" aria-hidden="true"></span>equivalently, limits of shape $\mathbf{I}$ commute with (all) limits. This gives another proof that limits commute with limits (Proposition 6.2.8), at least in the case where the category has all limits of one of the shapes concerned.

**Example 6.3.5** Theorem 6.3.1 is often used to prove that a functor does *not* have an adjoint. For instance, it was claimed in Example 2.1.3(e) that the forgetful functor $U:\mathbf{Field}\to\mathbf{Set}$ does not have a left adjoint. We can now prove this. If $U$ had a left adjoint $F:\mathbf{Set}\to\mathbf{Field}$, then $F$ would preserve colimits, and in particular, initial objects. Hence $F(\varnothing)$ would be an initial object of $\mathbf{Field}$. But $\mathbf{Field}$ has no initial object, since there are no maps between fields of different characteristic. Further examples of nonexistence of adjoints can be found in Exercise 6.3.21.

### Adjoint functor theorems

Every functor with a left adjoint preserves limits, but limit-preservation alone does not guarantee the existence of a left adjoint. For example, let $\mathscr{B}$ be any category. The unique functor $\mathscr{B}\to\mathbf{1}$ always preserves limits, but by Example 2.1.9, it only has a left adjoint if $\mathscr{B}$ has an initial object.

On the other hand, if we have a limit-preserving functor $G:\mathscr{B}\to\mathscr{A}$ *and $\mathscr{B}$ has all limits*, then there is an excellent chance that $G$ has a left adjoint. It is still not always true, but counterexamples are harder to find. For instance (taking $\mathscr{A}=\mathbf{1}$ again), can you find a category $\mathscr{B}$ that has all limits but no initial object?

The condition of having all limits is so important that it has its own word:

**Definition 6.3.6** A category is **complete** (or properly, **small complete**) if it has all limits.

There are various results called adjoint functor theorems, all of the following form:

> Let $\mathscr{A}$ be a category, $\mathscr{B}$ a complete category, and $G:\mathscr{B}\to\mathscr{A}$ a functor. Suppose that $\mathscr{A}$, $\mathscr{B}$ and $G$ satisfy certain further conditions. Then

$$
G\text{ has a left adjoint}\quad\Longleftrightarrow\quad G\text{ preserves limits}.
$$

The forwards implication is immediate from Theorem 6.3.1. It is the backwards implication that concerns us here.

Typically, the ‘further conditions’ involve the distinction between small and <span class="original-page-anchor" id="pdf-page-169" aria-hidden="true"></span>large collections. But there is a special case in which these complications disappear, and I will use it to explain the main idea behind the proofs of the adjoint functor theorems. It is the case where the categories $\mathscr{A}$ and $\mathscr{B}$ are ordered sets.

As we saw in Section 5.1, limits in ordered sets are meets. More precisely, if $D:\mathbf{I}\to\mathbf{B}$ is a diagram in an ordered set $\mathbf{B}$, then

$$
\lim_{\leftarrow\mathbf{I}}D=\bigwedge_{I\in\mathbf{I}}D(I),
$$

with one side defined if and only if the other is. So an ordered set is complete if and only if every subset has a meet. Similarly, a map $G:\mathbf{B}\to\mathbf{A}$ of ordered sets preserves limits if and only if

$$
G\left(\bigwedge_{i\in I}B_i\right)=\bigwedge_{i\in I}G(B_i)
$$

whenever $(B_i)_{i\in I}$ is a family of elements of $\mathbf{B}$ for which a meet exists.

We now show that for ordered sets, there is an adjoint functor theorem of the simplest possible kind: there are no ‘further conditions’ at all.

**Proposition 6.3.7 (Adjoint functor theorem for ordered sets)** Let $\mathbf{A}$ be an ordered set, $\mathbf{B}$ a complete ordered set, and $G:\mathbf{B}\to\mathbf{A}$ an order-preserving map. Then

$$
G\text{ has a left adjoint}\quad\Longleftrightarrow\quad G\text{ preserves meets}.
$$

**Proof** Suppose that $G$ preserves meets. By Corollary 2.3.7, it is enough to show that for each $A\in\mathbf{A}$, the comma category $(A\Rightarrow G)$ has an initial object. Let $A\in\mathbf{A}$. Then $(A\Rightarrow G)$ is an ordered set, namely, $\{B\in\mathbf{B}\mid A\le G(B)\}$ with the order inherited from $\mathbf{B}$. We have to show that $(A\Rightarrow G)$ has a least element.

Since $\mathbf{B}$ is complete, the meet $\bigwedge_{B\in\mathbf{B}:\ A\le G(B)}B$ exists in $\mathbf{B}$. This is the meet of all the elements of $(A\Rightarrow G)$, so it suffices to show that the meet is itself an element of $(A\Rightarrow G)$. And indeed, since $G$ preserves meets, we have

$$
G\left(\bigwedge_{B\in\mathbf{B}:\ A\le G(B)}B\right)=\bigwedge_{B\in\mathbf{B}:\ A\le G(B)}G(B)\ge A,
$$

as required. $\square$

In the general setting of Corollary 2.3.7, the initial object of $(A\Rightarrow G)$ is the pair $\bigl(F(A),A\xrightarrow{\eta_A}GF(A)\bigr)$, where $F$ is the left adjoint and $\eta$ is the unit map. So in Proposition 6.3.7, the left adjoint $F$ is given by

$$
F(A)=\bigwedge_{B\in\mathbf{B}:\ A\le G(B)}B.\tag{6.19}
$$

<span class="original-page-anchor" id="pdf-page-170" aria-hidden="true"></span>

**Example 6.3.8** Consider Proposition 6.3.7 in the case $\mathbf{A}=\mathbf{1}$. The unique functor $G:\mathbf{B}\to\mathbf{1}$ automatically preserves meets, and, as observed above, a left adjoint to $G$ is an initial object of $\mathbf{B}$. So in the case $\mathbf{A}=\mathbf{1}$, the proposition states that a complete ordered set has a least element. This is not quite trivial, since completeness means the existence of all meets, whereas a least element is an empty *join*.

By (6.19), the least element of $\mathbf{B}$ is $\bigwedge_{B\in\mathbf{B}}B$. Thus, a least element is not only a colimit of the functor $\varnothing\to\mathbf{B}$; it is also a limit of the identity functor $\mathbf{B}\to\mathbf{B}$.

The synonym ‘least upper bound’ for ‘join’ suggests a theorem: that a poset with all meets also has all joins. Indeed, given a poset $\mathbf{B}$ with all meets, the join of a subset of $\mathbf{B}$ is simply the meet of its upper bounds: quite literally, its least upper bound.

Let us now attempt to extend Proposition 6.3.7 from ordered sets to categories, starting with a limit-preserving functor $G$ from a complete category $\mathscr{B}$ to a category $\mathscr{A}$. In the case of ordered sets, we had for each $A\in\mathscr{A}$ an inclusion map $P_A:(A\Rightarrow G)\hookrightarrow\mathbf{B}$, and we showed that the left adjoint $F$ was given by

$$
F(A)=\lim_{\leftarrow(A\Rightarrow G)}P_A.\tag{6.20}
$$

In the general case, the analogue of the inclusion functor is the projection functor

$$
\begin{array}{rccc}
P_A:&(A\Rightarrow G)&\to&\mathscr{B}\\
&\bigl(B,A\xrightarrow{f}G(B)\bigr)&\mapsto&B.
\end{array}\tag{6.21}
$$

The case of ordered sets suggests that in general, equation (6.20) might define a left adjoint $F$ to $G$. And indeed, it can be shown that if this limit in $\mathscr{B}$ exists and is preserved by $G$, then (6.20) really does give a left adjoint (Theorem X.1.2 of Mac Lane (1971)).

This might seem to suggest that our adjoint functor theorem generalizes smoothly from ordered sets to arbitrary categories, with no need for further conditions. But it does not, for reasons that are quite subtle.

Those reasons are more easily explained if we relax our terminology slightly. When we defined limits, we built in the condition that the shape category $\mathbf{I}$ was small. However, the definition of limit makes sense for an arbitrary category $\mathbf{I}$. In this discussion, we will need to refer to this more inclusive notion of limit, so let us temporarily suspend the convention that the shape categories $\mathbf{I}$ of limits are always small.

Now, in the template for adjoint functor theorems stated above (after Definition 6.3.6), it was only required that $\mathscr{B}$ has, and $G$ preserves, *small* limits. But <span class="original-page-anchor" id="pdf-page-171" aria-hidden="true"></span>if $\mathscr{B}$ is a large category then $(A\Rightarrow G)$ might also be large, since to specify an object or map in $(A\Rightarrow G)$, we have to specify (among other things) an object or map in $\mathscr{B}$. So, the limit (6.20) defining the left adjoint is not guaranteed to be small. Hence there is no guarantee that this limit exists in $\mathscr{B}$, nor that it is preserved by $G$. It follows that the functor $F$ ‘defined’ by (6.20) might not be defined at all, let alone a left adjoint.

(The reader experiencing difficulty with reasoning about small and large collections might usefully compare finite and infinite collections. For instance, if $\mathscr{B}$ is a finite category and $\mathscr{A}$ has finite hom-sets then $(A\Rightarrow G)$ is also finite, but otherwise $(A\Rightarrow G)$ might be infinite.)

Proposition 6.3.7 still stands, since there we were dealing with ordered *sets*, which as categories are small. We might hope to extend it from posets to arbitrary small categories, since the problem just described affects only large categories. But this turns out not to be very fruitful, since in fact, complete posets are the *only* complete small categories (Exercise 6.3.23).

Alternatively, we could try to salvage the argument by assuming that $\mathscr{B}$ has, and $G$ preserves, *all* (possibly large) limits. But again, this is unhelpful: there are almost no such categories $\mathscr{B}$.

The situation therefore becomes more complicated. Each of the best-known adjoint functor theorems imposes further conditions implying that the large limit $\lim_{\leftarrow(A\Rightarrow G)}P_A$ can be replaced by a small limit in some clever way. This allows one to proceed with the argument above.

The two most famous adjoint functor theorems are the ‘general’ and the ‘special’. Their exact statements and proofs are perhaps less significant than their consequences.

**Definition 6.3.9** Let $\mathscr{C}$ be a category. A **weakly initial set** in $\mathscr{C}$ is a set $\mathbf{S}$ of objects with the property that for each $C\in\mathscr{C}$, there exist an element $S\in\mathbf{S}$ and a map $S\to C$.

Note that $\mathbf{S}$ must be a set, that is, small. So, the existence of a weakly initial set is some kind of size restriction. Such size restrictions are comparable to finiteness conditions in algebra.

**Theorem 6.3.10 (General adjoint functor theorem)** Let $\mathscr{A}$ be a category, $\mathscr{B}$ a complete category, and $G:\mathscr{B}\to\mathscr{A}$ a functor. Suppose that $\mathscr{B}$ is locally small and that for each $A\in\mathscr{A}$, the category $(A\Rightarrow G)$ has a weakly initial set. Then

$$
G\text{ has a left adjoint}\quad\Longleftrightarrow\quad G\text{ preserves limits}.
$$

**Proof** See the appendix. $\square$ <span class="original-page-anchor" id="pdf-page-172" aria-hidden="true"></span>**Example 6.3.11** The general adjoint functor theorem (GAFT) implies that for any category $\mathscr{B}$ of algebras ($\mathbf{Grp}$, $\mathbf{Vect}_k$, $\ldots$), the forgetful functor $U:\mathscr{B}\to\mathbf{Set}$ has a left adjoint. Indeed, we saw in Example 5.1.23 that $\mathscr{B}$ has all limits, and in Example 5.3.4 that $U$ preserves them. Also, $\mathscr{B}$ is locally small. To apply GAFT, we now just have to check that for each $A\in\mathbf{Set}$, the comma category $(A\Rightarrow U)$ has a weakly initial set. This requires a little cardinal arithmetic, omitted here; see Exercise 6.3.24.

So GAFT tells us that, for instance, the free group functor exists. In Examples 1.2.4(a) and 2.1.3(b), we began to see the trickiness of explicitly constructing the free group on a generating set $A$. One has to define the set of ‘formal expressions’ (such as $x^{-1}yx^2zy^{-3}$, with $x,y,z\in A$), then say what it means for two such expressions to be equivalent (so that $x^{-2}x^5y$ is equivalent to $x^3y$), then define $F(A)$ to be the set of all equivalence classes, then define the group structure, then check the group axioms, then prove that the resulting group has the universal property required. But using GAFT, we can avoid these complications entirely.

The price to be paid is that GAFT does not give us an explicit description of free groups (or left adjoints more generally). When people speak of knowing some object ‘explicitly’, they usually mean knowing its elements. An element of an object is a map *into* it, and we have no handle on maps into $F(A)$: since $F$ is a left adjoint, it is maps *out* of $F(A)$ that we know about. This is why explicit descriptions of left adjoints are often hard to come by.

**Example 6.3.12** More generally, GAFT guarantees that forgetful functors between categories of algebras, such as

$$
\mathbf{Ab}\to\mathbf{Grp},\quad\mathbf{Grp}\to\mathbf{Mon},\quad\mathbf{Ring}\to\mathbf{Mon},\quad\mathbf{Vect}_{\mathbb{C}}\to\mathbf{Vect}_{\mathbb{R}},
$$

have left adjoints. (Some of them are described in Examples 2.1.3.) This is ‘more generally’ because $\mathbf{Set}$ can be seen as a degenerate example of a category of algebras, in the sense of Remark 2.1.4: a group, ring, etc., is a set equipped with some operations satisfying some equations, and a set is a set equipped with no operations satisfying no equations.

The special adjoint functor theorem (SAFT) operates under much tighter hypotheses than GAFT, and is much less widely applicable. Its main advantage is that it removes the condition on weakly initial sets. Indeed, it removes *all* further conditions on the functor $G$.

**Theorem 6.3.13 (Special adjoint functor theorem)** Let $\mathscr{A}$ be a category, $\mathscr{B}$ a complete category, and $G:\mathscr{B}\to\mathscr{A}$ a functor. Suppose that $\mathscr{A}$ and $\mathscr{B}$ <span class="original-page-anchor" id="pdf-page-173" aria-hidden="true"></span>are locally small, and that $\mathscr{B}$ satisfies certain further conditions. Then

$$
G\text{ has a left adjoint}\quad\Longleftrightarrow\quad G\text{ preserves limits}.
$$

A precise statement and proof can be found in Section V.8 of Mac Lane (1971).

**Example 6.3.14** Here is the classic application of SAFT. Let $\mathbf{CptHff}$ be the category of compact Hausdorff spaces, and $U:\mathbf{CptHff}\to\mathbf{Top}$ the forgetful functor. SAFT tells us that $U$ has a left adjoint $F$, turning any space into a compact Hausdorff space in a canonical way.

The existence of this left adjoint is far from obvious, and verifying the hypotheses of SAFT (or indeed, constructing $F$ in any other way) requires some deep theorems of topology. Given a space $X$, the resulting compact Hausdorff space $F(X)$ is called its **Stone–Čech compactification**. Provided that $X$ satisfies some mild separation conditions, the unit of the adjunction at $X$ is an embedding, so that $UF(X)$ contains $X$ as a subspace.

Another advantage of SAFT is that one can extract from its proof a fairly explicit formula for the left adjoint. In this case, it tells us that $F(X)$ is the closure of the image of the canonical map

$$
X\to[0,1]^{\mathbf{Top}(X,[0,1])},
$$

where the codomain is a power of $[0,1]$ in $\mathbf{Top}$.

### Cartesian closed categories

We have seen that for every set $B$, there is an adjunction $(-\times B)\dashv(-)^B$ (Example 2.1.6), and that for every category $\mathscr{B}$, there is an adjunction $(-\times\mathscr{B})\dashv[\mathscr{B},-]$ (Remark 4.1.23(c)).

**Definition 6.3.15** A category $\mathscr{A}$ is **cartesian closed** if it has finite products and for each $B\in\mathscr{A}$, the functor $-\times B:\mathscr{A}\to\mathscr{A}$ has a right adjoint.

We write the right adjoint as $(-)^B$, and, for $C\in\mathscr{A}$, call $C^B$ an **exponential**. We may think of $C^B$ as the space of maps from $B$ to $C$. Adjointness says that for all $A,B,C\in\mathscr{A}$,

$$
\mathscr{A}(A\times B,C)\cong\mathscr{A}(A,C^B)
$$

naturally in $A$ and $C$. In fact, the isomorphism is natural in $B$ too; that comes for free.

**Example 6.3.16** $\mathbf{Set}$ is cartesian closed; $C^B$ is the function set $\mathbf{Set}(B,C)$.

**Example 6.3.17** $\mathbf{CAT}$ is cartesian closed; $\mathscr{C}^{\mathscr{B}}$ is the functor category $[\mathscr{B},\mathscr{C}]$.

<span class="original-page-anchor" id="pdf-page-174" aria-hidden="true"></span>

In any cartesian closed category with finite sums, the isomorphisms (6.17) and (6.18) of Example 6.3.3 hold, for the same reasons as stated there. The objects of a cartesian closed category therefore possess an arithmetic like that of the natural numbers. This thought can be developed in several interesting directions, but here we just note that these isomorphisms provide a way of proving that a category is *not* cartesian closed.

**Example 6.3.18** $\mathbf{Vect}_k$ is not cartesian closed, for any field $k$. It does have finite products, as we saw in Example 5.1.5: binary product is direct sum $\oplus$, and the terminal object is the trivial vector space $\{0\}$, which is also initial. But if $\mathbf{Vect}_k$ were cartesian closed then equations (6.17) would hold, so that $\{0\}\oplus B\cong\{0\}$ for all vector spaces $B$. This is plainly false.

**Remark 6.3.19** For any vector spaces $V$ and $W$, the set $\mathbf{Vect}_k(V,W)$ of linear maps can itself be given the structure of a vector space, as in Example 1.2.12. Let us now call this vector space $[V,W]$.

Given that exponentials are supposed to be ‘spaces of maps’, you might expect $\mathbf{Vect}_k$ to be cartesian closed, with $[-,-]$ as its exponential. We have just seen that this cannot be so. But as it turns out, the linear maps $U\to[V,W]$ correspond to the *bi*linear maps $U\times V\to W$, or equivalently the linear maps $U\otimes V\to W$. In the jargon, $\mathbf{Vect}_k$ is an example of a ‘monoidal closed category’. These are like cartesian closed categories, but with the cartesian (categorical) product replaced by some other operation called ‘product’, in this case the tensor product of vector spaces.

For any set $I$, the product category $\mathbf{Set}^I$ is cartesian closed, just because $\mathbf{Set}$ is. (Exponentials in $\mathbf{Set}^I$, as well as products, are computed pointwise.) Put another way, $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ is cartesian closed whenever $\mathbf{A}$ is discrete. We now show that, in fact, $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ is cartesian closed for any small category $\mathbf{A}$ whatsoever.

In preparation for proving this, let us conduct a thought experiment. Write $\hat{\mathbf{A}}=[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$. If $\hat{\mathbf{A}}$ *is* cartesian closed, what must exponentials in $\hat{\mathbf{A}}$ be? In other words, given presheaves $Y$ and $Z$, what must $Z^Y$ be in order that

$$
\hat{\mathbf{A}}(X,Z^Y)\cong\hat{\mathbf{A}}(X\times Y,Z)\tag{6.22}
$$

for all presheaves $X$? If this is true for all presheaves $X$, then in particular it is true when $X$ is representable, so

$$
Z^Y(A)\cong\hat{\mathbf{A}}(H_A,Z^Y)\cong\hat{\mathbf{A}}(H_A\times Y,Z)
$$

for all $A\in\mathbf{A}$, the first step by Yoneda. This tells us what $Z^Y$ must be. Notice that $Z^Y(A)$ is not simply $Z(A)^{Y(A)}$, as one might at first guess: exponentials in a presheaf category are *not* generally computed pointwise.

<span class="original-page-anchor" id="pdf-page-175" aria-hidden="true"></span>

**Theorem 6.3.20** For any small category $\mathbf{A}$, the presheaf category $\hat{\mathbf{A}}$ is cartesian closed.

Here is the strategy of the proof. The argument in the thought experiment gives us the isomorphism (6.22) whenever $X$ is representable. A general presheaf $X$ is not representable, but it is a colimit of representables, and this allows us to bootstrap our way up.

**Proof** We know that $\hat{\mathbf{A}}$ has all limits, and in particular, finite products. It remains to show that $\hat{\mathbf{A}}$ has exponentials. Fix $Y\in\hat{\mathbf{A}}$.

First we prove that $-\times Y:\hat{\mathbf{A}}\to\hat{\mathbf{A}}$ preserves colimits. (Eventually we will prove that $-\times Y$ has a right adjoint, from which preservation of colimits follows, but our proof that it has a right adjoint will *use* preservation of colimits.) Indeed, since products and colimits in $\hat{\mathbf{A}}$ are computed pointwise, it is enough to prove that for any set $S$, the functor $-\times S:\mathbf{Set}\to\mathbf{Set}$ preserves colimits, and this follows from the fact that $\mathbf{Set}$ is cartesian closed.

For each presheaf $Z$ on $\mathbf{A}$, let $Z^Y$ be the presheaf defined by

$$
Z^Y(A)=\hat{\mathbf{A}}(H_A\times Y,Z)
$$

for all $A\in\mathbf{A}$. This defines a functor $(-)^Y:\hat{\mathbf{A}}\to\hat{\mathbf{A}}$.

I claim that $(-\times Y)\dashv(-)^Y$. Let $X,Z\in\hat{\mathbf{A}}$. Write $P:\mathbf{E}(X)\to\mathbf{A}$ for the projection (as in Definition 6.2.16), and write $H_P=H_\bullet\circ P$. Then

$$
\hat{\mathbf{A}}(X,Z^Y)\cong\hat{\mathbf{A}}\left(\lim_{\rightarrow\mathbf{E}(X)}H_P,Z^Y\right)\tag{6.23}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\lim_{\leftarrow\mathbf{E}(X)^{\mathrm{op}}}\hat{\mathbf{A}}(H_P,Z^Y)\tag{6.24}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\lim_{\leftarrow\mathbf{E}(X)^{\mathrm{op}}}Z^Y(P)\tag{6.25}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\lim_{\leftarrow\mathbf{E}(X)^{\mathrm{op}}}\hat{\mathbf{A}}(H_P\times Y,Z)\tag{6.26}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\hat{\mathbf{A}}\left(\lim_{\rightarrow\mathbf{E}(X)}(H_P\times Y),Z\right)\tag{6.27}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\hat{\mathbf{A}}\left(\left(\lim_{\rightarrow\mathbf{E}(X)}H_P\right)\times Y,Z\right)\tag{6.28}
$$

$$
\phantom{\hat{\mathbf{A}}(X,Z^Y)}\cong\hat{\mathbf{A}}(X\times Y,Z)\tag{6.29}
$$

naturally in $X$ and $Z$. Here (6.23) and (6.29) follow from Theorem 6.2.17; (6.24) and (6.27) are because representables preserve limits (as rephrased in Remark 6.2.3); (6.25) is by Yoneda; (6.26) is by definition of $Z^Y$; and (6.28) is because $-\times Y$ preserves colimits. $\square$

This result can be seen as a step along the road to topos theory. A topos is a <span class="original-page-anchor" id="pdf-page-176" aria-hidden="true"></span>category with certain special properties. Topos theory unifies, in an extraordinary way, important aspects of logic and geometry.

For instance, a topos can be regarded as a ‘universe of sets’: $\mathbf{Set}$ is the most basic example of a topos, and every topos shares enough features with $\mathbf{Set}$ that one can reason with its objects as if they were sets of some exotic kind. On the other hand, a topos can be regarded as a generalized topological space: every space gives rise to a topos (namely, the category of sheaves on it), and topological properties of the space can be reinterpreted in a useful way as categorical properties of its associated topos.

By definition, a topos is a cartesian closed category with finite limits and with one further property: the existence of a so-called subobject classifier. For example, the two-element set $2$ is the subobject classifier of $\mathbf{Set}$, which means, informally, that subsets of a set $A$ correspond one-to-one with maps $A\to2$. Exercises 6.3.26 and 6.3.27 give the formal definition of subobject classifier, then guide you through the proof that $\mathbf{Set}$, and, more generally, every presheaf category, is a topos.

### Exercises

**6.3.21** (a) Prove that the forgetful functor $U:\mathbf{Grp}\to\mathbf{Set}$ has no right adjoint.

(b) Prove that the chain of adjunctions $C\dashv D\dashv O\dashv I$ in Exercise 3.2.16 extends no further in either direction.

(c) Does the chain of adjunctions in Exercise 2.1.17 extend further in either direction?

**6.3.22** Let $\mathscr{A}$ be a locally small category. For functors $U:\mathscr{A}\to\mathbf{Set}$, consider the following three conditions: (A) $U$ has a left adjoint; (R) $U$ is representable; (L) $U$ preserves limits.

(a) Show that (A) $\Longrightarrow$ (R) $\Longrightarrow$ (L).

(b) Show that if $\mathscr{A}$ has sums then (R) $\Longrightarrow$ (A).

(If $\mathscr{A}$ satisfies the hypotheses of the special adjoint functor theorem then also (L) $\Longrightarrow$ (A), so the three conditions are equivalent.)

**6.3.23** (a) Prove that every preordered set is equivalent (as a category) to an ordered set.

(b) Let $\mathscr{A}$ be a category with all small products. Suppose that $\mathscr{A}$ is not a preorder, so that there exists a parallel pair of maps

![Parallel pair f and g from A to B](/library/volume-87/diagrams/pdf-0176-parallel-pair.png)

in $\mathscr{A}$ with <span class="original-page-anchor" id="pdf-page-177" aria-hidden="true"></span>$f\ne g$. By considering the maps $A\to B^I$ for each set $I$, prove that $\mathscr{A}$ is not small.

(c) Deduce that every small category with small products is equivalent to a complete ordered set.

(d) Adapt the argument to prove that every finite category with finite products is equivalent to a complete ordered set.

**6.3.24** Probably the most important application of the general adjoint functor theorem is to proving that forgetful functors between categories of algebras have left adjoints (Example 6.3.11). Verifying the hypotheses can be done with some cardinal arithmetic. Here is a typical example.

(a) Let $A$ be a set. Prove that for any group $G$ and family $(g_a)_{a\in A}$ of elements of $G$, the subgroup of $G$ generated by $\{g_a\mid a\in A\}$ has cardinality at most $\max\{|\mathbb{N}|,|A|\}$.

(b) Prove that for any set $S$, the collection of isomorphism classes of groups of cardinality at most $|S|$ is small.

(c) Let $U:\mathbf{Grp}\to\mathbf{Set}$ be the forgetful functor from groups to sets. Deduce from (a) and (b) that for every set $A$, the comma category $(A\Rightarrow U)$ has a weakly initial set.

(d) Use GAFT to conclude that $U$ has a left adjoint.

**6.3.25** Let $\mathbf{A}$ be a small cartesian closed category. Prove that the Yoneda embedding $\mathbf{A}\to[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ preserves the whole cartesian closed structure (exponentials as well as products).

**6.3.26** Recall from Exercise 5.1.40 the notion of subobject. A category $\mathscr{A}$ is **well-powered** if for each $A\in\mathscr{A}$, the class of subobjects of $A$ is small, that is, a set. (All of our usual examples of categories are well-powered.) Let $\mathscr{A}$ be a well-powered category with pullbacks, and write $\operatorname{Sub}(A)$ for the set of subobjects of an object $A\in\mathscr{A}$.

(a) Deduce from Exercise 5.1.42 that any map $A'\xrightarrow{f}A$ in $\mathscr{A}$ induces a map $\operatorname{Sub}(f):\operatorname{Sub}(A)\to\operatorname{Sub}(A')$.

(b) Show that this determines a functor $\operatorname{Sub}:\mathscr{A}^{\mathrm{op}}\to\mathbf{Set}$. (Hint: use Exercise 5.1.35.)

(c) For some categories $\mathscr{A}$, the functor $\operatorname{Sub}$ is representable. A **subobject classifier** for $\mathscr{A}$ is an object $\Omega\in\mathscr{A}$ such that $\operatorname{Sub}\cong H_\Omega$. Prove that $2$ is a subobject classifier for $\mathbf{Set}$.

A **topos** is a cartesian closed category with finite limits and a subobject classifier. You have just completed the proof that $\mathbf{Set}$ is a topos.

<span class="original-page-anchor" id="pdf-page-178" aria-hidden="true"></span>

**6.3.27** This exercise follows on from the last, culminating in the proof that every presheaf category is a topos. Let $\mathbf{A}$ be a small category.

(a) By conducting a thought experiment similar to the one before the statement of Theorem 6.3.20, find out what the subobject classifier $\Omega$ of $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ must be if it exists.

(b) Prove that this $\Omega$ is indeed a subobject classifier.

(c) Conclude that $[\mathbf{A}^{\mathrm{op}},\mathbf{Set}]$ is a topos.
