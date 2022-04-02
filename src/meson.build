pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'minirouter')

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation('python3').path())
conf.set('pkgdatadir', pkgdatadir)

configure_file(
    input: 'minirouter.in',
    output: 'minirouter',
    configuration: conf,
    install: true,
    install_dir: get_option('bindir')
)

minirouter_sources = [
    '__init__.py',
    'main.py'
]

install_data(minirouter_sources, install_dir: moduledir)
