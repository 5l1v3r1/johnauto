#!/usr/bin/python
import sys
import argparse
import subprocess
import shutil

print("""
                                 __ _       _           
 _   _  ___  _   _ ___ ___  ___ / _(_) ___ | |__  _ __  
| | | |/ _ \| | | / __/ __|/ _ \ |_| |/ _ \| '_ \| '_ \ 
| |_| | (_) | |_| \__ \__ \  __/  _| | (_) | | | | | | |
 \__, |\___/ \__,_|___/___/\___|_|_/ |\___/|_| |_|_| |_|
 |___/                           |__/               
 """)
print("facebook:youssefslimene")
print("github:https://github.com/youhacker55")


def cleanup_routine():
    '''Cleanup old files and processes'''
    
    try:
        # Delete old temp files if the user wants to; default to leave old files
        response = raw_input("\nDelete old JTR session data (enter no if you want to keep old hashes, etc)? [no]")
        if "y" in response or "Y" in response:
            print("Deleting temp files...\n")
            shutil.rmtree("~/.john", True)
        else:             
            pass

    except:
        pass


def main(argv):
    
    parser = argparse.ArgumentParser(description='Automation script for JTR hash cracking.')
    parser.add_argument("infile", action="store", help="Input file containing hashes")
    parser.add_argument("--hashtype", "--t", action="store", help='Optional hash type (lm, nt, netntlmv2; defaults to nt)')
    args = parser.parse_args()
    
    inputfile = args.infile
    hashtype = args.hashtype
    wordlistdir = "~/hacking/dictionaries/"
    
    if hashtype == None:
        hashtype="nt"
    
    print "cleaning old JTR sessions"
    
    subprocess.Popen("john --single --format="+hashtype+" " + inputfile, shell=True).wait()
    subprocess.Popen("john --wordlist="+wordlistdir+"wordlists/numbers.txt --rules --format="+hashtype+" " + inputfile, shell=True).wait()
    subprocess.Popen("john --wordlist="+wordlistdir+"wordlists/names.txt --rules --format="+hashtype+" " + inputfile, shell=True).wait()
    subprocess.Popen("john --wordlist="+wordlistdir+"combined_all_unix.txt --rules --format="+hashtype+" " + inputfile, shell=True).wait()
    
    subprocess.Popen("john --wordlist="+wordlistdir+"combined_wordlists_unix.txt --rules=single --format="+hashtype+" " + inputfile, shell=True).wait()
    
    subprocess.Popen("john --show --format="+hashtype+" " + inputfile + "| cut -d: -f1,2", shell=True).wait()

if __name__ == "__main__":
    main(sys.argv[1:])
