# 文学作品阅读站

在线阅读：[https://minsecrus.github.io/tolstoy/](https://minsecrus.github.io/tolstoy/)

## 使用

```powershell
npm install
npm run docs:dev
```

用 `npm run docs:build` 验证站点。部署在子路径时，可通过
`VITEPRESS_BASE` 设置基础路径，例如 `/russian-literature/`。

正文使用到的注释会添加在对应页面末尾；正文标号和注释后的返回箭头可以在本页内双向跳转。
`npm run books:check-footnotes` 会检查全部脚注和返回链接；该检查也会在构建前自动运行。
