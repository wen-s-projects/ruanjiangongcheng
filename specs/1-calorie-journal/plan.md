# Implementation Plan: 卡路里日记（Calorie Journal）

**Feature**: `1-calorie-journal`  
**Owner**: 待分配  
**Created**: 2026-01-04  
**Status**: Draft

---

## 目标（Scope）
实现文章发布系统（支持 Markdown）、标签分类、评论功能；并与现有食物/卡路里记录（FoodDict / FoodRecord）建立可选引用关系，保持手机端与网页端一致的使用体验。后端采用 Node.js（NestJS + TypeScript），数据库采用 MySQL（兼容现有 schema）。

> 注意：此实现偏离项目宪法中对后端使用 Django 的声明；已记录为特性级例外，需维护者批准（见下文）。

---

## 里程碑与高阶时间表（建议）
- Phase 0（1–2d）: 项目初始化（mono-repo 结构、CI、`.env.example`、基础 lint/formatter）
- Phase 1（3–6d）: Foundational — DB schema (Prisma)、Auth、基本用户/角色、日志、监控
- Phase 2（5–8d）: Article 基础 — Article/Tag/Comment 模型、CRUD、单元测试、Markdown render pipeline
- Phase 3（3–5d）: 图片上传（presigned）与处理（sharp）、缩略图、CDN 集成
- Phase 4（2–4d）: 搜索、分页与过滤（标签过滤、全文检索接入 Meili/Elastic）
- Phase 5（3–6d）: SRS 集成：AI 食物引用、管理端审核流程、周边交互
- Phase 6（2–4d）: QA、压力测试、性能优化与部署（Docker/K8s）
- Phase 7（1–3d）: 上线后的监控策略与回滚跑演练

（估时为单一开发者参考，按团队规模调整）

---

## 技术选型与原因
- 后端框架：**NestJS (TypeScript)** — 模块化、强 DI、与团队 TypeScript 生态契合，测试/可维护性优秀。  
- ORM：**Prisma** — 类型安全、迁移工具友好、易写测试与种子数据。  
- Markdown 解析：**remark + rehype + rehype-sanitize** — 安全可配置，适合服务端与客户端一致性渲染。  
- 图片上传：**S3-compatible + presigned upload**（在本地可用 MinIO 测试）+ **sharp** 做处理与缩略图生成。  
- 搜索：短期可用 MySQL 索引与 LIKE + 标签索引，长期建议 **MeiliSearch** 或 **Elastic**。  
- 缓存与队列：**Redis**（缓存、限流、短时任务队列）。  
- 安全：JWT（HTTP-only cookie）或 Authorization header；XSS 防护在渲染 pipeline 严格 sanitize；图片白名单与尺寸/大小限制。  

---

## 数据库建模（变更摘要）
基于 `Design/Database_Schema.md`，新增/修改的表：
- `Article` (ArticleID, AuthorID, Title, Slug, Markdown, RenderedHTML, Status, AllowComments, CreatedAt, UpdatedAt)
- `Tag` (TagID, Name, Slug, Count)
- `ArticleTag` (ArticleID, TagID)
- `Comment` (CommentID, ArticleID, AuthorID, Content, Status, CreatedAt)
- `ArticleImage` (ImageID, ArticleID, Url, ThumbUrl, Width, Height, CreatedAt)
- `ArticleFoodRef` (RefID, ArticleID, FoodID, FoodRecordID, Note)
- `AuditLog` (LogID, EntityType, EntityID, Action, ActorID, Data, CreatedAt)

设计原则：遵循现有 User/FoodDict/FoodRecord 命名风格；Tag 去重并规范大小写；保留 Markdown 原文与渲染后的 HTML 以支持编辑与预览；将图片存储在 S3 并在 DB 中保存 URL 与元数据。

---

## API 设计（核心端点）
- GET /api/articles?tag=&page=&size=&search=  — 列表、过滤、分页
- GET /api/articles/:id  — 详情（包含渲染 HTML、标签、评论、图片、关联食物引用）
- POST /api/articles  (auth) — 创建
- PUT /api/articles/:id (author) — 编辑
- DELETE /api/articles/:id (author/admin) — 删除（软删除）
- POST /api/articles/:id/comments (auth) — 创建评论
- GET /api/articles/:id/comments?page=  — 评论分页
- POST /api/uploads/presigned  — 生成 presigned upload URL
- POST /api/uploads/complete  — 完成上传后通知并触发缩略图任务
- POST /api/markdown/preview — 渲染与 sanitize（供实时预览用）

认证：JWT + refresh token；管理端基于 role 的鉴权。

---

## 核心流程（发布文章示例）
1. 前端上传图片到 S3（presigned）并获得 URL（或直接上传并返回 URL）。
2. 用户在客户端编辑 Markdown，使用 /api/markdown/preview 获取实时渲染预览（同一渲染 pipeline）。
3. 提交文章：后端校验长度/标签/图片域合法性，创建新标签（去重）并保存 Article（包含 Markdown 与 RenderedHTML）。
4. 写入 AuditLog，触发异步任务：生成缩略图、更新 Tag count、索引（Meili/Elastic）、更新缓存（Redis）。
5. 返回 201 与文章详情。

---

## 非功能需求对齐（SLO / 性能）
- 首屏渲染目标：< 2s（正常网络）  
- 新发布文章在 5s 内可见于列表（缓存与索引异步更新策略）  
- 标签过滤查询 95% 响应 < 1s（基线）

---

## 测试策略
- 单元测试：模型、service、markdown sanitize、tag 去重逻辑  
- 集成测试：Article CRUD 流程、评论分页、图片上传完整流程  
- E2E：Login → 创建文章（含图片与标签）→ 发布 → 列表/详情验证  
- 安全测试：XSS 自动化扫描、上传文件类型验证、登录权限测试

---

## 部署 & 运维建议
- 使用 Docker + Docker Compose（开发/测试），生产建议使用 Kubernetes 或 ECS；配套使用 Redis、MinIO（测试）、MySQL、Sentry。  
- 使用 CI（GitHub Actions）在 PR 中运行测试、lint、迁移检查并生成 artifact。  
- 监控：Sentry + Prometheus/Grafana（请求延迟、错误率、队列长度、缩略图队列失败率）。

---

## 风险、回退与治理
- 宪法冲突：后端技术栈变更需记录为特性例外并获得至少 2 位核心维护者批准。  
- 图片存储成本：建议先使用 MinIO 并评估到 S3 的迁移成本；回退策略：若上传链路发生故障，使用后端代理上传并降级服务。  
- XSS/外链风险：使用严格 sanitize 策略并对外链图片使用代理或 CDN 缓存以减少攻击面。  

---

## 交付物（本次迭代）
- `plan.md`（本文件）  
- `tasks.md`（待生成）  
- `prisma/schema.prisma` 与初始 migration（待生成）  
- `backend/` skeleton（NestJS + Prisma + Docker + CI）（待生成）  

---

## 批准/例外记录（草案）
- 说明：本特性选择 Node.js/NestJS 替代宪法中规定的 Django 实现。  
- 建议流程：在 PR 描述中注明此例外并列出理由（团队熟练度、TypeScript 优势、生态需求）；至少 2 位维护者批准后方可合并。  

---

**Next**: 我将把 `tasks.md` 生成为下一个待办，并把该任务标为进行中。