#Eduardo Ramos, RA:1700087
#Geibson Araujo, RA:1700184

ip = open("ips.txt","w")
ip.write("200.135.80.9\n")
ip.write("192.168.1.1\n")
ip.write("8.35.67.74\n")
ip.write("257.32.4.5\n")
ip.write("85.345.1.2\n")
ip.write("1.2.3.4\n")
ip.write("9.8.234.5\n")
ip.write("192.168.0.256")
ip.close()

arquivo = open("ips.txt","r")
for linha in arquivo:
    if linha ==linha:  
        print('ok')
    else:
        print('nao encontrado')
arquivo.close()








        
    
