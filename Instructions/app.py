from flask import Flask, render_template, redirect, url_for

#import pymongo library, which let us connect Flask app to Mongo db
from flask_pymongo import PyMongo
from flask_pymongo import MongoClient
import scrape_mars

# Create instance of Flask app
app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/missiontomars'
mongo = PyMongo(app)

# Create route that renders index.html template
@app.route("/")
def index():
        # Find one record of data from the mongo database
        # Return teamplate data and render an index.html template and pass it to the dataretrieved from the db
        mars = mongo.db.mars.find_one()
        return render_template("index.html", mars = mars)

    
@app.route("/scrape")
def scraper():
    # Run the scrape function
    # mars_info = mongo.db.mars
    mars = mongo.db.mars
    mars_data = scrape_mars.scrape_all()

    # Insert the scraped data
    mars.update({}, mars_data, upsert=True)

    # Redirect back to home page
    return redirect("/", code=302)
    
    
if __name__ == "__main__":
    app.run(debug=True)

  