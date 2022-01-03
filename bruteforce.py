import itertools
import requests


def foo(chars, len):
    yield from itertools.product(*([chars] * len))


def check_string_double(string):
    count = 0
    temp = []
    for i in string:
        if i not in temp:
            count += 1
            temp.append(i)
    return count


COUNTER = 0

LEN = 2  # Length of the bruteforced domain
APIKEY = 'replace_this_with_your_api-key'  # Enter your own api key here

for x in foo('abcdefghijklmnopqrstuvwxyz1234567890', LEN):
    name = f"{''.join(x)}"

    if check_string_double(name) <= 2:  # Max different chars in the domain
        domainname = f"{name}.de"

        COUNTER += 1

        url = "https://domaination.p.rapidapi.com/domains/" + domainname

        headers = {
            'x-rapidapi-key': APIKEY,
            'x-rapidapi-host': "domaination.p.rapidapi.com"
        }

        response = requests.request("GET", url, headers=headers)

        rjson = response.json()

        if rjson["domain"]["isAvailable"] is True:
            print(f"{domainname}: available")

        remainder = COUNTER % 10

        is_divisible = remainder == 0

        if is_divisible:
            print(COUNTER)
