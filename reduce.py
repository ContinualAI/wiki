from sklearn.manifold import TSNE


def get_2d_coordinates(vectorized_text):
	out = TSNE(
		n_components=2, 
		random_state=42
		).fit_transform(vectorized_text)
	return out

