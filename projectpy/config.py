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
        ("license", writer_licence),
        ("git", writer_git),
        ("requirements", writer_requriements),
        ("readme", writer_readme),
        ("contributing", writer_contributing),
        ("manifest", writer_manifest),
        ("setup_cfg", writer_setup_cfg),
        ("setup_py", writer_setup_py),
        ("dockerfile", writer_dockerfile),
        ('gitignore', writer_gitignore),
        ('tests', writer_tests),
        ('main', writer_main),
    ])

# # ? Boolean Variables
# default = False

# basic = dict([
#     # ! Miscellenous options
#     ("default", True),
#     ("config_location", '.'),
#     ("display_options", True),
#     ("clear_directory", False),

#     # ! Project Details
#     ("project_name", 'PrjectGetGPA'),
#     ("project_version", '0.01alpha'),
#     ("project_description", 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'),
#     ("author_name", 'Ratin Kumar'),
#     ("author_email", 'placeholder.com'),
#     ("github_username", 'DumbMachine'),
#     ("license", 'MIT'),

#     # ! Repo related options
#     ('files', dict([
#         ("license", 'MIT'),
#         ("git", True),
#         ("color", True),
#         ("requirements", True),
#         ("tests", True),
#         ("main", True),
#         ("contributing", True),
#         ("interactive", False),
#         ("manifest", False),
#         ("setup_cfg", False),
#         ("setup_py", True),
#         ("dockerfile", False),
#         ("readme", 'markdown'),
#     ])),

#     # ! Shields
#     ('shields', dict([
#         ("base", ['chat', 'build', 'custom', 'license']),
#         ("entity", ['discord', 'appveyor', 'custom', 'github']),
#     ]))
# ])

# all = dict([
#     # ! Miscellenous options
#     ("default", True),
#     ("config_location", '.'),
#     ("display_options", True),
#     ("clear_directory", False),

#     # ! Project Details
#     ("project_name", 'PrjectGetGPA'),
#     ("project_version", '0.01alpha'),
#     ("project_description", 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'),
#     ("author_name", 'Ratin Kumar'),
#     ("author_email", 'placeholder.com'),
#     ("github_username", 'DumbMachine'),
#     ("license", 'MIT'),

#     # ! Repo related options
#     ('files', dict([
#         ("license", 'MIT'),
#         ("git", True),
#         ("color", True),
#         ("requirements", True),
#         ("tests", True),
#         ("main", True),
#         ("contributing", True),
#         ("interactive", False),
#         ("manifest", False),
#         ("setup_cfg", False),
#         ("setup_py", True),
#         ("dockerfile", False),
#         ("readme", 'markdown'),
#     ])),

#     # ! Shields
#     ('shields', dict([
#         ("base", []),
#         ("entity", []),
#     ]))
# ])

# full_option = dict([
#     # ! Miscellenous options
#     ("default", True),
#     ("config_location", '.'),
#     ("display_options", True),
#     ("clear_directory", False),

#     # ! Project Details
#     ("project_name", 'PrjectGetGPA'),
#     ("project_version", '0.01alpha'),
#     ("project_description", 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'),
#     ("author_name", 'Ratin Kumar'),
#     ("author_email", 'placeholder.com'),
#     ("github_username", 'DumbMachine'),
#     ("license", 'MIT'),

#     # ! Repo related options
#     ('files', dict([
#         ("license", 'MIT'),
#         ("git", True),
#         ("color", True),
#         ("requirements", True),
#         ("tests", True),
#         ("main", True),
#         ("contributing", True),
#         ("interactive", False),
#         ("manifest", False),
#         ("setup_cfg", False),
#         ("setup_py", True),
#         ("dockerfile", False),
#         ("readme", 'markdown'),
#     ])),

#     # ! Shields
#     ('shields', dict([
#         ("base", ['chat', 'build', 'custom', 'license']),
#         ("entity", ['discord', 'appveyor', 'custom', 'github']),
#     ]))
# ])

# # custom = read from YAML
# # ! Miscellenous options
# # default = True
# config_location = '.'
# display_options = True
# clear_directory = False

# # ! Project Details
# project_name = 'PrjectGetGPA'
# project_version = '0.01alpha'
# project_description = 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'
# author_name = 'Ratin Kumar'
# author_email = 'placeholder.com'
# github_username = 'DumbMachine'

# # ! Repo related options
# license = 'MIT'
# git = True
# color = True
# requirements = True
# readme = 'markdown'
# contributing = True
# interactive = False
# manifest = False
# setup_cfg = False
# dockerfile = False

# # ! Shields Related Options
# shields = {
#     "build": 'appveyor',
#     "codecov": 'codecov',
#     "analysis": 'gtihub-lanugage-count',
#     "chat": 'discord',
#     "dependencies": None,
#     "size": 'github-repo-size',
#     "downloads": None,
#     "funding": None,
#     "issues": None,
#     "license": 'github',
#     "rating": None,
#     "social": None,
#     "version": 'pypi',
#     "platform": None,
#     "monitoring": None,
#     "activity": None,
#     "other": None,
#     "custom_shield": False,
# }

# actions = {
#     'default': {
#         'files': {
#             'license': writer_licence,
#             'git': writer_git,
#             '# color': True,
#             'requirements': writer_requriements,
#             'readme': writer_readme,
#             'contributing': writer_contributing,
#             '# interactive': False,
#             'manifest': writer_manifest,
#             'setup_cfg': writer_setup_cfg,
#             'dockerfile': writer_dockerfile,
#             'setup_py': writer_setup_py,
#             'gitignore': writer_gitignore,
#             'tests': writer_tests,
#             'main': writer_main,
#         }
#     }
# }

# # actions = dict([

# #     ('basic', dict([
# #         # ! Miscellenous options
# #         ("default", True),
# #         ("config_location", '.'),
# #         ("display_options", True),
# #         ("clear_directory", False),

# #         # ! Project Details
# #         ("project_name", 'PrjectGetGPA'),
# #         ("project_version", '0.01alpha'),
# #         ("project_description", 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'),
# #         ("author_name", 'Ratin Kumar'),
# #         ("author_email", 'placeholder.com'),
# #         ("github_username", 'DumbMachine'),

# #         # ! Repo related options
# #         ("license", writer_licence),
# #         ("git", writer_git),
# #         ("requirements", writer_requriements),
# #         ("readme", writer_readme),
# #         ("contributing", writer_contributing),
# #         ("manifest", writer_manifest),
# #         ("setup_cfg", writer_setup_cfg),
# #         ("setup_py", writer_setup_py),
# #         ("dockerfile", writer_dockerfile),
# #     ]))
# # ])

# #     # ! Miscellenous options
# #     # default: True,
# #     config_location: "Use this in writer",
# #     # display_options: True,
# #     # clear_directory: False,

# #     # # ! Project Details
# #     # project_name: 'PrjectGetGPA',
# #     # project_version: '0.01alpha',
# #     # project_description: 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.',
# #     # author_name: 'Ratin Kumar',
# #     # author_email: "placeholder.com",
# #     # github_username: 'DumbMachine',

# #     # ! Repo related options
# #     license: writer_licence,
# #     git: writer_git,
# #     # color: True,
# #     requirements: writer_requriements,
# #     readme: writer_readme,
# #     contributing: writer_contributing,
# #     # interactive: False,
# #     manifest: writer_manifest,
# #     setup_cfg: writer_setup_cfg,
# #     dockerfile: writer_dockerfile,
# #     setup_py: writer_setup_py,
# #     gitignore: writer_gitignore,

# #     # # ! Shields Related Options
# #     # shields: {
# #     #     "build": 'appveyor',
# #     #     "codecov": 'codecov',
# #     #     "analysis": 'gtihub-lanugage-count',
# #     #     "chat": 'discord',
# #     #     "dependencies": None,
# #     #     "size": 'github-repo-size',
# #     #     "downloads": None,
# #     #     "funding": None,
# #     #     "issues": None,
# #     #     "license": 'github',
# #     #     "rating": None,
# #     #     "social": None,
# #     #     "version": 'pypi',
# #     #     "platform": None,
# #     #     "monitoring": None,
# #     #     "activity": None,
# #     #     "other": None,
# #     #     "custom_shield": False
# #     # }
# # }
