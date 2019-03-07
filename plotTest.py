#testing matplotlib

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import csv
import numpy as np
import datetime

f = open("decData.csv")
reader = csv.DictReader(f)

print(reader)

time = []
tsolar = []
px = []
mx = []
py = []
my = []

for row in reader:
    time.append(row['time'])
    tsolar.append(float(row['Total Solar']))
    px.append(float(row['+x']))
    mx.append(float(row['-x']))
    py.append(float(row['+y']))
    my.append(float(row['-y']))

print(time)
print(tsolar)

fig, ax1 = plt.subplots()
ax1.set_xlabel('time (s)')
ax1.set_ylabel('current')
ax1.plot(time, px, 'r--', label='+x')
ax1.plot(time, py, '',label='+y')
ax1.plot(time, mx, '',label='-x')
ax1.plot(time, my,'',label='-y')
ax1.plot(time, tsolar,'b--',label='total solar')
ax1.set_ylim(-100,400)

ax1.legend()

plt.savefig("data.png")
