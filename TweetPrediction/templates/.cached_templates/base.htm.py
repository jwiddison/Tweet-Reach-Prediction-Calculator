# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481259450.9616292
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
        self = context.get('self', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n  <head>\r\n    <title>Nuvi Project</title>\r\n\r\n    <meta charset="utf-8">\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1">\r\n    <meta name="description" content="">\r\n    <meta name="author" content="">\r\n\r\n    <title>Landing Page - Start Bootstrap Theme</title>\r\n\r\n    <!-- CSS -->\r\n    <link rel="stylesheet" type="text/css" href="')
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
        

        __M_writer('\r\n    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    ')
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
        __M_writer('\r\n      Site content goes here in sub-templates.\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"32": 18, "33": 18, "34": 19, "35": 19, "36": 21, "37": 21, "42": 27, "43": 29, "44": 29, "17": 1, "50": 25, "19": 0, "62": 56, "56": 25, "29": 1, "30": 17, "31": 17}, "filename": "C:/Users/Sean/Desktop/NuviProject/TweetPrediction/templates/base.htm", "source_encoding": "utf-8", "uri": "base.htm"}
__M_END_METADATA
"""
