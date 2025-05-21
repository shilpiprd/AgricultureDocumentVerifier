import streamlit as st
from google.oauth2 import service_account
from google.cloud import documentai_v1 as documentai


def get_documentai_client():
    credentials = service_account.Credentials.from_service_account_info(st.secrets["gcp"])
    return documentai.DocumentProcessorServiceClient(credentials=credentials)
