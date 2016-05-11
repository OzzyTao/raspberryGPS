import sys
import time
from daemon import runner
from httplib2 import Http
import argparse
import json


class Monitor(object):
	"""docstring for Monitor"""
	def __init__(self, args):
		super(Monitor, self).__init__()
		self.stdin_path = '/dev/null'
		self.stdout_path = '/Users/ozzytao/projects/raspberrypi/gps_daemon/log/stdout'
		self.stderr_path = '/Users/ozzytao/projects/raspberrypi/gps_daemon/log/stderr'
		self.pidfile_path =  '/Users/ozzytao/projects/raspberrypi/gps_daemon/log/testdaemon.pid'
		self.pidfile_timeout = 50

		self.url = args.url or "http://127.0.0.1:1234/"
		self.freq = args.frequency or 5
		self.user = args.username or "test" 
		self.h =Http(".cache")
		
	def run(self):
		while True:
			self.post()
			time.sleep(self.freq)

	def post(self):
		timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
		payload = {'username':self.user,'lat':0.0,'lon':0.0,'timestamp':timestr}
		resp,content = self.h.request(self.url,"POST",body=json.dumps(payload),headers={'content-type':'application/json'})
		print timestr



if __name__ == '__main__':
	parser = argparse.ArgumentParser(prog='gps.py')
	parser.add_argument('cmd',choices=['start', 'stop', 'restart'])
	parser.add_argument('--url',help="URL for server", required=False)
	parser.add_argument('--username',help="Identification for the device", required=False)
	parser.add_argument('--frequency',help="Frequency for posting GPS data", required=False)
	argsDict = parser.parse_args()
	daemon_runner = runner.DaemonRunner(Monitor(argsDict))
	daemon_runner.do_action()
