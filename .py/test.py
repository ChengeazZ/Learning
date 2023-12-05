#HelloToWorld

word = 'HelloToWorld'
new_word = ''
for i in word:
    if i.isupper():
        new_word += " " + i
    else:
        new_word += i
print(new_word[1:])


print(''.join([' ' + i if i.isupper() else i  for i in word])[1:])