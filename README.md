pelican-plugin-alias
====================

[Pelican](http://getpelican.com) plugin for creating alias pages (useful for moving from a different URL scheme such as /&lt;year>/&lt;month>/&lt;title>/ as used by Wordpress)

Inspired by [jekyll_alias_generator](https://github.com/tsmango/jekyll_alias_generator/)

License: MIT

Usage
=====

* Clone to your plugins directory (or git submodule)
* Add to `PLUGINS` in the pelican configuration file
* In each post or page that needs an alias, add an `:alias:` line to the metadata section. Example:

    My Aliased Post
    ##############################################
    :date: 2013-05-31 22:09
    :category: Pelican
    :slug: my-aliased-post
    :alias: /2013/05/my-aliased-post/

    My content goes here.

This will create an additional HTML document at the path specified by `:alias:` that performs a canonical `meta` refresh to the new URL.
If the path ends in a slash (as in the above example) then the file actually created will be index.html so that this system will work with
Github pages.

Multiple aliases can be created for a single post by using a comma-delimited list. The delimiter may be changed by setting `ALIAS_DELIMITER`
in the pelican configuration file.
