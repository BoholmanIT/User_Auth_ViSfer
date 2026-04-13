from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings): 
    HOSTDB: str
    USERDB: str
    PASSDB: str
    APPNAME: str
    PORTDB: str
    STACKDB: str
    
    @property
    def DATABASE_URL_asynccopg(self):
        return f"{self.STACKDB}://{self.USERDB}:{self.PASSDB}@{self.HOSTDB}:{self.PORTDB}/{self.APPNAME}"
    
    
    model_config = SettingsConfigDict(env_file = ".env")
    
settings = Settings() 