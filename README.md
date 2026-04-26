# 🤖 AI Model Comparison - AI 模型能力对比表

> 主流 AI 模型全面对比：Benchmark 数据、成本、速度、上下文长度，支持搜索和筛选

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/lanxinAIhub/ai-model-comparison)](https://github.com/lanxinAIhub/ai-model-comparison/stargazers)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

## 🎯 功能特性

- 📊 **模型对比表** - 多维度横向对比主流模型
- 🔍 **快速搜索** - 按名称、能力、厂商筛选
- 💰 **成本分析** - Input/Output 价格一览
- ⚡ **性能基准** - 主流 Benchmark 数据
- 📈 **上下文长度** - 各模型支持的最大上下文
- 🗣️ **多模态支持** - 图像/音频/视频能力对比

## 📋 模型分类

| 分类 | 代表模型 | 说明 |
|------|----------|------|
| [🌐 GPT 系列](data/models-gpt.md) | GPT-4o, GPT-4 Turbo, GPT-3.5 | OpenAI 模型 |
| [🤖 Claude 系列](data/models-claude.md) | Claude 3.5 Sonnet, Claude 3 Opus | Anthropic 模型 |
| [💎 Gemini 系列](data/models-gemini.md) | Gemini 1.5 Pro, Gemini 1.5 Flash | Google 模型 |
| [🦙 LLaMA 系列](data/models-llama.md) | LLaMA 3.1, LLaMA 3 | Meta 开源模型 |
| [🇨🇳 国产模型](data/models-china.md) | 通义千问, 文心一言, Kimi, DeepSeek | 国内主流模型 |
| [🔮 开源其他](data/models-open-source.md) | Mistral, Qwen, Yi, Command | 其他开源模型 |

## 🔍 快速搜索

在 [data/](data/) 目录查看各模型详细数据，或使用在线对比工具。

## 📊 核心对比维度

| 维度 | 说明 |
|------|------|
| **Benchmarks** | MMLU, HumanEval, MATH, GPQA 等 |
| **上下文长度** | 最大支持 token 数 |
| **多模态** | 图像/音频/视频输入支持 |
| **成本** | $/1M Input / Output Tokens |
| **速度** | 首次响应时间 |
| **API 可用性** | 官方 API / 第三方 / 本地部署 |

## 🚀 使用方式

### 1. 查看对比表
直接在 [data/](data/) 目录浏览各模型详细数据。

### 2. 搜索特定模型
```bash
# 搜索包含 "GPT" 的模型
grep -r "GPT" data/

# 搜索支持多模态的模型
grep -r "Image" data/
```

### 3. 生成对比报告
```bash
python3 scripts/compare.py --models "GPT-4o,Claude 3.5 Sonnet,Gemini 1.5 Pro"
```

## 📁 项目结构

```
ai-model-comparison/
├── README.md              # 项目说明
├── data/                  # 模型数据
│   ├── models-gpt.md
│   ├── models-claude.md
│   ├── models-gemini.md
│   ├── models-llama.md
│   ├── models-china.md
│   ├── models-open-source.md
│   └── benchmarks.md      # Benchmark 数据汇总
├── scripts/              # 工具脚本
│   └── compare.py         # 对比生成脚本
└── assets/               # 静态资源
```

## 🤝 贡献指南

欢迎提交 PR 补充新模型数据或修正错误！

请查看 [CONTRIBUTING.md](CONTRIBUTING.md) 了解提交格式。

## 📅 更新日志

- **2026-04-26** 初始化版本，收录 20+ 主流模型
- 持续更新最新模型数据

## 📄 License

MIT License - 自由使用，注明来源
