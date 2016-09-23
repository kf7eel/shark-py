#!/usr/bin/python
import shark
import sys, getopt, requests, json, re
from hashlib import sha256

shark.password = 'openspot'
shark.ip = 'openspot.local'
shark.tmp = '/tmp/.shark.auth'

def show_usage():
 print('''
  usage: ./shark.py
   display status

  usage: ./shark.py -g <talkgroup> -m <mode> -f <frequency>
   -m   idle/dmr/c4fm/dstar
   -g   dmr talkgroup number
   -f   frequency in MHz
  
  ex:
   ./shark.py
   ./shark.py -g 4639 -m c4fm
   ./shark.py -m dmr -f 433.1
   ./shark.py -g 0
  ''')
 exit()

def show_info():
 print("Status: " + shark.get_status()['status'])
 print("Connector: " + shark.get_connector())
 print("Recieve Freq: " + shark.get_freq()['rx'])
 print("Transmit Freq: " + shark.get_freq()['tx'])
 print("Mode: " + shark.get_mode()['mode'] + " (" + shark.get_mode()['submode'] +")")
 print("Talkgroup: " + shark.get_status()['room'])

def args(argv):
 try:
  opts, args = getopt.getopt(argv,"hf:m:g:")
 except getopt.GetoptError:
  show_usage()
 for opt, arg in opts:
  if opt == '-h':
   show_usage()
  elif opt == '-f':
   shark.set_freq(arg)
  elif opt == '-m':
   print(shark.set_mode(arg))
  elif opt == '-g':
   shark.set_talkgroup(arg)

shark.do_checkauth()
args(sys.argv[1:])
if len(sys.argv) <= 1:
 show_info()