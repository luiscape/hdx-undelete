#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
import requests
from hdx_format import item

## Logic 
def collectDatasetDataFromHDX(dataset_id, apikey, verbose = False, test_data = False):
  '''Collect dataset metadata from HDX.'''

  dataset_url = "https://data.hdx.rwlabs.org/api/action/dataset_show?id=" + dataset_id
  headers = { 'Authorization': apikey }

  r = requests.get(dataset_url, headers = headers)
  data = r.json()

  if data["success"] is False:
    print "%s dataset doesn't seem to exist." % item('prompt_error')

    if verbose:
      print data["error"]["message"]

    return False

  if data["success"] is True:
    print "%s collecting data from the dataset %s." % (item('prompt_bullet'), data["result"]["title"].encode('utf-8'))
    return data["result"]


def undeleteDataset(dataset_data, apikey, verbose = False):
  '''Undelete dataset based on JSON input.'''

  if dataset_data is None:
    print "%s dataset data must be provided as a CKAN JSON object." % item('prompt_error')

  print "%s undeleting dataset %s" % (item('prompt_bullet'), dataset_data["title"].encode('utf-8'))
  

  dataset_url = "https://data.hdx.rwlabs.org/api/action/package_update?id=" + dataset_data["id"]
  headers = { 'Authorization': apikey , 'content-type': 'application/json' }
  
  # untelete flag. from "deleted" to "active"
  dataset_data["state"] = "active"

  try:
    r = requests.post(dataset_url, headers=headers, data=json.dumps(dataset_data))
    return True

  except Exception as e:

    if verbose:
      print e

    else:  
      return False



## Execution 
def main(dataset_id, apikey):
  dataset_data = collectDatasetDataFromHDX(dataset_id=dataset_id, apikey=apikey)
  undeleteDataset(dataset_data=dataset_data, apikey=apikey, verbose = False)
  print "%s dataset successfully un-deleted." % item('prompt_success')


if __name__ == '__main__':

  if len(sys.argv) < 2:
    print "%s provide two arguments -- dataset id and API key." % item('prompt_error')

  else:
    main(dataset_id = sys.argv[1], apikey = sys.argv[2])