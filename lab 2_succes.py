d={}
x = int()
with open('conf', 'r') as file:
    for line in file:
        if line[0] != "#" and line[0] !=';' and line[0] != '\n':
            list0 = line.split(' ', 1)
            x = len(list0)
            if  x > 1:
                key = list0[0]
                value = list0[1] 
                d[key] = value
            




while key != "end":
    try: 
        key = input("""Введите значенение ключа или введите слово "end" чтобы выйти из программы:""")
        if key!= 'end':
            print ("Ключ:", key," Значение:", d[key])
        
    except:
        print("Ключ:", key," Значение: Значение не задано либо произошла ошибка обработки ключа.\n")
    finally:
        print("Завершение программы")