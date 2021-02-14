import os
from datetime import datetime as dt
import re


def cpu(cpu_no):

    return (
        dt.now().strftime('%Y-%m-%d %H:%M:%S'),
    
        str(
            round(
                (100 - \
                float(
                    re.findall(
                        '\d+\.\d+',
                        os.popen('mpstat') \
                            .read() \
                            .splitlines()[cpu_no + 2]
                        )[-1]
                    )
                ) / 100,
                4,
                )
            )
        )


def memory():

    t = dt.now().strftime('%Y-%m-%d %H:%M:%S')
    
    read = re.findall(
        '\d+',
        os.popen('free') \
            .read() \
            .splitlines()[1]
        )
        
    v = str(
            round(
                int(read[1]) / int(read[0]),
                4
            )
        )

    return (t, v)


        
