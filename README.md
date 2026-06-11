# 🧬 Druggability AI: Structure-Based Drug Target Prediction System

An end-to-end **AI-powered drug target prioritization platform** that predicts protein druggability from UniProt IDs using structural biology and machine learning.

The system integrates:
- 🧬 AlphaFold protein structures
- 🧪 fpocket binding pocket detection
- 📊 Feature engineering from protein structures
- 🤖 XGBoost machine learning model
- 🌐 FastAPI deployment for real-time inference

It converts raw protein identifiers into a **quantitative druggability score** to prioritize potential therapeutic targets.
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
python -m src.inference.test
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
uvicorn src.api.main:app     --host 0.0.0.0     --port 8000
Open in Browser: http://0.0.0.0:8000/docs
```

Example:

```json
{
    "uniprot":"A6NCS4"
}
```

Response:

```json
{
  "uniprot": "A6NCS4",
  "score": 0.9937459230422974,
  "prediction_class": 1,
  "probability": {
    "class0": 0.006254076957702637,
    "class1": 0.9937459230422974
  }
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
