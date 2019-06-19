import os
import sys
from .content import Content


def writer_gitignore(location):
    open(os.path.join(location, '.gitignore'), 'w+').write(Content.gitignore)


def writer_setup_py(location, data):
    open(os.path.join(location, 'setup.py'),
         'w+').write(Content.setup_py.format_map(data))


def writer_licence(location, hmm):
    # for licenze in Content.license.keys():
    try:
        open(os.path.join(
            location, f'LICENSE'), 'w+').write(Content.license[hmm.lower()])
    except:
        raise NotImplementedError(
            f"Given {hmm.lower()} license is not implemented.")


def writer_requriements(location):
    open(os.path.join(location, 'requirements.txt'), 'w+').close()


def writer_setup_cfg(location):
    open(os.path.join(location, 'setup.cfg'), 'w+').write(Content.setup_cfg)


def writer_dockerfile(location):
    open(os.path.join(location, 'dockerfile'), 'w+').write(Content.setup_cfg)


def writer_isort(location):
    open(os.path.join(location, 'setup.cfg'), 'w+').write(Content.setup_cfg)


def writer_black(location):
    open(os.path.join(location, 'black.'), 'w+').write(Content.setup_cfg)


def writer_manifest(location):
    open(os.path.join(location, 'MANIFEST.ini'),
         'w+').write(Content.setup_cfg)


def writer_travis(location):
    open(os.path.join(location, '.travis.yml'),
         'w+').write(Content.setup_cfg)


def writer_appveyor(location):
    open(os.path.join(location, 'appveyor.yml'),
         'w+').write(Content.setup_cfg)


def writer_contributing(location):
    pass
    # print("writer_contributing")
    # raise NotImplementedError


def writer_git(location):
    pass
    # raise NotImplementedError


def writer_readme(location):
    pass
    # raise NotImplementedError


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

# writer_setup_cfg(os.getcwd())
# writer_requriements(os.getcwd())
# licencer(os.getcwd())
# writer_gitignore(os.getcwd())
# writer_setup_py(os.getcwd())
