# CLAUDE HANDOFF — CRAZY FROGIFIER

You are lead engineer for **Crazy Frogifier**, a local Windows application that transforms a user-supplied song into a 2005-era Crazy Frog-like cover. Build actual, testable music-to-music processing; don't substitute a prompt-only demo, fabricated benchmarks, or a fake audio output. This is a personal comedic experiment.

## Product requirements
- Inputs: local MP3/WAV/FLAC; outputs: stereo WAV, optional MP3 and stems. Keep logs, seed and reproducibility metadata.
- Four modes: Classic Frog; Extra Frog; **100% Frog A Cappella** (melody, bass, beat, harmony and effects all rendered as frog-like vocal sounds); Frog Karaoke (new character vocals over backing).
- Controls: frog intensity, melody preservation, vocal insanity, tempo/style era, output stems, random seed.
- Visual UI: aggressively terrible Jamster-era ringtone subscription website: Comic Sans, neon clashing colors, tiled frog art, animated GIFs, flashing buttons, fake SMS pricing prominently marked fake, faux visitor counter. Functional input/job controls, errors and accessibility underneath.
- User hardware: Windows 11, Ryzen 7800X3D, RTX 3080 + RTX 4060, 32GB RAM. Check installed CUDA, GPU VRAM and model requirements; don't assume VRAM can be pooled.

## Separate the three learning problems
1. **Style adaptation** learns synth patches, dance drum production, vocal tone, mixing and typical arrangement from distinctive completed recordings. Reference-conditioned covers and LoRA fine-tuning may help.
2. **Original→frog arrangement transformations** learn section, melody, harmony, instrument assignment, tempo and vocal substitutions from carefully aligned *pairs*. LoRA on frog tracks alone does not learn this mapping.
3. **Vocal instrument** builds a classified/parameterized Frog Vocal Atlas to render pitched, timed, expressive parts. Acapella mode MUST resynthesize the music, not just strip instruments or isolate existing vocals.

## Proposed system
- Python 3.11, PyTorch, ffmpeg, local FastAPI service + async job worker; a model adapter interface so generation backends are replaceable.
- Benchmark ACE-Step 1.5 current cover/audio-to-audio capabilities against an alternative such as YuE, verifying actual APIs, dependencies, memory and performance from current official source.
- Separate source via Demucs/BS-RoFormer; analyze BPM/onsets/chroma/structure with librosa/Essentia and optional melody transcription; maintain confidence scores.
- Align original/cover at bars and musical sections, using chroma and dynamic time warping plus manual overrides. Avoid naive 1-to-1 timestamp alignment.
- Start with structured arrangement-change descriptors and human review. Train an arrangement policy only once enough validated pairs exist; hold out whole compositions across all editions.
- Build the Frog Vocal Atlas from isolated/acapella candidate tracks and extracted stems, tagged by note/syllable/transient/articulation; implement a short melody+bass+drum vocal synthesizer proof of concept before asserting full-song capability.

## Dataset
- `dataset/manifest.json` is a *candidate list*, NOT downloaded audio or fully verified pairs. Verify title, particular recording, album version and original artist against reliable catalogs. Different original versions may matter.
- Separate works/compositions, original/master recordings and release appearances. Deduplicate masters with fingerprints, not track names.
- Keep official_style, paired_cover, fan_candidate, fan_approved and vocal_atlas tiers. Never invent fan cover links; manually listen and QA them.
- Record stable IDs, title, release, artist, variant, source/provenance URL, confidence, acquisition state, QA notes, duration/sample rate/fingerprint, alignment and stems.
- Raw audio stays local in gitignored `data/`; no copyrighted masters or credentials in the repo. Personal use is not a substitute for provenance tracking.

## Ordered execution plan
1. Inspect scaffold; run manifest validator/tests. Improve schema and add export/import CLI.
2. Research official discography and release variants; distinguish confirmed vs proposed cover pairings, dedupe repeated album releases; validate fan audio rather than video memes.
3. Implement media intake and normalization with deterministic file hashes and failure tests.
4. Build pluggable audio generator and runnable local ACE-Step baseline; test on user-supplied audio and report actual GPU memory and latency.
5. Add stem extraction, beat/section analysis, paired alignment, QA visualization and machine-readable transformation descriptors.
6. Experiment with style LoRA and compare against a zero-shot baseline on unseen compositions. Never claim success without evaluated audio.
7. Prototype the vocal atlas plus fully frog-voiced 8-bar arrangement, then expand to full acapella and karaoke.
8. Implement FastAPI job queue/cancellation/progress and connect the hideous web frontend for upload, progress, playback, export.
9. Establish evaluation: recognizability, melody similarity, arrangement resemblance, distinctive vocal placement, artifact rate and user listening scores.
10. Package reproducibly for Windows; document CUDA setup, VRAM budget, weights acquisition and failure modes.

## MVP acceptance
- A real song enters, a real transformed audio file exits (no placeholder sound).
- Transparent setup/model availability, logs and error paths.
- Dataset candidate statuses honest and validator/tests passing.
- Experimental acapella is labeled unavailable until it genuinely works.
- The 2005 UI is extremely ugly but functionally reliable.

## Engineering discipline
Make changes in focused commits; update README with truth about capabilities. Use typed schemas, tests and immutable raw data. Do not silently download huge models. Confirm current upstream model interfaces instead of guessing. Do not confuse the static prototype page with a working backend.
