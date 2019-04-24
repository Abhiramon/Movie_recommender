from recommender_engine import get_recommendations
import urllib
import requests


def test_app_running(url):
	response = urllib.request.urlopen(url)
	assert response.code == 200, "Page shoud load"



def test_get_recommendations(title, n):
	recommendations = get_recommendations(title, n)
	assert recommendations.size > 0, "Should be non-empty list"
	assert str(type(recommendations)) == "<class 'pandas.core.series.Series'>", "Should be pandas.core.series.Series"


def test_movie_submission(url, title):
	r = requests.get(url, data={"movie_name": title})
	assert r.status_code==200, "Submission should succeed"



if __name__ == "__main__":

	url = "http://localhost:5001"

	test_app_running(url)
	test_get_recommendations("casino royale", 5)
	test_movie_submission(url, "the dark knight")
	print("All tests passed!")