# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 12:43:11 2020

@author: Alok Garg
"""

class Range:
    def __init__(self,start,stop=None,step=1):

        if stop is None:
            self.start,self.stop = 0,start
        else:
            self.start = start
            self.stop = stop
        if start > stop:
            raise ValueError('start is greater then stop')
        if step == 0:
            raise ValueError('step can not be 0')
        else:
            self.step = step

        #self.num = []


    def range_num(self):
        self.num = []
        while self.start < self.stop:
            self.num = self.num+[self.start]
            #self.num.append(self.start + self.step)
            self.start += self.step
        return self.num


if __name__ == '__main__':
    r = Range(2,10,2)
    num_list = r.range_num()
    print('Range:',num_list)




















#class Range:
#    def __init__(self,start,stop= None, step =1):
#        if self.step ==0:
#            raise ValueError('Step cant be 0')
#        if stop is None:
#            start
#        self.start = start
#        self.stop = stop
#        self.step = 1
#    def print_start_stop(self):
#        print(self.start,self.stop)
#
#    def __add__(self,step):
#        if self.step ==0:
#            return ValueError('arg 3 must not be zero')
#        i = 0
#        final_list =[]
#        while i <= self.stop:
#            final_list.append(result)
#            result += self.start+self.step
#
#        return final_list
#
#
#if __name__ == '__main__':
#    r = Range(1,11)
#    r.print_start_stop()
#    x = r.__add__(0)
#    y = r.__add__(3)
#
#
#
##range(1,5,0)
range(4)
