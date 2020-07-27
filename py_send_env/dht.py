from database import ConnectionFromPool
import datetime


class DHT:

    @classmethod
    def findByObject(cls):
        with ConnectionFromPool() as cursor:
            cursor.execute("SELECT * FROM public.sensor_humidities WHERE atualizar = '1'")
            data = cursor.fetchone()
            return data
                
               
