from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory list to store favorites (demo purpose)
favorites = [
    "Limited-time sneaker drop",
    "Exclusive concert tickets released"
]

@app.route('/')
def index():
    # For demo, just render index.html; trends fetching to be added separately
    return render_template('index.html')

@app.route('/favorites')
def show_favorites():
    return render_template('favorites.html', favorites=favorites)

@app.route('/remove_favorite', methods=['DELETE'])
def remove_favorite():
    data = request.get_json()
    fav_to_remove = data.get('favorite')
    if fav_to_remove and fav_to_remove in favorites:
        favorites.remove(fav_to_remove)
        return jsonify({"message": "Favorite removed"}), 200
    else:
        return jsonify({"error": "Favorite not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)

