### no use now, leave it for later
import os
import sys
from pathlib import Path

import logging
print("##############################################")
logger = logging.getLogger(__name__)
logger.info(sys.path)
print(sys.path)


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
logger.info(sys.path)
print(sys.path)

# Revert back if needed
os.chdir(original_cwd)

# --- Your custom overrides below ---
# Add extensions directory to PYTHONPATH
extension_dir = Path('extensions')
sys.path.insert(0, str(extension_dir.absolute()))
logger.info(sys.path)
print(sys.path)

# Append your own extensions
extensions += [
    'gitbook',
]

