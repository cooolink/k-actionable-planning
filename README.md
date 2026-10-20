# k-actionable-planning

**落地策划与整体协作**

让 AI 先理解完整需求，再把方案写清楚：做什么、在哪里做、谁负责、如何推进。适用于方案编写、修订与审核。

[![校验](https://github.com/cooolink/k-actionable-planning/actions/workflows/validate.yml/badge.svg)](https://github.com/cooolink/k-actionable-planning/actions/workflows/validate.yml)
[版本](https://github.com/cooolink/k-actionable-planning/releases/latest) · [MIT License](LICENSE) · [完整规则](SKILL.md)

[安装](#安装) · [使用](#使用) · [具体示例](#具体示例) · [更新](#更新) · [参与维护](#参与维护)

## 安装

在终端执行以下命令，将 Skill 安装到 Codex 个人目录。需要已安装 Git。

```bash
git clone https://github.com/cooolink/k-actionable-planning.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/k-actionable-planning"
```

目标目录已存在时先检查内容，避免覆盖。安装后在下一轮对话中使用 `$k-actionable-planning` 调用。

## 使用

提供方案或资料，并说明当前要讨论、审核还是直接修改。

**写方案**

```text
使用 $k-actionable-planning，根据这些资料编写执行方案。
先理解目标、受众和资源；写清内容、渠道、操作、分工与节点。
关键条件拿不准时先问，表达简洁。
```

**改方案**

```text
使用 $k-actionable-planning，通读并修改这份方案。
保留已确认设置，处理全文同类问题和前后冲突，不只修改我指出的位置。
直接更新正文。
```

**先审核**

```text
使用 $k-actionable-planning，检查这份方案是否有依据、看得懂、做得到。
列出具体问题和修改建议，先不修改文件。
```

## 具体示例

下面是说明写法的示例，不是实际活动结果。

> **只有概念**：通过多渠道传播增强互动，形成传播闭环。
>
> **写到操作**：运营在活动前一周发布报名说明，附报名表链接；用户提交后收到确认，运营每个工作日处理疑问。活动结束后整理共性问题，发布答复并通知报名用户。

实际方案应根据资源确定渠道、时间和负责人，不能把示例直接当成既定安排。

## 它如何处理需求

| 情况 | 处理方式 |
| --- | --- |
| 用户补充要求 | 结合原目标整合，保留此前有效决定 |
| 用户给出示例或主要渠道 | 用于理解方向，不自动视为完整清单或范围上限 |
| 发现一处问题 | 检查同类问题及前后关联，整体修订 |
| 缺少关键依据 | 核实或询问，不编造事实、数据和功能 |
| 信息已充分 | 直接推进，不机械分段确认 |
| 交付 | 检查内容及实际呈现，简短说明结果与待定项 |

Skill 提供协作规则，不绑定固定模板，也不自动授权修改文件或对外发布。完整要求见 [SKILL.md](SKILL.md)。

## 更新

通过上面的克隆命令安装后，更新 `main` 分支：

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/k-actionable-planning" pull --ff-only
```

本地有修改时先检查差异。手动复制安装的目录没有 Git 历史，需要备份后重新克隆。

<details>
<summary>固定版本安装</summary>

需要保持规则稳定时，使用已发布标签，例如：

```bash
git clone --branch v1.0.1 https://github.com/cooolink/k-actionable-planning.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/k-actionable-planning"
```

标签安装不跟随 `main` 更新。切换版本前先获取标签，并检查本地修改：

```bash
git -C "${CODEX_HOME:-$HOME/.codex}/skills/k-actionable-planning" fetch --tags
```

查看 [发布版本](https://github.com/cooolink/k-actionable-planning/releases)，再在该目录中执行 `git switch --detach <目标标签>`。

</details>

## 参与维护

- 使用问题或改进建议：[提交 Issue](https://github.com/cooolink/k-actionable-planning/issues/new/choose)。
- 修改规则与运行校验：[贡献指南](CONTRIBUTING.md)。
- 版本变化：[更新记录](CHANGELOG.md)。
- 授权：采用 [MIT License](LICENSE)。

使用 Skill 无需 Python 依赖。维护工具只检查元数据、版本和文档链接，不能代替实际使用验证。
