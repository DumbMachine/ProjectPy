# Using the CLI

The CLI is very easy to use and is highly flexible.

Users can make a bare-bones package, which comes with things just enough to install it.

Or they can choose the Recommended Default of the CLI, which provides the Package Structure and also minimal CI support, with configs and shields in the read-me.

Or they can make their own config.yaml file\( [Look here for an example](https://github.com/DumbMachine/ProjectPy) \), for a customizable experience.

Now lets get into some examples:

### Bare-Bones Packages:

Just like the heading we will name this package BareBones. To create this package all we have to do is run the following command in the directory where we want to initialize the package:

```bash
$ projectpy -n BareBones
```

This will create our package.

### Recommended Installation:

This is the recommended way of using the CLI. This will provide just enough options to the repo to keep it modern and functional. We will be using the CLI interactively here.

```bash
$ projectpy --interactive # or projectpy -i
----------------------------------------------------------------------------------------
PROJECTPY: A Python CLI to create packages
    ├── Project Name:  KermitMemes
    ├── Project Version:  69.420
    ├── Project Description:  My Python Package for using deep learning to create Kermit Memes
    ├── Author Name:  Keanu Reves
    ├── Github Username:  BREATH_TAKING_BOI
    ├── License Type:   mit
    ├── Minimal Installation? (Y/N):   N
    ├── Custom Config Location [Leave empty if not present]:  config.yaml
    ├── Github Email:  github@github.com
    ├── readme: markdown
    ├── Git Repository (Y/n): Y
    ├── Contributing.md (Y/n): Y
    ├── Setup.cfg (Y/n): Y
    ├── Tests folder (Y/n): yes
    ├── Conda feed stock (Y/n): N
    ├── Shields? (Y/n)  T: YES
                    ├── license  (Y/n): mit
                    ├── Builds   (Y/n): appveyor
                    ├── version  (Y/n): pypi
                    ├── Issues   (Y/n): github-issues
                    ├── PRs      (Y/n): github-pull-requests

# Clear the before screen.
Creating KermitMemes with the following config:

project_name: KermitMemes
project_version: 69.42
project_description: "My Python Package for using deep learning to create Kermit Memes"
author_name: "Keanu Reves"
github_username: "BREATH_TAKING_BOI"
github_email: "github@github.com"

license: "mit"
git: True
color: True
requirements: True
readme: "markdown"
contributing.md: True
setup.cfg: True
interactive: False

shields:
  build: "appveyor"
  version: "pypi"
  Issues: "github-issues"
  PRs: "github-pull-requests"
  
🌟 Done in 3 seconds.
✅ Success created KermitMemes in ~/KermitMemes

    ______________________________
    |                            |
    | Generation was successful  |
    | -------------------------  |
    | $ cd KermitMemes           |
    | $ python setup.py install  |
    ------------------------------
    
👋 bai bai    

```

### Using config.yaml:

For those who prefer customization, you can use config.yaml file to provide you inputs. Below is an example of a config file:

```yaml
project_name: KermitMemes
project_version: 69.42
project_description: "My Python Package for using deep learning to create Kermit Memes"
author_name: "Keanu Reves"
github_username: "BREATH_TAKING_BOI"
github_email: "github@github.com"

license: "mit"
git: True
color: True
requirements: True
readme: "markdown"
contributing.md: True
setup.cfg: True
interactive: False
conda-feedstock: False

shields: ['appveyor', 'circleci', 'docker-build-status', 'pypi', 'pypi--downloads']
  
```

Now to use the above config.yaml file, call the cli with the following command:

```bash
$ projectpy -c config.yaml #make sure that your in the same directory as the config
```

Your package will be ready in no time.



