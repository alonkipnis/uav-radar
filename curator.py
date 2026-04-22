#!/usr/bin/env python3
"""
UAV Radar Research Wiki Curator
Monitors papers/raw/ for new PDFs and links, summarizes them via Claude API,
and updates the wiki markdown files automatically.
"""

import os
import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
import anthropic
import fitz  # PyMuPDF

# ── Configuration ────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent
PAPERS_RAW = REPO_ROOT / "papers" / "raw"
PAPERS_DIR = REPO_ROOT / "papers"
WIKI_DIR = REPO_ROOT / "wiki"
STATE_FILE = REPO_ROOT / ".curator_state.json"

TOPICS = ["radar", "uav-detection", "tracking", "classification", "datasets", "other"]

CLIENT = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])
MODEL = "claude-sonnet-4-20250514"

# ── State management (track which files have been processed) ─────────────────

def load_state() -> dict:
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return {"processed": {}}

def save_state(state: dict):
    STATE_FILE.write_text(json.dumps(state, indent=2))

def file_hash(path: Path) -> str:
    return hashlib.md5(path.read_bytes()).hexdigest()

# ── PDF text extraction ───────────────────────────────────────────────────────

def extract_pdf_text(path: Path, max_chars: int = 12000) -> str:
    """Extract text from PDF, truncating to max_chars to stay within token limits."""
    try:
        doc = fitz.open(str(path))
        text = ""
        for page in doc:
            text += page.get_text()
            if len(text) >= max_chars:
                break
        doc.close()
        return text[:max_chars]
    except Exception as e:
        return f"[PDF extraction failed: {e}]"

# ── Claude API calls ──────────────────────────────────────────────────────────

def summarize_paper(filename: str, text: str) -> dict:
    """Ask Claude to extract metadata and summarize a research paper."""
    prompt = f"""You are a research assistant for a university lab working on UAV detection, identification, and tracking from radar data.

Analyze this research paper and return ONLY a JSON object with these fields:
- "title": full paper title (string)
- "authors": list of author last names (list of strings, max 4, use "et al." if more)
- "year": publication year as integer (or null if unknown)
- "venue": conference or journal name, abbreviated (string or null)
- "topics": list of relevant topic tags from this list ONLY: {TOPICS}
- "summary": 3-4 sentence summary focused on: what problem they solve, what method/approach, key results (string)
- "relevance": one sentence on why this is relevant to UAV radar research (string)
- "key_contribution": one crisp sentence, the single most important takeaway (string)

Filename: {filename}

Paper text (possibly truncated):
{text}

Return ONLY the JSON object, no markdown fences, no other text."""

    response = CLIENT.messages.create(
        model=MODEL,
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text.strip()
    # Strip markdown fences if present
    raw = re.sub(r"^```[a-z]*\n?", "", raw)
    raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)

def summarize_link(url: str, description: str) -> dict:
    """Ask Claude to categorize a link entry."""
    prompt = f"""You are a research assistant for a UAV radar detection lab.

Categorize this resource and return ONLY a JSON object:
- "title": descriptive title for this resource (string)
- "topics": relevant tags from: {TOPICS}
- "summary": 1-2 sentence description of what this resource contains (string)
- "type": one of: "paper", "dataset", "code", "tutorial", "tool", "survey", "other"

URL: {url}
Description provided: {description}

Return ONLY the JSON object, no markdown fences."""

    response = CLIENT.messages.create(
        model=MODEL,
        max_tokens=400,
        messages=[{"role": "user", "content": prompt}]
    )
    raw = response.content[0].text.strip()
    raw = re.sub(r"^```[a-z]*\n?", "", raw)
    raw = re.sub(r"\n?```$", "", raw)
    return json.loads(raw)

# ── Wiki update functions ─────────────────────────────────────────────────────

def load_papers_db() -> list:
    db_path = WIKI_DIR / "papers_db.json"
    if db_path.exists():
        return json.loads(db_path.read_text())
    return []

def save_papers_db(papers: list):
    db_path = WIKI_DIR / "papers_db.json"
    db_path.write_text(json.dumps(papers, indent=2))

def regenerate_wiki(papers: list):
    """Regenerate all wiki markdown files from the papers database."""
    WIKI_DIR.mkdir(exist_ok=True)
    _write_index(papers)
    _write_onboarding(papers)
    for topic in TOPICS:
        _write_topic_page(papers, topic)
    _write_all_papers(papers)
    print("  Wiki regenerated.")

def _write_index(papers: list):
    lines = [
        "# UAV Radar Research — Wiki Index",
        "",
        f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')} by curator bot*",
        "",
        f"**{len(papers)} papers and resources indexed.**",
        "",
        "## Topics",
        "",
    ]
    for topic in TOPICS:
        count = sum(1 for p in papers if topic in p.get("topics", []))
        if count > 0:
            lines.append(f"- [{topic.replace('-', ' ').title()}](topics/{topic}.md) — {count} entries")
    lines += [
        "",
        "## Quick Links",
        "",
        "- [All Papers](all_papers.md)",
        "- [Onboarding Guide](onboarding.md)",
        "- [Progress Log](progress/README.md)",
        "- [Meeting Notes](notes/meetings/README.md)",
        "",
        "## Recently Added",
        "",
    ]
    recent = sorted(papers, key=lambda p: p.get("added_date", ""), reverse=True)[:5]
    for p in recent:
        lines.append(f"- **{p['title']}** ({p.get('year', '?')}) — {p.get('key_contribution', '')}")
    (WIKI_DIR / "index.md").write_text("\n".join(lines))

def _write_onboarding(papers: list):
    """Generate onboarding guide — curated entry point for new students."""
    # Ask Claude to pick the best onboarding papers
    if not papers:
        return
    titles_and_summaries = "\n".join(
        f"- [{i}] {p['title']} ({p.get('year','?')}): {p.get('summary','')}"
        for i, p in enumerate(papers)
    )
    prompt = f"""You are writing an onboarding guide for a new PhD student joining a university research lab on UAV detection, identification, and tracking from radar data.

Here are the papers in our knowledge base:
{titles_and_summaries}

Write a structured onboarding guide in Markdown with these sections:
1. **Project Overview** — 2 paragraphs on what the lab works on
2. **Background Reading** — pick 3-6 foundational papers from the list above (by index number), explain reading order and why each matters
3. **Key Concepts to Understand** — bullet list of 6-8 technical concepts a new student must know
4. **Suggested First Steps** — practical advice for getting started in the lab

Use the paper titles from the list. Be specific and useful, not generic."""

    response = CLIENT.messages.create(
        model=MODEL,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}]
    )
    content = response.content[0].text
    header = (
        "# Onboarding Guide — UAV Radar Research Lab\n\n"
        f"*Auto-generated by curator bot on {datetime.now().strftime('%Y-%m-%d')}. "
        "Edit `papers/raw/` to improve this guide.*\n\n"
    )
    (WIKI_DIR / "onboarding.md").write_text(header + content)

def _write_topic_page(papers: list, topic: str):
    topic_papers = [p for p in papers if topic in p.get("topics", [])]
    if not topic_papers:
        return
    topic_dir = WIKI_DIR / "topics"
    topic_dir.mkdir(exist_ok=True)
    lines = [
        f"# {topic.replace('-', ' ').title()}",
        "",
        f"*{len(topic_papers)} entries — [← Back to Index](../index.md)*",
        "",
    ]
    for p in sorted(topic_papers, key=lambda x: x.get("year", 0), reverse=True):
        lines += [
            f"## {p['title']}",
            f"**{', '.join(p.get('authors', []))}** · {p.get('year', '?')} · {p.get('venue', '')}",
            "",
            p.get("summary", ""),
            "",
            f"**Key contribution:** {p.get('key_contribution', '')}",
            "",
            f"**Relevance:** {p.get('relevance', '')}",
            "",
            "---",
            "",
        ]
    (topic_dir / f"{topic}.md").write_text("\n".join(lines))

def _write_all_papers(papers: list):
    lines = [
        "# All Papers & Resources",
        "",
        f"*{len(papers)} total — sorted by year*",
        "",
        "| Title | Authors | Year | Topics | File |",
        "|-------|---------|------|--------|------|",
    ]
    for p in sorted(papers, key=lambda x: x.get("year", 0), reverse=True):
        topics_str = ", ".join(p.get("topics", []))
        file_str = f"[PDF]({p['file']})" if p.get("file") else p.get("url", "—")
        authors_str = ", ".join(p.get("authors", []))
        lines.append(f"| {p['title']} | {authors_str} | {p.get('year','?')} | {topics_str} | {file_str} |")
    (WIKI_DIR / "all_papers.md").write_text("\n".join(lines))

# ── Main processing loop ──────────────────────────────────────────────────────

def process_new_pdfs(state: dict, papers: list) -> bool:
    """Scan papers/raw/ for new PDFs. Returns True if anything was processed."""
    PAPERS_RAW.mkdir(parents=True, exist_ok=True)
    changed = False
    for pdf_path in sorted(PAPERS_RAW.glob("*.pdf")):
        h = file_hash(pdf_path)
        if state["processed"].get(str(pdf_path)) == h:
            continue
        print(f"  Processing PDF: {pdf_path.name}")
        text = extract_pdf_text(pdf_path)
        try:
            meta = summarize_paper(pdf_path.name, text)
            meta["file"] = f"../papers/raw/{pdf_path.name}"
            meta["added_date"] = datetime.now().strftime("%Y-%m-%d")
            meta["source"] = "pdf"
            papers.append(meta)
            state["processed"][str(pdf_path)] = h
            changed = True
            print(f"    ✓ {meta.get('title', pdf_path.name)}")
        except Exception as e:
            print(f"    ✗ Failed to process {pdf_path.name}: {e}")
    return changed

def process_links_file(state: dict, papers: list) -> bool:
    """Process links.md in notes/ for new URL entries."""
    links_file = REPO_ROOT / "notes" / "links.md"
    if not links_file.exists():
        return False
    h = file_hash(links_file)
    if state["processed"].get(str(links_file)) == h:
        return False
    print("  Processing links.md...")
    changed = False
    for line in links_file.read_text().splitlines():
        line = line.strip()
        # Expect format: - URL | optional description
        if not line.startswith("-"):
            continue
        line = line.lstrip("- ").strip()
        parts = line.split("|", 1)
        url = parts[0].strip()
        description = parts[1].strip() if len(parts) > 1 else ""
        if not url.startswith("http"):
            continue
        if any(p.get("url") == url for p in papers):
            continue
        try:
            meta = summarize_link(url, description)
            meta["url"] = url
            meta["added_date"] = datetime.now().strftime("%Y-%m-%d")
            meta["source"] = "link"
            papers.append(meta)
            changed = True
            print(f"    ✓ {meta.get('title', url)}")
        except Exception as e:
            print(f"    ✗ Failed to process {url}: {e}")
    state["processed"][str(links_file)] = h
    return changed

def main():
    print(f"\n{'='*60}")
    print(f"UAV Radar Wiki Curator — {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'='*60}\n")

    state = load_state()
    papers = load_papers_db()

    changed = False
    changed |= process_new_pdfs(state, papers)
    changed |= process_links_file(state, papers)

    if changed:
        print("\nUpdating wiki...")
        save_papers_db(papers)
        regenerate_wiki(papers)
        save_state(state)
        print("\nDone. Wiki updated.")
    else:
        print("No new material found. Wiki is up to date.")

if __name__ == "__main__":
    main()
