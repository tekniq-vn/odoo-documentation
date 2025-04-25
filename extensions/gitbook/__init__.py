import os
from docutils import nodes
from sphinx.environment.adapters.toctree import TocTree
import logging
logger = logging.getLogger(__name__)

def mark_folder_readmes(app, env):
    """Mark documents that should be written as folder/README.md."""
    env.gitbook_folder_readmes = set()

    for parent_doc, child_docs in env.toctree_includes.items():
        if child_docs:
            # If this doc includes children, mark it
            env.gitbook_folder_readmes.add(parent_doc)

def rewrite_links_in_doctree(app, doctree, docname):
    """Rewrite internal links during doctree-resolved stage."""
    if not hasattr(app.env, 'gitbook_folder_readmes'):
        return

    for node in doctree.traverse(nodes.reference):
        refuri = node.get('refuri')
        if not refuri:
            continue

        if refuri.endswith('.md'):
            target_doc = refuri[:-3]  # strip '.md'
            if target_doc in app.env.gitbook_folder_readmes:
                node['refuri'] = target_doc + '/'

def builder_get_outfilename(self, docname):
    """Custom get_outfilename to write folder/README.md."""
    if hasattr(self.env, 'gitbook_folder_readmes') and docname in self.env.gitbook_folder_readmes:
        return os.path.join(self.outdir, docname, 'README.md')
    return os.path.join(self.outdir, docname + '.md')

def builder_get_target_uri(self, docname, typ=None):
    """Custom get_target_uri to link to folder/ instead of file.md."""
    if hasattr(self.env, 'gitbook_folder_readmes') and docname in self.env.gitbook_folder_readmes:
        return docname + '/'
    return docname + '.md'

def setup(app):
    app.connect('env-updated', mark_folder_readmes)
    #app.connect('doctree-resolved', rewrite_links_in_doctree)

    # Patch the builder methods (only for markdown builder)
    #from sphinx_markdown_builder import MarkdownBuilder
    #MarkdownBuilder.get_outfilename = builder_get_outfilename
    #MarkdownBuilder.get_target_uri = builder_get_target_uri

