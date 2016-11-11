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

            data = {
                "Inputs": {
                        "input1":
                        [
                            {
                                'loan_amnt': form.cleaned_data.get('loan_amount'),
                                'term': form.cleaned_data.get('term'),
                                'int_rate': form.cleaned_data.get('int_rate'),
                                'installment': form.cleaned_data.get('installment'),
                                'sub_grade': form.cleaned_data.get('sub_grade'),
                                'emp_length': form.cleaned_data.get('emp_length'),
                                'home_ownership': form.cleaned_data.get('home_ownership'),
                                'annual_inc': form.cleaned_data.get('annual_inc'),
                                'is_inc_v': form.cleaned_data.get('is_inc_v'),
                                'purpose': form.cleaned_data.get('purpose'),
                                'dti': form.cleaned_data.get('dti'),
                                'delinq_2yrs': form.cleaned_data.get('delinq_2yrs'),
                                'earliest_cr_line': form.cleaned_data.get('earliest_cr_line'),
                                'inq_last_6mths': form.cleaned_data.get('inq_last_6mths'),
                                'open_acc': form.cleaned_data.get('open_acc'),
                                'pub_rec': form.cleaned_data.get('pub_rec'),
                                'revol_bal': form.cleaned_data.get('revol_bal'),
                                'revol_util': form.cleaned_data.get('revol_util'),
                                'total_acc': form.cleaned_data.get('total_acc'),
                                'pub_rec_bankruptcies': form.cleaned_data.get('pub_rec_bankruptcies'),
                                'tax_liens': form.cleaned_data.get('tax_liens'),
                            }
                        ],
                },
                "GlobalParameters":  {
                }
            }

            body = str.encode(json.dumps(data))

            url = 'https://ussouthcentral.services.azureml.net/workspaces/84c08bbf7ef948f09c5e7b5074bd3614/services/6f7841236c584fcc8588d66755e9084a/execute?api-version=2.0&format=swagger'
            api_key = 'LjvmH+004SytJP+Af0GnkGiE82LbO58iMCk0jSl55uW2lzZEuqL6fH91aw/Nx09W7F1HIyYJaMgb/gngjTL7CQ=='
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
    tweet_text = forms.CharField(label='Tweet Text', required=True, widget=forms.TextInput(attrs={'placeholder': '...', 'class': 'form-control'}))

    def clean(self):
        return self.cleaned_data
