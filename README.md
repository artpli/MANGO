# MANGO

Repository for the paper: *[MANGO: A Benchmark for Evaluating <u>Ma</u>pping and <u>N</u>avi<u>g</u>ati<u>o</u>n Abilities of Large Language Models](https://arxiv.org/abs/2403.19913)*

More details can be found on our [official website](https://mango.ttic.edu).

For questions or issues, please open an [issue on GitHub](https://github.com/Oaklight/mango/issues).

## Abstract

Large language models (LLMs), such as ChatGPT and GPT-4, have shown remarkable performance in various natural language processing tasks. In this paper, we introduce **MANGO**, a benchmark to assess the ability of LLMs to perform text-based mapping and navigation.

MANGO comprises 53 mazes from a suite of text-based games. Each maze is paired with a walkthrough that covers key locations but not all paths. The benchmark involves question-answering tasks where the LLM reads the walkthrough and answers hundreds of mapping and navigation questions, such as:

- *"How should you go to the Attic from West of House?"*
- *"Where would you be if you go north and east from Cellar?"*

While these questions are simple for humans, even the state-of-the-art model GPT-4 struggles with them. Our findings indicate that strong mapping and navigation capabilities are crucial for LLMs to perform downstream tasks, such as playing text-based games.

We host the **leaderboard**, **data**, **code**, and **evaluation** tools for MANGO [here](https://mango.ttic.edu), facilitating future research in this area.

## Setup

To set up the environment for MANGO, follow these steps:

```bash
git clone https://github.com/Oaklight/mango.git
cd mango

conda create -n mango python=3.11 -y
conda activate mango

# For evaluation
pip install -e .

# For evaluation and inference
pip install -e .[infer]
```

## Dataset

Our data is hosted on [Hugging Face](https://huggingface.co/mango-ttic). More information is available [here](https://oaklight.github.io/mgwb/data/).

To download the dataset for the first 70 moves of each game:

```bash
cd mango
wget https://huggingface.co/datasets/mango-ttic/data/resolve/main/data-70steps.tar.zst
zstd -d -c data-70steps.tar.zst | tar -xvf -
rm data-70steps.tar.zst
mv data-70steps data
```

Alternatively, the dataset is available in the `data` folder within this repository.

## Inference

The inference code is located in the `mango/inference/` directory. You can find additional details in the README file in that folder.

To query the `claude-instant-1` model for inference:

```bash
export ANTHROPIC_API_KEY=<YOUR KEY>

python mango/inference/main.py --exp_tag debug --data_folder ./data --save_folder ./results --game_name '905' --task_type 'route_finding' --model_name 'claude-instant-1'
```

## Evaluation

Evaluation can be performed using the script located at `mango/evaluation/scripts/evaluate.py`.

For the required output format for destination-finding evaluation, refer to the following sample:

```
/mango/examples/llm_output_example/claude-instant-1_desti_finding_debug/905/result_sample_id_1f51a779e76851bcc0bd9a9ce26ab9145349ea63f0810d7e5357b46b45c01f82.json
```

For route-finding evaluation, refer to:

```
/mango/examples/llm_output_example/claude-instant-1_route_finding_debug/905/result_sample_id_4ac913314591fb251c6b13678324b508e5cd383638938482322bd02be1718de0.json
```

Make sure the `response` field is a list of dictionaries with the required keys, such as:

```json
[{"location_before": "driveway", "action": "north", "location_after": "living room"}, ...]
```

You can customize the key names in `mango/mango/evaluation/config.py`. For example:

```python
"location_before": "location_before" --> "location_before": "prev_location"
```

### Evaluation Examples

For destination-finding:

```bash
mango-eval --mode df --rst-dir ./examples/llm_output_example/claude-instant-1_desti_finding_debug --map-dir ./data
```

For route-finding:

```bash
mango-eval --mode rf --rst-dir ./examples/llm_output_example/claude-instant-1_route_finding_debug --map-dir ./data
```

## Citation

If you use MANGO in your research, please cite our paper:

```bibtex
@misc{ding2024mango,
      title={MANGO: A Benchmark for Evaluating Mapping and Navigation Abilities of Large Language Models}, 
      author={Peng Ding and Jiading Fang and Peng Li and Kangrui Wang and Xiaochen Zhou and Mo Yu and Jing Li and Matthew R. Walter and Hongyuan Mei},
      year={2024},
      eprint={2403.19913},
      archivePrefix={arXiv},
      primaryClass={cs.CL}
}
```
