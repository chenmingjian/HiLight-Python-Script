import sys
import json
import urllib2

def usage():
    print 'Usage: python wifimode.py <remote> ap'
    print '       python wifimode.py <remote> sta [SSID] [PASSWORD]'
    exit(1)

try:
    host = sys.argv[1]
    mode = sys.argv[2]
    mode = { 
      'sta'    : 1,
      'station': 1,
      '1'      : 1,
      'ap'     : 0,
      '0'      : 0
    }[mode.lower()]
    parms = {}
    if mode == 1:
      parms = {'wifi_ssid': sys.argv[3], 'wifi_passwd': sys.argv[4]}
except:
    usage()
data = {'mode' : mode}
data.update(parms)
data = json.dumps(data)

req = urllib2.Request('http://' + host + '/setting')
req.add_header('Content-type', 'application/json')
print "send: " + data
recv = urllib2.urlopen(req, data).read()
print "recv: " + recv