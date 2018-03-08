# -*- coding: utf-8 -*-
import utils
import re

"""Main module."""
class LEDTester:
    lights = None
    
    def __init__(self, N, instructions):
        self.lights = [[False]*N for _ in range(N)]
        self.instructions = instructions
        self.operations(self)
    
    def operations(self, instructions, command):
        for i in self.instructions:
            pattern = re.compile(".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*") 
            matched = pattern.match(i)
            self.command = matched.group(1)
            self.start = matched.group(2), matched.group(3)
            self.end = matched.group(4), matched.group(5)

            #X1 = matched.group(2)
            #X2 = matched.group(3)
            #Y1 = matched.group(4)
            #Y2 = matched.group(5)

            #self.apply(self, command, start, end)
    
    def apply(self, command, start, end):
        if command == "turn on":
            self.turnon(self, start, end)
            
        elif command == 'turn off':
            self.turnoff(self, start, end)
            
        elif command == 'switch':
            self.switch(self, start, end)
            
    def turnon(self,start, end):
        for i in range (len(self.lights)):
            for j in range (len(self.lights)):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True
                           
    def turnoff(self, start, end):
        for i in range (len(self.lights)):
            for j in range (len(self.lights)):
                if self.lights[i][j] == True:
                    self.lights[i][j] = False
                           
       
        
    def switch(self, start, end):
        for i in range (len(self.lights)):
            for j in range (len(self.lights)):
                if self.lights[i][j] == False:
                    self.lights[i][j] = True       
                else:
                    self.lights[i][j] == True
                    self.lights[i][j] = False

    def countOccupied(self, T):
        self.T = 0
        
        for i in range (len(self.lights)):
            for j in range (len(self.lights)):
                if self.lights[i][j] == True:
                    T += 1
        print(self.T)
        return self.T

        
    
    

def main():
    ifile = "C:/Users/Pavinee/led_tester/data/input_assign3.txt"
    N, instructions = utils.parseFile(ifile)
    matrix = LEDTester(N, instructions)


if __name__=='__main__':
    main()