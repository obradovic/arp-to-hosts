""" Wheel Config
"""
import setuptools

with open("README.md", "r") as readme:
    long_description = readme.read()

setuptools.setup(
    name="arp-to-hosts",
    version="0.1.1",
    scripts=["arp-to-hosts"],
    author="Zo Obradovic",
    author_email="ping@obradovic.com",
    description="arp-scan to /etc/hosts",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/obradovic/arp-to-hosts",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
