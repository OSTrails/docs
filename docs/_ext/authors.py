# Authors: Marek Suchánek
# Description: Sphinx extension for adding authors and contributors to the page
# License: MIT
import pathlib
import yaml

from docutils import nodes

from sphinx.application import Sphinx
from sphinx.util import logging
from sphinx.util.docutils import SphinxDirective


LOG = logging.getLogger(__name__)
DOCS_ROOT = pathlib.Path(__file__).parent.parent
PROJECT_ROOT = DOCS_ROOT.parent
CONTRIBUTORS_FILE = PROJECT_ROOT / 'CONTRIBUTORS.yml'
CONTRIBUTORS = dict()


class Contributor:

    def __init__(self, name: str, orcid: str | None, github: str | None,
                 email: str | None, affiliation: str | None,
                 first_name: str | None = None, last_name: str | None = None):
        self.name = name
        self.orcid = orcid
        self.github = github
        self.email = email
        self.affiliation = affiliation
        self.first_name = first_name
        self.last_name = last_name
        if first_name is None and last_name is None:
            self.first_name, self.last_name = self.name.rsplit(maxsplit=1)


try:
    with open(CONTRIBUTORS_FILE, 'r') as f:
        contributors = yaml.safe_load(f)
        for name, details in contributors.items():
            CONTRIBUTORS[name] = Contributor(
                name=name,
                orcid=details.get('orcid', None),
                github=details.get('github', None),
                email=details.get('email', None),
                affiliation=details.get('affiliation', None),
            )
except Exception:
    LOG.warning(f'Failed to load contributors from {CONTRIBUTORS_FILE.as_posix()}')
    pass


class PageAuthorsDirective(SphinxDirective):
    has_content = True

    def run(self):
        authors_div = nodes.container(classes=['authors'])
        authors_title = nodes.container(classes=['authors-title'])
        authors_title.append(nodes.inline(text='Authors'))
        authors_div.append(authors_title)
        authors_list = nodes.bullet_list(bullet='*')
        authors_div.append(authors_list)
        for author in self.content:
            if author not in CONTRIBUTORS.keys():
                LOG.warning(f'Author "{author}" not found in CONTRIBUTORS.yaml',
                            location=self.get_location())
                continue
            contributor = CONTRIBUTORS[author]
            author_node = nodes.list_item()
            author_row = nodes.paragraph()
            author_row.append(nodes.inline(text=contributor.name, classes=['author-name']))
            if contributor.orcid:
                orcid_link = nodes.reference(
                    text=contributor.orcid,
                    refuri=f'https://orcid.org/{contributor.orcid}',
                    classes=['author-orcid-link'],
                )
                orcid_inline = nodes.inline(classes=['author-orcid'])
                orcid_inline.append(nodes.inline(text=' ('))
                orcid_inline.append(orcid_link)
                orcid_inline.append(nodes.inline(text=')'))
                author_row.append(orcid_inline)
            if contributor.affiliation:
                author_row.append(nodes.inline(
                    text=f', {contributor.affiliation}',
                    classes=['author-affiliation'],
                ))
            author_node.append(author_row)
            authors_list.append(author_node)

        return [authors_div]


class ContributorsDirective(SphinxDirective):
    has_content = True

    def run(self):
        if not CONTRIBUTORS:
            LOG.warning(f'No contributors found in {CONTRIBUTORS_FILE.as_posix()}',
                        location=self.get_location())

        contributors_div = nodes.container(classes=['contributors'])
        contributors_list = nodes.bullet_list(bullet='*')
        contributors_div.append(contributors_list)
        contributors = list(CONTRIBUTORS.values())
        contributors.sort(key=lambda x: f'{x.last_name}, {x.first_name}')
        for contributor in contributors:
            contributor_node = nodes.list_item()
            contributor_row = nodes.paragraph()
            contributor_name = nodes.inline(text=contributor.name, classes=['contributor-name'])
            contributor_row.append(contributor_name)
            if contributor.orcid:
                orcid_link = nodes.reference(
                    text=contributor.orcid,
                    refuri=f'https://orcid.org/{contributor.orcid}',
                    classes=['contributor-orcid-link'],
                )
                orcid_inline = nodes.inline(classes=['contributor-orcid'])
                orcid_inline.append(nodes.inline(text=' ('))
                orcid_inline.append(orcid_link)
                orcid_inline.append(nodes.inline(text=')'))
                contributor_row.append(orcid_inline)
            if contributor.affiliation:
                contributor_row.append(nodes.inline(
                    text=f', {contributor.affiliation}',
                    classes=['contributor-affiliation'],
                ))
            contributor_node.append(contributor_row)
            contributors_list.append(contributor_node)
        return [contributors_div]


def setup(app: Sphinx) -> dict:
    app.add_directive('page-authors', PageAuthorsDirective)
    app.add_directive('contributors', ContributorsDirective)
    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
