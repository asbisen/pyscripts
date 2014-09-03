#!/usr/bin/env python

__author__    = "Anand Bisen <abisen at gmail.com>"
__date__      = "05-05-2014"

import sys
import gzip
import os.path
import argparse
import datetime

try:
	from tweepy import Stream
	from tweepy import OAuthHandler
	from tweepy.streaming import StreamListener

except ImportError:
	print "Error: Unable to import tweepy, check if the module is installed"
	sys.exit(1)

class listener(StreamListener):

	def __init__(self, rotate_count, data_dir, api=None):
		super(listener, self).__init__()

		self.rotate_count = rotate_count
		self.data_dir = data_dir

		self.counter = 0
		self.rotate_count = 1000

	def on_data(self, data):
		if self.counter == 0:

			# Create a new datafile
			self.fullpath = os.path.join( self.data_dir, self.getFileName() )
			self.fd = gzip.open( self.fullpath, "w" )
			self.fd.write ( data )
			
			# Increment counter 
			self.counter = self.counter + 1
			print "Writing to datafile:", self.fullpath

			# Progress Indicator
			sys.stdout.write('.')
			sys.stdout.flush()
			
		# Write data till the counter is less than chunk count
		elif (self.counter > 0) & (self.counter < self.rotate_count):
			self.fd.write( data )

			# Increment counter
			self.counter = self.counter + 1

			# Progress Indicator
			sys.stdout.write('.')
			sys.stdout.flush()

		# Close the file when the chunk count is reached and reset the counter
		else:
			self.fd.write( data )
			self.fd.close()

			# Reset the counter
			self.counter = 0
			print "\nclosing file:", self.fullpath

		return True

	def on_error(self, status):
		print status

	# Helper function to generate a unique filename
	def getFileName(self, rootname="data-"):
		timestamp = datetime.datetime.now().strftime("%d-%m-%Y-%H-%M-%S")
		return rootname + timestamp + ".dat.gz"


if __name__ == "__main__":

	parser = argparse.ArgumentParser()
	
	parser.add_argument("api_key",       help="Twitter API Key")
	parser.add_argument("api_secret",    help="Twitter API Secret")
	parser.add_argument("access_token",  help="Twitter Access Token")
	parser.add_argument("access_secret", help="Twitter Access Secret")
	parser.add_argument("watch",         help="Comma delimited keywords to watch")

	parser.add_argument("--data-dir",    type=str, default="./",  help="Directory location to capture tweets")
	parser.add_argument("--chunk-size",  type=int, default=1000,  help="Number of chunks per data file (Default: 1000)")
	
	args = parser.parse_args()

	# StdOut
	print "Authenticating with Twitter....."

	auth = OAuthHandler(args.api_key, args.api_secret)
	auth.set_access_token(args.access_token, args.access_secret)

	keywords = [i for i in args.watch.split(",")]

	# StdOut
	print "Listening on:", keywords
	print "Chunk Size:", args.chunk_size
	print "Data Dir:", args.data_dir

	twitterStream = Stream( auth, listener( args.chunk_size, args.data_dir ) )
	twitterStream.filter(track=keywords)




