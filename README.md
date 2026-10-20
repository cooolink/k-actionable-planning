# k-actionable-planning

[![校验](https://github.com/cooolink/k-actionable-planning/actions/workflows/validate.yml/badge.svg)](https://github.com/cooolink/k-actionable-planning/actions/workflows/validate.yml) · [版本与更新](CHANGELOG.md) · [MIT License](LICENSE)

面向 AI 助手的策划协作 Skill：理解完整需求，以事实和资源为依据，把方案写到能执行，并在交付前检查整体一致性。

重点是讲清楚、做得到，减少逐句打补丁、空泛概念和冗长的 AI 式表达。

## 适用场景

- 编写活动、传播、内容运营或项目执行方案。
- 修订已有方案，保留已确认设置，处理前后冲突。
- 审核方案是否有依据、能看懂、能执行。

它提供工作方法，不绑定具体行业、项目、模板、渠道数量或章节结构，也不代替专业领域的事实核验。

## 核心规则

| 方面 | 要求 |
| --- | --- |
| 背景 | 先读相关会话、资料和现有方案，再判断与修改 |
| 依据 | 区分事实、用户决定、建议和待确认事项，不凭空编造 |
| 协作 | 整体推进；举例不视为穷举，补充不擅自变成范围上限 |
| 执行 | 写清做什么、在哪里做、用户怎么操作、谁负责及何时完成 |
| 表达 | 结论在前，保留必要信息，删除空话、重复和术语包装 |
| 交付 | 检查全文关联与实际呈现，如实说明完成和验证范围 |

完整规则见 [SKILL.md](SKILL.md)。

## 快速开始

需要本机已安装 Git，并有支持 `SKILL.md` 的助手环境。

### Codex

将仓库克隆到个人 Skills 目录：

```bash
git clone https://github.com/cooolink/k-actionable-planning.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/k-actionable-planning"
```

如果目标目录已存在，先检查已有内容，不直接覆盖。手动复制安装的目录没有 Git 历史，不能直接执行下面的更新命令；可先备份，再按克隆方式重新安装。

当前发布版为 `v1.0.0`；需要固定版本时，在克隆命令中加入 `--branch v1.0.0`。固定标签安装适合保持规则稳定，跟随 `main` 安装适合获取后续更新。

### 更新

跟随 `main` 分支安装后，可执行：

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/k-actionable-planning" pull --ff-only
```

存在本地修改或分支分歧时，先检查差异，不强制覆盖。固定标签安装不使用此命令；更新到其他发布版时先运行 `git fetch --tags`，再切换到目标标签。

## 使用

在 Codex 对话中显式调用，并提供相关资料、目标和约束：

```text
使用 $k-actionable-planning 修订这份方案。
先阅读正文和相关讨论，保留已确认设置，检查逻辑与执行路径。
表达简洁，必要处举例，直接更新正文。
```

只审核、不修改时：

```text
使用 $k-actionable-planning 审核这份方案，暂不修改文件。
指出有依据的问题、对执行的影响，以及具体修改建议。
```

先讨论时：

```text
使用 $k-actionable-planning 梳理需求和可行方向，先给我确认，不创建文件。
```

Skill 不扩大任务授权。是否修改文件、同步其他版本或执行发布，仍以当前任务要求为准。

## 工作方式

理解背景与约束 → 明确问题和目标 → 判断可行路径 → 写清操作与责任 → 检查全文及交付。

这是一条判断路径，不要求每一步都向用户确认。信息充分时继续推进；缺少会影响决策的关键信息时再问。

## 仓库结构

| 路径 | 用途 |
| --- | --- |
| [SKILL.md](SKILL.md) | 助手读取的规则，包含名称、描述、许可证和版本 |
| [agents/openai.yaml](agents/openai.yaml) | Codex 展示名称与简介 |
| [CHANGELOG.md](CHANGELOG.md) | 版本变化 |
| [CONTRIBUTING.md](CONTRIBUTING.md) | 提交问题、修改规则及验证方法 |
| [scripts/validate.py](scripts/validate.py) | 元数据、版本及本地文档链接检查 |
| [.github/workflows/validate.yml](.github/workflows/validate.yml) | 推送和 PR 自动校验 |

## 校验与维护

使用 Skill 无需安装 Python 依赖。修改仓库时，Python 校验工具需要 [requirements-dev.txt](requirements-dev.txt) 中的开发依赖；安装与执行方法见 [贡献指南](CONTRIBUTING.md)。

自动校验检查文件、元数据和链接，不判断策划质量。规则变更还需结合实际请求检查行为。

问题反馈请提交 [Issue](https://github.com/cooolink/k-actionable-planning/issues/new/choose)。发布与变更见 [更新记录](CHANGELOG.md)。

## 许可证

采用 [MIT License](LICENSE)，允许修改、分发和商用，须保留版权及许可声明。
