from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(
    name='ckanext-sustainhawaii',
    version=version,
    description="CKAN extension for Sustain Hawaii",
    long_description='''
    ''',
    classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
    keywords='',
    author='boxkite',
    author_email='contact@boxkite.ca',
    url='',
    license='AGPL',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    namespace_packages=['ckanext', 'ckanext.sustainhawaii'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        # -*- Extra requirements: -*-
    ],
    entry_points='''
        [ckan.plugins]
        # Add plugins here, e.g.
        hawaii=ckanext.sustainhawaii.plugin:HawaiiThemePlugin
    ''',
)
