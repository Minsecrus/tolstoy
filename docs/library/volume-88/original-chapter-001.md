---
title: "Introduction"
description: "《Introduction to Representation Theory》English。"
pageClass: algebra-reading representation-theory-reading
prev: false
next: {"text":"Basic notions of representation theory","link":"/library/volume-88/original-chapter-002"}
---

# Introduction

<span class="original-page-anchor" id="pdf-page-9" aria-hidden="true"></span>

Very roughly speaking, representation theory studies symmetry in linear spaces. It is a beautiful mathematical subject which has many applications, ranging from number theory and combinatorics to geometry, probability theory, quantum mechanics, and quantum field theory.

Representation theory was born in 1896 in the work of the German mathematician F. G. Frobenius. This work was triggered by a letter to Frobenius by R. Dedekind. In this letter Dedekind made the following observation: take the multiplication table of a finite group $G$ and turn it into a matrix $X_G$ by replacing every entry $g$ of this table by a variable $x_g$. Then the determinant of $X_G$ factors into a product of irreducible polynomials in $\{x_g\}$, each of which occurs with multiplicity equal to its degree. Dedekind checked this surprising fact in a few special cases but could not prove it in general. So he gave this problem to Frobenius. In order to find a solution of this problem (which we will explain below), Frobenius created the representation theory of finite groups.

The goal of this book is to give a “holistic” introduction to representation theory, presenting it as a unified subject which studies representations of associative algebras and treating the representation theories of groups, Lie algebras, and quivers as special cases. It is designed as a textbook for advanced undergraduate and beginning <span class="original-page-anchor" id="pdf-page-10" aria-hidden="true"></span>graduate students and should be accessible to students with a strong background in linear algebra and a basic knowledge of abstract algebra. Theoretical material in this book is supplemented by many problems and exercises which touch upon a lot of additional topics; the more difficult exercises are provided with hints.

The book covers a number of standard topics in representation theory of groups, associative algebras, Lie algebras, and quivers. For a more detailed treatment of these topics, we refer the reader to the textbooks [S], [FH], and [CR]. We mostly follow [FH], with the exception of the sections discussing quivers, which follow [BGP], and the sections on homological algebra and finite dimensional algebras, for which we recommend [W] and [CR], respectively.

The organization of the book is as follows.

Chapter 2 is devoted to the basics of representation theory. Here we review the basics of abstract algebra (groups, rings, modules, ideals, tensor products, symmetric and exterior powers, etc.), as well as give the main definitions of representation theory and discuss the objects whose representations we will study (associative algebras, groups, quivers, and Lie algebras).

Chapter 3 introduces the main general results about representations of associative algebras (the density theorem, the Jordan–Hölder theorem, the Krull–Schmidt theorem, and the structure theorem for finite dimensional algebras).

In Chapter 4 we discuss the basic results about representations of finite groups. Here we prove Maschke’s theorem and the orthogonality of characters and matrix elements and compute character tables and tensor product multiplicities for the simplest finite groups. We also discuss the Frobenius determinant, which was a starting point for development of the representation theory of finite groups.

We continue to study representations of finite groups in Chapter 5, treating more advanced and special topics, such as the Frobenius–Schur indicator, the Frobenius divisibility theorem, the Burnside theorem, the Frobenius formula for the character of an induced representation, representations of the symmetric group and the general <span class="original-page-anchor" id="pdf-page-11" aria-hidden="true"></span>linear group over $\mathbb{C}$, representations of $GL_2(\mathbb{F}_q)$, representations of semidirect products, etc.

In Chapter 6, we give an introduction to the representation theory of quivers (starting with the problem of the classification of configurations of $n$ subspaces in a vector space) and present a proof of Gabriel’s theorem, which classifies quivers of finite type.

In Chapter 7, we give an introduction to category theory, in particular, abelian categories, and explain how such categories arise in representation theory.

In Chapter 8, we give a brief introduction to homological algebra and explain how it can be applied to categories of representations.

Finally, in Chapter 9 we give a short introduction to the representation theory of finite dimensional algebras.

Besides, the book contains six historical interludes written by Dr. Slava Gerovitch.[^introduction-1] These interludes, written in an accessible and absorbing style, tell about the life and mathematical work of some of the mathematicians who played a major role in the development of modern algebra and representation theory: F. G. Frobenius, S. Lie, W. Burnside, W. R. Hamilton, H. Weyl, S. Mac Lane, and S. Eilenberg. For more on the history of representation theory, we recommend that the reader consult the references to the historical interludes, in particular the excellent book [Cu].

**Acknowledgments.** This book arose from the lecture notes of a representation theory course given by the first author to the remaining six authors in March 2004 within the framework of the Clay Mathematics Institute Research Academy for high school students and its extended version given by the first author to MIT undergraduate mathematics students in the fall of 2008.

The authors are grateful to the Clay Mathematics Institute for hosting the first version of this course. The first author is very indebted to Victor Ostrik for helping him prepare this course and thanks <span class="original-page-anchor" id="pdf-page-12" aria-hidden="true"></span>Josh Nichols-Barrer and Thomas Lam for helping run the course in 2004 and for useful comments. He is also very grateful to Darij Grinberg for his very careful reading of the text, for many useful comments and corrections, and for suggesting Problems 2.11.6, 3.3.3, 3.8.3, 3.8.4, 4.5.2, 5.10.2 and Exercises 5.27.2, 5.27.3, 7.9.8. Finally, the authors gratefully acknowledge the use of the Dynkin diagram pictures prepared by W. Casselman.

[^introduction-1]: I wish to thank Prof. Pavel Etingof and his co-authors for adding technical notes to my historical monograph. While they have made a commendable effort at a concise exposition, their notes, unfortunately, have grown in size and in the end occupied a better part of this volume. I hope the reader will forgive this preponderance of technicalities in what, in essence, is a history book. — S. Gerovitch.
