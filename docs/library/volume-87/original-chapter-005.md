---
title: "Limits"
description: "Tom Leinster《Basic Category Theory》English。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"Representables","link":"/library/volume-87/original-chapter-004"}
next: {"text":"Adjoints, representables and limits","link":"/library/volume-87/original-chapter-006"}
---

# Limits

<span class="original-page-anchor" id="pdf-page-116" aria-hidden="true"></span>

Limits, and the dual concept, colimits, provide our third approach to the idea of universal property.

Adjointness is about the relationships *between* categories. Representability is a property of *set-valued* functors. Limits are about what goes on *inside* a category.

The concept of limit unifies many familiar constructions in mathematics. Whenever you meet a method for taking some objects and maps in a category and constructing a new object out of them, there is a good chance that you are looking at either a limit or a colimit. For instance, in group theory, we can take a homomorphism between two groups and form its kernel, which is a new group. This construction is an example of a limit in the category of groups. Or, we might take two natural numbers and form their lowest common multiple. This is an example of a colimit in the poset of natural numbers, ordered by divisibility.

## 5.1 Limits: definition and examples

The definition of limit is very general. We build up to it by first examining some particularly useful types of limit: products, equalizers, and pullbacks.

### Products

Let $X$ and $Y$ be sets. The familiar cartesian product $X\times Y$ is characterized by the property that an element of $X\times Y$ is an element of $X$ together with an element of $Y$. Since elements are just maps from $1$, this says that a map $1\to X\times Y$ amounts to a map $1\to X$ together with a map $1\to Y$.

A little thought reveals that the same is true when $1$ is replaced throughout <span class="original-page-anchor" id="pdf-page-117" aria-hidden="true"></span>by any set $A$ whatsoever. (In other words, a generalized element of $X\times Y$ of shape $A$ amounts to a generalized element of $X$ of shape $A$ together with a generalized element of $Y$ of shape $A$.) The bijection between

$$
\text{maps }A\to X\times Y
$$

and

$$
\text{pairs of maps }(A\to X,\ A\to Y)
$$

is given by composing with the projection maps

![Projection maps and their action on elements](/library/volume-87/diagrams/pdf-0117-projections.png)

This suggests the following definition.

**Definition 5.1.1** Let $\mathscr{A}$ be a category and $X,Y\in\mathscr{A}$. A **product** of $X$ and $Y$ consists of an object $P$ and maps

![Product projections](/library/volume-87/diagrams/pdf-0117-product.png)

with the property that for all objects and maps

![Objects and maps (5.1)](/library/volume-87/diagrams/pdf-0117-cone-5-1.png)

in $\mathscr{A}$, there exists a unique map $\bar f:A\to P$ such that

![Universal property (5.2)](/library/volume-87/diagrams/pdf-0117-universal-5-2.png)

commutes. The maps $p_1$ and $p_2$ are called the **projections**.

**Remarks 5.1.2** (a) Products do not always exist. For example, if $\mathscr{A}$ is the discrete two-object category

![Discrete two-object category](/library/volume-87/diagrams/pdf-0117-discrete.png)

<span class="original-page-anchor" id="pdf-page-118" aria-hidden="true"></span>

then $X$ and $Y$ do not have a product. But when objects $X$ and $Y$ of a category do have a product, it is unique up to isomorphism. (This can be proved directly, much as in Lemma 2.1.8. It also follows from Corollary 6.1.2.) This justifies talking about *the* product of $X$ and $Y$.

(b) Strictly speaking, the product consists of the object $P$ *together with* the projections $p_1$ and $p_2$. But informally, we often refer to $P$ alone as the product of $X$ and $Y$. We write $P$ as $X\times Y$.

**Example 5.1.3** Any two sets $X$ and $Y$ have a product in $\mathbf{Set}$. It is the usual cartesian product $X\times Y$, equipped with the usual projection maps $p_1$ and $p_2$.

Let us check that this really is a product in the sense of Definition 5.1.1. Take sets and functions as in diagram (5.1). Define $\bar f:A\to X\times Y$ by $\bar f(a)=(f_1(a),f_2(a))$. Then $p_i\circ\bar f=f_i$ for $i=1,2$; that is, diagram (5.2) commutes with $P=X\times Y$. Moreover, this is the *only* map making diagram (5.2) commute. For suppose that $\hat f:A\to X\times Y$, in place of $\bar f$, also makes (5.2) commute. Let $a\in A$, and write $\hat f(a)$ as $(x,y)$. Then

$$
f_1(a)=p_1(\hat f(a))=p_1(x,y)=x,
$$

and similarly, $f_2(a)=y$. Hence $\hat f(a)=(f_1(a),f_2(a))=\bar f(a)$ for all $a\in A$, giving $\hat f=\bar f$, as required.

In general, in any category, the map $\bar f$ of diagram (5.2) is usually written as $(f_1,f_2)$.

**Example 5.1.4** In the category of topological spaces, any two objects $X$ and $Y$ have a product. It is the set $X\times Y$ equipped with the product topology and the standard projection maps. The product topology is deliberately designed so that a function

$$
\begin{array}{ccc}
A&\to&X\times Y\\
t&\mapsto&(x(t),y(t))
\end{array}
$$

is continuous if and only if it is continuous in each coordinate (that is to say, both functions

$$
t\mapsto x(t),\qquad t\mapsto y(t)
$$

are continuous). This holds for any space $A$, but the idea is perhaps at its most intuitively appealing when $A=\mathbb{R}$ and we think of $t$ as a time parameter.

A closely related statement is that the product topology is the smallest topology on $X\times Y$ for which the projections are continuous. Here ‘smallest’ means that for any other topology $\mathcal{T}$ on $X\times Y$ such that $p_1$ and $p_2$ are continuous, every subset of $X\times Y$ open in the product topology is also open in $\mathcal{T}$. Thus, <span class="original-page-anchor" id="pdf-page-119" aria-hidden="true"></span>to define the product topology, we declare just enough sets to be open that the projections are continuous.

**Example 5.1.5** Now let $X$ and $Y$ be vector spaces. We can form their direct sum, $X\oplus Y$, whose elements can be written as either $(x,y)$ or $x+y$ (with $x\in X$ and $y\in Y$), according to taste. There are linear projection maps

![Linear projection maps](/library/volume-87/diagrams/pdf-0119-vector-product.png)

It can be shown that $X\oplus Y$, together with $p_1$ and $p_2$, is the product of $X$ and $Y$ in the category of vector spaces (Exercise 5.1.33).

**Examples 5.1.6 (Elements of ordered sets)** (a) Let $x,y\in\mathbb{R}$. Their minimum $\min\{x,y\}$ satisfies

$$
\min\{x,y\}\leq x,\qquad\min\{x,y\}\leq y
$$

and has the further property that whenever $a\in\mathbb{R}$ with

$$
a\leq x,\qquad a\leq y,
$$

we have $a\leq\min\{x,y\}$. This means exactly that when the poset $(\mathbb{R},\leq)$ is viewed as a category, the product of $x,y\in\mathbb{R}$ is $\min\{x,y\}$. The definition of product simplifies when interpreted in a poset, since all diagrams commute.

(b) Fix a set $S$. Let $X,Y\in\mathscr{P}(S)$. Then $X\cap Y$ satisfies

$$
X\cap Y\subseteq X,\qquad X\cap Y\subseteq Y
$$

and has the further property that whenever $A\in\mathscr{P}(S)$ with

$$
A\subseteq X,\qquad A\subseteq Y,
$$

we have $A\subseteq X\cap Y$. This means that $X\cap Y$ is the product of $X$ and $Y$ in the poset $(\mathscr{P}(S),\subseteq)$ regarded as a category.

(c) Let $x,y\in\mathbb{N}$. Their greatest common divisor $\gcd(x,y)$ satisfies

$$
\gcd(x,y)\mid x,\qquad\gcd(x,y)\mid y
$$

(it’s a common divisor!) and has the further property that whenever $a\in\mathbb{N}$ with

$$
a\mid x,\qquad a\mid y,
$$

<span class="original-page-anchor" id="pdf-page-120" aria-hidden="true"></span>

we have $a\mid\gcd(x,y)$. This means that $\gcd(x,y)$ is the product of $x$ and $y$ in the poset $(\mathbb{N},\mid)$ regarded as a category.

Generally, let $(A,\leq)$ be a poset and $x,y\in A$. A **lower bound** for $x$ and $y$ is an element $a\in A$ such that $a\leq x$ and $a\leq y$. A **greatest lower bound** or **meet** of $x$ and $y$ is a lower bound $z$ for $x$ and $y$ with the further property that whenever $a$ is a lower bound for $x$ and $y$, we have $a\leq z$.

When a poset is regarded as a category, meets are exactly products. They do not always exist, but when they do, they are unique. The meet of $x$ and $y$ is usually written as $x\wedge y$ rather than $x\times y$. Thus, in the three examples above,

$$
x\wedge y=\min\{x,y\},\qquad X\wedge Y=X\cap Y,\qquad x\wedge y=\gcd(x,y),
$$

the second example being the origin of the notation.

We have been discussing products $X\times Y$ of *two* objects, so-called **binary products**. But there is no reason to stick to two. We can just as well talk about products $X\times Y\times Z$ of three objects, or of infinitely many objects. The definition changes in the most obvious way:

**Definition 5.1.7** Let $\mathscr{A}$ be a category, $I$ a set, and $(X_i)_{i\in I}$ a family of objects of $\mathscr{A}$. A **product** of $(X_i)_{i\in I}$ consists of an object $P$ and a family of maps

$$
\bigl(P\xrightarrow{p_i}X_i\bigr)_{i\in I}
$$

with the property that for all objects $A$ and families of maps

$$
\bigl(A\xrightarrow{f_i}X_i\bigr)_{i\in I}\tag{5.3}
$$

there exists a unique map $\bar f:A\to P$ such that $p_i\circ\bar f=f_i$ for all $i\in I$.

Remarks 5.1.2 apply equally to this definition. When the product $P$ exists, we write $P$ as $\prod_{i\in I}X_i$ and the map $\bar f$ as $(f_i)_{i\in I}$. We call the maps $f_i$ the **components** of the map $(f_i)_{i\in I}$. Taking $I$ to be a two-element set, we recover the special case of binary products.

**Example 5.1.8** In ordered sets, the extension from binary to arbitrary products works in the obvious way: given an ordered set $(A,\leq)$, a **lower bound** for a family $(x_i)_{i\in I}$ of elements is an element $a\in A$ such that $a\leq x_i$ for all $i$, and a **greatest lower bound** or **meet** of the family is a lower bound greater than any other, written as $\bigwedge_{i\in I}x_i$. These are the products in $(A,\leq)$.

For example, in $\mathbb{R}$ with its usual ordering, the meet of a family $(x_i)_{i\in I}$ is $\inf\{x_i\mid i\in I\}$ (and one exists if and only if the other does).

**Example 5.1.9** What happens to the definition of product when the indexing set $I$ is empty? Let $\mathscr{A}$ be a category. In general, an $I$-indexed family $(X_i)_{i\in I}$ of <span class="original-page-anchor" id="pdf-page-121" aria-hidden="true"></span>objects of $\mathscr{A}$ is a function $I\to\operatorname{ob}(\mathscr{A})$. When $I$ is empty, there is exactly one such function. In other words, there is exactly one family $(X_i)_{i\in\emptyset}$, the **empty family**. Similarly, when $I$ is empty, there is exactly one family (5.3) for any given object $A$.

A product of the empty family therefore consists of an object $P$ of $\mathscr{A}$ such that for each object $A$ of $\mathscr{A}$, there exists a unique map $\bar f:A\to P$. (The condition ‘$p_i\circ\bar f=f_i$ for all $i\in I$’ holds trivially.) In other words, a product of the empty family is exactly a terminal object.

We have been writing $1$ for terminal objects, which was justified by the fact that in categories such as $\mathbf{Set}$, $\mathbf{Top}$, $\mathbf{Ring}$ and $\mathbf{Grp}$, the terminal object has one element. But we have just seen that the terminal object is the product of no things, which in the context of elementary arithmetic is the number $1$. This is a second, related, reason for the notation.

**Example 5.1.10** Take an object $X$ of a category $\mathscr{A}$, and a set $I$. There is a constant family $(X)_{i\in I}$. Its product $\prod_{i\in I}X$, if it exists, is written as $X^I$ and called a **power** of $X$.

We met powers in $\mathbf{Set}$ in Section 3.1. When $X$ is a set, $X^I$ is the set of functions from $I$ to $X$, also written as $\mathbf{Set}(I,X)$.

### Equalizers

To define our second type of limit, we need a preliminary piece of terminology: a **fork** in a category consists of objects and maps

![Fork (5.4)](/library/volume-87/diagrams/pdf-0121-fork-5-4.png)

such that $sf=tf$.

**Definition 5.1.11** Let $\mathscr{A}$ be a category and let $X\overset{s}{\underset{t}{\rightrightarrows}}Y$ be objects and maps in $\mathscr{A}$. An **equalizer** of $s$ and $t$ is an object $E$ together with a map $E\xrightarrow{i}X$ such that

![Equalizer fork](/library/volume-87/diagrams/pdf-0121-equalizer.png)

is a fork, and with the property that for any fork (5.4), there exists a unique map $\bar f:A\to E$ such that

![Equalizer universal property (5.5)](/library/volume-87/diagrams/pdf-0121-universal-5-5.png)

<span class="original-page-anchor" id="pdf-page-122" aria-hidden="true"></span>

commutes.

Remarks 5.1.2 on products apply to equalizers too.

**Example 5.1.12** We have already met equalizers in $\mathbf{Set}$ (Section 3.1). They really are equalizers in the sense of Definition 5.1.11. Indeed, take sets and functions $X\overset{s}{\underset{t}{\rightrightarrows}}Y$, write

$$
E=\{x\in X\mid s(x)=t(x)\},
$$

and write $i:E\to X$ for the inclusion. Then $si=ti$, so we have a fork, and one can check that it is universal among all forks on $s$ and $t$.

An equalizer describes the set of solutions of a single equation, but by combining equalizers with products, we can also describe the solution-set of any system of simultaneous equations. Take a set $\Lambda$ and a family

![Family of pairs of maps](/library/volume-87/diagrams/pdf-0122-family.png)

of pairs of maps in $\mathbf{Set}$. Then the solution-set

$$
\{x\in X\mid s_\lambda(x)=t_\lambda(x)\text{ for all }\lambda\in\Lambda\}
$$

is the equalizer of the functions

![Functions to the product](/library/volume-87/diagrams/pdf-0122-product-pair.png)

(using the notation introduced after Definition 5.1.7). To see this, observe that for $x\in X$,

$$
\begin{aligned}
(s_\lambda)_{\lambda\in\Lambda}(x)=(t_\lambda)_{\lambda\in\Lambda}(x)
&\iff\bigl(s_\lambda(x)\bigr)_{\lambda\in\Lambda}=\bigl(t_\lambda(x)\bigr)_{\lambda\in\Lambda}\\
&\iff s_\lambda(x)=t_\lambda(x)\text{ for all }\lambda\in\Lambda,
\end{aligned}
$$

as required.

**Example 5.1.13** Take continuous maps $X\overset{s}{\underset{t}{\rightrightarrows}}Y$ between topological spaces. We can form their equalizer $E$ in the category of sets, with inclusion map $i:E\to X$, say. Since $E$ is a subset of the space $X$, it acquires the subspace topology from $X$, and $i$ is then continuous. This space $E$, together with $i$, is the equalizer of $s$ and $t$.

Showing this amounts to showing that for any fork (5.4) in $\mathbf{Top}$, the induced function $\bar f$ is continuous. This follows from the definition of the subspace topology, which is the smallest topology such that the inclusion map is continuous. Compare the remarks on products in Example 5.1.4.

<span class="original-page-anchor" id="pdf-page-123" aria-hidden="true"></span>

**Example 5.1.14** Let $\theta:G\to H$ be a homomorphism of groups. As in Example 0.8, the homomorphism $\theta$ gives rise to a fork

![Kernel fork](/library/volume-87/diagrams/pdf-0123-kernel.png)

where $\iota$ is the inclusion and $\varepsilon$ is the trivial homomorphism. This is an equalizer in $\mathbf{Grp}$. Showing this amounts to showing that the map that we have been calling $\bar f$ is a homomorphism, which is left to the reader.

Thus, kernels are a special case of equalizers.

**Example 5.1.15** Let $V\overset{s}{\underset{t}{\rightrightarrows}}W$ be linear maps between vector spaces. There is a linear map $t-s:V\to W$, and the equalizer of $s$ and $t$ in the category of vector spaces is the space $\ker(t-s)$ together with the inclusion map $\ker(t-s)\hookrightarrow V$.

### Pullbacks

We explore one more type of limit before formulating the general definition.

**Definition 5.1.16** Let $\mathscr{A}$ be a category, and take objects and maps

![Pullback diagram (5.6)](/library/volume-87/diagrams/pdf-0123-corner-5-6.png)

in $\mathscr{A}$. A **pullback** of this diagram is an object $P\in\mathscr{A}$ together with maps $p_1:P\to X$ and $p_2:P\to Y$ such that

![Pullback square (5.7)](/library/volume-87/diagrams/pdf-0123-square-5-7.png)

commutes, and with the property that for any commutative square

![Commutative square (5.8)](/library/volume-87/diagrams/pdf-0123-cone-5-8.png)

<span class="original-page-anchor" id="pdf-page-124" aria-hidden="true"></span>

in $\mathscr{A}$, there is a unique map $\bar f:A\to P$ such that

![Pullback universal property (5.9)](/library/volume-87/diagrams/pdf-0124-universal-5-9.png)

commutes. (For (5.9) to commute means only that $p_1\bar f=f_1$ and $p_2\bar f=f_2$, since the commutativity of the square is already given.)

Again, Remarks 5.1.2 apply.

We call (5.7) a **pullback square**. Another name for pullback is **fibred product**. This name is partially explained by the following fact: when $Z$ is a terminal object (and $s$ and $t$ are the only maps they can possibly be), a pullback of the diagram (5.6) is simply a product of $X$ and $Y$.

**Examples 5.1.17 (Pullbacks in $\mathbf{Set}$)** The pullback of a diagram (5.6) in $\mathbf{Set}$ is

$$
P=\{(x,y)\in X\times Y\mid s(x)=t(y)\}
$$

with projections $p_1$ and $p_2$ given by $p_1(x,y)=x$ and $p_2(x,y)=y$.

Although you might not be familiar with general pullbacks in $\mathbf{Set}$, there are at least two instances that you are likely to have met.

(a) A basic construction with sets and functions is the formation of inverse images. They are an instance of pullbacks. Indeed, given a function $f:X\to Y$ and a subset $Y'\subseteq Y$, we obtain a new set, the inverse image

$$
f^{-1}Y'=\{x\in X\mid f(x)\in Y'\}\subseteq X,
$$

and a new function,

$$
\begin{array}{cccc}
f':&f^{-1}Y'&\to&Y'\\
&x&\mapsto&f(x).
\end{array}
$$

We also have the inclusion functions $j:Y'\hookrightarrow Y$ and $i:f^{-1}Y'\hookrightarrow X$. Putting everything together gives a commutative square

![Inverse image square (5.10)](/library/volume-87/diagrams/pdf-0124-inverse-5-10.png)

<span class="original-page-anchor" id="pdf-page-125" aria-hidden="true"></span>

The data we started with was the lower-right part of this square ($X$, $Y$, $Y'$, $f$ and $j$), and from it we constructed the rest of the square ($f^{-1}Y'$, $f'$ and $i$).

The square (5.10) is a pullback. Let us verify this in detail. Take any commutative square

![Commutative square for the inverse image](/library/volume-87/diagrams/pdf-0125-cone.png)

We must show that there is a unique map $k:A\to f^{-1}Y'$ such that

![Universal property of the inverse image](/library/volume-87/diagrams/pdf-0125-universal.png)

commutes. For uniqueness, let $k$ be a map making the diagram commute. Then for all $a\in A$, we have $i(k(a))=g(a)$, that is, $k(a)=g(a)$, and this determines $k$ uniquely. For existence, first note that for all $a\in A$ we have $f(g(a))=j(h(a))\in Y'$, so $g(a)\in f^{-1}Y'$. Hence we may define $k:A\to f^{-1}Y'$ by $k(a)=g(a)$ for all $a\in A$. Then for all $a\in A$, we have $i(k(a))=k(a)=g(a)$ and

$$
f'(k(a))=f(k(a))=f(g(a))=j(h(a))=h(a).
$$

Hence $i\circ k=g$ and $f'\circ k=h$, as required.

(b) Intersection of subsets provides another example of pullbacks. Indeed, let $X$ and $Y$ be subsets of a set $Z$. Then

![Intersection as a pullback](/library/volume-87/diagrams/pdf-0125-intersection.png)

is a pullback square, where all the arrows are inclusions of subsets.

In fact, this is a special case of (a), since $X\cap Y$ is the inverse image of $Y\subseteq Z$ under the inclusion map $X\hookrightarrow Z$.

<span class="original-page-anchor" id="pdf-page-126" aria-hidden="true"></span>

In the situation of Example 5.1.17(a), where we have a map $f:X\to Y$ and a subset $Y'$ of $Y$, people sometimes say that $f^{-1}Y'$ is obtained by ‘pulling $Y'$ back’ along $f$: hence the name.

### The definition of limit

We have now looked at three constructions: products, equalizers and pullbacks. They clearly have something in common. Each starts with some objects and (in the case of equalizers and pullbacks) some maps between them. In each, we aim to construct a new object together with some maps from it to the original objects, with a universal property.

Let us analyse this more closely. What is the starting data in each construction? For (binary) products, it is a pair of objects

$$
X\qquad Y.\tag{5.11}
$$

For equalizers, it is a diagram

![Equalizer data (5.12)](/library/volume-87/diagrams/pdf-0126-equalizer-5-12.png)

For pullbacks, it is a diagram

![Pullback data (5.13)](/library/volume-87/diagrams/pdf-0126-pullback-5-13.png)

In Definition 4.1.25, we met the notion of generalized element, and we saw there that the ‘figures’ in a geometric object can often be described by maps into it. For instance, a curve in a topological space $A$ can be thought of as a map $\mathbb{R}\to A$. Similarly, an object of a category $\mathscr{A}$ amounts to a functor $D:\mathbf{1}\to\mathscr{A}$; think of $\mathbf{1}=\boxed{\bullet}$ as an unlabelled object and $D$ as labelling it with the name of an object of $\mathscr{A}$. And similarly again, a map in a category $\mathscr{A}$ is a functor $\mathbf{2}\to\mathscr{A}$, where $\mathbf{2}=\boxed{\bullet\to\bullet}$. (Here $\mathbf{2}$ is the category with two objects, say $0$ and $1$, with one map $0\to1$, and with no other maps except for identities.) Finally, if we take $\mathbf{I}$ to be one of the categories

![Limit shape categories (5.14)](/library/volume-87/diagrams/pdf-0126-shapes-5-14.png)

then a functor $\mathbf{I}\to\mathscr{A}$ consists of data (5.11), (5.12) or (5.13) in $\mathscr{A}$, respectively.

<span class="original-page-anchor" id="pdf-page-127" aria-hidden="true"></span>

![The definition of limit](/library/volume-87/diagrams/pdf-0127-limit-figure.png)

Figure 5.1 The definition of limit.

We have just begun to use the convention that one typeface ($\mathbf{A},\mathbf{B},\mathbf{C},\ldots$) denotes small categories, and another ($\mathscr{A},\mathscr{B},\mathscr{C},\ldots$) denotes arbitrary categories. Although not strictly necessary, this convention is helpful, since small categories and arbitrary categories often play different roles in the theory.

**Definition 5.1.18** Let $\mathscr{A}$ be a category and $\mathbf{I}$ a small category. A functor $\mathbf{I}\to\mathscr{A}$ is called a **diagram** in $\mathscr{A}$ of **shape $\mathbf{I}$**.

So (5.11), (5.12) and (5.13) are diagrams of shape $\mathbf{T}$, $\mathbf{E}$ and $\mathbf{P}$.

We already have the definitions of product of a diagram of shape $\mathbf{T}$, equalizer of a diagram of shape $\mathbf{E}$, and pullback of a diagram of shape $\mathbf{P}$. We now unify them in the definition of limit (Figure 5.1).

**Definition 5.1.19** Let $\mathscr{A}$ be a category, $\mathbf{I}$ a small category, and $D:\mathbf{I}\to\mathscr{A}$ a diagram in $\mathscr{A}$.

(a) A **cone** on $D$ is an object $A\in\mathscr{A}$ (the **vertex** of the cone) together with a family

$$
\bigl(A\xrightarrow{f_I}D(I)\bigr)_{I\in\mathbf{I}}\tag{5.15}
$$

of maps in $\mathscr{A}$ such that for all maps $I\xrightarrow{u}J$ in $\mathbf{I}$, the triangle

![Cone compatibility triangle](/library/volume-87/diagrams/pdf-0127-cone-triangle.png)

commutes. (Here and later, we abbreviate $D(u)$ as $Du$.)

(b) A **limit** of $D$ is a cone $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ with the property that for any cone (5.15) on $D$, there exists a unique map $\bar f:A\to L$ such that $p_I\circ\bar f=f_I$ for all $I\in\mathbf{I}$. The maps $p_I$ are called the **projections** of the limit.

<span class="original-page-anchor" id="pdf-page-128" aria-hidden="true"></span>

**Remarks 5.1.20** (a) Loosely, the universal property says that for any $A\in\mathscr{A}$, maps $A\to L$ correspond one-to-one with cones on $D$ with vertex $A$. (Any map $g:A\to L$ gives rise to a cone $\bigl(A\xrightarrow{p_Ig}D(I)\bigr)_{I\in\mathbf{I}}$, and the definition of limit is that for each $A$, this process is bijective.) In Section 6.1, we will use this thought to rephrase the definition of limit in terms of representability. From this it will follow that limits are unique up to canonical isomorphism, when they exist (Corollary 6.1.2). Alternatively, uniqueness can be proved by the usual kind of direct argument, as in Lemma 2.1.8.

(b) If $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ is a limit of $D$, we sometimes abuse language slightly by referring to $L$ (rather than the whole cone) as the limit of $D$. For emphasis, we sometimes call $\bigl(L\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ a **limit cone**. We write $L=\lim_{\leftarrow\mathbf{I}}D$. Remark (a) can then be stated as:

*A map into $\lim_{\leftarrow\mathbf{I}}D$ is a cone on $D$.*

(c) By assuming from the outset that the shape category $\mathbf{I}$ is small, we are restricting ourselves to what are officially called **small limits**. We will seldom be interested in any other kind.

**Examples 5.1.21 (Limit shapes)** Let $\mathscr{A}$ be any category. Recall the categories $\mathbf{T}$, $\mathbf{E}$ and $\mathbf{P}$ of (5.14).

(a) A diagram $D$ of shape $\mathbf{T}$ in $\mathscr{A}$ is a pair $(X,Y)$ of objects of $\mathscr{A}$. A cone on $D$ is an object $A$ together with maps $f_1:A\to X$ and $f_2:A\to Y$ (as in Definition 5.1.1), and a limit of $D$ is a product of $X$ and $Y$.

More generally, let $I$ be a set and write $\mathbf{I}$ for the discrete category on $I$. A functor $D:\mathbf{I}\to\mathscr{A}$ is an $I$-indexed family $(X_i)_{i\in I}$ of objects of $\mathscr{A}$, and a limit of $D$ is exactly a product of the family $(X_i)_{i\in I}$.

In particular, a limit of the unique functor $\emptyset\to\mathscr{A}$ is a terminal object of $\mathscr{A}$, where $\emptyset$ denotes the empty category.

(b) A diagram $D$ of shape $\mathbf{E}$ in $\mathscr{A}$ is a parallel pair $X\overset{s}{\underset{t}{\rightrightarrows}}Y$ of maps in $\mathscr{A}$. A cone on $D$ consists of objects and maps

![Cone on a parallel pair](/library/volume-87/diagrams/pdf-0128-parallel-cone.png)

such that $s\circ f=g$ and $t\circ f=g$. But since $g$ is determined by $f$, it is equivalent to say that a cone on $D$ consists of an object $A$ and a map $f:$

<span class="original-page-anchor" id="pdf-page-129" aria-hidden="true"></span>

$A\to X$ such that

![Fork on the parallel pair](/library/volume-87/diagrams/pdf-0129-fork.png)

is a fork. A limit of $D$ is a universal fork on $s$ and $t$, that is, an equalizer of $s$ and $t$.

(c) A diagram $D$ of shape $\mathbf{P}$ in $\mathscr{A}$ consists of objects and maps

![Diagram of pullback shape](/library/volume-87/diagrams/pdf-0129-corner.png)

in $\mathscr{A}$. Performing a simplification similar to that in (b), we see that a cone on $D$ is a commutative square (5.8). A limit of $D$ is a pullback.

(d) Let $\mathbf{I}=(\mathbb{N},\leq)^{\mathrm{op}}$. A diagram $D:\mathbf{I}\to\mathscr{A}$ consists of objects and maps

$$
\cdots\xrightarrow{s_3}X_2\xrightarrow{s_2}X_1\xrightarrow{s_1}X_0.
$$

For example, suppose that we have a set $X_0$ and a chain of subsets

$$
\cdots\subseteq X_2\subseteq X_1\subseteq X_0.
$$

The inclusion maps form a diagram in $\mathbf{Set}$ of the type above, and its limit is $\bigcap_{i\in\mathbb{N}}X_i$. In this and similar contexts, limits are sometimes referred to as **inverse limits**, although many category theorists regard this usage as old-fashioned.

In general, the limit of a diagram $D$ is the terminal object in the category of cones on $D$, and is therefore an extremal example of a cone on $D$. The word ‘limit’ can be understood as meaning ‘on the boundary’, rather than indicating a limiting process of the type encountered in analysis. Nevertheless, the two ideas make contact in Example 5.1.21(d).

We have said little so far about which limits exist, except to observe in Remark 5.1.2(a) that they do not exist always. We now show that in many familiar categories, all limits do exist; indeed, we can construct them explicitly.

**Example 5.1.22** Let $D:\mathbf{I}\to\mathbf{Set}$ and, as a kind of thought experiment, let us ask ourselves what $\lim_{\leftarrow\mathbf{I}}D$ would have to be if it existed. (We do not know yet <span class="original-page-anchor" id="pdf-page-130" aria-hidden="true"></span>that it does.) We would have

$$
\begin{aligned}
\varprojlim_{\mathbf{I}}D
&\cong\mathbf{Set}\left(1,\varprojlim_{\mathbf{I}}D\right)\\
&\cong\{\text{cones on }D\text{ with vertex }1\}\\
&\cong\Bigl\{(x_I)_{I\in\mathbf{I}}\ \Big|\ x_I\in D(I)\text{ for all }I\in\mathbf{I}\text{ and }(Du)(x_I)=x_J\\
&\hspace{5em}\text{for all }I\xrightarrow{u}J\text{ in }\mathbf{I}\Bigr\},
\end{aligned}\tag{5.16}
$$

where the second isomorphism is by Remark 5.1.20(a) and the third is by definition of cone. In fact, (5.16) really *is* the limit of $D$ in $\mathbf{Set}$, with projections $p_J:\varprojlim_{\mathbf{I}}D\to D(J)$ given by $p_J((x_I)_{I\in\mathbf{I}})=x_J$ (Exercise 5.1.37). So in $\mathbf{Set}$, all limits exist.

**Example 5.1.23** The same formula gives limits in categories of algebras such as $\mathbf{Grp}$, $\mathbf{Ring}$, $\mathbf{Vect}_k$, $\ldots$. Of course, we also have to say what the group/ring/$\ldots$ structure on the set (5.16) is, but this works in the most straightforward way imaginable. For instance, in $\mathbf{Vect}_k$, if $(x_I)_{I\in\mathbf{I}},(y_I)_{I\in\mathbf{I}}\in\varprojlim_{\mathbf{I}}D$ then

$$
(x_I)_{I\in\mathbf{I}}+(y_I)_{I\in\mathbf{I}}=(x_I+y_I)_{I\in\mathbf{I}}.
$$

**Example 5.1.24** The same formula also gives limits in $\mathbf{Top}$. The topology on the set (5.16) is the smallest for which the projection maps are continuous.

**Definition 5.1.25** (a) Let $\mathbf{I}$ be a small category. A category $\mathscr{A}$ **has limits of shape $\mathbf{I}$** if for every diagram $D$ of shape $\mathbf{I}$ in $\mathscr{A}$, a limit of $D$ exists.

(b) A category **has all limits** (or properly, **has small limits**) if it has limits of shape $\mathbf{I}$ for all small categories $\mathbf{I}$.

Thus, $\mathbf{Set}$, $\mathbf{Top}$, $\mathbf{Grp}$, $\mathbf{Ring}$, $\mathbf{Vect}_k$, $\ldots$ all have all limits.

Similar terminology can be applied to special classes of limits (for instance, ‘has pullbacks’). The class of finite limits is particularly important. By definition, a category is **finite** if it contains only finitely many maps (in which case it also contains only finitely many objects). A **finite limit** is a limit of shape $\mathbf{I}$ for some finite category $\mathbf{I}$. For instance, binary products, terminal objects, equalizers and pullbacks are all finite limits.

The next result tells us that all limits can be built up from limits of just a few familiar, basic types.

**Proposition 5.1.26** *Let $\mathscr{A}$ be a category.*

(a) *If $\mathscr{A}$ has all products and equalizers then $\mathscr{A}$ has all limits.*

(b) *If $\mathscr{A}$ has binary products, a terminal object and equalizers then $\mathscr{A}$ has finite limits.*

<span class="original-page-anchor" id="pdf-page-131" aria-hidden="true"></span>

To understand the idea, consider formula (5.16) for limits in $\mathbf{Set}$. There, the limit of a diagram $D$ is described as the subset of the product $\prod_{I\in\mathbf{I}}D(I)$ consisting of those elements for which certain equations hold. We saw in Example 5.1.12 that the set of solutions to any system of simultaneous equations can be described via products and equalizers. Thus, we can describe any limit in $\mathbf{Set}$ in terms of products and equalizers. And in fact, this same description is valid in any category.

We now examine this idea more closely, in preparation for the proof (Exercise 5.1.38). First-time readers may wish to skip the next two paragraphs, resuming at Example 5.1.27.

Equation (5.16) states that in $\mathbf{Set}$, the limit of a diagram $D:\mathbf{I}\to\mathbf{Set}$ consists of the elements $(x_I)_{I\in\mathbf{I}}\in\prod_{I\in\mathbf{I}}D(I)$ such that

$$
(Du)(x_J)=x_K
$$

in $D(K)$ for each map $J\xrightarrow{u}K$ in $\mathbf{I}$. For each such map $u$, define maps

![Component maps](/library/volume-87/diagrams/pdf-0131-component-pair.png)

by

$$
s_u((x_I)_{I\in\mathbf{I}})=(Du)(x_J),\qquad t_u((x_I)_{I\in\mathbf{I}})=x_K.
$$

Then $\varprojlim_{\mathbf{I}}D$ is the set of families $x=(x_I)_{I\in\mathbf{I}}$ satisfying the equation $s_u(x)=t_u(x)$ for each map $u$ in $\mathbf{I}$. It follows from Example 5.1.12 that $\varprojlim_{\mathbf{I}}D$ is the equalizer of

![Maps between products](/library/volume-87/diagrams/pdf-0131-product-pair.png)

where $s$ and $t$ are the maps with components $s_u$ and $t_u$, respectively.

We have now described any limit in $\mathbf{Set}$ in terms of products and equalizers. Although our argument took place entirely in $\mathbf{Set}$, it suggests how we might proceed in an arbitrary category. With this in mind, the proof of Proposition 5.1.26 is routine, and is left as Exercise 5.1.38.

**Example 5.1.27** Let $\mathbf{CptHff}$ denote the category of compact Hausdorff spaces and continuous maps. It is a classic exercise in topology to show that given continuous maps $s$ and $t$ from a topological space $X$ to a Hausdorff space $Y$, the subset $\{x\in X\mid s(x)=t(x)\}$ of $X$ is closed. From this it follows that $\mathbf{CptHff}$ has equalizers. Also, Tychonoff’s theorem states that any product (in $\mathbf{Top}$) of compact spaces is compact, and it is easy to show that any product (in <span class="original-page-anchor" id="pdf-page-132" aria-hidden="true"></span>$\mathbf{Top}$) of Hausdorff spaces is Hausdorff. From this it follows that $\mathbf{CptHff}$ has all products. Hence by Proposition 5.1.26(a), $\mathbf{CptHff}$ has all limits.

**Example 5.1.28** Recall from Example 5.1.15 that kernels provide equalizers in $\mathbf{Vect}_k$. By Proposition 5.1.26(b), finite limits in $\mathbf{Vect}_k$ can always be expressed in terms of $\oplus$ (binary direct sum), $\{0\}$, and kernels. The same is true in $\mathbf{Ab}$.

### Monics

For functions between sets, injectivity is an important concept. For maps in an arbitrary category, injectivity does not make sense, but there is a concept that plays a similar role.

**Definition 5.1.29** Let $\mathscr{A}$ be a category. A map $X\xrightarrow{f}Y$ in $\mathscr{A}$ is **monic** (or a **monomorphism**) if for all objects $A$ and maps $A\overset{x}{\underset{x'}{\rightrightarrows}}X$,

$$
f\circ x=f\circ x'\implies x=x'.
$$

This can be rephrased suggestively in terms of generalized elements: $f$ is monic if for all generalized elements $x$ and $x'$ of $X$ (of the same shape), $fx=fx'\implies x=x'$. Being monic is, therefore, the generalized-element analogue of injectivity.

**Example 5.1.30** In $\mathbf{Set}$, a map is monic if and only if it is injective. Indeed, if $f$ is injective then certainly $f$ is monic, and for the converse, take $A=1$.

**Example 5.1.31** In categories of algebras such as $\mathbf{Grp}$, $\mathbf{Vect}_k$, $\mathbf{Ring}$, etc., it is also true that the monic maps are exactly the injections. Again, it is easy to show that injections are monic. For the converse, take $A=F(1)$ where $F$ is the free functor (Examples 2.1.3).

Why is the definition of monic in a chapter on limits? Because of this:

**Lemma 5.1.32** *A map $X\xrightarrow{f}Y$ is monic if and only if the square*

![Monic pullback square](/library/volume-87/diagrams/pdf-0132-monic-pullback.png)

*is a pullback.*

**Proof** Exercise 5.1.41. $\square$ <span class="original-page-anchor" id="pdf-page-133" aria-hidden="true"></span>The significance of this lemma is that whenever we prove a result about limits, a result about monics will follow. For example, we will soon show that the forgetful functors from $\mathbf{Grp}$, $\mathbf{Vect}_k$, etc., to $\mathbf{Set}$ preserve limits (in a sense to be defined), from which it will follow immediately that they also preserve monics. This in turn gives an alternative proof that monics in these categories are injective.

### Exercises

**5.1.33** Verify that in the category of vector spaces, the product of two vector spaces is their direct sum (Example 5.1.5).

**5.1.34** Take objects and maps $E\xrightarrow{i}X\overset{f}{\underset{g}{\rightrightarrows}}Y$ in some category. If this is an equalizer, is the square

![Equalizer and pullback square](/library/volume-87/diagrams/pdf-0133-equalizer-square.png)

necessarily a pullback? What about the converse? Give proofs or counterexamples.

**5.1.35** Take a commutative diagram

![Two adjacent squares](/library/volume-87/diagrams/pdf-0133-pasting-pullbacks.png)

in some category. Suppose that the right-hand square is a pullback. Show that the left-hand square is a pullback if and only if the outer rectangle is a pullback.

**5.1.36** Let $D:\mathbf{I}\to\mathscr{A}$ be a diagram and $(L\xrightarrow{p_I}D(I))_{I\in\mathbf{I}}$ a limit cone on $D$.

(a) Prove that whenever $A\overset{h}{\underset{h'}{\rightrightarrows}}L$ are maps such that $p_I\circ h=p_I\circ h'$ for all $I\in\mathbf{I}$, then $h=h'$.

(b) What does the result of (a) mean when $\mathbf{I}$ is the two-object discrete category, $\mathscr{A}=\mathbf{Set}$, and $A=1$? Answer without using any category-theoretic terminology.

**5.1.37** Show that the set (5.16) in Example 5.1.22 really is a limit of $D$.

<span class="original-page-anchor" id="pdf-page-134" aria-hidden="true"></span>

**5.1.38** In this exercise, you will prove Proposition 5.1.26, following the plan described after the statement of that proposition.

(a) Let $\mathscr{A}$ be a category with all products and equalizers. Let $D:\mathbf{I}\to\mathscr{A}$ be a diagram in $\mathscr{A}$. Define maps

![Product maps](/library/volume-87/diagrams/pdf-0134-product-pair.png)

as follows: given $J\xrightarrow{u}K$ in $\mathbf{I}$, the $u$-component of $s$ is the composite

$$
\prod_{I\in\mathbf{I}}D(I)\xrightarrow{\operatorname{pr}_J}D(J)\xrightarrow{Du}D(K)
$$

(where $\operatorname{pr}$ denotes a product projection), and the $u$-component of $t$ is $\operatorname{pr}_K$. Let $L\xrightarrow{p}\prod_{I\in\mathbf{I}}D(I)$ be the equalizer of $s$ and $t$, and write $p_I$ for the $I$-component of $p$. Show that $(L\xrightarrow{p_I}D(I))_{I\in\mathbf{I}}$ is a limit cone on $D$, thus proving Proposition 5.1.26(a).

(b) Adapt the argument to prove Proposition 5.1.26(b).

**5.1.39** Prove that a category with pullbacks and a terminal object has all finite limits.

**5.1.40** Let $\mathscr{A}$ be a category and $A\in\mathscr{A}$. A **subobject** of $A$ is an isomorphism class of monics into $A$. More precisely, let $\mathbf{Monic}(A)$ be the full subcategory of $\mathscr{A}/A$ whose objects are the monics; then a subobject of $A$ is an isomorphism class of objects of $\mathbf{Monic}(A)$.

(a) Let $X\xrightarrow{m}A$ and $X'\xrightarrow{m'}A$ be monics in $\mathbf{Set}$. Show that $m$ and $m'$ are isomorphic in $\mathbf{Monic}(A)$ if and only if they have the same image. Deduce that the subobjects of $A$ are in canonical one-to-one correspondence with the subsets of $A$.

(b) Part (a) says that in $\mathbf{Set}$, subobjects are subsets. What are subobjects in $\mathbf{Grp}$, $\mathbf{Ring}$ and $\mathbf{Vect}_k$?

(c) What are subobjects in $\mathbf{Top}$? (Careful!)

**5.1.41** Prove Lemma 5.1.32.

**5.1.42** Let

![Pullback of a monic](/library/volume-87/diagrams/pdf-0134-pullback-monic.png)

<span class="original-page-anchor" id="pdf-page-135" aria-hidden="true"></span>

be a pullback square in some category. Show that if $m$ is monic then so is $m'$. (We already know this in the category of sets, by Example 5.1.17(a).)

## 5.2 Colimits: definition and examples

We have seen that examples of limits occur throughout mathematics. It therefore makes sense to examine the dual concept, colimit, and ask whether it is similarly ubiquitous.

By dualizing, we can write down the definition of colimit immediately. We then specialize to sums, coequalizers and pushouts, the duals of products, equalizers and pullbacks.

There are two common conventions for naming dual concepts: sometimes we add or subtract the prefix ‘co’ (as in limit/colimit), and sometimes we use ‘left’ and ‘right’ (as for adjoints). There are also some irregular names, such as terminal/initial object and pullback/pushout.

**Definition 5.2.1** Let $\mathscr{A}$ be a category and $\mathbf{I}$ a small category. Let $D:\mathbf{I}\to\mathscr{A}$ be a diagram in $\mathscr{A}$, and write $D^{\mathrm{op}}$ for the corresponding functor $\mathbf{I}^{\mathrm{op}}\to\mathscr{A}^{\mathrm{op}}$. A **cocone** on $D$ is a cone on $D^{\mathrm{op}}$, and a **colimit** of $D$ is a limit of $D^{\mathrm{op}}$.

Explicitly, a cocone on $D$ is an object $A\in\mathscr{A}$ (the **vertex** of the cocone) together with a family

$$
\left(D(I)\xrightarrow{f_I}A\right)_{I\in\mathbf{I}}\tag{5.17}
$$

of maps in $\mathscr{A}$ such that for all maps $I\xrightarrow{u}J$ in $\mathbf{I}$, the diagram

![Cocone condition](/library/volume-87/diagrams/pdf-0135-cocone.png)

commutes. A colimit of $D$ is a cocone

$$
\left(D(I)\xrightarrow{p_I}C\right)_{I\in\mathbf{I}}
$$

with the property that for any cocone (5.17) on $D$, there is a unique map $\bar{f}:C\to A$ such that $\bar{f}\circ p_I=f_I$ for all $I\in\mathbf{I}$. The associated picture is the mirror image of Figure 5.1.

Of course, Remarks 5.1.20 apply equally here. We write (the vertex of) the colimit as $\varinjlim_{\mathbf{I}}D$, and call the maps $p_I$ **coprojections**.

<span class="original-page-anchor" id="pdf-page-136" aria-hidden="true"></span>

### Sums

**Definition 5.2.2** A **sum** or **coproduct** is a colimit over a discrete category. (That is, it is a colimit of shape $\mathbf{I}$ for some discrete category $\mathbf{I}$.)

Let $(X_i)_{i\in I}$ be a family of objects of a category. Their sum (if it exists) is written as $\sum_{i\in I}X_i$ or $\coprod_{i\in I}X_i$. When $I$ is a finite set $\{1,\ldots,n\}$, we write $\sum_{i\in I}X_i$ as $X_1+\cdots+X_n$, or as $0$ if $n=0$.

**Example 5.2.3** By the dual of Example 5.1.9, a sum of the empty family is exactly an initial object.

**Example 5.2.4** Sums in $\mathbf{Set}$ were described in Section 3.1. Let us look in detail at the universal property, in the case of binary sums. Take two sets, $X_1$ and $X_2$. Form their sum, $X_1+X_2$, and consider the inclusions

![Inclusions into a sum](/library/volume-87/diagrams/pdf-0136-sum-coprojections.png)

This is a colimit cocone. To prove this, we have to prove the following universal property: for any diagram

![Cocone for two sets](/library/volume-87/diagrams/pdf-0136-sum-cocone.png)

of sets and functions, there is a unique function $\bar{f}:X_1+X_2\to A$ making

![Universal property of the sum](/library/volume-87/diagrams/pdf-0136-sum-universal.png)

commute. Now, we noted in Section 3.1 that $p_1$ and $p_2$ are injections whose images partition $X_1+X_2$. This means that every element $x$ of $X_1+X_2$ is *either* equal to $p_1(x_1)$ for some $x_1\in X_1$ (and this $x_1$ is then unique), *or* equal to $p_2(x_2)$ for some $x_2\in X_2$ (and this $x_2$ is then unique), but not both. So we may define $\bar{f}(x)$ to be equal to $f_1(x_1)$ in the first case and $f_2(x_2)$ in the second. This defines a function $\bar{f}$ making the diagram commute, and it is clearly the unique function that does so.

**Example 5.2.5** Let $X_1$ and $X_2$ be vector spaces. There are linear maps

![Direct sum coprojections](/library/volume-87/diagrams/pdf-0136-direct-sum-coprojections.png)

defined by $i_1(x_1)=(x_1,0)$ and $i_2(x_2)=(0,x_2)$, and it can be checked that (5.18) <span class="original-page-anchor" id="pdf-page-137" aria-hidden="true"></span>is a colimit cocone in $\mathbf{Vect}_k$. Hence binary direct sums are sums in the categorical sense. This is remarkable, since we saw in Example 5.1.5 that $X_1\oplus X_2$ is also the *product* of $X_1$ and $X_2$! Contrast this with the category of sets (or almost any other category), where sums and products are very different.

**Example 5.2.6** Let $(A,\leq)$ be an ordered set. **Upper bounds** and **least upper bounds** (or **joins**) in $A$ are defined by dualizing the definitions in Example 5.1.6, and, dually, they are sums in the corresponding category. The join of a family $(x_i)_{i\in I}$ is written as $\bigvee_{i\in I}x_i$. In the binary case (where $I$ has two elements), the join of $x_1$ and $x_2$ is written as $x_1\vee x_2$. A join of the empty family (where $I=\emptyset$) is an initial object of the category $A$, as in Example 5.2.3. Equivalently, it is a **least element** of $A$: an element $0\in A$ such that $0\leq a$ for all $a\in A$.

For instance, in $(\mathbb{R},\leq)$, join is supremum and there is no least element. In a power set $(\mathscr{P}(S),\subseteq)$, join is union and the least element is $\emptyset$. In $(\mathbb{N},\mid)$, join is lowest common multiple and the least element is $1$ (since $1$ divides everything). So in this order on the natural numbers, $1$ is least; but also, everything divides $0$, so $0$ is greatest!

### Coequalizers

We continue to write $\mathbf{E}$ for the category $\boxed{\bullet\rightrightarrows\bullet}$.

**Definition 5.2.7** A **coequalizer** is a colimit of shape $\mathbf{E}$.

In other words, given a diagram $X\overset{s}{\underset{t}{\rightrightarrows}}Y$, a coequalizer of $s$ and $t$ is a map $Y\xrightarrow{p}C$ satisfying $p\circ s=p\circ t$ and universal with this property.

We will see that coequalizers are something like quotients. But first, we need some background material on equivalence relations.

**Remarks 5.2.8** A binary relation $R$ on a set $A$ can be viewed as a subset $R\subseteq A\times A$. Think of $(a,a')\in R$ as meaning ‘$a$ and $a'$ are related’. We can speak of one relation $S$ on $A$ ‘containing’ another such relation, $R$. This means that $R\subseteq S$: whenever $a$ and $a'$ are $R$-related, they are also $S$-related.

We will need to use the fact that for any binary relation $R$ on a set $A$, there is a smallest equivalence relation $\sim$ containing $R$. This is called the equivalence relation **generated** by $R$. ‘Smallest’ means that any equivalence relation containing $R$ also contains $\sim$.

We can construct $\sim$ as the intersection of all equivalence relations on $A$ containing $R$, since the intersection of any family of equivalence relations is again an equivalence relation. There is also an explicit construction. The rough idea <span class="original-page-anchor" id="pdf-page-138" aria-hidden="true"></span>is as follows: writing $x\to y$ to mean $(x,y)\in R$, we should have $a\sim a'$ if and only if there is a zigzag such as

$$
a\to b\leftarrow c\leftarrow d\to e\leftarrow a'
$$

between $a$ and $a'$. To make this precise, we first define a relation $S$ on $A$ by

$$
S=\{(a,a')\in A\times A\mid(a,a')\in R\text{ or }(a',a)\in R\}
$$

(which enlarges $R$ to a symmetric relation), then define $\sim$ by declaring that $a\sim a'$ if and only if there exist $n\geq0$ and $a_0,\ldots,a_n\in A$ such that

$$
a=a_0,\ (a_0,a_1)\in S,\ (a_1,a_2)\in S,\ \ldots,\ (a_{n-1},a_n)\in S,\ a_n=a'
$$

(which forces reflexivity and transitivity, while preserving the symmetry).

Next, recall some facts about equivalence relations from Section 3.1. Given any equivalence relation $\sim$ on a set $A$, we can construct the set $A/{\sim}$ of equivalence classes and the quotient map $p:A\to A/{\sim}$. This quotient map $p$ is surjective and has the property that $p(a)=p(a')\iff a\sim a'$, for $a,a'\in A$. We saw that for any set $B$, the maps $A/{\sim}\to B$ correspond one-to-one (via composition with $p$) with the maps $f:A\to B$ such that

$$
\forall a,a'\in A,\qquad a\sim a'\implies f(a)=f(a').\tag{5.19}
$$

Finally, let us consider this universal property in the case where $\sim$ is the equivalence relation generated by some relation $R$. Condition (5.19) is then equivalent to:

$$
\forall a,a'\in A,\qquad (a,a')\in R\implies f(a)=f(a').\tag{5.20}
$$

(Proof: define an equivalence relation $\approx$ on $A$ by $a\approx a'\iff f(a)=f(a')$. Condition (5.19) says that ${\sim}\subseteq{\approx}$, and condition (5.20) that $R\subseteq{\approx}$. But $\sim$ is the smallest equivalence relation containing $R$, so these statements are equivalent.) In conclusion, for any set $B$, the maps $A/{\sim}\to B$ correspond one-to-one with the maps $f:A\to B$ satisfying (5.20).

**Example 5.2.9** Take sets and functions $X\overset{s}{\underset{t}{\rightrightarrows}}Y$. To find the coequalizer of $s$ and $t$, we must construct in some canonical way a set $C$ and a function $p:Y\to C$ such that $p(s(x))=p(t(x))$ for all $x\in X$. So, let $\sim$ be the equivalence relation on $Y$ generated by $s(x)\sim t(x)$ for all $x\in X$. (In other words, $\sim$ is generated by the relation

$$
R=\{(s(x),t(x))\mid x\in X\}
$$

on $Y$.) Take the quotient map $p:Y\to Y/{\sim}$. By the correspondence described in Remarks 5.2.8, this is indeed the coequalizer of $s$ and $t$.

<span class="original-page-anchor" id="pdf-page-139" aria-hidden="true"></span>

**Example 5.2.10** For each pair of homomorphisms $A\overset{s}{\underset{t}{\rightrightarrows}}B$ in $\mathbf{Ab}$, there is a homomorphism $t-s:A\to B$, which gives rise to a subgroup $\operatorname{im}(t-s)$ of $B$. The coequalizer of $s$ and $t$ is the canonical homomorphism $B\to B/\operatorname{im}(t-s)$. (Compare Example 5.1.15.)

### Pushouts

**Definition 5.2.11** A **pushout** is a colimit of shape

![Pushout shape](/library/volume-87/diagrams/pdf-0139-pushout-shape.png)

In other words, the pushout of a diagram

![Diagram for a pushout](/library/volume-87/diagrams/pdf-0139-pushout-diagram.png)

is (if it exists) a commutative square

![Pushout square](/library/volume-87/diagrams/pdf-0139-pushout-square.png)

that is universal as such. In other words still, a pushout in a category $\mathscr{A}$ is a pullback in $\mathscr{A}^{\mathrm{op}}$.

**Example 5.2.12** Take a diagram (5.21) in $\mathbf{Set}$. Its pushout $P$ is $(Y+Z)/{\sim}$, where $\sim$ is the equivalence relation on $Y+Z$ generated by $s(x)\sim t(x)$ for all $x\in X$. The coprojection $Y\to P$ sends $y\in Y$ to its equivalence class in $P$, and similarly for the coprojection $Z\to P$.

For example, let $Y$ and $Z$ be subsets of some set $A$. Then

![Union pushout](/library/volume-87/diagrams/pdf-0139-union-pushout.png)

is a pushout square in $\mathbf{Set}$. (It is also a pullback square! This coincidence is a special property of the category of sets.) You can check this by verifying the <span class="original-page-anchor" id="pdf-page-140" aria-hidden="true"></span>universal property or by using the formula just stated. In this case, the formula takes the two sets $Y$ and $Z$, places them side by side (giving $Y+Z$), then glues the subset $Y\cap Z$ of $Y$ to the subset $Y\cap Z$ of $Z$ (giving $(Y+Z)/{\sim}=Y\cup Z$).

**Example 5.2.13** If $\mathscr{A}$ is a category with an initial object $0$, and if $Y,Z\in\mathscr{A}$, then a pushout of the unique diagram

![Pushout over an initial object](/library/volume-87/diagrams/pdf-0140-initial-pushout.png)

is exactly a sum of $Y$ and $Z$.

**Example 5.2.14** The van Kampen theorem (Example 0.9) says that given a pushout square in $\mathbf{Top}$ satisfying certain further hypotheses, the square in $\mathbf{Grp}$ obtained by taking fundamental groups throughout is also a pushout.

Here is one more shape of colimit, dual to that in Example 5.1.21(d).

**Example 5.2.15** A diagram $D:(\mathbb{N},\leq)\to\mathscr{A}$ consists of objects and maps

$$
X_0\xrightarrow{s_1}X_1\xrightarrow{s_2}X_2\xrightarrow{s_3}\cdots
$$

in $\mathscr{A}$. Colimits of such diagrams are traditionally called **direct limits**. Although the old terms ‘inverse limit’ (Example 5.1.21(d)) and ‘direct limit’ are made redundant by the general categorical terms ‘limit’ and ‘colimit’ respectively, it is worth being aware of them.

With all these examples in mind, we now write down a general formula for colimits in $\mathbf{Set}$.

**Example 5.2.16** The colimit of a diagram $D:\mathbf{I}\to\mathbf{Set}$ is given by

$$
\varinjlim_{\mathbf{I}}D=\left(\sum_{I\in\mathbf{I}}D(I)\right)\Big/{\sim}
$$

where $\sim$ is the equivalence relation on $\sum D(I)$ generated by

$$
x\sim(Du)(x)
$$

for all $I\xrightarrow{u}J$ in $\mathbf{I}$ and $x\in D(I)$. To see this, note that for any set $A$, the maps

$$
\left(\sum D(I)\right)\Big/{\sim}\;\to A
$$

correspond bijectively with the maps $f:\sum D(I)\to A$ such that

$$
f(x)=f((Du)(x))
$$

<span class="original-page-anchor" id="pdf-page-141" aria-hidden="true"></span>

![Sphere as a limit and a colimit](/library/volume-87/diagrams/pdf-0141-sphere-limit-colimit.png)

Figure 5.2 Sphere as (a) a limit, and (b) a colimit.

for all $u$ and $x$ (by Remarks 5.2.8). These in turn correspond to families of maps $(D(I)\xrightarrow{f_I}A)_{I\in\mathbf{I}}$ such that $f_I(x)=f_J((Du)(x))$ for all $u$ and $x$; but these are exactly the cocones on $D$ with vertex $A$.

There is a kind of duality between the formulas for limits in $\mathbf{Set}$ (Example 5.1.22) and colimits in $\mathbf{Set}$. Whereas the limit is constructed as a *subset* of a *product*, the colimit is a *quotient* of a *sum*.

Figure 5.2 is intended to convey the difference in flavour between limits and colimits, in a particular topological context. In elementary texts, surfaces are almost always seen as subsets of Euclidean space $\mathbb{R}^3$, with the sphere $S^2$ typically defined as

$$
\{(x,y,z)\in\mathbb{R}^3\mid x^2+y^2+z^2=1\}.
$$

This is a *subspace* of the *product* space $\mathbb{R}^3=\mathbb{R}\times\mathbb{R}\times\mathbb{R}$, which suggests that it is a limit. Indeed, the sphere is the equalizer

![Sphere as an equalizer](/library/volume-87/diagrams/pdf-0141-sphere-equalizer.png)

where the maps $s,t:\mathbb{R}^3\to\mathbb{R}$ are given by

$$
s(x,y,z)=x^2+y^2+z^2,\qquad t(x,y,z)=1.
$$

(An equation is captured by an equalizer.)

In more advanced mathematics, however, this point of view is used less often. A surface can instead be thought of as the gluing-together of lots of little patches, each isomorphic to the open unit disk $D$. For example, we could in <span class="original-page-anchor" id="pdf-page-142" aria-hidden="true"></span>principle construct an entire bicycle inner tube by gluing together a large number of puncture-repair patches. Figure 5.2(b) shows the simpler example of a sphere made up of two disks glued together. This realizes the sphere as a *quotient* (gluing) of the *sum* (disjoint union) of the two copies of $D$, suggesting that we have constructed the sphere as a colimit. Indeed, the sphere is the coequalizer

![Sphere as a coequalizer](/library/volume-87/diagrams/pdf-0142-sphere-coequalizer.png)

where $S^1$ is the circle, the cylinder $S^1\times(0,1)$ is the intersection of the two copies of $D$ (the central belt of Figure 5.2(b)), and the two maps into $D+D$ are the inclusions of the cylinder into the first and second copies of $D$.

One disadvantage of the limit point of view is that it makes an arbitrary choice of coordinate system. It is generally best to think of spaces as free-standing objects, existing independently of any particular embedding into Euclidean space.

One disadvantage of the colimit point of view is that it makes an arbitrary choice of decomposition. For example, we could decompose the sphere into three patches rather than two, or use a different two patches from those shown.

The colimit point of view has the upper hand in modern geometry. (If you are familiar with the definition of manifold, you will recognize that an atlas is essentially a way of viewing a manifold as a colimit of Euclidean balls.) One reason for this is that we are often concerned with maps *out* of spaces $X$, such as maps $X\to\mathbb{R}$. Maps *out* of a colimit are easy; it is in the very definition of colimit that we know what the maps out of it are.

### Epics

**Definition 5.2.17** Let $\mathscr{A}$ be a category. A map $X\xrightarrow{f}Y$ in $\mathscr{A}$ is **epic** (or an **epimorphism**) if for all objects $Z$ and maps $Y\overset{g}{\underset{g'}{\rightrightarrows}}Z$,

$$
g\circ f=g'\circ f\implies g=g'.
$$

This is the formal dual of the definition of monic. (In other words, an epic in $\mathscr{A}$ is a monic in $\mathscr{A}^{\mathrm{op}}$.) It is in some sense the categorical version of surjectivity. But whereas the definition of monic closely resembles the definition of injective, the definition of epic does not look much like the definition of surjective. The following examples confirm that in categories where surjectivity makes sense, it is only sometimes equivalent to being epic.

**Example 5.2.18** In $\mathbf{Set}$, a map is epic if and only if it is surjective. If $f$ is <span class="original-page-anchor" id="pdf-page-143" aria-hidden="true"></span>surjective then certainly $f$ is epic. To see the converse, take $Z$ to be a two-element set $\{\texttt{true},\texttt{false}\}$, take $g$ to be the characteristic function of the image of $f$ (as defined in Section 3.1), and take $g'$ to be the function with constant value $\texttt{true}$.

Any isomorphism in any category is both monic and epic. In $\mathbf{Set}$, the converse also holds, since any injective surjective function is invertible (Example 1.1.5).

**Example 5.2.19** In categories of algebras, any surjective map is certainly epic. In some such categories, including $\mathbf{Ab}$, $\mathbf{Vect}_k$ and $\mathbf{Grp}$, the converse also holds. (The proof is straightforward for $\mathbf{Ab}$ and $\mathbf{Vect}_k$, but much harder for $\mathbf{Grp}$.) However, there are other categories of algebras where it fails. For instance, in $\mathbf{Ring}$, the inclusion $\mathbb{Z}\hookrightarrow\mathbb{Q}$ is epic but not surjective (Exercise 5.2.23). This is also an example of a map that is monic and epic but not an isomorphism.

**Example 5.2.20** In the category of Hausdorff topological spaces and continuous maps, any map with dense image is epic.

Of course, there is a dual of Lemma 5.1.32, saying that a map is epic if and only if a certain square is a pushout.

### Exercises

**5.2.21** Let $X\overset{s}{\underset{t}{\rightrightarrows}}Y$ be maps in some category. Prove that $s=t$ if and only if the equalizer of $s$ and $t$ exists and is an isomorphism, if and only if the coequalizer of $s$ and $t$ exists and is an isomorphism.

**5.2.22** (a) Let $X$ be a set and $f:X\to X$ a map. Describe the coequalizer of $X\overset{f}{\underset{1}{\rightrightarrows}}X$ in $\mathbf{Set}$ as explicitly as possible.

(b) Do the same in $\mathbf{Top}$ rather than $\mathbf{Set}$. When $X$ is the circle $S^1$, find an $f$ such that the coequalizer is an uncountable space with the indiscrete topology.

**5.2.23** (a) Prove that in the category of monoids, the inclusion $(\mathbb{N},+,0)\hookrightarrow(\mathbb{Z},+,0)$ is epic, even though it is not surjective.

(b) Prove that in the category of rings, the inclusion $\mathbb{Z}\hookrightarrow\mathbb{Q}$ is epic, even though it is not surjective.

**5.2.24** (Compare Exercise 5.1.40.) Let $\mathscr{A}$ be a category and $A\in\mathscr{A}$. Define a **quotient object** of $A$ to be an isomorphism class of epics out of $A$. That is, let $\mathbf{Epic}(A)$ be the full subcategory of $A/\mathscr{A}$ whose objects are the epics; then a quotient object of $A$ is an isomorphism class of objects of $\mathbf{Epic}(A)$.

<span class="original-page-anchor" id="pdf-page-144" aria-hidden="true"></span>

(a) Let $A\xrightarrow{e}X$ and $A\xrightarrow{e'}X'$ be epics in $\mathbf{Set}$. Show that $e$ and $e'$ are isomorphic in $\mathbf{Epic}(A)$ if and only if they induce the same equivalence relation on $A$. Deduce that the quotient objects of $A$ are in canonical one-to-one correspondence with the equivalence relations on $A$.

(b) Assuming the (nontrivial) fact that the epics in $\mathbf{Grp}$ are the surjections, show that the quotient objects of a group correspond one-to-one with its normal subgroups.

(The name ‘quotient object’ is not standard, and indeed there is no standard name for it. Arguably, ‘quotient object’ would be more suitable for an isomorphism class of *regular* epics, as defined in the following exercises.)

**5.2.25** A map $m:A\to B$ is **regular monic** if there exist an object $C$ and maps $B\rightrightarrows C$ of which $m$ is an equalizer. A map $m:A\to B$ is **split monic** if there exists a map $e:B\to A$ such that $em=1_A$.

(a) Show that split monic $\implies$ regular monic $\implies$ monic.

(b) In $\mathbf{Ab}$, show that all monics are regular but not all monics are split. (Hint for the first part: equalizers in $\mathbf{Ab}$ are calculated as in Example 5.1.15.)

(c) In $\mathbf{Top}$, describe the regular monics, and find a monic that is not regular.

**5.2.26** Dualizing the definitions in Exercise 5.2.25 gives definitions of **regular** and **split epic**.

(a) We saw in Example 5.2.19 that a map may be monic and epic but not an isomorphism. Prove that in any category, a map is an isomorphism if and only if it is both monic and *regular* epic.

(b) Using the assumption that our category of sets satisfies the axiom of choice (Section 3.1), show that

$$
\text{epic}\iff\text{regular epic}\iff\text{split epic}
$$

in $\mathbf{Set}$.

(c) Let us say that a category $\mathscr{A}$ satisfies the **axiom of choice** if all epics in $\mathscr{A}$ are split. Prove that neither $\mathbf{Top}$ nor $\mathbf{Grp}$ satisfies the axiom of choice.

**5.2.27** The result of Exercise 5.1.42 can be phrased as ‘the class of monics is stable under pullback’. It is also a fact that the composite of two monics is always monic; we say that the class of monics is ‘closed under composition’.

Consider the following six classes of map:

monics, regular monics, split monics, epics, regular epics, split epics.

Determine whether each class is stable under pullback or closed under composition.

<span class="original-page-anchor" id="pdf-page-145" aria-hidden="true"></span>

## 5.3 Interactions between functors and limits

We saw in Example 5.1.23 that limits in categories such as $\mathbf{Grp}$, $\mathbf{Ring}$ and $\mathbf{Vect}_k$ can be computed by first taking the limit in the category of sets, then equipping the result with a suitable algebraic structure. On the other hand, colimits in these categories are unlike colimits in $\mathbf{Set}$. For example, the underlying set of the initial object of $\mathbf{Grp}$ (which has one element) is not the initial object of $\mathbf{Set}$ (which has no elements), and the underlying set of the direct sum $X\oplus Y$ of two vector spaces is not the sum of the underlying sets of $X$ and $Y$. So, these forgetful functors interact well with limits and badly with colimits.

In this section, we develop terminology that will enable us to express these thoughts precisely.

**Definition 5.3.1** (a) Let $\mathbf{I}$ be a small category. A functor $F:\mathscr{A}\to\mathscr{B}$ **preserves limits of shape $\mathbf{I}$** if for all diagrams $D:\mathbf{I}\to\mathscr{A}$ and all cones $(A\xrightarrow{p_I}D(I))_{I\in\mathbf{I}}$ on $D$,

$$
\begin{aligned}
&\left(A\xrightarrow{p_I}D(I)\right)_{I\in\mathbf{I}}\text{ is a limit cone on }D\text{ in }\mathscr{A}\\
\implies\quad&\left(F(A)\xrightarrow{Fp_I}FD(I)\right)_{I\in\mathbf{I}}\text{ is a limit cone on }F\circ D\text{ in }\mathscr{B}.
\end{aligned}
$$

(b) A functor $F:\mathscr{A}\to\mathscr{B}$ **preserves limits** if it preserves limits of shape $\mathbf{I}$ for all small categories $\mathbf{I}$.

(c) **Reflection** of limits is defined as in (a), but with $\Longleftarrow$ in place of $\Longrightarrow$.

Of course, the same terminology applies to colimits.

Here is a different way to state the definition of preservation. A functor $F:\mathscr{A}\to\mathscr{B}$ preserves limits if and only if it has the following property: whenever $D:\mathbf{I}\to\mathscr{A}$ is a diagram that has a limit, the composite $F\circ D:\mathbf{I}\to\mathscr{B}$ also has a limit, and the canonical map

$$
F\left(\varprojlim_{\mathbf{I}}D\right)\to\varprojlim_{\mathbf{I}}(F\circ D)
$$

is an isomorphism. Here the ‘canonical map’ has $I$-component

$$
F\left(\varprojlim_{\mathbf{I}}D\right)\xrightarrow{F(p_I)}F(D(I)),
$$

where $p_I$ is the $I$th projection of the limit cone on $D$.

In particular, if $F$ preserves limits then

$$
F\left(\varprojlim_{\mathbf{I}}D\right)\cong\varprojlim_{\mathbf{I}}(F\circ D)\tag{5.22}
$$

whenever $D$ is a diagram with a limit. Preservation of limits says more than <span class="original-page-anchor" id="pdf-page-146" aria-hidden="true"></span>(5.22) does: the left- and right-hand sides are required to be not just isomorphic, but isomorphic *in a particular way*. Nevertheless, we will sometimes omit this check, acting as if preservation means only that (5.22) holds.

**Example 5.3.2** The forgetful functor $U\colon \mathbf{Top}\to\mathbf{Set}$ preserves both limits and colimits. (As we will see, this follows from the fact that $U$ has adjoints on both sides.) It does not reflect all limits or all colimits. For instance, choose any non-discrete spaces $X$ and $Y$, and let $Z$ be the set $U(X)\times U(Y)$ equipped with the discrete topology. (All that matters here is that the topology on $Z$ is strictly larger than the product topology.) Then we have a cone

$$
X\leftarrow Z\to Y\tag{5.23}
$$

in $\mathbf{Top}$ whose image in $\mathbf{Set}$ is the product cone

$$
U(X)\leftarrow U(X)\times U(Y)\to U(Y).
$$

But (5.23) is not a product cone in $\mathbf{Top}$, since the discrete topology on $U(X)\times U(Y)$ is not the product topology.

**Example 5.3.3** In the first paragraph of this section, we observed that the forgetful functor $\mathbf{Grp}\to\mathbf{Set}$ does not preserve initial objects and that the forgetful functor $\mathbf{Vect}_k\to\mathbf{Set}$ does not preserve binary sums. Forgetful functors out of categories of algebras very seldom preserve all colimits.

**Example 5.3.4** We also saw that (in the examples mentioned) forgetful functors on categories of algebras do preserve limits. In fact, something stronger is true. Let us examine the case of binary products in $\mathbf{Grp}$, although all of the following can be said for any limits in any of the categories $\mathbf{Grp}$, $\mathbf{Ab}$, $\mathbf{Vect}_k$, $\mathbf{Ring}$, etc.

Take groups $X_1$ and $X_2$. We can form the product set $U(X_1)\times U(X_2)$, which comes equipped with projections

$$
U(X_1)\xleftarrow{p_1}U(X_1)\times U(X_2)\xrightarrow{p_2}U(X_2).
$$

I claim that there is exactly one group structure on the set $U(X_1)\times U(X_2)$ with the property that $p_1$ and $p_2$ are homomorphisms. To prove uniqueness, suppose that we have a group structure on $U(X_1)\times U(X_2)$ with this property. Take elements $(x_1,x_2)$ and $(x'_1,x'_2)$ of $U(X_1)\times U(X_2)$ and write $(x_1,x_2)\cdot(x'_1,x'_2)=(y_1,y_2)$. Since $p_1$ is a homomorphism,

$$
y_1=p_1(y_1,y_2)=p_1((x_1,x_2)\cdot(x'_1,x'_2))=p_1(x_1,x_2)\cdot p_1(x'_1,x'_2)=x_1\cdot x'_1,
$$

and similarly $y_2=x_2\cdot x'_2$. Hence

$$
(x_1,x_2)\cdot(x'_1,x'_2)=(x_1x'_1,x_2x'_2).
$$

<span class="original-page-anchor" id="pdf-page-147" aria-hidden="true"></span>

![Creation of limits](/library/volume-87/diagrams/pdf-0147-creation.png)

Figure 5.3 Creation of limits.

A similar argument shows that $(x_1,x_2)^{-1}=(x_1^{-1},x_2^{-1})$ and that the identity element $1$ of the group is $(1,1)$. Now, for existence, define $\cdot$, $(\ )^{-1}$ and $1$ by the formulas just given; it can then be checked that the group axioms are satisfied and that $p_1$ and $p_2$ are group homomorphisms. This proves the claim.

Write $L$ for the set $U(X_1)\times U(X_2)$ equipped with this group structure. Then we have a cone

$$
X_1\xleftarrow{p_1}L\xrightarrow{p_2}X_2
$$

in $\mathbf{Grp}$. It is easy to check that this is, in fact, a *product* cone in $\mathbf{Grp}$.

We can summarize this in language that is not tied to group theory. Given objects $X_1$ and $X_2$ of $\mathbf{Grp}$,

- for any product cone on $(U(X_1),U(X_2))$ in $\mathbf{Set}$, there is a unique cone on $(X_1,X_2)$ in $\mathbf{Grp}$ whose image under $U$ is the cone we started with;
- this cone on $(X_1,X_2)$ is a product cone.

This suggests the following definition (Figure 5.3).

**Definition 5.3.5** A functor $F\colon\mathscr{A}\to\mathscr{B}$ **creates limits (of shape $\mathbf{I}$)** if whenever $D\colon\mathbf{I}\to\mathscr{A}$ is a diagram in $\mathscr{A}$,

- for any limit cone $\bigl(B\xrightarrow{q_I}FD(I)\bigr)_{I\in\mathbf{I}}$ on the diagram $F\circ D$, there is a unique cone $\bigl(A\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ on $D$ such that $F(A)=B$ and $F(p_I)=q_I$ for all $I\in\mathbf{I}$;
- this cone $\bigl(A\xrightarrow{p_I}D(I)\bigr)_{I\in\mathbf{I}}$ is a limit cone on $D$.

The forgetful functors from $\mathbf{Grp}$, $\mathbf{Ring}$, $\ldots$ to $\mathbf{Set}$ all create limits (Exercise 5.3.11). The word *creates* is explained by the following result.

<span class="original-page-anchor" id="pdf-page-148" aria-hidden="true"></span>

**Lemma 5.3.6** Let $F\colon\mathscr{A}\to\mathscr{B}$ be a functor and $\mathbf{I}$ a small category. Suppose that $\mathscr{B}$ has, and $F$ creates, limits of shape $\mathbf{I}$. Then $\mathscr{A}$ has, and $F$ preserves, limits of shape $\mathbf{I}$.

**Proof** Exercise 5.3.12. $\square$

Since $\mathbf{Set}$ has all limits, it follows that all our categories of algebras have all limits, and that the forgetful functors preserve them.

**Remark 5.3.7** There is something suspicious about Definition 5.3.5. It refers to *equality* of objects of a category, a relation that, as we saw on page 31, is usually too strict to be appropriate. It is almost always better to replace equality by isomorphism. If we replace equality by isomorphism throughout the definition of ‘creates limits’, we obtain a more healthy and inclusive notion. In the notation of Definition 5.3.5, we ask that if $F\circ D$ has a limit then there exists a cone on $D$ whose image under $F$ is a limit cone, and that every such cone is itself a limit cone.

In fact, what we are calling creation of limits should really be called *strict* creation of limits, with ‘creation of limits’ reserved for the more inclusive notion. That is how ‘creates’ is used in most of the literature. I have chosen to use the strict version here because it is slightly simpler to state, and because the examples at hand all satisfy the stricter condition.

### Exercises

**5.3.8** Taking the limit is a process that receives as its input a diagram in a category $\mathscr{A}$, and produces as its output a new object of $\mathscr{A}$. Later, we will see that this process is functorial (Proposition 6.1.4). Here you are asked to prove this in the case of binary products.

Let $\mathscr{A}$ be a category with binary products. Suppose that we have chosen for each pair $(X,Y)$ of objects a product cone

$$
X\xleftarrow{p_1^{X,Y}}X\times Y\xrightarrow{p_2^{X,Y}}Y.
$$

Construct a functor $\mathscr{A}\times\mathscr{A}\to\mathscr{A}$ given on objects by $(X,Y)\mapsto X\times Y$.

**5.3.9** Let $\mathscr{A}$ be a category with binary products. Prove directly that

$$
\mathscr{A}(A,X\times Y)\cong\mathscr{A}(A,X)\times\mathscr{A}(A,Y)
$$

naturally in $A,X,Y\in\mathscr{A}$. (This presupposes that we have chosen for each $X$ and $Y$ a product cone on $(X,Y)$. By Exercise 5.3.8, the assignment $(X,Y)\mapsto X\times Y$ is then functorial, which it must be in order for ‘naturally’ to make sense.)

<span class="original-page-anchor" id="pdf-page-149" aria-hidden="true"></span>

**5.3.10** Prove that if a functor creates limits then it also reflects them.

**5.3.11** It was shown in Example 5.3.4 that the forgetful functor $U\colon\mathbf{Grp}\to\mathbf{Set}$ creates binary products.

(a) Using the formula for limits in $\mathbf{Set}$ (Example 5.1.22), prove that, in fact, $U$ creates arbitrary limits.

(b) Satisfy yourself that the same is true if $\mathbf{Grp}$ is replaced by any other category of algebras such as $\mathbf{Ring}$, $\mathbf{Ab}$ or $\mathbf{Vect}_k$.

**5.3.12** Prove Lemma 5.3.6.

**5.3.13** (a) An object $P$ of a category $\mathscr{B}$ is **projective** if $\mathscr{B}(P,-)\colon\mathscr{B}\to\mathbf{Set}$ preserves epics. (This means that if $f$ is epic then so is $\mathscr{B}(P,f)$.) Let

![Adjunction](/library/volume-87/diagrams/pdf-0149-adjunction.png)

be an adjunction in which $G$ preserves epics. Prove that $F(S)$ is projective for all sets $S$.

(b) Find a non-projective object of $\mathbf{Ab}$.

(c) An object $I$ of a category $\mathscr{B}$ is **injective** if it is projective in $\mathscr{B}^{\mathrm{op}}$, or equivalently if $\mathscr{B}(-,I)\colon\mathscr{B}^{\mathrm{op}}\to\mathbf{Set}$ preserves epics. Show that all objects of $\mathbf{Vect}_k$ are injective, and find a non-injective object of $\mathbf{Ab}$.
