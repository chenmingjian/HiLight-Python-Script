import sys
import json
import urllib2

if len(sys.argv) < 3:
    print 'Usage: python mode.py <remote> <mode> [<args...>]'
    exit(1)

def parse(x):
  x = x.strip()
  if x[0] == '#':
    return x
  elif x[:2].lower() == '0x':
    return int(x[2:], 16)
  else:
    return int(x)

argv = sys.argv[1:]
if len(argv) >= 2:
  remote = argv[0]
  mode = argv[1]
params = argv[2:]
params = tuple( parse(x) for x in params )
req = urllib2.Request('http://' + remote + '/mode')
req.add_header('Content-type', 'application/json')
data = json.dumps({ 'mode' : mode, 'params' : params })
print "send: " + data
recv = urllib2.urlopen(req, data).read()
print "recv: " + recv