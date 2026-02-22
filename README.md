# ESM-2 Pathogen Effector Classifier

Fine-tuned ESM-2 protein language model for classifying pathogen effector proteins into specific virulence phenotypes.

## Overview

This project develops a computational pipeline that classifies pathogen effectors into five functional virulence categories (loss of pathogenicity, reduced virulence, increased virulence, unaffected pathogenicity, and effector) using a fine-tuned ESM-2 protein language model.

**Goal**: Replace traditional homology-based methods with faster, more accurate deep learning classification for identifying high-priority virulence targets.

## Repository Structure

This project is designed to be executed in Google Colab.

- `notebooks/`: Contains the sequential Colab notebooks for data curation, prototyping, fine-tuning, and validation.
- `src/`: Contains installable Python modules used by the notebooks.
- `requirements.txt`: Project dependencies.
- `setup.py`: Package installation script.

## Quick Start (Google Colab)

```
# 1. Clone the repository in a Colab cell
!git clone [https://github.com/joshuandwilliams/esm-phi-effector.git](https://github.com/joshuandwilliams/esm-phi-effector.git)
%cd esm-phi-effector

# 2. Install dependencies and the local src package
!pip install -r requirements.txt
!pip install -e .

# 3. Open the files in the notebooks/ directory to begin execution.
```

## Project Status

**In Development**

- [x] Project planning and literature review
- [ ] Data curation (PHI-base dataset) via Colab
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
