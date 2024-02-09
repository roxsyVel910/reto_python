#Tuplas - Diccionarios

#tubla --> es inmutable

#indices        0        1        2        3         4    
setting = {'locashost', 3306, 'root', 'password','database'}
print(len(setting)) #5 elementos (setting)

#desempaquetado de tuplas
host, port, username, password, name = setting
host, port, *_ = setting
host, *_, password, database = setting

print(host, port, username, password, name)
print(host,  database)

#tuplas anidadas
example = (
    (1,2,3),
    (4,5,6),
    (7,8,9)
)
for _tuple in example:
    for _tuple in _tuple:
        print(_tuple)

#tuplas anidadas
for number1, number2, number3 in example:
    print(number1, number2, number3)



#Diccionarios --> estructura de datos, no ordenado, no indexado trabajo con llaves- valor
    user = {
        #llave:valor
        'id': 1,
        'name': 'John',
        'age': 30,
        'email': 'XHfZS@example.com',
        'active': True,
        10: 3.13,
        True:'veradero',
        (1,2,3): 'tupla',
    }

for key, value in tuple(user).items():
    print(key, value)
    