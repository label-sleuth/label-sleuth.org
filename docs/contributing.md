# Contribution Guidelines

Label Sleuth is an open source project committed to bringing NLP model creation to domain experts. The guide below provides information on how you can join the Label Sleuth community in this goal.

## How can I contribute?

There are multiple ways to contribute to the project:

- [Report bugs](#reporting-bugs)
- [Request new features](#requesting-new-features)
- [Contribute code](#contributing-code)

## Reporting bugs

To report a bug, please open a bug issue in the [issue tracker](https://github.com/label-sleuth/label-sleuth/issues). To make it easier for the community to address the issue, please provide a detailed description of it and include steps to reproduce it.

## Requesting new features

If you have an idea about an enhancement or new feature, please open a feature request/enhancement issue in the [issue tracker](https://github.com/label-sleuth/label-sleuth/issues).

## Contributing code

### Working on Issues

While not required, it is good practice to ensure before you start working on a code change that what you will be working on is captured in an issue. This allows the community to be aware of what everyone is working on and provide input before you spend time on the actual change.

### Prerequisites

Before contributing to Label Sleuth, you should make sure you have the following tools
installed:

- Node.js v16 or above. You can install it [directly](https://nodejs.org/en/download/) or
  [through a package manager](https://nodejs.org/en/download/package-manager/).
  - If you are on macOS, we recommend using
    [nvm](https://github.com/nvm-sh/nvm) to help manage different versions of
    Node.js
- Git
- Anaconda

_Note: Node.js is only required if you are contributing code to the frontend of Label Sleuth._
  
### 1. Fork the repo

Go to
[Label Sleuth's GitHub repo](https://github.com/label-sleuth/label-sleuth)
and click the `Fork` button on the top-right corner. This will create a copy
of the repo associated with your account.

### 2. Clone your fork

2. Click on `[your_github_username]/label-sleuth`.
3. Click on the `Clone or Download` button and copy the URL from the
    `Clone with SSH` option. It should start with `git@github.com...`

In your terminal, run:

```sh
git clone git@github.com:[your_github_username]/label-sleuth.git
cd label-sleuth
```

See [GitHub docs](https://help.github.com/articles/fork-a-repo/) for more
details.

### 3. Add upstream remotes

When you clone your forked repo, running `git remote -v` will show that the
`origin` is pointing to your forked repo by default.

Now you also need to add the `label-sleuth/label-sleuth` repo as your upstream
remote branch:

```sh
# Add the upstream remote to your repo
git remote add upstream git@github.com:label-sleuth/label-sleuth.git

# Verify that the remote was added
git remote -v
```

Your terminal should output something like this:

```sh
origin  [your forked repo] (fetch)
origin  [your forked repo] (push)
upstream    git@github.com:label-sleuth/label-sleuth.git (fetch)
upstream    git@github.com:label-sleuth/label-sleuth.git (push)
```

### 4. Work in a branch

When contributing to Label Sleuth, your work should always be done in a separate branch.
This is also how you will be submitting your pull request when your work is done.

To create a new branch, ensure you are on your forked branch in your terminal
and run:

```sh
git pull origin main
git checkout -b {your-branch-name}
```


### 5. Build and start the development environment

From the root directory of your fork, run:

```sh
#To install backend dependencies
conda create --yes -n label-sleuth python=3.8
conda activate label-sleuth
pip install label-sleuth

#To run the backend 
python -m label_sleuth.start_label_sleuth


#To install frontend dependencies
cd frontend
npm install

#To run the frontend in development mode
npm start
```

The last version of the frontend is statically served by the backend, so if you are not making any frontend contributions, the frontend-related commands above are not required.

### 6. Test the application

To test the backend, run:

```sh
python -m unittest
```

To test the frontend, run:

```sh
npm start --prefix frontend
```

### 6. Create a Pull Request

We use [GitHub pull requests](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) to accept contributions. Once submitted, the pull request will be reviewed by the community as explained below.

#### Developer Certificate of Origin

Before contributing to the project, all contributors must sign a Developer Certificate of Origin (DCO). By signing the DCO, you are attesting that you are the author of the contribution and you are freely contributing it under the terms of the Apache-2.0 license.

To sign the DCO, include a copy of the [Developer's Certificate of Origin 1.1](https://elinux.org/Developer_Certificate_Of_Origin) in a pull request comment.

#### Code Review

Code review of pull requests is open to anyone. While only maintainers can merge pull requests, community feedback on pull requests is very valuable. It can also be helpful in becoming acquainted with the codebase. You can find a list of open pull requests [here](https://github.com/label-sleuth/label-sleuth/pulls).

#### Asking for Help/Feedback

If you are working on the code and need help finishing it or would want to get input from the community on the approach that you are following, you can create a Work In Progress pull request. To this end, when creating the pull request, select 'Create draft pull request' by clicking on the arrow next to 'Create pull request'. This will inform the reviewer that the code is not final. It also means that the pull request will not be merged. When the pull request is ready to be reviewed for merging, the reviewer or you can mark it as "Ready for review".

### 9. Updating a pull request

Stay up to date with the activity in your pull request. Contributors of Label Sleuth will be reviewing your work and making comments, asking questions and suggesting changes to be made before they merge your code.

Your branch has to be updated with the main branch before merging it. Thus, anytime new changes are added to the main branch, you will have to update the branch you are working on. To do so, run `git merge origin main` or `git pull --rebase origin main`. The former will include a merge commit while the latter will re-write history by adding the new commits of the main branch to your branch, while maintaining a cleaner and linear commit history. If you think that your changes should be added into main without being squashed into a single commit, use the rebase approach.

Once all revisions to your pull request are complete, a maintainer of Label Sleuth will merge your commits for you.

### Good First Issues

If you want to contribute to Label Sleuth and do not know where to start, take a look at the issues tagged with the `good first issue` label. These have been reviewed by other contributors and identified as self-contained issues that are suitable for a first contribution. You can find a list of currently open issues with this label [here](https://github.com/label-sleuth/label-sleuth/issues?q=is%3Aopen+is%3Aissue+label%3A%22good+first+issue%22).
