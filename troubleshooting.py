from textfsm import TextFSM
from netmiko import ConnectHandler
from collections import namedtuple
from threading import Thread
import os

class Troubleshooting:
    def __init__(self) -> None:
        self._commandtuples = namedtuple('commandTuples', ['arp','ping'])
        self._textfsmtuples = namedtuple('textfsmTuples', ['arp','ping'])
        self._ct = self._commandtuples('display arp', 'ping')
        self._tt = self._textfsmtuples('display_arp', 'ping_ip' )
        self._thread_lis=[]
        self._result_lis = []

        
class Layer2Troubleshooting(Troubleshooting):

    def __init__(self) -> None:
        super().__init__()
       
    def arp_main_function(self,device,normal_ip_set):
        try:
            with ConnectHandler(**device) as connect:
                out = connect.send_command(self._ct.arp)
                temp = TextFSM(open(self._tt.arp))
                ip_mac_list = temp.ParseText(out)
                ip_set = {x[0] for x in ip_mac_list}
                lack_ip_set = normal_ip_set-ip_set
                if len(lack_ip_set):
                    self._result_lis.append((device['ip'], tuple(lack_ip_set)))            
        except:
            self._result_lis.append((device['ip']))
    def arp_judgment(self,*device_tuple):
        normal_ip_set={x['ip'] for x in device_tuple}
        if not isinstance(device_tuple,tuple):tuple(device_tuple)
        for device in device_tuple:
            t=Thread(target=self.arp_main_function,args=(device,normal_ip_set))
            t.start()
            self._thread_lis.append(t)
        for t in self._thread_lis:
            t.join()
        return self._result_lis
    
class Layer3Troubleshooting(Troubleshooting):
    def __init__(self) -> None:
        super().__init__()
    def ping_main_function(self,device,ip_tuple):
        try:
            with ConnectHandler(**device) as connect:
                for ip in ip_tuple:
                    out=connect.send_command(self._ct.ping+ip)
                    temp=TextFSM(open(self._tt.ping))
                    temp.ParseText(out)
        except:
            self._result_lis.append(device['ip'])
    def ping_judgment(self,device):
        pass
        
    



if  __name__ == '__main__':
    device_tuple=(
    {
        'device_type':'huawei',
        'ip':'192.168.1.1',
        'username':'admin',
        'password':'admin@123'
    },
    {
        'device_type':'huawei',
        'ip':'192.168.1.2',
        'username':'admin',
        'password':'admin@123'
    },
     {
        'device_type':'huawei',
        'ip':'192.168.1.3',
        'username':'admin',
        'password':'admin@123'
    },
     {
        'device_type':'huawei',
        'ip':'192.168.1.4',
        'username':'admin',
        'password':'admin@123'
    },
    )
    print(os.getcwd())
    os.chdir(r'C:\Users\30862\Desktop\netknife-main\Core\dev_file')

    p=Layer2Troubleshooting()
    g1=p.arp_judgment(*device_tuple)
    print(g1)