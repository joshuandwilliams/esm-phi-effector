# ESM-2 Pathogen Virulence Gene Classifier
Fine-tuned ESM-2 protein language model for classifying pathogen virulence genes into functional biochemical classes.

## Overview
This project develops a computational pipeline that classifies pathogen virulence genes from PHI-base into 8 functional classes (Effector, Protease, Kinase / Signalling, Transcription factor / Regulator, Cell wall / Carbohydrate-active, Transporter / Membrane, Secondary metabolite / Biosynthesis, and Secretion system) using a fine-tuned ESM-2 protein language model with LoRA parameter-efficient fine-tuning.

**Goal**: Replace traditional homology-based methods with faster, more scalable deep learning classification for functional annotation of novel pathogen sequences.

## Results

All results are from the held-out test set (447 sequences).

### Test Set Summary

| Model | Accuracy | Macro F1 | Weighted F1 |
|---|---|---|---|
| Frozen ESM-2 150M | 73.2% | 0.676 | 0.738 |
| Frozen ESM-2 650M | 76.5% | 0.721 | 0.767 |
| LoRA ESM-2 150M | 79.2% | 0.760 | 0.771 |
| LoRA ESM-2 650M | 81.0% | 0.772 | 0.789 |

### Per-Class F1 (Test Set)

| Class | Frozen 150M | Frozen 650M | LoRA 150M | LoRA 650M |
|---|---|---|---|---|
| Effector | 0.797 | 0.794 | 0.806 | 0.829 |
| Transcription factor / Regulator | 0.854 | 0.869 | 0.877 | 0.898 |
| Kinase / Signalling | 0.667 | 0.693 | 0.737 | 0.776 |
| Protease | 0.683 | 0.811 | 0.800 | 0.865 |
| Cell wall / Carbohydrate-active | 0.737 | 0.787 | 0.780 | 0.800 |
| Transporter / Membrane | 0.667 | 0.729 | 0.712 | 0.700 |
| Secondary metabolite / Biosynthesis | 0.485 | 0.500 | 0.627 | 0.696 |
| Secretion system | 0.520 | 0.583 | 0.581 | 0.612 |

### Key Findings

- **LoRA fine-tuning substantially improves on frozen baselines**, with the small model gaining +6.0% accuracy and +0.084 macro F1, and the large model gaining +4.5% accuracy and +0.051 macro F1.
- **Improvement is largest for the hardest classes** — Secondary metabolite / Biosynthesis gains +0.196 F1 and Kinase / Signalling gains +0.083 F1 in the large model, demonstrating that encoder adaptation is most valuable where frozen representations are weakest.
- **Top-2 accuracy reaches 88.8% (small) and 91.1% (large)**, with 46–53% of misclassifications having the correct class as the second prediction (vs 14.3% random chance), indicating boundary ambiguity rather than arbitrary errors.
- **~24% of apparent errors reflect PHI-base annotation noise** rather than genuine model failures, based on manual literature review of all 85 large model misclassifications. PHI-base annotation errors are predicted at strikingly higher confidence (median >0.95) than true model errors, suggesting the model has learned genuine biochemical signal.
- **Kinase / Signalling confusion is driven by class definition, not sequence diversity** — within-class diversity analysis at 30–50% identity thresholds shows no significant correlation between diversity index and per-class F1 (r = -0.27 to -0.32, p > 0.44).
- **Truncation is not a meaningful error source** — only 2.7% of test sequences exceed the 1,022 AA token limit, and accuracy on truncated sequences (83.3% and 91.7%) exceeds full-length accuracy in both models.
- **LoRA fine-tuning is computationally practical** — only 14–16% throughput overhead versus frozen baselines, while reducing peak GPU memory by up to 42% (large model: 3,386 MB vs 5,852 MB). A full fungal proteome (~12,000 proteins) can be annotated in under 14 minutes on a single GPU.

## Dataset

Starting from 14,028 PHI-base records, the curation pipeline retained 4,458 unique, non-redundant sequences across 8 functional classes (31.8% of original records). The dataset was split 90/10 into a training pool (4,011 sequences) and held-out test set (447 sequences).

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
| `01_data_curation.ipynb` | PHI-base download, annotation mapping to 8 classes, quality filtering, MMseqs2 redundancy reduction, train/test splitting |
| `02_prototyping_jax.ipynb` | JAX/Flax classification head on frozen ESM-2 embeddings, 5-fold CV baseline for both 150M and 650M variants, error analysis, memory profiling |
| `03_finetuning_lora.ipynb` | LoRA fine-tuning of both ESM-2 variants with HuggingFace Trainer, 5-fold CV, W&B logging, error analysis, checkpoints saved to GCS |
| `04_validation.ipynb` | Held-out test set evaluation, frozen vs LoRA comparison, confidence and error analysis, within-class diversity analysis, computational efficiency profiling |

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
- [x] Test set evaluation and held-out validation
- [x] Efficiency profiling and deployment benchmarking

## Citation
This project builds on:
- **PHI-base**: Urban et al., 2025
- **ESM-2**: Lin et al., 2022
- **pLM Fine-Tuning**: Schmirler et al., 2024; Sledzieski et al., 2024

## License
Copyright (c) 2026 Joshua Williams. All rights reserved.
This repository and its contents (including code, documentation, and model weights) are proprietary. No part of this project may be used, reproduced, or distributed for any commercial or industrial purpose without explicit written permission from the author.
Access is granted for review and evaluation purposes only.
