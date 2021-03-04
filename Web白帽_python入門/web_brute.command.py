import optparse,math

parser=optparse.OptionParser()
parser.useage='web_brute.command.py -s url -u user_file -p pass_file -t num'

parser.add_option('-s','--site',dest='website',help='website to test',action='store',type='string',metavar='url')
parser.add_option('-u','--userfile',dest='userfile',help='username from file',action='store',type='string',metavar='userfile')
parser.add_option('-p','--passfile',dest='passfile',help='passfile from file',action='store',type='string',metavar='passfile')
parser.add_option('-t','--threads',dest='threads',help='number of threads',action='store',type='string',metavar='threads')

(options,arge)=parser.parse_args()

#playod確定
ths=options.threads
# print(ths)
pass_dic=options.passfile
# print(pass_dic)
user_dic=options.userfile
# print(user_dic)

##################
with open(pass_dic) as f:
    file=f.readlines()
    result=math.floor(len(file) / int(ths))
    result_list=[]
    pass_list=[]
    i=0
    for line in file:
        i+=1
        pass_list.append(line.strip())

        if i == result:
            result_list.append(pass_list)
            pass_list=[]
            i = 0
print(result_list)

with open(user_dic,'r') as user:
    user=user.readlines()
    for user_name in user:
        for passwd in result_list:
            pload={'user':user_name.strip(),'passwd':passwd}
            print(pload)



