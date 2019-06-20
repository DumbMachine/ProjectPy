import json
from datetime import datetime
import os
data = json.load(open('.data.json'))


def get_shielder(entity, mode='markdown', style='flat'):
    if style not in ['plastic', 'flat', 'flat-square', 'for-the-badge', 'poput', 'popout-square', 'social']:
        raise ValueError(f"{style} is not Available")
    else:
        if entity not in data.keys():
            raise ValueError(f'This shield {entity} is not in the dict')
        else:
            if mode == 'markdown':
                return f"![{entity}]({data[entity]}?style={style})"
            else:
                return f".. image:: {data[entity]}   :alt: {entity}?style={style}"
    return ""


def customShield(label='label', message='message', color='orange', mode='markdown', name='Custom Shield'):
    '''

    '''
    if mode not in ['markdown', 'md', 'restructuredtext', 'rst']:
        raise NotImplementedError(f'{mode} is not implemented yet.')
    else:
        if mode in ['markdown', 'md']:
            return f"![Custom Shield](https://img.shields.io/badge/{label}-{message}-{color}.svg)"
        else:
            return f".. image:: https://img.shields.io/badge/{label}-{message}-{color}.svg   :alt: Custom Shield"


def header(title=None, content='', style="##", mode='markdown'):
    if mode not in ['markdown', 'rst', 'md', 'restructuredtext']:
        raise ValueError('A very specific bad thing happened.')
    else:
        if mode == 'markdown' or mode == 'md':
            if not title:
                return f"{content}"
            return f"{style} {title}\n{content}"
        else:
            raise NotImplementedError('Will implement rst later.')


def lister(points, style="*", mode='markdown'):
    if mode not in ['markdown', 'rst', 'md', 'restructuredtext']:
        raise ValueError('A very specific bad thing happened.')
    else:
        if mode == 'markdown' or mode == 'md':
            return "\n".join([style + " " + str(point) for point in points])
        else:
            raise NotImplementedError('Will implement rst later.')


def requirements(location):
    text = open(os.path.join(location, 'requirements.txt'),
                'r').read().splitlines()
    return header(title='Requirements', content=lister(text))


def linker(placeholder='placeholder', link='www.reddit.com/r/memes'):
    return f"[{placeholder}]({link})"


def homepage(link):
    return linker(placeholder='🏠 Homepage', link=link)


def contributing():
    return header(
        title='🤝 Contributing',
        content='Contributions, issues and feature requests are welcome!\nCheck the [contributing.md](some.link.com) or [issues](issues.com).')


def license(license='MIT'):
    return header(
        title='📝 License',
        content=f'Copyright © {datetime.now().year}\nThis Project is [{license}](link.to.license.repo) licensed.'
    )


def watermark():
    awesome = 'https://img.shields.io/badge/made--with--%E2%99%A5--by-ProjectPy-blueviolet.svg'
    return f"\n---\n<sub>This README was generated with ❤ by create-python-project </sub>"


def code(language, content):
    return f"```{language}\n{content}\n```"


def generate_README(location, shields):
    '''
    >>> shields = {
            ['discord', 'appveyor']
        }
    '''
    readme = open(os.path.join(location, 'README.md'), 'w+')
    readme.write(header(
        title='REPO_NAME'
    ))
    if shields:
        for shield in shields:
            if shield == 'custom':
                # for count in range(len(shields['base'])):
                # if shields['base'][count] == 'custom':
                readme.write(customShield())
                readme.write(" ")
            else:
                # if
                # if type(shields['entity'][count]) == list:
                #     for enty in shields['entity'][count]:
                #         readme.write(Shields(
                #             base=shields['base'][count], entity=enty).get_shield())
                #         readme.write(" ")
                # else:
                if shield:
                    # readme.write(Shields(
                    # base=shields['base'][count], entity=shields['entity'][count]).get_shield())
                    readme.write(get_shielder(
                        entity=shield))
                    readme.write(" ")

    # readme.write(Shields(base='build', entity='appveyor').get_shield())
    readme.write("\n")
    readme.write(requirements(location=location))
    readme.write("\n")
    readme.write(header(
        title='Installation',
        content=f"{lister(['To Install in Development Mode'])}\n{code('bash', '$ pip setup.py develop')}\n{lister(['To Install in Normal Mode'])}\n{code('bash', '$ pip setup.py install')}\n"
    ))
    readme.write(header(
        title='Run Tests/ Check Installtion',
        content=f"{lister(['Run the following command to test the installtion:'])}\n{code('bash','$ something')}\n{lister(['Run tests with the following:'])}\n{code('bash','$ python run tests')}\n"
    ))
    readme.write(header(
        title='To serve this',
        content=f"Will check from others"
    ))
    readme.write("\n")
    readme.write(contributing())
    readme.write("\n")
    readme.write(license())
    readme.write("\n")
    readme.write(watermark())

    readme.close()
