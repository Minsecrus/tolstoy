---
title: "附录 一般伴随函子定理的证明"
description: "Tom Leinster《Basic Category Theory》中文译文。"
pageClass: algebra-reading category-theory-reading
prev: {"text":"第六章 伴随函子、可表函子与极限","link":"/library/volume-87/chapter-006"}
next: {"text":"延伸阅读","link":"/library/volume-87/further-reading"}
---

# 附录 一般伴随函子定理的证明

<span class="original-page-anchor" id="pdf-page-180" aria-hidden="true"></span>

这里我们证明一般伴随函子定理。为便于阅读，先将定理重述如下。从左到右的蕴涵由定理 6.3.1 立即得到；我们需要证明的是从右到左的蕴涵。

**定理 6.3.10（一般伴随函子定理）** 设 $\mathscr{A}$ 是一个范畴，$\mathscr{B}$ 是一个完备范畴，$G:\mathscr{B}\to\mathscr{A}$ 是一个函子。假设 $\mathscr{B}$ 局部小，并且对每个 $A\in\mathscr{A}$，范畴 $(A\Rightarrow G)$ 都有一个弱始集。那么

$$
G\text{ 有左伴随}\iff G\text{ 保持极限}.
$$

证明的核心是 $\mathscr{A}=\mathbf{1}$ 这一情形。此时，一般伴随函子定理（GAFT）断言：一个具有弱始集的完备局部小范畴必有始对象。我们先证明这一点。

要看清这个特殊情形的证明，可以考虑更特殊的情况：$\mathscr{A}=\mathbf{1}$，而范畴 $\mathscr{B}$ 是一个偏序集 $\mathbf{B}$。在例 6.3.8 中我们已经看到，完备偏序集 $\mathbf{B}$ 的始对象（也就是最小元）可以构造为其所有元素的交。换句话说，它就是恒等函子 $1_{\mathbf{B}}:\mathbf{B}\to\mathbf{B}$ 的极限。

我们也许会试着将这一结果推广到任意范畴 $\mathscr{B}$，方法是证明：恒等函子 $1_{\mathscr{B}}:\mathscr{B}\to\mathscr{B}$ 的极限（如果存在）是一个始对象。这个结论确实成立（见下面的习题 A.3）。但它在这里无济于事：如果 $\mathscr{B}$ 是大范畴，那么 $1_{\mathscr{B}}$ 的极限就是大极限，而已知条件只保证 $\mathscr{B}$ 具有小极限。

我们似乎陷入了僵局——但这正是 GAFT 背后的巧妙想法发挥作用的地方。构造完备偏序集的最小元时，不必取其*所有*元素的交。更节省的做法是，只取某个弱始子集中各元素的交（习题 A.4）。

<span class="original-page-anchor" id="pdf-page-181" aria-hidden="true"></span>

一般来说，对于任意完备范畴，任何弱始集的极限都是一个始对象。现在我们证明这一点。

**引理 A.1** 设 $\mathscr{C}$ 是具有弱始集的完备局部小范畴。那么 $\mathscr{C}$ 有始对象。

**证明** 设 $\mathbf{S}$ 是 $\mathscr{C}$ 中的一个弱始集。将 $\mathbf{S}$ 看成 $\mathscr{C}$ 的充满子范畴；由于 $\mathscr{C}$ 局部小，$\mathbf{S}$ 就是小范畴。因此，可以取包含函子 $\mathbf{S}\hookrightarrow\mathscr{C}$ 的一个极限锥

$$
\left(0\xrightarrow{p_S}S\right)_{S\in\mathbf{S}}\tag{A.1}
$$

下面证明 $0$ 是始对象。

取 $C\in\mathscr{C}$。我们需要证明恰有一个态射 $0\to C$。显然至少有一个这样的态射：可以选择某个 $S\in\mathbf{S}$ 以及态射 $j:S\to C$，随后取复合 $jp_S:0\to C$。为证明唯一性，设 $f,g:0\to C$，并构造它们的等化子

![f 与 g 的等化子](/library/volume-87/diagrams/pdf-0181-equalizer.png)

由于 $\mathbf{S}$ 是弱始集，可以选取 $S\in\mathbf{S}$ 以及 $h:S\to E$。于是我们得到态射链

$$
0\xrightarrow{p_S}S\xrightarrow{h}E\xrightarrow{i}0,
$$

并且对所有 $S'\in\mathbf{S}$，都有

$$
p_{S'}(ihp_S)=(p_{S'}ih)p_S=p_{S'}=p_{S'}1_0.
$$

这里第二个等号由 (A.1) 是一个锥而得。进一步，(A.1) 是一个*极限*锥，因此根据习题 5.1.36(a)，有 $ihp_S=1_0$。从而

$$
f=fihp_S=gihp_S=g,
$$

这就证明了所需的唯一性。$\square$

至此，我们已经证明了 $\mathscr{A}=\mathbf{1}$ 这一特殊情形下的 GAFT。余下的证明就比较常规了。

**引理 A.2** 设 $\mathscr{A}$ 和 $\mathscr{B}$ 是范畴，$G:\mathscr{B}\to\mathscr{A}$ 是一个保持极限的函子。那么，对每个 $A\in\mathscr{A}$，(6.21) 中的投影函子 $P_A:(A\Rightarrow G)\to\mathscr{B}$ 都创造极限。特别地，如果 $\mathscr{B}$ 完备，那么每个逗号范畴 $(A\Rightarrow G)$ 也都完备。

**证明** 第一个断言就是习题 A.5(b)；由引理 5.3.6，第二个断言随之成立。$\square$<span class="original-page-anchor" id="pdf-page-182" aria-hidden="true"></span>现在证明 GAFT。根据推论 2.3.7，只需证明对每个 $A\in\mathscr{A}$，$(A\Rightarrow G)$ 都有始对象。取 $A\in\mathscr{A}$。由引理 A.2，$(A\Rightarrow G)$ 是完备的；根据假设，它有一个弱始集。由于 $\mathscr{B}$ 局部小，它也局部小。因此，引理 A.1 保证它有始对象，这就完成了所需的证明。

### 习题

**A.3** 在本题中，我们暂时放下定义 5.1.19 中隐含的约定：只有当 $\mathbf{I}$ 为小范畴时，才谈论函子 $\mathbf{I}\to\mathscr{C}$ 的极限。设 $\mathscr{B}$ 是一个可能为大的范畴。本题的目标是证明：$\mathscr{B}$ 上恒等函子的极限，恰好就是 $\mathscr{B}$ 的始对象。

(a) 设 $0$ 是 $\mathscr{B}$ 的始对象。证明恒等函子 $1_{\mathscr{B}}$ 上的锥 $(0\to B)_{B\in\mathscr{B}}$ 是极限锥。

(b) 现在设 $\left(L\xrightarrow{p_B}B\right)_{B\in\mathscr{B}}$ 是 $1_{\mathscr{B}}$ 上的极限锥。证明 $p_L$ 是 $L$ 上的恒等态射，并由此推出 $L$ 是始对象。

**A.4** 本题要求证明引理 A.1 在范畴是偏序集时的特殊情形。设 $C$ 是偏序集，$S\subseteq C$。

(a) 完全用序论语言来说，$S$ 是 $C$ 中的弱始集意味着什么？

(b) 直接证明：若 $S$ 是弱始集，并且交 $\bigwedge_{s\in S}s$ 存在，那么 $\bigwedge_{s\in S}s$ 是 $C$ 的最小元。

**A.5** 设 $G:\mathscr{B}\to\mathscr{A}$ 是保持极限的函子，并取 $A\in\mathscr{A}$。

(a) 证明：对任意小范畴 $\mathbf{I}$，$(A\Rightarrow G)$ 中一个形状为 $\mathbf{I}$ 的图，等同于 $\mathscr{B}$ 中一个形状为 $\mathbf{I}$ 的图 $E$，加上 $G\circ E$ 上一个以 $A$ 为顶点的锥。

(b) 证明 (6.21) 中的投影函子 $P_A:(A\Rightarrow G)\to\mathscr{B}$ 创造极限。
