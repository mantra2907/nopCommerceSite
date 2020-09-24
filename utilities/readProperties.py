import configparser

config= configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")

class ReadConfig():

    @staticmethod
    def getApplicationURl():
        url= config.get('common info','baseURL')
        #url = "https://admin-demo.nopcommerce.com/login"
        return url

    @staticmethod
    def getUseremail():
        username = config.get('common info', 'username')
        #username ="admin@yourstore.com"
        return username

    @staticmethod
    def getPassword():
        passw = config.get('common info', 'password')
        #passw ="admin"
        return passw










