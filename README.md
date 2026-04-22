# UAV Radar Research — Lab Knowledge Base

This repository is the living knowledge base for our research group on **UAV detection, identification, and tracking from radar data**.

The wiki is maintained automatically by an AI curator bot. Students contribute raw material; the bot handles organization.

---

## How to contribute

### Adding a paper (PDF)
1. Go to `papers/raw/` in the GitHub web UI
2. Click **Add file → Upload files**
3. Drop your PDF and commit — done

The bot will automatically summarize it and add it to the wiki within minutes.

### Adding a link or resource
1. Open `notes/links.md`
2. Add a line in this format:
   ```
   - https://arxiv.org/abs/xxxx.xxxxx | Brief description of what this is
   ```
3. Commit — the bot handles the rest

### Adding meeting notes or weekly updates
Drop `.md` files into:
- `notes/meetings/YYYY-MM-DD.md`
- `notes/weekly-updates/YYYY-WXX-yourname.md`

These are not auto-processed but are available for manual AI queries.

---

## Wiki

The wiki lives in `wiki/` and is fully auto-generated:

| File | Contents |
|------|----------|
| `wiki/index.md` | Master index, topic list, recently added |
| `wiki/onboarding.md` | Auto-generated onboarding guide for new students |
| `wiki/all_papers.md` | Full table of all indexed papers |
| `wiki/topics/radar.md` | Papers tagged with *radar* |
| `wiki/topics/uav-detection.md` | Papers tagged with *uav-detection* |
| `wiki/topics/tracking.md` | Papers tagged with *tracking* |
| `wiki/topics/classification.md` | Papers tagged with *classification* |
| `wiki/topics/datasets.md` | Papers tagged with *datasets* |

---

## Repo structure

```
├── papers/
│   └── raw/              ← DROP PDFS HERE
├── notes/
│   ├── links.md          ← ADD LINKS HERE
│   ├── meetings/
│   └── weekly-updates/
├── wiki/                 ← AUTO-GENERATED, do not edit manually
├── .github/
│   └── workflows/
│       └── curator.yml   ← GitHub Actions pipeline
├── curator.py            ← AI curator script
└── requirements.txt
```

---

## Setup (one-time, for PI or lab manager)

1. **Fork or create** this repo on GitHub
2. Go to **Settings → Secrets → Actions**
3. Add a secret named `ANTHROPIC_API_KEY` with your Anthropic API key
4. Push any PDF to `papers/raw/` to trigger the first run

That's it. The bot runs automatically on every push that adds papers or links.

### Manual trigger
Go to **Actions → Wiki Curator → Run workflow** to trigger a run manually at any time.

---

## Querying the wiki with AI

Once the wiki is populated, you can use it with any LLM:

**Example prompts:**
- *"Here is our lab wiki [paste wiki/index.md + relevant topic pages]. Generate a 10-slide onboarding presentation for a new PhD student."*
- *"Summarize the state of the art in radar-based UAV detection based on these papers [paste wiki/topics/radar.md]."*
- *"What are the open problems in our research area based on the papers we've read?"*

---

*Wiki is auto-maintained by curator bot using Claude API.*
