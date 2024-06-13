import os, sys
try:
    __import__("ooc").main()
except Exception as e:
    exit(str(e))