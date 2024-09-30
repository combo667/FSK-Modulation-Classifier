import numpy as np
import struct
import matplotlib.pyplot as plt
import pandas as pd


file_path = 'rfd900_fsk_csv_files_fs_960KHz/rfd900_net25.csv'
fs = 960e3



IQ_data = pd.read_csv(file_path)
IQ_data = IQ_data.to_numpy()


nbins = 64
points = 128

start = 1
end = 480000
cnt = 1
while cnt<50:
    
    counts, xedges, yedges = np.histogram2d(IQ_data[start:start+(points-1),0], IQ_data[start:start+(points-1),1], bins=nbins)

    fig = plt.figure(figsize=(2.24, 2.24), dpi=100)  
    ax = fig.add_subplot(111)

    ax.imshow(counts, cmap='hot')



    ax.set_axis_off()

    plt.tight_layout(pad=0)

    plt.savefig(f"testFiles/test_{0+cnt}", bbox_inches='tight', pad_inches=0)


    #plt.show()
    plt.close(fig)

    
    start += points
    cnt+=1