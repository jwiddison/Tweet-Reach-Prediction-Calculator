# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1481330389.897778
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
        result = context.get('result', UNDEFINED)
        reccomendation = context.get('reccomendation', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
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
        result = context.get('result', UNDEFINED)
        reccomendation = context.get('reccomendation', UNDEFINED)
        def content():
            return render_content(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <nav class="navbar navbar-default navbar-fixed-top" role="navigation">\n    <div class="container">\n      <div class="navbar-header">\n        <button type="button" class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">\n          <span class="sr-only">Toggle navigation</span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n          <span class="icon-bar"></span>\n        </button>\n        <a class="navbar-brand"><img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/nuvi.jpg" class="img-responsive" id="navbar_image"/></a>\n      </div>\n      <div class="collapse navbar-collapse navbar-ex1-collapse">\n        <ul class="nav navbar-nav navbar-right">\n          <li><a href="#prediction">Prediction</a></li>\n          <li><a href="#about">About</a></li>\n          <li><a href="#dashboard">Dashboard</a></li>\n        </ul>\n      </div>\n    </div>\n  </nav>\n\n  <a name="prediction" class="page-scroll"></a>\n  <div class="intro-header">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <div class="intro-message">\n            <img src="')
        __M_writer(str(STATIC_URL))
        __M_writer('TweetPrediction/media/pics/twitter.svg" class="img-responsive center-block" style="margin-top:20px;"/>\n            <hr class="intro-divider">\n            <div class="row">\n              <div class="col-md-6 col-md-offset-3">\n                <form method="POST">\n                  ')
        __M_writer(str(form.as_p()))
        __M_writer('\n                  <input type="submit" class="btn btn-primary center-block" value="Predict Reach"/>\n                </form>\n                <p class="result">')
        __M_writer(str(result))
        __M_writer('</p>\n                <p class="result">')
        __M_writer(str(reccomendation))
        __M_writer('</p>\n              </div>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <a name="about" class="page-scroll"></a>\n  <div class="content-section-a">\n    <div class="container">\n        <div class="row">\n          <div class="col-lg-5 col-sm-6">\n            <hr class="section-heading-spacer">\n            <div class="clearfix"></div>\n            <h2 class="section-heading">Retweets Matter</h2>\n            <p class="lead">Your social media presence matters.  Use our free prediction calculator to predict the reach of your tweets.</p>\n          </div>\n          <div class="col-lg-5 col-lg-offset-2 col-sm-6">\n            <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/tablet_twitter.jpeg" alt="">\n          </div>\n      </div>\n    </div>\n  </div>\n\n  <div class="content-section-b">\n    <div class="container">\n      <div class="row">\n        <div class="col-lg-5 col-lg-offset-1 col-sm-push-6  col-sm-6">\n          <hr class="section-heading-spacer" />\n          <div class="clearfix"></div>\n          <h2 class="section-heading">Predictive Analytics</h2>\n          <p class="lead">We use advanced machine learning technology that digests real-time data in order to determine the best possible prediction of retweet reach.</p>\n        </div>\n        <div class="col-lg-5 col-sm-pull-6  col-sm-6">\n          <img class="img-responsive" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('TweetPrediction/media/pics/graph.jpeg" alt="">\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <a name="dashboard" class="page-scroll"></a>\n  <div class="content-section-a">\n    <div class="container">\n      <div class="row">\n        <div class="col-md-12">\n          <hr class="section-heading-spacer" />\n          <div class="clearfix"></div>\n          <h2 class="section-heading">Tweet Analytics</h2>\n          <div style="text-align: center">\n            <div style="display: inline-block;">\n              <div class=\'tableauPlaceholder\' id=\'viz1481315714488\' style=\'position: relative\'><noscript><a href=\'#\'><img alt=\'Retweet Stats \' src=\'https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;RK&#47;RKPN7QBYM&#47;1_rss.png\' style=\'border: none\' /></a></noscript><object class=\'tableauViz\'  style=\'display:none;\'><param name=\'host_url\' value=\'https%3A%2F%2Fpublic.tableau.com%2F\' /> <param name=\'path\' value=\'shared&#47;RKPN7QBYM\' /> <param name=\'toolbar\' value=\'yes\' /><param name=\'static_image\' value=\'https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;RK&#47;RKPN7QBYM&#47;1.png\' /> <param name=\'animate_transition\' value=\'yes\' /><param name=\'display_static_image\' value=\'yes\' /><param name=\'display_spinner\' value=\'yes\' /><param name=\'display_overlay\' value=\'yes\' /><param name=\'display_count\' value=\'yes\' /></object></div>                <script type=\'text/javascript\'>                    var divElement = document.getElementById(\'viz1481315714488\');                    var vizElement = divElement.getElementsByTagName(\'object\')[0];                    vizElement.style.width=\'1004px\';vizElement.style.height=\'869px\';                    var scriptElement = document.createElement(\'script\');                    scriptElement.src = \'https://public.tableau.com/javascripts/api/viz_v1.js\';                    vizElement.parentNode.insertBefore(scriptElement, vizElement);                </script>\n            </div>\n          </div>\n        </div>\n      </div>\n    </div>\n  </div>\n\n  <div class="banner">\n    <div class="container">\n      <div class="row">\n        <p class="copyright text-muted small white">Copyright &copy; 2016. All Rights Reserved</p>\n      </div>\n    </div>\n  </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"64": 31, "65": 36, "66": 36, "67": 39, "68": 39, "69": 40, "70": 40, "39": 1, "72": 60, "60": 3, "74": 76, "71": 60, "44": 108, "80": 74, "50": 3, "73": 76, "28": 0, "61": 13, "62": 13, "63": 31}, "filename": "/Users/Jordan/Documents/BYU/0 - MISM - 1/Fall 2016/IS 415/NuviProject/TweetPrediction/templates/index.html", "uri": "index.html"}
__M_END_METADATA
"""
