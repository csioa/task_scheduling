#!/usr/bin/env bash

export AIRFLOW_HOME=$(pwd)

airflow scheduler -D;

airflow webserver -D;