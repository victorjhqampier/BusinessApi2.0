from datetime import datetime, timedelta
from Application.Adpaters.Users.ClaimAdapter import ClaimAdapter
import jwt
import os
from dotenv import load_dotenv
load_dotenv()


class JwtHandler():
    __secret_key:str
    __expire_in:int
    def __init__(self) -> None:
        self.__secret_key=f"{os.getenv('JWT_SECRET_KEY')}"
        self.__expire_in=int(f"{os.getenv('JWT_EXPIRE_MIN')}")

    def create_token(self, objClaim: ClaimAdapter) -> str:
        token_expire = timedelta(minutes=self.__expire_in)
        dict_claim = objClaim.__dict__
        
        # dict_claim['exp'] = datetime.utcnow() + token_expire
        dict_claim.update({"exp":datetime.utcnow() + token_expire})
        return jwt.encode(dict_claim, self.__secret_key, algorithm="HS256")