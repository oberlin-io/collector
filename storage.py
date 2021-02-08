import os

class CSV():

    def __init__(self, filename):
        self.filename = filename
        self.name = filename.split('.')[0]

        self.filepath = os.path.join(
            'data',
            self.filename
        )
    

    def mk_file(self, headers):
        """Check if file exists. If not, makes it with headers via tuple."""
        
        self.headers = headers

        if not os.path.exists(self.filepath):
            with open(self.filepath, 'w') as f:
                f.write(','.join(self.headers) + '\n')
        
        #add else log and print file exists


    def append_csv(self, data):
        
        with open(self.filepath, 'a') as f:
            f.write(','.join(data) + '\n')
