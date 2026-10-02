# 个人主页

纯 HTML/CSS 的单页学术风个人主页，零依赖、零构建，托管在 GitHub Pages。

- 风格：单页滚动（简介 / 研究兴趣 / 论文 / 项目 / 笔记 / 联系）
- 特性：深色模式（跟随系统 + 手动切换）、响应式、可打印成 PDF、无 JS 依赖也可读
- 上线后地址：`https://luyiming123.github.io/homepage/`

---

## 一、改内容只需要动两个地方

| 想改什么 | 改哪里 |
| --- | --- |
| **页面上所有文字** | `index.html`（每个章节都有注释，占位文字均标注「示例」） |
| **颜色 / 字号 / 间距** | `assets/style.css` 顶部的 CSS 变量 `:root { … }` |

`index.html` 里需要你替换的占位项：

- 姓名 `Yiming Lu` / `卢一鸣`，以及 `<title>`、`<meta name="description">`
- 邮箱 `your-email@example.com`（出现 2 处）
- 简介、研究兴趣、论文、项目、笔记表格里的示例文字
- 头像：把方形照片存为 `assets/avatar.jpg`，然后删掉 `index.html` 里头像那段注释的包裹标记
- CV：把简历 PDF 存为 `assets/cv.pdf`，并把导航里的 `assets/cv-placeholder.txt` 改掉
- **上线后**：把 `index.html` 里的 `canonical` 和 `og:url` 改成你的真实网址，这样分享到社交平台会显示正确卡片

## 二、本地预览

改完想先看看效果，在 `homepage` 目录下起一个本地服务器（**不要直接双击 index.html**，
`file://` 协议下某些样式和相对路径行为和线上不一致）：

```powershell
cd C:\Users\luyiming123\Documents\deepseek-harness\default-workspace\homepage

# 有 Python 的话（你机器上有）
python -m http.server 8000

# 或者用 Node
npx serve -l 8000
```

然后浏览器打开 http://localhost:8000/ 。

## 三、发布上线

```powershell
cd C:\Users\luyiming123\Documents\deepseek-harness\default-workspace\homepage
git add -A
git commit -m "更新主页内容"
git push
```

推送后 GitHub Actions 自动发布，约 1 分钟生效。

## 四、首次上线要做的两件事

1. **在 GitHub 新建仓库**，名字填 `homepage`（Public），不要勾选任何初始化文件：

   ```powershell
   git remote add origin git@github.com:luyiming123/homepage.git
   git push -u origin main
   ```

2. 打开仓库 → **Settings → Pages → Source 选 `GitHub Actions`**（不要选 Deploy from a branch）

之后访问 `https://luyiming123.github.io/homepage/`。

> 换仓库名也行，但链接会跟着变（`https://luyiming123.github.io/<仓库名>/`），
> 记得同步改 `index.html` 里的 `canonical` 与 `og:url`。
> 想用自定义域名：在仓库根目录加一个内容为域名的 `CNAME` 文件，并在域名商处加 CNAME 解析。

## 五、目录结构

```
homepage/
├─ index.html                  # 页面内容（★ 主要改这个）
├─ assets/
│  ├─ style.css                # 样式（★ 颜色在这里）
│  ├─ favicon.svg              # 站点图标
│  ├─ favicon.ico / -32x32.png / apple-touch-icon.png
│  └─ cv-placeholder.txt       # 放上真实 CV 后删掉
├─ scripts/
│  ├─ make-icons.py            # 重新生成图标（改了姓名缩写或配色后才需要跑）
│  └─ check-workflow.py        # 校验 .github/workflows/pages.yml 结构（可选）
├─ .github/workflows/pages.yml # 自动部署
└─ README.md
```

## 六、可以后续加的东西

- 中英双语切换（现在只有中文版；如需英文版，复制一份 `index-en.html` 并互相加语言链接）
- 论文页 / 教学页拆成独立子页
- Google Scholar、ORCID、知乎等更多社交链接

---

内容许可：CC BY-NC-SA 4.0 ｜ 代码：MIT
