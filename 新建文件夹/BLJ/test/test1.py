import paramiko


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(hostname='192.168.14.51', port=22, username='root', password='123456')


stdin, stdout, stderr = ssh.exec_command('ifcofig')
print(stdout)

result = stdout.read()

ssh.close()