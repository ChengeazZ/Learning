#Rangoli
import string
size =6
pat = string.ascii_lowercase
letters = pat[:size][::-1]
rangoli = []
for i in range(size):
    left_side = letters[:i+1]
    right_side = left_side[::-1][1:]
    total_side = left_side + right_side
    final = "-".join(total_side)
    rangoli.append(final)

width = len(rangoli[-1])
d_rangoli = rangoli[:-1][::-1]

for i in rangoli + d_rangoli:
    print(i.center(width,"-"))

#Door Mat
n = 7
m = n * 3
pattern = ".|."

for i in range(1,n,2):
    print((pattern*i).center(m,"-"))
print("WELCOME".center(m,'-'))
for i in reversed(range(1,n,2)):
    print((pattern*i).center(m,"-"))
