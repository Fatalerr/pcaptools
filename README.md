pcaptools
===============

A convenient tool for pcap file analysis and extracting

## Information Extractor

extract the information you need and output as a format text.

Usage:

> python -m pcaptools.extract <finder> <pcap_file_or_directory>

**Example:**
let's say there are some `pcap` files under the directory `epc_pcap` which captured 
from EPC S11. you need to extract QoS info from all the files.

 * extract the Qos info from a single `pcap` file:
 
```
# python -m pcaptools.extract qos_info epc_pcap/pgw01.pcap 

QoS Info: 'epc_pcap/pgw01.pcap'
TIME                    MSISDN          QCI     PCI     PVI     PL      AMBR_UL AMBR_DL
------------------------------------------------------------------------------------------
2020-04-15 14:07:16     8619280843419   9       1       0       6       2097152 2097152
2020-04-15 14:07:29     8619280843419   9       1       0       6       2097152 2097152
2020-04-15 14:10:54     8619280843419   9       1       0       6       2097152 2097152
```

 * extract the QoS info from all `pcap` files in a directory:
 
 ```
# python -m pcaptools.extract qos_info epc_pcap

QoS Info: 'epc_pcap/pgw01.pcap'
TIME                    MSISDN          QCI     PCI     PVI     PL      AMBR_UL AMBR_DL
------------------------------------------------------------------------------------------
2020-04-15 14:07:16     8619280843419   9       1       0       6       2097152 2097152
2020-04-15 14:07:29     8619280843419   9       1       0       6       2097152 2097152
2020-04-15 14:10:54     8619280843419   9       1       0       6       2097152 2097152

QoS Info: 'epc_pcap\msisdn_8619388432909_200422_0241.pcap'
TIME                    MSISDN          QCI     PCI     PVI     PL      AMBR_UL AMBR_DL
------------------------------------------------------------------------------------------
2020-04-22 10:41:18     8619388432909   9       1       0       6       78644   314573
2020-04-22 10:41:19     n/a             9       1       0       9       None    None
2020-04-22 10:41:19     8619388432909   5       0       1       1       10240   10240

QoS Info: 'epc_pcap\msisdn_8619366474065_200419_1024.pcap'
TIME                    MSISDN          QCI     PCI     PVI     PL      AMBR_UL AMBR_DL
------------------------------------------------------------------------------------------
2020-04-19 18:26:11     8619366474065   9       1       0       6       2097152 2097152
2020-04-19 18:46:20     8619366474065   9       1       0       6       2097152 2097152

QoS Info: 'epc_pcap\msisdn_8619366474065_200420_0240(1).pcap'
TIME                    MSISDN          QCI     PCI     PVI     PL      AMBR_UL AMBR_DL
------------------------------------------------------------------------------------------
2020-04-20 10:57:18     8619366474065   9       1       0       6       2097152 2097152
2020-04-20 11:00:18     8619366474065   9       1       0       6       2097152 2097152
2020-04-20 11:04:22     8619366474065   9       1       0       6       2097152 2097152
```

