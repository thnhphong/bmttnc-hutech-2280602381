#!/bin/bash

# ECC API curl examples for Postman testing
# Make sure the API is running on port 5002: python api.py

# 1. Generate Keys (GET)
curl --location 'http://127.0.0.1:5002/api/ecc/generate_keys'

# 2. Sign (POST)
curl --location 'http://127.0.0.1:5002/api/ecc/sign' \
--header 'Content-Type: application/json' \
--data '{
    "message": "HUTECH University"
}'

# 3. Verify (POST)
# Note: Replace <signature_hex> with the actual signature from step 2
curl --location 'http://127.0.0.1:5002/api/ecc/verify' \
--header 'Content-Type: application/json' \
--data '{
    "message": "HUTECH University",
    "signature": "<signature_hex>"
}'

