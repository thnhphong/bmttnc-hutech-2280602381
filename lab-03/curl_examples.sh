#!/bin/bash

# RSA API curl examples
# Make sure the API is running on port 5002: python api.py

# 1. Generate Keys (GET)
curl --location 'http://127.0.0.1:5002/api/rsa/generate_keys'

# 2. Encrypt (POST)
curl --location 'http://127.0.0.1:5002/api/rsa/encrypt' \
--header 'Content-Type: application/json' \
--data '{
    "message": "Hello World",
    "key_type": "public"
}'

# 3. Decrypt (POST)
# Note: Replace <encrypted_hex> with the actual encrypted message from step 2
curl --location 'http://127.0.0.1:5002/api/rsa/decrypt' \
--header 'Content-Type: application/json' \
--data '{
    "ciphertext_hex": "8ec2eaf9d6df1cc8edd354fdd8689d8a79236a7d18c9b0fb1bb20b1dfcc7b8c1bcec0c9a4b8b879e41300d35e54b7b77521f92163bde1c8528c14eba726bc54ce5de524808e2dbfb39496e1632f8e7ae86409d2ac95c74d8d8e59d9c312e54249eac19fbb48abf4e7c49333c2b791002548ada2855da1aa6920f93782b223576fb6da53d22030fd586585b0965dbff10a6b623443584ef0f34f23005eca34781a96a790cdc67b8b1ff24c92aa8ec6998c6f393f8e0eab5649adcc6d05f1cc8f39be101d40e621bd422b65cd8dcd2c14ec2caa9fc72a8bdf0933624f45fddf3a3a409088ddd5f371a341e554255a7522efb4e56c8251352a2385c8eba5a67d53f",
    "key_type": "private"
}'

# 4. Sign (POST)
curl --location 'http://127.0.0.1:5002/api/rsa/sign' \
--header 'Content-Type: application/json' \
--data '{
    "message": "HUTECH University"
}'

# 5. Verify (POST)
# Note: Replace <signature_hex> with the actual signature from step 4
curl --location 'http://127.0.0.1:5002/api/rsa/verify' \
--header 'Content-Type: application/json' \
--data '{
    "message": "HUTECH University",
    "signature_hex": "<signature_hex>"
}'

