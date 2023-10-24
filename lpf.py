import pandas as pd
import numpy as np
from scipy.signal import butter, lfilter
import matplotlib.pyplot as plt 

# load datasheet
data = pd.read_csv('4.csv')  # Adjust the file path if necessary

# Select the relevant column (column at index 1 for X-axis)
raw_data = data.iloc[:, 1]

# definisikan fungsi filter the low-pass
def butter_lowpass(cutoff, fs, order=5):
    nyquist = 0.5 * fs
    normal_cutoff = cutoff / nyquist
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def butter_lowpass_filter(data, cutoff, fs, order=5):
    b, a = butter_lowpass(cutoff, fs, order=order)
    y = lfilter(b, a, data)
    return y

# Set the frekuensi filter cutoff and sample rate
cutoff_frequency = 14.0  
sample_rate = 100.0  

# jalankan low-pass filter
filtered_data = butter_lowpass_filter(raw_data, cutoff_frequency, sample_rate)

# visualisasi raw_data dan filtered_data dalam grafik
plt.figure(figsize=(10, 6))
plt.plot(raw_data, label='Raw Data')
plt.plot(filtered_data, label='LPF Data')
plt.legend()
plt.title('Raw Data vs. LPF Data (X-axis)')
plt.xlabel('Sample Index')
plt.ylabel('Acceleration')
plt.show()
