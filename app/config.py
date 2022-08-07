from pydantic import BaseSettings

class Setting(BaseSettings):
    database_hostname:str
    database_port:str
    database_password:str
    database_name:str
    database_username:str
    secret_key:str
    algorithm:str
    expire_access_token:int
    
    class Config:
        env_file=".env"
        
settings = Setting()
    
