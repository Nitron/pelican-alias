from os.path import abspath, dirname, join, normpath

from setuptools import setup

setup(
    name = 'pelican-alias',
    version = '1.0',
    py_modules = ('pelican_alias',),

    zip_safe = False,
    include_package_data = True,

    install_requires = ['pelican>=3.1.1'],

    author = 'Christopher Williams',
    author_email = 'chris@christopher-williams.net',
    license = 'MIT',
    url = 'http://github.com/Nitron/pelican-alias',
    download_url = 'http://github.com/Nitron/pelican-alias/tarball/1.0',
    keywords = 'pelican blog',
    description = 'Pelican plugin for creating alias pages (useful for moving from a different URL scheme such as /<year>/<month>/<title>/ as used by Wordpress).',
)
