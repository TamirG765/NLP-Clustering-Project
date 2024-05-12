# streamlit run streamlit_app.py

import streamlit as st
import requests

# Streamlit title
st.title('Mobile Communication Analysis')
st.write('This application let users to pick how many groups they want and show the names and number of claims in each group.')

# User input for the number of groups
groups = st.number_input('Enter the number of groups:', min_value=2, max_value=10, value=2, step=1)

# Button to trigger clustering
if st.button('Start'):
    
    # Making a request to the FastAPI backend
    response = requests.get(f'http://localhost:8000/group_paragraphs?groups={int(groups)}')
    
    if response.status_code == 200:
        results = response.json()
        st.write('Clustering completed successfully.')
        st.write(results)
    else:
        st.error('Failed to fetch results from the backend.')
