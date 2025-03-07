from Domain.Commons.DependencyContainer import register_dependency
from Domain.Interfaces.IAuthServerInfrastructure import IAuthServerInfrastructure
from Domain.Interfaces.IClientInfrastructure import IClientInfrastructure
from Domain.Interfaces.ILoggerInfraestructure import ILoggerInfraestructure
from Infrastructure.AuthServerInfrastructure.Commands.CognitoAutorizationCognito import CognitoAutorizationCognito
from Infrastructure.ClaPagosInfrastrucuture.Commands.ClientCommand import ClientCommand
from Infrastructure.CoreDatabaseInfrastructure.Commands.LoggerCommand import LoggerCommand

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

class CoreInfrastructureSetting:
    def __init__(self) -> None:        
        register_dependency(ILoggerInfraestructure, LoggerCommand)
        register_dependency(IClientInfrastructure, ClientCommand)
        register_dependency(IAuthServerInfrastructure, CognitoAutorizationCognito)