import glob
   
WORDS=["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
WORDSr=[s[::-1] for s in WORDS]
def find_digit(s, digits):
    for i,c in enumerate(s):
       if c in "0123456789":
           return int(c) 
       for j,x in enumerate(digits):
           if s[i:i+len(x)]==x:
               return j+1

for fname in glob.glob("day1_*input*.txt"):
    g=(line.strip() for line in open(fname))
    g=(find_digit(line, WORDS)*10 + find_digit(line[::-1], WORDSr) for line in g)
    print(f"{fname}: {sum(g)}")
    
