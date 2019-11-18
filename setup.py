from setuptools import setup
setup(
    name='snapshotalyzer-3000',
    version='0.1',
    author='Kris Venchus',
    author_email='k@k.com',
    description="Snapshotalyzer 30000 is a tool to manage AWS snapshots",
    license="GPLv3+",
    packages=['shotty'],
    install_requires=[
        'click',
        'boto3'
    ],
    entry_points='''
        [console_scripts]
        shotty=shotty.shotty:cli
    ''',



)
