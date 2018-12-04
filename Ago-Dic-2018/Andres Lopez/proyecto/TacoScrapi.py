from bs4 import BeautifulSoup
import requests
from BDall import *
class AppPedido(AbstractPedido):
    def get_Pedido(self,url):
        r  = requests.get(url)
        data = r.text
        soup = BeautifulSoup(data,'html5lib')

        name_box = soup.find('h1')
        nombre = name_box.text.strip()
        #print (name)
        i = 0
        for recipe in soup.find_all('div','recipe'):
            if (i == 0):
                ingrediente = recipe.text.strip()
                capa_base = ingrediente
                #print (capa_base)
            elif (i == 1):
                ingrediente = recipe.text.strip()
                salsas = ingrediente
                #print (salsas)
            elif (i == 2):
                ingrediente = recipe.text.strip()
                condimentos = ingrediente
                #print (condimentos)
            elif (i == 3):
                ingrediente = recipe.text.strip()
                sasonadores = ingrediente
                #print (sasonadores)
            elif (i == 4):
                ingrediente = recipe.text.strip()
                capas = ingrediente
                #print (capas)
            i += 1

        return Pedido(nombre,capa_base,salsas,condimentos,sasonadores,capas)
if __name__ == '__main__':
    y=AppPedido()
    twwt = y.get_Pedido('http://taco-randomizer.herokuapp.com/')
    print(twwt.nombre)
