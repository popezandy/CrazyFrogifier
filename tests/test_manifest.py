from pathlib import Path
from frogifier.manifest import load_manifest


def test_manifest_valid():
    root = Path(__file__).resolve().parents[1]
    data = load_manifest(root / "dataset" / "manifest.json")
    assert len(data["pairs"]) >= 20
    assert all(p["status"] == "candidate" for p in data["pairs"])
