# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481299539.9462857
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
        def content():
            return render_content(context._locals(__M_locals))
        sentiment = context.get('sentiment', UNDEFINED)
        entities = context.get('entities', UNDEFINED)
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        result = context.get('result', UNDEFINED)
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
        def content():
            return render_content(context)
        sentiment = context.get('sentiment', UNDEFINED)
        entities = context.get('entities', UNDEFINED)
        form = context.get('form', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        result = context.get('result', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <nav class="navbar navbar-default navbar-fixed-top" role="navigation">\r\n    <div class="container">\r\n      <div class="navbar-header">\r\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\r\n          <span class="sr-only">Toggle navigation</span>\r\n          <span class="icon-bar"></span>\r\n          <span class="icon-bar"></span>\r\n          <span class="icon-bar"></span>\r\n        </button>\r\n        <a class="navbar-brand"><img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/nuvi.jpg" class="img-responsive" id="navbar_image"/></a>\r\n      </div>\r\n      <div class="collapse navbar-collapse navbar-ex1-collapse">\r\n        <ul class="nav navbar-nav navbar-right">\r\n          <li><a href="#prediction">Prediction</a></li>\r\n          <li><a href="#about">About</a></li>\r\n          <li><a href="#dashboard">Dashboard</a></li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n  </nav>\r\n\r\n  <a name="prediction" class="page-scroll"></a>\r\n  <div class="intro-header">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <div class="intro-message">\r\n            <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/nuvi.jpg" class="img-responsive center-block"/>\r\n            <hr class="intro-divider">\r\n            <div class="row">\r\n              <div class="col-md-6 col-md-offset-3">\r\n                <form method="POST">\r\n                  ')
        __M_writer(str(form.as_p()))
        __M_writer('\r\n                  <input type="submit" class="btn btn-primary center-block" value="Predict Reach"/>\r\n                </form>\r\n                <p>')
        __M_writer(str(result))
        __M_writer('</p>\r\n                <p>')
        __M_writer(str(entities))
        __M_writer('</p>\r\n                <p>')
        __M_writer(str(sentiment))
        __M_writer('</p>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <a name="about" class="page-scroll"></a>\r\n  <div class="content-section-a">\r\n    <div class="container">\r\n        <div class="row">\r\n          <div class="col-lg-5 col-sm-6">\r\n            <hr class="section-heading-spacer">\r\n            <div class="clearfix"></div>\r\n            <h2 class="section-heading">Reach Matters</h2>\r\n            <p class="lead">Your social media presence matters.  Use our free prediction calculator to predict the reach of your business\'s tweets.</p>\r\n          </div>\r\n          <div class="col-lg-5 col-lg-offset-2 col-sm-6">\r\n            <img class="img-responsive img-thumbnail" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/tablet_twitter.jpeg" alt="">\r\n          </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <div class="content-section-b">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-lg-5 col-lg-offset-1 col-sm-push-6  col-sm-6">\r\n          <hr class="section-heading-spacer" />\r\n          <div class="clearfix"></div>\r\n          <h2 class="section-heading">Predictive Analytics</h2>\r\n          <p class="lead">Somebody needs to help me write something intelligent about the technology that we\'re using here.</p>\r\n        </div>\r\n        <div class="col-lg-5 col-sm-pull-6  col-sm-6">\r\n          <img class="img-responsive img-thumbnail" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/graph.jpeg" alt="">\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <a name="dashboard" class="page-scroll"></a>\r\n  <div class="content-section-a">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <hr class="section-heading-spacer" />\r\n          <div class="clearfix"></div>\r\n          <h2 class="section-heading">Dashboard</h2>\r\n          <p class="lead">Here\'s where you\'re gonna put your dashboard Michael.</p>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <div class="banner">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-lg-6">\r\n          <h2>Social Media</h2>\r\n          <p>We can take this out later if we want.</p>\r\n        </div>\r\n        <div class="col-lg-6">\r\n          <ul class="list-inline banner-social-buttons">\r\n            <li>\r\n              <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>\r\n            </li>\r\n            <li>\r\n              <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>\r\n            </li>\r\n            <li>\r\n              <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>\r\n            </li>\r\n          </ul>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <footer>\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <p class="copyright text-muted small">Copyright &copy; 2016. All Rights Reserved</p>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </footer>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:/Users/Sean/Desktop/NuviProject/TweetPrediction/templates/index.html", "uri": "index.html", "source_encoding": "utf-8", "line_map": {"64": 13, "65": 31, "66": 31, "67": 36, "68": 36, "69": 39, "70": 39, "71": 40, "72": 40, "73": 41, "74": 41, "75": 61, "76": 61, "77": 77, "78": 77, "84": 78, "28": 0, "40": 1, "45": 131, "51": 3, "62": 3, "63": 13}}
__M_END_METADATA
"""
