import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages()

setuptools.setup(
    name="hashtag_observer",
    version="0.0.0",
    author="littlesnore",
    description="Insert a hashtag and observe the images related",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/lilsnore/twitter_hashtag_observer",
    packages=packages,
    python_requires='>=3.8',
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'hashtag_observer = hashtag_observer.app:run',
        ]},
)