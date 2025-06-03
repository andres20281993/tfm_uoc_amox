# Biomedical Adverse Event Mining – Case Study: Amoxicillin

This repository contains the code and documentation for a biomedical natural language processing (NLP) pipeline developed as part of a master's thesis at the Universitat Oberta de Catalunya (UOC). The objective is to extract and analyze potential adverse drug reactions (ADRs) related to **amoxicillin** by processing scientific literature from **PubMed**.

## 📌 Project Overview

The project includes:

- Retrieval of abstracts related to amoxicillin via Entrez API (NCBI)
- Preprocessing and cleaning of biomedical text
- Named Entity Recognition (NER) using **SciSpaCy**
- Generation of semantic embeddings using **BioBERT** (exploratory)
- Extraction of relations between drugs and conditions
- Visual analytics using **NetworkX**, **Matplotlib**, and **Seaborn**
- A **Streamlit** application for interactive data exploration

## 🧪 Requirements

- Python 3.10
- Recommended environment manager: [Conda](https://docs.conda.io)

Install required packages with:

```bash
pip install -r requirements.txt
```

## 🛠 Installation

Clone the repository:

```bash
git clone https://github.com/andres20281993/tfm_uoc_amox.git
cd tfm_uoc_amox
```

Set up the environment (optional but recommended):

```bash
conda create -n tfm_uoc python=3.10
conda activate tfm_uoc
pip install -r requirements.txt
```

## 🚀 Usage

1. Download abstracts using `notebooks/01_get_abstracts_pubmed.ipynb`
2. Run preprocessing and entity extraction via `02_entity_extraction.ipynb`
3. Launch the Streamlit app:

```bash
streamlit run app.py
```

## 📁 Repository Structure

```
├── data/                   # Input and output CSV files
├── notebooks/              # Jupyter notebooks for each stage
├── app.py                  # Streamlit application
├── requirements.txt        # List of required Python packages
└── README.md               # Project description and instructions
```

## 📚 References

- SciSpaCy (https://allenai.github.io/scispacy/)
- BioBERT (https://github.com/dmis-lab/biobert)
- PubMed API (https://www.ncbi.nlm.nih.gov/books/NBK25500/)
- Streamlit (https://streamlit.io)

## 🧑‍💻 Author

**Andrés Jarrín Jurado**  
Master’s in Bioinformatics and Biostatistics – UOC  
Quito, Ecuador · 2025  
GitHub: [@andres20281993](https://github.com/andres20281993)