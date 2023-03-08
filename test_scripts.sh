python run_search.py \
    --supernet ofa_mbv3_d234_e346_k357_w1.0 \
    --dataset_path /dataset/ImageNet/Classification \
    --optimization_metrics accuracy_top1 \
    --measurements accuracy_top1 macs params \
    --results_path mbnv3w10_ga_acc.csv \
    --search_tactic evolutionary \
    --num_evals 250 \
    --search_algo ga