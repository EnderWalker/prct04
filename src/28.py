from math import sqrt

a=float(raw_input('Valor de a:'))
b=float(raw_input('Valor de b:'))
c=float(raw_input('Valor de c:'))
if a==0 and b==0 and c==0:
print 'La ecuacion tiene infinitas soluciones'
else:
 if a==0 and b==0
 print 'La ecuacion no tiene solucion'
else:
if a==0:
x=-c/b
print 'Solucion: %4.3f' % x
if b**2 < 4*a*c:
  print 'No tiene una solucion real, fallo de dominio(I|)'
else:
x1=(-b+sqrt(b**2-4*a*c))/2*a
x2=(-b-sqrt(b**2-4*a*c))/2*a
print'Soluciones: %4.3 y %4.3' % (x1,x2)

 #utiliza el and acortando el espacio y permitiendo intercalar más if en una misma línea de código.