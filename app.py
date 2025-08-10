import streamlit as st
from study_buddy_logic import generate_study_report

st.set_page_config(page_title="AI Algorithms Study Buddy", page_icon="🤖")

st.title("AI Algorithms Study Buddy")   
st.write("This is a study buddy for AI algorithms. It will help you generate a study report.")

#user_input
user_input= st.text_input("Enter the algorithm you want to study:",
placeholder="e.g., Dijkstra's Algorithm, Bubble Sort, K-Means Clustering")

if st.button("Generate Study Report"):
    if user_input:
        with st.spinner("Your AI crew is on the job! This may take a moment..."):

            report=generate_study_report(user_input)

            st.markdown(report)
    else:
        st.warning("Please enter an algorithm topic first.")