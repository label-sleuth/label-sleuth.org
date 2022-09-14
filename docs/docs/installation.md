---
layout: home
title: Installation 
---

# Installation
Label Sleuth can run on Windows, MacOS and Linux.<br>
The minimum requirements are 2 cores and 4GB RAM. For improved performance, it is recommended to use 8 cores and 16GB RAM, particularly when working with large datasets.<br>
Some models may have special hardware requirements to perform as expected, see [models](https://www.label-sleuth.org/docs/dev/model_training.html#models).  

::::{tab-set}

:::{tab-item} For users

Recommended procedure to install Label Sleuth:

1. **Install Anaconda**

   Anaconda will allow you to create a separate Python environment for Label Sleuth. This is important as Label Sleuth currently only supports Python 3.8 (other versions may cause issues). Download and install Anaconda from its official web-site:

   [https://www.anaconda.com/](https://www.anaconda.com/)  

2. **Activate Environment**

   Open a new terminal or restart it if it is already open.

   In the new terminal, create a Python environment for Label Sleuth: 

   ```text
   conda create --yes -n label-sleuth python=3.8
   ```

   Then, activate the new environment:

   ```text
   conda activate label-sleuth
   ```
3. **Install Label Sleuth**

   Install Label Sleuth by running the following command:

   ```text
   pip install label-sleuth
   ```

4. **Fire it all up**

   Start Label Sleuth:

   ```text
   python -m label_sleuth.start_label_sleuth --load_sample_corpus wiki_animals_2000_pages
   ```
   
   This command also pre-loads a collection of Wikipedia documents that will be used in the tutorial below.
   
   Access Label Sleuth on your browser by navigating to the following page:

   [http://localhost:8000/](http://localhost:8000/)

5. **Follow tutorial** (Recommended)

   Now that you have installed Label Sleuth, we strongly recommend following our step-by-step tutorial to get acquainted with the system.

   [View tutorial](tutorial.md)

:::

:::{tab-item} For developers
1. **Install Label Sleuth**

   If you wish to contribute code to the project, follow the installation instructions on [GitHub](https://github.com/label-sleuth/label-sleuth/#setting-up-a-development-environment).

2. **Follow tutorial** (Recommended)

   Once you have installed Label Sleuth, we strongly recommend following our step-by-step tutorial to get acquainted with the system.

   [View tutorial](tutorial.md)
:::

::::

:::{note}
**Changing the project directory and port**

When starting up Label Sleuth, the project directory and port can be customized by appending to the startup command `python -m label_sleuth.start_label_sleuth` the following flags:
- ```--output_path <your_path>```:
   - Set location of project files to ```<your_path>``` (default is ```<home_directory>/label-sleuth```)
- ```--port <port_number>```:
   - Set port to ```<port_number>``` (default is 8000)
- ```--host <ip_or_name>```:
   - Set host to ```<ip_or_name>``` (default is localhost, use 0.0.0.0 to expose the service to external communication)
:::
