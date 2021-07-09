
import argparse

parser = argparse.ArgumentParser(description='usage: python3 -f dictionary -p password')
parser.add_argument('-f')
parser.add_argument('-p')

args = parser.parse_args()

password = args.p

file1 = open(args.f)

readfile = file1.read()

if password in readfile: 
    print('Your Password is vulnerable against brute force!!')
else: 
    print('Password Not Found') 

file1.close() 
