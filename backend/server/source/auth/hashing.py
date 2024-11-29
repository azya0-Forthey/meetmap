from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["sha256_crypt"])

def verify_pwd(value: str, hashed_value: str) -> bool:
    return pwd_context.verify(value, hashed_value)

def hash_pwd(value: str) -> str:
    return pwd_context.hash(value)