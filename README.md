# Python-Automation-GNS3 (Using kron and archive)

### Objective
+ Compose a python script which use kron and archive functionality inside the Cisco Router
+ Compose a remote-server connection using SSH protocol using SSH Paramiko
***
### Tools use
+ GNS3 - Docker Container = [Toolbox](https://docs.gns3.com/appliances/net_toolbox.html) 
+ Router Images = Dynamips Cisco IOS - c7200-advipservicesk9-mz.152-4.S5.image
### 
***
### Outcome 
+ Build a python script that synchronize the backup file by using kron inside a Cisco Router.
+ Build a python script that include timestamp for the backup configuration using archive.
+ Connection from server to router using SSH Paramiko to secure the connection.

### Pre-installation for the server
## *Installing Paramiko in Ubuntu-Server*
```bash
apt-get update
apt-get install python -y
apt-get install build-essential libssl-dev libffi-dev -y
apt-get install python-pip -y
pip install cryptography
pip install paramiko
````
## *Setting up TFTP in router*
```bash
copy running-config tftp 
insert the ip addr 
destination filename  ---> **can set up any kind of file name**
```
## *Setting up the SSH in router*
```bash
host R1
ip domain-name router1.com
crypto key generate rsa --> set to 1024
```
## *Setting basic configuration*
```bash
enable password cisco
username luqman password cisco
username luqman privilege 15
line vty 0 4
login local
transport input ssh ---> transport only ssh connection for the time being
```
## *References:*
+ [David Bombal: Schedule Cisco config backup using kron and archive](https://youtu.be/-y-HUJOI8i4)

