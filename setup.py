from setuptools import setup, find_packages
setup(
    name = "TEMPLATE",
    version = "0.1",
    packages = ( 'aminatorplugins', ),
    namespace_packages = ( 'aminatorplugins', ),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires = [],

    package_data = { },

    # metadata for upload to PyPI
    author = "AUTHOR",
    author_email = "EMAIL",
    description = "DESCRIPTION",
    license = "APACHE 2.0",
    keywords = "aminator plugin",
)
