# -*- coding: utf-8 -*-
import led_tester.utils
import re
import led_tester
import pprint

"""Main module."""
class LEDTester:
    lights = None
    
    def __init__(self, N, instructions):
        self.N = N
        self.lights = [[False]*self.N for _ in range(self.N)]
        #pprint.pprint(self.lights)
        self.instructions = instructions
        self.command = ""
        self.operations()
        #pprint.pprint(self.lights)
        self.count = self.counting()
        print(self.count)

        
        #print(self.N)
        
        #self.apply(self)
#         print(self.lights)
        
    def operations(self):
        for i in self.instructions:
            pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
            matched = pattern.match(i)
            self.command = matched.group(1)
            print(self.command)
            self.start = matched.group(2), matched.group(3)
            self.end = matched.group(4), matched.group(5)
            if self.command == "turn on":
                self.turnon(self.command, self.start, self.end)
            elif self.command == 'turn off':
                self.turnoff(self.command, self.start, self.end)
            elif self.command == 'switch':
                self.switch(self.command, self.start, self.end)
        #return (self.get_count)
        #print(self.command,self.start,self.end)

            #X1 = matched.group(2)
            #X2 = matched.group(3)
            #Y1 = matched.group(4)
            #Y2 = matched.group(5)

            #self.apply(self, command, start, end)
    
#     def apply(self, instructions, command, start, end):
#         if self.command == "turn on":
#             self.turnon(self, start, end)
#             
#         elif self.command == 'turn off':
#             self.turnoff(self, start, end)
#             
#         elif command == 'switch':
#             self.switch(self, start, end)
            
    def turnon(self, command, start, end):
        #self.countTon = 0
        if self.command == "turn on":
            for i in range(int(self.start[0]),int(self.end[0])+1):
                for j in range(int(self.start[1]),int(self.end[1])+1):
                    self.lights[i][j] = True
                    #self.countTon += 1
        #return(self.countTon)
            #return(countTon)
                   
                           
    def turnoff(self, command, start, end):
        if self.command == 'turn off':
            for i in range (int(self.start[0]),int(self.end[0])+1):
                for j in range (int(self.start[1]),int(self.end[1])+1):
                    self.lights[i][j] = False
                           
       
        
    def switch(self, command, start, end):
        if command == 'switch':
            for i in range (int(self.start[0]),int(self.end[0])+1):
                for j in range (int(self.start[1]),int(self.end[1])+1):
                    self.lights[i][j] = not j


    def counting(self):
        T = 0
        for i in range (self.N):
            for j in range (self.N):
                if self.lights[i][j] == True:
                    T +=1
        #self.F = self.N * self.N - self.T                          
        return T

    
def main():
    ifile = "C:/Users/Pavinee/led_tester/data/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    #print(N, instructions)
    matrix = LEDTester(N, instructions)
#     F = 0
#     T = 0
# 
#     for i in range (len(lights)):
#         for j in range (len(lights)):
#             if lights[i][j] == False:
#                 F += 1
#             elif lights[i][j] == True:
#                 T += 1
#     print (F, T)
    #print(led_tester)
    #print (self.get_count)
    
    #matrix.countOccupied()
    #matrix.turnon()#
    
    
    #print(matrix)
    #print(matrix.countOccupied())


if __name__=='__main__':
    main()