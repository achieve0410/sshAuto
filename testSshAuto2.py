import paramiko
import time

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.load_system_host_keys()

# L2s = ["10.52.54.245", "10.52.31.241", "10.52.31.242", "10.52.54.241"]
# L2s = ["10.52.54.245", "10.52.54.241"]
L2s = ["10.52.38.201"]
#L2s = ["10.52.31.241", "10.52.31.242"]
for L2 in L2s:
    print("connect to ", L2)
    try:
        print('debug 1')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        
        ssh.connect(L2, username="wonhyo.choi", password="Pa$$w0rdLM", look_for_keys=False, allow_agent=False)
        print("ok3")
        
        stdin, stdout, stderr = ssh.exec_command("sh clock", get_pty=True, timeout=4)
        print(stdin, stdout, stderr)
        
        try:
            print('debug 2')
            #lines = stdout.read(1000)
            try:
                #print(stdout.read())
                lines = stdout.read()
                #print(lines)
                
                print('timeout')
            except:
                try:
                    print('111')
                    #lines = stdout.
                    
                except:
                    print('2222')
                    
            print(type(lines))
            if type(lines) is bytes:
                print('debug 3')
                try:
                    new_lines = str(lines,'cp1252')
                    print(new_lines)
                except:
                    print('debugasd')
            else:
                print('debug 1043')
            
                for line in lines:
                    print('debug 4')
                    re = str(line, "ISO-8859-1")
                    print(re)
            
            print('debug 5')
            
        except:
            print('debug 6')
            lines = stdout.read().decode('utf-8')
            
            for line in lines:
                print('deab')
                print(str(line))

    except Exception as err:
        print(err)