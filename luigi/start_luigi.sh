#!/usr/bin/env bash

source luigienv/bin/activate

# Starting the luigid server in the background
luigid --background --pidfile pidfile --logdir log_dir/ --state-path statefile

deactivate