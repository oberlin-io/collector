from collectors import machine
from collectors import filelines
from collectors import logs
import time
import pandas as pd

#import storage
#import config
#import filewatch


FL_authlog = filelines.FileLines('authlog')
FL_syslog = filelines.FileLines('syslog')


html = '''<html>
<head>
  <meta http-equiv='refresh' content='10'>
  <style>
    body {font-family: monospace;}
  </style>
</head>
<body>
<h3>CPU usage</h3>
#cpu
<h3>Memory usage</h3>
#memory
<br>
<h3>Invalid users</h3>
#invaliduser
<br><br>
</body></html>
'''

while True:
    
    authlog_lines = FL_authlog.get_newlines()
    FL_authlog.update_meta()    
    #for line in authlog_lines:
    #    print(f'[Authlog] {line}')
    authlog_data = logs.authlog_invaliduser(authlog_lines)
    with open('data/authlog_invaliduser.csv', 'a') as f:
        f.write(pd.DataFrame(authlog_data).to_csv(header=False, index=False))

    #syslog_lines = FL_syslog.get_newlines()
    #FL_syslog.update_meta()    
    #for line in syslog_lines:
    #    print(f'[Syslog ] {line}')

    cpudata = machine.cpu(1)
    #print(f'[CPU 1  ] {data}')

    memorydata = machine.memory()
    #print(f'[Memory ] {data}')
    
    #print('- - -   - - -')
    
    

    X = pd.read_csv('data/authlog_invaliduser.csv')
    X.drop_duplicates(inplace=True)
    X.sort_values(by='timestamp', ascending=False, inplace=True)
    X_html = X.to_html(index=False)
    html_final = html.replace('#invaliduser', X_html)

    fullbar = 70
    cpudatabar = int(round(float(cpudata[1]) * fullbar, 0))
    bar = '[' + '█'*cpudatabar + '░'*(fullbar-cpudatabar) + '] ' + str(round(float(cpudata[1])*100, 2)) + '%'
    html_final = html_final.replace('#cpu', bar)
    
    databar = int(round(float(memorydata[1]) * fullbar, 0))
    bar = '[' + '█'*databar + '░'*(fullbar-databar) + '] ' + str(round(float(memorydata[1])*100,2)) + '%'
    html_final = html_final.replace('#memory', bar)
    
    with open('/var/www/html/index.html', 'w') as f:
         f.write(html_final)


    time.sleep(10)


exit()
# # #

conf = config.get()

auth_fw = filewatch.FileWatch(conf['authlog_path'])

CSV_memory = storage.CSV('memory.csv')
CSV_memory.mk_file(('_time','percent_usage'))

CSV_cpu_1 = storage.CSV('cpu_1.csv')
CSV_cpu_1.mk_file(('_time','percent_usage'))

while True:
        
    auth_fw.check()
    fw_status = auth_fw.get()
    if fw_status[1] is True:
        auth_fw.to_var()
        #logs.()
        print(f"{auth_fw.filepath} modified at {auth_fw.var['authlog_last_mod']}")
    
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


