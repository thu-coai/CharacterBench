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
@inproceedings{DBLP:conf/aaai/ZhouHWBCK0XPTZZ25,
  author       = {Jinfeng Zhou and
                  Yongkang Huang and
                  Bosi Wen and
                  Guanqun Bi and
                  Yuxuan Chen and
                  Pei Ke and
                  Zhuang Chen and
                  Xiyao Xiao and
                  Libiao Peng and
                  Kuntian Tang and
                  Rongsheng Zhang and
                  Le Zhang and
                  Tangjie Lv and
                  Zhipeng Hu and
                  Hongning Wang and
                  Minlie Huang},
  editor       = {Toby Walsh and
                  Julie Shah and
                  Zico Kolter},
  title        = {CharacterBench: Benchmarking Character Customization of Large Language
                  Models},
  booktitle    = {AAAI-25, Sponsored by the Association for the Advancement of Artificial
                  Intelligence, February 25 - March 4, 2025, Philadelphia, PA, {USA}},
  pages        = {26101--26110},
  publisher    = {{AAAI} Press},
  year         = {2025},
  url          = {https://doi.org/10.1609/aaai.v39i24.34806},
  doi          = {10.1609/AAAI.V39I24.34806},
  timestamp    = {Thu, 17 Apr 2025 17:08:58 +0200},
  biburl       = {https://dblp.org/rec/conf/aaai/ZhouHWBCK0XPTZZ25.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```


## Contact Us

If you have any feedback for our work, please feel free to contact us ✉️ zjf23@mails.tsinghua.edu.cn.

