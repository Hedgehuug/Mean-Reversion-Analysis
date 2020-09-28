import numpy as np
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.style.use("ggplot")
import morePractice as mp



i = 200
e = 0
plt.ion()
plt.show(block=True)
fig = plt.figure(figsize=(13,6))
ax = fig.add_subplot(111)


line1 = []
line2 = []
sx = []
sy = []
sy2 = []

while i > 0:
    sx.append(e)
    sy.append(mp.getOrderBook('ETH/USDT')['bids'][0][0])
    sy2.append(mp.getOrderBook('ETH/USDT')['asks'][0][0])
    line1, = ax.plot(sy,'-o')
    line2, = ax.plot(sy2,'-o')
    #line1.set_ydata()
    plt.pause(0.1)
    i = i-1
    e = e+1

