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
    # ci = None  # ?('Tox','Jenkins','TravisCI')

    # readme = 'markdown'
    # license = 'unilicense'
    # gitignore = True
    # contributing = False
    # interactive = False

    # ! Project Details
    project_name = 'PrjectGetGPA'
    project_version = '0.01alpha'
    project_description = 'Working project has the following descriptions. I dont even remember                                       how to write fast of this things. I have gotten so function slow.'
    author_name = 'Ratin Kumar'
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
    setup.cfg = False
    docker = False

    # ! Shields Related Options
    extra = {
        build: 'appveyor'
        codecov: 'codecov'
        analysis: 'gtihub-lanugage-count'
        chat: 'discord'
        dependencies: None
        size: 'github-repo-size'
        downloads: None
        funding: None
        issues: None
        license: 'github'
        rating: None
        social: None
        version: 'pypi'
        platform: None
        monitoring: None
        activity: None
        other: None
        custom_shield: False
    }
