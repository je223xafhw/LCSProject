
import pandas as pd
import socket
import struct
import numpy as np


def convert_ipv4(addr):
    return struct.unpack("!I", socket.inet_aton(addr))[0]

def con_proto(proto):
    protos = ['icmp', 'tcp', 'udp']
    return protos.index(proto)

def norm_df(df, split_into=None):
    """
    param: split_into [this is a percentage, how much of the dataset should be used]
    """
    assert 0 < split_into < 1, "Number must be percentage"
    df = df.replace('-', np.nan)
    df['orig_h'] = df['orig_h'].apply(convert_ipv4)
    df['resp_h'] = df['resp_h'].apply(convert_ipv4)
    # df = pd.get_dummies(df, columns=['proto'], dtype=int)
    df['proto'] = df['proto'].apply(con_proto)
    # print(dummies.head())
    df = df.drop(['Unnamed: 0','service', 'duration', 'missed_bytes', 'history', 'uid', 'conn_state', 'local_orig', 'local_resp', 'orig_ip_bytes', 'resp_ip_bytes', 'orig_pkts', 'resp_pkts', 'detailed_label', 'ts'], axis=1)
    df['label'] = (df['label'] == "Malicious").astype(int)
    # df['resp_bytes'] = df['resp_bytes'].apply(to_int)
    df = df.dropna()
    df['resp_bytes'] = df['resp_bytes'].astype(int)
    df['orig_bytes'] = df['orig_bytes'].astype(int)
    if (split_into): df = np.array_split(df.sample(frac=1), 1/split_into)[0]
    df = df.reset_index(drop=True)
    return df


def generate_dtypes():
    fields = ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto', 'service', 'duration', 'orig_bytes', 'resp_bytes', 'conn_state',
              'local_orig', 'local_resp', 'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'tunnel_parents', 'label', 'detailed-label']
    types = ['time', 'string', 'addr',
             'port', 'addr', 'port', 'enum', 'string', 'interval', 'count', 'count', 'string', 'bool', 'bool', 'count', 'string', 'count', 'count', 'count', 'count', 'string', 'string']
    print("{")
    for ft in zip(fields, types):
        print(f"\"{ft[0]}\":\"{ft[1]}\",")
    print("}")


def main():
    convert_to_csv()


if __name__ == '__main__':
    main()
