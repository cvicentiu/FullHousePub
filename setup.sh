#!/bin/bash
echo Setting up virtual environment
virtualenv -p python2.7 sandbox
echo Installing dependancies
sandbox/bin/pip install -r requirements-pip
