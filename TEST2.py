n = 7
m = n * 3
pattern = ".|."

for i in range(1,n,2):
    print((pattern*i).center(m,"-"))
print("WELCOME".center(m,'-'))
for i in reversed(range(1,n,2)):
    print((pattern*i).center(m,"-"))


