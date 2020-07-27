import requests

class RequestAPI:
    @classmethod
    def changeVacancyStatus(cls,vacancyID,newStatus):
        url = "http://localhost:8000/api/vacancies/{}/".format(vacancyID)
        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"current_status\"\r\n\r\n{}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--".format(newStatus)
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Cache-Control': "no-cache",
            'Authorization': "Token dda6eb5d999cf4f144b2698841620e9cf86b0e1e"
        }
        response = requests.request("PUT", url, data=payload, headers=headers)
        print(response.text)
        return (response.text)
    @classmethod
    def getVacanciesbyCameraId(cls,cameraID):
        url = "http://localhost:8000/api/vacancies/"
        querystring = {"camera":cameraID}
        headers = {
            'Cache-Control': "no-cache",
            'Authorization': "Token dda6eb5d999cf4f144b2698841620e9cf86b0e1e"
        }
        response = requests.request("GET", url, headers=headers, params=querystring)
        return(response.text)

    @classmethod
    def createVacancy(cls,cameraID,x1,y1,x2,y2):

        url = "http://localhost:8000/api/vacancies/"

        payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"camera\"\r\n\r\n{}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"x1\"\r\n\r\n{}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"y1\"\r\n\r\n{}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"x2\"\r\n\r\n{}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"y2\"\r\n\r\n{}\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"current_status\"\r\n\r\nFalse\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--".format(cameraID,x1,y1,x2,y2)
        headers = {
            'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
            'Authorization': "Token dda6eb5d999cf4f144b2698841620e9cf86b0e1e",
            'Cache-Control': "no-cache",
            }

        response = requests.request("POST", url, data=payload, headers=headers)

        print(response.text)

    @classmethod
    def viewallVacancy(cls):
        url = "http://localhost:8000/api/vacancies/"

        headers = {
            'Authorization': "Token dda6eb5d999cf4f144b2698841620e9cf86b0e1e",
            'Cache-Control': "no-cache",
            }

        response = requests.request("GET", url, headers=headers)

        print(response.text)
    @classmethod
    def selectCamera(cls,cameraID):
        pass

