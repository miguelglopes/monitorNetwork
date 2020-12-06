from dataclasses import dataclass
from typing import List
import json

@dataclass
class Host:
    mac: str
    ip: str
    name: str

    def toJson(self):
        return {"mac": self.mac, "ip": self.ip, "name": self.name}

class Macs(set):
    _file="data/macs.json"

    @staticmethod
    def fromFile():
        with open(Macs._file, "r") as content:
           return set(json.load(content))
    
    @staticmethod
    def toFile(macs):
        with open(Macs._file, "w") as content:
           json.dump(list(macs), content)    


class Hosts(list):

    _file="data/hosts.json"

    def __init__(self) -> None:
        pass
    
    @staticmethod
    def fromFile():
        with open(Hosts._file, "r") as content:
           return json.load(content)
    
    def toFile(self):
        with open(self._file, "w") as content:
           json.dump(self, content)

    def add(self, host):
        self.append(host.toJson())    