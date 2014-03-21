py-api-streaming
================

A demo app in Python for streaming rates using OANDA open api

### Setup

Clone this repo to the location of your choice

Update the following information in connect_to_stream method in streaming.py:

    domain
    accountId
    access token (Authorization)

To execute, run the following command:

    python streaming.py [options]

    options:

    -b (or --displayHeartBeat):    A flag to determine whether HeartBeat will be displayed

### Sample Output

	{"instrument":"EUR_USD","time":"2014-03-07T20:58:07.461445Z","bid":1.38701,"ask":1.38712}
	{"instrument":"EUR_USD","time":"2014-03-07T20:58:09.345955Z","bid":1.38698,"ask":1.38709}
	{"instrument":"USD_CAD","time":"2014-03-07T20:58:12.320218Z","bid":1.10906,"ask":1.10922}
	{"instrument":"USD_CAD","time":"2014-03-07T20:58:12.360615Z","bid":1.10904,"ask":1.10925}

### More Information

http://developer.oanda.com/