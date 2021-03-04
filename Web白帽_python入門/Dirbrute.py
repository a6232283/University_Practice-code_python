import getopt,sys,math

# opts, args=getopt.getopt(sys.argv[1:],"u:t:d:")
# print(type(opts))
# print(opts)
# print(type(args))
# print(args)


with open('dir.txt','r') as f:
    file_list=f.readlines()
    result_list=[]
    temp=[]
    i=0
    print(len(file_list))
    for line in file_list:
        i+=1
        
        if i % 4==0:
            temp.append(line.strip())
            result_list.append(temp)
            temp=[]
        else:
            temp.append(line.strip())

print(result_list)