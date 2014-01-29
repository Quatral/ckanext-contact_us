from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(
	name='ckanext-contact_us',
	version=version,
	description="",
	long_description="""\
	""",
	classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
	keywords='',
	author='',
	author_email='0.1',
	url='',
	license='',
	packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
	namespace_packages=['ckanext', 'ckanext.contact_us'],
	include_package_data=True,
	zip_safe=False,
	install_requires=[
		# -*- Extra requirements: -*-
	],
	entry_points='''
    [ckan.plugins]
    contact_us_plugin=ckanext.contact_us.plugin:ContactUsPlugin
''',
)
