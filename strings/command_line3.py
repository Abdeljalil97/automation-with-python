import argparse
def main(charctere,number):
    print(charctere*number)
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='printing a number of charactere')
    parser.add_argument('number',type=int , help='a number')
    parser.add_argument('-c',type=str , help='a charactere to print', default = '#')
    args = parser.parse_args()
    main(args.c,args.number)