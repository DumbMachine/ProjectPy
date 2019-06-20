from .writer import *


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
        ("config_location", None),
        ("display_options", True),
        ("clear_directory", True),

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
            ("license", 'unilicense'),
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
            ("conda", False),
            ("dockerfile", False),
            ("readme", 'markdown'),
        ])),

        # ! Shields
        ('shields', ['discord', 'appveyor', 'custom', 'github']),
    ])

    actions = dict([
        # ! Miscellenous options
        ("default", True),
        ("config_location", '.'),
        ("display_options", True),
        ("clear_directory", False),

        # ! Project Details
        ("project_name", '[ProjectPy]PythonPackage'),
        ("project_version", '0.01alpha'),
        ("project_description", ''),
        ("author_name", ''),
        ("author_email", ''),
        ("github_username", ''),

        # ! Repo related options
        ("license", writer_licence),
        ("git", writer_git),
        ("requirements", writer_requriements),
        ("readme", writer_blank),
        ("conda", writer_blank),
        ("contributing", writer_contributing),
        ("manifest", writer_manifest),
        ("setup_cfg", writer_setup_cfg),
        ("setup_py", writer_setup_py),
        ("dockerfile", writer_dockerfile),
        ('gitignore', writer_gitignore),
        ('tests', writer_tests),
        ('main', writer_main),
    ])


# def questions():
#     conf = Config()
#     emojis = ['🚀', '✅', '🏠', '📘', '📦', '💡', '📝', '👤', '👤', '📃', '🗕', 'ℹ']
#     answers = {}
#     questions_to_ask = [
#         ['    Project Name:  ', '', conf.options['project_name']],
#         ['    Project Version:  ', '0.01', conf.options['project_version']],
#         ['    Project Description:  ', '', conf.options['project_description']],
#         ['    Author Name:  ', '', conf.options['author_name']],
#         ['    Github Username:  ', '', conf.options['github_username']],
#         ['    License Type:   ', 'mit', conf.options['license']],
#         ['    Minimal Installation? (Y/N):   ', '',
#          conf.options['default']],

#         ['    Custom Config Location [Leave empty if not present]:  ',
#             'config.yaml', conf.options['config_location']],
#         ['    Github Email:  ', '', conf.options['author_email']],
#         ['    Git Repository (Y/n): ', '', conf.options['files']['git']],
#         ['    Contributing.md (Y/n): ', '',
#          conf.options['files']['contributing']],
#         ['    Setup.cfg (Y/n): ', '', conf.options['files']['setup_cfg']],
#         ['    Tests folder (Y/n): ', 'yes', conf.options['files']['tests']],
#         ['    Conda feed stock (Y/n): ', '', conf.options['files']['conda']],
#         ['    Shields? (Y/n)  T: ', 'YES', emojis],

#         ['                    |-license  (Y/n): ',
#          'mit', conf.options['shields']['base']],

#         ['                    |-Builds   (Y/n): ',
#          'appveyor', conf.options['shields']['base'].append('build')],

#         ['                    |-version  (Y/n): ',
#          'pypi', conf.options['shields']['base'].append('version')],

#         ['                    |-Issues   (Y/n): ',
#          'github-issues', conf.options['shields']['base'].append('issue-tracking')],

#         ['                    |-PRs      (Y/n): ',
#          'github-pull-requests', conf.options['shields']['base'].append('issue-tracking')],
#     ]
#     conf.options['default'] = False
#     for question, answer, something in questions_to_ask:
#         answers[question] = str(input_with_prefill(question, answer)).lower()
#         something = answer
#         if [question, answer, something] in questions_to_ask[15:]:
#             pass
#         if question == questions_to_ask[6][0] and answers[question] == 'y':
#             break
#     # print(json.dumps(answers, indent=2))
#     print(json.dumps(conf.options, indent=2))
#     print(
#         '''
#     ______________________________
#     |                            |
#     | Generation was successful  |
#     | -------------------------  |
#     | $ cd repo_name             |
#     | $ python setup.py install  |
#     ------------------------------
# '''
#     )


# questions()
