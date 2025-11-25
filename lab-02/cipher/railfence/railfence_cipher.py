class RailfenceCipher:
  def __init__(self):
    pass
  
  def rail_fence_encrypt(self, plain_text, num_rails): 
    # Convert num_rails to int if it's a string
    num_rails = int(num_rails)
    rails = [[] for _ in range(num_rails)]
    rail_index = 0
    direction = 1
    for char in plain_text:
      rails[rail_index].append(char)
      if rail_index == 0: 
        direction = 1
      elif rail_index == num_rails - 1:
        direction = -1
      rail_index += direction
    # Join all rails row by row to form the cipher text
    cipher_text = ""
    for rail in rails:
      cipher_text += "".join(rail)
    return cipher_text

  def rail_fence_decrypt(self, cipher_text, num_rails):
    # Convert num_rails to int if it's a string
    num_rails = int(num_rails)
    rails_length = [0] * num_rails
    rail_index = 0
    direction = 1 
    for _ in range(len(cipher_text)):
      rails_length[rail_index] += 1
      if rail_index == 0:
        direction = 1
      elif rail_index == num_rails - 1:
        direction = -1
      rail_index += direction

    rails = []
    start = 0 
    for length in rails_length:
      rails.append(cipher_text[start:start+length])
      start += length
    plain_text = ""
    rail_index = 0 
    direction = 1

    for _ in range(len(cipher_text)):
      plain_text += rails[rail_index][0]
      rails[rail_index] = rails[rail_index][1:]
      if rail_index == 0:
        direction = 1
      elif rail_index == num_rails - 1:
        direction = -1
      rail_index += direction
    return plain_text