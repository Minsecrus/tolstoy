---
title: "信息检索导论"
description: "《Introduction to Information Retrieval》中文译本。"
---

# 信息检索导论中文译文

本系列依据用户提供的 *Introduction to Information Retrieval* PDF，按原书顺序分章翻译。作者为 Christopher D. Manning、Prabhakar Raghavan 和 Hinrich Schütze；底本为剑桥大学出版社 2009 年 4 月 1 日网络草稿版。

正文共 21 章，每章一个 Markdown 文件。扉页、目录、符号表与前言合为一篇，参考文献、作者索引和中英术语索引分别成篇。

## 版本与页码

- 原 PDF 共 581 页；印刷页第 1 页对应 PDF 第 38 页，正文页码换算为“PDF 页码 = 印刷页码 + 37”。
- 前置材料使用罗马数字页码；正文、参考文献和索引使用阿拉伯数字页码。扉页和空白页未印出的页码按其位置推定。
- 每个原书页面在译文中都有 `<!-- source: PDF …; printed: … -->` 标记，方便对照底本。19 个空白页保留位置标记。
- 原书的章节编号、编号公式、图表编号、习题编号、脚注和交叉引用随正文保留；印刷页码均指底本页码。
- 原书介绍的系统、实验结果和 Web 数据具有当时的时间背景，译文保留这一历史语境。

## 开始阅读

- [扉页、目录、符号表与前言](/library/volume-90/chapter-001)

## 正文章节

- [第 1 章 布尔检索](/library/volume-90/chapter-002) · 原书第 1–18 页
- [第 2 章 词项词汇表与倒排记录表](/library/volume-90/chapter-003) · 原书第 19–48 页
- [第 3 章 词典与容错检索](/library/volume-90/chapter-004) · 原书第 49–66 页
- [第 4 章 索引构建](/library/volume-90/chapter-005) · 原书第 67–84 页
- [第 5 章 索引压缩](/library/volume-90/chapter-006) · 原书第 85–108 页
- [第 6 章 评分、词项加权与向量空间模型](/library/volume-90/chapter-007) · 原书第 109–134 页
- [第 7 章 完整搜索系统中的评分计算](/library/volume-90/chapter-008) · 原书第 135–150 页
- [第 8 章 信息检索的评估](/library/volume-90/chapter-009) · 原书第 151–176 页
- [第 9 章 相关反馈与查询扩展](/library/volume-90/chapter-010) · 原书第 177–194 页
- [第 10 章 XML 检索](/library/volume-90/chapter-011) · 原书第 195–218 页
- [第 11 章 概率信息检索](/library/volume-90/chapter-012) · 原书第 219–236 页
- [第 12 章 用于信息检索的语言模型](/library/volume-90/chapter-013) · 原书第 237–252 页
- [第 13 章 文本分类与朴素贝叶斯](/library/volume-90/chapter-014) · 原书第 253–288 页
- [第 14 章 向量空间分类](/library/volume-90/chapter-015) · 原书第 289–318 页
- [第 15 章 支持向量机与文档机器学习](/library/volume-90/chapter-016) · 原书第 319–348 页
- [第 16 章 平面聚类](/library/volume-90/chapter-017) · 原书第 349–376 页
- [第 17 章 层次聚类](/library/volume-90/chapter-018) · 原书第 377–402 页
- [第 18 章 矩阵分解与潜在语义索引](/library/volume-90/chapter-019) · 原书第 403–420 页
- [第 19 章 Web 搜索基础](/library/volume-90/chapter-020) · 原书第 421–442 页
- [第 20 章 Web 爬取与索引](/library/volume-90/chapter-021) · 原书第 443–460 页
- [第 21 章 链接分析](/library/volume-90/chapter-022) · 原书第 461–482 页

## 参考资料与索引

- [参考文献](/library/volume-90/chapter-023)：保留作者、英文题名、发表信息和原文链接，附中文题名。
- [作者索引](/library/volume-90/chapter-024)：保留原书作者姓名及所关联的文献。
- [中英术语索引](/library/volume-90/chapter-025)：按原书英文词条顺序排列，保留中文译名、英文词条、页码和“见／另见”关系。

## 阅读约定

- **术语**：词项（term）、词元（token）、词型（type）分别处理；倒排记录（posting）与倒排记录表（postings list）保持区分。
- **评估指标**：precision 译为“查准率”，recall 译为“召回率／查全率”，accuracy 译为“准确率”，避免把两个不同指标混为一谈。
- **检索示例**：用于词项匹配、分词、拼写校正和分类的英文词、查询、文档样例及程序标识符保留原样，解释和题目译为中文。
- **公式**：行内使用 `$...$`，独立公式使用 `$$...$$`；原书编号通过 `\tag{...}` 保留。
- **图表与算法**：可转写的表格、矩阵、文档样例和伪代码以 Markdown、TeX 或代码块呈现；图形从原 PDF 截取，图题和图内标签另附中文说明。
- **脚注**：采用页内注释，标明原书脚注号和页码，避免合并章节后脚注编号冲突。

## 制作与核查

这份中文学习译稿采用 AI 辅助翻译，输入包含原 PDF 页面图像和提取文本。核查包括页码覆盖、公式与习题编号、章节导航、图片引用及 VitePress／MathJax 渲染，并对代表性正文、公式、图表和索引页作对照抽查。这些检查不等同于全书逐句人工审校。

同目录的 `source-manifest.json` 记录了底本指纹、页面对应关系和图像来源。原书作者与出版社信息、版权声明见前置材料；译文中的新增说明仅用于交代整理方式。

[从第 1 章开始](/library/volume-90/chapter-002)
