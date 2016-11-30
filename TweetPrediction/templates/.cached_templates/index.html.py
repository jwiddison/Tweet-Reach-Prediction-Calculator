# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1479240875.786022
_enable_loop = True
_template_filename = '/Users/Jordan/Documents/BYU/0 - MISM - 1/Fall 2016/IS 415/NuviProject/TweetPrediction/templates/index.html'
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <nav class="navbar navbar-default navbar-fixed-top topnav" role="navigation">\n    <div class="container topnav">\n      <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n          <span class="sr-only">Toggle navigation</span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand topnav" href="#">Nuvi Project</a>\n      </div>\n      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n        <ul class="nav navbar-nav navbar-right">\n          <li><a href="#about">About</a></li>\n          <li><a href="#prediction">Prediction</a></li>\n          <li><a href="#dashboard">Dashboard</a></li>\n        </ul>\n      </div>\n    </div>\n  </nav>\n\n  <div class="intro-header">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-12">\n          <div class="intro-message">\n            <h1>415 Nuvi Project</h1>\n            <h3>Subtitle</h3>\n            <hr class="intro-divider">\n            <ul class="list-inline intro-social-buttons">\n              <li>\n                <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>\n              </li>\n              <li>\n                <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>\n              </li>\n              <li>\n                <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>\n              </li>\n            </ul>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n\n\n\n  <a name="about"></a>\n  <div class="content-section-a">\n    <div class="container">\n        <div class="row">\n          <div class="col-lg-5 col-sm-6">\n            <hr class="section-heading-spacer">\n            <div class="clearfix"></div>\n            <h2 class="section-heading">Gonna Put Some Info Here</h2>\n            <p class="lead">Gonna put a graph or something over there. --></p>\n          </div>\n          <div class="col-lg-5 col-lg-offset-2 col-sm-6">\n            <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/ipad.png" alt="">\n          </div>\n      </div>\n    </div>\n  </div>\n\n  <div class="content-section-b">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-5 col-lg-offset-1 col-sm-push-6  col-sm-6">\n          <hr class="section-heading-spacer" />\n          <div class="clearfix"></div>\n          <h2 class="section-heading">Put Some More Info Here.</h2>\n          <p class="lead">Another graph or something probably.  Maybe something about people posting about their pets on social media.</p>\n        </div>\n        <div class="col-lg-5 col-sm-pull-6  col-sm-6">\n          <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/dog.png" alt="">\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <a  name="prediction"></a>\n  <div class="content-section-a">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-5 col-sm-6">\n          <hr class="section-heading-spacer">\n          <div class="clearfix"></div>\n')
        __M_writer('          <form method="POST">\n            ')
        __M_writer(str(form.as_table()))
        __M_writer('\n            <input type="submit" class="btn btn-default" />\n          </form>\n        </div>\n        <div class="col-lg-5 col-lg-offset-2 col-sm-6">\n          <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/phones.png" alt="">\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <a  name="dashboard"></a>\n  <div class="content-section-b">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <hr class="section-heading-spacer" />\n          <div class="clearfix"></div>\n          <h2 class="section-heading">Dashboard</h2>\n          <p>Gonna put the tableau dashboard in here maybe.</p>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-6">\n          <h2>Social Media Buttons \'Cause Millenials:</h2>\n        </div>\n        <div class="col-lg-6">\n          <ul class="list-inline banner-social-buttons">\n            <li>\n              <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>\n            </li>\n            <li>\n              <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>\n            </li>\n            <li>\n              <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>\n            </li>\n          </ul>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <footer>\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-12">\n')
        __M_writer('          <p class="copyright text-muted small">Copyright &copy; 2016. All Rights Reserved</p>\n        </div>\n      </div>\n    </div>\n  </footer>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "filename": "/Users/Jordan/Documents/BYU/0 - MISM - 1/Fall 2016/IS 415/NuviProject/TweetPrediction/templates/index.html", "line_map": {"64": 100, "65": 100, "66": 164, "37": 1, "72": 66, "60": 79, "42": 170, "48": 3, "56": 3, "57": 63, "58": 63, "59": 79, "28": 0, "61": 94, "62": 95, "63": 95}, "source_encoding": "utf-8"}
__M_END_METADATA
"""
