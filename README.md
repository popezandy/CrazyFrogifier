# Crazy Frogifier 🐸

A local-first, deliberately ridiculous **music-to-music transformation** research project: upload a song and turn it into a 2005-era hyperactive ringtone dance cover. The application should look like a cursed Jamster-era website while treating the audio engineering seriously.

## Project status

**Scaffold / research prototype.** No trained model, working audio generation, or verified audio dataset is included yet. The initial dataset is a *candidate list*, not a claim that audio files have been downloaded or paired.

## Core features
- Song upload and local project management
- Reference-conditioned music-to-music cover generation (ACE-Step 1.5 is a candidate to benchmark)
- Paired original-song ↔ Crazy Frog-cover arrangement learning
- Frog Vocal Atlas: isolated phrases, syllables, pitch and rhythmic annotations
- **100% Frog A Cappella:** resynthesize instrumental and vocal parts using character-like vocalizations
- Frog intensity, melody-preservation and vocal-insanity controls
- Optional stem export
- Aggressively hideous 2000s ringtone-ad UI

## Getting started

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
python scripts/validate_manifest.py
pytest -q
```

Open `web/index.html` to inspect the static visual concept. It is **not** connected to a backend.

## Navigation

- [CLAUDE.md](CLAUDE.md) — autonomous-agent engineering handoff
- [docs/DATASET_PLAN.md](docs/DATASET_PLAN.md) — dataset curation and pairing
- [docs/ROADMAP.md](docs/ROADMAP.md) — phased work
- [dataset/manifest.json](dataset/manifest.json) — seed catalog; candidates pending verification

Do not commit copyrighted recordings, model weights, credentials, or generated audio. Keep raw datasets and cached model files local.
