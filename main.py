# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# [START gae_python38_app]
# [START gae_python3_app]
import requests
import json
from geolib import geohash
from flask import Flask, request, jsonify


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
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
    # print("++++++++", search_data)

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
    # if(ticketmaster_response.get("page").get("number") == 0):
    #     print("No results.")
    
    print("----")
    return ticketmaster_response



if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
# [END gae_python3_app]
# [END gae_python38_app]
