import yaml
import json


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
            ("setup_py", True),
            ("color", True),
            ("requirements", True),
            ("tests", True),
            ("main", True),
            ("contributing", True),
            ("interactive", False),
            ("manifest", False),
            ("setup_cfg", False),
            ("dockerfile", False),
            ("conda", False),
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
    '''
    '''
    # thing = yaml.load(custom, Loader=yaml.Loader)
    thing = yaml.load(open(location), Loader=yaml.Loader)

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
    conf.options['config_location'] = location
    for item in thing.keys():
        print(item)
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
    print('I returned from cutom_reader', json.dumps(conf.options, indent=4))
    return conf


custom_reader('./.config.yaml')
