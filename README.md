# label-sleuth.org

This repository holds the source of the official website of Label Sleuth. The actual website pages are automatically built from the source files using sphinx.

## Live documentation
The website can be viewed at: https://www.label-sleuth.org

The documentation is automatically built and deployed to the location above upon each PR to the `main` branch of this repository, after receiving approval by the maintainers.

## Test documentation locally
If you want to test the documentation locally, follow the steps below:

1. Switch to the `docs` directory

```
cd docs
```

2. Install dependencies

```
pip install -r requirements.txt
```

3. Run the sphinx build

```
make html
```

4. Use your web browser to open the following page (relative to your current directory): `_build/html/index.html`
