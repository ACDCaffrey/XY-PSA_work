# This script determines the gates for XY-PSA and plots them
import matplotlib.pyplot as plt
import numpy as np

filename = 'aminusbdivaplusb.1' # select file here

with open(filename, 'r') as f:
    read_data = f.read()
    f.close()

read_data = read_data.split()
read_data = list(map(int,read_data))
total_data = 0
starting_bin = 0
ending_bin = 0
n = 0

# get the first and last bins containing data
for value in range(0,len(read_data)):

    if read_data[value] != 0:
        ending_bin = value

    if n == 0:
        if read_data[value] != 0:
            starting_bin = value - 1
            n = 1

    total_data = total_data + read_data[value]


events_in_bin = total_data/5 # 5 mm  pitch split into 1 mm bins

total_data = 0
cutoff_bins = [0]*5
n = 0
events = events_in_bin
for value in range(starting_bin,ending_bin):
     total_data = total_data + read_data[value]

     if total_data > events:
         cutoff_bins[n] = value
         n = n + 1
         events = events + events_in_bin

print(cutoff_bins)

x = np.arange(0,len(read_data)) # plots start here
plt.figure(facecolor = 'white')
plt.fill(x,read_data,'white')
plt.axvline(x = cutoff_bins[0], ymin = 0, ymax = max(read_data), color = 'r', linewidth = 2)
plt.axvline(x = cutoff_bins[1], ymin = 0, ymax = max(read_data), color = 'r', linewidth = 2)
plt.axvline(x = cutoff_bins[2], ymin = 0, ymax = max(read_data), color = 'r', linewidth = 2)
plt.axvline(x = cutoff_bins[3], ymin = 0, ymax = max(read_data), color = 'r', linewidth = 2)
plt.xlim(starting_bin - 40,ending_bin + 40)
plt.xlabel('\nAsymmetry Parameter', fontsize = 18)
plt.ylabel('Frequency\n', fontsize = 18)
plt.show()
