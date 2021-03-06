""" Wheel Config
"""
from setuptools import setup


def get_readme_md_contents():
    """read the contents of your README file"""
    with open("README.md", encoding="utf-8") as f:
        long_description = f.read()
        return long_description


setup(
    version="0.1.6",
    install_requires=["delegator.py", "python-hosts>=1.0.0", "validators>=0.18.0"],
    entry_points={"console_scripts": ["arp-to-hosts=arp_to_hosts.arp_to_hosts:main"]},
    name="arp-to-hosts",
    url="https://github.com/obradovic/arp-to-hosts",
    author="Zo Obradovic",
    author_email="ping@obradovic.com",
    description="arp-scan to /etc/hosts",
    long_description=get_readme_md_contents(),
    long_description_content_type="text/markdown",
    packages=["arp_to_hosts"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
