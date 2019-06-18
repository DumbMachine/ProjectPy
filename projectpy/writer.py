import os
import sys
from .content import Content


def writer_gitignore(location):
    open(os.path.join(location, 'mock_.gitignore'), 'w+').write(Content.gitignore)


def writer_setup_py(location):
    open(os.path.join(location, 'mock_setup.py'), 'w+').write(Content.setup_py)


def writer_licence(location, license):
    # for licenze in Content.license.keys():
    open(os.path.join(
        location, f'mock_{licenze}'), 'w+').write(Content.license[license])


def writer_requriements(location):
    open(os.path.join(location, 'mock_requirements.txt'), 'w+').close()


def writer_setup_cfg(location):
    open(os.path.join(location, 'mock_setup.cfg'), 'w+').write(Content.setup_cfg)


def writer_dockerfile(location):
    open(os.path.join(location, 'mock_dockerfile'), 'w+').write(Content.setup_cfg)


def writer_isort(location):
    open(os.path.join(location, 'mock_setup.cfg'), 'w+').write(Content.setup_cfg)


def writer_black(location):
    open(os.path.join(location, 'mock_black.'), 'w+').write(Content.setup_cfg)


def writer_manifest(location):
    open(os.path.join(location, 'mock_MANIFEST.ini'),
         'w+').write(Content.setup_cfg)


def writer_travis(location):
    open(os.path.join(location, 'mock_.travis.yml'),
         'w+').write(Content.setup_cfg)


def writer_appveyor(location):
    open(os.path.join(location, 'mock_appveyor.yml'),
         'w+').write(Content.setup_cfg)


def writer_contributing(location):
    print("writer_contributing")
    raise NotImplementedError


def writer_git(location):
    print("writer_git")
    raise NotImplementedError


def writer_readme(location):
    print("writer_readme")
    raise NotImplementedError


# writer_setup_cfg(os.getcwd())
# writer_requriements(os.getcwd())
# licencer(os.getcwd())
# writer_gitignore(os.getcwd())
# writer_setup_py(os.getcwd())
