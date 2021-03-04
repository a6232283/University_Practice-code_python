import optparse

parser=optparse.OptionParser()
parser.usage='command_argy.py -u user_file'

parser.add_option("-u","--user_file",help="read username from file",action="store",type="string",metavar="user_file",dest="username_file")

(options,args)=parser.parse_args()

