import streamlit as st
import requests

def get_json_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        st.error(f"Error retrieving JSON data: {e}")
        return None

def json_web_controller():
    st.title("JSON Web Controller")

    # Input URL for JSON data
    json_url = st.text_input("Enter JSON URL:", "https://jsonplaceholder.typicode.com/todos/1")

    # Button to fetch and display JSON data
    if st.button("Fetch JSON Data"):
        st.info(f"Fetching data from: {json_url}")
        json_data = get_json_data(json_url)

        if json_data:
            # Display JSON data
            st.write("### JSON Data:")
            st.json(json_data)