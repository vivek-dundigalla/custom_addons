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
            # JS files
            "sdm_pos_customization/static/src/js/product_price_patch.js",  # Price and barcode
            "sdm_pos_customization/static/src/js/order_line.js", # barcode on receipt
            "sdm_pos_customization/static/src/js/receipt_patch.js", # print custom full receipt

            # XML files for POS screens
            "sdm_pos_customization/static/src/xml/product_card.xml",  # product card template
            "sdm_pos_customization/static/src/xml/product_screen.xml",  # screen template
            "sdm_pos_customization/static/src/xml/order_line.xml", # barcode on receipt
            "sdm_pos_customization/static/src/xml/receipt_template.xml", # custom print full receipt

            # CSS files
            "sdm_pos_customization/static/src/css/styles.css",  # Custom styles
        ],


    },

    "data": [

    ],

    "installable": True,
    "auto_install": False,
}

