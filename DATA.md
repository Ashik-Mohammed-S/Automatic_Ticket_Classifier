# Recovered data and execution

The public copies below match the filenames and schemas used by this notebook.
Original lost-file byte identity cannot be proved. URLs are pinned to source commits,
and SHA-256 checksums in dataset-sources.json prevent silent source changes.
Data is downloaded locally rather than added as new dataset blobs in this PR.

| File | Rows / tokens | Source |
| --- | --- | --- |
| `complaints-2021-05-14_08_16.json` | 78313 | [Pinned source](https://raw.githubusercontent.com/himsitm/NLP_Automatic_Ticket_Classification_Assignment/2222a58b80f841a592f5af7253e86efeb8bb0d53/complaints-2021-05-14_08_16.zip) |

Source repository license metadata: No explicit repository license was reported; data is restored by download and no new redistribution license is granted.

```sh
python -m pip install -r requirements.txt
python scripts/fetch_data.py
python scripts/run_notebook.py --mode quick
python -m jupyterlab
```

Install the spaCy English model first where used: `python -m spacy download en_core_web_sm`.
The notebook also restores missing reference files automatically when run from the repository root.
Set DATA_DIR to use another directory containing these same reference files.
Existing files with a different checksum are left untouched and reported as mismatches.

Quick mode uses 1,500 real complaint narratives. Full experiments are available with `--mode full`, or set RUN_MODE=full before
launching the notebook. Quick results demonstrate execution; they do not reproduce
the historical trained-model quality. The runner writes results/execution-report.json.

