from labelbox.data.serialization.labelbox_v1.converter import LBV1Converter
from labelbox import Client
import os


annotations = [{
    'frameNumber':
        1,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 582,
            'left': 1644,
            'height': 340,
            'width': 212
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 712,
            'left': 1256,
            'height': 204,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 47,
            'left': 155,
            'height': 381,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 728,
            'left': 546,
            'height': 263,
            'width': 290
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 494,
            'left': 361,
            'height': 183,
            'width': 207
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        2,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 595,
            'left': 1635,
            'height': 340,
            'width': 212
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 719,
            'left': 1246,
            'height': 204,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 45,
            'left': 148,
            'height': 381,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 731,
            'left': 540,
            'height': 262,
            'width': 290
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 494,
            'left': 353,
            'height': 184,
            'width': 209
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        3,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 600,
            'left': 1628,
            'height': 326,
            'width': 212
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 724,
            'left': 1233,
            'height': 188,
            'width': 332
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 46,
            'left': 130,
            'height': 381,
            'width': 341
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 732,
            'left': 536,
            'height': 262,
            'width': 290
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 494,
            'left': 346,
            'height': 183,
            'width': 211
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        4,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 604,
            'left': 1619,
            'height': 322,
            'width': 214
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 728,
            'left': 1225,
            'height': 180,
            'width': 336
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 37,
            'left': 123,
            'height': 386,
            'width': 343
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 732,
            'left': 536,
            'height': 269,
            'width': 288
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 494,
            'left': 338,
            'height': 185,
            'width': 216
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        5,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 619,
            'left': 1606,
            'height': 322,
            'width': 214
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 729,
            'left': 1208,
            'height': 180,
            'width': 336
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 36,
            'left': 116,
            'height': 386,
            'width': 343
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 733,
            'left': 529,
            'height': 269,
            'width': 288
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 493,
            'left': 332,
            'height': 185,
            'width': 216
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        6,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 623,
            'left': 1597,
            'height': 322,
            'width': 214
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 736,
            'left': 1195,
            'height': 180,
            'width': 336
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 30,
            'left': 108,
            'height': 386,
            'width': 343
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 734.5,
            'left': 522,
            'height': 269,
            'width': 290
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 491,
            'left': 326,
            'height': 185,
            'width': 216
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        7,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 632,
            'left': 1586,
            'height': 322,
            'width': 214
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 743,
            'left': 1189,
            'height': 175,
            'width': 323
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 30,
            'left': 86,
            'height': 367,
            'width': 354
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 736,
            'left': 515,
            'height': 269,
            'width': 292
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 490,
            'left': 316,
            'height': 183,
            'width': 218
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        8,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 634,
            'left': 1582,
            'height': 321,
            'width': 209
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 751,
            'left': 1188,
            'height': 170,
            'width': 316
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 26,
            'left': 78,
            'height': 367,
            'width': 354
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 736,
            'left': 500,
            'height': 266,
            'width': 302
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 488,
            'left': 311,
            'height': 183,
            'width': 218
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        9,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 641,
            'left': 1575,
            'height': 321,
            'width': 209
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 755,
            'left': 1188,
            'height': 168,
            'width': 307
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 23,
            'left': 63,
            'height': 372,
            'width': 362
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 736,
            'left': 500,
            'height': 270,
            'width': 297
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 488,
            'left': 305,
            'height': 182,
            'width': 219
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        10,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 648,
            'left': 1563,
            'height': 315,
            'width': 203
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 754,
            'left': 1172,
            'height': 172,
            'width': 309
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 14,
            'left': 48,
            'height': 371,
            'width': 366
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 736,
            'left': 493,
            'height': 271,
            'width': 304
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 486,
            'left': 292,
            'height': 184,
            'width': 224
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        11,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 650,
            'left': 1555,
            'height': 317,
            'width': 208
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 755,
            'left': 1169,
            'height': 174,
            'width': 294
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 11,
            'left': 47,
            'height': 374,
            'width': 367
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 740,
            'left': 484,
            'height': 271,
            'width': 304
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 485,
            'left': 287,
            'height': 184,
            'width': 224
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        12,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 657,
            'left': 1545,
            'height': 317,
            'width': 204
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 750,
            'left': 1162,
            'height': 168,
            'width': 290
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 34,
            'height': 374,
            'width': 367
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 737,
            'left': 476,
            'height': 271,
            'width': 304
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 479,
            'left': 278,
            'height': 184,
            'width': 224
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        13,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 663,
            'left': 1538,
            'height': 317,
            'width': 204
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 749,
            'left': 1154,
            'height': 173,
            'width': 289
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 27,
            'height': 374,
            'width': 367
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 738,
            'left': 473,
            'height': 271,
            'width': 304
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 476,
            'left': 271,
            'height': 183,
            'width': 229
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        14,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 666,
            'left': 1531,
            'height': 314,
            'width': 211
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 748,
            'left': 1147,
            'height': 176,
            'width': 283
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 23,
            'height': 312,
            'width': 367
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 737,
            'left': 470,
            'height': 271,
            'width': 304
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 470,
            'left': 264,
            'height': 187,
            'width': 231
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        15,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 670,
            'left': 1519,
            'height': 316,
            'width': 207
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 742,
            'left': 1136,
            'height': 187,
            'width': 272
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 23,
            'height': 281,
            'width': 357
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 731,
            'left': 457,
            'height': 278,
            'width': 312
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 464,
            'left': 254,
            'height': 193,
            'width': 235
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        16,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 674,
            'left': 1512,
            'height': 311,
            'width': 204
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 739,
            'left': 1129,
            'height': 190,
            'width': 279
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 19,
            'height': 276,
            'width': 356
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 731,
            'left': 457,
            'height': 277,
            'width': 306
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 457,
            'left': 245,
            'height': 189,
            'width': 238
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        17,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 678,
            'left': 1502,
            'height': 310,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 733,
            'left': 1118,
            'height': 198,
            'width': 267
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 271,
            'width': 367
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 725,
            'left': 447,
            'height': 277,
            'width': 306
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 453,
            'left': 236,
            'height': 189,
            'width': 238
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        18,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 679,
            'left': 1496,
            'height': 310,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 733,
            'left': 1110,
            'height': 203,
            'width': 262
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 265.5,
            'width': 360
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 725,
            'left': 438,
            'height': 276,
            'width': 315
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 450,
            'left': 227,
            'height': 191,
            'width': 244
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        19,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 685,
            'left': 1489,
            'height': 317,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 730,
            'left': 1099,
            'height': 206,
            'width': 273
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 260,
            'width': 353
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 726,
            'left': 438,
            'height': 271,
            'width': 307
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 449,
            'left': 222,
            'height': 183,
            'width': 244
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        20,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 689,
            'left': 1477,
            'height': 317,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 731,
            'left': 1086,
            'height': 213,
            'width': 260
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 258,
            'width': 345
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 721,
            'left': 431,
            'height': 271,
            'width': 308
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 448,
            'left': 217,
            'height': 177,
            'width': 244
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        21,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 690,
            'left': 1470,
            'height': 317,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 728,
            'left': 1077,
            'height': 213,
            'width': 260
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 259,
            'width': 335
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 723,
            'left': 423,
            'height': 271,
            'width': 308
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 446,
            'left': 212,
            'height': 177,
            'width': 244
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        22,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 697,
            'left': 1458,
            'height': 317,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 728,
            'left': 1065,
            'height': 213,
            'width': 260
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 227,
            'width': 313
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 736,
            'left': 420,
            'height': 250,
            'width': 302
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 446,
            'left': 212,
            'height': 164,
            'width': 236
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        23,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 701,
            'left': 1449,
            'height': 317,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 727,
            'left': 1055,
            'height': 219,
            'width': 253
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 214,
            'width': 307
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 743,
            'left': 417,
            'height': 250,
            'width': 302
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 432,
            'left': 190,
            'height': 147,
            'width': 255
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        24,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 705,
            'left': 1447,
            'height': 321,
            'width': 193
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 723,
            'left': 1049,
            'height': 229,
            'width': 250
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 202,
            'width': 282
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 754,
            'left': 408,
            'height': 235,
            'width': 308
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 448,
            'left': 209,
            'height': 150,
            'width': 228
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        25,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 708,
            'left': 1433,
            'height': 321,
            'width': 193
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 724,
            'left': 1035,
            'height': 229,
            'width': 251
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 198,
            'width': 272
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 759,
            'left': 399,
            'height': 234,
            'width': 317
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 424,
            'left': 170,
            'height': 148,
            'width': 262
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        26,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 714,
            'left': 1425,
            'height': 313,
            'width': 194
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 723,
            'left': 1027,
            'height': 240,
            'width': 248
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 190,
            'width': 272
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 758,
            'left': 392,
            'height': 227,
            'width': 322
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 413,
            'left': 163,
            'height': 152,
            'width': 230
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        27,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 719,
            'left': 1413,
            'height': 313,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 726,
            'left': 1018,
            'height': 235,
            'width': 238
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 208,
            'width': 284
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 754,
            'left': 384.5,
            'height': 228.5,
            'width': 328.5
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 409,
            'left': 151,
            'height': 178,
            'width': 268
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        28,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 724,
            'left': 1408,
            'height': 313,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 735,
            'left': 1011,
            'height': 217,
            'width': 237
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 206,
            'width': 281
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 750,
            'left': 377,
            'height': 230,
            'width': 335
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 409,
            'left': 148,
            'height': 178,
            'width': 268
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        29,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 726,
            'left': 1398,
            'height': 313,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 738,
            'left': 1006,
            'height': 205,
            'width': 233
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 200,
            'width': 274
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 750,
            'left': 370,
            'height': 232,
            'width': 342
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 401,
            'left': 138,
            'height': 181,
            'width': 275
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        30,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 728,
            'left': 1389,
            'height': 313,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 751,
            'left': 993,
            'height': 182,
            'width': 230
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 191,
            'width': 261
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 745,
            'left': 368,
            'height': 232,
            'width': 342
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 397,
            'left': 132,
            'height': 181,
            'width': 275
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        31,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 733,
            'left': 1381,
            'height': 308,
            'width': 196
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 758,
            'left': 988,
            'height': 181,
            'width': 216
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 190,
            'width': 258
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 739,
            'left': 368,
            'height': 243,
            'width': 341
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 394,
            'left': 125,
            'height': 181,
            'width': 275
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        32,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 740,
            'left': 1369,
            'height': 308,
            'width': 193
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 769,
            'left': 979,
            'height': 167,
            'width': 204
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 181,
            'width': 247
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 728,
            'left': 367,
            'height': 251,
            'width': 341
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 387,
            'left': 116,
            'height': 182,
            'width': 280
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        33,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 740,
            'left': 1361,
            'height': 308,
            'width': 193
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 774,
            'left': 973,
            'height': 163,
            'width': 199
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 176,
            'width': 239
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 720,
            'left': 368,
            'height': 261,
            'width': 340
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 383,
            'left': 106,
            'height': 180,
            'width': 286
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        34,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 743,
            'left': 1353,
            'height': 308,
            'width': 193
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 778,
            'left': 967,
            'height': 162,
            'width': 196
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 171,
            'width': 235
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 718,
            'left': 364,
            'height': 257,
            'width': 344
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 379,
            'left': 100,
            'height': 183,
            'width': 287
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        35,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 749,
            'left': 1343,
            'height': 308,
            'width': 193
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 795,
            'left': 957,
            'height': 148,
            'width': 178
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 160,
            'width': 225
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 711,
            'left': 363,
            'height': 256,
            'width': 343
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 375,
            'left': 93.5,
            'height': 187,
            'width': 289.5
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        36,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 752,
            'left': 1337,
            'height': 309,
            'width': 190
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 796,
            'left': 948,
            'height': 149,
            'width': 185
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 150,
            'width': 216
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 710,
            'left': 365,
            'height': 269,
            'width': 340
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 371,
            'left': 87,
            'height': 191,
            'width': 292
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        37,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 758,
            'left': 1324,
            'height': 302,
            'width': 189
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 794,
            'left': 935,
            'height': 153,
            'width': 177
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 131,
            'width': 206
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 704,
            'left': 360,
            'height': 275,
            'width': 342
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 365,
            'left': 76,
            'height': 194,
            'width': 297
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        38,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 763,
            'left': 1318,
            'height': 302,
            'width': 189
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 789,
            'left': 928,
            'height': 160,
            'width': 174
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 106,
            'width': 199
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 702,
            'left': 357,
            'height': 277,
            'width': 341
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 363,
            'left': 70,
            'height': 199,
            'width': 300
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        39,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 766,
            'left': 1310,
            'height': 302,
            'width': 189
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 786,
            'left': 918,
            'height': 164,
            'width': 176
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 38,
            'width': 134
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 695,
            'left': 357,
            'height': 282,
            'width': 340
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 359,
            'left': 64,
            'height': 200,
            'width': 302
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        40,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 770,
            'left': 1299,
            'height': 302,
            'width': 189
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 775,
            'left': 905,
            'height': 177,
            'width': 177
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eo0y6188xz7m35',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 16,
            'width': 111
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 694,
            'left': 354,
            'height': 282,
            'width': 338
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 353,
            'left': 56,
            'height': 203,
            'width': 305
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        41,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 772,
            'left': 1289,
            'height': 302,
            'width': 189
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 766,
            'left': 896,
            'height': 185,
            'width': 176
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 688.5,
            'left': 351.5,
            'height': 287,
            'width': 338.5
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 350,
            'left': 51,
            'height': 203,
            'width': 306
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 321,
            'left': 569,
            'height': 125,
            'width': 109
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        42,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 775,
            'left': 1281,
            'height': 297,
            'width': 188
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 754,
            'left': 884,
            'height': 196,
            'width': 175
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 683,
            'left': 349,
            'height': 292,
            'width': 339
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 342,
            'left': 41,
            'height': 204,
            'width': 310
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 317,
            'left': 559.5,
            'height': 126,
            'width': 111
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        43,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 778,
            'left': 1273,
            'height': 297,
            'width': 188
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 748,
            'left': 875,
            'height': 202,
            'width': 152
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 682,
            'left': 346,
            'height': 292,
            'width': 339
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 335,
            'left': 37,
            'height': 204,
            'width': 310
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 313,
            'left': 550,
            'height': 127,
            'width': 113
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        44,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 779,
            'left': 1266,
            'height': 293,
            'width': 188
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 741,
            'left': 865,
            'height': 211,
            'width': 158
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 681,
            'left': 345,
            'height': 292,
            'width': 339
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 331,
            'left': 33,
            'height': 204,
            'width': 310
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 309,
            'left': 543,
            'height': 127,
            'width': 113
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        45,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 785,
            'left': 1255,
            'height': 293,
            'width': 188
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 734,
            'left': 855.5,
            'height': 217.5,
            'width': 160
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 672,
            'left': 340,
            'height': 296,
            'width': 339
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 322,
            'left': 28,
            'height': 211,
            'width': 311
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 303,
            'left': 532,
            'height': 127,
            'width': 113
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        46,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 784,
            'left': 1245,
            'height': 293,
            'width': 188
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 727,
            'left': 846,
            'height': 224,
            'width': 162
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 669,
            'left': 344,
            'height': 297,
            'width': 333
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 314,
            'left': 23,
            'height': 211,
            'width': 311
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 298,
            'left': 526,
            'height': 127,
            'width': 113
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        47,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 787,
            'left': 1234,
            'height': 290,
            'width': 186
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 723,
            'left': 832,
            'height': 224,
            'width': 165
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 668,
            'left': 339,
            'height': 297,
            'width': 333
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 306,
            'left': 12,
            'height': 211,
            'width': 315
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 291,
            'left': 514,
            'height': 127,
            'width': 113
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        48,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 790,
            'left': 1227,
            'height': 286,
            'width': 187
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 714,
            'left': 824,
            'height': 235,
            'width': 167
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 667,
            'left': 335,
            'height': 297,
            'width': 333
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 301,
            'left': 7,
            'height': 211,
            'width': 315
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 289,
            'left': 506,
            'height': 127,
            'width': 113
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        49,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 792,
            'left': 1216,
            'height': 286,
            'width': 190
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 710,
            'left': 815,
            'height': 238,
            'width': 167
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 664,
            'left': 337,
            'height': 297,
            'width': 327
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 298,
            'left': 0,
            'height': 214,
            'width': 319
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 285,
            'left': 498,
            'height': 127,
            'width': 115
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        50,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 797,
            'left': 1205,
            'height': 283,
            'width': 190
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 707,
            'left': 815,
            'height': 239,
            'width': 157
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 658,
            'left': 334,
            'height': 302,
            'width': 327
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 290,
            'left': 0,
            'height': 217,
            'width': 312
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 281,
            'left': 485,
            'height': 127,
            'width': 115
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        51,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 797,
            'left': 1197,
            'height': 283,
            'width': 190
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 707,
            'left': 812,
            'height': 240,
            'width': 157
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 657,
            'left': 328,
            'height': 302,
            'width': 327
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 284,
            'left': 0,
            'height': 223,
            'width': 310
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 277,
            'left': 478,
            'height': 127,
            'width': 115
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        52,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 801,
            'left': 1183,
            'height': 279,
            'width': 190
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 705,
            'left': 802,
            'height': 243,
            'width': 150
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 657,
            'left': 322,
            'height': 299,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 279,
            'left': 0,
            'height': 220,
            'width': 302
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 271,
            'left': 465,
            'height': 129,
            'width': 117
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        53,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 807,
            'left': 1177,
            'height': 273,
            'width': 191
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 705,
            'left': 802,
            'height': 243,
            'width': 144
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 659,
            'left': 316,
            'height': 297,
            'width': 333
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 274,
            'left': 0,
            'height': 225,
            'width': 298
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 270,
            'left': 456,
            'height': 129,
            'width': 117
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        54,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 807,
            'left': 1167,
            'height': 273,
            'width': 191
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 704,
            'left': 792,
            'height': 247,
            'width': 145
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 650,
            'left': 312,
            'height': 306,
            'width': 332
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 270,
            'left': 0,
            'height': 229,
            'width': 295
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 266,
            'left': 448,
            'height': 129,
            'width': 117
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        55,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 813,
            'left': 1156,
            'height': 267,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 706,
            'left': 783,
            'height': 247,
            'width': 145
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 650,
            'left': 310,
            'height': 304,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 260,
            'left': 0,
            'height': 231,
            'width': 290
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 261,
            'left': 435,
            'height': 129,
            'width': 118
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        56,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 813,
            'left': 1148,
            'height': 267,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 706,
            'left': 784,
            'height': 248,
            'width': 147
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 650,
            'left': 308,
            'height': 304,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 257,
            'left': 0,
            'height': 234,
            'width': 286
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 260,
            'left': 428,
            'height': 129,
            'width': 118
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        57,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 819,
            'left': 1134,
            'height': 261,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 705,
            'left': 776,
            'height': 248,
            'width': 146
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 647,
            'left': 303,
            'height': 304,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 250,
            'left': 0,
            'height': 235,
            'width': 283
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 255,
            'left': 415,
            'height': 128,
            'width': 120
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        58,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 822,
            'left': 1127,
            'height': 258,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 707,
            'left': 775,
            'height': 250,
            'width': 138
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 648,
            'left': 300,
            'height': 304,
            'width': 330
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 246,
            'left': 0,
            'height': 236,
            'width': 279
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 250,
            'left': 406,
            'height': 128,
            'width': 120
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        59,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 825,
            'left': 1120,
            'height': 255,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 709.5,
            'left': 780,
            'height': 249,
            'width': 124
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 645,
            'left': 297.5,
            'height': 306.5,
            'width': 328
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 244,
            'left': 11,
            'height': 238,
            'width': 265
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 248,
            'left': 396,
            'height': 127.5,
            'width': 122
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        60,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 828,
            'left': 1108,
            'height': 252,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 712,
            'left': 785,
            'height': 248,
            'width': 110
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 642,
            'left': 295,
            'height': 309,
            'width': 326
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 238,
            'left': 24,
            'height': 244,
            'width': 248
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 246,
            'left': 386,
            'height': 127,
            'width': 124
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        61,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 832,
            'left': 1099,
            'height': 248,
            'width': 191
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 716,
            'left': 790,
            'height': 241,
            'width': 98
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 640,
            'left': 279.5,
            'height': 310,
            'width': 340
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 233,
            'left': 41,
            'height': 243,
            'width': 227
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 243,
            'left': 379,
            'height': 128,
            'width': 123
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        62,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 836,
            'left': 1088,
            'height': 244,
            'width': 190
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 894,
            'left': 777,
            'height': 63,
            'width': 99
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 638,
            'left': 264,
            'height': 311,
            'width': 354
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 227,
            'left': 43,
            'height': 234,
            'width': 221
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 238,
            'left': 367,
            'height': 128,
            'width': 123
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        63,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 840,
            'left': 1081,
            'height': 240,
            'width': 191
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 892,
            'left': 776,
            'height': 60,
            'width': 94
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 638,
            'left': 256,
            'height': 312,
            'width': 359
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 226,
            'left': 38,
            'height': 225,
            'width': 226
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 235,
            'left': 361,
            'height': 128,
            'width': 123
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        64,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 843,
            'left': 1074,
            'height': 237,
            'width': 190
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 860,
            'left': 723,
            'height': 85.5,
            'width': 131
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 636.5,
            'left': 250,
            'height': 313,
            'width': 363
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 222,
            'left': 31,
            'height': 222,
            'width': 229
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 230,
            'left': 361,
            'height': 131,
            'width': 115
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        65,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 847,
            'left': 1064,
            'height': 233,
            'width': 190
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 828,
            'left': 670,
            'height': 111,
            'width': 168
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 635,
            'left': 244,
            'height': 314,
            'width': 367
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 216,
            'left': 29,
            'height': 190,
            'width': 228
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 227,
            'left': 350,
            'height': 131,
            'width': 115
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        66,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 852,
            'left': 1054,
            'height': 228,
            'width': 192
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 813,
            'left': 662,
            'height': 116,
            'width': 169
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 634.5,
            'left': 239,
            'height': 313,
            'width': 369
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 214,
            'left': 29,
            'height': 163,
            'width': 227
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 222,
            'left': 343,
            'height': 131,
            'width': 115
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        67,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 852,
            'left': 1042,
            'height': 228,
            'width': 193
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 808,
            'left': 651,
            'height': 122,
            'width': 166
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 634,
            'left': 234,
            'height': 312,
            'width': 371
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 209,
            'left': 23,
            'height': 161,
            'width': 229
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 220,
            'left': 337,
            'height': 130,
            'width': 110
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        68,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 852,
            'left': 1035,
            'height': 228,
            'width': 193
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 808,
            'left': 651,
            'height': 122,
            'width': 156
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 623,
            'left': 224,
            'height': 322,
            'width': 377
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 203,
            'left': 24,
            'height': 163,
            'width': 227
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 217,
            'left': 329,
            'height': 130,
            'width': 108
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        69,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 857,
            'left': 1028,
            'height': 223,
            'width': 196
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 802,
            'left': 637,
            'height': 127,
            'width': 158
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 623,
            'left': 220.667,
            'height': 321.667,
            'width': 379.333
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 203,
            'left': 19,
            'height': 153,
            'width': 231
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 213,
            'left': 325,
            'height': 130,
            'width': 108
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        70,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 864,
            'left': 1016,
            'height': 216,
            'width': 198
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 802,
            'left': 629.5,
            'height': 129.5,
            'width': 153
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 623,
            'left': 217.333,
            'height': 321.333,
            'width': 381.667
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 202.5,
            'left': 19.5,
            'height': 142.5,
            'width': 228
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 212,
            'left': 315,
            'height': 124.5,
            'width': 108
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        71,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 864,
            'left': 1009,
            'height': 216,
            'width': 198
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 802,
            'left': 622,
            'height': 132,
            'width': 148
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 623,
            'left': 214,
            'height': 321,
            'width': 384
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 202,
            'left': 20,
            'height': 132,
            'width': 225
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 211,
            'left': 305,
            'height': 119,
            'width': 108
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        72,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 868,
            'left': 994,
            'height': 212,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 798,
            'left': 610,
            'height': 138,
            'width': 165
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 620,
            'left': 203,
            'height': 323,
            'width': 388
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 189,
            'left': 16,
            'height': 137,
            'width': 227
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 212,
            'left': 294,
            'height': 114,
            'width': 108
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        73,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 873,
            'left': 987,
            'height': 207,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 787,
            'left': 603,
            'height': 151,
            'width': 172
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 620,
            'left': 203,
            'height': 323,
            'width': 389
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 183,
            'left': 17,
            'height': 126,
            'width': 223
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 211,
            'left': 286,
            'height': 112,
            'width': 109
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        74,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 873,
            'left': 980,
            'height': 207,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 788,
            'left': 596,
            'height': 150,
            'width': 173
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 615,
            'left': 195,
            'height': 323,
            'width': 389
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 173,
            'left': 10,
            'height': 123,
            'width': 229
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 209,
            'left': 278,
            'height': 112,
            'width': 107
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        75,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 878,
            'left': 968,
            'height': 202,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 788,
            'left': 588,
            'height': 143,
            'width': 175
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 616,
            'left': 188,
            'height': 323,
            'width': 389
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 168,
            'left': 5,
            'height': 113,
            'width': 234
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 213,
            'left': 276,
            'height': 98,
            'width': 98
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        76,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 882,
            'left': 961,
            'height': 198,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 788,
            'left': 582,
            'height': 143,
            'width': 175
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 614,
            'left': 185,
            'height': 326,
            'width': 396
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 168,
            'left': 0,
            'height': 103,
            'width': 237
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 217,
            'left': 276,
            'height': 86,
            'width': 93
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        77,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 882,
            'left': 950,
            'height': 198,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 768,
            'left': 573,
            'height': 174,
            'width': 175
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 613,
            'left': 182,
            'height': 327,
            'width': 399
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 161,
            'left': 0,
            'height': 112,
            'width': 232
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 223,
            'left': 282,
            'height': 55,
            'width': 76
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        78,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 886,
            'left': 944,
            'height': 194,
            'width': 199
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 763,
            'left': 567,
            'height': 179,
            'width': 177
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 613,
            'left': 182,
            'height': 324,
            'width': 399
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 158,
            'left': 0,
            'height': 118,
            'width': 224
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 225,
            'left': 301,
            'height': 47,
            'width': 49
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        79,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 886,
            'left': 936,
            'height': 194,
            'width': 199
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 760,
            'left': 562,
            'height': 181,
            'width': 176
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 611,
            'left': 179,
            'height': 324,
            'width': 399
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 154,
            'left': 0,
            'height': 179,
            'width': 218
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06er0y612emohrkf',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 225,
            'left': 309,
            'height': 41,
            'width': 33
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        80,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 891,
            'left': 925,
            'height': 189,
            'width': 196
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 762,
            'left': 555,
            'height': 181,
            'width': 174
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 608,
            'left': 177,
            'height': 327,
            'width': 401
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 144,
            'left': 0,
            'height': 239,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 338,
            'left': 1352,
            'height': 202,
            'width': 217
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        81,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 891,
            'left': 920,
            'height': 189,
            'width': 196
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 765,
            'left': 552,
            'height': 172,
            'width': 164
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 602,
            'left': 179,
            'height': 328,
            'width': 393
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 140,
            'left': 0,
            'height': 235,
            'width': 208
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 341,
            'left': 1347,
            'height': 202,
            'width': 217
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        82,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 891,
            'left': 910,
            'height': 189,
            'width': 196
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 765,
            'left': 544,
            'height': 173,
            'width': 174
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 602,
            'left': 179,
            'height': 327,
            'width': 393
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 132,
            'left': 0,
            'height': 235,
            'width': 208
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 342,
            'left': 1336,
            'height': 202,
            'width': 217
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        83,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 896,
            'left': 898,
            'height': 184,
            'width': 200
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 769,
            'left': 541,
            'height': 162,
            'width': 169
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 598,
            'left': 175,
            'height': 327,
            'width': 393
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 123,
            'left': 0,
            'height': 238,
            'width': 208
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 343,
            'left': 1331,
            'height': 203,
            'width': 217
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        84,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 896,
            'left': 889,
            'height': 184,
            'width': 203
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 767,
            'left': 537,
            'height': 153,
            'width': 168
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 595,
            'left': 171,
            'height': 327,
            'width': 393
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 117,
            'left': 0,
            'height': 238,
            'width': 208
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 343,
            'left': 1326,
            'height': 203,
            'width': 217
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        85,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 896,
            'left': 879,
            'height': 184,
            'width': 203
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 766,
            'left': 531,
            'height': 160,
            'width': 162
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 585,
            'left': 165,
            'height': 332,
            'width': 400
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 103,
            'left': 0,
            'height': 272,
            'width': 210
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 343,
            'left': 1318,
            'height': 204,
            'width': 215
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        86,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 895,
            'left': 868,
            'height': 185,
            'width': 205
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 759,
            'left': 526,
            'height': 159,
            'width': 161
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 584,
            'left': 164,
            'height': 329,
            'width': 400
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 94,
            'left': 0,
            'height': 274,
            'width': 211
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 343,
            'left': 1312,
            'height': 204,
            'width': 215
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        87,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 892,
            'left': 855,
            'height': 188,
            'width': 206
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 755,
            'left': 517,
            'height': 159,
            'width': 161
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 574,
            'left': 210,
            'height': 334,
            'width': 349
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 78,
            'left': 0,
            'height': 281,
            'width': 215
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 341,
            'left': 1300,
            'height': 204,
            'width': 215
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        88,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 890,
            'left': 849,
            'height': 190,
            'width': 206
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 753,
            'left': 512,
            'height': 163,
            'width': 161
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 569,
            'left': 207,
            'height': 333,
            'width': 352
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 71,
            'left': 0,
            'height': 281,
            'width': 220
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 338,
            'left': 1294,
            'height': 204,
            'width': 215
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        89,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 890,
            'left': 839,
            'height': 190,
            'width': 209
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 746,
            'left': 505,
            'height': 166,
            'width': 170
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 562,
            'left': 203,
            'height': 333,
            'width': 352
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 62,
            'left': 0,
            'height': 281,
            'width': 221
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 337,
            'left': 1288,
            'height': 204,
            'width': 215
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        90,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 892,
            'left': 832,
            'height': 188,
            'width': 203
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 747,
            'left': 498,
            'height': 143,
            'width': 175
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 557,
            'left': 196,
            'height': 333,
            'width': 352
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 47,
            'left': 0,
            'height': 283,
            'width': 217
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 337,
            'left': 1279,
            'height': 205,
            'width': 203
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        91,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 892,
            'left': 830,
            'height': 188,
            'width': 197
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 747,
            'left': 495,
            'height': 141,
            'width': 174
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 549,
            'left': 193,
            'height': 340,
            'width': 353
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 38,
            'left': 0,
            'height': 283,
            'width': 217
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 335,
            'left': 1272,
            'height': 208,
            'width': 207
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        92,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 890,
            'left': 826,
            'height': 190,
            'width': 189
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 739,
            'left': 487,
            'height': 146,
            'width': 145
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 546,
            'left': 187,
            'height': 334,
            'width': 357
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 27,
            'left': 0,
            'height': 285,
            'width': 213
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 334,
            'left': 1263,
            'height': 208,
            'width': 207
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        93,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 893,
            'left': 813,
            'height': 187,
            'width': 196
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 743,
            'left': 478,
            'height': 143,
            'width': 179
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 540,
            'left': 187,
            'height': 343,
            'width': 357
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 17,
            'left': 0,
            'height': 292,
            'width': 213
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 337,
            'left': 1258,
            'height': 208,
            'width': 198
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        94,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 893.5,
            'left': 812,
            'height': 186.5,
            'width': 186
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 735,
            'left': 474,
            'height': 149,
            'width': 177
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 533,
            'left': 184,
            'height': 343,
            'width': 357
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 9,
            'left': 0,
            'height': 292,
            'width': 213
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 337,
            'left': 1251,
            'height': 208,
            'width': 198
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        95,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 894,
            'left': 811,
            'height': 186,
            'width': 176
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 737,
            'left': 465,
            'height': 146,
            'width': 176
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 534,
            'left': 181,
            'height': 340,
            'width': 357
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 293,
            'width': 209
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 336,
            'left': 1240,
            'height': 208,
            'width': 192
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        96,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 898,
            'left': 809,
            'height': 182,
            'width': 171
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 740,
            'left': 460,
            'height': 143,
            'width': 181
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 528,
            'left': 178,
            'height': 340,
            'width': 357
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 288,
            'width': 210
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 336,
            'left': 1234,
            'height': 211,
            'width': 195
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        97,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 896,
            'left': 805,
            'height': 184,
            'width': 165
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 740,
            'left': 455,
            'height': 138,
            'width': 176
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 524.5,
            'left': 178,
            'height': 343.5,
            'width': 357.5
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 278,
            'width': 213
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 337,
            'left': 1223,
            'height': 211,
            'width': 195
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        98,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 893,
            'left': 800,
            'height': 187,
            'width': 163
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 741,
            'left': 449,
            'height': 134,
            'width': 176
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 521,
            'left': 178,
            'height': 347,
            'width': 358
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 268,
            'width': 211
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 337,
            'left': 1219,
            'height': 211,
            'width': 195
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        99,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 893,
            'left': 795,
            'height': 187,
            'width': 160
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 739,
            'left': 449,
            'height': 136,
            'width': 171
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 515,
            'left': 178,
            'height': 345,
            'width': 359
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 266,
            'width': 215
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 339,
            'left': 1214,
            'height': 211,
            'width': 195
        },
        'classifications': []
    }]
}, {
    'frameNumber':
        100,
    'classifications': [],
    'objects': [{
        'featureId': 'ckqcx1d9x06em0y618b90atyy',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 898,
            'left': 786,
            'height': 182,
            'width': 158
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06en0y612vo2feu6',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 738,
            'left': 467,
            'height': 136,
            'width': 146
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06ep0y617a2f5wbs',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': False,
        'bbox': {
            'top': 515,
            'left': 178,
            'height': 345,
            'width': 359
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06eq0y6136uoa1xg',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 0,
            'left': 0,
            'height': 256,
            'width': 217
        },
        'classifications': []
    }, {
        'featureId': 'ckqcx1d9x06es0y61gvx60aqk',
        'schemaId': 'ckqcx1d8h06dr0y61fqb87ecf',
        'title': 'Jellyfish',
        'value': 'jellyfish',
        'color': '#a23030',
        'keyframe': True,
        'bbox': {
            'top': 338,
            'left': 1203,
            'height': 211,
            'width': 195
        },
        'classifications': []
    }]
}]

payload = {
    'ID':
        'ckqcx1dae06ez0y61e7dsh65i',
    'DataRow ID':
        'ckqcx1d6f06c70y61dcap7u95',
    'Labeled Data':
        'https://storage.labelbox.com/cjhfn5y6s0pk507024nz1ocys%2Fb8837f3b-b071-98d9-645e-2e2c0302393b-jellyfish2-100-110.mp4?Expires=1627663739196&KeyName=labelbox-assets-key-3&Signature=JJ8HOcm57D7OclbC795cyjrrA3Q',
    'Label': {
        'frames': 'https://api.labelbox.com/v1/frames/ckqcx1dae06ez0y61e7dsh65i'
    },
    'Created By':
        'msokoloff+11@labelbox.com',
    'Project Name':
        'Sample Video Project',
    'Created At':
        '2021-06-25T22:38:27.000Z',
    'Updated At':
        '2021-06-25T22:38:27.997Z',
    'Seconds to Label':
        25.241,
    'External ID':
        'jellyfish2-100-110.mp4',
    'Agreement':
        -1,
    'Benchmark Agreement':
        -1,
    'Benchmark ID':
        None,
    'Dataset Name':
        'Example Jellyfish Dataset',
    'Reviews': [],
    'View Label':
        'https://editor.labelbox.com?project=ckqcx1d58068c0y619qv7hzgu&label=ckqcx1dae06ez0y61e7dsh65i',
    'Has Open Issues':
        0,
    'Skipped':
        False
}

def round_dict(data):
    for key in data:
        if isinstance(data[key], float):
            data[key] = int(data[key])
        elif isinstance(data[key], dict):
            data[key] = round_dict(data[key])
    return data

def test_video():
    payload['Label'] = annotations
    collection = LBV1Converter.deserialize([payload])
    serialized = next(LBV1Converter.serialize(collection, None))

    assert serialized.keys() == payload.keys()
    for key in serialized:
        if key != 'Label':
            assert serialized[key] == payload[key]
        elif key == 'Label':
            for annotation_a, annotation_b in zip(serialized[key],  payload[key]):
                assert annotation_a['frameNumber'] == annotation_b['frameNumber']
                assert annotation_a['classifications'] == annotation_b['classifications']

                for obj_a, obj_b in zip(annotation_a['objects'], annotation_b['objects']):
                    obj_a = round_dict(obj_a)
                    obj_b = round_dict(obj_b)
                    assert obj_a == obj_b

