import requests
import os

os.chdir(r'C:\Users\EricKim\Documents\konosuba14')

base = 'https://i2.wp.com/goodsworkspace.com/wp-content/uploads/2019/02/%EC%BD%94%EB%85%B8%EC%8A%A4%EB%B0%9414_'

temp = [str(i) for i in range(0, 274)]

new = []

for item in temp:
    if len(item) == 1:
        new.append('00' + item)
    if len(item) == 2:
        new.append('0' + item)
    if len(item) == 3:
        new.append(item)


for item in new:
    url = base + item + '.jpg'
    filename = url.split('/')[-1]
    r = requests.get(url, allow_redirects=True)
    open(filename, 'wb').write(r.content)



'April 29, 1-2PM'

'Predicting drill bit failure before 15 min it does.'
