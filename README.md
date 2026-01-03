# Knowledge Distillation–Based Protein–Protein Binding Affinity Prediction
(Inference-Only Usage Guide)

This repository provides an inference-only implementation of a knowledge distillation–based regression model for predicting protein–protein binding affinities from protein sequence information alone. The model has been trained using a structure-informed teacher network and a sequence-based student network, enabling the transfer of structural knowledge during training while retaining sequence-only applicability at test time.
This implementation is intended for external evaluation and practical use, consistent with the methodological standards of Bioinformatics and Briefings in Bioinformatics.
________________________________________
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
________________________________________
# Software Requirements
*	Python (version: 3.13.11)
*	PyTorch (version: 2.7.0)
*	Scikit-learn (version: 1.7.1)
*	NumPy (version: 2.3.5)
*	Biopython
*	Propy (protein sequence feature extraction) (pip install propy3)
________________________________________
# Input Format
Protein Sequences
*	FASTA format
*	Ligand and receptor chains provided separately
  
Feature Extraction (Sequence-Based)
*	Sequence features are extracted through Propy by using method define in feature_extraction.py. 
*	All feature standardization is performed using training-set statistics only. The fitted normalization parameters were saved and reused for external validation to prevent information leakage.
________________________________________
# Running Inference
*	To predict binding affinities for new complexes, use predict.py
________________________________________
# Reproducibility Statement
*	The released model corresponds exactly to the configuration reported in the manuscript.
*	Feature normalization parameters are fixed and embedded.
*	No external data is accessed during inference.
________________________________________
# Intended Use and Limitations
This model is intended for:
*	Benchmarking
*	External validation
*	Large-scale sequence-based affinity screening
  
Limitations:
*	Predictive performance is constrained by the size and diversity of available training data
*	Performance does not yet reach that of structure-based predictors, as discussed in the manuscript
________________________________________
# Citation
If you use this model or code, please cite:
Wajid Arshad Abbasi, Investigating knowledge distillation through neural networks for protein binding affinity prediction. preprint, 2026.
________________________________________
# License
MIT License
________________________________________
# Contact
For questions related to model usage or evaluation, please email at wajidarshad@uajk.edu.pk.



