from database import ConnectionFromPool
import datetime

class DHT:

    @classmethod
    def saveToDatabase(cls,temp,humidity):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with ConnectionFromPool() as cursor:
                cursor.execute('INSERT INTO public.sensor_humidities(temp,humidity,created_at,updated_at,atualizar) VALUES (%s, %s, %s, %s, %s)',(temp,humidity,now,now,'1'))
                
    @classmethod
    def saveToken(cls,token):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with ConnectionFromPool() as cursor:
                cursor.execute('INSERT INTO public.sensor_auth(token,created_at,updated_at) VALUES (%s, %s, %s)',(token,now,now))

    @classmethod
    def loadAllToken(cls):
        with ConnectionFromPool() as cursor:
                cursor.execute('SELECT * FROM public.sensor_auth')
                data = cursor.fetchone()
                return data

    @classmethod
    def deleteAllData(cls):
        with ConnectionFromPool() as cursor:
                cursor.execute('DELETE FROM public.sensor_humidities')

    @classmethod
    def deleteDataById(cls,id):
        with ConnectionFromPool() as cursor:
                cursor.execute('DELETE FROM public.sensor_humidities WHERE id =%s',(id,))
                               
    @classmethod
    def resetarSequence(cls):
        with ConnectionFromPool() as cursor:
                cursor.execute('ALTER SEQUENCE public.sensor_humidities_id_seq RESTART with 1')

    @classmethod
    def updateToken(cls,id,token):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with ConnectionFromPool() as cursor:
            cursor.execute('UPDATE public.sensor_auth SET updated_at = %s, token = %s WHERE id =%s',(now,token,id))

    @classmethod
    def loadAllFromDatabase(cls):
        with ConnectionFromPool() as cursor:
                cursor.execute('SELECT * FROM public.sensor_humidities order by id asc LIMIT 100')
                data = cursor.fetchall()
                return data
 
    @classmethod
    def updateToDatabase(cls,id,temp,humidity,atualizar):
        now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with ConnectionFromPool() as cursor:
            cursor.execute('UPDATE public.sensor_humidities SET temp = %s, humidity = %s,atualizar =%s ,updated_at = %s WHERE id =%s',(temp,humidity,atualizar,now,id))
            
    @classmethod
    def updateCursor(cls,primarykey,atualizar):
        with ConnectionFromPool() as cursor:
            cursor.execute('UPDATE public.sensor_humidities SET atualizar = %s WHERE id =%s',(atualizar,primarykey))

    @classmethod
    def checkCount(cls):
        with ConnectionFromPool() as cursor:
            cursor.execute("SELECT COUNT(*) from public.sensor_humidities")
            data = cursor.fetchone()
            return int(data[0])

    @classmethod
    def tamanhoArray(cls):
        with ConnectionFromPool() as cursor:
            cursor.execute("SELECT COUNT(*) from public.sensor_humidities")
            data = cursor.fetchall()
            return data
            
    @classmethod
    def findByCursor(cls):
        with ConnectionFromPool() as cursor:
            cursor.execute("SELECT id FROM public.sensor_humidities WHERE atualizar = '1'")
            data = cursor.fetchone()
            return int(data[0])
