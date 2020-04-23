#! coding: utf-8
"""pcap info extractor 

Usage: python -m pcaptools.extract <finder>  <pcap file or directory>

"""
import logging
from pathlib import Path
from importlib import import_module
from . import PcapFile

from .finders import FinderList

__author__ = "weyjun.com"
__version__ = '0.1'

if __name__ == "__main__":
    import sys
    
    try:
        confile_name  = sys.argv[1]
        file_or_dir = Path(sys.argv[2])
    except IndexError:
        print(__doc__)
        sys.exit(1)
        
    conf = FinderList.get(confile_name)
        
    if not conf:
        conf = import_module(confile_name)
    
    #print('conf:', conf)
    
    if file_or_dir.is_dir():
        pcapfiles=file_or_dir.glob('*.pcap')
    else:
        pcapfiles = [file_or_dir]
    
    for pfile in pcapfiles:
        pcap = PcapFile(pfile, display_filter=conf.display_filter)

        data = pcap.apply(conf.extractor)
        conf.output(data, pfile)
    