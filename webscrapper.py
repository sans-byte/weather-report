import pandas as pd #this is for converting data into neat and clean tables threw dictionary and also can save file as csv file
from bs4 import BeautifulSoup  # this is for scrappig data from the website  
import requests  #this is for making request to a website for url and other

url = requests.get("https://mausam.imd.gov.in/")
soup = BeautifulSoup(url.content,"html.parser")
# print(soup)


#list all the names and temprature of the places
#make a table using pandas
#put them into a csv file

# link_tags = soup.find_all("a")
# print(*link_tags ,sep="\n")



names_of_places = soup.find_all(class_="capital")
places_names =[names_of_places.find("h3").get_text() for names_of_places in names_of_places]
temperature =[names_of_places.find(class_="now").get_text() for names_of_places in names_of_places]
wind_speed =[names_of_places.find(class_= "wind").get_text() for names_of_places in names_of_places]
maximum =[names_of_places.find(class_="max").get_text() for names_of_places in names_of_places]

weather_report = pd.DataFrame(
    {
        "capitals" : places_names,
        "temperature" : temperature,
        "wind speed" : wind_speed,
        "maximum" : maximum,
    })

print(weather_report)
weather_report.to_csv(r"C:\Users\91881\Documents\report.csv") #set path depending upon your conveniance
