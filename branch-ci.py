print("this is only a python file so that it gets uploaded to github. I dont want to lose it but I don't want any of github's whl building backend to see it")


# This branch-ci is removed in case it was what was preventing the .whl from being created.

# name: difi pull request pipeline

# on:
#   push:
#     branches: ["difi8_and_xDIFI"]

# jobs:
#   test:
#     runs-on: ubuntu-latest

#     steps:
#     - name: Checkout code
#       uses: actions/checkout@v4

#     - name: Set up Python
#       uses: actions/setup-python@v5
#       with:
#         python-version: "3.13"

#     - name: Install dependencies
#       run: |
#         python -m pip install --upgrade pip
#         pip install -e .

#     - name: Compare with main branch
#       run: |
#         python -m unittest tests/test_getSQfield.py
#         python tests/validate_xdifi2.py
#         python tests/validate_difi8.py
#         python tests/validate_above_sq_current.py