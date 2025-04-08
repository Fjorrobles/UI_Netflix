"""
Fjor Robles
used Streamlit multipage website code as a start
"""
import streamlit as st
st.set_page_config("Netflix | Fjor ", page_icon=":movie_camera:", layout="wide",initial_sidebar_state="collapsed")
st.logo("https://images.ctfassets.net/4cd45et68cgf/7LrExJ6PAj6MSIPkDyCO86/542b1dfabbf3959908f69be546879952/Netflix-Brand-Logo.png?w=700&h=456", size="large",link="https://www.netflix.com")
# Define the page
main_page = st.Page("UI_NetflixShows.py", title="Shows", icon="🎥")
page_2 = st.Page("json_view.py", title="JSON View", icon="📼")
page_3 = st.Page("UI_NetflixMovies.py",title="Movies",icon="🎞️")


# Set up navigation
pg = st.navigation([main_page, page_3, page_2])

# Run the selected page
pg.run()
