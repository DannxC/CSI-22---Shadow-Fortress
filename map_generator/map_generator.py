from PIL import Image
import numpy as np


mapnum = '01'
img = np.array(Image.open('map'+mapnum+'.png'))

pos = []
ini = ()
spikes = []

for i in range(len(img)):
    for j in range(len(img[i])):
        if(img[i][j][2] < 250 and img[i][j][3] > 250):
            pos.append([j,i])
        if(img[i][j][0] > 250):
            ini = (j,i)
        if(img[i][j][2] > 250):
            spikes.append([j,i])


for i in range(len(pos)):
    pos[i][0] -= ini[0]
    pos[i][1] -= ini[1]
for i in range(len(spikes)):
    spikes[i][0] -= ini[0]
    spikes[i][1] -= ini[1]


# take ini out of pos
pos.remove(list((0,0)))
# put ini at the beginning of pos
pos.insert(0, list((0,0)))


for i in range(len(pos)):
    pos[i] = tuple(pos[i])
for i in range(len(spikes)):
    spikes[i] = tuple(spikes[i])

# clear file
f = open('map'+mapnum+'.txt','w')
f.close()
f = open('map'+mapnum+'.txt','at')
for p in pos:
    f.write("%d,%d\n" % (p[0], p[1]))
f.close()
# clear file
f = open('map_spikes'+mapnum+'.txt','w')
f.close()
f = open('map_spikes'+mapnum+'.txt','at')
for p in spikes:
    f.write("%d,%d\n" % (p[0], p[1]))
f.close()


with open('map'+mapnum+'.txt') as f:
    data = f.readlines()
new_data = []
for d in data:
    #remove newline
    d = d[:-1]
    #transform string to int
    d = tuple(map(int, d.split(',')))
    new_data.append(d)

print(new_data)