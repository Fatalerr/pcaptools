#! coding: utf-8

from importlib import import_module
from pathlib import Path
from . import PcapFile

__author__ = "weyjun.com"

if __name__ == "__main__":
    import sys
    
    confile_name = sys.argv[1]
    file_or_dir = Path(sys.argv[2])
    
    conf = import_module(confile_name)
    
    if file_or_dir.is_dir():
        pcapfiles=file_or_dir.glob('*.pcap')
    else:
        pcapfiles = [file_or_dir]
    
    for pfile in pcapfiles:
        #print(f"extract data from file: '{pfile}'...")
        pcap = PcapFile(pfile, display_filter=conf.display_filter)

        data = pcap.apply(conf.extractor)
        conf.output(data, pfile)
    