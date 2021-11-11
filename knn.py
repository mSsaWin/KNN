from collections import Counter
from math_func import *
def majority_vote(labels):
  # метки упорядочены от ближней к дальней
  vote_counts = Counter(labels)
  winner, winner_count = vote_counts.most_common(1)[0]
  num_winners = len([count for count in vote_counts.values() if count ==
  winner_count])
  if num_winners == 1:
    return winner
  else:
    return majority_vote(labels[:-1]) # пытаемся снова
def knn_classify(k, labeled_points, new_point):
# sort first
  by_distance = sorted(labeled_points, key = lambda point:
  distance(point[0], new_point))
  # k nearest find
  k_nearest_labels = [label for _,label in by_distance[:k]]
  # vote & return
  return majority_vote(k_nearest_labels)