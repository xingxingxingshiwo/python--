# coding=utf-8

import web

# url组织
urls = ("/.*", "hello")

#
app = web.application(urls, globals())


class hello:
    def GET(self):
        web.header('Content-Type', 'text/json; charset=utf-8', unique=True)
        return 'Hello, world!'


if __name__ == "__main__":
    app.run()
