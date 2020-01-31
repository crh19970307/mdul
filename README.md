# mdul

[![pypi](https://img.shields.io/pypi/v/mdul.svg?style=flat)](pypi_mdul)
[![Build Status](https://travis-ci.org/crh19970307/mdul.svg?branch=master)](https://travis-ci.org/crh19970307/mdul)
[![license](https://img.shields.io/github/license/crh19970307/mdul.svg)](LICENSE)

It is safe to store images locally when writing markdown but it's not convenient compared to uploading images into cloud. `mdul` is a utility to upload local images in markdown to [sm.ms](https://sm.ms) and convert markdown file correspondingly. It will also convert markdown equation format. 

## Installation

```bash
git clone https://github.com/crh19970307/mdul.git
cd mdul
python setup.py install
```

## Usage

```bash
usage: mdul [-h] [--imgdir IMG_DIR] [--input INPUT_FILE]
            [--output OUTPUT_FILE] [--key KEY]

optional arguments:
  -h, --help            show this help message and exit
  --imgdir IMG_DIR      image folder，note.assets by default
  --input INPUT_FILE    file to be converted, note.md by default
  --output OUTPUT_FILE  output file name,note_upload.md by default
  --key KEY             Secret Token of sm.ms
```

Secret Token of sm.ms can also be specified in `$HOME/.myconfig` file such as:

```bash
[sm.ms]
    put your KEY here
```
