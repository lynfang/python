# -*- coding: UTF-8 -*-
import time
import string
import os
import re


db = []

def newinfo():
    promt = 'info desired:'
    while True:
        info = raw_input(promt)
        if info  in  db:
            promt = 'name take , try another: '
            continue
        else:
            break
    db.append(info)


def listinfo():
    promt = """  Please enter zone nums of key word:

        """
    sort = {}
    choise = input(promt)

    for lines in db:

        lines_list = re.split(':', lines)
        zone_flag = 1
        for zone in lines_list:
            #print str(choise) + '\t' + str(zone_flag) + '\t' + line_zone + '\t'  + zone
            if zone_flag == choise:
                line_zone = zone
                break
            else:
                zone_flag = zone_flag + 1
                continue

        sort[line_zone] = lines
        #print  lines + ':' + line_zone

    lis = sort.keys()

    print """



        ##############################


        """
    for sort_lines in bubble_sort(lis):
        print sort_lines,sort[sort_lines]




def bubble_sort(lis):
     count = len(lis)
     for i in range(0, count):
         for j in range(i + 1, count):
             if lis[i] > lis[j]:
                 lis[i], lis[j] = lis[j], lis[i]
     return  lis


def showmenu():
    promt = """
    (A)dd new line
    (L)ist info
    (Q)uit   
    Enter choice:    """

    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choise = raw_input(promt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choise = 'q'
            print '\n You picked: [%s]' % choise
            if choise not in 'alq':
                print 'invalid option,try again'
            else:
                chosen = True

        if choise == 'q': done = True
        if choise == 'a': newinfo()
        if choise == 'l': listinfo()



if __name__ == '__main__':
    showmenu()

