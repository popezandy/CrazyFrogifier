from pathlib import Path
from frogifier.manifest import load_manifest

path = Path(__file__).resolve().parents[1] / "dataset" / "manifest.json"
payload = load_manifest(path)
print(f"OK: {len(payload['pairs'])} candidate pair records")
