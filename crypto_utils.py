# cypro_utils.py

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64
import os

# 비밀번호와 salt로부터 AES 대칭키를 생성하는 함수
def generate_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=390000,
    )
    return base64.urlsafe_b64encode(kdf.derive(password.encode()))

# 파일을 AES 방식으로 암호화하는 함수
def encrypt_file(file_path: str, password: str):
    salt = os.urandom(16)
    key = generate_key(password, salt)
    fernet = Fernet(key)

    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)

    with open(file_path + ".enc", "wb") as enc_file:
        enc_file.write(salt + encrypted)


# 암호화된 파일을 복호화하는 함수
def decrypt_file(file_path: str, password: str):
    with open(file_path, "rb") as file:
        content = file.read()

    salt = content[:16]
    encrypted = content[16:]
    key = generate_key(password, salt)
    fernet = Fernet(key)
    decrypted = fernet.decrypt(encrypted)

    with open(file_path.replace(".enc", "_decrypted"), "wb") as dec_file:
        dec_file.write(decrypted)
