from setuptools import setup, find_packages

setup(
    name='zUMI_converter',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'anndata',
        'mudata',
        'scipy',
        'rpy2'
    ],
    entry_points={
        'console_scripts': [
            'zUMI_converter = zUMI_converter.zUMI_converter:main',
        ],
    },
    author='Prach Techameena',
    author_email='prach.techa@gmail.com',
    description='A package for converting zUMI files',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/PrachTecha/zUMI_converter',
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
