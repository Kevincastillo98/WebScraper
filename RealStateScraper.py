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
    TituloCabecera = Soup.find_all("h2", class_="posting-title")
    DireccionCabezara = Soup.find_all("span",class_="posting-location")
    ListaCaracteristicas = Soup.find_all("ul",class_="main-features")
    Costo = Soup.find_all("span",class_="first-price")
    Descripcion = Soup.find_all("div", class_="posting-description")
    FechaVenta = Soup.find_all("ul",class_="posting-features")
    
    ListaNumeroImagen = []
    ListaTituloCabecera = []
    ListaDireccionCabecera = []
    ListaCosto = []
    ListaFechaVenta = []

    for i in ContenedorGeneral:

        NumeroIm = i.find('span',class_ = "ftag-text photoNumber")
        ListaNumeroImagen.append(NumeroIm.text)

        TituloCab = i.find('h2',class_="posting-title")
        ListaTituloCabecera.append(TituloCab.text)
        
        DireccionCab = i.find("span",class_="posting-location")
        ListaDireccionCabecera.append(DireccionCab)
        
        CostoAux = i.find("span",class_="first-price")
        ListaCosto.append(CostoAux)

    Tabla = pd.DataFrame({"NumeroImagen":ListaNumeroImagen,"TituloCabecera":ListaTituloCabecera,"Direccion":ListaDireccionCabecera,"Costo":ListaCosto})
    return(Tabla)

print(Peticion('https://www.inmuebles24.com/casas-en-venta.html'))
