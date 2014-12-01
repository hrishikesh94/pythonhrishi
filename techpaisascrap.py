import urllib
import re
import msvcrt as m
import json
import datetime as DT
import numpy as np
import csv
import matplotlib.pyplot as plt
from matplotlib.dates import date2num
import operator

def getColumn(filename, column):
    results = csv.reader(open(filename))
    return [result[column] for result in results]

total =0
data=[0]
dates=[]
#while True:
htmlfile = urllib.urlopen("http://techpaisa.com/chart/acc/volume/?xhr")
htmltext= htmlfile.read()
print "one"
htmlfile2 = urllib.urlopen("http://techpaisa.com/chart/acc/adx/?xhr")
htmltext2=htmlfile2.read()

htmlfile3=urllib.urlopen("http://techpaisa.com/supres/acc")
htmltext3=htmlfile3.read()
g=0
while (g<40):
    w=1
    
    if (g/2==0):
        w=1
    if (g==9):
        w=0
    if (g==11):
        w=0
    if (g==13):
        w=0
    if (g==17):
        w=0
    if (g==15):
        w=0
    if (g==19):
        w=0
    if (g==21):
        w=0
    if (g==23):
        w=0
    if (g==25):
        w=0
    if (g==27):
        w=0
    if (g==29):
        w=0
    if (g==31):
        w=0
    if (g==33):
        w=0
    if (g==35):
        w=0
    if (g==37):
        w=0
    if (g==39):
        w=0
    if (g==0):
        w=2
    if (g==1):
        w=0
    if (g==3):
        w=0
    if (g==5):
        w=0
    if (g==7):
        w=0
    
    print htmltext3.split(':')[5].split(',')[g].split('[')[w]
    g=g+1

i=4000  #for simple average calc
k=5    #for SMA calc
SMA=0.0000
print "pop"

#_______________________________________________________________________________________#
#calculating the average of the term

writer = csv.writer(open('prices.csv', 'wb'))
while i <int(len(htmltext.split("#"))-1):
              #Since printing the values will kill the speed!!!!!!!!!!!!!!!!
              #print "date", htmltext.split("#")[i].split(",")[0],"price",htmltext.split("#")[i].split(",")[1],"volume",htmltext.split("#")[i].split(",")[2]
              i+=1
              dates=DT.datetime.strptime(htmltext.split("#")[i].split(",")[0].split("0:00")[0], "%Y/%m/%d")
              dates2=date2num(DT.datetime.strptime(htmltext.split("#")[i].split(",")[0], "%Y/%m/%d"))
              val = float(htmltext.split("#")[i].split(",")[1])
              writer.writerow(([dates2][0],[val][0]))
              total=total+val

average =total/(i-1)
print "average price ", average


#_______________________________________________________________________________________#
#calculating the SMA( simple moving average over five days )

writer = csv.writer(open('smadates.csv', 'wb'))
while k <=int(len(htmltext.split("#"))-1):

    
    #Since printing the values will kill the speed!!!!!!!!!!!!!!!!
    #print "date", htmltext.split("#")[i].split(",")[0],"price",htmltext.split("#")[i].split(",")[1],"volume",htmltext.split("#")[i].split(",")[2]

           
    while (k<int(len(htmltext.split("#"))-1)):
        total=float(htmltext.split("#")[k].split(",")[1])+float(htmltext.split("#")[k-1].split(",")[1])+float(htmltext.split("#")[k-2].split(",")[1])+float(htmltext.split("#")[k-3].split(",")[1])+float(htmltext.split("#")[k-4].split(",")[1])
        SMA=total/5
        break
    dates=DT.datetime.strptime(htmltext.split("#")[k].split(",")[0].split("0:00")[0], "%Y/%m/%d")
    dates2=date2num(DT.datetime.strptime(htmltext.split("#")[k].split(",")[0], "%Y/%m/%d"))

    #Since printing the values will kill the speed!!!!!!!!!!!!!!!!
    #print k," date",dates,"  AMount  ",SMA

    
    writer.writerow(([dates2][0],[SMA][0]))
    k+=1
                                                             

print "blah"
time = getColumn("smadates.csv",0)
volt = getColumn("smadates.csv",1)

#### OLD CODE FOR THE CHART...CAN BE REMOVED LATER!
#data1=np.genfromtxt('smadata.csv', skip_header=1) #suppose it is in the current working directory
#data2=np.genfromtxt('smadates.csv', skip_header=1)
#plt.plot(data1,'o-')
#plt.savefig('mpl_font_testA.png')
#plt.plot(data2, '.b', label='aErr < bErr')

plt.figure("SMA over the entire period")
plt.xlabel("Time(ms)")
plt.ylabel("Volt(mV)")
plt.plot(time,volt)
plt.show('else')


#_______________________________________________________________________________________#
#calculate the ATR as chart
####### THRESHOLD: 25!
k=14

plusdi14=0
minusdi14=0
writer3 = csv.writer(open('atrchart.csv', 'wb'))
while k <int(len(htmltext2.split("#"))-1):

              #collecting all the values for the ATR representation :

    
              dates2=date2num(DT.datetime.strptime(htmltext2.split("#")[k].split(",")[0], "%Y/%m/%d"))
              ADX= htmltext2.split("#")[k].split(",")[1]
              plusdi= htmltext2.split("#")[k].split(",")[2]
              minusdi=htmltext2.split("#")[k].split(",")[3]
              i+=1
              m=14
              print 'working'
              while (m<0):
                      plusdi14=float(htmltext.split("#")[k-m].split(",")[2])+plusdi14
                      minusdi14=float(htmltext.split("#")[k-m].split(",")[3])+minusdi14
                      m=m-1
            
              diffdi=operator.abs(plusdi14-minusdi14)
              summdi=plusdi14+minusdi14
              print diffdi
              print summdi
              writer.writerow(([dates2][0],plusdi14,minusdi14))
                    

                      
                      
              
              
