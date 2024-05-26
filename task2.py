from mininet.net import Mininet
from mininet.node import Controller, OVSKernelAP
from mininet.cli import CLI
from mininet.link import TCLink

def create_topology():
    net = Mininet(controller=Controller, accessPoint=OVSKernelAP, link=TCLink)
    
    # Add controller
    c0 = net.addController('c0')

    # Add nodes
    adhoc1 = net.addHost('adhoc1', mac='00:00:00:00:00:01', ip='192.168.1.1/24', position='20,5,0')
    adhoc2 = net.addHost('adhoc2', mac='00:00:00:00:00:02', ip='192.168.1.2/24', position='20,5,0')
    adhoc3 = net.addHost('adhoc3', mac='00:00:00:00:00:03', ip='192.168.1.3/24', position='20,5,0')
    adhoc4 = net.addHost('adhoc4', mac='00:00:00:00:00:04', ip='192.168.1.4/24', position='20,5,0')
    adhoc5 = net.addHost('adhoc5', mac='00:00:00:00:00:05', ip='192.168.1.5/24', position='20,5,0')
    adhoc6 = net.addHost('adhoc6', mac='00:00:00:00:00:06', ip='192.168.1.6/24', position='20,5,0')

    # Add switches
    ap1 = net.addAccessPoint('ap1', ssid='adhoc', mode='g', channel='1',
                             position='20,5,0', range='30', antennaHeight='1', antennaGain='5')
    
    # Add links
    net.addLink(adhoc1, ap1)
    net.addLink(adhoc2, ap1)
    net.addLink(adhoc3, ap1)
    net.addLink(adhoc4, ap1)
    net.addLink(adhoc5, ap1)
    net.addLink(adhoc6, ap1)

    # Start the network
    net.build()
    c0.start()
    ap1.start([c0])

    # Assign IP addresses
    adhoc1.cmd('ifconfig adhoc1-eth0 192.168.1.1 netmask 255.255.255.0')
    adhoc2.cmd('ifconfig adhoc2-eth0 192.168.1.2 netmask 255.255.255.0')
    adhoc3.cmd('ifconfig adhoc3-eth0 192.168.1.3 netmask 255.255.255.0')
    adhoc4.cmd('ifconfig adhoc4-eth0 192.168.1.4 netmask 255.255.255.0')
    adhoc5.cmd('ifconfig adhoc5-eth0 192.168.1.5 netmask 255.255.255.0')
    adhoc6.cmd('ifconfig adhoc6-eth0 192.168.1.6 netmask 255.255.255.0')

    # Start the CLI
    CLI(net)

    # Stop Mininet
    net.stop()

if __name__ == '__main__':
    create_topology()
