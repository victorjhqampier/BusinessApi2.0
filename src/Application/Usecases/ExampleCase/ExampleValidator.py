from Application.Adpaters.Bians.FieldErrorBianCoreAdapter import FieldErrorBianCoreAdapter
from Application.Adpaters.ExampleAdapters.ExampleRequestAdaper import ExampleRequestAdaper, ExampleRequestAdaperValidator
from Application.Adpaters.FieldErrorCoreAdapter import FieldErrorCoreAdapter
from Domain.Commons.Validators.ArifyValidatorBuilder import ArifyValidationRuleResponse


class ExampleValidator:
    
    @staticmethod
    def validate_example_request(request: ExampleRequestAdaper) -> list[FieldErrorBianCoreAdapter]:

        arrResult: list[ArifyValidationRuleResponse] = ExampleRequestAdaperValidator(request).validate()
        errors = []        
        for rule in arrResult:
            field_error = FieldErrorBianCoreAdapter(
                status_code=rule.error_code,
                message=rule.message + ", in " + rule.field_name
            )
            errors.append(field_error)

        return errors