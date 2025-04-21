
        ######
        this_doc = self.builder.current_doc_name
        this_dir = posixpath.dirname(this_doc)
        node["uri"] = self.builder.get_relative_uri(uri, this_dir)
        #####
