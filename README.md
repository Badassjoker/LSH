# LSH
The dataset can be downloaded from http://files.grouplens.org/datasets/movielens/ml-20m.zip.

This LSH uses the rating file only.

preprocess.py will first preprocess the rating file which in my program is named rating.csv,
and generate train.txt. The name of the intput file can be changed in the Line 3 of preprocess.py.

The get_signature.py will use tran.txt to generate signature.txt.

At last, use lsh_mapper.py and lsh_reducer.py to get the final result file named result.txt.
To get the result Hadoop can be used. It also can be done by typing the command in the terminal as following:
python lsh_mapper.py | sort | python lsh_reducer.py

Using prediction&RMSE.py to get the final prediction value and RMSE
