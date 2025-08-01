from setuptools import setup, find_packages

setup(
    name="ft_package",
    version="0.0.1",
    author="eagle",
    author_email="eagle@42.fr",
    description="A sample test package",
    license="MIT",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/eagle/ft_package",
    packages=find_packages(),
    python_requires=">=3.6",
)
