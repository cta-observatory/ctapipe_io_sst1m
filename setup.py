from setuptools import setup, find_packages

setup(
    name='ctapipe_io_sst1m',
    packages=find_packages(),
    version='0.1',
    description=(
        'a ctapipe io plugin providing a camera specific EventSource'
    ),
    install_requires=[
        'astropy',   # for is_compatible
        'ctapipe',
        'protozfits',
    ],
    tests_require=['pytest'],
    author='Dominik Neise',
    author_email='neised@phys.ethz.ch',
    license='MIT',
)
