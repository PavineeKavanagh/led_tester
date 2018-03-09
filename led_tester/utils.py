import urllib.request#led_tester/utils.py

def parseFile(input):
    
    if input.startswith("http"):
        N, instructions = None, []
        with urllib.request.urlopen(input) as f:
            N = int(f.readline().decode("utf-8"))
            for line in f.readlines():
                line = line.decode()
                instructions.append(line)
        return N, instructions
    
        
            
    else:
        # read from disk
        N, instructions = None, []
        with open(input, 'r') as f:
            N = int(f.readline())
            for line in f.readlines():
                instructions.append(line)
        return N, instructions
    return
