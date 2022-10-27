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

:::{dropdown} **Can I build a multiclass model?** 
:margin: 2 2 0 0
:color: light

At the moment the system does not support a multiclass scenario. Label Sleuth is geared towards working with binary classes which reduces the cognitive load on the labeler. However, there is no limit on the amount of binary classes you can build, and you can download the collected labeled data for the different classes, and use it to train a multiclass classifier.

:::

##
### **Have more questions?**

Talk to us on [![Slack](https://img.shields.io/badge/Slack-darkblue?logo=slack&logoColor=white)](https://join.slack.com/t/labelsleuth/shared_invite/zt-1h1exje12-wuSTcktxUVHefZgAZ9bEiQ)