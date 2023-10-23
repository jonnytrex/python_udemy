upper = 'ABC'
lower = 'abc'
def lowercase_word(word):
  '''check a word for uppercase letters and make the uppercase letters lowercase'''
  newword = ''
  for char in word:
    if char in upper:
      index = upper.index(char)
      newchar = lower[index]
      newword += newchar
    else:
      newword += char
  return newword

print(lowercase_word(word="hAbitAt"))

    