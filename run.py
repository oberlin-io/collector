import collectors
import storage

storage.append(
    collectors.machine.cpu(),
    '../data/cpu.csv',
    )

