import json

def load_projects(json_path="input.json"):
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_markdown(projects):
    lines = ["# 📌 My Projects", ""]
    for p in projects:
        lines.append(f"### 🧩 {p['title']}")
        lines.append(p["desc"])
        lines.append("")

        if "badge" in p:
            lines.append(f"![Badge]({p['badge']})")
            lines.append("")

        if "type" in p:
            lines.append(f"> 🧪 {p['type']}")
        
        if "date" in p:
            lines.append(f"🗓️ Last updated: {p['date']}")
        
        if "tags" in p:
            tags = " · ".join(f"`{tag}`" for tag in p["tags"])
            lines.append(f"**Tech Stack:** {tags}")

        if "demo" in p:
            lines.append(f"[🚀 Live Demo]({p['demo']})")

        lines.append(f"[🔗 View Project]({p['link']})")

        if "image" in p:
            lines.append(f"![Project Preview]({p['image']})")

        lines.append("---")
    return "\n".join(lines)

def save_readme(markdown, path="outputREADME.md"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(markdown)
    print(f"✅ README.md generated with {len(markdown.splitlines())} lines.")

if __name__ == "__main__":
    projects = load_projects()
    md = generate_markdown(projects)
    save_readme(md)