from bs4 import BeautifulSoup as BS
import requests
import time

start_time = time.time()



page = requests.get("http://quotes.toscrape.com/page/100")
soup = BS(page.text, "html.parser")
quote = soup.find("div", attrs={"class": "col-md-8"})

print(quote.text)

range = range(1, 101)
for p in range:
    page = requests.get("http://quotes.toscrape.com/page/" + str(p))
    soup = BS(page.text, "html.parser")
    text = soup.findAll("div", attrs={"class": "col-md-8"})
    text = str(text)
    textcheck = text.find("No quotes found!")
    quotes = soup.findAll("span", attrs={"class": "text"})
    authors = soup.findAll("small", attrs={"class": "author"})

    if textcheck != -1:
        print("No more information beyond page " + str(p-1))
        end_time = time.time()
        elapsed_time = end_time - start_time
        print("The stopwatch ran for {} seconds".format(elapsed_time))
        quit()
    else:
        for quote, author in zip(quotes, authors):
            print(quote.text + " - " + author.text)




