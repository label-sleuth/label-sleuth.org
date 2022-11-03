# FAQ


:::{dropdown} **Can I export the generated model?**
:margin: 2 2 0 0
:color: light

Yes! The latest model can be downloaded using the download icon next to the model version indicator. In the downloaded zip file you will find the model itself, as well as a code snippet demonstrating how it can be used within a python application. 

:::

:::{dropdown} **Can multiple users use the system simultaneously?**
:margin: 2 2 0 0
:color: light

Multiple users can use the system simultaneously by working in different workspaces or in different categories within the same workspace. Note that currently all workspaces and categories are visible to all users. Extended multi-user support is an area that we plan to explore in the future.  

:::

:::{dropdown} **Does the system require a GPU?** 
:margin: 2 2 0 0
:color: light

Label Sleuth in its default configuration _does not_ require a GPU, using instead lightweight machine learning models. This ensures that the system can run on low computational resource environments, including laptops or low-power workstations.
   
However, as the system is customizable, one can override the default configuration to use different machine learning models. Depending on the choice of model, a GPU may be required. For a list of models that can be configured and their hardware requirements, refer to the [models](dev/model_training.md#models) documentation.

:::

:::{dropdown} **Can I build a multi-class model?** 
:margin: 2 2 0 0
:color: light

At the moment the system does not natively support building multi-class models. Label Sleuth is geared towards working with one binary model at a time, in order to reduce the cognitive load on the labeler. However, you can use Label Sleuth to build multiple binary models (one per class). The collected labeled data for the different classes can then be downloaded and used to train a multi-class model.

:::

<br />

:::{admonition} Have more questions?

Reach out to us on <span>&nbsp;</span> {{ '[![Slack](https://img.shields.io/badge/Slack-darkgreen?logo=slack&logoColor=white)]({})'.format(slack_link) }}
:::

