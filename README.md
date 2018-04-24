# AutoDownloadReferences
Automatically download PDFs of a paper's references

Currently only working with DOI papers available at ACM Digital Library.

## Setup

```
pip3 install selenium==3.11.0
```
Also download ```chromedriver``` for your system [from here](https://sites.google.com/a/chromium.org/chromedriver/downloads).

## Usage

```
usage: getreferences.py [-h] doi

Get all the PDFs in a paper's reference

positional arguments:
  doi         tries to find and download all paper's references

optional arguments:
  -h, --help  show this help message and exit
```
