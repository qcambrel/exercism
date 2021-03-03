def latest(scores):
	return scores[-1]


def personal_best(scores):
	return max(scores)


def personal_top_three(scores):
	scores_descending = sorted(scores, key=lambda x: x, reverse=True)
	return scores_descending[:3] if len(scores) > 3 else scores_descending