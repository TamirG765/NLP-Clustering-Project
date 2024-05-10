import requests
from bs4 import BeautifulSoup
import pandas as pd

# Function to scrape the patent claims
def scrape_patent_claims(url):
    # Fetch the content from the URL using GET method
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find the section containing the claims
    claims_section = soup.find('section', itemprop='claims')
    
    # Extract all claim divs within the section
    claims = claims_section.find_all('div', class_='claim')
    
    # Extract and clean the text from each claim div
    claims_text = [claim.get_text(separator=' ', strip=True) for claim in claims]
    
    return claims_text

# URLs of the patents
patent_urls =[
    'https://patents.google.com/patent/GB2478972A/en?q=(phone)&oq=phone',
    'https://patents.google.com/patent/US9634864B2/en?oq=US9634864B2',
    'https://patents.google.com/patent/US9980046B2/en?oq=US9980046B2'
]

# Dictionary to store claims
patent_claims = {}

# Loop through the patent URLs and scrape claims
for url in patent_urls:
    claims = scrape_patent_claims(url)
    patent_claims[url] = claims

# Convert to DataFrame for better manipulation
claims_df = pd.DataFrame(list(patent_claims.items()), columns=['Patent URL', 'Claims'])
claims_df.to_csv('patent_claims.csv', index=False)
