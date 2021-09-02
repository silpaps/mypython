# files
#read,write
#f1=open('first','r')
#print(f1) =o/p(<_io.TextIOWrapper name='first' mode='r' encoding='cp1252'>)
#for i in f1:
#    print(i)
# to print contents of file we have to itrate it instead of print, orint only gives the location,mode of file
#>>>>>>>>>>writing
# f=open('first','w')
# f.write("hello world,i am a programer")
#>>>>>if no fle exist , then create one and content to it
f=open('aaa','w')
f.write("hello world")
f.write("how are you")