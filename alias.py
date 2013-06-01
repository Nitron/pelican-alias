# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
import logging

from pelican import signals

logger = logging.getLogger(__name__)


class AliasGenerator(object):
    def __init__(self, context, settings, path, theme, output_path, *args):
        self.output_path = output_path
        self.context = context
        self.alias_delimiter = settings.get('ALIAS_DELIMITER', ',')

    def create_alias(self, page, alias):
        # If path starts with a /, remove it
        if alias[0] == '/':
            relative_alias = alias[1:]
        else:
            relative_alias = alias

        path = os.path.join(self.output_path, relative_alias)
        directory, filename = os.path.split(path)

        try:
            os.makedirs(directory)
        except OSError:
            logger.warn('[alias] Directory %s already exists' % directory)

        if filename == '':
            path = os.path.join(path, 'index.html')

        logger.info('[alias] Writing to alias file %s' % path)
        # TODO: Find a better way to get the URL to redirect to. This method doesn't work in development.
        with open(path, 'w') as fd:
            fd.write("""<!DOCTYPE html><html><head><link rel="canonical" href="%s"/>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta http-equiv="refresh" content="0;url=/%s" /></head></html>""" % (alias, page.url))

    def generate_output(self, writer):
        pages = self.context['pages'] + self.context['articles']

        for page in pages:
            if 'alias' not in page.metadata.keys():
                continue

            for alias in page.metadata['alias'].split(self.alias_delimiter):
                logger.info('[alias] Processing alias %s' % alias)
                self.create_alias(page, alias)


def get_generators(generators):
    return AliasGenerator


def register():
    signals.get_generators.connect(get_generators)
