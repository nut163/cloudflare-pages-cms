from setuptools import setup, find_packages

setup(
    name='cms_application',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'flask',
        'flask_sqlalchemy',
        'flask_migrate',
        'flask_wtf',
        'wtforms',
        'jinja2',
    ],
    entry_points={
        'console_scripts': [
            'cms_application=cms_application.main:main',
        ],
    },
)