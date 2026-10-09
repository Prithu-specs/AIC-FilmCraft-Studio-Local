---
name: aic-filmcraft-studio-local
description: Produce real local 3D animated film shots without cloud video generators, using rigged characters, staged scenes, local rendering, and Filmcraft continuity review.
---

# AIC FilmCraft Studio Local

Use this skill for a film, short, trailer, or scene that the user wants produced locally as real 3D animation rather than cloud-generated video or an animated still.

## Outcome and boundary

Produce shots from editable local 3D scenes: meshes, rigs, materials, lights, cameras, animation curves, and a local renderer. Do not describe a pan over a still image as a final animated film shot. A 2D or 3D reference image is design evidence, not an animatable character.

This skill replaces the **production workflow** commonly performed in cloud video tools. It does not recreate proprietary video models. Do not use Google Flow or another cloud generator unless the user explicitly asks for it.

## Route before production

Choose one route and record it in the project ledger.

1. **True local 3D animation — preferred.** Requires Blender (or another local DCC), a mesh and rig for every visible character, a modeled environment, prop meshes, a local renderer, and an editable scene file. Use this route for final film shots.
2. **Verified local image-to-video.** Use only when the installed model demonstrably accepts the approved reference images and preserves them in a controlled five-second test. Treat it as a candidate route, never as a substitute for a rig.
3. **Previs / animatic.** Static boards with editorial camera moves are permitted only when labelled `PREVIS`, never `FINAL CLIP` or `ANIMATION`.

If neither Route 1 nor Route 2 is available, mark final animation as blocked. Continue with asset modeling, rigging, scene setup, shot planning, sound, and edit prep; do not generate text-only video of locked characters.

Read [local 3D production protocol](references/local-3d-production.md) for the required records, shot build order, and acceptance gate.

## Required asset states

Before final-shot animation, maintain a local asset registry for each visible item:

- Character: sculpt/model, UV/material, front/side/back reference, skeleton, tested controls, costume and facial controls.
- Location: modular geometry, scale map, entrances/exits, doors/windows, materials, lighting rig, and camera-safe areas.
- Prop: geometry, material, scale, resting state, ownership, grip/attachment point, and state-change rules.
- Audio: approved dialogue, ambience, Foley, music, and timing notes.

An image-only lock can guide modeling but cannot pass the final-animation readiness check.

## Filmcraft local dispatch gate

For every five-second or shorter unit, create this package before rendering:

```text
[project]/production/scene-[NN]-[slug]/unit-[NN]-[slug]-[duration]/
  01-authority/     scene beat, shot card, continuity in/out state
  02-assets/        registry links, mesh/rig/scene versions, source references
  03-animation/     blocking, camera, lighting, action timing, exclusions
  04-scene-file/    editable DCC scene and render settings
  05-renders/       preview, final candidate, review frames
  06-audio/         dialogue, ambience, Foley, music timing
  07-ledger/        render provenance, review result, next action
```

Never start a final render until the package establishes: scene beat, exact character count, required meshes/rigs, location version, prop ownership, start/end state, one primary action, camera direction, lighting state, audio state, and acceptance criteria.

## Animation rules

- Animate one causal action per short unit. Split entrances, prop transfers, and reactions into separate units when that preserves control.
- Block with simple poses and camera framing first. Review the silhouette, spacing, screen direction, and prop contact before spline animation or final lighting.
- Use rig constraints or attachment points for hands and props. Do not simulate a handoff without an explicit ownership transition.
- Keep doors, windows, and other fixed geography as rigged scene objects with named open/closed states.
- Render a low-cost viewport preview first; final render only after the preview passes continuity review.
- At 0%, 25%, 50%, 75%, and 100%, review identity, count, wardrobe, prop state, contact, mechanics, geography, lighting, and final state. Retire failed candidates; do not carry their state forward.

## Local-first tool discipline

- Prefer Blender with Eevee for previews and Cycles for final quality when hardware permits.
- Use FFmpeg only to encode, transcode, review, or assemble rendered frames; it does not create character animation.
- Do not install a model, plugin, extension, or repository merely because it claims video generation. Inspect origin, license, dependencies, active maintenance, hardware requirements, and security signals first. Obtain user authorization immediately before downloading or installing a new runtime.
- Never claim a reference image has become a mesh, a rig, or an animated clip until the corresponding local file exists and has been inspected.

## Delivery

A final local 3D shot must include the editable scene file, linked asset manifest, render settings, image sequence or lossless master, encoded review file, audio references, and a review decision. Archive these with the script and canon so the project is reproducible without Google Flow.
