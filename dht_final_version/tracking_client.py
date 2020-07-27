import requests as req
import json as gson

location = dict.fromkeys(['local', 'room', 'latitude', 'longitude'])
login = dict.fromkeys(['username', 'password'])
headers = dict.fromkeys(['accept', 'Content-Type','Authorization'])

class TrankingAPI:

    resources = {'inst':'institutions', 'act':'activities', 'sl':'sleep', 'auth':'auth'} #Metodos
    
    def __init__(self, url):
        self.url = url


    def post_auth(self, username, password):
        headers ={'accept':'application/json','Content-Type':'application/json'}  
        
        login['username'] = username
        login['password'] = password
        
        url = self.url + self.resources['auth']
        print url
        
        response = req.post(url , headers=headers, json=login, verify=False)
        return response
    
 #   def get_environments(self,token):
 #       authorization = 'Bearer ' + token
 #
 #       headers['accept'] = 'application/json'
 #       headers['Content-Type'] = 'application/json'
 #       headers['Authorization'] = authorization
 #
 #       
 #       url = self.url + self.resources['env']
 #        
 #      return req.get(url, headers=headers,verify=False).text

          
    def montar_array(self,alldata):
        my_list = []
        
        for dado in alldata :
            timestamp = str(dado[4].strftime("%Y-%m-%dT%H:%M:%SZ"))
            
            f=open('/home/pi/Desktop/local-instalacao.txt')
            lines=f.readlines()
            
            local = lines[0].rstrip()
            room = lines[1].rstrip()
            latitude = lines[2].rstrip()
            longitude = lines[3].rstrip()

            data = {"location":{"local":local,"room": room,"latitude":latitude,"longitude":longitude},
                    "measurements":[{"type":"temperature","value":dado[1],"unit":"C"},
                                    {"type":"humidity","value":dado[2],"unit":"%"},
                                    {"type":"pm1","value":0.0,"unit":"Um"},
                                    {"type":"pm2.5","value":0.0,"unit":"Um"},
                                    {"type":"pm10","value":0.0,"unit":"Um"}],
                     "climatized":True,
                     "timestamp": timestamp}
            

            my_list.append(data)
        
        return my_list



    def post_dado_formatado(self,token,json_array,ID_INSTITUTION):
        
        authorization = 'Bearer ' + token
        
        headers['accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = authorization
     
        url = self.url + 'institutions/'+ID_INSTITUTION+'/environments'
        print "Printando resposta"
        response = req.post(url , headers=headers, data=gson.dumps(json_array), verify=False)
        return response.status_code
    
        
    def post_environments(self,token ,umidade, temperatura, timestamp,ID_INSTITUTION):
        my_list = []
        
        f=open('/home/pi/Desktop/local-instalacao.txt')
        lines=f.readlines()
        
        local = lines[0].rstrip()
        room = lines[1].rstrip()
        latitude = lines[2].rstrip()
        longitude = lines[3].rstrip()
        
        authorization = 'Bearer ' + token
        
        headers['accept'] = 'application/json'
        headers['Content-Type'] = 'application/json'
        headers['Authorization'] = authorization

        data = {"location":{"local":local,"room": room,"latitude":latitude,"longitude":longitude},
                "measurements":[{"type":"temperature","value":temperatura,"unit":"C"},
                                {"type":"humidity","value":umidade,"unit":"%"},
                                {"type":"pm1","value":0.0,"unit":"Um"},
                                {"type":"pm2.5","value":0.0,"unit":"Um"},
                                {"type":"pm10","value":0.0,"unit":"Um"}],
                 "climatized":True,
                 "timestamp": timestamp}

        my_list.append(data)
        
        
        url = self.url + 'institutions/'+ID_INSTITUTION+'/environments'
    
        response = req.post(url , headers=headers, data=gson.dumps(my_list), verify=False)
        
        return response.status_code

    def respose_status_code(response):
        if response.status_code == 201:
            return 'Ambiente Salvo com sucesso'
        elif response.status_code == 401:
            return 'Autenticacao falhou para uma credencial invalida'
