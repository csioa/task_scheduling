#!/usr/bin/env bash

kill -9 `cat airflow-scheduler.pid`

rm airflow-scheduler*

kill -9 `cat airflow-webserver.pid`

rm airflow-webserver*