from mininet.net import Mininet
from mininet.node import Controller, OVSKernelAP
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink
from mininet.wifi.node import OVSKernelAP
from mininet.wifi.cli import CLI as WiFiCLI
from mininet.wifi.net import Mininet_wifi
from mininet.wifi.mobility import mobility
import time

def myNetwork():
    net = Mininet_wifi(controller=Controller, accessPoint=OVSKernelAP, link=TCLink)

    print("*** Creating nodes")
    
    ap1 = net.addAccessPoint('ap1', ssid='DI524_AP1', mode='g', channel='1', failMode='standalone', encryption='wpa2', range=35, position='10,10,0')
    ap2 = net.addAccessPoint('ap2', ssid='DI524_AP2', mode='g', channel='6', failMode='standalone', encryption='wpa2', range=35, position='30,10,0')
    ap3 = net.addAccessPoint('ap3', ssid='DI524_AP3', mode='g', channel='11', failMode='standalone', encryption='wpa2', range=35, position='50,10,0')
    ap4 = net.addAccessPoint('ap4', ssid='DI524_AP4', mode='g', channel='1', failMode='standalone', encryption='wpa2', range=35, position='70,10,0')
    ap5 = net.addAccessPoint('ap5', ssid='DI524_AP5', mode='g', channel='6', failMode='standalone', encryption='wpa2', range=35, position='90,10,0')

    # Stations
    sta1 = net.addStation('sta1', ip='10.0.0.1/24', position='0,0,0')
    sta2 = net.addStation('sta2', ip='10.0.0.2/24', position='0,0,0')
    sta3 = net.addStation('sta3', ip='10.0.0.3/24', position='0,0,0')
    sta4 = net.addStation('sta4', ip='10.0.0.4/24', position='0,0,0')
    sta5 = net.addStation('sta5', ip='10.0.0.5/24', position='0,0,0')

    print("*** Configuring wifi nodes")
    net.configureWifiNodes()

    print("*** Creating links")
    net.addLink(ap1, ap2)
    net.addLink(ap2, ap3)
    net.addLink(ap3, ap4)
    net.addLink(ap4, ap5)

    net.addLink(sta1, ap1)
    net.addLink(sta2, ap2)
    net.addLink(sta3, ap3)
    net.addLink(sta4, ap4)
    net.addLink(sta5, ap5)

    print("*** Starting network")
    net.build()
    net.start()

    print("*** Applying mobility")
    mobility(sta1, 'start', time=10000, position='10,10,0')
    mobility(sta1, 'stop', time=20000, position='30,10,0', min_v=1, max_v=5)

    mobility(sta2, 'start', time=30000, position='10,10,0')
    mobility(sta2, 'stop', time=60000, position='50,10,0', min_v=5, max_v=5)

    mobility(sta3, 'start', time=25000, position='10,10,0')
    mobility(sta3, 'stop', time=60000, position='70,10,0', min_v=7, max_v=7)

    mobility(sta4, 'start', time=10000, position='10,10,0')
    mobility(sta4, 'stop', time=20000, position='30,10,0', min_v=1, max_v=10)

    mobility(sta5, 'start', time=10000, position='10,10,0')
    mobility(sta5, 'stop', time=20000, position='50,10,0', min_v=1, max_v=10)

    print("*** Running CLI")
    WiFiCLI(net)

    print("*** Stopping network")
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    myNetwork()