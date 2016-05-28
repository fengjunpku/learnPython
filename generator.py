def basic():
  g = (x*x for x in range(10))
  for n in g:
    print(n)

def fab(n):
  x,a,b = 0,0,1
  while x<n:
    yield b
    a,b = b,a+b
    x+=1

for x in fab(7):
  print(x)
