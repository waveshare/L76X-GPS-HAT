import L76X
import time
import math

# try:
x=L76X.L76X()
x.L76X_Set_Baudrate(9600)
x.L76X_Send_Command(x.SET_NMEA_BAUDRATE_115200)
time.sleep(2)
x.L76X_Set_Baudrate(115200)

x.L76X_Send_Command(x.SET_POS_FIX_400MS);

#Set output message
x.L76X_Send_Command(x.SET_NMEA_OUTPUT);


x.L76X_Exit_BackupMode();


h = 0
m = 0
s = 0
h1 = 0
m1 = 0
s1 = 0

m1 = math.floor(time.time())/60%60
h1 = math.floor(time.time())/3600%60
s1 = math.floor(time.time())%60
if(m1 >= 59):
    h1 = h1 + 1;
    m1 = m1 + 1 -60;
m1 = m1 +1
while(1):
    x.L76X_Gat_GNRMC()
    if(x.Status == 1):
        print 'Already positioned'
    else:
        print 'No positioning'
    print 'Time %d:'%x.Time_H,
    print '%d:'%x.Time_M,
    print '%d'%x.Time_S

    print 'Lon = %f'%x.Lon,
    print ' Lat = %f'%x.Lat
    x.L76X_Baidu_Coordinates(x.Lat, x.Lon)
    print 'Baidu coordinate %f'%x.Lat_Baidu,
    print ',%f'%x.Lon_Baidu
    
    m = math.floor(time.time())/60%60
    h = math.floor(time.time())/3600%60
    s = math.floor(time.time())%60
    if(h >= h1 and m >= m1 and s >= s1):
        print("Enter backup mode \r\n");
        x.L76X_Send_Command(x.SET_PERPETUAL_BACKUP_MODE)
        
        print("Please enter any character to exit backup mode\r\n")
        raw_input()
        print("Exit backup mode \r\n")
        x.L76X_Exit_BackupMode();
        m1 = math.floor(time.time())/60%60
        h1 = math.floor(time.time())/3600%60
        m1 = m1 +1 
        if(m1 >= 59):
            h1 = h1 + 1;
            m1 = m1 + 1 -60;
        
# except:
    # GPIO.cleanup()
    # print "\nProgram end"
    # exit()