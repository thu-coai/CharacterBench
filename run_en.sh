model=$1

output_path=results/results_${model}_en
mkdir -p $output_path
python model_generation_qwen_chat.py  --output_path $output_path/checkpoint-1120 --input_path eval_data/evaluation_data_en
python all_eval.py --result_path $output_path/checkpoint-1120 --output_path $output_path/checkpoint-1120.json