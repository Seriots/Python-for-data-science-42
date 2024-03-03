from DiamondTrap import King

Joffrey = King("Joffrey")
print(Joffrey.__dict__)
Joffrey.set_eyes("blue")
Joffrey.set_hairs("light")
print(Joffrey.get_eyes())
print(Joffrey.get_hairs())
print(Joffrey.__dict__)
Joffrey._eyes = "green"
Joffrey._hairs = "blond"
print(Joffrey._eyes)
print(Joffrey._hairs)
print(Joffrey.__dict__)
