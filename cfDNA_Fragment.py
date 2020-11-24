import random

class Fragment:
    """""
    A class used to represent a cfDNA fragment
    ...
    
    Attributes
    ----------
    barcode : int
        a unique randomly-generated number used to identify fragment
        
    location : int
        position of fragment within the genome; assume all fragments are mapped to the same location for now

    Methods
    -------
    ligation()
        Link a unique molecular barcode to fragment
    

    """""
    barcode = 1 # each fragment's barcode is represented by a single integer

    def __init__(self):

        self.barcode = None
        self.location = None # disregarded for now

    def ligation(self):
        self.barcode = Fragment.barcode
        Fragment.barcode += 1

