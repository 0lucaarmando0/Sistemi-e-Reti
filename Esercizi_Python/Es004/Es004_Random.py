import random as rnd

notSorted = ["Armando Yuri" , "Acchiardi Paolo" , "Everyone else"]
sorted = []

for num, student in enumerate(notSorted):
    print(f"{num} - {student}")

print(f"viene interrogato : {notSorted[rnd.randint(0,len(notSorted)-1)]}")