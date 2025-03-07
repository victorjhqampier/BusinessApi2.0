from Domain.Commons.DependencyContainer import register_dependency
from Domain.Interfaces.IFakeApiInfrastructure import IFakeApiInfrastructure
from Domain.Interfaces.IHttpClientInfrastructure import IHttpClientInfrastructure
from Infrastructure.ExampleFakeApiInfra.Queries.FakeApiCommand import FakeApiCommand
from Infrastructure.HttpClientInfrastrucuture.HttpClientInfrastructure import HttpClientInfrastructure

# ********************************************************************************************************          
# * Copyright © 2025 Arify Labs - All rights reserved.   
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
        # register_dependency(ILoggerInfraestructure, LoggerCommand)
        register_dependency(IHttpClientInfrastructure, HttpClientInfrastructure)
        register_dependency(IFakeApiInfrastructure, FakeApiCommand)
        # register_dependency(IAuthServerInfrastructure, CognitoAutorizationCognito)