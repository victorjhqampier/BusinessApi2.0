from typing import Type
from functools import wraps

class DependencyContainer:
    _instance = None
    _dependencies = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def register(cls, interface: Type, implementation: Type):
        """Registra una implementación para una interfaz dada."""
        cls._dependencies[interface] = implementation
    
    # @classmethod
    # def register(cls, interface: Type, implementation: Type, *args, **kwargs):
    #     """Registra una implementación para una interfaz dada."""
    #     cls._dependencies[interface] = (implementation, args, kwargs)

    # def resolve(cls, interface: Type):
    #     """Resuelve una implementación para una interfaz dada."""
    #     implementation_data = cls._dependencies.get(interface)
    #     if implementation_data:
    #         implementation, args, kwargs = implementation_data
    #         return implementation(*args, **kwargs)
    #     else:
    #         return None


    @classmethod
    def resolve(cls, interface: Type):
        """Resuelve una implementación para una interfaz dada."""
        return cls._dependencies.get(interface)

def register_dependency(interface: Type, implementation: Type):    
    """Función para registrar una implementación como una dependencia."""
    DependencyContainer.register(interface, implementation)

def get_dependency(interface: Type):
    """Obtiene la implementación de una interfaz dada."""
    implementation = DependencyContainer.resolve(interface)
    if implementation:
        return implementation()
    else:
        raise Exception(f"No se encontró implementación para la interfaz {interface}")
