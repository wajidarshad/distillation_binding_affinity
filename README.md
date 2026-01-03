# Knowledge Distillation–Based Protein–Protein Binding Affinity Prediction
(Inference-Only Usage Guide)

This repository provides an inference-only implementation of a knowledge distillation–based regression model for predicting protein–protein binding affinities from protein sequence information alone. The model has been trained using a structure-informed teacher network and a sequence-based student network, enabling the transfer of structural knowledge during training while retaining sequence-only applicability at test time.
This implementation is intended for external evaluation and practical use, consistent with the methodological standards of Bioinformatics and Briefings in Bioinformatics.

# Method Summary
The released model corresponds to the best-performing distillation configuration identified under Leave-One-Complex-Out (LOCO) cross-validation, using:
*	Teacher network: structure-based descriptors (Moal features)
*	Student network: sequence-based descriptors (Propy features)

At inference time, only sequence-based features are required. No structural information is needed for the test complexes.

________________________________________
# Repository Scope
This repository supports:
*	Testing the pre-trained distillation-based student model
*	Predicting binding affinities for new protein–protein complexes
  
Model training and hyperparameter optimization are not included, as these are fully described in the associated manuscript and supplementary material.
________________________________________
# Directory Structure
- **`model/`** - Contains Pre-trained student model (PyTorch).
  - `student_with_diss_weights.pth` - trained model.
  - `scaler_labels.pkl` - StandarScaler for labels.
  - `caler_propy.pkl` - StandarScaler for features.
- **`example/`** - Example FASTA files (ligand & receptor).
- **`src/`** - python files.
  - `feature_extraction.py` - Propy feature extraction.
  - `predict.py ` - Model inference script.
- `README.md` - The file you are reading now.



