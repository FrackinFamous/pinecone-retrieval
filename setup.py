from setuptools import setup, find_packages

setup(
    name='pinecone-retrieval',
    version='0.1.0',
    packages=find_packages(),
    author='FrackinFamous',
    author_email='frackinfamous@gmail.com',
    url='https://github.com/FrackinFamous/pinecone-retrieval',
    description='A pinecone-retrieval project',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
