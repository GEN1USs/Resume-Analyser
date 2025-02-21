# Resume-Analyser
The Resume Analyzer is an AI-powered tool that classifies resumes as Good Fit, Partial Fit, or Not a Fit based on job descriptions. It uses NLP and a BERT-based model to extract key features, providing an interactive web interface via Streamlit and an API with FastAPI, making resume screening more efficient.

## Overview
The Resume Analyzer is a machine learning project that classifies resumes as **Good Fit, Partial Fit, or Not a Fit** based on job descriptions. It uses **Natural Language Processing (NLP)** and a **Transformer-based model (BERT)** to extract key features from resumes and compare them with job descriptions.

## Features
- **Text Preprocessing:** Cleans resumes and job descriptions using `spaCy`
- **Feature Extraction:** Uses **TF-IDF** and Named Entity Recognition (NER)
- **Model Training:** Fine-tunes a **BERT** model for classification
- **API:** Deploys model using **FastAPI**
- **Web Interface:** Built with **Streamlit** for easy interaction
- **Containerization:** Uses **Docker** for deployment

## Project Structure
```
Resume-Analyzer/
│── data/               # Datasets (raw & preprocessed)
│── models/             # Saved trained models
│── notebooks/          # Jupyter Notebooks for experiments
│── src/                # Main source code
│   ├── preprocess.py   # Text preprocessing functions
│   ├── train.py        # Model training script
│   ├── predict.py      # Prediction function
│   ├── api.py          # FastAPI backend
│   ├── app.py          # Streamlit UI
│── requirements.txt    # Python dependencies
│── Dockerfile          # Containerization setup
│── README.md           # Project documentation
```

## Installation
### Prerequisites
- Python 3.9+
- Git
- Docker (for deployment)

### Clone Repository
```bash
git clone https://github.com/yourusername/Resume-Analyzer.git
cd Resume-Analyzer
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Project
### 1. Start FastAPI Backend
```bash
uvicorn src.api:app --reload
```

### 2. Run Streamlit Frontend
```bash
streamlit run src/app.py
```

## Deployment with Docker
```bash
docker build -t resume-analyzer .
docker run -p 8000:8000 resume-analyzer
```

## Datasets
- [Resume Dataset](https://www.kaggle.com/datasets/ayushvij02/resume-dataset)
- [Job Descriptions Dataset](https://www.kaggle.com/datasets/jakecoppinger/job-descriptions)

## Technologies Used
- **Python** (NLP, Machine Learning)
- **Transformers (BERT)** (Hugging Face)
- **FastAPI** (API Backend)
- **Streamlit** (Frontend)
- **Docker** (Deployment)

## Contributing
Feel free to submit pull requests or report issues!

## License
This project is licensed under the MIT License.

