#coding=utf-8
def datasplit(inputfile,outputfile,lineindex): #提取某一列数据和时间
    f1 = open(inputfile,'r')
    f2 = open(outputfile,'w')
    #linenum = 0
    for line in f1:
        #linenum = linenum + 1
        #if linenum != 1:
            dataline = line.split(',')
            time = dataline[0]
            if dataline[lineindex] == '--':
                tmdata = ''
            else:
                tmdata = dataline[lineindex]
            if dataline[lineindex] != dataline[-1]:
                outputline = time +','+ tmdata + '\n'
            else:
                outputline = time +','+ tmdata
            f2.write(outputline)
    f1.close()
    f2.close()
    print 'write file complete'

#datasplit('huatushuju.csv', 'ttmu007.csv', 2)

def datasplit_multi(inputfile,outputfile,lineindex): #提取某几列数据和时间 lineindex为list型变量
    f1 = open(inputfile, 'r')
    f2 = open(outputfile, 'w')
    # linenum = 0
    for line in f1:
        # linenum = linenum + 1
        # if linenum != 1:
        dataline = line.split(',')
        time = dataline[0]
        tmdata = ''
        for element in lineindex:
            if dataline[element] == '--':
                tmdata = tmdata + ','
            else:
                tmdata = tmdata + ',' + dataline[element]
            if dataline[element] != dataline[-1]:
                outputline = time  + tmdata + '\n'
            else:
                outputline = time  + tmdata
        f2.write(outputline)
    f1.close()
    f2.close()
    print 'write file complete'


#datasplit_multi('huatushuju.csv', 'ttmu007.csv', [2,3,57])
