import sys
import argparse
import math_lib as ml


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
                                 description = 'Gives sum and division (if non-zero) of two integers'
                                 )
    parser.add_argument('--int1',
                        type = int, 
                        help = 'First number and numberator',  # INFORMATION FOR THE BUILT IN --HELP METHOD
                        required = True) #default is false

    parser.add_argument('--int2',
                        type = int, 
                        help = 'Second number and denominator',
                        required = True)

    args = parser.parse_args()
    
    print("here are the sum and division of your given numbers:")
    
    print("%a + %a = %a" % (args.int1, args.int2, ml.add(args.int1, args.int2) ) )
    
    if args.int2 == 0:
          print("cannot divide by zero")
          sys.exit(1)
    else:
          print("%a / %a = %a" % (args.int1, args.int2, ml.div(args.int1, args.int2) ) )
                
    sys.exit(0)