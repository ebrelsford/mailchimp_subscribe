from setuptools import setup, find_packages
import os

import mailchimp_subscribe


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 3',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
]

setup(
    author='Eric Brelsford',
    author_email='ebrelsford@gmail.com',
    name='mailchimp_subscribe',
    version=mailchimp_subscribe.__version__,
    description=("Simple module to subscribe users to a Mailchimp mailing list"),
    long_description=open(os.path.join(os.path.dirname(__file__), 'README.rst')).read(),
    url='https://github.com/ebrelsford/mailchimp_subscribe',
    license='BSD License',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    install_requires=[
        'requests',
    ],
    packages=find_packages(),
    include_package_data=True,
)
