
import pandas as pd
# import tensorflow as tf
FILE = '/Users/jonny/Documents/capture52_1.csv'
FILE2 = "/Users/jonny/Downloads/opt/Malware-Project/BigDataset/IoTScenarios/CTU-IoT-Malware-Capture-52-1/bro/conn.log.labeled"
SHUFFLE_BUFFER = 500
BATCH_SIZE = 2


def convert_to_csv():
    fieldsIN = ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto', 'service', 'duration', 'orig_bytes', 'resp_bytes', 'conn_state',
              'local_orig', 'local_resp', 'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'tunnel_parents', 'label', 'detailed-label']
    fieldsOUT = ['ts', 'uid', 'id.orig_h', 'id.orig_p', 'id.resp_h', 'id.resp_p', 'proto', 'service', 'duration', 'orig_bytes', 'resp_bytes', 'conn_state',
              'local_orig', 'local_resp', 'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'label']
    dtypes = {"ts": "int", "uid": "string", "id.orig_h": "string", "id.orig_p": "int", "id.resp_h": "string", "id.resp_p": "int", 
              "proto": "string", "service": "string", "duration": "string", "orig_bytes": "float", "resp_bytes": "int", "conn_state": "string",
              "local_orig": "string", "local_resp": "string", "missed_bytes": "int", "historyw": "string", "orig_pkts": "int", "orig_ip_bytes": "int", "resp_pkts": "int", "resp_ip_bytes": "int", "label": "string"}
    df = pd.read_csv(FILE2, sep='\x09', skiprows=10, skipfooter=2,
                     names=fieldsIN, header=None, engine='python', dtype=dtypes)
    df.to_csv('capture52_1.csv', columns=fieldsOUT)


def pandatry():
    dtypes = {"ts": "float", "uid": "string", "id.orig_h": "string", "id.orig_p": "int", "id.resp_h": "string", "id.resp_p": "int", 
              "proto": "string", "service": "string", "duration": "string", "orig_bytes": "float", "resp_bytes": "int", "conn_state": "string",
              "local_orig": "string", "local_resp": "string", "missed_bytes": "int", "history": "string", "orig_pkts": "int", "orig_ip_bytes": "int", "resp_pkts": "int", "resp_ip_bytes": "int", "tunnel_parents": "string", "label": "string"}
    df = pd.read_csv(FILE, encoding='big5hkscs', dtype=dtypes)
    # numeric_feature_names = ['age', 'thalach', 'trestbps',  'chol', 'oldpeak']
    # numeric_features = df[numeric_feature_names]
    # numeric_features.head()
    print(df.head())


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
