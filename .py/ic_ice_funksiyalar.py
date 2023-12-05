def kvadrat(x):
    return x*x

a = kvadrat

#print(kvadrat(5))
#print(a(5))
#=------------------------------------------------------------------------------------

def hesablamalar(novu):
    def toplama(*args):
        return sum(args)
    def ortalama(*args):
        return sum(args)/len(args)
    if novu == "ortalama":
        return ortalama
    elif novu == "toplama":
        return toplama
    
toplayan = hesablamalar("toplama")
#print(toplayan(5,5,10))

#-----------------------------------------------------------------------------------------
def ad_sec(ad):
    def kamanda_sec(kamanda):
        return f"{ad} {kamanda} komandasina azarkeslik edir"
    return kamanda_sec

a = ad_sec("Cingiz")
print(a("Galatasaray"))
        
    


