# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os.path
import logging

from pelican import signals
from jinja2 import Template

logger = logging.getLogger(__name__)


class AliasGenerator(object):
    TEMPLATE = """<!DOCTYPE html><html><head><link rel="canonical" href="/{{ destination_path }}"/>
<meta http-equiv="content-type" content="text/html; charset=utf-8" />
<meta http-equiv="refresh" content="0;url=/{{ destination_path }}" />
</head></html>
"""

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
            pass

        if filename == '':
            path = os.path.join(path, 'index.html')

        logger.info('[alias] Writing to alias file %s' % path)
        with open(path, 'w') as fd:
            template = Template(self.TEMPLATE)
            fd.write(template.render(destination_path=page.url))

    def generate_output(self, writer):
        pages = self.context['pages'] + self.context['articles']

        for page in pages:
            if 'alias' not in page.metadata.keys():
                continue

            for alias in page.metadata['alias'].split(self.alias_delimiter):
                alias = alias.strip()
                logger.info('[alias] Processing alias %s' % alias)
                self.create_alias(page, alias)


def get_generators(generators):
    return AliasGenerator


def register():
    signals.get_generators.connect(get_generators)
