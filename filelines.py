import yaml


class FileLines():


    def __init__(self, metaname):

        self.metaname = metaname

        with open('meta.yaml') as f:
            self.meta = yaml.safe_load(f.read())


    def get_newindex(self):

        for line in self.lines:
            if line == self.meta[self.metaname]['recent_line']:
                return self.lines.index(line) + 1 

        return 0


    def get_newlines(self):

        with open(self.meta[self.metaname]['filepath']) as f:
            self.lines = f.read().splitlines()
        
        self.newlines = self.lines[self.get_newindex():]
        
        
        if len(self.newlines) < 0:
            self.meta[self.metaname]['recent_line'] = self.newlines[-1]

        return self.newlines


    def update_meta(self):

        with open('meta.yaml', 'w') as f:
            f.write(yaml.dump(self.meta))


    def reset_recentline(self):

        self.meta[self.metaname]['recent_line'] = None

        self.update_meta()
        
