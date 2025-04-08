import requests
from bs4 import BeautifulSoup
import json

def web_scraper2():
    """ function to get data from a specific website """
    url = 'https://www.netflix.com/browse/genre/83'  
    # JSON data file path
    data_file1 = "./app/data/shows.json" 

    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # List to store the scraped data
        data = []

        # Extracting names (You can modify this to extract specific data, such as titles or descriptions)
        name_elements = soup.find_all('span')
        name_NA = [span['title-name'] for span in name_elements if 'title-name' in span.attrs]
        for name in name_elements:
            name_text = name.get_text(strip=True)
            if name_text:  
                data.append({
                    'Show Name': name_text
                })  
        data = data[3:]          

        # Extracting all 'img' tags for images
        img_tags = soup.find_all('img')
        img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

        # Combine the scraped names and image URLs
        for i in range(len(data)):
            if i < len(img_urls):
                data[i]['image_url'] = img_urls[i]
        
        # Write the data to a JSON file
        with open(data_file1, 'w') as f:
            json.dump(data, f, indent=4)
        
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []


if __name__ == "__main__":
    scraped_data = web_scraper2()
    if scraped_data:
        print("Data successfully scraped and saved.")
    else:
        print("No data found.")
