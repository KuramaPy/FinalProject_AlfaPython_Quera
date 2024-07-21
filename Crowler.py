import requests
import pandas as pd
import time
from bs4 import BeautifulSoup


Data = { "Brand":["lenovo","orange","asus","asus",'acer','dell','dell','lenovo','acer','msi','lenovo','hp','lenovo','dell','hp','microsoft','orange','quera','quera','orange'],
        "Model":["IdeaPadSlim3-C","m3","VivoBookX1502ZA","VivobookGOL1504FA","Aspire3","Inspiron15",'Latitude3410','L340','T572','R80','IdeaPadFlex5','X2pro','IdeaPad1','Vostro3510','ZBOOK15U-G6','SurfaceBook1','a11','ab102','c17','b13'],
        "Class":["both","neither","both","torob","both","torob",'both','neither','neither','neither','neither','torob','both','torob','torob','torob','neither','neither','neither','neither']
        }


def Technolife(url:str):
    #url = "https://www.technolife.ir/product/list/164_163_130/%D8%AA%D9%85%D8%A7%D9%85%DB%8C-%DA%A9%D8%A7%D9%85%D9%BE%DB%8C%D9%88%D8%AA%D8%B1%D9%87%D8%A7-%D9%88-%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%87%D8%A7?only_available=true&manufacturer_id=19&pto=20000000&pfrom=0"
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")

    sections = soup.find_all("section",class_="relative w-full rounded-[10px] bg-white pt-[52px] xl:max-w-[32%] 2xl:w-[24%] 3xl:w-[19.2%] border shadow-[0px_1px_4px_rgba(0,0,0,0.08)]")

    names=[]
    prices=[]
    for section in sections:
        name = section.find("h2",class_="yekanbakh-en line-clamp-3 h-[75px] overflow-hidden text-sm font-medium leading-6.5 -tracking-0.5 text-gray-800")
        price = section.find("p",class_="text-[22px] font-semiBold leading-5 text-gray-800")
        
        for word in Data['Model']:
            if word in name.text:
                names.append(word)
                try :
                    prices.append(price.text)
                except:
                    prices.append(section.find("p",class_="text-[22px] font-semiBold leading-5 text-red-600").text)
            
    data = {"name":names,"price":prices}
    dataframe= pd.DataFrame(data)
    return dataframe

def Torob(url:str):
    #url= "https://torob.com/browse/99/%D9%84%D9%BE-%D8%AA%D8%A7%D9%BE-%D9%88-%D9%86%D9%88%D8%AA-%D8%A8%D9%88%DA%A9-laptop/b/29/asus-%D8%A7%DB%8C%D8%B3%D9%88%D8%B3/?price__gt=10000000&price__lt=20000000&stock_status=new&available=true"
    response = requests.get(url)
    soup = BeautifulSoup(response.text,"html.parser")

    names_html = soup.find_all("h2",class_="jsx-9e6201846c11ef54 product-name")
    

    names=[]
    prices=[]
    for name in names_html:
        for word in Data["Model"]:
            if word in name.text:
                names.append(word)
                
                prices.append(name.parent.find("div",class_="jsx-9e6201846c11ef54 product-price-text").text)

    data = {"name":names,"price":prices}
    dataframe=pd.DataFrame(data)

    return dataframe
