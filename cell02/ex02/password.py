#!/usr/bin/env python3
def main(u_password):
    password = "Puthon is awesome"
    if u_password == password:
        print("ACCESS GRANTED.")
    else:
        print("ACCESS DENIED.")
main(input())