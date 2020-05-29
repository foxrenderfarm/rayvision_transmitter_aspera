"""Describe our module distribution to Distutils."""

# Import third-party modules
from setuptools import find_packages
from setuptools import setup


def parse_requirements(filename):
    with open(filename, "r") as f:
        for line in f:
            yield line.strip()


setup(
    name="rayvision_transmitter_aspera",
    author="Shenzhen Rayvision Technology Co., Ltd",
    author_email="developer@rayvision.com",
    version="1.1.2",
    url="",
    package_dir={"": "."},
    packages=find_packages("."),
    description=("Aspera transfer tool, including window and centos versions"),
    entry_points={},
    package_data={
        'rayvision_transmitter_aspera': ["./rayvision_transmitter_win/*", "./rayvision_transmitter_win/*/*",
                                         "./rayvision_transmitter_win/*/*/*",
                                         "./rayvision_transmitter_centos/*/*", "./rayvision_transmitter_centos/*"],
    },
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
    ],
    # use_scm_version=True,
    setup_requires=["setuptools_scm"],
)
