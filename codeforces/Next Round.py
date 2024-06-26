  input_line = input().strip().split()
  n = int(input_line[0])
  k = int(input_line[1])

  scores_line = input().strip().split()
  scores = list(map(int, scores_line))

  k_score = scores[k-1]

  advancers = 0
  for score in scores:
      if score >= k_score and score > 0:
          advancers += 1

  print(advancers)