# 1. Business API - BIAN Capability - API LED  

A Go-based web server designed to deliver lightweight and efficient endpoints for various applications. Developed with extensibility and scalability in mind, this project utilizes FastAPI.

---

## 1.1. Copyright

© 2025 Arify Labs

This code is licensed under the **GNU Affero General Public License (AGPL), version 3.0 or later**.  
You are free to use, modify, and distribute this code, but any changes or improvements must be contributed back to the original project and shared under the same license.

For more details about the license, visit:  
[https://www.gnu.org/licenses/agpl-3.0.html](https://www.gnu.org/licenses/agpl-3.0.html)

---

## 1.2. Features

- Lightweight and modular structure.
- Easily extensible for adding new endpoints.
- Powered by FastAPI
- Built-in support for JSON-based responses.

---

## 1.3. How to Run

1. Run Command - Go to src/
   ```bash
    cd src/
    python -m venv env
    Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser
    env/Scripts/activate.ps1
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    uvicorn Presentation.app:app --reload

2. Or Run
   ```bash
   .\start.ps1

## 1.5. How to use HTTP Client Builder (soon: pip install arify-httpclient)
1. Ejemplo de Uso Básico
   ```python
   import asyncio
   from Infrastructure.HttpClientInfrastrucuture.HttpClientInfrastructure import HttpClientInfrastructure

   async def main():
      # Instanciar el builder con timeout de 15s (por defecto).
      client = HttpClientInfrastructure(timeout=15)

      # Construir una petición GET a "https://jsonplaceholder.typicode.com/todos/1".
      response = await (client
         .http("https://jsonplaceholder.typicode.com")
         .endpoint("todos/1")
         .get()
      )

      print("Status code:", response.StatusCode)
      print("Contenido:", response.Content)

      # Cerrar la conexión cuando no se use más.
      await client.close()

   asyncio.run(main())
2. Realizar una petición GET simple
   ```python
   response = await (
      client
         .http("https://api.example.com")
         .endpoint("users")
         .get()
   )
3. Agregar parámetros y query string
   ```python
   response = await (
      client
         .http("https://api.example.com")
         .endpoint("search")
         .param("sort", "desc")         # Parámetro enviado en "params="
         .query("filter", "active")     # Parámetro de query string "?filter=active"
         .get()
   )
4. Enviar múltiples cabeceras
   ```python
   response = await (
      client
         .http("https://api.example.com")
         .endpoint("batchHeaders")
         .headers({"X-Request-ID": "abc123", "X-Custom-Token": "xyz789"})
         .get()
   )
5. Usar cabeceras personalizadas
   ```python
   response = await (
      client
         .http("https://api.example.com")
         .endpoint("profile")
         .header("X-Client-Version", "1.0.0")
         .header("X-Device", "Desktop")
         .get()
   )
6. Autenticación con Bearer token
   ```python
   response = await (
      client
         .http("https://api.example.com")
         .endpoint("reports")
         .authorization("Bearer", "MiTokenSecreto123")
         .get()
   )
7. Enviar datos en el cuerpo (POST/PUT)
   ```python
   payload = {
      "title": "Nuevo Item",
      "description": "Creando un item via API"
   }

   response = await (
      client
         .http("https://api.example.com")
         .endpoint("items")
         .post(body=payload)
   )
## 1.6. How to use pydantic Validator (soon: pip install arify-validator)
1. Considera un modelo Pydantic sencillo con dos campos
   ```python
   from typing import Optional
   from pydantic import BaseModel

   class UserRequest(BaseModel):
      username: Optional[str] = None
      email: Optional[str] = None

2. Ejemplo de reglas de validación
   ```python
   class UserRequestValidator(ArifyValidator):
    def __init__(self, obj: UserRequest):        
        super().__init__()
        
        # Validación para el campo 'username'
        self.add_rules(
            self.field(obj, obj.username)
                .not_null()
                .not_empty()
                .min_length(5)
                .max_length(20)
                .with_code("U001")
                .with_message("El nombre de usuario debe tener entre 5 y 20 caracteres.")
                .validate()
        )
        
        # Validación para el campo 'email'
        self.add_rules(
            self.field(obj, obj.email)
                .not_null()
                .not_empty()
                .min_length(5)
                .max_length(50)
                .with_code("E001")
                .with_message("El email debe tener entre 5 y 50 caracteres.")
                .validate()
        )
3. Ejemplo de Validador con Grupos de Validación
   ```python
   class UserRequestValidator(ArifyValidator):
    def __init__(self, obj: UserRequest, group: str = "primary"):        
        super().__init__()
        self.obj = obj

        if group == "primary":
            self._build_primary_rules()
        elif group == "secondary":
            self._build_secondary_rules()
        else:
            raise ValueError(f"Grupo de validación desconocido: {group}")

    def _build_primary_rules(self):        
        # Reglas estrictas para 'email'
        self.add_rules(
            self.field(self.obj, self.obj.email)
                .not_null()
                .not_empty()
                .min_length(5)
                .max_length(50)
                .with_code("E001")
                .with_message("El email debe tener entre 5 y 50 caracteres.")
                .validate()
        )

    def _build_secondary_rules(self):
        # Reglas alternativas para 'username'
        self.add_rules(
            self.field(self.obj, self.obj.username)
                .not_null()
                .min_length(3)
                .max_length(30)
                .with_code("U002")
                .with_message("El nombre de usuario debe tener entre 3 y 30 caracteres (validación secundaria).")
                .validate()
        )
   # Constructor alternativo que crea el validador usando las reglas del grupo 'secondary'.
    @classmethod
    def from_secondary(cls, obj: UserRequest) -> "UserRequestValidator":        
        return cls(obj, group="secondary")

4. Cómo Implementar el Validador
   ```python
   class ExampleValidator:
    
    @staticmethod
    def validate_example_request(request: UserRequest) -> list[FieldErrorBianCoreAdapter]:
        # Se crea el validador para el request utilizando las reglas primarias
        arr_result: list[ArifyValidationRuleResponse] = UserRequestValidator(UserRequest).validate()
        
        errors = []
        for rule in arr_result:
            field_error = FieldErrorBianCoreAdapter(
                status_code=rule.error_code,
                message=f"{rule.message}, in {rule.field_name}"
            )
            errors.append(field_error)
    
        return errors
5. Cómo usar el Validador
   ```python
   # Crear una instancia del modelo con algunos datos (pueden ser inválidos)
   example_request = UserRequest(
      username="   ",   # Vacío o solo espacios
      email="Msg1@email.com"
   )

   # Ejecutar la validación
   errors = ExampleValidator.validate_example_request(example_request)

   # Procesar o mostrar los errores de validación
   if errors:
      for error in errors:
         print(f"Error en '{error.field_name}': [{error.status_code}] {error.message}")
   else:
      print("¡Validación exitosa!")