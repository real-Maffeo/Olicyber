import pyshark

# Path al file pcap
capture_file = '/home/sergio/ProgettiProgrammazione/Python/CyberChallenge/CHAOS/CHAOS.pcap'

# filtro che vogliamo applicare
display_filter = 'tcp.analysis.retransmission'

# lista dei payload
payloads = []

# in questo caso prendo il valore del payload tcp
def extract_payload(packet):
    try:
        return packet.tcp.payload.raw_value
    except AttributeError:
        return None

# apro il pcap
cap = pyshark.FileCapture(capture_file, display_filter=display_filter)

packet_list = []

# salvo i pacchetti in una lista per poterli ordinare in ordine cronologico
for packet in cap:
    packet_list.append(packet)
#ordino i pacchetti in ordine cronologico
packet_list.sort(key=lambda packet: packet.sniff_time)

# estraggo i payload
for packet in packet_list:
    payload = extract_payload(packet)
    if payload is not None:
        payloads.append(payload)

# chiudo il pcap
cap.close()

flag = ""
# appendo i payload in una stringa
for idx, payload in enumerate(payloads, start=1):
    flag+= chr(int(payload, 16))
print(flag)
