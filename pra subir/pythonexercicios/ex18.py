import math
a=float(input('qul o angulo q vc deseja'))
se=math.sin(math.radians(a))
print(' o angulo de {} tem o seno de {:.2f}'.format(a,se))
co=math.cos(math.radians(a))
print('e seu coseno é',co )
tan=math.tan(math.radians(a))
print('e a tangente de ',tan)