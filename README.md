# docstring-gen-lite

解析函数签名，生成 **Google 风格 docstring** 占位。用标准库 `ast`，零依赖。

## 功能简介

- 提取函数名、参数、返回注解；
- 生成含 `Args:` / `Returns:` 的 docstring 模板；
- 自动跳过 `self`。

## 快速开始

```bash
python3 docstring_gen.py --file your_module.py --func add
```

## 无 API key 如何运行

纯 ast 解析，**不需要任何 API key**。

## 目录结构

```
docstring-gen-lite/
├── docstring_gen.py
├── tests/test_docstring_gen.py
├── README.md / LICENSE / .gitignore
```

## 运行测试

```bash
python3 -m unittest discover -s tests -v
```

## 许可证

[MIT](./LICENSE) © 2026 ljiang9
