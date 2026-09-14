import psutil 

from pprint import pprint as pp
# print(ps.cpu_times())

# print(ps.getloadavg())



import getpass

pp([(p.pid, p.info['name']) for p in psutil.process_iter(['name', 'username']) if p.info['username'] == getpass.getuser()])