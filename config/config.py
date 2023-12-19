import os
from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())



class DatabaseSettings(BaseSettings):
    model_config = SettingsConfigDict(extra='allow', env_file='./.env', env_file_encoding='utf-8')
    DATABASE_USERNAME: str
    DATABASE_PASSWORD: str
    DATABASE_HOST: str
    DATABASE_NAME: str
    DATABASE_PORT: int


class JWTSettings(BaseSettings):
    model_config = SettingsConfigDict(extra='allow', env_file='./.env', env_file_encoding='utf-8')
    ACCESS_TOKEN_EXPIRE_TIME_MINUTES: int
    REFRESH_TOKEN_EXPIRE_TIME_HOURS: int
    JWT_ALGORITHM: str
    AUTH_JWT_HEADER_TYPE: str
    AUTH_SECRET_KEY: str
    AUTH_JWT_DECODE_ALGORITHMS: list = ["HS384", "HS512"]
    TEST_DB_URL: str
    authjwt_secret_key: str

class TestConfiguration(BaseSettings):
    model_config = SettingsConfigDict(extra='allow', env_file='./.env', env_file_encoding='utf-8')
    TEST_DB_URL: str


class Settings(DatabaseSettings, JWTSettings):
    pass


class DevelopmentConfig(Settings):
    """
    This class for generates the config for development instance.
    """
    DEBUG: bool = True
    TESTING: bool = False
    SQLALCHEMY_DATABASE_URL: str = f"postgresql+psycopg2://{Settings().DATABASE_USERNAME}:{Settings().DATABASE_PASSWORD}@{Settings().DATABASE_HOST}:{Settings().DATABASE_PORT}/{Settings().DATABASE_NAME}"


class ProductionConfig(Settings):
    """
    This class for generates the config for the development instance.
    """
    DEBUG: bool = False
    TESTING: bool = False


def get_current_server_config():
    server_type = os.environ.get('SERVER_TYPE', 'DEVELOPMENT')
    return DevelopmentConfig() if server_type.upper() == 'DEVELOPMENT' else ProductionConfig
