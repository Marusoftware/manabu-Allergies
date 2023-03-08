from pydantic import BaseSettings
from datetime import timedelta as _timedelta

class Settings(BaseSettings):
    postgres_host:str
    postgres_port:str
    postgres_user:str
    postgres_password:str
    postgres_db:str
    timedelta:_timedelta = _timedelta()
    
    class Config:
        env_file = ".env"