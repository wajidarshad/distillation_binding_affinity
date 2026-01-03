# -*- coding: utf-8 -*-
"""
Created on Fri Jan  2 19:23:18 2026

@author: Wajid_Arshad_Abbasi
"""

import torch
import torch.nn as nn
from feature_extraction import *
import joblib
import numpy as np
from sklearn.preprocessing import normalize

# Define student model architecture (must be defined in advance)
class StudentNet(nn.Module):
   def __init__(self, ):
       super().__init__()
       self.fc1 = nn.Linear(3074, 384)
       self.fc2 = nn.Linear(384, 128)
       self.fc3 = nn.Linear(128, 16)
       self.out = nn.Linear(16, 1)
       # Dropout layers
       self.drop1 = nn.Dropout(0.3)
       self.drop2 = nn.Dropout(0.2)

   def forward(self, x):
       h1 = torch.relu(self.fc1(x))
       h1 = self.drop1(h1)
       h2 = torch.relu(self.fc2(h1))
       h2 = self.drop2(h2)
       features = torch.relu(self.fc3(h2))   
       output = self.out(features)
       return output, features
def read_fasta(file_path):
    sequences = {}
    with open(file_path) as f:
        seq_id = None
        seq = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if seq_id:
                    sequences[seq_id] = "".join(seq)
                seq_id = line[1:].split()[0]
                seq = []
            else:
                seq.append(line)
        if seq_id:
            sequences[seq_id] = "".join(seq)
    return sequences

ligand_feats=get_features_proPy_list_Full_des(list(read_fasta('../example/ligand.fasta').values())[0])
receptor_feats=get_features_proPy_list_Full_des(list(read_fasta('../example/receptor.fasta').values())[0])
X_test=[np.concatenate((ligand_feats,receptor_feats),axis=0)]

scaler = joblib.load("../model/scaler_propy.pkl")
label_scaler = joblib.load("../model/scaler_labels.pkl")

X_test_scaled = normalize(scaler.transform(X_test))
loaded_model = StudentNet()

# Load the saved state_dict
loaded_model.load_state_dict(torch.load('../model/student_with_diss_weights.pth'))

# Set the model to evaluation mode
# This is crucial for models with layers like dropout or batch normalization
loaded_model.eval()
with torch.no_grad():
    prediction = loaded_model(torch.tensor(X_test_scaled, dtype=torch.float32))
    scaled_prediction=label_scaler.inverse_transform([[prediction[0].item()]])
    print(f"The predicted Binding Affinity of the given complex is: {scaled_prediction[0][0]}")
