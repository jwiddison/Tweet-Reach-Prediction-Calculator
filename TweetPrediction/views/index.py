import json
import urllib.request
from .. import dmp_render_to_string, dmp_render
from django import forms
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function

@view_function
def process_request(request):
    form = PredictionForm()
    result = 'The results will display here'
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():

            # data = {
            #     "Inputs": {
            #             "input1":
            #             [
            #                 {
            #                     'tweet_text': form.cleaned_data.get('tweet_text'),
            #                 }
            #             ],
            #     },
            #     "GlobalParameters":  {
            #     }
            # }

            data = {
                "document":{
                    "type":"PLAIN_TEXT",
                    "content": form.cleaned_data.get('tweet_text'),
                },
                "encodingType":"UTF8"
            }

            body = str.encode(json.dumps(data))

            url = 'https://language.googleapis.com/v1/documents:analyzeEntities'
            api_key = 'ya29.El-oA3PRKJ_KCwXKdbE9-yNa1sUzWcAAEF_k8AKk_Ds_qBwZmyPuPUL-eHMFwd9Um9-ga6Rf2rzzbUxT9ChGlkF8FYzyS0kxnkIq_DjeKyWkxtaPKK3dpkriDcZ9hcjYIw'
            headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

            req = urllib.request.Request(url, body, headers)

            try:
                response = urllib.request.urlopen(req)
                result = response.read()
                print(result)
            except urllib.error.HTTPError as error:
                print("The request failed with status code: " + str(error.code))
                # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
                print(error.info())
                print(json.loads(error.read().decode("utf8", 'ignore')))


    template_vars = {
        'form': form,
        'result': result,
    }
    return dmp_render(request, 'index.html', template_vars)


class PredictionForm(forms.Form):
    tweet_text = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder': 'Tweet Text', 'class': 'form-control'}))

    def clean(self):
        return self.cleaned_data
