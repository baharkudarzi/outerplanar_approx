from setuptools import setup, find_packages

setup(
    name="outerplanar_approx",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "networkx>=2.6"
    ],
    author="Your Name",
    description="7/10-approximation for maximum outerplanar subgraphs (STS algorithm)",
    url="https://github.com/yourusername/outerplanar_approx",
)
