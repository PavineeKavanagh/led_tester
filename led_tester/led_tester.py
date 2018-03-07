# -*- coding: utf-8 -*-
from led_tester import utils
"""Main module."""
class LEDTester:
    lights = None
    
    def __init__(self, N, instructions):
        self.lights = [[False]*N for _ in range(N)]
        self.instructions = instructions
        self.operations(self)
    
    def operations(self):
        for i in self.instructions:
            command, start, end = #regex here
            self.apply(self, command, start, end)
    
    def apply(self, command, start, end):
        if command == "turn on"
            self.turnon(self, start, end)
        elif command == 'turn off'
            self.turnoff(self, start, end)
        elif command == 'switch'
            self.switch(self, start, end)
            
    def turnon(self, start, end):
        for i in range():
            for j in range():
            
        
    def turnoff(self, start, end):
        
    def switch(self, start, end):
    
    def countOccupied(self):
        return count
    
    

def main():
    ifile = "C:/Users/Pavinee/led_tester/data/test_data.txt"
    N, instructions = utils.parseFile(ifile)
    matrix = LEDTester(N, instructions)


if __name__=='__main__':
    main()