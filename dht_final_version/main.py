from database import Database
from dht import DHT
import Adafruit_DHT
import RPi.GPIO as GPIO
import tracking_client as trk
import datetime
import requests as req


def salvando_dados_local(umidade,temperatura):
    print 'Salvando dados localmente'
    DHT.saveToDatabase(temperatura,umidade)
    print "Dados salvos com sucesso!"
    

def verificando_se_tem_dados_local(token,ID_INSTITUTION):
    
    while(DHT.tamanhoArray()[0][0] > 0):
        print "Coletando dados do banco"
        alldata = DHT.loadAllFromDatabase()
        json_array = api.montar_array(alldata)
        result = api.post_dado_formatado(token,json_array,ID_INSTITUTION)
        if (result == 201):
            print "201 Dados armazenados localmente foram enviados com sucesso"
        if (result == 409):
            print "dado já foi enviado,nao e possivel salva-lo"
        if (result == 207):
            print "Status:207, Dados armazenados localmente foram enviados com sucesso"
            for dados in alldata:
                DHT.deleteDataById(dados[0])
                print "Dado: "+str(dados[0])+ " deletado com sucesso!"
    else:
        print "Banco de dados esta vazio!"


    if(DHT.tamanhoArray()[0][0] == 0):
        DHT.resetarSequence()
        print "Resetando Sequencia do PGSQL"

   

            
###################CONFIGURACOES INICIAIS####################################################################################
#URL = 'https://ocariot.nutes.uepb.edu.br/v1/'
# URL = 'https://api.ocariot.com.br/v1/'
URL = 'https://api.ocariot.tk/v1'
ID_INSTITUTION = '5ef4d632d127b000b0422b7d'

#INICIALIZANDO BANCO DE DADOS
Database.initialise(database="development_sensores",user="postgres",password="postgres",host = "localhost")

#URL SERVIDOR ONDE SERA COLETADO AS INFORMACOES
api = trk.TrankingAPI(URL)  #Instanciando o objeto


# Define o tipo e GPIO do sensor
sensor = Adafruit_DHT.DHT22
GPIO.setmode(GPIO.BOARD)

# Define a GPIO conectada ao pino de dados do sensor
pino_sensor = 25

########################################################################################################

# Efetua a leitura do sensor
umidade, temperatura = Adafruit_DHT.read_retry(sensor, pino_sensor)
umidade = round(umidade, 2)
temperatura = round(temperatura, 2)
timestamp = str(datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ"))
print umidade
print temperatura
try:
    print 'Tentando conectar ao servidor'
    request = req.get(URL,verify=False)
    print 'Servidor conectado com sucesso!'
    token = DHT.loadAllToken()[1]
    # print 'Verificando se tem dados local para enviar'
    # verificando_se_tem_dados_local(token,ID_INSTITUTION)
    print 'Atualizando temperatura e umidade'
    print api.post_environments(token, umidade, temperatura, timestamp,ID_INSTITUTION)

except req.exceptions.HTTPError as errh:
    salvando_dados_local(umidade,temperatura)
except req.exceptions.ConnectionError as errc:
    salvando_dados_local(umidade,temperatura)
except req.exceptions.ConnectionTimeout as errt:
    salvando_dados_local(umidade,temperatura)
except req.exceptions.RequestException as err:
    salvando_dados_local(umidade,temperatura)