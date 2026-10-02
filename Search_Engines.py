from search_engines import bing_search

# Construct a search URL for Bing
url = bing_search.get_search_url('Tesla TSLA')

# Use requests to fetch the HTML page
import requests

resp = requests.get(url)
html = resp.text

# Extract structured search results
results, next_page_url = bing_search.extract_search_results(html, url)

for item in results:
  print(item['title'], item['url'])
