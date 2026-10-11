---
title: "Quiver representations"
description: "《Introduction to Representation Theory》English。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"Representations of finite groups: Further results","link":"/library/volume-88/original-chapter-005"}
next: {"text":"Introduction to categories","link":"/library/volume-88/original-chapter-007"}
---

# Quiver representations

<span class="original-page-anchor" id="pdf-page-153" aria-hidden="true"></span>

## 6.1. Problems

**Problem 6.1.1. Field embeddings.** Recall that $k(y_1,\ldots,y_m)$ denotes the field of rational functions of $y_1,\ldots,y_m$ over a field $k$. Let $f:k[x_1,\ldots,x_n]\to k(y_1,\ldots,y_m)$ be an injective $k$-algebra homomorphism. Show that $m\ge n$. (Look at the growth of dimensions of the spaces $W_N$ of polynomials of degree $N$ in $x_i$ and their images under $f$ as $N\to\infty$.) Deduce that if $f:k(x_1,\ldots,x_n)\to k(y_1,\ldots,y_m)$ is a $k$-linear field embedding, then $m\ge n$.

**Problem 6.1.2. Some algebraic geometry.** Let $k$ be an algebraically closed field, and let $G=GL_n(k)$. Let $V$ be an algebraic representation of $G$. Show that if $G$ has finitely many orbits on $V$, then $\dim(V)\le n^2$. Namely:

(a) Let $x_1,\ldots,x_N$ be linear coordinates on $V$. Let us say that a subset $X$ of $V$ is **Zariski dense** if any polynomial $f(x_1,\ldots,x_N)$ which vanishes on $X$ is zero (coefficientwise). Show that if $G$ has finitely many orbits on $V$, then $G$ has at least one Zariski dense orbit on $V$.

(b) Use (a) to construct a field embedding $k(x_1,\ldots,x_N)\to k(g_{pq})$. Then use Problem 6.1.1.

(c) Generalize the result of this problem to the case when $G=GL_{n_1}(k)\times\cdots\times GL_{n_m}(k)$.

<span class="original-page-anchor" id="pdf-page-154" aria-hidden="true"></span>

**Problem 6.1.3. Dynkin diagrams.** Let $\Gamma$ be a graph, i.e., a finite set of points (vertices) connected with a certain number of edges (we allow multiple edges). We assume that $\Gamma$ is connected (any vertex can be connected to any other by a path of edges) and has no self-loops (edges from a vertex to itself). Suppose the vertices of $\Gamma$ are labeled by integers $1,\ldots,N$. Then one can assign to $\Gamma$ an $N\times N$ matrix $R_\Gamma=(r_{ij})$, where $r_{ij}$ is the number of edges connecting vertices $i$ and $j$. This matrix is obviously symmetric and is called the **adjacency matrix**. Define the matrix $A_\Gamma=2I-R_\Gamma$, where $I$ is the identity matrix.

**Definition 6.1.4.** $\Gamma$ is said to be a **Dynkin diagram** if the quadratic form on $\mathbb R^N$ with matrix $A_\Gamma$ is positive definite.

Dynkin diagrams appear in many areas of mathematics (singularity theory, Lie algebras, representation theory, algebraic geometry, mathematical physics, etc.). In this problem you will get a complete classification of Dynkin diagrams. Namely, you will prove

**Theorem.** $\Gamma$ is a Dynkin diagram if and only if it is one of the following graphs:

![A_N](/library/volume-88/diagrams/pdf-0154-an.png)

![D_N](/library/volume-88/diagrams/pdf-0154-dn.png)

![E_6](/library/volume-88/diagrams/pdf-0154-e6.png)

<span class="original-page-anchor" id="pdf-page-155" aria-hidden="true"></span>

![E_7](/library/volume-88/diagrams/pdf-0155-e7.png)

![E_8](/library/volume-88/diagrams/pdf-0155-e8.png)

(a) Compute the determinant of $A_\Gamma$ where $\Gamma=A_N,D_N$. (Use the row decomposition rule, and write down a recursive equation for it.) Deduce by Sylvester criterion that $A_N,D_N$ are Dynkin diagrams.[^sylvester-155]

(b) Compute the determinants of $A_\Gamma$ for $E_6,E_7,E_8$ (use row decomposition and reduce to (a)). Show they are Dynkin diagrams.

(c) Show that if $\Gamma$ is a Dynkin diagram, it cannot have cycles. For this, show that $\det(A_\Gamma)=0$ for a graph $\Gamma$ below:[^labels-155]

![Cycle](/library/volume-88/diagrams/pdf-0155-cycle.png)

(Show that the sum of rows is $0$.) Thus $\Gamma$ has to be a tree.

(d) Show that if $\Gamma$ is a Dynkin diagram, it cannot have vertices with four or more incoming edges and that $\Gamma$ can have no more than one vertex with three incoming edges. For this, show that $\det(A_\Gamma)=0$ for a graph $\Gamma$ below:

![Two branching vertices](/library/volume-88/diagrams/pdf-0155-fork.png)

(e) Show that $\det(A_\Gamma)=0$ for all graphs $\Gamma$ below:

<span class="original-page-anchor" id="pdf-page-156" aria-hidden="true"></span>

![Affine Dynkin diagrams](/library/volume-88/diagrams/pdf-0156-affine.png)

(f) Deduce from (a)–(e) the classification theorem for Dynkin diagrams.

(g) A (simply laced) **affine Dynkin diagram** is a connected graph without self-loops such that the quadratic form defined by $A_\Gamma$ is positive semidefinite. Classify affine Dynkin diagrams. (Show that they are exactly the forbidden diagrams from (c)–(e).)

**Problem 6.1.5.** Let $Q$ be a quiver with a set of vertices $D$. We say that $Q$ is of **finite type** if it has finitely many indecomposable representations. Let $b_{ij}$ be the number of edges from $i$ to $j$ in $Q$ ($i,j\in D$).

We have the following remarkable theorem, proved by P. Gabriel in early 1970s.

**Theorem.** A connected quiver $Q$ is of finite type if and only if the corresponding unoriented graph (i.e., with directions of arrows forgotten) is a Dynkin diagram (see Theorem 6.5.2 below).

In this problem you will prove the “only if” direction of this theorem (i.e., why other quivers are NOT of finite type).

<span class="original-page-anchor" id="pdf-page-157" aria-hidden="true"></span>

(a) Show that if $Q$ is of finite type, then for any rational numbers $x_i\ge0$ which are not simultaneously zero, one has $q(x_1,\ldots,x_N)>0$, where

$$
q(x_1,\ldots,x_N):=\sum_{i\in D}x_i^2-\frac12\sum_{i,j\in D}b_{ij}x_ix_j.
$$

Hint: It suffices to check the result for integers: $x_i=n_i$. First assume that $n_i\ge0$, and consider the space $W$ of representations $V$ of $Q$ such that $\dim V_i=n_i$. Show that the group $\prod_i GL_{n_i}(k)$ acts with finitely many orbits on $W\oplus k$, and use Problem 6.1.2 to derive the inequality. Then deduce the result in the case when $n_i$ are arbitrary integers.

(b) Deduce that $q$ is a positive definite quadratic form.

Hint: Use the fact that $\mathbb Q$ is dense in $\mathbb R$.

(c) Show that a quiver of finite type can have no self-loops. Then, using Problem 6.1.3, deduce the theorem.

**Problem 6.1.6.** Let $G\ne\{1\}$ be a finite subgroup of $SU(2)$ and let $V$ be the 2-dimensional representation of $G$ coming from its embedding into $SU(2)$. Let $V_i$, $i\in I$, be all the irreducible representations of $G$. Let $r_{ij}$ be the multiplicity of $V_i$ in $V\otimes V_j$.

(a) Show that $r_{ij}=r_{ji}$.

(b) The **McKay graph** of $G$, $M(G)$, is the graph whose vertices are labeled by $i\in I$, and $i$ is connected to $j$ by $r_{ij}$ edges. Show that $M(G)$ is connected. (Use Problem 4.12.10.)

(c) Show that $M(G)$ is an affine Dynkin diagram (one of the “forbidden” graphs in Problem 6.1.3). For this, show that the matrix $a_{ij}=2\delta_{ij}-r_{ij}$ is positive semidefinite but not definite, and use Problem 6.1.3.

Hint: Let $f=\sum x_i\chi_{V_i}$, where $\chi_{V_i}$ are the characters of $V_i$. Show directly that $((2-\chi_V)f,f)\ge0$. When is it equal to $0$? Next, show that $M(G)$ has no self-loops by using the fact that if $G$ is not cyclic, then $G$ contains the central element $-\operatorname{Id}\in SU(2)$.

(d) Which groups from Problem 4.12.8 correspond to which diagrams?

<span class="original-page-anchor" id="pdf-page-158" aria-hidden="true"></span>

(e) Using the McKay graph, find the dimensions of irreducible representations of all finite $G\subset SU(2)$ (namely, show that they are the numbers labeling the vertices of the affine Dynkin diagrams on our pictures). Compare with the results on subgroups of $SO(3)$ we obtained in Problem 4.12.8.

## 6.2. Indecomposable representations of the quivers $A_1,A_2,A_3$

We have seen that a central question about representations of quivers is whether a certain connected quiver has only finitely many indecomposable representations. In the previous subsection it is shown that only those quivers whose underlying undirected graph is a Dynkin diagram may have this property. To see if they actually do have this property, we first explicitly decompose representations of certain easy quivers.

**Remark 6.2.1.** By an object of the type $1\longrightarrow0$ we mean a map from a 1-dimensional vector space to the zero space. Similarly, an object of the type $0\longrightarrow1$ is a map from the zero space into a 1-dimensional space. The object $1\longrightarrow1$ means an isomorphism from a 1-dimensional to another 1-dimensional space. The numbers in such diagrams always mean the dimension of the attached spaces and the maps are the canonical maps (unless specified otherwise).

**Example 6.2.2 ($A_1$).** The quiver $A_1$ consists of a single vertex and has no edges. Since a representation of this quiver is just a single vector space, the only indecomposable representation is the ground field (= a 1-dimensional space).

**Example 6.2.3 ($A_2$).** The quiver $A_2$ consists of two vertices connected by a single edge:

$$
\bullet\longrightarrow\bullet
$$

A representation of this quiver consists of two vector spaces $V,W$ and an operator $A:V\to W$:

![A_2 representation](/library/volume-88/diagrams/pdf-0158-a2.png)

<span class="original-page-anchor" id="pdf-page-159" aria-hidden="true"></span>

To decompose this representation, we first let $V'$ be a complement to the kernel of $A$ in $V$ and let $W'$ be a complement to the image of $A$ in $W$. Then we can decompose the representation as follows:

![Decomposition of an A_2 representation](/library/volume-88/diagrams/pdf-0159-a2-decomposition.png)

The first summand is a multiple of the object $1\longrightarrow0$, the second a multiple of $1\longrightarrow1$, and the third of $0\longrightarrow1$. We see that the quiver $A_2$ has three indecomposable representations, namely

$$
1\longrightarrow0,\qquad1\longrightarrow1,\qquad\text{and}\quad0\longrightarrow1.
$$

Note that this statement is just the Gauss elimination theorem for matrices.

**Example 6.2.4 ($A_3$).** The quiver $A_3$ consists of three vertices and two connections between them. So we have to choose between two possible orientations:

$$
\bullet\longrightarrow\bullet\longrightarrow\bullet\qquad\text{or}\qquad\bullet\longrightarrow\bullet\longleftarrow\bullet.
$$

(1) We first look at the orientation

$$
\bullet\longrightarrow\bullet\longrightarrow\bullet.
$$

Then a representation of this quiver looks like

![An A_3 representation](/library/volume-88/diagrams/pdf-0159-a3.png)

As in Example 6.2.3 we first split away

![Splitting off the kernel of A](/library/volume-88/diagrams/pdf-0159-kernel.png)

This object is a multiple of $1\longrightarrow0\longrightarrow0$. Next, let $Y'$ be a complement of $\operatorname{Im}B$ in $Y$. Then we can also split away

![Splitting off a complement of the image of B](/library/volume-88/diagrams/pdf-0159-cokernel.png)

which is a multiple of the object $0\longrightarrow0\longrightarrow1$. This results in a situation where the map $A$ is injective and the map $B$ is surjective <span class="original-page-anchor" id="pdf-page-160" aria-hidden="true"></span>(we rename the spaces to simplify notation):

![Injective A and surjective B](/library/volume-88/diagrams/pdf-0160-injective-surjective.png)

Next, let $X=\ker(B\circ A)$ and let $X'$ be a complement of $X$ in $V$. Let $W'$ be a complement of $A(X)$ in $W$ such that $A(X')\subset W'$. Then we get

![First decomposition](/library/volume-88/diagrams/pdf-0160-first-decomposition.png)

The first of these summands is a multiple of $1\xrightarrow{\sim}1\longrightarrow0$. Looking at the second summand, we now have a situation where $A$ is injective, $B$ is surjective, and furthermore $\ker(B\circ A)=0$. To simplify notation, we redefine

$$
V=X',\qquad W=W'.
$$

Next we let $X=\operatorname{Im}(B\circ A)$ and let $X'$ be a complement of $X$ in $Y$. Furthermore, let $W'=B^{-1}(X')$. Then $W'$ is a complement of $A(V)$ in $W$. This yields the decomposition

![Second decomposition](/library/volume-88/diagrams/pdf-0160-second-decomposition.png)

Here, the first summand is a multiple of $1\xrightarrow{\sim}1\xrightarrow{\sim}1$. By splitting away the kernel of $B$, the second summand can be decomposed into multiples of $0\longrightarrow1\xrightarrow{\sim}1$ and $0\longrightarrow1\longrightarrow0$. So, on the whole, this quiver has six indecomposable representations:

$$
\begin{gathered}
1\longrightarrow0\longrightarrow0,\quad0\longrightarrow0\longrightarrow1,\quad1\xrightarrow{\sim}1\longrightarrow0,\\
1\xrightarrow{\sim}1\xrightarrow{\sim}1,\quad0\longrightarrow1\xrightarrow{\sim}1,\quad0\longrightarrow1\longrightarrow0.
\end{gathered}
$$

(2) Now we look at the orientation

$$
\bullet\longrightarrow\bullet\longleftarrow\bullet.
$$

<span class="original-page-anchor" id="pdf-page-161" aria-hidden="true"></span>

Very similarly to the other orientation, we can split away objects of the type

$$
1\longrightarrow0\longleftarrow0,\qquad0\longrightarrow0\longleftarrow1,
$$

which results in a situation where both $A$ and $B$ are injective:

![Two injective maps](/library/volume-88/diagrams/pdf-0161-injective-pair.png)

By identifying $V$ and $Y$ as subspaces of $W$, this leads to the problem of classifying pairs of subspaces of a given space $W$ up to isomorphism (the **pair of subspaces problem**). To do so, we first choose a complement $W'$ of $V\cap Y$ in $W$ and set $V'=W'\cap V$, $Y'=W'\cap Y$. Then we can decompose the representation as follows:

![Splitting off the intersection](/library/volume-88/diagrams/pdf-0161-intersection-decomposition.png)

The second summand is a multiple of the object $1\xrightarrow{\sim}1\xleftarrow{\sim}1$. We go on decomposing the first summand. Again, to simplify notation, we let

$$
V=V',\qquad W=W',\qquad Y=Y'.
$$

We can now assume that $V\cap Y=0$. Next, let $W'$ be a complement of $V\oplus Y$ in $W$. Then we get

![Splitting off a complement to the sum](/library/volume-88/diagrams/pdf-0161-sum-decomposition.png)

The second of these summands is a multiple of the indecomposable object $0\longrightarrow1\longleftarrow0$. The first summand can be further decomposed as follows:

![Decomposing the sum of subspaces](/library/volume-88/diagrams/pdf-0161-separate-decomposition.png)

These summands are multiples of

$$
1\longrightarrow1\longleftarrow0,\qquad0\longrightarrow1\longleftarrow1.
$$

<span class="original-page-anchor" id="pdf-page-162" aria-hidden="true"></span>

So—as in the other orientation—we get six indecomposable representations of $A_3$:

$$
\begin{gathered}
1\longrightarrow0\longleftarrow0,\quad0\longrightarrow0\longleftarrow1,\quad1\xrightarrow{\sim}1\xleftarrow{\sim}1,\\
0\longrightarrow1\longleftarrow0,\quad1\longrightarrow1\longleftarrow0,\quad0\longrightarrow1\longleftarrow1.
\end{gathered}
$$

## 6.3. Indecomposable representations of the quiver $D_4$

As the last—slightly more complicated—example we consider the quiver $D_4$.

**Example 6.3.1 ($D_4$).** We restrict ourselves to the orientation

![D_4 orientation](/library/volume-88/diagrams/pdf-0162-d4.png)

So a representation of this quiver looks like

![D_4 representation](/library/volume-88/diagrams/pdf-0162-representation.png)

The first thing we can do is—as usual—split away the kernels of the maps $A_1,A_2,A_3$. More precisely, we split away the representations

![Kernel of A_1](/library/volume-88/diagrams/pdf-0162-kernel1.png)

![Kernel of A_2](/library/volume-88/diagrams/pdf-0162-kernel2.png)

<span class="original-page-anchor" id="pdf-page-163" aria-hidden="true"></span>

![Kernel of A_3](/library/volume-88/diagrams/pdf-0163-kernel3.png)

These representations are multiples of the indecomposable objects

![First outer-vertex simple representation](/library/volume-88/diagrams/pdf-0163-simple1.png)

![Second outer-vertex simple representation](/library/volume-88/diagrams/pdf-0163-simple2.png)

![Third outer-vertex simple representation](/library/volume-88/diagrams/pdf-0163-simple3.png)

So we get to a situation where all of the maps $A_1,A_2,A_3$ are injective:

![Three injective maps](/library/volume-88/diagrams/pdf-0163-injective.png)

As in Example 6.2.4, we can then identify the spaces $V_1,V_2,V_3$ with subspaces of $V$. So we get to the **triple of subspaces problem** of classifying triples of subspaces of a given space $V$.

<span class="original-page-anchor" id="pdf-page-164" aria-hidden="true"></span>

The next step is to split away a multiple of

![Central-vertex simple representation](/library/volume-88/diagrams/pdf-0164-central-simple.png)

to reach a situation where

$$
V_1+V_2+V_3=V.
$$

By letting $Y=V_1\cap V_2\cap V_3$, choosing a complement $V'$ of $Y$ in $V$, and setting $V_i'=V'\cap V_i$, $i=1,2,3$, we can decompose this representation into

![Splitting off the triple intersection](/library/volume-88/diagrams/pdf-0164-triple-intersection.png)

The last summand is a multiple of the indecomposable representation

![All four spaces have dimension one](/library/volume-88/diagrams/pdf-0164-full-simple.png)

So—considering the first summand and renaming the spaces to simplify notation—we are in a situation where

$$
V=V_1+V_2+V_3,\qquad V_1\cap V_2\cap V_3=0.
$$

As a next step, we let $Y=V_1\cap V_2$ and we choose a complement $V'$ of $Y$ in $V$ such that $V_3\subset V'$ and set $V_1'=V'\cap V_1$, $V_2'=V'\cap V_2$. This <span class="original-page-anchor" id="pdf-page-165" aria-hidden="true"></span>yields the decomposition

![Splitting off V_1 intersection V_2](/library/volume-88/diagrams/pdf-0165-pair-intersection.png)

The second summand is a multiple of the indecomposable object

![A one-dimensional V_1 and V_2 intersection](/library/volume-88/diagrams/pdf-0165-pair12.png)

In the resulting situation we have $V_1\cap V_2=0$. Similarly we can split away multiples of

![A V_1 and V_3 intersection](/library/volume-88/diagrams/pdf-0165-pair13.png) and ![A V_2 and V_3 intersection](/library/volume-88/diagrams/pdf-0165-pair23.png)

to reach a situation where the spaces $V_1,V_2,V_3$ do not intersect pairwise:

$$
V_1\cap V_2=V_1\cap V_3=V_2\cap V_3=0.
$$

If $V_1\nsubseteq V_2\oplus V_3$, we let $Y=V_1\cap(V_2\oplus V_3)$. We let $V_1'$ be a complement of $Y$ in $V_1$. Since then $V_1'\cap(V_2\oplus V_3)=0$, we can select a complement <span class="original-page-anchor" id="pdf-page-166" aria-hidden="true"></span>$V'$ of $V_1'$ in $V$ which contains $V_2\oplus V_3$. This gives us the decomposition

![Splitting off a complement in V_1](/library/volume-88/diagrams/pdf-0166-sum-splitting.png)

The first of these summands is a multiple of

![One nonzero outer space V_1](/library/volume-88/diagrams/pdf-0166-arm1.png)

By splitting these away, we get to a situation where $V_1\subseteq V_2\oplus V_3$. Similarly, we can split away objects of the type

![One nonzero outer space V_2](/library/volume-88/diagrams/pdf-0166-arm2.png) and ![One nonzero outer space V_3](/library/volume-88/diagrams/pdf-0166-arm3.png)

to reach a situation in which the following conditions hold:

(1) $V_1+V_2+V_3=V$.

(2) $V_1\cap V_2=0$, $V_1\cap V_3=0$, $V_2\cap V_3=0$.

(3) $V_1\subseteq V_2\oplus V_3$, $V_2\subseteq V_1\oplus V_3$, $V_3\subseteq V_1\oplus V_2$.

But this implies that

$$
V_1\oplus V_2=V_1\oplus V_3=V_2\oplus V_3=V.
$$

So we get

$$
\dim V_1=\dim V_2=\dim V_3=n
$$

<span class="original-page-anchor" id="pdf-page-167" aria-hidden="true"></span>

and

$$
\dim V=2n.
$$

Since $V_3\subseteq V_1\oplus V_2$, we can write every element of $V_3$ in the form

$$
x\in V_3,\qquad x=(x_1,x_2),\quad x_1\in V_1,\quad x_2\in V_2.
$$

We then can define the projections

$$
B_1:V_3\to V_1,\quad(x_1,x_2)\mapsto x_1,
$$

$$
B_2:V_3\to V_2,\quad(x_1,x_2)\mapsto x_2.
$$

Since $V_3\cap V_1=0$ and $V_3\cap V_2=0$, these maps have to be injective and therefore are isomorphisms. We then define the isomorphism

$$
A=B_2\circ B_1^{-1}:V_1\to V_2.
$$

Let $e_1,\ldots,e_n$ be a basis for $V_1$. Then we get

$$
\begin{aligned}
V_1&=\mathbb Ce_1\oplus\mathbb Ce_2\oplus\cdots\oplus\mathbb Ce_n,\\
V_2&=\mathbb CAe_1\oplus\mathbb CAe_2\oplus\cdots\oplus\mathbb CAe_n,\\
V_3&=\mathbb C(e_1+Ae_1)\oplus\mathbb C(e_2+Ae_2)\oplus\cdots\oplus\mathbb C(e_n+Ae_n).
\end{aligned}
$$

So we can think of $V_3$ as the graph of an isomorphism $A:V_1\to V_2$. From this we obtain the decomposition

![Decomposition into graph representations](/library/volume-88/diagrams/pdf-0167-graph-decomposition.png)

These correspond to the indecomposable object

![The indecomposable representation with central dimension two](/library/volume-88/diagrams/pdf-0167-two-dimensional.png)

Thus the quiver $D_4$ with the selected orientation has 12 indecomposable objects. If one were to explicitly decompose representations for the other possible orientations, one would also find 12 indecomposable objects.

<span class="original-page-anchor" id="pdf-page-168" aria-hidden="true"></span>

It appears as if the number of indecomposable representations does not depend on the orientation of the edges—and indeed Gabriel’s theorem will generalize this observation.

## 6.4. Roots

From now on, let $\Gamma$ be a fixed graph of type $A_n,D_n,E_6,E_7,E_8$. We denote the adjacency matrix of $\Gamma$ by $R_\Gamma$.

**Definition 6.4.1 (Cartan matrix).** We define the **Cartan matrix** of $\Gamma$ as

$$
A_\Gamma=2\operatorname{Id}-R_\Gamma.
$$

On the lattice $\mathbb Z^n$ (or the space $\mathbb R^n$) we then define an inner product

$$
B(x,y)=x^TA_\Gamma y
$$

corresponding to the graph $\Gamma$.

**Lemma 6.4.2.** (1) $B$ is positive definite.

(2) $B(x,x)$ takes only even values for $x\in\mathbb Z^n$.

**Proof.** (1) This follows by definition, since $\Gamma$ is a Dynkin diagram.

(2) By the definition of the Cartan matrix we get

$$
\begin{aligned}
B(x,x)=x^TA_\Gamma x
&=\sum_{i,j}x_i a_{ij}x_j
=2\sum_i x_i^2+\sum_{i,j,\ i\ne j}x_i a_{ij}x_j\\
&=2\sum_i x_i^2+2\cdot\sum_{i<j}a_{ij}x_ix_j,
\end{aligned}
$$

which is even. $\square$

**Definition 6.4.3.** A **root** with respect to a certain positive inner product is a shortest (with respect to this inner product) nonzero vector in $\mathbb Z^n$.

So for the inner product $B$, a root is a nonzero vector $x\in\mathbb Z^n$ such that

$$
B(x,x)=2.
$$

**Remark 6.4.4.** There can be only finitely many roots, since all of them have to lie in some ball.

<span class="original-page-anchor" id="pdf-page-169" aria-hidden="true"></span>

**Definition 6.4.5.** We call vectors of the form

$$
\alpha_i=(0,\ldots,\overbrace{1}^{\text{ith}},\ldots,0)
$$

**simple roots**.

The $\alpha_i$ naturally form a basis of the lattice $\mathbb Z^n$.

**Lemma 6.4.6.** Let $\alpha$ be a root, $\alpha=\sum_{i=1}^n k_i\alpha_i$. Then either $k_i\geq 0$ for all $i$ or $k_i\leq 0$ for all $i$.

**Proof.** Assume the contrary, i.e., $k_i>0$, $k_j<0$. Without loss of generality, we can also assume that $k_s=0$ for all $s$ between $i$ and $j$. We can identify the indices $i,j$ with vertices of the graph $\Gamma$:

![The edge between i and i′ on the path toward j.](/library/volume-88/diagrams/pdf-0169-root-graph.png)

Next, let $\epsilon$ be the edge connecting $i$ with the next vertex towards $j$ and let $i'$ be the vertex on the other end of $\epsilon$. We then let $\Gamma_1,\Gamma_2$ be the graphs obtained from $\Gamma$ by removing $\epsilon$. Since $\Gamma$ is supposed to be a Dynkin diagram—and therefore has no cycles or loops—both $\Gamma_1$ and $\Gamma_2$ will be connected graphs which are not connected to each other:

![The two connected components Γ₁ and Γ₂ after removing the edge.](/library/volume-88/diagrams/pdf-0169-split-graph.png)

Then we have $i\in\Gamma_1$, $j\in\Gamma_2$. We define

$$
\beta=\sum_{m\in\Gamma_1}k_m\alpha_m,\qquad
\gamma=\sum_{m\in\Gamma_2}k_m\alpha_m.
$$

With this choice we get

$$
\alpha=\beta+\gamma.
$$

Since $k_i>0$, $k_j<0$, we know that $\beta\neq 0$, $\gamma\neq 0$ and therefore

$$
B(\beta,\beta)\geq 2,\qquad B(\gamma,\gamma)\geq 2.
$$

<span class="original-page-anchor" id="pdf-page-170" aria-hidden="true"></span>

Furthermore,

$$
B(\beta,\gamma)=-k_i k_{i'}
$$

since $\Gamma_1,\Gamma_2$ are only connected at $\epsilon$. But this has to be a nonnegative number, since $k_i>0$ and $k_{i'}\leq 0$. This yields

$$
B(\alpha,\alpha)=B(\beta+\gamma,\beta+\gamma)
=\underbrace{B(\beta,\beta)}_{\geq 2}
+2\underbrace{B(\beta,\gamma)}_{\geq 0}
+\underbrace{B(\gamma,\gamma)}_{\geq 2}\geq 4.
$$

But this is a contradiction, since $\alpha$ was assumed to be a root. $\square$

**Definition 6.4.7.** We call a root $\alpha=\sum_i k_i\alpha_i$ a **positive root** if all $k_i\geq 0$. A root for which $k_i\leq 0$ for all $i$ is called a **negative root**.

**Remark 6.4.8.** Lemma 6.4.6 states that every root is either positive or negative.

**Example 6.4.9.** (1) Let $\Gamma$ be of the type $A_{N-1}$. Then the lattice $L=\mathbb Z^{N-1}$ can be realized as a subgroup of the lattice $\mathbb Z^N$ by letting $L\subseteq\mathbb Z^N$ be the subgroup of all vectors $(x_1,\ldots,x_N)$ such that

$$
\sum_i x_i=0.
$$

The vectors

$$
\begin{aligned}
\alpha_1&=(1,-1,0,\ldots,0),\\
\alpha_2&=(0,1,-1,0,\ldots,0),\\
&\phantom{=}\vdots\\
\alpha_{N-1}&=(0,\ldots,0,1,-1)
\end{aligned}
$$

naturally form a basis of $L$. Furthermore, the standard inner product

$$
(x,y)=\sum_i x_i y_i
$$

on $\mathbb Z^N$ restricts to the inner product $B$ given by $\Gamma$ on $L$, since it takes the same values on the basis vectors:

$$
\begin{aligned}
(\alpha_i,\alpha_i)&=2,\\
(\alpha_i,\alpha_j)&=\begin{cases}
-1,&i,j\text{ are adjacent},\\
0,&\text{otherwise}.
\end{cases}
\end{aligned}
$$

This means that vectors of the form

$$
(0,\ldots,0,1,0,\ldots,0,-1,0,\ldots,0)
=\alpha_i+\alpha_{i+1}+\cdots+\alpha_{j-1}
$$

<span class="original-page-anchor" id="pdf-page-171" aria-hidden="true"></span>

and

$$
(0,\ldots,0,-1,0,\ldots,0,1,0,\ldots,0)
=-(\alpha_i+\alpha_{i+1}+\cdots+\alpha_{j-1})
$$

are the roots of $L$. Therefore the number of positive roots in $L$ equals

$$
\frac{N(N-1)}{2}.
$$

(2) As a fact, we also state the number of positive roots in the other Dynkin diagrams:

$$
\begin{aligned}
D_N:&\quad N(N-1)\text{ roots},\\
E_6:&\quad 36\text{ roots},\\
E_7:&\quad 63\text{ roots},\\
E_8:&\quad 120\text{ roots}.
\end{aligned}
$$

**Definition 6.4.10.** Let $\alpha\in\mathbb Z^n$ be a positive root. The reflection $s_\alpha$ is defined by the formula

$$
s_\alpha(v)=v-B(v,\alpha)\alpha.
$$

We denote $s_{\alpha_i}$ by $s_i$ and call these **simple reflections**.

**Remark 6.4.11.** As a linear operator of $\mathbb R^n$, $s_\alpha$ fixes any vector orthogonal to $\alpha$ and

$$
s_\alpha(\alpha)=-\alpha.
$$

Therefore $s_\alpha$ is the reflection at the hyperplane orthogonal to $\alpha$ and in particular fixes $B$. The $s_i$ generate a subgroup $W\subseteq O(\mathbb R^n)$, which is called the **Weyl group** of $\Gamma$. Since for every $w\in W$, $w(\alpha_i)$ is a root, and since there are only finitely many roots, $W$ has to be finite.

## 6.5. Gabriel’s theorem

**Definition 6.5.1.** Let $Q$ be a quiver with any labeling $1,\ldots,n$ of the vertices. Let $V=(V_1,\ldots,V_n)$ be a representation of $Q$. We then call

$$
d(V)=(\dim V_1,\ldots,\dim V_n)
$$

the **dimension vector** of this representation.

We are now able to formulate Gabriel’s theorem using roots.

<span class="original-page-anchor" id="pdf-page-172" aria-hidden="true"></span>

**Theorem 6.5.2 (Gabriel’s theorem).** Let $Q$ be a quiver of type $A_n$, $D_n$, $E_6$, $E_7$, $E_8$. Then $Q$ has finitely many indecomposable representations. Namely, the dimension vector of any indecomposable representation is a positive root (with respect to $B_\Gamma$) and for any positive root $\alpha$ there is exactly one indecomposable representation with dimension vector $\alpha$.

## 6.6. Reflection functors

**Definition 6.6.1.** Let $Q$ be any quiver. We call a vertex $i\in Q$ a **sink** if all edges connected to $i$ point towards $i$:

![All arrows point toward the sink i.](/library/volume-88/diagrams/pdf-0172-sink.png)

We call a vertex $i\in Q$ a **source** if all edges connected to $i$ point away from $i$:

![All arrows point away from the source i.](/library/volume-88/diagrams/pdf-0172-source.png)

**Definition 6.6.2.** Let $Q$ be any quiver and let $i\in Q$ be a sink (respectively, a source). Then we let $\overline Q_i$ be the quiver obtained from $Q$ by reversing all arrows pointing into (respectively, pointing out of) $i$.

We are now able to define the **reflection functors** (also called **Coxeter functors**).

**Definition 6.6.3.** Let $Q$ be a quiver, and let $i\in Q$ be a sink. Let $V$ be a representation of $Q$. Then we define the reflection functor

$$
F_i^+:\operatorname{Rep}Q\longrightarrow\operatorname{Rep}\overline Q_i
$$

by the rule

$$
\begin{aligned}
F_i^+(V)_k&=V_k\quad\text{if }k\neq i,\\
F_i^+(V)_i&=\ker\left(\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i\right).
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-173" aria-hidden="true"></span>

Also, all maps stay the same except those now pointing out of $i$; these are replaced by compositions of the inclusion of $\ker\varphi$ into $\bigoplus_{j\to i}V_j$ with the projections $\bigoplus_j V_{j\to i}\to V_i$.

**Definition 6.6.4.** Let $Q$ be a quiver, and let $i\in Q$ be a source. Let $V$ be a representation of $Q$. Let $\psi$ be the canonical map

$$
\psi:V_i\longrightarrow\bigoplus_{i\to j}V_j.
$$

Then we define the reflection functor

$$
F_i^-:\operatorname{Rep}Q\longrightarrow\operatorname{Rep}\overline Q_i
$$

by the rule

$$
\begin{aligned}
F_i^-(V)_k&=V_k\quad\text{if }k\neq i,\\
F_i^-(V)_i&=\operatorname{Coker}(\psi)=\left(\bigoplus_{i\to j}V_j\right)/\operatorname{Im}\psi.
\end{aligned}
$$

Again, all maps stay the same except those now pointing into $i$; these are replaced by the compositions of the inclusions $V_k\to\bigoplus_{i\to j}V_j$ with the natural map $\bigoplus_{i\to j}V_j\to\bigoplus_{i\to j}V_j/\operatorname{Im}\psi$.

**Proposition 6.6.5.** Let $Q$ be a quiver and $V$ be an indecomposable representation of $Q$.

(1) Let $i\in Q$ be a sink. Then either $\dim V_i=1$, $\dim V_j=0$ for $j\neq i$ or

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

is surjective.

(2) Let $i\in Q$ be a source. Then either $\dim V_i=1$, $\dim V_j=0$ for $j\neq i$ or

$$
\psi:V_i\longrightarrow\bigoplus_{i\to j}V_j
$$

is injective.

**Proof.** (1) Choose a complement $W$ of $\operatorname{Im}\varphi$. Then we get

![V is the direct sum of a representation supported at the vertex with space W and V′.](/library/volume-88/diagrams/pdf-0173-decomposition.png)

<span class="original-page-anchor" id="pdf-page-174" aria-hidden="true"></span>

Since $V$ is indecomposable, one of these summands has to be zero. If the first summand is zero, then $\varphi$ has to be surjective. If the second summand is zero, then the first one has to be of the desired form, because else we could write it as a direct sum of several objects of the type

![A representation with a one-dimensional space at the sink and zero elsewhere.](/library/volume-88/diagrams/pdf-0174-simple-representation.png)

which is impossible since $V$ was supposed to be indecomposable.

(2) This follows similarly by splitting away the kernel of $\psi$. $\square$

**Proposition 6.6.6.** Let $Q$ be a quiver, and let $V$ be a representation of $Q$.

(1) If

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

is surjective, then

$$
F_i^-F_i^+V=V.
$$

(2) If

$$
\psi:V_i\longrightarrow\bigoplus_{i\to j}V_j
$$

is injective, then

$$
F_i^+F_i^-V=V.
$$

**Proof.** In the following proof, by $i\to j$ we will always mean that $i$ points into $j$ in the original quiver $Q$. We only establish the first statement and we also restrict ourselves to showing that the spaces of $V$ and $F_i^-F_i^+V$ are the same. It is enough to do so for the $i$th space. Let

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

be surjective and let

$$
K=\ker\varphi.
$$

<span class="original-page-anchor" id="pdf-page-175" aria-hidden="true"></span>

When applying $F_i^+$, the space $V_i$ gets replaced by $K$. Furthermore, let

$$
\psi:K\longrightarrow\bigoplus_{j\to i}V_j.
$$

After applying $F_i^-$, $K$ gets replaced by

$$
K'=\left(\bigoplus_{j\to i}V_j\right)/(\operatorname{Im}\psi).
$$

But

$$
\operatorname{Im}\psi=K
$$

and therefore

$$
K'=\left(\bigoplus_{j\to i}V_j\right)
/\left(\ker\left(\varphi:\bigoplus_{j\to i}V_j\to V_i\right)\right)
=\operatorname{Im}\left(\varphi:\bigoplus_{j\to i}V_j\to V_i\right)
$$

by the homomorphism theorem. Since $\varphi$ was assumed to be surjective, we get

$$
K'=V_i.
$$

$\square$

**Proposition 6.6.7.** Let $Q$ be a quiver, and let $V$ be an indecomposable representation of $Q$. Then $F_i^+V$ and $F_i^-V$ (whenever defined) are either indecomposable or $0$.

**Proof.** We prove the proposition for $F_i^+V$; the case $F_i^-V$ follows similarly. By Proposition 6.6.5 it follows that either

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

is surjective or $\dim V_i=1$, $\dim V_j=0$, $j\neq i$. In the last case

$$
F_i^+V=0.
$$

So we can assume that $\varphi$ is surjective. In this case, assume that $F_i^+V$ is decomposable as

$$
F_i^+V=X\oplus Y
$$

<span class="original-page-anchor" id="pdf-page-176" aria-hidden="true"></span>

with $X,Y\neq 0$. But $F_i^+V$ is injective at $i$, since the maps are canonical projections, whose direct sum is the tautological embedding. Therefore $X$ and $Y$ also have to be injective at $i$ and hence (by Proposition 6.6.6)

$$
F_i^+F_i^-X=X,\qquad F_i^+F_i^-Y=Y.
$$

In particular

$$
F_i^-X\neq 0,\qquad F_i^-Y\neq 0.
$$

Therefore

$$
V=F_i^-F_i^+V=F_i^-X\oplus F_i^-Y,
$$

which is a contradiction, since $V$ was assumed to be indecomposable. So we can infer that

$$
F_i^+V
$$

is indecomposable. $\square$

**Proposition 6.6.8.** Let $Q$ be a quiver and let $V$ be a representation of $Q$.

(1) Let $i\in Q$ be a sink and let $V$ be surjective at $i$. Then

$$
d(F_i^+V)=s_i(d(V)).
$$

(2) Let $i\in Q$ be a source and let $V$ be injective at $i$. Then

$$
d(F_i^-V)=s_i(d(V)).
$$

**Proof.** We only prove the first statement; the second one follows similarly. Let $i\in Q$ be a sink and let

$$
\varphi:\bigoplus_{j\to i}V_j\longrightarrow V_i
$$

be surjective. Let $K=\ker\varphi$. Then

$$
\dim K=\sum_{j\to i}\dim V_j-\dim V_i.
$$

Therefore we get

$$
(d(F_i^+V)-d(V))_i=\sum_{j\to i}\dim V_j-2\dim V_i=-B(d(V),\alpha_i)
$$

and

$$
(d(F_i^+V)-d(V))_j=0,\qquad j\neq i.
$$

<span class="original-page-anchor" id="pdf-page-177" aria-hidden="true"></span>

This implies

$$
\begin{aligned}
d(F_i^+V)-d(V)&=-B(d(V),\alpha_i)\alpha_i\\
\Longleftrightarrow\quad d(F_i^+V)&=d(V)-B(d(V),\alpha_i)\alpha_i=s_i(d(V)).
\end{aligned}
$$

$\square$

## 6.7. Coxeter elements

**Definition 6.7.1.** Let $Q$ be a quiver and let $\Gamma$ be the underlying graph. Fix any labeling $1,\ldots,n$ of the vertices of $\Gamma$. Then the **Coxeter element** $c$ of $Q$ corresponding to this labeling is defined as

$$
c=s_1s_2\cdots s_n.
$$

**Lemma 6.7.2.** Let

$$
\beta=\sum_i k_i\alpha_i
$$

with $k_i\geq 0$ for all $i$ but not all $k_i=0$. Then there is $N\in\mathbb N$, such that

$$
c^N\beta
$$

has at least one strictly negative coefficient.

**Proof.** The Coxeter element $c$ belongs to a finite group $W$. So there is $M\in\mathbb N$, such that

$$
c^M=1.
$$

We claim that

$$
1+c+c^2+\cdots+c^{M-1}=0
$$

as operators on $\mathbb R^n$. This implies what we need, since $\beta$ has at least one strictly positive coefficient, so one of the elements

$$
c\beta,c^2\beta,\ldots,c^{M-1}\beta
$$

must have at least one strictly negative coefficient. Furthermore, it is enough to show that $1$ is not an eigenvalue for $c$, since

$$
\begin{aligned}
(1+c+c^2+\cdots+c^{M-1})v&=w\neq 0\\
\Longrightarrow\quad cw&=c(1+c+c^2+\cdots+c^{M-1})v\\
&=(c+c^2+c^3+\cdots+c^{M-1}+1)v=w.
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-178" aria-hidden="true"></span>

Assume the contrary, i.e., $1$ is an eigenvalue of $c$ and let $v$ be a corresponding eigenvector:

$$
\begin{aligned}
cv=v&\Longrightarrow s_1\cdots s_n v=v\\
&\Longleftrightarrow s_2\cdots s_n v=s_1v.
\end{aligned}
$$

But since $s_i$ only changes the $i$th coordinate of $v$, we get

$$
s_1v=v\quad\text{and}\quad s_2\cdots s_n v=v.
$$

Repeating the same procedure, we get

$$
s_i v=v
$$

for all $i$. But this means

$$
B(v,\alpha_i)=0
$$

for all $i$, and since $B$ is nondegenerate, we get $v=0$. But this is a contradiction, since $v$ is an eigenvector. $\square$

## 6.8. Proof of Gabriel’s theorem

Let $V$ be an indecomposable representation of $Q$. We introduce a fixed labeling $1,\ldots,n$ on $Q$, such that $i<j$ if one can reach $j$ from $i$. This is possible, since we can assign the highest label to any sink, remove this sink from the quiver, assign the next highest label to a sink of the remaining quiver, and so on. This way we create a labeling of the desired kind.

We now consider the sequence

$$
V^{(0)}=V,\quad V^{(1)}=F_n^+V,\quad V^{(2)}=F_{n-1}^+F_n^+V,\ldots.
$$

This sequence is well defined because of the selected labeling: $n$ has to be a sink of $Q$, $n-1$ has to be a sink of $\overline Q_n$ (where $\overline Q_n$ is obtained from $Q$ by reversing all the arrows at the vertex $r$) and so on. Furthermore, we note that $V^{(n)}$ is a representation of $Q$ again, since every arrow has been reversed twice (since we applied a reflection functor to every vertex). This implies that we can define

$$
V^{(n+1)}=F_n^+V^{(n)},\ldots
$$

and continue the sequence to infinity.

<span class="original-page-anchor" id="pdf-page-179" aria-hidden="true"></span>

**Theorem 6.8.1.** There exists $m\in\mathbb N$, such that

$$
d\left(V^{(m)}\right)=\alpha_p
$$

for some $p$.

**Proof.** If $V^{(i)}$ is surjective at the appropriate vertex $k$, then

$$
d\left(V^{(i+1)}\right)=d\left(F_k^+V^{(i)}\right)=s_k d\left(V^{(i)}\right).
$$

This implies that if $V^{(0)},\ldots,V^{(i-1)}$ are surjective at the appropriate vertices, then

$$
d\left(V^{(i)}\right)=\cdots s_{n-1}s_n d(V).
$$

By Lemma 6.7.2 this cannot continue indefinitely, since $d\left(V^{(i)}\right)$ may not have any negative entries. Let $i$ be the smallest number such that $V^{(i)}$ is not surjective at the appropriate vertex. By Proposition 6.6.7 it is indecomposable. So, by Proposition 6.6.5, we get

$$
d\left(V^{(i)}\right)=\alpha_p
$$

for some $p$. $\square$

We are now able to prove Gabriel’s theorem. Namely, we get the following corollaries.

**Corollary 6.8.2.** Let $Q$ be a quiver, and let $V$ be any indecomposable representation. Then $d(V)$ is a positive root.

**Proof.** By Theorem 6.8.1

$$
s_{i_1}\cdots s_{i_m}(d(V))=\alpha_p.
$$

Since the $s_i$ preserve $B$, we get

$$
B(d(V),d(V))=B(\alpha_p,\alpha_p)=2.
$$

$\square$

**Corollary 6.8.3.** Let $V,V'$ be indecomposable representations of $Q$ such that $d(V)=d(V')$. Then $V$ and $V'$ are isomorphic.

<span class="original-page-anchor" id="pdf-page-180" aria-hidden="true"></span>

**Proof.** Let $i$ be such that

$$
d\left(V^{(i)}\right)=\alpha_p.
$$

Then we also get $d\left(V'^{(i)}\right)=\alpha_p$. So

$$
V'^{(i)}=V^{(i)}=:V^i.
$$

Furthermore we have

$$
\begin{aligned}
V^{(i)}&=F_k^+\cdots F_{n-1}^+F_n^+V^{(0)},\\
V'^{(i)}&=F_k^+\cdots F_{n-1}^+F_n^+V'^{(0)}.
\end{aligned}
$$

But both $V^{(i-1)},\ldots,V^{(0)}$ and $V'^{(i-1)},\ldots,V'^{(0)}$ have to be surjective at the appropriate vertices. This implies

$$
\begin{aligned}
&F_n^-F_{n-1}^-\cdots F_k^-V^i\\
&\quad=\begin{cases}
F_n^-F_{n-1}^-\cdots F_k^-F_k^+\cdots F_{n-1}^+F_n^+V^{(0)}=V^{(0)}=V,\\
F_n^-F_{n-1}^-\cdots F_k^-F_k^+\cdots F_{n-1}^+F_n^+V'^{(0)}=V'^{(0)}=V'.
\end{cases}
\end{aligned}
$$

$\square$

These two corollaries show that there are only finitely many indecomposable representations (since there are only finitely many roots) and that the dimension vector of each of them is a positive root. The last statement of Gabriel’s theorem follows from

**Corollary 6.8.4.** For every positive root $\alpha$, there is an indecomposable representation $V$ with

$$
d(V)=\alpha.
$$

**Proof.** Consider the sequence

$$
s_n\alpha,\ s_{n-1}s_n\alpha,\ldots.
$$

Consider the first element of this sequence which is a negative root (this has to happen by Lemma 6.7.2) and look at one step before that, calling this element $\beta$. So $\beta$ is a positive root and $s_i\beta$ is a negative root for some $i$. But since the $s_i$ only change one coordinate, we get

$$
\beta=\alpha_i
$$

and

$$
(s_q\cdots s_{n-1}s_n)\alpha=\alpha_i.
$$

<span class="original-page-anchor" id="pdf-page-181" aria-hidden="true"></span>

We let $\mathbb C_{(i)}$ be the representation having dimension vector $\alpha_i$. Then we define

$$
V=F_n^-F_{n-1}^-\cdots F_q^-\mathbb C_{(i)}.
$$

This is an indecomposable representation and

$$
d(V)=\alpha.
$$

$\square$

**Example 6.8.5.** Let us demonstrate by example how reflection functors work. Consider the quiver $D_4$ with the orientation of all arrows towards the node (which is labeled by $4$). Start with the $1$-dimensional representation $V_{\alpha_4}$ sitting at the fourth vertex. Apply to $V_{\alpha_4}$ the functor $F_3^-F_2^-F_1^-$. This yields

$$
F_1^-F_2^-F_3^-V_{\alpha_4}=V_{\alpha_1+\alpha_2+\alpha_3+\alpha_4}.
$$

Now applying $F_4^-$, we get

$$
F_4^-F_1^-F_2^-F_3^-V_{\alpha_4}=V_{\alpha_1+\alpha_2+\alpha_3+2\alpha_4}.
$$

Note that this is exactly the inclusion of three lines into the plane, which is the most complicated indecomposable representation of the $D_4$ quiver.

## 6.9. Problems

**Problem 6.9.1.** Let $Q_n$ be the cyclic quiver of length $n$, i.e., $n$ vertices connected by $n$ oriented edges forming a cycle. Obviously, the classification of indecomposable representations of $Q_1$ is given by the Jordan normal form theorem. Obtain a similar classification of indecomposable representations of $Q_2$. In other words, classify pairs of linear operators $A:V\to W$ and $B:W\to V$ up to isomorphism. Namely:

(a) Consider the following pairs (for $n\geq 1$):

(1) $E_{n,\lambda}$: $V=W=\mathbb C^n$, $A$ is the Jordan block of size $n$ with eigenvalue $\lambda$, $B=1$ ($\lambda\in\mathbb C$).

(2) $E_{n,\infty}$: is obtained from $E_{n,0}$ by exchanging $V$ with $W$ and $A$ with $B$.

(3) $H_n$: $V=\mathbb C^n$ with basis $v_i$, $W=\mathbb C^{n-1}$ with basis $w_i$, $Av_i=w_i$, $Bw_i=v_{i+1}$ for $i<n$, and $Av_n=0$.

<span class="original-page-anchor" id="pdf-page-182" aria-hidden="true"></span>

(4) $K_n$ is obtained from $H_n$ by exchanging $V$ with $W$ and $A$ with $B$.

Show that these are indecomposable and pairwise nonisomorphic.

(b) Show that if $E$ is a representation of $Q_2$ such that $AB$ is not nilpotent, then $E=E'\oplus E''$, where $E''=E_{n,\lambda}$ for some $\lambda\neq 0$.

(c) Consider the case when $AB$ is nilpotent, and consider the operator $X$ on $V\oplus W$ given by $X(v,w)=(Bw,Av)$. Show that $X$ is nilpotent and admits a basis consisting of chains (i.e., sequences $u,Xu,X^2u,\ldots,X^{l-1}u$, where $X^lu=0$) which are compatible with the direct sum decomposition (i.e., for every chain $u\in V$ or $u\in W$). Deduce that (1)–(4) are the only indecomposable representations of $Q_2$.

(d) (Harder!) Generalize this classification to the Kronecker quiver, which has two vertices $1$ and $2$ and two edges both going from $1$ to $2$.

(e) (Still harder!) Can you generalize this classification to $Q_n$, $n>2$ with any orientation? (Easier version: consider only the cyclic orientation).

**Problem 6.9.2.** Let $L\subset\frac12\mathbb Z^8$ be the lattice of vectors where the coordinates are either all integers or all half-integers (but not integers) and the sum of all coordinates is an even integer.

(a) Let $\alpha_i=e_i-e_{i+1}$, $i=1,\ldots,6$, $\alpha_7=e_6+e_7$, $\alpha_8=-\frac12\sum_{i=1}^8 e_i$. Show that $\alpha_i$ are a basis of $L$ (over $\mathbb Z$).

(b) Show that roots in $L$ (under the usual inner product) form a root system of type $E_8$ (compute the inner products of $\alpha_i$).

(c) Show that the $E_7$ and $E_6$ lattices can be obtained as the sets of vectors in the $E_8$ lattice $L$ where the first two, respectively three, coordinates (in the basis $e_i$) are equal.

(d) Show that $E_6,E_7,E_8$ have $72$, $126$, and $240$ roots, respectively (enumerate types of roots in terms of the presentations in the basis $e_i$, and count the roots of each type).

**Problem 6.9.3.** Let $V_\alpha$ be the indecomposable representation of a Dynkin quiver $Q$ which corresponds to a positive root $\alpha$. For instance, if $\alpha_i$ is a simple root, then $V_{\alpha_i}$ has a $1$-dimensional space at $i$ and is $0$ everywhere else.

<span class="original-page-anchor" id="pdf-page-183" aria-hidden="true"></span>

(a) Show that if $i$ is a source, then $\operatorname{Ext}^1(V,V_{\alpha_i})=0$ for any representation $V$ of $Q$, and if $i$ is a sink, then $\operatorname{Ext}^1(V_{\alpha_i},V)=0$.

(b) Given an orientation of the quiver, find a Jordan–Hölder series of $V_\alpha$ for that orientation.

[^sylvester-155]: The Sylvester criterion says that a symmetric bilinear form $(\ ,\ )$ on $\mathbb R^N$ is positive definite if and only if for any $k\le N$, $\det_{1\le i,j\le k}(e_i,e_j)>0$.

[^labels-155]: Please ignore the numerical labels; they will be relevant for Problem 6.1.6 below.
