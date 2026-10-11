---
title: "Proof of the general adjoint functor theorem"
description: "Tom Leinster《Basic Category Theory》English。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"Adjoints, representables and limits","link":"/library/volume-87/original-chapter-006"}
next: {"text":"Further reading","link":"/library/volume-87/original-further-reading"}
---

# Proof of the general adjoint functor theorem

<span class="original-page-anchor" id="pdf-page-180" aria-hidden="true"></span>

Here we prove the general adjoint functor theorem, which for convenience is restated below. The left-to-right implication follows immediately from Theorem 6.3.1; it is the right-to-left implication that we have to prove.

**Theorem 6.3.10 (General adjoint functor theorem)** Let $\mathscr{A}$ be a category, $\mathscr{B}$ a complete category, and $G:\mathscr{B}\to\mathscr{A}$ a functor. Suppose that $\mathscr{B}$ is locally small and that for each $A\in\mathscr{A}$, the category $(A\Rightarrow G)$ has a weakly initial set. Then

$$
G\text{ has a left adjoint}\iff G\text{ preserves limits}.
$$

The heart of the proof is the case $\mathscr{A}=\mathbf{1}$, where GAFT asserts that a complete locally small category with a weakly initial set has an initial object. We prove this first.

The proof of this special case is illuminated by considering the even more special case where $\mathscr{A}=\mathbf{1}$ and the category $\mathscr{B}$ is a poset $\mathbf{B}$. We saw in Example 6.3.8 that the initial object (least element) of a complete poset $\mathbf{B}$ can be constructed as the meet of all its elements. Otherwise put, it is the limit of the identity functor $1_{\mathbf{B}}:\mathbf{B}\to\mathbf{B}$.

One might try to extend this result to arbitrary categories $\mathscr{B}$ by proving that the limit of the identity functor $1_{\mathscr{B}}:\mathscr{B}\to\mathscr{B}$ is (if it exists) an initial object. This is indeed true (Exercise A.3 below). However, it is unhelpful: for if $\mathscr{B}$ is large then the limit of $1_{\mathscr{B}}$ is a large limit, but we are only given that $\mathscr{B}$ has small limits.

We seem to be at an impasse — but this is where the clever idea behind GAFT comes in. In order to construct the least element of a complete poset, it is not necessary to take the meet of *all* the elements. More economically, we could just take the meet of the elements of some weakly initial subset (Exercise A.4).

<span class="original-page-anchor" id="pdf-page-181" aria-hidden="true"></span>

In general, for an arbitrary complete category, the limit of any weakly initial set is an initial object. We prove this now.

**Lemma A.1** Let $\mathscr{C}$ be a complete locally small category with a weakly initial set. Then $\mathscr{C}$ has an initial object.

**Proof** Let $\mathbf{S}$ be a weakly initial set in $\mathscr{C}$. Regard $\mathbf{S}$ as a full subcategory of $\mathscr{C}$; then $\mathbf{S}$ is small, since $\mathscr{C}$ is locally small. We may therefore take a limit cone

$$
\left(0\xrightarrow{p_S}S\right)_{S\in\mathbf{S}}\tag{A.1}
$$

of the inclusion $\mathbf{S}\hookrightarrow\mathscr{C}$. We prove that $0$ is initial.

Let $C\in\mathscr{C}$. We have to show that there is exactly one map $0\to C$. Certainly there is at least one, since we may choose some $S\in\mathbf{S}$ and map $j:S\to C$, and we then have the composite $jp_S:0\to C$. To prove uniqueness, let $f,g:0\to C$. Form the equalizer

![Equalizer of f and g](/library/volume-87/diagrams/pdf-0181-equalizer.png)

Since $\mathbf{S}$ is weakly initial, we may choose $S\in\mathbf{S}$ and $h:S\to E$. We then have maps

$$
0\xrightarrow{p_S}S\xrightarrow{h}E\xrightarrow{i}0
$$

with the property that for all $S'\in\mathbf{S}$,

$$
p_{S'}(ihp_S)=(p_{S'}ih)p_S=p_{S'}=p_{S'}1_0
$$

(where the second equality follows from (A.1) being a cone). But (A.1) is a *limit* cone, so $ihp_S=1_0$ by Exercise 5.1.36(a). Hence

$$
f=fihp_S=gihp_S=g,
$$

as required. $\square$

We have now proved GAFT in the special case $\mathscr{A}=\mathbf{1}$. The rest of the proof is comparatively routine.

**Lemma A.2** Let $\mathscr{A}$ and $\mathscr{B}$ be categories. Let $G:\mathscr{B}\to\mathscr{A}$ be a functor that preserves limits. Then the projection functor $P_A:(A\Rightarrow G)\to\mathscr{B}$ of (6.21) creates limits, for each $A\in\mathscr{A}$. In particular, if $\mathscr{B}$ is complete then so is each comma category $(A\Rightarrow G)$.

**Proof** The first statement is Exercise A.5(b), and the second follows from Lemma 5.3.6. $\square$ <span class="original-page-anchor" id="pdf-page-182" aria-hidden="true"></span>We now prove GAFT. By Corollary 2.3.7, it is enough to show that $(A\Rightarrow G)$ has an initial object for each $A\in\mathscr{A}$. Let $A\in\mathscr{A}$. By Lemma A.2, $(A\Rightarrow G)$ is complete, and by hypothesis, it has a weakly initial set. It is also locally small, since $\mathscr{B}$ is. Hence by Lemma A.1, it has an initial object, as required.

### Exercises

**A.3** In this exercise, we suspend the convention (made implicitly in Definition 5.1.19) that we only speak of the limit of a functor $\mathbf{I}\to\mathscr{C}$ when $\mathbf{I}$ is small. Let $\mathscr{B}$ be a category, possibly large. The aim is to prove that a limit of the identity functor on $\mathscr{B}$ is exactly an initial object of $\mathscr{B}$.

(a) Let $0$ be an initial object of $\mathscr{B}$. Show that the cone $(0\to B)_{B\in\mathscr{B}}$ on the identity functor $1_{\mathscr{B}}$ is a limit cone.

(b) Now let $\left(L\xrightarrow{p_B}B\right)_{B\in\mathscr{B}}$ be a limit cone on $1_{\mathscr{B}}$. Prove that $p_L$ is the identity on $L$, and deduce that $L$ is initial.

**A.4** Here you will prove the special case of Lemma A.1 in which the category concerned is a poset. Let $C$ be a poset and $S\subseteq C$.

(a) What does it mean, in purely order-theoretic terms, for $S$ to be a weakly initial set in $C$?

(b) Prove directly that if $S$ is weakly initial and the meet $\bigwedge_{s\in S}s$ exists then $\bigwedge_{s\in S}s$ is a least element of $C$.

**A.5** Let $G:\mathscr{B}\to\mathscr{A}$ be a limit-preserving functor, and let $A\in\mathscr{A}$.

(a) Show that for any small category $\mathbf{I}$, a diagram of shape $\mathbf{I}$ in $(A\Rightarrow G)$ amounts to a diagram $E$ of shape $\mathbf{I}$ in $\mathscr{B}$ together with a cone on $G\circ E$ with vertex $A$.

(b) Prove that the projection functor $P_A:(A\Rightarrow G)\to\mathscr{B}$ of (6.21) creates limits.
