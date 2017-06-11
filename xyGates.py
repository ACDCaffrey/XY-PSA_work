# This script determines the gates to be set for XY-PSA

import matplotlib.pyplot as plt
import numpy as np
import glob

filename_key = 'aminusb*'

night = glob.glob(filename_key)
stored_ = np.zeros([len(night), 4])

for file_ in night:
    with open(file_, 'r') as f:
        read_data = f.read()
        f.close()

    plot_number = int(file_.split('.')[1]) - 1 # row in numpy array to store data
    read_data = read_data.split()
    read_data = list(map(int, read_data))
    if (np.sum(read_data) > 0):
        events_in_bin = np.sum(read_data)/5 # 5 mm  pitch split into 1 mm bins
        cumulative_list = np.cumsum(read_data)
        gate_values = np.array([1,2,3,4])
        gate_1 = np.where(cumulative_list > events_in_bin*gate_values[0])
        gate_2 = np.where(cumulative_list > events_in_bin*gate_values[1])
        gate_3 = np.where(cumulative_list > events_in_bin*gate_values[2])
        gate_4 = np.where(cumulative_list > events_in_bin*gate_values[3])
        stored_[plot_number,] = gate_1[0][0], gate_2[0][0], gate_3[0][0], gate_4[0][0]
print(stored_)
