from __future__ import print_function

__author__ = 'nishanth'

from scapy.all import *


def modifypacket(packet):

    choice = 1

    while True:
        print('Modifiable IP fields: ')
        print('1. Fragmentation Flags')
        print('2. Identification Flags (16 bits) ')
        print('3. Checksum modification')
        print('4. Type of Service Field')
        choice = int(raw_input('Enter choice: (0 to stop) '))


        if choice == 0:
            return

        elif choice == 1:
           
            modifyflags(packet)

        elif choice == 2:
    
            modifyid(packet)

        elif choice == 3:

            modifychecksum(packet)

        elif choice == 4:

            modifytos(packet)

        else:

            print('Invalid choice. Re-enter.')


# Function to modify the fragmentation offset field

def modifyflags(packet):
    pass

# Function to modify the fragmentation identification flags

def modifyid(packet):

    newid = raw_input('Enter the new fragmentation id: ')
    print(is_number(newid))

    while (is_number(newid) is False) or int(newid) > 65535:
        
        print("Invalid ID, enter a valid ID( integer < 65535)\n")
        newid = raw_input('Enter the new fragmentation id: ')

    packet.id = int(newid)
    return

# Function to modify the IP-level checksum

def modifychecksum(packet):

    newchksum = raw_input('Enter new data in checksum field: ')

    while (is_number(newchksum) is False) or int(newchksum) > 65535:
        
        print("Invalid checksum,enter a valid checksum: (integer < 65536) \n")
        newchksum = raw_input('Enter new data in checksum field: ')

    packet.chksum = int(newchksum)
    return


# Function to modify the Type of Service field

def modifytos(packet):

    newtos = raw_input('Enter type of service: ')
    while (is_number(newtos) is False) or int(newtos) > 255:

        print("Invalid TOS, enter a valid TOS: (integer < 256)\n")
        newtos = raw_input('Enter type of service: ')
    
    packet.tos = int(newtos)
    return


# ##### Helper Function ##### #


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False