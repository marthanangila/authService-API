from pydantic_settings import BaseSettings
class Settings(BaseSettings):

    #database
    DATABASE_URL : str

    #JWT
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int= 30

    model_config = {"env_file": ".env"}

settings = Settings()
