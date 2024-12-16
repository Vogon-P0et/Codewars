#odd even practice
def even_or_odd(number):
  if int(number) % 2 == 0:
    return "Even"
  else:
    return "Odd"


#numbers to strings
def number_to_string(num):
    return str(num)


#vowel count
def getCount(sentence):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return sum([sentence.count(vowel) for vowel in vowels])
