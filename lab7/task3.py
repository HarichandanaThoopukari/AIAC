#code1

with open("example.txt","w") as f:
    f.write("hello, world!")

    #code2
f1=open("data1.txt","w")
f2=open("data2.txt","w")
f1.write("first file content\n")
f2.write("second file content\n")
print("files written successfully")
#code 3
data=open("input.txt","r").readlines()
output=open("output.txt","w")
for line in data:
    output.write(line.upper())
    print("processing done")
#code 4
f=open("numbers.txt","r")
nums=f.readlines()
squares=[]
for n in nums:
    n=n.strip()
    if n.isdigit():
        squares.append(int(n)*int(n))
f2=open("squares.txt","w")
for sq in squares:
    f2.write(str(sq)+"\n")
print("squares written")