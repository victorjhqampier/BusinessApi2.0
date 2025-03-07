from typing import Optional # 👈 new imports

import jwt # 👈 new imports
from fastapi import Depends, HTTPException, status # 👈 new imports
from fastapi.security import SecurityScopes, HTTPAuthorizationCredentials, HTTPBearer # 👈 new imports

# from application.config import get_settings # 👈 new imports

import os
from dotenv import load_dotenv
load_dotenv()

class UnauthorizedException(HTTPException):
    def __init__(self, detail: str, **kwargs):
        """Returns HTTP 403"""
        super().__init__(status.HTTP_403_FORBIDDEN, detail=detail)

class UnauthenticatedException(HTTPException):
    def __init__(self):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Requires authentication"
        )

# 👇 new code
class VerifyToken:
    """Does all the token verification using PyJWT"""

    def __init__(self):
        
        jwks_url = f'https://{os.getenv("AUTH0_DOMAIN")}/.well-known/jwks.json'
        self.jwks_client = jwt.PyJWKClient(jwks_url)
        
        # 👇 new code
    async def verify(self,
                     security_scopes: SecurityScopes,
                     token: Optional[HTTPAuthorizationCredentials] = Depends(HTTPBearer())
                     ):
        if token is None:
            raise UnauthenticatedException
        
        
        # This gets the 'kid' from the passed token
        try:
            signing_key = self.jwks_client.get_signing_key_from_jwt(
                token.credentials
            ).key
        except jwt.exceptions.PyJWKClientError as error:
            raise UnauthorizedException(str(error))
        except jwt.exceptions.DecodeError as error:
            raise UnauthorizedException(str(error))
        try:
            payload = jwt.decode(
                token.credentials,
                signing_key,
                algorithms=f"{os.getenv('AUTH0_ALGORITHMS')}",
                audience=f"{os.getenv('AUTH0_API_AUDIENCE')}",
                issuer=f"{os.getenv('AUTH0_ISSUER')}"
            )
        except Exception as error:
            raise UnauthorizedException(str(error))
    
        return payload    
        # 👆 new code