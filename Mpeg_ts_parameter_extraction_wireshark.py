import pyshark
import concurrent


capture = pyshark.FileCapture('D:/RVS2XXVW11_module/CVC/X055/X055_rc1_mpegts.pcapng',
                              decode_as={'udp.port==42800': 'rtp'})
status = 0
for cap in capture:
    if cap.mp2t.afc == "3":
        print(cap.mp2t.afc)
        print("PES PID:", cap.mp2t.pid)
        print("PCR flag:", cap.mp2t.af_pcr_flag)
        print("PCR Timestamp:", cap.mp2t.af_pcr)
        status = 1
        capture.close()
        break
    if cap.mp2t.afc == "2":
        print(cap.mp2t.afc)
        print("PES PID:", cap.mp2t.pid)
        print("PCR flag:", cap.mp2t.af_pcr_flag)
        print("PCR Timestamp:", cap.mp2t.af_pcr)
        status = 1
        capture.close()
        break
    if cap.mp2t.afc == "1":
        print(cap.mp2t.afc)


print(status)
