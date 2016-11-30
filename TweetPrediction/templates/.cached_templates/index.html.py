# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1480548231.6753843
_enable_loop = True
_template_filename = 'C:/Users/Sean/Desktop/NuviProject/TweetPrediction/templates/index.html'
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
        result = context.get('result', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        result = context.get('result', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <nav class="navbar navbar-default navbar-fixed-top topnav" role="navigation">\r\n    <div class="container topnav">\r\n      <div class="navbar-header">\r\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n          <span class="sr-only">Toggle navigation</span>\r\n          <span class="icon-bar"></span>\r\n          <span class="icon-bar"></span>\r\n          <span class="icon-bar"></span>\r\n        </button>\r\n        <a class="navbar-brand topnav" href="#">Nuvi Project</a>\r\n      </div>\r\n      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n        <ul class="nav navbar-nav navbar-right">\r\n          <li><a href="#about">About</a></li>\r\n          <li><a href="#prediction">Prediction</a></li>\r\n          <li><a href="#dashboard">Dashboard</a></li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n  </nav>\r\n\r\n  <div class="intro-header">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <div class="intro-message">\r\n            <h1>Nuvi Project</h1>\r\n            <h3>Put the text of your tweet in the field below to predict the reach</h3>\r\n            <hr class="intro-divider">\r\n            <div class="row">\r\n              <div class="col-md-6 col-md-offset-3">\r\n                <form method="POST">\r\n                  ')
        __M_writer(str(form.as_p()))
        __M_writer('\r\n                  <input type="submit" class="btn btn-primary center-block" value="Predict Reach"/>\r\n                </form>\r\n                <p>RESULT: ')
        __M_writer(str(result))
        __M_writer('</p>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n\r\n\r\n  <a name="about"></a>\r\n  <div class="content-section-a">\r\n    <div class="container">\r\n        <div class="row">\r\n          <div class="col-lg-5 col-sm-6">\r\n            <hr class="section-heading-spacer">\r\n            <div class="clearfix"></div>\r\n            <h2 class="section-heading">Twitter</h2>\r\n            <p class="lead">Something about why twitter matters</p>\r\n          </div>\r\n          <div class="col-lg-5 col-lg-offset-2 col-sm-6">\r\n            <img class="img-responsive img-thumbnail" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/tablet_twitter.jpeg" alt="">\r\n          </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <div class="content-section-b">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-lg-5 col-lg-offset-1 col-sm-push-6  col-sm-6">\r\n          <hr class="section-heading-spacer" />\r\n          <div class="clearfix"></div>\r\n          <h2 class="section-heading">Predicting Reach</h2>\r\n          <p class="lead">Another graph or something probably.  Maybe something about people posting about their pets on social media.</p>\r\n        </div>\r\n        <div class="col-lg-5 col-sm-pull-6  col-sm-6">\r\n          <img class="img-responsive img-thumbnail" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/graph.jpeg" alt="">\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <a  name="prediction"></a>\r\n  <div class="content-section-a">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-6 col-md-offset-3">\r\n          <hr class="section-heading-spacer">\r\n          <div class="clearfix"></div>\r\n          <form method="POST">\r\n            ')
        __M_writer(str(form.as_p()))
        __M_writer('\r\n            <input type="submit" class="btn btn-primary center-block" value="Predict Reach"/>\r\n          </form>\r\n          <p>RESULT: ')
        __M_writer(str(result))
        __M_writer('</p>\r\n        </div>\r\n')
        __M_writer('      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <a  name="dashboard"></a>\r\n  <div class="content-section-b">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <hr class="section-heading-spacer" />\r\n          <div class="clearfix"></div>\r\n          <h2 class="section-heading">Dashboard</h2>\r\n          <p>Gonna put the tableau dashboard in here maybe.</p>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <div class="banner">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-lg-6">\r\n          <h2>Social Media Buttons \'Cause Millenials:</h2>\r\n        </div>\r\n        <div class="col-lg-6">\r\n          <ul class="list-inline banner-social-buttons">\r\n            <li>\r\n              <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>\r\n            </li>\r\n            <li>\r\n              <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>\r\n            </li>\r\n            <li>\r\n              <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>\r\n            </li>\r\n          </ul>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <footer>\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <p class="copyright text-muted small">Copyright &copy; 2016. All Rights Reserved</p>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </footer>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "source_encoding": "utf-8", "filename": "C:/Users/Sean/Desktop/NuviProject/TweetPrediction/templates/index.html", "line_map": {"64": 61, "65": 77, "66": 77, "67": 91, "68": 91, "69": 94, "38": 1, "71": 99, "28": 0, "43": 150, "70": 94, "77": 71, "49": 3, "58": 3, "59": 36, "60": 36, "61": 39, "62": 39, "63": 61}}
__M_END_METADATA
"""
