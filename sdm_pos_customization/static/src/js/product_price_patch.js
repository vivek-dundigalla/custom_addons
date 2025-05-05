/** @odoo-module **/

import { ProductCard } from "@point_of_sale/app/generic_components/product_card/product_card";
import { patch } from "@web/core/utils/patch";

patch(ProductCard, {
    props: {
        ...ProductCard.props,
        name: String,
        barcode: String,
        lst_price: { type: Number, optional: true },
        qty_available: { type: Number, optional: true },
    },
});
