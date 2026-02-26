### Goal

To develop a high-throughput computational pipeline that classifies pathogen virulence genes using a fine-tuned Protein Language Model (pLM).

### Hypothesis

Fine-tuning a pre-trained ESM-2 model on PHI-base data will allow the model to capture functional sequence signatures more accurately than traditional sequence-alignment methods (e.g. HMMer), enabling faster functional annotation of novel pathogen sequences into biochemical classes such as protease, kinase, and effector.

### Rationale

- **Sequence-Function Relationship:** ESM-2 captures latent structural and evolutionary information within its embeddings, which is critical for classifying virulence genes where primary sequence homology is often low across distantly related pathogens but functional class is conserved.
- **Speed and Scalability:** Once fine-tuned, inference is significantly faster than structure-based methods for initial large-scale screening of newly sequenced pathogen genomes.
- **Platform Fit:** A pLM-based classifier could serve as a high-throughput triage step for prioritising virulence gene candidates prior to experimental validation, complementing existing tools like EffectorP that focus narrowly on effector prediction.

### Experimental Plan

- **Data Curation**: Extract and clean sequences from PHI-base. Map 4,137 free-text functional annotations to 8 biochemical classes (effector, protease, kinase/signalling, transcription factor/regulator, cell wall/carbohydrate-active, transporter/membrane, secondary metabolite/biosynthesis, secretion system) via keyword matching. Reduce redundancy using MMseqs2 clustering at 90% identity.
- **Prototyping**: Implement a JAX-based classification head on top of the frozen ESM-2 encoder to validate data loading, embedding quality, and gradient flow.
- **Fine-Tuning**: Apply LoRA (Low-Rank Adaptation) fine-tuning on an A100 GPU (Colab) to optimise weights for functional class discrimination across 8 virulence gene categories.
- **Validation**: Evaluate model performance against held-out test data using per-class F1-scores and confusion matrices to identify classification overlaps between biochemically related classes.
- **Integration**: Transfer finalised model weights and training logic to a Google Cloud Platform GCS Bucket and document deployment via Vertex AI.

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