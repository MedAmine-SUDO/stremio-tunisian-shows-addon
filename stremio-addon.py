from flask import Flask, Response, jsonify, url_for, abort
from functools import wraps

MANIFEST = {
    'id': 'org.stremio.tunisians',
    'version': '1.0.0',

    'name': 'Tunisian Shows and series',
    'description': 'Sample addon made with Flask providing a few public domain tunisian shows and series',

    'types': ['shows', 'series'],

    'catalogs': [
        {'type': 'shows', 'id': 'Hello, Python'},
        {'type': 'series', 'id': 'Hello, Python'}
    ],

    'resources': [
        'catalog',
        {'name': 'stream', 'types': [
            'shows', 'series'], 'idPrefixes': ['tt', 'hpy']}
    ]
}

STREAMS = {
    'movie': {
        'tt0032138': [
            {'title': 'Torrent',
                'infoHash': '24c8802e2624e17d46cd555f364debd949f2c81e', 'fileIdx': 0}
        ],
        'tt0017136': [
            {'title': 'Torrent',
                'infoHash': 'dca926c0328bb54d209d82dc8a2f391617b47d7a', 'fileIdx': 1}
        ],
        'tt0051744': [
            {'title': 'Torrent', 'infoHash': '9f86563ce2ed86bbfedd5d3e9f4e55aedd660960'}
        ],
        'tt1254207': [
            {'title': 'HTTP URL', 'url': 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4'}
        ],
        'tt0031051': [
            {'title': 'YouTube', 'ytId': 'm3BKVSpP80s'}
        ],
        'tt0137523': [
            {'title': 'External URL',
                'externalUrl': 'https://www.netflix.com/watch/26004747'}
        ]
    },

    'series': {
        'tt1748166:1:1': [
            {'title': 'Torrent', 'infoHash': '07a9de9750158471c3302e4e95edb1107f980fa6'}
        ],

        'hpytt0147753:1:1': [
            {'title': 'YouTube', 'ytId': '5EQw5NYlbyE'}
        ],
        'hpytt0147753:1:2': [
            {'title': 'YouTube', 'ytId': 'ZzdBKcVzx9Y'}
        ]
    }
}

CATALOG = {
    'movie': [
        {'id': 'tt0032138', 'name': 'The Wizard of Oz', 'genres': [
            'Adventure', 'Family', 'Fantasy', 'Musical']},
        {'id': 'tt0017136', 'name': 'Metropolis',
         'genres': ['Drama', 'Sci-Fi']},
        {'id': 'tt0051744', 'name': 'House on Haunted Hill',
         'genres': ['Horror', 'Mystery']},
        {'id': 'tt1254207', 'name': 'Big Buck Bunny',
         'genres': ['Animation', 'Short', 'Comedy'], },
        {'id': 'tt0031051', 'name': 'The Arizona Kid',
         'genres': ['Music', 'War', 'Western']},
        {'id': 'tt0137523', 'name': 'Fight Club', 'genres': ['Drama']}
    ],
    'series': [
        {
            'id': 'tt1748166',
            'name': 'Pioneer One',
            'genres': ['Drama'],
            'videos': [
                    {'season': 1, 'episode': 1, 'id': 'tt1748166:1:1',
                        'title': 'Earthfall', 'released': '2010-06-16'}
            ]
        },
        {
            'id': 'hpytt0147753',
            'name': 'Captain Z-Ro',
            'description': 'From his secret laboratory, Captain Z-Ro and his associates use their time machine, the ZX-99, to learn from the past and plan for the future.',
            'releaseInfo': '1955-1956',
            'logo': 'https://fanart.tv/fanart/tv/70358/hdtvlogo/captain-z-ro-530995d5e979d.png',
            'imdbRating': 6.9,
            'genres': ['Sci-Fi'],
            'videos': [
                    {'season': 1, 'episode': 1, 'id': 'hpytt0147753:1:1',
                        'title': 'Christopher Columbus', 'released': '1955-12-18'},
                    {'season': 1, 'episode': 2, 'id': 'hpytt0147753:1:2',
                        'title': 'Daniel Boone', 'released': '1955-12-25'}
            ]
        }
    ]
}

METAHUB_URL = 'https://images.metahub.space/poster/medium/{}/img'   

app = Flask(__name__)


def respond_with(data):
    resp = jsonify(data)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Access-Control-Allow-Headers'] = '*'
    return resp


@app.route('/manifest.json')
def addon_manifest():
    return respond_with(MANIFEST)

@app.route('/stream/<type>/<id>.json')
def addon_stream(type, id):
    if type not in MANIFEST['types']:
        abort(404)

    streams = {'streams': []}
    if type in STREAMS and id in STREAMS[type]:
        streams['streams'] = STREAMS[type][id]
    return respond_with(streams)

@app.route('/catalog/<type>/<id>.json')
def addon_catalog(type, id):
    if type not in MANIFEST['types']:
        abort(404)

    catalog = CATALOG[type] if type in CATALOG else []
    metaPreviews = {
        'metas': [
            {
                'id': item['id'],
                'type': type,
                'name': item['name'],
                'genres': item['genres'],
                'poster': METAHUB_URL.format(item['id'])
            } for item in catalog
        ]
    }
    return respond_with(metaPreviews)

if __name__ == '__main__':
    app.run()