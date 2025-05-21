
from config import get_documentai_client
client = get_documentai_client()

from google.cloud import documentai_v1 as documentai
import re

def identity_proof(file_path):
    """
    Possible proofs: 
    1. Aadhaar
    2. PAN
    Things being checked in documents : Name + Gender + DOB + ValidIDNo + location(optional) 
    """

    project_id = "agricultureloanpoc"
    location = "us"  # Or "eu"
    processor_id = "a853506b322a51ac" #id doc processor.
    mime_type = "application/pdf"

    processor_name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    # client = documentai.DocumentProcessorServiceClient()

    with open(file_path, "rb") as file:
        file_content = file.read()

    raw_document = documentai.RawDocument(content=file_content, mime_type=mime_type)
    request = documentai.ProcessRequest(name=processor_name, raw_document=raw_document)
    result = client.process_document(request=request)
    document = result.document

    text = document.text.lower()

    name_check = bool(re.search(r"\b(cristiano ronaldo|[a-z]{3,} [a-z]{2,})\b", text))
    # gender_check = any(g in text for g in ["male", "female", "other"])
    dob_check = bool(re.search(r"\b\d{2}[/-]\d{2}[/-]\d{4}\b", text))  # e.g., 01/01/1990
    aadhaar_check = bool(re.search(r"\b\d{4} \d{4} \d{4}\b", text))
    pan_check = bool(re.search(r"\b[A-Z]{5}[0-9]{4}[A-Z]{1}\b", text, re.IGNORECASE))

    has_valid_id = any([aadhaar_check, pan_check])
    required_fields_present = all([name_check]) and has_valid_id
    return required_fields_present

# file_path = "/home/shilpifire/Documents/projectAssig/ahdaar.pdf"
# file_path = '/home/shilpifire/Documents/projectAssig/Aadhaar_letter_large.pdf'
# # file_path = "/home/shilpifire/Documents/projectAssig/pan.pdf" 
# file_path = "/home/shilpifire/Documents/projectAssig/pass.pdf"
# text_retrieved = identity_proof(file_path)
# print(text_retrieved)

def address_proof(file_path): 
    """ 
    Accept: 1. Electiricty / Water / Gas bill 
    2. Passport 
    3. driving License 
    """
    project_id = "agricultureloanpoc"
    location = "us"  # Or "eu"
    processor_id = "7712f151ed52961b"
    mime_type = "application/pdf"

    processor_name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    # client = documentai.DocumentProcessorServiceClient()

    with open(file_path, "rb") as file:
        file_content = file.read()

    raw_document = documentai.RawDocument(content=file_content, mime_type=mime_type)
    request = documentai.ProcessRequest(name=processor_name, raw_document=raw_document)
    result = client.process_document(request=request)
    document = result.document

    text = document.text.lower()

    # Checks for name
    name_check = bool(re.search(r"[a-z]{3,} [a-z]{2,}", text))

    # Check for address – look for keywords like street, locality, city, pin
    address_keywords = ["road", "street", "sector", "lane", "nagar", "city", "district", "pincode", "pin", "state", "address"]
    address_check = any(keyword in text for keyword in address_keywords)

    # Check for known document hints
    is_utility = any(k in text for k in ["electricity", "water bill", "gas bill", "discom", "bijli", "bill no"])
    # is_passport = "passport" in text
    # is_license = "driving license" in text or "licence" in text

    # Utility Bill Case
    if is_utility:
        print("Utility Bill Detected")
        utility_date_check = bool(re.search(r"\d{2}[/-]\d{2}[/-]\d{4}", text))
        return name_check and address_check

    else:
        print("No known address proof format detected.")
        return False
    

def income_proof(file_path): 
    """ 
    Accept 1. Bank Statement 
    """
    project_id = "agricultureloanpoc"
    location = "us"
    processor_id = "7712f151ed52961b"
    mime_type = "application/pdf"

    processor_name = f"projects/{project_id}/locations/{location}/processors/{processor_id}"
    # client = documentai.DocumentProcessorServiceClient()

    with open(file_path, "rb") as file:
        file_content = file.read()

    raw_document = documentai.RawDocument(content=file_content, mime_type=mime_type)
    request = documentai.ProcessRequest(name=processor_name, raw_document=raw_document)
    result = client.process_document(request=request)
    document = result.document

    text = document.text.lower()

    # Basic field checks
    name_check = bool(re.search(r"[a-z]{3,} [a-z]{2,}", text))  # First + last name
    account_number_check = bool(re.search(r"\b\d{2,5}[-\s]?\d{2,5}[-\s]?\d{2,5}\b", text))
    bank_keywords = ["bank", "account", "statement", "ifsc", "branch"]

    bank_context_check = any(word in text for word in bank_keywords)
    # print('account no check: ', account_number_check) 
    # print('name check: ', name_check) 
    # print('bank context check: ', bank_context_check)
    if account_number_check and name_check and bank_context_check:
        return True
    else:
        return False