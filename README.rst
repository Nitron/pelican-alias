pelican-alias
====================

`Pelican <http://getpelican.com>`_ plugin for creating alias pages (useful for moving from a different URL scheme such as */<year>/<month>/<title>/* as used by Wordpress).

Inspired by `jekyll_alias_generator <https://github.com/tsmango/jekyll_alias_generator/>`_.

License: MIT

Installation
============

Simply run::

	pip install pelican-alias

Usage
=====

* Add *pelican_alias* to *PLUGINS* in the pelican configuration file
* In each post or page that needs an alias, add an *:alias:* line to the metadata section. Example::

	My Aliased Post
	##############################################
	:date: 2013-05-31 22:09
	:category: Pelican
	:slug: my-aliased-post
	:alias: /2013/05/my-aliased-post/, /2013/even-older-post-address

	My content goes here.

* Markdown example::

    Title: Another Aliased Post
    Date: 2013-06-01 21:10
    Category: Pelican
    Alias: /2013/06/another-aliased-post/
           /2013/even-older-aliased-post-address

    My content goes here.

This will create an additional HTML document at the path specified by *:alias:* that performs a canonical *meta* refresh to the new URL.
If the path ends in a slash (as in the above example) then the file actually created will be index.html so that this system will work with
Github pages.

Multiple aliases can be created for a single post. The delimiter for ReST
format may be changed by setting *ALIAS_DELIMITER* in the pelican
configuration file.
