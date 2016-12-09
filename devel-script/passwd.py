import md5
import sys

def usage():
    print 'Usage: python passwd.py [HiLight-SSID]'
    exit(1)

if len(sys.argv) == 2:
  raw_passwd = sys.argv[1]
else:
  usage()

prefix = '\xb3\xc2\xc3\xf7\xbc\xfc'
suffix = '\xc2\xe3\xcc\xe5'
result = md5.md5(prefix + raw_passwd + suffix).digest()
result = md5.md5(prefix + result + suffix).hexdigest()
print result
