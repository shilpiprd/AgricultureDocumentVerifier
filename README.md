# 📄 Automated Loan Document Processor

A web application that allows users to upload key documents to check if their submission is sufficient to begin an agricultural loan application process.

---

## 🚀 What This App Does

This app simulates a document pre-screening tool for agricultural loan applications.

Users are required to upload three types of documents:

1. **Identity Proof**  
   - Accepts: Aadhaar or PAN card  
   - Required fields: Name and Aadhaar number / PAN number

2. **Address Proof**  
   - Accepts: Electricity Bill, Water Bill, or Gas Bill  
   - Required fields: Name and full or partial address

3. **Income Proof**  
   - Accepts: Bank Statement  
   - Required fields: Name and Account Number

Each document is scanned using Google Cloud’s Document AI, and simple heuristics (via regex) are used to check for required fields. If the expected information is present, the document is considered verified.

---

## 🧪 How It Works

- Documents are parsed using **Google Cloud Document AI** (Form Parser and ID Parser)
- Extracted text is validated using **regex-based rules**
- The app is built using **Streamlit** for an intuitive and fast user experience
- All files must be uploaded in **PDF format**
- Feedback is provided instantly for each document category

---

## 🌐 Live App

👉 Try the app here: [Agriculture Document Verifier](https://agriculturedocumentverifier-betvtbmntzgp9ux7hmr66x.streamlit.app/)

---

## 🛠 Tech Stack

- [Streamlit](https://streamlit.io/) – For the web interface
- [Google Cloud Document AI](https://cloud.google.com/document-ai) – For document text extraction
  - ID Document Processor
  - Form Parser
- Python (regex for field validation)
- Hosted on Streamlit Cloud

---

## 🔐 Note on Security

No credentials are included in this repository. GCP authentication is handled securely using Streamlit Cloud’s **Secrets Management** feature.

---

## 🧠 Future Improvements

- Multi-language support for regional documents.
- Adding more options for the addition of document for confirming a category of Proof. 

---

🖼️ The final interface looks like below:
<br> 

<p float="left">
  <img src="Pasted image.png" width="700" length="310" />
</p>