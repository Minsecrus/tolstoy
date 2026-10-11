---
title: "Introduction"
description: "Tom Leinster《Basic Category Theory》English。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"Note to the reader","link":"/library/volume-87/original-note-to-reader"}
next: {"text":"Categories, functors and natural transformations","link":"/library/volume-87/original-chapter-001"}
---

# Introduction

<span class="original-page-anchor" id="pdf-page-10" aria-hidden="true"></span>

Category theory takes a bird’s eye view of mathematics. From high in the sky, details become invisible, but we can spot patterns that were impossible to detect from ground level. How is the lowest common multiple of two numbers like the direct sum of two vector spaces? What do discrete topological spaces, free groups, and fields of fractions have in common? We will discover answers to these and many similar questions, seeing patterns in mathematics that you may never have seen before.

The most important concept in this book is that of *universal property*. The further you go in mathematics, especially pure mathematics, the more universal properties you will meet. We will spend most of our time studying different manifestations of this concept.

Like all branches of mathematics, category theory has its own special vocabulary, which we will meet as we go along. But since the idea of universal property is so important, I will use this introduction to explain it with no jargon at all, by means of examples.

Our first example of a universal property is very simple.

**Example 0.1** Let $1$ denote a set with one element. (It does not matter what this element is called.) Then $1$ has the following property:

> for all sets $X$, there exists a unique map from $X$ to $1$.

(In this context, the words ‘map’, ‘mapping’ and ‘function’ all mean the same thing.)

Indeed, let $X$ be a set. There *exists* a map $X \to 1$, because we can define $f: X \to 1$ by taking $f(x)$ to be the single element of $1$ for each $x \in X$. This is the *unique* map $X \to 1$, because there is no choice in the matter: any map $X \to 1$ must send each element of $X$ to the single element of $1$.

Phrases of the form ‘there exists a unique such-and-such satisfying some <span class="original-page-anchor" id="pdf-page-11" aria-hidden="true"></span>condition’ are common in category theory. The phrase means that there is one and only one such-and-such satisfying the condition. To prove the existence part, we have to show that there is at least one. To prove the uniqueness part, we have to show that there is at most one; in other words, any two such-and-suches satisfying the condition are equal.

Properties such as this are called ‘universal’ because they state how the object being described (in this case, the set $1$) relates to the entire universe in which it lives (in this case, the universe of sets). The property begins with the words ‘*for all* sets $X$’, and therefore says something about the relationship between $1$ and *every* set $X$: namely, that there is a unique map from $X$ to $1$.

**Example 0.2** This example involves rings, which in this book are always taken to have a multiplicative identity, called $1$. Similarly, homomorphisms of rings are understood to preserve multiplicative identities.

The ring $\mathbb{Z}$ has the following property: for all rings $R$, there exists a unique homomorphism $\mathbb{Z} \to R$.

To prove existence, let $R$ be a ring. Define a function $\phi: \mathbb{Z} \to R$ by

$$
\phi(n) = \begin{cases}
\underbrace{1 + \cdots + 1}_{n} & \text{if } n > 0, \\
0 & \text{if } n = 0, \\
-\phi(-n) & \text{if } n < 0
\end{cases}
$$

($n \in \mathbb{Z}$). A series of elementary checks confirms that $\phi$ is a homomorphism.

To prove uniqueness, let $R$ be a ring and let $\psi: \mathbb{Z} \to R$ be a homomorphism. We show that $\psi$ is equal to the homomorphism $\phi$ just defined. Since homomorphisms preserve multiplicative identities, $\psi(1) = 1$. Since homomorphisms preserve addition,

$$
\psi(n) = \psi\left(\underbrace{1 + \cdots + 1}_{n}\right) = \underbrace{\psi(1) + \cdots + \psi(1)}_{n} = \underbrace{1 + \cdots + 1}_{n} = \phi(n)
$$

for all $n > 0$. Since homomorphisms preserve zero, $\psi(0) = 0 = \phi(0)$. Finally, since homomorphisms preserve negatives, $\psi(n) = -\psi(-n) = -\phi(-n) = \phi(n)$ whenever $n < 0$.

Crucially, there can be essentially only *one* object satisfying a given universal property. The word ‘essentially’ means that two objects satisfying the same universal property need not literally be equal, but they are always isomorphic. For example:

**Lemma 0.3** *Let $A$ be a ring with the following property: for all rings $R$, there exists a unique homomorphism $A \to R$. Then $A \cong \mathbb{Z}$.*

<span class="original-page-anchor" id="pdf-page-12" aria-hidden="true"></span>

**Proof** Let us call a ring with this property ‘initial’. We are given that $A$ is initial, and we proved in Example 0.2 that $\mathbb{Z}$ is initial.

Since $A$ is initial, there is a unique homomorphism $\phi: A \to \mathbb{Z}$. Since $\mathbb{Z}$ is initial, there is a unique homomorphism $\phi': \mathbb{Z} \to A$. Now $\phi' \circ \phi: A \to A$ is a homomorphism, but so too is the identity map $1_A: A \to A$; hence, since $A$ is initial, $\phi' \circ \phi = 1_A$. (This follows from the uniqueness part of initiality, taking ‘$R$’ to be $A$.) Similarly, $\phi \circ \phi' = 1_{\mathbb{Z}}$. So $\phi$ and $\phi'$ are mutually inverse, and therefore define an isomorphism between $A$ and $\mathbb{Z}$. $\square$

This proof has very little to do with rings. It really belongs at a higher level of generality. To properly understand this, and to convey more fully the idea of universal property, it will help to consider some more complex examples.

**Example 0.4** Let $V$ be a vector space with a basis $(v_s)_{s \in S}$. (For example, if $V$ is finite-dimensional then we might take $S = \{1, \ldots, n\}$.) If $W$ is another vector space, we can specify a linear map from $V$ to $W$ simply by saying where the basis elements go. Thus, for any $W$, there is a natural one-to-one correspondence between

> linear maps $V \to W$

and

> functions $S \to W$.

This is because any function defined on the basis elements extends uniquely to a linear map on $V$.

Let us rephrase this last statement. Define a function $i: S \to V$ by $i(s) = v_s$ ($s \in S$). Then $V$ together with $i$ has the following universal property:

![The universal property of a vector space with a specified basis.](/library/volume-87/diagrams/pdf-0012-basis-universal.png)

This diagram means that for all vector spaces $W$ and all functions $f: S \to W$, there exists a unique linear map $\bar{f}: V \to W$ such that $\bar{f} \circ i = f$. The symbol $\forall$ means ‘for all’, and the symbols $\exists!$ mean ‘there exists a unique’.

Another way to say ‘$\bar{f} \circ i = f$’ is ‘$\bar{f}(v_s) = f(s)$ for all $s \in S$’. So, the diagram asserts that every function $f$ defined on the basis elements extends uniquely to a linear map $\bar{f}$ defined on the whole of $V$. In other words still, the function

$$
\begin{array}{ccc}
\{\text{linear maps } V \to W\} & \to & \{\text{functions } S \to W\} \\
\bar{f} & \mapsto & \bar{f} \circ i
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-13" aria-hidden="true"></span>

is bijective.

**Example 0.5** Given a set $S$, we can build a topological space $D(S)$ by equipping $S$ with the **discrete topology**: all subsets are open. With this topology, *any* map from $S$ to a space $X$ is continuous.

Again, let us rephrase this. Define a function $i: S \to D(S)$ by $i(s) = s$ ($s \in S$). Then $D(S)$ together with $i$ has the following universal property:

![The universal property of a discrete topological space.](/library/volume-87/diagrams/pdf-0013-discrete-universal.png)

In other words, for all topological spaces $X$ and all functions $f: S \to X$, there exists a unique continuous map $\bar{f}: D(S) \to X$ such that $\bar{f} \circ i = f$. The continuous map $\bar{f}$ is the same thing as the function $f$, except that we are regarding it as a continuous map between topological spaces rather than a mere function between sets.

You may feel that this universal property is almost too trivial to mean anything. But if we change the definition of $D(S)$ – say from the discrete to the indiscrete topology, in which the only open sets are $\emptyset$ and $S$ – then the property becomes false. So this property really does say something about the discrete topology. What it says is that all maps out of a discrete space are continuous.

Indeed, given $S$, the universal property determines $D(S)$ and $i$ uniquely (or rather, uniquely up to isomorphism; but who could want more?). The proof of this is similar to that of Lemma 0.3 above and Lemma 0.7 below.

**Example 0.6** Given vector spaces $U$, $V$ and $W$, a **bilinear map** $f: U \times V \to W$ is a function $f$ that is linear in each variable:

$$
\begin{aligned}
f(u, v_1 + \lambda v_2) &= f(u, v_1) + \lambda f(u, v_2), \\
f(u_1 + \lambda u_2, v) &= f(u_1, v) + \lambda f(u_2, v)
\end{aligned}
$$

for all $u, u_1, u_2 \in U$, $v, v_1, v_2 \in V$, and scalars $\lambda$. A good example is the scalar product (dot product), which is a bilinear map

$$
\begin{array}{ccc}
\mathbb{R}^{n} \times \mathbb{R}^{n} & \to & \mathbb{R} \\
(\mathbf{u}, \mathbf{v}) & \mapsto & \mathbf{u}.\mathbf{v}
\end{array}
$$

of real vector spaces. The vector product (cross product) $\mathbb{R}^{3} \times \mathbb{R}^{3} \to \mathbb{R}^{3}$ is also bilinear.

Let $U$ and $V$ be vector spaces. It is a fact that there is a ‘universal bilinear <span class="original-page-anchor" id="pdf-page-14" aria-hidden="true"></span>map out of $U \times V$’. In other words, there exist a certain vector space $T$ and a certain bilinear map $b: U \times V \to T$ with the following universal property:

![Universal bilinear map, equation (0.1)](/library/volume-87/diagrams/pdf-0014-tensor-universal.png)

Roughly speaking, this property says that bilinear maps out of $U \times V$ correspond one-to-one with linear maps out of $T$.

Even without knowing that such a $T$ and $b$ exist, we can immediately prove that this universal property determines $T$ and $b$ uniquely up to isomorphism. The proof is essentially the same as that of Lemma 0.3, but looks more complicated because of the more complicated universal property.

**Lemma 0.7** *Let $U$ and $V$ be vector spaces. Suppose that $b: U \times V \to T$ and $b': U \times V \to T'$ are both universal bilinear maps out of $U \times V$. Then $T \cong T'$. More precisely, there exists a unique isomorphism $j: T \to T'$ such that $j \circ b = b'$.*

In the proof that follows, it does not actually matter what ‘bilinear’, ‘linear’ or even ‘vector space’ mean. The hard part is getting the logic straight. That done, you should be able to see that there is really only one possible proof. For instance, to use the universality of $b$, we will have to choose some bilinear map $f$ out of $U \times V$. There are only two in sight, $b$ and $b'$, and we use each in the appropriate place.

**Proof** In diagram (0.1), take $\bigl(U \times V \xrightarrow{f} W\bigr)$ to be $\bigl(U \times V \xrightarrow{b'} T'\bigr)$. This gives a linear map $j: T \to T'$ satisfying $j \circ b = b'$. Similarly, using the universality of $b'$, we obtain a linear map $j': T' \to T$ satisfying $j' \circ b' = b$:

![The maps defining the tensor-product isomorphism](/library/volume-87/diagrams/pdf-0014-tensor-isomorphism.png)

Now $j' \circ j: T \to T$ is a linear map satisfying $(j' \circ j) \circ b = b$; but also, the identity map $1_T: T \to T$ is linear and satisfies $1_T \circ b = b$. So by the uniqueness part of the universal property of $b$, we have $j' \circ j = 1_T$. (Here we took the ‘$f$’ of (0.1) to be $b$.) Similarly, $j \circ j' = 1_{T'}$. So $j$ is an isomorphism. $\square$ <span class="original-page-anchor" id="pdf-page-15" aria-hidden="true"></span>In Example 0.6, it was stated that given vector spaces $U$ and $V$, there exists a pair $(T, b)$ with the universal property of (0.1). We just proved that there is essentially only one such pair $(T, b)$. The vector space $T$ is called the **tensor product** of $U$ and $V$, and is written as $U \otimes V$. Tensor products are very important in algebra. They reduce the study of bilinear maps to the study of linear maps, since a bilinear map out of $U \times V$ is really the same thing as a linear map out of $U \otimes V$.

However, tensor products will not be important in this book. The real lesson for us is that it is safe to speak of *the* tensor product, not just *a* tensor product, and the reason for that is Lemma 0.7. This is a general point that applies to anything satisfying a universal property.

Once you know a universal property of an object, it often does no harm to forget how it was constructed. For instance, if you look through a pile of algebra books, you will find several different ways of constructing the tensor product of two vector spaces. But once you have proved that the tensor product satisfies the universal property, you can forget the construction. The universal property tells you all you need to know, because it determines the object uniquely up to isomorphism.

**Example 0.8** Let $\theta: G \to H$ be a homomorphism of groups. Associated with $\theta$ is a diagram

![The kernel and the parallel group homomorphisms, equation (0.2)](/library/volume-87/diagrams/pdf-0015-kernel.png)

where $\iota$ is the inclusion of $\ker(\theta)$ into $G$ and $\varepsilon$ is the trivial homomorphism. ‘Inclusion’ means that $\iota(x) = x$ for all $x \in \ker(\theta)$, and ‘trivial’ means that $\varepsilon(g) = 1$ for all $g \in G$. The symbol $\hookrightarrow$ is often used for inclusions; it is a combination of a subset symbol $\subset$ and an arrow.

The map $\iota$ into $G$ satisfies $\theta \circ \iota = \varepsilon \circ \iota$, and is universal as such. Exercise 0.11 asks you to make this precise.

Here is our final example of a universal property.

**Example 0.9** Take a topological space covered by two open subsets: $X = U \cup V$. The diagram

![The inclusion maps for an open cover](/library/volume-87/diagrams/pdf-0015-open-cover.png)

of inclusion maps has a universal property in the world of topological spaces <span class="original-page-anchor" id="pdf-page-16" aria-hidden="true"></span>and continuous maps, as follows:

![The universal property of an open cover, equation (0.3)](/library/volume-87/diagrams/pdf-0016-open-cover-universal.png)

The diagram means that given $Y$, $f$ and $g$ such that $f \circ i = g \circ j$, there is exactly one continuous map $h: X \to Y$ such that $h \circ j' = f$ and $h \circ i' = g$.

Under favourable conditions, the induced diagram

![The induced diagram of fundamental groups](/library/volume-87/diagrams/pdf-0016-fundamental-groups.png)

of fundamental groups has the same property in the world of groups and group homomorphisms. This is *van Kampen’s theorem*. In fact, van Kampen stated his theorem in a much more complicated way. Stating it transparently requires some categorical language, but he was working in the 1930s, before category theory had been born.

You have now seen several examples of universal properties. As this book progresses, we will develop different ways of talking about them. Once we have set up the basic vocabulary of categories and functors, we will study *adjoint functors*, then *representable functors*, then *limits*. Each of these provides an approach to universal properties, and each places the idea in a different light. For instance, Examples 0.4 and 0.5 can most readily be described in terms of adjoint functors, Example 0.6 via representable functors, and Examples 0.1, 0.2, 0.8 and 0.9 in terms of limits.

### Exercises

**0.10** Let $S$ be a set. The **indiscrete** topological space $I(S)$ is the space whose set of points is $S$ and whose only open subsets are $\emptyset$ and $S$ itself. Imitating Example 0.5, find a universal property satisfied by the space $I(S)$.

<span class="original-page-anchor" id="pdf-page-17" aria-hidden="true"></span>

**0.11** Fix a group homomorphism $\theta: G \to H$. Find a universal property satisfied by the pair $(\ker(\theta), \iota)$ of diagram (0.2). (This property can – indeed, must – make reference to $\theta$.)

**0.12** Verify the universal property shown in diagram (0.3).

**0.13** Denote by $\mathbb{Z}[x]$ the polynomial ring over $\mathbb{Z}$ in one variable.

(a) Prove that for all rings $R$ and all $r \in R$, there exists a unique ring homomorphism $\phi: \mathbb{Z}[x] \to R$ such that $\phi(x) = r$.

(b) Let $A$ be a ring and $a \in A$. Suppose that for all rings $R$ and all $r \in R$, there exists a unique ring homomorphism $\phi: A \to R$ such that $\phi(a) = r$. Prove that there is a unique isomorphism $\iota: \mathbb{Z}[x] \to A$ such that $\iota(x) = a$.

**0.14** Let $X$ and $Y$ be vector spaces.

(a) For the purposes of this exercise only, a *cone* is a triple $(V, f_1, f_2)$ consisting of a vector space $V$, a linear map $f_1: V \to X$, and a linear map $f_2: V \to Y$. Find a cone $(P, p_1, p_2)$ with the following property: for all cones $(V, f_1, f_2)$, there exists a unique linear map $f: V \to P$ such that $p_1 \circ f = f_1$ and $p_2 \circ f = f_2$.

(b) Prove that there is essentially only one cone with the property stated in (a). That is, prove that if $(P, p_1, p_2)$ and $(P', p'_1, p'_2)$ both have this property then there is an isomorphism $i: P \to P'$ such that $p'_1 \circ i = p_1$ and $p'_2 \circ i = p_2$.

(c) For the purposes of this exercise only, a *cocone* is a triple $(V, f_1, f_2)$ consisting of a vector space $V$, a linear map $f_1: X \to V$, and a linear map $f_2: Y \to V$. Find a cocone $(Q, q_1, q_2)$ with the following property: for all cocones $(V, f_1, f_2)$, there exists a unique linear map $f: Q \to V$ such that $f \circ q_1 = f_1$ and $f \circ q_2 = f_2$.

(d) Prove that there is essentially only one cocone with the property stated in (c), in a sense that you should make precise.
