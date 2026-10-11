---
title: "Representations of finite groups: Further results"
description: "《Introduction to Representation Theory》English。"
pageClass: algebra-reading representation-theory-reading
prev: {"text":"Representations of finite groups: Basic results","link":"/library/volume-88/original-chapter-004"}
next: {"text":"Quiver representations","link":"/library/volume-88/original-chapter-006"}
---

# Representations of finite groups: Further results

<span class="original-page-anchor" id="pdf-page-99" aria-hidden="true"></span>

## 5.1. Frobenius-Schur indicator

Suppose that $G$ is a finite group and $V$ is an irreducible representation of $G$ over $\mathbb C$.

**Definition 5.1.1.** We say that $V$ is

- of complex type if $V\not\cong V^*$,
- of real type if $V$ has a nondegenerate symmetric form invariant under $G$,
- of quaternionic type if $V$ has a nondegenerate skew form invariant under $G$.

**Problem 5.1.2.** (a) Show that $\operatorname{End}_{\mathbb R[G]}V$ is $\mathbb C$ for $V$ of complex type, $\operatorname{Mat}_2(\mathbb R)$ for $V$ of real type, and $\mathbb H$ for $V$ of quaternionic type, which motivates the names above.

Hint: Show that the complexification $V_{\mathbb C}$ of $V$ decomposes as $V\oplus V^*$. Use this to compute the dimension of $\operatorname{End}_{\mathbb R[G]}V$ in all three cases. Using the fact that $\mathbb C\subset\operatorname{End}_{\mathbb R[G]}V$, prove the result in the complex case. In the remaining two cases, let $B$ be the invariant bilinear form on $V$ and let $(\ ,\ )$ be the invariant positive Hermitian form (they are defined up to a nonzero complex scalar and a positive <span class="original-page-anchor" id="pdf-page-100" aria-hidden="true"></span>real scalar, respectively). Define the operator $j:V\to V$ such that $B(v,w)=(v,jw)$. Show that $j$ is complex antilinear ($ji=-ij$), and $j^2=\lambda\cdot\operatorname{Id}$, where $\lambda$ is a real number, positive in the real case and negative in the quaternionic case (if $B$ is renormalized, $j$ multiplies by a nonzero complex number $z$ and $j^2$ by $z\bar z$, as $j$ is antilinear). Thus $j$ can be normalized so that $j^2=1$ in the real case and $j^2=-1$ in the quaternionic case. Deduce the claim from this.

(b) Show that $V$ is of real type if and only if $V$ is the complexification of a representation $V_{\mathbb R}$ over the field of real numbers.

**Example 5.1.3.** For $\mathbb Z/n\mathbb Z$ all irreducible representations are of complex type except the trivial one and, if $n$ is even, the “sign” representation $m\to(-1)^m$, which are of real type. For $S_3$ all three irreducible representations $\mathbb C_+,\mathbb C_-,\mathbb C^2$ are of real type. For $S_4$ there are five irreducible representations $\mathbb C_+,\mathbb C_-,\mathbb C^2,\mathbb C_+^3,\mathbb C_-^3$, which are all of real type. Similarly, all five irreducible representations of $A_5$ — $\mathbb C,\mathbb C_+^3,\mathbb C_-^3,\mathbb C^4,\mathbb C^5$ — are of real type. As for $Q_8$, its $1$-dimensional representations are of real type, and the $2$-dimensional one is of quaternionic type.

**Definition 5.1.4.** The **Frobenius-Schur indicator** $FS(V)$ of an irreducible representation $V$ is $0$ if it is of complex type, $1$ if it is of real type, and $-1$ if it is of quaternionic type.

**Theorem 5.1.5 (Frobenius-Schur).** *The number of involutions (= elements of order $\le2$) in $G$ is equal to $\sum_V\dim(V)FS(V)$, i.e., the sum of dimensions of all representations of $G$ of real type minus the sum of dimensions of its representations of quaternionic type.*

**Proof.** Let $A:V\to V$ have eigenvalues $\lambda_1,\lambda_2,\ldots,\lambda_n$. We have

$$
\operatorname{Tr}|_{S^2V}(A\otimes A)=\sum_{i\le j}\lambda_i\lambda_j,
$$

$$
\operatorname{Tr}|_{\Lambda^2V}(A\otimes A)=\sum_{i<j}\lambda_i\lambda_j.
$$

Thus,

$$
\operatorname{Tr}|_{S^2V}(A\otimes A)-\operatorname{Tr}|_{\Lambda^2V}(A\otimes A)=\sum_{1\le i\le n}\lambda_i^2=\operatorname{Tr}(A^2).
$$

<span class="original-page-anchor" id="pdf-page-101" aria-hidden="true"></span>

Thus for $g\in G$ we have

$$
\chi_V(g^2)=\chi_{S^2V}(g)-\chi_{\Lambda^2V}(g).
$$

Therefore, setting $P=|G|^{-1}\sum_{g\in G}g$, we get

$$
\begin{aligned}
|G|^{-1}\chi_V\left(\sum_{g\in G}g^2\right)
&=\chi_{S^2V}(P)-\chi_{\Lambda^2V}(P)\\
&=\dim(S^2V)^G-\dim(\Lambda^2V)^G\\
&=\begin{cases}
1&\text{if }V\text{ is of real type},\\
-1&\text{if }V\text{ is of quaternionic type},\\
0&\text{if }V\text{ is of complex type}.
\end{cases}
\end{aligned}
$$

Finally, the number of involutions in $G$ equals

$$
\frac1{|G|}\sum_V\dim V\chi_V\left(\sum_{g\in G}g^2\right)=\sum_{\text{real }V}\dim V-\sum_{\text{quat. }V}\dim V.
$$

$\square$

**Corollary 5.1.6.** *Assume that all representations of a finite group $G$ are defined over real numbers (i.e., all complex representations of $G$ are obtained by complexifying real representations). Then the sum of the dimensions of all the irreducible representations of $G$ equals the number of involutions in $G$.*

**Exercise 5.1.7.** Show that any nontrivial finite group of odd order has an irreducible representation which is not defined over $\mathbb R$ (i.e., not realizable by real matrices).

## 5.2. Algebraic numbers and algebraic integers

We are now passing to deeper results in the representation theory of finite groups. These results require the theory of algebraic numbers, which we will now briefly review.

**Definition 5.2.1.** $z\in\mathbb C$ is an **algebraic number** (respectively, an **algebraic integer**) if $z$ is a root of a monic polynomial with rational (respectively, integer) coefficients.

**Definition 5.2.2.** $z\in\mathbb C$ is an **algebraic number**, (respectively, an **algebraic integer**), if $z$ is an eigenvalue of a matrix with rational (respectively, integer) entries.

<span class="original-page-anchor" id="pdf-page-102" aria-hidden="true"></span>

**Proposition 5.2.3.** *Definitions (5.2.1) and (5.2.2) are equivalent.*

**Proof.** To show that the condition of Definition 5.2.2 implies the condition of Definition 5.2.1, notice that $z$ is a root of the characteristic polynomial of the matrix (a monic polynomial with rational, respectively integer, coefficients). To establish the converse, suppose $z$ is a root of

$$
p(x)=x^n+a_1x^{n-1}+\cdots+a_{n-1}x+a_n.
$$

Then the characteristic polynomial of the following matrix (called the **companion matrix**) is $p(x)$:

$$
\begin{pmatrix}
0&0&0&\cdots&0&-a_n\\
1&0&0&\cdots&0&-a_{n-1}\\
0&1&0&\cdots&0&-a_{n-2}\\
\vdots&\vdots&\ddots&\ddots&\vdots&\vdots\\
0&0&0&\cdots&1&-a_1
\end{pmatrix}.
$$

Since $z$ is a root of the characteristic polynomial of this matrix, it is an eigenvalue of this matrix. $\square$

The set of algebraic numbers is denoted by $\overline{\mathbb Q}$, and the set of algebraic integers is denoted by $\mathbb A$.

**Proposition 5.2.4.** *(i) $\mathbb A$ is a ring.*

*(ii) $\overline{\mathbb Q}$ is a field. Namely, it is an algebraic closure of the field of rational numbers.*

**Proof.** We will be using Definition 5.2.2. Let $\alpha$ be an eigenvalue of

$$
A\in\operatorname{Mat}_n(\mathbb C)
$$

with eigenvector $v$, and let $\beta$ be an eigenvalue of

$$
B\in\operatorname{Mat}_m(\mathbb C)
$$

with eigenvector $w$. Then $\alpha\pm\beta$ is an eigenvalue of

$$
A\otimes\operatorname{Id}_m\pm\operatorname{Id}_n\otimes B,
$$

<span class="original-page-anchor" id="pdf-page-103" aria-hidden="true"></span>

and $\alpha\beta$ is an eigenvalue of

$$
A\otimes B.
$$

The corresponding eigenvector is in both cases $v\otimes w$. This shows that both $\mathbb A$ and $\overline{\mathbb Q}$ are rings. To show that the latter is a field, it suffices to note that if $\alpha\ne0$ is a root of a polynomial $p(x)$ of degree $d$, then $\alpha^{-1}$ is a root of $x^dp(1/x)$. The last statement is easy, since a number $\alpha$ is algebraic if and only if it defines a finite extension of $\mathbb Q$. $\square$

**Proposition 5.2.5.** $\mathbb A\cap\mathbb Q=\mathbb Z$.

**Proof.** We will be using Definition 5.2.1. Let $z$ be a root of

$$
p(x)=x^n+a_1x^{n-1}+\cdots+a_{n-1}x+a_n,
$$

and suppose

$$
z=\frac pq\in\mathbb Q,\qquad\gcd(p,q)=1.
$$

Notice that the leading term of $p(x)$ will have $q^n$ in the denominator, whereas all the other terms will have a lower power of $q$ there. Thus, if $q\ne\pm1$, then $p(z)\notin\mathbb Z$, a contradiction. Thus, $z\in\mathbb A\cap\mathbb Q\Rightarrow z\in\mathbb Z$. The reverse inclusion follows because $n\in\mathbb Z$ is a root of $x-n$. $\square$

Every algebraic number $\alpha$ has a **minimal polynomial** $p(x)$ which is the monic polynomial with rational coefficients of the smallest degree such that $p(\alpha)=0$. Any other polynomial $q(x)$ with rational coefficients such that $q(\alpha)=0$ is divisible by $p(x)$. Roots of $p(x)$ are called the **algebraic conjugates** of $\alpha$; they are roots of any polynomial $q$ with rational coefficients such that $q(\alpha)=0$.

Note that any algebraic conjugate of an algebraic integer is obviously also an algebraic integer. Therefore, by the Vieta theorem, the minimal polynomial of an algebraic integer has integer coefficients.

Below we will need the following lemma:

**Lemma 5.2.6.** *If $\alpha_1,\ldots,\alpha_m$ are algebraic numbers, then all algebraic conjugates to $\alpha_1+\cdots+\alpha_m$ are of the form $\alpha'_1+\cdots+\alpha'_m$, where $\alpha'_i$ are some algebraic conjugates of $\alpha_i$.*

**Proof.** It suffices to prove this for two summands. If $\alpha_i$ are eigenvalues of rational matrices $A_i$ of smallest size (i.e., their characteristic <span class="original-page-anchor" id="pdf-page-104" aria-hidden="true"></span>polynomials are the minimal polynomials of $\alpha_i$), then $\alpha_1+\alpha_2$ is an eigenvalue of $A:=A_1\otimes\operatorname{Id}+\operatorname{Id}\otimes A_2$. Therefore, so is any algebraic conjugate to $\alpha_1+\alpha_2$. But all eigenvalues of $A$ are of the form $\alpha'_1+\alpha'_2$, so we are done. $\square$

**Problem 5.2.7.** (a) Show that for any finite group $G$ there exists a finite Galois extension $K\subset\mathbb C$ of $\mathbb Q$ such that any finite dimensional complex representation of $G$ has a basis in which the matrices of the group elements have entries in $K$.

Hint: Consider the representations of $G$ over the field $\overline{\mathbb Q}$ of algebraic numbers.

(b) Show that if $V$ is an irreducible complex representation of a finite group $G$ of dimension $>1$, then there exists $g\in G$ such that $\chi_V(g)=0$.

Hint: Assume the contrary. Use orthonormality of characters to show that the arithmetic mean of the numbers $|\chi_V(g)|^2$ for $g\ne1$ is $<1$. Deduce that their product $\beta$ satisfies $0<\beta<1$. Show that all conjugates of $\beta$ satisfy the same inequalities (consider the Galois conjugates of the representation $V$, i.e., representations obtained from $V$ by the action of the Galois group of $K$ over $\mathbb Q$ on the matrices of group elements in the basis from part (a)). Then derive a contradiction.

**Remark 5.2.8.** Here is a modification of this argument, which does not use (a). Let $N=|G|$. For any $0<j<N$ coprime to $N$, show that the map $g\mapsto g^j$ is a bijection $G\to G$. Deduce that $\prod_{g\ne1}|\chi_V(g^j)|^2=\beta$. Then show that $\beta\in K:=\mathbb Q(\zeta)$, $\zeta=e^{2\pi i/N}$, and that it does not change under the automorphism of $K$ given by $\zeta\mapsto\zeta^j$. Deduce that $\beta$ is an integer, and derive a contradiction.

## 5.3. Frobenius divisibility

**Theorem 5.3.1.** *Let $G$ be a finite group, and let $V$ be an irreducible representation of $G$ over $\mathbb C$. Then*

$$
\dim V\text{ divides }|G|.
$$

<span class="original-page-anchor" id="pdf-page-105" aria-hidden="true"></span>

**Proof.** Let $C_1,C_2,\ldots,C_n$ be the conjugacy classes of $G$. Let $g_{C_i}$ be representatives of $C_i$. Set

$$
\lambda_i=\chi_V(g_{C_i})\frac{|C_i|}{\dim V}.
$$

**Proposition 5.3.2.** *The numbers $\lambda_i$ are algebraic integers for all $i$.*

**Proof.** Let $C$ be a conjugacy class in $G$, and let $P=\sum_{h\in C}h$. Then $P$ is a central element of $\mathbb Z[G]$, so it acts on $V$ by some scalar $\lambda$, which is an algebraic integer (indeed, since $\mathbb Z[G]$ is a finitely generated $\mathbb Z$-module, any element of $\mathbb Z[G]$ is integral over $\mathbb Z$, i.e., satisfies a monic polynomial equation with integer coefficients). On the other hand, taking the trace of $P$ in $V$, we get $|C|\chi_V(g)=\lambda\dim V$, $g\in C$, so $\lambda=\frac{|C|\chi_V(g)}{\dim V}$. $\square$

Now, consider

$$
\sum_i\lambda_i\overline{\chi_V(g_{C_i})}.
$$

This is an algebraic integer, since:

(i) $\lambda_i$ are algebraic integers by Proposition 5.3.2,

(ii) $\chi_V(g_{C_i})$ is a sum of roots of unity (it is the sum of eigenvalues of the matrix of $\rho(g_{C_i})$, and since $g_{C_i}^{|G|}=e$ in $G$, the eigenvalues of $\rho(g_{C_i})$ are roots of unity), and

(iii) $\mathbb A$ is a ring (Proposition 5.2.4).

On the other hand, from the definition of $\lambda_i$,

$$
\sum_{C_i}\lambda_i\overline{\chi_V(g_{C_i})}=\sum_i\frac{|C_i|\chi_V(g_{C_i})\overline{\chi_V(g_{C_i})}}{\dim V}.
$$

Recalling that $\chi_V$ is a class function, this is equal to

$$
\sum_{g\in G}\frac{\chi_V(g)\overline{\chi_V(g)}}{\dim V}=\frac{|G|(\chi_V,\chi_V)}{\dim V}.
$$

Since $V$ is an irreducible representation, $(\chi_V,\chi_V)=1$, so

$$
\sum_{C_i}\lambda_i\overline{\chi_V(g_{C_i})}=\frac{|G|}{\dim V}.
$$

<span class="original-page-anchor" id="pdf-page-106" aria-hidden="true"></span>

Since $\frac{|G|}{\dim V}\in\mathbb Q$ and $\sum_{C_i}\lambda_i\overline{\chi_V(g_{C_i})}\in\mathbb A$, by Proposition 5.2.5, $\frac{|G|}{\dim V}\in\mathbb Z$. $\square$

## 5.4. Burnside’s theorem

**Definition 5.4.1.** A group $G$ is called **solvable** if there exists a series of nested normal subgroups

$$
\{e\}=G_1\triangleleft G_2\triangleleft\cdots\triangleleft G_n=G
$$

where $G_{i+1}/G_i$ is abelian for all $1\le i\le n-1$.

**Remark 5.4.2.** Such groups are called solvable because they first arose as Galois groups of polynomial equations which are solvable in radicals.

**Theorem 5.4.3 (Burnside).** *Any group $G$ of order $p^aq^b$, where $p$ and $q$ are primes and $a,b\ge0$, is solvable.*

This famous result in group theory was proved by the British mathematician William Burnside in the early $20$th century, using representation theory (see Section 5.5 and [Cu]). Here is this proof, presented in modern language.

Before proving Burnside’s theorem, we will prove several other results which are of independent interest.

**Theorem 5.4.4.** *Let $V$ be an irreducible representation of a finite group $G$ and let $C$ be a conjugacy class of $G$ with $\gcd(|C|,\dim(V))=1$. Then for any $g\in C$, either $\chi_V(g)=0$ or $g$ acts as a scalar on $V$.*

The proof will be based on the following lemma.

**Lemma 5.4.5.** *If $\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n$ are roots of unity such that $\frac1n(\varepsilon_1+\varepsilon_2+\cdots+\varepsilon_n)$ is an algebraic integer, then either $\varepsilon_1=\cdots=\varepsilon_n$ or $\varepsilon_1+\cdots+\varepsilon_n=0$.*

**Proof.** Let $a=\frac1n(\varepsilon_1+\cdots+\varepsilon_n)$. If not all $\varepsilon_i$ are equal, then $|a|<1$. Moreover, since any algebraic conjugate of a root of unity is also a root of unity, $|a'|\le1$ for any algebraic conjugate $a'$ of $a$. But the product of all algebraic conjugates of $a$ is an integer. Since it has absolute value $<1$, it must equal zero. Therefore, $a=0$. $\square$

<span class="original-page-anchor" id="pdf-page-107" aria-hidden="true"></span>

**Proof of Theorem 5.4.4.** Let $\dim V=n$. Let $\varepsilon_1,\varepsilon_2,\ldots,\varepsilon_n$ be the eigenvalues of $\rho_V(g)$. They are roots of unity, so $\chi_V(g)$ is an algebraic integer. Also, by Proposition 5.3.2, $\frac1n|C|\chi_V(g)$ is an algebraic integer. Since $\gcd(n,|C|)=1$, there exist integers $a,b$ such that $a|C|+bn=1$. This implies that

$$
\frac{a|C|\chi_V(g)}n+b\chi_V(g)=\frac{\chi_V(g)}n=\frac1n(\varepsilon_1+\cdots+\varepsilon_n)
$$

is an algebraic integer. Thus, by Lemma 5.4.5, we get that either $\varepsilon_1=\cdots=\varepsilon_n$ or $\varepsilon_1+\cdots+\varepsilon_n=\chi_V(g)=0$. In the first case, since $\rho_V(g)$ is diagonalizable, it must be scalar. In the second case, $\chi_V(g)=0$. The theorem is proved. $\square$

**Theorem 5.4.6.** *Let $G$ be a finite group, and let $C$ be a conjugacy class in $G$ of order $p^k$ where $p$ is a prime and $k>0$. Then $G$ has a proper nontrivial normal subgroup (i.e., $G$ is not simple).*

**Proof.** Choose an element $g\in C$. Since $g\ne e$, by orthogonality of columns of the character table,

$$
\sum_{V\in\operatorname{Irr}G}\dim V\chi_V(g)=0.\tag{5.4.1}
$$

We can divide $\operatorname{Irr}G$ into three parts:

(1) the trivial representation,

(2) $D$, the set of irreducible representations whose dimension is divisible by $p$, and

(3) $N$, the set of nontrivial irreducible representations whose dimension is not divisible by $p$.

**Lemma 5.4.7.** *There exists $V\in N$ such that $\chi_V(g)\ne0$.*

**Proof.** If $V\in D$, the number $\frac1p\dim(V)\chi_V(g)$ is an algebraic integer, so

$$
a=\sum_{V\in D}\frac1p\dim(V)\chi_V(g)
$$

is an algebraic integer.

<span class="original-page-anchor" id="pdf-page-108" aria-hidden="true"></span>

Now, by (5.4.1), we have

$$
\begin{aligned}
0&=\chi_{\mathbb C}(g)+\sum_{V\in D}\dim V\chi_V(g)+\sum_{V\in N}\dim V\chi_V(g)\\
&=1+pa+\sum_{V\in N}\dim V\chi_V(g).
\end{aligned}
$$

This means that the last summand is nonzero. $\square$

Now pick $V\in N$ such that $\chi_V(g)\ne0$; it exists by Lemma 5.4.7. Theorem 5.4.4 implies that $g$ (and hence any element of $C$) acts by a scalar in $V$. Now let $H$ be the subgroup of $G$ generated by elements $ab^{-1}$, $a,b\in C$. It is normal and acts trivially in $V$, so $H\ne G$, as $V$ is nontrivial. Also $H\ne1$, since $|C|>1$. $\square$

**Proof of Burnside’s theorem.** Assume Burnside’s theorem is false. Then there exists a nonsolvable group $G$ of order $p^aq^b$. Let $G$ be the smallest such group. Then $G$ is simple, and by Theorem 5.4.6, it cannot have a conjugacy class of order $p^k$ or $q^k$, $k\ge1$. So the order of any conjugacy class in $G$ either equals $1$ or is divisible by $pq$. Adding the orders of conjugacy classes and equating the sum to $p^aq^b$, we see that there has to be more than one conjugacy class consisting just of one element. So $G$ has a nontrivial center, which gives a contradiction. $\square$

## 5.5. Historical interlude: William Burnside and intellectual harmony in mathematics

While at Cambridge, William Burnside (1852–1927) distinguished himself in rowing; his other achievements include emerging from the 1875 Mathematical Tripos as Second Wrangler and then beating First Wrangler in an even more grueling mathematical competition for the Smith Prize. Afterwards, he taught at Cambridge as a mathematics lecturer and a coach for both the Math Tripos and for the rowing crews. In 1885, true to his aquatic interests, Burnside accepted the position of professor of mathematics in the Royal Naval College at Greenwich, where he taught until retirement. When his enthusiasm for rowing subsided, fishing became Burnside’s favorite hobby. Even <span class="original-page-anchor" id="pdf-page-109" aria-hidden="true"></span>in mathematical research he stayed close to water, making major contributions to hydrodynamics.

On the strength of his contributions to mathematical physics and complex function theory, Burnside was elected to the Royal Society in 1893. Once this worthy goal was achieved, however, he abandoned such trifle subjects and dipped into the theory of groups. Four years later Burnside published the first English textbook on the subject, *Theory of Groups of Finite Order*. He was apparently delighted to take a break from applied studies and to immerse himself in an abstract theory, for he wrote in the preface: “The present treatise is intended to introduce to the reader the main outlines of the theory of groups of finite order apart from any applications”. Burnside noted that group theory was not yet particularly popular in England. “It will afford me much satisfaction”, he remarked, “if, by means of this book, I shall succeed in arousing interest among English mathematicians in a branch of pure mathematics which becomes the more fascinating the more it is studied” (quoted in [11, pp. 88–89]).

The interest of English mathematicians, however, proved not to be easily aroused, and ten years later Burnside bitterly remarked in his retiring Presidential address to the London Mathematical Society: “It is undoubtedly the fact that the theory of groups of finite order has failed, so far, to arouse the interest of any but a very small number of English mathematicians”. Burnside cited the proliferation of courses on group theory in France, the United States, and especially Germany (attended by thirty students in Göttingen!), and he lamented the total indifference of British students toward the subject. His explanation was that group theory was treated in a highly abstract manner, “one which the young mind grasps with difficulty, if at all”. As an example, Burnside cited a formal statement about the properties of the icosahedral group and claimed that “a proposal to verify the statement appears equivalent to proposing a series of conundrums. There would be nothing here to attract the student or to suggest anything but the driest formalism utterly divorced from any of his previous mathematical studies” [8, pp. 1, 3, 5].

Burnside himself, however, had done much to establish the culture of purely abstract reasoning in group theory. In the preface to <span class="original-page-anchor" id="pdf-page-110" aria-hidden="true"></span>his 1897 book he wrote that his university teacher Arthur Cayley’s “dictum that ‘a group is defined by means of the laws of combination of its symbols’ would imply that, in dealing with the theory of groups, no more concrete mode of representation should be used than is absolutely necessary” (quoted in [11, p. 90]). No wonder Burnside omitted any applications from his book, while his 1899 article on the simple group of order 504 mentioned a concrete example only in the last paragraph [1, p. 13]. He cultivated conciseness as a highest virtue. When a friend once asked for a more expanded treatment of certain topics from *Theory of Groups*, Burnside responded by “a declaration of regret that he had been unable to effect further condensation” [15, p. 70]. Burnside’s ideal lived on in the tradition of Bourbaki, causing the wrath of the champions of “mathematics with a human face”, led by Vladimir Arnold: “Algebraists usually define groups as sets with operations that satisfy a long list of hard-to-remember axioms. I think one cannot understand such a definition. I believe the algebraists set up such obstacles in the path of students to make it harder for the uninitiated to penetrate their field. Perhaps their goal, if only subconscious, is to boost the reputation of their field” [2, p. 118].

While pursuing the condensation ideal, Burnside decided to omit any discussion of linear substitution groups from the 1897 edition of *Theory of Groups*. “It would be difficult to find a result that could be most directly obtained by the consideration of groups of linear transformations”, he wrote, justifying the exclusion of this useless subject (quoted in [11, p. 90]). Within a few months, however, Burnside had to reevaluate the wisdom of his decision, as he came across Frobenius’s articles on group characters. Frobenius’s results proved highly relevant to Burnside’s own research on finite groups, and Burnside set out to reformulate them in his own language. Unlike Frobenius, Burnside felt at ease with Sophus Lie’s apparatus of continuous groups of transformations, and he was able to derive all of Frobenius’s main results on characters and on the group determinant by using the methods of Lie groups and Lie algebras. Burnside published his research with a modest disclaimer that his paper was “not original, as the results arrived at are, with one or two slight exceptions, due to Herr Frobenius. The modes of proof, however, are in general quite distinct from those used by Herr Frobenius” (quoted in [11, p. 106]).

<span class="original-page-anchor" id="pdf-page-111" aria-hidden="true"></span>

Herr Frobenius was hardly impressed by what he saw as a lame excuse for stepping on his toes. Richard Dedekind was similarly outraged, when he recognized in one of Burnside’s papers his own theorem on the factorization of the group determinant of an abelian group. Frobenius consoled his friend by recounting his own losses: “This is the same Herr Burnside who annoyed me several years ago by quickly rediscovering all the theorems I had published on the theory of groups, in the same order and without exception: first my proof of Sylow’s Theorems, then the theorem on groups with square-free orders, on groups of order $p^a q$, on groups whose order is a product of four or five prime numbers, etc., etc. In any case, a very remarkable and amazing example of intellectual harmony, probably as is possible only in England and perhaps America” (quoted in [24, p. 242]). Burnside, for his part, began stressing that he had “obtained independently the chief results of Prof. Frobenius’ earlier memoirs” (quoted in [23, p. 278]). Herren Burnside and Frobenius never corresponded to straighten things out, leaving the matter to historians, who somewhat qualified Burnside’s claim of independence. Burnside was clearly inspired by Frobenius’s work, although he did not know all of the relevant Frobenius papers, which left him enough space to explore on his own [23, p. 278].

Burnside and Frobenius worked neck and neck on the solvability of $p^a q^b$ groups. While Sylow (1872), Frobenius (1895), and Jordan (1898) proved some special cases, Burnside succeeded in proving the general case in 1904. Burnside’s character theoretic proof has been described as “so easy and pleasant” that later group-theoretic proofs would not even come close to its “compelling simplicity” and “striking beauty” [30, p. 469]. As Walter Feit suggested, “[T]he elegance of both the statement and the proof have attracted more people to the study of characters than any other result in the subject” [14, p. 4]. In particular, they attracted Feit, who in 1962 proved (with J. G. Thompson) Burnside’s conjecture that every group of odd order is solvable. Another seminal conjecture, Burnside’s Problem, related to the structure of torsion groups, has preoccupied group theory and representation theory specialists for over a century, yielding the 1994 Fields Medal to Efim Zelmanov for the solution of its restricted version.

<span class="original-page-anchor" id="pdf-page-112" aria-hidden="true"></span>

The appreciation of the beauty of Burnside’s work took quite a while. His employment at the Royal Naval College separated him geographically from his university colleagues. He apparently had no “extensive direct contacts with other mathematicians interested in the subject (of group theory). It appears that he worked in isolation, possibly even more so than was normal for his times, with little opportunity (or, perhaps, inclination) to discuss his ideas with others”, according to his biographer [41, p. 32]. Burnside taught several generations of navy officers but created no mathematical school of his own.

In December 1925 Burnside suffered a stroke, and his doctor forbade him, among other unhealthy activities, from doing mathematics. Burnside naturally disobeyed and did not live very long. His obituary in the *London Evening News* barely mentioned his mathematical studies but reported that “rowing men will regret to hear of the death of W. Burnside, one of the best known Cambridge athletes of his day” (quoted in [11, p. 96]).

Shortly before his death Burnside answered a query from a young mathematician named Philip Hall, who asked for advice on topics of group theory. Burnside sent him a postcard listing a few problems worth investigating. This message in a bottle, thrown into the sea, miraculously found a perfect addressee. The same volume of the *Journal of the London Mathematical Society* that contained Burnside’s obituary featured Hall’s “Note on Soluble Groups”, which marked the beginning of his lifetime career in this field. Hall eventually succeeded Burnside as the chief promoter of group theory in England. “The aim of my researches”, he later wrote, “has been to a very considerable extent that of extending and completing in certain directions the work of Burnside” (quoted in [11, p. 96]).

## 5.6. Representations of products

**Theorem 5.6.1.** Let $G,H$ be finite groups, let $\{V_i\}$ be the irreducible representations of $G$ over a field $k$ (of any characteristic), and let $\{W_j\}$ be the irreducible representations of $H$ over $k$. Then the irreducible representations of $G\times H$ over $k$ are $\{V_i\otimes W_j\}$.

<span class="original-page-anchor" id="pdf-page-113" aria-hidden="true"></span>

**Proof.** This follows from Theorem 3.10.2. $\square$

## 5.7. Virtual representations

**Definition 5.7.1.** A **virtual representation** of a finite group $G$ is an integer linear combination of irreducible representations of $G$, $V=\sum n_iV_i$, $n_i\in\mathbb Z$ (i.e., $n_i$ are not assumed to be nonnegative). The character of $V$ is $\chi_V:=\sum n_i\chi_{V_i}$.

The following lemma is often very useful (and will be used several times below).

**Lemma 5.7.2.** Let $V$ be a virtual representation with character $\chi_V$. If $(\chi_V,\chi_V)=1$ and $\chi_V(1)>0$, then $\chi_V$ is a character of an irreducible representation of $G$.

**Proof.** Let $V_1,V_2,\ldots,V_m$ be the irreducible representations of $G$, and let $V=\sum n_iV_i$. Then by orthonormality of characters, $(\chi_V,\chi_V)=\sum_i n_i^2$. So $\sum_i n_i^2=1$, meaning that $n_i=\pm1$ for exactly one $i$ and $n_j=0$ for $j\ne i$. But $\chi_V(1)>0$, so $n_i=+1$ and we are done. $\square$

## 5.8. Induced representations

Given a representation $V$ of a group $G$ and a subgroup $H\subset G$, there is a natural way to construct a representation of $H$. The **restriction** of $V$ to $H$, $\operatorname{Res}_H^G V$, is the representation given by the vector space $V$, and the action $\rho_{\operatorname{Res}_H^G V}=\rho_V|_H$.

There is also a natural, but less trivial, way to construct a representation of a group $G$ given a representation $V$ of its subgroup $H$.

**Definition 5.8.1.** If $G$ is a group, $H\subset G$, and $V$ is a representation of $H$, then the **induced representation** $\operatorname{Ind}_H^G V$, is the representation of $G$ with

$$
\operatorname{Ind}_H^G V=\{f:G\to V\mid f(hx)=\rho_V(h)f(x)\ \forall x\in G,h\in H\}
$$

and the action $g(f)(x)=f(xg)$ $\forall g\in G$.

**Remark 5.8.2.** In fact, $\operatorname{Ind}_H^G V$ is naturally isomorphic to the representation $\operatorname{Hom}_H(k[G],V)$.

<span class="original-page-anchor" id="pdf-page-114" aria-hidden="true"></span>

Let us check that $\operatorname{Ind}_H^G V$ is well defined as a representation. Indeed, we have

$$
g(f)(hx)=f(hxg)=\rho_V(h)f(xg)=\rho_V(h)g(f)(x),
$$

and

$$
g(g'(f))(x)=g'(f)(xg)=f(xgg')=(gg')(f)(x)
$$

for any $g,g',x\in G$ and $h\in H$.

**Remark 5.8.3.** Notice that if we choose a representative $x_\sigma$ from every right $H$-coset $\sigma$ of $G$, then any $f\in\operatorname{Ind}_H^G V$ is uniquely determined by $\{f(x_\sigma)\}$.

Because of this,

$$
\dim(\operatorname{Ind}_H^G V)=\dim V\cdot\frac{|G|}{|H|}.
$$

**Problem 5.8.4.** Check that if $K\subset H\subset G$ are groups and if $V$ is a representation of $K$, then $\operatorname{Ind}_H^G\operatorname{Ind}_K^H V$ is isomorphic to $\operatorname{Ind}_K^G V$.

**Exercise 5.8.5.** Let $K\subset G$ be finite groups, and let $\chi:K\to\mathbb C^*$ be a homomorphism. Let $\mathbb C_\chi$ be the corresponding 1-dimensional representation of $K$. Let

$$
e_\chi=\frac{1}{|K|}\sum_{g\in K}\chi(g)^{-1}g\in\mathbb C[K]
$$

be the idempotent corresponding to $\chi$. Show that the $G$-representation $\operatorname{Ind}_K^G\mathbb C_\chi$ is naturally isomorphic to $\mathbb C[G]e_\chi$ (with $G$ acting by left multiplication).

## 5.9. The Frobenius formula for the character of an induced representation

Let us now compute the character $\chi$ of $\operatorname{Ind}_H^G V$. In each right coset $\sigma\in H\backslash G$, choose a representative $x_\sigma$.

**Theorem 5.9.1.** One has

$$
\chi(g)=\sum_{\substack{\sigma\in H\backslash G:\\x_\sigma g x_\sigma^{-1}\in H}}\chi_V(x_\sigma g x_\sigma^{-1}).
$$

This formula is called the Frobenius formula.

<span class="original-page-anchor" id="pdf-page-115" aria-hidden="true"></span>

**Remark 5.9.2.** If the characteristic of the ground field $k$ is relatively prime to $|H|$, then this formula can be written as

$$
\chi(g)=\frac{1}{|H|}\sum_{\substack{x\in G:\\xgx^{-1}\in H}}\chi_V(xgx^{-1}).
$$

**Proof.** For a right $H$-coset $\sigma$ of $G$, let us define

$$
V_\sigma=\{f\in\operatorname{Ind}_H^G V\mid f(g)=0\ \forall g\notin\sigma\}.
$$

Then one has

$$
\operatorname{Ind}_H^G V=\bigoplus_\sigma V_\sigma,
$$

and so

$$
\chi(g)=\sum_\sigma\chi_\sigma(g),
$$

where $\chi_\sigma(g)$ is the trace of the diagonal block of $\rho(g)$ corresponding to $V_\sigma$.

Since $g(\sigma)=\sigma g$ is a right $H$-coset for any right $H$-coset $\sigma$, $\chi_\sigma(g)=0$ if $\sigma\ne\sigma g$.

Now assume that $\sigma=\sigma g$. Then $x_\sigma g=hx_\sigma$ where $h=x_\sigma g x_\sigma^{-1}\in H$. Consider the map $\alpha:V_\sigma\to V$ defined by $\alpha(f)=f(x_\sigma)$. Since $f\in V_\sigma$ is uniquely determined by $f(x_\sigma)$, $\alpha$ is an isomorphism. We have

$$
\alpha(gf)=g(f)(x_\sigma)=f(x_\sigma g)=f(hx_\sigma)=\rho_V(h)f(x_\sigma)=h\alpha(f),
$$

and $gf=\alpha^{-1}h\alpha(f)$. This means that $\chi_\sigma(g)=\chi_V(h)$. Therefore

$$
\chi(g)=\sum_{\substack{\sigma\in H\backslash G,\\\sigma g=\sigma}}\chi_V(x_\sigma g x_\sigma^{-1}).
$$

$\square$

## 5.10. Frobenius reciprocity

A very important result about induced representations is the Frobenius reciprocity theorem which connects the operations $\operatorname{Ind}$ and $\operatorname{Res}$.

**Theorem 5.10.1 (Frobenius reciprocity).** Let $H\subset G$ be groups, $V$ a representation of $G$ and $W$ a representation of $H$. Then the space $\operatorname{Hom}_G(V,\operatorname{Ind}_H^G W)$ is naturally isomorphic to $\operatorname{Hom}_H(\operatorname{Res}_H^G V,W)$.

<span class="original-page-anchor" id="pdf-page-116" aria-hidden="true"></span>

**Proof.** Let $E=\operatorname{Hom}_G(V,\operatorname{Ind}_H^G W)$ and $E'=\operatorname{Hom}_H(\operatorname{Res}_H^G V,W)$. Define $F:E\to E'$ and $F':E'\to E$ as follows: $F(\alpha)v=(\alpha v)(e)$ for any $\alpha\in E$ and $(F'(\beta)v)(x)=\beta(xv)$ for any $\beta\in E'$.

In order to check that $F$ and $F'$ are well defined and inverse to each other, we need to check the following five statements.

Let $\alpha\in E$, $\beta\in E'$, $v\in V$, and $x,g\in G$.

(a) $F(\alpha)$ is an $H$-homomorphism; i.e., $F(\alpha)hv=hF(\alpha)v$.

Indeed, $F(\alpha)hv=(\alpha hv)(e)=(h\alpha v)(e)=(\alpha v)(he)=(\alpha v)(eh)=h\cdot(\alpha v)(e)=hF(\alpha)v$.

(b) $F'(\beta)v\in\operatorname{Ind}_H^G W$; i.e., $(F'(\beta)v)(hx)=h(F'(\beta)v)(x)$.

Indeed, $(F'(\beta)v)(hx)=\beta(hxv)=h\beta(xv)=h(F'(\beta)v)(x)$.

(c) $F'(\beta)$ is a $G$-homomorphism; i.e., $F'(\beta)gv=g(F'(\beta)v)$.

Indeed, $(F'(\beta)gv)(x)=\beta(xgv)=(F'(\beta)v)(xg)=(g(F'(\beta)v))(x)$.

(d) $F\circ F'=\operatorname{Id}_{E'}$.

This holds since $F(F'(\beta))v=(F'(\beta)v)(e)=\beta(v)$.

(e) $F'\circ F=\operatorname{Id}_E$; i.e., $(F'(F(\alpha))v)(x)=(\alpha v)(x)$.

Indeed, $(F'(F(\alpha))v)(x)=F(\alpha xv)=(\alpha xv)(e)=(x\alpha v)(e)=(\alpha v)(x)$, and we are done. $\square$

**Problem 5.10.2.** The purpose of this problem is to understand the notions of restricted and induced representations as part of a more advanced framework. This framework is the notion of tensor products over $k$-algebras. In particular, this understanding will lead us to a new proof of the Frobenius reciprocity and to some analogies between induction and restriction.

Throughout this exercise, we will use the notation and results of Problem 2.11.6.

Let $G$ be a finite group and $H\subset G$ a subgroup. We consider $k[G]$ as a $(k[H],k[G])$-bimodule (both module structures are given by multiplication inside $k[G]$). We denote this bimodule by $k[G]_1$.

On the other hand, we can also consider $k[G]$ as a $(k[G],k[H])$-bimodule (again, both module structures are given by multiplication). We denote this bimodule by $k[G]_2$.

<span class="original-page-anchor" id="pdf-page-117" aria-hidden="true"></span>

(a) Let $V$ be a representation of $G$. Then, $V$ is a left $k[G]$-module. Thus, the tensor product $k[G]_1\otimes_{k[G]}V$ is a left $k[H]$-module. Prove that this tensor product is isomorphic to $\operatorname{Res}_H^G V$ as a left $k[H]$-module. The isomorphism

$$
\operatorname{Res}_H^G V\to k[G]_1\otimes_{k[G]}V
$$

is given by $v\mapsto1\otimes_{k[G]}v$ for every $v\in\operatorname{Res}_H^G V$.

(b) Let $W$ be a representation of $H$. Then $W$ is a left $k[H]$-module. According to Remark 5.8.2, $\operatorname{Ind}_H^G W\cong\operatorname{Hom}_H(k[G],W)$. In other words, we have $\operatorname{Ind}_H^G W\cong\operatorname{Hom}_{k[H]}(k[G]_1,W)$. Now use part (b) of Problem 2.11.6 to conclude Theorem 5.10.1.

(c) Let $V$ be a representation of $G$. Then, $V$ is a left $k[G]$-module. Prove that not only $k[G]_1\otimes_{k[G]}V$ but also $\operatorname{Hom}_{k[G]}(k[G]_2,V)$ is isomorphic to $\operatorname{Res}_H^G V$ as a left $k[H]$-module. The isomorphism

$$
\operatorname{Hom}_{k[G]}(k[G]_2,V)\to\operatorname{Res}_H^G V
$$

is given by $f\mapsto f(1)$ for every $f\in\operatorname{Hom}_{k[G]}(k[G]_2,V)$.

(d) Let $W$ be a representation of $H$. Then, $W$ is a left $k[H]$-module. Show that $\operatorname{Ind}_H^G W$ is isomorphic to $k[G]_2\otimes_{k[H]}W$. The isomorphism $\operatorname{Hom}_{k[H]}(k[G]_1,W)\to k[G]_2\otimes_{k[H]}W$ is given by $f\mapsto\sum_{g\in P}g^{-1}\otimes_{k[H]}f(g)$ for every $f\in\operatorname{Hom}_{k[H]}(k[G]_1,W)$, where $P$ is a set of distinct representatives for the right $H$-cosets in $G$. (This isomorphism is independent of the choice of representatives.)

(e) Let $V$ be a representation of $G$ and let $W$ be a representation of $H$. Use (b) to prove that $\operatorname{Hom}_G(\operatorname{Ind}_H^G W,V)$ is naturally isomorphic to $\operatorname{Hom}_H(W,\operatorname{Res}_H^G V)$.

(f) Let $V$ be a representation of $H$. Prove that $\operatorname{Ind}_H^G(V^*)\cong(\operatorname{Ind}_H^G V)^*$ as representations of $G$. [Hint: Write $\operatorname{Ind}_H^G V$ as $k[G]_2\otimes_{k[H]}V$ and write $\operatorname{Ind}_H^G(V^*)$ as $\operatorname{Hom}_{k[H]}(k[G]_1,V^*)$. Prove that the map $\operatorname{Hom}_{k[H]}(k[G]_1,V^*)\times(\operatorname{Ind}_H^G(V^*))\to k$ given by $(f,(x\otimes_{k[H]}v))\mapsto(f(Sx))(v)$ is a nondegenerate $G$-invariant bilinear form, where $S:k[G]\to k[G]$ is the linear map defined by $Sg=g^{-1}$ for every $g\in G$.]

<span class="original-page-anchor" id="pdf-page-118" aria-hidden="true"></span>

## 5.11. Examples

Here are some examples of induced representations (we use the notation for representations from the character tables).

(1) Let $G=S_3$, $H=\mathbb Z_2$. Using the Frobenius reciprocity, we obtain $\operatorname{Ind}_H^G\mathbb C_+=\mathbb C^2\oplus\mathbb C_+$ and $\operatorname{Ind}_H^G\mathbb C_-=\mathbb C^2\oplus\mathbb C_-$.

(2) Let $G=S_3$, $H=\mathbb Z_3$. Then we obtain $\operatorname{Ind}_H^G\mathbb C_+=\mathbb C_+\oplus\mathbb C_-$, $\operatorname{Ind}_H^G\mathbb C_\varepsilon=\operatorname{Ind}_H^G\mathbb C_{\varepsilon^2}=\mathbb C^2$.

(3) Let $G=S_4$, $H=S_3$. Then $\operatorname{Ind}_H^G\mathbb C_+=\mathbb C_+\oplus\mathbb C_-^3$, $\operatorname{Ind}_H^G\mathbb C_-=\mathbb C_-\oplus\mathbb C_+^3$, $\operatorname{Ind}_H^G\mathbb C^2=\mathbb C^2\oplus\mathbb C_-^3\oplus\mathbb C_+^3$.

**Problem 5.11.1.** Compute the decomposition into irreducibles of all the representations of $A_5$ induced from the irreducible representations of

(a) $\mathbb Z_2$;

(b) $\mathbb Z_3$;

(c) $\mathbb Z_5$;

(d) $A_4$;

(e) $\mathbb Z_2\times\mathbb Z_2$.

## 5.12. Representations of $S_n$

In this subsection we give a description of the representations of the symmetric group $S_n$ for any $n$.

**Definition 5.12.1.** A **partition** $\lambda$ of $n$ is a representation of $n$ in the form $n=\lambda_1+\lambda_2+\cdots+\lambda_p$, where $\lambda_i$ are positive integers and $\lambda_i\ge\lambda_{i+1}$.

To such $\lambda$ we will attach a **Young diagram** $Y_\lambda$, which is the union of rectangles $-i\le y\le-i+1$, $0\le x\le\lambda_i$ in the coordinate plane, for $i=1,\ldots,p$. Clearly, $Y_\lambda$ is a collection of $n$ unit squares. A **Young tableau** corresponding to $Y_\lambda$ is the result of filling the numbers $1,\ldots,n$ into the squares of $Y_\lambda$ in some way (without repetitions). For example, we will consider the Young tableau $T_\lambda$ obtained by filling in the numbers in increasing order, left to right, top to bottom.

We can define two subgroups of $S_n$ corresponding to $T_\lambda$:

<span class="original-page-anchor" id="pdf-page-119" aria-hidden="true"></span>

1. The row subgroup $P_\lambda$: the subgroup which maps every element of $\{1,\ldots,n\}$ into an element standing in the same row in $T_\lambda$.

2. The column subgroup $Q_\lambda$: the subgroup which maps every element of $\{1,\ldots,n\}$ into an element standing in the same column in $T_\lambda$.

Clearly, $P_\lambda\cap Q_\lambda=\{1\}$.

Define the **Young projectors**

$$
a_\lambda:=\frac{1}{|P_\lambda|}\sum_{g\in P_\lambda}g,
$$

$$
b_\lambda:=\frac{1}{|Q_\lambda|}\sum_{g\in Q_\lambda}(-1)^g g,
$$

where $(-1)^g$ denotes the sign of the permutation $g$. Set $c_\lambda=a_\lambda b_\lambda$. Since $P_\lambda\cap Q_\lambda=\{1\}$, this element is nonzero.

The irreducible representations of $S_n$ are described by the following theorem.

**Theorem 5.12.2.** The subspace $V_\lambda:=\mathbb C[S_n]c_\lambda$ of $\mathbb C[S_n]$ is an irreducible representation of $S_n$ under left multiplication. Every irreducible representation of $S_n$ is isomorphic to $V_\lambda$ for a unique $\lambda$.

The modules $V_\lambda$ are called the **Specht modules**.

The proof of this theorem is given in the next subsection.

**Example 5.12.3.** For the partition $\lambda=(n)$, $P_\lambda=S_n$, $Q_\lambda=\{1\}$, so $c_\lambda$ is the symmetrizer, and hence $V_\lambda$ is the trivial representation.

For the partition $\lambda=(1,\ldots,1)$, $Q_\lambda=S_n$, $P_\lambda=\{1\}$, so $c_\lambda$ is the antisymmetrizer, and hence $V_\lambda$ is the sign representation.

$n=3$. For $\lambda=(2,1)$, $V_\lambda=\mathbb C^2$.

$n=4$. For $\lambda=(2,2)$, $V_\lambda=\mathbb C^2$; for $\lambda=(3,1)$, $V_\lambda=\mathbb C_-^3$; for $\lambda=(2,1,1)$, $V_\lambda=\mathbb C_+^3$.

**Corollary 5.12.4.** All irreducible representations of $S_n$ can be given by matrices with rational entries.

**Problem 5.12.5.** Find the sum of dimensions of all irreducible representations of the symmetric group $S_n$.

<span class="original-page-anchor" id="pdf-page-120" aria-hidden="true"></span>

Hint: Show that all irreducible representations of $S_n$ are real, i.e., admit a nondegenerate invariant symmetric form. Then use the Frobenius–Schur theorem.

## 5.13. Proof of the classification theorem for representations of $S_n$

**Lemma 5.13.1.** Let $x\in\mathbb C[S_n]$. Then $a_\lambda x b_\lambda=\ell_\lambda(x)c_\lambda$, where $\ell_\lambda$ is a linear function.

**Proof.** If $g\in P_\lambda Q_\lambda$, then $g$ has a unique representation as $pq$, $p\in P_\lambda$, $q\in Q_\lambda$, so $a_\lambda g b_\lambda=(-1)^q c_\lambda$. Thus, to prove the required statement, we need to show that if $g$ is a permutation which is not in $P_\lambda Q_\lambda$, then $a_\lambda g b_\lambda=0$.

To show this, it is sufficient to find a transposition $t$ such that $t\in P_\lambda$ and $g^{-1}tg\in Q_\lambda$; then

$$
a_\lambda g b_\lambda=a_\lambda t g b_\lambda=a_\lambda g(g^{-1}tg)b_\lambda=-a_\lambda g b_\lambda,
$$

so $a_\lambda g b_\lambda=0$. In other words, we have to find two elements $i,j$ standing in the same row in the tableau $T=T_\lambda$ and in the same column in the tableau $T'=gT$ (where $gT$ is the tableau of the same shape as $T$ obtained by permuting the entries of $T$ by the permutation $g$). Thus, it suffices to show that if such a pair does not exist, then $g\in P_\lambda Q_\lambda$, i.e., there exists $p\in P_\lambda$, $q'\in Q'_\lambda:=gQ_\lambda g^{-1}$ such that $pT=q'T'$ (so that $g=pq^{-1}$, $q=g^{-1}q'g\in Q_\lambda$).

Any two elements in the first row of $T$ must be in different columns of $T'$, so there exists $q'_1\in Q'_\lambda$ which moves all these elements to the first row. So there is $p_1\in P_\lambda$ such that $p_1T$ and $q'_1T'$ have the same first row. Now do the same procedure with the second row, finding elements $p_2,q'_2$ such that $p_2p_1T$ and $q'_2q'_1T'$ have the same first two rows. Continuing so, we will construct the desired elements $p,q'$. The lemma is proved. $\square$

Let us introduce the **lexicographic ordering** on partitions: $\lambda>\mu$ if the first nonvanishing $\lambda_i-\mu_i$ is positive.

**Lemma 5.13.2.** If $\lambda>\mu$, then $a_\lambda\mathbb C[S_n]b_\mu=0$.

<span class="original-page-anchor" id="pdf-page-121" aria-hidden="true"></span>

**Proof.** Similarly to the previous lemma, it suffices to show that for any $g\in S_n$ there exists a transposition $t\in P_\lambda$ such that $g^{-1}tg\in Q_\mu$. Let $T=T_\lambda$ and $T'=gT_\mu$. We claim that there are two integers which are in the same row of $T$ and the same column of $T'$. Indeed, if $\lambda_1>\mu_1$, this is clear by the pigeonhole principle (already for the first row). Otherwise, if $\lambda_1=\mu_1$, as in the proof of the previous lemma, we can find elements $p_1\in P_\lambda$, $q'_1\in gQ_\mu g^{-1}$ such that $p_1T$ and $q'_1T'$ have the same first row and repeat the argument for the second row, and so on. Eventually, having done $i-1$ such steps, we’ll have $\lambda_i>\mu_i$, which means that some two elements of the $i$th row of the first tableau are in the same column of the second tableau, completing the proof. $\square$

**Lemma 5.13.3.** $c_\lambda$ is proportional to an idempotent. Namely, $c_\lambda^2=\frac{n!}{\dim V_\lambda}c_\lambda$.

**Proof.** Lemma 5.13.1 implies that $c_\lambda^2$ is proportional to $c_\lambda$. Also, it is easy to see that the trace of $c_\lambda$ in the regular representation is $n!$ (as the coefficient of the identity element in $c_\lambda$ is $1$). This implies the statement. $\square$

**Lemma 5.13.4.** Let $A$ be an algebra and let $e$ be an idempotent in $A$. Then for any left $A$-module $M$, one has $\operatorname{Hom}_A(Ae,M)\cong eM$ (namely, $x\in eM$ corresponds to $f_x:Ae\to M$ given by $f_x(a)=ax$, $a\in Ae$).

**Proof.** Note that $1-e$ is also an idempotent in $A$. Thus the statement immediately follows from the fact that $\operatorname{Hom}_A(A,M)\cong M$ and the decomposition $A=Ae\oplus A(1-e)$. $\square$

Now we are ready to prove Theorem 5.12.2. Let $\lambda\ge\mu$. Then by Lemmas 5.13.3 and 5.13.4

$$
\operatorname{Hom}_{S_n}(V_\lambda,V_\mu)=\operatorname{Hom}_{S_n}(\mathbb C[S_n]c_\lambda,\mathbb C[S_n]c_\mu)=c_\lambda\mathbb C[S_n]c_\mu.
$$

The latter space is zero for $\lambda>\mu$ by Lemma 5.13.2 and 1-dimensional if $\lambda=\mu$ by Lemmas 5.13.1 and 5.13.3. Therefore, $V_\lambda$ are irreducible, and $V_\lambda$ is not isomorphic to $V_\mu$ if $\lambda\ne\mu$. Since the number of partitions equals the number of conjugacy classes in $S_n$, the representations $V_\lambda$ exhaust all the irreducible representations of $S_n$. The theorem is proved.

<span class="original-page-anchor" id="pdf-page-122" aria-hidden="true"></span>

## 5.14. Induced representations for $S_n$

Denote by $U_\lambda$ the representation $\operatorname{Ind}_{P_\lambda}^{S_n}\mathbb C$. It is easy to see that $U_\lambda$ can be alternatively defined as $U_\lambda=\mathbb C[S_n]a_\lambda$.

**Proposition 5.14.1.** We have $\operatorname{Hom}(U_\lambda,V_\mu)=0$ for $\mu<\lambda$ and $\dim\operatorname{Hom}(U_\lambda,V_\lambda)=1$. Thus, $U_\lambda=\bigoplus_{\mu\ge\lambda}K_{\mu\lambda}V_\mu$, where $K_{\mu\lambda}$ are nonnegative integers and $K_{\lambda\lambda}=1$.

**Definition 5.14.2.** The integers $K_{\mu\lambda}$ are called the **Kostka numbers**.

**Proof.** By Lemmas 5.13.3 and 5.13.4,

$$
\operatorname{Hom}(U_\lambda,V_\mu)=\operatorname{Hom}(\mathbb C[S_n]a_\lambda,\mathbb C[S_n]a_\mu b_\mu)=a_\lambda\mathbb C[S_n]a_\mu b_\mu,
$$

and the result follows from Lemmas 5.13.1 and 5.13.2. $\square$

Now let us compute the character of $U_\lambda$. Let $C_{\mathbf i}$ be the conjugacy class in $S_n$ having $i_l$ cycles of length $l$ for all $l\ge1$ (here $\mathbf i$ is a shorthand notation for $(i_1,\ldots,i_l,\ldots)$). Also let $x_1,\ldots,x_N$ be variables, and let

$$
H_m(x)=\sum_i x_i^m
$$

be the power sum polynomials.

**Theorem 5.14.3.** Let $N\ge p$ (where $p$ is the number of parts of $\lambda$). Then $\chi_{U_\lambda}(C_{\mathbf i})$ is the coefficient[^pdf122-1] of $x^\lambda:=\prod_j x_j^{\lambda_j}$ in the polynomial

$$
\prod_{m\ge1}H_m(x)^{i_m}.
$$

**Proof.** The proof is obtained easily from the Frobenius formula. Namely, $\chi_{U_\lambda}(C_{\mathbf i})$ is the number of elements $x\in S_n$ such that $xgx^{-1}\in P_\lambda$ (for a representative $g\in C_{\mathbf i}$), divided by $|P_\lambda|$. The order of $P_\lambda$ is $\prod_i\lambda_i!$, and the number of elements $x$ such that $xgx^{-1}\in P_\lambda$ is the number of elements in $P_\lambda$ conjugate to $g$ (i.e., $|C_{\mathbf i}\cap P_\lambda|$) times the order of the centralizer $Z_g$ of $g$ (which is $n!/|C_{\mathbf i}|$). Thus,

$$
\chi_{U_\lambda}(C_{\mathbf i})=\frac{|Z_g|}{\prod_j\lambda_j!}|C_{\mathbf i}\cap P_\lambda|.
$$

<span class="original-page-anchor" id="pdf-page-123" aria-hidden="true"></span>

Now, it is easy to see that the centralizer $Z_g$ of $g$ is isomorphic to

$$
\prod_m\bigl(S_{i_m}\ltimes(\mathbb Z/m\mathbb Z)^{i_m}\bigr),
$$

so

$$
|Z_g|=\prod_m m^{i_m}i_m!,
$$

and we get

$$
\chi_{U_\lambda}(C_{\mathbf i})=\frac{\prod_m m^{i_m}i_m!}{\prod_j\lambda_j!}|C_{\mathbf i}\cap P_\lambda|.
$$

Now, since $P_\lambda=\prod_j S_{\lambda_j}$, we have

$$
|C_{\mathbf i}\cap P_\lambda|=\sum_r\prod_{j\ge1}\frac{\lambda_j!}{\prod_{m\ge1}m^{r_{jm}}r_{jm}!},
$$

where $r=(r_{jm})$ runs over all collections of nonnegative integers such that

$$
\sum_m mr_{jm}=\lambda_j,\qquad\sum_j r_{jm}=i_m.
$$

Indeed, an element of $C_{\mathbf i}$ that is in $P_\lambda$ would define an ordered partition of each $\lambda_j$ into parts (namely, cycle lengths), with $m$ occurring $r_{jm}$ times, such that the total (over all $j$) number of times each part $m$ occurs is $i_m$. Thus we get

$$
\chi_{U_\lambda}(C_{\mathbf i})=\sum_r\prod_m\frac{i_m!}{\prod_j r_{jm}!}.
$$

But this is exactly the coefficient of $x^\lambda$ in

$$
\prod_{m\ge1}(x_1^m+\cdots+x_N^m)^{i_m}
$$

($r_{jm}$ is the number of times we take $x_j^m$). $\square$

## 5.15. The Frobenius character formula

Let $\Delta(x)=\prod_{1\le i<j\le N}(x_i-x_j)$. Let $\rho=(N-1,N-2,\ldots,0)\in\mathbb C^N$. The following theorem, due to Frobenius, gives a character formula for the Specht modules $V_\lambda$.

<span class="original-page-anchor" id="pdf-page-124" aria-hidden="true"></span>

**Theorem 5.15.1.** Let $N\ge p$. Then $\chi_{V_\lambda}(C_{\mathbf i})$ is the coefficient of $x^{\lambda+\rho}:=\prod_j x_j^{\lambda_j+N-j}$ in the polynomial

$$
\Delta(x)\prod_{m\ge1}H_m(x)^{i_m}.
$$

**Remark 5.15.2.** Here is an equivalent formulation of Theorem 5.15.1: $\chi_{V_\lambda}(C_{\mathbf i})$ is the coefficient of $x^\lambda$ in the (Laurent) polynomial

$$
\prod_{i<j}\left(1-\frac{x_j}{x_i}\right)\prod_{m\ge1}H_m(x)^{i_m}.
$$

**Proof.** For brevity denote $\chi_{V_\lambda}$ by $\chi_\lambda$. Let us denote the class function defined in the theorem by $\theta_\lambda$. We claim that this function has the property $\theta_\lambda=\sum_{\mu\ge\lambda}L_{\mu\lambda}\chi_\mu$, where $L_{\mu\lambda}$ are integers and $L_{\lambda\lambda}=1$. Indeed, from Theorem 5.14.3 we have

$$
\theta_\lambda=\sum_{\sigma\in S_N}(-1)^\sigma\chi_{U_{\lambda+\rho-\sigma(\rho)}},
$$

where if the vector $\lambda+\rho-\sigma(\rho)$ has a negative entry, the corresponding term is dropped, and if it has nonnegative entries which fail to be nonincreasing, then the entries should be reordered in nonincreasing order, making a partition that we’ll denote by $\langle\lambda+\rho-\sigma(\rho)\rangle$ (i.e., we agree that $U_{\lambda+\rho-\sigma(\rho)}:=U_{\langle\lambda+\rho-\sigma(\rho)\rangle}$). Now note that $\mu=\langle\lambda+\rho-\sigma(\rho)\rangle$ is obtained from $\lambda$ by adding vectors of the form $e_i-e_j$, $i<j$, which implies that $\mu>\lambda$ or $\mu=\lambda$, and the case $\mu=\lambda$ arises only if $\sigma=1$, as desired.

Therefore, to show that $\theta_\lambda=\chi_\lambda$, by Lemma 5.7.2, it suffices to show that $(\theta_\lambda,\theta_\lambda)=1$.

We have

$$
(\theta_\lambda,\theta_\lambda)=\frac{1}{n!}\sum_{\mathbf i}|C_{\mathbf i}|\theta_\lambda(C_{\mathbf i})^2.
$$

Using that

$$
|C_{\mathbf i}|=\frac{n!}{\prod_m m^{i_m}i_m!},
$$

we conclude that $(\theta_\lambda,\theta_\lambda)$ is the coefficient of $x^{\lambda+\rho}y^{\lambda+\rho}$ in the series $R(x,y)=\Delta(x)\Delta(y)S(x,y)$, where

$$
\begin{aligned}
S(x,y)&=\sum_{\mathbf i}\prod_m\frac{(\sum_j x_j^m)^{i_m}(\sum_k y_k^m)^{i_m}}{m^{i_m}i_m!}\\
&=\sum_{\mathbf i}\prod_m\frac{(\sum_{j,k}x_j^m y_k^m/m)^{i_m}}{i_m!}.
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-125" aria-hidden="true"></span>

Summing over $\mathbf i$ and $m$, we get

$$
\begin{aligned}
S(x,y)&=\prod_m\exp\left(\sum_{j,k}x_j^m y_k^m/m\right)\\
&=\exp\left(-\sum_{j,k}\log(1-x_jy_k)\right)=\prod_{j,k}(1-x_jy_k)^{-1}.
\end{aligned}
$$

Thus,

$$
R(x,y)=\frac{\prod_{i<j}(x_i-x_j)(y_i-y_j)}{\prod_{i,j}(1-x_i y_j)}.
$$

Now we need the following lemma.

**Lemma 5.15.3.**

$$
\frac{\prod_{i<j}(z_j-z_i)(y_i-y_j)}{\prod_{i,j}(z_i-y_j)}=\det\left(\frac{1}{z_i-y_j}\right).
$$

**Proof.** Multiply both sides by $\prod_{i,j}(z_i-y_j)$. Then the right-hand side must vanish on the hyperplanes $z_i=z_j$ and $y_i=y_j$ (i.e., must be divisible by $\Delta(z)\Delta(y)$) and is a homogeneous polynomial of degree $N(N-1)$. This implies that the right-hand side and the left-hand side are proportional. The proportionality coefficient (which is equal to $1$) is found by induction by multiplying both sides by $z_N-y_N$ and then setting $z_N=y_N$. $\square$

Now setting $z_i=1/x_i$ in the lemma, we get

**Corollary 5.15.4 (Cauchy identity).**

$$
R(x,y)=\det\left(\frac{1}{1-x_i y_j}\right)=\sum_{\sigma\in S_N}\frac{1}{\prod_{j=1}^N(1-x_j y_{\sigma(j)})}.
$$

Corollary 5.15.4 easily implies that the coefficient of $x^{\lambda+\rho}y^{\lambda+\rho}$ is $1$. Indeed, if $\sigma\ne1$ is a permutation in $S_N$, the coefficient of this monomial in $\frac{1}{\prod_j(1-x_jy_{\sigma(j)})}$ is obviously zero. $\square$

**Remark 5.15.5.** For partitions $\lambda$ and $\mu$ of $n$, let us say that $\lambda\preceq\mu$ or $\mu\succeq\lambda$ if $\mu-\lambda$ is a sum of vectors of the form $e_i-e_j$, $i<j$ (called positive roots). This is a partial order, and $\mu\succ\lambda$ implies $\mu>\lambda$. It follows from Theorem 5.15.1 and its proof that

$$
\chi_\lambda=\sum_{\mu\succeq\lambda}\widetilde K_{\mu\lambda}\chi_{U_\mu},
$$

<span class="original-page-anchor" id="pdf-page-126" aria-hidden="true"></span>

where $(\widetilde K_{\lambda\mu})$ is the matrix inverse to the matrix of Kostka numbers $(K_{\lambda\mu})$. This implies that the Kostka numbers $K_{\mu\lambda}$ vanish unless $\mu\succeq\lambda$.

## 5.16. Problems

In the following problems, we do not make a distinction between Young diagrams and partitions.

**Problem 5.16.1.** For a Young diagram $\mu$, let $A(\mu)$ be the set of Young diagrams obtained by adding a square to $\mu$, and let $R(\mu)$ be the set of Young diagrams obtained by removing a square from $\mu$.

(a) Show that $\operatorname{Res}_{S_{n-1}}^{S_n}V_\mu=\bigoplus_{\lambda\in R(\mu)}V_\lambda$.

(b) Show that $\operatorname{Ind}_{S_{n-1}}^{S_n}V_\mu=\bigoplus_{\lambda\in A(\mu)}V_\lambda$.

**Problem 5.16.2.** The **content** $c(\lambda)$ of a Young diagram $\lambda$ is the sum $\sum_j\sum_{i=1}^{\lambda_j}(i-j)$. Let $C=\sum_{i<j}(ij)\in\mathbb C[S_n]$ be the sum of all transpositions. Show that $C$ acts on the Specht module $V_\lambda$ by multiplication by $c(\lambda)$.

**Problem 5.16.3.** (a) Let $V$ be any finite dimensional representation of $S_n$. Show that the element $E:=(12)+\cdots+(1n)$ is diagonalizable and has integer eigenvalues on $V$ which are between $1-n$ and $n-1$.

Hint: Represent $E$ as $C_n-C_{n-1}$, where $C_n=C$ is the element from Problem 5.16.2.

(b) Show that the element $(12)+\cdots+(1n)$ acts on $V_\lambda$ by a scalar if and only if $\lambda$ is a rectangular Young diagram, and compute this scalar.

## 5.17. The hook length formula

Let us use the Frobenius character formula to compute the dimension of $V_\lambda$. According to the character formula, $\dim V_\lambda$ is the coefficient of $x^{\lambda+\rho}$ in $\Delta(x)(x_1+\cdots+x_N)^n$. Let $l_j=\lambda_j+N-j$. Then, using the determinant formula for $\Delta(x)$ and expanding the determinant as <span class="original-page-anchor" id="pdf-page-127" aria-hidden="true"></span>a sum over permutations, we get

$$
\begin{aligned}
\dim V_\lambda
&=\sum_{\substack{s\in S_N:\\l_j\ge N-s(j)}}(-1)^s\frac{n!}{\prod_j(l_j-N+s(j))!}\\
&=\frac{n!}{l_1!\cdots l_N!}\sum_{s\in S_N}(-1)^s\prod_j l_j(l_j-1)\cdots(l_j-N+s(j)+1)\\
&=\frac{n!}{\prod_j l_j!}\det\bigl(l_j(l_j-1)\cdots(l_j-N+i+1)\bigr).
\end{aligned}
$$

Using column reduction and the Vandermonde determinant formula, we see from this expression that

$$
\dim V_\lambda=\frac{n!}{\prod_j l_j!}\det(l_j^{N-i})=\frac{n!}{\prod_j l_j!}\prod_{1\le i<j\le N}(l_i-l_j).\tag{5.17.1}
$$

(where $N\ge p$).

In this formula, there are many cancellations. After making some of these cancellations, we obtain the hook length formula. Namely, for a square $(i,j)$ in a Young diagram $\lambda$ ($i,j\ge1$, $i\le\lambda_j$), define the **hook** of $(i,j)$ to be the set of all squares $(i',j')$ in $\lambda$ with $i'\ge i$, $j'=j$ or $i'=i$, $j'\ge j$. Let $h(i,j)$ be the length of the hook of $i,j$, i.e., the number of squares in it.

**Theorem 5.17.1 (The hook length formula).** One has

$$
\dim V_\lambda=\frac{n!}{\prod_{i\le\lambda_j}h(i,j)}.
$$

**Proof.** The formula follows from formula (5.17.1). Namely, note that

$$
\frac{l_1!}{\prod_{1<j\le N}(l_1-l_j)}=\prod_{\substack{1\le k\le l_1,\\k\ne l_1-l_j}}k.
$$

It is easy to see that the factors in this product are exactly the hook lengths $h(i,1)$. Now delete the first row of the diagram and proceed by induction. $\square$

## 5.18. Schur–Weyl duality for $\mathfrak{gl}(V)$

We start with a simple result which is called the **Double Centralizer Theorem**.

<span class="original-page-anchor" id="pdf-page-128" aria-hidden="true"></span>

**Theorem 5.18.1.** Let $A,B$ be two subalgebras of the algebra $\operatorname{End}E$ of endomorphisms of a finite dimensional vector space $E$, such that $A$ is semisimple and $B=\operatorname{End}_A E$. Then:

(i) $A=\operatorname{End}_B E$ (i.e., the centralizer of the centralizer of $A$ is $A$).

(ii) $B$ is semisimple.

(iii) As a representation of $A\otimes B$, $E$ decomposes as

$$
E=\bigoplus_{i\in I}V_i\otimes W_i,
$$

where $V_i$ are all the irreducible representations of $A$ and $W_i$ are all the irreducible representations of $B$. In particular, we have a natural bijection between irreducible representations of $A$ and $B$.

**Proof.** Since $A$ is semisimple, we have a natural decomposition $E=\bigoplus_{i\in I}V_i\otimes W_i$, where $W_i:=\operatorname{Hom}_A(V_i,E)$ and $A=\bigoplus_i\operatorname{End}V_i$. Therefore, by Schur’s lemma, $B=\operatorname{End}_A(E)$ is naturally identified with $\bigoplus_i\operatorname{End}(W_i)$. This implies all the statements of the theorem. $\square$

We will now apply Theorem 5.18.1 to the following situation: $E=V^{\otimes n}$, where $V$ is a finite dimensional vector space over a field of characteristic zero and $A$ is the image of $\mathbb C[S_n]$ in $\operatorname{End}E$. Let us now characterize the algebra $B$. Let $\mathfrak{gl}(V)$ be $\operatorname{End}V$ regarded as a Lie algebra with operation $ab-ba$.

**Theorem 5.18.2.** The algebra $B=\operatorname{End}_A E$ is the image of the universal enveloping algebra $\mathcal U(\mathfrak{gl}(V))$ under its natural action on $E$. In other words, $B$ is generated by elements of the form

$$
\Delta_n(b):=b\otimes1\otimes\cdots\otimes1+1\otimes b\otimes\cdots\otimes1+\cdots+1\otimes1\otimes\cdots\otimes b,
$$

$b\in\mathfrak{gl}(V)$.

**Proof.** Clearly, the image of $\mathcal U(\mathfrak{gl}(V))$ is contained in $B$, so we just need to show that any element of $B$ is contained in the image of $\mathcal U(\mathfrak{gl}(V))$. By definition, $B=S^n\operatorname{End}V$, so the result follows from part (ii) of the following lemma.

**Lemma 5.18.3.** Let $k$ be a field of characteristic zero.

<span class="original-page-anchor" id="pdf-page-129" aria-hidden="true"></span>

(i) For any finite dimensional vector space $U$ over $k$, the space $S^nU$ is spanned by elements of the form $u\otimes\cdots\otimes u$, $u\in U$.

(ii) For any algebra $A$ over $k$, the algebra $S^nA$ is generated by elements $\Delta_n(a)$, $a\in A$.

**Proof.** (i) The space $S^nU$ is an irreducible representation of $GL(U)$ (Problem 4.12.3). The subspace spanned by $u\otimes\cdots\otimes u$ is a nonzero subrepresentation, so it must be everything.

(ii) By the fundamental theorem on symmetric functions, there exists a polynomial $P$ with rational coefficients such that

$$
P(H_1(x),\ldots,H_n(x))=x_1\cdots x_n
$$

(where $x=(x_1,\ldots,x_n)$). Then

$$
P(\Delta_n(a),\Delta_n(a^2),\ldots,\Delta_n(a^n))=a\otimes\cdots\otimes a.
$$

The rest follows from (i). $\square$

This completes the proof of the theorem. $\square$

Now, the algebra $A$ is semisimple by Maschke's theorem, so the double centralizer theorem applies, and we get the following result, which goes under the name “Schur–Weyl duality” (as it was discovered by Schur and popularized by Weyl in his books *The theory of groups and quantum mechanics* and *Classical groups*; see Section 5.20).

**Theorem 5.18.4.** (i) The image $A$ of $\mathbb C[S_n]$ and the image $B$ of $\mathcal U(\mathfrak{gl}(V))$ in $\operatorname{End}(V^{\otimes n})$ are centralizers of each other.

(ii) Both $A$ and $B$ are semisimple. In particular, $V^{\otimes n}$ is a semisimple $\mathfrak{gl}(V)$-module.

(iii) We have a decomposition of $(A\otimes B)$-modules

$$
V^{\otimes n}=\bigoplus_\lambda V_\lambda\otimes L_\lambda,
$$

where the summation is taken over partitions of $n$, $V_\lambda$ are Specht modules for $S_n$, and $L_\lambda$ are some distinct irreducible representations of $\mathfrak{gl}(V)$ or zero.

<span class="original-page-anchor" id="pdf-page-130" aria-hidden="true"></span>

## 5.19. Schur–Weyl duality for $GL(V)$

The Schur–Weyl duality for the Lie algebra $\mathfrak{gl}(V)$ implies a similar statement for the group $GL(V)$.

**Proposition 5.19.1.** The image of $GL(V)$ in $\operatorname{End}(V^{\otimes n})$ spans $B$.

**Proof.** Denote the span of $g^{\otimes n}$, $g\in GL(V)$, by $B'$. Let $b\in\operatorname{End}V$ be any element.

We claim that $B'$ contains $b^{\otimes n}$. Indeed, for all values of $t$ but finitely many, $t\cdot\mathrm{Id}+b$ is invertible, so $(t\cdot\mathrm{Id}+b)^{\otimes n}$ belongs to $B'$. This implies that this is true for all $t$, in particular for $t=0$, since $(t\cdot\mathrm{Id}+b)^{\otimes n}$ is a polynomial in $t$.

The rest follows from Lemma 5.18.3. $\square$

**Corollary 5.19.2.** As a representation of $S_n\times GL(V)$, $V^{\otimes n}$ decomposes as $\bigoplus_\lambda V_\lambda\otimes L_\lambda$, where $L_\lambda=\operatorname{Hom}_{S_n}(V_\lambda,V^{\otimes n})$ are distinct irreducible representations of $GL(V)$ or zero.

**Example 5.19.3.** If $\lambda=(n)$, then $L_\lambda=S^nV$, and if $\lambda=(1^n)$ ($n$ copies of $1$), then $L_\lambda=\wedge^nV$. It was shown in Problem 4.12.3 that these representations are indeed irreducible (except that $\wedge^nV$ is zero if $n>\dim V$).

## 5.20. Historical interlude: Hermann Weyl at the intersection of limitation and freedom

Hermann Weyl (1885–1955) received his doctorate at the University of Göttingen under the guidance of David Hilbert, whom he later paid a rather dubious compliment by calling him “the Pied Piper …seducing so many rats to follow him into the deep river of mathematics”. Hilbert called mathematical physics “a vital nerve” of mathematics, and Weyl inherited the interest in cross-fertilization of mathematics and physics from his teacher (quoted in [53, pp. 357, 358]). The willingness of Göttingen mathematicians to get their formulas dirty by engaging physical problems set them apart from the obsessive purism of the Berlin mathematical school.

<span class="original-page-anchor" id="pdf-page-131" aria-hidden="true"></span>

In 1913 Weyl was offered a professorship at the ETH in Zurich, despite a somewhat lukewarm endorsement from Frobenius, who regarded the work of all candidates who came from the Göttingen school as “very general, very deep, so abysmally deep that a shortsighted person like me finds it difficult to recognize new ideas” (quoted in [22, p. 421]). Weyl accepted and found himself in the company of Albert Einstein, who was teaching at the ETH at the time. Yet it took a world war to make Weyl pay attention to what Einstein was doing. The German government initially judged Weyl unfit to fight in World War I, but as losses were mounting, it reevaluated the concept of physical fitness and dragged him onto the battlefield. Weyl's encounter with the German army brought little satisfaction to either side. In 1916, at the request of the Swiss government, Weyl was discharged and allowed to resume his work at the ETH. “My mathematical mind was as blank as any veteran's, and I did not know what to do”, he later recalled. “I began to study algebraic surfaces; but before I had gotten far, Einstein's memoir came into my hands and set me afire” (quoted in [52, p. 62]). The inflaming memoir was Einstein's account of general relativity.

In 1917 Weyl gave a lecture course on general relativity at the ETH and soon turned it into the widely read book *Space-Time-Matter*, which went through four different editions within five years and was admired by Einstein himself as a “symphonic masterpiece” (quoted in [46, p. 65]). Weyl, however, could hardly resist the impulse to improve on Einstein's belabored mathematics. He was convinced that Riemannian geometry, on which Einstein based his theory, was not a consistently infinitesimal geometry and set out to create a “purely infinitesimal geometry”. When he explained to a student that in Riemannian geometry the direction of the transported vector depended on the path, the student innocently asked whether the vector length changed as well. “Of course I gave him the orthodox answer at that moment, but in my bosom gnawed the doubt”, Weyl recalled (quoted in [52, p. 154]). The orthodox answer was *no*, but he was tempted to see what would happen if the length indeed depended on the path. Weyl questioned the assumption of a fixed distance scale, or “gauge”, implicit in Riemannian geometry, and arrived at a more general geometry, in which the gauge factor varied from point to point <span class="original-page-anchor" id="pdf-page-132" aria-hidden="true"></span>in space-time, just as railway gauge varied from country to country in the early 20th century [42, p. 3].

Weyl aspired at a unified field theory, bringing together the gravitational and the electromagnetic fields. Einstein was delighted to count Weyl among the supporters of general relativity but was less than enthusiastic to see him compete in the construction of physical theories. Einstein praised Weyl's theory as a “stroke of genius of the highest order” and concluded that “except for the agreement with reality it is in any case a grandiose achievement of thought” (quoted in [52, pp. 163–164]). As a true mathematician, Weyl could hardly share Einstein's obsession with “reality”. As he later argued, “[I]t becomes evident that now the words ‘in reality’ must be put between quotation marks; we have a symbolic construction, but nothing which we could seriously pretend to be the true real world” (quoted in [42, p. 15]). In his reply to Einstein, Weyl pointedly wrote: “It must be emphasized that the geometry that has been developed here is, from the mathematical viewpoint, the true local geometry. It would be strange if, instead of this true (geometry), a partial and inconsistent local geometry with the electromagnetic field glued to it were realized in Nature”. Weyl easily matched Einstein in the degree of his sarcasm: “If you are right with regard to the real world, then I regret having to point out a mathematical inconsistency to the dear Lord” (quoted in [22, p. 434]).

Recasting the tensor language of Einstein's general relativity in the mold of the Göttingen school, Weyl focused on the development of tensor algebra, particularly on tensors with specific symmetry properties relevant to physical applications. He aspired to obtain a mathematical overview of possible symmetry types and found an appropriate vantage point in Frobenius's theory of finite group representations. Gradually Weyl turned further away from relativity and towards purely mathematical questions of group theory, trying to develop a group-theoretical foundation of the tensor calculus. Drawing on the work of Élie Cartan and Issai Schur, Weyl delved into the representation theory of finite groups, which he called “one of the most wonderful theories to be found in mathematics”. Weyl exchanged <span class="original-page-anchor" id="pdf-page-133" aria-hidden="true"></span>letters with Schur, who wrote that “it would be of considerable interest to me to see how my latest results on the number of variables and characters could be derived on the basis of Cartan's methods” (quoted in [22, pp. 456, 473]). Weyl obliged and quickly arranged the marriage of Élie Cartan's infinitesimal methods with Issai Schur's integral procedure. He did not limit himself, however, to rederiving Schur's results but went somewhat further and developed an entire theory of the representations of simple Lie groups, including explicit formulas for the irreducible characters and for the degrees of the corresponding representations.

The rise of quantum mechanics provided an occasion for Weyl to mount an attack on the hegemonic status of the mathematical continuum. He believed that different branches of mathematics might have different concepts of the number and supported the view that “each object which is offered to mathematical analysis carries its own kind of numbers to be defined in terms of that object and its intrinsic constituents, instead of approaching every object by the same universal number system developed a priori and independently of the applications” (quoted in [52, p. 240]). In his 1928 book, *The Theory of Groups and Quantum Mechanics*, Weyl argued that the essence of symmetries central to quantum mechanics was to be found not in the continuum of real numbers but in the concepts of group theory, particularly in the “reciprocity” between the representations of symmetric permutation groups and complete linear groups [60, p. vii].

The physics community welcomed the help of a mathematician with cries of outrage and disgust. The American theoretical physicist John Slater christened the approach of Weyl and his followers “Gruppenpest”, or “the pest of group theory”. “The authors of the ‘Gruppenpest’ wrote papers which were incomprehensible to those like me who had not studied group theory”, he later confessed. Their results appeared “negligible” to him, and he widely shared his “frustrating experience, worthy of the name of a pest”, with other physicists, who were, as he claimed, “as disgusted as I had been with the group-theoretical approach to the problem” (quoted in [55, p. x]). As late <span class="original-page-anchor" id="pdf-page-134" aria-hidden="true"></span>as 1975, he still believed that he had “slain the ‘Gruppenfest’”, blissfully unaware of the essential and now routine applications of group theory in elementary particle physics.

More sympathetic physicists also had difficulty grappling with Weyl's mathematics, but this only heightened their admiration for him. Julian Schwinger had to admit that he had not “ever—not even to this day—fully mastered” Weyl's *Theory of Groups and Quantum Mechanics*. Yet he called Weyl “one of my gods”, explaining that “the ways of gods are mysterious, inscrutable, and beyond the comprehension of ordinary mortals”. When asked if he ever met a scholar he could not understand, Paul Dirac unhesitatingly replied, “Weyl”. Yet he found Weyl's—purely mathematical—argument that electrons and antielectrons must have the same mass so disarmingly convincing that he reportedly derived from this encounter his famous maxim, “[I]t is more important to have beauty in one's equations than to have them fit experiment” (quoted in [42, p. 11, 19, 12]). Weyl expressed a similar sentiment with respect to mathematics: “My work has always tried to unite the true with the beautiful, and when I had to choose one or the other, I usually chose the beautiful” (quoted in [45, p. 161]).

Weyl's return to Göttingen in 1930 to take up Hilbert's chair was badly timed to coincide with the Nazis' rise to power. One contemporary privately remarked, “Prof. Weyl is a peculiar race mixture, at least seven parts Holstein and one part Jewish blood with the particular vasomotor irritability that one encounters relatively often in people from Holstein and Friesland” (quoted in [49, p. 52]). Whatever vasomotor dysfunction may have resulted from the German components of his blood, it clearly paled in comparison with the trouble that his Jewish ancestry could cause him in Nazi Germany. Although Weyl's low Jewish blood count exempted him from the Nazis' direct attacks, his wife and children would have become targets of anti-Semitic measures. Having barely returned to his homeland, Weyl had to face the prospect of immigration again. The decision was difficult. At first he rejected an invitation to join the Princeton Institute for Advanced Study, unable to overcome “the love that binds me with every string of my heart to the German language” (quoted in [52, p.

<span class="original-page-anchor" id="pdf-page-135" aria-hidden="true"></span>

271]). But when Hitler came to power, Weyl's head prevailed over his heart, and his family left for America.

Upon his arrival at Princeton, Weyl plunged into a mathematical culture quite inhospitable to the speculative philosophy so dear to him. Weyl perceived the “danger of a too thorough specialization and technicalization” of American mathematical research that produced “a mode of writing which must give the reader the impression of being shut up in a brightly illuminated cell where every detail sticks out with the same dazzling clarity, but without relief”. Personally Weyl preferred “the open landscape under a clear sky with its depth of perspective, where the wealth of sharply defined nearby details gradually fades away toward the horizon” [57, p. viii].

In 1939, struggling with the “yoke of foreign language”, imposed upon his writing, Weyl summed up his results on group invariants and representations in the book *The Classical Groups* [57, p. viii]. As Sir Michael Atiyah has noted, this volume “is not a linear book with a beginning, middle, and end. It is more like an elaborate painting that has to be studied from different angles and in different lights. It is the despair of the student and the delight of the professor” [3, p. 328].

Weyl viewed his mathematical writings as works of art, as much as science. “My own mathematical works are always quite unsystematic, without mode or connection”, he admitted. “Expression and shape are almost more to me than knowledge itself. But I believe that, leaving aside my own peculiar nature, there is in mathematics itself, in contrast to the experimental disciplines, a character which is nearer to that of free creative art” (quoted in [3, p. 323]). Weyl believed that “‘mathematizing’ may well be a creative activity of man, like language or music, of primary originality, whose historical decisions defy complete objective rationalization” [58, p. 550].

In the artistry of mathematical creativity, in the beauty of formulas, in the eternal truths of mathematics sought Weyl a refuge from the horrors of the world wars and from the destruction of European culture [53, p. 365]. Yet after Hiroshima he realized that even pretty formulas may have deadly uses. “To what extent shall and can the theorist take responsibility for the practical consequences of his discoveries?” he asked. “What a beautiful theoretical edifice is quantum <span class="original-page-anchor" id="pdf-page-136" aria-hidden="true"></span>physics—and what a terrible thing is the atomic bomb!”. Weyl disagreed with G. H. Hardy's defense of pure mathematics as a useless and harmless pursuit of beauty. Weyl insisted that the very meaning and value of mathematics were questioned “by the deadly menace of its misuse” (quoted in [49, p. 67–68]). He saw in mathematics the same moral choices that one faced in real life. His earlier reflections on the “metaphysical implications” of knowledge now acquired a broader meaning. “Mathematics is not the rigid and uninspiring schematism which the layman is so apt to see in it”, he had written. “On the contrary, we stand in mathematics precisely at that point of intersection of limitation and freedom which is the essence of man himself” [59, p. 68].

## 5.21. Schur polynomials

Let $\lambda=(\lambda_1,\ldots,\lambda_p)$ be a partition of $n$, and let $N\geq p$. Let

$$
D_\lambda(x)=\sum_{s\in S_N}(-1)^s\prod_{j=1}^N x_{s(j)}^{\lambda_j+N-j}=\det(x_i^{\lambda_j+N-j}).
$$

Define the polynomials

$$
S_\lambda(x):=\frac{D_\lambda(x)}{D_0(x)}
$$

(clearly $D_0(x)$ is just $\Delta(x)$). It is easy to see that these are indeed polynomials, as $D_\lambda$ is antisymmetric and therefore must be divisible by $\Delta$. The polynomials $S_\lambda$ are called the **Schur polynomials**.

**Proposition 5.21.1.**

$$
\prod_m(x_1^m+\cdots+x_N^m)^{i_m}=\sum_{\lambda:p\leq N}\chi_\lambda(C_i)S_\lambda(x).
$$

**Proof.** The identity follows from the Frobenius character formula and the antisymmetry of

$$
\Delta(x)\prod_m(x_1^m+\cdots+x_N^m)^{i_m}.
$$

$\square$

Certain special values of Schur polynomials are of importance. Namely, we have

<span class="original-page-anchor" id="pdf-page-137" aria-hidden="true"></span>

**Proposition 5.21.2.**

$$
S_\lambda(1,z,z^2,\ldots,z^{N-1})=\prod_{1\leq i<j\leq N}\frac{z^{\lambda_i-i}-z^{\lambda_j-j}}{z^{-i}-z^{-j}}.
$$

Therefore,

$$
S_\lambda(1,\ldots,1)=\prod_{1\leq i<j\leq N}\frac{\lambda_i-\lambda_j+j-i}{j-i}.
$$

**Proof.** The first identity is obtained from the definition using the Vandermonde determinant. The second identity follows from the first one by setting $z=1$. $\square$

## 5.22. The characters of $L_\lambda$

Proposition 5.21.1 allows us to calculate the characters of the representations $L_\lambda$.

Namely, let $\dim V=N$, let $g\in GL(V)$, and let $x_1,\ldots,x_N$ be the eigenvalues of $g$ on $V$. To compute the character $\chi_{L_\lambda}(g)$, let us calculate $\operatorname{Tr}_{V^{\otimes n}}(g^{\otimes n}s)$, where $s\in S_n$. If $s\in C_i$, we easily get that this trace equals

$$
\prod_m\operatorname{Tr}(g^m)^{i_m}=\prod_m H_m(x)^{i_m}.
$$

On the other hand, by the Schur–Weyl duality

$$
\operatorname{Tr}_{V^{\otimes n}}(g^{\otimes n}s)=\sum_\lambda\chi_\lambda(C_i)\operatorname{Tr}_{L_\lambda}(g).
$$

Comparing this to Proposition 5.21.1 and using linear independence of columns of the character table of $S_n$, we obtain

**Theorem 5.22.1 (Weyl character formula).** The representation $L_\lambda$ is zero if and only if $N<p$, where $p$ is the number of parts of $\lambda$. If $N\geq p$, the character of $L_\lambda$ is the Schur polynomial $S_\lambda(x)$. Therefore, the dimension of $L_\lambda$ is given by the formula

$$
\dim L_\lambda=\prod_{1\leq i<j\leq N}\frac{\lambda_i-\lambda_j+j-i}{j-i}.
$$

<span class="original-page-anchor" id="pdf-page-138" aria-hidden="true"></span>

This shows that irreducible representations of $GL(V)$ which occur in $V^{\otimes n}$ for some $n$ are labeled by Young diagrams with any number of squares but at most $N=\dim V$ rows.

**Proposition 5.22.2.** The representation $L_{\lambda+1^N}$ (where $1^N=(1,1,\ldots,1)\in\mathbb Z^N$) is isomorphic to $L_\lambda\otimes\wedge^NV$.

**Proof.** Indeed, $L_\lambda\otimes\wedge^NV\subset V^{\otimes n}\otimes\wedge^NV\subset V^{\otimes(n+N)}$, and the only component of $V^{\otimes(n+N)}$ that has the same character as $L_\lambda\otimes\wedge^NV$ is $L_{\lambda+1^N}$. This implies the statement. $\square$

## 5.23. Algebraic representations of $GL(V)$

**Definition 5.23.1.** We say that a finite dimensional representation $Y$ of $GL(V)$ is **algebraic** (or **rational**, or **polynomial**) if its matrix elements are polynomial functions of the entries of $g,g^{-1}$, $g\in GL(V)$ (i.e., belong to $k[g_{ij}][1/\det(g)]$).

For example, $V^{\otimes n}$ and hence all $L_\lambda$ are algebraic. Also define $L_{\lambda-r\cdot1^N}:=L_\lambda\otimes(\wedge^NV^*)^{\otimes r}$ (this definition makes sense by Proposition 5.22.2). This is also an algebraic representation. Thus we have attached a unique irreducible algebraic representation $L_\lambda$ of $GL(V)=GL_N$ to any sequence $(\lambda_1,\ldots,\lambda_N)$ of integers (not necessarily positive) such that $\lambda_1\geq\cdots\geq\lambda_N$. This sequence is called the **highest weight** of $L_\lambda$.

**Theorem 5.23.2.** (i) Every finite dimensional algebraic representation of $GL(V)$ is completely reducible, and decomposes into summands of the form $L_\lambda$ (which are pairwise nonisomorphic).

(ii) (*The Peter–Weyl theorem for $GL(V)$*) Let $R$ be the algebra of polynomial functions on $GL(V)$. Then as a representation of $GL(V)\times GL(V)$ (with action $(\rho(g,h)\phi)(x)=\phi(g^{-1}xh)$, $g,h,x\in GL(V)$, $\phi\in R$), $R$ decomposes as

$$
R=\bigoplus_\lambda L_\lambda^*\otimes L_\lambda,
$$

where the summation runs over all $\lambda$.

**Proof.** (i) Let $Y$ be an algebraic representation of $GL(V)$. We have an embedding $\xi:Y\to Y\otimes R$ given by $(u,\xi(v))(g):=u(gv)$, $u\in Y^*$.

<span class="original-page-anchor" id="pdf-page-139" aria-hidden="true"></span>

It is easy to see that $\xi$ is a homomorphism of representations (where the action of $GL(V)$ on the first component of $Y\otimes R$ is trivial). Thus, it suffices to prove the theorem for a subrepresentation $Y\subset R^m$. Now, every element of $R$ is a polynomial of $g_{ij}$ times a nonpositive power of $\det(g)$. Thus, $R$ is a quotient of a direct sum of representations of the form $S^r(V\otimes V^*)\otimes(\wedge^NV^*)^{\otimes s}$. So we may assume that $Y$ is contained in a quotient of a (finite) direct sum of such representations. As $V^*=\wedge^{N-1}V\otimes\wedge^NV^*$, $Y$ is contained in a direct sum of representations of the form $V^{\otimes n}\otimes(\wedge^NV^*)^{\otimes s}$, and we are done.

(ii) Let $Y$ be an algebraic representation of $GL(V)$, and let us regard $R$ as a representation of $GL(V)$ via $(\rho(h)\phi)(x)=\phi(xh)$.

Then $\operatorname{Hom}_{GL(V)}(Y,R)$ is the space of polynomial functions $f$ on $GL(V)$ with values in $Y^*$ which are $GL(V)$-equivariant (i.e., such that $f(gx)=gf(x)$). This space is naturally identified with $Y^*$. Taking into account the proof of (i), we deduce that $R$ has the required decomposition, which is compatible with the second action of $GL(V)$ (by left multiplications). This implies the statement. $\square$

**Remark 5.23.3.** Since the Lie algebra $\mathfrak{sl}(V)$ of traceless operators on $V$ is a quotient of $\mathfrak{gl}(V)$ by scalars, the above results extend in a straightforward manner to representations of the Lie algebra $\mathfrak{sl}(V)$. Similarly, the results for $GL(V)$ extend to the case of the group $SL(V)$ of operators with determinant $1$. The only difference is that in this case the representations $L_\lambda$ and $L_{\lambda+1^m}$ are isomorphic, so the irreducible representations are parametrized by integer sequences $\lambda_1\geq\cdots\geq\lambda_N$ up to a simultaneous shift by a constant.

In particular, one can show that any finite dimensional representation of $\mathfrak{sl}(V)$ is completely reducible and any irreducible representation is of the form $L_\lambda$ (we will not do this here). For $\dim V=2$ one then recovers the representation theory of $\mathfrak{sl}(2)$ studied in Problem 2.15.1.

## 5.24. Problems

**Problem 5.24.1.** (a) Show that the $S_n$-representation

$$
V'_\lambda:=\mathbb C[S_n]b_\lambda a_\lambda
$$

is isomorphic to $V_\lambda$.

<span class="original-page-anchor" id="pdf-page-140" aria-hidden="true"></span>

Hint: Define $S_n$-homomorphisms $f:V_\lambda\to V'_\lambda$ and $g:V'_\lambda\to V_\lambda$ by the formulas $f(x)=xa_\lambda$ and $g(y)=yb_\lambda$, and show that they are inverse to each other up to a nonzero scalar.

(b) Let $\phi:\mathbb C[S_n]\to\mathbb C[S_n]$ be the automorphism sending $s$ to $(-1)^ss$ for any permutation $s$. Show that $\phi$ maps any representation $V$ of $S_n$ to $V\otimes\mathbb C_-$. Show also that $\phi(\mathbb C[S_n]a)=\mathbb C[S_n]\phi(a)$, for $a\in\mathbb C[S_n]$. Use (a) to deduce that $V_\lambda\otimes\mathbb C_-=V_{\lambda^*}$, where $\lambda^*$ is the conjugate partition to $\lambda$, obtained by reflecting the Young diagram of $\lambda$.

**Problem 5.24.2.** Let $R_{k,N}$ be the algebra of polynomials on the space of $k$-tuples of complex $N\times N$ matrices $X_1,\ldots,X_k$, invariant under simultaneous conjugation. An example of an element of $R_{k,N}$ is the function $T_w:=\operatorname{Tr}(w(X_1,\ldots,X_k))$, where $w$ is any finite word on a $k$-letter alphabet. Show that $R_{k,N}$ is generated by the elements $T_w$.

Hint: Consider invariant functions that are of degree $d_i$ in each $X_i$, and realize this space as a tensor product $\bigotimes_i S^{d_i}(V\otimes V^*)$. Then embed this tensor product into $(V\otimes V^*)^{\otimes N}=\operatorname{End}(V)^{\otimes n}$, and use the Schur–Weyl duality to get the result.

## 5.25. Representations of $GL_2(\mathbb F_q)$

**5.25.1. Conjugacy classes in $GL_2(\mathbb F_q)$.** Let $\mathbb F_q$ be a finite field of size $q$ of characteristic other than $2$ and $G=GL_2(\mathbb F_q)$. Then

$$
|G|=(q^2-1)(q^2-q),
$$

since the first column of an invertible $2\times2$ matrix must be nonzero and the second column may not be a multiple of the first one. Factoring,

$$
|GL_2(\mathbb F_q)|=q(q+1)(q-1)^2.
$$

The goal of this section is to describe the irreducible representations of $G$.

<span class="original-page-anchor" id="pdf-page-141" aria-hidden="true"></span>

To begin, let us find the conjugacy classes in $GL_2(\mathbb F_q)$.

| Representatives | Number of elements in a conjugacy class | Number of classes |
| --- | --- | --- |
| Scalar $\begin{pmatrix}x&0\\0&x\end{pmatrix}$ | $1$ (this is a central element) | $q-1$ (one for every nonzero $x$) |
| Parabolic $\begin{pmatrix}x&1\\0&x\end{pmatrix}$ | $q^2-1$ (elements that commute with this one are of the form $\begin{pmatrix}t&u\\0&t\end{pmatrix}$, $t\ne0$) | $q-1$ (one for every nonzero $x$) |
| Hyperbolic $\begin{pmatrix}x&0\\0&y\end{pmatrix}$, $y\ne x$ | $q^2+q$ (elements that commute with this one are of the form $\begin{pmatrix}t&0\\0&u\end{pmatrix}$, $t,u\ne0$) | $\frac12(q-1)(q-2)$ ($x,y\ne0$ and $x\ne y$) |
| Elliptic $\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}$, $x\in\mathbb F_q$, $y\in\mathbb F_q^\times$, $\varepsilon\in\mathbb F_q\setminus\mathbb F_q^2$ (characteristic polynomial over $\mathbb F_q$ is irreducible) | $q^2-q$ (the reason will be described below) | $\frac12q(q-1)$ (matrices with $y$ and $-y$ are conjugate) |

Let us explain the structure of the conjugacy class of *elliptic* matrices in more detail. These are the matrices whose characteristic polynomial is irreducible over $\mathbb F_q$ and which therefore don't have eigenvalues in $\mathbb F_q$. Let $A$ be such a matrix, and consider a quadratic extension of $\mathbb F_q$, namely, $\mathbb F_q(\sqrt\varepsilon)$, where $\varepsilon\in\mathbb F_q\setminus\mathbb F_q^2$. Over this field, $A$ will have eigenvalues

$$
\alpha=\alpha_1+\sqrt\varepsilon\alpha_2
$$

and

$$
\overline\alpha=\alpha_1-\sqrt\varepsilon\alpha_2,
$$

with corresponding eigenvectors

$$
v,\ \overline v\qquad(Av=\alpha v,\ A\overline v=\overline\alpha\overline v).
$$

<span class="original-page-anchor" id="pdf-page-142" aria-hidden="true"></span>

Choose a basis

$$
\{e_1=v+\overline v,\ e_2=\sqrt\varepsilon(v-\overline v)\}.
$$

In this basis, the matrix $A$ will have the form

$$
\begin{pmatrix}\alpha_1&\varepsilon\alpha_2\\\alpha_2&\alpha_1\end{pmatrix},
$$

justifying the description of representative elements of this conjugacy class.

In the basis $\{v,\overline v\}$, matrices that commute with $A$ will have the form

$$
\begin{pmatrix}\lambda&0\\0&\overline\lambda\end{pmatrix},
$$

for all

$$
\lambda\in\mathbb F_{q^2}^\times,
$$

so the number of such matrices is $q^2-1$.

**5.25.2. 1-dimensional representations.** First, we describe the 1-dimensional representations of $G$.

**Proposition 5.25.1.** $[G,G]=SL_2(\mathbb F_q)$.

**Proof.** Clearly,

$$
\det(xyx^{-1}y^{-1})=1,
$$

so

$$
[G,G]\subseteq SL_2(\mathbb F_q).
$$

To show the converse, it suffices to show that the matrices

$$
\begin{pmatrix}1&1\\0&1\end{pmatrix},\quad\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix},\quad\begin{pmatrix}1&0\\1&1\end{pmatrix}
$$

are commutators (as such matrices generate $SL_2(\mathbb F_q)$). Clearly, by using transposition, it suffices to show that only the first two matrices are commutators. But it is easy to see that the matrix

$$
\begin{pmatrix}1&1\\0&1\end{pmatrix}
$$

is the commutator of the matrices

$$
A=\begin{pmatrix}1&1/2\\0&1\end{pmatrix},\quad B=\begin{pmatrix}1&0\\0&-1\end{pmatrix},
$$

<span class="original-page-anchor" id="pdf-page-143" aria-hidden="true"></span>

while the matrix

$$
\begin{pmatrix}a&0\\0&a^{-1}\end{pmatrix}
$$

is the commutator of the matrices

$$
A=\begin{pmatrix}a&0\\0&1\end{pmatrix},\quad B=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
$$

This completes the proof. $\square$

Therefore,

$$
G/[G,G]\cong\mathbb F_q^\times\qquad\text{via }g\mapsto\det(g).
$$

The 1-dimensional representations of $G$ thus have the form

$$
\rho(g)=\xi(\det(g)),
$$

where $\xi$ is a homomorphism

$$
\xi:\mathbb F_q^\times\to\mathbb C^\times;
$$

so there are $q-1$ such representations, denoted $\mathbb C_\xi$.

**5.25.3. Principal series representations.** Let

$$
B\subset G,\quad B=\left\{\begin{pmatrix}*&*\\0&*\end{pmatrix}\right\}
$$

(the set of upper triangular matrices); then

$$
|B|=(q-1)^2q,
$$

$$
[B,B]=U=\left\{\begin{pmatrix}1&*\\0&1\end{pmatrix}\right\},
$$

and

$$
B/[B,B]\cong\mathbb F_q^\times\times\mathbb F_q^\times
$$

(the isomorphism maps an element of $B$ to its two diagonal entries). Let

$$
\lambda:B\to\mathbb C^\times
$$

be a homomorphism defined by

$$
\lambda\begin{pmatrix}a&b\\0&c\end{pmatrix}=\lambda_1(a)\lambda_2(c)
$$

<span class="original-page-anchor" id="pdf-page-144" aria-hidden="true"></span>

for some pair of homomorphisms $\lambda_1,\lambda_2:\mathbb F_q^\times\to\mathbb C^\times$. Define

$$
V_{\lambda_1,\lambda_2}=\operatorname{Ind}_B^G\mathbb C_\lambda,
$$

where $\mathbb C_\lambda$ is the 1-dimensional representation of $B$ in which $B$ acts by $\lambda$. We have

$$
\dim(V_{\lambda_1,\lambda_2})=\frac{|G|}{|B|}=q+1.
$$

**Theorem 5.25.2.** (1) $\lambda_1\ne\lambda_2\Rightarrow V_{\lambda_1,\lambda_2}$ is irreducible.

(2) $\lambda_1=\lambda_2=\mu\Rightarrow V_{\lambda_1,\lambda_2}=\mathbb C_\mu\oplus W_\mu$, where $W_\mu$ is a $q$-dimensional irreducible representation of $G$.

(3) $W_\mu\cong W_\nu$ if and only if $\mu=\nu$; $V_{\lambda_1,\lambda_2}\cong V_{\lambda'_1,\lambda'_2}$ if and only if $\{\lambda_1,\lambda_2\}=\{\lambda'_1,\lambda'_2\}$ (in the second case, $\lambda_1\ne\lambda_2$, $\lambda'_1\ne\lambda'_2$).

**Proof.** From the Frobenius formula, we have

$$
\operatorname{Tr}_{V_{\lambda_1,\lambda_2}}(g)=\frac1{|B|}\sum_{a\in G,\ aga^{-1}\in B}\lambda(aga^{-1}).
$$

If

$$
g=\begin{pmatrix}x&0\\0&x\end{pmatrix},
$$

the expression on the right evaluates to

$$
\lambda(g)\frac{|G|}{|B|}=\lambda_1(x)\lambda_2(x)(q+1).
$$

If

$$
g=\begin{pmatrix}x&1\\0&x\end{pmatrix},
$$

the expression evaluates to

$$
\lambda(g)\cdot1,
$$

since here $aga^{-1}\in B\Rightarrow a\in B$.

If

$$
g=\begin{pmatrix}x&0\\0&y\end{pmatrix},
$$

the expression evaluates to

$$
(\lambda_1(x)\lambda_2(y)+\lambda_1(y)\lambda_2(x))\cdot1,
$$

<span class="original-page-anchor" id="pdf-page-145" aria-hidden="true"></span>

since here $aga^{-1}\in B$ implies that $a\in B$ or $a$ is an element of $B$ multiplied by the transposition matrix.

If

$$
g=\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix},\quad x\ne y,
$$

the expression on the right evaluates to $0$ because matrices of this type do not have eigenvalues over $\mathbb F_q$ (and thus cannot be conjugated into $B$). From the definition, $\lambda_i(x)$ for $i=1,2$ is a root of unity, so

$$
\begin{aligned}
|G|\langle\chi_{V_{\lambda_1,\lambda_2}},\chi_{V_{\lambda_1,\lambda_2}}\rangle
&=(q+1)^2(q-1)+(q^2-1)(q-1)\\
&\quad+2(q^2+q)\frac{(q-1)(q-2)}2\\
&\quad+(q^2+q)\sum_{x\ne y}\lambda_1(x)\lambda_2(y)\overline{\lambda_1(y)\lambda_2(x)}.
\end{aligned}
$$

The last two summands come from the expansion

$$
|a+b|^2=|a|^2+|b|^2+a\overline b+\overline a b.
$$

If

$$
\lambda_1=\lambda_2=\mu,
$$

the last term is equal to

$$
(q^2+q)(q-2)(q-1),
$$

and the total in this case is

$$
\begin{aligned}
&(q+1)(q-1)[(q+1)+(q-1)+2q(q-2)]\\
&\qquad=(q+1)(q-1)2q(q-1)=2|G|,
\end{aligned}
$$

so

$$
\langle\chi_{V_{\lambda_1,\lambda_2}},\chi_{V_{\lambda_1,\lambda_2}}\rangle=2.
$$

Clearly,

$$
\mathbb C_\mu\subseteq\operatorname{Ind}_B^G\mathbb C_{\mu,\mu},
$$

since

$$
\operatorname{Hom}_G(\mathbb C_\mu,\operatorname{Ind}_B^G\mathbb C_{\mu,\mu})=\operatorname{Hom}_B(\mathbb C_\mu,\mathbb C_\mu)=\mathbb C\qquad\text{(Theorem 5.10.1).}
$$

Therefore, $\operatorname{Ind}_B^G\mathbb C_{\mu,\mu}=\mathbb C_\mu\oplus W_\mu$; $W_\mu$ is irreducible; and the character of $W_\mu$ is different for distinct values of $\mu$, proving that $W_\mu$ are distinct.

If $\lambda_1\ne\lambda_2$, let $z=xy^{-1}$. Then the last term of the summation is

$$
\begin{aligned}
&(q^2+q)\sum_{x\ne y}\lambda_1(z)\overline{\lambda_2(z)}\\
&\qquad=(q^2+q)\sum_{x;\ z\ne1}\frac{\lambda_1}{\lambda_2}(z)
=(q^2+q)(q-1)\sum_{z\ne1}\frac{\lambda_1}{\lambda_2}(z).
\end{aligned}
$$

<span class="original-page-anchor" id="pdf-page-146" aria-hidden="true"></span>

Since

$$
\sum_{z\in\mathbb F_q^\times}\frac{\lambda_1}{\lambda_2}(z)=0,
$$

because the sum of all roots of unity of a given order $m>1$ is zero, the last term becomes

$$
-(q^2+q)(q-1)\frac{\lambda_1}{\lambda_2}(1)=-(q^2+q)(q-1).
$$

The difference between this case and the case of $\lambda_1=\lambda_2$ is equal to

$$
-(q^2+q)[(q-2)(q-1)+(q-1)]=|G|,
$$

so this is an irreducible representation by Lemma 5.7.2.

To prove the third assertion of the theorem, we look at the characters on hyperbolic elements and note that the function

$$
\lambda_1(x)\lambda_2(y)+\lambda_1(y)\lambda_2(x)
$$

determines $\lambda_1,\lambda_2$ up to permutation. $\square$

**5.25.4. Complementary series representations.** Let $\mathbb F_{q^2}\supset\mathbb F_q$ be a quadratic extension $\mathbb F_q(\sqrt\varepsilon)$, $\varepsilon\in\mathbb F_q\setminus\mathbb F_q^2$. We regard this as a 2-dimensional vector space over $\mathbb F_q$; then $G$ is the group of linear transformations of $\mathbb F_{q^2}$ over $\mathbb F_q$. Let $K\subset G$ be the cyclic group of multiplications by elements of $\mathbb F_{q^2}^\times$,

$$
K=\left\{\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}\right\},\qquad |K|=q^2-1.
$$

For $\nu:K\to\mathbb C^\times$ a homomorphism, let

$$
Y_\nu=\operatorname{Ind}_K^G\mathbb C_\nu.
$$

This representation, of course, is reducible. Let us compute its character, using the Frobenius formula. We get

$$
\chi\begin{pmatrix}x&0\\0&x\end{pmatrix}=q(q-1)\nu(x),
$$

$$
\chi(A)=0\quad\text{for }A\text{ parabolic or hyperbolic},
$$

$$
\chi\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}
=\nu\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}
+\nu\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}^{q}.
$$

<span class="original-page-anchor" id="pdf-page-147" aria-hidden="true"></span>

The last assertion holds because if we regard the matrix as an element of $\mathbb F_{q^2}$, conjugation is an automorphism of $\mathbb F_{q^2}$ over $\mathbb F_q$, but the only nontrivial automorphism of $\mathbb F_{q^2}$ over $\mathbb F_q$ is the $q$th power map.

We thus have

$$
\operatorname{Ind}_K^G\mathbb C_{\nu^q}\cong\operatorname{Ind}_K^G\mathbb C_\nu
$$

because they have the same character. Therefore, for $\nu^q\ne\nu$ we get $\frac12q(q-1)$ representations.

Next, we look at the tensor product

$$
W_1\otimes V_{\alpha,1},
$$

where $1$ is the trivial character and $W_1$ is defined as in the previous section. The character of this representation is

$$
\chi\begin{pmatrix}x&0\\0&x\end{pmatrix}=q(q+1)\alpha(x),
$$

$$
\chi(A)=0\quad\text{for }A\text{ parabolic or elliptic},
$$

$$
\chi\begin{pmatrix}x&0\\0&y\end{pmatrix}=\alpha(x)+\alpha(y).
$$

Thus the “virtual representation”

$$
W_1\otimes V_{\alpha,1}-V_{\alpha,1}-\operatorname{Ind}_K^G\mathbb C_\nu,
$$

where $\alpha$ is the restriction of $\nu$ to scalars, has the character

$$
\chi\begin{pmatrix}x&0\\0&x\end{pmatrix}=(q-1)\alpha(x),
$$

$$
\chi\begin{pmatrix}x&1\\0&x\end{pmatrix}=-\alpha(x),
$$

$$
\chi\begin{pmatrix}x&0\\0&y\end{pmatrix}=0,
$$

$$
\chi\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}
=-\nu\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}
-\nu^q\begin{pmatrix}x&\varepsilon y\\y&x\end{pmatrix}.
$$

In all that follows, we will have $\nu^q\ne\nu$.

The following two lemmas will establish that the inner product of this character with itself is equal to $1$ and that its value at $1$ is <span class="original-page-anchor" id="pdf-page-148" aria-hidden="true"></span>positive. As we know from Lemma 5.7.2, these two properties imply that it is the character of an irreducible representation of $G$.

**Lemma 5.25.3.** Let $\chi$ be the character of the virtual representation defined above. Then

$$
\langle\chi,\chi\rangle=1
$$

and

$$
\chi(1)>0.
$$

**Proof.**

$$
\chi(1)=q(q+1)-(q+1)-q(q-1)=q-1>0.
$$

We now compute the inner product $\langle\chi,\chi\rangle$. Since $\alpha$ is a root of unity, this will be equal to

$$
\begin{aligned}
\frac1{(q-1)^2q(q+1)}\Big[&(q-1)\cdot(q-1)^2\cdot1+(q-1)\cdot1\cdot(q^2-1)\\
&+\frac{q(q-1)}2\cdot\sum_{\zeta\ \mathrm{elliptic}}(\nu(\zeta)+\nu^q(\zeta))\overline{(\nu(\zeta)+\nu^q(\zeta))}\Big].
\end{aligned}
$$

Because $\nu$ is also a root of unity, the last term of the expression evaluates to

$$
\sum_{\zeta\ \mathrm{elliptic}}(2+\nu^{q-1}(\zeta)+\nu^{1-q}(\zeta)).
$$

Let's evaluate the last summand.

Since $\mathbb F_{q^2}^\times$ is cyclic and $\nu^q\ne\nu$,

$$
\sum_{\zeta\in\mathbb F_{q^2}^\times}\nu^{q-1}(\zeta)=\sum_{\zeta\in\mathbb F_{q^2}^\times}\nu^{1-q}(\zeta)=0.
$$

Therefore,

$$
\begin{aligned}
\sum_{\zeta\ \mathrm{elliptic}}(\nu^{q-1}(\zeta)+\nu^{1-q}(\zeta))
&=-\sum_{\zeta\in\mathbb F_q^\times}(\nu^{q-1}(\zeta)+\nu^{1-q}(\zeta))\\
&=-2(q-1)
\end{aligned}
$$

since $\mathbb F_q^\times$ is cyclic of order $q-1$. Therefore,

$$
\begin{aligned}
\langle\chi,\chi\rangle=\frac1{(q-1)^2q(q+1)}\Big(&(q-1)\cdot(q-1)^2\cdot1+(q-1)\cdot1\cdot(q^2-1)\\
&+\frac{q(q-1)}2\cdot(2(q^2-q)-2(q-1))\Big)=1.
\end{aligned}
$$

$\square$ <span class="original-page-anchor" id="pdf-page-149" aria-hidden="true"></span>We have now shown that for any $\nu$ with $\nu^q\ne\nu$ the representation $Y_\nu$ with the same character as

$$
W_1\otimes V_{\alpha,1}-V_{\alpha,1}-\operatorname{Ind}_K^G\mathbb C_\nu
$$

exists and is irreducible. These characters are distinct for distinct pairs $(\alpha,\nu)$ (up to switching $\nu\to\nu^q$), so there are $\frac{q(q-1)}2$ such representations, each of dimension $q-1$.

We have thus found $q-1$ 1-dimensional representations of $G$, $\frac{q(q-1)}2$ principal series representations, and $\frac{q(q-1)}2$ complementary series representations, for a total of $q^2-1$ representations, i.e., the number of conjugacy classes in $G$. This implies that we have in fact found all irreducible representations of $GL_2(\mathbb F_q)$.

## 5.26. Artin’s theorem

**Theorem 5.26.1.** Let $X$ be a conjugation-invariant system of subgroups of a finite group $G$. Then two conditions are equivalent:

(i) Any element of $G$ belongs to a subgroup $H\in X$.

(ii) The character of any irreducible representation of $G$ belongs to the $\mathbb Q$-span of characters of induced representations $\operatorname{Ind}_H^G V$, where $H\in X$ and $V$ is an irreducible representation of $H$.

**Remark 5.26.2.** Statement (ii) of Theorem 5.26.1 is equivalent to the same statement with $\mathbb Q$-span replaced by $\mathbb C$-span. Indeed, consider the matrix whose columns consist of the coefficients of the decomposition of $\operatorname{Ind}_H^G V$ (for various $H,V$) with respect to the irreducible representations of $G$. Then both statements are equivalent to the condition that the rows of this matrix are linearly independent.

**Proof.** *Proof that (ii) implies (i).* Assume that $g\in G$ does not belong to any of the subgroups $H\in X$. Then, since $X$ is conjugation invariant, it cannot be conjugated into such a subgroup. Hence by the Frobenius formula, $\chi_{\operatorname{Ind}_H^G(V)}(g)=0$ for all $H\in X$ and $V$. So by (ii), for any irreducible representation $W$ of $G$, $\chi_W(g)=0$. But irreducible characters span the space of class functions, so any class function vanishes on $g$, which is a contradiction.

*Proof that (i) implies (ii).* Let $U$ be a virtual representation of $G$ over $\mathbb C$ (i.e., a linear combination of irreducible representations with <span class="original-page-anchor" id="pdf-page-150" aria-hidden="true"></span>nonzero integer coefficients) such that $(\chi_U,\chi_{\operatorname{Ind}_H^G V})=0$ for all $H,V$. So by Frobenius reciprocity, $(\chi_{U|_H},\chi_V)=0$. This means that $\chi_U$ vanishes on $H$ for any $H\in X$. Hence by (i), $\chi_U$ is identically zero. This implies (ii) (because of Remark 5.26.2). $\square$

**Corollary 5.26.3.** Any irreducible character of a finite group is a rational linear combination of induced characters from its cyclic subgroups.

## 5.27. Representations of semidirect products

Let $G,A$ be groups and let $\phi:G\to\operatorname{Aut}(A)$ be a homomorphism. For $a\in A$, denote $\phi(g)a$ by $g(a)$. The **semidirect product** $G\ltimes A$ is defined to be the product $A\times G$ with multiplication law

$$
(a_1,g_1)(a_2,g_2)=(a_1g_1(a_2),g_1g_2).
$$

Clearly, $G$ and $A$ are subgroups of $G\ltimes A$ in a natural way.

We would like to study irreducible complex representations of $G\ltimes A$. For simplicity, let us do it when $A$ is abelian.

In this case, irreducible representations of $A$ are 1-dimensional and form the character group $A^\vee$, which carries an action of $G$. Let $O$ be an orbit of this action, $x\in O$ a chosen element, and $G_x$ the stabilizer of $x$ in $G$. Let $U$ be an irreducible representation of $G_x$. Then we define a representation $V_{(O,U)}$ of $G\ltimes A$ as follows.

As a representation of $G$, we set

$$
V_{(O,x,U)}=\operatorname{Ind}_{G_x}^G U=\{f:G\to U\mid f(hg)=hf(g),\ h\in G_x\}.
$$

Next, we introduce an additional action of $A$ on this space by $(af)(g)=x(g(a))f(g)$. Then it is easy to check that these two actions combine into an action of $G\ltimes A$. Also, it is clear that this representation does not really depend on the choice of $x$, in the following sense. Let $x,y\in O$ and $g\in G$ be such that $gx=y$, and let $g(U)$ be the representation of $G_y$ obtained from the representation $U$ of $G_x$ by the action of $g$. Then $V_{(O,x,U)}$ is (naturally) isomorphic to $V_{(O,y,g(U))}$. Thus we will denote $V_{(O,x,U)}$ by $V_{(O,U)}$ (remembering, however, that $x$ has been fixed).

**Theorem 5.27.1.** (i) The representations $V_{(O,U)}$ are irreducible.

<span class="original-page-anchor" id="pdf-page-151" aria-hidden="true"></span>

(ii) They are pairwise nonisomorphic.

(iii) They form a complete set of irreducible representations of $G\ltimes A$.

(iv) The character of $V=V_{(O,U)}$ is given by the Frobenius-type formula

$$
\chi_V(a,g)=\frac1{|G_x|}\sum_{h\in G:\,hgh^{-1}\in G_x}x(h(a))\chi_U(hgh^{-1}).
$$

**Proof.** (i) Let us decompose $V=V_{(O,U)}$ as an $A$-module. Then we get

$$
V=\bigoplus_{y\in O}V_y,
$$

where $V_y=\{v\in V_{(O,U)}\mid av=(y,a)v,\ a\in A\}$. (Equivalently, $V_y=\{v\in V_{(O,U)}\mid v(g)=0\text{ unless }gy=x\}$.) So if $W\subset V$ is a subrepresentation, then $W=\bigoplus_{y\in O}W_y$, where $W_y\subset V_y$. Now, $V_y$ is a representation of $G_y$, which goes to $U$ under any isomorphism $G_y\to G_x$ determined by $g\in G$ mapping $x$ to $y$. Hence, $V_y$ is irreducible over $G_y$, so $W_y=0$ or $W_y=V_y$ for each $y$. Also, if $hy=z$, then $hW_y=W_z$, so either $W_y=0$ for all $y$ or $W_y=V_y$ for all $y$, as desired.

(ii) The orbit $O$ is determined by the $A$-module structure of $V$, and the representation $U$ is determined by the structure of $V_x$ as a $G_x$-module.

(iii) We have

$$
\begin{aligned}
\sum_{U,O}\dim V_{(U,O)}^2
&=\sum_{U,O}|O|^2(\dim U)^2\\
&=\sum_O|O|^2|G_x|=\sum_O|O||G/G_x||G_x|\\
&=|G|\sum_O|O|=|G||A^\vee|=|G\ltimes A|.
\end{aligned}
$$

(iv) The proof is essentially the same as that of the Frobenius formula. $\square$

**Exercise 5.27.2.** Redo Problems 4.12.1(a), 4.12.2, and 4.12.6 using Theorem 5.27.1.

**Exercise 5.27.3.** Deduce parts (i)–(iii) of Theorem 5.27.1 from part (iv).

[^pdf122-1]: If $j>p$, we define $\lambda_j$ to be zero.
