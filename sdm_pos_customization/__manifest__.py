{
    "name": "POS Customization",
    "version": "18.0.0.0",
    "category": "POS",
    "summary": "POS session product barcode",
    "description": """Displaying product barcode in POS session""",
    "author": "Vivek",
    "company": "Sidmec Technology",
    "maintainer": "Sidmec Technology",
    "license": "LGPL-3",

    "depends": ["point_of_sale",],

    "assets": {
        "point_of_sale._assets_pos": [
            "sdm_pos_customization/static/src/css/styles.css",
            "sdm_pos_customization/static/src/js/product_price_patch.js",
            "sdm_pos_customization/static/src/xml/product_card.xml",
            "sdm_pos_customization/static/src/xml/product_screen.xml",
        ],
    },

    "data": [

    ],

    "installable": True,
    "auto_install": False,
    "models": ["models/pos_config.py"],
}