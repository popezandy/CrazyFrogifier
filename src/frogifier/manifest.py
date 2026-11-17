"""Conservative validation of candidate track-pair manifest."""
import json
from pathlib import Path


def load_manifest(path: str | Path) -> dict:
    payload = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(payload.get("pairs"), list):
        raise ValueError("Expected top-level pairs list")
    seen = set()
    for item in payload["pairs"]:
        for key in ("id", "frog_title", "original_artist", "original_title", "status"):
            if not isinstance(item.get(key), str) or not item[key].strip():
                raise ValueError(f"Invalid {key}: {item!r}")
        if item["id"] in seen:
            raise ValueError(f"Duplicate pair ID: {item['id']}")
        seen.add(item["id"])
        if item["status"] not in ("candidate", "reviewed", "verified"):
            raise ValueError(f"Invalid status: {item['status']}")
    return payload
