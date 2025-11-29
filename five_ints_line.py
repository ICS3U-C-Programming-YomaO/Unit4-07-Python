#!/usr/bin/env python3
# Created By: Yoma Ozoh
# Date: November, 2025
# This program counts by 5 from 1000 to 2000

def main():

   for year in range(1000, 2001, 1):
       
       print(year, end=" ")
       
       # Print a new line after every 5 numbers

       if year % 5 == 0:

           print()

   # Print end message

   print("\nThanks for playing!")

if __name__ == "__main__":

   main()
