# 🛡️ Phishing Email Detection Using BERT

## 🚀 Live Demo

**Hugging Face Space:**
https://huggingface.co/spaces/kadiravyshnavi/phishing-email-detector

**GitHub Repository:**
https://github.com/kadiravyshnavi/phishing-email-detection-bert

---

## 📌 Project Overview

Phishing emails are one of the most common cybersecurity threats. This project uses a fine-tuned BERT (Bidirectional Encoder Representations from Transformers) model to automatically classify emails as either:

* ✅ Legitimate Email
* ⚠️ Phishing Email

The model was trained on a phishing email dataset and deployed using Streamlit and Hugging Face Spaces for real-time predictions.

---

## 🎯 Features

* Real-time phishing email detection
* BERT-based NLP classification
* Streamlit web interface
* Cloud deployment using Hugging Face
* High accuracy email classification
* End-to-end machine learning pipeline

---

## 🛠️ Tech Stack

* Python
* PyTorch
* Transformers (BERT)
* Streamlit
* Hugging Face Spaces
* Docker
* GitHub
* Pandas
* Scikit-learn

---

## 📊 Model Performance

### Accuracy Metrics

| Metric    | Score  |
| --------- | ------ |
| Accuracy  | 99%    |
| Precision | 99%    |
| Recall    | 98-99% |
| F1 Score  | 99%    |

### Confusion Matrix

### Classification Report

### Performance Summary

* True Negatives (Legitimate Correctly Identified): 1425
* False Positives: 16
* False Negatives: 28
* True Positives (Phishing Correctly Identified): 1531

The model achieved approximately **99% accuracy** on a test dataset of 3000 email samples.

---

## 🚀 Application Interface

The deployed application allows users to paste email content and instantly receive a phishing or legitimate classification result.

---

## 📂 Project Structure

```text
phishing-email-detection-bert/
│
├── app.py
├── requirements.txt
├── README.md
├── phishing_email_detection_using_bert.ipynb
├── confusion_matrix.png
├── classification_report.png
└── app_ui.png
```

---

## ▶️ Run Locally

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

---

## 💡 Future Enhancements

* Confidence score visualization
* Risk level classification (Low / Medium / High)
* Email subject and body analysis
* Explainable AI predictions
* Browser extension integration
* Email client integration

---

## 👩‍💻 Author

**Vyshnavi Kadira**
Chaitanya Bharathi Institute of Technology (CBIT)

---

## ⭐ Acknowledgements

This project was developed as part of learning and exploring Natural Language Processing (NLP), Cybersecurity, and Transformer-based Deep Learning models using BERT.
