from enum import Enum
class ErrorCoreMessage(str, Enum):    
    URL_BASE:str = "http://apps-test.losandes.pe"
    PATH_NIUBIZ_CLIENT:str = 'api/clientes/consulta/antifraude'