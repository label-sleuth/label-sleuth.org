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


### Adding support for a new language

The system can easily be extended to support additional languages, and we encourage developers who are fluent in additional languages to contribute them to Label Sleuth.

To support a new language, follow the steps below:

1. **Find your desired language in the page for [FastText word vectors](https://fasttext.cc/docs/en/crawl-vectors.html)**

    Assuming your language is listed on this webpage, you will need to check for the *2- or 3-letter **language code*** associated with the language.
    
    This can be done by looking at the download links that appear next to your desired language. The language code can be found within the template `cc.{XX}.300` in the download link. For example, the download link for Nepali is https://dl.fbaipublicfiles.com/fasttext/vectors-crawl/cc.ne.300.bin.gz, indicating that the appropriate code is `ne`. This code is the `fasttext_language_id`.

2. **Compile or find a list of *stop-words* for the language**

    Stop-words are words that are considered less "meaningful" (in English, for instance, a word like *"such"* is considered a stop-word, as it carries very little semanatic meaning compared to words like *"kitchen"* or *"celebrate"*). For this reason, stop-words are often ignored by automated language systems, including some components that can be found within Label Sleuth.

    Bear in mind that the specific set of stop-words you choose is not so crucial; if in doubt, you can go for a very short list of words that come to mind.

    
3. **Create a Language object**

    Each language is defined by a Language instance in [languages.py](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/models/core/languages.py). Create a new object for your language, filling in the name of the language as well as the information from steps 1-2. For example, this is the language object for Arabic:

    ```python
    Arabic = Language(name='Arabic',
                      stop_words=["التى", "التي", "الذى", "الذي", "الذين", "ذلك", "هذا", "هذه", "هؤلاء", "قد", "وقد", "حيث",
                              "ان", "إن", "انه", "وان", "فان", "فإن", "بان", "اي", "أي", "ايضا", "أيضا", "إياه"],
                      fasttext_language_id='ar',
                      right_to_left=True)
     ```
    
    *Note that in this particular case an additional parameter of `right_to_left` is specified; this is only necessary for languages that use a right-to-left writing direction.*
    
4. **Add the object to the `Languages` class**

    [languages.py](https://github.com/label-sleuth/label-sleuth/blob/main/label_sleuth/models/core/languages.py) also contains a `Languages` class which holds all the languages supported by the system. Simply add your newly-created language object to `Languages`.
    
5. **Try it out**

    All done! As specified on the top of this page, you can now start up Label Sleuth to use your chosen language, with `python -m label_sleuth.start_label_sleuth --language <YOUR_LANGUAGE>` (It may take a little longer to start up the system for the first time, as the system downloads the necessary files for this newly-added language).
    
    Once Label Sleuth has started up using the chosen language, you can load documents in this language and work with the system as usual. Be sure to [open a pull request](https://github.com/label-sleuth/label-sleuth) so that fellow language speakers could use it!
