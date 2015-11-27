#!/usr/bin/env python3

import logging;logging.basicConfig(level=logging.INFO)

import asyncio,os,json,time
from datetime import datetime

from aiohttp import web
import orm

def index(request):
	h_body = b'<h1>Hello</h1>'
	return web.Response(body=h_body)

@asyncio.coroutine
def init(loop):
	yield from orm.create_pool(loop=loop,\
#			host='1d1816801.gz.cdb.myqcloud.com',\
#			port=5630,user='root',password='2016@chrome',db='test')
			host='127.0.0.1',\
			port=3306,user='root',password='1234',db='mysql')

	app = web.Application(loop=loop)
	app.router.add_route('GET','/',index)
	srv = yield from loop.create_server(app.make_handler(),\
			'',8080)
	logging.info('server started at port:8080...')
	return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()
