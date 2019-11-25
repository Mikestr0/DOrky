from setuptools import setup, find_packages

setup(name='DOrky',
      version='1.0',
      description='Automated Google dorking',
      long_description='A utility for performing automated Google dorking with simple HTML output',
      classifiers=[
        'Development Status :: 3 - Alpha',
        'GNU General Public License v3.0',
        'Programming Language :: Python :: 3.x',
      ],
      keywords='google dork dorking dorky DOrky',
      url='https://github.com/Mikestr0/DOrky',
      author='Mike Carthy - Mikestro',
      author_email='mikestro@wearehackerone.com',
      license='GNU',
      packages=find_packages(),
      install_requires=[
          'argparse',
          'termcolor',
          'selenium',
          'tabulate',
          'google-api-python-client'
      ],
      include_package_data=True,
      zip_safe=False)
     
