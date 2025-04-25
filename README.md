# CharacterBench: Benchmarking Character Customization of Large Language Models

<p align="center">
   🤗 <a href="https://huggingface.co/thu-coai/CharacterJudge" target="_blank">Hugging Face</a> • ⏬ <a href="#eval_data" target="_blank">Data</a> •   📃 <a href="https://arxiv.org/pdf/2412.11912" target="_blank">Paper</a>
</p>

## Data Preparation

- Using the provided test set, instruct the evaluated large language model to play specific characters for generating responses.

- These generated responses will then be evaluated by CharacterJudge in subsequent evaluations.

- **Ensure that you update the model (`YOUR_MODEL_NAME`) and the path (`data_path` and `output_path`) as necessary.**


```shell
python process.py --data_path eval_data/raw_data --output_path eval_data/response_data --model_name YOUR_MODEL_NAME
```

- Convert the generated data into the input format of CharacterJudge.

```shell
cd construct_prompts
python process_wo_context_zh_all.py --data_path ../eval_data/response_data --output_path ../eval_data/evaluation_data_zh --model_name YOUR_MODEL_NAME
python process_wo_context_en_all.py --data_path ../eval_data/response_data --output_path ../eval_data/evaluation_data_en --model_name YOUR_MODEL_NAME
```

## Evaluation

- Run CharacterJudge to generate evaluation results.

```shell
bash run_zh.sh YOUR_MODEL_NAME
bash run_en.sh YOUR_MODEL_NAME
```

## Citation

If you find our work useful for your research, please kindly cite our paper as follows:

```
@article{characterbench,
  title={CharacterBench: Benchmarking Character Customization of Large Language Models},
  author={Jinfeng Zhou, Yongkang Huang, Bosi Wen, Guanqun Bi, Yuxuan Chen, Pei Ke, Zhuang Chen, Xiyao Xiao, Libiao Peng, Kuntian Tang, Rongsheng Zhang, Le Zhang, Tangjie Lv, Zhipeng Hu, Hongning Wang, Minlie Huang},
  journal={AAAI},
  year={2025}
}
```


## Contact Us

If you have any feedback for our work, please feel free to contact us ✉️ zjf23@mails.tsinghua.edu.cn.

