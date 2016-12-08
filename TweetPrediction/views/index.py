import json
import os
from NuviProject.settings import BASE_DIR
import urllib.request
from .. import dmp_render_to_string, dmp_render
from django import forms
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django_mako_plus import view_function

@view_function
def process_request(request):

    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.path.join(BASE_DIR, 'google.json')

    form = PredictionForm()
    entities = 'The entities will display here'
    sentiment = 'The sentiment will display here'
    result = 'The result will display here'
    if request.method == 'POST':
        form = PredictionForm(request.POST)
        if form.is_valid():

            data = {
                "document":{
                    "type":"PLAIN_TEXT",
                    "content": form.cleaned_data.get('tweet_text'),
                },
                "encodingType":"UTF8"
            }

            body = str.encode(json.dumps(data))

            url = 'https://language.googleapis.com/v1/documents:analyzeEntities'
            api_key = 'ya29.El-uA_XL_trOwfwPTOa-npqNANiBJG7U86K71Iv4BYnxQN12Kn6bF2zld_vhrf1EUW-S_zvjALaTVWCpeKw1fAyaOVuRxjNGe8JH5-T4iceU09ADkoUC_ZUixBwDUPfPxg'
            headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

            try:
                req = urllib.request.Request(url, body, headers)
            except:
                print("Google Authentication Failed")

            entities = hitGoogleAPI(req)
            types = []
            for ent in entities['entities']:
                types.append(ent['type'])

            unknown = types.count('UNKNOWN')
            person = types.count('PERSON')
            location = types.count('LOCATION')
            organization = types.count('ORGANIZATION')
            event = types.count('EVENT')
            art = types.count('WORK_OF_ART')
            consumer_good = types.count('CONSUMER_GOOD')
            other = types.count('OTHER')

            total = unknown + person + location + organization + event+ art + consumer_good + other

            unknown_a = unknown / total
            person_a = person / total
            location_a = location / total
            organization_a = organization / total
            event_a = event / total
            art_a = art / total
            consumer_good_a = consumer_good / total
            other_a = other / total

            language = entities['language']

            print(types)

            url = 'https://language.googleapis.com/v1/documents:analyzeSentiment'
            req2 = urllib.request.Request(url, body, headers)

            sentiment = hitGoogleAPI(req2)
            sentiment = sentiment['documentSentiment']
            magnitude = sentiment['magnitude']
            polarity = sentiment['score']

            #now hit the Microsoft API
            data = {
                "Inputs": {
                    "input1":
                        [
                            {
                                'Lang': language,
                                'IsReshare': form.cleaned_data.get('is_reshare'),
                                'RetweetCount': "1",
                                'Network': "Twitter",
                                'Country': "United States",
                                'State': "Utah",
                                'City': "Provo",
                                'Gender': "Male",
                                'weekday': "Monday",
                                'hour': "1",
                                'day': "1",
                                'polarity': polarity,
                                'magnitude': magnitude,
                                'UNKNOWN_AVG': unknown_a,
                                'PERSON_AVG': person_a,
                                'LOCATION_AVG': location_a,
                                'ORGANIZATION_AVG': organization_a,
                                'EVENT_AVG': event_a,
                                'WORK_OF_ART_AVG': art_a,
                                'CONSUMER_GOOD_AVG': consumer_good_a,
                                'OTHER_AVG': other_a,
                            }
                        ],
                    },
                "GlobalParameters":  {
                }
            }


            body = str.encode(json.dumps(data))

            url = 'https://ussouthcentral.services.azureml.net/workspaces/4bb4313c768a46d6ba271a0fba4d5fcd/services/db557902b3c74f96a5fe3b009cb1eaf2/execute?api-version=2.0&format=swagger'
            api_key = 'HQbjX/Pe7z+qMyv8VtY4xLiw8+muIR9hHIqnjfRoYxIZolCGnD0cvWDS8YpUj2b2NS9laQYDSNs5o9HHECgZeA=='
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
        'entities': entities,
        'sentiment': sentiment,
        'result' : result,
    }
    return dmp_render(request, 'index.html', template_vars)


class PredictionForm(forms.Form):
    tweet_text = forms.CharField(label='',required=True, widget=forms.TextInput(attrs={'placeholder': 'Tweet Text', 'class': 'form-control'}))
    is_reshare = forms.BooleanField(label = 'Are you retweeting this?', required=True, widget=forms.CheckboxInput())

    def clean(self):
        return self.cleaned_data

def hitGoogleAPI(req):
    try:
        response = urllib.request.urlopen(req)
        string = response.read().decode('utf-8')
        result = json.loads(string)
        return result
    except urllib.error.HTTPError as error:
        print("The request failed with status code: " + str(error.code))
        # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
        print(error.info())
        print(json.loads(error.read().decode("utf8", 'ignore')))
        return error.info()



## NOTES:

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
            # TimeMs  HourMs  DayMs   AggregatedMs    Lang    IsReshare   Reach   Stats   TopicReach  TopicSpread RetweetCount    Likes   Klout   Sentiment   Network SourceName  Lat Long    Country State   StateCode   City    UserId  Gender  text

            # is_reshare = forms.cleaned_data.get('is_reshare')
