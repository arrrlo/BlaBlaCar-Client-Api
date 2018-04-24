from setuptools import setup


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='BlaBlaCar API',
    version='0.2.2',

    description='BlaBlaCar Client Api',
    long_description=readme(),
    long_description_content_type='text/markdown',

    url='https://github.com/arrrlo/BlaBlaCar-Client-Api',
    licence='MIT',

    author='Ivan Arar',
    author_email='ivan.arar@gmail.com',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='blablacar, api, trip, distance',

    packages=['blablacarapi'],
    install_requires=[
        'requests ~= 2.11.0',
        'click ~= 6.7',
        'colorama~=0.3'
    ],

    project_urls={
        'Source': 'https://github.com/arrrlo/BlaBlaCar-Client-Api',
    },
)
