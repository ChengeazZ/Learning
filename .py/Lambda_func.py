#lambda tek setirde funksiya yaradir. Eger bir funskiyadan bir defe istifade edecksense , funksiya yaradib yaddashda saxlamaq yerine bununla tekli funksiya et
# en esasda map() ve s kimi argument olaraq funskiya isteyen funksiyalarda istifade et
kvadrat_al =lambda x : x * x  #lambda dan sonra daxil olacaq argumentler : noqteden sonra olacaq prossesler , lambda variabili funksiya edir. kvadrat_al artiq bir funksiyadi
print(kvadrat_al(5))

print ((lambda a, b, c : a*b+c)(2,3,14)) #lambda avtomatik funksiya yaratdigi ucun variable assign etmeye ehtiyac duymur
print ((lambda *args : sum(args)/len(args))(10,20))

#-----------------------------------------------------------------------
#numune asagidaki tuple lardan ibaret listi yas sirasina gore siralamaq/sort etmek lazimdi. sort(key= ) funksiya isteyir . tekseferlik isledek

listim = [("Cingiz",24),("ELdar",23),("Seymur",22),('Azer',45)]
listim.sort(key=lambda x : x[1])
print(listim)