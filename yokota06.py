## testdata ディレクトリに含まれる全てのサンプルについて、１サンプルずつ per control(0~500 bp) のpdfを出力する
# Pythonスクリプト or シェルスクリプトを作成する。

import pandas as pd
from glob import glob
import matplotlib.pyplot as plt
import os

folder = input('Enter folder name: ')
dir=folder
print(dir)

for file in glob(dir + '/*.csv'):
    df = pd.read_csv(file, sep='\t', skiprows=6, index_col='Strand shift')
    file_name=os.path.basename(file).split('.', 1)[0]
    #plt.figure(figsize=(4,4))
    plt.plot(df["per control"], label=file_name, color="blue")
    plt.xlim(0,500)
    #plt.ylim(0,4)
    plt.legend(loc='upper right')
    pdf_name="pdf/" + file_name + ".pdf"
    plt.savefig(pdf_name)
    plt.close()
