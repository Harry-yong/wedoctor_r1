#!/bin/bash
CURRENT_DIR="$( cd "$( dirname "$0" )" && pwd )"
export PYTHONPATH=$PYTHONPATH:${CURRENT_DIR}/src/
echo "PYTHONPATH: ${PYTHONPATH}"
accelerate launch --config_file /root/autodl-fs/code/wedoctor_r1/accelerate_configs/zero3_sft.yaml src/open_r1/sft.py --config /root/autodl-fs/code/wedoctor_r1/examples/Qwen7B-Instruct-grpo.yaml