from setuptools import setup, Extension
from rena.version import __version__

description = "rena is a command for easily renaaming directories and files.",

setup(
    name = 'rena',
    version = __version__,
    description = description,
    long_description = description,
    keywords = 'filesystem bash rename mv move',
    author = 'Xiaoyong Guo',
    author_email = 'guo.xiaoyong@gmail.com',
    url = 'https://github.com/guoxiaoyong/rena',
    packages = ['rena'],
    package_dir = {"rena": "rena"},
    entry_points = {
        'console_scripts': [
            'rena = rena:main',
        ],
    },
)
