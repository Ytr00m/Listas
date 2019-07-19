n = 10
ma = None
me = None
for i in range(n):
   x = float(input("Digite um número: "))
   ma = ma if ma != None and ma >  x else x
   me = me if me != None and me < x else x

print ('O maior valor digitado foi {} e o menor foi {}'.format(ma,me))