import requests
from bs4 import BeautifulSoup
import csv

URL="https://www.airlinequality.com/airline-reviews/british-airways/?sortby=post_date%3ADesc&pagesize=3068"
page=requests.get(URL)
soup=BeautifulSoup(page.content,"html.parser")
results=soup.find_all("div",class_="body")
data=[]
i=0

for r in results:
    table=r.find_all("table",class_="review-ratings")
    for tr in table:
        td=tr.find_all("td",class_="review-value")
        list=[]
        for x in td:
            list.append(x.text)
        data.append(list)
        i+=1
i=0

for item in data:
    list=["","","","",""]
    for x in item:
        if x[0]=="A" and x[1].isdigit():
            list[0]=x
        elif "Leisure" in x:
            list[1]=x
        elif "Class" in x:
            list[2]=x
        elif "202" in x or "201" in x:
            list[3]=x
        elif x=="yes" or x=="no":
            list[4]=x
        else:
            pass
    data[i]=list
    i+=1
    
f=open("customer_reviews.csv","w",newline='')
csvwriter=csv.writer(f)
csvwriter.writerow(["Aircraft","Traveller_type","Seat_type","Date_flown","Recommended"])
csvwriter.writerows(data)
f.close()
print("Dataset has been generated")
