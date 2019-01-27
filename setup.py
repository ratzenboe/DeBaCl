from setuptools import setup, find_packages

setup(
    name='debacl',
    version='1.101',
    description='DEnsity-BAsed CLustering Updated for Python 3',
    url='https://github.com/CoAxLab/DeBaCl',
    author='Brian Kent',
    author_email='bpkent@gmail.com',
    license='BSD',
    classifiers=[
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization'
        ],
    packages=find_packages(),
    install_requires=["prettytable", "networkx"]
)
