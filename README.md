# SMS Spam Classifier

![License: MIT](https://img.shields.io/badge/license-MIT-brightgreen)
![Language: Python](https://img.shields.io/badge/language-Python-blue)

Professional documentation for the SMS Spam Classifier project. This README follows a clear, structured format so contributors and users can quickly understand, run, and extend the project.

Table of contents
- [Project overview](#project-overview)
- [Repository structure](#repository-structure)
- [Quick start](#quick-start)
- [How it was built](#how-it-was-built)
- [Model artifacts & data](#model-artifacts--data)
- [Running locally](#running-locally)
- [Deploying to Streamlit Community Cloud](#deploying-to-streamlit-community-cloud)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## Project overview

The SMS Spam Classifier is a small demo project demonstrating a text classification pipeline that detects whether an SMS message is spam or not. The repository includes:

- a Streamlit app (`app.py`) that provides a minimal UI for running inference,
- the original dataset used for experiments (`spam.csv`),
- serialized model artifacts (if present) for fast inference without retraining,
- a short notebook demonstrating training and evaluation (`sms-spam_classifier.ipynb`).

This project is intended as a reproducible demo and learning artifact rather than a production-grade system.

## Repository structure

- `app.py` — Streamlit application and inference pipeline.
- `sms-spam_classifier.ipynb` — Jupyter notebook with EDA, preprocessing and training steps.
- `spam.csv` — Source dataset (public SMS spam collection).
- `model.pkl`, `vectorizer.pkl` — Serialized model and vectorizer used by `app.py` (may be large).
- `requirements.txt` — Python dependencies for running and deploying the app.
- `.gitignore` — files and directories ignored by Git.

## Quick start

Prerequisites:
- Python 3.8 or newer
- Git and GitHub account for deployment to Streamlit Cloud

To get started locally:

```bash
git clone https://github.com/mananbyte/SMS-Spam-Classifier.git
cd "SMS Spam Classifier"
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

Open the URL printed by Streamlit (typically `http://localhost:8501`).

## How it was built

High level steps used while creating the model and app:

1. Data ingestion: `spam.csv` is loaded with pandas and cleaned (drop duplicates / NaNs).
2. Text preprocessing: tokenization, stopword removal, stemming (PorterStemmer).
3. Vectorization: `TfidfVectorizer` or `TfidfTransformer` was used to transform SMS text to numeric features.
4. Model training: a classification model (e.g. `LogisticRegression`, `RandomForestClassifier`) was trained on the vectorized text.
5. Persistence: the fitted vectorizer and trained model were saved with `pickle`/`joblib` as `vectorizer.pkl` and `model.pkl`.
6. App wiring: `app.py` loads the artifacts, preprocesses user input, and returns the prediction.

If you want to reproduce training from scratch, open `sms-spam_classifier.ipynb` and follow the notebook cells.

## Model artifacts & data

- `spam.csv` is included for convenience and small-scale experiments.
- If `model.pkl` and `vectorizer.pkl` are present they are used directly by `app.py` for inference. If you prefer not to store binary artifacts in Git, use Git LFS or cloud storage and update `app.py` to download artifacts at runtime.

## Running locally (detailed)

1. Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

4. Use the UI to paste a message and click **Predict**.

## Deploying to Streamlit Community Cloud (recommended)

1. Visit https://share.streamlit.io and sign in with GitHub.
2. Click **New app** → **From a GitHub repo**.
3. Select `mananbyte/SMS-Spam-Classifier`, branch `main`, and set the file path to `app.py`.
4. Click **Deploy**. Streamlit will install dependencies from `requirements.txt` and run `app.py`.

Secrets and environment variables
- If your `app.py` requires secrets (API keys), add them via the Streamlit app settings (Manage → Secrets).

## Troubleshooting

- Missing NLTK resources: `app.py` includes logic to download required NLTK data into a writable `nltk_data` folder. If you still see NLTK LookupError in Streamlit logs, check the app logs (Manage → Logs) and ensure `nltk` is in `requirements.txt`.
- Dependency mismatches when unpickling models: you may see `InconsistentVersionWarning` when the scikit-learn version used to unpickle differs from the one that created the model. Rebuild the model using the environment version or retrain.
- Large binary files: if `model.pkl` or `vectorizer.pkl` are large, consider moving them off-repo (S3, GCS) or use Git LFS.

## Contributing

1. Fork the repository.
2. Create a feature branch: `git checkout -b feat/your-feature`.
3. Make changes and add tests if appropriate.
4. Open a pull request describing the change.

## License

This project is provided under the MIT License. Add a `LICENSE` file if you want to make the license explicit.

---

If you want, I can also:

- generate a `requirements.lock` or `pip freeze` for exact versions,
- add automatic model download logic (S3 or GitHub release),
- add a small CI step to run basic linting/tests on push.

Tell me which follow-up you'd like and I'll implement it.
