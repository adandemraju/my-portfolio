weight = int(input('Weight: '))
unit = input('(L)bs or (K)g: ')

if unit.upper() == 'L':
    new_weight = round(weight * 0.45)
    new_unit = 'kilograms'
elif unit.upper() == 'K':
    new_weight = round(weight / 0.45)
    new_unit = 'pounds'

print(f'You are about {new_weight} {new_unit}')