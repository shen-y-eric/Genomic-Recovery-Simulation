import numpy as np
import random
from cfDNA_Fragment import Fragment

class FragmentCopies:

    """
A class used to represent and run the assay process
...
Attributes
----------
fragment_copies : list
    A storage of Fragment objects that is used for each step of the process

Methods
-------
cfDNA_convert(input = 15, genomic_equivalent = 330)
    Converts the cfDNA input amount (ng) into its genomic equivalent

ligation_process(lig_efficiency = 0.5)
    Link unique molecular barcodes to individual cfDNA fragments by running each fragment's ligation method

pcr(cycles = 8, pcr_efficiency = 1.8)
    PCR pre-amplification during library preparation before target enrichment

target_enrichment(panel_size = 200, capture_efficiency = 0.5, cycles = 12, pcr_efficiency = 1.8)
    Capture fragments within selected target regions and use PCR post-capture amplification

calculate():
    Count the number of unique cfDNA fragments after entire process and calculate GE recovery rate and duplication rate

    """
    fragment_amount_check = [] # Adds total fragment count to list after each simulation for graphing later
    unique_count_check = [] #  Adds unique fragment count to list after each simulation for graphing later
    ge_recovery_rate_check = [] # Adds GE recovery rate to list after each simulation for graphing later


    def __init__(self):

        self.fragment_copies = []

    def cfDNA_convert(self, input=15, genomic_equivalent=330):
        """
        Parameters
        ----------
        input : int
            cfDNA input amount (ng)
            Default = 15 ng

        genomic_equivalent : int
            Around 330 double stranded whole genome coverage per ng of cfDNA input
            Default = 330

        """

        for i in range(input * genomic_equivalent):
            fragment = Fragment()
            self.fragment_copies.append(fragment)

    def ligation_process(self):
        """
        Parameters
        ----------
        lig_efficiency : float
            Percentage of fragments that have unique barcode attached to them
            Default = 0.5

        """
        lig_efficiency = np.random.normal(0.5, 0.1)
        list_size, i = int(lig_efficiency * len(self.fragment_copies)), 0
        while i < list_size:
            self.fragment_copies.pop(random.randrange(0, len(self.fragment_copies)))
            i += 1

        for i in self.fragment_copies:
            i.ligation()

    def pcr(self, cycles=8, pcr_efficiency=np.random.normal(1.8, 0.1)):
        """
        Parameters
        ----------
        cycles : int
            Number of pcr cycles during pre-amplification
            Default = 8 cycles

        pcr_efficiency : float
            Percentage that each fragment will get amplified by
            Default = 1.8x
        """

        list_size, i, count = len(self.fragment_copies), 0, int(pcr_efficiency ** cycles)
        for i in range(list_size):
            for j in range(count):
                self.fragment_copies.append(self.fragment_copies[i])

    def target_enrichment(self, panel_size=200, capture_efficiency=0.5, cycles=12, pcr_efficiency=np.random.normal(1.8, 0.1)):
        """
        Parameters
        ----------
        panel_size : int
            Selected target region (kb) that fragments are captured from
            Default = 200 kb

        capture_efficiency : float
            Percentage of fragments that are captured within target region
            Default = 0.5

        cycles : int
            Number of pcr cycles during post-capture amplification
            Default = 12 cycles

        pcr_efficiency : float
            Percentage that each fragment will get amplified by
            Default = 1.8x
        """

        list_size, i = int(capture_efficiency * len(self.fragment_copies)), 0
        while i < list_size:
            self.fragment_copies.pop(random.randrange(0, list_size - 1))
            i += 1

        self.pcr_process(cycles, pcr_efficiency)

    def calculate(self):

        fragment_amount = len(self.fragment_copies)
        unique_count = len(set(x.barcode for x in self.fragment_copies))
        ge_recovery_rate = unique_count/(15*330)

        FragmentCopies.fragment_amount_check.append(fragment_amount)
        FragmentCopies.unique_count_check.append(unique_count)
        FragmentCopies.ge_recovery_rate_check.append(ge_recovery_rate)

