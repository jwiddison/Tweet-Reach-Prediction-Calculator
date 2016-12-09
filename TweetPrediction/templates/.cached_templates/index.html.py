# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
<<<<<<< HEAD
_modified_time = 1481259022.8920884
=======
<<<<<<< HEAD
_modified_time = 1481259167.972847
=======
_modified_time = 1481258242.8808331
>>>>>>> 83589d846faa01f61173d1efcdc7af130826f225
>>>>>>> 2816a6b029273c71996b4f955a41db508e93fb14
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
<<<<<<< HEAD
        result = context.get('result', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
=======
<<<<<<< HEAD
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        entities = context.get('entities', UNDEFINED)
        form = context.get('form', UNDEFINED)
=======
>>>>>>> 83589d846faa01f61173d1efcdc7af130826f225
        sentiment = context.get('sentiment', UNDEFINED)
        result = context.get('result', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
<<<<<<< HEAD
=======
        form = context.get('form', UNDEFINED)
        result = context.get('result', UNDEFINED)
>>>>>>> 2816a6b029273c71996b4f955a41db508e93fb14
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        entities = context.get('entities', UNDEFINED)
<<<<<<< HEAD
        sentiment = context.get('sentiment', UNDEFINED)
=======
>>>>>>> 83589d846faa01f61173d1efcdc7af130826f225
>>>>>>> 2816a6b029273c71996b4f955a41db508e93fb14
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
<<<<<<< HEAD
        result = context.get('result', UNDEFINED)
        def content():
            return render_content(context)
=======
<<<<<<< HEAD
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        entities = context.get('entities', UNDEFINED)
        form = context.get('form', UNDEFINED)
=======
>>>>>>> 83589d846faa01f61173d1efcdc7af130826f225
        sentiment = context.get('sentiment', UNDEFINED)
        result = context.get('result', UNDEFINED)
        def content():
            return render_content(context)
<<<<<<< HEAD
        __M_writer = context.writer()
        __M_writer('\n  <nav class="navbar navbar-default navbar-fixed-top" role="navigation">\n    <div class="container">\n      <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n          <span class="sr-only">Toggle navigation</span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand"><img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/nuvi.jpg" class="img-responsive" id="navbar_image"/></a>\n      </div>\n      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n        <ul class="nav navbar-nav navbar-right">\n          <li><a href="#prediction" class="white">Prediction</a></li>\n          <li><a href="#about" class="white">About</a></li>\n          <li><a href="#dashboard" class="white">Dashboard</a></li>\n        </ul>\n      </div>\n    </div>\n  </nav>\n\n  <a name="prediction" class="page-scroll"></a>\n  <div class="intro-header">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <div class="intro-message">\n            <img src="')
=======
        form = context.get('form', UNDEFINED)
        result = context.get('result', UNDEFINED)
>>>>>>> 2816a6b029273c71996b4f955a41db508e93fb14
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        entities = context.get('entities', UNDEFINED)
        sentiment = context.get('sentiment', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n  <nav class="navbar navbar-default navbar-fixed-top topnav" role="navigation">\r\n    <div class="container topnav">\r\n      <div class="navbar-header">\r\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\r\n          <span class="sr-only">Toggle navigation</span>\r\n          <span class="icon-bar"></span>\r\n          <span class="icon-bar"></span>\r\n          <span class="icon-bar"></span>\r\n        </button>\r\n        <a class="navbar-brand topnav" href="#"><img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/nuvi.jpg" class="img-responsive" id="navbar_image"/></a>\r\n      </div>\r\n      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\r\n        <ul class="nav navbar-nav navbar-right">\r\n          <li><a href="#about">About</a></li>\r\n          <li><a href="#prediction">Prediction</a></li>\r\n          <li><a href="#dashboard">Dashboard</a></li>\r\n        </ul>\r\n      </div>\r\n    </div>\r\n  </nav>\r\n\r\n  <div class="intro-header">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <div class="intro-message">\r\n            <img src="')
>>>>>>> 83589d846faa01f61173d1efcdc7af130826f225
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/nuvi.jpg" class="img-responsive center-block"/>\r\n')
        __M_writer('            <hr class="intro-divider">\r\n            <div class="row">\r\n              <div class="col-md-6 col-md-offset-3">\r\n                <form method="POST">\r\n                  ')
        __M_writer(str(form.as_p()))
        __M_writer('\r\n                  <input type="submit" class="btn btn-primary center-block" value="Predict Reach"/>\r\n                </form>\r\n                <p>')
        __M_writer(str(result))
        __M_writer('</p>\r\n                <p>')
        __M_writer(str(entities))
        __M_writer('</p>\r\n                <p>')
        __M_writer(str(sentiment))
<<<<<<< HEAD
        __M_writer('</p>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n\n\n\n  <a name="about" class="page-scroll"></a>\n  <div class="content-section-a">\n    <div class="container">\n        <div class="row">\n          <div class="col-lg-5 col-sm-6">\n            <hr class="section-heading-spacer">\n            <div class="clearfix"></div>\n            <h2 class="section-heading">Twitter</h2>\n            <p class="lead">Something about why twitter matters</p>\n          </div>\n          <div class="col-lg-5 col-lg-offset-2 col-sm-6">\n            <img class="img-responsive img-thumbnail" src="')
=======
        __M_writer('</p>\r\n              </div>\r\n            </div>\r\n          </div>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n\r\n\r\n  <a name="about"></a>\r\n  <div class="content-section-a">\r\n    <div class="container">\r\n        <div class="row">\r\n          <div class="col-lg-5 col-sm-6">\r\n            <hr class="section-heading-spacer">\r\n            <div class="clearfix"></div>\r\n            <h2 class="section-heading">Twitter</h2>\r\n            <p class="lead">Something about why twitter matters</p>\r\n          </div>\r\n          <div class="col-lg-5 col-lg-offset-2 col-sm-6">\r\n            <img class="img-responsive img-thumbnail" src="')
>>>>>>> 83589d846faa01f61173d1efcdc7af130826f225
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/tablet_twitter.jpeg" alt="">\r\n          </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <div class="content-section-b">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-lg-5 col-lg-offset-1 col-sm-push-6  col-sm-6">\r\n          <hr class="section-heading-spacer" />\r\n          <div class="clearfix"></div>\r\n          <h2 class="section-heading">Predicting Reach</h2>\r\n          <p class="lead">Another graph or something probably.  Maybe something about people posting about their pets on social media.</p>\r\n        </div>\r\n        <div class="col-lg-5 col-sm-pull-6  col-sm-6">\r\n          <img class="img-responsive img-thumbnail" src="')
        __M_writer(str( STATIC_URL ))
<<<<<<< HEAD
        __M_writer('TweetPrediction/media/pics/graph.jpeg" alt="">\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <div class="content-section-a">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-6 col-md-offset-3">\n          <hr class="section-heading-spacer">\n          <div class="clearfix"></div>\n')
        __M_writer('        </div>\n')
        __M_writer('      </div>\n    </div>\n  </div>\n\n  <a name="dashboard" class="page-scroll"></a>\n  <div class="content-section-b">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <hr class="section-heading-spacer" />\n          <div class="clearfix"></div>\n          <h2 class="section-heading">Dashboard</h2>\n          <p>Gonna put the tableau dashboard in here maybe.</p>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-6">\n          <h2>Social Media Buttons \'Cause Millenials:</h2>\n        </div>\n        <div class="col-lg-6">\n          <ul class="list-inline banner-social-buttons">\n            <li>\n              <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>\n            </li>\n            <li>\n              <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>\n            </li>\n            <li>\n              <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>\n            </li>\n          </ul>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <footer>\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <p class="copyright text-muted small">Copyright &copy; 2016. All Rights Reserved</p>\n        </div>\n      </div>\n    </div>\n  </footer>\n\n')
=======
        __M_writer('TweetPrediction/media/pics/graph.jpeg" alt="">\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <a  name="prediction"></a>\r\n  <div class="content-section-a">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-6 col-md-offset-3">\r\n          <hr class="section-heading-spacer">\r\n          <div class="clearfix"></div>\r\n')
        __M_writer('        </div>\r\n')
        __M_writer('      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <a  name="dashboard"></a>\r\n  <div class="content-section-b">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <hr class="section-heading-spacer" />\r\n          <div class="clearfix"></div>\r\n          <h2 class="section-heading">Dashboard</h2>\r\n          <p>Gonna put the tableau dashboard in here maybe.</p>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <div class="banner">\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-lg-6">\r\n          <h2>Social Media Buttons \'Cause Millenials:</h2>\r\n        </div>\r\n        <div class="col-lg-6">\r\n          <ul class="list-inline banner-social-buttons">\r\n            <li>\r\n              <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>\r\n            </li>\r\n            <li>\r\n              <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>\r\n            </li>\r\n            <li>\r\n              <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>\r\n            </li>\r\n          </ul>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </div>\r\n\r\n  <footer>\r\n    <div class="container">\r\n      <div class="row">\r\n        <div class="col-md-12">\r\n          <p class="copyright text-muted small">Copyright &copy; 2016. All Rights Reserved</p>\r\n        </div>\r\n      </div>\r\n    </div>\r\n  </footer>\r\n\r\n')
>>>>>>> 83589d846faa01f61173d1efcdc7af130826f225
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
<<<<<<< HEAD
{"uri": "index.html", "source_encoding": "utf-8", "filename": "C:/Users/Sean/Desktop/NuviProject/TweetPrediction/templates/index.html", "line_map": {"64": 13, "65": 30, "66": 30, "67": 32, "68": 36, "69": 36, "70": 39, "71": 39, "72": 40, "73": 40, "74": 41, "75": 41, "76": 63, "77": 63, "78": 79, "79": 79, "80": 97, "81": 101, "87": 81, "28": 0, "40": 1, "45": 152, "51": 3, "62": 3, "63": 13}}
=======
<<<<<<< HEAD
{"line_map": {"64": 13, "65": 31, "66": 31, "67": 33, "68": 37, "69": 37, "70": 40, "71": 40, "72": 41, "73": 41, "74": 42, "75": 42, "76": 64, "77": 64, "78": 80, "79": 80, "80": 97, "81": 101, "87": 81, "28": 0, "40": 1, "45": 152, "51": 3, "62": 3, "63": 13}, "uri": "index.html", "filename": "/Users/Jordan/Documents/BYU/0 - MISM - 1/Fall 2016/IS 415/NuviProject/TweetPrediction/templates/index.html", "source_encoding": "utf-8"}
=======
{"uri": "index.html", "line_map": {"64": 13, "65": 30, "66": 30, "67": 32, "68": 36, "69": 36, "70": 39, "71": 39, "72": 40, "73": 40, "74": 41, "75": 41, "76": 63, "77": 63, "78": 79, "79": 79, "80": 97, "81": 101, "87": 81, "28": 0, "40": 1, "45": 152, "51": 3, "62": 3, "63": 13}, "filename": "C:/Users/Sean/Desktop/NuviProject/TweetPrediction/templates/index.html", "source_encoding": "utf-8"}
>>>>>>> 83589d846faa01f61173d1efcdc7af130826f225
>>>>>>> 2816a6b029273c71996b4f955a41db508e93fb14
__M_END_METADATA
"""
