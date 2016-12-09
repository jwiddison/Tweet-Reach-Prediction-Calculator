# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481299539.9883156
_enable_loop = True
_template_filename = 'C:/Users/Sean/Desktop/NuviProject/TweetPrediction/templates/base.htm'
_template_uri = 'base.htm'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


from django_mako_plus import get_template_css, get_template_js 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        self = context.get('self', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    <title>Nuvi Tweet Prediction</title>\r\n    <link rel="icon" type="img/ico" href="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/nuvi-favicon.ico">\r\n    <meta charset="utf-8">\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">\r\n    <meta name="HandheldFriendly" content="True">\r\n    <meta name="MobileOptimized" content="320">\r\n    <meta name="viewport" content="initial-scale=1.0, minimum-scale=1.0, user-scalable=0">\r\n    <meta name="apple-mobile-web-app-capable" content="yes">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1.0">\r\n\r\n    <!-- CSS -->\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/bootstrap/css/bootstrap.min.css" />\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/styles/landing-page.css" >\r\n    ')
        __M_writer(str( get_template_css(self, request, context) ))
        __M_writer('\r\n    <!-- Fonts -->\r\n    <link rel="stylesheet" type="text/css" href="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/font-awesome/css/font-awesome.min.css" >\r\n    <link rel="stylesheet" type="text/css" href="https://fonts.googleapis.com/css?family=Lato|Raleway:300,400,700,300italic,400italic,700italic" >\r\n  </head>\r\n  <body>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <script src="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/bootstrap/js/bootstrap.min.js"></script>\r\n    ')
        __M_writer(str( get_template_js(self, request, context) ))
        __M_writer('\r\n  </body>\r\n</html>\r\n')
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
{"filename": "C:/Users/Sean/Desktop/NuviProject/TweetPrediction/templates/base.htm", "uri": "base.htm", "source_encoding": "utf-8", "line_map": {"32": 18, "33": 18, "34": 19, "35": 19, "36": 20, "37": 20, "38": 22, "39": 22, "44": 26, "45": 28, "46": 28, "47": 29, "48": 29, "17": 1, "19": 0, "54": 26, "65": 54, "29": 1, "30": 7, "31": 7}}
__M_END_METADATA
"""
