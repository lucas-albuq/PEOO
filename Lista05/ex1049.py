type01 = input()
type02 = input()
type03 = input()

if type01 == 'vertebrado':
    if type02 == 'ave':
        if type03 == 'carnivoro':
            print('aguia')
        else:
            print('pomba')
    else:
        if type03 == 'onivoro':
            print('homem')
        else:
            print('vaca')
elif type01 == 'invertebrado':
    if type02 == 'inseto':
        if type03 == 'hematofago':
            print('pulga')
        else:
            print('lagarta')
    else:
        if type03 == 'hematofago':
            print('sanguessuga')
        else:
            print('minhoca')
