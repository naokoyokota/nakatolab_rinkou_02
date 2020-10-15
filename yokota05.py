#yokota05.property
#python yokota05.py 20201009_nakato_testdata/file1 20201009_nakato_testdata/file2 20201009_nakato_testdata/file3 new_PDF_name.pdf
import os
import sys
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import glob

#read csv files
def read_file(file_1, file_2, file_3):
    df1 = pd.read_csv(file_1, sep='\t', skiprows=6, index_col='Strand shift')
    df2 = pd.read_csv(file_2, sep='\t', skiprows=6, index_col='Strand shift')
    df3 = pd.read_csv(file_3, sep='\t', skiprows=6, index_col='Strand shift')

    return df1, df2, df3

# extract legend name except ".jaccrd.csv"
def legend_name(file_1, file_2, file_3):
    filename_list = [file_1, file_2, file_3]
    legend_list = []
    for f in filename_list:
        name = os.path.basename(f)
        legend_list.append(name.split(".", 1)[0])

    return legend_list

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file1", help="file1 path", type=str)
    parser.add_argument("file2", help="file2 path", type=str)
    parser.add_argument("file3", help="file3 path", type=str)
    parser.add_argument("newfile", help="new file name", type=str)

    args = parser.parse_args()

    file_1 = args.file1
    file_2 = args.file2
    file_3 = args.file3
    newfile = args.newfile

    print('file1: %s' % file_1)
    print('file2: %s' % file_2)
    print('file3: %s' % file_3)
    print('new_file_name: %s' % newfile)

df1, df2, df3 = read_file(file_1, file_2, file_3)
legend_list = legend_name(file_1, file_2, file_3)

# 3サンプルを重ねて可視化
plt.figure(figsize=(4,4))
plt.plot(df1.iloc[:,3], label=legend_list[0], color="red")
plt.plot(df2.iloc[:,3], label=legend_list[1], color="blue")
plt.plot(df3.iloc[:,3], label=legend_list[2], color="black")
plt.xlim(0,500)
plt.xlabel("index")
plt.ylabel("per control")
plt.legend(loc='upper right')
plt.savefig(newfile)
