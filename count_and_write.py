import time

#Initialization
start_time = time.time()
num = 0


#Write numbers for 10 seconds.
#After 10 seconds, it writes "Done!"
with open('/home/ec2-user/Output/output_'+str(start_time), 'w') as f:
    while ( time.time() - start_time < 10):
        f.write(str(num)+"\n")
        num += 1
    f.write("Done!\n")
