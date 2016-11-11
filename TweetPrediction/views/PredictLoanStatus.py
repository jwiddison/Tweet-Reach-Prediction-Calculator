import urllib.request
import json

data = {
    "Inputs": {
            "input1":
            [
                {
                    'loan_amnt': "1",
                    'term': "",
                    'int_rate': "1",
                    'installment': "1",
                    'sub_grade': "",
                    'emp_length': "",
                    'home_ownership': "",
                    'annual_inc': "1",
                    'is_inc_v': "",
                    'purpose': "",
                    'dti': "1",
                    'delinq_2yrs': "1",
                    'earliest_cr_line': "1",
                    'inq_last_6mths': "1",
                    'open_acc': "1",
                    'pub_rec': "1",
                    'revol_bal': "1",
                    'revol_util': "1",
                    'total_acc': "1",
                    'pub_rec_bankruptcies': "1",
                    'tax_liens': "1",
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
