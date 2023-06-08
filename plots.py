import matplotlib.pylab as plt
# import tensorflow as tf
import pandas as pd
import seaborn as sns
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
import numpy as np

def make_bytes_plot(df) -> plt.figure:
    fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2, figsize=(12,12))
    range_for_ip_bytes = range(0, 100000, 10000)
    range_for_bytes = range(0, 100, 100)
    ax1.set_xticks(range_for_ip_bytes)
    ax1.set_yticks(range_for_ip_bytes)
    ax3.set_xticks(range_for_ip_bytes)
    ax3.set_yticks(range_for_ip_bytes)
    ax2.set_yticks(range_for_bytes)
    ax2.set_xticks(range(0, 100, 10))
    ax4.set_yticks(range_for_bytes)
    ax4.set_xticks(range(0, 100, 10))
    sns.scatterplot(data=df, x='orig_ip_bytes', y='resp_ip_bytes', hue='detailed_label', ax=ax1)
    sns.scatterplot(data=df, x='orig_ip_bytes', y='resp_ip_bytes', hue='proto', ax=ax3)
    sns.scatterplot(data=df, x='orig_bytes', y='resp_bytes', hue='detailed_label', ax=ax2)
    sns.scatterplot(data=df, x='orig_bytes', y='resp_bytes', hue='proto', ax=ax4)
    return fig

def make_port_plot(df):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(12,6))
    sns.scatterplot(data=df, x='orig_p', y='resp_p', hue='label', ax=ax1)
    sns.scatterplot(data=df, x='orig_p', y='resp_p', hue='proto', ax=ax2)
    return fig

def create_plots():
    FILEIDS = [1, 3, 36, 39, 49, 52]
    for FILEID in FILEIDS:
        df = pd.read_csv(f"csv/capture{FILEID}_1.csv")
        print(df.shape)
        make_bytes_plot(df)
        plt.savefig(f'img/plot_bytes_{FILEID}')
        make_port_plot(df)
        plt.savefig(f'img/plot_ports_{FILEID}')


def neighbors(df, fileid):
    neighb = NearestNeighbors(n_neighbors=2)
    nbrs = neighb.fit(df)
    distances, indices = nbrs.kneighbors(df)
    print(len(distances))
    distances = np.sort(distances, axis=0)
    plt.rcParams['figure.figsize'] = (12,6)
    plt.plot(distances)
    plt.savefig(f'img/plot_neigh_{fileid}.png')

def dbscan(df,fileid):
    dbscan = DBSCAN(eps=8, min_samples=4).fit(df)
    labels=dbscan.labels_
    plt.scatter(df[:, 0], df[:, 1], c=labels, cmap='plasma')
    plt.savefig(f'img/plotdbs_{fileid}.png')

def create_db_scans():
    FILEIDS = [1, 3, 36, 39, 49, 52]
    for FILEID in FILEIDS:
        df = pd.read_csv(f"csv/capture{FILEID}_1.csv")
        df = df.loc[:, ['orig_p', 'resp_p']].values
        dbscan(df, FILEID)

create_db_scans()