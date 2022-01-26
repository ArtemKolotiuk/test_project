## _Learning project for testing API with python_
#### It run tests based in pytest and generates reports in allure.
### Requirements
- Python 3.7+ 
- pipenv

### Setup project (it work in virtual environment  - pipenv)
```
pipenv shell
 ```
 ```
 pipenv sync
 ```
 ```
 pipenv install
 ```
 ### Run tests
#### To run all tests 
```
pytest -v
```
#### To run custom file
```
pytest <your_file.py> -v
```
##### More about [custom run tests](https://docs.pytest.org/en/6.2.x/example/markers.html)

### Reporting
##### Generates reports in [allure](https://docs.qameta.io/allure-report/frameworks/python/pytest)

To generate reports for all tests
```  
pytest  --alluredir=./<raw_reports_folder>
```
 To generate report for custom test
 ```
pytest <your_file.py> --alluredir=./<raw_reports_folder>
```
#### Run allure server with results
```
allure serve <raw_reports_folder>
```