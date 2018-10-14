import os
import sys



class Synchronizer():
    
    def __init__(self):
        pass
    
    def findTime(self,fileName,inputTime):
        self.fileName = fileName
        print(fileName,':',inputTime,'time is checking')
        with open(fileName,'r') as f:
            index = 0
            for line in f:
                if(-1 != line.find(inputTime)):
                    print(line)
                    return line
                else:
                    print(index,'Not now!')
                index += 1

    def findTimeDifference(self,timeLine,newTime):
        oldTime = timeLine.split('-->')[0]
        print('oldTime:',oldTime)
        print('newTime:',newTime)
        return int(self.time2MilliSecond(newTime) - self.time2MilliSecond(oldTime))

    def time2MilliSecond(self,time):
        timeArry = time.split(':')
        result = 0
        for i in range(len(timeArry)-1,0,-1):
            if -1 != timeArry[i].find(','):
                eachValue = timeArry[i].split(',')
                
                value = int(eachValue[0]) * pow(60,len(timeArry)-1-i) * 1000              
                value += int(eachValue[1])
                
                result += value
            else:
                print('42',timeArry[i])
                result += int(timeArry[i]) * pow(60,len(timeArry)-1-i) * 1000
        print('convertTime2Ms',result)
        return int(result)

    def milliSecond2Time(self,milliSecond):
        total = milliSecond /1000
        second = milliSecond / 1000
        
        hh = int(second / 3600)
        total -= float(hh * 3600)
        print('hh =',hh)
        print('total =',total)
        
        mm = int(second / 60)
        total -= float(mm * 60)
        print('mm =',mm)
        print('total =',total)
        
        ss = float(total)
        print('ss =',ss)
        print('total =',total)

        hh = '{0:02.0f}'.format(hh)
        mm = '{0:02.0f}'.format(mm)
        
        if type(ss) == float(ss):
            ss = '{0:06.3f}'.format(ss)
            ss.replace('.',',')
        else:
            ss = '{0:06.3f}'.format(ss)
            ss.replace('.',',')
        return hh + ':' + mm + ':' + ss

    def changeSubtitleTime(self,diff):
        with open(self.fileName,'r') as f:
            with open('new_'+self.fileName,'w') as newSubtitle:
                for line in f:
                    if -1 != line.find('-->'):
                        beginTime = line.split('-->')[0]
                        endTime = line.split('-->')[1]

                        newBeginTime = self.time2MilliSecond(beginTime) + diff
                        newEndTime = self.time2MilliSecond(endTime) + diff

                        newBeginTime = self.milliSecond2Time(newBeginTime) #format hh:mm:ss
                        newEndTime = self.milliSecond2Time(newEndTime) #format hh:mm:ss
                        
                        newLine = newBeginTime + ' --> ' + newEndTime + '\n'
                        newSubtitle.write(newLine)
                    else:
                        newSubtitle.write(line)
        

if __name__ == '__main__':
    subTitle = Synchronizer()
    timeLine = subTitle.findTime('sub.srt','00:01:33,712')
    newTime = '00:01:36,508'
    difference = subTitle.findTimeDifference(timeLine,newTime)
    print('Difference:',str(difference),'ms')
    subTitle.changeSubtitleTime(difference)
