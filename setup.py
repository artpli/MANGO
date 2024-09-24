# coding:utf-8

from setuptools import find_packages, setup

def parse_requirements(filename):
    """Return requirements from a requirements file."""
    with open(filename, "r", encoding="utf-8") as file:
        # Filter out empty lines or comments
        return [line.strip() for line in file if line.strip() and not line.startswith('#')]

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Parse the requirements from the respective files
eval_requirement = parse_requirements("eval_requirements.txt")
infer_requirement = parse_requirements("infer_requirements.txt")

setup(
    name="mango-ttic",
    version="1.0",
    author="ttic",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Oaklight/mango/tree/camera_ready",
    packages=find_packages(),
    python_requires=">=3.11",
    install_requires=eval_requirement,  # Default installation from eval_requirements.txt
    extras_require={
        'infer': infer_requirement,  # Optional installation from infer_requirements.txt
    },
    entry_points={
        'console_scripts': [
            'mango-eval=mango.cli:main',
        ],
    },
)
