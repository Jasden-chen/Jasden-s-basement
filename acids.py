# set up
comp1 = input('chemical compound: ')
comp1_sep = [char for char in comp1]
comp2 = input('chemical compound: ')
comp2_sep = [char for char in comp2]
acid = 'nan'
base = 'nan'

# determining which one is acid and base
if comp1 == 'H2O' and not comp2_sep.__contains__('H'):
    acid = comp1
    base = comp2
if comp2 == 'H2O' and not comp1_sep.__contains__("H'"):
    acid = comp2
    base = comp1
if comp1 or comp2 != 'H2O':
    if comp1_sep[0] == 'H' and comp1 != "H2O":
        acid = comp1
        base = comp2
    elif comp2_sep[0] == 'H' and comp2 != "H2O":
        acid = comp2
        base = comp1

print('Acid: ', acid)
print('base: ', base)

# solving for conjugate bases and acids

# solving for conjugate acid
acid = [char for char in acid]
conjacid = 'N/A'
if acid[1].isalpha():
    conjacid = [acid for acid in acid if acid != 'H']
    conjacid = "".join(conjacid)
    print('conjugate acid: ', conjacid)
elif not acid[1].isalpha() == True:
    conjacid = [acid for acid in acid]
    conjacid = conjacid[0], str(int(conjacid[1]) - 1).join(conjacid[2:len(conjacid)])
    conjacid = ''.join(conjacid)
    print('conjugate acid: ', conjacid.replace('H1O', 'OH') and conjacid.replace('1', ''))


# solving for conjugate base
conjbase = [char for char in base]
if conjbase == 'H':
    conjbase = [char for char in base]
    conjbase = conjbase[0], str(int(conjbase[1]) + 1), conjbase[2]
    conjbase = "".join(conjbase)
    print('conjugate base: ', conjbase)
elif conjbase.__contains__("H"):
    conjbase = [char for char in base]
    index_H = conjbase.index('H')
    if index_H + 1 < len(conjbase):
        conjbase[index_H + 1] = str(int(conjbase[index_H + 1]) + 1)
        conjbase = "".join(conjbase)
        print('Conjugate base: ', conjbase)
    elif index_H + 1 >= len(conjbase):
        conjbase = 'H2O'
        print('Conjugate base: ', conjbase)
elif not conjbase.__contains__("H"):
    conjbase.insert(0, "H")
    conjbase = ''.join(conjbase)
    print('Conjugate base: ', conjbase)
