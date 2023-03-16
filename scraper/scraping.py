import requests
from bs4 import BeautifulSoup


def scrape_data(make, model, year, location, max_price):
    url = f"https://www.otomoto.pl/osobowe/{make}/{model}/{year}/?search%5Bfilter_float_price%3Ato%5D={max_price}&search%5Bcountry%5D="
    if location:
        url += f"{location}&"
    else:
        url += "polska&"

    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find_all("article")

    data = []
    for result in results:
        try:
            title = result.find("a", class_="offer-title__link").text.strip()
            price = result.find("span", class_="offer-price__number").text.strip().replace(" ", "")
            year = result.find("li", class_="offer-item__params-item").text.strip().split("/")[0]
            mileage = result.find_all("li", class_="offer-item__params-item")[1].text.strip().split("km")[0].replace(" ", "")
            location = result.find("span", class_="seller-box__seller-address__label").text.strip()
            data.append({
                "title": title,
                "price": price,
                "year": year,
                "mileage": mileage,
                "location": location
            })
        except AttributeError:
            continue

    return data
