import setuptools

setuptools.setup(
    name="extension_vocos",
    packages=setuptools.find_namespace_packages(),
    version="0.0.1",
    author="rsxdalv",
    description="Vocos is a neural audio codec for high-quality audio compression and reconstruction",
    url="https://github.com/rsxdalv/extension_vocos",
    project_urls={},
    scripts=[],
    install_requires=[
        "vocos==0.1.0",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
