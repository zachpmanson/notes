'''
Based on Backlinks Extension for Python-Markdown
======================================

Converts [[Backlinks]] to relative links.

See <https://Python-Markdown.github.io/extensions/backlinks>
for documentation.

Original code Copyright [Waylan Limberg](http://achinghead.com/).

All changes Copyright The Python Markdown Project

License: [BSD](https://opensource.org/licenses/bsd-license.php)

Modified by Zach Manson to support [[Backlink|Aliases]]
'''

from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree

import re


def build_url(label, base, end):
    """ Build a URL from the label, a base, and an end. """
    clean_label = re.sub(r'([ ]+_)|(_[ ]+)|([ ]+)', '_', label)
    return '{}{}{}'.format(base, clean_label, end)


class BacklinkExtension(Extension):

    def __init__(self, **kwargs):
        self.config = {
            'base_url': ['/', 'String to append to beginning or URL.'],
            'end_url': ['/', 'String to append to end of URL.'],
            'html_class': ['backlink', 'CSS hook. Leave blank for none.'],
            'build_url': [build_url, 'Callable formats URL from label.'],
        }

        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        self.md = md

        # append to end of inline patterns
        BACKLINK_RE = r'\[\[([\w0-9_ \-\|\#\,\'\(\)]+)\]\]'
        backlinkPattern = BacklinkInlineProcessor(BACKLINK_RE, self.getConfigs())
        backlinkPattern.md = md
        md.inlinePatterns.register(backlinkPattern, 'backlink', 75)


class BacklinkInlineProcessor(InlineProcessor):
    def __init__(self, pattern, config):
        super().__init__(pattern)
        self.config = config

    def handleMatch(self, m, data):
        if m.group(1).strip():
            base_url, end_url, html_class = self._getMeta()
            segments = m.group(1).strip().split("|")
            if len(segments) == 2:
                alias = segments[1]
                url_segment = segments[0]
            else:
                alias = segments[0]
                url_segment = segments[0]
            
            url = self.config['build_url'](url_segment, base_url, end_url)
            a = etree.Element('a')
            a.text = alias
            a.set('href', url)
            if html_class:
                a.set('class', html_class)
        else:
            a = ''
        return a, m.start(0), m.end(0)

    def _getMeta(self):
        """ Return meta data or `config` data. """
        base_url = self.config['base_url']
        end_url = self.config['end_url']
        html_class = self.config['html_class']
        if hasattr(self.md, 'Meta'):
            if 'wiki_base_url' in self.md.Meta:
                base_url = self.md.Meta['wiki_base_url'][0]
            if 'wiki_end_url' in self.md.Meta:
                end_url = self.md.Meta['wiki_end_url'][0]
            if 'wiki_html_class' in self.md.Meta:
                html_class = self.md.Meta['wiki_html_class'][0]
        return base_url, end_url, html_class


def makeExtension(**kwargs):  # pragma: no cover
    return BacklinkExtension(**kwargs)