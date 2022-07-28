
N=int(input('digite um angulo'))
n=float(input("diga o valor do cateto 1 adjascente"))
s=float(input('diga o valor do cateto 2 oposto'))
z=(n**2)+(s**2)
x=z/2
print('hipotenusa{}'.format(x))
seno=s/x
cose=n/x
tangente=s/n
print('seno{}, cose{},tangente{}' .format(seno,cose,tangente))

