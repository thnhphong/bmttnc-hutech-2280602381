from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.backends import default_backend
import os

class RSACipher:
    def __init__(self):
        self.keys_dir = os.path.join(os.path.dirname(__file__), 'keys')
        os.makedirs(self.keys_dir, exist_ok=True)
        self.public_key_path = os.path.join(self.keys_dir, 'public_key.pem')
        self.private_key_path = os.path.join(self.keys_dir, 'private_key.pem')

    def generate_keys(self):
        """Generate RSA key pair and save to files"""
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )
        public_key = private_key.public_key()

        # Save private key
        private_pem = private_key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        )
        with open(self.private_key_path, 'wb') as f:
            f.write(private_pem)

        # Save public key
        public_pem = public_key.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        )
        with open(self.public_key_path, 'wb') as f:
            f.write(public_pem)

    def load_keys(self):
        """Load RSA keys from files"""
        if not os.path.exists(self.public_key_path) or not os.path.exists(self.private_key_path):
            raise FileNotFoundError("Keys not found. Please generate keys first.")

        # Load private key
        with open(self.private_key_path, 'rb') as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None,
                backend=default_backend()
            )

        # Load public key
        with open(self.public_key_path, 'rb') as f:
            public_key = serialization.load_pem_public_key(
                f.read(),
                backend=default_backend()
            )

        return public_key, private_key

    def encrypt(self, message, key):
        """Encrypt message using RSA key"""
        message_bytes = message.encode('utf-8')
        encrypted = key.encrypt(
            message_bytes,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return encrypted

    def decrypt(self, ciphertext, key):
        """Decrypt ciphertext using RSA key"""
        decrypted = key.decrypt(
            ciphertext,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )
        return decrypted.decode('utf-8')

    def sign(self, message, private_key):
        """Sign message using private key"""
        message_bytes = message.encode('utf-8')
        signature = private_key.sign(
            message_bytes,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )
        return signature

    def verify(self, message, signature, public_key):
        """Verify signature using public key"""
        message_bytes = message.encode('utf-8')
        try:
            public_key.verify(
                signature,
                message_bytes,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                hashes.SHA256()
            )
            return True
        except Exception:
            return False
