#! coding: utf-8

import pyshark

__author__ = "weyjun.com"
__date__ = "2020-04-22"

def qos_info(pkt):
    data = {}
    data['qci'] = pkt.gtpv2.get('bearer_qos_label_qci')
    data['pci'] = pkt.gtpv2.get('bearer_qos_pci')
    data['stream'] = pkt.udp.get('stream')
    data['pvi'] = pkt.gtpv2.get('bearer_qos_pvi')
    
    return data
    
class DataExtractor(object):
    def __init__(self, fields_name=None):
        self.fields_name = fields_name
        
    def _filter(self, pkt):
        data = self.get_data(pkt)
    
class QosInfo(DataExtractor):
    def filter_data(self, pkt):
        pass

class PcapFile(object):
    def __init__(self, pcapfile=None, display_filter=None):
        self.filename = pcapfile
        self._packets = None
        
        if self.filename:
            self._packets = pyshark.FileCapture(str(self.filename), 
                                                display_filter=display_filter,
                                                tshark_path=None)
    
    def apply(self, data_filter):
        data = []
        
        def _filter(pkt):
            data.append(data_filter(pkt))
        
        self._packets.apply_on_packets(_filter)
        
        return data