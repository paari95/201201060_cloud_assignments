from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost, OVSController
from mininet.link import TCLink
from mininet.cli import CLI
from mininet.util import irange,dumpNodeConnections
from mininet.log import setLogLevel , info



def topo():
        print "enter no of hosts per switch"	
        h=raw_input();
        h=int(h)
        print "enter no of switches"
        k=raw_input();
        k=int(k)
        switches = [] 
        odd_ip = '11.0.0.'
        even_ip = '11.0.1.'
        even_ctr = 1 
        odd_ctr = 1
        net = Mininet(host=CPULimitedHost, link=TCLink , controller=OVSController, autoStaticArp=True)
        info( '*** Adding controller\n' )
        net.addController('c0')
        
        for i in range(1, k+1):
            switch = net.addSwitch('s%s' % i)
            switches.append(switch)
            for j in range( 1, h+1 ):
                no=(i-1)*h+j
                if(no%2):
                    host=net.addHost('h%s' % ((i-1)*h+j) ,ip=odd_ip+str(odd_ctr)+'/24' )
                    odd_ctr+=1                    
                else:
                    host=net.addHost('h%s' % ((i-1)*h+j) ,ip=even_ip+str(even_ctr)+'/24' )
                    even_ctr+=1
                    
                net.addLink( host, switch, bw=no%2 + 1 )
		
        for i in range(0,len(switches)-1):
            net.addLink( switches[i], switches[i+1], bw=2)
		
        info( '*** Starting the Network and CLI\n' )	
        net.start()
        CLI(net)

        net.stop()

if __name__ == '__main__':
# Tell mininet to print useful information
	setLogLevel('info')
	topo();

