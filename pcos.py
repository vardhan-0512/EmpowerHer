def calculate_pcos_likelihood(responses):
    weights = {
        "irregular_periods": 0.2,
        "excessive_hair_growth": 0.2,
        "acne_oily_skin": 0.15,
        "weight_gain": 0.15,
        "hair_loss": 0.1,
        "dark_patches": 0.1,
        "mood_changes": 0.1
    }
    response_map = {
        "irregular_periods": responses.get("irregular_periods") == "Yes",
        "excessive_hair_growth": responses.get("excessive_hair_growth") == "Yes",
        "acne_oily_skin": responses.get("acne_oily_skin") == "Yes",
        "weight_gain": responses.get("weight_gain") == "Yes",
        "hair_loss": responses.get("hair_loss") == "Yes",
        "dark_patches": responses.get("dark_patches") == "Yes",
        "mood_changes": responses.get("mood_changes") == "Yes"
    }
    score = 0
    for key, weight in weights.items():
        if response_map.get(key, False):
            score += weight
    likelihood_percentage = min(score * 100, 100)
    return round(likelihood_percentage)