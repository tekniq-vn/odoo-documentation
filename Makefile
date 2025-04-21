# Makefile for Sphinx documentation
include .env

# Pass WORKERS=1 for single-worker build
ifndef WORKERS
  WORKERS = auto
endif

ODOO_DIR       = odoo-docs

ifndef BUILD_DIR
  BUILD_DIR    = _build
endif

ifndef CURRENT_LANG
  CURRENT_LANG = en
endif

SPHINX_BUILD   = sphinx-build
CONFIG_DIR     = $(ODOO_DIR)
SPHINXOPTS     = -D project_root=$(ROOT) -D canonical_version=$(CANONICAL_VERSION) \
                 -D versions=$(VERSIONS) -D languages=$(LANGUAGES) -D language=$(CURRENT_LANG) \
                 -D is_remote_build=$(IS_REMOTE_BUILD) \
                 -T \
                 -A google_analytics_key=$(GOOGLE_ANALYTICS_KEY) \
                 -A plausible_script=$(PLAUSIBLE_SCRIPT) \
                 -A plausible_domain=$(PLAUSIBLE_DOMAIN) \
				 -j $(WORKERS)
SOURCE_DIR     = $(ODOO_DIR)/content

MD_BUILD_DIR = $(BUILD_DIR)/md
ifdef VERSIONS
  MD_BUILD_DIR := $(MD_BUILD_DIR)/17.0
endif
ifneq ($(CURRENT_LANG),en)
  MD_BUILD_DIR := $(MD_BUILD_DIR)/$(CURRENT_LANG)
endif


.PHONY: markdown clean

clean: 
	@echo "Cleaning build files..."
	rm -rf $(BUILD_DIR)/*
	@echo "Cleaning finished."

markdown: $(MD_BUILD_DIR)/_static/style.css
	@echo "Starting build..."
	$(SPHINX_BUILD) -c $(CONFIG_DIR) -b markdown $(SPHINXOPTS) $(SOURCE_DIR) $(MD_BUILD_DIR)
	@echo "Build finished."

$(MD_BUILD_DIR)/_static/style.css: $(ODOO_DIR)/extensions/odoo_theme/static/style.scss $(ODOO_DIR)/extensions/odoo_theme/static/scss/*.scss
	@echo "Compiling stylesheets..."
	mkdir -p $(MD_BUILD_DIR)/_static
	python3 -m pysassc $(ODOO_DIR)/extensions/odoo_theme/static/style.scss $(MD_BUILD_DIR)/_static/style.css
	@echo "Compilation finished."

static:
	@echo "⏳  Copying images from content/ …"
	@rsync -av \
	  --include='*/' \
	  --include='*.png' \
	  --include='*.jpg' \
	  --include='*.jpeg' \
	  --include='*.svg' \
	  --exclude='*' \
	  $(ODOO_DIR)/content/ \
	  $(MD_BUILD_DIR)
	@echo "✅  Markdown + images in $(MD_BUILD_DIR)"
