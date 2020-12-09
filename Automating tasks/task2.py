import argparse
import sys
import configparser
import yaml
def main(number1,number2,output):
    result = number1*number2
    print(f'the result is:{result}',file=output)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description= 'Produit the 2 number')
    parser.add_argument('-n1',dest='number1' ,help='the first number',type=int)
    parser.add_argument('-n2',dest='number2', help='the second number',type=int)
    parser.add_argument('-config','-c',help='config file',type=argparse.FileType('r'))
    parser.add_argument('-o',dest='output',help='output file',type=argparse.FileType('a'),default=sys.stdout)
    args = parser.parse_args()
    if args.config:
        config = configparser.ConfigParser()
        config.read_file(args.config)
        #transforming values into integers
        args.number1 = int(config['ARGUMENTS']['number1'])
        args.number2 = int(config['ARGUMENTS']['number2'])
        main(args.number1,args.number2,args.output)
#