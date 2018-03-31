from setuptools import setup,find_packages

setup(
    name='snakeeater',
    version='0.0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        snakeeater=snakeeater.scripts.snakeater:cli
    ''',
    )
    url='',
    license='MIT',
    author='Eric Robibaro',
    author_email='perlchild@perlchild.org',
    description='Like kitchen, but with more python'
)
