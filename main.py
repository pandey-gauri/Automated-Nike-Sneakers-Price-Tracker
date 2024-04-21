import smtplib
import requests
import lxml
from bs4 import BeautifulSoup




url = "https://www.nike.com/in/t/air-max-sc-shoes-gMGhP8/FJ3242-100"
header ={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language":"en-GB,en;q=0.9,hi-IN;q=0.8,hi;q=0.7,en-US;q=0.6"
}

response = requests.get(url,headers=header)

soup=BeautifulSoup(response.content,"lxml")
print(soup.prettify())

price_string = soup.find(string="MRP : ₹ 8 595.00")
price=[]
for char in price_string:
    if char.isdigit():
        price.append(int(char))


string_list = [ str(I) for I in price ]
final_str = "".join(string_list)
money=int(final_str)/100
print(money)



title = soup.find(id="pdp_product_title").get_text().strip()
print(title)

BUY_PRICE = 9000

if money < BUY_PRICE:
    message = f"{title} is now {money}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login("gauri22pandey@gmail.com", "qdanxmcbdeldetac")
        connection.sendmail(
            from_addr="YOUR_EMAIL",
            to_addrs="RECIPIENT_EMAIL",
            msg=f"Subject:Nike Sneakers Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )
