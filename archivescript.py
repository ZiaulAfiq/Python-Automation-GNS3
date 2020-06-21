import paramiko
import time

## Edit your ip_address for the router configuration
ip_address = "192.168.122.62"
username = "luqman"
password = "cisco"

## Connection SSH Paramiko connect to router
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=ip_address,username=username,password=password)

print 'Successful connection', ip_address

remote_connection = ssh_client.invoke_shell()

## archive configuration inside here
remote_connection.send("conf t\n")
remote_connection.send("archive\n")
remote_connection.send("log config\n")
remote_connection.send("logging enable\n")
remote_connection.send("hidekeys\n")
remote_connection.send("exit\n")
## Input the tftp server ip_address in this line
remote_connection.send("path tftp://192.168.122.62/$-h\n")
remote_connection.send("write-memory\n")
remote_connection.send("time-period 1\n")
remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print(output)

ssh_client.close
