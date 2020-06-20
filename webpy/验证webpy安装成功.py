# coding=utf-8

import web

urls = (
    '/(.*)', 'hello'
)
app = web.application(urls, globals())

class hello:
    def GET(self, name):
        if not name:
            name = 'mm'
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return 'Hello, ' + name + '!'

if __name__ == "__main__":
    app.run()