import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import re
#Step-1: Web Scraping
url="http://books.toscrape.com/"
try:
    response=requests.get(url)
    response.encoding='utf-8'  #Fix encoding issue
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error fetching data: ",e)
    exit()
soup=BeautifulSoup(response.text, features="html.parser")
books=soup.find_all(name="article",class_="product_pod")
names=[]
prices=[]
for book in books:
    name=book.h3.a["title"]

    #Get raw price text
    price_text=book.find("p",class_="price_color").text

    #Extract numeric value using regex
    price = float(re.findall(r"\d+\.\d+", price_text)[0])
    names.append(name)
    prices.append(price)
#Step2: Store Data in Table
    df=pd.DataFrame({
        "Book Name":names,
        "Price":prices
        })

print("\n table Data: \n")
print(df)
print(df.shape)
print(df.head())
#Save to CSV
df.to_csv(path_or_buf="books_data.csv",index=False)
print("\n CSV file 'books_data.csv' created successfully")
plt.figure()
plt.bar(names[:10],prices[:10])
plt.xticks(rotation=90)
plt.xlabel("Book Names")
plt.ylabel("Price")
plt.title("Book Prices (Top 10)")
plt.tight_layout()
plt.show()
