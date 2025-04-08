"""
Fjor Robles
"""
import streamlit as st
from WS_NetflixShows import web_scraper2
from WS_NetflixMovies import web_scraper1

st.markdown("# JSON View 📼")
st.sidebar.markdown("# JSON View 📼")

#point to the data file with the scraped information
data_file = "./app/data/shows.json" 
#call function
Shows = web_scraper2()
Movies = web_scraper1()
st.title("Netflix Shows Data:")
st.json(Shows)
st.title("Netflix Movies Data:")
st.json(Movies)
