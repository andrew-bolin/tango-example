#!/usr/bin/env python
# -*- coding: utf-8 -*-

from argparse import ArgumentParser
import tango

class DatabaseTool:
    """Database manipulation for Andrew's experimental Tango device"""
    
    _server = "AndrewDev/test"
    _class = "AndrewDev"
    _name_string = "test/andrew_dev/dev{:d}"
    _count = 10
    db = tango.Database()

    def add(self):
        """Add instances of the device to the DB"""
        dev_info = tango.DbDevInfo()
        dev_info.server = self._server
        dev_info._class = self._class
        for i in range(self._count):
            dev_info.name = self._name_string.format(i)
            self.db.add_device(dev_info)
    
    def delete(self):
        """Delete instances of the device from the DB"""
        for i in range(self._count):
            self.db.delete_device(self._name_string.format(i))
    
    def list(self):
        """Return a list of all instances of the device in the DB"""
        return self.db.get_device_name(self._server, self._class).value_string

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-a", "--add", action="store_true",
            help="add items to Tango databse")
    parser.add_argument("-d", "--delete", action="store_true",
            help="delete items from Tango databse")

    args = parser.parse_args()
    tool = DatabaseTool()

    if(args.add):
        tool.add()
    
    if(args.delete):
        tool.delete()

    l = tool.list()

    if(len(l) == 1):
        heading = "There is {:d} instance of class {} on server {}:"
    else:
        heading = "There are {:d} instances of class {} on server {}:"
        if(len(l) == 0):
            heading = heading[:-1] # remove colon if no list to follow

    print(heading.format(len(l), tool._class, tool._server))
    for i in l:
        print(i)
