import requests
from bs4 import BeautifulSoup
import json
import streamlit as st

@st.cache_data(show_spinner="Fetching data from Netflix", ttl=60*10)
def web_scraper1():
    """ function to get data from a specific website """
    url = 'https://www.netflix.com/browse/genre/34399'  
    # JSON data file path
    data_file2 = "./app/data/movies.json" 
    
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # List to store the scraped data
        data = []
        
        # Extracting all 'img' tags for images
        img_tags = soup.find_all('img')
        img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]
        
        # Extracting names (You can modify this to extract specific data, such as titles or descriptions)
        name_elements = soup.find_all('span')
        for name in name_elements:
            name_text = name.get_text(strip=True)
            if name_text:  
                data.append({
                    'Movie Name': name_text
                })
        
        # Skip first three elements of data from webpage
        data = data[3:784]

        # Combine the scraped names and image URLs
        for i in range(len(data)):
            if i < len(img_urls):
                data[i]['image_url'] = img_urls[i]
        
        # Write the data to a JSON file
        with open(data_file2, 'w') as f:
            json.dump(data, f, indent=4)
        
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []


if __name__ == "__main__":
    scraped_data = web_scraper1()
    if scraped_data:
        print("Data successfully scraped and saved.")
    else:
        print("No data found.")
