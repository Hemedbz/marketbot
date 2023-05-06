import requests
from bs4 import BeautifulSoup
from math import ceil


class Fetcher:
    def __init__(self, market):
        #TODO : PARSE MARKET
        self.market = market
        self.urlbase = f'https://www.zillow.com/{market}'

    def get_listings(self):
        for id in self._get_listings_zpids():
            self._get_listing_details(id)

    def _get_zpids_pp(self, response):
        anchor = response.find("searchListZpids")
        start = response.find("[", anchor)
        end = response.find("]", anchor)

        zpids = response[start+1:end].split(", ")

        return zpids

    def _get_listings_zpids(self):
        response = requests.get(url=f"{self.urlbase}", headers={"User-Agent": "Mozilla/5.0"}).text

        soup = BeautifulSoup(response, 'html.parser')
        # parent = soup.findParent(string="searchListZpids")

        results_count = int(soup.find("span", class_="result-count").contents[0].split()[0])
        page_count = ceil(results_count/40)

        all_zpids = self._get_zpids_pp(response)

        for i in range(2, page_count+1):
            response = requests.get(url=f"{self.urlbase}/{i}_p", headers={"User-Agent": "Mozilla/5.0"}).text
            all_zpids.extend(self._get_zpids_pp(response))

        return all_zpids


    def _get_listing_details(self, zpid):
        response = requests.get(f"https://www.zillow.com/homedetails/x/{zpid}_zpid/",
                                headers={"User-Agent": "Mozilla/5.0"}).text
        soup = BeautifulSoup(response, 'html.parser')

        return soup.find(attrs={"name": "description"})


if __name__ == '__main__':
    fetch = Fetcher("cleveland-heights-oh")
    print(fetch.get_listings())
