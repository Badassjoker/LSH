import numpy as np

def max_users_and_movies(filename):
  file = open(filename, 'r')

  movie_max = 0
  user_max = 0

  for line in file:
    line = line.strip()
    user_id, movie_id, rating = line.split('\t')

    try:
      user_id = int(user_id)
      movie_id = int(movie_id)
    except ValueError:
      continue

    movie_max = max(movie_max, movie_id)
    user_max = max(user_max, user_id)
  file.close()
  return [user_max, movie_max]


def rating_matrix(filename, max_user_number, max_movie_number):
  file = open(filename, 'r')

  I = np.zeros((max_user_number, max_movie_number))

  for line in file:
    line = line.strip()
    user_id, movie_id, rating = line.split('\t')

    try:
      user_id = int(user_id)
      movie_id = int(movie_id)
      rating = float(rating)
    except ValueError:
      continue

    if rating >= 3.5:
      I[user_id-1][movie_id-1] = 1.0
  
  file.close()
  return I

train_filename = 'train.txt'

max_user_number, max_movie_number = max_users_and_movies(train_filename)
I = rating_matrix(train_filename, max_user_number, max_movie_number)

fp1 = open('signature.txt', 'w')

for i in range(max_user_number):
  fp1.write('%s ' % (i+1))

  for j in range(max_movie_number):
    if I[i][j] == 1.0:
      fp1.write('%s ' % (j+1))

  fp1.write('\n')

fp1.close()