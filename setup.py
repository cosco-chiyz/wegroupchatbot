# coding:utf-8
from setuptools import setup, find_packages
from codecs import open
from os import path

__version__ = '0.0.5'

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# get the dependencies and installs
with open(path.join(here, 'requirements.txt'), encoding='utf-8') as f:
    all_reqs = f.read().split('\n')

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip().replace('git+', '') for x in all_reqs if x.startswith('git+')]

setup(
    name='wegroupchatBot',
    version=__version__,
    description='group chat WeGroupChatBot for Wechat of enterprise 企业微信群机器人接口',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/cosco-chiyz/wegroupchatbot',
    download_url='https://github.com/bonashen/wegroupchatBot/tarball/' + __version__,
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Programming Language :: Python :: 3',
    ],
    keywords='wechat,groupchat,WeGroupChatBot',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='shen yang',
    install_requires=install_requires,
    dependency_links=dependency_links,
    author_email='cnshenyang@outlook.com'
)
