from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher 
app = Flask(__name__)

#CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok", "message": "API is running", "endpoints": ["/api/caesar/encrypt", "/api/caesar/decrypt"]})

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt(): 
  try:
    # Check Content-Type header
    if not request.is_json:
      return jsonify({
        "error": "Content-Type must be application/json",
        "received_content_type": request.content_type,
        "tip": "Set Header: Content-Type = application/json"
      }), 400
    
    data = request.json 
    if not data:
      return jsonify({
        "error": "No JSON data provided",
        "tip": "Make sure Body is set to 'raw' and format is 'JSON'"
      }), 400
    
    plain_text = data.get("plain_text")
    key = data.get("key")
    
    if plain_text is None or key is None:
      return jsonify({
        "error": "Missing required fields: plain_text and key",
        "received_data": data,
        "tip": "Required JSON: {\"plain_text\": \"YOUR_TEXT\", \"key\": NUMBER}"
      }), 400
    
    key = int(key)
    encrypt_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_text": encrypt_text})
  except ValueError as e:
    return jsonify({"error": f"Invalid key value: {str(e)}"}), 400
  except Exception as e:
    return jsonify({"error": str(e)}), 500

@app.route("/api/caesar/decrypt", methods=["POST"])
def caesar_decrypt():
  try:
    # Check Content-Type header
    if not request.is_json:
      return jsonify({
        "error": "Content-Type must be application/json",
        "received_content_type": request.content_type,
        "tip": "Set Header: Content-Type = application/json"
      }), 400
    
    data = request.json
    if not data:
      return jsonify({
        "error": "No JSON data provided",
        "tip": "Make sure Body is set to 'raw' and format is 'JSON'"
      }), 400
    
    # Accept both "encrypted_text" and "cipher_text" field names
    encrypted_text = data.get("encrypted_text") or data.get("cipher_text")
    key = data.get("key")
    
    if encrypted_text is None or key is None:
      return jsonify({
        "error": "Missing required fields: encrypted_text (or cipher_text) and key",
        "received_data": data,
        "tip": "Required JSON: {\"encrypted_text\": \"YOUR_TEXT\", \"key\": NUMBER} or {\"cipher_text\": \"YOUR_TEXT\", \"key\": NUMBER}"
      }), 400
    
    key = int(key)
    decrypt_text = caesar_cipher.decrypt_text(encrypted_text, key)
    return jsonify({"decrypted_text": decrypt_text})
  except ValueError as e:
    return jsonify({"error": f"Invalid key value: {str(e)}"}), 400
  except Exception as e:
    return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5001, debug=True)
