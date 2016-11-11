# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1478890640.966807
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        form = context.get('form', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <nav class="navbar navbar-default navbar-fixed-top topnav" role="navigation">\n    <div class="container topnav">\n      <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target="#bs-example-navbar-collapse-1">\n          <span class="sr-only">Toggle navigation</span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand topnav" href="#">Nuvi Project</a>\n      </div>\n      <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">\n        <ul class="nav navbar-nav navbar-right">\n          <li><a href="#about">About</a></li>\n          <li><a href="#services">Services</a></li>\n          <li><a href="#contact">Contact</a></li>\n        </ul>\n      </div>\n    </div>\n  </nav>\n\n  <a name="about"></a>\n  <div class="intro-header">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-12">\n          <div class="intro-message">\n            <h1>Landing Page</h1>\n            <h3>A Template by Start Bootstrap</h3>\n            <hr class="intro-divider">\n            <ul class="list-inline intro-social-buttons">\n              <li>\n                <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>\n              </li>\n              <li>\n                <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>\n              </li>\n              <li>\n                <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>\n              </li>\n            </ul>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <a  name="services"></a>\n  <div class="content-section-a">\n    <div class="container">\n        <div class="row">\n          <div class="col-lg-5 col-sm-6">\n            <hr class="section-heading-spacer">\n            <div class="clearfix"></div>\n            <form method="POST">\n              ')
        __M_writer(str(form.as_table()))
        __M_writer('\n            </form>\n            <h2 class="section-heading">Death to the Stock Photo:<br>Special Thanks</h2>\n            <p class="lead">A special thanks to <a target="_blank" href="http://join.deathtothestockphoto.com/">Death to the Stock Photo</a> for providing the photographs that you see in this template. Visit their website to become a member.</p>\n          </div>\n          <div class="col-lg-5 col-lg-offset-2 col-sm-6">\n            <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/ipad.png" alt="">\n          </div>\n      </div>\n    </div>\n  </div>\n\n  <div class="content-section-b">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-5 col-lg-offset-1 col-sm-push-6  col-sm-6">\n          <hr class="section-heading-spacer" />\n          <div class="clearfix"></div>\n          <h2 class="section-heading">3D Device Mockups<br>by PSDCovers</h2>\n          <p class="lead">Turn your 2D designs into high quality, 3D product shots in seconds using free Photoshop actions by <a target="_blank" href="http://www.psdcovers.com/">PSDCovers</a>! Visit their website to download some of their awesome, free photoshop actions!</p>\n        </div>\n        <div class="col-lg-5 col-sm-pull-6  col-sm-6">\n          <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/dog.png" alt="">\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <div class="content-section-a">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-5 col-sm-6">\n          <hr class="section-heading-spacer">\n          <div class="clearfix"></div>\n          <h2 class="section-heading">Google Web Fonts and<br>Font Awesome Icons</h2>\n          <p class="lead">This template features the \'Lato\' font, part of the <a target="_blank" href="http://www.google.com/fonts">Google Web Font library</a>, as well as <a target="_blank" href="http://fontawesome.io">icons from Font Awesome</a>.</p>\n        </div>\n        <div class="col-lg-5 col-lg-offset-2 col-sm-6">\n          <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/phones.png" alt="">\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <a  name="contact"></a>\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-6">\n          <h2>Connect to Start Bootstrap:</h2>\n        </div>\n        <div class="col-lg-6">\n          <ul class="list-inline banner-social-buttons">\n            <li>\n              <a href="https://twitter.com/SBootstrap" class="btn btn-default btn-lg"><i class="fa fa-twitter fa-fw"></i> <span class="network-name">Twitter</span></a>\n            </li>\n            <li>\n              <a href="https://github.com/IronSummitMedia/startbootstrap" class="btn btn-default btn-lg"><i class="fa fa-github fa-fw"></i> <span class="network-name">Github</span></a>\n            </li>\n            <li>\n              <a href="#" class="btn btn-default btn-lg"><i class="fa fa-linkedin fa-fw"></i> <span class="network-name">Linkedin</span></a>\n            </li>\n          </ul>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <footer>\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-12">\n          <ul class="list-inline">\n            <li>\n                <a href="#">Home</a>\n            </li>\n            <li class="footer-menu-divider">&sdot;</li>\n            <li>\n              <a href="#about">About</a>\n            </li>\n            <li class="footer-menu-divider">&sdot;</li>\n            <li>\n              <a href="#services">Services</a>\n            </li>\n            <li class="footer-menu-divider">&sdot;</li>\n            <li>\n              <a href="#contact">Contact</a>\n            </li>\n          </ul>\n          <p class="copyright text-muted small">Copyright &copy; Your Company 2014. All Rights Reserved</p>\n        </div>\n      </div>\n    </div>\n  </footer>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "index.html", "source_encoding": "utf-8", "filename": "/Users/Jordan/Documents/BYU/0 - MISM - 1/Fall 2016/IS 415/NuviProject/TweetPrediction/templates/index.html", "line_map": {"64": 97, "37": 1, "70": 64, "60": 65, "42": 154, "48": 3, "56": 3, "57": 59, "58": 59, "59": 65, "28": 0, "61": 81, "62": 81, "63": 97}}
__M_END_METADATA
"""
