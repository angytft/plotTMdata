#coding=utf-8
def TM2lineindex(inputfile,TM):
    index = []
    lst_TM = []
    for eachi in TM:
        lst_TM.append(eachi.split(' ')[0])
        print lst_TM
    f = open(inputfile,'r')
    linenum = 0
    for line in f:
        dataline = line.split(',')
        linenum = linenum + 1
        listnum = 0
        for eachdata in dataline:
            for element in lst_TM:
                if eachdata.split(' ')[0] == element :
                    index.append(listnum)
            listnum = listnum + 1
    return index


#print TM2lineindex('huatushuju.csv',['TTMU021 星箭分离状态','TTMU054 推进舱下位机B机5v'])