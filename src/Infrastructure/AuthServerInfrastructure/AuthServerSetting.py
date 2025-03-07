from datetime import datetime, timedelta
import os
from Domain.Commons.AuthServerContainer import register_vars
from Domain.Messages.InternalCoreMessage import InternalCoreMessage
from dotenv import load_dotenv

class AuthServerSetting:  
    def __init__(self) -> None:
        load_dotenv()
        self.__name:str = InternalCoreMessage.COGNITO_NAME_APPCLIENTE_SYSTEM.value
        self.__host:str = os.getenv('COGNITO_HOST_APPCLIENTE_SYSTEM')
        self.__user:str = os.getenv('COGNITO_USER_APPCLIENTE_SYSTEM')
        self.__passwd:str = os.getenv('COGNITO_PASSWD_APPCLIENTE_SYSTEM')
        self.__scope:str = os.getenv('COGNITO_SCOPE_APPCLIENTE_SYSTEM') 

        if (self.__name == None or self.__name == ""):
            raise KeyError("Variable name to container is empty ...")

        data:dict = {
            "host":self.__host, 
            "user":self.__user, 
            "passwd":self.__passwd,
            "token":"",
            "expire":(datetime.now() - timedelta(days=7)).isoformat(),
            "scope":self.__scope
        }

        register_vars(self.__name,data)

