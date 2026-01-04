---

description: "Task list for feature implementation: 卡路里日记（Calorie Journal）"

---

# Tasks: 卡卡（1-calorie-journal）

**Input**: specs/1-calorie-journal/spec.md, specs/1-calorie-journal/plan.md
**Owner**: 待分配
**Estimation Unit**: 人-天（1d = 一位开发者工作日）

---

## Phase 0: Setup (Shared Infrastructure)

Purpose: project repo structure, CI, lint, env example

- [ ] T001 (0.5d) 创建仓库结构与目录：`backend/`, `frontend/`, `docs/`, `scripts/`，并添加 README、LICENSE
- [ ] T002 (0.5d) 初始化 CI（GitHub Actions）：lint、测试、build pipelines；为后续 PR 强制检查
- [ ] T003 (0.5d) 添加根目录 `/.env.example` 并在 `.gitignore` 中列出 `/.env`
- [ ] T004 (0.5d) 设置 repo 格式化与静态检查（ESLint/Prettier 前端，ESLint/TypeScript 后端/Nest 规范或兼容工具）

---

## Phase 1: Foundational (Blocking Prerequisites)

Purpose: DB schema, auth, logging, monitoring

- [ ] T005 (1.0d) 定义 Prisma schema（初稿包含 User、Article、Tag、Comment、ArticleImage、ArticleFoodRef、AuditLog）并生成初始 migration
- [ ] T006 (1.0d) 搭建开发用 MySQL（Docker Compose）并编写本地 dev 快速启动脚本
- [ ] T007 (1.0d) 实现 Auth（JWT + Refresh Token），基础 User registration/login endpoints
- [ ] T008 (1.0d) 集成基础日志（pino）与错误追踪（Sentry）配置
- [ ] T009 (0.5d) Redis 容器配置（缓存与短时队列）
- [ ] T010 (0.5d) 制定 DB 迁移与回滚策略文档

Checkpoint: Foundational 完成后可并行实现文章与图片子系统

---

## Phase 2: Article Core

Purpose: Article CRUD、Tag、Comment、Markdown rendering

- [ ] T011 (2.0d) 实现 Article 模型与 CRUD endpoints（POST/GET/PUT/DELETE）、含软删除
- [ ] T012 (1.0d) 实现 Tag 模型与 Tag 管理（创建去重、计数更新、按标签过滤 API）
- [ ] T013 (1.0d) 实现 Comment 模型与评论分页 API（含权限校验、删除/隐藏）
- [ ] T014 (1.0d) 实现 Markdown 渲染 pipeline（/api/markdown/preview），集成 remark+rehype+rehype-sanitize，并对应单元测试
- [ ] T015 (1.0d) 实现 Article 编辑/发布前的验证（长度限制、标签合法性、XSS 防护验证）
- [ ] T016 (1.0d) 添加 audit logging（Article/Comment 的 create/update/delete 事件）并写入 AuditLog 表
- [ ] T017 (1.0d) 添加 Article 图片元数据模型与 API （ArticleImage）用于显示图片列表与元信息

Acceptance for Phase 2: Article create->list->detail->comment 完整 E2E 流程通过

---

## Phase 3: Image Upload & Processing

Purpose: Presigned uploads、sharp 处理、CDN 减速

- [ ] T018 (1.0d) 实现 /api/uploads/presigned endpoint（生成 presigned URL 或 uploadUrl）
- [ ] T019 (1.0d) 实现 /api/uploads/complete endpoint（记录上传完成、入队生成缩略图）
- [ ] T020 (1.0d) 集成 image processing worker（sharp）生成缩略图与 WebP，存储 metadata 至 ArticleImage
- [ ] T021 (0.5d) 前端上传组件：支持 presigned 上传、进度条、失败重试
- [ ] T022 (0.5d) 配置 CDN（本地可先使用 MinIO + 本地代理）并测试 CORS 与缓存 headers

Acceptance: 图片上传成功并在 60s 内为文章显示缩略图，图片类型/大小验证通过

---

## Phase 4: Search, Pagination & Performance

Purpose: 高效查询与搜索体验

- [ ] T023 (1.0d) 实现文章列表分页与 tag 过滤（DB 索引调优）
- [ ] T024 (2.0d) 为全文搜索接入 MeiliSearch（或 Elastic）并实现同步策略（事件驱动或定时批量）
- [ ] T025 (0.5d) 添加缓存层（Redis）用于热点列表/标签结果缓存与失效策略
- [ ] T026 (0.5d) 添加监控与性能基线脚本（加载测试脚本）

---

## Phase 5: SRS Integration (AI 食物引用 & Admin Audit)

Purpose: 与 AI 识图与食物记录的集成

- [ ] T027 (1.0d) ArticleFoodRef 模型与 API：允许 article 引用 FoodDict 或 FoodRecord
- [ ] T028 (1.0d) 管理端审核流：显示用户提交的食物申请并批准/拒绝；批准后更新 FoodDict
- [ ] T029 (1.0d) 当 AI 识别出新食物时，支持文章中嵌入占位条目并在后续补全

---

## Phase 6: QA, Security & Deployment

Purpose: 测试、安全审计、部署脚本

- [ ] T030 (1.0d) 编写全面集成测试与 E2E 流程（Cypress 或 Playwright）
- [ ] T031 (1.0d) 进行 XSS 安全扫描与上传漏洞测试
- [ ] T032 (1.0d) 准备 Dockerfile、docker-compose.yml 与基础 K8s manifests（示例）
- [ ] T033 (0.5d) 完成 CI 流程：单元 + 集成 + E2E（必要时在 PR 运行轻量 E2E）

---

## Phase 7: Polish & Release

- [ ] T034 (0.5d) CHANGELOG 与发布说明
- [ ] T035 (0.5d) 监控/告警运行与回滚演练
- [ ] T036 (0.5d) 性能调优与用户体验小改动

---

## Dependencies & Notes
- T005 (Prisma schema) 应先完成，避免架构重做
- 图片尺寸与格式策略需与前端约定（最大 5MB, jpg/png/webp 推荐）
- 所有任务需包含相应的测试任务（单元/集成/E2E）

## Next
- 我将开始生成 Prisma schema（`prisma/schema.prisma`）并把任务 3 标记为进行中。