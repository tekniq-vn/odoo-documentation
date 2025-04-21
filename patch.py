def setup(app):
    try:
        from sphinx_markdown_builder.builder import MarkdownTranslator
    except ImportError:
        raise ImportError("sphinx_markdown_builder not installed or wrong path")

    original_visit_image = MarkdownTranslator.visit_image

    def custom_visit_image(self, node):
        images = ImageAdapter(self.env)
        node['uri'] = get_original_image_uri(node['uri'])
        return original_visit_image(self, node)

    # Monkey-patch the method
    MarkdownTranslator.visit_image = custom_visit_image

    return {
        'version': '0.1',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }




