import setuptools

with open("README.md") as fp:
    long_description = fp.read()

setuptools.setup(
    name="tasks_service",
    version="0.1.0",
    description="A serverless CRUD API for managing tasks",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Your Name",
    package_dir={"": "tasks_service"},
    packages=setuptools.find_packages(where="tasks_service"),
    install_requires=[
        "aws-cdk-lib>=2.0.0",
        "constructs>=10.0.0",
        "boto3",
    ],
    python_requires=">=3.8",
)
