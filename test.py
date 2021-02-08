from collectors import machine
import storage

import time


CSV_memory = storage.CSV('memory.csv')
CSV_memory.mk_file(('_time','percent_usage'))

CSV_cpu_1 = storage.CSV('cpu_1.csv')
CSV_cpu_1.mk_file(('_time','percent_usage'))

while True:
    data = machine.memory()
    print('{}{}'.format(
        CSV_memory.name,
        data
        ))
    CSV_memory.append_csv(data)
    
    data = machine.cpu(1)
    print('{}{}'.format(
        CSV_cpu_1.name,
        data
        ))
    CSV_cpu_1.append_csv(data)
    
    time.sleep(5)


