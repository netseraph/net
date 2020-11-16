import netmodule
import threading
import IPy


def ipscan_threading(ip, maxport):
    try:
        print('开始扫描%s开放端口' % ip)
        threadlist = []
        for i in range(maxport):
            t = threading.Thread(target=netmodule.getportstatus, args=(ip, i))
            threadlist.append((i, t))
            t.start()
            t.join()
        for item in threadlist:
            # item[1].join()
            print(item[0], item[1].get_result())
    except Exception as e:
        print('扫描%s出错' % (ip), e)


if __name__ == '__main__':
    localip = netmodule.gethostip()
    net = localip+'/24'
    iplist = IPy.IP(net, make_net=True)
    maxport = 65535
    for item in iplist:
        s = netmodule.getonlinestatus(str(item))
        if s:
            print(item, '在线！')
            ipscan_threading(str(item), maxport)
        else:
            print(item, '不在线！')
