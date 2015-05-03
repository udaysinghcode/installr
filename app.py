#!/usr/bin/env python

from flask import Flask, request
app = Flask(__name__)
app.debug = True

@app.route('/i/<url>')
def url_return_install(url):
  returnValue = ""
  if (url.find("%") != -1):
    # do stuff to pull it out
    wordList = url.split("%")
    for word in wordList:
      returnValue += 'brew_cask_install "' + word + '"<br/>'
  else:
    returnValue += 'brew_cask_install "' + url + '"'
  return returnValue
 
@app.route('/u/<url>')
def url_return_uninstall(url):
  returnValue = ""
  if (url.find("%") != -1):
    # do stuff to pull it out
    wordList = url.split("%")
    for word in wordList:
      returnValue += 'brew_cask_uninstall \'' + word + '\'\n'
  else:
    returnValue += 'brew_cask_uninstall "' + url + '"'
  return returnValue
 
if __name__ == '__main__':
    app.run()