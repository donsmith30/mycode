#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   For - Using a file's lines as a source for the for-loop"""

def main():

    # open file in read mode
    with open("dnsservers.txt", "r") as dnsfile:
        for svr in dnsfile:
            svr = svr.rstrip('\n')

            if svr.endswith('org'):
                with open("org-domain.txt", "a") as srvfile:  # 'a' is append mode
                    srvfile.write(svr + "\n")
        # ELSE-IF the string svr ends with 'com'
            elif svr.endswith('com'):
                with open("com-domain.txt", "a") as srvfile:  # 'a' is append mode
                    srvfile.write(svr + "\n")


if __name__ == "__main__":
    main()
