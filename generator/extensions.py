from markdown.inlinepatterns import InlineProcessor
from markdown.extensions import Extension
import xml.etree.ElementTree as etree


class CiteInlineProcessor(InlineProcessor):
    def handleMatch(self, m, data):
        el = etree.Element('cite')
        el.text = m.group(1)
        return el, m.start(0), m.end(0)

class CiteExtension(Extension):
    def extendMarkdown(self, md):
        CITE_PATTERN = r'--(.*)$'  # like --Zach Manson
        md.inlinePatterns.register(CiteInlineProcessor(CITE_PATTERN, md), 'cite', 175)