"""
Fjor Robles
"""
import streamlit as st
import json

# Path to the saved JSON data
data_file2 = "./app/data/movies.json"

def load_data():
    """Load data from the JSON file"""
    try:
        with open(data_file2, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        st.error(f"File not found: {data_file2}")
        return []
    except json.JSONDecodeError:
        st.error(f"Error decoding JSON data in: {data_file2}")
        return []

st.markdown("# Netflix Movies 🎞️")
st.sidebar.markdown("# Netflix Movie View 🎞️")

# Load the data from the JSON file
data = load_data()
# Check if there's data to display
if data:
    # Alternatively, if the data is just a list of items, you can display it as a table
    st.write("Current Showing Movies on Netflix:")
    
    #st.dataframe(data)  # Display data as a table (if it's a list of dictionaries)
    st.data_editor(
        data,
        column_config={
            "image_url":
            st.column_config.ImageColumn(label=None, width="large")
        },
        row_height=180,
    )
    #st.image("https://about.netflix.com/images/meta/netflix-symbol-black.png")
    #st.image("https://images.ctfassets.net/4cd45et68cgf/7LrExJ6PAj6MSIPkDyCO86/542b1dfabbf3959908f69be546879952/Netflix-Brand-Logo.png?w=700&h=456")
else:
    st.write("No data available to display.")
