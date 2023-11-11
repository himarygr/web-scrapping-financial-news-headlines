import requests
from bs4 import BeautifulSoup

def scrape_financial_news(url):
    # Send a GET request to the specified URL
    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find and extract financial news headlines
        headlines = soup.find_all(class_='item__title rm-cm-item-text js-rm-central-column-item-text')

        # Print the headlines
        for index, headline in enumerate(headlines, start=1):
            print(f"{index}. {headline.text.strip()}")
    else:
        print(f"Failed to retrieve page. Status Code: {response.status_code}")

# Example usage with a hypothetical finance news website
finance_news_url = 'https://www.rbc.ru/finances/'
scrape_financial_news(finance_news_url)
