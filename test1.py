
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

def convert_to_csv(FILEID):
    NUMERIC_COLUMNS = ['ts', 'orig_p', 'resp_p', "orig_bytes", "resp_bytes", "missed_bytes", "orig_pkts", 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'duration'] # integer columns
    LOGFILE = f"/Users/jonny/Downloads/opt/Malware-Project/BigDataset/IoTScenarios/CTU-IoT-Malware-Capture-{FILEID}-1/bro/conn.log.labeled"
    fieldsIN = ['ts', 'uid', 'orig_h', 'orig_p', 'resp_h', 'resp_p', 'proto', 'service', 'duration', 'orig_bytes', 'resp_bytes', 'conn_state',
            'local_orig', 'local_resp', 'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'tunnel_parents', 'label', 'detailed_label']
    df = pd.read_csv(LOGFILE, sep="\x09|\x20\x20\x20", skiprows=10, skipfooter=2,
                    names=fieldsIN, header=None, engine='python')
                            
    df = df.drop(['tunnel_parents'], axis=1)
    df.to_csv(f'csv/capture{FILEID}_1.csv')
    return df

convert_to_csv(1)