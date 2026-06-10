# Druggability AI Platform

## Overview

The **Druggability AI Platform** is an end-to-end computational pipeline for predicting the **druggability potential of human proteins** using structural biology and machine learning.

Instead of relying on manually curated druggable/non-druggable labels, this platform leverages:

* Known human drug targets
* AlphaFold protein structures
* Binding pocket analysis using Fpocket
* Pocket feature engineering
* Machine learning models
* REST API deployment

The final output is a **Druggability Score (0–1)** indicating the likelihood that a protein possesses druggable characteristics.

---
# Data from chembl download
filter Human only, with compunds and activity keep them with csv Uniprot (unprot_id),Target(name of target)
Link: https://www.ebi.ac.uk/chembl/explore/targets/STATE_ID:14cqebWY36k0CKHSivC1_Q%3D%3D

# Pipeline

```
Known Drug Targets
          │
          ▼
Data Cleaning
          │
          ▼
Download AlphaFold Structures
          │
          ▼
Run Fpocket
          │
          ▼
Extract Pocket Features
          │
          ▼
Build Feature Matrix
          │
          ▼
Train AI Model
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
GCP Deployment
```

---

# Project Structure

```
druggability-platform/

├── README.md
├── requirements.txt
├── environment.yml

├── data
│   ├── raw
│   ├── processed
│   ├── pdb
│   ├── fpocket
│   └── features

├── models

├── src
│   ├── cleaning
│   ├── download
│   ├── fpocket
│   ├── features
│   ├── training
│   ├── inference
│   └── api

└── notebooks
```

---

# Dataset

The dataset is constructed from **human protein targets with bioactivity information**.

Initial columns:

| Target | Accessions |
| ------ | ---------- |
| EGFR   | P00533     |
| AKT1   | P31749     |
| BRAF   | P15056     |

After preprocessing:

| Target | UniProt |
| ------ | ------- |
| EGFR   | P00533  |
| AKT1   | P31749  |
| BRAF   | P15056  |

Multiple UniProt accessions are automatically split into individual rows.

Duplicates are removed before downstream analysis.

---

# Step 1: Data Cleaning

```
python src/cleaning/splitting.py
python src/cleaning/cleaning_data.py

```

Tasks:

* Fix malformed CSV rows
* Split multiple UniProt IDs
* Remove duplicates
* Generate cleaned dataset

Output:

```
data/processed/proteins_final.csv
```

---

# Step 2: Download AlphaFold Structures

```
python src/download/download_alphafold.py
```

For every UniProt accession:

```
P00533

↓

AlphaFold

↓

P00533.pdb
```

Output:

```
data/pdb/
```

---

# Step 3: Run Fpocket

```
python src/fpocket/run_fpocket.py
```

The pipeline:

* Reads every PDB
* Runs Fpocket
* Skips completed proteins
* Continues after failures

Output:

```
P00533_out/
P31749_out/
...
```

---

# Step 4: Feature Extraction

```
python -m src.features.extract_features

```

Extracted features include:

* Number of pockets
* Largest pocket volume
* Mean pocket volume
* Hydrophobicity
* Polarity
* Druggability score
* Alpha sphere count

Output:

```
data/features/features.csv
```

---

# Step 5: Build Feature Matrix

Pocket features are aggregated into a machine learning dataset.

Example:

| UniProt | PocketCount | MaxVolume | MeanVolume |
| ------- | ----------- | --------- | ---------- |

Output:

```
data/processed/training_data.csv
```

---

# Step 6: Train AI Model

```
python src/training/train.py
```

Current model:

* XGBoost (recommended)

Future models:

* LightGBM
* CatBoost
* Deep Neural Networks

Output:

```
models/model.pkl
```

---

# Step 7: Prediction

```
python src/inference/predict.py
```

Input:

```
UniProt ID
```

or

```
Protein Structure
```

Output:

```
{
    "score":0.91
}
```

---

# Step 8: REST API

```
POST /predict
```

Example:

```json
{
    "uniprot":"P00533"
}
```

Response:

```json
{
    "score":0.94
}
```

---

# Docker

Build

```
docker build -t druggability-ai .
```

Run

```
docker run -p 8000:8000 druggability-ai
```

---

# GCP Deployment

The application can be deployed on:

* Google Compute Engine
* Cloud Run
* GKE (future)

---

# Current Workflow

```
proteins.csv

↓

Cleaning

↓

AlphaFold Structures

↓

Fpocket

↓

Pocket Features

↓

Feature Matrix

↓

Machine Learning

↓

Prediction
```

---

# Future Roadmap

* Integrate ESM2 protein embeddings
* Combine sequence and structural features
* Improve feature engineering
* Hyperparameter optimization
* Batch prediction API
* Interactive web dashboard
* Automated CI/CD
* Large-scale deployment on GCP

---

# Tech Stack

* Python
* Pandas
* NumPy
* AlphaFold Database
* Fpocket
* XGBoost
* FastAPI
* Docker
* Google Cloud Platform

---

# Goal

To build a scalable AI platform capable of estimating the **druggability potential of human proteins** by integrating structural analysis and machine learning into a production-ready pipeline.
