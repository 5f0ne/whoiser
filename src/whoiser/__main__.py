import sys
import argparse

from ipwhois import IPWhois
from prettytable import PrettyTable

from whoiser.Controller import Controller

def main(args_=None):
    """The main routine."""
    if args_ is None:
        args_ = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("--path", "-p", type=str, required=True, help="Path to list of IPs")
    args = parser.parse_args()

    c = Controller()

    c.printHeader()

    x = PrettyTable()
    x.field_names = ["Query", "CIDR", "Range", "Network Name", "Contact Name"]

    with open(args.path, "r") as f:
        while True:
            ip = f.readline().replace("\n", "")

            if not ip:
                break
            
            r = IPWhois(ip)

            result = r.lookup_rdap(depth=1)
            query = result["query"]
            cidr = result["network"]["cidr"]
            range = str(result["network"]["start_address"]) + " - " + str(result["network"]["end_address"])

            name = "-/-"
            if(result["network"]["name"] != None):
                netName = str(result["network"]["name"])

            contactName = "-/-"
            if(len(result["entities"]) > 0):
                contactName = result["objects"][result["entities"][0]]["contact"]["name"]

            
            x.add_row([query, cidr, range, netName, contactName])

    print(x)
    c.printExecutionTime()

if __name__ == "__main__":
    sys.exit(main())


