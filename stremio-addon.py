#!/usr/bin/env python3

from flask import Flask, Response, jsonify, url_for, abort
from functools import wraps

MANIFEST = {
    'id': 'org.stremio.tunisians',
    'version': '1.0.0',

    'name': 'Tunisian TV Shows Addon',
    'description': 'Sample addon made with Flask providing a few Tunisian TV Shows',

    'types': ['series'],    

    'catalogs': [
            # {'type': 'series', 'id': 'tunisianTVS', 'name':'Tunisian TV Shows'}
    ],

    'resources': [
        # 'catalog', 
        # {'name': 'stream', 'types': ['series'] , 'idPrefixes': ['tt', 'hpy']}
    ]
}

# CATALOG = {
#     'series': [
#         {
#             'id': 'tt0032138',
#             'name': 'Inchallah Mabrouk',
#             'genres': ['Family', 'Comedy'],
#             'description':'',
#             'releaseInfo':'',
#             'logo' : 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.elhiwarettounsi.com%2Fvod%2Fserie%2F50%2Finchallah-mabrouk&psig=AOvVaw1PmpBQ29ToXroXq9amF08J&ust=1613578763961000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjUprzn7u4CFQAAAAAdAAAAABAD',
#             'videos': [
#                     {'season': 1, 'episode': 1, 'id': 'tt1748166:1:1',
#                         'title': 'Inchallah Mabrouk Ep 01 Part 01', 'released': '2021-01-11'}
#             ]
#         },
#         {
#             'id': 'tt0017136',
#             'name': 'Dez Takhtef',
#             'description': '',
#             'releaseInfo': '',
#             'logo': 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.facebook.com%2FEttounsiyaTV%2Fvideos%2F444925966672819%2F&psig=AOvVaw1BOs7YcWpxdFmrbU5sFLLy&ust=1613579076911000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCOjsqOHo7u4CFQAAAAAdAAAAABAD',
#             'genres': ['Family', 'Game'],
#             'videos': [
#                     {'season': 1, 'episode': 1, 'id': 'hpytt0147753:1:1',
#                         'title': 'Dez Takhtef S01 E01', 'released': '2020-12-27'},
#             ]
#         }
#     ]
# }


# STREAMS = {
#     'series': {
#         'tt1748166:1:1': [
#             {'title': 'YouTube', 'ytId': '6cmW0I9mmfE'}
#         ],

#         'hpytt0147753:1:1': [
#             {'title': 'YouTube', 'ytId': 'H4uKxQ88Ah0'}
#         ]
#     }
# }

# # This is template we'll be using to construct URL for the item poster
# METAHUB_URL = 'https://images.metahub.space/poster/medium/{}/img'

# OPTIONAL_META = ["posterShape", "background", "logo", "videos", "description", "releaseInfo", "imdbRating", "director", "cast",
#                  "dvdRelease", "released", "inTheaters", "certification", "runtime", "language", "country", "awards", "website", "isPeered"]

app = Flask(__name__)


def respond_with(data):
    resp = jsonify(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp


@app.route('/manifest.json')
def addon_manifest():
    return respond_with(MANIFEST)


# @app.route('/catalog/<type>/<id>.json')
# def addon_catalog(type, id):
#     if type not in MANIFEST['types']:
#         abort(404)

#     catalog = CATALOG[type] if type in CATALOG else []
#     metaPreviews = {
#         'metas': [
#             {
#                 'id': item['id'],
#                 'type': type,
#                 'name': item['name'],
#                 'genres': item['genres'],
#                 'poster': item['logo']
#             } for item in catalog
#         ]
#     }
#     return respond_with(metaPreviews)


# @app.route('/meta/<type>/<id>.json')
# def addon_meta(type, id):
#     if type not in MANIFEST['types']:
#         abort(404)

#     def mk_item(item):
#         meta = dict((key, item[key])
#                     for key in item.keys() if key in OPTIONAL_META)
#         meta['id'] = item['id']
#         meta['type'] = type
#         meta['name'] = item['name']
#         meta['genres'] = item['genres']
#         meta['poster'] = item['logo']
#         return meta

#     meta = {
#         'meta': next((mk_item(item)
#                       for item in CATALOG[type] if item['id'] == id),
#                      None)
#     }

#     return respond_with(meta)


# @app.route('/stream/<type>/<id>.json')
# def addon_stream(type, id):
#     if type not in MANIFEST['types']:
#         abort(404)

#     streams = {'streams': []}
#     if type in STREAMS and id in STREAMS[type]:
#         streams['streams'] = STREAMS[type][id]
#     return respond_with(streams)


if __name__ == '__main__':
    app.run()