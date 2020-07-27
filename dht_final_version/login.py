from database import Database
from dht import DHT
import tracking_client as trk
import datetime
import requests as req
import time
import json as gson

# Metodo que verifica se o TOKEN passou de 24h
def validandoHora(horaBanco):
    horaAtual = time.mktime(datetime.datetime.now().timetuple())
    horaAntiga = time.mktime(horaBanco.timetuple())
    minutos = (horaAtual - horaAntiga)/60
    print minutos
    if(minutos <= 1440):
        return True
    else:
        return False
    
    
###################CONFIGURACOES INICIAIS####################################################################################
#URL = 'https://ocariot.nutes.uepb.edu.br/v1/'
# URL = 'https://api.ocariot.com.br/v1/'
URL = 'https://api.ocariot.tk/v1'


#INICIALIZANDO BANCO DE DADOS
Database.initialise(database="development_sensores",user="postgres",password="postgres",host = "localhost")

#URL SERVIDOR ONDE SERA COLETADO AS INFORMACOES
api = trk.TrankingAPI(URL)  #Instanciando o objeto

#USUARIO E SENHA DA RASPBERRY PI
usuario = 'APPBR02'  
senha =   'APPBR02!@#'

#############################################################################################################################

try:
    print 'Tentando conectar ao servidor'
    request = req.get(URL,verify=False)
    print 'Servidor conectado com sucesso!'
    if(validandoHora(DHT.loadAllToken()[3])):
        print 'Nao precisa atualizar o token'
    else:
        response=api.post_auth(usuario,senha)
        if(response.status_code==200):
            novo_token = gson.loads(response.text)["access_token"]
            print novo_token
            print 'atualizando token'
            id_auth = DHT.loadAllToken()[0]
            print id_auth;
            DHT.updateToken(id_auth,novo_token)
        if(response.status_code==401):
            print 'USUARIO INVALIDO'
        if(response.status_code==404):
            print 'URL NÂO ENCONTRADA'

except req.exceptions.HTTPError as errh:
    print errh
except req.exceptions.ConnectionError as errc:
    print errc
except req.exceptions.ConnectionTimeout as errt:
    print errt
except req.exceptions.RequestException as err:
    print err


