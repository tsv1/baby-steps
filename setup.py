from setuptools import find_packages, setup


setup(
    name="baby-steps",
    version="1.2.1",
    description="Readability Matters",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Nikita Tsvetkov",
    author_email="nikitanovosibirsk@yandex.com",
    python_requires=">=3.6",
    url="https://github.com/nikitanovosibirsk/baby-steps",
    license="Apache-2.0",
    packages=find_packages(exclude=("tests",)),
    package_data={"baby_steps": ["py.typed"]},
    install_requires=[],
    tests_require=[],
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
