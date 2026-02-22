from setuptools import setup, find_packages

setup(
    name="esm_phi_effector",
    version="0.1.0",
    description="ESM-2 Fine-tuning for PHI-base Effector Classification",
    author="Joshua Williams",
    packages=find_packages(),
    python_requires=">=3.9",
    install_requires=[
        "biopython",
        "pandas",
        "torch",
        "transformers",
        "peft"
    ]
)
