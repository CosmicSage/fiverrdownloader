#!/usr/bin/env python
import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
import re
from urllib.parse import urlparse

# Define the target URL
target_url = "https://fiverr.com/kymmypops"  # Replace with the website URL you want to scrape

# Define the domain you want to filter for
target_domain = "fiverr-res.cloudinary"

# Define user agent and other browser-related headers
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
"Accept-Language": "en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
}

# Send an HTTP GET request to the target URL
response = requests.get(target_url, headers=headers)



# Check if the request was successful
if True:
# if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Get the raw HTML content
    raw_html = response.text

    # Write the raw HTML content to a file
    with open("out.html", "w", encoding="utf-8") as file:
        file.write(raw_html)

    # exit()

    # Find all the URLs in the HTML content
    urls = re.findall('"((http)s?://.*?)"', raw_html)
    # urls = re.findall(rf'https://{target_domain}\.com\S*', raw_html)
    # urls = [re.findall(rf'https://{target_domain}\.com\S*', url) for url in urls]

    print(len(urls))

    # Filter and print the URLs with the specified domain
    domain_urls = [url for url in urls if target_domain in urlparse(url[0]).netloc]
    print(len(domain_urls))
    for url in domain_urls:
        print(url, end="\n\n")


    print("Raw HTML response has been written to 'out.html'.")

    # # Iterate through the links and filter by domain
    # domain_links = [link.get('href') for link in links if link.get('href') and target_domain in urlparse(link.get('href')).netloc]
    #
    # # Print the filtered URLs
    # for link in domain_links:
    #     print(link)
else:
    print("Failed to retrieve the web page. Status code:", response.status_code)
