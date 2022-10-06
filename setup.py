from setuptools import setup, find_packages

setup(
	name='ca_pa',
	version='0.0.1',
	description='Cellranger ATAC Peak Annotation, sourced from Cellranger ATAC v2.1.0',
	url='https://github.com/Teichlab/ca_pa',
	packages=find_packages(),
	install_requires=['six', 'pybedtools'],
	entry_points = {
        "console_scripts": ['ca_pa = ca_pa.ca_pa:main']
    },
	author='Krzysztof Polanski',
	author_email='kp9@sanger.ac.uk',
	license='MIT'
)
