import jinja2
import feedparser
import os
import copy               # Added for deepcopy() support
from pprint import pprint # For easy debugging (To be removed in production code)

# Start of programming
default_file = 'feed.xml'
rendered_filename = "demo.html"

root = os.path.dirname(os.path.abspath(__file__))
templates_dir = os.path.join(root, 'templates')
env = jinja2.Environment( loader = jinja2.FileSystemLoader(templates_dir) )
template = env.get_template('demo_template.html')
output_file_path = os.path.join(root, 'Output')
rendered_file_path = os.path.join(output_file_path, rendered_filename)

f = feedparser.parse(url_file_stream_or_string=default_file)

job_list = []

for item in f['entries']:
    job_dict = {
        'title':    item['title'],
        # 'id':       item['id'],
        'summary':  item['summary']
        # 'content':  item['content'][0]['value']
    }
    job_list.append(copy.deepcopy(job_dict))

output_text_html = template.render(parent_list=job_list)

with open(rendered_file_path, "w") as result_file:
    result_file.write(output_text_html)
print("Successfully written to "+str(rendered_filename)+"!")
