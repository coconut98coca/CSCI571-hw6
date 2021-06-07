import requests
import json
from geolib import geohash
from flask import Flask, request, jsonify

app = Flask(__name__)
get_geo_url = "https://ipinfo.io/?token=c4eba8a0a82929"

@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    return app.send_static_file('base.html')

@app.route('/search', methods=["GET"])
def do_search():
    ticketmaster_base_url = "https://app.ticketmaster.com/discovery/v2/events.json?apikey=Qf8PRg3ggae12R8TRPqlTRnJdD6EE3q3"
    arg = request.args
    search_data = arg.to_dict()
    print("++++++++", search_data)

    # geo point
    latitude = search_data["latitude"]
    longitude = search_data["longitude"]
    geoPoint = geohash.encode(latitude, longitude, 7)
    ticketmaster_base_url += "&geoPoint=" + geoPoint
    # radius
    radius = search_data["distance"]
    ticketmaster_base_url += "&radius=" + radius
    # segment id
    segment_choose = search_data["category"]
    if segment_choose != "Default":
        if segment_choose == "Music":
            segment_id = "KZFzniwnSyZfZ7v7nJ"
        if segment_choose == "Sports":
            segment_id = "KZFzniwnSyZfZ7v7nE"
        if segment_choose == "ArtsTheatre":
            segment_id = "KZFzniwnSyZfZ7v7na"
        if segment_choose == "Film":
            segment_id = "KZFzniwnSyZfZ7v7nn"
        if segment_choose == "Miscellaneous":
            segment_id = "KZFzniwnSyZfZ7v7n1"
        ticketmaster_base_url += "&segmentId=" + segment_id
    # unit
    ticketmaster_base_url += "&unit=" + "miles"
    # keyword
    keyword = search_data["keyword"]
    ticketmaster_base_url += "&keyword=" + keyword
    print(ticketmaster_base_url)
    # request api
    ticketmaster_response = requests.get(ticketmaster_base_url).json()
    print(json.dumps(ticketmaster_response))
    ticketmaster_response = jsonify(ticketmaster_response)
    ticketmaster_response.headers['Access-Control-Allow-Origin'] = '*'
    print("----")
    return ticketmaster_response



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
