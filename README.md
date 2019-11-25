# DOrky
DOrky is a simple and efficient command-line utility for the automation of Google dorking. 

## Getting Started
<p align="justify">In order to install DOrky onto your machine you will need to meet the prerequisites outlined below and follow the installation instructions for your environment. DOrky has only been tested using Python 3.7 on Kali Linux. </p>

#### Prerequisites
In order to use DOrky you will need to have or obtain the following: -
```
1. Google Cloud API key - https://cloud.google.com/console/google/
2. Google Custom Search Engine (CSE) ID - https://cse.google.com/cse/all
3. Google Chrome web browser (required for selenium / web screenshot integration)
```
These are required in order for calls to the Google Search API to function.

#### Installation
1. Run `git clone https://github.com/Mikestr0/DOrky.git`
2. Change into the project directory.
3. Run `python3 setup.py install` to install the required packages / dependencies. 

#### Dependencies

- tabulate
- termcolor
- selenium
- google-api-python-client

#### Usage

Dorky can be ran from the command line using the following syntax. Simply specify the domain you would like to target along with a file containing your search strings / Google dorks. DOrky will perform a search query for each line in the file against your target domain and output the results to a HTML file along with a screenshot of each web page.
```
usage: dorky.py [-h] -d D [-r R]

Example: dorky.py -d google.com -r dorks.txt

optional arguments:
  -h, --help  show this help message and exit
  -d D        Use this argument to specify your domain
  -r R        Use this argument to specify your dorks file
```

## Screenshots
![Alt text](https://i.ibb.co/CVWSbvW/dorky3.png "DOrky Screenshot")

## Contributing
Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.

## Authors
Mike Carthy (Mikestro) - https://www.linkedin.com/in/mikecarthy/ 

## License
This project is licensed under the GNU General Public License v3.0 - see the LICENSE.md file for details.

## Acknowledgments
A massive thank you to Nedbat over at #Python / Freenode for his help in debugging some of my code.
