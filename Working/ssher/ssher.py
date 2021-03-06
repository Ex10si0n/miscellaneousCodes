import os
import sys

def conn(ip='userinput'):
    ipnotfound = True
    if ip == 'userinput':
        ip = input('[IP]: ')
    
    f = None


    try:
        f = open('known_hosts', mode='r')
    except:
        os.system('touch known_hosts')
        f = open('known_hosts', mode='r')

    hosts = f.read()
    hosts = hosts.split()
    cmd = None
    cmdlist = []
    f.close()

    for i in range(len(hosts)):
        if hosts[i] == ip:
            usr = hosts[i+1]
            cmd = 'ssh %s@%s' % (usr, ip)
            ipnotfound = False

        # If IP
        if '.' in hosts[i]:
            hostfrag = hosts[i].split('.')
            ipfrag = ip.split('.')
            for fr in ipfrag:
                if str(fr) == str(hostfrag[0]):
                    ip = hosts[i]
                    usr = hosts[i+1]
                    cmd = 'ssh %s@%s' % (usr, ip)
                    ipnotfound = False
                    cmdlist.append(cmd)

    if len(cmdlist) >= 2:
        print("Select from %d Servers:" % len(cmdlist))
        i = 0
        for c in cmdlist:
            print("[%d]" % i, c[4:])
            i += 1
        choice = int(input("[Choice]: "))
        cmd = cmdlist[choice]


    if ipnotfound:
        usr = input('[User]: ')
        f = open('known_hosts', mode='a+')
        f.write('%s %s\n' % (ip, usr))
        f.close()
        cmd = 'ssh %s@%s' % (usr, ip)

    os.system(cmd)

def hosts():
    print('[ssher hosts]')
    f = open('known_hosts', mode='r')
    hosts = f.read()
    print(hosts)

def helpdocs():
    print('[ssher docs]')
    helptext = '''ssher help          help docs
ssher hosts/h       list all hosts
ssher <ip>          ssh to a server
ssher <abbr ip>     ssh to a server with shorter input
    '''
    print(helptext)

def main():
    if len(sys.argv) == 1:
        conn()
    else:
        if len(sys.argv) == 2 and sys.argv[1] == 'help':
            helpdocs()
        if len(sys.argv) == 2 and sys.argv[1] == 'hosts' or sys.argv[1] == 'h':
            hosts()
        if len(sys.argv) == 2 and '.' in sys.argv[1]:
            conn(sys.argv[1])
        if len(sys.argv) == 2 and sys.argv[1].isdigit():
            conn(sys.argv[1])
            

if __name__ == '__main__':
    main()
