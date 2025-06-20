from pathlib import Path

from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = Path(__file__).parent.parent


class AuthJWT(BaseModel):
    private_key_path: Path = BASE_DIR / 'certs' / 'jwt-private.pem'
    public_key_path: Path = BASE_DIR / 'certs' / 'jwt-public.pem'
    algorithm: str = 'RS256'
    access_token_expire_minutes: int = 60
    refresh_token_expire_minutes: int = 43200


class Settings(BaseSettings):
    db_url: str = 'postgresql+asyncpg://test:test@localhost/sber'
    db_echo: bool = True
    auth_jwt: AuthJWT = AuthJWT()


settings = Settings()

