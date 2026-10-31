# Complaint Product Classification

[![Validation](https://github.com/Ashik-Mohammed-S/Automatic_Ticket_Classifier/actions/workflows/validate.yml/badge.svg)](https://github.com/Ashik-Mohammed-S/Automatic_Ticket_Classifier/actions/workflows/validate.yml)

Route consumer complaint narratives to their recorded product/service category.

Independent public portfolio work; historical educational notebooks remain under `historical/`. The current implementation and results described here take precedence over historical in-sample numbers.

## Data and approach

78,313 source records; 20,930 deduplicated nonempty narratives enter the current full evaluation.

Remove duplicate narratives before a stratified holdout; fit TF-IDF only on training text and use class-balanced logistic regression. Group source products with fewer than ten examples explicitly rather than assigning topic IDs as labels.

## Current full-data result

| Measure | Current analysis | Baseline where applicable |
| --- | --- | --- |
| Accuracy | 0.655 | 0.240 |
| Balanced accuracy | 0.482 | 0.067 |
| Macro-F1 | 0.464 | 0.026 |

Results are specific to the documented dataset and split. See generated `results/analysis.json` after execution for full metrics and assumptions.

## Run locally

Use the Python version in `.python-version`, then:

```sh
python -m pip install -r requirements.txt
python scripts/fetch_data.py
python scripts/run_notebook.py --mode full
```

Reference data is committed under `dataset/`, directly or as reconstructable compressed parts. The downloader verifies checksums and restores stored data offline. See [DATA.md](DATA.md) and [dataset-sources.json](dataset-sources.json) for provenance and upstream terms. Package installation and the spaCy model, where needed, require network access on a fresh machine.

## Review the implementation

Inspect rare-class results, deduplication, label definitions and vocabulary fitting in scripts/analysis.py. Start with [scripts/analysis.py](scripts/analysis.py), then the root notebook. The workflow validates dependencies, smoke checks and full-data notebook execution with dataset downloads disabled.

## Limitations

Rare categories remain difficult and some have zero test recall. Product labels reflect the source taxonomy, not inferred NMF topic names. This is a historical offline routing experiment; no deployed ticketing integration or LLM is claimed.

[Method notes](ANALYSIS.md) · [All portfolio projects](https://github.com/Ashik-Mohammed-S/Ashik-Mohammed-S/blob/main/PORTFOLIO.md)
