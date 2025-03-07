from enum import Enum
class ClaPagosSetting(str, Enum):    
    URL_BASE:str = "http://apps-test.losandes.pe"
    PATH_NIUBIZ_CLIENT:str = 'api/clientes/consulta/antifraude'