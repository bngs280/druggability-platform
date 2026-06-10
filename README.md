# Druggability AI Platform
# data from chembl download
# filter Human only, with compunds and activity keep them with csv Uniprot (unprot_id),Target(name of target)
Link: https://www.ebi.ac.uk/chembl/explore/targets/STATE_ID:14cqebWY36k0CKHSivC1_Q%3D%3D
## Objective

Predict whether a protein is druggable using:

* AlphaFold / ColabFold
* Binding Pocket Detection
* Feature Engineering
* XGBoost Machine Learning

## Workflow

Protein Sequence
→ Structure Prediction
→ Pocket Detection
→ Feature Extraction
→ XGBoost Prediction
→ Druggability Score

## Tech Stack

Python

FastAPI

ColabFold

Fpocket

XGBoost

Docker

GCP Cloud Run

## Directory Structure

src/
data/
models/
docker/
cloudrun/

## Run

conda activate druggability-ai

uvicorn src.api.main:app --reload


## nEw
ChEMBL Human Targets (Bioactivity)
                │
                ▼
        proteins.csv
                │
                ▼
Download AlphaFold Structures
                │
                ▼
Store PDB Files
                │
                ▼
Run Fpocket
                │
                ▼
Extract Pocket Features
                │
                ▼
Create Feature Matrix
                │
                ▼
Train XGBoost Model
                │
                ▼
Druggability Score (0-1)
                │
                ▼
FastAPI
                │
                ▼
Docker
                │
                ▼
GCP