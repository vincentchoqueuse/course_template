import numpy as np

class Exporter():
    
    def __init__(self):
        self.name ="exporter"

    def get_context_data(self):
        data = []
        return data

    def save(self,filename="output.csv"):
        """cd do
        docstring
        """
        data = self.get_context_data()
        numpy.savetxt("foo.csv", data, delimiter=",",header="")
    