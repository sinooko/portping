import socket
import sys
from time import sleep


def is_open(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        return 'Port is open'
    except ConnectionRefusedError:
        return 'Connection Refused'


if len(sys.argv) == 1:
    ip = input('\nPlease enter the IP address you wish to check.\n')
    port = input('Please enter the port on that IP that you wish to check.\n')

    print(is_open(ip, port))
elif len(sys.argv) == 3 or len(sys.argv) == 4:
    ip = sys.argv[1]
    port = sys.argv[2]
    if len(sys.argv) == 4:
        if sys.argv[3] == 'i':
            # Intentionally create an infinite loop
            loop = -1
        else:
            loop = int(sys.argv[3])

        i = 0
        while i != loop:
            i += 1
            print('Try ' + str(i) + ': ' + is_open(ip, port))
            sleep(1)
    else:
        print(is_open(ip, port))
else:
    print(
        '\nInvalid number of arguments.\nPlease provide 2 or 3 '
        'arguments.\n 1st argument IP\n 2nd argument PORT\n '
        '3rd argument NUMBER of tries, (i for infinite)'
    )
