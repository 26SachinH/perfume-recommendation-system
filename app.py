from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load dataset
df = pd.read_csv(r"C:\Users\SACHIN HEBBALAKAR\OneDrive\Desktop\all project folder\final_perfume_data.csv", encoding='ISO-8859-1')
df.dropna(subset=['Description', 'Notes'], inplace=True)
df['combined_text'] = df['Description'] + ' ' + df['Notes']
perfume_names = df['Name'].tolist()

# Fit TF-IDF once
vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
X_tfidf = vectorizer.fit_transform(df['combined_text'])

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/perfume-recommendations", methods=["POST"])
def get_recommendations():
    data = request.get_json()
    perfume_name = data.get("perfume_name")

    if not perfume_name or perfume_name not in perfume_names:
        return jsonify({"recommendations": []})

    # Find index of selected perfume
    idx = df[df['Name'] == perfume_name].index[0]
    target_vector = X_tfidf[idx].toarray()

    # Compute similarity
    y = cosine_similarity(X_tfidf, target_vector).flatten()
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_tfidf.toarray(), y)
    predicted_scores = model.predict(X_tfidf.toarray())

    df['similarity_score'] = predicted_scores
    top_recs = df[df.index != idx].sort_values(by='similarity_score', ascending=False).head(5)

    recommendations = [
        {
            'name': row['Name'],
            'brand': row['Brand'],
            'description': row['Description'],
            'image': row['Image URL']
        }
        for _, row in top_recs.iterrows()
    ]

    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True)
