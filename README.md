# ESM-2 Pathogen Virulence Gene Classifier

Fine-tuned ESM-2 protein language model for classifying pathogen virulence genes into functional biochemical classes.

## Overview

This project develops a computational pipeline that classifies pathogen virulence genes from PHI-base into 8 functional classes (effector, protease, kinase/signalling, transcription factor/regulator, cell wall/carbohydrate-active, transporter/membrane, secondary metabolite/biosynthesis, and secretion system) using a fine-tuned ESM-2 protein language model with LoRA parameter-efficient fine-tuning.

**Goal**: Replace traditional homology-based methods with faster, more scalable deep learning classification for functional annotation of novel pathogen sequences.

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

**In Development**

- [x] Project planning and literature review
- [x] Data curation (PHI-base dataset) - 4,518 sequences across 8 functional classes
- [ ] Model prototyping
- [ ] Fine-tuning with LoRA on A100 GPU
- [ ] Validation and benchmarking
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