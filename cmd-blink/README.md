cmd-blink
=========

Simple function definition to emulate the --blink option found in blink1-tool
for the blink(1) USB device.

Prerequisites
-------------

- blink1.py - This code uses Stephen Youndt's blink1.py library available in the 
thingm GetSatisfaction forum at 
[(link)](https://getsatisfaction.com/thingm/topics/more_comprehensive_python_support), 
and which should also soon be available via their 
[(github repo)](https://github.com/todbot/blink1).

- blink1-lib.so - Found in thingm's github repo (under commandline)

Notes
-----

- In testing, I found that without the added sleep(1) delays, the command
only worked about 10% of the time.

SS
  

