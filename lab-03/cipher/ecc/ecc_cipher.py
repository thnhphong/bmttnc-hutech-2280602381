import ecdsa
import os
from pathlib import Path

class ECCCipher:
    def __init__(self):
        # Get the directory where this file is located
        self.base_dir = Path(__file__).parent
        self.keys_dir = self.base_dir / 'keys'
        self.keys_dir.mkdir(exist_ok=True)
        self.private_key_path = self.keys_dir / 'privateKey.pem'
        self.public_key_path = self.keys_dir / 'publicKey.pem'

    def generate_keys(self):
        # Tạo khóa riêng tư
        sk = ecdsa.SigningKey.generate()
        # Lấy khóa công khai từ khóa riêng tư
        vk = sk.get_verifying_key()
        
        # Lưu khóa riêng tư
        with open(self.private_key_path, 'wb') as p:
            p.write(sk.to_pem())
        
        # Lưu khóa công khai
        with open(self.public_key_path, 'wb') as p:
            p.write(vk.to_pem())

    def load_keys(self):
        # Load private key
        with open(self.private_key_path, 'rb') as p:
            sk = ecdsa.SigningKey.from_pem(p.read())
        
        # Load public key
        with open(self.public_key_path, 'rb') as p:
            vk = ecdsa.VerifyingKey.from_pem(p.read())
        
        return sk, vk

    def sign(self, message, key):
        # Ký dữ liệu bằng khóa riêng tư
        return key.sign(message.encode('ascii'))

    def verify(self, message, signature, key):
        try:
            key.verify(signature, message.encode('ascii'))
            return True
        except ecdsa.BadSignatureError:
            return False

