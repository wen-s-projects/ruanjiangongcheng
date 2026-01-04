<!--
Sync Impact Report
- Version change: unknown → 1.0.0
- Modified/Added principles:
  - 新增: Modern Stack & Architecture (前端 Vue3, 后端 Django, MySQL)
  - 新增: Environment & Secrets Management (.env 根目录统一管理)
  - 新增: 文档要求 (中文优先)
  - 新增: Test & CI Requirements
  - 新增: Observability & Versioning
- Added sections: Security & Data Handling; Development Workflow
- Removed sections: none
- Templates requiring updates:
  - .specify/templates/spec-template.md ✅ updated
  - .specify/templates/tasks-template.md ✅ updated
- Follow-up TODOs:
  - TODO(RATIFICATION_DATE): 请在批准时填写宪法的实际采纳日期
  - 手动检查 CI 配置（`.github/workflows/*`、`azure-pipelines.yml` 等）是否依赖或调用 `.specify` 脚本（⚠ pending）
  - 审查 `.claude/commands/` 中 agent-specific 名称（如 claude）并在需要时改为通用指令（⚠ pending）
-->

# 项目宪法（Modern 双端软件项目）

## Core Principles

### 1. Modern Stack & Architecture
- 本项目的**前端**必须采用 **Vue 3**（推荐使用 Composition API + TypeScript），并遵循组件驱动设计与模块化最佳实践。
- **后端**必须采用 **Django**（建议使用 Django REST Framework 提供 API）。服务间通信应使用明确的 HTTP/REST 或 gRPC 协议并有契约（contracts）文档。
- **数据库**必须为 **MySQL**（版本信息在规格中声明），所有数据库变更通过迁移工具（Django Migrations）管理并包含回滚说明。
- 理由：统一技术栈能减少认知负担，加速新成员入门并提升长期可维护性。

### 2. Environment & Secrets Management
- 所有运行时配置与环境变量应集中管理，开发时在仓库根目录维护一份示例文件 `/.env.example`，真正的敏感信息不得提交到仓库，生产环境应使用机密管理（Secret Manager）。
- 本地开发可以使用 `/.env`（列入 `.gitignore`）来读取环境变量，CI/CD 管道必须使用受控的机密注入方式。
- 理由：集中管理环境变量能显著降低配置混乱与泄露风险，并使本地/CI 环境一致。

### 3. 文档优先（中文）
- 所有**用户文档、开发者文档、API 文档与快速入门指南**应以**简体中文**为主，必要时可提供英文摘要或双语片段以便外部协作。
- 文档必须包含清晰的本地开发（Quickstart）、部署流程、环境配置（包括 `.env.example` 说明）和常见故障排查步骤。
- 理由：使用单一语言可以提高内部沟通效率和知识共享质量，降低误解。

### 4. Test-First & CI Enforcement (NON-NEGOTIABLE)
- 单元测试、集成测试和关键路径的端到端测试必须随代码一起编写。对后端：覆盖模型、序列化、视图等关键逻辑；对前端：组件及关键交互覆盖。
- 所有 PR 必须通过自动化测试套件并在 CI 中运行静态检查（前端：ESLint/TypeScript；后端：flake8/Black 或等价工具）。
- 理由：Test-First 能确保设计可测试、减少回归并维持交付速度。

### 5. Observability, Versioning & Release Practices
- 所有服务必须产生日志（结构化 JSON）和错误监控集成（如 Sentry 或等价方案），并有基本的指标暴露（请求延迟、错误率、数据库连接数等）。
- 发布必须遵循语义化版本（SemVer），重大不兼容改动需在宪法中记录并在 PR 中说明迁移策略。变更日志（CHANGELOG）应记录用户可见的变更。
- 理由：可观测性与明确的版本控制减少运维负担并提升回溯与排查效率。

## Security & Data Handling
- 敏感数据传输必须使用 TLS；在数据库中存储敏感数据时应使用加密或哈希，根据法律/合规要求采取必要保护措施。
- 数据备份与恢复策略必须有文档并周期性演练。

## Development Workflow
- PR 要求：至少一名代码审查者通过且 CI 绿灯（测试+静态检查）后方可合并；重大设计变化需书面说明并征得核心维护者同意。
- 格式化工具与 lint 配置：前端推荐使用 ESLint + Prettier + TypeScript，后端推荐使用 Black + flake8 或等价工具，并在 CI 中强制执行。
- 任务拆分与模板：任务必须基于 `spec.md` 中的用户故事拆分并在 `tasks.md` 中维护可验收的测试点。

## Governance
- 宪法优先于其他实践；任何与宪法冲突的实践、模板或任务必须通过显式修订流程来解决。
- 宪法修改流程：提出修订 → 更新本文件草案并说明影响 → 至少 2 名核心维护者审阅并批准 → 更新受影响模板/脚本 → 将 `LAST_AMENDED_DATE` 设为批准日期并提交更改。重大或不兼容性的原则重定义需要 MAJOR 版本号升级。
- 合规检查：在关键发布前和每季度进行一次宪法合规审查（自动化脚本或人工审核）。

**Version**: 1.0.0 | **Ratified**: TODO(RATIFICATION_DATE) | **Last Amended**: 2026-01-04
