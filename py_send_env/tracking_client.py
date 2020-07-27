import requests as req

# Todos os campos a seguir sao obrigatorios
env = dict.fromkeys(['timestamp', 'temperature', 'humidity', 'location'])
location = dict.fromkeys(['school', 'room', 'country', 'city'])

class TrankingAPI:

    resources = {'env':'environments', 'act':'activities', 'sl':'sleep'}
    
    def __init__(self, url):
        self.url = url

    def post_envdata(self, timestamp, temperature, humidity, location):
        """ post_envdata(timestamp: str, temperature: float, humidity: float, location: dict) """

        env_data = env
        env_data['timestamp'] = timestamp
        env_data['temperature'] = temperature
        env_data['humidity'] = humidity
        env_data['location'] = location
        
        url = self.url + self.resources['env']
        resp = req.post(url, json=env_data)
        return resp.text
    
    def get_envdata(self):
        url = self.url + self.resources['env']
        return req.get(url).text