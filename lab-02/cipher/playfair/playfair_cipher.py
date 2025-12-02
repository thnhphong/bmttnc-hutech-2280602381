class PlayfairCipher:
  def __init__(self):
    pass

  def create_playfair_matrix(self, key):
    key = key.replace("J", "I")
    key = key.upper()

    key_set = set()
    key_unique = ""
    for char in key:
      if char.isalpha() and char not in key_set:
        key_set.add(char)
        key_unique += char
    key = key_unique
    
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    remaining_letters = [
      letter for letter in alphabet if letter not in key_set
    ]
    matrix = list(key)

    for letter in remaining_letters:
      matrix.append(letter)
      if len(matrix) == 25:
        break
    playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    return playfair_matrix

  def find_letter_coords(self, matrix, letter): 
    for row in range(len(matrix)):
      for col in range(len(matrix[row])):
        if matrix[row][col] == letter:
          return row, col

  def playfair_encrypt(self, plain_text, matrix):
    plain_text = plain_text.replace("J", "I")
    plain_text = plain_text.upper()
    # Prepare text: handle duplicate letters in pairs
    prepared_text = ""
    i = 0
    while i < len(plain_text):
      if i < len(plain_text) - 1 and plain_text[i] == plain_text[i+1]:
        prepared_text += plain_text[i] + "X"
        i += 1
      else:
        prepared_text += plain_text[i]
        i += 1
    
    # Add X if odd length
    if len(prepared_text) % 2 == 1:
      prepared_text += "X"
    
    encrypted_text = ""
    for i in range(0, len(prepared_text), 2):
      pair = prepared_text[i:i+2]
      row1, col1 = self.find_letter_coords(matrix, pair[0])
      row2, col2 = self.find_letter_coords(matrix, pair[1])
      if row1 == row2:
        encrypted_text += matrix[row1][(col1+1)%5] + matrix[row2][(col2+1)%5]
      elif col1 == col2:
        encrypted_text += matrix[(row1+1)%5][col1] + matrix[(row2+1)%5][col2]
      else:
        encrypted_text += matrix[row1][col2] + matrix[row2][col1]
    return encrypted_text

  def playfair_decrypt(self, cipher_text, matrix):
    cipher_text = cipher_text.upper()
    decrypt_text = ""

    for i in range(0, len(cipher_text), 2):
      pair = cipher_text[i:i+2]
      row1, col1 = self.find_letter_coords(matrix, pair[0])
      row2, col2 = self.find_letter_coords(matrix, pair[1])
      if row1 == row2: 
        decrypt_text += matrix[row1][(col1-1)%5] + matrix[row2][(col2-1)%5]
      elif col1 == col2:
        decrypt_text += matrix[(row1-1)%5][col1] + matrix[(row2-1)%5][col2]
      else:
        decrypt_text += matrix[row1][col2] + matrix[row2][col1]

    # Remove padding X and handle duplicate letters
    plain_text = ""
    i = 0
    while i < len(decrypt_text):
      if i < len(decrypt_text) - 1:
        if decrypt_text[i] == decrypt_text[i+1] and decrypt_text[i] != 'X':
          plain_text += decrypt_text[i]
          i += 1
        else:
          plain_text += decrypt_text[i] + decrypt_text[i+1]
          i += 2
      else:
        plain_text += decrypt_text[i]
        i += 1
    
    # Remove trailing X if it was padding
    if len(plain_text) > 0 and plain_text[-1] == 'X' and len(plain_text) % 2 == 1:
      plain_text = plain_text[:-1]
    
    return plain_text
