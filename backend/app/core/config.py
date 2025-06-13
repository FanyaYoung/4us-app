from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "4-Us"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your-secret-key-please-change-this"  # Change this in production
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    DATABASE_URL: str = "postgresql://user:password@localhost:5432/4us_db"

    class Config:
        case_sensitive = True

settings = Settings()
