import streamlit as st
# Import your validation functions
from proof import identity_proof, address_proof, income_proof  # Adjust path

st.title("📄 Loan Document Verifier")

st.markdown("Upload the required documents to verify identity, address, and income.")

# ---------- Identity Proof ----------
st.header("Identity Proof")
st.caption("Accepts: Aadhaar or PAN Card")
identity_file = st.file_uploader("Upload Identity Proof (PDF only)", type="pdf", key="identity")

# ---------- Address Proof ----------
st.header("Address Proof")
st.caption("Accepts; Electricity/ Water/ Gas Bill.")
address_file = st.file_uploader("Upload Address Proof (PDF only)", type="pdf", key="address")

# ---------- Income Proof ----------
st.header("Income Proof")
st.caption("Accepts: Bank Statement")
income_file = st.file_uploader("Upload Income Proof (PDF only)", type="pdf", key="income")

# ---------- Submit Button ----------
if st.button("Validate Documents"):
    if not all([identity_file, address_file, income_file]):
        st.warning("Please upload all three documents before validating.")
    else:
        # pass
        with open("identity_temp.pdf", "wb") as f:
            f.write(identity_file.read())
        with open("address_temp.pdf", "wb") as f:
            f.write(address_file.read())
        with open("income_temp.pdf", "wb") as f:
            f.write(income_file.read())

        id_result = identity_proof("identity_temp.pdf")
        addr_result = address_proof("address_temp.pdf")
        income_result = income_proof("income_temp.pdf")

        # ---------- Results ----------
        st.subheader("Results:")
        st.write(f"✅ Identity Proof Verified: {id_result}")
        st.write(f"✅ Address Proof Verified: {addr_result}")
        st.write(f"✅ Income Proof Verified: {income_result}")
