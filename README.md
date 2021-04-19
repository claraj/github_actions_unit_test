1. Go to Action tab
2. Select Python Application and select Set up this workflow
3. Edit python-app.yml file as needed (see example in this repo https://github.com/claraj/github_actions_unit_test/blob/main/.github/workflows/python-app.yml)
4. This workflow installs and runs Flake8 to check for unused variables, code errors. The action will fail if Flake8 finds any https://flake8.pycqa.org/en/latest/
5. Commit python-app.yml file to repo
6. Action runs whenever the events listed occur, in this example, on any push or pull request.
7. Action reports can be found in the Action tab. They will also display as part of a PR

More on GitHub actions https://docs.github.com/en/actions 