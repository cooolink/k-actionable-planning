#!/usr/bin/env python3
"""检查 Skill 元数据、仓库文件及 Markdown 本地链接。"""

import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml


def validate(root):
    errors = []
    required = (
        'SKILL.md', 'README.md', 'LICENSE', 'CHANGELOG.md',
        'CONTRIBUTING.md', 'agents/openai.yaml',
        '.github/workflows/validate.yml', 'requirements-dev.txt',
    )
    for name in required:
        if not (root / name).is_file():
            errors.append(f'缺少文件：{name}')
    if errors:
        return errors

    skill = (root / 'SKILL.md').read_text(encoding='utf-8')
    front = re.match(r'\A---\n(.*?)\n---\n', skill, re.S)
    if not front:
        return ['SKILL.md 缺少有效的 YAML 元数据区。']
    try:
        meta = yaml.safe_load(front.group(1))
        if not isinstance(meta, dict):
            return ['Skill 元数据必须是映射。']
        name = meta.get('name')
        if name != 'k-actionable-planning':
            errors.append('Skill 名称与仓库调用名称不一致。')
        description = meta.get('description')
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            errors.append('description 必须为 1—1024 字符的文本。')
        if meta.get('license') != 'MIT':
            errors.append('Skill 许可证须与 LICENSE 一致。')
        metadata = meta.get('metadata')
        version = metadata.get('version') if isinstance(metadata, dict) else None
        if not isinstance(version, str) or not re.fullmatch(r'\d+\.\d+\.\d+', version):
            errors.append('metadata.version 须为带引号的三段版本号。')
        elif f'## {version} ' not in (root / 'CHANGELOG.md').read_text(encoding='utf-8'):
            errors.append('当前版本缺少更新记录。')
        ui = yaml.safe_load((root / 'agents/openai.yaml').read_text(encoding='utf-8'))
        interface = ui.get('interface', {}) if isinstance(ui, dict) else {}
        if interface.get('display_name') != name:
            errors.append('展示名称与 Skill 名称不一致。')
        short = interface.get('short_description')
        if not isinstance(short, str) or not 25 <= len(short) <= 64:
            errors.append('展示简介须为 25—64 字符。')
        # 使用 BaseLoader 保留工作流 on 等 YAML 键的原始含义。
        for path in root.glob('.github/**/*.y*ml'):
            yaml.load(path.read_text(encoding='utf-8'), Loader=yaml.BaseLoader)
    except yaml.YAMLError as exc:
        errors.append(f'YAML 格式错误：{exc}')

    for path in root.rglob('*.md'):
        if any(part.startswith('.') for part in path.relative_to(root).parts[:-1]):
            continue
        text = path.read_text(encoding='utf-8')
        fence = None
        prose = []
        for line in text.splitlines():
            marker = re.match(r'^\s*(`{3,}|~{3,})(.*)$', line)
            if marker:
                token, suffix = marker.groups()
                if fence is None:
                    fence = token
                elif token[0] == fence[0] and len(token) >= len(fence) and not suffix.strip():
                    fence = None
            elif fence is None:
                prose.append(line)
        if fence is not None:
            errors.append(f'未闭合代码块：{path.relative_to(root)}')
        for link in re.findall(r'(?<!!)\[[^\]]*\]\(([^\s)]+)\)', '\n'.join(prose)):
            target = urlsplit(link)
            if target.scheme or target.netloc or not target.path:
                continue
            dest = (path.parent / unquote(target.path)).resolve()
            if not dest.is_relative_to(root.resolve()) or not dest.exists():
                errors.append(f'无效本地链接：{path.relative_to(root)} → {link}')
    return errors


def main():
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    errors = validate(root)
    if errors:
        print('\n'.join(f'ERROR: {message}' for message in errors))
        return 1
    print('校验通过：元数据、版本记录、YAML、代码块及本地文档链接。')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
