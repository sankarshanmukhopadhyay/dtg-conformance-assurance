"""Generate synthetic source records and assessor manifest; never real conformance evidence."""
import hashlib
import json
import sys
from pathlib import Path


def sha(data):
    return hashlib.sha256(data).hexdigest()


def write(path, value):
    raw = (json.dumps(value, indent=2, sort_keys=True) + "\n").encode()
    path.write_bytes(raw)
    return sha(raw)


def generate(directory):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    vector_hash = sha(b"synthetic fixture, not an upstream vector")
    vector_digest = "sha256:" + sha(f"{vector_hash}  fixture.json\n".encode())
    run = {"format": "tt-conformance-run/0.2", "today": "2026-11-24", "todaySource": "pinned",
        "suite": {"commit": "864687a5bc072b12c952e16539b42e738c4a7dd5", "dirty": False, "version": "0.1.0-draft"},
        "vectors": {"dir": "synthetic", "files": {"fixture.json": vector_hash}, "digest": vector_digest},
        "exceptions": None, "implementations": [{"spec": "synthetic", "capabilities": {"name": "fixture", "version": "1"}}],
        "node": "synthetic", "argv": []}
    results = [{"impl": "fixture", "tier": 1, "channels": ["registry"], "drift": [],
        "windowDifference": [], "essentialProbe": {"result": "not-probed"},
        "results": [{"id": "positive", "group": "fixture", "family": "fixture", "tier": 1, "status": "PASS", "anchor": True},
                    {"id": "negative", "group": "fixture", "family": "fixture", "tier": 1, "status": "PASS"}]}]
    manifest = {"format": "dcas-tt-assessor/0.1", "evaluation_id": "synthetic-only",
        "target": {"baseline": "synthetic", "version": "1", "profile": "fixture"},
        "assessor": "synthetic-assessor", "review_ref": "urn:synthetic:review",
        "observed_at": "2026-11-24T12:00:00Z", "valid_until": "2026-11-26T00:00:00Z",
        "evaluation_time": "2026-11-25T00:00:00Z",
        "source": {"run_sha256": write(directory / "run.json", run), "results_sha256": write(directory / "results.json", results),
            "vector_digest": vector_digest, "implementation": "fixture", "implementation_version": "1",
            "implementation_revision": "synthetic", "implementation_revision_ref": "urn:synthetic:checkout", "specification_revision": "synthetic", "tier": 1},
        "requirements": {"synthetic-R1": {"vectors": ["positive", "negative"], "positive_anchors": ["positive"]}}}
    write(directory / "manifest.json", manifest)
    return run, results, manifest


if __name__ == "__main__":
    generate(sys.argv[1])
