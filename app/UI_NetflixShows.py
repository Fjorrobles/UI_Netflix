"""
Fjor Robles
"""
import streamlit as st
import json

# Path to the saved JSON data
data_file1 = "./app/data/shows.json"

def load_data():
    """Load data from the JSON file"""
    try:
        with open(data_file1, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error(f"File not found: {data_file1}")
        return []
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON data in: {data_file1}")
        return []

st.markdown("# Netflix Shows 🎥")
st.sidebar.markdown("# Netflix Shows View 🎥")
# Load the data from the JSON file
data = load_data()
# Check if there's data to display
if data:
    # Alternatively, if the data is just a list of items, you can display it as a table
    st.write("Current Showing Shows on Netflix:")
    st.data_editor(
        data,
        column_config={
            "image_url":
            st.column_config.ImageColumn(label=None, width="large")
        },
        row_height=200
    )
    #st.image("https://about.netflix.com/images/meta/netflix-symbol-black.png")
    #st.image("https://images.ctfassets.net/4cd45et68cgf/7LrExJ6PAj6MSIPkDyCO86/542b1dfabbf3959908f69be546879952/Netflix-Brand-Logo.png?w=700&h=456")
else:
    st.write("No data available to display.")
