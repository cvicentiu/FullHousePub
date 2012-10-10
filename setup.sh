#!/bin/bash
echo Setting up virtual environment
virtualenv -p python2.7 sandbox
echo Installing dependancies
pip install -r requirements-pip
