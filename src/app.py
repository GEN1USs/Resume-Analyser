import streamlit as st
import requests

st.title("AI-Powered Resume Analyzer")

resume_file = st.file_uploader("Upload Resume (text or PDF)", type=["txt", "pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):
    if resume_file and job_desc:
        files = {"resume": resume_file.getvalue()}
        data = {"text": job_desc}
        response = requests.post("http://localhost:8000/analyze/", data=data, files=files)
        result = response.json()
        st.write("**Result**")
        st.write("**Fit Level:**", result["prediction"])
        st.write("**Confidence:**", f"{result['confidence']*100:.2f}%")
    else:
        st.error("Please upload both resume and job description!")