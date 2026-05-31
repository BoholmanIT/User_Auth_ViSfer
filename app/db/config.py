from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings): 
    HOSTDB: str
    USERDB: str
    PASSDB: str
    APPNAME: str
    PORTDB: str
    STACKDB: str
    DATABASE_URL: str
    
    @property
    def DATABASE_URL_asynccopg(self):
        return f"{self.DATABASE_URL}"
    
    
    model_config = SettingsConfigDict(env_file = ".env")
    
settings = Settings() 