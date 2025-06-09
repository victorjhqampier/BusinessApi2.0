from Application.Interfaces.IAuthServerCoreApplication import IAuthServerCoreApplication
from Application.Interfaces.IClientNiubizCaseApplication import IClientNiubizCaseApplication
from Application.Interfaces.ICustomerApplication import ICustomerApplication
from Application.Interfaces.ICustomerWorkerApplication import ICustomerWorkerApplication
from Application.Interfaces.ILoggerCoreApplication import ILoggerCoreApplication
from Application.Usecases.CustomerCase.CustomerCase import CustomerCase
from Application.Usecases.CustomerWorkerCase.CustomerWorkerCase import CustomerWorkerCase
from Application.Usecases.InternalCoreCase.AuthServerUsecase import AuthServerUsecase
from Application.Usecases.InternalCoreCase.LogUsecase import LogUsecase
from Application.Usecases.NiubizCase.ClientNiubizCase import ClientNiubizCase
from Domain.Commons.CoreServices import CoreServices as Services
from Infrastructure.ExampleFakeApiInfra.ExampleFakeApiSetting import ExampleFakeApiSetting
from Infrastructure.HttpClientInfrastrucuture.HttpClientSetting import HttpClientSetting
from Infrastructure.KafkaInfrastructure.KafkaInfrastructureSetting import KafkaInfrastructureSetting
from Infrastructure.KafkaProducerInfrastructure.KafkaProducerSetting import KafkaProducerSetting
from Infrastructure.MongoClientInfrastructure.MongoInfrastructureSetting import MongoInfrastructureSetting

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

class CoreApplicationSetting:
    def __init__(self) -> None:
        self.__add_infrastructure()
        self.__add_dependencies()

    def __add_infrastructure(self) -> None:
        HttpClientSetting.add_services()
        ExampleFakeApiSetting.add_services()
        KafkaProducerSetting.add_services()
        # CoreInfrastructureSetting()      
        KafkaInfrastructureSetting.add_services()
        MongoInfrastructureSetting.add_services()  
        
    def __add_dependencies(self) -> None:
        Services.add_singleton_dependency(ILoggerCoreApplication, LogUsecase)        
        Services.add_singleton_dependency(IAuthServerCoreApplication, AuthServerUsecase)
        Services.add_singleton_dependency(IClientNiubizCaseApplication, ClientNiubizCase)
        Services.add_singleton_dependency(ICustomerApplication, CustomerCase)
        Services.add_singleton_dependency(ICustomerWorkerApplication, CustomerWorkerCase)
    
    # ********************************************************************************************************          
    # * Please not use or added sigleton instance in this layer, only in the infrastructure layer.
    # ********************************************************************************************************          
