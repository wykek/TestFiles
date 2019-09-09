import os, threading, time

global on
on = 1
    
def pingResponse(hostname,retrieve,test):
    global on
    while on:
        #response = os.system("ping -c 1 "+hostname)
        response = os.system("ping -n 1 -w 1000 "+hostname)
        if response == 0:
            print("good hit on %s with response %s" % (hostname,response))
        else:
            print("bad hit on %s with response %s" % (hostname,response))
        retrieve[0] = response
        print(hostname)
        print(threading.currentThread().ident)
        print(threading.current_thread().getName())
        logFile = open("/home/user/scripts/kzz.log", "a")
        logFile.write(hostname+"\n")
        logFile.close()
        print test.isAlive()
        time.sleep(3)
def tess(mainProcess):
    global on
    while on:
        if mainProcess.isAlive():
            print(mainProcess, "is alive\n\n")
            time.sleep(3)
        else:
            print("herr\n\n\n\n\n\n\n\n\n\n\n")
            on = 0
        

def main():
    hostname = ["172.20.1.11","172.20.1.111"]
    process = []
    test = [None]*len(hostname)
    for i in range(len(hostname)):
        test[i] = [None]
    for i in range(len(hostname)):
        process.append(threading.Thread(target=pingResponse, args=(hostname[i],\
                test[i],threading.currentThread())))
    thisProcess = threading.currentThread()
    off = threading.Thread(target=tess, args=(thisProcess,))
    for p in process:
        p.start()
    off.start()
    for i in test:
        print i
    print("\n\n%s"%(threading.currentThread().ident))
    print(threading.current_thread())
    for p in process:
        print"here"
        print threading.currentThread().isAlive()
    
a = 4
def atest():
    print a
try:
    #main()
    atest()
    time.sleep(.5)
    #while True:
    #    time.sleep(1)
except Exception as e:
    on = False
    print e
