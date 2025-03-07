from typing import Any, List, Optional
# ********************************************************************************************************          
# * Copyright © 2025 Arify Labs- All rights reserved.   
# * 
# * Info                  : Backend.
# *
# * By                    : Victor Jhampier Caxi Maquera
# * Email/Mobile/Phone    : -| victorjhampier@gmail.com | 968991*14
# *
# * Creation date         : 18/08/2024
# * 
# **********************************************************************************************************

class ArifyValidationRuleResponse:
    def __init__(self, field_name: str, error_code: str, message: str):
        self.field_name = field_name
        self.error_code = error_code
        self.message = message

class FieldValidator:
    def __init__(self, field_name: str, value: Any):
        self.__field_name = field_name
        self.__obj_field = value
        self.__broken_rules: List[ArifyValidationRuleResponse] = []
        self.__current_rule: Optional[ArifyValidationRuleResponse] = None

    def __append_rule(self, error_code: str, message: str):
        self.__current_rule = ArifyValidationRuleResponse(self.__field_name, error_code, message)
        self.__broken_rules.append(self.__current_rule)

    def not_null(self):
        if self.__obj_field is None:
            self.__append_rule("not_null", "No puede ser nulo.")
        return self

    def not_empty(self):
        if isinstance(self.__obj_field, str) and self.__obj_field.strip() == "":
            self.__append_rule("not_empty", "No puede estar vacío.")
        return self

    def min_length(self, min_len: int):
        if isinstance(self.__obj_field, str) and len(self.__obj_field) < min_len:
            self.__append_rule("min_length", f"Debe tener al menos {min_len} caracteres.")
        return self

    def max_length(self, max_len: int):
        if isinstance(self.__obj_field, str) and len(self.__obj_field) > max_len:
            self.__append_rule("max_length", f"No puede tener más de {max_len} caracteres.")
        return self

    def is_numeric(self):
        if not isinstance(self.__obj_field, str) or not self.__obj_field.isdigit():
            self.__append_rule("is_numeric", "Debe ser una cadena que contenga solo números.")
        return self

    def with_message(self, custom_message: str):
        if self.__current_rule:
            self.__current_rule.message = custom_message
        return self

    def with_code(self, custom_code: str):
        if self.__current_rule:
            self.__current_rule.error_code = custom_code
        return self
    
    def where(self, condition: bool):
        if not condition and self.__current_rule:
            self.__broken_rules.remove(self.__current_rule)
            self.__current_rule = None
        return self

    def validate(self) -> List[ArifyValidationRuleResponse]:
        return self.__broken_rules