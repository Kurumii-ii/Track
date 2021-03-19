import pygeoip

gip = pygeoip.GeoIP("GeoLiteCity.dat")
res = gip.record_by_addr(input(''))
for key, val in res.items():
    print('%s : %s' % (key,val))
