# Get Proxy Test
`Get Proxy Test` 是一个可以在服务器IP已知的情况下通过循环Telent连接的方式扫描代理服务器端口的脚本。

## 运行环境
- 系统:          Ubuntu 18.04 LTS
- Python:       Python 3.6.9
- 所需库:       telnetlib、time

## 使用方法
- 修改`test.py` 中的 `port_start` 、`port_end` 、`ip_addr`
- 在ubuntu下执行 python3 test.py运行即可
