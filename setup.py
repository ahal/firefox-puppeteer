# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.

from setuptools import setup, find_packages

PACKAGE_VERSION = '0.1'

deps = [
    'marionette-client',
]

setup(name='firefox-puppeteer',
      version=PACKAGE_VERSION,
      description='A library built around marionette-client to make automation of the Firefox UI easier.',
      long_description='See https://github.com/mozilla/firefox-puppeteer',
      classifiers=['Environment :: Console',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
                   'Natural Language :: English',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Software Development :: Libraries :: Python Modules',
                   ],
      keywords='mozilla',
      author='Andrew Halberstadt',
      author_email='ahalberstadt@mozilla.com',
      url='https://github.com/mozilla/firefox-puppeteer',
      license='MPL 2.0',
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      install_requires=deps,
)
