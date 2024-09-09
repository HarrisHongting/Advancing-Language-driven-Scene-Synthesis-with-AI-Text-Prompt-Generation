Advancing Language driven Scene Synthesis with AI Text Prompt Generation

This project is fully based on LSDM project created by @andvg3 

Here is the link of the LSDM repository: [link](https://github.com/andvg3/LSDM.git)

## Introduction
In this project, I used the Groq AI API to overwrite the original PRO-teXt text dataset. Optimised training using the LSDM model.

I recommend you to use native Ubuntu (I used Ubuntu 24.04 LTS) system to run this project. For the All guidance can be found in LSDM repository. The relevant datasets and code files are already included in this repository.

## Some things to note
Before run this project, please make sure that all settings are done that introduced by the LSDM README file. (Such as environment setup and training process)

Changed files is provided in this repository.

Make sure download the [PRO-teXt dataset](https://forms.gle/AutfNYQEF6K9DRYs7) successfully. Follows by the format below:

```
|- data/
    |- protext
         |- mesh_ds
         |- objs
         |- proxd_test
         |- proxd_test_edit
         |- proxd_train
         |- proxd_valid
         |- scenes
    |- supp
         |- proxd_train
         |- proxd_valid
```

The text file batch of AI overwrite is stored in the "data/protext/proxd_train/context_versions/" path by default.

More training commend detail please view [LSDM repository](https://github.com/andvg3/LSDM.git)

After run the groq_prompts.py script, make sure there are some folders generated in the path: data/protext/proxd_train/context_versions.

Then use the following commend to run the project.

```
python -m run.train_sdm \
      --train_data_dir data/protext/proxd_train \
      --valid_data_dir data/protext/proxd_valid \
      --fix_ori \
      --epochs 500 \
      --out_dir training/sdm_batches \
      --experiment sdm
```

Run this to test:

```
python -m run.test_sdm data/protext/proxd_test/ \
      --load_model training/sdm/model_ckpt/best_model_cfd.pt \
      --model_name sdm \
      --fix_ori \
      --test_on_valid_set \
      --output_dir training/sdm/output
```

For the visualisation instructions, please refer to the original repository.
