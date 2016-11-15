#! /usr/bin/env python

from __future__ import print_function
import sys


import logging

logging.basicConfig(filename='captured_tweets_error.log', filemode='w', format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)
logging.basicConfig(filename='captured_tweets_error.log', level=logging.DEBUG)
log = logging.getLogger(__name__)


log.debug('very granular')
log.info('simple update')
#log.warning('Youve seen these in sklearn, warning about methods being deprecated')
#log.error('Logs an error message')
#log.critical('Well this is an issue')


import twitter


if __name__ == '__main__':
    results = twitter.retrieve_tweets(topic=sys.argv[1])
    out = open('captured-tweets.txt', 'ab')
    # The tweet is stored with key 'text',
    i = 0
    for result in results:
        # Filter to english tweets
        log.info('This is English')
        if result['lang'] == 'en':
        
            out.write((result['text'] + "\n").encode('utf-8'))
            i += 1
        # Defaulting to capturing 5000, this takes a long time...This part changes quantity
        if i == 50:      #This part changes quantity
            log.critical('Not enough')
            exit()