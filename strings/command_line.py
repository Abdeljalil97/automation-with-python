import argparse
def main(parametre):
    print("#"*parametre)
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('number',type=int , help='a number')
    args = parser.parse_args()
    main(args.number)