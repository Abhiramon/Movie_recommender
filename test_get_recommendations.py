from recommender_engine import get_recommendations


def test_get_recommendations(title)

    recommendations = get_recommendations(title).head(10)

    assert recommendations.size > 0, "Should be non-empty list"
    assert str(type(recommendations)) == "<class 'pandas.core.series.Series'>", "Should be pandas.core.series.Series"

if __name__ == '__main__':

    title = "The Dark Knight"

    test_get_recommendations(title)
