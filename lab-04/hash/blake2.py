import hashlib

def blake2(message):
  blake2_hash = hashlib.blake2b()
  blake2_hash.update(message)
  return blake2_hash.digest()

def main():
  text = input("Enter a string to calculate Blake2 hash: ").encode('utf-8')
  hashed_text = blake2(text)
  print(f"Entered string: {text.decode('utf-8')}")
  print(f"Blake2 hash: {hashed_text.hex()}")

if __name__ == "__main__":
  main()