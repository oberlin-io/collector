import os
import yaml

class AuthLog():

    def __init__(self, config):
        
        with open('../var.yaml', 'r') as f:
            self.var = yaml.safe_load(f.read())

        self.authlog_path = config['authlog_path']


    def watch_authlog(self):
        """By monitoring file last modified and tracking most recent index."""
        
        self.new_last_mod = os.path.getmtime(self.authlog_path)
    
        if self.new_last_mod > self.var['authlog_last_mod']:
            return True
        else:
            return False
    
    
    def set_authlog():
        
        with open(authlog_path) as f:
            self.authlog = f.readlines()[var['authlog_index']:]


    def set_last_mod(self):

        self.var['authlog_last_mod'] = self.new_last_mod
        
        with open('../var.yaml', 'w') as f:
            f.write(yaml.dump(self.var))


    def get_user_session(self):
        
        pat = re.compile(r'^(\w{3}\s{2}\d+\s\d{2}:\d{2}:\d{2})\s.+systemd-logind\[(\d+)\]:\s.+user\s(\w+)\s.+uid=(\d+)')

        for line in self.auth.readlines():
            if 'systemd-logind[' in line:
                m = pat.match(line)
                
