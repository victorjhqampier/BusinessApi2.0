import asyncio
import random
from Application.Adpaters.ExampleAdapters.CreateExampleAdapter import CreateExampleAdapter, CreateExampleResponse
from Application.Adpaters.ExampleAdapters.ExampleRequestAdaper import ExampleRequestAdaper
from Application.Helpers.EasyBianResponseCoreHelper import EasyBianResponseCoreHelper
from Application.Usecases.ExampleCase.ExampleValidator import ExampleValidator
from Domain.Commons.DependencyContainer import get_dependency
from Domain.Entities.ExampleFakeApi.FakeApiEntity import FakeApiEntity
from Domain.Interfaces.IFakeApiInfrastructure import IFakeApiInfrastructure

class ExampleUsecase():
    def __init__(self):
        self.__fake_api:IFakeApiInfrastructure = get_dependency(IFakeApiInfrastructure)
        # self.__easy_response= EasyResponseCoreHelper()
        self.__easy_response= EasyBianResponseCoreHelper()

    # ¡EL RESPONSE del metodo SIEMPRE HEREDA DE ResponseBianCoreAdapter!
    async def get_client_async(self, example_request:ExampleRequestAdaper) -> CreateExampleAdapter:
        arrError = ExampleValidator.validate_example_request(example_request)

        if len(arrError) > 0:
            return self.__easy_response.easy_general_error_respond(CreateExampleAdapter, arrError)
        
        # Ejemplo de llamada en paralelo
        result_1_task = self.__fake_api.get_user_async(random.randint(1, 10))
        result_2_task = self.__fake_api.get_user_async(random.randint(1, 10))
        result_1, result_2  = await asyncio.gather(result_1_task, result_2_task)

        if not result_1 or not result_2 :
            return self.__easy_response.easy_empty_respond(CreateExampleAdapter)
        
        return self.__easy_response.easy_success_respond(CreateExampleAdapter, CreateExampleResponse(
            name=result_1.title,
            age=5,
            email=result_2.title
        ))