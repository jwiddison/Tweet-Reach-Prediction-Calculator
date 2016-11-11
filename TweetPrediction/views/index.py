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

    # Tuples to fill in drop-down values

    TERM_CHOICES = ((' 36 Months', '36 Months'),(' 60 Months', '60 Months'))

    SUB_GRADES = (
        ('A1','A1'),('A2','A2'),('A3','A3'),('A4','A4'),('A5','A5'),
        ('B1','B1'),('B2','B2'),('B3','B3'),('B4','B4'),('B5','B5'),
        ('C1','C1'),('C2','C2'),('C3','C3'),('C4','C4'),('C5','C5'),
        ('D1','D1'),('D2','D2'),('D3','D3'),('D4','D4'),('D5','D5'),
        ('E1','E1'),('E2','E2'),('E3','E3'),('E4','E4'),('E5','E5'),
        ('F1','F1'),('F2','F2'),('F3','F3'),('F4','F4'),('F5','F5'),
        ('G1','G1'),('G2','G2'),('G3','G3'),('G4','G4'),('G5','G5'),
    )

    EMP_LENGTH = (
        ('n/a','n/a'),
        ('< 1 year','< 1 year'),
        ('1 year','1 year'),
        ('2 years','2 years'),
        ('3 years','3 years'),
        ('4 years','4 years'),
        ('5 years','5 years'),
        ('6 years','6 years'),
        ('7 years','7 years'),
        ('8 years','8 years'),
        ('9 years','9 years'),
        ('10+ years','10+ years'),
    )

    HOME_OWNERSHIP = (('RENT','RENT'),('MORTGAGE','MORTGAGE'),('OWN','OWN'))

    INCOME_VERIFIED = (('Not Verified','NOT VERIFIED'),('Verified','VERIFIED'),('Source Verified','SOURCE VERIFIED'))

    PURPOSE = (
        ('car','CAR'),
        ('credit_card', 'CREDIT CARD'),
        ('debt_consolidation', 'DEBT CONSOLIDATION'),
        ('home_improvement', 'HOME IMPROVEMENT'),
        ('house', 'HOUSE'),
        ('major_purchase', 'MAJOR PURCHASE'),
        ('medical', 'MEDICAL'),
        ('moving', 'MOVING'),
        ('other','OTHER'),
        ('renewable_energy','RENEWABLE ENERGY'),
        ('small_business','SMALL BUSINESS'),
        ('vacation','VACATION'),
        ('wedding','WEDDING'),
    )

    # Form Fields

    loan_amount = forms.CharField(label='Proposed Loan Amount', required=True, widget=forms.TextInput(attrs={'placeholder': '$10,000', 'class': 'form-control'}))
    term = forms.ChoiceField(label='Term', required=True, choices=TERM_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    int_rate = forms.CharField(label="Interest Rate", required=True, widget=forms.TextInput(attrs={'placeholder': '12.5%', 'class': 'form-control'}))
    installment = forms.CharField(label="Monthly Installment", required=True, widget=forms.TextInput(attrs={'placeholder': '$1,500.00', 'class': 'form-control'}))
    sub_grade = forms.ChoiceField(label="Sub Grade", required=True, choices=SUB_GRADES, widget=forms.Select(attrs={'class': 'form-control'}))
    emp_length = forms.ChoiceField(label="Employment Length", required=True, choices=EMP_LENGTH, widget=forms.Select(attrs={'class': 'form-control'}))
    home_ownership = forms.ChoiceField(label="Home Ownership Status", required=True, choices=HOME_OWNERSHIP, widget=forms.Select(attrs={'class': 'form-control'}))
    annual_inc = forms.CharField(label="Annual Income", required=True, widget=forms.TextInput(attrs={'placeholder': '$45,000.00', 'class': 'form-control'}))
    is_inc_v = forms.ChoiceField(label="Is Income Verified?", required=True, choices=INCOME_VERIFIED, widget=forms.Select(attrs={'class': 'form-control'}))
    purpose = forms.ChoiceField(label="Loan Purpose", required=True, choices=PURPOSE, widget=forms.Select(attrs={'class': 'form-control'}))
    dti = forms.CharField(label="DTI", required=True, widget=forms.TextInput(attrs={'placeholder': '1.0', 'class': 'form-control'}))
    delinq_2yrs = forms.CharField(label="Delinquencies in Last 2 Years", required=True, widget=forms.TextInput(attrs={'placeholder': '1', 'class': 'form-control'}))
    earliest_cr_line = forms.CharField(label="Date of Earliest Credit Line", required=True, widget=forms.TextInput(attrs={'placeholder': '01/01/1990', 'class': 'form-control'}))
    inq_last_6mths = forms.CharField(label="Credit Inquiries in Last 6 Months", required=True, widget=forms.TextInput(attrs={'placeholder': '0', 'class': 'form-control'}))
    open_acc = forms.CharField(label="Number of Open Credit Accounts", required=True, widget=forms.TextInput(attrs={'placeholder': '1', 'class': 'form-control'}))
    total_acc = forms.CharField(label="Total Credit Lines", required=True, widget=forms.TextInput(attrs={'placeholder': '1', 'class': 'form-control'}))
    pub_rec = forms.CharField(label="Number of Derogatory Public Records", required=True, widget=forms.TextInput(attrs={'placeholder': '0', 'class': 'form-control'}))
    revol_bal = forms.CharField(label="Total Credit Revolving Balance", required=True, widget=forms.TextInput(attrs={'placeholder': '$10,000', 'class': 'form-control'}))
    revol_util = forms.CharField(label="Revolving Line Utilization Rate", required=True, widget=forms.TextInput(attrs={'placeholder': '$1,000.00', 'class': 'form-control'}))
    pub_rec_bankruptcies = forms.CharField(label="Number of Recorded Bankruptcies", required=True, widget=forms.TextInput(attrs={'placeholder': '0', 'class': 'form-control'}))
    tax_liens = forms.CharField(label="Number of Tax Liens", required=True, widget=forms.TextInput(attrs={'placeholder': '0', 'class': 'form-control'}))

    def clean(self):
        return self.cleaned_data
