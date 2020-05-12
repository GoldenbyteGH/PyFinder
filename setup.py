from distutils.core import setup

setup(
    name= 'pyfinder',
    version='0.5',
    description= ' Look for files and text inside files',
    long_description= open('README').read(),
    py_modules= ['pyfinder'],
    author= 'Giovanni C. Oberti',    # Tratto da "Python Gioda completa" di Marco Buttu
    author_email= 'giovanni.oberti@goldenbyte.it',
    license='BSD',
    keywords= ' python generators distutils',
    scripts= ['scripts/pyfinder'],
    platforms= 'all',
    classifiers= [
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'Licence :: OSI Approved :: BSD Licence',
        'Operating System :: OS Indipendent',
        'Programming Language :: Python :: 3.3',
        'Topic :: Documentation',
        'Topic :: Education :: Testing',
        'Topic :: Text Processing :: Filters',
        'Topic :: Utilities'
    ]
)