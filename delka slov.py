dict = {}
radek = ['wfdefc', 'ac', 'qw', 'hgftdtydtydtf', 'qvcq', 'as']
for slovo in radek:

	#delka slova je klic
	#hodnota ke klici je pocet vyskytu

	if len(slovo) in dict.keys():
		dict[len(slovo)] +=1
	else:
		dict[len(slovo)] = 1

for klic in sorted(dict.keys()):
	print(dict[klic],"*" * klic, klic)
print (dict)