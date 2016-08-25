from setuptools import setup

setup(
    name='ted-tools',
    version='0.2.0a1',
    description='Scripts to monitor your car using the OBD-II connector and an ELM327 adapter',  # NOQA
    author='Auke Willem Oosterhoff',
    author_email='auke@orangetux.nl',
    url='https://github.com/orangetux/ted',
    packages=[],
    install_requires=[
        'obd==0.6.1',
        'pyfiglet==0.7.5',
        'pyserial==3.1.1',
        'pyzmq==14.3.1',
    ],
    scripts=[
        'scripts/ted',
        'scripts/tscreen',
    ],
    license='MPL',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)
