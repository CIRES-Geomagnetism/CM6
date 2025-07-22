print("this is only a python file so that it gets uploaded to github. I dont want to lose it but I don't want any of github's whl building backend to see it")


# name: Publish to PyPI

# on:
#   release:
#     types: [created]

# jobs:
#   deploy:
#     runs-on: ubuntu-latest

#     steps:
#     - name: Checkout repository
#       uses: actions/checkout@v4

#     - name: Set up Python
#       uses: actions/setup-python@v4
#       with:
#         python-version: "3.12"

#     - name: Install build tools
#       run: |
#         python -m pip install --upgrade pip
#         pip install build twine

#     - name: Build package
#       run: python -m build

#     - name: Push to PyPI
#       env:
#         TWINE_USERNAME: "__token__"
#         TWINE_PASSWORD: "${{ secrets.PYPI_API_TOKEN }}"
#       run: twine upload dist/*