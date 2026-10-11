---
title: "Appendix 1: The Transcendence of e and π"
description: "Serge Lang《Algebra》English。"
pageClass: algebra-reading
prev: {"text":"Chapter XXI: Finite Free Resolutions","link":"/library/volume-86/original-chapter-021"}
next: {"text":"Appendix 2: Some Set Theory","link":"/library/volume-86/original-appendix-02"}
---

# Appendix 1: The Transcendence of e and π

<span class="original-page-anchor" id="pdf-page-875" aria-hidden="true"></span>

The proof which we shall give here follows the classical method of Gelfond and Schneider, properly formulated. It is based on a theorem concerning values of functions satisfying differential equations, and it had been recognized for some time that such values are subject to severe restrictions, in various contexts. Here, we deal with the most general algebraic differential equation.

We shall assume that the reader is acquainted with elementary facts concerning functions of a complex variable. Let $f$ be an entire function (i.e. a function which is holomorphic on the complex plane). For our purposes, we say $f$ is of order $\leqq\rho$ if there exists a number $C>1$ such that for all large $R$ we have

$$
|f(z)|\leqq C^{R^\rho}
$$

whenever $|z|\leqq R$. A meromorphic function is said to be of order $\leqq\rho$ if it is a quotient of entire functions of order $\leqq\rho$.

**Theorem.** *Let $K$ be a finite extension of the rational numbers. Let $f_1,\ldots,f_N$ be meromorphic functions of order $\leqq\rho$. Assume that the field $K(f_1,\ldots,f_N)$ has transcendence degree $\geqq2$ over $K$, and that the derivative $D=d/dz$ maps the ring $K[f_1,\ldots,f_N]$ into itself. Let $w_1,\ldots,w_m$ be distinct complex numbers not lying among the poles of the $f_i$, such that*

$$
f_i(w_\nu)\in K
$$

*for all $i=1,\ldots,N$ and $\nu=1,\ldots,m$. Then $m\leqq10\rho[K:\mathbf Q]$.*

**Corollary 1.** (Hermite-Lindemann). *If $\alpha$ is algebraic (over $\mathbf Q$) and $\ne0$, then $e^\alpha$ is transcendental. Hence $\pi$ is transcendental.*

<span class="original-page-anchor" id="pdf-page-876" aria-hidden="true"></span>

*Proof.* Suppose that $\alpha$ and $e^\alpha$ are algebraic. Let $K=\mathbf Q(\alpha,e^\alpha)$. The two functions $z$ and $e^z$ are algebraically independent over $K$ (trivial), and the ring $K[z,e^z]$ is obviously mapped into itself by the derivative. Our functions take on algebraic values in $K$ at $\alpha,2\alpha,\ldots,m\alpha$ for any $m$, contradiction. Since $e^{2\pi i}=1$, it follows that $2\pi i$ is transcendental.

**Corollary 2.** (Gelfond-Schneider). *If $\alpha$ is algebraic $\ne0,1$ and if $\beta$ is algebraic irrational, then $\alpha^\beta=e^{\beta\log\alpha}$ is transcendental.*

*Proof.* We proceed as in Corollary 1, considering the functions $e^{\beta t}$ and $e^t$ which are algebraically independent because $\beta$ is assumed irrational. We look at the numbers $\log\alpha,2\log\alpha,\ldots,m\log\alpha$ to get a contradiction as in Corollary 1.

Before giving the main arguments proving the theorem, we state some lemmas. The first two, due to Siegel, have to do with integral solutions of linear homogeneous equations.

**Lemma 1.** *Let*

$$
\begin{gathered}
a_{11}x_1+\cdots+a_{1n}x_n=0\\
\cdots\\
a_{r1}x_1+\cdots+a_{rn}x_n=0
\end{gathered}
$$

*be a system of linear equations with integer coefficients $a_{ij}$, and $n>r$. Let $A$ be a number such that $|a_{ij}|\leqq A$ for all $i,j$. Then there exists an integral, non-trivial solution with*

$$
|x_j|\leqq2(2nA)^{r/(n-r)}.
$$

*Proof.* We view our system of linear equations as a linear equation $L(X)=0$, where $L$ is a linear map, $L:\mathbf Z^{(n)}\longrightarrow\mathbf Z^{(r)}$, determined by the matrix of coefficients. If $B$ is a positive number, we denote by $\mathbf Z^{(n)}(B)$ the set of vectors $X$ in $\mathbf Z^{(n)}$ such that $|X|\leqq B$ (where $|X|$ is the maximum of the absolute values of the coefficients of $X$). Then $L$ maps $\mathbf Z^{(n)}(B)$ into $\mathbf Z^{(r)}(nBA)$. The number of elements in $\mathbf Z^{(n)}(B)$ is $\geqq B^n$ and $\leqq(2B+1)^n$. We seek a value of $B$ such that there will be two distinct elements $X,Y$ in $\mathbf Z^{(n)}(B)$ having the same image, $L(X)=L(Y)$. For this, it will suffice that $B^n>(2nBA)^r$, and thus it will suffice that

$$
B=(2nA)^{r/(n-r)}.
$$

We take $X-Y$ as the solution of our problem.

Let $K$ be a finite extension of $\mathbf Q$, and let $I_K$ be the integral closure of $\mathbf Z$ in $K$. From Exercise 5 of Chapter IX, we know that $I_K$ is a free module over $\mathbf Z$, of dimension $[K:\mathbf Q]$. We view $K$ as contained in the complex numbers. If <span class="original-page-anchor" id="pdf-page-877" aria-hidden="true"></span>$\alpha\in K$, a conjugate of $\alpha$ will be taken to be an element $\sigma\alpha$, where $\sigma$ is an embedding of $K$ in $\mathbf C$. By the **size** of a set of elements of $K$ we shall mean the maximum of the absolute values of all conjugates of these elements.

By the size of a vector $X=(x_1,\ldots,x_n)$ we shall mean the size of the set of its coordinates.

Let $\omega_1,\ldots,\omega_M$ be a basis of $I_K$ over $\mathbf Z$. Let $\alpha\in I_K$, and write

$$
\alpha=a_1\omega_1+\cdots+a_M\omega_M.
$$

Let $\omega'_1,\ldots,\omega'_M$ be the dual basis of $\omega_1,\ldots,\omega_M$ with respect to the trace. Then we can express the (Fourier) coefficients $a_j$ of $\alpha$ as a trace,

$$
a_j=\operatorname{Tr}(\alpha\omega'_j).
$$

The trace is a sum over the conjugates. Hence the size of these coefficients is bounded by the size of $\alpha$, times a fixed constant, depending on the size of the elements $\omega'_j$.

**Lemma 2.** *Let $K$ be a finite extension of $\mathbf Q$. Let*

$$
\begin{gathered}
\alpha_{11}x_1+\cdots+\alpha_{1n}x_n=0\\
\cdots\\
\alpha_{r1}x_1+\cdots+\alpha_{rn}x_n=0
\end{gathered}
$$

*be a system of linear equations with coefficients in $I_K$, and $n>r$. Let $A$ be a number such that $\operatorname{size}(\alpha_{ij})\leqq A$, for all $i,j$. Then there exists a non-trivial solution $X$ in $I_K$ such that*

$$
\operatorname{size}(X)\leqq C_1(C_2nA)^{r/(n-r)},
$$

*where $C_1,C_2$ are constants depending only on $K$.*

*Proof.* Let $\omega_1,\ldots,\omega_M$ be a basis of $I_K$ over $\mathbf Z$. Each $x_j$ can be written

$$
x_j=\xi_{j1}\omega_1+\cdots+\xi_{jM}\omega_M
$$

with unknowns $\xi_{j\lambda}$. Each $\alpha_{ij}$ can be written

$$
\alpha_{ij}=a_{ij1}\omega_1+\cdots+a_{ijM}\omega_M
$$

with integers $a_{ij\lambda}\in\mathbf Z$. If we multiply out the $\alpha_{ij}x_j$, we find that our linear equations with coefficients in $I_K$ are equivalent to a system of $rM$ linear equations in the $nM$ unknowns $\xi_{j\lambda}$, with coefficients in $\mathbf Z$, whose size is bounded by $CA$, where $C$ is a number depending only on $M$ and the size of the elements $\omega_\lambda$, together with the products $\omega_\lambda\omega_\mu$, in other words where $C$ depends only on $K$. Applying Lemma 1, we obtain a solution in terms of the $\xi_{j\lambda}$, and hence a solution $X$ in $I_K$, whose size satisfies the desired bound.

<span class="original-page-anchor" id="pdf-page-878" aria-hidden="true"></span>

The next lemma has to do with estimates of derivatives. By the size of a polynomial with coefficients in $K$, we shall mean the size of its set of coefficients. A **denominator** for a set of elements of $K$ will be any positive rational integer whose product with every element of the set is an algebraic integer. We define in a similar way a denominator for a polynomial with coefficients in $K$. We abbreviate “denominator” by den.

Let

$$
P(T_1,\ldots,T_N)=\sum\alpha_{(\nu)}M_{(\nu)}(T)
$$

be a polynomial with complex coefficients, and let

$$
Q(T_1,\ldots,T_N)=\sum\beta_{(\nu)}M_{(\nu)}(T)
$$

be a polynomial with real coefficients $\geqq0$. We say that **$Q$ dominates $P$** if $|\alpha_{(\nu)}|\leqq\beta_{(\nu)}$ for all $(\nu)$. It is then immediately verified that the relation of dominance is preserved under addition, multiplication, and taking partial derivatives with respect to the variables $T_1,\ldots,T_N$.

**Lemma 3.** *Let $K$ be of finite degree over $\mathbf Q$. Let $f_1,\ldots,f_N$ be functions, holomorphic on a neighborhood of a point $w\in\mathbf C$, and assume that $D=d/dz$ maps the ring $K[f_1,\ldots,f_N]$ into itself. Assume that $f_i(w)\in K$ for all $i$. Then there exists a number $C_1$ having the following property. Let $P(T_1,\ldots,T_N)$ be a polynomial with coefficients in $K$, of degree $\leqq r$. If we set $f=P(f_1,\ldots,f_N)$, then we have, for all positive integers $k$,*

$$
\operatorname{size}(D^kf(w))\leqq\operatorname{size}(P)r^kk!C_1^{k+r}
$$

*Furthermore, there is a denominator for $D^kf(w)$ bounded by $\operatorname{den}(P)C_1^{k+r}$.*

*Proof.* There exist polynomials $P_i(T_1,\ldots,T_N)$ with coefficients in $K$ such that

$$
Df_i=P_i(f_1,\ldots,f_N).
$$

Let $h$ be the maximum of their degrees. There exists a unique derivation $\bar D$ on $K[T_1,\ldots,T_N]$ such that $\bar DT_i=P_i(T_1,\ldots,T_N)$. For any polynomial $P$ we have

$$
\bar D(P(T_1,\ldots,T_N))=\sum_{i=1}^N(D_iP)(T_1,\ldots,T_N)\cdot P_i(T_1,\ldots,T_N),
$$

where $D_1,\ldots,D_N$ are the partial derivatives. The polynomial $P$ is dominated by

$$
\operatorname{size}(P)(1+T_1+\cdots+T_N)^r,
$$

and each $P_i$ is dominated by $\operatorname{size}(P_i)(1+T_1+\cdots+T_N)^h$. Thus $\bar DP$ is dominated by

$$
\operatorname{size}(P)C_2r(1+T_1+\cdots+T_N)^{r+h}.
$$

<span class="original-page-anchor" id="pdf-page-879" aria-hidden="true"></span>

Proceeding inductively, one sees that $\bar D^kP$ is dominated by

$$
\operatorname{size}(P)C_3^kr^kk!(1+T_1\cdots+T_N)^{r+kh}.
$$

Substituting values $f_i(w)$ for $T_i$, we obtain the desired bound on $D^kf(w)$. The second assertion concerning denominators is proved also by a trivial induction.

We now come to the main part of the proof of our theorem. Let $f,g$ be two functions among $f_1,\ldots,f_N$ which are algebraically independent over $K$. Let $r$ be a positive integer divisible by $2m$. We shall let $r$ tend to infinity at the end of the proof.

Let

$$
F=\sum_{i,j=1}^r b_{ij}f^ig^j
$$

have coefficients $b_{ij}$ in $K$. Let $n=r^2/2m$. We can select the $b_{ij}$ not all equal to $0$, and such that

$$
D^kF(w_\nu)=0
$$

for $0\leqq k<n$ and $\nu=1,\ldots,m$. Indeed, we have to solve a system of $mn$ linear equations in $r^2=2mn$ unknowns. Note that

$$
\frac{mn}{2mn-mn}=1.
$$

We multiply these equations by a denominator for the coefficients. Using the estimate of Lemma 3, and Lemma 2, we can in fact take the $b_{ij}$ to be algebraic integers, whose size is bounded by

$$
O(r^nn!C_1^{n+r})\leqq O(n^{2n})
$$

for $n\longrightarrow\infty$.

Since $f,g$ are algebraically independent over $K$, our function $F$ is not identically zero. We let $s$ be the smallest integer such that all derivatives of $F$ up to order $s-1$ vanish at all points $w_1,\ldots,w_m$, but such that $D^sF$ does not vanish at one of the $w$, say $w_1$. Then $s\geqq n$. We let

$$
\gamma=D^sF(w_1)\ne0.
$$

Then $\gamma$ is an element of $K$, and by Lemma 3, it has a denominator which is bounded by $O(C_1^s)$ for $s\longrightarrow\infty$. Let $c$ be this denominator. The norm of $c\gamma$ from $K$ to $\mathbf Q$ is then a non-zero rational integer. Each conjugate of $c\gamma$ is bounded by $O(s^{5s})$. Consequently, we get

$$
\tag{1}1\leqq|N_{\mathbf Q}^K(c\gamma)|\leqq O(s^{5s})^{[K:\mathbf Q]-1}|\gamma|,
$$

<span class="original-page-anchor" id="pdf-page-880" aria-hidden="true"></span>

where $|\gamma|$ is the fixed absolute value of $\gamma$, which will now be estimated very well by global arguments.

Let $\theta$ be an entire function of order $\leqq\rho$, such that $\theta f$ and $\theta g$ are entire, and $\theta(w_1)\ne0$. Then $\theta^{2r}F$ is entire. We consider the entire function

$$
H(z)=\frac{\theta(z)^{2r}F(z)}{\displaystyle\prod_{\nu=1}^m(z-w_\nu)^s}.
$$

Then $H(w_1)$ differs from $D^sF(w_1)$ by obvious factors, bounded by $C_4^ss!$. By the maximum modulus principle, its absolute value is bounded by the maximum of $H$ on a large circle of radius $R$. If we take $R$ large, then $z-w_\nu$ has approximately the same absolute value as $R$, and consequently, on the circle of radius $R$, $H(z)$ is bounded in absolute value by an expression of type

$$
\frac{s^{3s}C_5^{2rR^\rho}}{R^{ms}}.
$$

We select $R=s^{1/2\rho}$. We then get the estimate

$$
|\gamma|\leqq\frac{s^{4s}C_6^s}{s^{ms/2\rho}}.
$$

We now let $r$ tend to infinity. Then both $n$ and $s$ tend to infinity. Combining this last inequality with inequality (1), we obtain the desired bound on $m$. This concludes the proof.

Of course, we made no effort to be especially careful in the powers of $s$ occurring in the estimates, and the number $10$ can obviously be decreased by exercising a little more care in the estimates.

The theorem we proved is only the simplest in an extensive theory dealing with problems of transcendence degree. In some sense, the theorem is best possible without additional hypotheses. For instance, if $P(t)$ is a polynomial with integer coefficients, then $e^{P(t)}$ will take the value $1$ at all roots of $P$, these being algebraic. Furthermore, the functions

$$
t,e^t,e^{t^2},\ldots,e^{t^n}
$$

are algebraically independent, but take on values in $\mathbf Q(e)$ for all integral values of $t$.

However, one expects rather strong results of algebraic independence to hold. Lindemann proved that *if $\alpha_1,\ldots,\alpha_n$ are algebraic numbers, linearly independent over $\mathbf Q$, then*

$$
e^{\alpha_1},\ldots,e^{\alpha_n}
$$

*are algebraically independent.*

<span class="original-page-anchor" id="pdf-page-881" aria-hidden="true"></span>

More generally, Schanuel has made the following conjecture: If $\alpha_1,\ldots,\alpha_n$ are complex numbers, linearly independent over $\mathbf Q$, then the transcendence degree of

$$
\alpha_1,\ldots,\alpha_n,e^{\alpha_1},\ldots,e^{\alpha_n}
$$

should be $\geqq n$.

From this one would deduce at once the algebraic independence of $e$ and $\pi$ (looking at $1,2\pi i,e,e^{2\pi i}$), and all other independence statements concerning the ordinary exponential function and logarithm which one feels to be true, for instance, the statement that $\pi$ cannot lie in the field obtained by starting with the algebraic numbers, adjoining values of the exponential function, taking algebraic closure, and iterating these two operations. Such statements have to do with values of the exponential function lying in certain fields of transcendence degree $<n$, and one hopes that by a suitable deepening of Theorem 1, one will reach the desired results.
