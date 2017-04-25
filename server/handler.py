from tornado import ioloop , web , httpserver , websocket, options 
import os
import random
import string
from wavsplite import wavSplit
static_url = os.path.join(os.path.dirname(__file__))

class MainHandler(web.RequestHandler):
    def get(self):
        self.render("static/client.html")

class WavFileHandler(web.RequestHandler):
	def post(self):
		file1 = self.request.files['wav_file'][0]
		original_fname = file1['filename']
		extension = os.path.splitext(original_fname)[1]
		fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(8))
		dirname = "uploads"
		final_filename= os.path.join(os.path.dirname(__file__),dirname,fname+extension)
		output_file = open(final_filename, 'w')
		output_file.write(file1['body'])
		text_lists = wavSplit(final_filename)
		print text_lists
		self.redirect("/")