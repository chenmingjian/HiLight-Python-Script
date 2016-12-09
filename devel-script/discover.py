import sys
import struct
import time
import socket

def discover(address, type = '', timeout = 1):
  rmdup = set()
  endtime = time.time() + timeout
  header = 'DISCOVER'
  data   = struct.pack('8s16s', header, type)
  addr = (address, 25187)
  client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, True)
  for i in xrange(3):
    # send 3 times to increase the success rate
    client.sendto(data, addr)
  while True:
    client.settimeout(endtime - time.time())
    try:
      data, addr = client.recvfrom(1024)
    except socket.timeout:
      break
    r_header, r_type, r_name = struct.unpack('8s16s32s', data)
    if r_header != "I'M HERE":
      continue
    try:
      r_type = r_type[:r_type.index('\0')]
    except ValueError:
      pass
    if type != '' and type != r_type:
      continue
    ret = (addr[0], r_name)
    # remove duplications
    if ret in rmdup:
        continue
    rmdup.add(ret)
    yield ret

if len(sys.argv) == 2:
  broadcast = sys.argv[1]
  print 'Using broadcast address: ' + broadcast
else:
  print 'Please enter a broadcast address(255.255.255.255 may not working)'
  broadcast = raw_input('Broadcast address: ')
  
devices = discover(broadcast, 'Light')
for dev in devices:
  print 'ip: %s, name: %s' % (dev[0], dev[1])
