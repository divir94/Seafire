import json
from pprint import pprint

data = json.loads(open('../data/companies.json').read())
values = data['values']

d = {}

# add industries
for person in values:
    if 'industry' in person:
        d[person['industry']] = {}


# add companies
for person in values:
    if 'industry' in person:
        industry = person['industry']
        if 'positions' in person and 'values' in person['positions']:
            positions = person['positions']['values']
            for company in positions:
                company_name = company['company']['name']
                if company_name in d[industry]:
                    count = d[industry][company_name]
                    d[industry][company_name] = count + 1
                else:
                    d[industry][company_name] = 1

treemap_data = []

for industry, companies in d.iteritems():
    obj = {'name': industry}
    children = []
    values = 0
    for company, count in companies.iteritems():
        children.append({'name': company, 'value': count})
        values += count
    obj['children'] = children
    obj['values'] = values
    treemap_data.append(obj)

json_data = json.dumps(treemap_data)
print json_data
