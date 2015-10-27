from os import path
from setuptools import setup, find_packages


base_dir = path.dirname(__file__)
requirements_path = path.join(base_dir, 'requirements.txt')
install_requires = map(str.strip, open(requirements_path).readlines())


setup(
    name='iamport',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    install_requires=install_requires,
    author='lexifdev',
    author_email='lexifdev@lxf.kr',
    url='',
    description='''Python binding for I'mport;(http://www.iamport.kr) korean payment service provider.''',
    license='zlib',
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
