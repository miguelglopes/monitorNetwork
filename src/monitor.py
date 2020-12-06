import nmap
import model
import gotify


def getCurrentDevices():

    nm=nmap.PortScanner()
    output=nm.scan(hosts='192.168.1.0/24', arguments='-sP --system-dns')

    currentHosts = model.Hosts()
    for key, value in output["scan"].items():
        name = value["hostnames"][0]["name"]
        ip=value["addresses"]["ipv4"]
        try:
            mac=value["addresses"]["mac"]
        except:
            mac="no_mac"
        host = model.Host(mac, ip, name)
        currentHosts.add(host)
    
    return currentHosts

def getDevicesDif(old, new):

    set_old = set(tuple(sorted(d.items())) for d in old)
    set_new= set(tuple(sorted(d.items())) for d in new)

    dif=set_new.symmetric_difference(set_old)
    message=""
    for tuple_element in dif:
        message = message + tuple_element[0][1]+"/"+tuple_element[1][1]+"/"+tuple_element[2][1]+"\n"
    return message

def run():
    currentHosts = getCurrentDevices()
    oldHosts=model.Hosts.fromFile()
    dif = getDevicesDif(currentHosts, oldHosts)
    currentHosts.toFile()

    if dif!="":
        got=gotify.Gotify()
        got.pushMessage(dif, "Devices Dif")

    macCurrent = {c["mac"] for c in currentHosts}
    macOld=model.Macs.fromFile()
    dif=macCurrent.difference(macOld)
    if len(dif)>0:
        got=gotify.Gotify()
        got.pushMessage(str(list(dif)), "New Macadress!!!!")
        model.Macs.toFile(macOld.union(macCurrent))

run()

        