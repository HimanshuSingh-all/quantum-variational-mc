import numpy as np
import matplotlib.pyplot as plt
points =1000
np.random.seed()
randompts = np.random.uniform(0,1,[points,2])
inpoints=0

for a in randompts:
    if np.linalg.norm(a)<=1:
        inpoints+=1

print(f'The value of pi is: {4*inpoints/points}')
theta = np.linspace( 0 ,np.pi/2,1000 )

def circ(theta,r=1):
    return r*np.vstack( [np.cos(theta), np.sin(theta)] ) 
cir = circ(theta)

fig,ax = plt.subplots(1)
plt.rcParams['font.family']='serif'

ax.plot(cir[0],cir[1], color = '#012fc8')
for a in randompts:
    if np.linalg.norm(a)<=1:
        ax.scatter(a[0],a[1], s=5, color='#1AA6B7')#'#D9ECF2')
    else:
        ax.scatter(a[0],a[1], s=5, color='#F56A79')
ax.set_aspect('equal', 'box')
ax.margins(x=0)
ax.margins(y=0)
ax.set_title(r'Calculation of $\pi$ Using Sampling')
fig.savefig("pi.png", dpi=300)

fig.tight_layout
