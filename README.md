# Aid Architecture, Local Economic Participation, and Capacity Formation

Reproducible research pipeline for the manuscript "Beyond Aid Volume: Aid
Architecture, Local Economic Participation, Capacity Formation, and Persistent
Development Outcomes".

## Layout

- `config/` — project config, variable ontology, source registry
- `data/` — raw / external / interim / processed / metadata (raw is never edited)
- `scripts/` — numbered pipeline steps (00_setup → 18_reproducibility_audit)
- `results/` — tables, figures, model objects, dashboard exports, audit logs
- `manuscript/` — docx deliverables
- `dashboard/` — prototype and schema for the interactive supplement
- `reproducibility/`, `submission/`

## Reproduce

```bash
pip install -r environment/requirements.txt
# then run scripts in numeric order; see FINAL_HANDOFF.md for the canonical command list
```

## Data provenance

Every raw dataset is stored under `data/raw/<source>/` with a manifest in
`data/metadata/` recording URL, retrieval time (UTC), license, and SHA-256.
Raw files are never modified or overwritten.
