import urllib2
import re, json
import pickle
import operator
from pprint import pprint
from bs4 import BeautifulSoup

def stripTags(data):
    p = re.compile(r'<.*?>')
    return p.sub('', str(data))

def get_html(url):
   hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
          'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',}
   req = urllib2.Request(url, headers=hdr)
   html = None
   try:
       html = urllib2.urlopen(req).read()
   except urllib2.HTTPError, e:
       print "URL broke: %s" % url
   return html

def find_tags(html, tag_name, class_name=False):
   soup = BeautifulSoup(html)
   if class_name: tags = soup.findAll(tag_name, { "class" : class_name })
   else: tags = soup.findAll(tag_name)
   return tags

def print_text(url):
     html = get_html(url)
     tags = find_tags(html, 'p')
     for tag in tags:
          print tag.text.replace('\n','').replace('\r','').replace('  ','')
          print

def get_skills(profile_url):
    html = get_html(profile_url)
    tags = stripTags(find_tags(html, 'span', 'endorse-item-name-text'))
    return tags

def read_profile_links(file):
    data = json.loads(open(file, 'r+').read())
    return [link['publicProfileUrl'] for link in data if link]

def get_all_skills(file = '../data/profile-links.json'):
    links = read_profile_links(file)
    total_skills = []

    for i, link in enumerate(links):
        print i
        skills = get_skills(link)
        total_skills.append(skills)

    pickle.dump(total_skills, open( "../data/skills.p", "wb" ))

skills = pickle.load(open('../data/skills.p', 'rb'))

d = {}
for skill_list in skills:
    for skill in re.split('\[|\]|\, ', skill_list):
        if skill: d[skill] = d.setdefault(skill,0) + 1

sorted_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
pprint(sorted_d)
