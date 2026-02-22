### Goal

To develop a high-throughput computational pipeline that classifies pathogen effectors using a fine-tuned Protein Language Model (pLM).

### Hypothesis

Fine-tuning a pre-trained ESM-2 model on the PHI-base dataset will allow the model to capture effector-specific structural motifs and evolutionary signatures more accurately than traditional sequence-alignment methods (e.g. HMMer), enabling faster functional annotation of novel pathogen sequences into specific virulence classes.

### Rationale

- **Structural Context:** ESM-2 captures latent structural information within its embeddings, which is critical for effector proteins that often lack primary sequence homology but share conserved 3D folds to manipulate host targets.
- **Speed and Scalability:** Once fine-tuned, inference is significantly faster than AlphaFold2 for initial large-scale screening of newly sequenced pathogen genomes.
- **Platform Fit:** A pLM-based classifier could serve as a high-throughput triage step for identifying high-priority virulence targets prior to experimental validation.

### Experimental Plan

- **Data Curation**: Extract and clean sequences from the PHI-base dataset. Ensure balanced representation of the five core phenotype classes: loss of pathogenicity, reduced virulence, increased virulence, unaffected pathogenicity, and effector.    
- **Prototyping**: Implement a JAX-based classification head on top of the frozen ESM-2 encoder to validate data loading and gradient flow.
- **Fine-Tuning**: Execute full-parameter or LoRA (Low-Rank Adaptation) fine-tuning on an A100 GPU (Colab) to optimize weights for effector-specific motifs.
- **Validation**: Compare model accuracy against the ground truth labels in a held-out test dataset and generate a confusion matrix to identify specific classification overlaps.
- **Integration**: Transfer the finalised model weights and training logic to a Google Cloud Platform GCS Bucket and document the deployment via Vertex AI.
### Key Literature

**1. PHI-base**
Urban et al., 2025 "PHI-base – the multi-species pathogen–host interaction database in 2025"
https://doi.org/10.1093/nar/gkae1084

**2. ESM-2**
Lin et al., 2022 "Evolutionary-scale prediction of atomic-level protein structure with a protein language model"
https://doi/10.1126/science.ade2574

**3. pLM Parameter-Efficient Fine-Tuning**
Schmirler et al., 2024 "Fine-tuning protein language models boosts predictions across diverse tasks"
https://doi.org/10.1038/s41467-024-51844-2

**4. pLM Parameter-Efficient Fine-Tuning**
Sledzieski et al., 2024 "Democratizing protein language models with parameter-efficient fine-tuning"
https://doi.org/10.1073/pnas.2405840121
