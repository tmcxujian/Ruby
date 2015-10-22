import re

##normal split() can't deal with multiple separators
##normal split() can't deal with spaces near separators
##pay attention to capture group [] won;t capture separator while () will
def specialSplit():
         line = 'asdf sdda;sjdasd, sdad,dadad,     foo'
         lineOne = re.split(r'[;,\s]\s*',line)
         lineTwo = re.split(r'(;|,|\s)\s*',line)
         lineThree = re.split(r'(?:;|,|\s)\s*',line)
         lineFour = line.split(',')        
         print lineOne
         print lineTwo
         print lineThree
         print lineFour
         specialJoin(lineTwo)

##output:
##['asdf', 'sdda', 'sjdasd', 'sdad', 'dadad', 'foo']
##['asdf', ' ', 'sdda', ';', 'sjdasd', ',', 'sdad', ',', 'dadad', ',', 'foo']
##['asdf', 'sdda', 'sjdasd', 'sdad', 'dadad', 'foo']
##['asdf sdda;sjdasd', ' sdad', 'dadad', '     foo']
         
#sometimes delimters are useful, it might need to save
def specialJoin(line):
         values = line[::2]
         delimiters = line[1::2] + ['']
         ##reform the line using the same delimiters
         print(''.join(v+d for v,d in zip(values,delimiters)))
##output:
##asdf sdda;sjdasd,sdad,dadad,foo
         
specialSplit()
