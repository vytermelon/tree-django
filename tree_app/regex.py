import re
"""
with open("del.txt",'r') as fh:
    data = fh.read().split('\n')
    covered_true = 0.0
    covered_false = 0.0
    total_lines = 0.0
    for i in data:
        total_lines += 1.0
        if "true" in i.lower():
            if "branchesToCover=\"0\"" not in i:
                i = i[i.find("branchesToCover"):]
                true_percent = re.findall(r'"(.*?)"', i)
                true_percent = int(true_percent[1])/int(true_percent[0])
                covered_true = covered_true + true_percent
            else:
                covered_true = covered_true + 1.0
        if "false" in i.lower():
            covered_false = covered_false + 1.0
    print("Total coverage= %f" % (covered_true * 100.0/(total_lines)))
    print("Total lines= %f" % total_lines)
    print("covered_true = %f" % covered_true)
    print("covered_false = %f" % covered_false)


s = "(asdex)METAGEN/specifications/asdex/"
match_lparanth = re.search('\(', s )
match_rparanth = re.search('\)', s)
print(s[match_lparanth.end():match_rparanth.start()])
a = ["a"] *3
print(a)


import requests
from optparse import OptionParser
from requests.auth import HTTPBasicAuth

class BitBucketBuildStatusNotifier:
    def __init__(self, commit, url, state):
        base_url = "https://bitbucket.vih.infineon.com/rest/build-status/1.0/commits/%s" % commit
        payload = {
            "state": state,
            "key": "buildkey",
            "name": "buildname",
            "url": url,
            "description": state
        }
        headers = {"Content-Type": "application/json"}

    def post(self):
        response = requests.post(self.base_url, json=self.payload, verify=False, headers=self.headers,
                                 auth=HTTPBasicAuth('BLRcictajenkins', 'Infineon*123456789'))
        print("Status code: %s " % response.status_code)

parser = OptionParser()
parser.add_option("-c", "--commit",
                    action="store", dest="commit", default=None,
                    help="The required commit id for updating status")
parser.add_option("-u", "--url", action="store", dest="url", default=None,
                    help="Url of the Jenkins Job")
parser.add_option("-s", "--state", action="store", dest="state", default=None,
                    help="State of the Jenkins job")
(options, args) = parser.parse_args()

if options.commit == None:
    parser.error('Commit id not given')
if options.url == None:
    parser.error('Url not given')
if options.state == None:
    parser.error('State not given')
elif options.state not in ["INPROGRESS","SUCCESSFUL","FAILED"]:
    parser.error('State not valid')
else:
    bitbucketBuildStatusNotifier = BitBucketBuildStatusNotifier(options.commit, options.url, options.state)
    bitbucketBuildStatusNotifier.post()
"""
with open("log.txt",'r') as fh:
    data = fh.read()
    if "ERROR: Some missing data!" in data and "ERROR: Some differences found!" in data:
        print("yes")
