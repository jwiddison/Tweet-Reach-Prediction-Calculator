# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478826417.199022
_enable_loop = True
_template_filename = '/Users/Jordan/Desktop/415MLStudio/TweetPrediction/templates/index.html'
_template_uri = 'index.html'
_source_encoding = 'utf-8'
import os, os.path, re, json
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        result = context.get('result', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        result = context.get('result', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class="container">\n    <div class="row">\n      <div class="col-md-12">\n        <h1>IS415 NuviProject Loan Calculator</h1>\n        <hr />\n      </div>\n    </div>\n    <div class="row">\n      <div class="col-md-6">\n        <h3>Enter Loan Information:</h3>\n        <form id="prediction_form" method=\'POST\'>\n          <table id="prediction_table">\n            ')
        __M_writer(str(form.as_table()))
        __M_writer('\n          </table>\n          <input type="submit" class="btn btn-primary" value="Get a Prediction">\n        </form>\n      </div>\n      <div class="col-md-6">\n        <p>\n          <div id="response_placeholder">\n            ')
        __M_writer(str(result))
        __M_writer('\n          </div>\n        </p>\n      </div>\n    </div>\n  </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "/Users/Jordan/Desktop/415MLStudio/TweetPrediction/templates/index.html", "uri": "index.html", "line_map": {"48": 3, "66": 60, "37": 1, "56": 3, "57": 16, "42": 30, "59": 24, "28": 0, "58": 16, "60": 24}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
