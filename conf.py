### no use now, leave it for later
import os
import sys

# Save original directory
original_cwd = os.getcwd()

# Adjust path to your local clone of Odoo docs
# e.g., if your project is at ./mydocs and Odoo is at ../odoo/documentation
odoo_docs_path = os.path.abspath('odoo-docs')

# Change working directory so relative imports & paths inside Odoo's conf.py work
os.chdir(odoo_docs_path)

# Add Odoo docs to sys.path
sys.path.insert(0, odoo_docs_path)

# Import Odoo's Sphinx config
from conf import *  # noqa: F403

# Revert back if needed
os.chdir(original_cwd)

# --- Your custom overrides below ---

# Append your own extensions
extensions += [
    'sphinx.ext.duration',
    'sphinx.ext.autosectionlabel',
]

# Override theme options
html_title = "Custom Docs Based on Odoo"
html_theme_options['logo_only'] = True  # noqa: F405

# Add your custom static assets
html_static_path.append('_static')  # noqa: F405

