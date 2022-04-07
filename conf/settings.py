base_dir = '/dl/sry/TUT/usage/ftp'
ip = '222.30.62.7'
port = '2020'
#上传速度  300kb/s
max_upload = 0# * 1024

#下载速度 3000kb/s
max_download = 3000 * 1024

#最大连接数
max_cons = 20

#最多IP数
max_per_ip = 50

#被动端口范围，注意被动端口数量要比最大IP数多，否则可能出现无法连接的情况
passive_ports = (2000, 2200)

#是否开启匿名访问 on|off
enable_anonymous = 'off'
#匿名用户目录
anonymous_path = f'{base_dir}/files'

#是否开启日志 on|off
enable_logging = 'on'
#日志文件
loging_name = f'{base_dir}/ftp.log'

#欢迎信息
welcome_msg = 'OCR2020NKU'
