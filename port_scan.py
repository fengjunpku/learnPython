# -*- coding: utf-8 -*-

import sys
from socket import *
import threading

# port_scan.py <host> <start_port>-<end_port>

def scan(ip,port):
  sock = socket(AF_INET, SOCK_STREAM)
  sock.settimeout(10)
  result = sock.connect_ex((ip, port))
  if result == 0:
    print "%s : %s"%(ip,port)



  # for port in range(start_port, end_port):
    # sock = socket(AF_INET, SOCK_STREAM)
    # sock.settimeout(1)
    # result = sock.connect_ex((target_ip, port))
    # if result == 0:
        # opened_ports.append(port)

if __name__ == "__main__":
  host = sys.argv[1]
  portstrs = sys.argv[2].split('-')

  start_port = int(portstrs[0])
  end_port = int(portstrs[1])

  target_ip = gethostbyname(host)
  opened_ports = []
  
  for port in range(start_port, end_port):
    thread = threading.Thread(target = scan, args = (target_ip,port))
    thread.start()
    thread.join(3)