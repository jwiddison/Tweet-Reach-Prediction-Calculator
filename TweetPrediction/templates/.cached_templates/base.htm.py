# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481330389.906465
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - MISM - 1/Fall 2016/IS 415/NuviProject/TweetPrediction/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n<!DOCTYPE html>\n<html>\n  <meta charset="UTF-8">\n  <head>\n    <title>Nuvi Tweet Prediction</title>\n    <link rel="icon" type="img/ico" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/nuvi-favicon.ico">\n    <meta charset="utf-8">\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\n    <meta http-equiv="Content-Type" content="text/html">\n    <meta name="HandheldFriendly" content="True">\n    <meta name="MobileOptimized" content="320">\n    <meta name="viewport" content="width=device-width, initial-scale=1.0, minimum-scale=1.0, user-scalable=0">\n    <meta name="apple-mobile-web-app-capable" content="yes">\n\n    <!-- CSS -->\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/bootstrap/css/bootstrap.min.css" />\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/styles/landing-page.css" >\n    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\n    <!-- Fonts -->\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/font-awesome/css/font-awesome.min.css" >\n    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Lato|Raleway:300,400,700,300italic,400italic,700italic" >\n  </head>\n  <body>\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/bootstrap/js/bootstrap.min.js"></script>\n    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\n  </body>\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 17, "33": 17, "34": 18, "35": 18, "36": 19, "37": 19, "38": 21, "39": 21, "44": 25, "45": 27, "46": 27, "47": 28, "48": 28, "17": 1, "19": 0, "54": 25, "65": 54, "29": 1, "30": 7, "31": 7}, "filename": "/Users/Jordan/Documents/BYU/0 - MISM - 1/Fall 2016/IS 415/NuviProject/TweetPrediction/templates/base.htm", "uri": "base.htm"}
__M_END_METADATA
"""
