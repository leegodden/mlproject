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

## Project Structure, Logging And Exception Handling

1. add `components` folder in src and add `__init__.py` `components` will contain all our modules
2. create `data_ingestions.py` & `data_transformation` & `model_trainer.py` in `components` folder
   a brief summary of what these files will do is below:

   `Data ingestion` is the process of moving data from a source into a landing area or an object store where it can
   be used for ad hoc queries and analytics

   `Data transformation` involves creating new features from the existing features in the data, or reducing
   the dimensionality of the data. This can help to improve the performance of the machine learning algorithm.

   `A machine learning model` is a mathematical representation of real-world data. The model is trained with large
   datasets, and algorithms assist in learning from the available data. The ML models recognize data patterns, take
   input queries, and make predictions based on previous data.

3. add a `pipeline` folder in components and add `train_pipeline.py` & `predict_pipeline.py` & `__init__.py` files into it

   `A data pipeline` is a data engineering pipeline that typically `ingests`, `cleans`, and `processes` data to make
   it compatible or optimized for `machine learning (ML)` or other analytical and visualization processes.

4. add a further 3 files into the src folder: `exceptions.py` `logger.py` & `utils.py`

5. add code for our `exceptions.py`
6. add code for `logger.py`
