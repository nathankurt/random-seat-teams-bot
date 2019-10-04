#!/usr/bin/env python3
import random, argparse


parser = argparse.ArgumentParser()
parser.add_argument("-r", "--rows", help="how many rows defaults to 2")
parser.add_argument("-c", "--cols", help="how many cols defaults to 2")
args = parser.parse_args()

if args.rows:
    try:
        rows = int(args.rows)

    except:
        print("Arguments must be integer... using 2 as default rows\n")
        rows = 2
else:
    rows = 2

if args.cols:
    try:
        cols = int(args.cols)
    except:
        print("Arguments must be integers... using 2 as default cols\n")
        cols = 2
else:
    cols = 2

name_ls = ["Nate", "Ben", "Laurent", "Gabe", "Jessy", "Imran", "Dionte", "Sakib"]
random.shuffle(name_ls)


string = "FRONT OF CLASS"
#print(f"{string:^50}")
#longest_name_len = max(len(x) for x in name_ls)

for i in range(cols):
    for j in range(rows):
        if(name_ls):
            # 2 per table so pop both names from list then put in front left.
            name1 = name_ls.pop(0)
            name2 = name_ls.pop(0)
            #table = f"{name1:^{longest_name_len}}   {name2:^{longest_name_len}}                           "
            #can't use thing above because it doesn't like text formatting that way
            #11 and 7 just got from experimenting and playing around with names
            table = f"{name1:>11}   {name2:<7}"
            #print(table, end="    ")
    #print("\n")
print("You guys make me sad")






    


