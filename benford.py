import matplotlib.pyplot as plt
import numpy as np
log10=np.log10
import random
'''
x=np.linspace(1,9,100)
plt.plot(x,log10(x))
plt.plot(x,log10(x+1))
plt.plot(x,log10(1+1/x))
plt.grid()
plt.title('Loi de Benford')
#plt.show()
'''
max=10000
freq=[0]*10
print(freq)
for k in range(100):
	p=1
	for m in range(np.random.randint(5,10)):
		p*=np.random.randint(1,max)
	f=int(str(p)[0])
	freq[f]+=1
print(freq)
x=[i for i in range(1,10)]
plt.bar(x,freq[1:])
plt.show()