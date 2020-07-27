import http.client
import json
import ssl

certificate_file = 'certificate.pem'


certificate_secret = 'private.key'
host = 'iot.ocariot.tk'



request_url='/v1/institutions/5ef4d632d127b000b0422b7d/environments'
request_headers = {
  'Content-Type': 'application/json'
}
request_body_dict = [
  {
    "location": {
      "local": "indoor",
      "room": "Bloco H sala 01",
      "latitude": "-7.2100766",
      "longitude": "-35.9175756"
    },
    "measurements": [
      {
        "type": "temperature",
        "value": 35.6,
        "unit": "°C"
      },
    ],
    "climatized": True,
    "timestamp": "2018-11-19T14:40:00Z"
  }
]

print('teste1')
context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
context.load_verify_locations('certificate.pem')
print('teste2')
context.load_cert_chain('certificate.pem', 'private.key')
print('teste3')
connection = http.client.HTTPSConnection(host, 443, context=context)
print('teste4')
connection.request("POST", url=request_url, headers=request_headers, body=json.dumps(request_body_dict))
print('teste5')
response = connection.getresponse()
print(response.status, response.reason)
data = response.read()
print(data)

connection.close()
