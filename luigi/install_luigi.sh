#!/usr/bin/env bash

virtualenv luigienv

source luigienv/bin/activate

pip install luigi

deactivate