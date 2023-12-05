import glob, sys

#answers: part1 short 35 long 111627841
#answers: part2 short 46 long  69323688

for fname in glob.glob("day5_input_*.txt"):
    d={}
    seeds=None
    (lsrc,ldst)=("","")
    g=(line for line in open(fname) if line.strip()!="")
    for line in g:
        i=line.find(':')
        if i>0 and line[0:i]=="seeds":
            seeds=[int(w) for w in line[i+1:].split()]
        elif i>0:
            name,_=line[:i].split()
            lsrc,_,ldst=name.split('-')
            d[(lsrc,ldst)]=[]
        else:
            (dst,src,n) = [int(w) for w in line.split()]
            d[(lsrc,ldst)] += [(src,dst,n)]

    def find_dst(label):
        for (x,y) in d.keys():
            if x==label:
                return y

    def transform_sample(k,transform):
        for (src,dst,n) in transform:
            if k>=src and k<src+n:
                return dst + k-src
        return k 

    #chain transforms
    transforms=[]
    prev="seed"
    nxt=prev
    while nxt!="location" and nxt!=None:
        nxt=find_dst(prev)
        transforms+=[d[(prev,nxt)]]
        prev=nxt
    if nxt==None: 
        print("Failed to chain transforms")
        sys.exit(1) 

    def lookup_location(v, transforms):
        for transform in transforms:
            v=transform_sample(v,transform)
        return v

    N=min((lookup_location(v,transforms) for v in seeds))
    print(f"part1 {fname}", N)

    seed_ranges=[(seeds[i],seeds[i+1]) for i in range(0,len(seeds),2)]
    N=min( (lookup_location(v,transforms) for (start,n)  in seed_ranges for v in range(start,start+n+1)) )
    print(f"part2 {fname}", N)

