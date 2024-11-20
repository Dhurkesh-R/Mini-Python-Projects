from bs4 import BeautifulSoup
import requests 
import numpy as np
import csv
from datetime import datetime

LINK = "https://www.amazon.sg/s?k=printer&rh=n%3A6314449051%2Cp_n_feature_twelve_browse-bin%3A24310805051&dc&ds=v1%3Af2d1lTWJqzY4j4FfyAqi0FgDccFH0%2BJUbZUbCXPp0HM&crid=1TIU5NBJ7ZK6O&qid=1717051872&rnid=24310758051&sprefix=pri%2Caps%2C662&ref=sr_nr_p_n_feature_twelve_browse-bin_2"

def get_prices_by_link(link):
    # get source
    r = requests.get(link)
    # parse source
    page_parse = BeautifulSoup(r.text, 'html.parser')
    # find all list items from search results
    search_results = page_parse.find_all("div", {"data-component-type": "s-search-result"})

    if not search_results:
        print("No search results found.")
        return []

    item_prices = []

    for result in search_results:
        price_whole = result.find("span", {"class": "a-price-whole"})
        price_fraction = result.find("span", {"class": "a-price-fraction"})
        if price_whole and price_fraction:
            price_as_text = price_whole.text + price_fraction.text
            price = float(price_as_text.replace(",", ""))
            item_prices.append(price)
    
    return item_prices

def remove_outliers(prices, m=2):
    data = np.array(prices)
    return data[abs(data - np.mean(data)) < m * np.std(data)]

def get_statistics(prices):
    min_price = np.min(prices)
    max_price = np.max(prices)
    avg_price = np.mean(prices)
    return min_price, max_price, avg_price

def save_to_file(min_price, max_price, avg_price):
    fields = [datetime.today().strftime("%B-%d-%Y"), np.around(avg_price, 2), np.around(min_price, 2), np.around(max_price, 2)]
    with open('prices.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(fields)

if __name__ == "__main__":
    prices = get_prices_by_link(LINK)
    if prices:
        prices_without_outliers = remove_outliers(prices)
        min_price, max_price, avg_price = get_statistics(prices_without_outliers)
        print(f"Average Price: {avg_price}")
        print(f"Minimum Price: {min_price}")
        print(f"Maximum Price: {max_price}")
        save_to_file(min_price, max_price, avg_price)
    else:
        print("No prices to process.")
