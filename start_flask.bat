@echo off

:: change to current directory
cd %cd%

:: change to parent directory
cd ..

:: ------ FLASK ------
set FLASK_APP=MUII_G2_Family-Lock-Manager

flask run --host=0.0.0.0