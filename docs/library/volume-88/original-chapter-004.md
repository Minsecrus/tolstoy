---
title: "Representations of finite groups: Basic results"
description: "《Introduction to Representation Theory》English。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"General results of representation theory","link":"/library/volume-88/original-chapter-003"}
next: {"text":"Representations of finite groups: Further results","link":"/library/volume-88/original-chapter-005"}
---

# Representations of finite groups: Basic results

<span class="original-page-anchor" id="pdf-page-67" aria-hidden="true"></span>

Recall that a **representation** of a group $G$ over a field $k$ is a $k$-vector space $V$ together with a group homomorphism $\rho:G\to GL(V)$. As we have explained above, a representation of a group $G$ over $k$ is the same thing as a representation of its group algebra $k[G]$.

In this section, we begin a systematic development of representation theory of finite groups.

## 4.1. Maschke’s theorem

**Theorem 4.1.1 (Maschke).** Let $G$ be a finite group and let $k$ be a field whose characteristic does not divide $|G|$. Then:

(i) The algebra $k[G]$ is semisimple.

(ii) There is an isomorphism of algebras $\psi:k[G]\to\bigoplus_i\operatorname{End}V_i$ defined by $g\mapsto\bigoplus_i g|_{V_i}$, where $V_i$ are the irreducible representations of $G$. In particular, this is an isomorphism of representations of $G$ (where $G$ acts on both sides by left multiplication). Hence, the regular representation $k[G]$ decomposes into irreducibles as $\bigoplus_i\dim(V_i)V_i$, and one has the “sum of squares formula”

$$
|G|=\sum_i\dim(V_i)^2.
$$

<span class="original-page-anchor" id="pdf-page-68" aria-hidden="true"></span>

**Proof.** By Proposition 3.5.8, (i) implies (ii), and to prove (i), it is sufficient to show that if $V$ is a finite dimensional representation of $G$ and $W\subset V$ is any subrepresentation, then there exists a subrepresentation $W'\subset V$ such that $V=W\oplus W'$ as representations.

Choose any complement $\widehat{W}$ of $W$ in $V$. (Thus $V=W\oplus\widehat{W}$ as vector spaces, but not necessarily as representations.) Let $P$ be the projection along $\widehat{W}$ onto $W$, i.e., the operator on $V$ defined by $P|_W=\operatorname{Id}$ and $P|_{\widehat{W}}=0$. Let

$$
\overline{P}:=\frac{1}{|G|}\sum_{g\in G}\rho(g)P\rho(g^{-1}),
$$

where $\rho(g)$ is the action of $g$ on $V$, and let

$$
W'=\ker\overline{P}.
$$

Now $\overline{P}|_W=\operatorname{Id}$ and $\overline{P}(V)\subseteq W$, so $\overline{P}^2=\overline{P}$, and so $\overline{P}$ is a projection along $W'$. Thus, $V=W\oplus W'$ as vector spaces.

Moreover, for any $h\in G$ and any $y\in W'$,

$$
\begin{aligned}
\overline{P}\rho(h)y&=\frac{1}{|G|}\sum_{g\in G}\rho(g)P\rho(g^{-1}h)y\\
&=\frac{1}{|G|}\sum_{\ell\in G}\rho(h\ell)P\rho(\ell^{-1})y=\rho(h)\overline{P}y=0,
\end{aligned}
$$

so $\rho(h)y\in\ker\overline{P}=W'$. Thus, $W'$ is invariant under the action of $G$ and is therefore a subrepresentation of $V$. Thus, $V=W\oplus W'$ is the desired decomposition into subrepresentations. $\square$

The converse to Theorem 4.1.1(i) also holds.

**Proposition 4.1.2.** If $k[G]$ is semisimple, then the characteristic of $k$ does not divide $|G|$.

**Proof.** Write $k[G]=\bigoplus_{i=1}^r\operatorname{End}V_i$, where the $V_i$ are irreducible representations and $V_1=k$ is the trivial $1$-dimensional representation. Then

$$
k[G]=k\oplus\bigoplus_{i=2}^r\operatorname{End}V_i=k\oplus\bigoplus_{i=2}^r d_iV_i,
$$

<span class="original-page-anchor" id="pdf-page-69" aria-hidden="true"></span>

where $d_i=\dim V_i$. By Schur's lemma,

$$
\operatorname{Hom}_{k[G]}(k,k[G])=k\Lambda,
\qquad \operatorname{Hom}_{k[G]}(k[G],k)=k\epsilon,
$$

for nonzero homomorphisms of representations $\epsilon:k[G]\to k$ and $\Lambda:k\to k[G]$ unique up to scaling. We can take $\epsilon$ such that $\epsilon(g)=1$ for all $g\in G$, and we can take $\Lambda$ such that $\Lambda(1)=\sum_{g\in G}g$. Then

$$
\epsilon\circ\Lambda(1)=\epsilon\left(\sum_{g\in G}g\right)=\sum_{g\in G}1=|G|.
$$

If $|G|=0$, then $\Lambda$ has no left inverse, as $(a\epsilon)\circ\Lambda(1)=0$ for any $a\in k$. This is a contradiction. $\square$

**Example 4.1.3.** If $G=\mathbb Z/p\mathbb Z$ and $k$ has characteristic $p$, then every irreducible representation of $G$ over $k$ is trivial (so $k[\mathbb Z/p\mathbb Z]$ indeed is not semisimple). Indeed, an irreducible representation of this group is a 1-dimensional space on which the generator acts by a $p$th root of unity. But every $p$th root of unity in $k$ equals $1$, as $x^p-1=(x-1)^p$ over $k$.

**Problem 4.1.4.** Let $G$ be a group of order $p^n$. Show that every irreducible representation of $G$ over a field $k$ of characteristic $p$ is trivial.

## 4.2 Characters

If $V$ is a finite dimensional representation of a finite group $G$, then its character $\chi_V:G\to k$ is defined by the formula $\chi_V(g)=\operatorname{Tr}|_V(\rho(g))$.

Obviously, $\chi_V(g)$ is simply the restriction of the character $\chi_V(a)$ of $V$ as a representation of the algebra $A=k[G]$ to the basis $G\subset A$, so it carries exactly the same information. The character is a **central function**, or **class function**: $\chi_V(g)$ depends only on the conjugacy class of $g$; i.e., $\chi_V(hgh^{-1})=\chi_V(g)$.

Denote by $F(G,k)$ the space of $k$-valued functions on $G$ and by $F_c(G,k)\subset F(G,k)$ the subspace of class functions.

**Theorem 4.2.1.** *If the characteristic of $k$ does not divide $|G|$, characters of irreducible representations of $G$ form a basis in the space $F_c(G,k)$.*

<span class="original-page-anchor" id="pdf-page-70" aria-hidden="true"></span>

**Proof.** By the Maschke theorem, $k[G]$ is semisimple, so by Theorem 3.6.2, the characters are linearly independent and are a basis of $(A/[A,A])^*$, where $A=k[G]$. It suffices to note that, as vector spaces over $k$,

$$
\begin{aligned}
(A/[A,A])^*&\cong\{\varphi\in\operatorname{Hom}_k(k[G],k)\mid gh-hg\in\ker\varphi\ \forall g,h\in G\}\\
&\cong\{f\in F(G,k)\mid f(gh)=f(hg)\ \forall g,h\in G\},
\end{aligned}
$$

which is precisely $F_c(G,k)$. $\square$

**Corollary 4.2.2.** *The number of isomorphism classes of irreducible representations of $G$ equals the number of conjugacy classes of $G$ (if $|G|\ne0$ in $k$).*

**Exercise 4.2.3.** Show that if $|G|=0$ in $k$, then the number of isomorphism classes of irreducible representations of $G$ over $k$ is strictly less than the number of conjugacy classes in $G$.

Hint: Let $P=\sum_{g\in G}g\in k[G]$. Then $P^2=0$. So $P$ has zero trace in every finite dimensional representation of $G$ over $k$.

**Corollary 4.2.4.** *Any representation of $G$ is determined by its character if $k$ has characteristic $0$; namely, $\chi_V=\chi_W$ implies $V\cong W$.*

## 4.3 Examples

The following are examples of representations of finite groups over $\mathbb C$.

(1) Finite abelian groups $G=\mathbb Z_{n_1}\times\cdots\times\mathbb Z_{n_k}$. Let $G^\vee$ be the set of irreducible representations of $G$. Every element of $G$ forms a conjugacy class, so $|G^\vee|=|G|$. Recall that all irreducible representations over $\mathbb C$ (and algebraically closed fields in general) of commutative algebras and groups are 1-dimensional. Thus, $G^\vee$ is an abelian group: if $\rho_1,\rho_2:G\to\mathbb C^\times$ are irreducible representations, then so are the representations $\rho_1(g)\rho_2(g)$ and $\rho_1(g)^{-1}$. The group $G^\vee$ is called the **dual group** or **character group** of $G$.

For given $n\ge1$, define $\rho:\mathbb Z_n\to\mathbb C^\times$ by $\rho(m)=e^{2\pi im/n}$. Then $\mathbb Z_n^\vee=\{\rho^k:k=0,\ldots,n-1\}$, so $\mathbb Z_n^\vee\cong\mathbb Z_n$. In general,

$$
(G_1\times G_2\times\cdots\times G_n)^\vee=G_1^\vee\times G_2^\vee\times\cdots\times G_n^\vee,
$$

so $G^\vee\cong G$ for any finite abelian group $G$. This isomorphism is, however, noncanonical: the particular decomposition of $G$ as <span class="original-page-anchor" id="pdf-page-71" aria-hidden="true"></span>$\mathbb Z_{n_1}\times\cdots\times\mathbb Z_{n_k}$ is not unique as far as which elements of $G$ correspond to $\mathbb Z_{n_1}$, etc., is concerned. On the other hand, $G\cong(G^\vee)^\vee$ is a canonical isomorphism, given by $\varphi:G\to(G^\vee)^\vee$, where $\varphi(g)(\chi)=\chi(g)$.

(2) The symmetric group $S_3$. In the symmetric group $S_n$, conjugacy classes are determined by cycle decomposition sizes: two permutations are conjugate if and only if they have the same number of cycles of each length. For $S_3$, there are three conjugacy classes, so there are three different irreducible representations over $\mathbb C$. If their dimensions are $d_1,d_2,d_3$, then $d_1^2+d_2^2+d_3^2=6$, so $S_3$ must have two 1-dimensional and one 2-dimensional representations. The 1-dimensional representations are the trivial representation $\mathbb C_+$ given by $\rho(\sigma)=1$ and the sign representation $\mathbb C_-$ given by $\rho(\sigma)=(-1)^\sigma$.

The 2-dimensional representation can be visualized as representing the symmetries of the equilateral triangle with vertices $1,2,3$ at the points $(\cos120^\circ,\sin120^\circ)$, $(\cos240^\circ,\sin240^\circ)$, $(1,0)$ of the coordinate plane, respectively. Thus, for example,

$$
\rho((12))=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
\rho((123))=\begin{pmatrix}\cos120^\circ&-\sin120^\circ\\\sin120^\circ&\cos120^\circ\end{pmatrix}.
$$

To show that this representation is irreducible, consider any subrepresentation $V$. The space $V$ must be the span of a subset of the eigenvectors of $\rho((12))$, which are the nonzero multiples of $(1,0)$ and $(0,1)$. Also, $V$ must be the span of a subset of the eigenvectors of $\rho((123))$, which are different vectors. Thus, $V$ must be either $\mathbb C^2$ or $0$.

(3) The quaternion group $Q_8=\{\pm1,\pm i,\pm j,\pm k\}$, with defining relations

$$
i=jk=-kj,\quad j=ki=-ik,\quad k=ij=-ji,\quad -1=i^2=j^2=k^2.
$$

The five conjugacy classes are $\{1\}$, $\{-1\}$, $\{\pm i\}$, $\{\pm j\}$, $\{\pm k\}$, so there are five different irreducible representations, the sum of the squares of whose dimensions is $8$, so their dimensions must be $1$, $1$, $1$, $1$, and $2$.

The center $Z(Q_8)$ is $\{\pm1\}$, and $Q_8/Z(Q_8)\cong\mathbb Z_2\times\mathbb Z_2$. The four 1-dimensional irreducible representations of $\mathbb Z_2\times\mathbb Z_2$ can be “pulled back” to $Q_8$. That is, if $q:Q_8\to Q_8/Z(Q_8)$ is the quotient map and <span class="original-page-anchor" id="pdf-page-72" aria-hidden="true"></span>$\rho$ is any representation of $Q_8/Z(Q_8)$, then $\rho\circ q$ gives a representation of $Q_8$.

The 2-dimensional representation is $V=\mathbb C^2$, given by $\rho(-1)=-\operatorname{Id}$ and

$$
\begin{aligned}
\rho(i)&=\begin{pmatrix}0&1\\-1&0\end{pmatrix},\\
\rho(j)&=\begin{pmatrix}\sqrt{-1}&0\\0&-\sqrt{-1}\end{pmatrix},\\
\rho(k)&=\begin{pmatrix}0&-\sqrt{-1}\\-\sqrt{-1}&0\end{pmatrix}.
\end{aligned}\tag{4.3.1}
$$

These are the Pauli matrices, which arise in quantum mechanics.

**Exercise 4.3.1.** Show that the 2-dimensional irreducible representation of $Q_8$ can be realized in the space of functions $f:Q_8\to\mathbb C$ such that $f(gi)=\sqrt{-1}f(g)$ (the action of $G$ is by right multiplication, $g\circ f(x)=f(xg)$).

(4) The symmetric group $S_4$. The order of $S_4$ is $24$, and there are five conjugacy classes: $e$, $(12)$, $(123)$, $(1234)$, $(12)(34)$. Thus the sum of the squares of the dimensions of five irreducible representations is $24$. As with $S_3$, there are two of dimension $1$: the trivial and sign representations, $\mathbb C_+$ and $\mathbb C_-$. The other three must then have dimensions $2$, $3$, and $3$. Because $S_3\cong S_4/\mathbb Z_2\times\mathbb Z_2$, where $\mathbb Z_2\times\mathbb Z_2$ is $\{e,(12)(34),(13)(24),(14)(23)\}$, the 2-dimensional representation of $S_3$ can be pulled back to the 2-dimensional representation of $S_4$, which we will call $\mathbb C^2$.

We can consider $S_4$ as the group of rotations of a cube acting by permuting the interior diagonals (or, equivalently, on a regular octahedron permuting pairs of opposite faces); this gives the 3-dimensional representation $\mathbb C_+^3$.

The last 3-dimensional representation is $\mathbb C_-^3$, the product of $\mathbb C_+^3$ with the sign representation. $\mathbb C_+^3$ and $\mathbb C_-^3$ are different, for if $g$ is a transposition, $\det g|_{\mathbb C_+^3}=1$ while $\det g|_{\mathbb C_-^3}=(-1)^3=-1$. Note that another realization of $\mathbb C_-^3$ is by action of $S_4$ by symmetries (not necessarily rotations) of the regular tetrahedron. Yet another realization of this representation is the space of functions on the set of <span class="original-page-anchor" id="pdf-page-73" aria-hidden="true"></span>four elements (on which $S_4$ acts by permutations) with zero sum of values.

## 4.4 Duals and tensor products of representations

If $V$ is a representation of a group $G$, then $V^*$ is also a representation, via

$$
\rho_{V^*}(g)=(\rho_V(g)^*)^{-1}=(\rho_V(g)^{-1})^*=\rho_V(g^{-1})^*.
$$

The character is $\chi_{V^*}(g)=\chi_V(g^{-1})$.

We have $\chi_V(g)=\sum\lambda_i$, where the $\lambda_i$ are the eigenvalues of $g$ in $V$. These eigenvalues must be roots of unity because $\rho(g)^{|G|}=\rho(g^{|G|})=\rho(e)=\operatorname{Id}$. Thus for complex representations

$$
\chi_{V^*}(g)=\chi_V(g^{-1})=\sum\lambda_i^{-1}=\sum\overline{\lambda_i}=\overline{\sum\lambda_i}=\overline{\chi_V(g)}.
$$

In particular, $V\cong V^*$ *as representations* (not just as vector spaces) if and only if $\chi_V(g)\in\mathbb R$ for all $g\in G$.

If $V,W$ are representations of $G$, then $V\otimes W$ is also a representation, via

$$
\rho_{V\otimes W}(g)=\rho_V(g)\otimes\rho_W(g).
$$

Therefore, $\chi_{V\otimes W}(g)=\chi_V(g)\chi_W(g)$.

An interesting problem discussed below is decomposing $V\otimes W$ (for irreducible $V,W$) into the direct sum of irreducible representations.

## 4.5 Orthogonality of characters

We define a positive definite Hermitian inner product on $F_c(G,\mathbb C)$ (the space of central functions) by

$$
(f_1,f_2)=\frac1{|G|}\sum_{g\in G}f_1(g)\overline{f_2(g)}.
$$

The following theorem says that characters of irreducible representations of $G$ form an orthonormal basis of $F_c(G,\mathbb C)$ under this inner product.

<span class="original-page-anchor" id="pdf-page-74" aria-hidden="true"></span>

**Theorem 4.5.1.** *For any representations $V,W$*

$$
(\chi_V,\chi_W)=\dim\operatorname{Hom}_G(W,V),
$$

*and*

$$
(\chi_V,\chi_W)=\begin{cases}1,&\text{if }V\cong W,\\0,&\text{if }V\not\cong W\end{cases}
$$

*if $V,W$ are irreducible.*

**Proof.** By the definition

$$
\begin{aligned}
(\chi_V,\chi_W)&=\frac1{|G|}\sum_{g\in G}\chi_V(g)\overline{\chi_W(g)}=\frac1{|G|}\sum_{g\in G}\chi_V(g)\chi_{W^*}(g)\\
&=\frac1{|G|}\sum_{g\in G}\chi_{V\otimes W^*}(g)=\operatorname{Tr}|_{V\otimes W^*}(P),
\end{aligned}
$$

where $P=\frac1{|G|}\sum_{g\in G}g\in Z(\mathbb C[G])$. (Here $Z(\mathbb C[G])$ denotes the center of $\mathbb C[G]$.) If $X$ is an irreducible representation of $G$, then

$$
P|_X=\begin{cases}\operatorname{Id},&\text{if }X=\mathbb C,\\0,&X\ne\mathbb C.\end{cases}
$$

Therefore, for any representation $X$ the operator $P|_X$ is the $G$-invariant projector onto the subspace $X^G$ of $G$-invariants in $X$. Thus,

$$
\begin{aligned}
\operatorname{Tr}|_{V\otimes W^*}(P)&=\dim\operatorname{Hom}_G(\mathbb C,V\otimes W^*)\\
&=\dim(V\otimes W^*)^G=\dim\operatorname{Hom}_G(W,V).
\end{aligned}
$$

$\square$

Theorem 4.5.1 gives a powerful method of checking if a given complex representation $V$ of a finite group $G$ is irreducible. Indeed, it implies that $V$ is irreducible if and only if $(\chi_V,\chi_V)=1$.

**Problem 4.5.2.** Let $G$ be a finite group. Let $V_i$ be the irreducible complex representations of $G$.

For every $i$, let

$$
\psi_i=\frac{\dim V_i}{|G|}\sum_{g\in G}\chi_{V_i}(g)\cdot g^{-1}\in\mathbb C[G].
$$

<span class="original-page-anchor" id="pdf-page-75" aria-hidden="true"></span>

(i) Prove that $\psi_i$ acts on $V_j$ as the identity if $j=i$, and as the null map if $j\ne i$.

(ii) Prove that $\psi_i$ are **idempotents**; i.e., $\psi_i^2=\psi_i$ for any $i$, and $\psi_i\psi_j=0$ for any $i\ne j$.

Hint: In (i), notice that $\psi_i$ commutes with any element of $k[G]$ and thus acts on $V_j$ as an intertwining operator. Corollary 2.3.10 thus yields that $\psi_i$ acts on $V_j$ as a scalar. Compute this scalar by taking its trace in $V_j$.

**Remark 4.5.3.** We see that characters of irreducible complex representations of $G$ can be defined without mentioning irreducible representations. Namely, equip the space $F(G,\mathbb C)$ of complex-valued functions on $G$ with the convolution product

$$
(f*g)(z)=\sum_{x,y\in G:xy=z}f(x)g(y).
$$

This product turns $F(G,\mathbb C)$ into an associative algebra, with unit $\delta_e$ (the characteristic function of the unit $e\in G$), and the space of class functions $F_c(G,\mathbb C)$ is a commutative subalgebra. Then one can define renormalized characters $\widetilde\chi_i\in F_c(G,\mathbb C)$ to be the primitive idempotents in this algebra, i.e., solutions of the equation $f*f=f$ which cannot be decomposed into a sum of other nonzero solutions. Then one can define the characters by the formula

$$
\chi_i(g)=\sqrt{\frac{|G|}{\widetilde\chi_i(1)}}\widetilde\chi_i(g)
$$

(check it!). This is, essentially, how Frobenius defined characters (see [Cu], equation (7)). Note that Frobenius defined representations at approximately the same time, but for some time it was not clear that there is a simple relation between irreducible representations and characters (namely, that irreducible characters are simply traces of group elements in irreducible representations). Even today, many group theorists sometimes talk of irreducible characters of a finite group rather than irreducible representations.

Here is another “orthogonality formula” for characters, in which summation is taken over irreducible representations rather than group elements.

<span class="original-page-anchor" id="pdf-page-76" aria-hidden="true"></span>

**Theorem 4.5.4.** *Let $g,h\in G$, and let $Z_g$ denote the centralizer of $g$ in $G$. Then*

$$
\sum_V\chi_V(g)\overline{\chi_V(h)}=\begin{cases}|Z_g|,&\text{if }g\text{ is conjugate to }h,\\0,&\text{otherwise},\end{cases}
$$

*where the summation is taken over all irreducible representations of $G$.*

**Proof.** As noted above, $\overline{\chi_V(h)}=\chi_{V^*}(h)$, so the left-hand side equals (using Maschke's theorem):

$$
\begin{aligned}
\sum_V\chi_V(g)\chi_{V^*}(h)&=\operatorname{Tr}|_{\bigoplus_V V\otimes V^*}(g\otimes(h^*)^{-1})\\
&=\operatorname{Tr}|_{\bigoplus_V\operatorname{End}V}(x\mapsto gxh^{-1})=\operatorname{Tr}|_{\mathbb C[G]}(x\mapsto gxh^{-1}).
\end{aligned}
$$

If $g$ and $h$ are not conjugate, this trace is clearly zero, since the matrix of the operator $x\mapsto gxh^{-1}$ in the basis of group elements has zero diagonal entries. On the other hand, if $g$ and $h$ are in the same conjugacy class, the trace is equal to the number of elements $x$ such that $x=gxh^{-1}$, i.e., the order of the centralizer $Z_g$ of $g$. We are done. $\square$

**Remark 4.5.5.** Another proof of this result is as follows. Consider the matrix $U$ whose rows are labeled by irreducible representations of $G$ and whose columns are labeled by conjugacy classes, with entries $U_{V,g}=\chi_V(g)/\sqrt{|Z_g|}$. Note that the conjugacy class of $g$ is $G/Z_g$; thus $|G|/|Z_g|$ is the number of elements conjugate to $G$. Thus, by Theorem 4.5.1, the rows of the matrix $U$ are orthonormal. This means that $U$ is unitary and hence its columns are also orthonormal, which implies the statement.

## 4.6 Unitary representations. Another proof of Maschke's theorem for complex representations

**Definition 4.6.1.** A **unitary finite dimensional representation** of a group $G$ is a representation of $G$ on a complex finite dimensional vector space $V$ over $\mathbb C$ equipped with a $G$-invariant positive definite <span class="original-page-anchor" id="pdf-page-77" aria-hidden="true"></span>Hermitian form[^4-6-1] $(\ ,\ )$, i.e., such that $\rho_V(g)$ are unitary operators: $(\rho_V(g)v,\rho_V(g)w)=(v,w)$.

**Theorem 4.6.2.** *If $G$ is finite, then any finite dimensional representation of $G$ has a unitary structure. If the representation is irreducible, this structure is unique up to scaling by a positive real number.*

**Proof.** Take any positive definite form $B$ on $V$ and define another form $\overline B$ as follows:

$$
\overline B(v,w)=\sum_{g\in G}B(\rho_V(g)v,\rho_V(g)w).
$$

Then $\overline B$ is a positive definite Hermitian form on $V$, and $\rho_V(g)$ are unitary operators. If $V$ is an irreducible representation and $B_1,B_2$ are two positive definite Hermitian forms on $V$, then $B_1(v,w)=B_2(Av,w)$ for some homomorphism $A:V\to V$ (since any positive definite Hermitian form is nondegenerate). By Schur's lemma, $A=\lambda\operatorname{Id}$, and clearly $\lambda>0$. $\square$

Theorem 4.6.2 implies that if $V$ is a finite dimensional representation of a finite group $G$, then the **complex conjugate representation** $\overline V$ (i.e., the same space $V$ with the same addition and the same action of $G$, but complex conjugate action of scalars) is isomorphic to the dual representation $V^*$. Indeed, a homomorphism of representations $\overline V\to V^*$ is obviously the same thing as an invariant sesquilinear form on $V$ (i.e., a form additive on both arguments which is linear on the first one and antilinear on the second one), and an isomorphism is the same thing as a nondegenerate invariant sesquilinear form. So one can use a unitary structure on $V$ to define an isomorphism $\overline V\to V^*$.

**Theorem 4.6.3.** *A finite dimensional unitary representation $V$ of any group $G$ is completely reducible.*

**Proof.** Let $W$ be a subrepresentation of $V$. Let $W^\perp$ be the orthogonal complement of $W$ in $V$ under the Hermitian inner product. Then $W^\perp$ is a subrepresentation of $W$, and $V=W\oplus W^\perp$. This implies that $V$ is completely reducible. $\square$ <span class="original-page-anchor" id="pdf-page-78" aria-hidden="true"></span>Theorems 4.6.2 and 4.6.3 imply Maschke's theorem for complex representations (Theorem 4.1.1). Thus, we have obtained a new proof of this theorem over the field of complex numbers.

**Remark 4.6.4.** Theorem 4.6.3 shows that for infinite groups $G$, a finite dimensional representation may fail to admit a unitary structure (as there exist finite dimensional representations, e.g., for $G=\mathbb Z$, which are indecomposable but not irreducible).

## 4.7 Orthogonality of matrix elements

Let $V$ be an irreducible representation of a finite group $G$, and let $v_1,v_2,\ldots,v_n$ be an orthonormal basis of $V$ under the invariant Hermitian form. The matrix elements of $V$ are $t_{ij}^V(x)=(\rho_V(x)v_i,v_j)$.

**Proposition 4.7.1.** *(i) Matrix elements of nonisomorphic irreducible representations are orthogonal in $F(G,\mathbb C)$ under the form $(f,g)=\frac1{|G|}\sum_{x\in G}f(x)\overline{g(x)}$.*

*(ii) One has $(t_{ij}^V,t_{i'j'}^V)=\delta_{ii'}\delta_{jj'}\cdot\frac1{\dim V}$.*

*Thus, matrix elements of irreducible representations of $G$ form an orthogonal basis of $F(G,\mathbb C)$.*

**Proof.** Let $V$ and $W$ be two irreducible representations of $G$. Take $\{v_i\}$ to be an orthonormal basis of $V$ and $\{w_i\}$ to be an orthonormal basis of $W$ under their positive definite invariant Hermitian forms. Let $w_i^*\in W^*$ be the linear function on $W$ defined by taking the inner product with $w_i$: $w_i^*(u)=(u,w_i)$. Then for $x\in G$ we have $(xw_i^*,w_j^*)=\overline{(xw_i,w_j)}$. Therefore, putting $P=\frac1{|G|}\sum_{x\in G}x$, we have

$$
\begin{aligned}
(t_{ij}^V,t_{i'j'}^W)&=|G|^{-1}\sum_{x\in G}(xv_i,v_j)\overline{(xw_{i'},w_{j'})}\\
&=|G|^{-1}\sum_{x\in G}(xv_i,v_j)(xw_{i'}^*,w_{j'}^*)=(P(v_i\otimes w_{i'}^*),v_j\otimes w_{j'}^*).
\end{aligned}
$$

If $V\ne W$, this is zero, since $P$ projects to the trivial representation, which does not occur in $V\otimes W^*$. If $V=W$, we need to consider <span class="original-page-anchor" id="pdf-page-79" aria-hidden="true"></span>$(P(v_i\otimes v_{i'}^*),v_j\otimes v_{j'}^*)$. We have a $G$-invariant decomposition

$$
\begin{aligned}
V\otimes V^*&=\mathbb C\oplus L,\\
\mathbb C&=\operatorname{span}\left(\sum v_k\otimes v_k^*\right),\\
L&=\operatorname{span}_{a:\sum_k a_{kk}=0}\left(\sum_{k,l}a_{kl}v_k\otimes v_l^*\right),
\end{aligned}
$$

and $P$ projects to the first summand along the second one. The projection of $v_i\otimes v_{i'}^*$ to $\mathbb C\subset\mathbb C\oplus L$ is thus

$$
\frac{\delta_{ii'}}{\dim V}\sum v_k\otimes v_k^*.
$$

This shows that

$$
(P(v_i\otimes v_{i'}^*),v_j\otimes v_{j'}^*)=\frac{\delta_{ii'}\delta_{jj'}}{\dim V},
$$

which finishes the proof of (i) and (ii). The last statement follows immediately from the sum of squares formula. $\square$

## 4.8 Character tables, examples

The characters of all the irreducible representations of a finite group can be arranged into a **character table**, with conjugacy classes of elements as the columns and characters as the rows. More specifically, the first row in a character table lists representatives of conjugacy classes, the second one lists the numbers of elements in the conjugacy classes, and the other rows list the values of the characters on the conjugacy classes. Due to Theorems 4.5.1 and 4.5.4, the rows and columns of a character table are orthonormal with respect to the appropriate inner products.

Note that in any character table, the row corresponding to the trivial representation consists of ones, and the column corresponding to the neutral element consists of the dimensions of the representations.

Here is, for example, the character table of $S_3$:

<span class="original-page-anchor" id="pdf-page-80" aria-hidden="true"></span>

$$
\begin{array}{c|c|c|c}
S_3&\operatorname{Id}&(12)&(123)\\\hline
\#&1&3&2\\\hline
\mathbb C_+&1&1&1\\\hline
\mathbb C_-&1&-1&1\\\hline
\mathbb C^2&2&0&-1
\end{array}
$$

It is obtained by explicitly computing traces in the irreducible representations.

For another example consider $A_4$, the group of even permutations of four items. There are three 1-dimensional representations (as $A_4$ has a normal subgroup $\mathbb Z_2\oplus\mathbb Z_2$ and $A_4/(\mathbb Z_2\oplus\mathbb Z_2)=\mathbb Z_3$). Since there are four conjugacy classes in total, there is one more irreducible representation of dimension $3$. Finally, the character table is

$$
\begin{array}{c|c|c|c|c}
A_4&\operatorname{Id}&(123)&(132)&(12)(34)\\\hline
\#&1&4&4&3\\\hline
\mathbb C&1&1&1&1\\\hline
\mathbb C_\epsilon&1&\epsilon&\epsilon^2&1\\\hline
\mathbb C_{\epsilon^2}&1&\epsilon^2&\epsilon&1\\\hline
\mathbb C^3&3&0&0&-1
\end{array}
$$

where $\epsilon=\exp(\frac{2\pi i}3)$.

The last row can be computed using the orthogonality of rows. Another way to compute the last row is to note that $\mathbb C^3$ is the representation of $A_4$ by rotations of the regular tetrahedron: in this case $(123),(132)$ are the rotations by $120^\circ$ and $240^\circ$ around a perpendicular to a face of the tetrahedron, while $(12)(34)$ is the rotation by $180^\circ$ around an axis perpendicular to two opposite edges.

**Example 4.8.1.** The following three character tables are of $Q_8$, $S_4$, and $A_5$, respectively:

$$
\begin{array}{c|c|c|c|c|c}
Q_8&1&-1&i&j&k\\\hline
\#&1&1&2&2&2\\\hline
\mathbb C_{++}&1&1&1&1&1\\\hline
\mathbb C_{+-}&1&1&1&-1&-1\\\hline
\mathbb C_{-+}&1&1&-1&1&-1\\\hline
\mathbb C_{--}&1&1&-1&-1&1\\\hline
\mathbb C^2&2&-2&0&0&0
\end{array}
$$

<span class="original-page-anchor" id="pdf-page-81" aria-hidden="true"></span>

$$
\begin{array}{c|c|c|c|c|c}
S_4&\operatorname{Id}&(12)&(12)(34)&(123)&(1234)\\\hline
\#&1&6&3&8&6\\\hline
\mathbb C_+&1&1&1&1&1\\\hline
\mathbb C_-&1&-1&1&1&-1\\\hline
\mathbb C^2&2&0&2&-1&0\\\hline
\mathbb C_+^3&3&-1&-1&0&1\\\hline
\mathbb C_-^3&3&1&-1&0&-1
\end{array}
$$

$$
\begin{array}{c|c|c|c|c|c}
A_5&\operatorname{Id}&(123)&(12)(34)&(12345)&(13245)\\\hline
\#&1&20&15&12&12\\\hline
\mathbb C&1&1&1&1&1\\\hline
\mathbb C_+^3&3&0&-1&\frac{1+\sqrt5}2&\frac{1-\sqrt5}2\\\hline
\mathbb C_-^3&3&0&-1&\frac{1-\sqrt5}2&\frac{1+\sqrt5}2\\\hline
\mathbb C^4&4&1&0&-1&-1\\\hline
\mathbb C^5&5&-1&1&0&0
\end{array}
$$

Indeed, the computation of the characters of the 1-dimensional representations is straightforward.

The character of the 2-dimensional representation of $Q_8$ is obtained from the explicit formula (4.3.1) for this representation, or by using orthogonality.

For $S_4$, the 2-dimensional irreducible representation is obtained from the 2-dimensional irreducible representation of $S_3$ via the surjective homomorphism $S_4\to S_3$, which allows one to obtain its character from the character table of $S_3$.

The character of the 3-dimensional representation $\mathbb C_+^3$ is computed from its geometric realization by rotations of the cube. Namely, by rotating the cube, $S_4$ permutes the main diagonals. Thus $(12)$ is the rotation by $180^\circ$ around an axis that is perpendicular to two opposite edges, $(12)(34)$ is the rotation by $180^\circ$ around an axis that is perpendicular to two opposite faces, $(123)$ is the rotation around a main diagonal by $120^\circ$, and $(1234)$ is the rotation by $90^\circ$ around an axis that is perpendicular to two opposite faces; this allows us to compute the traces easily, using the fact that the trace of a rotation by the angle $\varphi$ in $\mathbb R^3$ is $1+2\cos\varphi$. Now the character of $\mathbb C_-^3$ is found by multiplying the character of $\mathbb C_+^3$ by the character of the sign representation.

<span class="original-page-anchor" id="pdf-page-82" aria-hidden="true"></span>

Finally, we explain how to obtain the character table of $A_5$ (even permutations of five items). The group $A_5$ is the group of rotations of the regular icosahedron. Thus it has a 3-dimensional “rotation representation” $\mathbb C_+^3$, in which $(12)(34)$ is the rotation by $180^\circ$ around an axis perpendicular to two opposite edges, $(123)$ is the rotation by $120^\circ$ around an axis perpendicular to two opposite faces, and $(12345),(13254)$ are the rotations by $72^\circ$, respectively $144^\circ$, around axes going through two opposite vertices. The character of this representation is computed from this description in a straightforward way.

Another representation of $A_5$, which is also 3-dimensional, is $\mathbb C_+^3$ twisted by the automorphism of $A_5$ given by conjugation by $(12)$ inside $S_5$. This representation is denoted by $\mathbb C_-^3$. It has the same character as $\mathbb C_+^3$, except that the conjugacy classes $(12345)$ and $(13245)$ are interchanged.

There are two remaining irreducible representations, and by the sum of squares formula their dimensions are $4$ and $5$. So we call them $\mathbb C^4$ and $\mathbb C^5$.

The representation $\mathbb C^4$ is realized on the space of functions on the set $\{1,2,3,4,5\}$ with zero sum of values, where $A_5$ acts by permutations (check that it is irreducible!). The character of this representation is equal to the character of the 5-dimensional permutation representation minus the character of the 1-dimensional trivial representation (constant functions). The former at an element $g$ is equal to the number of items among $1,2,3,4,5$ which are fixed by $g$.

The representation $\mathbb C^5$ is realized on the space of functions on pairs of opposite vertices of the icosahedron which has zero sum of values (check that it is irreducible!). The character of this representation is computed similarly to the character of $\mathbb C^4$, or from the orthogonality formula.

## 4.9 Computing tensor product multiplicities using character tables

Character tables allow us to compute the tensor product multiplicities $N_{ij}^k$ using

$$
V_i\otimes V_j=\sum N_{ij}^kV_k,\qquad N_{ij}^k=(\chi_i\chi_j,\chi_k).
$$

<span class="original-page-anchor" id="pdf-page-83" aria-hidden="true"></span>

**Example 4.9.1.** The following tables represent computed tensor product multiplicities of irreducible representations of $S_3$, $S_4$, and $A_5$, respectively:


$$
\begin{array}{c|c|c|c}
S_3&\mathbb C_+&\mathbb C_-&\mathbb C^2\\\hline
\mathbb C_+&\mathbb C_+&\mathbb C_-&\mathbb C^2\\\hline
\mathbb C_-&&\mathbb C_+&\mathbb C^2\\\hline
\mathbb C^2&&&\mathbb C_+\oplus\mathbb C_-\oplus\mathbb C^2
\end{array}
$$

$$
\small\begin{array}{c|c|c|c|c|c}
S_4&\mathbb C_+&\mathbb C_-&\mathbb C^2&\mathbb C_+^3&\mathbb C_-^3\\\hline
\mathbb C_+&\mathbb C_+&\mathbb C_-&\mathbb C^2&\mathbb C_+^3&\mathbb C_-^3\\\hline
\mathbb C_-&&\mathbb C_+&\mathbb C^2&\mathbb C_-^3&\mathbb C_+^3\\\hline
\mathbb C^2&&&\mathbb C_+\oplus\mathbb C_-\oplus\mathbb C^2&\mathbb C_+^3\oplus\mathbb C_-^3&\mathbb C_+^3\oplus\mathbb C_-^3\\\hline
\mathbb C_+^3&&&&\mathbb C_+\oplus\mathbb C^2\oplus\mathbb C_+^3\oplus\mathbb C_-^3&\mathbb C_-\oplus\mathbb C^2\oplus\mathbb C_+^3\oplus\mathbb C_-^3\\\hline
\mathbb C_-^3&&&&&\mathbb C_+\oplus\mathbb C^2\oplus\mathbb C_+^3\oplus\mathbb C_-^3
\end{array}
$$

$$
\small\begin{array}{c|c|c|c|c|c}
A_5&\mathbb C&\mathbb C_+^3&\mathbb C_-^3&\mathbb C^4&\mathbb C^5\\\hline
\mathbb C&\mathbb C&\mathbb C_3^+&\mathbb C_-^3&\mathbb C^4&\mathbb C^5\\\hline
\mathbb C_+^3&&\mathbb C\oplus\mathbb C^5\oplus\mathbb C_+^3&\mathbb C^4\oplus\mathbb C^5&\mathbb C_-^3\oplus\mathbb C^4\oplus\mathbb C^5&\mathbb C_+^3\oplus\mathbb C_-^3\oplus\mathbb C^4\oplus\mathbb C^5\\\hline
\mathbb C_-^3&&&\mathbb C\oplus\mathbb C^5\oplus\mathbb C_+^3&\mathbb C_+^3\oplus\mathbb C^4\oplus\mathbb C^5&\mathbb C_+^3\oplus\mathbb C_-^3\oplus\mathbb C^4\oplus\mathbb C^5\\\hline
\mathbb C^4&&&&\substack{\mathbb C_+^3\oplus\mathbb C_-^3\oplus\mathbb C\\\oplus\mathbb C^4\oplus\mathbb C^5}&\mathbb C_+^3\oplus\mathbb C_-^3\oplus2\mathbb C^5\oplus\mathbb C^4\\\hline
\mathbb C^5&&&&&\substack{\mathbb C\oplus\mathbb C_+^3\oplus\mathbb C_-^3\\\oplus2\mathbb C^4\oplus2\mathbb C^5}
\end{array}
$$


## 4.10 Frobenius determinant

Enumerate the elements of a finite group $G$ as follows: $g_1,g_2,\ldots,g_n$. Introduce $n$ variables indexed with the elements of $G$:

$$
x_{g_1},x_{g_2},\ldots,x_{g_n}.
$$

**Definition 4.10.1.** Consider the matrix $X_G$ with entries $a_{ij}=x_{g_ig_j}$. The determinant of $X_G$ is some polynomial of degree $n$ of $x_{g_1},x_{g_2},\ldots,x_{g_n}$ that is called the **Frobenius determinant**, or **group determinant**.

<span class="original-page-anchor" id="pdf-page-84" aria-hidden="true"></span>

The following theorem, discovered by Dedekind and proved by Frobenius, became the starting point for creation of representation theory (see [Cu] and Section 4.11).

**Theorem 4.10.2.**

$$
\det X_G=\prod_{j=1}^r P_j(x)^{\deg P_j}
$$

*for some pairwise nonproportional irreducible polynomials $P_j(x)$, where $r$ is the number of conjugacy classes of $G$.*

We will need the following simple lemma.

**Lemma 4.10.3.** *Let $Y$ be an $n\times n$ matrix with entries $y_{ij}$. Then $\det Y$ is an irreducible polynomial of $\{y_{ij}\}$.*

**Proof.** Let $X=t\cdot\operatorname{Id}+\sum_{i=1}^n x_iE_{i,i+1}$, where $i+1$ is computed modulo $n$, and $E_{i,j}$ are the elementary matrices. Then $\det(X)=t^n-(-1)^nx_1\cdots x_n$, which is obviously irreducible. Hence $\det(Y)$ is irreducible (since it is so when $Y$ is specialized to $X$, and since irreducible factors of a homogeneous polynomial are homogeneous, so cannot specialize to nonzero constants). $\square$

Now we are ready to proceed to the proof of Theorem 4.10.2.

**Proof.** Let $V=\mathbb C[G]$ be the regular representation of $G$. Consider the operator-valued polynomial

$$
L(x)=\sum_{g\in G}x_g\rho(g),
$$

where $\rho(g)\in\operatorname{End}V$ is induced by $g$. The action of $L(x)$ on an element $h\in G$ is

$$
L(x)h=\sum_{g\in G}x_g\rho(g)h=\sum_{g\in G}x_ggh=\sum_{z\in G}x_{zh^{-1}}z.
$$

So the matrix of the linear operator $L(x)$ in the basis $g_1,g_2,\ldots,g_n$ is $X_G$ with permuted columns and hence has the same determinant up to sign.

<span class="original-page-anchor" id="pdf-page-85" aria-hidden="true"></span>

Further, by Maschke's theorem, we have

$$
\det_V L(x)=\prod_{i=1}^r(\det_{V_i}L(x))^{\dim V_i},
$$

where $V_i$ are the irreducible representations of $G$. We set $P_i=\det_{V_i}L(x)$. Let $\{e_{im}\}$ be bases of $V_i$ and let $E_{i,jk}\in\operatorname{End}V_i$ be the matrix units in these bases. Then $\{E_{i,jk}\}$ is a basis of $\mathbb C[G]$ and

$$
L(x)|_{V_i}=\sum_{j,k}y_{i,jk}E_{i,jk},
$$

where $y_{i,jk}$ are new coordinates on $\mathbb C[G]$ related to $x_g$ by a linear transformation. Then

$$
P_i(x)=\det_{V_i}L(x)=\det(y_{i,jk}).
$$

Hence, $P_i$ are irreducible (by Lemma 4.10.3) and not proportional to each other (as they depend on different collections of variables $y_{i,jk}$). The theorem is proved. $\square$

## 4.11 Historical interlude: Georg Frobenius's “Principle of Horse Trade”

Ferdinand Georg Frobenius (1849–1917) studied at the famous Berlin University under both Karl Weierstrass and Leopold Kronecker, two great mathematicians who later became bitter opponents. Weierstrass considered Frobenius one of his brightest doctoral students and greased the wheels of his career by securing him a full professorship at the Zürich Polytechnikum. In Zürich Frobenius quickly got married, but the joys of happy matrimony did not prevent him from continuing productive research. Frobenius earned a high reputation for his studies of elliptic and theta functions, determinant and matrix theory, and bilinear forms. Some fifteen years later, Kronecker's passing opened a vacant slot in Berlin, and Weierstrass got posthumous revenge on his old opponent by hiring his own student, Frobenius, for Kronecker's chair. In 1892 Frobenius left for Berlin, just four years before Einstein enrolled as a student in the Zürich Polytechnikum.

Praised by his colleagues as “a first-rate stylist”, who “writes clearly and understandably without ever attempting to delude the <span class="original-page-anchor" id="pdf-page-86" aria-hidden="true"></span>reader with empty phrases”, Frobenius was soon elected to the prestigious Prussian Academy of Sciences [11, p. 38]. At this point, Frobenius began reevaluating his research interests. As he explained in his inaugural speech, the “labyrinth of formulas” in the theory of theta functions was having “a withering effect upon the mathematical imagination”. He intended “to overcome this paralysis of the mathematical creative powers by time and again seeking renewal at the fountain of youth of arithmetic”, i.e., number theory (quoted in [24, p. 220]). In his 40s, Frobenius indeed found this “fountain of youth” in “arithmetic”, that is, in the theory of finite groups linked to the theory of numbers by Galois theory.

In 1896 Frobenius's comfortable life in Berlin was unceremoniously disrupted by several letters from Richard Dedekind, his old acquaintance and a predecessor at the Zürich Polytechnikum, now the dean of abstract algebra in Germany. After dealing with epistolary niceties and thanking Frobenius for brightening “the African darkness of the theory of groups”, Dedekind shared some of his recent results on group theory, including his concept of the group determinant and the statement of his theorem about its factorization for abelian groups. Since Dedekind had not bothered to publish his work on the topic, Frobenius had never even heard of the group determinant, but he quickly grasped this concept and never let it go again. In his reply, Frobenius mildly chastised Dedekind for keeping back these “extremely beautiful results from your friends and admirers”, and asked for more details. Dedekind then stumped his colleague with a “conjectured theorem” that the number of linear factors in the group determinant is equal to the index of the commutator subgroup and admitted, “I distinctly feel that I will not achieve anything here” (quoted in [24, pp. 223, 224]).

Dedekind's challenge was perfectly timed for the spring break, and Frobenius, having some free time on his hands, immediately took the bait. Employing military metaphors to describe his own work, he waged a war against the group determinant. He invented generalized group characters and assaulted Dedekind's conjecture with their help. Frobenius's initial results seemed unsatisfactory, and he reported them to Dedekind with a disclaimer that “my conclusions <span class="original-page-anchor" id="pdf-page-87" aria-hidden="true"></span>are so complicated that I myself do not rightly know where the main point of the proof is, and in fact I am still slightly mistrustful of it” (quoted in [24, pp. 225, 230]).

A few days later a jubilant Frobenius wrote to Dedekind that he finally saw the way to a solution. Citing his former colleague Friedrich Schottky, Frobenius now looked at his own earlier frustration as the harbinger of a forthcoming breakthrough: “If in an investigation, after difficult mental exertion, the feeling arises that nothing will be achieved on the matter in question, then one can rejoice for he is standing before the solution” (quoted in [24, p. 230]). Within ten days, Frobenius proved all the main theorems of the theory of group determinants, except for one most important result.

The missing theorem stated, in modern language, that an irreducible representation occurs in the regular representation as often as its degree and was called by Frobenius “the Fundamental Theorem of the theory of group determinants”. “It would be wonderful” if it were true, he wrote, “for then my theory would supply everything needful” for the determination of prime factors (quoted in [24, p. 235]). The proof took five months, during which Frobenius repeatedly used a new, effective technique, which he kept secret and shared privately only with Dedekind. The new method drew on the well-known bargaining strategy: “At the market, the desired horse is ignored as much as possible and at last is allowed to be formally recognized” (quoted in [24, p. 236]). In Frobenius's interpretation, in order to solve a mathematical problem, one had to preoccupy oneself with activities totally unrelated to mathematics. He applied this “Principle of the Horse Trade” widely, taking his wife to trade exhibits and art shows, reading fiction, and clearing his garden of caterpillars. Frobenius implored Dedekind to keep this ingenious method a secret, promising to disclose it in a posthumous volume, *On the Methods of Mathematical Research*, with an appendix on caterpillar catching [24, p. 237]. Unfortunately, this volume never came out, which was a huge setback for the science of caterpillar-catching.

Miraculously, taking a break from research, combined with a healthy dose of working desk disorder, did help Frobenius refresh his <span class="original-page-anchor" id="pdf-page-88" aria-hidden="true"></span>thoughts and find a new approach. After returning home from vacation, Frobenius failed to find his earlier proof of one particular case of the missing theorem among his “highly scattered and disorganized papers”. After “much torment”, however, he discovered a new proof and recognized the crucial possibility of generalization [24, p. 237].

The same year Frobenius announced his results to the world in a series of papers. This was a wise move, since most of his correspondence with Dedekind eventually ended up in the hands of an American lawyer, who kept it in his drawer for thirty odd years and parted with it only after his retirement by giving it to a mathematics professor in exchange for \$25 [27].

Wielding the group determinant as his main weapon, within a few years Frobenius demolished a whole range of targets in representation theory. Although his proofs have now been supplanted by easier modern versions, his skills as a group determinant virtuoso remain unsurpassed, as the tool itself went out of use.

Frobenius labored mightily to keep things at the University of Berlin just the way they were in the glorious days of his student youth, and he accused the advocates of applied mathematics of trying to reduce this venerable institution to the rank of a technical school. His personality, which has been described as “occasionally choleric, quarrelsome, and given to invectives” [21], alienated him from many of his colleagues. Despite (or maybe partly due to?) Frobenius's uncompromising stance, the numbers of doctorates and teaching staff at the University gradually declined. Frobenius advised nineteen doctoral students, and only one of them wrote a dissertation on representation theory. Training that one student, however, proved fortuitous, for that student was the brilliant mathematician Issai Schur, who kept the Frobenius tradition alive for decades to come.

In the meantime, Berlin was losing its reputation as the leading center of German mathematics to Göttingen. This did not endear Göttingen-style mathematics to Frobenius's heart, and he disaffectionately called it “a school, in which one amuses oneself more with rosy images than hard ideas” (quoted in [11, p. 47]). His aversion to the Göttingen patriarch Felix Klein and to Sophus Lie, according to one commentator, “knew no limits” (Biermann in [11, p. 47]).

<span class="original-page-anchor" id="pdf-page-89" aria-hidden="true"></span>

Despite Frobenius’s best efforts to keep the subject pure, representation theory has since been irretrievably polluted by applications in quantum physics and chemistry, crystallography, spectroscopy, and even virology. Worse still, thanks to the efforts of Hermann Weyl and Claude Chevalley, his beloved representation theory eventually merged with the theory of Lie groups. Frobenius thus was eventually reconciled with Lie, if only in the Platonic world of eternal mathematical objects.

## 4.12. Problems

**Problem 4.12.1.** Let $G$ be the group of symmetries of a regular $N$-gon (it has $2N$ elements).

(a) Describe all irreducible complex representations of this group (consider the cases of odd and even $N$).

(b) Let $V$ be the $2$-dimensional complex representation of $G$ obtained by complexification of the standard representation on the real plane (the plane of the polygon). Find the decomposition of $V\otimes V$ in a direct sum of irreducible representations.

**Problem 4.12.2.** Let $p$ be a prime. Let $G$ be the group of $3\times3$ matrices over $\mathbb F_p$ which are upper triangular and have $1$’s on the diagonal, under multiplication (its order is $p^3$). It is called the **Heisenberg group**. For any complex number $z$ such that $z^p=1$, we define a representation of $G$ on the space $V$ of complex functions on $\mathbb F_p$ by

$$
\left(\rho\begin{pmatrix}1&1&0\\0&1&0\\0&0&1\end{pmatrix}f\right)(x)=f(x-1),
$$

$$
\left(\rho\begin{pmatrix}1&0&0\\0&1&1\\0&0&1\end{pmatrix}f\right)(x)=z^x f(x)
$$

(note that $z^x$ makes sense since $z^p=1$).

(a) Show that such a representation exists and is unique, and compute $\rho(g)$ for all $g\in G$.

(b) Denote this representation by $R_z$. Show that $R_z$ is irreducible if and only if $z\ne1$.

<span class="original-page-anchor" id="pdf-page-90" aria-hidden="true"></span>

(c) Classify all $1$-dimensional representations of $G$. Show that $R_1$ decomposes into a direct sum of $1$-dimensional representations, where each of them occurs exactly once.

(d) Use (a)–(c) and the “sum of squares” formula to classify all irreducible representations of $G$.

**Problem 4.12.3.** Let $V$ be a finite dimensional complex vector space, and let $GL(V)$ be the group of invertible linear transformations of $V$. Then $S^mV$ and $\Lambda^mV$ ($m\le\dim(V)$) are representations of $GL(V)$ in a natural way. Show that they are irreducible representations.

Hint: Choose a basis $\{e_i\}$ in $V$. Find a diagonal element $H$ of $GL(V)$ such that $\rho(H)$ has distinct eigenvalues (where $\rho$ is one of the above representations). This shows that if $W$ is a subrepresentation, then it is spanned by a subset $S$ of a basis of eigenvectors of $\rho(H)$. Use the invariance of $W$ under the operators $\rho(1+E_{ij})$ (where $E_{ij}$ is defined by $E_{ij}e_k=\delta_{jk}e_i$) for all $i\ne j$ to show that if the subset $S$ is nonempty, it is necessarily the entire basis.

**Problem 4.12.4.** Recall that the adjacency matrix of a graph $\Gamma$ (without multiple edges) is the matrix in which the $ij$th entry is $1$ if the vertices $i$ and $j$ are connected with an edge, and zero otherwise. Let $\Gamma$ be a finite graph whose automorphism group is nonabelian. Show that the adjacency matrix of $\Gamma$ must have repeated eigenvalues.

**Problem 4.12.5.** Let $I$ be the set of vertices of a regular icosahedron ($|I|=12$). Let $F(I)$ be the space of complex functions on $I$. Recall that the group $G=A_5$ of even permutations of five items acts on the icosahedron, so we have a $12$-dimensional representation of $G$ on $F(I)$.

(a) Decompose this representation in a direct sum of irreducible representations (i.e., find the multiplicities of occurrence of all irreducible representations).

(b) Do the same for the representation of $G$ on the space of functions on the set of faces and the set of edges of the icosahedron.

**Problem 4.12.6.** Let $\mathbb F_q$ be a finite field with $q$ elements, and let $G$ be the group of nonconstant inhomogeneous linear transformations, <span class="original-page-anchor" id="pdf-page-91" aria-hidden="true"></span>$x\to ax+b$, over $\mathbb F_q$ (i.e., $a\in\mathbb F_q^\times$, $b\in\mathbb F_q$). Find all irreducible complex representations of $G$, and compute their characters. Compute the tensor products of irreducible representations.

Hint: Let $V$ be the representation of $G$ on the space of functions on $\mathbb F_q$ with sum of all values equal to zero. Show that $V$ is an irreducible representation of $G$.

**Problem 4.12.7.** Let $G=SU(2)$ (the group of unitary $2\times2$ matrices with determinant $1$), and let $V=\mathbb C^2$ be the standard $2$-dimensional representation of $SU(2)$. We regard $V$ as a real representation, so it is $4$-dimensional.

(a) Show that $V$ is irreducible (as a real representation).

(b) Let $\mathbb H$ be the subspace of $\operatorname{End}_{\mathbb R}(V)$ consisting of endomorphisms of $V$ as a real representation. Show that $\mathbb H$ is $4$-dimensional and closed under multiplication. Show that every nonzero element in $\mathbb H$ is invertible, i.e., $\mathbb H$ is an algebra with division.

(c) Find a basis $1,i,j,k$ of $\mathbb H$ such that $1$ is the unit and

$$
i^2=j^2=k^2=-1,\quad ij=-ji=k,\quad jk=-kj=i,\quad ki=-ik=j.
$$

Thus we have that $Q_8$ is a subgroup of the group $\mathbb H^\times$ of invertible elements of $\mathbb H$ under multiplication.

The algebra $\mathbb H$ is called the **quaternion algebra**, and its elements are called **quaternions**. Quaternions were discovered by W. R. Hamilton in 1843 (see Section 4.13).

(d) For $q=a+bi+cj+dk$, $a,b,c,d\in\mathbb R$, let $\bar q=a-bi-cj-dk$ and $\|q\|^2=q\bar q=a^2+b^2+c^2+d^2$. Show that $\overline{q_1q_2}=\bar q_2\bar q_1$ and $\|q_1q_2\|=\|q_1\|\cdot\|q_2\|$.

(e) Let $G$ be the group of quaternions of norm $1$. Show that this group is isomorphic to $SU(2)$. (Thus geometrically $SU(2)$ is the $3$-dimensional sphere.)

(f) Consider the action of $G$ on the space $V\subset\mathbb H$ spanned by $i,j,k$, by $x\to qxq^{-1}$, $q\in G$, $x\in V$. Since this action preserves the norm on $V$, we have a homomorphism $h:SU(2)\to SO(3)$, where $SO(3)$ is the group of rotations of the $3$-dimensional Euclidean space. Show that this homomorphism is surjective and that its kernel is $\{1,-1\}$.

<span class="original-page-anchor" id="pdf-page-92" aria-hidden="true"></span>

**Problem 4.12.8.** It is known that the classification of finite subgroups of $SO(3)$ is as follows:

1) the cyclic group $\mathbb Z/n\mathbb Z$, $n\ge1$, generated by a rotation by $2\pi/n$ around an axis;

2) the dihedral group $D_n$ of order $2n$, $n\ge2$ (the group of rotational symmetries in $3$-space of a plane containing a regular $n$-gon[^regular-two-gon];

3) the group of rotations of a regular tetrahedron ($A_4$);

4) the group of rotations of a cube or regular octahedron ($S_4$);

5) the group of rotations of a regular dodecahedron or icosahedron ($A_5$).

(a) Derive this classification.

Hint: Let $G$ be a finite subgroup of $SO(3)$. Consider the action of $G$ on the unit sphere. A point of the sphere preserved by some nontrivial element of $G$ is called a pole. Show that every nontrivial element of $G$ fixes a unique pair of opposite poles and that the subgroup of $G$ fixing a particular pole $P$ is cyclic, of some order $m$ (called the order of $P$). Thus the orbit of $P$ has $n/m$ elements, where $n=|G|$. Now let $P_1,\ldots,P_k$ be a collection of poles representing all the orbits of $G$ on the set of poles (one representative per orbit), and let $m_1,\ldots,m_k$ be their orders. By counting nontrivial elements of $G$, show that

$$
2\left(1-\frac1n\right)=\sum_i\left(1-\frac1{m_i}\right).
$$

Then find all possible $m_i$ and $n$ that can satisfy this equation and classify the corresponding groups.

(b) Using this classification, classify finite subgroups of $SU(2)$ (use the homomorphism $SU(2)\to SO(3)$).

**Problem 4.12.9.** Find the characters and tensor products of irreducible complex representations of the Heisenberg group from Problem 4.12.2.

**Problem 4.12.10.** Let $G$ be a finite group and let $V$ be a complex representation of $G$ which is faithful, i.e., the corresponding map $G\to$ <span class="original-page-anchor" id="pdf-page-93" aria-hidden="true"></span>$GL(V)$ is injective. Show that any irreducible representation of $G$ occurs inside $S^nV$ (and hence inside $V^{\otimes n}$) for some $n$.

Hint: Show that there exists a vector $u\in V^*$ whose stabilizer in $G$ is $1$. Now define the map $SV\to F(G,\mathbb C)$ sending a polynomial $f$ on $V^*$ to the function $f_u$ on $G$ given by $f_u(g)=f(gu)$. Show that this map is surjective and use this to deduce the desired result.

**Problem 4.12.11.** This problem is about an application of representation theory to physics (elasticity theory). We first describe the physical motivation and then state the mathematical problem.

Imagine a material which occupies a certain region $U$ in the physical space $V=\mathbb R^3$ (a space with a positive definite inner product). Suppose the material is deformed. This means, we have applied a diffeomorphism (= change of coordinates) $g:U\to U'$. The question in elasticity theory is how much stress in the material this deformation will cause.

For every point $P\in U$, let $A_P:V\to V$ be defined by $A_P=dg(P)$. Here $A_P$ is nondegenerate, so it has a polar decomposition $A_P=D_PO_P$, where $O_P$ is orthogonal and $D_P$ is symmetric. The matrix $O_P$ characterizes the rotation part of $A_P$ (which clearly produces no stress), and $D_P$ is the distortion part, which actually causes stress. If the deformation is small, $D_P$ is close to $1$, so $D_P=1+d_P$, where $d_P$ is a small symmetric matrix, i.e., an element of $S^2V$. This matrix is called the **deformation tensor** at $P$.

Now we define the stress tensor, which characterizes stress. Let $v$ be a small nonzero vector in $V$, and let $\sigma$ be a small disk perpendicular to $v$ centered at $P$ of area $\|v\|$. Let $F_v$ be the force with which the part of the material on the $v$-side of $\sigma$ acts on the part on the opposite side. It is easy to deduce from Newton’s laws that $F_v$ is linear in $v$, so there exists a linear operator $S_P:V\to V$ such that $F_v=S_Pv$. It is called the **stress tensor**.

An elasticity law is an equation $S_P=f(d_P)$, where $f$ is a function. The simplest such law is a linear law (Hooke’s law): $f:S^2V\to\operatorname{End}(V)$ is a linear function. In general, such a function is defined by $9\cdot6=54$ parameters, but we will show there are actually only two <span class="original-page-anchor" id="pdf-page-94" aria-hidden="true"></span>essential ones — the **compression modulus** $K$ and the **shearing modulus** $\mu$. For this purpose we will use representation theory.

Recall that the group $SO(3)$ of rotations acts on $V$, so $S^2V$, $\operatorname{End}(V)$ are representations of this group. The laws of physics must be invariant under this group (Galileo transformations), so $f$ must be a homomorphism of representations.

(a) Show that $\operatorname{End}(V)$ admits a decomposition $\mathbb R\oplus V\oplus W$, where $\mathbb R$ is the trivial representation, $V$ is the standard $3$-dimensional representation, and $W$ is a $5$-dimensional representation of $SO(3)$. Show that $S^2V=\mathbb R\oplus W$.

(b) Show that $V$ and $W$ are irreducible, even after complexification. Deduce using Schur’s lemma that $S_P$ is always symmetric, and for $x\in\mathbb R$, $y\in W$ one has $f(x+y)=Kx+\mu y$ for some real numbers $K,\mu$.

In fact, it is clear from physics that $K,\mu$ are positive. Physically, the compression modulus $K$ characterizes resistance of the material to compression or dilation, while the shearing modulus $\mu$ characterizes its resistance to changing the shape of the object without changing its volume. For instance, clay (used for sculpting) has a large compression modulus but a small shearing modulus.

## 4.13. Historical interlude: William Rowan Hamilton’s quaternion of geometry, algebra, metaphysics, and poetry

At age $17$, William Rowan Hamilton’s interest in mathematics was sparked by his discovery of an error in Laplace’s *Celestial Mechanics*. The Royal Astronomer of Ireland was so impressed that in a few years he secured for Hamilton the appointment as Royal Astronomer at Dunsinsk Observatory, where Hamilton was stuck for the rest of his life. Hamilton ploughed through university studies by winning every conceivable honor and took his job at the Observatory even before graduation, but as a practical astronomer he proved to be a failure. Tedious observations did not appeal to him; he found theoretical subjects much more exciting.

<span class="original-page-anchor" id="pdf-page-95" aria-hidden="true"></span>

Hamilton’s social circle included major Romantic poets and philosophers. Hamilton himself harbored poetic aspirations, but William Wordsworth gently channeled his creative energies back to mathematics. Hamilton immersed himself in the reading of Kant, absorbed the Kantian notions of space and time as pure intuitions, and became intrigued by Kant’s casual remark that just as geometry was the “science of space”, algebra could be thought of as the “science of pure time” [61]. Later Hamilton insisted that Kant merely confirmed his own ideas and reading him was more “recognizing” than “discovering” [17, 2:96, 2:98].

Hamilton made his reputation as a mathematician by his studies in optics and mechanics, based on his notion of the characteristic function. He saw his greatest achievement in reducing the solution of $3n$ ordinary differential equations of the second order to the solution of two partial differential equations of the first order and second degree. It was not obvious that this represented any progress toward actually solving the problem, but Hamilton was convinced that even if “no practical facility is gained” from his method, the reduction of all complex calculations to the study of one characteristic function should give one “an intellectual pleasure” (quoted in [18, p. 89]).

Hamilton divided all algebraists into three schools of thought: the practical, the philological, and the theoretical. The practical school viewed algebra as an art and was interested in computation; the philological school viewed it as a language, a set of symbols to be manipulated according to some rules; and only the theoretical school, to which Hamilton modestly assigned himself, treated algebra as a science, “strict, pure, and independent, deduced by valid reasonings from its own intuitive principles” [17, 2:48].

“I am never satisfied unless I think that I can look beyond or through the signs to the things signified”, wrote Hamilton. He was frustrated by the inability to find “things signified” behind the notions of negative and imaginary numbers, which therefore looked absurd to him. By 1828 he became “greatly dissatisfied with the phrases, if not the reasonings, of even very eminent analysts”. He believed that in order to “clear away the metaphysical stumbling-blocks that beset the entrance of analysis”, one needed either to discard negative and <span class="original-page-anchor" id="pdf-page-96" aria-hidden="true"></span>imaginary numbers or to explain their “true sense” [17, 2:143, 1:304]. Hamilton soon learned of the so-called Argand diagram representing the complex number as a point on a plane, with its real and imaginary parts plotted on two rectangular axes. Inspired by this geometrical representation, he began looking for an algebraic representation of complex numbers for which all valid operations could be defined and soon developed the concept of algebraic couples. Echoing the Kantian vision of algebra as a science of time, Hamilton viewed these number couples as “steps” in time, rather than magnitudes, and he interpreted negative signs as reversals of temporality [43, p. 281]. He sought a new foundation of algebra in the intuitive notion of pure or mathematical time: the moment was to algebra what the point was to geometry, time intervals were finite straight lines, and an indefinite straight line represented Time itself. Being awfully busy prevented Hamilton from pursuing this promising line of reasoning further. As he remarked, “Time is needed, with all its gross reality of hours and days, even to write upon Pure Time” [17, 2:144].

The $2$-dimensional representation of complex numbers also inspired Hamilton to seek hypercomplex numbers related to the “real” $3$-dimensional space, or “triplets”, as he called them. “Triplets” fit nicely with his philosophical interest in the idealistic triad “thesis-antithesis-synthesis” [20]. Adding triplets was easy, but they stubbornly refused to multiply. They did it for a good reason, for, as Frobenius would prove only after Hamilton’s death, no such algebra was possible. In desperation, Hamilton tried ordered sets of four numbers, or “quaternions”. They agreed to multiply only if the commutative law was lifted. This realization came to Hamilton on October 16th, 1843, as he was walking with his wife along the Royal Canal in Dublin. “I then and there felt the galvanic circuit of thought close; and the sparks which fell from it were the *fundamental equations*” of quaternions, he later recalled. In a less poetic metaphor, he compared his satisfaction upon solving the problem to “an intellectual want relieved” [17, 2:435–436]. Hamilton immediately pulled out his notebook and jotted down the fundamental quaternion formula. Anxious to check the consistency of his new algebra, he continued scribbling in a carriage on the way to a meeting of the Council of the Royal Irish Academy and later while presiding over that meeting as <span class="original-page-anchor" id="pdf-page-97" aria-hidden="true"></span>Academy President. Neither chatting with his wife nor chairing an academic meeting apparently interfered with the train of his mathematical thought.

Hamilton felt that he might explore the ramifications of the quaternion theory for $10$–$15$ years — as long as he had spent trying to work it out. He speculated that the scalar part of the quaternion might express quantity (say, of electricity), while the imaginary parts might determine direction and intensity, for example, electrical polarity. He even gave the calculus of quaternions a “semi-metaphysical” interpretation as a “calculus of polarities”, echoing his earlier interest in idealist philosophy [17, 2:436, 2:440]. In an even stronger metaphysical vein, he came to view quaternions as a natural algebra of space and time, in which the three dimensions of space were joined by the fourth dimension of time. “The quaternion (was) born, as a curious offspring of a quaternion of parents, say of geometry, algebra, metaphysics, and poetry”, he wrote and quoted his own sonnet addressed to Sir John Herschel as the clearest expression of the quaternion idea:

> “And how the one of Time, of Space the Three,  
> Might in the Chain of Symbols girdled be”

(quoted in [20, p. 176]).

Hamilton did everything he could to make his theory unpalatable to the reader, choosing from the outset a “*metaphysical style of expression*”. Herschel implored him to make his ideas “clear and familiar down to the level of ordinary unmetaphysical apprehension” and to “introduce the new phrases as strong meat gradually given to babes” [17, 2:633], but to no avail. Hamilton loaded his $800$-page-long *Lectures on Quaternions* (1853) with new impenetrable terminology, such as *vector*, *vehend*, *vection*, *vectum*, *revector*, *revehend*, *revection*, *revectum*, *provector*, *transvector*, *factor*, *profactor*, *versor*, and *quandrantal versor* [10, p. 36]. His attempt at a more basic introduction, *Elements of Quaternions*, ended up being even longer than the *Lectures*.

Quaternions were popularized by Hamilton’s disciple Peter Tait, who fought a protracted battle with Josiah Willard Gibbs and Oliver Heaviside, promoters of the rival vector analysis. If quaternion multiplication lacked commutativity, the dot product and the cross product <span class="original-page-anchor" id="pdf-page-98" aria-hidden="true"></span>of vectors seemed to have even greater problems, and Tait branded vector analysis a “hermaphrodite monster” [10, p. 185].

Telling his great discovery story to his son $23$ years after the fact, Hamilton added that at his *eureka* moment he could not “resist the impulse — unphilosophical as it may have been — to cut (the quaternion formula) with a knife on a stone” of a nearby bridge [17, 2:435]. Whether this was true or Hamilton simply could not resist the impulse to embellish his story, we will never know, as Time has long erased the etching off the bridge stone — but not off the annals of mathematics. Today the site of Hamilton’s vandalism is marked by a plaque which reads, “Here as he walked by on the 16th of October 1843 Sir William Rowan Hamilton in a flash of genius discovered the fundamental formula for quaternion multiplication $i^2=j^2=k^2=ijk=-1$ & cut it on a stone of this bridge”. The bridge is now a pilgrimage site for mathematicians seeking to ignite their imagination off the sparks of the original flash.

[^4-6-1]: We agree that Hermitian forms are linear in the first argument and antilinear in the second one.

[^regular-two-gon]: A regular $2$-gon is just a line segment.
