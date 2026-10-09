#!/usr/bin/env python3
"""Fail closed when a locked film unit lacks approved visual authority."""
import json
import sys
from pathlib import Path

if len(sys.argv) != 2:
    raise SystemExit('usage: validate_asset_gate.py /absolute/path/to/unit')
unit = Path(sys.argv[1]).resolve()
lock_path = unit / '01-authority' / 'asset-lock.json'
errors = []
if not lock_path.is_file():
    errors.append('missing 01-authority/asset-lock.json')
    lock = {}
else:
    try:
        lock = json.loads(lock_path.read_text())
    except json.JSONDecodeError as exc:
        errors.append(f'invalid asset-lock.json: {exc}')
        lock = {}
route = lock.get('route')
if route not in {'blender', 'image-to-video'}:
    errors.append('route must be blender or image-to-video; text-only generation is prohibited')
assets = lock.get('assets')
if not isinstance(assets, list) or not assets:
    errors.append('assets must be a non-empty list')
for i, asset in enumerate(assets if isinstance(assets, list) else []):
    if not asset.get('visible'):
        continue
    for field in ('id', 'kind', 'reference', 'allowed_state'):
        if not asset.get(field):
            errors.append(f'assets[{i}] missing {field}')
    ref = asset.get('reference')
    if ref and not (unit / ref).resolve().is_file():
        errors.append(f'assets[{i}] reference does not exist: {ref}')
    if route == 'blender':
        editable = asset.get('editable_asset')
        if not editable:
            errors.append(f'assets[{i}] needs editable_asset for Blender')
        elif not (unit / editable).resolve().is_file():
            errors.append(f'assets[{i}] editable asset does not exist: {editable}')
if not lock.get('exclusions'):
    errors.append('exclusions must specify disallowed people, props, text, or interactions')
review = lock.get('preview_review', {})
if review.get('status') != 'approved':
    errors.append('camera-match preview has not been approved')
if errors:
    print('ASSET GATE: BLOCKED')
    print('\n'.join(f'- {e}' for e in errors))
    raise SystemExit(2)
print('ASSET GATE: PASS')
