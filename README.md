# SMS Spam Classifier

Quick guide to run and deploy the Streamlit app included in this repository.

1) Requirements

- Python 3.8+
- Install packages from `requirements.txt` (see below)

2) Run locally

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

3) Deploy on Streamlit Community Cloud

- Go to https://share.streamlit.io
- Log in with GitHub and choose **New app → From a GitHub repo**
- Select this repository and branch `main`, and set the file path to `app.py`
- Click **Deploy**

Notes

- This repository contains saved model artifacts so the Streamlit app can run without retraining.
- If your model artifacts are large, consider using Git LFS or hosting them separately and updating `app.py` to download them at startup.
