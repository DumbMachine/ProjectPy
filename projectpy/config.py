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
    #  * GITHUB/GIT data
    # username = None
    # usermail = None

    #  ! Settings for Template/Repo
    # REPO_NAME = None
    # git = True
    # docker = False
    # color = True
    # requirements = True
    # manifest = None
    # " ci = None  # "?('Tox','Jenkins','TravisCI')

    # readme = 'markdown'
    # license = 'unilicense'
    # gitignore = True
    # contributing = False
    # interactive = False

    # ? Boolean Variables
    default = False

    basic = dict([
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

    full_option = dict([])

    # custom = read from YAML
    # ! Miscellenous options
    # default = True
    config_location = '.'
    display_options = True
    clear_directory = False

    # ! Project Details
    project_name = 'PrjectGetGPA'
    project_version = '0.01alpha'
    project_description = 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'
    author_name = 'Ratin Kumar'
    author_email = 'placeholder.com'
    github_username = 'DumbMachine'

    # ! Repo related options
    license = 'MIT'
    git = True
    color = True
    requirements = True
    readme = 'markdown'
    contributing = True
    interactive = False
    manifest = False
    setup_cfg = False
    dockerfile = False

    # ! Shields Related Options
    shields = {
        "build": 'appveyor',
        "codecov": 'codecov',
        "analysis": 'gtihub-lanugage-count',
        "chat": 'discord',
        "dependencies": None,
        "size": 'github-repo-size',
        "downloads": None,
        "funding": None,
        "issues": None,
        "license": 'github',
        "rating": None,
        "social": None,
        "version": 'pypi',
        "platform": None,
        "monitoring": None,
        "activity": None,
        "other": None,
        "custom_shield": False,
    }

    actions = {
        'default': {
            'files': {
                'license': writer_licence,
                'git': writer_git,
                '# color': True,
                'requirements': writer_requriements,
                'readme': writer_readme,
                'contributing': writer_contributing,
                '# interactive': False,
                'manifest': writer_manifest,
                'setup_cfg': writer_setup_cfg,
                'dockerfile': writer_dockerfile,
                'setup_py': writer_setup_py,
                'gitignore': writer_gitignore,
                'tests': writer_tests,
                'main': writer_main,
            }
        }
    }

    # actions = dict([

    #     ('basic', dict([
    #         # ! Miscellenous options
    #         ("default", True),
    #         ("config_location", '.'),
    #         ("display_options", True),
    #         ("clear_directory", False),

    #         # ! Project Details
    #         ("project_name", 'PrjectGetGPA'),
    #         ("project_version", '0.01alpha'),
    #         ("project_description", 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'),
    #         ("author_name", 'Ratin Kumar'),
    #         ("author_email", 'placeholder.com'),
    #         ("github_username", 'DumbMachine'),

    #         # ! Repo related options
    #         ("license", writer_licence),
    #         ("git", writer_git),
    #         ("requirements", writer_requriements),
    #         ("readme", writer_readme),
    #         ("contributing", writer_contributing),
    #         ("manifest", writer_manifest),
    #         ("setup_cfg", writer_setup_cfg),
    #         ("setup_py", writer_setup_py),
    #         ("dockerfile", writer_dockerfile),
    #     ]))
    # ])

    #     # ! Miscellenous options
    #     # default: True,
    #     config_location: "Use this in writer",
    #     # display_options: True,
    #     # clear_directory: False,

    #     # # ! Project Details
    #     # project_name: 'PrjectGetGPA',
    #     # project_version: '0.01alpha',
    #     # project_description: 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.',
    #     # author_name: 'Ratin Kumar',
    #     # author_email: "placeholder.com",
    #     # github_username: 'DumbMachine',

    #     # ! Repo related options
    #     license: writer_licence,
    #     git: writer_git,
    #     # color: True,
    #     requirements: writer_requriements,
    #     readme: writer_readme,
    #     contributing: writer_contributing,
    #     # interactive: False,
    #     manifest: writer_manifest,
    #     setup_cfg: writer_setup_cfg,
    #     dockerfile: writer_dockerfile,
    #     setup_py: writer_setup_py,
    #     gitignore: writer_gitignore,

    #     # # ! Shields Related Options
    #     # shields: {
    #     #     "build": 'appveyor',
    #     #     "codecov": 'codecov',
    #     #     "analysis": 'gtihub-lanugage-count',
    #     #     "chat": 'discord',
    #     #     "dependencies": None,
    #     #     "size": 'github-repo-size',
    #     #     "downloads": None,
    #     #     "funding": None,
    #     #     "issues": None,
    #     #     "license": 'github',
    #     #     "rating": None,
    #     #     "social": None,
    #     #     "version": 'pypi',
    #     #     "platform": None,
    #     #     "monitoring": None,
    #     #     "activity": None,
    #     #     "other": None,
    #     #     "custom_shield": False
    #     # }
    # }
