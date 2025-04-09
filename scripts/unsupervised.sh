#!/bin/bash

# Please define your own path here
huggingface_path=~/Workspace/hg-cache

for model_name in bert-base
do
    CUDA_VISIBLE_DEVICES=0 python scripts/emote.py --finetune 0 --model_name $model_name --portion 1 --hfpath $huggingface_path
done
