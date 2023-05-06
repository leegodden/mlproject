## ML End to End Projects

`https://www.youtube.com/watch?v=Rv6UFGNmNZg&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG&index=2&pp=iAQB`

## SETUP

1. create github repo for the project
2. download `anaconda` and `environmnt` for `python` data science
3. intialise zsh for `conda` `sudo conda init zsh`
4. intialise new venv environment for python
   `conda create -p venv python==3.8 -y`

5. run `conda activate venv/` to activate our environment - you will see below now in the termminal
   `Desktop/dev/ml-project via conda venv`

6. now run `git init` add files, first commit then:
   `git remote add origin https://github.com/leegodden/mlproject.git`
   `git branch -M main`
   `git push -u origin main`

7. create `.gitignore` file & add code for python including venv/
8. create `requirements.txt` and `setup.py` setup.py enables us to build & deploy our app package

9. create a source folder in the root and in it add `__init__.py`
   The `__init__.py` files are required to make Python treat directories containing the file as packages.
   so our app will be built in src

10. add code to `setup.py`
11. in `requirements.txt` add `-e .` which will automatically trigger `setup.py`
12. to get `setup.py` to ignore the `-e .` in the `requirements.txt` file add an if statement

13. now we can install `requirements.txt` using `pip` and all our packages will be installed
    `pip install -r requirements.txt`
