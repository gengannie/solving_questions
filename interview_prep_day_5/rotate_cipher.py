def rotateCharacter(c, rotation_f):
  if c.isalpha() and c.isupper():
    return (ord(c) - ord('A') + rotation_f) % 26 + ord('A')
  elif c.isalpha():
    return (ord(c) - ord('a') + rotation_f) % 26 + ord('a')
  else:
    return (ord(c) - ord('0') + rotation_f) % 10 + ord('0')
def rotationalCipher(input, rotation_factor):
  # Write your code here
  ans = list(input)
  for count, i in enumerate(ans):
    if (ord(i) <= ord('9') and ord(i) >= ord('0')) or i.isalpha():
      ans[count] = chr(rotateCharacter(i, rotation_factor))
  return "".join(ans)
print(rotationalCipher("Zebra-493?", 3))