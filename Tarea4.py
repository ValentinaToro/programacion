#
#En el primero deberán demostrar las 4 operaciones aritméticas, además de la operación módulo
# definiendo variables e imprimiéndolas en cada paso, usando f-strings.
print ("Primero definiré la variable,")
valor_global = 6
x = valor_global
print(x)
print(type(x))
print ("luego realizaré las cuatro operaciones más el cálculo del módulo.")
x = x + 4.0
print (x)
print(f"La primera operación, suma, da como resultado {x}, operando un int con un float, dando en resultado float.")
x = valor_global
x = x - 1
print (x)
print (f"La segunda operación, resta, da {x}.")
x = valor_global
x = x * 3
print (x)
print(f"La tercera operación, multiplicación, da {x}.")
x = valor_global
x = x / 2
print (x)
print (f"La cuarta operación, división, da como resultado {x}.")
x = valor_global
x = x % 2
print (x)
print (f"La quinta operación, módulo, da como resultado {x}.")