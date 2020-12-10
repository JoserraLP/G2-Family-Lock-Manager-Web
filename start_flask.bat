@echo off

:: change to current directory
cd %cd%

:: change to parent directory
cd ..

:: ------ FLASK ------
set FLASK_APP=Family_Lock_Manager

flask run --host=0.0.0.0