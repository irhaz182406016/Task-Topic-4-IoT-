import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

# load datasheet
data = pd.read_csv('4.csv')  # Adjust the file path if necessary

# pilih kolom
raw_data = data.iloc[:, 1]

# definikana fungsi mva
def moving_average(data, window_size):
    return data.rolling(window=window_size, min_periods=1).mean()

# set ukuran window untuk mva filter
window_sizes = [5, 10, 15]

# Apply the moving average filter
mva_filtered_data = moving_average(raw_data, window_size)

#buat subplot untuk pembanding
plt.figure(figsize=(15, 6))
for i, window_size in enumerate(window_sizes):
    mva_filtered_data = moving_average(raw_data, window_size)

# visualisasikan hasil dalam grafik
  plt.subplot(1, len(window_sizes), i+1)
    plt.plot(raw_data, label='Raw Data')
    plt.plot(mva_filtered_data, label=f'MVA Data (window={window_size})')
    plt.legend()
    plt.title(f'Raw Data vs. MVA Data (Window={window_size})')
    plt.xlabel('Sample Index')
    plt.ylabel('Acceleration')

plt.show()
