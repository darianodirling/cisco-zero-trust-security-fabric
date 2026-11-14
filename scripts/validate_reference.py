#!/usr/bin/env python3
"""Offline structural checks; no network access or device configuration."""
from pathlib import Path
root = Path(__file__).resolve().parents[1]
required = [
 "README.md", "docs/architecture-decisions.md", "docs/segmentation-matrix.md",
 "docs/ise-policy-flow.md", "docs/threat-model.md", "docs/implementation-runbook.md",
 "configs/ios/aaa-radius-8021x.example.cfg", "configs/ios/ospf-bgp.example.cfg",
 "configs/ios/trustsec.example.cfg", "configs/asa/vpn-landing-zone.example.cfg",
 "configs/ise/authorization-policy.yaml", "configs/secure-access/policy-intent.yaml",
 "configs/fmc/access-control-intent.yaml",
]
missing = [x for x in required if not (root / x).is_file()]
if missing:
    raise SystemExit("Missing files: " + ", ".join(missing))
assert "mermaid" in (root / "README.md").read_text()
print("PASS: reference files and architecture diagram found.")
print("NOTE: no Cisco syntax, API or live deployment validation performed.")
