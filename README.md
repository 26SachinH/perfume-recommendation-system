An elegant, intelligent full-stack web application to discover perfumes similar to your favorite scents, using machine learning and modern web design.

Overview
This project enables users to search for a perfume and instantly receive a list of the top 5 similar fragrances based on their description and notes.
It combines:

Natural Language Processing (NLP) techniques for text analysis.

Machine Learning algorithms for ranking similarity.

A RESTful API and interactive web frontend for a seamless experience.

🎯 Key Features
**Smart Recommendations Engine
**
Vectorizes perfume descriptions and notes using TF-IDF (Term Frequency-Inverse Document Frequency).

Calculates cosine similarity to measure how closely other perfumes relate to the selected one.

Refines the recommendations with a Random Forest Regressor to boost the relevance and smooth ranking.

Beautiful Responsive UI

Clean, modern design with a luxury fragrance theme.

Intuitive search and discover interface.

Loading animations and elegant error messages.

**REST API**

Lightweight JSON API to integrate recommendations into other apps or services.

**Customizable Dataset
**
Easily swap or extend the dataset to include more perfumes.

🧠 How It Works
The process includes several steps:

Data Loading & Preprocessing

Load a CSV file of perfumes.

Combine Description and Notes into a single text field.

Remove rows with missing values.

Text Vectorization

Use TfidfVectorizer to convert text into numeric vectors representing each perfume's unique scent profile.

Similarity Computation

For the selected perfume, extract its TF-IDF vector.

Compute cosine similarity between this vector and all others in the dataset.

Ranking with Random Forest

Train a Random Forest Regressor using all vectors and their similarity scores.

Predict refined similarity scores for ranking.

Result Formatting

Select the top 5 most similar perfumes.

Return relevant metadata: name, brand, description, and image URL.

Frontend Display

Show recommendations in visually appealing cards.

Handle no results and errors gracefully.

📂 Dataset
CSV Columns Required:

Name: Perfume name

Brand: Brand name

Description: Short fragrance description

Notes: Key scent notes (e.g., floral, citrus)

Image URL: Link to the perfume image

Tip: You can replace the CSV with your own dataset, as long as these columns exist.

🛠️ Tech Stack
Layer	Tools & Libraries
Backend	Python, Flask, scikit-learn, pandas
Frontend	HTML, CSS, JavaScript
ML	TfidfVectorizer, Cosine Similarity, Random Forest
Web Server	Flask Development Server

🚀 Installation
1️⃣ Clone the Repository

bash
Copy
Edit
git clone https://github.com/your-username/perfume-recommendation-system.git
cd perfume-recommendation-system
2️⃣ Install Python Dependencies

bash
Copy
Edit
pip install flask pandas scikit-learn
(or create a requirements.txt and install with pip install -r requirements.txt)

3️⃣ Adjust Dataset Path
Make sure app.py points to your dataset CSV:

python
Copy
Edit
df = pd.read_csv("path/to/final_perfume_data.csv", encoding="ISO-8859-1")
4️⃣ Run the App

bash
Copy
Edit
python app.py
5️⃣ Access in Browser

cpp
Copy
Edit
http://127.0.0.1:5000
🖥️ Usage
Open the homepage.

Enter a perfume name in the search box.

Click Discover Similar Fragrances.

View the recommendations as cards with images and descriptions.

Use Clear to reset the search.

API Reference
Endpoint:

bash
Copy
Edit
POST /perfume-recommendations
Request Body (JSON):

json
Copy
Edit
{
  "perfume_name": "Chanel No. 5"
}
Response Example:

json
Copy
Edit
{
  "recommendations": [
    {
      "name": "Dior J'adore",
      "brand": "Dior",
      "description": "A sophisticated floral bouquet with jasmine and rose.",
      "image": "https://example.com/jadore.jpg"
    },
    ...
  ]
}

Use Cases
Fragrance e-commerce sites recommending similar products.

Personal scent discovery tools.

Interactive kiosks in perfume shops.

Mobile apps for fragrance matching.

🔮 Future Improvements
Replace TF-IDF with transformer embeddings (e.g., Sentence-BERT).

Allow filtering by price, brand, or scent family.

Add user login and favorites.

Provide personalized recommendations based on user history.

Deploy with Docker and Nginx for production.
