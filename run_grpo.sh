#!/bin/bash
CURRENT_DIR="$( cd "$( dirname "$0" )" && pwd )"
export PYTHONPATH=$PYTHONPATH:${CURRENT_DIR}/src/
echo "PYTHONPATH: ${PYTHONPATH}"
accelerate launch --config_file accelerate_configs/zero3.yaml src/open_r1/grpo.py --config examples/Qwen0.5B-Instruct-grpo.yaml