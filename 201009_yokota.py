import os
import sys
import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# main関数を定義 (to increase readability)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="show partial lines of file")
    parser.add_argument("file1", help="file1 path", type=str)
    parser.add_argument("file2", help="file2 path", type=str)
    parser.add_argument("file3", help="file3 path", type=str)

    args = parser.parse_args()

    filename1 = args.file1
    filename2 = args.file2
    filename3 = args.file3

    print('file1: %s' % filename1)
    print('file2: %s' % filename2)
    print('file3: %s' % filename3)

def read_file():
    df1 = pd.read_csv("20201009_nakato_testdata/filename1", sep='\t', skiprows=6, index_col='Strand shift')
    df2 = pd.read_csv("20201009_nakato_testdata/filename2", sep='\t', skiprows=6, index_col='Strand shift')
    df3 = pd.read_csv("20201009_nakato_testdata/filename3", sep='\t', skiprows=6, index_col='Strand shift')


# 3サンプルを重ねて可視化
    df1 = pd.read_csv("20201009_nakato_testdata/filename1", sep='\t', skiprows=6, index_col='Strand shift')
    df2 = pd.read_csv("20201009_nakato_testdata/filename2", sep='\t', skiprows=6, index_col='Strand shift')
    df3 = pd.read_csv("20201009_nakato_testdata/filename3", sep='\t', skiprows=6, index_col='Strand shift')
    pc1 = df1["per control"]
    pc1_new=pc1.rename(columns={ "per control":"filename1"})
    pc2 = df2["per control"]
    pc2_new=pc2.rename(columns={"per control": "filename2"})
    pc3 = df3["per control"]
    pc3_new=pc3.rename(columns={"per control": "filename3"})
    df_concat = pd.concat([pc1_new, pc2_new, pc3_new],axis=1)
    print(df_concat)
    df_mean=df_concat.mean(axis='columns')

    plt.figure(figsize=(4,4))
    plt.plot(df1["per control"], label="E01", color="red")
    plt.plot(df2["per control"], label="E02", color="blue")
    plt.plot(df3["per control"], label="E03", color="black")
    plt.plot(df_mean, label="mean", color="green")
    plt.xlim(0,500)
    plt.ylim(0,4)
    plt.legend(loc='upper right')
    plt.savefig("yokota.pdf")
