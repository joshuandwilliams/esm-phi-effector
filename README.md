# ESM-2 Pathogen Virulence Gene Classifier
Fine-tuned ESM-2 protein language model for classifying pathogen virulence genes into functional biochemical classes.

## Overview
This project develops a computational pipeline that classifies pathogen virulence genes from PHI-base into 8 functional classes (Effector, Protease, Kinase / Signalling, Transcription factor / Regulator, Cell wall / Carbohydrate-active, Transporter / Membrane, Secondary metabolite / Biosynthesis, and Secretion system) using a fine-tuned ESM-2 protein language model with LoRA parameter-efficient fine-tuning.

**Goal**: Replace traditional homology-based methods with faster, more scalable deep learning classification for functional annotation of novel pathogen sequences.

## Results

All results are from 5-fold stratified cross-validation on the training pool (4,023 sequences). The best fold (fold 2) is reported for per-class metrics.

### Cross-Validation Summary

| Model | Macro F1 (mean ± std) | Accuracy (mean ± std) |
|---|---|---|
| Frozen ESM-2 150M | 0.698 ± 0.019 | 74.2% ± 0.8% |
| Frozen ESM-2 650M | 0.733 ± 0.016 | 77.3% ± 1.1% |
| LoRA ESM-2 150M | 0.742 ± 0.010 | 78.0 ± 0.8%|
| LoRA ESM-2 650M | 0.753 ± 0.008 | 79.6 ± 0.7% |

### Per-Class F1 (Best Fold — LoRA Fine-Tuned)

| Class | 150M (small) | 650M (large) |
|---|---|---|
| Effector | 0.759 | 0.783 |
| Transcription factor / Regulator | 0.873 | 0.898 |
| Kinase / Signalling | 0.750 | 0.802 |
| Protease | 0.829 | 0.800 |
| Cell wall / Carbohydrate-active | 0.725 | 0.755 |
| Transporter / Membrane | 0.755 | 0.769 |
| Secondary metabolite / Biosynthesis | 0.720 | 0.708 |
| Secretion system | 0.636 | 0.604 |

### Key Findings

- **LoRA fine-tuning improves both models over frozen baselines**, with the small model gaining more (+0.044 macro F1) than the large model (+0.020), narrowing the gap between variants from 0.035 to 0.011.
- **Top-2 accuracy reaches ~89% for both models**, with 46–50% of misclassifications having the correct class as the second prediction (vs 14.3% random chance), indicating boundary ambiguity rather than arbitrary errors.
- **The dominant confusion axis is Transcription factor / Regulator ↔ Kinase / Signalling** (21 cases in both models), reflecting genuine biological overlap in two-component signal transduction systems identified during data curation.
- **Effector ↔ Secretion system confusion is structurally expected** — effectors are delivered by secretion systems, so sequence-level similarity reflects real biological coupling.
- **Truncation is not a meaningful error source** — only 5.5% of sequences exceed the 1,022 AA token limit, with 97.7% accuracy on truncated sequences vs ~78–80% on full-length.
- **~25% of apparent errors likely reflect PHI-base annotation ambiguity** rather than genuine model failures, based on cross-class identity analysis during data curation.

## Dataset

Starting from 14,028 PHI-base records, the curation pipeline retained 4,458 unique, non-redundant sequences across 8 functional classes (31.8% of original records). The dataset was split 90/10 into a training pool (4,023 sequences) and held-out test set (447 sequences).

| Class | Train | Test |
|---|---|---|
| Transcription factor / Regulator | 1,383 | 154 |
| Kinase / Signalling | 888 | 99 |
| Effector | 588 | 65 |
| Transporter / Membrane | 330 | 37 |
| Cell wall / Carbohydrate-active | 248 | 27 |
| Secondary metabolite / Biosynthesis | 225 | 25 |
| Secretion system | 182 | 20 |
| Protease | 179 | 20 |

Key curation steps: duplicate removal, quality filtering (50–1,500 AA, standard amino acids), MMseqs2 clustering at 90% identity for redundancy reduction, and stratified train/test splitting.

## Repository Structure
This project is designed to be executed in Google Colab.
- `notebooks/`: Sequential Colab notebooks for data curation, prototyping, and fine-tuning.
- `src/`: Installable Python modules used by the notebooks.
- `configs/`: YAML configuration files for data, model, and training parameters.
- `requirements.txt`: Project dependencies.
- `setup.py`: Package installation script.

### Notebooks

| Notebook | Description |
|---|---|
| `01_data_curation.ipynb` | PHI-base download, annotation mapping to 8 classes, quality filtering, MMseqs2 redundancy reduction, train/test splitting, within-class diversity analysis |
| `02_prototyping_jax.ipynb` | JAX/Flax classification head on frozen ESM-2 embeddings, 5-fold CV baseline for both 150M and 650M variants, error analysis, memory profiling |
| `03_finetuning_lora.ipynb` | LoRA fine-tuning of both ESM-2 variants with HuggingFace Trainer, 5-fold CV, W&B logging, error analysis, checkpoints saved to GCS |

## Quick Start (Google Colab)
```python
# 1. Clone the repository in a Colab cell
!git clone https://github.com/joshuandwilliams/esm-phi-effector.git
%cd esm-phi-effector

# 2. Install MMseqs2 (not pip installable)
!apt-get install -y mmseqs2

# 3. Install dependencies and the local src package
!pip install -r requirements.txt
!pip install -e .

# 4. Open the notebooks/ directory and execute sequentially:
#    01_data_curation.ipynb → 02_prototyping_jax.ipynb → 03_finetuning_lora.ipynb
```

## Project Status

- [x] Data curation (PHI-base dataset) — 4,458 sequences across 8 functional classes
- [x] Model prototyping (frozen ESM-2 + JAX classification head)
- [x] Fine-tuning with LoRA on A100 GPU
- [ ] Test set evaluation and held-out validation
- [ ] Efficiency profiling and deployment benchmarking

## Citation
This project builds on:
- **PHI-base**: Urban et al., 2025
- **ESM-2**: Lin et al., 2022
- **pLM Fine-Tuning**: Schmirler et al., 2024; Sledzieski et al., 2024

## License
Copyright (c) 2026 Joshua Williams. All rights reserved.
This repository and its contents (including code, documentation, and model weights) are proprietary. No part of this project may be used, reproduced, or distributed for any commercial or industrial purpose without explicit written permission from the author.
Access is granted for review and evaluation purposes only.
