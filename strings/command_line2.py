import argparse
def main(charctere,number):
    print(charctere*number)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='printing a number of charactere')
    parser.add_argument('number',type=int , help='a number')
    parser.add_argument('-c',type=str , help='a charactere to print', default = '#')
    parser.add_argument('-U',help='print charactere uppercase',action='store_true' ,default = False,
                            dest='uppercase')
    args = parser.parse_args()
    if args.uppercase:
        args.c=args.c.upper()
    main(args.c,args.number)

