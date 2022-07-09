# FAQ


:::{dropdown} **Can I export the generated model?**
:margin: 2 2 0 0
:color: light

It is currently not possible to export the model that Label Sleuth generates. However, this is something that we plan to add in the near future. In the mean-time, you can export the labeled data that you created in Label Sleuth. This can be done by clicking on the "Download Data" button on the left side of the screen. 

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
