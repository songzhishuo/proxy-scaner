
import telnetlib
import time

port_start = 32000                 ### 扫描端口起始地址
port_end = 32050                   ### 扫描端口结束地址
ip_addr = '10.192.1.192'           ### 扫描的服务器IP


CanUsePort = 0
CanUsePort_num = 0

port_total_num = port_end - port_start

for i in range(port_start, port_end):

     # url = ip_addr+':'+str(i)
     try:
          telnetlib.Telnet(ip_addr, i, timeout=3)
          print("代理IP有效！")
          print('port:' + str(i))
          CanUsePort = i
          CanUsePort_num = CanUsePort_num + 1
     except:
          time.sleep(1.5)               ##睡眠防止服务器判断为泛洪
          print('pass')

     print('plan ['+ str(((i - port_start) * 100)/port_total_num) + ']')

print('可用端口: '+ str(CanUsePort))
print('可用端口数目: '+ str(CanUsePort_num))

# ip_addr = 'https://10.192.1.192'
# port_start = 32040
# port_end = 32052


# import urllib3
# import time

# # url = ip_addr+':'+str(32048)
# # http = urllib3.proxy_from_url(url) 
# # print(url)
                              
# # http = urllib3.proxy_from_url("http://10.192.1.192:32048")  # This returns a ProxyManager object which has the same API as other ConnectionPool objects.
# # resp = http.request('GET', 'http://www.baidu.com')
# # print('check ip:' + ip_addr +'  ,port:'+str(32048))
# # for i in range(2):
# for i in range(port_start, port_end):

#      url = ip_addr+':'+str(i)
#      # url = "http://10.192.1.192:32048"
#      print(url)
     
#      try:
#           http = urllib3.proxy_from_url(url)  # This returns a ProxyManager object which has the same API as other ConnectionPool objects.
#           resp = http.request('GET', 'myip.ipip.net',timeout=2)
#           print('check ip:' + ip_addr +'  ,port:'+str(i))
#      except:
#           a = 1
#           time.sleep(2)


     # try:
     #      resp = urllib3.request('GET', 'http://www.baidu.com')
     #      print('check ip:' + ip_addr +'  ,port:'+str(i))
     # except:
     # print('not check')
     
# print(json.load(reader(resp)))
# import urllib.request
# proxy=urllib.request.ProxyHandler({"http": "http://120.77.249.46:8080"})
# opener=urllib.request.build_opener(proxy)
# urllib.request.install_opener(opener)
# data = urllib.request.urlopen('http://www.baidu.com',timeout = 2).read().decode('utf-8','ignore')
# try:
#      if(len(data) > 5000):
#           print(thisIP + ':可用')
#      else:
#           print(thisIP + ':无效')
# except :
#      print(thisIP + ':无效！！!')
