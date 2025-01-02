from setuptools import find_packages, setup

from tele_graph import __version__

setup(
    name="data-view",
    packages=find_packages(exclude=["tests"]),
    version=__version__,
    description="This open-source repository houses the code for a standalone web application designed to create interactive visualizations of telematics data.",
    url="https://github.com/kevintalaue/data-view",
    author="kevin_talaue",
    author_email="kevintalaue@hotmail.com",
)
