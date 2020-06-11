import sys
import speedtest
from tkinter import *   
from tkinter import ttk 

def internet_test():    
    s = speedtest.Speedtest()
    s.get_best_server() 
    s.download()    
    s.upload()  
    res = s.results.dict()  
    dls = int(res["download"    ]) * (8 ** -6)
    uls = int(res["upload"]) * (8 ** -6)
    ping = int(res["ping"])
    clientdict = res["client"]
    ispstr = "ISP : " + clientdict["isp"]
    ipstr = "IP : " + clientdict["ip"]
    locstr = "Location : " + "lat : " + clientdict["lat"] + " lon : " + clientdict["lon"]
    dlstr = "Download Speed : %5.2f Mb" % dls
    ulstr = "Upload Speed : %5.2f Mb" % uls
    pingstr = "Ping : %3.0f ms " % ping
    return [ispstr, ipstr, locstr, dlstr, ulstr, pingstr]

def Result():
    reswin = Toplevel()
    reswin.title('Result',)
    reswin.geometry('300x100')
    reswin.resizable(False, False)
    var = StringVar()
    lb1 = Label(reswin, textvariable = var, relief = RAISED)
    lb1.config(justify = 'left')
    reinter = internet_test()
    var.set(reinter[0] + '\n' + reinter[1] + '\n' + reinter[2] + '\n' + reinter[3] + '\n' + reinter[4] + '\n' +reinter[5])
    lb1.pack()
    mainloop()

mainwin = Tk()
mainwin.title('Internet Test')
lb = Label(mainwin, text = 'Please click on Start to Run Internet Test')
lb.pack()
btn = Button(mainwin, text = 'Start', command = Result)
btn.pack()
mainwin.geometry("400x100")
mainwin.resizable(False, False)
lb2 = Label(mainwin, text = "By SeyedAliMousaviEdu")

lb2.pack()
mainloop()