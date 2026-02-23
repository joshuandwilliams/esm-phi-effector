# ESM-2 Pathogen Virulence Gene Classifier
Fine-tuned ESM-2 protein language model for classifying pathogen virulence genes into functional biochemical classes.

## Overview
This project develops a computational pipeline that classifies pathogen virulence genes from PHI-base into 8 functional classes (effector, protease, kinase/signalling, transcription factor/regulator, cell wall/carbohydrate-active, transporter/membrane, secondary metabolite/biosynthesis, and secretion system) using a fine-tuned ESM-2 protein language model with LoRA parameter-efficient fine-tuning.

**Goal**: Replace traditional homology-based methods with faster, more scalable deep learning classification for functional annotation of novel pathogen sequences.

## Results

| Metric | Frozen baseline | LoRA fine-tuned (val) | LoRA fine-tuned (test) |
|---|---|---|---|
| Accuracy | 75.2% | 80.1% | 80.1% |
| Macro F1 | 0.711 | 0.761 | 0.757 |
| Weighted F1 | 0.757 | 0.802 | 0.798 |

Consistent val/test performance confirms genuine generalisation rather than overfitting.

**Per-class F1 (test set):**

| Class | Frozen baseline | LoRA fine-tuned | Change |
|---|---|---|---|
| Effector | 0.778 | 0.765 | -0.013 |
| Transcription factor / Regulator | 0.827 | 0.893 | +0.066 |
| Kinase / Signalling | 0.745 | 0.780 | +0.035 |
| Protease | 0.611 | 0.757 | +0.146 |
| Cell wall / Carbohydrate-active | 0.786 | 0.808 | +0.022 |
| Transporter / Membrane | 0.667 | 0.816 | +0.149 |
| Secondary metabolite / Biosynthesis | 0.618 | 0.744 | +0.126 |
| Secretion system | 0.654 | 0.714 | +0.060 |

**Key findings:**
- LoRA fine-tuning improves macro F1 by 0.050 over frozen ESM-2 embeddings, with the largest gains in the weakest baseline classes (Protease, Transporter/Membrane, Secondary metabolite/Biosynthesis)
- Manual literature review of 40 high-confidence misclassifications found ~25% reflect PHI-base annotation errors rather than genuine model failures; correcting these raises estimated true accuracy to 82–84%
- Kinase/Signalling acts as a confusion gravity well across all classes — within-class sequence diversity analysis at 30–50% identity thresholds rules out sequence heterogeneity as the cause, pointing instead to the class definition being too functionally broad
- At optimal batch size 4 on an A100, the LoRA model achieves 38.6 sequences/second (13.9% slower than frozen baseline) while using 42% less GPU memory (808 MB vs 1,384 MB); a full fungal pathogen proteome (~12,000 proteins) can be annotated in ~5 minutes

## Repository Structure
This project is designed to be executed in Google Colab.
- `notebooks/`: Sequential Colab notebooks for data curation, prototyping, fine-tuning, and validation.
- `src/`: Installable Python modules used by the notebooks.
- `configs/`: YAML configuration files for data, model, and training parameters.
- `requirements.txt`: Project dependencies.
- `setup.py`: Package installation script.

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
#    01_data_curation.ipynb → 02_prototyping_jax.ipynb → 03_finetuning_lora.ipynb → 04_validation.ipynb
```

## Project Status
**Complete**
- [x] Project planning and literature review
- [x] Data curation (PHI-base dataset) — 4,518 sequences across 8 functional classes
- [x] Model prototyping (frozen ESM-2 + JAX classification head, 75.2% accuracy)
- [x] Fine-tuning with LoRA on A100 GPU (80.1% accuracy, 0.761 macro F1)
- [x] Validation and benchmarking (test set, error analysis, diversity analysis, efficiency profiling)
- [ ] Deployment to GCP

## Citation
This project builds on:
- **PHI-base**: Urban et al., 2025
- **ESM-2**: Lin et al., 2022
- **pLM Fine-Tuning**: Schmirler et al., 2024; Sledzieski et al., 2024

## License
Copyright (c) 2026 Joshua Williams. All rights reserved.
This repository and its contents (including code, documentation, and model weights) are proprietary. No part of this project may be used, reproduced, or distributed for any commercial or industrial purpose without explicit written permission from the author.
Access is granted for review and evaluation purposes only.