import requests
from bs4 import BeautifulSoup
import pandas

url = requests.get("https://superloop.com/consumer/home-broadband/nbn.html")
soup = BeautifulSoup(url.content, "html.parser")

table = soup.find("section", class_="pb-4")

data = []

# headers
column1 = table.find_all("h1", class_="m-0")[0].text + "\n" + table.find_all("div", class_="plan-header")[0].find_all("p", class_="mb-0")[0].text
column2 = table.find_all("h1", class_="m-0")[1].text + "\n" + table.find_all("div", class_="plan-header")[1].find_all("p", class_="mb-0")[0].text

# row titles
row1 = table.find_all("h1", class_="mb-0")[0].text
row2 = table.find_all("h1", class_="mb-0")[1].text

# content
g_data = table.find_all("div", class_="inset-padding")
plans = g_data[0].find_all("div", class_="plan-price")

plans1 = {}
plans1[""] = g_data[0].find_all("h1", class_="mb-0")[0].text
plans1[column1] = plans[2].find_all("h1", class_="mb-0")[1].text + "\n" + plans[2].find_all("h5", class_="mt-0")[0].text + "\n" + plans[2].find_all("p", class_="mb-0")[1].text.replace("3", "")
plans1[column2] = plans[4].find_all("h1", class_="mb-0")[1].text + "\n" + plans[4].find_all("h5", class_="mt-0")[0].text + "\n" + plans[4].find_all("p", class_="mb-0")[1].text
data.append(plans1)

plans2 = {}
plans2[""] = g_data[0].find_all("h1", class_="mb-0")[1].text
plans2[column1] = plans[3].find_all("h1", class_="mb-0")[1].text + "\n" + plans[3].find_all("p", class_="mb-0")[1].text.replace("3", "")
plans2[column2] = plans[5].find_all("h1", class_="mb-0")[1].text + "\n" + plans[5].find_all("p", class_="mb-0")[1].text
data.append(plans2)

df = pandas.DataFrame(data)
df.to_csv("superloop_broadband_NBN.csv")
