#!/usr/bin/env python3
"""
AI Model Comparison Tool
Usage: python compare.py --models "GPT-4o,Claude 3.5 Sonnet,Gemini 1.5 Pro"
"""

import argparse
import json
import sys

# 简化的模型数据
MODELS = {
    "GPT-4o": {
        "provider": "OpenAI",
        "context": 128000,
        "multimodal": ["text", "image", "audio", "video"],
        "mmlu": 88,
        "humaneval": 90,
        "math": 76,
        "input_cost": 5.00,
        "output_cost": 15.00,
        "speed": "medium",
        "chinese": 4,
        "code": 5,
    },
    "Claude 3.5 Sonnet": {
        "provider": "Anthropic",
        "context": 200000,
        "multimodal": ["text", "image"],
        "mmlu": 89,
        "humaneval": 92,
        "math": 73,
        "input_cost": 3.00,
        "output_cost": 15.00,
        "speed": "medium",
        "chinese": 4,
        "code": 5,
    },
    "Gemini 1.5 Pro": {
        "provider": "Google",
        "context": 2000000,
        "multimodal": ["text", "image", "audio", "video"],
        "mmlu": 85,
        "humaneval": 84,
        "math": 67,
        "input_cost": 1.25,
        "output_cost": 5.00,
        "speed": "slow",
        "chinese": 4,
        "code": 4,
    },
    "Qwen2.5 72B": {
        "provider": "Alibaba",
        "context": 128000,
        "multimodal": ["text", "image"],
        "mmlu": 86,
        "humaneval": 89,
        "math": 57,
        "input_cost": 0.20,
        "output_cost": 0.60,
        "speed": "medium",
        "chinese": 5,
        "code": 5,
    },
    "DeepSeek V2": {
        "provider": "DeepSeek",
        "context": 128000,
        "multimodal": ["text", "image"],
        "mmlu": 82,
        "humaneval": 90,
        "math": 58,
        "input_cost": 0.14,
        "output_cost": 0.28,
        "speed": "fast",
        "chinese": 4,
        "code": 5,
    },
    "LLaMA 3.1 405B": {
        "provider": "Meta",
        "context": 128000,
        "multimodal": ["text"],
        "mmlu": 87,
        "humaneval": 88,
        "math": 58,
        "input_cost": None,  # 需要本地部署
        "output_cost": None,
        "speed": "slow",
        "chinese": 3,
        "code": 5,
    },
}


def print_stars(n):
    return "⭐" * n


def compare_models(model_names):
    print("\n" + "=" * 80)
    print("🤖 AI Model Comparison Report")
    print("=" * 80)

    for name in model_names:
        if name not in MODELS:
            print(f"\n⚠️ Model '{name}' not found in database")
            continue

        m = MODELS[name]
        print(f"\n## {name}")
        print("-" * 40)
        print(f"📦 Provider: {m['provider']}")
        print(f"📏 Context: {m['context']:,} tokens")
        print(f"🖼️ Multimodal: {', '.join(m['multimodal'])}")
        print(f"📊 MMLU: {m['mmlu']}%")
        print(f"💻 HumanEval: {m['humaneval']}%")
        print(f"🔢 MATH: {m['math']}%")
        print(f"🇨🇳 Chinese: {print_stars(m['chinese'])}")
        print(f"⌨️ Code: {print_stars(m['code'])}")

        if m['input_cost']:
            print(f"💰 Input: ${m['input_cost']}/1M tokens")
            print(f"💰 Output: ${m['output_cost']}/1M tokens")
        else:
            print("💰 Cost: Local deployment required")

    print("\n" + "=" * 80)


def main():
    parser = argparse.ArgumentParser(description="Compare AI Models")
    parser.add_argument("--models", type=str, help="Comma-separated model names")
    parser.add_argument("--list", action="store_true", help="List all available models")
    parser.add_argument("--export", type=str, help="Export to JSON file")

    args = parser.parse_args()

    if args.list:
        print("\n📋 Available Models:")
        for name in MODELS.keys():
            print(f"  - {name}")
        return

    if args.export:
        with open(args.export, "w") as f:
            json.dump(MODELS, f, indent=2)
        print(f"✅ Exported to {args.export}")
        return

    if args.models:
        model_list = [m.strip() for m in args.models.split(",")]
        compare_models(model_list)
    else:
        compare_models(list(MODELS.keys()))


if __name__ == "__main__":
    main()
