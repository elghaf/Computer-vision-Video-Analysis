import requests
from bs4 import BeautifulSoup

# extract data from websites
# Define the URL of the webpage you want to scrape
url = "https://www.affiliateprogramdb.com/reviews/automattic-wordpress-com-affiliate-program/"  # Replace with the actual URL

# Send an HTTP GET request to the webpage
response = requests.get(url)



# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(response.content, "html.parser")

# Scrape the fields using appropriate CSS selectors or XPath expressions
website_url = url

# Example CSS selectors for scraping the fields
affiliate_program_url = soup.select_one("CSS_SELECTOR_FOR_AFFILIATE_PROGRAM_URL").get("href")
affiliate_program_name = soup.select_one("CSS_SELECTOR_FOR_AFFILIATE_PROGRAM_NAME").text
video_url = soup.select_one("CSS_SELECTOR_FOR_VIDEO_URL").get("src")
image_url = soup.select_one("CSS_SELECTOR_FOR_IMAGE_URL").get("src")
brand_description = soup.select_one("CSS_SELECTOR_FOR_BRAND_DESCRIPTION").text
affiliate_program_description = soup.select_one("CSS_SELECTOR_FOR_AFFILIATE_PROGRAM_DESCRIPTION").text
related_niches = [item.text for item in soup.select("CSS_SELECTOR_FOR_RELATED_NICHES")]
program_type = soup.select_one("CSS_SELECTOR_FOR_PROGRAM_TYPE").text
company_type = soup.select_one("CSS_SELECTOR_FOR_COMPANY_TYPE").text


# Print or process the scraped data as needed
print("Website URL:", website_url)
print("Affiliate Program URL:", affiliate_program_url)
print("Affiliate Program Name:", affiliate_program_name)
print("Video URL:", video_url)
print("Image URL:", image_url)
print("Brand Description:", brand_description)
print("Affiliate Program Description:", affiliate_program_description)
print("Related Niches:", related_niches)
print("Program Type:", program_type)
print("Company Type:", company_type)
