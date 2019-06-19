class Config:
    '''
    Class to Create the Config for installation
    ------------------------------------------
    User_name:
    User_email:

    interactive:
    REPO_NAME:
    GIT:
    docker:
    color:
    requriements:
    manifest:
    ci:
    readme:
    license:
    gitignore:
    contributing:
    '''

    licenses = ['mit', 'agpl3', 'apache2', 'gnu2',
                'gnugpl3', 'gpl3', 'lgpl3', 'mpl2', 'unilicense']

    basic_files = [
        "license",
        "git",
        "color",
        "requirements",
        "tests",
        "main",
        "contributing",
        "setup_py",
        "readme",
    ]

    not_basic_files = [
        "license",
        "git",
        "color",
        "requirements",
        "tests",
        "main",
        "contributing",
        "interactive",
        "manifest",
        "setup_cfg",
        "setup_py",
        "dockerfile",
        "readme",
    ]

    options = dict([
        # ! Miscellenous options
        ("default", True),
        ("config_location", '.'),
        ("display_options", True),
        ("clear_directory", False),

        # ! Project Details
        ("project_name", 'gayshit'),
        ("project_version", '0.01alpha'),
        ("project_description", 'project_descriptions'),
        ("author_name", 'Ratin Kumar'),
        ("author_email", 'placeholder.com'),
        ("github_username", 'DumbMachine'),
        ("license", 'MIT'),

        # ! Repo related options
        ('files', dict([
            ("license", 'MIT'),
            ("git", True),
            ("color", True),
            ("requirements", True),
            ("tests", True),
            ("main", True),
            ("contributing", True),
            ("interactive", False),
            ("manifest", False),
            ("setup_cfg", False),
            ("setup_py", True),
            ("dockerfile", False),
            ("readme", 'markdown'),
        ])),

        # ! Shields
        ('shields', dict([
            ("base", ['chat', 'build', 'custom', 'license']),
            ("entity", ['discord', 'appveyor', 'custom', 'github']),
        ]))
    ])

    actions = dict([
        # ! Miscellenous options
        ("default", True),
        ("config_location", '.'),
        ("display_options", True),
        ("clear_directory", False),

        # ! Project Details
        ("project_name", 'PrjectGetGPA'),
        ("project_version", '0.01alpha'),
        ("project_description", 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'),
        ("author_name", 'Ratin Kumar'),
        ("author_email", 'placeholder.com'),
        ("github_username", 'DumbMachine'),

        # ! Repo related options
        ("license", 'writer_licence'),
        ("git", 'writer_git'),
        ("requirements", 'writer_requriements'),
        ("readme", 'writer_readme'),
        ("contributing", 'writer_contributing'),
        ("manifest", 'writer_manifest'),
        ("setup_cfg", 'writer_setup_cfg'),
        ("setup_py", 'writer_setup_py'),
        ("dockerfile", 'writer_dockerfile'),
        ('gitignore', 'writer_gitignore'),
        ('tests', 'writer_tests'),
        ('main', 'writer_main'),
    ])


def custom_reader(location):
    custom = '''project_name: "PrjectGetGPA"
project_version: 0.01alpha
project_description: "Working project has the following descriptions. I dont even remember how to write fast of this things. I have gotten so function slow."
author_name: "Ratin Kumar"
github_username: "DumbMachine"
github_email: "ratin.kumar.2k@gmail.com"

license: "MIT"
git: True
color: True
requirements: True
readme: "markdown"
contributing: True
interactive: False

shields:
  build: "bitrise"
  codecov: "codecov"
  analysis: "gtihub-lanugage-count"
  chat: "discord"
  dependencies:
  size: "github-repo-size"
  downloads:
  funding:
  issues:
  license: "github"
  rating:
  social:
  version: "pypi"
  platform:
  monitoring:
  activity:
  other:
'''
    thing = yaml.load(custom, Loader=yaml.Loader)

    files = [
        "license",
        "git",
        "color",
        "requirements",
        "tests",
        "main",
        "contributing",
        "interactive",
        "manifest",
        "setup_cfg",
        "setup_py",
        "dockerfile",
        "readme",
    ]

    shields = [
        "build",
        "codecov",
        "analysis",
        "chat",
        "dependencies",
        "size",
        "downloads",
        "funding",
        "issues",
        "license",
        "rating",
        "social",
        "version",
        "platform",
        "monitoring",
        "activity",
        "other",
        "custom_shield",
    ]

    conf = Config()
    print('gay', conf.options)
    for item in thing.keys():
        if item in files:
            conf.options['files'][item] = thing[item]
        # elif item in shields:
        elif item == 'shields':
            for small_item in thing[item].keys():
                conf.options['shields']['base'].append(small_item)
                conf.options['shields']['entity'].append(
                    thing[item][small_item])
        else:
            # try:
            conf.options[item] = thing[item]

    print(conf.options)
    return conf


custom = '''project_name: 'PrjectGetGPA'
project_version: 0.01alpha
project_description: 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'
author_name: 'Ratin Kumar'
github_username: 'DumbMachine'

default: False

license: 'MIT'
git: True
colour: True
interactive: True
default: True
git: True
colour: True
interactive: True

setup_py: True
setup_cfg: True
main: True
manifest: True
setup.cfg: True
docker: True
requirements: True
contributing: True
readme: 'markdown'

shields:
    build: 'appveyor'
    codecov: 'codecov'
    analysis: 'gtihub-lanugage-count'
    chat: 'discord'
    dependencies:
    size: 'github-repo-size'
    downloads:
    funding:
    issues:
    license: 'github'
    rating:
    social:
    version: 'pypi'
    platform:
    monitoring:
    activity:
    other:
'''
thing = yaml.load(custom, Loader=yaml.Loader)

files = [
    "license",
    "git",
    "color",
    "requirements",
    "tests",
    "main",
    "contributing",
    "interactive",
    "manifest",
    "setup_cfg",
    "setup_py",
    "dockerfile",
    "readme",
]

shields = [
    "build",
    "codecov",
    "analysis",
    "chat",
    "dependencies",
    "size",
    "downloads",
    "funding",
    "issues",
    "license",
    "rating",
    "social",
    "version",
    "platform",
    "monitoring",
    "activity",
    "other",
    "custom_shield",
]


class Config:
    '''
    Class to Create the Config for installation
    ------------------------------------------
    User_name:
    User_email:

    interactive:
    REPO_NAME:
    GIT:
    docker:
    color:
    requriements:
    manifest:
    ci:
    readme:
    license:
    gitignore:
    contributing:
    '''

    licenses = ['mit', 'agpl3', 'apache2', 'gnu2',
                'gnugpl3', 'gpl3', 'lgpl3', 'mpl2', 'unilicense']

    basic_files = [
        "license",
        "git",
        "color",
        "requirements",
        "tests",
        "main",
        "contributing",
        "setup_py",
        "readme",
    ]

    not_basic_files = [
        "license",
        "git",
        "color",
        "requirements",
        "tests",
        "main",
        "contributing",
        "interactive",
        "manifest",
        "setup_cfg",
        "setup_py",
        "dockerfile",
        "readme",
    ]

    options = dict([
        # ! Miscellenous options
        ("default", True),
        ("config_location", '.'),
        ("display_options", True),
        ("clear_directory", False),

        # ! Project Details
        ("project_name", 'gayshit'),
        ("project_version", '0.01alpha'),
        ("project_description", 'project_descriptions'),
        ("author_name", 'Ratin Kumar'),
        ("author_email", 'placeholder.com'),
        ("github_username", 'DumbMachine'),
        ("license", 'MIT'),

        # ! Repo related options
        ('files', dict([
            ("license", 'MIT'),
            ("git", True),
            ("color", True),
            ("requirements", True),
            ("tests", True),
            ("main", True),
            ("contributing", True),
            ("interactive", False),
            ("manifest", False),
            ("setup_cfg", False),
            ("setup_py", True),
            ("dockerfile", False),
            ("readme", 'markdown'),
        ])),

        # ! Shields
        ('shields', dict([
            ("base", ['chat', 'build', 'custom', 'license']),
            ("entity", ['discord', 'appveyor', 'custom', 'github']),
        ]))
    ])

    actions = dict([
        # ! Miscellenous options
        ("default", True),
        ("config_location", '.'),
        ("display_options", True),
        ("clear_directory", False),

        # ! Project Details
        ("project_name", 'PrjectGetGPA'),
        ("project_version", '0.01alpha'),
        ("project_description", 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'),
        ("author_name", 'Ratin Kumar'),
        ("author_email", 'placeholder.com'),
        ("github_username", 'DumbMachine'),

        # ! Repo related options
        ("license", 'writer_licence'),
        ("git", 'writer_git'),
        ("requirements", 'writer_requriements'),
        ("readme", 'writer_readme'),
        ("contributing", 'writer_contributing'),
        ("manifest", 'writer_manifest'),
        ("setup_cfg", 'writer_setup_cfg'),
        ("setup_py", 'writer_setup_py'),
        ("dockerfile", 'writer_dockerfile'),
        ('gitignore', 'writer_gitignore'),
        ('tests', 'writer_tests'),
        ('main', 'writer_main'),
    ])


def custom_reader(location):
    custom = '''project_name: "PrjectGetGPA"
project_version: 0.01alpha
project_description: "Working project has the following descriptions. I dont even remember how to write fast of this things. I have gotten so function slow."
author_name: "Ratin Kumar"
github_username: "DumbMachine"
github_email: "ratin.kumar.2k@gmail.com"

license: "MIT"
git: True
color: True
requirements: True
readme: "markdown"
contributing: True
interactive: False

shields:
  build: "bitrise"
  build: "not_bitrise"
  codecov: "codecov"
  analysis: "gtihub-lanugage-count"
  chat: "discord"
  dependencies:
  size: "github-repo-size"
  downloads:
  funding:
  issues:
  license: "github"
  rating:
  social:
  version: "pypi"
  platform:
  monitoring:
  activity:
  other:
'''
    thing = yaml.load(custom, Loader=yaml.Loader)

    files = [
        "license",
        "git",
        "color",
        "requirements",
        "tests",
        "main",
        "contributing",
        "interactive",
        "manifest",
        "setup_cfg",
        "setup_py",
        "dockerfile",
        "readme",
    ]

    shields = [
        "build",
        "codecov",
        "analysis",
        "chat",
        "dependencies",
        "size",
        "downloads",
        "funding",
        "issues",
        "license",
        "rating",
        "social",
        "version",
        "platform",
        "monitoring",
        "activity",
        "other",
        "custom_shield",
    ]

    conf = Config()
    print('gay', conf.options)
    for item in thing.keys():
        if item in files:
            conf.options['files'][item] = thing[item]
        # elif item in shields:
        elif item == 'shields':
            for small_item in thing[item].keys():
                conf.options['shields']['base'].append(small_item)
                conf.options['shields']['entity'].append(
                    thing[item][small_item])
        else:
            # try:
            conf.options[item] = thing[item]

    print(conf.options)
    return conf


{
    'default': True,
    'config_location': '.',
    'display_options': True,
    'clear_directory': False,
    'project_name': 'PrjectGetGPA',
    'project_version': '0.01alpha',
    'project_description': 'Working project has the following descriptions. I dont even remember how to write fast of this things. I have gotten so function slow.',
    'author_name': 'Ratin Kumar',
    'author_email': 'placeholder.com',
    'github_username': 'DumbMachine',
    'license': 'MIT',
    'files': {
        'license': 'MIT',
        'git': True,
        'color': True,
        'requirements': True,
        'tests': True,
        'main': True,
        'contributing': True,
        'interactive': False,
        'manifest': False,
        'setup_cfg': False,
        'setup_py': True,
        'dockerfile': False,
        'readme': 'markdown'},
    'shields': {
        'base': [
            'chat',
            'build',
            'custom',
            'license',
            'build',
            'codecov',
            'analysis',
            'chat',
            'dependencies',
            'size',
            'downloads',
            'funding',
            'issues',
            'license',
            'rating',
            'social',
            'version',
            'platform',
            'monitoring',
            'activity',
            'other'],
        'entity': [
            'discord',
            'appveyor',
            'custom',
            'github',
            'not_bitrise',
            'codecov',
            'gtihub-lanugage-count',
            'discord',
            None,
            'github-repo-size',
            None,
            None,
            None,
            'github',
            None,
            None,
            'pypi',
            None,
            None,
            None,
            None]},
    'github_email': 'ratin.kumar.2k@gmail.com'}

{'default': True,
    'config_location': '.',
    'display_options': True,
    'clear_directory': False,
    'project_name': 'gayshit',
    'project_version': '0.01alpha',
    'project_description': 'project_descriptions',
    'author_name': 'Ratin Kumar',
    'author_email': 'placeholder.com',
    'github_username': 'DumbMachine',
    'license': 'MIT',
    'files': {'license': 'MIT',
              'git': True,
              'color': True,
              'requirements': True,
              'tests': True,
              'main': True,
              'contributing': True,
              'interactive': False,
              'manifest': False,
              'setup_cfg': False,
              'setup_py': True,
              'dockerfile': False,
              'readme': 'markdown'},
    'shields': {'base': ['chat',
                         'build',
                         'custom',
                         'license'],
                'entity': ['discord',
                           'appveyor',
                           'custom',
                           'github']}}
