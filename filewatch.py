import yaml
import os


class FileWatch():


    def __init__(self, filepath):
        
        self.filepath = filepath
        self.is_modified = False


    def check(self):

        with open('var.yaml') as f:
            self.var = yaml.safe_load(f.read())
            
        x = os.path.getmtime(self.filepath)

        if x > self.var['authlog_last_mod']:
            self.is_modified = True
            self.var['authlog_last_mod'] = x

        else:
            self.is_modified = False


    def get(self):

        return (self.var['authlog_last_mod'], self.is_modified)


    def to_var(self):

        with open('var.yaml', 'w') as f:
            f.write(yaml.dump(self.var))
