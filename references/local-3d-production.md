# Local 3D Production Protocol

## Readiness audit

Run this audit before committing to a local final-animation route.

| Requirement | Evidence needed | If absent |
|---|---|---|
| DCC renderer | local executable and a saved test scene | install only with user authorization |
| Character animation | mesh, armature, controls, pose test | model/rig; do not render a character shot |
| Environment | editable geometry, scale, collision/geography | build or acquire licensed geometry |
| Props | editable mesh and attachment point | model or acquire licensed asset |
| Materials/lights | reusable material and light setup | build the scene look before animation |
| Audio | timing track and rights record | prepare temp track; do not final-mix |
| Render test | short local preview renders and decodes | diagnose before allocating batch renders |

## Unit production order

1. Read the approved screenplay beat and scene packet.
2. Copy only required asset versions into the unit registry.
3. Build or open the scene file; verify character count and fixed geography.
4. Block the action at start, midpoint, and end frame.
5. Make a low-cost preview. Check screen direction, prop contact, character count, entrance/exit, and door/window state.
6. Correct the source scene, not the rendered video.
7. Add camera, lighting, facial/body refinement, sound timing, and final render settings.
8. Render one candidate. Decode it and extract review frames at 0/25/50/75/100.
9. Record approved, repair, or retired with the observable reason.

## The Offer starter requirements

For this project, the active references define the desired 3D look. They do **not** replace the following production assets:

- Alex, Evelyn, and Marcus need separately editable rigged 3D character models.
- The repair shop needs an editable environment with a blue double glass-pane entrance, brass pulls, warm practical lights, counter, bench, and camera-safe geography.
- The silver-and-charcoal rangefinder, brown leather case, cream archival box, and Marcus's parts case need editable prop meshes and named attachment/rest states.
- The relevant screenplay scene must specify who is visible, action, object ownership, and start/end door state.

Until those are present, produce only labelled 3D previs and asset-development material. Do not call it final animation.
