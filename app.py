import streamlit as st
import torch
from transformers import BertTokenizer, BertForSequenceClassification
from url_analyzer import analyze_urls

# Page configuration
st.set_page_config(
    page_title="Phishing Email Detector",
    page_icon="🛡️",
    layout="centered"
)

# Load model and tokenizer
@st.cache_resource
def load_model():
    model = BertForSequenceClassification.from_pretrained(
        "kadiravyshnavi/bert-phishing-email-detector"
    )

    tokenizer = BertTokenizer.from_pretrained(
        "kadiravyshnavi/bert-phishing-email-detector"
    )

    return model, tokenizer

model, tokenizer = load_model()

# Title
st.title("🛡️ Phishing Email Detection Using BERT")
st.write(
    "Enter an email message below and the model will predict whether it is "
    "a phishing email or a legitimate email."
)

# Input box
email_text = st.text_area(
    "Enter Email Content",
    height=200,
    placeholder="Paste email content here..."
)

# Predict button
if st.button("Detect Email"):

    if email_text.strip() == "":
        st.warning("Please enter some email text.")
    else:

        inputs = tokenizer(
            email_text,
            return_tensors="pt",
            truncation=True,
            padding=True,
            max_length=128
        )

        with torch.no_grad():
            outputs = model(**inputs)

        prediction = torch.argmax(outputs.logits, dim=1).item()

        probabilities = torch.softmax(outputs.logits, dim=1)
        confidence = torch.max(probabilities).item() * 100
        if confidence >= 90:
            risk_level = "High"
        elif confidence >= 70:
            risk_level = "Medium"
        else:
            risk_level = "Low"

        st.subheader("Prediction Result")

        if prediction == 1:
            st.error(
            f"⚠️ Phishing Email Detected\n\n"
            f"Confidence: {confidence:.2f}%\n\n"
            f"Risk Level: {risk_level}"
        )
        else:
            st.success(
            f"✅ Legitimate Email\n\n"
            f"Confidence: {confidence:.2f}%\n\n"
            f"Risk Level: {risk_level}")
        url_findings = analyze_urls(email_text)
        if url_findings:
            st.subheader("🔍 URL Analysis")
            for finding in url_findings:
                st.warning(finding)

# Footer
st.markdown("---")
st.markdown(
    "Developed using BERT, PyTorch, Transformers, and Streamlit"
)
