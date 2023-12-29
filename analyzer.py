import re
import ignored

with open('input.txt', encoding="utf-8") as input_file:
  text = input_file.read()

words = re.split(r'\s+', text.lower())
words = [re.sub(r'^\W+|\W+$', '', w) for w in words]

frequency = {}

for w in words:
  if w in frequency:
    frequency[w] += 1
  else:
    frequency[w] = 1

frequency_list = list(frequency.items())
frequency_list = [row for row in frequency_list if row[0] not in ignored.words]
frequency_list.sort(reverse=True, key=(lambda row : row[1]))

for item in frequency_list[:10]:
  print(f'{item[0]} \t {item[1]}')
