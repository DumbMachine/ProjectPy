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
#         ['    Project Name:  ', '', 'project_name'],
#         ['    Project Version:  ', '0.01', 'project_version'],
#         ['    Project Description:  ', '', 'project_description'],
#         ['    Author Name:  ', '', 'author_name'],
#         ['    Github Username:  ', '', 'github_username'],
#         ['    License Type:   ', 'mit', 'license'],
#         ['    Minimal Installation? (Y/N):   ', '',
#          'default'],

#         ['    Custom Config Location [Leave empty if not present]:  ',
#             'config.yaml', 'config_location'],
#         ['    Github Email:  ', '', 'author_email'],
#         ['    Git Repository (Y/n): ', '', 'git'],
#         ['    Contributing.md (Y/n): ', '',
#          'contributing'],
#         ['    Setup.cfg (Y/n): ', '', conf.options['files']['setup_cfg']],
#         ['    Tests folder (Y/n): ', 'yes', conf.options['files']['tests']],
#         ['    Conda feed stock (Y/n): ', '', conf.options['files']['conda']],
#         ['    Shields? (Y/n)  T: ', 'YES', emojis],

#         ['                    |-license  (Y/n): ',
#          'mit', ''],

#         ['                    |-Builds   (Y/n): ',
#          'appveyor', ''],

#         ['                    |-version  (Y/n): ',
#          'pypi', ''],

#         ['                    |-Issues   (Y/n): ',
#          'github-issues', ''],

#         ['                    |-PRs      (Y/n): ',
#          'github-pull-requests', ''],
#     ]
#     conf.options['default'] = False
#     for question, answer, something in questions_to_ask:
#         answers[question] = str(input_with_prefill(question, answer)).lower()
#         # something = answer
#         if [question, answer, something] in questions_to_ask[15:]:
#             conf.options['shields'].append(answers[question])
#         elif question == questions_to_ask[6][0] and answers[question] == 'y':
#             break
#         elif question == questions_to_ask[10][0] or question == questions_to_ask[9][0]:
#             conf.options['files'][something] = answers[question]
#         elif question == questions_to_ask[14][0]:
#             pass
#         else:
#             # try:
#             conf.options[something] = answers[question]
#             # except:
#             # raise Exception(f"{question}")
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
