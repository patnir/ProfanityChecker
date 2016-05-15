# -*- coding: utf-8 -*-
"""
Created on Sun May 15 14:55:24 2016

@author: Rahul Patni
"""
import urllib

def read_text():
    quotes = open("C:\Users\SUNITA\Documents\Python Scripts\movie_quotes.txt")    
    contents = quotes.read()
    #print contents    
    quotes.close()
    check_profanity(contents)
    
def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q=" + text_to_check)
    output = connection.read()
    #print output
    connection.close()
    if (output == "true"):
        print "There is profanity in this document."
    else:
        print "No profanity found in this document."
read_text()