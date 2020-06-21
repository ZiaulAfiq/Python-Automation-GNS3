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

print("Successful connection", ip_address)

remote_connection = ssh_client.invoke_shell()

## kron configuration inside here
remote_connection.send("kron policy-list backupconfig")
remote_connection.send("cli show run | redirect tftp://192.168.122.62/router-shrun.cfg")
remote_connection.send("exit")
remote_connection.send("kron occurrence backupminute in 1 recurring")
remote_connection.send("policy-list backupconfig")
remote_connection.send("end\n")

time.sleep(1)
output = remote_connection.recv(65535)
print(output)

ssh_client.close
