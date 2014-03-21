"""
Demonstrates streaming feature in OANDA open api

To execute, run the following command:

python streaming.py [options]

To show heartbeat, replace [options] by -b or --displayHeartBeat
"""

import requests
import json

from optparse import OptionParser

def connect_to_stream():
    """
    For your testing, please use a proper domain (like stream-fxpractice/fxtrade) with your access token and account ID

    Feel free to include more instruments (10 instruments at most)
    """

    try:
        s = requests.Session()
        url = "https://<domain>/v1/quote"
        headers = {'Authorization' : 'Bearer <your access token>'}
        params = {'instruments' : 'EUR_USD,USD_CAD', 'accountId' : '<your account ID>'}
        req = requests.Request('GET', url, headers = headers, params = params)
        pre = req.prepare()
        resp = s.send(pre, stream = True, verify = False)
        return resp
    except Exception as e:
        s.close()
        print "Caught exception when connecting to stream\n" + str(e) 

def demo(displayHeartbeat):
    response = connect_to_stream()
    for line in response.iter_lines(1):
        if line:
            try:
                msg = json.loads(line)
            except Exception as e:
                print "Caught exception when convert message into json\n" + str(e)
            
            if displayHeartbeat:
                print line
            else:
                if msg.has_key("instrument"):
                    print line

def main():
    usage = "usage: %prog [options]"
    parser = OptionParser(usage)
    parser.add_option("-b", "--displayHeartBeat", dest = "verbose", action = "store_true", 
                        help = "Display HeartBeat in streaming data")
    displayHeartbeat = False

    (options, args) = parser.parse_args()
    if len(args) > 1:
        parser.error("incorrect number of arguments")
    if options.verbose:
        displayHeartbeat = True
    demo(displayHeartbeat)


if __name__ == "__main__":
    main()