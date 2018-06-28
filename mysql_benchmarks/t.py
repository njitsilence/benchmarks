import numpy as np
import json
dir = r'C:\bm_test\mysql\all_results.json'

with open(dir,'r') as f:
    dt = json.loads(f.read())
    all_time = np.array(dt['insert_elapse_time_list']).sum()

    print(all_time)