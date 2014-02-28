#El programa 24 utiliza las diferencias, es decir cuando algunas de las partes es 0, iniciando desde:ninguna con 0, hasta, todas con 0. Aquí es al revez, se empieza por considerar todas 0 y se acaba por todas distintas de este valor.
from math import sqrt

a=float(raw_input('Valor de a: '))
b=float(raw_input('Valor de b: '))
c=float(raw_input('Valor de c: '))

if a==0:
if b==0:
if c==0:
print 'La ecuacion no tiene solucion'
else:
print 'Tiene infinitas soluciones'
else:
x=-c/b
print 'La solucion de la ecuacion es x=%4.3f' % (x1,x2)
else:
  x1=(-b+sqrt(b**2-4*a*c))/2*a
  x2?(-b -sqrt(b**2-4*a*c))/2*a
  print 'Soluciones %4.3f y %4.3f' % I(x1,x2)
