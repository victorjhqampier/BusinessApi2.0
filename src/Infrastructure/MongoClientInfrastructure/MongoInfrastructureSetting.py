from Domain.Commons.CoreServices import CoreServices as Services
from Domain.Interfaces.ICustomerInfrastructure import ICustomerInfrastructure
from Domain.Interfaces.ILoggerInfraestructure import ILoggerInfraestructure
from Infrastructure.MongoClientInfrastructure.Commands.CustomerCommand import CustomerCommand
from Infrastructure.MongoClientInfrastructure.Commands.LoggerCommand import LoggerCommand
from Infrastructure.MongoClientInfrastructure.Settings.MongoSetting import MongoSetting

class MongoInfrastructureSetting:
    @classmethod
    def add_services(self) -> None:
        Services.add_singleton_instance(MongoSetting(
                db_type="mongodb",
                user="uDev",
                password="L0s4nd3sD3v21",
                server="10.5.81.16:27017",
                db_name="DB_CoreFlowKata"
            ))

        Services.add_singleton_dependency(ILoggerInfraestructure, LoggerCommand)
        Services.add_singleton_dependency(ICustomerInfrastructure, CustomerCommand)
