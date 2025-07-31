import streamlit as st

# --- Title and description ---
st.title("AQAP-2110 Compliance Checklist")
st.subheader("Radar Subsystem Change Evaluation")

st.markdown("""
This tool helps evaluate whether a proposed change to a radar subsystem complies with AQAP-2110 requirements.
Please go through each checklist item below:
""")

# --- Checklist Items ---
checklist = {
    "Change impact analysis documented": False,
    "Risk assessment performed and approved": False,
    "Configuration management updated": False,
    "Supplier notified and documentation reviewed": False,
    "Testing and validation plan defined": False,
    "QA notified of change and has signed off": False,
    "Customer approval (if required) documented": False,
    "Training needs evaluated and addressed": False,
    "Traceability maintained for all modified parts": False,
    "Verification of compliance with all technical requirements": False
}

# --- User interaction ---
st.header("Checklist")
checked_items = []
for item in checklist:
    if st.checkbox(item):
        checked_items.append(item)

# --- Result output ---
st.markdown("---")
st.subheader("Checklist Summary")

total = len(checklist)
completed = len(checked_items)
st.write(f"✅ Completed: {completed} / {total}")

if completed == total:
    st.success("The change appears to meet all AQAP-2110 compliance requirements.")
else:
    st.warning("Not all compliance points have been completed. Please review before proceeding.")

# --- Optional notes ---
st.markdown("---")
notes = st.text_area("Additional Notes or Comments")
if st.button("Submit"):
    st.success("Checklist submitted. Thank you!")

