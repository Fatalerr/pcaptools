#! coding: utf-8
"""
QoS Info Description
QCI:
PCI - Pre-emption Capability, 1->disable, 0->enable
PVI - Pre-emption Vulnerability, 1->disable, 0->enable
PL  - Priority level.
AMBR_UL - AMBR upload
AMBR_DL - AMBR download
"""
from datetime import datetime
#### Mandatory Parameters #####
display_filter = 'gtpv2'

### Optional Parameters #####
data_fields = ["TIME", "MSISDN", "QCI", "PCI", "PVI",'PL','AMBR_UL','AMBR_DL']
output_template = "{time:%Y-%m-%d %H:%M:%S}\t{msisdn:15s}\t{qci}\t{pci}\t{pvi}\t{pl}\t{ambr_ul}\t{ambr_dl}"

### Mandatory Callback Function
## - extractor
## - output

def extractor(pkt):
    data = {}
    data['time'] = pkt.sniff_time
    data['stream'] = pkt.udp.get('stream')    
    data['msisdn'] = pkt.gtpv2.get('e164.msisdn','n/a')
    data['qci'] = pkt.gtpv2.get('bearer_qos_label_qci')
    data['pci'] = pkt.gtpv2.get('bearer_qos_pci')
    data['pvi'] = pkt.gtpv2.get('bearer_qos_pvi')
    data['pl'] = pkt.gtpv2.get('bearer_qos_pl')    
    data['ambr_ul'] = pkt.gtpv2.get('ambr_up')
    data['ambr_dl'] = pkt.gtpv2.get('ambr_down') 
    
    return data
   
def output(pkts_data, pcap_filename):
    "pkts_data is a list of packet's info data"
    buf=[]
    buf.append(f"\nQoS Info: '{pcap_filename}'")
    buf.append("{:20s}\t{:15s}\t{}\t{}\t{}\t{}\t{}\t{}".format(*data_fields))
    buf.append("-"*90)
    for pkt in pkts_data:
        if pkt.get('qci'):
            buf.append(output_template.format(**pkt))
    #buf.append('\n')
    print("\n".join(buf))