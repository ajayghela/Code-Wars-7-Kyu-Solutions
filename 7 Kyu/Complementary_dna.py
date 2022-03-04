# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G". You have function with one side of the DNA (string, except for Haskell); you need to get the other complementary side. DNA strand is never empty or there is no DNA at all (again, except for Haskell).

# More similar exercise are found here: http://rosalind.info/problems/list-view/ (source)

# Example: (input --> output)

# "ATTGC" --> "TAACG"
# "GTAT" --> "CATA"
# dnaStrand []        `shouldBe` []
# dnaStrand [A,T,G,C] `shouldBe` [T,A,C,G]
# dnaStrand [G,T,A,T] `shouldBe` [C,A,T,A]
# dnaStrand [A,A,A,A] `shouldBe` [T,T,T,T]


dna = "AAAA"

new_dna = ""
for i in dna:
    if i == 'A':
        new_dna += 'T'
    if i == 'T':
        new_dna += 'A'
    if i == 'C':
        new_dna += 'G'
    if i == 'G':
        new_dna += 'C'
    

print(new_dna)

import string
def DNA_strand(dna):
    return dna.translate(string.maketrans("ATCG","TAGC"))  

pairs = {'A':'T','T':'A','C':'G','G':'C'}
def DNA_strand(dna):
    return ''.join([pairs[x] for x in dna]) 


