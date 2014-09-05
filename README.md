# Setting up your development environment

## Pre-requisites:
Setup CKAN [from source](http://docs.ckan.org/en/latest/maintaining/installing/install-from-source.html)

Install the CKAN scheme extension [ckanext-scheming](https://github.com/open-data/ckanext-scheming)

Specify the dataset schema to use (in your CKAN's development.ini file):
```
ckan.plugins = ... scheming_datasets

scheming.dataset_schemas = ckanext.sustainhawaii:dataset_schema.json
```

## Setup
- Clone this repo:

`git clone git@github.com:SustainHawaii/mapp.git`

- Activate the `virtualenv` you previously setup for you CKAN:

eg. `. /usr/lib/ckan/default/bin/activate`

- Install your extension:
```
cd mapp/
python setup.py develop
```

- Add the extension to the CKAN configuration (your CKAN's development.ini file):
```
ckan.plugins = ... hawaii
```

Finally, start your CKAN:
```
cd /usr/lib/ckan/default/src/ckan/
paster serve development.ini
```
