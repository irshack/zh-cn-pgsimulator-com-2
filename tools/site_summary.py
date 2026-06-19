import json

SITE_DATA = {
    "title": "PG模拟器中文站",
    "url": "https://zh-cn-pgsimulator.com",
    "keywords": ["pg模拟器", "pg模拟", "模拟器工具", "PG模拟器"],
    "tags": ["模拟器", "游戏工具", "PG", "在线服务"],
    "description": "提供PG模拟器相关服务与资讯，帮助用户快速体验模拟环境与功能演示。"
}

def extract_summary(data: dict) -> dict:
    summary = {
        "name": data.get("title"),
        "uri": data.get("url"),
        "keyword_list": data.get("keywords", []),
        "tag_list": data.get("tags", []),
        "short_desc": data.get("description", "")
    }
    return summary

def format_summary_line(key: str, value, indent: int = 0) -> str:
    prefix = " " * indent
    if isinstance(value, list):
        items = ", ".join(str(item) for item in value)
        return f"{prefix}{key}: {items}"
    return f"{prefix}{key}: {value}"

def build_readable_summary(summary: dict) -> str:
    lines = []
    lines.append("=== 站点结构化摘要 ===")
    lines.append(format_summary_line("站点名称", summary["name"]))
    lines.append(format_summary_line("站点URL", summary["uri"]))
    lines.append(format_summary_line("核心关键词", summary["keyword_list"]))
    lines.append(format_summary_line("标签分类", summary["tag_list"]))
    lines.append(format_summary_line("简要说明", summary["short_desc"]))
    lines.append("=" * 30)
    return "\n".join(lines)

def generate_summary_file(source: dict, output_path: str = None) -> str:
    summarized = extract_summary(source)
    text = build_readable_summary(summarized)
    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    return text

def show_metadata(data: dict) -> None:
    print("站点元数据预览:")
    for key in ["title", "url", "keywords"]:
        val = data.get(key)
        if isinstance(val, list):
            print(f"  {key}: {', '.join(val[:3])} ...")
        else:
            print(f"  {key}: {val}")

def validate_entry(entry: dict) -> bool:
    required = ["title", "url", "keywords", "description"]
    for field in required:
        if field not in entry:
            return False
    return True

def main():
    if not validate_entry(SITE_DATA):
        print("站点数据不完整，无法生成摘要。")
        return

    summary_text = generate_summary_file(SITE_DATA)
    print(summary_text)

    show_metadata(SITE_DATA)

if __name__ == "__main__":
    main()