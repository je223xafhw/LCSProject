
import pandas as pd

def fetch_log(FILEID):
    LOGFILE = f"https://mcfp.felk.cvut.cz/publicDatasets/IoTDatasets/CTU-IoT-Malware-Capture-{FILEID}-1/bro/conn.log.labeled"
    # LOGFILE = f"/Users/jonny/Downloads/opt/Malware-Project/BigDataset/IoTScenarios/CTU-IoT-Malware-Capture-{FILEID}-1/bro/conn.log.labeled"
    fieldsIN = ['ts', 'uid', 'orig_h', 'orig_p', 'resp_h', 'resp_p', 'proto', 'service', 'duration', 'orig_bytes', 'resp_bytes', 'conn_state',
            'local_orig', 'local_resp', 'missed_bytes', 'history', 'orig_pkts', 'orig_ip_bytes', 'resp_pkts', 'resp_ip_bytes', 'tunnel_parents', 'label', 'detailed_label']
    return pd.read_csv(LOGFILE, sep="\x09|\x20\x20\x20", skiprows=10, skipfooter=2,
                    names=fieldsIN, header=None, engine='python')


def test_dfs():
    ids = [1,3,7,8,9,17,20,21,33, 34,35,36,39, 42,43,44,48,49,52,60]
    for id in ids:
        try:
            df = fetch_log(id)
            print(f"The {id} dataset has shape {df.shape} with {len(df[df['label'] == 'Malicious'])} malicious and {len(df[df['label'] == 'Benign'])} benign")
        except Exception as e:
            print(f"id {id} not working: {e}")
        df = None


        
        
test_dfs()