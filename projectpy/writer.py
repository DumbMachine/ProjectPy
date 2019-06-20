import os
import sys
from .content import Content
import subprocess


def writer_blank(location):
    pass


def writer_gitignore(location):
    open(os.path.join(location, '.gitignore'), 'w+').write(Content.gitignore)


def writer_setup_py(location, data):
    open(os.path.join(location, 'setup.py'),
         'w+').write(Content.setup_py.format_map(data))


def writer_licence(location, license_type):
    try:
        open(os.path.join(
            location, f'LICENSE'), 'w+').write(Content.license[license_type.lower()])
    except:
        raise NotImplementedError(
            f"Given {hmm.lower()} license is not implemented.")


def writer_requriements(location):
    open(os.path.join(location, 'requirements.txt'), 'w+').close()


def writer_setup_cfg(location):
    open(os.path.join(location, 'setup.cfg'), 'w+').write(Content.setup_cfg)


def writer_dockerfile(location, name):
    open(os.path.join(location, 'dockerfile'),
         'w+').write(Content.dockerfile.format(name))


def writer_isort(location):
    open(os.path.join(location, 'setup.cfg'), 'w+').write(Content.setup_cfg)


def writer_black(location):
    open(os.path.join(location, 'black.'), 'w+').write(Content.setup_cfg)


def writer_manifest(location, name):
    open(os.path.join(location, 'MANIFEST.ini'),
         'w+').write(Content.manifest.format(name))


def writer_travis(location):
    open(os.path.join(location, '.travis.yml'),
         'w+').write(Content.setup_cfg)


def writer_appveyor(location):
    open(os.path.join(location, 'appveyor.yml'),
         'w+').write(Content.setup_cfg)


def writer_contributing(location):
    open(os.path.join(location, 'appveyor.yml'),
         'w+').write(Content.contributing)


def writer_git(location):
    # os.system(f"git init {location}")
    subprocess.Popen(f"git init {location}",
                     shell=True, stdout=subprocess.PIPE)
    # p = subprocess.Popen(["git", "init", f"{location}"], shell=True,
    #                      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    # p.wait()
    # print(p.stdout)


def writer_tests(location):
    if not os.path.exists(os.path.join(location, 'tests')):
        os.makedirs(os.path.join(location, 'tests'))
    open(os.path.join(os.path.join(location, 'tests'),
                      '__init__.py'), 'w+').write("TESTS file")


def writer_main(location, repo_name):
    if not os.path.exists(os.path.join(location, repo_name)):
        os.makedirs(os.path.join(location, repo_name))
    open(os.path.join(os.path.join(location, repo_name),
                      '__init__.py'), 'w+').write("print('Succesfull Installation')")


def big_writer(location, data):
    '''
    Responsible for writing the following files:
    ['dockerfile', 'LICENSE', 'MANIFEST.in', 'README.md', 'requirements.txt', 'setup.cfg', 'setup.py']
    '''
