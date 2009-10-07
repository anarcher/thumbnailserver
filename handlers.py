import tornado.web
import os
import stat
import mimetypes

class BaseHandler(tornado.web.RequestHandler):
    pass

class HelloHandler(BaseHandler):
    def get(self):
        FILEPATH = "./a.jpg"
        file = open(FILEPATH)
        stat_result = os.stat(FILEPATH)
        self.set_header("Content-Length",stat_result[stat.ST_SIZE])
        mime_type, encoding = mimetypes.guess_type(FILEPATH)
        if mime_type:
            self.set_header("Content-Type", mime_type)

        try:
            self.write(file.read()) 
        finally:
            file.close()
