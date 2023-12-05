import itertools

iterable1 = [1,2,3]
iterable2 = ["a","b","c"]

product = itertools.product(iterable1,iterable2)
permutations = itertools.permutations(iterable2,3) #3 burda yaranacaq tupllarin icindeki elemntlerin limitidi / No element is repeated in a permutation
combinations = itertools.combinations(iterable2,2) #No element is repeated in a permutation
combinations_with_replacements = itertools.combinations_with_replacement(iterable1,3) # Elements can be repeated in a combination


print(list(product))
print("#"*60)
print(list(permutations))
print("#"*60)
print(list(combinations))
print("#"*60)
print(list(combinations_with_replacements))

