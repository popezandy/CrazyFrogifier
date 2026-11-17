# Dataset construction

Three separate groups: (A) official Frog style tracks, deduplicated by exact master fingerprint; (B) paired original recording ↔ Frog cover with source/version/structural alignment; (C) manually reviewed fan reinterpretations. Add a Frog Vocal Atlas of isolated voice material.

**Current manifest is only an inventory of candidates. No audio is provided or verified.**

For each candidate collect canonical work ID, exact master, recording date/edition, provenance URL, status, original artist and version, confidence, review notes, SHA256/fingerprint, BPM/key, separated stems and section alignment.

Important: Axel F, Popcorn, Cotton Eye Joe, Everytime We Touch and other songs have multiple musically relevant prior recordings; distinguish composition from specific master. A title match is not a verified cover pair.

Fan covers: reject visual-only memes, straight mashups, low-quality pitch changes and reused masters. Rate melody fidelity, recreation quality, Frog-like vocals, production resemblance and clean audio; mark unreviewed as candidates.

For all pairs: normalize and extract stems, estimate beats/chroma, align by bars and sections (not raw timestamps), annotate substituted leads/bass/drums/vocals and structure changes, assign confidence, and hold out *compositions* in evaluation to avoid duplicate leakage.

Store untracked recordings in local `data/`, not Git. Record provenance and separate permissions metadata if future distribution is considered.
