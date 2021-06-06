from setuptools import find_packages, setup


setup(
    name="baby-steps",
    version="0.0.1",
    description="Readability Matters",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nikita Tsvetkov",
    author_email="nikitanovosibirsk@yandex.com",
    python_requires=">=3.6",
    url="https://github.com/nikitanovosibirsk/baby-steps",
    license="Apache-2.0",
    packages=find_packages(exclude=("tests",)),
    install_requires=[],
    tests_require=[],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
