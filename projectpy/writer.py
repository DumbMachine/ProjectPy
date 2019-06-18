import os
import sys
from content import Content


def writer_gitignore(location):
    open(os.path.join(location, 'mock_.gitignore'), 'w+').write(Content.gitignore)


def writer_setup_py(location):
    open(os.path.join(location, 'mock_setup.py'), 'w+').write(Content.setup_py)


def licencer(location):
    for licenze in Content.license.keys():
        open(os.path.join(
            location, f'mock_{licenze}'), 'w+').write(Content.license[licenze])


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


writer_setup_cfg(os.getcwd())
writer_requriements(os.getcwd())
licencer(os.getcwd())
writer_gitignore(os.getcwd())
writer_setup_py(os.getcwd())
