#!/usr/bin/env python3
"""docstring_gen —— 解析函数签名生成 Google 风格 docstring。

用 ast 提取函数名、参数、返回注解，生成占位 docstring。
零第三方依赖。

用法：
    from docstring_gen import gen_docstring
    print(gen_docstring(source, "add"))
"""
from __future__ import annotations

import argparse
import ast
import sys


def gen_docstring(source: str, funcname: str | None = None) -> str:
    tree = ast.parse(source)
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            if funcname and node.name != funcname:
                continue
            args = [a.arg for a in node.args.args]
            ret = ""
            if node.returns:
                ret = ast.unparse(node.returns)
            lines = [f'"""TODO: {node.name} 的一句话描述。', ""]
            lines.append("Args:")
            for a in args:
                if a == "self":
                    continue
                lines.append(f"    {a} (TODO): TODO")
            if ret:
                lines.append("")
                lines.append(f"Returns:\n    {ret}: TODO")
            lines.append('"""')
            return "\n".join(lines)
    return ""


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="函数 -> Google 风格 docstring")
    p.add_argument("--file", required=True)
    p.add_argument("--func", default=None)
    args = p.parse_args(argv)
    src = open(args.file, encoding="utf-8").read()
    print(gen_docstring(src, args.func))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
