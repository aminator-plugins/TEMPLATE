This page will give you an overview on how to correctly structure your plugin to be accepted into
the aminator-plugins suite.

## Repo structure overview
When building an aminator plugin compatible with the aminator-plugin utility, you should start by
cloning this template structure into a new folder that you will use as the basis for your plugin.
Below is an example of a provisioner plugin's folder structure.
```none
├── aminatorplugins
│   ├── __init__.py
│   └── provisioner
│       ├── __init__.py
│       └── my_plugin.py
├── default_conf
│   └── aminatorplugins.provisioner.my_plugin.yml
└── setup.py
```

### setup.py
The `setup.py` file is a standard [setuptools](http://pythonhosted.org/setuptools/setuptools.html) file, but there are some key points of the file that
are vital for correct operation with aminator.

#### Namespace package
Firstly, to make sure that your plugin is able to be picked up, you must declare that you are
providing a namespace package. Doing so allows multiple installed packages to share the same
namespace. This is done by adding the line 
```
namespace_packages = ( 'aminatorplugins', ),
```

#### Data files
Next we need to ensure that any configuration files needed by your plugin, is copied to the standard
aminator plugin configuration location. This is done with the data_files section in the setup call:
```python
    data_files = [
        ('/etc/aminator/plugins', ['default_conf/aminatorplugins.provisioner.my_plugin.yml']),
    ],
```
This block tells setuptools to copy `default_conf/aminatorplugins.provisioner.my_plugin.yml` 
into `/etc/aminator/plugins`. It's important to note, that aminator will load the configuration
files based off the package name, not the class name.

#### Entry points
Finally, but most importantly, we need to declare an entry point. This is the mechanism by which aminator
discovers all plugins.

```python
    entry_points = {
       'aminator.plugins.TYPE': [
           'my_plugin = aminatorplugins.TYPE.my_plugin:MyPluginClass',
       ],
    },
```

It is important to note here, that the entry point namespace needs to be the actual aminator namespace,
for example `aminator.plugins.provisioner`, otherwise aminator will not be able to discover your plugin. More information on entry_points can be found in the [pkg_resources documentation](http://pythonhosted.org/distribute/pkg_resources.html#entry-points)
