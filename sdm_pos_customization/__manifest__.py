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
            # JavaScript files
            "sdm_pos_customization/static/src/js/customer_order_receipt.js",
            "sdm_pos_customization/static/src/js/reprint_receipt_screen.js",
            "sdm_pos_customization/static/src/js/product_price_patch.js",  # Price and barcode

            # XML files for POS screens
            "sdm_pos_customization/static/src/xml/order_receipt.xml",
            "sdm_pos_customization/static/src/xml/product_card.xml",  # Custom product card template
            "sdm_pos_customization/static/src/xml/product_screen.xml",  # Custom screen template (optional)

            # CSS files
            "sdm_pos_customization/static/src/css/styles.css",  # Custom styles
        ],


    },

    "data": [

    ],

    "installable": True,
    "auto_install": False,
}