from setuptools import find_packages, setup

setup(
    name="gh2023",
    author="roostinghawk",
    author_email="roostinghawk@163.com",
    url="https://github.com/roostinghawk/2023",
    license="MIT",
    version="2.3.0",
    description="My repo of my 2023",
    packages=find_packages(),
    include_package_data=True,
    install_requires=["PyGithub", "requests", "pendulum"],
    entry_points={
        "console_scripts": ["gh2023 = github_daily.cli:main"],
    },
)
