import urllib             # For BasicHTTPAuthentication
import feedparser         # For parsing the feed
from textwrap import wrap # For pretty printing assistance
import pyautogui

_URL = "https://mail.google.com/gmail/feed/atom"

def auth():
    #method to do HTTPBasicAuthentication
    opener = urllib.FancyURLopener()
    pyautogui.typewrite('anjaligaur1969')
    pyautogui.press('enter')
    pyautogui.typewrite('Anjali23021969')
    pyautogui.press('enter')
    f = opener.open(_URL)
    feed = f.read()
    return feed

def fill(text, width):
    #method to assist in pretty printing
    if len(text) < width:
        return text # + ' '*(width-len(text))
    else:
        return text

def readmail(feed):
    #Parse the Atom feed and print a summary
    atom = feedparser.parse(feed)
    print ""
    print atom.feed.title
    print "You have %s new mails" % len(atom.entries)
   # Mostly pretty printing magic
   # print "+"+("-"*84)+"+"
   # print "| Sl.|"+" Subject"+' '*48+"|"+" Author"+' '*15+"|"
   # print "+"+("-"*84)+"+"
    for i in xrange(len(atom.entries)):
        print " %s %s %s" % (
            fill(str(i), 3),
            fill(wrap(atom.entries[i].title, 50)[0]+"[...]", 55),
            fill(wrap(atom.entries[i].author, 15)[0]+"[...]", 21))
    #print "+"+("-"*84)+"+"

if __name__ == "__main__":
    f = auth()  # Do auth and then get the feed
    readmail(f) # Let the feed be chewed by feedparser