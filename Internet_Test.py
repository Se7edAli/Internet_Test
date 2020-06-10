import speedtest
s = speedtest.Speedtest()
s.get_best_server()
s.download()
s.upload()
res = s.results.dict()
dls = int(res["download"]) * (8 ** -6)
uls = int(res["upload"]) * (8 ** -6)
ping = int(res["ping"])
clientdict = res["client"]

print ("ISP : ", clientdict["isp"])
print ("IP : ",clientdict["ip"])
print ("Location : ", "lat : ",clientdict["lat"]," lon : ",clientdict["lon"])
print ("Download Speed : %5.2f MB" % dls)
print ("Upload Speed : %5.2f MB" % uls)
print ("Ping : %3.0f ms " % ping)

end = input("Please Enter any key to Exit !!!")