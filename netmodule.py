import scapy.all
import IPy
import socket

#import os
#import sys


def gethostip():
    try:
        socketobj = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socketobj.connect(('8.8.8.8', 53))
        ip = socketobj.getsockname()[0]
    finally:
        socketobj.close()
    return ip


def getonlinestatus(ip):
    if ip!=gethostip():
        pkt = scapy.all.IP(dst=ip)/scapy.all.ICMP()
        res = scapy.all.sr1(pkt, timeout=0.1, verbose=0)
        if res:
            return True
        else:
            return False
    else:
        return True

def getportstatus(ip, port):
    # 扫描端口是否开放
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = s.connect_ex((ip, port))
        if(result == 0):
            status=True
        else:
            status=False    
        s.close()
        return status
    except Exception as e:
        print('扫描端口异常%s:%d' % (ip, port), e)


