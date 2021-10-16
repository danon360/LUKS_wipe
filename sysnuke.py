import subprocess

#partition in which the luks header is located 
header_location = "/dev/nvme0n1p3"

#size of the luks header 
header_size = '20'

#command to run
command = ['dd', 'if=/dev/zero', 'of=' + header_location, 'bs=1M', 'count=' + header_size]

#different systems might have different shut down commands and arguments 
shutdown_command = ['shutdown','0']

#run the command 
process = subprocess.Popen(command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

#run the shutdown command 
process = subprocess.Popen(shutdown_command, stdout = subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()

print(stdout)
exit()
