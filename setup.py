from setuptools import find_packages,setup

setup(
    name='mcqgenrator',
    version='0.0.1',
    author='Mukesh Sethi',
    author_email='sethi.mukeshjain@gmail.com',
    install_requires=["openai","langchain-openai","streamlit","python-dotenv","PyPDF2"],
    packages=find_packages()
)