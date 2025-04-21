import os, sys

sys.path.insert(0, os.path.abspath('odoo-docs'))

def main():
    from conf import extensions
    extensions = list(extensions) + ['..patch']
    print(",".join(extensions))
    return extensions

if __name__ == "__main__":
    main()
