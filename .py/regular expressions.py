# re (Regular expressions) esas metnlerde xusisi yazilari xusisi formalarda tapmaq ucun istifade olunur
# Regular Expressions = regex = re library  = import re
# re.findall(text,sentence) = nece dene varsa gosterir
# re.span() axtardigin sheyin  bashlam ve bitme indeksi
# re.compile()  
# group() = returns 
# for loopda ishletmek ucun re.finditer(text,sentence)
# re.search(text,sentence)
# (055)-857-41-44   r"(\d\d\d)-\d\d\d-\d\d-\d\d" or r"(\d{3})-\d{3}-\d{2}-\d{2}"

# \d - A Digit (0-9)
# \w - Alphanumeratic  (A,b,_,1,2)
# \s - Whitespace (space,probel)
# \D - Non Digit (ABC)
# \W -  Non-Alphanumeratic(*-=+)
# \S - Non-Whitespace

# . Default MODE Matches Any character except newline
# +  Occurs one or more times (A-b1_1  = \w-\w+)
# {3} Occurs 3 times
# {2,4} Occurs 2to 4 times
# {3,} Occurs 3 or more times 
# * Occurs zero or more times
# ? Once or none

# ^  - Starts with  (^\d starts with digit)
# $ - Ends with  (\d$  Ends with digit)
# [^] - Exclude  ( [^\d] Exclude digits)

import re
#print(dir(re)) #dir modulun hansi funskiyalari oldugunu gosterir
string = "Telefon nomresi (055)-857-41-44"

print(re.split("[()-]",string)) #adi splitden ferqli olaraq re.splitde []-in icine bir nece sheye gore bolmek olur
re.search(r"",string) #textde gedib ilk patterni tapir ve index locationunu tuple olaraq verir
re.match(r"",string) # patterin sadece stringin evvelinde olanda tapir
