from Application.Interfaces.IAuthServerCoreApplication import IAuthServerCoreApplication
from Application.Interfaces.IClientNiubizCaseApplication import IClientNiubizCaseApplication
from Application.Interfaces.ILoggerCoreApplication import ILoggerCoreApplication
from Application.Usecases.AuthorizationCase.AuthServerUsecase import AuthServerUsecase
from Application.Usecases.LoggerCase.LogUsecase import LogUsecase
from Application.Usecases.NiubizCase.ClientNiubizCase import ClientNiubizCase
from Domain.Commons.DependencyContainer import register_dependency
from Infrastructure.CoreInfrastructureSetting import CoreInfrastructureSetting

# ********************************************************************************************************          
# * Copyright © 2024 Victor Jhampier Caxi - All rights reserved.   
# * 
# * Info                  : Dependency injection Handler.
# *
# * By                    : Victor Jhampier Caxi Maquera
# * Email/Mobile/Phone    : victorjhampier@gmail.com | 968991*14
# *
# * Creation date         : 20/10/2024
# * 
# **********************************************************************************************************

class CoreApplicationSetting:
    def __init__(self) -> None:

        # add infrastructure
        CoreInfrastructureSetting() 
        
        register_dependency(ILoggerCoreApplication, LogUsecase)        
        register_dependency(IAuthServerCoreApplication, AuthServerUsecase)
        register_dependency(IClientNiubizCaseApplication, ClientNiubizCase)