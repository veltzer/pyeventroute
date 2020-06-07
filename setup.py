import setuptools


def get_readme():
    with open('README.rst') as f:
        return f.read()


setuptools.setup(
    # the first three fields are a must according to the documentation
    name="pyeventroute",
    version="0.0.3",
    packages=[
        'pyeventroute',
    ],
    # from here all is optional
    description="pyeventroute helps you route events to loggers or to any other place",
    long_description=get_readme(),
    long_description_content_type="text/x-rst",
    author="Mark Veltzer",
    author_email="mark.veltzer@gmail.com",
    maintainer="Mark Veltzer",
    maintainer_email="mark.veltzer@gmail.com",
    keywords=[
        'event',
        'logging',
    ],
    url="https://veltzer.github.io/pyeventroute",
    download_url="https://github.com/veltzer/pyeventroute",
    # license="MIT",
    platforms=[
        'python3',
    ],
    install_requires=[
        'pytconf',
    ],
    extras_require={
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
    ],
    data_files=[
    ],
    entry_points={"console_scripts": [
    ]},
    python_requires=">=3.5",
)
