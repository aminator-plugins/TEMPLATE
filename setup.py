from setuptools import setup, find_packages
setup(
    name = "TEMPLATE",
    version = "0.1",
    packages = find_packages(),
    namespace_packages = ( 'aminatorplugins', 'aminatorplugins.provisioner'),

    data_files = [
        ('/etc/aminator/plugins', ['default_conf/aminatorplugins.TYPE.my_plugin.yml']),
    ],

    entry_points = {
       'aminator.plugins.TYPE': [
           'my_plugin = aminatorplugins.TYPE.my_plugin:MyPluginClass',
       ],
    },

    # metadata for upload to PyPI
    author = "AUTHOR",
    author_email = "EMAIL",
    description = "DESCRIPTION",
    license = "Apache 2.0",
    keywords = "aminator plugin",
)
