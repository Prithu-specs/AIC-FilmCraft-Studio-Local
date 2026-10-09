# Asset grounding protocol

## Purpose

Every final clip must reproduce its approved visual locks. The renderer or model may not fill gaps with a new interpretation.

## Required `asset-lock.json`

Save this file in `[unit]/01-authority/asset-lock.json` before rendering.

```json
{
  "unit_id": "scene-01-unit-01",
  "route": "blender",
  "approved": false,
  "assets": [
    {
      "id": "hero-camera-v1",
      "kind": "prop",
      "reference": "../02-assets/HERO-CAMERA-3D-PROP-LOCK-v1.png",
      "editable_asset": "../04-scene-file/hero-camera-v1.blend",
      "visible": true,
      "allowed_state": "rests on counter; one camera only"
    }
  ],
  "exclusions": ["people", "hands", "text", "logos", "duplicate props"],
  "preview_review": {
    "reference_comparison": "../05-renders/camera-match-preview.png",
    "status": "pending"
  }
}
```

Use `route: "blender"` only when every visible asset has an editable mesh, rig, or scene representation. Use `route: "image-to-video"` only when the engine has a documented, tested reference-image input and all input reference paths exist. `text-to-video` is prohibited for locked shots.

## Blender camera-match review

Render the actual shot camera at frame 1. Place the approved image and the candidate preview next to each other. Mark every feature `match`, `mismatch`, or `not visible`:

- Character: identity, hair, face, age, costume, body proportions, count.
- Location: door/window placement, walls, furniture, lighting, entrances and exits.
- Props: silhouette, material, color, straps, dials, wear, scale, count and state.
- Composition: camera height, lens, screen direction and blocking.

Any `mismatch` prevents animation. Repair the editable asset and rerun this comparison. The user’s approval is the only way to accept a deliberate visual change.

## Final review

Decode 0%, 25%, 50%, 75% and 100% frames. Verify all locks against the same checklist. Retire the output on one mismatch; do not edit the next unit from it.
