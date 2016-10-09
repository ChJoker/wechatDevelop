import router
import tornado.ioloop
import tornado.web
import tornado.httpserver

settings = {
    "debug": 1,
    "cookie_secret": 'xuyung_JingGle'
}

def main():
    app = tornado.web.Application(router.url_map)
    server = tornado.httpserver.HTTPServer(app)
    server.bind(8080)
    server.start(3)

    tornado.ioloop.IOLoop.instance().start()

if __name__ == '__main__':
    main()
