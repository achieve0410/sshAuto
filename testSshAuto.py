import paramiko

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.load_system_host_keys()

# L2s = ["10.52.54.245", "10.52.31.241", "10.52.31.242", "10.52.54.241"]
# L2s = ["10.52.54.245", "10.52.54.241"]
# L2s = ["10.52.38.201"]
L2s = ["10.52.38.201"]
for L2 in L2s:
    print("connect to ", L2)
    try:
        print('debug 1')
        ssh.connect(L2, username="wonhyo.choi1", password="Pa$$w0rdLM")
        print("ok1")
        
        
        #for line in iter(stdout.readline, ""):
        #    print(line.encode('utf-8'), end="")
        
        try:
            stdin, stdout, stderr = ssh.exec_command("sh clock", get_pty=True)
            print('debug 2')
            
            for line in iter(stdout.readline, ""):
                print(line, end="")
            
            break
        except:
            print('debug 3')
            break
            lines = stdout.read()
            if type(lines) is bytes:
                new_lines = lines.decode('utf-8')
                print(new_lines)

    except:
        print("debug 4")
        try:
            print('debug 5')
            ssh.connect(L2, username="admin1", password="Symbol!123")
            print("ok2")
            
            stdin, stdout, stderr = ssh.exec_command("sh wi cl")
            
            for line in iter(stdout.readline, ""):
                print(line, end="")
            
            try:
                print('debug 6')
                lines = stdout.readlines()
                
                for line in lines:
                    re = str(line).replace('\n', '')
                    print(re)
                    
            except:
                print('debug 7')
                lines = stdout.read()
                if type(lines) is bytes:
                    new_lines = lines.decode('utf-8')
                    print(new_lines)

        
        except:
            try:
                print('debug 8')
                ssh.connect(L2, username="wonhyo.choi", password="Pa$$w0rdLM")
                print("ok3")
                
                stdin, stdout, stderr = ssh.exec_command("sh clock")
                print(stdin, stdout, stderr)
                
                try:
                    print('debug 9')
                    lines = stdout.readlines()
                    print(lines)
                    
                    for line in lines:
                        re = str(line, "utf-8").replace('\n', '')
                        print(re)
                        
                except:
                    print('debug 10')
                    lines = stdout.read()
                    if type(lines) is bytes:
                        new_lines = lines.decode('utf-8')
                        print(new_lines)


    
    
    
    
            except Exception as err:
                print(err)