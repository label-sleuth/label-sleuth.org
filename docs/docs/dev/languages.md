# Language support

Currently, Label Sleuth can work with text data in the following languages:
- `ENGLISH` <br /><defvalue>default</defvalue>
- `ITALIAN`
- `ROMANIAN`
- `HEBREW`
- `ARABIC`

To start up the system with your chosen language, use the following command:
   ```text
   python -m label_sleuth.start_label_sleuth --language <YOUR_LANGUAGE>
   ```
   
Note that not every machine learning model is compatible with every language. For model-language compatibility, see [here](model_training.md#model-policies).
