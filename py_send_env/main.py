import tracking_client as trk
import datetime
from database import Database
from dht import DHT
import urllib2


##print 'Enviando requisicao'
##try:
##    urllib2.urlopen('http://ec2-54-82-98-197.compute-1.amazonaws.com/api/v1/',timeout=2)
##    print 'deu certo'
##except urllib2.URLError as err:
##    print 'deu errado'

Database.initialise(database="development_sensores",user="postgres",password="postgres",host = "localhost")
api = trk.TrankingAPI('https://api.ocariot.com.br/')

#sensor = DHT.findByObject()
##temperatura =  float(sensor[1])
##umidade = float(sensor[2])
##timestamp = str(sensor[4])
##
##
##local = trk.location
##local['school'] = 'Unifor'
##local['room']  = 'M13'
##local['country'] = 'Brasil'
##local['city'] = 'Fortaleza'
##
###timestamp = str(datetime.datetime.today())
###resp = api.post_envdata(timestamp,temperatura,umidade,local)
###print(resp)
##
resp = api.get_envdata()
print(resp)


