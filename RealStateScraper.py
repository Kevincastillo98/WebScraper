import re
import requests
import pandas as pd
from bs4 import  BeautifulSoup

def Peticion(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    respuesta = requests.get(url,headers=headers)
    Soup = BeautifulSoup(respuesta.content,'html.parser')
    
    ContenedorGeneral = Soup.find_all("div",class_="posting-card super-highlighted")
    
    NumeroImagenes = Soup.find_all("span",class_="ftag-text photoNumber")
    TituloCabezara = Soup.find_all("h2", class_="posting-title")
    DireccionCabezara = Soup.find_all("span",class_="posting-location")
    ListaCaracteristicas = Soup.find_all("ul",class_="main-features")
    Costo = Soup.find_all("span",class_="first-price")
    Descripcion = Soup.find_all("div", class_="posting-description")
    FechaVenta = Soup.find_all("ul",class_="posting-features")
    


print(Peticion('https://www.inmuebles24.com/casas-en-venta.html'))
