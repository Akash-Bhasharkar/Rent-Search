from bs4 import BeautifulSoup 
import requests

#Link of the Rental site
PAGE_LINK = "https://www.zillow.com/san-francisco-ca/rentals/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22u" 
"sersSearchTerm%22%3A%22San%20Francisco%2C%20CA%22%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56811751527907%2C%22east%22%3A-122"
".29854048472093%2C%22south%22%3A37.73932632963956%2C%22north%22%3A37.81123909008061%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22min%22%3A0%2C%22max%22%3A872627%7D%2C%22mp%22%3A%7B%22min%22%3A0%2C%22max%22%3A3000%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"

class Data :

    def __init__(self) :
        
        self.headers = {
                    "User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36",
                    "Accept-Language" : "en-US,en;q=0.9"
        }

        self.response = requests.get(url = PAGE_LINK, headers = self.headers)
        content = self.response.text
        
        self.soup = BeautifulSoup(content, "html.parser")
        
        
    def rent_price(self) : 
        
        self.rent_price_text = self.soup.select("li div .list-card-price")
        self.rent_price_list = []
        for rent in self.rent_price_text :
            if "+" in rent.text :
                self.rent_price_list.append(rent.text.split("+")[0])
            if "/" in rent.text :
                self.rent_price_list.append(rent.text.split("/")[0])
        return self.rent_price_list


    def rent_address(self) :

        self.rent_addr_text = self.soup.select("li a .list-card-addr")
        self.rent_addr = [addr.getText() for addr in self.rent_addr_text]
        return self.rent_addr

    
    def rent_link(self) :

        self.rent_link_text = self.soup.select("li .list-card-info a")
        self.rent_link_list = []
        for link in self.rent_link_text :
            href = link["href"]
            if "http" in href : 
                self.rent_link_list.append(href)
            else :
                self.rent_link_list.append(f"https://www.zillow.com{href}")
        return self.rent_link_list
    
        
    
