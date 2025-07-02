from setuptools import setup, find_packages

setup(
    name='terminal_colors',
    version='0.1.0',
    package_dir={'': 'src'},  # Tells setuptools to look for packages/folders in the 'src' directory
    packages=find_packages(where='src'), # Tells find_packages() to search *within* 'src'

    author='Brandon Landry',
    author_email='githotpocket@gmail.com',
    description='A simple Python package for printing colored text to the terminal.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/hotpocket/terminal_colors', # Optional: Your project's URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ],
    python_requires='>=3.6',
    extras_require={
        'dev': [
            'pytest>=6.0',
         ],
    },
)