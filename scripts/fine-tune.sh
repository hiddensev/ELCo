#!/bin/bash

# Please define your own path here
huggingface_path=/workspace/ELCo/huggingface

for model_name in bert-base
do
    for seed in 43
    do
        CUDA_VISIBLE_DEVICES=0 python scripts/emote.py --finetune 1 --model_name $model_name --portion 1 --seed $seed --hfpath $huggingface_path
    done
done
