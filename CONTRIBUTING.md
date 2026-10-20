# 贡献指南

## 报告问题

使用 [Issue](https://github.com/cooolink/k-actionable-planning/issues/new/choose) 描述问题，附上经过脱敏的请求、实际表现和期望结果。涉及输出质量时，给出能说明问题的短例子。

## 修改规则

1. 在分支中修改，行为规则集中在 `SKILL.md`。
2. 保持通用性，不加入具体项目决定，不把个别案例写成普遍禁令。
3. 安装开发依赖并运行校验：

   ```bash
   python3 -m venv .venv
   .venv/bin/python -m pip install -r requirements-dev.txt
   .venv/bin/python scripts/validate.py
   ```

4. 涉及行为调整时，用实际请求检查是否改善原问题、是否改变确认边界，并在 PR 中说明；结构检查不能替代行为验证。
5. 更新 `CHANGELOG.md`；发布版本由维护者统一更新 `SKILL.md` 中的版本号并创建标签。

PR 请写清问题、最终变化和验证结果。无需为普通文档修正添加重复测试或无关工具。

提交贡献表示同意以本仓库的 [MIT 许可证](LICENSE) 提供该贡献。请勿提交未获授权的资料或包含个人信息的会话。
