import string

alph = string.ascii_lowercase[:]
cypher = {x:y for x,y in zip(alph, alph[::-1])}

def answer(s):
	return ''.join([(cypher[c] if c in cypher else c) for c in list(s)])
	
s1 = "wrw blf hvv ozhg mrtsg'h vkrhlwv?"
s2 = "Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!"
print(answer(s1))
print(answer(s2))
